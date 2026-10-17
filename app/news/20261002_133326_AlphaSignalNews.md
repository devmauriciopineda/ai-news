# Anthropic Claude Code Plugins 🔌, OpenAI Codex Security Scanning 🛡️, De

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Fri, 2 Oct 2026 13:33:26 +0000

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
The coding agent wars just got a new front. Anthropic lets you mod Claude Code with TypeScript. OpenAI ships always-on security scanning for your repos. And DeepMind is quietly building a consciousness scoreboard for AI.
The pattern? AI tools are eating their own surface area, not just writing code but watching it, securing it, and modding themselves.
Someone at DeepMind noticed that consciousness signals overlap with raw capability. That's either fascinating or terrifying. Probably both.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 37 sec
Top News
▸ Anthropic opens Claude Code to
custom mods written
in TypeScript
DigitalOcean & NVIDIA
▸
O
p
e
n
I
n
t
e
l
l
i
g
e
n
c
e
S
u
m
m
i
t
b
y
D
i
g
i
t
a
l
O
c
e
a
n
&
N
V
I
D
I
A
Top Repo
▸ New open-source
prompt skill rewrites
stiff AI-generated Japanese into natural text
Fin
▸
F
i
r
e
s
i
d
e
:
L
e
a
d
i
n
g
t
h
r
o
u
g
h
t
h
e
A
I
t
r
a
n
s
f
o
r
m
a
t
i
o
n
Top News
▸ OpenAI upgrades Codex Security Cloud to
scan entire GitHub
repos automatically
Signals
1. Cursor adds
inline chart and diagram
generation directly in chat
2.
Mercor:
Mercor Research team post-trains Qwen3.5-397B-A17B using expert data to raise Pass@1 by 11.2 points on APEX-Agents
3. Google DeepMind builds a
scoring system
to measure AI consciousness without solving it first
4. New
diffusion model beats
a 6.5x larger model using 4.9x less compute
5. New 1.58-bit 27B model writes ComfyUI image prompts and
fits on a
16 GB GPU
6. Free open-source tool lets Claude Code
edit your videos
automatically
Top News
Anthropic opens Claude Code to custom mods written in TypeScript
16,862 Likes
Claude Code just got a mod system. You can now write small TypeScript plugins that hook into the agent loop, change how it behaves, and draw custom UI. Think of it like browser extensions, but for your AI coding tool.
Three built-in mods show what's possible:
Blast Radius
intercepts risky commands like rm -rf or git reset --hard, shows you what would be affected, and asks Proceed or Cancel before anything runs.
Token Weather
shows a live bar above your prompt with how full your context window is, plus a sparkline of your last 12 turns so you know when to start a fresh session.
Replay Theater
records every file edit Claude makes, then lets you step through each diff one at a time with /replay.
A mod is just a TypeScript file with hooks. You can write one yourself, or ask Claude to build it for you. Install with
/plugin
in the CLI or desktop app.
One heads-up: mods run with full access to your machine, same as Claude Code itself. Only install from sources you trust.
READ MORE
forward →
Presented by DigitalOcean & NVIDIA
Open Intelligence Summit by DigitalOcean & NVIDIA
A movement is forming around Open Intelligence: the intelligence powering your products should be open, portable, and under your control.
On Oct 13 in San Francisco, the Open Intelligence Summit, hosted by DigitalOcean and NVIDIA, brings together the teams building it that way: open weights, open tooling, open infrastructure.
Hear from Thomas Eastman (Nous Research), Lei Xu (LanceDB), Peter Walker (OpenRouter), and Yifan Qiao (Inferact). Invite-only.
REQUEST YOUR SEAT
partner with us →
Top Repo
New open-source prompt skill rewrites stiff AI-generated Japanese into natural text
7,335 Likes
You know that stiff, robotic feel AI-generated Japanese text has? Someone built a fix for it.
yomiyasu
is an agent skill that rewrites AI-generated Japanese into natural, human-readable text. The old approach was just banning certain words, which only swapped one awkward word for another. yomiyasu goes deeper.
It targets two root causes:
Broken sentence structure
(who did what to whom gets lost in AI output) -- yomiyasu restores the subject, verb, and object so each sentence stands on its own
Metaphor verbs
like "silently breaks" or "dissolves time" get replaced with precise, literal descriptions of what actually happens
It also ships with a
Python linter
that scores your text for AI-ness, flagging overuse of bold, bullet points, and vague phrasing.
You can drop it into Claude Code, Codex, or Cursor right now. Install with
npx skills add nanaism/yomiyasu
, then just paste your draft and say "make this readable."
READ MORE
forward →
Presented by Fin
Fireside: Leading through the AI transformation
Join Aaron Levie (Co-founder & CEO, Box), and Eoghan McCabe (Co-founder & CEO, Fin) on
Oct 7 at Pioneer
for a fireside discussion on leading their companies through the biggest technological shift of our time.
You’ll discover key decision points in their journeys, challenges they faced and how they navigated them.
REGISTER NOW
partner with us →
Top News
OpenAI upgrades Codex Security Cloud to scan entire GitHub repos automatically
4,388 Likes
Codex Security Cloud
just got a big upgrade. Think of it as a security guard that never sleeps, watching your GitHub repo around the clock, even when your laptop is shut.
Here is what it actually does for you:
Scans your entire GitHub repo and flags vulnerabilities
Watches every new commit and reviews it automatically
Removes duplicate alerts so you are not drowning in noise
Prepares a ready-to-review fix, not just a warning
The big deal here is
Daybreak Blue
, OpenAI's defensive security AI tier, which is now bundled in by default. No separate application needed. It runs on a model with a
1,050,000-token context window
, meaning it can read your entire codebase at once, not just snippets.
Previously, accessing these stronger cyber models required a separate approval process. Now you just get it. Install the plugin in Codex desktop or web, connect your GitHub repo, and let it run.
READ MORE
forward →
Signals
1
Cursor adds inline chart and diagram generation directly in chat
3,753 Likes
2
Mercor Research team post-trains Qwen3.5-397B-A17B using expert data to raise Pass@1 by 11.2 points on APEX-Agents
Presented by Mercor
3
Google DeepMind builds a scoring system to measure AI consciousness without solving it first
590 Likes
4
New diffusion model beats a 6.5x larger model using 4.9x less compute
444 Likes
5
New 1.58-bit 27B model writes ComfyUI image prompts and fits on a 16 GB GPU
3,388 Downloads
6
Free open-source tool lets Claude Code edit your videos automatically
2,688 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=2b46af0fa283cac5