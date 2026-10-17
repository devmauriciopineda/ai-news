# Cross-Model KV Cache Transfer (caché KV multi-modelo)

> Fecha de investigación: 2026-10-15 · Fuentes: últimos 30 días (desde 2026-09-15); una fuente primaria queda fuera de la ventana, ver nota

## Resumen

La caché KV es la memoria interna que un LLM construye al procesar el contexto (la fase de *prefill*). Cuando un agente pasa una tarea de un modelo a otro, el segundo modelo normalmente recalcula todo ese contexto desde cero. Un paper de NVIDIA, citado por cobertura de octubre de 2026, propone transformar la caché del modelo emisor a la forma del receptor con una proyección lineal de tipo ridge regression, sin volver a ejecutar el *prefill*. Los autores reportan una aceleración de hasta 25 veces en la transición entre dos modelos de la misma familia, con una pérdida de precisión que depende del par de modelos. Importa porque hace viable el enrutamiento entre modelos pequeños y grandes en agentes con contextos largos. No hay una librería oficial verificada para usarlo.

## Ficha técnica

| Campo | Detalle |
|-------|---------|
| Desarrollador | NVIDIA, junto con investigadores académicos. El paper principal figura en arXiv con autoría de NVIDIA según la cobertura consultada; la lista completa de autores no se pudo verificar. |
| Fecha de anuncio o lanzamiento | Paper: agosto de 2026 (arXiv 2608.03893, fuera de la ventana de 30 días). Cobertura de octubre de 2026 (Nexforce, 13-10-2026), dentro de la ventana. |
| Tipo de recurso | Técnica de inferencia (método), no una librería ni un producto. |
| Licencia y acceso | Método descrito en un paper académico. Licencia del código: No verificado (no se encontró repositorio oficial). |
| Repositorio o sitio oficial | Paper: https://arxiv.org/abs/2608.03893. Código oficial: No verificado. |

### Prerrequisitos

- **Infraestructura:** servidor con GPU para ejecutar los modelos. El paper reporta medidas en un nodo de 8 GPU H100 con precisión bf16. El método en sí es ligero.
- **Hardware:** GPU con memoria suficiente para los dos modelos del par, más la caché KV del contexto. Requisitos exactos: No verificado.
- **Lenguajes y herramientas:** no hay código oficial verificado. Una implementación requeriría PyTorch y acceso a las activaciones KV del motor de inferencia.
- **Conocimientos previos:** arquitectura Transformer (atención, claves y valores, RoPE), álgebra lineal y ridge regression, y experiencia con motores de inferencia.
- **Licencias y suscripciones:** No aplica para el método. Los modelos usados (familia Qwen3 en la prueba principal) tienen sus propias licencias.

## Contexto: qué existía antes

En un agente multimodelo, una tarea pasa de un modelo a otro: por ejemplo, un modelo pequeño clasifica y un modelo grande razona. Hasta ahora el modelo receptor tenía dos opciones, ambas malas:

1. **Recalcular el contexto (re-prefill):** recorre de nuevo todos los tokens. El coste crece con la longitud del contexto y con el tamaño del modelo.
2. **Resumir en texto:** el emisor escribe un resumen y el receptor lo lee. Esto necesita generar tokens (lento) y pierde información continua, como las probabilidades intermedias.

Las dos opciones hacen que el ahorro de usar un modelo pequeño se pierda en el salto. Por eso muchos sistemas evitan cambiar de modelo a mitad de tarea.

## Explicación técnica

### Qué es y qué problema resuelve

Según la cobertura del paper, el método tiene tres componentes:

1. **Selección de capas fuente:** para cada capa del modelo receptor se eligen las capas del modelo emisor que mejor la predicen, medidas con el R² de una regresión lineal.
2. **Eliminación de RoPE:** la codificación posicional rotatoria (RoPE) hace que las claves dependan de la posición. Se invierte esa rotación para que el mapeo no dependa de la posición.
3. **Proyección lineal por cabeza de atención:** una ridge regression ajustada una vez, con unas 500 secuencias de calibración, convierte las cachés del emisor en las del receptor. En inferencia, el cambio es una multiplicación de matrices.

Según Nexforce, para Qwen3 14B a Qwen3 32B con 32.768 tokens de contexto, la conversión tarda 278 ms frente a 6.975 ms del *prefill* completo, en 8 H100 con bf16. Esas cifras proceden de la cobertura de octubre; el paper original no se pudo leer en texto.

### Conceptos clave

- **Caché KV:** claves (*keys*) y valores (*values*) que el Transformer guarda por cada token y capa. Permiten no recalcular la atención de tokens anteriores.
- **Prefill y decode:** el *prefill* procesa el contexto de entrada en paralelo y es limitado por cómputo. El *decode* genera tokens uno a uno y es limitado por ancho de banda de memoria.
- **RoPE:** codificación posicional que rota los vectores según la posición del token.
- **Ridge regression:** regresión lineal con regularización L2, que estabiliza la solución cuando las variables están correlacionadas.

### Qué lo diferencia

- **Frente al re-prefill:** evita recalcular el contexto. Según la cobertura, el coste del mapeo es independiente de la longitud del contexto, a diferencia del *prefill*.
- **Frente al resumen en texto:** transfiere estados continuos en lugar de texto, lo que evita generar tokens y no pierde las distribuciones intermedias.
- **Resultados reportados:** 73 % a 98 % de precisión retenida en cuatro de seis pares de modelos. Dos pares (Ministral 3B a 14B y 8B a 14B) caen al 41–44 % con el mapeo lineal. Un mapeo no lineal (MLP) recupera entre 24 y 37 puntos en esos pares, según Nexforce.

### Limitaciones

- **Misma familia de modelos:** el mapeo funciona en pares con formatos de caché compatibles. Entre familias distintas no hay resultados verificados.
- **Compatibilidad impredecible:** no hay un criterio previo para saber qué par funcionará. Hay que medirlo con una evaluación propia.
- **Pérdida de precisión:** la retención de precisión no es del 100 %, y depende de la tarea.
- **Calibración:** el mapeo se ajusta con datos de calibración y debe repetirse si cambian los modelos.
- **Madurez:** es un resultado de investigación. Faltan implementaciones de producción verificadas.

## Alternativas y productos equivalentes

| Alternativa | Desarrollador | Acceso | Diferencia principal |
|-------------|---------------|--------|----------------------|
| LMCache | Proyecto de código abierto (LMCache) | Apache-2.0 (verificado en el repositorio) | Reutiliza la caché KV entre motores de inferencia y entre sesiones. Reduce el *prefill* repetido, pero no transfiere cachés entre modelos distintos. Cifra de estrellas y uso en producción: No verificado. |
| Cache-to-Cache (C2C) | Fu et al. (ICLR 2026) | Paper académico, código: No verificado | Fusiona las cachés de dos modelos especialistas mediante una capa neuronal aprendida, en lugar de una regresión lineal. Según Nexforce, 2,5 veces de aceleración frente a texto intermedio. El paper es de 2025, fuera de la ventana. |
| Resumen en texto entre modelos | Enfoque general, sin autor | Según el modelo usado | Sin infraestructura especial, pero añade tokens de salida y pierde información continua. |

## Primeros pasos (Get Started)

No se encontró una librería o SDK oficial verificado para este método, por lo que no se incluye código. Pasos para probarlo sobre un caso propio:

1. Lee el paper en https://arxiv.org/abs/2608.03893 y revisa si publica código o material suplementario. Ese repositorio, si existe, sería la fuente oficial para empezar.
2. Elige dos modelos de la misma familia, por ejemplo un modelo pequeño y otro grande de una misma serie.
3. Reúne unos cientos de secuencias representativas de tu dominio para calibrar el mapeo. El paper usa 500 secuencias de 1.024 tokens de FineWeb-Edu.
4. Mide en tu tarea la precisión del receptor con y sin mapeo, y la latencia de la transición frente al *prefill*. No asumas los resultados del paper.
5. Si la precisión cae demasiado en tu par de modelos, prueba un mapeo no lineal o mantén el resumen en texto para esa transición.

Si quieres reutilizar caché entre sesiones o motores (sin cambiar de modelo), LMCache es el punto de partida más documentado: https://docs.lmcache.ai/.

## Notas sobre la verificación

- **Ventana temporal:** el paper principal (arXiv 2608.03893) y la cobertura de agosto de 2026 quedan fuera de los últimos 30 días. Se usan solo para identificar el método. Los datos numéricos provienen de Nexforce (13-10-2026), que cita el paper. El PDF no se pudo leer en texto, así que las cifras no están verificadas contra el paper.
- **Cifra de 25 veces:** procede del paper y de sus citas. Se da solo para la transición entre Qwen3 14B y 32B con 32.768 tokens, no como una cifra general.
- **Fuente secundaria sin fecha:** el artículo de Hashnode (miainflorence) describe el método, pero no muestra fecha de publicación. No se usa como fuente para ningún dato.
- **Autoría:** la lista de autores del paper no se pudo confirmar.
- **Código oficial:** No verificado. Una búsqueda no devolvió repositorio oficial.

## Fuentes consultadas

| Fuente | Tipo | Fecha de publicación | URL |
|--------|------|----------------------|-----|
| Cross-model KV cache: agent latency falls (Nexforce) | Blog (prensa técnica) | 2026-10-13 | https://nexforce.ai/en/blog/kv-cache-transfer-models-ai-agents |
| Cross-Model KV Cache Transfer in LLM Families (arXiv 2608.03893) | Paper | 2026-08 (fuera de ventana) | https://arxiv.org/abs/2608.03893 |
| Cache-to-Cache (arXiv 2510.03215, ICLR 2026) | Paper | 2025-10 (fuera de ventana) | https://arxiv.org/abs/2510.03215 |
| Welcome to LMCache (documentación) | Documentación oficial | Sin fecha visible | https://docs.lmcache.ai/ |
| LMCache, licencia Apache-2.0 | Repositorio oficial | Sin fecha visible | https://github.com/LMCache/LMCache |
