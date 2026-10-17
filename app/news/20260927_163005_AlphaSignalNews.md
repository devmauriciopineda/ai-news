# 🚀 System One models are carving out a new layer in the AI stack

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Sun, 27 Sep 2026 16:30:05 +0000

🚀 System One models are carving out a new layer in the AI stack
Jev and new System One models make fast, typed AI decisions for a fraction of LLM cost. See where they fit.
Stay updated with today’s top AI news, papers, and repos.
Signup
|
Work With Us
|
Follow on X
Hey Mauricio,
LLMs have become the default building block for almost every AI task, from writing code to deciding which support queue should receive an email.
But many of those tasks don’t require generation at all. They require fast, reliable decisions, and using a full generative model for every one can become expensive as applications scale.
Jev and a growing group of “System One” models are taking a different approach.
Today we break down where they fit in your AI stack, and when developers should use them instead of code or an LLM.
Today's Author
Ben Dickson is a veteran software engineer and former CTO known as the "Engineer's Journalist" for translating technical AI research into practical, production-focused insights. He is a lead contributor to TechCrunch and VentureBeat.
From Ory
Security after an AI agent acts is like no security at all.

Put deterministic controls around probabilistic systems. Outside-in checkpoints like gateways and MCP servers are easily bypassed by agents. Ory provides inside-out observability and security at runtime. 

See Ory in action with full platform access. Unlimited agents, no restrictions. Plus, the first 100 sign-ups get exclusive Ory swag. Limited time only.
Try Ory Today ↗
Sunday Deep Dive
Where Jev and System One models fit in your AI stack
TypeSafe AI released Jev, its new “
System One Model
,” on September 15. Jev is designed to make lightning-fast structured decisions instead of generating text like LLMs.
The launch drew strong developer interest, and open alternatives followed quickly. Laya provides an open System One-style model, while Stanford and Nvidia researchers released CLM-8B, which tackles the same class of bounded decisions with a different contrastive architecture.
It is too early to call System One an established model category, but the rapid appearance of alternatives suggests Jev has exposed a useful niche: models built to choose, score and verify instead of generate.
AI applications often make decisions that are too fuzzy for hand-written rules but do not require a generative model: choosing an agent tool, routing a request, enforcing a guardrail, or selecting the best answer from several candidates.
System One models provide another building block for handling those decisions, with the potential to make production AI systems more predictable and economical as they scale.
How Jev changes the model interface
Large language models are autoregressive. They create output one token at a time, which is good for generating text and code. But that flexibility is unnecessary if you only want to decide whether a support ticket belongs to billing, sales or technical support.
Jev handles these kinds of situations. You provide it with the application state, questions and possible answers. It returns typed values with probability and confidence information. Instead of asking an LLM to generate and then parse “This looks like a billing issue,” your application can directly receive a typed “billing” value.
Jev produces its outputs in parallel instead of decoding a string token by token. TypeSafe reports 70–500 millisecond end-to-end latency, $0.042 per million input tokens and no metered output-token cost.
Image source:
TypeSafe AI
For “System One shaped” queries at comparable intelligence levels, it claims 40–200x lower latency than frontier LLMs and 444.6x gains in cost reduction.
TypeSafe also trained Jev with Reinforcement Learning for Calibrated Decisions, or RLCD. The practical benefit is useful uncertainty. A spam score of 0.52 should not be treated like 0.998. A system can send uncertain cases to a stronger model or human while automatically processing high-confidence ones.
Technically, Jev solves the hallucination problem of LLMs in decision-based tasks because it can’t invent output types and its answers are constrained to the schema you define.
However, it can still choose the wrong answer and its quality depends on the options you provide. If a ticket concerns fraud but the available answers are “billing,” “sales” and “technical,” the model cannot return the correct category.
The quality of the answer space therefore becomes part of the quality of the system. Developers therefore need to make sure the choices are complete and distinct.
Where System One models fit in your stack
A useful way to decide whether you need Jev is to start with ordinary code. If you can express the logic reliably with an explicit rule, use the rule. There is little benefit in adding probabilistic AI to something like “if balance < 0: require_payment().”
The sweet spot comes when you know the possible answers but cannot easily write the rule that separates them. Examples include email classification, sentiment and urgency scoring, agent tool selection, content moderation, and retrieval ranking.
One particularly interesting application is replacing LLM-as-a-judge with
Jev-as-a-judge
. Many AI systems generate several candidate responses and use another model to verify them.
A powerful reasoning model could generate multiple candidates and have Jev rank them. High-confidence decisions could be accepted immediately, while ambiguous cases fall back to an LLM judge or human reviewer.
Image source:
arXiv
This division of labor leaves expensive models to do what they are good at: generation and reasoning. Cheaper decision models handle selection, routing and verification.
Open alternatives are already emerging
Laya
is an open-source alternative to Jev. It has 421 million parameters and uses ModernBERT with a dedicated decision head. It accepts state and typed questions and scores every option in a single forward pass. The project also provides a Jev-compatible server API.
Laya’s developers report around 33 milliseconds for single-question inference on the multilingual checkpoint on a Tesla T4. That is not directly comparable with Jev’s hosted end-to-end latency.
Contrastive Language Models
(CLM) takes a different approach. Its 8-billion-parameter model maps the current state and candidate actions into a shared embedding space, then selects the best match.
Image source:
CLM team
In the researchers’ zero-shot tests, CLM ran up to 9x faster than Jev. The largest CLM speedups appeared when actions could be reused across many states or the candidate set was large.
The CLM team also tested the judge pattern directly. Larger models generated several coding solutions, and a fine-tuned CLM ranked them. On small held-out subsets, CLM reached 81.6% on 38 DeepSWE tasks and 87.6% on 30 Terminal-Bench 2.1 tasks, versus 71.1% and 83.1% for Jev.
Bigger models are not the only way to scale AI
Autoregressive models remain essential when applications need difficult reasoning or new text, code and other content. But routing every intelligent operation through the same general-purpose model creates unnecessary latency and cost.
The emerging stack can be more heterogeneous: conventional code for explicit rules, decision models for fuzzy choices, and generative models for open-ended tasks.
Jev and the models following it give engineers another way to turn expensive intelligence into applications that are reliable, fast and economical enough to operate at scale.
Outside-in checkpoints aren't enough. Get full access to Ory's agent security
Learn More →
At Alpha Signal, our mission is to build a sharp, engaged community focused on AI, machine learning, and cutting-edge language models, helping over 200,000 developers stay informed and ahead. We’re passionate about curating the best in AI, from top research and trending technical blogs to expert insights and tailored job opportunities. We keep you connected to the breakthroughs and discussions that matter, so you can stay in the loop without endless searching. We also work closely with partners who value the future of AI, including employers and advertisers who want to reach an audience as passionate about AI as we are.
Our partnerships are based on shared values of ethics, responsibility, and a commitment to building a better world through technology.Privacy is a priority at Alpha Signal. Our Privacy Policy clearly explains how we collect, store, and use your personal and non-personal information. By using our website, you accept these terms, which you can review on our website. This policy applies across all Alpha Signal pages, outlining your rights and how to contact us if you want to adjust the use of your information. We’re based in the United States. By using our site, you agree to be governed by U.S. laws.
Looking to promote your company, product, service, or event to 250,000+ AI developers?
WORK WITH US
How was today’s email?
Awesome
Decent
Not Great
unsubscribe_me(): return True
{"AlphaSignal": "214 Barton Springs Rd, Austin, USA"}

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=7cbae252395cbec5