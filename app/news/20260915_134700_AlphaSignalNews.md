# Frank Fly Brain 🦟, ByteDance Self-Improving AI 🔄, Bolt Open Model 💡

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 15 Sep 2026 13:47:00 +0000

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
Today's news shares a quiet theme:
we're rethinking how AI learns, at every level.
Sakana trains 1000-layer nets without backprop. ByteDance maps a 5-stage path to AI that rewrites itself. Bolt pays users in usage to crowdsource a trillion-parameter open model. Each story, in its own way, asks: what if the training process itself is the next frontier?
We're not just scaling models anymore. We're redesigning the engine.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 33 sec
Top Repo
▸ Frank wires a 166,700-neuron
fruit fly brain
model into a walking robot
WorkOS
▸
S
t
o
p
f
a
k
e
a
c
c
o
u
n
t
s
b
e
f
o
r
e
t
h
e
y
b
u
r
n
t
o
k
e
n
s
Top Repo
▸ New looped transformer design gives language models
unlimited reasoning depth
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
'
s
E
n
t
e
r
p
r
i
s
e
A
I
A
g
e
n
t
A
r
c
h
i
t
e
c
t
u
r
e
Top Repo
▸ Developer builds
open-source Codex clone
that runs on your existing ChatGPT plan
Signals
1. shadcn releases a linter that
stops AI agents
from breaking your design system
2.
Attio:
Attio's MCP server connects Claude Code, n8n & Notion straight to your CRM, so every agent has context to act on
3. ByteDance and Tsinghua map a 5-stage path to
self-improving AI
that rewrites itself
4. Free open-source tool
auto-generates TikTok
and Shorts videos from a single keyword
5. The growing divide between developers with
unlimited AI tokens
and those who can't afford $20 a month
6.
Uncensored Qwen3 8B
vision model hits 665K downloads running fully local
Top Repo
Frank wires a 166,700-neuron fruit fly brain model into a walking robot
12,785 Likes
Scientists at Google and HHMI Janelia just published the first complete wiring map of a fruit fly's nervous system:
166,700 neurons
and
125 million connections
. Think of it like a blueprint of every wire in a tiny biological computer.
Someone took that blueprint, simulated it in software, and plugged it into a physical walking robot called a Strandbeest. The simulated brain's activity gets translated into motor commands that move the legs. Before this robot, the same brain played Doom and Chrome Dino.
Here's the honest part: this is not a living brain.
A connectome is a snapshot of dead wiring
, not a mind. The simulation uses simplified neuron models, so it's an approximation running on top of real biological structure.
What this opens up for you:
Wire the brain to any robot using
UDP motor commands
over a network
Feed camera or sensor input as simulated sensory signals
Swap in your own robot, including a robot vacuum
The full open-source bridge code is on GitHub at Frankweb33/flybrain-robot-bridge.
READ MORE
forward →
Presented by WorkOS
Stop fake accounts before they burn tokens
Free-tier abuse gets expensive fast in an AI product. One person can cycle through email addresses, devices, and trials while your app keeps issuing credits and paying inference costs. Blocking a single address only slows them down.
WorkOS Radar
checks device, email, and network signals at signup, then returns a risk verdict before the account reaches your product.
You can block obvious abuse, step up suspicious users, and review the evidence behind each decision without maintaining rules or deny lists.
SEE RADAR
partner with us →
Top Repo
New looped transformer design gives language models unlimited reasoning depth
7,254 Likes
Normal AI models (transformers) have a
fixed number of layers
, like a stack of floors in a building. More thinking? You generate more tokens. That costs more money every time.
The
Recurrent Looped Transformer (RLT)
flips this. Instead of a fixed stack, the model loops its layers across every token it processes, building a growing internal memory as the sequence gets longer. The reasoning depth scales with the sequence, not the architecture.
Three things it targets:
Deeper reasoning over time
without generating extra tokens
Hardware-friendly design with parallel encoding and memory reuse
Cleaner AI training, where the model behaves the same during learning and real use
Important caveat: this is a
design spec, not a tested product
. Early experiments show mixed results, and the paper itself says efficiency and scaling gains need future validation. Worth watching, not shipping.
READ MORE
forward →
Presented by Google Cloud
Google Cloud's Enterprise AI Agent Architecture
Learn how to accelerate agentic workloads with G4 VMs accelerated by NVIDIA RTX Pro GPUs through Cloud Run and GKE.
This session
includes a live multi-agent drug discovery demo running on the Gemini Enterprise Agent Platform. Watch the complete episode on YouTube.
WATCH THE DEMO
partner with us →
Top Repo
Developer builds open-source Codex clone that runs on your existing ChatGPT plan
3,317 Likes
Codex is OpenAI's AI coding agent that works directly on your project files. Cool, but it has a separate usage limit. Once you hit it, you're stuck.
Chat On Steroids
flips that. It uses your regular ChatGPT conversation instead, so it does not consume your Codex quota at all. Same power, different bucket.
Here's what you can actually do with it:
Read and edit files directly in your project folder
Send corrections while work is still running
Split tasks across
multiple agents
working in parallel
Resume a session in a fresh chat without losing context
To get started: install CoS, approve your project folder in Settings, then connect it through ChatGPT's Developer mode. Pairing is automatic.
You need Windows, macOS, or Linux, plus Chrome or Edge with a ChatGPT account that supports Developer mode. The code is open source on GitHub.
READ MORE
forward →
Signals
1
shadcn releases a linter that stops AI agents from breaking your design system
2,520 Likes
2
Attio's MCP server connects Claude Code, n8n & Notion straight to your CRM, so every agent has context to act on
Presented by Attio
3
ByteDance and Tsinghua map a 5-stage path to self-improving AI that rewrites itself
784 Likes
4
Free open-source tool auto-generates TikTok and Shorts videos from a single keyword
2,322 Likes
5
The growing divide between developers with unlimited AI tokens and those who can't afford $20 a month
2,036 Likes
6
Uncensored Qwen3 8B vision model hits 665K downloads running fully local
2,263 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=0f2b79151c7087e6