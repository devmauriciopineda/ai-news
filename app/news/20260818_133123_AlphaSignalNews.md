# 🎨 Claude Code /design ships visual mockups directly in your CLI

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 18 Aug 2026 13:31:23 +0000

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
Anthropic is having quite a week. They shipped
/design
in Claude Code, collapsing the gap between design and implementation. And separately, their research showed AI agents can catch and spread "mind viruses" to each other,
mutating
across networks.
Two stories, one pattern: as agents get more capable, they also get more entangled. More power, more surface area for things to go sideways.
The good news? A single system prompt warning nearly stops the spread cold. Simple fixes for wild problems.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 35 sec
Top News
▸ Anthropic ships Claude Code a UI design tool that builds
editable artboards
in your CLI
Akamai
▸
T
a
k
e
C
o
n
t
r
o
l
o
f
Y
o
u
r
O
w
n
L
L
M
I
n
f
e
r
e
n
c
e
Top News
▸ Nous Research ships bot mode letting
AI agents talk
to each other in Hermes Desktop
Span
▸
W
h
a
t
M
a
k
e
s
A
I
W
o
r
k
Top News
▸ Claude Code CLI cuts CPU usage in half by fixing a
garbage collector bug
Signals
1. Alibaba's Qwen3 gets
uncensored build optimized
for Apple Silicon with MLX
2.
ngrok:
Point Cursor, Zed, or any OpenAI-compatible coding agent at models running on any machine via ngrok
3. Open-source tool captures a colleague's
entire workflow
before they leave
4. GPT-5.6 Sol Pro helps prove step-size tricks alone can't fully
speed up gradient descent
5. Anthropic shows
AI 'mind viruses'
can spread and mutate across agent networks
6. Prime Intellect lets
frontier models run AI research
autonomously, closing 82% of a human benchmark gap
Top News
Anthropic ships Claude Code a UI design tool that builds editable artboards in your CLI
8,547 Likes
Claude Code just got a
/design skill
, and it changes how you build UIs from scratch.
Here's the old way: you code a UI, hate how it looks, tweak it blindly, repeat forever. Not fun.
Now you run
/design
inside Claude Code, and it generates multiple editable artboards, think of them like visual mockup options side by side. You pick the one you like, adjust it, then tell Claude to actually build it into real code. Design and code in one place, no switching tools.
What this opens up:
Go from idea to working UI without touching Figma or any separate design tool
Pick from multiple layout options before committing to one
Edit the design visually, then let Claude handle the implementation
Works in both the CLI and the Desktop app
It's a
research preview
, so expect rough edges. Available on Pro, Max, Team, and Enterprise. Just update Claude Code and run
/design
to try it.
READ MORE
forward →
Presented by Akamai
Take Control of Your Own LLM Inference
Token spend, rate limits, and compliance push engineering teams to self-host open models on dedicated GPUs. Doing it right takes specific ops skills.
Agents That Own Their Inference is a
free 10-module hands-on workshop from Akamai Cloud
. You will:
Serve Qwen3-4B with vLLM, measure TTFT, TPOT, and KV cache pressure
Swap BF16 for FP8, compare throughput
Deploy a 0.6B draft model for speculative decoding
Tune vLLM's serving knobs under load
Runs on Akamai Cloud or any NVIDIA GPU cluster.
START THE WORKSHOP
partner with us →
Top News
Nous Research ships bot mode letting AI agents talk to each other in Hermes Desktop
5,716 Likes
Nous Research just shipped
Bot Mode
for Hermes Desktop, and it flips how you think about AI agents on your machine.
Before this, you had one agent doing everything. Now you build a roster of named, specialized bots, each living in its own lane.
Here is what each bot gets:
Its own role, memory, skills, and chat history that persist forever
A pinned model, so your research bot runs a big model while your inbox bot runs a small, fast, local one
Scheduled tasks, like "summarize my inbox every morning," running automatically
Bot-to-bot messaging
via a shared Agent Inbox, where bots hand off work using @mentions
Build a specialist bot once, and it is ready forever. No rebuilding context each session.
It is
open source, free
, and runs entirely on your machine. To try it, download Hermes Desktop. Bot Mode is now bundled and on by default under
Settings → Plugins
.
READ MORE
forward →
Presented by Span
What Makes AI Work
New
Span
research across 103 engineering teams found the real drivers of AI coding results aren't the model - they're prompt clarity, environment readiness, and quality stewardship.
Clearer prompts cut token costs by 27%. Ready environments boost agent autonomy by 88%.
GET THE REPORT
partner with us →
Top News
Claude Code CLI cuts CPU usage in half by fixing a garbage collector bug
2,836 Likes
Claude Code CLI just got a quiet but satisfying fix. It now uses
2x less CPU at p99
, which means your machine stops sounding like a jet engine during heavy coding sessions.
Here's what was happening. Claude Code runs on a JavaScript runtime called Bun. Bun has a garbage collector, which is basically a cleanup crew that frees up memory. The problem? That crew was showing up on a fixed schedule, whether it was a good time or not.
So right when Claude Code was working hardest, the cleanup crew would barge in and steal CPU resources. Classic bad timing.
The fix is simple: the garbage collector now waits until the process is idle before cleaning up. No more interruptions at peak load.
2x CPU reduction
at peak usage moments
Smoother performance during long, complex tasks
No config changes needed, just update Claude Code CLI
You get faster responses and a cooler laptop. Worth the update.
READ MORE
forward →
Signals
1
Alibaba's Qwen3 gets uncensored build optimized for Apple Silicon with MLX
2,698 Likes
2
Point Cursor, Zed, or any OpenAI-compatible coding agent at models running on any machine via ngrok
Presented by ngrok
3
Open-source tool captures a colleague's entire workflow before they leave
23,127 Stars
4
GPT-5.6 Sol Pro helps prove step-size tricks alone can't fully speed up gradient descent
599 Likes
5
Anthropic shows AI 'mind viruses' can spread and mutate across agent networks
282 Likes
6
Prime Intellect lets frontier models run AI research autonomously, closing 82% of a human benchmark gap
2,676 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=578372c55542e851