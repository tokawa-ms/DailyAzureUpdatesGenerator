# August 14, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 14, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: Azure Managed Instance for Apache Cassandra v5.0

**Published**: August 13, 2025 16:00:27 UTC
**Link**: [Public Preview: Azure Managed Instance for Apache Cassandra v5.0](https://azure.microsoft.com/updates?id=499753)

**Update ID**: 499753
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure Managed Instance for Apache Cassandra, Features

**Summary**:

- What was updated  
Azure Managed Instance for Apache Cassandra now supports Cassandra version 5.0, available in public preview.

- Key changes or new features  
This update enables developers and IT professionals to leverage the latest Cassandra 5.0 capabilities, including improved performance optimizations and enhanced indexing features. Users benefit from these advancements without needing to manage the underlying infrastructure, as Azure handles deployment, scaling, and maintenance.

- Target audience affected  
Developers building scalable, distributed applications using Apache Cassandra and IT professionals responsible for managing Cassandra databases in Azure environments will find this update particularly relevant.

- Important notes if any  
Since this is a public preview release, users should consider it for testing and evaluation purposes before production deployment. Monitoring Azure updates for GA announcements and feature enhancements is recommended. For detailed documentation and migration guidance, refer to the official Azure Managed Instance for Apache Cassandra resources.

**Details**:

The Azure update announces the public preview availability of Azure Managed Instance for Apache Cassandra supporting version 5.0, enabling users to leverage the latest Apache Cassandra features within a fully managed environment on Azure.

Background and Purpose:
Apache Cassandra is a widely adopted distributed NoSQL database designed for high availability, scalability, and fault tolerance, commonly used for large-scale, mission-critical applications requiring fast writes and reads across multiple regions. Traditionally, managing Cassandra clusters involves significant operational overhead, including infrastructure provisioning, patching, scaling, and tuning. Azure Managed Instance for Apache Cassandra abstracts these complexities by providing a fully managed Cassandra service on Azure. The update to version 5.0 in public preview allows customers to access the newest Cassandra capabilities while benefiting from Azure’s managed service features, reducing operational burden and accelerating development.

Specific Features and Detailed Changes:
Cassandra 5.0 introduces several enhancements over previous versions, including improved performance optimizations, new indexing capabilities, and enhanced consistency and stability features. Key improvements include:
- Better performance through optimized compaction strategies and improved read/write path efficiencies.
- New indexing options such as SASI (SSTable-Attached Secondary Index) improvements and support for custom index implementations, enabling more flexible and efficient query patterns.
- Enhanced repair and streaming mechanisms that reduce resource consumption and improve cluster stability.
- Improved schema management and support for new CQL (Cassandra Query Language) features.
By upgrading Azure Managed Instance for Apache Cassandra to version 5.0, users gain access to these enhancements without manual cluster upgrades or downtime.

Technical Mechanisms and Implementation Methods:
Azure Managed Instance for Apache Cassandra is built on top of Azure infrastructure, providing automated provisioning, patching, scaling, and backup capabilities. The service abstracts the underlying virtual machines and storage, exposing a managed Cassandra endpoint compatible with Apache Cassandra clients and tools. With version 5.0 support, the managed instance runs the updated Cassandra binaries and leverages Azure’s monitoring and diagnostics integrations to provide telemetry and health insights. The service supports multi-region replication and automatic failover, ensuring high availability. Users interact with the service via standard CQL interfaces, and the service handles cluster management tasks such as node replacement, repair, and scaling transparently.

Use Cases and Application Scenarios:
This update is particularly beneficial for enterprises and developers building large-scale, globally distributed applications requiring low-latency access to large volumes of structured and semi-structured data. Typical use cases include:
- IoT telemetry ingestion and analytics, where Cassandra’s write-optimized architecture suits high-velocity data streams.
- Real-time personalization engines and recommendation systems that require fast read/write access.
- Financial services and retail applications needing high availability and fault tolerance.
- Gaming backends managing player state and session data at scale.
By using Azure Managed Instance for Apache Cassandra 5.0, organizations can focus on application logic rather than database management.

Important Considerations and Limitations:
As the service is in public preview, it may not yet have full SLA guarantees and could undergo changes before general availability. Users should evaluate the preview in non-production environments initially. Some advanced Cassandra features or custom configurations may not be supported in the managed environment. Additionally, integration with existing on-premises Cassandra clusters requires careful planning for data migration and compatibility. Monitoring and alerting capabilities are integrated but may require configuration to align with organizational standards.

Integration with Related Azure Services:
Azure Managed Instance for Apache Cassandra integrates seamlessly with other Azure services to provide a comprehensive data platform. For example:
- Azure Monitor and Azure Log Analytics enable detailed telemetry and diagnostics.
- Azure Data Factory and Azure Synapse Analytics facilitate data movement and analytics pipelines.
- Azure Active Directory integration supports role-based access control and security.
- Azure Virtual Network integration allows secure network isolation and connectivity.
- Backup and disaster recovery are managed via Azure Backup and geo-replication features.
This ecosystem integration simplifies building end-to-end solutions leveraging Cassandra’s capabilities within Azure.

In summary, the public preview of Azure Managed Instance for Apache Cassandra v5.0

---

### 2. Generally Available: Azure Database for PostgreSQL flexible server in Malaysia West

**Published**: August 13, 2025 16:00:27 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL flexible server in Malaysia West](https://azure.microsoft.com/updates?id=499679)

**Update ID**: 499679
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL flexible server is now generally available in the Malaysia West Azure region.

- Key changes or new features  
Developers and IT professionals can deploy fully managed PostgreSQL flexible servers closer to their users in Malaysia West, improving latency and compliance with local data residency requirements. This expansion supports high availability, automated backups, scaling options, and built-in security features consistent with other regions.

- Target audience affected  
Developers building applications requiring PostgreSQL databases, database administrators, and IT professionals managing cloud infrastructure in Southeast Asia, particularly those with data residency or latency considerations in Malaysia.

- Important notes if any  
Existing customers can leverage this new region for new deployments; however, migration of existing databases to Malaysia West will require standard data migration processes. Pricing and service SLAs are consistent with other flexible server regions. For detailed configuration and region-specific considerations, refer to the official Azure documentation.

**Details**:

The recent general availability of Azure Database for PostgreSQL flexible server in the Malaysia West region expands Azure’s global footprint, enabling customers in Southeast Asia to deploy managed PostgreSQL instances closer to their end users and data sources, thereby reducing latency and improving performance. This update addresses the growing demand for scalable, fully managed PostgreSQL database services in the Malaysia West region, supporting regional compliance and data residency requirements.

Azure Database for PostgreSQL flexible server is a managed database service that offers enhanced control and flexibility over database configuration, maintenance windows, and high availability compared to the single server deployment option. With this update, organizations can now provision flexible servers in Malaysia West, leveraging features such as zone-redundant high availability, burstable and scalable compute tiers, custom maintenance windows, and built-in automated backups with point-in-time restore capabilities. The flexible server deployment model supports both single-zone and zone-redundant high availability configurations, which are critical for mission-critical applications requiring minimal downtime.

Technically, the flexible server architecture decouples compute and storage, allowing independent scaling of resources. It uses Azure’s underlying infrastructure to provide automated patching, monitoring, and security updates, while giving users control over maintenance timing to minimize operational impact. The deployment in Malaysia West utilizes Azure’s regional data centers and network backbone to ensure low-latency connectivity and compliance with local data sovereignty laws. The service supports PostgreSQL versions 11, 12, and 13, enabling compatibility with a wide range of applications and extensions.

Typical use cases for deploying PostgreSQL flexible server in Malaysia West include web and mobile applications serving Southeast Asian customers, SaaS platforms requiring regional data residency, and analytics workloads that benefit from proximity to data sources in the region. Enterprises can also use this service to implement disaster recovery strategies by replicating data across regions or integrating with Azure Backup and Azure Monitor for comprehensive operational management.

Key considerations when adopting this service include understanding the pricing model, which is based on vCores, storage, and backup retention; evaluating network latency and throughput requirements; and planning for high availability configurations to meet uptime SLAs. Users should also consider the supported PostgreSQL extensions and version compatibility to ensure application functionality. While flexible server offers more customization than single server, it does not yet support all features available in Azure Database for PostgreSQL Hyperscale (Citus), so workload requirements should guide the choice of deployment option.

Integration with other Azure services is seamless: Azure Database for PostgreSQL flexible server can be connected with Azure App Service, Azure Kubernetes Service (AKS), and Azure Functions for building scalable applications. It supports Azure Private Link for secure, private connectivity, and can be monitored using Azure Monitor and Azure Advisor for performance tuning and cost optimization. Additionally, integration with Azure Active Directory enables centralized identity and access management.

In summary, the general availability of Azure Database for PostgreSQL flexible server in Malaysia West empowers organizations in Southeast Asia to deploy highly available, scalable, and fully managed PostgreSQL databases with regional data residency, enhanced operational control, and seamless integration with the Azure ecosystem, thereby facilitating the development of performant and compliant applications tailored to local markets.

---

### 3. Public Preview: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key

**Published**: August 13, 2025 16:00:27 UTC
**Link**: [Public Preview: Azure Cosmos DB for MongoDB (vCore) encryption with customer-managed key](https://azure.microsoft.com/updates?id=499670)

**Update ID**: 499670
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Azure Cosmos DB for MongoDB (vCore) clusters now support encryption using customer-managed keys (CMK) in public preview, complementing the existing service-managed key (SMK) encryption.

- Key changes or new features  
Developers and IT professionals can configure Azure Cosmos DB for MongoDB (vCore) to use Azure Key Vault customer-managed keys for data encryption at rest. This provides enhanced control over encryption keys, allowing organizations to meet stricter compliance and security requirements. The CMK encryption works seamlessly alongside the default Microsoft-managed keys, enabling layered security without impacting application performance or availability.

- Target audience affected  
This update primarily affects database administrators, security engineers, and developers managing Azure Cosmos DB for MongoDB (vCore) workloads who require advanced encryption key management and compliance controls.

- Important notes if any  
The feature is currently in public preview, so it should be used with caution in production environments. Proper Azure Key Vault permissions and configurations are necessary to enable CMK encryption. Customers should evaluate key lifecycle management and rotation policies to maintain security best practices. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The recent Azure update introduces Public Preview support for customer-managed key (CMK) encryption in Azure Cosmos DB for MongoDB (vCore) API, enhancing data security by allowing users to control encryption keys beyond the default service-managed keys (SMK). This update addresses growing enterprise demands for greater control over data encryption and compliance requirements by enabling an additional encryption layer using keys stored in Azure Key Vault.

**Background and Purpose:**  
Azure Cosmos DB for MongoDB (vCore) clusters have traditionally encrypted data at rest using Microsoft-managed keys, ensuring baseline security and compliance. However, many organizations require the ability to manage their own encryption keys to meet stringent regulatory standards, maintain key lifecycle control, and implement separation of duties. This update introduces customer-managed key encryption, empowering customers to bring their own keys (BYOK) and manage them within Azure Key Vault, thereby enhancing data sovereignty and security posture.

**Specific Features and Changes:**  
- **Customer-Managed Key Encryption:** Users can now configure their Cosmos DB for MongoDB (vCore) clusters to use CMK stored in Azure Key Vault for encryption at rest, supplementing the existing SMK encryption.  
- **Key Vault Integration:** The encryption keys are securely stored and managed in Azure Key Vault, allowing centralized key lifecycle management, including rotation, revocation, and auditing.  
- **Seamless Encryption:** Data encryption and decryption remain transparent to applications, with no changes required in application code or MongoDB drivers.  
- **Granular Control:** Customers can enable or disable CMK encryption per cluster, providing flexibility in security configurations.

**Technical Mechanisms and Implementation:**  
- When CMK encryption is enabled, Cosmos DB uses the specified key from Azure Key Vault to encrypt the data encryption keys (DEKs) that protect the data at rest.  
- The DEKs are wrapped (encrypted) with the CMK, ensuring that access to the underlying data requires access to the customer’s key.  
- Azure Cosmos DB integrates with Azure Key Vault via managed identities, allowing secure, role-based access to the keys without embedding credentials.  
- Key rotation in Azure Key Vault triggers Cosmos DB to rewrap DEKs with the new key version, maintaining continuous data protection without downtime.  
- The encryption process is handled at the storage layer, ensuring minimal performance impact and transparent operation.

**Use Cases and Application Scenarios:**  
- Enterprises subject to regulatory frameworks such as GDPR, HIPAA, or PCI DSS that mandate customer control over encryption keys.  
- Organizations requiring separation of duties between database administrators and security teams managing encryption keys.  
- Scenarios demanding auditability and compliance reporting on key usage and access.  
- Applications handling highly sensitive data where enhanced encryption governance is critical.

**Important Considerations and Limitations:**  
- This feature is currently in Public Preview; production workloads should evaluate readiness and potential limitations.  
- Enabling CMK encryption requires appropriate Azure Key Vault permissions and proper configuration of managed identities.  
- Key Vault availability and latency can impact Cosmos DB operations; ensure Key Vault is deployed in the same region or with low-latency connectivity.  
- Key rotation policies must be carefully planned to avoid unintended access disruptions.  
- Not all Cosmos DB APIs or features may support CMK encryption at this stage; verify compatibility with MongoDB (vCore) API clusters specifically.

**Integration with Related Azure Services:**  
- **Azure Key Vault:** Central to CMK encryption, providing secure key storage, access control, and auditing capabilities.  
- **Azure Active Directory (AAD):** Used for authentication and authorization of Cosmos DB managed identities to access Key Vault keys.  
- **Azure Monitor and Azure Security Center:** Can be leveraged to monitor key usage, audit logs, and security posture related to encryption.  
- **Azure Policy:** May be used to enforce organizational standards for encryption and key management across Cosmos DB resources.

In summary, the Public Preview of customer-managed key encryption for Azure Cosmos DB for MongoDB (v

---

### 4. Generally Available: Deployment resumption - Azure Automation revised Service and Subscription limits

**Published**: August 13, 2025 12:15:34 UTC
**Link**: [Generally Available: Deployment resumption - Azure Automation revised Service and Subscription limits](https://azure.microsoft.com/updates?id=500198)

**Update ID**: 500198
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Automation, Management

**Summary**:

- What was updated  
Azure Automation is resuming the deployment of revised Service and Subscription limits starting August 11, 2025.

- Key changes or new features  
The update enforces updated limits on Azure Automation services and subscriptions to ensure equitable resource allocation. These revised limits aim to enhance overall platform reliability and performance by preventing resource contention and overuse.

- Target audience affected  
Developers and IT professionals who manage automation runbooks, jobs, and related resources within Azure Automation at scale will be impacted. Organizations with high-volume automation workloads should review their usage against the new limits.

- Important notes if any  
The deployment was briefly paused but will now continue as scheduled. Users should monitor their automation accounts for any potential throttling or limit enforcement and adjust their automation strategies accordingly. Detailed limit specifications and guidance are available in the Azure Automation documentation to help plan for these changes.

**Details**:

The Azure Automation update titled "Generally Available: Deployment resumption - Azure Automation revised Service and Subscription limits," effective from August 11, 2025, marks the resumption of enforcing updated service and subscription limits designed to optimize resource allocation, enhance system reliability, and maintain performance consistency across customers.

**Background and Purpose**  
Azure Automation is a cloud-based automation and configuration service that enables IT professionals to automate frequent, time-consuming, and error-prone management tasks. Over time, as customer demand and scale have grown, Microsoft identified the need to revise service and subscription limits to ensure equitable resource distribution and prevent any single tenant from disproportionately impacting shared infrastructure. The update follows a brief pause in deployment to allow customers to adapt and prepare for the changes. Resuming the deployment of these revised limits aims to improve overall platform stability and performance by mitigating resource contention and throttling risks.

**Specific Features and Detailed Changes**  
The update introduces revised limits on key Azure Automation resources, including but not limited to:  
- **Runbook concurrency limits:** Caps on the number of simultaneously running jobs per subscription or service instance to prevent resource exhaustion.  
- **Job queue depth:** Maximum queued jobs awaiting execution are adjusted to balance throughput and latency.  
- **Hybrid Runbook Worker limits:** Restrictions on the number of workers per subscription to ensure optimal load distribution.  
- **Webhook and DSC (Desired State Configuration) resource limits:** Adjusted thresholds to maintain service responsiveness.  

These limits are carefully calibrated based on telemetry and usage patterns to provide fair usage while minimizing disruptions.

**Technical Mechanisms and Implementation Methods**  
The enforcement of these limits is implemented at the Azure Automation service layer, leveraging internal throttling and quota management mechanisms. When a subscription approaches or exceeds a limit, the service responds with throttling errors (HTTP 429) or job rejection messages, prompting clients to implement retry logic with exponential backoff. The limits are monitored continuously, and customers can query their current usage and limits via Azure Resource Manager APIs and Azure Portal metrics. Additionally, Azure Automation logs relevant throttling events to Azure Monitor, enabling proactive alerting and diagnostics.

**Use Cases and Application Scenarios**  
- Enterprises running large-scale automation workflows benefit from predictable execution and reduced risk of job failures due to resource contention.  
- Managed service providers (MSPs) can plan capacity and scale automation workloads without unexpected throttling.  
- DevOps teams integrating Azure Automation with CI/CD pipelines gain improved reliability for deployment and configuration tasks.  
- Organizations leveraging Hybrid Runbook Workers for on-premises integration can optimize worker allocation within subscription limits.

**Important Considerations and Limitations**  
- Customers must review their current automation workloads and adjust concurrency and scheduling to comply with the new limits.  
- Automation runbooks that previously operated at high concurrency may require redesign or workload distribution across multiple subscriptions or Automation accounts.  
- Throttling responses necessitate robust error handling and retry mechanisms in automation scripts and client applications.  
- The limits are subject to change; customers should monitor Azure Updates and documentation for future revisions.  
- Some legacy or specialized scenarios may require engagement with Microsoft support for limit increase requests or exceptions.

**Integration with Related Azure Services**  
This update complements Azure Monitor by providing enhanced telemetry on Automation resource usage and throttling events, enabling integrated monitoring and alerting workflows. It also aligns with Azure Policy and Azure Cost Management by helping enforce governance and cost control through predictable automation resource consumption. Furthermore, customers integrating Azure Automation with Azure Logic Apps, Azure Functions, or Azure DevOps pipelines will experience improved orchestration reliability due to stabilized Automation service performance.

In summary, the resumption of deployment of revised Azure Automation service and subscription limits from August 11, 2025, is a strategic enhancement to ensure equitable resource distribution, improve platform reliability, and maintain consistent performance for all customers. IT professionals should proactively assess and adapt their automation workloads to comply with these limits, implement robust error handling for throttling scenarios, and leverage Azure monitoring tools to maintain

---


*This report was automatically generated - 2025-08-14 03:03:17 UTC*