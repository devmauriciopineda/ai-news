# Anthropic Claude Math Proof 🔢, OpenAI GPT-5 Cyber Zero-Days 🔓, Nvidia 

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 11 Aug 2026 17:48:15 +0000

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
AI is no longer just answering questions. It's doing the work.
Claude failed to prove the Riemann Hypothesis (obviously) but stumbled onto the biggest single jump in 160 years of math history. OpenAI's GPT-5.6-Cyber found zero-days in Chrome before most humans even knew to look. Both unreleased, both already outperforming the field.
The pattern is clear: the most interesting AI results are happening before the models ship.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 40 sec
Top News
▸ Anthropic's unreleased Claude model pushes
Riemann hypothesis progress
from 41.6% to 67.2%
Agent Field AI
▸
#
1
O
p
e
n
-
S
o
u
r
c
e
C
o
d
e
R
e
v
i
e
w
,
~
1
0
x
C
h
e
a
p
e
r
Top News
▸ OpenAI ships GPT-5.6-Cyber, a model that
found zero-days
in Chrome's V8 engine
Datadog
▸
L
e
a
d
A
I
F
r
o
m
P
i
l
o
t
t
o
P
r
o
v
e
n
i
n
9
0
D
a
y
s
Top News
▸ NVIDIA releases
open 30B model
that runs 4x faster than similar-sized models
Signals
1. Higgsfield open-sources a $2M AI feature film with
real celebrity actors
2. Hyperball optimizer gives Muon a 20–30% training speedup by fixing weight norms
3. Metis builds
persistent memory
directly into a model's forward pass, no retrieval needed
4. Amazon tests whether AI agents can
replace A/B tests
before launch
5. Dev uses GPT and Gemini to
port Command & Conquer
Red Alert 2 to iPhone
Top News
Anthropic's unreleased Claude model pushes Riemann hypothesis progress from 41.6% to 67.2%
16,928 Likes
Someone told Claude to take a real stab at one of math's hardest unsolved problems. Claude failed. But what it found on the way down is interesting.
The
Riemann Hypothesis
is a 160-year-old math problem about where a special function hits zero. Think of it like a treasure map where all the X marks should land on one specific line. Nobody has proven they all do. The best humans could do was prove that
at least 41.6%
of those X marks land where expected.
Claude just pushed that to
67.2%
, the biggest single jump in history on this problem. It did this by treating the zeros as one unified space instead of analyzing them separately.
Used
60 AI subagents
running in parallel inside Claude Code
Tried 650 failed ideas before finding the approach that worked
Ran 2,400 shell commands over a day and a half
Proof verified in Lean 4 and reviewed by two external math experts
The proof code and process logs are all public. The model is unreleased, but the agent architecture is yours to study today.
READ MORE
forward →
Presented by Agent Field AI
#1 Open-Source Code Review, ~10x Cheaper
PR-AF
just posted the #1 open-source score on Martian's Code-Review-Bench: 0.706 across 42 tools, ~3x more valid findings than leading commercial tools.
Built for deep code review, not shallow diff summaries: it plans a strategy per PR, runs reviewer agents in parallel, and verifies every finding against your source.
Use cheaper models for regular PRs, GLM-5.2 for CI gates, or Opus-class for highest-stakes reviews, at ~10x cheaper per review. Licensed Apache 2.0, self-hosted, and one-step GitHub Action.
STAR & DEPLOY
partner with us →
Top News
OpenAI ships GPT-5.6-Cyber, a model that found zero-days in Chrome's V8 engine
9,319 Likes
OpenAI just split its
Daybreak
cybersecurity program into two tiers, and the difference matters a lot depending on what you're building.
Daybreak Blue
is the starting point. You get GPT-5.6 Sol with security guardrails loosened just enough for defensive work. Think of it as the standard model, but it won't refuse you when you ask it to analyze malware or review vulnerable code.
Daybreak Red
is the serious tier. It unlocks
GPT-5.6-Cyber
, a model specifically trained to do the risky stuff: finding zero-day vulnerabilities (unknown security holes), building exploit chains, and validating attacks. It completed
95% of advanced security tasks
in testing, versus just 1.5% for the regular GPT-5.6.
Blue: vulnerability discovery, malware analysis, code review, incident response
Red: exploit development, zero-day research, security testing
Real proof: it found two unknown bugs in Chrome's V8 JavaScript engine
Red access requires approval. You apply, get vetted, then get monitored. Not open to everyone yet.
READ MORE
forward →
Presented by Datadog
Lead AI From Pilot to Proven in 90 Days
AI has moved from pilot to production, and engineering leaders are expected to show results.
This playbook
gives you a practical framework of four priority plays, three enabling capabilities, and a 90-day checklist to build reliable, evidence-driven AI systems.
GET THE EBOOK
partner with us →
Top News
NVIDIA releases open 30B model that runs 4x faster than similar-sized models
3,469 Likes
NVIDIA just dropped
Nemotron 3.5 Lightning
, and the story here is speed without the usual tradeoff.
Most AI agents waste compute. They use a massive, slow model for every single step, even boring ones like calling a tool or checking a result. Lightning fixes that.
Here is the trick: it has
30B total parameters
but only activates
3B at a time
. Think of it like a team of specialists where only the right people show up for each task, instead of the whole company attending every meeting. That is the MoE (Mixture-of-Experts) design.
The numbers back it up:
4x faster
output than similar-sized models
86% accuracy on PinchBench, completing 10,000 tasks 35% faster than Qwen3 35B
1M token context window for long agent sessions
Runs on a single H100 or DGX Spark
You can fine-tune it on your own data using NVIDIA NeMo for domains like cybersecurity, coding, or legal work. Weights are open on Hugging Face, deployable via vLLM or SGLang today.
READ MORE
forward →
Signals
1
Higgsfield open-sources a $2M AI feature film with real celebrity actors
2,735 Likes
2
Hyperball optimizer gives Muon a 20–30% training speedup by fixing weight norms
474 Likes
3
Metis builds persistent memory directly into a model's forward pass, no retrieval needed
357 Likes
4
Amazon tests whether AI agents can replace A/B tests before launch
242 Likes
5
Dev uses GPT and Gemini to port Command & Conquer Red Alert 2 to iPhone
2,497 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=ec26e8bdcd70fa43