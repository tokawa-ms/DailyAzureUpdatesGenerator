# May 06, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 06, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Retirement: Azure Reserved Virtual Machines Instances for select VM series

**Published**: May 05, 2026 20:00:13 UTC
**Link**: [Retirement: Azure Reserved Virtual Machines Instances for select VM series](https://azure.microsoft.com/updates?id=560948)

**Update ID**: 560948
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements, Pricing & Offerings

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Reserved Virtual Machine Instances (RIs) for select VM series.

- Key changes or new features  
Starting July 1, 2026, customers will no longer be able to purchase or renew one-year Azure Reserved VM Instances for the following VM series: Av2, Amv2, Bv1, D, Ds, Dv2, Dsv2, F, Fs, Fsv2, G, Gs, Ls, and Lsv2. Additionally, both one-year and three-year reserved instances for these VM series will be retired.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently using or planning to use Reserved VM Instances for the affected VM series to optimize costs.

- Important notes if any  
Existing reservations will remain valid until their end date, but after July 1, 2026, no new purchases or renewals will be possible for these VM series. Customers should plan to transition workloads to supported VM series or consider alternative cost management options, such as Azure Savings Plans for Compute. Review your current VM deployments and reservation strategies to ensure continued cost optimization and support. For more information, refer to the official Azure update: https://azure.microsoft.com/updates?id=560948

**Details**:

**Azure Update Report: Retirement of Azure Reserved Virtual Machines Instances for Select VM Series**

**Background and Purpose of the Update**  
Microsoft Azure periodically reviews its product offerings to align with evolving customer needs, hardware lifecycle management, and platform modernization strategies. The retirement of Azure Reserved Virtual Machines (VM) Instances for select VM series reflects Azure’s ongoing efforts to optimize its portfolio, streamline VM offerings, and encourage migration to newer or more efficient VM families.

**Specific Features and Detailed Changes**  
Effective July 1, 2026, Azure will discontinue the ability to purchase or renew one-year Reserved VM Instances for the following VM series: Av2, Amv2, Bv1, D, Ds, Dv2, Dsv2, F, Fs, Fsv2, G, Gs, Ls, and Lsv2. This change means that after this date, customers will not be able to acquire new one-year reservations or renew existing ones for these VM types. Furthermore, both one-year and three-year reserved instance options will be affected, as indicated by the update content.

**Technical Mechanisms and Implementation Methods**  
Azure Reserved VM Instances allow customers to pre-commit to a specific VM size and region for a one-year or three-year term, in exchange for significant cost savings compared to pay-as-you-go pricing. The retirement will be enforced at the Azure platform level, preventing new purchases or renewals for the specified VM series through the Azure Portal, APIs, and CLI. Existing reservations will remain valid until their expiration date, after which customers must transition to alternative purchasing options or VM series.

**Use Cases and Application Scenarios**  
Reserved VM Instances are commonly used in scenarios with predictable, steady-state workloads such as production environments, persistent application servers, and long-term projects where cost optimization is critical. The affected VM series are often utilized for general-purpose, compute-optimized, and memory-optimized workloads. After retirement, customers with workloads on these VM series must evaluate migration strategies, such as moving to newer VM families or switching to pay-as-you-go pricing, to maintain cost efficiency.

**Important Considerations and Limitations**  
- After July 1, 2026, no new one-year reservations or renewals for the listed VM series will be possible.  
- Existing reservations will continue to function until their natural expiration.  
- Customers should plan for migration to supported VM series before their reservations expire to avoid unexpected cost increases.  
- Workloads running on the retired VM series will not be interrupted immediately, but the lack of reservation options may impact long-term budgeting and cost management strategies.  
- The update does not specify changes to pay-as-you-go VM instances for these series, but reserved instance cost benefits will no longer be available.

**Integration with Related Azure Services**  
Reserved VM Instances are closely integrated with Azure Cost Management, Azure Advisor, and Azure Resource Manager. Customers should leverage these tools to identify impacted resources, analyze cost implications, and plan migrations. Azure Migrate can assist in workload assessment and migration planning to newer VM series that support reservations. Integration with Azure Policy can help enforce compliance with updated VM usage guidelines.

**Summary Sentence**  
Starting July 1, 2026, Azure will retire one-year Reserved VM Instance purchases and renewals for select VM series, requiring customers to transition to alternative VM families or purchasing models for continued cost optimization.

---

### 2. Public Preview: Application Gateway for Containers managed add-on + AKS Automatic 

**Published**: May 05, 2026 17:30:03 UTC
**Link**: [Public Preview: Application Gateway for Containers managed add-on + AKS Automatic ](https://azure.microsoft.com/updates?id=558403)

**Update ID**: 558403
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
The Application Gateway for Containers managed add-on for Azure Kubernetes Service (AKS) is now in Public Preview, including support for AKS automatic management.

- Key changes or new features  
  - The Application Gateway for Containers can now be deployed and managed as a native AKS managed add-on, simplifying integration and lifecycle management.
  - AKS automatic management enables seamless provisioning, scaling, and updates of the Application Gateway for Containers alongside AKS clusters.
  - This update removes previous limitations, allowing for more streamlined and automated deployment scenarios for containerized workloads.

- Target audience affected  
  - Developers deploying containerized applications on AKS.
  - IT professionals and platform engineers managing AKS clusters and ingress solutions.

- Important notes if any  
  - The managed add-on is currently in Public Preview and not recommended for production workloads.
  - Integration with AKS automatic management reduces operational overhead and aligns with Azure’s best practices for cloud-native ingress.
  - Users should review documentation for configuration details and limitations during the preview phase.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=558403)

**Details**:

**Azure Update Report: Public Preview – Application Gateway for Containers Managed Add-on + AKS Automatic**

**Background and Purpose of the Update:**  
Previously, Microsoft introduced Application Gateway for Containers and the Application Gateway for Containers AKS Add-on to enhance ingress capabilities for Azure Kubernetes Service (AKS) environments. However, a notable limitation was that Application Gateway for Containers could not be managed automatically as an add-on within AKS. This update addresses that gap by enabling automatic management of Application Gateway for Containers as a managed add-on for AKS, streamlining deployment and operational workflows.

**Specific Features and Detailed Changes:**  
With this public preview, Application Gateway for Containers can now be provisioned and managed directly as an AKS managed add-on. This eliminates the need for manual setup and configuration, allowing AKS users to leverage Application Gateway for Containers with simplified lifecycle management. Key features include:

- **Automated Provisioning:** The add-on can be enabled during AKS cluster creation or updated on existing clusters, automating the deployment of Application Gateway for Containers.
- **Integrated Management:** The lifecycle (creation, update, deletion) of Application Gateway for Containers is now tightly integrated with AKS, reducing operational overhead.
- **Enhanced Ingress Capabilities:** Application Gateway for Containers provides advanced Layer 7 load balancing, SSL termination, Web Application Firewall (WAF), and routing features for containerized workloads.

**Technical Mechanisms and Implementation Methods:**  
The managed add-on leverages Azure Resource Manager (ARM) templates and AKS extension APIs to automate the provisioning and configuration of Application Gateway for Containers. When enabled, AKS orchestrates the deployment of the gateway, configures necessary networking, and ensures that the ingress controller is properly registered with the cluster. This integration uses Azure’s native identity and access management to secure communication between AKS and Application Gateway for Containers.

**Use Cases and Application Scenarios:**  
- **Production-Grade Ingress:** Enterprises running mission-critical workloads on AKS can now use Application Gateway for Containers as a managed add-on for robust ingress with advanced security and routing.
- **Simplified Operations:** DevOps teams benefit from reduced complexity in managing ingress controllers, as the add-on automates deployment and updates.
- **Compliance and Security:** Organizations requiring WAF and SSL termination at the ingress layer can easily enable these features with minimal manual intervention.

**Important Considerations and Limitations:**  
- **Preview Status:** The managed add-on is currently in public preview, which may entail limited support and potential changes before general availability.
- **Feature Parity:** Some features of Application Gateway for Containers may not be fully available or supported in the managed add-on during the preview phase.
- **Resource Constraints:** Users should review Azure documentation for any resource limitations or quotas associated with the managed add-on.

**Integration with Related Azure Services:**  
The managed add-on is designed for seamless integration with AKS, leveraging Azure networking (Virtual Networks, Subnets), Azure Monitor for logging and metrics, and Azure Active Directory for identity management. It also works alongside other Azure services such as Azure Key Vault for SSL certificate management and Azure Policy for governance.

**Summary Sentence:**  
The public preview of Application Gateway for Containers as a managed AKS add-on enables automated provisioning and integrated lifecycle management, simplifying advanced ingress deployment for containerized workloads in Azure Kubernetes Service.

---

### 3. Generally Available: Azure Elastic SAN support for AVS Gen2 Private Cloud  

**Published**: May 05, 2026 16:00:38 UTC
**Link**: [Generally Available: Azure Elastic SAN support for AVS Gen2 Private Cloud  ](https://azure.microsoft.com/updates?id=560909)

**Update ID**: 560909
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Elastic SAN is now generally available for use as a datastore with Azure VMware Solution (AVS) Gen2 Private Cloud.

- Key changes or new features  
  - Elastic SAN datastores now integrate with AVS Gen2 Private Cloud, providing simpler connectivity and improved performance.  
  - No ExpressRoute gateway is required for connectivity between AVS and Elastic SAN.  
  - Configuration is streamlined: only a single Private Endpoint is needed to connect Elastic SAN to AVS Gen2, reducing complexity and setup time.

- Target audience affected  
Developers and IT professionals managing Azure VMware Solution (AVS) Gen2 Private Cloud environments, especially those responsible for storage architecture and connectivity.

- Important notes if any  
  - This update simplifies the deployment and management of storage for AVS Gen2 by removing the need for ExpressRoute gateways and minimizing network configuration steps.  
  - It enables faster and more secure storage provisioning for VMware workloads on Azure.  
  - Review the official documentation for any prerequisites or limitations before migrating or deploying Elastic SAN datastores with AVS Gen2.

[Read more](https://azure.microsoft.com/updates?id=560909)

**Details**:

**Azure Update Report: Generally Available – Azure Elastic SAN Support for AVS Gen2 Private Cloud**

**Background and Purpose of the Update:**  
This update announces the general availability of Azure Elastic SAN (Storage Area Network) support for Azure VMware Solution (AVS) Gen2 Private Cloud environments. The primary objective is to simplify storage connectivity and configuration for AVS customers, while also delivering improved performance for workloads hosted on AVS Gen2 Private Clouds.

**Specific Features and Detailed Changes:**  
- **Simpler Connectivity and Configuration:** The integration allows AVS Gen2 Private Cloud environments to connect to Elastic SAN datastores with a significantly reduced network and configuration footprint.
- **No ExpressRoute Gateway Required:** Previously, connecting external storage to AVS typically necessitated an ExpressRoute gateway, introducing additional complexity and cost. With this update, the ExpressRoute gateway is no longer required for Elastic SAN connectivity.
- **Single Private Endpoint Configuration:** The new approach enables the use of a single Private Endpoint to establish connectivity between the AVS Gen2 Private Cloud and the Elastic SAN datastore, streamlining the setup process and reducing management overhead.

**Technical Mechanisms and Implementation Methods:**  
- **Private Endpoint Utilization:** Connectivity between AVS Gen2 Private Cloud and Azure Elastic SAN is established via an Azure Private Endpoint. This mechanism ensures secure, private connectivity over the Azure backbone, eliminating the need for public IP exposure or complex routing.
- **Direct Integration:** The Elastic SAN datastore can be directly mounted to the AVS environment using the Private Endpoint, bypassing the need for intermediate networking components such as ExpressRoute gateways.
- **Performance Improvements:** By leveraging Azure’s backbone and the optimized integration path, AVS workloads can benefit from reduced latency and increased throughput when accessing Elastic SAN storage.

**Use Cases and Application Scenarios:**  
- **Enterprise Workloads:** Organizations running VMware-based workloads in AVS Gen2 Private Clouds that require scalable, high-performance, and resilient storage can now leverage Azure Elastic SAN as a native datastore.
- **Simplified Disaster Recovery and Backup:** The streamlined connectivity model is ideal for scenarios where rapid provisioning and simplified management of storage resources are critical, such as backup, disaster recovery, and workload migration.
- **Cost and Complexity Reduction:** Enterprises seeking to minimize infrastructure complexity and operational costs benefit from the removal of the ExpressRoute gateway requirement and the simplified endpoint configuration.

**Important Considerations and Limitations:**  
- **Supported Only on AVS Gen2 Private Cloud:** This update specifically applies to AVS Gen2 Private Cloud environments; earlier AVS versions may not support this integration.
- **Single Private Endpoint Limitation:** While the use of a single Private Endpoint simplifies configuration, organizations must ensure that their network security and access policies are appropriately configured to maintain isolation and compliance.
- **Elastic SAN Service Limits:** Users should be aware of any existing service limits or quotas associated with Azure Elastic SAN, as these may impact large-scale or high-throughput scenarios.

**Integration with Related Azure Services:**  
- **Azure Private Link:** The solution leverages Azure Private Link for secure, private connectivity.
- **Azure VMware Solution (AVS):** The update enhances the storage options available to AVS Gen2 Private Cloud, enabling tighter integration with Azure-native storage services.
- **Elastic SAN Ecosystem:** This integration allows AVS workloads to participate in broader Elastic SAN scenarios, such as multi-cloud storage, high-availability architectures, and seamless scaling.

**Summary Sentence:**  
Azure Elastic SAN is now generally available for AVS Gen2 Private Cloud, providing simplified, high-performance storage connectivity via a single Private Endpoint without the need for an ExpressRoute gateway.

---

### 4. Generally Available: Single Volume Snapshots on Azure Elastic SAN

**Published**: May 05, 2026 16:00:38 UTC
**Link**: [Generally Available: Single Volume Snapshots on Azure Elastic SAN](https://azure.microsoft.com/updates?id=560899)

**Update ID**: 560899
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Elastic SAN now offers general availability of single volume snapshots.

- Key changes or new features  
Single volume snapshots allow incremental, point-in-time backups of individual SAN volumes. Only changes since the last snapshot are captured, optimizing storage and backup efficiency. Snapshots are stored within the SAN, enabling fast deployment of new volumes from snapshots for rapid data recovery or cloning scenarios.

- Target audience affected  
Developers and IT professionals managing storage infrastructure, backup/restore operations, or data protection on Azure Elastic SAN.

- Important notes if any  
This feature enhances data protection and disaster recovery strategies by allowing granular backups at the volume level. It supports efficient backup workflows and quick volume provisioning for test/dev or recovery use cases. No additional infrastructure is required, as snapshots are managed natively within the Elastic SAN resource.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=560899

**Details**:

**Azure Update Report: Generally Available – Single Volume Snapshots on Azure Elastic SAN**

**Background and Purpose of the Update**  
Azure Elastic SAN is a cloud-native, fully managed storage area network (SAN) solution designed to deliver scalable and high-performance block storage for Azure workloads. Previously, snapshot capabilities were limited in granularity. The introduction of single volume snapshots addresses the need for more precise, volume-level data protection and recovery, enabling organizations to safeguard individual SAN volumes with incremental, point-in-time backups.

**Specific Features and Detailed Changes**  
With this update, Azure Elastic SAN now supports the creation of snapshots at the single volume level. These snapshots are incremental, capturing only the changes made since the previous snapshot, which optimizes storage consumption and backup efficiency. The snapshots are stored within the Elastic SAN resource itself, ensuring rapid access and deployment.

Key features include:
- **Incremental Snapshots:** Only data blocks that have changed since the last snapshot are stored, minimizing storage overhead.
- **Point-in-Time Recovery:** Snapshots represent the exact state of a volume at the moment of creation, enabling precise restoration.
- **Volume-Level Granularity:** Users can now target individual SAN volumes for backup and recovery operations, rather than being restricted to broader scopes.

**Technical Mechanisms and Implementation Methods**  
The snapshot mechanism leverages Azure’s underlying storage technology to track and store only the differential data between snapshots. When a snapshot is initiated, the system creates a metadata reference to the current state of the volume, and subsequent changes are tracked at the block level. This approach ensures that only unique, changed blocks are stored for each incremental snapshot, reducing both storage costs and the time required for backup operations.

Snapshots are managed and accessed through the Azure portal, CLI, or REST APIs, providing flexibility for automation and integration into existing workflows.

**Use Cases and Application Scenarios**  
- **Backup and Restore:** Organizations can use single volume snapshots for regular backups of critical data, enabling rapid restoration in the event of data corruption or accidental deletion.
- **Dev/Test Environments:** Snapshots allow teams to quickly clone or deploy new volumes from a specific point in time, facilitating testing, development, or troubleshooting scenarios.
- **Compliance and Audit:** Point-in-time snapshots support regulatory requirements for data retention and recovery.

**Important Considerations and Limitations**  
- **Snapshot Storage:** Snapshots reside within the Elastic SAN resource, so storage planning must account for the cumulative size of incremental snapshots.
- **Performance Impact:** While incremental snapshots are designed to be efficient, frequent snapshot operations may have an impact on performance, depending on workload and volume size.
- **Recovery Scope:** Snapshots are at the volume level; restoring a snapshot will revert the entire volume to the captured state.

**Integration with Related Azure Services**  
Single volume snapshots on Azure Elastic SAN can be integrated with Azure Backup and automation tools via Azure CLI or REST APIs, supporting streamlined backup strategies and disaster recovery workflows. They complement existing Azure storage solutions, enabling consistent data protection across hybrid and cloud-native environments.

**Summary Sentence**  
Azure Elastic SAN’s general availability of single volume snapshots enables efficient, incremental, point-in-time backups for individual SAN volumes, enhancing data protection and operational agility for enterprise workloads.

---

### 5. Generally Available: AVS Support for AV64 SKU on Azure Elastic SAN

**Published**: May 05, 2026 16:00:38 UTC
**Link**: [Generally Available: AVS Support for AV64 SKU on Azure Elastic SAN](https://azure.microsoft.com/updates?id=560894)

**Update ID**: 560894
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Elastic SAN now supports AV64 SKUs for Azure VMware Solution (AVS) deployments. This update is generally available.

- Key changes or new features  
AVS deployments can now use AV64 SKUs with Elastic SAN datastores, providing higher scalability and improved storage performance. This enables larger and more demanding VMware workloads to leverage Elastic SAN’s capabilities for storage.

- Target audience affected  
This update is relevant for IT professionals and developers managing or deploying Azure VMware Solution environments, especially those requiring high-performance or large-scale storage solutions.

- Important notes if any  
Organizations can now design AVS environments with greater storage flexibility and performance by combining AV64 SKUs and Elastic SAN. Review your current AVS architecture to determine if migrating to AV64 SKUs with Elastic SAN can optimize your workloads. No additional configuration is required beyond standard AVS and Elastic SAN setup procedures. For more details, refer to the official Azure documentation.

**Details**:

**Azure Update Technical Explanation: AVS Support for AV64 SKU on Azure Elastic SAN (Generally Available)**

**Background and Purpose of the Update:**  
This update introduces general availability of Azure Elastic SAN datastore support for AV64 SKUs within Azure VMware Solution (AVS) deployments. The primary goal is to provide AVS users with access to higher-scale and higher-performance storage options by leveraging the capabilities of the AV64 SKU in conjunction with Azure Elastic SAN. This enhancement addresses the growing demand for scalable and performant storage in enterprise-grade VMware workloads hosted on Azure.

**Specific Features and Detailed Changes:**  
- **AV64 SKU Support:** The AV64 SKU is now officially supported for use with Azure Elastic SAN datastores in AVS environments.  
- **Elastic SAN Integration:** AVS clusters can now attach Elastic SAN as a datastore, utilizing the AV64 SKU’s increased performance and capacity characteristics.  
- **Performance and Scale:** This update enables larger and more demanding workloads to be supported, as AV64 SKUs offer higher throughput and IOPS compared to lower-tier SKUs.

**Technical Mechanisms and Implementation Methods:**  
- **Elastic SAN as Datastore:** Azure Elastic SAN provides block storage resources that can be provisioned and mapped as datastores to AVS clusters.  
- **AV64 SKU Utilization:** By selecting the AV64 SKU, organizations can provision AVS nodes with enhanced storage connectivity, taking advantage of the SKU’s optimized throughput and performance parameters.  
- **Integration Workflow:** Administrators can configure Elastic SAN volumes and present them to AVS clusters as datastores, following standard AVS and Elastic SAN provisioning workflows. The AV64 SKU ensures that the underlying infrastructure can handle the required storage performance.

**Use Cases and Application Scenarios:**  
- **Enterprise Workloads:** Ideal for organizations running large-scale VMware workloads on AVS that require high-performance storage, such as databases, analytics, or high-transaction applications.  
- **Storage-Intensive Applications:** Suitable for scenarios where applications demand high IOPS and low latency, leveraging the performance benefits of the AV64 SKU with Elastic SAN.  
- **Scalable Deployments:** Supports environments where storage needs may grow over time, providing a scalable and performant datastore solution.

**Important Considerations and Limitations:**  
- **SKU Selection:** Only the AV64 SKU is supported for this integration; other SKUs may not provide the required performance or compatibility.  
- **General Availability:** The feature is generally available, indicating production readiness, but organizations should verify regional availability and any associated quotas or limits.  
- **Configuration Requirements:** Proper configuration of both AVS and Elastic SAN resources is necessary to ensure optimal performance and reliability.

**Integration with Related Azure Services:**  
- **Azure VMware Solution (AVS):** The update enhances AVS by enabling it to leverage Elastic SAN as a high-performance datastore using the AV64 SKU.  
- **Azure Elastic SAN:** Acts as the underlying storage platform, providing scalable and performant block storage resources to AVS clusters.  
- **Ecosystem Compatibility:** This integration allows seamless use of other Azure services that interact with AVS and Elastic SAN, supporting hybrid and cloud-native VMware architectures.

**Summary:**  
Azure Elastic SAN datastores are now generally available for use with AV64 SKUs in Azure VMware Solution, enabling higher-scale and higher-performance storage options for demanding enterprise workloads.

---


*This report was automatically generated - 2026-05-06 03:02:34 UTC*