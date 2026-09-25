# September 25, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 25, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028

**Published**: September 24, 2026 17:51:23 UTC
**Link**: [Retirement: Azure Communication Services (ACS) standalone services will be retired on September 30, 2028](https://azure.microsoft.com/updates?id=557117)

**Update ID**: 557117
**Data source**: Azure Updates API

**Categories**: Mobile, Web, Azure Communication Services, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of several standalone Azure Communication Services (ACS) offerings, effective September 30, 2028.

- Key changes or new features  
The affected ACS standalone services will no longer be available after the retirement date. This includes APIs and features that are not part of integrated ACS solutions. No new features are being introduced; this is a deprecation notice. Customers are advised to transition to other communication solutions or integrated ACS offerings before the deadline.

- Target audience affected  
Developers and IT professionals who currently use ACS standalone services for building communication features (such as chat, SMS, voice, or video) in their applications.

- Important notes  
Existing ACS standalone services will continue to operate until September 30, 2028, but after that, they will be fully discontinued. Microsoft recommends planning migration strategies well in advance to avoid service disruption. Review your current ACS usage and explore alternative solutions or integrated ACS offerings. For more details and guidance, refer to the official Azure update page: https://azure.microsoft.com/updates?id=557117

**Details**:

**Azure Update Report: Retirement of Azure Communication Services (ACS) Standalone Services (September 30, 2028)**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of several standalone Azure Communication Services (ACS) offerings, effective September 30, 2028. This update is part of Microsoft’s ongoing lifecycle management strategy, ensuring that Azure services remain current, secure, and aligned with evolving customer needs and platform priorities. The retirement aims to streamline communication service offerings and encourage customers to transition to more integrated or updated solutions within the Azure ecosystem.

**Specific Features and Detailed Changes:**  
The update specifically targets standalone ACS services. After September 30, 2028, these services will be discontinued and will no longer be accessible or supported. This means that any applications, workflows, or integrations relying on standalone ACS endpoints or APIs will cease to function unless migrated to alternative solutions. The retirement affects all core ACS functionalities provided as standalone services, including but not limited to telephony, SMS, chat, and video communication features.

**Technical Mechanisms and Implementation Methods:**  
The retirement process will involve decommissioning ACS service endpoints, APIs, and associated resources. Microsoft will gradually phase out support, culminating in a complete shutdown of service availability post-retirement date. Customers are expected to plan and execute migration strategies well in advance, including updating application code, reconfiguring service dependencies, and provisioning new communication resources as needed. Technical teams should monitor Azure notifications and documentation for migration guidance and tooling support.

**Use Cases and Application Scenarios:**  
ACS standalone services are commonly used in scenarios such as customer engagement platforms, telehealth solutions, contact centers, and collaborative applications requiring real-time communication. Organizations leveraging ACS for SMS notifications, video conferencing, or chat functionalities will need to assess their current deployments and identify alternative Azure communication solutions or third-party integrations to maintain continuity.

**Important Considerations and Limitations:**  
- After September 30, 2028, all standalone ACS services will be unavailable, and existing implementations will fail unless migrated.
- Customers must review their ACS usage, inventory affected resources, and plan for migration to avoid service disruption.
- No further updates, bug fixes, or technical support will be provided for retired ACS services.
- Migration may require code changes, reconfiguration, and testing to ensure compatibility with new communication platforms.
- It is critical to consult Azure documentation and support channels for official migration paths and recommended alternatives.

**Integration with Related Azure Services:**  
While standalone ACS services are being retired, Microsoft continues to offer integrated communication capabilities within Azure. Customers are encouraged to explore Azure Communication Services as part of broader Azure solutions, such as integration with Microsoft Teams, Azure Logic Apps, and Azure Functions. These integrated services provide enhanced scalability, security, and feature sets, supporting modern communication requirements within the Azure ecosystem.

**Summary Sentence:**  
Microsoft will retire several standalone Azure Communication Services (ACS) offerings on September 30, 2028, requiring customers to migrate their communication workloads to alternative Azure solutions to ensure continued functionality and support.

---

### 2. Generally Available: Instant Access for VM restore points

**Published**: September 24, 2026 16:04:16 UTC
**Link**: [Generally Available: Instant Access for VM restore points](https://azure.microsoft.com/updates?id=572573)

**Update ID**: 572573
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Compute, Azure Disk Storage, Virtual Machines, Compliance, Management, Feature

**Summary**:

- What was updated  
Instant Access for application-consistent restore points on Azure virtual machines (VMs) with Premium v2 or Ultra disks is now generally available.

- Key changes or new features  
This update allows users to start restoring a disk from a restore point immediately after the snapshot is taken, without waiting for the entire restore point to be finalized. This significantly reduces recovery time for VMs, especially those using high-performance disks. Instant Access supports application-consistent restore points, ensuring data integrity for workloads such as databases and enterprise applications.

- Target audience affected  
Developers and IT professionals managing Azure VMs with Premium v2 or Ultra disks, particularly those responsible for backup, disaster recovery, and application availability.

- Important notes  
Instant Access is only available for VMs using Premium v2 or Ultra disks as data disks. This feature enhances recovery speed and reliability for critical workloads. For more details and implementation guidance, refer to the official Azure documentation: [Azure Update Link](https://azure.microsoft.com/updates?id=572573).

**Details**:

**Azure Update Report: Generally Available – Instant Access for VM Restore Points**

**Background and Purpose of the Update:**  
Traditionally, restoring Azure virtual machines (VMs) from restore points could involve significant wait times, especially for large disks or when application-consistent restore points were required. The need for faster recovery times is critical for business continuity and minimizing downtime. This update addresses these requirements by introducing Instant Access for application-consistent restore points, specifically for VMs utilizing Premium v2 or Ultra disks as data disks.

**Specific Features and Detailed Changes:**  
- **Instant Access Availability:** Instant Access is now generally available for application-consistent restore points on VMs with Premium v2 or Ultra data disks.
- **Faster Restore Operations:** With Instant Access, the restoration process can begin as soon as the snapshot of the restore point is created, eliminating the traditional delay associated with preparing the full disk data for access.
- **Support for Advanced Disk Types:** This feature is targeted at VMs using high-performance disk types (Premium v2 and Ultra), which are commonly deployed for mission-critical workloads requiring both high throughput and low latency.

**Technical Mechanisms and Implementation Methods:**  
- **Snapshot-Based Restoration:** When a restore point is created, Azure takes a snapshot of the VM disks. With Instant Access, the system allows you to start the disk restore operation immediately after the snapshot is available, rather than waiting for the entire restore point to be fully materialized.
- **Application-Consistent Restore Points:** These restore points ensure that application data is in a consistent state, typically by leveraging VSS (Volume Shadow Copy Service) or similar mechanisms to quiesce applications before taking the snapshot.
- **Disk Attachment:** The restored disk can be attached to a VM or used to create a new VM as soon as the snapshot is ready, significantly reducing recovery time objectives (RTO).

**Use Cases and Application Scenarios:**  
- **Disaster Recovery:** Organizations can quickly restore critical VMs after accidental deletions, corruption, or ransomware attacks, minimizing service disruption.
- **Test and Development:** Developers can rapidly spin up environments from application-consistent restore points for testing or troubleshooting, improving agility.
- **Patch and Upgrade Rollback:** In scenarios where a patch or upgrade fails, IT teams can quickly revert to a known good state using Instant Access restore points.

**Important Considerations and Limitations:**  
- **Disk Type Requirement:** Instant Access is available only for VMs with Premium v2 or Ultra disks as data disks. VMs using other disk types are not eligible for this feature.
- **Application-Consistent Only:** The feature applies specifically to application-consistent restore points, not crash-consistent or file-consistent restore points.
- **Snapshot Dependency:** Restoration can begin as soon as the snapshot is ready, but full performance may depend on the completion of background data hydration processes.

**Integration with Related Azure Services:**  
- **Azure Backup:** Instant Access enhances the restore experience for VMs protected by Azure Backup, enabling faster recovery from backup restore points.
- **Azure Site Recovery:** Can be leveraged in conjunction with disaster recovery strategies for rapid failover and failback.
- **Azure Resource Manager (ARM):** Restore operations can be automated and managed via ARM templates or Azure PowerShell/CLI, supporting integration into DevOps workflows.

**Summary Sentence:**  
Instant Access for application-consistent restore points on Azure VMs with Premium v2 or Ultra disks is now generally available, enabling IT professionals to begin disk restoration immediately after snapshot creation, thereby significantly reducing recovery times for critical workloads.

---


*This report was automatically generated - 2026-09-25 03:01:49 UTC*