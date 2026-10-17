# 🌍 image-blaster turns one photo into a 3D world in 5 min

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Mon, 5 Oct 2026 13:30:00 +0000

AlphaSignal
Stay updated with today's top AI news, papers, and repos.
Signup
|
Work With Us
|
Follow on X
|
Archive
Hey Mauricio,
Two stories dropped this week that share the same quiet message:
the infrastructure layer is becoming the moat.
Prime Intellect didn't just ship an inference platform. They proved that owning your stack, from GPU to API, changes what's possible. 600B tokens daily, near-zero tool-call errors. That's not a demo.
Meanwhile, Meta's Muse Spark co-authored six math papers solving open research problems, through a regular chat window. No custom scaffold. The frontier is moving faster than the tooling.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 27 sec
Top Repo
▸ New open-source tool turns any photo into a
full 3D world
in five minutes
Redis
▸
R
e
d
i
s
A
g
e
n
t
M
e
m
o
r
y
h
i
t
s
8
6
.
5
%
a
c
c
u
r
a
c
y
.
Top Repo
▸ Open-source tool lets Claude agents
code your repos
inside Minecraft
Google Cloud
▸
G
o
o
g
l
e
C
l
o
u
d
a
t
G
T
C
B
e
r
l
i
n
Top Model
▸ Aleph Alpha open-sources 78B model with only 3.5B
active params
and 1M token context
Signals
1. This writing standard cuts
AI agent output
slop in the terminal
2. New MCMC trick makes
supervised finetuning generalize
better than reinforcement learning
3. Wavestone
tears apart
11 coding agents and finds the same 7-part blueprint
4. New RL training trick
cuts decoding compute
2.5x by trusting the critic
5. Cua ships free source-available tool letting AI agents run
real desktop apps
on your Mac
Top Repo
New open-source tool turns any photo into a full 3D world in five minutes
18,827 Likes
image-blaster
just dropped on GitHub and it does exactly what it sounds like: drop in one photo, get back a full 3D world.
Here is what comes out the other side:
Explorable 3D environment
with real depth and geometry you can navigate
Individual object meshes with physics colliders, exported as .glb or .obj files
Ambient sound and object-specific sound effects, auto-generated
Works directly in Unity, Unreal, Godot, Blender, and Three.js
Under the hood, it runs as a
Claude Code skill
, meaning Claude acts as the agent that coordinates everything. It picks which objects to make 3D, removes them from the background, renders them with Hunyuan 3D, and adds audio via ElevenLabs. All in
under 5 minutes
.
To try it: git clone the repo, drop an image into the input folder, give Claude your World Labs and FAL API keys, and ask it to blast. Each provider has free trial credits to start.
READ MORE
forward →
Presented by Redis
Redis Agent Memory hits 86.5% accuracy.
Building agents that need to remember across sessions?
Redis Agent Memory
combines raw conversation evidence with extracted facts, scoring 86.5% accuracy on LongMemEval at about $0.07 per session in modeled LLM costs.
Redis tested the approach across 500 questions covering preferences, changing facts, and reasoning across sessions.
See how the memory strategies compare, where retrieval succeeds or fails, and the accuracy, cost, and latency trade-offs before choosing your agent’s memory stack.
READ THE REPORT
partner with us →
Top Repo
Open-source tool lets Claude agents code your repos inside Minecraft
11,718 Likes
AgentCraft
turns your coding workflow into a Minecraft studio you can literally walk around in. Forget staring at a terminal. Your AI teammates exist as characters in a 3D world.
Here is how it flows. You type a goal.
Marlow
(the lead agent) breaks it into tasks. Worker agents then code in parallel, each in their own isolated copy of your repo so they never conflict. When an agent hits a decision only you should make, it physically walks over and asks you in-game.
The safety model is solid:
Nothing is ever pushed. Agents have zero git network access.
Risky commands trigger an in-game permission prompt showing exactly what gets allowed.
You review the real code diff inside the game, then hit merge.
To get started you need Minecraft Java Edition,
Java 25
, Node 22+, and a Claude API key. Point it at any existing repo and go. Fully open-source, MIT licensed.
READ MORE
forward →
Presented by Google Cloud
Google Cloud at GTC Berlin
Agentic AI demands more than raw compute, it requires a fully optimized, flexible stack.
With our
AI Hypercomputer architecture
, we provide the scale, resilience and efficiency you need to turn your most ambitious AI visions into reality.
See multi-agent demos and explore sessions on Sovereign AI.
CONNECT AT GTC
partner with us →
Top Model
Aleph Alpha open-sources 78B model with only 3.5B active params and 1M token context
5,119 Likes
Aleph Alpha just dropped
Kolibri-1
, a European open-weight reasoning model you can run on your own hardware. The weights are yours under
Apache 2.0
, so no usage restrictions.
Here is what makes it interesting architecturally: it uses a Mixture-of-Experts design, meaning the model has 78B total parameters but only activates
3.46B per token
. Think of it like a team of specialists where only the relevant ones show up for each task. You get big-model quality at small-model inference cost.
What you can actually build with it:
Process up to
1M tokens
of context, great for large documents or long codebases
Agentic tool calling with reasoning mode at low, medium, or high effort levels
Strong German and English support, purpose-built for both languages
RAG pipelines, coding, and multi-step reasoning tasks
To run it, install the aleph-alpha-inference package and serve via vLLM. It exposes an OpenAI-compatible API, so you can drop it into existing setups. Minimum hardware is 2x A100 80GB or 1x H200.
READ MORE
forward →
Signals
1
This writing standard cuts AI agent output slop in the terminal
3,200 Likes
2
New MCMC trick makes supervised finetuning generalize better than reinforcement learning
2,132 Likes
3
Wavestone tears apart 11 coding agents and finds the same 7-part blueprint
1,331 Likes
4
New RL training trick cuts decoding compute 2.5x by trusting the critic
701 Likes
5
Cua ships free source-available tool letting AI agents run real desktop apps on your Mac
2,471 Likes
At Alpha Signal, our mission is to build a sharp, engaged community focused on AI, machine learning, and cutting-edge language models, helping over 300,000 developers stay informed and ahead. We're passionate about curating the best in AI, from top research and trending technical blogs to expert insights and tailored job opportunities. We keep you connected to the breakthroughs and discussions that matter, so you can stay in the loop without endless searching. We also work closely with partners who value the future of AI, including employers and advertisers who want to reach an audience as passionate about AI as we are.
Our partnerships are based on shared values of ethics, responsibility, and a commitment to building a better world through technology.Privacy is a priority at Alpha Signal. Our Privacy Policy clearly explains how we collect, store, and use your personal and non-personal information. By using our website, you accept these terms, which you can review on our website. This policy applies across all Alpha Signal pages, outlining your rights and how to contact us if you want to adjust the use of your information. We're based in the United States. By using our site, you agree to be governed by U.S. laws.
Looking to promote your company, product, service, or event to 300,000+ AI developers?
WORK WITH US
How was today's email?
Awesome
Decent
Not Great
unsubscribe_me(): return True
{"AlphaSignal": "214 Barton Springs Rd, Austin, USA"}

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=f048a35cb731c6f8