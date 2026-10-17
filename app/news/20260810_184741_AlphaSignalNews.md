# 🤝 Claude Code sessions talk mid-task, catching 89% of bad commands

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Mon, 10 Aug 2026 18:47:41 +0000

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
AI agents are learning to work together. Claude Code sessions now talk to each other mid-task, and its auto mode catches 89% of dangerous commands vs. 13% for tired humans. The solo AI assistant era is quietly ending.
Meanwhile, Harvard and MIT just simulated all 8.3 billion humans overnight to test products. Think about that pairing: agents that coordinate autonomously, tested against a synthetic world population.
We're not building tools anymore. We're building teams that run without us.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 19 sec
Top News
▸ Claude Code sessions can now
talk to each other
mid-task
WorkOS
▸
A
g
e
n
t
s
C
a
n
N
o
w
S
i
g
n
U
p
f
o
r
Y
o
u
r
A
p
p
Top News
▸ Anthropic makes Claude Code
auto mode default
, catching 89% of dangerous commands
Tiger Data
▸
L
e
a
r
n
T
i
m
e
s
c
a
l
e
D
B
.
E
a
r
n
a
S
w
a
g
P
a
c
k
.
Top News
▸ OpenAI flags its Astra model as a cybersecurity risk under its safety framework
Signals
1. Meta releases open-weight 30B model that runs
full agent workflows
on your laptop
2. Invoke releases a free open-source
creative studio built
on Stable Diffusion
3. Harvard and MIT simulate all 8.3 billion humans to test products overnight
4. Chelsea Finn's study finds
pretraining Q-functions rarely
helps RL fine-tuning
5. Anthropic ships four Claude Managed Agents upgrades including spend limits and advisor models
Top News
Claude Code sessions can now talk to each other mid-task
62,761 Likes
Picture this: you have
three terminals open
on the same project. Backend in one, tests in another, database migration in the third. One session finds a breaking change. You used to manually copy that info across windows. Not anymore.
Claude Code now lets sessions talk to each other directly. Here is what it does:
One session sends a plain-text summary to another, never your full chat history or files
It works both ways: ask another session a question and get the answer back in your active window
Claude can message another session on its own when a change it just made affects what that session is doing
Messages stay
local to your machine
and never hit Anthropic's servers
Two tools power it under the hood: one finds your active sessions, the other delivers the message. To try it, just update Claude Code to
v2.1.224
and say something like "Tell the other session what we just changed." Available on macOS and Linux.
READ MORE
forward →
Presented by WorkOS
Agents Can Now Sign Up for Your App
Agents are hitting your signup flow and bouncing off a browser login built for humans. Every one that gives up is a signup you never see.
WorkOS Agent Registration
turns that traffic into signups. Enroll via the dashboard and AuthKit publishes an auth.md file agents read to register for scoped, short-lived credentials you control.
ENABLE IT TODAY
partner with us →
Top News
Anthropic makes Claude Code auto mode default, catching 89% of dangerous commands
17,640 Likes
Manual approval for AI shell commands sounds safe. It isn't. In a study with over 1,000 paid testers, humans only caught
13.6% of dangerous commands
. After 50 prompts, that dropped to 5%. Approval fatigue is real.
Claude Code's auto mode runs a classifier (think: a small AI that checks every action before it runs) on every tool call. It caught
89% of dangerous commands
, flat across the whole session. No fatigue.
So here's what this opens up:
Kick off multi-hour tasks and walk away, no babysitting permissions
Run
multiple tasks in parallel
and come back to finished PRs
Classifier tokens no longer count toward your usage limits on Pro, Max, and Team plans
Auto mode becomes the default soon. You'll get an in-app notification. Toggle anytime with
Shift+Tab
, and admins can pin or disable it in managed settings.
READ MORE
forward →
Presented by Tiger Data
Learn TimescaleDB. Earn a Swag Pack.
Take the Tiger Hunt challenge: skill up on TimescaleDB by building, not reading.
Sign up for TimescaleDB on Tiger Cloud
and finish five quick tasks: load a dataset, install the MCP/Tiger CLI, create a hypertable, build a continuous aggregate, join a live workshop and earn an exclusive swag box.
START THE HUNT
partner with us →
Top News
OpenAI flags its Astra model as a cybersecurity risk under its safety framework
9,920 Likes
OpenAI just hit a milestone nobody was rushing toward. Their upcoming model,
Astra
, is the first model they've ever flagged as
"Critical"
for cybersecurity risk.
What does Critical actually mean? It means Astra may be able to find and exploit security holes in real-world systems, completely on its own, with zero human help. Think of it like an AI that can independently break into well-protected computer systems just from a high-level instruction.
Every previous model, including GPT-5.6 Sol, only hit the "High" tier. Astra is a step above that, which triggers a whole different set of rules under OpenAI's safety playbook.
So what's actually happening right now:
Internal work on Astra is
partially paused
until safeguards catch up
Universal monitoring is now active across all uses of the model
Government agencies and safety groups are being brought in to test it
The goal is still to release Astra broadly, with its cyber powers aimed at defenders, not attackers. But it needs more time to get there safely.
READ MORE
forward →
Signals
1
Meta releases open-weight 30B model that runs full agent workflows on your laptop
6,286 Likes
2
Invoke releases a free open-source creative studio built on Stable Diffusion
27,799 Stars
3
Harvard and MIT simulate all 8.3 billion humans to test products overnight
3,002 Likes
4
Chelsea Finn's study finds pretraining Q-functions rarely helps RL fine-tuning
555 Likes
5
Anthropic ships four Claude Managed Agents upgrades including spend limits and advisor models
5,855 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=182f93ebb29d1a32