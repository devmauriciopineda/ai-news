# Reflection Beam runs 501B params with only 23B active — 4x cheaper

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 6 Oct 2026 13:31:54 +0000

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
Two big moves yesterday, one pattern: the open web is getting
provenance-aware
.
OpenAI's textGrain watermarks AI text invisibly, nudging word choices against a hidden key. Regulation-driven, yes. But it signals that who made this is becoming infrastructure. Meanwhile, Reflection's Beam drops 501B parameters with only 23B active at once. Smarter, cheaper, open.
Efficiency and accountability are now the same race.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 46 sec
Top News
▸ OpenAI adds
invisible text watermarks
to ChatGPT to meet EU AI Act rules
The Linux Foundation
▸
S
e
e
W
h
a
t
’
s
N
e
x
t
f
o
r
P
y
T
o
r
c
h
a
n
d
A
I
Top News
▸ Reflection releases Beam, a 501B
open-source model 4x
more inference-efficient than rivals
Datalab
▸
A
n
e
x
t
r
a
c
t
i
o
n
b
e
n
c
h
m
a
r
k
t
h
a
t
s
h
o
w
s
i
t
s
w
o
r
k
Top News
▸ Vals AI uses 90 Claude agents to find two
room-temperature magnetic semiconductor
candidates in 3 days
Signals
1. DeepSeek open-sources its GPU math library,
cutting token costs
by 98%
2.
Multiverse Computing:
Multiverse Computing releases an optimized Whisper Large V3 Turbo, 15x cheaper than other speech-to-text APIs
3. Princeton's 4B model plays chess at grandmaster level and explains every move
4. New open-source
world model predicts
molecules, weather, and patients with one framework
5. FlashAttention-3 has a
hidden BF16 bug
that silently wrecks training after 25B tokens
6. Open-source trick turns your iPhone into a Mac's GPU,
boosting Qwen 27B
speed by 40%
Top News
OpenAI adds invisible text watermarks to ChatGPT to meet EU AI Act rules
7,160 Likes
OpenAI just launched
textGrain
, an invisible watermark baked into text from ChatGPT and Codex. Here is what you need to know.
Think of it like a secret fingerprint. The model subtly nudges its word choices against a hidden key, hiding a statistical pattern you cannot see but a detector can find. It does not slow the model down or change how responses read.
What does it actually tell you? Just one thing: this text was probably made by an OpenAI model. It does not name a user, account, or prompt.
API access is opt-in globally, off by default outside the EU rollout.
EU ChatGPT and Codex users get it automatically over the coming weeks.
The detector is limited to approved researchers and expert organizations for now.
Big caveat: editing a quarter of the words cuts detection to 17%. Short texts and translations are even harder to detect reliably.
This opens up content verification pipelines for EU-facing products. If you build tools that publish or moderate AI-assisted content,
machine-readable provenance
is now a real requirement you need to plan for.
READ MORE
forward →
Presented by The Linux Foundation
See What’s Next for PyTorch and AI
The AI stack is moving fast. At PyTorch Conference North America, go deep on the advances shaping what comes next - from PyTorch and vLLM to distributed training, inference, model optimization, and performance. Hear how researchers and engineers are tackling technical challenges, pushing performance, and turning new approaches into production systems.
Just two weeks to go - join us Oct 20–21 in San Jose. AlphaSignal readers save 25% with code ALPHA25 through Oct 13.
Register now + Save
!
GET 25% OFF NOW
partner with us →
Top News
Reflection releases Beam, a 501B open-source model 4x more inference-efficient than rivals
6,849 Likes
Reflection AI just dropped
Beam
, its first open model, and the efficiency numbers are hard to ignore.
Here is the trick: Beam has 501B total parameters, but only
23B are active at once
. Think of it like a huge library where you only pull the books you actually need. You get big-model smarts without paying big-model compute costs.
3-4x cheaper to run than GLM-5.2, a rival model with 250B more parameters
1M token context window
, so you can feed it massive codebases
Built for coding, tool use, and running multi-step AI agents
Apache 2.0 license, meaning you can use it commercially, no strings attached
FP8 and NVFP4 formats available for efficient self-hosting
This opens up running a frontier-class model on your own infra without a massive GPU bill. Early independent benchmarking calls it one of the most token-efficient open models seen at this capability level. Full weights drop this month.
READ MORE
forward →
Presented by Datalab
An extraction benchmark that shows its work
Comparing extraction models is hard when datasets and scoring differ.
Datalab's OmniExtractBench
brings together 620 documents, 4 sources and 10 systems.
It includes clear rules and field-level verdicts that show what each model got right, missed or invented. Explore the code yourself.
RUN THE BENCHMARK
partner with us →
Top News
Vals AI uses 90 Claude agents to find two room-temperature magnetic semiconductor candidates in 3 days
5,678 Likes
For decades, scientists searched for materials that could sort electrons by their spin (think of spin like a tiny magnetic arrow pointing up or down) while staying magnetic at room temperature. Nobody found one. Then
90+ AI agents
ran hundreds of simulations in just
3 days
and surfaced two real candidates.
Here is what makes this interesting. One material, KV[Cr(CN)₆], was actually made in a lab back in 1999. Its spin-sorting ability was hiding in plain sight for 27 years. Nobody thought to look for it.
The two candidates found:
YBaMnFeO₅
: a completely new design, never proposed before, predicted to stay magnetic above room temperature
KV[Cr(CN)₆]
: already synthesized, now predicted to sort electrons by spin with a 2.1 eV energy gap
These are simulation predictions, not lab measurements yet. The next step is re-making KV[Cr(CN)₆] and actually measuring the spin sorting. All inputs, outputs, and scripts are public with a one-command checker you can run yourself.
READ MORE
forward →
Signals
1
DeepSeek open-sources its GPU math library, cutting token costs by 98%
3,399 Likes
2
Multiverse Computing releases an optimized Whisper Large V3 Turbo, 15x cheaper than other speech-to-text APIs
Presented by Multiverse Computing
3
Princeton's 4B model plays chess at grandmaster level and explains every move
833 Likes
4
New open-source world model predicts molecules, weather, and patients with one framework
816 Likes
5
FlashAttention-3 has a hidden BF16 bug that silently wrecks training after 25B tokens
546 Likes
6
Open-source trick turns your iPhone into a Mac's GPU, boosting Qwen 27B speed by 40%
2,718 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=0b43443c1b00c851