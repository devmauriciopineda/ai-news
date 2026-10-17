# 🤖 DeepSeek V4-Flash beats V4-Pro on 9 benchmarks, same size

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Mon, 3 Aug 2026 13:33:52 +0000

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
The real story today isn't bigger models. It's
better training
.
DeepSeek's V4-Flash just beat its own flagship Pro on agent benchmarks, same size, just retrained. Alibaba's Qwen3.8-Max codes autonomously for 10 days straight. And a new paper shows a simple for-loop boosts image generation efficiency 6x.
We're watching post-training become the new moat. Raw parameters matter less every week.
In Partnership with
·
AlphaSignal In-Person Event / SF, CA on 8.6.26
🍕 Build an AI agent. Order a pizza. Win $2,500. You have 90 minutes.
No hackathon prep. No pre-built demos. No safety net.
At AlphaSignal’s Pizza Agent Challenge in SF, competitors get 90 minutes to build an agent from scratch that autonomously orders a pepperoni jalapeño pizza. First box through the door wins $2,500.
Come build, watch the chaos, and network with the room.
Register to attend today!
Thank you to our sponsor
, Brave, for making this event possible. Power your agents and chatbots with the world’s largest independent index of the web — third-party verified for the highest agent quality score and lowest latency among leading search APIs. Learn more at
Brave.com/search/api
Save Your Seat
Summary
Read time: 7 min 12 sec
Top News
▸ DeepSeek launches V4-Flash API with
stronger agent skills
and Codex support
WorkOS
▸
W
o
r
k
O
S
P
i
p
e
s
:
M
o
r
e
c
o
n
t
e
x
t
m
a
k
e
s
f
o
r
s
m
a
r
t
e
r
p
r
o
d
u
c
t
s
Top Repo
▸ Open-source Rust tool
classifies PDFs
in 20ms, no OCR needed
Anyscale
▸
R
a
y
S
u
m
m
i
t
+
v
L
L
M
C
o
n
f
e
r
e
n
c
e
Top News
▸ Qwen releases 2.4T parameter model that
codes autonomously
for 10+ days straight
Signals
1. Open-source tool builds
Apple-style 3D scroll
sites for $27 instead of $15,000
2.
Render:
Define tasks with Render SDK and chain them into distributed workflows. Queuing, orchestration and retries handled
3. ZOMI releases open-source course on
large model infrastructure
and distributed training
4. New training trick
boosts image generation
6x more efficiently with just a for loop
5. Frontis AI open-sources a
self-improving ML agent
that beats GPT-5.5 on one RTX 4090
6. Open-source tool lets you
visualize any place
on Earth at any point in history
Top News
DeepSeek launches V4-Flash API with stronger agent skills and Codex support
32,653 Likes
DeepSeek just pushed
V4-Flash into public beta
, and the story here is not a bigger model. Same architecture, same size as the preview. They just retrained it, and the numbers jumped hard.
The agent scores now beat the higher-tier V4-Pro-Preview across all nine benchmarks. We're talking about a lighter model outrunning its own bigger sibling on real coding tasks:
Terminal Bench 2.1: 82.7
vs 72.1 for V4-Pro-Preview, nearly matching Anthropic's Opus-4.8 at 85.0
DeepSWE: 54.4 vs 7.3 for the preview
DSBench-FullStack: 68.7 vs 37.0 for the preview
Native
Responses API
support plus full Codex integration, out of the box
To use it, just set your model to
deepseek-v4-flash
. No URL changes, no auth changes. If you were already calling this endpoint, you got the upgrade automatically.
Note: scores are vendor-reported, not independently verified yet. V4-Pro API and the web app are still unchanged.
READ MORE
forward →
Presented by WorkOS
WorkOS Pipes: More context makes for smarter products
Users expect apps and agents to reach the tools they already work in. Every integration that gets you there is a different OAuth flow, a different token lifecycle, weeks of infrastructure before you write a line of product code.
WorkOS Pipes
handles it with one API call. Pre-built connectors for GitHub, Slack, Salesforce, Google Drive, and more. Pipes handles OAuth, token refresh, and credential storage. You call the real provider API with a fresh token, every time.
CONNECT YOUR STACK
partner with us →
Top Repo
Open-source Rust tool classifies PDFs in 20ms, no OCR needed
10,378 Likes
PDFs have always been a pain for AI agents. You send one through OCR (a slow process that reads text from images), and you wait seconds per page. Firecrawl just shipped
pdf-inspector
to fix that.
The trick: not every PDF needs OCR. About
54% of PDFs
are already text-based, like reports, invoices, and research papers. pdf-inspector checks which type you have in roughly 20ms, then skips OCR entirely for text-based files and only sends scanned pages through the slow path.
What you get out of it:
Clean markdown with correct reading order, tables, and formulas preserved
200 PDFs processed in under 5 seconds
, faster than every competing tool
Works in Python, Node.js, Rust, or the CLI
No external services, no GPU needed for text PDFs
You can drop it in with pip install pdf-inspector or npm install @firecrawl/pdf-inspector. It is fully open source under MIT.
READ MORE
forward →
Presented by Anyscale
Ray Summit + vLLM Conference
Catch sessions and network with the teams building at the frontier of AI:
Get trained on Ray, vLLM, DeepSpeed on other top oss frameworks
60+ sessions on RL, Physical AI, Foundation models for life sciences & more
Keynotes from CTOs and Heads of AI across industries
Get 50% off with code RS26SUMMITMKTG50
GET YOUR TICKET
partner with us →
Top News
Qwen releases 2.4T parameter model that codes autonomously for 10+ days straight
5,509 Likes
Alibaba just dropped
Qwen3.8-Max
, a massive
2.4 trillion parameter
model built to handle real, long-running tasks on its own. Think of parameters as the model's "brain cells" -- more means more capacity to reason and plan.
Here's what makes it different from typical AI models:
It ran
10+ days of autonomous coding
-- starting from an empty folder and shipping production code with zero hand-holding
It handles text, images, video, and documents all in one model -- and uses what it sees to check and fix its own work
It ran 500+ rounds of chip design optimization and a full year of e-commerce planning, all on its own
API-compatible with both OpenAI and Anthropic protocols, so you can point existing tooling at it without a rewrite
You can access it now via Alibaba Cloud's API. Pricing sits at
$2/M input tokens
and $6/M output, with cached input dropping to just $0.25/M. Open weights for Qwen3.8-Max and the smaller Qwen3.8-27B are coming next week.
READ MORE
forward →
Signals
1
Open-source tool builds Apple-style 3D scroll sites for $27 instead of $15,000
4,389 Likes
2
Define tasks with Render SDK and chain them into distributed workflows. Queuing, orchestration and retries handled
Presented by Render
3
ZOMI releases open-source course on large model infrastructure and distributed training
7,790 Stars
4
New training trick boosts image generation 6x more efficiently with just a for loop
2,645 Likes
5
Frontis AI open-sources a self-improving ML agent that beats GPT-5.5 on one RTX 4090
252 Likes
6
Open-source tool lets you visualize any place on Earth at any point in history
3,732 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=f50ea4edf88c4f6a