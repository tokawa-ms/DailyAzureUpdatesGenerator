# April 23, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 23, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Public Preview: Azure Arc adds SQL Server on Azure Virtual Machines as a migration target 

**Published**: April 22, 2026 20:45:32 UTC
**Link**: [Public Preview: Azure Arc adds SQL Server on Azure Virtual Machines as a migration target ](https://azure.microsoft.com/updates?id=560805)

**Update ID**: 560805
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Azure Arc, Features

**Summary**:

- What was updated  
Azure Arc migration now supports SQL Server on Azure Virtual Machines (VMs) as a migration target in public preview.

- Key changes or new features  
Previously, Azure Arc-enabled SQL Server instances could only be migrated to Azure SQL Managed Instance. With this update, you can now migrate Arc-enabled SQL Server instances directly to SQL Server running on Azure Virtual Machines. The migration process uses the same unified Azure Arc migration experience, streamlining and simplifying migrations to both Platform as a Service (PaaS) and Infrastructure as a Service (IaaS) targets.

- Target audience affected  
This update is relevant for database administrators, IT professionals, and developers managing SQL Server workloads who are planning migrations to Azure. Organizations with hybrid or multi-cloud environments using Azure Arc-enabled SQL Server will benefit most.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. Users should validate compatibility and review documentation for any limitations or prerequisites. The unified migration experience helps reduce complexity and downtime during migrations, offering greater flexibility in choosing between Azure SQL Managed Instance and SQL Server on Azure VMs as migration targets.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=560805

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Azure Arc adds SQL Server on Azure Virtual Machines as a migration target

**Background and Purpose of the Update:**  
Previously, Azure Arc-enabled SQL Server migration capabilities were primarily focused on moving workloads to Azure SQL Managed Instance. However, many organizations require the flexibility to migrate SQL Server workloads to infrastructure-as-a-service (IaaS) environments, such as SQL Server running on Azure Virtual Machines (VMs), to maintain compatibility with existing applications and configurations. This update addresses that need by expanding migration targets, allowing organizations to leverage Azure Arc for migrations not only to managed database services but also to SQL Server instances hosted on Azure VMs.

**Specific Features and Detailed Changes:**  
- **Expanded Migration Targets:** Azure Arc migration now supports SQL Server on Azure Virtual Machines as a destination, in addition to Azure SQL Managed Instance.
- **Unified Migration Experience:** The migration workflow remains consistent, enabling IT professionals to use the same unified migration tooling and processes for both managed and IaaS-based SQL Server targets.
- **Arc-Enabled Source Support:** The source SQL Server instances must be Arc-enabled, ensuring consistent management and governance across hybrid and multi-cloud environments.

**Technical Mechanisms and Implementation Methods:**  
- **Migration Orchestration:** The migration process is orchestrated through Azure Arc, which provides centralized management and monitoring for SQL Server instances regardless of their location.
- **Source Requirements:** The source SQL Server must be Arc-enabled, which involves installing the Azure Arc agent and registering the instance with Azure.
- **Target Selection:** During migration, users can now select SQL Server on Azure Virtual Machines as the target environment, in addition to previously available options.
- **Migration Workflow:** The migration leverages the same tooling and automation as migrations to Azure SQL Managed Instance, streamlining the process and reducing operational complexity.

**Use Cases and Application Scenarios:**  
- **Lift-and-Shift Migrations:** Organizations with legacy or custom SQL Server workloads that require full control over the operating system and SQL Server configuration can migrate to Azure VMs instead of managed services.
- **Hybrid Deployments:** Enterprises managing a mix of on-premises, multi-cloud, and Azure-based SQL Server instances can standardize migration and management practices using Azure Arc.
- **Regulatory or Application Constraints:** Workloads with specific compliance, licensing, or application dependencies that are not supported on Azure SQL Managed Instance can be migrated to SQL Server on Azure VMs.

**Important Considerations and Limitations:**  
- **Public Preview:** This feature is currently in public preview, which may involve limited support and potential changes before general availability.
- **Arc-Enablement Requirement:** Only Arc-enabled SQL Server instances are eligible for migration using this method.
- **Feature Parity:** The update does not specify feature parity or limitations between migration to Azure SQL Managed Instance and Azure VMs; users should evaluate their workload requirements accordingly.

**Integration with Related Azure Services:**  
- **Azure Arc:** Central to the migration process, providing unified management, monitoring, and governance for SQL Server instances across environments.
- **Azure Virtual Machines:** Serves as the new migration target for SQL Server workloads, offering flexibility and control for IaaS deployments.
- **Azure SQL Managed Instance:** Remains a supported migration target, allowing organizations to choose the best fit for their workloads.

**Summary:**  
Azure Arc migration now supports SQL Server on Azure Virtual Machines as a migration target in public preview, enabling a unified migration experience for Arc-enabled SQL Server instances to both Azure SQL Managed Instance and SQL Server on Azure infrastructure.

---

### 2. Generally Available: Azure Database for PostgreSQL flexible server in Denmark East  

**Published**: April 22, 2026 17:45:10 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL flexible server in Denmark East  ](https://azure.microsoft.com/updates?id=560288)

**Update ID**: 560288
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server is now generally available in the Denmark East Azure region.

- Key changes or new features  
Developers and IT professionals can now deploy and manage PostgreSQL flexible servers in the Denmark East region. This enables improved data residency options, lower latency for local users, and enhanced disaster recovery and high availability configurations within Denmark.

- Target audience affected  
Developers, database administrators, and IT professionals who use Azure Database for PostgreSQL Flexible Server and require deployment in the Denmark East region, especially those with data residency or compliance requirements in Denmark.

- Important notes if any  
This update allows organizations to meet local compliance and data sovereignty requirements by hosting PostgreSQL databases within Denmark. All features available in other regions for Azure Database for PostgreSQL Flexible Server are now supported in Denmark East. For more information, refer to the official Azure documentation.

**Details**:

**Comprehensive Technical Explanation: Azure Database for PostgreSQL Flexible Server – General Availability in Denmark East**

**Background and Purpose of the Update**  
This update announces the general availability of Azure Database for PostgreSQL Flexible Server in the Denmark East Azure region. The purpose of this release is to expand the regional coverage of Azure’s managed PostgreSQL database service, enabling customers to deploy workloads closer to users and data sources within Denmark East. This supports compliance, data residency, and performance requirements for organizations operating in or serving this geographic area.

**Specific Features and Detailed Changes**  
With this update, all features of Azure Database for PostgreSQL Flexible Server are now available for deployment in the Denmark East region. This includes high availability options, zone-redundant deployments, automated backups, scaling of compute and storage resources, and advanced security features such as network isolation and private access. The update does not introduce new features to the service itself but extends the existing capabilities to a new geographic location.

**Technical Mechanisms and Implementation Methods**  
Azure Database for PostgreSQL Flexible Server is a fully managed database service built on the open-source PostgreSQL engine. The service provides flexible configuration options for compute, storage, and backup retention. Deployments in Denmark East are provisioned using the same Azure Resource Manager (ARM) templates, CLI commands, or Azure Portal workflows as in other supported regions. The underlying infrastructure leverages Azure’s regional data centers in Denmark East, ensuring local data processing and storage.

**Use Cases and Application Scenarios**  
- Organizations with users or operations in Denmark can now deploy PostgreSQL workloads with lower latency and improved performance.
- Applications requiring data residency within Denmark for regulatory or compliance reasons can utilize this regional deployment.
- Multi-region architectures can include Denmark East for disaster recovery, high availability, or geo-distributed applications.
- SaaS providers targeting Danish customers can offer improved service levels by hosting their data in Denmark East.

**Important Considerations and Limitations**  
- Customers must verify that all required service tiers, compute sizes, and storage options are available in Denmark East, as initial regional rollouts may have phased availability.
- Pricing for the service in Denmark East may differ from other regions and should be reviewed in the Azure pricing calculator.
- Network latency and data transfer costs should be considered when architecting solutions that span multiple regions.
- Customers should confirm that all compliance and data residency requirements are met by hosting data in Denmark East.

**Integration with Related Azure Services**  
Azure Database for PostgreSQL Flexible Server in Denmark East can be integrated with other Azure services available in the region, such as Azure Virtual Network, Azure Key Vault, Azure Monitor, and Azure Backup. This enables secure network architectures, centralized secrets management, monitoring and alerting, and automated backup solutions. Integration is performed using standard Azure mechanisms such as managed identities, private endpoints, and resource group management.

**Summary Sentence**  
Azure Database for PostgreSQL Flexible Server is now generally available in the Denmark East region, allowing customers to deploy managed PostgreSQL databases with full feature support, regional data residency, and integration with local Azure services.

---

### 3. Generally Available: Dynamic data masking with Azure Cosmos DB 

**Published**: April 22, 2026 17:45:10 UTC
**Link**: [Generally Available: Dynamic data masking with Azure Cosmos DB ](https://azure.microsoft.com/updates?id=559633)

**Update ID**: 559633
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Dynamic Data Masking (DDM) is now generally available in Azure Cosmos DB.

- Key changes or new features  
DDM is a server-side, policy-based security feature that enables organizations to automatically mask sensitive data in Azure Cosmos DB. It enforces masking rules at the database layer, ensuring that non-privileged users see obfuscated data while privileged users retain full access. DDM is configurable via policies, allowing granular control over which fields are masked and how. This feature helps organizations comply with data privacy requirements and reduces the risk of data exposure.

- Target audience affected  
Developers and IT professionals managing Azure Cosmos DB, especially those responsible for data security, compliance, and application development involving sensitive information.

- Important notes if any  
DDM operates transparently at the API/data access layer, requiring minimal changes to application code. It supports multiple APIs (e.g., SQL API) and integrates with existing Cosmos DB RBAC and security models. Review your current data access patterns and update masking policies as needed to ensure sensitive data is protected according to your organization’s requirements.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=559633).

**Details**:

**Azure Update Report: Dynamic Data Masking with Azure Cosmos DB (Generally Available)**  
[Source Link](https://azure.microsoft.com/updates?id=559633)

---

**Background and Purpose of the Update**

Dynamic Data Masking (DDM) is now generally available for Azure Cosmos DB. The primary purpose of this update is to enhance data security by providing organizations with a server-side, policy-driven mechanism to protect sensitive information stored in Cosmos DB. DDM is designed to prevent unauthorized access to sensitive data, especially for nonprivileged users, by masking data dynamically at query time.

---

**Specific Features and Detailed Changes**

- **Server-Side Masking:** DDM operates at the server level, ensuring that data is masked before it is returned to the client application. This prevents exposure of sensitive data in query results for users without sufficient privileges.
- **Policy-Based Configuration:** Administrators can define masking policies specifying which fields or attributes in Cosmos DB documents should be masked and under what conditions.
- **Granular Access Control:** Masking is applied dynamically based on user roles and privileges, allowing organizations to tailor data visibility according to operational requirements.
- **General Availability:** The feature is now fully supported and ready for production use across Cosmos DB deployments.

---

**Technical Mechanisms and Implementation Methods**

- **Policy Definition:** Masking policies are configured at the server level, typically through Azure Portal, Azure CLI, or ARM templates. Policies specify target fields and masking rules (e.g., full masking, partial masking, custom masking patterns).
- **Role-Based Enforcement:** When a query is executed, Cosmos DB evaluates the user's privileges. If the user is nonprivileged, the masking policy is applied to the query result set.
- **Transparent Masking:** The masking occurs transparently, requiring no changes to client applications or query syntax. Data is masked in real-time as it is retrieved from the database.
- **Integration with Cosmos DB Security Model:** DDM leverages Cosmos DB’s built-in authentication and authorization mechanisms to determine user privilege levels.

---

**Use Cases and Application Scenarios**

- **Regulatory Compliance:** Organizations subject to regulations such as GDPR, HIPAA, or PCI DSS can use DDM to ensure sensitive data (e.g., personal identifiers, financial information) is not exposed to unauthorized users.
- **Application Development:** Developers can test applications with masked data, reducing the risk of accidental exposure during development or QA processes.
- **Operational Security:** DDM allows operational staff, support teams, or analytics users to access necessary data without revealing sensitive information, supporting least-privilege access models.

---

**Important Considerations and Limitations**

- **Policy Management:** Careful policy configuration is required to ensure that masking is applied correctly and does not interfere with legitimate business processes.
- **Performance Impact:** While DDM is designed to be efficient, masking operations may introduce minimal latency depending on the complexity of masking rules and query patterns.
- **Scope of Masking:** DDM only masks data at query time for nonprivileged users; privileged users and administrators retain full access to unmasked data.
- **Data Consistency:** Masked data is only visible in query results; the underlying data remains unchanged in the database.

---

**Integration with Related Azure Services**

- **Azure Portal and CLI:** DDM policies can be managed via Azure Portal or CLI, facilitating integration with existing Azure management workflows.
- **Azure Security and Compliance:** DDM complements other Azure security features such as encryption at rest, network security, and access control, providing a layered approach to data protection.
- **Monitoring and Auditing:** Integration with Azure Monitor and auditing tools enables tracking of masked data access and policy changes for compliance reporting.

---

**Summary Sentence**  
Dynamic Data Masking for Azure Cosmos DB is now generally available, providing a server-side, policy-driven solution to protect sensitive data by dynamically masking query results for nonprivileged users, thereby enhancing security and compliance in cloud-based applications.

---

### 4. Public Preview: Logical replication slot sync Status metric for Azure PostgreSQL Flexible Server 

**Published**: April 22, 2026 17:45:10 UTC
**Link**: [Public Preview: Logical replication slot sync Status metric for Azure PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=513249)

**Update ID**: 513249
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports monitoring the synchronization status of logical replication slots using a new Azure Monitor metric, logical_replication_slot_sync_status, available in public preview.

- Key changes or new features  
A new metric, logical_replication_slot_sync_status, is introduced. This metric allows users to track whether each logical replication slot is synchronized or not. It provides real-time visibility into replication slot health, enabling proactive detection of synchronization issues that could impact data replication or downstream applications.

- Target audience affected  
Developers and IT professionals managing PostgreSQL Flexible Server instances, especially those using logical replication for data integration, change data capture, or high availability scenarios.

- Important notes if any  
This feature is currently in public preview and may be subject to changes before general availability. Monitoring replication slot status helps prevent data loss and replication lag by alerting users to synchronization problems early. Integration with Azure Monitor enables automated alerting and dashboarding for improved operational visibility.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=513249

**Details**:

**Azure Update Technical Explanation: Public Preview: Logical replication slot sync Status metric for Azure PostgreSQL Flexible Server**

**Background and Purpose of the Update:**  
Logical replication is a widely used feature in PostgreSQL, enabling selective replication of data changes to other databases or systems. In Azure Database for PostgreSQL – Flexible Server, replication slots are essential to maintain the state and progress of logical replication streams. However, monitoring the synchronization status of these slots has previously been challenging, making it difficult for administrators to ensure replication health and troubleshoot issues proactively. This update introduces the logical_replication_slot_sync_status metric, now available in public preview, to address this visibility gap.

**Specific Features and Detailed Changes:**  
The update adds a new Azure Monitor metric called logical_replication_slot_sync_status for Azure Database for PostgreSQL – Flexible Server. This metric provides real-time information on whether each logical replication slot is synchronized. The metric can be visualized, queried, and alerted on using Azure Monitor tools, enabling administrators to track the health and status of logical replication slots directly from the Azure portal or via APIs.

**Technical Mechanisms and Implementation Methods:**  
The logical_replication_slot_sync_status metric is exposed through Azure Monitor, leveraging the native integration between Azure Database for PostgreSQL – Flexible Server and Azure’s monitoring infrastructure. The metric reflects the synchronization state of each logical replication slot, allowing for automated or manual monitoring. The metric can be consumed via Azure Monitor dashboards, Log Analytics, or custom alerting rules, providing flexibility in how monitoring data is accessed and acted upon.

**Use Cases and Application Scenarios:**  
- **High Availability and Disaster Recovery:** Ensuring logical replication slots are synchronized is critical for scenarios involving read replicas, data warehousing, or cross-region replication for business continuity.
- **Change Data Capture (CDC):** Organizations using logical replication for CDC pipelines can monitor slot health to prevent data loss or pipeline failures.
- **Operational Monitoring:** Database administrators can set up alerts to be notified if a replication slot falls out of sync, enabling rapid response to potential replication issues.

**Important Considerations and Limitations:**  
- The logical_replication_slot_sync_status metric is currently in public preview, and should be evaluated accordingly before use in production-critical monitoring.
- The metric is specific to logical replication slots and does not provide information about physical replication or other replication mechanisms.
- Users should ensure that their monitoring and alerting configurations are updated to include this new metric for comprehensive replication health monitoring.

**Integration with Related Azure Services:**  
This metric is fully integrated with Azure Monitor, allowing seamless use with Azure Monitor dashboards, Log Analytics for advanced querying, and Azure Alerts for automated notifications. It complements existing monitoring capabilities for Azure Database for PostgreSQL – Flexible Server, providing a more complete view of replication health alongside other performance and availability metrics.

**Summary:**  
The logical_replication_slot_sync_status metric, now in public preview for Azure Database for PostgreSQL – Flexible Server, enables real-time monitoring of logical replication slot synchronization status through Azure Monitor, enhancing visibility and operational control for replication scenarios.

---

### 5. Generally Available: Premium SSD v2 for Azure Database for PostgreSQL  

**Published**: April 22, 2026 17:30:14 UTC
**Link**: [Generally Available: Premium SSD v2 for Azure Database for PostgreSQL  ](https://azure.microsoft.com/updates?id=560336)

**Update ID**: 560336
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Premium SSD v2 is now generally available for Azure Database for PostgreSQL flexible server.

- Key changes or new features  
Premium SSD v2 offers up to 4x higher IOPS compared to previous disk options, significantly lower latency, and improved price-performance for I/O-intensive workloads. This enhancement enables faster data access and better overall database performance.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL flexible servers, especially those with high I/O or latency-sensitive workloads.

- Important notes if any  
Premium SSD v2 is recommended for production environments requiring high throughput and low-latency storage. Existing deployments can migrate to Premium SSD v2 to take advantage of these benefits. Review your workload requirements and consider updating storage configurations to optimize performance and cost. For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=560336

**Details**:

**Comprehensive Technical Explanation: Azure Update – Premium SSD v2 for Azure Database for PostgreSQL (Generally Available)**

**Background and Purpose of the Update**  
The general availability of Premium SSD v2 for Azure Database for PostgreSQL flexible server addresses the growing demand for higher performance and cost-efficient storage solutions in cloud-based database environments. As workloads become more data-intensive and require faster access to persistent storage, this update aims to deliver improved IOPS (Input/Output Operations Per Second), reduced latency, and enhanced price-performance for I/O-intensive applications.

**Specific Features and Detailed Changes**  
Premium SSD v2 introduces several key enhancements over previous storage offerings for Azure Database for PostgreSQL flexible server:

- **Up to Four Times Higher IOPS:** Compared to earlier Premium SSD options, Premium SSD v2 delivers a substantial increase in IOPS, enabling faster data access and processing.
- **Significantly Lower Latency:** The new storage tier reduces latency, which is critical for transactional and real-time workloads.
- **Improved Price-Performance:** Premium SSD v2 is designed to offer better value, optimizing cost relative to performance for I/O-intensive workloads.
- **General Availability:** The feature is now fully supported and ready for production use, ensuring reliability and support from Azure.

**Technical Mechanisms and Implementation Methods**  
Premium SSD v2 leverages advancements in Azure’s storage infrastructure, utilizing next-generation solid-state drives (SSDs) with optimized controllers and firmware. The integration with Azure Database for PostgreSQL flexible server is seamless, allowing users to select Premium SSD v2 as their storage option during server provisioning or via configuration changes. The storage tier is managed and provisioned through Azure Resource Manager, ensuring consistent deployment and management practices.

**Use Cases and Application Scenarios**  
Premium SSD v2 is particularly suited for:

- **High-Volume Transactional Systems:** Applications requiring rapid read/write operations, such as financial systems, e-commerce platforms, and real-time analytics.
- **I/O-Intensive Workloads:** Scenarios involving large data ingestion, batch processing, or complex queries that benefit from high throughput and low latency.
- **Mission-Critical Databases:** Deployments where consistent performance and reliability are paramount, such as healthcare, manufacturing, and enterprise resource planning (ERP) systems.

**Important Considerations and Limitations**  
When adopting Premium SSD v2, IT professionals should consider:

- **Compatibility:** Ensure that the selected PostgreSQL flexible server configuration supports Premium SSD v2.
- **Cost Management:** While Premium SSD v2 offers improved price-performance, it may still represent a higher cost tier compared to standard storage options. Proper sizing and workload analysis are recommended.
- **Migration:** Existing servers may require migration or reconfiguration to leverage Premium SSD v2, which could involve downtime or data transfer operations.
- **Performance Tuning:** Optimal results may require tuning PostgreSQL parameters to fully utilize the increased IOPS and reduced latency.

**Integration with Related Azure Services**  
Premium SSD v2 is fully integrated with Azure Database for PostgreSQL flexible server and can be managed through the Azure Portal, CLI, or ARM templates. It supports standard Azure features such as backup, restore, and monitoring. The storage tier can also be used in conjunction with other Azure services, such as Azure Virtual Network, Azure Backup, and Azure Security Center, to provide comprehensive solutions for secure, high-performance database deployments.

**Summary Sentence**  
Premium SSD v2 for Azure Database for PostgreSQL flexible server is now generally available, offering up to four times higher IOPS, significantly lower latency, and improved price-performance for I/O-intensive workloads.

---

### 6. Public Preview: Migrating from virtual network-integrated to Private Endpoint–capable network configuration 

**Published**: April 22, 2026 17:30:14 UTC
**Link**: [Public Preview: Migrating from virtual network-integrated to Private Endpoint–capable network configuration ](https://azure.microsoft.com/updates?id=560298)

**Update ID**: 560298
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL now supports migrating from virtual network-integrated deployments to network configurations that enable Private Endpoint connectivity (Public Preview).

- Key changes or new features  
  - You can migrate existing PostgreSQL servers that were originally deployed inside a virtual network (using VNet integration) to a setup that supports Private Endpoint connections.
  - This migration allows for enhanced security and network isolation by leveraging Private Endpoints, which provide private IP addresses within your VNet for database access.
  - The update streamlines the transition to Private Endpoint without needing to redeploy or recreate the database server.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL deployments, especially those seeking improved network security and isolation using Private Endpoints.

- Important notes if any  
  - The feature is currently in Public Preview and may not be recommended for production workloads.
  - Review Azure documentation for migration prerequisites and limitations before starting the migration.
  - This update helps organizations meet stricter compliance and security requirements by moving away from public network exposure.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=560298)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Migrating from virtual network-integrated to Private Endpoint–capable network configuration  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=560298)

---

**Background and Purpose of the Update**  
Azure Database for PostgreSQL servers have traditionally supported deployment within a virtual network (VNet) using VNet integration. This approach provides network isolation and control but does not leverage the enhanced security and connectivity features offered by Azure Private Endpoint. The purpose of this update is to enable customers to migrate their PostgreSQL server deployments from VNet integration to a network configuration that supports Private Endpoint connectivity, thereby improving security, simplifying network architecture, and aligning with best practices for secure database access.

**Specific Features and Detailed Changes**  
- **Migration Capability:** The update introduces the ability to migrate an existing Azure Database for PostgreSQL server from a VNet-integrated deployment to a configuration that allows Private Endpoint connectivity.
- **Network Configuration Enhancement:** Post-migration, the server can be accessed securely via Private Endpoint, which maps the database service to a private IP address within your VNet.
- **Public Preview:** This feature is currently in public preview, allowing customers to test and validate the migration process before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Migration Process:** The migration involves reconfiguring the network settings of the PostgreSQL server instance. This typically requires removing the VNet integration and enabling Private Endpoint support.
- **Private Endpoint Setup:** After migration, a Private Endpoint can be created in the desired VNet, associating it with the PostgreSQL server. This enables access to the server over a private IP, eliminating exposure to public internet and reducing attack surface.
- **DNS Configuration:** Proper DNS setup is required to resolve the server’s hostname to the private IP address assigned by the Private Endpoint.

**Use Cases and Application Scenarios**  
- **Enhanced Security:** Organizations seeking to restrict database access to only specific VNets and eliminate public internet exposure will benefit from this migration.
- **Compliance Requirements:** Enterprises with strict regulatory or compliance mandates (e.g., PCI DSS, HIPAA) can leverage Private Endpoint to meet network isolation and data privacy requirements.
- **Simplified Network Architecture:** Migrating to Private Endpoint reduces the complexity of managing firewall rules and network security groups compared to VNet integration.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Customers should validate functionality and monitor for any issues.
- **Downtime and Service Impact:** Migration may require downtime or service interruption. Careful planning and testing are recommended.
- **Compatibility:** Not all features or configurations may be supported during the preview phase. Review Azure documentation for supported scenarios.
- **DNS and Connectivity:** Ensure proper DNS resolution and connectivity testing post-migration to avoid disruptions.

**Integration with Related Azure Services**  
- **Azure Private Link:** The migration enables integration with Azure Private Link, allowing secure connectivity to the PostgreSQL server from within the VNet.
- **Azure Virtual Network:** Private Endpoint operates within the Azure VNet, maintaining network isolation and control.
- **Azure DNS:** Integration with Azure DNS or custom DNS solutions is necessary for proper name resolution to the Private Endpoint.

---

**Summary Sentence:**  
Azure Database for PostgreSQL now supports migration from virtual network-integrated deployments to Private Endpoint–capable network configurations in public preview, enabling enhanced security and simplified connectivity for database access within Azure VNets.

---

### 7. Generally Available: Enhanced Mirroring Azure Database for PostgreSQL in Microsoft Fabric 

**Published**: April 22, 2026 17:30:14 UTC
**Link**: [Generally Available: Enhanced Mirroring Azure Database for PostgreSQL in Microsoft Fabric ](https://azure.microsoft.com/updates?id=560293)

**Update ID**: 560293
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Analytics, Azure Database for PostgreSQL, Microsoft Fabric, Features

**Summary**:

- What was updated  
Enhanced Mirroring for Azure Database for PostgreSQL in Microsoft Fabric is now generally available.

- Key changes or new features  
  - Improved support for mirroring real-world Azure Database for PostgreSQL workloads at scale within Microsoft Fabric.  
  - Native support for PostgreSQL data types, including JSON, JSONB, and other commonly used types, ensuring seamless data compatibility and integrity during mirroring.  
  - Enhanced operational reliability and confidence when managing mirrored workloads.

- Target audience affected  
  - Developers and IT professionals who manage, migrate, or analyze PostgreSQL data in Azure environments.  
  - Teams leveraging Microsoft Fabric for analytics, reporting, or integration scenarios involving PostgreSQL data sources.

- Important notes if any  
  - The enhanced mirroring capabilities simplify the process of integrating and operating PostgreSQL workloads in Microsoft Fabric, reducing friction for analytics and operational use cases.  
  - Native data type support minimizes the need for custom data transformations, streamlining migrations and ongoing operations.  
  - This update is now generally available and ready for production workloads.

For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=560293).

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Enhanced Mirroring Azure Database for PostgreSQL in Microsoft Fabric  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=560293)

---

**Background and Purpose of the Update**  
This update addresses the need for scalable, reliable mirroring of Azure Database for PostgreSQL workloads within Microsoft Fabric. As organizations increasingly leverage PostgreSQL for mission-critical applications, ensuring seamless data integration and operational confidence in analytics platforms like Microsoft Fabric is essential. The update aims to simplify and enhance the process of mirroring real-world PostgreSQL workloads, supporting advanced data types and providing robust operational capabilities.

**Specific Features and Detailed Changes**  
- **Native PostgreSQL Data Type Support:** The update introduces the ability to mirror native PostgreSQL data types, including JSON, JSONB, and other commonly used types. This ensures that complex data structures are accurately replicated within Microsoft Fabric.
- **Scalable Mirroring Capabilities:** Enhanced mirroring allows for the replication of large-scale PostgreSQL workloads, supporting enterprise-grade data volumes and performance requirements.
- **Operational Confidence:** The update provides improved reliability and consistency in mirrored data, enabling IT professionals to operate their workloads with greater assurance.

**Technical Mechanisms and Implementation Methods**  
- **Data Type Handling:** The mirroring process now natively understands and replicates PostgreSQL-specific data types such as JSON and JSONB. This is achieved through advanced schema mapping and data transformation mechanisms that preserve data fidelity during transfer.
- **Mirroring Architecture:** The mirroring solution leverages Microsoft Fabric’s integration pipelines to connect to Azure Database for PostgreSQL instances, extract data, and synchronize it efficiently. The architecture is designed to minimize latency and ensure transactional consistency.
- **Operational Tools:** Enhanced monitoring and management tools are provided to oversee the mirroring process, detect anomalies, and ensure data integrity.

**Use Cases and Application Scenarios**  
- **Analytics and Reporting:** Organizations can mirror their operational PostgreSQL databases into Microsoft Fabric for advanced analytics, business intelligence, and reporting without impacting production workloads.
- **Data Lake Integration:** Mirrored data can be ingested into Microsoft Fabric’s data lake for large-scale processing, machine learning, and downstream application integration.
- **Disaster Recovery and Backup:** Mirroring can be used as part of a disaster recovery strategy, ensuring a consistent copy of PostgreSQL data is available in Microsoft Fabric.

**Important Considerations and Limitations**  
- **Data Type Compatibility:** While support for JSON, JSONB, and other commonly used types is included, IT professionals should verify compatibility for any custom or less common data types.
- **Performance Impact:** Large-scale mirroring may impact source database performance; proper resource planning and monitoring are recommended.
- **Operational Overhead:** Monitoring and managing mirrored workloads require additional operational oversight to ensure data consistency and integrity.

**Integration with Related Azure Services**  
- **Azure Database for PostgreSQL:** The update directly enhances integration between Azure Database for PostgreSQL and Microsoft Fabric, streamlining data movement and synchronization.
- **Microsoft Fabric:** Mirrored data can be utilized across Fabric’s analytics, data lake, and reporting services, enabling unified data workflows.
- **Azure Data Factory:** Integration pipelines may leverage Azure Data Factory for orchestrating mirroring operations, providing flexibility and automation.

---

**Summary Sentence:**  
The enhanced mirroring capabilities for Azure Database for PostgreSQL in Microsoft Fabric are now generally available, enabling scalable replication of native PostgreSQL data types such as JSON and JSONB for robust analytics and operational confidence.

---


*This report was automatically generated - 2026-04-23 03:03:32 UTC*