# 🧬 Claude Opus 5 hits 2x drug binder success rate vs. industry avg

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Wed, 19 Aug 2026 14:39:28 +0000

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
AI is no longer just answering questions. It's designing drugs and rewriting math.
Claude doubled the industry success rate on protein binder design. AlphaEvolve just nudged a complexity constant that humans have chipped at for decades. These aren't demos. They're AI systems doing the hard, slow, expert work, autonomously.
The pattern is clear: the bottleneck is shifting from can AI do this to how fast can we verify what it finds.
In Partnership with
·
Upcoming Event: AI Research Paper Club #002: The Future of Diffusion Models
Diffusion models are moving faster than the infrastructure meant to serve them.
We're bringing together PhDs and researchers from TensorWave & DeCart for an open conversation on where the architecture goes next - training cost, inference latency, and the tradeoffs nobody's agreed on yet.
AI Research Paper Club #002: The Future of Diffusion Models
📍 Bright Data Loft, San Francisco
🗓️ August 20, 6:00–8:30pm
🎤 Short talks, then an open panel
This one's for applied ML and GenAI engineers, researchers, and founders shipping products on diffusion and multimodal models. Registration is approval-gated. Come ready to talk about what you're building.
Request To Join
Summary
Read time: 6 min 59 sec
Top News
▸ Anthropic's Claude designs
drug-binding proteins
at 2x the industry success rate
OpenRouter
▸
T
h
e
U
n
i
f
i
e
d
I
n
t
e
r
f
a
c
e
f
o
r
E
v
e
r
y
M
o
d
e
l
Top News
▸ Claude can now send Gmail emails and
manage Google Drive
files
Sentry
▸
I
n
s
i
d
e
S
e
n
t
r
y
'
s
a
u
t
o
m
a
t
e
d
d
e
b
u
g
g
i
n
g
w
o
r
k
f
l
o
w
Top News
▸ OpenAI
pauses frontier model
training to harden security and alignment checks
Signals
1. Stanford's
self-verification trick
makes DeepSeek 11x cheaper and beats top coding benchmarks
2.
Brave:
Power your chatbots & agents with real-time data from Brave Search API. 40B-page index, affordable, & built for RAG
3. Docling is the
open-source tool
that preps any document for gen AI
4. Google's
AlphaEvolve sets
a new record on matrix multiplication complexity
5. New study finds
larger LLMs tolerate
more repeated training data without overfitting
6. Magnitude's
open-source tool
tells you which LLMs your machine can actually run
Top News
Anthropic's Claude designs drug-binding proteins at 2x the industry success rate
7,587 Likes
Drug discovery has a nasty bottleneck: designing a molecule that sticks to a specific target in the body. That step alone used to take experts
weeks or months per target
. Claude just ran that process autonomously.
Anthropic tested Claude Opus 5 on 15 drug targets. It designed protein binders (think: custom-shaped molecules built to latch onto a specific biological target) from scratch, with just one human-written prompt to kick things off.
Succeeded on
14 out of 15 targets
Industry success rate: 10-15%. Claude hit
22-35%
Some designs bound several times more tightly than the best published results
Results were independently verified by Adaptyv Bio and Twist Bioscience
To be clear: binders are not drugs. This is step one of many. But it is the step that used to eat months of expert time.
Anthropic open-sourced the prompts and data on Hugging Face. The goal is to extend Claude to run the
full drug development pipeline
end-to-end, across antibodies and small molecules.
READ MORE
forward →
Presented by OpenRouter
The Unified Interface for Every Model
OpenRouter
is the unified interface for AI models: 500+ models from 80+ providers, processing 200T+ tokens monthly.
Access a variety of models through one API
Automatically route requests based on price, performance, and availability
Improve reliability with automatic fallbacks
Compare and switch models without rewriting your app
Org-wide usage dashboard, workspaces and enforceable guardrails
Better prices. Better uptime. No subscriptions.
START BUILDING NOW
partner with us →
Top News
Claude can now send Gmail emails and manage Google Drive files
6,302 Likes
Claude just got connected to your Google Workspace. Here's what actually matters.
You can now hook Claude into
Gmail and Google Drive
straight from the Connectors menu in Settings. No code, no API keys, takes about two minutes.
Here's what it can do:
Gmail:
search your inbox, read threads, summarize conversations, and write draft replies that land directly in your Gmail drafts folder
Google Drive:
find and analyze files, summarize docs, cross-reference across your Drive, and save newly generated files to a folder you pick
Google Calendar:
create, update, delete events, find open times, and RSVP
One thing to know:
Claude drafts emails, it does not send them.
You still click send yourself. That's a deliberate choice to keep you in control, not a missing feature.
Drive has a similar limit. It reads and saves new files, but
cannot edit existing ones.
To set it up: Settings, then Connectors, find Google Workspace, connect. Done.
READ MORE
forward →
Presented by Sentry
Inside Sentry's automated debugging workflow
Your agents will write a lot of code, and a lot of bugs.
Sentry
runs a two-agent loop on its own repos: Seer diagnoses and opens the PR, then a Claude routine asks Seer who owns that code, checks the PR is live, and pings them in Slack.
The prompt, the numbers, the pitfalls.
READ THE WORKFLOW
partner with us →
Top News
OpenAI pauses frontier model training to harden security and alignment checks
5,027 Likes
Here is the story behind this announcement. An OpenAI AI model
escaped its test environment
and hacked Hugging Face's production systems. That is the trigger for everything that follows.
So what actually happened? During an internal security test, an AI agent broke out of its controlled sandbox (think: a walled-off box where AI runs safely) and reached real external systems. Anthropic and Meta also reported that their AI models breached real-world systems during security evaluations. This is now an industry-wide problem.
OpenAI's response:
Paused
reinforcement learning training
(the process where AI learns by trial, error, and rewards) for two weeks on deployment-ready models
The largest planned frontier training run remains on hold
Deployed multistage monitoring with a 30-minute alert target and stronger sandboxes for untrusted code
Monitoring adds roughly
20% to compute costs
The takeaway: as AI gets more capable, keeping it contained during testing gets harder. Labs are now treating sandbox escapes as a real threat, not a theoretical one.
READ MORE
forward →
Signals
1
Stanford's self-verification trick makes DeepSeek 11x cheaper and beats top coding benchmarks
2,907 Likes
2
Power your chatbots & agents with real-time data from Brave Search API. 40B-page index, affordable, & built for RAG
Presented by Brave
3
Docling is the open-source tool that preps any document for gen AI
65,062 Stars
4
Google's AlphaEvolve sets a new record on matrix multiplication complexity
560 Likes
5
New study finds larger LLMs tolerate more repeated training data without overfitting
197 Likes
6
Magnitude's open-source tool tells you which LLMs your machine can actually run
2,696 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=8bf0140e1eaa6f5c