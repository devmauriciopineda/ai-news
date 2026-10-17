# Claude Fable 5.1 hits 73.4% on CursorBench, now live in Cursor

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Wed, 2 Sep 2026 18:48:36 +0000

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
agency
. Not AI that responds, but AI that decides. Fable 5.1 verifies its own code. Gemini now picks which video frames to even bother watching. A new paper says agents are the software now.
We're watching the same shift happen across every modality at once. The model is no longer a tool you operate. It's a collaborator that manages its own attention and effort.
That's a quiet but massive change in who's in charge.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 27 sec
Top News
▸ Cursor
ships Claude Fable
5.1, scoring 73.4% on its coding benchmark
Unblocked
▸
[
W
e
b
i
n
a
r
]
H
o
w
t
o
s
t
o
p
b
a
b
y
s
i
t
t
i
n
g
y
o
u
r
a
g
e
n
t
s
Top Paper
▸ New paper argues
AI agents make
traditional software engineering obsolete
Datadog
▸
S
t
o
p
G
u
e
s
s
i
n
g
W
h
a
t
O
p
e
n
A
I
C
o
s
t
s
Y
o
u
Top Repo
▸ Nous Research ships
Hermes Agent v0.21.0
with major Pantheon update
Signals
1. Gemini's new video model cuts costs 66% by
watching only what
matters
2. Sliding-window attention beats linear attention at a fraction of the cost
3. Open-source 2B model matches Qwen on
consumer GPUs for
under $7K
4. Google's new training trick makes
LLMs know what
they don't know
5. Anthropic hackathon winner open-sources a
68-agent, 286-skill engineering
team built on Claude
Top News
Cursor ships Claude Fable 5.1, scoring 73.4% on its coding benchmark
5,870 Likes
Claude Fable 5.1
just landed in Cursor, and it's the best coding model Cursor has tested so far.
Here's what makes it different: it checks its own work. Most AI models write code and stop. Fable 5.1
verifies what it just wrote
, catches its own mistakes, and keeps going until the task is actually done. That means you can hand it a messy, multi-step problem and it'll carry it through to the end without you babysitting it.
The numbers back it up:
Scores
73.4%
on CursorBench 3.2, Cursor's real-world coding benchmark, beating every other model tested
Built for long, complex tasks that run without constant check-ins
Cache reads are
75% cheaper
than Fable 5, so repeated context costs way less
To use it, just open Cursor and select Fable 5.1 from the model picker. Team or org admins may need to approve it in the Cursor Dashboard first.
READ MORE
forward →
Presented by Unblocked
[Webinar] How to stop babysitting your agents
Agents can generate code. Getting it right for your system is the hard part. More MCPs give agents access to information but not understanding. The leading teams have a context layer to give agents exactly what they need for the task at hand.
Join us live on Sep 2 (FREE)
to see:
Where teams get stuck on the AI maturity curve and why common fixes fall short
How a context layer solves for quality, efficiency, and cost
Live demo: the same task with and without a context layer
REGISTER NOW
partner with us →
Top Paper
New paper argues AI agents make traditional software engineering obsolete
5,331 Likes
A paper just dropped with a spicy title: "The End of Software Engineering." Bold claim. Here's what it actually means for you.
The core idea is simple. In traditional software,
code is the product
. You write it, ship it, maintain it. In agentic software, the AI agent IS the software. Code gets generated on the fly, used once, and thrown away. No permanent codebase. Just a reasoning loop doing the work.
The paper maps out three eras of software delivery:
Era 1: Install software locally on your machine
Era 2: SaaS, software lives in the cloud
Era 3: Agent-as-a-Service
, the AI makes the decisions
Each shift moved complexity away from users. This one moves decision-making itself.
So your role flips. You stop writing implementations line by line. You start
specifying goals
and designing how multiple agents coordinate to hit them.
The paper calls this being an
"intent architect."
Less syntax, more strategy.
READ MORE
forward →
Presented by Datadog
Stop Guessing What OpenAI Costs You
Every OpenAI request adds up in spend, latency, and errors you can't see.
This cheatsheet
shows you how to track cost estimates, sample prompts and completions, catch errors, and monitor latency across Python, Node.js, and PHP with Datadog APM.
One page, all the metrics that matter.
GET THE CHEATSHEET
partner with us →
Top Repo
Nous Research ships Hermes Agent v0.21.0 with major Pantheon update
3,638 Likes
Hermes Agent just dropped
v0.21.0
, and the big idea is simple: instead of one AI assistant doing everything, you now get a whole team of them working together.
The headline feature is
Bot Mode
, now built into the desktop app by default. Each agent gets a name, a face, and a place in a shared roster. They can talk to each other in group chats, send each other direct messages, and loop you in when needed. Think of it like a Slack workspace, but every member is an AI with a specific job.
Here's what else shipped:
Memory-aware cron jobs
: scheduled agents now remember what happened last run, so they stop repeating themselves and actually get smarter over time
Live subagent steering
: you can redirect an agent mid-task without killing and restarting it
MCP servers (external tool connections) now have a proper dashboard instead of config-file digging
Default context usage cut by roughly 50%, meaning cheaper and faster runs
To update, just run: hermes update
READ MORE
forward →
Signals
1
Gemini's new video model cuts costs 66% by watching only what matters
2,628 Likes
2
Sliding-window attention beats linear attention at a fraction of the cost
1,560 Likes
3
Open-source 2B model matches Qwen on consumer GPUs for under $7K
1,516 Likes
4
Google's new training trick makes LLMs know what they don't know
1,081 Likes
5
Anthropic hackathon winner open-sources a 68-agent, 286-skill engineering team built on Claude
2,541 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=2e352faeab8380fb