# 🧩 Understanding the “harness tax” behind coding agents

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Sun, 20 Sep 2026 15:11:23 +0000

🧩 Understanding the “harness tax” behind coding agents
Same model, same task, up to 5x the cost. The difference is your harness.
Stay updated with today’s top AI news, papers, and repos.
Signup
|
Work With Us
|
Follow on X
Hey Mauricio,
Two developers can use the same model on the same coding task and end up paying very different inference costs.
The difference can come from the harness. Whether you use Codex, Claude Code, Pi, or some other harness can make a huge difference.
A new study finds that simple harnesses can be surprisingly competitive, more complex setups can add substantial cost for small gains, and models do not always perform best inside their own vendor’s harness.
Today we look at what that means when choosing a coding-agent stack.
Today's Author
Ben Dickson is a veteran software engineer and former CTO known as the "Engineer's Journalist" for translating technical AI research into practical, production-focused insights. He is a lead contributor to TechCrunch and VentureBeat.
From Google Cloud
Unreliable GPUs cost you 10-20% extra hardware. Without reliable infra, teams often buy 10-20% more GPUs as a failure buffer. Google Cloud's GPU reliability approach uses rigorous pre-delivery hardware testing and real-time telemetry to catch issues before they interrupt training, keeping AI workloads running without costly checkpoint restarts.
Watch how it works ↗
Sunday Deep Dive
How to avoid the harness tax when choosing coding agents
Giving a coding task to the same model but with different harnesses can change its inference cost by as much as 5x without producing a comparable change in task success. That is the key finding of
HarnessTax
, a new study that tests how much the software surrounding an AI model affects coding-agent performance and cost.
The harness is the layer that determines the model’s instructions, tools, memory and context management, and how the agent executes a task. When choosing between Claude Code, Codex CLI, Pi and other coding agents, you’re choosing two things at once: a model and the harness.
The study suggests three useful rules of thumb:
Harness choice can move cost much more than aggregate success
A minimal harness can compete with feature-rich alternatives
A model does not necessarily perform best in the harness built by its own provider
For developers, the key lesson is to evaluate the model and harness as one system instead of accepting the default pairing.
What HarnessTax tested
The researchers tested a total of 21 model-harness combinations, composed of seven models and three harnesses: Claude Code, Codex CLI and Pir. They randomly selected 30 tasks from SWE-bench Lite, which tests an agent’s ability to fix software issues, and 30 from Terminal-Bench 2.0, which tests command-line tasks.
The researchers measured both task success and token cost based on API pricing. This makes it possible to see whether one harness causes the same model to consume more tokens instead of mixing that effect with differences in product pricing.
Finding 1: The harness can move the bill more than the score
On SWE-bench Lite, Claude Fable 5 solved 97.8% of attempts with Claude Code and 96.7% with Pi. But an average attempt cost $1.33 with Claude Code and $0.67 with Pi. That means you’re paying roughly double the cost for an observed success difference of 1.1 percentage points.
Interestingly, both Claude Code and Pi averaged around 15 turns per task. However, each Claude Code turn carried more information. Across all seven models, its mean initial context was more than 10 times Pi’s, driven by longer instructions and larger tool definitions.
This overhead matters because the model has to process the harness instructions and tool descriptions alongside the actual task. Token cost is therefore not only a property of the model you choose. The model-harness combination determines how much inference you need to buy to get a result.
Finding 2: A simple harness can be competitive
Pi gives the agent four basic tools: read, write, edit and bash. Yet its configurations reach the study’s cost-success Pareto frontier on both benchmarks, meaning that it gives the highest accuracy for a given budget.
That does not mean that simpler harnesses are always better. These experiments cover two public benchmarks and do not measure every reason developers might choose a richer product, such as integrations, permissions, memory, hooks or workflow features.
But the results make a simple harness a useful baseline. You can add additional scaffolding when it fixes a failure or provides a feature that matters for the application.
Finding 3: The vendor default is only a starting point
The study shows that models do not necessarily work best inside their provider’s harness. Across six Anthropic and OpenAI models and two benchmarks, an alternative harness recorded the highest observed success rate in nine of 12 comparisons.
For example, on Terminal-Bench 2.0, GPT-5.6 Sol scored 83.3% with Pi at around $0.42 per attempt, compared with 78.9% and about $0.76 with OpenAI’s Codex CLI. This does not prove that Pi is generally better for GPT models, especially given the sample size of experiments. But it suggests that native pairing should not be considered as the ultimate best choice.
What it means for developers
HarnessTax also exposes a problem with how developers choose agent stacks today.
“Many harness decisions nowadays are sort of made by: preference, tribal knowledge, word of mouth,” Melissa Pan, co-author of the paper, told AlphaSignal. “It is very unclear whether a particular harness is more accurate, more cost efficient, more this or that on certain metrics for certain workload.”
A practical evaluation should therefore treat “model × harness × workload” as the unit of comparison. Start with a representative sample of your own tasks, run several combinations against it, and track task success, cost and latency.
A harness that looks inexpensive per attempt might become expensive if failed attempts require retries, so cost per successful task is often more useful than cost per run.
The right tradeoff depends on the application. For high-volume routine work, doubling inference cost for a small change in accuracy makes little sense. For a task where failure is expensive, even a modest reliability improvement might justify a higher bill.
Also don’t put too much trust in aggregate success rates. Two configurations can achieve similar overall scores while failing on different tasks. If your workload contains many of the cases where one configuration breaks, the aggregate benchmark can hide the difference that matters most.
A useful process should be to build a representative task set, test several model-harness combinations, measure success, cost and latency, and inspect the failed cases. Choose the least expensive configuration that clears your reliability requirements, and rerun the evaluation when models or harnesses change.
Harnesses are also an optimization layer
There is a broader implication for the developer community. Frontier model training requires resources that few organizations have. “Harness effort is one of the few ways that people can improve performance without touching the model,” Pan said.
“For research, [the study] gives us hope that we have a chance to win in the harness space without having the ability to co-train with SOTA models,” Pan said. “This is very exciting for people who are doing work in the open including academia and the developer community.”
HarnessTax shows why that layer deserves more scrutiny from developers as well. The practical question is no longer only which model to use. It is which model-harness combination provides the reliability your application needs at a cost you can justify.
Google Cloud uses pre-delivery testing and real-time telemetry to catch GPU failures before they interrupt training
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=8f2be5a907777e51