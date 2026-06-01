## Outwire | AI Security Digest — Week of June 01, 2026
*Issue #8*

---

### 1. [OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain Attack](https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html)
**Source**: The Hacker News

A malicious npm package named `codexui-android` — posing as a remote web UI for OpenAI Codex — has been stealing authentication tokens from developers, with 29,000 weekly downloads and the package still live on the registry. This is a direct LLM supply chain attack targeting developer environments with production AI access credentials.

> **Take**: The 29K weekly download count means this has enterprise blast radius — any team using Codex in CI/CD pipelines should audit their token exposure immediately and treat this as a credential rotation event, not just a package removal.

---

### 2. [ChatGPhish Vulnerability Turns ChatGPT Web Summaries Into a Phishing Surface](https://thehackernews.com/2026/05/chatgphish-vulnerability-turns-chatgpt.html)
**Source**: The Hacker News

Permiso Security disclosed ChatGPhish, a technique exploiting ChatGPT's implicit trust in Markdown rendering to trigger prompt injections via embedded links and images, converting the AI's web summary responses into a phishing delivery mechanism. The chatgpt.com renderer trusts Markdown in a way that opens end users to credential harvesting without any traditional malicious attachment.

> **Take**: This is the category of vulnerability that's going to keep compounding — every LLM feature that renders external content is a potential injection surface, and most enterprises haven't mapped those surfaces at all.

---

### 3. [Attackers Use LLM Agent for Post-Exploitation After Marimo CVE-2026-39987 Exploit](https://thehackernews.com/2026/05/attackers-use-llm-agent-for-post.html)
**Source**: The Hacker News

A threat actor exploited CVE-2026-39987 in a publicly-accessible Marimo notebook to gain initial access, then deployed an LLM agent to automate post-compromise actions including cloud credential extraction. This is a documented instance of adversaries operationalizing LLM agents as a post-exploitation tool in production environments.

> **Take**: The pivot from "LLM-assisted" to "LLM-agentic" post-exploitation changes the speed and scale calculus for incident response — your detection and containment timelines were not built for automated credential harvesting driven by reasoning models.

---

### 4. [Hackers Used Meta's AI Support Bot to Seize Instagram Accounts](https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/)
**Source**: Krebs on Security

Instructions circulating on Telegram showed how to manipulate Meta's AI support assistant into triggering account password resets, resulting in the compromise of high-profile Instagram accounts including the Obama White House and a U.S. Space Force senior NCO. The attack demonstrates prompt injection or social engineering against a production LLM-based support system with privileged account recovery capabilities.

> **Take**: Any enterprise deploying an LLM support bot with backend write access to identity or account systems needs to treat that integration as a privileged access path — the same controls you'd put on a service account should apply to the model's tool permissions.

---

### 5. [The Surface You Test Is Not the Surface That Breaks](https://arxiv.org/abs/2605.30454)
**Source**: arXiv cs.CR

Researchers demonstrate that tool-augmented LLM agents have a second, under-evaluated injection surface in tool *descriptions* — not just tool outputs — that attackers can target with identical payloads while bypassing evaluations focused solely on tool output channels. Current benchmark ASR numbers are therefore structurally incomplete as a security signal.

> **Take**: If your red team is only injecting through tool outputs, you're testing a fraction of the actual attack surface — tool descriptions are read every turn and attackers will pick the weakest channel, not the one you evaluated.

---

### 6. [Depth-Dependent Indirect Prompt Injection in Tool-Calling ReAct Agents](https://arxiv.org/abs/2605.30686)
**Source**: arXiv cs.CR

New research maps three under-explored risk dimensions for indirect prompt injection in ReAct agents — injection depth within the observation loop, payload framing, and turn-budget sensitivity — against agents deployed for scheduling, file retrieval, and data access. Existing benchmarks evaluated at fixed injection positions miss significant attack variance across these dimensions.

> **Take**: Enterprises deploying ReAct agents for anything touching data or scheduling need to pressure-test injection resilience across variable depth and budget conditions, not just the happy-path scenarios vendors demo.

---

### 7. [What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security Stacks](https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html)
**Source**: The Hacker News

Analysis of 2,000 internet-exposed applications built with AI coding tools found employees are now shipping full applications wired into production systems — without security or IT involvement — representing a materially larger shadow AI risk than the prompt-leakage concerns of a year ago. The artifact has moved from a prompt to a deployed product, and the attack surface has moved with it.

> **Take**: Shadow AI is no longer a data governance problem — it's a perimeter problem, and your AppSec program almost certainly has no visibility into what's getting deployed out of Cursor or Copilot Workspaces directly to cloud infrastructure.

---

### 8. [How we contain Claude across products](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything)
**Source**: Simon Willison

Anthropic published detailed technical documentation of their sandboxing and containment architecture across Claude.ai, Claude Code, and Cowork — covering process sandboxes, VMs, and agent isolation mechanisms — which Simon Willison flags as unusually thorough compared to the industry norm of opaque security claims. This is a rare concrete reference architecture for LLM agent containment from a frontier lab.

> **Take**: Read this as a benchmark, not just an Anthropic product explainer — if your own agentic deployments can't articulate equivalent containment properties, that gap is your risk.

---

### 9. [Strengthening Polymorphic Prompt Assembling: Dynamic Separator Generation Against Emerging Prompt Injection Attacks](https://arxiv.org/abs/2605.30534)
**Source**: arXiv cs.CR

Researchers identify a "blast-radius vulnerability" in Polymorphic Prompt Assembling (PPA) — the static separator pool can be exploited once any separator leaks — and propose per-request dynamic separators using domain-separated SHA-256 digests keyed on timestamp, session ID, and cryptographic nonce to generate unique canary pairs. This closes a structural weakness in one of the more practical prompt injection mitigations for LLM agents.

> **Take**: If your LLM agent pipeline is using PPA with a fixed separator pool, the static variant is now a known-weak configuration — the upgrade path here is well-defined and worth implementing before this becomes an active exploitation pattern.

---

### 10. [CacheProbe: Auditing Prompt Cache Isolation in Gateway APIs](https://arxiv.org/abs/2605.30613)
**Source**: arXiv cs.CR

Researchers investigate whether OpenRouter's API gateway architecture introduces timing-based vulnerabilities in prompt caching implementations, building on prior ICML work showing that many LLM inference APIs are vulnerable to KV cache timing attacks and metadata disclosure. Gateway-level caching — increasingly common as a cost optimization — is a leakage surface that most enterprise API security reviews aren't accounting for.

> **Take**: If you're routing LLM traffic through a gateway that does prompt caching for latency or cost reasons, you need to verify that cache isolation is enforced per-tenant — this is the kind of side-channel that gets exploited quietly long before it gets patched.

---

*Outwire — signal over noise.*