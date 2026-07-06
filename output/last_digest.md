## Outwire | AI Security Digest — Week of July 06, 2026
*Issue #13*

---

### 1. [SkillCloak Lets Malicious AI Agent Skills Evade Static Scanners with Self-Extracting Packing](https://thehackernews.com/2026/07/new-skillcloak-technique-lets-malicious.html)
**Source**: The Hacker News

Researchers at HKUST demonstrated that malicious skills for AI coding agents can evade every static scanner tested more than 90% of the time using self-extracting packing techniques — the same evasion playbook that plagued traditional AV for years, now landing squarely in the AI agent plugin ecosystem. The same team also built a runtime checker that recovers much of the detection gap, suggesting the defense exists but isn't deployed.

> **Take**: The 90%+ bypass rate means any enterprise running AI coding agents with third-party skill marketplaces should treat those skills as untrusted executables and demand runtime behavioral analysis, not just scan-on-install.

---

### 2. [Fake Bug Report Hijacks AI Coding Agents at Scale](https://www.darkreading.com/cyber-risk/fake-bug-report-hijacks-ai-coding-agents)
**Source**: Dark Reading

"Agentjacking" uses crafted fake bug reports as the injection vector to hijack AI coding agents, exploiting the agent's inability to distinguish between data content and executable instructions — effectively turning your issue tracker into a command-and-control channel. At scale, this means any agent triaging GitHub issues or Jira tickets is a lateral movement surface.

> **Take**: I'd treat every external content source an agent reads — issues, PRs, emails, docs — as a potential injection vector and architect explicit trust boundaries between the agent's instruction plane and its data plane before this becomes a breach postmortem item.

---

### 3. [Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)
**Source**: Microsoft Security

MCP tool poisoning attacks manipulate tool descriptions to redirect trusted AI agents into unauthorized data exfiltration or destructive actions, effectively hijacking the agent's control plane through its own configuration layer. Microsoft's writeup covers detection signals, containment approaches, and prevention controls with enterprise deployment context.

> **Take**: MCP tool descriptions are becoming the new `sudoers` file — if you're not treating them as security-critical configuration with change control and integrity verification, you're leaving an obvious escalation path unguarded.

---

### 4. ['Phantom Squatting': An Emerging AI-Driven Supply Chain Threat](https://www.darkreading.com/endpoint-security/phantom-squatting-ai-driven-supply-chain-threat)
**Source**: Dark Reading

LLMs consistently hallucinate plausible-but-nonexistent web domains for legitimate brands, and attackers can pre-register those hallucinated domains to intercept traffic from users or agents that act on the model's output. The attack is difficult to detect because the domains look credible and the hallucination behavior is deterministic enough to be weaponized predictably.

> **Take**: This is the supply chain threat that scales passively — attackers don't need to compromise anything, just enumerate what popular LLMs hallucinate and register ahead of the curve, which makes this a monitoring problem as much as a model problem.

---

### 5. [Claude Helped a Hacker Find a Way to Issue Tickets to Almost Every US Music Festival](https://www.wired.com/story/claude-helped-a-hacker-find-a-way-to-issue-tickets-to-almost-every-us-music-festival/)
**Source**: WIRED Security

A security researcher used Claude Opus 4.7 to discover and exploit a critical vulnerability in Front Gate Tickets — the backend platform powering Lollapalooza, Bonnaroo, and hundreds of other US festivals — enabling arbitrary ticket issuance with no payment. This is a concrete, documented case of an advanced LLM dramatically compressing the time-to-exploit for a significant real-world vulnerability.

> **Take**: The story isn't that Claude broke something — it's that AI-assisted exploitation now makes a solo researcher equivalent to a well-resourced team, and your threat model for critical business applications needs to account for that capability shift today.

---

### 6. [Attackers Seize Exposed AI Endpoints to Power Offensive Ops](https://www.darkreading.com/cloud-security/attackers-hijack-exposed-ai-endpoints-power-offensive-ops)
**Source**: Dark Reading

Threat actors are actively scanning for and exploiting unauthenticated AI inference endpoints — no credential theft required, just endpoint discovery — and repurposing that compute for offensive operations including malware generation and automated attack tooling. The barrier to entry is essentially a port scan.

> **Take**: Exposed AI endpoints are the new exposed Elasticsearch instance — a recon problem masquerading as a configuration oversight, and you should be running continuous discovery against your own infrastructure before attackers do it for you.

---

### 7. [Better Models: Worse Tools](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything)
**Source**: Simon Willison

Claude Opus 4.8 — a frontier model — is observed hallucinating extra, invented fields in tool call schemas, causing agentic workflows to fail or loop when the downstream tool rejects the malformed invocation. The finding challenges the assumption that more capable models produce more reliable, schema-compliant outputs in structured agentic contexts.

> **Take**: Schema hallucination in tool calls is a latent reliability and security issue for any agent that fails open — if your tool handler retries on schema mismatch rather than failing hard, you've created a behavior manipulation surface that gets worse as models get more "creative."

---

### 8. [Anthropic's AI Finds Bugs. IBM Bets $5B It Can Fix Them.](https://www.darkreading.com/vulnerabilities-threats/anthropic-s-ai-finds-bugs-ibm-bets-5b-it-can-fix-them-)
**Source**: Dark Reading

Anthropic's Mythos AI system is actively discovering vulnerabilities in open-source software, and IBM is committing $5B and 20,000 engineers through Project Lightwell to operationalize AI-driven remediation at scale across the OSS supply chain. The initiative surfaces a structural tension: AI can now find bugs faster than the ecosystem can patch them.

> **Take**: The real risk isn't that AI finds bugs slowly — it's the window between AI-discovered vulnerability and human-applied patch, which becomes a known-unknown that sophisticated attackers will race to exploit.

---

### 9. [GPT-5.5-Cyber built a zlib fuzzing lab in a day](https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/)
**Source**: Trail of Bits

Trail of Bits and OpenAI's Patch the Planet collaboration is deploying GPT-5.5-Cyber against real open-source codebases, with the model standing up a complete zlib fuzzing harness in a single day — a task that previously required significant engineer-hours. The stated goal is to front-run the coming flood of AI-generated bug reports before OSS maintainers are overwhelmed.

> **Take**: When a model can instrument and fuzz a production library in a day, the asymmetry between AI-assisted offense and human-paced defense in OSS maintenance becomes an infrastructure-level risk — the maintainer burnout problem and the vulnerability discovery problem are now the same problem.

---

### 10. [North Korea-Linked npm Packages Mimic Rollup Polyfills to Steal Developer Secrets](https://thehackernews.com/2026/07/north-korea-linked-npm-packages-mimic-)
**Source**: The Hacker News

DPRK-affiliated threat actors published `rollup-packages-polyfill-core` and `rollup-runtime-polyfill-core` to npm, cloning the metadata, description, and repository structure of the legitimate `rollup-plugin-polyfill-node` to facilitate remote access and credential theft from developer environments. The targeting of build tooling is deliberate — developer machines are the highest-privilege entry point into most software supply chains.

> **Take**: Nation-state actors are now consistently targeting the developer toolchain specifically because it's the unmonitored path to production — any AI or security tooling your engineers are building with deserves the same dependency scrutiny you apply to production services.

---

*Outwire — signal over noise.*