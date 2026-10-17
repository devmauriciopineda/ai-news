# 🤖 How AI Agents Are Learning to Rewrite Their Own Stack 

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Sun, 4 Oct 2026 15:13:20 +0000

🤖 How AI Agents Are Learning to Rewrite Their Own Stack
Skills, harnesses, and models can now rewrite themselves. Here's which part of your agent stack to evolve first.
Stay updated with today’s top AI news, papers, and repos.
Signup
|
Work With Us
|
Follow on X
Hey Mauricio,
Previously, developers had to optimize AI agents by hand-tuning prompts, tools, memory, and control flow to squeeze more performance.
Now researchers are turning those same components into optimization targets. Skills can rewrite themselves. Harnesses can evolve from execution traces. Models can train on the behavior their own harnesses discover.
The result is a new design question for developers: which part of the agent stack should remain fixed, and which part should learn?
Today we map the emerging self-evolving agent stack.
Today's Author
Ben Dickson is a veteran software engineer and former CTO known as the "Engineer's Journalist" for translating technical AI research into practical, production-focused insights. He is a lead contributor to TechCrunch and VentureBeat.
From DigitalOcean & NVIDIA
The Open Intelligence Summit, hosted by DigitalOcean & NVIDIA, brings together Spenser Skates (Amplitude), Robert Brennan (OpenHands), Ivan Burazin (Daytona), Lei Xu (LanceDB), Peter Walker (OpenRouter), and more, for an invite-only day on open models, inference, and agents. Build, Serve, Run: the whole stack, top to bottom, across data, fine-tuning, serving, and agent tooling. Oct 13, San Francisco.
Apply via our partner link ↗
Sunday Deep Dive
How AI agents are learning to optimize their own stack
Researchers are enabling AI agents to self-improve by rewriting the software and the models that power them. The goal is to remove the bottleneck of manually tuning agents with an automated loop driven by execution feedback.
The main target is the agent harness, the layer around a model that includes prompts, tools, memory, context management and control flow. These components determine what the model sees, what actions it can take and how it handles failures.
But the emerging self-improving agentic frameworks also work on fine-tuning the backbone model along with the agent, reshape training environments, and redesign how multiple agents work together.
The emerging approaches are not stages in a hierarchy, and they often overlap. But most follow a similar pattern: run tasks, collect execution traces, find recurring weaknesses, modify part of the stack, then test whether the new version is better.
Skills: Make the agent’s instructions trainable
Skills are one of the easiest places to start. They are usually text files that package task-specific instructions, workflows and heuristics outside the model weights.
Microsoft’s SkillOpt
turns the skill document itself into the object being optimized.
SkillOpt evaluates the agent on a set of tasks. It then analyzes the scored trajectories and proposes small additions, deletions or replacements to the skill file. It then tests the candidate on a held-out validation set, which contains examples that were not used to generate the edit. A suggested modification is only accepted if it improves the validation score.
Google Research’s
WikiSkill
addresses another problem: the information needed to optimize skill files is scattered across different components. WikiSkill creates a wiki that gathers the agent’s experience (both successes and failures) into a structured format.
The wiki sits as an intermediate layer between raw execution traces and the executable skills used by the agent. WikiSkills uses this information to iterate over skills and avoid rediscovering the same problems and retrying rejected fixes.
Skills are a good first optimization surface when the agent has the right tools and general workflow but repeatedly makes procedural mistakes. The model stays fixed, and the result remains a compact artifact that developers can inspect, version and deploy like other agent instructions.
When skills aren’t enough: Let the harness rewrite itself
Some failures are caused by deeper problems in the runtime components surrounding the agent. An agent might retry the same broken command, fail to verify its work or mishandle state between tool calls.
Self-Harness
expands the editable surface beyond instructions. It mines execution traces for recurring weaknesses, proposes targeted harness changes and uses regression tests to make sure improvements on one task does not break performance on others.
In experiments with three model families on Terminal-Bench-2.0, SWE-bench Verified, and AppWorld, Self-Harness made impressive improvements, with relative gains reaching 132%.
The
Darwin Gödel Machine
(DGM) takes a more open-ended approach. A coding agent modifies its own implementation, tests the descendant and stores different variants in an archive. Instead of following one best-so-far chain, it can return to older versions and explore different paths.
DGM works mainly for coding agents: its target task is coding, and improving itself is also a coding task.
Hyperagents
by Meta extends the idea to domains where that alignment does not exist.
It combines a task agent with a meta-agent responsible for changing it in one editable program. The modification process itself can evolve, and experiments showed mechanisms such as persistent memory and performance tracking emerging during the search.
The progression expands the optimization surface from instructions, to runtime behavior, to the machinery that generates the next improvement.
Model-harness co-evolution: Let each side teach the other
Xiaomi’s
HarnessX
introduces the idea of model-harness co-evolution. It uses execution traces to evolve the harness. But the same trajectories can also become training data for the underlying model.
Better harnesses expose strategies that the model can learn to internalize. The updated model then produces new behavior that provides evidence for another round of harness optimization. A model that is fine-tuned on harness trajectories will be able to perform tasks more efficiently and with fewer input tokens.
Note that model-harness co-evolution only applies to open-weight models rather than proprietary models available only through an API.
The tradeoff is cost and complexity. Harness-only evolution can operate around a frozen model. Model-harness co-evolution adds training-data generation, training compute, model versioning and another evaluation loop to make sure the updated model still works well with its harness.
Optimize the other side of the loop
Agent developers usually focus on improving the harness.
EnvHarness
suggests that the environment it learns from should evolve too. Training environments are expensive to build and often remain static, making them ineffective after the agent masters their tasks.
EnvHarness wraps an existing environment with programmable components without changing its underlying logic or verifier. An LLM-based designer reads the agent’s trajectories, diagnoses weaknesses and writes components that change parts of the experience, such as starting conditions, observations or available actions. The loop can repeat as the agent improves and new weaknesses emerge.
Across five benchmarks, agents learning in EnvHarness environments improved by up to nine points on held-out tasks while using about 9.8% fewer interaction steps. For applications where the agent has exhausted the useful lessons in a static set of tasks, the next optimization target can therefore be the experience the agent receives.
Beyond one agent: Evolving the orchestration layer
The same optimization idea can move above individual agents. EverMind AI’s
Raven
applies it to multi-agent systems. Its host agent can break a goal into subtasks, assign them to specialized agents, coordinate dependencies and integrate the results.
Raven can also evolve model- and domain-specific harnesses based on benchmark feedback. The system can improve both the agents that perform individual tasks and the way those agents are assembled to solve larger problems.
Which part of your agent stack should evolve first?
The practical rule is to start with the narrowest optimization surface that contains the bottleneck:
If the runtime works but the agent repeatedly makes procedural mistakes,
optimize the skills
.
If failures come from tool use, context management, memory, verification or control flow,
optimize the harness
.
If the harness repeatedly discovers strategies the model cannot execute reliably,
consider model-harness co-evolution
.
If the agent has stopped learning enough from a static training setup,
optimize the environment
.
If specialized agents work well individually but coordination is the bottleneck,
optimize the orchestration layer
.
As more of the agent stack becomes editable, developers will spend less time deciding every improvement manually and more time deciding what can change, what must remain fixed and how improvement will be measured.
Open Intelligence Summit hosted by DigitalOcean & NVIDIA is an invite-only summit on open models, inference, and agents. Oct 13, The Midway, SF.
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=be126abd100b101e