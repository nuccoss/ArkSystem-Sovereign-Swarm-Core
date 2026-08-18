# 4-Tier SSoT Architecture

ArkSystem maintains data equivalence across 4 physical tiers:
- **Tier 1 (Local Storage)**: High-speed developer scratchpad & air-gapped confidential vault.
- **Tier 2 (Google Drive)**: Desktop file streaming & office suite collaboration.
- **Tier 3 (Google Cloud Storage)**: Multi-region authoritative object storage & Eventarc hub.
- **Tier 4 (BigQuery)**: Enterprise analytics, historical chronicle aggregation & semantic search.
