# 💸 Anthropic Claude Opus 5.5: 40% cheaper, 30% faster output

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Wed, 23 Sep 2026 14:10:47 +0000

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
Both OpenAI and Anthropic dropped major model updates on the same day. GPT-6 Sol and Luna, Claude Opus 5.5: all cheaper, all faster. The pattern is clear: the frontier is getting commoditized in real time.
We're watching intelligence get priced like cloud storage. Every quarter, you get more for less. Great for builders, brutal for margins.
Meanwhile, a study found em-dash use in medical papers nearly tripled post-ChatGPT. Ironic that we banned em-dashes from our own writing.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 46 sec
Top News
▸ Anthropic
ships Claude Opus
5.5 at 40% lower cost and 30% faster output
Encord
▸
L
o
n
g
H
o
r
i
z
o
n
:
T
h
e
P
h
y
s
i
c
a
l
A
I
S
u
m
m
i
t
Top News
▸ OpenAI
ships GPT-6 Sol
and Luna at 50% lower API prices
AI Conference
▸
Y
o
u
R
e
a
d
A
b
o
u
t
A
I
D
a
i
l
y
.
N
o
w
B
e
i
n
t
h
e
R
o
o
m
.
Top Paper
▸ Study finds
em-dash use
in medical preprints nearly tripled after ChatGPT launched
Signals
1. New plugin brings
Claude Code subscriptions
back to Hermes Agent
2.
Nyra, 1.4k stars:
CrisperWhisper 2.0: an open speech-to-text model that transcribes every um, stutter, and vocal sound with precise timestamps
3. Stanford team trains agent groups to
self-organize and hit
66.7% where solo agents scored 48.8%
4. New paper reveals transformers build
faithful internal maps
of the world
5. Qwen-Image-2.1 gets GGUF quantization,
runs locally down
to 4 GB
6. New Qwen3-based model claims to
write more like
a human than any other
Top News
Anthropic ships Claude Opus 5.5 at 40% lower cost and 30% faster output
125,529 Likes
Anthropic just shipped
Claude Opus 5.5
, and the headline is simple: same top-tier quality, noticeably lower bill.
The old Opus 5 was powerful but pricey. Opus 5.5 fixes that. It matches the performance of the bigger, more expensive Fable 5.1 model on most tasks, while costing
40% less
to run on typical workloads. Output also comes back more than 30% faster.
Here is what changed under the hood:
Pricing dropped to
$4/$20 per million tokens
(input/output), down from $5/$25
Cache reads (reusing content already processed) fell 60%, from $0.50 to $0.20, which is huge for agent loops that repeat large chunks of context
Agentic coding and computer use got major upgrades, one tester migrated a 680,000-line codebase in under a day
Responses are cleaner: key info comes first, and it actually follows your writing instructions
One catch: four breaking changes affect existing Opus 5 integrations, so check the docs before swapping model IDs in production.
READ MORE
forward →
Presented by Encord
Long Horizon: The Physical AI Summit
Building robotics or autonomy systems?
Long Horizon
puts you in the room with the engineers shipping physical AI today, from DeepMind, Boston Dynamics, Waymo, Skild AI, and Wayve.
Two days of hands-on workshops and breakout sessions on data flywheels, perception, and real-world motion for humanoid robots, plus an expo floor to test sponsor demos and talk shop with the teams building them.
Join 1,000+ engineers and researchers — Oct 20-21, Fort Mason, San Francisco.
SECURE YOUR SPOT
partner with us →
Top News
OpenAI ships GPT-6 Sol and Luna at 50% lower API prices
54,457 Likes
OpenAI just dropped two new models:
GPT-6 Sol
for complex, multi-step work and
GPT-6 Luna
for high-volume, well-defined tasks like summarizing docs or answering quick questions. Both are trained with the same techniques as the flagship Astra, just faster and cheaper.
The big story is price. These are
permanent rates
, not promos:
Sol: $2 / $10 per million input/output tokens (down from $4 / $20)
Luna: $0.10 / $0.50 per million tokens (down from $0.20 / $1.20)
Both share a 1M token context window with 128k output tokens, no long-context surcharge
Cached inputs now get a 90% discount, and you can swap tools or change settings without losing that cache
Sol makes
half as many mistakes
as its predecessor. Luna matches GPT-5.6 Sol at roughly 1/100th the cost at higher effort. You can call them via
gpt-6-sol
and
gpt-6-luna
in the API right now.
READ MORE
forward →
Presented by AI Conference
You Read About AI Daily. Now Be in the Room.
Only 5 days until
The AI Conference
lands in San Francisco.
AlphaSignal readers can save 30% with code ALPHA30 and join the conversations shaping the future of AI. This exclusive member offer ends in 24 hours, so now’s the time to claim your seat in SF.
REGISTER NOW
partner with us →
Top Paper
Study finds em-dash use in medical preprints nearly tripled after ChatGPT launched
8,179 Likes
Researchers analyzed
69,632 medical preprints
and found something quietly telling about how AI is changing scientific writing.
The em-dash (this thing: –) used to appear in about
4% of research papers
. After ChatGPT launched, that number climbed to nearly 20% by 2025. AI models love em-dashes. They use them constantly. And it shows up in the data.
The key findings:
Em-dash use tripled across thousands of papers after AI tools became mainstream
The rise was gradual, not a sudden spike, suggesting slow adoption of AI writing tools
The pattern held across every test they ran, making it hard to dismiss as noise
Boilerplate sections showed almost no change, meaning the signal is real
This does not prove any specific paper used AI. It just shows that
writing patterns shifted at scale
right when AI tools arrived. Think of it as a fingerprint on a population, not on any one person.
Why care? If you build tools that detect AI content, this is exactly the kind of signal worth tracking.
READ MORE
forward →
Signals
1
New plugin brings Claude Code subscriptions back to Hermes Agent
3,417 Likes
2
CrisperWhisper 2.0: an open speech-to-text model that transcribes every um, stutter, and vocal sound with precise timestamps
Presented by Nyra, 1.4k stars
3
Stanford team trains agent groups to self-organize and hit 66.7% where solo agents scored 48.8%
359 Likes
4
New paper reveals transformers build faithful internal maps of the world
319 Likes
5
Qwen-Image-2.1 gets GGUF quantization, runs locally down to 4 GB
182,313 Downloads
6
New Qwen3-based model claims to write more like a human than any other
3,192 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=3b0069ed2fa97e1b