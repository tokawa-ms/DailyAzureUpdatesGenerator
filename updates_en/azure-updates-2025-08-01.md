# August 01, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 01, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Generally Available: Live Resize for Premium SSD v2 and Ultra NVMe Disks

**Published**: July 31, 2025 17:15:08 UTC
**Link**: [Generally Available: Live Resize for Premium SSD v2 and Ultra NVMe Disks](https://azure.microsoft.com/updates?id=495106)

**Update ID**: 495106
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Disk Storage, Features

**Summary**:

- What was updated  
Azure has announced the general availability of Live Resize for Premium SSD v2 (Pv2) and Ultra NVMe disks.

- Key changes or new features  
This feature enables dynamic expansion of disk storage capacity without requiring downtime or application disruption. Users can increase disk size on-the-fly, improving flexibility and scalability. This capability helps optimize costs by allowing incremental storage growth aligned with workload demands.

- Target audience affected  
Developers and IT professionals managing Azure virtual machines and storage, particularly those using Premium SSD v2 and Ultra NVMe disks, will benefit from this update. It is especially relevant for scenarios requiring high-performance storage with minimal operational impact.

- Important notes if any  
Live Resize supports only disk expansion, not shrinking. Ensure your applications and operating systems support online disk resizing to fully leverage this feature. Review Azure documentation for any region-specific availability or limitations.

**Details**:

The Azure update announces the general availability of the Live Resize feature for Premium SSD v2 (Pv2) and Ultra NVMe managed disks, enabling dynamic, non-disruptive expansion of disk storage capacity to enhance flexibility and cost optimization in cloud storage management.

**Background and Purpose:**  
Traditionally, resizing Azure managed disks required detaching the disk or stopping the associated virtual machine (VM), causing downtime and operational disruption. With increasing demands for scalable storage in performance-sensitive workloads, there was a need for a seamless method to adjust disk sizes on-the-fly. This update addresses that by allowing IT professionals to expand disk capacity live, improving operational agility and minimizing downtime.

**Specific Features and Detailed Changes:**  
- **Live Resize Capability:** Users can increase the size of Premium SSD v2 and Ultra NVMe disks without detaching them or stopping the VM.  
- **Supported Disk Types:** This feature applies specifically to Premium SSD v2 and Ultra NVMe managed disks, which are designed for high-performance workloads requiring low latency and high IOPS.  
- **Granularity:** Disk sizes can be increased in increments consistent with Azure’s disk sizing tiers, allowing precise scaling according to workload needs.  
- **Cost Optimization:** By resizing disks dynamically, organizations can start with smaller disks and scale up only when necessary, avoiding upfront over-provisioning and reducing costs.

**Technical Mechanisms and Implementation Methods:**  
- The live resize operation leverages Azure’s underlying storage architecture that supports dynamic volume expansion.  
- When a resize request is made via Azure Portal, CLI, or REST API, the platform updates the disk size metadata and allocates additional storage blocks without interrupting the VM’s I/O operations.  
- The guest OS must then recognize the new disk size; this typically involves rescanning the disk and extending the partition and filesystem using OS-level tools (e.g., `diskpart` on Windows or `growpart` and `resize2fs` on Linux).  
- Azure handles the backend storage allocation and ensures data integrity and consistency during the resize process.

**Use Cases and Application Scenarios:**  
- **Database Scaling:** Databases with growing storage needs can be scaled without downtime, ensuring continuous availability.  
- **Big Data and Analytics:** Workloads that require fluctuating storage sizes can dynamically adjust capacity during peak processing times.  
- **Dev/Test Environments:** Developers can start with minimal disk sizes and expand as projects evolve, optimizing resource usage.  
- **Enterprise Applications:** Mission-critical applications requiring high IOPS and low latency benefit from seamless storage scaling without impacting SLAs.

**Important Considerations and Limitations:**  
- **Resize Direction:** Currently, only increasing disk size is supported; shrinking disks live is not supported and requires manual intervention.  
- **Guest OS Support:** The guest operating system must support online disk resizing; otherwise, a reboot or additional manual steps may be necessary.  
- **Performance Impact:** While the resize is live, there may be transient performance impacts; it is advisable to perform resizing during low-usage periods if possible.  
- **Quota and Limits:** Resizing is subject to subscription quotas and maximum disk size limits defined by Azure for Premium SSD v2 and Ultra NVMe disks.  
- **Backup and Recovery:** It is recommended to have backups before resizing operations as a best practice, despite the operation being designed to be safe.

**Integration with Related Azure Services:**  
- **Azure Virtual Machines:** Direct integration allows resizing disks attached to VMs without VM downtime.  
- **Azure CLI and PowerShell:** Support for scripting and automation of live resize operations.  
- **Azure Monitor:** Can be used to track disk performance and capacity trends to proactively trigger resizing.  
- **Azure Backup and Azure Site Recovery:** Compatible with resized disks, ensuring continuity of backup and disaster recovery processes post-resize.

In summary, the Live Resize feature for Premium SSD v2 and Ultra NVMe disks empowers IT professionals to dynamically scale storage capacity without VM downtime

---

### 2. Generally Available: Azure Virtual Network Manager in Azure US Government Cloud

**Published**: July 31, 2025 17:00:19 UTC
**Link**: [Generally Available: Azure Virtual Network Manager in Azure US Government Cloud](https://azure.microsoft.com/updates?id=499387)

**Update ID**: 499387
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure Virtual Network Manager, Regions & Datacenters, Security, Services, Pricing & Offerings, Management, Features

**Summary**:

- What was updated  
Azure Virtual Network Manager (AVNM) is now generally available in the Azure US Government Cloud.

- Key changes or new features  
AVNM provides centralized management for network connectivity, security policies, and routing configurations across multiple subscriptions, regions, and tenants within the US Government Cloud environment. It automates network configuration deployment to ensure consistent policy enforcement and simplifies large-scale network management. This includes unified control over virtual networks, network security groups, and routing tables, enabling streamlined governance and operational efficiency.

- Target audience affected  
Developers, network administrators, and IT professionals managing Azure US Government Cloud environments who require scalable, consistent network configuration and security management across complex, multi-subscription and multi-tenant deployments.

- Important notes if any  
The general availability of AVNM in the US Government Cloud aligns with compliance and security requirements specific to government workloads. Users should evaluate integration with existing network management workflows to leverage automation benefits fully. Further details and deployment guidance are available on the official Azure update page.

**Details**:

The Azure Virtual Network Manager (AVNM) has reached general availability (GA) in the Azure US Government Cloud, delivering centralized and automated management of network connectivity, security, and routing policies across multiple Azure subscriptions, regions, and tenants within the government cloud environment. This update addresses the complexity and operational overhead of managing large-scale, distributed network topologies in regulated government sectors by providing a unified control plane tailored to meet stringent compliance and governance requirements.

**Background and Purpose**  
Managing network configurations in large enterprises, especially within government agencies, often involves multiple subscriptions and isolated environments to meet compliance and security mandates. Prior to AVNM, network administrators had to configure and maintain connectivity, security rules, and routing policies individually per virtual network or subscription, increasing the risk of configuration drift, inconsistent policies, and operational inefficiencies. The introduction of AVNM in Azure US Government Cloud aims to simplify and standardize network management at scale, ensuring consistent policy enforcement and reducing manual errors while adhering to government compliance standards.

**Specific Features and Detailed Changes**  
AVNM provides a centralized management framework that allows administrators to:  
- Define and apply connectivity groups that link virtual networks across subscriptions and regions, enabling seamless and secure communication.  
- Create and enforce security admin rules globally, such as network security group (NSG) policies, firewall rules, and threat protection settings, ensuring uniform security posture.  
- Manage routing policies centrally, including user-defined routes (UDRs) and BGP configurations, to optimize traffic flow and enforce routing compliance.  
- Automate network configuration deployment and updates, minimizing manual intervention and configuration drift.  
- Support multi-tenant scenarios, allowing cross-tenant network management within the Azure US Government Cloud, which is critical for government agencies collaborating across departments or with partners.

**Technical Mechanisms and Implementation Methods**  
AVNM operates as a control plane service that abstracts the underlying network resources and exposes policy-driven management constructs. It leverages Azure Resource Manager (ARM) templates and APIs to declaratively define connectivity groups, security admin rules, and routing policies. These policies are then automatically propagated and enforced across targeted virtual networks, subscriptions, and regions. The service integrates with Azure Policy and Role-Based Access Control (RBAC) to ensure governance and secure delegation of network management tasks. AVNM uses Azure’s native identity and access management to authenticate and authorize policy application, ensuring compliance with government security standards.

**Use Cases and Application Scenarios**  
- **Government agencies with multiple subscriptions:** Centralize network policy management to enforce consistent security and routing across various departments and projects.  
- **Multi-region deployments:** Ensure connectivity and security policies are uniformly applied across geographically dispersed virtual networks.  
- **Cross-tenant collaboration:** Manage network connectivity and security between different government entities or partners securely and efficiently.  
- **Compliance-driven environments:** Automate enforcement of network security policies to meet regulatory requirements such as FedRAMP and DoD SRG.

**Important Considerations and Limitations**  
- AVNM is currently available only within the Azure US Government Cloud, designed to meet specific compliance and security requirements of government customers.  
- While AVNM automates and centralizes network management, administrators must carefully design policies to avoid unintended connectivity or security exposures.  
- Integration with legacy network configurations may require migration or adaptation to AVNM’s policy model.  
- Role assignments and permissions must be meticulously configured to prevent unauthorized policy changes.

**Integration with Related Azure Services**  
AVNM integrates tightly with Azure Resource Manager for policy deployment and management, Azure Policy for compliance auditing, Azure Security Center for threat detection, and Azure Firewall and Network Security Groups for security enforcement. It also complements Azure Sentinel for security monitoring and Azure Monitor for network diagnostics, providing a holistic network governance and security posture management solution within the Azure US Government Cloud.

In summary, the general availability of Azure Virtual Network Manager in the Azure US Government Cloud enables government IT professionals to centrally and consistently manage network connectivity, security, and routing policies across complex, multi-subscription

---

### 3. Public Preview: New tagging features in Azure confidential ledger

**Published**: July 31, 2025 17:00:19 UTC
**Link**: [Public Preview: New tagging features in Azure confidential ledger](https://azure.microsoft.com/updates?id=499382)

**Update ID**: 499382
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Security, Storage, Azure confidential ledger, Features

**Summary**:

- What was updated  
Azure Confidential Ledger now supports tagging features in public preview.

- Key changes or new features  
Users can assign up to five tags per transaction within the confidential ledger. These tags act as secondary keys, enhancing data organization and enabling more efficient retrieval and categorization of ledger entries. This feature improves the ability to filter and query transactions based on custom metadata, facilitating better management of ledger data.

- Target audience affected  
Developers and IT professionals working with Azure Confidential Ledger, especially those implementing secure, tamper-proof transaction logging and requiring advanced data organization and querying capabilities.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments first. Tagging improves data handling but does not alter the underlying security or immutability guarantees of the confidential ledger. Developers should update their applications to leverage tagging via the ledger’s API.

**Details**:

The recent public preview update for Azure Confidential Ledger introduces enhanced tagging capabilities designed to improve data organization, retrieval, and management within ledger collections. Azure Confidential Ledger is a blockchain-based service that provides a tamper-proof, cryptographically verifiable ledger for storing sensitive data with confidentiality guarantees using trusted execution environments (TEEs). This update addresses the need for more granular and flexible data categorization, which is critical for enterprises managing complex transaction records in confidential environments.

**Background and Purpose**  
Azure Confidential Ledger ensures data integrity and confidentiality by leveraging hardware-based trusted execution environments, but until now, its querying and data management capabilities were limited to basic transaction retrieval. As organizations increasingly adopt ledger technology for audit trails, compliance, and secure record-keeping, the ability to organize and filter transactions efficiently becomes essential. The introduction of tagging features aims to provide secondary keys—metadata labels—that can be attached to transactions to facilitate easier indexing, searching, and categorization without compromising the ledger’s security and immutability.

**Specific Features and Detailed Changes**  
- **Tagging per Transaction:** Users can now assign up to five tags per transaction. Each tag acts as a secondary key or metadata label associated with the transaction data.  
- **Enhanced Querying:** Tags enable more efficient filtering and retrieval of transactions within a ledger collection, allowing users to query based on tag values rather than scanning the entire ledger.  
- **Immutable Tagging:** Tags, once assigned to a transaction, are stored immutably alongside the transaction record, preserving the integrity and auditability of metadata.  
- **Backward Compatibility:** Existing ledger operations remain unchanged, and tagging is an additive feature that does not affect the core transaction processing or ledger consensus mechanisms.

**Technical Mechanisms and Implementation Methods**  
Tags are implemented as metadata fields attached to each transaction payload before submission to the ledger. When a transaction is committed, the tags are cryptographically bound to the transaction record within the trusted execution environment, ensuring they cannot be altered post-commit. The ledger’s indexing engine incorporates these tags to support efficient secondary key lookups. The API surface has been extended to accept tag parameters during transaction submission and to filter query results based on tag values. This design maintains the ledger’s cryptographic proofs and consensus guarantees while enhancing usability.

**Use Cases and Application Scenarios**  
- **Audit and Compliance:** Organizations can tag transactions by audit categories, compliance requirements, or regulatory domains, simplifying retrieval during audits.  
- **Financial Services:** Tagging transactions by account, transaction type, or risk level enables faster forensic analysis and reporting.  
- **Supply Chain:** Tags can represent shipment status, origin, or product categories, aiding traceability and verification.  
- **Healthcare:** Patient records or consent transactions can be tagged by department, treatment type, or urgency for efficient access.  
- **Multi-Tenant Environments:** Tags help segregate and manage transactions belonging to different tenants or business units within a shared ledger.

**Important Considerations and Limitations**  
- **Tag Limit:** A maximum of five tags per transaction limits granularity; users must plan tag usage strategically.  
- **Tag Size and Format:** Tags must conform to size and character restrictions defined by the API to ensure efficient indexing.  
- **Security and Privacy:** While tags aid retrieval, they should not contain sensitive information unless encrypted, as metadata may be visible in query results.  
- **Preview Status:** As a public preview feature, tagging may undergo changes and should not be used in production-critical environments without validation.  
- **Performance Impact:** Although indexing tags improves query efficiency, excessive or complex tag usage could impact ledger performance and storage.

**Integration with Related Azure Services**  
Azure Confidential Ledger’s tagging feature complements other Azure services by enabling better data governance and integration:  
- **Azure Monitor and Log Analytics:** Tags can be used to filter and correlate ledger transactions with monitoring logs for operational insights.  
- **Azure Policy and Governance:** Tags facilitate policy enforcement and compliance tracking across ledger transactions.

---

### 4. Generally Available: Log or block shared access signature (SAS) tokens for Azure Storage based on expiration policy

**Published**: July 31, 2025 17:00:19 UTC
**Link**: [Generally Available: Log or block shared access signature (SAS) tokens for Azure Storage based on expiration policy](https://azure.microsoft.com/updates?id=498759)

**Update ID**: 498759
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Storage Accounts, Security

**Summary**:

- What was updated  
Azure Storage now generally supports logging or blocking Shared Access Signature (SAS) tokens based on their expiration policy.

- Key changes or new features  
Administrators can enforce an upper limit on SAS token validity intervals via SAS expiration policies. Beyond setting validity duration, they can now configure Azure Storage to either log usage of SAS tokens that exceed the defined expiration policy or block such tokens entirely. This enhances security by preventing or monitoring the use of overly long-lived SAS tokens that could pose risks.

- Target audience affected  
Developers and IT professionals managing Azure Storage access controls, especially those implementing fine-grained, time-bound access via SAS tokens, will benefit from improved governance and security capabilities.

- Important notes if any  
This feature is generally available, meaning it is production-ready and supported for all Azure Storage accounts. Organizations should review and update their SAS expiration policies to leverage logging or blocking to better align with their security compliance requirements. Implementing these controls helps mitigate risks associated with long-lived SAS tokens.  

For more details, visit: https://azure.microsoft.com/updates?id=498759

**Details**:

The recent Azure update titled "Generally Available: Log or block shared access signature (SAS) tokens for Azure Storage based on expiration policy" introduces enhanced governance capabilities over SAS tokens by enabling administrators to enforce and monitor SAS token validity periods through expiration policies.

**Background and Purpose**  
Shared Access Signatures (SAS) are widely used in Azure Storage to delegate limited access to storage resources without sharing account keys. However, controlling the lifespan of SAS tokens has been a challenge, often leading to security risks if tokens remain valid longer than intended. Prior to this update, administrators could define an upper limit on SAS token validity via expiration policies but lacked mechanisms to enforce or audit compliance effectively. This update aims to strengthen security posture by allowing organizations to log or outright block SAS tokens that exceed defined expiration policies, thereby reducing the risk of unauthorized or prolonged access.

**Specific Features and Detailed Changes**  
- **Expiration Policy Enforcement:** Administrators can now configure SAS expiration policies that not only set maximum validity intervals but also enforce them by blocking SAS tokens that exceed these limits.  
- **Logging Capabilities:** SAS tokens that violate expiration policies can be logged for audit and compliance purposes, providing visibility into potential security issues.  
- **Granular Control:** These policies can be applied at the storage account level, enabling consistent governance across all SAS tokens issued within that scope.  
- **General Availability (GA):** The feature has moved from preview to GA, indicating production readiness and Microsoft’s commitment to support and maintain it.

**Technical Mechanisms and Implementation Methods**  
The expiration policy is implemented as a configuration on the Azure Storage account. When a SAS token is presented for authentication, Azure Storage evaluates the token’s expiry time against the configured expiration policy:  
- If the token’s validity period exceeds the maximum allowed interval, the system either logs the event or blocks the request based on the policy settings.  
- Logging integrates with Azure Monitor and Azure Storage analytics, allowing administrators to track non-compliant SAS token usage.  
- Enforcement occurs at the service level, ensuring that invalid SAS tokens are rejected before any storage operation is performed.

Administrators configure these policies via Azure CLI, PowerShell, or Azure Portal, specifying the maximum allowed SAS token lifetime and the desired action (log or block).

**Use Cases and Application Scenarios**  
- **Security Compliance:** Organizations with strict security requirements can enforce SAS token lifetimes to comply with internal policies or regulatory mandates.  
- **Risk Mitigation:** Preventing long-lived SAS tokens reduces the attack surface in case tokens are leaked or compromised.  
- **Operational Auditing:** Logging non-compliant SAS token usage helps security teams detect and investigate potential misuse or policy violations.  
- **Automated Governance:** Enables automated enforcement without manual intervention, improving operational efficiency.

**Important Considerations and Limitations**  
- Existing SAS tokens issued before policy enforcement may continue to function until expiration unless explicitly blocked.  
- Careful planning is needed to avoid service disruptions, especially if applications rely on long-lived SAS tokens.  
- The policy applies at the storage account level and does not differentiate between individual containers or blobs; thus, all SAS tokens issued by the account are subject to the same rules.  
- Integration with logging requires proper configuration of Azure Monitor or Storage analytics to capture events effectively.

**Integration with Related Azure Services**  
- **Azure Monitor:** For capturing and analyzing logs related to SAS token violations.  
- **Azure Storage Analytics:** Provides detailed metrics and logs for storage operations, including SAS token usage.  
- **Azure Active Directory (AAD):** While SAS tokens are independent of AAD, organizations can combine SAS expiration policies with AAD-based access controls for layered security.  
- **Azure Policy:** Can be used alongside to enforce organizational standards on storage account configurations.

In summary, this GA update empowers IT professionals to enforce strict SAS token expiration policies on Azure Storage accounts by enabling blocking or logging of tokens that exceed configured validity intervals. This enhances security governance, reduces

---


*This report was automatically generated - 2025-08-01 03:02:11 UTC*