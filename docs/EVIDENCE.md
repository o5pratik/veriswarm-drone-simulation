# Evidence boundaries and review scope

## What supports this portfolio

- The original contribution branch and commits linked in CONTRIBUTIONS.md.
- A committed historical nominal-v1 PASS report with route, error, separation and landing measurements.
- Local SIH conversations describing implementation, debugging, screenshots and handoffs.

The portfolio review covered the current **After A to B simulation** conversation and seven other SIH project chats: **Fix drone underwater movement**, **Analyze VeriSwarm drone simulation**, **Review tomorrow handoff plan**, **Add adversarial patch setup**, **Create hackathon project plan**, **Create Hackathon project plan**, and **IG Algo**. IG Algo was unrelated and excluded from technical attribution. Private transcripts are not published.

## Historical success is not the latest scratch state

The mutable `latest/` development outputs were overwritten. At review time, an A → B output recorded rooftop-contact timeout, and a movement-v2 output recorded stale startup authorization with no control-loop progress. Those files must not be substituted for the earlier PASS report. The nominal metrics here are explicitly **reported historical measurements**, not independently remeasured today.

The team status also reported 58 focused post-merge tests at the nominal milestone and 82 focused tests at a movement-v2 milestone. These are historical counts, not this repository's test count.

## Not claimed

- Retained live acceptance of every HOLD, QUARANTINE, obstacle-deflection or task-reassignment scenario.
- Five-drone 3-D survivor localization, GPS-denied SLAM, validated thermal sensing, or physical-drone deployment.
- Authorship of teammates' inference, dashboard or security systems.
- Adversarial-proof, tamper-proof or unhackable behavior.

A rooftop character and debris are scene fixtures, not evidence of AI detection. The standalone Python example uses synthetic inputs and demonstrates selected control invariants only.
