# September 25, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 25, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: Discover and assess PostgreSQL in Azure Migrate 

**Published**: September 24, 2025 17:00:24 UTC
**Link**: [Public Preview: Discover and assess PostgreSQL in Azure Migrate ](https://azure.microsoft.com/updates?id=503641)

**Update ID**: 503641
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Migrate has introduced public preview support for discovering and assessing PostgreSQL workloads across diverse environments including VMware, Hyper-V, physical servers, and other clouds.

- Key changes or new features  
The update enables centralized discovery of PostgreSQL instances, providing insights into configuration, sizing, and dependencies. It facilitates assessment for migration readiness and helps plan migration strategies by estimating costs and compatibility within Azure. This enhancement extends Azure Migrate’s capabilities beyond traditional VM and app assessments to include PostgreSQL database workloads.

- Target audience affected  
Developers and IT professionals responsible for database migration, infrastructure planning, and cloud adoption strategies involving PostgreSQL workloads will benefit from this update. It is particularly useful for teams managing heterogeneous environments aiming to migrate PostgreSQL databases to Azure.

- Important notes if any  
This feature is currently in public preview, so users should expect potential changes and consider it for evaluation and testing purposes rather than production use. Users are encouraged to provide feedback to help improve the service before general availability.  

For more details, visit: https://azure.microsoft.com/updates?id=503641

**Details**:

The recent Azure Migrate public preview introduces the capability to discover and assess PostgreSQL workloads across diverse environments—including VMware, Hyper-V, physical servers, and other clouds—streamlining migration planning for PostgreSQL databases to Azure. This enhancement addresses the growing demand for comprehensive migration tools that support open-source relational databases beyond traditional SQL Server workloads, enabling IT professionals to gain centralized visibility and assessment insights for PostgreSQL as part of their cloud migration strategy.

**Background and Purpose**  
Azure Migrate has traditionally focused on assessing and migrating Windows and Linux servers, virtual machines, and SQL Server databases. However, PostgreSQL’s increasing adoption in enterprises necessitated integrated migration support. This update aims to fill that gap by extending Azure Migrate’s discovery and assessment capabilities to PostgreSQL databases, allowing organizations to evaluate readiness, sizing, and cost estimates for migrating PostgreSQL workloads to Azure Database for PostgreSQL or other managed services. The goal is to simplify migration planning, reduce manual inventory efforts, and provide data-driven recommendations.

**Specific Features and Detailed Changes**  
- **Discovery of PostgreSQL Instances:** Azure Migrate now supports agent-based and agentless discovery of PostgreSQL servers running on VMware, Hyper-V, physical hosts, and other cloud platforms.  
- **Assessment Reports:** The tool generates detailed assessment reports covering compatibility, performance metrics, sizing recommendations, and migration readiness specific to PostgreSQL workloads.  
- **Centralized Management:** PostgreSQL discoveries and assessments are integrated into the existing Azure Migrate hub, allowing unified management alongside other workload assessments.  
- **Support for Multiple Deployment Models:** The assessment supports PostgreSQL instances running on-premises or in other clouds, facilitating heterogeneous migration scenarios.

**Technical Mechanisms and Implementation Methods**  
Azure Migrate uses a combination of agents and discovery tools to collect metadata and performance data from PostgreSQL instances. For VMware and Hyper-V environments, it leverages existing Azure Migrate appliance infrastructure to scan virtual machines and identify PostgreSQL services. For physical servers and other clouds, agents can be installed to gather detailed configuration and workload data. The collected data is analyzed against Azure Database for PostgreSQL capabilities and sizing models to produce assessment reports. The process involves:  
1. Deploying or configuring the Azure Migrate appliance or agents.  
2. Running discovery scans to enumerate PostgreSQL instances and collect telemetry.  
3. Uploading data securely to Azure Migrate service for analysis.  
4. Reviewing assessment outputs in the Azure portal.

**Use Cases and Application Scenarios**  
- Enterprises planning to migrate PostgreSQL workloads from on-premises VMware or Hyper-V environments to Azure Database for PostgreSQL.  
- Organizations consolidating heterogeneous database environments, including physical servers and multi-cloud PostgreSQL instances, into Azure.  
- IT teams seeking to perform readiness assessments and cost estimations before migration projects.  
- Managed service providers offering migration services for PostgreSQL workloads to Azure.

**Important Considerations and Limitations**  
- This feature is currently in public preview; users should expect potential changes and should not use it for production migration without validation.  
- Agent installation may be required on physical or cloud-based PostgreSQL servers, which could involve operational overhead and permissions considerations.  
- The assessment focuses on discovery and sizing; actual migration execution requires complementary tools such as Azure Database Migration Service.  
- Some PostgreSQL extensions or custom configurations may not be fully assessed or supported in the preview.  
- Network connectivity and firewall rules must allow communication between the Azure Migrate appliance/agents and Azure services.

**Integration with Related Azure Services**  
- **Azure Database Migration Service (DMS):** After assessment, users can leverage DMS to perform the actual migration of PostgreSQL databases to Azure Database for PostgreSQL.  
- **Azure Monitor:** Performance data collected during assessment can be correlated with Azure Monitor metrics post-migration for ongoing optimization.  
- **Azure Cost Management:** Sizing and cost estimates from the assessment feed into cost management planning.  
- **Azure Arc:** For hybrid management scenarios

---

### 2. Generally Available: Delete on-demand backup in Azure DB for MySQL - Flexible Server 

**Published**: September 24, 2025 17:00:24 UTC
**Link**: [Generally Available: Delete on-demand backup in Azure DB for MySQL - Flexible Server ](https://azure.microsoft.com/updates?id=503622)

**Update ID**: 503622
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Azure Database for MySQL - Flexible Server now supports manual deletion of on-demand backups, introduced as part of the August 2025 update.

- Key changes or new features  
Previously, users could only create on-demand backups but could not delete them manually. With this update, developers and IT professionals can trigger deletion of specific on-demand backups via API or portal, allowing better management of backup storage and costs. Automated backups and their retention policies remain unaffected. This feature enhances control over backup lifecycle and storage optimization.

- Target audience affected  
Developers, database administrators, and IT professionals managing Azure Database for MySQL - Flexible Server instances who require granular control over backup retention and storage management.

- Important notes if any  
- Deletion applies only to on-demand backups, not automated backups.  
- Use API or Azure portal to manage backup deletions.  
- Helps reduce storage costs by removing unnecessary backups manually.  
- Ensure compliance and data retention policies are considered before deleting backups.  

For more details, visit: https://azure.microsoft.com/updates?id=503622

**Details**:

The recent Azure update for Azure Database for MySQL – Flexible Server introduces the generally available capability to delete on-demand backups, enhancing backup management flexibility beyond the existing automated backup system. Previously, users could create manual backups on-demand but had no direct control to remove these backups, potentially leading to unnecessary storage consumption and increased costs. This update addresses that limitation by enabling IT professionals to manually delete on-demand backups that are no longer needed, thereby optimizing storage usage and cost efficiency.

**Background and Purpose:**  
Azure Database for MySQL – Flexible Server provides a managed MySQL database service with built-in automated backups to ensure data protection and disaster recovery. While automated backups run on a schedule and are managed by the system, on-demand backups allow users to create manual snapshots at critical points, such as before major schema changes or application updates. Prior to this update, these on-demand backups were immutable from the user perspective, causing challenges in managing backup retention and storage costs. The purpose of this update is to empower users with full lifecycle control over on-demand backups, aligning backup management with enterprise data governance and cost optimization strategies.

**Specific Features and Changes:**  
- **Delete On-Demand Backups:** Users can now explicitly delete on-demand backups via Azure Portal, Azure CLI, or REST API. This capability complements the existing manual backup creation feature.  
- **Retention Management:** While automated backups continue to adhere to configured retention policies, on-demand backups can be selectively removed at any time, independent of retention settings.  
- **Integration with Existing Backup Infrastructure:** The deletion operation only applies to on-demand backups and does not affect automated backups or point-in-time restore capabilities.

**Technical Mechanisms and Implementation:**  
- On-demand backups in Flexible Server are stored as discrete backup points within the Azure Backup infrastructure linked to the MySQL Flexible Server resource.  
- The deletion API call triggers a backend process that marks the specified on-demand backup for removal and asynchronously cleans up the associated storage blobs.  
- Role-based access control (RBAC) and Azure Resource Manager (ARM) policies govern permissions for backup deletion, ensuring only authorized users can perform this operation.  
- The Azure CLI and REST API have been extended with new commands and endpoints (`az mysql flexible-server backup delete`) to facilitate scripting and automation of backup lifecycle management.

**Use Cases and Application Scenarios:**  
- **Pre-Upgrade Snapshots:** Create on-demand backups before database schema migrations or application upgrades, then delete them after successful deployment to reduce storage costs.  
- **Compliance and Governance:** Retain critical backups as per compliance requirements and remove redundant ones to maintain an optimal backup repository.  
- **Cost Management:** Actively manage backup storage by deleting obsolete manual backups, especially in environments with frequent manual snapshot creation.  
- **Disaster Recovery Planning:** Combine automated backups with selective manual backups, deleting those that are no longer relevant post-recovery or testing.

**Important Considerations and Limitations:**  
- Deleting an on-demand backup is irreversible; once deleted, the backup cannot be recovered.  
- This feature does not affect automated backups or the ability to perform point-in-time restores within the retention window.  
- Users must ensure proper RBAC permissions are assigned to avoid unauthorized deletion of backups.  
- Backup deletion operations may take some time to complete due to asynchronous cleanup processes.  
- The feature is currently limited to Azure Database for MySQL – Flexible Server and does not apply to Single Server or other database engines.

**Integration with Related Azure Services:**  
- **Azure Portal:** Provides a graphical interface to view, create, and delete on-demand backups.  
- **Azure CLI & REST API:** Enables automation and integration with CI/CD pipelines or backup management scripts.  
- **Azure Monitor & Azure Policy:** Can be used to monitor backup operations and enforce organizational policies on backup retention and deletion.  
- **Azure Cost Management:** Helps track storage costs associated with backups, enabling informed decisions about backup lifecycle management.

In summary, the ability to delete

---

### 3. Retirement: Azure Disk Encryption

**Published**: September 24, 2025 11:45:14 UTC
**Link**: [Retirement: Azure Disk Encryption](https://azure.microsoft.com/updates?id=493779)

**Update ID**: 493779
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machine Scale Sets, Virtual Machines, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Azure Disk Encryption (ADE), effective September 15, 2028.

- Key changes or new features  
After this date, ADE will no longer be supported. Microsoft recommends transitioning to Encryption at Host, which provides disk encryption natively at the hypervisor level. Additionally, CVM OS disk encryption is highlighted as an alternative offering broader operating system support and enhanced security capabilities compared to ADE.

- Target audience affected  
This update primarily affects developers, IT professionals, and cloud administrators who currently use Azure Disk Encryption to secure virtual machine disks.

- Important notes if any  
Organizations should plan and execute migration strategies well before the retirement date to avoid potential security and compliance risks. Encryption at Host offers improved performance and simplified management, making it a preferred solution moving forward. Review your existing encryption configurations and test workloads with Encryption at Host to ensure compatibility and seamless transition. For more details, refer to the official Azure update link.

**Details**:

The Azure update announces the planned retirement of Azure Disk Encryption (ADE) on September 15, 2028, urging customers to transition to Encryption at Host or alternative disk encryption solutions such as CVM OS disk encryption before this date. This update reflects Microsoft’s strategic shift towards more integrated and scalable encryption technologies that enhance security and operational efficiency for Azure virtual machines (VMs).

**Background and Purpose of the Update**  
Azure Disk Encryption has been a key feature enabling encryption of Windows and Linux VM disks using BitLocker and DM-Crypt, respectively, with integration to Azure Key Vault for key management. However, as cloud security paradigms evolve, Microsoft is moving towards Encryption at Host, which encrypts data at the physical host level, providing encryption without the overhead of in-guest encryption agents. This shift aims to simplify encryption management, improve performance, and reduce operational complexity. The retirement announcement provides a clear timeline for customers to plan migration and avoid disruption.

**Specific Features and Detailed Changes**  
- **Azure Disk Encryption (ADE):** Utilizes in-guest encryption technologies (BitLocker for Windows, DM-Crypt for Linux) to encrypt OS and data disks. Requires VM agent and extension installation, and integration with Azure Key Vault for key storage and management.  
- **Encryption at Host:** Encrypts data at the host infrastructure layer transparently to the guest OS, eliminating the need for VM agent extensions. It encrypts all data written to the VM’s disks, including temporary disks, with keys managed by Azure Storage.  
- **CVM OS Disk Encryption:** An alternative solution providing OS disk encryption with broader OS support and improved integration.  

The update signals that after September 15, 2028, ADE will no longer be supported, and customers should migrate workloads to Encryption at Host or other supported encryption mechanisms.

**Technical Mechanisms and Implementation Methods**  
- **Azure Disk Encryption:** ADE requires installation of the Azure Disk Encryption extension on the VM, which configures BitLocker or DM-Crypt inside the guest OS. Keys are stored and managed in Azure Key Vault, enabling centralized key lifecycle management and compliance. ADE encrypts OS and data disks individually.  
- **Encryption at Host:** This feature is enabled at the VM or host level without requiring guest OS changes or extensions. Encryption keys are managed by Azure Storage and hardware security modules (HSMs) in Azure data centers. Encryption at Host protects data at rest on the physical storage layer, including ephemeral disks, with minimal performance impact.  
- **Migration:** Transitioning involves disabling ADE extensions, enabling Encryption at Host on the VM or VM scale set, and verifying encryption status via Azure Portal, CLI, or PowerShell.  

**Use Cases and Application Scenarios**  
- Workloads requiring compliance with data-at-rest encryption standards but seeking simplified management and reduced operational overhead.  
- Enterprises aiming to leverage native Azure infrastructure encryption without modifying VM guest OS configurations.  
- Scenarios where performance is critical and in-guest encryption overhead is undesirable.  
- Customers using ephemeral or temporary disks that need encryption, which ADE does not support but Encryption at Host does.  

**Important Considerations and Limitations**  
- ADE supports granular control over OS and data disk encryption keys via Azure Key Vault, which may be necessary for certain compliance requirements; Encryption at Host uses Azure-managed keys by default, though customer-managed keys are supported for storage accounts.  
- Some legacy operating systems or configurations may not be compatible with Encryption at Host, requiring validation before migration.  
- ADE provides encryption tied to the VM guest OS, which can be beneficial for certain security models; Encryption at Host encrypts at the infrastructure layer, which may affect forensic or incident response processes differently.  
- Migration requires careful planning to avoid downtime or data loss, including backing up keys and data.  

**Integration with Related Azure Services**  
- **Azure Key Vault:** ADE tightly integrates with Key Vault for key management; Encryption at Host leverages Azure Storage encryption

---


*This report was automatically generated - 2025-09-25 03:02:14 UTC*