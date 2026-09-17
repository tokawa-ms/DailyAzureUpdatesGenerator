# September 17, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 17, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Retirement Update: SAP container images removed October 14, 2026

**Published**: September 16, 2026 17:19:02 UTC
**Link**: [Retirement Update: SAP container images removed October 14, 2026](https://azure.microsoft.com/updates?id=571342)

**Update ID**: 571342
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Retirement notice for the containerized SAP data connector in Azure Monitor. The connector was retired on September 14, 2026, and its container images will be removed from repositories on October 14, 2026.

- Key changes or new features  
The SAP data connector is no longer supported or maintained. After October 14, 2026, container images will no longer be available for download or deployment. Existing TLS-compliant agents may still send logs via the retired HTTP Data Collector API, but no updates or support will be provided.

- Target audience affected  
Developers and IT professionals managing SAP integrations with Azure Monitor, especially those deploying or maintaining the SAP data connector in containerized environments.

- Important notes if any  
- Migrate to supported alternatives before October 14, 2026, to avoid disruptions.
- After the retirement date, new deployments using the SAP data connector container images will not be possible, and existing deployments will not receive updates or support.
- Review your monitoring architecture and plan for migration to ensure continued log collection from SAP systems.

For more details, see the official update: https://azure.microsoft.com/updates?id=571342

**Details**:

**Azure Update Report: Retirement Update – SAP Container Images Removed October 14, 2026**

**Background and Purpose of the Update:**  
Microsoft Azure has announced the retirement of the containerized SAP data connector, which ceased support and maintenance as of September 14, 2026. The primary purpose of this update is to inform users that the associated SAP container images will be permanently removed from Azure repositories on October 14, 2026. This retirement is part of Azure’s lifecycle management strategy, ensuring that deprecated components are phased out to maintain platform security and reliability.

**Specific Features and Detailed Changes:**  
- The containerized SAP data connector is no longer supported or maintained after September 14, 2026.
- Container images related to this connector will be deleted from Azure repositories on October 14, 2026.
- Existing TLS-compliant agents may continue to send logs using the retired HTTP Data Collector API, but this API is no longer actively supported.

**Technical Mechanisms and Implementation Methods:**  
The SAP data connector was distributed as container images, enabling deployment in containerized environments. These images facilitated log collection from SAP systems and transmission to Azure services via the HTTP Data Collector API. After retirement, the container images will be removed, preventing new deployments or redeployments. However, agents already configured with TLS compliance can continue to send logs through the HTTP Data Collector API, though this pathway is unsupported and unmaintained.

**Use Cases and Application Scenarios:**  
Previously, the containerized SAP data connector was used in scenarios where organizations needed to collect and forward SAP logs to Azure for monitoring, analytics, or compliance purposes. Typical deployments included:
- Integrating SAP log data with Azure Monitor or Log Analytics.
- Using containerized agents for scalable log collection in hybrid or cloud environments.
- Supporting TLS-compliant log transmission for secure data handling.

With the retirement, these use cases are no longer supported for new deployments. Existing agents may continue to operate, but organizations should plan migration strategies to alternative solutions.

**Important Considerations and Limitations:**  
- After October 14, 2026, the container images will not be available for download or deployment.
- The HTTP Data Collector API, while still accessible for log transmission, is retired and unsupported. This means no bug fixes, security updates, or technical support will be provided.
- Continued use of the retired connector or API may expose organizations to operational risks and compliance issues.
- Migration to supported log collection solutions is strongly recommended to ensure ongoing support and security.

**Integration with Related Azure Services:**  
The SAP data connector was typically integrated with Azure Monitor, Log Analytics, and other Azure data ingestion services via the HTTP Data Collector API. With its retirement, users must transition to alternative supported mechanisms for SAP log integration, such as Azure-native connectors or custom ingestion pipelines.

**Summary Sentence:**  
The containerized SAP data connector and its associated container images will be permanently removed from Azure repositories on October 14, 2026, following their retirement and end of support, and users should migrate to supported log collection solutions to maintain secure and reliable SAP log integration with Azure services.

---

### 2. Public Preview: Azure SQL updates for mid-September 2026 

**Published**: September 16, 2026 17:15:10 UTC
**Link**: [Public Preview: Azure SQL updates for mid-September 2026 ](https://azure.microsoft.com/updates?id=571056)

**Update ID**: 571056
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Azure SQL received updates in mid-September 2026, introducing the ability to configure soft delete for Azure SQL logical servers.

- Key changes or new features  
A new soft delete feature is now available for Azure SQL logical servers. When a logical server is deleted, it enters a soft deleted state instead of being permanently removed. During this period, the server can be self-restored within a configurable retention window, providing an additional layer of data protection and recovery options.

- Target audience affected  
This update is relevant for database administrators, IT professionals managing Azure SQL resources, and developers responsible for data protection and disaster recovery strategies.

- Important notes if any  
The soft delete feature helps prevent accidental or malicious deletion of logical servers by allowing recovery within the retention period. IT teams should review and configure appropriate retention settings based on organizational policies. Integration with existing backup and recovery workflows should be evaluated to maximize data protection. This feature is currently in public preview, so it may not yet be suitable for production workloads. Review official documentation for limitations and best practices.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure SQL updates for mid-September 2026  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=571056)

---

**Background and Purpose of the Update:**  
The mid-September 2026 Azure SQL update introduces the capability to configure soft delete for Azure SQL logical servers. The primary purpose of this enhancement is to improve data protection and operational resilience by allowing logical servers to be placed in a recoverable state upon deletion. This feature addresses scenarios where accidental or malicious deletion of logical servers could result in significant data loss or service disruption, providing administrators with a safety net to restore deleted resources within a configurable retention window.

---

**Specific Features and Detailed Changes:**  
- **Soft Delete Configuration:** Administrators can now enable soft delete for Azure SQL logical servers. When enabled, deletion of a logical server does not immediately remove it from the environment; instead, it transitions the server into a soft deleted state.
- **Self-Restorable State:** During the configured retention period, the logical server can be restored by the user, allowing for recovery of databases and server-level configurations.
- **Retention Window:** The duration for which the logical server remains in the soft deleted state is configurable, providing flexibility to align with organizational policies and compliance requirements.

---

**Technical Mechanisms and Implementation Methods:**  
- **Soft Delete Workflow:** Upon deletion, the Azure SQL logical server is not permanently removed. Instead, Azure marks the server as soft deleted and retains its metadata, configuration, and associated databases for the duration specified by the retention policy.
- **Restoration Process:** During the soft deleted state, users can initiate a restoration operation through the Azure portal, CLI, or REST API. This process reverts the logical server and its databases to their pre-deletion state.
- **Configuration Interface:** Soft delete settings can be managed via Azure Resource Manager templates, PowerShell, or the Azure portal, allowing integration with existing infrastructure-as-code and automation workflows.

---

**Use Cases and Application Scenarios:**  
- **Accidental Deletion Recovery:** Organizations can recover logical servers that were mistakenly deleted, minimizing downtime and preventing data loss.
- **Operational Safety:** Soft delete provides an additional layer of protection during maintenance or migration activities, ensuring that resources can be restored if issues arise.
- **Compliance and Audit:** The feature supports compliance requirements by allowing retention and recovery of deleted resources within a specified window, aiding in audit and investigation scenarios.

---

**Important Considerations and Limitations:**  
- **Retention Period:** The logical server is only restorable within the configured retention window. After this period, the server and associated data are permanently deleted and cannot be recovered.
- **Resource Billing:** While in the soft deleted state, billing implications may apply depending on Azure’s resource management policies; users should review documentation for cost considerations.
- **Feature Scope:** The soft delete functionality is specific to Azure SQL logical servers and may not extend to other Azure SQL resource types or related services unless explicitly stated.

---

**Integration with Related Azure Services:**  
- **Azure Resource Manager:** Soft delete is integrated with ARM, enabling management through templates and automation tools.
- **Azure Backup and Recovery:** The feature complements existing backup and recovery solutions, providing an additional recovery option at the logical server level.
- **Azure Security and Compliance:** Soft delete aligns with Azure’s security and compliance frameworks, supporting data protection and retention policies.

---

**Summary Sentence:**  
The mid-September 2026 Azure SQL update introduces configurable soft delete for logical servers, enabling self-restoration within a defined retention window to enhance data protection and operational resilience.

---

### 3. Public Preview: Azure Red Hat OpenShift with hosted control planes 

**Published**: September 16, 2026 14:13:08 UTC
**Link**: [Public Preview: Azure Red Hat OpenShift with hosted control planes ](https://azure.microsoft.com/updates?id=571621)

**Update ID**: 571621
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Red Hat OpenShift, Feature

**Summary**:

- What was updated  
Azure Red Hat OpenShift now offers a new deployment option called "hosted control planes," which has entered public preview.

- Key changes or new features  
The hosted control planes option separates the OpenShift control plane from the worker nodes. The control plane is fully managed by Azure and runs as a service, while customer applications continue to run on worker nodes in the customer’s Azure subscription. This architecture provides improved cluster startup times, better resource isolation, and enhanced security. It also reduces management overhead for the control plane, allowing customers to focus on their workloads.

- Target audience affected  
This update is relevant for developers and IT professionals who deploy and manage containerized applications on Azure Red Hat OpenShift, especially those seeking greater scalability, security, and operational efficiency.

- Important notes if any  
The hosted control planes feature is currently in public preview and may not yet be suitable for production workloads. Customers should evaluate the feature in test environments and review Azure’s preview terms. Existing Azure Red Hat OpenShift clusters are not affected; this is an additional deployment option. For more details, refer to the official documentation and the Azure Updates page.

**Details**:

**Azure Update Report: Public Preview – Azure Red Hat OpenShift with Hosted Control Planes**

**Background and Purpose of the Update**  
Azure Red Hat OpenShift (ARO) is a managed Kubernetes platform jointly engineered by Microsoft and Red Hat, providing enterprise-grade OpenShift clusters on Azure. Traditionally, both the OpenShift control plane and worker nodes are deployed and managed together within the customer’s Azure environment. The new deployment option, now available in public preview, introduces hosted control planes, where the OpenShift control plane is operated as a fully managed service, distinct from the worker nodes that execute customer workloads. The primary purpose of this update is to simplify cluster management, enhance operational efficiency, and improve scalability by decoupling the control plane from the worker nodes.

**Specific Features and Detailed Changes**  
- **Hosted Control Plane Architecture:** The control plane components (API server, scheduler, controller manager, etcd) are hosted and managed by Azure, while worker nodes remain in the customer’s Azure subscription.
- **Separation of Management Responsibilities:** Azure manages the lifecycle, upgrades, and health of the control plane, reducing the operational burden on customers.
- **Enhanced Security and Isolation:** By separating the control plane, customers gain improved isolation between management and application workloads.
- **Simplified Cluster Operations:** Customers can focus on managing their application workloads without needing to provision or maintain control plane infrastructure.
- **Public Preview Availability:** This feature is currently in public preview, allowing customers to evaluate and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Managed Service Model:** The control plane is provisioned and maintained by Azure, leveraging Azure’s infrastructure for high availability and resilience.
- **Worker Node Deployment:** Customers deploy worker nodes in their own Azure subscription, which connect securely to the hosted control plane.
- **Networking and Connectivity:** Secure communication channels are established between the hosted control plane and worker nodes, ensuring data integrity and operational security.
- **Lifecycle Management:** Azure automates control plane upgrades, patching, and monitoring, while customers retain control over worker node lifecycle and scaling.

**Use Cases and Application Scenarios**  
- **Enterprise Workloads:** Organizations seeking to run production-grade OpenShift clusters with reduced management overhead.
- **Multi-Cluster Deployments:** Scenarios where multiple clusters are required, and centralized management of control planes enhances scalability and operational consistency.
- **Dev/Test Environments:** Teams needing rapid provisioning of OpenShift clusters without the complexity of managing control plane infrastructure.
- **Regulatory Compliance:** Workloads requiring strict separation between management and application resources for compliance purposes.

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for mission-critical workloads and is subject to change based on user feedback.
- **Resource Boundaries:** Customers must ensure proper configuration of networking and permissions between their worker nodes and the hosted control plane.
- **Integration Limitations:** Some advanced OpenShift features or customizations may not be fully supported in the hosted control plane model during preview.

**Integration with Related Azure Services**  
- **Azure Networking:** Integration with Azure Virtual Networks (VNet) for secure connectivity between worker nodes and the hosted control plane.
- **Azure Monitoring and Logging:** Customers can leverage Azure Monitor and Log Analytics for observability of worker node workloads, while Azure manages control plane monitoring.
- **Azure Identity and Access Management:** Azure Active Directory can be used for authentication and authorization, ensuring secure access to cluster resources.

**Summary Sentence:**  
Azure Red Hat OpenShift with hosted control planes, now in public preview, offers a fully managed control plane service separated from customer-deployed worker nodes, streamlining cluster management and enhancing operational efficiency for enterprise OpenShift workloads on Azure.

---

### 4. Public Preview: PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL 

**Published**: September 16, 2026 14:07:14 UTC
**Link**: [Public Preview: PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=569664)

**Update ID**: 569664
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL now offers a public preview of PostgreSQL skills and the MCP plugin, enabling AI coding assistants to provide expert PostgreSQL guidance and interact directly with connected databases.

- Key changes or new features  
  - Integration of PostgreSQL skills and MCP plugin with supported AI coding assistants (such as GitHub Copilot, Azure AI, etc.).  
  - AI assistants become context-aware PostgreSQL experts, able to answer questions, provide code suggestions, and perform actions on connected PostgreSQL databases.  
  - Plugin includes expert-curated PostgreSQL and Azure Data skills, enhancing productivity and accuracy for database development and management tasks.

- Target audience affected  
  - Developers working with Azure Database for PostgreSQL who use AI coding assistants.  
  - IT professionals and DBAs managing PostgreSQL workloads on Azure.

- Important notes if any  
  - This feature is in public preview and may be subject to changes before general availability.  
  - Supported AI coding assistants must be compatible with the MCP plugin.  
  - Review documentation for setup instructions and supported scenarios.  
  - Using AI-driven actions on production databases should be carefully evaluated for security and compliance.

[More details](https://azure.microsoft.com/updates?id=569664)

**Details**:

**Azure Update Report: Public Preview – PostgreSQL Skills and MCP Plugin for Azure Database for PostgreSQL**

**Background and Purpose of the Update:**  
The update introduces the public preview of the PostgreSQL skills and MCP (Model Customization Platform) plugin for Azure Database for PostgreSQL. The primary objective is to enhance the productivity and efficiency of developers and database administrators by integrating AI-powered coding assistants with expert-level PostgreSQL knowledge. This integration aims to provide both contextual guidance and actionable capabilities directly on connected PostgreSQL databases within Azure, streamlining database development and management tasks.

**Specific Features and Detailed Changes:**  
- **Expert-Curated PostgreSQL Skills:** The plugin bundles a set of PostgreSQL skills curated by experts, enabling AI coding assistants to deliver precise, context-aware recommendations and solutions for PostgreSQL-related queries and tasks.
- **MCP Plugin Integration:** The MCP plugin framework is leveraged to extend the capabilities of supported AI coding assistants, allowing them to interact with and execute actions on Azure Database for PostgreSQL instances.
- **Guidance and Actionability:** The plugin not only provides guidance (such as query optimization tips, schema design recommendations, and troubleshooting advice) but also enables the AI assistant to perform actions directly on the connected database, subject to permissions and security controls.
- **Azure Data Integration:** The plugin is designed to work seamlessly with Azure Data services, ensuring that recommendations and actions are tailored for the Azure Database for PostgreSQL environment.

**Technical Mechanisms and Implementation Methods:**  
- The plugin operates as an extension to supported AI coding assistants, interfacing with Azure Database for PostgreSQL via secure, authenticated connections.
- It leverages a curated knowledge base of PostgreSQL best practices and Azure-specific configurations, enabling the AI assistant to interpret user intent and translate it into actionable database operations or recommendations.
- The MCP plugin architecture facilitates modular integration, allowing for updates and enhancements to the PostgreSQL skill set without disrupting existing workflows.
- Security and compliance are maintained through Azure’s authentication and authorization mechanisms, ensuring that only permitted actions are executed on the database.

**Use Cases and Application Scenarios:**  
- **Developer Productivity:** Developers can use AI coding assistants equipped with the plugin to receive instant, context-aware guidance while writing SQL queries, designing schemas, or debugging issues in Azure Database for PostgreSQL.
- **Database Administration:** DBAs can leverage the plugin to automate routine maintenance tasks, receive optimization suggestions, and quickly resolve performance bottlenecks.
- **Onboarding and Training:** New team members can benefit from expert-curated guidance, reducing the learning curve associated with PostgreSQL and Azure Data services.
- **DevOps and Automation:** The plugin can be integrated into CI/CD pipelines where AI-driven recommendations and actions help maintain database quality and performance.

**Important Considerations and Limitations:**  
- The plugin is currently in public preview; features and capabilities may change before general availability.
- Only supported AI coding assistants can utilize the plugin; compatibility should be verified before deployment.
- Actionability is governed by user permissions and Azure security policies, ensuring that only authorized operations are performed.
- The plugin is designed for Azure Database for PostgreSQL and may not support other PostgreSQL deployments or cloud providers.

**Integration with Related Azure Services:**  
- The plugin is tightly integrated with Azure Database for PostgreSQL, leveraging Azure’s authentication, authorization, and data management frameworks.
- It complements other Azure Data services by providing PostgreSQL-specific expertise within the broader Azure ecosystem.
- The plugin’s architecture allows for potential future integration with additional Azure AI and data management tools.

**Summary Sentence:**  
The public preview of the PostgreSQL skills and MCP plugin for Azure Database for PostgreSQL enables AI coding assistants to deliver expert, context-aware guidance and actionable capabilities, streamlining database development and management within the Azure ecosystem.

---


*This report was automatically generated - 2026-09-17 03:03:05 UTC*