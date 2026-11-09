## Outwire | AI Security Digest — Week of November 09, 2026
*Issue #31*

---

### 1. [Threat actors use agentic AI tooling to find and abuse exposed secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)
**Source**: Microsoft Security

Microsoft Threat Intelligence confirmed threat actors are deploying ARTEX, an agentic offensive security framework, to autonomously scan GitHub for exposed OAuth application secrets and then use those compromised applications to pivot inside victim tenants — a fully automated, multi-stage attack chain requiring minimal human involvement.

> **Take**: This is the clearest evidence yet that agentic AI has crossed from red team curiosity to active threat actor infrastructure — if your OAuth secrets have ever touched a public repo, treat them as burned today.

---

### 2. [ARTEX abuse expands as cybercriminals target financial sector](https://www.microsoft.com/en-us/security/blog/2026/11/06/artex-abuse-expands-as-cybercriminals-target-financial-sector/)
**Source**: Microsoft Security

Storm-3358, a financially motivated threat actor, has expanded ARTEX framework operations specifically against financial sector organizations as of October 2026, signaling that agentic AI offensive tooling is now being sector-targeted rather than opportunistically deployed.

> **Take**: Sector-specific targeting with agentic tooling means adversaries are tuning their AI agents for domain context — financial sector defenders need to pressure-test their AI-adjacent attack surface now, not after the breach.

---

### 3. [Attackers Crash Claude's 'Office Party' Flaw to Run Malicious Code on Linux](https://www.darkreading.com/endpoint-security/attackers-claude-office-party-flaw-malicious-code-linux)
**Source**: Dark Reading

A flaw in Claude's document-processing tool allows attackers to craft a malicious temporary file that Claude can access and execute on a user's Linux machine, turning a document-handling workflow into an arbitrary code execution vector on the endpoint.

> **Take**: Document-processing pipelines in LLM tooling are becoming the new macro-enabled Office files — enterprises deploying Claude in any document-adjacent workflow need to sandbox these processes at the OS level, not rely on model guardrails.

---

### 4. [Claude Code's "Don't Ask Again" File Exposes Passwords and Keys in 1,122 Public Copies on GitHub](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html)
**Source**: The Hacker News

Claude Code's "Yes, and don't ask again" approval flow persists the full plaintext command — including embedded secrets — into a project settings file, which Apiiro confirmed has resulted in 1,122 public GitHub repositories leaking passwords and API keys verbatim.

> **Take**: AI coding assistants are creating a new class of secret sprawl that existing DLP and secret-scanning tools weren't built to catch — your AppSec team needs Claude Code's settings files added to their scanning scope immediately.

---

### 5. [Taiwan-Based Hacker Used BOSSAI AI Agents to Steal Taipei Emergency Dispatch Records](https://thehackernews.com/2026/11/taiwan-based-hacker-used-bossai-ai.html)
**Source**: The Hacker News

A single attacker leveraged BOSSAI AI agents to exfiltrate emergency dispatch records across seven Taipei districts and discover an unauthenticated fire department platform exposing patient ECG data and ambulance footage dating to 2018 — a solo operation with breach scale previously requiring a team.

> **Take**: The force-multiplier effect of AI agents on individual attackers is now empirically demonstrated against critical infrastructure — threat modeling that assumes organized groups as the minimum bar for large-scale data theft is obsolete.

---

### 6. [Free Chinese AI Models Are Getting Scary Good at Hacking](https://www.wired.com/story/free-chinese-ai-models-are-getting-scary-good-at-hacking/)
**Source**: WIRED Security

Experimental testing against simulated networks showed DeepSeek and GLM performing near parity with OpenAI's most advanced (non-public) cyber model on network penetration tasks, establishing that capable offensive AI is now freely accessible rather than gated behind closed APIs.

> **Take**: The assumption that offensive AI capability tracks with API access controls is broken — defenders need to price in adversaries running uncensored, locally-hosted models with no usage restrictions or rate limits.

---

### 7. [AI Gave Your Incident Archive a Second Job](https://www.darkreading.com/cyber-risk/ai-gave-your-incident-archive-second-job)
**Source**: Dark Reading

Security vendors are increasingly using enterprise incident records — IR reports, threat intelligence feeds, forensic artifacts — to train their AI models, turning historical breach data into a model training asset that may exfiltrate TTPs and victim context outside the original data handling agreement.

> **Take**: I'd treat any security vendor contract signed before 2025 as likely silent on AI training rights — your legal team needs to audit those agreements before your incident archive becomes someone else's training corpus.

---

### 8. [Spooky New Infostealer Malware Uses AI to 'Autodox' Victims](https://www.wired.com/story/kernel-panic-volta-autodoxer-ai-infostealer-malware/)
**Source**: WIRED Security

Volta-Autodoxer is a newly uncovered infostealer that uses AI tools to automatically aggregate and cross-correlate stolen data — credentials, credit cards, session tokens, and personal records — into structured victim profiles at scale, moving beyond raw data dumps to actionable intelligence packages.

> **Take**: AI-driven correlation inside malware means defenders can no longer assume that individually low-value stolen data points are low-risk — the dossier built from them is the real threat.

---

### 9. [AI Vulnerability Finding](https://www.schneier.com/blog/archives/2026/11/ai-vulnerability-finding-2.html)
**Source**: Schneier on Security

Cited analysis suggests AI-assisted vulnerability discovery has found 3% of all historically recorded critical software bugs within a single month, putting the tooling on pace to add approximately 26% to the all-time CVE total within a year.

> **Take**: Patch velocity is now the existential constraint — if vulnerability discovery is outrunning remediation capacity by this margin, enterprises without automated patch prioritization and backporting pipelines are structurally falling behind.

---

### 10. [Fuzzers vs. AI: Comparing Fuzzilli and BigSleep on JavaScript Engines](https://projectzero.google/2026/10/fuzzing-v-AI.html)
**Source**: Google Project Zero

Google Project Zero ran a six-month head-to-head between Fuzzilli (generative fuzzer) and BigSleep (LLM-based bug finder) against Chrome's V8 engine: BigSleep found 45 vulnerabilities to Fuzzilli's 37, with only 25% overlap — meaning the two approaches surface meaningfully different bug classes.

> **Take**: The non-overlapping findings are the story here — LLM-based and traditional fuzzing are complementary, not substitutes, and security teams treating AI bug-finding as a fuzzer replacement are leaving a significant slice of their attack surface uncovered.

---

*Outwire — signal over noise.*