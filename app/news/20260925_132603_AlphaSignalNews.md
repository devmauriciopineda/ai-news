# Claude Marketplace launches with 2,000+ plugins and unified billing

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Fri, 25 Sep 2026 13:26:03 +0000

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
AI models now have
fingerprints
. Researchers can identify which LLM answered with 80% accuracy just from personality tests. Claude is empathetic, GPT is egalitarian, DeepSeek dodges questions. Not blank slates anymore.
Meanwhile, Anthropic turned Claude into a
platform
with 2,000+ plugins. And NVIDIA shipped a tiny 100M-parameter model that knows
who said what
in a room of eight people.
The pattern? AI is getting specific. Identifiable personalities, niche models, ecosystem lock-in. The generic AI era is quietly ending.
In Partnership with
·
Upcoming Webinar: Your Audio Data Passed. But Is It Actually AI Ready? (9/29/26)
A strong DNSMOS score can still hide audio problems that quietly hurt TTS, voice cloning, and ASR models.
Join AlphaSignal and Voices for a technical deep dive into the “grey zone” between good-looking scores and truly training-ready audio. Geoff Bremner, Senior Audio Software Engineer at Voices, will break down where automated quality metrics fall short, why reverb is especially tricky, and how teams can make better calls on which audio is actually worth keeping.
Plus, you’ll hear live audio comparisons so you can hear the difference for yourself.
Register Today
Summary
Read time: 6 min 59 sec
Top News
▸ NVIDIA releases 100M-parameter
speaker tracking model
with 24% lower error than rivals
Prior Labs
▸
Y
o
u
r
s
t
r
o
n
g
e
s
t
b
a
s
e
l
i
n
e
d
e
s
e
r
v
e
s
a
c
h
a
l
l
e
n
g
e
r
Top News
▸ Anthropic launches
Claude Marketplace
to browse agents, plugins, and service partners
Origin Technology
▸
S
e
e
w
h
a
t
y
o
u
r
A
I
a
g
e
n
t
s
d
i
d
,
p
r
o
m
p
t
t
o
o
u
t
c
o
m
e
Top News
▸ OpenAI releases open
mental health benchmark
built with 80 clinicians
Signals
1. New open-source 8B model hits 81.6% on coding benchmarks at 9x
faster inference
2.
Sentry:
How to tell whether your agent's bad answer came from the prompt or the tool. Live Oct 7. Save your spot
3. Open-source stock monitor uses a 9-agent AI team to analyze your portfolio
4. Psychological tests can
identify which LLM
answered with over 80% accuracy
5. Viggle ships
turbo image model
that runs in 6 steps instead of 40
6. Unreal Labs ships open-source
agent harness
that's 39% cheaper than rivals
Top News
NVIDIA releases 100M-parameter speaker tracking model with 24% lower error than rivals
9,743 Likes
Ever tried reading a transcript from a meeting with four people talking over each other? It's a mess. That's the problem
speaker diarization
solves: figuring out who said what, and when.
NVIDIA just dropped
Nemotron 3 Diarization
, an open model that does exactly this, even when voices overlap. It's small at
100M parameters
, runs on live audio or pre-recorded files, and supports up to eight speakers.
It ranked
#1 out of 12 systems
on VoiceArena's Diarization-Bench, with a 14.72% error rate, roughly 24% better than the runner-up.
Here's what you can build with it:
Meeting transcripts with per-speaker labels
Multi-speaker voice agents and call analytics
Real-time captions for live conversations
Pair it with an ASR (speech-to-text) model to get full transcripts with speaker names attached. It's live on Hugging Face with a demo you can try right now.
READ MORE
forward →
Presented by Prior Labs
Your strongest baseline deserves a challenger
Run
TabPFN-3.5
beside XGBoost, LightGBM or the model your team already uses and compare using your own data. It ranks #1 across tabular benchmarks, from TabArena to BeyondArena, ahead of every classical and foundation model.
If your model wins, you know. If TabPFN wins, you know before putting it into production.
Open-source. Published in Nature. 4M+ downloads.
BENCHMARK TABPFN
partner with us →
Top News
Anthropic launches Claude Marketplace to browse agents, plugins, and service partners
5,685 Likes
Anthropic just launched
Claude Marketplace
, and it's basically an app store for Claude. One place to find everything you need to plug Claude into your existing stack.
Here's what you can actually do with it:
Add connectors and plugins
-- over
2,000 at launch
, including Google Drive, Slack, Notion, Salesforce, and Microsoft 365. Connect Claude to tools your team already uses.
Buy Claude-powered agents
from companies like Cursor, CrowdStrike, and Snowflake. The cool part: you can use your existing Anthropic budget toward these purchases, no separate billing.
Hire consulting partners
like Accenture or Deloitte if you need help rolling Claude out at scale.
Connectors are built on MCP (Model Context Protocol), an open standard that lets Claude talk to external tools and data sources. Think of it like a universal adapter.
If you're building something for Claude users, you can list your own tool or agent on the marketplace to reach teams already using Claude.
READ MORE
forward →
Presented by Origin Technology
See what your AI agents did, prompt to outcome
Most tools log single agent events, not the chain from instruction to outcome.
On Oct 1 at 11 AM ET
, SACR analyst Lawrence Pingree and Origin CEO Spencer Thompson walk through SACR's Endpoint Control and Prevention report and show how agent runtime observability traces make that chain visible.
RESERVE YOUR SEAT
partner with us →
Top News
OpenAI releases open mental health benchmark built with 80 clinicians
4,926 Likes
Most AI mental health tests only check one thing: does the model avoid saying something dangerous in a crisis? That leaves out most of what people actually talk about. OpenAI just shipped
MentalHealthBench
to fix that.
It covers the full range of real conversations, scored across
three levels
:
Everyday stress, rough weeks, emotional strain
Serious distress without an immediate emergency
Crisis situations needing real-world help
The benchmark has
1,215 synthetic conversations
, built with over 80 licensed psychologists and psychiatrists across 22 countries and 19 languages. Each conversation has expert-written scoring criteria that reward good behavior and penalize bad ones.
Top scores so far: GPT-6 Astra at 57.3%, Claude Opus 5.5 at 52.4%. Nobody is close to perfect yet.
It is fully open. You can run it on your own app's prompts and guardrails, not just on big models. If you are building anything that touches user wellbeing, this is the tool to stress-test it.
READ MORE
forward →
Signals
1
New open-source 8B model hits 81.6% on coding benchmarks at 9x faster inference
4,512 Likes
2
How to tell whether your agent's bad answer came from the prompt or the tool. Live Oct 7. Save your spot
Presented by Sentry
3
Open-source stock monitor uses a 9-agent AI team to analyze your portfolio
1,771 Stars
4
Psychological tests can identify which LLM answered with over 80% accuracy
390 Likes
5
Viggle ships turbo image model that runs in 6 steps instead of 40
12,425 Downloads
6
Unreal Labs ships open-source agent harness that's 39% cheaper than rivals
4,411 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=e53c1b581ec9b101