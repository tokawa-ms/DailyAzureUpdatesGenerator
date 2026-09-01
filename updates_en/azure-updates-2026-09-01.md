# September 01, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 01, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: Per-disk resiliency for Azure VMs

**Published**: August 31, 2026 23:11:39 UTC
**Link**: [Public Preview: Per-disk resiliency for Azure VMs](https://azure.microsoft.com/updates?id=569711)

**Update ID**: 569711
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Disk Storage, Feature

**Summary**:

- What was updated  
Azure has introduced per-disk resiliency for Azure Virtual Machines (VMs) in Public Preview.

- Key changes or new features  
Azure VMs now automatically recover from extended managed disk connectivity loss. If a VM loses access to an attached managed disk for a prolonged period, Azure will shut down the VM and restart it once disk connectivity is restored. This process is automated and requires no manual intervention from customers. The default VM behavior remains unchanged; the new feature enhances resiliency at the disk level.

- Target audience affected  
This update is relevant for developers, IT professionals, and administrators managing Azure VMs with attached managed disks, especially those running critical workloads that require high availability and minimal downtime.

- Important notes if any  
No customer action is required to benefit from this feature; it is enabled by default. The update helps reduce manual recovery efforts and improves VM availability during disk-related incidents. As this is a Public Preview, it is recommended to test the feature in non-production environments and monitor for any issues before full-scale adoption.

Data source: Using API data  
For more details, see the [Azure Update announcement](https://azure.microsoft.com/updates?id=569711).

**Details**:

**Azure Update Report: Public Preview – Per-disk resiliency for Azure VMs**

**Background and Purpose of the Update**  
Azure Virtual Machines (VMs) rely on attached managed disks for persistent storage. Previously, if a VM lost access to a managed disk for an extended period, Azure’s default behavior was to automatically recover the VM by shutting it down and powering it back on once disk connectivity was restored. This process required no manual intervention from customers and was designed to minimize downtime and data loss. The purpose of this update is to enhance VM resiliency by introducing per-disk recovery mechanisms, ensuring more granular and efficient recovery from disk-related failures.

**Specific Features and Detailed Changes**  
With the introduction of per-disk resiliency in public preview, Azure now automatically monitors the connectivity status of each attached managed disk. If a VM loses access to a specific disk for an extended period, Azure triggers an automated recovery workflow for the affected VM. The VM is shut down and subsequently powered back on after disk connectivity is restored. This feature is enabled by default and does not require any customer action, maintaining the existing recovery behavior while providing improved visibility and control at the disk level.

**Technical Mechanisms and Implementation Methods**  
The per-disk resiliency mechanism leverages Azure’s internal monitoring and orchestration capabilities. When a managed disk becomes inaccessible, Azure detects the connectivity loss and initiates a recovery sequence for the VM. The VM is gracefully shut down to prevent potential data corruption and is restarted once the disk is available again. This process is fully automated and integrated into the Azure platform, ensuring consistent and reliable recovery without manual intervention. The update does not alter the underlying VM or disk configurations; instead, it enhances the recovery logic to operate on a per-disk basis.

**Use Cases and Application Scenarios**  
Per-disk resiliency is particularly valuable for workloads that depend on multiple managed disks, such as databases, application servers, and file storage solutions. In scenarios where disk connectivity issues occur, this feature ensures that the VM is automatically recovered, reducing downtime and minimizing operational impact. IT professionals managing large-scale deployments or mission-critical applications can benefit from improved fault tolerance and simplified incident response, as Azure handles disk recovery transparently.

**Important Considerations and Limitations**  
- The feature is currently in public preview and may not be available in all Azure regions or for all VM types.
- The default recovery behavior remains unchanged; VMs are shut down and restarted after disk connectivity is restored.
- No customer action is required to enable or utilize this feature.
- The update does not address other types of VM failures unrelated to disk connectivity.
- Customers should continue to monitor their VMs and disks for overall health and performance, as this feature specifically targets disk connectivity issues.

**Integration with Related Azure Services**  
Per-disk resiliency is natively integrated with Azure Virtual Machines and Azure Managed Disks. It complements existing Azure recovery and monitoring solutions, such as Azure Monitor and Azure Site Recovery, by providing additional automated recovery capabilities at the disk level. IT professionals can leverage this feature alongside their current backup, monitoring, and disaster recovery strategies to enhance overall VM reliability.

**Summary Sentence**  
Azure’s public preview of per-disk resiliency for VMs provides automated recovery from managed disk connectivity issues by shutting down and restarting affected VMs, requiring no customer intervention and maintaining the default recovery behavior.

---

### 2. Public Preview: Azure Multicloud Interconnect

**Published**: August 31, 2026 18:36:12 UTC
**Link**: [Public Preview: Azure Multicloud Interconnect](https://azure.microsoft.com/updates?id=570364)

**Update ID**: 570364
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Networking, Azure ExpressRoute, Services

**Summary**:

- What was updated  
Azure Multicloud Interconnect has entered public preview. This is a managed service enabling private connectivity between Azure and other supported cloud providers, with AWS as the first provider available during the preview.

- Key changes or new features  
  - Provides automated, managed private network connections between Azure and AWS.
  - Simplifies multicloud networking by eliminating the need for manual configuration of VPNs or third-party solutions.
  - Offers integrated monitoring, security, and policy management for intercloud connectivity.
  - Supports high-bandwidth, low-latency connections for workloads spanning Azure and AWS.

- Target audience affected  
  - Cloud architects and IT professionals managing multicloud environments.
  - Developers building applications that require secure, performant connectivity between Azure and AWS resources.
  - Enterprises with hybrid or multicloud strategies.

- Important notes if any  
  - Currently in public preview with AWS as the only supported non-Azure cloud provider; support for additional providers is expected in the future.
  - Service is managed via the Azure portal and APIs.
  - Preview features may be subject to change before general availability.
  - Review documentation for supported regions, pricing, and limitations during the preview phase.

[More details](https://azure.microsoft.com/updates?id=570364)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure Multicloud Interconnect  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=570364)

---

**Background and Purpose of the Update**

Azure Multicloud Interconnect enters public preview as a managed service designed to facilitate private connectivity between Azure and other supported cloud providers. The primary motivation for this update is to address the increasing demand from organizations for secure, reliable, and high-performance inter-cloud networking solutions. As enterprises adopt multicloud strategies, seamless and private connectivity becomes essential for workload migration, hybrid deployments, and cross-cloud application integration. AWS is the first supported provider in this preview, reflecting the need for interoperability between the two largest public cloud platforms.

---

**Specific Features and Detailed Changes**

- **Managed Service:** Azure Multicloud Interconnect is delivered as a managed offering, reducing operational overhead and simplifying network configuration for IT teams.
- **Private Connectivity:** The service enables private, non-public network links between Azure and AWS, bypassing the public internet to enhance security and performance.
- **Provider Support:** AWS is available as the initial supported provider during the preview phase, with potential for additional cloud providers in future releases.
- **Preview Availability:** The service is currently in public preview, allowing customers to evaluate its capabilities and provide feedback.

---

**Technical Mechanisms and Implementation Methods**

Azure Multicloud Interconnect leverages Azure’s networking infrastructure to establish private connections between Azure and AWS environments. The service abstracts the complexity of configuring cross-cloud networking, offering a managed interface for provisioning and monitoring connections. Connectivity is established using secure, dedicated network paths, ensuring data confidentiality and minimizing latency. The service likely utilizes Azure’s existing backbone and partner interconnects to facilitate these links, although specific implementation details are not disclosed in the preview announcement.

---

**Use Cases and Application Scenarios**

- **Hybrid Cloud Architectures:** Organizations running workloads across Azure and AWS can use Multicloud Interconnect to securely link resources, enabling seamless data exchange and application integration.
- **Disaster Recovery and Backup:** Enterprises can replicate data between Azure and AWS using private connectivity, supporting robust disaster recovery strategies.
- **Cross-Cloud Application Deployment:** Applications distributed across Azure and AWS can benefit from low-latency, private communication channels, improving performance and security.
- **Migration Projects:** The service simplifies migration of workloads between Azure and AWS by providing reliable, private network paths.

---

**Important Considerations and Limitations**

- **Preview Status:** As the service is in public preview, it may not offer full production-level guarantees, and features may evolve based on customer feedback.
- **Provider Support:** Only AWS is supported in the current preview; connectivity to other cloud providers is not available at this stage.
- **Service Availability:** Customers should verify regional availability and supported configurations before planning deployments.
- **Integration Requirements:** Existing network architectures may require adjustments to leverage the managed connectivity.

---

**Integration with Related Azure Services**

Azure Multicloud Interconnect can be integrated with Azure networking services such as Azure Virtual Network, ExpressRoute, and Network Security Groups to enhance security and control. It complements Azure’s hybrid and multicloud offerings, providing a foundation for advanced scenarios like Azure Arc-enabled workloads and cross-cloud governance.

---

**Summary Sentence**

Azure Multicloud Interconnect public preview introduces a managed service for private connectivity between Azure and AWS, enabling secure, high-performance inter-cloud networking for multicloud architectures.

---


*This report was automatically generated - 2026-09-01 03:01:41 UTC*