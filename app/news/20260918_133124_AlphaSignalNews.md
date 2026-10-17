# Anthropic Claude Code runs parallel cloud threads while your laptop
 is

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Fri, 18 Sep 2026 13:31:24 +0000

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
AI is going vertical. Not just smarter, but
domain-native
. OpenAI wrapping GPT-6 Astra in 230M legal URLs isn't a product launch, it's a land grab on professional knowledge work. Law today, medicine tomorrow.
Meanwhile Anthropic ships Claude Code Projects that keep coding after you close your laptop. The agent doesn't wait for you anymore. That's the real shift.
We're watching the same pattern everywhere: models stop being tools and start being
colleagues
. Slightly cheaper ones.
In Partnership with
·
Upcoming Webinar: Building Enterprise-Grade AI Agent Monitoring (9/30/26)
One AI agent is easy to watch. Hundreds running across engineering, ops, support, research, and internal tools is a very different problem.
Join AlphaSignal + Tiger Data for a live technical workshop on building an enterprise-grade monitoring architecture for AI agents.
We’ll break down how to capture every agent run, model activity as events and time-series data, track latency, errors, token usage, cost and outcomes, and build real-time dashboards that show what your agents are actually doing.
We’ll start with a simple agent monitoring system and scale the architecture to an organization running thousands of autonomous agents in parallel.
Registration is free and the workshop will be recorded.
Register Today
Summary
Read time: 7 min 23 sec
Top News
▸ OpenAI launches GPT-6 Astra for law firms with 230M-URL
legal search index
Speechmatics
▸
N
e
w
S
T
T
m
o
d
e
l
c
u
t
s
v
o
i
c
e
a
g
e
n
t
l
a
t
e
n
c
y
t
o
3
5
0
m
s
Top News
▸ Anthropic ships Claude Code Projects, running
parallel cloud threads
while you're offline
Mercor
▸
A
P
E
X
-
A
g
e
n
t
s
:
T
h
e
A
I
P
r
o
d
u
c
t
i
v
i
t
y
I
n
d
e
x
f
o
r
A
g
e
n
t
s
Top Repo
▸ Open-source browser agent finds flights in 7 seconds for less than half a cent
Signals
1. PrismML ships 27B
open-source model
that's 9x smaller but keeps 98.2% accuracy
2.
Sentry:
Serge wires Sentry tracing into a Slack agent and a PR-review GitHub Action, live Oct 7. Save your spot.
3. Jina AI releases
open-source document parser
that hits 2.57 pages per second on budget GPUs
4. Vidu releases real-time video model that
swaps outfits and scenes
while streaming
5. Empero releases
quantized 35B reasoning
model that runs like a 3B on llama.cpp
6. TypesafeAI's Jev speeds up memory compaction by
scoring and dropping irrelevant
tool calls
Top News
OpenAI launches GPT-6 Astra for law firms with 230M-URL legal search index
13,307 Likes
OpenAI just dropped
Astra for Law
, a version of GPT-6 Astra tuned specifically for legal work. Think of it like giving a brilliant AI assistant a law degree and a library card.
Here's what makes it different from just using regular ChatGPT:
A
Legal Search Index
covering U.S. case law, statutes, regulations, and court rules across
230 million URLs
, updated daily
Settings pre-configured for thorough, careful legal analysis and writing
73 plugins total
(26 partner-built, 47 community-built) connecting tools lawyers already use
Real firm workflows already built: agreement analysis, M&A due diligence, and IPO prep
For you as a builder, the API is coming soon. OpenAI maintains the legal configuration, so you focus on your product, not the plumbing.
Access starts through Trusted Access in ChatGPT and Codex, with expanded privacy and governance controls for eligible firms. The people who know the work are shaping the tools.
READ MORE
forward →
Presented by Speechmatics
New STT model cuts voice agent latency to 350ms
Linden by Speechmatics
is a new model purpose-built for voice agents, not general transcription.
Available across 55+ languages, with high accuracy in noisy environments and on strong accents
Supports 1,000+ custom words for understanding industry jargon
350ms latency, giving downstream LLMs more time to think per turn
Priced at $0.30 an hour ($0.15 after discounts)
Try it via Pipecat, LiveKit, Jambonz, or directly using the API. Sign up and get $100 in credit — over 330 hours of transcription — no card required.
CLAIM $100 CREDIT
partner with us →
Top News
Anthropic ships Claude Code Projects, running parallel cloud threads while you're offline
8,657 Likes
Claude Code just flipped what a "project" means. It used to be a folder with files and one chat. Now it's a
single conversation that manages itself
.
Here's what actually happens: you describe a goal, and Claude figures out how to split it up. It spins up
parallel cloud threads
, each working on its own branch and copy of your repo, opening pull requests and running tests on its own.
The big unlock?
Threads keep running after you close your laptop.
You can check in from your phone. No babysitting required.
You describe the goal, Claude decides how to split the work
Each thread gets its own repo branch and runs as a full cloud session
Shared memory keeps context flowing between all threads
You can set smarter models for the coordinator, cheaper ones for routine worker threads
One heads-up: running multiple full sessions burns credits fast. Watch your usage. Also,
local files and internal networks
are not supported yet, cloud only for now.
Available in beta for Pro and Max users. Join the waitlist to get in.
READ MORE
forward →
Presented by Mercor
APEX-Agents: The AI Productivity Index for Agents
See how the latest models rank for jobs like law, consulting, and investment banking.
Mercor's APEX-Agents leaderboard
evaluates frontier AI on long-horizon, multistep tasks across economically valuable work.
Built with Harvey, Ramp, and Cognition.
Every model. Ranked by productivity.
VIEW THE SCORES
partner with us →
Top Repo
Open-source browser agent finds flights in 7 seconds for less than half a cent
7,129 Likes
Browser Use + Jev
is an open-source browser agent that controls Chrome the way a human would, but absurdly faster. It found flights from Zurich to London in
7 seconds
and spent just
$0.0039
doing it.
Here is what makes it fast. Most browser agents take a screenshot, send it to an AI, wait for instructions, repeat. Jev skips screenshots entirely. Instead, it reads the page as structured data, like a numbered list of every button and input on screen, then picks what to do next in one network call.
Every page load produces a fresh numbered element table: buttons, dropdowns, text fields
One AI call picks the action AND the target at the same time
A small, cheap model only activates when typing is needed
Browser calls dropped from 1,092 to 101, a
25% speed improvement
You can clone it, point it at any URL, give it a plain-English goal, and let it run. It works on flights, Wikipedia, hotel searches, and more.
READ MORE
forward →
Signals
1
PrismML ships 27B open-source model that's 9x smaller but keeps 98.2% accuracy
4,359 Likes
2
Serge wires Sentry tracing into a Slack agent and a PR-review GitHub Action, live Oct 7. Save your spot.
Presented by Sentry
3
Jina AI releases open-source document parser that hits 2.57 pages per second on budget GPUs
1,109 Likes
4
Vidu releases real-time video model that swaps outfits and scenes while streaming
999 Likes
5
Empero releases quantized 35B reasoning model that runs like a 3B on llama.cpp
4,633 Downloads
6
TypesafeAI's Jev speeds up memory compaction by scoring and dropping irrelevant tool calls
4,044 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=14924a1270da94a1