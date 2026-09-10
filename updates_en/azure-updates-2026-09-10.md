# September 10, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 10, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: User-bound user delegation SAS for Azure Storage 

**Published**: September 09, 2026 22:30:41 UTC
**Link**: [Generally Available: User-bound user delegation SAS for Azure Storage ](https://azure.microsoft.com/updates?id=569241)

**Update ID**: 569241
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage, Security, Feature

**Summary**:

- What was updated  
Azure Storage now supports the general availability of user-bound user delegation Shared Access Signatures (SAS).

- Key changes or new features  
This update introduces user-bound user delegation SAS, which combines the flexibility of user-delegation SAS with the enhanced security of Entra ID (formerly Azure AD) user-bound access. With this feature, SAS tokens are now tied to a specific Entra ID user, ensuring that only the authenticated user who requested the SAS can use it. This reduces the risk of token misuse if the SAS is leaked or shared, as it cannot be used by other users.

- Target audience affected  
Developers and IT professionals managing secure access to Azure Storage resources, especially those building applications that require delegated, time-limited, and user-specific access to storage data.

- Important notes if any  
To use user-bound user delegation SAS, applications must authenticate users with Entra ID. This feature is recommended for scenarios where fine-grained, user-specific access control is required. Existing SAS mechanisms remain available, but this update provides a more secure option for user delegation. Review your application’s authentication and authorization flows to leverage this enhanced security model.  

[Read more](https://azure.microsoft.com/updates?id=569241)

**Details**:

**Azure Update Report: Generally Available – User-bound User Delegation SAS for Azure Storage**

**Background and Purpose of the Update**  
Azure Storage has long supported Shared Access Signatures (SAS) to enable granular, time-limited access to storage resources. Traditionally, SAS tokens could be account-based or user delegation-based, with the latter leveraging Azure Entra ID (formerly Azure Active Directory) for authentication. However, standard user delegation SAS tokens are not inherently bound to a specific user’s identity, which can present security and compliance challenges in scenarios requiring strict user-level access control. This update introduces user-bound user delegation SAS, enhancing security by tightly coupling SAS tokens to individual Entra ID users.

**Specific Features and Detailed Changes**  
- **User-bound User Delegation SAS**: This new feature allows SAS tokens to be issued that are explicitly bound to a specific Entra ID user.  
- **Enhanced Secure Authentication**: The SAS token now combines the flexibility of user delegation with the assurance that only the designated Entra ID user can use the token.  
- **General Availability**: This capability is now generally available, indicating full support and production readiness across Azure Storage.

**Technical Mechanisms and Implementation Methods**  
- **Token Generation**: When generating a user-bound user delegation SAS, the process requires authentication via Entra ID. The resulting SAS token is cryptographically linked to the specific user’s Entra ID identity.  
- **Access Enforcement**: When a request is made using a user-bound SAS, Azure Storage validates that the request is being made by the same Entra ID user to whom the SAS was issued.  
- **Integration with Entra ID**: The mechanism leverages Entra ID’s authentication and token issuance processes to ensure that user-bound SAS tokens cannot be used by unauthorized users, even if the token is leaked.

**Use Cases and Application Scenarios**  
- **Per-user Secure File Access**: Organizations can issue SAS tokens to individual users for accessing specific blobs or containers, ensuring that only the intended user can access the data.  
- **Delegated Access in Multi-user Applications**: Applications that need to grant temporary storage access to users (e.g., uploading documents or downloading reports) can now do so with strict user-level binding.  
- **Compliance-driven Data Access**: Scenarios requiring auditability and non-repudiation benefit from SAS tokens that are traceable to individual users.

**Important Considerations and Limitations**  
- **Token Scope and Lifetime**: As with all SAS tokens, user-bound SAS tokens should be scoped to the minimum required permissions and set with appropriate expiration times to minimize risk.  
- **Dependency on Entra ID**: This feature requires integration with Azure Entra ID; users must be authenticated via Entra ID to use user-bound SAS tokens.  
- **Backward Compatibility**: Existing SAS mechanisms remain available; user-bound user delegation SAS is an additional option for enhanced security.

**Integration with Related Azure Services**  
- **Azure Storage**: Fully supported across Azure Blob Storage and other Azure Storage services that support user delegation SAS.  
- **Azure Entra ID**: Central to the authentication and authorization process, ensuring user identity is enforced at the storage access level.  
- **Azure RBAC and Monitoring**: Can be used in conjunction with Azure Role-Based Access Control (RBAC) and monitoring solutions for comprehensive access management and auditing.

**Summary Sentence**  
User-bound user delegation SAS for Azure Storage is now generally available, providing enhanced security by binding SAS tokens to individual Entra ID users, thereby enabling precise, user-specific access control for storage resources.

---

### 2. Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS 

**Published**: September 09, 2026 21:24:37 UTC
**Link**: [Generally Available: Azure Ephemeral OS Disk with full caching for VM/VMSS ](https://azure.microsoft.com/updates?id=570551)

**Update ID**: 570551
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Features

**Summary**:

- What was updated  
Azure Ephemeral OS Disk with full caching is now generally available for new Virtual Machines (VMs) and Virtual Machine Scale Sets (VMSS).

- Key changes or new features  
This update enables the full OS disk image to be cached on the VM’s local storage. After the initial caching process, all subsequent OS disk reads are served from local storage, eliminating the need for remote storage access. This enhancement improves VM boot times, reduces read latency, and can enhance overall VM performance. The feature is available for both standalone VMs and VMSS deployments.

- Target audience affected  
Developers and IT professionals deploying or managing Azure VMs and VMSS, especially those with workloads sensitive to disk performance, such as stateless applications, scale-out scenarios, or environments requiring rapid VM provisioning and high availability.

- Important notes if any  
Ephemeral OS disks are ideal for stateless workloads, as data on the OS disk is lost if the VM is deallocated or deleted. Ensure your workloads are designed to handle this behavior. The feature is supported on select VM sizes with sufficient local storage. Review documentation for supported SKUs and best practices before adoption.

Data source: Using API data  
More info: [Azure Update](https://azure.microsoft.com/updates?id=570551)

**Details**:

**Azure Update Report: Generally Available – Azure Ephemeral OS Disk with Full Caching for VM/VMSS**

**Background and Purpose of the Update:**  
The Azure Ephemeral OS Disk with full caching is now generally available for new Virtual Machines (VMs) and Virtual Machine Scale Sets (VMSS). This update addresses the need for improved performance and reduced latency in VM boot and OS operations by leveraging local storage for the operating system disk. The primary purpose is to eliminate dependency on remote storage reads after the OS disk has been fully cached, thereby enhancing VM responsiveness and reliability.

**Specific Features and Detailed Changes:**  
- **Full Caching of OS Disk:** The complete OS image is cached on the VM’s local storage, ensuring that all subsequent reads are served from the local cache rather than remote Azure storage.
- **Availability:** This feature is now generally available, meaning it is production-ready and supported for new deployments of VMs and VMSS.
- **Ephemeral Disk:** The OS disk is ephemeral, meaning it exists only on the local storage of the VM and is not persisted in Azure managed disks. This results in faster provisioning and deletion times.

**Technical Mechanisms and Implementation Methods:**  
- **Local Storage Utilization:** The OS disk is stored on the VM’s local SSD or HDD, depending on the VM size and configuration. After the initial caching process, all OS disk operations (reads) are performed locally.
- **No Remote Storage Reads:** Once the OS disk is fully cached, there are no further reads from Azure remote storage, which reduces latency and improves performance.
- **VM/VMSS Support:** The feature is available for both individual VMs and VMSS, allowing for scalable deployments with consistent performance benefits.

**Use Cases and Application Scenarios:**  
- **Stateless Workloads:** Ideal for stateless workloads where the OS disk does not need to be persisted, such as web servers, microservices, and batch processing nodes.
- **Rapid Scaling:** Suitable for scenarios requiring rapid VM provisioning and deprovisioning, such as auto-scaling environments in VMSS.
- **Performance-Critical Applications:** Beneficial for applications that require fast boot times and high I/O performance from the OS disk.

**Important Considerations and Limitations:**  
- **Ephemeral Nature:** The OS disk is not persisted. Any data stored on the OS disk is lost if the VM is deallocated, deleted, or moved to another host. Persistent data should be stored on separate managed disks or Azure storage services.
- **VM Size Compatibility:** The feature depends on the availability of local storage on the VM size selected. Not all VM sizes support ephemeral OS disks.
- **Backup and Recovery:** Traditional backup and restore mechanisms for OS disks are not applicable. Disaster recovery strategies must account for the ephemeral nature.

**Integration with Related Azure Services:**  
- **VMSS Integration:** Seamlessly integrates with VMSS for large-scale, stateless deployments.
- **Azure Managed Disks:** Ephemeral OS disks are an alternative to managed disks for specific use cases but do not replace managed disks where persistence is required.
- **Azure Storage:** For persistent application data, Azure Storage or managed disks should be used alongside ephemeral OS disks.

**Summary Sentence:**  
Azure Ephemeral OS Disk with full caching is now generally available for new VMs and VMSS, providing enhanced performance by caching the entire OS image on local storage and eliminating remote-storage reads after caching, making it ideal for stateless and performance-critical workloads.

---


*This report was automatically generated - 2026-09-10 03:02:02 UTC*