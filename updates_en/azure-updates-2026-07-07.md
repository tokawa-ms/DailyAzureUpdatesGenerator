# July 07, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 07, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Microsoft Entra ID-based access for Azure Blob Storage SFTP

**Published**: July 06, 2026 15:54:08 UTC
**Link**: [Generally Available: Microsoft Entra ID-based access for Azure Blob Storage SFTP](https://azure.microsoft.com/updates?id=567085)

**Update ID**: 567085
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage, Features

**Summary**:

- What was updated  
Microsoft Entra ID-based access for Azure Blob Storage SFTP is now generally available in all regions.

- Key changes or new features  
Azure Blob Storage now supports authentication via Microsoft Entra ID (formerly Azure AD) for SFTP access. This includes support for guest users through Entra External Identities. Users can securely connect to Blob Storage over SFTP using Entra ID identities, eliminating the need to provision and manage local storage account credentials or SSH keys.

- Target audience affected  
Developers and IT professionals managing secure file transfer workflows to Azure Blob Storage, especially those integrating with external partners or requiring centralized identity management.

- Important notes if any  
This update simplifies identity and access management for SFTP by leveraging Entra ID, enabling single sign-on and improved security. It also supports external/guest users, facilitating secure collaboration with third parties. No additional credential management is required—access is governed by Entra ID role assignments and policies. Review your access policies and update documentation to leverage Entra ID-based authentication for SFTP scenarios.  

For more details, see the official update: https://azure.microsoft.com/updates?id=567085

**Details**:

**Background and Purpose of the Update**  
This update introduces the general availability of Microsoft Entra ID-based access for Azure Blob Storage SFTP. Previously, access to Azure Blob Storage via SFTP required local storage account credentials or other authentication mechanisms. The purpose of this update is to enhance security and streamline identity management by enabling direct use of Microsoft Entra ID (formerly Azure Active Directory) identities—including guest users managed via Entra External Identities—for SFTP access to Blob Storage.

**Specific Features and Detailed Changes**  
- **Entra ID Authentication for SFTP**: Users can now authenticate to Azure Blob Storage SFTP endpoints using their Entra ID credentials, eliminating the need for local user accounts or passwords.
- **Guest User Support**: Entra External Identities allows guest users, such as partners or contractors, to securely connect via SFTP using their own identity providers.
- **General Availability**: This feature is now fully supported in all Azure regions, making it accessible for global deployments.

**Technical Mechanisms and Implementation Methods**  
- **Identity Management**: Access control is managed through Microsoft Entra ID, leveraging its robust identity and access management capabilities.
- **SFTP Integration**: Azure Blob Storage exposes SFTP endpoints, and now these endpoints can be configured to accept Entra ID-based authentication.
- **External Identities**: Guest users are provisioned and managed via Entra External Identities, allowing organizations to extend SFTP access to external collaborators without creating local accounts.
- **Security**: Authentication is performed using Entra ID, which supports modern security features such as conditional access policies, multi-factor authentication, and centralized auditing.

**Use Cases and Application Scenarios**  
- **Enterprise Data Exchange**: Organizations can securely share files with internal users and external partners via SFTP, leveraging centralized identity management.
- **Automated Data Ingestion**: Applications and services that require SFTP for automated uploads to Blob Storage can now use Entra ID identities, simplifying credential management.
- **Partner Collaboration**: External collaborators can be granted SFTP access to specific Blob Storage containers using their own identity providers, reducing administrative overhead and improving security.

**Important Considerations and Limitations**  
- **Identity Requirements**: Only users with Entra ID identities (including guest users via Entra External Identities) can authenticate; legacy authentication methods may not be supported for SFTP endpoints configured for Entra ID.
- **Regional Availability**: The feature is generally available in all Azure regions, but organizations should verify regional feature support for their specific deployment.
- **Security Policies**: Organizations must ensure their Entra ID policies are properly configured to enforce secure access, including conditional access and MFA as needed.
- **Integration Complexity**: Existing SFTP workflows may require updates to leverage Entra ID authentication, including changes to client configuration and access provisioning.

**Integration with Related Azure Services**  
- **Microsoft Entra ID**: Centralized identity and access management for SFTP access.
- **Azure Blob Storage**: SFTP endpoints now support Entra ID-based authentication.
- **Entra External Identities**: Enables secure access for guest users and external partners.
- **Azure Security and Compliance Tools**: Enhanced auditing and monitoring through Entra ID integration.

**Summary Sentence**  
Microsoft Entra ID-based access for Azure Blob Storage SFTP is now generally available, enabling secure, centralized identity management—including guest users via Entra External Identities—for SFTP connections to Blob Storage across all Azure regions.

---

### 2. Generally Available: Support 5x churn in Azure Site Recovery

**Published**: July 06, 2026 15:00:33 UTC
**Link**: [Generally Available: Support 5x churn in Azure Site Recovery](https://azure.microsoft.com/updates?id=566966)

**Update ID**: 566966
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery, Features, Compliance, Management

**Summary**:

- What was updated  
Azure Site Recovery now supports up to 5x churn, allowing replication of data changes at rates up to 500 MB/s per VM.

- Key changes or new features  
The maximum supported churn rate per virtual machine has increased from 1x to 5x (500 MB/s). This enables support for high IOPS workloads and large, data-intensive applications, improving disaster recovery capabilities for demanding enterprise environments.

- Target audience affected  
Developers and IT professionals responsible for business continuity, disaster recovery planning, and management of high-throughput or mission-critical workloads in Azure.

- Important notes if any  
This enhancement allows organizations to replicate and protect VMs with high data change rates, such as those running databases, analytics, or other intensive applications. Review your current Site Recovery configurations to take advantage of the increased churn limits, and ensure your network and storage infrastructure can support higher replication throughput.

[Read more](https://azure.microsoft.com/updates?id=566966)

**Details**:

**Azure Update Report: Generally Available – Support 5x Churn in Azure Site Recovery**

**Background and Purpose of the Update**  
Azure Site Recovery (ASR) is a disaster recovery solution that enables seamless replication, failover, and recovery of workloads hosted on-premises or in Azure. Traditionally, ASR supported a certain level of data churn (rate of data change) per VM, which limited its applicability for high IOPS workloads. The purpose of this update is to significantly increase the supported churn rate, thereby expanding ASR’s suitability for mission-critical applications with heavy write operations.

**Specific Features and Detailed Changes**  
With this update, ASR now supports up to 5x churn, specifically quantified as 500 MB/s per VM. This enhancement allows customers to replicate and protect VMs with much higher data change rates than previously possible. The increased churn threshold means that workloads generating substantial amounts of data per second—such as large databases, transaction-heavy applications, and high-performance computing workloads—can now be reliably protected using ASR.

**Technical Mechanisms and Implementation Methods**  
The update likely involves improvements to ASR’s underlying replication engine, network throughput optimization, and storage handling mechanisms. By supporting 500 MB/s per VM, ASR must efficiently capture, compress, and transfer changed data blocks to the target recovery site without bottlenecks. This may include enhancements in parallel data processing, optimized delta tracking, and improved bandwidth utilization. The replication process remains asynchronous, ensuring minimal impact on production workloads while maintaining data consistency for recovery.

**Use Cases and Application Scenarios**  
- **High IOPS Databases:** Enterprises running SQL Server, Oracle, or other high-throughput databases can now use ASR for disaster recovery without concern for replication lag or throttling.
- **Transactional Applications:** Applications with frequent and large-scale data writes, such as financial trading platforms or e-commerce systems, benefit from robust failover capabilities.
- **Large-scale File Servers and Storage Solutions:** Organizations managing large file shares or storage clusters can ensure rapid recovery and minimal data loss in disaster scenarios.
- **Mission-critical Workloads:** Any workload requiring stringent RPO (Recovery Point Objective) and RTO (Recovery Time Objective) can leverage ASR’s enhanced churn support for improved resilience.

**Important Considerations and Limitations**  
- **Bandwidth Requirements:** Achieving 500 MB/s per VM replication requires sufficient network bandwidth between the source and target locations. IT professionals must ensure their infrastructure can support these rates to avoid bottlenecks.
- **Storage Performance:** The target recovery site must be provisioned with adequate storage performance to handle high-volume data ingestion.
- **Cost Implications:** Increased churn may result in higher consumption of network and storage resources, potentially impacting operational costs.
- **Compatibility:** The update applies to supported VM types and configurations; engineers should verify compatibility with their specific workloads and environments.

**Integration with Related Azure Services**  
ASR integrates with Azure Backup, Azure Storage, and Azure Networking to provide comprehensive disaster recovery solutions. The increased churn support enhances synergy with high-performance storage tiers (such as Premium SSDs) and advanced networking configurations (ExpressRoute, VPN Gateway) to ensure end-to-end reliability and performance. ASR can also be orchestrated with Azure Automation and Azure Monitor for customized recovery workflows and monitoring.

**Summary Sentence**  
Azure Site Recovery now supports up to 5x churn (500 MB/s per VM), enabling robust disaster recovery for high IOPS workloads and mission-critical applications, with enhanced replication performance, broader applicability, and integration with Azure’s ecosystem.

---


*This report was automatically generated - 2026-07-07 03:01:51 UTC*