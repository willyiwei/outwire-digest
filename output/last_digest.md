## Outwire | AI Security Digest — Week of May 18, 2026
*Issue #6*

---

### 1. [Hidden in Memory: Sleeper Memory Poisoning in LLM Agents](https://arxiv.org/abs/2605.15338)
**Source**: arXiv cs.CR

Researchers demonstrate a delayed attack vector against stateful LLM agents: adversarial content embedded in documents, webpages, or repositories causes the assistant to write fabricated memories that persist across sessions and silently corrupt future interactions. Unlike prompt injection, this attack survives the original context and compounds over time — a critical distinction for any enterprise deploying persistent-memory agents.

> **Take**: Persistent memory is the feature that turns a useful assistant into a persistent attack surface, and most enterprise deployments aren't logging or auditing what gets written to memory stores — fix that before you expand agent rollouts.

---

### 2. [Compositional Jailbreaking: An Empirical Analysis of Mutator Chain Interactions in Aligned LLMs](https://arxiv.org/abs/2605.15598)
**Source**: arXiv cs.CR

Researchers systematically studied chaining weak jailbreak transformations in sequence, finding that individually ineffective mutations can combine to reliably bypass safety alignment in deployed LLMs. The implication for enterprise AI deployments is that guardrail testing against known single-technique jailbreaks is insufficient if you haven't evaluated compositional attack chains.

> **Take**: Red-teaming your aligned model against individual techniques and calling it done is now a false assurance — your next evaluation cycle needs multi-step mutation chains in scope.

---

### 3. [How Dangerous Is Anthropic's Mythos AI?](https://www.schneier.com/blog/archives/2026/05/how-dangerous-is-anthropics-mythos-ai.html)
**Source**: Schneier on Security

Anthropic restricted Claude Mythos Preview from general release due to its exceptional capability at finding software vulnerabilities, instead making it available only to a vetted group for defensive scanning — an unprecedented vendor-imposed capability gate on an AI model. Schneier contextualizes what this restriction signals about the actual offensive potential and what it means when a lab self-censors a product rather than shipping it.

> **Take**: A vendor voluntarily withholding a model from general availability is a more meaningful capability signal than any benchmark — treat it as a forcing function to audit what vulnerabilities in your own codebase you haven't found yet.

---

### 4. [OpenAI's GPT-5.5 is as Good as Mythos at Finding Security Vulnerabilities](https://www.schneier.com/blog/archives/2026/05/openais-gpt-5-5-is-as-good-as-mythos-at-finding-security-vulnerabilities.html)
**Source**: Schneier on Security

The UK AI Security Institute evaluated GPT-5.5's vulnerability-discovery capabilities and found them comparable to Anthropic's restricted Mythos model — and GPT-5.5 is generally available to anyone. This means the offensive capability Anthropic chose to gate is already accessible through a competing, widely-deployed model.

> **Take**: The restricted-access guardrail Anthropic built around Mythos is strategically irrelevant if the same capability ships in GPT-5.5 via API — the threat model for AI-assisted exploitation just became everyone's problem, not just Anthropic customers'.

---

### 5. [The Boring Stuff is Dangerous Now](https://www.darkreading.com/cyber-risk/ai-code-and-agents-forces-defenders-adapt)
**Source**: Dark Reading

AI agents are autonomously discovering and exploiting obscure vulnerability classes at the same time that AI-generated code is flooding production systems with novel flaws — defenders face both an accelerated attack cycle and a larger, lower-quality attack surface simultaneously. The compounding effect demands architectural rethinking of detection and response, not incremental tuning.

> **Take**: The asymmetry here is the real problem: AI-generated code ships at developer speed but gets reviewed at human speed — close that gap or accept that your vulnerability backlog will structurally grow faster than you can remediate.

---

### 6. [uGen: An Agentic Framework for Generating Microarchitectural Attack PoCs](https://arxiv.org/abs/2605.15503)
**Source**: arXiv cs.CR

Researchers built an LLM-based agentic framework that automatically generates functional proof-of-concept implementations of microarchitectural attacks (e.g., cache-timing, transient execution), addressing the portability and expertise barriers that have historically limited systematic assessment of hardware-level vulnerabilities. This lowers the skill floor for generating working hardware attack code.

> **Take**: Microarchitectural exploitation has been gated by deep expertise for years — LLM agents eroding that gate means your hardware attack surface needs to be in scope for AI red-team planning, not just your software stack.

---

### 7. [TanStack Supply Chain Attack Hits Two OpenAI Employee Devices, Forces macOS Updates](https://thehackernews.com/2026/05/tanstack-supply-chain-attack-hits-two.html)
**Source**: The Hacker News

A supply chain compromise of TanStack — a widely used JavaScript library — resulted in malicious code executing on two OpenAI employee devices within the corporate environment; OpenAI confirmed no production systems, user data, or IP were accessed. The incident illustrates how developer toolchain supply chain attacks are a viable initial access vector specifically targeting AI company infrastructure.

> **Take**: AI labs are high-value targets for supply chain attacks precisely because their developer environments sit adjacent to model weights and training pipelines — standard endpoint controls aren't enough if the compromise rides in on a trusted npm package.

---

### 8. [Ivanti, Fortinet, SAP, VMware, n8n Patch RCE, SQL Injection, Privilege Escalation Flaws](https://thehackernews.com/2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html)
**Source**: The Hacker News

Among a batch of critical patches this week, n8n — a workflow automation platform increasingly used as an AI agent orchestration layer — received an RCE fix, while Ivanti Xtraction (CVE-2026-8043, CVSS 9.6) carries critical information disclosure risk. RCE in an agent orchestration platform is a direct path to hijacking automated workflows with privileged system access.

> **Take**: n8n RCE is the one to prioritize in this roundup — agent orchestration platforms run with broad permissions by design, and RCE there isn't just a server compromise, it's full control over every automated workflow it manages.

---

### 9. [Rethinking the Security of DP-SGD: A Corrected Analysis of Differentially Private Machine Learning](https://arxiv.org/abs/2605.15648)
**Source**: arXiv cs.CR

Researchers identify a fundamental mismatch between the formal privacy analysis of DP-SGD and how it's actually implemented in practice, showing that the privacy guarantees enterprises believe they have from differential privacy in ML training may be weaker than claimed. This undermines a core compliance and risk management argument for DP-SGD adoption in regulated industries.

> **Take**: If your data governance posture leans on DP-SGD as a training data protection guarantee, this paper deserves a read by whoever made that architectural decision — the math and the implementation may not be saying the same thing.

---

### 10. [Enabling Adversarial Robustness in AI Models through Kubeflow MLOps](https://arxiv.org/abs/2605.15249)
**Source**: arXiv cs.CR

Researchers propose an architecture integrating Kubeflow-based MLOps pipelines with automated adversarial attack detection at inference time, triggering defense mechanisms in Kubernetes-hosted ML deployments without taking models offline. It addresses a real gap: Kubernetes provides infrastructure orchestration but has no native understanding of adversarial ML inputs.

> **Take**: Inference-time adversarial detection inside the MLOps pipeline is the right architectural layer to target — I'd watch whether this approach holds up against adaptive attackers who know the defense is present.

---

*Outwire — signal over noise.*