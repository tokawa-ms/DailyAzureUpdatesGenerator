# April 16, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 16, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: End of lift reminder of HBv2/HC-Series/NP-Series Azure Virtual Machine in Azure Batch Pool

**Published**: April 15, 2026 17:30:33 UTC
**Link**: [Retirement: End of lift reminder of HBv2/HC-Series/NP-Series Azure Virtual Machine in Azure Batch Pool](https://azure.microsoft.com/updates?id=559751)

**Update ID**: 559751
**Data source**: Azure Updates API

**Categories**: Compute, Batch, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of HBv2-series, HC-series, and NP-series Azure Virtual Machines (VMs) in Azure Batch pools, effective May 31, 2027.

- Key changes or new features  
Support for the following VM series in Azure Batch pools will end:  
  - HBv2-series (120 AMD EPYC 7V12 vCPUs, 480 GB RAM, 200 Gb/s HDR InfiniBand)  
  - HC-series (44 Intel Xeon Platinum 8168 vCPUs, 352 GB RAM, 100 Gb/s EDR InfiniBand)  
  - NP-series (NVIDIA Tesla V100 GPUs)  
After the retirement date, these VM sizes will no longer be available for new or existing Azure Batch pools.

- Target audience affected  
This update impacts developers, IT professionals, and organizations using HBv2, HC, or NP-series VMs in Azure Batch workloads, such as high-performance computing (HPC), AI, and GPU-accelerated tasks.

- Important notes if any  
Users must migrate their Batch workloads to supported VM series before May 31, 2027, to avoid service disruption. Review current Batch pools and plan migration to newer VM series (e.g., HBv3, ND, NC) as appropriate. No action is needed for other VM types or Azure services outside Batch pools. For more information, refer to the official Azure Update: https://azure.microsoft.com/updates?id=559751

**Details**:

**Azure Update: Retirement of HBv2/HC-Series/NP-Series Azure Virtual Machines in Azure Batch Pools (Effective May 31, 2027)**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of HBv2-series, HC-series, and NP-series Virtual Machines (VMs) within Azure Batch pools, effective May 31, 2027. This update serves as an end-of-life (EOL) reminder for these specific VM sizes in the context of Azure Batch, which is Azure’s managed service for running large-scale parallel and high-performance computing (HPC) batch jobs efficiently in the cloud. The retirement aligns with Azure’s lifecycle management policies, ensuring customers transition to newer, more performant, and secure VM offerings.

**Specific Features and Detailed Changes**  
The following VM series will no longer be supported in Azure Batch pools after the retirement date:
- **HBv2-series**: Notable for 120 AMD EPYC 7V12 vCPUs, 480 GB RAM, and 200 Gb/s HDR InfiniBand connectivity, optimized for memory-intensive and HPC workloads.
- **HC-series**: Featuring 44 Intel Xeon Platinum 8168 vCPUs, designed for compute-intensive workloads.
- **NP-series**: (Details not specified in the update, but typically GPU-enabled VMs for AI and visualization workloads.)

After May 31, 2027, these VM sizes cannot be provisioned in new or existing Azure Batch pools. Existing Batch pools using these VM sizes will need to migrate to supported VM series to maintain service continuity.

**Technical Mechanisms and Implementation Methods**  
Azure Batch pools are logical groupings of compute nodes (VMs) that execute parallel tasks. The retirement means that the Azure Batch resource provider will no longer allow allocation, scaling, or scheduling of jobs to HBv2, HC, or NP-series VMs. Any API calls, ARM templates, or Azure CLI/PowerShell scripts referencing these VM sizes for Batch pools will fail after the retirement date. Customers must update their deployment and scaling scripts to use supported VM sizes.

**Use Cases and Application Scenarios**  
The affected VM series are commonly used in scenarios such as:
- Computational fluid dynamics (CFD)
- Finite element analysis (FEA)
- Molecular modeling
- Rendering and visualization (NP-series)
- Large-scale scientific simulations

Organizations leveraging Azure Batch for these HPC and AI workloads must plan to transition to newer VM series, such as HBv3 or HC-series successors, to ensure continued support and access to the latest hardware features.

**Important Considerations and Limitations**  
- **Migration Required**: Workloads running on HBv2, HC, or NP-series in Azure Batch must be migrated to supported VM sizes before May 31, 2027.
- **No Exceptions**: After the retirement date, the affected VM sizes will be unavailable in Batch pools, potentially causing job failures or service disruptions if not addressed.
- **Testing and Validation**: Customers should validate workload compatibility and performance on replacement VM series prior to migration.

**Integration with Related Azure Services**  
Azure Batch integrates with other Azure services such as Azure Storage (for input/output data), Azure Key Vault (for secrets management), and Azure Monitor (for monitoring and logging). This retirement specifically impacts the compute layer within Batch pools; integration with these services remains unchanged. Customers should ensure that their end-to-end workflows are tested with the new VM series to maintain seamless integration and performance.

**Summary Sentence**  
Microsoft Azure will retire support for HBv2, HC, and NP-series Virtual Machines in Azure Batch pools on May 31, 2027; customers must migrate Batch workloads to supported VM sizes before this date to ensure uninterrupted service.

---

### 2. Generally Available: Encrypt Premium SSD v2 and Ultra Disks with Cross Tenant Customer Managed Keys

**Published**: April 15, 2026 17:15:38 UTC
**Link**: [Generally Available: Encrypt Premium SSD v2 and Ultra Disks with Cross Tenant Customer Managed Keys](https://azure.microsoft.com/updates?id=559761)

**Update ID**: 559761
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Disk Storage, Compliance, Security

**Summary**:

- What was updated  
Azure now supports general availability of cross-tenant customer-managed keys (CMK) encryption for Premium SSD v2 and Ultra Disks.

- Key changes or new features  
Managed disks (Premium SSD v2 and Ultra Disks) can now be encrypted using a customer-managed key stored in an Azure Key Vault that resides in a different Microsoft Entra tenant. This enables organizations to separate disk resources and key management across tenants, supporting advanced security and compliance scenarios such as mergers, acquisitions, or cross-organization collaboration.

- Target audience affected  
Azure developers, IT professionals, and security administrators managing disk encryption, especially those working in multi-tenant environments or with strict compliance requirements.

- Important notes if any  
- Ensure proper permissions and access policies are configured between the source and target tenants for seamless key usage.  
- This feature enhances control over encryption keys and supports scenarios where key management must be isolated from disk resources.  
- Review Azure documentation for implementation details and best practices to avoid misconfiguration or access issues.  

Link: https://azure.microsoft.com/updates?id=559761

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Encrypt Premium SSD v2 and Ultra Disks with Cross Tenant Customer Managed Keys  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=559761)

---

**Background and Purpose of the Update**  
This update introduces the general availability of cross-tenant customer-managed keys (CMK) support for encrypting Premium SSD v2 and Ultra Disks in Azure. Traditionally, customer-managed keys for disk encryption were limited to key vaults within the same Microsoft Entra tenant as the managed disks. The purpose of this update is to enhance data security and compliance by allowing organizations to store and manage encryption keys in an Azure Key Vault located in a different Microsoft Entra tenant than the one hosting the disks.

**Specific Features and Detailed Changes**  
- **Cross-Tenant CMK Support:** Premium SSD v2 and Ultra Disks can now be encrypted using a CMK stored in an Azure Key Vault belonging to a different Microsoft Entra tenant.
- **General Availability:** This feature is now generally available, indicating full support and production readiness.
- **Managed Disk Encryption:** Applies specifically to managed disks of type Premium SSD v2 and Ultra Disks.

**Technical Mechanisms and Implementation Methods**  
- **Key Storage:** The customer-managed key used for disk encryption must reside in an Azure Key Vault, which can now be in a separate Microsoft Entra tenant from the disks.
- **Encryption Process:** When creating or updating a managed disk, administrators can specify the URI of the key in the cross-tenant Key Vault. Azure Disk Encryption will use this key for encrypting the disk data at rest.
- **Access Control:** Proper permissions must be configured to allow the disk’s tenant to access the key in the external tenant’s Key Vault, typically using Azure RBAC and Key Vault access policies.

**Use Cases and Application Scenarios**  
- **Multi-Tenant Organizations:** Enterprises operating across multiple Microsoft Entra tenants can centralize key management in a single tenant while hosting workloads in others.
- **Managed Service Providers (MSPs):** MSPs can manage encryption keys on behalf of customers in their own tenant, while the customer’s workloads run in a separate tenant.
- **Regulatory Compliance:** Organizations with strict compliance requirements can separate key management from data storage, ensuring keys are managed by a different administrative boundary.

**Important Considerations and Limitations**  
- **Supported Disk Types:** This feature is limited to Premium SSD v2 and Ultra Disks only.
- **Key Vault Configuration:** The external Key Vault must be properly configured to allow cross-tenant access, including setting appropriate permissions and network rules.
- **Operational Complexity:** Cross-tenant key management introduces additional complexity in terms of access control, monitoring, and auditing.
- **No Inference Beyond Scope:** The update does not specify support for other disk types or services.

**Integration with Related Azure Services**  
- **Azure Key Vault:** Central to this feature, as it stores the customer-managed keys used for encryption.
- **Microsoft Entra ID (formerly Azure AD):** Used for tenant separation and access control between the disk’s tenant and the Key Vault’s tenant.
- **Azure Disk Encryption:** Utilizes the specified CMK from the cross-tenant Key Vault to encrypt managed disks.

---

**Summary Sentence:**  
Cross-tenant customer-managed key encryption for Premium SSD v2 and Ultra Disks is now generally available, enabling organizations to use encryption keys stored in an Azure Key Vault in a different Microsoft Entra tenant for enhanced security and centralized key management.

---


*This report was automatically generated - 2026-04-16 03:02:24 UTC*