# October 24, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 24, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup

**Published**: October 23, 2026 19:21:07 UTC
**Link**: [Generally Available: Item Level Recovery for Azure VMs with Premium SSDv2 and Ultra Disks in Azure Backup](https://azure.microsoft.com/updates?id=577963)

**Update ID**: 577963
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Storage, Azure Backup, Feature

**Summary**:

- What was updated  
Azure Backup now offers Item-Level Recovery (ILR) for Azure virtual machines (VMs) using Premium SSD v2 and Ultra disks, supporting both 512-byte and 4KB logical sector sizes.

- Key changes or new features  
Developers and IT professionals can now recover individual files and folders from backups of Azure VMs running on Premium SSD v2 and Ultra disks, rather than restoring the entire VM. This feature streamlines granular recovery operations and reduces downtime. ILR is available for both disk types and sector sizes, expanding backup flexibility and recovery options.

- Target audience affected  
This update is relevant for IT administrators, DevOps engineers, and developers managing Azure VMs with Premium SSD v2 or Ultra disks, especially those responsible for backup and disaster recovery strategies.

- Important notes  
ILR enhances recovery efficiency by allowing file-level restores, which is particularly useful for quick remediation of accidental deletions or corruption. Ensure your Azure Backup vault and VM configurations are compatible with Premium SSD v2 or Ultra disks to leverage this feature. Review Azure Backup documentation for supported scenarios and prerequisites.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=577963

**Details**:

**Background and Purpose of the Update**  
Azure Backup has extended its Item-Level Recovery (ILR) capabilities to support Azure virtual machines (VMs) that utilize Premium SSD v2 and Ultra disks, including disks formatted with both 512 byte and 4KB logical sector sizes. Previously, ILR was limited to certain disk types, restricting granular recovery options for VMs using high-performance storage. This update addresses the need for fine-grained data recovery in environments where Premium SSD v2 and Ultra disks are deployed, enhancing backup flexibility and minimizing downtime during file or folder restoration.

**Specific Features and Detailed Changes**  
The update introduces ILR for VMs with Premium SSD v2 and Ultra disks, regardless of whether the logical sector size is 512 bytes or 4KB. ILR enables users to browse and restore individual files and folders from VM backups, rather than requiring a full VM or disk restore. This granular recovery is now available for the latest disk types, ensuring that organizations leveraging advanced storage options can benefit from efficient backup and recovery operations.

**Technical Mechanisms and Implementation Methods**  
Azure Backup’s ILR works by mounting a recovery point as a temporary disk on a separate Azure VM. The process involves the following steps:
1. Initiate an ILR operation from the Azure portal for a VM backup protected by Azure Backup.
2. Azure Backup creates a temporary VM and attaches the backup disk to it.
3. The user accesses the temporary VM via Remote Desktop Protocol (RDP) or Azure portal, browses the disk, and copies required files or folders.
4. After recovery, the temporary VM and attached disk are automatically cleaned up.

With this update, the ILR workflow is extended to Premium SSD v2 and Ultra disks, supporting both 512 byte and 4KB sector sizes. This ensures compatibility with high-performance workloads and modern disk configurations.

**Use Cases and Application Scenarios**  
- **Granular Recovery:** Restore specific files or folders lost due to accidental deletion, corruption, or ransomware without restoring the entire VM.
- **Compliance and Auditing:** Retrieve individual files for legal or regulatory requirements from backups of VMs using Premium SSD v2 or Ultra disks.
- **Operational Efficiency:** Quickly recover critical data for applications running on high-performance disks, reducing recovery time objectives (RTO).

**Important Considerations and Limitations**  
- ILR is available only for VMs protected by Azure Backup and using Premium SSD v2 or Ultra disks with supported sector sizes.
- The process involves creating a temporary VM, which may incur additional Azure resource costs during the recovery operation.
- ILR is intended for file and folder recovery; it does not support application-level recovery or restore of system state.
- Ensure proper permissions and network access to the temporary VM for successful file retrieval.

**Integration with Related Azure Services**  
ILR is tightly integrated with Azure Backup, leveraging its backup vaults and recovery points. The temporary VM used for ILR can be managed through the Azure portal, and the recovered files can be stored in Azure Storage or other Azure services as needed. This update aligns with Azure’s broader backup and disaster recovery ecosystem, supporting advanced storage types and facilitating seamless integration with VM management and storage solutions.

**Summary Sentence**  
Azure Backup now offers Item-Level Recovery for Azure VMs using Premium SSD v2 and Ultra disks, enabling granular file and folder restoration with support for both 512 byte and 4KB sector sizes, thereby enhancing backup flexibility and operational efficiency for high-performance workloads.

---


*This report was automatically generated - 2026-10-24 03:01:19 UTC*