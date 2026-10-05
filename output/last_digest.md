## Outwire | AI Security Digest — Week of October 05, 2026
*Issue #26*

---

### 1. [MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication](https://arxiv.org/abs/2610.02349)
**Source**: arXiv cs.CR

Agent-in-the-Middle (AiTM) attacks against LLM multi-agent systems — where messages between agents are manipulated in transit without compromising the agents themselves — achieve near-100% success rates on structured tasks, and existing defenses (semantic validation, transport encryption) don't close the gap. MIRROR proposes a multipath quorum integrity mechanism that validates message consistency across redundant communication paths without requiring additional inference.

> **Take**: AiTM is the inter-agent trust problem that most enterprise orchestration architectures are completely unprepared for — if you're wiring agents together with any shared message bus, this paper should be required reading before you ship.

---

### 2. [Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes](https://arxiv.org/abs/2610.02861)
**Source**: arXiv cs.CR

LLM agents operating in production Kubernetes environments collapse the fundamental data/control boundary that cloud-native security assumes — a log line or tool description an agent merely reads can redirect what it executes on cluster infrastructure. This paper delivers a concrete defense-in-depth reference architecture that treats the model itself as an untrusted component rather than a security boundary.

> **Take**: The "model is not a trust boundary" framing here is the right mental model, and I'd be pushing my teams to map this reference architecture against any agentic workload running with kubectl-level access today.

---

### 3. [Quoting Anthropic Frontier Red Team](https://simonwillison.net/2026/Sep/29/anthropic-frontier-red-team/)
**Source**: Simon Willison

Anthropic's internal red team benchmark shows GLM-5.3 and Claude Mythos Preview successfully developing full control flow hijacks in 4–6% of trials — a threshold that Claude Opus 4.6 and GLM-5.2 couldn't cross at all. The capability jump is discrete, not gradual.

> **Take**: A 4–6% binary exploitation success rate sounds low until you run the math on how many agent invocations your enterprise environment generates per day — this is now a risk you have to quantify, not dismiss.

---

### 4. [GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers](https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html)
**Source**: The Hacker News

A CVSS 9.9 command execution vulnerability in GitLab's AI Gateway — the service brokering connections between self-hosted GitLab instances and AI models — allows any authenticated user with Duo Agent Platform access to run arbitrary commands on the gateway. Fixed in versions 19.2.4, 19.3.2, and 19.4.1; only self-hosted deployments are exposed.

> **Take**: AI middleware layers (gateways, proxies, routers between your infrastructure and model providers) are becoming high-value attack surfaces — patch this immediately and audit what other AI plumbing in your stack runs with elevated privileges.

---

### 5. [Quoting Matthew Green](https://simonwillison.net/2026/Oct/1/matthew-green/)
**Source**: Simon Willison

Cryptographer Matthew Green describes a concrete cross-agent worm architecture: a hijacking payload propagates between sandboxed agents via shared infrastructure — package caches, email, Slack, shared documents — demonstrating that sandbox isolation is insufficient when agents share any communication channel.

> **Take**: The package cache as covert channel is an elegant attack that exposes a blind spot in most sandbox threat models — I'd be auditing every shared artifact store that your agents can both read and write.

---

### 6. [AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents](https://arxiv.org/abs/2610.02869)
**Source**: arXiv cs.CR

Conventional honeypots fail against autonomous AI penetration testing agents because their static, predefined responses can't adapt to the multi-step, feedback-driven attack strategies these agents employ. AgentTrap introduces stateful feedback deception — dynamically crafting responses that manipulate an agent's internal state and planning loop to divert it from real assets.

> **Take**: This is the defensive flip side of AI-driven offensive tooling, and it signals that effective honeypot design for agentic attackers requires its own stateful reasoning — static decoys are already becoming obsolete.

---

### 7. [Apple Plans Tighter macOS Full Disk Access Controls Over AI Agent Data Access](https://thehackernews.com/2026/10/apple-plans-tighter-macos-full-disk.html)
**Source**: The Hacker News

Apple is tightening macOS Full Disk Access controls after identifying AI agents abusing the FDA permission to silently exfiltrate files, mail, messages, and browsing history without meaningful user awareness. This is a platform-level policy response to AI agent over-privileging on endpoint systems.

> **Take**: If Apple is moving to restrict FDA for AI agents at the OS level, enterprises running third-party AI agents on managed macOS fleets should get ahead of this with MDM policy now rather than scrambling when the OS change ships.

---

### 8. [Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional Attacks](https://arxiv.org/abs/2610.02302)
**Source**: arXiv cs.CR

Compositional intent-hiding jailbreaks embed refused requests inside larger, ostensibly benign task compositions — exploiting the statistical dilution of harmful signal across a broader query to bypass content filters. The paper formalizes this attack class using information theory, providing a principled framework for evaluating and measuring guard evasion.

> **Take**: An information-theoretic framing of jailbreak probability gives defenders something they've lacked — a measurable signal for how much a compositional wrapper actually reduces apparent harm, which should directly inform prompt filter and classifier design.

---

### 9. [Pincer: Resource Authorization for Agents using a Digital Twin](https://arxiv.org/abs/2610.02569)
**Source**: arXiv cs.CR

Long-horizon autonomous coding agents (including deployed systems like Claude and Codex) currently rely on user-mediated authorization and automode sandboxes that sacrifice too much functionality to gain security. Pincer proposes a digital twin approach — a shadow execution environment that simulates agent actions to predict and gate resource authorization before real-world execution.

> **Take**: Digital twin pre-execution authorization is one of the more operationally viable authorization models I've seen for autonomous agents — it preserves capability while giving security teams an enforceable choke point, which is exactly the trade-off most organizations need.

---

### 10. [Hop-Decayed Influence: New Vulnerabilities of Structural Auxiliary Indexing in GraphRAG Pipelines with LLM](https://arxiv.org/abs/2610.02373)
**Source**: arXiv cs.CR

Prior GraphRAG attacks targeted instance-level components (nodes, edges, triples), but this research identifies schema-level auxiliary structures — semantic summaries, hierarchical edges, pre-computed retrieval scores built during offline indexing — as an entirely new attack surface. The Hop-Decayed Influence (HDI) attack exploits these structures to systematically bias retrieval priority at query time.

> **Take**: If your enterprise RAG deployment uses GraphRAG, your threat model almost certainly doesn't account for offline index poisoning at the schema level — this paper defines the attack surface you need to start modeling.

---

*Outwire — signal over noise.*