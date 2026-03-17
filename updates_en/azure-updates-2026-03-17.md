# March 17, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 17, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Retirement: Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027

**Published**: March 16, 2026 18:45:11 UTC
**Link**: [Retirement: Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027](https://azure.microsoft.com/updates?id=549077)

**Update ID**: 549077
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of support for Windows Server 2016 Marketplace images on Azure Batch pools, effective January 12, 2027.

- Key changes or new features  
After January 12, 2027, Azure Batch will no longer support creating or managing pools using Windows Server 2016 Marketplace images. Existing pools running these images will not be supported, and you will not be able to create new pools with them.

- Target audience affected  
This update primarily affects developers, IT professionals, and organizations using Azure Batch pools with Windows Server 2016 Marketplace images for their compute workloads.

- Important notes if any  
Users must migrate their Azure Batch pools to supported Windows Server versions (such as 2019 or 2022) before the retirement date to ensure continued support and security updates. Failure to migrate may result in unsupported workloads and potential security risks. Plan and test your migration strategy in advance to avoid service disruption.

For more details, see the official update: https://azure.microsoft.com/updates?id=549077

**Details**:

**Azure Update Technical Explanation**

**Title:** Retirement: Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027  
**Reference:** [Azure Update Link](https://azure.microsoft.com/updates?id=549077)

---

### Background and Purpose of the Update

Azure Batch is a managed service that enables large-scale parallel and high-performance computing (HPC) workloads in the cloud. To maintain security, compliance, and operational efficiency, Azure Batch periodically retires support for operating systems that have reached their end-of-life (EOL) status. Microsoft ended mainstream support for Windows Server 2016 on January 11, 2022, and extended support will conclude on January 12, 2027. This update informs users that Azure Batch will retire support for Windows Server 2016 Marketplace images on Batch pools effective January 12, 2027.

---

### Specific Features and Detailed Changes

- **Retirement of Windows Server 2016 Marketplace Images:**  
  After January 12, 2027, users will no longer be able to create or manage Azure Batch pools using Windows Server 2016 images from the Azure Marketplace.
- **Impact Scope:**  
  This change applies specifically to Marketplace images; custom images based on Windows Server 2016 are not addressed in this update.
- **No New Deployments:**  
  Creation of new Batch pools with Windows Server 2016 Marketplace images will be blocked post-retirement date.

---

### Technical Mechanisms and Implementation Methods

- **Image Availability:**  
  Azure Batch pools rely on Marketplace images for provisioning compute nodes. After the retirement date, the Windows Server 2016 image references will be removed from the Marketplace, preventing their selection during pool creation or scaling operations.
- **Lifecycle Management:**  
  Existing pools running Windows Server 2016 images may be impacted if nodes are reimaged or the pool is resized, as the retired image will no longer be available for node allocation.
- **Compliance with Microsoft Support Policy:**  
  The retirement aligns Azure Batch’s supported OS lifecycle with Microsoft’s published support timelines for Windows Server products.

---

### Use Cases and Application Scenarios

- **Current Use:**  
  Organizations running HPC, batch processing, or parallel workloads on Azure Batch pools using Windows Server 2016 Marketplace images.
- **Migration Planning:**  
  IT professionals must plan to migrate workloads to supported OS versions (e.g., Windows Server 2019 or later) before the retirement date to ensure continued support and security compliance.

---

### Important Considerations and Limitations

- **Security and Compliance:**  
  Continuing to use unsupported OS images after EOL exposes workloads to security vulnerabilities and compliance risks.
- **Operational Impact:**  
  Pools using Windows Server 2016 Marketplace images will not be able to scale or recover failed nodes using the retired image after January 12, 2027.
- **No Automatic Migration:**  
  Users are responsible for updating their Batch pool configurations to use supported images before the cutoff date.
- **Custom Images:**  
  The update does not specify the impact on custom images based on Windows Server 2016; users should verify support status for custom scenarios.

---

### Integration with Related Azure Services

- **Azure Marketplace:**  
  The retirement is enforced at the Marketplace image level, affecting all services that consume these images via Azure Batch.
- **Azure Batch Pools:**  
  Pool creation, scaling, and node reimaging operations will be directly impacted.
- **Other Azure Services:**  
  While this update is specific to Azure Batch, similar retirement policies may apply to other services utilizing Marketplace images.

---

**Summary:**  
Support for Windows Server 2016 Marketplace images on Azure Batch pools will end on January 12, 2027, requiring users to migrate to supported OS images to maintain security, compliance, and operational continuity.

---

### 2. Retirement: Migration of Azure Batch Low-Priority VMs to Spot VMs in early March

**Published**: March 16, 2026 18:45:11 UTC
**Link**: [Retirement: Migration of Azure Batch Low-Priority VMs to Spot VMs in early March](https://azure.microsoft.com/updates?id=543279)

**Update ID**: 543279
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Retirements

**Summary**:

- What was updated  
Azure Batch is retiring Low-Priority VMs and will migrate existing workloads to Spot VMs starting March 1, 2026.

- Key changes or new features  
Low-Priority VMs in Azure Batch were retired as of September 30, 2025. Beginning March 1, 2026, Azure will automatically migrate any remaining Low-Priority VM workloads in Batch to Spot VMs. This update aligns Azure Batch with the broader Azure Spot VM infrastructure, streamlining VM offerings and management.

- Target audience affected  
Developers and IT professionals using Azure Batch with Low-Priority VMs for cost-effective compute workloads.

- Important notes if any  
- No action is required if you are already using Spot VMs in Azure Batch.  
- If you are still using Low-Priority VMs, review your workloads and test them on Spot VMs before the migration to ensure compatibility and performance.  
- Spot VMs offer similar cost savings but may have different eviction policies and quotas compared to Low-Priority VMs.  
- Review the official documentation and update your Batch job configurations as needed to avoid disruption after the migration.  
- For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=543279

**Details**:

**Azure Update Explanation: Retirement: Migration of Azure Batch Low-Priority VMs to Spot VMs in Early March**

**Background and Purpose of the Update**  
Azure Batch previously offered Low-Priority Virtual Machines (VMs) as a cost-effective compute option for batch workloads that can tolerate interruptions. However, Microsoft has announced the retirement of Low-Priority VMs in Azure Batch, effective September 30, 2025. Beginning March 1, 2026, Azure Batch will initiate a system-driven migration of workloads from Low-Priority VMs to Spot VMs. This update is intended to align Azure Batch with the broader Azure Spot VM infrastructure, streamlining and simplifying the platform’s VM offerings.

**Specific Features and Detailed Changes**  
- **Retirement of Low-Priority VMs:** After September 30, 2025, Low-Priority VMs will no longer be available for use in Azure Batch pools.
- **System-Initiated Migration:** Starting March 1, 2026, Azure Batch will automatically migrate existing workloads configured to use Low-Priority VMs to Spot VMs.
- **Unified Spot VM Offering:** Post-migration, all preemptible compute workloads in Azure Batch will utilize Azure Spot VMs, ensuring consistency with other Azure services.

**Technical Mechanisms and Implementation Methods**  
- **Automatic Migration Process:** The migration from Low-Priority VMs to Spot VMs will be handled by Azure Batch as a system-initiated process, requiring no manual intervention from users.
- **VM Pool Configuration:** Existing Batch pools using Low-Priority VMs will be reconfigured to use Spot VMs. The underlying scheduling and eviction policies will transition to those defined for Spot VMs.
- **Resource Management:** Spot VMs, like Low-Priority VMs, are allocated from surplus Azure compute capacity and can be evicted at any time based on capacity needs and pricing.

**Use Cases and Application Scenarios**  
- **Interruption-Tolerant Workloads:** The migration is relevant for batch processing scenarios such as large-scale data analysis, rendering, and testing, where workloads can tolerate VM interruptions.
- **Cost Optimization:** Spot VMs provide similar cost benefits as Low-Priority VMs, making them suitable for non-critical, parallelizable, or checkpointed jobs.

**Important Considerations and Limitations**  
- **Eviction Policies:** Spot VMs may have different eviction policies or pricing models compared to Low-Priority VMs. Users should review Spot VM documentation to understand these changes.
- **Timeline:** Users must plan for the retirement of Low-Priority VMs by September 30, 2025, and be aware that system-initiated migration will commence on March 1, 2026.
- **Testing and Validation:** It is recommended to test workloads on Spot VMs prior to migration to ensure compatibility and performance expectations.
- **No Manual Intervention Required:** The migration is managed by Azure, but users should monitor their Batch pools and update automation or scripts as needed.

**Integration with Related Azure Services**  
- **Azure Spot VMs:** After migration, all preemptible compute in Azure Batch will use Spot VMs, leveraging the same infrastructure and management features available in other Azure services.
- **Azure Batch Pools:** The update affects how Batch pools are configured and managed, but does not change the integration between Azure Batch and other services such as Azure Storage or Azure Active Directory.

**Summary Sentence**  
Azure Batch will retire Low-Priority VMs on September 30, 2025, and will begin automatically migrating workloads to Spot VMs from March 1, 2026, aligning with Azure’s unified Spot VM infrastructure and simplifying the platform’s compute offerings.

---

### 3. Public Preview: Entra ID-Based Access for Azure Blob Storage SFTP

**Published**: March 16, 2026 18:30:34 UTC
**Link**: [Public Preview: Entra ID-Based Access for Azure Blob Storage SFTP](https://azure.microsoft.com/updates?id=558662)

**Update ID**: 558662
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Blob Storage, Features

**Summary**:

- What was updated  
Microsoft has announced the public preview of Microsoft Entra ID-based access for Azure Blob Storage SFTP.

- Key changes or new features  
This update allows users to authenticate and authorize SFTP access to Azure Blob Storage using Microsoft Entra ID identities. This includes support for both internal users and guest users via Entra External Identities. With this feature, SFTP permissions can now be managed through Entra ID roles and policies instead of traditional local storage account keys or shared access signatures.

- Target audience affected  
This update is relevant for developers and IT professionals managing secure file transfer workflows, especially those leveraging SFTP for integration with Azure Blob Storage. Organizations with external collaborators or partners can now provide secure, identity-based SFTP access.

- Important notes if any  
- The feature is currently in public preview and may be subject to changes before general availability.  
- Integration with Entra ID simplifies access management and improves security by enabling centralized identity and access control.  
- Existing SFTP workflows using local users or access keys can be migrated to Entra ID-based authentication for enhanced security and compliance.  
- Review the official documentation for configuration steps and limitations during the preview phase.  

[Learn more](https://azure.microsoft.com/updates?id=558662)

**Details**:

**Azure Update Report: Public Preview – Entra ID-Based Access for Azure Blob Storage SFTP**

**Background and Purpose of the Update**  
This update introduces Microsoft Entra ID-based access for Azure Blob Storage SFTP, now available in public preview. The primary goal is to enhance security and simplify identity management by allowing organizations to leverage Microsoft Entra ID (formerly Azure Active Directory) identities—including guest users via Entra External Identities—for authenticating and authorizing SFTP access to Azure Blob Storage. This addresses the need for centralized identity and access management, reducing reliance on local or shared credentials.

**Specific Features and Detailed Changes**  
- **Entra ID Authentication for SFTP:** Users can now authenticate to Azure Blob Storage over SFTP using their Microsoft Entra ID credentials.
- **Support for Guest Users:** External collaborators can be granted SFTP access using Entra External Identities, supporting B2B scenarios.
- **Centralized Access Management:** Access policies and permissions are managed through Entra ID, aligning with organizational security and compliance requirements.
- **Public Preview Availability:** The feature is currently in public preview, allowing organizations to test and evaluate its capabilities.

**Technical Mechanisms and Implementation Methods**  
- **Identity Integration:** SFTP access is integrated with Microsoft Entra ID, enabling single sign-on (SSO) and multi-factor authentication (MFA) for enhanced security.
- **Role Assignment:** Access to Blob Storage via SFTP is governed by Entra ID roles and permissions, providing granular control over who can connect and what operations they can perform.
- **Guest Access via Entra External Identities:** Organizations can invite external users and assign them appropriate roles, enabling secure cross-organization collaboration without managing separate credentials.
- **Connection Flow:** When connecting to Blob Storage via SFTP, users authenticate using their Entra ID credentials, which are validated against the directory before access is granted.

**Use Cases and Application Scenarios**  
- **Secure File Transfer:** Enterprises can securely transfer files to and from Azure Blob Storage using SFTP, authenticated by Entra ID.
- **B2B Collaboration:** External partners and vendors can be granted temporary or limited SFTP access using Entra External Identities, streamlining onboarding and offboarding.
- **Centralized Access Control:** Organizations can enforce consistent access policies across SFTP and other Azure resources by managing permissions in Entra ID.

**Important Considerations and Limitations**  
- **Preview Feature:** As this is a public preview, the feature may not be suitable for production workloads and may be subject to changes.
- **Supported Scenarios:** Only scenarios explicitly supported in the public preview documentation should be used; unsupported configurations may not function as expected.
- **Compliance and Security:** Organizations should review their compliance requirements and ensure that Entra ID-based authentication aligns with their security policies.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** Central to authentication and authorization, providing unified identity management for SFTP access.
- **Azure Blob Storage:** The underlying storage service, now enhanced with Entra ID-based SFTP access.
- **Entra External Identities:** Enables secure external user access, facilitating B2B and partner collaboration scenarios.

**Summary:**  
Microsoft has introduced public preview support for Microsoft Entra ID-based access to Azure Blob Storage via SFTP, allowing both internal and external users to securely authenticate using Entra ID identities and enabling centralized, policy-driven access management.

---

### 4. Retirement: End of life reminder of NVv3 and NVv4-series Azure virtual machine in Azure Batch pools 

**Published**: March 16, 2026 18:30:34 UTC
**Link**: [Retirement: End of life reminder of NVv3 and NVv4-series Azure virtual machine in Azure Batch pools ](https://azure.microsoft.com/updates?id=516070)

**Update ID**: 516070
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Features, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of NVv3 and NVv4-series Azure Virtual Machines (VMs) in Azure Batch pools. Support for these VM sizes will end on September 30, 2026.

- Key changes or new features  
After September 30, 2026, NVv3 and NVv4-series VMs—including all listed SKUs (e.g., Standard_NV12s_v3, Standard_NV24ms_v3, Standard_NV48s_v3, NVv4)—will no longer be available for deployment in Azure Batch pools. Existing pools using these VM sizes must be migrated to supported alternatives before the retirement date.

- Target audience affected  
This update impacts developers, IT professionals, and organizations using NVv3 or NVv4-series GPU-enabled VMs in Azure Batch workloads, particularly those relying on NVIDIA Tesla M60 or AMD Radeon Instinct MI25 GPUs for compute or graphics acceleration.

- Important notes if any  
To avoid service disruption, review your Azure Batch pools and plan migration to supported VM sizes before the retirement date. Evaluate alternative GPU VM series (e.g., NVadsA10 v5, NC, ND) that meet your workload requirements. No action is required if you are not using NVv3 or NVv4-series VMs. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=516070).

**Details**:

**Azure Update Technical Explanation: Retirement: End of life reminder of NVv3 and NVv4-series Azure virtual machine in Azure Batch pools**

**Background and Purpose of the Update:**  
Microsoft Azure has announced the retirement of support for NVv3 and NVv4-series virtual machines (VMs) in Azure Batch pools, effective September 30th, 2026. This update serves as a formal reminder to customers leveraging these VM series, particularly in GPU-accelerated workloads managed through Azure Batch. The purpose is to provide sufficient notice for organizations to plan migration strategies and avoid service disruption.

**Specific Features and Detailed Changes:**  
The retirement affects the following VM SKUs within the NVv3 series, all based on NVIDIA Tesla M60 GPUs:  
- Standard_NV12s_v3  
- Standard_NV12hs_v3  
- Standard_NV24s_v3  
- Standard_NV24ms_v3  
- Standard_NV32ms_v3  
- Standard_NV48s_v3  

Additionally, the NVv4 series is included in this retirement. After September 30th, 2026, these VM sizes will no longer be available for allocation in Azure Batch pools. Existing pools using these VM sizes will need to transition to supported alternatives before the retirement date to maintain operational continuity.

**Technical Mechanisms and Implementation Methods:**  
Azure Batch pools are collections of compute nodes (VMs) used to execute parallel and high-performance computing (HPC) workloads. The NVv3 and NVv4-series VMs are specialized for GPU-accelerated tasks, such as visualization, rendering, and machine learning inference. The retirement process will involve the removal of these VM sizes from the Azure Batch pool configuration options. After the specified date, any attempt to create or resize pools with these VM sizes will fail, and existing pools may be decommissioned or become unsupported.

**Use Cases and Application Scenarios:**  
NVv3 and NVv4-series VMs are commonly used in scenarios requiring GPU acceleration, such as:  
- Graphics rendering and visualization workloads  
- Virtual desktop infrastructure (VDI) with GPU support  
- Machine learning inference and data processing tasks  
- Simulation and modeling applications in engineering and media sectors  
Organizations utilizing these VMs in Azure Batch for automated, large-scale job processing must identify alternative VM series that provide equivalent or superior GPU capabilities.

**Important Considerations and Limitations:**  
- After September 30th, 2026, NVv3 and NVv4-series VMs will be unavailable in Azure Batch pools, impacting any workflows or pipelines dependent on these resources.
- Customers must proactively migrate workloads to supported VM series to avoid service interruption.
- The update does not specify replacement VM series; customers should evaluate current Azure GPU VM offerings (such as NVads, NC, ND, or newer series) for compatibility and performance.
- There is no mention of migration tools or automated transition processes; migration planning and execution are the responsibility of the customer.

**Integration with Related Azure Services:**  
Azure Batch integrates with various Azure services, including Azure Storage, Azure Virtual Network, and Azure Machine Learning. The retirement of NVv3 and NVv4-series VMs may require updates to integration points, such as compute resource selection in Azure Machine Learning pipelines or storage throughput planning for new VM sizes. Customers should review dependencies and update configurations accordingly.

**Summary Sentence:**  
Microsoft Azure will retire NVv3 and NVv4-series GPU VM support in Azure Batch pools on September 30th, 2026, requiring customers to migrate affected workloads to supported VM series to ensure continued service.

---

### 5. Retirement: Flatcar Container Linux for AKS (preview) 

**Published**: March 16, 2026 18:15:54 UTC
**Link**: [Retirement: Flatcar Container Linux for AKS (preview) ](https://azure.microsoft.com/updates?id=557929)

**Update ID**: 557929
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Flatcar Container Linux for AKS (preview). Support will end on June 8, 2026.

- Key changes or new features  
Flatcar Container Linux for AKS (preview) will no longer be supported after June 8, 2026. Until then, users can continue to deploy and manage AKS clusters using this OS image. No new features or enhancements will be added, and only critical security updates will be provided until retirement.

- Target audience affected  
Developers and IT professionals managing Azure Kubernetes Service (AKS) clusters that use Flatcar Container Linux (preview) as the node operating system.

- Important notes if any  
All AKS clusters running Flatcar Container Linux (preview) must be migrated to a supported OS (such as Ubuntu or Mariner) before June 8, 2026, to ensure continued support and security updates. After this date, clusters using Flatcar Container Linux (preview) will not receive any support or updates. Begin planning your migration strategy as soon as possible to avoid service disruption.  
For more information, refer to the official Azure Update: https://azure.microsoft.com/updates?id=557929

**Details**:

**Retirement: Flatcar Container Linux for AKS (preview)**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Flatcar Container Linux for Azure Kubernetes Service (AKS) in preview. This means that support for using Flatcar Container Linux as a node operating system within AKS clusters will end on June 8, 2026. The purpose of this update is to inform users of the deprecation timeline and to encourage migration to supported alternatives before the retirement date.

**Specific Features and Detailed Changes:**  
- **Retirement Date:** Flatcar Container Linux for AKS (preview) will no longer be supported after June 8, 2026.
- **Continued Usage:** Until June 7, 2026, users can continue to deploy and operate AKS clusters with Flatcar Container Linux as the node OS in preview.
- **Change in Support:** After the retirement date, Microsoft will not provide updates, security patches, or technical support for AKS clusters using Flatcar Container Linux.

**Technical Mechanisms and Implementation Methods:**  
- **Node OS Selection:** When creating AKS clusters, users could select Flatcar Container Linux as the underlying node operating system during the preview period.
- **Retirement Process:** After June 8, 2026, the option to deploy new AKS clusters or node pools with Flatcar Container Linux will be removed. Existing clusters using this OS will be unsupported, and users must transition to a supported node OS (such as Ubuntu or Windows) to maintain support and security compliance.

**Use Cases and Application Scenarios:**  
- **Current Use:** Organizations leveraging Flatcar Container Linux for AKS may have chosen it for its container-optimized, minimal OS footprint, and automated update capabilities.
- **Transition Planning:** Workloads running on AKS clusters with Flatcar Container Linux must be migrated to supported alternatives before the retirement date to ensure continued support and security.

**Important Considerations and Limitations:**  
- **End of Support:** After June 8, 2026, Flatcar Container Linux for AKS will not receive updates or support, exposing clusters to potential security and compliance risks.
- **Migration Requirement:** Users must plan and execute migration strategies to supported node operating systems before the retirement date.
- **Preview Status:** The feature was only available in preview, and may not have had full production support or feature parity with other supported node OS options.

**Integration with Related Azure Services:**  
- **AKS Integration:** Flatcar Container Linux was integrated as a selectable node OS for AKS clusters, enabling container-optimized workloads.
- **Migration Path:** Users should evaluate integration with other Azure services (such as Azure Monitor, Azure Policy, and Azure Security Center) when migrating to a supported node OS to ensure compatibility and continued operational monitoring.

**Summary:**  
Support for Flatcar Container Linux for AKS (preview) will be retired on June 8, 2026; users should transition to a supported node operating system before this date to maintain support and security for their AKS clusters.

---


*This report was automatically generated - 2026-03-17 03:03:39 UTC*