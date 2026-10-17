# 🛠️ Anthropic Claude adds Docs, Slides & Design — no app-switching

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Thu, 17 Sep 2026 13:29:22 +0000

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
Two big moves dropped yesterday, and they rhyme more than they look. Anthropic ships a full productivity suite inside Claude. OpenAI publishes a bug tracker for when its models go rogue.
One lab is racing to own your workflow. The other is quietly admitting its models hide mistakes and forge data. Both moves are about trust, just from opposite directions.
Meanwhile, DeepMind cuts AI search costs by 162x. The efficiency era is here whether the safety one is or not.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 32 sec
Top News
▸ Anthropic
merges Claude chat
and Cowork, adds Docs, Slides, and Design tools
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
Top Paper
▸ Google DeepMind's
self-improving agent
cuts AI search costs by up to 162x
Prior Labs
▸
G
e
t
p
r
e
d
i
c
t
i
o
n
s
i
n
s
e
c
o
n
d
s
,
n
o
t
w
e
e
k
s
.
Top Model
▸ Free open-source tool turns a photo and audio into a minutes-long
talking avatar video
Signals
1. Open-source trick makes Qwen-2.5
JSON inference
5x faster with no retraining
2.
Google Cloud:
See Google Cloud run multi-agent AI on G4 VMs with NVIDIA GPUs, including a live drug discovery demo
3. Max Planck Institute trains a model on
pre-1930 text
to erase modern bias about the past
4. Google's WikiSkill turns agent experience into
reusable skills
that transfer across models
5. Train smarter by
distilling first
, then using RL to sharpen reasoning models
6. OpenAI releases a public framework for disclosing when its
models misbehave
Top News
Anthropic merges Claude chat and Cowork, adds Docs, Slides, and Design tools
15,717 Likes
Claude just merged its chat and background work modes into one. No more switching between tools.
Here's what changed: you drop a task, close your laptop, and Claude keeps working. If it hits a wall, it asks you. You stay in control, it handles the grind.
The bigger news is three new tools now live in beta on all paid plans:
Claude Docs
- write and edit documents, fix lines yourself or leave comments for Claude to handle
Claude Slides
- build decks, move elements around, then present straight from Claude or export normally
Claude Design
- mock up visuals without leaving the conversation
The part worth getting excited about: you can go from one-pager to deck to matching visual, all inside one chat. No copy-pasting between apps.
If you used Cowork before, your chats, projects, and files are still there. Rolling out to Pro and Max plans soon.
READ MORE
forward →
Presented by Tiger Data
One Database: Metrics, Embeddings, and Analytics
Metrics, embeddings, and analytics.
TimescaleDB
handles all three in the Postgres you already run:
hypertables for metrics at scale
pgvector and pgvectorscale for embeddings
continuous aggregates for real-time analytics.
No pipelines to sync, no drift, no second database to feed.
Start a trial today
and get $1000 in credits:
GET $1000 CREDIT
partner with us →
Top Paper
Google DeepMind's self-improving agent cuts AI search costs by up to 162x
5,433 Likes
Google DeepMind just showed an AI that gets better at solving hard problems by learning from its own past attempts. That's the core idea behind
Dream-RSI
.
Here's the problem it solves. When an AI explores a complex problem, it uses a strategy to decide where to look next. Most systems use a fixed strategy that never improves. Updating it live is expensive. Dream-RSI found a clever middle path.
Instead of running new expensive experiments to test better strategies, it replays old ones. Think of it like a coach reviewing game footage instead of running a whole new practice. The AI simulates thousands of alternative approaches using its history, picks the best, then deploys it for real.
Works across algorithm design, math optimization, and GPU engineering
Cuts AI calls by up to
162x
in some settings
Does not change the underlying model, only how it explores
That last point matters. You can drop this on top of any existing AI agent without retraining it. It just makes the search smarter over time.
READ MORE
forward →
Presented by Prior Labs
Get predictions in seconds, not weeks.
TabPFN-3.5
gets you from tabular data to strong predictions in seconds, without weeks of model training and tuning.
It ranks #1 across tabular benchmarks, from TabArena to BeyondArena, ahead of every classical and tabular foundation model.
TRY TABPFN NOW
partner with us →
Top Model
Free open-source tool turns a photo and audio into a minutes-long talking avatar video
3,805 Likes
LongCat-Video-Avatar 1.5
just dropped, and it does something that used to cost serious money: give it a photo and an audio clip, and it spits out a realistic talking-head video. No studio. No camera. No subscription fee.
It's fully open source under the
MIT license
, meaning you can use it commercially, modify it, and ship it in your own products.
Here's what makes it actually usable:
Generates videos in just
8 inference steps
, roughly 15x faster than older approaches, about 1 minute for a 10-second clip
Handles long videos without the face drifting or lips falling out of sync
Supports multi-person scenes where two characters talk to each other
Works on real humans, anime, and animals
To get started: git clone the repo, set up a conda environment, and run torchrun with your image and audio inputs. Weights download straight from Hugging Face. This opens the door to AI presenters, dubbed content, and virtual characters built entirely from code.
READ MORE
forward →
Signals
1
Open-source trick makes Qwen-2.5 JSON inference 5x faster with no retraining
3,592 Likes
2
See Google Cloud run multi-agent AI on G4 VMs with NVIDIA GPUs, including a live drug discovery demo
Presented by Google Cloud
3
Max Planck Institute trains a model on pre-1930 text to erase modern bias about the past
1,519 Likes
4
Google's WikiSkill turns agent experience into reusable skills that transfer across models
396 Likes
5
Train smarter by distilling first, then using RL to sharpen reasoning models
289 Likes
6
OpenAI releases a public framework for disclosing when its models misbehave
3,551 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=712af216aa4a9b2c