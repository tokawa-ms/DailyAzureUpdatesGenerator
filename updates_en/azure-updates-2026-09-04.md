# September 04, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 04, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions 

**Published**: September 03, 2026 17:17:08 UTC
**Link**: [Generally Available: Azure Virtual Network Manager IPAM in additional Azure regions ](https://azure.microsoft.com/updates?id=570557)

**Update ID**: 570557
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure Virtual Network Manager, Features, Management, Regions & Datacenters, Services

**Summary**:

- What was updated  
Azure Virtual Network Manager’s IP Address Management (IPAM) feature is now generally available in additional Azure regions: US Gov Virginia, US Gov Texas, US Gov Arizona, China North 3, and China East 3.

- Key changes or new features  
The IPAM capability within Azure Virtual Network Manager enables centralized management, tracking, and organization of IP address spaces across complex cloud network environments. With this update, organizations operating in the newly supported Azure regions can now leverage IPAM for improved visibility, automated IP address allocation, and conflict prevention across their virtual networks.

- Target audience affected  
This update primarily impacts IT professionals, network administrators, and cloud architects managing Azure environments in US Government and China regions. Developers working on networked applications in these regions may also benefit from improved network reliability and simplified IP address management.

- Important notes if any  
Organizations with regulatory or sovereignty requirements in US Gov or China regions can now use Azure’s native IPAM capabilities to streamline network operations and ensure compliance. No additional configuration is required if you are already using Azure Virtual Network Manager; the feature is available immediately in the newly supported regions. For more information, refer to the official Azure documentation.

**Details**:

**Azure Update Report: Azure Virtual Network Manager IPAM Now Generally Available in Additional Azure Regions**

**Background and Purpose of the Update**  
Azure Virtual Network Manager (AVNM) IP Address Management (IPAM) is designed to streamline and automate the management of IP addresses within Azure environments. The update announces the general availability of AVNM IPAM in new regions: US Gov Virginia, US Gov Texas, US Gov Arizona, China North 3, and China East 3. This expansion addresses the needs of organizations operating in these regions, particularly those with complex network architectures or regulatory requirements, by providing advanced IP address management capabilities natively within Azure.

**Specific Features and Detailed Changes**  
With this update, AVNM IPAM is now accessible in the aforementioned Azure regions. IPAM enables centralized management of IP address spaces, allocation, and tracking across multiple virtual networks. Key features include:
- Centralized visibility and control over IP address usage within Azure subscriptions.
- Automated IP address allocation and reclamation, reducing manual errors and conflicts.
- Support for tracking IP address assignments across virtual networks and subnets.
- Enhanced reporting and auditing capabilities for compliance and operational efficiency.

**Technical Mechanisms and Implementation Methods**  
AVNM IPAM leverages Azure’s native networking infrastructure to provide a unified management layer. It integrates with Azure Resource Manager (ARM) to orchestrate IP address assignments and maintain consistency across resources. IPAM operates by:
- Maintaining a database of IP address pools, subnets, and allocations.
- Enforcing policies for IP address assignment and usage.
- Providing APIs and portal interfaces for administrators to configure, monitor, and report on IP address utilization.
- Synchronizing with Azure networking resources to ensure real-time updates and accuracy.

**Use Cases and Application Scenarios**  
Typical scenarios for AVNM IPAM include:
- Large enterprises managing multiple Azure virtual networks across regions, requiring centralized IP address governance.
- Government and regulated industry customers in US Gov and China regions needing compliant and auditable IP address management.
- Organizations seeking to automate IP address allocation and reduce operational overhead in complex cloud environments.
- Multi-region deployments where consistent IP address policies are critical for connectivity, security, and application performance.

**Important Considerations and Limitations**  
- AVNM IPAM is now generally available only in the specified regions; customers in other regions must verify availability.
- Integration and usage may require updates to existing network management workflows and tooling.
- Compliance requirements in government and China regions may necessitate additional configuration or auditing steps.
- Existing IP address management solutions may need to be migrated or integrated with AVNM IPAM for unified management.

**Integration with Related Azure Services**  
AVNM IPAM is tightly integrated with Azure Virtual Network Manager, Azure Resource Manager, and Azure networking services. It can be used alongside:
- Azure Virtual Networks and Subnets for automated IP address allocation.
- Azure Policy for enforcing IP address management standards.
- Azure Monitor and Azure Security Center for auditing and monitoring IP address usage and security.

**Summary Sentence**  
Azure Virtual Network Manager IP address management is now generally available in US Gov Virginia, US Gov Texas, US Gov Arizona, China North 3, and China East 3, providing centralized, automated IP address management capabilities for complex network environments in these regions.

---

### 2. Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.

**Published**: September 03, 2026 16:09:44 UTC
**Link**: [Generally Available: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.](https://azure.microsoft.com/updates?id=565103)

**Update ID**: 565103
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery, Management, Feature

**Summary**:

- What was updated  
Azure Site Recovery now generally supports replication and disaster recovery for Linux Azure Virtual Machines (VMs) with NVMe disk controllers.

- Key changes or new features  
Support is added for Linux VMs running on NVMe-enabled Generation 2 VM families, including Da/Ea/Fa v6-series and Ebsv5/Ebdsv5, in Azure-to-Azure disaster recovery scenarios. This enables seamless replication and failover for workloads using NVMe-based disks.

- Target audience affected  
Developers and IT professionals managing Linux workloads on Azure, especially those using Generation 2 VMs with NVMe disk controllers, and teams responsible for business continuity and disaster recovery planning.

- Important notes if any  
This support is currently limited to Azure-to-Azure scenarios and specific VM series (Da/Ea/Fa v6-series and Ebsv5/Ebdsv5). Ensure your VMs meet these requirements before enabling replication. Review Azure Site Recovery documentation for any additional prerequisites or configuration steps.

[Read the official update](https://azure.microsoft.com/updates?id=565103)

**Details**:

**Comprehensive Technical Explanation: Azure Site Recovery Support for Linux Azure VMs with NVMe Disk Controllers**

**Background and Purpose of the Update**  
Azure Site Recovery (ASR) is a disaster recovery solution designed to ensure business continuity by enabling replication, failover, and recovery of workloads running on Azure Virtual Machines (VMs). Historically, ASR has supported a wide range of VM configurations, but support for Linux VMs utilizing NVMe disk controllers was previously unavailable. The purpose of this update is to extend ASR’s capabilities to Linux VMs running on NVMe-enabled Generation 2 VM families, addressing the growing demand for high-performance storage and disaster recovery in enterprise environments.

**Specific Features and Detailed Changes**  
With this update, ASR now supports replication and disaster recovery for Linux Azure VMs that use NVMe disk controllers, specifically within Generation 2 VM families. Supported VM series include Da/Ea/Fa v6-series and Ebsv5/Ebdsv5, which are known for their enhanced performance characteristics and NVMe-based storage subsystems. The update is applicable in Azure-to-Azure scenarios, meaning replication and failover are supported between Azure regions for these VM types.

**Technical Mechanisms and Implementation Methods**  
ASR leverages Azure’s native replication mechanisms to capture and synchronize disk data from the source VM to a target region. For NVMe-enabled VMs, the replication process is optimized to handle the unique characteristics of NVMe storage, such as high throughput and low latency. The implementation ensures that the disk controller type (NVMe) is preserved during replication and failover, maintaining the integrity and performance profile of the original VM. The process involves configuring ASR for the supported VM series, enabling replication, and managing failover/failback operations through the Azure portal or REST APIs.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations running performance-sensitive Linux workloads on NVMe-enabled Azure VMs, such as databases, analytics engines, and high-throughput applications. Typical scenarios include:
- Enterprise disaster recovery planning for Linux workloads requiring NVMe storage.
- Migration of high-performance Linux applications across Azure regions.
- Ensuring business continuity for mission-critical services hosted on Da/Ea/Fa v6-series and Ebsv5/Ebdsv5 VMs.

**Important Considerations and Limitations**  
- The support is limited to Azure-to-Azure replication scenarios; cross-cloud or on-premises replication is not covered.
- Only Linux VMs with NVMe disk controllers on specified Generation 2 VM families (Da/Ea/Fa v6-series and Ebsv5/Ebdsv5) are supported.
- Users must ensure their VM configurations match the supported series and disk controller type before enabling ASR.
- There may be additional prerequisites or configuration steps required for NVMe disk support; refer to official Azure documentation for details.

**Integration with Related Azure Services**  
ASR integrates seamlessly with other Azure services, including Azure Backup, Azure Monitor, and Azure Automation. This enables comprehensive disaster recovery workflows, monitoring of replication health, and automated failover processes. The update enhances the overall Azure ecosystem by allowing NVMe-enabled Linux VMs to participate in enterprise-grade disaster recovery strategies.

**Summary**  
Azure Site Recovery now provides general availability support for replication and disaster recovery of Linux Azure VMs with NVMe disk controllers in select Generation 2 VM families, enabling high-performance workloads to benefit from robust Azure-to-Azure disaster recovery capabilities.

---


*This report was automatically generated - 2026-09-04 03:02:00 UTC*