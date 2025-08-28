# August 28, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 28, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: Azure SQL updates for late-August 2025 

**Published**: August 27, 2025 16:00:53 UTC
**Link**: [Public Preview: Azure SQL updates for late-August 2025 ](https://azure.microsoft.com/updates?id=500780)

**Update ID**: 500780
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Azure SQL Database introduced a new replication lag metric during its late-August 2025 public preview update.

- Key changes or new features  
The replication lag metric provides real-time visibility into the recovery point objective (RPO) when Geo-Disaster Recovery (Geo-DR) is enabled. This enhancement allows users to monitor how current the secondary replicas are relative to the primary database, improving transparency and aiding in disaster recovery planning and validation.

- Target audience affected  
This update primarily benefits developers and IT professionals managing Azure SQL Database instances with Geo-DR configurations, including database administrators responsible for high availability and disaster recovery strategies.

- Important notes if any  
The feature is currently in public preview, so users should test it in non-production environments before full adoption. Monitoring replication lag can help optimize failover readiness and ensure compliance with recovery objectives. For more details and implementation guidance, refer to the official Azure update page.

**Details**:

The late-August 2025 public preview update for Azure SQL Database introduces a new replication lag metric designed to enhance monitoring and management of Geo-Distributed Replication (Geo-DR) scenarios by providing real-time visibility into the recovery point objective (RPO). This update addresses a critical need for database administrators and IT professionals to precisely track data synchronization latency between primary and secondary replicas in geo-replicated environments, thereby improving disaster recovery readiness and operational decision-making.

**Background and Purpose:**  
Geo-DR in Azure SQL Database enables high availability and disaster recovery by replicating data asynchronously from a primary database to one or more secondary databases located in different geographic regions. While this replication ensures data durability and availability, asynchronous replication inherently involves some lag, which impacts the RPO—the maximum acceptable amount of data loss measured in time. Prior to this update, customers had limited visibility into the exact replication lag, making it challenging to assess real-time data currency on secondary replicas and to validate compliance with RPO objectives. The introduction of a replication lag metric aims to fill this gap by offering precise, real-time measurement of replication latency.

**Specific Features and Detailed Changes:**  
- **Replication Lag Metric:** Azure SQL Database now exposes a metric that quantifies the delay between the primary and secondary replicas in terms of time, reflecting how far behind the secondary is in applying transaction log records.  
- **Real-Time Monitoring:** This metric is available in near real-time, enabling continuous monitoring rather than relying on periodic or indirect indicators.  
- **Integration with Azure Monitor:** The replication lag metric can be ingested into Azure Monitor, allowing users to create alerts, dashboards, and automated responses based on replication lag thresholds.  
- **API and Portal Access:** The metric is accessible via Azure Portal, REST APIs, and CLI tools, facilitating integration into existing monitoring workflows and automation scripts.

**Technical Mechanisms and Implementation Methods:**  
The replication lag metric is derived from internal transaction log synchronization timestamps between the primary and secondary databases. Azure SQL Database tracks the last committed transaction time on the primary and compares it with the last applied transaction time on the secondary replica. The difference represents the replication lag. This metric is surfaced through the Azure Resource Manager (ARM) metrics pipeline and exposed as a first-class metric under the Azure SQL Database resource namespace. The underlying telemetry is collected with minimal performance overhead, ensuring that monitoring does not impact database throughput or latency.

**Use Cases and Application Scenarios:**  
- **Disaster Recovery Validation:** DBAs can verify that the secondary replica is within the defined RPO limits, ensuring that failover will not result in unacceptable data loss.  
- **Operational Alerting:** Automated alerts can be configured to notify teams when replication lag exceeds thresholds, prompting investigation or failover readiness.  
- **Capacity Planning and Performance Tuning:** Understanding replication lag trends helps optimize workload distribution and network configurations to minimize lag.  
- **Compliance and Reporting:** Organizations with strict data protection requirements can document real-time RPO adherence as part of audit and compliance processes.

**Important Considerations and Limitations:**  
- The replication lag metric is currently in public preview, which means it may be subject to changes and should not be used as the sole basis for critical production decisions without validation.  
- Asynchronous replication lag can fluctuate due to network conditions, workload spikes, or maintenance activities; thus, transient spikes should be interpreted with caution.  
- The metric applies only to Azure SQL Databases configured with Geo-DR; it is not relevant for single-region or synchronous replication scenarios.  
- Integration with third-party monitoring tools requires custom ingestion of Azure Monitor metrics or use of APIs.

**Integration with Related Azure Services:**  
- **Azure Monitor:** Enables collection, visualization, and alerting on replication lag metrics, supporting proactive operational management.  
- **Azure Automation and Logic Apps:** Can leverage metric alerts to trigger automated remediation workflows or notifications.  
- **Azure Resource Manager:** Provides programmatic access to the metric for integration into infrastructure

---

### 2. Generally Available: Schema migration is now available in Azure Database Migration Service (DMS) 

**Published**: August 27, 2025 16:00:53 UTC
**Link**: [Generally Available: Schema migration is now available in Azure Database Migration Service (DMS) ](https://azure.microsoft.com/updates?id=500770)

**Update ID**: 500770
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Migration, Azure Database Migration Service, Features

**Summary**:

- What was updated  
Azure Database Migration Service (DMS) now generally supports schema migration for Azure SQL Database.

- Key changes or new features  
Developers and IT professionals can migrate missing schema objects alongside data by simply enabling a new checkbox option in DMS. This enhancement streamlines the migration process by combining schema and data migration into a single operation, reducing manual steps and potential errors.

- Target audience affected  
Database administrators, developers, and IT professionals involved in migrating on-premises or other cloud databases to Azure SQL Database.

- Important notes if any  
This feature improves migration efficiency and reliability but users should still validate schema compatibility and test migrated databases post-migration. The update is generally available, indicating production readiness and full Microsoft support.

For more details, visit: https://azure.microsoft.com/updates?id=500770

**Details**:

The recent general availability of schema migration in Azure Database Migration Service (DMS) significantly enhances the service’s capability by enabling automated migration of database schema objects alongside data when migrating to Azure SQL Database. This update addresses a longstanding challenge in database migration workflows, where schema and data migrations were often handled separately, increasing complexity, risk, and manual effort.

**Background and Purpose**  
Traditionally, migrating databases to Azure SQL Database required separate steps for schema and data migration. Customers had to manually generate and apply schema scripts or use third-party tools to replicate schema objects before migrating data. This fragmented approach could lead to inconsistencies, longer migration windows, and increased potential for errors. The purpose of this update is to streamline the migration process by integrating schema migration directly into Azure DMS, thereby simplifying the migration workflow and reducing operational overhead.

**Specific Features and Detailed Changes**  
With this update, Azure DMS now supports migrating missing schema objects such as tables, indexes, constraints, stored procedures, views, and functions automatically during the migration process. Users can enable this feature by selecting a single checkbox in the migration project configuration, which instructs DMS to detect and create any schema objects absent in the target Azure SQL Database before or during data migration. This ensures schema consistency and integrity without requiring separate schema deployment steps.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure DMS performs a schema comparison between the source database and the target Azure SQL Database. It identifies schema objects that exist on the source but are missing or different on the target. Using this metadata, DMS generates the necessary Data Definition Language (DDL) scripts to create or alter schema objects in the target environment. These scripts are executed as part of the migration workflow, ensuring the target schema aligns with the source before data is migrated. This process leverages Azure DMS’s existing connectivity and orchestration capabilities, supporting both online and offline migration modes.

**Use Cases and Application Scenarios**  
This feature is particularly beneficial for enterprises migrating on-premises SQL Server databases or other supported sources to Azure SQL Database, where schema drift or incomplete schema deployment can cause migration failures or data inconsistencies. It is ideal for lift-and-shift migrations, modernization projects, and hybrid cloud scenarios where minimizing downtime and manual intervention is critical. Additionally, it supports complex database environments with multiple schema objects, enabling smoother transitions to managed Azure SQL Database services.

**Important Considerations and Limitations**  
While schema migration automation simplifies the process, users should be aware of certain limitations. Complex schema elements such as cross-database references, certain types of triggers, or unsupported features in Azure SQL Database may require manual intervention or post-migration adjustments. It is recommended to review the generated schema scripts and perform thorough testing in a non-production environment prior to cutover. Additionally, schema migration currently supports Azure SQL Database targets; migrating to other targets like Azure SQL Managed Instance may have different considerations.

**Integration with Related Azure Services**  
This update complements other Azure migration and management tools such as Azure Data Factory for data orchestration, Azure Monitor for migration monitoring, and Azure DevOps for CI/CD pipeline integration. It also aligns with Azure SQL Database’s built-in features like automatic tuning and performance monitoring, enabling a more seamless post-migration operational experience. By consolidating schema and data migration within Azure DMS, organizations can leverage a unified, Azure-native migration strategy that reduces complexity and accelerates cloud adoption.

In summary, the general availability of schema migration in Azure Database Migration Service represents a significant advancement in simplifying and automating database migrations to Azure SQL Database, improving reliability, reducing manual effort, and enabling faster cloud modernization initiatives.

---

### 3. Public Preview: Azure Cosmos DB for MongoDB (vCore)—add shards and rebalance data 

**Published**: August 27, 2025 16:00:53 UTC
**Link**: [Public Preview: Azure Cosmos DB for MongoDB (vCore)—add shards and rebalance data ](https://azure.microsoft.com/updates?id=500755)

**Update ID**: 500755
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Azure Cosmos DB for MongoDB (vCore) now supports adding physical shards and rebalancing data within clusters during scale-out operations.

- Key changes or new features  
Developers and IT professionals can dynamically add physical shards (nodes) to their Cosmos DB for MongoDB (vCore) clusters as workload demands increase. This enables seamless scaling of both compute and storage resources. The update leverages the inherent elasticity of Cosmos DB, allowing clusters to grow without downtime. Additionally, data rebalancing across shards ensures optimal distribution and performance as shards are added.

- Target audience affected  
This update primarily benefits developers and database administrators managing large or growing MongoDB workloads on Azure Cosmos DB who require scalable, high-performance, and flexible cluster configurations.

- Important notes if any  
The feature is currently in public preview, so users should evaluate it in non-production environments before full adoption. Proper monitoring and management of shard rebalancing are recommended to maintain performance during scaling operations.  

For more details, visit: https://azure.microsoft.com/updates?id=500755

**Details**:

The recent public preview update for Azure Cosmos DB for MongoDB (vCore) introduces the capability to add physical shards and rebalance data dynamically as clusters scale, enhancing the service’s elasticity and performance for large-scale, distributed MongoDB workloads.

**Background and Purpose**  
Azure Cosmos DB for MongoDB (vCore) is a managed database service that offers MongoDB API compatibility on the Azure Cosmos DB platform, combining MongoDB’s developer ecosystem with Cosmos DB’s global distribution, low latency, and scalability. Previously, scaling was constrained by fixed shard counts, limiting flexibility in handling growing data volumes and throughput demands. This update addresses these limitations by enabling dynamic shard addition and data rebalancing, thereby supporting seamless horizontal scaling and improved resource utilization as workloads evolve.

**Specific Features and Detailed Changes**  
- **Add Physical Shards:** Users can now increase the number of physical shards (nodes) in their Cosmos DB for MongoDB (vCore) clusters without downtime. This allows the cluster to distribute data and workload more evenly across additional shards, improving performance and capacity.  
- **Data Rebalancing:** When new shards are added, the system automatically redistributes data across all shards to maintain balanced storage and throughput utilization. This rebalancing process is transparent to applications and ensures optimal resource usage.  
- **Elastic Compute and Storage:** Leveraging Cosmos DB’s decoupled compute and storage architecture, each shard can independently scale compute resources, enabling fine-grained performance tuning per shard.  
- **Operational Simplicity:** The shard addition and rebalancing operations are integrated into the Azure portal and APIs, providing straightforward management and automation capabilities.

**Technical Mechanisms and Implementation Methods**  
Under the hood, the update leverages Cosmos DB’s distributed architecture and partitioning model. Each physical shard corresponds to a set of logical partitions managed by the Cosmos DB partition key. When a new shard is added, the system recalculates partition-to-shard mappings and migrates partition data asynchronously to the new shard nodes. This migration uses internal data movement protocols optimized for minimal impact on availability and latency. The vCore-based billing model allows independent scaling of compute resources per shard, enabling cost-effective resource allocation aligned with workload demands.

**Use Cases and Application Scenarios**  
- **Scaling Large MongoDB Workloads:** Applications experiencing growth in data size or throughput can add shards dynamically to maintain performance without downtime.  
- **Multi-tenant SaaS Platforms:** SaaS providers can isolate tenant data across shards and add shards as tenant count or workload increases.  
- **Real-time Analytics and IoT:** Workloads with variable ingestion rates and data volumes benefit from elastic shard scaling to handle spikes efficiently.  
- **Geographically Distributed Applications:** Combined with Cosmos DB’s global distribution, shard scaling supports regional workload balancing and disaster recovery.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it may have limitations or changes before general availability; production use should be carefully evaluated.  
- **Shard Count Limits:** There may be maximum shard counts per cluster based on the current preview constraints; users should consult documentation for exact limits.  
- **Rebalancing Impact:** Although designed to minimize disruption, data rebalancing can temporarily increase resource consumption and latency; planning shard additions during low-traffic periods is advisable.  
- **Compatibility:** Existing applications using MongoDB drivers should verify compatibility with dynamic shard topology changes, especially if relying on shard-specific configurations.

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Metrics:** Integration enables monitoring shard performance, resource utilization, and rebalancing operations for proactive management.  
- **Azure Automation and Azure CLI:** Support for scripting shard addition and management facilitates DevOps workflows and infrastructure-as-code practices.  
- **Azure Virtual Network (VNet) and Security:** Shards can be deployed within VNets for enhanced security and compliance.  
- **Azure Backup and Azure Site Recovery:** Data protection strategies can be aligned with

---


*This report was automatically generated - 2025-08-28 03:02:05 UTC*