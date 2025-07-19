# July 19, 2025 - Azure Updates Summary Report

**Generated on**: July 19, 2025
**Target period**: Within the last 24 hours
**Number of updates**: 1 items

## Update List

### 1. [Launched] Generally Available:  Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging

**Published**: July 18, 2025 16:45:08 UTC
**Link**: [[Launched] Generally Available:  Azure Firewall now supports ingestion-time transformation in Log Analytics for flexible, cost-efficient logging](https://azure.microsoft.com/updates?id=498568)

**Categories**: Launched, Networking, Security, Azure Firewall, Features, Services

**Summary**:

- What was updated  
Azure Firewall now supports ingestion-time transformation of logs within Azure Monitor Log Analytics.

- Key changes or new features  
This update enables selective logging and advanced filtering of firewall logs at ingestion time. Customers can define transformation rules to filter, modify, or drop log records before they are stored in Log Analytics. This reduces the volume of ingested data, optimizing both ingestion and storage costs. The feature improves log management flexibility by allowing tailored data collection aligned with specific monitoring and compliance needs.

- Target audience affected  
Developers, IT professionals, and security operations teams who use Azure Firewall and rely on Log Analytics for security monitoring, troubleshooting, and auditing will benefit from this feature. It is especially relevant for organizations aiming to optimize log data costs and improve log query performance.

- Important notes if any  
This capability is now generally available and can be configured through Azure Monitor’s ingestion-time transformation rules. Users should carefully design transformation policies to ensure critical security events are not inadvertently filtered out. This enhancement complements existing post-ingestion query and alerting capabilities, providing a more cost-efficient and scalable logging solution for Azure Firewall.

**Details**:

Azure Firewall now supports ingestion-time
transformation of logs in Log Analytics, enabling
selective logging and advanced filtering. Why it matters:
For customers using Log Analytics to analyse firewall logs, the cost of log
ingestion and storage itself

---


*This report was automatically generated - 2025-07-19 06:19:35 UTC*