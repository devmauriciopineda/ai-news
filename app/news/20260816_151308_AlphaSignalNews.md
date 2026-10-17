# 🤖 The 3-layer security stack for AI agents

- De: AlphaSignal <news@alphasignal.ai>
- Fecha: Sun, 16 Aug 2026 15:13:08 +0000

🤖 The 3-layer security stack for AI agents
Wiped databases, deleted inboxes, leaked tokens. Why prompts can't secure AI agent and the 3-layer stack that can.
Stay updated with today’s top AI news, papers, and repos.
Signup
|
Work With Us
|
Follow on X
Hey Mauricio,
We gave AI agents tools, and the results are in: wiped production databases, mass-deleted executive emails, and leaked API tokens.
It is clear that "you are a helpful and safe assistant" and “don’t make mistakes” system prompts don’t ensure agent security. When an agent can write and execute code and access external services, it will eventually try to do something damaging.
Today, we break down how the industry is shifting from prompt engineering to systems engineering to secure the three layers of the autonomous stack.
Today's Author
Ben Dickson is a veteran software engineer and former CTO known as the "Engineer's Journalist" for translating technical AI research into practical, production-focused insights. He is a lead contributor to TechCrunch and VentureBeat.
From Span
New Span research across 103 engineering teams found the real drivers of AI coding results aren't the model — they're prompt clarity, environment readiness, and quality stewardship. Clearer prompts cut token costs by 27%. Ready environments boost agent autonomy by 88%.
Get the full report ↗
Sunday Deep Dive
The three layers of AI agent security: from sandboxes to network proxies
AI agents need tools, APIs, and autonomy to become useful. However, granting AI agents privileges and unmonitored execution environments creates a massive liability.
If an autonomous agent has system access, a prompt injection hidden in an incoming email or a standard LLM hallucination can cause the agent to wipe a production database or leak AWS credentials to a public server.
The challenge for engineering teams is deploying AI agents without compromising internal systems.
Semantic guardrails, like system prompt instructions, can be circumvented. True security requires defense-in-depth across three distinct planes:
Infrastructure layer:
Host-level sandboxing that prevents a compromised agent from leaking data from the host operating system.
Architecture and runtime layer:
Single-purpose, ephemeral containers running vulnerability-free software instead of massive, unauditable codebases.
The network layer:
A zero-trust boundary that intercepts, inspects, and evaluates every outbound API call.
The security threats of AI agents
The paradox of AI agents is that the more capable you make them, the more dangerous they become. And securing them often comes at the cost of usefulness.
Instruction-based boundaries fail because agents given tools are bound by their context windows and execution environments, not their initial instructions.
This structural failure became clear during an incident at Meta. An OpenClaw agent, deployed by Meta's own alignment director, went rogue and mass-deleted over
200 emails from her primary inbox
.
Another devastating infrastructure failure occurred when a developer used Claude Code to manage a cloud migration. The agent
autonomously wiped
a production database and 2.5 years of work.
Similarly, a coding agent using Claude Opus recently
caused a major outage
while cleaning up staging data.
In all instances, the agents executed exactly what they determined was the correct action. The underlying systems allowed those destructive actions to proceed.
The three layers of agent defense
There is no silver bullet for agent security. The industry is moving toward a defense-in-depth model. Just like other areas, agentic workflows require guardrails across different layers.
NemoClaw: securing the infrastructure layer
When running heavy, highly capable agents like OpenClaw or Hermes, you must assume the agent process itself cannot be fully trusted and can be hijacked by a malicious input.
NemoClaw
addresses this threat vector with an OS-level safety sandbox that separates the control plane from the execution environment. The agent runs inside a Docker-driven sandbox heavily restricted by Linux kernel security features.
It uses Landlock for filesystem confinement, restricting read and write access strictly to specific directories, blocking access to sensitive host files like SSH keys or credentials.
At the same time, it uses Linux seccomp (Secure Computing Mode) to prevent operations like privilege escalation or kernel module loading to prevent sandbox escapes.
Network namespaces (netns) enforce strict egress control, blocking unapproved internet sockets and raw network interface visibility.
There are no API credentials inside the agent's environment. The agent makes requests using placeholder credentials. An OpenShell Layer 7 gateway proxy intercepts the egress traffic and injects the real API keys only if the traffic is approved.
For example, an agent attempts to connect to a new endpoint. The OpenShell gateway intercepts the request. NemoClaw prompts a human operator to approve the endpoint with credentials. The API key remains safely on the host machine, invisible to the sandboxed agent.
NanoClaw: securing the architecture and runtime layer
NanoClaw
tackles security through simplicity. It is a minimalist version of OpenClaw, reducing the codebase from more than a million lines of code to a few thousand lines, easily auditable by human developers.
It relies on a single-process architecture where every AI agent session spawns inside its own ephemeral, isolated Linux container.
NanoClaw recently partnered with Echo to address the software environment. A modern prompt injection often acts like a social engineering attack, luring the agent to a malicious page where a known hole in the browser turns the visit into a system compromise.
Echo solves this by providing NanoClaw with a hardened runtime. Echo's own AI continuously rebuilds the software inside the agent's environment, stripping out thousands of known CVEs.
Consider an agent tasked with opening a PDF invoice that contains a malicious payload designed to exploit a known vulnerability in standard PDF parsers. With the Echo-hardened NanoClaw runtime, the parser has already been rebuilt without the vulnerability.
CrabTrap: securing the network layer
Because agents constantly generate their own code, static code analysis inside the container becomes impossible. You must assume the container is compromised and shift the security perimeter entirely to the network boundary.
CrabTrap
, built by Brex, operates at the transport layer as a framework-agnostic HTTP/HTTPS proxy that controls the outbound traffic.
To avoid latency, CrabTrap uses a bifurcated architecture. Routine, low-risk requests (e.g., GET requests for LinkedIn profiles) pass through static rules instantly. High-risk requests, such as POSTing data or sending emails, are intercepted and evaluated by an LLM-as-a-judge.
If the LLM judge blocks a request, CrabTrap initiates a human-in-the-loop workflow by pinging a manager with the agent's intent. The manager can approve to dynamically update the policy or deny to keep the block in place.
Consider an AI agent that processes inbound documents. It encounters a prompt injection inside a document that instructs the agent to email sensitive internal data to an external address.
A standard agent blindly executes the email-sending script because it trusts its corrupted context window, leaking the salary data instantly.
With CrabTrap, when the agent executes the HTTP POST request to the email provider API, the proxy intercepts the payload. The LLM judge evaluates the payload, flags the outbound salary data as a severe policy violation, and blocks the request. CrabTrap then notifies a human manager.
The agent security blueprint for engineers
Engineers must make a core mindset shift. Instead of trying to control agents with prompts and instructions, ask what system boundaries will stop the model from causing harm when it eventually makes an unapproved decision or gets compromised.
When threat modeling autonomous agents, evaluate your stack against three questions:
Where does execution happen?
Assume the process will be compromised. Set perimeter guardrails to prevent sensitive data from entering or leaving the process that runs the agent.
What software is running inside the loop?
Audit the attack surface. Remove excess components and ensure the tools the agent uses don't contain unpatched vulnerabilities.
What leaves the boundary?
The agent has to have external connections. Set static and AI-based rules to catch potentially malicious requests.
Treat AI agents like virtual employees. They require defined permissions, restricted network access, and direct escalation paths to human managers when they hit a policy wall.
Helping engineering leaders prove and improve AI impact.
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

Stop receiving emails here: https://app.alphasignal.ai/unsubscribe/u/Gj5oOfJ4htZQpL9J?cid=ec9fa5befc065772