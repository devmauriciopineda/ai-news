# 🔥 DeepSeek 552B beats its own Pro model, then kills it

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Fri, 11 Sep 2026 14:14:29 +0000

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
Two big drops yesterday, and they tell the same story from opposite sides. DeepSeek ships a 552B model that beats its own Pro flagship on every metric, then retires it. Meanwhile, Anthropic publishes how bad actors tried to weaponize Claude across seven harm categories.
More power, lower cost, higher stakes. That's the loop we're in.
The open-source pressure is real, and safety is no longer optional PR.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 39 sec
Top News
▸ DeepSeek ships 552B
multimodal model
with 8x smaller cache and lower API prices
AI Conference
▸
W
h
a
t
A
r
e
A
I
’
s
T
o
p
B
u
i
l
d
e
r
s
S
e
e
i
n
g
N
e
x
t
?
Top News
▸ Anthropic publishes its most detailed report on
Claude misuse
and how it stopped them
Attio
▸
I
n
t
r
o
d
u
c
i
n
g
t
h
e
f
i
r
s
t
a
g
e
n
t
i
c
C
R
M
:
A
t
t
i
o
Top News
▸ OpenAI ships ChatGPT for
financial services
with GPT-6 and live market data
Signals
1. OpenAI ships GPT-Live-1 API so
voice agents
can listen and speak at the same time
2.
Google Cloud:
Explore strategies for powering AI agents using Google Cloud and NVIDIA-accelerated compute and custom deployment models
3. RadixArk open-sources Miles, a production-ready
reinforcement learning training
system for frontier models
4. Greg Brockman trains a virtual fly to navigate and drive autonomously
5. Nex-AGI releases agentic model family built to
browse, click, and
self-correct
6. Open-source framework runs a
35B model
on your phone using just 2 GB of RAM
Top News
DeepSeek ships 552B multimodal model with 8x smaller cache and lower API prices
25,515 Likes
DeepSeek just dropped
V4.1-Flash
, and it is quietly replacing everything in their lineup.
Here is the setup: their previous Flash model was decent, but V4-Pro was the "smart" option you paid more for. Now V4.1-Flash beats V4-Pro on speed, cost, and performance. So they are retiring V4-Pro entirely.
The architecture is the interesting part. It packs
552 billion parameters
total, but only activates 8B while reading your input and 16B while writing output. Think of it like a huge library where you only pull the books you actually need. More knowledge, less energy spent.
The biggest win for anyone building AI agents: the memory cache (the scratch pad the model keeps between calls) now needs
4x less RAM and 8x less storage
. That directly cuts your API costs.
Sees images natively, no extra setup
#1 on Terminal-Bench 2.1
, ahead of Claude Opus 5 and GPT-5.6
Off-peak pricing is 50% cheaper, schedule batch jobs accordingly
To use it: set your model to
deepseek-flash
. Old model names still route there automatically.
READ MORE
forward →
Presented by AI Conference
What Are AI’s Top Builders Seeing Next?
In two weeks, the people shaping what comes next in AI are gathering in San Francisco.
At The AI Conference
, hear from 130+ speakers, including Chris Lattner, Emmanuel Ameisen, Peter Norvig, Illia Polosukhin, co-author of “Attention Is All You Need,” plus builders from OpenAI, NVIDIA, Google, Near AI, and more.
Hear what leading AI teams are actually building and what’s changing across agents, LLMs, infrastructure, and applied AI before it becomes common knowledge.
AlphaSignal members save 30% with code ALPHA30.
GET 30% OFF
partner with us →
Top News
Anthropic publishes its most detailed report on Claude misuse and how it stopped them
18,668 Likes
Anthropic just dropped its most detailed look yet at how people tried to weaponize Claude, and every single operation got caught and shut down.
So what were people actually trying to do?
Seven harm areas
: cyber operations, influence operations, surveillance, scams and fraud, biological misuse, weapons development, and model theft.
Here are the standout findings:
Attackers used Claude not just as an advisor but to execute attacks directly. A suspected Chinese state group used it to infiltrate roughly thirty global targets.
AI has removed the skill advantage that once set state-sponsored hackers apart from lone criminals.
In one case, Claude scored social media posts by political sensitivity and flagged people for government control.
Anthropic tightened controls on newer models, restricting a broader range of dual-use biological queries.
Every operation was disrupted, safeguards were strengthened, and intelligence was shared with authorities. Protect your API keys. Seriously.
READ MORE
forward →
Presented by Attio
Introducing the first agentic CRM: Attio
With agents and automations that build pipeline, chase signals, and move deals forward,
Attio
orchestrates your revenue work around the clock.
Loved by high-growth startups like Granola, Modal, and Wispr Flow, Attio amplifies what you can achieve.
GET STARTED
partner with us →
Top News
OpenAI ships ChatGPT for financial services with GPT-6 and live market data
16,928 Likes
OpenAI just launched
ChatGPT for Financial Services
, a dedicated workspace powered by GPT-6 Astra, built with Morgan Stanley and Evercore.
The big deal? No more stitching together data sources. You can start working with these datasets immediately, with no separate contracts to negotiate or connectors to set up.
Here's what's included out of the box:
Built-in data
from Daloopa, PitchBook, LSEG News, and Crunchbase covering earnings transcripts, financial statements, and private company info
Editable research notes, financial models, and pitchbooks using your firm's own Excel, Word, and PowerPoint templates
Granular citations
that let you trace every figure back to the exact paragraph or table it came from
GPT-6 Astra has been tuned specifically for retrieval, financial reasoning, and artifact generation. That means the AI actually understands financial documents, not just text.
Eligible financial institutions can contact OpenAI sales or their account team to get access. OpenAI has not published pricing.
READ MORE
forward →
Signals
1
OpenAI ships GPT-Live-1 API so voice agents can listen and speak at the same time
13,456 Likes
2
Explore strategies for powering AI agents using Google Cloud and NVIDIA-accelerated compute and custom deployment models
Presented by Google Cloud
3
RadixArk open-sources Miles, a production-ready reinforcement learning training system for frontier models
529 Likes
4
Greg Brockman trains a virtual fly to navigate and drive autonomously
13,282 Likes
5
Nex-AGI releases agentic model family built to browse, click, and self-correct
2,444 Downloads
6
Open-source framework runs a 35B model on your phone using just 2 GB of RAM
8,776 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=d831910c5147f628