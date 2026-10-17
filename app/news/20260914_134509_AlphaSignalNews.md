# 🔧 OpenAI: trim bloated prompts, ElevenLabs rival ships free voice clon

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Mon, 14 Sep 2026 13:45:09 +0000

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
The theme today is
doing more with less
. OpenAI says your old prompts are now dead weight on smarter agents. Cognition ships a dual-model harness that cuts costs 39% by letting a cheap sidekick handle grunt work.
As models get smarter, the scaffolding we built around dumber ones becomes the bottleneck. Less hand-holding, leaner prompts, cheaper executors.
And a new paper shows self-replicating agents naturally evolve cooperation when resources are shared. Turns out alignment might just be good economics.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 38 sec
Top News
▸ OpenAI shares tips to get
better results
from GPT-4o agents
Span
▸
M
a
p
t
o
k
e
n
s
a
n
d
t
i
m
e
t
o
b
e
t
t
e
r
s
o
f
t
w
a
r
e
o
u
t
c
o
m
e
s
Top Repo
▸ Solo dev open-sources free ElevenLabs rival that
clones voices
and dubs video into 646 languages
Ory
▸
C
o
d
i
n
g
a
g
e
n
t
s
d
o
n
'
t
b
u
i
l
d
a
u
t
h
.
T
h
e
y
u
s
e
O
r
y
.
Top Repo
▸ 10 free
open-source GitHub tools
that replace software you're paying for monthly
Signals
1. Google DeepMind open-sources a
physics-simulated fruit fly
that walks, grips, and flies
2.
Wiz:
AI Threat Readiness 101 - Learn the four pillars of AI threat readiness and how security teams can reduce risk faster
3. New model shows
self-replicating agents
evolve cooperation when energy is shared
4. New denoising trick trains
looped models
to hit 58.8% on ARC-AGI-1
5. New study finds
LLM steering vectors
can mirror human value theory with 0.51 correlation
6. DeepSeek multimodal model ships
uncensored FP8 version
with fewer content filters
Top News
OpenAI shares tips to get better results from GPT-4o agents
12,441 Likes
Your old Codex prompts might be hurting you now. OpenAI just dropped guidance saying that instructions written for older models can actually
slow GPT-6 Astra down
by wasting its memory and triggering the wrong behaviors.
Here's the core idea: Astra is smarter, so it needs less hand-holding. All that bloated guidance you wrote to babysit weaker models? It's now dead weight.
Three things to fix right now:
Skills
are prompt files that load for specific tasks. Make their trigger descriptions narrow and precise, so Astra grabs the right one instead of misfiring.
AGENTS.md
loads on every single task. Strip out mandatory pre-reading and generic "run your tests" reminders. Astra already does that on its own.
Task prompts
should clearly define what "done" looks like, so Astra knows when to stop instead of pausing to ask you.
The move: ask Astra itself to audit your existing skills and AGENTS.md files. Less scaffolding, cleaner results.
READ MORE
forward →
Presented by Span
Map tokens and time to better software outcomes
Your AI program has two inputs: engineers and tokens. Most tools only show one side of the equation.
Span is the ledger
that maps human effort and token spend to tickets, PRs, projects, and production outcomes.
Connect agent traces to the work around them so you know what it cost, what shipped, what the results were, and where to improve.
One ledger for effort, spend, and the software you actually ship.
SEE HOW SPAN WORKS
partner with us →
Top Repo
Solo dev open-sources free ElevenLabs rival that clones voices and dubs video into 646 languages
11,932 Likes
ElevenLabs charges per character, caps your usage, and sends your audio to their servers.
VoiceStudio
flips all of that. It's a free, open-source tool that runs 100% on your own machine.
A solo builder shipped this, and it already has
25K GitHub stars
. Here's what it actually does:
Clone any voice from one clean audio clip
Dub videos into
646 languages
(ElevenLabs does 32)
Generate audiobooks, run transcription, and dictation
Pick from 14 different text-to-speech engines instead of being locked to one
No billing. No caps. Your audio never touches a server.
To get started: git clone the repo, run bun install, then bun run desktop. It auto-configures all Python dependencies on first launch.
The honest tradeoff: quality depends on your hardware and which engine you pick. But for language coverage and privacy, nothing else comes close right now.
READ MORE
forward →
Presented by Ory
Coding agents don't build auth. They use Ory.
Add customer identity, OAuth, permissions, B2B SSO, and agent security to your website or app with industry best practices built in. One command spins up a local stack in seconds.
Ory supports 11 harnesses and 14 SDK frameworks, start building with Ory today -
Ory Agent Plugins.
START TEST DRIVE
partner with us →
Top Repo
10 free open-source GitHub tools that replace software you're paying for monthly
8,670 Likes
GitHub is quietly full of free tools that replace software you are probably paying for monthly. Here are
10 open-source projects
worth knowing about.
The two standouts worth digging into first:
LibreChat
lets you run ChatGPT, Claude, Gemini, Mistral, and local models all inside one self-hosted interface. You own your data, control which models load, and pay only for the API calls you make. No more juggling five browser tabs or five subscriptions.
TradingAgents
simulates a real trading firm using AI. Separate AI agents act as a fundamentals analyst, sentiment expert, technical analyst, and risk manager. They discuss, debate, and land on a strategy together. Built for research, not live trading.
The rest of the list covers an open-source Bloomberg terminal clone, a one-click short video generator, an AI email assistant, a voice cloning tool, an API integration platform, a video generation engine, and a Claude Code skills library.
The takeaway: before you renew that SaaS subscription, check GitHub first.
READ MORE
forward →
Signals
1
Google DeepMind open-sources a physics-simulated fruit fly that walks, grips, and flies
5,367 Likes
2
AI Threat Readiness 101 - Learn the four pillars of AI threat readiness and how security teams can reduce risk faster
Presented by Wiz
3
New model shows self-replicating agents evolve cooperation when energy is shared
506 Likes
4
New denoising trick trains looped models to hit 58.8% on ARC-AGI-1
326 Likes
5
New study finds LLM steering vectors can mirror human value theory with 0.51 correlation
203 Likes
6
DeepSeek multimodal model ships uncensored FP8 version with fewer content filters
2,438 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=95f6513f5643c920