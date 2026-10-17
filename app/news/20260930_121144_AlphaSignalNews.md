# OpenAI GPT-6.1 Sol 🤖, PageIndex Tree Search 98.7% 🌳, OpenAI Decisions 

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Wed, 30 Sep 2026 12:11:44 +0000

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
OpenAI's DevDay was essentially one big argument:
you don't need the best model, you need the best value.
GPT-6.1 Sol matches flagship Astra on coding at one-fifth the cost. The Decisions API routes your app logic in 150ms. Meta's self-evolving training trick doubles math accuracy for free.
The pattern is clear. The frontier is no longer just about raw capability.
It's about making power affordable enough to ship.
In Partnership with
·
Today's Author
Lior Alexander. Founder of AlphaSignal and former ML Engineer. Previously built ML systems at Iguazio, Guesty, Enphase, Mila.
Summary
Read time: 6 min 48 sec
Top News
▸ OpenAI ships GPT-6.1 Sol at 80% less cost with
near-flagship performance
WorkOS
▸
S
t
o
p
f
a
k
e
a
c
c
o
u
n
t
s
b
e
f
o
r
e
t
h
e
y
b
u
r
n
t
o
k
e
n
s
Top Repo
▸ Tree search framework hits 98.7% on documents where
vector search fails
Sentry
▸
D
e
b
u
g
A
g
e
n
t
s
i
n
C
h
a
t
,
S
l
a
c
k
,
C
I
-
L
i
v
e
W
o
r
k
s
h
o
p
Top News
▸ OpenAI ships Decisions API letting apps
route and classify
with GPT-6 Luna
Signals
1. Anthropic ships Claude Sonnet 5.5
matching Opus 5.5
on agentic tasks but using 7x more tokens
2.
DigitalOcean & NVIDIA:
Open Intelligence Summit, SF, Oct 13, with Nous Research, LanceDB. Apply via our partner link
3. RedAmon ships open-source framework that
runs full cyberattacks
and auto-patches your code
4. Meta's training trick
doubles Qwen3-8B math
accuracy while cutting output length
5. Blackfrost AI releases 180B
MoE model with
6B active params in GGUF format
6. Open-source AI companion runs locally,
plays Minecraft and
supports 30+ LLM models
Top News
OpenAI ships GPT-6.1 Sol at 80% less cost with near-flagship performance
23,168 Likes
OpenAI just dropped
GPT-6.1 Sol
, and the pitch is simple: nearly the same smarts as their top model, Astra, for a fraction of the cost.
Astra is OpenAI's most powerful model. Sol sits just below it. The upgrade here is that 6.1 Sol now closes that gap significantly on coding, document analysis, and multi-step tasks, without raising the price.
Here's what the numbers actually look like:
Coding tasks (DeepSWE): matches Astra at
$0.65/task vs Astra's $3.92
Computer use (OSWorld): within 2 points of Astra at one-seventh the cost
Science work (Terminal-Bench): $5.47/task vs $23.80 for Astra
Cached input dropped to
$0.10 per million tokens
, half of what GPT-6 Sol charged
Caching means reusing repeated text in your prompts so you pay less. That
95% discount
off standard input pricing makes running large apps at scale way cheaper.
You can access it via the API using
gpt-6.1-sol
, or through ChatGPT Work and Codex right now.
READ MORE
forward →
Presented by WorkOS
Stop fake accounts before they burn tokens
Free-tier abuse gets expensive fast in an AI product. One person can cycle through email addresses, devices, and trials while your app keeps issuing credits and paying inference costs. Blocking a single address only slows them down.
WorkOS Radar
checks device, email, and network signals at signup, then returns a risk verdict before the account reaches your product.
You can block obvious abuse, step up suspicious users, and review the evidence behind each decision without maintaining rules or deny lists.
SEE RADAR
partner with us →
Top Repo
Tree search framework hits 98.7% on documents where vector search fails
4,598 Likes
Traditional RAG, the technique that lets AI answer questions from your documents, has a dirty secret: it chops your docs into random chunks, converts them to numbers, and hopes a similarity search finds the right piece. It often doesn't.
PageIndex
flips the whole model. Instead of chunking, it reads your document and builds a tree structure, like a smart table of contents. Then the AI reasons through that tree to find exactly what's relevant, the way a human expert would flip to the right chapter.
What this means for you:
No vector database
, no embeddings, no chunking setup
98.7% accuracy
on FinanceBench, beating every vector RAG on the leaderboard
Works great on legal docs, financial reports, technical manuals
Fully open source, self-hostable with a simple pip install
You can run it locally in three steps: install deps, add your API key, then point it at a PDF. It also supports MCP and API for production use.
READ MORE
forward →
Presented by Sentry
Debug Agents in Chat, Slack, CI - Live Workshop
In this hands-on workshop, Serge from Sentry instruments three agents with
Sentry Agent Tracing
: an ecommerce chatbot, a custom Slack agent, and a GitHub Action that reviews PRs.
You'll see how to catch bad tool calls and unexpected output, plus track token spend and performance across every agent you run.
SAVE YOUR SPOT
partner with us →
Top News
OpenAI ships Decisions API letting apps route and classify with GPT-6 Luna
4,494 Likes
OpenAI just dropped the
Decisions API
, and it flips how you handle routing logic inside your app.
Here is the idea. Instead of writing a pile of if-else conditions to figure out what your app should do next, you hand the API a question and a list of possible answers. It picks one. That is it.
You can send text or images as context. Think: a support ticket plus a list of teams. The API tells you where to send it. Under the hood it runs on
GPT-6 Luna
, tuned specifically for this task, and it answers in
150 milliseconds
, compared to 1.6 seconds for a regular Luna call.
What you can actually build with this:
Content moderation: classify what a user sent before doing anything with it
Request routing: send users to the right team or agent automatically
Agent logic: let your AI agent pick its next action from a defined set of moves
Access is limited right now to selected API customers, with a broad release coming very soon.
READ MORE
forward →
Signals
1
Anthropic ships Claude Sonnet 5.5 matching Opus 5.5 on agentic tasks but using 7x more tokens
3,689 Likes
2
Open Intelligence Summit, SF, Oct 13, with Nous Research, LanceDB. Apply via our partner link
Presented by DigitalOcean & NVIDIA
3
RedAmon ships open-source framework that runs full cyberattacks and auto-patches your code
2,748 Stars
4
Meta's training trick doubles Qwen3-8B math accuracy while cutting output length
625 Likes
5
Blackfrost AI releases 180B MoE model with 6B active params in GGUF format
1,406 Downloads
6
Open-source AI companion runs locally, plays Minecraft and supports 30+ LLM models
3,445 Likes
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=a6b1cdbf68ca1c19