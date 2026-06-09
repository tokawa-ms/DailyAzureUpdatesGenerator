# June 09, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 09, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Update: Minimum billable object size for cooler storage tiers

**Published**: June 08, 2026 23:45:02 UTC
**Link**: [Update: Minimum billable object size for cooler storage tiers](https://azure.microsoft.com/updates?id=559756)

**Update ID**: 559756
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage, Pricing & Offerings

**Summary**:

- What was updated  
The planned introduction of a minimum billable object size for Azure Blob Storage’s cool, cold, and archive access tiers has been paused.

- Key changes or new features  
Previously, Microsoft announced that starting July 1, 2026, objects stored in cool, cold, and archive tiers would be subject to a minimum billable size. This update pauses that change, meaning there will be no new minimum billable object size enforcement on that date. Billing behavior remains unchanged for all new and existing storage accounts.

- Target audience affected  
Developers and IT professionals managing Azure Blob Storage, especially those optimizing costs for workloads using cool, cold, or archive tiers.

- Important notes if any  
No action is required at this time. Continue to use cool, cold, and archive storage tiers as before. Microsoft will provide further updates regarding any future changes to billing policies for these tiers. Monitor the Azure Updates page for the latest information.

**Details**:

**Azure Update Report: Minimum Billable Object Size for Cooler Storage Tiers**

**Background and Purpose of the Update**  
Azure Storage offers multiple access tiers—Cool, Cold, and Archive—to optimize costs for infrequently accessed data. Previously, Microsoft announced the introduction of a minimum billable object size for these cooler storage tiers, intended to align billing with industry standards and ensure cost efficiency for storing small objects. This update was scheduled to take effect on July 1, 2026.

**Specific Features and Detailed Changes**  
With this update, Microsoft is pausing the planned introduction of a minimum billable object size for the Cool, Cold, and Archive access tiers. As a result, there will be no changes to the current billing behavior for these storage tiers on July 1, 2026. Both new and existing storage accounts will continue to be billed based on the actual object size stored, without the imposition of a minimum billable size per object.

**Technical Mechanisms and Implementation Methods**  
No technical changes or new mechanisms are being introduced as part of this update. The billing engine for Azure Blob Storage will continue to calculate storage costs based on the actual size of each object within the Cool, Cold, and Archive tiers. There will be no enforcement of a minimum billable object size, and no additional configuration or migration steps are required from customers or administrators.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations that store large numbers of small objects in the Cool, Cold, or Archive tiers, such as backup files, logs, or IoT telemetry data. These customers will continue to benefit from billing that reflects the true size of their stored objects, without incurring additional costs due to a minimum object size threshold. The update ensures cost predictability and maintains the current cost structure for scenarios that involve granular data storage.

**Important Considerations and Limitations**  
- The billing model for Cool, Cold, and Archive tiers remains unchanged; there is no minimum billable object size.
- The pause applies to both new and existing storage accounts.
- No action is required from customers at this time.
- Microsoft has indicated that further updates regarding minimum billable object size may be provided in the future, so customers should monitor Azure Updates for any changes.
- This update does not affect other aspects of Azure Storage billing, such as transaction costs or data retrieval charges.

**Integration with Related Azure Services**  
The update is specific to Azure Blob Storage’s Cool, Cold, and Archive access tiers. It does not impact integration with other Azure services such as Azure Data Lake Storage, Azure Backup, or Azure Site Recovery. Customers leveraging these services in conjunction with Blob Storage can continue their current configurations and workflows without modification.

**Summary Sentence**  
Microsoft has paused the introduction of a minimum billable object size for Azure Storage’s Cool, Cold, and Archive tiers, ensuring that billing will continue to reflect actual object sizes for all storage accounts beyond July 1, 2026, with no immediate changes required from customers.

---

### 2. Generally Available: Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines

**Published**: June 08, 2026 18:15:14 UTC
**Link**: [Generally Available: Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines](https://azure.microsoft.com/updates?id=565271)

**Update ID**: 565271
**Data source**: Azure Updates API

**Categories**: Launched, Features

**Summary**:

- What was updated  
Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines (NCv6-series VMs) are now generally available in the Southeast Asia and West US 2 regions.

- Key changes or new features  
The NCv6-series VMs are powered by NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs, each with 96 GB of GPU memory. These VMs offer high-performance GPU capabilities suitable for AI/ML training and inference, graphics rendering, and visualization workloads. The new series provides improved compute and memory performance, supporting demanding enterprise and research scenarios.

- Target audience affected  
Developers, data scientists, and IT professionals working with GPU-accelerated workloads, including AI/ML, deep learning, HPC, and advanced visualization applications.

- Important notes if any  
The NCv6-series VMs are now available in Southeast Asia and West US 2, with potential expansion to other regions in the future. Users should review region availability and consider updating deployment scripts or infrastructure-as-code templates to leverage the new VM series. For optimal performance, ensure your workloads and drivers are compatible with the NVIDIA Blackwell architecture.  

[More details](https://azure.microsoft.com/updates?id=565271)

**Details**:

**Azure Update Report: Generally Available – Azure NC RTX PRO 6000 Blackwell Server Edition v6 Series Virtual Machines**

**Background and Purpose of the Update**  
Microsoft Azure has announced the general availability of NCv6-series virtual machines in the Southeast Asia and West US 2 regions. This update introduces VMs powered by NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs. The purpose of this update is to provide customers with access to advanced GPU capabilities for high-performance workloads, supporting the increasing demand for compute-intensive applications such as AI, machine learning, and graphics rendering.

**Specific Features and Detailed Changes**  
The NCv6-series VMs are equipped with NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs. Each GPU features 96 GB of memory, enabling substantial computational throughput and memory bandwidth for demanding workloads. This series represents a significant upgrade in GPU resources compared to previous NC-series VM generations, offering enhanced performance for parallel processing, deep learning model training, and large-scale data analytics.

**Technical Mechanisms and Implementation Methods**  
Azure NCv6-series VMs leverage the NVIDIA RTX PRO 6000 Blackwell Server Edition GPU architecture, which is designed for server-grade reliability and performance. The VMs are provisioned in Azure’s cloud infrastructure, allowing users to dynamically allocate GPU resources as needed. The implementation ensures that customers can deploy these VMs in the Southeast Asia and West US 2 regions, utilizing Azure’s global network and resource management capabilities. The VMs can be accessed and managed through Azure Portal, CLI, or ARM templates, integrating seamlessly into existing Azure workflows.

**Use Cases and Application Scenarios**  
Typical use cases for NCv6-series VMs include:
- **AI and Machine Learning:** Training and inference for deep neural networks, large language models, and generative AI workloads.
- **High-Performance Computing (HPC):** Scientific simulations, financial modeling, and engineering analysis requiring massive parallel computation.
- **Graphics Rendering:** Real-time rendering, video processing, and visualization tasks for media and entertainment industries.
- **Data Analytics:** Processing large datasets for business intelligence, predictive analytics, and big data applications.

**Important Considerations and Limitations**  
- **Regional Availability:** The NCv6-series is currently available only in the Southeast Asia and West US 2 regions, which may impact deployment strategies for global workloads.
- **GPU Memory:** Each GPU provides 96 GB of memory, which is suitable for most large-scale workloads but should be assessed against specific application requirements.
- **VM Quotas:** Users should verify their Azure subscription’s GPU VM quotas and request increases if necessary to deploy NCv6-series VMs at scale.
- **Cost Management:** Due to the high-performance nature of these VMs, cost considerations should be factored into workload planning and resource allocation.

**Integration with Related Azure Services**  
NCv6-series VMs can be integrated with Azure Machine Learning, Azure Batch, and Azure Kubernetes Service (AKS) to orchestrate and scale GPU workloads. They also support Azure Storage for data persistence and Azure Virtual Network for secure connectivity. The VMs can be incorporated into Azure DevOps pipelines for automated deployment and testing of GPU-enabled applications.

**Summary Sentence**  
Azure NCv6-series virtual machines, powered by NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs with 96 GB memory per GPU, are now generally available in Southeast Asia and West US 2 regions, providing high-performance compute resources for AI, HPC, graphics rendering, and analytics workloads.

---

### 3. Generally Available: Premium SSD v2 disks now support non-zonal Azure Virtual Machines 

**Published**: June 08, 2026 18:00:23 UTC
**Link**: [Generally Available: Premium SSD v2 disks now support non-zonal Azure Virtual Machines ](https://azure.microsoft.com/updates?id=565359)

**Update ID**: 565359
**Data source**: Azure Updates API

**Categories**: Launched, Features

**Summary**:

- What was updated  
Premium SSD v2 disks in Azure now support deployment with non-zonal, single-instance virtual machines (VMs) in regions that offer Availability Zones.

- Key changes or new features  
Previously, Premium SSD v2 disks could only be attached to zonal VMs (VMs pinned to a specific Availability Zone). With this update, you can now use Premium SSD v2 disks with non-zonal VMs, meaning you are no longer required to select an Availability Zone when deploying these disks. This provides greater flexibility in VM and disk deployments, especially for workloads that do not require zone-level redundancy.

- Target audience affected  
Azure developers and IT professionals who manage VM storage configurations, particularly those deploying VMs in regions with Availability Zones and who want to leverage Premium SSD v2 disks without zone constraints.

- Important notes if any  
This feature is available only in select Azure regions that support Availability Zones. Review region availability before planning deployments. This update simplifies disk management and can help optimize costs and architecture for non-zonal workloads. For more details and region support, refer to the official Azure documentation.

**Details**:

**Azure Update Report: Premium SSD v2 Disks Support for Non-Zonal Azure Virtual Machines**

**Background and Purpose of the Update:**  
Previously, Azure Premium SSD v2 disks were available only for zonal deployments, requiring customers to select an Availability Zone (AZ) when provisioning virtual machines (VMs) in regions with AZ support. This limited the flexibility for customers who wanted to deploy single-instance, non-zonal VMs but still benefit from the performance and features of Premium SSD v2 disks. The purpose of this update is to expand Premium SSD v2 disk support to non-zonal, single-instance VMs in select Azure regions with AZs, thereby increasing deployment options and simplifying infrastructure design.

**Specific Features and Detailed Changes:**  
With this update, customers can now attach Premium SSD v2 disks to non-zonal VMs in regions that offer Availability Zones. The key change is the removal of the requirement to select an AZ when deploying Premium SSD v2 disks with VMs. This means that Premium SSD v2 disks are now available for both zonal and non-zonal VM configurations, allowing for greater deployment flexibility. The update is generally available and applies to select Azure regions that support AZs.

**Technical Mechanisms and Implementation Methods:**  
The implementation involves extending the disk provisioning logic within Azure to allow Premium SSD v2 disks to be attached to VMs that are not associated with a specific Availability Zone. When deploying a VM, customers can now select Premium SSD v2 as their disk type without specifying an AZ, and the disk will be provisioned as a non-zonal resource. This change is managed through Azure Resource Manager (ARM) templates, the Azure portal, and CLI tools, ensuring consistent deployment workflows across all supported interfaces.

**Use Cases and Application Scenarios:**  
- **Single-instance VM Deployments:** Customers who require high-performance storage for single-instance workloads but do not need zonal redundancy can now leverage Premium SSD v2 disks.
- **Simplified Infrastructure:** Organizations can deploy non-zonal VMs with Premium SSD v2 disks, reducing complexity in scenarios where zone selection is unnecessary.
- **Cost Optimization:** Non-zonal deployments may help optimize costs for workloads that do not require the additional availability provided by AZs.
- **Development and Testing:** Teams can use Premium SSD v2 disks in non-zonal VMs for development or test environments, where zonal resilience is not a priority.

**Important Considerations and Limitations:**  
- **Region Availability:** This feature is available only in select Azure regions that support Availability Zones. Customers should verify region support before planning deployments.
- **Resilience:** Non-zonal VMs do not benefit from the fault isolation provided by AZs. Workloads requiring high availability should still consider zonal deployments.
- **Disk Features:** The update does not alter the performance or features of Premium SSD v2 disks; it only changes the deployment scope.
- **Resource Management:** Customers must ensure proper resource management and backup strategies, as non-zonal VMs may have different failure characteristics compared to zonal VMs.

**Integration with Related Azure Services:**  
Premium SSD v2 disks can be used with other Azure services such as Azure Backup, Azure Site Recovery, and Azure Managed Disks. The update ensures compatibility with standard VM management workflows, including ARM templates, Azure CLI, and PowerShell. Integration with monitoring and management tools remains unchanged, allowing customers to leverage existing operational practices.

**Summary Sentence:**  
Azure Premium SSD v2 disks are now generally available for use with non-zonal, single-instance virtual machines in select regions with Availability Zones, enabling greater flexibility and simplified deployment options without requiring zone selection.

---

### 4. Public Preview: Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud are transitioning to a Microsoft Agent 365 license

**Published**: June 08, 2026 17:15:43 UTC
**Link**: [Public Preview: Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud are transitioning to a Microsoft Agent 365 license](https://azure.microsoft.com/updates?id=565171)

**Update ID**: 565171
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Security, Microsoft Defender for Cloud, Features, Pricing & Offerings, Feature

**Summary**:

**What was updated:**  
Microsoft Foundry agent security capabilities within Microsoft Defender for Cloud are moving to a Microsoft Agent 365 license model, effective July 1, 2026.

**Key changes or new features:**  
- Foundry agent security features will no longer be included directly in Microsoft Defender for Cloud.  
- These capabilities will require a Microsoft Agent 365 license going forward.  
- Agent protection in Defender for Cloud will be integrated with Agent 365 observability logs, enhancing monitoring and security insights.

**Target audience affected:**  
- Developers and IT professionals using Microsoft Defender for Cloud with Foundry agent security features.  
- Security and compliance teams managing agent-based protection and observability.

**Important notes:**  
- Organizations relying on Foundry agent security in Defender for Cloud must transition to Microsoft Agent 365 licensing by July 1, 2026, to maintain coverage.  
- Review licensing and integration plans to ensure continued protection and compliance.  
- Plan for updates to automation, monitoring, and security workflows that depend on Foundry agent data, as these will now be sourced from Agent 365 observability logs.

[More details](https://azure.microsoft.com/updates?id=565171)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud are transitioning to a Microsoft Agent 365 license

**Background and Purpose of the Update:**  
This update announces a significant licensing and operational change for organizations using Microsoft Foundry agent security capabilities within Microsoft Defender for Cloud. Effective July 1, 2026, these security features will no longer be available under the current Defender for Cloud license. Instead, access and functionality will transition to a Microsoft Agent 365 license. The primary purpose of this update is to inform IT professionals of the upcoming licensing shift and the underlying changes in how agent protection is delivered and monitored.

**Specific Features and Detailed Changes:**  
- **Licensing Transition:** The Foundry agent security capabilities, previously managed and consumed through Microsoft Defender for Cloud, will require a Microsoft Agent 365 license from July 1, 2026.
- **Observability Logs:** Agent protection within Defender for Cloud will now be powered by Agent 365 observability logs. This represents a shift in the telemetry and monitoring mechanisms used for agent security.
- **Feature Scope:** The update specifically applies to the Foundry agent security capabilities, which are a subset of Defender for Cloud’s broader security features.

**Technical Mechanisms and Implementation Methods:**  
- **Agent 365 Observability Logs:** The technical foundation for agent protection is moving to leverage the observability logs provided by Agent 365. These logs are expected to provide telemetry and monitoring data necessary for security operations, replacing previous mechanisms used by Defender for Cloud for Foundry agents.
- **Integration Path:** Organizations must ensure that their environments are configured to collect, store, and process Agent 365 observability logs to maintain equivalent or improved security visibility and response capabilities.

**Use Cases and Application Scenarios:**  
- **Security Monitoring:** Enterprises using Foundry agents for endpoint or workload protection within Defender for Cloud will need to transition their monitoring and incident response workflows to utilize Agent 365 observability logs.
- **Compliance and Reporting:** Organizations with compliance requirements tied to Defender for Cloud’s Foundry agent capabilities should review the impact of the licensing and telemetry change on their audit and reporting processes.
- **Operational Continuity:** IT teams responsible for security operations must plan for the transition to ensure uninterrupted agent protection and monitoring post-July 2026.

**Important Considerations and Limitations:**  
- **Licensing Impact:** Continued use of Foundry agent security capabilities after July 1, 2026, will require procurement and assignment of Microsoft Agent 365 licenses.
- **Transition Planning:** Organizations should assess their current Defender for Cloud deployments and prepare for the operational and administrative changes associated with the new licensing model and observability log integration.
- **Feature Availability:** Only the Foundry agent security capabilities are affected by this transition; other Defender for Cloud features may not be impacted.

**Integration with Related Azure Services:**  
- **Defender for Cloud:** The update directly affects Defender for Cloud, requiring integration with Agent 365 observability logs for continued agent protection.
- **Agent 365:** IT professionals must become familiar with Agent 365’s observability log structure, collection, and analysis to fully leverage the new security monitoring capabilities.

**Summary Sentence:**  
Starting July 1, 2026, Microsoft Foundry agent security capabilities in Microsoft Defender for Cloud will require a Microsoft Agent 365 license, with agent protection powered by Agent 365 observability logs, necessitating operational and licensing adjustments for continued security monitoring.

---

### 5. Public Preview: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.

**Published**: June 08, 2026 17:15:43 UTC
**Link**: [Public Preview: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers.](https://azure.microsoft.com/updates?id=565103)

**Update ID**: 565103
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Site Recovery, Management, Feature

**Summary**:

- What was updated  
Azure Site Recovery now supports replication and disaster recovery for Linux Azure Virtual Machines (VMs) with NVMe disk controllers in the Azure-to-Azure scenario.

- Key changes or new features  
Support has been added for Linux VMs running on NVMe-enabled Generation 2 VM families, including Da/Ea/Fa v6-series and Ebsv5/Ebdsv5. This enables replication and failover capabilities for workloads using high-performance NVMe storage.

- Target audience affected  
Developers and IT professionals managing Linux workloads on Azure, especially those using Generation 2 VMs with NVMe disks for performance-intensive applications.

- Important notes if any  
- This feature is currently in Public Preview and only supports Azure-to-Azure disaster recovery scenarios.  
- Supported VM series include Da/Ea/Fa v6-series and Ebsv5/Ebdsv5.  
- Ensure your Linux VMs are running on supported VM families with NVMe disk controllers to leverage this capability.  
- Review the official documentation for any limitations or prerequisites before enabling replication.

For more details, see the official update: https://azure.microsoft.com/updates?id=565103

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Site Recovery support for Linux Azure VMs with NVMe disk controllers  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=565103)

---

**Background and Purpose of the Update:**  
Azure Site Recovery (ASR) is a disaster recovery and business continuity solution that enables replication, failover, and recovery of workloads hosted on Azure Virtual Machines (VMs). With the increasing adoption of NVMe-enabled Generation 2 VM families for Linux workloads, there was a gap in disaster recovery support for these high-performance VMs. This update addresses that gap by introducing public preview support for Linux Azure VMs running on NVMe disk controllers, specifically in Azure-to-Azure replication scenarios.

---

**Specific Features and Detailed Changes:**  
- **Supported VM Families:** The update enables ASR support for Linux VMs on NVMe-enabled Generation 2 VM families, including Da/Ea/Fa v6-series and Ebsv5/Ebdsv5 series.
- **Replication and Disaster Recovery:** ASR can now replicate these Linux VMs and orchestrate failover and recovery operations between Azure regions.
- **Scope:** The support is currently limited to Azure-to-Azure scenarios, meaning replication and recovery are available only between Azure regions and not for on-premises or other cloud environments.

---

**Technical Mechanisms and Implementation Methods:**  
- **NVMe Disk Controller Support:** NVMe (Non-Volatile Memory Express) disk controllers provide high throughput and low latency storage access. ASR’s replication engine has been enhanced to handle the specific disk formats and controller interfaces used by NVMe-enabled VMs.
- **Generation 2 VM Compatibility:** Generation 2 VMs offer improved security and performance features. ASR’s agent and orchestration mechanisms have been updated to ensure compatibility with these VM types and their boot architectures.
- **Replication Workflow:** The replication process involves capturing disk changes from the source VM, transferring them securely to the target region, and applying them to a standby VM configured with NVMe disk controllers.

---

**Use Cases and Application Scenarios:**  
- **High-Performance Linux Workloads:** Organizations running performance-sensitive Linux applications (such as databases, analytics, or AI workloads) on NVMe-enabled VMs can now ensure business continuity using ASR.
- **Regional Disaster Recovery:** Enterprises can replicate Linux VMs across Azure regions to protect against regional outages, ensuring minimal downtime and data loss.
- **Compliance and SLA Requirements:** Businesses with strict recovery time objectives (RTO) and recovery point objectives (RPO) can leverage this feature for enhanced disaster recovery planning.

---

**Important Considerations and Limitations:**  
- **Preview Status:** The feature is in public preview, which may involve limited support and possible changes before general availability.
- **Scope Limitation:** Support is restricted to Azure-to-Azure replication; on-premises or cross-cloud scenarios are not included.
- **VM Family Restriction:** Only specific NVMe-enabled Generation 2 VM families (Da/Ea/Fa v6-series, Ebsv5/Ebdsv5) are supported. Other VM types or disk controllers are not covered by this update.
- **Linux Only:** The update applies exclusively to Linux VMs; Windows VMs with NVMe disk controllers are not mentioned.

---

**Integration with Related Azure Services:**  
- **Azure Site Recovery:** Seamlessly integrates with ASR’s orchestration, monitoring, and automation features.
- **Azure VM Management:** Works alongside Azure VM provisioning and management tools for Generation 2 VM families.
- **Azure Storage:** Utilizes Azure’s storage infrastructure for secure replication and recovery of NVMe disk data.

---

**Summary Sentence:**  
Azure Site Recovery now supports replication and disaster recovery for Linux Azure VMs running on NVMe-enabled Generation 2 VM families in Azure-to-Azure scenarios, providing enhanced business continuity for high-performance workloads.

---

### 6. Generally Available: Maintenance control for Azure Database for PostgreSQL - reschedule, apply on demand, view and download

**Published**: June 08, 2026 17:15:43 UTC
**Link**: [Generally Available: Maintenance control for Azure Database for PostgreSQL - reschedule, apply on demand, view and download](https://azure.microsoft.com/updates?id=563756)

**Update ID**: 563756
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Maintenance control features for Azure Database for PostgreSQL Flexible Server are now generally available.

- Key changes or new features  
Users can now reschedule maintenance windows, apply maintenance updates on demand, and view or download maintenance event details. These enhancements provide improved visibility into upcoming platform maintenance and greater flexibility to manage when updates are applied, helping to minimize service disruption.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL Flexible Server instances.

- Important notes if any  
These capabilities allow teams to better align maintenance with business needs, ensuring critical workloads experience minimal downtime. It is recommended to regularly review and manage maintenance schedules using these new controls to optimize database availability and performance.

[Read the official update](https://azure.microsoft.com/updates?id=563756)

**Details**:

**Azure Update Report: Maintenance Control for Azure Database for PostgreSQL Flexible Server**

**Background and Purpose of the Update**  
The update introduces enhanced maintenance control capabilities for Azure Database for PostgreSQL Flexible Server, now generally available. The primary purpose is to provide IT professionals with greater visibility and flexibility in managing platform maintenance events. This aims to minimize operational disruptions by allowing administrators to better plan and execute maintenance activities according to their organizational requirements.

**Specific Features and Detailed Changes**  
The update delivers several new features:
- **Rescheduling Maintenance:** Administrators can now reschedule platform maintenance events, enabling them to align maintenance windows with business-critical operations and reduce impact on workloads.
- **Apply Maintenance On Demand:** Maintenance can be applied on demand, giving users the ability to trigger updates when it is most convenient for their environment.
- **View Maintenance Events:** Users can view upcoming and past maintenance events, providing transparency into the maintenance history and schedule.
- **Download Maintenance Logs:** Maintenance event details can be downloaded for auditing and compliance purposes, supporting operational governance.

These features collectively enhance control over the maintenance lifecycle, allowing for proactive management and improved operational continuity.

**Technical Mechanisms and Implementation Methods**  
The maintenance control capabilities are integrated into the Azure Database for PostgreSQL Flexible Server platform. Administrators interact with these features through the Azure Portal, Azure CLI, or REST APIs. The platform maintains a schedule of maintenance events, which can be queried, rescheduled, or triggered manually. Maintenance logs and event details are generated and made available for download, supporting traceability and compliance. The underlying mechanism ensures that maintenance operations are executed in a controlled manner, with minimal disruption to database services.

**Use Cases and Application Scenarios**  
- **Mission-Critical Workloads:** Organizations running workloads that require high availability can use rescheduling and on-demand maintenance to avoid downtime during peak business hours.
- **Compliance and Auditing:** Downloadable maintenance logs support regulatory compliance and internal auditing processes.
- **Change Management:** IT teams can integrate maintenance control into their change management workflows, ensuring maintenance aligns with planned releases or updates.
- **Operational Transparency:** Viewing maintenance events provides stakeholders with visibility into platform changes, supporting informed decision-making.

**Important Considerations and Limitations**  
- Maintenance control is available only for Azure Database for PostgreSQL Flexible Server.
- The ability to reschedule or apply maintenance on demand may be subject to platform constraints, such as mandatory updates or critical security patches.
- Maintenance logs and event details are limited to the scope of platform maintenance; application-level events are not included.
- Proper planning is required to avoid conflicts with business operations when rescheduling maintenance.

**Integration with Related Azure Services**  
Maintenance control features integrate seamlessly with Azure management tools, including Azure Portal, Azure CLI, and REST APIs. This allows for automation and scripting within broader Azure workflows. The update supports operational governance and compliance, complementing Azure Monitor and Azure Policy for tracking and enforcing maintenance-related activities.

**Summary Sentence**  
Enhanced maintenance control for Azure Database for PostgreSQL Flexible Server is now generally available, offering IT professionals improved flexibility and visibility to reschedule, apply, view, and download maintenance events, thereby reducing operational disruption and supporting compliance.

---

### 7. Public Preview: Azure Managed Redis now supports Entra ID based RBAC for data management 

**Published**: June 08, 2026 16:15:40 UTC
**Link**: [Public Preview: Azure Managed Redis now supports Entra ID based RBAC for data management ](https://azure.microsoft.com/updates?id=564873)

**Update ID**: 564873
**Data source**: Azure Updates API

**Categories**: In preview, Azure Managed Redis, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Managed Redis now supports Microsoft Entra ID-based role-based access control (RBAC) for data management in public preview.

- Key changes or new features  
Developers and IT professionals can now use Entra ID identities to assign granular permissions (read, write, administer) for Redis data access, eliminating the need for shared access keys. This RBAC model is built on Redis Access Control Lists (ACLs), enabling secure and auditable access management. Integration with Entra ID streamlines identity and access management, aligning Redis with enterprise security standards.

- Target audience affected  
Azure Managed Redis users, including developers, DevOps engineers, and IT administrators responsible for securing and managing Redis data access.

- Important notes if any  
This feature is in public preview and may not be suitable for production workloads yet. Transitioning to Entra ID-based RBAC improves security posture by reducing reliance on shared secrets and enabling centralized access control. Review documentation for configuration steps and limitations during the preview phase.

Data source: Using API data  
[Azure Update Link](https://azure.microsoft.com/updates?id=564873)

**Details**:

**Azure Update Report: Public Preview – Azure Managed Redis now supports Entra ID based RBAC for data management**

**Background and Purpose of the Update:**  
Traditionally, access to Azure Managed Redis has relied on shared access keys, which can pose security and management challenges, especially in environments requiring granular access control and strict auditing. The introduction of role-based access control (RBAC) for Azure Managed Redis data access addresses these concerns by enabling precise, identity-based permissions management. This update leverages Microsoft Entra ID (formerly Azure Active Directory) to authenticate and authorize users, aligning Redis data access with enterprise security standards and best practices.

**Specific Features and Detailed Changes:**  
- **RBAC Integration:** Azure Managed Redis now supports RBAC for data access, allowing administrators to assign specific roles (such as read, write, or admin) to users or service principals authenticated via Microsoft Entra ID.
- **Fine-Grained Permissions:** Permissions can be tailored to individual users or groups, eliminating the need for distributing and managing shared keys.
- **Access Control List (ACL) Foundation:** The RBAC implementation is built on top of Redis Access Control Lists (ACLs), ensuring compatibility with Redis-native security features while extending them with Azure’s identity management capabilities.

**Technical Mechanisms and Implementation Methods:**  
- **Authentication:** Users authenticate to Azure Managed Redis using their Microsoft Entra ID credentials, rather than a static access key.
- **Authorization:** Upon authentication, RBAC policies determine the level of access (read, write, or admin) granted to the user, based on their assigned roles in Entra ID.
- **Policy Enforcement:** The Redis instance enforces access policies at the data operation level, leveraging underlying ACL mechanisms to permit or deny specific commands or actions.

**Use Cases and Application Scenarios:**  
- **Enterprise Security Compliance:** Organizations can enforce least-privilege access and comply with regulatory requirements by assigning only necessary permissions to users and applications.
- **Multi-Tenant Applications:** SaaS providers can segregate access for different tenants or user groups without managing separate Redis instances or keys.
- **DevOps and Automation:** Service principals or managed identities can be granted programmatic access for CI/CD pipelines or automation scripts, with permissions scoped to operational requirements.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads requiring guaranteed stability or support.
- **Migration Planning:** Existing deployments using shared keys will need to transition to Entra ID-based RBAC, which may involve changes to client authentication mechanisms and access workflows.
- **Feature Scope:** The update specifically addresses data access management; administrative operations outside of data commands may still require traditional access methods or additional configuration.

**Integration with Related Azure Services:**  
- **Microsoft Entra ID:** Central to the RBAC implementation, enabling unified identity and access management across Azure resources.
- **Azure Role Assignments:** RBAC roles can be managed using Azure’s standard role assignment tools, facilitating integration with existing governance and compliance processes.
- **Monitoring and Auditing:** Access events can be logged and monitored through Azure Monitor and Entra ID audit logs, supporting security operations and incident response.

**Summary Sentence:**  
Azure Managed Redis now supports Microsoft Entra ID-based RBAC for data management in public preview, enabling precise, identity-driven access control and eliminating the need for shared access keys.

---


*This report was automatically generated - 2026-06-09 03:03:18 UTC*