## Outwire | AI Security Digest — Week of May 25, 2026
*Issue #7*

---

### 1. [The Misattribution Gap: When Memory Poisoning Looks Like Model Failure in Agentic AI Systems](https://arxiv.org/abs/2605.22842)
**Source**: arXiv cs.CR

Researchers formalize the "Misattribution Gap" in multi-agent pipelines: memory-layer attacks that inject policy-formatted documents into shared vector stores produce behavioral drift (Semantic Norm Drift) that is structurally indistinguishable from model misalignment, causing defenders to remediate the wrong layer. This means existing model-focused monitoring and retraining responses are blind to an entire attack class operating below them in the stack.

> **Take**: If your agentic incident response playbook treats all misbehavior as a model problem, you're almost certainly going to burn cycles retraining clean models while the poisoned memory store sits untouched — audit your shared vector stores as first-class attack surfaces.

---

### 2. [Prompt Overflow: What the Guardrail Inspects Is Not What the Model Infers](https://arxiv.org/abs/2605.23196)
**Source**: arXiv cs.CR

Guardrail models that truncate or segment overlength prompts before inspection create a structural mismatch: the safety checker evaluates a different token sequence than the LLM actually processes, enabling prompt injection payloads to survive screening by exploiting that gap. This effectively turns a fundamental input-handling constraint into a bypass primitive against the primary enterprise defense layer.

> **Take**: Guardrails built on truncation-based inspection are architecturally broken against adversarial long inputs — I'd treat any deployment where max context differs between the safety checker and the downstream model as an open vulnerability until proven otherwise.

---

### 3. [Introducing RAMPART and Clarity: Open source tools to bring safety into Agent development workflow](https://www.microsoft.com/en-us/security/blog/2026/05/20/introducing-rampart-and-clarity-open-source-tools-to-bring-safety-into-agent-development-workflow/)
**Source**: Microsoft Security

Microsoft released RAMPART and Clarity as open-source tools targeting safety gaps in production AI agents that execute code, access email and CRM systems, and take actions across connected enterprise infrastructure — a direct acknowledgment that current development workflows ship agents without adequate security instrumentation. These aren't research prototypes; they're positioned as developer-workflow integrations.

> **Take**: This is the one to actually evaluate this sprint — Microsoft shipping open-source tooling here signals they're seeing enough unsafe agent deployments in enterprise telemetry to justify the investment, and that's a threat model signal worth taking seriously.

---

### 4. [PoisonForge: Task-Level Targeted Poisoning Benchmark for Instruction-Tuned LLMs](https://arxiv.org/abs/2605.23168)
**Source**: arXiv cs.CR

PoisonForge demonstrates that an adversary can insert a small number of crafted instruction-response pairs into fine-tuning datasets to cause targeted behavioral corruption on specific task families across 12 open-weight models, while the model behaves normally elsewhere — a supply chain attack against the fine-tuning pipeline that evades broad behavioral testing. The benchmark parameterizes the attack along four dimensions, giving defenders a concrete threat model to test against.

> **Take**: Any team fine-tuning on unvetted datasets — Hugging Face pulls, third-party instruction sets, contractor-curated data — should be running PoisonForge-class evaluations before promoting models to production; dataset provenance is now a security control, not just a quality concern.

---

### 5. [What Does the Server See? Understanding Privacy Leakage from Large Language Models in Split Inference](https://arxiv.org/abs/2605.23158)
**Source**: arXiv cs.CR

Researchers introduce ActInv, an attack that reconstructs client-side input from intermediate activations transmitted during split inference LLM deployments — breaking the core privacy assumption that motivated the architecture in the first place. Enterprises deploying split inference to keep sensitive prompts off cloud infrastructure are exposed if the server-side component is compromised or adversarial.

> **Take**: Split inference was being sold as a privacy-preserving compromise for regulated industries; ActInv demonstrates it's a threat model, not a control — factor this into any on-prem/cloud hybrid LLM deployment design.

---

### 6. [CachePrune: Privacy-Aware and Fine-Grained KV Cache Sharing for Efficient LLM Inference](https://arxiv.org/abs/2605.23640)
**Source**: arXiv cs.CR

Cross-user KV cache sharing in LLM serving infrastructure introduces a side-channel that allows adversaries to infer other users' inputs by probing cache reuse patterns; CachePrune proposes fine-grained cache partitioning as a defense that preserves performance without disabling sharing entirely. This is a production infrastructure vulnerability, not a theoretical one — any multi-tenant LLM serving stack is potentially affected.

> **Take**: If you're running a shared LLM inference layer across internal teams or customers, validate your serving framework's cache isolation model now — this side-channel is the kind of low-visibility data leak that won't show up in application logs.

---

### 7. [Beyond Zero: Enterprise Security for the AI Era](https://arxiv.org/abs/2605.22985)
**Source**: arXiv cs.CR

This paper argues that zero trust's application-level trust boundary is insufficient for autonomous AI agents operating at machine speed across corporate data, and proposes "Beyond Zero" — a per-resource, per-method authorization model that combines static policy guarantees with dynamic AI-driven reasoning to shrink the blast radius of agent actions. The architecture targets the gap where agents inherit broad application-level permissions rather than operating under fine-grained, action-scoped controls.

> **Take**: The framing is right even if the implementation is academic — the enterprise identity teams I'd worry about are the ones still thinking about agent permissions as a role assignment problem rather than an action authorization problem.

---

### 8. [A Hacker Group Is Poisoning Open Source Code at an Unprecedented Scale](https://www.wired.com/story/teampcp-software-supply-chain-attack-spree-github/)
**Source**: WIRED Security

TeamPCP has executed a systematic supply chain poisoning campaign across hundreds of organizations through GitHub and multiple package ecosystems, with confirmed impact on a Microsoft-published Python SDK and AI/ML adjacent tooling in the dependency graph. The scale and cross-ecosystem reach represent a qualitative escalation from previous supply chain campaigns.

> **Take**: With TeamPCP now confirmed hitting Python SDKs and AI tooling dependencies, any enterprise ingesting open-source packages into an AI/ML pipeline without hash-pinning and provenance verification is carrying unquantified exposure right now.

---

### 9. [We hardened zizmor's GitHub Actions static analyzer](https://blog.trailofbits.com/2026/05/22/we-hardened-zizmors-github-actions-static-analyzer/)
**Source**: Trail of Bits

A `pull_request_target` misconfiguration in `aquasecurity/trivy-action` was exploited to exfiltrate secrets and backdoor LiteLLM on PyPI — a concrete AI tooling supply chain compromise via CI/CD pipeline — with Trail of Bits subsequently hardening zizmor to detect the class of misconfiguration that made it possible. LiteLLM is widely deployed in enterprise LLM routing infrastructure.

> **Take**: If LiteLLM is in your stack and you haven't verified the integrity of your pinned version against the pre-compromise state, that's the first thing to check before anything else this week.

---

### 10. [On AI Security](https://www.schneier.com/blog/archives/2026/05/on-ai-security.html)
**Source**: Schneier on Security

The referenced Berryville IML report argues that AI security cannot be validated by maximizing benchmark scores — because security and privacy are emergent systemic properties that benchmarks structurally cannot measure — and traces why 30 years of software security engineering methods don't transfer cleanly to ML systems. This is a foundational framing problem that affects how enterprises are currently auditing and certifying AI deployments.

> **Take**: I'd send this to every team that's using benchmark pass rates as a proxy for production security assurance — the report articulates exactly why that practice creates false confidence, and it's a conversation worth forcing before the next audit cycle.

---

*Outwire — signal over noise.*