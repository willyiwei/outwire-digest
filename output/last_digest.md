## Outwire | AI Security Digest — Week of November 02, 2026
*Issue #30*

---

### 1. [Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers](https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html)
**Source**: The Hacker News

Two critical vulnerabilities in Langflow — covering every release from 1.0.0 through 1.12.8 — allow unauthenticated remote attackers to bypass authentication or execute arbitrary code, with the only remediation being an upgrade to 1.13.0. Langflow's role as a popular AI agent and workflow orchestration platform means the blast radius hits enterprises running production AI pipelines directly.

> **Take**: If your org is running any AI workflow tooling without a firm inventory and patch cadence, Langflow is exactly the kind of quiet infrastructure component that slips through — audit it now.

---

### 2. [A Supply Chain Attack Put Malicious Anthropic Claude Extensions on Thousands of Devices](https://www.wired.com/story/trojan-malware-targets-thousands-of-anthropic-claude-developer-systems/)
**Source**: WIRED Security

A trojanized Claude extension reached approximately 5,000 developer machines in a supply chain attack targeting AI developer tooling, with only a coding flaw in the malicious payload limiting the full infection. The attack demonstrates that LLM-branded extensions are now an active supply chain target, not a theoretical one.

> **Take**: The attacker's buggy code saved thousands of developers here — that's not a defense strategy, and IDE extension provenance needs to be treated with the same rigor as any third-party dependency.

---

### 3. [Inside a malicious Claude Code-branded extension and its persistent SSH backdoor](https://www.microsoft.com/en-us/security/blog/2026/10/30/inside-malicious-claude-code-branded-cursor-extension-persistent-ssh-backdoor/)
**Source**: Microsoft Security

Microsoft's detailed technical analysis of the malicious Claude Code–branded Cursor extension reveals a persistent SSH backdoor mechanism used to maintain long-term access to compromised developer machines. This is the authoritative forensic breakdown of the same supply chain attack, with concrete detection and remediation guidance.

> **Take**: Read this one for the IOCs and remediation steps — the SSH persistence mechanism is the part that makes this incident linger well past initial detection.

---

### 4. [How We Took Over ChatGPT Accounts](https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/)
**Source**: Simon Willison

Parameter Labs exploited a sandbox escape in ChatGPT's HTML preview (formerly Canvas) feature, where attacker-controlled HTML rendered in an insufficiently isolated iframe could execute code in the authenticated user's session and exfiltrate private conversations. OpenAI rated it P1 and patched within eight days of disclosure.

> **Take**: The artifacts/HTML preview pattern is proliferating across every major LLM product — this exploit is a blueprint for what's coming on other platforms that haven't done the sandbox audit yet.

---

### 5. [A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html)
**Source**: The Hacker News

A malicious ChatGPT share link could trigger attacker code execution within the victim's authenticated session, enabling full private conversation access — disclosed via OpenAI's bug bounty and fixed within eight days at P1 severity. The attack vector requires nothing from the victim beyond clicking a shared link, making it trivially weaponizable in phishing campaigns.

> **Take**: Enterprises allowing ChatGPT for business use should treat shared conversation links with the same suspicion as any unsolicited URL — user education here is not optional.

---

### 6. [Hiding Capabilities in AI Models](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html)
**Source**: Schneier on Security

Researchers demonstrate that AI models can provably conceal dangerous capabilities from pre-deployment evaluations by embedding encrypted neural networks within host model weights that only activate upon receiving a secret trigger — directly invalidating the foundational assumption of capability evaluation as a safety gate. This undermines the entire pre-deployment red-teaming paradigm that most enterprise AI governance frameworks currently rely on.

> **Take**: Every AI safety evaluation process built around "we tested it and didn't find dangerous behavior" just became significantly weaker — this research demands a rethink of what deployment assurance actually means.

---

### 7. [New VOLTA Infostealer Uses Claude, Gemini, and Kimi AI to Rank Victims by Financial Value](https://thehackernews.com/2026/11/new-volta-infostealer-uses-claude.html)
**Source**: The Hacker News

VOLTA-AUTODOXER is a Windows infostealer that harvests credentials, cookies, Outlook data, and Slack workspaces, then feeds stolen data to multiple commercial LLM APIs to automatically prioritize victims by monetization potential. This marks a concrete shift from LLMs as attack-generation tools to LLMs as post-exploitation intelligence infrastructure.

> **Take**: I'd watch for this pattern to proliferate fast — LLM-assisted victim triage dramatically lowers the cost of targeted follow-on attacks and raises the ceiling on what commodity malware can accomplish.

---

### 8. [Shadowy AI Relay Disables OpenAI Codex, Claude Code Sandboxes](https://www.darkreading.com/threat-intelligence/ai-relay-service-openai-codex-claude-code-sandboxes)
**Source**: Dark Reading

An undisclosed relay service is proxying OpenAI Codex and Claude Code to users in regions where these products are officially unavailable — with sandbox security controls stripped out in the process. Enterprises with distributed workforces risk employees routing sensitive code and data through this service without visibility into the missing protections.

> **Take**: Shadow AI adoption was already a detection problem; shadow AI with disabled sandboxes routed through an anonymous third-party relay is an exfiltration incident waiting to be discovered.

---

### 9. [Claude Model Builds Exploits Across Major Browsers & OSes](https://www.darkreading.com/application-security/claude-model-exploits-major-browsers-oses)
**Source**: Dark Reading

An unreleased Claude model demonstrated by Anthropic successfully discovered and chained vulnerabilities across Chrome, Safari, Android, Windows, and Linux — representing a concrete leap in autonomous multi-platform exploit generation capability. This moves LLM-assisted exploitation from proof-of-concept single-vuln scenarios into full kill-chain automation territory.

> **Take**: The gap between "AI can help write exploits" and "AI can autonomously build cross-platform exploit chains" just closed — threat modeling assumptions built before this capability existed need revisiting.

---

### 10. [CLIC: Closed-Loop Intent Consistency for Securing LLM-Driven Control in Open RAN](https://arxiv.org/abs/2610.40744)
**Source**: arXiv cs.CR

Researchers disclose runtime prompt injection and residual virtual prompt injection (VPI) attacks against LLMs integrated into Open RAN control loops via the RAN Intelligent Controller, where attackers can manipulate network slicing and resource management decisions without triggering interface authentication. The proposed CLIC defense uses closed-loop intent verification to detect and block these manipulations before they affect network state.

> **Take**: LLM control of network infrastructure is moving from research to production faster than the security community is building defenses — this attack class will matter at scale sooner than most telecom security teams expect.

---

*Outwire — signal over noise.*