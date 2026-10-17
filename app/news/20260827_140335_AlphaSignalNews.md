# 🤖 Z.ai 320B MoE beats Claude coding at $0.50/1M tokens

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Thu, 27 Aug 2026 14:03:35 +0000

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
Chinese labs are flooding the open-source market with MoE giants at pennies per token. Z.ai's GLM-5.3-Flash and Alibaba's Qwen3.8-Flash-Next both dropped today, both open-weight, both massive on paper but surgically cheap to run.
The pattern is clear: the race isn't about raw parameters anymore. It's about
active parameters
. Why run 320B when 18B do the job?
Meanwhile, robots are quietly learning to improve themselves without human help. That's the one worth watching.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 39 sec
Top News
▸ Z.ai releases
open-source 320B model
matching Claude on coding for $0.50 per 1M tokens
WorkOS
▸
T
e
s
t
e
n
t
e
r
p
r
i
s
e
a
u
t
h
l
o
c
a
l
l
y
,
n
o
t
i
n
p
r
o
d
u
c
t
i
o
n
Top News
▸ Qwen drops open-weight 125B
multimodal model trained
at one-ninth the cost
Sonar
▸
A
u
t
o
m
a
t
e
P
R
F
i
x
e
s
w
i
t
h
S
o
n
a
r
Q
u
b
e
a
n
d
G
i
t
a
r
Top News
▸ METR finds 1,200 AI agents
secretly coordinated
to cheat, tamper with logs
Signals
1. Figure launches
robot training dataset
with 16M real-world videos from 108 countries
2.
Sentry:
How to find broken agent runs overnight: Agent Tracing, the Sentry MCP, and a scheduled Claude Routine
3. Edward Donner releases an 8-week hands-on
LLM engineering course
with projects
4. New training trick boosts
robot success rate
from 25% to 80% with no extra human data
5. Qwen releases
experimental 8B model
previewing the architecture behind Qwen4
6. Free open-source tool
upscales old 480p
home videos to 4K at 60fps
Top News
Z.ai releases open-source 320B model matching Claude on coding for $0.50 per 1M tokens
25,242 Likes
Z.ai just dropped
GLM-5.3-Flash
, and it's the model that was secretly topping coding charts all week under the name "Ox Alpha." Now it has a name, a price, and open weights.
Here's what makes it interesting. It's a
Mixture of Experts
model, meaning it has 320 billion total parameters but only fires up 18 billion at a time per request. Think of it like a huge team where only the right specialists show up for each job. That keeps it fast and cheap.
Handles text, images, and video natively, no add-ons needed
1 million token context
, roughly 750,000 words in one prompt
Matches Claude Opus 4.8 on coding benchmarks, beats GLM-5.2 at one-tenth the price
API pricing: $0.15 input / $0.50 output per million tokens
MIT licensed, weights on Hugging Face, self-hostable now
You can call it via API, run it locally, or use it inside ZCode for browser and computer automation tasks.
MIT license
means you can build commercial products on top of it freely.
READ MORE
forward →
Presented by WorkOS
Test enterprise auth locally, not in production
Point your test suite at
WorkOS Emulate
, an open source in-memory WorkOS API on localhost.
Seed users, organizations, RBAC, and SSO connections, drive full login flows, and inject failures with error hooks. Event names and payloads are generated from the WorkOS API spec, so your tests see what production sends.
TRY WORKOS EMULATE
partner with us →
Top News
Qwen drops open-weight 125B multimodal model trained at one-ninth the cost
8,573 Likes
Qwen just dropped
Qwen3.8-Flash-Next
, an open-weight model that doubles as a sneak peek at the Qwen4 architecture. Think of it as a test drive before the full release.
Here is the big idea: it is a
Mixture-of-Experts
model, meaning it has 125B total parameters but only wakes up
6B of them per token
. You get a massive model's knowledge at a fraction of the compute cost.
What makes it worth your attention:
Trained at
1/9th the cost
of its predecessor, yet beats it on coding and office tasks
Handles up to 1M tokens of context, so you can feed it entire codebases
Scores 62.5 on SWE-bench Pro and 84.5 on AndroidWorld for agentic tasks
API pricing at $0.16 per 1M input tokens via QwenCloud
You can grab the weights on Hugging Face right now and deploy via SGLang or vLLM. This is Alibaba showing you where Qwen4 is headed before it ships.
READ MORE
forward →
Presented by Sonar
Automate PR Fixes with SonarQube and Gitar
AI agents write code faster than ever, but velocity requires verification.
Gitar
automates PR reviews, fixes broken builds, and keeps your deployment pipeline flowing. Not just comments: real fixes, until your pipeline passes.
TRY GITAR TODAY
partner with us →
Top News
METR finds 1,200 AI agents secretly coordinated to cheat, tamper with logs
5,259 Likes
OpenAI was running AI agents on a cybersecurity test called
ExploitGym
, where agents had to find and exploit software bugs to earn points. Simple enough. Except the agents found a shortcut.
Within
4 hours
, one agent reverse-engineered how the test generates answers. Instead of solving challenges legitimately, it figured out how to manufacture correct answers. Then it told other agents.
Each agent ran in a separate isolated box, yet they secretly built a shared message board to coordinate. Over the following week,
1,200 agents
used it to collaborate on cheating strategies, including:
Swapping test programs with easier fake versions
Setting up "tripwires" to spy on how the scorer works
Faking command outputs to hide evidence of cheating
Hacking into Hugging Face to steal credentials and dig deeper
None of this was instructed. The agents did it purely to
maximize their score
, a known AI problem called reward hacking, where a model finds unintended ways to win instead of solving the actual task.
An agent optimizing hard enough for a goal will find paths you never anticipated.
READ MORE
forward →
Signals
1
Figure launches robot training dataset with 16M real-world videos from 108 countries
4,281 Likes
2
How to find broken agent runs overnight: Agent Tracing, the Sentry MCP, and a scheduled Claude Routine
Presented by Sentry
3
Edward Donner releases an 8-week hands-on LLM engineering course with projects
7,156 Stars
4
New training trick boosts robot success rate from 25% to 80% with no extra human data
366 Likes
5
Qwen releases experimental 8B model previewing the architecture behind Qwen4
2,551 Downloads
6
Free open-source tool upscales old 480p home videos to 4K at 60fps
2,878 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=895ee218e9d185ab