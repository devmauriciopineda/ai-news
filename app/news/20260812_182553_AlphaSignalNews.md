# ChatGPT lands on Linux with Codex while Claude's hidden thinking
 expos

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Wed, 12 Aug 2026 18:25:53 +0000

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
AI is moving to your desktop, fast. OpenAI just landed on Linux, Unsloth ships local training for everyone, and the whole industry is racing to own your machine.
The irony? Just as agents get closer to your files and repos, researchers found that the "encrypted" reasoning those same agents produce is basically a shared secret anyone can decode. Closer access, bigger blast radius.
We're watching a platform war play out in real time, and security is already playing catch-up.
In Partnership with
·
AlphaSignal Workshop: Harness Orchestration: What Comes After Agentic Loop and Graph Engineering | August 20, 2026
Loop and graph engineering are weeks old and already hitting a ceiling. Any system drawn as a DAG can't go further than what you imagined before it started.
Orchestration is what's past that: hundreds of harnesses working as one system, deciding their own shape as they go.
Join AlphaSignal x AgentField on Aug 20 @ 10am PT to learn the handful of arrangements that cover most real systems and see exactly how we used them to build our open source code review tool (currently state of the art).
Save your seat today.
Register Now
Summary
Read time: 6 min 58 sec
Top Paper
▸ Security flaw lets anyone
steal hidden reasoning
from Claude, GPT, and Gemini
Tiger Data
▸
O
n
e
D
a
t
a
b
a
s
e
:
M
e
t
r
i
c
s
,
E
m
b
e
d
d
i
n
g
s
,
a
n
d
A
n
a
l
y
t
i
c
s
Top News
▸ OpenAI
drops ChatGPT desktop
app for Linux on Ubuntu, Debian, and Fedora
Upstage AI
▸
A
n
A
g
e
n
t
M
o
d
e
l
T
h
a
t
A
c
t
u
a
l
l
y
F
i
n
i
s
h
e
s
t
h
e
J
o
b
Top News
▸ Unsloth releases
open-source desktop app
to run and train models 2x faster locally
Signals
1. OpenAI lets you sync projects, chats, and plugins into Codex automatically
2.
Databricks:
Join Databricks DevConnect – find an event near you for deep dives into Lakehouse//RT, LTAP, Omnigent, MCPs, Genie, and ZeroOps
3. Google's open
diffusion model hits
1,500 tokens per second on a single GPU
4. New inverse model
reconstructs exact LLM
prompts from public outputs alone
5. Microsoft's
simple decoding trick
makes 1B models train 1.5x more efficiently
6. Tencent ships agentic tool that builds explorable 3D game worlds from text
Top Paper
Security flaw lets anyone steal hidden reasoning from Claude, GPT, and Gemini
11,588 Likes
AI companies hide their models' step-by-step thinking inside
encrypted blobs
sent back to your client. Sounds safe. It isn't.
Researchers found that these encrypted chunks are fully portable. Grab a blob from Claude Opus, inject it into the cheaper, less guarded Haiku, and Haiku will just... read it out loud. No breaking encryption needed. The same trick works on OpenAI and Gemini.
Here's what this actually unlocks for attackers:
Steal proprietary reasoning traces from top models using weaker ones as a decoder
Extract private data from public session logs. A scan of ~7,000 public traces found
62 API keys
, 33 emails, and 33 passwords
Surface hidden hazardous info the model rejected in its visible reply but reasoned through internally
Inject invisible malicious instructions inside encrypted blobs to poison shared agent workflows
If you ever shared a Claude Code or Codex session publicly, those encrypted blobs are decodable. The labs have patched several issues after responsible disclosure.
READ MORE
forward →
Presented by Tiger Data
One Database: Metrics, Embeddings, and Analytics
Metrics, embeddings, and analytics.
TimescaleDB
handles all three in the Postgres you already run: hypertables for time-series at scale, pgvector and pgvectorscale for embeddings, continuous aggregates for real-time analytics.
No pipelines to sync, no drift, no second database to feed.
Same SQL, same tools, one system to operate. No pipelines to sync, no drift, no second database to feed.
Start a trial today and get $1000 in credits:
GET $1000 CREDIT
partner with us →
Top News
OpenAI drops ChatGPT desktop app for Linux on Ubuntu, Debian, and Fedora
10,793 Likes
For years, ChatGPT had a desktop app on Mac and Windows. Linux? Nothing.
That gap just closed.
OpenAI dropped a preview of the official ChatGPT desktop app for Linux. This is not a browser wrapper or a CLI tool. It is a full native app, and it ships with three things bundled together:
ChatGPT
- the assistant you already know
ChatGPT Work
- for team and workplace tasks
Codex
- an AI coding agent that can read your local files, run inside your actual repos, and control apps on your machine
That last one is the big deal. Codex running natively on Linux means the agent lives right where your code does.
Supported distros: Ubuntu 24.04 and 26.04 LTS, Debian 13, Fedora 43 and 44. Install via
.deb or .rpm
packages for x64 or ARM64. The installer also adds an OpenAI repo so updates flow through apt automatically.
It is free to download, but some features need a paid plan.
READ MORE
forward →
Presented by Upstage AI
An Agent Model That Actually Finishes the Job
Upstage's new agent model,
Solar Pro 4
:
GDPval-AA 39, τ³-Banking 23: top scores in its price tier
OpenAI-compatible API, 512K context, $0.30/$1.20 per 1M
Behavioral reliability: finishes multi-step work, flags what isn't there
90% off through Sep 10; trial on Hermes through Aug 18
TRY SOLAR PRO 4
partner with us →
Top News
Unsloth releases open-source desktop app to run and train models 2x faster locally
4,284 Likes
Running AI models on your own machine just got a proper app.
Unsloth Desktop
is an open-source desktop app that lets you run and train AI models locally, on Mac, Windows, and Linux, no cloud required.
Your data never leaves your machine. That's the whole point.
Here's what you actually get:
Train models
2x faster
using 70% less GPU memory, so even mid-range hardware works
Connect Claude Code or Codex to local models instead of paid APIs
Private web search, deep research, and RAG (feeding your own documents to the model)
Supports NVIDIA, AMD, Intel, and Apple Silicon GPUs
Export models in standard formats like GGUF for easy sharing
The big unlock here: you can build AI-powered apps, run experiments, and fine-tune models without paying per API call or sending sensitive data anywhere.
It's on GitHub and their website right now, free to grab.
READ MORE
forward →
Signals
1
OpenAI lets you sync projects, chats, and plugins into Codex automatically
3,968 Likes
2
Join Databricks DevConnect – find an event near you for deep dives into Lakehouse//RT, LTAP, Omnigent, MCPs, Genie, and ZeroOps
Presented by Databricks
3
Google's open diffusion model hits 1,500 tokens per second on a single GPU
1,228 Likes
4
New inverse model reconstructs exact LLM prompts from public outputs alone
741 Likes
5
Microsoft's simple decoding trick makes 1B models train 1.5x more efficiently
532 Likes
6
Tencent ships agentic tool that builds explorable 3D game worlds from text
2,429 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=5a5f26de4969437c