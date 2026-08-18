# SASS v5.0: Sovereign Agent Swarm Specification

## 1. Governance Laws
1. **`LAW-FBL-RESPONSE-COMPLETION`**: A task is declared 100% completed ONLY when the recipient agent emits a valid FBL ACK packet.
2. **`LAW-TASK-BOARD-EVERY-QUERY-GOVERNANCE`**: Every active turn MUST render a structured Task Board reflecting live state.
3. **`LAW-HERITAGE-AUTONOMOUS-UPDATE`**: Thread migrations MUST autonomously update 5-Tier long-term memory (`01_heritage/`).

## 2. Directory Architecture (FTA)
All agents strictly follow 1-digit sub-slots under standardized 2-digit prefixes (`01_heritage`, `15_plans`, `16_goals`, `18_tasks`, `25_log`, `31_feedback_loop`).
