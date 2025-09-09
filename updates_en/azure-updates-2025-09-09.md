# September 09, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 09, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Operating System (OS) Disks on Standard HDD will be retired on 08 September 2028 

**Published**: September 08, 2025 21:00:36 UTC
**Link**: [Retirement: Operating System (OS) Disks on Standard HDD will be retired on 08 September 2028 ](https://azure.microsoft.com/updates?id=500157)

**Update ID**: 500157
**Data source**: Azure Updates API

**Categories**: Storage, Azure Disk Storage, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Operating System (OS) disks on Standard HDD storage in Azure, effective September 8, 2028.

- Key changes or new features  
After this date, OS disks using Standard HDD will no longer be supported. Customers are encouraged to migrate OS disks to other storage types, such as Standard SSD or Premium SSD, which offer better performance and reliability. This change aligns with evolving usage patterns and Azure’s focus on investing in higher-performance disk options.

- Target audience affected  
Developers and IT professionals managing Azure virtual machines with OS disks on Standard HDD storage will be impacted. This includes those responsible for VM provisioning, disk management, and performance optimization.

- Important notes if any  
Plan and execute migration well before the retirement date to avoid service disruptions. Review existing VM disk configurations and update deployment templates or automation scripts accordingly. Consider performance and cost implications when selecting alternative disk types. For detailed guidance, refer to Azure documentation and migration best practices.

**Details**:

The announced retirement of Operating System (OS) Disks on Standard HDD in Azure, effective September 8, 2028, reflects Microsoft’s strategic initiative to optimize disk performance and align its storage offerings with modern workload requirements and customer usage trends. This update signifies the planned deprecation of OS disks provisioned on Standard HDD managed disks, encouraging migration towards higher-performance storage options such as Standard SSD or Premium SSD.

**Background and Purpose**  
Standard HDD managed disks have traditionally served as a cost-effective storage tier for less performance-sensitive workloads. However, evolving application demands and the increasing need for improved I/O throughput, latency, and reliability have shifted the preference towards SSD-backed disks. Microsoft’s decision to retire OS disks on Standard HDD aims to streamline the disk portfolio, reduce maintenance overhead, and focus investments on storage tiers that deliver better performance and scalability, thereby enhancing overall customer experience.

**Specific Features and Detailed Changes**  
- **Retirement Date:** September 8, 2028, marks the cutoff for creating or maintaining OS disks on Standard HDD.  
- **Scope:** Applies exclusively to OS disks; data disks on Standard HDD are not explicitly mentioned and may continue to be supported.  
- **Migration Path:** Customers will need to migrate existing OS disks from Standard HDD to supported tiers such as Standard SSD or Premium SSD before the retirement date.  
- **Creation Restrictions:** Post-retirement, creation of new OS disks on Standard HDD will be disabled.

**Technical Mechanisms and Implementation Methods**  
- **Disk Migration:** Azure supports disk migration through snapshot and disk copy operations or by leveraging Azure Site Recovery and Azure Backup to facilitate OS disk upgrades.  
- **Disk Conversion:** Customers can create a snapshot of the existing Standard HDD OS disk and then create a new managed disk from that snapshot on a supported tier (e.g., Standard SSD). The VM can then be reattached to the new disk.  
- **Automation:** PowerShell, Azure CLI, and ARM templates can be used to automate the migration process at scale.  
- **Monitoring:** Azure Monitor and Azure Advisor may provide insights and recommendations to identify OS disks on Standard HDD and track migration progress.

**Use Cases and Application Scenarios**  
- **Legacy Workloads:** Applications currently running on VMs with OS disks on Standard HDD, especially development or test environments, will need to plan migration to avoid disruption.  
- **Cost-Performance Optimization:** Customers balancing cost and performance can transition to Standard SSD, which offers a good middle ground, or Premium SSD for high I/O workloads.  
- **Compliance and Security:** Ensuring OS disks are on supported tiers aligns with Azure’s security and compliance best practices, as newer disk types receive ongoing feature updates and patches.

**Important Considerations and Limitations**  
- **Migration Planning:** Migration requires downtime or VM redeployment; hence, scheduling during maintenance windows is critical.  
- **Cost Implications:** Upgrading to SSD tiers may increase storage costs; customers should analyze workload requirements to select appropriate tiers.  
- **Backup and Recovery:** Prior to migration, ensure backups are current to prevent data loss.  
- **Unsupported Scenarios:** Some legacy VM sizes or configurations may have compatibility constraints with newer disk types, necessitating VM resizing or reconfiguration.

**Integration with Related Azure Services**  
- **Azure Backup:** Supports backup and restore operations for managed disks across all tiers, facilitating safe migration.  
- **Azure Site Recovery:** Can be used to replicate and failover VMs to upgraded disk tiers with minimal downtime.  
- **Azure Monitor & Azure Advisor:** Provide telemetry and recommendations to identify Standard HDD OS disks and optimize migration strategies.  
- **Azure Policy:** Organizations can enforce policies to prevent creation of OS disks on deprecated tiers post-retirement.

In summary, the retirement of OS disks on Standard HDD by September 8, 2028, requires IT professionals to proactively assess and migrate existing VMs to supported disk tiers to maintain performance, reliability, and supportability

---

### 2. Public Preview: Graph Query Language (GQL) in KQL graph semantics

**Published**: September 08, 2025 12:00:02 UTC
**Link**: [Public Preview: Graph Query Language (GQL) in KQL graph semantics](https://azure.microsoft.com/updates?id=502638)

**Update ID**: 502638
**Data source**: Azure Updates API

**Categories**: In preview, Analytics, Azure Data Explorer, Microsoft Fabric, Features

**Summary**:

- What was updated  
Azure has introduced public preview support for Graph Query Language (GQL) within Kusto Query Language (KQL) graph semantics, aligning with the ISO standard for graph querying.

- Key changes or new features  
Developers and IT professionals can now execute GQL queries directly on graph data stored in Fabric Eventhouse and Azure Data Explorer. This integration simplifies querying complex graph structures by leveraging a standardized, widely recognized graph query language. It enhances interoperability and provides a more intuitive syntax for graph data exploration and analysis within Azure’s data services.

- Target audience affected  
This update primarily benefits developers, data engineers, and IT professionals working with graph data in Azure Data Explorer or Fabric Eventhouse who require advanced graph querying capabilities. It is especially relevant for those building graph-based applications, performing network analysis, or managing connected data sets.

- Important notes if any  
The feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. As it aligns with the ISO GQL standard, it may influence future graph query implementations and tooling within Azure. Users should review documentation for syntax differences and integration details before adoption.

For more details, visit: https://azure.microsoft.com/updates?id=502638

**Details**:

The recent Azure update introduces public preview support for Graph Query Language (GQL) within Kusto Query Language (KQL) graph semantics, aligning with the ISO/IEC 39075:2021 standard for graph query languages. This enhancement enables IT professionals and data engineers to execute standardized GQL queries directly on graph data stored in Azure Data Explorer and Fabric Eventhouse, streamlining graph data analysis and interoperability.

**Background and Purpose**  
Graph data models are increasingly critical for representing complex relationships in domains such as social networks, fraud detection, knowledge graphs, and IoT. While Azure Data Explorer (ADX) has long supported graph semantics through KQL extensions, the lack of a standardized graph query language limited cross-platform compatibility and adoption. GQL, recently standardized by ISO, offers a vendor-neutral, declarative language for graph querying. By integrating GQL support into KQL graph semantics, Azure aims to provide users with a familiar, industry-standard syntax to query graph data, thereby enhancing usability, portability, and integration with other graph systems.

**Specific Features and Detailed Changes**  
- **GQL Query Support:** Users can now write queries using GQL syntax within the KQL environment, enabling graph pattern matching, traversal, and manipulation consistent with the ISO standard.  
- **Seamless Execution on Azure Data Explorer and Fabric Eventhouse:** The update allows GQL queries to run natively on graph data stored in these services without requiring data transformation or export.  
- **Interoperability:** This feature bridges the gap between KQL’s proprietary graph extensions and the standardized GQL, facilitating easier migration and integration with other graph databases and tools supporting GQL.  
- **Syntax and Semantics Alignment:** The implementation ensures that GQL constructs such as MATCH, PATH, and graph pattern expressions are supported, mapped to underlying KQL graph operators and data structures.

**Technical Mechanisms and Implementation Methods**  
Under the hood, the Azure Data Explorer engine extends its query parser and execution layer to recognize and interpret GQL syntax. The GQL queries are translated into equivalent KQL graph operations, leveraging ADX’s optimized graph processing capabilities. This translation layer ensures that the declarative GQL patterns are efficiently executed using ADX’s columnar storage and indexing mechanisms. The integration with Fabric Eventhouse allows streaming event data to be queried in graph form using GQL, enabling near real-time graph analytics.

**Use Cases and Application Scenarios**  
- **Social Network Analysis:** Querying relationships and community structures using standardized graph patterns.  
- **Fraud Detection:** Detecting suspicious transaction paths or anomalous connections in financial data.  
- **Knowledge Graph Exploration:** Navigating complex entity relationships in enterprise knowledge bases.  
- **IoT and Telemetry:** Analyzing device communication graphs and event flows in real time.  
- **Cross-Platform Graph Analytics:** Facilitating migration or integration of graph workloads between Azure and other GQL-compliant graph databases.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, users should expect potential limitations in scalability, performance optimizations, and feature completeness. Production use should be approached cautiously.  
- **Feature Parity:** Not all GQL features may be fully supported initially; users should consult the official documentation for supported syntax and functions.  
- **Learning Curve:** While GQL is standardized, users familiar only with KQL may require training to leverage GQL effectively.  
- **Resource Consumption:** Complex graph queries can be resource-intensive; proper query tuning and resource management are advised.

**Integration with Related Azure Services**  
- **Azure Data Explorer:** Native support for GQL queries on graph data stored in ADX clusters, benefiting from its high-performance analytics engine.  
- **Fabric Eventhouse:** Enables streaming event data ingestion and real-time graph querying using GQL, supporting event-driven architectures.  
- **Azure Synapse Analytics:** Potential future integration for unified analytics combining relational and graph data.

---


*This report was automatically generated - 2025-09-09 03:01:42 UTC*