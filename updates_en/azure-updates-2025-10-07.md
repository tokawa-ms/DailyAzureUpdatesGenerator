# October 07, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 07, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server 

**Published**: October 06, 2025 20:45:03 UTC
**Link**: [Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server ](https://azure.microsoft.com/updates?id=503636)

**Update ID**: 503636
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports the latest PostgreSQL minor versions: 17.6, 16.10, 15.14, 14.19, 13.22, and 18 Beta 3.

- Key changes or new features  
These updates include the most recent minor version releases, which typically contain important bug fixes, security patches, and performance improvements. The upgrades are applied automatically during Azure’s monthly planned maintenance windows, ensuring minimal disruption and up-to-date database environments.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure Flexible Server benefit from improved stability, security, and compliance with the latest PostgreSQL minor releases. Those leveraging new PostgreSQL features or requiring the latest patches should note these updates.

- Important notes if any  
The inclusion of PostgreSQL 18 Beta 3 support allows early testing of upcoming features but should be used cautiously in production environments. Automatic minor version upgrades help maintain security and performance without manual intervention, but users should review release notes for any breaking changes or deprecated features.  

For more details, visit: https://azure.microsoft.com/updates?id=503636

**Details**:

The recent Azure update announces the general availability of support for the latest PostgreSQL minor versions—specifically 17.6, 16.10, 15.14, 14.19, 13.22, and 18 Beta 3—on Azure Database for PostgreSQL – Flexible Server. This enhancement enables users to benefit from the most recent bug fixes, security patches, and performance improvements inherent in these minor releases, which are automatically applied during Azure’s monthly planned maintenance windows.

**Background and Purpose:**  
Azure Database for PostgreSQL – Flexible Server is a managed database service designed to provide high availability, scalability, and control over PostgreSQL deployments in the cloud. PostgreSQL minor versions typically include critical security updates, stability improvements, and minor feature enhancements without altering the major version’s compatibility. Supporting the latest minor versions ensures that Azure customers can maintain secure, stable, and performant database environments without manual intervention. This update aligns Azure’s managed service with the upstream PostgreSQL community releases, promoting best practices in database maintenance and security.

**Specific Features and Detailed Changes:**  
The update introduces support for the following PostgreSQL minor versions: 17.6, 16.10, 15.14, 14.19, 13.22, and the 18 Beta 3. Each minor version increment generally contains:

- Security patches addressing vulnerabilities discovered since the last release.
- Bug fixes improving query planner stability, replication reliability, and general database engine robustness.
- Performance optimizations, such as improved indexing or vacuuming processes.
- Minor feature enhancements and deprecations consistent with PostgreSQL’s release notes.

The inclusion of PostgreSQL 18 Beta 3 support allows early adopters to test upcoming features in a managed environment, facilitating feedback and preparation for future major version upgrades.

**Technical Mechanisms and Implementation Methods:**  
Azure Database for PostgreSQL – Flexible Server automates minor version upgrades as part of its monthly planned maintenance. This process involves:

- Detecting eligible servers running older minor versions.
- Scheduling upgrades during low-usage maintenance windows to minimize disruption.
- Applying the minor version upgrade in-place, ensuring data integrity and continuity.
- Performing post-upgrade validation checks to confirm service health.

This automation reduces operational overhead for database administrators, eliminating the need for manual patching while maintaining compliance with security standards.

**Use Cases and Application Scenarios:**  
- Enterprises requiring continuous security compliance benefit from automatic patching of known vulnerabilities.  
- Applications with high availability requirements leverage the automated maintenance to reduce downtime risks associated with manual updates.  
- Development and testing teams can utilize PostgreSQL 18 Beta 3 support to validate application compatibility with upcoming PostgreSQL features.  
- Organizations managing multiple PostgreSQL instances can standardize on the latest minor versions to simplify support and troubleshooting.

**Important Considerations and Limitations:**  
- While minor version upgrades are backward-compatible, it is recommended to test application compatibility in staging environments before production rollout.  
- The automatic upgrade process occurs during predefined maintenance windows, which may cause brief service interruptions. Proper scheduling and communication are essential.  
- PostgreSQL 18 Beta 3 is a pre-release version; thus, it should be used cautiously in production environments due to potential instability.  
- Custom extensions or third-party tools should be verified for compatibility with the new minor versions.

**Integration with Related Azure Services:**  
Azure Database for PostgreSQL – Flexible Server integrates seamlessly with Azure Monitor for performance and health monitoring, Azure Backup for data protection, and Azure Security Center for threat detection. The update ensures these integrations continue to function optimally with the latest PostgreSQL engine versions. Additionally, Azure Arc-enabled data services can manage PostgreSQL Flexible Servers across hybrid environments, benefiting from consistent patching and version support.

In summary, this update enhances the security, stability, and feature set of Azure Database for PostgreSQL – Flexible Server by supporting the latest PostgreSQL minor versions and automating their deployment during scheduled maintenance, thereby reducing operational complexity and improving service reliability for

---

### 2. Azure unmanaged disks will be retired on 31 March 2026 (formerly 30 September 2025)

**Published**: October 06, 2025 20:45:03 UTC
**Link**: [Azure unmanaged disks will be retired on 31 March 2026 (formerly 30 September 2025)](https://azure.microsoft.com/updates?id=azure-unmanaged-disks-will-be-retired-on-30-september-2025)

**Update ID**: azure-unmanaged-disks-will-be-retired-on-30-september-2025
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Azure announced the retirement of unmanaged disks, originally planned for September 30, 2025, now extended to March 31, 2026.

- Key changes or new features  
Unmanaged disks, introduced before 2017, will be fully deprecated as Azure Managed Disks have matured to offer all their capabilities plus enhanced features such as better scalability, improved reliability, simplified management, and integrated snapshot and backup support. Starting September 30, 2022, deprecation efforts began, encouraging migration to managed disks.

- Target audience affected  
Developers and IT professionals managing Azure virtual machine storage, especially those using unmanaged disks in production environments, need to plan and execute migration to managed disks before the retirement date.

- Important notes if any  
The extended retirement date gives organizations additional time to transition workloads. Post-March 31, 2026, unmanaged disks will no longer be supported. Migrating to managed disks is critical to leverage ongoing Azure platform improvements, ensure supportability, and avoid service disruptions. Azure provides tools and documentation to assist with migration planning and execution.

**Details**:

The Azure update announces the retirement of Azure unmanaged disks on March 31, 2026, extending the original deprecation date from September 30, 2025, reflecting Microsoft’s ongoing transition to Azure Managed Disks, which were introduced in 2017 to provide enhanced disk management capabilities, improved scalability, and simplified operations compared to unmanaged disks.

**Background and Purpose:**  
Azure unmanaged disks require users to manage storage accounts that hold the VHD files, leading to complexity in scalability, availability, and management. Since the launch of Azure Managed Disks, Microsoft has continuously enhanced their features, offering better reliability, simplified management, integrated snapshot and backup capabilities, and improved performance. The update’s purpose is to fully transition users to Managed Disks, which eliminate the need to manage storage accounts, provide automatic storage account management, and support advanced features such as zone-redundant storage and encryption.

**Specific Features and Detailed Changes:**  
- **Deprecation Timeline:** Unmanaged disks will no longer be supported after March 31, 2026, giving customers ample time to migrate workloads.  
- **Managed Disk Advantages:** Managed Disks abstract storage account management, allowing Azure to handle scalability and availability automatically. They support features like incremental snapshots, Azure Backup integration, disk encryption with Azure Disk Encryption, and availability zone support.  
- **Migration Tools:** Azure provides tools such as Azure PowerShell cmdlets, Azure CLI commands, and Azure Migrate to facilitate the transition from unmanaged to managed disks without downtime.

**Technical Mechanisms and Implementation Methods:**  
- **Storage Abstraction:** Managed Disks use a resource abstraction layer where the disk is a first-class Azure resource, decoupling it from storage accounts. This enables Azure to distribute disks across storage clusters for high availability and scalability.  
- **Migration Process:** The migration involves detaching the unmanaged disk from the VM, converting it to a managed disk using Azure CLI or PowerShell, and then reattaching it. This can be done online or offline depending on the workload.  
- **Automation:** Scripts and Azure Resource Manager (ARM) templates can automate bulk migration, minimizing manual intervention and errors.

**Use Cases and Application Scenarios:**  
- **Enterprise Workloads:** Enterprises running large-scale VMs benefit from Managed Disks’ scalability and reliability.  
- **Disaster Recovery and Backup:** Managed Disks integrate seamlessly with Azure Backup and Site Recovery, enhancing data protection strategies.  
- **High Availability Applications:** Applications requiring zone-redundant storage and availability zones leverage Managed Disks for improved uptime.  
- **DevOps and Automation:** Managed Disks simplify infrastructure as code (IaC) deployments and CI/CD pipelines by abstracting storage management.

**Important Considerations and Limitations:**  
- **Migration Planning:** Organizations must inventory existing unmanaged disks and plan migration to avoid service disruption.  
- **Cost Implications:** Managed Disks pricing differs from unmanaged disks; users should analyze cost impacts, especially for large-scale deployments.  
- **Feature Parity:** While Managed Disks now support all features of unmanaged disks and more, some legacy scripts or tools may require updates.  
- **Region Availability:** Managed Disk features like zone redundancy depend on Azure region support; verify availability before migration.

**Integration with Related Azure Services:**  
- **Azure Backup:** Managed Disks integrate natively with Azure Backup for snapshot-based backups.  
- **Azure Site Recovery:** Supports disaster recovery scenarios with managed disks.  
- **Azure Monitor:** Provides enhanced monitoring and diagnostics for Managed Disks.  
- **Azure Security Center:** Offers improved security posture management for managed disk resources.  
- **Azure Policy:** Enables governance by enforcing managed disk usage across subscriptions.

In summary, the retirement of Azure unmanaged disks by March 31, 2026, mandates a strategic migration to Azure Managed Disks, which offer superior management, scalability, and integration capabilities, ensuring enhanced operational efficiency, reliability, and security for Azure virtual machine

---


*This report was automatically generated - 2025-10-07 03:01:37 UTC*