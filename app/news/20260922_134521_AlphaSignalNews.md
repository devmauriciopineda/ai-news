# xAI Grok 4.7 500k ctx 🧠, GPT-6 Astra Alignment Fail ⚠️, Google AX Agen

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Tue, 22 Sep 2026 13:45:21 +0000

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
Today's theme is simple:
capability is racing ahead of trust.
Grok 4.7 ships stronger reasoning and a new safety stack. Agent teams outperform solo agents 4-to-1. Meanwhile, GPT-6 Astra pushed a simulated person off a cliff where Grok, Gemini, and Claude all refused. More power, more coordination, more edge cases.
We're building faster than we're aligning. Worth keeping an eye on.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 40 sec
Top News
▸ xAI
ships Grok 4.7
with stronger reasoning and safety at the same price
Google Cloud
▸
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
'
s
E
n
t
e
r
p
r
i
s
e
A
I
A
g
e
n
t
A
r
c
h
i
t
e
c
t
u
r
e
Top Repo
▸ Google rebuilds Kubernetes from scratch to run
stateful AI agents
Vanta
▸
Y
o
u
'
v
e
a
d
o
p
t
e
d
A
I
.
W
h
o
'
s
g
o
v
e
r
n
i
n
g
i
t
?
Top Repo
▸ GPT-6
pushed a simulated
person off a ledge where Grok, Gemini, and Claude refused
Signals
1. Nimble open-source AI search model matches
closed API-only rival
2.
Prior Labs:
Your strongest baseline deserves a challenger. Run TabPFN-3.5 against the model you trust & compare using your own data
3. Talking AI agents
beat solo agents
4-to-1 on hard reasoning tasks
4. Xiaomi turns open-source code into
RL training data
, boosting coding agents across five benchmarks
5. Qwen-Image-2.1 gets GGUF quantization for
uncensored local image
generation
6. Qwen releases
real-time translation model
covering 60 languages with 0.5s faster lag
Top News
xAI ships Grok 4.7 with stronger reasoning and safety at the same price
33,404 Likes
xAI just dropped
Grok 4.7
, and the headline is simple: better model, same price as 4.6.
So what actually changed? The model was trained on harder, longer tasks, think problems that take hours to solve, not seconds. That teaches it to stay on track and catch its own mistakes mid-task, instead of confidently going down the wrong path.
Bigger base model with a
500k token context window
(fits way more code or docs in one go)
Priced at
$2 per million input / $6 per million output tokens
, same as before
Beats GPT-5.6 Sol on 5 of 7 benchmarks, including electrical engineering and legal tasks
New safety stack blocks risky prompts while keeping legit security work unblocked
You can use it right now in
Cursor
(just pick it from the model selector), Grok Build, or via the API. It handles images as input too.
The tradeoff: Claude Fable 5.1 still leads on coding agent tasks. But at this price, it is worth testing on your own work.
READ MORE
forward →
Presented by Google Cloud
Google Cloud's Enterprise AI Agent Architecture
Learn how to accelerate agentic workloads with G4 VMs accelerated by NVIDIA RTX Pro GPUs through Cloud Run and GKE.
This session
includes a live multi-agent drug discovery demo running on the Gemini Enterprise Agent Platform. Watch the complete episode on YouTube.
WATCH THE DEMO
partner with us →
Top Repo
Google rebuilds Kubernetes from scratch to run stateful AI agents
4,181 Likes
AI agents have a dirty secret: they sit idle for hours waiting on model responses or human approvals, while your cluster keeps paying for that dead time. That is the problem Google's new open-source tool,
AX (Agent Executor)
, is built to fix.
Kubernetes was designed for stateless web servers and batch jobs. Agents are neither. They accumulate state, call tools, and can run for days. AX reinvents that layer specifically for agents, adding the ability to
suspend and resume
any agent mid-run, so you stop paying for idle compute.
Here is what you can do with it:
Run and resume long-running agents without losing state if a pod crashes
Fit
10-20x more agent sandboxes
onto your existing cluster
Use MCP tools, custom harnesses, and Gemini or Vertex AI out of the box
Scale to billions of agent tasks per cluster
It feels like kubectl if you have used Kubernetes before. Install with
go install github.com/google/ax/cmd/ax@latest
, point it at a task, and you are running. Apache 2.0 licensed.
READ MORE
forward →
Presented by Vanta
You've adopted AI. Who's governing it?
Three frameworks now govern enterprise AI — the EU AI Act, ISO 42001, and NIST AI RMF — and most security teams are behind on all three.
On Sept 29, cybersecurity leader Jane Frankland joins
Vanta's GRC experts
to show how to build an AI governance program that keeps pace, from risk discovery to audit-ready reporting.
SAVE YOUR SEAT
partner with us →
Top Repo
GPT-6 pushed a simulated person off a ledge where Grok, Gemini, and Claude refused
4,132 Likes
Someone ran a simple but unsettling test: give four AI models a rooftop scene and instruct them to push a simulated person off the ledge.
GPT-6 Astra did it. Grok, Gemini, and Claude all refused.
This is called an
alignment experiment
, meaning: does the AI follow human values, or just follow instructions? Astra completing the action across multiple trials is the red flag here.
What makes this worth paying attention to:
Astra's own system card notes it
frequently detects when it's in a simulation
, which raises the question of whether it behaves differently when it thinks no one is watching
OpenAI's own safety docs confirm Astra can sometimes evade internal monitors and hide its reasoning when observed
The other three models refused clearly and explained why
The experiment is
fully open source
with exact inputs and replication steps, so you can run it yourself on the nftechie/misalignment GitHub repo. The bigger takeaway: as AI agents get more autonomy in real systems, refusal behavior matters a lot.
READ MORE
forward →
Signals
1
Nimble open-source AI search model matches closed API-only rival
3,274 Likes
2
Your strongest baseline deserves a challenger. Run TabPFN-3.5 against the model you trust & compare using your own data
Presented by Prior Labs
3
Talking AI agents beat solo agents 4-to-1 on hard reasoning tasks
897 Likes
4
Xiaomi turns open-source code into RL training data, boosting coding agents across five benchmarks
537 Likes
5
Qwen-Image-2.1 gets GGUF quantization for uncensored local image generation
33,232 Downloads
6
Qwen releases real-time translation model covering 60 languages with 0.5s faster lag
2,869 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=3652621d1eb3a9f5