# Muse Wonder y Muse Wonder Full

> Fecha de investigación: 2026-10-15

## Resumen

Muse Wonder y Muse Wonder Full son dos modelos de lenguaje de Meta Superintelligence Labs, anunciados en octubre de 2026 y orientados a agentes: sistemas que ejecutan tareas de varios pasos. Su rasgo distintivo son dos capacidades: Active Memory, que conserva contexto del usuario entre conversaciones, y Active Focus, que mantiene el trabajo hacia un objetivo cuando aparecen obstáculos. En el índice de inteligencia de Artificial Analysis, Muse Wonder Full queda segundo, detrás de Claude Opus 5.5. Ninguno de los dos modelos tiene pesos descargables, así que solo se usan mediante API o suscripción.

## Ficha técnica

| Campo | Detalle |
|-------|---------|
| Desarrollador | Meta Superintelligence Labs (Meta) |
| Fecha de anuncio o lanzamiento | Octubre de 2026 |
| Tipo de recurso | Modelo de lenguaje para agentes |
| Licencia y acceso | Propietario y cerrado: sin pesos descargables. Muse Wonder está en la Meta Model API y en Muse Code; Muse Wonder Full solo está en los planes de Muse Code |
| Precio | Muse Wonder: 4 dólares por millón de tokens de entrada y 20 por millón de salida. Muse Code: planes Power de 50 dólares al mes y Maximum de 200 dólares al mes |
| Ventana de contexto | 1 millón de tokens |
| Entradas y salidas | Entrada de texto, imagen, voz y vídeo; salida de texto (Muse Wonder Full) |
| Sitio oficial | https://research.meta.ai/blog/muse-wonder |

### Prerrequisitos

- **Infraestructura:** una cuenta con acceso a la Meta Model API o a Muse Code. Sin pesos descargables, el modelo no se puede ejecutar en infraestructura propia.
- **Hardware:** ninguno en local; el cómputo lo proporciona Meta.
- **Lenguajes y herramientas:** acceso por API desde cualquier lenguaje que pueda hacer peticiones HTTP, o Muse Code, una aplicación de terminal.
- **Conocimientos previos:** entender qué es un agente y que el precio se calcula por token (un token es un fragmento de texto, aproximadamente tres cuartos de palabra).
- **Licencias y suscripciones:** Muse Wonder Full requiere un plan Power o Maximum de Muse Code.

## Contexto: qué existía antes

Meta había presentado antes Muse Spark. Meta prometió pesos abiertos para Muse Spark, pero según The Neuron todavía no los ha publicado. Muse Wonder (codename Watermelon, según The Rundown AI) es la nueva familia de modelos de Meta y, según el mismo boletín, completa una subida hasta la frontera que hace un año parecía lejana para Meta.

## Explicación técnica

### Qué es y qué problema resuelve

Muse Wonder es el modelo estándar y Muse Wonder Full el de mayor capacidad. Meta destaca dos capacidades:

- **Active Memory:** guarda el contexto importante del usuario entre conversaciones y recupera los detalles relevantes para la tarea actual.
- **Active Focus:** mantiene el trabajo hacia un objetivo difícil probando otros enfoques, resolviendo bloqueos y adaptándose a información nueva. Pide aclaraciones cuando hacen falta y confirma antes de acciones importantes.

Según The Rundown AI, en las pruebas de Meta Muse Wonder Full supera a Claude Opus 5.5 y a GPT-6 Astra en trabajo legal, programación de larga duración y memoria, mientras Opus 5.5 lidera en salud, uso de ordenador y algunas áreas de programación. Meta evalúa Active Focus con FocusBench y la ejecución sostenida con SWE-Marathon, un conjunto de proyectos de software largos.

### Conceptos clave

- **Agente:** sistema que planifica y ejecuta varios pasos para completar una tarea.
- **Índice de Artificial Analysis:** puntuación agregada de capacidad calculada por un tercero independiente a partir de pruebas estandarizadas.

### Qué lo diferencia

- **Rendimiento independiente:** en el índice de Artificial Analysis, Opus 5.5 obtiene 58 puntos, Muse Wonder Full 56, GPT-6 Astra 53 y Muse Wonder 52, según The Neuron, que cita a VentureBeat. The Rundown AI sitúa a Gemini 4 Argon, GPT-6 Astra y Claude Fable 5.1 en 53 puntos.
- **Precio frente a rendimiento:** según The Neuron, Muse Wonder cuesta lo mismo que Opus 5.5 por token, aunque puntúa más bajo. Sonnet 5.5 cuesta la mitad y puntúa más alto que Muse Wonder.
- **Pruebas de Meta:** según The Neuron, en la gráfica de Meta Muse Wonder Full supera a Opus 5.5, Claude Fable 5.1 y GPT-6 Astra en 7 de 14 filas, sobre todo en proyectos largos de software y tareas de agentes legales.

### Limitaciones

- **Sin pesos abiertos:** no se puede desplegar ni ajustar localmente.
- **Acceso restringido:** Muse Wonder Full solo está en los planes de pago de Muse Code.
- **Datos de entrenamiento:** según VentureBeat, citado por The Neuron, Muse Code usa por defecto un modo Contributor que permite a Meta usar lo que el usuario envía para entrenar. El usuario puede desactivarlo, pero solo para envíos futuros. La API no entrena con el contenido.
- **Resultados propios de Meta:** las pruebas de Meta son suyas; la evaluación independiente que se cita aquí es la de Artificial Analysis.
- **Coste en tareas largas:** un desarrollador ejecutó Muse Wonder como agente jugando a Pokémon Red el día del lanzamiento. Según The Neuron, el agente pasó unos 792 turnos en el Bosque Viridian, gastó unos 96 dólares en seis horas y no derrotó al primer líder de gimnasio. Es una sola ejecución, no un benchmark.

## Alternativas y productos equivalentes

| Alternativa | Desarrollador | Acceso | Diferencia principal |
|-------------|---------------|--------|----------------------|
| Claude Opus 5.5 | Anthropic | API y suscripción | Primero en el índice de Artificial Analysis con 58 puntos, al mismo precio por token que Muse Wonder según The Neuron |
| Claude Sonnet 5.5 | Anthropic | API y suscripción | Cuesta la mitad que Muse Wonder y puntúa más alto, según The Neuron |
| GPT-6 Astra | OpenAI | API y suscripción | 53 puntos en el índice de Artificial Analysis; usa una arquitectura de profundidad recurrente, según el boletín local `news.md` |
| Gemini 4 Argon | Google | API y suscripción | 53 puntos en el índice; 2 dólares por millón de tokens de entrada y 10 de salida hasta el 30 de noviembre, según `news.md` |

## Primeros pasos (Get Started)

1. Muse Wonder está disponible en la Meta Model API y en Muse Code, la aplicación de terminal de Meta (según TLDR).
2. Para usar Muse Wonder Full, necesitas un plan Power o Maximum de Muse Code.
3. Antes de pegar documentos de clientes o datos financieros, revisa la configuración de entrenamiento de Muse Code, porque el modo Contributor está activado por defecto (según The Neuron).

## Fuentes consultadas

| Fuente | Tipo | Fecha de publicación | URL o archivo local |
|--------|------|----------------------|---------------------|
| Blog de investigación de Meta: Muse Wonder | Documentación oficial | Octubre de 2026 | https://research.meta.ai/blog/muse-wonder |
| Anuncio de Meta: Introducing Muse Wonder models | Documentación oficial | Octubre de 2026 | https://about.fb.com/news/2026/10/introducing-muse-wonder-models/ |
| Artificial Analysis: Muse Wonder Full (Max) | Benchmark independiente | Consultada el 15 de octubre de 2026 | https://artificialanalysis.ai/models/muse-wonder-full |
| Precios de la API y de los planes de Muse Code | Sitios secundarios | Octubre de 2026 | https://kie.ai, https://techpilot.ai |
| The Neuron: Meta's New Muse Wonder Costs Opus Prices | Newsletter | 2026-10-13 | app/news/20261013_094045_TheNeuron.md |
| The Rundown AI: Meta's Muse Wonder lands at the frontier | Newsletter | 2026-10-13 | app/news/20261013_100842_RundownAI.md |
| TLDR: Meta launches Muse Wonder and Wonder Full | Newsletter | 2026-10-13 | app/news/20261013_104900_TLDR.md |
| Digest de newsletters: Gemini 4 Argon y GPT-6 Astra | Newsletter local | Octubre de 2026 | news.md |
