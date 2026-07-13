## Outwire | AI Security Digest — Week of July 13, 2026
*Issue #14*

---

### 1. [New MemGhost Attack Plants Persistent False Memories in AI Agents Through One Email](https://thehackernews.com/2026/07/new-memghost-attack-plants-persistent.html)
**Source**: The Hacker News

A single malicious email can inject a false "fact" into an AI assistant's persistent memory, conceal the write operation from the user, and silently bias all future sessions — no exploit chain required, just inbox access and a memory-enabled agent. This is a direct attack on the trust model that makes AI assistants useful in enterprise settings: the assumption that what the agent "knows" reflects reality.

> **Take**: Any AI assistant deployment with persistent memory and email access should be treated as a target for context poisoning today — audit what your agents are writing to memory stores with the same scrutiny you'd apply to database writes.

---

### 2. [AI Gateways Offer Attackers the Keys to the Kingdom](https://www.darkreading.com/cyber-risk/ai-gateways-keys-kingdom)
**Source**: Dark Reading

A cryptomining incident exposed how AI gateways — the orchestration layer sitting between users and AI models — can hand attackers simultaneous access to model inference endpoints, cloud infrastructure, and IAM data in a single compromise. The blast radius of a gateway breach isn't just model abuse; it's a pivot point into your cloud environment.

> **Take**: AI gateways are becoming the new API management layer, and they're being deployed without the same threat modeling discipline — treat them like privileged infrastructure from day one.

---

### 3. [Someone Is Scanning for Your MCP Servers and AI Assistant Credentials](https://isc.sans.edu/diary/rss/33150)
**Source**: SANS ISC

Active reconnaissance campaigns are now targeting Model Context Protocol (MCP) servers and AI assistant credential endpoints, signaling that attackers have mapped the agent infrastructure stack and are probing it systematically. MCP servers, which broker tool and context access for AI agents, represent a new class of exposed attack surface that most organizations haven't inventoried yet.

> **Take**: If you've stood up MCP servers without putting them behind the same access controls as your other API infrastructure, assume they're already in someone's scan results.

---

### 4. [Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents](https://arxiv.org/abs/2607.09011)
**Source**: arXiv cs.CR

Researchers built an AI agent that goes beyond regex-based secret detection to extract credentials from fragmented, reformatted text in emails, tickets, and incident notes — and critically, also identifies the specific cloud resource, account, or database that each credential unlocks. The "what door does this key open" capability closes the gap that leaves incident responders guessing about blast radius during active breaches.

> **Take**: This is the tooling IR teams actually need, but the same capability in attacker hands makes credential exfiltration from unstructured data far more dangerous than traditional secret scanners suggest.

---

### 5. [AI Agents Are a New Kind of Identity — and Most Organizations Aren't Ready](https://www.darkreading.com/identity-access-management-security/ai-agents-new-kind-identity-most-organizations-not-ready)
**Source**: Dark Reading

AI agents acting autonomously on behalf of users don't fit cleanly into service account or API token identity models — they need dynamic, context-aware authorization that tracks intent and scope across multi-step workflows. Organizations treating agent identity as a static credential problem are leaving privilege escalation and lateral movement paths wide open.

> **Take**: I'd watch whether your IAM vendor actually ships agent-aware identity controls this year or just rebadges existing service account tooling — the gap between the two is where breaches will happen.

---

### 6. [Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents](https://arxiv.org/abs/2607.08906)
**Source**: arXiv cs.CR

Researchers propose that possession-based authorization models (tokens, credentials) are fundamentally insufficient for multi-step AI agent execution chains because they can't guarantee the causal relationship between a request's origin and the authority exercised at later steps. Proof-of-Continuity is a minimal discipline for encoding that causal chain, closing a gap that current agent frameworks leave entirely unaddressed.

> **Take**: This is the right framing for a problem most practitioners haven't articulated yet — if your agent orchestration relies solely on token possession to authorize downstream actions, you don't have an authorization model, you have a chain of assumptions.

---

### 7. [Lone Attacker Uses AI to Breach AWS Cloud Environment in 72 Hours](https://www.darkreading.com/cloud-security/lone-attacker-ai-breach-aws-cloud-environment)
**Source**: Dark Reading

A single threat actor leveraged AI-assisted workflows to chain cloud misconfigurations and stolen credentials into a full AWS environment compromise within 72 hours, ultimately extorting the victim. The speed is the signal: attack timelines that previously required a team and days of manual pivoting are now within reach of an individual operator using AI tooling.

> **Take**: The 72-hour window is a forcing function for detection — if your cloud threat detection isn't generating actionable alerts within hours of initial credential misuse, you're already behind the attacker's decision loop.

---

### 8. [SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills](https://arxiv.org/abs/2607.09016)
**Source**: arXiv cs.CR

Researchers introduce SkillLogic, a framework that analyzes logical dependencies — preconditions, constraints, fallback behaviors — across LLM agent skill files and surfaces cases where agents violate those relations in ways that could enable unsafe or unintended actions. Scanning 5,000+ skill definitions, they found systematic failure patterns that static testing misses entirely.

> **Take**: Agent skill files are becoming a new attack surface for logic abuse, and this work is the first systematic approach I've seen for auditing them — enterprise teams shipping agent workflows should be running this class of analysis before deployment.

---

### 9. ["Comment stuffing" in HTML phishing attachments as a mechanism for evading AI-based detection](https://isc.sans.edu/diary/rss/33144)
**Source**: SANS ISC

Attackers are injecting HTML comment noise into phishing attachments specifically to disrupt AI-based detection pipelines, exploiting the assumption that semantic analysis of rendered content will generalize to obfuscated markup. The technique is low-sophistication but effective against detection systems that don't pre-process or normalize HTML before analysis.

> **Take**: Adversarial evasion of AI security tooling is maturing faster than vendors are acknowledging — if your email security stack uses AI detection, ask your vendor directly how they handle pre-analysis normalization and whether they're testing against comment-stuffed samples.

---

### 10. [AI Found a Root Bug in Linux That Everyone Missed for 15 Years](https://www.wired.com/story/security-news-this-week-ai-found-a-root-bug-in-linux-that-everyone-missed-for-15-years/)
**Source**: WIRED Security

An AI system surfaced a privilege-escalation vulnerability in the Linux kernel that had been present and undetected for 15 years, underscoring both the capability of AI-assisted code auditing and the depth of the unreviewed attack surface sitting in production infrastructure. The finding is a proof point that AI vulnerability discovery is moving beyond synthetic benchmarks into real-world critical systems.

> **Take**: The uncomfortable implication isn't that AI found a bug — it's that well-resourced adversaries with the same tooling may have found it first and stayed quiet.

---

*Outwire — signal over noise.*