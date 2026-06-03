# June 03, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 03, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 131 items

## Update List

### 1. Generally Available: Simple log alerts in Azure Monitor

**Published**: June 03, 2026 02:00:57 UTC
**Link**: [Generally Available: Simple log alerts in Azure Monitor](https://azure.microsoft.com/updates?id=561978)

**Update ID**: 561978
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features, Microsoft Build

**Summary**:

- What was updated  
Simple log alerts in Azure Monitor are now generally available.

- Key changes or new features  
The Simple log alerts feature offers a streamlined and user-friendly experience for creating and managing log-based alerts in Azure Monitor. This enhancement simplifies the process of setting up alerts based on log data, reducing configuration complexity and making it easier to monitor critical events and issues. It supports faster alert rule creation, improved management, and a more intuitive interface compared to classic log alerts.

- Target audience affected  
Developers and IT professionals responsible for monitoring, alerting, and incident response in Azure environments. Teams managing application performance, infrastructure health, and security events using Azure Monitor will benefit most.

- Important notes if any  
Simple log alerts are recommended for new alerting scenarios and are intended to eventually replace classic log alerts. Users should consider migrating existing classic log alert rules to the new Simple log alerts for improved experience and future support. For more details, refer to the official documentation: https://azure.microsoft.com/updates?id=561978

**Details**:

**Azure Update Report: Generally Available – Simple log alerts in Azure Monitor**

**Background and Purpose of the Update**  
The General Availability (GA) of Simple log alerts in Azure Monitor is aimed at streamlining the process of monitoring and alerting within the Azure ecosystem. The primary purpose of this update is to deliver a more simplified and intuitive experience for IT professionals who need to detect and respond to critical events in their Azure environments. This enhancement addresses the need for a user-friendly alerting mechanism that reduces complexity and accelerates the configuration and management of log-based alerts.

**Specific Features and Detailed Changes**  
With this release, Azure Monitor introduces "Simple log alerts," a feature that allows users to create log-based alerts with a more straightforward workflow. The update focuses on reducing the steps and configuration overhead typically associated with traditional log alert rules. Users can now define alert conditions directly from log queries with minimal setup, making it easier to monitor key metrics and logs without extensive customization. The user interface and alert rule creation process have been optimized for clarity and efficiency, targeting common monitoring scenarios.

**Technical Mechanisms and Implementation Methods**  
Simple log alerts operate by leveraging Azure Monitor’s existing log analytics capabilities. Users can specify a log query, and the system evaluates this query at defined intervals. When the query returns results that match the alert criteria, an alert is triggered. The implementation abstracts much of the complexity found in advanced log alert rules, such as detailed threshold configurations or multi-condition logic, focusing instead on rapid deployment and ease of use. This approach is particularly beneficial for scenarios where straightforward alerting suffices, and rapid response is critical.

**Use Cases and Application Scenarios**  
Simple log alerts are well-suited for IT professionals who require quick setup of monitoring for common operational events, such as error log detection, service health monitoring, or security incident identification. Typical scenarios include monitoring application logs for specific error codes, tracking resource usage anomalies, or receiving notifications when certain audit events occur. The simplified alerting process enables teams to deploy monitoring solutions rapidly, supporting both development and production environments.

**Important Considerations and Limitations**  
While Simple log alerts offer a streamlined experience, they may not provide the full range of customization available in advanced log alert rules. IT professionals should assess whether their monitoring requirements can be met with the simplified model or if more complex alert logic is necessary. Additionally, the GA status indicates production readiness, but users should review any service-specific documentation for potential limitations regarding supported log sources, alert frequency, or integration options.

**Integration with Related Azure Services**  
Simple log alerts are fully integrated within Azure Monitor and can be used in conjunction with other Azure services such as Azure Log Analytics, Azure Resource Manager, and Azure Action Groups. This integration enables automated responses, notifications, and incident management workflows to be triggered based on alert events. The feature is designed to complement existing Azure monitoring and automation tools, providing a cohesive experience for managing operational health and security within Azure environments.

**Summary Sentence**  
The General Availability of Simple log alerts in Azure Monitor introduces a streamlined, user-friendly approach to log-based alerting, enabling IT professionals to rapidly configure and manage essential monitoring scenarios with reduced complexity and seamless integration across Azure services.

---

### 2. Public Preview: Code-first observability for Foundry Agents in VS Code 

**Published**: June 02, 2026 23:15:29 UTC
**Link**: [Public Preview: Code-first observability for Foundry Agents in VS Code ](https://azure.microsoft.com/updates?id=563197)

**Update ID**: 563197
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry introduces code-first observability for agent developers, now available in public preview as an "observe" skill within the Foundry Plugin for VS Code Copilot Chat.

- Key changes or new features  
  - Developers can now access observability features directly in VS Code using the Foundry Plugin.  
  - The "observe" skill enables evaluation-driven optimization loops, allowing developers to monitor, debug, and refine agent behavior from within the editor.  
  - Integration with Copilot Chat streamlines the development and troubleshooting workflow for AI agents.

- Target audience affected  
  - Developers building and optimizing AI agents using Microsoft Foundry.  
  - IT professionals and DevOps teams responsible for agent performance and reliability.

- Important notes if any  
  - This feature is in public preview and may be subject to changes.  
  - The update enhances developer productivity by embedding observability and optimization tools directly in the development environment, reducing context switching.  
  - Users should ensure they have the latest version of the Foundry Plugin for VS Code to access these features.

For more details, see the [Azure Update](https://azure.microsoft.com/updates?id=563197).

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Code-first observability for Foundry Agents in VS Code

**Background and Purpose of the Update:**  
This update introduces code-first observability for developers building Foundry Agents, now available in public preview. The feature is designed to streamline the development and optimization of agents by integrating observability directly into the coding workflow. The primary goal is to enable developers to efficiently monitor, evaluate, and optimize agent behavior from within their development environment, reducing context switching and accelerating the development lifecycle.

**Specific Features and Detailed Changes:**  
- **Observe Skill in Foundry Plugin:** The update delivers a new "observe skill" as part of the Foundry Plugin for VS Code Copilot Chat.  
- **Editor-based Evaluation Loop:** Developers can execute the full evaluation-driven optimization loop directly from their VS Code editor. This means they can observe agent performance, analyze results, and iterate on improvements without leaving their coding environment.
- **Public Preview Availability:** The feature is currently in public preview, allowing early access for feedback and iterative improvement.

**Technical Mechanisms and Implementation Methods:**  
- **Integration with VS Code Copilot Chat:** The observe skill is embedded within the Foundry Plugin, leveraging the Copilot Chat interface. This integration allows developers to interact with observability features using natural language prompts and commands.
- **Code-first Approach:** Observability is initiated and managed through code-centric actions, aligning with modern DevOps and MLOps practices where monitoring and evaluation are tightly coupled with the development process.
- **Evaluation-driven Optimization:** The mechanism supports running evaluation loops—developers can trigger evaluations, view metrics, and refine agent logic iteratively, all from the VS Code environment.

**Use Cases and Application Scenarios:**  
- **Agent Development and Debugging:** Developers building Foundry Agents can use the observe skill to monitor agent performance in real-time, identify issues, and optimize logic during the coding phase.
- **Continuous Improvement:** Teams practicing continuous integration and deployment (CI/CD) can incorporate observability into their workflows, enabling rapid feedback and iterative enhancement of agent capabilities.
- **Collaborative Development:** The integration with Copilot Chat facilitates collaborative troubleshooting and knowledge sharing among team members within the familiar context of VS Code.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in public preview, it may not be fully stable or feature-complete. Users should be aware of potential changes and provide feedback to Microsoft for improvement.
- **VS Code and Plugin Requirements:** Utilization requires the Foundry Plugin for VS Code and access to Copilot Chat. Compatibility with other IDEs or environments is not mentioned.
- **Scope of Observability:** The update focuses specifically on Foundry Agents; applicability to other agent frameworks or services is not indicated.

**Integration with Related Azure Services:**  
- **Microsoft Foundry Platform:** The observe skill is part of the broader Microsoft Foundry ecosystem, which supports agent development and deployment.
- **VS Code Integration:** By embedding observability in the VS Code environment, the update aligns with Azure’s emphasis on developer productivity and seamless tooling.
- **Copilot Chat:** The feature leverages Copilot Chat for interactive, conversational access to observability functions, enhancing the developer experience.

**Summary:**  
Microsoft has released a public preview of code-first observability for Foundry Agents, enabling developers to monitor, evaluate, and optimize agent behavior directly within VS Code using the Foundry Plugin and Copilot Chat, streamlining the agent development and optimization workflow.

---

### 3. Generally Available: Agent kit for Azure Cosmos DB

**Published**: June 02, 2026 22:30:49 UTC
**Link**: [Generally Available: Agent kit for Azure Cosmos DB](https://azure.microsoft.com/updates?id=563022)

**Update ID**: 563022
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure Cosmos DB Agent Kit is now generally available.

- Key changes or new features  
The Agent Kit provides AI-powered coding agents with built-in best practices for developing high-performance applications on Azure Cosmos DB. It streamlines the development workflow by offering guidance and automation for common database tasks, such as data modeling, query optimization, and performance tuning. The kit integrates directly into your development environment, enabling faster and more reliable application development.

- Target audience affected  
Developers and IT professionals building or managing applications on Azure Cosmos DB, especially those leveraging AI coding agents or seeking to optimize database performance.

- Important notes if any  
The general availability of the Agent Kit means it is fully supported for production use. Developers can now incorporate these tools to improve application efficiency and reliability. Integration with existing workflows is designed to be seamless, but review documentation for compatibility with your current toolchain. For more details, visit the official update: https://azure.microsoft.com/updates?id=563022

**Details**:

**Azure Update Report: Generally Available – Agent Kit for Azure Cosmos DB**

**Background and Purpose of the Update**  
The Agent Kit for Azure Cosmos DB is now generally available, marking its transition from preview to a fully supported release. This update is designed to enhance the capabilities of AI coding agents, enabling them to build high-performance database applications more effectively. The primary purpose is to streamline the development workflow by embedding proven best practices for Azure Cosmos DB directly into the application development process.

**Specific Features and Detailed Changes**  
With this general availability, the Agent Kit provides a set of tools and resources that guide AI coding agents in the design, modeling, and implementation of database solutions using Azure Cosmos DB. The kit incorporates established best practices, which can help ensure that applications are optimized for performance, scalability, and reliability from the outset. The update signifies that the kit is now production-ready and supported for enterprise use.

**Technical Mechanisms and Implementation Methods**  
The Agent Kit operates by integrating with the development environment used by AI coding agents. It supplies templates, code snippets, and configuration guidelines that adhere to Azure Cosmos DB’s recommended patterns. This integration allows agents to automatically apply optimal partitioning strategies, indexing policies, and throughput configurations. The kit also facilitates the adoption of efficient data modeling techniques and query patterns, reducing the likelihood of common performance pitfalls.

**Use Cases and Application Scenarios**  
The Agent Kit is particularly valuable in scenarios where AI coding agents are tasked with generating or maintaining database-backed applications on Azure Cosmos DB. Typical use cases include:  
- Automated generation of data access layers in enterprise applications  
- Rapid prototyping of AI-driven solutions that require scalable NoSQL storage  
- Continuous integration and deployment (CI/CD) pipelines where database best practices must be enforced automatically  
- Educational environments where developers need to learn and apply Cosmos DB best practices efficiently

**Important Considerations and Limitations**  
While the Agent Kit brings best practices into the development workflow, it is essential for IT professionals to validate that the generated configurations and code align with their specific workload requirements. The kit is designed to accelerate and standardize development but may not cover all advanced or niche scenarios. Users should review the output for compliance with organizational standards and security policies. Additionally, as with any tool that automates code generation, ongoing maintenance and updates to the kit should be monitored to ensure compatibility with the latest Azure Cosmos DB features.

**Integration with Related Azure Services**  
The Agent Kit is intended to work seamlessly within the Azure ecosystem. It can be integrated into development pipelines that utilize Azure DevOps, GitHub Actions, or similar CI/CD tools. The kit’s output is optimized for deployment to Azure Cosmos DB, and it can be used in conjunction with other Azure services such as Azure Functions, Azure Logic Apps, and Azure App Service to create end-to-end cloud-native solutions.

**Summary**  
The general availability of the Agent Kit for Azure Cosmos DB delivers production-ready tools and best practices to AI coding agents, enabling the streamlined development of high-performance, scalable database applications on Azure Cosmos DB.

---

### 4. Public Preview: Azure SQL updates for early-June

**Published**: June 02, 2026 22:15:55 UTC
**Link**: [Public Preview: Azure SQL updates for early-June](https://azure.microsoft.com/updates?id=563142)

**Update ID**: 563142
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure SQL Database now supports using AES 256 symmetric keys for configuring Transparent Data Encryption (TDE) with customer-managed keys.

- Key changes or new features  
Developers and IT professionals can now select AES 256 encryption for TDE when using customer-managed keys, enhancing data protection options beyond previous offerings. This update allows for stronger encryption standards, aligning with industry best practices and compliance requirements.

- Target audience affected  
This update is relevant to database administrators, security architects, and developers managing Azure SQL Database instances, especially those with strict security or compliance needs requiring customer-managed encryption keys.

- Important notes if any  
The feature is currently in public preview as of early June 2026. Users should evaluate and test the new AES 256 option in non-production environments before broad adoption. Review Azure documentation for implementation details and any limitations during the preview phase.

Learn more: [Azure Update](https://azure.microsoft.com/updates?id=563142)

**Details**:

**Azure Update Report: Public Preview – Azure SQL updates for early-June**

**Background and Purpose of the Update**  
This update introduces support for using AES 256 symmetric keys to configure Transparent Data Encryption (TDE) with customer-managed keys (CMK) in Azure SQL Database. The primary purpose is to enhance data protection and compliance by allowing organizations to use stronger encryption algorithms and maintain greater control over their encryption keys.

**Specific Features and Detailed Changes**  
- Azure SQL Database now supports AES 256 symmetric keys for TDE when using customer-managed keys.
- Previously, TDE with customer-managed keys may have been limited to other algorithms or key sizes; this update specifically enables AES 256, which is widely regarded as a strong industry standard for symmetric encryption.
- The update is available in public preview as of early June 2026.

**Technical Mechanisms and Implementation Methods**  
- Transparent Data Encryption (TDE) is a feature that encrypts data at rest in Azure SQL Database, ensuring that stored data is protected from unauthorized access.
- With this update, when configuring TDE with customer-managed keys, users can now generate and manage AES 256 symmetric keys for encryption.
- Customer-managed keys are typically stored in Azure Key Vault, which integrates with Azure SQL Database to provide secure key management and access control.
- The process involves creating an AES 256 key in Azure Key Vault and configuring Azure SQL Database to use this key for TDE.
- The encryption and decryption operations are performed transparently by the database engine, without requiring changes to applications.

**Use Cases and Application Scenarios**  
- Organizations with strict regulatory or compliance requirements (such as financial services, healthcare, or government) that mandate the use of strong encryption algorithms like AES 256.
- Enterprises seeking to align with internal security policies that require customer control over encryption keys.
- Scenarios where data residency and sovereignty are critical, and customers need to manage their own keys for audit and compliance purposes.

**Important Considerations and Limitations**  
- This feature is currently in public preview, which means it may not be recommended for production workloads until it reaches general availability.
- Customers must ensure that their Azure Key Vault is properly configured and that they have the necessary permissions to create and manage AES 256 keys.
- Integration with TDE using customer-managed keys may require updates to existing key management processes and policies.
- There may be limitations or additional requirements specific to the preview phase; users should consult the official documentation for the latest guidance.

**Integration with Related Azure Services**  
- Azure Key Vault is the primary service for managing and storing customer-managed keys used by TDE in Azure SQL Database.
- The integration leverages Azure Active Directory (Azure AD) for authentication and access control to the keys.
- This update enhances the security posture of Azure SQL Database and complements other Azure security and compliance offerings.

**Summary Sentence**  
Azure SQL Database now supports configuring Transparent Data Encryption (TDE) with customer-managed AES 256 symmetric keys, providing enhanced encryption strength and greater key control for organizations, available in public preview as of early June 2026.

---

### 5. Public Preview: Secure, Modern Access to Azure Files on macOS with MS Entra ID 

**Published**: June 02, 2026 22:00:05 UTC
**Link**: [Public Preview: Secure, Modern Access to Azure Files on macOS with MS Entra ID ](https://azure.microsoft.com/updates?id=565073)

**Update ID**: 565073
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Files, Features, Microsoft Build, Security, Feature

**Summary**:

- What was updated  
Azure Files now supports access from macOS using Microsoft Entra ID (formerly Azure AD) authentication, available in Public Preview.

- Key changes or new features  
Developers and IT professionals can now enable secure, identity-based access to Azure Files from macOS devices. This integration allows macOS users to authenticate with Entra ID, aligning with existing support for Windows and Linux. It simplifies cross-platform collaboration and enforces modern security practices like conditional access and multi-factor authentication (MFA).

- Target audience affected  
This update is relevant for organizations with cross-platform teams, especially those using macOS devices alongside Windows and Linux. IT administrators managing file shares in Azure and developers building solutions that require secure file access from macOS will benefit.

- Important notes if any  
This feature is currently in Public Preview and may not be suitable for production workloads. Organizations should review the preview documentation for limitations and best practices. Integration with Entra ID enables centralized identity management and improved security posture for Azure Files across all major operating systems.

For more details, refer to the official update: https://azure.microsoft.com/updates?id=565073

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Secure, Modern Access to Azure Files on macOS with MS Entra ID

**Background and Purpose of the Update:**  
This update introduces support for accessing Azure Files from macOS using Microsoft Entra ID (formerly Azure Active Directory) authentication, now available in Public Preview. The primary objective is to enable secure, identity-based access to Azure file shares for users on macOS, thereby facilitating cross-platform collaboration and modernizing authentication workflows. Previously, Azure Files authentication was limited in scope for macOS users, often relying on less integrated or less secure methods. This enhancement addresses the need for unified, secure access across diverse operating systems within enterprise environments.

**Specific Features and Detailed Changes:**  
- **Entra ID Authentication for macOS:** Azure Files now supports authentication via Microsoft Entra ID for macOS clients. This allows users to access file shares using their organizational credentials, aligning with identity-based security practices.
- **Cross-Platform Access:** The update extends Azure Files’ compatibility, enabling seamless access for macOS users alongside existing Windows and Linux support.
- **Public Preview Availability:** The feature is currently in public preview, allowing organizations to evaluate and adopt the capability before general availability.

**Technical Mechanisms and Implementation Methods:**  
- **Identity-Based Access:** Authentication is performed using Microsoft Entra ID, ensuring that access to Azure Files is governed by organizational identity and access management policies.
- **Secure Authentication Flow:** Users on macOS authenticate against Entra ID, which issues the necessary tokens to authorize access to Azure file shares. This eliminates the need for legacy authentication mechanisms such as storage account keys or shared access signatures.
- **Integration with Azure Files:** The macOS client interacts with Azure Files over supported protocols, leveraging Entra ID tokens for authentication and access control.

**Use Cases and Application Scenarios:**  
- **Cross-Platform Teams:** Organizations with mixed operating system environments can enable secure, unified file share access for macOS users, improving collaboration and productivity.
- **Modern Workforce Enablement:** Enterprises supporting remote or hybrid work scenarios can ensure that macOS devices adhere to the same security and access standards as other platforms.
- **Identity-Driven Security:** IT administrators can enforce conditional access, multi-factor authentication, and other identity-based security controls for file share access on macOS.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads requiring full support or service-level guarantees.
- **Compatibility:** Organizations should verify macOS client compatibility and ensure that users have the necessary Entra ID credentials and permissions configured.
- **Policy Enforcement:** IT teams should review and update access policies in Entra ID to reflect the inclusion of macOS clients.

**Integration with Related Azure Services:**  
- **Microsoft Entra ID:** Central to the authentication process, providing identity management and access control for Azure Files.
- **Azure Files:** The core file storage service, now enhanced with modern authentication for macOS clients.
- **Conditional Access and Security Policies:** Organizations can leverage Entra ID’s security features to enforce access controls and compliance requirements for macOS users.

**Summary:**  
Azure Files now supports secure, identity-based access from macOS using Microsoft Entra ID authentication in public preview, enabling cross-platform teams to collaborate efficiently with modern security controls.

---

### 6. Generally Available: File share centric management model (Microsoft.FileShares) for Azure Files

**Published**: June 02, 2026 21:30:23 UTC
**Link**: [Generally Available: File share centric management model (Microsoft.FileShares) for Azure Files](https://azure.microsoft.com/updates?id=565062)

**Update ID**: 565062
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Files, Features, Management, Microsoft Build

**Summary**:

- What was updated  
The File share centric management model (Microsoft.FileShares) for Azure Files is now generally available, specifically for NFS 4.1 shares on SSD storage.

- Key changes or new features  
  - File shares are now first-class, top-level Azure resources, managed via the Microsoft.FileShares resource provider.  
  - You can directly create, manage, secure, and monitor file shares independently of the underlying storage account.  
  - Enhanced management capabilities, including Azure RBAC, resource-level locks, tags, and diagnostic settings, are now available at the file share level.  
  - Improved integration with Azure Resource Manager (ARM) templates, CLI, and REST APIs for automation and deployment.

- Target audience affected  
  - Developers and IT professionals managing Azure Files, especially those using NFS 4.1 shares on SSD storage.  
  - Teams automating infrastructure deployments or requiring granular access control and monitoring for file shares.

- Important notes if any  
  - This model is currently supported only for NFS 4.1 shares on premium SSD storage.  
  - Existing file shares on standard storage or using SMB protocols are not yet supported.  
  - Review your automation scripts and management processes to leverage the new resource provider and capabilities.

[More details](https://azure.microsoft.com/updates?id=565062)

**Details**:

**Azure Update: Generally Available – File Share Centric Management Model (Microsoft.FileShares) for Azure Files**

**Background and Purpose of the Update:**  
This update marks the general availability of a new file share service management experience for Azure Files, specifically targeting NFS 4.1 shares on SSD storage. The primary purpose is to enhance the management model by introducing file shares as top-level Azure resources, managed through the Microsoft.FileShares resource provider. This change aims to simplify and modernize the management, security, and lifecycle operations of Azure Files, aligning with how other Azure resources are managed.

**Specific Features and Detailed Changes:**  
- **Top-Level Resource Management:** File shares are now represented as first-class, top-level Azure resources. This allows direct creation, configuration, and management of file shares, rather than managing them as sub-resources of storage accounts.
- **Resource Provider:** The experience is powered by the new Microsoft.FileShares resource provider, which standardizes API interactions and resource management.
- **NFS 4.1 on SSD Support:** The update is currently available for file shares using the NFS 4.1 protocol on SSD-based storage, enabling high-performance and POSIX-compliant file sharing scenarios.
- **Security and Lifecycle Operations:** With file shares as top-level resources, IT professionals can now apply Azure RBAC, policies, and resource locks directly to individual file shares, providing granular security and governance.

**Technical Mechanisms and Implementation Methods:**  
- **Resource Model:** The Microsoft.FileShares resource provider introduces a new Azure Resource Manager (ARM) resource type for file shares. This enables CRUD (Create, Read, Update, Delete) operations via ARM templates, Azure CLI, PowerShell, and the Azure Portal.
- **Decoupling from Storage Accounts:** While file shares previously existed as entities within storage accounts, they now have their own resource identity and management plane, streamlining automation and integration.
- **Security Integration:** The model supports direct assignment of Azure policies and RBAC roles to file shares, leveraging Azure’s native identity and access management infrastructure.

**Use Cases and Application Scenarios:**  
- **Enterprise File Services:** Organizations requiring POSIX-compliant, high-performance file shares for Linux-based workloads can benefit from simplified provisioning and management.
- **DevOps Automation:** Teams can automate file share deployment and configuration using ARM templates or infrastructure-as-code tools, improving CI/CD workflows.
- **Granular Access Control:** Scenarios demanding per-share security policies, such as multi-tenant environments or departmental isolation, are now easier to implement.

**Important Considerations and Limitations:**  
- **Scope:** The update is generally available only for NFS 4.1 shares on SSD storage. Other protocols (such as SMB) or storage tiers are not included in this release.
- **Migration:** Existing file shares managed under the storage account model may require migration or special handling to leverage the new management model.
- **Resource Limits:** As with other Azure resources, there may be quotas or limitations on the number of top-level file shares per subscription or region.

**Integration with Related Azure Services:**  
- **Azure RBAC and Policy:** Direct integration allows for fine-grained access control and compliance enforcement at the file share level.
- **Azure Monitor and Security Center:** File shares as top-level resources can be monitored and secured using Azure’s native management and security tools.
- **Automation Tools:** The new model supports integration with ARM templates, Azure CLI, and PowerShell for automated deployment and lifecycle management.

**Summary:**  
The general availability of the file share centric management model (Microsoft.FileShares) for Azure Files introduces top-level resource management for NFS 4.1 shares on SSD storage, enabling direct creation, security, and lifecycle operations with enhanced integration into Azure’s resource management ecosystem.

---

### 7. Preview: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines 

**Published**: June 02, 2026 21:00:30 UTC
**Link**: [Preview: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines ](https://azure.microsoft.com/updates?id=564451)

**Update ID**: 564451
**Data source**: Azure Updates API

**Categories**: In development, Compute, Virtual Machines, Features, Microsoft Build

**Summary**:

- What was updated  
Azure has announced the public preview of new Arm-based Cobalt 200 series Virtual Machines: Dpsv7, Dplsv7 (general purpose), Epsv7 (memory-optimized), Mpsv4 (high-memory), and Lpsv5 (dense storage).

- Key changes or new features  
These new VM series offer significant performance and efficiency improvements over the previous Cobalt 100 series. Key enhancements include:  
  - Up to 20% better price-performance for general-purpose workloads  
  - Increased memory and storage options, especially in Epsv7 (memory-optimized) and Lpsv5 (dense storage) variants  
  - Enhanced scalability and support for a wider range of workloads, including high-memory and storage-intensive applications  
  - Built on the latest Arm architecture, providing improved energy efficiency and cost savings

- Target audience affected  
Developers and IT professionals running Linux-based workloads, cloud-native applications, databases, and storage-intensive solutions on Azure. Organizations seeking cost-effective, scalable, and energy-efficient VM options will benefit most.

- Important notes if any  
These VMs are currently in public preview and may not be suitable for production workloads. Review compatibility for your applications, as these VMs are Arm-based and may require architecture-specific optimizations. Check regional availability and pricing before deployment.

[Read more](https://azure.microsoft.com/updates?id=564451)

**Details**:

**Azure Update Technical Explanation**

**Title:** Preview: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=564451)

---

### Background and Purpose of the Update

This update announces the public preview of the Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines (VMs). The purpose is to provide Azure customers with access to the latest generation of Arm-based VMs, which deliver significant enhancements over the previous Cobalt 100 series. These improvements are targeted at increasing performance, efficiency, and workload specialization across general-purpose, memory-optimized, high-memory, and dense storage VM categories.

---

### Specific Features and Detailed Changes

- **VM Series Introduced:**
  - **Dpsv7 and Dplsv7:** General-purpose VMs suitable for a wide range of workloads.
  - **Epsv7:** Memory-optimized VMs designed for memory-intensive applications.
  - **Mpsv4:** High-memory VMs for demanding enterprise workloads.
  - **Lpsv5:** Dense storage VMs optimized for storage-heavy scenarios.

- **Enhancements Over Previous Generation:**
  - These VMs are based on the new Cobalt 200 Arm architecture, offering improved performance and capabilities compared to the Cobalt 100 series.
  - Each VM series is tailored to specific workload requirements, providing better alignment with customer needs for compute, memory, and storage.

---

### Technical Mechanisms and Implementation Methods

- **Cobalt 200 Arm-based Architecture:**
  - The VMs leverage the Cobalt 200 Arm-based processors, which are engineered to deliver higher efficiency and performance.
  - The architecture enables Azure to offer differentiated VM SKUs optimized for various workload profiles (general-purpose, memory-optimized, high-memory, and dense storage).

- **Preview Availability:**
  - These VM series are currently available in preview, allowing customers to test and evaluate the new capabilities before general availability.

---

### Use Cases and Application Scenarios

- **General-Purpose Workloads:**  
  Dpsv7 and Dplsv7 VMs are suitable for web servers, application servers, and enterprise-grade applications requiring balanced CPU and memory resources.

- **Memory-Intensive Applications:**  
  Epsv7 VMs are ideal for in-memory databases, caching solutions, and analytics workloads that demand high memory bandwidth and capacity.

- **High-Memory Enterprise Workloads:**  
  Mpsv4 VMs support large-scale databases, SAP HANA, and other business-critical applications that require extensive memory resources.

- **Storage-Heavy Scenarios:**  
  Lpsv5 VMs are optimized for big data, data warehousing, and storage-centric applications needing high disk throughput and capacity.

---

### Important Considerations and Limitations

- **Preview Status:**  
  As these VMs are in preview, they may not be suitable for production workloads. Customers should validate compatibility and performance in test environments.

- **Regional Availability:**  
  Availability may be limited to specific Azure regions during the preview phase.

- **Support and SLA:**  
  Preview features typically do not carry the same support and SLA commitments as generally available services.

---

### Integration with Related Azure Services

- These VM series can be integrated with standard Azure services such as Azure Virtual Network, Azure Storage, Azure Backup, and Azure Monitor.
- Customers can leverage these VMs as part of their existing Azure infrastructure, utilizing familiar management tools and automation frameworks.

---

**Summary:**  
The preview release of Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv

---

### 8. Generally Available: Unified Text Translation API in Azure AI Translator

**Published**: June 02, 2026 21:00:30 UTC
**Link**: [Generally Available: Unified Text Translation API in Azure AI Translator](https://azure.microsoft.com/updates?id=563631)

**Update ID**: 563631
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure AI Translator service has announced the general availability of its Unified Text Translation API.

- Key changes or new features  
The Unified Text Translation API provides a single endpoint that integrates multiple translation capabilities, including neural machine translation, large language model (LLM) translation, small language model translation, and Adaptive custom translation. This consolidation simplifies integration and management for developers by removing the need to interact with multiple APIs for different translation scenarios.

- Target audience affected  
This update is relevant for developers building multilingual applications, IT professionals managing translation services, and organizations leveraging Azure AI Translator for global content localization.

- Important notes if any  
Developers can now access various translation models and custom translation features through one unified API endpoint, streamlining workflows and reducing complexity in codebases. Existing users should review documentation to understand migration paths from legacy endpoints to the new unified API. This release supports improved scalability and flexibility for integrating translation services into applications. For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=563631

**Details**:

**Azure Update Technical Report: Generally Available – Unified Text Translation API in Azure AI Translator**

**Background and Purpose of the Update**  
The Azure AI Translator service has announced the general availability (GA) of its unified Text Translation API. The primary purpose of this update is to streamline and simplify the integration of multiple translation technologies by providing developers with a single API endpoint. This unification aims to reduce complexity in application development, enhance maintainability, and provide a consistent interface for accessing various translation capabilities within Azure AI Translator.

**Specific Features and Detailed Changes**  
With this update, the unified Text Translation API consolidates several translation technologies under one endpoint. The API now fronts:
- Neural Machine Translation (NMT)
- Large Language Model (LLM) Translation
- Small Language Model (SLM) Translation
- Adaptive Custom Translation

This consolidation means that developers no longer need to manage multiple endpoints or APIs for different translation models or customizations. Instead, all translation requests—whether using standard neural models, large or small language models, or adaptive customizations—are routed through a single, unified API endpoint.

**Technical Mechanisms and Implementation Methods**  
The unified API abstracts the underlying translation model selection and orchestration. When a translation request is made, the API determines the appropriate translation engine (NMT, LLM, SLM, or Adaptive Custom) based on the request parameters and configuration. This mechanism allows for seamless switching between different translation technologies without code changes on the client side. The API endpoint exposes standard RESTful interfaces, ensuring compatibility with existing HTTP-based integration patterns.

**Use Cases and Application Scenarios**  
The unified Text Translation API is suitable for a wide range of enterprise and developer scenarios, including:
- Multilingual content translation for web and mobile applications
- Real-time chat or messaging translation
- Document localization workflows
- Integration into customer support platforms for language support
- Custom domain-specific translation using Adaptive Custom Translation

By consolidating translation capabilities, organizations can more easily scale their multilingual solutions and maintain a consistent integration approach across different projects.

**Important Considerations and Limitations**  
- The update provides a single endpoint for multiple translation models, but developers should ensure that their usage scenarios align with the supported features of each underlying model (NMT, LLM, SLM, Adaptive Custom).
- Existing integrations may require endpoint reconfiguration to leverage the unified API.
- Developers should review the API documentation for any changes in authentication, request structure, or response formats.
- Performance and latency may vary depending on the selected translation model and the complexity of the translation task.

**Integration with Related Azure Services**  
The unified Text Translation API is designed to integrate seamlessly with other Azure AI services and workflows. It can be used in conjunction with Azure Cognitive Services, Azure Logic Apps, Azure Functions, and Azure Data Factory for automated translation pipelines. The unified endpoint also simplifies integration with Azure security and monitoring tools, such as Azure Active Directory for authentication and Azure Monitor for logging and diagnostics.

**Summary**  
The general availability of the unified Text Translation API in Azure AI Translator provides a single, streamlined endpoint for accessing neural, large and small language model, and adaptive custom translation capabilities, simplifying integration and management for developers and IT professionals.

---

### 9. Public Preview: Azure API Management introduces a Unified Model API for multi-model AI applications. 

**Published**: June 02, 2026 21:00:30 UTC
**Link**: [Public Preview: Azure API Management introduces a Unified Model API for multi-model AI applications. ](https://azure.microsoft.com/updates?id=562853)

**Update ID**: 562853
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management has introduced a Unified Model API in public preview, designed to simplify integration with multiple large language model (LLM) providers for AI applications.

- Key changes or new features  
The Unified Model API provides a standardized interface for developers to interact with various LLM providers (such as OpenAI, Azure OpenAI, and others) through a single API endpoint. This eliminates the need to manage different API formats, SDKs, and integration patterns for each provider. The unified model also streamlines provider switching, failover, and governance, making it easier to build, manage, and scale multi-model AI solutions.

- Target audience affected  
This update is relevant to developers building AI applications that leverage multiple LLM providers, as well as IT professionals responsible for API management, integration, and governance in enterprise environments.

- Important notes if any  
The Unified Model API is currently in public preview and may not be suitable for production workloads. Developers should review the documentation for supported providers and features. Integration with Azure API Management enables centralized monitoring, security, and policy enforcement across all LLM endpoints.  
For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=562853).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure API Management introduces a Unified Model API for multi-model AI applications

**Background and Purpose of the Update:**  
As organizations increasingly adopt multiple large language model (LLM) providers, developers face significant challenges due to the need to accommodate various API formats, SDKs, and integration patterns for each model vendor. This diversity increases application complexity and operational overhead, complicates provider switching, impedes seamless failover, and introduces governance difficulties. The purpose of this update is to address these issues by standardizing how multi-model AI applications interact with different LLM providers.

**Specific Features and Detailed Changes:**  
Azure API Management now introduces a Unified Model API, available in public preview, specifically designed for multi-model AI applications. This feature provides a single, consistent API surface for developers to interact with multiple LLM providers. The Unified Model API abstracts the differences between various model vendors, enabling developers to integrate and manage multiple LLMs through a standardized interface. This reduces the need for custom code to handle each provider's unique API and simplifies the overall integration process.

**Technical Mechanisms and Implementation Methods:**  
The Unified Model API is implemented as part of Azure API Management. It acts as an intermediary layer that translates standardized API requests from client applications into the appropriate format required by each underlying LLM provider. This translation mechanism ensures that developers can use a common request and response schema, regardless of the actual LLM backend. The API Management platform handles the routing, transformation, and aggregation of requests and responses, providing a seamless and unified developer experience.

**Use Cases and Application Scenarios:**  
- **Multi-vendor LLM Integration:** Organizations leveraging multiple AI model providers can use the Unified Model API to streamline integration and reduce development effort.
- **Provider Switching and Failover:** Applications can more easily switch between LLM providers or implement failover strategies without significant code changes.
- **Centralized Governance:** Enterprises can enforce consistent governance, monitoring, and security policies across all LLM interactions via the unified API layer.
- **Simplified Development:** Developers building AI-driven applications can focus on business logic rather than handling multiple SDKs and API formats.

**Important Considerations and Limitations:**  
- The Unified Model API is currently in public preview, which may imply limited support, potential changes, and the need for caution when deploying in production environments.
- As the feature abstracts multiple LLM providers, some provider-specific capabilities or optimizations may not be fully exposed through the unified interface.
- Developers should review documentation for supported LLM providers and any limitations in API coverage or functionality.

**Integration with Related Azure Services:**  
The Unified Model API is integrated within Azure API Management, allowing organizations to leverage existing API gateway features such as authentication, authorization, rate limiting, logging, and analytics. This integration facilitates centralized management and monitoring of AI model interactions, and supports broader Azure ecosystem capabilities such as Azure Monitor and Azure Policy for compliance and operational insights.

**Summary:**  
Azure API Management’s Unified Model API, now in public preview, provides a standardized interface for multi-model AI applications, reducing integration complexity and enabling streamlined management of multiple LLM providers.

---

### 10. Generally Available: Azure API Management Premium v2 and Standard v2 now support wildcard custom hostnames. 

**Published**: June 02, 2026 20:45:52 UTC
**Link**: [Generally Available: Azure API Management Premium v2 and Standard v2 now support wildcard custom hostnames. ](https://azure.microsoft.com/updates?id=562894)

**Update ID**: 562894
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management Premium v2 and Standard v2 now support wildcard custom hostnames (generally available).

- Key changes or new features  
Both Premium v2 and Standard v2 tiers of Azure API Management now allow configuration of wildcard custom hostnames (e.g., *.api.contoso.com). This enables a single SSL certificate to secure multiple subdomains, simplifying domain and certificate management. Previously, each subdomain required individual configuration and certificates, increasing operational complexity.

- Target audience affected  
Developers and IT professionals managing large API estates, especially those using Azure API Management Premium v2 or Standard v2 and handling multiple subdomains.

- Important notes if any  
Wildcard hostname support streamlines onboarding and management of APIs with many subdomains, reducing administrative overhead and certificate sprawl. Ensure your DNS and certificate configurations are compatible with wildcard usage. This feature is only available in Premium v2 and Standard v2 tiers; it is not supported in the Consumption or Developer tiers. Review your security policies to ensure wildcard certificates meet your compliance requirements.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=562894)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure API Management Premium v2 and Standard v2 now support wildcard custom hostnames  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562894)

---

### Background and Purpose of the Update

As organizations expand their API portfolios, the number of APIs and corresponding subdomains increases significantly. Traditionally, each subdomain (e.g., payments.api.contoso.com, inventory.api.contoso.com) required individual configuration and management of custom domains and SSL/TLS certificates within Azure API Management (APIM). This approach quickly becomes operationally complex and difficult to scale, especially for large API estates. The purpose of this update is to simplify domain and certificate management by introducing support for wildcard custom hostnames in Azure API Management Premium v2 and Standard v2 tiers.

---

### Specific Features and Detailed Changes

- **Wildcard Custom Hostname Support:**  
  Both Premium v2 and Standard v2 tiers of Azure API Management now allow the configuration of wildcard custom hostnames (e.g., *.api.contoso.com).
- **Simplified Certificate Management:**  
  Administrators can now use a single wildcard SSL/TLS certificate to secure all subdomains under a given domain, instead of managing individual certificates for each subdomain.
- **Scalability:**  
  This feature removes the need to manually register and configure each new subdomain, streamlining the process as new APIs are deployed.

---

### Technical Mechanisms and Implementation Methods

- **Hostname Binding:**  
  When configuring a custom domain in APIM, users can now specify a wildcard hostname (e.g., *.api.contoso.com) in the custom domain settings.
- **Certificate Association:**  
  A corresponding wildcard SSL/TLS certificate must be uploaded and associated with the wildcard hostname. The certificate must be valid for all subdomains covered by the wildcard.
- **Routing and Resolution:**  
  Incoming requests to any subdomain matching the wildcard pattern are routed to the APIM instance, which uses the associated certificate for TLS termination and processes the request as per the configured API policies.

---

### Use Cases and Application Scenarios

- **Multi-API Environments:**  
  Organizations hosting multiple APIs under different subdomains (e.g., payments.api.contoso.com, orders.api.contoso.com) can now manage all endpoints with a single wildcard domain and certificate.
- **Dynamic API Provisioning:**  
  Environments where APIs are dynamically created or scaled (such as multi-tenant SaaS platforms) benefit from reduced operational overhead, as new subdomains do not require manual configuration.
- **DevOps Automation:**  
  Automated deployment pipelines can provision new APIs without additional steps for domain or certificate management.

---

### Important Considerations and Limitations

- **Certificate Requirements:**  
  The wildcard certificate must be valid for the entire subdomain range (e.g., *.api.contoso.com) and securely stored.
- **Tier Availability:**  
  Wildcard custom hostname support is only available in Premium v2 and Standard v2 tiers. It is not available in lower tiers.
- **DNS Configuration:**  
  DNS records must be properly configured to route all relevant subdomains to the APIM gateway endpoint.
- **Security:**  
  Proper management of wildcard certificates is critical, as compromise of a wildcard certificate can affect all subdomains.

---

### Integration with Related Azure Services

- **Azure Key Vault:**  
  Wildcard certificates can be securely stored and managed in Azure Key Vault, and referenced from APIM for automated certificate rotation.
- **Azure DNS:**  
  DNS zones and records for wildcard subdomains can be managed via Azure DNS for seamless integration with APIM.
- **Azure DevOps:**  
  Integration with CI/CD pipelines allows automated deployment of APIs under new subdomains without manual intervention.

---

**Summary Sentence:**  
Azure API Management Premium v2 and Standard v2 now support wildcard custom hostnames, enabling simplified and scalable management of domains and certificates

---

### 11. Global PTU Reservations Are Now Region-Agnostic

**Published**: June 02, 2026 20:45:52 UTC
**Link**: [Global PTU Reservations Are Now Region-Agnostic](https://azure.microsoft.com/updates?id=562657)

**Update ID**: 562657
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Pricing & Offerings

**Summary**:

- What was updated  
Global Provisioned Throughput Unit (PTU) reservations in Azure are now region-agnostic.

- Key changes or new features  
Previously, PTU reservations were tied to specific regions. With this update, a single Global PTU reservation can now be used across multiple Azure regions, rather than being restricted to one. This allows organizations to optimize their reserved capacity usage and maximize cost savings by applying a single reservation to deployments in any region.

- Target audience affected  
This update primarily affects developers and IT professionals managing global Azure deployments, especially those using services that rely on provisioned throughput (such as Azure Cosmos DB or other globally distributed databases).

- Important notes if any  
Organizations can now achieve better reservation utilization and reduce costs by consolidating PTU reservations across regions. No changes are required to existing deployments to take advantage of this feature. Review your current PTU reservation strategy to ensure you are maximizing savings under the new region-agnostic model.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=562657)

**Details**:

**Azure Update Report: Global PTU Reservations Are Now Region-Agnostic**

**Background and Purpose of the Update**  
Previously, Provisioned Throughput Unit (PTU) reservations in Azure were tied to specific regions. This meant that organizations deploying global workloads had to manage separate PTU reservations for each region, often resulting in underutilized reservations and increased operational complexity. The purpose of this update is to streamline PTU reservation management and optimize cost efficiency for customers with multi-region deployments.

**Specific Features and Detailed Changes**  
With this update, Global PTU reservations are now region-agnostic. A single PTU reservation can now be applied across multiple Azure regions, rather than being limited to a specific region. This enhancement allows customers to consolidate their PTU reservations and allocate provisioned throughput more flexibly across their global deployments.

**Technical Mechanisms and Implementation Methods**  
The implementation of region-agnostic PTU reservations means that when a customer purchases a Global PTU reservation, Azure automatically applies the reserved throughput to eligible deployments, regardless of their regional location. The Azure platform tracks PTU consumption across all regions and ensures that the reservation is utilized wherever the workload is deployed. This is managed through Azure’s centralized billing and resource management systems, which now recognize and allocate PTU reservations at a global rather than regional level.

**Use Cases and Application Scenarios**  
- **Global SaaS Providers:** Organizations running Software-as-a-Service (SaaS) applications with users distributed worldwide can now purchase a single PTU reservation to cover throughput needs in all regions, simplifying management and optimizing costs.
- **Disaster Recovery and High Availability:** Enterprises deploying redundant workloads across multiple regions for disaster recovery or high availability can leverage a single reservation, ensuring efficient utilization without the need for over-provisioning in each region.
- **Dynamic Workload Distribution:** Businesses with fluctuating workloads that shift between regions (e.g., due to traffic patterns or compliance requirements) benefit from the flexibility of region-agnostic reservations, as throughput can be dynamically allocated where needed.

**Important Considerations and Limitations**  
- **Reservation Scope:** Only Global PTU reservations are region-agnostic. Region-specific reservations may still exist for certain services or legacy configurations.
- **Eligible Deployments:** The reservation applies only to Global PTU deployments. Customers must ensure their workloads are compatible with global reservation policies.
- **Billing and Reporting:** Usage and savings are consolidated at the global level, so customers should review their billing reports to understand how reservations are being applied across regions.
- **Service Compatibility:** This update applies to services that support Global PTU reservations. Customers should verify service eligibility before planning migrations or consolidations.

**Integration with Related Azure Services**  
Region-agnostic PTU reservations integrate seamlessly with Azure’s resource management, billing, and monitoring tools. Customers can manage reservations via the Azure Portal, Azure Resource Manager (ARM), and APIs. Integration with Azure Cost Management allows for detailed tracking of reservation utilization and cost savings across all regions. This update also complements Azure’s global infrastructure, supporting consistent and efficient resource provisioning for distributed applications.

**Summary Sentence**  
Global PTU reservations are now region-agnostic, allowing a single reservation to cover deployments across multiple Azure regions, thereby simplifying management and optimizing cost efficiency for multi-region workloads.

---

### 12. Public Preview: Azure Backup for Cosmos DB

**Published**: June 02, 2026 20:15:03 UTC
**Link**: [Public Preview: Azure Backup for Cosmos DB](https://azure.microsoft.com/updates?id=562769)

**Update ID**: 562769
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Backup for Cosmos DB is now available in Public Preview, enabling vaulted backups for Cosmos DB accounts.

- Key changes or new features  
  - Vaulted backups: Secure, isolated, and resilient backups for Cosmos DB data, stored in an Azure Recovery Services vault.  
  - Enhanced cyber-resiliency: Protects against accidental deletion, ransomware, and other data loss scenarios.  
  - Compliance support: Meets organizational and regulatory backup and retention requirements.  
  - Centralized management: Integrates with Azure Backup Center for unified backup monitoring and management.  
  - Granular restore: Supports point-in-time restore capabilities for Cosmos DB accounts.

- Target audience affected  
Developers and IT professionals managing mission-critical data in Azure Cosmos DB, especially those with compliance, security, or backup retention requirements.

- Important notes  
  - This feature is currently in Public Preview and may not be suitable for production workloads.  
  - Vaulted backups are stored outside the Cosmos DB account, enhancing data isolation and protection.  
  - Integration with Azure Backup Center allows for streamlined backup operations across multiple data sources.  
  - Review preview documentation and limitations before enabling in critical environments.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=562769).

**Details**:

**Azure Update Report: Public Preview – Azure Backup for Cosmos DB**

**Background and Purpose of the Update**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications requiring high availability, scalability, and performance. Traditionally, backup and restore capabilities for Cosmos DB have been limited to built-in periodic backups, which may not meet stringent requirements for cyber-resiliency, compliance, or isolated backup storage. The introduction of Azure Backup for Cosmos DB addresses these gaps by enabling vaulted backups, providing enhanced data protection and recovery options for enterprise workloads.

**Specific Features and Detailed Changes**  
With this update, users can now enable vaulted backups for their Azure Cosmos DB accounts. Vaulted backups are stored in a secure, isolated location, separate from the primary Cosmos DB instance, offering increased resilience against accidental deletion, corruption, or ransomware attacks. The preview release allows users to configure backup policies, schedule backups, and manage backup retention, supporting compliance and regulatory requirements for data protection. This feature is accessible through the Azure Backup service, providing a unified experience for managing backups across multiple Azure resources.

**Technical Mechanisms and Implementation Methods**  
Azure Backup for Cosmos DB leverages the Azure Backup infrastructure to orchestrate and store backups in a dedicated backup vault. When enabled, the service periodically captures consistent snapshots of Cosmos DB data and transfers them to the backup vault, ensuring isolation from the source database. Backup operations are managed via Azure Portal, REST APIs, or PowerShell, allowing for automation and integration into existing workflows. The backup vault provides secure storage, access control, and lifecycle management for backup data, supporting granular restore operations as needed.

**Use Cases and Application Scenarios**  
- **Cyber-resiliency:** Protecting against ransomware, accidental deletion, or malicious activity by storing backups in an isolated vault.
- **Compliance:** Meeting regulatory requirements for data retention, backup isolation, and recovery capabilities.
- **Disaster Recovery:** Enabling rapid restoration of Cosmos DB accounts in the event of data loss or corruption.
- **Operational Backup:** Supporting routine backup and restore operations for development, testing, or migration scenarios.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not support all Cosmos DB configurations or regions. Users should verify compatibility with their Cosmos DB account types and review documentation for supported backup frequencies, retention policies, and restore procedures. Performance impacts during backup operations, cost implications for vaulted storage, and integration with existing backup strategies should be evaluated. Additionally, preview features may be subject to change and are not recommended for production-critical workloads until general availability.

**Integration with Related Azure Services**  
Azure Backup for Cosmos DB integrates directly with Azure Backup, allowing centralized management of backups across Azure resources such as VMs, SQL databases, and now Cosmos DB. Backup vaults provide secure storage and policy management, while Azure Monitor and Azure Policy can be used to track backup status and enforce compliance. Integration with Azure Resource Manager enables automated deployment and configuration of backup settings within infrastructure-as-code workflows.

**Summary Sentence**  
Azure Backup for Cosmos DB, now in public preview, enables secure, isolated, and resilient vaulted backups for Cosmos DB accounts, supporting cyber-resiliency and compliance needs through integration with Azure Backup and backup vaults.

---

### 13. Public Preview: Azure Policy Coverage for Model Router in Foundry Models

**Published**: June 02, 2026 20:00:59 UTC
**Link**: [Public Preview: Azure Policy Coverage for Model Router in Foundry Models](https://azure.microsoft.com/updates?id=563636)

**Update ID**: 563636
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Policy now supports centralized governance for deployments using the model router in Foundry Models, currently in public preview.

- Key changes or new features  
Organizations can define and enforce policies for how models are routed and selected within their Azure environment. This enables consistent application of security, compliance, and operational standards to model selection and routing processes. Policy coverage helps automate governance and reduces manual oversight for model deployments.

- Target audience affected  
This update is relevant for IT professionals responsible for governance, security, and compliance, as well as developers deploying AI models using the model router in Foundry Models.

- Important notes if any  
Policies can be created to restrict or require specific model routing behaviors, ensuring alignment with organizational standards. This feature is in public preview, so it may not be suitable for production workloads yet. Early adoption is recommended for organizations seeking to standardize and automate model deployment governance. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=563636).

**Details**:

**Azure Update Report: Public Preview – Azure Policy Coverage for Model Router in Foundry Models**

**Background and Purpose of the Update**  
The update introduces Azure Policy coverage for the model router component in Foundry Models, now available in public preview. The model router is a critical element in AI/ML deployments, responsible for directing inference requests to appropriate machine learning models based on defined criteria. The purpose of this update is to enable organizations to apply centralized governance and compliance controls to model routing activities, ensuring that model selection and routing adhere to organizational standards for security, compliance, and operational consistency.

**Specific Features and Detailed Changes**  
With this update, Azure Policy can now be used to define, enforce, and audit routing standards for deployments utilizing the model router in Foundry Models. Key features include:

- **Centralized Policy Management:** Administrators can create and assign Azure Policy definitions that govern how model routers select and route models.
- **Enforcement of Routing Standards:** Policies can enforce specific routing behaviors, such as restricting model selection to approved models or enforcing compliance with regulatory requirements.
- **Audit and Compliance Reporting:** Azure Policy provides auditing capabilities to track policy compliance and generate reports on routing activities.

**Technical Mechanisms and Implementation Methods**  
Azure Policy operates by evaluating resources against defined policy rules. For the model router in Foundry Models:

- **Policy Definitions:** Custom or built-in policy definitions are created to specify routing requirements (e.g., allowed models, routing criteria).
- **Assignment:** Policies are assigned to relevant scopes (subscriptions, resource groups, or individual resources) where model routers are deployed.
- **Evaluation and Enforcement:** Azure Policy continuously evaluates model router configurations and activities against assigned policies, enforcing compliance by denying non-compliant deployments or flagging them for remediation.
- **Integration with Foundry Models:** The model router exposes configuration and operational metadata that Azure Policy can reference for evaluation.

**Use Cases and Application Scenarios**  
This update is particularly valuable for:

- **Regulated Industries:** Ensuring that only compliant models are routed in environments subject to regulatory oversight (e.g., finance, healthcare).
- **Enterprise Governance:** Enforcing internal standards for model selection, versioning, and operational practices across multiple teams and projects.
- **Security and Risk Management:** Restricting routing to models that have passed security reviews or limiting exposure to sensitive data.

**Important Considerations and Limitations**  
- **Public Preview:** The feature is currently in public preview, which may entail limited support and evolving functionality.
- **Scope of Enforcement:** Policies are only effective within the boundaries of the model router and Foundry Models; external integrations or custom routing logic may not be covered.
- **Policy Complexity:** Careful design of policy definitions is required to avoid unintended blocking of legitimate routing scenarios.

**Integration with Related Azure Services**  
Azure Policy coverage for the model router integrates seamlessly with:

- **Azure Policy Management:** Leverages existing policy management, assignment, and compliance reporting tools.
- **Foundry Models:** Directly governs model router operations within Foundry Models deployments.
- **Azure Monitor and Security Center:** Policy compliance data can be surfaced in monitoring and security dashboards for broader visibility.

**Summary Sentence**  
Azure Policy coverage for the model router in Foundry Models enables organizations to centrally define, enforce, and audit routing standards for AI/ML model deployments, supporting enhanced security, compliance, and operational governance in Azure environments.

---

### 14. Generally Available: Voice Live integration with Microsoft Foundry Agent Service

**Published**: June 02, 2026 20:00:59 UTC
**Link**: [Generally Available: Voice Live integration with Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=563601)

**Update ID**: 563601
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- **What was updated**  
Microsoft Foundry Agent Service is now generally available with Voice Live integration.

- **Key changes or new features**  
Developers can now integrate real-time speech-to-text and text-to-speech capabilities directly with a Foundry Agent using Voice Live, without needing to build or manage their own audio processing pipeline. This streamlines the process of adding voice interaction to applications and leverages existing agent features such as conversation management and orchestration.

- **Target audience affected**  
This update is relevant for developers building conversational AI solutions, IT professionals managing voice-enabled applications, and teams leveraging Microsoft Foundry Agent Service for intelligent agent scenarios.

- **Important notes if any**  
The integration reduces development complexity and accelerates deployment of voice-enabled agents. Existing Foundry Agent capabilities remain available and are now enhanced with seamless voice support. Developers should review the updated documentation for integration guidelines and best practices. No additional infrastructure is required for audio pipeline management.

**Details**:

**Comprehensive Technical Explanation of "Generally Available: Voice Live integration with Microsoft Foundry Agent Service"**

**Background and Purpose of the Update**  
The Microsoft Foundry Agent Service is now generally available with Voice Live integration. The primary purpose of this update is to simplify and accelerate the process for developers to connect real-time speech-to-text (STT) and text-to-speech (TTS) capabilities to a Foundry Agent. Previously, developers needed to implement their own custom audio pipelines to enable voice interactions with agents. This update eliminates that requirement, streamlining the integration of voice features into agent-based solutions.

**Specific Features and Detailed Changes**  
- **Voice Live Integration:** Developers can now directly connect real-time STT and TTS functionalities to a Foundry Agent through Voice Live, without manual audio pipeline development.
- **Agent Capability Extension:** The update leverages existing agent capabilities, allowing them to process and respond to voice input/output natively.
- **General Availability:** The feature has moved from preview or limited access to full production support, ensuring stability and support for enterprise workloads.

**Technical Mechanisms and Implementation Methods**  
- **Real-Time Audio Processing:** The integration provides a managed pathway for streaming audio data to and from the Foundry Agent, handling both the conversion of spoken language to text (STT) and the synthesis of agent responses back to speech (TTS).
- **Abstraction of Audio Pipeline:** By abstracting the audio pipeline, developers interact with higher-level APIs or service endpoints, bypassing the need to manage low-level audio encoding, streaming, or synchronization.
- **Service-Oriented Architecture:** The Foundry Agent Service acts as the central orchestrator, interfacing with Voice Live for audio processing and managing agent logic for conversation handling.

**Use Cases and Application Scenarios**  
- **Conversational AI Applications:** Rapidly enable voice-driven bots or virtual assistants in customer support, helpdesk, or information retrieval scenarios.
- **Accessibility Solutions:** Integrate voice interaction for accessibility features in applications, reducing development effort.
- **IoT and Edge Devices:** Deploy voice-enabled agents on devices where implementing custom audio pipelines is impractical or resource-intensive.
- **Enterprise Workflow Automation:** Use voice commands to interact with business process automation agents, improving hands-free operation.

**Important Considerations and Limitations**  
- **Scope of Integration:** The update specifically addresses the connection between Voice Live and Foundry Agent Service for real-time STT and TTS. It does not extend to custom audio processing or third-party speech services.
- **Agent Capability Dependency:** The effectiveness of voice integration depends on the underlying capabilities of the Foundry Agent; complex conversational logic or domain-specific models may require additional configuration.
- **Service Availability:** As the feature is generally available, it is covered by standard Azure support and SLAs, but users should review regional availability and compliance requirements.

**Integration with Related Azure Services**  
- **Azure Cognitive Services:** While not explicitly mentioned, Voice Live integration typically leverages Azure’s speech services for STT and TTS, ensuring compatibility with other Azure AI offerings.
- **Azure Bot Service:** The Foundry Agent Service can complement Azure Bot Service deployments, providing a seamless voice interface for bots.
- **Azure Monitoring and Logging:** Standard Azure monitoring tools can be used to track agent performance, voice interaction metrics, and troubleshoot integration issues.

**Summary**  
The general availability of Voice Live integration with Microsoft Foundry Agent Service enables developers to add real-time speech-to-text and text-to-speech capabilities to agents without building custom audio pipelines, streamlining the development of voice-enabled applications and enhancing agent functionality.

---

### 15. Generally Available: Azure Sphere OS version 26.06 is now available

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: Azure Sphere OS version 26.06 is now available](https://azure.microsoft.com/updates?id=565033)

**Update ID**: 565033
**Data source**: Azure Updates API

**Categories**: Launched, Internet of Things, Azure Sphere, Operating System

**Summary**:

- What was updated  
Azure Sphere OS version 26.06 is now generally available in the Retail feed.

- Key changes or new features  
This release provides updates to the Azure Sphere OS only; there is no new SDK included. The update is delivered automatically to internet-connected devices via the cloud. Specific details about OS improvements or security patches are not provided in the announcement.

- Target audience affected  
Developers and IT professionals managing Azure Sphere devices, especially those responsible for device fleet management, security, and OS compliance.

- Important notes if any  
No SDK update is included with this release—developers do not need to update their development environment. Devices connected to the internet will receive the OS update automatically; no manual intervention is required. For environments with controlled update policies, review and test the new OS version as needed. For more details or release notes, refer to the official Azure update link.

**Details**:

**Azure Sphere OS version 26.06 is now generally available in the Retail feed, providing the latest operating system updates for Azure Sphere devices.**

**Background and Purpose of the Update:**  
The release of Azure Sphere OS version 26.06 is part of Microsoft’s ongoing commitment to enhance the security, reliability, and performance of Azure Sphere, a comprehensive platform for securing IoT devices. The primary purpose of this update is to deliver improvements and patches to the Azure Sphere OS, ensuring that connected devices remain up-to-date with the latest system enhancements. Notably, this release is an OS-only update and does not include a new version of the Azure Sphere SDK.

**Specific Features and Detailed Changes:**  
This update introduces changes exclusively to the Azure Sphere OS. While the detailed changelog is not provided in the announcement, such OS updates typically address security vulnerabilities, improve system stability, and may optimize device performance. No SDK updates are included, so development workflows and tooling remain unchanged.

**Technical Mechanisms and Implementation Methods:**  
Azure Sphere devices are designed to receive OS updates automatically from the cloud when connected to the internet. The update is distributed via the Retail feed, which is the default update channel for production devices. The update process is managed by the Azure Sphere security service, which ensures that devices are running the latest approved OS version. No manual intervention is required for devices configured for automatic updates, streamlining fleet management and reducing operational overhead.

**Use Cases and Application Scenarios:**  
This update is relevant for organizations deploying Azure Sphere-powered IoT solutions in production environments. Typical scenarios include connected appliances, industrial controllers, and other embedded systems where security and reliability are paramount. By ensuring devices receive timely OS updates, organizations can maintain compliance with security best practices and reduce exposure to vulnerabilities.

**Important Considerations and Limitations:**  
- This release does not include an updated SDK; development tools and APIs remain as in the previous version.
- Devices must be connected to the internet to receive the update automatically from the Retail feed.
- Organizations should verify that their device update policies and network configurations allow for seamless OS updates.
- There may be a brief window during which devices reboot or restart services as part of the update process, which should be considered in high-availability scenarios.

**Integration with Related Azure Services:**  
Azure Sphere OS integrates closely with the Azure Sphere Security Service, which orchestrates secure OS updates and device authentication. The update process leverages Azure’s cloud infrastructure to deliver updates at scale, ensuring consistent security posture across all managed devices. Azure Sphere devices can also interact with other Azure IoT services, such as Azure IoT Hub, for device management and telemetry, but this update does not alter those integrations.

**Summary:**  
Azure Sphere OS version 26.06 is now generally available in the Retail feed, providing the latest OS updates for connected devices without requiring changes to the SDK or development workflows.

---

### 16. Public Preview: Automatic OS Image Upgrades for VMSS Flex

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Public Preview: Automatic OS Image Upgrades for VMSS Flex](https://azure.microsoft.com/updates?id=564976)

**Update ID**: 564976
**Data source**: Azure Updates API

**Categories**: In preview, Features, Microsoft Build

**Summary**:

- What was updated  
Automatic OS Image Upgrades are now available in public preview for Virtual Machine Scale Sets (VMSS) using Flexible Orchestration (VMSS Flex).

- Key changes or new features  
This update introduces automated OS image upgrades for VMSS Flex, allowing VM instances to automatically receive the latest OS images without manual intervention. The feature ensures consistent and up-to-date OS versions across all instances in a scale set, reducing operational overhead and the risk of unpatched vulnerabilities. Previously, this automation was only available for VMSS Uniform orchestration mode.

- Target audience affected  
Azure developers, DevOps engineers, and IT professionals managing infrastructure with VMSS Flex.

- Important notes if any  
- The feature is currently in public preview and may not be suitable for production workloads.  
- Automated image upgrades help maintain compliance and security by streamlining OS patching processes.  
- Review and test the upgrade process in non-production environments before enabling in production.  
- For more details and to get started, refer to the official documentation: https://azure.microsoft.com/updates?id=564976

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Automatic OS Image Upgrades for VMSS Flex

**Background and Purpose of the Update:**  
Azure Virtual Machine Scale Sets (VMSS) are widely used to deploy and manage large sets of identical, load-balanced VMs. Traditionally, keeping the operating system (OS) images up to date across all instances in a scale set required significant manual intervention, especially when using the Flexible Orchestration mode (VMSS Flex), which offers greater deployment flexibility. The purpose of this update is to introduce automatic OS image upgrades for VMSS Flex, reducing operational overhead and ensuring consistent, up-to-date OS versions across all VMs in the scale set.

**Specific Features and Detailed Changes:**  
- **Automatic OS Image Upgrades:** VMSS Flex now supports automated, fleet-wide OS image updates. This feature, previously available for VMSS Uniform orchestration, is now extended to VMSS Flex.
- **Consistent Updates:** The update process ensures that all VM instances within a scale set are running the latest OS image, promoting security and compliance.
- **Reduced Manual Effort:** Administrators no longer need to manually coordinate and apply OS image updates for each VM in a flexible scale set.

**Technical Mechanisms and Implementation Methods:**  
- **Orchestration Mode:** The feature is available specifically for VMSS configured with Flexible Orchestration. This mode allows for a mix of VM sizes and configurations within the same scale set.
- **Image Management:** When enabled, the automatic OS image upgrade mechanism detects new versions of the base OS image and orchestrates the rolling upgrade of VM instances within the scale set.
- **Upgrade Process:** The upgrade process is managed by Azure, which handles the scheduling and sequencing of VM updates to minimize service disruption and maintain availability.

**Use Cases and Application Scenarios:**  
- **Large-Scale Deployments:** Organizations managing large fleets of VMs with varying configurations can benefit from consistent and automated OS patching.
- **Security and Compliance:** Environments with strict compliance requirements can ensure all VMs are running the latest, supported OS images.
- **DevOps and CI/CD Pipelines:** Automated OS image upgrades can be integrated into deployment pipelines, reducing the need for manual intervention and potential human error.

**Important Considerations and Limitations:**  
- **Public Preview:** This feature is currently in public preview, which means it is not recommended for production workloads until it reaches General Availability (GA).
- **VMSS Flex Only:** The feature applies to VMSS using Flexible Orchestration; it does not impact VMSS Uniform, which already supports automatic OS image upgrades.
- **Service Disruption:** While Azure manages the upgrade process to minimize impact, there may still be brief disruptions as VMs are updated and restarted.
- **Configuration Requirements:** Administrators must ensure that their VMSS Flex configurations are compatible with the automatic upgrade process.

**Integration with Related Azure Services:**  
- **Azure Compute:** This feature is part of the broader Azure Compute platform, enhancing VMSS Flex capabilities.
- **Azure Monitoring and Management:** Administrators can use Azure Monitor and related tools to track upgrade progress and VM health during the upgrade process.
- **Azure Policy and Security Center:** Integration with these services can help enforce compliance and monitor security posture during OS image upgrades.

**Summary:**  
Automatic OS Image Upgrades for VMSS Flex, now in public preview, enable consistent and automated OS updates across flexible scale sets, reducing manual management and improving security and compliance for large-scale Azure deployments.

---

### 17. Generally Available: OpenTelemetry Metrics, Visualizations, and Enhanced Monitoring in Azure Monitor for Azure VMs and Arc Servers

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: OpenTelemetry Metrics, Visualizations, and Enhanced Monitoring in Azure Monitor for Azure VMs and Arc Servers](https://azure.microsoft.com/updates?id=564802)

**Update ID**: 564802
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Monitor now offers generally available support for OpenTelemetry metrics, visualizations, and enhanced monitoring for Azure Virtual Machines (VMs) and Arc Servers.

- Key changes or new features  
  - Native integration of OpenTelemetry metrics, enabling standardized metric collection and export from Azure VMs and Arc Servers.  
  - Unified monitoring experience: Metrics, logs, and visualizations are consolidated within Azure Monitor, simplifying troubleshooting and performance analysis.  
  - Enhanced visualizations: Improved dashboards and charts for real-time and historical metric analysis.  
  - Support for both Azure-native and hybrid (Arc-enabled) environments, providing consistent monitoring across cloud and on-premises resources.

- Target audience affected  
  - Developers building or maintaining applications on Azure VMs or Arc Servers who require standardized observability and telemetry.  
  - IT professionals and operations teams responsible for infrastructure monitoring, troubleshooting, and performance optimization in Azure or hybrid environments.

- Important notes if any  
  - OpenTelemetry is an open-source observability framework, allowing for vendor-neutral metric collection and export.  
  - Existing monitoring configurations may need updates to leverage new OpenTelemetry-based features.  
  - This update streamlines monitoring workflows, reducing the need for multiple tools or custom integrations.  
  - More details and onboarding instructions are available in the official Azure documentation.

**Details**:

**Comprehensive Technical Explanation of the Azure Update: OpenTelemetry Metrics, Visualizations, and Enhanced Monitoring in Azure Monitor for Azure VMs and Arc Servers**

**Background and Purpose of the Update**  
This update marks the general availability of OpenTelemetry metrics and visualizations within Azure Monitor, specifically targeting Azure Virtual Machines (VMs) and Azure Arc-enabled servers. The primary purpose is to deliver an enhanced and unified monitoring experience by consolidating critical monitoring capabilities into a single, streamlined interface. This addresses the need for standardized observability and improved operational insights across both native Azure and hybrid environments.

**Specific Features and Detailed Changes**  
- **OpenTelemetry Metrics Support:** Azure Monitor now natively supports OpenTelemetry metrics, enabling collection, storage, and analysis of telemetry data from Azure VMs and Arc Servers.
- **Unified Visualizations:** Enhanced visualizations allow users to view and analyze OpenTelemetry metrics alongside other monitoring data within Azure Monitor’s dashboards.
- **Consolidated Monitoring Experience:** Key monitoring functionalities are now accessible through a single experience, reducing the need to switch between multiple tools or interfaces.
- **General Availability:** These features are now fully supported and ready for production workloads.

**Technical Mechanisms and Implementation Methods**  
- **Data Collection:** OpenTelemetry agents or SDKs are deployed on Azure VMs and Arc Servers to collect metrics. These agents adhere to the OpenTelemetry specification, ensuring consistent data formats and interoperability.
- **Data Ingestion:** Collected metrics are ingested into Azure Monitor using standardized APIs and protocols supported by OpenTelemetry.
- **Visualization Layer:** Azure Monitor’s visualization engine has been enhanced to natively interpret and render OpenTelemetry metrics, allowing users to create custom charts, dashboards, and alerts based on this data.
- **Integration with Azure Monitor:** The update ensures that OpenTelemetry data is first-class within Azure Monitor, benefiting from the platform’s scalability, security, and analytics capabilities.

**Use Cases and Application Scenarios**  
- **Hybrid Monitoring:** Organizations running workloads on both Azure and on-premises or multi-cloud environments (via Arc Servers) can now standardize monitoring using OpenTelemetry.
- **Application Performance Monitoring:** Developers and IT operators can collect, visualize, and analyze application and infrastructure metrics in real time, facilitating root cause analysis and performance optimization.
- **Compliance and Reporting:** Unified metrics collection supports compliance reporting and operational audits by providing consistent, centralized telemetry data.

**Important Considerations and Limitations**  
- **Scope:** The general availability applies specifically to Azure VMs and Arc Servers. Other Azure resources or services may not yet be covered by this update.
- **Agent Deployment:** Proper deployment and configuration of OpenTelemetry agents are required to leverage these features.
- **Data Compatibility:** Only metrics conforming to the OpenTelemetry specification are supported; custom or legacy telemetry formats may require transformation.
- **Platform Dependencies:** Full functionality depends on the latest versions of Azure Monitor and OpenTelemetry agents.

**Integration with Related Azure Services**  
- **Azure Arc:** Extends monitoring capabilities to non-Azure environments, enabling consistent observability across hybrid and multi-cloud infrastructures.
- **Azure Monitor Dashboards:** OpenTelemetry metrics are fully integrated into Azure Monitor dashboards, supporting advanced visualization and alerting scenarios.
- **Other Azure Services:** While this update focuses on VMs and Arc Servers, the unified monitoring experience can complement other Azure observability tools and services.

**Summary Sentence**  
OpenTelemetry metrics and visualizations are now generally available in Azure Monitor for Azure VMs and Arc Servers, providing a unified, enhanced monitoring experience through consolidated data collection, advanced visualizations, and seamless integration with Azure’s observability platform.

---

### 18. Public preview: Azure Linux 4.0 for Azure Virtual Machines and VM Scale Sets

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Public preview: Azure Linux 4.0 for Azure Virtual Machines and VM Scale Sets](https://azure.microsoft.com/updates?id=564543)

**Update ID**: 564543
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Linux Virtual Machines, Azure Linux, Microsoft Build, Open Source, Services

**Summary**:

- What was updated  
Azure Linux 4.0, Microsoft’s in-house Linux distribution optimized for Azure, is now available in public preview for Azure Virtual Machines (VMs) and Virtual Machine Scale Sets (VMSS).

- Key changes or new features  
  - Updated to Linux kernel 6.18 LTS, providing enhanced performance, security, and hardware support.  
  - Introduction of the dnf5 package manager for improved package management efficiency and speed.  
  - Modernized system stack, including updated core libraries and tools.  
  - Designed for seamless integration and optimized performance on Azure infrastructure.

- Target audience affected  
  - Developers deploying Linux workloads on Azure VMs or VM Scale Sets.  
  - IT professionals managing Azure-based Linux environments, especially those seeking a Microsoft-supported Linux OS.

- Important notes if any  
  - Azure Linux 4.0 is currently in public preview; not recommended for production workloads yet.  
  - Existing Azure Linux users should review migration and compatibility considerations before upgrading.  
  - This release aims to provide a secure, consistent, and fully supported Linux experience tailored for Azure cloud environments.

For more details, visit the official update: https://azure.microsoft.com/updates?id=564543

**Details**:

**Azure Update Technical Report**

**Title:** Public preview: Azure Linux 4.0 for Azure Virtual Machines and VM Scale Sets  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=564543)

---

### Background and Purpose of the Update

Azure Linux 4.0 marks a significant milestone as Microsoft’s first-party Linux distribution, purpose-built specifically for the Azure platform. The release of Azure Linux 4.0 in public preview aims to provide Azure customers with a modern, secure, and optimized Linux environment for running workloads on Azure Virtual Machines (VMs) and Virtual Machine Scale Sets (VMSS). This update reflects Microsoft’s commitment to delivering a tightly integrated and performance-optimized Linux experience for cloud-native applications and infrastructure.

---

### Specific Features and Detailed Changes

Azure Linux 4.0 introduces several notable enhancements:

- **Linux Kernel 6.18 LTS:** The distribution is based on the Long-Term Support (LTS) version 6.18 of the Linux kernel, offering improved hardware compatibility, enhanced security features, and better performance.
- **dnf5 Package Manager:** Azure Linux 4.0 adopts `dnf5` as its package manager, providing faster, more efficient package management and dependency resolution compared to previous versions.
- **Modernized Stack:** The distribution includes a refreshed set of core utilities and libraries, ensuring compatibility with modern workloads and developer tools.
- **Purpose-Built for Azure:** The OS is optimized for Azure infrastructure, ensuring seamless integration with Azure’s management, monitoring, and security services.

---

### Technical Mechanisms and Implementation Methods

Azure Linux 4.0 is delivered as a first-party image in the Azure Marketplace, available for deployment on both Azure Virtual Machines and Virtual Machine Scale Sets. The distribution leverages the latest LTS kernel and integrates the `dnf5` package manager for streamlined system updates and package installations. The image is maintained and updated by Microsoft, ensuring timely security patches and compatibility updates tailored to Azure’s environment.

Deployment is performed through standard Azure provisioning workflows, using the Azure Portal, Azure CLI, ARM templates, or Bicep. The image is designed to work seamlessly with Azure’s VM extensions, diagnostics, and monitoring agents.

---

### Use Cases and Application Scenarios

Azure Linux 4.0 is suitable for a wide range of scenarios, including:

- **Cloud-Native Application Hosting:** Ideal for running containerized workloads, microservices, and modern application stacks.
- **Dev/Test Environments:** Provides a consistent and up-to-date Linux environment for development and testing.
- **Production Workloads:** Suitable for enterprise-grade applications requiring long-term support, security, and performance.
- **Scale-Out Deployments:** Optimized for use with VM Scale Sets, supporting auto-scaling and high-availability architectures.

---

### Important Considerations and Limitations

- **Public Preview:** Azure Linux 4.0 is currently in public preview, which may imply limited support and potential changes before general availability.
- **Compatibility:** While the stack is modernized, users should verify application compatibility, especially with the new kernel and package manager.
- **Support Lifecycle:** As a preview release, production workloads should be evaluated carefully, and users should monitor Microsoft’s guidance for updates and support policies.

---

### Integration with Related Azure Services

Azure Linux 4.0 is engineered for deep integration with Azure services, including:

- **Azure Monitor and Azure Security Center:** Out-of-the-box compatibility for monitoring and security management.
- **Azure VM Extensions:** Full support for extensions such as diagnostics, custom scripts, and configuration management.
- **Azure Marketplace:** Easy deployment and scaling through the Marketplace interface and automation tools.

---

**Summary:**  
Azure Linux 4.0, now in public preview, delivers a modern, Azure-optimized Linux distribution featuring kernel 6.18 LTS and the dnf5 package manager, available for Azure Virtual Machines and VM Scale Sets to enhance performance, security,

---

### 19. Azure Container Linux (ACL) now generally available on Azure Kubernetes Service (AKS)

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Azure Container Linux (ACL) now generally available on Azure Kubernetes Service (AKS)](https://azure.microsoft.com/updates?id=564537)

**Update ID**: 564537
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Linux Virtual Machines, Azure Linux, Microsoft Build, Open Source, Services

**Summary**:

- What was updated  
Azure Container Linux (ACL) is now generally available as a supported operating system for node pools in Azure Kubernetes Service (AKS).

- Key changes or new features  
  - ACL is a container-optimized, immutable OS derived from Flatcar Container Linux, built on Azure Linux RPM packages.  
  - Provides a minimal, locked-down host environment specifically designed for running containerized workloads securely and efficiently.  
  - Integrates seamlessly with AKS, supporting modern Kubernetes features and Azure security/compliance standards.  
  - Delivers automatic updates, improved security posture, and reduced attack surface compared to general-purpose OS options.

- Target audience affected  
  - Kubernetes platform engineers and cluster operators managing AKS node pools.  
  - Developers deploying containerized applications on AKS who require a secure, minimal host OS.  
  - IT professionals responsible for security, compliance, and OS lifecycle management in AKS environments.

- Important notes  
  - ACL is recommended for production workloads that prioritize security, immutability, and minimal OS footprint.  
  - Existing AKS clusters can add ACL-based node pools; migration from other OS types may require workload validation.  
  - ACL is fully supported by Azure, with ongoing updates and integration into Azure’s managed Kubernetes platform.

[More details](https://azure.microsoft.com/updates?id=564537)

**Details**:

**Azure Update Report: Azure Container Linux (ACL) now generally available on Azure Kubernetes Service (AKS)**

**Background and Purpose of the Update**  
Azure Container Linux (ACL) is now generally available as an operating system option for node pools in Azure Kubernetes Service (AKS). ACL is a container-optimized, immutable operating system derived from Flatcar Container Linux and built on Azure Linux RPM packages. The primary purpose of this update is to provide a minimal, locked-down host OS specifically designed for running containerized workloads in AKS environments. This addresses the need for a secure, lightweight, and maintainable OS platform for container orchestration in Azure.

**Specific Features and Detailed Changes**  
- **Container-Optimized OS**: ACL is tailored for container workloads, minimizing unnecessary packages and services to reduce the attack surface.
- **Immutable Infrastructure**: The OS is designed to be immutable, meaning system files and configurations are not changed during operation, improving consistency and reliability.
- **Flatcar Lineage**: ACL inherits features from Flatcar Container Linux, such as automatic updates and a read-only root filesystem, while integrating Azure Linux RPM packages for enhanced compatibility and support within Azure.
- **General Availability in AKS**: ACL can now be selected as the host OS for AKS node pools, making it a supported and production-ready option for customers.

**Technical Mechanisms and Implementation Methods**  
- **Node Pool Integration**: When creating or updating AKS clusters, users can specify ACL as the node pool OS. This ensures that all VMs in the node pool are provisioned with ACL images.
- **Security and Updates**: The immutable design and automatic update mechanisms inherited from Flatcar help maintain security and reduce configuration drift. Updates are delivered as atomic operations, minimizing downtime and risk.
- **Azure Linux RPM Packages**: By building on Azure Linux RPMs, ACL ensures compatibility with Azure’s management and monitoring tools, and aligns with Azure’s support lifecycle.

**Use Cases and Application Scenarios**  
- **Production-Grade Container Hosting**: Organizations running critical containerized applications on AKS can leverage ACL for enhanced security and operational consistency.
- **Immutable Infrastructure Deployments**: Teams adopting immutable infrastructure patterns benefit from ACL’s read-only root filesystem and atomic updates.
- **Regulated Environments**: Environments requiring minimal OS footprints and hardened security postures, such as finance or healthcare, can utilize ACL to meet compliance requirements.

**Important Considerations and Limitations**  
- **Supported Only on AKS Node Pools**: ACL is currently available only as the OS for AKS node pools and is not intended for general-purpose VM workloads.
- **Immutable Design**: Customizations to the base OS are limited due to its immutable nature. Application-specific dependencies should be included in container images rather than modifying the host OS.
- **Update Mechanisms**: Automatic updates may require coordination with maintenance windows to avoid disruptions in production environments.

**Integration with Related Azure Services**  
- **AKS Integration**: ACL is tightly integrated with AKS, supporting Azure-native cluster management, scaling, and monitoring.
- **Azure Linux Ecosystem**: By building on Azure Linux RPM packages, ACL aligns with Azure’s broader Linux strategy, ensuring compatibility with Azure Monitor, Azure Policy, and other platform services.

**Summary**  
Azure Container Linux (ACL) is now generally available as a secure, container-optimized, and immutable operating system for AKS node pools, offering a minimal and locked-down host derived from Flatcar and Azure Linux RPM packages, purpose-built for running containerized workloads in production environments.

---

### 20. Generally Available: Azure Event Grid - MQTT v5 Subscription Identifier

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: Azure Event Grid - MQTT v5 Subscription Identifier](https://azure.microsoft.com/updates?id=564532)

**Update ID**: 564532
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Event Grid, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Event Grid Standard Namespace now supports MQTT v5 subscription identifiers, and this feature is generally available (GA).

- Key changes or new features  
Developers can now assign a unique subscription identifier to each MQTT v5 subscription. This identifier is delivered with every incoming message, allowing applications to immediately recognize which subscription the message relates to. This enables more efficient event routing and processing logic within client applications, especially in scenarios with multiple subscriptions.

- Target audience affected  
This update is relevant for developers and IT professionals building solutions that use Azure Event Grid with MQTT v5, particularly those managing multiple MQTT subscriptions or requiring granular event handling.

- Important notes if any  
The subscription identifier feature is available only in the Standard tier of Azure Event Grid Namespace. Applications must use MQTT v5 protocol to leverage this capability. This enhancement simplifies message handling and routing, reducing the need for custom logic to track subscriptions on the client side.

For more details, see the official update: https://azure.microsoft.com/updates?id=564532

**Details**:

**Azure Event Grid – MQTT v5 Subscription Identifier Now Generally Available**

**Background and Purpose of the Update**  
Azure Event Grid is a fully managed event routing service that supports multiple protocols for event-driven architectures. MQTT (Message Queuing Telemetry Transport) is a lightweight messaging protocol commonly used in IoT and distributed systems. With the increasing adoption of MQTT v5, advanced features such as subscription identifiers are essential for efficient event management and routing. This update introduces General Availability (GA) support for MQTT v5 subscription identifiers in Azure Event Grid Standard Namespace, enabling more granular event handling and routing capabilities.

**Specific Features and Detailed Changes**  
The update brings GA support for the MQTT v5 subscription identifier feature within the Azure Event Grid Standard Namespace. Now, each MQTT subscription can include a unique identifier. This identifier is attached to incoming messages and delivered to the subscriber application. The main change is the ability for applications to distinguish between multiple subscriptions by using these identifiers, which are now natively supported in Event Grid.

**Technical Mechanisms and Implementation Methods**  
In MQTT v5, the subscription identifier is an integer value assigned by the client when creating a subscription. Azure Event Grid now preserves and propagates this identifier with each published message that matches the subscription. When a message is delivered to the subscriber, the subscription identifier is included in the MQTT packet, allowing the client application to immediately determine which subscription the message corresponds to. This mechanism leverages the MQTT v5 protocol extension and is seamlessly integrated into the Event Grid’s message processing pipeline.

**Use Cases and Application Scenarios**  
- **IoT Solutions:** Devices or gateways subscribing to multiple topics can use subscription identifiers to efficiently route incoming events to the appropriate processing logic.
- **Event-Driven Microservices:** Applications managing multiple event streams can quickly identify the source subscription for each event, enabling dynamic routing and processing.
- **Multi-Tenant Architectures:** Solutions supporting multiple tenants or customers can assign subscription identifiers to segregate and manage event flows per tenant.
- **Complex Event Processing:** Systems that require differentiated handling based on the subscription context can use identifiers to trigger specific workflows or business rules.

**Important Considerations and Limitations**  
- The feature is available only in the Azure Event Grid Standard Namespace and requires MQTT v5 protocol support.
- Subscription identifiers must be managed by the client application; uniqueness and assignment logic are the responsibility of the subscriber.
- There may be limits on the number of simultaneous subscriptions or identifiers, subject to the Event Grid Standard Namespace quotas.
- Backward compatibility with MQTT v3.x clients is not provided for this feature.

**Integration with Related Azure Services**  
The MQTT v5 subscription identifier support enhances integration with other Azure services that rely on Event Grid for event distribution, such as Azure IoT Hub, Azure Functions, and Logic Apps. Applications can now implement more sophisticated event routing and processing logic by leveraging subscription identifiers, improving interoperability and efficiency in event-driven solutions.

**Summary**  
Azure Event Grid Standard Namespace now supports MQTT v5 subscription identifiers in General Availability, enabling applications to receive and route events based on unique subscription identifiers included with incoming messages.

---

### 21. Private Preview: multiparty analytics with Azure Confidential Clean Rooms

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Private Preview: multiparty analytics with Azure Confidential Clean Rooms](https://azure.microsoft.com/updates?id=564495)

**Update ID**: 564495
**Data source**: Azure Updates API

**Categories**: In development, Microsoft Build

**Summary**:

- What was updated  
Microsoft announced the private preview of multiparty analytics in Azure Confidential Clean Rooms, a fully managed service for secure, collaborative analytics on sensitive data.

- Key changes or new features  
  - Enables multiple organizations to jointly analyze privacy-sensitive datasets without exposing raw data to each other.  
  - Built on Apache Spark, supporting big data analytics workloads.  
  - Leverages Azure Confidential Computing and hardware-based trusted execution environments to ensure data privacy and security during processing.  
  - Provides policy-based controls and auditing for data access and usage.

- Target audience affected  
  - Data engineers, data scientists, and developers working with sensitive or regulated data.  
  - IT professionals responsible for data governance, compliance, and security in collaborative analytics scenarios.  
  - Organizations needing to collaborate with partners on data analytics while maintaining strict privacy controls.

- Important notes if any  
  - Currently available in private preview; interested customers must apply for access.  
  - Designed for scenarios such as joint marketing analytics, fraud detection, or healthcare research where data privacy is critical.  
  - Integration with Apache Spark allows use of familiar analytics tools and workflows.  
  - Helps organizations meet compliance requirements (e.g., GDPR, HIPAA) when sharing and analyzing sensitive data.

**Details**:

**Azure Update Report: Private Preview – Multiparty Analytics with Azure Confidential Clean Rooms**

**Background and Purpose of the Update:**  
Microsoft has announced the private preview of multiparty analytics with Azure Confidential Clean Rooms. This update addresses the growing need for organizations to collaboratively analyze privacy-sensitive datasets without compromising data confidentiality. The primary purpose is to enable secure, privacy-preserving analytics between customers and their partners, particularly in scenarios where data sharing is restricted by regulatory or contractual obligations.

**Specific Features and Detailed Changes:**  
The update introduces a fully managed service that leverages Azure Confidential Clean Rooms for multiparty analytics. The service is built on Apache Spark, a widely adopted big-data analytics engine, allowing users to perform scalable analytics on combined datasets from multiple parties. Key features include:
- Secure collaboration between multiple organizations on sensitive datasets.
- Fully managed infrastructure, reducing operational overhead for setup and maintenance.
- Native integration with Apache Spark, supporting complex analytics and data processing workflows.

**Technical Mechanisms and Implementation Methods:**  
Azure Confidential Clean Rooms utilize confidential computing technologies to ensure data privacy during processing. Data from each party remains protected and is only accessible within the secure enclave of the clean room. The service orchestrates the ingestion and processing of data using Apache Spark clusters, which are provisioned and managed by Azure. All computations occur within the clean room environment, preventing unauthorized access to raw data. The managed nature of the service abstracts away the complexities of cluster management, security configuration, and compliance enforcement.

**Use Cases and Application Scenarios:**  
Typical scenarios for this service include:
- Joint analytics between business partners in regulated industries (e.g., healthcare, finance) where data privacy is paramount.
- Collaborative research involving sensitive datasets from multiple institutions.
- Marketing and advertising analytics where customer data from different sources must be combined without direct data sharing.
- Supply chain optimization and risk analysis involving confidential partner data.

**Important Considerations and Limitations:**  
As this is a private preview, access is limited and subject to Microsoft’s preview terms. Organizations should evaluate the service’s compliance with their internal policies and regulatory requirements. Performance and feature completeness may differ from the eventual general availability release. Integration with existing data pipelines and security controls should be carefully planned. Users should also be aware of any data residency or sovereignty requirements that may impact usage.

**Integration with Related Azure Services:**  
Azure Confidential Clean Rooms are designed to work seamlessly with other Azure data and security services. The managed Apache Spark environment can integrate with Azure Data Lake Storage for data input and output. Security and access controls can be managed through Azure Active Directory. The service may also complement Azure Purview for data governance and compliance tracking, and Azure Key Vault for managing encryption keys.

**Summary Sentence:**  
Microsoft’s private preview of multiparty analytics with Azure Confidential Clean Rooms introduces a fully managed, Apache Spark-based service that enables secure, privacy-preserving analysis of sensitive datasets across organizational boundaries, leveraging confidential computing to ensure data protection throughout the analytics workflow.

---

### 22. Private Preview: Storage optimized Lasv5 and Laosv5 Azure VM series

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Private Preview: Storage optimized Lasv5 and Laosv5 Azure VM series](https://azure.microsoft.com/updates?id=564446)

**Update ID**: 564446
**Data source**: Azure Updates API

**Categories**: In development, Compute, Virtual Machines, Microsoft Build

**Summary**:

- What was updated  
Azure announced the private preview of the Lasv5 and Laosv5 storage-optimized Virtual Machine (VM) series, powered by 5th Gen AMD EPYC™ (Turin) processors.

- Key changes or new features  
  - Introduction of Lasv5-series VMs, optimized for storage-intensive workloads, offering high disk capacity, throughput, and IOPS.  
  - Introduction of Laosv5-series VMs, also storage-optimized, with configurations tailored for workloads requiring both high storage performance and compute efficiency.  
  - Both series leverage the latest AMD EPYC™ (Turin) processors, providing improved performance and efficiency compared to previous generations.

- Target audience affected  
Developers and IT professionals running storage-intensive applications, such as large databases, big data analytics, data warehousing, and high-performance transactional systems on Azure.

- Important notes if any  
  - These VM series are currently in private preview; access may require registration or approval.  
  - Ideal for scenarios demanding high disk throughput and IOPS.  
  - Evaluate compatibility and migration paths if planning to leverage these new VM types for existing workloads.  
  - Stay updated on general availability for broader deployment options.

Link: https://azure.microsoft.com/updates?id=564446

**Details**:

**Azure Update Technical Explanation: Private Preview: Storage optimized Lasv5 and Laosv5 Azure VM series**

**Background and Purpose of the Update**  
This update introduces the Lasv5 and Laosv5 series of storage-optimized Azure Virtual Machines (VMs) into private preview. These VM series are built on the 5th Generation AMD EPYC™ processor (codenamed Turin). The primary purpose of this release is to address the growing demand for high-performance, storage-intensive workloads on Azure by providing VMs specifically engineered for high disk capacity, throughput, and I/O operations.

**Specific Features and Detailed Changes**  
- **Lasv5-series**: Designed for storage-intensive workloads, these VMs offer high disk capacity, increased throughput, and enhanced I/O performance.  
- **Laosv5-series**: Also based on the 5th Gen AMD EPYC™ processor, this series is optimized for similar storage-focused scenarios, with specific tuning for throughput and IOPS requirements.  
- **Processor**: Both series leverage the latest AMD EPYC™ (Turin) CPUs, providing improved performance and efficiency compared to previous generations.

**Technical Mechanisms and Implementation Methods**  
- **Hardware Platform**: The Lasv5 and Laosv5 VMs utilize the 5th Gen AMD EPYC™ architecture, which is known for its high core counts, advanced memory bandwidth, and optimized I/O capabilities.
- **Storage Optimization**: These VMs are configured to maximize disk throughput and IOPS, making them suitable for scenarios where storage performance is a bottleneck.
- **Preview Availability**: As these VM series are in private preview, access is limited and intended for early evaluation and feedback from selected customers.

**Use Cases and Application Scenarios**  
- **High-Performance Databases**: Ideal for running large-scale SQL, NoSQL, or analytics databases that require sustained high disk throughput and IOPS.
- **Big Data Analytics**: Suitable for workloads such as Hadoop, Spark, or other data processing frameworks where disk performance is critical.
- **Backup and Archival Solutions**: Useful for applications that need to process or move large volumes of data efficiently.
- **Log Processing and Data Warehousing**: Well-suited for environments with continuous high-volume data ingestion and transformation.

**Important Considerations and Limitations**  
- **Preview Status**: As these VM series are in private preview, they may not be available in all regions, and features are subject to change based on customer feedback and further development.
- **Access**: Participation in the preview may require registration or approval from Microsoft.
- **Production Readiness**: These VMs should not be used for production workloads until they reach General Availability (GA) and are fully supported.

**Integration with Related Azure Services**  
- **Azure Managed Disks**: These VMs can be paired with Azure’s premium or ultra disks to fully leverage their storage throughput capabilities.
- **Azure Backup and Site Recovery**: The enhanced disk performance can accelerate backup and disaster recovery operations.
- **Azure Monitor**: Integration with monitoring services is recommended to track disk I/O, throughput, and VM performance metrics.
- **Azure Virtual Network**: These VMs can be deployed within existing virtual networks, enabling secure connectivity to other Azure resources.

**Summary Sentence**  
The Lasv5 and Laosv5 Azure VM series, now in private preview, provide storage-optimized virtual machines based on the 5th Gen AMD EPYC™ processor, designed to deliver high disk capacity, throughput, and I/O for storage-intensive workloads.

---

### 23. Generally Available: Github Copilot modernization

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: Github Copilot modernization](https://azure.microsoft.com/updates?id=564431)

**Update ID**: 564431
**Data source**: Azure Updates API

**Categories**: Launched, Features, Microsoft Build, SDK and Tools

**Summary**:

- What was updated  
The GitHub Copilot modernization agent is now generally available (GA) on Azure.

- Key changes or new features  
The modernization agent enables coordinated orchestration from estate to code, allowing organizations to scale application assessments and upgrades across their entire app portfolio. It leverages GitHub Copilot to automate and streamline modernization tasks, including code analysis, recommendations, and upgrade execution.

- Target audience affected  
This update is relevant for developers, DevOps engineers, and IT professionals responsible for managing, upgrading, and modernizing application portfolios in Azure environments.

- Important notes if any  
The GA release means the modernization agent is production-ready and supported for enterprise use. It provides integration with Azure services and GitHub, supporting large-scale modernization initiatives. Teams can now automate repetitive upgrade tasks, reduce technical debt, and accelerate cloud adoption. For optimal results, ensure your Azure and GitHub environments are properly configured to leverage the agent’s capabilities.

[Read more](https://azure.microsoft.com/updates?id=564431)

**Details**:

**Azure Update Technical Explanation: GitHub Copilot Modernization Agent Generally Available**

**Background and Purpose of the Update:**  
The general availability (GA) of the GitHub Copilot modernization agent marks a significant milestone in automating and scaling application modernization efforts. The primary purpose of this update is to provide IT professionals and developers with an orchestrated solution that streamlines the process of assessing and upgrading applications across an organization’s entire application estate. This addresses the growing need for coordinated modernization as organizations manage increasingly complex portfolios of applications.

**Specific Features and Detailed Changes:**  
- **Coordinated Orchestration:** The modernization agent enables centralized management and orchestration of modernization activities, bridging the gap from infrastructure (estate) to application code.
- **Portfolio-Scale Assessments:** The agent can perform assessments and upgrades at scale, allowing organizations to evaluate and modernize multiple applications simultaneously.
- **General Availability (GA):** The service is now production-ready, with full support from Microsoft and GitHub, ensuring enterprise-grade reliability and support.

**Technical Mechanisms and Implementation Methods:**  
The GitHub Copilot modernization agent operates as an orchestrator, connecting to your application portfolio and automating the assessment and upgrade process. It leverages GitHub Copilot’s AI-powered capabilities to analyze codebases, identify modernization opportunities, and facilitate code changes. The agent can be integrated into existing DevOps pipelines, enabling seamless automation and reducing manual intervention in modernization workflows.

**Use Cases and Application Scenarios:**  
- **Large-Scale Application Modernization:** Enterprises with extensive application portfolios can use the agent to systematically assess and upgrade legacy applications, reducing technical debt and improving maintainability.
- **Continuous Modernization:** Organizations adopting continuous improvement practices can integrate the agent into their CI/CD pipelines to ensure applications remain up-to-date with the latest frameworks and best practices.
- **Cloud Migration Projects:** The agent can assist in preparing applications for migration to Azure by identifying and implementing necessary code changes.

**Important Considerations and Limitations:**  
- **Scope of Automation:** While the agent automates many aspects of assessment and upgrade, manual review and validation of code changes may still be required to ensure alignment with business requirements and compliance standards.
- **Integration Requirements:** Successful deployment may require integration with existing source control and DevOps tools, which should be evaluated for compatibility.
- **Portfolio Coverage:** The effectiveness of the agent depends on the breadth and depth of application portfolio coverage; custom or highly specialized applications may require additional attention.

**Integration with Related Azure Services:**  
The GitHub Copilot modernization agent is designed to complement Azure’s application and DevOps services. It can be integrated with Azure DevOps for end-to-end pipeline automation, and with Azure App Service or Azure Kubernetes Service (AKS) for streamlined deployment of modernized applications. The agent’s orchestration capabilities align with Azure’s focus on scalable, automated cloud operations.

**Summary:**  
The GitHub Copilot modernization agent is now generally available, providing coordinated orchestration for application assessments and upgrades at scale, enabling organizations to modernize their entire application portfolio efficiently.

---

### 24. Generally Available: Rolling updates in Flex Consumption 

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: Rolling updates in Flex Consumption ](https://azure.microsoft.com/updates?id=562365)

**Update ID**: 562365
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features, Microsoft Build

**Summary**:

- What was updated  
Rolling updates are now generally available for the Azure Functions Flex Consumption plan.

- Key changes or new features  
The Flex Consumption plan now supports rolling updates, enabling zero-downtime deployments. Instead of restarting all instances simultaneously during code or configuration changes, the platform updates instances gradually and gracefully. This minimizes service interruptions and reduces the risk of deployment-related outages. Rolling updates can be enabled with a simple configuration change.

- Target audience affected  
Developers and IT professionals managing serverless workloads on Azure Functions using the Flex Consumption plan.

- Important notes if any  
This feature is generally available and recommended for production workloads to ensure high availability during deployments. Existing deployments on Flex Consumption can adopt rolling updates with minimal configuration changes. Review deployment and monitoring practices to take full advantage of zero-downtime updates.  
For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=562365).

**Details**:

**Azure Update Report: Generally Available – Rolling Updates in Flex Consumption**

**Background and Purpose of the Update**  
The Flex Consumption plan is a scalable hosting option for Azure Functions, designed to optimize cost and performance for event-driven workloads. Traditionally, updating code or configuration in this environment required forcefully restarting all instances, which could lead to service interruptions and downtime. The purpose of this update is to introduce rolling updates, enabling zero-downtime deployments and improving reliability and user experience during maintenance or release cycles.

**Specific Features and Detailed Changes**  
With rolling updates now generally available, the Flex Consumption plan supports seamless deployments. Instead of simultaneous restarts, instances are updated in a controlled, sequential manner. This feature is activated through a simple configuration change, making it accessible and easy to adopt for existing workloads. The update eliminates the need for manual intervention or complex deployment scripts to achieve high availability during updates.

**Technical Mechanisms and Implementation Methods**  
The rolling update mechanism works by orchestrating the update process across multiple instances. When a deployment is triggered (either for code or configuration changes), the platform updates instances one at a time or in small batches, ensuring that at least some instances remain operational throughout the process. This approach prevents service disruption and maintains continuous availability. The configuration change required to enable rolling updates is integrated into the deployment workflow, allowing IT professionals to specify update behavior without modifying application code.

**Use Cases and Application Scenarios**  
Rolling updates are particularly valuable for production environments running mission-critical Azure Functions where uptime is essential. Common scenarios include:  
- Deploying new features or bug fixes without impacting active users  
- Applying configuration changes or security patches with no downtime  
- Supporting continuous integration and continuous deployment (CI/CD) pipelines for serverless applications  
- Maintaining high availability for APIs, event processing, or backend automation tasks

**Important Considerations and Limitations**  
While rolling updates provide zero-downtime deployments, IT professionals should consider the following:  
- The update process is managed by the platform, so custom update logic or sequencing is not supported beyond the provided configuration options  
- Application state and session management should be designed to handle instance restarts gracefully  
- Monitoring and logging should be configured to track update progress and identify any issues during deployment  
- The feature is specific to the Flex Consumption plan; other hosting plans may not support rolling updates in the same manner

**Integration with Related Azure Services**  
Rolling updates in Flex Consumption integrate seamlessly with Azure Functions and related deployment tools, such as Azure DevOps, GitHub Actions, and ARM templates. The feature supports standard deployment workflows and can be combined with Azure Monitor for observability and alerting during update cycles. It also complements Azure’s broader high availability and scalability features, ensuring that serverless workloads remain resilient during maintenance.

**Summary Sentence**  
Rolling updates in the Flex Consumption plan are now generally available, enabling zero-downtime deployments for Azure Functions through a simple configuration change and sequential instance updates.

---

### 25. Generally Available: Dynamic threshold for Log search alerts

**Published**: June 02, 2026 19:30:20 UTC
**Link**: [Generally Available: Dynamic threshold for Log search alerts](https://azure.microsoft.com/updates?id=561984)

**Update ID**: 561984
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features, Microsoft Build

**Summary**:

- What was updated  
Dynamic threshold support for Log search alerts in Azure Monitor is now generally available.

- Key changes or new features  
Dynamic thresholds automatically calculate optimal alert thresholds for Log search alert rules, removing the need for users to manually define static thresholds. This feature leverages historical data patterns to set intelligent alert limits, improving detection accuracy and reducing false positives or missed alerts.

- Target audience affected  
Developers and IT professionals who configure and manage Log search alerts in Azure Monitor, especially those responsible for monitoring application and infrastructure logs.

- Important notes if any  
To use dynamic thresholds, select the "Dynamic" threshold type when creating or editing a Log search alert rule in Azure Monitor. This feature is particularly useful for environments with variable or unpredictable log data patterns. No additional configuration or manual tuning is required, streamlining alert management and improving operational efficiency. For more details, refer to the official documentation: https://azure.microsoft.com/updates?id=561984

**Details**:

**Comprehensive Technical Explanation: Generally Available – Dynamic Threshold for Log Search Alerts**

**Background and Purpose of the Update**  
Traditionally, configuring Log search alerts in Azure Monitor required users to manually define static thresholds for alert rules. This process often demanded deep domain knowledge and ongoing tuning, as the optimal threshold could vary over time or across different environments. The introduction of Dynamic Thresholds for Log search alerts addresses these challenges by automating threshold determination, thereby reducing manual effort and improving alert accuracy.

**Specific Features and Detailed Changes**  
With this update, Dynamic Thresholds for Log search alerts are now generally available. This feature enables users to configure alert rules without specifying a fixed threshold value. Instead, the system automatically calculates and applies the most appropriate threshold based on the underlying log data patterns. This enhancement streamlines alert rule creation and maintenance, ensuring that alerts remain relevant even as baseline metrics shift.

**Technical Mechanisms and Implementation Methods**  
Dynamic Thresholds leverage built-in algorithms to analyze historical log data and determine what constitutes normal versus anomalous behavior. When configuring a Log search alert, users can now select the dynamic threshold option. The system then continuously evaluates log data, adapting thresholds to reflect current trends and variations. This approach minimizes false positives and negatives by aligning alerting criteria with real-time operational baselines.

**Use Cases and Application Scenarios**  
Dynamic Thresholds are particularly valuable in environments where log data exhibits variable or seasonally shifting patterns, such as application performance monitoring, infrastructure health checks, or security event detection. For example, in a scenario where application request rates fluctuate throughout the day, dynamic thresholds ensure that alerts are triggered only when deviations from the norm occur, rather than on every minor fluctuation.

**Important Considerations and Limitations**  
While Dynamic Thresholds simplify alert configuration, users should be aware that the effectiveness of the feature depends on the quality and quantity of historical log data available for analysis. Insufficient or highly irregular data may impact the accuracy of threshold calculations. Additionally, users should review alert rule configurations periodically to ensure alignment with operational requirements and compliance policies.

**Integration with Related Azure Services**  
Dynamic Thresholds for Log search alerts are integrated into Azure Monitor, allowing seamless use alongside other monitoring and alerting capabilities. Alerts generated using dynamic thresholds can trigger automated actions, notifications, or integrations with services such as Azure Logic Apps, Azure Functions, and ITSM tools, supporting end-to-end incident management workflows.

**Summary Sentence**  
The general availability of Dynamic Thresholds for Log search alerts in Azure Monitor enables IT professionals to automate threshold management, enhancing alert accuracy and reducing manual configuration effort by leveraging intelligent, data-driven threshold determination.

---

### 26. Public Preview: Azure Databricks workspace-wide Genie MCP for Microsoft Copilot Studio

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Databricks workspace-wide Genie MCP for Microsoft Copilot Studio](https://azure.microsoft.com/updates?id=564868)

**Update ID**: 564868
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Databricks introduced a public preview of a workspace-wide Genie MCP endpoint for Microsoft Copilot Studio integration.

- Key changes or new features  
A new single Genie MCP endpoint allows Microsoft Copilot Studio agents to query natural-language questions across the entire Azure Databricks workspace. The endpoint automatically routes queries across all connected Genie spaces and underlying data sources, simplifying integration and enabling broader data discovery and interaction via Copilot Studio. This enhancement streamlines how Copilot agents access and retrieve data, eliminating the need to configure multiple endpoints for different spaces.

- Target audience affected  
Developers and IT professionals who build, manage, or integrate Microsoft Copilot Studio agents with Azure Databricks workspaces. This is particularly relevant for teams leveraging natural language interfaces for data exploration, analytics, or automation.

- Important notes if any  
This feature is currently in public preview and may be subject to changes before general availability. Users should validate compatibility with their existing Genie spaces and review security and access controls for workspace-wide querying. Documentation and API references should be consulted for integration details.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=564868

**Details**:

**Azure Update Report: Public Preview – Azure Databricks Workspace-wide Genie MCP for Microsoft Copilot Studio**

**Background and Purpose of the Update**  
This update introduces a workspace-wide Genie MCP (Managed Control Point) endpoint for Azure Databricks, specifically designed to enhance integration with Microsoft Copilot Studio. The primary purpose is to enable Copilot Studio agents to query natural-language questions across the entire Databricks workspace via a single endpoint. This streamlines access to Databricks resources and data, facilitating more efficient and comprehensive interaction through conversational AI.

**Specific Features and Detailed Changes**  
- **Workspace-wide Genie MCP Endpoint:** A new endpoint is available that covers the entire Azure Databricks workspace, rather than being limited to individual Genie spaces.
- **Unified Querying:** Copilot Studio agents can now issue natural-language queries that span all connected Genie spaces within a workspace, eliminating the need to target specific spaces or endpoints.
- **Auto-routing:** The endpoint automatically routes queries across all connected Genie spaces, ensuring that the most relevant data and resources are accessed without manual intervention.
- **Public Preview Availability:** The feature is currently in public preview, allowing IT professionals to test and evaluate its capabilities before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Endpoint Architecture:** The Genie MCP endpoint acts as a central access point within the Databricks workspace. It abstracts the complexity of multiple Genie spaces by providing a unified interface for Copilot Studio agents.
- **Auto-routing Logic:** When a natural-language query is submitted, the endpoint determines which Genie spaces are relevant and routes the query accordingly. This mechanism ensures comprehensive coverage and reduces the need for manual configuration.
- **Integration with Copilot Studio:** The endpoint is designed to be compatible with Microsoft Copilot Studio, enabling conversational agents to leverage Databricks data and resources seamlessly.

**Use Cases and Application Scenarios**  
- **Conversational Data Exploration:** Data analysts and business users can use Copilot Studio agents to ask questions about datasets, notebooks, and other resources across the Databricks workspace, receiving unified responses.
- **Automated Reporting:** IT professionals can automate report generation by leveraging Copilot Studio agents to query and aggregate data from multiple Genie spaces.
- **Workspace-wide Insights:** Organizations can gain holistic insights from their Databricks workspace without needing to manually consolidate information from individual Genie spaces.

**Important Considerations and Limitations**  
- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should monitor for updates and changes as the feature matures.
- **Endpoint Scope:** The endpoint covers all connected Genie spaces within a workspace, but details about unsupported scenarios or limitations are not specified in the update.
- **Security and Access Control:** IT professionals should ensure that proper access controls are in place, as the endpoint provides broad access across the workspace.

**Integration with Related Azure Services**  
- **Azure Databricks:** The Genie MCP endpoint is native to Azure Databricks, providing deep integration with its workspace architecture.
- **Microsoft Copilot Studio:** The update is specifically designed to enhance Copilot Studio’s ability to interact with Databricks, enabling conversational AI agents to access and query Databricks resources.
- **Genie Spaces:** The endpoint consolidates access to all Genie spaces, simplifying integration and reducing configuration overhead.

**Summary Sentence**  
The public preview of the Azure Databricks workspace-wide Genie MCP endpoint enables Microsoft Copilot Studio agents to query natural-language questions across the entire workspace through a single, auto-routing endpoint, streamlining data access and conversational AI integration.

---

### 27. Public Preview: Azure Databricks Lakebase branching with GitHub Copilot agent mode

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Databricks Lakebase branching with GitHub Copilot agent mode](https://azure.microsoft.com/updates?id=564863)

**Update ID**: 564863
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Databricks Lakebase now supports branching with GitHub Copilot agent mode in public preview.

- Key changes or new features  
Developers can create a copy-on-write branch of their Lakebase production database using a single command. This branch acts as an isolated environment, allowing safe experimentation. GitHub Copilot’s agent mode can connect directly to the branch endpoint, enabling developers to debug AI applications and agents against real production data without impacting the live environment.

- Target audience affected  
This update is relevant to data engineers, AI/ML developers, and IT professionals managing Azure Databricks environments, especially those integrating with GitHub Copilot and working with production data.

- Important notes  
This feature enhances developer productivity and safety by allowing real-world testing and debugging without risking production data integrity. It streamlines the workflow for AI app development and troubleshooting in Azure Databricks. As this is a public preview, it is recommended to review documentation and test in non-critical environments before full-scale adoption.

[More details](https://azure.microsoft.com/updates?id=564863)

**Details**:

**Azure Update Report: Public Preview – Azure Databricks Lakebase Branching with GitHub Copilot Agent Mode**

**Background and Purpose of the Update**  
This update introduces a new capability in Azure Databricks Lakebase, allowing developers to create copy-on-write branches of their production databases. The primary goal is to enable safe, efficient debugging and development of AI applications and agents using real production data, without risking data integrity or impacting live environments. By integrating with GitHub Copilot agent mode, this feature streamlines the development workflow, making it easier to test and iterate on AI solutions in a controlled environment.

**Specific Features and Detailed Changes**  
- **Copy-on-Write Branching:** Developers can now generate a branch of their Lakebase production database with a single command. This branch is a copy-on-write version, meaning changes made in the branch do not affect the original production data.
- **GitHub Copilot Agent Mode Integration:** The update allows the branch endpoint to be connected directly to GitHub Copilot agent mode. This integration facilitates AI-assisted development and debugging workflows.
- **Real Data Debugging:** Developers can debug AI applications and agents against actual production data, increasing the reliability and accuracy of testing without exposing or modifying the production environment.

**Technical Mechanisms and Implementation Methods**  
- **Branch Creation:** The branching process utilizes a copy-on-write mechanism, which efficiently creates a logical copy of the production database. Only changes made in the branch consume additional storage, optimizing resource usage.
- **Endpoint Connectivity:** The branch exposes a dedicated endpoint, which can be linked to GitHub Copilot agent mode. This allows AI-powered code suggestions, debugging, and agent testing to interact directly with the branched data.
- **Isolation:** All operations performed within the branch are isolated from the production database, ensuring that experimental changes, tests, or debug actions do not propagate to the live environment.

**Use Cases and Application Scenarios**  
- **AI Application Debugging:** Developers can safely test new AI features, algorithms, or agents using real production data, ensuring that their solutions are robust and production-ready.
- **Rapid Prototyping:** Teams can quickly spin up isolated environments for prototyping new data models, queries, or AI agents, accelerating innovation cycles.
- **Collaborative Development:** Multiple developers can create their own branches for parallel development, reducing bottlenecks and merge conflicts in shared environments.

**Important Considerations and Limitations**  
- **Data Privacy and Security:** While branches provide isolation, access controls and data governance policies should be enforced to prevent unauthorized data exposure.
- **Resource Consumption:** Although copy-on-write is storage-efficient, extensive modifications in branches may increase storage usage.
- **Preview Limitations:** As this feature is in public preview, there may be limitations in scalability, support, or integration with other Azure Databricks features. Production use should be approached with caution.

**Integration with Related Azure Services**  
- **Azure Databricks:** The feature is natively integrated within Azure Databricks Lakebase, leveraging its data management and analytics capabilities.
- **GitHub Copilot:** Direct integration with GitHub Copilot agent mode enhances developer productivity by providing AI-powered coding assistance and debugging tools.
- **Azure Data Governance:** Organizations should integrate this feature with their existing Azure data governance and security frameworks to maintain compliance and control.

**Summary Sentence:**  
Azure Databricks Lakebase now enables developers to create isolated, copy-on-write branches of production databases and connect them to GitHub Copilot agent mode, streamlining AI application debugging and development against real data while preserving production integrity.

---

### 28. Generally Available: Improved PDF batch document translation in Azure AI Translator

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Improved PDF batch document translation in Azure AI Translator](https://azure.microsoft.com/updates?id=564422)

**Update ID**: 564422
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Translator's batch document translation now has generally available improvements for PDF translation.

- Key changes or new features  
The service now leverages Azure AI Document Intelligence to recover document structure from both digital-native and scanned PDFs before translating the recognized text. This enhancement improves the accuracy and fidelity of translated PDFs, preserving layouts, tables, and other structural elements.

- Target audience affected  
Developers and IT professionals integrating document translation workflows, especially those handling multilingual PDF content in enterprise applications or automated pipelines.

- Important notes if any  
These improvements apply to both digital-native and scanned PDFs, making it easier to process a wide range of document types. Developers should consider updating their workflows to take advantage of the improved structure recognition and translation quality. No changes to API usage are required, but reviewing output quality and adjusting post-processing logic (if any) is recommended. For more details, refer to the official documentation: https://azure.microsoft.com/updates?id=564422

**Details**:

**Azure Update Report: Generally Available – Improved PDF Batch Document Translation in Azure AI Translator**

**Background and Purpose of the Update:**  
The update addresses the need for accurate and efficient translation of PDF documents at scale within Azure AI Translator. Previously, translating PDFs—especially scanned or image-based files—posed challenges in structure recognition and text extraction. The purpose of this update is to enhance the reliability and quality of PDF translation by leveraging advanced document processing capabilities.

**Specific Features and Detailed Changes:**  
- **General Availability:** The improvements for PDF batch document translation are now generally available, signifying production readiness and support.
- **Enhanced Structure Recovery:** The service now utilizes Azure AI Document Intelligence to recover document structure from both digital-native PDFs (containing selectable text) and scanned PDFs (image-based, requiring OCR).
- **Improved Translation Accuracy:** Recognized text, extracted with structural context, is passed to Azure AI Translator for translation, resulting in more accurate and contextually appropriate output.

**Technical Mechanisms and Implementation Methods:**  
- **Document Structure Extraction:** Azure AI Document Intelligence is integrated into the translation pipeline. For digital-native PDFs, it extracts text and preserves layout and formatting. For scanned PDFs, it employs optical character recognition (OCR) to detect and extract text from images, reconstructing the document’s logical structure.
- **Batch Processing:** The solution supports batch translation, allowing multiple PDF documents to be processed in a single operation, streamlining large-scale translation workflows.
- **Translation Pipeline:** After structure and text extraction, the recognized content is sent to Azure AI Translator, which performs the language translation while maintaining as much of the original document's structure as possible.

**Use Cases and Application Scenarios:**  
- **Enterprise Document Localization:** Organizations can translate large volumes of PDF reports, manuals, contracts, or regulatory documents for global operations.
- **Archival and Compliance:** Scanned legacy documents can be translated for compliance, audit, or knowledge management purposes.
- **Cross-border Collaboration:** Multinational teams can share translated technical documentation, training materials, or policy documents in PDF format.

**Important Considerations and Limitations:**  
- **Input Types:** Both digital-native and scanned PDFs are supported, but the quality of translation for scanned PDFs depends on the clarity and legibility of the original scan.
- **Structure Preservation:** While the service aims to recover and preserve document structure, complex layouts or heavily formatted PDFs may experience partial fidelity loss.
- **Batch Limits:** Users should consult Azure AI Translator documentation for any limitations on batch sizes, file sizes, or supported languages.
- **Service Dependencies:** The translation quality and structure recovery are dependent on the capabilities of Azure AI Document Intelligence and Azure AI Translator.

**Integration with Related Azure Services:**  
- **Azure AI Document Intelligence:** This service is directly leveraged for structure and text extraction from PDFs.
- **Azure AI Translator:** Handles the core translation process after text extraction.
- **Workflow Automation:** The improved batch translation can be integrated into broader Azure workflows, such as Logic Apps, Azure Functions, or Data Factory pipelines, to automate document translation tasks as part of business processes.

**Summary Sentence:**  
Azure AI Translator’s generally available improvements for PDF batch document translation now leverage Azure AI Document Intelligence to accurately recover and translate text from both digital-native and scanned PDFs, enhancing translation quality and scalability for enterprise document workflows.

---

### 29. Generally Available: Image file translation for batch document translation in Azure AI Translator

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Image file translation for batch document translation in Azure AI Translator](https://azure.microsoft.com/updates?id=564417)

**Update ID**: 564417
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Translator’s batch document translation now generally supports image file input.

- Key changes or new features  
Developers and IT professionals can now submit image files (.jpeg, .png, .bmp, .webp) for translation in batch mode. The service uses Optical Character Recognition (OCR) to extract text from images and then translates the recognized text into the specified target language.

- Target audience affected  
This update is relevant for developers integrating translation workflows, IT professionals managing document processing pipelines, and organizations needing to translate image-based documents at scale.

- Important notes if any  
Ensure that image quality is sufficient for accurate OCR extraction. This feature enables end-to-end translation of scanned documents, photos, and other image-based content, expanding beyond traditional text and document formats. The update is now generally available and can be accessed via the Azure AI Translator API. For more details, refer to the official documentation.

**Details**:

**Comprehensive Technical Explanation: Azure AI Translator – Image File Translation for Batch Document Translation (General Availability)**

**Background and Purpose of the Update:**  
Azure AI Translator’s batch document translation service has expanded its input capabilities to include image files, now generally available. Previously, the service focused on text-based documents, limiting scenarios where textual content was embedded within images. This update addresses the need for automated translation workflows that include image-based content, supporting broader document types and enhancing accessibility for organizations dealing with scanned documents, photographs, or image-based archives.

**Specific Features and Detailed Changes:**  
- **Supported Image Formats:** The batch document translation service now accepts `.jpeg`, `.png`, `.bmp`, and `.webp` image files as input.
- **OCR Integration:** Upon receiving image files, the service automatically applies Optical Character Recognition (OCR) to extract text.
- **Translation Workflow:** Extracted text is then translated into the specified target language(s) using Azure AI Translator’s translation models.
- **Output:** The translated text is provided as part of the batch translation output, consistent with the service’s handling of other document types.

**Technical Mechanisms and Implementation Methods:**  
- **Input Handling:** Users submit image files in supported formats to the batch document translation endpoint.
- **OCR Processing:** The service leverages built-in OCR capabilities to detect and extract textual content from the images. This step is fully managed and requires no separate configuration.
- **Translation Pipeline:** Recognized text is passed through Azure’s neural machine translation models, ensuring language support parity with existing document translation features.
- **Batch Processing:** The system processes multiple image files in parallel, maintaining the scalability and throughput characteristics of the batch document translation service.

**Use Cases and Application Scenarios:**  
- **Multilingual Digitization Projects:** Organizations digitizing paper archives or scanned documents can now automate translation workflows, even when source material is in image format.
- **Globalization of Visual Content:** Businesses with image-based manuals, posters, or marketing materials can efficiently localize content for international audiences.
- **Accessibility Solutions:** Educational institutions and public sector entities can translate scanned forms or notices, improving accessibility for non-native speakers.

**Important Considerations and Limitations:**  
- **Supported Formats:** Only `.jpeg`, `.png`, `.bmp`, and `.webp` formats are supported; other image types require conversion.
- **OCR Accuracy:** Translation quality is dependent on the accuracy of OCR extraction. Poor image quality, handwriting, or complex layouts may affect results.
- **Language Support:** The range of supported source and target languages aligns with those available in Azure AI Translator.
- **Output Format:** The translated output is text-based; the service does not reconstruct the original image with translated text overlays.

**Integration with Related Azure Services:**  
- **Azure Blob Storage:** Image files can be stored and managed in Azure Blob Storage, which is commonly used as the source and destination for batch translation jobs.
- **Azure Cognitive Services:** The OCR component is tightly integrated with Azure’s cognitive capabilities, ensuring seamless operation within the Translator workflow.
- **Automation and Orchestration:** The service can be incorporated into larger Azure-based automation pipelines, such as Logic Apps or Azure Functions, for end-to-end document processing and translation.

**Summary:**  
Azure AI Translator’s batch document translation now generally supports image files, enabling automated OCR and translation workflows for `.jpeg`, `.png`, `.bmp`, and `.webp` formats, thereby broadening multilingual content processing capabilities for enterprise and organizational scenarios.

---

### 30. Generally Available: Image translation inside Office documents for batch document translation

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Image translation inside Office documents for batch document translation](https://azure.microsoft.com/updates?id=564412)

**Update ID**: 564412
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Translator’s batch document translation now generally supports translating text inside images embedded in Word (.docx) files.

- Key changes or new features  
The service can now:  
  - Detect image regions within .docx files  
  - Perform OCR (Optical Character Recognition) on embedded images  
  - Translate the recognized text  
  - Re-render the translated text back into the original image context within the document  
This enhancement is generally available and fully supported.

- Target audience affected  
Developers and IT professionals who automate or integrate document translation workflows, especially those handling multilingual Word documents containing images with text (e.g., scanned forms, annotated screenshots, or presentations).

- Important notes if any  
- The feature streamlines translation processes for documents containing both editable text and embedded images, reducing manual effort.  
- No additional configuration is required; the feature is available through the existing Translator batch document translation API.  
- Review the documentation for supported languages and image formats.  
- This update improves localization quality for organizations working with complex documents in global environments.

For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=564412).

**Details**:

**Azure Update Technical Explanation: Generally Available: Image translation inside Office documents for batch document translation**

**Background and Purpose of the Update:**  
This update addresses the need for comprehensive multilingual support in document translation workflows, specifically targeting scenarios where textual content is embedded within images inside Microsoft Word (`.docx`) files. Previously, Azure AI Translator’s batch document translation service could translate only the editable text within documents, leaving out text that was part of embedded images. This limitation posed challenges for organizations needing complete translation coverage for documents containing scanned content, screenshots, or annotated images.

**Specific Features and Detailed Changes:**  
The Azure AI Translator batch document translation service now offers general availability of image translation capabilities within Word `.docx` files. The key enhancement is the ability to detect, extract, translate, and re-render text that appears inside images embedded in these documents. This feature ensures that both standard document text and image-contained text are translated in a single batch operation, resulting in a more accurate and complete multilingual document output.

**Technical Mechanisms and Implementation Methods:**  
The service enhancement operates through a multi-step pipeline:
1. **Image Region Detection:** The service scans the `.docx` file to identify image regions embedded within the document.
2. **Optical Character Recognition (OCR):** Detected images undergo OCR processing to extract any textual content present within the images.
3. **Text Translation:** The recognized text is then passed through Azure AI Translator’s neural translation models to generate the translated text in the target language.
4. **Re-rendering Translated Text:** The translated text is programmatically re-inserted into the original image regions, preserving the document’s layout and visual fidelity.

This process is fully automated and integrated within the batch document translation workflow, requiring no manual intervention for image text extraction or re-insertion.

**Use Cases and Application Scenarios:**  
- **Global Documentation:** Enterprises translating product manuals, training materials, or reports containing annotated screenshots or scanned pages.
- **Legal and Compliance:** Organizations needing to translate contracts or regulatory documents with embedded scanned signatures or stamps.
- **Education:** Institutions converting course materials with diagrams or labeled images for multilingual audiences.
- **Healthcare:** Translating medical documents with embedded images containing handwritten or printed notes.

**Important Considerations and Limitations:**  
- The feature is specifically available for Word `.docx` files processed via the batch document translation API.
- The quality of OCR and translation may vary depending on the image quality, font clarity, and language support.
- There may be limitations in accurately re-rendering complex or highly stylized images.
- The update does not mention support for other Office formats (e.g., PowerPoint, Excel) or for images in non-`.docx` files.

**Integration with Related Azure Services:**  
This capability is part of the Azure AI Translator suite and leverages Azure’s OCR technology, likely integrated with Azure Cognitive Services Computer Vision for text extraction. It can be orchestrated within broader Azure-based document processing pipelines, such as those using Azure Logic Apps, Azure Functions, or Azure Data Factory, to automate end-to-end multilingual document workflows.

**Summary:**  
Azure AI Translator’s batch document translation now generally supports translating text inside images embedded in Word `.docx` files, using OCR and neural translation to deliver fully localized documents in automated workflows.

---

### 31. Generally Available: OneLake catalog integration for Azure AI Search knowledge sources

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: OneLake catalog integration for Azure AI Search knowledge sources](https://azure.microsoft.com/updates?id=564407)

**Update ID**: 564407
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
OneLake catalog integration is now generally available for Azure AI Search knowledge sources.

- Key changes or new features  
Developers and IT professionals can now register a OneLake item once in the catalog and reuse it across multiple Azure AI Search knowledge sources and agents. The integration respects existing OneLake item-level permissions, ensuring secure and consistent access control. This streamlines data management and reduces duplication when configuring search solutions.

- Target audience affected  
Developers and IT professionals working with Azure AI Search, especially those managing multiple knowledge sources or agents, and those leveraging Microsoft OneLake as a data platform.

- Important notes if any  
The integration simplifies the process of connecting OneLake data to Azure AI Search, improving efficiency and security. Existing OneLake permissions are enforced, so no additional configuration is required for access control. This update is relevant for organizations standardizing on OneLake for data storage and discovery.

[Read more](https://azure.microsoft.com/updates?id=564407)

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
This update announces the general availability of OneLake catalog integration for Azure AI Search knowledge sources. The primary goal is to streamline and centralize the management of data assets used as knowledge sources in Azure AI Search. By enabling direct integration with the OneLake catalog, customers can efficiently register and reuse OneLake items across multiple knowledge sources and agents, reducing redundancy and simplifying data governance.

**Specific Features and Detailed Changes:**  
- **One-Time Registration:** Users can now register a OneLake item (such as a file, folder, or dataset) once in the Azure AI Search knowledge source configuration.
- **Reuse Across Multiple Knowledge Sources and Agents:** After registration, the same OneLake item can be referenced by multiple knowledge sources and AI agents, eliminating the need for repeated registration or configuration.
- **Permission Enforcement:** The integration respects existing OneLake item-level permissions, ensuring that access control and security policies defined in OneLake are consistently enforced when the items are accessed via Azure AI Search.

**Technical Mechanisms and Implementation Methods:**  
- **Catalog Integration:** Azure AI Search connects directly to the OneLake catalog, allowing items to be discovered and registered as knowledge sources through the Azure portal or API.
- **Reference Model:** Instead of duplicating data or manually configuring access for each agent, Azure AI Search uses a reference to the registered OneLake item. This reference model ensures that updates to the item or its permissions in OneLake are automatically reflected in all dependent knowledge sources.
- **Security Alignment:** The integration leverages OneLake’s native item-level permission model, so only authorized users and agents can access the registered data, maintaining compliance and security best practices.

**Use Cases and Application Scenarios:**  
- **Enterprise Knowledge Management:** Organizations with large, distributed datasets in OneLake can centrally manage their knowledge sources for Azure AI Search, improving efficiency and reducing administrative overhead.
- **Multi-Agent Scenarios:** In environments where multiple AI agents or search applications require access to the same datasets, this integration allows for consistent data access and governance.
- **Data Governance and Compliance:** By reusing OneLake items with enforced permissions, organizations can ensure that data access policies are uniformly applied across all AI Search scenarios.

**Important Considerations and Limitations:**  
- **Permission Inheritance:** Access to OneLake items via Azure AI Search is governed strictly by existing OneLake item-level permissions. Users must ensure that permissions are correctly configured in OneLake to avoid access issues or unintentional data exposure.
- **Catalog Scope:** The integration is limited to items registered in the OneLake catalog. Data not present in OneLake or not cataloged cannot be used with this feature.
- **No Data Duplication:** The integration does not duplicate data; it references the original OneLake item, which may have performance or availability implications depending on the underlying OneLake storage configuration.

**Integration with Related Azure Services:**  
- **Azure AI Search:** The feature is directly integrated into Azure AI Search, enhancing its ability to use OneLake as a primary data source for knowledge mining and search scenarios.
- **OneLake:** Acts as the central data lake and catalog, providing unified data management, security, and governance.
- **Azure Portal and APIs:** The integration can be managed through the Azure portal or programmatically via APIs, supporting automation and DevOps workflows.

**Summary Sentence:**  
The general availability of OneLake catalog integration for Azure AI Search knowledge sources enables centralized, secure, and reusable data asset management, streamlining knowledge source configuration and enforcing consistent item-level permissions across multiple search agents and applications.

---

### 32. Generally Available: Managed virtual network for evaluations in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Managed virtual network for evaluations in Microsoft Foundry](https://azure.microsoft.com/updates?id=564402)

**Update ID**: 564402
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Managed virtual network (VNET) support for evaluations in Microsoft Foundry is now generally available.

- Key changes or new features  
Customers can now run cloud evaluation jobs against models and agents that are secured behind private endpoints, using a Foundry-managed VNET. This managed VNET handles all outbound connectivity required for evaluation jobs, simplifying network configuration and enhancing security by avoiding exposure to public internet endpoints.

- Target audience affected  
Developers and IT professionals using Microsoft Foundry for model and agent evaluations, especially those with strict network isolation or security requirements.

- Important notes if any  
This update enables secure, private connectivity for evaluation workloads without the need for customers to manage their own VNETs or complex network peering. It is particularly beneficial for organizations with compliance or data privacy needs, as it ensures that evaluation traffic remains within a controlled Azure environment. No additional setup is required for outbound connectivity; Foundry manages the necessary network resources automatically.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=564402)

**Details**:

**Azure Update Report: Generally Available – Managed Virtual Network for Evaluations in Microsoft Foundry**

**Background and Purpose of the Update:**  
Microsoft Foundry has announced the general availability of managed virtual network (VNET) support for evaluation workloads. This update addresses the need for secure and controlled network environments when running evaluation jobs against models and agents that are protected behind private endpoints. The primary purpose is to enable customers to perform cloud-based evaluations without exposing sensitive resources to the public internet, thereby enhancing security and compliance.

**Specific Features and Detailed Changes:**  
- **Managed VNET for Evaluations:** Customers can now leverage a Foundry-managed virtual network to run evaluation jobs. This allows evaluation workloads to securely access models and agents that are only accessible via private endpoints.
- **Outbound Connectivity:** The managed VNET is responsible for handling outbound connectivity, ensuring that evaluation jobs can communicate with necessary resources without requiring direct public internet exposure.

**Technical Mechanisms and Implementation Methods:**  
- **Private Endpoint Integration:** The managed VNET is configured to allow evaluation jobs to access resources (such as models and agents) that are only reachable through Azure Private Endpoints. This ensures that traffic remains within the Azure backbone network, reducing exposure to external threats.
- **Network Isolation:** By utilizing a managed VNET, evaluation jobs are isolated from other network traffic, providing an additional layer of security and reducing the risk of data leakage.
- **Outbound Routing:** The Foundry-managed VNET manages all outbound traffic required for the evaluation jobs, simplifying network configuration and reducing the need for customers to manage complex routing or firewall rules.

**Use Cases and Application Scenarios:**  
- **Secure Model Evaluation:** Organizations can evaluate machine learning models or AI agents that are hosted behind private endpoints, ensuring that sensitive intellectual property is not exposed to the public internet during testing.
- **Compliance-Driven Workloads:** Enterprises with strict regulatory or compliance requirements can use the managed VNET to ensure that evaluation jobs adhere to internal security policies.
- **Multi-Tenant Environments:** Managed VNETs help segregate evaluation workloads from other tenants or environments, supporting scenarios where multiple teams or projects require isolated network access.

**Important Considerations and Limitations:**  
- **Scope Limited to Evaluations:** The managed VNET feature is specifically for evaluation jobs within Microsoft Foundry. It may not extend to other types of workloads or general-purpose networking needs.
- **Outbound Connectivity Only:** The update highlights outbound connectivity management. Inbound connectivity or custom network configurations may not be supported within this managed VNET context.
- **Dependency on Private Endpoints:** To benefit from this feature, models and agents must be accessible via Azure Private Endpoints.

**Integration with Related Azure Services:**  
- **Azure Private Link:** The managed VNET leverages Azure Private Endpoints, which are part of Azure Private Link, to securely connect to resources without traversing the public internet.
- **Azure Networking Services:** The managed VNET operates within the Azure networking ecosystem, allowing seamless integration with other Azure services that support private endpoints and virtual networks.

**Summary Sentence:**  
Microsoft Foundry now offers general availability of managed virtual network support for evaluation jobs, enabling secure, private access to models and agents behind private endpoints by handling outbound connectivity within a Foundry-managed VNET.

---

### 33. Generally Available: LLM Speech API in Azure AI Speech

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: LLM Speech API in Azure AI Speech](https://azure.microsoft.com/updates?id=564387)

**Update ID**: 564387
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The LLM Speech API in Azure AI Speech is now generally available.

- Key changes or new features  
  - The API leverages large language models (LLMs) to provide advanced transcription and translation for audio files.  
  - Multi-lingual support is expanded to 25 languages and over 90 locales.  
  - Improved transcription and translation accuracy.  
  - Service availability is expanded to more Azure regions.  
  - Enhanced developer experience and integration capabilities.

- Target audience affected  
  - Developers building applications that require speech-to-text or audio translation features.  
  - IT professionals managing AI-powered voice and language solutions in enterprise environments.

- Important notes if any  
  - The LLM Speech API is suitable for scenarios needing high-accuracy, multi-lingual transcription and translation, such as media, customer service, and accessibility solutions.  
  - Developers can integrate the API via REST or SDKs, and should review updated documentation for best practices and region availability.  
  - Consider reviewing pricing and compliance details, as LLM-powered features may have different cost or data handling implications.

[Read more](https://azure.microsoft.com/updates?id=564387)

**Details**:

**Azure Update Technical Report: Generally Available – LLM Speech API in Azure AI Speech**

**Background and Purpose of the Update**  
The general availability of the LLM Speech API in Azure AI Speech marks a significant advancement in Azure’s speech services. This update aims to provide IT professionals and developers with access to state-of-the-art transcription and translation capabilities powered by large language models (LLMs). The purpose is to enhance the accuracy and flexibility of audio file processing, supporting diverse multilingual scenarios and expanding the reach of Azure AI Speech to more regions and use cases.

**Specific Features and Detailed Changes**  
- **LLM-Powered Transcription and Translation:** The API leverages advanced LLMs to deliver high-accuracy speech-to-text transcription and audio translation.
- **Multi-Lingual Support:** The service supports transcription and translation across 25 languages and over 90 locales, enabling broad global applicability.
- **Improved Accuracy:** The use of LLMs provides enhanced recognition accuracy, particularly in complex or nuanced audio content.
- **Expanded Regional Availability:** The API is now accessible in more Azure regions, allowing customers to deploy solutions closer to their users and comply with data residency requirements.
- **Enhancements:** While the summary mentions “enh,” it is inferred that this refers to general enhancements in the service’s capabilities, such as performance or reliability improvements.

**Technical Mechanisms and Implementation Methods**  
The LLM Speech API is built on Azure’s AI infrastructure, utilizing large language models for both transcription and translation tasks. Audio files are processed through RESTful API endpoints, where the speech content is analyzed and converted into text or translated into the target language. The API’s architecture supports batch processing of audio files, making it suitable for large-scale or asynchronous workflows. The multi-lingual support is managed through locale parameters, allowing developers to specify source and target languages as needed.

**Use Cases and Application Scenarios**  
- **Enterprise Transcription:** Automate meeting, interview, or call center audio transcription with improved accuracy for compliance and analytics.
- **Media Localization:** Translate podcasts, webinars, or training materials into multiple languages to reach a global audience.
- **Accessibility Solutions:** Generate real-time captions or translated transcripts to support users with hearing impairments or non-native speakers.
- **Legal and Healthcare Documentation:** Accurately transcribe and translate sensitive audio files for record-keeping and cross-border collaboration.

**Important Considerations and Limitations**  
- **Language and Locale Coverage:** While the API supports 25 languages and 90+ locales, users should verify that their required languages are included.
- **Regional Availability:** Expanded regions are supported, but customers must confirm that their preferred Azure region offers the LLM Speech API.
- **Data Security and Compliance:** Users should review Azure’s data handling policies to ensure compliance with organizational and regulatory requirements when processing audio files.
- **API Quotas and Pricing:** As with other Azure AI services, usage may be subject to quotas and billing based on the volume of audio processed.

**Integration with Related Azure Services**  
The LLM Speech API integrates seamlessly with other Azure AI services, such as Azure Cognitive Services for further text analysis, Azure Blob Storage for audio file management, and Azure Logic Apps or Azure Functions for workflow automation. This allows IT professionals to build end-to-end solutions for audio processing, transcription, translation, and downstream analytics within the Azure ecosystem.

**Summary Sentence**  
The general availability of the LLM Speech API in Azure AI Speech delivers advanced, LLM-powered transcription and translation for audio files with multi-lingual support, improved accuracy, and broader regional coverage, enabling robust and scalable audio processing solutions for global enterprises.

---

### 34. Generally Available: Oracle schema conversion to Azure PostgreSQL in Visual Studio Code

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Oracle schema conversion to Azure PostgreSQL in Visual Studio Code](https://azure.microsoft.com/updates?id=563791)

**Update ID**: 563791
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
The PostgreSQL extension for Visual Studio Code now supports general availability of Oracle schema conversion to Azure Database for PostgreSQL-compatible schema.

- Key changes or new features  
Developers can convert Oracle database schema objects (such as tables, indexes, and views) directly within Visual Studio Code using the PostgreSQL extension. The feature introduces a project-based workflow, streamlining schema migration from Oracle to Azure Database for PostgreSQL. This integration simplifies and accelerates database modernization and migration projects by reducing the need for separate migration tools.

- Target audience affected  
This update is relevant for database developers, data engineers, and IT professionals responsible for migrating Oracle databases to Azure Database for PostgreSQL. It is particularly useful for teams working within Visual Studio Code environments.

- Important notes if any  
The feature is now generally available, meaning it is fully supported for production use. Users can leverage the familiar Visual Studio Code interface to manage schema conversion projects, improving productivity and reducing migration complexity. For more details, refer to the official update: https://azure.microsoft.com/updates?id=563791

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Oracle schema conversion to Azure PostgreSQL in Visual Studio Code  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563791)

---

**Background and Purpose of the Update**  
This update addresses the need for seamless migration of database schemas from Oracle to Azure Database for PostgreSQL. Organizations frequently seek to modernize their database infrastructure by moving from proprietary systems like Oracle to open-source platforms such as PostgreSQL, especially within the Azure cloud ecosystem. The purpose of this update is to simplify and accelerate the schema conversion process, reducing manual effort and potential errors during migration.

**Specific Features and Detailed Changes**  
The PostgreSQL extension for Visual Studio Code now supports direct conversion of Oracle database schema objects to Azure Database for PostgreSQL-compatible schemas. Key features include:

- **Project-Based Workflow:** Users can initiate and manage schema conversion projects within Visual Studio Code, allowing for organized, repeatable migration processes.
- **Schema Object Conversion:** The extension handles the translation of Oracle schema objects (such as tables, indexes, views, and other database constructs) into PostgreSQL-compatible formats, ensuring structural compatibility.
- **Integrated Experience:** The conversion functionality is embedded within the PostgreSQL extension, eliminating the need for external tools or manual scripting.

**Technical Mechanisms and Implementation Methods**  
The conversion process is facilitated by the PostgreSQL extension in Visual Studio Code, which provides:

- **Automated Mapping:** The extension parses Oracle schema definitions and maps them to equivalent PostgreSQL constructs, addressing differences in data types, constraints, and object definitions.
- **Project Management:** Conversion tasks are organized into projects, enabling version control, incremental conversion, and tracking of schema changes.
- **Direct Integration:** All operations are performed within Visual Studio Code, leveraging its extensibility and familiar development environment for database administrators and developers.

**Use Cases and Application Scenarios**  
This update is particularly valuable in scenarios such as:

- **Cloud Migration Projects:** Enterprises migrating Oracle databases to Azure Database for PostgreSQL can streamline schema conversion, reducing downtime and risk.
- **Development and Testing:** Developers can quickly convert Oracle schemas for prototyping or testing PostgreSQL compatibility within Azure.
- **Modernization Initiatives:** Organizations seeking to adopt open-source database solutions on Azure can leverage this tool to facilitate the transition from Oracle.

**Important Considerations and Limitations**  
- **Schema Conversion Only:** The update focuses on schema conversion; data migration and application compatibility are not addressed within this feature.
- **Extension Dependency:** Users must install and use the PostgreSQL extension in Visual Studio Code to access this functionality.
- **Oracle to PostgreSQL Differences:** While automated mapping is provided, users should review converted schemas for compatibility, especially regarding complex Oracle-specific features that may not have direct PostgreSQL equivalents.

**Integration with Related Azure Services**  
- **Azure Database for PostgreSQL:** The converted schemas are intended for deployment to Azure Database for PostgreSQL, facilitating integration with Azure’s managed database services.
- **Visual Studio Code Ecosystem:** The extension leverages Visual Studio Code’s extensibility, enabling integration with source control, CI/CD pipelines, and other Azure development tools.

---

**Summary Sentence:**  
The PostgreSQL extension for Visual Studio Code now enables direct conversion of Oracle database schema objects to Azure Database for PostgreSQL-compatible schemas, providing a project-based workflow that streamlines migration and modernization efforts within the Azure cloud environment.

---

### 35. Public Preview: Pre-upgrade validation checks for Azure Database for PostgreSQL

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Pre-upgrade validation checks for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=563786)

**Update ID**: 563786
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Public preview release of pre-upgrade validation checks for Major Version Upgrades (MVU) in Azure Database for PostgreSQL flexible server.

- Key changes or new features  
Users can now independently run pre-upgrade validation checks to assess upgrade compatibility before starting the actual major version upgrade. These checks help identify potential issues or blockers that could impact the upgrade process, allowing for proactive remediation and smoother upgrades.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL flexible servers, especially those planning major version upgrades.

- Important notes  
The pre-upgrade validation feature enables early detection of compatibility issues, reducing upgrade risks and downtime. It is available in public preview and can be accessed via the Azure portal, CLI, or API. This tool is particularly useful for production environments where upgrade reliability is critical. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=563786).

**Details**:

**Azure Update Report: Public Preview – Pre-upgrade Validation Checks for Azure Database for PostgreSQL**

**Background and Purpose of the Update:**  
Major Version Upgrades (MVU) for Azure Database for PostgreSQL flexible server are critical for maintaining security, performance, and access to new features. However, MVUs can introduce compatibility issues or operational disruptions if the database or its configurations are not ready for the new version. The purpose of this update is to enable IT professionals to proactively assess their PostgreSQL flexible server’s readiness for a major version upgrade, reducing risk and improving upgrade reliability.

**Specific Features and Detailed Changes:**  
This update introduces new pre-upgrade validation checks for Azure Database for PostgreSQL flexible server. Users can now independently execute upgrade compatibility validation before starting the actual MVU process. The validation checks examine the server and its database objects for potential incompatibilities with the target major version, such as deprecated features, unsupported extensions, or configuration settings that may not be compatible with the new version.

**Technical Mechanisms and Implementation Methods:**  
The pre-upgrade validation is implemented as a self-service feature within the Azure portal and/or via Azure CLI/REST API. When invoked, the validation process runs a series of automated checks against the current PostgreSQL server instance. These checks analyze database schema, extensions, and configuration parameters to identify issues that could prevent a successful upgrade. The results are presented as a compatibility report, detailing any detected problems and providing guidance on remediation steps.

**Use Cases and Application Scenarios:**  
- **Proactive Upgrade Planning:** IT teams can run validation checks well ahead of scheduled maintenance windows, allowing time to resolve compatibility issues.
- **Risk Mitigation:** By identifying potential blockers before the upgrade, organizations can avoid unexpected downtime or data loss.
- **Compliance and Best Practices:** Enterprises with strict change management policies can use validation reports as part of their documentation and approval workflows.
- **Dev/Test Environments:** Developers can validate upgrade readiness in test environments before applying changes to production.

**Important Considerations and Limitations:**  
- The feature is currently in Public Preview, so it may not support all PostgreSQL versions or configurations.
- Validation checks are limited to compatibility issues detectable by automated analysis; manual review may still be necessary for complex scenarios.
- The process does not perform the actual upgrade; it only assesses readiness and highlights potential issues.
- Remediation of detected issues is the responsibility of the user, and some issues may require significant changes to database schema or application code.

**Integration with Related Azure Services:**  
Pre-upgrade validation checks are integrated with Azure Database for PostgreSQL flexible server management workflows. Results can be accessed via the Azure portal, and may be incorporated into automation scripts using Azure CLI or REST API. This feature complements Azure’s broader database management and monitoring capabilities, such as Azure Advisor, Azure Monitor, and automated backup/restore, by providing targeted upgrade readiness insights.

**Summary Sentence:**  
Azure Database for PostgreSQL flexible server now offers pre-upgrade validation checks in Public Preview, enabling IT professionals to proactively assess and address major version upgrade compatibility issues before initiating the upgrade process.

---

### 36. Public Preview: Microsoft Defender security assessments for Azure Database for PostgreSQL

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Microsoft Defender security assessments for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=563781)

**Update ID**: 563781
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Defender security assessments are now available in public preview for Azure Database for PostgreSQL.

- Key changes or new features  
This update introduces continuous security posture assessments for Azure Database for PostgreSQL. The assessments automatically identify potential vulnerabilities and misconfigurations in your PostgreSQL databases. Recommendations are provided to help remediate detected issues and strengthen database security. Integration with Microsoft Defender for Cloud enables centralized visibility and management of security findings.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL instances, especially those responsible for database security, compliance, and operational risk management.

- Important notes if any  
The feature is currently in public preview and may be subject to changes before general availability. It is recommended to review the assessment results regularly and implement suggested remediations to maintain a strong security posture. Integration with existing security workflows in Microsoft Defender for Cloud can help streamline incident response and compliance efforts.

For more details, refer to the official update: https://azure.microsoft.com/updates?id=563781

**Details**:

**Background and Purpose of the Update**  
This update introduces the public preview of Microsoft Defender security assessments for Azure Database for PostgreSQL. The primary objective is to enable organizations to continuously monitor and evaluate the security posture of their PostgreSQL databases hosted on Azure. By identifying potential vulnerabilities and misconfigurations, this feature supports proactive risk mitigation and helps maintain compliance with organizational and regulatory security standards.

**Specific Features and Detailed Changes**  
With this update, Microsoft Defender now extends its security assessment capabilities to Azure Database for PostgreSQL. Key features include:
- **Continuous Security Posture Evaluation:** The service automatically and regularly assesses the security configuration of PostgreSQL databases.
- **Vulnerability and Misconfiguration Detection:** It identifies security weaknesses, such as insecure settings, missing updates, or other configuration issues that could expose the database to threats.
- **Actionable Recommendations:** The assessments provide guidance on how to remediate detected issues, helping database administrators and security teams to strengthen their security controls.

**Technical Mechanisms and Implementation Methods**  
The security assessments are powered by Microsoft Defender for Cloud. Once enabled for Azure Database for PostgreSQL, Defender leverages built-in security policies and best practices to scan and analyze database configurations. The assessment engine evaluates parameters such as network exposure, authentication settings, and other security-related configurations. Findings are surfaced in the Azure portal, where users can review detected issues and follow recommended remediation steps.

**Use Cases and Application Scenarios**  
- **Continuous Compliance Monitoring:** Organizations subject to compliance requirements can use these assessments to ensure their PostgreSQL databases adhere to internal and external security standards.
- **Proactive Risk Management:** Security teams can leverage the continuous evaluation to detect and remediate vulnerabilities before they are exploited.
- **Operational Efficiency:** Database administrators can streamline security operations by receiving prioritized and actionable recommendations directly within the Azure portal.

**Important Considerations and Limitations**  
- **Public Preview:** As this feature is in public preview, it may not yet be suitable for production-critical environments. Users should evaluate the feature in test or development environments and monitor for updates regarding general availability.
- **Scope:** The assessments are specific to Azure Database for PostgreSQL and may not cover other database types or self-hosted PostgreSQL instances.
- **Remediation Responsibility:** While Defender provides recommendations, actual remediation actions must be performed by database administrators or security teams.

**Integration with Related Azure Services**  
- **Microsoft Defender for Cloud:** The assessments are integrated into the Defender for Cloud platform, allowing unified visibility and management of security findings across multiple Azure resources.
- **Azure Portal Integration:** All findings and recommendations are accessible via the Azure portal, enabling seamless workflow integration for IT and security professionals.
- **Security Center Reporting:** Results can be incorporated into broader security reports and dashboards, supporting organizational security governance and reporting requirements.

**Summary**  
The public preview of Microsoft Defender security assessments for Azure Database for PostgreSQL enables continuous evaluation of database security posture, identification of vulnerabilities and misconfigurations, and provides actionable recommendations to strengthen security within the Azure ecosystem.

---

### 37. Public Preview: Azure Database PostgreSQL - Flexible Server cross-tenant customer-managed keys

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Database PostgreSQL - Flexible Server cross-tenant customer-managed keys](https://azure.microsoft.com/updates?id=563776)

**Update ID**: 563776
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports cross-tenant customer-managed keys (CMK) in public preview.

- Key changes or new features  
You can now encrypt data at rest in Azure Database for PostgreSQL – Flexible Server using an Azure Key Vault key that resides in a different Microsoft Entra tenant than the database resource. This enables organizations to separate key management from data resources, supporting multi-tenant architectures and scenarios where key ownership and data ownership are managed by different entities.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL – Flexible Server, especially those in organizations with strict compliance requirements, multi-tenant environments, or those who need to separate key management from data management.

- Important notes if any  
This feature is in public preview and may not be suitable for production workloads. Proper permissions are required to access the cross-tenant Key Vault. Review Azure documentation for configuration steps and limitations. This update enhances compliance and security options for organizations with complex tenant and key management needs.

[Learn more](https://azure.microsoft.com/updates?id=563776)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Database PostgreSQL - Flexible Server cross-tenant customer-managed keys

**Background and Purpose of the Update:**  
Azure Database for PostgreSQL – Flexible Server has introduced support for cross-tenant customer-managed keys (CMK) in public preview. The primary purpose of this update is to enhance data security and control by allowing organizations to encrypt data at rest using keys stored in an Azure Key Vault located in a different Microsoft Entra tenant than the database server. This addresses scenarios where key management and database resources are intentionally separated across organizational boundaries or subsidiaries for compliance, security, or operational reasons.

**Specific Features and Detailed Changes:**  
The new feature enables encryption of PostgreSQL Flexible Server data at rest with a customer-managed key from an Azure Key Vault in a separate Microsoft Entra tenant. Previously, CMK support was limited to Key Vaults within the same tenant as the database server. With this update, administrators can specify a Key Vault and key from another tenant, providing greater flexibility in key management and supporting advanced multi-tenant architectures.

**Technical Mechanisms and Implementation Methods:**  
The implementation leverages Azure Key Vault and Microsoft Entra ID (formerly Azure Active Directory) for secure key management and access control. When configuring cross-tenant CMK, administrators must establish trust and permissions between the database server’s tenant and the Key Vault’s tenant. This typically involves:

- Granting the necessary permissions in the Key Vault to the managed identity or service principal associated with the PostgreSQL server in the source tenant.
- Configuring access policies in the Key Vault to allow key operations (such as wrap/unwrap) from the external tenant.
- Specifying the Key Vault URI and key identifier during server provisioning or configuration.

Azure ensures that all cryptographic operations required for data encryption and decryption are performed using the specified customer-managed key, without exposing the key material to the database server.

**Use Cases and Application Scenarios:**  
This feature is particularly valuable in the following scenarios:

- **Multi-tenant SaaS providers:** Where key management is centralized in a parent tenant, but databases are deployed in customer-specific tenants.
- **Subsidiary or organizational separation:** Enterprises with multiple subsidiaries or business units may keep key management in a central security tenant while deploying databases in operational tenants.
- **Compliance and regulatory requirements:** Organizations needing strict separation of duties or key ownership for compliance purposes can now enforce these policies across tenant boundaries.

**Important Considerations and Limitations:**  
- The feature is currently in public preview and may not be suitable for production workloads until general availability.
- Proper configuration of Microsoft Entra permissions and Key Vault access policies is critical; misconfiguration can result in failed encryption or access issues.
- Cross-tenant CMK support is limited to Azure Database for PostgreSQL – Flexible Server and may not be available for other Azure database services.
- Key rotation and management processes must account for cross-tenant access and potential changes in tenant relationships.

**Integration with Related Azure Services:**  
This update integrates Azure Database for PostgreSQL – Flexible Server with Azure Key Vault and Microsoft Entra ID for cross-tenant key management. It enables advanced scenarios where database and key management resources are distributed across multiple tenants, leveraging Azure’s identity and access management capabilities for secure and compliant operations.

**Summary Sentence:**  
Azure Database for PostgreSQL – Flexible Server now supports cross-tenant customer-managed keys in public preview, enabling organizations to encrypt data at rest using keys stored in an Azure Key Vault located in a different Microsoft Entra tenant, thereby enhancing security and flexibility in key management across tenant boundaries.

---

### 38. Generally Available: Azure Database for PostgreSQL flexible server pg_ivm extension

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL flexible server pg_ivm extension](https://azure.microsoft.com/updates?id=563771)

**Update ID**: 563771
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now supports the pg_ivm extension as generally available.

- Key changes or new features  
Customers can now install and use the pg_ivm (Incremental View Maintenance) extension on Azure Database for PostgreSQL Flexible Server. This extension enables materialized views to be updated incrementally, improving query performance and reducing the overhead of full view refreshes.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure, especially those leveraging materialized views for analytics, reporting, or data warehousing scenarios.

- Important notes if any  
To use the pg_ivm extension, ensure your PostgreSQL flexible server is running a compatible version. The extension must be installed and enabled per database. This feature can help optimize workloads that rely on frequent materialized view updates, but users should review the extension’s documentation for limitations and best practices. For more details, refer to the official Azure Update: [Azure Database for PostgreSQL flexible server pg_ivm extension](https://azure.microsoft.com/updates?id=563771).

**Details**:

**Azure Update Report: General Availability of pg_ivm Extension for Azure Database for PostgreSQL Flexible Server**

**Background and Purpose of the Update:**  
This update announces the general availability of the pg_ivm extension for Azure Database for PostgreSQL flexible server. The purpose of this release is to enable customers to install and use the pg_ivm extension, thereby enhancing the capabilities of PostgreSQL instances hosted on Azure's flexible server platform.

**Specific Features and Detailed Changes:**  
With this update, users can now install the pg_ivm extension directly within their Azure Database for PostgreSQL flexible server environments. The pg_ivm extension provides additional functionality to PostgreSQL databases, which is now fully supported in the flexible server deployment option. This update does not mention any other changes to the core database service or its management interfaces.

**Technical Mechanisms and Implementation Methods:**  
The pg_ivm extension is made available as an installable PostgreSQL extension within the flexible server environment. Users can enable the extension using standard PostgreSQL commands (e.g., `CREATE EXTENSION pg_ivm;`) once connected to their database instance. The extension is integrated into the Azure Database for PostgreSQL flexible server platform, ensuring compatibility and support within the managed service context. The installation and management of the extension are handled through the PostgreSQL extension management system, leveraging Azure’s platform capabilities for reliability and security.

**Use Cases and Application Scenarios:**  
This update is relevant for technical professionals who require advanced PostgreSQL extension support in their managed database environments. Typical use cases include scenarios where the pg_ivm extension is needed to enhance database functionality, such as supporting specific application requirements or optimizing query performance. The ability to install pg_ivm allows organizations to leverage its features without managing on-premises infrastructure or custom PostgreSQL builds.

**Important Considerations and Limitations:**  
The update specifies that the pg_ivm extension can be installed in Azure Database for PostgreSQL flexible server. There are no additional considerations or limitations mentioned in the update content. Users should refer to official Azure and pg_ivm documentation for compatibility, versioning, and operational guidelines to ensure proper usage within their environments.

**Integration with Related Azure Services:**  
The pg_ivm extension is available within the Azure Database for PostgreSQL flexible server, which can be integrated with other Azure services such as Azure Virtual Network, Azure Key Vault, and Azure Monitor for enhanced security, management, and monitoring. The extension operates within the managed database instance and does not require changes to other Azure services for its installation or operation.

**Summary Sentence:**  
Azure Database for PostgreSQL flexible server now supports the installation of the pg_ivm extension, enabling customers to enhance their PostgreSQL database capabilities within a fully managed Azure environment.

---

### 39. Public Preview: Foundry Memory preview refresh

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Foundry Memory preview refresh](https://azure.microsoft.com/updates?id=563616)

**Update ID**: 563616
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Foundry Memory public preview has been refreshed, introducing a redesigned storage model, enhanced retrieval controls, and deeper integration with the Foundry Agent Service.

- Key changes or new features  
  - Redesigned storage model for improved data handling and scalability.  
  - New retrieval controls, allowing more precise and flexible data access.  
  - Tighter integration with the Foundry Agent Service tool, streamlining agent workflows.  
  - Agents can now write, search, and update user-scoped data more efficiently.

- Target audience affected  
Developers and IT professionals building or managing solutions with Microsoft Foundry, especially those leveraging Foundry Agents and Memory for user data storage and retrieval.

- Important notes if any  
This update is in public preview, so features and APIs may change before general availability. Developers should review the updated documentation and test integrations to ensure compatibility. Enhanced retrieval and storage capabilities can improve application performance and user experience, but may require code or configuration updates.  

For more details, see the official update: https://azure.microsoft.com/updates?id=563616

**Details**:

**Azure Update Technical Report: Public Preview – Foundry Memory Preview Refresh**

**Background and Purpose of the Update:**  
The Foundry Memory public preview refresh is part of Microsoft’s ongoing efforts to enhance the capabilities of the Foundry platform, specifically targeting agent-based applications that require efficient, user-scoped memory management. The update aims to improve how agents interact with memory storage, retrieval, and update operations, thereby enabling more robust and context-aware agent behaviors.

**Specific Features and Detailed Changes:**  
- **Redesigned Storage Model:** The refresh introduces a new storage architecture for Foundry Memory. This redesign is intended to optimize how agents persist and manage user-scoped data, likely improving performance, scalability, and reliability.
- **New Retrieval Controls:** Enhanced retrieval mechanisms give agents finer control over how stored memories are accessed. This can facilitate more precise and contextually relevant data retrieval, supporting advanced agent logic and user personalization.
- **Tighter Integration with Foundry Agent Service:** The update deepens the integration between Foundry Memory and the Foundry Agent Service tool surface. This allows agents to seamlessly write, search, and update user-scoped data within the same operational context, streamlining development and operational workflows.

**Technical Mechanisms and Implementation Methods:**  
- Agents can now leverage the updated Foundry Memory APIs to perform CRUD (Create, Read, Update, Delete) operations on user-scoped memory objects.
- The redesigned storage model likely introduces new data structures or indexing strategies to optimize search and update operations, though specific implementation details are not disclosed.
- Integration with the Foundry Agent Service ensures that memory operations are accessible directly from the agent’s execution environment, reducing the need for custom integrations or external storage management.

**Use Cases and Application Scenarios:**  
- **Personalized Agent Experiences:** Agents can maintain persistent, user-specific context across sessions, enabling personalized interactions and recommendations.
- **Contextual Data Management:** Scenarios where agents need to recall previous user interactions, preferences, or historical data benefit from efficient memory retrieval and update capabilities.
- **Dynamic Workflow Adaptation:** Agents can update user-scoped memory in real time, supporting adaptive workflows and decision-making based on evolving user data.

**Important Considerations and Limitations:**  
- As this is a public preview, the features and APIs are subject to change and may not be suitable for production workloads.
- Users should expect potential limitations in terms of scalability, performance, or API stability during the preview phase.
- Detailed documentation on migration paths from previous storage models, if applicable, should be reviewed to ensure compatibility.

**Integration with Related Azure Services:**  
- The update is tightly coupled with the Foundry Agent Service, enhancing the overall agent development and deployment experience within the Azure ecosystem.
- While not explicitly stated, the improved storage model and retrieval controls may facilitate better interoperability with other Azure data services, depending on future integrations.

**Summary:**  
The Foundry Memory public preview refresh introduces a redesigned storage model, new retrieval controls, and enhanced integration with the Foundry Agent Service, enabling agents to efficiently write, search, and update user-scoped data for improved context management and personalized experiences.

---

### 40. Public Preview: Purview admin access auditing for sensitivity-labeled content in Azure AI Search

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Purview admin access auditing for sensitivity-labeled content in Azure AI Search](https://azure.microsoft.com/updates?id=563606)

**Update ID**: 563606
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search now supports Microsoft Purview admin access auditing for sensitivity-labeled content, available in public preview.

- Key changes or new features  
Admin operations involving Purview-labeled documents within Azure AI Search, knowledge retrieval, and Foundry IQ knowledge bases are now audited. These audit logs are integrated into Microsoft Purview, providing visibility and traceability of administrative actions on sensitive data.

- Target audience affected  
Developers and IT professionals managing sensitive or regulated data in Azure AI Search, especially those using Microsoft Purview for data governance and compliance.

- Important notes if any  
This feature enhances compliance and security monitoring by allowing organizations to track admin access to sensitive, labeled documents. It is currently in public preview, so it may not be suitable for production workloads. Integration with Microsoft Purview enables centralized auditing and reporting, supporting regulatory requirements and internal governance policies.

[Learn more](https://azure.microsoft.com/updates?id=563606)

**Details**:

**Azure Update Report: Public Preview – Purview Admin Access Auditing for Sensitivity-Labeled Content in Azure AI Search**

**Background and Purpose of the Update:**  
This update introduces Microsoft Purview admin access auditing for sensitivity-labeled content within Azure AI Search, now available in public preview. The primary goal is to enhance compliance and security by providing visibility into administrative operations involving documents labeled with sensitivity information via Microsoft Purview. This capability addresses the need for organizations to monitor and audit access to sensitive data, ensuring regulatory and internal policy adherence.

**Specific Features and Detailed Changes:**  
- **Admin Operation Auditing:** Administrative actions performed on Purview-labeled documents within Azure AI Search, including knowledge retrieval and Foundry IQ knowledge bases, are now auditable.
- **Audit Log Integration:** These admin operations are captured and flow into Microsoft Purview’s audit logs, providing a centralized and consistent audit trail for sensitive content management activities.
- **Scope:** The auditing covers any admin-level interaction with documents that have been classified and labeled for sensitivity using Microsoft Purview within the Azure AI Search environment.

**Technical Mechanisms and Implementation Methods:**  
- **Audit Event Generation:** When an admin interacts with Purview-labeled content in Azure AI Search (such as viewing, modifying, or managing documents), an audit event is generated.
- **Audit Log Flow:** These events are transmitted to Microsoft Purview’s audit log infrastructure, leveraging Purview’s native auditing and monitoring capabilities.
- **Label Recognition:** Azure AI Search recognizes sensitivity labels applied via Purview and triggers auditing mechanisms specifically for these labeled documents.
- **Integration Points:** The auditing mechanism is tightly integrated with Azure AI Search’s document management and Purview’s labeling and auditing APIs, ensuring seamless operation.

**Use Cases and Application Scenarios:**  
- **Regulatory Compliance:** Organizations subject to regulatory requirements (e.g., GDPR, HIPAA) can now demonstrate and monitor administrative access to sensitive information stored in Azure AI Search.
- **Internal Security Monitoring:** Security teams can track and review admin actions on sensitive documents, supporting internal investigations and risk management.
- **Knowledge Base Governance:** Enterprises using Foundry IQ or similar knowledge bases can ensure that sensitive knowledge assets are properly monitored when accessed or managed by administrators.

**Important Considerations and Limitations:**  
- **Public Preview Status:** This feature is currently in public preview, which may imply limited support, potential changes, and the need for validation in production environments.
- **Scope Limitation:** Auditing is specifically for admin operations on Purview-labeled documents; actions on unlabeled or non-Purview-labeled content are not covered by this feature.
- **Integration Requirements:** Proper configuration of Purview sensitivity labels and Azure AI Search is required to ensure audit events are generated and captured.

**Integration with Related Azure Services:**  
- **Microsoft Purview:** Central to this update, Purview provides the sensitivity labeling and audit log management infrastructure.
- **Azure AI Search:** Acts as the content repository and search platform where labeled documents reside and are managed.
- **Foundry IQ Knowledge Bases:** Supported as part of the knowledge retrieval scenarios, ensuring that knowledge assets are included in the auditing scope.

**Summary:**  
Azure AI Search now supports Microsoft Purview admin access auditing for sensitivity-labeled content in public preview, enabling organizations to monitor and audit administrative operations on sensitive documents for enhanced compliance and security.

---

### 41. Public Preview: Hosted Agents in Microsoft Foundry Agent Service

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Hosted Agents in Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=563596)

**Update ID**: 563596
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry Agent Service now offers Hosted Agents in public preview, enabling developers to run their own agent code on Microsoft-managed infrastructure.

- Key changes or new features  
  - Hosted Agents provide a container-based runtime environment where developers can deploy custom agent code written in any framework or language.  
  - Each Hosted Agent operates in an isolated, per-session virtual machine instance, enhancing security and resource isolation.  
  - The service abstracts away underlying infrastructure management, allowing users to focus on agent development and deployment.  
  - Hosted Agents support integration with existing Foundry workflows and APIs.

- Target audience affected  
  - Developers building custom agents or automation solutions that require flexible runtime environments.  
  - IT professionals responsible for managing agent infrastructure, security, and deployment pipelines.

- Important notes if any  
  - This is a public preview; features and performance may change before general availability.  
  - Hosted Agents are suitable for scenarios where code isolation, custom frameworks, or language flexibility are required.  
  - Review documentation for current limitations and onboarding steps.  
  - More details: [Azure Update link](https://azure.microsoft.com/updates?id=563596)

**Details**:

**Background and Purpose of the Update**  
The Public Preview of Hosted Agents in Microsoft Foundry Agent Service introduces a new container-based runtime environment. This update is designed to provide developers with the flexibility to bring their own agent code, written in any framework, and deploy it on Microsoft-managed infrastructure. The main objective is to streamline the deployment and management of custom agent workloads by leveraging a fully managed, scalable, and secure platform.

**Specific Features and Detailed Changes**  
- **Hosted Agents:** Developers can now package their agent code as containers and deploy them as Hosted Agents within the Foundry Agent Service.
- **Framework Agnostic:** The service supports agent code written in any framework, removing language or runtime constraints.
- **Microsoft-Managed Infrastructure:** Hosted Agents run on infrastructure managed by Microsoft, reducing operational overhead for users.
- **Per-Session VM Isolation:** Each Hosted Agent is executed within a dedicated, per-session virtual machine instance, enhancing security and isolation for each agent session.

**Technical Mechanisms and Implementation Methods**  
- **Container-Based Runtime:** The Hosted Agents leverage containerization technology, allowing developers to encapsulate their agent code and dependencies within a container image.
- **Session-Based VM Provisioning:** When a Hosted Agent is initiated, the Foundry Agent Service provisions a new VM instance for the session, deploys the container, and manages the agent lifecycle.
- **Managed Agent Execution:** The service handles the orchestration, scaling, and teardown of agent sessions, ensuring that resources are allocated efficiently and securely.

**Use Cases and Application Scenarios**  
- **Custom Workflow Automation:** Organizations can implement custom automation agents for CI/CD pipelines, DevOps tasks, or other workflow automation scenarios without being restricted to predefined agent environments.
- **Multi-Framework Support:** Teams working with diverse technology stacks can standardize agent deployment processes, regardless of programming language or framework.
- **Ephemeral and Isolated Workloads:** Security-sensitive operations benefit from the per-session VM isolation, ensuring that each agent execution is sandboxed from others.

**Important Considerations and Limitations**  
- **Preview Release:** As this feature is in Public Preview, it may not be suitable for production workloads and could be subject to changes or limitations in support and SLAs.
- **Session-Based Resource Allocation:** Each agent session consumes a dedicated VM, which may have implications for resource usage and cost.
- **Containerization Requirements:** Developers must package their agent code as containers, which may require adjustments to existing codebases or build processes.

**Integration with Related Azure Services**  
- **Azure DevOps and Automation:** Hosted Agents can be integrated into Azure DevOps pipelines or other automation workflows, providing a flexible alternative to standard Microsoft-hosted agents.
- **Azure Container Registry:** Developers can store and manage their agent container images in Azure Container Registry for streamlined deployment.
- **Security and Compliance:** By leveraging Microsoft-managed infrastructure and per-session VM isolation, organizations can align with security and compliance requirements for agent execution.

**Summary**  
The Public Preview of Hosted Agents in Microsoft Foundry Agent Service enables developers to deploy containerized agent code in any framework on Microsoft-managed, per-session VM infrastructure, providing flexibility, isolation, and simplified management for custom automation and workflow scenarios.

---

### 42. Public Preview: Purview sensitivity labels in Azure AI Search knowledge sources

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Purview sensitivity labels in Azure AI Search knowledge sources](https://azure.microsoft.com/updates?id=563591)

**Update ID**: 563591
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- **What was updated**  
Azure AI Search now supports Microsoft Purview sensitivity labels for knowledge sources in public preview.

- **Key changes or new features**  
Sensitivity labels applied in source systems (e.g., SharePoint, OneDrive, Exchange) are now preserved and flow through the ingestion process into Azure AI Search. These labels are also maintained within knowledge bases that underpin Foundry agents and copilots. This integration enables automated data classification and enhanced data governance, ensuring that sensitive information remains protected and properly labeled throughout the AI search and knowledge management lifecycle.

- **Target audience affected**  
Developers and IT professionals who build or manage Azure AI Search solutions, especially those integrating with Microsoft Purview for data governance and compliance. This is particularly relevant for organizations with strict regulatory or data protection requirements.

- **Important notes if any**  
This feature is currently in public preview and may not be suitable for production workloads. Review your organization’s data governance policies to ensure proper configuration and compliance. Integration with Purview sensitivity labels helps streamline security and compliance workflows, reducing manual labeling and risk of data exposure.

[Learn more](https://azure.microsoft.com/updates?id=563591)

**Details**:

**Azure Update Report: Public Preview – Purview Sensitivity Labels in Azure AI Search Knowledge Sources**

**Background and Purpose of the Update**  
Azure AI Search is a cloud-based search service that enables developers to build sophisticated search experiences over content. Microsoft Purview is an enterprise data governance solution that provides classification, labeling, and protection of sensitive information across Microsoft cloud services. The purpose of this update is to enhance data security and compliance within Azure AI Search by supporting Microsoft Purview sensitivity labels. This integration ensures that sensitivity labels applied in the source system are preserved and propagated during data ingestion into Azure AI Search, thereby maintaining consistent data governance and compliance throughout the data lifecycle.

**Specific Features and Detailed Changes**  
The main feature introduced in this public preview is the support for Microsoft Purview sensitivity labels within Azure AI Search knowledge sources. When data is ingested from a source system (such as SharePoint, SQL Database, or other supported repositories) into Azure AI Search, any sensitivity labels assigned in Purview are retained and transferred into the search index and knowledge bases. These knowledge bases are subsequently used to ground Foundry agents and copilots, ensuring that AI-driven applications are aware of and respect the sensitivity of the underlying data.

**Technical Mechanisms and Implementation Methods**  
The technical implementation involves the automatic flow of sensitivity labels from the source system into Azure AI Search during the ingestion process. This means that the metadata associated with each document or data item, specifically the Purview sensitivity label, is captured and stored within the Azure AI Search index. The ingestion pipeline is enhanced to recognize and preserve this metadata, making it accessible to downstream applications, such as Foundry agents and copilots, which use the knowledge base for generating responses or performing actions. The mechanism relies on integration points between Azure AI Search and Microsoft Purview, leveraging Purview’s labeling APIs and metadata management capabilities.

**Use Cases and Application Scenarios**  
- **Enterprise Search Solutions:** Organizations can build search solutions where sensitive information is automatically labeled and protected, ensuring compliance with internal and external regulations.
- **AI Copilot and Agent Grounding:** Foundry agents and copilots can utilize knowledge bases with sensitivity labels, enabling context-aware responses that respect data confidentiality.
- **Regulatory Compliance:** Businesses in regulated industries (finance, healthcare, etc.) can ensure that sensitive data is properly labeled and handled throughout AI-driven workflows.
- **Data Governance Automation:** IT departments can automate the propagation of sensitivity labels, reducing manual overhead and potential errors in data classification.

**Important Considerations and Limitations**  
- This feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes.
- Only sensitivity labels applied at the source system via Microsoft Purview are supported; custom labeling or unsupported sources may not propagate labels.
- Integration is dependent on the compatibility between the source system, Purview, and Azure AI Search ingestion pipelines.
- Users should verify label propagation and test compliance scenarios during the preview phase.

**Integration with Related Azure Services**  
This update strengthens the integration between Azure AI Search and Microsoft Purview, leveraging Purview’s sensitivity labeling and metadata management. It also enhances the capabilities of Foundry agents and copilots by grounding their knowledge bases with sensitivity-aware data. The update supports broader Azure data governance strategies, enabling seamless compliance across Azure data services.

**Summary Sentence**  
Azure AI Search now supports Microsoft Purview sensitivity labels in knowledge sources, enabling automatic label propagation during data ingestion and ensuring consistent data governance for search indexes and AI knowledge bases in public preview.

---

### 43. Public Preview: MAI-Transcribe-1.5 in Microsoft Foundry model catalog

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: MAI-Transcribe-1.5 in Microsoft Foundry model catalog](https://azure.microsoft.com/updates?id=563586)

**Update ID**: 563586
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
MAI-Transcribe-1.5, Microsoft’s next-generation speech-to-text model, has been added to the Microsoft Foundry model catalog and is now available in public preview.

- Key changes or new features  
The MAI-Transcribe-1.5 model delivers improved transcription accuracy, specifically achieving a noticeably lower word error rate on long-tail locales compared to previous versions. This enhancement benefits scenarios involving diverse accents, dialects, or less commonly supported languages.

- Target audience affected  
Developers and IT professionals building or maintaining applications that require speech-to-text capabilities, especially those working with global or multilingual user bases, will benefit from this update. Teams leveraging Microsoft Foundry’s model catalog for AI/ML workflows are directly impacted.

- Important notes if any  
The model is currently in public preview, so it may not yet be recommended for production-critical workloads. Developers are encouraged to test the new model’s performance and accuracy in their scenarios and provide feedback. Integration is available via the Microsoft Foundry API, and documentation should be reviewed for any changes in endpoints or usage patterns.

For more details, see the official update: https://azure.microsoft.com/updates?id=563586

**Details**:

**Comprehensive Technical Explanation: Public Preview of MAI-Transcribe-1.5 in Microsoft Foundry Model Catalog**

**Background and Purpose of the Update**  
Microsoft Foundry has introduced MAI-Transcribe-1.5 to its model catalog in public preview. This update is part of Microsoft’s ongoing efforts to advance speech-to-text capabilities, specifically targeting improved transcription accuracy. The primary purpose is to provide IT professionals and developers access to Microsoft’s next-generation speech-to-text model, enabling enhanced performance, especially in less common languages and dialects ("long-tail locales").

**Specific Features and Detailed Changes**  
MAI-Transcribe-1.5 offers several improvements over previous speech-to-text models:
- **Improved Accuracy:** The model delivers a noticeably lower word error rate, particularly for long-tail locales, which are languages or dialects with less representation in mainstream datasets.
- **Next-Generation Model:** As a successor to earlier versions, MAI-Transcribe-1.5 incorporates advancements in model architecture and training data, resulting in more reliable transcription outputs.

**Technical Mechanisms and Implementation Methods**  
The MAI-Transcribe-1.5 model is accessible via the Microsoft Foundry platform, which serves as a catalog for AI models. While specific architectural details are not provided, the update highlights the model’s enhanced accuracy, implying improvements in underlying neural network design and possibly expanded training datasets.  
- **Deployment:** IT professionals can leverage MAI-Transcribe-1.5 through Microsoft Foundry’s APIs or integration points, allowing for seamless incorporation into custom applications or workflows.
- **Model Catalog Integration:** The public preview status means the model is available for testing and evaluation, enabling feedback and iterative improvements before general availability.

**Use Cases and Application Scenarios**  
MAI-Transcribe-1.5 is particularly suited for scenarios where accurate speech-to-text conversion is critical, including:
- **Transcription Services:** Automated transcription of meetings, interviews, or lectures, especially in less common languages or dialects.
- **Voice-Driven Applications:** Enhancing the accuracy of voice commands and interactions in applications targeting global audiences.
- **Accessibility Solutions:** Improving real-time captioning and accessibility features for users in diverse linguistic regions.
- **Content Indexing:** Enabling precise indexing and searchability of audio/video content in enterprise environments.

**Important Considerations and Limitations**  
- **Public Preview:** The model is in public preview, which means it may not be fully optimized or supported for production workloads. Users should validate performance and reliability in their specific scenarios.
- **Locale Coverage:** While improved for long-tail locales, the model’s performance may vary across languages and dialects. Testing is recommended to ensure suitability.
- **Feedback Loop:** As a preview release, Microsoft encourages feedback from users to refine the model before general availability.

**Integration with Related Azure Services**  
MAI-Transcribe-1.5 can be integrated with other Azure AI services, such as Azure Cognitive Services Speech API, for end-to-end speech processing solutions. IT professionals can leverage Microsoft Foundry’s catalog to select and deploy the model within Azure-based workflows, enhancing existing applications with improved transcription capabilities.

**Summary Sentence**  
Microsoft Foundry’s public preview release of MAI-Transcribe-1.5 introduces a next-generation speech-to-text model with significantly improved accuracy and lower word error rates for long-tail locales, enabling IT professionals to enhance transcription and voice-driven applications while evaluating the model’s performance for diverse linguistic scenarios.

---

### 44. Public Preview: MAI-Image-2.5 in Microsoft Foundry model catalog

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: MAI-Image-2.5 in Microsoft Foundry model catalog](https://azure.microsoft.com/updates?id=563581)

**Update ID**: 563581
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has released MAI-Image-2.5, the next-generation in-house image generation model, to its model catalog in public preview.

- Key changes or new features  
MAI-Image-2.5 offers significant improvements over the previous MAI-Image-2 model, including enhanced photorealism, better prompt fidelity (more accurate rendering of user prompts), and faster image generation speeds. The model is also tunable, allowing for further customization based on specific use cases.

- Target audience affected  
This update is relevant for developers, data scientists, and IT professionals who use Microsoft Foundry’s model catalog for building, integrating, or deploying AI-powered image generation solutions.

- Important notes if any  
The model is currently in public preview, so it may not be recommended for production workloads yet. Users are encouraged to test and provide feedback. Integration with Azure services enables streamlined experimentation and deployment. For more details and access, visit the [official update page](https://azure.microsoft.com/updates?id=563581).

**Details**:

**Azure Update Technical Explanation: Public Preview: MAI-Image-2.5 in Microsoft Foundry model catalog**

**Background and Purpose of the Update:**  
Microsoft Foundry has introduced MAI-Image-2.5, the latest generation of its proprietary image generation model, into the model catalog as a public preview. This update aims to provide users with enhanced capabilities for generating images, building upon the foundation established by the previous MAI-Image-2 model. The primary goal is to deliver improvements in image quality, prompt fidelity, and processing speed, thereby supporting advanced AI-driven image generation scenarios.

**Specific Features and Detailed Changes:**  
MAI-Image-2.5 introduces several notable enhancements over its predecessor:
- **Improved Photorealism:** The model generates images with higher visual fidelity and realism, making outputs more suitable for production and creative use cases.
- **Enhanced Prompt Fidelity:** There is a significant increase in the model’s ability to accurately interpret and reflect user prompts in the generated images, ensuring outputs are more aligned with user intent.
- **Faster Generation Speed:** The model delivers reduced latency and improved throughput, enabling quicker image generation for interactive and batch processing scenarios.
- **Catalog Availability:** MAI-Image-2.5 is now accessible via the Microsoft Foundry model catalog, allowing users to select and utilize the model directly within the Foundry environment.

**Technical Mechanisms and Implementation Methods:**  
MAI-Image-2.5 is implemented as a managed model within the Microsoft Foundry platform. Users can access the model through the model catalog, leveraging Foundry’s standardized interfaces for prompt submission and image retrieval. The model’s architecture and inference pipeline have been optimized for both quality and performance, though specific architectural details are not disclosed in this update. Integration with Foundry ensures seamless deployment, scaling, and management of the model in cloud-based workflows.

**Use Cases and Application Scenarios:**  
- **Content Creation:** Designers and content creators can use MAI-Image-2.5 to generate high-quality, photorealistic images for marketing materials, media, and digital assets.
- **Prototyping and Visualization:** Product teams can rapidly visualize concepts and prototypes by generating images from textual descriptions.
- **Automation Workflows:** Enterprises can integrate image generation into automated pipelines for tasks such as synthetic data generation, creative automation, and rapid prototyping.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As MAI-Image-2.5 is in public preview, it may be subject to changes and may not yet be suitable for production-critical workloads.
- **Model Tuning:** The update notes that the model is tunable, but specific tuning mechanisms or parameters are not detailed in the announcement.
- **Documentation and Support:** Users should consult Microsoft Foundry documentation for guidance on model integration, usage limits, and support during the preview phase.

**Integration with Related Azure Services:**  
MAI-Image-2.5 is available through the Microsoft Foundry model catalog, which is designed to integrate with other Azure AI services and workflows. Users can incorporate the model into broader Azure solutions, leveraging Foundry’s APIs and orchestration capabilities to combine image generation with data processing, storage, and analytics services within the Azure ecosystem.

**Summary:**  
MAI-Image-2.5 is now available in public preview within the Microsoft Foundry model catalog, offering improved photorealism, prompt fidelity, and generation speed for advanced image generation scenarios.

---

### 45. Public Preview: Serverless indexers in Azure AI Search

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Serverless indexers in Azure AI Search](https://azure.microsoft.com/updates?id=563531)

**Update ID**: 563531
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search introduced serverless native indexers, now available in public preview.

- Key changes or new features  
  - Serverless indexers eliminate the need to provision or manage dedicated indexer compute resources for data ingestion workflows.  
  - Indexer execution automatically scales based on workload demand, enabling dynamic resource allocation.  
  - Customers only pay for actual indexer usage, reducing costs associated with idle compute resources.

- Target audience affected  
  - Developers building search solutions with Azure AI Search who use indexers for data ingestion from various sources (e.g., Azure Blob Storage, Cosmos DB, SQL).  
  - IT professionals responsible for managing and optimizing search infrastructure and costs.

- Important notes  
  - This feature is currently in public preview and may not be suitable for production workloads.  
  - Serverless indexers simplify operational management and can help optimize costs, especially for workloads with variable or unpredictable ingestion patterns.  
  - Existing indexer APIs and workflows are supported, making migration straightforward.  
  - For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=563531).

**Details**:

**Azure Update Report: Public Preview – Serverless Indexers in Azure AI Search**

**Background and Purpose of the Update**  
Azure AI Search traditionally required customers to provision and manage dedicated compute resources for indexer operations, which are responsible for ingesting data from various sources into search indexes. This approach often led to inefficiencies, such as paying for idle compute when ingestion workloads were sporadic or variable. The new serverless option for native indexers addresses this challenge by eliminating the need for manual compute provisioning and management, thereby optimizing cost and operational overhead.

**Specific Features and Detailed Changes**  
With the introduction of serverless indexers in public preview, Azure AI Search now enables customers to execute indexer workflows without allocating dedicated compute resources. Indexer execution automatically scales according to workload demand, ensuring that customers only pay for actual ingestion activity rather than idle capacity. This update applies specifically to native indexers, which are built-in components for ingesting data from supported sources into Azure AI Search indexes.

**Technical Mechanisms and Implementation Methods**  
The serverless indexer model leverages Azure’s underlying serverless infrastructure to dynamically allocate compute resources for indexer execution. When an ingestion workflow is triggered, Azure provisions the required compute on-demand, executes the indexer job, and deallocates resources upon completion. This mechanism abstracts away infrastructure management from the user, providing a fully managed experience for data ingestion. The scaling is handled automatically, based on the volume and frequency of ingestion requests, ensuring efficient resource utilization.

**Use Cases and Application Scenarios**  
Serverless indexers are ideal for scenarios where ingestion workloads are unpredictable, intermittent, or bursty. Examples include:
- Periodic ingestion of data from external databases, blob storage, or other supported sources.
- Event-driven indexing, such as updating search indexes in response to changes in upstream data sources.
- Development and testing environments where ingestion activity is sporadic and does not justify dedicated compute resources.
- Multi-tenant applications with varying ingestion patterns across tenants.

**Important Considerations and Limitations**  
As this feature is in public preview, customers should be aware of potential limitations:
- The serverless indexer option currently applies only to native indexers within Azure AI Search.
- Preview features may not be suitable for production workloads due to possible changes, limited support, or constraints in functionality.
- Pricing is based on actual indexer execution, but detailed billing information and quotas should be reviewed in the official documentation.
- Customers should monitor ingestion performance and reliability, as preview features may have evolving SLAs.

**Integration with Related Azure Services**  
Serverless indexers in Azure AI Search can be seamlessly integrated with other Azure services that provide data sources for indexing, such as Azure Blob Storage, Azure SQL Database, and Cosmos DB. The serverless model simplifies ingestion workflows by removing the need to coordinate compute provisioning across services. Additionally, this update aligns with Azure’s broader serverless strategy, enabling customers to build scalable, cost-efficient solutions across the Azure ecosystem.

**Summary Sentence**  
Azure AI Search now offers serverless native indexers in public preview, enabling automatic scaling and eliminating the need for dedicated compute provisioning for ingestion workflows, thereby optimizing cost and operational efficiency.

---

### 46. Public Preview: Neural HD voice update (HDv2.5) in Azure AI Speech

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Neural HD voice update (HDv2.5) in Azure AI Speech](https://azure.microsoft.com/updates?id=563526)

**Update ID**: 563526
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Speech has released the Neural HD voice update (HDv2.5) for its text-to-speech (TTS) service in public preview, transitioning customers from the previous DragonHDLatest model.

- Key changes or new features  
  - Improved audio quality: HDv2.5 delivers higher audio quality scores for synthesized speech.  
  - Enhanced expressiveness: English voices now support style and paralinguistic tags, enabling more natural and expressive speech output.  
  - Reduced word error rate: The update decreases transcription errors, improving overall accuracy.

- Target audience affected  
Developers and IT professionals integrating Azure AI Speech TTS capabilities into their applications, especially those requiring high-fidelity, expressive English voice synthesis.

- Important notes if any  
  - The update is currently in public preview; production workloads should monitor for any changes before general availability.  
  - Developers using the DragonHDLatest model will be transitioned to HDv2.5 and should test their applications for compatibility and quality improvements.  
  - New style and paralinguistic tags may require minor code changes to leverage enhanced expressiveness.  
  - Review the official documentation for guidance on migration and feature usage.  

For more details, see the [official update](https://azure.microsoft.com/updates?id=563526).

**Details**:

**Azure Update Technical Explanation: Public Preview – Neural HD Voice Update (HDv2.5) in Azure AI Speech**

**Background and Purpose of the Update**  
Azure AI Speech is enhancing its text-to-speech (TTS) capabilities by introducing an updated Neural HD voice model, HDv2.5, in public preview. This update transitions customers from the previous DragonHDLatest model to HDv2.5. The primary purpose is to deliver higher audio quality, improved expressiveness, and greater accuracy in synthesized speech, thereby meeting advanced requirements for natural and intelligible voice output in enterprise and developer applications.

**Specific Features and Detailed Changes**  
- **Audio Quality Improvement:** The HDv2.5 model increases audio quality scores, indicating more natural and clear speech synthesis compared to DragonHDLatest.
- **Style and Paralinguistic Tag Support:** HDv2.5 introduces support for style and paralinguistic tags specifically for English voices. This enables developers to control expressive elements such as speaking style, tone, and non-verbal cues within the generated speech.
- **Reduced Word Error Rate:** The update reduces word error rate, improving the accuracy of pronunciation and intelligibility in the output audio.

**Technical Mechanisms and Implementation Methods**  
- **Model Upgrade:** The transition from DragonHDLatest to HDv2.5 involves deploying a new neural network-based TTS model. This model leverages advanced deep learning architectures to synthesize speech with higher fidelity and nuanced expressiveness.
- **Tag Processing:** The model interprets style and paralinguistic tags embedded in the input text, adjusting prosody, intonation, and other speech parameters accordingly for English voices.
- **API Integration:** The updated model is accessible via Azure AI Speech’s text-to-speech API endpoints. Existing integrations using DragonHDLatest can migrate to HDv2.5 by specifying the new model in API requests.

**Use Cases and Application Scenarios**  
- **Conversational AI:** Enhanced voice quality and expressiveness benefit virtual assistants, chatbots, and interactive voice response (IVR) systems requiring natural human-like interactions.
- **Content Creation:** Media, e-learning, and accessibility solutions can leverage style and paralinguistic tags to produce engaging and contextually appropriate audio content.
- **Accessibility:** Improved accuracy and clarity assist in generating speech for users with visual impairments or reading difficulties.

**Important Considerations and Limitations**  
- **Language Support:** Style and paralinguistic tag support is currently limited to English voices.
- **Model Selection:** Customers must explicitly select HDv2.5 in their API requests to utilize the new features and quality improvements.
- **Preview Status:** As this is a public preview, the model may undergo further changes and is not recommended for production-critical workloads without appropriate validation.

**Integration with Related Azure Services**  
- **Azure AI Speech:** HDv2.5 is a direct enhancement to the Azure AI Speech service, fully compatible with its existing TTS API.
- **Azure Cognitive Services:** The update can be integrated with other Cognitive Services, such as Language Understanding (LUIS) or Speech-to-Text, to build comprehensive voice-driven applications.
- **Azure Bot Services:** Developers can use HDv2.5 to provide more natural and expressive voice output in bot frameworks and conversational interfaces.

**Summary**  
Azure AI Speech’s Neural HDv2.5 model, now in public preview, offers improved audio quality, support for expressive tags in English, and reduced word error rates, enabling more natural and accurate text-to-speech experiences for a wide range of applications.

---

### 47. Public Preview: Toolbox connectors and triggers in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Toolbox connectors and triggers in Microsoft Foundry](https://azure.microsoft.com/updates?id=563456)

**Update ID**: 563456
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has introduced connectors and time-based triggers to the Foundry Tools toolbox, now available in public preview.

- Key changes or new features  
  - Native support for connectors and time-based triggers enables enterprise developers and automation engineers to build event-driven AI agents directly within Microsoft Foundry.  
  - Previously, Foundry agents could only be invoked through direct API calls; with this update, agents can now be triggered by external events or scheduled intervals.  
  - The toolbox expansion allows integration with various data sources and services, facilitating more complex and automated workflows.

- Target audience affected  
Enterprise developers, automation engineers, and IT professionals building AI-driven automation solutions using Microsoft Foundry.

- Important notes  
  - This feature is currently in public preview, so it may not be suitable for production workloads.  
  - Developers can now create more flexible and responsive AI agents by leveraging event-based and scheduled triggers, reducing the need for manual or API-based invocations.  
  - Integration with connectors streamlines connectivity to external systems, enhancing automation capabilities within enterprise environments.

For more details, see the official update: https://azure.microsoft.com/updates?id=563456

**Details**:

**Azure Update Technical Explanation: Public Preview – Toolbox Connectors and Triggers in Microsoft Foundry**

**Background and Purpose of the Update**  
This update introduces connectors and time-based triggers to the Foundry Tools toolbox in Microsoft Foundry, now available in public preview. The primary goal is to provide enterprise developers and automation engineers with a native mechanism to build event-driven AI agents. Previously, Foundry agents could only be invoked directly, limiting automation and integration capabilities. This enhancement addresses the need for more flexible and automated agent invocation methods within enterprise environments.

**Specific Features and Detailed Changes**  
- **Connectors**: The update adds a set of connectors to the Foundry Tools toolbox. These connectors enable integration with external systems and data sources, allowing agents to interact with a broader range of enterprise resources.
- **Time-Based Triggers**: Time-based triggers are now available, enabling the scheduling of agent execution based on specific time intervals or schedules. This allows for the automation of repetitive tasks and periodic workflows.
- **Native Event-Driven Architecture**: With these additions, developers can now build agents that respond to events (such as data changes or scheduled times) rather than requiring manual or direct invocation.

**Technical Mechanisms and Implementation Methods**  
- **Connectors**: These are pre-built integration components that facilitate communication between Foundry agents and external services or data sources. They abstract the complexity of API calls and data transformations, providing a streamlined interface for developers.
- **Triggers**: Time-based triggers are implemented as part of the Foundry Tools toolbox, allowing developers to configure schedules (e.g., cron expressions or interval-based triggers) that automatically invoke agents at defined times.
- **Toolbox Integration**: Both connectors and triggers are natively integrated into the Foundry Tools toolbox, ensuring a unified development and configuration experience within Microsoft Foundry.

**Use Cases and Application Scenarios**  
- **Automated Data Processing**: Schedule agents to process data from connected sources at regular intervals, such as nightly data aggregation or transformation tasks.
- **Event-Driven AI Workflows**: Trigger AI agents in response to events detected via connectors, such as new entries in a database or updates in a CRM system.
- **Routine Task Automation**: Use time-based triggers to automate routine maintenance, reporting, or monitoring tasks without manual intervention.

**Important Considerations and Limitations**  
- **Public Preview**: As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate stability and support limitations before deploying in critical environments.
- **Scope of Connectors and Triggers**: The range of available connectors and the granularity of trigger scheduling may be limited during the preview phase. Users should consult the official documentation for supported integrations and configuration options.

**Integration with Related Azure Services**  
- **Azure Ecosystem**: The connectors enhance interoperability with other Azure services and external systems, enabling seamless data flow and event handling across the enterprise landscape.
- **Agent Orchestration**: By leveraging these toolbox features, organizations can orchestrate complex workflows involving multiple Azure services and Foundry agents, improving automation and efficiency.

**Summary**  
Microsoft Foundry now offers public preview support for connectors and time-based triggers in the Foundry Tools toolbox, enabling enterprise developers and automation engineers to build event-driven AI agents with native scheduling and integration capabilities.

---

### 48. Generally Available: Custom Avatar and Custom Video portal in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Custom Avatar and Custom Video portal in Microsoft Foundry](https://azure.microsoft.com/updates?id=563436)

**Update ID**: 563436
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Speech has made the Custom Avatar and Custom Video authoring experiences generally available within the Microsoft Foundry portal.

- Key changes or new features  
Approved customers can now use the Microsoft Foundry portal to:
  - Upload an actor’s video recording.
  - Fine-tune and create custom video avatars.
  - Generate synthetic talking head videos using these avatars.
This streamlines the process of building and deploying personalized AI-driven video content.

- Target audience affected  
This update is relevant for developers, AI engineers, and IT professionals working with Azure AI Speech, especially those building custom video or avatar solutions for applications such as virtual assistants, training, or digital content creation.

- Important notes if any  
- Access to these features is limited to approved customers; not all users have immediate access.
- The new portal experience simplifies the workflow for creating and managing custom avatars and synthetic videos.
- Developers should review compliance and responsible AI guidelines when using synthetic media features.

For more details, see the official update: https://azure.microsoft.com/updates?id=563436

**Details**:

**Azure Update Report: Generally Available – Custom Avatar and Custom Video Portal in Microsoft Foundry**

**Background and Purpose of the Update**  
Azure AI Speech has announced the general availability of Custom Avatar and Custom Video authoring experiences within the Microsoft Foundry portal. The primary objective of this update is to streamline and centralize the workflow for creating synthetic video avatars, enabling approved customers to leverage advanced AI-driven video generation capabilities directly within the Foundry environment. This update addresses the growing demand for personalized, scalable video content creation, particularly in scenarios where human-like avatars are required for communication, training, or customer engagement.

**Specific Features and Detailed Changes**  
With this release, the Microsoft Foundry portal now supports the following features for approved customers:

- **Actor Video Upload:** Customers can upload video recordings of actors, which serve as the foundational data for avatar creation.
- **Custom Video Avatar Fine-Tuning:** The portal provides tools to fine-tune the uploaded video to generate a custom video avatar. This process allows for adjustments to ensure the avatar accurately reflects the actor’s likeness and mannerisms.
- **Synthetic Video Generation:** Once the avatar is fine-tuned, users can generate synthetic video content using the custom avatar. This enables the creation of videos where the avatar delivers scripted content, powered by Azure AI Speech.

These features are now generally available, meaning they are production-ready and accessible to all approved customers.

**Technical Mechanisms and Implementation Methods**  
The technical implementation leverages Azure AI Speech’s advanced neural network models for speech synthesis and video generation. The workflow typically involves:

1. **Data Ingestion:** Actor video recordings are uploaded via the Foundry portal.
2. **Model Training and Fine-Tuning:** The system uses the uploaded data to train and fine-tune a custom avatar model, optimizing for visual and audio fidelity.
3. **Synthetic Video Rendering:** The trained model is used to generate synthetic videos, combining AI-generated speech with the custom avatar’s visual representation.

The portal provides an integrated authoring experience, abstracting complex backend processes and offering a user-friendly interface for managing the entire lifecycle of avatar creation and video generation.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations seeking to automate and personalize video communications at scale. Typical scenarios include:

- **Corporate Training:** Creating custom avatars for training modules, allowing consistent delivery of educational content.
- **Customer Service:** Deploying avatars in customer-facing applications for interactive support or onboarding.
- **Marketing and Outreach:** Generating personalized video messages for campaigns or product demonstrations.

**Important Considerations and Limitations**  
- **Access Restriction:** The features are available only to approved customers, implying a vetting or approval process.
- **Data Privacy:** Handling actor video recordings requires strict adherence to privacy and consent protocols.
- **Quality Control:** Fine-tuning is essential to ensure the avatar’s accuracy and prevent uncanny or misleading representations.

**Integration with Related Azure Services**  
The Custom Avatar and Custom Video portal is tightly integrated with Azure AI Speech, leveraging its speech synthesis capabilities. It is also part of the Microsoft Foundry ecosystem, which may offer additional tools for content management, workflow automation, and deployment. Integration with other Azure services (such as Azure Storage for video assets or Azure Cognitive Services for additional AI features) is likely facilitated via the portal’s architecture.

**Summary Sentence**  
Azure AI Speech’s Custom Avatar and Custom Video authoring experiences are now generally available in the Microsoft Foundry portal, enabling approved customers to upload actor videos, fine-tune custom avatars, and generate synthetic video content through a streamlined, integrated workflow.

---

### 49. Public Preview: Trace Replay and trace visualizations for Foundry agents

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Trace Replay and trace visualizations for Foundry agents](https://azure.microsoft.com/updates?id=563426)

**Update ID**: 563426
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry observability now offers Trace Replay and enhanced trace visualizations in public preview.

- Key changes or new features  
  - **Trace Replay:** Developers can step through captured traces of multi-step agent runs, reviewing each stage (model, tool, inter-agent calls) in detail.  
  - **New Visualizations:** Improved visual tools make it easier to analyze and debug complex agent workflows by providing clear insights into each trace step.

- Target audience affected  
  - Agent developers building with Microsoft Foundry  
  - IT professionals responsible for monitoring, debugging, and maintaining AI agent workflows

- Important notes  
  - These features accelerate debugging and troubleshooting for multi-step agent runs, reducing time to resolution.  
  - Available in public preview; feedback is encouraged to help refine the experience.  
  - Integration with existing Foundry observability tools ensures a seamless workflow for current users.

[Read more on the Azure Update page.](https://azure.microsoft.com/updates?id=563426)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Trace Replay and Trace Visualizations for Foundry Agents  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563426)

---

**Background and Purpose of the Update:**  
Microsoft has introduced Trace Replay and new trace visualizations in public preview as part of Foundry observability. The primary objective of this update is to enhance the debugging capabilities for agent developers working with multi-step runs. By providing a more granular and interactive approach to trace analysis, the update aims to streamline the identification and resolution of issues within complex agent workflows.

---

**Specific Features and Detailed Changes:**  
- **Trace Replay:**  
  - Offers a step-by-step rewind of captured traces, allowing developers to sequentially review each stage of an agent’s execution.
  - Displays detailed information for each step, including the model used, the tool invoked, and inter-agent interactions.
- **Trace Visualizations:**  
  - Introduces new visual representations of trace data, making it easier to interpret the flow and dependencies within multi-step agent runs.
  - Visualizations provide clarity on the execution path, helping to quickly pinpoint anomalies or unexpected behaviors.

---

**Technical Mechanisms and Implementation Methods:**  
- **Trace Capture:**  
  - During agent execution, traces are captured, recording detailed metadata about each step, including model invocations, tool usage, and agent-to-agent communication.
- **Replay Engine:**  
  - The replay functionality reconstructs the execution sequence, enabling users to navigate backward and forward through each step.
  - The replay view synchronizes trace data with corresponding visualizations, ensuring contextual understanding at each stage.
- **Visualization Layer:**  
  - Utilizes graphical representations (such as flow diagrams or step charts) to map out the agent’s execution path and dependencies.
  - Visualizations are dynamically updated as users step through the replay, providing real-time insights into the agent’s behavior.

---

**Use Cases and Application Scenarios:**  
- **Debugging Multi-Step Agent Runs:**  
  - Developers can use trace replay to isolate and analyze failures or unexpected outcomes in complex agent workflows.
- **Performance Optimization:**  
  - By visualizing the execution path, bottlenecks or inefficient steps can be identified and addressed.
- **Collaboration and Review:**  
  - Teams can leverage visualizations to communicate trace findings and collaborate on troubleshooting efforts.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:**  
  - As this feature is in public preview, it may not be fully stable or feature-complete. Users should exercise caution when relying on it in production environments.
- **Scope of Trace Data:**  
  - The replay and visualization features are dependent on the granularity and completeness of the captured trace data. Incomplete traces may limit the effectiveness of these tools.
- **Integration Requirements:**  
  - Users must ensure that their agents are instrumented to capture the necessary trace data for replay and visualization.

---

**Integration with Related Azure Services:**  
- **Foundry Observability:**  
  - The new features are integrated directly into the Foundry observability platform, enhancing its existing monitoring and debugging capabilities.
- **Agent Development Workflows:**  
  - These tools are designed to be used in conjunction with other Foundry agent development and monitoring features, providing a comprehensive observability solution.

---

**Summary Sentence:**  
Microsoft Foundry observability now offers Trace Replay and enhanced trace visualizations in public preview, enabling agent developers to efficiently debug and analyze multi-step agent runs through stepwise trace review and interactive visual insights.

---

### 50. Public Preview: MCP Server Knowledge Source in Microsoft Foundry IQ

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: MCP Server Knowledge Source in Microsoft Foundry IQ](https://azure.microsoft.com/updates?id=563411)

**Update ID**: 563411
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry IQ now supports external MCP (Microsoft Connector Platform) servers as federated knowledge sources in public preview.

- Key changes or new features  
  - Teams can register external MCP servers as knowledge sources within Foundry IQ.  
  - This enables retrieval of data not just from customer-indexed sources, but also from external systems such as Salesforce, Atlassian, Confluence, and ServiceNow.  
  - Expands Foundry IQ’s data integration capabilities, allowing broader and more flexible knowledge retrieval for enterprise scenarios.

- Target audience affected  
  - Developers building solutions that require integration with third-party knowledge sources.  
  - IT professionals managing enterprise data and knowledge management platforms.  
  - Teams leveraging Microsoft Foundry IQ for advanced search and retrieval across multiple data systems.

- Important notes  
  - This feature is currently in public preview and may be subject to changes before general availability.  
  - Registration and configuration of MCP servers are required to enable this integration.  
  - Useful for organizations seeking unified search and retrieval across both internal and external knowledge bases.

[More details](https://azure.microsoft.com/updates?id=563411)

**Details**:

**Azure Update Technical Explanation: Public Preview – MCP Server Knowledge Source in Microsoft Foundry IQ**

**Background and Purpose of the Update**  
This update introduces support for external MCP (Microsoft Common Protocol) servers as federated knowledge sources within Microsoft Foundry IQ, now available in public preview. Previously, Foundry IQ’s retrieval capabilities were limited to data that customers indexed themselves. The purpose of this update is to broaden the scope of data retrieval by allowing integration with external MCP servers, thereby enabling organizations to leverage knowledge stored in third-party systems such as Salesforce, Atlassian, and Confluence.

**Specific Features and Detailed Changes**  
- **Federated Knowledge Source Support:** Foundry IQ can now register and connect to external MCP servers as knowledge sources.
- **Expanded Data Retrieval:** Teams are no longer restricted to self-indexed data; they can access and retrieve information directly from external systems that support the MCP protocol.
- **Integration with Third-party Systems:** The update specifically mentions compatibility with systems like Salesforce, Atlassian, and Confluence, enabling broader enterprise knowledge integration.

**Technical Mechanisms and Implementation Methods**  
- **MCP Server Registration:** Teams can register MCP servers within Foundry IQ, establishing a federated connection.
- **Federated Retrieval:** Once registered, Foundry IQ queries the MCP servers as part of its knowledge retrieval process, aggregating results from both internal and external sources.
- **Protocol-based Integration:** The integration leverages the MCP protocol, ensuring secure and standardized communication between Foundry IQ and external knowledge repositories.

**Use Cases and Application Scenarios**  
- **Unified Knowledge Search:** Organizations can provide users with a single search interface in Foundry IQ that returns results from both internal indexes and external systems like Salesforce or Confluence.
- **Cross-platform Insights:** Teams working across multiple platforms can access relevant information without duplicating or migrating data, improving productivity and decision-making.
- **Enterprise Knowledge Management:** IT departments can centralize knowledge discovery, compliance, and governance by federating multiple knowledge sources.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes.
- **Supported Systems:** Only MCP-compatible systems are supported; integration is limited to systems like Salesforce, Atlassian, and Confluence as specified.
- **Security and Compliance:** Organizations should review access controls and data governance policies when federating external knowledge sources.

**Integration with Related Azure Services**  
- **Microsoft Foundry IQ:** The update directly enhances Foundry IQ’s capabilities, making it a more powerful knowledge discovery tool.
- **Azure Data Services:** While not explicitly mentioned, federated knowledge retrieval can complement Azure data analytics and AI services by providing richer data sources.
- **Azure Security and Identity:** Integration with Azure Active Directory and security controls is recommended to manage access to federated knowledge sources.

**Summary Sentence**  
Microsoft Foundry IQ now supports external MCP servers as federated knowledge sources in public preview, enabling teams to register and retrieve knowledge from systems like Salesforce, Atlassian, and Confluence, thereby expanding data discovery beyond self-indexed content.

---

### 51. Public Preview: Incremental SharePoint permissions sync for Azure AI Search and Foundry IQ

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Incremental SharePoint permissions sync for Azure AI Search and Foundry IQ](https://azure.microsoft.com/updates?id=563396)

**Update ID**: 563396
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search and Foundry IQ Knowledge Sources now support incremental SharePoint permissions synchronization, available in public preview.

- Key changes or new features  
The update introduces the ability to incrementally sync SharePoint permissions, including document-level, site, and library access control lists (ACLs). As SharePoint permissions change, Azure AI Search and Foundry IQ will automatically update access controls for indexed content, ensuring that search results and knowledge mining respect the latest permissions without requiring a full re-index.

- Target audience affected  
This update impacts developers and IT professionals integrating Azure AI Search or Foundry IQ with SharePoint as a data source, especially those managing enterprise environments with frequently changing permissions.

- Important notes if any  
Incremental permissions sync improves security and compliance by ensuring that only authorized users can access sensitive content in search results. It also reduces operational overhead and latency compared to full re-indexing. This feature is currently in public preview, so it may not be suitable for production workloads in highly regulated environments.

For more details, refer to the official update: https://azure.microsoft.com/updates?id=563396

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Incremental SharePoint permissions sync for Azure AI Search and Foundry IQ  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563396)

---

### 1. Background and Purpose of the Update

Enterprises frequently use SharePoint to store business-critical content, with access governed by granular permissions at the document, site, and library levels. Azure AI Search and Foundry IQ utilize SharePoint as a knowledge source, requiring up-to-date access control to ensure secure and compliant search experiences. Previously, synchronization of SharePoint permissions with Azure AI Search and Foundry IQ was not incremental, potentially leading to outdated access control lists (ACLs) and security risks. This update introduces incremental SharePoint permissions synchronization in public preview, addressing the need for real-time, accurate permission management.

---

### 2. Specific Features and Detailed Changes

- **Incremental Permissions Sync:** The update enables Azure AI Search and Foundry IQ Knowledge Sources to incrementally synchronize SharePoint permissions. This ensures that changes to document-level, site, and library ACLs in SharePoint are reflected promptly in the search index and knowledge base.
- **Scope of Synchronization:** The sync covers all relevant SharePoint access control layers—document, site, and library—ensuring comprehensive coverage for enterprise scenarios.
- **Public Preview Availability:** The feature is currently in public preview, allowing organizations to test and validate the functionality before general availability.

---

### 3. Technical Mechanisms and Implementation Methods

- **Incremental Synchronization Process:** Instead of performing full permission syncs, the system now detects and applies only the changes (deltas) in SharePoint permissions. This reduces synchronization time and resource consumption.
- **Real-time ACL Updates:** As SharePoint permissions are modified (e.g., when users are added or removed from groups, or when access rights change), these updates are incrementally propagated to Azure AI Search and Foundry IQ, maintaining alignment between source and index.
- **Integration with Knowledge Sources:** The incremental sync is implemented at the knowledge source connector level, ensuring that any SharePoint-based content ingested by Azure AI Search or Foundry IQ respects the latest permission settings.

---

### 4. Use Cases and Application Scenarios

- **Enterprise Search Security:** Organizations leveraging Azure AI Search for internal document discovery can ensure that search results always respect the most current SharePoint permissions, preventing unauthorized access.
- **Knowledge Management:** Foundry IQ users can maintain compliance and data governance by ensuring that knowledge bases reflect up-to-date SharePoint ACLs.
- **Dynamic Access Environments:** Enterprises with frequent changes in user roles or project teams benefit from near real-time permission updates, reducing administrative overhead and risk.

---

### 5. Important Considerations and Limitations

- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads with strict compliance requirements. Organizations should validate functionality in test environments.
- **Scope of Support:** The update specifically addresses SharePoint permissions. Other content sources or custom ACL models are not covered by this incremental sync.
- **Operational Monitoring:** IT teams should monitor sync operations for errors or delays, especially in large or complex SharePoint environments.

---

### 6. Integration with Related Azure Services

- **Azure AI Search:** The incremental sync directly enhances Azure AI Search by ensuring its security trimming features remain accurate as SharePoint permissions evolve.
- **Foundry IQ:** Knowledge sources in Foundry IQ benefit from up-to-date access control, supporting secure knowledge discovery.
- **SharePoint Online:** The update leverages SharePoint’s native permission models and integrates with its change tracking mechanisms.

---

**Summary Sentence:**  
This public preview update introduces incremental SharePoint permissions synchronization for Azure AI Search and Foundry IQ Knowledge Sources, ensuring that document, site, and library access control lists remain current as SharePoint permissions change, thereby enhancing security and compliance for enterprise search and knowledge management scenarios.

---

### 52. Public Preview: Content Understanding NextGen in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Content Understanding NextGen in Microsoft Foundry](https://azure.microsoft.com/updates?id=563361)

**Update ID**: 563361
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Content Understanding NextGen is now available in public preview within Microsoft Foundry, integrating content processing capabilities directly into the Foundry portal.

- Key changes or new features  
Developers can now access Read and Layout playgrounds inside Microsoft Foundry, enabling OCR text extraction and document layout analysis without switching to the separate Content Understanding Studio. This integration streamlines workflows by allowing users to test and develop content understanding solutions directly within the Foundry environment.

- Target audience affected  
Developers and IT professionals working with document processing, OCR, and content understanding solutions in Azure, especially those who previously used Content Understanding Studio.

- Important notes if any  
This update eliminates the need to context-switch between platforms, improving productivity and user experience. The feature is currently in public preview, so it may not yet be suitable for production workloads. Users are encouraged to provide feedback during the preview phase. For more details, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=563361

**Details**:

**Azure Update Technical Explanation: Public Preview: Content Understanding NextGen in Microsoft Foundry**

**Background and Purpose of the Update**  
This update introduces the public preview of Content Understanding NextGen within Microsoft Foundry. Previously, users had to switch to a standalone Content Understanding Studio to perform content understanding tasks. The primary goal of this update is to streamline the workflow for developers by integrating Content Understanding capabilities directly into the Foundry portal, thereby eliminating the need for context switching and improving productivity for everyday content processing tasks.

**Specific Features and Detailed Changes**  
- **Integrated Content Understanding:** Content Understanding tools are now natively available within the Microsoft Foundry portal.
- **Read and Layout Playgrounds:** Developers gain access to Read and Layout playgrounds. These are interactive environments for performing and testing OCR (Optical Character Recognition) text extraction tasks directly within Foundry.
- **End of Context Switching:** By embedding these features, the update removes the dependency on the separate Content Understanding Studio for routine operations.

**Technical Mechanisms and Implementation Methods**  
- **Portal Integration:** Content Understanding functionalities are implemented as part of the Foundry portal, leveraging the same authentication, user interface, and workflow mechanisms as other Foundry features.
- **OCR Capabilities:** The Read and Layout playgrounds utilize Microsoft’s OCR engines to extract text from documents and images. The playgrounds provide an interactive interface for developers to upload content, run OCR processes, and view results in real-time.
- **NextGen Architecture:** The update references "NextGen," indicating that the underlying Content Understanding services are the latest generation, offering improved performance and accuracy for text extraction tasks.

**Use Cases and Application Scenarios**  
- **Document Processing:** Developers can use the integrated playgrounds to extract text from scanned documents, PDFs, and images as part of automated workflows.
- **Form Recognition:** The Layout playground is suitable for extracting structured data from forms and tables, supporting scenarios like invoice processing, contract analysis, and compliance checks.
- **Rapid Prototyping:** The playgrounds enable quick experimentation and validation of OCR models within the same portal used for other Foundry tasks.

**Important Considerations and Limitations**  
- **Public Preview:** The feature is currently in public preview, which means it may not be fully production-ready and could be subject to changes. Users should evaluate the feature in non-critical environments before broad adoption.
- **Scope:** The update specifically mentions Read and Layout playgrounds for OCR text extraction. Other advanced content understanding features may not yet be available in this integrated experience.
- **Transition from Studio:** While the update reduces the need for the standalone Content Understanding Studio, users with complex or legacy workflows may need to assess migration strategies.

**Integration with Related Azure Services**  
- **Microsoft Foundry:** The update is fully integrated with Microsoft Foundry, aligning with its authentication, user management, and workflow orchestration.
- **Azure Cognitive Services:** The underlying OCR and layout analysis capabilities are likely powered by Azure Cognitive Services, ensuring compatibility with other AI and machine learning services within the Azure ecosystem.
- **Workflow Automation:** The extracted text and structured data can be used in downstream Azure services for further processing, analytics, or integration with business applications.

**Summary Sentence**  
Microsoft Foundry now offers Content Understanding NextGen in public preview, enabling developers to perform OCR text extraction via integrated Read and Layout playgrounds within the portal, thereby streamlining document processing workflows without the need for the standalone Content Understanding Studio.

---

### 53. Generally Available: Document translation for image files (synchronous, single document)

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Document translation for image files (synchronous, single document)](https://azure.microsoft.com/updates?id=563341)

**Update ID**: 563341
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Translator’s Document Translation API now supports synchronous translation of single image files (e.g., JPEG, PNG) and is generally available.

- Key changes or new features  
Developers and IT professionals can now submit a single image file via a synchronous API call and receive the translated text result immediately. Supported image formats include JPEG, PNG, and similar types. This update enables real-time translation workflows for image-based documents without the need for batch processing or asynchronous handling.

- Target audience affected  
Developers integrating translation features into applications, IT professionals managing document processing pipelines, and organizations needing instant translation of image-based documents.

- Important notes if any  
This feature is limited to single image files per request and is intended for synchronous (real-time) use cases. For batch or asynchronous translation of multiple documents, existing asynchronous APIs should be used. Ensure that image files meet the supported format and size requirements as specified in the API documentation.

[Read more](https://azure.microsoft.com/updates?id=563341)

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Document translation for image files (synchronous, single document)  
**Link:** [Azure Update Reference](https://azure.microsoft.com/updates?id=563341)

---

**Background and Purpose of the Update**  
Azure AI Translator has expanded its capabilities to include synchronous translation for image files. The primary purpose of this update is to enable customers to translate the content of standalone image documents (e.g., JPEG, PNG) in real-time via a single API call. This addresses the growing demand for seamless translation workflows involving image-based documents, such as scanned pages, photos of text, or screenshots, without the need for asynchronous processing or manual extraction of text.

**Specific Features and Detailed Changes**  
- **Synchronous API Support:** Users can now submit a single image file and receive the translated result immediately in the same API call.
- **Supported Formats:** The service supports common image formats, including JPEG and PNG.
- **General Availability:** This feature is now generally available, indicating production-level support and stability.

**Technical Mechanisms and Implementation Methods**  
- **Input Handling:** The API accepts an image file as input. The image is processed in real-time.
- **Text Extraction and Translation:** Internally, the service likely uses Optical Character Recognition (OCR) to extract text from the image, then applies Azure AI Translator’s machine translation models to the recognized text.
- **Synchronous Workflow:** The entire process—from image upload, text extraction, translation, to result delivery—occurs within a single synchronous HTTP request/response cycle, ensuring immediate availability of the translation output.
- **API Endpoint:** The feature is exposed via a dedicated synchronous API endpoint, designed for single-document translation scenarios.

**Use Cases and Application Scenarios**  
- **Instant Translation of Scanned Documents:** Organizations can translate scanned contracts, letters, or official documents without manual text extraction.
- **Mobile and Web Applications:** Developers can integrate this API to allow users to translate photos or screenshots containing text directly within their applications.
- **Localization Workflows:** Teams handling multilingual content can streamline translation of image-based assets, such as marketing materials or user guides.
- **Accessibility Solutions:** The feature can be used to provide translated versions of image-based content for users with different language requirements.

**Important Considerations and Limitations**  
- **Single Document Limitation:** The API is designed for single-document translation per call; batch processing of multiple images is not supported in this synchronous mode.
- **Supported Formats:** Only specific image formats (such as JPEG and PNG) are supported; unsupported formats will not be processed.
- **Synchronous Processing:** While suitable for real-time applications, synchronous processing may not be optimal for large-scale or high-throughput scenarios due to potential request timeouts or performance considerations.
- **Result Format:** The translated result is returned immediately, but the exact structure (e.g., plain text, structured data) should be verified in the API documentation.

**Integration with Related Azure Services**  
- **Azure AI Translator:** This feature is part of the broader Azure AI Translator service, leveraging its translation models.
- **Potential Integration with Azure Cognitive Services:** While not explicitly stated, the OCR component may utilize Azure Cognitive Services’ Computer Vision capabilities for text extraction.
- **Workflow Automation:** The API can be integrated into Azure Logic Apps, Azure Functions, or custom workflows to automate translation tasks involving image files.

---

**Summary Sentence**  
Azure AI Translator now offers general availability of synchronous single-document image translation, enabling immediate translation of JPEG, PNG, and similar image files via a single API call for streamlined and real-time multilingual workflows.

---

### 54. Generally Available: Azure AI Translator SDKs for the latest text translation API

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure AI Translator SDKs for the latest text translation API](https://azure.microsoft.com/updates?id=563326)

**Update ID**: 563326
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Translator SDKs for the latest text translation REST API (v4) are now generally available across four programming languages: C#/.NET, Java, JavaScript, and Python.

- Key changes or new features  
The SDKs provide official, production-ready support for Translator API v4, enabling developers to easily integrate advanced text translation capabilities into their applications. The SDKs offer streamlined methods for accessing translation features, improved language support, and enhanced API capabilities compared to previous versions.

- Target audience affected  
Developers and IT professionals working with Azure AI Translator services, especially those building applications in C#/.NET, Java, JavaScript, or Python. Teams maintaining or upgrading translation features in their software will benefit from these updates.

- Important notes if any  
The SDKs are now recommended for all new development targeting Azure AI Translator. Existing applications using older API versions or unofficial SDKs should consider upgrading to leverage the latest features, improved performance, and ongoing support. Documentation and migration guides are available to assist with the transition.  

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=563326

**Details**:

**Azure Update Report: Generally Available – Azure AI Translator SDKs for the Latest Text Translation API**

**Background and Purpose of the Update:**  
Azure AI Translator has announced the general availability (GA) of SDKs targeting the latest text translation REST API (Translator API v4). The primary purpose of this update is to provide developers with robust, production-ready SDKs across four major programming languages: C#/.NET, Java, JavaScript, and Python. This enables seamless integration of Azure’s advanced text translation capabilities into a wide range of applications and services, supporting multilingual scenarios and global user bases.

**Specific Features and Detailed Changes:**  
- **GA SDKs for API v4:** The update delivers officially supported SDKs for Translator API v4, ensuring stability, reliability, and long-term support.
- **Language Coverage:** SDKs are available for C#/.NET, Java, JavaScript, and Python, catering to diverse development environments.
- **REST API Integration:** The SDKs abstract the complexities of direct REST API calls, offering simplified methods for text translation operations.
- **Feature Exposure:** All core features of Translator API v4 are accessible via the SDKs, including real-time text translation, language detection, and support for multiple translation scenarios.

**Technical Mechanisms and Implementation Methods:**  
- **SDK Architecture:** Each SDK acts as a wrapper around the Translator REST API v4, handling HTTP requests, authentication, and response parsing.
- **Authentication:** The SDKs utilize Azure authentication mechanisms, typically requiring an Azure subscription and API key for secure access.
- **API Calls:** Developers can invoke translation functions directly from their codebase, passing source text and specifying target languages. The SDKs manage request formatting and error handling.
- **Version Targeting:** By targeting API v4, the SDKs ensure compatibility with the latest features and improvements in Azure Translator.

**Use Cases and Application Scenarios:**  
- **Multilingual Applications:** Integrate real-time translation into web, mobile, or desktop apps to support users in different languages.
- **Content Localization:** Automate translation workflows for websites, documents, or customer communications.
- **Chatbots and Virtual Agents:** Enable bots to communicate in multiple languages using integrated translation services.
- **Data Processing Pipelines:** Incorporate translation steps in data analytics or ETL pipelines using Python or Java SDKs.

**Important Considerations and Limitations:**  
- **API Key Management:** Secure handling of API keys is essential; keys should not be exposed in client-side code.
- **Supported Features:** Only features available in Translator API v4 are exposed; legacy API features may not be supported.
- **Language Support:** Translation quality and language coverage depend on the underlying API; consult official documentation for supported languages.
- **Rate Limits and Quotas:** Usage is subject to Azure Translator’s pricing, rate limits, and quotas as defined in the Azure portal.

**Integration with Related Azure Services:**  
- **Azure Cognitive Services:** Translator SDKs are part of Azure Cognitive Services, enabling integration with other AI capabilities such as speech, vision, and language.
- **Azure Functions and Logic Apps:** SDKs can be used within serverless workflows to automate translation tasks.
- **Azure DevOps and CI/CD:** Incorporate translation steps in automated pipelines using SDKs for supported languages.

**Summary Sentence:**  
Azure AI Translator now provides generally available SDKs for Translator API v4 in C#/.NET, Java, JavaScript, and Python, enabling developers to easily integrate advanced text translation capabilities into their applications with robust, production-ready tools.

---

### 55. Generally Available: Adaptive custom translation in the Azure AI Foundry NextGen playground

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Adaptive custom translation in the Azure AI Foundry NextGen playground](https://azure.microsoft.com/updates?id=563307)

**Update ID**: 563307
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Adaptive Custom Translation (AdaptCT) is now generally available in the Azure AI Foundry NextGen playground for Azure Translator.

- Key changes or new features  
AdaptCT allows organizations to customize machine translation models with domain-specific terminology using small datasets. This feature removes the need for large-scale training data, enabling faster and more efficient adaptation of translation models to specialized business or industry language.

- Target audience affected  
Developers and IT professionals working with Azure Translator, especially those needing tailored translation solutions for enterprise or industry-specific applications.

- Important notes if any  
AdaptCT is accessible within the Azure AI Foundry NextGen playground, making it easier to experiment and deploy custom translation models. This update is particularly valuable for teams with limited data resources who require accurate, context-aware translations. No extensive machine learning expertise or large datasets are needed to leverage this feature. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=563307).

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Adaptive custom translation in the Azure AI Foundry NextGen playground

**Background and Purpose of the Update:**  
The release of Adaptive Custom Translation (AdaptCT) as generally available in the Azure AI Foundry NextGen playground for Azure Translator addresses the growing demand among enterprises for domain-specific translation capabilities. Traditional translation models often struggle with specialized terminology, leading to inaccuracies in industries such as legal, medical, or technical fields. The purpose of this update is to enable organizations to tailor translation outputs to their unique vocabularies and contexts, improving translation quality without requiring extensive training datasets.

**Specific Features and Detailed Changes:**  
AdaptCT introduces the ability for users to customize translation models within the Azure AI Foundry NextGen playground. The key feature is its support for adaptation using small datasets, which significantly lowers the barrier for enterprises to implement domain-specific translation. This eliminates the need for large-scale training data, making the customization process more accessible and efficient. The update makes AdaptCT generally available, meaning it is now fully supported and ready for production use within the playground environment.

**Technical Mechanisms and Implementation Methods:**  
AdaptCT leverages Azure Translator’s underlying AI infrastructure, allowing users to upload small, curated datasets containing domain-specific terminology and phrases. The system then adapts the translation model to incorporate these terms, ensuring that future translations reflect the enterprise’s preferred language and context. The adaptation process is streamlined within the NextGen playground, providing an interactive interface for dataset submission and model customization. The mechanism is designed to be lightweight, focusing on incremental adaptation rather than full retraining, which reduces computational requirements and speeds up deployment.

**Use Cases and Application Scenarios:**  
- **Legal and Regulatory Documents:** Enterprises can adapt translation models to handle legal jargon and regulatory language, ensuring compliance and accuracy.
- **Medical and Healthcare Content:** Hospitals and pharmaceutical companies can customize translations for medical terminology, improving patient communication and documentation.
- **Technical Manuals and Engineering Documentation:** Manufacturers and engineering firms can tailor translations for technical terms, reducing errors in multilingual manuals.
- **Corporate Communications:** Organizations with branded terminology or internal lingo can ensure consistent translation across global teams.

**Important Considerations and Limitations:**  
While AdaptCT enables customization with small datasets, the quality and effectiveness of adaptation depend on the relevance and accuracy of the provided data. Users must ensure that their datasets are representative of the domain-specific terminology they wish to incorporate. The adaptation process is designed for incremental improvements and may not fully replace the need for larger datasets in highly specialized or nuanced domains. Additionally, the feature is currently available within the Azure AI Foundry NextGen playground, and users should verify compatibility and integration with their existing workflows.

**Integration with Related Azure Services:**  
AdaptCT is integrated with Azure Translator, leveraging its core translation capabilities. It operates within the Azure AI Foundry NextGen playground, which serves as a collaborative environment for AI experimentation and deployment. Enterprises can utilize AdaptCT alongside other Azure AI services, such as Azure Cognitive Services for language processing and Azure Machine Learning for broader AI model management. The seamless integration facilitates end-to-end workflows for translation customization, deployment, and monitoring.

**Summary Sentence:**  
Adaptive Custom Translation (AdaptCT) is now generally available in the Azure AI Foundry NextGen playground, enabling enterprises to efficiently tailor Azure Translator outputs to domain-specific terminology using small datasets, thereby improving translation accuracy and reducing the need for extensive training data.

---

### 56. Generally Available: Photo Avatar standard and custom in Azure AI Speech

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Photo Avatar standard and custom in Azure AI Speech](https://azure.microsoft.com/updates?id=563282)

**Update ID**: 563282
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Photo Avatar (standard and custom) in Azure AI Speech is now generally available.

- Key changes or new features  
  - **Standard Photo Avatar:** Allows generation of a talking head video from a single photo at 512x512 resolution.  
  - **Custom Photo Avatar:** Enables users to fine-tune the avatar’s appearance using their own images, providing more control over the final output.

- Target audience affected  
  - Developers integrating AI-driven avatars into applications (e.g., chatbots, virtual assistants, content creation tools).  
  - IT professionals managing AI services and media pipelines in enterprise environments.

- Important notes if any  
  - Both standard and custom avatars are now production-ready and supported by Azure AI Speech.  
  - The API supports easy integration for generating personalized or generic talking head videos from photos.  
  - Consider compliance and privacy requirements when using custom avatars with user-provided images.

[Read the official update](https://azure.microsoft.com/updates?id=563282)

**Details**:

**Azure Update Report: Generally Available – Photo Avatar Standard and Custom in Azure AI Speech**

**Background and Purpose of the Update:**  
The general availability of Photo Avatar in Azure AI Speech marks the introduction of advanced avatar generation capabilities to Azure’s speech services. This update aims to enhance digital communication and content creation by enabling users to generate realistic talking head videos from static images, leveraging Azure’s AI-driven speech synthesis and image processing technologies.

**Specific Features and Detailed Changes:**  
- **Standard Photo Avatar:**  
  - Generates a talking head video from a single photo.
  - Output resolution is 512x512 pixels.
  - Designed for quick and accessible avatar creation using a predefined process.
- **Custom Photo Avatar:**  
  - Allows users to fine-tune the avatar’s appearance using their own images.
  - Offers greater flexibility and control over the resulting video’s look and feel.
  - Enables organizations to create avatars that match specific branding or personalization requirements.

**Technical Mechanisms and Implementation Methods:**  
- The service utilizes advanced AI models to map facial features from a static photo and animate them in sync with synthesized speech.
- The process involves:
  - Uploading a single image (for standard) or a set of custom images (for custom).
  - Inputting the desired speech text.
  - The system generates a video where the avatar’s facial movements and lip-sync correspond to the input speech.
- The generated video is produced at a fixed resolution of 512x512 pixels, ensuring consistency across outputs.
- The service is accessible via Azure AI Speech APIs, allowing for integration into custom applications and workflows.

**Use Cases and Application Scenarios:**  
- **Digital Assistants and Chatbots:** Enhance user engagement by providing a visual, human-like interface.
- **E-learning and Training:** Create personalized instructional videos with minimal production effort.
- **Customer Service:** Deploy branded avatars for automated video responses.
- **Marketing and Content Creation:** Rapidly generate spokesperson videos for campaigns or announcements.

**Important Considerations and Limitations:**  
- The output resolution is limited to 512x512 pixels, which may not be suitable for all high-definition video requirements.
- The quality and realism of the avatar are dependent on the quality of the input image(s).
- Custom avatars require additional configuration and image preparation compared to the standard option.
- Users should ensure compliance with privacy and consent regulations when using personal images for avatar creation.

**Integration with Related Azure Services:**  
- **Azure AI Speech:** The Photo Avatar feature is tightly integrated with Azure AI Speech, leveraging its text-to-speech capabilities for synchronized audio-visual output.
- **Azure Cognitive Services:** Can be combined with other cognitive services (e.g., language understanding, translation) to create comprehensive AI-driven communication solutions.
- **Azure Media Services:** Generated videos can be further processed, stored, or streamed using Azure Media Services for broader distribution.

**Summary Sentence:**  
Photo Avatar in Azure AI Speech is now generally available, offering both standard and custom options to generate talking head videos from photos at 512x512 resolution, enabling seamless integration of realistic avatars into digital communication and content workflows via Azure’s speech and cognitive services.

---

### 57. Public Preview: Microsoft Purview sensitivity label auditing in Azure AI Search

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Microsoft Purview sensitivity label auditing in Azure AI Search](https://azure.microsoft.com/updates?id=563267)

**Update ID**: 563267
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search now supports auditing of Microsoft Purview sensitivity labels in Public Preview.

- Key changes or new features  
Azure AI Search emits audit events for sensitivity labels attached to indexed documents. When using the SharePoint in Microsoft 365 indexer with label preservation enabled, the system logs query-time filtering decisions and label-related actions. This provides visibility into how sensitivity labels are handled during search operations, supporting compliance and security requirements.

- Target audience affected  
Developers and IT professionals integrating Azure AI Search with SharePoint in Microsoft 365, especially those managing sensitive or regulated data and leveraging Microsoft Purview for information protection.

- Important notes if any  
To benefit from this feature, ensure the SharePoint indexer is configured to preserve and honor sensitivity labels. Audit logs can help organizations track label usage and filtering, aiding in compliance audits and investigations. This feature is currently in Public Preview and may change before general availability.

[Learn more](https://azure.microsoft.com/updates?id=563267)

**Details**:

**Azure Update Report: Public Preview – Microsoft Purview Sensitivity Label Auditing in Azure AI Search**

**Background and Purpose of the Update**  
This update introduces audit event emission for Microsoft Purview sensitivity labels within Azure AI Search. The primary goal is to enhance compliance and security by providing visibility into how sensitivity labels are managed and utilized during indexing and querying operations. This is particularly relevant for organizations leveraging SharePoint in Microsoft 365 as a data source, where sensitivity labels are used to classify and protect content.

**Specific Features and Detailed Changes**  
Azure AI Search now generates audit events whenever sensitivity labels, managed by Microsoft Purview, are carried alongside indexed documents. The update specifically targets scenarios where the SharePoint indexer in Microsoft 365 is configured to preserve and honor these labels. Audit events are emitted during query-time filtering decisions and label handling processes, enabling organizations to track and review how sensitive information is accessed and processed within Azure AI Search.

**Technical Mechanisms and Implementation Methods**  
The technical implementation involves the integration of Microsoft Purview sensitivity label metadata into the Azure AI Search indexing pipeline. When documents are indexed from SharePoint, the indexer preserves sensitivity labels as part of the document metadata. During query execution, Azure AI Search evaluates these labels to enforce filtering decisions based on label policies. Audit events are generated at key points—such as label preservation during indexing and filtering actions during querying—and are emitted to a designated audit log or monitoring system for review.

**Use Cases and Application Scenarios**  
- **Compliance Monitoring:** Organizations can track access and usage of sensitive documents indexed from SharePoint, ensuring adherence to data protection policies.
- **Security Auditing:** IT teams can review audit logs to detect unauthorized access or misuse of sensitive information, supporting incident response and forensic investigations.
- **Label Policy Enforcement:** Administrators can verify that sensitivity label policies are correctly applied and honored during both indexing and querying operations within Azure AI Search.
- **Regulatory Reporting:** Audit events can be used to generate reports for regulatory compliance, demonstrating that sensitive data is handled according to organizational and legal requirements.

**Important Considerations and Limitations**  
- The feature is in public preview, which may imply limited support and potential changes before general availability.
- Audit event emission is dependent on the SharePoint indexer being configured to preserve and honor sensitivity labels; misconfiguration may result in incomplete auditing.
- The scope of auditing is limited to indexed documents and query-time filtering decisions; other operations may not be covered.
- Organizations must ensure proper integration with their monitoring and audit log systems to capture and utilize emitted events effectively.

**Integration with Related Azure Services**  
This feature leverages Microsoft Purview for sensitivity label management and integrates with Azure AI Search for indexing and querying. It is specifically designed for environments where SharePoint in Microsoft 365 is used as a data source. Audit events can be further integrated with Azure Monitor or other SIEM solutions for centralized logging and analysis, enhancing the overall security and compliance posture.

**Summary Sentence**  
Azure AI Search now emits audit events for Microsoft Purview sensitivity labels during indexing and query-time filtering, enabling enhanced compliance and security monitoring for organizations using SharePoint in Microsoft 365 as a data source.

---

### 58. Public Preview: SharePoint in Microsoft 365 indexer supports ASPX pages and Lists

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: SharePoint in Microsoft 365 indexer supports ASPX pages and Lists](https://azure.microsoft.com/updates?id=563262)

**Update ID**: 563262
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure AI Search SharePoint in Microsoft 365 indexer is now in public preview with expanded indexing capabilities.

- Key changes or new features  
The indexer now supports indexing ASPX site content (web pages) and SharePoint Lists, in addition to previously supported document libraries. This enables broader content discovery and search scenarios across SharePoint sites. The indexer connects to SharePoint using a Microsoft Entra application registration, supporting both application and delegated permissions.

- Target audience affected  
Developers and IT professionals integrating Azure AI Search with SharePoint in Microsoft 365, especially those building enterprise search solutions or custom applications that require comprehensive content indexing.

- Important notes if any  
To leverage the new capabilities, ensure your Microsoft Entra application registration is properly configured with the necessary permissions. This update allows for richer search experiences by including web pages and list data, not just documents. Review your indexing configurations to include new content types as needed.

[More details](https://azure.microsoft.com/updates?id=563262)

**Details**:

**Azure Update Report: Public Preview – SharePoint in Microsoft 365 Indexer Supports ASPX Pages and Lists**

**Background and Purpose of the Update:**  
Previously, the Azure AI Search SharePoint in Microsoft 365 indexer was limited to indexing content from SharePoint document libraries. This limitation restricted the scope of searchable content within organizations leveraging SharePoint as a central repository for various types of information. The purpose of this update is to expand the indexer’s capabilities, enabling organizations to extract and search a broader range of SharePoint content, thereby improving discoverability and knowledge management within Microsoft 365 environments.

**Specific Features and Detailed Changes:**  
With this update, the SharePoint in Microsoft 365 indexer now supports indexing two additional content types:
- **ASPX Site Content:** The indexer can now crawl and index content from ASPX pages, which are commonly used for web-based content, site pages, and custom web parts within SharePoint sites.
- **SharePoint Lists:** The indexer can also extract and index data from SharePoint Lists, which are frequently used for structured data such as tasks, issues, contacts, or custom business data.

These new capabilities are in addition to the existing support for document libraries, significantly broadening the range of searchable SharePoint content.

**Technical Mechanisms and Implementation Methods:**  
The indexer connects to SharePoint in Microsoft 365 using a Microsoft Entra (formerly Azure Active Directory) application registration. This connection can be established using either application permissions (app-only access) or delegated permissions (on-behalf-of a user). The indexer authenticates via the registered Entra application, ensuring secure and controlled access to SharePoint content.

The indexing process involves:
- Configuring the indexer to target specific SharePoint sites, libraries, lists, or ASPX pages.
- Authenticating via the Entra application with the required permissions.
- Extracting content and metadata from the specified sources.
- Populating an Azure AI Search index with the retrieved data, making it available for advanced search and retrieval scenarios.

**Use Cases and Application Scenarios:**  
- **Enterprise Search:** Organizations can now build comprehensive search solutions that include not only documents but also site content (ASPX pages) and structured data (Lists), providing users with a unified search experience across all relevant SharePoint content.
- **Knowledge Management:** Enhanced indexing supports knowledge discovery by making site pages and list-based knowledge repositories searchable.
- **Business Process Automation:** Automated workflows and applications can leverage the enriched search index to surface relevant information from lists and site pages, improving process efficiency.

**Important Considerations and Limitations:**  
- This feature is currently in public preview, which may entail limited support and potential changes before general availability.
- Proper configuration of Microsoft Entra application registration and permissions is required to ensure secure and successful indexing.
- Only content from SharePoint in Microsoft 365 is supported; on-premises SharePoint is not included.
- The update does not mention support for other SharePoint content types (e.g., calendars, discussion boards), so coverage is limited to ASPX pages, Lists, and document libraries.

**Integration with Related Azure Services:**  
The SharePoint in Microsoft 365 indexer is a component of Azure AI Search, enabling integration with other Azure services such as:
- **Azure Cognitive Search:** For advanced search, enrichment, and AI-powered content analysis.
- **Azure Logic Apps or Power Automate:** For automating workflows based on indexed content.
- **Azure Monitor and Security Center:** For monitoring and securing the indexing process via Entra application controls.

**Summary Sentence:**  
The public preview update enables the Azure AI Search SharePoint in Microsoft 365 indexer to index ASPX site content and SharePoint Lists, expanding search capabilities beyond document libraries and allowing secure, permission-based access via Microsoft Entra application registration.

---

### 59. Generally Available: Content Understanding extractionMode for documents

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Content Understanding extractionMode for documents](https://azure.microsoft.com/updates?id=563257)

**Update ID**: 563257
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry’s Content Understanding feature is now generally available with a new extractionMode setting for document analysis.

- Key changes or new features  
A new extractionMode option allows users to select between two modes when analyzing documents:  
  - Layout-aware mode: Preserves tables, sections, and reading order, ideal for structured documents.  
  - Text-only mode: Provides faster processing by extracting plain text without layout information.

- Target audience affected  
Developers and IT professionals integrating document processing or content extraction into their applications, especially those handling structured documents (e.g., forms, reports, contracts).

- Important notes if any  
Choosing the appropriate extractionMode can optimize for either accuracy (layout-aware) or speed (text-only), depending on your use case. This flexibility enables better alignment with application requirements and resource constraints. Review documentation for API usage and migration considerations if you are updating existing workflows.  
More details: [Azure Update](https://azure.microsoft.com/updates?id=563257)

**Details**:

**Background and Purpose of the Update**  
The update introduces the extractionMode setting for Content Understanding in Microsoft Foundry, now generally available. The purpose is to enhance document analysis capabilities by allowing users to select the most suitable extraction approach based on document structure and processing requirements. This flexibility addresses the need for accurate parsing of structured documents (such as forms and reports) versus faster processing of unstructured or plain text documents.

**Specific Features and Detailed Changes**  
The key feature is the extractionMode parameter, which enables two distinct modes:
- **Layout-aware mode:** Designed for documents where structural elements—such as tables, sections, and reading order—are critical. This mode preserves the spatial and logical arrangement of content, ensuring that extracted data maintains its original context.
- **Text-only mode:** Optimized for speed, this mode extracts only the textual content, disregarding layout information. It is suitable for documents where structure is less important, and rapid processing is required.

This update allows users to explicitly choose the mode that best fits their document processing scenario, improving both accuracy and performance.

**Technical Mechanisms and Implementation Methods**  
The extractionMode setting is implemented as a configurable parameter within the Content Understanding API or workflow in Microsoft Foundry. When processing a document, users specify the extractionMode:
- In layout-aware mode, the system applies advanced document parsing algorithms that analyze spatial relationships, detect tables, sections, and reading order, and reconstruct the logical structure.
- In text-only mode, the system performs a streamlined extraction, focusing solely on the textual content without analyzing layout or structural elements.

This mechanism ensures that document processing is tailored to the specific requirements of the input, optimizing resource utilization and extraction quality.

**Use Cases and Application Scenarios**  
- **Layout-aware mode:** Ideal for processing invoices, contracts, financial statements, and forms where data is organized in tables or sections and the reading order is essential for accurate interpretation.
- **Text-only mode:** Suitable for processing articles, emails, or simple documents where only the textual content is needed, and speed is a priority.

Organizations can leverage this flexibility to build document processing pipelines that adapt to diverse document types, improving automation and reducing manual intervention.

**Important Considerations and Limitations**  
- Selecting the appropriate extractionMode is crucial; layout-aware mode may require more processing time and resources, while text-only mode may not capture structural context.
- The update does not specify additional configuration options or limitations beyond the two modes.
- Users should assess document types and processing requirements before choosing the extractionMode to ensure optimal results.

**Integration with Related Azure Services**  
Content Understanding in Microsoft Foundry can be integrated with other Azure services such as Azure Cognitive Search, Azure Form Recognizer, and Azure Logic Apps. By leveraging extractionMode, downstream services can receive structured or unstructured data as needed, enabling more accurate indexing, automated workflows, and analytics.

**Summary Sentence**  
Content Understanding in Microsoft Foundry now offers a configurable extractionMode setting, enabling IT professionals to choose between layout-aware and text-only document analysis for improved accuracy and performance in document processing workflows.

---

### 60. Generally Available: GenAI prompt skill and chat completion in Azure AI Search knowledge sources

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: GenAI prompt skill and chat completion in Azure AI Search knowledge sources](https://azure.microsoft.com/updates?id=563247)

**Update ID**: 563247
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search has made the GenAI prompt skill and chat completion integration generally available for knowledge sources.

- Key changes or new features  
Developers can now use the GenAI prompt skill within Azure AI Search indexers to call chat completion models (such as OpenAI or Foundry-hosted models) during data enrichment, without writing custom code. Authors can define prompt templates that reference specific field values, enabling dynamic and context-aware enrichment of indexed content.

- Target audience affected  
Developers and IT professionals building intelligent search solutions, especially those leveraging generative AI for content enrichment, summarization, or conversational experiences within Azure AI Search.

- Important notes if any  
This update streamlines the integration of generative AI models into the indexing pipeline, reducing development effort and enabling more advanced AI-powered search scenarios. Prompt templates can be customized for various use cases, and the feature is available for use with Foundry-hosted models. No additional custom code is required to leverage these capabilities.

Link: https://azure.microsoft.com/updates?id=563247

**Details**:

**Azure Update Report**

**Title:** Generally Available: GenAI prompt skill and chat completion in Azure AI Search knowledge sources  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563247)

---

**Background and Purpose of the Update**  
Azure AI Search is evolving to support advanced enrichment scenarios by integrating Generative AI (GenAI) capabilities directly into its indexing pipeline. The purpose of this update is to streamline the use of chat completion models for content enrichment, eliminating the need for custom code. This enables organizations to leverage large language models (LLMs) for generating, summarizing, or transforming content during indexing, thereby enhancing the quality and relevance of searchable data.

**Specific Features and Detailed Changes**  
- **GenAI Prompt Skill (GA):** The GenAI prompt skill is now generally available, allowing indexers to invoke chat completion models as part of the enrichment process.
- **No Custom Code Required:** Indexers can call chat completion models without writing custom code, simplifying integration and maintenance.
- **Prompt Templates:** Authors can create prompt templates that reference field values from the indexed content, enabling dynamic and context-aware prompts.
- **Foundry-Hosted Model Integration:** The skill is designed to point directly at a Foundry-hosted model, ensuring compatibility and ease of deployment within Azure AI Search.

**Technical Mechanisms and Implementation Methods**  
- **Skill Configuration:** The GenAI prompt skill is configured within the Azure AI Search enrichment pipeline. Authors specify the Foundry-hosted model endpoint and define prompt templates that utilize field values from the source data.
- **Field Value Referencing:** Prompt templates can dynamically reference and inject field values, allowing for personalized or context-specific chat completions.
- **Model Invocation:** During the enrichment phase, the skill invokes the chat completion model, processes the prompt, and returns the generated content, which is then indexed.
- **No-Code Integration:** The process is managed through Azure AI Search’s built-in skillset configuration, removing the need for custom scripting or API calls.

**Use Cases and Application Scenarios**  
- **Content Summarization:** Automatically generate concise summaries for documents, articles, or records during indexing.
- **Question Answering:** Enrich indexed data with generated answers to common queries based on document content.
- **Metadata Generation:** Create descriptive metadata or tags using LLMs to improve search relevance and discoverability.
- **Knowledge Extraction:** Extract structured information or insights from unstructured text using chat completion models.

**Important Considerations and Limitations**  
- **Model Selection:** Only Foundry-hosted models are supported for this skill, which may limit flexibility compared to custom model endpoints.
- **Prompt Design:** Effective prompt templates are critical for quality output; poorly designed prompts may yield irrelevant or inaccurate results.
- **Resource Usage:** Invoking LLMs during indexing may impact resource consumption and indexing performance; capacity planning is recommended.
- **Data Privacy:** Ensure compliance with organizational data privacy policies when sending content to external models for processing.

**Integration with Related Azure Services**  
- **Azure AI Search:** The GenAI prompt skill is natively integrated into Azure AI Search’s enrichment pipeline, enhancing search capabilities.
- **Azure Foundry:** The skill leverages Foundry-hosted models, ensuring seamless compatibility and managed deployment.
- **Azure Cognitive Services:** While this update focuses on GenAI skills, it complements other enrichment skills such as entity recognition and image analysis.

---

**Summary Sentence:**  
Azure AI Search now offers a generally available GenAI prompt skill, enabling indexers to enrich content using Foundry-hosted chat completion models and dynamic prompt templates without custom code, thereby streamlining advanced enrichment scenarios and improving search quality.

---

### 61. Generally Available: Managed identity for Foundry billing calls from Azure AI Search

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Managed identity for Foundry billing calls from Azure AI Search](https://azure.microsoft.com/updates?id=563242)

**Update ID**: 563242
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search now supports managed identity authentication for billing operations with Microsoft Foundry resources, moving away from key-based authentication.

- Key changes or new features  
  - Managed identities (system-assigned or user-assigned) can now be assigned to Azure AI Search services for authenticating billing calls to Foundry resources.  
  - This replaces the previous requirement to use API keys for these operations, enhancing security and simplifying credential management.

- Target audience affected  
  - Developers and IT professionals managing Azure AI Search services that interact with Microsoft Foundry resources, especially those responsible for authentication, security, and billing integration.

- Important notes if any  
  - Transitioning to managed identities reduces the risk associated with key management and potential credential leaks.  
  - Existing deployments using key-based authentication should consider migrating to managed identities for improved security and compliance.  
  - Both system-assigned and user-assigned managed identities are supported, offering flexibility in identity management.

[Read the official update](https://azure.microsoft.com/updates?id=563242)

**Details**:

**Background and Purpose of the Update**

This update introduces managed identity authentication for billing operations performed by Azure AI Search against Microsoft Foundry resources. Previously, these billing calls relied on key-based authentication. The purpose of this update is to enhance security, simplify credential management, and align with Azure best practices by leveraging managed identities instead of static keys.

**Specific Features and Detailed Changes**

- Azure AI Search now supports both system-assigned and user-assigned managed identities for authenticating billing operations with Microsoft Foundry.
- The previous method, which required customers to manage and secure access keys for authentication, is now replaced by Azure-managed identities.
- Customers can assign either a system-assigned identity (tied to the lifecycle of the search service) or a user-assigned identity (which can be shared across multiple resources) to their Azure AI Search service for this purpose.

**Technical Mechanisms and Implementation Methods**

- Managed identities are Azure Active Directory (Azure AD) entities automatically managed by Azure, used to authenticate to services that support Azure AD authentication.
- When a managed identity is assigned to an Azure AI Search service, the service obtains an OAuth 2.0 token from Azure AD at runtime.
- This token is used to authenticate billing API calls to Microsoft Foundry, removing the need to store or rotate access keys.
- The process involves configuring the managed identity on the Azure AI Search resource and granting it the necessary permissions on the target Foundry resources.

**Use Cases and Application Scenarios**

- Organizations using Azure AI Search in conjunction with Microsoft Foundry resources for billing and metering scenarios can now streamline authentication processes.
- This is particularly beneficial in environments with strict security and compliance requirements, as it reduces the risk associated with key management.
- It also facilitates automation and DevOps workflows, as managed identities can be provisioned and assigned programmatically without manual key distribution.

**Important Considerations and Limitations**

- Customers must ensure that the assigned managed identity (system-assigned or user-assigned) has the appropriate permissions on the Microsoft Foundry resources to perform billing operations.
- Transitioning from key-based authentication to managed identity may require updates to existing infrastructure-as-code templates or deployment scripts.
- The update is specific to billing operations between Azure AI Search and Microsoft Foundry; other integrations or custom APIs may still require separate authentication mechanisms.

**Integration with Related Azure Services**

- Managed identities are a core feature of Azure AD and are widely supported across Azure services, enabling seamless integration with other Azure resources that support Azure AD-based authentication.
- This update aligns Azure AI Search with other Azure services that have adopted managed identity for secure, keyless authentication.
- It simplifies cross-service authentication scenarios, especially when integrating Azure AI Search with other Azure services that also support managed identities.

**Summary Sentence**

Azure AI Search now supports managed identity authentication for billing operations with Microsoft Foundry resources, enhancing security and simplifying credential management by replacing key-based authentication with system-assigned or user-assigned managed identities.

---

### 62. Public Preview: Image serving in Foundry IQ knowledge bases

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Image serving in Foundry IQ knowledge bases](https://azure.microsoft.com/updates?id=563237)

**Update ID**: 563237
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Foundry IQ knowledge bases now support image serving at query time in public preview.

- Key changes or new features  
Document-extracted images (such as figures, screenshots, and diagrams) are now surfaced alongside relevant text when querying Foundry IQ knowledge bases. During ingestion, images from PDFs, slides, and Office files are retained and associated with the text context in which they appeared. This enables richer, more informative search results, as users can view both text and related images directly in query responses.

- Target audience affected  
Developers and IT professionals building or managing solutions with Foundry IQ knowledge bases, especially those working with document-heavy data sources or requiring visual context in search and knowledge management applications.

- Important notes if any  
This feature is currently in public preview and may be subject to changes or improvements before general availability. Integration of image serving can enhance user experience in applications that rely on Foundry IQ for document search and knowledge extraction. Developers should review API documentation for any changes related to image handling and consider updating client applications to display images in query results.  

Data source: [Azure Update](https://azure.microsoft.com/updates?id=563237)

**Details**:

**Azure Update Report: Public Preview – Image Serving in Foundry IQ Knowledge Bases**

**Background and Purpose of the Update**  
This update introduces the public preview of image serving within Foundry IQ knowledge bases. The primary objective is to enhance the retrieval experience by surfacing images—such as figures, screenshots, and diagrams—extracted from source documents (PDFs, slides, and Office files) at query time. This addresses the need for richer, more contextually complete search results, especially when visual information is critical for understanding or decision-making.

**Specific Features and Detailed Changes**  
- **Image Extraction During Ingestion:** During the ingestion process, Foundry IQ now identifies and extracts images embedded in supported document types.
- **Image Retention with Context:** Each extracted image is retained alongside the text from which it was sourced, preserving the contextual relationship between visual and textual information.
- **Query-Time Image Surfacing:** When users query the knowledge base, relevant images are surfaced along with text results, allowing for immediate access to both data types within the search interface.
- **Supported File Types:** The feature supports extraction from PDFs, slide decks, and Microsoft Office files, covering a wide range of business documentation.

**Technical Mechanisms and Implementation Methods**  
- **Document Parsing:** Foundry IQ employs document parsing techniques to identify image objects within supported file formats during the ingestion pipeline.
- **Image-Text Association:** Extracted images are programmatically linked to their surrounding text, ensuring context is maintained for downstream retrieval.
- **Indexing and Storage:** Both images and their associated text are indexed within the knowledge base, enabling efficient retrieval at query time.
- **Query Processing:** At query execution, the system evaluates both textual and visual content, returning images that are contextually relevant to the user’s search terms.

**Use Cases and Application Scenarios**  
- **Technical Documentation:** Engineers and support teams can retrieve diagrams or screenshots directly related to troubleshooting steps or architectural overviews.
- **Business Reports:** Analysts can access charts and figures embedded in financial or operational reports alongside explanatory text.
- **Training Materials:** Trainers and learners can quickly locate instructional images or annotated slides from large collections of educational documents.

**Important Considerations and Limitations**  
- **Preview Feature:** As this is a public preview, the feature may be subject to changes, and some limitations in extraction accuracy or file type support may exist.
- **Document Types:** Only images from PDFs, slides, and Office files are supported; other formats may not be processed.
- **Image Quality and Placement:** The fidelity and placement of extracted images depend on the source document’s structure and formatting.

**Integration with Related Azure Services**  
- **Foundry IQ Knowledge Bases:** The feature is natively integrated into Foundry IQ, leveraging its ingestion, indexing, and query infrastructure.
- **Azure Cognitive Search (Potential):** While not explicitly stated, organizations using Azure Cognitive Search in conjunction with Foundry IQ may benefit from enhanced search experiences due to richer content indexing.
- **Document Management Workflows:** This update can be incorporated into broader Azure-based document management and knowledge discovery solutions.

**Summary Sentence**  
Foundry IQ knowledge bases now support surfacing document-extracted images at query time in public preview, enabling users to access figures, screenshots, and diagrams alongside relevant text from PDFs, slides, and Office files for a more comprehensive search experience.

---

### 63. Public Preview: OneLake Catalog integration for Foundry IQ Knowledge Sources

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: OneLake Catalog integration for Foundry IQ Knowledge Sources](https://azure.microsoft.com/updates?id=563227)

**Update ID**: 563227
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry IQ now supports integration with the OneLake Catalog as a knowledge source in public preview.

- Key changes or new features  
Foundry IQ agents can now use data from OneLake Catalog, including lakehouse tables, files, and shortcuts managed within Microsoft Fabric, to ground their responses. Data engineers only need to register the OneLake Catalog once for it to be available as a knowledge source. This streamlines access to governed data assets for AI and analytics scenarios.

- Target audience affected  
Data engineers, developers, and IT professionals working with Microsoft Fabric, Foundry IQ, and OneLake Catalog.

- Important notes if any  
This integration allows for simplified and centralized data governance, as all lakehouse data registered in OneLake Catalog becomes accessible to Foundry IQ agents. It enhances the ability to leverage existing data assets for AI-driven solutions without redundant data onboarding. The feature is currently in public preview, so production use should be evaluated accordingly.  
For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=563227).

**Details**:

**Azure Update Technical Explanation: Public Preview – OneLake Catalog Integration for Foundry IQ Knowledge Sources**

**Background and Purpose of the Update:**  
This update introduces public preview support for integrating the OneLake Catalog as a knowledge source within Microsoft Foundry IQ. The primary goal is to enable Foundry IQ agents to utilize data assets—such as lakehouse tables, files, and shortcuts—already governed within Microsoft Fabric. This integration streamlines data discovery and access, allowing organizations to leverage their existing data governance and management investments in Microsoft Fabric when grounding agent responses.

**Specific Features and Detailed Changes:**  
- **OneLake Catalog as a Knowledge Source:** Foundry IQ now supports the OneLake Catalog as a first-class knowledge source. This means agents can directly reference and utilize data assets registered in OneLake.
- **Single Registration:** Data engineers only need to register the OneLake Catalog once. After registration, all governed assets within the catalog become accessible to Foundry IQ agents.
- **Support for Multiple Asset Types:** The integration covers lakehouse tables, files, and shortcuts—enabling broad data coverage for agent grounding.
- **Governance Alignment:** Assets accessed via OneLake Catalog retain their governance and security settings as defined in Microsoft Fabric, ensuring compliance and data protection.

**Technical Mechanisms and Implementation Methods:**  
- **Catalog Registration:** Data engineers perform a one-time registration of the OneLake Catalog within Foundry IQ. This process establishes a connection between the knowledge source and the agent environment.
- **Catalog Discovery:** Once registered, Foundry IQ agents can enumerate and access tables, files, and shortcuts as knowledge sources. The catalog acts as a metadata layer, abstracting the underlying storage.
- **Governed Access:** All access to data assets is mediated through Microsoft Fabric’s governance controls, ensuring that permissions, lineage, and data policies are enforced.
- **Agent Grounding:** When responding to queries, Foundry IQ agents can ground their answers using the data assets from the OneLake Catalog, improving accuracy and relevance.

**Use Cases and Application Scenarios:**  
- **Data-Driven Agent Responses:** Organizations can deploy Foundry IQ agents that answer business or technical questions using up-to-date, governed data from their lakehouse environment.
- **Unified Data Access:** Teams benefit from a single point of access to diverse data assets (tables, files, shortcuts) without duplicating data or managing multiple knowledge sources.
- **Compliance-Centric Scenarios:** Enterprises with strict governance requirements can ensure that all agent interactions with data comply with organizational policies set in Microsoft Fabric.

**Important Considerations and Limitations:**  
- **Public Preview:** The feature is in public preview, which may entail limited support, potential changes, or feature gaps before general availability.
- **Governance Dependence:** Access and visibility are strictly governed by Microsoft Fabric configurations; misconfigured permissions may restrict agent access.
- **Asset Types Supported:** Only lakehouse tables, files, and shortcuts are supported as knowledge sources in this integration.

**Integration with Related Azure Services:**  
- **Microsoft Fabric:** The integration leverages Microsoft Fabric for governance, asset management, and policy enforcement.
- **OneLake:** OneLake serves as the unified data lake, with the catalog providing metadata and access control.
- **Foundry IQ:** Foundry IQ agents are enhanced by the ability to ground responses on governed data assets from OneLake.

**Summary:**  
The public preview of OneLake Catalog integration for Foundry IQ Knowledge Sources enables agents to ground responses on governed lakehouse tables, files, and shortcuts within Microsoft Fabric, streamlining data access and governance for enterprise scenarios.

---

### 64. Generally Available: Region-agnostic reservations for Global PTU in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Region-agnostic reservations for Global PTU in Microsoft Foundry](https://azure.microsoft.com/updates?id=563212)

**Update ID**: 563212
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry now offers region-agnostic reservations for Global Provisioned Throughput Units (PTUs) at general availability.

- Key changes or new features  
Customers can now reserve PTU capacity globally, rather than being restricted to a specific Azure region. This means a single PTU reservation can be consumed from any supported region, providing greater flexibility and simplifying capacity planning for distributed workloads.

- Target audience affected  
This update is relevant for developers and IT professionals managing workloads on Microsoft Foundry that require scalable and predictable throughput across multiple Azure regions. It is particularly beneficial for organizations with global operations or those deploying multi-region solutions.

- Important notes if any  
Existing region-specific PTU reservations remain valid, but new reservations can leverage the region-agnostic model. This change can help optimize costs and resource utilization for global deployments. Review your current PTU reservation strategy to take advantage of this increased flexibility. For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=563212

**Details**:

**Azure Update Report: Generally Available – Region-agnostic reservations for Global PTU in Microsoft Foundry**

**Background and Purpose of the Update**  
Microsoft Foundry previously required customers to reserve Provisioned Throughput Units (PTUs) for specific Azure regions. This regional binding limited flexibility and could lead to inefficient resource utilization, especially for organizations operating workloads across multiple geographies. The update introduces region-agnostic reservations for Global PTUs, now generally available, enabling customers to commit to PTU capacity once and utilize it from any supported region. The primary purpose is to simplify capacity management and optimize throughput allocation for globally distributed workloads.

**Specific Features and Detailed Changes**  
The key feature of this update is the ability to reserve PTU capacity in a global, region-agnostic manner. Customers are no longer required to designate a specific region when making a PTU reservation. Instead, a single commitment covers all supported regions, allowing PTU consumption wherever needed. This change eliminates the need to manage multiple regional reservations and provides a unified throughput pool accessible across global deployments.

**Technical Mechanisms and Implementation Methods**  
Technically, Microsoft Foundry now abstracts PTU reservations from regional boundaries. When a customer commits to a certain number of Global PTUs, these units are tracked and managed centrally. The Foundry platform allocates PTU resources dynamically to any supported region based on workload demand, ensuring that the committed throughput is available wherever required. The reservation and allocation process is managed through the Foundry control plane, which orchestrates PTU distribution and monitors usage across regions.

**Use Cases and Application Scenarios**  
Region-agnostic PTU reservations are particularly beneficial for organizations with distributed applications, multi-region failover strategies, or global data processing pipelines. For example, a SaaS provider with customers in North America, Europe, and Asia can reserve a single pool of PTUs and allocate throughput dynamically as user demand shifts geographically. This approach supports scenarios such as disaster recovery, global scaling, and time-zone-based workload distribution without the overhead of managing separate regional reservations.

**Important Considerations and Limitations**  
While region-agnostic reservations provide significant flexibility, customers should ensure that their workloads are compatible with the supported regions for Global PTU consumption. It is important to monitor PTU usage to avoid over-commitment or underutilization, as the unified pool may lead to contention if demand spikes simultaneously across multiple regions. Additionally, customers should review Foundry documentation for any region-specific limitations or operational constraints related to PTU allocation.

**Integration with Related Azure Services**  
This update enhances integration with other Azure services that leverage Microsoft Foundry for throughput provisioning. Services such as Azure Data Explorer, Azure Synapse, or custom analytics solutions can benefit from simplified PTU management and improved scalability. The region-agnostic model aligns with Azure’s global resource management strategies, enabling seamless integration with cross-region networking, failover, and geo-redundancy features.

**Summary Sentence**  
Microsoft Foundry now offers generally available region-agnostic reservations for Global PTUs, allowing customers to commit to throughput capacity once and consume it flexibly from any supported region, thereby streamlining capacity management and optimizing resource utilization for globally distributed workloads.

---

### 65. Generally Available: Speech SDK 1.50 for Azure AI Speech

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Speech SDK 1.50 for Azure AI Speech](https://azure.microsoft.com/updates?id=563192)

**Update ID**: 563192
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Speech SDK 1.50 for Azure AI Speech is now generally available across all supported programming languages.

- Key changes or new features  
This release consolidates the latest speech-to-text and text-to-speech capabilities, providing a stable API surface for developers. It includes updates and improvements to speech recognition and synthesis features, ensuring consistency and reliability across C#, C++, Java, JavaScript, Python, Objective-C, Swift, and Go. Developers can leverage the newest enhancements without breaking changes to their existing integrations.

- Target audience affected  
Developers and IT professionals building or maintaining applications that utilize Azure AI Speech services, particularly those working with speech recognition, transcription, or synthesis in any of the supported languages.

- Important notes if any  
Applications should be updated to use SDK version 1.50 to benefit from the latest features and stability improvements. Review the official release notes for language-specific changes or migration considerations. This update ensures long-term support and compatibility for future Azure AI Speech features.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=563192)

**Details**:

**Azure Update Technical Report: Speech SDK 1.50 for Azure AI Speech (Generally Available)**

**Background and Purpose of the Update**  
The release of Speech SDK 1.50 as generally available (GA) marks the culmination of ongoing enhancements to Azure AI Speech capabilities. The primary purpose of this update is to deliver the latest speech-to-text and text-to-speech features through a stable and unified API surface. By reaching GA status, this SDK version is now recommended for production workloads, ensuring long-term support and reliability for enterprise and developer adoption.

**Specific Features and Detailed Changes**  
Speech SDK 1.50 consolidates recent advancements in both speech-to-text and text-to-speech functionalities. This release is available across a broad spectrum of programming languages, including C#, C++, Java, JavaScript, Python, Objective-C, Swift, and Go. The update ensures that all supported languages have access to the latest features within a consistent API framework. This roll-up approach simplifies version management and reduces fragmentation, enabling developers to leverage new capabilities without disruptive API changes.

**Technical Mechanisms and Implementation Methods**  
The SDK provides client libraries that abstract the complexities of integrating Azure AI Speech services into applications. By exposing a stable API surface, Speech SDK 1.50 allows for seamless invocation of speech recognition and synthesis operations. The SDK handles authentication, network communication, and protocol management internally, enabling developers to focus on application logic. The multi-language support ensures that applications across different platforms and environments can uniformly access Azure AI Speech features.

**Use Cases and Application Scenarios**  
Speech SDK 1.50 is suitable for a wide range of voice-driven applications, including but not limited to:
- Real-time transcription services (speech-to-text) for meetings, customer support, and accessibility solutions.
- Voice assistants and chatbots requiring natural language understanding and text-to-speech output.
- Interactive voice response (IVR) systems in telephony and customer engagement platforms.
- Multilingual applications that require speech processing across different languages and locales.

**Important Considerations and Limitations**  
As a generally available release, Speech SDK 1.50 is intended for production use and benefits from Azure’s support and service-level agreements. However, developers must ensure compatibility with their target language and platform, as only the languages listed (C#, C++, Java, JavaScript, Python, Objective-C, Swift, and Go) are supported. It is also important to review the official documentation for any language-specific limitations or prerequisites.

**Integration with Related Azure Services**  
Speech SDK 1.50 is designed to integrate seamlessly with Azure AI Speech services, which are part of the broader Azure Cognitive Services suite. This enables developers to build comprehensive AI solutions that combine speech recognition, synthesis, and other cognitive capabilities such as translation and intent recognition. The SDK’s stable API surface facilitates integration with other Azure services, such as Azure Functions, Logic Apps, and Azure Bot Service, supporting scalable and maintainable architectures.

**Summary Sentence:**  
Speech SDK 1.50 is now generally available, providing a stable and unified API for the latest Azure AI Speech-to-Text and Text-to-Speech features across all major programming languages, streamlining integration for production-grade voice applications.

---

### 66. Public Preview: CLI and SDK support for Deployment Templates

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: CLI and SDK support for Deployment Templates](https://azure.microsoft.com/updates?id=563187)

**Update ID**: 563187
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Internet of Things, Azure Machine Learning, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Machine Learning Deployment Templates now support management via CLI and SDK, available in public preview.

- Key changes or new features  
Platform teams and developers can now create, update, delete, and manage deployment templates using the Azure CLI (az ml) and SDK, in addition to the Azure portal. This enables integration with infrastructure-as-code (IaC) pipelines, improving automation and repeatability for machine learning deployment workflows.

- Target audience affected  
This update is relevant for developers, DevOps engineers, and IT professionals managing Azure Machine Learning environments, especially those using IaC practices and automation pipelines.

- Important notes if any  
The CLI and SDK support is currently in public preview, so features and APIs may change before general availability. Users should test in non-production environments and monitor for updates. This enhancement streamlines template management and aligns with best practices for automated and version-controlled deployments in Azure ML.

**Details**:

**Azure Update Report: Public Preview – CLI and SDK Support for Deployment Templates in Azure Machine Learning**

**Background and Purpose of the Update:**  
Previously, management of deployment templates in Azure Machine Learning was limited to the Azure Portal, constraining automation and integration with infrastructure-as-code (IaC) workflows. This update introduces public preview support for managing deployment templates via the Azure CLI and SDK, empowering platform teams to automate template operations and integrate them directly into CI/CD pipelines and IaC processes.

**Specific Features and Detailed Changes:**  
- **CLI and SDK Support:** New commands are available through the `az ml` CLI and corresponding SDK methods, enabling programmatic management of deployment templates.
- **Template Lifecycle Management:** Users can now create, update, delete, and manage deployment templates entirely through scripts or code, removing reliance on manual portal operations.
- **Integration with Automation Pipelines:** These capabilities facilitate seamless integration with DevOps pipelines, allowing deployment templates to be managed as part of automated infrastructure provisioning and application deployment workflows.

**Technical Mechanisms and Implementation Methods:**  
- **Azure CLI (`az ml`) Integration:** The Azure Machine Learning CLI extension now exposes commands for deployment template management. These commands interact with the Azure Machine Learning service backend to perform CRUD (Create, Read, Update, Delete) operations on deployment templates.
- **SDK Enhancements:** The Azure Machine Learning SDK provides corresponding methods, allowing developers to manage templates using Python or other supported languages, enabling integration within custom scripts and applications.
- **IaC Compatibility:** By exposing deployment template management via CLI and SDK, templates can be version-controlled, parameterized, and deployed as part of repeatable, automated workflows, aligning with IaC best practices.

**Use Cases and Application Scenarios:**  
- **Automated Model Deployment:** Platform teams can automate the deployment of machine learning models using templates managed through code, ensuring consistency and repeatability across environments.
- **CI/CD Integration:** Deployment templates can be incorporated into CI/CD pipelines (e.g., Azure DevOps, GitHub Actions), enabling automated testing and deployment of ML services.
- **Template Versioning and Governance:** Teams can manage deployment templates in source control, track changes, and enforce governance policies through code reviews and automated checks.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should test thoroughly and monitor for updates or changes in functionality.
- **Command Scope:** The new CLI and SDK commands are specific to deployment templates within Azure Machine Learning. Users should refer to official documentation for supported parameters and usage patterns.
- **Portal Functionality:** Portal-based management remains available, but automation and integration are now possible via CLI and SDK.

**Integration with Related Azure Services:**  
- **Azure DevOps and GitHub Actions:** The CLI and SDK support enables direct integration with Azure DevOps pipelines and GitHub Actions for end-to-end ML lifecycle automation.
- **Resource Management:** Deployment templates managed via CLI and SDK can be linked with other Azure resources (e.g., compute, networking) as part of comprehensive IaC solutions.

**Summary Sentence:**  
Azure Machine Learning now supports public preview of deployment template management via CLI and SDK, enabling platform teams to automate template operations and integrate them into infrastructure-as-code pipelines for enhanced automation, consistency, and DevOps alignment.

---

### 67. Public Preview: Deployment Templates support packaging deployment configurations in registries for curated deployment

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Deployment Templates support packaging deployment configurations in registries for curated deployment](https://azure.microsoft.com/updates?id=563172)

**Update ID**: 563172
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Internet of Things, Azure Machine Learning, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Machine Learning deployment templates now support packaging deployment configurations in registries, available in public preview.

- Key changes or new features  
  - Deployment templates can now be sourced directly from model registries, not just from local or workspace sources.  
  - This allows users to package models, deployment configurations, and environment dependencies together in a registry, enabling curated and reusable deployments across multiple workspaces or teams.  
  - The update expands the set of registries that can be used for templated deployments, improving portability and governance.

- Target audience affected  
  - Machine Learning developers and MLOps engineers who manage model deployment workflows.  
  - IT professionals responsible for standardizing and governing ML deployment processes across teams or environments.

- Important notes if any  
  - This feature is in public preview and may be subject to changes before general availability.  
  - Using registries for deployment templates helps enforce consistency, versioning, and reuse of deployment assets, streamlining operationalization of ML models.  
  - Review Azure documentation for guidance on using deployment templates with registries and any preview limitations.

[More details](https://azure.microsoft.com/updates?id=563172)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Deployment Templates support packaging deployment configurations in registries for curated deployment  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563172)

---

**Background and Purpose of the Update:**

Azure Machine Learning (AML) has introduced public preview support for deployment templates that enable packaging deployment configurations in registries. The primary purpose of this update is to expand the set of model registries available as sources for templated deployments, thereby streamlining and standardizing the deployment process for machine learning models. This enhancement addresses the need for curated, reusable deployment workflows that can be sourced from multiple registries, promoting consistency and efficiency across teams and projects.

---

**Specific Features and Detailed Changes:**

- **Deployment from Registries:** Deployment templates now support deploying directly from registries. This means customers can select models and associated deployment configurations stored in registries as the source for their deployments.
- **Expanded Registry Support:** The update increases the number of model registries that can be used, allowing for greater flexibility in sourcing models and deployment configurations.
- **Packaging Deployment Configurations:** Deployment templates package not only the model but also the deployment configuration, which may include environment specifications, inference scripts, and other operational parameters.

---

**Technical Mechanisms and Implementation Methods:**

- **Registry Integration:** The deployment template mechanism interacts with Azure Machine Learning registries, enabling retrieval of models and deployment configurations. This integration leverages registry APIs to access and package the necessary assets.
- **Template Packaging:** Deployment templates encapsulate the model artifact and its deployment configuration into a single package, which can be versioned and reused. The packaging process ensures that all dependencies and operational parameters are included, reducing manual configuration errors.
- **Curated Deployment:** By supporting curated deployment, templates ensure that deployments follow predefined standards and best practices, which are encoded within the template and registry configuration.

---

**Use Cases and Application Scenarios:**

- **Enterprise Model Deployment:** Organizations can maintain a central registry of approved models and deployment templates, enabling teams to deploy models with consistent configurations.
- **Multi-Environment Deployment:** Templates can be reused across different environments (e.g., development, staging, production), ensuring uniformity in deployment processes.
- **Collaborative Model Sharing:** Teams can share curated deployment templates via registries, facilitating collaboration and reducing onboarding time for new projects.

---

**Important Considerations and Limitations:**

- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads due to potential instability or incomplete feature sets.
- **Registry Compatibility:** Only registries supported by Azure Machine Learning are compatible with this feature; unsupported registries cannot be used as sources for deployment templates.
- **Template Scope:** The deployment template packages the model and deployment configuration, but additional resources (such as data or external dependencies) may need to be managed separately.

---

**Integration with Related Azure Services:**

- **Azure Machine Learning Registries:** Direct integration with AML registries is central to this update, enabling model and configuration retrieval.
- **Azure Resource Manager (ARM):** Deployment templates may leverage ARM for resource provisioning during deployment.
- **Azure DevOps:** Teams can incorporate deployment templates into CI/CD pipelines for automated, repeatable deployments.

---

**Summary Sentence:**  
Deployment templates in Azure Machine Learning now support packaging deployment configurations in registries, enabling curated and consistent model deployments from an expanded set of model registries in public preview.

---

### 68. Public Preview: Benchmark evaluations for fine-tuned models in Microsoft Foundry

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Benchmark evaluations for fine-tuned models in Microsoft Foundry](https://azure.microsoft.com/updates?id=563167)

**Update ID**: 563167
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry now offers benchmark evaluations for fine-tuned models in Public Preview.

- Key changes or new features  
Developers and IT professionals can now systematically evaluate the performance of their fine-tuned AI models using standardized benchmarks directly within Microsoft Foundry. This includes support for various evaluation metrics across reasoning, math, and domain-specific knowledge, enabling more informed model selection and tuning. The feature helps compare custom fine-tuned models against public leaderboard models and measure real-world performance.

- Target audience affected  
AI/ML developers, data scientists, and IT professionals working with custom or fine-tuned models in Microsoft Foundry.

- Important notes if any  
Benchmark evaluations help identify the most suitable models for specific business needs, reducing the risk of underperformance in production scenarios. The feature is currently in Public Preview, so functionality and APIs may change before General Availability. Early adopters should monitor for updates and provide feedback to Microsoft.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=563167

**Details**:

**Azure Update Report: Public Preview – Benchmark Evaluations for Fine-Tuned Models in Microsoft Foundry**

**Background and Purpose of the Update**  
The update introduces benchmark evaluations for fine-tuned models within Microsoft Foundry, now available in public preview. The primary purpose is to address the complexity of selecting optimal AI systems, especially as newer or larger models do not always guarantee superior performance. Additionally, agents—software components that interact with models—introduce further variability, making it essential to evaluate models beyond public leaderboard scores. This update aims to provide IT professionals with robust evaluation tools for reasoning, mathematical, and domain-specific tasks, ensuring that chosen models meet real-world requirements.

**Specific Features and Detailed Changes**  
The public preview enables users to conduct benchmark evaluations on models that have been fine-tuned within Microsoft Foundry. Key features include:
- Access to standardized evaluation datasets and metrics tailored for reasoning, mathematics, and domain knowledge.
- Comparative analysis tools to assess fine-tuned models against baseline or public leaderboard models.
- Integration of evaluation workflows directly into the Foundry environment, streamlining the process for model developers and operators.

These features allow for more granular and relevant performance insights, moving beyond generic leaderboard results to task-specific benchmarks.

**Technical Mechanisms and Implementation Methods**  
Benchmark evaluations are implemented through automated testing pipelines within Microsoft Foundry. The mechanism involves:
- Selection of relevant benchmark datasets, which are curated to reflect reasoning, mathematical, and domain-specific challenges.
- Execution of evaluation scripts that measure model performance using standardized metrics (e.g., accuracy, F1 score, reasoning correctness).
- Aggregation and visualization of results within the Foundry interface, enabling users to interpret and compare performance across models and tasks.

The evaluation process is tightly integrated with the model fine-tuning workflow, allowing seamless transition from training to benchmarking.

**Use Cases and Application Scenarios**  
This update is particularly valuable in scenarios where:
- Organizations need to validate the effectiveness of custom fine-tuned models for specific business tasks (e.g., financial analysis, scientific reasoning, customer support).
- IT teams are comparing multiple models or agents to select the best fit for production deployment.
- Developers require evidence-based performance metrics to justify model selection to stakeholders.

The benchmark evaluations support both experimental and operational use cases, facilitating informed decision-making in AI system deployment.

**Important Considerations and Limitations**  
- The feature is currently in public preview, implying that it may not be fully supported or production-ready.
- Benchmark datasets and metrics are limited to those provided within Microsoft Foundry; custom benchmarks may require additional integration.
- Performance evaluation is constrained to reasoning, math, and domain knowledge tasks as described; other task types may not be covered.
- Variability introduced by agents may still require separate evaluation, depending on deployment architecture.

**Integration with Related Azure Services**  
Benchmark evaluations are designed to work natively within Microsoft Foundry, which is part of the broader Azure AI ecosystem. They complement existing model training and deployment workflows, and results can be used to inform downstream services such as Azure Machine Learning, Azure Cognitive Services, or custom AI solutions built on Azure infrastructure.

**Summary Sentence**  
The public preview of benchmark evaluations for fine-tuned models in Microsoft Foundry provides IT professionals with standardized tools to assess model performance on reasoning, math, and domain-specific tasks, enabling more informed AI system selection and deployment within the Azure ecosystem.

---

### 69. Generally Available: Azure Database for MySQL now available in new regions and expanded availability zones

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Database for MySQL now available in new regions and expanded availability zones](https://azure.microsoft.com/updates?id=563152)

**Update ID**: 563152
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Database for MySQL Flexible Server is now generally available in new regions and with expanded availability zone support.

- Key changes or new features  
  - Azure Database for MySQL Flexible Server can now be deployed in the following new regions: Denmark East, Austria East, and Belgium East.  
  - Enhanced support for Availability Zones in these regions improves high availability and disaster recovery capabilities.

- Target audience affected  
  - Developers and IT professionals who build, deploy, or manage MySQL-based applications on Azure, especially those with users or compliance needs in Denmark, Austria, or Belgium.

- Important notes if any  
  - The regional expansion allows organizations to deploy workloads closer to their users, reducing latency and helping meet data residency or sovereignty requirements.  
  - Availability Zone support offers increased resilience against datacenter-level failures, improving service uptime for mission-critical applications.  
  - Review regional pricing and service limitations before deployment, as features and costs may vary by region.

For more details, see the official update: https://azure.microsoft.com/updates?id=563152

**Details**:

**Azure Update Report**

**Title:** Generally Available: Azure Database for MySQL now available in new regions and expanded availability zones  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563152)

---

**Background and Purpose of the Update:**  
Azure Database for MySQL Flexible Server is a managed database service designed to provide high availability, scalability, and security for MySQL workloads in the cloud. The purpose of this update is to increase the global reach and resilience of the service by making it available in new Azure regions and expanding support for availability zones. This enables customers to deploy MySQL databases closer to their users and comply with regional data residency requirements.

**Specific Features and Detailed Changes:**  
With this update, Azure Database for MySQL Flexible Server can now be deployed in the following new regions:  
- Denmark East  
- Austria East  
- Belgium Central (incomplete region name in provided content, assumed as Belgium Central)

Additionally, the service now offers expanded support for availability zones in these regions. Availability zones are physically separate locations within an Azure region, providing enhanced fault tolerance and high availability for workloads.

**Technical Mechanisms and Implementation Methods:**  
Azure Database for MySQL Flexible Server leverages Azure’s infrastructure to offer managed MySQL instances with built-in backup, patching, and monitoring. The expanded regional availability means that the underlying compute, storage, and networking resources are provisioned within the new regions, allowing customers to select these locations during server deployment.  
Availability zone support is implemented by distributing resources across multiple isolated zones within a region. This architecture ensures that database instances remain operational even if one zone experiences a failure, thereby minimizing downtime and improving service reliability.

**Use Cases and Application Scenarios:**  
- **Data Residency Compliance:** Organizations with regulatory requirements can now deploy MySQL databases in Denmark East, Austria East, and Belgium Central, ensuring data remains within specified geographic boundaries.
- **Reduced Latency:** Deploying databases closer to end-users in these regions improves application responsiveness and user experience.
- **High Availability Solutions:** By utilizing availability zones, customers can architect solutions that require business continuity and disaster recovery, such as mission-critical web applications, SaaS platforms, and transactional systems.

**Important Considerations and Limitations:**  
- Customers should verify the specific features and SKUs available in the new regions, as some advanced configurations or performance tiers may not be immediately supported.
- Availability zone support is region-specific; not all regions may offer the same level of zone redundancy.
- Network latency and inter-zone communication should be considered when designing highly available architectures.

**Integration with Related Azure Services:**  
Azure Database for MySQL Flexible Server integrates seamlessly with other Azure services, including:  
- **Azure Virtual Network:** For secure, private connectivity to MySQL servers.
- **Azure Backup:** For automated backup and restore capabilities.
- **Azure Monitor:** For performance and health monitoring.
- **Azure App Service and Azure Kubernetes Service:** For deploying applications that require backend MySQL databases.

---

**Summary Sentence:**  
Azure Database for MySQL Flexible Server is now generally available in Denmark East, Austria East, and Belgium Central regions, with expanded support for availability zones, enabling customers to deploy highly available, regionally compliant MySQL workloads with enhanced resilience and integration across Azure services.

---

### 70. Generally Available: Azure Database for MySQL Flexible Server self-service quota management experience

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Database for MySQL Flexible Server self-service quota management experience](https://azure.microsoft.com/updates?id=563147)

**Update ID**: 563147
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Database for MySQL Flexible Server now offers a generally available self-service quota management experience.

- Key changes or new features  
Users can now manage their resource quotas directly via the Azure Quotas blade in the Azure portal. This includes the ability to:
  - View current quota usage and limits for MySQL Flexible Server resources.
  - Submit quota increase requests through a streamlined, self-service process.
  - Track the status of quota requests for better transparency and control.

- Target audience affected  
Developers, database administrators, and IT professionals managing Azure Database for MySQL Flexible Server resources.

- Important notes if any  
This update simplifies and accelerates quota management, reducing dependency on support tickets and manual processes. It enables faster scaling and resource planning for MySQL workloads. Users should familiarize themselves with the Azure Quotas blade to take full advantage of the new self-service capabilities.

For more details, see the official update: https://azure.microsoft.com/updates?id=563147

**Details**:

**Comprehensive Technical Explanation: Azure Database for MySQL Flexible Server Self-Service Quota Management (Generally Available)**

**Background and Purpose of the Update:**  
The update addresses the need for improved quota management within Azure Database for MySQL Flexible Server. Previously, quota adjustments and visibility were often handled through support requests or indirect mechanisms, leading to delays and reduced transparency. The purpose of this update is to empower IT professionals and database administrators with direct, streamlined control over quota management, enhancing operational efficiency and resource planning.

**Specific Features and Detailed Changes:**  
The Azure Database for MySQL Flexible Server now supports self-service quota management via the Azure Quotas blade in the Azure portal. Key features include:
- **Quota Visibility:** Users can view their current quota usage and limits for MySQL Flexible Server resources directly in the portal.
- **Quota Requests:** Administrators can submit quota increase requests through the self-service interface, eliminating the need for manual support tickets.
- **Simplified Workflow:** The process is faster and more transparent, with clear feedback on quota status and request progress.

**Technical Mechanisms and Implementation Methods:**  
The self-service quota management is implemented through the Azure Quotas blade, which is integrated into the Azure portal. This blade provides a unified interface for quota management across various Azure services. For MySQL Flexible Server:
- **Quota Data Integration:** Real-time quota usage and limits are displayed by querying backend resource management APIs.
- **Request Handling:** When a quota increase is requested, the portal initiates an automated workflow that validates the request and updates quota allocations accordingly, subject to internal policies and resource availability.
- **Role-Based Access Control (RBAC):** Access to quota management functions is governed by Azure RBAC, ensuring only authorized users can view or modify quotas.

**Use Cases and Application Scenarios:**  
- **Scaling Operations:** Organizations scaling their MySQL Flexible Server deployments can proactively manage quotas to avoid resource bottlenecks.
- **Resource Planning:** IT teams can monitor quota usage trends and plan for future growth without waiting for support intervention.
- **Dev/Test Environments:** Developers can quickly adjust quotas to accommodate testing scenarios, improving agility and reducing downtime.
- **Compliance and Auditing:** Transparent quota management supports compliance requirements by providing clear records of resource allocations and changes.

**Important Considerations and Limitations:**  
- **Quota Increase Approval:** While requests are self-service, actual quota increases may still be subject to Azure’s internal validation and approval processes.
- **Portal Dependency:** All quota management activities must be performed through the Azure portal’s Quotas blade; API or CLI support is not mentioned in the update.
- **Scope:** The feature is specific to Azure Database for MySQL Flexible Server and does not necessarily extend to other MySQL offerings or Azure database services.
- **Permissions:** Users must have appropriate permissions to access and modify quota settings, as enforced by Azure RBAC.

**Integration with Related Azure Services:**  
The Azure Quotas blade is a centralized interface for quota management across multiple Azure services, promoting consistency and ease of use. For MySQL Flexible Server, this integration enables:
- **Unified Resource Management:** Administrators can manage quotas alongside other Azure resources, such as compute, storage, and networking, within the same portal experience.
- **Interoperability:** Quota management aligns with Azure’s broader resource governance and monitoring capabilities, facilitating seamless integration with tools like Azure Monitor and Azure Policy.

**Summary Sentence:**  
Azure Database for MySQL Flexible Server now offers a generally available self-service quota management experience through the Azure Quotas blade in the portal, enabling faster, simpler, and more transparent quota visibility and adjustment for IT professionals.

---

### 71. Generally Available: Azure SQL updates for June

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure SQL updates for June](https://azure.microsoft.com/updates?id=563137)

**Update ID**: 563137
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure SQL received updates in June 2026, specifically enhancing the MSSQL extension for Visual Studio Code.

- Key changes or new features  
Developers can now execute SQL queries, document workflows using Markdown, and combine multiple kernels (such as Python and SQL) within SQL Notebooks directly in the MSSQL extension for VS Code. This enables more interactive and flexible data exploration and documentation workflows.

- Target audience affected  
These updates primarily impact developers, data engineers, and IT professionals who use Visual Studio Code for database development and management, especially those leveraging Azure SQL and integrated data science workflows.

- Important notes if any  
The new features improve productivity by allowing users to mix code and documentation in a single environment, supporting advanced scenarios like data analysis and reporting. Users should ensure they are running the latest version of the MSSQL extension to access these capabilities. For more details, refer to the official Azure update documentation.

**Details**:

**Azure SQL Updates for June 2026 – Technical Report**

**Background and Purpose of the Update**  
The June 2026 Azure SQL update focuses on enhancing developer productivity and flexibility by improving the integration between Azure SQL and the development environment. Specifically, the update targets the MSSQL extension for Visual Studio Code, a widely used tool for database development and management. The purpose is to streamline workflows by enabling direct execution of SQL queries, improved documentation capabilities, and support for multi-language (polyglot) data analysis within a single interface.

**Specific Features and Detailed Changes**  
Key features introduced or enhanced in this update include:

1. **SQL Query Execution in Notebooks**: Users can now execute SQL queries directly within SQL Notebooks in the MSSQL extension for Visual Studio Code. This allows for interactive querying and immediate feedback within the development environment.
2. **Markdown Documentation**: The update adds support for Markdown cells within SQL Notebooks. This enables users to document their queries, results, and analytical processes in a readable and structured format alongside executable code.
3. **Mixed Kernel Support (Polyglot Notebooks)**: Users can now mix kernels such as Python with SQL within the same notebook. This feature enables seamless integration of data querying (SQL) and advanced data processing or visualization (Python), supporting richer data workflows.

**Technical Mechanisms and Implementation Methods**  
- The MSSQL extension leverages Visual Studio Code’s notebook interface, which supports cell-based execution and rendering.
- SQL cells are executed against configured Azure SQL databases, with results rendered inline.
- Markdown cells utilize the standard Markdown rendering engine in VS Code, allowing for formatted text, images, and links.
- Kernel mixing is enabled by the underlying notebook architecture, which allows different cells to be executed by different interpreters (e.g., SQL kernel for SQL cells, Python kernel for Python cells), with shared context where supported.

**Use Cases and Application Scenarios**  
- **Data Exploration and Analysis**: Data scientists and analysts can query Azure SQL databases, process results with Python, and document findings—all within a single notebook.
- **Database Development and Testing**: Developers can write, test, and document SQL scripts, and include Python-based test automation or data validation.
- **Collaborative Documentation**: Teams can create living documents that combine executable code, results, and explanatory text, facilitating knowledge sharing and reproducibility.

**Important Considerations and Limitations**  
- The features are available within the MSSQL extension for Visual Studio Code; users must ensure they have the latest version installed.
- Mixed kernel support may require additional configuration, such as Python environment setup, and may have limitations on variable sharing between kernels.
- Notebooks are best suited for interactive and exploratory workflows; for production automation, traditional scripts or pipelines may be preferable.

**Integration with Related Azure Services**  
- The update is designed to work with Azure SQL databases, including Azure SQL Database and Azure SQL Managed Instance.
- Notebooks can be used in conjunction with other Azure data services (e.g., Azure Data Studio, Azure Machine Learning) by exporting or sharing notebook files.
- Integration with Azure DevOps or GitHub is facilitated by storing notebooks as version-controlled files.

**Summary**  
The June 2026 Azure SQL update enhances the MSSQL extension for Visual Studio Code by enabling SQL query execution, Markdown documentation, and mixed-language (e.g., Python and SQL) workflows within SQL Notebooks, improving productivity and collaboration for data professionals.

---

### 72. Generally Available: GitHub Copilot integration in Schema Designer for the MSSQL extension

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: GitHub Copilot integration in Schema Designer for the MSSQL extension](https://azure.microsoft.com/updates?id=563132)

**Update ID**: 563132
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Build, Feature

**Summary**:

- What was updated  
The GitHub Copilot integration is now generally available in the Schema Designer within the MSSQL extension for Visual Studio Code.

- Key changes or new features  
Developers can now leverage GitHub Copilot’s AI-powered code suggestions directly while designing and editing SQL database schemas visually in VS Code. This integration streamlines schema creation, modification, and review by providing context-aware recommendations and automating repetitive tasks within the Schema Designer interface.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use Visual Studio Code with the MSSQL extension for SQL Server database development and management.

- Important notes if any  
The feature is based on user feedback and aims to enhance productivity by integrating AI assistance into database schema workflows. Users need an active GitHub Copilot subscription to access Copilot features. The update supports modern database development practices and can help teams accelerate schema design and reduce manual errors.

For more details, see the official update: https://azure.microsoft.com/updates?id=563132

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: GitHub Copilot integration in Schema Designer for the MSSQL extension

**Background and Purpose of the Update:**  
The integration of GitHub Copilot with Schema Designer in the MSSQL extension for Visual Studio Code has reached general availability. This update is driven by developer feedback and the need for enhanced workflows in database schema design. The primary purpose is to augment the visual schema design experience with AI-assisted capabilities, thereby improving productivity and reducing manual effort in designing and managing SQL Server schemas.

**Specific Features and Detailed Changes:**  
With this release, the Schema Designer within the MSSQL extension now leverages GitHub Copilot to provide AI-powered assistance directly in Visual Studio Code. Key features include:
- AI-generated suggestions for schema design, such as table creation, column definitions, and relationships.
- Context-aware code completion and recommendations based on the current schema and user input.
- Enhanced visual experience, allowing users to interact with schema objects and receive Copilot-driven guidance in real time.
- Seamless integration, enabling developers to utilize Copilot’s capabilities without leaving the Schema Designer interface.

**Technical Mechanisms and Implementation Methods:**  
The integration is implemented within the MSSQL extension for Visual Studio Code, utilizing GitHub Copilot’s AI engine. Copilot analyzes the schema context and developer actions to generate relevant suggestions. The technical workflow involves:
- Copilot accessing schema metadata and user input within the Schema Designer.
- Real-time communication between the extension and Copilot’s cloud-based AI service.
- Suggestions are rendered in the Schema Designer UI, allowing users to accept, modify, or reject them.
- The extension maintains compatibility with standard MSSQL workflows, ensuring that Copilot’s recommendations are aligned with SQL Server best practices.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial in scenarios such as:
- Rapid prototyping of database schemas, where developers need to quickly iterate on table structures and relationships.
- Onboarding new team members, who can leverage Copilot’s suggestions to learn schema design conventions.
- Reducing errors in schema creation, as Copilot provides context-aware recommendations that adhere to SQL Server syntax and practices.
- Collaborative development environments, where multiple users can benefit from consistent, AI-assisted schema design guidance.

**Important Considerations and Limitations:**  
- The integration is available only within the Schema Designer of the MSSQL extension for Visual Studio Code.
- Copilot’s suggestions are based on AI models and may require review for accuracy and alignment with organizational standards.
- Users must have appropriate permissions and licenses for GitHub Copilot to access its features.
- The extension relies on internet connectivity to communicate with Copilot’s cloud service.

**Integration with Related Azure Services:**  
While the update is focused on Visual Studio Code and the MSSQL extension, it complements Azure SQL Database development workflows. Developers designing schemas for Azure SQL Database can utilize Copilot-assisted Schema Designer to streamline schema creation and management, ensuring compatibility with Azure-hosted SQL Server instances.

**Summary Sentence:**  
The general availability of GitHub Copilot integration in Schema Designer for the MSSQL extension enhances the Visual Studio Code experience by providing AI-assisted schema design capabilities, streamlining SQL Server development workflows for technical professionals.

---

### 73. Generally Available: Data API builder with built-in GitHub Copilot in MSSQL extension

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Data API builder with built-in GitHub Copilot in MSSQL extension](https://azure.microsoft.com/updates?id=563127)

**Update ID**: 563127
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Build, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now includes the Data API builder with built-in GitHub Copilot integration, which is now generally available.

- Key changes or new features  
Developers can now use the Data API builder directly within the MSSQL extension to quickly generate REST, GraphQL, and Model Context APIs for SQL databases. The integration with GitHub Copilot provides AI-powered guidance and code suggestions, streamlining the process of building and configuring back-end APIs. This feature enables faster prototyping and development by automating much of the API creation workflow.

- Target audience affected  
This update is relevant for developers and IT professionals who use Visual Studio Code for SQL Server or Azure SQL development, especially those building data-driven applications that require REST or GraphQL APIs.

- Important notes if any  
The feature is generally available and can be accessed by updating the MSSQL extension in Visual Studio Code. The Copilot integration helps reduce manual coding and configuration, but developers should review generated code for security and compliance. This update enhances productivity for teams adopting API-first or modern application architectures.  
For more information, see the official [Azure Update](https://azure.microsoft.com/updates?id=563127).

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Data API builder with built-in GitHub Copilot in MSSQL extension  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563127)

---

**Background and Purpose of the Update**

This update announces the general availability of the Data API builder with integrated GitHub Copilot support within the MSSQL extension for Visual Studio Code. The primary purpose is to streamline and accelerate back-end development workflows for SQL Server databases by enabling developers to generate APIs and model contexts directly from their database schema, leveraging AI-assisted guidance.

---

**Specific Features and Detailed Changes**

- **Data API Builder Integration:** The MSSQL extension now includes a Data API builder, allowing users to generate REST and GraphQL endpoints, as well as Model Contexts, directly from their SQL Server database objects.
- **GitHub Copilot Built-In:** The extension incorporates GitHub Copilot, providing AI-powered suggestions and code completions during API generation, enhancing productivity and reducing manual coding errors.
- **General Availability:** The feature is now production-ready and supported for all users of the MSSQL extension in Visual Studio Code.

---

**Technical Mechanisms and Implementation Methods**

- **Extension Architecture:** The MSSQL extension operates within Visual Studio Code, interfacing with SQL Server databases. The Data API builder leverages database introspection to read schema definitions and automatically generate API endpoints.
- **REST and GraphQL Generation:** The builder creates RESTful and GraphQL APIs based on table and view structures, exposing CRUD operations and query capabilities without manual endpoint coding.
- **Model Context Generation:** The extension can generate model contexts, which are representations of database entities, facilitating integration with application code.
- **Copilot Integration:** GitHub Copilot is embedded within the extension, providing real-time AI suggestions for API configurations, query definitions, and model context generation, based on the database schema and developer input.

---

**Use Cases and Application Scenarios**

- **Rapid API Development:** Developers can quickly expose SQL Server data as REST or GraphQL APIs, ideal for building web, mobile, or microservices applications.
- **Prototyping and Proof-of-Concepts:** The extension enables fast prototyping by automating API scaffolding, reducing setup time for new projects.
- **Model Context Generation:** Useful for generating data access layers or integrating with ORM frameworks in application development.
- **AI-Assisted Coding:** Copilot integration helps developers write API definitions and model contexts more efficiently, especially for complex schemas.

---

**Important Considerations and Limitations**

- **Supported Database:** The feature is specific to SQL Server databases accessed via the MSSQL extension in Visual Studio Code.
- **API Customization:** While the builder automates endpoint generation, advanced customization may require manual adjustments.
- **Copilot Usage:** GitHub Copilot suggestions depend on the context and may require review for accuracy and security.
- **Production Readiness:** As the feature is generally available, it is suitable for production use, but users should validate generated APIs for compliance and performance.

---

**Integration with Related Azure Services**

- **Azure SQL Database:** The extension can connect to Azure SQL Database instances, enabling API generation for cloud-hosted databases.
- **Azure App Services:** Generated APIs can be deployed to Azure App Services for scalable web and mobile backend hosting.
- **Azure Functions:** REST and GraphQL endpoints generated can be integrated with Azure Functions for serverless workflows.
- **Azure DevOps:** The extension’s integration with Visual Studio Code supports CI/CD pipelines via Azure DevOps for automated deployment.

---

**Summary Sentence**

The MSSQL extension for Visual Studio Code now offers a generally available Data API builder with built-in GitHub Copilot integration, enabling developers to efficiently generate REST, GraphQL, and Model Contexts for SQL Server databases with AI-assisted guidance, streamlining back-end development workflows.

---

### 74. Public Preview: Azure SQL Database provisioning in the MSSQL extension

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure SQL Database provisioning in the MSSQL extension](https://azure.microsoft.com/updates?id=563122)

**Update ID**: 563122
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Build, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now supports provisioning Azure SQL Databases directly from the editor, available in public preview.

- Key changes or new features  
  - Developers can create and connect to a fully managed Azure SQL Database (starting with the free tier) without leaving Visual Studio Code.  
  - The extension provides a guided workflow for database provisioning and connection setup.  
  - This feature streamlines development and testing by integrating cloud database creation into the local development environment.

- Target audience affected  
  - Developers and IT professionals who use Visual Studio Code for database development and management.  
  - Teams adopting Azure SQL Database for application development, testing, or prototyping.

- Important notes if any  
  - The feature is currently limited to the free tier of Azure SQL Database during public preview.  
  - Users can quickly provision and connect to cloud databases at no cost, making it ideal for experimentation and early-stage development.  
  - Feedback during the preview phase is encouraged to help improve the feature before general availability.

[Learn more](https://azure.microsoft.com/updates?id=563122)

**Details**:

**Azure Update Summary: Public Preview: Azure SQL Database provisioning in the MSSQL extension**

**Background and Purpose of the Update:**  
This update introduces the capability to provision Azure SQL Databases directly from the MSSQL extension within Visual Studio Code. The primary goal is to streamline the workflow for developers and database administrators by enabling the creation and connection to fully managed Azure SQL Databases without leaving the code editor environment. This feature is initially available for the free tier, allowing users to evaluate and utilize Azure SQL Database at no cost.

**Specific Features and Detailed Changes:**  
- **Azure SQL Database Provisioning:** Users can now create new Azure SQL Database instances directly from the MSSQL extension in Visual Studio Code.
- **Free Tier Support:** The provisioning capability is currently limited to the free tier, enabling users to deploy and connect to a cost-free, fully managed cloud database.
- **Guided Workflow:** The extension provides a guided wizard or workflow, simplifying the process of database creation and connection setup within the editor.
- **Direct Connection:** After provisioning, users can immediately connect to the newly created database for development and management tasks.

**Technical Mechanisms and Implementation Methods:**  
The MSSQL extension integrates with Azure APIs to facilitate database provisioning. When a user initiates the creation of an Azure SQL Database, the extension communicates with Azure Resource Manager (ARM) services to deploy the database instance in the cloud. Authentication and authorization are managed through the user’s Azure credentials, ensuring secure access and resource management. The guided workflow abstracts the complexity of resource configuration, presenting a user-friendly interface within Visual Studio Code.

**Use Cases and Application Scenarios:**  
- **Rapid Development and Prototyping:** Developers can quickly spin up a managed SQL database for testing, prototyping, or development purposes without navigating the Azure Portal.
- **Learning and Experimentation:** The free tier and integrated workflow make it easy for students, new users, or teams evaluating Azure SQL Database to get started with minimal setup.
- **Streamlined DevOps Pipelines:** Teams can automate or standardize database provisioning as part of their development workflow, reducing context switching and manual steps.

**Important Considerations and Limitations:**  
- **Public Preview:** This feature is in public preview, meaning it may be subject to changes and is not recommended for production workloads.
- **Free Tier Only:** Provisioning is currently limited to the free tier of Azure SQL Database; users requiring higher tiers or production-grade resources must use other provisioning methods.
- **Editor Dependency:** The feature is available exclusively through the MSSQL extension in Visual Studio Code and may not be accessible from other IDEs or tools.

**Integration with Related Azure Services:**  
The MSSQL extension leverages Azure Resource Manager for resource provisioning and integrates with Azure SQL Database, a fully managed relational database service. Users can manage authentication using their Azure Active Directory credentials, and the created databases are fully compatible with other Azure data services and tools, enabling seamless integration into broader Azure-based solutions.

**Summary Sentence:**  
The MSSQL extension for Visual Studio Code now allows users to provision and connect to free-tier Azure SQL Databases directly within the editor via a guided workflow, streamlining development and evaluation of managed cloud databases without leaving the coding environment.

---

### 75. Public Preview: MCP toolkit for Azure DocumentDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: MCP toolkit for Azure DocumentDB](https://azure.microsoft.com/updates?id=563112)

**Update ID**: 563112
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure DocumentDB now supports the Model Context Protocol (MCP) through a new MCP toolkit, available in public preview.

- Key changes or new features  
The MCP toolkit enables direct integration between Azure DocumentDB and AI agents or large language model (LLM)-powered applications. This allows developers to perform natural language queries, document retrieval, and other AI-driven operations on DocumentDB data. The toolkit simplifies connecting LLMs to your database, making it easier to build intelligent, context-aware applications.

- Target audience affected  
Developers building AI, machine learning, or LLM-powered applications; IT professionals managing Azure DocumentDB environments; solution architects designing intelligent data solutions.

- Important notes if any  
This feature is currently in public preview and may be subject to changes before general availability. Users should evaluate the toolkit in non-production environments and monitor for updates. Documentation and API references are available to assist with integration.

[Learn more](https://azure.microsoft.com/updates?id=563112)

**Details**:

**Azure Update Report: Public Preview – MCP Toolkit for Azure DocumentDB**

**Background and Purpose of the Update**  
Azure DocumentDB introduces support for the Model Context Protocol (MCP) via a dedicated toolkit, now available in public preview. The primary goal of this update is to facilitate seamless integration between DocumentDB and AI agents or applications powered by large language models (LLMs). This enhancement is designed to enable direct, natural language interaction with DocumentDB, streamlining the development of AI-driven solutions that require dynamic data access and manipulation.

**Specific Features and Detailed Changes**  
- **MCP Toolkit Availability:** The MCP toolkit is now accessible for Azure DocumentDB, allowing developers to leverage the protocol for enhanced connectivity.
- **Natural Language Queries:** With MCP support, AI agents and LLM-based applications can issue natural language queries directly to DocumentDB, simplifying data retrieval and interaction.
- **Document Retrieval:** The toolkit enables efficient document retrieval operations, making it easier for AI applications to fetch relevant data from DocumentDB collections.
- **Public Preview Release:** The features are currently in public preview, indicating that they are available for testing and feedback but may not yet be suitable for production workloads.

**Technical Mechanisms and Implementation Methods**  
- **Model Context Protocol (MCP):** MCP is a protocol designed to standardize the way AI models interact with data sources. By implementing MCP, DocumentDB exposes endpoints and interfaces that are compatible with AI agents and LLM-powered applications.
- **Direct Database Connectivity:** The MCP toolkit facilitates direct connections between AI applications and DocumentDB, bypassing the need for custom middleware or translation layers for natural language processing.
- **Natural Language Processing Integration:** The toolkit interprets natural language queries from AI agents, translates them into DocumentDB queries, and returns results in a format suitable for further AI processing.

**Use Cases and Application Scenarios**  
- **AI-Powered Search:** Organizations can build intelligent search solutions where users interact with DocumentDB using natural language, powered by LLMs.
- **Conversational AI Agents:** Virtual assistants and chatbots can retrieve and manipulate data from DocumentDB in real time, enhancing user experiences with contextual information.
- **Automated Document Analysis:** LLM applications can automate document retrieval and analysis tasks, leveraging the MCP toolkit for efficient data access.

**Important Considerations and Limitations**  
- **Preview Status:** As the MCP toolkit is in public preview, it may not offer full production-level support, and features or APIs may change before general availability.
- **Documentation and Support:** Users should refer to the official Azure documentation for the latest guidance and report any issues encountered during the preview phase.
- **Security and Compliance:** Evaluate the security implications of enabling direct AI agent access to DocumentDB, and ensure compliance with organizational policies.

**Integration with Related Azure Services**  
- **Azure AI Services:** The MCP toolkit is designed to work with AI agents and LLM-powered applications, which may be built using Azure OpenAI Service or Azure Cognitive Services.
- **Azure DocumentDB Ecosystem:** The toolkit enhances the existing capabilities of DocumentDB, allowing it to serve as a backend for AI-driven solutions without additional integration layers.

**Summary:**  
The public preview of the MCP toolkit for Azure DocumentDB enables direct, natural language interaction between AI agents or LLM-powered applications and DocumentDB, streamlining document retrieval and query operations for intelligent application development.

---

### 76. Public Preview: BM25 full-text search in Azure HorizonDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: BM25 full-text search in Azure HorizonDB](https://azure.microsoft.com/updates?id=563107)

**Update ID**: 563107
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Build, Feature

**Summary**:

- **What was updated**  
BM25 full-text search is now available in public preview for Azure HorizonDB.

- **Key changes or new features**  
Azure HorizonDB now supports BM25, a state-of-the-art relevance ranking algorithm widely used in search engines like Elasticsearch, Solr, and Azure AI Search. This enables production-quality keyword search capabilities natively within HorizonDB, allowing developers to perform advanced full-text search queries with improved relevance ranking directly inside the database, without the need for external search services.

- **Target audience affected**  
Developers and IT professionals building applications on Azure HorizonDB who require advanced search functionality, especially those migrating from or integrating with systems like Elasticsearch or Azure AI Search.

- **Important notes if any**  
This feature is currently in public preview and may not be suitable for all production workloads. Users should evaluate the feature in test environments and monitor for updates before adopting in critical production systems. Documentation and API support are available to help integrate BM25 search into existing HorizonDB solutions.

[Read more](https://azure.microsoft.com/updates?id=563107)

**Details**:

**Azure Update Report: Public Preview – BM25 Full-Text Search in Azure HorizonDB**

**Background and Purpose of the Update:**  
This update introduces BM25 full-text search capabilities in public preview for Azure HorizonDB. The primary goal is to enhance the search experience within HorizonDB by leveraging BM25, a widely adopted relevance ranking algorithm. BM25 is recognized for its effectiveness in keyword search scenarios and is used by major search engines such as Elasticsearch, Solr, and Azure AI Search. By integrating BM25 directly into HorizonDB, Microsoft aims to provide production-quality search relevance natively within the database.

**Specific Features and Detailed Changes:**  
- **BM25 Algorithm Integration:** HorizonDB now supports BM25-based full-text search, enabling advanced keyword search functionalities.
- **Production-Quality Search:** The search experience is designed to meet production standards, offering improved relevance and ranking for search results.
- **Native Execution:** The BM25 search runs entirely inside HorizonDB, eliminating the need for external search engines or additional infrastructure.

**Technical Mechanisms and Implementation Methods:**  
- **BM25 Relevance Ranking:** BM25 is a probabilistic information retrieval model that scores documents based on term frequency, inverse document frequency, and document length normalization. This results in more accurate and relevant search results for keyword queries.
- **In-Database Processing:** All BM25 computations and search operations are performed within HorizonDB, ensuring low-latency access and simplified architecture without the need for data synchronization with external search services.

**Use Cases and Application Scenarios:**  
- **Enterprise Applications:** Applications requiring advanced search capabilities for structured or semi-structured data stored in HorizonDB can benefit from BM25’s relevance ranking.
- **Content Management Systems:** Solutions that manage large volumes of documents or articles can implement BM25 search to improve user experience in content discovery.
- **Business Intelligence:** Data analysts can leverage BM25 search for faster and more relevant querying of textual data within HorizonDB.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be recommended for mission-critical workloads until general availability. Users should evaluate the feature in test or development environments before production deployment.
- **Feature Scope:** The update specifically enables BM25-based keyword search. No additional details about language support, advanced query syntax, or integration with other search features are provided in this release.

**Integration with Related Azure Services:**  
- **Alignment with Azure AI Search:** BM25 is the same algorithm used in Azure AI Search, ensuring consistency in search relevance for organizations utilizing both HorizonDB and Azure AI Search.
- **Standalone Functionality:** The BM25 search capability operates entirely within HorizonDB, reducing the need for external search services or complex integration scenarios.

**Summary:**  
BM25 full-text search is now available in public preview for Azure HorizonDB, providing production-quality keyword search with advanced relevance ranking natively within the database.

---

### 77. Public Preview: Advanced filtering for DiskANN vector search in Azure HorizonDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Advanced filtering for DiskANN vector search in Azure HorizonDB](https://azure.microsoft.com/updates?id=563102)

**Update ID**: 563102
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Advanced filtering for DiskANN vector search in Azure HorizonDB is now available in public preview.

- Key changes or new features  
This update introduces advanced metadata filtering capabilities to DiskANN-based vector search in HorizonDB. Developers can now combine vector similarity searches with structured metadata filters (e.g., category, date range, price, tenant ID) in a single query. This enables more precise and relevant search results without sacrificing performance.

- Target audience affected  
Developers and IT professionals building AI, search, or recommendation solutions using Azure HorizonDB, especially those leveraging vector similarity search and requiring complex filtering.

- Important notes if any  
The advanced filtering feature is currently in public preview and may not be suitable for production workloads. This enhancement allows for more granular control over search results, supporting use cases such as multi-tenant applications, e-commerce, and content recommendation systems. Review the official documentation for API usage details and limitations during the preview phase.

Data source: Using API data  
[Azure Update Link](https://azure.microsoft.com/updates?id=563102)

**Details**:

**Background and Purpose of the Update**  
The public preview of advanced filtering for DiskANN vector search in Azure HorizonDB addresses the need for more precise and efficient retrieval of vector-based data. Traditionally, vector similarity search retrieves items based solely on their vector proximity, which can be limiting when datasets are large and contain diverse metadata. This update enables users to refine search results by combining vector similarity with additional metadata filters, enhancing the relevance and specificity of search outcomes for enterprise-scale applications.

**Specific Features and Detailed Changes**  
With this release, Azure HorizonDB’s DiskANN vector search now supports advanced filtering capabilities. Users can apply metadata filters—such as category, date range, price, or tenant ID—in conjunction with vector similarity queries. This means that search operations can return only those items that are both similar in vector space and meet specified metadata criteria. The update ensures that these combined queries do not degrade search performance, maintaining the efficiency of DiskANN’s approximate nearest neighbor (ANN) search algorithm.

**Technical Mechanisms and Implementation Methods**  
The advanced filtering feature is implemented by integrating metadata-based filtering directly into the DiskANN vector search pipeline. When a query is executed, the system first applies the specified metadata filters to narrow down the candidate set. DiskANN then performs vector similarity search only within this filtered subset. This approach leverages efficient indexing and query execution strategies to ensure that the addition of metadata filters does not introduce significant latency or resource overhead.

**Use Cases and Application Scenarios**  
- **Personalized Recommendations:** E-commerce platforms can use vector search to find similar products, while filtering by category or price range to tailor recommendations.
- **Multi-tenant Solutions:** SaaS providers can ensure that search results are restricted to a specific tenant’s data by filtering on tenant ID.
- **Time-bound Searches:** Applications can combine vector similarity with date range filters to retrieve relevant documents or media within a specific timeframe.
- **Content Moderation:** Systems can search for similar images or text, filtered by content category or moderation status.

**Important Considerations and Limitations**  
- The advanced filtering feature is currently in public preview, which may imply limited support and potential changes before general availability.
- Performance is maintained when combining vector search with metadata filters, but users should validate this in their specific workload scenarios.
- The set of supported metadata filters includes category, date range, price, and tenant ID, as explicitly mentioned in the update.

**Integration with Related Azure Services**  
Azure HorizonDB’s advanced filtering for DiskANN vector search can be integrated with other Azure data and AI services. For example, it can be used in conjunction with Azure Cognitive Search for hybrid search scenarios or with Azure Machine Learning for vector generation and embedding management. The feature is particularly relevant for applications leveraging Azure’s scalable, high-performance data platforms.

**Summary Sentence**  
Azure HorizonDB now supports advanced filtering for DiskANN vector search in public preview, enabling users to combine vector similarity queries with metadata filters such as category, date range, price, or tenant ID, without impacting search performance.

---

### 78. Generally Available: Azure HorizonDB Agentic Advisor Solution Accelerator

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure HorizonDB Agentic Advisor Solution Accelerator](https://azure.microsoft.com/updates?id=563092)

**Update ID**: 563092
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Agentic Advisor Solution Accelerator for Azure HorizonDB is now generally available.

- Key changes or new features  
This release provides a reference solution specifically designed for financial services, enabling the development of multi-agent applications in Python. It leverages LangGraph and Mem0 frameworks, with Azure HorizonDB serving as the data and memory backend. The accelerator streamlines the integration of advanced agentic workflows, supporting rapid prototyping and deployment of AI-driven financial applications.

- Target audience affected  
Developers and IT professionals in the financial services sector, particularly those building AI/multi-agent solutions in Python, and teams adopting Azure HorizonDB for data management.

- Important notes if any  
The accelerator is optimized for use with Azure HorizonDB and integrates with LangGraph and Mem0, making it suitable for advanced AI and agentic application scenarios. It is intended as a reference implementation, allowing for customization and extension to meet specific organizational needs. Early adoption is encouraged for teams seeking to accelerate their financial services AI projects on Azure.  

[More details](https://azure.microsoft.com/updates?id=563092)

**Details**:

**Azure Update Report: Generally Available – Azure HorizonDB Agentic Advisor Solution Accelerator**

**Background and Purpose of the Update**  
The Azure HorizonDB Agentic Advisor Solution Accelerator is now generally available. This release targets the financial services sector, providing a reference solution designed to streamline the development of multi-agent applications. The accelerator leverages Python as the primary programming language and integrates with LangGraph and Mem0 frameworks, utilizing Azure HorizonDB as the underlying data platform. The main purpose is to enable organizations to rapidly prototype and deploy agent-based systems tailored to financial services use cases.

**Specific Features and Detailed Changes**  
- **Reference Solution:** The accelerator offers a ready-to-use template for building multi-agent applications, reducing the complexity and development time for financial services solutions.
- **Python Support:** Developers can use Python to implement and orchestrate agent behaviors, benefiting from Python’s rich ecosystem and ease of use.
- **LangGraph Integration:** LangGraph is supported for defining agent workflows and interactions, allowing for structured and scalable multi-agent architectures.
- **Mem0 Integration:** Mem0 is included for memory management within agent applications, facilitating context-aware and stateful agent operations.
- **Azure HorizonDB as Data Platform:** The solution is built to utilize Azure HorizonDB, ensuring scalable, secure, and high-performance data storage and retrieval for agent applications.

**Technical Mechanisms and Implementation Methods**  
- **Agent Orchestration:** The accelerator employs LangGraph to define and manage the interactions between multiple agents, enabling complex workflows and decision-making processes.
- **State Management:** Mem0 provides mechanisms for agents to maintain and recall state information, which is critical for applications requiring persistent context or historical data.
- **Data Handling:** Azure HorizonDB serves as the central data repository, offering robust data management capabilities optimized for agent-based workloads.
- **Python SDKs and APIs:** The solution leverages Python SDKs for seamless integration with LangGraph, Mem0, and Azure HorizonDB, facilitating rapid development and deployment.

**Use Cases and Application Scenarios**  
- **Financial Services Automation:** Automate tasks such as portfolio management, risk analysis, and customer advisory services using intelligent agents.
- **Multi-Agent Collaboration:** Implement systems where multiple agents interact to solve complex problems, such as fraud detection or transaction monitoring.
- **Context-Aware Advisory:** Build advisory solutions that leverage persistent memory and historical data to provide personalized recommendations to clients.

**Important Considerations and Limitations**  
- **Financial Services Focus:** The accelerator is optimized for financial services scenarios; adaptation may be required for other industries.
- **Python-Centric:** The solution is designed for Python, which may limit use in environments where other languages are preferred.
- **Dependency on Azure HorizonDB:** Applications built with this accelerator are tightly coupled with Azure HorizonDB, and migration to other data platforms may require significant rework.
- **Framework Dependencies:** Utilization of LangGraph and Mem0 is required, which may necessitate additional learning or adaptation for teams unfamiliar with these frameworks.

**Integration with Related Azure Services**  
- **Azure HorizonDB:** Acts as the primary data platform, ensuring seamless integration with other Azure data services and analytics tools.
- **Potential for Broader Azure Integration:** While not explicitly stated, the solution can be extended to interact with other Azure services (e.g., Azure Functions, Logic Apps) through Python SDKs and APIs, supporting end-to-end automation and orchestration.

**Summary Sentence**  
The Azure HorizonDB Agentic Advisor Solution Accelerator is now generally available, providing a financial services-focused reference solution for building multi-agent Python applications using LangGraph and Mem0 with Azure HorizonDB as the data platform.

---

### 79. Public Preview: Azure HorizonDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure HorizonDB](https://azure.microsoft.com/updates?id=563087)

**Update ID**: 563087
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure HorizonDB, a new PostgreSQL-compatible database service, is now available in Public Preview.

- Key changes or new features  
  - Fully managed, cloud-native PostgreSQL-compatible database.  
  - Autoscaling storage up to 128 TB, supporting large-scale workloads without manual intervention.  
  - Performance improvements: Up to 3x faster than self-managed PostgreSQL deployments.  
  - Rapid compute scaling to handle variable workloads efficiently.  
  - Designed for future extensibility and advanced use cases.

- Target audience affected  
  - Developers building applications that require scalable, high-performance PostgreSQL databases.  
  - IT professionals and database administrators seeking managed database solutions with minimal operational overhead.

- Important notes if any  
  - As a Public Preview, HorizonDB may not yet be suitable for production workloads; features and SLAs may change before general availability.  
  - Existing PostgreSQL tools and drivers are compatible, simplifying migration and integration.  
  - Ideal for teams planning for future growth or requiring dynamic scaling and high throughput.  

For more details, refer to the official update: [Azure HorizonDB Public Preview](https://azure.microsoft.com/updates?id=563087)

**Details**:

**Azure Update Report: Public Preview – Azure HorizonDB**

**Background and Purpose of the Update**  
Azure HorizonDB is introduced as a PostgreSQL-compatible database service, specifically engineered to deliver enhanced performance and scalability for modern cloud workloads. The update aims to address the growing demand for high-performance, future-proof database solutions that can seamlessly scale and support advanced application requirements, while maintaining compatibility with PostgreSQL. The purpose is to provide IT professionals and organizations with a managed database platform that simplifies operations, improves throughput, and supports evolving business needs.

**Specific Features and Detailed Changes**  
- **PostgreSQL Compatibility:** HorizonDB offers full compatibility with PostgreSQL, enabling migration of existing workloads and use of familiar tools, extensions, and drivers.
- **Autoscaling Storage:** The service supports automatic scaling of storage capacity up to 128 TB, allowing databases to grow dynamically without manual intervention or downtime.
- **Performance Improvements:** HorizonDB delivers up to three times faster performance compared to self-managed PostgreSQL deployments. This includes optimized query execution, faster data ingestion, and improved transaction processing.
- **Rapid Compute Provisioning:** The platform is designed for rapid provisioning of compute resources, enabling quick scaling to meet workload demands.
- **Managed Service:** As a managed Azure service, HorizonDB provides built-in operational automation, including backups, patching, and monitoring.

**Technical Mechanisms and Implementation Methods**  
- **Autoscaling:** Storage autoscaling is implemented natively within the service, automatically expanding disk capacity as data grows, eliminating manual storage management.
- **Performance Optimization:** HorizonDB leverages Azure’s underlying infrastructure and proprietary optimizations to accelerate database operations. This may include advanced caching, parallel processing, and efficient resource allocation.
- **Compute Scaling:** The service supports rapid provisioning and scaling of compute nodes, enabling high concurrency and responsiveness for demanding workloads.
- **Managed Operations:** Azure HorizonDB integrates with Azure’s management plane, providing automated maintenance, security updates, and monitoring capabilities.

**Use Cases and Application Scenarios**  
- **Enterprise Applications:** Ideal for mission-critical business applications requiring high throughput and scalability.
- **Data Warehousing and Analytics:** Suitable for large-scale analytics workloads that demand fast query performance and dynamic storage expansion.
- **Cloud-native Development:** Supports modern cloud applications that require seamless integration, rapid scaling, and managed operations.
- **Migration Projects:** Facilitates migration from self-managed PostgreSQL environments to a managed Azure service with minimal changes.

**Important Considerations and Limitations**  
- **Public Preview:** HorizonDB is currently in public preview, which may involve limited features, support, and regional availability. Production use should be carefully evaluated.
- **Storage Limit:** Maximum autoscaling storage is capped at 128 TB.
- **Performance Claims:** Performance improvements are benchmarked against self-managed PostgreSQL; actual results may vary based on workload characteristics.
- **Compatibility:** While PostgreSQL compatibility is emphasized, users should validate specific extensions and features for their workloads.

**Integration with Related Azure Services**  
- **Azure Monitoring and Security:** HorizonDB integrates with Azure’s monitoring, logging, and security services for operational visibility and compliance.
- **Azure Backup:** Automated backup capabilities are provided as part of the managed service.
- **Azure Networking:** Supports integration with Azure Virtual Networks and private endpoints for secure connectivity.

**Summary Sentence**  
Azure HorizonDB, now in public preview, is a PostgreSQL-compatible managed database service offering autoscaling storage up to 128 TB, up to three times faster performance than self-managed PostgreSQL, and rapid compute provisioning, designed to support high-performance, scalable cloud workloads with seamless integration into Azure’s ecosystem.

---

### 80. Generally Available: Azure DocumentDB instant free tier clusters

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure DocumentDB instant free tier clusters](https://azure.microsoft.com/updates?id=563082)

**Update ID**: 563082
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure DocumentDB now offers generally available instant provisioning of free tier clusters.

- Key changes or new features  
Developers and IT professionals can now provision free tier clusters for Azure DocumentDB almost instantly. This allows users to quickly start developing, testing, or exploring DocumentDB without waiting for resource allocation or incurring initial costs.

- Target audience affected  
Developers, solution architects, and IT professionals who want to evaluate, prototype, or build applications using Azure DocumentDB, especially those seeking a cost-effective or no-cost entry point.

- Important notes if any  
The instant free tier clusters are ideal for getting started, prototyping, or running small workloads. Users should review any limitations or quotas associated with the free tier before deploying production workloads. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=563082).

**Details**:

**Azure Update Report: Generally Available – Azure DocumentDB Instant Free Tier Clusters**

**Background and Purpose of the Update:**  
This update announces the general availability of instant provisioning for free tier clusters in Azure DocumentDB. The primary goal is to enable users to start working with Azure DocumentDB immediately, reducing the time and friction typically associated with cluster setup. This enhancement is designed to accelerate onboarding, experimentation, and development processes, especially for users evaluating Azure DocumentDB or building prototypes.

**Specific Features and Detailed Changes:**  
- **Instant Provisioning:** Users can now create free tier clusters in Azure DocumentDB with near-instant availability. This eliminates previous wait times for resource allocation and cluster initialization.
- **Free Tier Clusters:** The free tier provides users with a cost-free entry point to Azure DocumentDB, allowing them to explore features, develop applications, and test workloads without incurring charges.
- **General Availability:** The feature is now fully supported and available for production use, ensuring reliability and support from Azure.

**Technical Mechanisms and Implementation Methods:**  
- **Automated Cluster Deployment:** The instant provisioning mechanism leverages Azure’s underlying automation and resource management infrastructure to pre-allocate or rapidly configure clusters upon request.
- **Resource Management Integration:** The provisioning process is integrated with Azure Resource Manager (ARM), enabling seamless deployment through the Azure Portal, CLI, or ARM templates.
- **Service Quotas and Limits:** The free tier clusters are subject to predefined resource limits (such as storage, throughput, and number of clusters per subscription), ensuring fair usage and resource availability.

**Use Cases and Application Scenarios:**  
- **Development and Testing:** Developers can quickly spin up free tier clusters to build, test, and validate applications using Azure DocumentDB without waiting for resource provisioning or incurring costs.
- **Proof-of-Concept (PoC) Projects:** Teams evaluating Azure DocumentDB can utilize instant free clusters to prototype solutions and assess service capabilities.
- **Learning and Training:** Organizations and individuals can use free tier clusters for educational purposes, hands-on labs, and workshops, benefiting from immediate access.

**Important Considerations and Limitations:**  
- **Resource Constraints:** Free tier clusters have limited resources compared to paid clusters. These constraints may include reduced storage capacity, throughput limits, and a cap on the number of free clusters per subscription.
- **No SLA for Free Tier:** Free tier clusters may not include the same service level agreements (SLAs) as paid offerings, making them unsuitable for production workloads.
- **Upgrade Path:** Users requiring higher performance, scalability, or production-grade features must upgrade to paid clusters.

**Integration with Related Azure Services:**  
- **Azure Portal and CLI:** Instant free tier clusters can be provisioned and managed through the Azure Portal and Azure CLI, supporting standard Azure workflows.
- **Azure Resource Manager:** Integration with ARM allows for automated deployment and configuration as part of larger infrastructure-as-code solutions.
- **Ecosystem Compatibility:** Free tier clusters can be used with other Azure services (e.g., Azure Functions, Logic Apps, or App Services) for end-to-end solution prototyping and integration testing.

**Summary:**  
Azure DocumentDB now offers generally available instant provisioning of free tier clusters, enabling users to start working with the service immediately for development, testing, and evaluation purposes.

---

### 81. Generally Available: Azure DocumentDB Migration Extension in Visual Studio Code

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure DocumentDB Migration Extension in Visual Studio Code](https://azure.microsoft.com/updates?id=563072)

**Update ID**: 563072
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure DocumentDB Migration Extension for Visual Studio Code is now generally available.

- Key changes or new features  
Developers and IT professionals can now create, run, and manage migration jobs directly within Visual Studio Code. This extension enables seamless migration of data from on-premises or cloud-based MongoDB sources to Azure Cosmos DB (DocumentDB API). The extension provides an integrated, code-centric workflow for configuring migration jobs, monitoring progress, and handling errors without leaving the VS Code environment.

- Target audience affected  
Developers and IT professionals working with MongoDB databases who need to migrate data to Azure Cosmos DB, especially those who use Visual Studio Code as their primary development environment.

- Important notes  
This GA release streamlines the migration process by eliminating the need for separate migration tools or command-line utilities. It enhances productivity by integrating migration management into the developer workflow. Users should ensure they have the latest version of Visual Studio Code and the extension installed to access all features. For more details, refer to the official [Azure update](https://azure.microsoft.com/updates?id=563072).

**Details**:

**Background and Purpose of the Update**  
The Azure DocumentDB Migration Extension for Visual Studio Code has reached general availability. The purpose of this update is to streamline and simplify the process of migrating data to Azure DocumentDB by enabling migration job management directly within the Visual Studio Code (VS Code) environment. This extension is designed to support IT professionals and developers who need to move data from on-premises or cloud-based MongoDB sources to Azure DocumentDB, providing a more integrated and efficient workflow.

**Specific Features and Detailed Changes**  
- **Migration Job Management:** Users can now create, run, and manage migration jobs directly from VS Code, eliminating the need for separate migration tools or command-line utilities.
- **Source Flexibility:** The extension supports data migration from both on-premises and cloud-based MongoDB instances, offering flexibility in source environments.
- **VS Code Integration:** The extension leverages the familiar VS Code interface, allowing users to configure migration settings, monitor progress, and manage jobs within their development environment.

**Technical Mechanisms and Implementation Methods**  
- **Extension Architecture:** The migration extension is installed as a VS Code add-on, integrating with the editor’s UI and command palette.
- **Job Creation and Execution:** Users can define migration jobs by specifying source (MongoDB) and target (Azure DocumentDB) connection details, along with any necessary migration parameters.
- **Job Management:** The extension provides controls for starting, stopping, and monitoring migration jobs, with status updates and logs available within VS Code.
- **Secure Connectivity:** The extension supports secure connections to both source and target databases, leveraging VS Code’s credential management and connection profiles.

**Use Cases and Application Scenarios**  
- **Cloud Migration Projects:** Organizations migrating MongoDB workloads from on-premises data centers or other cloud providers to Azure DocumentDB can use this extension to manage the migration process efficiently.
- **Development and Testing:** Developers can use the extension to quickly move sample or test datasets into Azure DocumentDB for development and QA purposes.
- **Data Consolidation:** Teams consolidating multiple MongoDB sources into a single Azure DocumentDB instance can coordinate and monitor multiple migration jobs from within VS Code.

**Important Considerations and Limitations**  
- **Supported Sources:** The extension is specifically designed for MongoDB to Azure DocumentDB migrations. Other source or target databases are not supported.
- **VS Code Dependency:** Users must have Visual Studio Code installed and configured to use the extension.
- **Migration Scope:** The extension’s capabilities are focused on migration job management; advanced transformation or complex ETL scenarios may require additional tools or custom scripts.
- **Security and Permissions:** Appropriate permissions are required on both the source MongoDB and the target Azure DocumentDB to perform migrations.

**Integration with Related Azure Services**  
- **Azure DocumentDB:** The extension is tightly integrated with Azure DocumentDB, facilitating direct data import and migration management.
- **Azure Portal and CLI:** While the extension focuses on VS Code integration, it complements other Azure management tools such as the Azure Portal and Azure CLI for post-migration validation and monitoring.
- **Azure Resource Management:** Migration jobs can be coordinated as part of broader Azure resource deployment workflows, supporting DevOps and automation scenarios.

**Summary Sentence**  
The Azure DocumentDB Migration Extension for Visual Studio Code is now generally available, enabling IT professionals to efficiently create, run, and manage MongoDB-to-DocumentDB migration jobs directly within the VS Code environment.

---

### 82. Public Preview: Change streams (multi-shard) in Azure DocumentDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Change streams (multi-shard) in Azure DocumentDB](https://azure.microsoft.com/updates?id=563067)

**Update ID**: 563067
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure DocumentDB now supports change streams with multi-shard (multi-node) capability, available in public preview.

- Key changes or new features  
  - Change streams allow developers to capture and process real-time data changes (inserts, updates, deletes) across multiple shards/nodes in DocumentDB.  
  - Controlled polling enables efficient and scalable monitoring of data changes, supporting event-driven architectures.  
  - This feature helps power instant analytics, automation, and integration scenarios by providing near real-time access to change events.

- Target audience affected  
  - Application developers building real-time, event-driven, or reactive applications on Azure DocumentDB.  
  - IT professionals and architects responsible for data integration, analytics, or automation workflows using DocumentDB.

- Important notes if any  
  - This is a public preview feature; it is not recommended for production workloads yet.  
  - Multi-shard support means applications can now monitor changes across partitioned collections, improving scalability and reliability.  
  - Developers can use the API to consume change streams and integrate with downstream systems or trigger business logic.  
  - Review the official documentation for API usage patterns, limitations, and best practices during the preview phase.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=563067)

**Details**:

**Azure Update Report: Public Preview – Change Streams (Multi-Shard) in Azure DocumentDB**

**Background and Purpose of the Update**  
Azure DocumentDB introduces change streams with multi-shard support in public preview to facilitate the development of real-time, event-driven applications. The purpose of this update is to enable users to capture and process live data changes efficiently, supporting scenarios such as instant analytics and automation. By providing controlled polling mechanisms, this feature aims to enhance the responsiveness and scalability of applications that depend on timely data updates.

**Specific Features and Detailed Changes**  
The update delivers change streams functionality, allowing users to monitor and react to data modifications within Azure DocumentDB. Key features include:
- **Multi-Node (Multi-Shard) Support:** Change streams now operate across multiple shards, enabling scalable tracking of changes in distributed DocumentDB deployments.
- **Controlled Polling:** Users can configure polling intervals to balance data freshness and resource consumption, ensuring efficient retrieval of change events.
- **Live Data Capture:** The system can detect and expose inserts, updates, and deletes in real time, empowering applications to respond immediately to data changes.

**Technical Mechanisms and Implementation Methods**  
Change streams are implemented as a mechanism that continuously monitors the underlying data store for modifications. With multi-shard support, the system aggregates change events from all shards, presenting a unified stream to the application. Controlled polling is achieved by specifying polling intervals or strategies, allowing clients to fetch new events at a cadence that suits their workload and performance requirements. The change stream interface exposes events in a structured format, enabling downstream processing and integration.

**Use Cases and Application Scenarios**  
This feature is particularly valuable in scenarios requiring immediate awareness of data changes, such as:
- **Real-Time Analytics:** Applications can process and analyze incoming data as soon as it is written, supporting dashboards and operational intelligence.
- **Automation Workflows:** Triggering automated actions (e.g., notifications, business logic execution) in response to data changes.
- **Data Synchronization:** Keeping external systems or caches updated by propagating changes from DocumentDB.
- **Event-Driven Microservices:** Decoupling services by using change streams as a source of truth for inter-service communication.

**Important Considerations and Limitations**  
- **Public Preview:** The feature is currently in public preview, which may involve limited support, evolving APIs, and potential changes before general availability.
- **Resource Consumption:** Controlled polling must be configured carefully to avoid excessive resource usage or missed events.
- **Consistency and Ordering:** While change streams provide real-time data, engineers should review documentation for guarantees regarding event ordering and consistency, especially in multi-shard environments.
- **Integration Complexity:** Applications must handle event processing, error handling, and potential duplication or gaps in change events.

**Integration with Related Azure Services**  
Change streams in Azure DocumentDB can be integrated with other Azure services to build robust event-driven architectures:
- **Azure Functions:** Automatically trigger serverless functions in response to change events.
- **Azure Event Grid:** Route change notifications to other services for further processing.
- **Azure Logic Apps:** Orchestrate complex workflows based on DocumentDB changes.
- **Azure Synapse Analytics:** Feed real-time data into analytics pipelines for immediate insights.

**Summary Sentence**  
Azure DocumentDB now offers change streams with multi-shard support in public preview, enabling real-time, event-driven applications through controlled polling and live data capture for instant analytics and automation.

---

### 83. Generally Available: Graceful failover with zero data loss guarantee

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Graceful failover with zero data loss guarantee](https://azure.microsoft.com/updates?id=563062)

**Update ID**: 563062
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure DocumentDB now offers generally available support for graceful failovers with a zero data loss guarantee.

- Key changes or new features  
The new graceful failover feature allows replica clusters to be promoted to primary with a guarantee of zero data loss. This is in contrast to the existing "force promote" option, which enables immediate promotion but may risk data loss. Graceful failover ensures all committed transactions are replicated before the role switch, providing higher data integrity during planned failover scenarios.

- Target audience affected  
This update is relevant for developers and IT professionals managing high-availability and disaster recovery for applications using Azure DocumentDB. It is especially important for those requiring strict data consistency and minimal downtime during failover events.

- Important notes if any  
Graceful failover is intended for planned maintenance or migration scenarios where zero data loss is critical. For emergency situations requiring immediate failover, the force promote option remains available but may not guarantee data integrity. Developers and IT teams should update their failover strategies to leverage this new capability for improved reliability and compliance.  

For more details, see the official update: https://azure.microsoft.com/updates?id=563062

**Details**:

**Azure Update Report: Generally Available – Graceful Failover with Zero Data Loss Guarantee for Azure DocumentDB**

**Background and Purpose of the Update:**  
Azure DocumentDB has introduced the general availability of a new failover capability designed to enhance data durability and service continuity. Previously, the platform offered a "force promote" feature, which allowed immediate promotion of replica clusters during failover events. However, this method could potentially risk data loss if all writes were not fully replicated at the time of promotion. The new "graceful failover" feature addresses this limitation by ensuring that failover operations can be performed with a guarantee of zero data loss, thereby meeting stricter data consistency and durability requirements for mission-critical applications.

**Specific Features and Detailed Changes:**  
The update introduces the following key feature:
- **Graceful Failover with Zero Data Loss Guarantee:** This capability allows administrators to promote replica clusters to primary status during failover events, ensuring that all committed data is fully replicated and acknowledged before the promotion occurs. This is distinct from the existing "force promote" option, which prioritizes availability over data consistency and may result in data loss under certain conditions.

**Technical Mechanisms and Implementation Methods:**  
- **Data Replication Synchronization:** During a graceful failover, Azure DocumentDB coordinates the promotion of a replica cluster by verifying that all data changes (writes) have been successfully replicated to the target replica. The failover process waits until there is confirmation that no unreplicated data remains, thus guaranteeing zero data loss.
- **Cluster Promotion Workflow:** The system manages the transition of the replica cluster to primary status in a controlled manner, only proceeding once data consistency is assured. This mechanism is designed to minimize the risk of split-brain scenarios or data divergence between clusters.

**Use Cases and Application Scenarios:**  
- **Mission-Critical Applications:** Organizations running applications that require strict data consistency and cannot tolerate any data loss during failover (e.g., financial services, healthcare, or transactional systems) will benefit significantly from this feature.
- **Planned Maintenance and Disaster Recovery:** The graceful failover capability is ideal for scenarios where administrators need to perform planned maintenance or respond to regional outages, ensuring seamless continuity without compromising data integrity.

**Important Considerations and Limitations:**  
- **Failover Latency:** Because the graceful failover process waits for all data to be replicated before promoting the replica, there may be increased latency compared to forceful failover methods. This trade-off is necessary to guarantee zero data loss.
- **Operational Planning:** Administrators should plan for the potential additional time required for failover operations, especially in environments with high write throughput or network latency between clusters.
- **Feature Scope:** This update specifically applies to Azure DocumentDB and does not infer changes to other Azure database services.

**Integration with Related Azure Services:**  
- **Seamless Integration:** The graceful failover feature is natively integrated into Azure DocumentDB’s high availability and disaster recovery workflows. It complements existing Azure monitoring, alerting, and automation tools, allowing IT professionals to incorporate zero data loss failover into their broader Azure-based business continuity strategies.

**Summary Sentence:**  
Azure DocumentDB now offers generally available graceful failover with a zero data loss guarantee, enabling replica cluster promotion only after all data is fully replicated, thereby ensuring data consistency and integrity during failover events for mission-critical workloads.

---

### 84. Generally Available: Service-managed failover in Azure DocumentDB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Service-managed failover in Azure DocumentDB](https://azure.microsoft.com/updates?id=563057)

**Update ID**: 563057
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Service-managed failover for multi-region clusters in Azure DocumentDB is now generally available.

- Key changes or new features  
Azure DocumentDB can now automatically perform failover of globally distributed clusters in the event of a regional outage. This means the service will detect outages and shift the primary region to a healthy secondary region without manual intervention, ensuring high availability and business continuity.

- Target audience affected  
Developers and IT professionals managing multi-region Azure DocumentDB deployments, especially those requiring high availability and disaster recovery.

- Important notes if any  
No additional configuration is required to enable service-managed failover; it is managed by Azure. However, review your application’s regional endpoint usage and connection policies to ensure seamless failover. This feature reduces operational overhead and improves resiliency for mission-critical applications. For more details, refer to the official documentation: https://azure.microsoft.com/updates?id=563057

**Details**:

**Azure Update Report: Service-managed Failover in Azure DocumentDB – General Availability**

**Background and Purpose of the Update:**  
Azure DocumentDB, a globally distributed NoSQL database service, has introduced the general availability of service-managed failover for multi-region clusters. The primary goal of this update is to enhance business continuity and disaster recovery by automating the failover process in the event of a regional outage. This reduces the need for manual intervention and minimizes downtime for mission-critical applications that rely on high availability and global distribution.

**Specific Features and Detailed Changes:**  
With this update, Azure DocumentDB now supports automatic, service-managed failover for clusters deployed across multiple regions. When a regional outage occurs, the service will automatically detect the failure and initiate a failover from the affected primary region to a healthy secondary region. This feature eliminates the need for customers to manually trigger failover operations, streamlining operational processes and improving recovery time objectives (RTO).

**Technical Mechanisms and Implementation Methods:**  
Service-managed failover leverages Azure’s underlying global infrastructure and DocumentDB’s multi-region replication capabilities. The system continuously monitors the health of all participating regions within a multi-region cluster. Upon detecting a regional outage or loss of connectivity in the primary region, the service orchestrates a failover by promoting a secondary region to become the new primary. This process involves redirecting client requests and updating the cluster’s metadata to reflect the new primary region, ensuring continued availability and consistency of data.

**Use Cases and Application Scenarios:**  
This feature is particularly beneficial for organizations with globally distributed applications that require high availability and resilience against regional failures. Typical scenarios include:  
- Enterprises running mission-critical workloads with strict uptime requirements  
- SaaS providers serving customers across multiple geographies  
- Applications with regulatory or compliance needs for disaster recovery and data residency  
- Any deployment where minimizing manual operational overhead during outages is a priority

**Important Considerations and Limitations:**  
- Service-managed failover is applicable only to multi-region clusters; single-region deployments do not benefit from this feature.  
- The automatic failover process is triggered solely in the event of a regional outage as detected by the service; it does not cover other types of failures (e.g., application-level issues).  
- Customers should review their application’s retry logic and connection configurations to ensure seamless operation during and after failover events.  
- There may be a brief period of service disruption during the failover process, depending on the nature and scope of the outage.

**Integration with Related Azure Services:**  
Service-managed failover in Azure DocumentDB integrates with Azure’s global networking and monitoring infrastructure, leveraging Azure’s capabilities for region health detection and traffic redirection. It complements other Azure high-availability and disaster recovery features, such as Azure Traffic Manager and Azure Site Recovery, by providing database-level resilience as part of a broader business continuity strategy.

**Summary Sentence:**  
Azure DocumentDB’s general availability of service-managed failover for multi-region clusters automates failover during regional outages, enhancing high availability and reducing manual intervention for globally distributed applications.

---

### 85. Public Preview: Relational Database to Azure Cosmos DB NoSQL Migration Assistant

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Relational Database to Azure Cosmos DB NoSQL Migration Assistant](https://azure.microsoft.com/updates?id=563052)

**Update ID**: 563052
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure announced the public preview of the Relational Database to Azure Cosmos DB NoSQL Migration Assistant, now available in the Azure Cosmos DB extension for Visual Studio Code.

- Key changes or new features  
Developers and IT professionals can now use a guided workflow within Visual Studio Code to migrate data from relational databases (Oracle, SQL Server, PostgreSQL, MySQL) to Azure Cosmos DB for NoSQL. The Migration Assistant simplifies schema mapping, data transformation, and data transfer, reducing manual effort and potential errors during migration.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals planning to modernize applications by moving from relational databases to Azure Cosmos DB NoSQL. It is especially useful for those already using Visual Studio Code and working with Azure data services.

- Important notes if any  
The Migration Assistant is currently in public preview and may not support all advanced scenarios or production workloads. Users should validate migrations and test thoroughly before deploying to production. Documentation and support are available via the Azure Cosmos DB extension for Visual Studio Code.

Data source: Using API data  
For more information, see the [official update](https://azure.microsoft.com/updates?id=563052).

**Details**:

**Azure Update Report: Public Preview – Relational Database to Azure Cosmos DB NoSQL Migration Assistant**

**Background and Purpose of the Update:**  
The migration of data from traditional relational databases (such as Oracle, SQL Server, PostgreSQL, and MySQL) to Azure Cosmos DB for NoSQL workloads has historically required significant manual effort and specialized tooling. This update introduces a Migration Assistant within the Azure Cosmos DB extension for Visual Studio Code, aiming to streamline and simplify the migration process for IT professionals and developers. The purpose is to reduce complexity, minimize migration errors, and accelerate the adoption of Azure Cosmos DB for NoSQL by providing a guided, structured workflow.

**Specific Features and Detailed Changes:**  
The Migration Assistant is now available in public preview as part of the Azure Cosmos DB extension for Visual Studio Code. Key features include:

- **Guided Workflow:** The assistant provides step-by-step guidance for migrating data from supported relational databases (Oracle, SQL Server, PostgreSQL, MySQL) to Azure Cosmos DB for NoSQL.
- **Source Database Connectivity:** Enables secure connection to the source relational database directly from Visual Studio Code.
- **Schema Mapping:** Assists in mapping relational schemas to Cosmos DB’s NoSQL document model, addressing differences in data structure and types.
- **Data Extraction and Transformation:** Facilitates extraction of data from relational tables and transformation into JSON documents suitable for Cosmos DB.
- **Data Loading:** Supports bulk loading of transformed data into Azure Cosmos DB collections.
- **Progress Monitoring:** Offers real-time feedback and progress indicators throughout the migration process.

**Technical Mechanisms and Implementation Methods:**  
The Migration Assistant leverages the extensibility of Visual Studio Code and the Azure Cosmos DB extension. It uses built-in connectors to establish secure connections to supported relational databases. Data extraction is performed using standard SQL queries, followed by transformation routines that convert tabular data into JSON format. The assistant then utilizes Azure Cosmos DB’s APIs to load the transformed documents into the target collections. The workflow is orchestrated within Visual Studio Code, providing a unified interface for all migration steps.

**Use Cases and Application Scenarios:**  
- **Cloud Modernization:** Organizations seeking to modernize legacy applications by transitioning from relational databases to scalable, globally distributed NoSQL solutions in Azure.
- **Application Re-architecting:** Developers re-architecting applications to leverage Cosmos DB’s flexible schema and high availability.
- **Data Consolidation:** Projects requiring consolidation of disparate relational data sources into a single NoSQL store for analytics or operational workloads.
- **Rapid Prototyping:** Teams needing to quickly migrate sample datasets for proof-of-concept or pilot projects on Azure Cosmos DB.

**Important Considerations and Limitations:**  
- **Public Preview:** The Migration Assistant is in public preview, which may imply limited support, incomplete features, or potential changes before general availability.
- **Supported Databases:** Only Oracle, SQL Server, PostgreSQL, and MySQL are supported as source databases.
- **Schema Complexity:** Complex relational schemas or advanced database features (e.g., stored procedures, triggers) may require manual adjustments during migration.
- **Data Transformation:** Users must validate the accuracy of schema mapping and data transformation to ensure data integrity.
- **Performance:** Bulk data migration performance may vary based on source database size, network bandwidth, and Cosmos DB throughput settings.

**Integration with Related Azure Services:**  
The Migration Assistant is tightly integrated with Azure Cosmos DB and leverages Azure authentication and resource management. It operates within Visual Studio Code, which can be used alongside other Azure extensions for resource provisioning, monitoring, and management. Migrated data can be further integrated with Azure services such as Azure Functions, Azure Logic Apps, and Azure Data Factory for downstream processing and automation.

**Summary Sentence:**  
The public preview of the Relational Database to Azure Cosmos DB NoSQL Migration Assistant in Visual Studio Code offers a structured, guided workflow for migrating data from Oracle, SQL Server, PostgreSQL, and MySQL to Azure Cosmos DB, streamlining

---

### 86. Public Preview: Azure Cosmos DB distributed transactions

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Cosmos DB distributed transactions](https://azure.microsoft.com/updates?id=563047)

**Update ID**: 563047
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB now supports distributed transactions in public preview.

- Key changes or new features  
You can perform atomic operations across multiple items and partitions within Azure Cosmos DB. This means that changes made in a transaction will either all commit successfully or automatically roll back if any part fails, ensuring data consistency. Distributed transactions remove the need for complex client-side coordination or manual compensation logic when working with multi-item or multi-partition scenarios.

- Target audience affected  
Developers and IT professionals building applications on Azure Cosmos DB, especially those requiring transactional consistency across multiple documents or partitions.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads yet. It simplifies development for scenarios that previously required custom logic to maintain consistency. Review the documentation for limitations and best practices during the preview phase.  

Data source: Using API data  
More details: [Azure Update link](https://azure.microsoft.com/updates?id=563047)

**Details**:

**Azure Update Report: Public Preview – Azure Cosmos DB Distributed Transactions**

**Background and Purpose of the Update:**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications requiring low latency and high availability. Traditionally, transactional guarantees in Cosmos DB were limited to single logical partitions, restricting atomicity and consistency for operations spanning multiple items or partitions. The introduction of distributed transactions addresses this limitation, enabling atomic operations across multiple items and partitions. The purpose of this update is to simplify development and ensure data integrity for complex, multi-entity operations.

**Specific Features and Detailed Changes:**  
With this public preview, Azure Cosmos DB now supports distributed transactions, allowing users to execute atomic operations across different items and partitions within a container. This means that a group of operations can be committed as a single transaction: either all changes are applied, or none are, in the event of a failure. This enhancement eliminates the need for manual coordination or compensating logic in application code to maintain consistency across partitions.

**Technical Mechanisms and Implementation Methods:**  
The distributed transactions feature leverages a transactional protocol that coordinates changes across multiple partitions. When a distributed transaction is initiated, all intended operations are grouped and executed as a single atomic unit. The system ensures that either all operations succeed and are committed, or, if any operation fails, all changes are rolled back automatically. This is managed internally by Cosmos DB, abstracting the complexity of distributed transaction coordination from the application developer.

**Use Cases and Application Scenarios:**  
- **Multi-entity Updates:** Applications that need to update several related items across different partitions (e.g., order and inventory records) can now do so atomically.
- **Financial Transactions:** Scenarios requiring strict consistency, such as transferring funds between accounts stored in different partitions, benefit from distributed transactions.
- **Event Sourcing and State Management:** Systems that record events or state changes spanning multiple entities can ensure all-or-nothing persistence.
- **Microservices Coordination:** Distributed transactions simplify workflows where multiple microservices interact with Cosmos DB and require atomic updates across partitioned data.

**Important Considerations and Limitations:**  
- This feature is currently in public preview and may not be recommended for production workloads until general availability.
- As with any distributed transaction system, there may be performance implications due to coordination overhead.
- The preview may have limitations on supported operations, partition counts, or transaction size; users should consult the official documentation for current constraints.
- Rollback and commit semantics are managed by Cosmos DB, but application-level error handling should still account for transaction failures.

**Integration with Related Azure Services:**  
Distributed transactions in Cosmos DB can be leveraged by any Azure service or application that interacts with Cosmos DB, including Azure Functions, Azure Logic Apps, and Azure App Services. This feature enhances integration scenarios where atomicity across multiple partitions is required, supporting more robust workflows and reducing the need for external transaction orchestration or compensating logic.

**Summary Sentence:**  
The public preview of distributed transactions in Azure Cosmos DB enables atomic operations across items and partitions, ensuring that changes are committed together or rolled back automatically on failure, thereby simplifying multi-entity consistency and reducing application complexity for distributed data scenarios.

---

### 87. Generally Available: Per-partition automatic failover for Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Per-partition automatic failover for Azure Cosmos DB](https://azure.microsoft.com/updates?id=563042)

**Update ID**: 563042
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB now offers General Availability (GA) of Per-partition Automatic Failover (PPAF).

- Key changes or new features  
PPAF enables automatic failover at the partition level rather than the entire Cosmos DB account during a regional disruption. This results in faster recovery times and improved availability for mission-critical workloads. Instead of failing over all partitions, only the affected partitions are failed over, minimizing impact and downtime. This feature is especially valuable for large, multi-region Cosmos DB deployments.

- Target audience affected  
Developers and IT professionals managing high-availability, globally distributed applications on Azure Cosmos DB. Teams responsible for business continuity, disaster recovery, and operational resilience will benefit most.

- Important notes if any  
No application changes are required to leverage PPAF; it is managed by the Cosmos DB platform. Review your partitioning strategy to maximize the benefits of this feature. Existing failover policies and SLAs are enhanced by this update, further reducing recovery time objectives (RTO). For more information, refer to the official Azure documentation.

Link: https://azure.microsoft.com/updates?id=563042

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Per-partition automatic failover for Azure Cosmos DB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563042)

---

### Background and Purpose of the Update

Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications requiring high availability and low latency. Traditionally, failover in Cosmos DB has been performed at the account level, meaning all partitions within an account would fail over together during a regional disruption. The purpose of this update is to introduce per-partition automatic failover (PPAF), enabling more granular and efficient failover operations. This enhancement aims to minimize downtime and improve the availability of applications by allowing only affected partitions to fail over, rather than the entire account.

---

### Specific Features and Detailed Changes

- **Per-partition Automatic Failover (PPAF):** This feature allows individual partitions within a Cosmos DB account to automatically fail over to a secondary region during a regional disruption.
- **Faster Recovery:** By failing over only the impacted partitions, recovery times are reduced, and unaffected partitions continue to operate without interruption.
- **Higher Availability:** Applications experience improved availability, as only the partitions experiencing issues are failed over, reducing the blast radius of regional outages.

---

### Technical Mechanisms and Implementation Methods

- **Partition-level Monitoring:** Cosmos DB now monitors the health and availability of each partition independently rather than at the account level.
- **Automatic Detection and Failover:** When a regional disruption is detected for a specific partition, the system automatically initiates failover for that partition to a pre-configured secondary region.
- **No Manual Intervention Required:** The failover process is fully automated, requiring no manual action from administrators for affected partitions.
- **Seamless Application Experience:** Applications connected to unaffected partitions continue to operate normally, while only the impacted partitions are redirected to the secondary region.

---

### Use Cases and Application Scenarios

- **Mission-critical Applications:** Systems requiring high availability and minimal downtime, such as financial services, e-commerce, and healthcare applications, benefit from more granular failover.
- **Multi-region Deployments:** Organizations with globally distributed data and applications can ensure localized disruptions have minimal impact on the overall system.
- **Partitioned Workloads:** Workloads that are partitioned by customer, geography, or business unit can leverage per-partition failover to isolate and recover only the affected segments.

---

### Important Considerations and Limitations

- **Configuration Requirements:** PPAF must be enabled and properly configured for each Cosmos DB account and its partitions.
- **Regional Pairing:** Secondary regions must be pre-configured for failover to function correctly.
- **Monitoring and Alerts:** Administrators should ensure appropriate monitoring and alerting are in place to track partition health and failover events.
- **Compatibility:** Review documentation to ensure compatibility with existing partitioning strategies and application architectures.

---

### Integration with Related Azure Services

- **Azure Monitor:** Integrate with Azure Monitor to track partition health, failover events, and performance metrics.
- **Azure Traffic Manager:** Use in conjunction with Azure Traffic Manager for global routing and optimized client connectivity during failover scenarios.
- **Azure Automation:** Combine with automation runbooks for custom remediation or notification workflows triggered by failover events.

---

**Summary Sentence:**  
Per-partition automatic failover for Azure Cosmos DB is now generally available, providing faster recovery and enhanced availability by enabling automatic, partition-level failover during regional disruptions, thereby minimizing downtime and impact on mission-critical applications.

---

### 88. Generally Available: MCP Toolkit for Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: MCP Toolkit for Azure Cosmos DB](https://azure.microsoft.com/updates?id=563032)

**Update ID**: 563032
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The MCP Toolkit for Azure Cosmos DB is now generally available.

- Key changes or new features  
The MCP Toolkit provides a standardized way to expose Azure Cosmos DB capabilities, enabling seamless integration between Cosmos DB and AI agents or copilots. It supports connecting operational data to AI solutions with enterprise-grade reliability, making it easier to build intelligent applications that leverage real-time data from Cosmos DB.

- Target audience affected  
Developers building AI-powered applications, solution architects, and IT professionals responsible for data integration and operational reliability in enterprise environments.

- Important notes if any  
The general availability of the MCP Toolkit ensures production readiness and support from Microsoft. Developers can now confidently use this toolkit to connect AI agents and copilots to Cosmos DB, streamlining data access and enhancing application intelligence. For more details and implementation guidance, refer to the official Azure Update: https://azure.microsoft.com/updates?id=563032

**Details**:

**Azure Update Report: Generally Available – MCP Toolkit for Azure Cosmos DB**

**Background and Purpose of the Update:**  
The MCP Toolkit for Azure Cosmos DB has reached general availability, marking its readiness for production environments. The primary purpose of this update is to provide a standardized and enterprise-ready mechanism for connecting AI agents and copilots to operational data stored in Azure Cosmos DB. This toolkit is designed to facilitate seamless and reliable integration between AI-driven applications and Cosmos DB, ensuring that operational data can be accessed and utilized with the robustness required for enterprise scenarios.

**Specific Features and Detailed Changes:**  
With this release, the MCP Toolkit offers a standardized approach to exposing Cosmos DB capabilities. This standardization simplifies the process of connecting AI agents and copilots to operational data, reducing the complexity of custom integration and enabling consistent access patterns. The toolkit is now generally available, which means it has passed all necessary validation and quality gates for enterprise use, and is fully supported by Microsoft.

**Technical Mechanisms and Implementation Methods:**  
The MCP Toolkit acts as an abstraction layer between AI agents/copilots and Azure Cosmos DB. It provides a set of APIs or connectors that allow these AI components to interact with operational data in a reliable and standardized manner. By leveraging this toolkit, developers can ensure that their AI solutions access Cosmos DB using best practices for reliability, security, and performance. The toolkit likely encapsulates connection management, query execution, and data retrieval, ensuring that AI agents can consume data without needing to manage the underlying complexities of Cosmos DB’s APIs.

**Use Cases and Application Scenarios:**  
Typical use cases include enterprise AI agents or copilots that require real-time or near-real-time access to operational data for tasks such as customer support, business process automation, or data-driven decision-making. For example, a copilot integrated into a customer service platform could use the MCP Toolkit to fetch customer records or transaction histories from Cosmos DB, enabling more informed and context-aware responses. Similarly, AI-driven analytics platforms can leverage the toolkit to access large volumes of operational data for processing and insights.

**Important Considerations and Limitations:**  
As the toolkit is now generally available, it is intended for production workloads and is supported by Microsoft. However, users should ensure that their AI agents and copilots are compatible with the toolkit’s interfaces and that they adhere to any best practices or guidance provided by Microsoft for secure and efficient data access. It is important to review the official documentation for any limitations regarding supported Cosmos DB features, data models, or performance characteristics.

**Integration with Related Azure Services:**  
The MCP Toolkit is specifically designed for Azure Cosmos DB, but it is also intended to serve as a bridge between Cosmos DB and AI agents or copilots, which may be hosted on Azure AI services such as Azure OpenAI Service, Azure Machine Learning, or Azure Bot Service. By standardizing the way operational data is exposed to AI components, the toolkit facilitates smoother integration across the Azure ecosystem, enhancing the ability to build intelligent, data-driven applications that leverage both Cosmos DB and Azure’s AI capabilities.

**Summary Sentence:**  
The MCP Toolkit for Azure Cosmos DB, now generally available, provides a standardized and enterprise-ready solution for connecting AI agents and copilots to operational data, enabling reliable and efficient integration for production workloads in Azure environments.

---

### 89. Public Preview: Introducing AI Assistant in the Azure Cosmos DB extension for Visual Studio Code

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Introducing AI Assistant in the Azure Cosmos DB extension for Visual Studio Code](https://azure.microsoft.com/updates?id=563027)

**Update ID**: 563027
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure Cosmos DB extension for Visual Studio Code now includes an AI Assistant feature, available in public preview.

- Key changes or new features  
  - AI-powered assistance is integrated into the Cosmos DB VS Code extension.  
  - Users can interact with the AI Assistant using natural language to generate optimized Cosmos DB queries.  
  - The assistant supports chat-based commands, reducing manual query writing and data handling.  
  - Designed to streamline working with Cosmos DB data directly within VS Code.

- Target audience affected  
  - Developers and database administrators working with Azure Cosmos DB in Visual Studio Code.  
  - IT professionals managing or developing applications that use Cosmos DB.

- Important notes if any  
  - The feature is currently in public preview; expect ongoing improvements and potential changes.  
  - The AI Assistant can help accelerate query development and reduce errors, but users should review AI-generated queries for accuracy and security before deployment.  
  - Integration with the VS Code extension means no additional installation is required beyond updating the extension.

[Learn more](https://azure.microsoft.com/updates?id=563027)

**Details**:

**Azure Update Report: Public Preview – AI Assistant in Azure Cosmos DB Extension for Visual Studio Code**

**Background and Purpose of the Update**  
This update introduces an AI-powered assistant within the Azure Cosmos DB extension for Visual Studio Code, now available in public preview. The primary objective is to streamline data interaction workflows for developers and database administrators by reducing manual query creation and enhancing productivity. The AI assistant leverages natural language processing to facilitate easier and faster data manipulation, addressing common pain points such as query optimization and syntax complexity.

**Specific Features and Detailed Changes**  
- **Natural Language Querying:** Users can now input questions or requests in plain English directly within the Cosmos DB extension. The AI assistant interprets these inputs and generates optimized Cosmos DB queries automatically.
- **Optimized Query Generation:** The assistant provides queries tailored to Azure Cosmos DB’s syntax and performance best practices, minimizing manual tuning.
- **Chat Participant Command:** The extension introduces a chat-based interface, allowing users to interact with the AI assistant in a conversational manner. This feature supports iterative query refinement and contextual assistance.
- **Reduced Manual Effort:** By automating query generation and providing contextual guidance, the AI assistant reduces the need for manual coding and troubleshooting.

**Technical Mechanisms and Implementation Methods**  
The AI assistant is integrated into the Azure Cosmos DB extension for Visual Studio Code. It utilizes advanced natural language processing models to parse user input and translate it into valid Cosmos DB queries. The chat interface is embedded within the extension, enabling real-time interaction. The AI models are likely hosted and managed by Azure, ensuring scalability and reliability. The extension communicates with Azure Cosmos DB APIs to validate and execute generated queries.

**Use Cases and Application Scenarios**  
- **Rapid Query Development:** Developers can quickly generate queries for data retrieval, insertion, or modification without deep knowledge of Cosmos DB query syntax.
- **Data Exploration:** Analysts can ask exploratory questions in plain English, receiving immediate query suggestions to investigate data trends or anomalies.
- **Educational Scenarios:** New users can learn Cosmos DB query syntax by observing AI-generated queries based on their natural language inputs.
- **Iterative Query Optimization:** Users can refine queries through conversational interaction, improving performance and accuracy with AI guidance.

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be fully stable or feature-complete. Users should exercise caution when deploying in production environments.
- **Query Accuracy:** While the AI assistant aims to generate optimized queries, users should validate the output for correctness and efficiency, especially for complex scenarios.
- **Security and Privacy:** Users should avoid inputting sensitive data into the AI assistant, as natural language processing may involve external processing.
- **Extension Dependency:** The AI assistant is available exclusively within the Azure Cosmos DB extension for Visual Studio Code and requires the latest version of the extension.

**Integration with Related Azure Services**  
The AI assistant is tightly integrated with Azure Cosmos DB, leveraging its APIs for query execution. It operates within the Visual Studio Code environment, which is commonly used for Azure development workflows. The assistant may utilize Azure’s AI and machine learning services for natural language processing, though specific integration details are not provided.

**Summary Sentence**  
The public preview of the AI Assistant in the Azure Cosmos DB extension for Visual Studio Code enables users to generate optimized queries and interact with their data using plain English, significantly reducing manual effort and accelerating data workflows.

---

### 90. Generally Available: Change partition keys in Azure Cosmos DB for NoSQL API

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Change partition keys in Azure Cosmos DB for NoSQL API](https://azure.microsoft.com/updates?id=563017)

**Update ID**: 563017
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- **What was updated**  
Azure Cosmos DB for NoSQL API now supports changing the partition key of an existing container directly from the Azure portal.

- **Key changes or new features**  
  - You can change the partition key of a Cosmos DB NoSQL container with just a few clicks in the Azure portal.  
  - The process is available in both online and offline modes, allowing you to choose between minimal downtime or a full outage, depending on your application’s needs.  
  - Data is copied from the source container to a new container with the new partition key, using the Change Feed mechanism to ensure data consistency.

- **Target audience affected**  
  - Developers and IT professionals managing Azure Cosmos DB NoSQL workloads, especially those needing to optimize partitioning for performance or scalability.

- **Important notes if any**  
  - The operation creates a new container and copies all data, which may incur additional costs and time depending on data size.  
  - Application changes may be required to point to the new container after the partition key change.  
  - Review the Azure documentation for guidance on best practices and limitations before initiating the partition key change.

[Read the official update](https://azure.microsoft.com/updates?id=563017)

**Details**:

**Azure Update Report**

**Title:** Generally Available: Change partition keys in Azure Cosmos DB for NoSQL API  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563017)

---

**Background and Purpose of the Update**  
Partition keys are fundamental to the scalability and performance of Azure Cosmos DB NoSQL containers. Historically, changing the partition key of an existing container was not supported, requiring manual data migration and application downtime. This update addresses the need for flexibility in partition key management, allowing organizations to adapt their data models as requirements evolve without significant operational overhead.

**Specific Features and Detailed Changes**  
With this update, Azure Cosmos DB now allows users to change the partition key of a NoSQL container directly from the Azure portal. The feature is accessible via a streamlined interface, enabling users to initiate the partition key change with minimal steps. The process supports both online and offline modes, providing options to suit different operational needs. Data is copied from the source container to a new container, ensuring that the new partition key is applied throughout the dataset.

**Technical Mechanisms and Implementation Methods**  
The partition key change is implemented by creating a new container with the desired partition key configuration. Data from the original container is then copied to the new container. The process can be executed in two modes:
- **Online Mode:** Data migration occurs while the source container remains available for read and write operations, minimizing downtime.
- **Offline Mode:** The source container is temporarily unavailable during the migration, which may be preferable for scenarios requiring strict data consistency or minimal operational complexity.

The migration leverages the Cosmos DB Change Feed (as indicated by the partial content), ensuring efficient and reliable data transfer. The Azure portal automates the migration workflow, reducing manual intervention and potential errors.

**Use Cases and Application Scenarios**  
- **Schema Evolution:** Organizations can adapt their partitioning strategy as their data access patterns change, improving performance and scalability.
- **Performance Optimization:** If the original partition key leads to hotspots or uneven data distribution, changing the partition key can resolve these issues.
- **Application Modernization:** Migrating legacy applications to Cosmos DB and optimizing partition keys post-migration.
- **Compliance and Data Management:** Adjusting partition keys to align with regulatory requirements or new business logic.

**Important Considerations and Limitations**  
- The process involves creating a new container; application endpoints and connection strings may need to be updated accordingly.
- Data migration may incur additional costs, including storage and throughput during the copy operation.
- Offline mode results in temporary unavailability of the source container, which may impact dependent applications.
- The update is available only for containers using the NoSQL API.
- Users should validate the new partition key’s suitability for their workload to avoid future scalability or performance issues.

**Integration with Related Azure Services**  
This feature is integrated within the Azure portal, leveraging Cosmos DB’s native capabilities such as the Change Feed for data migration. It complements other Azure services that depend on Cosmos DB, such as Azure Functions, Logic Apps, and Azure Synapse Analytics, by enabling seamless partition key management without disrupting service integration.

---

**Summary Sentence:**  
Azure Cosmos DB for NoSQL API now enables direct partition key changes from the Azure portal, supporting both online and offline migration modes to streamline data management and improve operational flexibility.

---

### 91. Public Preview: New Azure Cosmos DB cost estimator

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: New Azure Cosmos DB cost estimator](https://azure.microsoft.com/updates?id=562976)

**Update ID**: 562976
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB has introduced a new cost estimator tool, now available in public preview.

- Key changes or new features  
The Azure Cosmos DB cost estimator allows users to quickly and accurately model estimated costs for their Cosmos DB deployments. Users can input parameters such as throughput, storage, number of regions, and capacity mode (provisioned or serverless) to forecast costs before creating any resources. The tool provides instant feedback, helping users optimize configurations and budget planning.

- Target audience affected  
This update primarily benefits developers, solution architects, and IT professionals responsible for designing, deploying, and managing Azure Cosmos DB workloads. It is especially useful for those planning new projects or migrations, as well as those seeking to optimize existing deployments.

- Important notes if any  
The cost estimator is currently in public preview, so features and estimates may change before general availability. It is designed to improve planning accuracy but should be used as a guide; actual costs may vary based on real-world usage. Integration with the Azure Portal and API-driven workflows enables seamless cost modeling during the design phase.

Data source: Using API data  
For more information, visit the [Azure Update page](https://azure.microsoft.com/updates?id=562976).

**Details**:

**Azure Update Report: Public Preview – New Azure Cosmos DB Cost Estimator**

**Background and Purpose of the Update:**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications. Accurately forecasting and managing costs for Cosmos DB deployments has been a challenge due to the complexity of factors such as throughput, storage, regional replication, and capacity modes. The introduction of the Azure Cosmos DB cost estimator in public preview addresses this challenge by providing IT professionals with a tool to model and estimate costs before provisioning resources.

**Specific Features and Detailed Changes:**  
The new Azure Cosmos DB cost estimator offers the following capabilities:
- **Throughput Modeling:** Users can input anticipated throughput requirements (measured in Request Units per second, RU/s) to estimate associated costs.
- **Storage Estimation:** The tool allows modeling of expected data storage needs, factoring in the impact on pricing.
- **Region Selection:** Users can simulate deployments across multiple Azure regions, helping to understand the cost implications of global distribution.
- **Capacity Mode Selection:** The estimator supports both provisioned and serverless capacity modes, enabling comparison of pricing models based on workload patterns.
- **Pre-Provisioning Simulation:** All modeling and estimation can be performed before creating any Cosmos DB account, reducing the risk of unexpected charges.

**Technical Mechanisms and Implementation Methods:**  
The cost estimator is implemented as an interactive tool, likely accessible via the Azure Portal or a dedicated web interface. It leverages up-to-date Azure Cosmos DB pricing models and integrates parameters such as RU/s, storage volume, number of regions, and capacity mode. The tool dynamically calculates projected costs based on user inputs, providing immediate feedback and allowing iterative scenario planning. This enables users to fine-tune configurations for optimal cost efficiency before actual deployment.

**Use Cases and Application Scenarios:**  
- **Pre-Deployment Planning:** Solution architects and database administrators can use the estimator to forecast costs for new applications, ensuring budget alignment.
- **Capacity Planning:** Teams can model different workload scenarios (e.g., peak vs. average usage) to determine the most cost-effective capacity mode.
- **Global Distribution Analysis:** Organizations with multi-region requirements can assess the financial impact of geographic replication.
- **Cost Optimization:** Existing Cosmos DB users can simulate changes to throughput or storage to evaluate potential savings before making adjustments.

**Important Considerations and Limitations:**  
- The estimator is currently in public preview; features and accuracy may evolve based on user feedback and further development.
- Estimates are based on current Azure pricing and may not account for future pricing changes or discounts (e.g., reserved capacity, Azure Hybrid Benefit).
- The tool provides cost projections for Cosmos DB resources only and does not include costs for related services (e.g., network egress, backup, or integration with other Azure components).
- Actual costs may vary depending on real-world usage patterns and unforeseen factors.

**Integration with Related Azure Services:**  
While the estimator is focused on Cosmos DB, it complements broader Azure cost management practices. IT professionals can use the estimator in conjunction with Azure Cost Management and Billing tools to develop comprehensive budgeting and monitoring strategies. The estimator’s output can inform resource provisioning workflows and integration with Infrastructure as Code (IaC) pipelines, ensuring that cost considerations are embedded in the deployment lifecycle.

**Summary Sentence:**  
The public preview of the Azure Cosmos DB cost estimator provides IT professionals with a precise, pre-deployment tool to model and forecast costs for throughput, storage, regions, and capacity modes, enabling informed planning and cost optimization for Cosmos DB solutions.

---

### 92. Generally Available: Azure Cosmos DB all versions and deletes change feed mode

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Cosmos DB all versions and deletes change feed mode](https://azure.microsoft.com/updates?id=562971)

**Update ID**: 562971
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB's "all versions and deletes" change feed mode is now generally available.

- Key changes or new features  
This update introduces a change feed mode that provides a complete history of all changes—including inserts, updates (all versions), and deletes—to items in Cosmos DB containers. Unlike the default change feed, which only exposes the latest version of each item, this mode allows you to track every modification and deletion. Developers can now build scenarios such as auditing, versioned data processing, and data recovery with full fidelity.

- Target audience affected  
Developers and IT professionals working with Azure Cosmos DB, especially those building solutions requiring detailed change tracking, auditing, or event sourcing.

- Important notes if any  
To use this feature, you must enable the "all versions and deletes" mode on your Cosmos DB containers. This may increase storage and throughput consumption, so review your resource and cost implications. The feature is accessible via the Cosmos DB SDKs and API. For more details, refer to the official documentation: https://azure.microsoft.com/updates?id=562971

**Details**:

**Azure Update Technical Report: Azure Cosmos DB All Versions and Deletes Change Feed Mode (General Availability)**

**Background and Purpose of the Update**  
Azure Cosmos DB’s change feed is a powerful feature that allows users to track changes (inserts and updates) to items within a container. Traditionally, the default change feed mode only exposes the latest version of each item, which is sufficient for many scenarios but limits visibility into the full history of changes, including intermediate versions and deletions. The purpose of this update is to provide comprehensive visibility into all changes—every version and deletion—within Cosmos DB containers, supporting advanced auditing, compliance, and data synchronization requirements.

**Specific Features and Detailed Changes**  
With the general availability of the “all versions and deletes” change feed mode, users can now access a complete record of all mutations (inserts, updates, and deletes) that occur in their Cosmos DB containers. This mode differs from the default “latest version” mode by including:  
- Every version of an item, not just the most recent state  
- Explicit records of deleted items (tombstones), enabling tracking of deletions  
This enhancement enables more granular change tracking and supports scenarios where historical data lineage and deletion events are critical.

**Technical Mechanisms and Implementation Methods**  
The all versions and deletes change feed mode leverages Cosmos DB’s underlying multi-version concurrency control (MVCC) architecture. When enabled, the change feed emits an ordered sequence of change events for all versions of items, including delete operations.  
To utilize this feature, users must configure their Cosmos DB container to enable the all versions and deletes mode. Once enabled, applications can consume the change feed using the SDKs or Azure Functions triggers, specifying the desired mode. The change feed delivers each change event with metadata indicating the operation type (insert, update, or delete) and the corresponding version information.

**Use Cases and Application Scenarios**  
This feature is particularly valuable for:  
- **Audit and Compliance:** Maintaining a full audit trail of all data changes, including who made changes and when, for regulatory or security purposes.  
- **Data Synchronization:** Propagating all changes, including deletions, to downstream systems or data lakes for analytics or backup.  
- **Event Sourcing:** Implementing event-driven architectures that require a complete history of state changes for replay or debugging.  
- **Soft Deletes and Recovery:** Tracking deletions explicitly enables recovery scenarios and supports soft delete patterns.

**Important Considerations and Limitations**  
- Enabling all versions and deletes mode may increase storage and throughput consumption, as more change events are retained and processed.  
- Applications must be designed to handle multiple versions of the same item and deletion events appropriately.  
- This mode must be explicitly enabled; it is not the default behavior.  
- Retention and access patterns should be evaluated to manage costs and performance.

**Integration with Related Azure Services**  
The all versions and deletes change feed mode integrates seamlessly with Azure Functions, Azure Data Factory, and custom applications using the Cosmos DB SDKs. This allows for automated workflows, ETL processes, and real-time event processing based on the comprehensive change feed.

**Summary Sentence**  
Azure Cosmos DB’s all versions and deletes change feed mode is now generally available, providing complete visibility into every data change—including all versions and deletions—in your containers for advanced auditing, synchronization, and compliance scenarios.

---

### 93. Public Preview: Azure Logic Apps now enables developers to invoke Microsoft Foundry Agents directly from workflows. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Logic Apps now enables developers to invoke Microsoft Foundry Agents directly from workflows. ](https://azure.microsoft.com/updates?id=562939)

**Update ID**: 562939
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure Logic Apps now supports direct invocation of Microsoft Foundry Agents from workflows, available in Public Preview.

- Key changes or new features  
Developers can now integrate and trigger Microsoft Foundry Agents directly within Logic Apps workflows. This enhancement streamlines the process of operationalizing AI agents by bridging the gap between AI agent development (in Azure AI Foundry) and business process automation (in Logic Apps). Workflows can now seamlessly call Foundry Agents, enabling more intelligent automation scenarios.

- Target audience affected  
This update impacts developers, solution architects, and IT professionals who build or manage business process automation using Azure Logic Apps and are leveraging AI agents developed with Azure AI Foundry.

- Important notes if any  
This feature is currently in Public Preview and may be subject to changes before general availability. Integration allows for more rapid deployment of AI-powered automation, but users should validate workflows in non-production environments before widespread adoption. Review documentation for authentication and security best practices when invoking Foundry Agents via Logic Apps.

Data source: Using API data  
More info: [Azure Update Link](https://azure.microsoft.com/updates?id=562939)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Logic Apps now enables developers to invoke Microsoft Foundry Agents directly from workflows.

**Background and Purpose of the Update:**  
Organizations developing AI agents frequently encounter challenges in bridging the gap between the environments where agents are created and the platforms used for business process automation. Traditionally, integrating AI agent capabilities into automated workflows required custom connectors or intermediary services, leading to increased complexity and maintenance overhead. This update aims to streamline operationalization by enabling direct invocation of Microsoft Foundry Agents from Azure Logic Apps, thereby simplifying the integration of AI-driven actions within business process automation.

**Specific Features and Detailed Changes:**  
The update introduces native support for invoking Microsoft Foundry Agents within Azure Logic Apps workflows. Developers can now directly call Foundry Agents as part of their workflow steps, eliminating the need for external APIs or custom integration layers. This feature is available in public preview and enhances Logic Apps’ extensibility by allowing seamless orchestration of AI agent operations alongside other workflow actions.

**Technical Mechanisms and Implementation Methods:**  
Azure Logic Apps now provides a built-in connector or action that enables direct invocation of Microsoft Foundry Agents. When designing a workflow, developers can add a step to trigger a Foundry Agent, passing relevant input parameters and receiving output from the agent within the workflow context. This integration leverages Azure’s secure communication protocols and authentication mechanisms to ensure reliable and authorized interactions between Logic Apps and Foundry Agents. The implementation abstracts the complexities of API calls, offering a declarative approach to integrating AI agents into business processes.

**Use Cases and Application Scenarios:**  
- **Automated Customer Support:** Organizations can embed Foundry Agents into Logic Apps workflows to automate customer inquiry triage, leveraging AI for intent detection and response generation.
- **Document Processing:** Logic Apps can invoke Foundry Agents for intelligent document classification or extraction tasks as part of a larger workflow.
- **Business Process Automation:** AI agents can be operationalized for decision-making, anomaly detection, or predictive analytics within automated workflows, enhancing process efficiency and intelligence.
- **Integration with Existing Systems:** Logic Apps workflows can combine Foundry Agent actions with other Azure services (e.g., Azure Functions, Service Bus) to build end-to-end solutions.

**Important Considerations and Limitations:**  
- The feature is currently in public preview, which may imply limited support, evolving APIs, and potential changes before general availability.
- Developers should review documentation for authentication requirements, input/output schema, and any restrictions on agent invocation frequency or payload size.
- Monitoring and error handling should be implemented within Logic Apps workflows to manage agent invocation failures or unexpected outputs.
- Compatibility with existing Logic Apps connectors and actions should be validated to ensure seamless workflow execution.

**Integration with Related Azure Services:**  
This update enhances Azure Logic Apps’ interoperability with Azure AI Foundry, enabling direct utilization of AI agent capabilities within automated workflows. Logic Apps can orchestrate Foundry Agent actions alongside other Azure services such as Azure Functions, Azure Data Factory, and Azure Cognitive Services, facilitating comprehensive business process automation and AI integration.

**Summary Sentence:**  
Azure Logic Apps now supports direct invocation of Microsoft Foundry Agents from workflows, streamlining AI agent integration and operationalization within automated business processes in public preview.

---

### 94. Public Preview: Anyscale on Azure

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Anyscale on Azure](https://azure.microsoft.com/updates?id=562934)

**Update ID**: 562934
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Build

**Summary**:

- What was updated  
Anyscale on Azure is now available in Public Preview. Anyscale is a managed, cloud-native Ray platform designed for large-scale Python workloads, especially in machine learning and AI.

- Key changes or new features  
  - Fully managed Ray clusters on Azure, enabling distributed Python and AI/ML workloads at scale.  
  - Native integration with Azure services for streamlined resource management, security, and networking.  
  - Simplified deployment and scaling of Ray-based applications without infrastructure overhead.  
  - Enhanced monitoring, autoscaling, and cost management features for production workloads.

- Target audience affected  
  - Machine learning engineers, data scientists, and AI developers running large-scale Python workloads.  
  - IT professionals managing cloud infrastructure for AI/ML projects.

- Important notes if any  
  - Public Preview means features may change and are not yet generally available (GA).  
  - Anyscale on Azure enables teams to leverage Ray’s distributed computing capabilities with Azure’s security and compliance.  
  - Developers can focus on building and scaling AI/ML applications without managing underlying infrastructure.  
  - Review Azure documentation for region availability and onboarding instructions.

[More details](https://azure.microsoft.com/updates?id=562934)

**Details**:

**Azure Update Technical Report: Public Preview – Anyscale on Azure**

**Background and Purpose of the Update**  
Anyscale on Azure is now available in Public Preview, introducing a cloud-native managed Ray platform specifically designed for machine learning engineers and AI developers. The primary objective of this update is to enable users to run Python workloads at massive scale, leveraging distributed computing capabilities without sacrificing speed or operational control. This addresses the growing demand for scalable, efficient, and manageable infrastructure for AI and machine learning workloads in the cloud.

**Specific Features and Detailed Changes**  
- **Managed Ray Platform**: Anyscale on Azure provides a fully managed environment for Ray, a popular open-source framework for distributed Python and machine learning workloads.
- **Cloud-Native Integration**: The platform is natively integrated with Azure, offering seamless deployment and management of Ray clusters.
- **Scalability**: Users can scale their Python-based workloads to massive levels, taking advantage of Azure’s underlying compute resources.
- **Performance and Control**: The solution is designed to maintain high performance and provide fine-grained control over distributed workloads, catering to both development and production scenarios.

**Technical Mechanisms and Implementation Methods**  
- **Ray Orchestration**: Anyscale manages the orchestration of Ray clusters, handling provisioning, scaling, and lifecycle management on Azure infrastructure.
- **Python Workload Support**: The platform is optimized for Python, supporting a wide range of machine learning and AI libraries that are compatible with Ray.
- **Managed Service Model**: As a managed service, Anyscale abstracts away much of the operational complexity, such as cluster setup, resource allocation, and fault tolerance, allowing engineers to focus on workload development and execution.
- **Azure Resource Integration**: The service leverages Azure’s compute, storage, and networking capabilities to provide a robust and secure environment for distributed workloads.

**Use Cases and Application Scenarios**  
- **Large-Scale Machine Learning Training**: Ideal for training machine learning models that require distributed data processing and parallel computation.
- **AI Development and Experimentation**: Supports rapid prototyping and experimentation for AI developers working with Python.
- **Batch Data Processing**: Suitable for executing large-scale batch processing jobs, such as ETL pipelines or data transformation tasks, using Ray’s distributed execution model.

**Important Considerations and Limitations**  
- **Public Preview Status**: As the service is in Public Preview, it may not yet offer full production SLAs or feature completeness. Users should evaluate suitability for production use accordingly.
- **Service Boundaries**: The managed platform is specifically tailored for Ray workloads; other distributed frameworks or non-Python workloads may not be supported.
- **Operational Constraints**: Users should review Azure’s documentation for any limitations related to cluster size, supported regions, or integration features during the preview phase.

**Integration with Related Azure Services**  
- **Azure Compute**: Anyscale on Azure utilizes Azure’s compute resources, such as virtual machines and scale sets, to provision and manage Ray clusters.
- **Azure Networking and Security**: The platform integrates with Azure’s networking and security features to ensure secure and isolated execution environments.
- **Potential for Data Services Integration**: While not explicitly detailed, the platform is positioned to work alongside Azure’s data storage and analytics services, enhancing end-to-end machine learning workflows.

**Summary Sentence**  
Anyscale on Azure, now in Public Preview, delivers a managed, cloud-native Ray platform that empowers machine learning engineers and AI developers to efficiently run large-scale Python workloads with high performance and operational control on Azure.

---

### 95. Public Preview: Knowledge as a Service with Azure Logic Apps.

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Knowledge as a Service with Azure Logic Apps.](https://azure.microsoft.com/updates?id=562929)

**Update ID**: 562929
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure Logic Apps now offers "Knowledge as a Service" in Public Preview, simplifying Retrieval-Augmented Generation (RAG) workflows.

- Key changes or new features  
Developers can now leverage built-in connectors and actions within Logic Apps to create RAG solutions without building complex ingestion pipelines, managing embeddings, or configuring vector stores manually. The service abstracts away the operational overhead of chunking, retrieval, and orchestration, enabling low-code/no-code integration with various data sources and AI services. This update streamlines the process of building, deploying, and maintaining RAG-based applications.

- Target audience affected  
Developers and IT professionals building AI-powered applications, especially those interested in integrating RAG workflows, knowledge retrieval, or generative AI features into business processes using Azure Logic Apps.

- Important notes if any  
This feature is currently in Public Preview and may not be suitable for production workloads. Early adopters should evaluate the service for their use cases and monitor for updates as it moves toward general availability.

Data source: Using API data  
For more details, see the official update: https://azure.microsoft.com/updates?id=562929

**Details**:

**Azure Update Report: Public Preview – Knowledge as a Service with Azure Logic Apps**

**Background and Purpose of the Update:**  
The update addresses the complexity inherent in current Retrieval-Augmented Generation (RAG) implementations. Traditionally, deploying RAG solutions involves building and maintaining ingestion pipelines, handling data chunking and embeddings, configuring vector stores, and integrating retrieval layers, all of which require significant engineering effort and operational overhead. The purpose of this update is to simplify and streamline the process of implementing RAG by leveraging Azure Logic Apps, making it more accessible and manageable for organizations.

**Specific Features and Detailed Changes:**  
With this public preview, Azure Logic Apps introduces "Knowledge as a Service," a feature that abstracts and automates the core components of RAG workflows. This enhancement allows users to orchestrate RAG pipelines without the need to manually construct and operate each individual layer. The update provides pre-built connectors and workflow actions within Logic Apps, enabling users to ingest data, process chunking and embeddings, and interact with vector stores through a low-code/no-code interface.

**Technical Mechanisms and Implementation Methods:**  
Azure Logic Apps utilizes its workflow automation engine to encapsulate RAG processes as reusable components. Users can design workflows that automatically handle data ingestion, apply chunking strategies, generate embeddings, and store vectors, all within the Logic Apps designer. The platform manages the orchestration and execution of these steps, reducing the need for custom code and infrastructure management. Integration with Azure Cognitive Services and other AI capabilities is facilitated through Logic Apps connectors, ensuring seamless communication between services.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for organizations looking to implement RAG-based solutions for knowledge retrieval, document understanding, and enterprise search without deep expertise in AI infrastructure. Example scenarios include building intelligent chatbots that reference internal knowledge bases, automating document summarization and Q&A systems, and enhancing search capabilities within business applications. The low-code approach enables rapid prototyping and deployment by IT teams and citizen developers.

**Important Considerations and Limitations:**  
As this is a public preview, the feature set may be subject to change, and certain capabilities might be limited or not production-ready. Users should evaluate the preview in test environments before considering production deployment. It is important to review the documentation for supported data sources, vector store integrations, and any constraints on workflow complexity or scale. Operational monitoring, security, and compliance should be assessed based on the preview’s current capabilities.

**Integration with Related Azure Services:**  
Knowledge as a Service within Azure Logic Apps is designed to integrate seamlessly with other Azure services, such as Azure Cognitive Services for language understanding, Azure Storage for data management, and Azure AI Search for vector-based retrieval. Logic Apps’ extensive connector ecosystem allows for interoperability with both Microsoft and third-party services, enabling end-to-end automation across the Azure platform.

**Summary:**  
The public preview of Knowledge as a Service in Azure Logic Apps significantly simplifies the deployment and management of RAG solutions by providing automated, low-code orchestration of ingestion, chunking, embeddings, and retrieval processes, thereby reducing engineering complexity and accelerating time-to-value for AI-driven knowledge applications.

---

### 96. Public Preview: Azure Logic Apps Automation SKU for agentic business process automation. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Logic Apps Automation SKU for agentic business process automation. ](https://azure.microsoft.com/updates?id=562924)

**Update ID**: 562924
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure Logic Apps introduces a new Automation SKU in Public Preview, designed specifically for agentic business process automation.

- Key changes or new features  
The new Automation SKU enables developers to more easily orchestrate workflows that integrate APIs, AI agents, and other automation components into cohesive, production-ready business processes. It simplifies the process of connecting and managing multiple Azure services, reducing the need for custom integration code. The SKU is optimized for agentic automation scenarios, supporting advanced workflow capabilities and seamless integration with AI services.

- Target audience affected  
This update primarily impacts developers, solution architects, and IT professionals building automated business processes, especially those leveraging AI agents and complex workflow orchestration in Azure.

- Important notes if any  
The Automation SKU is currently in Public Preview, so it is recommended for development and testing rather than production workloads. Early adopters can provide feedback to influence the final release. Existing Logic Apps users should evaluate compatibility and migration paths if considering the new SKU for future projects.

Data source: Using API data  
For more details, visit the [Azure Update page](https://azure.microsoft.com/updates?id=562924).

**Details**:

**Azure Update Report: Public Preview – Azure Logic Apps Automation SKU for Agentic Business Process Automation**

**Background and Purpose of the Update:**  
The introduction of the Azure Logic Apps Automation SKU in public preview addresses the increasing demand for agentic automation within organizations. As businesses shift toward more autonomous, AI-driven processes, developers require streamlined solutions to integrate workflows, APIs, and AI agents into cohesive, production-ready business processes. Traditionally, achieving such integration has involved complex orchestration across multiple Azure services, resulting in increased development overhead and operational complexity.

**Specific Features and Detailed Changes:**  
This update introduces a new Automation SKU for Azure Logic Apps, specifically designed to facilitate agentic business process automation. The SKU provides enhanced capabilities for combining workflows, APIs, and AI agents within a unified environment. Key features include:
- Simplified orchestration of business processes involving both traditional APIs and AI agents.
- Production-readiness, enabling deployment of complex automations with reduced manual integration.
- A SKU-based offering, allowing organizations to select automation capabilities tailored to agentic scenarios.

**Technical Mechanisms and Implementation Methods:**  
The Automation SKU leverages the core Logic Apps engine, extending its workflow orchestration capabilities to natively support agentic automation patterns. Developers can design and deploy workflows that seamlessly invoke APIs and interact with AI agents, reducing the need for custom code or manual service integration. The SKU is provisioned and managed through the Azure Portal, CLI, or ARM templates, ensuring consistency with existing Azure resource management practices.

**Use Cases and Application Scenarios:**  
Typical use cases for the Logic Apps Automation SKU include:
- Automating end-to-end business processes that require both deterministic logic (via APIs) and adaptive, AI-driven decision-making (via agents).
- Integrating AI agents into existing workflows for tasks such as document processing, customer support, or intelligent routing.
- Rapidly deploying agentic automations in production environments with minimal custom development.

**Important Considerations and Limitations:**  
As this SKU is in public preview, it may be subject to feature changes, limited regional availability, and preview-specific support policies. Organizations should evaluate the SKU in non-production environments and review Azure’s preview terms before adopting it for critical workloads. Integration with certain advanced AI agents or third-party APIs may require additional configuration or custom connectors.

**Integration with Related Azure Services:**  
The Logic Apps Automation SKU is designed to work seamlessly with other Azure services, such as:
- Azure Functions for custom code execution within workflows.
- Azure API Management for managing and securing API integrations.
- Azure Cognitive Services and Azure OpenAI for embedding AI agent capabilities.
- Azure Monitor and Log Analytics for operational monitoring and diagnostics.

**Summary Sentence:**  
The public preview of the Azure Logic Apps Automation SKU enables IT professionals to efficiently orchestrate agentic business process automation by simplifying the integration of workflows, APIs, and AI agents into production-ready solutions.

---

### 97. Generally available: Generally available: Managed system node pools in AKS Automatic

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally available: Generally available: Managed system node pools in AKS Automatic](https://azure.microsoft.com/updates?id=562919)

**Update ID**: 562919
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Build

**Summary**:

- What was updated  
Managed system node pools in Azure Kubernetes Service (AKS) are now generally available with the AKS Automatic option.

- Key changes or new features  
The AKS Automatic feature automates the provisioning and management of system node pools. This means Azure now handles infrastructure tasks such as scaling, patching, and ensuring high availability for system node pools, reducing operational overhead. Developers and IT admins no longer need to manually manage these core components, enabling more focus on application workloads.

- Target audience affected  
This update is relevant to developers, DevOps engineers, and IT professionals who manage AKS clusters, especially those responsible for cluster infrastructure, scaling, and maintenance.

- Important notes if any  
- Existing AKS clusters can adopt managed system node pools to streamline operations.
- Automated management may impact custom configurations; review documentation to ensure compatibility with your workloads.
- This feature is intended to improve reliability and reduce the operational burden associated with AKS system node pools.

For more details, visit the [official update](https://azure.microsoft.com/updates?id=562919).

**Details**:

**Azure Update Technical Explanation: Managed System Node Pools in AKS Automatic (Generally Available)**

**Background and Purpose of the Update**  
Provisioning and maintaining system node pools in Azure Kubernetes Service (AKS) traditionally requires continuous operational effort. Tasks such as scaling, patching, and ensuring high availability of system node pools are the responsibility of the user or the operations team. The introduction of Managed System Node Pools in AKS Automatic aims to offload these responsibilities, allowing the Azure platform to automatically provision and manage the underlying infrastructure for system node pools. This update is designed to reduce operational overhead and simplify cluster management for IT professionals.

**Specific Features and Detailed Changes**  
With this update, AKS now offers Managed System Node Pools in "Automatic" mode as a generally available feature. The platform takes over the lifecycle management of system node pools, including their provisioning, scaling, patching, and availability. Users no longer need to manually intervene in these processes, as the Azure platform ensures that system node pools are always up-to-date and appropriately scaled to meet cluster requirements. This change streamlines the management experience and reduces the risk of misconfiguration or delayed updates.

**Technical Mechanisms and Implementation Methods**  
Managed System Node Pools in AKS Automatic leverage Azure’s underlying orchestration and automation capabilities. When this feature is enabled, AKS automatically creates and manages the system node pools required for cluster operations. The platform monitors the health and capacity of these node pools, applies necessary patches, and scales resources based on workload demands. The automation ensures that critical system components always have the required resources and are running on supported, secure infrastructure without manual intervention.

**Use Cases and Application Scenarios**  
This feature is particularly beneficial for organizations seeking to minimize operational complexity and focus on application workloads rather than infrastructure management. Common scenarios include:
- Enterprises running production AKS clusters that require high availability and security compliance.
- Teams with limited Kubernetes or infrastructure expertise who want to leverage managed services.
- Environments where rapid scaling and frequent patching are necessary to meet business or regulatory requirements.

**Important Considerations and Limitations**  
While Managed System Node Pools in AKS Automatic significantly reduce operational burden, users should be aware that control over certain configuration aspects may be limited compared to manually managed node pools. It is important to review Azure documentation for any constraints regarding customization, compatibility with specific workloads, or integration with custom scripts and extensions. Additionally, organizations should ensure that their cluster design aligns with the automated management model to avoid conflicts with existing operational practices.

**Integration with Related Azure Services**  
Managed System Node Pools in AKS Automatic are fully integrated with the broader Azure ecosystem. They work seamlessly with Azure monitoring, security, and compliance services, ensuring that node pool operations are visible and auditable through Azure Monitor, Azure Policy, and related tools. This integration supports end-to-end management and governance of AKS clusters within enterprise environments.

**Summary Sentence**  
Managed System Node Pools in AKS Automatic, now generally available, enable Azure to automatically provision, operate, and maintain system node pools in AKS clusters, reducing operational overhead and simplifying cluster lifecycle management for IT professionals.

---

### 98. Generally Available: Azure API Center now provides a data plane MCP server for enterprise-wide discovery of APIs and AI assets. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Center now provides a data plane MCP server for enterprise-wide discovery of APIs and AI assets. ](https://azure.microsoft.com/updates?id=562914)

**Update ID**: 562914
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Center is now generally available with a data plane MCP (Microsoft Cloud Platform) server, enabling enterprise-wide discovery of APIs and AI assets.

- Key changes or new features  
  - Introduction of a data plane MCP server in Azure API Center.  
  - Simplifies discovery and connection to enterprise MCP servers, APIs, AI assets, and related tools.  
  - Supports MCP-based tooling and AI agent integration at scale.  
  - Enhances centralized API and AI asset management for organizations.

- Target audience affected  
  - Developers building or integrating with APIs and AI assets across the enterprise.  
  - IT professionals managing API governance, discovery, and lifecycle.  
  - Teams adopting MCP-based tools and AI agents.

- Important notes if any  
  - This update streamlines enterprise API and AI asset discovery, improving productivity and governance.  
  - Supports large-scale adoption of AI and API solutions by providing a unified discovery mechanism.  
  - Organizations can leverage the MCP server to accelerate integration scenarios and maintain better control over their API landscape.

For more details, see the official update: https://azure.microsoft.com/updates?id=562914

**Details**:

**Azure Update Summary:**

Azure API Center is now generally available with a data plane MCP (Microsoft Cloud Platform) server, enabling enterprise-wide discovery of APIs and AI assets.

---

### Background and Purpose of the Update

As organizations scale their adoption of MCP-based tooling and AI agents, the number of APIs, tools, and AI assets within the enterprise ecosystem increases significantly. This growth creates challenges for developers who need efficient mechanisms to discover and connect to these resources. The update addresses the need for a unified and simplified discovery process, facilitating seamless integration and utilization of APIs and AI assets across the enterprise.

### Specific Features and Detailed Changes

- **Introduction of Data Plane MCP Server:** Azure API Center now includes a data plane MCP server, which acts as a centralized registry for APIs and AI assets.
- **Enterprise-Wide Discovery:** Developers can now discover APIs and AI assets across the organization, not limited to individual projects or teams.
- **Support for MCP-Based Tooling and AI Agents:** The update enhances compatibility with MCP-based development tools and AI agents, streamlining their ability to locate and interact with enterprise assets.

### Technical Mechanisms and Implementation Methods

- **Centralized Registry:** The data plane MCP server functions as a central repository, cataloging APIs and AI assets registered within the Azure API Center.
- **Discovery Protocols:** MCP-based tools and AI agents can query the MCP server to retrieve metadata and connection details for available APIs and assets.
- **Integration Points:** The server is designed to interoperate with existing MCP-based infrastructure, ensuring that discovery operations are consistent and scalable.

### Use Cases and Application Scenarios

- **Developer Productivity:** Developers can quickly locate and connect to required APIs and AI assets, reducing onboarding time and minimizing redundant integration efforts.
- **AI Agent Enablement:** AI agents operating within the enterprise can dynamically discover and utilize APIs and AI assets, supporting advanced automation and orchestration scenarios.
- **Enterprise Governance:** Centralized discovery supports governance and compliance by ensuring that only registered and approved APIs and assets are discoverable and consumable.

### Important Considerations and Limitations

- **Scope of Discovery:** Discovery is limited to APIs and AI assets registered within the Azure API Center’s MCP server. Assets outside this scope are not discoverable via this mechanism.
- **Tooling Compatibility:** Only MCP-based tools and AI agents can leverage the discovery features provided by the data plane MCP server.
- **Security and Access Controls:** Organizations must ensure proper access controls are in place to restrict discovery and usage of sensitive APIs and assets.

### Integration with Related Azure Services

- **Azure API Center:** The data plane MCP server is a core component of the Azure API Center, enhancing its role as a centralized API and asset management platform.
- **MCP-Based Tools and AI Agents:** The update is designed to work seamlessly with MCP-based development and AI tools, supporting enterprise integration strategies.
- **Other Azure Services:** While the update focuses on discovery, it can be combined with Azure services such as Azure API Management and Azure Active Directory for end-to-end API lifecycle management and access control.

---

This update provides a robust, enterprise-grade solution for centralized discovery of APIs and AI assets, streamlining development workflows and supporting scalable adoption of MCP-based tools and AI agents.

---

### 99. Generally Available: Azure API Center now supports agent registration, agent assessment, and Git-based synchronization. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Center now supports agent registration, agent assessment, and Git-based synchronization. ](https://azure.microsoft.com/updates?id=562909)

**Update ID**: 562909
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Center is now generally available with new capabilities: agent registration, agent assessment, and Git-based synchronization.

- Key changes or new features  
  - **Agent Registration:** Developers can now register autonomous AI agents in Azure API Center, making it easier to catalog and manage these assets centrally.  
  - **Agent Assessment:** The platform provides tools to assess registered agents, helping ensure compliance, quality, and readiness for reuse.  
  - **Git-based Synchronization:** API and agent definitions can now be synchronized with Git repositories, enabling version control, collaboration, and CI/CD integration.

- Target audience affected  
  - Developers building and deploying AI agents and APIs  
  - IT professionals responsible for API governance, lifecycle management, and automation  
  - Teams managing API and agent catalogs across enterprise environments

- Important notes if any  
  - These features support organizations aiming to automate workflows and orchestrate tasks using AI agents.  
  - Centralized discovery and governance of APIs and agents can improve reuse, compliance, and collaboration across teams.  
  - Git-based sync aligns API Center with modern DevOps practices, facilitating seamless integration into existing workflows.

[Read the official update](https://azure.microsoft.com/updates?id=562909)

**Details**:

**Azure Update Report: Generally Available – Azure API Center now supports agent registration, agent assessment, and Git-based synchronization**

---

**Background and Purpose of the Update**

As organizations increasingly develop autonomous AI agents to automate workflows and orchestrate enterprise tasks, there is a growing need for a centralized platform to discover, govern, and reuse these agent capabilities across teams. The Azure API Center addresses this requirement by providing a unified solution for managing APIs and, with this update, extends its capabilities to support AI agent lifecycle management. The purpose of this update is to streamline the integration and governance of AI agents within enterprise environments, enhancing collaboration and operational efficiency.

---

**Specific Features and Detailed Changes**

This update introduces three major features to Azure API Center:

1. **Agent Registration**  
   Developers can now register autonomous AI agents within the Azure API Center. This allows organizations to catalog agents alongside traditional APIs, providing a single pane of glass for managing both APIs and AI agents.

2. **Agent Assessment**  
   The platform now supports assessment capabilities for registered agents. This feature enables organizations to evaluate agents for compliance, security, and operational readiness, ensuring that only validated agents are deployed in production environments.

3. **Git-based Synchronization**  
   Azure API Center now integrates with Git repositories, enabling synchronization of agent and API definitions. This allows for source-controlled management of agent metadata and configurations, supporting DevOps practices and facilitating version control, auditing, and collaborative development.

---

**Technical Mechanisms and Implementation Methods**

- **Agent Registration** is facilitated through the Azure API Center interface or programmatically via API calls, allowing developers to submit agent metadata, endpoints, and operational details.
- **Agent Assessment** leverages built-in or custom assessment policies that can be applied to registered agents. These assessments may include validation checks, policy enforcement, and readiness reviews, which are tracked within the API Center.
- **Git-based Synchronization** is implemented by connecting the API Center to a Git repository. Changes made to agent or API definitions in the repository are automatically synchronized with the API Center, and vice versa, ensuring consistency between source control and the centralized catalog.

---

**Use Cases and Application Scenarios**

- **Enterprise AI Orchestration:** Centralized management of AI agents that automate business processes, enabling teams to discover and reuse agents across departments.
- **DevOps Integration:** Leveraging Git-based synchronization for CI/CD pipelines, ensuring agent definitions and configurations are versioned and auditable.
- **Compliance and Governance:** Applying assessment policies to agents before deployment to meet organizational security and compliance requirements.

---

**Important Considerations and Limitations**

- The update is generally available, indicating production readiness, but organizations should review compatibility with existing workflows.
- Assessment capabilities depend on the definition and enforcement of appropriate policies; organizations must configure these according to their compliance needs.
- Git-based synchronization requires proper repository access and permissions to ensure secure and reliable integration.

---

**Integration with Related Azure Services**

- **Azure API Management:** API Center can be used in conjunction with API Management for end-to-end API and agent lifecycle management.
- **Azure DevOps:** Git-based synchronization aligns with Azure DevOps workflows, supporting automated build and deployment pipelines.
- **Azure Security and Compliance Tools:** Agent assessment can be integrated with Azure Policy and other governance tools for enhanced compliance management.

---

**Summary**

Azure API Center now provides general availability support for agent registration, agent assessment, and Git-based synchronization, enabling organizations to centrally manage, govern, and integrate autonomous AI agents alongside APIs, with enhanced DevOps and compliance capabilities.

---

### 100. Generally Available: Azure Kubernetes Fleet Manager for Arc-enabled clusters

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Kubernetes Fleet Manager for Arc-enabled clusters](https://azure.microsoft.com/updates?id=562904)

**Update ID**: 562904
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Kubernetes Fleet Manager, Microsoft Build

**Summary**:

- What was updated  
Azure Kubernetes Fleet Manager is now generally available (GA) for managing Azure Arc-enabled Kubernetes clusters.

- Key changes or new features  
  - Azure Kubernetes Fleet Manager now supports Azure Arc-enabled Kubernetes clusters in GA.  
  - IT teams and developers can centrally manage, govern, and deploy applications across Kubernetes clusters running on-premises, in Azure, or in other clouds (hybrid/multi-cloud).  
  - Any CNCF-conformant Kubernetes cluster connected via Azure Arc can be included in a fleet, enabling unified operations, policy management, and application deployment.  
  - Provides a single control plane and consistent tooling for cluster lifecycle management, updates, and governance across diverse environments.

- Target audience affected  
  - IT professionals managing hybrid or multi-cloud Kubernetes environments.  
  - Developers deploying and operating applications across multiple Kubernetes clusters, including on-premises and other cloud providers.

- Important notes if any  
  - This GA release enables organizations to standardize Kubernetes management and governance using Azure tools, reducing operational complexity.  
  - Existing Azure Arc-enabled Kubernetes clusters can now be seamlessly integrated into Azure Kubernetes Fleet Manager for centralized management.  
  - Ensure clusters are CNCF-conformant and connected via Azure Arc to leverage these capabilities.

[More details](https://azure.microsoft.com/updates?id=562904)

**Details**:

**Azure Update Report: Generally Available – Azure Kubernetes Fleet Manager for Arc-enabled Clusters**

**Background and Purpose of the Update:**  
Managing Kubernetes clusters across hybrid and multi-cloud environments has traditionally been fragmented, requiring the use of multiple consoles, tools, and operational models. This fragmentation complicates cluster management, governance, and operational consistency for organizations operating in diverse environments. The purpose of this update is to address these challenges by making Azure Kubernetes Fleet Manager generally available (GA) for Azure Arc-enabled Kubernetes clusters. This enables organizations to centrally manage Kubernetes clusters, regardless of whether they are running on Azure, on-premises, or in other clouds, provided they are Arc-enabled.

**Specific Features and Detailed Changes:**  
With this update, Azure Kubernetes Fleet Manager now fully supports Azure Arc-enabled Kubernetes clusters in its GA release. This means that any CNCF-conformant Kubernetes cluster, once Arc-enabled, can be managed as part of a fleet within Azure. Key features include:

- Centralized management of Kubernetes clusters across hybrid and multi-cloud environments.
- Unified operational model and tooling for both Azure-native and Arc-enabled clusters.
- Fleet-level operations, such as policy enforcement, configuration management, and workload orchestration, can be performed across all registered clusters.
- Support for standard Kubernetes distributions that are CNCF-conformant, broadening the scope of manageable clusters.

**Technical Mechanisms and Implementation Methods:**  
Azure Kubernetes Fleet Manager leverages Azure Arc to onboard and connect external Kubernetes clusters to Azure. Once a cluster is Arc-enabled, it is registered with Azure and becomes manageable via Azure Resource Manager (ARM) APIs, Azure Portal, and CLI. Fleet Manager then allows these clusters to be grouped into logical fleets, enabling centralized operations. The management plane abstracts the underlying heterogeneity of the clusters, providing a consistent interface for fleet-wide actions such as policy application, configuration deployment, and monitoring.

**Use Cases and Application Scenarios:**  
- **Hybrid Cloud Management:** Organizations with Kubernetes clusters deployed on-premises, in Azure, and in other clouds can manage all clusters through a single Azure-based interface.
- **Multi-Cloud Governance:** Enterprises adopting a multi-cloud strategy can enforce consistent policies and configurations across clusters, regardless of their physical location.
- **Centralized Operations:** IT teams can streamline operations such as rolling out updates, applying security policies, and monitoring health across all clusters from Azure.
- **DevOps Enablement:** Developers and operators can use familiar Azure tools and APIs to manage the lifecycle of applications and infrastructure across distributed Kubernetes environments.

**Important Considerations and Limitations:**  
- Only CNCF-conformant Kubernetes clusters can be managed via Azure Kubernetes Fleet Manager once they are Arc-enabled.
- The update does not mention support for non-conformant or proprietary Kubernetes distributions.
- Organizations must ensure clusters are properly Arc-enabled to leverage Fleet Manager capabilities.
- Operational consistency depends on the correct configuration and connectivity of Arc agents on external clusters.

**Integration with Related Azure Services:**  
Azure Kubernetes Fleet Manager integrates with Azure Arc, which acts as the bridge to connect external Kubernetes clusters to Azure. Once clusters are Arc-enabled, they can be managed alongside native Azure Kubernetes Service (AKS) clusters. This integration allows organizations to leverage Azure Policy, Azure Monitor, and other Azure management tools across their entire Kubernetes fleet, providing a unified management and governance experience.

**Summary Sentence:**  
Azure Kubernetes Fleet Manager is now generally available for Azure Arc-enabled Kubernetes clusters, enabling centralized, consistent management and governance of CNCF-conformant clusters across hybrid and multi-cloud environments through Azure’s unified tooling and operational model.

---

### 101. Generally Available: Azure API Management Premium v2 now supports multiple custom domains

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Management Premium v2 now supports multiple custom domains](https://azure.microsoft.com/updates?id=562899)

**Update ID**: 562899
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management Premium v2 now supports multiple custom domains, and this feature is generally available.

- Key changes or new features  
Organizations can now configure multiple custom domain names for their API gateways, developer portals, and management endpoints within a single Azure API Management Premium v2 instance. This enables the use of different branded or organizational domain names (e.g., api.contoso.com, apis.hrportal.contoso.com) for various audiences or business units.

- Target audience affected  
Developers and IT professionals managing API Management solutions, especially those needing to expose APIs and portals under multiple domains for internal and external users.

- Important notes if any  
This feature is only available in the Premium v2 tier of Azure API Management. It helps organizations meet branding, security, and organizational requirements by allowing separation of API endpoints and portals by domain. Review your DNS and SSL certificate management processes to accommodate multiple custom domains.  
More details: [Azure Update link](https://azure.microsoft.com/updates?id=562899)

**Details**:

**Azure Update Report: Azure API Management Premium v2 Now Supports Multiple Custom Domains (Generally Available)**

**Background and Purpose of the Update:**  
Organizations frequently require the ability to expose APIs, developer portals, and management endpoints under distinct branded or organizational domain names. This is essential for maintaining clear separation between external and internal API consumers, supporting multiple business units, and aligning with corporate branding strategies. Previously, Azure API Management Premium v2 had limitations regarding the number of custom domains that could be configured, restricting flexibility for enterprises with complex domain requirements.

**Specific Features and Detailed Changes:**  
With this update, Azure API Management Premium v2 now supports the configuration of multiple custom domains. This enhancement allows users to assign different domain names to various endpoints within their API Management instance, such as:
- External API endpoints (e.g., api.contoso.com)
- Internal platform APIs (e.g., apis.hrportal.contoso.com)
- Developer portals and management endpoints

This feature is generally available, meaning it is fully supported and ready for production workloads.

**Technical Mechanisms and Implementation Methods:**  
The implementation involves configuring custom domain names within the Azure API Management Premium v2 instance. Administrators can:
- Map multiple domain names to different endpoints (API gateway, developer portal, management endpoint)
- Utilize Azure Resource Manager or Azure Portal for domain configuration
- Manage SSL certificates for each domain, ensuring secure HTTPS communication
- Leverage Azure’s DNS and certificate management capabilities for seamless integration

Each custom domain is associated with its own TLS/SSL certificate, and DNS records must be updated to point to the appropriate Azure API Management gateway endpoints.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for:
- Enterprises needing to expose APIs to external partners under a branded domain (e.g., api.contoso.com)
- Internal business units requiring dedicated domains for their APIs (e.g., apis.hrportal.contoso.com)
- Organizations that wish to provide a customized developer portal experience for different audiences
- Multi-tenant scenarios where each tenant or business unit requires a unique domain name for their APIs

**Important Considerations and Limitations:**  
- Proper DNS configuration is required for each custom domain, including CNAME or A records pointing to Azure API Management endpoints.
- Each domain must have a valid SSL certificate, which can be managed via Azure Key Vault or uploaded directly.
- The update is specific to the Premium v2 tier; other tiers may not support multiple custom domains.
- Careful planning is needed to avoid domain conflicts and ensure correct routing of API traffic.
- Monitoring and managing certificates for multiple domains increases operational complexity.

**Integration with Related Azure Services:**  
- Azure Key Vault: Used for secure storage and management of SSL certificates for custom domains.
- Azure DNS: Facilitates domain name resolution and management of DNS records for custom domains.
- Azure Resource Manager: Enables automated deployment and configuration of custom domains via ARM templates.
- Azure Active Directory: Can be integrated for authentication and authorization across different domain endpoints.

**Summary Sentence:**  
Azure API Management Premium v2 now generally supports multiple custom domains, enabling organizations to expose APIs, developer portals, and management endpoints under distinct branded or organizational domain names, thereby enhancing flexibility, branding, and security for enterprise API solutions.

---

### 102. Public Preview: Azure API Management now supports token metrics for all token types

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure API Management now supports token metrics for all token types](https://azure.microsoft.com/updates?id=562885)

**Update ID**: 562885
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management now supports token metrics for all token types in Public Preview.

- Key changes or new features  
The update expands token usage metrics beyond traditional prompt and completion tokens to include newer categories such as cached, reasoning, and thinking tokens. This enhancement enables organizations to monitor and analyze comprehensive token consumption data when using AI models via Azure API Management. Developers and IT professionals can now access detailed token metrics through API data, supporting more accurate usage tracking and cost management.

- Target audience affected  
Developers and IT professionals managing AI workloads, especially those integrating advanced AI models through Azure API Management, will benefit from these expanded metrics. Teams responsible for monitoring, optimizing, and billing AI API usage are directly impacted.

- Important notes if any  
This feature is currently in Public Preview and may be subject to changes before general availability. Organizations should review their monitoring and reporting configurations to take advantage of the new token categories. This update is particularly relevant for those using or planning to use advanced AI models that generate diverse token types beyond traditional prompt and completion tokens.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=562885

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure API Management now supports token metrics for all token types  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562885)

---

**Background and Purpose of the Update**  
As organizations increasingly leverage advanced AI models, the complexity of tracking token consumption has grown. Traditionally, metrics in AI workloads focused on prompt and completion tokens, which represent the input and output of AI models. However, modern AI models introduce additional token categories—such as cached, reasoning, or thinking tokens—that are not captured by legacy monitoring approaches. This update aims to provide comprehensive visibility into all token types consumed by AI models, enabling more accurate monitoring, cost management, and optimization.

**Specific Features and Detailed Changes**  
Azure API Management now offers support for token metrics across all token types in public preview. This enhancement expands metric collection beyond prompt and completion tokens to include newer categories such as cached tokens (tokens retrieved from cache rather than generated), reasoning tokens (tokens used during intermediate model reasoning steps), and thinking tokens (tokens associated with internal model processes). The update enables organizations to monitor, analyze, and report on the full spectrum of token usage within their AI-driven APIs.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages Azure API Management’s built-in analytics and monitoring capabilities. Token metrics are collected at the API gateway level, where API Management inspects traffic to identify and categorize token usage according to the expanded taxonomy. These metrics are exposed through Azure Monitor and can be accessed via the Azure portal, REST APIs, or integrated dashboards. The system aggregates token data per API operation, allowing granular visibility into consumption patterns. This mechanism ensures that all token types, regardless of their origin or function, are tracked consistently.

**Use Cases and Application Scenarios**  
- **Cost Optimization:** Organizations can identify which token types contribute most to usage and costs, enabling targeted optimization of AI model interactions.
- **Billing and Reporting:** Enterprises can produce more accurate usage reports for internal chargeback or external billing, especially when offering AI APIs as a service.
- **Performance Analysis:** Developers can analyze token distribution to optimize model prompts and reduce unnecessary token consumption.
- **Compliance and Governance:** Enhanced token tracking supports audit requirements and helps organizations enforce usage policies across different token types.

**Important Considerations and Limitations**  
- The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- Token categorization relies on the correct identification of token types at the API gateway; custom or proprietary token formats may require additional configuration.
- Integration with existing monitoring tools may require updates to dashboards and alerting rules to accommodate new token metrics.
- Organizations should review their API Management policies to ensure that token metrics collection does not impact performance or introduce privacy concerns.

**Integration with Related Azure Services**  
Token metrics are accessible via Azure Monitor, enabling integration with Log Analytics, Application Insights, and custom dashboards. This allows seamless correlation with other API Management metrics and broader Azure resource monitoring. The update also facilitates integration with Azure Cost Management for budgeting and forecasting, and with Azure Policy for enforcing governance rules based on token consumption.

---

**Summary Sentence:**  
Azure API Management now provides comprehensive token metrics for all token types in public preview, enabling organizations to monitor, analyze, and optimize AI model token consumption with expanded visibility and integration across Azure monitoring and governance tools.

---

### 103. Generally Available: Azure API Management now supports content safety controls for MCP and A2A APIs. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Management now supports content safety controls for MCP and A2A APIs. ](https://azure.microsoft.com/updates?id=562880)

**Update ID**: 562880
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management now offers general availability support for content safety controls specifically for Managed Control Plane (MCP) and Agent-to-Agent (A2A) APIs.

- Key changes or new features  
This update introduces built-in content safety controls that allow organizations to enforce consistent safety and compliance policies across agentic applications and MCP-based tools. Previously, teams often relied on fragmented or custom solutions to manage content safety. With this release, content moderation and compliance checks can be standardized and centrally managed within Azure API Management for both MCP and A2A API scenarios.

- Target audience affected  
Developers and IT professionals managing agentic applications, MCP-based tools, or A2A APIs, especially those responsible for API security, compliance, and governance.

- Important notes if any  
This feature streamlines the implementation of content safety policies, reducing the need for custom or third-party solutions. It enhances security and compliance for organizations deploying AI agents or agent-based integrations via APIs. Teams should review their existing API management configurations to leverage these new built-in controls for improved safety and policy enforcement.

Data source: Using API data  
For more details, see the official update: https://azure.microsoft.com/updates?id=562880

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
As organizations increasingly deploy agentic applications and tools based on Managed Control Plane (MCP) and Agent-to-Agent (A2A) APIs, there is a growing need to enforce consistent safety and compliance policies across agent interactions. Previously, many teams relied on fragmented or custom implementations to manage content safety, leading to inconsistent enforcement and increased operational complexity. This update addresses the need for a unified, scalable approach to content safety within Azure API Management.

**Specific Features and Detailed Changes:**  
Azure API Management now provides built-in support for content safety controls specifically for MCP and A2A APIs. This enhancement allows organizations to centrally define and enforce content safety policies, ensuring that all agent interactions via these APIs adhere to organizational compliance and safety standards. The update introduces new configuration options within API Management to enable content safety checks, policy enforcement, and monitoring for MCP and A2A endpoints.

**Technical Mechanisms and Implementation Methods:**  
Content safety controls are implemented as native policies within Azure API Management. Administrators can configure these policies at the API, operation, or product level, leveraging Azure’s policy engine to inspect and validate content exchanged between agents. The mechanism supports real-time content analysis, blocking or flagging unsafe content based on predefined rules. Integration with MCP and A2A APIs is seamless, allowing safety controls to be applied without modifying the underlying API code. Policy definitions can be managed through the Azure portal, ARM templates, or REST API, ensuring flexibility and automation in deployment.

**Use Cases and Application Scenarios:**  
- **Agentic Applications:** Organizations deploying intelligent agents that interact via MCP or A2A APIs can ensure all communications are compliant with safety standards.
- **Enterprise Compliance:** Enterprises with strict regulatory requirements can enforce content safety across internal and external agent interactions.
- **Centralized Policy Management:** IT teams can replace fragmented, custom content safety solutions with a unified, scalable platform, reducing maintenance overhead and improving consistency.

**Important Considerations and Limitations:**  
- The content safety controls are currently scoped to MCP and A2A APIs within Azure API Management; other API types may not be covered by this feature.
- Policy configuration requires careful planning to avoid unintended blocking or false positives, especially in complex agent interaction scenarios.
- Monitoring and reporting capabilities should be leveraged to audit policy effectiveness and adjust rules as needed.

**Integration with Related Azure Services:**  
This update enhances Azure API Management’s integration capabilities by allowing content safety controls to be applied alongside existing API security, authentication, and monitoring features. It can be combined with Azure Monitor for logging and alerting, Azure Active Directory for access control, and Azure Policy for broader governance. The unified approach streamlines compliance across agentic applications and MCP/A2A APIs, supporting enterprise-scale deployments.

**Summary Sentence:**  
Azure API Management now offers generally available content safety controls for MCP and A2A APIs, enabling organizations to centrally enforce safety and compliance policies across agent interactions with native, scalable policy mechanisms.

---

### 104. Public preview: Connector Namespace

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public preview: Connector Namespace](https://azure.microsoft.com/updates?id=562874)

**Update ID**: 562874
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure announced the public preview of Connector Namespace, a fully managed service designed to simplify integration with SaaS and line-of-business systems.

- Key changes or new features  
Connector Namespace provides pre-built, managed connectors that eliminate the need for custom API client code. The service handles common integration challenges such as authentication, credential management, retries, pagination, and webhooks. Developers can now connect to various services using standardized connectors, reducing integration complexity and operational overhead.

- Target audience affected  
This update is relevant for developers, integration specialists, and IT professionals who build or maintain applications that connect to third-party SaaS solutions or internal business systems.

- Important notes if any  
Connector Namespace is currently in public preview, so features and APIs may change before general availability. Early adopters should review documentation for supported connectors and integration patterns. Using Connector Namespace can accelerate development timelines and improve reliability by offloading integration management to Azure. For more details and to get started, visit the [Azure Update page](https://azure.microsoft.com/updates?id=562874).

**Details**:

**Azure Update: Public Preview – Connector Namespace**

**Background and Purpose of the Update**  
Integrating applications with SaaS (Software as a Service) and line-of-business (LOB) systems typically requires developers to write custom API client code for each service. This process involves managing credentials, implementing logic for retries and pagination, and handling webhooks, which increases development complexity and operational overhead. The purpose of the Connector Namespace update is to simplify and standardize the integration process by providing a fully managed service with pre-built connectors.

**Specific Features and Detailed Changes**  
Connector Namespace introduces a managed environment where developers can access pre-built connectors to various SaaS and LOB systems. This eliminates the need for custom integration code for each service. Key features include:
- **Pre-built Connectors**: Ready-to-use connectors for common SaaS and LOB systems.
- **Credential Management**: Centralized and secure handling of authentication and authorization for connected services.
- **Built-in Support for Retries and Pagination**: Automatic handling of common API integration patterns such as retry logic and data pagination.
- **Webhook Handling**: Simplified management of event-driven integrations via webhooks.

**Technical Mechanisms and Implementation Methods**  
Connector Namespace operates as a fully managed Azure service, abstracting away the complexities of direct API integration. Developers interact with the service through a standardized interface, leveraging Azure’s security and scalability. The service manages the lifecycle of API connections, including authentication, token refresh, and error handling. It also provides mechanisms for managing webhook subscriptions and processing incoming events.

**Use Cases and Application Scenarios**  
Connector Namespace is particularly useful in scenarios where applications need to integrate with multiple SaaS or LOB systems, such as:
- **Enterprise Application Integration**: Connecting internal business applications with external SaaS platforms like CRM, ERP, or HR systems.
- **Workflow Automation**: Enabling low-code or pro-code automation scenarios where data flows between different services.
- **Event-driven Architectures**: Simplifying the consumption and processing of webhook events from third-party services.

**Important Considerations and Limitations**  
- **Service Availability**: As this is a public preview, the service may not be available in all regions and may be subject to change.
- **Connector Coverage**: The set of available pre-built connectors may be limited during the preview phase.
- **Integration Boundaries**: The service is designed to handle standard integration patterns, but custom or highly specialized integration requirements may still necessitate custom code.

**Integration with Related Azure Services**  
Connector Namespace is designed to integrate seamlessly with other Azure services, such as:
- **Azure Logic Apps**: For building automated workflows that leverage pre-built connectors.
- **Azure Functions**: For serverless event-driven processing of data from connected services.
- **Azure API Management**: For exposing and managing APIs that utilize Connector Namespace integrations.

**Summary**  
Connector Namespace, now in public preview, is a fully managed Azure service that streamlines integration with SaaS and LOB systems by providing pre-built connectors, centralized credential management, and automated handling of common API patterns, reducing development effort and operational complexity for IT professionals.

---

### 105. Generally Available: Azure Logic Apps MCP Server. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Logic Apps MCP Server. ](https://azure.microsoft.com/updates?id=562868)

**Update ID**: 562868
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure Logic Apps MCP Server is now generally available.

- Key changes or new features  
Azure Logic Apps MCP Server enables direct integration between Logic Apps workflows and Microsoft Copilot Platform (MCP)-based tools and AI agents. This release eliminates the need for integration teams to build and maintain custom API layers just to expose existing workflows to AI agents. The MCP Server allows workflows to be called directly by agents, reducing development and operational overhead.

- Target audience affected  
This update is relevant for developers, integration specialists, and IT professionals working with Azure Logic Apps, AI agents, and MCP-based solutions. Teams responsible for workflow automation, API integration, and AI-driven process orchestration will benefit most.

- Important notes if any  
By removing the need for custom API plumbing, the MCP Server streamlines integration efforts, accelerates time-to-market, and reduces maintenance complexity. Organizations can now more easily leverage existing Logic Apps workflows within AI and Copilot scenarios. Review the official documentation for guidance on enabling and configuring MCP Server for your Logic Apps environment.

**Details**:

**Azure Update Report: General Availability of Azure Logic Apps MCP Server**

**Background and Purpose of the Update**  
With the increasing adoption of AI agents and Model Control Plane (MCP)-based tooling, integration teams are often required to expose existing workflows to these agents. Traditionally, this has involved building and maintaining custom API layers, which adds significant development overhead and operational complexity. The release of Azure Logic Apps MCP Server aims to address these challenges by streamlining the process of making workflows accessible to AI agents and MCP-based tools, reducing the need for custom integration code.

**Specific Features and Detailed Changes**  
The Azure Logic Apps MCP Server is now generally available, providing a standardized and managed way to expose Logic Apps workflows to MCP-based systems. This update eliminates the necessity for custom-built API layers, enabling direct invocation of workflows by AI agents and other MCP-compliant tools. Key features include:

- Native support for MCP-based tooling, allowing seamless integration with AI agents.
- Simplified workflow exposure, reducing the need for additional API management or custom connectors.
- Operational efficiency improvements by minimizing custom code and integration points.

**Technical Mechanisms and Implementation Methods**  
The MCP Server acts as a bridge between Azure Logic Apps and MCP-based clients. By registering workflows with the MCP Server, organizations can make them discoverable and callable by AI agents without additional API development. The server handles authentication, authorization, and invocation routing, ensuring secure and reliable execution of workflows. This managed approach abstracts away the complexities of protocol handling and endpoint management, allowing integration teams to focus on workflow logic rather than infrastructure.

**Use Cases and Application Scenarios**  
- **AI Agent Integration:** Organizations deploying AI agents that need to trigger business processes or workflows can now do so directly via MCP, without custom API layers.
- **MCP Tooling Automation:** Enterprises using MCP-based automation tools can orchestrate Logic Apps workflows as part of broader automation scenarios.
- **Legacy Workflow Enablement:** Existing Logic Apps workflows can be rapidly exposed to new AI-driven or MCP-compliant systems, accelerating digital transformation initiatives.

**Important Considerations and Limitations**  
- The MCP Server is designed specifically for integration with MCP-based tooling and AI agents; it may not be suitable for non-MCP scenarios.
- Security and access control are managed by the MCP Server, but organizations should review and configure permissions according to their compliance requirements.
- The update focuses on reducing operational complexity, but teams should validate compatibility with their existing Logic Apps workflows and MCP clients.

**Integration with Related Azure Services**  
The MCP Server works natively with Azure Logic Apps, leveraging its workflow orchestration capabilities. It can be integrated with other Azure services such as Azure API Management, Azure Functions, and Azure Active Directory for enhanced security, monitoring, and extensibility. This enables organizations to build comprehensive automation and integration solutions across the Azure ecosystem.

**Summary**  
The general availability of Azure Logic Apps MCP Server streamlines the integration of Logic Apps workflows with AI agents and MCP-based tooling, reducing development and operational overhead by eliminating the need for custom API layers.

---

### 106. Public Preview: Azure Logic Apps Codeful Workflows with Logic Apps Standard SDK. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Logic Apps Codeful Workflows with Logic Apps Standard SDK. ](https://azure.microsoft.com/updates?id=562863)

**Update ID**: 562863
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Build

**Summary**:

- What was updated  
Azure Logic Apps now offers Codeful Workflows in Public Preview, enabled by the new Logic Apps Standard SDK.

- Key changes or new features  
Developers can now author workflows directly in code (C#) using the Logic Apps Standard SDK, rather than only through designer-based models. This approach allows integration with modern DevOps practices, version control, and CI/CD pipelines. Codeful Workflows still leverage managed orchestration, enterprise connectors, and cloud-scale capabilities of Logic Apps. The SDK supports local development, debugging, and deployment to Azure.

- Target audience affected  
Developers and IT professionals building integration and automation solutions, especially those who prefer code-first approaches and want to integrate Logic Apps into existing software engineering workflows.

- Important notes if any  
This feature is in Public Preview and may not be suitable for production workloads yet. Existing designer-based workflows remain supported; this update adds a new code-based option. Review the documentation for SDK usage, limitations, and best practices. For more details, see the [Azure Update announcement](https://azure.microsoft.com/updates?id=562863).

**Details**:

**Azure Update Report: Public Preview – Azure Logic Apps Codeful Workflows with Logic Apps Standard SDK**

**Background and Purpose of the Update:**  
Modern integration and automation teams require the flexibility to define workflows directly in code, rather than relying solely on visual designers or declarative models. This update addresses the demand for code-first workflow development while retaining the benefits of Azure Logic Apps, such as managed orchestration, access to enterprise connectors, and cloud-scale operational capabilities. The purpose is to empower developers and integration specialists to build, manage, and deploy workflows using familiar coding paradigms, thus enhancing productivity and enabling more complex automation scenarios.

**Specific Features and Detailed Changes:**  
With the introduction of Codeful Workflows in public preview, Azure Logic Apps now supports the development of workflows using the Logic Apps Standard SDK. This SDK enables users to author workflows programmatically, leveraging the full capabilities of a code-based approach. Key features include:
- Direct workflow authoring in code, offering granular control over logic and flow.
- Continued access to managed orchestration provided by Logic Apps.
- Seamless integration with enterprise connectors for connectivity to various services and systems.
- Support for cloud-scale operations, ensuring workflows are robust and scalable.

**Technical Mechanisms and Implementation Methods:**  
The Logic Apps Standard SDK serves as the primary toolset for codeful workflow development. Developers can use the SDK within their preferred development environments to define workflow steps, conditions, and actions programmatically. The SDK abstracts the underlying orchestration engine, allowing code-defined workflows to be executed and managed by the Logic Apps runtime. This approach bridges the gap between traditional visual workflow design and modern code-centric development, enabling version control, CI/CD integration, and advanced logic implementation.

**Use Cases and Application Scenarios:**  
- **Complex Integrations:** Teams needing to implement intricate business logic or custom control flows that are cumbersome to express in visual designers.
- **DevOps and CI/CD:** Organizations integrating workflow definitions into source control and automated deployment pipelines.
- **Reusable Components:** Developers building reusable workflow components or libraries for broader organizational use.
- **Hybrid Automation:** Scenarios where codeful workflows interact with both cloud and on-premises systems via enterprise connectors.

**Important Considerations and Limitations:**  
- This feature is currently in public preview, which may entail limited support and potential changes before general availability.
- Users must familiarize themselves with the Logic Apps Standard SDK and its programming model.
- Existing workflows built with visual designers or declarative models may require migration or adaptation to leverage codeful workflows.
- Preview features should not be used for production-critical workloads without thorough validation.

**Integration with Related Azure Services:**  
Codeful workflows retain full compatibility with the broader Azure Logic Apps ecosystem, including managed connectors, triggers, and monitoring tools. They can be integrated with Azure DevOps for CI/CD, Azure Monitor for operational insights, and other Azure services as endpoints or workflow participants. This ensures that codeful workflows can participate in enterprise-grade automation and integration scenarios alongside traditional Logic Apps workflows.

**Summary Sentence:**  
Azure Logic Apps Codeful Workflows with the Logic Apps Standard SDK (public preview) enables direct code-based workflow authoring while maintaining managed orchestration, enterprise connectors, and cloud-scale capabilities, providing modern integration teams with enhanced flexibility and control.

---

### 107. Generally Available: Azure API Management now supports AI gateway capabilities for Anthropic and Vertex AI models. 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Management now supports AI gateway capabilities for Anthropic and Vertex AI models. ](https://azure.microsoft.com/updates?id=562858)

**Update ID**: 562858
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- **What was updated**  
Azure API Management is now generally available with AI gateway capabilities supporting Anthropic and Vertex AI models.

- **Key changes or new features**  
  - Azure API Management can now act as a unified AI gateway for Anthropic and Vertex AI models, in addition to previously supported models.
  - Platform teams can apply consistent security, governance, and monitoring policies across multiple external AI providers.
  - Centralized controls and telemetry are now available for model interactions, improving compliance, troubleshooting, and observability.
  - Developers can use Azure API Management to securely expose, manage, and monitor AI model endpoints from Anthropic and Vertex AI.

- **Target audience affected**  
  - Developers integrating Anthropic or Vertex AI models into Azure-based applications.
  - IT professionals and platform teams responsible for API governance, security, and monitoring across multi-cloud AI solutions.

- **Important notes if any**  
  - This update simplifies management of external AI models by providing a single entry point for policy enforcement and telemetry.
  - It helps organizations maintain compliance and operational consistency when using multiple AI providers.
  - Existing API Management policies and features can be leveraged for these new AI endpoints.  
  - More information: [Azure Update link](https://azure.microsoft.com/updates?id=562858)

**Details**:

**Azure Update Report: Azure API Management – AI Gateway Capabilities for Anthropic and Vertex AI Models (General Availability)**

**Background and Purpose of the Update**  
As organizations increasingly integrate external AI providers into their production applications, there is a growing need for platform teams to maintain consistent security, governance, and observability across multiple AI model providers. Traditionally, managing compliance, troubleshooting, and monitoring interactions with diverse AI models has been challenging due to the lack of centralized controls and telemetry. This update addresses these challenges by enabling Azure API Management (APIM) to act as an AI gateway, specifically supporting Anthropic and Vertex AI models.

**Specific Features and Detailed Changes**  
With this update, Azure API Management now provides native support for Anthropic and Vertex AI models as part of its AI gateway capabilities. This means that organizations can leverage APIM to centrally manage API traffic to these external AI providers. The key features include:

- **Centralized Security:** APIM enforces consistent authentication and authorization policies for requests to Anthropic and Vertex AI models.
- **Governance:** Platform teams can apply governance policies such as quota management, request throttling, and access control across AI model endpoints.
- **Observability:** Enhanced telemetry and logging are available for all interactions with Anthropic and Vertex AI models, enabling detailed monitoring and troubleshooting.
- **Unified Management:** APIM provides a single interface to manage APIs across multiple AI providers, simplifying operational complexity.

**Technical Mechanisms and Implementation Methods**  
Azure API Management acts as a proxy gateway between client applications and external AI model endpoints (Anthropic and Vertex AI). The technical implementation involves:

- **API Proxying:** APIM routes requests from client applications to the respective AI provider endpoints, applying configured policies and capturing telemetry.
- **Policy Enforcement:** APIM supports custom policies for authentication, authorization, rate limiting, and logging, which can be applied to AI model APIs.
- **Telemetry Collection:** APIM integrates with Azure Monitor to collect metrics, logs, and traces for all API interactions with Anthropic and Vertex AI models.
- **Configuration:** Platform teams can use the Azure Portal, ARM templates, or REST APIs to configure and manage AI gateway settings within APIM.

**Use Cases and Application Scenarios**  
- **Production AI Integration:** Enterprises deploying applications that utilize Anthropic or Vertex AI models can ensure consistent security and governance.
- **Compliance Management:** Organizations in regulated industries can enforce compliance policies and audit interactions with external AI providers.
- **Multi-Provider AI Strategy:** Teams managing AI workloads across multiple providers benefit from unified API management and observability.
- **Troubleshooting and Monitoring:** Enhanced telemetry allows for rapid identification and resolution of issues in AI model interactions.

**Important Considerations and Limitations**  
- **Provider-Specific Features:** The AI gateway capabilities are specific to Anthropic and Vertex AI models; other AI providers may not be supported.
- **Policy Configuration:** Proper configuration of APIM policies is required to ensure security and governance.
- **Telemetry Scope:** Observability is limited to interactions routed through APIM; direct calls to AI providers bypassing APIM will not be monitored.
- **Compliance Responsibility:** While APIM provides tools for governance, ultimate compliance responsibility remains with the organization.

**Integration with Related Azure Services**  
- **Azure Monitor:** Telemetry and logging from APIM can be integrated with Azure Monitor for centralized observability.
- **Azure Active Directory:** APIM can leverage Azure AD for authentication and authorization of API requests.
- **Azure Logic Apps / Functions:** APIM can orchestrate workflows involving AI models, integrating with other Azure services for end-to-end solutions.

**Summary Sentence**  
Azure API Management now generally supports AI gateway capabilities for Anthropic and Vertex AI models, enabling platform teams to centrally secure, govern, and observe interactions with these external AI providers in production environments.

---

### 108. Generally Available: Azure API Management workspaces now support the built-in gateway

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Management workspaces now support the built-in gateway](https://azure.microsoft.com/updates?id=562848)

**Update ID**: 562848
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management workspaces now support the built-in gateway, and this feature is generally available.

- Key changes or new features  
Previously, organizations using workspace-based API management required a dedicated workspace gateway and a Premium tier deployment to use API Management workspaces. With this update, the built-in gateway is now supported in workspaces, eliminating the need for a dedicated gateway and Premium tier. This reduces both cost and operational complexity. Developers and IT professionals can now manage and expose APIs within workspaces using the built-in gateway, streamlining API deployment and management.

- Target audience affected  
Developers and IT professionals managing APIs with Azure API Management, especially those using or planning to use workspace-based models.

- Important notes if any  
This update enables broader adoption of API Management workspaces by removing the Premium tier requirement, making it more cost-effective and easier to manage. Organizations can now leverage workspace-based API management with the built-in gateway on lower tiers, improving flexibility and scalability. Review your current API Management deployment to assess potential cost savings and operational improvements.  

Data source: [Azure Update](https://azure.microsoft.com/updates?id=562848)

**Details**:

**Azure Update Report: Azure API Management Workspaces Now Support the Built-in Gateway (Generally Available)**

**Background and Purpose of the Update**  
Previously, organizations adopting workspace-based API management models in Azure API Management (APIM) were required to deploy a dedicated workspace gateway and utilize the Premium tier. This approach increased both operational complexity and cost, as the dedicated gateway infrastructure and Premium tier pricing were mandatory for workspace-based API management. The purpose of this update is to streamline API management operations by enabling the use of the built-in gateway within workspaces, thereby reducing the need for additional infrastructure and lowering the entry barrier for organizations.

**Specific Features and Detailed Changes**  
With this update, Azure API Management workspaces now support the built-in gateway. This means that APIs managed within a workspace can be published and accessed via the built-in gateway, without requiring a dedicated workspace gateway or Premium tier deployment. The built-in gateway is a managed endpoint provided by Azure, which simplifies API exposure and management. The update removes the dependency on dedicated gateway resources, allowing organizations to leverage the built-in gateway for their workspace APIs, thus optimizing resource utilization and cost.

**Technical Mechanisms and Implementation Methods**  
The built-in gateway is a managed Azure resource that handles API traffic, authentication, and policy enforcement without requiring customers to provision or manage gateway infrastructure. With this update, when an API is published in a workspace, it can be configured to use the built-in gateway endpoint. This is accomplished through the Azure portal, REST API, or ARM templates, where API deployment settings now include the option to select the built-in gateway. The built-in gateway automatically handles routing, security, and policy execution for workspace APIs, leveraging Azure’s native scalability and reliability.

**Use Cases and Application Scenarios**  
- **Cost Optimization:** Organizations can manage APIs in workspaces without incurring the additional costs associated with dedicated gateways and Premium tier subscriptions.
- **Simplified Operations:** Teams can quickly set up workspace-based API management with minimal infrastructure overhead, making it ideal for development, testing, and production scenarios where operational simplicity is desired.
- **Multi-team API Management:** Enterprises with multiple teams or business units can use workspaces to segment API management responsibilities, now with the built-in gateway supporting each workspace.
- **Rapid Prototyping:** Developers can publish APIs in isolated workspaces and expose them via the built-in gateway for fast prototyping and iterative development.

**Important Considerations and Limitations**  
- The update removes the requirement for dedicated workspace gateways and Premium tier, but organizations should review their API traffic and security requirements to ensure the built-in gateway meets their needs.
- Existing deployments using dedicated gateways may need to update their configuration to leverage the built-in gateway.
- The built-in gateway may have limitations compared to dedicated gateways in terms of customization, network isolation, or advanced routing scenarios; organizations should consult Azure documentation for feature parity and constraints.

**Integration with Related Azure Services**  
The built-in gateway integrates seamlessly with other Azure services, such as Azure Active Directory for authentication, Azure Monitor for logging and diagnostics, and Azure DevOps for CI/CD automation. APIs managed in workspaces can leverage these integrations for end-to-end API lifecycle management, security, and monitoring.

**Summary Sentence**  
Azure API Management workspaces now support the built-in gateway, enabling organizations to manage and expose APIs within workspaces without the need for dedicated gateway infrastructure or Premium tier, thereby reducing cost and operational complexity.

---

### 109. Generally Available: Azure API Management adds support for Agent-to-Agent (A2A) APIs

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure API Management adds support for Agent-to-Agent (A2A) APIs](https://azure.microsoft.com/updates?id=562843)

**Update ID**: 562843
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Build

**Summary**:

- What was updated  
Azure API Management is now generally available with support for Agent-to-Agent (A2A) APIs.

- Key changes or new features  
This update enables organizations to manage, secure, and monitor agent-to-agent API traffic within Azure API Management. It extends API governance and policy enforcement to A2A communication, which is increasingly common in enterprise AI and agentic applications. Developers and IT admins can now apply consistent authentication, authorization, rate limiting, and monitoring to A2A APIs, just as they do for traditional APIs.

- Target audience affected  
This update is relevant for developers building agentic or AI-driven applications, IT professionals responsible for API governance, and organizations adopting agent-based architectures.

- Important notes if any  
Agent traffic, which previously operated outside standard API governance, can now be brought under the same management and security controls as other APIs. This enhances compliance, observability, and operational control for agent-based systems. Integration with Azure API Management policies and analytics is supported. No additional configuration is required for existing API Management users to begin managing A2A APIs.  

Data source: Using API data  
More info: [Azure Update Announcement](https://azure.microsoft.com/updates?id=562843)

**Details**:

**Azure Update Report: Generally Available – Azure API Management adds support for Agent-to-Agent (A2A) APIs**

**Background and Purpose of the Update**  
As organizations increasingly adopt agentic applications—systems where autonomous agents interact to perform tasks—agent-to-agent (A2A) communication is becoming a foundational element of enterprise AI architectures. Traditionally, agent traffic has operated outside the established API governance frameworks, making it challenging for IT teams to enforce security, compliance, and monitoring standards. This update addresses the gap by enabling Azure API Management (APIM) to support A2A APIs, thereby extending governance and control to agentic workloads.

**Specific Features and Detailed Changes**  
With this update, Azure API Management now provides native support for A2A APIs. This means that agent-generated API traffic can be routed through APIM, allowing organizations to apply the same governance, security, and monitoring policies as they do for traditional APIs. Key features include:

- **API Registration:** Agents can register their APIs within APIM, enabling centralized management.
- **Policy Enforcement:** Existing APIM policies (authentication, authorization, throttling, logging, etc.) can be applied to A2A API traffic.
- **Monitoring and Analytics:** Agent traffic is now visible in APIM’s analytics dashboards, providing insights into usage patterns and potential anomalies.
- **Lifecycle Management:** A2A APIs benefit from APIM’s versioning, deprecation, and lifecycle controls.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages APIM’s core architecture, where APIs are proxied through the APIM gateway. For A2A scenarios:

- **Agents are configured to send API requests via APIM endpoints.**
- **APIM processes these requests using its policy engine, applying configured rules and controls.**
- **Traffic is logged and monitored using APIM’s built-in telemetry and diagnostic tools.**
- **APIM can integrate with Azure Active Directory (AAD) for identity and access management, ensuring secure agent interactions.**

This approach ensures that agent traffic is subject to the same operational and security controls as human-initiated API calls.

**Use Cases and Application Scenarios**  
- **Enterprise AI Systems:** Where multiple autonomous agents collaborate, such as in orchestration of business processes or AI-driven automation.
- **IoT Deployments:** Devices acting as agents communicating with each other via APIs.
- **Microservices Architectures:** Agent-based services interacting in a distributed environment.
- **Regulated Industries:** Where compliance and auditability of agent interactions are required.

**Important Considerations and Limitations**  
- **Performance:** Routing agent traffic through APIM may introduce additional latency; performance testing is recommended.
- **Policy Complexity:** Applying granular policies to agent APIs may require careful configuration to avoid unintended restrictions.
- **Compatibility:** Ensure agents are capable of interacting with APIM endpoints and can handle APIM’s authentication mechanisms.
- **Cost:** Increased API traffic through APIM may affect pricing; review APIM’s billing model.

**Integration with Related Azure Services**  
- **Azure Active Directory:** For securing agent API access.
- **Azure Monitor and Log Analytics:** For extended monitoring and alerting on agent API traffic.
- **Azure Functions and Logic Apps:** For automating workflows triggered by agent APIs.
- **Azure DevOps:** For managing API lifecycle and deployment.

**Summary Sentence**  
Azure API Management now generally supports agent-to-agent (A2A) APIs, enabling organizations to apply governance, security, and monitoring to agentic application traffic within enterprise AI systems.

---

### 110. Generally Available: Azure Cosmos DB global secondary indexes

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Cosmos DB global secondary indexes](https://azure.microsoft.com/updates?id=562799)

**Update ID**: 562799
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB now offers General Availability (GA) of Global Secondary Indexes (GSIs).

- Key changes or new features  
GSIs are read-only containers that automatically stay in sync with your source data. They enable you to optimize and accelerate query performance for specific access patterns without modifying your application code or data model. GSIs support flexible indexing strategies, allowing you to create indexes on different attributes or partition keys than your primary container. This helps improve query efficiency and reduce latency for complex queries or analytical workloads.

- Target audience affected  
Developers and IT professionals working with Azure Cosmos DB, especially those managing large-scale, globally distributed applications or requiring enhanced query performance and scalability.

- Important notes if any  
GSIs are managed and maintained by Azure Cosmos DB, minimizing operational overhead. They are read-only and cannot be directly written to; all writes must go through the source container. Pricing is based on the provisioned throughput and storage used by the GSIs. Review the documentation for best practices on index design and cost management.  

[More details](https://azure.microsoft.com/updates?id=562799)

**Details**:

**Azure Update Report: General Availability of Azure Cosmos DB Global Secondary Indexes (GSIs)**  
[Reference: Azure Update](https://azure.microsoft.com/updates?id=562799)

---

**Background and Purpose of the Update:**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications requiring low latency and high availability. Traditionally, optimizing query performance in distributed databases often requires complex application logic or manual index management. The introduction of Global Secondary Indexes (GSIs) aims to simplify this process by providing a native, managed solution to accelerate query performance without increasing application complexity.

---

**Specific Features and Detailed Changes:**  
- **General Availability:** GSIs for Azure Cosmos DB are now generally available, moving from preview to full production support.
- **Read-only Containers:** GSIs are implemented as read-only containers that mirror the data from the source container.
- **Automatic Synchronization:** These containers automatically stay in sync with the source data, ensuring that queries run against the GSI reflect the latest state of the data.
- **No Application Code Changes:** Developers can leverage GSIs to optimize queries without modifying existing application code, reducing development overhead and risk.

---

**Technical Mechanisms and Implementation Methods:**  
- **Container-based Indexing:** A GSI is provisioned as a separate container within Azure Cosmos DB. It is configured to index specific attributes or partition keys optimized for targeted query patterns.
- **Data Synchronization:** The GSI container is kept up-to-date with the source container through automatic, managed synchronization. This ensures data consistency for read operations.
- **Query Routing:** When a query is executed, it can be directed to the GSI container, which is optimized for the specific query pattern, resulting in improved performance.
- **Read-only Nature:** Since GSIs are read-only, all write operations continue to be performed on the source container, while read operations benefit from the optimized indexes.

---

**Use Cases and Application Scenarios:**  
- **Optimizing Analytical Queries:** Applications that require complex analytical queries or aggregations on large datasets can benefit from GSIs by creating indexes tailored to these query patterns.
- **Multi-tenant Applications:** Scenarios where different tenants or user groups require different query optimizations can leverage GSIs without duplicating data or complicating application logic.
- **Read-heavy Workloads:** Workloads with high read-to-write ratios, especially those with diverse query patterns, can use GSIs to improve query latency and throughput.

---

**Important Considerations and Limitations:**  
- **Read-only Access:** GSIs are strictly read-only; all data modifications must occur on the source container.
- **Synchronization Latency:** While synchronization is automatic, there may be minimal latency between the source and GSI containers, which should be considered for scenarios requiring strict real-time consistency.
- **Cost Implications:** Provisioning additional GSI containers may incur extra costs for storage and throughput, depending on the size and usage patterns.
- **Operational Management:** GSIs are managed resources and must be monitored and maintained alongside the primary containers.

---

**Integration with Related Azure Services:**  
- **Seamless Integration:** GSIs are natively integrated within Azure Cosmos DB, requiring no external services or manual synchronization.
- **Compatibility:** They work with existing Cosmos DB APIs and tools, ensuring compatibility with current deployments and management workflows.

---

**Summary Sentence:**  
Azure Cosmos DB Global Secondary Indexes (GSIs) are now generally available, providing a managed, read-only, automatically synchronized indexing solution that significantly enhances query performance without increasing application complexity.

---

### 111. Public Preview: Agentic Retrieval Toolkit for Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Agentic Retrieval Toolkit for Azure Cosmos DB](https://azure.microsoft.com/updates?id=562794)

**Update ID**: 562794
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Agentic Retrieval Toolkit for Azure Cosmos DB is now available in public preview.

- Key changes or new features  
This toolkit introduces advanced retrieval-augmented generation (RAG) capabilities for Azure Cosmos DB, inspired by GraphRAG and multi-hop reasoning scenarios. It enables developers to build applications that can perform complex, multi-step data retrieval and reasoning over graph-like data structures stored in Cosmos DB. The toolkit supports agentic workflows, allowing for more sophisticated question answering and knowledge discovery by chaining multiple retrieval and reasoning steps.

- Target audience affected  
Developers and IT professionals building AI-powered applications on Azure Cosmos DB, especially those working with RAG, knowledge graphs, or multi-hop reasoning use cases.

- Important notes if any  
This is a public preview release; features and APIs may change before general availability. The toolkit is designed to enhance AI application capabilities, particularly for scenarios requiring advanced reasoning over interconnected data. Early adoption feedback is encouraged. For more details and to get started, refer to the official documentation: [Azure Update Link](https://azure.microsoft.com/updates?id=562794).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Agentic Retrieval Toolkit for Azure Cosmos DB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562794)

---

**Background and Purpose of the Update**

The Agentic Retrieval Toolkit for Azure Cosmos DB has entered public preview, targeting the development of advanced retrieval-augmented generation (RAG) applications. This toolkit is motivated by the need to address complex reasoning tasks, such as those found in GraphRAG and multiple-hop reasoning scenarios. The primary purpose is to enhance the retrieval capabilities of Azure Cosmos DB, enabling developers to build intelligent applications that require sophisticated data access patterns beyond simple queries.

---

**Specific Features and Detailed Changes**

- **Advanced Retrieval Capabilities:** The toolkit introduces mechanisms to support multi-hop reasoning, allowing applications to traverse and retrieve interconnected data in a graph-like manner.
- **GraphRAG Support:** By focusing on GraphRAG, the toolkit enables retrieval workflows that involve navigating relationships and dependencies between data entities, which is essential for knowledge graph and graph-based AI applications.
- **RAG Application Enablement:** The toolkit is designed to facilitate the construction of RAG applications, where retrieved data from Cosmos DB is used to augment generative AI models, improving the quality and relevance of generated content.

---

**Technical Mechanisms and Implementation Methods**

- **Agentic Retrieval:** The toolkit leverages agentic retrieval strategies, which involve orchestrating multiple retrieval steps or agents to gather and synthesize data from Cosmos DB. This is particularly useful for scenarios requiring multi-hop reasoning, where the retrieval process may span several related documents or entities.
- **Integration with Cosmos DB:** The toolkit operates natively with Azure Cosmos DB, utilizing its flexible data model and global distribution to efficiently execute complex retrieval operations.
- **Graph Traversal:** The toolkit supports graph traversal patterns, enabling applications to perform queries that follow relationships between nodes (documents) in the database, which is a foundational requirement for GraphRAG and similar reasoning tasks.

---

**Use Cases and Application Scenarios**

- **Knowledge Graph Applications:** The toolkit is ideal for applications that build or query knowledge graphs stored in Cosmos DB, supporting advanced reasoning and relationship exploration.
- **AI-Driven Content Generation:** RAG applications that combine retrieved data with generative AI models (such as large language models) can leverage the toolkit to improve context and accuracy.
- **Multi-Hop Reasoning Systems:** Systems that require chaining multiple retrieval steps to answer complex queries or perform logical inference will benefit from the toolkit’s capabilities.

---

**Important Considerations and Limitations**

- **Preview Status:** As the toolkit is in public preview, it may be subject to changes and may not be suitable for production workloads. Users should monitor for updates and provide feedback.
- **Compatibility:** The toolkit is specifically designed for Azure Cosmos DB and may not be directly applicable to other Azure database services.
- **Complexity:** Advanced retrieval patterns such as multi-hop reasoning may require careful design and optimization to ensure performance and scalability within Cosmos DB.

---

**Integration with Related Azure Services**

- **Azure Cosmos DB:** The toolkit is tightly integrated with Cosmos DB, leveraging its data model and querying capabilities.
- **Azure AI Services:** RAG applications built with the toolkit can be combined with Azure AI services, such as Azure OpenAI, to enable retrieval-augmented generation workflows.
- **Azure Data Integration:** The toolkit can be used alongside Azure Data Factory or Azure Synapse for broader data orchestration and analytics scenarios.

---

**Summary Sentence**

The Agentic Retrieval Toolkit for Azure Cosmos DB, now in public preview, introduces advanced retrieval and reasoning capabilities to support the development of sophisticated RAG applications, particularly those involving GraphRAG and multi-hop reasoning, by enhancing data access patterns and integration with generative AI workflows.

---

### 112. Public Preview: Semantic reranker in Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Semantic reranker in Azure Cosmos DB](https://azure.microsoft.com/updates?id=562784)

**Update ID**: 562784
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- **What was updated**  
Azure Cosmos DB introduces the public preview of the semantic reranker feature.

- **Key changes or new features**  
Semantic reranker enables more relevant query and search results in Azure Cosmos DB by reordering results based on semantic (contextual) meaning rather than just keyword matching. This feature leverages advanced AI models to analyze both the intent of the query and the meaning of the stored data, improving result accuracy for complex or ambiguous queries. It is accessible via API, allowing integration into existing applications and search experiences.

- **Target audience affected**  
Developers building applications on Azure Cosmos DB, especially those implementing search or recommendation features, and IT professionals managing data-driven solutions that require high-quality, context-aware search results.

- **Important notes if any**  
The semantic reranker is currently in public preview and may not be suitable for production workloads. Developers should evaluate performance and cost impacts before adoption. Integration requires use of the Cosmos DB API, and additional configuration may be necessary. For more details, refer to the [official update](https://azure.microsoft.com/updates?id=562784).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Semantic reranker in Azure Cosmos DB  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=562784)

---

### Background and Purpose of the Update

The introduction of the semantic reranker in Azure Cosmos DB addresses the need for enhanced query and search result relevance. Traditional database queries often rely on syntactic matching, which may not capture the contextual meaning or intent behind a query. This update aims to improve the quality of results returned from Cosmos DB by leveraging semantic analysis, thereby delivering more contextually relevant data to users and applications.

---

### Specific Features and Detailed Changes

- **Semantic Reranking Capability:** The semantic reranker is now available in public preview for Azure Cosmos DB. It can be applied to any query or search operation within Cosmos DB.
- **Contextual Reordering:** The reranker analyzes both the query and the underlying data, reordering the results based on semantic (contextual) relevance rather than just keyword or pattern matching.
- **Improved Relevance:** By understanding the meaning behind queries and data, the reranker ensures that the most contextually appropriate results are prioritized.

---

### Technical Mechanisms and Implementation Methods

- **Semantic Analysis Engine:** The reranker utilizes semantic analysis techniques to interpret the intent and context of queries. It compares this understanding with the meaning derived from the data stored in Cosmos DB.
- **Result Reordering:** After the initial query execution, the reranker processes the result set and reorders it according to semantic relevance scores.
- **Integration Point:** The semantic reranker operates as an additional processing layer on top of standard query execution, requiring no changes to the underlying data model.

---

### Use Cases and Application Scenarios

- **Enterprise Search:** Organizations can use the semantic reranker to enhance search experiences within applications that rely on Cosmos DB, ensuring users find the most relevant documents or records.
- **Recommendation Systems:** Applications that suggest content or products can benefit from improved relevance, increasing user engagement and satisfaction.
- **Knowledge Management:** Internal tools that aggregate and retrieve knowledge articles or FAQs can deliver more accurate answers by leveraging semantic reranking.

---

### Important Considerations and Limitations

- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate its performance and stability in test environments before broader adoption.
- **Scope of Application:** The reranker applies to queries and searches within Cosmos DB. There is no information provided about support for other data sources or cross-database queries.
- **No Additional Configuration Details Provided:** The update does not specify configuration steps, supported query types, or limitations regarding data size or throughput.

---

### Integration with Related Azure Services

- **Azure Cosmos DB:** The semantic reranker is integrated directly into Azure Cosmos DB, enhancing its native query and search capabilities.
- **No Mention of External Dependencies:** The update does not reference integration with other Azure services such as Azure Cognitive Search or AI services.

---

**Summary:**  
The public preview of semantic reranker in Azure Cosmos DB enables improved contextual relevance for query and search results by semantically analyzing and reordering data, offering enhanced user experiences for applications that depend on Cosmos DB.

---

### 113. Public Preview: Agent Memory Toolkit for Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Agent Memory Toolkit for Azure Cosmos DB](https://azure.microsoft.com/updates?id=562779)

**Update ID**: 562779
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Agent Memory Toolkit for Azure Cosmos DB is now available in public preview.

- Key changes or new features  
This toolkit introduces a customizable, code-first solution for building memory systems within agentic applications. It enables developers to create scalable, durable, and cost-efficient memory architectures using Azure Cosmos DB as the backend. The toolkit is designed to simplify the integration of persistent memory into AI agents, supporting advanced scenarios such as context retention, long-term knowledge storage, and efficient retrieval.

- Target audience affected  
Developers and IT professionals building agentic or AI-powered applications on Azure, especially those requiring persistent and scalable memory solutions.

- Important notes if any  
The toolkit is in public preview, so it may not be suitable for production workloads yet. Users can leverage the toolkit to accelerate development and experiment with advanced agent memory patterns, but should monitor for updates and best practices as the toolkit matures. Integration with Azure Cosmos DB ensures global distribution, high availability, and low-latency access to stored memory data.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=562779

**Details**:

**Azure Update Report: Public Preview – Agent Memory Toolkit for Azure Cosmos DB**

**Background and Purpose of the Update:**  
The Agent Memory Toolkit for Azure Cosmos DB has been introduced in public preview to support the development of agentic applications. These applications require robust, scalable, and persistent memory systems to manage and recall information across sessions and interactions. The toolkit is designed to accelerate the creation of such memory architectures by providing a customizable, code-first approach, leveraging the globally distributed and scalable nature of Azure Cosmos DB.

**Specific Features and Detailed Changes:**  
- **Customizable Memory Systems:** The toolkit offers developers the ability to tailor memory structures to the unique requirements of their agentic applications.
- **Code-First Solution:** Developers can define and manage memory constructs directly in code, streamlining integration into existing application workflows and CI/CD pipelines.
- **Scalability and Durability:** By utilizing Azure Cosmos DB as the underlying storage, the toolkit ensures that memory systems can scale horizontally and maintain high availability and durability.
- **Cost-Efficiency:** The toolkit is optimized to leverage Cosmos DB’s cost model, helping developers build memory solutions that are both performant and economical.

**Technical Mechanisms and Implementation Methods:**  
- The toolkit interfaces directly with Azure Cosmos DB, utilizing its APIs for data storage, retrieval, and management.
- Memory objects and structures are defined in code, which are then persisted in Cosmos DB containers.
- The toolkit likely provides abstractions or helper libraries (such as SDKs or code templates) to simplify common memory operations (e.g., storing, querying, updating agent memory).
- Developers can customize the schema and indexing strategies to optimize for their specific access patterns and performance requirements.

**Use Cases and Application Scenarios:**  
- **Conversational AI Agents:** Store and recall user preferences, conversation history, and contextual information across sessions.
- **Autonomous Agents:** Maintain persistent state, goals, and environmental knowledge for agents operating over long periods.
- **Recommendation Systems:** Track user interactions and feedback to refine recommendations over time.
- **Workflow Automation:** Persist workflow states and decision points for complex, multi-step automated processes.

**Important Considerations and Limitations:**  
- The toolkit is currently in public preview, which may entail limited support and potential changes before general availability.
- As a code-first solution, integration requires development resources and familiarity with both Cosmos DB and the toolkit’s programming model.
- Cost and performance are dependent on Cosmos DB’s configuration and usage patterns; careful planning of throughput, partitioning, and indexing is necessary.
- Durability and scalability are subject to Cosmos DB’s SLAs and regional availability.

**Integration with Related Azure Services:**  
- The toolkit is designed to work natively with Azure Cosmos DB, leveraging its multi-model, globally distributed database capabilities.
- It can be integrated into broader Azure solutions, such as Azure Functions for serverless compute, Azure Logic Apps for orchestration, and Azure Cognitive Services for AI-driven applications.
- The code-first approach facilitates integration with Azure DevOps for automated deployment and management.

**Summary Sentence:**  
The Agent Memory Toolkit for Azure Cosmos DB, now in public preview, provides a customizable, code-first solution for building scalable, durable, and cost-efficient memory systems to accelerate the development of agentic applications on Azure.

---

### 114. Public Preview: Safe key rotation for Azure Cosmos DB

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Safe key rotation for Azure Cosmos DB](https://azure.microsoft.com/updates?id=562774)

**Update ID**: 562774
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB introduces the Safe Key Rotation feature in Public Preview.

- Key changes or new features  
Safe Key Rotation provides visibility into when each Cosmos DB account key was last used. This enables developers and IT professionals to safely rotate keys by identifying which key is currently in use by applications. The feature helps prevent accidental outages caused by rotating a key that is still actively used.

- Target audience affected  
Developers and IT professionals managing Azure Cosmos DB accounts, especially those responsible for security, key management, and application uptime.

- Important notes if any  
This feature is currently in Public Preview and may not be available in all regions or for all Cosmos DB APIs. It is recommended to use this feature to enhance security practices and minimize the risk of application downtime during key rotation. Integration with existing key management workflows is advised for best results.

For more details, see the official update: https://azure.microsoft.com/updates?id=562774

**Details**:

**Azure Update Report: Public Preview – Safe Key Rotation for Azure Cosmos DB**

**Background and Purpose of the Update**  
The safe key rotation feature for Azure Cosmos DB addresses a critical security and operational challenge: rotating account keys without disrupting active applications. Traditionally, rotating Cosmos DB account keys is essential for security best practices, but without insight into key usage, administrators risk invalidating keys that are still in use, potentially causing application downtime or failures. This update aims to provide visibility into key usage, enabling safer and more confident key rotation processes.

**Specific Features and Detailed Changes**  
With this public preview, Azure Cosmos DB introduces a mechanism to track and display when each account key was last used. This feature enhances the key management experience by allowing administrators to see the last usage timestamp for each key directly within the Azure portal or via supported APIs. The update does not change the existing key rotation process but augments it with actionable insights, reducing the risk of premature key invalidation.

**Technical Mechanisms and Implementation Methods**  
The safe key rotation feature works by recording and exposing metadata about key usage. When an application or service authenticates to Cosmos DB using an account key, the system logs the timestamp of the last successful use for each key. This information is then made available to administrators, who can view the last-used date and time for both primary and secondary keys. The feature is integrated into the Cosmos DB management interface, allowing for seamless access to key usage data during the rotation workflow.

**Use Cases and Application Scenarios**  
- **Planned Key Rotation:** Enterprises with regular key rotation policies can use the last-used timestamp to ensure a key is no longer in active use before rotating or invalidating it.
- **Incident Response:** In the event of a suspected key compromise, administrators can quickly assess which keys are actively used and coordinate safe rotation without disrupting services.
- **Compliance:** Organizations with strict compliance requirements can demonstrate and document safe key management practices using the visibility provided by this feature.

**Important Considerations and Limitations**  
- The feature is currently in public preview, which means it may not be available in all regions or for all Cosmos DB account types.
- The last-used timestamp reflects only successful authentication attempts; it does not provide details about which application or client used the key.
- Administrators should continue to follow established key rotation best practices and not rely solely on the last-used timestamp for critical security decisions.
- There may be a slight delay between key usage and the update of the last-used timestamp due to system processing times.

**Integration with Related Azure Services**  
The safe key rotation feature is designed to work natively within Azure Cosmos DB and integrates with the Azure portal’s key management experience. While it does not directly interface with Azure Key Vault or other external key management solutions, it complements these services by providing additional operational visibility. Administrators using automated deployment or configuration management tools can leverage the API access to programmatically retrieve key usage information as part of their DevOps workflows.

**Summary Sentence**  
The public preview of safe key rotation for Azure Cosmos DB enhances security and operational reliability by providing visibility into the last usage of account keys, enabling IT professionals to rotate keys with confidence and minimize application disruption.

---

### 115. Public Preview: Integrated embeddings for Azure Cosmos DB for NoSQL

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Integrated embeddings for Azure Cosmos DB for NoSQL](https://azure.microsoft.com/updates?id=562764)

**Update ID**: 562764
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Cosmos DB for NoSQL now offers integrated embeddings in public preview.

- Key changes or new features  
Developers can now automatically generate and maintain vector embeddings for their data directly within Azure Cosmos DB for NoSQL, eliminating the need for separate data pipelines or external embedding generation services. This integration streamlines the process of building AI-powered applications, such as semantic search, recommendation systems, and generative AI solutions, by enabling vector search and similarity queries natively within the database.

- Target audience affected  
This update is relevant to developers and IT professionals building AI/ML applications, especially those leveraging Azure Cosmos DB for NoSQL as their data store. It is particularly beneficial for teams working on applications requiring semantic search, personalization, or generative AI capabilities.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production workloads. Users should review the preview documentation for limitations, supported regions, and pricing details. Integration with Azure AI services and APIs is simplified, but developers should validate compatibility with their existing data models and AI workflows. For more information, refer to the official [Azure Update announcement](https://azure.microsoft.com/updates?id=562764).

**Details**:

**Azure Update Summary: Public Preview – Integrated Embeddings for Azure Cosmos DB for NoSQL**

**Background and Purpose of the Update:**  
This update introduces integrated embeddings for Azure Cosmos DB for NoSQL, now available in public preview. The primary goal is to simplify the development of AI applications that leverage data stored in Azure Cosmos DB. Traditionally, generating vector embeddings from data required building and maintaining separate data pipelines, often involving external services or custom code. This update aims to streamline the process by enabling automatic generation and maintenance of embeddings directly within Azure Cosmos DB for NoSQL.

**Specific Features and Detailed Changes:**  
- **Automatic Embedding Generation:** Azure Cosmos DB for NoSQL can now automatically create and update embeddings for your data. This eliminates the need for external ETL (Extract, Transform, Load) processes or custom embedding generation logic.
- **Integrated Maintenance:** The service manages the lifecycle of embeddings, ensuring they remain synchronized with the underlying data as it changes.
- **Public Preview Availability:** The feature is currently in public preview, allowing customers to evaluate and test the functionality before general availability.

**Technical Mechanisms and Implementation Methods:**  
- **Native Embedding Support:** The embedding generation is integrated into the Cosmos DB for NoSQL engine. When data is ingested or updated, the system automatically computes and stores the corresponding embeddings.
- **No Separate Pipeline Required:** Unlike traditional approaches where data is exported to an external service (such as Azure OpenAI or custom ML models) for embedding generation, this feature operates entirely within the Cosmos DB environment.
- **Maintenance and Synchronization:** Embeddings are kept up-to-date with the source data, reducing the risk of stale or inconsistent vector representations.

**Use Cases and Application Scenarios:**  
- **AI Application Development:** Developers building AI-powered applications (e.g., semantic search, recommendation systems, or natural language processing solutions) can leverage integrated embeddings to enable advanced querying and analysis without additional infrastructure.
- **Real-Time Data Processing:** Applications that require up-to-date embeddings for streaming or frequently changing data benefit from the automatic synchronization of embeddings with the source data.
- **Simplified Architecture:** Organizations can reduce operational complexity by eliminating the need for separate embedding pipelines, leading to faster development cycles and easier maintenance.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should evaluate the feature in test environments and monitor for updates regarding general availability.
- **Scope:** The feature is specific to Azure Cosmos DB for NoSQL and may not be available for other Cosmos DB APIs (e.g., MongoDB, Cassandra, Gremlin, Table).
- **Documentation and Support:** Users should refer to official Azure documentation for configuration, supported data types, and any limitations related to embedding size, update frequency, or supported operations.

**Integration with Related Azure Services:**  
- **Azure AI Services:** While integrated embeddings reduce the need for external embedding generation, they can complement other Azure AI services, such as Azure Cognitive Search, for building end-to-end AI solutions.
- **Data Workflows:** The feature can be incorporated into broader data workflows involving Azure Data Factory, Azure Synapse Analytics, or other data integration tools, further streamlining AI application development.

**Summary Sentence:**  
Azure Cosmos DB for NoSQL now offers integrated, automatically maintained embeddings in public preview, simplifying AI application development by eliminating the need for separate embedding pipelines and ensuring embeddings remain synchronized with your data.

---

### 116. Public Preview: OmniVec, an open-source embedding toolkit for Azure

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: OmniVec, an open-source embedding toolkit for Azure](https://azure.microsoft.com/updates?id=562759)

**Update ID**: 562759
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure announced the public preview of OmniVec, an open-source embedding toolkit designed to automate embedding generation from various data sources into Azure Cosmos DB and other Azure destinations.

- Key changes or new features  
  - OmniVec streamlines the process of extracting data, generating vector embeddings, and writing them to vector databases like Azure Cosmos DB.  
  - Supports multiple data sources and destinations within Azure, reducing the need for custom integration code.  
  - Open-source toolkit, enabling extensibility and community contributions.

- Target audience affected  
  - Developers building AI applications that require vector search or semantic search capabilities.  
  - IT professionals managing data pipelines and Azure data infrastructure.

- Important notes if any  
  - OmniVec simplifies the workflow for embedding generation, making it easier to integrate unstructured data into AI-powered applications on Azure.  
  - The toolkit is in public preview; production use should consider potential changes or limitations.  
  - Documentation and source code are available for customization and integration into existing Azure solutions.

For more information, see the [official update](https://azure.microsoft.com/updates?id=562759).

**Details**:

**Background and Purpose of the Update**

The introduction of OmniVec as an open-source embedding toolkit for Azure addresses the growing need for streamlined workflows in AI application development. Traditionally, building AI solutions that leverage vector databases requires manual integration of data extraction, embedding generation, and data ingestion processes. This update aims to automate and simplify these tasks, thereby accelerating development cycles and reducing operational complexity for IT professionals.

**Specific Features and Detailed Changes**

OmniVec enables automated embedding generation from multiple data sources directly into Azure Cosmos DB and other Azure destinations. Key features include:
- Support for multiple data sources, allowing organizations to extract data from various origins.
- Automated embedding generation, which transforms raw data into vector representations suitable for AI workloads.
- Direct integration with Azure Cosmos DB and other Azure storage or database services, facilitating seamless data flow into vector-enabled environments.

**Technical Mechanisms and Implementation Methods**

OmniVec operates as an open-source toolkit, which means IT professionals can access, modify, and extend its functionality as needed. The toolkit automates the pipeline that typically involves:
1. Extracting data from supported sources.
2. Generating embeddings using pre-defined or custom models.
3. Writing the resulting vectors into Azure Cosmos DB or other configured Azure destinations.

This automation reduces the need for custom scripting and manual orchestration, leveraging Azure’s scalable infrastructure to handle embedding workflows efficiently.

**Use Cases and Application Scenarios**

OmniVec is particularly useful in scenarios where organizations need to:
- Build AI applications that rely on semantic search, recommendation engines, or similarity matching, all of which require efficient vector storage and retrieval.
- Integrate unstructured or structured data from various sources into a unified vector database for downstream AI processing.
- Rapidly prototype and deploy AI features without building complex data pipelines from scratch.

**Important Considerations and Limitations**

While OmniVec automates key aspects of embedding generation and ingestion, IT professionals should consider:
- The toolkit is currently in public preview, which may imply limited support, potential changes, and the need for caution before deploying in production environments.
- Compatibility with data sources and Azure destinations may be constrained to specific services or formats as defined in the current release.
- Performance and scalability should be evaluated in the context of specific workloads, especially for large-scale or latency-sensitive applications.

**Integration with Related Azure Services**

OmniVec integrates natively with Azure Cosmos DB, enabling direct ingestion of vector data for use in vector search and other AI-powered scenarios. It also supports writing embeddings to other Azure destinations, potentially including Azure Blob Storage, Azure SQL Database, or other services as supported. This integration streamlines the process of operationalizing AI models within the Azure ecosystem, leveraging existing security, scalability, and management features.

**Summary Sentence**

OmniVec, now in public preview, is an open-source Azure toolkit that automates embedding generation from multiple data sources into Azure Cosmos DB and other destinations, simplifying the development of AI applications by streamlining data extraction, embedding, and ingestion workflows.

---

### 117. Generally Available: Azure Cosmos DB Linux emulator (vNext)

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Cosmos DB Linux emulator (vNext)](https://azure.microsoft.com/updates?id=562754)

**Update ID**: 562754
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure Cosmos DB Linux emulator (vNext) is now generally available. This is a cross-platform, Docker-based emulator for local development and testing with Azure Cosmos DB for NoSQL.

- Key changes or new features  
  - The emulator runs as a lightweight Docker container, enabling developers to simulate Azure Cosmos DB for NoSQL workloads locally on Linux, macOS, and Windows.  
  - Supports local development and automated testing scenarios without requiring a cloud subscription or incurring costs.  
  - Provides API compatibility with Azure Cosmos DB for NoSQL, allowing seamless transition from local development to cloud deployment.  
  - Enhanced developer productivity by supporting CI/CD pipelines and integration testing environments.

- Target audience affected  
  - Developers building applications with Azure Cosmos DB for NoSQL.  
  - DevOps and IT professionals managing development, testing, and CI/CD workflows across multiple platforms.

- Important notes if any  
  - The Linux emulator is intended for development and testing only; it is not supported for production workloads.  
  - The emulator can be easily integrated into local and automated testing environments using Docker.  
  - For more details and setup instructions, refer to the official documentation: https://aka.ms/cosmosdb-emulator-linux

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=562754

**Details**:

**Azure Update Report: General Availability of Azure Cosmos DB Linux Emulator (vNext)**

**Background and Purpose of the Update:**  
The general availability of the Azure Cosmos DB Linux emulator (vNext) addresses the need for a cross-platform, local development and testing environment for Azure Cosmos DB for NoSQL. Previously, the Cosmos DB emulator was primarily available for Windows environments, which limited development flexibility for teams using Linux or macOS. This update enables developers to emulate Cosmos DB locally on any platform that supports Docker, facilitating consistent development workflows and testing scenarios without incurring cloud resource costs or requiring an active Azure subscription.

**Specific Features and Detailed Changes:**  
- The vNext emulator is a Docker-based solution, allowing it to run as a lightweight container on Linux, macOS, and Windows systems.
- It emulates the Azure Cosmos DB for NoSQL API, enabling developers to test and validate their applications locally before deploying to the cloud.
- The emulator supports local development and testing scenarios, providing a feature set that closely mirrors the production Cosmos DB environment for NoSQL workloads.
- This release marks the transition from preview to general availability, signifying production-ready stability and support.

**Technical Mechanisms and Implementation Methods:**  
- The emulator is distributed as a Docker container image, which can be pulled and run using standard Docker commands.
- It encapsulates the necessary services to simulate the behavior of Azure Cosmos DB for NoSQL, including endpoint emulation, authentication, and data storage, within the containerized environment.
- Developers can interact with the emulator using the same SDKs, APIs, and connection strings as they would with the actual Azure Cosmos DB service, ensuring seamless code portability.
- The containerized approach simplifies setup, isolation, and teardown, supporting CI/CD pipelines and automated testing environments.

**Use Cases and Application Scenarios:**  
- Local development: Developers can build and test Cosmos DB-based applications on their local machines, regardless of the operating system.
- Automated testing: The emulator can be integrated into CI/CD workflows, enabling automated unit and integration testing without requiring access to live Azure resources.
- Cross-platform team collaboration: Teams using diverse development environments (Linux, macOS, Windows) can standardize on a single emulator for consistent results.
- Cost-effective prototyping: Developers can validate data models, queries, and application logic without incurring cloud costs.

**Important Considerations and Limitations:**  
- The emulator is intended for development and testing purposes only and is not supported for production workloads.
- While the emulator provides a high-fidelity simulation of Cosmos DB for NoSQL, there may be minor differences or unsupported features compared to the full Azure service.
- Users must ensure Docker is installed and properly configured on their development machines to utilize the emulator.
- The emulator is specific to the NoSQL API and may not support other Cosmos DB APIs (e.g., MongoDB, Cassandra, Gremlin, Table).

**Integration with Related Azure Services:**  
- Applications developed and tested against the emulator can be deployed to Azure Cosmos DB with minimal changes, as the emulator supports the same SDKs and APIs.
- The emulator can be used in conjunction with other Azure development tools and services, such as Azure Functions, Logic Apps, and App Services, for comprehensive local testing scenarios.
- It supports integration into DevOps pipelines, enhancing automated testing and validation processes before cloud deployment.

**Summary:**  
The Azure Cosmos DB Linux emulator (vNext) is now generally available, providing a cross-platform, Docker-based local development and testing environment for Azure Cosmos DB for NoSQL, enabling consistent and cost-effective workflows for engineering teams.

---

### 118. Public Preview: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)](https://azure.microsoft.com/updates?id=562569)

**Update ID**: 562569
**Data source**: Azure Updates API

**Categories**: In preview, Features

**Summary**:

- **What was updated**  
Microsoft Defender for Cloud now supports Azure Container Apps environments in its Serverless Containers Posture management, available in Public Preview.

- **Key changes or new features**  
  - Security teams can now onboard Azure Container Apps into Defender for Cloud’s Serverless Containers Posture experience.  
  - This integration enables unified security posture management for both serverless containers and other containerized workloads from a single workflow.  
  - Provides visibility into security configurations, compliance, and recommendations for Azure Container Apps environments.

- **Target audience affected**  
  - Security teams  
  - IT professionals managing containerized workloads  
  - Developers deploying applications with Azure Container Apps  
  - Organizations leveraging Microsoft Defender for Cloud for security posture management

- **Important notes if any**  
  - This feature is currently in Public Preview; functionality and coverage may change before General Availability.  
  - Extending Defender for Cloud’s posture management to Azure Container Apps helps organizations maintain consistent security and compliance across their container estate, including serverless scenarios.  
  - Review the official documentation for onboarding steps and current limitations.

[Learn more](https://azure.microsoft.com/updates?id=562569)

**Details**:

**Azure Update Technical Summary**

**Title:** Public Preview: Microsoft Defender for Cloud support for Azure Container Apps (Serverless Containers Posture)  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562569)

---

**Background and Purpose of the Update:**  
This update introduces public preview support for Azure Container Apps environments within Microsoft Defender for Cloud’s Serverless Containers Posture experience. The primary goal is to enable security teams to extend their security posture management capabilities to include Azure Container Apps, thereby providing unified visibility and control over a broader range of containerized workloads from a single workflow.

---

**Specific Features and Detailed Changes:**  
- **Integration of Azure Container Apps:** Customers can now onboard Azure Container Apps environments into Microsoft Defender for Cloud.
- **Serverless Containers Posture Management:** The update adds posture management capabilities specifically tailored for serverless container workloads, which were previously not covered in the same workflow as other container services.
- **Centralized Security Workflow:** Security teams can manage the security posture of both traditional container services and serverless container environments (Azure Container Apps) from a unified interface within Microsoft Defender for Cloud.

---

**Technical Mechanisms and Implementation Methods:**  
- **Onboarding Process:** Azure Container Apps environments can be registered with Microsoft Defender for Cloud, allowing the service to assess and monitor their security posture.
- **Posture Assessment:** Defender for Cloud evaluates the configuration and deployment of Azure Container Apps, identifying potential security risks and compliance issues in alignment with best practices for serverless containers.
- **Workflow Integration:** The update leverages existing Defender for Cloud workflows, enabling seamless extension of posture management to Azure Container Apps without requiring separate tools or processes.

---

**Use Cases and Application Scenarios:**  
- **Unified Security Management:** Organizations running both orchestrated containers (e.g., AKS) and serverless containers (Azure Container Apps) can now manage their security posture from a single pane of glass.
- **Compliance Monitoring:** Enterprises with regulatory requirements can include Azure Container Apps in their compliance assessments and reporting, ensuring consistent security standards across all containerized workloads.
- **Risk Mitigation:** Security teams can proactively identify and remediate misconfigurations or vulnerabilities in serverless container environments, reducing the attack surface.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** The feature is currently in public preview, which may entail limited support, potential changes before general availability, and possible feature gaps.
- **Scope:** The update specifically targets Azure Container Apps and does not extend to other serverless or container services unless explicitly stated.
- **Workflow Dependencies:** Full functionality may depend on proper configuration and integration with Microsoft Defender for Cloud and the correct onboarding of Azure Container Apps environments.

---

**Integration with Related Azure Services:**  
- **Microsoft Defender for Cloud:** This update enhances Defender for Cloud’s capabilities, allowing it to cover a wider range of Azure-native container services.
- **Azure Container Apps:** Direct integration enables posture management for serverless containerized applications, aligning with existing Azure security and compliance workflows.
- **Broader Azure Ecosystem:** By centralizing security posture management, organizations can streamline their security operations across multiple Azure services, improving efficiency and consistency.

---

**Summary Sentence:**  
The public preview of Microsoft Defender for Cloud support for Azure Container Apps enables security teams to extend serverless containers posture management to Azure Container Apps environments, providing unified and centralized security posture visibility and control within the existing Defender for Cloud workflow.

---

### 119. Generally Available: Confidential Compute support on Azure Container Apps

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Confidential Compute support on Azure Container Apps](https://azure.microsoft.com/updates?id=562564)

**Update ID**: 562564
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features

**Summary**:

- What was updated  
Confidential Compute support is now generally available on Azure Container Apps.

- Key changes or new features  
Azure Container Apps now allows customers to run containerized workloads on confidential computing hardware. This provides enhanced data protection by encrypting data in use, not just at rest or in transit. Workloads can now run in isolated, hardware-based Trusted Execution Environments (TEEs), helping meet strict compliance and regulatory requirements. Developers can deploy sensitive applications without major code changes, leveraging confidential containers for increased security.

- Target audience affected  
This update is relevant for developers and IT professionals running regulated, sensitive, or multi-tenant containerized workloads on Azure. It is particularly important for organizations in industries with high compliance needs, such as finance, healthcare, and government.

- Important notes if any  
To use Confidential Compute, select supported SKUs (e.g., DCsv3, DCesv5) when deploying Azure Container Apps. Some limitations may apply regarding supported features and regions. Review documentation for best practices and integration guidance. This feature helps organizations achieve higher data privacy and compliance standards with minimal changes to their existing containerized applications.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=562564

**Details**:

**Comprehensive Technical Explanation: Azure Update – Confidential Compute Support on Azure Container Apps (Generally Available)**

**Background and Purpose of the Update**  
The update addresses the need for enhanced data protection for customers running regulated or sensitive containerized workloads on Azure. Many organizations, especially those in highly regulated industries, require robust security measures to protect data not only at rest and in transit but also during active processing. This is particularly important for scenarios demanding higher isolation and stricter compliance controls. The introduction of Confidential Compute support to Azure Container Apps is designed to meet these requirements by providing stronger guarantees for data confidentiality during runtime.

**Specific Features and Detailed Changes**  
With this update, Azure Container Apps now offer Confidential Compute capabilities. This means containerized workloads can be executed within trusted execution environments (TEEs), ensuring that data remains protected while being processed. The feature is generally available, indicating production readiness and full support. The update specifically enables customers to deploy container apps that leverage confidential computing, thereby extending the security model of Azure Container Apps to include runtime data protection.

**Technical Mechanisms and Implementation Methods**  
Confidential Compute on Azure Container Apps utilizes hardware-based TEEs, such as Intel SGX or AMD SEV, to isolate workloads and encrypt memory during execution. This ensures that data processed within the container is inaccessible to unauthorized entities, including the underlying cloud provider and other tenants. The implementation involves provisioning container apps on confidential nodes, which are equipped with the necessary hardware and software to support confidential computing. Developers and IT professionals can specify confidential compute requirements when deploying container apps, ensuring that workloads are scheduled on appropriate infrastructure.

**Use Cases and Application Scenarios**  
Typical application scenarios include:
- Financial services processing sensitive transactions and customer data.
- Healthcare organizations handling patient records and medical data.
- Government agencies running workloads with strict compliance and isolation requirements.
- Any enterprise needing to meet regulatory standards such as GDPR, HIPAA, or PCI-DSS for data protection during processing.
- Workloads requiring secure multi-party computation or protection against insider threats.

**Important Considerations and Limitations**  
When utilizing Confidential Compute on Azure Container Apps, IT professionals should be aware of potential limitations such as:
- Performance overhead due to encryption and isolation mechanisms.
- Compatibility constraints, as not all container images or workloads may be suitable for execution within TEEs.
- Additional configuration steps required to enable confidential computing, including specifying confidential nodes and ensuring proper attestation.
- Compliance with Azure’s supported confidential hardware and runtime environments.
- Possible restrictions on integrations or features that are not yet supported in confidential environments.

**Integration with Related Azure Services**  
Confidential Compute support in Azure Container Apps can be integrated with other Azure security and compliance services, such as Azure Key Vault for secure key management, Azure Policy for governance, and Azure Monitor for auditing and monitoring confidential workloads. It complements existing Azure Confidential Computing offerings, allowing organizations to build end-to-end secure solutions across virtual machines, Kubernetes, and now container apps.

**Summary Sentence**  
Azure Container Apps now generally support Confidential Compute, enabling IT professionals to securely run sensitive containerized workloads with enhanced runtime data protection, higher isolation, and compliance controls using trusted execution environments.

---

### 120. Generally Available: Monitor HTTP traffic in Azure Container Apps 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Monitor HTTP traffic in Azure Container Apps ](https://azure.microsoft.com/updates?id=562559)

**Update ID**: 562559
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features

**Summary**:

- What was updated  
Azure Container Apps now provides a dedicated diagnostic setting category, ContainerAppHTTPLogs, for monitoring HTTP traffic.

- Key changes or new features  
A new Azure Monitor diagnostic setting, ContainerAppHTTPLogs, is generally available. This feature exposes detailed HTTP access logs for all incoming traffic to Azure Container Apps. The logs are optimized for high-volume request scenarios, enabling granular monitoring and analysis of HTTP requests. This is in addition to existing platform-level logs.

- Target audience affected  
Developers and IT professionals managing applications deployed on Azure Container Apps, especially those responsible for application monitoring, diagnostics, and security.

- Important notes if any  
The new HTTP access logs can be enabled via Azure Monitor diagnostic settings. These logs provide valuable data for troubleshooting, performance monitoring, and security auditing. Integration with Azure Monitor allows for further analysis, alerting, and export to other monitoring tools or SIEM solutions. This update helps teams meet compliance and observability requirements for applications handling significant HTTP traffic.

For more information, see the official update: https://azure.microsoft.com/updates?id=562559

**Details**:

**Comprehensive Technical Explanation: Azure Container Apps – Monitor HTTP Traffic (General Availability)**

**Background and Purpose of the Update:**  
Azure Container Apps previously provided platform-level logs, offering basic insights into containerized workloads. However, there was a growing need for more granular visibility into HTTP traffic, especially for applications handling high request volumes. This update introduces a dedicated diagnostic log category—**ContainerAppHTTPLogs**—to address the demand for detailed HTTP access logging, enabling IT professionals to monitor, analyze, and troubleshoot HTTP traffic more effectively.

**Specific Features and Detailed Changes:**  
- **New Diagnostic Setting Category:** The update adds **ContainerAppHTTPLogs** as a dedicated diagnostic setting in Azure Monitor for Azure Container Apps.
- **Detailed HTTP Access Logs:** This category exposes comprehensive HTTP access logs for all incoming traffic to container apps, capturing request and response metadata.
- **High-Volume Data Support:** The logging mechanism is designed to efficiently handle and expose high-volume HTTP request data, ensuring scalability for production workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Azure Monitor Integration:** The new log category is integrated via Azure Monitor’s diagnostic settings. Users can enable **ContainerAppHTTPLogs** through the Azure Portal, ARM templates, or CLI.
- **Log Delivery Destinations:** Once enabled, logs can be routed to supported destinations such as Log Analytics workspaces, Azure Storage accounts, or Event Hubs for further analysis, retention, or downstream processing.
- **Log Schema:** The logs typically include fields such as timestamp, HTTP method, URL, response status code, latency, client IP, and user agent, though the exact schema should be confirmed in the official documentation.

**Use Cases and Application Scenarios:**  
- **Security Monitoring:** Track and audit incoming HTTP requests for suspicious patterns or unauthorized access attempts.
- **Performance Analysis:** Analyze request rates, response times, and error codes to identify performance bottlenecks or degraded endpoints.
- **Troubleshooting and Debugging:** Correlate HTTP access logs with application logs to diagnose issues, reproduce errors, and validate fixes.
- **Compliance and Auditing:** Maintain detailed records of HTTP traffic for regulatory compliance or internal audits.

**Important Considerations and Limitations:**  
- **Data Volume and Costs:** High-volume HTTP logging can generate significant log data, impacting storage costs and ingestion rates in Log Analytics or other destinations.
- **Retention Policies:** Ensure appropriate retention policies are configured to manage log lifecycle and comply with organizational data governance.
- **Performance Impact:** While designed for high-volume scenarios, excessive logging can introduce minimal overhead; monitor resource utilization accordingly.
- **Log Content:** Sensitive information may be present in HTTP logs (e.g., URLs, headers); implement proper access controls and data masking as needed.

**Integration with Related Azure Services:**  
- **Azure Monitor:** Centralized log management and querying via Log Analytics.
- **Azure Storage:** Long-term archival of HTTP access logs for compliance or offline analysis.
- **Event Hubs:** Real-time streaming of HTTP log data to SIEM solutions or custom analytics pipelines.
- **Azure Security Center and Sentinel:** Enhanced visibility for security monitoring and incident response through integration with security tools.

**Summary:**  
Azure Container Apps now provides a dedicated ContainerAppHTTPLogs diagnostic setting in Azure Monitor, enabling detailed, high-volume HTTP access logging for incoming traffic, which enhances monitoring, troubleshooting, and security analysis capabilities for containerized applications.

---

### 121. Generally Available: Additional support for OpenTelemetry destinations (New Relic, Dynatrace, Elastic) 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Additional support for OpenTelemetry destinations (New Relic, Dynatrace, Elastic) ](https://azure.microsoft.com/updates?id=562554)

**Update ID**: 562554
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features

**Summary**:

- What was updated  
Azure Container Apps has expanded its OpenTelemetry (OTel) integration, now offering additional support for third-party observability platforms.

- Key changes or new features  
Developers and IT professionals can now configure Azure Container Apps to export telemetry data directly to New Relic, Dynatrace, and Elastic endpoints. This enhancement allows for seamless integration with these popular monitoring and observability tools, enabling more flexible and comprehensive application monitoring.

- Target audience affected  
This update is relevant for developers, DevOps engineers, and IT professionals who use Azure Container Apps and require advanced monitoring and observability, especially those leveraging New Relic, Dynatrace, or Elastic as their preferred platforms.

- Important notes if any  
To take advantage of these new integrations, users must configure their Container Apps to specify the desired third-party OTel endpoint. This update streamlines the process of centralizing logs, metrics, and traces, reducing the need for custom exporters or additional middleware. For detailed configuration steps, refer to the official Azure documentation.

Link: https://azure.microsoft.com/updates?id=562554

**Details**:

**Azure Update Report: Expanded OpenTelemetry Destination Support in Azure Container Apps**

**Background and Purpose of the Update**  
Azure Container Apps is a managed service for hosting containerized applications and microservices. Observability is crucial for monitoring, troubleshooting, and optimizing these workloads. OpenTelemetry (OTel) is an open-source framework for collecting telemetry data (logs, metrics, traces) from cloud-native applications. Previously, Azure Container Apps supported OTel for certain destinations, but many organizations rely on third-party observability platforms for advanced monitoring and analytics. This update addresses the need for broader integration by adding support for additional OTel destinations: New Relic, Dynatrace, and Elastic.

**Specific Features and Detailed Changes**  
With this update, Azure Container Apps now allows users to configure OTel endpoints for New Relic, Dynatrace, and Elastic directly within their container app environments. This means that telemetry data generated by applications running in Azure Container Apps can be exported to these platforms for centralized monitoring and analysis. The update expands the list of supported OTel destinations, providing more flexibility in observability tooling and enabling organizations to leverage their existing investments in monitoring solutions.

**Technical Mechanisms and Implementation Methods**  
The integration leverages OpenTelemetry’s standard protocol for exporting telemetry data. Azure Container Apps provides configuration options to specify the endpoint URLs for New Relic, Dynatrace, and Elastic. When telemetry data is generated by the application or the platform, it is sent to the configured OTel endpoint using supported formats (such as OTLP over HTTP or gRPC). This process is managed by the Azure Container Apps runtime, which ensures that data is transmitted securely and reliably to the selected third-party platform. No custom instrumentation is required beyond standard OTel setup, streamlining the integration process.

**Use Cases and Application Scenarios**  
- Organizations running microservices in Azure Container Apps can now export telemetry data to New Relic, Dynatrace, or Elastic for enhanced monitoring, alerting, and analytics.
- Teams that already use these observability platforms can maintain consistent monitoring workflows across hybrid or multi-cloud environments.
- DevOps and SRE teams can leverage advanced features in third-party platforms, such as anomaly detection, distributed tracing, and custom dashboards, using data collected from Azure Container Apps.

**Important Considerations and Limitations**  
- Only the specified third-party platforms (New Relic, Dynatrace, Elastic) are supported as additional OTel destinations in this update.
- Proper endpoint configuration is required to ensure secure and successful data transmission.
- Users should verify compatibility of their OTel instrumentation and ensure their destination platforms are configured to accept incoming telemetry from Azure Container Apps.
- The update does not include custom logic or advanced filtering; telemetry is exported as collected by OTel.

**Integration with Related Azure Services**  
This update enhances the interoperability of Azure Container Apps with external observability platforms, complementing Azure Monitor and other native Azure telemetry solutions. It allows for hybrid monitoring strategies, where telemetry can be sent simultaneously to Azure Monitor and third-party platforms for comprehensive visibility.

**Summary Sentence**  
Azure Container Apps now generally supports exporting OpenTelemetry data to New Relic, Dynatrace, and Elastic, enabling seamless integration with popular third-party observability platforms for enhanced monitoring and analytics.

---

### 122. Generally Available: Override Scale Rules in Azure Functions on Azure Container Apps

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Override Scale Rules in Azure Functions on Azure Container Apps](https://azure.microsoft.com/updates?id=562511)

**Update ID**: 562511
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Functions running on Azure Container Apps now support overriding default platform-managed scaling rules.

- Key changes or new features  
A new property, allowScalingRuleOverride, has been introduced. This allows users to override the default scaling rules automatically generated by the platform (via KEDA) for Azure Functions. Developers and IT admins can now define custom scaling rules tailored to their workloads, instead of relying solely on the platform’s automatic translation of triggers to KEDA scale rules.

- Target audience affected  
Developers and IT professionals deploying and managing Azure Functions on Azure Container Apps, especially those with advanced scaling requirements or custom workload patterns.

- Important notes if any  
Custom scaling rules can improve performance and cost efficiency for specialized workloads, but require careful configuration to avoid unintended scaling behavior. This feature is now generally available, so it can be used in production environments. Review the documentation to ensure proper implementation and to understand the implications of overriding default scaling logic.

[Read more](https://azure.microsoft.com/updates?id=562511)

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Override Scale Rules in Azure Functions on Azure Container Apps

**Background and Purpose of the Update:**  
Azure Functions on Azure Container Apps has, until now, relied exclusively on platform-managed scaling. In this model, Azure automatically translates function triggers into KEDA (Kubernetes Event-driven Autoscaling) scale rules, abstracting scaling logic from the user. While this simplifies operations, it limits the ability of customers to fine-tune scaling behavior to meet specific workload requirements. The purpose of this update is to introduce greater flexibility and control by allowing users to override the default scaling rules.

**Specific Features and Detailed Changes:**  
This update introduces the `allowScalingRuleOverride` property for Azure Functions deployed on Azure Container Apps. When enabled, this property allows customers to override the platform-managed scaling rules with custom KEDA scale rules. This means users can now define their own scaling logic, rather than relying solely on the automatic translation of triggers by the platform.

**Technical Mechanisms and Implementation Methods:**  
- **Platform-Managed Scaling:** Traditionally, Azure Functions on Container Apps automatically generate KEDA scale rules based on the function triggers (e.g., HTTP, Queue, Event Hub). These rules are managed by the platform and are not directly configurable by the user.
- **Override Mechanism:** By setting the `allowScalingRuleOverride` property, users can bypass the default behavior and specify their own KEDA scale rules. This is typically done by providing custom scaling definitions in the Container Apps configuration, allowing for granular control over scaling thresholds, polling intervals, and other KEDA-specific parameters.
- **KEDA Integration:** KEDA is the underlying component responsible for event-driven autoscaling in Azure Container Apps. By exposing the ability to override scale rules, the update leverages KEDA’s extensibility, enabling advanced scenarios such as custom metrics, multiple triggers, or non-standard scaling logic.

**Use Cases and Application Scenarios:**  
- **Advanced Scaling Requirements:** Organizations with workloads that have unique scaling patterns (e.g., bursty traffic, long-running jobs, or custom event sources) can now tailor scaling behavior to optimize resource utilization and performance.
- **Cost Optimization:** By fine-tuning scaling rules, customers can avoid over-provisioning and reduce costs associated with unnecessary instance scaling.
- **Hybrid Event Sources:** Scenarios where functions are triggered by multiple or custom event sources can benefit from custom KEDA rules to coordinate scaling across different triggers.

**Important Considerations and Limitations:**  
- **Configuration Complexity:** Overriding platform-managed scaling introduces additional configuration complexity and requires a solid understanding of KEDA scale rules.
- **Responsibility Shift:** Customers are responsible for maintaining and validating their custom scaling logic, which may increase operational overhead.
- **Compatibility:** Only available for Azure Functions running on Azure Container Apps; not applicable to other hosting models.

**Integration with Related Azure Services:**  
- **Azure Container Apps:** The update is specific to Azure Functions hosted on Azure Container Apps, leveraging its native KEDA integration.
- **KEDA:** Users interact directly with KEDA’s scaling mechanisms, enabling advanced autoscaling scenarios.
- **Azure Functions:** The core serverless compute platform benefits from enhanced scaling flexibility when running in a containerized environment.

**Summary:**  
This update enables Azure Functions on Azure Container Apps to override platform-managed scaling by allowing custom KEDA scale rules through the `allowScalingRuleOverride` property, providing users with enhanced control and flexibility over autoscaling behavior.

---

### 123. Public Preview: Go language support on Azure Functions

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Go language support on Azure Functions](https://azure.microsoft.com/updates?id=562502)

**Update ID**: 562502
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Build

**Summary**:

- What was updated  
Azure Functions now supports Go as a first-class language in public preview.

- Key changes or new features  
Developers can now write serverless, event-driven applications in Go using the Azure Functions Go programming model and SDK. This includes integration with Azure Functions’ triggers and bindings, enabling Go developers to leverage the platform’s scaling and event-driven capabilities. The release provides native tooling and templates for Go, making it easier to build, test, and deploy Go-based functions.

- Target audience affected  
Go developers, cloud architects, and IT professionals who build or manage serverless applications on Azure Functions.

- Important notes if any  
This is a public preview release, so features may change before general availability. Developers should review documentation for current limitations and best practices. Integration with Azure Functions Core Tools and Visual Studio Code is available for local development and deployment. This update enables Go developers to use Azure Functions without relying on custom handlers or workarounds, streamlining the development experience.

Data source: Using API data  
More details: [Azure Update: Go language support on Azure Functions](https://azure.microsoft.com/updates?id=562502)

**Details**:

**Public Preview: Go Language Support on Azure Functions**

**Background and Purpose of the Update:**  
Azure Functions is a serverless compute service that enables developers to run event-driven code without managing infrastructure. Previously, Azure Functions supported several languages such as C#, JavaScript, Python, and Java. This update introduces Go as a first-class language option in public preview, addressing the growing demand from the developer community for native Go support. The purpose is to allow Go developers to leverage Azure Functions for building scalable, event-driven applications using their preferred language.

**Specific Features and Detailed Changes:**  
With this release, developers can now author Azure Functions using Go, utilizing the Azure Functions Go programming model and SDK. This integration enables Go as a supported language in the Azure Functions runtime, providing access to the same triggers, bindings, and event-driven capabilities available to other languages. The update includes:
- Native Go language support in the Azure Functions runtime (public preview).
- An official Azure Functions Go SDK for streamlined development.
- Compatibility with the Azure Functions programming model, including triggers (e.g., HTTP, Timer, Queue) and bindings.

**Technical Mechanisms and Implementation Methods:**  
The Go language support is implemented as a first-class citizen in the Azure Functions runtime. Developers write functions in Go, using the provided SDK to interact with Azure Functions features such as triggers and bindings. The Azure Functions runtime manages the execution environment, scaling, and event handling, abstracting infrastructure concerns from the developer. The SDK provides idiomatic Go interfaces for registering functions, handling events, and integrating with Azure services. Deployment and management workflows remain consistent with other supported languages, leveraging Azure CLI, Visual Studio Code extensions, or GitHub Actions.

**Use Cases and Application Scenarios:**  
Go support in Azure Functions is ideal for:
- Developers and teams with existing Go expertise who want to build serverless, event-driven applications.
- Implementing microservices, REST APIs, and automation scripts in Go.
- Processing events from Azure services (e.g., Storage, Event Grid, Service Bus) using Go functions.
- Building lightweight, high-performance serverless applications that benefit from Go’s concurrency and efficiency.

**Important Considerations and Limitations:**  
- This feature is currently in public preview; production workloads should be evaluated carefully.
- As a preview feature, some advanced capabilities or integrations may be limited or subject to change.
- Developers should consult the official documentation for up-to-date information on supported triggers, bindings, and SDK versions.
- Support for Go in Azure Functions may not yet be available in all Azure regions or hosting plans.

**Integration with Related Azure Services:**  
Go-based Azure Functions can integrate seamlessly with other Azure services through triggers and bindings. This includes:
- Event-driven triggers from Azure Storage, Event Grid, Service Bus, and HTTP endpoints.
- Output bindings to services such as Azure Cosmos DB, Storage, and others.
- Integration with Azure monitoring, logging, and deployment pipelines.
Developers can use the Azure Functions Go SDK to interact with these services in an idiomatic Go manner, ensuring consistency with other Azure Functions workflows.

**Summary:**  
Azure Functions now offers public preview support for Go, enabling developers to build event-driven serverless applications in Go using the official programming model and SDK, while benefiting from the scalability and integration capabilities of the Azure Functions platform.

---

### 124. Generally Available: Built-in Grafana dashboards for Azure Functions

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Built-in Grafana dashboards for Azure Functions](https://azure.microsoft.com/updates?id=562492)

**Update ID**: 562492
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Microsoft Build

**Summary**:

- What was updated  
Azure Functions now offers generally available built-in Grafana dashboards integrated directly within the Azure portal.

- Key changes or new features  
Developers and IT professionals can now access pre-configured Grafana dashboards for Azure Functions without needing to provision a separate Grafana instance or configure data sources. These dashboards provide a comprehensive, single-pane view of function app health, performance, and scaling metrics out-of-the-box.

- Target audience affected  
This update primarily benefits developers, DevOps engineers, and IT professionals responsible for monitoring and managing Azure Functions.

- Important notes if any  
No additional setup or infrastructure is required—users can immediately leverage these dashboards from the Azure portal. This enhancement simplifies monitoring workflows, reduces operational overhead, and accelerates troubleshooting and performance optimization for serverless applications.

For more details, see the official update: https://azure.microsoft.com/updates?id=562492

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Built-in Grafana dashboards for Azure Functions  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562492)

---

### Background and Purpose of the Update

Azure Functions is a serverless compute service that enables users to run event-driven code without managing infrastructure. Monitoring and observability are critical for maintaining the health, performance, and scalability of function apps. Traditionally, integrating advanced dashboards like Grafana required manual provisioning of Grafana instances and configuration of data sources. The purpose of this update is to streamline monitoring by providing built-in Grafana dashboards directly within the Azure portal, eliminating the need for manual setup and reducing operational overhead.

---

### Specific Features and Detailed Changes

- **Built-in Grafana Dashboards:** Azure Functions now includes pre-configured Grafana dashboards accessible from the Azure portal.
- **Zero-Setup Experience:** Users do not need to provision or manage a separate Grafana instance or configure data sources.
- **Unified Monitoring:** The dashboards offer a single pane of glass for visualizing the health, performance, and scaling metrics of function apps.
- **Direct Portal Integration:** All monitoring capabilities are embedded within the Azure portal, providing immediate access to visualization tools.

---

### Technical Mechanisms and Implementation Methods

- **Native Integration:** The Grafana dashboards are natively integrated with Azure Functions, leveraging Azure’s internal telemetry and monitoring infrastructure.
- **No External Provisioning:** There is no requirement to deploy or maintain a standalone Grafana server or configure connections to Azure Monitor or other data sources.
- **Automatic Data Source Configuration:** The necessary data sources for function app telemetry are automatically connected, ensuring that metrics and logs are immediately available in the dashboards.
- **Portal-Based Access:** Users can access these dashboards directly from the Azure portal interface, ensuring a seamless workflow for monitoring and troubleshooting.

---

### Use Cases and Application Scenarios

- **Operational Monitoring:** DevOps teams can monitor the real-time health and performance of their Azure Functions without additional setup.
- **Performance Analysis:** Developers can quickly identify bottlenecks, failures, or scaling issues using the built-in visualizations.
- **Incident Response:** During outages or performance incidents, teams can use the dashboards for rapid root cause analysis.
- **Cost and Resource Optimization:** The dashboards provide visibility into scaling behavior, helping teams optimize resource allocation and control costs.

---

### Important Considerations and Limitations

- **Scope:** The built-in dashboards are specific to Azure Functions and may not support custom metrics or logs beyond the standard telemetry provided by the service.
- **Customization:** Since these are built-in dashboards, customization options may be limited compared to a self-hosted Grafana instance.
- **Portal Dependency:** Access to the dashboards is through the Azure portal; external access or API-based integration is not indicated in this update.
- **No External Grafana Instance:** Users requiring advanced customizations or integration with other data sources may still need to provision their own Grafana environment.

---

### Integration with Related Azure Services

- **Azure Monitor:** The dashboards likely leverage telemetry collected by Azure Monitor, providing a consistent monitoring experience across Azure services.
- **Azure Portal:** Full integration with the Azure portal ensures a unified management and monitoring experience for Azure Functions alongside other Azure resources.
- **No Additional Services Required:** The update removes the need for external Grafana provisioning or third-party monitoring tools for standard function app metrics.

---

**Summary Sentence:**  
Azure Functions now offers generally available, built-in Grafana dashboards within the Azure portal, enabling users to monitor health, performance, and scaling metrics of their function apps with zero setup and no need to provision or configure external Grafana instances or data sources.

---

### 125. Public Preview: Copilot-assisted coding & agent skills to build, deploy, and run Azure Functions faster in VS Code, CLI, and azd

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Copilot-assisted coding & agent skills to build, deploy, and run Azure Functions faster in VS Code, CLI, and azd](https://azure.microsoft.com/updates?id=562487)

**Update ID**: 562487
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Build

**Summary**:

- What was updated  
Azure announced the public preview of Copilot-assisted coding and agent skills for building, deploying, and running Azure Functions faster in Visual Studio Code (VS Code), the Azure CLI, and the Azure Developer CLI (azd).

- Key changes or new features  
  - Integration of Copilot-powered AI assistance directly into VS Code, CLI, and azd for Azure Functions development.  
  - Enhanced AI agent skills tailored for Azure Functions, providing context-aware code generation, deployment, and troubleshooting guidance.  
  - Improved support for generating function triggers, bindings, and code scaffolding using natural language prompts.  
  - Streamlined workflows for building, deploying, and running serverless functions, reducing manual steps and errors.

- Target audience affected  
  - Developers building serverless applications with Azure Functions.  
  - IT professionals and DevOps engineers managing Azure Functions deployments and automation using CLI tools.

- Important notes if any  
  - This feature is currently in public preview and may be subject to changes before general availability.  
  - Developers can leverage these AI-powered capabilities to accelerate development and reduce errors, but should validate generated code for production use.  
  - Requires the latest versions of VS Code, Azure CLI, or azd, and may require enabling preview features or extensions.  
  - More details and onboarding instructions are available in the official Azure Update link.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Copilot-assisted coding & agent skills to build, deploy, and run Azure Functions faster in VS Code, CLI, and azd  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562487)

---

**Background and Purpose of the Update:**  
The update addresses the variability and inconsistency in the quality of AI-assisted coding for Azure Functions. Existing AI coding assistants differ in effectiveness due to their underlying models and the recency of their training data. This public preview aims to standardize and enhance the developer experience by providing improved AI-powered assistance specifically tailored for Azure Functions development, deployment, and execution.

**Specific Features and Detailed Changes:**  
- **Copilot-assisted Coding:** Integration of AI-powered coding assistance directly into development environments such as Visual Studio Code (VS Code), the Azure Command-Line Interface (CLI), and the Azure Developer CLI (azd).  
- **Agent Skills:** Introduction of specialized agent skills that streamline the process of building, deploying, and running Azure Functions. These skills are designed to accelerate common workflows and reduce manual effort.
- **Enhanced Tooling:** The update brings Copilot capabilities to VS Code, CLI, and azd, enabling developers to leverage AI suggestions and automation across multiple interfaces.

**Technical Mechanisms and Implementation Methods:**  
- **AI Integration:** Copilot is embedded within the supported tools, providing context-aware code suggestions and automation. The agent skills are implemented as extensions or modules within VS Code, CLI, and azd, allowing seamless interaction with Azure Functions workflows.
- **Workflow Automation:** The agent skills automate repetitive tasks such as scaffolding, deployment, and execution of Azure Functions, reducing the need for manual scripting and configuration.
- **Model Utilization:** The quality of assistance is improved by utilizing up-to-date models and training data, ensuring relevant and accurate guidance for Azure Functions development.

**Use Cases and Application Scenarios:**  
- **Rapid Prototyping:** Developers can quickly scaffold and build Azure Functions with AI-assisted code generation and workflow automation.
- **Continuous Deployment:** Integration with CLI and azd enables streamlined deployment pipelines, allowing for faster iteration and reduced errors.
- **Multi-Interface Support:** Teams working across VS Code, CLI, and azd benefit from consistent Copilot assistance, improving productivity regardless of preferred tooling.

**Important Considerations and Limitations:**  
- **Public Preview Status:** The features are in public preview, meaning they may be subject to change and could have limited support or stability.
- **Model Dependency:** The quality of AI assistance is dependent on the underlying Copilot model and its training data, which may not cover all edge cases or custom scenarios.
- **Tool Compatibility:** The update is specific to VS Code, CLI, and azd; other development environments may not be supported.

**Integration with Related Azure Services:**  
- **Azure Functions:** Direct integration with Azure Functions enables end-to-end development, deployment, and execution workflows.
- **Azure CLI and azd:** The update enhances the Azure CLI and Azure Developer CLI experience, providing AI-powered automation and guidance for Azure Functions operations.
- **VS Code Extensions:** The Copilot and agent skills are delivered as extensions or modules within VS Code, facilitating seamless integration with existing Azure development tools.

---

**Summary Sentence:**  
This public preview introduces Copilot-assisted coding and agent skills to streamline the development, deployment, and execution of Azure Functions in VS Code, CLI, and azd, providing developers with enhanced AI-powered guidance and automation for improved productivity and consistency.

---

### 126. Public Preview: Serverless agents runtime for Azure Functions

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Serverless agents runtime for Azure Functions](https://azure.microsoft.com/updates?id=562482)

**Update ID**: 562482
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Build

**Summary**:

- What was updated  
Azure Functions introduced a public preview of a serverless agents runtime, enabling developers to build AI agents as a first-class workload using a markdown-first programming model.

- Key changes or new features  
  - Developers can now author event-driven serverless agents in natural language (markdown), simplifying the creation of AI-driven workflows.  
  - The new runtime allows integration of AI agents directly within Azure Functions, leveraging serverless scalability and event-driven triggers.  
  - This model supports rapid prototyping and deployment of AI agents without managing infrastructure or complex codebases.

- Target audience affected  
  - Developers building AI-powered applications and workflows on Azure.  
  - IT professionals managing serverless architectures and event-driven solutions.  
  - Teams interested in leveraging natural language programming models for rapid AI agent development.

- Important notes if any  
  - This feature is currently in public preview and not recommended for production workloads.  
  - Documentation and SDKs may evolve; users should monitor updates for breaking changes.  
  - The markdown-first approach lowers the barrier for integrating AI agents but may require adaptation for advanced or highly customized scenarios.

Source: [Azure Update](https://azure.microsoft.com/updates?id=562482)

**Details**:

**Azure Update Report: Public Preview – Serverless Agents Runtime for Azure Functions**

**Background and Purpose of the Update:**  
This update introduces a public preview of the serverless agents runtime for Azure Functions, targeting the growing demand for AI-driven automation and event-driven workloads. The purpose is to enable developers to build AI agents as a primary workload within Azure Functions, leveraging a markdown-first programming model. This approach aims to simplify the process of creating, deploying, and managing AI agents in a serverless environment, reducing the barriers to entry for integrating AI capabilities into cloud-native applications.

**Specific Features and Detailed Changes:**  
- **AI Agents as First-Class Workloads:** Azure Functions now officially supports AI agents, allowing them to be authored and managed as core components within the serverless platform.
- **Markdown-First Programming Model:** Developers can define agent logic and workflows using markdown syntax, enabling natural language authoring. This lowers the complexity of writing traditional code and accelerates the development of event-driven AI agents.
- **Event-Driven Serverless Agents:** The runtime is designed for event-driven architectures, allowing agents to respond to various triggers and events natively within Azure Functions.

**Technical Mechanisms and Implementation Methods:**  
- **Serverless Runtime Integration:** The new runtime extends the existing Azure Functions infrastructure, providing a managed, scalable environment for executing agent logic without the need for explicit infrastructure management.
- **Markdown-Based Authoring:** By supporting markdown as the primary authoring format, the platform parses and interprets natural language instructions, converting them into executable workflows. This mechanism abstracts much of the underlying code complexity, enabling rapid prototyping and iteration.
- **Event Binding:** Serverless agents can be bound to Azure Functions triggers (such as HTTP requests, queue messages, or timer events), ensuring seamless integration with event sources.

**Use Cases and Application Scenarios:**  
- **Conversational AI and Chatbots:** Rapidly build and deploy conversational agents that can interact with users via various channels.
- **Automated Process Orchestration:** Implement agents that automate business processes by responding to events and integrating with other services.
- **AI-Driven Monitoring and Alerting:** Create agents that monitor data streams or system events and trigger automated responses or notifications.

**Important Considerations and Limitations:**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Stability, performance, and feature completeness may be subject to change.
- **Markdown Model Constraints:** While markdown-first authoring simplifies development, it may limit the complexity of logic that can be expressed compared to traditional programming languages.
- **Documentation and Support:** Users should consult the latest Azure documentation for guidance on supported features and best practices during the preview phase.

**Integration with Related Azure Services:**  
- **Azure Functions Ecosystem:** Serverless agents can leverage the full range of Azure Functions triggers and bindings, enabling integration with storage, messaging, and other Azure services.
- **AI and Cognitive Services:** Agents can be designed to interact with Azure AI services, such as Language Understanding or Computer Vision, to enhance their capabilities.
- **Event Grid and Logic Apps:** Serverless agents can participate in broader event-driven architectures by integrating with Azure Event Grid and orchestrating workflows via Logic Apps.

**Summary Sentence:**  
Azure Functions now offers a public preview of a serverless agents runtime, enabling developers to build event-driven AI agents using a markdown-first programming model, thereby simplifying agent authoring and integration within Azure’s serverless ecosystem.

---

### 127. Public Preview: Azure Functions now includes managed connectors to integrate with 1400+ of your favorite systems 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Functions now includes managed connectors to integrate with 1400+ of your favorite systems ](https://azure.microsoft.com/updates?id=562442)

**Update ID**: 562442
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Integration, Azure Functions, Logic Apps, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Functions now supports managed connectors (public preview), enabling integration with over 1,400 systems and services directly within Azure Functions.

- Key changes or new features  
  - Azure Functions can now use the same managed connectors available in Logic Apps and Power Platform.  
  - Developers can use these connectors as first-class triggers and actions within their serverless workflows.  
  - This update allows seamless integration with SaaS platforms, on-premises systems, and other cloud services (e.g., Microsoft 365, Salesforce, SAP, ServiceNow, etc.) without custom connector code.

- Target audience affected  
  - Developers building serverless applications with Azure Functions.  
  - IT professionals and integration specialists managing workflows and automation across multiple systems.  
  - Teams looking to simplify integration between Azure Functions and external services.

- Important notes if any  
  - This feature is currently in public preview; not recommended for production workloads yet.  
  - Managed connectors enable low-code/no-code integration patterns within Azure Functions, reducing development effort for common integration scenarios.  
  - Pricing and regional availability may differ from Logic Apps; review documentation for details.  
  - Existing Azure Functions can be enhanced with these connectors without major refactoring.

[Learn more](https://azure.microsoft.com/updates?id=562442)

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Azure Functions now includes managed connectors to integrate with 1400+ of your favorite systems  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=562442)

---

### Background and Purpose of the Update

Azure Functions is a serverless compute service that enables event-driven execution of code. Traditionally, integrating Azure Functions with external systems required custom code, bindings, or the use of Logic Apps for advanced connectivity. The purpose of this update is to streamline and enhance integration capabilities by natively including managed connectors—previously exclusive to Logic Apps and Power Platform—directly within Azure Functions. This update aims to simplify the development of integrated solutions by providing out-of-the-box connectivity to over 1,400 systems, reducing the need for custom integration logic.

---

### Specific Features and Detailed Changes

- **Managed Connectors Integration:** Azure Functions now supports the same set of 1,400+ managed connectors available in Logic Apps and Power Platform.
- **First-Class Triggers and Operations:** These connectors can be used as both triggers (to initiate function execution) and actions (to perform operations within a function).
- **Broader Ecosystem Access:** Developers can now build Azure Functions that interact seamlessly with a wide range of SaaS, on-premises, and cloud services, including Microsoft 365, Salesforce, SAP, and more.
- **Public Preview Availability:** The feature is currently in public preview, allowing early access for testing and feedback.

---

### Technical Mechanisms and Implementation Methods

- **Connector Abstraction Layer:** Managed connectors are integrated as first-class citizens within the Azure Functions runtime, allowing them to be configured as triggers or actions without custom code.
- **Declarative Bindings:** Developers can declaratively bind function parameters to connector inputs and outputs, leveraging the same connector configuration experience as Logic Apps.
- **Event-Driven Execution:** Functions can be triggered by events from any supported connector, enabling event-driven architectures that span multiple systems.
- **Security and Authentication:** Managed connectors handle authentication and secure connectivity, abstracting away the complexity of credential management.

---

### Use Cases and Application Scenarios

- **Automated Workflows:** Trigger Azure Functions from events in external systems (e.g., new email in Outlook, new record in Salesforce) and automate downstream processing.
- **Data Integration:** Seamlessly move and transform data between cloud services, databases, and on-premises systems using managed connectors.
- **Business Process Automation:** Orchestrate business processes that require integration with multiple SaaS platforms, such as order processing or ticketing systems.
- **Event-Driven Microservices:** Build microservices that react to events from a diverse set of sources without custom integration code.

---

### Important Considerations and Limitations

- **Preview Limitations:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes.
- **Connector Availability:** While over 1,400 connectors are supported, not all connectors may offer the same capabilities or performance as in Logic Apps.
- **Cost Implications:** Usage of managed connectors may incur additional charges, similar to their use in Logic Apps or Power Platform.
- **Security and Compliance:** Ensure compliance with organizational policies when connecting to external systems, especially when handling sensitive data.

---

### Integration with Related Azure Services

- **Logic Apps and Power Platform:** This update aligns Azure Functions with Logic Apps and Power Platform by providing a unified connector ecosystem, enabling consistent integration patterns across services.
- **Azure Event Grid and Service Bus:** Managed connectors can complement existing event-driven services, broadening the range of trigger sources and destinations.
- **Azure API Management:** Functions using managed connectors can be exposed as APIs and managed through Azure API Management for governance and monitoring.

---

**Summary:**  
Azure Functions now supports over 1,400 managed connectors as first-class triggers and actions, enabling seamless integration with a wide range of external systems and simplifying the

---

### 128. Generally Available: Azure Functions now supports hosting MCP Apps 

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Generally Available: Azure Functions now supports hosting MCP Apps ](https://azure.microsoft.com/updates?id=562099)

**Update ID**: 562099
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features, Microsoft Build, Services

**Summary**:

- What was updated  
Azure Functions now supports hosting Model Context Protocol (MCP) Apps, and this feature is generally available.

- Key changes or new features  
Developers can now host MCP servers directly within Azure Functions. This enables richer user experiences beyond plain text, such as visual data exploration, complex configuration, real-time status monitoring, and multi-step workflows. The integration allows for scalable, serverless hosting of MCP Apps, leveraging Azure Functions’ event-driven and pay-per-use model.

- Target audience affected  
This update is relevant for developers building MCP servers or applications, as well as IT professionals managing serverless infrastructure or integrating advanced user interaction features in Azure environments.

- Important notes if any  
Developers can now use Azure Functions to deliver interactive and dynamic MCP-based applications without managing dedicated infrastructure. This enhancement streamlines deployment and scaling, and supports richer client-server interactions. Existing MCP Apps can be migrated to Azure Functions to take advantage of these benefits. For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=562099

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Functions now supports hosting MCP Apps

**Background and Purpose of the Update:**  
Model Context Protocol (MCP) servers have traditionally returned plain text responses, which limited the ability to deliver advanced user experiences such as interactive data visualizations, complex configurations, real-time monitoring, and multi-step workflows. This update addresses the need for richer, more interactive application responses by enabling Azure Functions to host MCP Apps, thereby enhancing the capabilities of serverless applications.

**Specific Features and Detailed Changes:**  
With this update, Azure Functions can now natively host MCP Apps. This means that developers can deploy MCP-based applications directly within Azure Functions environments. The primary change is the integration of MCP App hosting capabilities into the Azure Functions runtime, allowing for seamless deployment and execution of MCP servers that produce richer, more interactive responses beyond plain text.

**Technical Mechanisms and Implementation Methods:**  
Azure Functions provides a serverless compute platform that automatically manages infrastructure, scaling, and execution. By supporting MCP Apps, Azure Functions now allows developers to upload and run MCP server code as part of their function app deployments. The runtime manages the lifecycle of MCP servers, handling HTTP triggers and routing requests to the appropriate MCP endpoints. This integration streamlines the deployment process, as developers can use familiar Azure Functions deployment pipelines (such as CI/CD with Azure DevOps or GitHub Actions) to publish MCP Apps.

**Use Cases and Application Scenarios:**  
- **Visual Data Exploration:** Developers can build MCP Apps that return interactive visualizations, enabling users to analyze data in real time.
- **Complex Configuration Interfaces:** MCP Apps can provide dynamic configuration UIs, allowing users to manage application settings through rich interfaces.
- **Real-Time Status Monitoring:** MCP Apps hosted on Azure Functions can deliver live status updates and dashboards, improving operational visibility.
- **Multi-Step Workflows:** Developers can implement guided, multi-step processes that require stateful interactions, enhancing user productivity.

**Important Considerations and Limitations:**  
- **Resource Constraints:** Azure Functions imposes execution time and resource limits depending on the hosting plan (Consumption, Premium, or Dedicated). MCP Apps must be designed to operate within these constraints.
- **Cold Start Latency:** On the Consumption plan, cold starts may introduce latency when MCP Apps are triggered infrequently.
- **Security and Compliance:** Developers must ensure that MCP Apps hosted on Azure Functions adhere to organizational security and compliance requirements, including authentication and data protection.
- **Supported Languages and Runtimes:** MCP App hosting is available for supported Azure Functions languages and runtimes; developers should verify compatibility before deployment.

**Integration with Related Azure Services:**  
- **Azure Logic Apps:** MCP Apps hosted on Azure Functions can be integrated into workflows for automation and orchestration.
- **Azure API Management:** Expose MCP endpoints through API Management for secure, scalable API access.
- **Azure Monitor and Application Insights:** Leverage built-in monitoring and logging to track MCP App performance and diagnose issues.
- **Azure DevOps/GitHub Actions:** Use CI/CD pipelines to automate the deployment of MCP Apps to Azure Functions.

**Summary:**  
Azure Functions now generally supports hosting MCP Apps, enabling developers to deliver richer, interactive application experiences through serverless deployments, with integration into the broader Azure ecosystem for monitoring, automation, and API management.

---

### 129. Public Preview: Azure Container Apps Sandboxes

**Published**: June 02, 2026 19:00:47 UTC
**Link**: [Public Preview: Azure Container Apps Sandboxes](https://azure.microsoft.com/updates?id=561262)

**Update ID**: 561262
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Container Apps Sandboxes has been released in Public Preview.

- Key changes or new features  
Azure Container Apps Sandboxes provides a secure, isolated environment for running untrusted code within Azure Container Apps. It enables developers to safely execute code from various sources, preserve state across sessions, and scale to handle bursty workloads. Sandboxes are designed to simplify scenarios like agentic applications, multi-tenant platforms, development environments, and CI/CD systems, reducing the need for custom infrastructure to manage security and isolation.

- Target audience affected  
Developers and IT professionals building applications that require secure code execution, isolation for multi-tenancy, or support for dynamic and bursty workloads. This includes teams working on SaaS platforms, internal development tools, agent-based systems, and CI/CD pipelines.

- Important notes if any  
This is a Public Preview feature; it may not be suitable for production workloads yet. Users should review documentation for limitations and best practices. Integration with Azure Container Apps means existing workflows can leverage Sandboxes with minimal changes. Security and isolation are managed by Azure, reducing operational overhead for teams handling untrusted or third-party code.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=561262)

**Details**:

**Azure Update Report: Public Preview – Azure Container Apps Sandboxes**

**Background and Purpose of the Update**  
The introduction of Azure Container Apps Sandboxes addresses a common challenge faced by teams building agentic applications, multi-tenant platforms, development environments, and CI/CD systems: the need to safely execute untrusted code, maintain state across sessions, and efficiently manage bursty workloads. Traditionally, organizations have had to develop custom infrastructure solutions to securely run such workloads, which increases complexity and operational overhead. This update aims to provide a managed, secure, and scalable environment for these scenarios, reducing the need for bespoke solutions.

**Specific Features and Detailed Changes**  
Azure Container Apps Sandboxes introduces a new managed capability within Azure Container Apps that allows users to run untrusted code in isolated environments. Key features include:

- **Isolated Execution Environments:** Each sandbox provides strong isolation boundaries, ensuring that untrusted code cannot affect other workloads or compromise the host environment.
- **State Preservation:** Sandboxes are designed to preserve state across sessions, enabling scenarios where continuity is required between executions.
- **On-Demand Scalability:** The platform is optimized to handle bursty demand, automatically provisioning and de-provisioning sandboxes as needed to meet workload requirements.
- **Managed Service:** As a fully managed Azure service, operational complexity is reduced, and users can focus on application logic rather than infrastructure management.

**Technical Mechanisms and Implementation Methods**  
Azure Container Apps Sandboxes leverages containerization and Azure’s orchestration capabilities to provide secure, ephemeral environments for code execution. Each sandbox is provisioned as a containerized instance with enforced isolation at the process and network level. Azure manages the lifecycle of these sandboxes, including creation, scaling, and teardown, according to workload demand. State preservation is likely implemented through persistent storage mechanisms attached to each sandbox, ensuring data continuity between sessions.

**Use Cases and Application Scenarios**  
This feature is particularly relevant for:

- **Agentic Applications:** Applications that need to execute user-provided or third-party code in a secure manner.
- **Multi-Tenant Platforms:** SaaS or PaaS solutions requiring tenant isolation for custom code execution.
- **Development Environments:** Cloud-based IDEs or code runners that need to provide isolated, stateful environments for each user or session.
- **CI/CD Systems:** Build and test pipelines that must safely execute arbitrary code as part of the automation process.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not be suitable for production workloads. Users should be aware of potential limitations in terms of scalability, feature completeness, and support. Security boundaries are enforced, but users should review the documentation for any constraints or best practices related to sandboxed code execution, state management, and resource quotas.

**Integration with Related Azure Services**  
Azure Container Apps Sandboxes integrates seamlessly with the broader Azure Container Apps ecosystem, allowing users to leverage existing deployment, monitoring, and scaling capabilities. It can be used alongside Azure DevOps for CI/CD scenarios, Azure Storage for state persistence, and other Azure services as required by the application architecture.

**Summary Sentence**  
Azure Container Apps Sandboxes (public preview) provides a managed, scalable, and secure environment for running untrusted code with state preservation and burst handling, streamlining the development of agentic applications, multi-tenant platforms, development environments, and CI/CD systems without the need for custom infrastructure.

---

### 130. Public Preview: Snapshot backup for SQL Server in Azure VMs

**Published**: June 02, 2026 15:15:36 UTC
**Link**: [Public Preview: Snapshot backup for SQL Server in Azure VMs](https://azure.microsoft.com/updates?id=564668)

**Update ID**: 564668
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Storage, Azure Backup, Features, Compliance, Management, Security, Services

**Summary**:

- What was updated  
Azure Backup now offers snapshot-based backup for SQL Server running on Azure Virtual Machines (VMs) in Public Preview.

- Key changes or new features  
  - Supports near-instant, low-impact full backups using Azure disk snapshots, significantly reducing backup windows for large SQL databases.  
  - Integrates with native SQL transaction log backups to ensure point-in-time recovery.  
  - Enables faster and more efficient backup and restore operations, especially for large or mission-critical SQL Server workloads.  
  - Reduces performance impact on production workloads during backup operations.

- Target audience affected  
  - SQL Server database administrators (DBAs) managing SQL Server on Azure VMs  
  - IT professionals responsible for backup and disaster recovery  
  - Developers and DevOps teams running large-scale or high-availability SQL workloads in Azure

- Important notes if any  
  - This feature is currently in Public Preview and may not be suitable for production workloads requiring full support.  
  - Existing Azure Backup policies can be leveraged, but review documentation for any new configuration steps or limitations.  
  - For more details and prerequisites, refer to the official [Azure Update announcement](https://azure.microsoft.com/updates?id=564668).

**Details**:

**Azure Update Report: Public Preview – Snapshot Backup for SQL Server in Azure VMs**

**Background and Purpose of the Update:**  
Azure Backup has introduced support for snapshot-based backup of SQL Server instances running on Azure Virtual Machines (VMs). Traditionally, backing up large SQL Server databases can be time-consuming and resource-intensive, especially when using only native SQL backup mechanisms. The purpose of this update is to provide a faster, more efficient backup solution by leveraging Azure disk snapshots, thereby minimizing backup windows and reducing the impact on production workloads.

**Specific Features and Detailed Changes:**  
- **Snapshot-Based Full Backups:** The new feature enables near-instant full backups of SQL Server databases by taking Azure disk snapshots, significantly reducing the time required compared to traditional streaming backups.
- **Native SQL Transaction Log Backups:** Alongside disk snapshots, Azure Backup continues to capture native SQL transaction log backups, ensuring point-in-time recovery capabilities.
- **Low-Impact Operations:** By offloading the full backup process to disk snapshots, the impact on SQL Server performance during backup operations is minimized, which is particularly beneficial for large databases.

**Technical Mechanisms and Implementation Methods:**  
- **Azure Disk Snapshots:** During a backup operation, Azure Backup orchestrates the creation of a consistent disk snapshot of the underlying managed disks attached to the SQL Server VM. This snapshot captures the entire state of the disk at a specific point in time.
- **SQL Transaction Log Integration:** After the snapshot is taken, Azure Backup coordinates the backup of SQL transaction logs using native SQL Server mechanisms. This ensures that all changes since the last backup are captured, supporting granular recovery.
- **Backup Management:** The process is managed through Azure Backup, which handles scheduling, retention, and recovery workflows, integrating snapshot and log backups into a unified backup set.

**Use Cases and Application Scenarios:**  
- **Large SQL Server Databases:** Organizations running large SQL Server databases on Azure VMs can benefit from reduced backup windows and lower performance impact.
- **Mission-Critical Applications:** Environments requiring frequent backups and minimal downtime, such as financial or e-commerce systems, can leverage this feature to enhance data protection without disrupting operations.
- **Point-in-Time Recovery:** Workloads that demand granular recovery options can utilize the combination of snapshot and transaction log backups for robust restore capabilities.

**Important Considerations and Limitations:**  
- **Public Preview Status:** The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- **Backup Consistency:** The snapshot mechanism is designed to ensure consistency, but users should validate compatibility with their specific SQL Server workloads and configurations.
- **Resource Requirements:** Utilizing disk snapshots may have implications for storage costs and snapshot retention policies, which should be planned accordingly.

**Integration with Related Azure Services:**  
- **Azure Backup:** The snapshot backup capability is fully integrated with Azure Backup, allowing centralized management of backup policies, monitoring, and restores.
- **Azure Virtual Machines and Managed Disks:** The feature leverages Azure’s VM and managed disk infrastructure, ensuring compatibility with existing VM deployments running SQL Server.
- **Azure Portal and Automation:** Backup operations, including scheduling and restores, can be managed via the Azure Portal or automated using Azure PowerShell and CLI tools.

**Summary Sentence:**  
Azure Backup now offers public preview support for snapshot-based backup of SQL Server on Azure VMs, combining Azure disk snapshots with native SQL transaction log backups to deliver fast, low-impact full backups and point-in-time recovery, enhancing data protection for large and mission-critical SQL Server workloads.

---

### 131. Retirement: Azure VMware Solution AV36 node End of Support on September 30, 2027

**Published**: June 02, 2026 13:00:06 UTC
**Link**: [Retirement: Azure VMware Solution AV36 node End of Support on September 30, 2027](https://azure.microsoft.com/updates?id=564735)

**Update ID**: 564735
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the Azure VMware Solution (AVS) AV36 node. Support for this node will end on September 30, 2027, in line with Broadcom’s end of support for the current AV36 VMware Cloud Foundation (VCF) version.

- Key changes or new features  
The AV36 SKU will not be compatible with VMware Cloud Foundation (VCF) 9, the upcoming next-generation release. There are no new features for AV36; instead, customers must plan to migrate to supported SKUs that are compatible with future VCF versions.

- Target audience affected  
This update impacts IT professionals, infrastructure architects, and developers managing workloads on Azure VMware Solution using AV36 nodes.

- Important notes if any  
Customers running AV36 nodes must plan to migrate their workloads to supported node types before September 30, 2027, to maintain support and compatibility with future VCF releases. Failure to migrate may result in unsupported environments and potential security or compliance risks. Review your AVS deployments and coordinate with Microsoft or your solution provider to ensure a smooth transition.  
For more details, see the official [Azure Update notice](https://azure.microsoft.com/updates?id=564735).

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Azure VMware Solution AV36 node End of Support on September 30, 2027  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=564735)

---

**Background and Purpose of the Update**  
This update announces the scheduled retirement of support for the Azure VMware Solution (AVS) AV36 node SKU, aligning Microsoft’s support lifecycle with VMware’s evolving roadmap. Broadcom, the current owner of VMware, will end support for the AV36 VCF (VMware Cloud Foundation) version on September 30, 2027. The AV36 SKU is not compatible with VMware Cloud Foundation (VCF) 9, which is the next-generation platform from VMware. The purpose is to inform customers of the upcoming end-of-support date and to encourage planning for migration or upgrade to supported SKUs and VCF versions.

---

**Specific Features and Detailed Changes**  
- **AV36 Node SKU Retirement:** The AV36 node SKU, which is a specific hardware configuration for Azure VMware Solution, will no longer be supported after September 30, 2027.
- **VCF Version Compatibility:** The AV36 SKU does not support VMware Cloud Foundation 9. This means customers using AV36 nodes will not be able to upgrade to VCF 9, which is expected to be the next major release.
- **Support Lifecycle Alignment:** Microsoft is aligning its support lifecycle for AVS with VMware’s roadmap, ensuring that Azure customers are kept in sync with VMware’s official support timelines.

---

**Technical Mechanisms and Implementation Methods**  
- **Lifecycle Management:** Azure will enforce the retirement of AV36 nodes by ceasing support and maintenance for this SKU after the specified date.
- **Upgrade Path:** Customers will need to migrate workloads from AV36 nodes to newer, supported SKUs that are compatible with future VCF releases, including VCF 9.
- **Platform Compatibility:** The technical incompatibility between AV36 and VCF 9 is likely due to hardware or firmware requirements that are not met by the AV36 configuration.

---

**Use Cases and Application Scenarios**  
- **Current Deployments:** Organizations currently running production workloads on AV36 nodes in Azure VMware Solution must plan for migration before the end-of-support date.
- **Migration Planning:** IT teams should assess their inventory of AV36 nodes and develop strategies for moving workloads to newer node SKUs that will support VCF 9 and future releases.
- **Lifecycle Management:** This update is relevant for enterprises with long-term VMware infrastructure planning, ensuring compliance with support and security requirements.

---

**Important Considerations and Limitations**  
- **End-of-Support Date:** After September 30, 2027, AV36 nodes will not receive technical support, security updates, or maintenance from Microsoft or VMware.
- **Upgrade Limitation:** AV36 nodes cannot be upgraded to VCF 9, which may limit access to new features, performance improvements, and security enhancements available in future VCF releases.
- **Migration Requirement:** Customers must plan and execute migration to supported SKUs to avoid unsupported infrastructure and potential compliance risks.

---

**Integration with Related Azure Services**  
- **Azure VMware Solution (AVS):** The update directly affects AVS, which enables running VMware workloads natively on Azure infrastructure.
- **Azure Migration Tools:** Customers may leverage Azure migration tools and services to facilitate the transition from AV36 nodes to newer SKUs.
- **Azure Resource Management:** Integration with Azure’s resource management and monitoring services can help track node inventory and plan for lifecycle events.

---

**Summary Sentence**  
Microsoft has announced the retirement of Azure VMware Solution AV36 node support effective September 30, 2027, due to incompatibility with VMware Cloud Foundation 9, and customers are advised to plan migration to supported SKUs to maintain compliance and access to future VMware platform enhancements.

---


*This report was automatically generated - 2026-06-03 04:01:04 UTC*