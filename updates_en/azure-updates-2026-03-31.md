# March 31, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 31, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Public Preview: Ephemeral OS Disk with full caching for VM/VMSS

**Published**: March 30, 2026 21:45:47 UTC
**Link**: [Public Preview: Ephemeral OS Disk with full caching for VM/VMSS](https://azure.microsoft.com/updates?id=559322)

**Update ID**: 559322
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machine Scale Sets, Virtual Machines, Features

**Summary**:

- What was updated  
Ephemeral OS Disk with full caching is now available in public preview for Azure Virtual Machines (VM) and Virtual Machine Scale Sets (VMSS).

- Key changes or new features  
This update enables the entire OS disk image to be cached on the local VM storage (cache disk or resource disk), providing significantly faster and more reliable OS disk performance. Full caching reduces boot and read/write latency, improves VM provisioning times, and enhances overall workload performance. Ephemeral OS disks are ideal for stateless workloads, as they do not persist data after VM deallocation.

- Target audience affected  
Azure developers and IT professionals managing infrastructure, especially those deploying large-scale, stateless workloads on Azure VMs or VMSS.

- Important notes if any  
Ephemeral OS disks with full caching are best suited for stateless applications where OS persistence is not required. Data on the OS disk is lost if the VM is deallocated or deleted. Review VM size and region availability, as not all configurations support ephemeral disks. For production workloads, ensure your application can tolerate non-persistent OS disks.

Data source: Using API data  
[Learn more](https://azure.microsoft.com/updates?id=559322)

**Details**:

**Azure Update Report: Public Preview – Ephemeral OS Disk with Full Caching for VM/VMSS**

**Background and Purpose of the Update**  
Ephemeral OS disks are designed for stateless workloads, offering high-performance and cost-effective storage by leveraging local VM storage instead of remote Azure storage. The purpose of this update is to enhance the performance and reliability of OS disk operations for Azure Virtual Machines (VM) and Virtual Machine Scale Sets (VMSS) by introducing full caching for ephemeral OS disks. This addresses the need for faster boot times, improved I/O throughput, and reduced latency for workloads that do not require persistent OS disk storage.

**Specific Features and Detailed Changes**  
With this public preview, Azure now supports the caching of the entire ephemeral OS disk image on the local VM storage, specifically utilizing the cache disk or resource disk. Previously, ephemeral OS disks leveraged local storage but did not offer full caching capabilities. The update introduces:

- **Full OS Disk Caching:** The entire OS disk is cached locally, ensuring all read and write operations are performed against the VM’s local storage.
- **Enhanced Performance:** This approach delivers significantly faster disk operations, including boot, shutdown, and OS-level I/O, compared to traditional remote-managed disks.
- **Reliability Improvements:** By eliminating network dependencies for OS disk operations, the risk of latency or interruptions due to network or remote storage issues is reduced.

**Technical Mechanisms and Implementation Methods**  
The technical implementation leverages the VM’s local cache disk or resource disk to store the OS disk image. When a VM or VMSS instance is provisioned with an ephemeral OS disk and full caching enabled, the OS disk is not persisted in Azure Storage; instead, it resides entirely on the local disk. This means:

- **Disk Operations:** All disk reads and writes occur on the local disk, bypassing Azure Storage.
- **VM Provisioning:** Ephemeral OS disks are created during VM provisioning and are lost when the VM is deallocated or deleted.
- **Caching Layer:** The full caching mechanism uses the available local disk space, maximizing throughput and minimizing latency.

**Use Cases and Application Scenarios**  
This feature is best suited for stateless workloads where OS persistence is not required, such as:

- **Auto-scaling VMSS scenarios:** Rapid provisioning and deprovisioning of VM instances for scale-out workloads.
- **Dev/Test environments:** Fast boot and shutdown cycles for temporary VMs.
- **Container hosts:** Where the OS disk is used only for ephemeral operations and containers are managed externally.
- **Batch processing:** Short-lived compute tasks that require quick startup and teardown.

**Important Considerations and Limitations**  
- **Statelessness:** Ephemeral OS disks are not persisted; all data is lost when the VM is deleted or deallocated.
- **Local Storage Dependency:** The feature depends on the availability and performance of the VM’s local cache/resource disk.
- **Preview Limitations:** As this is a public preview, production use is not recommended until general availability and full support.
- **VM Size Compatibility:** Only VM sizes with sufficient local disk capacity can utilize full caching for ephemeral OS disks.

**Integration with Related Azure Services**  
Ephemeral OS disks with full caching integrate seamlessly with Azure VM and VMSS provisioning workflows. They can be used alongside Azure DevOps, Azure Batch, and other automation tools that require rapid VM lifecycle management. However, integration with Azure Backup, Azure Site Recovery, and other persistent storage services is not applicable due to the stateless nature of ephemeral disks.

**Summary Sentence**  
Ephemeral OS Disk with full caching for Azure VM/VMSS, now in public preview, delivers significantly faster and more reliable OS disk performance by caching the entire OS disk image on local VM storage, ideal for stateless and high-performance workloads.

---

### 2. Generally Available: Azure Red Hat OpenShift in Indonesia Central

**Published**: March 30, 2026 21:30:50 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift in Indonesia Central](https://azure.microsoft.com/updates?id=559552)

**Update ID**: 559552
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Open Source

**Summary**:

- What was updated  
Azure Red Hat OpenShift (ARO) is now generally available in the Indonesia Central Azure region.

- Key changes or new features  
This update expands the regional availability of ARO, allowing organizations to deploy and manage mission-critical OpenShift workloads on Azure within Indonesia Central. Customers can now leverage fully managed, enterprise-grade Kubernetes with integrated security, compliance, and support from both Microsoft and Red Hat in this region.

- Target audience affected  
Developers and IT professionals in Indonesia or those with workloads requiring data residency in Indonesia. Organizations seeking to modernize applications using OpenShift on Azure, or those with regulatory or latency requirements specific to the Indonesia Central region.

- Important notes if any  
This expansion supports local compliance and data residency needs, enabling customers to meet regulatory requirements. Existing ARO features, such as automated updates, scaling, and integrated monitoring, are available in Indonesia Central. Customers should review regional pricing and service availability before deployment.

For more details, see the official update: https://azure.microsoft.com/updates?id=559552

**Details**:

**Azure Update Technical Summary: Azure Red Hat OpenShift Now Generally Available in Indonesia Central**

**Background and Purpose of the Update:**  
Azure Red Hat OpenShift (ARO) is now generally available in the Indonesia Central Azure region. This update expands the regional footprint of ARO, enabling organizations operating in Indonesia and its vicinity to deploy and manage mission-critical OpenShift workloads directly within their local Azure datacenter. The primary purpose is to address data residency, compliance, and latency requirements for enterprises in Indonesia, supporting their cloud adoption and modernization strategies.

**Specific Features and Detailed Changes:**  
With this release, all core ARO features are now accessible in Indonesia Central. Customers can provision fully managed OpenShift clusters, leveraging enterprise-grade Kubernetes orchestration with integrated security, monitoring, and scaling. This includes automated cluster operations (installation, upgrades, patching), built-in CI/CD tooling, and seamless integration with Azure networking and identity services. The update ensures that organizations can utilize the same SLA-backed, production-ready OpenShift service previously available in other regions.

**Technical Mechanisms and Implementation Methods:**  
ARO is a jointly engineered and supported service by Microsoft and Red Hat, delivered as a managed offering on Azure infrastructure. When deploying ARO in Indonesia Central, clusters are provisioned using Azure Resource Manager templates and are managed through the Azure portal, CLI, or REST APIs. The service automates cluster lifecycle management, including node provisioning, scaling, and security patching. Integration with Azure Active Directory (AAD) provides centralized identity and access management, while Azure Monitor and Log Analytics enable operational visibility.

**Use Cases and Application Scenarios:**  
Typical use cases include hosting containerized enterprise applications, microservices architectures, and DevOps pipelines that require high availability and regulatory compliance. Organizations in regulated industries (such as finance, government, and healthcare) benefit from local data residency and reduced network latency. The service is also suitable for multinational companies seeking to standardize their OpenShift deployments across multiple Azure regions, including Indonesia Central.

**Important Considerations and Limitations:**  
Customers should verify regional service quotas and resource availability, as not all VM sizes or Azure services may be available in Indonesia Central. Network architecture should be designed to accommodate local compliance requirements, and customers must ensure that their workloads align with the region’s data residency policies. As with all managed services, cluster-level customizations may be subject to platform constraints. It is recommended to consult the official Azure regional services availability documentation for the latest supported features.

**Integration with Related Azure Services:**  
ARO clusters in Indonesia Central can be integrated with a wide range of Azure services, including Azure Container Registry (for image storage), Azure Key Vault (for secrets management), Azure Monitor (for logging and metrics), and Azure Policy (for governance). Native integration with Azure networking (VNETs, Private Link) and identity (AAD) ensures a secure and compliant environment. This enables organizations to build end-to-end cloud-native solutions leveraging both OpenShift and the broader Azure ecosystem.

**Summary:**  
Azure Red Hat OpenShift is now generally available in the Indonesia Central region, providing local access to a fully managed, enterprise-grade OpenShift platform for running mission-critical containerized workloads on Azure.

---

### 3. Retirement: Deprecation of sidecar for remote-write for Azure Monitor managed service for Prometheus

**Published**: March 30, 2026 21:30:50 UTC
**Link**: [Retirement: Deprecation of sidecar for remote-write for Azure Monitor managed service for Prometheus](https://azure.microsoft.com/updates?id=550519)

**Update ID**: 550519
**Data source**: Azure Updates API

**Categories**: Compute, Containers, DevOps, Management and governance, Azure Kubernetes Service (AKS), Azure Monitor, Retirements

**Summary**:

- What was updated  
Azure Monitor is deprecating the sidecar for remote-write of Prometheus metrics to Azure Monitor Workspace.

- Key changes or new features  
The sidecar component, used for remote-writing Prometheus metrics to Azure Monitor Workspace, will be retired on March 31, 2027. After this date, the sidecar will no longer be supported. Users are advised to configure their self-hosted Prometheus instances to write metrics directly to Azure Monitor Workspace, without relying on the sidecar.

- Target audience affected  
Developers and IT professionals managing Prometheus monitoring solutions on Azure, especially those using the sidecar for remote-write integration with Azure Monitor Workspace.

- Important notes if any  
Existing deployments using the sidecar must transition to direct remote-write configurations before March 31, 2027, to ensure continued metric ingestion and support. This change aims to improve reliability and reduce operational complexity. Review your current monitoring setup and update configurations as recommended by Microsoft to avoid service disruption. For migration guidance, refer to official Azure documentation.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=550519

**Details**:

**Azure Update Report: Retirement of Sidecar for Remote-Write in Azure Monitor Managed Service for Prometheus**

**Background and Purpose of the Update**  
Azure Monitor’s managed service for Prometheus currently allows users to remote-write Prometheus metrics to Azure Monitor Workspace using a sidecar component. The sidecar acts as an intermediary, facilitating the transfer of metrics from Prometheus to Azure Monitor. As part of ongoing efforts to improve reliability and reduce operational complexity, Microsoft has announced the deprecation of this sidecar mechanism. The retirement is scheduled for March 31, 2027. The purpose of this update is to streamline metric ingestion workflows, minimize dependencies, and encourage more robust and scalable integration patterns.

**Specific Features and Detailed Changes**  
The primary change is the removal of the sidecar component used for remote-write operations. After the deprecation date, the sidecar will no longer be supported or maintained, and users will need to transition to alternative methods for sending Prometheus metrics to Azure Monitor Workspace. This update affects any deployments utilizing the sidecar for remote-write, whether in self-hosted or managed environments.

**Technical Mechanisms and Implementation Methods**  
Previously, the sidecar provided a lightweight container or process that intercepted Prometheus metrics and relayed them to Azure Monitor Workspace using the remote-write protocol. With its retirement, users must configure Prometheus to send metrics directly to Azure Monitor Workspace, bypassing the sidecar. This typically involves updating Prometheus’s remote-write configuration to point directly to Azure Monitor’s ingestion endpoints, ensuring proper authentication and data formatting as required by Azure Monitor.

**Use Cases and Application Scenarios**  
This change impacts IT professionals managing Kubernetes clusters, virtual machines, or other environments where Prometheus is used for monitoring and metrics collection. Common scenarios include:
- Monitoring containerized workloads in Azure Kubernetes Service (AKS) with Prometheus.
- Collecting infrastructure metrics from self-hosted Prometheus instances.
- Integrating Prometheus metrics into centralized Azure Monitor Workspaces for unified observability.

Organizations relying on the sidecar for remote-write must update their deployment pipelines and monitoring configurations to ensure uninterrupted metric ingestion post-deprecation.

**Important Considerations and Limitations**  
- The sidecar will be fully unsupported after March 31, 2027; continued use beyond this date may result in loss of functionality and lack of support.
- Migration to direct remote-write requires careful configuration of Prometheus, including endpoint URLs, authentication, and compatibility with Azure Monitor’s ingestion requirements.
- Users should validate their monitoring pipelines and perform thorough testing to ensure metrics are correctly ingested after removing the sidecar.
- Documentation and support resources should be consulted to facilitate the transition and avoid disruptions.

**Integration with Related Azure Services**  
Azure Monitor Workspace remains the central destination for Prometheus metrics, supporting advanced analytics, alerting, and visualization. Direct remote-write integration simplifies the architecture and enhances reliability. This update aligns with Azure’s broader strategy to reduce intermediary components and promote direct, scalable integrations across Azure Monitor, Azure Kubernetes Service, and other Azure resources.

**Summary Sentence**  
Azure Monitor will retire the sidecar for remote-write of Prometheus metrics to Azure Monitor Workspace by March 31, 2027, requiring users to transition to direct remote-write configurations to improve reliability and reduce complexity.

---

### 4. Retirement: Azure Cosmos DB for PostgreSQL will retire on March 31, 2029

**Published**: March 30, 2026 17:45:08 UTC
**Link**: [Retirement: Azure Cosmos DB for PostgreSQL will retire on March 31, 2029](https://azure.microsoft.com/updates?id=556085)

**Update ID**: 556085
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Azure Cosmos DB for PostgreSQL will be retired on March 31, 2029.

- Key changes or new features  
After the retirement date, Azure Cosmos DB for PostgreSQL will no longer be available. Customers are required to migrate their workloads to Azure Database for PostgreSQL Elastic Cluster, which provides equivalent distributed PostgreSQL capabilities.

- Target audience affected  
Developers and IT professionals currently using Azure Cosmos DB for PostgreSQL, especially those managing distributed PostgreSQL workloads in Azure.

- Important notes  
Migration to Azure Database for PostgreSQL Elastic Cluster must be completed before March 31, 2029 to avoid service disruption. The Elastic Cluster service offers the same distributed PostgreSQL features, ensuring continuity for existing workloads. Planning and testing migration strategies ahead of time is recommended to minimize downtime and ensure compatibility. Microsoft will provide guidance and tools to support the migration process. Review your current deployments and begin preparing for migration as soon as possible.  

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=556085

**Details**:

**Azure Update Report: Retirement of Azure Cosmos DB for PostgreSQL on March 31, 2029**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Azure Cosmos DB for PostgreSQL, effective March 31, 2029. This update is part of Azure’s ongoing efforts to streamline its database offerings and consolidate distributed PostgreSQL capabilities under a single managed service. Customers currently using Azure Cosmos DB for PostgreSQL are required to migrate their workloads to Azure Database for PostgreSQL Elastic Cluster by the retirement date. The purpose of this update is to provide a clear migration path and ensure continued support and feature enhancements under the Azure Database for PostgreSQL Elastic Cluster service.

**Specific Features and Detailed Changes:**  
- **Retirement of Service:** Azure Cosmos DB for PostgreSQL will no longer be available after March 31, 2029.
- **Migration Requirement:** All existing deployments must transition to Azure Database for PostgreSQL Elastic Cluster before the retirement date.
- **Feature Parity:** Azure Database for PostgreSQL Elastic Cluster offers the same distributed PostgreSQL capabilities as Cosmos DB for PostgreSQL, ensuring minimal disruption to existing workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Distributed PostgreSQL:** Both services provide distributed PostgreSQL functionality, allowing for horizontal scaling and sharding of data across multiple nodes.
- **Migration Path:** Customers will need to plan and execute a migration from Cosmos DB for PostgreSQL to the Elastic Cluster service. This may involve exporting data, reconfiguring applications to point to the new service endpoint, and validating distributed query performance.
- **Service Management:** Post-migration, all management, monitoring, and scaling operations will be handled through Azure Database for PostgreSQL Elastic Cluster’s management interfaces and APIs.

**Use Cases and Application Scenarios:**  
- **Scalable OLTP Workloads:** Applications requiring high-throughput transactional processing with distributed data storage.
- **Multi-tenant SaaS Platforms:** Solutions that benefit from sharding and elastic scaling to support multiple customers or tenants.
- **Data-Intensive Applications:** Scenarios where distributed query processing and large-scale data ingestion are required.

**Important Considerations and Limitations:**  
- **Mandatory Migration:** Failure to migrate by March 31, 2029, will result in loss of service availability and support for Cosmos DB for PostgreSQL deployments.
- **Migration Planning:** IT teams should assess their current usage, plan for data migration, and test application compatibility with Azure Database for PostgreSQL Elastic Cluster.
- **Feature Alignment:** While feature parity is stated, teams should verify any service-specific configurations or integrations that may require adjustment during migration.

**Integration with Related Azure Services:**  
- **Azure Database for PostgreSQL Ecosystem:** The Elastic Cluster service is part of the broader Azure Database for PostgreSQL family, enabling integration with Azure security, monitoring, and backup solutions.
- **Azure Resource Management:** Post-migration, resources can be managed using standard Azure tools, including Azure Portal, CLI, and ARM templates.
- **Data Integration:** Applications leveraging Azure Data Factory, Logic Apps, or other data movement services should update connection endpoints as part of the migration process.

**Summary Sentence:**  
Azure Cosmos DB for PostgreSQL will be retired on March 31, 2029, requiring all users to migrate to Azure Database for PostgreSQL Elastic Cluster, which offers the same distributed PostgreSQL capabilities, and IT professionals should plan and execute migration strategies to ensure service continuity and feature alignment.

---

### 5. Generally Available: Azure Premium SSD v2 Disk is now available in South India

**Published**: March 30, 2026 16:30:50 UTC
**Link**: [Generally Available: Azure Premium SSD v2 Disk is now available in South India](https://azure.microsoft.com/updates?id=559526)

**Update ID**: 559526
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Compute, Azure Disk Storage, Virtual Machines, Features, Services

**Summary**:

- What was updated  
Azure Premium SSD v2 disk is now generally available in the South India region (which does not have Availability Zones).

- Key changes or new features  
Premium SSD v2 is a next-generation general-purpose block storage option for Azure virtual machines. It delivers sub-millisecond latencies and improved price-performance compared to previous disk offerings. This enables faster application performance and more cost-effective storage for workloads requiring high throughput and low latency.

- Target audience affected  
Developers and IT professionals deploying or managing Azure virtual machines in South India, especially those with performance-sensitive workloads such as databases, analytics, and enterprise applications.

- Important notes if any  
Since South India does not have Availability Zones, Premium SSD v2 disks are only available in single-zone configurations. Users should consider this when architecting for high availability and disaster recovery. Existing workloads can be migrated to Premium SSD v2 for improved performance and cost efficiency. Review Azure documentation for compatibility and migration guidance.

**Details**:

**Azure Update Report: General Availability of Azure Premium SSD v2 Disk in South India**

**Background and Purpose of the Update**  
Azure Premium SSD v2 Disk, a next-generation general-purpose block storage solution for Azure Virtual Machines (VMs), is now generally available in the South India region. This update addresses the demand for high-performance, cost-effective disk storage in South India, a region that does not have Availability Zone support. The purpose is to extend advanced disk storage capabilities to customers operating workloads in this specific geography.

**Specific Features and Detailed Changes**  
Premium SSD v2 disks offer sub-millisecond latencies, providing significant improvements in performance compared to previous disk offerings. This disk type is designed to deliver exceptional price-performance for a wide range of enterprise workloads. With this update, customers in South India can now provision and attach Premium SSD v2 disks to their Azure VMs, leveraging the latest advancements in Azure block storage technology.

**Technical Mechanisms and Implementation Methods**  
Premium SSD v2 disks are engineered as general-purpose block storage, optimized for Azure VMs. These disks utilize Azure’s storage infrastructure to achieve consistent sub-millisecond latencies, which is critical for latency-sensitive applications. The provisioning and management of Premium SSD v2 disks are performed through the Azure Portal, CLI, PowerShell, or ARM templates, consistent with other managed disk types. The disks can be attached to supported VM sizes and managed using standard Azure Disk APIs.

**Use Cases and Application Scenarios**  
Premium SSD v2 disks are suitable for a variety of enterprise workloads that require high IOPS, low latency, and predictable performance. Typical use cases include:  
- Hosting databases (SQL, NoSQL) that demand fast storage response times  
- Running transactional workloads and line-of-business applications  
- Supporting virtual desktop infrastructure (VDI) deployments  
- Serving as storage for latency-sensitive analytics workloads

**Important Considerations and Limitations**  
- The Premium SSD v2 disk offering is available in South India, which does not have Availability Zone support. As such, customers should architect their solutions with regional redundancy in mind if high availability across zones is required.  
- Customers should verify VM size compatibility and ensure that their workloads are configured to take advantage of the performance characteristics of Premium SSD v2.  
- Pricing, disk size options, and performance tiers should be reviewed in the Azure documentation to align with workload requirements and cost constraints.

**Integration with Related Azure Services**  
Premium SSD v2 disks integrate seamlessly with Azure Virtual Machines and can be managed using the same tools and APIs as other Azure Managed Disks. They can be used in conjunction with Azure Backup, Azure Site Recovery, and other Azure storage management solutions, enabling comprehensive data protection and disaster recovery strategies. Integration with monitoring and alerting services (such as Azure Monitor) allows for proactive management of disk performance and health.

**Summary Sentence**  
Azure Premium SSD v2 Disk, now generally available in the South India region, provides Azure customers with high-performance, low-latency block storage for virtual machines, supporting a broad range of enterprise workloads with improved price-performance, even in regions without Availability Zone support.

---


*This report was automatically generated - 2026-03-31 03:03:12 UTC*