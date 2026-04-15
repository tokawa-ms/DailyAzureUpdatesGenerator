# April 15, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 15, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: Azure Site Recovery support for Windows Azure VMs with NVMe disk controllers. 

**Published**: April 14, 2026 21:15:15 UTC
**Link**: [Public Preview: Azure Site Recovery support for Windows Azure VMs with NVMe disk controllers. ](https://azure.microsoft.com/updates?id=560241)

**Update ID**: 560241
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Site Recovery, Features, Management

**Summary**:

- What was updated  
Azure Site Recovery (ASR) now supports replication and disaster recovery for Windows Azure Virtual Machines (VMs) with NVMe disk controllers in public preview.

- Key changes or new features  
ASR can now replicate and protect Generation 2 Azure VMs that use NVMe-enabled disk controllers. Supported VM families include Da/Ea/Fa v6-series and Ebsv5/Ebdsv5, specifically in Azure-to-Azure disaster recovery scenarios. This update enables organizations to leverage high-performance NVMe disks while maintaining business continuity and disaster recovery capabilities.

- Target audience affected  
Azure developers and IT professionals managing infrastructure, especially those deploying or maintaining Generation 2 VMs with NVMe disks in supported VM series. This is relevant for teams responsible for business continuity, disaster recovery planning, and those adopting newer VM families for performance workloads.

- Important notes if any  
This feature is currently in public preview and only supports Azure-to-Azure replication scenarios. Review the official documentation for any limitations or prerequisites before enabling ASR for NVMe-enabled VMs. Production workloads should consider the preview status before full-scale adoption.  

Link: https://azure.microsoft.com/updates?id=560241

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Azure Site Recovery support for Windows Azure VMs with NVMe disk controllers

**Background and Purpose of the Update:**  
Azure Site Recovery (ASR) is a disaster recovery (DR) solution that enables business continuity by replicating workloads running on virtual machines (VMs). As Azure introduces more high-performance VM series equipped with NVMe (Non-Volatile Memory Express) disk controllers, there has been a growing need for DR support for these VM types. Previously, ASR did not support VMs with NVMe-enabled disk controllers, limiting DR capabilities for organizations using these high-throughput, low-latency storage options. This update addresses that gap by extending ASR support to Windows Azure VMs running on NVMe-enabled Generation 2 VM families.

**Specific Features and Detailed Changes:**  
- **ASR now supports replication and disaster recovery for Windows Azure VMs with NVMe disk controllers.**
- **Supported VM families include Generation 2 VMs such as Da/Ea/Fa v6-series and Ebsv5/Ebdsv5 series.**
- **The support is specifically for Azure-to-Azure DR scenarios, enabling replication between Azure regions.**

**Technical Mechanisms and Implementation Methods:**  
- **NVMe Disk Controller Support:** ASR can now interact with the NVMe disk subsystem of supported VM series, capturing data changes and orchestrating replication without requiring modifications to the underlying disk architecture.
- **Generation 2 VM Compatibility:** The update leverages the enhanced firmware and boot capabilities of Generation 2 VMs, ensuring that the replication process is compatible with both the UEFI boot process and NVMe storage paths.
- **Azure-to-Azure Replication:** The replication process remains within the Azure ecosystem, utilizing Azure’s native networking and storage replication mechanisms to ensure data consistency and minimal RPO/RTO.

**Use Cases and Application Scenarios:**  
- **High-Performance Workloads:** Organizations running performance-intensive applications (e.g., databases, analytics, transactional systems) on NVMe-enabled VMs can now implement DR strategies using ASR.
- **Business Continuity for Modern VM Series:** Enterprises adopting the latest Generation 2 VM families for their Windows workloads can ensure business continuity and compliance by leveraging ASR for DR.
- **Cross-Region Replication:** Businesses requiring geo-redundancy for critical workloads can replicate NVMe-enabled VMs between Azure regions.

**Important Considerations and Limitations:**  
- **Public Preview:** The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- **Scope:** The update is limited to Windows Azure VMs with NVMe disk controllers in the specified VM families and only supports Azure-to-Azure scenarios.
- **No Mention of Linux Support:** The update specifically refers to Windows VMs; support for other operating systems is not indicated.
- **VM Family Restriction:** Only the Da/Ea/Fa v6-series and Ebsv5/Ebdsv5 series are explicitly supported.

**Integration with Related Azure Services:**  
- **Azure Site Recovery:** This update directly enhances ASR’s capabilities, allowing seamless integration with existing DR workflows.
- **Azure Virtual Machines:** The update ensures that organizations leveraging the latest VM innovations can integrate DR without architectural changes.
- **Azure Storage and Networking:** ASR continues to use Azure’s native storage replication and networking for data transfer and failover orchestration.

**Summary Sentence:**  
Azure Site Recovery now supports replication and disaster recovery for Windows Azure Virtual Machines with NVMe disk controllers in select Generation 2 VM families, enabling Azure-to-Azure DR for high-performance workloads in public preview.

---

### 2. Announcing: Minimum billable object size for cooler storage tiers

**Published**: April 14, 2026 21:15:15 UTC
**Link**: [Announcing: Minimum billable object size for cooler storage tiers](https://azure.microsoft.com/updates?id=559756)

**Update ID**: 559756
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage, Pricing & Offerings

**Summary**:

- What was updated  
Azure has introduced a minimum billable object size for cooler storage tiers (cool, cold, and archive) in Azure Blob Storage and Azure Data Lake Storage (ADLS).

- Key changes or new features  
For objects stored in the cool, cold, or archive tiers, any object smaller than 128 KiB will now be billed as if it were 128 KiB in size. This applies to all storage accounts using these tiers.

- Target audience affected  
This update impacts developers and IT professionals managing storage solutions that use Azure Blob Storage or ADLS, especially those storing large numbers of small files in cool, cold, or archive tiers.

- Important notes if any  
If your workloads involve storing many small objects (less than 128 KiB) in cooler storage tiers, you may see an increase in storage costs due to this minimum billable size. Review your data storage patterns and consider aggregating small files or adjusting your storage tier usage to optimize costs. This change does not affect the hot tier.  
For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=559756).

**Details**:

**Comprehensive Technical Explanation: Azure Update – Minimum Billable Object Size for Cooler Storage Tiers**

**Background and Purpose of the Update**  
Azure Blob Storage and Azure Data Lake Storage (ADLS) offer multiple access tiers—Cool, Cold, and Archive—designed for infrequently accessed data with lower storage costs. To optimize billing consistency and resource utilization, Microsoft is introducing a minimum billable object size for these cooler storage tiers. This change ensures that very small objects stored in these tiers are billed in a way that reflects the underlying storage infrastructure and operational costs.

**Specific Features and Detailed Changes**  
With this update, any object stored in the Cool, Cold, or Archive access tiers of Azure Blob Storage or ADLS that is smaller than 128 KiB will be billed as if it is 128 KiB in size. This means that, for billing purposes, the minimum chargeable size per object in these tiers is now set at 128 KiB. Objects equal to or larger than 128 KiB are billed based on their actual size, while smaller objects are rounded up to this minimum threshold for billing calculations.

**Technical Mechanisms and Implementation Methods**  
The billing system for Azure Blob and ADLS storage accounts is being updated to enforce this minimum billable object size. When calculating storage costs for the Cool, Cold, or Archive tiers, the system will automatically apply a 128 KiB minimum per object. This is a billing-side change only and does not affect the actual stored data or its retrieval. The mechanism is transparent to users in terms of object storage and access; only the billing metrics are impacted.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations storing large numbers of small objects in the Cool, Cold, or Archive tiers. Common use cases include backup archives, compliance data, logs, or telemetry data where objects may be smaller than 128 KiB. For workloads with predominantly larger objects, the impact is minimal. However, for scenarios involving many small files, such as IoT data ingestion or granular log storage, this change may increase overall storage costs, as each small object will be billed at the 128 KiB minimum.

**Important Considerations and Limitations**  
- The minimum billable size applies only to the Cool, Cold, and Archive access tiers; Hot tier objects are not affected.
- The actual data stored is not padded or changed—only the billing calculation is affected.
- Customers should review their storage patterns, especially if they store large numbers of small objects in cooler tiers, to assess potential cost impacts.
- This update does not affect data retrieval, access performance, or API behavior.

**Integration with Related Azure Services**  
This billing change applies to both Azure Blob Storage and Azure Data Lake Storage (ADLS) accounts utilizing the Cool, Cold, or Archive tiers. It is relevant for any Azure service or application that leverages these storage tiers, including Azure Backup, Azure Site Recovery, and custom solutions using the Azure Storage SDKs or REST APIs.

**Summary Sentence**  
Azure Blob and Data Lake Storage now enforce a minimum billable object size of 128 KiB for Cool, Cold, and Archive tiers, meaning any object smaller than 128 KiB in these tiers will be billed as 128 KiB, impacting storage cost calculations for small objects.

---

### 3. Generally Available: Smart Tier (Azure Blob and Data Lake Storage)

**Published**: April 14, 2026 17:15:47 UTC
**Link**: [Generally Available: Smart Tier (Azure Blob and Data Lake Storage)](https://azure.microsoft.com/updates?id=559746)

**Update ID**: 559746
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage, Features

**Summary**:

- What was updated  
Azure Blob Storage and Azure Data Lake Storage (ADLS) now have Smart Tier storage generally available (GA) in most public cloud regions.

- Key changes or new features  
Smart Tier automatically optimizes storage costs by dynamically moving data between hot and cool tiers based on access patterns, without requiring manual tier management. This feature helps reduce costs for workloads with unpredictable or changing access patterns. Smart Tier is available for both block blobs and ADLS Gen2.

- Target audience affected  
Developers and IT professionals managing storage solutions on Azure Blob Storage or ADLS Gen2, especially those with variable or unpredictable data access patterns.

- Important notes if any  
Smart Tier is not available in Israel Central, Qatar Central, and UAE North regions at this time. Users should review pricing and consider Smart Tier for scenarios where data access frequency is difficult to predict. No application changes are required to leverage Smart Tier; it can be enabled via API, SDK, or Azure Portal.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=559746

**Details**:

**Background and Purpose of the Update**  
The General Availability (GA) of Smart Tier for Azure Blob Storage and Azure Data Lake Storage (ADLS) addresses the need for automated and optimized storage cost management. Traditionally, customers have had to manually select storage access tiers (such as Hot, Cool, or Archive) based on their anticipated data access patterns. This process can be complex and may lead to suboptimal cost efficiency if access patterns change or are unpredictable. The Smart Tier is designed to simplify this by automatically optimizing data placement and cost, reducing the operational overhead for IT teams.

**Specific Features and Detailed Changes**  
With this update, Smart Tier is now generally available in nearly all zonal public cloud regions, except Israel Central, Qatar Central, and UAE North. The Smart Tier feature can be enabled for both Azure Blob Storage and Azure Data Lake Storage (ADLS), providing a unified approach to intelligent data tiering. This release marks the transition from preview to a fully supported, production-ready feature.

**Technical Mechanisms and Implementation Methods**  
Smart Tier leverages built-in intelligence to monitor data access patterns and dynamically manage the placement of objects within the most cost-effective storage tier. This is achieved without requiring manual policy configuration or intervention from users. The system automatically tracks how frequently data is accessed and adjusts the storage tier accordingly, ensuring that data is stored in the optimal tier based on real-time usage. The implementation is seamless and integrated into the existing storage account management workflows, allowing IT professionals to enable Smart Tier at the container or account level through the Azure Portal, CLI, or ARM templates.

**Use Cases and Application Scenarios**  
Smart Tier is particularly beneficial for workloads with unpredictable or variable access patterns, such as data lakes, analytics workloads, backup repositories, and content management systems. Organizations that manage large volumes of unstructured data, where access frequency can fluctuate, will benefit from cost savings and reduced administrative effort. It is also suitable for scenarios where IT teams want to minimize the risk of misconfigured tiering policies and ensure consistent cost optimization.

**Important Considerations and Limitations**  
While Smart Tier is generally available in most regions, it is not supported in Israel Central, Qatar Central, and UAE North as of this release. IT professionals should verify regional availability before planning deployments. Additionally, as with any automated system, it is important to monitor billing and access patterns to ensure that Smart Tier is delivering the expected cost benefits. Integration with existing data lifecycle management policies should be reviewed to avoid conflicts or unintended data movements.

**Integration with Related Azure Services**  
Smart Tier integrates natively with Azure Blob Storage and Azure Data Lake Storage (ADLS), supporting seamless operation alongside existing storage features such as access policies, encryption, and monitoring. It can be managed using standard Azure management tools, including the Azure Portal, Azure CLI, and ARM templates, ensuring compatibility with existing automation and infrastructure-as-code practices.

**Summary Sentence**  
Smart Tier for Azure Blob and Data Lake Storage is now generally available in most regions, offering automated, intelligent data tiering to optimize storage costs and simplify management for dynamic and unpredictable workloads.

---


*This report was automatically generated - 2026-04-15 03:02:44 UTC*