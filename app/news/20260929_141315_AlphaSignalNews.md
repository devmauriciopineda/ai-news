# Claude Sonnet 5.5 hits 70.6% on Terminal-Bench, beats Opus 5

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 29 Sep 2026 14:13:15 +0000

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
Two things dropped today that, together, tell a bigger story: models are getting cheaper and smarter at the same time. Sonnet 5.5 does more with fewer tokens. ScientistTwo writes papers that beat humans at NeurIPS.
We're past the "AI as assistant" era. The question is no longer can it help? It's how much of the job does it own?
Spoiler: more than yesterday.
In Partnership with
·
Upcoming Event: Join AlphaSignal at a16z Speedrun in SF (10/7/2026)
AlphaSignal is heading to a16z Speedrun in San Francisco.
Our CEO, Lior Alexander, will be on the main stage alongside leaders from OpenAI, Google, Palantir, Anthropic, Cognition, Box, Greylock, and more for a day of conversations about what’s next in AI.
As a community partner, we’ve also secured 50 tickets for the AlphaSignal community at 50% off. The conference is approval-only, and AlphaSignal community members will receive priority consideration.
Apply For A 50% Off Ticket
Summary
Read time: 6 min 57 sec
Top News
▸ Anthropic releases
Claude Sonnet 5.5
, 30% faster and 30% cheaper than its predecessor
AgentField AI
▸
C
o
d
e
A
F
:
n
e
a
r
l
y
4
x
C
l
a
u
d
e
C
o
d
e
'
s
s
o
l
v
e
s
,
s
a
m
e
m
o
d
e
l
Top News
▸ OpenAI
patches GPT-6 bug
that was breaking image understanding in the API
Prior Labs
▸
Y
o
u
r
n
e
x
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
i
s
j
u
s
t
o
n
e
A
P
I
c
a
l
l
a
w
a
y
.
Top News
▸ xAI launches
Grok Team Bots
that learn and coordinate work inside Slack
Signals
1. Typesafe AI's new CLI
cuts coding agent
costs by 40% on SWE-bench
2.
Google Cloud:
See how Google Cloud accelerates AI agents with NVIDIA RTX PRO GPUs and watch a live multi-agent drug discovery demo
3. DataTalks Club offers a
free 4-month hands-on
ML engineering course
4. Google's
autonomous research agent
outperforms human papers on 86 tasks by 25%
5. IST-DASLab shrinks a 354 GB coding model to 58 GB by
pruning half its
experts
6. AMD
acquires World Labs
, making Fei-Fei Li its chief scientist
Top News
Anthropic releases Claude Sonnet 5.5, 30% faster and 30% cheaper than its predecessor
66,454 Likes
Anthropic just dropped
Claude Sonnet 5.5
, and the numbers are hard to ignore.
Same price as Sonnet 5, but it uses fewer tokens to finish the same job. That means you pay up to
30% less per task
and get results
30% faster
. No price hike, just a better deal.
The coding jump is the real story. On Terminal-Bench 4.0, a test where an AI agent completes real command-line engineering tasks on its own, Sonnet 5.5 scores 70.6%, up from 10.3% for Sonnet 5 and ahead of Opus 5.5's 66.4%. That is not a small step.
Here is what it unlocks for you:
Agentic coding
: fixes bugs and navigates codebases with fewer steps and tool calls
Knowledge work
: creates polished slides, docs, and spreadsheets with minimal editing
1M token context
with 128K output, so large projects fit in one shot
Beats Sonnet 5's best score at low effort, for about one-tenth the cost
It is available now everywhere Sonnet 5 was. Just swap the model name and go.
READ MORE
forward →
Presented by AgentField AI
CodeAF: nearly 4x Claude Code's solves, same model
On DeepSWE, CodeAF solved nearly 4× as many real GitHub issues as Claude Code on the same open model, at about half the cost per solve of the next-best harness.
CodeAF is a new open-source coding harness
built for open models like DeepSeek, Qwen, GLM and Kimi: frontier-grade coding without locking you into a closed model, and it still works with any provider you choose. One small Go binary, Apache 2.0.
TRY CODEAF
partner with us →
Top News
OpenAI patches GPT-6 bug that was breaking image understanding in the API
6,198 Likes
OpenAI just quietly fixed a bug that was making
GPT-6 Sol and GPT-6 Luna
worse at understanding images. Not a new feature. Just a fix that was silently hurting your results this whole time.
What broke? The models were misreading visual inputs, meaning anything you sent with an image attached was getting worse answers than it should have. That includes the API, Codex, and computer use tasks where the model watches your screen and takes actions.
Here is what this fix unlocks for you:
Sharper answers when you send screenshots or diagrams to the API
More reliable
computer use
, where the model clicks and navigates your UI
Better Codex results when your workflow includes visual context
If you have any pipeline that sends images to these models,
rerun your tests now
. You might find your old results were being dragged down by this bug the whole time.
READ MORE
forward →
Presented by Prior Labs
Your next prediction is just one API call away.
Call
TabPFN-3.5
and get predictions back in seconds. Test more ideas, compare what works, and get state-of-the-art models into production faster.
It ranks #1 across benchmarks, ahead of every classical and foundation model.
TRY TABPFN TODAY
partner with us →
Top News
xAI launches Grok Team Bots that learn and coordinate work inside Slack
4,766 Likes
xAI just shipped
Team Bots
, and it flips the script on how AI fits into a team. Until now, your Grok Bot was yours alone. Team Bots are shared: one bot, configured once, used by everyone on the team.
Think of it like a coworker with a specific job. You give it access to your tools, teach it its role, and it keeps getting better the more your team uses it.
Each person still gets their own private conversation
, but the bot's skills and knowledge are shared across the whole group.
Here's what you can actually hand off to one:
Morning briefings and account prep
Engineering coordination and triage
Customer feedback sorting
Data questions and hiring workflows
It plugs into
Slack or Grok Bot
, and xAI ships pre-built versions for sales, marketing, product, and data analytics so you're not starting from scratch. Access is currently on
Teams and Enterprise plans
only.
READ MORE
forward →
Signals
1
Typesafe AI's new CLI cuts coding agent costs by 40% on SWE-bench
4,747 Likes
2
See how Google Cloud accelerates AI agents with NVIDIA RTX PRO GPUs and watch a live multi-agent drug discovery demo
Presented by Google Cloud
3
DataTalks Club offers a free 4-month hands-on ML engineering course
14,612 Stars
4
Google's autonomous research agent outperforms human papers on 86 tasks by 25%
1,820 Likes
5
IST-DASLab shrinks a 354 GB coding model to 58 GB by pruning half its experts
5,522 Downloads
6
AMD acquires World Labs, making Fei-Fei Li its chief scientist
3,883 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=9910f36a35dac710