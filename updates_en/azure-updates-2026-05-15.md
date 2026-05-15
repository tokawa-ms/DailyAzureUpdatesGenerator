# May 15, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 15, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Support for workloads with large files in Azure NetApp Files 

**Published**: May 14, 2026 18:00:48 UTC
**Link**: [Generally Available: Support for workloads with large files in Azure NetApp Files ](https://azure.microsoft.com/updates?id=561722)

**Update ID**: 561722
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files now supports file sizes up to 64 TiB for regular volumes, and this feature is now generally available.

- Key changes or new features  
The maximum supported file size for regular volumes in Azure NetApp Files has increased from previous limits to 64 TiB. This enhancement enables seamless migration and operation of workloads that require large files, such as Azure VMware Solution (AVS) virtual machines with large VMDK disks.

- Target audience affected  
Developers and IT professionals managing storage-intensive workloads, particularly those using Azure NetApp Files for enterprise applications, databases, or AVS environments.

- Important notes if any  
This update simplifies migration and management of large files, reducing the need to split or restructure data to fit previous file size limits. It is especially relevant for organizations moving large-scale VMs or data sets to Azure. No additional configuration is required to leverage the new file size limit, but ensure your application and workflow are compatible with larger file handling. For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=561722

**Details**:

**Azure Update Report: Generally Available – Support for workloads with large files in Azure NetApp Files**

**Background and Purpose of the Update:**  
Azure NetApp Files is a high-performance, enterprise-grade file storage service designed for critical workloads that require low latency and high throughput. Many enterprise workloads, such as those running on Azure VMware Solution (AVS), utilize large files (e.g., virtual machine disk files like VMDKs) that often exceed the previous file size limits of Azure NetApp Files. The purpose of this update is to enable seamless migration and operation of such workloads by increasing the maximum supported file size, thus removing a key barrier for customers with large file storage requirements.

**Specific Features and Detailed Changes:**  
With this update, Azure NetApp Files now supports individual file sizes of up to 64 TiB (tebibytes) for regular volumes. This is a significant enhancement over previous limits, allowing customers to store and manage much larger files within a single volume. The change specifically targets workloads that require handling of large files, such as AVS virtual machines with large VMDK disks, but is applicable to any workload utilizing large files.

**Technical Mechanisms and Implementation Methods:**  
The update increases the maximum supported file size for regular volumes in Azure NetApp Files to 64 TiB. This enhancement is made generally available, meaning it is fully supported and ready for production use across supported Azure regions. The underlying technical mechanism involves improvements to the Azure NetApp Files service’s file system capabilities, ensuring that the storage infrastructure can efficiently handle large file operations without compromising performance, reliability, or data integrity.

**Use Cases and Application Scenarios:**  
- **Azure VMware Solution (AVS):** Migration and operation of AVS virtual machines that use large VMDK files, enabling enterprises to move their on-premises VMware workloads to Azure without needing to split or reconfigure large disks.
- **Enterprise Applications:** Support for applications that generate or process large files, such as media and entertainment workloads (video editing, rendering), scientific computing (large datasets), and backup/archival solutions.
- **Database and Analytics:** Storage of large database files or data warehouse workloads that require high-capacity, high-performance file storage.

**Important Considerations and Limitations:**  
- The 64 TiB file size support applies to regular volumes in Azure NetApp Files. Customers should verify that their workloads and applications are compatible with large file handling.
- It is essential to ensure that client operating systems and protocols used (such as NFS or SMB) also support large file sizes.
- Customers must monitor their quota and capacity planning, as storing larger files may impact overall volume and service limits.
- No additional details regarding performance implications, pricing, or region-specific availability are provided in the update; customers should consult Azure documentation for further guidance.

**Integration with Related Azure Services:**  
Azure NetApp Files integrates with a variety of Azure services, including Azure VMware Solution (AVS), enabling direct storage of large VMDK files for virtual machines. This update enhances interoperability with AVS by removing file size constraints. Additionally, it supports integration with other Azure services and workloads that require high-performance, large-scale file storage, such as Azure Virtual Machines, Azure Backup, and analytics services.

**Summary Sentence:**  
Azure NetApp Files now supports individual file sizes up to 64 TiB for regular volumes, enabling seamless migration and operation of workloads with large files—such as AVS virtual machines with large VMDK disks—by removing previous file size limitations and enhancing enterprise storage capabilities.

---

### 2. Generally Available: Managed Identity Support for Azure Files SMB Is now GA

**Published**: May 14, 2026 17:30:02 UTC
**Link**: [Generally Available: Managed Identity Support for Azure Files SMB Is now GA](https://azure.microsoft.com/updates?id=562350)

**Update ID**: 562350
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Files, Features, Compliance, Microsoft Build, Security, Services

**Summary**:

- What was updated  
Managed Identity support for Azure Files SMB access is now generally available (GA).

- Key changes or new features  
Azure Files now allows applications and services to authenticate to SMB shares using Azure Managed Identities, eliminating the need to store static credentials or account keys. Authentication is performed using Entra-issued tokens (formerly Azure AD), supporting Zero Trust security models. This enables seamless, secure access for workloads running on Azure VMs, App Services, and other Azure resources that support managed identities.

- Target audience affected  
Developers and IT professionals managing Azure Files, especially those building or deploying applications that require secure SMB access without handling credentials. This includes teams focused on security, automation, and compliance.

- Important notes if any  
To use this feature, both the client and storage account must be properly configured for managed identity authentication. This GA release helps reduce credential management overhead and improves security posture. Review the official documentation for setup requirements and supported scenarios.  
Link: https://azure.microsoft.com/updates?id=562350

**Details**:

**Azure Update Report: Managed Identity Support for Azure Files SMB Now Generally Available**

**Background and Purpose of the Update**  
Azure Files provides cloud-based file shares accessible via the SMB protocol, commonly used for file storage and sharing in enterprise environments. Traditionally, SMB access required static credentials or storage account keys, which posed security risks and management overhead. The update introduces managed identity support for Azure Files SMB access, aligning with Zero Trust security principles by eliminating the need for static credentials and enabling secure, token-based authentication.

**Specific Features and Detailed Changes**  
With this update, Azure Files now allows applications and services to authenticate SMB access using managed identities. Managed identities are Azure Active Directory (Entra) identities assigned to resources such as virtual machines, web apps, or functions. These identities can now be used to obtain access tokens for SMB file shares, replacing the previous requirement for storage account keys or user credentials. The feature is now generally available (GA), indicating production readiness and full support.

**Technical Mechanisms and Implementation Methods**  
The technical mechanism involves leveraging Azure Entra (formerly Azure Active Directory) to issue access tokens for managed identities. When an application or service with an assigned managed identity attempts to access an Azure Files SMB share, it requests an access token from Entra. This token is then used to authenticate the SMB session, granting access based on the permissions assigned to the managed identity. This process removes the need to embed or manage static credentials within application code or configuration, reducing the attack surface and simplifying credential management.

**Use Cases and Application Scenarios**  
- **Virtual Machines:** VMs with managed identities can mount Azure Files SMB shares without storing credentials, ideal for workloads requiring secure, automated file access.
- **App Services and Functions:** Web apps and Azure Functions can access file shares for logging, data exchange, or configuration, using managed identities for seamless authentication.
- **Enterprise File Sharing:** Organizations can implement secure file sharing between services and users, adhering to Zero Trust principles and minimizing credential exposure.
- **Automated Workflows:** CI/CD pipelines or automation scripts running in Azure can access SMB shares securely using managed identities.

**Important Considerations and Limitations**  
- **Permissions Management:** Access is governed by Azure role-based access control (RBAC) and Entra token issuance. Proper assignment of permissions to managed identities is essential.
- **Token Lifetime:** Access tokens have limited lifetimes and must be refreshed as needed by applications.
- **Compatibility:** Only workloads capable of using managed identities and Entra tokens can utilize this feature. Legacy applications may require refactoring.
- **SMB Protocol Support:** The feature is specific to SMB access; other protocols or access methods may not be supported.
- **GA Status:** As the feature is GA, it is supported for production use, but users should review documentation for any region-specific availability or limitations.

**Integration with Related Azure Services**  
Managed identity support for Azure Files SMB integrates seamlessly with Azure Entra (Azure Active Directory) for authentication and token issuance. It also works with Azure role-based access control (RBAC) for permission management. This feature enhances security and operational efficiency when used with Azure Virtual Machines, App Services, Functions, and other resources capable of managed identity assignment.

**Summary Sentence**  
Azure Files SMB now supports managed identities for authentication, enabling secure, credential-free access for applications and services in alignment with Zero Trust principles, and is now generally available for production use.

---


*This report was automatically generated - 2026-05-15 03:02:08 UTC*