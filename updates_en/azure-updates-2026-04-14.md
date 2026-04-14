# April 14, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 14, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Generally Available: Azure File Sync in Belgium Central, Malaysia West, and Indonesia Central

**Published**: April 13, 2026 23:45:31 UTC
**Link**: [Generally Available: Azure File Sync in Belgium Central, Malaysia West, and Indonesia Central](https://azure.microsoft.com/updates?id=557828)

**Update ID**: 557828
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Files, Features

**Summary**:

- What was updated  
Azure File Sync is now generally available in the Belgium Central, Malaysia West, and Indonesia Central regions.

- Key changes or new features  
This update expands Azure File Sync’s regional availability, allowing organizations in these locations to tier data from on-premises Windows Servers to Azure Files. It supports hybrid storage scenarios, enabling seamless data migration and centralized file management. Users can leverage on-premises file server performance while benefiting from Azure’s scalability and flexibility.

- Target audience affected  
Developers and IT professionals managing hybrid storage solutions, especially those operating in or serving Belgium, Malaysia, and Indonesia. Organizations planning cloud migration or requiring efficient file synchronization between on-premises and Azure environments are directly impacted.

- Important notes if any  
With this regional expansion, local organizations can now meet data residency and compliance requirements more easily. Existing Azure File Sync features, such as cloud tiering, multi-site sync, and rapid disaster recovery, are fully supported in these new regions. Review regional pricing and service limits before deployment.  

Data source: Using API data  
Link: [Azure Update](https://azure.microsoft.com/updates?id=557828)

**Details**:

**Azure Update Report: General Availability of Azure File Sync in Belgium Central, Malaysia West, and Indonesia Central**

**Background and Purpose of the Update:**  
Azure File Sync is a hybrid cloud storage solution that extends on-premises Windows Server file shares to Azure Files, enabling organizations to centralize file services in Azure while maintaining local access and performance. The general availability (GA) of Azure File Sync in the Belgium Central, Malaysia West, and Indonesia Central regions addresses the growing demand for hybrid cloud storage capabilities in these geographies. This expansion allows customers in these regions to leverage Azure File Sync for data tiering, backup, and migration scenarios, while complying with data residency and latency requirements.

**Specific Features and Detailed Changes:**  
With this update, Azure File Sync is now fully supported and available in the Belgium Central, Malaysia West, and Indonesia Central Azure regions. Key features include:
- **Seamless Data Tiering:** Automatically moves infrequently accessed files from on-premises Windows Servers to Azure Files, freeing up local storage while keeping frequently accessed files cached locally.
- **Simplified Migration:** Facilitates migration of file server data to Azure Files without disrupting existing workflows or requiring changes to user access patterns.
- **Hybrid Access:** Maintains compatibility and performance of on-premises file servers while leveraging Azure’s scalability and durability.

**Technical Mechanisms and Implementation Methods:**  
Azure File Sync operates by installing the Azure File Sync agent on supported Windows Servers. These servers are registered with an Azure Storage Sync Service, which orchestrates synchronization between the on-premises file shares and Azure Files shares in the specified region. The agent monitors file changes and manages tiering policies, ensuring that only metadata or frequently accessed files remain on-premises, while the rest are stored in Azure Files. This is achieved through cloud endpoints (Azure Files shares) and server endpoints (local folders on Windows Servers), with synchronization and tiering policies defined in the Azure portal.

**Use Cases and Application Scenarios:**  
- **Hybrid File Server Deployments:** Organizations can maintain local file server performance for branch offices or remote sites while centralizing data management in Azure.
- **Data Migration:** Simplifies the process of moving file server data to Azure Files for cloud-first or cloud-migration strategies.
- **Disaster Recovery and Backup:** Provides an offsite copy of critical data, supporting business continuity and compliance requirements.
- **Capacity Management:** Reduces the need for frequent on-premises storage upgrades by offloading cold data to Azure.

**Important Considerations and Limitations:**  
- **Regional Availability:** Azure File Sync must be deployed in the same region as the Azure Files storage account. With this update, Belgium Central, Malaysia West, and Indonesia Central are now supported.
- **Agent and OS Compatibility:** The Azure File Sync agent must be installed on supported versions of Windows Server.
- **Network Connectivity:** Reliable and secure connectivity between on-premises servers and Azure is required for synchronization and tiering operations.
- **Data Residency:** Organizations must ensure compliance with local data residency regulations when selecting the Azure region for deployment.

**Integration with Related Azure Services:**  
Azure File Sync integrates natively with Azure Files, leveraging its SMB compatibility and scalability. It can also be used in conjunction with Azure Backup for protecting file shares, and with Azure Monitor for operational insights and alerting. Integration with Azure Active Directory and on-premises Active Directory enables seamless authentication and access control.

**Summary Sentence:**  
Azure File Sync is now generally available in Belgium Central, Malaysia West, and Indonesia Central, enabling organizations in these regions to efficiently tier, synchronize, and migrate file server data to Azure Files for hybrid cloud storage scenarios.

---

### 2. Public Preview: Managed identity support for graphical session recording

**Published**: April 13, 2026 18:45:30 UTC
**Link**: [Public Preview: Managed identity support for graphical session recording](https://azure.microsoft.com/updates?id=560162)

**Update ID**: 560162
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Bastion, Features, Services

**Summary**:

- What was updated  
Azure Bastion now supports managed identities for graphical session recording in public preview.

- Key changes or new features  
Azure Bastion graphical session recording can now use managed identities to provide write access to Azure Storage accounts. This enables secure and simplified authentication for storing session recordings, eliminating the need for storage account keys or SAS tokens. Users can configure Bastion to use either a system-assigned or user-assigned managed identity for this purpose.

- Target audience affected  
Azure administrators, IT professionals managing secure remote access, and developers integrating Bastion with storage solutions.

- Important notes if any  
This feature enhances security and simplifies management by leveraging Azure AD-based authentication for storage access. It is currently in public preview, so it is recommended for testing and non-production workloads. Review your Bastion and storage account permissions to ensure the managed identity has the necessary write access. For more details, refer to the official Azure documentation.

**Details**:

**Azure Update: Public Preview – Managed Identity Support for Graphical Session Recording in Azure Bastion**

**Background and Purpose of the Update**  
Azure Bastion provides secure and seamless RDP and SSH connectivity to virtual machines directly in the Azure portal without exposing public IPs. Graphical session recording is a feature that captures and stores session activity for auditing and compliance. Previously, configuring storage access for session recordings required explicit storage account keys or SAS tokens, which can introduce management overhead and potential security risks. The purpose of this update is to enhance security and simplify management by enabling the use of managed identities for storage access during graphical session recording.

**Specific Features and Detailed Changes**  
With this public preview, Azure Bastion now supports the use of managed identities to grant write access to Azure Storage accounts for graphical session recordings. This means that instead of manually managing and rotating storage account keys or SAS tokens, Bastion can use an assigned managed identity to authenticate and authorize access to the storage account where session recordings are saved. This update provides an additional option for secure and streamlined access management.

**Technical Mechanisms and Implementation Methods**  
- **Managed Identity Assignment:** Azure Bastion can be configured with a system-assigned or user-assigned managed identity.
- **Role-Based Access Control (RBAC):** The managed identity must be granted the necessary RBAC permissions (such as the "Storage Blob Data Contributor" role) on the target storage account to enable write access for session recordings.
- **Session Recording Workflow:** When a graphical session is recorded, Bastion uses the managed identity’s credentials to authenticate to Azure Storage and write the session data directly, without the need for storage account keys or SAS tokens.
- **Configuration:** Administrators can opt-in to use managed identities for session recording via the Azure portal or ARM templates, as per the updated documentation.

**Use Cases and Application Scenarios**  
- **Security-First Environments:** Organizations with strict security policies can leverage managed identities to eliminate the risks associated with distributing and managing storage account keys.
- **Automated Environments:** Enterprises using Infrastructure-as-Code (IaC) can automate the assignment of managed identities and RBAC permissions for Bastion and storage resources.
- **Compliance and Auditing:** Environments requiring session recording for audit trails can now manage access more securely and efficiently.

**Important Considerations and Limitations**  
- **Preview Feature:** This capability is currently in public preview and may not be recommended for production workloads until general availability.
- **RBAC Configuration:** Proper RBAC permissions must be assigned to the managed identity; misconfiguration may result in failed session recordings.
- **Supported Storage Accounts:** The update specifically mentions write access to storage accounts, but does not detail compatibility with all storage account types or tiers.
- **Opt-In Model:** Users must explicitly opt-in to use managed identities for session recording; existing configurations using keys or SAS tokens remain unchanged.

**Integration with Related Azure Services**  
- **Azure Storage:** Session recordings are stored in Azure Storage accounts, leveraging RBAC for access control.
- **Azure Active Directory (AAD):** Managed identities are backed by Azure AD, ensuring secure identity management and access governance.
- **Azure RBAC:** Role assignments are managed through Azure RBAC, aligning with best practices for least privilege access.

**Summary Sentence**  
Azure Bastion now supports using managed identities for secure, streamlined write access to storage accounts during graphical session recording, reducing key management overhead and enhancing security through Azure RBAC integration.

---

### 3. Generally Available: Azure Storage Mover now available in Azure Government (US)

**Published**: April 13, 2026 18:00:56 UTC
**Link**: [Generally Available: Azure Storage Mover now available in Azure Government (US)](https://azure.microsoft.com/updates?id=560198)

**Update ID**: 560198
**Data source**: Azure Updates API

**Categories**: Launched, Migration, Storage, Azure Storage Mover, Features, Regions & Datacenters, Services

**Summary**:

- What was updated  
Azure Storage Mover is now generally available in Azure Government (US) regions.

- Key changes or new features  
Azure Storage Mover, a fully managed migration service, now supports secure, large-scale file data migration to Azure Government cloud environments. This service automates and orchestrates the migration process, reducing manual effort and minimizing downtime. It supports migration from on-premises file shares and other storage sources directly to Azure Government storage accounts.

- Target audience affected  
U.S. government customers, partners, IT professionals, and developers working with regulated workloads in Azure Government environments who need to migrate large volumes of file data securely and efficiently.

- Important notes if any  
Azure Storage Mover in Azure Government meets compliance and security requirements specific to U.S. government workloads. The service simplifies migration planning and execution, supporting scenarios such as data center migrations, cloud adoption, and modernization initiatives. Existing Azure Storage Mover documentation and APIs are applicable, but users should verify region-specific availability and compliance requirements.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Storage Mover now available in Azure Government (US)  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=560198)

---

**Background and Purpose of the Update**  
Azure Storage Mover is now generally available in Azure Government (US). The primary purpose of this update is to provide U.S. government customers and partners with a secure, scalable, and fully managed solution for migrating large-scale file data into Azure Government cloud environments. This addresses the need for compliance with government regulations and ensures that sensitive data is handled within a dedicated, compliant cloud infrastructure.

**Specific Features and Detailed Changes**  
With this release, Azure Storage Mover is accessible within Azure Government (US) regions. The service offers a fully managed migration experience, enabling users to transfer extensive file datasets securely and efficiently. Key features include:

- Support for large-scale file data migration.
- Secure transfer mechanisms tailored for government compliance.
- Integration with Azure Government cloud environments.
- Managed service model, reducing operational overhead for migration tasks.

**Technical Mechanisms and Implementation Methods**  
Azure Storage Mover operates as a fully managed migration service. It abstracts the complexity of data transfer by providing automated orchestration and monitoring of migration jobs. Users can configure migration tasks through the Azure portal, specifying source and destination file storage endpoints within the Azure Government cloud. The service handles authentication, data movement, and error handling, ensuring data integrity and security throughout the process.

**Use Cases and Application Scenarios**  
Typical application scenarios include:

- Migrating legacy file data from on-premises or other cloud environments to Azure Government storage solutions.
- Consolidating file data into Azure Government for centralized management and compliance.
- Supporting digital transformation initiatives within U.S. government agencies and partners by enabling secure cloud adoption.

**Important Considerations and Limitations**  
When utilizing Azure Storage Mover in Azure Government (US), IT professionals should consider:

- The service is designed specifically for Azure Government environments, ensuring compliance with U.S. government requirements.
- Migration is limited to file data; other data types may require alternative migration tools.
- Users should validate compatibility between source and destination storage formats prior to migration.
- Network connectivity and bandwidth may impact migration performance; planning for large-scale transfers is essential.

**Integration with Related Azure Services**  
Azure Storage Mover integrates seamlessly with Azure Government storage services, such as Azure Blob Storage and Azure Files. It can be orchestrated via the Azure portal, allowing users to leverage existing Azure Government identity and access management controls. The service complements other Azure migration tools and can be used in conjunction with Azure Monitor for tracking migration progress and auditing.

---

**Summary Sentence**  
Azure Storage Mover is now generally available in Azure Government (US), providing U.S. government customers and partners with a secure, fully managed solution for migrating large-scale file data to Azure Government cloud environments.

---

### 4. Public Preview: Monitor AKS applications with OpenTelemetry and Azure Monitor 

**Published**: April 13, 2026 17:45:02 UTC
**Link**: [Public Preview: Monitor AKS applications with OpenTelemetry and Azure Monitor ](https://azure.microsoft.com/updates?id=560119)

**Update ID**: 560119
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Open Source

**Summary**:

- What was updated  
Azure Monitor now supports monitoring AKS (Azure Kubernetes Service) applications using OpenTelemetry, available in Public Preview.

- Key changes or new features  
  - Developers and IT teams can now instrument AKS workloads with OpenTelemetry for telemetry data collection.  
  - Azure Monitor provides an OpenTelemetry distribution (distro) that can be deployed via autoinstrumentation or integrated manually into applications.  
  - This enables unified collection of traces, metrics, and logs from containerized applications running on AKS, improving observability and troubleshooting.  
  - Integration supports both .NET and Java applications, with plans for more language support.

- Target audience affected  
  - Application developers deploying workloads on AKS.  
  - DevOps and IT professionals responsible for monitoring and maintaining AKS clusters.

- Important notes if any  
  - This feature is currently in Public Preview and may not be suitable for production workloads.  
  - Autoinstrumentation simplifies setup by reducing code changes required for telemetry collection.  
  - Using OpenTelemetry with Azure Monitor aligns with industry standards, making it easier to integrate with other observability tools.  
  - For more details and setup instructions, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=560119).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Monitor AKS applications with OpenTelemetry and Azure Monitor  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=560119)

---

**Background and Purpose of the Update:**  
Azure Monitor has introduced support for monitoring applications running on Azure Kubernetes Service (AKS) using OpenTelemetry for instrumentation and data collection. The purpose of this update is to enable IT professionals and developers to leverage the OpenTelemetry standard for observability, facilitating seamless integration of telemetry data from AKS workloads into Azure Monitor.

---

**Specific Features and Detailed Changes:**  
- **OpenTelemetry Integration:** Azure Monitor now natively supports OpenTelemetry, allowing applications on AKS to send telemetry data (traces, metrics, and logs) using the OpenTelemetry protocol.
- **Autoinstrumentation:** The update introduces autoinstrumentation capabilities, enabling users to deploy the Azure Monitor OpenTelemetry distribution (distro) directly to their workloads. This reduces manual instrumentation efforts and accelerates observability adoption.
- **Azure Monitor OpenTelemetry Distro:** Users can deploy the Azure Monitor-specific OpenTelemetry distribution to their AKS workloads, ensuring compatibility and optimized data collection for Azure Monitor.

---

**Technical Mechanisms and Implementation Methods:**  
- **Instrumentation:** Applications running on AKS can be instrumented using OpenTelemetry SDKs or agents. With autoinstrumentation, the Azure Monitor OpenTelemetry distro can be injected into workloads without modifying application code.
- **Data Collection:** The OpenTelemetry collector or agents collect telemetry data from instrumented applications and forward it to Azure Monitor.
- **Deployment:** The Azure Monitor OpenTelemetry distro can be deployed as a sidecar, DaemonSet, or integrated directly into application containers, depending on the workload architecture and operational requirements.

---

**Use Cases and Application Scenarios:**  
- **Distributed Tracing:** Gain end-to-end visibility into distributed applications running on AKS by collecting trace data via OpenTelemetry and visualizing it in Azure Monitor.
- **Performance Monitoring:** Monitor application performance metrics (e.g., latency, error rates, throughput) for workloads on AKS, leveraging OpenTelemetry’s standardized data model.
- **Log Aggregation:** Centralize and analyze logs from AKS applications using OpenTelemetry and Azure Monitor.
- **Cloud-Native Observability:** Adopt a cloud-native observability approach by standardizing on OpenTelemetry for all AKS workloads, simplifying multi-cloud and hybrid monitoring strategies.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** This feature is currently in public preview, which may imply limited support, potential changes, and possible instability. Production use should be evaluated accordingly.
- **Compatibility:** Ensure that workloads are compatible with the Azure Monitor OpenTelemetry distro and autoinstrumentation methods.
- **Configuration:** Proper configuration of the OpenTelemetry collector and Azure Monitor endpoints is required for successful data ingestion.
- **Resource Overhead:** Autoinstrumentation and additional telemetry collection may introduce resource overhead on application pods or nodes.

---

**Integration with Related Azure Services:**  
- **Azure Monitor:** Telemetry data collected via OpenTelemetry is ingested directly into Azure Monitor, enabling unified monitoring, alerting, and visualization.
- **AKS (Azure Kubernetes Service):** The update is specifically tailored for AKS workloads, aligning with Azure’s managed Kubernetes offering.
- **Other Azure Observability Tools:** Data collected can be further analyzed using Azure Log Analytics, Application Insights, and integrated with Azure dashboards and alerting systems.

---

**Summary Sentence:**  
Azure Monitor now supports public preview integration with OpenTelemetry for AKS workloads, enabling streamlined application monitoring through autoinstrumentation and the Azure Monitor OpenTelemetry distribution, thereby enhancing observability and reducing manual instrumentation efforts for Kubernetes-based applications.

---

### 5. Generally Available: Granular Encryption-in-Transit Controls for SMB and NFS on Azure Files 

**Published**: April 13, 2026 17:45:02 UTC
**Link**: [Generally Available: Granular Encryption-in-Transit Controls for SMB and NFS on Azure Files ](https://azure.microsoft.com/updates?id=560001)

**Update ID**: 560001
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Files, Security

**Summary**:

- What was updated  
Azure Files now offers generally available support for granular, protocol-specific encryption-in-transit controls for SMB and NFS at the storage account level.

- Key changes or new features  
Customers can independently configure encryption-in-transit requirements for SMB and NFS protocols within the same storage account. This allows for the creation of protocol-specific security policies, enabling more precise control over how data is protected during transit. For example, you can enforce encryption for SMB while allowing different settings for NFS, or vice versa.

- Target audience affected  
This update is relevant for IT professionals managing Azure Files storage accounts, as well as developers building applications that interact with SMB or NFS shares on Azure Files. Organizations with mixed workloads or compliance requirements will particularly benefit.

- Important notes if any  
Review your current storage account configurations to ensure protocol-specific encryption settings align with your organization’s security and compliance needs. This feature enhances flexibility but requires careful policy management to avoid unintentional exposure. For more details, refer to the official Azure documentation.  
Link: https://azure.microsoft.com/updates?id=560001

**Details**:

**Comprehensive Technical Explanation: Granular Encryption-in-Transit Controls for SMB and NFS on Azure Files**

**Background and Purpose of the Update**  
Azure Files provides fully managed file shares in the cloud, accessible via SMB (Server Message Block) and NFS (Network File System) protocols. Previously, encryption-in-transit settings were applied at a broader scope, limiting flexibility for organizations with mixed protocol environments or varying compliance requirements. The purpose of this update is to enhance security posture and compliance alignment by allowing customers to independently configure encryption-in-transit policies for SMB and NFS at the storage account level.

**Specific Features and Detailed Changes**  
With this update, Azure Files introduces the ability to set protocol-specific encryption-in-transit requirements. Administrators can now:  
- Independently enable or disable encryption-in-transit for SMB and NFS protocols on a per-storage account basis.  
- Define security policies that are tailored to the specific protocol, rather than applying a single policy to all protocols.  
- Achieve more granular control over data protection for file shares, aligning with organizational or regulatory needs.

**Technical Mechanisms and Implementation Methods**  
The implementation is managed through the Azure portal, CLI, PowerShell, or ARM templates, where protocol-specific encryption-in-transit settings can be configured at the storage account level. When enabled, encryption-in-transit ensures that data transmitted between clients and Azure Files is protected using industry-standard encryption protocols (such as SMB 3.0+ for SMB and NFS 4.1+ with encryption support). The settings are enforced by Azure Files, and connections that do not meet the specified encryption requirements are denied.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations subject to strict compliance standards (e.g., HIPAA, GDPR) can enforce encryption-in-transit for sensitive workloads while allowing exceptions for legacy systems that may not support encryption.
- **Mixed Protocol Environments:** Enterprises using both SMB and NFS can apply different encryption policies based on protocol capabilities or business requirements.
- **Migration and Modernization:** During migration phases, organizations can gradually enforce encryption-in-transit as client systems are upgraded, reducing disruption.

**Important Considerations and Limitations**  
- Encryption-in-transit settings are configured at the storage account level and apply to all file shares within that account for the specified protocol.
- Disabling encryption-in-transit for a protocol may expose data to interception during transmission; this should only be done for trusted networks or legacy compatibility scenarios.
- Clients must support the required encryption protocols (e.g., SMB 3.0+ or NFS 4.1+) to connect when encryption-in-transit is enforced.
- This update does not affect encryption-at-rest, which remains enabled by default for all Azure Files data.

**Integration with Related Azure Services**  
- Azure Files integrates with Azure Active Directory (Azure AD) and Azure RBAC for access management, and these controls operate independently of encryption-in-transit settings.
- The update is compatible with Azure Backup, Azure File Sync, and other Azure storage management tools, ensuring seamless operation across the Azure ecosystem.

**Summary Sentence**  
Azure Files now allows IT professionals to independently configure encryption-in-transit settings for SMB and NFS protocols at the storage account level, providing enhanced, protocol-specific security controls for cloud file shares.

---

### 6. Retirement: Azure Managed Grafana Essential SKU will retire on March 30, 2027

**Published**: April 13, 2026 17:15:23 UTC
**Link**: [Retirement: Azure Managed Grafana Essential SKU will retire on March 30, 2027](https://azure.microsoft.com/updates?id=559395)

**Update ID**: 559395
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Azure Managed Grafana, Retirements

**Summary**:

- What was updated  
Azure Managed Grafana Essential SKU will be retired on March 30, 2027.

- Key changes or new features  
The Essential SKU for Azure Managed Grafana will no longer be available after the retirement date. Customers are advised to migrate to the Azure Managed Grafana Standard SKU or use Azure Monitor Dashboards with Grafana for continued support and service.

- Target audience affected  
This update affects developers, DevOps engineers, and IT professionals currently using the Azure Managed Grafana Essential SKU for monitoring and visualization.

- Important notes if any  
To avoid service disruption, users must transition to the Standard SKU or Azure Monitor Dashboards with Grafana before March 30, 2027. Planning migration ahead of time is recommended to ensure continuity and take advantage of enhanced features and support in the Standard SKU. No new features will be added to the Essential SKU, and support will end after the retirement date. For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=559395

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Azure Managed Grafana Essential SKU will retire on March 30, 2027  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=559395)

---

**Background and Purpose of the Update:**  
Azure Managed Grafana is a managed service offering Grafana dashboards for monitoring and visualization within the Azure ecosystem. The Essential SKU, which provides a basic tier of this service, will be retired on March 30, 2027. The purpose of this update is to inform customers of the planned retirement and to encourage migration to alternative solutions, specifically the Azure Managed Grafana Standard SKU or Azure Monitor Dashboards with Grafana, to ensure continued service and support.

**Specific Features and Detailed Changes:**  
The Essential SKU currently offers a limited set of features compared to higher tiers such as the Standard SKU. With its retirement, customers will lose access to the Essential SKU, and no new deployments or renewals will be possible after the retirement date. The update does not specify feature-level differences, but it is implied that the Standard SKU offers enhanced capabilities and support. Customers are advised to transition to the Standard SKU or utilize Azure Monitor Dashboards with Grafana, which are fully supported and offer broader functionality.

**Technical Mechanisms and Implementation Methods:**  
The retirement process will involve decommissioning the Essential SKU from the Azure Managed Grafana service catalog. Existing deployments will need to be migrated to the Standard SKU or Azure Monitor Dashboards with Grafana prior to March 30, 2027. Migration typically involves provisioning a new instance of the Standard SKU, exporting dashboards and configurations from the Essential SKU, and importing them into the new environment. Azure provides tools and APIs for dashboard export/import, and integration with Azure Monitor ensures continuity of monitoring data and alerting.

**Use Cases and Application Scenarios:**  
Azure Managed Grafana is commonly used for visualizing telemetry, metrics, and logs from Azure resources, including VMs, containers, and PaaS services. The Essential SKU is suitable for small-scale or development environments with basic monitoring needs. The Standard SKU and Azure Monitor Dashboards with Grafana are recommended for production workloads, enterprise monitoring, and scenarios requiring advanced features such as role-based access control, enhanced data source integrations, and support for larger user bases.

**Important Considerations and Limitations:**  
Customers must plan their migration before the retirement date to avoid service disruption. Failure to transition will result in loss of access to the Essential SKU and potential downtime for monitoring dashboards. It is important to evaluate feature parity between the Essential and Standard SKUs and ensure compatibility of existing dashboards and integrations. Licensing, pricing, and support terms may differ between SKUs, so review these aspects during migration planning.

**Integration with Related Azure Services:**  
Azure Managed Grafana integrates closely with Azure Monitor, Log Analytics, Application Insights, and other Azure data sources. Migrating to the Standard SKU or Azure Monitor Dashboards with Grafana ensures continued seamless integration with these services. The Standard SKU supports advanced Azure integrations, enabling richer visualization and alerting capabilities. Azure Monitor Dashboards with Grafana provide a native experience for monitoring Azure resources using Grafana within the Azure portal.

---

**Summary Sentence:**  
Azure Managed Grafana Essential SKU will be retired on March 30, 2027; customers should migrate to the Standard SKU or Azure Monitor Dashboards with Grafana to maintain uninterrupted monitoring and visualization capabilities.

---

### 7. Public Preview: StandardV2 NAT Gateway as an outbound type for AKS 

**Published**: April 13, 2026 16:00:36 UTC
**Link**: [Public Preview: StandardV2 NAT Gateway as an outbound type for AKS ](https://azure.microsoft.com/updates?id=560207)

**Update ID**: 560207
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Networking, Azure Kubernetes Service (AKS), Azure NAT Gateway, Features, Services

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now supports StandardV2 NAT Gateway (managed and user-assigned) as an outbound type in public preview.

- Key changes or new features  
  - AKS clusters (both managed and BYO VNets) can use StandardV2 NAT Gateway for outbound connectivity.  
  - Enables zone-redundant outbound connectivity, improving high availability.  
  - Supports up to 100 Gbps outbound throughput, meeting high-scale networking requirements.  
  - Adds IPv6 outbound support for AKS clusters.

- Target audience affected  
  - Developers deploying applications on AKS that require high-throughput or IPv6 outbound connectivity.  
  - IT professionals and network administrators managing AKS networking, especially those designing for high availability and scalability.

- Important notes if any  
  - This feature is in public preview and not recommended for production workloads yet.  
  - Both managed and user-assigned StandardV2 NAT Gateways are supported, providing flexibility in network design.  
  - Review Azure documentation for configuration details and limitations during the preview phase.

For more information, see the official update: https://azure.microsoft.com/updates?id=560207

**Details**:

**Azure Update Explanation: Public Preview: StandardV2 NAT Gateway as an outbound type for AKS**

---

**Background and Purpose of the Update:**

Azure Kubernetes Service (AKS) clusters require reliable and scalable outbound connectivity for workloads running within the cluster. Traditionally, AKS supported various outbound types, but with growing requirements for higher throughput, zone redundancy, and IPv6 support, there was a need to enhance outbound connectivity options. This update introduces support for managed and user-assigned StandardV2 NAT Gateway as an outbound type for AKS, addressing these advanced networking needs.

---

**Specific Features and Detailed Changes:**

- **StandardV2 NAT Gateway Support:** AKS now allows the use of StandardV2 NAT Gateway as an outbound type for both managed and Bring Your Own (BYO) Virtual Networks (VNets).
- **Zone-Redundant Outbound Connectivity:** StandardV2 NAT Gateway provides zone-redundant outbound connectivity, enhancing availability and resiliency for egress traffic from AKS clusters.
- **High Outbound Throughput:** The update enables up to 100 Gbps outbound throughput, supporting high-scale workloads and reducing potential bottlenecks.
- **IPv6 Outbound Support:** AKS clusters can now leverage IPv6 for outbound connectivity, facilitating modern application requirements and compliance with IPv6 mandates.

---

**Technical Mechanisms and Implementation Methods:**

- **Outbound Type Configuration:** When creating or updating an AKS cluster, users can specify StandardV2 NAT Gateway as the outbound type. This can be applied to both managed VNets (provisioned by AKS) and user-provided VNets.
- **Managed vs. User-Assigned:** The update supports both managed NAT Gateway instances (provisioned and managed by AKS) and user-assigned NAT Gateways (created and managed by the user and then associated with the AKS subnet).
- **Zone Redundancy:** StandardV2 NAT Gateway is deployed across multiple availability zones, ensuring that outbound traffic remains available even if a zone experiences an outage.
- **Throughput Scaling:** The NAT Gateway automatically scales to support up to 100 Gbps of outbound traffic, accommodating demanding workloads without manual intervention.
- **IPv6 Enablement:** With StandardV2 NAT Gateway, outbound IPv6 connectivity is natively supported, allowing AKS workloads to communicate over IPv6 networks.

---

**Use Cases and Application Scenarios:**

- **High-Scale Applications:** Workloads requiring large-scale outbound connectivity, such as data processing, analytics, or high-traffic web services, benefit from the increased throughput.
- **Multi-Zone Deployments:** Applications that require high availability and disaster recovery across Azure Availability Zones can leverage zone-redundant outbound connectivity.
- **IPv6-Ready Solutions:** Organizations adopting IPv6 or operating in environments where IPv6 is mandated can use this feature to ensure outbound IPv6 connectivity from AKS clusters.
- **Custom Networking:** Enterprises using custom VNets (BYO VNet) can now integrate StandardV2 NAT Gateway for enhanced outbound traffic management.

---

**Important Considerations and Limitations:**

- **Public Preview:** This feature is currently in public preview and may not be recommended for production workloads until it reaches general availability.
- **Configuration Requirements:** Proper configuration of the NAT Gateway and its association with the AKS subnet is necessary to ensure correct operation.
- **Compatibility:** Only StandardV2 NAT Gateway is supported as an outbound type; other NAT Gateway SKUs are not mentioned in this update.
- **IPv6 Support:** Outbound IPv6 is supported, but inbound IPv6 or dual-stack cluster configurations are not specified in this update.

---

**Integration with Related Azure Services:**

- **AKS Networking:** Seamlessly integrates with AKS networking models, supporting both managed and BYO VNets.
- **Azure NAT Gateway:** Leverages the StandardV2 NAT Gateway resource for scalable and resilient outbound connectivity.
- **Azure Availability Zones:** Utilizes

---


*This report was automatically generated - 2026-04-14 03:04:44 UTC*