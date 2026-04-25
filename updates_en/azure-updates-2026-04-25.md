# April 25, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 25, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Public Preview: Azure Backup for Elastic SAN 

**Published**: April 24, 2026 18:30:50 UTC
**Link**: [Public Preview: Azure Backup for Elastic SAN ](https://azure.microsoft.com/updates?id=560904)

**Update ID**: 560904
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Backup now supports Elastic SAN in public preview, enabling backup and restore capabilities for Elastic SAN volumes.

- Key changes or new features  
  - Fully managed backup and restore solution for Elastic SAN volumes.  
  - Protects data from accidental deletions, ransomware, and application updates.  
  - Allows exporting of Elastic SAN snapshots for recovery and compliance scenarios.  
  - Integration with Azure Backup provides centralized management, monitoring, and policy-driven automation.

- Target audience affected  
  - Developers and IT professionals managing storage infrastructure with Elastic SAN.  
  - Organizations requiring robust data protection, disaster recovery, and compliance for SAN-based workloads.

- Important notes if any  
  - This feature is currently in public preview; not recommended for production workloads yet.  
  - Review pricing, regional availability, and documentation before adoption.  
  - Existing Elastic SAN deployments can leverage this integration without major changes.

For more details, see the official update: https://azure.microsoft.com/updates?id=560904

**Details**:

**Azure Update Technical Explanation: Public Preview – Azure Backup for Elastic SAN**

**Background and Purpose of the Update:**  
Azure Backup now supports Elastic SAN, introducing a fully managed backup and restore capability for Elastic SAN volumes. The primary goal of this update is to enhance data protection for organizations using Azure Elastic SAN, safeguarding against risks such as accidental deletions, ransomware attacks, and issues arising from application updates. By integrating backup functionality directly with Elastic SAN, Azure provides a streamlined and robust solution for enterprise-grade data resilience.

**Specific Features and Detailed Changes:**  
- **Managed Backup and Restore:** Azure Backup can now natively back up and restore Elastic SAN volumes, eliminating the need for custom or third-party backup solutions.
- **Data Protection:** The solution is designed to protect against data loss scenarios, including accidental deletions, security incidents (e.g., ransomware), and unintended consequences of application changes.
- **Export Functionality:** The update enables the export of Elastic SAN volumes, facilitating recovery and data mobility as part of the backup process.

**Technical Mechanisms and Implementation Methods:**  
- **Service Integration:** The backup process is fully managed by Azure, leveraging the native integration between Azure Backup and Elastic SAN. This means that backup operations (such as scheduling, retention, and restoration) are handled through the Azure portal or APIs, consistent with other Azure Backup-supported resources.
- **Backup Storage:** Backups are stored separately from the source Elastic SAN volumes, ensuring that backup data remains isolated and protected from primary storage failures or compromises.
- **Restore Operations:** Restoration of Elastic SAN volumes is supported, allowing for point-in-time recovery to address data loss or corruption events.

**Use Cases and Application Scenarios:**  
- **Disaster Recovery:** Organizations can use this feature to quickly recover Elastic SAN volumes after accidental deletion or corruption.
- **Ransomware Protection:** In the event of a ransomware attack, protected volumes can be restored to a clean state, minimizing downtime and data loss.
- **Application Lifecycle Management:** During application updates or migrations, backup and restore capabilities provide a safety net to revert changes if necessary.

**Important Considerations and Limitations:**  
- **Public Preview:** This feature is currently in public preview, which means it may not be suitable for production workloads requiring full support or SLAs.
- **Scope of Protection:** The update specifically covers Elastic SAN volumes. Other SAN or storage types are not included unless otherwise specified.
- **Operational Limits:** As with any preview feature, there may be limitations on scale, supported regions, or integration depth. Users should consult the official documentation and preview terms before deployment.

**Integration with Related Azure Services:**  
- **Azure Backup:** The feature leverages the core capabilities of Azure Backup, including centralized management, policy-based protection, and monitoring.
- **Elastic SAN:** The integration is seamless, allowing users to manage backup and restore operations directly from the Elastic SAN resource context within the Azure portal.
- **Security and Compliance:** By using Azure Backup, organizations can align with Azure’s security and compliance standards for backup data.

**Summary:**  
Azure Backup for Elastic SAN (public preview) delivers a fully managed, integrated solution for backing up and restoring Elastic SAN volumes, enhancing data protection against deletion, ransomware, and application errors through native Azure service integration.

---

### 2. Public Preview: Hosted Agents in Foundry Agent Service 

**Published**: April 24, 2026 18:15:17 UTC
**Link**: [Public Preview: Hosted Agents in Foundry Agent Service ](https://azure.microsoft.com/updates?id=560997)

**Update ID**: 560997
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features

**Summary**:

- What was updated  
Azure Foundry Agent Service now offers Hosted Agents in Public Preview.

- Key changes or new features  
Hosted Agents provide an isolated execution sandbox for each agent session. Each session starts with a clean environment, ensuring no shared state or cross-session data leakage. Strong compute boundaries are enforced, enhancing security and session isolation. This setup enables secure, dedicated runtimes for automation and CI/CD workloads.

- Target audience affected  
Developers and IT professionals using Azure Foundry Agent Service for automation, CI/CD pipelines, or other agent-based workloads.

- Important notes if any  
Hosted Agents in Foundry Agent Service are currently in Public Preview. The isolation model improves security and reliability by preventing data leakage and ensuring clean environments for each session. This is particularly beneficial for organizations with strict security or compliance requirements. Review preview limitations and pricing before adoption.

Data source: [Azure Update](https://azure.microsoft.com/updates?id=560997)

**Details**:

**Azure Update Report: Public Preview – Hosted Agents in Foundry Agent Service**

**Background and Purpose of the Update**  
The introduction of Hosted Agents in the Foundry Agent Service addresses the need for secure, isolated execution environments within Azure. This update is designed to enhance security, reliability, and operational integrity by ensuring that each agent session operates independently, without risk of data leakage or interference from other sessions. The primary purpose is to provide a robust runtime for automation, orchestration, and integration tasks where isolation and session cleanliness are critical.

**Specific Features and Detailed Changes**  
- **Isolated Execution Sandbox:** Each hosted agent runs in a dedicated sandbox, ensuring that the runtime environment is exclusive to the session.  
- **Clean Session Initialization:** Sessions begin with a pristine environment, with no residual data or configuration from previous sessions.  
- **No Shared State:** There is strict separation between agent sessions, preventing any sharing of state or data.  
- **No Cross-Session Data Leakage:** The architecture eliminates the possibility of data leaking between sessions, supporting compliance and security requirements.  
- **Strong Compute Boundaries:** Each agent session is provisioned with strong compute isolation, ensuring performance consistency and preventing resource contention.

**Technical Mechanisms and Implementation Methods**  
The Hosted Agents leverage containerization or virtualization technologies to create isolated sandboxes for each session. Upon session start, a new sandbox is provisioned, ensuring that no artifacts or data from previous sessions persist. The agent runtime is instantiated within this sandbox, and all operations are confined to its boundaries. When the session ends, the sandbox is destroyed, guaranteeing that no session data remains. This approach enforces strict compute boundaries and eliminates cross-session contamination.

**Use Cases and Application Scenarios**  
- **CI/CD Pipelines:** Hosted Agents are ideal for build and deployment tasks where session isolation is required to prevent interference and ensure reproducibility.  
- **Automated Testing:** Test environments can be provisioned per session, ensuring that tests run in clean, controlled conditions.  
- **Data Processing Workloads:** Sensitive data processing tasks benefit from the secure, isolated runtime, reducing risk of data exposure.  
- **Integration and Orchestration:** Complex workflows involving multiple agents can be executed with confidence in session isolation and security.

**Important Considerations and Limitations**  
- **Session Isolation:** While isolation is guaranteed, users must ensure their workflows are compatible with stateless execution, as no data persists between sessions.  
- **Resource Allocation:** Compute boundaries are enforced, but users should monitor resource utilization to avoid exceeding quotas or limits.  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes or limitations.  
- **No Shared State:** Applications relying on shared state or persistent data across sessions will need to adapt their architecture.

**Integration with Related Azure Services**  
Hosted Agents in Foundry Agent Service can be integrated with Azure DevOps, Azure Pipelines, and other automation services that require agent-based execution. The isolated sandbox model complements Azure’s security and compliance offerings, and can be used alongside Azure Key Vault, Azure Storage, and other services for secure data handling and workflow orchestration.

**Summary Sentence**  
Hosted Agents in Foundry Agent Service provide secure, isolated execution sandboxes for agent sessions, ensuring clean environments, strong compute boundaries, and no cross-session data leakage, now available in public preview.

---

### 3. Generally Available: Foundry Toolkit for Visual Studio Code (formerly AI Toolkit for VS Code)

**Published**: April 24, 2026 18:15:17 UTC
**Link**: [Generally Available: Foundry Toolkit for Visual Studio Code (formerly AI Toolkit for VS Code)](https://azure.microsoft.com/updates?id=560987)

**Update ID**: 560987
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features

**Summary**:

- What was updated  
The Foundry Toolkit for Visual Studio Code (formerly known as AI Toolkit for VS Code) is now generally available.

- Key changes or new features  
  - Provides integrated VS Code tooling for the Microsoft Agent Framework.  
  - Enables agent creation using templates or GitHub Copilot.  
  - Supports local testing and debugging with visualization and trace capabilities.  
  - Allows direct deployment of agents to Foundry environments from within VS Code.

- Target audience affected  
Developers and IT professionals building, testing, and deploying AI agents using the Microsoft Agent Framework, especially those working in Visual Studio Code environments.

- Important notes  
  - The toolkit streamlines the end-to-end agent development workflow within VS Code, reducing context switching and improving productivity.  
  - Integration with GitHub Copilot accelerates agent creation through AI-assisted code generation.  
  - Local visualization and trace features help with debugging and monitoring agent behavior before deployment.  
  - Direct deployment to Foundry simplifies operationalization of agents.  
  - Existing users of the AI Toolkit for VS Code should note the rebranding to Foundry Toolkit.

For more details, see the official update: https://azure.microsoft.com/updates?id=560987

**Details**:

**Azure Update Report: Generally Available – Foundry Toolkit for Visual Studio Code (formerly AI Toolkit for VS Code)**  
[Reference: Azure Update](https://azure.microsoft.com/updates?id=560987)

---

**Background and Purpose of the Update:**  
The Foundry Toolkit for Visual Studio Code (VS Code), previously known as the AI Toolkit for VS Code, has reached general availability. This update aims to streamline the development lifecycle for solutions built using the Microsoft Agent Framework by providing integrated tooling within the popular VS Code environment. The toolkit is designed to enhance developer productivity by simplifying agent creation, testing, debugging, and deployment workflows directly from the editor.

---

**Specific Features and Detailed Changes:**  
- **Agent Creation:**  
  Developers can now create agents using pre-defined templates or leverage GitHub Copilot for code generation, accelerating the initial setup and reducing manual configuration.
- **Local Test/Debug with Visualization and Traces:**  
  The toolkit introduces capabilities for local testing and debugging of agents. It provides visualization tools and trace outputs, enabling developers to inspect agent behavior, monitor execution flows, and identify issues efficiently.
- **Direct Deployment to Foundry:**  
  The toolkit supports direct deployment of agents to Foundry environments from within VS Code, streamlining the transition from development to production.

---

**Technical Mechanisms and Implementation Methods:**  
- **VS Code Extension:**  
  The Foundry Toolkit is implemented as a VS Code extension, integrating seamlessly into the editor’s interface. It utilizes VS Code’s extension APIs to provide UI elements, command palette actions, and context menus for agent management.
- **Template-Based Scaffolding:**  
  Agent creation leverages template-based scaffolding, allowing developers to instantiate new projects with recommended structure and configuration.
- **Integration with GitHub Copilot:**  
  The toolkit can invoke GitHub Copilot to assist with code generation, offering AI-powered suggestions tailored to the agent framework.
- **Local Runtime and Debugger:**  
  For local testing and debugging, the toolkit likely interacts with a local runtime environment, capturing execution traces and rendering visualizations within VS Code panels.
- **Deployment Automation:**  
  Deployment features are integrated to connect to Foundry environments, automating packaging and publishing of agent artifacts directly from the development workspace.

---

**Use Cases and Application Scenarios:**  
- **Rapid Prototyping of Agents:**  
  Developers can quickly scaffold and iterate on agent-based solutions, leveraging templates and Copilot assistance.
- **Debugging and Visualization:**  
  Teams can locally test and debug agents, using visualization and trace outputs to troubleshoot logic and performance issues before deployment.
- **Continuous Integration and Deployment:**  
  The direct deployment capability supports streamlined CI/CD workflows, enabling faster release cycles for agent updates in Foundry environments.

---

**Important Considerations and Limitations:**  
- **Environment Compatibility:**  
  Ensure that the VS Code environment and any required dependencies are compatible with the Foundry Toolkit extension.
- **Foundry Access:**  
  Direct deployment requires appropriate permissions and access to target Foundry environments.
- **Feature Scope:**  
  The toolkit’s features are focused on the Microsoft Agent Framework and may not generalize to other frameworks or agent platforms.

---

**Integration with Related Azure Services:**  
While the update specifically targets the Microsoft Agent Framework and Foundry, it is designed to fit into broader Azure-based development workflows. Integration with GitHub Copilot leverages Azure’s AI ecosystem, and deployment to Foundry aligns with Azure’s managed agent hosting and orchestration capabilities.

---

**Summary Sentence:**  
The Foundry Toolkit for Visual Studio Code is now generally available, providing integrated agent creation, local testing/debugging with visualization, and direct deployment to Foundry, thereby streamlining the development and operational lifecycle for Microsoft Agent Framework solutions within VS Code.

---

### 4. Generally Available: WireGuard In‑Transit Encryption for Azure Kubernetes Service (AKS)

**Published**: April 24, 2026 18:15:17 UTC
**Link**: [Generally Available: WireGuard In‑Transit Encryption for Azure Kubernetes Service (AKS)](https://azure.microsoft.com/updates?id=560015)

**Update ID**: 560015
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features, Security

**Summary**:

- What was updated  
WireGuard in-transit encryption is now generally available for Azure Kubernetes Service (AKS) clusters using Azure CNI powered by Cilium and Advanced Container Networking Services (ACNS).

- Key changes or new features  
AKS clusters can now leverage WireGuard to provide transparent, node-level encryption for all pod-to-pod and pod-to-node traffic. This ensures that data in transit within the cluster is encrypted without requiring application changes. The feature is integrated with Azure CNI (Cilium) and ACNS, supporting enhanced security and compliance requirements.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those with strict security and compliance needs, such as in regulated industries. Platform engineers and DevOps teams responsible for cluster networking and security will benefit most.

- Important notes if any  
WireGuard encryption is implemented at the node level, requiring no modifications to application code. It is available for clusters using Azure CNI powered by Cilium and ACNS. Review cluster compatibility and prerequisites before enabling. This feature helps meet compliance standards for data protection in transit within AKS environments.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=560015

**Details**:

**Azure Update Report: Generally Available – WireGuard In‑Transit Encryption for Azure Kubernetes Service (AKS)**

**Background and Purpose of the Update**  
This update announces the general availability of WireGuard in-transit encryption for Azure Kubernetes Service (AKS) clusters that utilize Azure CNI powered by Cilium and Advanced Container Networking Services (ACNS). The primary purpose of this feature is to enhance the security posture of AKS environments by enabling transparent, node-level encryption for network traffic traversing between cluster nodes. This addresses the need for robust data protection within Kubernetes clusters, especially for organizations with strict compliance or security requirements.

**Specific Features and Detailed Changes**  
- **WireGuard Integration:** WireGuard, a modern and high-performance VPN protocol, is now natively supported for in-transit encryption within AKS clusters.
- **Node-Level Encryption:** Encryption is applied at the node level, ensuring that all traffic between nodes is automatically encrypted without requiring application-level changes.
- **Support Scope:** This feature is available for AKS clusters configured with Azure CNI (Container Networking Interface) powered by Cilium and ACNS, providing advanced networking capabilities.

**Technical Mechanisms and Implementation Methods**  
- **Transparent Encryption:** WireGuard operates at the networking layer, establishing secure tunnels between AKS nodes. This is implemented transparently, so workloads and applications do not need to be modified to benefit from encryption.
- **Integration with Azure CNI and Cilium:** The feature leverages the programmable networking capabilities of Cilium and the advanced features provided by ACNS, ensuring compatibility with Azure’s managed Kubernetes networking stack.
- **Operational Model:** Once enabled, WireGuard automatically manages key exchange and tunnel establishment between nodes, minimizing operational overhead.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in finance, healthcare, or government sectors can use this feature to meet compliance requirements for data-in-transit encryption within Kubernetes clusters.
- **Multi-Tenant Environments:** AKS clusters hosting workloads for multiple teams or customers benefit from enhanced traffic isolation and security.
- **Hybrid and Multi-Cloud Deployments:** When AKS clusters span multiple regions or integrate with on-premises environments, WireGuard ensures that all node-to-node traffic remains encrypted.

**Important Considerations and Limitations**  
- **Prerequisites:** This feature is only available for AKS clusters using Azure CNI powered by Cilium and ACNS. It is not available for clusters using other networking plugins or configurations.
- **Performance Impact:** While WireGuard is designed for high performance, enabling encryption may introduce minimal overhead. Performance testing is recommended for latency-sensitive workloads.
- **Scope of Encryption:** The encryption applies to node-to-node traffic within the AKS cluster. Traffic outside the cluster or to external endpoints is not covered by this feature.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** The feature is tightly integrated with AKS, leveraging its managed cluster lifecycle and networking configuration.
- **Azure CNI and Cilium:** WireGuard encryption is built on top of Azure CNI with Cilium, ensuring compatibility with advanced networking features such as network policies and observability.
- **Advanced Container Networking Services (ACNS):** ACNS provides the underlying infrastructure for enhanced networking and security capabilities, including this encryption feature.

**Summary Sentence:**  
WireGuard in-transit encryption is now generally available for AKS clusters using Azure CNI powered by Cilium and ACNS, providing transparent, node-level encryption for enhanced security of inter-node traffic.

---

### 5. Retirement: Support for .NET 8 (LTS) ends on November 10, 2026—upgrade your apps to .NET 10 (LTS) 

**Published**: April 24, 2026 17:45:05 UTC
**Link**: [Retirement: Support for .NET 8 (LTS) ends on November 10, 2026—upgrade your apps to .NET 10 (LTS) ](https://azure.microsoft.com/updates?id=558033)

**Update ID**: 558033
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of support for .NET 8 (Long-Term Support, LTS) on November 10, 2026, for applications hosted on Azure App Service.

- Key changes or new features  
After November 10, 2026, .NET 8 (LTS) will no longer receive security updates or customer support from Microsoft. Applications running on .NET 8 (LTS) will continue to function, but without ongoing maintenance or security patches. Developers and IT professionals are advised to upgrade their applications to .NET 10 (LTS) before the retirement date to ensure continued support and security.

- Target audience affected  
Developers and IT professionals managing applications on Azure App Service that are built with .NET 8 (LTS).

- Important notes if any  
Failure to upgrade to .NET 10 (LTS) before the end-of-support date may expose applications to security vulnerabilities and compliance risks, as no further security updates will be provided. Begin planning and testing your application upgrades to .NET 10 (LTS) as soon as possible to ensure a smooth transition and continued support.  
For more details, refer to the official update: https://azure.microsoft.com/updates?id=558033

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Support for .NET 8 (LTS) ends on November 10, 2026—upgrade your apps to .NET 10 (LTS)  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=558033)

---

**Background and Purpose of the Update:**  
Microsoft Azure App Service is announcing the end of support for .NET 8 (Long-Term Support, LTS) effective November 10, 2026. This update is part of Microsoft’s regular lifecycle management for .NET LTS releases, ensuring that customers benefit from the latest features, performance enhancements, and security improvements. The purpose of this update is to inform customers that after the specified date, .NET 8 (LTS) will no longer receive security updates or customer service, and to encourage migration to .NET 10 (LTS), which will be the next supported LTS version.

---

**Specific Features and Detailed Changes:**  
- **End of Support:** After November 10, 2026, .NET 8 (LTS) will not receive any further security patches, bug fixes, or technical support from Microsoft.
- **Continued Operation:** Applications hosted on Azure App Service using .NET 8 (LTS) will continue to run, but without ongoing support or updates.
- **Upgrade Path:** Customers are advised to upgrade their applications to .NET 10 (LTS) to maintain access to security updates and support.

---

**Technical Mechanisms and Implementation Methods:**  
- **Lifecycle Management:** Azure App Service manages .NET runtime versions according to Microsoft’s official support policy. When a runtime reaches end-of-support, Azure stops providing updates and customer service for that version.
- **Upgrade Process:** To upgrade, customers must modify their application codebase to be compatible with .NET 10 (LTS), update project files, and redeploy their applications to App Service using the new runtime version.
- **Runtime Selection:** Azure App Service allows users to select the desired .NET runtime version in their app configuration. After .NET 8 (LTS) retirement, .NET 10 (LTS) should be selected for continued support.

---

**Use Cases and Application Scenarios:**  
- **Enterprise Applications:** Organizations running mission-critical workloads on .NET 8 (LTS) in App Service must plan migration to .NET 10 (LTS) to ensure compliance and security.
- **DevOps Pipelines:** Automated deployment pipelines should be updated to target .NET 10 (LTS) after the retirement date.
- **ISVs and SaaS Providers:** Independent software vendors and SaaS providers using App Service for customer-facing applications must upgrade to maintain service reliability and support.

---

**Important Considerations and Limitations:**  
- **Security Risks:** Continuing to run applications on .NET 8 (LTS) after November 10, 2026 exposes them to potential security vulnerabilities due to lack of updates.
- **No Customer Service:** Microsoft will not provide technical support for issues related to .NET 8 (LTS) after the retirement date.
- **Compatibility Testing:** Before upgrading, thorough testing is required to ensure application compatibility with .NET 10 (LTS).

---

**Integration with Related Azure Services:**  
- **App Service:** The update directly affects applications hosted on Azure App Service using .NET 8 (LTS).
- **Azure DevOps:** Integration with Azure DevOps pipelines should be updated to build and deploy with .NET 10 (LTS).
- **Monitoring and Security:** Azure Monitor and Defender for Cloud should be configured to alert on unsupported runtime usage post-retirement.

---

**Summary Sentence:**  
Support for .NET 8 (LTS) on Azure App Service will end on November 10, 2026; to maintain security and support, upgrade your applications to .NET 10 (LTS) before this date

---

### 6. Generally Available: Cascading read replicas in Azure Database for PostgreSQL 

**Published**: April 24, 2026 16:45:30 UTC
**Link**: [Generally Available: Cascading read replicas in Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=560939)

**Update ID**: 560939
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Cascading read replicas are now generally available in Azure Database for PostgreSQL.

- Key changes or new features  
You can now create read replicas from existing read replicas (cascading replication), not just from the primary server. This enables up to 30 read replicas across two levels of replication. This feature allows for greater scalability and flexibility in distributing read workloads, improving performance for read-heavy applications.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL, especially those with high read throughput requirements or distributed application architectures.

- Important notes if any  
Cascading read replicas help reduce replication lag and network latency by allowing replicas to be created closer to application endpoints or in different regions. This feature is particularly useful for global applications and disaster recovery scenarios. Review Azure’s documentation for configuration guidance and best practices to ensure optimal performance and reliability.  
[Learn more](https://azure.microsoft.com/updates?id=560939)

**Details**:

**Azure Update Report: Cascading Read Replicas in Azure Database for PostgreSQL (General Availability)**

**Background and Purpose of the Update:**  
Azure Database for PostgreSQL now supports generally available cascading read replicas. This update addresses the need for greater scalability and flexibility in handling read-intensive workloads. Traditionally, read replicas were created only from the primary server, which could limit scalability and introduce bottlenecks in environments with high read demands. Cascading replication enables organizations to extend their replica topology, supporting larger and more distributed workloads.

**Specific Features and Detailed Changes:**  
- **Cascading Replication:** Users can now create read replicas not only from the primary PostgreSQL server but also from existing read replicas.
- **Replica Topology:** The system supports up to 30 read replicas, distributed across two levels of replication. This means a replica can itself serve as the source for additional replicas, forming a cascading hierarchy.
- **General Availability:** This feature is now fully supported and available for production workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Replication Process:** Cascading replication leverages PostgreSQL’s native streaming replication capabilities. In this model, a read replica can act as a replication source for other replicas, forwarding changes received from its upstream server.
- **Hierarchy Structure:** The two-level limit means that you can have a primary server, first-level replicas directly replicating from the primary, and second-level replicas replicating from first-level replicas. The total number of replicas across both levels can be up to 30.
- **Deployment:** Configuration is managed through the Azure portal, CLI, or ARM templates, allowing administrators to specify the source server for each replica.

**Use Cases and Application Scenarios:**  
- **Scaling Read Workloads:** Organizations with applications that require high read throughput—such as analytics, reporting, or content delivery—can distribute queries across multiple replicas, reducing load on the primary server.
- **Geographical Distribution:** Cascading replicas can be deployed in different regions, improving read latency for globally distributed users.
- **Disaster Recovery and High Availability:** Additional replicas can serve as failover targets in the event of regional outages or maintenance.

**Important Considerations and Limitations:**  
- **Replication Depth:** The cascading model supports only two levels of replication. Deeper hierarchies are not supported.
- **Consistency:** As with all asynchronous replication, there may be replication lag between the primary and replicas, and between replica levels.
- **Write Operations:** Read replicas remain read-only; all write operations must be directed to the primary server.
- **Management Overhead:** Administrators must monitor replication health and lag, especially in complex topologies.

**Integration with Related Azure Services:**  
- **Monitoring and Management:** Integration with Azure Monitor and Azure Portal allows for tracking replica status, performance, and replication lag.
- **Automation:** The Azure CLI and ARM templates can be used to automate the deployment and scaling of cascading replicas.
- **Security and Networking:** Cascading replicas inherit the security, networking, and compliance configurations of Azure Database for PostgreSQL, including VNet integration and role-based access control.

**Summary Sentence:**  
Cascading read replicas in Azure Database for PostgreSQL are now generally available, enabling up to 30 replicas across two replication levels for enhanced scalability and flexibility in read-intensive workloads.

---

### 7. Generally Available: CRC Protection 

**Published**: April 24, 2026 16:45:30 UTC
**Link**: [Generally Available: CRC Protection ](https://azure.microsoft.com/updates?id=560889)

**Update ID**: 560889
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Elastic SAN now supports CRC-32C checksum verification for data integrity.

- Key changes or new features  
CRC-32C checksum protection can be enabled on the client side for connections to Elastic SAN volumes. This feature can be activated during the creation of a new Elastic SAN or enabled on existing Elastic SAN resources. The checksum verification helps detect and prevent data corruption during data transfers.

- Target audience affected  
Developers and IT professionals managing storage solutions with Azure Elastic SAN, especially those with high data integrity requirements.

- Important notes if any  
CRC protection must be enabled on the client side; it is not active by default. Enabling CRC-32C may have a minor performance impact due to additional verification steps. Review your client configurations and storage workflows to ensure compatibility and optimal use of this feature. For more details, refer to the official Azure documentation.

**Details**:

**Azure Update Report: Generally Available – CRC Protection for Azure Elastic SAN**

**Background and Purpose of the Update**  
Azure Elastic SAN is a managed storage solution designed to provide scalable, high-performance block storage for cloud workloads. Data integrity is a critical requirement for enterprise storage, especially in environments where large volumes of data are transferred and stored. The introduction of CRC-32C checksum verification addresses the need for robust data integrity checks, ensuring that data corruption during transmission or storage can be detected and mitigated.

**Specific Features and Detailed Changes**  
With this update, Azure Elastic SAN now supports CRC-32C (Cyclic Redundancy Check) checksum verification. This feature can be enabled either during the creation of a new Elastic SAN or retroactively on existing Elastic SAN instances. The CRC protection is activated on the client side for connections to Elastic SAN volumes, allowing for end-to-end data integrity validation. This enhancement provides users with the option to enforce checksum validation, thereby reducing the risk of undetected data corruption.

**Technical Mechanisms and Implementation Methods**  
CRC-32C is a widely adopted checksum algorithm that computes a 32-bit hash value based on the contents of data blocks. When CRC protection is enabled, the client computes the CRC-32C checksum for each data block transmitted to or received from the Elastic SAN volume. Upon receipt, the Elastic SAN verifies the checksum against the data block. If a mismatch is detected, it indicates potential data corruption, prompting corrective actions such as retransmission or error logging. The implementation leverages client-side configuration, meaning that the checksum calculation and verification are handled by the client software interfacing with Elastic SAN.

**Use Cases and Application Scenarios**  
- **Enterprise Storage:** Organizations requiring high data integrity for mission-critical workloads, such as databases, analytics, and backup solutions, can benefit from CRC protection.
- **Regulatory Compliance:** Workloads subject to compliance standards (e.g., healthcare, finance) often mandate data integrity checks; CRC-32C provides a mechanism to meet these requirements.
- **Distributed Applications:** Applications that span multiple regions or rely on frequent data transfers can use CRC protection to ensure data consistency and reliability.
- **Backup and Restore Operations:** CRC verification helps detect silent data corruption during backup or restore processes, enhancing the reliability of disaster recovery solutions.

**Important Considerations and Limitations**  
- **Client-Side Enablement:** CRC protection must be enabled on the client side, requiring compatible client software or configuration changes.
- **Performance Impact:** While CRC-32C is efficient, checksum computation and verification may introduce additional CPU overhead on the client, potentially affecting performance in high-throughput scenarios.
- **Compatibility:** Existing Elastic SAN instances can be retrofitted with CRC protection, but users must ensure that their client applications support CRC-32C.
- **Scope:** The update applies specifically to connections to Elastic SAN volumes; it does not extend to other Azure storage services unless explicitly stated.

**Integration with Related Azure Services**  
Azure Elastic SAN can be integrated with Azure Virtual Machines, Azure Kubernetes Service, and other compute resources that require block storage. Enabling CRC protection enhances the reliability of these integrations by ensuring data integrity across the storage layer. It is important to verify that the client software used in these integrations supports CRC-32C when enabling this feature.

**Summary Sentence**  
Azure Elastic SAN now offers generally available CRC-32C checksum verification, enabling client-side data integrity protection for connections to Elastic SAN volumes, which can be activated during creation or on existing instances to enhance reliability and compliance for enterprise workloads.

---


*This report was automatically generated - 2026-04-25 03:03:17 UTC*