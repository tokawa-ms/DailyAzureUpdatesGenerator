# September 11, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 11, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 8 items

## Update List

### 1. Generally Available: Azure Databricks automatic identity management

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Generally Available: Azure Databricks automatic identity management](https://azure.microsoft.com/updates?id=502633)

**Update ID**: 502633
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks now supports automatic identity management, generally available for production use.

- Key changes or new features  
This feature enables automated user provisioning and deprovisioning by integrating Azure Databricks directly with Microsoft Entra (formerly Azure AD). It streamlines identity lifecycle management by syncing user identities and access permissions without manual intervention, improving security and operational efficiency.

- Target audience affected  
Developers and IT professionals managing Azure Databricks workspaces and user access, especially those responsible for identity and access management in enterprise environments.

- Important notes if any  
This native integration reduces administrative overhead and helps maintain compliance by ensuring timely updates to user access. Organizations should review their Microsoft Entra configurations to leverage this capability fully. The feature is now generally available, indicating production readiness and support from Microsoft.  

For more details, visit: https://azure.microsoft.com/updates?id=502633

**Details**:

The recent general availability of Azure Databricks automatic identity management introduces a streamlined and automated approach to managing user identities within Azure Databricks workspaces by leveraging native integration with Microsoft Entra (formerly Azure Active Directory). This update addresses the complexity and operational overhead associated with manual user provisioning and deprovisioning, enabling IT teams to enforce consistent access controls and improve security posture through identity lifecycle automation.

**Background and Purpose:**  
Prior to this update, managing user access in Azure Databricks required manual configuration or custom scripting to synchronize identities and permissions, often leading to delays, errors, and inconsistent access policies. The purpose of this feature is to simplify identity lifecycle management by automating provisioning and deprovisioning processes directly through Microsoft Entra, ensuring that user access to Databricks resources aligns dynamically with their status in the organization’s identity directory.

**Specific Features and Detailed Changes:**  
- **Automated User Provisioning and Deprovisioning:** Users and groups defined in Microsoft Entra can now be automatically created, updated, or removed in Azure Databricks workspaces without manual intervention.  
- **Native Integration with Microsoft Entra:** This integration uses SCIM (System for Cross-domain Identity Management) 2.0 protocol, enabling standardized and secure synchronization of user identities and group memberships.  
- **Role and Permission Synchronization:** User roles assigned in Microsoft Entra can be mapped to corresponding Databricks workspace roles, ensuring appropriate access levels are enforced automatically.  
- **Audit and Compliance:** Changes to user access are logged, supporting compliance and governance requirements.

**Technical Mechanisms and Implementation Methods:**  
The implementation leverages Microsoft Entra’s provisioning service configured to connect to Azure Databricks via SCIM endpoints. IT administrators set up a provisioning connection in the Microsoft Entra portal, specifying the Azure Databricks workspace as the target application. The provisioning service periodically queries Microsoft Entra for user and group changes and pushes these updates to Databricks. Role mappings are configured through attribute mappings and transformation rules within Microsoft Entra, enabling granular control over access rights. Authentication continues to be managed via Azure AD SSO, while provisioning automates the lifecycle management of user accounts and group memberships inside Databricks.

**Use Cases and Application Scenarios:**  
- **Enterprise-scale User Management:** Organizations with large or frequently changing user bases can maintain up-to-date access without manual overhead.  
- **Onboarding and Offboarding Automation:** New hires gain immediate access to required Databricks resources, and departing employees’ access is revoked promptly, reducing security risks.  
- **Compliance and Governance:** Automated provisioning supports audit trails and enforces least privilege access policies consistently.  
- **Multi-team Collaboration:** Different teams can be assigned appropriate roles via group memberships managed centrally in Microsoft Entra.

**Important Considerations and Limitations:**  
- The feature requires an Azure Databricks workspace configured to support SCIM provisioning and Microsoft Entra tenant with appropriate permissions.  
- Role mapping must be carefully planned to align Microsoft Entra groups and roles with Databricks workspace roles to avoid privilege escalation or access gaps.  
- Provisioning cycles are periodic (typically every 40 minutes), so changes are not instantaneous.  
- Custom roles or complex permission models in Databricks may require additional configuration or manual adjustments.  
- Existing manual user management workflows should be reviewed to prevent conflicts with automated provisioning.

**Integration with Related Azure Services:**  
- **Microsoft Entra (Azure AD):** Core identity provider and provisioning orchestrator.  
- **Azure Databricks:** Target platform for identity synchronization and role enforcement.  
- **Azure Monitor and Azure Log Analytics:** Can be used to monitor provisioning logs and audit user lifecycle events.  
- **Azure Policy and Azure Security Center:** Complementary services to enforce security policies and monitor compliance related to identity and access management.

In summary, the GA release of Azure Databricks automatic identity management significantly enhances operational efficiency and security by automating user lifecycle

---

### 2. Generally Available: Azure Database for PostgreSQL flexible server in Austria East and Chile Central 

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL flexible server in Austria East and Chile Central ](https://azure.microsoft.com/updates?id=502009)

**Update ID**: 502009
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL flexible server is now generally available in the Austria East and Chile Central regions.

- Key changes or new features  
Developers and IT professionals can deploy and manage PostgreSQL flexible servers closer to their users in these new geographic locations, improving latency and compliance with data residency requirements. This expansion supports high availability, scaling, and cost optimization features inherent to the flexible server deployment option.

- Target audience affected  
Developers building applications requiring PostgreSQL databases, database administrators, and IT professionals managing cloud infrastructure in Austria, Chile, or nearby regions.

- Important notes if any  
Ensure to evaluate region-specific service availability and pricing. Migrating or deploying new workloads in these regions can enhance performance and meet local data sovereignty regulations. For detailed configuration and best practices, refer to the official Azure documentation.

**Details**:

The Azure update announces the general availability of Azure Database for PostgreSQL Flexible Server in the Austria East and Chile Central regions, enabling customers to deploy fully managed PostgreSQL instances closer to their users in these geographies. This expansion supports Azure’s global footprint growth and addresses data residency, latency, and compliance requirements for organizations operating in or serving these regions.

**Background and Purpose:**  
Azure Database for PostgreSQL Flexible Server is a managed database service designed to provide greater control and flexibility over PostgreSQL deployments compared to the single server option. It offers customizable maintenance windows, high availability, and scaling options tailored for production workloads. By making Flexible Server available in Austria East and Chile Central, Microsoft aims to reduce latency for local users, comply with regional data sovereignty laws, and support disaster recovery strategies by enabling geo-distributed deployments.

**Specific Features and Detailed Changes:**  
The key change is the regional availability of Flexible Server in two new Azure data centers. This means customers can now provision PostgreSQL flexible servers with the same feature set—such as zone-redundant high availability, burstable and scalable compute tiers, and customizable maintenance schedules—in Austria East and Chile Central. The service supports PostgreSQL versions 11, 12, and 13, with built-in automated backups, point-in-time restore, and security features like Azure Active Directory integration and virtual network service endpoints.

**Technical Mechanisms and Implementation Methods:**  
Flexible Server uses a decoupled compute and storage architecture, allowing independent scaling of CPU/memory and storage resources. It supports zone-redundant high availability by replicating data synchronously across availability zones within the region, minimizing downtime during failures. Deployment is managed through the Azure Portal, CLI, ARM templates, or Terraform, enabling infrastructure as code practices. Networking options include public access with firewall rules and private access via Azure Private Link, ensuring secure connectivity. Automated backups leverage Azure Blob Storage, enabling point-in-time recovery within the configured retention period.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for enterprises and ISVs with customers or operations in Austria and Chile who require low-latency database access and compliance with regional data protection regulations such as GDPR or local privacy laws. Typical scenarios include ecommerce platforms, financial services applications, and SaaS solutions needing scalable, highly available PostgreSQL databases. Additionally, organizations implementing multi-region disaster recovery or data residency strategies can now include these regions in their architecture.

**Important Considerations and Limitations:**  
While the service is generally available, customers should verify PostgreSQL version support and feature parity with other regions, as some preview features may not yet be available. Network latency and throughput should be tested to ensure performance meets application requirements. Pricing may vary by region, so budgeting should account for regional cost differences. Also, customers must configure high availability and backups according to their SLA needs, as default settings may not suffice for all production workloads.

**Integration with Related Azure Services:**  
Flexible Server integrates seamlessly with Azure ecosystem components such as Azure App Service, Azure Kubernetes Service (AKS), and Azure Functions for building scalable applications. It supports Azure Monitor for performance metrics and alerts, Azure Security Center for vulnerability assessments, and Azure Active Directory for authentication and role-based access control. Additionally, it can be connected to Azure Data Factory or Azure Synapse Analytics for data integration and analytics workflows.

In summary, the general availability of Azure Database for PostgreSQL Flexible Server in Austria East and Chile Central enables organizations to deploy scalable, highly available PostgreSQL databases with flexible management capabilities closer to their users in these regions, supporting compliance, performance, and disaster recovery objectives while integrating with the broader Azure ecosystem.

---

### 3. Public Preview: Azure MySQL Self Heal

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Public Preview: Azure MySQL Self Heal](https://azure.microsoft.com/updates?id=501999)

**Update ID**: 501999
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Azure Database for MySQL – Flexible Server introduced a new Self-Heal feature, now available in Public Preview.

- Key changes or new features  
The Self-Heal capability enables automatic detection and proactive resolution of common server issues, such as unresponsiveness, without requiring users to open a support ticket. This reduces downtime and operational overhead by allowing the system to self-diagnose and remediate problems autonomously.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL – Flexible Server instances who seek improved reliability and reduced manual intervention in database maintenance.

- Important notes if any  
As this feature is in Public Preview, it should be used with caution in production environments. Users are encouraged to provide feedback to help improve the service before general availability. Detailed documentation and support guidelines are available on the Azure portal.

**Details**:

The Azure update titled "Public Preview: Azure MySQL Self Heal" introduces a proactive self-healing capability for Azure Database for MySQL – Flexible Server, designed to automatically detect and resolve common server issues without requiring users to open a support case. This feature is now available in public preview, enhancing operational resilience and reducing downtime for MySQL workloads hosted on Azure.

**Background and Purpose**  
Azure Database for MySQL – Flexible Server is a managed database service that provides high availability, scalability, and security for MySQL workloads. Despite these capabilities, transient or common server issues such as unresponsiveness, configuration anomalies, or resource contention can still impact service availability. Traditionally, resolving such issues often required manual intervention or support case escalation, leading to increased downtime and operational overhead. The Self-Heal feature aims to empower users with automated remediation tools that proactively identify and fix these issues, thereby improving service reliability and reducing the need for manual troubleshooting.

**Specific Features and Detailed Changes**  
- **Automated Issue Detection:** The Self-Heal feature continuously monitors server health metrics and operational logs to detect symptoms of common issues such as server unresponsiveness or degraded performance.  
- **Proactive Remediation:** Upon detecting an issue, the system triggers predefined remediation workflows that may include restarting the server, resetting configurations, or reallocating resources to restore normal operation.  
- **User Control and Transparency:** Users can initiate self-healing actions manually via the Azure portal or CLI, or configure automatic self-healing to run without user intervention. Detailed logs and status updates are provided to keep users informed about the actions taken.  
- **No Support Case Required:** By resolving common issues internally, the feature reduces dependency on Azure support, accelerating recovery times and minimizing disruption.

**Technical Mechanisms and Implementation Methods**  
The Self-Heal feature leverages Azure Monitor and built-in diagnostic telemetry to continuously assess the health of MySQL Flexible Servers. It uses a combination of health probes, error pattern recognition, and performance counters to identify anomalies. Once an issue is detected, Azure Resource Manager (ARM) templates and automation runbooks execute remediation steps, such as restarting the MySQL service or adjusting server parameters. The system is integrated with Azure Activity Logs to track all self-healing operations for audit and compliance purposes. This modular design allows extensibility for future enhancements and custom remediation workflows.

**Use Cases and Application Scenarios**  
- **Unresponsive Server Recovery:** Automatically restarting a MySQL Flexible Server instance that becomes unresponsive due to transient faults or resource exhaustion.  
- **Configuration Drift Correction:** Detecting and reverting configuration changes that negatively impact server stability or performance.  
- **Performance Degradation Mitigation:** Identifying and resolving issues caused by resource contention or suboptimal settings without manual intervention.  
- **Operational Efficiency:** Reducing the need for manual troubleshooting and support case submissions, enabling DBAs and DevOps teams to focus on higher-value tasks.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, Self-Heal may have limited SLA guarantees and could undergo changes before general availability. Users should test in non-production environments before broad adoption.  
- **Scope of Issues:** The feature currently targets common and well-understood issues; complex or rare failure scenarios may still require manual intervention or support engagement.  
- **User Permissions:** Appropriate Azure RBAC permissions are required to initiate or configure self-healing actions.  
- **Impact on Workloads:** Automated restarts or configuration changes may cause brief service interruptions; users should plan accordingly and inform stakeholders.

**Integration with Related Azure Services**  
- **Azure Monitor:** Provides the telemetry and alerting foundation for health monitoring and issue detection.  
- **Azure Automation:** Executes remediation runbooks triggered by the Self-Heal logic.  
- **Azure Activity Logs:** Records all self-healing operations for auditing and compliance tracking.  
- **Azure CLI and Portal:** Offer user interfaces for managing and invoking self-healing actions.  
-

---

### 4. Generally Available: Azure MySQL Extended Support 

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Generally Available: Azure MySQL Extended Support ](https://azure.microsoft.com/updates?id=501994)

**Update ID**: 501994
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Azure Database for MySQL – Flexible Server now offers Extended Support for MySQL versions reaching end-of-life, starting spring 2026.

- Key changes or new features  
Extended Support allows customers to continue running MySQL versions beyond their official end-of-life dates with security updates and critical fixes provided by Azure. This feature helps manage upgrade timelines more flexibly, reducing immediate pressure to migrate to newer MySQL versions. It supports smoother transitions and better operational continuity.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL Flexible Server instances, especially those with workloads on MySQL versions nearing or past end-of-life.

- Important notes if any  
Extended Support is designed to bridge the gap during upgrade planning but is not a permanent substitute for upgrading to supported MySQL versions. Customers should plan to upgrade eventually to benefit from full feature sets and long-term support. This update enhances compliance and security posture for legacy MySQL deployments on Azure.  

For detailed guidance and timelines, refer to the official Azure update page.

**Details**:

The Azure update titled "Generally Available: Azure MySQL Extended Support" introduces Extended Support for Azure Database for MySQL – Flexible Server, starting from spring 2026, enabling customers to manage MySQL version upgrade timelines with greater flexibility by continuing to receive security updates and critical fixes for MySQL versions that have reached their official end-of-life (EOL).

**Background and Purpose:**  
MySQL, as an open-source relational database, follows a defined lifecycle for each version, after which official vendor support and patches cease. This can pose operational and security risks for enterprises running legacy MySQL versions on Azure Database for MySQL – Flexible Server. The update addresses this challenge by offering Extended Support, allowing customers to defer immediate upgrades while maintaining compliance and security. This is especially critical for organizations with complex application dependencies or regulatory requirements that delay rapid version migration.

**Specific Features and Detailed Changes:**  
- **Extended Security Updates (ESU):** Azure will provide security patches and critical bug fixes for MySQL versions that have reached EOL, specifically for Flexible Server deployments.  
- **Supported Versions:** Initially, this applies to MySQL versions approaching or past their official support end date starting spring 2026.  
- **Flexible Upgrade Scheduling:** Customers gain additional time to plan and execute version upgrades without compromising security posture.  
- **Seamless Integration:** Extended Support is integrated into the existing Azure Database for MySQL – Flexible Server management experience, with no need for manual patching by customers.  
- **Automatic Patch Deployment:** Security updates are applied automatically by Azure, reducing operational overhead.

**Technical Mechanisms and Implementation Methods:**  
Microsoft will maintain forked versions of MySQL binaries for the supported EOL versions, backporting security fixes and critical patches from newer MySQL releases or independently developed fixes. These patches are tested and validated within Azure’s managed environment to ensure stability and compatibility. The Azure platform automates the deployment of these updates to Flexible Server instances enrolled in Extended Support, leveraging Azure’s control plane and update orchestration frameworks. Customers continue to manage their servers via Azure Portal, CLI, or ARM templates without changes to existing workflows.

**Use Cases and Application Scenarios:**  
- Enterprises with legacy applications that depend on specific MySQL versions and cannot upgrade immediately due to application compatibility or testing constraints.  
- Regulated industries requiring continuous security compliance but facing lengthy validation cycles for database upgrades.  
- Organizations undergoing cloud migration or modernization projects that want to decouple upgrade timing from migration schedules.  
- Managed service providers supporting multiple clients with heterogeneous MySQL versions seeking to minimize downtime and risk during version transitions.

**Important Considerations and Limitations:**  
- Extended Support is limited to security and critical fixes; it does not include new features or performance improvements.  
- Customers should view Extended Support as a temporary measure, not a permanent alternative to upgrading.  
- Pricing and licensing details for Extended Support may differ from standard support and should be reviewed in the Azure pricing documentation.  
- Not all MySQL versions may be eligible; customers must verify version support timelines.  
- Extended Support is currently available only for Flexible Server deployment model, not for Single Server or other MySQL deployment types on Azure.

**Integration with Related Azure Services:**  
- **Azure Monitor and Azure Security Center:** Extended Support updates integrate with Azure monitoring and security tools, enabling alerting on patch status and compliance.  
- **Azure Automation:** Customers can incorporate Extended Support patching status into automation workflows for operational governance.  
- **Azure Backup:** Ensures that backup and restore operations remain consistent with the patched database versions.  
- **Azure Policy:** Organizations can enforce policies to require Extended Support enrollment or mandate upgrade timelines.

In summary, Azure’s Generally Available Extended Support for MySQL Flexible Server empowers IT professionals to maintain secure, compliant MySQL deployments beyond official vendor support end dates by providing managed security updates, thereby reducing operational risks and enabling more controlled upgrade planning within Azure’s fully managed database platform.

---

### 5. Generally Available: Azure Database for MySQL 8.4 

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Generally Available: Azure Database for MySQL 8.4 ](https://azure.microsoft.com/updates?id=501989)

**Update ID**: 501989
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Azure Database for MySQL – Flexible Server has reached general availability for version 8.4.

- Key changes or new features  
This release enables creation of new MySQL 8.4 servers optimized for production workloads. It includes the latest MySQL 8.4 features, performance improvements, and security enhancements. Developers can leverage improved query performance and new MySQL functionalities to build scalable applications. IT professionals benefit from enhanced manageability and reliability for database operations.

- Target audience affected  
Developers building applications on MySQL, database administrators, and IT professionals managing Azure Database for MySQL deployments.

- Important notes if any  
Existing servers running earlier MySQL versions need to be upgraded to 8.4 to access these new capabilities. It is recommended to test workloads on MySQL 8.4 in non-production environments before migrating production databases. For detailed upgrade guidance and feature lists, refer to the official Azure documentation.  

Link: https://azure.microsoft.com/updates?id=501989

**Details**:

The general availability of Azure Database for MySQL – Flexible Server version 8.4 marks a significant update enabling IT professionals to deploy MySQL 8.4 instances on Azure for production workloads, leveraging the latest MySQL enhancements alongside Azure’s managed database capabilities. This update addresses the need for modernized database engines that deliver improved performance, security, and feature sets aligned with evolving application demands.

**Background and Purpose:**  
Azure Database for MySQL – Flexible Server is a managed database service designed to provide high availability, scalability, and operational flexibility for MySQL workloads on Azure. The release of version 8.4 aligns with the upstream MySQL community’s latest stable release, aiming to offer users access to new database features, improved query performance, and enhanced security. This update helps organizations modernize their data infrastructure by adopting the newest MySQL version without the overhead of manual upgrades or complex migrations.

**Specific Features and Detailed Changes:**  
MySQL 8.4 introduces several key improvements over previous versions, including enhanced JSON functionality, improved optimizer features, and better replication capabilities. Notable features include:  
- **Enhanced JSON support:** New functions and operators for more efficient and flexible JSON data manipulation.  
- **Improved query optimizer:** Smarter execution plans that reduce latency and resource consumption.  
- **Replication enhancements:** More robust and flexible replication options, including better support for multi-source replication and group replication.  
- **Security improvements:** Strengthened default authentication plugins and encryption options.  
- **Performance enhancements:** Optimizations in indexing, caching, and concurrency control to support high-throughput workloads.

Azure’s Flexible Server deployment model complements these features by offering zone-redundant high availability, customizable maintenance windows, and burstable compute tiers, enabling fine-tuned resource allocation and operational control.

**Technical Mechanisms and Implementation Methods:**  
The Flexible Server architecture uses a decoupled compute and storage model, allowing independent scaling and maintenance. Upon creating a MySQL 8.4 Flexible Server instance, Azure provisions a managed environment with automated backups, patching, and monitoring integrated into the Azure portal and CLI. The service supports VNet integration for secure network isolation and private endpoint connectivity. Users can configure server parameters and extensions through Azure Resource Manager templates or the Azure CLI, facilitating infrastructure-as-code deployments.

**Use Cases and Application Scenarios:**  
This update is ideal for cloud-native applications requiring a relational database with advanced JSON handling, such as content management systems, e-commerce platforms, and IoT data ingestion services. Enterprises modernizing legacy MySQL workloads can leverage the improved replication and high availability features for disaster recovery and geo-distributed applications. The flexible compute options suit variable workloads, including development/test environments and production systems with fluctuating demand.

**Important Considerations and Limitations:**  
While MySQL 8.4 brings many enhancements, IT professionals should validate application compatibility, especially for custom plugins or deprecated features from earlier MySQL versions. Migration from older Azure Database for MySQL versions or on-premises MySQL instances requires careful planning to avoid downtime. Certain advanced MySQL features may have limited support or require configuration adjustments in the managed environment. Additionally, cost implications of higher compute tiers and zone-redundant deployments should be evaluated against workload requirements.

**Integration with Related Azure Services:**  
Azure Database for MySQL 8.4 integrates seamlessly with Azure ecosystem components such as Azure Data Factory for data orchestration, Azure Monitor for telemetry and alerting, and Azure Security Center for threat detection and compliance. It supports Azure Private Link for secure connectivity and can be paired with Azure App Service or Azure Kubernetes Service for scalable application hosting. Backup and restore operations integrate with Azure Blob Storage, enabling long-term retention and disaster recovery strategies.

In summary, the general availability of Azure Database for MySQL Flexible Server 8.4 empowers IT professionals to deploy the latest MySQL version with Azure’s managed service benefits, enhancing performance, security, and operational flexibility for diverse production workloads while maintaining tight integration within

---

### 6. Generally Available: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key 

**Published**: September 10, 2025 21:30:10 UTC
**Link**: [Generally Available: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key ](https://azure.microsoft.com/updates?id=501980)

**Update ID**: 501980
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Azure Cosmos DB for MongoDB (vCore) clusters now support encryption using customer-managed keys (CMK) in addition to the existing service-managed key (SMK) encryption.

- Key changes or new features  
Developers and IT professionals can configure their Cosmos DB for MongoDB (vCore) clusters to use Azure Key Vault keys for encryption at rest, providing enhanced control over encryption keys. This feature enables double encryption layering and key rotation management, improving data security and compliance posture. The integration is seamless and does not impact application connectivity or performance.

- Target audience affected  
This update primarily affects developers, database administrators, and IT security professionals managing Azure Cosmos DB for MongoDB (vCore) workloads who require advanced encryption controls and compliance with organizational or regulatory key management policies.

- Important notes if any  
Using customer-managed keys requires appropriate Azure Key Vault setup and permissions. Transitioning to CMK encryption should be planned to avoid disruptions. Service-managed encryption remains the default and fallback option. This feature is generally available, indicating full support and SLA coverage from Microsoft.

For more details, visit: https://azure.microsoft.com/updates?id=501980

**Details**:

The recent general availability of customer-managed key (CMK) encryption for Azure Cosmos DB for MongoDB (vCore) clusters enhances data security by allowing IT professionals to control encryption keys beyond the default service-managed keys (SMK). Previously, data at rest in Cosmos DB for MongoDB (vCore) was encrypted transparently using Microsoft-managed keys, providing strong baseline protection. This update introduces the capability to use Azure Key Vault to manage your own encryption keys, enabling an additional layer of security and compliance control aligned with organizational policies and regulatory requirements.

**Background and Purpose:**  
Azure Cosmos DB for MongoDB (vCore) is a fully managed NoSQL database service that supports MongoDB workloads with predictable pricing and scalability. While Microsoft-managed encryption keys ensure data is encrypted at rest, some organizations require direct control over encryption keys to meet stringent compliance mandates such as GDPR, HIPAA, or industry-specific standards. Customer-managed keys empower organizations to enforce key lifecycle management, including rotation, revocation, and auditing, thereby enhancing data sovereignty and security posture.

**Specific Features and Detailed Changes:**  
- **Customer-Managed Key Encryption:** Users can now configure their Cosmos DB for MongoDB (vCore) accounts to use CMK stored in Azure Key Vault instead of relying solely on Microsoft-managed keys.  
- **Seamless Integration:** This capability is integrated into the existing encryption-at-rest framework, ensuring no disruption to ongoing operations or performance degradation.  
- **Key Vault Support:** Supports integration with Azure Key Vault, including managed HSM or software-protected keys, providing flexibility in key management and compliance.  
- **Key Rotation and Revocation:** Users can rotate keys or revoke access through Key Vault without downtime, maintaining continuous encryption protection.  
- **Audit and Monitoring:** Key Vault integration enables detailed logging and auditing of key usage via Azure Monitor and Azure Security Center.

**Technical Mechanisms and Implementation Methods:**  
When CMK encryption is enabled, Cosmos DB encrypts data at rest using a data encryption key (DEK) that is itself encrypted with the customer’s key stored in Azure Key Vault (the key encryption key, KEK). The KEK is never stored in Cosmos DB; instead, Cosmos DB requests access to the KEK from Key Vault during encryption and decryption operations. This envelope encryption model ensures that data remains encrypted with keys controlled by the customer. To enable CMK, administrators configure the Cosmos DB account with the Key Vault key URI and assign appropriate permissions (get, wrapKey, unwrapKey) to Cosmos DB’s managed identity in Azure AD. The encryption process is transparent to applications and does not require code changes.

**Use Cases and Application Scenarios:**  
- **Compliance-Driven Environments:** Organizations subject to regulations requiring customer control over encryption keys can meet these requirements by enabling CMK.  
- **Enhanced Security Posture:** Enterprises seeking defense-in-depth strategies can layer CMK encryption atop Microsoft-managed encryption.  
- **Key Lifecycle Management:** Organizations needing to enforce strict key rotation policies or immediate key revocation in case of compromise benefit from this feature.  
- **Multi-Tenant or Sensitive Data Workloads:** Scenarios where separation of duties or data sovereignty is critical can leverage CMK to ensure keys remain under customer control.

**Important Considerations and Limitations:**  
- **Initial Setup Complexity:** Enabling CMK requires proper configuration of Azure Key Vault, including key creation, access policies, and assigning managed identities, which may require coordination between security and cloud teams.  
- **Potential for Service Disruption:** Misconfiguration or revocation of Key Vault permissions can lead to Cosmos DB service interruptions; therefore, careful management and monitoring are essential.  
- **Supported Regions and SKUs:** CMK support is currently available for Azure Cosmos DB for MongoDB (vCore) clusters and may have regional availability constraints; verify support in your deployment region.  
- **No Impact on Data in Transit:** CMK encryption applies only to data at rest; data in transit

---

### 7. Public Preview: File share centric management model (Microsoft.FileShares) for Azure Files

**Published**: September 10, 2025 19:30:42 UTC
**Link**: [Public Preview: File share centric management model (Microsoft.FileShares) for Azure Files](https://azure.microsoft.com/updates?id=503096)

**Update ID**: 503096
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Files, Features

**Summary**:

- What was updated  
Azure Files introduced a new file share-centric management model via the Microsoft.FileShares resource provider, now available in public preview.

- Key changes or new features  
File shares are promoted to top-level Azure resources, enabling more straightforward creation, management, and organization of file shares independently from storage accounts. This model simplifies API interactions and resource management by allowing direct operations on file shares without navigating through storage account hierarchies.

- Target audience affected  
Developers and IT professionals managing Azure Files, especially those automating file share provisioning and lifecycle management through APIs or Infrastructure as Code (IaC) tools.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should review updated API documentation and consider potential impacts on existing automation scripts or tools that assume the previous storage account-centric model. Feedback during the preview phase is encouraged to help improve the final release.

**Details**:

The recent Azure update introduces a public preview of a file share-centric management model for Azure Files, implemented via the new Microsoft.FileShares resource provider. This enhancement aims to streamline and modernize the way IT professionals create, manage, and organize file shares within Azure, elevating file shares to first-class, top-level resources in the Azure Resource Manager (ARM) hierarchy.

**Background and Purpose**  
Previously, Azure Files management was tightly coupled with storage accounts, where file shares existed as subordinate resources under storage accounts. This hierarchical model often complicated management tasks such as applying policies, monitoring, or automating workflows specifically targeting file shares. The update addresses these challenges by decoupling file shares from their storage accounts in terms of resource management, enabling more granular control, improved clarity, and simplified automation.

**Specific Features and Detailed Changes**  
- **File Share as a Top-Level Resource:** File shares are now represented as independent ARM resources under the Microsoft.FileShares resource provider, rather than nested within storage accounts.  
- **Direct Resource Management:** Users can create, update, delete, and manage file shares directly via ARM templates, Azure CLI, PowerShell, and REST APIs targeting Microsoft.FileShares.  
- **Improved Resource Organization:** This model allows tagging, role-based access control (RBAC), and policy application directly at the file share level, enhancing governance and security.  
- **Simplified Automation:** The decoupling facilitates more straightforward scripting and automation workflows, as file shares can be addressed explicitly without navigating through storage account resource structures.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages the ARM framework by introducing a new resource provider namespace, Microsoft.FileShares. Under this namespace, file shares are defined as first-class resources with their own resource IDs, properties, and lifecycle management. The resource provider abstracts the underlying storage account association but maintains the linkage implicitly to ensure data integrity and performance. This means that while file shares appear independently in ARM, they still reside physically within storage accounts, preserving compatibility and performance characteristics.

Management operations are exposed via updated ARM APIs, CLI commands, and PowerShell modules that target Microsoft.FileShares resources. The resource provider handles orchestration behind the scenes, mapping operations to the appropriate storage account and file share endpoints.

**Use Cases and Application Scenarios**  
- **Granular Access Control:** Enterprises can assign RBAC roles specifically to file shares, enabling precise permission management without granting broader storage account access.  
- **Policy Enforcement:** Azure Policy can be applied directly to file shares for compliance, auditing, or cost management purposes.  
- **Simplified DevOps Pipelines:** Infrastructure as Code (IaC) templates can now declare file shares as standalone resources, simplifying deployment scripts and reducing complexity.  
- **Resource Organization:** Tagging file shares individually allows for better resource tracking, billing, and lifecycle management.  
- **Multi-Tenant Environments:** Service providers managing multiple clients can isolate file share management per tenant more effectively.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview, the feature may have limited SLA guarantees and could undergo changes before general availability.  
- **Compatibility:** Existing scripts and tools targeting storage account–scoped file shares may require updates to leverage the new model.  
- **Resource Quotas:** File share quotas and limits remain governed by the underlying storage account constraints.  
- **Billing and Metrics:** Billing continues to be associated with storage accounts; the new model does not change the billing structure.  
- **Migration:** Existing file shares are not automatically migrated to the new resource model; management via Microsoft.FileShares applies to new shares created under this model.

**Integration with Related Azure Services**  
- **Azure Policy:** Direct application of policies on file shares enhances governance.  
- **Azure RBAC:** Enables fine-grained access control at the file share level.  
- **Azure Monitor:** Improved resource granularity allows more targeted monitoring and alerting.  
- **Azure DevOps

---

### 8. Generally Available: Azure D192 Sizes in the Azure Dsv6 and Ddsv6-series VM Families

**Published**: September 10, 2025 15:15:43 UTC
**Link**: [Generally Available: Azure D192 Sizes in the Azure Dsv6 and Ddsv6-series VM Families](https://azure.microsoft.com/updates?id=503049)

**Update ID**: 503049
**Data source**: Azure Updates API

**Categories**: Launched, Services

**Summary**:

- What was updated  
Azure has introduced the D192 VM size to the Dsv6 and Ddsv6-series virtual machine families. These VM families are powered by the 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processors.

- Key changes or new features  
The new D192 size offers a higher compute capacity within the Dsv6 and Ddsv6-series, enabling workloads that require significant CPU and memory resources. Dsv6-series VMs continue to support Azure managed disks exclusively, while Ddsv6-series VMs support both Azure managed disks and ephemeral OS disks, providing flexibility in storage options and performance. This addition enhances the scalability options for compute-intensive applications.

- Target audience affected  
Developers and IT professionals managing high-performance computing, large-scale enterprise applications, or memory-intensive workloads will benefit from this update. It is particularly relevant for those optimizing VM sizing for cost and performance on Azure.

- Important notes if any  
Users should consider the storage differences between Dsv6 (managed disks only) and Ddsv6 (managed and ephemeral disks) when selecting the VM size. The D192 size availability may vary by region, so checking regional availability before deployment is recommended. This update aligns with Azure’s ongoing efforts to provide more powerful and flexible VM options based on the latest Intel processor technology.

**Details**:

The recent Azure update announces the general availability of the D192 VM size within the Azure Dsv6 and Ddsv6-series virtual machine families, which are powered by the 5th Generation Intel® Xeon® Platinum 8573C (Emerald Rapids) processors. This enhancement expands the compute options available in these VM families, designed to deliver high performance and scalability for demanding enterprise workloads.

**Background and Purpose**  
The Dsv6 and Ddsv6-series VMs represent Azure’s latest generation of general-purpose and storage-optimized virtual machines, respectively, leveraging the advanced capabilities of the Intel Emerald Rapids CPU architecture. Prior to this update, these series offered a range of VM sizes optimized for balanced CPU, memory, and storage throughput. The introduction of the D192 size addresses the need for larger-scale compute instances within these families, enabling customers to run more intensive workloads that require substantial CPU cores and memory capacity without switching to a different VM family.

**Specific Features and Detailed Changes**  
The D192 VM size provides 192 vCPUs and a proportional amount of memory, typically maintaining the Dsv6-series memory-to-vCPU ratio of 8 GiB per vCPU, resulting in approximately 1.5 TiB of RAM. This VM size is available in both Dsv6-series (which supports only Azure managed disks) and Ddsv6-series (which supports premium storage and is optimized for disk throughput). The underlying Intel® Xeon® Platinum 8573C processor delivers improved performance per core, enhanced security features such as Intel SGX and Total Memory Encryption, and better energy efficiency compared to previous generations.

**Technical Mechanisms and Implementation Methods**  
The D192 size is implemented by scaling out the number of CPU cores and memory modules on the Azure host hardware that supports the Dsv6 and Ddsv6 VM families. These VMs utilize Azure’s hypervisor technology to allocate the 192 vCPUs as virtualized cores mapped to physical cores on the Emerald Rapids processors. The VMs exclusively use Azure managed disks to ensure high availability, durability, and integration with Azure storage features such as snapshots and backups. The Ddsv6-series additionally supports premium SSDs and ultra disks, enabling high IOPS and throughput for storage-intensive applications.

**Use Cases and Application Scenarios**  
The D192 VM size is ideal for large-scale enterprise applications requiring massive parallel processing capabilities, such as big data analytics, in-memory databases (e.g., SAP HANA), high-performance computing (HPC) workloads, and large-scale virtualization hosts. It also suits scenarios involving extensive data caching, real-time analytics, and AI model training where both high CPU count and large memory capacity are critical. The availability of this size within the Dsv6 and Ddsv6 families allows customers to maintain consistency in VM features and management while scaling up resources.

**Important Considerations and Limitations**  
While the D192 size offers significant compute power, users should consider the associated cost implications and ensure their workloads can efficiently utilize the high number of vCPUs and memory. Additionally, these VMs require deployment in Azure regions that support the Dsv6 and Ddsv6-series with the D192 size, which may not be universally available. The Dsv6-series VMs only support Azure managed disks, so legacy unmanaged disks or other storage types are not compatible. Network bandwidth and throughput limits should also be reviewed to ensure they meet workload requirements at this scale.

**Integration with Related Azure Services**  
The D192 VMs integrate seamlessly with Azure services such as Azure Monitor for performance and health monitoring, Azure Backup for data protection, and Azure Security Center for threat detection and compliance. They can be deployed within Azure Virtual Networks (VNets) for secure connectivity and can leverage Azure Load Balancer or Application Gateway for traffic distribution. Additionally, these VMs support Azure Hybrid Benefit and Azure Reserved Instances for cost optimization. For storage-optimized Ddsv6-series V

---


*This report was automatically generated - 2025-09-11 03:03:40 UTC*