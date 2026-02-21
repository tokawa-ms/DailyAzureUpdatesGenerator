# February 21, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 21, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: Azure Premium SSD v2 Disk is now available in Brazil Southeast, and in a third Availability Zone in Malaysia West and Indonesia Central

**Published**: February 20, 2026 19:00:04 UTC
**Link**: [Generally Available: Azure Premium SSD v2 Disk is now available in Brazil Southeast, and in a third Availability Zone in Malaysia West and Indonesia Central](https://azure.microsoft.com/updates?id=557623)

**Update ID**: 557623
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Compute, Azure Disk Storage, Virtual Machines, Services, Features, Regions & Datacenters

**Summary**:

- What was updated  
Azure Premium SSD v2 Disk is now generally available in the Brazil Southeast region (which does not have Availability Zones) and in a third Availability Zone in both Malaysia West and Indonesia Central regions.

- Key changes or new features  
Premium SSD v2 is Azure’s next-generation general-purpose block storage, offering improved performance, scalability, and cost-efficiency compared to previous disk offerings. The expansion means customers in these regions can now deploy workloads using Premium SSD v2 disks, leveraging features such as flexible disk sizes, higher throughput, and lower latency.

- Target audience affected  
Developers and IT professionals managing workloads in Brazil Southeast, Malaysia West, and Indonesia Central regions, especially those requiring high-performance and scalable block storage for applications like databases, virtual machines, and enterprise workloads.

- Important notes if any  
Brazil Southeast does not support Availability Zones, so redundancy options are limited compared to the other regions. For Malaysia West and Indonesia Central, the addition of a third Availability Zone enhances high availability and disaster recovery options. Customers should review their storage requirements and consider migrating to Premium SSD v2 for improved performance and cost benefits where available.

**Details**:

**Background and Purpose of the Update**  
This update announces the general availability of Azure Premium SSD v2 disks in the Brazil Southeast region (which does not have Availability Zones), and in a third Availability Zone in both Malaysia West and Indonesia Central. The purpose is to expand the geographic reach and redundancy options for Azure Premium SSD v2, enabling more customers in these regions to leverage next-generation block storage for their workloads.

**Specific Features and Detailed Changes**  
Azure Premium SSD v2 is a next-generation, general-purpose block storage solution designed for Azure virtual machines. The update specifically introduces:

- Availability of Premium SSD v2 disks in the Brazil Southeast region (single-region, without Availability Zones).
- Expansion to a third Availability Zone in Malaysia West and Indonesia Central, enhancing high availability and disaster recovery options for workloads deployed in these regions.

**Technical Mechanisms and Implementation Methods**  
Azure Premium SSD v2 disks are managed disks that provide improved performance, scalability, and cost efficiency compared to previous generations. They are provisioned and managed through the Azure portal, CLI, PowerShell, or ARM templates, and can be attached to supported Azure Virtual Machines. The addition of a third Availability Zone in Malaysia West and Indonesia Central allows customers to architect solutions with greater fault tolerance by distributing resources across physically separate locations within the same region.

**Use Cases and Application Scenarios**  
Key scenarios for leveraging Azure Premium SSD v2 in these newly supported regions include:

- Hosting mission-critical applications that require consistent high performance and low latency storage.
- Deploying enterprise databases, transactional systems, or analytics workloads that benefit from the improved throughput and IOPS of Premium SSD v2.
- Architecting highly available solutions by distributing VMs and disks across multiple Availability Zones, now including a third zone in Malaysia West and Indonesia Central.
- Supporting customers in Brazil Southeast who require premium disk performance but previously lacked access to this disk type.

**Important Considerations and Limitations**  
- In Brazil Southeast, Premium SSD v2 is available only at the region level, as the region does not support Availability Zones. This limits the ability to architect zone-redundant solutions in this region.
- In Malaysia West and Indonesia Central, the addition is specifically for a third Availability Zone, meaning customers can now deploy across three zones for enhanced resilience.
- Customers should verify VM size and region compatibility for Premium SSD v2 before planning migrations or deployments.

**Integration with Related Azure Services**  
Azure Premium SSD v2 disks integrate seamlessly with Azure Virtual Machines, supporting managed disk features such as snapshots, backup, and disk encryption. They can be used in conjunction with Azure Site Recovery for disaster recovery, Azure Backup for data protection, and Azure Availability Sets or Availability Zones for high availability architectures.

**Summary Sentence**  
Azure Premium SSD v2 disks are now generally available in Brazil Southeast and in a third Availability Zone in Malaysia West and Indonesia Central, providing enhanced performance, availability, and deployment flexibility for enterprise workloads in these regions.

---


*This report was automatically generated - 2026-02-21 03:01:37 UTC*