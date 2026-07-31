# July 31, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 31, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Generally Available: Azure Database for PostgreSQL flexible server in India South Central 

**Published**: July 30, 2026 19:14:44 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL flexible server in India South Central ](https://azure.microsoft.com/updates?id=568334)

**Update ID**: 568334
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL flexible server is now generally available in the India South Central Azure region.

- Key changes or new features  
This update enables deployment and management of PostgreSQL flexible servers in the India South Central region. Developers and IT teams can leverage features such as high availability, automated backups, scaling, and enhanced security within this new geographic location.

- Target audience affected  
Developers, database administrators, and IT professionals who require PostgreSQL flexible server hosting in India South Central, or need to meet regional data residency and compliance requirements.

- Important notes  
This expansion supports improved latency and performance for applications serving users in or near India South Central. It also helps organizations comply with local data governance policies. Existing Azure Database for PostgreSQL flexible server capabilities remain unchanged; only the regional availability is new. For more details, visit the official Azure Update [link](https://azure.microsoft.com/updates?id=568334).

**Details**:

**Comprehensive Technical Explanation: Azure Database for PostgreSQL Flexible Server – India South Central Region General Availability**

**Background and Purpose of the Update:**  
The Azure Database for PostgreSQL flexible server service is now generally available in the India South Central Azure region. This update expands the geographic footprint of Azure’s managed PostgreSQL offering, enabling customers to deploy flexible server instances closer to their users and data sources in South Central India. The primary purpose is to support regional compliance, reduce latency, and improve performance for workloads requiring data residency within India.

**Specific Features and Detailed Changes:**  
With this update, IT professionals can provision Azure Database for PostgreSQL flexible server resources in the India South Central region. The flexible server deployment model offers enhanced control over database configuration, maintenance windows, high availability options, and scaling. Key features include:

- Customizable server parameters for performance tuning.
- Choice of single zone or zone redundant high availability.
- Automated backups and point-in-time restore capabilities.
- Fine-grained maintenance scheduling.
- Support for scaling compute and storage independently.

This update does not introduce new features to the flexible server itself but makes all existing capabilities available in the India South Central region.

**Technical Mechanisms and Implementation Methods:**  
Deployment is managed via the Azure Portal, CLI, PowerShell, or ARM templates. Engineers select the India South Central region when creating a flexible server instance. The service leverages Azure’s regional infrastructure to provision compute, storage, and networking resources, ensuring data is stored and processed within the specified region. High availability is achieved through zone redundant architecture, where supported, and automated failover mechanisms.

**Use Cases and Application Scenarios:**  
- **Regional Data Residency:** Organizations with regulatory requirements to keep data within India can now use Azure Database for PostgreSQL flexible server in South Central India.
- **Low Latency Applications:** Deploying in India South Central reduces latency for users and applications located in or near this region.
- **Disaster Recovery:** Multi-region architectures can include India South Central for backup, failover, or replication scenarios.
- **Local Development and Testing:** Teams based in South Central India can provision resources locally for development, testing, and production workloads.

**Important Considerations and Limitations:**  
- **Service Availability:** All flexible server features are available, but engineers should verify specific SKUs, storage options, and high availability configurations supported in India South Central.
- **Compliance:** While regional deployment supports data residency, customers must ensure compliance with local regulations and Azure’s shared responsibility model.
- **Networking:** Review regional networking capabilities, including VNet integration, private endpoints, and firewall rules.
- **Quotas and Capacity:** Check for regional quotas and capacity limits, which may differ from other Azure regions.

**Integration with Related Azure Services:**  
Azure Database for PostgreSQL flexible server integrates with other Azure services such as:

- **Azure Virtual Network (VNet):** For secure, private connectivity.
- **Azure Backup:** For automated backup and restore.
- **Azure Monitor:** For performance and health monitoring.
- **Azure Key Vault:** For managing secrets and encryption keys.
- **Azure App Service and Azure Functions:** For building web and serverless applications with PostgreSQL backends.

**Summary Sentence:**  
Azure Database for PostgreSQL flexible server is now generally available in the India South Central region, enabling IT professionals to deploy managed PostgreSQL instances with flexible configuration and high availability options, supporting regional compliance and low-latency application scenarios.

---

### 2. Generally Available: Azure Automation supports PowerShell 7.6 runbooks and Runtime environment

**Published**: July 30, 2026 19:10:35 UTC
**Link**: [Generally Available: Azure Automation supports PowerShell 7.6 runbooks and Runtime environment](https://azure.microsoft.com/updates?id=568102)

**Update ID**: 568102
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Automation, Feature

**Summary**:

- What was updated  
Azure Automation now offers General Availability (GA) support for PowerShell 7.6 runbooks and the PowerShell 7.6 runtime environment.

- Key changes or new features  
1. PowerShell 7.6 runbooks are fully supported, allowing users to leverage the latest PowerShell features and security updates.  
2. Customers can upgrade existing scripts from older, unsupported PowerShell versions to PowerShell 7.6, ensuring compatibility and improved performance.  
3. Enhanced support for Azure CLI commands within PowerShell 7.6 runbooks, enabling more robust automation scenarios.

- Target audience affected  
Developers and IT professionals using Azure Automation for script-based automation, especially those maintaining or developing PowerShell runbooks.

- Important notes  
1. Upgrading to PowerShell 7.6 is recommended for improved security, support, and access to new language features.  
2. Existing runbooks using older PowerShell versions should be reviewed and tested for compatibility before migration.  
3. The new runtime environment supports Azure CLI integration, which may require updates to existing scripts if Azure CLI commands are used.  
4. This update ensures continued support and compliance for automation workloads in Azure.

For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=568102

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Automation supports PowerShell 7.6 runbooks and Runtime environment  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=568102)

---

**Background and Purpose of the Update**

Azure Automation has announced the General Availability (GA) of PowerShell 7.6 support for runbooks and its associated runtime environment. The primary purpose of this update is to allow customers to upgrade their automation scripts from outdated PowerShell versions to a supported and modern runtime. This ensures compatibility, security, and access to the latest PowerShell features, addressing the need for organizations to maintain up-to-date automation workflows in their cloud environments.

---

**Specific Features and Detailed Changes**

- **PowerShell 7.6 Runbook Support:** Runbooks in Azure Automation can now be authored and executed using PowerShell 7.6, which is a current, in-support version.
- **Runtime Environment GA:** The PowerShell 7.6 runtime environment is now generally available, meaning it is fully supported for production workloads.
- **Upgrade Path:** Customers can seamlessly transition existing scripts from older PowerShell versions to PowerShell 7.6, minimizing disruption and ensuring continued support.
- **Azure CLI Command Support:** The update also includes support for Azure CLI commands within PowerShell 7.6 runbooks, enhancing script versatility and integration with Azure resources.

---

**Technical Mechanisms and Implementation Methods**

- **Runbook Authoring:** IT professionals can create new runbooks or update existing ones to utilize PowerShell 7.6 syntax and features within the Azure Automation service.
- **Runtime Selection:** When configuring a runbook, users can select PowerShell 7.6 as the runtime environment, ensuring scripts execute with the latest supported interpreter.
- **Execution Environment:** The Azure Automation infrastructure provisions and manages the PowerShell 7.6 runtime, providing a consistent and secure execution context for automation tasks.
- **Azure CLI Integration:** Scripts can invoke Azure CLI commands directly within PowerShell 7.6 runbooks, enabling hybrid automation scenarios that leverage both PowerShell and Azure CLI capabilities.

---

**Use Cases and Application Scenarios**

- **Modernizing Automation Workflows:** Organizations can update legacy runbooks to PowerShell 7.6, taking advantage of new language features, improved performance, and enhanced security.
- **Hybrid Scripting:** Combining PowerShell and Azure CLI commands in a single runbook allows for more flexible automation, especially for tasks where Azure CLI offers unique functionality.
- **Production Automation:** With GA support, IT teams can confidently deploy PowerShell 7.6 runbooks in mission-critical environments, knowing they are fully supported by Azure.
- **Compliance and Security:** Upgrading to a supported runtime helps meet compliance requirements and reduces risks associated with unsupported scripting environments.

---

**Important Considerations and Limitations**

- **Script Compatibility:** Existing scripts may require modification to run under PowerShell 7.6, as there may be breaking changes or deprecated features compared to older versions.
- **Runtime Selection:** Careful selection of the runtime environment is necessary when migrating runbooks to ensure compatibility and proper execution.
- **Azure CLI Usage:** While Azure CLI commands are supported, users should validate command syntax and output handling within PowerShell 7.6 runbooks.

---

**Integration with Related Azure Services**

- **Azure Automation:** The update is native to Azure Automation, enhancing its capabilities for orchestrating cloud and hybrid workloads.
- **Azure Resource Management:** Runbooks can interact with Azure resources using both PowerShell and Azure CLI, streamlining resource provisioning, management, and monitoring.
- **Security and Compliance:** Integration with Azure’s security and monitoring services ensures that runbook execution adheres to organizational policies.

---

**Summary Sentence**

Azure Automation now offers General Availability support for PowerShell 7.6 runbooks and runtime environment, enabling IT professionals to upgrade scripts to a modern, supported platform and leverage Azure CLI commands within

---

### 3. Announcing: Reservation exchanges for Azure services supported by savings plans will no longer be available starting February 1, 2027  

**Published**: July 30, 2026 19:03:21 UTC
**Link**: [Announcing: Reservation exchanges for Azure services supported by savings plans will no longer be available starting February 1, 2027  ](https://azure.microsoft.com/updates?id=568514)

**Update ID**: 568514
**Data source**: Azure Updates API

**Categories**: Announcement

**Summary**:

- What was updated  
Microsoft announced that reservation exchanges for Azure services supported by savings plans will be discontinued starting February 1, 2027.

- Key changes or new features  
After February 1, 2027, customers will no longer be able to exchange reservations for services covered by savings plans. Currently, this applies to Azure Virtual Machine reservations. Reservation exchanges allow users to modify existing reservations (e.g., change VM sizes or regions) without cancelling and repurchasing.

- Target audience affected  
This update impacts developers and IT professionals who manage Azure reservations for compute resources, especially those using Azure Virtual Machines and leveraging savings plans.

- Important notes  
Existing reservation exchanges will continue to be available until February 1, 2027. After this date, reservation exchanges for services supported by savings plans will be disabled, and customers will need to plan purchases and modifications accordingly. Reservations for services not supported by savings plans are not affected by this change. It’s recommended to review reservation strategies and savings plans to optimize costs and flexibility before the deadline.

For more details, visit the official Azure Update announcement: https://azure.microsoft.com/updates?id=568514

**Details**:

**Azure Update Report: Reservation Exchanges for Azure Services Supported by Savings Plans Will No Longer Be Available Starting February 1, 2027**

**Background and Purpose of the Update**  
Azure offers two primary cost optimization options for compute services: Reservations and Savings Plans. Reservations allow customers to commit to a specific resource type, region, and term, often with the flexibility to exchange reservations if their requirements change. Savings Plans provide broader cost savings across eligible services without the need for resource-specific commitments. This update announces that, starting February 1, 2027, Azure will discontinue the ability to exchange reservations for services that are supported by savings plans. The purpose is to streamline cost management options and encourage the adoption of savings plans, which offer greater flexibility.

**Specific Features and Detailed Changes**  
Currently, Azure customers can exchange reservations for certain compute services (such as Azure Virtual Machines) covered by savings plans. Reservation exchanges allow customers to modify their reserved resource type, size, or region during the reservation term, adapting to changing workloads. This update specifies that after February 1, 2027, reservation exchanges will no longer be available for these services. Reservations for Azure Virtual Machines and other compute services supported by savings plans will become non-exchangeable after this date. Customers will retain the ability to use savings plans, which do not require exchanges due to their flexible nature.

**Technical Mechanisms and Implementation Methods**  
Reservation exchanges are managed through the Azure portal, APIs, or PowerShell, enabling customers to swap existing reservations for new ones with different configurations. After the cutoff date, these exchange mechanisms will be disabled for compute services covered by savings plans. Technically, reservation objects for these services will become immutable during their term, and the exchange APIs will return errors or be unavailable for these resource types. Customers will need to plan their reservation purchases carefully, as post-purchase modifications will not be possible.

**Use Cases and Application Scenarios**  
Common use cases for reservation exchanges include scaling up or down virtual machine sizes, changing regions due to workload migration, or adapting to new business requirements. With the removal of exchanges, customers must rely on savings plans for flexibility, as savings plans automatically apply discounts to eligible resources without the need for manual exchanges. For static workloads with predictable resource requirements, reservations may still be appropriate, but customers must ensure their selections are accurate at purchase time.

**Important Considerations and Limitations**  
- After February 1, 2027, reservation exchanges for compute services supported by savings plans (e.g., Azure Virtual Machines) will not be possible.
- Customers must carefully evaluate their reservation needs before purchase, as changes will not be allowed post-purchase.
- Savings plans remain available and provide flexibility for dynamic workloads.
- Existing reservations purchased before the cutoff date will be subject to the new policy if their exchange is attempted after February 1, 2027.

**Integration with Related Azure Services**  
Reservations and savings plans are integrated with Azure Cost Management and Billing, allowing customers to track usage and optimize spend. The update affects only the exchange functionality for reservations; all other management, reporting, and billing features remain unchanged. Customers can continue to use savings plans alongside reservations for services not covered by savings plans.

**Summary Sentence**  
Starting February 1, 2027, Azure will discontinue reservation exchanges for compute services supported by savings plans, requiring customers to rely on savings plans for flexibility and to carefully plan reservation purchases, as post-purchase modifications will no longer be possible.

---

### 4. Public Preview: Symmetric keys on Azure Key Vault Premium

**Published**: July 30, 2026 18:57:18 UTC
**Link**: [Public Preview: Symmetric keys on Azure Key Vault Premium](https://azure.microsoft.com/updates?id=566746)

**Update ID**: 566746
**Data source**: Azure Updates API

**Categories**: In preview, Security, Key Vault, Features

**Summary**:

- What was updated  
Azure Key Vault Premium now supports symmetric keys in public preview.

- Key changes or new features  
Symmetric encryption capabilities are available using the oct-HSM key type and Advanced Encryption Standard (AES). This allows customers to generate, store, and use symmetric keys securely within Azure Key Vault Premium, leveraging hardware security modules (HSM) for enhanced protection. Developers can now perform symmetric cryptographic operations (such as encrypt, decrypt, wrap, and unwrap) directly with AES keys managed in Key Vault.

- Target audience affected  
Developers and IT professionals who require secure management of symmetric keys for encryption workloads, especially those needing HSM-backed key storage and operations. This update is relevant for teams building applications with sensitive data, compliance requirements, or integrating with Azure services that use symmetric encryption.

- Important notes if any  
This feature is currently in public preview, so it should not be used for production workloads until general availability. Customers and partners are encouraged to evaluate and provide feedback. Existing Key Vault APIs are extended to support symmetric key operations, but review documentation for compatibility and limitations during the preview phase.  
For more details, visit: https://azure.microsoft.com/updates?id=566746

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Symmetric keys on Azure Key Vault Premium  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=566746)

---

**Background and Purpose of the Update**  
Azure Key Vault is a cloud service for securely storing and accessing cryptographic keys, secrets, and certificates. Previously, Azure Key Vault primarily supported asymmetric keys for encryption, signing, and key management. This update introduces symmetric keys in Azure Key Vault Premium, specifically for customers and partners to evaluate symmetric encryption capabilities. The public preview aims to expand cryptographic support, addressing scenarios that require symmetric key operations, such as bulk data encryption and integration with applications needing AES-based encryption.

---

**Specific Features and Detailed Changes**  
- **Symmetric Key Support:** Azure Key Vault Premium now supports symmetric keys, enabling users to create, store, and manage symmetric keys within the vault.
- **oct-HSM Key Type:** The update introduces the `oct-HSM` key type, which represents symmetric keys stored and managed by Hardware Security Modules (HSMs) in Azure Key Vault Premium.
- **AES Algorithm:** Symmetric keys can be used with the Advanced Encryption Standard (AES), a widely adopted encryption algorithm for securing data.
- **Public Preview Availability:** The feature is currently in public preview, allowing customers to test and evaluate symmetric key functionalities before general availability.

---

**Technical Mechanisms and Implementation Methods**  
- **Key Creation and Management:** Users can generate symmetric keys of the `oct-HSM` type through Azure Key Vault Premium APIs, CLI, PowerShell, or portal interfaces.
- **HSM-backed Security:** Symmetric keys are protected by HSMs, ensuring high security and compliance for key material.
- **Cryptographic Operations:** Supported operations include encryption and decryption using AES. The Key Vault APIs facilitate these operations, abstracting direct access to key material and ensuring secure usage.
- **Access Control:** Access to symmetric keys is governed by Azure Key Vault’s access policies and RBAC, ensuring only authorized applications and users can perform cryptographic operations.

---

**Use Cases and Application Scenarios**  
- **Bulk Data Encryption:** Applications requiring high-performance encryption of large datasets can leverage AES symmetric keys for efficient cryptographic operations.
- **Integration with Line-of-Business Applications:** Systems that use symmetric encryption for securing sensitive information, such as financial or healthcare data, can now utilize Azure Key Vault Premium for centralized key management.
- **Compliance Requirements:** Organizations needing HSM-backed symmetric key storage for regulatory compliance can use this feature to meet security standards.
- **Partner Solutions:** Azure partners can integrate symmetric key management into their offerings, enhancing security for customer solutions.

---

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate and test thoroughly before deployment.
- **Supported Algorithms:** Currently, only AES is supported for symmetric key operations; other algorithms are not mentioned in the update.
- **Premium Tier Requirement:** Symmetric key support is exclusive to Azure Key Vault Premium, requiring users to provision and utilize this tier.
- **API and SDK Support:** Users should verify compatibility and support in their preferred Azure SDKs and tools for symmetric key operations.

---

**Integration with Related Azure Services**  
- **Azure Key Vault Integration:** Symmetric keys are managed alongside existing secrets, certificates, and asymmetric keys, providing a unified key management solution.
- **Azure Security and Compliance:** HSM-backed keys facilitate integration with Azure’s security and compliance frameworks, supporting secure application development.
- **Application Integration:** Applications hosted on Azure can securely access symmetric keys for cryptographic operations via Key Vault APIs, enabling seamless integration with Azure’s authentication and authorization mechanisms.

---

**Summary Sentence:**  
Azure Key Vault Premium now offers public preview support for symmetric keys using the oct-HSM key type and AES encryption, enabling secure, HSM-backed symmetric key management and

---

### 5. Public Preview: Support for SMB Opportunistic Locking (Oplocks) configuration 

**Published**: July 30, 2026 16:38:15 UTC
**Link**: [Public Preview: Support for SMB Opportunistic Locking (Oplocks) configuration ](https://azure.microsoft.com/updates?id=568396)

**Update ID**: 568396
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files, Feature

**Summary**:

**What was updated:**  
Azure NetApp Files now offers public preview support for configuring SMB opportunistic locking (oplocks) on SMB and dual-protocol volumes.

**Key changes or new features:**  
- Administrators can now enable or disable SMB oplocks during volume creation or update, providing greater control over SMB client caching behavior.
- Oplocks are enabled by default, but can be customized to suit application requirements.
- This feature applies to both new and existing volumes.

**Target audience affected:**  
- Developers working with applications that use Azure NetApp Files SMB shares, especially those requiring specific caching or file locking behavior.
- IT professionals and storage administrators managing file shares in Azure environments.

**Important notes:**  
- Oplocks improve performance by allowing SMB clients to cache files locally, but may need to be disabled for applications requiring strict data consistency (e.g., certain database workloads).
- Configuration changes can be made via Azure NetApp Files management interfaces.
- This feature is currently in public preview and may be subject to change before general availability.

[Read more](https://azure.microsoft.com/updates?id=568396)

**Details**:

**Azure Update Report: Public Preview – Support for SMB Opportunistic Locking (Oplocks) Configuration in Azure NetApp Files**

**Background and Purpose of the Update**  
This update introduces the ability to configure SMB opportunistic locking (oplocks) for SMB and dual-protocol volumes in Azure NetApp Files. Opportunistic locks are a critical SMB protocol feature that enhances client-side caching, reducing network traffic and improving performance for file operations. The purpose of this update is to provide administrators with granular control over oplock settings, allowing them to optimize performance and compatibility for their specific workloads.

**Specific Features and Detailed Changes**  
- **Oplocks Configuration:** Administrators can now enable or disable SMB oplocks on both new and existing Azure NetApp Files volumes that use SMB or dual-protocol (NFS+SMB) access.
- **Default Behavior:** Oplocks are enabled by default, aligning with standard SMB server behavior to maximize client caching efficiency.
- **Volume-Level Control:** Configuration can be applied during volume creation or updated on existing volumes, providing flexibility in managing file sharing scenarios.

**Technical Mechanisms and Implementation Methods**  
- **SMB Oplocks:** Oplocks are a mechanism in the SMB protocol that allows clients to cache file data locally while ensuring data consistency. When enabled, the server grants an oplock to a client, permitting local caching until another client requests access, at which point the oplock is broken and the client must synchronize changes.
- **Azure NetApp Files Integration:** The update exposes oplock configuration as a volume property within Azure NetApp Files. Administrators can set this property via the Azure Portal, CLI, or API when creating or modifying volumes.
- **Dual-Protocol Support:** The feature is available for both SMB-only and dual-protocol volumes, ensuring consistent behavior across heterogeneous access scenarios.

**Use Cases and Application Scenarios**  
- **Performance Optimization:** Workloads with high read operations and low file-sharing contention (e.g., user profile directories, home folders) benefit from enabled oplocks due to reduced latency and network load.
- **Compatibility:** Certain legacy applications or multi-client editing scenarios may require oplocks to be disabled to prevent caching-related conflicts. This update allows precise tuning for such environments.
- **Mixed Protocol Environments:** Organizations using both SMB and NFS can ensure consistent file access semantics by configuring oplocks appropriately on dual-protocol volumes.

**Important Considerations and Limitations**  
- **Default Setting:** Oplocks are enabled by default; administrators must explicitly disable them if required for specific workloads.
- **Data Consistency:** Disabling oplocks may impact performance but can be necessary for applications that do not tolerate client-side caching.
- **Preview Feature:** As this capability is in public preview, it may not be suitable for production workloads and is subject to change.
- **Scope:** The update applies only to Azure NetApp Files volumes with SMB or dual-protocol access. It does not affect NFS-only volumes.

**Integration with Related Azure Services**  
- **Azure NetApp Files:** The feature is natively integrated into Azure NetApp Files and managed through its standard interfaces (Portal, CLI, API).
- **Azure Ecosystem:** While specific integration points are not detailed, the update enhances compatibility for applications using SMB shares within the broader Azure environment, such as VMs, Azure Virtual Desktop, and hybrid scenarios.

**Summary Sentence**  
Azure NetApp Files now supports configurable SMB opportunistic locking (oplocks) for SMB and dual-protocol volumes, enabling administrators to optimize file caching behavior and performance according to workload requirements.

---


*This report was automatically generated - 2026-07-31 03:03:48 UTC*