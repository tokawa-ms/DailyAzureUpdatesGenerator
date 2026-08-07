# August 07, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 07, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Announcing:  Azure Databricks Genie One and Genie Agents Free Usage Extended Through January 31, 2027 

**Published**: August 06, 2026 19:41:52 UTC
**Link**: [Announcing:  Azure Databricks Genie One and Genie Agents Free Usage Extended Through January 31, 2027 ](https://azure.microsoft.com/updates?id=568964)

**Update ID**: 568964
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Analytics, Azure Databricks, Announcement

**Summary**:

- What was updated  
The free usage period for Genie One and Genie Agents in Azure Databricks has been extended.

- Key changes or new features  
The promotional free usage for Genie One and Genie Agents is now available until January 31, 2027, instead of the previous end date of July 31, 2026. During this extended period, budget controls (such as spending limits or quotas) do not apply to these products, allowing unrestricted usage within the promotion.

- Target audience affected  
This update impacts developers, data engineers, and IT professionals who use Azure Databricks and are leveraging Genie One and Genie Agents for data analytics, AI, and automation workflows.

- Important notes if any  
Users can continue to use Genie One and Genie Agents free of charge until January 31, 2027, without budget restrictions. This extension provides more time to experiment, develop, and deploy solutions using these tools. However, after the promotional period ends, standard pricing and budget controls will likely resume. Organizations should plan accordingly for future costs and monitor updates for any changes to the promotion.

**Details**:

**Azure Update Technical Explanation: Extension of Free Usage for Azure Databricks Genie One and Genie Agents**

---

**Background and Purpose of the Update**

The update announces an extension of the free usage period for Genie One and Genie Agents within Azure Databricks. Originally, the free usage promotion was set to end on July 31, 2026. With this update, the free usage period is now extended through January 31, 2027. The purpose of this extension is to provide users with continued, cost-free access to Genie One and Genie Agents, supporting broader adoption and experimentation without financial barriers.

---

**Specific Features and Detailed Changes**

- **Extended Free Usage:** Azure Databricks users can now utilize Genie One and Genie Agents at no cost until January 31, 2027.
- **Budget Controls:** During this promotional period, Azure budget controls do not apply to Genie One and Genie Agents. This means that usage of these products will not be counted against any Azure cost management or budget thresholds set within the Azure portal.
- **Promotion Coverage:** The promotion applies to all users of Genie One and Genie Agents within the Azure Databricks environment.

---

**Technical Mechanisms and Implementation Methods**

- **Service Activation:** Genie One and Genie Agents are available as integrated features within Azure Databricks. Users can activate and use these services directly from the Databricks workspace without incurring charges during the promotional period.
- **Billing Exclusion:** The Azure billing system is configured to exclude Genie One and Genie Agents from cost calculations and budget alerts for the duration of the promotion. This is implemented at the platform level, ensuring seamless usage without manual intervention.
- **Access Control:** Standard Azure Databricks authentication and role-based access control (RBAC) mechanisms continue to govern access to Genie One and Genie Agents.

---

**Use Cases and Application Scenarios**

- **AI and Data Engineering:** Genie One and Genie Agents are designed to enhance productivity for data engineers, data scientists, and AI practitioners by automating and streamlining data workflows within Databricks.
- **Experimentation and Pilot Projects:** The free usage period enables teams to experiment with Genie One and Genie Agents for proof-of-concept projects, pilot deployments, and evaluation of advanced automation features without budget constraints.
- **Integration with Data Pipelines:** Organizations can integrate Genie One and Genie Agents into their existing Databricks pipelines to automate routine tasks, monitor data quality, or facilitate advanced analytics.

---

**Important Considerations and Limitations**

- **Budget Controls Disabled:** Since budget controls do not apply, organizations should monitor usage independently if they require internal tracking, as Azure’s built-in budget alerts will not trigger for Genie One and Genie Agents during the promotion.
- **Promotion End Date:** After January 31, 2027, standard billing and budget control mechanisms will resume unless further updates are announced.
- **Scope of Promotion:** The promotion is limited to Genie One and Genie Agents within Azure Databricks and does not extend to other Databricks features or Azure services.

---

**Integration with Related Azure Services**

- **Azure Databricks:** Genie One and Genie Agents are natively integrated into Azure Databricks, leveraging its unified analytics platform.
- **Azure Cost Management:** While budget controls are disabled for these products during the promotion, integration with Azure Cost Management remains for other Databricks and Azure resources.
- **Security and Compliance:** All activities involving Genie One and Genie Agents are subject to Azure’s security, compliance, and access control frameworks.

---

**Summary Sentence**

Free usage of Genie One and Genie Agents in Azure Databricks is now extended through January 31, 2027, with budget controls not applying during this promotional period.

---

### 2. Public Preview: Migrate from AWS FSx for Windows File Server to Azure Files with Azure Storage Mover

**Published**: August 06, 2026 16:40:19 UTC
**Link**: [Public Preview: Migrate from AWS FSx for Windows File Server to Azure Files with Azure Storage Mover](https://azure.microsoft.com/updates?id=567979)

**Update ID**: 567979
**Data source**: Azure Updates API

**Categories**: In preview, Migration, Storage, Azure Storage Mover, Feature

**Summary**:

- What was updated  
Azure Storage Mover now supports agentless, cloud-to-cloud migration from AWS FSx for Windows File Server (SMB) to Azure Files (SMB), available in public preview.

- Key changes or new features  
This update enables seamless migration of Windows file shares from AWS FSx to Azure Files without the need to deploy or manage migration agents. The migration process is fully cloud-based and supports SMB protocol, simplifying the transition for organizations moving workloads from AWS to Azure.

- Target audience affected  
Developers and IT professionals responsible for cloud storage management, migration planning, and hybrid cloud environments. Organizations currently using AWS FSx for Windows File Server and considering or planning migration to Azure Files will benefit most.

- Important notes if any  
The feature is currently in public preview, so production use should be carefully evaluated. This agentless migration reduces operational overhead and accelerates migration timelines. Users should review Azure Storage Mover documentation for supported scenarios, limitations, and best practices before initiating migration. No additional infrastructure is required, making it easier to adopt and scale migrations.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Migrate from AWS FSx for Windows File Server to Azure Files with Azure Storage Mover  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=567979)

---

### Background and Purpose of the Update

This update introduces a new capability in Azure Storage Mover, now in public preview, enabling agentless, cloud-to-cloud migration from AWS FSx for Windows File Server (SMB) to Azure Files (SMB). The primary purpose is to simplify and accelerate the migration process for organizations moving Windows file shares from AWS FSx to Azure Files, eliminating the need to deploy or manage migration agents or infrastructure.

---

### Specific Features and Detailed Changes

- **Agentless Migration:** Azure Storage Mover can now perform migrations directly between cloud environments (AWS to Azure) without requiring the installation or management of migration agents on-premises or in the cloud.
- **SMB Protocol Support:** The migration supports the SMB protocol, ensuring compatibility with Windows file shares on both AWS FSx and Azure Files.
- **Cloud-to-Cloud Workflow:** The migration process is fully managed within Azure Storage Mover, streamlining the transition from AWS FSx for Windows File Server to Azure Files.

---

### Technical Mechanisms and Implementation Methods

- **Azure Storage Mover Service:** The migration leverages Azure Storage Mover’s cloud-based orchestration and data movement capabilities. The service connects to the source AWS FSx for Windows File Server (over SMB) and the destination Azure Files share (also over SMB).
- **No Agent Deployment:** Since the migration is agentless, users do not need to provision or maintain any additional compute resources or install software on the source or destination environments.
- **Preview Feature:** As this is a public preview, the feature set may be subject to change, and users should evaluate its suitability for production workloads.

---

### Use Cases and Application Scenarios

- **Cloud-to-Cloud File Share Migration:** Organizations seeking to transition from AWS cloud services to Azure can use this feature to migrate Windows file shares efficiently.
- **Data Center Exit or Consolidation:** Enterprises consolidating cloud services or exiting AWS infrastructure can move file-based workloads to Azure Files with minimal operational overhead.
- **Hybrid and Multi-Cloud Strategies:** Businesses adopting hybrid or multi-cloud strategies can leverage this migration path to unify file storage under Azure management.

---

### Important Considerations and Limitations

- **Public Preview Status:** The feature is currently in public preview, which may imply limited support, potential changes, and not all production scenarios are recommended.
- **SMB Protocol Requirement:** Both source and destination must support SMB, as the migration is designed for SMB-based file shares.
- **Service Availability:** Users should verify regional availability and any preview-specific constraints before planning large-scale migrations.
- **No Agent Management:** While agentless migration reduces operational complexity, users should ensure network connectivity and permissions between AWS FSx and Azure Files are properly configured.

---

### Integration with Related Azure Services

- **Azure Files:** The destination for migrated data, providing fully managed SMB file shares in Azure.
- **Azure Storage Mover:** Acts as the central migration orchestration service, integrating with Azure management and monitoring tools.
- **Azure Security and Compliance:** Post-migration, organizations can leverage Azure’s security, backup, and compliance features for their file shares.

---

**Summary:**  
Azure Storage Mover now offers public preview support for agentless, cloud-to-cloud migration of Windows file shares from AWS FSx for Windows File Server to Azure Files, streamlining the transition process without the need to deploy or manage migration agents.

---


*This report was automatically generated - 2026-08-07 03:02:10 UTC*