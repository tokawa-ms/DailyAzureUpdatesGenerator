# September 12, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 12, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Azure Linux with OS Guard in Azure Kubernetes Service

**Published**: September 11, 2026 18:08:28 UTC
**Link**: [Retirement: Azure Linux with OS Guard in Azure Kubernetes Service](https://azure.microsoft.com/updates?id=571257)

**Update ID**: 571257
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Support for Azure Linux with OS Guard in Azure Kubernetes Service (AKS) will be retired on December 10, 2026.

- Key changes or new features  
After December 10, 2026, users will no longer be able to create new Azure Linux node pools with OS Guard in AKS. The recommended replacement is Azure Container Linux, which offers enhanced security and performance features. Existing deployments will not be supported after this date.

- Target audience affected  
This update impacts developers and IT professionals managing AKS clusters using Azure Linux with OS Guard. Teams responsible for container orchestration, platform engineering, and security in AKS environments are directly affected.

- Important notes if any  
To avoid service disruption, migrate workloads from Azure Linux with OS Guard to Azure Container Linux before December 10, 2026. Review your AKS clusters and update deployment templates and automation scripts accordingly. Early migration is recommended to ensure compatibility and continued support. For more information, refer to the official Azure update: https://azure.microsoft.com/updates?id=571257

**Details**:

**Comprehensive Technical Explanation: Retirement of Azure Linux with OS Guard in Azure Kubernetes Service**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of support for Azure Linux with OS Guard in Azure Kubernetes Service (AKS), effective December 10, 2026. The purpose of this update is to transition users from the preview feature, Azure Linux with OS Guard, to its successor, Azure Container Linux. This change aligns with Microsoft’s ongoing efforts to streamline and enhance container-optimized operating systems within AKS, ensuring improved performance, security, and supportability.

**Specific Features and Detailed Changes**  
The retirement specifically affects Azure Linux with OS Guard, a preview feature designed to provide enhanced OS-level security within AKS. After December 10, 2026, users will no longer be able to create new Azure Linux node pools with OS Guard enabled in AKS. The recommended replacement is Azure Container Linux, which is positioned as the new container-optimized OS for AKS node pools. Existing Azure Linux with OS Guard node pools will not be able to be created post-retirement, and users are encouraged to migrate workloads to Azure Container Linux.

**Technical Mechanisms and Implementation Methods**  
Azure Linux with OS Guard leverages OS Guard technology to enforce additional security boundaries at the operating system level, protecting container workloads from potential threats. The transition to Azure Container Linux involves updating AKS node pool configurations to use the new OS image. Azure Container Linux is designed to provide a secure, lightweight, and efficient environment for running containers, and it is fully integrated with AKS for seamless orchestration and lifecycle management. Migration typically involves updating node pool definitions and redeploying workloads to the new OS platform.

**Use Cases and Application Scenarios**  
Azure Linux with OS Guard has been used in scenarios requiring enhanced OS-level security for containerized workloads, such as regulated industries (finance, healthcare) or environments with strict compliance requirements. Azure Container Linux will continue to serve these use cases, offering a modern, container-focused OS with improved support and performance. Typical application scenarios include microservices architectures, DevOps pipelines, and production-grade Kubernetes clusters requiring robust security and operational efficiency.

**Important Considerations and Limitations**  
- After December 10, 2026, creation of new Azure Linux with OS Guard node pools will be blocked in AKS.
- Existing node pools using Azure Linux with OS Guard should be migrated to Azure Container Linux before the retirement date to ensure continued support and security updates.
- Azure Container Linux is the recommended replacement and should be evaluated for compatibility with existing workloads.
- The retirement only affects Azure Linux with OS Guard in AKS; other OS options in AKS are not impacted.
- Users must plan for migration, testing, and validation to avoid disruption to production workloads.

**Integration with Related Azure Services**  
Azure Container Linux is fully integrated with Azure Kubernetes Service, supporting native AKS features such as auto-scaling, managed upgrades, monitoring, and security controls. It also works seamlessly with Azure Container Registry, Azure Monitor, and Azure Security Center, enabling end-to-end container lifecycle management and compliance. Migration to Azure Container Linux ensures continued compatibility with Azure’s ecosystem of container and orchestration services.

**Summary Sentence**  
Support for Azure Linux with OS Guard in Azure Kubernetes Service will end on December 10, 2026, and users are advised to migrate to Azure Container Linux for continued container-optimized OS support in AKS.

---

### 2. Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB)

**Published**: September 11, 2026 15:58:56 UTC
**Link**: [Public Preview: Agentless migration of on-premises SMB file shares to Azure Files (SMB)](https://azure.microsoft.com/updates?id=570910)

**Update ID**: 570910
**Data source**: Azure Updates API

**Categories**: In preview, Migration, Storage, Azure Storage Mover, Features

**Summary**:

- What was updated  
Azure Storage Mover now supports agentless migration of on-premises SMB file shares to Azure Files (SMB), available in public preview.

- Key changes or new features  
The new agentless migration capability allows users to move file data from Windows Server or NAS SMB shares to Azure Files without the need to deploy, register, or maintain a migration agent. This simplifies the migration process, reduces infrastructure overhead, and minimizes operational complexity. The feature supports large-scale migrations and is integrated with Azure Storage Mover’s management and monitoring tools.

- Target audience affected  
This update is relevant for IT professionals and developers responsible for data migration, storage management, and cloud adoption projects. Organizations planning to move file-based workloads from on-premises environments to Azure Files will benefit most.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. Users should review preview limitations and provide feedback to Microsoft. Agentless migration reduces the need for additional on-premises resources and streamlines migration planning. For more details and to participate in the preview, refer to the official Azure Update: https://azure.microsoft.com/updates?id=570910

**Details**:

**Azure Update Report: Public Preview – Agentless Migration of On-Premises SMB File Shares to Azure Files (SMB)**

**Background and Purpose of the Update**  
This update introduces agentless migration capabilities for on-premises SMB file shares to Azure Files (SMB) using Azure Storage Mover, now available in public preview. The primary goal is to simplify and streamline the migration process by eliminating the need for deploying, registering, or maintaining a migration agent. This enhancement is designed to reduce operational overhead and accelerate cloud adoption for organizations managing file data on Windows Server or NAS devices.

**Specific Features and Detailed Changes**  
- **Agentless Migration**: Azure Storage Mover can now migrate file data from on-premises SMB shares directly to Azure Files (SMB) without requiring any migration agent installation on source systems.
- **Supported Sources and Targets**: The solution supports Windows Server and NAS SMB shares as sources, with Azure Files (SMB) as the migration target.
- **Public Preview Availability**: This feature is currently in public preview, allowing organizations to evaluate and adopt the new migration approach before general availability.

**Technical Mechanisms and Implementation Methods**  
- **No Agent Deployment**: Unlike traditional migration solutions that require an agent to be deployed on each source server or device, this agentless approach leverages native SMB protocol access. Azure Storage Mover orchestrates the migration process remotely, connecting to the source SMB shares and transferring data directly to Azure Files.
- **Centralized Management**: The migration workflow is managed centrally via Azure Storage Mover, reducing complexity and the need for on-premises software maintenance.
- **Security and Connectivity**: The migration process requires network connectivity between the on-premises SMB shares and Azure Storage Mover, with appropriate permissions for data access and transfer.

**Use Cases and Application Scenarios**  
- **Data Center Modernization**: Organizations migrating legacy file shares from Windows Server or NAS appliances to Azure Files can leverage this agentless solution to minimize migration friction.
- **Cloud Adoption Acceleration**: Enterprises seeking to consolidate file storage in Azure can now do so without the operational burden of agent deployment and management.
- **Branch Office Data Migration**: Distributed environments with multiple SMB shares can benefit from simplified, centralized migration orchestration.

**Important Considerations and Limitations**  
- **Preview Feature**: As this capability is in public preview, it may not be suitable for production workloads. Users should evaluate and test the feature in non-critical environments.
- **Network Requirements**: Reliable and secure network connectivity between on-premises SMB shares and Azure is essential for successful migration.
- **Feature Scope**: The update specifically supports SMB file shares as sources and Azure Files (SMB) as the target. Other protocols or storage types are not covered in this release.
- **Maintenance and Support**: Since no agent is required, ongoing maintenance is reduced, but users should monitor for updates as the feature progresses toward general availability.

**Integration with Related Azure Services**  
- **Azure Storage Mover**: The migration workflow is orchestrated through Azure Storage Mover, which provides a centralized platform for managing data movement.
- **Azure Files (SMB)**: The migrated data is stored in Azure Files, enabling seamless integration with other Azure services and workloads that rely on SMB file shares.

**Summary**  
Azure Storage Mover now enables agentless migration of on-premises SMB file shares to Azure Files (SMB), streamlining data transfer without the need for agent deployment, and is available in public preview for evaluation and testing.

---


*This report was automatically generated - 2026-09-12 03:01:47 UTC*