## Outwire | AI Security Digest — Week of April 17, 2026
*Issue #1*

---

### 1. [Lack of Isolation in Agentic Browsers Resurfaces Old Vulnerabilities](https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/)
**Source**: Trail of Bits

Trail of Bits exploited missing isolation mechanisms in multiple agentic browsers to demonstrate XSS- and CSRF-equivalent attacks — cross-site data leaks and disinformation injection — against AI agents that treat external web content as trusted input. The root cause isn't novel: it's the same inadequate isolation the web security community spent a decade fixing, now being reintroduced by AI browser integrations that skipped that history.

> **Take**: We're re-running the entire browser security gauntlet from 2005 — any enterprise deploying agentic browsers should gate on whether the vendor can articulate their isolation model before the thing touches production.

---

### 2. [Microsoft, Salesforce Patch AI Agent Data Leak Flaws](https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws)
**Source**: Dark Reading

Prompt injection vulnerabilities in both Salesforce Agentforce and Microsoft Copilot allowed external attackers to exfiltrate sensitive data from enterprise environments — two of the most widely deployed AI agent platforms, patched concurrently. The fact that both flagship enterprise AI products shipped with exploitable prompt injection in the same window should be a calibration point for anyone doing AI vendor risk assessment.

> **Take**: If the biggest players are shipping exploitable prompt injection in GA products, assume your AI vendors are too — add it to your standard vulnerability disclosure questionnaire now.

---

### 3. [How AI Assistants Are Moving the Security Goalposts](https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/)
**Source**: Krebs on Security

AI agents with broad access to files, credentials, and online services are erasing the distinction between trusted user and insider threat — and simultaneously collapsing the skill barrier for attackers. The traditional security perimeter assumes human actors operating at human speed; autonomous agents break both assumptions at once.

> **Take**: The insider threat model needs to be updated to include compromised or manipulated AI agents as a first-class threat actor, not an edge case.

---

### 4. [Using Threat Modeling and Prompt Injection to Audit Comet](https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/)
**Source**: Trail of Bits

Before launch, Perplexity engaged Trail of Bits to test their Comet browser's AI assistant, where four distinct prompt injection techniques successfully extracted private Gmail data from users — all stemming from external content being treated as trusted input rather than an adversarial channel. The five recommendations Trail of Bits distilled are the closest thing to a pre-deployment checklist the industry has right now.

> **Take**: This is the audit template I'd hand to any team shipping an AI-powered product — the TRAIL threat model approach is actionable, not just theoretical.

---

### 5. [Mythos and Cybersecurity](https://www.schneier.com/blog/archives/2026/04/mythos-and-cybersecurity.html)
**Source**: Schneier on Security

Anthropic's Claude Mythos Preview is a vulnerability-finding AI model deemed too dangerous for public release, with access restricted to roughly 50 organizations including Microsoft, Apple, AWS, and CrowdStrike. The concentration of offensive AI capability in a small set of vendors creates a new kind of supply chain risk: if any of those 50 organizations are compromised, the blast radius is the entire software ecosystem.

> **Take**: Restricted access isn't a security model — it's a risk deferral, and the enterprises on that access list just became high-value targets.

---

### 6. [On Anthropic's Mythos Preview and Project Glasswing](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
**Source**: Schneier on Security

Anthropic launched Project Glasswing to run Mythos against public and proprietary software at scale — finding and patching vulnerabilities proactively before the model's offensive capabilities can be reverse-engineered or leaked. This is an unprecedented attempt at coordinated AI-assisted vulnerability remediation, and it sets a precedent for how frontier AI labs manage capability overhang.

> **Take**: Watch how Glasswing handles disclosure to proprietary software vendors — the coordination model they establish will either become an industry standard or a cautionary tale.

---

### 7. [Inside an AI-Enabled Device Code Phishing Campaign](https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/)
**Source**: Microsoft Security

Threat actors are using AI and end-to-end automation to generate live device authentication codes on demand, enabling sustained post-compromise access at scale beyond what traditional phishing infrastructure supports. This isn't AI-assisted phishing in the buzzword sense — it's fully automated credential compromise pipelines that degrade the effectiveness of time-bounded authentication flows.

> **Take**: Device code flow should be on your conditional access audit list today; the assumption that it's low-risk because of its complexity no longer holds.

---

### 8. [Hijacking Large Audio-Language Models via Imperceptible Auditory Prompt Injection](https://arxiv.org/abs/2604.14604)
**Source**: arXiv cs.CR

Researchers demonstrate auditory prompt injection against large audio-language models — imperceptible audio perturbations that hijack model behavior without requiring text access — extending the prompt injection threat model to the continuous, high-dimensional audio channel. Any enterprise deploying voice-based AI assistants for customer service, meeting transcription, or call analysis is now in scope for this attack class.

> **Take**: Multimodal AI deployments have been evaluated on text-channel prompt injection alone; audio is an unguarded input surface and this paper draws the map for attackers.

---

### 9. [What We Learned About TEE Security from Auditing WhatsApp's Private Inference](https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/)
**Source**: Trail of Bits

Trail of Bits audited Meta's WhatsApp Private Inference — a system running LLM inference on encrypted messages inside trusted execution environments — and found several vulnerabilities before launch, with the full report now public. This is one of the most technically detailed public examinations of production AI-in-TEE architecture available, covering concrete vulnerability classes that will recur across any enterprise attempting confidential AI inference.

> **Take**: If your organization is evaluating confidential computing for AI workloads, this audit report is required reading — the failure modes here will show up in your architecture too.

---

### 10. [n8n Webhooks Abused Since October 2025 to Deliver Malware via Phishing Emails](https://thehackernews.com/2026/04/n8n-webhooks-abused-since-october-2025.html)
**Source**: The Hacker News

Threat actors have weaponized n8n — a widely used AI workflow automation platform — as trusted phishing infrastructure since at least October 2025, using its webhooks to bypass email security filters and deliver malware or fingerprint targets. The attack exploits the implicit trust organizations extend to their own automation tooling, turning shadow AI deployments into persistent delivery mechanisms.

> **Take**: Every unsanctioned AI workflow tool in your environment is a potential trusted relay for attackers — shadow AI isn't just a governance problem, it's an active attack surface.

---

*Outwire — signal over noise.*