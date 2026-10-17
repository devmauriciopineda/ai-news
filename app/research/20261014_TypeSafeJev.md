# TypeSafe Jev

> Fecha de investigación: 2026-10-14 · Fuentes: últimos 30 días (desde 2026-09-14)

## Resumen

Jev es un modelo de TypeSafe AI que no genera texto: devuelve decisiones tipadas (una opción de una lista, una puntuación en una escala ordenada o un sí/no) con probabilidades asociadas. TypeSafe lo presenta como el primer modelo de su familia "System One", pensado para tareas de clasificación y enrutamiento dentro de sistemas de agentes, donde basta con una decisión y no hace falta una respuesta conversacional completa. Según el fabricante, reduce latencia y coste frente a un LLM generativo; esas cifras no están verificadas de forma independiente. Su lanzamiento fue el 15 de septiembre de 2026 y el acceso se abrió sin lista de espera el 21 de septiembre de 2026, según una fuente de terceros.

## Ficha técnica

| Campo | Detalle |
|-------|---------|
| Desarrollador | TypeSafe AI (typesafe.ai). Financiación de Serie A de 870 M$ a una valoración de 7.500 M$, liderada por a16z, con participación de Sequoia y DCVC (blog oficial "Series AI"). |
| Fecha de anuncio o lanzamiento | 15-09-2026 según fuentes de terceros (explainx.ai). El blog oficial dice "hoy" sin fecha visible. Acceso general sin lista de espera: 21-09-2026 (explainx.ai, cita un post en X de TypeSafe). |
| Tipo de recurso | Modelo de IA accesible por API, con SDK oficiales para Python y JavaScript. |
| Licencia y acceso | Modelo y API propietarios, de pago por uso: 0,042 $ por millón de tokens de entrada; los tokens de salida son gratuitos (blog oficial). Cuenta nueva con 5 $ de crédito gratuito, que TypeSafe estima en unos 120 millones de tokens (explainx.ai). Los SDK son open source bajo licencia MIT (archivo LICENSE del repositorio oficial). Términos de servicio de la API: No verificado. |
| Repositorio o sitio oficial | Sitio: https://typesafe.ai · Documentación: https://docs.typesafe.ai · SDK Python: https://github.com/typesafe-ai/typesafe-sdk-python · SDK JS: https://github.com/typesafe-ai/typesafe-sdk-js |

### Prerrequisitos

- **Infraestructura:** conexión a Internet y acceso a la API de TypeSafe. No necesita GPU local ni servidor propio.
- **Hardware:** cualquier equipo capaz de ejecutar Python o Node.js.
- **Lenguajes y herramientas:** Python 3.10 o superior (instalación con `uv add typesafe-sdk`) o Node.js 20 o superior (`npm install @typesafe-ai/sdk`). Las versiones mínimas provienen de la documentación de instalación de cada SDK, que no se revisó completa.
- **Conocimientos previos:** saber escribir una llamada a una API y entender qué es una clasificación. No requiere experiencia en entrenamiento de modelos.
- **Licencias y suscripciones:** una API key de TypeSafe en la variable de entorno `TYPESAFE_API_KEY`. Hay crédito gratuito inicial; después, facturación por uso.

## Contexto: qué existía antes

En muchos sistemas con agentes, una decisión pequeña (¿a qué área va este ticket?, ¿este mensaje es urgente?, ¿qué herramienta debe usar el agente a continuación?) se resuelve con un LLM generativo. El modelo produce texto libre y después ese texto se interpreta, a menudo con expresiones regulares o con salida en JSON. Este enfoque tiene tres problemas:

1. **Latencia:** el modelo genera tokens uno a uno, aunque la respuesta sea una sola palabra de un conjunto cerrado.
2. **Coste:** se paga por los tokens de salida, y con frecuencia se pagan también los de razonamiento.
3. **Fiabilidad del formato:** la salida libre puede salirse del formato esperado, y el parseo de ese texto introduce fallos.

Las salidas estructuradas de los LLM (JSON Schema) reducen el tercer problema, pero no el primero ni el segundo. Los clasificadores propios, entrenados con datos etiquetados, son rápidos y baratos, pero requieren datos, entrenamiento y mantenimiento. Jev busca un punto intermedio: una decisión calibrada, sin texto, expuesta como un tipo de dato.

## Explicación técnica

### Qué es y qué problema resuelve

Jev recibe dos entradas: un `state` (texto o JSON con el contexto) y una lista de `questions` tipadas. Devuelve, para cada pregunta, una distribución de probabilidad sobre las opciones posibles, además de una medida de confianza. Las preguntas se responden en paralelo, y cada una se evalúa de forma independiente. El límite de entrada documentado es de 64.000 tokens.

Según la documentación oficial y el artículo de Wikipedia dedicado al modelo, los tipos de pregunta son:

- **`Choice`:** elegir una opción de una lista cerrada (por ejemplo, `billing`, `technical`, `other`).
- **`score`:** puntuar en una escala ordenada.
- **`noul`:** responder sí o no a una afirmación.

El resultado es un objeto con los campos `choices` (y sus equivalentes para las otras preguntas) que contienen la decisión elegida y las probabilidades. El SDK de Python lo expone como `response.choices["category"].choice`.

El problema que resuelve es el de obtener una decisión de un LLM sin pagar y esperar la generación de texto libre, y de hacerlo como un valor que el código puede usar directamente.

### Conceptos clave

- **Salida tipada:** la respuesta tiene un esquema fijo (opción, puntuación o booleano), no texto libre. El código no necesita parsear nada.
- **Distribución de probabilidad:** para cada pregunta, el modelo asigna una probabilidad a cada opción. La decisión es la de mayor probabilidad, y la distribución indica cuánta seguridad tiene el modelo.
- **Calibración:** una probabilidad calibrada significa que, si el modelo dice 80 %, la opción resulta correcta aproximadamente el 80 % de las veces. TypeSafe declara que Jev está calibrado. Esa afirmación no se ha verificado con un benchmark independiente.
- **Modelo "System One":** TypeSafe llama así a esta familia por analogía con el Sistema 1 de Kahneman, es decir, respuestas rápidas e intuitivas frente al razonamiento deliberado del Sistema 2 de los LLM generativos.

### Qué lo diferencia

- **Sin generación de texto:** elimina el coste de los tokens de salida y la latencia de generarlos. El fabricante indica tiempos de 70 a 500 ms y un precio de entrada de 0,042 $ por millón de tokens.
- **Preguntas en paralelo e independientes:** varias decisiones sobre el mismo estado se obtienen en una sola llamada. La contrapartida es que las preguntas no razonan entre sí.
- **Cifras del fabricante:** la página principal muestra "193,6 veces más rápido" y "444,6 veces más barato", y un blog oficial habla de 40 a 200 veces más rápido en tareas de tipo System One. Son comparaciones del propio proveedor, frente a un modelo generativo de referencia, con condiciones no publicadas en el texto que se consultó. No están verificadas de forma independiente.

### Limitaciones

- **Solo decisiones:** no sirve para generar texto, resúmenes, código ni explicaciones. Para eso sigue siendo necesario un LLM generativo.
- **Preguntas independientes:** si una decisión depende de otra, hay que encadenar llamadas o diseñar el estado para que incluya ese contexto.
- **Límite de contexto:** 64.000 tokens de entrada por llamada.
- **Dependencia de un proveedor cerrado:** el modelo y la API son propietarios. Los SDK son MIT, pero el modelo no se puede ejecutar en local.
- **Datos de adopción sin confirmar:** ver la sección de fuentes y la sección de notas.
- **Madurez:** el lanzamiento es de hace menos de un mes. Faltan benchmarks independientes y casos de producción documentados fuera del fabricante.

## Alternativas y productos equivalentes

Las alternativas siguientes son categorías de solución y no se han revisado con fuentes publicadas en la ventana de 30 días. Son descripciones generales, no comparativas verificadas.

| Alternativa | Desarrollador | Acceso | Diferencia principal |
|-------------|---------------|--------|----------------------|
| LLM generativo con salida estructurada (JSON Schema) | Varios proveedores de LLM | De pago por tokens, según el proveedor | Genera texto y luego lo convierte en estructura. Tiene más latencia y coste de salida que Jev, pero entiende tareas abiertas. |
| Clasificador propio (fine-tuning de un modelo pequeño) | Equipo propio, con modelos de código abierto | Open source o autoalojado | Muy barato y rápido en local, pero requiere datos etiquetados, entrenamiento y mantenimiento. |
| `system-one-adapter-python` | TypeSafe AI (repositorio oficial, 394 estrellas) | Open source | Adaptador oficial del ecosistema de Jev. Su función exacta no se ha revisado en detalle. |

## Primeros pasos (Get Started)

1. Crea una cuenta en [console.typesafe.ai](https://console.typesafe.ai) y obtén una API key. La cuenta nueva incluye 5 $ de crédito.
2. Guarda la clave en la variable de entorno `TYPESAFE_API_KEY`.
3. Instala el SDK de Python con `uv add typesafe-sdk` (o con `pip install typesafe-sdk`). Para HTTP/2, usa `typesafe-sdk[http2]`.
4. Ejecuta el siguiente ejemplo, tomado del README oficial del repositorio:

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
                criteria={"billing": None, "technical": None, "other": None},
            ),
        },
    )

print(response.choices["category"].choice)
```

Para seguir aprendiendo, consulta la [documentación del SDK de Python](https://docs.typesafe.ai/sdk/python/) y la [guía de inicio rápido](https://docs.typesafe.ai/introduction/quickstart).

## Notas sobre la verificación

- **Adopción "viral" en miles de repositorios:** No verificado. La organización oficial `typesafe-ai` tiene 9 repositorios públicos. Sus estrellas son: `skills` 2.696, `system-one-adapter-python` 394, `typesafe-sdk-python` 292 y `typesafe-sdk-js` 276. Una búsqueda de código en GitHub devolvió unos 300 archivos con identificadores del SDK. Ninguna cifra demuestra "miles de repositorios" ni un uso masivo.
- **Porcentaje de adopción en el Fortune 500:** No verificado. El artículo de a16z habla del 25 %; el blog oficial "Series AI" habla de "un tercio". Las dos cifras proceden del fabricante o de sus inversores y se contradicen entre sí.
- **Cifras de mercado:** la afirmación de "un billón de tokens en 3 días" procede de a16z y no se ha comprobado en una fuente independiente.
- **Ruido de fuentes no oficiales:** hay sitios no oficiales (typesafe-jev.com, jevnotes.com, jevmodel.org) con tablas de benchmark sin fuente trazable. No se han usado para ningún dato.

## Fuentes consultadas

| Fuente | Tipo | Fecha de publicación | URL |
|--------|------|----------------------|-----|
| Introducing System One Models & Jev | Blog oficial | 2026-09-15 (según terceros; el blog no muestra fecha) | https://typesafe.ai/blog/introducing-system-one-models-and-jev |
| Series AI | Blog oficial | No verificada | https://typesafe.ai/blog/series-ai |
| Página principal de TypeSafe AI | Sitio oficial | Sin fecha visible | https://typesafe.ai |
| Documentación: introducción y quickstart | Documentación oficial | Sin fecha visible | https://docs.typesafe.ai/introduction |
| Repositorio typesafe-sdk-python (MIT) | Repositorio oficial | Sin fecha de release visible | https://github.com/typesafe-ai/typesafe-sdk-python |
| Repositorio typesafe-sdk-js | Repositorio oficial | Sin fecha de release visible | https://github.com/typesafe-ai/typesafe-sdk-js |
| Paquete typesafe-sdk | Registro oficial (PyPI) | Sin fecha verificada | https://pypi.org/project/typesafe-sdk/ |
| Lanzamiento de acceso general sin lista de espera | Terceros (explainx.ai) | 2026-09-21 | https://www.explainx.ai/blog/jev-general-availability-no-waitlist-2026 |
| Investing in TypeSafe AI | Inversor (a16z) | No verificada | https://a16z.com/announcement/investing-in-typesafe-ai/ |
| Jev (AI model) | Secundaria (Wikipedia) | No verificada | https://en.wikipedia.org/wiki/Jev_(AI_model) |
