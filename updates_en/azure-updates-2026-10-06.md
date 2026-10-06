# October 06, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 06, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Public Preview: Azure HorizonDB expands to additional regions

**Published**: October 05, 2026 18:51:57 UTC
**Link**: [Public Preview: Azure HorizonDB expands to additional regions](https://azure.microsoft.com/updates?id=572940)

**Update ID**: 572940
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Feature

**Summary**:

- What was updated  
Azure HorizonDB is now available in additional Azure regions as part of its public preview.

- Key changes or new features  
The regional expansion allows users to deploy Azure HorizonDB—Microsoft’s managed PostgreSQL-compatible database—closer to their applications and end users. This enhances performance, reduces latency, and provides more options for meeting data residency and compliance requirements.

- Target audience affected  
Developers and IT professionals who are building or managing PostgreSQL workloads on Azure, especially those with global applications or specific regional compliance needs.

- Important notes if any  
The expanded regional availability is currently in public preview, so some features may be subject to change or have limited support. Users should review the list of supported regions and consider testing workloads in the new regions to validate performance and compatibility before moving production workloads. For more details and the latest supported regions, refer to the official Azure Updates page.

**Details**:

**Azure Update Report: Public Preview – Azure HorizonDB Expands to Additional Regions**

**Background and Purpose of the Update**  
Azure HorizonDB, a managed database solution for PostgreSQL workloads, is now available in additional Azure regions. The primary purpose of this update is to provide customers with greater flexibility in deploying their PostgreSQL workloads closer to their applications and end-users. By expanding regional availability, Azure aims to reduce latency, improve performance, and support compliance with local data residency requirements.

**Specific Features and Detailed Changes**  
The update introduces Azure HorizonDB to more Azure regions, increasing the geographic options for deployment. This expansion allows customers to select from a broader range of locations when provisioning HorizonDB instances, optimizing for proximity to their users or application infrastructure. The core features of HorizonDB remain unchanged; the update focuses on regional availability rather than new database functionality.

**Technical Mechanisms and Implementation Methods**  
Azure HorizonDB leverages Azure’s global infrastructure to provision managed PostgreSQL database instances in newly supported regions. The technical implementation involves enabling HorizonDB resource provisioning within the Azure portal, CLI, and ARM templates for these regions. Customers can select the desired region during deployment, and Azure automatically handles resource allocation, networking, and high availability configurations according to regional capabilities.

**Use Cases and Application Scenarios**  
- **Latency-sensitive Applications:** Deploying HorizonDB in regions closer to application servers or end-users minimizes network latency, improving responsiveness for real-time workloads.
- **Global SaaS Platforms:** Organizations with a global user base can provision HorizonDB instances in multiple regions to support regional data access and performance.
- **Compliance and Data Residency:** Enterprises with regulatory requirements can deploy HorizonDB in specific regions to ensure data remains within designated geographic boundaries.
- **Disaster Recovery and High Availability:** Multi-region deployment enables robust disaster recovery strategies and enhances high availability by distributing workloads across regions.

**Important Considerations and Limitations**  
- **Regional Feature Parity:** While HorizonDB is available in additional regions, some advanced features or configurations may not be uniformly supported across all regions during the public preview phase.
- **Pricing and Quotas:** Resource pricing, quotas, and availability may vary by region. IT professionals should consult the Azure documentation for region-specific details before deployment.
- **Public Preview Status:** As this is a public preview, HorizonDB in new regions may be subject to changes, limited support, or evolving SLAs. Production workloads should be carefully evaluated for preview suitability.
- **Migration and Replication:** Existing HorizonDB instances may require migration or replication strategies to take advantage of new regional availability.

**Integration with Related Azure Services**  
Azure HorizonDB integrates seamlessly with other Azure services such as Azure Virtual Machines, Azure App Service, and Azure Kubernetes Service for application hosting. It also supports Azure networking features, including Virtual Network integration and private endpoints, to secure database access. Customers can leverage Azure Monitor and Azure Security Center for operational insights and security management of HorizonDB deployments in expanded regions.

**Summary Sentence**  
Azure HorizonDB’s expansion to additional Azure regions in public preview offers IT professionals enhanced flexibility for deploying managed PostgreSQL workloads closer to their applications and users, supporting improved performance, compliance, and regional deployment strategies.

---

### 2. Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu 

**Published**: October 05, 2026 18:12:09 UTC
**Link**: [Generally Available: SQL Server on Azure Virtual Machines in Azure Bleu ](https://azure.microsoft.com/updates?id=571499)

**Update ID**: 571499
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Databases, SQL Server on Azure Virtual Machines, Feature

**Summary**:

- What was updated  
SQL Server on Azure Virtual Machines is now generally available in Azure Bleu, Microsoft’s sovereign cloud for France.

- Key changes or new features  
This update enables deployment and management of SQL Server workloads on Azure Virtual Machines within Azure Bleu. It supports compliance with French data residency and sovereignty regulations, ensuring that sensitive data remains within France’s national cloud infrastructure.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who manage SQL Server workloads and require compliance with French or EU data sovereignty requirements. Organizations in regulated sectors such as government, healthcare, and finance will benefit most.

- Important notes if any  
Workloads can now be migrated or deployed directly to Azure Bleu, leveraging familiar Azure VM and SQL Server management tools while meeting strict compliance needs. Ensure your applications and data governance policies align with Azure Bleu’s operational model. Review Azure Bleu’s documentation for any service limitations or differences compared to global Azure regions.

Learn more: [Azure Update](https://azure.microsoft.com/updates?id=571499)

**Details**:

**Comprehensive Technical Explanation of the Azure Update: SQL Server on Azure Virtual Machines in Azure Bleu**

**Background and Purpose of the Update**  
This update announces the general availability of SQL Server on Azure Virtual Machines (VMs) within Azure Bleu, Microsoft's sovereign cloud offering for France. The primary purpose is to enable organizations operating in France to deploy and manage SQL Server workloads in a cloud environment that adheres to strict data residency and sovereignty requirements. Azure Bleu is designed to meet regulatory and compliance needs specific to the French public sector and regulated industries, ensuring that sensitive data remains within national borders and under local jurisdiction.

**Specific Features and Detailed Changes**  
With this update, SQL Server on Azure VMs is now fully supported in Azure Bleu. This means customers can provision Windows or Linux-based Azure VMs pre-configured with SQL Server editions (such as Standard, Enterprise, or Web) directly within the Azure Bleu region. The offering includes all standard SQL Server VM features, such as automated patching, backup, and integration with Azure management tools. The deployment options mirror those available in global Azure regions, but are tailored to operate within the sovereign cloud infrastructure.

**Technical Mechanisms and Implementation Methods**  
Technically, SQL Server on Azure VMs in Azure Bleu leverages the same architecture as in other Azure regions, utilizing Azure Resource Manager (ARM) for provisioning, management, and automation. Customers can use Azure Portal, CLI, or PowerShell to deploy SQL Server VMs, selecting from a range of VM sizes and storage configurations. The VMs are hosted in data centers located in France, ensuring compliance with data residency requirements. Integration with Azure Bleu’s identity and access management, as well as networking and security features, is provided to maintain sovereignty and control over data.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Government agencies and regulated industries (such as healthcare and finance) requiring SQL Server workloads to remain within French borders.
- Organizations migrating legacy SQL Server databases to the cloud while maintaining compliance with local regulations.
- Enterprises needing high availability, disaster recovery, and scalability for SQL Server workloads in a sovereign cloud context.
- Development and testing environments for SQL Server applications that must comply with French data sovereignty.

**Important Considerations and Limitations**  
IT professionals should note:
- All resources and data must reside within Azure Bleu’s French data centers to meet sovereignty requirements.
- Service availability, features, and integration may differ from global Azure regions due to the sovereign nature of Azure Bleu.
- Licensing and pricing for SQL Server on Azure VMs in Azure Bleu may be distinct from other Azure regions; review documentation for specifics.
- Connectivity and integration with external systems must comply with Azure Bleu’s security and compliance standards.

**Integration with Related Azure Services**  
SQL Server on Azure VMs in Azure Bleu can be integrated with other Azure Bleu services, such as Azure Backup for database protection, Azure Monitor for performance and health monitoring, and Azure Security Center for enhanced security management. The update ensures that SQL Server workloads benefit from the same management and automation capabilities as in global Azure, but within a sovereign cloud environment.

**Summary Sentence**  
SQL Server on Azure Virtual Machines is now generally available in Azure Bleu, enabling secure, compliant deployment and management of SQL Server workloads within France’s sovereign cloud to meet data residency and sovereignty requirements.

---

### 3. Announcing: Table discovery in OneLake Catalog search

**Published**: October 05, 2026 17:55:23 UTC
**Link**: [Announcing: Table discovery in OneLake Catalog search](https://azure.microsoft.com/updates?id=573875)

**Update ID**: 573875
**Data source**: Azure Updates API

**Categories**: Analytics, Microsoft Fabric, Announcement

**Summary**:

- What was updated  
Microsoft Fabric’s OneLake Catalog search functionality has been enhanced to support table-level discovery.

- Key changes or new features  
Starting October 15, 2026, search results in Microsoft Fabric will include individual tables from semantic models, lakehouses, and mirrored databases. Users can search for tables by their name or description, and can also locate tables by matching exact column names. This improves granularity and precision in data discovery within the OneLake Catalog.

- Target audience affected  
This update primarily impacts developers, data engineers, and IT professionals who manage or interact with data assets in Microsoft Fabric, especially those leveraging OneLake for analytics, data warehousing, or BI scenarios.

- Important notes if any  
The enhanced search capability streamlines data asset discovery, making it easier to find and reference specific tables across different data sources. Developers and IT professionals should review their data cataloging practices to ensure table names and descriptions are meaningful and up-to-date, optimizing searchability for end users. The update is scheduled to take effect on October 15, 2026.

[More details](https://azure.microsoft.com/updates?id=573875)

**Details**:

**Comprehensive Technical Explanation: Azure Update – Table Discovery in OneLake Catalog Search**

**Background and Purpose of the Update**  
The update introduces enhanced table discovery capabilities within the Microsoft Fabric environment, specifically targeting the OneLake Catalog search functionality. The primary purpose is to streamline data asset identification by enabling granular search of tables across various data storage paradigms, including semantic models, lakehouses, and mirrored databases. This improvement addresses the need for more precise and efficient data exploration, facilitating easier access to relevant datasets for analytics, reporting, and integration tasks.

**Specific Features and Detailed Changes**  
Starting October 15, 2026, the Microsoft Fabric search feature will return tables as individual search results. This enhancement applies to tables originating from semantic models, lakehouses, and mirrored databases. Users can now search for tables using the following criteria:
- Table name
- Table description
- Exact column-name match

This granular search capability allows users to locate specific tables or columns without navigating through entire models or databases, thereby reducing time spent on data discovery and increasing productivity.

**Technical Mechanisms and Implementation Methods**  
The update leverages the OneLake Catalog, which acts as a unified metadata repository for Microsoft Fabric assets. The search functionality is extended to index and retrieve table-level metadata, including names, descriptions, and column definitions. When a user initiates a search, the system parses the query and matches it against indexed table attributes across supported storage types. The results are presented as discrete table entities, enabling direct access or further exploration.

The implementation likely involves enhancements to the catalog’s indexing and search algorithms, ensuring efficient retrieval and accurate matching for both table and column-level queries. The search interface is updated to support these new criteria, providing a seamless user experience.

**Use Cases and Application Scenarios**  
- **Data Analysts and BI Developers:** Quickly locate tables relevant to their reporting needs by searching for specific column names or table descriptions.
- **Data Engineers:** Identify tables across lakehouses, semantic models, and mirrored databases for integration, ETL, or migration tasks.
- **Compliance and Governance Teams:** Efficiently discover tables containing sensitive columns (e.g., “SSN”) for audit or regulatory purposes.
- **Application Developers:** Find tables with specific schema attributes required for application logic or API integration.

**Important Considerations and Limitations**  
- The update is effective from October 15, 2026; prior to this date, table-level search may not be available.
- Search results are limited to tables from semantic models, lakehouses, and mirrored databases; other asset types may not be included.
- Exact column-name match is supported, but partial matches or advanced filtering capabilities are not specified.
- The update does not detail access control or security implications; users should ensure appropriate permissions are enforced for table discovery.

**Integration with Related Azure Services**  
The enhanced table discovery is tightly integrated with Microsoft Fabric and OneLake, which are foundational components for unified analytics in Azure. This update improves interoperability with Power BI, Azure Synapse, and other analytics tools by simplifying the process of finding and utilizing tables within the broader Azure data ecosystem. It supports streamlined data asset management and enhances the discoverability of tables for downstream Azure services and workflows.

**Summary Sentence**  
Starting October 15, 2026, Microsoft Fabric’s OneLake Catalog search will allow users to discover tables from semantic models, lakehouses, and mirrored databases by table name, description, or exact column-name match, significantly improving data asset discoverability and search precision across the Azure analytics landscape.

---

### 4. Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)

**Published**: October 05, 2026 17:44:31 UTC
**Link**: [Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)](https://azure.microsoft.com/updates?id=573425)

**Update ID**: 573425
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Storage, Databases, Hybrid + multicloud, Azure Backup, Azure Database for PostgreSQL, Feature

**Summary**:

- **What was updated**  
Azure Backup now supports public preview for PostgreSQL Flexible Server and Elastic Cluster (v2).

- **Key changes or new features**  
  - Enterprise-grade long-term retention for PostgreSQL databases.
  - Physical backups are created from managed disk snapshots.
  - Backups are securely vaulted in an Azure Backup vault, enabling centralized management and compliance.
  - Supports automated backup scheduling, retention policies, and point-in-time restore capabilities.
  - Enhanced data protection and disaster recovery for PostgreSQL workloads.

- **Target audience affected**  
  - Developers and database administrators using Azure Database for PostgreSQL Flexible Server or Elastic Cluster (v2).
  - IT professionals responsible for data protection, backup, and compliance in Azure environments.

- **Important notes**  
  - This feature is currently in public preview and may not be suitable for production workloads.
  - Integration with Azure Backup vault enables unified backup management across multiple data sources.
  - Review preview limitations and regional availability before adoption.
  - For more details, refer to the [official update](https://azure.microsoft.com/updates?id=573425).

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Backup for PostgreSQL flexible server and elastic cluster (v2)  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=573425)

---

**Background and Purpose of the Update**  
Azure Backup for PostgreSQL flexible server and elastic cluster (v2) enters public preview to address enterprise requirements for robust, long-term data retention and protection. The update is designed to enhance the backup and recovery capabilities for PostgreSQL workloads hosted on Azure, ensuring compliance, business continuity, and disaster recovery for mission-critical databases.

**Specific Features and Detailed Changes**  
- **Enterprise-Grade Long-Term Retention:** The update introduces support for extended backup retention periods, enabling organizations to meet regulatory and business requirements for data preservation.
- **Physical Backups via Managed Disk Snapshots:** Backups are now performed as physical snapshots of managed disks, providing a more reliable and consistent backup mechanism compared to logical backups.
- **Vaulted Storage in Azure Backup Vault:** Backup data is vaulted in an Azure Backup vault, offering secure, isolated, and scalable storage for backup copies. This separation enhances security and simplifies management.
- **Support for PostgreSQL Flexible Server and Elastic Cluster:** The update covers both single flexible server instances and elastic clusters, broadening the scope of supported PostgreSQL deployment models.

**Technical Mechanisms and Implementation Methods**  
- **Backup Process:** Physical backups are created by taking managed disk snapshots of the PostgreSQL server or cluster. These snapshots capture the entire disk state, ensuring point-in-time consistency and faster recovery.
- **Vault Integration:** Snapshots are transferred and stored in an Azure Backup vault, leveraging Azure’s built-in redundancy and security features. The vault acts as a centralized repository for backup management, retention policies, and recovery operations.
- **Retention Management:** Administrators can configure retention policies within the Azure Backup vault to control how long backups are preserved, aligning with organizational or regulatory requirements.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations needing to retain database backups for extended periods to comply with legal or industry regulations.
- **Disaster Recovery:** Enterprises seeking reliable recovery options for PostgreSQL databases in the event of accidental deletion, corruption, or infrastructure failure.
- **Business Continuity:** Businesses requiring consistent and secure backup solutions to ensure uninterrupted operations and rapid restoration of services.
- **Multi-Instance and Cluster Protection:** Environments utilizing PostgreSQL elastic clusters benefit from scalable backup and recovery across multiple nodes.

**Important Considerations and Limitations**  
- **Preview Limitations:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate the feature in test environments and review Azure’s preview terms.
- **Backup Type:** Only physical backups via disk snapshots are supported; logical backups or custom backup scripts may not be integrated.
- **Retention Policy Configuration:** Proper configuration of retention policies is essential to avoid unnecessary storage costs or compliance risks.
- **Vault Storage Costs:** Storing backups in Azure Backup vault incurs additional costs based on storage consumption and retention duration.

**Integration with Related Azure Services**  
- **Azure Backup Vault:** The solution is tightly integrated with Azure Backup vault, enabling centralized backup management, monitoring, and policy enforcement.
- **PostgreSQL Flexible Server and Elastic Cluster:** Direct support for these deployment models ensures seamless backup and recovery operations within Azure’s managed PostgreSQL ecosystem.
- **Azure Security and Compliance:** Vaulted backups benefit from Azure’s security features, including encryption at rest and access controls, supporting compliance with data protection standards.

---

**Summary Sentence:**  
Azure Backup for PostgreSQL flexible server and elastic cluster (v2) public preview introduces enterprise-grade, long-term retention using physical managed disk snapshots vaulted in Azure Backup, enhancing data protection and compliance for PostgreSQL workloads on Azure.

---

### 5. Public Preview: IPv6 Support for Application Gateway WAF 

**Published**: October 05, 2026 17:41:41 UTC
**Link**: [Public Preview: IPv6 Support for Application Gateway WAF ](https://azure.microsoft.com/updates?id=573861)

**Update ID**: 573861
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Web Application Firewall, Features

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) now supports IPv6 traffic in Public Preview.

- Key changes or new features  
  - Application Gateway WAF can now inspect and enforce security policies for both IPv4 and IPv6 traffic.  
  - This enables organizations to support dual-stack (IPv4/IPv6) applications and modernize their network infrastructure.  
  - IPv6 support applies to both frontend and backend configurations, allowing end-to-end IPv6 connectivity through the Application Gateway.

- Target audience affected  
  - Developers and IT professionals managing web applications behind Azure Application Gateway WAF.  
  - Organizations planning to migrate to or support IPv6 traffic in their applications.

- Important notes if any  
  - This feature is currently in Public Preview and may not be recommended for production workloads.  
  - Users should test IPv6 configurations and monitor for any issues during the preview phase.  
  - For more details and limitations, refer to the official documentation and the Azure Updates page: https://azure.microsoft.com/updates?id=573861

**Details**:

**Azure Update Technical Report: Public Preview – IPv6 Support for Application Gateway WAF**

**Background and Purpose of the Update**  
The Public Preview of IPv6 support for Application Gateway Web Application Firewall (WAF) addresses the growing need for modern network architectures to accommodate IPv6 traffic. As organizations expand their cloud presence and global reach, IPv6 adoption is increasing due to its larger address space and improved network efficiency. This update aims to modernize the Application Gateway platform by enabling inspection and enforcement of IPv6 traffic, ensuring that security controls remain effective as network protocols evolve.

**Specific Features and Detailed Changes**  
With this update, Application Gateway WAF can now process, inspect, and enforce security policies on IPv6 traffic. Previously, WAF functionality was limited to IPv4, restricting organizations from fully leveraging dual-stack or IPv6-only deployments. The Public Preview introduces the following changes:
- Support for IPv6 endpoints on Application Gateway WAF.
- Inspection of inbound IPv6 traffic for web applications.
- Enforcement of WAF rules and policies on IPv6 requests.
- Logging and monitoring capabilities extended to IPv6 traffic.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages Azure’s underlying dual-stack networking capabilities. Application Gateway instances can now be configured with IPv6 frontend IP addresses, allowing them to accept traffic from both IPv4 and IPv6 clients. The WAF engine applies the same rule sets and inspection logic to IPv6 packets as it does for IPv4, ensuring consistent security posture across both protocols. Configuration is managed through Azure Resource Manager templates, the Azure Portal, or CLI, where users can specify IPv6 frontend IPs during gateway setup or modification.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations:
- Migrating workloads to IPv6 or operating in environments where IPv6 is mandated (e.g., government or global enterprises).
- Deploying web applications that must be accessible to IPv6-only clients, such as mobile networks or regions with limited IPv4 availability.
- Implementing dual-stack architectures to future-proof their infrastructure.
- Ensuring compliance with security standards that require inspection of all inbound traffic, regardless of protocol.

**Important Considerations and Limitations**  
As this feature is in Public Preview, it may not be suitable for production workloads requiring full SLA guarantees. Users should:
- Review documentation for any feature gaps or unsupported scenarios during the preview phase.
- Test IPv6 WAF configurations in non-production environments to validate compatibility and performance.
- Monitor for updates regarding general availability and expanded support.
- Be aware that integration with existing monitoring and logging systems may require updates to capture IPv6-specific data.

**Integration with Related Azure Services**  
IPv6 support for Application Gateway WAF enhances integration with other Azure networking services, including:
- Azure Virtual Networks, which support IPv6 addressing.
- Azure Front Door and Azure Traffic Manager, which can route IPv6 traffic to Application Gateway.
- Azure Monitor and Log Analytics, which can now track IPv6 traffic metrics and security events.

**Summary Sentence**  
The Public Preview of IPv6 support for Application Gateway WAF enables inspection and enforcement of IPv6 traffic, modernizing Azure’s web application security platform and supporting dual-stack network architectures for evolving enterprise requirements.

---


*This report was automatically generated - 2026-10-06 03:03:43 UTC*