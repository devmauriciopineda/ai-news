# Anthropic Shopping Agents 🛍️, Qwen3 1M Context 📦, Gemini 2.5 Flash 🔥

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Thu, 3 Sep 2026 14:28:46 +0000

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
Both Alibaba and Google shipped upgrades yesterday, no new model numbers, just sharper versions of what already exists. That's the new normal: post-training is the product now.
Meanwhile, an 8-year research paper quietly dropped, showing LLMs secretly build symbolic structure inside their vectors on their own. If that holds, we can finally inspect and steer these things, not just prompt and pray.
Better models, lower prices, and now interpretability. We're having a moment.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 37 sec
Top Repo
▸ Anthropic open-sources
Claude shopping agents
that boost cart size by 35%
OpenRouter
▸
O
n
e
A
P
I
F
o
r
E
v
e
r
y
M
o
d
e
l
Top News
▸ Qwen upgrades its 2.4T
parameter model with
1M token context at $2 per million
Vanta
▸
S
t
o
p
l
o
s
i
n
g
d
e
a
l
s
t
o
c
o
m
p
l
i
a
n
c
e
d
e
l
a
y
s
Top News
▸ Google ships Gemini 2.5 Flash with stronger coding and
multi-step reasoning
at same price
Signals
1. MiniMax H3 Max is fast enough to power
real-time interactive games
2.
Granola:
Walk out of in-person meetings with notes done. Granola on Apple Watch: tap your wrist and focus on the person you're meeting
3. 8-year study finds LLMs secretly
build symbolic structure
inside their vectors
4. New paper explains why some
generative models need
100 steps and others just one
5. Google's framework lets small AI agents outperform models 3x their size using a
persistent knowledge wiki
6. Meta ships Muse Spark 1.3 with 25% fewer tokens and
smarter agentic coding
Top Repo
Anthropic open-sources Claude shopping agents that boost cart size by 35%
6,219 Likes
Anthropic just open-sourced
Claude Commerce Agents
, a ready-to-use blueprint for building AI shopping assistants. Think of it as a starter kit so you skip weeks of figuring out how to wire an AI agent to a store backend.
There are two agents included:
Shopping agent
: sits inside a customer-facing app, searches products, fills carts, and answers order questions
Merchant agent
: helps store staff manage listings, inventory, and pricing, but every change waits for a human to approve it
Four vertical demos
: retail, travel, telecom, and entertainment, all runnable out of the box
A Claude Code plugin
that scaffolds an agent against your own backend automatically
Real results from pilots:
35% larger carts
and shoppers
60% more likely to complete a purchase
. To get started, clone the repo, add your API key, and run
python
scripts
/
run_demo
.
py
retail
.
READ MORE
forward →
Presented by OpenRouter
One API For Every Model
OpenRouter
gives you access to 500+ AI models from 80+ providers through one API.
Switch models without rebuilding your stack, route requests based on price, performance, and availability, and stay resilient with automatic failover when providers go down.
Get the flexibility to use the right model for every request - without juggling provider keys or managing complex routing infrastructure.
START BUILDING NOW
partner with us →
Top News
Qwen upgrades its 2.4T parameter model with 1M token context at $2 per million
5,733 Likes
Alibaba just pushed an update to
Qwen3.8-Max
, and the new version is called
Qwen3.8-Max-0902
. Same giant model underneath, but with extra post-training focused on coding and collaborative work tasks.
Quick recap of what this thing actually is: a 2.4-trillion-parameter model with 95B active parameters and a
1M-token context window
. That context window means you can feed it an entire large codebase in one shot.
The upgrade sharpens it for real enterprise work. Here is what it handles well:
PaperBench score of
93.0
, ahead of GPT-5.6 Sol, Claude Fable 5, and Opus 4.8
OSWorld-Verified score of 86.1, beating GPT-5.6 Sol Max and Claude Fable 5
Strong vision across satellite imagery, documents, technical drawings, and crowded scenes
Pricing stays the same: $2 per 1M input tokens and $6 per 1M output tokens, plus cache discounts. You can hit it right now via the QwenCloud API.
READ MORE
forward →
Presented by Vanta
Stop losing deals to compliance delays
Your prospects won’t sign without proof of security. A proof of compliance request stalls deals and pulls engineers into audit prep.
Vanta
gets you compliant fast (SOC 2, ISO 27001, HIPAA+) and keeps you that way. Trusted by 16,000+ companies like Ramp, Harvey, and Writer. See how it works below.
WATCH ON DEMAND
partner with us →
Top News
Google ships Gemini 2.5 Flash with stronger coding and multi-step reasoning at same price
3,949 Likes
Google just dropped
Gemini 3.8 Flash
, and the pitch is simple: smarter reasoning, same low price as 3.7 Flash.
So what actually changed? The model now works harder on tough tasks. The performance boost comes from a design choice: it executes extra internal reasoning steps and calls tools repeatedly to reach better answers. Think of it like a teammate who keeps double-checking their work instead of stopping at the first answer.
Here is what it is good at:
On long-horizon coding, it beats most larger, pricier models at solving complex engineering problems end to end.
On Terminal-Bench 2.1, an agentic terminal coding test, it scores
89.4%
, edging out Claude Opus 5.
It handles text, image, audio, video, and PDF input with a
1M token context window.
Pricing stays at
$0.75 per 1M input tokens
and $3.75 per 1M output. If you need lower compute overhead, you can adjust effort settings or stay on 3.7 Flash. You can try it now via the Gemini API and AI Studio.
READ MORE
forward →
Signals
1
MiniMax H3 Max is fast enough to power real-time interactive games
3,203 Likes
2
Walk out of in-person meetings with notes done. Granola on Apple Watch: tap your wrist and focus on the person you're meeting
Presented by Granola
3
8-year study finds LLMs secretly build symbolic structure inside their vectors
900 Likes
4
New paper explains why some generative models need 100 steps and others just one
866 Likes
5
Google's framework lets small AI agents outperform models 3x their size using a persistent knowledge wiki
406 Likes
6
Meta ships Muse Spark 1.3 with 25% fewer tokens and smarter agentic coding
2,505 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=7f3e3f23495ae8b8