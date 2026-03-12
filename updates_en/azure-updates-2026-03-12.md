# March 12, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 12, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Generally Available: Terraform, Bicep, Ansible support for elastic clusters on Azure Database for PostgreSQL 

**Published**: March 11, 2026 18:00:35 UTC
**Link**: [Generally Available: Terraform, Bicep, Ansible support for elastic clusters on Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=558145)

**Update ID**: 558145
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL elastic clusters now have General Availability (GA) support for provisioning and management using Terraform, Bicep, and Ansible.

- Key changes or new features  
Native Infrastructure-as-Code (IaC) support is now available for elastic clusters on Azure Database for PostgreSQL. Developers and IT professionals can use Terraform, Bicep, and Ansible to consistently create, scale, and manage elastic clusters. This enables automated deployment, configuration, and lifecycle management of PostgreSQL elastic clusters using popular IaC tools.

- Target audience affected  
This update is relevant for DevOps engineers, cloud architects, database administrators, and IT professionals who manage PostgreSQL workloads on Azure and use Terraform, Bicep, or Ansible for infrastructure automation.

- Important notes if any  
With this GA release, IaC integrations are fully supported and production-ready. Users can now standardize and automate PostgreSQL elastic cluster deployments, improving consistency and reducing manual effort. Ensure you are using the latest versions of Terraform, Bicep, and Ansible modules to access these capabilities.

For more information, see the official update: https://azure.microsoft.com/updates?id=558145

**Details**:

**Background and Purpose of the Update**  
This update announces the General Availability (GA) of native Infrastructure-as-Code (IaC) support for provisioning and managing Azure Database for PostgreSQL elastic clusters using Terraform, Bicep, and Ansible. The primary purpose is to enable IT professionals and DevOps teams to automate and standardize the lifecycle management of PostgreSQL elastic clusters on Azure, leveraging widely adopted IaC tools.

**Specific Features and Detailed Changes**  
- **Terraform Support:** Users can now define, deploy, and manage Azure Database for PostgreSQL elastic clusters declaratively using HashiCorp Terraform configurations. This includes resource provisioning, scaling, and configuration management.
- **Bicep Support:** Bicep, Azure’s domain-specific language for ARM template authoring, is now fully supported for elastic clusters, enabling concise and modular resource definitions.
- **Ansible Support:** Ansible playbooks can now orchestrate the deployment and management of PostgreSQL elastic clusters, allowing for configuration management and automation within CI/CD pipelines.
- **General Availability:** These features are now fully supported and recommended for production workloads.

**Technical Mechanisms and Implementation Methods**  
- **Terraform:** Azure provides updated Terraform providers/modules that expose resources and data sources for PostgreSQL elastic clusters. Users write HCL (HashiCorp Configuration Language) files, which Terraform interprets to interact with Azure Resource Manager (ARM) APIs.
- **Bicep:** Bicep templates are transpiled into ARM templates, which are then deployed via Azure Resource Manager. This enables the declarative provisioning of elastic clusters with parameterization and modularity.
- **Ansible:** Azure modules for Ansible are updated to include tasks and roles for managing PostgreSQL elastic clusters. Playbooks can invoke these modules to automate cluster operations via ARM APIs.

**Use Cases and Application Scenarios**  
- **Automated Provisioning:** Teams can automate the creation of PostgreSQL elastic clusters as part of infrastructure deployment pipelines, ensuring consistency across environments (dev, test, prod).
- **Scaling Operations:** IaC templates can be updated to modify cluster size or configuration, and changes can be applied programmatically, supporting dynamic scaling needs.
- **Disaster Recovery and Replication:** Clusters can be redeployed or replicated in different regions using the same IaC definitions, facilitating disaster recovery strategies.
- **Compliance and Auditing:** Declarative templates serve as documentation and audit trails for infrastructure changes, supporting compliance requirements.

**Important Considerations and Limitations**  
- **Template Accuracy:** Ensure that Terraform, Bicep, or Ansible templates are kept up-to-date with the latest Azure provider/module versions to leverage new features and avoid deprecated configurations.
- **State Management:** For Terraform and Ansible, manage state files securely to prevent configuration drift and unauthorized changes.
- **Feature Parity:** While the update confirms GA support, always verify that all required PostgreSQL elastic cluster features are exposed via the chosen IaC tool’s modules/providers.
- **Resource Limits:** Be aware of Azure subscription and service limits when automating large-scale deployments.

**Integration with Related Azure Services**  
- **Azure Resource Manager (ARM):** All IaC tools interact with ARM for resource provisioning and management.
- **CI/CD Pipelines:** Integration with Azure DevOps, GitHub Actions, or other CI/CD platforms is straightforward, enabling infrastructure automation as part of application delivery workflows.
- **Monitoring and Security:** IaC deployments can be combined with Azure Monitor and Azure Policy for enhanced observability and governance.

**Summary:**  
Azure Database for PostgreSQL elastic clusters now offer full General Availability support for provisioning and management via Terraform, Bicep, and Ansible, enabling automated, consistent, and scalable infrastructure management using industry-standard Infrastructure-as-Code tools.

---

### 2. Generally Available: Azure Database for PostgreSQL dashboards with Grafana 

**Published**: March 11, 2026 18:00:35 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL dashboards with Grafana ](https://azure.microsoft.com/updates?id=558140)

**Update ID**: 558140
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL now offers generally available, built-in Grafana dashboards directly within the Azure portal.

- Key changes or new features  
  - Native integration with Azure Monitor enables out-of-the-box Grafana dashboards for Azure Database for PostgreSQL.  
  - Users can access rich monitoring and visualization tools without deploying or managing a separate Grafana instance.  
  - Dashboards provide deep visibility into database performance, resource utilization, and operational metrics.

- Target audience affected  
Developers, database administrators, and IT professionals managing Azure Database for PostgreSQL instances.

- Important notes  
  - This update streamlines monitoring workflows by centralizing database observability within the Azure portal.  
  - No additional configuration or infrastructure is required to use the built-in dashboards.  
  - The feature enhances troubleshooting and performance tuning capabilities for PostgreSQL workloads on Azure.

For more details, see the official update: https://azure.microsoft.com/updates?id=558140

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Azure Database for PostgreSQL dashboards with Grafana  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=558140)

---

### Background and Purpose of the Update

This update introduces the general availability of built-in Grafana dashboards for monitoring Azure Database for PostgreSQL directly within the Azure portal. The primary goal is to streamline and enhance the monitoring experience for PostgreSQL workloads on Azure by providing immediate access to advanced visualization tools without the need for separate Grafana deployments. This integration aims to reduce operational overhead and accelerate insights into database performance and health.

---

### Specific Features and Detailed Changes

- **Native Grafana Dashboards:** Azure Database for PostgreSQL now includes rich, pre-configured Grafana dashboards accessible from the Azure portal.
- **Built-in Monitoring:** Users can leverage these dashboards without deploying or managing an external Grafana instance.
- **Deep Visibility:** The dashboards provide comprehensive metrics and visualizations for PostgreSQL instances, supporting in-depth monitoring and troubleshooting.

---

### Technical Mechanisms and Implementation Methods

- **Azure Monitor Integration:** The solution leverages native integration with Azure Monitor, which collects and aggregates metrics and logs from PostgreSQL databases.
- **Embedded Grafana Experience:** The Grafana dashboards are embedded directly within the Azure portal, utilizing Azure’s authentication and access control mechanisms.
- **No External Setup Required:** Users do not need to provision, configure, or maintain a standalone Grafana server; all dashboard functionality is provided as a managed, built-in feature.

---

### Use Cases and Application Scenarios

- **Performance Monitoring:** Database administrators and DevOps engineers can monitor key performance indicators (KPIs) such as CPU usage, memory consumption, query performance, and connection statistics.
- **Troubleshooting:** The dashboards facilitate rapid identification of performance bottlenecks, resource contention, or abnormal behavior in PostgreSQL instances.
- **Operational Reporting:** Teams can use the visualizations for regular health checks, capacity planning, and compliance reporting without additional setup.
- **Integrated Workflows:** Since the dashboards are available in the Azure portal, they fit seamlessly into existing Azure-based operational workflows.

---

### Important Considerations and Limitations

- **Scope:** The feature is specific to Azure Database for PostgreSQL and does not extend to other database services unless similarly updated.
- **Customization:** The update does not specify whether users can customize the built-in dashboards or if only default visualizations are available.
- **Data Source:** All metrics are sourced from Azure Monitor, so the granularity and retention of data are subject to Azure Monitor’s capabilities and configuration.
- **Access Control:** Dashboard access is governed by Azure portal authentication and role-based access control (RBAC).

---

### Integration with Related Azure Services

- **Azure Monitor:** Serves as the underlying telemetry platform, collecting and providing the metrics visualized in Grafana.
- **Azure Portal:** The dashboards are fully integrated into the Azure portal, offering a unified management and monitoring interface.
- **Security and Compliance:** Integration with Azure’s security and identity management ensures that monitoring data is protected and access is controlled.

---

**Summary:**  
Azure Database for PostgreSQL now offers generally available, built-in Grafana dashboards within the Azure portal, enabling users to monitor database performance and health with advanced visualizations powered by Azure Monitor, without the need for separate Grafana infrastructure.

---

### 3. Public Preview: Customer‑managed encryption keys now supported on Premium SSD v2 disks for Azure Database for PostgreSQL 

**Published**: March 11, 2026 18:00:35 UTC
**Link**: [Public Preview: Customer‑managed encryption keys now supported on Premium SSD v2 disks for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=557527)

**Update ID**: 557527
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL now supports customer-managed encryption keys (CMKs) for data at rest on Premium SSD v2 disks, available in public preview.

- Key changes or new features  
This update enables users to leverage their own encryption keys, managed through Azure Key Vault, to encrypt data stored on Premium SSD v2 disks used by Azure Database for PostgreSQL. This provides enhanced control over data security and compliance, allowing organizations to meet strict regulatory or internal security requirements. The feature is currently in public preview.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL deployments, especially those with advanced security, compliance, or data governance needs.

- Important notes if any  
- This feature is only available for Premium SSD v2 disks and is in public preview, so it may not be recommended for production workloads yet.  
- Integration with Azure Key Vault is required to manage the customer-managed keys.  
- Review Azure documentation for any regional availability limitations and best practices for implementing CMKs with your PostgreSQL databases.  
- Existing databases using other disk types or encryption methods are not affected by this update.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Customer‑managed encryption keys now supported on Premium SSD v2 disks for Azure Database for PostgreSQL  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=557527)

---

**Background and Purpose of the Update:**  
The update introduces customer-managed encryption keys (CMKs) support for Premium SSD v2 disks used by Azure Database for PostgreSQL. The primary purpose is to enhance data security for PostgreSQL workloads by allowing customers to control the encryption of data at rest. This responds to increasing requirements for compliance, regulatory standards, and enterprise security policies that mandate customer ownership of encryption keys.

**Specific Features and Detailed Changes:**  
With this public preview, Azure Database for PostgreSQL now supports the use of CMKs with Premium SSD v2 disks. Previously, disk encryption was managed solely by Azure using platform-managed keys. The new feature enables customers to specify and manage their own encryption keys for disk-level encryption, thereby providing greater control and flexibility over data protection.

**Technical Mechanisms and Implementation Methods:**  
The implementation leverages Azure’s integration with Azure Key Vault, which is used to store and manage customer-managed keys. When provisioning or configuring Azure Database for PostgreSQL with Premium SSD v2 disks, customers can select a CMK stored in their Azure Key Vault. The disk encryption process utilizes this key to encrypt data at rest, ensuring that only authorized users with access to the Key Vault can manage the encryption keys. This mechanism enhances security by isolating key management from the platform and allowing for key rotation, revocation, and auditing.

**Use Cases and Application Scenarios:**  
- **Regulatory Compliance:** Organizations subject to strict regulatory requirements (such as GDPR, HIPAA, or PCI DSS) can use CMKs to demonstrate control over encryption keys and meet compliance needs.
- **Enterprise Security:** Enterprises with internal security policies requiring customer ownership of encryption keys can leverage this feature for PostgreSQL workloads.
- **Data Sovereignty:** Customers concerned with data sovereignty can ensure that encryption keys remain under their control, reducing risk associated with platform-managed keys.

**Important Considerations and Limitations:**  
- This feature is currently in public preview, which means it may not be suitable for production workloads until general availability.
- CMK support is limited to Premium SSD v2 disks; other disk types may not support this capability.
- Customers must configure and maintain their Azure Key Vault, including proper access policies and key lifecycle management.
- Integration and compatibility with existing backup, restore, and migration workflows should be validated, as CMK usage may impact these operations.
- There may be additional costs associated with Azure Key Vault usage and Premium SSD v2 disks.

**Integration with Related Azure Services:**  
- **Azure Key Vault:** Central to the implementation, Azure Key Vault stores and manages CMKs, enabling secure key management and access control.
- **Azure Database for PostgreSQL:** The update directly enhances the security posture of this managed database service by supporting CMKs for disk encryption.
- **Premium SSD v2 Disks:** The feature is specific to this disk type, which offers high performance and advanced features for enterprise workloads.

---

**Summary Sentence:**  
Azure Database for PostgreSQL now supports customer-managed encryption keys for Premium SSD v2 disks in public preview, enabling enhanced data security and greater control over encryption of data at rest through integration with Azure Key Vault.

---

### 4. Generally Available: Azure SRE Agent with new capabilities 

**Published**: March 11, 2026 17:45:49 UTC
**Link**: [Generally Available: Azure SRE Agent with new capabilities ](https://azure.microsoft.com/updates?id=558321)

**Update ID**: 558321
**Data source**: Azure Updates API

**Categories**: Launched, Features, Gallery, Open Source, Services

**Summary**:

- What was updated  
Azure SRE Agent is now generally available (GA), offering new capabilities for AI-powered operations management.

- Key changes or new features  
  - Deep contextual awareness for faster incident diagnosis.  
  - Automated response workflows to reduce manual intervention and operational toil.  
  - Enhanced integration with Azure services for improved uptime and incident impact mitigation.  
  - AI-driven recommendations and actionable insights to support Site Reliability Engineering (SRE) practices.

- Target audience affected  
  - Developers and IT professionals responsible for application reliability, operations, and incident management.  
  - SRE teams seeking to automate and streamline operational workflows on Azure.

- Important notes if any  
  - The GA release makes the Azure SRE Agent production-ready for enterprise workloads.  
  - Teams can leverage the agent to accelerate root cause analysis and automate common remediation tasks, reducing mean time to recovery (MTTR).  
  - Integration with existing Azure monitoring and management tools is supported, enabling seamless adoption within current DevOps and IT operations environments.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=558321).

**Details**:

**Azure Update Report: Generally Available – Azure SRE Agent with New Capabilities**

**Background and Purpose of the Update**  
The Azure SRE (Site Reliability Engineering) Agent is now generally available, marking its transition from preview to production-ready status. The primary purpose of this update is to empower operations teams with an AI-powered agent that enhances service reliability by improving uptime, reducing the impact of incidents, and minimizing operational toil. The agent is designed to accelerate incident diagnosis and automate response workflows, addressing common challenges in cloud operations such as slow troubleshooting and manual remediation.

**Specific Features and Detailed Changes**  
With the GA (General Availability) release, Azure SRE Agent introduces new capabilities, notably “deep context.” This feature enables the agent to provide richer, more granular operational insights during incident diagnosis and response. The agent leverages AI to analyze telemetry, logs, and operational signals, offering actionable recommendations and automating remediation steps. The update focuses on:

- Enhanced incident diagnosis: Faster identification of root causes using deep contextual analysis.
- Automated response workflows: AI-driven automation of common operational tasks and incident responses.
- Improved operational insights: Advanced analytics and context-aware recommendations for resolving issues.
- Reduction of manual toil: Streamlining repetitive tasks and minimizing the need for manual intervention.

**Technical Mechanisms and Implementation Methods**  
The Azure SRE Agent operates by ingesting operational data from Azure resources, including telemetry, logs, and metrics. It uses AI algorithms to process this data, detect anomalies, and correlate events across services. The agent’s deep context capability allows it to synthesize information from multiple sources, providing a holistic view of incidents. Response workflows are automated through integration with Azure automation tools, enabling the agent to execute remediation actions directly or guide operators with step-by-step instructions. The agent can be deployed across Azure environments and configured to monitor specific resources or workloads.

**Use Cases and Application Scenarios**  
Typical application scenarios include:

- Automated incident diagnosis and remediation for mission-critical Azure workloads.
- Proactive monitoring and alerting for distributed applications.
- Reduction of mean time to resolution (MTTR) in production environments.
- Streamlining operational workflows for DevOps and SRE teams managing large-scale Azure deployments.
- Enhancing reliability and uptime for services with complex dependencies.

**Important Considerations and Limitations**  
IT professionals should consider the following:

- The agent’s effectiveness depends on the quality and completeness of operational data ingested.
- Integration and configuration may require alignment with existing monitoring and automation frameworks.
- The scope of automated workflows and recommendations is limited to supported Azure services and scenarios.
- Security and access controls must be carefully managed to ensure the agent can execute remediation actions without compromising compliance.

**Integration with Related Azure Services**  
The Azure SRE Agent integrates seamlessly with Azure Monitor, Azure Log Analytics, and Azure Automation. It can ingest data from these services for analysis and trigger remediation workflows using Azure Automation Runbooks or Logic Apps. The agent is designed to work alongside existing Azure operational tools, enhancing their capabilities with AI-driven insights and automation.

**Summary Sentence**  
Azure SRE Agent is now generally available, offering AI-powered incident diagnosis, automated response workflows, and deep contextual insights to improve uptime and reduce operational toil for Azure environments.

---

### 5. Public Preview: Query Profiler in MSSQL extension for Visual Studio Code 

**Published**: March 11, 2026 17:45:49 UTC
**Link**: [Public Preview: Query Profiler in MSSQL extension for Visual Studio Code ](https://azure.microsoft.com/updates?id=558164)

**Update ID**: 558164
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now includes a Query Profiler feature, available in public preview.

- Key changes or new features  
Query Profiler enables developers and database administrators to capture and analyze SQL query and database activity in real time directly within Visual Studio Code. It provides execution plans, query statistics, and performance insights without leaving the code editor. This integration streamlines the process of identifying performance bottlenecks and optimizing queries during development.

- Target audience affected  
This update primarily benefits developers, database administrators (DBAs), and IT professionals who use Visual Studio Code for SQL Server development and troubleshooting.

- Important notes if any  
The Query Profiler is currently in public preview, meaning features may change before general availability and some limitations may exist. Users are encouraged to provide feedback to help improve the feature. To access Query Profiler, ensure you have the latest version of the MSSQL extension installed in Visual Studio Code.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=558164).

**Details**:

**Azure Update Technical Explanation: Public Preview: Query Profiler in MSSQL extension for Visual Studio Code**

**Background and Purpose of the Update:**  
The introduction of Query Profiler in the MSSQL extension for Visual Studio Code addresses the need for integrated, real-time query and database activity monitoring within a lightweight development environment. Traditionally, database profiling and performance analysis required switching to dedicated tools or SQL Server Management Studio (SSMS). This update aims to streamline the developer and DBA workflow by embedding profiling capabilities directly into Visual Studio Code, enhancing productivity and reducing context switching.

**Specific Features and Detailed Changes:**  
- **Query Profiler Integration:** The MSSQL extension now includes Query Profiler functionality in public preview.  
- **Real-Time Insights:** Users can capture query and database activity as it happens, without leaving Visual Studio Code.  
- **Activity Capture:** The profiler records query executions and database events, providing immediate feedback on query performance and resource utilization.  
- **In-Editor Visualization:** Profiling results are visualized directly within the Visual Studio Code interface, allowing users to analyze performance metrics alongside their code.

**Technical Mechanisms and Implementation Methods:**  
- **Extension-Based Profiling:** The Query Profiler is implemented as part of the MSSQL extension, leveraging Visual Studio Code’s extension APIs to provide a seamless user experience.  
- **Live Data Capture:** When enabled, the profiler hooks into the active database connection to monitor and record query execution data in real time.  
- **Result Presentation:** Captured profiling data is rendered within Visual Studio Code, likely using custom views or panels, enabling users to inspect execution plans, duration, and resource usage without external tools.

**Use Cases and Application Scenarios:**  
- **Query Optimization:** Developers and DBAs can use the profiler to identify slow-running queries and optimize SQL statements during development.  
- **Performance Troubleshooting:** The profiler assists in diagnosing performance bottlenecks by providing immediate visibility into query execution characteristics.  
- **Development Workflow Integration:** By embedding profiling into Visual Studio Code, teams can incorporate performance analysis into their standard development and testing processes.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be fully stable or feature-complete. Users should exercise caution when using it in production environments.  
- **Scope of Profiling:** The profiler captures activity for queries executed within Visual Studio Code via the MSSQL extension. It may not monitor queries initiated from other tools or applications.  
- **Resource Impact:** Running the profiler may introduce additional overhead on the database connection, potentially affecting performance during profiling sessions.

**Integration with Related Azure Services:**  
- **Azure SQL Database Support:** The Query Profiler can be used with Azure SQL Database connections established through the MSSQL extension, providing a unified experience for profiling both on-premises and cloud-based SQL databases.  
- **Developer Toolchain Alignment:** The update aligns with Azure’s focus on developer productivity by enhancing the capabilities of Visual Studio Code, a widely used tool for Azure development.

**Summary:**  
The public preview of Query Profiler in the MSSQL extension for Visual Studio Code enables real-time query and database activity monitoring directly within the editor, streamlining performance analysis and optimization for developers and DBAs working with SQL Server and Azure SQL Database.

---


*This report was automatically generated - 2026-03-12 03:04:19 UTC*