# Jev 1.14 frente a Clef-omni: capacidades multimodales

> Fecha de investigación: 2026-10-17

## Resumen

Jev 1.14, de TypeSafe, y Clef-omni, de Cloudflare, convierten entradas en decisiones tipadas en lugar de respuestas de texto libre, pero su alcance multimodal es distinto. Jev 1.14 añade imágenes y preguntas `box` para localizar objetos, aunque estas funciones siguen detrás de una cabecera experimental. Clef-omni procesa texto, JSON, imágenes, audio y vídeo sincronizados en una misma llamada, devuelve probabilidades para opciones definidas por el programa y se ofrece tanto en Workers AI como con pesos abiertos Apache-2.0. Para un flujo exclusivamente visual y experimental, Jev 1.14 puede bastar; para inspección conjunta de imagen, sonido y vídeo, Clef-omni es la opción más completa.

## Ficha técnica

| Campo | Jev 1.14 | Clef-omni |
|-------|----------|-----------|
| Desarrollador | TypeSafe AI | Cloudflare |
| Fecha de anuncio o lanzamiento | 14 de octubre de 2026 | 9 de octubre de 2026 |
| Tipo de recurso | Modelo de decisiones tipadas, System One | Modelo de decisiones multimodal basado en un MoE |
| Licencia y acceso | API de TypeSafe; 42 USD por mil millones de tokens de entrada; las funciones de imagen están en modo experimental | API de Workers AI a 0,15 USD por millón de tokens de entrada; pesos abiertos Apache-2.0 |
| Repositorio o sitio oficial | [Blog de Jev 1.14](https://www.typesafe.ai/blog/jev-1-14) y [documentación](https://docs.typesafe.ai/go/images) | [Documentación de Cloudflare](https://developers.cloudflare.com/workers-ai/models/clef-omni/) y [modelo en Hugging Face](https://huggingface.co/Cloudflare/clef-omni) |

### Prerrequisitos

- **Infraestructura:** Jev requiere una cuenta y una API key de TypeSafe. Clef-omni puede consumirse desde Workers AI o autoalojarse desde Hugging Face.
- **Hardware:** Para autoalojar Clef-omni, el modelo documenta una prueba con una NVIDIA H200 y unos 64 GB de GPU en bfloat16; las imágenes requieren Pillow y audio o vídeo requieren `av`. Jev no exige hardware local cuando se usa su API.
- **Lenguajes y herramientas:** Ambos exponen una API de decisiones. Jev tiene SDKs para Python y JavaScript/TypeScript; Clef-omni ofrece API HTTP y ejemplos para Workers AI, Python y TypeScript.
- **Conocimientos previos:** Hay que modelar preguntas como `noul` (sí/no), `choice` (opciones) o `score` (niveles). Las preguntas deben ser acotadas y accionables.
- **Licencias y suscripciones:** Las imágenes y `box` de Jev requieren `TypeSafe-Danger-Zone-Images: true` y están marcadas como funciones no listas para producción. En Clef-omni, el uso alojado se factura por tokens de entrada; los pesos publicados están bajo Apache-2.0.

## Contexto

### Qué existía antes

Los modelos de decisiones resuelven una tensión común de los LLM: pedir texto y después extraer o validar JSON introduce una etapa de análisis sintáctico y deja al programa expuesto a respuestas fuera del esquema. TypeSafe diseñó System One para evaluar un estado frente a preguntas tipadas y devolver directamente probabilidades, confianza y valores limitados a las opciones declaradas. Cloudflare describe Clef-omni como una ampliación de esa misma familia de modelos de decisión hacia medios que antes exigían una cadena de modelos: separar el vídeo, transcribir el audio y después clasificar el texto.

La noticia local de TLDR AI del 15 de octubre de 2026 ya describía Jev 1.14 como una versión con imágenes, mayor contexto y un nuevo tipo. La misma edición advertía que Jev rinde peor en multimodalidad que con texto. Esa advertencia coincide con la publicación oficial de TypeSafe, que presenta las funciones visuales como experimentales y recomienda probarlas antes de usarlas en producción.

## Explicación técnica

### Qué es y qué problema resuelve

Jev 1.14 recibe un estado textual o estructurado y varias preguntas independientes. Con imágenes activadas, una imagen puede vivir en el estado, en las instrucciones o en los criterios de una pregunta. Esto permite, por ejemplo, comparar una foto con una imagen de referencia o clasificar una escena según ejemplos visuales. Su novedad más específica es `box`: una pregunta devuelve las coordenadas normalizadas `top`, `bottom`, `left` y `right` de un único objeto, además de una confianza. Es útil para encontrar un elemento antes de recortarlo, inspeccionarlo o pasarlo a otro sistema.

La entrada visual de Jev es deliberadamente acotada. La documentación enumera PNG y JPEG estáticos, archivos de hasta 16 MiB por imagen, dimensiones entre 280 y 1568 píxeles y un máximo de 32 MiB para la petición expandida. No acepta audio ni vídeo directamente; estos deben convertirse en imágenes o texto antes de llamar al modelo. La cabecera de imágenes es obligatoria, y la documentación marca tanto las imágenes como `box` como “dreamer-ready”: el formato y la precisión pueden cambiar.

Clef-omni usa un backbone Qwen3-Omni-30B-A3B-Instruct de mezcla de expertos, con 30.000 millones de parámetros totales y 3.000 millones activos. Su cabeza de esquema produce un logit por opción permitida y aplica una distribución de probabilidad por pregunta, sin generar una explicación libre. Clef-omni admite audio y vídeo de forma nativa, además de texto, JSON e imágenes, en una sola petición: el vídeo se muestrea a dos fotogramas por segundo y su pista sonora se procesa junto con los fotogramas cuando está disponible. Jev 1.14 no admite audio ni vídeo nativos y requiere convertirlos en texto o extraer fotogramas.

### Conceptos clave

- **Decisión tipada:** respuesta limitada a una forma conocida por el programa, como una opción, un nivel o una probabilidad booleana.
- **Calibración:** las probabilidades intentan reflejar la incertidumbre del modelo; no garantizan que cada decisión individual sea correcta.
- **MoE:** arquitectura de mezcla de expertos en la que solo una parte de los parámetros se activa para cada entrada.
- **`box`:** rectángulo normalizado que localiza un objetivo en una imagen. Jev devuelve un solo rectángulo por pregunta.
- **Contexto:** presupuesto conjunto para texto, preguntas y representación de los medios. En Clef-omni es de 64.000 tokens; audio y vídeo consumen parte de ese presupuesto.

### Qué lo diferencia

La tabla siguiente resume la diferencia que importa al diseñar el pipeline:

| Capacidad | Jev 1.14 | Clef-omni |
|---|---|---|
| Texto y JSON | Sí | Sí |
| Imágenes | Sí, con cabecera experimental | Sí |
| Audio | No directo | Sí, hasta 4 clips por petición y 300 segundos por clip |
| Vídeo | No directo; hay que extraer fotogramas | Sí, hasta 2 vídeos de 60 segundos; muestreo a 2 fps |
| Localización | `box` para un objetivo por pregunta | Decisiones tipadas; la documentación consultada no presenta un tipo `box` equivalente |
| Salida | `choice`, `score`, `noul` y `box` en Jev 1.14 | `choice`, `score` y `noul` con probabilidades por opción |
| Latencia publicada | La documentación consultada no da una cifra multimodal comparable | Aproximadamente 150 ms para imagen, unos cientos de ms para audio y 1,5 s para un vídeo de 21 s con sonido, según Cloudflare |

Clef-omni no solo acepta más formatos: evita una cascada de ASR, captioning y clasificación cuando la decisión depende de varios canales a la vez. Por ejemplo, puede preguntar simultáneamente si una etiqueta es visible en una foto, si una máquina suena normal en un audio y si un ventilador gira en un vídeo. Jev es más flexible para insertar imágenes dentro de instrucciones o criterios y tiene una ventaja concreta de localización con `box`, pero la propia TypeSafe recomienda dividir las preguntas y no tratar todavía estas funciones como una base estable de producción.

### Limitaciones

Jev 1.14 no cubre audio ni vídeo como entradas nativas, y su modo visual experimental añade una cabecera, límites estrictos de imagen y una advertencia de menor fiabilidad multimodal. Una respuesta `box` siempre devuelve un rectángulo, incluso si el objeto no está presente; TypeSafe recomienda acompañarla de una pregunta `noul` que compruebe la presencia y descartar el rectángulo si la probabilidad es baja.

Clef-omni sí cubre las tres modalidades, pero impone límites de cantidad, tamaño y duración. La documentación acepta hasta cuatro imágenes, cuatro audios y dos vídeos; el audio se convierte en unos 780 tokens por minuto y el vídeo puede consumir hasta unos 15.400 tokens por minuto de imagen, además del audio. Si los medios llenan el contexto de 64k, el estado textual se trunca o la petición falla. El modelo no genera texto libre, por lo que no sustituye a un modelo conversacional cuando se necesita una explicación narrativa.

Los benchmarks publicados no son una prueba aislada de superioridad multimodal. Cloudflare compara Clef-omni con Jev en tareas de decisión generales: por ejemplo, reporta 94,8 frente a 79,7 en BANKING77 y 97,7 frente a 89,3 en CLINC150+OOS, mientras Jev queda por delante en When2Call, 81,0 frente a 63,3, y BRIGHT, 47,5 frente a 42,0. Son resultados del proveedor en su propia suite; no miden de forma directa la calidad de localizar objetos en imágenes ni la comprensión de audio y vídeo.

## Alternativas

| Alternativa | Desarrollador | Acceso | Diferencia principal |
|-------------|---------------|--------|----------------------|
| Jev 1.13 | TypeSafe AI | API de pago | También admite imágenes en el modo experimental, pero no ofrece el tipo `box`, reservado para Jev 1.14. |
| Clef | Cloudflare | API y pesos abiertos | Modelo de decisión con imágenes y vídeo, pero no la entrada de audio nativa de Clef-omni. |
| Clef-flash | Cloudflare | API y pesos abiertos | Variante más barata, a 0,038 USD por millón de tokens de entrada según el anuncio de Cloudflare, con contexto alojado de 24k. |

## Fuentes

| Fuente | Tipo | Fecha de publicación | URL o archivo local |
|--------|------|----------------------|---------------------|
| Jev: For the builders AND dreamers | Blog oficial de TypeSafe | 14 de octubre de 2026 | https://www.typesafe.ai/blog/jev-1-14 |
| Images | Documentación oficial de TypeSafe | Consultada el 17 de octubre de 2026 | https://docs.typesafe.ai/go/images |
| Box | Documentación oficial de TypeSafe | Consultada el 17 de octubre de 2026 | https://docs.typesafe.ai/go/box |
| Models | Documentación oficial de TypeSafe | Consultada el 17 de octubre de 2026 | https://docs.typesafe.ai/models |
| Quick start | Documentación oficial de TypeSafe | Consultada el 17 de octubre de 2026 | https://docs.typesafe.ai/introduction/quickstart |
| Introducing Clef-omni with full multimodality, plus a faster Clef and a cheaper Clef-flash | Blog oficial de Cloudflare | 9 de octubre de 2026 | https://blog.cloudflare.com/clef-faster-cheaper-multimodal |
| clef-omni | Documentación oficial de Cloudflare | Consultada el 17 de octubre de 2026 | https://developers.cloudflare.com/workers-ai/models/clef-omni/ |
| Cloudflare / clef-omni | Repositorio y modelo oficial en Hugging Face | Consultada el 17 de octubre de 2026 | https://huggingface.co/Cloudflare/clef-omni |
| Jev 1.14 ⚡, Grok Voice 3 🎙️, RSI 🔁 | Newsletter local TLDR AI | 15 de octubre de 2026 | app/news/20261015_141330_TLDR.md |
| Deep Learning Weekly: Issue 477 | Newsletter local Deep Learning Weekly | 16 de octubre de 2026 | app/news/20261016_150203_DeepLearningWeekly.md |
