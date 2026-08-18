# SASS v5.0: Sovereign Agent Swarm Specification

## 1. Governance Laws
1. **`LAW-FBL-COMPLETION-PROTOCOL`**: A task is declared 100% completed ONLY when the recipient agent emits a valid FBL ACK packet.
2. **`LAW-TASK-BOARD-GOVERNANCE`**: Every active turn MUST render a structured Task Board reflecting live state.
3. **`LAW-HERITAGE-MEMORY-UPDATE`**: Thread migrations MUST autonomously update long-term memory (`heritage/`).

## 2. Directory Architecture
All agents strictly follow structured sub-slots under standardized prefixes (`heritage`, `plans`, `goals`, `tasks`, `logs`, `feedback_loop`).
