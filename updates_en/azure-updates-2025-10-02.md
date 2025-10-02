# October 02, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 02, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: MSSQL extension integration with Microsoft Fabric 

**Published**: October 01, 2025 17:30:57 UTC
**Link**: [Public Preview: MSSQL extension integration with Microsoft Fabric ](https://azure.microsoft.com/updates?id=503646)

**Update ID**: 503646
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Analytics, Azure SQL Database, Microsoft Fabric, Features

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code (VS Code) now supports integration with Microsoft Fabric, enabling direct connectivity to Fabric SQL databases within the development environment.

- Key changes or new features  
A new Fabric connectivity option has been added to the Connection Dialog in the MSSQL extension. Developers can now sign in using Microsoft Entra ID to authenticate seamlessly. Once connected, users can browse and interact with SQL databases hosted in Microsoft Fabric directly from VS Code, streamlining database development and management workflows.

- Target audience affected  
This update primarily benefits developers and IT professionals who use VS Code for database development and management, especially those working with Microsoft Fabric and Azure SQL databases.

- Important notes if any  
This feature is currently in public preview, so users should expect potential changes and provide feedback. Proper Microsoft Entra ID credentials are required for authentication. Integration aims to improve productivity by consolidating database access and development tools within VS Code.

**Details**:

The recent public preview update introduces integration of the MSSQL extension for Visual Studio Code (VS Code) with Microsoft Fabric, enabling developers to seamlessly incorporate Fabric SQL databases into their development workflows. This enhancement addresses the need for streamlined access and management of Fabric data sources directly within a popular code editor, improving productivity and operational efficiency for data professionals and developers working with Fabric’s analytics and data engineering capabilities.

**Background and Purpose**  
Microsoft Fabric is a unified analytics platform designed to simplify data engineering, data warehousing, data science, and real-time analytics. Prior to this update, accessing Fabric SQL databases required separate tools or portals, which could disrupt developer workflows. The MSSQL extension for VS Code is widely used for managing SQL Server and Azure SQL databases. Integrating Fabric connectivity into this extension aims to consolidate database management and development tasks into a single environment, reducing context switching and accelerating development cycles.

**Specific Features and Detailed Changes**  
- **Fabric Connectivity Option:** A new option appears in the MSSQL extension’s Connection Dialog, allowing users to connect directly to Microsoft Fabric SQL databases.  
- **Microsoft Entra ID Authentication:** Users authenticate via Microsoft Entra ID (formerly Azure Active Directory), ensuring secure, enterprise-grade identity management and single sign-on capabilities.  
- **Fabric Resource Browsing:** Once connected, developers can browse Fabric SQL databases, schemas, tables, and other relevant objects within the VS Code interface, similar to traditional SQL Server connections.  
- **Query and Development Support:** Users can write, execute, and manage SQL queries against Fabric databases, leveraging the extension’s existing features such as IntelliSense, syntax highlighting, and query result visualization.  

**Technical Mechanisms and Implementation Methods**  
The integration leverages Microsoft Entra ID for authentication, using OAuth 2.0 protocols to securely obtain access tokens that authorize VS Code to interact with Fabric resources. The MSSQL extension’s connection management layer has been extended to recognize Fabric endpoints and handle the specific API calls needed to enumerate and query Fabric SQL objects. Communication with Fabric services likely uses REST APIs or dedicated Fabric SQL endpoints, abstracted within the extension to provide a seamless experience identical to connecting to traditional SQL databases.

**Use Cases and Application Scenarios**  
- **Data Engineering and Analytics Development:** Data engineers can develop and test SQL scripts directly against Fabric data lakes and warehouses without leaving VS Code.  
- **Integrated Data Workflows:** Developers building data applications or pipelines that consume Fabric data can maintain all code and queries in one environment, improving traceability and version control.  
- **Rapid Prototyping and Exploration:** Analysts and data scientists can quickly explore Fabric datasets and run ad hoc queries during data exploration phases.  
- **DevOps and CI/CD Pipelines:** Integration with VS Code facilitates embedding Fabric SQL scripts into source control and automated deployment workflows.  

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, some functionality may be limited or subject to change, and users should test in non-production environments initially.  
- **Authentication Requirements:** Microsoft Entra ID is mandatory, so organizations must have appropriate identity configurations and permissions set up.  
- **Feature Parity:** Not all advanced Fabric management features may be available through the extension; complex administrative tasks may still require the Fabric portal or CLI tools.  
- **Performance and Connectivity:** Query performance depends on network conditions and Fabric service responsiveness; local caching or offline capabilities are not indicated.  

**Integration with Related Azure Services**  
This update complements Azure Synapse and Azure Data Factory by enabling direct SQL development against Fabric, which itself integrates multiple Azure data services under one platform. The use of Microsoft Entra ID aligns with Azure’s identity and access management strategy, ensuring consistent security policies across Azure resources. Additionally, VS Code’s extensibility allows combining this Fabric integration with other Azure extensions (e.g., Azure Storage, Azure Functions) to build end-to-end data solutions.

In summary, the MSSQL extension’s integration with Microsoft Fabric

---

### 2. Retirement: Azure Machine Learning - Data labeling Deprecation

**Published**: October 01, 2025 17:30:57 UTC
**Link**: [Retirement: Azure Machine Learning - Data labeling Deprecation](https://azure.microsoft.com/updates?id=501692)

**Update ID**: 501692
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements

**Summary**:

- What was updated  
Azure Machine Learning’s built-in Data Labeling feature is being retired, with official end-of-support on September 30, 2026.

- Key changes or new features  
The native data labeling service within Azure Machine Learning will no longer be available after the retirement date. Users are advised to transition to third-party data labeling providers before September 30, 2026. Until then, the service remains fully operational without disruption.

- Target audience affected  
Developers and IT professionals who leverage Azure Machine Learning’s data labeling capabilities for preparing and annotating datasets in machine learning workflows.

- Important notes if any  
Plan your migration strategy early to avoid service interruption after September 30, 2026. Evaluate and integrate third-party data labeling solutions compatible with your ML pipelines. Existing labeled data and workflows should be reviewed to ensure smooth transition. For more details, refer to the official Azure update page.

**Details**:

The Azure update announces the planned retirement of the Azure Machine Learning Data Labeling service effective September 30, 2026, urging users to transition to third-party data labeling providers before this date. This deprecation reflects Microsoft’s strategic decision to streamline Azure Machine Learning offerings and encourage integration with specialized external labeling solutions.

**Background and Purpose:**  
Azure Machine Learning Data Labeling was introduced to facilitate the creation of high-quality labeled datasets essential for supervised machine learning model training. As the AI ecosystem has matured, numerous specialized third-party data labeling platforms have emerged, offering advanced annotation tools, scalable workforce management, and domain-specific labeling capabilities. Microsoft’s decision to retire this native service aims to optimize resource allocation and encourage customers to leverage these mature, dedicated providers that often provide richer features and better cost-effectiveness.

**Specific Features and Detailed Changes:**  
The core feature being deprecated is the integrated data labeling workspace within Azure Machine Learning, which allowed users to create labeling projects, assign tasks to labelers, and manage labeling workflows directly in the Azure portal. Post-retirement, this functionality will no longer be available, and users must rely on external providers for dataset annotation. Until September 30, 2026, the service remains fully operational without disruption, allowing ample time for migration planning.

**Technical Mechanisms and Implementation Methods:**  
Currently, Azure Machine Learning Data Labeling integrates tightly with datasets stored in Azure Blob Storage or Azure Data Lake, enabling seamless import/export of data for labeling. The service supports various data types including images, text, and videos, and offers labeling interfaces for manual annotation or semi-automated labeling using pre-labeling models.

After retirement, users will need to export their datasets from Azure storage accounts and ingest them into third-party labeling platforms. Integration typically involves using APIs or SDKs provided by these vendors to upload raw data and download labeled outputs. Subsequently, labeled datasets can be re-imported into Azure Machine Learning for model training. Automation scripts and Azure Data Factory pipelines can facilitate this data transfer and synchronization process.

**Use Cases and Application Scenarios:**  
This service was primarily used in scenarios requiring supervised learning, such as computer vision (image classification, object detection), natural language processing (text classification, entity recognition), and video analytics. Organizations building custom AI models for industries like healthcare, retail, and autonomous vehicles leveraged this service to generate training data.

Post-retirement, these use cases remain valid but will depend on external labeling solutions. Enterprises with large-scale or highly specialized labeling needs may benefit from providers offering workforce management, quality control workflows, and domain expertise.

**Important Considerations and Limitations:**  
- Migration Planning: Organizations must plan data export and integration with third-party providers well before the retirement date to avoid disruption.  
- Data Security and Compliance: When using external labeling services, ensure compliance with data governance policies, especially for sensitive or regulated data.  
- Cost Implications: Third-party services may have different pricing models; budget adjustments may be necessary.  
- Workflow Changes: Existing labeling workflows embedded in Azure ML pipelines will require redesign to accommodate external tools and data flows.

**Integration with Related Azure Services:**  
While the native data labeling feature is deprecated, Azure Machine Learning continues to support model training, deployment, and MLOps workflows. Users can integrate labeled datasets from third-party providers stored in Azure Blob Storage or Data Lake. Azure Data Factory and Logic Apps can automate data movement between Azure and external services. Additionally, Azure Cognitive Services may offer pre-built AI capabilities that reduce the need for custom labeling in some scenarios.

In summary, the retirement of Azure Machine Learning Data Labeling by September 30, 2026, necessitates transitioning to third-party annotation platforms, requiring careful migration planning, workflow adjustments, and consideration of data governance, while continuing to leverage Azure’s robust ML infrastructure for downstream model development and deployment.

---

### 3. Retirement: Azure Network Policy Manager (NPM) for Linux nodes on AKS to Be Retired by September 30, 2028

**Published**: October 01, 2025 17:15:18 UTC
**Link**: [Retirement: Azure Network Policy Manager (NPM) for Linux nodes on AKS to Be Retired by September 30, 2028](https://azure.microsoft.com/updates?id=500268)

**Update ID**: 500268
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Network Policy Manager (NPM) support for Linux nodes on Azure Kubernetes Service (AKS), effective September 30, 2028.

- Key changes or new features  
After this date, NPM will no longer be supported on Linux nodes in AKS clusters. Users must migrate their network policies from NPM to the Cilium Network Policy framework, which offers enhanced security and observability features for Kubernetes networking.

- Target audience affected  
This update primarily affects developers and IT professionals managing AKS clusters with Linux nodes that currently use NPM for network policy enforcement.

- Important notes if any  
To avoid service disruptions, plan and execute the migration to Cilium Network Policy well before the retirement date. Cilium provides advanced capabilities such as eBPF-based enforcement, improved scalability, and richer network visibility, making it a recommended replacement. Review your cluster configurations and test workloads during migration to ensure compatibility and performance stability.

For detailed guidance, refer to the official Azure update: https://azure.microsoft.com/updates?id=500268

**Details**:

The Azure update announces the planned retirement of Azure Network Policy Manager (NPM) support for Linux nodes in Azure Kubernetes Service (AKS) by September 30, 2028, urging users to migrate to Cilium Network Policy to ensure uninterrupted network policy enforcement and cluster security.

**Background and Purpose:**  
Azure Network Policy Manager (NPM) has been the default Kubernetes network policy enforcement solution for AKS Linux nodes, providing basic Layer 3/4 network segmentation using iptables-based mechanisms. However, evolving Kubernetes networking demands and the need for more scalable, performant, and feature-rich network policy enforcement have driven Azure to adopt Cilium, a more advanced eBPF-based networking and security solution. The retirement of NPM aligns with this strategic shift to modernize AKS networking, improve observability, and support advanced use cases such as Layer 7 policies and network visibility.

**Specific Features and Detailed Changes:**  
- **End of Support Date:** September 30, 2028, after which NPM will no longer be supported on Linux nodes in AKS.  
- **Migration Path:** Users must transition existing AKS clusters from NPM to Cilium Network Policy.  
- **Cilium Advantages:** Cilium leverages eBPF (extended Berkeley Packet Filter) technology in the Linux kernel to provide high-performance, scalable, and fine-grained network policy enforcement, including Layer 7 (application layer) policies, transparent encryption, and enhanced observability.  
- **Deprecation of iptables-based NPM:** NPM’s iptables-based approach will be phased out in favor of Cilium’s eBPF-based datapath, which reduces complexity and improves throughput and latency.

**Technical Mechanisms and Implementation Methods:**  
- **NPM Architecture:** NPM uses iptables rules to enforce Kubernetes NetworkPolicies, which can become complex and less efficient at scale due to rule explosion and kernel overhead.  
- **Cilium Architecture:** Cilium uses eBPF programs loaded into the Linux kernel to dynamically enforce policies, perform load balancing, and provide network observability without the overhead of iptables chains.  
- **Migration Process:**  
  - Enable Cilium Network Policy add-on in AKS clusters via Azure CLI or ARM templates.  
  - Validate existing network policies for compatibility and translate any NPM-specific configurations if necessary.  
  - Gradually switch enforcement from NPM to Cilium, ensuring no disruption to workloads.  
  - Monitor cluster network behavior and performance post-migration using Cilium’s observability tools.  
- **Compatibility:** Cilium supports standard Kubernetes NetworkPolicy APIs and extends them with additional capabilities.

**Use Cases and Application Scenarios:**  
- **Security Compliance:** Enforcing fine-grained network segmentation and micro-segmentation within AKS clusters.  
- **Performance-Sensitive Applications:** Applications requiring low-latency networking and high throughput benefit from eBPF’s efficient packet processing.  
- **Advanced Network Policies:** Use of Layer 7 policies to control HTTP, DNS, and other protocols beyond basic IP/port filtering.  
- **Observability and Troubleshooting:** Real-time network flow visibility and diagnostics using Cilium’s Hubble observability platform.  
- **Multi-Tenancy and Service Mesh Integration:** Enhanced support for multi-tenant environments and integration with service meshes like Istio.

**Important Considerations and Limitations:**  
- **Migration Planning:** Migration should be planned well before the 2028 deadline to avoid service disruptions.  
- **Kernel and OS Requirements:** Cilium requires Linux kernel version 4.8+ with eBPF support; verify node OS compatibility.  
- **Policy Compatibility:** While Cilium supports standard Kubernetes NetworkPolicy, some NPM-specific features or customizations may require adaptation.  
- **Operational Changes:** Teams must familiarize themselves with Cilium’s tooling, observability, and policy model.  
- **Resource Overhead:** Although efficient, eBPF programs consume

---

### 4. Public Preview: Azure SQL updates for late September 2025 

**Published**: October 01, 2025 16:00:52 UTC
**Link**: [Public Preview: Azure SQL updates for late September 2025 ](https://azure.microsoft.com/updates?id=503612)

**Update ID**: 503612
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Azure SQL received an update in late September 2025 introducing enhanced protection for long-term retention (LTR) backups.

- Key changes or new features  
The primary enhancement is the addition of immutability for LTR backups, which safeguards these backups against ransomware attacks. This immutability feature ensures that once backups are created, they cannot be altered or deleted until the retention period expires, providing a robust defense mechanism to protect critical backup data from malicious tampering or deletion.

- Target audience affected  
This update is particularly relevant for developers, database administrators, and IT security professionals managing Azure SQL databases and responsible for backup and disaster recovery strategies.

- Important notes if any  
The immutability feature for LTR backups is currently in public preview, allowing customers to test and provide feedback before general availability. It is recommended to review the implementation guidelines and limitations in the official documentation to ensure compatibility with existing backup policies and compliance requirements.

For more details, visit: https://azure.microsoft.com/updates?id=503612

**Details**:

In late September 2025, Azure SQL introduced a public preview feature enhancing the security of long-term retention (LTR) backups by enabling immutability to protect against ransomware attacks. This update addresses the growing need for robust data protection mechanisms in cloud database backup strategies, particularly as ransomware threats increasingly target backup data to prevent recovery.

**Background and Purpose:**  
Long-term retention backups are critical for compliance, disaster recovery, and data archival purposes. However, traditional backup storage can be vulnerable to ransomware attacks that encrypt or delete backup files, undermining recovery efforts. The purpose of this update is to safeguard LTR backups by making them immutable, meaning once written, the backup files cannot be altered or deleted within a specified retention period, thereby ensuring data integrity and availability even in the event of a ransomware attack.

**Specific Features and Detailed Changes:**  
- **Immutability for LTR Backups:** Azure SQL now supports setting immutability policies on LTR backups stored in Azure Blob Storage.  
- **Write-Once-Read-Many (WORM) Compliance:** The backups adhere to WORM storage principles, preventing modification or deletion during the retention window.  
- **Configurable Retention Periods:** Users can define the immutability period aligned with organizational compliance requirements.  
- **Integration with Azure Blob Storage Immutable Storage:** The feature leverages Azure Blob Storage’s native immutable storage capabilities, including time-based retention policies.

**Technical Mechanisms and Implementation Methods:**  
- When an LTR backup is created, it is stored in a dedicated Azure Blob Storage container configured with immutable storage policies.  
- The immutability policy enforces a retention period during which the backup blob cannot be deleted or overwritten.  
- Azure SQL manages the lifecycle of these backups, ensuring compliance with the immutability settings while maintaining seamless restore capabilities.  
- The implementation uses Azure Blob Storage’s native immutability features such as legal holds and time-based retention policies, integrated transparently with Azure SQL backup orchestration.

**Use Cases and Application Scenarios:**  
- **Ransomware Resilience:** Organizations can ensure that backup data remains intact and recoverable even if primary databases are compromised.  
- **Regulatory Compliance:** Industries with strict data retention requirements (e.g., finance, healthcare) benefit from immutable backups that meet audit and compliance standards.  
- **Disaster Recovery Planning:** Immutable backups provide a reliable fallback for restoring databases to a known good state without risk of tampering.  
- **Long-Term Archival:** Enterprises needing to retain data for extended periods can leverage immutability to guarantee data preservation.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview feature, it may have limitations in availability, region support, or functionality and should be tested thoroughly before production use.  
- **Retention Period Management:** Once set, immutability policies cannot be shortened or removed until the retention period expires, requiring careful planning.  
- **Cost Implications:** Immutable backups stored in Blob Storage may incur additional storage costs due to longer retention and storage class usage.  
- **Restore Operations:** While backups are immutable, restore operations remain fully supported; however, the immutability applies only to backup storage, not to the restored database.

**Integration with Related Azure Services:**  
- **Azure Blob Storage:** The update leverages Azure Blob Storage’s immutable storage capabilities, integrating seamlessly with existing storage accounts used for LTR backups.  
- **Azure SQL Database and Managed Instances:** The feature is applicable across Azure SQL Database and Managed Instance LTR backups, maintaining consistency across deployment models.  
- **Azure Security and Compliance Tools:** Organizations can monitor and audit immutable backup policies using Azure Security Center and Azure Policy for governance.  
- **Azure Backup and Recovery Solutions:** This enhancement complements Azure Backup strategies by providing an additional layer of protection specifically for SQL database backups.

In summary, the September 2025 public preview update for Azure SQL introduces immutability for long-term

---


*This report was automatically generated - 2025-10-02 03:02:15 UTC*