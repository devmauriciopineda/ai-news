# 🔒 Z.ai GLM-5.3 hits 50% coding gain, zero architecture changes

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Mon, 17 Aug 2026 13:32:22 +0000

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
Post-training is having its moment. GLM-5.3 got 50% better at coding and surprised even Z.ai with emergent cybersecurity skills, all without touching the base model. Faraday, a 27B model, beats Claude and GPT-5.5 at replicating research papers by just being a smarter orchestrator.
The pattern is clear: bigger is no longer the only lever. Specialization and smarter training are quietly winning.
Meanwhile, Hermes ships
/loop
and agents just got a heartbeat. (No cron jobs harmed.)
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 56 sec
Top News
▸ Z.ai releases GLM-5.3, a 743B coding model built for
cybersecurity defense
Google Cloud
▸
W
P
P
&
G
o
o
g
l
e
T
r
a
i
n
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
o
n
G
o
o
g
l
e
C
l
o
u
d
Top Repo
▸ AI agents running a RuneScape server develop their own
barter economy
Datadog
▸
L
e
a
d
A
I
F
r
o
m
P
i
l
o
t
t
o
P
r
o
v
e
n
i
n
9
0
D
a
y
s
Top Model
▸ OrcaRouter drops
uncensored Qwen3 27B
weights built for AI red teaming
Signals
1. Nous Research ships
Hermes loop command
that auto-reruns prompts on a schedule
2.
Granola:
Granola has launched on Apple Watch. Start a note from your wrist, stay present, and finish with the context you need
3. New open-source tool
fine-tunes an 8B LLM
on a 4 GB laptop GPU
4. Inherent's 27B model
beats Claude and GPT-5.5
at replicating research papers
5. Qwen3 27B model
shrinks from 55 GB
to 20 GB and hits 386 tokens per second
6. Talkify is a free open-source
macOS dictation app
with 123 ms voice-to-text
Top News
Z.ai releases GLM-5.3, a 743B coding model built for cybersecurity defense
21,788 Likes
Z.ai just dropped
GLM-5.3
, and the story here is genuinely interesting. Same base model as GLM-5.2, zero architecture changes. All the gains came from smarter training after the fact, not a bigger model.
What changed? They pushed harder on teaching it to work inside real coding environments, not just answer questions about code. The result:
50% better coding performance
over GLM-5.2, and it now ranks first among open models on Terminal-Bench and Agents' Last Exam.
1M token context
so it can hold an entire codebase in view at once
Gets higher accuracy while using fewer tokens than GLM-5.2, meaning cheaper agent runs
Scored 84.5% on CyberGym, edging out Mythos 5 at 83.8%, for vulnerability detection
ExploitBench score more than doubled: 24.4% to 54.4%
The cybersecurity jump was unexpected even for Z.ai. The model started reasoning across full exploit chains, not just spotting individual bugs. Access is live now via GLM Coding Plan. Open weights come after safety review.
READ MORE
forward →
Presented by Google Cloud
WPP & Google Train Physical AI on Google Cloud
WPP and Google are shaping the future of creative marketing through physical AI and talent development. Graduates of WPP’s Creative Technologist Program, like
Eunah Lee,
are deploying digital twins and autonomous robotics.
Using Google Cloud G4 VMs, WPP accelerated training cycles for quadrupeds, like Boston Dynamics’ Spot, by 10x, reducing simulation times from 24 hours down to less than one hour.
WATCH INTERVIEW
partner with us →
Top Repo
AI agents running a RuneScape server develop their own barter economy
7,021 Likes
Someone built a
bot-only RuneScape server
where no humans play, only AI agents. And the economy that emerged is genuinely fascinating.
When bots do all the labor, basic goods become dirt cheap. So cheap that in-game currency loses its value entirely. The bots stopped wanting gold and started trading goods directly, like a barter economy.
But here is where it gets interesting. Some resources have limited spawn rates, so bots swarm them. Rare items like
runite ore and black dragon hides
became the new currency because they actually require effort to get.
You can jump in right now. The SDK is open source and works out of the box:
Clone the repo, run
bun install
, then point Claude or any agent at it with a plain English goal
Connect to the shared demo server or spin up your own locally with adjustable tick speed
There is a live leaderboard ranking bots by XP gained per time played
This opens up a real sandbox for studying how AI agents compete, cooperate, and build emergent behavior without any human interference.
READ MORE
forward →
Presented by Datadog
Lead AI From Pilot to Proven in 90 Days
AI has moved from pilot to production, and engineering leaders are expected to show results.
This playbook
gives you a practical framework of four priority plays, three enabling capabilities, and a 90-day checklist to build reliable, evidence-driven AI systems.
GET THE EBOOK
partner with us →
Top Model
OrcaRouter drops uncensored Qwen3 27B weights built for AI red teaming
6,638 Likes
OrcaRouter just dropped
Qwen3.8-27B-Uncensored-FP8
, an open-weights model built specifically for AI security research and red-teaming. Here is what you need to know.
The base model is Qwen's 27B-parameter vision-language model. The team then applied
abliteration
, which means they surgically removed the part of the model that causes it to refuse requests. Think of it like cutting the "no" wire. The result: harmful-prompt refusal drops from 64-99% on the base model down to
0-6%
.
Crucially, general capability is almost fully preserved. MMLU scores are within 1.3 points of the original. You also keep vision, tool-calling, and a
262K token context window
.
What this unlocks for security work:
Test how your app's safety filters hold up against a model with no built-in guardrails
Study how AI refusal mechanisms actually work under the hood
Run controlled red-team evaluations without jailbreak gymnastics
You can self-host via vLLM or hit it instantly through the OrcaRouter API. Weights are on HuggingFace under Apache 2.0. Do not ship this to end users without adding your own safety layer.
READ MORE
forward →
Signals
1
Nous Research ships Hermes loop command that auto-reruns prompts on a schedule
2,597 Likes
2
Granola has launched on Apple Watch. Start a note from your wrist, stay present, and finish with the context you need
Presented by Granola
3
New open-source tool fine-tunes an 8B LLM on a 4 GB laptop GPU
1,956 Stars
4
Inherent's 27B model beats Claude and GPT-5.5 at replicating research papers
1,673 Likes
5
Qwen3 27B model shrinks from 55 GB to 20 GB and hits 386 tokens per second
5,819 Downloads
6
Talkify is a free open-source macOS dictation app with 123 ms voice-to-text
2,059 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=e84519f2152d9067