# August 20, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 20, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 6 items

## Update List

### 1. Generally Available: Azure Databricks Lakebase in four additional regions

**Published**: August 19, 2026 21:04:18 UTC
**Link**: [Generally Available: Azure Databricks Lakebase in four additional regions](https://azure.microsoft.com/updates?id=569684)

**Update ID**: 569684
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Feature

**Summary**:

- What was updated  
Azure Databricks Lakebase is now generally available in four additional Azure regions: North Central US, France Central, Germany West Central, and East Asia.

- Key changes or new features  
This update expands the regional availability of Azure Databricks Lakebase, enabling customers to deploy and operate Lakebase in these new regions. It offers greater flexibility for data residency, compliance, and disaster recovery strategies.

- Target audience affected  
Developers, data engineers, and IT professionals using or planning to use Azure Databricks Lakebase for analytics, data engineering, and AI workloads, especially those with regional requirements.

- Important notes if any  
Customers can now select these additional regions when provisioning Lakebase resources, supporting scenarios that require local data processing or compliance with regional regulations. This expansion may also help reduce latency for users and applications located in or near the new regions. No changes to API or service functionality were announced; this update is focused on regional availability.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Databricks Lakebase in four additional regions  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=569684)

---

**Background and Purpose of the Update**  
Azure Databricks Lakebase is a unified analytics platform designed to simplify and accelerate data engineering, data science, and analytics workloads. The purpose of this update is to expand the general availability of Lakebase to four additional Azure regions: North Central US, France Central, Germany West Central, and East Asia. This regional expansion aims to provide customers with increased flexibility in deployment, improved data residency options, and enhanced performance by reducing latency for workloads hosted closer to their user base.

**Specific Features and Detailed Changes**  
The core change in this update is the general availability (GA) of Lakebase in the newly listed regions. Customers can now provision Lakebase resources in North Central US, France Central, Germany West Central, and East Asia, in addition to previously supported regions. This enables organizations to leverage Lakebase’s capabilities for scalable data processing, analytics, and machine learning in these geographies. No new features or functional changes to Lakebase are announced; the update strictly pertains to expanded regional support.

**Technical Mechanisms and Implementation Methods**  
From a technical perspective, the regional expansion involves the provisioning of Lakebase infrastructure within the Azure datacenters located in North Central US, France Central, Germany West Central, and East Asia. This is achieved by deploying Lakebase’s managed services and compute clusters in these regions, ensuring compliance with Azure’s regional architecture and operational standards. Customers can select the desired region during resource creation in the Azure portal or via ARM templates, allowing for seamless integration with existing Azure resource management workflows.

**Use Cases and Application Scenarios**  
The regional availability of Lakebase is particularly beneficial for organizations with data residency requirements or those seeking to optimize performance for users in the newly supported regions. Typical use cases include:
- Localized data analytics and reporting for regulatory compliance.
- High-performance ETL and data engineering workloads with reduced latency.
- Machine learning model training and inference on region-specific datasets.
- Multi-region disaster recovery and business continuity planning.

**Important Considerations and Limitations**  
IT professionals should consider the following when utilizing Lakebase in these regions:
- Ensure that Lakebase is supported in the selected region for all required features and integrations.
- Review Azure’s regional quotas and capacity limits, as these may differ across regions.
- Validate compliance with local data residency and privacy regulations when deploying in France Central, Germany West Central, and East Asia.
- Existing Lakebase deployments in other regions are unaffected; migration or replication strategies may be required for cross-region workloads.

**Integration with Related Azure Services**  
Lakebase integrates seamlessly with other Azure services such as Azure Data Lake Storage, Azure Synapse Analytics, and Azure Machine Learning. The regional expansion ensures that these integrations can be leveraged locally, enabling end-to-end data pipelines and analytics solutions within the supported regions. IT professionals can architect solutions that combine Lakebase with Azure-native storage, compute, and security services for comprehensive data management and analytics.

---

**Summary Sentence:**  
Azure Databricks Lakebase is now generally available in North Central US, France Central, Germany West Central, and East Asia, providing customers with expanded regional deployment options and enhanced flexibility for data analytics workloads.

---

### 2. Generally Available: Azure SQL updates for mid-August 2026 

**Published**: August 19, 2026 21:01:47 UTC
**Link**: [Generally Available: Azure SQL updates for mid-August 2026 ](https://azure.microsoft.com/updates?id=569145)

**Update ID**: 569145
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Azure SQL received updates in mid-August 2026, focusing on enhanced integration with Visual Studio Code.

- Key changes or new features  
Developers can now customize keyboard shortcuts for Quick Queries, the Results Grid, and the Query Editor directly within Visual Studio Code. This allows users to tailor their workflow and increase productivity without leaving the editor. Shortcut conflicts can be resolved within the same interface, ensuring a smoother experience.

- Target audience affected  
These updates primarily impact developers and IT professionals who use Azure SQL within Visual Studio Code, especially those who rely on keyboard shortcuts for efficient database development and management.

- Important notes if any  
The new customization options are available natively in Visual Studio Code, requiring no external tools or extensions. Users should review and adjust their shortcut settings to avoid conflicts and optimize their workflow. For more details, refer to the official Azure Update documentation.

**Details**:

**Azure SQL Update Report – Mid-August 2026**

**Background and Purpose of the Update**  
The mid-August 2026 Azure SQL update focuses on enhancing developer productivity and customization within the Visual Studio Code (VS Code) environment. The primary goal is to streamline SQL development workflows by allowing users to tailor keyboard shortcuts for key Azure SQL features, thereby improving efficiency and accessibility for technical professionals working with Azure SQL databases.

**Specific Features and Detailed Changes**  
The update introduces the ability to customize keyboard shortcuts for the following Azure SQL functionalities within VS Code:

- **Quick Queries:** Users can assign or modify shortcuts for executing ad-hoc SQL queries rapidly.
- **Results Grid:** Shortcuts can be customized for actions such as navigating, copying, or exporting query results.
- **Query Editor:** Developers can personalize shortcuts for editing, formatting, or executing SQL statements.

These enhancements are accessible directly within the VS Code editor, eliminating the need to exit the development environment or use external configuration tools. The customization interface is integrated into VS Code’s settings, allowing for seamless adjustment of shortcuts according to individual or team preferences.

**Technical Mechanisms and Implementation Methods**  
The update leverages VS Code’s extensibility and keyboard shortcut management system. Azure SQL’s VS Code extension now exposes additional command bindings for Quick Queries, Results Grid, and Query Editor actions. Users can configure these shortcuts via VS Code’s built-in “Keyboard Shortcuts” panel (`Ctrl+K Ctrl+S`), where Azure SQL-specific commands are listed and can be assigned to preferred key combinations.

The implementation ensures that shortcut changes are persisted within the user’s VS Code settings, supporting both local and cloud-synced environments. This mechanism relies on VS Code’s JSON-based settings files, which can be versioned and shared across development teams.

**Use Cases and Application Scenarios**  
- **Database Developers:** Accelerate common tasks such as running queries, reviewing results, and editing SQL scripts without leaving VS Code.
- **Data Analysts:** Customize shortcuts for frequent actions, improving data exploration and reporting workflows.
- **DevOps Engineers:** Streamline database management and automation tasks by assigning shortcuts to repetitive SQL operations.
- **Teams with Accessibility Needs:** Adapt shortcut configurations to accommodate ergonomic or accessibility requirements.

**Important Considerations and Limitations**  
- Shortcut customization is limited to the VS Code environment and does not affect Azure SQL operations in other tools or portals.
- Conflicts may arise if shortcuts overlap with existing VS Code or extension commands; users should review and resolve any conflicts during configuration.
- The update does not introduce new SQL functionality but improves interaction and usability within VS Code.
- Shortcut settings are user-specific unless explicitly exported and shared.

**Integration with Related Azure Services**  
This update is tightly integrated with the Azure SQL extension for VS Code, which connects to Azure SQL Database, Azure SQL Managed Instance, and SQL Server on Azure Virtual Machines. It complements Azure DevOps workflows by facilitating faster query execution and script editing, and it can be used alongside other Azure services accessed via VS Code, such as Azure Resource Manager or Azure Storage extensions.

**Summary Sentence**  
The mid-August 2026 Azure SQL update enables direct customization of keyboard shortcuts for Quick Queries, Results Grid, and Query Editor within Visual Studio Code, enhancing developer productivity and workflow efficiency without leaving the editor environment.

---

### 3. Public Preview: SQL Formatter in MSSQL extension 

**Published**: August 19, 2026 21:00:19 UTC
**Link**: [Public Preview: SQL Formatter in MSSQL extension ](https://azure.microsoft.com/updates?id=569155)

**Update ID**: 569155
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now includes a SQL Formatter feature, available in public preview.

- Key changes or new features  
Developers can now format SQL scripts directly within the editor, improving code readability and consistency. The SQL Formatter offers enhanced customization options, allowing users to tailor formatting rules to their preferred coding style. This streamlines development workflows and helps maintain code quality across teams.

- Target audience affected  
This update is relevant to developers, database administrators, and IT professionals who use the MSSQL extension in Visual Studio Code for SQL Server development and management.

- Important notes if any  
As this feature is in public preview, users may encounter minor bugs or incomplete functionality. Feedback is encouraged to help improve the formatter before general availability. Users should review the extension’s documentation for configuration details and best practices.  

For more information, visit the [official update page](https://azure.microsoft.com/updates?id=569155).

**Details**:

**Azure Update Technical Report: Public Preview – SQL Formatter in MSSQL Extension**

**Background and Purpose of the Update**  
The introduction of the SQL Formatter in the MSSQL extension addresses the need for improved code readability and maintainability within SQL development workflows. Traditionally, SQL scripts can become inconsistent in style due to manual formatting, which complicates collaboration and code review processes. The purpose of this update is to provide developers with an integrated tool to automatically format SQL scripts directly within their editor, promoting cleaner and more consistent codebases.

**Specific Features and Detailed Changes**  
The SQL Formatter, now available in public preview, offers the following enhancements within the MSSQL extension:
- **Direct Formatting in Editor:** Users can format SQL scripts without leaving their development environment, streamlining the editing process.
- **Customizable Formatting Options:** The formatter includes expanded settings that allow users to tailor formatting rules to their preferred coding style. This includes options for indentation, keyword casing, spacing, and line breaks.
- **Consistency and Readability:** By automating formatting, the extension ensures that SQL code adheres to a uniform style, making it easier to read and review.

**Technical Mechanisms and Implementation Methods**  
The SQL Formatter is integrated into the MSSQL extension, which is typically used with Visual Studio Code or similar editors. The formatting engine processes SQL scripts in real-time, applying user-defined or default formatting rules. Customization is achieved through configuration files or editor settings, enabling granular control over formatting behavior. The extension leverages editor APIs to trigger formatting actions, either manually (via command palette or keyboard shortcuts) or automatically (on file save).

**Use Cases and Application Scenarios**  
- **Development Teams:** Facilitates collaborative development by ensuring all team members’ SQL scripts follow the same formatting conventions.
- **Code Review Processes:** Enhances code reviews by reducing time spent on style-related feedback and focusing on logic and performance.
- **Database Administrators:** Helps maintain large SQL script repositories with consistent formatting, aiding in troubleshooting and maintenance.
- **Continuous Integration Pipelines:** Can be incorporated into CI workflows to automatically format SQL scripts before deployment, reducing manual intervention.

**Important Considerations and Limitations**  
- **Public Preview Status:** As the feature is in public preview, it may not be fully stable or feature-complete. Users should test formatting options thoroughly before integrating into production workflows.
- **Customization Scope:** While the formatter offers more customizable options, the extent of customization may be limited compared to dedicated formatting tools. Users should review available settings to ensure they meet organizational standards.
- **Editor Compatibility:** The SQL Formatter is tied to the MSSQL extension and may require specific versions of supported editors (e.g., Visual Studio Code). Compatibility with other editors or environments is not guaranteed.

**Integration with Related Azure Services**  
The MSSQL extension, and by extension the SQL Formatter, is designed to work with Azure SQL Database and SQL Server instances. This integration streamlines development and management of Azure-based SQL resources by providing a consistent, formatted scripting experience. While the formatter itself does not directly interact with Azure services, its use within the MSSQL extension supports Azure SQL workflows, improving script quality and maintainability for cloud-based database solutions.

**Summary Sentence**  
The public preview of SQL Formatter in the MSSQL extension enables IT professionals to format SQL scripts directly within their editor, offering customizable options for cleaner, more consistent, and readable code to streamline SQL development and collaboration.

---

### 4. Generally Available: Azure SQL Database provisioning in MSSQL extension 

**Published**: August 19, 2026 20:59:19 UTC
**Link**: [Generally Available: Azure SQL Database provisioning in MSSQL extension ](https://azure.microsoft.com/updates?id=569160)

**Update ID**: 569160
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Azure SQL Database provisioning is now generally available in the MSSQL extension.

- Key changes or new features  
Developers and IT professionals can now create and connect to fully managed Azure SQL Databases directly from their code editor (such as Visual Studio Code) using the MSSQL extension. This feature is free to use and streamlines the database provisioning process without leaving the development environment. The update also provides ready-to-use templates for Azure Resource Manager (ARM), Bicep, and Terraform, enabling Infrastructure as Code (IaC) workflows for automated and repeatable deployments.

- Target audience affected  
Developers, DevOps engineers, and IT professionals who use Azure SQL Database and Infrastructure as Code tools (ARM, Bicep, Terraform), especially those working within code editors.

- Important notes if any  
This feature simplifies database provisioning and integration with IaC pipelines, reducing setup time and potential errors. It is suitable for development, testing, and learning scenarios at no cost, but production workloads should still consider Azure’s standard pricing and resource limits. Ensure you have the latest MSSQL extension version to access these capabilities.

Data source: Using API data  
[Azure Update Link](https://azure.microsoft.com/updates?id=569160)

**Details**:

**Azure Update Report: Generally Available – Azure SQL Database Provisioning in MSSQL Extension**

**Background and Purpose of the Update**  
This update announces the general availability of Azure SQL Database provisioning directly within the MSSQL extension. The primary purpose is to streamline the process for developers and IT professionals to create and connect to fully managed Azure SQL Databases from their code editor environment, eliminating the need to switch between multiple tools or portals. This enhancement is aimed at improving developer productivity and simplifying cloud database adoption during development and testing phases, especially as the provisioning is offered at no cost.

**Specific Features and Detailed Changes**  
- **Direct Provisioning from Editor:** Users can now create and connect to Azure SQL Databases directly from their code editor using the MSSQL extension, without navigating to the Azure Portal.
- **No-Cost Provisioning:** The feature allows for the creation of databases at no cost, supporting rapid prototyping and development workflows.
- **Infrastructure-as-Code (IaC) Templates:** The update includes ready-to-use templates for Azure Resource Manager (ARM), Bicep, and Terraform. These templates facilitate automated and repeatable database deployments, aligning with modern DevOps and IaC practices.

**Technical Mechanisms and Implementation Methods**  
- **MSSQL Extension Integration:** The MSSQL extension, typically used within editors like Visual Studio Code, now incorporates UI and command-line options to initiate the provisioning of Azure SQL Databases.
- **Template Support:** The extension provides pre-configured ARM, Bicep, and Terraform templates. These templates define the necessary Azure resources and configurations, enabling users to deploy databases programmatically or through CI/CD pipelines.
- **Connection Management:** Upon successful provisioning, the extension manages connection strings and authentication, allowing seamless connectivity between the editor and the newly created Azure SQL Database instance.

**Use Cases and Application Scenarios**  
- **Development and Testing:** Developers can quickly spin up managed SQL databases for application development, testing, or proof-of-concept work without incurring costs or requiring Azure Portal access.
- **DevOps and Automation:** Teams leveraging IaC can utilize the provided templates to standardize and automate database provisioning as part of their deployment pipelines.
- **Education and Training:** Instructors and students can provision databases for learning or demonstration purposes directly from their development environment, simplifying setup.

**Important Considerations and Limitations**  
- **Scope of No-Cost Provisioning:** The update specifies that provisioning is at no cost, but users should verify any limitations regarding resource quotas, performance tiers, or duration of free usage.
- **Template Customization:** While ready-to-use templates are provided, organizations may need to customize them to align with internal policies, compliance requirements, or specific deployment scenarios.
- **Extension Requirements:** Users must ensure they have the latest version of the MSSQL extension installed in their editor to access these features.

**Integration with Related Azure Services**  
- **Azure Resource Manager (ARM):** Enables declarative management and deployment of Azure resources, including SQL Databases, via ARM templates.
- **Bicep:** Provides a domain-specific language for ARM template authoring, simplifying IaC workflows.
- **Terraform:** Supports multi-cloud infrastructure provisioning, allowing integration of Azure SQL Database deployments into broader infrastructure management strategies.
- **Azure SQL Database:** The core managed database service, benefiting from enhanced provisioning and connectivity through the extension.

**Summary Sentence**  
The general availability of Azure SQL Database provisioning in the MSSQL extension enables IT professionals to create and connect to fully managed cloud databases directly from their editor at no cost, with integrated support for ARM, Bicep, and Terraform templates to streamline development, automation, and DevOps workflows.

---

### 5. Generally Available: vCore Customization: Disable Multithreading and Configurable Constrained Cores  

**Published**: August 19, 2026 17:20:42 UTC
**Link**: [Generally Available: vCore Customization: Disable Multithreading and Configurable Constrained Cores  ](https://azure.microsoft.com/updates?id=569051)

**Update ID**: 569051
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Feature

**Summary**:

- What was updated  
Azure Virtual Machines now offer General Availability of vCore Customization, specifically the ability to disable Simultaneous Multi-Threading/Hyper-Threading (SMT/HT) and configure constrained cores.

- Key changes or new features  
  - **Disable SMT/HT:** Users can now turn off multi-threading on supported VM sizes, allowing for single-threaded core operation.  
  - **Configurable Constrained Cores:** Users can specify the exact number of active cores (vCPUs) within a VM, independent of the VM’s memory allocation, enabling better alignment with workload licensing and performance requirements.

- Target audience affected  
  - Developers and IT professionals managing workloads sensitive to multi-threading, such as certain databases, high-performance computing (HPC), and applications with per-core licensing models.  
  - Organizations seeking to optimize cost and performance by tailoring VM core counts to their specific workload needs.

- Important notes if any  
  - These features are available on select VM series and regions; check documentation for compatibility.  
  - Disabling SMT/HT may impact overall throughput but can improve performance consistency for single-threaded workloads.  
  - Configurable constrained cores can help reduce licensing costs for software licensed per core.  
  - No VM redeployment is required; changes can be made during VM creation or via supported APIs.

[More details](https://azure.microsoft.com/updates?id=569051)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: vCore Customization: Disable Multithreading and Configurable Constrained Cores   
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=569051)

---

### Background and Purpose of the Update

The General Availability of VM vCore Customization for Azure Virtual Machines addresses the need for greater control over CPU resource allocation and performance characteristics in cloud environments. Traditionally, Azure VMs have offered fixed vCPU configurations, often with Simultaneous Multi-Threading (SMT) or Hyper-Threading (HT) enabled by default. However, certain workloads—such as high-performance computing (HPC), latency-sensitive applications, and software licensing scenarios—require more granular control over CPU threading and core allocation. This update provides IT professionals with enhanced flexibility to optimize VM performance and compliance.

---

### Specific Features and Detailed Changes

1. **Disable Simultaneous Multi-Threading/Hyper-Threading (SMT/HT):**
   - Azure now allows users to disable SMT/HT at the VM level. This means each vCore will correspond to a physical CPU core, rather than a logical thread, eliminating potential performance variability caused by sharing physical resources between threads.

2. **Configurable Constrained Cores:**
   - Users can now specify the exact number of vCores allocated to a VM, independent of the VM size’s default configuration. This enables precise resource provisioning, which is particularly useful for workloads requiring specific CPU counts or for software licensing compliance.

---

### Technical Mechanisms and Implementation Methods

- **SMT/HT Disabling:**  
  When provisioning a VM, administrators can select an option to disable SMT/HT. Azure orchestrates the VM deployment to ensure that only physical cores are presented to the guest OS, effectively preventing the operating system from seeing or utilizing logical (hyper-threaded) cores.

- **Configurable Constrained Cores:**  
  During VM creation or resizing, users can define the desired number of vCores. Azure’s resource manager enforces this constraint, allocating only the specified number of cores to the VM, regardless of the underlying hardware’s total core count.

Both features are accessible via Azure Portal, CLI, ARM templates, and API, ensuring seamless integration into existing deployment workflows.

---

### Use Cases and Application Scenarios

- **High-Performance Computing (HPC):**  
  Disabling SMT/HT can improve determinism and reduce contention for physical CPU resources, benefiting compute-intensive workloads.
- **Latency-Sensitive Applications:**  
  Applications requiring consistent response times can leverage physical cores to minimize unpredictable delays caused by hyper-threading.
- **Software Licensing Compliance:**  
  Many software vendors license based on physical cores. Configurable constrained cores allow organizations to align VM configurations with licensing requirements.
- **Resource Optimization:**  
  Organizations can avoid over-provisioning and reduce costs by allocating only the necessary number of vCores.

---

### Important Considerations and Limitations

- **Performance Impact:**  
  Disabling SMT/HT may reduce overall throughput for multi-threaded workloads but can improve performance consistency for single-threaded or core-bound applications.
- **VM Size Compatibility:**  
  Not all VM sizes may support these customization features. Users should verify compatibility before deployment.
- **Billing:**  
  Billing is based on the number of vCores provisioned, not the underlying hardware. Ensure configurations align with budgetary constraints.
- **Licensing:**  
  Adjusting vCore counts may affect software licensing; validate compliance with vendor agreements.

---

### Integration with Related Azure Services

- **Azure Resource Manager (ARM):**  
  vCore customization is fully integrated with ARM templates, enabling automated and repeatable deployments.
- **Azure Portal & CLI:**  
  Administrators can configure these features directly through the Azure Portal or CLI, simplifying management.
- **Monitoring & Management:**  
  Azure Monitor and related tools can track VM performance

---

### 6. Generally Available: BYON (Bring Your Own NIC) in Azure Site Recovery

**Published**: August 19, 2026 16:36:30 UTC
**Link**: [Generally Available: BYON (Bring Your Own NIC) in Azure Site Recovery](https://azure.microsoft.com/updates?id=569515)

**Update ID**: 569515
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery, Feature

**Summary**:

- What was updated  
Azure Site Recovery now supports Bring Your Own NIC (BYON) for Azure-to-Azure disaster recovery scenarios.

- Key changes or new features  
You can now attach an existing, pre-provisioned Network Interface Card (NIC) in the target region during test-failover and failover operations. This allows you to retain custom networking configurations, such as static IP addresses, network security groups, and other settings associated with the NIC. Previously, Azure Site Recovery would create a new NIC during failover, requiring manual reconfiguration.

- Target audience affected  
This update is relevant for IT professionals managing disaster recovery, network administrators, and developers responsible for Azure infrastructure automation and configuration. It is especially useful for organizations with strict networking requirements or those leveraging Infrastructure as Code (IaC) for environment consistency.

- Important notes if any  
To use BYON, you must pre-provision the NIC in the target region before initiating failover or test-failover. Ensure that the NIC is not attached to any other VM and is configured with the necessary network settings. This feature enhances automation, reduces manual intervention, and helps maintain compliance with organizational networking policies.

For more details, see the official update: https://azure.microsoft.com/updates?id=569515

**Details**:

**Azure Update Report: Generally Available – BYON (Bring Your Own NIC) in Azure Site Recovery**

**Background and Purpose of the Update:**  
Azure Site Recovery (ASR) is a disaster recovery solution that enables replication, failover, and recovery of workloads across Azure regions. Previously, during failover or test-failover in Azure-to-Azure scenarios, ASR automatically created and attached a new Network Interface Card (NIC) to the recovered VM. This often resulted in loss of custom networking configurations, IP reservations, and security settings, requiring additional post-failover configuration. The purpose of this update is to provide greater control and flexibility by allowing users to bring and attach a pre-provisioned NIC in the target region, thereby preserving networking configurations and reducing recovery time.

**Specific Features and Detailed Changes:**  
The update introduces the ability to use an existing, pre-provisioned NIC for both test-failover and actual failover operations in Azure-to-Azure disaster recovery scenarios. Users can now select a NIC that has been configured in advance with desired settings such as IP address, subnet, network security group (NSG), and other network properties. This feature is generally available and can be leveraged during the recovery process to ensure that the VM retains its network identity and configuration.

**Technical Mechanisms and Implementation Methods:**  
The implementation allows users to specify a pre-provisioned NIC in the target Azure region when configuring recovery settings for a protected VM in ASR. During failover or test-failover, ASR will attach the specified NIC to the recovered VM instead of creating a new NIC. This preserves all custom configurations associated with the NIC, including static IP assignments, NSG rules, and any other network-related settings. The process is managed through the Azure portal or via automation using Azure Resource Manager templates and APIs.

**Use Cases and Application Scenarios:**  
- **Preserving Network Configurations:** Enterprises with complex networking requirements can pre-configure NICs with specific IP addresses, DNS settings, and NSG rules, ensuring that recovered VMs maintain their network identity and security posture.
- **IP Reservation:** Organizations needing to reserve IP addresses for compliance or application requirements can pre-provision NICs with static IPs, which are retained during failover.
- **Simplified Recovery:** Reduces manual post-failover configuration, accelerating recovery time and minimizing downtime.
- **Testing Scenarios:** Enables realistic test-failover operations by using production-like network settings, improving the accuracy of disaster recovery tests.

**Important Considerations and Limitations:**  
- The feature is applicable only in Azure-to-Azure recovery scenarios.
- The pre-provisioned NIC must exist in the target region and be compatible with the VM size and configuration.
- Users must ensure that the NIC is not attached to any other VM prior to failover.
- Network settings such as NSG, IP address, and subnet must be validated for compatibility with the recovered VM.
- There may be limitations regarding the number of NICs supported per VM, depending on VM size.

**Integration with Related Azure Services:**  
BYON NIC in ASR integrates seamlessly with Azure Virtual Network, Network Security Groups, and Azure Resource Manager. It enhances disaster recovery workflows by enabling tighter integration with network management and security services, and supports automation through ARM templates and Azure APIs. This update complements existing ASR features, providing a more robust and customizable recovery solution.

**Summary Sentence:**  
Azure Site Recovery now supports attaching pre-provisioned NICs during failover and test-failover in Azure-to-Azure scenarios, enabling preservation of custom network configurations and reducing post-recovery setup time.

---


*This report was automatically generated - 2026-08-20 03:05:29 UTC*