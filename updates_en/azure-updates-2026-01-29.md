# January 29, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: January 29, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Retirement: Support for Python 3.10 ends on October 1, 2026 – upgrade your Azure Functions apps to Python 3.13 

**Published**: January 28, 2026 23:15:47 UTC
**Link**: [Retirement: Support for Python 3.10 ends on October 1, 2026 – upgrade your Azure Functions apps to Python 3.13 ](https://azure.microsoft.com/updates?id=545771)

**Update ID**: 545771
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions will retire support for Python 3.10 starting October 1, 2026.

- Key changes or new features  
After this date, Python 3.10 apps on Azure Functions will continue to run but will no longer receive security patches or performance improvements. Developers are advised to upgrade their Azure Functions apps to Python 3.13 to maintain support, security, and optimal performance.

- Target audience affected  
Developers and IT professionals who build, deploy, or maintain Azure Functions apps using Python 3.10.

- Important notes if any  
This change aligns with the official end of community support for Python 3.10. Upgrading to Python 3.13 ensures continued security updates and access to the latest runtime enhancements. Plan your migration ahead of the October 2026 deadline to avoid potential vulnerabilities and performance degradation.

For more details, visit: https://azure.microsoft.com/updates?id=545771

**Details**:

The Azure update announces the retirement of support for Python 3.10 in Azure Functions effective October 1, 2026, urging developers to upgrade their Azure Functions apps to Python 3.13 to maintain security, performance, and support compliance.

**Background and Purpose:**  
This update aligns Azure Functions’ Python runtime support lifecycle with the broader Python community’s end-of-life schedule for Python 3.10. As Python 3.10 reaches end-of-life status, it no longer receives official security patches or performance improvements from the Python Software Foundation. Consequently, Azure is retiring support to ensure that Azure Functions customers run their serverless workloads on a secure, performant, and actively maintained Python runtime. The purpose is to encourage proactive migration to Python 3.13, which benefits from ongoing updates and improvements.

**Specific Features and Detailed Changes:**  
- **End of Support Date:** October 1, 2026, after which Python 3.10 runtime will no longer receive security updates or performance optimizations in Azure Functions.  
- **Upgrade Path:** Developers must update their Azure Functions apps to use Python 3.13, which is the supported runtime version post-retirement.  
- **Runtime Behavior:** Existing apps running on Python 3.10 will continue to function after the cutoff date but without any security patches or performance fixes, increasing risk exposure.  
- **Deprecation of Python 3.10 Images:** Azure Functions’ underlying container images and runtime environments for Python 3.10 will be deprecated and eventually removed.

**Technical Mechanisms and Implementation Methods:**  
- **Runtime Version Specification:** Azure Functions apps specify the Python runtime version via the `FUNCTIONS_WORKER_RUNTIME` and `pythonVersion` settings in the function app configuration or deployment files.  
- **Container and Platform Updates:** Azure updates the underlying platform images and runtime stacks to remove Python 3.10 support and provide Python 3.13 images.  
- **Migration Process:** Developers should update their local development environments, dependencies, and deployment pipelines to target Python 3.13. This includes testing for compatibility with Python 3.13 language features and library versions.  
- **CI/CD Pipelines:** Adjust build and release pipelines to use updated base images or runtime versions that support Python 3.13.  
- **Function App Configuration:** Modify the app settings or deployment templates (ARM, Bicep, Terraform) to specify Python 3.13 as the runtime version.

**Use Cases and Application Scenarios:**  
- Serverless applications using Azure Functions with Python 3.10 runtime, including event-driven processing, API backends, automation scripts, and data processing workflows.  
- Organizations leveraging Azure Functions for scalable, cost-effective compute that rely on Python for rapid development and integration with Azure services.  
- Scenarios requiring compliance with security policies that mandate supported and patched runtimes.

**Important Considerations and Limitations:**  
- **Compatibility Testing:** Python 3.13 introduces new language features and deprecations; thorough testing is necessary to ensure existing codebases are compatible.  
- **Dependency Updates:** Third-party libraries used in functions may need updates to versions compatible with Python 3.13.  
- **Potential Downtime:** Plan upgrades during maintenance windows to minimize disruption.  
- **No Forced Shutdown:** Azure will not forcibly stop Python 3.10 apps immediately after October 1, 2026, but running unsupported runtimes increases risk.  
- **Documentation and Support:** Review Azure Functions and Python runtime documentation for migration guidance and best practices.

**Integration with Related Azure Services:**  
- **Azure DevOps / GitHub Actions:** Update CI/CD workflows to build and deploy functions targeting Python 3.13.  
- **Azure Monitor and Application Insights:** Continue monitoring function performance and errors post-migration to detect runtime-related issues.  
- **Azure Container Registry (ACR):** If using custom container images for functions, rebuild and push

---

### 2. Generally Available: Azure AMD Turin Dasv7, Easv7, and Fasv7-series Virtual Machines    

**Published**: January 28, 2026 19:15:24 UTC
**Link**: [Generally Available: Azure AMD Turin Dasv7, Easv7, and Fasv7-series Virtual Machines    ](https://azure.microsoft.com/updates?id=552318)

**Update ID**: 552318
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines

**Summary**:

- What was updated  
Azure has announced the general availability of AMD-based Turin series virtual machines: Dasv7 and Dalsv7 (general purpose), Easv7 (memory-optimized), and Fasv7, Falsv7, Famsv7 (compute-optimized). These VM sizes now support configurations both with and without local disk storage.

- Key changes or new features  
These new VM series leverage AMD Milan processors, offering enhanced performance and cost efficiency for diverse workloads. The availability of local disk options provides flexibility in storage performance and persistence. The VMs are currently available in select Azure regions, including Australia East and Central.

- Target audience affected  
Developers and IT professionals seeking scalable, cost-effective VM options optimized for general purpose, memory-intensive, or compute-heavy applications will benefit. This is particularly relevant for workloads requiring AMD architecture advantages or local disk storage configurations.

- Important notes if any  
Availability is initially limited to specific regions; users should verify regional support before deployment. The inclusion of local disk support allows for improved I/O performance but may affect data persistence depending on VM lifecycle. Review workload requirements to choose appropriate VM series and storage options.

For more details, visit: https://azure.microsoft.com/updates?id=552318

**Details**:

The recent general availability (GA) of Azure AMD Turin-based Dasv7, Dalsv7, Easv7, Fasv7, Falsv7, and Famsv7 virtual machine (VM) series marks a significant expansion of Azure’s VM portfolio, offering enhanced performance and cost efficiency for diverse workloads. These VMs leverage AMD’s latest EPYC 9004-series processors (Turin), delivering improved compute power, memory bandwidth, and energy efficiency compared to previous generations.

**Background and Purpose**  
Azure continuously evolves its VM offerings to meet growing demands for scalable, cost-effective, and high-performance cloud compute resources. The AMD Turin-based VM series aims to provide a competitive alternative to Intel-based VMs, optimizing price-performance ratios for general-purpose, memory-optimized, and compute-optimized workloads. The introduction of these VMs with and without local disk support addresses varied storage latency and throughput requirements.

**Specific Features and Detailed Changes**  
- **VM Series and Types**:  
  - *Dasv7 and Dalsv7*: General-purpose VMs suitable for balanced CPU-to-memory workloads.  
  - *Easv7*: Memory-optimized VMs designed for high-memory workloads such as large databases and in-memory analytics.  
  - *Fasv7, Falsv7, Famsv7*: Compute-optimized VMs targeting CPU-intensive applications like batch processing, gaming, and high-performance computing (HPC).  
- **Processor**: All these VMs utilize AMD EPYC 9004-series (Turin) processors, providing up to 64 cores per VM with enhanced instructions per cycle (IPC) and energy efficiency.  
- **Local Disk Support**: Availability with and without local ephemeral storage gives flexibility for applications requiring low-latency temporary storage or those relying solely on remote storage options like Azure Managed Disks.  
- **Regional Availability**: Initially available in Australia East and Central regions, with planned expansion to additional Azure regions.  

**Technical Mechanisms and Implementation**  
These VMs are built on Azure’s hyper-scale infrastructure, integrating AMD EPYC Turin CPUs with Azure’s custom firmware and hypervisor optimizations. The local disk option uses NVMe-based ephemeral storage directly attached to the VM host, enabling high IOPS and low latency for temporary data. The VMs support Azure features such as Accelerated Networking, enabling enhanced network throughput and reduced jitter, and Azure Premium SSDs for persistent storage. They also integrate with Azure Monitor and Azure Security Center for observability and security compliance.

**Use Cases and Application Scenarios**  
- *General Purpose (Dasv7, Dalsv7)*: Web servers, enterprise applications, small to medium databases, and development/test environments.  
- *Memory Optimized (Easv7)*: Large relational databases (e.g., SQL Server, PostgreSQL), in-memory caches (e.g., Redis), real-time analytics, and SAP HANA workloads.  
- *Compute Optimized (Fasv7 series)*: High-performance computing, batch processing, gaming servers, video encoding, and AI inferencing workloads requiring high CPU throughput.  
- *Local Disk Support*: Suitable for workloads needing temporary scratch space, such as big data processing, caching layers, or ephemeral data storage during computations.  

**Important Considerations and Limitations**  
- Local ephemeral storage is non-persistent and data is lost on VM deallocation or host failure; critical data must be stored on durable Azure Managed Disks or Azure Blob Storage.  
- Regional availability is initially limited; customers should verify availability in their target regions.  
- Compatibility with existing VM extensions and Azure services should be validated, especially for specialized workloads or custom images.  
- Pricing and performance should be benchmarked against existing VM families to ensure cost-effectiveness for specific workloads.  

**Integration with Related Azure Services**  
- These VMs seamlessly integrate with Azure Virtual Network for secure connectivity and Azure Load

---

### 3. Generally Available: Azure Databricks Agent Bricks Knowledge Assistant

**Published**: January 28, 2026 18:45:08 UTC
**Link**: [Generally Available: Azure Databricks Agent Bricks Knowledge Assistant](https://azure.microsoft.com/updates?id=542455)

**Update ID**: 542455
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks

**Summary**:

- What was updated  
Azure Databricks introduced the Agent Bricks Knowledge Assistant, now generally available, enabling AI agent creation, deployment, and management directly within the Azure Databricks environment.

- Key changes or new features  
The update provides a unified platform combining data and AI capabilities to streamline the development of AI agents. It includes prebuilt components and templates that simplify building intelligent agents without extensive custom coding. This integration enhances productivity by allowing developers to leverage Databricks’ scalable data processing alongside AI models seamlessly.

- Target audience affected  
Developers, data scientists, and IT professionals working with Azure Databricks who want to build, deploy, and maintain AI-driven agents within their data workflows will benefit most from this feature.

- Important notes if any  
This feature leverages the existing Azure Databricks infrastructure, so users should ensure their workspace is updated to the latest version to access Agent Bricks. It is designed to accelerate AI agent development while maintaining security and governance within enterprise environments. For detailed implementation guidance, refer to the official Azure Databricks documentation.

**Details**:

The Azure Databricks Agent Bricks Knowledge Assistant, now generally available, introduces a powerful capability to build, deploy, and manage AI agents natively within the Azure Databricks environment by leveraging unified data and AI services. This update addresses the growing demand for integrated AI-driven automation and intelligent agent workflows directly on big data platforms, streamlining the development lifecycle and operational management of AI agents.

**Background and Purpose**  
As enterprises increasingly adopt AI to automate complex workflows and decision-making processes, there is a need to embed intelligent agents closer to data processing environments. Azure Databricks, a leading unified analytics platform, traditionally focuses on big data engineering, data science, and machine learning. However, integrating AI agents that can interact with data, perform tasks, and provide insights directly within Databricks clusters was a gap. The Agent Bricks Knowledge Assistant fills this gap by enabling AI agent creation and management without leaving the Databricks workspace, thus reducing context switching and accelerating AI-driven automation.

**Specific Features and Detailed Changes**  
- **Prebuilt Components:** The update provides prebuilt AI agent templates (“agent bricks”) that simplify the creation of conversational and task-oriented agents. These templates come with built-in natural language understanding (NLU), dialog management, and integration hooks.  
- **Unified Data and AI Integration:** Agents can seamlessly access and query data lakes, Delta Lake tables, and machine learning models hosted within Databricks, enabling context-aware responses and actions.  
- **Agent Lifecycle Management:** Tools for deploying, monitoring, updating, and scaling AI agents are integrated into the Databricks UI and APIs, facilitating operational control.  
- **Extensibility:** Developers can customize agent behavior using Python, Scala, or SQL, leveraging Databricks notebooks and jobs for orchestration.  
- **Security and Compliance:** The assistant supports Azure Active Directory (AAD) authentication and role-based access control (RBAC), ensuring secure agent operations aligned with enterprise policies.

**Technical Mechanisms and Implementation Methods**  
The Agent Bricks Knowledge Assistant is architected as a set of microservices and SDKs embedded within the Databricks runtime environment. It leverages Databricks’ existing compute clusters and integrates with Azure Cognitive Services for NLU and language understanding capabilities. Agents operate as managed workloads that can invoke Spark jobs, MLflow models, or REST APIs, enabling complex workflows. The assistant uses Delta Lake for state management and knowledge base storage, ensuring consistency and scalability. Developers interact with the assistant through Databricks notebooks or RESTful APIs, enabling programmatic control and automation.

**Use Cases and Application Scenarios**  
- **Data-Driven Chatbots:** Build chatbots that answer queries about datasets, generate reports, or provide operational insights by querying Delta Lake tables.  
- **Automated Data Operations:** Agents can trigger ETL pipelines, monitor data quality, and alert stakeholders based on predefined conditions.  
- **AI-Enhanced Analytics:** Integrate predictive models with conversational agents to provide recommendations or anomaly detection results interactively.  
- **DevOps Automation:** Automate cluster management, job scheduling, and incident response within Databricks through intelligent agents.  
- **Customer Support and Knowledge Management:** Deploy agents that assist internal teams by providing documentation, troubleshooting guides, or system status updates.

**Important Considerations and Limitations**  
- **Resource Overhead:** Running AI agents on Databricks clusters consumes compute resources; appropriate cluster sizing and cost management are necessary.  
- **Latency:** Real-time conversational responsiveness depends on cluster performance and network latency; optimization may be required for low-latency scenarios.  
- **Security:** While AAD and RBAC are supported, careful configuration is essential to prevent unauthorized data access through agents.  
- **Customization Complexity:** Advanced agent behaviors require proficiency in Databricks programming languages and AI concepts, which may necessitate training.  
- **Region Availability:** Features may initially be available in select Azure regions; verify availability for your deployment region

---

### 4. Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server  

**Published**: January 28, 2026 17:00:53 UTC
**Link**: [Generally Available: Latest PostgreSQL minor versions supported by Azure Database for PostgreSQL – Flexible Server  ](https://azure.microsoft.com/updates?id=550164)

**Update ID**: 550164
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports the latest minor versions of PostgreSQL: 18.1, 17.7, 16.11, 15.15, 14.20, and 13.23.

- Key changes or new features  
These updates include the most recent minor version releases for multiple major PostgreSQL versions, ensuring improved stability, security patches, and bug fixes. The minor version upgrades are automatically applied during Azure’s monthly planned maintenance windows, minimizing manual intervention.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure Flexible Server will benefit from enhanced performance, security, and compliance with the latest PostgreSQL minor releases. This is particularly relevant for teams prioritizing up-to-date database environments without downtime.

- Important notes if any  
Automatic minor version upgrades occur during planned maintenance, so users should plan accordingly. No action is required to enable these updates, but reviewing release notes for each PostgreSQL minor version is recommended to understand specific fixes or changes. This update helps maintain secure and reliable PostgreSQL deployments on Azure Flexible Server.

**Details**:

The recent Azure update announces the general availability of support for the latest PostgreSQL minor versions—18.1, 17.7, 16.11, 15.15, 14.20, and 13.23—on Azure Database for PostgreSQL – Flexible Server. This enhancement ensures that customers benefit from the most recent stability, security, and performance improvements delivered by the PostgreSQL community, with upgrades applied automatically during Azure’s monthly planned maintenance windows.

**Background and Purpose:**  
Azure Database for PostgreSQL – Flexible Server is a managed database service designed to offer high availability, scalability, and operational flexibility for PostgreSQL workloads. PostgreSQL minor version updates typically include critical bug fixes, security patches, and performance optimizations without introducing breaking changes. By supporting the latest minor versions, Azure ensures that customers run secure, stable, and optimized database instances with minimal administrative overhead. Automating these upgrades as part of monthly maintenance reduces manual intervention and helps maintain compliance with security best practices.

**Specific Features and Detailed Changes:**  
The update covers support for PostgreSQL minor versions 13.23 through 18.1, spanning multiple major versions. Each minor version includes cumulative fixes and enhancements such as improved query planner stability, security vulnerability patches (e.g., CVE mitigations), and fixes for edge-case bugs affecting replication, indexing, or data integrity. While no major feature changes occur in minor updates, these incremental improvements collectively enhance database reliability and performance.

**Technical Mechanisms and Implementation Methods:**  
Azure Database for PostgreSQL – Flexible Server employs a managed upgrade process integrated into its monthly planned maintenance cycle. During this window, the service automatically applies minor version upgrades to the underlying PostgreSQL engine with minimal downtime, leveraging rolling upgrade techniques and failover mechanisms where applicable. This process includes pre-upgrade validation, backup snapshots for recovery, and post-upgrade health checks to ensure service continuity. Customers can monitor upgrade status through Azure Portal or Azure CLI and configure maintenance windows to align with their operational requirements.

**Use Cases and Application Scenarios:**  
This update is particularly relevant for enterprises and developers running production workloads on PostgreSQL that require high availability and security compliance. Applications benefiting include web and mobile backends, analytics platforms, and SaaS solutions relying on PostgreSQL’s extensibility and robustness. By staying current with minor versions, customers reduce exposure to known vulnerabilities and improve overall system stability, which is critical for regulated industries and mission-critical applications.

**Important Considerations and Limitations:**  
While minor version upgrades are backward-compatible, customers should test application compatibility in staging environments before production rollout, especially if they use PostgreSQL extensions or custom configurations. The automatic upgrade process may cause brief service interruptions during maintenance windows, so planning for maintenance windows is essential. Additionally, major version upgrades remain a separate process requiring manual intervention and testing. Customers should also review Azure’s documentation for any region-specific availability or feature differences.

**Integration with Related Azure Services:**  
Azure Database for PostgreSQL – Flexible Server integrates seamlessly with Azure services such as Azure Monitor for performance and health metrics, Azure Backup for data protection, and Azure Active Directory for authentication. The update ensures that these integrations continue to function optimally with the latest PostgreSQL engine versions. Furthermore, compatibility with Azure Data Factory and Azure Synapse Analytics enables streamlined data movement and analytics workflows on up-to-date PostgreSQL instances.

In summary, the general availability of the latest PostgreSQL minor versions on Azure Database for PostgreSQL – Flexible Server enhances security, stability, and performance by automating critical engine updates during planned maintenance, thereby enabling IT professionals to maintain robust and compliant PostgreSQL deployments with minimal operational overhead.

---


*This report was automatically generated - 2026-01-29 03:02:29 UTC*