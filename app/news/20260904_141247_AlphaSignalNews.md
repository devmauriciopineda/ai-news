# Anthropic Claude Shopping 🛍️, Cursor Self-Hosted Agents 🖥️, NVIDIA DLS

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Fri, 4 Sep 2026 14:12:47 +0000

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
Agents are no longer demos. They're shipping into your store, your codebase, your enterprise firewall.
Anthropic open-sourced a full commerce agent blueprint. Cursor moved coding agents behind your own firewall. A new reasoning model solves Sudoku at 99.5% with 44x less compute. The pattern is clear: the bottleneck shifted from "can AI do this?" to "can we actually deploy it?"
We're in the infrastructure era now. And it's moving fast.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 49 sec
Top News
▸ Anthropic open-sources
Claude shopping agents
that grow cart sizes by 35%
Finest
▸
S
a
v
e
u
p
t
o
7
0
%
o
n
A
I
s
p
e
n
d
w
i
t
h
t
w
o
l
i
n
e
s
o
f
c
o
d
e
Top Repo
▸ Developer releases open-source demo applying DLSS 5 to
live webcam footage
Google Cloud
▸
O
n
l
y
1
7
%
o
f
I
T
T
e
a
m
s
F
e
e
l
R
e
a
d
y
f
o
r
A
I
A
g
e
n
t
s
Top News
▸ Cursor lets you run
cloud coding agents
on your own infrastructure
Signals
1. Meta releases Muse Spark 1.3, the
cheapest model
at its intelligence level
2.
Tiger Data:
One database for metrics, embeddings, and analytics, all in Postgres. Start a trial, get $1000 in credits
3. New reasoning model
solves Sudoku
at 99.5% accuracy with 44× fewer compute operations
4. New framework uses incentive design to
stop AI agents
from sandbagging or faking alignment
5. New transformer trick cuts training compute by up to 18% by
looping middle layers
twice
6. Claude can now
control your Mac
apps silently in the background
Top News
Anthropic open-sources Claude shopping agents that grow cart sizes by 35%
12,250 Likes
Anthropic just open-sourced
Claude Commerce Agents
, a ready-to-use blueprint for building AI shopping assistants. Think of it as a starter kit, not a finished product.
There are two agents baked in:
Shopping agent
: sits inside a store's app, chats with customers in plain language, finds products, and adds items to their cart
Merchant agent
: a back-office tool for store staff that tracks sales, monitors inventory, flags problems, and drafts promotions. Nothing goes live until a human approves it.
The repo ships with
four working demos
across retail, travel, telecom, and entertainment. You clone it, drop in your API key, and a vertical spins up locally.
There's also a Claude Code plugin that reads your existing stack and scaffolds a custom agent against your own backend.
It deploys wherever you already use Claude: the Claude API, Amazon Bedrock, Microsoft Foundry, or Google Cloud Vertex AI. Early results show
carts up 35%
and shoppers 60% more likely to check out.
READ MORE
forward →
Presented by Finest
Save up to 70% on AI spend with two lines of code
Most teams pick an extreme: a frontier model for everything and a bloated bill, or a cheaper model everywhere and weaker output.
Finest calibrates against your work.
Finest API
serves a lower-cost configuration only when it clears your task's quality bar. Otherwise, the model you named serves.
Finest Code
brings the same evidence-gated approach to Claude Code. Every request carries a receipt showing what served, and both prices.
BUILD WITH FINEST
partner with us →
Top Repo
Developer releases open-source demo applying DLSS 5 to live webcam footage
6,553 Likes
Someone just open-sourced a demo that pipes a
live webcam feed through DLSS 5
, NVIDIA's new AI image enhancer. Here's the quick explainer.
DLSS 5 is an AI model that takes a rendered frame and adds realistic lighting, skin texture, and material detail on top. Think of it like a photo filter, but one that actually understands what it's looking at: faces, hair, fabric, lighting conditions.
This demo hooks that same AI into your webcam in real time. It upscales from
1280x720 input to 2560x1440 output
, runs A/B split comparison so you can see before and after side by side, and even uses a person-detection model to apply the effect only to you.
What you need to run it:
An NVIDIA RTX GPU and a webcam
ReShade and the NR runtime (sourced separately, not included)
About
1.4 GB
of dependencies total
The source code is MIT-licensed and public on GitHub. The DLSS binaries are not included, so you'll need to grab those yourself through official channels.
READ MORE
forward →
Presented by Google Cloud
Only 17% of IT Teams Feel Ready for AI Agents
90% of enterprises plan to deploy AI agents within three years, but bursty workloads keep straining infrastructure and underutilized compute.
Google Cloud's
new dynamic capacity framework schedules GPU/TPU capacity ahead of demand, builds automated fallback plans, and orchestrates it all through GKE for predictable cost and performance.
GET THE PLAYBOOK
partner with us →
Top News
Cursor lets you run cloud coding agents on your own infrastructure
3,806 Likes
Cursor just shipped
self-hosted cloud agents
, and it flips how AI coding tools work inside locked-down companies.
Here is the core idea. Cursor's AI does the thinking in its cloud. But all the actual work, running code, hitting your internal APIs, reading secrets, stays on
your machines
. Nothing leaves your network.
Why does that matter? Lots of teams could not use AI agents at all because their security rules block sending code to outside servers. Many enterprises in highly-regulated spaces cannot let code, secrets, or build artifacts leave their environment. This solves that.
What you can actually do now:
Connect agents to internal databases, private APIs, and build pipelines they could not touch before
Run agents on sandbox providers like AWS Lambda, Vercel, Modal, Cloudflare, and more
Agents keep working after your laptop closes, and you can run multiple agents on different features simultaneously
Each agent connects outbound via HTTPS to Cursor's cloud for planning only, with no inbound ports or firewall changes needed. Enable it in your
Cursor Dashboard
to get started.
READ MORE
forward →
Signals
1
Meta releases Muse Spark 1.3, the cheapest model at its intelligence level
3,208 Likes
2
One database for metrics, embeddings, and analytics, all in Postgres. Start a trial, get $1000 in credits
Presented by Tiger Data
3
New reasoning model solves Sudoku at 99.5% accuracy with 44× fewer compute operations
1,388 Likes
4
New framework uses incentive design to stop AI agents from sandbagging or faking alignment
482 Likes
5
New transformer trick cuts training compute by up to 18% by looping middle layers twice
439 Likes
6
Claude can now control your Mac apps silently in the background
3,177 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=1d0f8d21d564f866