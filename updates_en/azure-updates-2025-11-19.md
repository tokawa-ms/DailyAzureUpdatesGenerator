# November 19, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 19, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 143 items

## Update List

### 1. Generally Available: Claude in Microsoft Foundry

**Published**: November 19, 2025 00:00:31 UTC
**Link**: [Generally Available: Claude in Microsoft Foundry](https://azure.microsoft.com/updates?id=532303)

**Update ID**: 532303
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Anthropic’s Claude AI models are now generally available within Microsoft Foundry, enhancing the platform’s unified frontier AI ecosystem.

- Key changes or new features  
Microsoft Foundry users can access multiple Claude models—Sonnet 4.5, Opus 4.1, and Haiku 4.5—offering advanced capabilities such as long-context reasoning, improved coding assistance, and multimodal comprehension. This integration enables enterprises to leverage cutting-edge AI for complex workflows, including natural language understanding and generation across diverse data types.

- Target audience affected  
Developers and IT professionals working in enterprise environments who utilize Microsoft Foundry for AI-driven applications, especially those focusing on advanced language models, coding automation, and multimodal AI solutions.

- Important notes if any  
The availability of Claude models within Microsoft Foundry provides a seamless, unified AI platform experience, simplifying integration and management of frontier AI technologies. Enterprises should evaluate these models to enhance their AI workloads requiring extended context handling and multimodal inputs. For detailed implementation guidance, refer to the official Microsoft Foundry documentation.

**Details**:

The recent Azure update announces the general availability of Anthropic’s Claude AI models within Microsoft Foundry, significantly enhancing the platform’s frontier AI capabilities by integrating advanced large language models (LLMs) designed for enterprise-grade applications.

**Background and Purpose:**  
Microsoft Foundry is a unified AI platform aimed at enabling enterprises to build, deploy, and manage AI solutions at scale. The integration of Anthropic’s Claude models—Claude Sonnet 4.5, Opus 4.1, and Haiku 4.5—addresses the growing demand for versatile, high-performance AI models that support complex reasoning, coding assistance, and multimodal inputs. This update expands Foundry’s AI ecosystem beyond Microsoft’s native models, providing customers with more options tailored to specific workloads and compliance needs.

**Specific Features and Detailed Changes:**  
- **Claude Sonnet 4.5:** Optimized for advanced long-context reasoning, enabling the processing of extended documents or conversations without losing context, which is critical for applications like legal analysis, research synthesis, and detailed report generation.  
- **Claude Opus 4.1:** Focused on coding tasks, this model offers enhanced capabilities for code generation, debugging, and explanation, supporting multiple programming languages and frameworks.  
- **Claude Haiku 4.5:** A multimodal model capable of understanding and generating content that combines text with other data types (e.g., images), facilitating richer AI interactions such as document summarization with embedded visuals or interactive chatbots.

**Technical Mechanisms and Implementation Methods:**  
These Claude models are hosted within Microsoft Foundry’s secure, scalable infrastructure, leveraging containerized deployments and managed Kubernetes clusters for orchestration. The models utilize Anthropic’s proprietary training techniques emphasizing safety, interpretability, and robustness. Enterprises can access these models via Foundry’s unified API layer, which abstracts model-specific complexities and provides consistent authentication, rate limiting, and telemetry. The integration supports fine-tuning and prompt engineering within Foundry’s development environment, allowing customization to domain-specific data and workflows.

**Use Cases and Application Scenarios:**  
- **Enterprise Knowledge Management:** Long-context reasoning models like Claude Sonnet 4.5 enable deep document analysis, summarization, and question answering across large corpora.  
- **Software Development:** Claude Opus 4.1 assists developers by generating code snippets, automating code reviews, and providing explanations, thus accelerating development cycles.  
- **Multimodal Customer Support:** Claude Haiku 4.5 can power chatbots that understand and respond to queries involving both text and images, improving customer interaction quality.  
- **Regulatory Compliance and Risk Analysis:** The models’ ability to process complex, lengthy documents aids in compliance monitoring and risk assessment workflows.

**Important Considerations and Limitations:**  
While Claude models are designed with safety and interpretability in mind, enterprises must still implement governance frameworks to monitor AI outputs, especially in regulated industries. Latency and cost implications should be evaluated based on workload size and frequency. Additionally, multimodal capabilities may require integration with data preprocessing pipelines to handle non-text inputs effectively. Data residency and privacy compliance must be ensured by leveraging Foundry’s security features and Azure’s regional availability.

**Integration with Related Azure Services:**  
Claude models in Foundry seamlessly integrate with Azure Data Lake for scalable data storage, Azure Synapse Analytics for data processing, and Azure Cognitive Search for indexing and retrieval. They can be combined with Azure Machine Learning for model lifecycle management and Azure DevOps for CI/CD pipelines. Furthermore, integration with Azure Active Directory enables enterprise-grade identity and access management, while Azure Monitor and Log Analytics provide operational insights and alerting.

In summary, the general availability of Anthropic’s Claude models within Microsoft Foundry offers enterprises a robust, scalable, and versatile AI toolkit for advanced reasoning, coding, and multimodal applications, supported by seamless integration with Azure’s comprehensive cloud ecosystem and enterprise security standards.

---

### 2. Public Preview: Azure Copilot agents - a closer look at the deployment agent 

**Published**: November 18, 2025 20:15:19 UTC
**Link**: [Public Preview: Azure Copilot agents - a closer look at the deployment agent ](https://azure.microsoft.com/updates?id=526751)

**Update ID**: 526751
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Azure Copilot

**Summary**:

- What was updated  
Azure introduced the public preview of the Azure Copilot deployment agent, one of six new agentic capabilities designed to enhance cloud workload management.

- Key changes or new features  
The deployment agent assists developers and IT professionals in discovering existing cloud resources, planning deployment strategies, and automating the deployment of workloads. It leverages AI-driven insights to accelerate cloud adoption and reduce manual configuration errors, enabling faster and more confident deployment processes.

- Target audience affected  
This update primarily targets developers, DevOps engineers, and IT professionals responsible for cloud infrastructure deployment and management within Azure environments.

- Important notes if any  
As a public preview feature, the deployment agent may have limited availability and is subject to ongoing improvements. Users are encouraged to provide feedback to help shape future capabilities. Integration with other Azure Copilot agents is expected to enhance end-to-end cloud workload lifecycle management.  

For more details, visit: https://azure.microsoft.com/updates?id=526751

**Details**:

The recent Azure update introduces the public preview of Azure Copilot agents, with a focused deep dive on the deployment agent, one of six new agentic capabilities designed to enhance cloud workload management. This deployment agent is engineered to streamline and accelerate the discovery, planning, and deployment phases of cloud workloads, leveraging AI-driven automation to improve operational efficiency and deployment confidence.

**Background and Purpose:**  
Azure Copilot agents extend Azure’s AI-powered management capabilities by embedding autonomous agents that assist IT professionals in managing complex cloud environments. The deployment agent specifically addresses the challenges of workload deployment by providing intelligent guidance and automation, reducing manual effort and minimizing errors during deployment processes. This aligns with Azure’s broader strategy to integrate AI into cloud operations, enabling faster, more reliable cloud adoption and management.

**Specific Features and Detailed Changes:**  
The deployment agent offers several key features:  
- **Automated Discovery:** It scans existing environments to identify workloads suitable for migration or deployment, providing a comprehensive inventory and dependency mapping.  
- **Intelligent Planning:** Using AI, it generates optimized deployment plans tailored to workload requirements, resource availability, and organizational policies.  
- **Guided Deployment:** The agent assists in executing deployment steps, automating routine tasks such as resource provisioning, configuration, and validation checks.  
- **Continuous Feedback:** It provides real-time insights and recommendations during deployment, enabling proactive issue resolution and adjustment.

These features represent a significant enhancement over manual deployment processes, integrating AI to reduce complexity and increase deployment speed.

**Technical Mechanisms and Implementation Methods:**  
The deployment agent operates as a containerized service within the Azure environment, leveraging Azure Machine Learning models and Azure Cognitive Services for AI-driven decision-making. It interfaces with Azure Resource Manager (ARM) APIs to orchestrate resource provisioning and configuration. The agent collects telemetry and environment metadata through Azure Monitor and Log Analytics, feeding this data into its AI models to refine deployment strategies dynamically. Deployment workflows are defined using Azure Blueprints and ARM templates, which the agent customizes based on discovered workload characteristics.

**Use Cases and Application Scenarios:**  
- **Cloud Migration:** Enterprises migrating on-premises applications to Azure can use the deployment agent to automate discovery and plan migration paths, reducing downtime and risk.  
- **DevOps Pipelines:** Integration into CI/CD pipelines allows automated deployment of infrastructure and applications with AI-optimized configurations.  
- **Multi-Cloud and Hybrid Environments:** The agent aids in orchestrating deployments across hybrid setups, ensuring consistency and compliance.  
- **Resource Optimization:** By analyzing workload requirements, the agent helps right-size resources, improving cost efficiency.

**Important Considerations and Limitations:**  
As a public preview feature, the deployment agent may have limited support for certain complex or custom workloads and may require manual intervention in edge cases. Users should validate AI-generated plans before execution and monitor deployments closely. Security considerations include ensuring the agent’s permissions are scoped appropriately to prevent unauthorized resource modifications. Additionally, integration with existing governance and compliance frameworks should be tested to maintain organizational policies.

**Integration with Related Azure Services:**  
The deployment agent tightly integrates with several Azure services:  
- **Azure Resource Manager (ARM):** For resource provisioning and deployment orchestration.  
- **Azure Monitor and Log Analytics:** To gather telemetry and monitor deployment health.  
- **Azure Machine Learning:** Powers the AI models that analyze workloads and generate deployment plans.  
- **Azure Blueprints:** Provides deployment templates and governance controls that the agent utilizes.  
- **Azure DevOps and GitHub Actions:** Enables embedding the deployment agent’s capabilities into CI/CD workflows.

In summary, the Azure Copilot deployment agent public preview introduces an AI-driven, automated approach to discovering, planning, and deploying cloud workloads, significantly enhancing deployment efficiency and reliability. IT professionals can leverage this agent to reduce manual overhead, optimize resource allocation, and integrate deployment automation seamlessly into their existing Azure environments and DevOps processes, while remaining mindful of its preview status and operational boundaries.

---

### 3. Private Preview: Azure HorizonDB 

**Published**: November 18, 2025 18:00:28 UTC
**Link**: [Private Preview: Azure HorizonDB ](https://azure.microsoft.com/updates?id=529806)

**Update ID**: 529806
**Data source**: Azure Updates API

**Categories**: In development

**Summary**:

- What was updated  
Microsoft announced the private preview of Azure HorizonDB for PostgreSQL, a new managed database service optimized for high performance and scalability.

- Key changes or new features  
Azure HorizonDB offers autoscaling storage up to 128 TB, delivering up to 3x faster performance compared to standard open-source PostgreSQL. It supports rapid compute scaling up to 3,072 vCores, enabling handling of demanding workloads with ease. The service is engineered to provide future-proof infrastructure for PostgreSQL applications requiring large-scale storage and high throughput.

- Target audience affected  
Developers building PostgreSQL-based applications needing enhanced performance and scalability, and IT professionals managing enterprise-grade database deployments on Azure will benefit from this service.

- Important notes if any  
Currently, Azure HorizonDB for PostgreSQL is available in private preview, requiring registration for access. As a preview service, features and performance may evolve before general availability. Users should evaluate compatibility and test workloads accordingly.  

For more details and to request access, visit the official Azure update page.

**Details**:

Azure has announced the private preview of Azure HorizonDB for PostgreSQL, a next-generation managed database service designed to address the growing demands of modern, data-intensive applications requiring high performance, massive scale, and operational simplicity. This update aims to provide IT professionals and developers with a future-proof, highly scalable PostgreSQL-compatible database engine optimized for both compute and storage scalability.

**Background and Purpose**  
Traditional PostgreSQL deployments, whether self-managed or managed via Azure Database for PostgreSQL, face challenges in scaling storage and compute independently, often leading to performance bottlenecks and operational complexity as workloads grow. Many enterprise applications require databases that can handle large volumes of data (multi-terabyte scale) with low latency and high throughput, while also adapting dynamically to fluctuating workloads. Azure HorizonDB is engineered to meet these needs by delivering a cloud-native, hyperscale PostgreSQL service that significantly improves performance and scalability beyond the capabilities of open-source PostgreSQL.

**Specific Features and Detailed Changes**  
- **Autoscaling Storage up to 128 TB:** HorizonDB supports automatic storage scaling up to 128 terabytes without downtime or manual intervention, enabling seamless handling of large datasets.  
- **Up to 3x Faster Performance:** Leveraging architectural enhancements and optimized query processing, HorizonDB delivers performance improvements up to three times faster than standard open-source PostgreSQL, benefiting transaction-heavy and analytical workloads.  
- **Rapid Compute Scalability to 3,072 vCores:** Compute resources can be scaled rapidly and independently up to 3,072 virtual cores, allowing the database to handle massive concurrent workloads and complex queries efficiently.  
- **PostgreSQL Compatibility:** HorizonDB maintains compatibility with PostgreSQL, enabling existing applications and tools to work with minimal changes.  
- **Private Preview Availability:** Currently available in private preview, allowing select customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
Azure HorizonDB is built on a cloud-native architecture that decouples compute and storage layers, enabling independent scaling. Storage is implemented on a distributed, durable, and highly available storage system that automatically grows as data volume increases. Compute nodes run optimized PostgreSQL engines enhanced with performance improvements such as advanced caching, parallel query execution, and efficient resource management. The service integrates with Azure’s underlying infrastructure for networking, security, and monitoring, ensuring enterprise-grade reliability and compliance. Autoscaling mechanisms monitor workload patterns and trigger resource adjustments dynamically without impacting availability.

**Use Cases and Application Scenarios**  
- **Enterprise Applications:** Large-scale ERP, CRM, and financial systems requiring high throughput and low latency.  
- **Analytics and BI:** Real-time analytics on transactional data with rapid query performance.  
- **SaaS Platforms:** Multi-tenant SaaS applications needing elastic scaling to handle variable workloads.  
- **IoT and Telemetry:** Ingesting and processing massive streams of time-series data.  
- **Gaming and Media:** Applications demanding rapid scaling during peak usage periods.

**Important Considerations and Limitations**  
- As a private preview service, HorizonDB may have limited regional availability and feature completeness.  
- Users should validate compatibility with their specific PostgreSQL extensions and custom configurations.  
- Pricing and SLA details are not yet finalized and may change upon general availability.  
- Migration from existing PostgreSQL deployments may require planning to leverage new scaling capabilities effectively.

**Integration with Related Azure Services**  
Azure HorizonDB integrates seamlessly with Azure ecosystem components such as:  
- **Azure Data Factory and Synapse Analytics** for data ingestion and advanced analytics workflows.  
- **Azure Monitor and Azure Security Center** for observability and security management.  
- **Azure Virtual Network (VNet)** for secure network isolation.  
- **Azure Active Directory (AAD)** for identity and access management.  
- **Azure Backup and Azure Site Recovery** for data protection and disaster recovery strategies.

In summary, Azure HorizonDB for PostgreSQL introduces a high-performance, hyperscale managed database solution with autos

---

### 4. Generally Available: Private Marketplace for VS Code

**Published**: November 18, 2025 18:00:28 UTC
**Link**: [Generally Available: Private Marketplace for VS Code](https://azure.microsoft.com/updates?id=526909)

**Update ID**: 526909
**Data source**: Azure Updates API

**Categories**: Launched, Developer tools, Visual Studio, Features, SDK and Tools, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft has launched the Generally Available (GA) release of the VS Code Private Marketplace.

- Key changes or new features  
The VS Code Private Marketplace enables organizations to securely host and manage Visual Studio Code extensions internally. It is fully integrated with VS Code, allowing teams to self-host extensions, control deployment, and manage updates with granular flexibility. This solution supports enterprise security requirements by restricting extension availability to approved internal users and streamlining extension lifecycle management within the organization.

- Target audience affected  
Developers and IT professionals in enterprise environments who require secure, controlled distribution and management of VS Code extensions. This is particularly relevant for teams with strict compliance or security policies around software extensions.

- Important notes if any  
The Private Marketplace simplifies extension governance by centralizing extension hosting and update management, reducing reliance on the public VS Code Marketplace. Organizations should evaluate integration steps and governance policies to leverage this feature effectively. Further technical details and setup guidance are available via the official Azure update link.

**Details**:

The Azure update announcing the general availability of the VS Code Private Marketplace introduces a secure, enterprise-grade solution for organizations to internally host, manage, and distribute Visual Studio Code extensions within their teams. This capability addresses the need for controlled extension deployment in corporate environments, enhancing security, compliance, and operational governance.

**Background and Purpose**  
Visual Studio Code extensions significantly enhance developer productivity by adding language support, debugging tools, and integrations. However, in enterprise contexts, unrestricted access to the public VS Code Marketplace can pose security risks, compliance challenges, and version control issues. Organizations require a mechanism to curate, approve, and distribute only vetted extensions to their developers. The VS Code Private Marketplace fulfills this need by enabling teams to create a private repository of extensions that integrates seamlessly with the VS Code client, ensuring consistent and secure extension management.

**Specific Features and Detailed Changes**  
- **Self-hosted Extension Repository:** Organizations can host their own curated set of VS Code extensions, including both public marketplace extensions and custom-developed ones, within a private marketplace.  
- **Seamless VS Code Integration:** The private marketplace appears natively within the VS Code extension manager, allowing developers to browse, install, and update extensions as if from the public marketplace but restricted to the enterprise-approved set.  
- **Flexible Deployment and Update Management:** IT teams can control which extensions are available, manage versioning, and push updates centrally, ensuring developers use approved and up-to-date tools.  
- **Security and Compliance:** By restricting extension sources, organizations reduce exposure to malicious or unvetted code, supporting compliance with internal policies and regulatory requirements.

**Technical Mechanisms and Implementation Methods**  
The private marketplace operates by hosting an extension feed that conforms to the VS Code Marketplace API specifications, enabling VS Code clients to consume it transparently. Organizations can deploy the marketplace feed on-premises or in a secure cloud environment, such as Azure App Service or Azure Blob Storage with static website hosting. Authentication and authorization mechanisms can be layered on top, such as Azure Active Directory integration, to restrict access to the marketplace feed. The update management process leverages VS Code’s native extension update framework, allowing administrators to publish new versions to the private feed, which clients detect and apply automatically or on-demand.

**Use Cases and Application Scenarios**  
- **Enterprise Security and Compliance:** Companies in regulated industries (finance, healthcare, government) can enforce strict controls on developer tooling, ensuring only approved extensions are used.  
- **Custom Extension Distribution:** Organizations developing proprietary VS Code extensions can distribute them internally without exposing them publicly.  
- **Standardized Development Environments:** IT teams can ensure consistency across developer workstations by controlling extension versions and availability.  
- **Offline or Restricted Network Environments:** The private marketplace can be hosted internally to support environments without internet access or with strict outbound traffic policies.

**Important Considerations and Limitations**  
- **Initial Setup Complexity:** Deploying and maintaining the private marketplace feed requires infrastructure setup and ongoing management, including security configurations.  
- **Extension Compatibility:** Extensions must be compatible with the VS Code versions used by developers; testing is recommended before publishing to the private feed.  
- **Update Latency:** Updates to extensions may not propagate as quickly as the public marketplace, depending on organizational processes.  
- **Licensing and Compliance:** Organizations must ensure compliance with extension licensing terms, especially when redistributing third-party extensions internally.

**Integration with Related Azure Services**  
- **Azure Active Directory (AAD):** Enables secure authentication and access control to the private marketplace feed, ensuring only authorized users can access or install extensions.  
- **Azure App Service or Azure Blob Storage:** Provides scalable, reliable hosting options for the private marketplace feed.  
- **Azure DevOps or GitHub Actions:** Can be integrated to automate the packaging, testing, and deployment of custom extensions to the private marketplace.  
- **Azure Monitor and Security Center:** Can be used to monitor the health, access patterns, and security posture

---

### 5. Public Preview: Microsoft Defender for Cloud + GitHub Advanced Security 

**Published**: November 18, 2025 18:00:28 UTC
**Link**: [Public Preview: Microsoft Defender for Cloud + GitHub Advanced Security ](https://azure.microsoft.com/updates?id=526876)

**Update ID**: 526876
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Security, DevOps, Microsoft Defender for Cloud, GitHub Advanced Security for Azure DevOps

**Summary**:

- What was updated  
Microsoft announced the public preview of the native integration between Microsoft Defender for Cloud and GitHub Advanced Security.

- Key changes or new features  
This integration enables unified protection for cloud-native applications throughout the entire application lifecycle—from code development in GitHub to deployment and runtime in Azure. It streamlines security workflows by combining GitHub’s code scanning, secret scanning, and dependency vulnerability detection with Defender for Cloud’s cloud workload protection and threat detection capabilities. This unified approach helps developers and security teams collaborate more effectively within a single workflow, improving security posture and accelerating remediation.

- Target audience affected  
Developers, DevOps engineers, and security professionals managing cloud-native applications on Azure and using GitHub for source control and CI/CD pipelines.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Organizations should plan for integration into existing DevSecOps processes to maximize benefits. Further enhancements and updates are expected as the preview progresses.  

Link: https://azure.microsoft.com/updates?id=526876

**Details**:

The recent public preview announcement of Microsoft Defender for Cloud integration with GitHub Advanced Security introduces a unified, end-to-end security solution designed to protect cloud-native applications throughout their entire lifecycle—from source code development to deployment and runtime in the cloud. This update addresses the growing need for seamless collaboration between development and security teams by embedding security controls directly into the developer workflow, thereby enhancing threat detection, vulnerability management, and compliance posture in a cohesive manner.

**Background and Purpose:**  
As organizations increasingly adopt DevOps and cloud-native architectures, security challenges have expanded beyond traditional perimeter defenses to encompass code quality, supply chain risks, and runtime threats. Historically, security tools for code scanning and cloud workload protection operated in silos, creating friction and delayed remediation. This update aims to bridge that gap by natively integrating GitHub Advanced Security’s code scanning, secret scanning, and dependency vulnerability detection capabilities with Microsoft Defender for Cloud’s runtime threat protection and compliance management. The goal is to provide a comprehensive security posture that spans from development pipelines to cloud infrastructure, enabling proactive risk mitigation and faster incident response.

**Specific Features and Changes:**  
- **Unified Security Insights:** Security alerts and recommendations from GitHub Advanced Security are now accessible within the Microsoft Defender for Cloud portal, consolidating vulnerability data across code repositories and deployed workloads.  
- **End-to-End Visibility:** Developers and security teams gain visibility into vulnerabilities detected during code scanning alongside runtime threats detected by Defender for Cloud’s cloud workload protection platform (CWPP).  
- **Automated Remediation Workflows:** Integration supports automated or semi-automated workflows that trigger remediation tasks based on findings from either environment, streamlining DevSecOps processes.  
- **Compliance and Governance:** Enhanced compliance reporting combines code-level security posture with cloud resource compliance, supporting regulatory requirements and internal policies.  
- **Native Integration:** The solution leverages native connectors and APIs between GitHub and Azure Defender, minimizing configuration overhead and ensuring real-time synchronization of security data.

**Technical Mechanisms and Implementation:**  
The integration is implemented through secure API connections that allow Defender for Cloud to ingest GitHub Advanced Security alerts and metadata. GitHub’s security features—such as CodeQL-powered code scanning, secret scanning, and dependency graph analysis—generate findings that are pushed to Microsoft Defender for Cloud via connectors configured in the Azure portal. Defender for Cloud correlates these findings with cloud workload telemetry, including Azure Security Center data, to provide a holistic security view. Role-based access control (RBAC) and Azure Active Directory (AAD) integration ensure that only authorized users can access combined security insights. Additionally, Azure Logic Apps or Azure Functions can be employed to automate response actions triggered by integrated alerts.

**Use Cases and Application Scenarios:**  
- **DevSecOps Pipelines:** Integrate security scanning early in CI/CD pipelines with GitHub Advanced Security, while monitoring deployed applications with Defender for Cloud to detect runtime anomalies or misconfigurations.  
- **Supply Chain Security:** Detect vulnerable dependencies and exposed secrets in code repositories before deployment, reducing the risk of introducing compromised components into production.  
- **Compliance Monitoring:** Maintain continuous compliance by correlating code-level security posture with cloud resource compliance, useful for industries with stringent regulatory requirements.  
- **Incident Response:** Centralize security alerts from code and cloud environments to accelerate investigation and remediation workflows across development and security teams.

**Important Considerations and Limitations:**  
- As a public preview feature, some functionalities may be subject to change and might not yet support all GitHub or Azure regions.  
- Integration requires appropriate licensing for both Microsoft Defender for Cloud and GitHub Advanced Security, which may impact cost planning.  
- Organizations must ensure proper configuration of permissions and API access to enable seamless data flow between GitHub and Azure.  
- The solution currently focuses on GitHub repositories and Azure cloud workloads; extending support to other source control or cloud platforms may require additional tools or custom integration.

**Integration with Related Azure Services:**  
This update complements Azure DevOps and Azure Pip

---

### 6. Public Preview: Smart Tier account level tiering (Azure Blob Storage and ADLS)

**Published**: November 18, 2025 18:00:28 UTC
**Link**: [Public Preview: Smart Tier account level tiering (Azure Blob Storage and ADLS)](https://azure.microsoft.com/updates?id=526188)

**Update ID**: 526188
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage

**Summary**:

- What was updated  
Azure Blob Storage and Azure Data Lake Storage (ADLS) now support Smart Tier account-level tiering, announced in public preview.

- Key changes or new features  
Smart Tier is a fully managed, automated data tiering solution that operates at the storage account level. It automatically moves data between hot, cool, and archive tiers based on usage patterns and access frequency, eliminating the need for manual tier management. This enhances cost optimization by ensuring data is stored in the most appropriate tier without user intervention.

- Target audience affected  
Developers and IT professionals managing large-scale storage accounts in Azure Blob Storage and ADLS who seek to optimize storage costs and simplify data lifecycle management.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments before full adoption. Integration with existing lifecycle management policies should be reviewed to avoid conflicts. Monitoring and analytics tools can be used to track tiering behavior and cost impact.  

For more details, visit: https://azure.microsoft.com/updates?id=526188

**Details**:

The Azure update announces the public preview of Smart Tier account-level tiering for Azure Blob Storage and Azure Data Lake Storage (ADLS), a fully managed, automated data tiering solution designed to optimize storage costs and management by dynamically moving data between access tiers at the account level without manual intervention.

**Background and Purpose:**  
As organizations increasingly store vast amounts of unstructured data in Azure Blob Storage and ADLS, managing data lifecycle and optimizing storage costs become critical challenges. Traditionally, tiering—moving data between Hot, Cool, and Archive tiers—has been configured at the container or blob level, requiring manual policies or scripts to manage data movement. This update addresses the need for a more scalable, automated, and account-wide tiering mechanism that reduces operational overhead and ensures cost efficiency.

**Specific Features and Detailed Changes:**  
- **Account-Level Tiering:** Unlike previous tiering capabilities scoped to individual blobs or containers, Smart Tier operates at the storage account level, enabling holistic data tiering policies across all blobs and files within the account.  
- **Fully Managed Automation:** Smart Tier automatically analyzes data access patterns and moves data between Hot, Cool, and Archive tiers based on usage, without requiring manual lifecycle management rules.  
- **Support for Azure Blob Storage and ADLS Gen2:** The feature supports both Blob Storage and hierarchical namespace-enabled ADLS Gen2 accounts, ensuring broad applicability for data lakes and general-purpose storage.  
- **Public Preview Availability:** This feature is currently in public preview, allowing customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods:**  
Smart Tier leverages telemetry and access pattern analytics at the account level to identify cold data that can be moved to lower-cost tiers and hot data that should remain in or be promoted to higher-performance tiers. The system continuously monitors read/write operations, last access times, and other metadata to make tiering decisions. Data movement is performed transparently by the Azure Storage backend, ensuring no disruption to applications. The tiering logic is embedded within the Azure Storage service, eliminating the need for users to create lifecycle management policies manually. Users enable Smart Tier via the Azure Portal, CLI, or ARM templates by toggling the feature on the storage account.

**Use Cases and Application Scenarios:**  
- **Cost Optimization for Large Data Lakes:** Organizations with large ADLS Gen2 accounts storing infrequently accessed data can reduce costs by automatically tiering cold data to Cool or Archive tiers.  
- **Simplified Data Lifecycle Management:** Enterprises can offload manual lifecycle management tasks, reducing operational complexity and risk of misconfiguration.  
- **Dynamic Workloads:** Applications with unpredictable or variable data access patterns benefit from automated tiering that adapts in near real-time.  
- **Backup and Archive Storage:** Data that transitions from active use to archival storage can be tiered automatically without manual intervention.

**Important Considerations and Limitations:**  
- **Preview Feature:** As a public preview, Smart Tier may have feature limitations and is not recommended for production-critical workloads without validation.  
- **Billing Implications:** Automated tiering may cause data to move to Archive tier, which has higher latency and retrieval costs; users should understand the cost model and access patterns.  
- **Data Access Impact:** Moving data between tiers may introduce access latency, especially when retrieving from Archive; applications must handle potential delays.  
- **Compatibility:** Smart Tier currently supports only Blob Storage and ADLS Gen2 accounts; other storage types are not supported.  
- **Control Granularity:** Since tiering is at the account level, fine-grained control per container or blob is limited compared to manual lifecycle policies.

**Integration with Related Azure Services:**  
Smart Tier integrates seamlessly with Azure Storage’s existing tiering infrastructure and lifecycle management framework. It complements Azure Monitor by providing telemetry data on tiering operations and cost savings. Additionally, it works alongside Azure Data Factory and Azure Synapse Analytics by optimizing storage costs for data lakes without impacting data ingestion or analytics workflows

---

### 7. Public Preview: Managed Instance on Azure App Service

**Published**: November 18, 2025 18:00:28 UTC
**Link**: [Public Preview: Managed Instance on Azure App Service](https://azure.microsoft.com/updates?id=523623)

**Update ID**: 523623
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Mobile, Web, App Service

**Summary**:

- What was updated  
Microsoft announced the Public Preview of Managed Instance on Azure App Service, a new capability that simplifies migrating existing web applications to Azure App Service.

- Key changes or new features  
This feature enables developers and IT professionals to move .NET web apps running on-premises or in virtual machines to Azure App Service with minimal configuration and no need for code rewrites. It provides a managed environment that supports seamless lift-and-shift migrations, reducing operational overhead and accelerating cloud adoption.

- Target audience affected  
Developers and IT professionals managing .NET web applications who want to modernize their infrastructure by migrating apps to Azure App Service without extensive redevelopment efforts.

- Important notes if any  
As this feature is currently in Public Preview, users should evaluate it in non-production environments and provide feedback. Some capabilities may still be evolving, and full production support will come after general availability. Users should review documentation and compatibility details before migration.  

For more details, visit: https://azure.microsoft.com/updates?id=523623

**Details**:

The Public Preview of Managed Instance on Azure App Service introduces a streamlined approach for migrating and running existing .NET web applications on Azure with minimal configuration changes and no need for code rewrites. This update addresses the complexity and operational overhead traditionally associated with moving on-premises or VM-hosted web apps to the cloud by providing a managed, scalable, and secure hosting environment integrated within Azure App Service.

**Background and Purpose:**  
Many enterprises face challenges when migrating legacy or custom .NET web applications to the cloud, often requiring extensive refactoring or re-architecting to fit Platform as a Service (PaaS) models. The Managed Instance on Azure App Service aims to simplify this transition by offering a near lift-and-shift experience that preserves application compatibility and operational familiarity. This reduces migration time, lowers risk, and accelerates cloud adoption.

**Specific Features and Detailed Changes:**  
- **Managed Instance Environment:** Provides a dedicated, isolated environment within Azure App Service that mimics on-premises IIS hosting, supporting full .NET Framework applications without modification.  
- **Minimal Configuration:** Supports existing app configurations, including web.config and application settings, enabling apps to run as-is.  
- **Integrated DevOps and Monitoring:** Leverages Azure App Service’s native capabilities such as deployment slots, auto-scaling, built-in diagnostics, and Application Insights integration.  
- **Security and Compliance:** Offers network isolation options, integration with Azure Virtual Network (VNet), and compliance with Azure security standards.  
- **Compatibility:** Supports .NET Framework versions and common IIS modules, allowing legacy dependencies to continue functioning.

**Technical Mechanisms and Implementation Methods:**  
The Managed Instance environment is implemented as a dedicated App Service Environment (ASE)-like construct but optimized for .NET Framework workloads. It abstracts the underlying infrastructure, providing managed IIS instances with pre-configured runtime stacks. Applications are deployed via standard Azure App Service deployment methods (ZIP deploy, Git, Azure DevOps pipelines). The environment supports VNet integration for secure backend connectivity and enables seamless scaling through Azure’s App Service scaling mechanisms. Configuration settings and environment variables are managed through the Azure portal or ARM templates, preserving existing app settings.

**Use Cases and Application Scenarios:**  
- **Legacy .NET Web App Migration:** Enterprises with on-premises .NET Framework web applications can migrate to Azure without rewriting code or re-architecting.  
- **Hybrid Cloud Deployments:** Organizations running apps in VMs or on-premises can gradually shift workloads to Azure App Service while maintaining operational consistency.  
- **Dev/Test Environments:** Rapid provisioning of managed instances for testing legacy apps in cloud environments.  
- **Compliance-Driven Deployments:** Scenarios requiring isolated and secure hosting environments with integration to corporate VNets.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- **Supported Frameworks:** Primarily targets .NET Framework apps; .NET Core/5+ apps are already well-supported on Azure App Service standard plans.  
- **Resource Constraints:** Managed Instances may have specific SKU or scaling limitations compared to standard App Service plans.  
- **Migration Testing:** Despite minimal configuration changes, thorough testing is recommended to validate app behavior in the managed environment.  
- **Cost Implications:** Dedicated managed environments may incur higher costs than multi-tenant App Service plans.

**Integration with Related Azure Services:**  
- **Azure Virtual Network:** Enables secure, private connectivity to backend databases or services.  
- **Azure SQL Managed Instance / Azure SQL Database:** Common backend databases for migrated web apps.  
- **Azure DevOps / GitHub Actions:** Supports CI/CD pipelines for automated deployments.  
- **Azure Monitor and Application Insights:** Provides telemetry, diagnostics, and performance monitoring.  
- **Azure Key Vault:** For secure management of application secrets and certificates.

In summary, the Managed Instance on Azure App Service Public Preview offers IT professionals a powerful

---

### 8. Public Preview: Entra-only identities support with Azure Files SMB 

**Published**: November 18, 2025 17:30:44 UTC
**Link**: [Public Preview: Entra-only identities support with Azure Files SMB ](https://azure.microsoft.com/updates?id=527713)

**Update ID**: 527713
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Files

**Summary**:

- What was updated  
Azure Files now supports Entra-only identities for SMB access in public preview.

- Key changes or new features  
This update enables customers to authenticate SMB file share access using Microsoft Entra Kerberos without relying on on-premises Active Directory domain controllers. It introduces a fully cloud-native authentication model, allowing organizations to retire legacy infrastructure while maintaining secure access to Azure Files over SMB.

- Target audience affected  
Developers and IT professionals managing file shares in Azure, especially those looking to simplify identity management and reduce dependency on on-premises domain controllers for SMB authentication.

- Important notes if any  
This feature is currently in public preview, so it should be tested thoroughly before production use. Organizations planning to adopt this should evaluate their existing identity infrastructure and migration path to Entra-only identities for SMB access. Additional configuration and permissions setup in Microsoft Entra ID may be required.

**Details**:

The recent Azure update introduces public preview support for Entra-only identities with Azure Files SMB, enabling organizations to authenticate SMB file share access using Microsoft Entra (formerly Azure AD) without relying on on-premises Active Directory Domain Services (AD DS). This advancement facilitates a fully cloud-native identity and access management model for Azure Files, leveraging Microsoft Entra Kerberos for secure authentication.

**Background and Purpose:**  
Traditionally, Azure Files SMB shares required integration with on-premises Active Directory Domain Controllers (AD DS) to authenticate users and enforce access controls, necessitating hybrid infrastructure and complex synchronization. This dependency posed challenges for organizations aiming to modernize and migrate fully to the cloud, as maintaining domain controllers increases operational overhead and complexity. The update addresses this by enabling Azure Files to authenticate SMB access directly using Entra identities, eliminating the need for on-premises domain controllers and simplifying cloud migration and management.

**Specific Features and Changes:**  
- **Entra-only Identity Support:** Azure Files SMB now supports authentication exclusively through Microsoft Entra identities, without requiring AD DS or domain-joined machines.  
- **Microsoft Entra Kerberos Authentication:** This feature introduces a cloud-native Kerberos protocol implementation integrated with Microsoft Entra, enabling secure ticket-based authentication for SMB access.  
- **Simplified Identity Management:** Customers can manage user identities and access policies entirely within Microsoft Entra, streamlining administration and reducing infrastructure dependencies.  
- **Public Preview Availability:** The feature is currently in public preview, allowing early adopters to test and provide feedback before general availability.

**Technical Mechanisms and Implementation:**  
Azure Files implements a cloud-based Kerberos Key Distribution Center (KDC) integrated with Microsoft Entra. When a user attempts to access an SMB share, the client requests a Kerberos ticket from the Entra KDC. Upon successful authentication, the ticket is presented to Azure Files to authorize access. This process replaces the traditional on-premises KDC role. To enable this, customers configure their Azure Files shares to use Entra authentication, assign appropriate Azure RBAC roles or NTFS-like ACLs mapped to Entra identities, and ensure clients support Microsoft Entra Kerberos authentication protocols. The SMB clients must be updated or configured to request Kerberos tickets from Microsoft Entra rather than an on-premises domain.

**Use Cases and Application Scenarios:**  
- **Cloud-Only Environments:** Organizations operating fully in the cloud without on-premises infrastructure can securely authenticate SMB file shares using Entra identities.  
- **Hybrid Cloud Migration:** Customers transitioning from on-premises AD DS to cloud-native identity management can phase out domain controllers while maintaining SMB access continuity.  
- **Simplified Identity and Access Management:** Enterprises seeking to reduce complexity and cost by consolidating identity management within Microsoft Entra benefit from this update.  
- **Dev/Test and Remote Work Scenarios:** Environments where domain joining is impractical or impossible can leverage Entra-only authentication for SMB file shares.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview feature, it may have limitations or require specific client configurations; production use should be carefully evaluated.  
- **Client Compatibility:** SMB clients must support Microsoft Entra Kerberos authentication; legacy clients may not be compatible.  
- **Access Control Models:** While Entra identities are supported, customers should verify that their access control policies and NTFS permissions align with the new authentication model.  
- **Geographic and Performance Factors:** Latency to Entra KDC services may impact authentication times; network design should consider this.  
- **Feature Parity:** Some advanced AD DS features (e.g., Group Policy) are not applicable in Entra-only scenarios.

**Integration with Related Azure Services:**  
This update tightly integrates Azure Files with Microsoft Entra ID, leveraging Azure AD’s identity platform capabilities. It complements Azure RBAC by enabling role assignments to control file share access. Additionally, it aligns with Azure AD Conditional Access policies, allowing organizations

---

### 9. Private Preview: Azure Boost confidential device

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Private Preview: Azure Boost confidential device](https://azure.microsoft.com/updates?id=530661)

**Update ID**: 530661
**Data source**: Azure Updates API

**Categories**: In development

**Summary**:

- What was updated  
Azure Boost confidential device feature has entered private preview.

- Key changes or new features  
Azure Boost offloads virtualization tasks—including networking, storage, and host management—from the hypervisor and host OS to dedicated hardware and software components. This approach enhances performance, security, and isolation by reducing the hypervisor’s workload and attack surface. The confidential device aspect focuses on protecting sensitive workloads through hardware-based security and trusted execution environments.

- Target audience affected  
Developers and IT professionals managing virtualized environments, especially those running confidential or sensitive workloads on Azure, will benefit from improved security and efficiency. This is particularly relevant for cloud architects, security engineers, and infrastructure teams looking to optimize virtualization performance and confidentiality.

- Important notes if any  
The feature is currently in private preview, so access is limited and requires enrollment. Users interested in early testing or integration should contact Microsoft for preview access. As a preview feature, it may have limited support and is subject to change before general availability.

**Details**:

The Azure Boost confidential device feature, now available in private preview, introduces a hardware-accelerated offloading mechanism designed to enhance virtualization performance and security within Azure confidential computing environments. This update addresses the overhead traditionally imposed on hypervisors and host operating systems by shifting critical virtualization tasks—such as networking, storage I/O, and host management—onto dedicated, purpose-built hardware and software components, thereby optimizing resource utilization and improving workload isolation.

**Background and Purpose**  
Virtualized environments inherently involve significant processing overhead on the hypervisor and host OS to manage networking, storage, and other virtualization services. This overhead can impact performance, increase latency, and potentially expose attack surfaces. Azure Boost confidential device aims to mitigate these challenges by offloading these tasks to specialized hardware, reducing the burden on the hypervisor and enhancing the confidentiality and integrity of workloads, particularly in confidential computing scenarios where data protection at runtime is paramount.

**Specific Features and Detailed Changes**  
- **Hardware Offloading:** Azure Boost confidential device integrates dedicated hardware accelerators that handle virtualization functions such as packet processing, storage I/O, and host management operations.  
- **Confidential Computing Focus:** The device is designed to operate within Azure confidential computing nodes, ensuring that offloaded tasks maintain the same level of security guarantees as the protected workloads.  
- **Improved Performance:** By offloading tasks, the hypervisor and host OS can allocate more CPU and memory resources directly to guest VMs, reducing latency and increasing throughput.  
- **Softwarized Control Plane:** Alongside hardware, a specialized software stack manages the offloading process, ensuring seamless integration with existing Azure infrastructure and hypervisor components.

**Technical Mechanisms and Implementation Methods**  
Azure Boost confidential device leverages a combination of hardware accelerators embedded within the host server and a tightly integrated software control plane. The hardware components handle low-level virtualization tasks such as network packet routing, storage request processing, and host management commands. The software layer interfaces with the hypervisor (likely Hyper-V) to redirect relevant operations to the hardware, maintaining synchronization and state consistency. This offloading is transparent to guest VMs but requires host OS and hypervisor support to enable and manage the device. The implementation likely involves custom drivers and firmware that ensure secure communication channels and enforce strict access controls to maintain confidentiality.

**Use Cases and Application Scenarios**  
- **Confidential VM Workloads:** Enterprises running sensitive workloads that require confidential computing protections can benefit from improved performance without compromising security.  
- **High-Performance Networking and Storage:** Applications with intensive network or storage I/O demands, such as financial services or real-time analytics, can achieve lower latency and higher throughput.  
- **Cloud-Native and Hybrid Deployments:** Organizations leveraging Azure confidential computing for hybrid cloud scenarios can optimize resource utilization and reduce operational overhead.  
- **Security-Sensitive Multi-Tenancy:** Azure Boost helps maintain strong isolation between tenants by offloading tasks to secure hardware, reducing the attack surface on the host.

**Important Considerations and Limitations**  
- **Preview Status:** As a private preview feature, Azure Boost confidential device is available to select customers and may not yet support all Azure regions or VM sizes.  
- **Hardware Dependency:** Utilization requires specific hardware configurations supporting the Boost device, limiting deployment flexibility.  
- **Compatibility:** Integration depends on host OS and hypervisor versions; legacy systems may not support the offloading mechanism.  
- **Security Assurance:** While designed for confidential computing, customers must validate compliance and security posture within their environment.  
- **Operational Complexity:** Enabling and managing the Boost device may introduce additional operational considerations, including monitoring and troubleshooting hardware-software interactions.

**Integration with Related Azure Services**  
Azure Boost confidential device complements Azure Confidential Computing services such as Azure Confidential VMs and Azure Trusted Launch by enhancing the underlying virtualization infrastructure. It integrates with Azure networking and storage services to accelerate data paths securely. Additionally, it aligns with Azure Security Center and Azure Monitor for visibility into performance and security

---

### 10. Public Preview: Microsoft HTTP DDoS Ruleset 1.0 on Application Gateway WAF v2

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Microsoft HTTP DDoS Ruleset 1.0 on Application Gateway WAF v2](https://azure.microsoft.com/updates?id=530609)

**Update ID**: 530609
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Azure DDoS Protection, Web Application Firewall

**Summary**:

- What was updated  
Microsoft announced the public preview of the HTTP DDoS Ruleset 1.0 for Application Gateway Web Application Firewall (WAF) v2.

- Key changes or new features  
The new ruleset enhances protection against HTTP-layer Distributed Denial of Service (DDoS) attacks, which are a major cause of application downtime. Unlike traditional static controls, this ruleset is designed to better detect and mitigate sophisticated, evolving botnet attacks targeting the application layer. It integrates seamlessly with Application Gateway WAF v2, providing improved automated threat detection and mitigation capabilities at the HTTP protocol level.

- Target audience affected  
Developers and IT professionals responsible for securing web applications hosted on Azure Application Gateway WAF v2 will benefit from this update. Security architects and operations teams managing DDoS defenses should evaluate the new ruleset to strengthen their application-layer protection.

- Important notes if any  
This feature is currently in public preview, so users should test it in non-production environments before full deployment. Feedback during the preview phase will help Microsoft refine the ruleset. Users must enable the HTTP DDoS Ruleset explicitly to leverage its protections.  

For more details, visit: https://azure.microsoft.com/updates?id=530609

**Details**:

The Azure update titled "Public Preview: Microsoft HTTP DDoS Ruleset 1.0 on Application Gateway WAF v2" introduces a new, specialized ruleset designed to enhance protection against HTTP-layer Distributed Denial of Service (DDoS) attacks within Azure Application Gateway Web Application Firewall (WAF) v2. This update addresses the increasing sophistication of HTTP-based DDoS attacks that traditional static rule sets struggle to mitigate effectively.

**Background and Purpose**  
HTTP-layer DDoS attacks target the application layer (Layer 7), aiming to exhaust server resources by flooding web applications with malicious HTTP requests. These attacks are notoriously difficult to detect because they often mimic legitimate traffic patterns, making static WAF rules insufficient. The purpose of this update is to provide a dynamic, Microsoft-maintained HTTP DDoS ruleset that leverages advanced detection techniques to identify and mitigate such attacks proactively, thereby reducing application downtime and improving resilience.

**Specific Features and Detailed Changes**  
- Introduction of the Microsoft HTTP DDoS Ruleset 1.0, specifically tailored for Application Gateway WAF v2.  
- The ruleset includes heuristics and anomaly detection patterns designed to identify volumetric and low-and-slow HTTP attacks, including those generated by evolving botnets.  
- It complements existing OWASP Core Rule Set (CRS) protections by focusing on traffic volumetrics and behavioral anomalies rather than just signature-based threats.  
- The ruleset is delivered as a managed, continuously updated component, ensuring protection adapts to emerging threats without manual rule tuning.  
- It is available in public preview, allowing customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
The HTTP DDoS Ruleset operates by analyzing HTTP request patterns in real-time at the Application Gateway WAF v2 layer. Key mechanisms include:  
- Traffic profiling: Establishes baseline normal traffic behaviors per application to detect deviations indicative of DDoS.  
- Rate limiting and anomaly detection: Identifies unusual request rates and patterns that suggest automated attack traffic.  
- Behavioral heuristics: Uses machine learning-derived heuristics to differentiate between legitimate users and malicious bots or attack vectors.  
- Integration with WAF policy: The ruleset is enabled via WAF policy configuration, allowing seamless deployment alongside existing security rules.  
- Logging and telemetry: Provides detailed diagnostics and metrics through Azure Monitor and Application Gateway logs for incident analysis.

**Use Cases and Application Scenarios**  
- Protection of web applications hosted behind Azure Application Gateway from HTTP floods and bot-driven volumetric attacks.  
- Scenarios where traditional WAF rules fail to mitigate sophisticated Layer 7 DDoS attacks that mimic legitimate user behavior.  
- Enterprises requiring adaptive, managed DDoS mitigation integrated directly into their application delivery infrastructure.  
- Organizations looking to reduce operational overhead by leveraging Microsoft’s continuous threat intelligence updates.

**Important Considerations and Limitations**  
- As a public preview feature, the HTTP DDoS Ruleset 1.0 may have limited SLA guarantees and could undergo changes before general availability.  
- It is designed specifically for Application Gateway WAF v2; customers using WAF v1 or other WAF solutions will not benefit from this ruleset.  
- Proper tuning and monitoring are recommended to avoid false positives that could block legitimate traffic, especially in complex or highly variable traffic environments.  
- The ruleset focuses on HTTP-layer volumetric attacks and should be used in conjunction with Azure DDoS Protection Standard for network-layer DDoS defense.

**Integration with Related Azure Services**  
- Works natively with Azure Application Gateway WAF v2, leveraging its scalable, regional load balancing and security capabilities.  
- Integrates with Azure Monitor and Azure Log Analytics for enhanced visibility, alerting, and forensic analysis of DDoS events.  
- Complements Azure DDoS Protection Standard, which provides network-layer DDoS mitigation, creating a layered defense strategy.  
- Can

---

### 11. Private Preview: Azure Boost remote storage throughput and network bandwidth enhancements

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Private Preview: Azure Boost remote storage throughput and network bandwidth enhancements](https://azure.microsoft.com/updates?id=530287)

**Update ID**: 530287
**Data source**: Azure Updates API

**Categories**: In development

**Summary**:

- What was updated  
Azure Boost’s remote storage throughput and network bandwidth performance enhancements are now available in private preview.

- Key changes or new features  
The latest Azure Boost architecture improves offloading of virtualization tasks, specifically enhancing remote storage throughput and network bandwidth. These improvements aim to optimize performance for virtualized workloads by reducing host CPU overhead and increasing data transfer speeds across the network and storage layers.

- Target audience affected  
Developers and IT professionals managing Azure virtualized environments, especially those focused on high-performance storage and networking scenarios, will benefit from these enhancements. Cloud architects and infrastructure engineers optimizing Azure VM performance should evaluate these updates.

- Important notes if any  
This update is currently in private preview, so access is limited and requires enrollment. Users should test workloads in controlled environments before production deployment. Further documentation and general availability timelines are expected to be announced later.

**Details**:

The recent private preview announcement of Azure Boost’s enhanced remote storage throughput and network bandwidth capabilities introduces significant performance improvements in Azure’s virtualization offload architecture. Azure Boost is a specialized Microsoft Azure system designed to offload critical virtualization tasks—including networking, storage, and host management—from the hypervisor to dedicated hardware or optimized software components, thereby improving overall VM performance and reducing CPU overhead on host machines.

**Background and Purpose:**  
As cloud workloads increasingly demand higher I/O throughput and lower latency, traditional hypervisor-based virtualization can become a bottleneck, especially for storage and network-intensive applications. The update aims to address these limitations by enhancing the Azure Boost architecture to deliver greater remote storage throughput and expanded network bandwidth. This is critical for scenarios involving high-performance computing, large-scale data processing, and latency-sensitive applications, where maximizing data transfer rates and minimizing virtualization overhead directly impact application responsiveness and scalability.

**Specific Features and Detailed Changes:**  
The update introduces optimized data path enhancements within Azure Boost that accelerate remote storage I/O operations and increase available network bandwidth for virtual machines. Key changes include:  
- Improved offload algorithms that reduce CPU cycles spent on storage and network virtualization tasks.  
- Enhanced data plane processing that supports higher throughput rates for remote storage access, enabling faster read/write operations over the network.  
- Expanded network bandwidth allocation per VM, allowing workloads to utilize more network resources without contention or throttling.  
- Integration of advanced queuing and scheduling mechanisms to better manage I/O requests and network packets, reducing latency and jitter.

**Technical Mechanisms and Implementation Methods:**  
Azure Boost leverages a combination of hardware acceleration (such as SmartNICs or FPGA-based offload engines) and software optimizations within the Azure host environment. The updated architecture utilizes direct memory access (DMA) techniques and kernel bypass networking to streamline data movement between VMs and remote storage endpoints. By offloading packet processing and storage I/O tasks from the hypervisor to dedicated components, the system minimizes context switches and CPU interrupts. Additionally, the update employs enhanced RDMA (Remote Direct Memory Access) protocols and NVMe-over-Fabrics optimizations to maximize throughput and reduce latency for remote storage operations.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for:  
- High-performance computing (HPC) clusters requiring rapid access to distributed storage.  
- Big data analytics platforms that process large volumes of data stored remotely.  
- Enterprise applications with stringent SLAs for network and storage latency.  
- Virtual desktop infrastructure (VDI) environments where network responsiveness impacts user experience.  
- Any scenario where maximizing VM network bandwidth and storage throughput can improve application performance and cost efficiency.

**Important Considerations and Limitations:**  
- As this is a private preview, access is limited and may require enrollment or invitation from Microsoft.  
- Compatibility with existing VM sizes and storage types should be verified, as certain configurations may not yet support the enhanced Azure Boost features.  
- Monitoring and diagnostics tools may need updates to fully capture performance metrics related to the new offload capabilities.  
- Workloads should be tested in controlled environments to assess real-world benefits and identify any integration issues before production deployment.

**Integration with Related Azure Services:**  
The enhanced Azure Boost architecture complements Azure’s broader ecosystem, including Azure NetApp Files, Azure Blob Storage, and Azure Virtual Network. It can be leveraged alongside Azure Accelerated Networking to further reduce network latency and improve throughput. Moreover, integration with Azure Monitor and Azure Network Watcher allows IT professionals to track performance improvements and troubleshoot network/storage bottlenecks effectively. This update also aligns with Azure’s push towards software-defined infrastructure and hardware-accelerated virtualization, enabling seamless scaling of compute, storage, and network resources.

In summary, the private preview of Azure Boost’s remote storage throughput and network bandwidth enhancements represents a strategic advancement in Azure’s virtualization offload capabilities, delivering measurable performance gains for demanding workloads through hardware-accelerated and software-optimized mechanisms, with broad applicability across high-throughput and latency

---

### 12. Public Preview: NVv6 Virtual Machines

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: NVv6 Virtual Machines](https://azure.microsoft.com/updates?id=530208)

**Update ID**: 530208
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines

**Summary**:

- What was updated  
Azure announced the public preview of NCv6 Virtual Machines featuring Nvidia RTX PRO 6000 Blackwell Server Edition GPUs, as the latest enhancement to the NC Series VM lineup.

- Key changes or new features  
The NCv6 VMs leverage Nvidia RTX PRO 6000 BSE GPUs designed to accelerate diverse workloads such as AI, machine learning, rendering, and simulation. These VMs offer improved GPU performance and scalability for compute-intensive applications. They provide enhanced graphics capabilities and support for virtualization scenarios requiring high-end GPU acceleration.

- Target audience affected  
Developers and IT professionals working on GPU-accelerated workloads, including data scientists, AI/ML engineers, graphics professionals, and HPC users, will benefit from these new VMs. Organizations needing powerful GPU resources in Azure for development, testing, or production deployments should consider these VMs.

- Important notes if any  
This offering is currently in public preview, so users should expect potential limitations or changes before general availability. Pricing and availability details may vary by region. Users should evaluate compatibility with their workloads and monitor Azure updates for GA announcements.  

For more details, visit the official Azure update page.

**Details**:

The recent Azure update announces the public preview of NCv6 Virtual Machines, specifically the NCv6 RTX PRO 6000 Blackwell Server Edition (BSE) VMs, marking a significant advancement in the NC Series GPU-enabled VM offerings on Azure. This update aims to provide IT professionals and developers with enhanced GPU capabilities tailored for demanding compute-intensive and graphics workloads.

**Background and Purpose**  
The NC Series VMs have traditionally catered to high-performance computing (HPC), AI training, and visualization workloads by leveraging NVIDIA GPUs. The introduction of the NCv6 series with the RTX PRO 6000 Blackwell GPUs addresses the growing demand for more powerful, flexible, and cost-effective GPU resources in the cloud. By entering public preview, Microsoft enables customers to evaluate these new VMs for workloads requiring advanced GPU acceleration, improved graphics rendering, and AI inferencing capabilities.

**Specific Features and Detailed Changes**  
- **GPU Hardware**: The NCv6 VMs are equipped with NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs, which offer significant improvements in GPU architecture, including enhanced ray tracing, AI acceleration, and compute throughput compared to previous generations.  
- **VM Sizes and Scalability**: These VMs come in various sizes to accommodate different workload scales, allowing users to select configurations optimized for their specific compute and memory requirements.  
- **Virtualization Technology**: The NCv6 series supports GPU virtualization, enabling multiple users or processes to share GPU resources efficiently, increasing utilization and reducing costs.  
- **Enhanced Graphics and Compute**: The RTX PRO 6000 BSE GPUs support advanced features such as real-time ray tracing, AI-enhanced workflows, and large-scale parallel compute, making them suitable for both visualization and AI workloads.

**Technical Mechanisms and Implementation Methods**  
The NCv6 VMs leverage Azure’s underlying hypervisor and GPU partitioning technologies to expose the RTX PRO 6000 BSE GPUs to virtual machines securely and efficiently. The GPUs support NVIDIA’s latest drivers and software stacks, including CUDA, TensorRT, and RTX technologies, ensuring compatibility with a wide range of AI frameworks and graphics applications. Azure integrates these VMs with its networking, storage, and identity services to provide a seamless and secure environment. Users can deploy these VMs via Azure CLI, ARM templates, or the Azure portal, with support for GPU-accelerated containers and Kubernetes clusters.

**Use Cases and Application Scenarios**  
- **AI and Machine Learning**: Training and inferencing of deep learning models that require high GPU throughput and memory bandwidth.  
- **3D Rendering and Visualization**: Real-time ray tracing and photorealistic rendering for design, engineering, and media production workflows.  
- **Simulation and HPC**: Scientific simulations and computational fluid dynamics that benefit from GPU acceleration.  
- **Virtual Workstations**: Providing remote GPU-accelerated desktops for CAD, video editing, and other graphics-intensive applications.

**Important Considerations and Limitations**  
- **Public Preview Status**: As a preview offering, the NCv6 VMs may have limited availability and could undergo changes before general availability. Users should test workloads thoroughly before production deployment.  
- **Region Availability**: Initially, these VMs may be available only in select Azure regions.  
- **Cost Implications**: The advanced GPU capabilities come with higher costs; users should optimize VM sizing and usage to balance performance and budget.  
- **Driver and Software Compatibility**: Ensuring that applications and frameworks are compatible with the RTX PRO 6000 BSE GPU drivers is critical for optimal performance.

**Integration with Related Azure Services**  
NCv6 VMs integrate seamlessly with Azure Machine Learning for scalable AI model training, Azure Kubernetes Service (AKS) for orchestrating GPU-accelerated container workloads, and Azure Virtual Desktop for delivering GPU-powered virtual workstations. Additionally, these VMs can utilize Azure Blob Storage and Azure NetApp Files for high-throughput

---

### 13. Public Preview: New integration and extensibility capabilities to Azure SRE Agent

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: New integration and extensibility capabilities to Azure SRE Agent](https://azure.microsoft.com/updates?id=529944)

**Update ID**: 529944
**Data source**: Azure Updates API

**Categories**: In preview

**Summary**:

- What was updated  
Azure SRE Agent now offers new integration and extensibility capabilities, currently in public preview, enhancing its AI-driven operational automation platform.

- Key changes or new features  
The update introduces expanded integration options allowing developers and IT teams to connect SRE Agent more seamlessly with existing tools and workflows. It supports custom extensibility, enabling users to tailor prompt-based automation to specific operational needs. This shift from static automation to dynamic, AI-powered workflows reduces complexity and operational overhead by unifying disparate processes into a single interface.

- Target audience affected  
This update primarily targets cloud operations engineers, site reliability engineers (SREs), developers, and IT professionals responsible for managing and automating Azure cloud environments.

- Important notes if any  
As the features are in public preview, users should evaluate them in non-production environments and provide feedback. Integration and extensibility enhancements require familiarity with prompt engineering and automation scripting to fully leverage the new capabilities.  

For more details, visit: https://azure.microsoft.com/updates?id=529944

**Details**:

The recent public preview update to Azure SRE Agent introduces enhanced integration and extensibility capabilities designed to streamline and unify operational workflows for Site Reliability Engineering (SRE) teams managing cloud environments. Azure SRE Agent leverages AI-driven automation to replace fragmented, static scripts and manual interventions with a dynamic, prompt-based automation layer that simplifies complex cloud operations and reduces operational overhead.

**Background and Purpose**  
Traditional cloud operations often involve multiple disparate tools and manual processes, leading to inefficiencies and increased risk of human error. Azure SRE Agent was developed to address these challenges by providing a centralized, intelligent automation platform that integrates with existing operational workflows. The purpose of this update is to expand the agent’s ability to integrate with external systems and extend its automation capabilities, thereby enabling more comprehensive and customizable operational scenarios.

**Specific Features and Detailed Changes**  
This update introduces new integration points and extensibility options that allow users to connect Azure SRE Agent with a broader range of Azure services and third-party tools. Key features include:

- **Custom Connector Support:** Users can now build and deploy custom connectors to integrate with external APIs and services, enabling the agent to trigger workflows or retrieve data beyond native Azure resources.
- **Enhanced Prompt Customization:** The agent’s AI-driven prompts can be tailored with user-defined templates and variables, allowing for more precise control over automation logic and outputs.
- **Event-Driven Automation Triggers:** Integration with Azure Event Grid and Azure Monitor alerts enables the agent to initiate workflows automatically in response to specific operational events or anomalies.
- **Extensible Plugin Framework:** Developers can create plugins that extend the agent’s capabilities, such as adding new command sets or integrating with proprietary monitoring tools.

**Technical Mechanisms and Implementation Methods**  
The extensibility is implemented via a modular architecture where custom connectors and plugins are registered with the SRE Agent runtime environment. These components interact with the agent through well-defined APIs and SDKs provided by Azure. Event-driven triggers leverage Azure Event Grid subscriptions and Azure Monitor alert rules to invoke the agent’s automation workflows. Prompt customization is facilitated through a templating engine that supports variables, conditional logic, and integration with Azure Key Vault for secure parameter management.

**Use Cases and Application Scenarios**  
This update enables a variety of practical scenarios, such as:

- Automating incident response by integrating with ITSM tools (e.g., ServiceNow) to create tickets automatically when alerts are detected.
- Extending operational workflows to include third-party monitoring or logging platforms, consolidating data and actions within a single automation layer.
- Customizing remediation steps for specific environments or applications by tailoring prompt templates and commands.
- Enabling proactive operational tasks triggered by scheduled events or real-time alerts, such as scaling resources or applying configuration changes.

**Important Considerations and Limitations**  
As this is a public preview, users should be aware that some features may be subject to change and not recommended for production-critical environments without thorough testing. Custom connectors and plugins require development effort and security review, especially when integrating with external systems. Proper role-based access control (RBAC) and credential management practices must be followed to safeguard automation workflows. Additionally, reliance on AI-driven prompts necessitates monitoring and tuning to ensure accuracy and relevance of automated actions.

**Integration with Related Azure Services**  
The update deepens integration with core Azure services including Azure Monitor, Azure Event Grid, Azure Logic Apps, and Azure Key Vault. Azure Monitor provides alerting data that can trigger SRE Agent workflows, while Event Grid facilitates event-driven automation. Logic Apps can be orchestrated alongside SRE Agent for complex multi-step workflows. Key Vault integration ensures secure handling of sensitive parameters within automation scripts. This cohesive integration enables SRE teams to build robust, secure, and scalable operational automation pipelines within the Azure ecosystem.

In summary, the new integration and extensibility capabilities in Azure SRE Agent public preview empower IT professionals to create more adaptive, automated, and integrated cloud operations by leveraging customizable connectors, event-driven triggers, and AI-enhanced

---

### 14. Generally Available: Advanced sampling and richer data collection in Azure Monitor OpenTelemetry Distro

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Advanced sampling and richer data collection in Azure Monitor OpenTelemetry Distro](https://azure.microsoft.com/updates?id=529519)

**Update ID**: 529519
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Azure Monitor OpenTelemetry Distro has reached general availability with enhanced sampling and richer data collection features. This update improves how telemetry data is collected and processed for Azure Monitor Application Insights.

- Key changes or new features  
The update introduces advanced sampling options including rate-limited sampling and trace-based log sampling. Rate-limited sampling helps control the volume of telemetry data by limiting the number of traces collected per time unit, reducing ingestion costs and noise. Trace-based log sampling enables correlation of logs with traces, allowing more precise and context-rich data collection. These features improve data quality and observability while optimizing resource usage.

- Target audience affected  
Developers and IT professionals using Azure Monitor Application Insights and OpenTelemetry for application monitoring and diagnostics will benefit. Those implementing distributed tracing and log correlation in cloud-native or hybrid environments will find these new sampling capabilities particularly useful.

- Important notes if any  
These capabilities align with open standards, reinforcing Azure’s commitment to interoperability. Users should review and adjust their sampling configurations to balance telemetry detail and cost effectively. The update is generally available, ready for production use.

**Details**:

The recent general availability of advanced sampling and richer data collection features in the Azure Monitor OpenTelemetry Distro represents a significant enhancement aimed at improving telemetry data efficiency and quality for distributed applications monitored via Azure Monitor Application Insights. This update aligns with Azure’s commitment to open standards by extending the OpenTelemetry-based monitoring capabilities with more granular and customizable sampling controls.

**Background and Purpose**  
Azure Monitor OpenTelemetry Distro is a Microsoft-supported distribution of OpenTelemetry components designed to simplify instrumentation and telemetry data collection for Azure Monitor. As cloud-native applications grow in complexity, the volume of telemetry data—traces, metrics, and logs—can become overwhelming, leading to increased storage costs and processing overhead. The purpose of this update is to provide IT professionals with more sophisticated sampling mechanisms that reduce data volume while preserving critical diagnostic information, thereby optimizing performance and cost-efficiency without sacrificing observability.

**Specific Features and Detailed Changes**  
The update introduces two key sampling enhancements:

1. **Rate-limited Sampling:** This feature allows users to specify a maximum rate of telemetry data (traces or spans) to be collected and exported. Unlike traditional probabilistic sampling, rate-limited sampling enforces a hard cap on the number of samples per time unit, preventing data spikes during high traffic periods.

2. **Trace-based Log Sampling:** This new capability enables logs to be sampled based on trace context, meaning that logs associated with sampled traces are retained while others can be dropped. This ensures that logs relevant to important traces are preserved, improving correlation and root cause analysis.

These features extend the existing sampling options, such as probabilistic and adaptive sampling, by providing more deterministic control over telemetry volume and relevance.

**Technical Mechanisms and Implementation Methods**  
The advanced sampling features are implemented within the Azure Monitor OpenTelemetry Distro’s collector and SDK components. Rate-limited sampling operates by maintaining counters and timers to enforce export limits, dropping excess telemetry beyond configured thresholds. Trace-based log sampling leverages trace context propagation; when a trace is sampled, associated logs tagged with the trace ID are retained, while logs outside sampled traces can be filtered out.

Configuration is typically done via YAML or environment variables in the OpenTelemetry Collector or SDK configuration files, allowing users to define sampling policies per service or environment. The distro integrates these sampling processors seamlessly into the telemetry pipeline before data export to Azure Monitor Application Insights.

**Use Cases and Application Scenarios**  
- **High-traffic microservices:** Rate-limited sampling prevents telemetry overload during traffic spikes, maintaining stable ingestion rates and controlling costs.  
- **Complex distributed tracing:** Trace-based log sampling ensures that logs correlated with important traces are preserved, enhancing troubleshooting and diagnostics.  
- **Cost-sensitive environments:** Organizations can optimize telemetry data volume without losing critical insights, balancing observability with budget constraints.  
- **Hybrid and multi-cloud setups:** Since OpenTelemetry is vendor-neutral, these features facilitate consistent telemetry management across heterogeneous environments while leveraging Azure Monitor’s backend.

**Important Considerations and Limitations**  
- Over-aggressive sampling may lead to loss of critical telemetry data, potentially impacting diagnostic accuracy. Careful tuning of sampling rates and policies is essential.  
- Trace-based log sampling requires consistent trace context propagation; applications must correctly instrument and propagate trace IDs for effective correlation.  
- Some legacy or custom telemetry formats may not fully support these sampling features without additional instrumentation adjustments.  
- Rate-limited sampling enforces hard limits that may drop data during peak loads, so monitoring and alerting on telemetry ingestion rates remains important.

**Integration with Related Azure Services**  
This update tightly integrates with Azure Monitor Application Insights, enhancing its data ingestion pipeline by reducing noise and focusing on relevant telemetry. It complements Azure Monitor Metrics and Logs by ensuring that correlated trace and log data are efficiently captured. Additionally, it supports Azure Kubernetes Service (AKS) and Azure Functions by enabling optimized telemetry collection in containerized and serverless environments. The distro’s open-source foundation also allows integration with Azure Arc and hybrid monitoring solutions, providing consistent

---

### 15. Public Preview: Azure Network Watcher Topology – Agentless Connection Troubleshoot

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Network Watcher Topology – Agentless Connection Troubleshoot](https://azure.microsoft.com/updates?id=527815)

**Update ID**: 527815
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Management and governance, Networking, Azure Kubernetes Service (AKS), Network Watcher

**Summary**:

- What was updated  
Azure Network Watcher Topology now supports visualization of Azure Kubernetes Service (AKS) clusters in Public Preview, providing agentless connection troubleshooting capabilities.

- Key changes or new features  
The update enables end-to-end visibility of AKS networking directly within the Azure Network Watcher Topology tool. Developers and IT professionals can explore Kubernetes cluster components and their network connections without deploying agents. This agentless connection troubleshoot feature simplifies diagnosing connectivity issues in AKS environments by visualizing pod-to-service and cluster network paths seamlessly.

- Target audience affected  
This update primarily benefits developers, DevOps engineers, and IT professionals managing AKS clusters who require enhanced network diagnostics and visualization tools integrated into Azure’s native networking experience.

- Important notes if any  
As this feature is in Public Preview, users should evaluate it in non-production environments and expect potential changes before general availability. Integration with existing Network Watcher capabilities ensures a unified troubleshooting experience without additional agent overhead.  

For more details, visit: https://azure.microsoft.com/updates?id=527815

**Details**:

The recent Azure update introduces the Public Preview of the Azure Network Watcher Topology feature with Agentless Connection Troubleshoot capabilities specifically enhanced for Azure Kubernetes Service (AKS) clusters. This update aims to provide IT professionals and network administrators with comprehensive, end-to-end visibility into the networking topology of AKS environments directly within the Azure Network Watcher experience, thereby simplifying troubleshooting and network diagnostics without requiring additional agents.

**Background and Purpose:**  
As organizations increasingly adopt Kubernetes for container orchestration, understanding the complex network interactions within AKS clusters becomes critical for maintaining application performance and security. Traditional network troubleshooting in Kubernetes often involves deploying agents or manually correlating network data, which can be cumbersome and error-prone. This update addresses these challenges by integrating AKS cluster visualization into Azure Network Watcher Topology and enabling agentless connection troubleshooting, streamlining network diagnostics and reducing operational overhead.

**Specific Features and Detailed Changes:**  
- **AKS Cluster Visualization:** The Network Watcher Topology now graphically represents AKS clusters, including nodes, pods, and their network relationships, within the Azure portal. This visualization extends to show virtual networks (VNets), subnets, network interfaces, and connected resources, enabling a holistic view of the cluster’s network architecture.  
- **Agentless Connection Troubleshoot:** This feature allows users to diagnose network connectivity issues between resources in the AKS cluster and other Azure services or endpoints without deploying any agents inside the cluster. It leverages Azure’s control plane and network telemetry to perform connectivity checks, path analysis, and latency measurements.  
- **End-to-End Network Visibility:** The integration provides a seamless experience to trace network paths, identify bottlenecks, and detect misconfigurations or security group rules that might be affecting communication within the AKS environment.

**Technical Mechanisms and Implementation Methods:**  
The topology visualization leverages Azure Network Watcher’s existing capabilities to collect network configuration and state information from Azure Resource Manager (ARM) and Azure networking APIs. For AKS clusters, it queries Kubernetes API servers and Azure resource metadata to map pods, nodes, and their network interfaces. The agentless connection troubleshoot uses Azure’s control plane telemetry, including Network Watcher’s connection troubleshoot API, to simulate and analyze network paths without requiring in-cluster agents. This approach reduces resource consumption and security risks associated with deploying additional software inside Kubernetes nodes.

**Use Cases and Application Scenarios:**  
- **Network Troubleshooting:** Quickly identify connectivity issues between pods, services, and external endpoints without complex manual diagnostics or agent deployment.  
- **Security Auditing:** Visualize network flows to verify that network security groups (NSGs) and Azure Firewall rules are correctly applied and not inadvertently blocking traffic.  
- **Performance Optimization:** Analyze network paths and latency to optimize service mesh configurations or pod placement strategies within AKS.  
- **Operational Monitoring:** Provide network topology insights to DevOps teams for better understanding of cluster networking and faster incident response.

**Important Considerations and Limitations:**  
- As a Public Preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- The agentless troubleshoot is dependent on Azure’s control plane telemetry and may not capture all types of network issues, especially those internal to the Kubernetes overlay network or caused by third-party CNI plugins.  
- Visualization granularity may vary depending on cluster size and complexity, and some custom networking configurations might not be fully represented.  
- Users must ensure appropriate RBAC permissions to access Network Watcher and AKS resources for topology data retrieval.

**Integration with Related Azure Services:**  
This update tightly integrates Azure Network Watcher with AKS and Azure Monitor, enabling enriched telemetry and diagnostics. It complements Azure Monitor’s container insights by adding network-specific visualization and troubleshooting capabilities. Additionally, it works alongside Azure Security Center by providing network topology context that can aid in threat detection and compliance assessments. The agentless connection troubleshoot also aligns with Azure Firewall and NSG diagnostics, offering a unified platform for network health monitoring

---

### 16. Public Preview: Azure Network Watcher Topology – AKS Visualization

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Network Watcher Topology – AKS Visualization](https://azure.microsoft.com/updates?id=527810)

**Update ID**: 527810
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Management and governance, Networking, Azure Kubernetes Service (AKS), Network Watcher

**Summary**:

- What was updated  
Azure Network Watcher Topology now includes a Public Preview feature for visualizing Azure Kubernetes Service (AKS) clusters.

- Key changes or new features  
This update enables end-to-end visibility of AKS clusters directly within the Network Watcher Topology tool. Developers and IT professionals can explore Kubernetes environments graphically, including nodes, pods, and networking components, integrated seamlessly into the Azure networking experience. This visualization helps in troubleshooting, monitoring, and managing AKS networking configurations more effectively.

- Target audience affected  
Developers, DevOps engineers, and IT professionals managing AKS clusters and Azure networking infrastructure will benefit from enhanced observability and diagnostics capabilities.

- Important notes if any  
This feature is currently in Public Preview, so users should expect potential changes and limitations. It is recommended to use it in non-production environments initially and provide feedback to Microsoft for improvements. Access requires appropriate Azure permissions to view Network Watcher and AKS resources.  

For more details and updates, visit: https://azure.microsoft.com/updates?id=527810

**Details**:

The recent Azure update introduces a Public Preview feature for Azure Network Watcher Topology that enhances visualization capabilities specifically for Azure Kubernetes Service (AKS) clusters. This integration aims to provide IT professionals and network administrators with comprehensive, end-to-end visibility of their AKS networking environments directly within the Azure portal’s Network Watcher experience.

**Background and Purpose**  
Managing and troubleshooting network connectivity in containerized environments like AKS can be complex due to dynamic pod scheduling, overlay networking, and multiple network components such as virtual nodes, network interfaces, and load balancers. Prior to this update, Network Watcher’s topology visualization primarily focused on traditional Azure networking resources without native support for Kubernetes-specific constructs. The purpose of this update is to bridge that gap by enabling visualization of AKS clusters’ network topology, helping users better understand the relationships and data flows between Kubernetes nodes, pods, services, and Azure networking components.

**Specific Features and Detailed Changes**  
- **AKS Cluster Visualization:** The topology graph now includes AKS-specific entities such as Kubernetes nodes, pods, and services, alongside Azure networking resources like virtual networks (VNets), subnets, network security groups (NSGs), and load balancers.  
- **End-to-End Network Mapping:** Users can see how Kubernetes workloads are connected internally and externally, including pod-to-pod communication, ingress/egress traffic paths, and integration with Azure infrastructure.  
- **Interactive Exploration:** The topology interface allows zooming, panning, and clicking on individual nodes or pods to reveal detailed metadata such as IP addresses, network policies, and security group associations.  
- **Real-Time Updates:** The visualization reflects the current state of the AKS cluster network, dynamically updating as pods scale or network configurations change.  
- **Public Preview Status:** As a preview feature, it is available for evaluation and feedback but may have limitations or require specific AKS versions and configurations.

**Technical Mechanisms and Implementation Methods**  
This feature leverages Azure Network Watcher’s existing topology engine, enhanced with Kubernetes API integration to extract cluster state and network information. It queries the AKS control plane and Kubernetes API server to gather pod and service metadata, mapping these to underlying Azure networking constructs. The topology engine correlates this data with Network Watcher’s network flow logs and diagnostic data to build a unified graph. The visualization is rendered within the Azure portal using interactive web technologies, providing a seamless user experience.

**Use Cases and Application Scenarios**  
- **Network Troubleshooting:** Quickly identify connectivity issues between pods, services, and external endpoints by visualizing network paths and security configurations.  
- **Security Auditing:** Assess network security group rules and Kubernetes network policies in context to ensure compliance and detect potential vulnerabilities.  
- **Capacity Planning and Optimization:** Understand traffic flows and resource utilization to optimize cluster scaling and network design.  
- **Onboarding and Training:** Help new team members visualize complex AKS networking setups for faster ramp-up.  
- **Hybrid and Multi-Cluster Environments:** Correlate AKS network topology with other Azure resources in hybrid cloud scenarios.

**Important Considerations and Limitations**  
- Being a Public Preview, the feature may not support all AKS configurations or Kubernetes versions; users should verify compatibility.  
- Some advanced Kubernetes networking plugins or custom CNI configurations might not be fully visualized.  
- Performance and update frequency depend on cluster size and network complexity; very large clusters may experience latency in topology rendering.  
- Role-based access control (RBAC) and permissions must be configured properly to allow Network Watcher to access AKS cluster metadata.  
- This visualization complements but does not replace specialized Kubernetes monitoring tools; it focuses on network topology rather than application-level metrics.

**Integration with Related Azure Services**  
- **Azure Network Watcher:** The core service providing network diagnostics, flow logs, and topology visualization.  
- **Azure Monitor:** Can be used alongside for collecting metrics and logs from AKS clusters and

---

### 17. Public Preview: Azure VNet Flow Log - Filtering 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure VNet Flow Log - Filtering ](https://azure.microsoft.com/updates?id=527805)

**Update ID**: 527805
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher

**Summary**:

- What was updated  
Azure VNet Flow Logs now support advanced filtering capabilities in public preview.

- Key changes or new features  
Users can apply granular filters on VNet Flow Logs to capture specific IP traffic flowing through Virtual Networks (VNets), Subnets, and Network Interface Cards (NICs). This enhancement allows selective logging based on criteria such as IP addresses, ports, protocols, and traffic direction. It improves monitoring precision, reduces storage costs by limiting unnecessary data, and enhances troubleshooting and security analysis.

- Target audience affected  
Developers, network engineers, and IT professionals responsible for network monitoring, security, compliance, and performance optimization in Azure environments.

- Important notes if any  
This feature is currently in public preview; users should evaluate it in non-production environments before full deployment. Advanced filtering can significantly optimize log data management but requires careful configuration to avoid missing critical traffic data. Integration with existing monitoring and SIEM tools remains supported.  

For more details and configuration guidance, refer to the official Azure update page.

**Details**:

The recent Azure update introduces Public Preview of advanced filtering capabilities in Azure Virtual Network (VNet) Flow Logs, a feature designed to enhance network traffic monitoring and diagnostics by allowing more granular control over the data captured. 

**Background and Purpose**  
Azure VNet Flow Logs have long served as a vital tool for capturing IP traffic metadata traversing VNets, Subnets, and Network Interface Cards (NICs). These logs are essential for network monitoring, troubleshooting connectivity issues, optimizing network performance, ensuring security compliance, and conducting forensic analysis. However, prior to this update, VNet Flow Logs collected traffic data broadly, which could result in large volumes of log data, increased storage costs, and challenges in isolating relevant traffic patterns. The introduction of filtering addresses these challenges by enabling users to specify criteria to selectively capture flow logs, thereby improving efficiency and relevance of the data collected.

**Specific Features and Detailed Changes**  
This update adds the ability to define advanced filters directly within the VNet Flow Log configuration. Users can now specify filtering rules based on various traffic attributes such as source and destination IP addresses, ports, protocols, and traffic direction (ingress or egress). Filters can be combined using logical operators to create complex conditions, allowing precise targeting of traffic flows to be logged. This selective logging reduces noise in the data, lowers storage and ingestion costs, and accelerates analysis by focusing on pertinent traffic.

**Technical Mechanisms and Implementation Methods**  
The filtering capability is implemented at the network infrastructure level, integrated with Azure Network Watcher’s flow logging pipeline. When enabled, the filtering engine evaluates each flow record against the defined filter criteria before committing the log entry to the storage account or Event Hub. The configuration is managed via Azure PowerShell, CLI, or ARM templates, where users specify filter expressions as part of the flow log settings. The filters operate on the metadata of network flows without impacting actual packet forwarding or network performance. This design ensures minimal overhead while providing powerful data reduction.

**Use Cases and Application Scenarios**  
- **Security Monitoring:** Organizations can focus on suspicious IP ranges or specific ports known for malicious activity, improving threat detection and incident response.  
- **Compliance Auditing:** Filter logs to capture only traffic relevant to regulatory requirements, reducing data volume and simplifying audit processes.  
- **Performance Troubleshooting:** Isolate traffic flows related to specific applications or services to diagnose latency or connectivity issues more effectively.  
- **Cost Optimization:** By filtering out irrelevant traffic, organizations reduce the volume of logs stored and processed, lowering Azure Monitor and storage costs.  

**Important Considerations and Limitations**  
- As this feature is in Public Preview, it should not be used in production environments without thorough testing.  
- Filtering applies only to flow logs metadata and does not capture packet payloads.  
- Complex filters may require careful construction to avoid unintentionally excluding critical traffic data.  
- There may be a slight delay in filter propagation after configuration changes.  
- Integration with existing monitoring solutions should be validated to ensure compatibility with filtered log data.  

**Integration with Related Azure Services**  
Filtered VNet Flow Logs continue to integrate seamlessly with Azure Monitor, Log Analytics, and Event Hubs, enabling downstream analytics, alerting, and visualization workflows. The reduced log volume enhances the efficiency of these services. Additionally, integration with Azure Sentinel can leverage filtered flow logs for more focused security analytics and automated threat hunting. The filtering feature also complements Network Watcher’s other diagnostic tools, providing a more tailored data set for comprehensive network management.

In summary, the Public Preview of filtering in Azure VNet Flow Logs empowers IT professionals to capture targeted network traffic data, improving monitoring precision, reducing operational costs, and enhancing security and compliance efforts through customizable, efficient log management.

---

### 18. Generally Available: ExpressRoute Scalable Gateway

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: ExpressRoute Scalable Gateway](https://azure.microsoft.com/updates?id=526729)

**Update ID**: 526729
**Data source**: Azure Updates API

**Categories**: Launched, Hybrid + multicloud, Networking, Azure ExpressRoute, Features, Services, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft has announced the general availability of the ExpressRoute Scalable Gateway (ErGwScale), a next-generation Virtual Network Gateway offering for Azure ExpressRoute.

- Key changes or new features  
ErGwScale introduces dynamic scaling of gateway infrastructure, allowing seamless adjustment of capacity to meet varying network traffic demands without downtime. This enhances performance and operational simplicity compared to previous fixed-capacity gateways. The scalable gateway supports higher throughput and improved resiliency, enabling better handling of large-scale ExpressRoute deployments. It simplifies management by automating scaling operations and reduces the need for manual intervention.

- Target audience affected  
This update primarily impacts network architects, cloud engineers, and IT professionals responsible for designing and managing Azure ExpressRoute connectivity. Developers leveraging ExpressRoute for hybrid or multi-cloud scenarios will also benefit from improved network reliability and performance.

- Important notes if any  
Users should evaluate existing ExpressRoute gateway deployments to consider migrating to the scalable gateway for enhanced flexibility and scalability. The update may require configuration changes or redeployment depending on current gateway SKU. Refer to official Azure documentation for migration guidance and pricing details.

**Details**:

The ExpressRoute Scalable Gateway (ErGwScale) is now generally available, representing a significant advancement in Azure Virtual Network Gateway technology designed to enhance the scalability, performance, and operational efficiency of ExpressRoute connections. Traditionally, ExpressRoute gateways required manual provisioning of fixed capacity SKUs, which limited flexibility and could lead to either underutilization or capacity bottlenecks. The introduction of the Scalable Gateway addresses these challenges by enabling dynamic scaling of gateway infrastructure in response to traffic demands, thereby optimizing resource utilization and improving overall network throughput.

From a feature perspective, the ExpressRoute Scalable Gateway supports automatic and on-demand scaling of gateway capacity without downtime, allowing seamless adjustment to fluctuating workloads. This is achieved through a distributed gateway architecture that decouples the control plane from the data plane, enabling independent scaling of data processing units. The gateway can scale out to multiple instances, aggregating bandwidth and providing higher aggregate throughput compared to traditional fixed-size gateways. Additionally, the scalable gateway supports all existing ExpressRoute features, including private peering, Microsoft peering, and Global Reach, ensuring backward compatibility and ease of migration.

Technically, the implementation of the Scalable Gateway leverages Azure’s underlying software-defined networking (SDN) infrastructure. The gateway is deployed as a managed service with a multi-instance architecture where each instance handles a portion of the traffic. Azure’s control plane monitors traffic patterns and automatically adjusts the number of instances based on predefined thresholds or manual triggers via Azure CLI, PowerShell, or the Azure portal. This elasticity eliminates the need for gateway downtime during scale operations, which is critical for enterprise workloads requiring high availability. The gateway also integrates with Azure Monitor and Network Watcher for enhanced observability and diagnostics.

Use cases for the ExpressRoute Scalable Gateway are broad and particularly relevant for enterprises with dynamic or growing bandwidth requirements, such as large-scale data migrations, hybrid cloud architectures, and multi-region deployments requiring Global Reach. Organizations running latency-sensitive or high-throughput applications benefit from the improved performance and reduced operational overhead. The ability to scale on demand also supports scenarios where traffic patterns are unpredictable, such as seasonal workloads or bursty data transfers.

Important considerations include the need to review pricing implications, as scaling out gateway instances may affect cost. While the scalable gateway supports most existing ExpressRoute features, users should verify compatibility with their specific configurations, especially custom routing or advanced security appliances. Migration from traditional gateways to the scalable gateway requires planning to minimize impact, though Azure provides tools and documentation to facilitate this process. Additionally, network administrators should update their monitoring and alerting strategies to account for the dynamic nature of the gateway instances.

Integration with related Azure services is seamless; the scalable gateway works natively with Azure Virtual WAN for centralized network management and with Azure Firewall and Network Virtual Appliances (NVAs) for enhanced security. It also complements Azure Private Link and Azure Bastion by providing robust, scalable connectivity to on-premises environments. The gateway’s compatibility with Azure Policy and Role-Based Access Control (RBAC) ensures governance and security compliance in enterprise environments.

In summary, the ExpressRoute Scalable Gateway introduces a flexible, high-performance, and operationally simple solution for managing ExpressRoute connectivity, enabling IT professionals to dynamically scale network gateways in line with evolving business needs while maintaining high availability and integration with Azure’s networking ecosystem.

---

### 19. Generally Available: Azure Container Registry Repository Permissions with Attribute-based Access Control (ABAC)

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Container Registry Repository Permissions with Attribute-based Access Control (ABAC)](https://azure.microsoft.com/updates?id=526644)

**Update ID**: 526644
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Registry

**Summary**:

- What was updated  
Azure Container Registry (ACR) now generally supports repository-level permissions using attribute-based access control (ABAC).

- Key changes or new features  
This update enables fine-grained, least-privilege access management for container image repositories within ACR. Organizations can define policies that control which Microsoft Entra identities can push or pull images based on attributes such as user, device, or environment context. This enhances security by moving beyond broad registry-level roles to more precise repository-scoped permissions. ABAC integration allows dynamic access decisions, improving governance and compliance.

- Target audience affected  
Developers and IT professionals managing containerized applications and DevOps pipelines using Azure Container Registry. Security and identity administrators responsible for enforcing least-privilege access in container image management will also benefit.

- Important notes if any  
To leverage repository permissions with ABAC, organizations need to configure Microsoft Entra ID and define appropriate attribute-based policies. This feature complements existing role-based access control (RBAC) but provides more granular control at the repository level. It is recommended to review and update access policies to align with least-privilege principles and operational requirements.  

For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The Azure update titled "Generally Available: Azure Container Registry Repository Permissions with Attribute-based Access Control (ABAC)" introduces fine-grained, attribute-driven access control capabilities for Azure Container Registry (ACR), enabling organizations to enforce least-privilege permissions on container image operations based on dynamic attributes of Microsoft Entra identities.

**Background and Purpose**  
Azure Container Registry is a managed Docker container registry service used to store and manage container images for deployment in Azure and other environments. Traditionally, ACR access control relied on role-based access control (RBAC) at the registry or repository scope, which can be coarse-grained and static. As organizations adopt zero-trust security models and require more granular, context-aware access policies, there is a need to control which identities can push or pull images based on attributes such as user, device, or environment properties. This update addresses this by integrating attribute-based access control (ABAC) into ACR repository permissions, allowing dynamic, attribute-driven authorization decisions.

**Specific Features and Detailed Changes**  
- **Repository-level ABAC Permissions:** Administrators can now define permissions at the repository level within an ACR instance, specifying which Microsoft Entra identities can perform actions like `push`, `pull`, or `delete` on container images based on attributes.  
- **Attribute Conditions:** Access policies can include conditions based on identity attributes (e.g., user department, device compliance state) or request context, enabling fine-grained control beyond static RBAC roles.  
- **Least-Privilege Enforcement:** By leveraging ABAC, organizations can minimize over-permissioning, granting only the necessary rights to identities under specific conditions, improving security posture.  
- **Integration with Microsoft Entra:** ABAC leverages Microsoft Entra ID (formerly Azure AD) attributes and claims, enabling seamless policy enforcement tied to identity properties and device states.

**Technical Mechanisms and Implementation Methods**  
- **Policy Definition:** Administrators define repository permissions using Azure CLI, Azure Portal, or ARM templates, specifying attribute-based conditions on identities. These policies are evaluated at runtime during authentication and authorization.  
- **Enforcement:** When a client attempts to push or pull images, ACR evaluates the request against ABAC policies by querying Microsoft Entra identity attributes and request context. If conditions are met, access is granted; otherwise, it is denied.  
- **Attribute Sources:** Attributes can include user properties (department, job title), device compliance status (via Microsoft Intune), or other claims issued by Microsoft Entra ID.  
- **Compatibility:** ABAC permissions complement existing RBAC roles; administrators can combine both for layered access control.

**Use Cases and Application Scenarios**  
- **DevOps Pipelines:** Restrict image publishing rights to specific service principals or users with verified device compliance, ensuring only authorized build agents can push images.  
- **Multi-Tenant Registries:** Enforce tenant-specific access by requiring user attributes to match tenant identifiers before allowing image consumption or publishing.  
- **Security Compliance:** Implement conditional access policies that prevent image pulls from non-compliant devices or users outside corporate networks.  
- **Least-Privilege Access:** Grant temporary or conditional permissions to contractors or external collaborators based on attributes like project membership or device state.

**Important Considerations and Limitations**  
- **Attribute Availability:** Effective ABAC enforcement depends on accurate and up-to-date identity attributes in Microsoft Entra; stale or missing attributes can lead to unintended access denials.  
- **Policy Complexity:** Overly complex attribute conditions may complicate troubleshooting and increase latency during authorization checks.  
- **Backward Compatibility:** Existing RBAC permissions remain valid; administrators should carefully plan migration or coexistence strategies to avoid conflicts.  
- **Audit and Monitoring:** Organizations should monitor access logs to verify ABAC policies behave as intended and adjust as needed.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** ABAC relies on Entra ID for identity attributes and claims, integrating with

---

### 20. Public Preview: Azure Kubernetes Service desktop 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Kubernetes Service desktop ](https://azure.microsoft.com/updates?id=526242)

**Update ID**: 526242
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) Desktop is now available in public preview, providing a modern, application-centric interface for managing AKS workloads.

- Key changes or new features  
AKS Desktop offers a guided, self-service experience built on existing AKS features and best practices. It leverages the open-source Headlamp project to deliver an intuitive GUI for deploying, monitoring, and managing Kubernetes clusters and applications. This tool simplifies complex Kubernetes operations, improves visibility into workloads, and streamlines cluster management without requiring deep Kubernetes CLI expertise.

- Target audience affected  
Developers and IT professionals who deploy and manage containerized applications on AKS will benefit from this update. It is especially useful for teams seeking a more user-friendly, visual approach to Kubernetes management within Azure.

- Important notes if any  
As a public preview, AKS Desktop may have limited features and is not recommended for production-critical environments yet. Users should provide feedback to help shape the final product. Access and usage details are available via the Azure portal and official documentation.

**Details**:

The Azure Kubernetes Service (AKS) desktop, now available in public preview, introduces a modern, application-centric user interface designed to simplify the deployment and management of containerized workloads on AKS clusters. This update addresses the complexity often faced by IT professionals and developers when interacting with Kubernetes resources by providing a guided, self-service experience that integrates best practices and leverages the open-source Headlamp project.

**Background and Purpose:**  
Kubernetes, while powerful, presents a steep learning curve due to its command-line-centric management and complex resource configurations. AKS desktop aims to lower this barrier by delivering a graphical interface tailored for AKS users, enabling more intuitive cluster and workload management. This initiative aligns with Azure’s goal to enhance developer productivity and operational efficiency by abstracting Kubernetes intricacies and providing actionable insights directly within the Azure ecosystem.

**Specific Features and Detailed Changes:**  
AKS desktop offers a rich, application-focused dashboard that allows users to visualize and manage Kubernetes workloads, namespaces, pods, services, and other resources with ease. Key features include:  
- **Guided Workload Deployment:** Step-by-step wizards to deploy applications, reducing manual YAML editing and potential misconfigurations.  
- **Resource Monitoring and Logs:** Integrated views for real-time metrics and logs, facilitating troubleshooting without switching tools.  
- **Role-Based Access Control (RBAC) Awareness:** The interface respects Azure AD and Kubernetes RBAC permissions, ensuring users only see and manage authorized resources.  
- **Namespace and Context Management:** Simplified switching between clusters and namespaces to streamline multi-environment operations.  
- **Extension of Headlamp Project:** Built upon the open-source Headlamp Kubernetes dashboard, AKS desktop adds Azure-specific integrations and support, ensuring a seamless experience tailored to AKS clusters.

**Technical Mechanisms and Implementation Methods:**  
AKS desktop is implemented as a web-based application that interacts with the Kubernetes API server of the AKS cluster. Authentication leverages Azure Active Directory tokens, ensuring secure and compliant access. The solution integrates Azure Monitor for container insights, pulling telemetry data to present health and performance metrics within the UI. By extending Headlamp, AKS desktop inherits a modular architecture, allowing extensibility and customization while maintaining compatibility with Kubernetes API versions supported by AKS.

**Use Cases and Application Scenarios:**  
- **DevOps and Developers:** Rapidly deploy and manage microservices without deep Kubernetes expertise.  
- **Cluster Operators:** Monitor cluster health and resource utilization with an intuitive interface, reducing reliance on CLI tools.  
- **Multi-tenant Environments:** Manage access and visibility across namespaces and clusters using RBAC-aware controls.  
- **Training and Onboarding:** Serve as a learning tool for teams new to Kubernetes by providing visual feedback and guided workflows.

**Important Considerations and Limitations:**  
As a public preview feature, AKS desktop may have limited support and could undergo significant changes before general availability. It currently supports clusters running Kubernetes versions compatible with Headlamp and may not expose all advanced Kubernetes features. Users should continue to rely on CLI tools and Azure Portal for critical or unsupported operations. Additionally, performance and scalability in very large clusters are yet to be fully validated.

**Integration with Related Azure Services:**  
AKS desktop tightly integrates with Azure Active Directory for authentication and authorization, ensuring secure access management. It leverages Azure Monitor Container Insights for telemetry and diagnostics, providing a unified monitoring experience. The tool complements Azure Portal and Azure CLI by offering a focused UI for Kubernetes workloads, enhancing the overall AKS management ecosystem.

In summary, the AKS desktop public preview provides IT professionals with a streamlined, application-centric interface for managing AKS workloads, combining open-source innovation with Azure’s security and monitoring capabilities to improve operational efficiency and reduce Kubernetes management complexity.

---

### 21. Generally Available: Pod sandboxing on AKS 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Pod sandboxing on AKS ](https://azure.microsoft.com/updates?id=526237)

**Update ID**: 526237
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now generally supports pod sandboxing, allowing containers to run inside dedicated pod virtual machines (VMs).

- Key changes or new features  
Pod sandboxing enhances security and workload isolation by running each pod within its own lightweight VM rather than sharing the underlying node OS kernel. This approach reduces attack surface and prevents noisy neighbor issues in multi-tenant or shared environments. Developers and IT professionals can now configure AKS clusters to enable pod VM isolation, improving compliance and security posture for sensitive or regulated workloads.

- Target audience affected  
This update primarily benefits developers building containerized applications on AKS and IT professionals managing Kubernetes clusters who require stronger isolation guarantees, especially in shared or multi-tenant scenarios.

- Important notes if any  
Enabling pod sandboxing may introduce additional resource overhead due to VM provisioning per pod, so capacity planning should account for this. Compatibility with existing tooling and monitoring should be validated, as pod VMs differ from traditional container runtimes. Refer to official AKS documentation for configuration details and best practices.

**Details**:

The Azure Kubernetes Service (AKS) update announcing the general availability of pod sandboxing introduces a significant enhancement in workload isolation and security by enabling containers to run within dedicated pod virtual machines (VMs) rather than sharing the underlying node OS kernel. This update addresses the inherent risks of multi-tenant and shared-node environments where containerized workloads might be vulnerable to kernel-level attacks or resource contention.

**Background and Purpose:**  
Traditionally, AKS runs multiple pods on shared nodes, where containers share the same OS kernel. While Kubernetes namespaces and cgroups provide logical isolation, they do not fully mitigate risks from kernel exploits or noisy neighbors. Pod sandboxing in AKS aims to elevate isolation by encapsulating each pod within its own lightweight VM, effectively creating a hardware-level boundary. This approach enhances security posture and workload isolation, which is critical for sensitive or compliance-driven applications.

**Specific Features and Changes:**  
- **Per-pod VM isolation:** Each pod runs inside a dedicated VM sandbox, isolating its kernel and system resources from other pods on the same node.  
- **Seamless Kubernetes integration:** Pod sandboxing is fully integrated into the AKS control plane and Kubernetes API, requiring minimal changes to existing manifests or deployment workflows.  
- **Support for standard container runtimes:** The sandboxed pods continue to support OCI-compliant container images and standard Kubernetes features such as networking, storage, and secrets.  
- **Performance optimizations:** The sandbox VMs are lightweight and optimized for fast startup and minimal overhead, preserving the agility and scalability of AKS.

**Technical Mechanisms and Implementation:**  
Pod sandboxing leverages a lightweight virtualization technology, such as Kata Containers or Azure’s own Hyper-V isolation, to instantiate a minimal VM per pod. This VM runs a stripped-down kernel and container runtime, isolating the pod’s processes from the host and other pods at the hardware virtualization layer. AKS manages lifecycle operations—creation, scaling, and termination—of these pod VMs transparently through the Kubernetes scheduler and kubelet, which have been enhanced to support sandboxed pods. Networking is handled via Azure CNI or other supported plugins, ensuring pod VMs integrate seamlessly into the cluster network fabric. Storage and volume mounts are virtualized and passed through to the sandbox VM securely.

**Use Cases and Application Scenarios:**  
- **Security-sensitive workloads:** Financial services, healthcare, and government applications requiring strict isolation and compliance benefit from reduced attack surfaces.  
- **Multi-tenant clusters:** Service providers or enterprises running multiple customers’ workloads on shared infrastructure can prevent cross-tenant interference.  
- **Legacy or untrusted code:** Running third-party or legacy containers with unknown security posture inside sandboxed pods minimizes risk to the host.  
- **Regulatory compliance:** Environments requiring kernel-level isolation to meet standards such as PCI-DSS, HIPAA, or FedRAMP.

**Important Considerations and Limitations:**  
- **Resource overhead:** Although optimized, pod VMs consume more CPU and memory than standard containers, potentially reducing node density. Capacity planning should account for this.  
- **Compatibility:** Some Kubernetes features or third-party tools that depend on direct node access or kernel modules may not be fully compatible with sandboxed pods.  
- **Startup latency:** Pod VM initialization introduces slightly higher startup latency compared to traditional containers, which may impact burst scaling scenarios.  
- **Cluster configuration:** Enabling pod sandboxing requires specific AKS cluster configurations and may not be available on all VM sizes or regions initially.

**Integration with Related Azure Services:**  
- **Azure Monitor and Azure Security Center:** Enhanced visibility and security posture management for sandboxed pods, including VM-level telemetry and threat detection.  
- **Azure Policy:** Ability to enforce policies that mandate pod sandboxing for specific namespaces or workloads.  
- **Azure Active Directory and RBAC:** Seamless integration for secure access control to sandboxed workloads.  
- **Azure DevOps and CI/CD pipelines:** Support for building

---

### 22. Generally Available: Managed namespaces on AKS 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Managed namespaces on AKS ](https://azure.microsoft.com/updates?id=526232)

**Update ID**: 526232
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) has introduced Managed Namespaces, now generally available, to simplify namespace management across AKS clusters.

- Key changes or new features  
Managed Namespaces automate the creation, configuration, and maintenance of Kubernetes namespaces within AKS clusters. This reduces manual setup efforts and minimizes risks of misconfiguration. It enables consistent namespace policies, access controls, and resource quotas to be centrally managed and propagated across clusters. The feature improves operational efficiency and governance for multi-tenant or multi-environment AKS deployments.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those responsible for cluster governance, security, and multi-tenant environments, will benefit from streamlined namespace management and enhanced consistency.

- Important notes if any  
Users should review existing namespace configurations to align with Managed Namespaces policies. This feature supports better scalability and reduces configuration drift but requires adoption of the new management approach for namespaces within AKS. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The Azure Kubernetes Service (AKS) update announcing the general availability of Managed Namespaces addresses the longstanding challenge of managing namespace configurations consistently and securely across multiple AKS clusters. Traditionally, namespace management in Kubernetes environments required manual creation and configuration on each cluster, which was error-prone and operationally complex, especially at scale. This update introduces a centralized, automated mechanism to provision and maintain namespaces, reducing misconfiguration risks and simplifying governance.

**Background and Purpose**  
Namespaces in Kubernetes provide a scope for names, enabling resource isolation, access control, and organizational boundaries within clusters. However, when operating multiple AKS clusters, IT teams had to replicate namespace configurations individually, often leading to inconsistencies and increased operational overhead. The Managed Namespaces feature was developed to streamline namespace lifecycle management by enabling centralized control, consistent policy enforcement, and automated synchronization across clusters.

**Specific Features and Detailed Changes**  
With Managed Namespaces now generally available, AKS users can define namespaces centrally and have them automatically provisioned and updated on target AKS clusters. Key features include:  
- **Central Namespace Definition:** Namespaces can be created and configured declaratively through Azure APIs or CLI, specifying labels, annotations, resource quotas, and role-based access control (RBAC) settings.  
- **Automated Synchronization:** Changes to namespace configurations are propagated automatically to all associated AKS clusters, ensuring consistency without manual intervention.  
- **Lifecycle Management:** Supports creation, update, and deletion of namespaces centrally, with changes reflected in real-time or near real-time on clusters.  
- **Integration with Azure RBAC:** Managed Namespaces leverage Azure Active Directory and Azure RBAC for fine-grained access control, aligning Kubernetes namespace permissions with Azure identity management.  
- **Policy Enforcement:** Integration with Azure Policy allows enforcement of compliance and security standards on namespaces.

**Technical Mechanisms and Implementation Methods**  
Managed Namespaces are implemented through a control plane component within AKS that interfaces with the Kubernetes API servers of the target clusters. The control plane monitors namespace definitions stored centrally (likely in Azure Resource Manager or a dedicated configuration store) and uses Kubernetes controllers or operators to reconcile the desired state with the actual state on each cluster. This reconciliation loop ensures that namespaces are created or updated as needed. The synchronization mechanism uses secure API calls authenticated via Azure AD, ensuring secure and auditable operations. RBAC settings are mapped from Azure roles to Kubernetes roles within the namespaces, facilitating seamless permission management.

**Use Cases and Application Scenarios**  
- **Multi-Cluster Management:** Organizations running multiple AKS clusters across regions or environments (dev, test, prod) can maintain consistent namespace configurations effortlessly.  
- **Governance and Compliance:** Centralized namespace management helps enforce organizational policies, resource quotas, and security standards uniformly.  
- **DevOps Automation:** Integrates with CI/CD pipelines to automate namespace provisioning as part of application deployment workflows.  
- **Resource Isolation:** Facilitates multi-tenant scenarios by ensuring namespaces are configured with appropriate access controls and resource limits.

**Important Considerations and Limitations**  
- Managed Namespaces require clusters to be registered and connected to the central management plane, which may introduce network and security considerations.  
- There may be latency between configuration changes and their propagation depending on cluster connectivity and scale.  
- Existing namespaces created manually may require reconciliation or migration to the managed model to avoid conflicts.  
- RBAC mappings depend on Azure AD integration; clusters not using Azure AD may have limited functionality.  
- Currently, the feature supports AKS clusters only; integration with other Kubernetes distributions is not provided.

**Integration with Related Azure Services**  
- **Azure Active Directory:** Provides identity and access management for namespace RBAC.  
- **Azure Policy:** Enables policy enforcement on namespaces for compliance and security.  
- **Azure Monitor and Log Analytics:** Can be used to track namespace provisioning events and audit changes.  
- **Azure DevOps/GitHub Actions:** Can integrate namespace management into infrastructure-as-code pipelines.

---

### 23. Public Preview: Azure Kubernetes Fleet Manager for Arc-enabled clusters 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Kubernetes Fleet Manager for Arc-enabled clusters ](https://azure.microsoft.com/updates?id=526227)

**Update ID**: 526227
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Compute, Azure Kubernetes Fleet Manager, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Fleet Manager has entered public preview with support for Azure Arc-enabled Kubernetes clusters.

- Key changes or new features  
The update enables centralized management of Kubernetes clusters across hybrid and multi-cloud environments through a unified control plane. Organizations can now onboard any CNCF-compliant Kubernetes cluster via Azure Arc and manage them consistently alongside Azure-native clusters. This simplifies cluster lifecycle management, policy enforcement, and monitoring at scale.

- Target audience affected  
Developers and IT professionals responsible for managing Kubernetes deployments in hybrid or multi-cloud scenarios, especially those leveraging Azure Arc for Kubernetes cluster governance.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in test environments before production use. It requires clusters to be CNCF-compliant and connected via Azure Arc. The unified management approach helps reduce operational complexity and improve governance across diverse Kubernetes environments.

For more details, visit: https://azure.microsoft.com/updates?id=526227

**Details**:

The Azure update titled "Public Preview: Azure Kubernetes Fleet Manager for Arc-enabled clusters" introduces enhanced capabilities for managing Kubernetes clusters across hybrid and multi-cloud environments by integrating Azure Kubernetes Fleet Manager with Azure Arc-enabled Kubernetes. This integration addresses the complexity and fragmentation typically encountered in managing distributed Kubernetes deployments.

**Background and Purpose**  
As organizations increasingly adopt hybrid and multi-cloud strategies, Kubernetes clusters often span on-premises data centers, edge locations, and multiple public clouds. Managing these clusters individually or through disparate tools leads to operational overhead, inconsistent policies, and security challenges. Azure Arc-enabled Kubernetes extends Azure management capabilities to any CNCF-compliant Kubernetes cluster, regardless of location. However, managing large fleets of such clusters at scale remained complex. The Azure Kubernetes Fleet Manager aims to centralize and simplify this management by providing a unified control plane. This update’s purpose is to bring Azure Arc-enabled Kubernetes clusters under the Fleet Manager umbrella, enabling seamless, scalable, and consistent management.

**Specific Features and Detailed Changes**  
- **Unified Fleet Management:** Azure Kubernetes Fleet Manager now supports onboarding and managing Azure Arc-enabled Kubernetes clusters, allowing IT teams to view, organize, and operate all clusters from a single pane of glass.  
- **Cluster Grouping and Hierarchies:** Users can create logical groupings or hierarchies of clusters (fleets) based on geography, environment, or business units, facilitating targeted policy application and operational actions.  
- **Policy and Configuration Consistency:** Integration with Azure Policy and GitOps enables consistent enforcement of security, compliance, and configuration policies across all Arc-enabled clusters within a fleet.  
- **Centralized Monitoring and Insights:** Fleet Manager aggregates telemetry and health data, providing unified dashboards and alerts for Arc-enabled clusters, improving observability and operational responsiveness.  
- **Lifecycle Management:** Streamlined onboarding, updating, and decommissioning of Arc-enabled Kubernetes clusters within the fleet, reducing manual intervention and errors.

**Technical Mechanisms and Implementation Methods**  
Azure Kubernetes Fleet Manager leverages Azure Arc’s control plane extension capabilities. When an Arc-enabled Kubernetes cluster is onboarded, it registers with Azure Resource Manager and connects securely via the Azure Arc agent. Fleet Manager uses this registration to discover and organize clusters into fleets. It employs Azure Policy for Kubernetes to enforce governance and integrates with GitOps operators like Flux or Argo CD for configuration management. Telemetry data is collected through Azure Monitor containers and aggregated in Azure Monitor workspaces. The Fleet Manager’s APIs and Azure Portal extensions provide the interface for managing fleets and clusters.

**Use Cases and Application Scenarios**  
- **Enterprise-scale Kubernetes Operations:** Large organizations managing hundreds or thousands of clusters across on-premises, edge, and multiple clouds can use Fleet Manager to reduce operational complexity.  
- **Regulated Industries:** Enforce compliance policies consistently across distributed clusters in finance, healthcare, or government sectors.  
- **Edge and IoT Deployments:** Manage Kubernetes clusters deployed at edge locations with limited connectivity, ensuring centralized policy and configuration management.  
- **DevOps and GitOps Pipelines:** Automate application deployment and configuration updates across fleets using integrated GitOps workflows.

**Important Considerations and Limitations**  
- **Public Preview Status:** As a preview feature, some capabilities may be subject to change, and SLAs are not guaranteed. Production use should be carefully evaluated.  
- **Supported Kubernetes Versions:** Only CNCF-compliant Kubernetes clusters supported by Azure Arc can be onboarded; clusters must meet version and configuration prerequisites.  
- **Network Connectivity:** Clusters require outbound connectivity to Azure endpoints for agent communication and telemetry. Limited or intermittent connectivity may impact functionality.  
- **Role-Based Access Control (RBAC):** Proper Azure RBAC and Kubernetes RBAC configurations are necessary to enable secure and effective management.  
- **Resource Costs:** Additional Azure resources such as Azure Monitor and Policy may incur costs depending on usage.

**Integration with Related Azure Services**  
- **Azure Arc:** Core enabling technology for extending Azure

---

### 24. Public Preview: Windows Server 2025 on AKS

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Windows Server 2025 on AKS](https://azure.microsoft.com/updates?id=526213)

**Update ID**: 526213
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now offers public preview support for Windows Server 2025 as a node operating system for Windows-based workloads.

- Key changes or new features  
The update enables customers to run Windows Server 2025 containers on AKS clusters, helping organizations modernize their Windows workloads and extend support beyond older Windows Server versions nearing end of support. This includes compatibility improvements and updated container images aligned with Windows Server 2025 features.

- Target audience affected  
Developers and IT professionals managing Windows containerized applications on AKS who need to upgrade to a supported Windows Server version to maintain security, compliance, and feature parity.

- Important notes if any  
This is a public preview feature, so it is recommended for testing and validation rather than production workloads at this time. Customers should plan migration strategies accordingly and monitor Azure updates for general availability announcements. Existing AKS clusters will require node image upgrades to leverage Windows Server 2025 support.

**Details**:

The recent Azure update announces the public preview of Windows Server 2025 support on Azure Kubernetes Service (AKS), addressing the need for organizations to modernize Windows-based container workloads as legacy Windows Server versions near end-of-support. This update enables IT professionals to deploy and manage Windows Server 2025 container images within AKS clusters, facilitating enhanced security, performance, and feature parity with the latest Windows Server capabilities.

**Background and Purpose:**  
Many enterprises rely on Windows Server containers to run critical applications on AKS, but the lifecycle of older Windows Server versions (such as 2019 or 2022) is limited by Microsoft’s support policies. As these versions approach retirement, organizations face operational risks and compliance challenges. Introducing Windows Server 2025 support in AKS allows customers to future-proof their containerized Windows workloads by leveraging the latest OS improvements while maintaining the benefits of Kubernetes orchestration.

**Specific Features and Detailed Changes:**  
- **Windows Server 2025 Container Images:** AKS now supports Windows Server 2025 container base images, enabling developers to build and run containers with updated OS components, security patches, and performance enhancements.  
- **Compatibility with AKS Node Pools:** Customers can create Windows Server 2025 node pools within their AKS clusters, allowing mixed OS versions in a single cluster for gradual migration.  
- **Improved Security and Compliance:** Windows Server 2025 includes enhanced security features such as improved kernel hardening and updated cryptographic libraries, which are now available within AKS-hosted containers.  
- **Support for Latest Kubernetes Versions:** The preview ensures compatibility with recent Kubernetes releases, enabling the use of new Kubernetes features alongside Windows Server 2025 workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Node Pool Provisioning:** Users can provision Windows Server 2025 node pools via Azure CLI or Azure Portal by specifying the new OS image SKU during node pool creation.  
- **Container Image Management:** Developers must build or obtain container images based on Windows Server 2025 base layers, which can be pushed to Azure Container Registry (ACR) or other container registries.  
- **Cluster Upgrades and Mixed OS Support:** AKS supports running multiple node pools with different Windows Server versions, facilitating phased upgrades without downtime.  
- **Networking and Storage Compatibility:** Windows Server 2025 nodes support existing AKS networking models (such as Azure CNI) and storage integrations, ensuring seamless integration with Azure infrastructure.

**Use Cases and Application Scenarios:**  
- **Modernizing Legacy Windows Applications:** Organizations can containerize and migrate legacy Windows Server applications to AKS using the latest OS platform, improving maintainability and scalability.  
- **Hybrid Workloads:** Enterprises running mixed Linux and Windows workloads can leverage AKS’s multi-OS support with updated Windows Server nodes.  
- **Security-Sensitive Environments:** Customers requiring up-to-date security patches and compliance certifications benefit from running Windows Server 2025 containers in AKS.  
- **DevOps and CI/CD Pipelines:** Development teams can build, test, and deploy Windows Server 2025 container images within AKS, streamlining application lifecycle management.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview, Windows Server 2025 support in AKS may have limited SLA guarantees and could undergo changes before general availability.  
- **Image Availability:** Official Windows Server 2025 container base images must be used to ensure compatibility; custom images should be tested thoroughly.  
- **Feature Parity:** Some Windows Server 2025 features may not yet be fully supported within containerized environments or AKS node pools.  
- **Resource Requirements:** Windows Server 2025 nodes may have different resource profiles; capacity planning should account for potential changes in CPU, memory, and storage needs.  
- **Upgrade Path:** Customers should plan for gradual migration and validate application compatibility before decommissioning older Windows Server nodes.

**Integration with Related Azure Services

---

### 25. Generally Available: AKS Automatic pod readiness SLA

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: AKS Automatic pod readiness SLA](https://azure.microsoft.com/updates?id=526208)

**Update ID**: 526208
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) Automatic clusters now include a Service Level Agreement (SLA) for pod readiness.

- Key changes or new features  
The new SLA guarantees that eligible pods will meet readiness criteria within five minutes at the 99.9th percentile. This means that in 99.9% of cases, pods will become ready within five minutes after deployment or scaling events, improving reliability and predictability for workloads running on AKS Automatic clusters.

- Target audience affected  
This update primarily impacts developers and IT professionals managing containerized applications on AKS Automatic clusters, especially those running mission-critical workloads that require high availability and fast pod readiness.

- Important notes if any  
The SLA applies only to eligible pods running on AKS Automatic clusters. Customers can now confidently deploy critical applications on AKS with improved assurance of pod readiness timing, aiding in operational planning and SLA commitments. For detailed terms and eligibility, refer to the official Azure SLA documentation.

**Details**:

The recent Azure update announces the general availability of the Automatic Pod Readiness Service Level Agreement (SLA) for Azure Kubernetes Service (AKS) clusters, marking a significant enhancement in AKS reliability guarantees for mission-critical containerized workloads.

**Background and Purpose**  
Kubernetes workloads rely heavily on pod readiness to ensure that applications are fully initialized and ready to serve traffic before being exposed via services or ingress controllers. Prior to this update, while AKS provided robust cluster management and scaling capabilities, there was no formal SLA specifically guaranteeing pod readiness times. This gap made it challenging for enterprises running latency-sensitive or mission-critical applications to have contractual assurances on pod startup and readiness performance. The introduction of an SLA focused on pod readiness addresses this by providing a quantifiable and enforceable commitment, thereby increasing confidence in AKS for production-grade deployments.

**Specific Features and Detailed Changes**  
The core feature introduced is a pod readiness SLA that guarantees eligible pods will meet Kubernetes readiness criteria within five minutes at the 99.9th percentile. This means that for 99.9% of pod startups, readiness probes will succeed within five minutes of pod creation, ensuring timely availability of application instances. The SLA applies specifically to AKS clusters configured with the Automatic cluster management feature, which leverages Azure’s managed control plane and optimized node provisioning.

**Technical Mechanisms and Implementation Methods**  
To achieve this SLA, AKS integrates enhanced telemetry and pod lifecycle monitoring within the managed control plane. The system continuously tracks pod readiness probe results and startup durations, correlating this data with underlying infrastructure health metrics such as node provisioning times, container image pulls, and network initialization. AKS automatically optimizes scheduling and resource allocation to minimize delays, including pre-pulling container images and prioritizing pod startup on healthy nodes. Additionally, AKS may leverage Azure’s accelerated networking and storage subsystems to reduce I/O bottlenecks affecting pod initialization. The SLA is enforced through backend monitoring and customer support escalation paths if the readiness targets are not met.

**Use Cases and Application Scenarios**  
This SLA is particularly valuable for organizations deploying latency-sensitive microservices, real-time data processing pipelines, or customer-facing applications requiring high availability and rapid scaling. For example, e-commerce platforms experiencing traffic surges can rely on the SLA to ensure new pods become ready quickly during autoscaling events. Similarly, financial services running event-driven architectures benefit from predictable pod readiness to maintain compliance and service-level objectives. The SLA also supports DevOps teams by providing measurable performance targets that can be integrated into CI/CD pipelines and operational dashboards.

**Important Considerations and Limitations**  
The SLA applies only to pods that meet certain eligibility criteria defined by AKS, such as those running on supported node types and configured with standard readiness probes. Custom or complex readiness checks outside typical Kubernetes probe mechanisms may not be covered. The five-minute readiness window is measured from pod creation to readiness probe success, so workloads with inherently long initialization times (e.g., large JVM startups) should be designed accordingly. Customers must ensure their pod specifications and cluster configurations align with AKS best practices to benefit fully from the SLA. Additionally, the SLA does not cover pod readiness impacted by user application bugs or external dependencies.

**Integration with Related Azure Services**  
This pod readiness SLA complements other AKS features such as Cluster Autoscaler, Azure Monitor for containers, and Azure Policy for Kubernetes, enabling holistic management of cluster health and compliance. Integration with Azure Monitor allows customers to visualize pod readiness metrics and set alerts aligned with the SLA thresholds. When combined with Azure DevOps or GitHub Actions, teams can automate deployment validations against readiness guarantees. Furthermore, the SLA enhances the reliability foundation for Azure Arc-enabled Kubernetes clusters, where consistent readiness performance is critical across hybrid environments.

In summary, the AKS Automatic Pod Readiness SLA provides a formal, measurable guarantee that eligible pods will become ready within five minutes at the 99.9th percentile, leveraging enhanced AKS control plane telemetry and optimization to support mission-critical workloads requiring

---

### 26. Public Preview: AKS Automatic managed system node pools

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: AKS Automatic managed system node pools](https://azure.microsoft.com/updates?id=526203)

**Update ID**: 526203
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) introduced Public Preview of Automatic managed system node pools.

- Key changes or new features  
This feature automates the provisioning, scaling, patching, and availability management of system node pools in AKS clusters. It reduces manual operational overhead by handling lifecycle management tasks for system node pools, ensuring they remain healthy and up-to-date without user intervention. This enables seamless scaling aligned with cluster demands and automatic updates to maintain security and reliability.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those responsible for cluster infrastructure and operations, will benefit from reduced maintenance efforts and improved system node pool reliability.

- Important notes if any  
As a public preview feature, it may have limited regional availability and could undergo changes before general availability. Users should test in non-production environments and review Azure documentation for any prerequisites or limitations. This feature currently focuses on system node pools, not user node pools.  

For more details, visit: https://azure.microsoft.com/updates?id=526203

**Details**:

The Azure Kubernetes Service (AKS) update introducing the Public Preview of Automatic Managed System Node Pools addresses the operational complexity and resource overhead associated with provisioning, scaling, patching, and maintaining system node pools in AKS clusters. Traditionally, system node pools—critical for running cluster infrastructure components such as the kube-system pods—require manual management to ensure availability, security, and performance, which can detract from core application development efforts.

This update enables AKS to automatically manage system node pools, significantly reducing the administrative burden on IT teams. The key feature is the automation of lifecycle management tasks for system node pools, including automatic scaling based on workload demands, seamless patching to maintain security and compliance, and proactive availability management to minimize downtime. This is achieved through integration with AKS control plane enhancements and Azure infrastructure services that monitor node health and performance metrics, triggering automated remediation actions without manual intervention.

Technically, the implementation leverages AKS’s enhanced control plane capabilities to orchestrate system node pool operations. Automatic scaling is driven by cluster metrics and predefined policies, while patching is coordinated during maintenance windows with minimal disruption. The system node pools are provisioned using managed identities and Azure Resource Manager templates, ensuring secure and consistent deployments. This automation abstracts the complexity of node pool lifecycle management, allowing clusters to maintain optimal operational states dynamically.

Use cases for this feature include production AKS clusters running critical workloads where high availability and security are paramount, and where operational efficiency is desired to reduce overhead. It is particularly beneficial for organizations adopting GitOps or DevOps practices, enabling infrastructure teams to focus on application delivery rather than cluster maintenance. Additionally, this feature supports scenarios requiring compliance with strict patching and uptime SLAs by automating routine maintenance tasks.

Important considerations include the current preview status, which means the feature may have limitations or require specific cluster configurations to enable. Users should evaluate compatibility with existing node pool customizations and confirm that automatic scaling policies align with workload requirements. Monitoring and alerting should be configured to track automated actions and cluster health. Furthermore, integration with Azure Policy and Azure Monitor enhances governance and observability of the managed system node pools.

Integration with related Azure services is seamless: Azure Monitor provides telemetry and alerting for node pool health; Azure Policy can enforce compliance on node pool configurations; and Azure Arc can extend management capabilities to hybrid environments. This update complements AKS’s existing managed node pool features by extending automation to system node pools, thereby unifying cluster management under a consistent operational model.

In summary, the AKS Automatic Managed System Node Pools public preview introduces automated lifecycle management for critical system node pools, streamlining operational tasks such as scaling, patching, and availability management, which enhances cluster reliability and security while freeing IT resources to focus on application innovation.

---

### 27. Public Preview: Add durability to AI agents in Azure Functions using Microsoft Agent Framework

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Add durability to AI agents in Azure Functions using Microsoft Agent Framework](https://azure.microsoft.com/updates?id=526179)

**Update ID**: 526179
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Microsoft has introduced a public preview integration of the Microsoft Agent Framework with Azure Functions Durable extension, enabling durable orchestration for AI agents.

- Key changes or new features  
This update allows developers to build and host production-grade AI agents with enhanced reliability and stateful orchestration by leveraging Azure Functions’ durable capabilities. The durable extension ensures AI agents can maintain state, handle retries, and recover from failures seamlessly, improving robustness in long-running workflows.

- Target audience affected  
Developers and IT professionals building AI-driven applications and conversational agents who require scalable, resilient, and stateful orchestration in Azure Functions will benefit from this update.

- Important notes if any  
As this feature is in public preview, it is recommended to test thoroughly before production deployment. Users should monitor the Azure Updates page for general availability announcements and review the preview limitations and documentation to understand any constraints or breaking changes.  

For more details, visit: https://azure.microsoft.com/updates?id=526179

**Details**:

The recent Azure update introduces a public preview feature that enhances the Microsoft Agent Framework by integrating it with Azure Functions’ durable extension, enabling the creation of durable, reliable, and production-grade AI agents. This update addresses the need for resilient orchestration and stateful management of AI-driven workflows within serverless environments.

**Background and Purpose**  
AI agents—autonomous software entities capable of performing tasks, making decisions, and interacting with users or systems—are increasingly used in complex applications such as customer support, automation, and intelligent workflows. However, building these agents to be reliable and stateful, especially in serverless architectures, poses challenges due to the ephemeral nature of functions and the need for durable state management. The update aims to solve this by combining the Microsoft Agent Framework, which simplifies AI agent development, with Azure Functions Durable extension, which provides durable orchestration and state persistence.

**Specific Features and Detailed Changes**  
- **Durable Extension Integration:** The Microsoft Agent Framework now supports the Durable Functions extension, allowing AI agents to maintain state across multiple function invocations and long-running workflows.  
- **Stateful Orchestration:** Agents can orchestrate complex, multi-step processes with checkpoints, retries, and event-driven triggers, ensuring resilience against failures or restarts.  
- **Production-Grade Reliability:** The integration supports scalable, fault-tolerant execution of AI agents, making them suitable for production environments.  
- **Simplified Development:** Developers can leverage familiar Durable Functions programming models (orchestrator functions, activity functions) within the Agent Framework, reducing complexity in managing agent lifecycles and state.

**Technical Mechanisms and Implementation Methods**  
Under the hood, the Microsoft Agent Framework leverages Durable Functions’ orchestration context to persist agent state in Azure Storage (or other supported durable stores). Orchestrator functions manage the AI agent’s workflow, invoking activity functions that perform discrete tasks such as calling AI models, processing data, or interacting with external APIs. The framework handles durable timers, event raising, and state checkpoints, enabling agents to pause and resume seamlessly. Developers implement agents as orchestrator functions, defining the logic for decision-making and task delegation, while the framework manages underlying state persistence and fault tolerance.

**Use Cases and Application Scenarios**  
- **Conversational AI:** Building chatbots or virtual assistants that maintain context over long conversations and complex interactions.  
- **Automated Workflows:** Orchestrating multi-step automation processes that involve AI decision points, such as document processing or customer onboarding.  
- **Intelligent Monitoring:** Agents that continuously monitor systems or data streams, reacting to events with durable state tracking.  
- **Multi-turn AI Interactions:** Scenarios requiring agents to manage multi-turn dialogues or multi-stage decision trees reliably.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- **State Storage Costs:** Durable Functions rely on Azure Storage for state persistence, which may incur additional costs depending on usage patterns.  
- **Latency and Execution Time:** Durable orchestrations introduce some latency due to checkpointing and state management; not suitable for ultra-low-latency scenarios.  
- **Complexity in Debugging:** Durable Functions’ asynchronous and event-driven nature can complicate debugging and monitoring, requiring appropriate tooling and logging strategies.

**Integration with Related Azure Services**  
- **Azure Functions:** Core compute platform hosting the durable orchestrations and activity functions.  
- **Azure Storage:** Provides the backend for durable state persistence (blobs, queues, tables).  
- **Azure Cognitive Services / OpenAI:** AI models and APIs that agents can invoke within activity functions for natural language understanding, vision, or other AI capabilities.  
- **Azure Monitor and Application Insights:** For monitoring agent performance, logging, and diagnostics.  
- **Azure Logic Apps / Event Grid:** Can be integrated for event-driven triggers or to extend orchestration workflows beyond Azure

---

### 28. Public Preview: Cross region pool association support for Azure Virtual Network Manager IP address management

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Cross region pool association support for Azure Virtual Network Manager IP address management](https://azure.microsoft.com/updates?id=526174)

**Update ID**: 526174
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure Virtual Network Manager

**Summary**:

- What was updated  
Azure Virtual Network Manager (AVNM) IP Address Management (IPAM) now supports cross-region pool association in public preview.

- Key changes or new features  
Developers and IT professionals can associate a single IPAM pool with virtual networks spanning multiple Azure regions. This enhancement simplifies IP address space management by enabling centralized governance and consistent CIDR block allocation across regions. It reduces complexity and potential errors when managing multi-region network environments.

- Target audience affected  
Network administrators, cloud architects, and developers managing Azure virtual networks and IP address spaces across multiple regions will benefit from this update.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should review any limitations or prerequisites in the official documentation before adoption. The update aims to improve scalability and governance in large, distributed Azure deployments.

For more details, visit: https://azure.microsoft.com/updates?id=526174

**Details**:

The recent Azure update introduces public preview support for cross-region pool association within Azure Virtual Network Manager’s (AVNM) IP Address Management (IPAM) capabilities, addressing the complexities of managing IP address spaces across multiple Azure regions.

**Background and Purpose:**  
In large-scale, multi-region Azure deployments, managing IP address spaces consistently and avoiding CIDR overlaps is critical yet challenging. Previously, IPAM pools in AVNM were region-scoped, requiring separate pools per region and complicating governance, increasing the risk of misconfiguration and inefficient utilization. This update enables a single IPAM pool to be associated with virtual networks (VNets) across multiple regions, streamlining IP address governance and ensuring uniform CIDR allocation policies.

**Specific Features and Changes:**  
- **Cross-region IPAM Pool Association:** A single IP address pool can now be linked to VNets deployed in different Azure regions, breaking the prior regional boundary constraint.  
- **Simplified IP Governance:** Centralized management of IP address spaces reduces administrative overhead and potential errors in CIDR block assignments.  
- **Consistent CIDR Allocation:** Ensures that IP address ranges allocated to VNets across regions do not overlap, maintaining network isolation and connectivity integrity.

**Technical Mechanisms and Implementation:**  
Azure Virtual Network Manager acts as a centralized network management service that orchestrates IPAM pools and their associations with VNets. With this update, the IPAM pool resource model has been extended to support multi-region scope, allowing the pool’s CIDR ranges to be referenced by VNets regardless of their region. Internally, AVNM maintains a global state of IP allocations within the pool, enforcing non-overlapping CIDR assignments and validating new associations against existing allocations. The association is managed declaratively via ARM templates, Azure CLI, or PowerShell, enabling infrastructure-as-code practices.

**Use Cases and Application Scenarios:**  
- **Global Enterprise Networks:** Organizations with VNets spanning multiple regions can centrally manage IP address spaces, simplifying network design and reducing fragmentation.  
- **Multi-Region Hub-and-Spoke Architectures:** Central IPAM pools can allocate CIDRs to spokes in different regions, facilitating consistent routing and security policies.  
- **Hybrid and Multi-Cloud Connectivity:** Ensures predictable IP address management when integrating on-premises networks or other cloud environments with Azure VNets distributed globally.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As a preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- **Regional Service Availability:** While IPAM pools can be associated cross-region, underlying VNets and their resources remain region-specific.  
- **Quota and Size Constraints:** IPAM pool CIDR sizes and the number of associations per pool may have limits; users should consult the latest Azure documentation for quotas.  
- **Compatibility:** Existing IPAM configurations may require review to leverage cross-region associations effectively without conflicts.

**Integration with Related Azure Services:**  
- **Azure Virtual Network Manager:** Core service enabling centralized network and IP address management.  
- **Azure Resource Manager (ARM):** Infrastructure-as-code deployment and management of IPAM pools and associations.  
- **Azure Policy:** Can be used to enforce IP address management policies across subscriptions and management groups.  
- **Azure Firewall and Network Security Groups (NSGs):** Benefit from consistent IP addressing for defining rules across regions.  
- **Azure ExpressRoute and VPN Gateway:** Predictable IP addressing simplifies routing configurations in hybrid connectivity scenarios.

In summary, the cross-region pool association feature in Azure Virtual Network Manager’s IPAM enhances multi-region network management by allowing a unified IP address pool to govern VNets across different Azure regions. This reduces complexity, enforces consistent CIDR allocation, and supports scalable, global network architectures, making it a valuable capability for enterprises managing extensive Azure network footprints.

---

### 29. Generally Available: Azure Virtual Network Manager address overlap prevention in mesh 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Virtual Network Manager address overlap prevention in mesh ](https://azure.microsoft.com/updates?id=526169)

**Update ID**: 526169
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure Virtual Network Manager

**Summary**:

- What was updated  
Azure Virtual Network Manager’s address space overlap prevention in mesh is now generally available.

- Key changes or new features  
This feature prevents unintended IP address space overlaps across virtual networks within a mesh topology. By enforcing address space validation, it reduces the risk of dropped traffic caused by overlapping address ranges. It enhances network reliability and governance in complex multi-virtual network environments managed through Azure Virtual Network Manager.

- Target audience affected  
Developers and IT professionals managing large-scale Azure virtual network deployments, especially those using mesh topologies with multiple interconnected VNets, will benefit from improved network stability and simplified governance.

- Important notes if any  
Implementing address overlap prevention requires configuring Azure Virtual Network Manager policies to enforce non-overlapping address spaces. This update helps avoid connectivity issues and supports better compliance with network design best practices. Users should review existing VNet address spaces to ensure compatibility before enabling this feature.

**Details**:

The Azure Virtual Network Manager (AVNM) address space overlap prevention in mesh, now generally available, is a critical enhancement designed to improve network reliability and governance in complex multi-virtual network (VNet) topologies. This update addresses a common and impactful issue where overlapping IP address spaces across VNets connected in a mesh topology cause traffic drops and connectivity failures, thereby disrupting application availability and network performance.

**Background and Purpose:**  
In large-scale Azure deployments, organizations often deploy multiple VNets interconnected through mesh topologies to enable broad communication across workloads, environments, or regions. However, when VNets have overlapping IP address ranges, routing conflicts arise, leading to dropped packets and unpredictable network behavior. Prior to this update, detecting and preventing such overlaps required manual configuration checks and complex governance policies. The purpose of this update is to automate and enforce address space uniqueness within a managed mesh, thereby reducing operational overhead and increasing network reliability.

**Specific Features and Detailed Changes:**  
The key feature introduced is automated address space overlap detection and prevention within AVNM-managed mesh topologies. When creating or updating a mesh, AVNM now validates the address spaces of all participating VNets to ensure no overlaps exist. If an overlap is detected, the operation is blocked or flagged, preventing the mesh from being deployed or updated with conflicting address spaces. This feature integrates seamlessly with AVNM’s existing centralized network management capabilities, including policy enforcement and connectivity topology management.

**Technical Mechanisms and Implementation Methods:**  
Technically, AVNM maintains a global view of all VNets included in a mesh. It performs real-time validation of the address prefixes configured on each VNet against the aggregated address spaces in the mesh. This validation occurs during mesh creation and updates, leveraging Azure Resource Manager (ARM) APIs and internal state synchronization to ensure consistency. The prevention mechanism enforces strict non-overlapping CIDR blocks across all VNets in the mesh, leveraging AVNM’s control plane to block conflicting configurations before they propagate to the data plane. This proactive validation reduces runtime network errors caused by IP conflicts.

**Use Cases and Application Scenarios:**  
This update is particularly valuable in scenarios such as:  
- Large enterprises managing multiple VNets across departments or subsidiaries that require mesh connectivity without IP conflicts.  
- Service providers or managed service environments where multiple customer VNets are interconnected in a shared mesh topology.  
- Multi-region or hybrid cloud architectures where VNets are interconnected for failover, disaster recovery, or data replication, requiring strict IP governance.  
- DevOps environments where automation scripts or Infrastructure as Code (IaC) templates provision VNets and meshes, benefiting from automated overlap prevention to avoid deployment failures.

**Important Considerations and Limitations:**  
While the overlap prevention feature enhances reliability, it requires that all VNets intended to be part of a mesh be registered and managed through AVNM. Overlaps outside of AVNM-managed meshes are not detected by this feature. Additionally, existing meshes with overlapping address spaces must be remediated before enabling this feature. Careful IP address planning remains essential, especially in hybrid or multi-cloud scenarios where external networks connect to Azure VNets. The feature currently focuses on IPv4 address spaces; IPv6 support should be verified based on the latest AVNM documentation.

**Integration with Related Azure Services:**  
This update complements Azure Virtual Network Manager’s broader capabilities, including centralized connectivity topology management, security policy enforcement, and monitoring. It integrates with Azure Resource Manager for deployment and policy compliance and works alongside Azure Firewall, Azure Network Watcher, and Azure Monitor to provide comprehensive network governance and diagnostics. Organizations leveraging Azure ExpressRoute or VPN Gateway for hybrid connectivity benefit indirectly by ensuring their Azure VNets are free from internal IP conflicts, reducing troubleshooting complexity.

In summary, the general availability of address space overlap prevention in Azure Virtual Network Manager mesh significantly enhances multi-VNet mesh deployments by automating conflict detection and enforcing IP address uniqueness, thereby improving network stability, simplifying governance, and reducing operational risks in complex Azure network architectures.

---

### 30. Public Preview: Azure Functions support for Node.js 24 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Functions support for Node.js 24 ](https://azure.microsoft.com/updates?id=526077)

**Update ID**: 526077
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions now supports Node.js 24 in public preview, enabling developers to build and deploy serverless functions using the latest Node.js runtime.

- Key changes or new features  
Developers can develop Azure Functions locally with Node.js 24 and deploy them on both Windows and Linux environments. New Windows-based Function Apps targeting Node.js 24 default to 64-bit to ensure compatibility, as 32-bit Windows systems are no longer supported for this runtime.

- Target audience affected  
This update primarily impacts developers building serverless applications with Azure Functions using Node.js, as well as IT professionals managing Azure Function Apps and runtime environments.

- Important notes if any  
Node.js 24 support excludes 32-bit Windows systems; therefore, existing Function Apps on 32-bit Windows need migration or adjustment. Testing locally with Node.js 24 is recommended before deployment. This is a public preview feature, so users should evaluate it accordingly before production use.  

For more details, visit: https://azure.microsoft.com/updates?id=526077

**Details**:

The recent Azure Functions update introduces public preview support for Node.js 24, enabling developers to build and deploy serverless functions using the latest Node.js runtime on both Windows and Linux environments. This enhancement aligns Azure Functions with the current Node.js Long-Term Support (LTS) release, ensuring access to the newest JavaScript features, performance improvements, and security patches.

**Background and Purpose:**  
Node.js is a widely adopted runtime for serverless applications due to its event-driven, non-blocking I/O model. Azure Functions traditionally supports multiple Node.js versions, but keeping pace with the latest LTS releases is critical for performance, security, and developer productivity. Node.js 24 introduces updated V8 engine capabilities, improved diagnostics, and enhanced ECMAScript support. By adding Node.js 24 support, Azure Functions empowers developers to leverage these advancements in their serverless workloads, ensuring modern, efficient, and secure function execution.

**Specific Features and Detailed Changes:**  
- **Runtime Support:** Azure Functions now supports Node.js 24 in public preview on both Windows and Linux platforms.  
- **Local Development:** Developers can build and test functions locally using the Azure Functions Core Tools configured with Node.js 24, streamlining the development lifecycle.  
- **Deployment:** Functions developed with Node.js 24 can be deployed seamlessly to Azure Functions, maintaining compatibility across environments.  
- **Default Architecture on Windows:** Due to Node.js 24 dropping support for 32-bit Windows systems, new Windows-based Function Apps targeting Node.js 24 default to 64-bit architecture to ensure runtime compatibility and stability.

**Technical Mechanisms and Implementation Methods:**  
Azure Functions integrates Node.js 24 by updating the underlying runtime environment and the Azure Functions host to recognize and execute functions using the new Node.js version. The Azure Functions Core Tools have been updated to allow local invocation and debugging with Node.js 24. The platform automatically provisions the appropriate runtime environment during deployment, selecting the 64-bit architecture on Windows where necessary. This update requires developers to specify the Node.js 24 runtime in their function app configuration (e.g., via the `FUNCTIONS_WORKER_RUNTIME` and `WEBSITE_NODE_DEFAULT_VERSION` settings).

**Use Cases and Application Scenarios:**  
- **Modern JavaScript Applications:** Developers can utilize the latest ECMAScript features and syntax improvements in serverless functions.  
- **Performance-Critical Functions:** Node.js 24’s V8 engine enhancements can improve execution speed and reduce cold start times.  
- **Security-Sensitive Workloads:** Updated Node.js security patches help protect serverless functions from known vulnerabilities.  
- **Cross-Platform Development:** Consistent runtime behavior across Windows and Linux environments supports hybrid deployment strategies.

**Important Considerations and Limitations:**  
- **32-bit Windows Unsupported:** Node.js 24 does not support 32-bit Windows; hence, Windows Function Apps using Node.js 24 must run on 64-bit architecture. Existing 32-bit apps will require migration.  
- **Preview Status:** As a public preview feature, Node.js 24 support may have limited SLA and could undergo changes before general availability. Production workloads should evaluate stability accordingly.  
- **Dependency Compatibility:** Some Node.js modules or native add-ons may not yet be fully compatible with Node.js 24, necessitating testing and potential updates.  
- **Azure Functions Version:** Ensure the Azure Functions runtime version in use supports Node.js 24; upgrading the runtime may be required.

**Integration with Related Azure Services:**  
Node.js 24 functions can interact seamlessly with other Azure services such as Azure Cosmos DB, Azure Event Grid, Azure Storage, and Azure API Management. The updated runtime supports the latest Azure SDKs optimized for Node.js 24, enabling improved performance and new features. Additionally, integration with Azure DevOps and GitHub Actions for CI/CD pipelines can leverage the updated Azure Functions Core Tools supporting Node.js 24, facilitating automated build, test, and deployment workflows.

In summary, the

---

### 31. Public Preview: Azure Functions support for Java 25 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Functions support for Java 25 ](https://azure.microsoft.com/updates?id=526072)

**Update ID**: 526072
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions now supports Java 25 in public preview, enabling developers to build and deploy serverless functions using the latest Java runtime.

- Key changes or new features  
Developers can develop Azure Functions locally with Java 25 and deploy them on both Windows and Linux environments. This update offers enhanced security features, a longer support lifecycle, and ensures continued compatibility with Azure Functions runtime.

- Target audience affected  
Java developers building serverless applications on Azure Functions, DevOps engineers managing function deployments, and IT professionals overseeing runtime environments.

- Important notes if any  
This support is currently in public preview, so it may not be recommended for production workloads yet. Developers should test their applications thoroughly when upgrading to Java 25 to ensure compatibility. Existing Azure Functions apps can be upgraded to leverage the new runtime benefits.  

For more details, visit: https://azure.microsoft.com/updates?id=526072

**Details**:

The recent Azure Functions update introduces public preview support for Java 25, enabling developers to build and deploy serverless functions using the latest Java runtime on both Windows and Linux environments. This update addresses the need for modern, secure, and long-term supported Java versions within Azure Functions, ensuring that applications can leverage the newest language features and runtime improvements while maintaining seamless integration with the Azure serverless ecosystem.

**Background and Purpose**  
Java remains one of the most widely used programming languages in enterprise and cloud-native applications. Azure Functions historically supported multiple Java versions, but with the release of Java 25, there is a demand to adopt newer language enhancements, improved performance, and extended security support. This update aims to provide developers with the ability to upgrade existing functions or create new ones using Java 25, thereby future-proofing their serverless applications and aligning with Java’s long-term support (LTS) strategy.

**Specific Features and Detailed Changes**  
- **Java 25 Runtime Support:** Azure Functions now supports Java 25 as a runtime option, available for both Windows and Linux-based function apps.  
- **Local Development and Deployment:** Developers can build and test Java 25 functions locally using the Azure Functions Core Tools and then deploy them directly to Azure.  
- **Enhanced Security:** Java 25 includes important security fixes and improvements, which are now available to Azure Functions workloads.  
- **Longer Support Window:** By adopting Java 25, applications benefit from Oracle’s or OpenJDK’s extended support lifecycle, reducing the need for frequent runtime upgrades.  
- **Compatibility:** The update ensures that Azure Functions’ programming model, triggers, and bindings remain fully compatible with Java 25, minimizing migration friction.

**Technical Mechanisms and Implementation Methods**  
Azure Functions uses custom handlers and language workers to support multiple runtimes. For Java 25, the Azure Functions Java worker has been updated to recognize and execute functions compiled against the Java 25 runtime. The runtime environment on Azure hosts is provisioned with the Java 25 JDK, ensuring that function apps run within a fully compatible JVM. Developers can specify the Java version in the function app configuration or during deployment via Azure CLI, ARM templates, or Azure Portal settings. Local development leverages updated Azure Functions Core Tools that support Java 25, including debugging and packaging capabilities.

**Use Cases and Application Scenarios**  
- **Modernizing Legacy Functions:** Organizations can upgrade existing Java-based serverless functions to Java 25 to leverage new language features and performance improvements.  
- **Security-Sensitive Applications:** Applications requiring the latest security patches and compliance standards benefit from the updated runtime.  
- **Long-Lived Serverless Apps:** Functions with extended maintenance windows can rely on the longer support lifecycle of Java 25.  
- **Cross-Platform Development:** Developers targeting both Windows and Linux environments can maintain consistent Java versions across platforms.  
- **Microservices and Event-Driven Architectures:** Java 25 support enhances the development of event-driven functions triggered by Azure Event Grid, Service Bus, or HTTP requests.

**Important Considerations and Limitations**  
- **Preview Status:** As this is a public preview, some features may not be fully production-ready, and breaking changes or bugs could occur. It is advisable to test thoroughly before production deployment.  
- **Dependency Compatibility:** Some third-party libraries or frameworks may require updates to be fully compatible with Java 25.  
- **Performance Testing:** While Java 25 includes performance improvements, actual function performance should be validated in the target environment.  
- **Runtime Selection:** Existing function apps defaulting to earlier Java versions will not automatically upgrade; explicit configuration changes are required.  
- **Monitoring and Diagnostics:** Ensure that monitoring tools and Application Insights integrations are compatible with Java 25 runtime logs and telemetry.

**Integration with Related Azure Services**  
Azure Functions with Java 25 integrates seamlessly with Azure DevOps pipelines for CI/CD, enabling automated builds and deployments using the updated Java runtime. It supports

---

### 32. Generally Available: Application Gateway for Containers – Slow start

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Application Gateway for Containers – Slow start](https://azure.microsoft.com/updates?id=525893)

**Update ID**: 525893
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Application Gateway for Containers now generally supports the Slow Start load balancing algorithm.

- Key changes or new features  
The Slow Start feature gradually ramps up traffic to newly added backend pods over a configurable time window. This approach helps prevent sudden traffic spikes to new instances during scale-up events, improving overall stability and backend performance.

- Target audience affected  
Developers and IT professionals managing containerized applications behind Azure Application Gateway, especially those using autoscaling or dynamic backend pools.

- Important notes if any  
The slow start duration is configurable, allowing fine-tuning based on application behavior and scale-up patterns. Implementing Slow Start can reduce backend errors and improve user experience during scaling operations. Users should review their load balancing settings to enable and optimize this feature for their container workloads.

Reference: https://azure.microsoft.com/updates?id=525893

**Details**:

The Azure Application Gateway for Containers has reached general availability for the Slow Start load balancing algorithm, a feature designed to enhance backend stability and performance during scale-up events by gradually ramping up traffic to new pods over a configurable time window. This update addresses common challenges in containerized environments where sudden traffic surges to freshly instantiated pods can cause performance degradation or instability.

**Background and Purpose**  
In containerized applications, especially those orchestrated via Kubernetes or Azure Kubernetes Service (AKS), scaling out backend pods is a frequent operation to handle increased load. However, immediately directing full traffic to new pods can overwhelm them before they are fully warmed up, leading to increased latency, errors, or even pod crashes. Traditional load balancers often distribute traffic evenly without regard to pod readiness or warm-up state. The Slow Start feature was introduced to mitigate these issues by gradually increasing traffic, allowing new pods to initialize properly and stabilize.

**Specific Features and Detailed Changes**  
The Slow Start algorithm in Application Gateway for Containers enables a configurable ramp-up period during which traffic to new pods increases linearly from zero to full capacity. This is controlled via a time window setting, allowing operators to tailor the duration based on application characteristics and pod initialization times. The feature is now generally available, meaning it is fully supported for production workloads with SLAs. It integrates seamlessly with the existing Application Gateway for Containers load balancing capabilities, including health probes and session affinity.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Application Gateway monitors pod lifecycle events and health probe responses to detect new backend pods. When a new pod is added, the Slow Start algorithm initiates a timer corresponding to the configured ramp-up duration. During this period, the load balancer incrementally increases the proportion of traffic routed to the new pod, starting from zero. This gradual increase helps the pod to warm up its caches, establish database connections, and complete any initialization logic without being overwhelmed by immediate full traffic load. The implementation leverages Application Gateway’s integration with Kubernetes endpoints, dynamically adjusting traffic distribution based on pod readiness and Slow Start state.

**Use Cases and Application Scenarios**  
This feature is particularly beneficial for microservices architectures and stateless applications deployed on AKS or other Kubernetes platforms where pods frequently scale in and out. Applications with complex initialization routines, such as those requiring heavy caching, JIT compilation, or connection pooling, will see improved stability and reduced error rates during scaling events. It also benefits scenarios with bursty traffic patterns or auto-scaling policies that rapidly add pods, ensuring smoother transitions and better user experience.

**Important Considerations and Limitations**  
While Slow Start improves stability, it introduces a delay before new pods receive full traffic, which may temporarily reduce overall capacity during scale-up. Proper configuration of the ramp-up window is critical; too short may negate benefits, too long may delay full utilization. Monitoring and tuning based on application behavior are recommended. Additionally, Slow Start applies only to new pods detected by Application Gateway and requires accurate health probes to function correctly. It does not replace other scaling best practices like readiness probes or pod lifecycle hooks.

**Integration with Related Azure Services**  
Application Gateway for Containers integrates tightly with AKS, leveraging Kubernetes APIs to track pod states and endpoints. It works alongside Azure Monitor and Azure Log Analytics for telemetry and diagnostics, enabling operators to observe Slow Start behavior and pod performance metrics. When combined with Azure Autoscale and Azure Policy, it supports automated, resilient scaling strategies. This update complements Azure Front Door and Azure Traffic Manager by optimizing backend load distribution at the application gateway layer within containerized environments.

In summary, the general availability of the Slow Start load balancing algorithm in Azure Application Gateway for Containers provides IT professionals with a robust mechanism to enhance backend pod stability and performance during scale-up by incrementally increasing traffic to new pods over a configurable time window, thereby reducing initialization-related errors and improving overall application reliability in containerized deployments.

---

### 33. Public Preview: Application Gateway for Containers Istio Service Mesh integration

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Application Gateway for Containers Istio Service Mesh integration](https://azure.microsoft.com/updates?id=525874)

**Update ID**: 525874
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Compute, Containers, Application Gateway, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Application Gateway for Containers now offers public preview support for integration with the Istio service mesh via an optional service mesh extension.

- Key changes or new features  
This integration enables simplified and secure north-south traffic management between external clients and services running inside the Istio service mesh. The extension facilitates seamless ingress traffic routing, improving security and operational efficiency by leveraging Application Gateway’s advanced Layer 7 capabilities alongside Istio’s service mesh features.

- Target audience affected  
Developers and IT professionals deploying containerized applications with Istio service mesh who require robust, secure ingress solutions for external client communication.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should monitor updates for GA release and review compatibility with existing Istio configurations. Further configuration details and best practices are available in the Azure documentation.

**Details**:

The recent Azure update announces the public preview of Application Gateway for Containers with integration support for the Istio service mesh via an optional service mesh extension. This enhancement is designed to streamline and secure north-south traffic—traffic entering and leaving the cluster—between external clients and microservices managed within an Istio service mesh environment.

**Background and Purpose**  
As containerized applications and microservices architectures grow in complexity, managing secure and efficient ingress traffic becomes critical. Istio, a popular open-source service mesh, provides advanced traffic management, security, and observability within Kubernetes clusters but traditionally requires additional configuration and components to handle ingress traffic securely. Azure’s Application Gateway for Containers aims to simplify this by natively integrating with Istio, providing a unified ingress solution that leverages Application Gateway’s Layer 7 load balancing, Web Application Firewall (WAF), and SSL termination capabilities directly with Istio-managed services.

**Specific Features and Detailed Changes**  
- **Service Mesh Extension:** The update introduces an optional service mesh extension that enables Application Gateway for Containers to interface directly with Istio’s ingress gateway components.  
- **Simplified North-South Traffic Management:** This integration allows Application Gateway to act as a secure ingress point for external traffic, routing requests into the Istio service mesh with minimal manual configuration.  
- **Enhanced Security:** Leveraging Application Gateway’s WAF and SSL offloading capabilities, the solution enhances security for incoming traffic before it reaches the mesh.  
- **Seamless Traffic Routing:** The extension supports routing rules and policies defined in Istio, enabling consistent traffic management and observability across the mesh and ingress boundary.

**Technical Mechanisms and Implementation Methods**  
The integration is achieved by deploying the Application Gateway for Containers with the service mesh extension enabled. This extension configures the Application Gateway to recognize and route traffic to Istio ingress gateways, typically implemented as Kubernetes ingress resources or Gateway API resources within the cluster. The Application Gateway handles TLS termination and WAF inspection at the perimeter, then forwards traffic to the Istio ingress gateway using HTTP/HTTPS protocols. Istio then manages intra-mesh routing, service discovery, and policy enforcement. Configuration synchronization between Application Gateway and Istio is automated via the extension, reducing manual intervention and potential misconfigurations.

**Use Cases and Application Scenarios**  
- **Microservices Exposed to External Clients:** Organizations running microservices on AKS with Istio can use this integration to expose services securely to the internet.  
- **Hybrid Traffic Management:** Enterprises requiring advanced Layer 7 routing with WAF protection at the edge while leveraging Istio’s internal service mesh capabilities benefit from this setup.  
- **Simplified Security Posture:** Teams looking to consolidate ingress security controls and reduce complexity in managing ingress gateways gain operational efficiencies.  
- **Multi-tenant Environments:** The solution supports routing traffic to multiple services or namespaces within the mesh, facilitating multi-tenant Kubernetes clusters.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it may not be fully production-ready and could have limitations or require feedback for improvements.  
- **Compatibility:** This integration currently targets Istio service mesh; compatibility with other service meshes or versions should be verified.  
- **Configuration Complexity:** While simplified, some knowledge of both Application Gateway and Istio configurations remains necessary to optimize routing and security policies.  
- **Resource Overhead:** Running Application Gateway alongside Istio ingress components may introduce additional resource consumption and latency considerations.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** This feature is primarily designed for AKS clusters running Istio, providing a managed environment for containerized workloads.  
- **Azure Monitor and Azure Security Center:** Integration with these services allows enhanced observability and security posture management for ingress traffic and mesh communications.  
- **Azure Active Directory (AAD):** Can be combined for authentication and authorization scenarios at the ingress level.  
- **Azure Firewall and Network Security

---

### 34. Public Preview: Azure DocumentDB high-performance storage 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure DocumentDB high-performance storage ](https://azure.microsoft.com/updates?id=525549)

**Update ID**: 525549
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure DocumentDB (now Azure Cosmos DB) introduces a public preview of high-performance storage capabilities.

- Key changes or new features  
The update enables running larger and faster workloads on fewer physical nodes by enhancing storage performance per shard. Each physical shard now supports up to 64 TiB of storage capacity, 80,000 IOPS, and 1,200 MB/s throughput. This significantly boosts the scalability and efficiency of DocumentDB deployments.

- Target audience affected  
Developers and IT professionals managing Azure DocumentDB/Cosmos DB workloads who require high throughput and large storage capacity for demanding applications.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should monitor performance and compatibility during the preview phase. The update leverages Azure’s underlying storage infrastructure improvements to deliver these enhancements.  

For more details, visit: https://azure.microsoft.com/updates?id=525549

**Details**:

The Azure DocumentDB high-performance storage public preview introduces a significant enhancement in storage capacity and performance per physical shard (node), enabling larger and faster workloads on fewer nodes, thereby optimizing resource utilization and cost efficiency for document database applications.

**Background and Purpose of the Update**  
Azure DocumentDB, now part of Azure Cosmos DB’s multi-model database service, is designed for globally distributed, low-latency, and scalable document database workloads. As customer demands grow for bigger datasets and higher throughput, the existing storage and IOPS limits per node constrained scaling and performance. This update addresses these limitations by increasing the storage capacity and I/O performance per physical shard, allowing customers to consolidate workloads, reduce node count, and achieve better performance without proportional increases in infrastructure.

**Specific Features and Detailed Changes**  
- **Increased Storage Capacity:** The update expands the maximum storage per physical shard to 64 TiB, a substantial increase that supports much larger datasets on a single node.  
- **Enhanced IOPS:** Up to 80,000 IOPS per shard are now supported, enabling faster read/write operations and improved responsiveness for high-throughput applications.  
- **Higher Throughput:** The throughput per shard reaches up to 1,200 MB/s, facilitating rapid data ingestion and query processing.  
These improvements collectively allow for more data and higher transaction volumes to be handled efficiently on fewer physical shards.

**Technical Mechanisms and Implementation Methods**  
The enhancement leverages advancements in Azure’s underlying storage infrastructure, likely utilizing premium SSDs or ultra-durable storage tiers optimized for high IOPS and throughput. The architecture maintains the physical shard abstraction, ensuring backward compatibility with existing DocumentDB APIs and partitioning schemes. Internally, the system optimizes data layout, caching, and I/O scheduling to maximize throughput and minimize latency. The update is available as a public preview, meaning customers can opt-in to test these capabilities while Microsoft gathers feedback and further refines the service.

**Use Cases and Application Scenarios**  
- **Large-scale IoT telemetry ingestion:** Applications ingesting massive streams of JSON documents can benefit from the increased throughput and storage to handle spikes and large datasets.  
- **Real-time analytics:** High IOPS and throughput enable faster querying and aggregation of large document collections for operational analytics.  
- **Gaming and social media platforms:** These workloads often require rapid reads and writes of user-generated content and metadata, which this update supports efficiently.  
- **Enterprise content management:** Organizations managing extensive document repositories can consolidate storage and improve performance with fewer shards.  

**Important Considerations and Limitations**  
- As a public preview, this feature may have limited SLA guarantees and could undergo changes before general availability.  
- Workloads must be designed to leverage the increased shard capacity effectively; partitioning strategies should be reviewed to avoid hot partitions.  
- Cost implications should be analyzed, as higher performance storage tiers may incur increased charges.  
- Compatibility with existing SDKs and APIs remains, but testing is recommended to validate performance gains and stability.  

**Integration with Related Azure Services**  
This update complements Azure Cosmos DB’s multi-model capabilities, allowing seamless integration with other APIs (SQL, MongoDB, Cassandra, Gremlin, Table). It also synergizes with Azure Monitor and Azure Advisor for performance monitoring and optimization. For data ingestion and processing, Azure Event Hubs and Azure Stream Analytics can feed data into DocumentDB shards benefiting from the enhanced storage. Additionally, integration with Azure Functions and Logic Apps enables event-driven workflows that leverage the improved throughput and capacity.

In summary, the Azure DocumentDB high-performance storage public preview significantly boosts storage capacity and I/O performance per shard, empowering IT professionals to run larger, faster document database workloads more efficiently, with practical benefits across diverse high-scale, low-latency application scenarios while maintaining compatibility and integration within the broader Azure ecosystem.

---

### 35. Generally Available: Model Context Protocol (MCP) tool trigger for Azure Functions 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Model Context Protocol (MCP) tool trigger for Azure Functions ](https://azure.microsoft.com/updates?id=525523)

**Update ID**: 525523
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions now generally supports the Model Context Protocol (MCP) tool trigger, enabling seamless integration of AI agents with serverless functions.

- Key changes or new features  
MCP allows applications to expose capabilities and contextual information to large language models (LLMs). With this update, developers can define custom tools that AI agents invoke via Azure Functions, facilitating dynamic task execution. This integration empowers AI-driven workflows to call serverless endpoints as part of their reasoning and action steps, enhancing automation and extensibility.

- Target audience affected  
Developers building AI-powered applications and IT professionals managing AI integrations in Azure environments will benefit from this update. It is particularly relevant for teams leveraging LLMs and Azure Functions to create intelligent, context-aware solutions.

- Important notes if any  
This feature is now generally available, indicating production readiness and full support. Developers should review MCP specifications and Azure Functions triggers documentation to implement and secure these tool integrations effectively. This update enhances the interoperability between AI models and Azure serverless compute, streamlining complex AI workflows.

**Details**:

The recent Azure update announces the general availability of the Model Context Protocol (MCP) tool trigger integration for Azure Functions, enabling developers to extend AI agent capabilities by invoking serverless functions as part of AI workflows.

**Background and Purpose**  
Model Context Protocol (MCP) is designed to standardize how applications expose contextual data and functional tools to large language models (LLMs) and AI agents. MCP facilitates a structured interaction where AI agents can dynamically discover and invoke external tools to perform specific tasks beyond pure language generation, such as querying databases, executing business logic, or integrating with other APIs. The purpose of this update is to enable Azure Functions to act as MCP-compliant tools, allowing AI agents to trigger serverless functions directly within their operational context, thereby bridging AI reasoning with real-world actions in a scalable, event-driven manner.

**Specific Features and Detailed Changes**  
- **MCP Tool Trigger for Azure Functions:** Azure Functions can now be registered as MCP tools, exposing their endpoints and capabilities to AI agents through the MCP framework.  
- **Standardized Invocation:** AI agents using MCP can invoke Azure Functions seamlessly, passing contextual parameters and receiving structured responses.  
- **Enhanced Tooling Support:** Developers can define metadata and interface contracts for Azure Functions to describe their capabilities clearly to MCP clients.  
- **Security and Authentication:** Integration supports secure authentication mechanisms to ensure that only authorized AI agents can trigger Azure Functions.  
- **Monitoring and Logging:** Invocation of Azure Functions via MCP is integrated with Azure Monitor and Application Insights for observability.

**Technical Mechanisms and Implementation Methods**  
The integration leverages the MCP specification, which defines a protocol for AI models to query and invoke external tools. Azure Functions are configured with MCP metadata, including function signatures, input/output schemas, and authentication details. When an AI agent operating under MCP needs to perform a task, it queries the MCP server for available tools, discovers the Azure Function endpoint, and sends a structured request. The Azure Function executes the logic and returns a response in the expected format. This interaction is typically RESTful, secured via OAuth or managed identities, and supports asynchronous execution patterns. Developers can use Azure Functions bindings and triggers to customize the function behavior in response to MCP calls.

**Use Cases and Application Scenarios**  
- **Automated IT Operations:** AI agents can trigger Azure Functions to automate routine maintenance tasks, such as restarting services or scaling resources.  
- **Business Process Automation:** AI-driven workflows can invoke Azure Functions to process transactions, update CRM systems, or generate reports dynamically.  
- **Data Enrichment and Querying:** AI agents can call Azure Functions to fetch or transform data from enterprise systems, enabling contextual responses.  
- **Custom AI Tooling:** Organizations can expose proprietary logic or APIs as MCP tools via Azure Functions, extending AI capabilities with domain-specific functions.

**Important Considerations and Limitations**  
- **Latency:** Invoking Azure Functions introduces network and execution latency; design workflows accordingly to handle asynchronous or delayed responses.  
- **Security:** Proper authentication and authorization must be enforced to prevent unauthorized access or abuse of function endpoints.  
- **Function Complexity:** Azure Functions should be designed to handle idempotent, stateless operations to align with serverless best practices.  
- **MCP Compliance:** Functions must adhere strictly to MCP metadata and protocol requirements for seamless integration.  
- **Scaling:** Consider function scaling limits and concurrency to avoid throttling during high-volume AI agent interactions.

**Integration with Related Azure Services**  
- **Azure Functions:** Core serverless compute platform hosting MCP tools.  
- **Azure API Management:** Can be used to expose and secure Azure Functions as APIs for MCP consumption.  
- **Azure Active Directory (AAD):** Provides authentication and authorization for secure MCP tool invocation.  
- **Azure Monitor and Application Insights:** Enable monitoring, logging, and diagnostics of MCP-triggered function executions.  
- **Azure OpenAI Service:** AI agents powered by Azure OpenAI can leverage

---

### 36. Generally Available: Azure Functions durable task scheduler Dedicated SKU (GA) & Consumption SKU (Public Preview)

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Functions durable task scheduler Dedicated SKU (GA) & Consumption SKU (Public Preview)](https://azure.microsoft.com/updates?id=525518)

**Update ID**: 525518
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions Durable Task Scheduler is now Generally Available (GA) for the Dedicated SKU and available in Public Preview for the Consumption SKU.

- Key changes or new features  
The Durable Task Scheduler provides an orchestration engine tailored for complex workflows and intelligent agents. It automatically checkpoints progress and manages orchestration state to ensure resilience and reliability. The GA release for the Dedicated SKU offers production-ready stability and performance, while the Consumption SKU preview allows developers to experiment with serverless, consumption-based billing models for durable orchestrations.

- Target audience affected  
Developers building stateful, long-running serverless workflows and IT professionals managing Azure Functions infrastructure will benefit from improved orchestration capabilities and flexible deployment options.

- Important notes if any  
The Dedicated SKU is now production-ready with SLA-backed support, suitable for mission-critical workloads. The Consumption SKU remains in Public Preview, so users should evaluate it accordingly before production use. This update enhances the ability to build scalable, fault-tolerant applications using Azure Functions durable orchestrations.  

For more details, visit: https://azure.microsoft.com/updates?id=525518

**Details**:

The Azure Functions Durable Task Scheduler update marks the General Availability (GA) release of the Dedicated SKU and the Public Preview of the Consumption SKU, enhancing the orchestration capabilities for complex, stateful workflows within Azure Functions. This update builds upon the durable task scheduler introduced earlier, which serves as an orchestration engine designed to manage long-running, stateful, and fault-tolerant workflows by automatically checkpointing progress and safeguarding orchestration state.

**Background and Purpose:**  
Azure Functions Durable Task Scheduler addresses the need for reliable orchestration of complex workflows and intelligent agents that require state persistence, retries, and coordination across distributed components. Prior to this update, durable functions were primarily available in consumption plans with some limitations on scale and control. The introduction of a Dedicated SKU in GA and Consumption SKU in Public Preview provides customers with flexible deployment options tailored to their performance, scalability, and cost requirements.

**Specific Features and Changes:**  
- **Dedicated SKU (GA):** Offers enhanced performance and predictable scaling by running on dedicated infrastructure. This SKU is suitable for enterprise workloads requiring high throughput and low latency orchestration.  
- **Consumption SKU (Public Preview):** Enables serverless, pay-per-execution orchestration with automatic scaling, ideal for variable workloads and cost-sensitive scenarios.  
- **Automatic Checkpointing:** The scheduler persistently saves orchestration state after each significant step, ensuring resiliency against failures and enabling reliable restarts.  
- **State Management:** Durable Task Scheduler manages orchestration state transparently, abstracting complexities from developers and reducing the need for manual state handling.  
- **Improved Orchestration Engine:** Supports complex control flow patterns such as fan-out/fan-in, chaining, and human interaction workflows with enhanced reliability.

**Technical Mechanisms and Implementation:**  
The Durable Task Scheduler leverages Azure Storage or Cosmos DB for durable state persistence, checkpointing orchestration progress after each activity execution. It uses event sourcing and reliable messaging patterns to coordinate tasks and maintain consistency. The Dedicated SKU runs on isolated compute resources, providing predictable performance, while the Consumption SKU uses dynamic scaling based on event triggers. The orchestration logic is implemented as stateful functions that communicate via durable entities and orchestrator functions, enabling complex workflow definitions in code.

**Use Cases and Application Scenarios:**  
- **Complex Workflow Automation:** Automating multi-step business processes that require state persistence and error handling, such as order processing or approval workflows.  
- **Intelligent Agents:** Managing long-running AI/ML workflows that need checkpointing and recovery, such as data pipeline orchestration.  
- **Human-in-the-Loop Processes:** Orchestrating workflows that require human intervention and asynchronous waiting periods.  
- **Event-Driven Microservices Coordination:** Coordinating distributed microservices with reliable state management and retry policies.

**Important Considerations and Limitations:**  
- The Consumption SKU is currently in Public Preview and may have feature or SLA limitations compared to the GA Dedicated SKU.  
- State storage costs and latency depend on the underlying storage choice (Azure Storage vs Cosmos DB).  
- Developers must design orchestrations mindful of execution time limits and potential cold starts in the Consumption SKU.  
- Monitoring and diagnostics should be configured to track orchestration health and performance.  
- Integration with existing durable functions codebases may require adjustments to leverage the new SKU options.

**Integration with Related Azure Services:**  
- **Azure Storage and Cosmos DB:** Used for state persistence and checkpointing.  
- **Azure Monitor and Application Insights:** For telemetry, logging, and diagnostics of orchestrations.  
- **Azure Event Grid and Service Bus:** Can be integrated as triggers or communication channels within orchestrations.  
- **Azure Logic Apps:** Durable Task Scheduler can complement Logic Apps by handling complex custom workflows requiring code-based orchestration.  
- **Azure Functions Premium Plan:** The Dedicated SKU aligns with Premium Plan capabilities, enabling VNET integration and enhanced security.

In summary, the GA release of the Azure Functions Durable Task Scheduler Dedicated SKU alongside the

---

### 37. Public Preview: Self-hosted remote MCP servers on Azure Functions 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Self-hosted remote MCP servers on Azure Functions ](https://azure.microsoft.com/updates?id=525505)

**Update ID**: 525505
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure now supports hosting self-hosted remote Model Context Protocol (MCP) servers built with MCP SDKs on Azure Functions, currently in public preview.

- Key changes or new features  
This update enables developers to deploy MCP servers as serverless functions, leveraging Azure Functions’ platform benefits such as built-in server authentication, automatic scaling, and simplified management. This reduces infrastructure overhead and enhances security and scalability for MCP server deployments.

- Target audience affected  
Developers building applications that use the Model Context Protocol and IT professionals managing MCP server infrastructure will benefit from this update. It is particularly relevant for teams looking to integrate MCP servers into cloud-native, serverless architectures.

- Important notes if any  
As this feature is in public preview, it may have limited SLA and could undergo changes before general availability. Users should evaluate it in non-production environments first. Refer to the official Azure documentation and MCP SDK guidance for implementation details and best practices.

For more information, visit: https://azure.microsoft.com/updates?id=525505

**Details**:

The recent Azure update announces the public preview of self-hosted remote Model Context Protocol (MCP) servers on Azure Functions, enabling developers to deploy MCP servers built with MCP SDKs directly on the serverless Functions platform. This advancement aims to simplify and enhance the hosting and management of MCP servers by leveraging Azure Functions' scalable and secure environment.

**Background and Purpose**  
Model Context Protocol (MCP) is a communication protocol used primarily in AI and machine learning workflows to facilitate interactions between clients and model-serving backends. Traditionally, hosting MCP servers required dedicated infrastructure or containerized environments, which introduced operational overhead and complexity in scaling, authentication, and maintenance. The update’s purpose is to streamline MCP server deployment by integrating it with Azure Functions, a serverless compute service that automatically manages infrastructure, scaling, and security, thereby reducing operational burden and accelerating development cycles.

**Specific Features and Detailed Changes**  
- **Self-hosting MCP servers on Azure Functions:** Developers can now deploy MCP servers as Azure Functions, eliminating the need for separate VM or container orchestration.  
- **Built-in server authentication:** Azure Functions’ native authentication mechanisms can be leveraged to secure MCP server endpoints without additional custom code.  
- **Automatic scaling:** Functions’ dynamic scaling ensures MCP servers can handle variable workloads efficiently, scaling out during high demand and scaling in when idle.  
- **Simplified deployment and management:** MCP servers benefit from Azure Functions’ deployment pipelines, monitoring, and diagnostics tools, improving operational visibility and control.

**Technical Mechanisms and Implementation Methods**  
To implement this, developers use the MCP SDKs to build MCP server logic encapsulated within Azure Functions triggers (typically HTTP triggers). The MCP server’s request/response handling is mapped to function invocations, allowing seamless protocol communication. Authentication can be integrated using Azure Functions’ built-in authentication providers (e.g., Azure AD, social logins). The serverless nature abstracts away infrastructure management, while Azure Functions’ runtime handles execution, scaling, and lifecycle management. Developers deploy the function app via Azure CLI, ARM templates, or CI/CD pipelines, enabling rapid iteration and updates.

**Use Cases and Application Scenarios**  
- **AI/ML model serving:** Hosting MCP servers that serve model inference requests in real-time, benefiting from automatic scaling during peak usage.  
- **Edge and IoT scenarios:** Lightweight MCP servers deployed as Functions can serve remote devices with minimal management overhead.  
- **Multi-tenant environments:** Functions’ isolated execution and authentication features support secure multi-tenant MCP server deployments.  
- **Rapid prototyping and development:** Developers can quickly spin up MCP servers without provisioning infrastructure, accelerating experimentation and testing.

**Important Considerations and Limitations**  
- **Preview status:** As a public preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- **Cold start latency:** Azure Functions may introduce cold start delays, which could impact latency-sensitive MCP interactions.  
- **Resource constraints:** Function apps have execution time and memory limits that may restrict complex or long-running MCP server operations.  
- **Authentication scope:** While built-in authentication simplifies security, custom or advanced authorization scenarios may require additional implementation.  
- **Protocol compatibility:** Ensure the MCP SDK version used is compatible with the Functions runtime environment and triggers.

**Integration with Related Azure Services**  
- **Azure Active Directory (AAD):** For secure authentication and authorization of MCP server endpoints.  
- **Azure Monitor and Application Insights:** To track function execution metrics, logs, and diagnose MCP server behavior.  
- **Azure DevOps/GitHub Actions:** For CI/CD pipelines automating MCP server deployment and updates.  
- **Azure API Management:** Can be layered in front of MCP servers for additional security, throttling, and analytics.  
- **Azure Storage or Cosmos DB:** For persisting MCP server state or logs if needed.

In summary, this update enables IT professionals and developers to deploy MCP servers on a scalable, secure, and

---

### 38. Announcing: Resources for migrating to Azure Functions Flex Consumption 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Announcing: Resources for migrating to Azure Functions Flex Consumption ](https://azure.microsoft.com/updates?id=525500)

**Update ID**: 525500
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure announced new resources to support migration to Azure Functions Flex Consumption, now the recommended hosting plan for serverless workloads needing advanced scaling, networking, and cost optimization.

- Key changes or new features  
The update provides guidance and tools to help developers and IT professionals migrate from the Azure Functions Consumption plan or AWS Lambda to the Flex Consumption plan. This plan offers enhanced scaling capabilities, improved networking options (such as VNET integration), and better cost management for serverless applications.

- Target audience affected  
Developers and IT professionals managing serverless applications on Azure Functions Consumption plan or AWS Lambda who require more advanced hosting features and want to optimize performance and costs.

- Important notes if any  
Migrating to Flex Consumption can enable more complex serverless scenarios but may involve changes in deployment and configuration. Users should review the provided migration resources carefully to ensure a smooth transition. This update reflects Azure’s commitment to improving serverless hosting flexibility and cost efficiency.

Link for details: https://azure.microsoft.com/updates?id=525500

**Details**:

The recent Azure update announces the availability of comprehensive resources to facilitate migration to the Azure Functions Flex Consumption hosting plan, which is now the recommended environment for serverless workloads that demand advanced scaling capabilities, enhanced networking options, and improved cost optimization compared to the traditional Consumption plan.

**Background and Purpose:**  
Azure Functions has long offered the Consumption plan as a serverless hosting option that automatically scales based on demand, charging only for actual execution time. However, as serverless applications grow in complexity and scale, customers require more granular control over scaling behavior, networking configurations (such as VNET integration), and cost management. The Flex Consumption plan addresses these needs by providing a more flexible and powerful hosting model. This update aims to assist customers currently using the Azure Functions Consumption plan or migrating workloads from AWS Lambda by providing targeted migration resources, best practices, and tooling to ease the transition.

**Specific Features and Detailed Changes:**  
- **Advanced Scaling:** Flex Consumption supports more sophisticated scaling scenarios, including longer maximum execution durations and the ability to scale to a higher number of concurrent instances. This is critical for workloads with bursty or unpredictable traffic patterns.  
- **Enhanced Networking:** Unlike the Consumption plan, Flex Consumption allows seamless integration with Azure Virtual Networks (VNETs), enabling secure, private connectivity to backend services, databases, and on-premises resources.  
- **Cost Optimization:** The plan introduces improved cost controls by enabling more predictable billing models and options to optimize resource consumption, such as pre-warmed instances or scaling limits.  
- **Migration Resources:** Microsoft provides detailed documentation, migration guides, and tooling to analyze existing Consumption plan functions or AWS Lambda workloads, identify compatibility considerations, and automate parts of the migration process.

**Technical Mechanisms and Implementation Methods:**  
The Flex Consumption plan is built on Azure Kubernetes Service (AKS) and leverages Kubernetes-based scaling and orchestration under the hood, allowing for more customizable scaling policies and network configurations. Functions run inside containers orchestrated by Kubernetes, enabling longer execution times and more control over runtime environments. Migration involves assessing function triggers, bindings, and runtime dependencies, then redeploying functions to the Flex Consumption environment with updated configuration files that specify the new hosting plan and networking settings. Integration with Azure DevOps or GitHub Actions can automate deployment pipelines for the migrated functions.

**Use Cases and Application Scenarios:**  
- Serverless APIs requiring VNET integration to securely access databases or other protected resources.  
- Event-driven applications with unpredictable or high-volume workloads needing rapid and granular scaling beyond Consumption plan limits.  
- Applications migrating from AWS Lambda seeking feature parity or enhanced Azure-native capabilities.  
- Long-running background jobs or workflows that exceed the maximum execution duration of the Consumption plan.  
- Enterprises optimizing serverless costs through more predictable scaling and resource management.

**Important Considerations and Limitations:**  
- While Flex Consumption offers greater flexibility, it may introduce slightly higher baseline costs due to pre-warmed instances or reserved capacity.  
- Migration requires careful validation of function triggers and bindings, as some bindings may have different behaviors or support levels in Flex Consumption.  
- Network configuration changes, such as VNET integration, may require additional setup and permissions.  
- Some legacy Consumption plan features or third-party extensions might not yet be fully supported.  
- Monitoring and debugging tools may differ slightly due to the underlying Kubernetes infrastructure.

**Integration with Related Azure Services:**  
Flex Consumption functions can seamlessly integrate with Azure Monitor for advanced telemetry, Azure Application Insights for distributed tracing, and Azure API Management for secure API exposure. They can also connect to Azure Event Grid, Service Bus, and Storage services within secured VNET environments. Integration with Azure DevOps and GitHub Actions facilitates CI/CD pipelines tailored for the Flex Consumption hosting model. Additionally, Flex Consumption supports Azure Private Link and Azure Firewall for enhanced security postures.

In summary, this update equips IT professionals with the necessary resources and guidance to migrate serverless workloads to Azure Functions Flex Consumption, enabling advanced scaling, secure networking, and

---

### 39. Generally Available: Azure Functions enables OpenTelemetry support 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Functions enables OpenTelemetry support ](https://azure.microsoft.com/updates?id=525479)

**Update ID**: 525479
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions

**Summary**:

- What was updated  
Azure Functions has reached general availability (GA) for OpenTelemetry support.

- Key changes or new features  
Developers can now natively export logs, traces, and metrics from Azure Functions using OpenTelemetry, an open standard for observability data. This update transitions from public preview to a production-ready experience, improving integration with monitoring and tracing tools. It enables consistent telemetry collection across distributed applications, facilitating enhanced diagnostics and performance monitoring.

- Target audience affected  
Developers building serverless applications with Azure Functions and IT professionals responsible for application monitoring and diagnostics will benefit from this update.

- Important notes if any  
This GA release ensures stable and supported OpenTelemetry integration, encouraging adoption of open standards for observability in serverless environments. Users should review their telemetry pipelines to leverage this native support and improve their monitoring strategies. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The Azure Functions update announcing general availability (GA) of OpenTelemetry support marks a significant enhancement in the observability capabilities for serverless applications, enabling developers to collect and export telemetry data—logs, traces, and metrics—using open standards for improved monitoring and diagnostics.

**Background and Purpose:**  
Prior to this update, Azure Functions users relied on platform-specific monitoring tools such as Application Insights for telemetry, which, while powerful, limited interoperability and vendor flexibility. OpenTelemetry is an open-source, vendor-neutral standard for telemetry data collection, designed to unify and simplify observability across diverse environments. By integrating OpenTelemetry support natively, Azure Functions aims to provide developers with a standardized, extensible, and production-grade observability framework that aligns with modern cloud-native practices and multi-cloud strategies.

**Specific Features and Detailed Changes:**  
- **GA Support for OpenTelemetry SDKs:** Azure Functions now fully supports OpenTelemetry SDKs for automatic and manual instrumentation of functions code.  
- **Exporters Integration:** Developers can configure exporters to send telemetry data to various backends, including Azure Monitor, Application Insights, or third-party observability platforms that support OpenTelemetry protocols.  
- **Automatic Context Propagation:** The update ensures seamless context propagation across distributed function invocations, enabling end-to-end tracing in complex serverless workflows.  
- **Metrics and Logs Collection:** Beyond traces, the GA release supports exporting metrics and logs, providing a comprehensive observability dataset.  
- **Configuration via Azure Functions Host and Environment Variables:** Users can configure OpenTelemetry settings declaratively through host.json or environment variables, facilitating easy integration into CI/CD pipelines.

**Technical Mechanisms and Implementation Methods:**  
Under the hood, Azure Functions integrates OpenTelemetry SDKs into the runtime environment, enabling automatic instrumentation of triggers, bindings, and HTTP requests. The runtime captures telemetry data and enriches it with contextual metadata such as invocation IDs, function names, and execution durations. Exporters use OpenTelemetry Protocol (OTLP) or other supported protocols to transmit data securely to configured backends. The system supports both automatic instrumentation (out-of-the-box telemetry capture) and manual instrumentation via OpenTelemetry APIs for custom telemetry needs.

**Use Cases and Application Scenarios:**  
- **Distributed Tracing in Microservices Architectures:** Developers can trace requests flowing through multiple Azure Functions and other services, identifying latency bottlenecks and failure points.  
- **Multi-Cloud and Hybrid Monitoring:** Organizations using diverse observability tools can standardize telemetry collection with OpenTelemetry, facilitating unified dashboards and alerts.  
- **Performance Optimization:** Detailed metrics enable performance tuning of serverless functions under varying loads.  
- **Compliance and Auditing:** Logs and traces collected via OpenTelemetry can support audit trails and compliance reporting.  
- **Custom Instrumentation:** Developers building complex workflows can add custom spans and metrics to capture domain-specific telemetry.

**Important Considerations and Limitations:**  
- **Version Compatibility:** Ensure that the OpenTelemetry SDK versions used are compatible with the Azure Functions runtime version to avoid instrumentation conflicts.  
- **Sampling Configuration:** Proper configuration of sampling rates is critical to balance telemetry granularity and cost.  
- **Latency Overhead:** While optimized, telemetry collection introduces some overhead; performance testing is recommended.  
- **Security:** Exported telemetry data should be secured in transit and at rest, especially when integrating with third-party systems.  
- **Feature Parity:** Some advanced Application Insights features may not yet be fully supported via OpenTelemetry exporters.

**Integration with Related Azure Services:**  
- **Azure Monitor and Application Insights:** Native exporters allow seamless ingestion of OpenTelemetry data into Azure Monitor and Application Insights, enabling rich analytics, alerting, and visualization.  
- **Azure Event Hubs and Log Analytics:** Telemetry can be routed to Event Hubs or Log Analytics workspaces for custom processing and long-term storage.  
- **Azure DevOps and CI/CD Pipelines:** Configuration via environment variables and host.json supports automated deployment and observability configuration as

---

### 40. Public Preview: Azure Container Apps adds support for agentic Docker Compose 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Container Apps adds support for agentic Docker Compose ](https://azure.microsoft.com/updates?id=525470)

**Update ID**: 525470
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps

**Summary**:

- What was updated  
Azure Container Apps now supports agentic Docker Compose in public preview, enabling developers to deploy multi-container applications using Docker Compose files directly within the Azure Container Apps environment.

- Key changes or new features  
This update integrates the widely adopted Docker Compose workflow into Azure Container Apps, allowing developers to define, configure, and run multi-container applications with familiar Compose syntax. It simplifies the transition from local development to cloud deployment by supporting Compose files natively, reducing the need for complex YAML configurations or manual container orchestration setup.

- Target audience affected  
Developers building multi-container applications and IT professionals managing containerized workloads on Azure will benefit from streamlined deployment and management. This is particularly useful for teams leveraging Docker Compose locally and seeking a seamless path to Azure Container Apps without re-architecting their applications.

- Important notes if any  
As this feature is in public preview, users should expect potential changes and are advised to test workloads thoroughly before production use. Monitoring Azure updates for GA announcements and best practices is recommended. For more details and getting started guidance, refer to the official Azure update link.

**Details**:

The recent Azure update announces the public preview of agentic Docker Compose support within Azure Container Apps, enabling developers to leverage the familiar Docker Compose workflow natively in Azure’s serverless container environment. This enhancement aims to streamline the deployment and management of multi-container applications by bridging local development practices with cloud-native operations.

**Background and Purpose**  
Docker Compose is a widely adopted tool that allows developers to define and orchestrate multi-container applications using a simple YAML file. Traditionally, deploying Docker Compose applications to cloud platforms required manual translation or reconfiguration into platform-specific formats such as Kubernetes manifests or Azure Resource Manager templates. Azure Container Apps, designed as a fully managed serverless container service, previously required users to define applications and services through Azure CLI commands or ARM templates. This update addresses the gap by enabling direct use of Docker Compose files, thus reducing friction and accelerating cloud adoption for containerized workloads.

**Specific Features and Detailed Changes**  
- **Native Docker Compose Support:** Users can now deploy multi-container applications defined in standard `docker-compose.yml` files directly to Azure Container Apps without converting to Kubernetes or other orchestrators.  
- **Agentic Mode:** The term “agentic” implies that Azure Container Apps acts as an intelligent agent interpreting Docker Compose configurations, managing the underlying infrastructure and scaling automatically.  
- **Simplified Deployment Workflow:** Developers can use familiar Docker Compose commands or Azure CLI extensions to deploy and manage containerized applications, preserving environment variables, service dependencies, volumes, and networking configurations as defined in Compose files.  
- **Preview Availability:** The feature is currently in public preview, allowing early adopters to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Container Apps translates Docker Compose service definitions into the platform’s internal configuration model. This involves:  
- Parsing the Compose YAML to extract service definitions, environment variables, ports, and volume mounts.  
- Mapping Compose services to Azure Container Apps instances, configuring ingress and egress rules accordingly.  
- Utilizing Azure Container Apps’ built-in Dapr integration for service-to-service communication and observability.  
- Leveraging the platform’s autoscaling capabilities based on HTTP traffic, CPU, or custom metrics, applied per service as defined.  
- Managing persistent storage through Azure Files or other supported volume providers, aligned with Compose volume definitions.

**Use Cases and Application Scenarios**  
- **Microservices Development:** Developers building microservices locally with Docker Compose can seamlessly deploy to Azure Container Apps without rewriting manifests.  
- **Dev/Test Environments:** Rapidly spin up multi-container test environments in the cloud that mirror local setups.  
- **Hybrid Workflows:** Teams can maintain a single Compose file for both local development and cloud deployment, improving consistency and reducing errors.  
- **Event-Driven Architectures:** Combine containerized services with Azure Event Grid or Azure Functions, orchestrated via Compose, for reactive applications.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview, some features may be incomplete or subject to change; production workloads should be carefully evaluated.  
- **Compose Version Support:** The preview may support a subset of Docker Compose features; complex Compose files with advanced networking or volume drivers might require adjustments.  
- **Resource Constraints:** Azure Container Apps imposes limits on CPU, memory, and storage per container instance; Compose files exceeding these may need modification.  
- **Security and Compliance:** Users must ensure that container images and configurations comply with organizational security policies, as the platform manages underlying infrastructure abstractly.  
- **Integration with Azure Networking:** While basic Compose networking is supported, advanced network topologies or custom virtual networks may require additional configuration.

**Integration with Related Azure Services**  
- **Azure CLI and Azure Portal:** Enhanced tooling support for deploying Compose files directly via CLI commands and portal interfaces.  
- **Azure Container Registry (ACR):** Seamless integration for pulling container images referenced in Compose files.  
- **Azure Monitor and

---

### 41. Public Preview: Azure Container Apps introduces flexible workload profile 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Container Apps introduces flexible workload profile ](https://azure.microsoft.com/updates?id=525465)

**Update ID**: 525465
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps

**Summary**:

- What was updated  
Azure Container Apps now offers a new Flexible Workload Profile, currently in public preview.

- Key changes or new features  
The Flexible Workload Profile combines the simplicity and cost-effectiveness of the consumption-based serverless model with enhanced performance and control features typically found in dedicated workload profiles. This allows developers and IT professionals to run containerized applications with a pay-per-use pricing model while gaining more predictable resource allocation and improved workload management capabilities.

- Target audience affected  
Developers building containerized applications and IT professionals managing Azure Container Apps workloads who require a balance between serverless ease-of-use and dedicated resource control.

- Important notes if any  
This feature is in public preview, so it should be used with caution in production environments. Users can expect easier scaling and cost optimization without sacrificing performance, making it suitable for a broader range of containerized workloads. Further updates and GA announcements will follow as the feature matures.  

For more details, visit: https://azure.microsoft.com/updates?id=525465

**Details**:

The Azure Container Apps flexible workload profile, now in public preview, introduces a hybrid deployment model that combines the simplicity and cost-efficiency of the serverless consumption plan with enhanced performance and control features typically found in dedicated workload profiles. This update addresses the need for more adaptable scaling and resource allocation options within Azure Container Apps, enabling IT professionals to optimize containerized application workloads with greater precision and cost-effectiveness.

**Background and Purpose**  
Azure Container Apps traditionally offers two workload profiles: the consumption-based serverless model, which automatically scales to zero and charges based on actual usage, and the dedicated profile, which provides fixed compute resources for predictable performance but at a higher baseline cost. The flexible workload profile emerges to bridge these models by delivering a pay-per-use serverless experience while allowing users to specify minimum and maximum resource boundaries, thus improving workload predictability and control without sacrificing the elasticity of serverless.

**Specific Features and Detailed Changes**  
- **Configurable Resource Boundaries:** Users can define minimum and maximum CPU and memory allocations, ensuring baseline performance while still benefiting from automatic scaling.  
- **Improved Scaling Behavior:** Unlike the pure consumption model that scales down to zero, flexible profiles maintain a minimum number of active instances, reducing cold start latency for critical workloads.  
- **Cost Efficiency:** By blending serverless billing with resource guarantees, this profile helps balance cost and performance, particularly for workloads with variable but sustained demand.  
- **Simplified Management:** The flexible profile retains the Azure Container Apps’ ease of deployment and management, using the same CLI, ARM templates, and Azure Portal experience.

**Technical Mechanisms and Implementation Methods**  
The flexible workload profile leverages Kubernetes-based autoscaling mechanisms under the hood, enhanced with custom controllers that respect the defined resource boundaries. It integrates with KEDA (Kubernetes Event-driven Autoscaling) to dynamically adjust instance counts based on real-time metrics such as CPU, memory, or custom triggers, while ensuring the minimum instance count is maintained. This approach allows workloads to avoid cold starts and maintain responsiveness during fluctuating traffic patterns. The profile is configured via the Azure CLI or ARM templates by specifying the `workloadProfile` property and setting resource limits and minimum replicas.

**Use Cases and Application Scenarios**  
- **Latency-Sensitive Applications:** Services requiring low startup latency, such as APIs or real-time event processing, benefit from the minimum instance guarantee.  
- **Variable Traffic Workloads:** Applications with unpredictable but sustained traffic, like e-commerce platforms or SaaS applications, can optimize costs while ensuring performance.  
- **Batch Processing with Bursty Demand:** Workloads that experience spikes but require baseline throughput can leverage flexible scaling to handle bursts efficiently.  
- **Development and Testing Environments:** Teams can simulate production-like performance without committing to fully dedicated resources.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it may have limited SLA guarantees and could undergo changes before general availability.  
- **Resource Constraints:** Minimum and maximum resource boundaries must be carefully planned to avoid over-provisioning or throttling.  
- **Scaling Granularity:** While flexible, scaling is still subject to Kubernetes and KEDA limitations, including scaling cooldown periods and metric collection intervals.  
- **Compatibility:** Some advanced features available in dedicated profiles might not be fully supported in the flexible profile during preview.

**Integration with Related Azure Services**  
The flexible workload profile seamlessly integrates with Azure Monitor for telemetry and alerting, Azure Application Insights for performance diagnostics, and Azure DevOps or GitHub Actions for CI/CD pipelines. It supports integration with Azure Virtual Network for secure connectivity and Azure Key Vault for secrets management. Additionally, it works in conjunction with Azure API Management to expose containerized APIs with enhanced security and throttling policies.

In summary, the Azure Container Apps flexible workload profile offers IT professionals a versatile deployment option that balances serverless cost efficiency with enhanced performance control, making it suitable for a wide range of containerized applications requiring dynamic scaling with

---

### 42. Generally Available: Azure Container Apps serverless GPUs in additional regions 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Container Apps serverless GPUs in additional regions ](https://azure.microsoft.com/updates?id=525460)

**Update ID**: 525460
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps

**Summary**:

- What was updated  
Azure Container Apps serverless GPU capabilities have reached general availability (GA) in additional Azure regions.

- Key changes or new features  
The expansion enables developers to deploy GPU-accelerated workloads such as AI inference, machine learning model training, and other compute-intensive tasks within Azure Container Apps without managing infrastructure. This serverless GPU offering simplifies scaling and reduces operational overhead by providing on-demand GPU resources in a fully managed environment.

- Target audience affected  
Developers building AI/ML applications, data scientists requiring GPU compute, and IT professionals managing containerized workloads who want to leverage GPU acceleration in a serverless container platform.

- Important notes if any  
The availability in more regions improves latency and compliance options for global applications. Users should verify region support for serverless GPUs when planning deployments. This update enhances Azure’s container ecosystem by combining serverless ease with GPU power, optimizing cost and performance for GPU workloads.  

For detailed region availability and getting started guidance, refer to the official Azure update link.

**Details**:

The recent Azure update announces the general availability of serverless GPU support for Azure Container Apps across additional Azure regions, addressing the increasing demand for GPU-accelerated containerized workloads. This expansion allows developers and IT professionals to leverage GPU resources in a serverless container environment, facilitating scalable and cost-effective execution of AI inference, machine learning model training, and other GPU-intensive applications without managing underlying infrastructure.

**Background and Purpose:**  
Azure Container Apps is a fully managed serverless container service designed to simplify the deployment and scaling of microservices and containerized applications. Traditionally, GPU workloads required provisioning and managing specialized VM instances or Kubernetes clusters with GPU nodes, which adds operational complexity and cost overhead. The introduction of serverless GPU capabilities in Azure Container Apps aims to abstract infrastructure management while providing on-demand GPU acceleration, enabling developers to focus on application logic rather than resource orchestration. Expanding this capability to additional regions enhances global availability and reduces latency for distributed teams and applications.

**Specific Features and Detailed Changes:**  
- **Serverless GPU Support:** Users can now specify GPU resources (e.g., NVIDIA GPUs) in their container app configurations, enabling GPU acceleration without managing VM scale sets or Kubernetes nodes.  
- **Regional Expansion:** The feature is no longer limited to initial preview regions but is generally available in multiple new Azure regions, improving geographic coverage and compliance options.  
- **Seamless Scaling:** GPU-enabled container apps benefit from Azure Container Apps’ native scaling capabilities, including scale-to-zero and scale-out based on HTTP traffic, events, or custom metrics, optimizing cost-efficiency.  
- **Integration with Dapr and KEDA:** These frameworks continue to support GPU workloads, enabling event-driven architectures and microservice communication patterns with GPU acceleration.

**Technical Mechanisms and Implementation Methods:**  
Under the hood, Azure Container Apps leverages Azure Kubernetes Service (AKS) with virtual nodes and GPU-enabled node pools abstracted away from the user. When a container app requests GPU resources, the platform schedules the container on GPU-capable nodes managed by Azure, automatically provisioning and deprovisioning resources as needed. The serverless model means users are billed based on actual resource consumption rather than pre-allocated capacity. Container images must include GPU-compatible drivers and frameworks (e.g., CUDA, cuDNN) to utilize the hardware acceleration effectively.

**Use Cases and Application Scenarios:**  
- **AI Inference:** Deploying real-time machine learning models for image recognition, natural language processing, or recommendation engines that require GPU acceleration for low-latency responses.  
- **Model Training:** Running distributed or single-node training jobs for deep learning models within containerized environments without managing GPU clusters.  
- **Video Processing and Rendering:** Accelerating workloads such as transcoding, video analytics, or 3D rendering in a scalable, event-driven manner.  
- **Scientific Computing:** Performing simulations or data analysis tasks that benefit from parallel GPU computation in a serverless container context.

**Important Considerations and Limitations:**  
- **Container Image Requirements:** Containers must include appropriate GPU drivers and libraries; base images should be compatible with NVIDIA GPU architectures supported by Azure.  
- **Resource Quotas and Limits:** GPU resources are subject to regional availability and subscription quotas; users should verify limits and request quota increases if necessary.  
- **Cold Start Latency:** While serverless scaling optimizes cost, initial cold starts for GPU-enabled containers may introduce latency, which should be accounted for in latency-sensitive applications.  
- **Compatibility:** Not all Azure Container Apps features may be fully supported with GPU workloads; users should consult documentation for any feature-specific constraints.

**Integration with Related Azure Services:**  
- **Azure Machine Learning:** GPU-enabled container apps can be integrated with Azure ML pipelines for flexible deployment of training and inference workloads.  
- **Azure Event Grid and KEDA:** Enable event-driven scaling of GPU workloads based on custom triggers and metrics.  
- **Azure Monitor and Log Analytics:** Provide observability into GPU utilization

---

### 43. Public Preview: Confidential computing in Azure Container Apps

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Confidential computing in Azure Container Apps](https://azure.microsoft.com/updates?id=525455)

**Update ID**: 525455
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps

**Summary**:

- What was updated  
Azure Container Apps now supports confidential computing in public preview.

- Key changes or new features  
This update introduces hardware-based Trusted Execution Environments (TEEs) to containerized workloads running in Azure Container Apps. It enhances security by enabling code and data to be protected while in use, complementing existing encryption for data at rest and in transit. Developers can now build applications that handle sensitive data with greater assurance against insider threats and compromised infrastructure.

- Target audience affected  
Developers and IT professionals deploying containerized applications on Azure who require enhanced data protection and compliance. Security architects and DevOps teams focused on confidential computing scenarios will benefit from this capability.

- Important notes if any  
As this feature is in public preview, it is not recommended for production workloads yet. Users should evaluate the feature in test environments and monitor Azure updates for general availability and additional enhancements. Integration may require updates to container images and deployment configurations to leverage TEEs effectively.

For more details, visit: https://azure.microsoft.com/updates?id=525455

**Details**:

The recent public preview release of confidential computing support in Azure Container Apps introduces hardware-based Trusted Execution Environments (TEEs) to containerized workloads, enhancing data security beyond traditional encryption methods. This update addresses the growing need for protecting data and code in use, complementing Azure’s existing encryption of data at rest and in transit by enabling secure processing within isolated, tamper-resistant environments.

**Background and Purpose**  
Confidential computing is a security paradigm designed to protect data while it is being processed, mitigating risks from privileged access or compromised hosts. Prior to this update, Azure Container Apps provided secure and scalable container hosting but lacked native support for TEEs. By integrating confidential computing capabilities, Azure Container Apps now enable organizations to run sensitive workloads with stronger guarantees against data exposure, meeting compliance and regulatory requirements for data privacy and security.

**Specific Features and Detailed Changes**  
- Introduction of hardware-based TEEs (such as Intel SGX or AMD SEV) within Azure Container Apps environments.  
- Support for running containers inside secure enclaves that isolate code and data from the host OS, hypervisor, and other tenants.  
- Seamless integration with existing Azure Container Apps deployment workflows, allowing developers to enable confidential computing with minimal changes.  
- Enhanced attestation mechanisms to verify the integrity and authenticity of the enclave before workload execution.  
- Continued support for encryption of data at rest and in transit, now complemented by encryption and protection during computation.

**Technical Mechanisms and Implementation Methods**  
Confidential computing in Azure Container Apps leverages hardware TEEs that create isolated execution environments on the underlying physical servers. When a container is deployed with confidential computing enabled, its workload runs inside a secure enclave that encrypts memory and CPU registers, preventing unauthorized access even from privileged system software. Azure’s attestation service validates the enclave’s identity and state, ensuring that only trusted code executes within the enclave. This process integrates with container orchestration and runtime layers, abstracting complexity from developers while maintaining high security standards.

**Use Cases and Application Scenarios**  
- Processing sensitive financial data or personally identifiable information (PII) in multi-tenant environments without exposing data to cloud operators.  
- Running confidential machine learning models where intellectual property protection is critical.  
- Secure multi-party computations where data privacy must be preserved while sharing insights.  
- Compliance-driven workloads requiring proof of data protection during processing, such as healthcare or government applications.

**Important Considerations and Limitations**  
- As a public preview feature, confidential computing support may have limitations in regional availability and SLA guarantees.  
- Performance overhead may be incurred due to enclave initialization and memory encryption, which should be evaluated against workload requirements.  
- Not all container images or runtime libraries may be compatible with TEEs; developers should validate their applications accordingly.  
- Debugging and monitoring workloads running inside enclaves require specialized tools and approaches due to the isolation properties.  
- Integration with third-party security tools may be limited until broader ecosystem support matures.

**Integration with Related Azure Services**  
- Azure Key Vault can be used to securely provision and manage cryptographic keys within confidential computing workflows.  
- Azure Attestation service provides the necessary attestation and trust verification mechanisms for enclaves.  
- Azure Monitor and Azure Security Center are expected to evolve to support confidential computing telemetry and security posture assessments.  
- Integration with Azure DevOps pipelines facilitates automated deployment and management of confidential container workloads.  
- This feature complements Azure Confidential Ledger and Azure Confidential VMs, enabling a comprehensive confidential computing strategy across different compute models.

In summary, the public preview of confidential computing in Azure Container Apps significantly enhances the security posture of containerized applications by enabling hardware-based TEEs that protect data in use, expanding Azure’s comprehensive data protection capabilities and enabling new confidential workload scenarios with minimal developer friction.

---

### 44. Public Preview: Standard V2 NAT Gateway and StandardV2 Public IPs

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Standard V2 NAT Gateway and StandardV2 Public IPs](https://azure.microsoft.com/updates?id=525405)

**Update ID**: 525405
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure NAT Gateway

**Summary**:

- What was updated  
Azure introduced the StandardV2 SKU NAT Gateway and StandardV2 Public IPs, now available in public preview.

- Key changes or new features  
The StandardV2 NAT Gateway offers enhanced scalability and resilience for outbound connectivity. It supports zone-redundancy, enabling high availability across availability zones in supported regions. This improves fault tolerance and uptime. The new StandardV2 Public IPs complement the NAT Gateway by providing zone-redundant public IP addresses. These enhancements enable better traffic distribution and improved network performance for outbound scenarios.

- Target audience affected  
Developers and IT professionals managing Azure virtual networks, especially those requiring highly available and scalable outbound internet connectivity for their applications and services.

- Important notes if any  
As this is a public preview feature, it should be used with caution in production environments. Users should validate compatibility with their workloads and monitor Azure updates for GA (general availability) announcements. Zone-redundancy requires deployment in regions supporting availability zones.  

For more details, visit: https://azure.microsoft.com/updates?id=525405

**Details**:

The Azure update announces the public preview of the StandardV2 SKU NAT Gateway and StandardV2 Public IPs, introducing enhanced capabilities for outbound network connectivity with improved scalability, resilience, and availability.

**Background and Purpose:**  
Azure NAT Gateway provides managed outbound internet connectivity for virtual networks, simplifying network address translation and eliminating the need for complex user-managed NAT solutions. The StandardV2 SKU represents the next generation of NAT Gateway and Public IP services, designed to address evolving enterprise requirements for higher availability, zone redundancy, and improved traffic management. This update aims to enhance the robustness and scalability of outbound connectivity, particularly in multi-zone and large-scale deployments.

**Specific Features and Detailed Changes:**  
- **Zone-Redundancy:** StandardV2 NAT Gateway supports zone-redundant deployment in regions with availability zones, ensuring high availability by distributing resources across multiple zones. This reduces the risk of downtime due to zone failures.  
- **Improved Scalability:** The StandardV2 SKU increases the maximum number of outbound flows and supports larger SNAT (Source Network Address Translation) port pools, enabling better handling of high-volume outbound traffic.  
- **Enhanced Traffic Survivability:** The update introduces mechanisms to maintain outbound connectivity even during transient failures or maintenance events, improving overall network resiliency.  
- **StandardV2 Public IPs:** These new public IP addresses complement the NAT Gateway by offering zone-redundant, scalable, and resilient public IPs that can be associated with various Azure resources, supporting consistent outbound connectivity and simplified IP management.

**Technical Mechanisms and Implementation Methods:**  
StandardV2 NAT Gateway leverages Azure’s underlying infrastructure to distribute NAT resources across availability zones, using zone-redundant public IP prefixes and load balancing techniques to maintain connectivity. It manages SNAT port allocation dynamically to optimize resource utilization and reduce port exhaustion. The service integrates with virtual networks and subnets, allowing seamless attachment and automatic outbound connectivity for associated resources without manual NAT configuration. The StandardV2 Public IPs use zone-redundant IP prefixes, ensuring IP address availability and failover across zones.

**Use Cases and Application Scenarios:**  
- **High Availability Applications:** Applications requiring uninterrupted outbound internet access benefit from zone-redundant NAT Gateway deployments to mitigate zone-level failures.  
- **Large-Scale Enterprise Networks:** Enterprises with extensive outbound traffic can leverage the increased SNAT port capacity and scalability for reliable connectivity.  
- **Multi-Zone Architectures:** Deployments spanning multiple availability zones can maintain consistent outbound connectivity with zone-redundant IPs and NAT Gateway resources.  
- **Simplified Network Management:** Organizations seeking to reduce complexity in managing outbound NAT and IP addresses can utilize the managed StandardV2 services for streamlined operations.

**Important Considerations and Limitations:**  
- As a public preview feature, StandardV2 NAT Gateway and Public IPs may have limited regional availability and are subject to change before general availability.  
- Users should evaluate compatibility with existing network configurations and test workloads in non-production environments before full deployment.  
- Pricing and SLA details for StandardV2 SKUs may differ from Standard SKU and should be reviewed accordingly.  
- Certain legacy features or integrations may not yet be supported in StandardV2 and require validation.

**Integration with Related Azure Services:**  
StandardV2 NAT Gateway integrates seamlessly with Azure Virtual Network, Azure Firewall, Azure Load Balancer, and Azure Application Gateway, providing consistent outbound connectivity across these services. It supports association with subnets and virtual machine scale sets, enabling scalable and resilient outbound access. The zone-redundant Public IPs can be used with Azure Kubernetes Service (AKS), Azure App Service Environment, and other PaaS offerings requiring stable outbound IP addresses.

In summary, the StandardV2 NAT Gateway and StandardV2 Public IPs public preview introduces zone-redundant, scalable, and resilient outbound connectivity solutions designed to enhance high availability and simplify network management for enterprise-grade Azure deployments.

---

### 45. Generally Available: SQL database in Microsoft Fabric

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: SQL database in Microsoft Fabric](https://azure.microsoft.com/updates?id=525388)

**Update ID**: 525388
**Data source**: Azure Updates API

**Categories**: Launched, Analytics, Microsoft Fabric

**Summary**:

- What was updated  
Microsoft Fabric now offers SQL database as a generally available (GA) service.  

- Key changes or new features  
The SQL database in Fabric is built on the proven SQL Server and Azure SQL Database engine, providing a fully SaaS-native experience. It enables developers and data professionals to unify operational and analytical workloads within a single environment. The service emphasizes speed and security, allowing seamless integration of transactional and analytical data processing without managing infrastructure.  

- Target audience affected  
Developers, data engineers, database administrators, and IT professionals working with data platforms and analytics in Azure environments.  

- Important notes if any  
As a GA release, the SQL database in Fabric is production-ready and supported for enterprise workloads. This offering simplifies data architecture by consolidating workloads previously handled by separate systems, improving efficiency and governance. Users should evaluate integration with existing Microsoft Fabric components and consider migration strategies for current SQL workloads to leverage this unified platform.  

For more details, visit: https://azure.microsoft.com/updates?id=525388

**Details**:

The recent general availability of the SQL database in Microsoft Fabric marks a significant advancement in cloud data platform capabilities by delivering a fully SaaS-native SQL database service built on the proven SQL Server and Azure SQL Database engine. This update aims to unify operational and analytical workloads within a single environment, enhancing developer productivity and data professional efficiency through a secure, scalable, and integrated solution.

**Background and Purpose**  
Microsoft Fabric is an integrated analytics platform designed to simplify data engineering, data science, and business intelligence workflows. Prior to this update, users often managed separate systems for transactional (OLTP) and analytical (OLAP) workloads, leading to complexity, latency, and data silos. The introduction of a native SQL database within Fabric addresses these challenges by providing a unified data engine that supports both operational and analytical processing natively, reducing the need for data movement and synchronization between disparate systems. This aligns with the industry trend towards converged data platforms that streamline data management and accelerate insights.

**Specific Features and Detailed Changes**  
- **SaaS-Native SQL Database**: Delivered as a fully managed service within Microsoft Fabric, eliminating infrastructure management overhead.  
- **Unified Workloads**: Supports both transactional and analytical queries with optimized performance, enabling real-time analytics on operational data.  
- **Built on Trusted Engine**: Leverages the mature SQL Server and Azure SQL Database engine, ensuring compatibility with existing T-SQL, tools, and security models.  
- **Security and Compliance**: Incorporates Azure’s enterprise-grade security features, including data encryption at rest and in transit, role-based access control, and compliance certifications.  
- **Elastic Scalability**: Dynamically scales compute and storage independently to meet varying workload demands without downtime.  
- **Integration with Fabric Components**: Seamlessly integrates with other Microsoft Fabric services such as OneLake (data lake), Power BI for analytics, and Data Factory for data orchestration.

**Technical Mechanisms and Implementation Methods**  
The SQL database in Fabric is architected as a multi-tenant, distributed service running on Azure infrastructure, leveraging containerization and microservices for scalability and resilience. It uses a decoupled storage-compute architecture where data is stored in OneLake, Microsoft Fabric’s unified data lake, enabling consistent data access across workloads. The compute layer executes SQL queries using a query optimizer adapted from Azure SQL Database, supporting both OLTP and OLAP workloads with adaptive caching and indexing strategies. Security is enforced through integration with Azure Active Directory and Fabric’s identity management, ensuring seamless authentication and authorization.

**Use Cases and Application Scenarios**  
- **Real-Time Operational Analytics**: Businesses can run analytics directly on live transactional data without ETL delays, supporting scenarios like fraud detection, inventory management, and customer 360 views.  
- **Unified Data Platform for BI and AI**: Data professionals can prepare, query, and visualize data within Fabric using Power BI and Azure Machine Learning, streamlining data science workflows.  
- **Modern Application Development**: Developers can build SaaS applications that require both transactional consistency and analytical insights using a single database service.  
- **Data Consolidation**: Organizations consolidating multiple data silos into a single Fabric workspace benefit from simplified data governance and lineage tracking.

**Important Considerations and Limitations**  
- While the service supports a broad range of SQL Server features, some advanced or legacy SQL Server functionalities may not be fully supported initially.  
- As a SaaS service, customization of underlying infrastructure is limited compared to IaaS or on-premises deployments.  
- Performance tuning requires understanding of Fabric’s resource governance and scaling options, which differ from traditional SQL Server environments.  
- Migration of existing databases requires careful planning to leverage Fabric’s data lake storage and integration patterns effectively.

**Integration with Related Azure Services**  
The SQL database in Fabric is tightly integrated with Azure ecosystem components:  
- **OneLake**: Acts as the unified storage layer, enabling consistent data access and governance.  
-

---

### 46. Public Preview: Support for Italian and Portuguese in Azure Cosmos DB for NoSQL full-text search 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Support for Italian and Portuguese in Azure Cosmos DB for NoSQL full-text search ](https://azure.microsoft.com/updates?id=523824)

**Update ID**: 523824
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB for NoSQL full-text search now includes support for Italian and Portuguese languages in public preview.

- Key changes or new features  
The update expands the set of supported languages for full-text search, enabling language-aware tokenization, stemming, and relevance ranking specifically tailored for Italian and Portuguese. This enhancement allows developers to build richer, more accurate search experiences for applications targeting users in these language regions.

- Target audience affected  
Developers building multilingual applications with Azure Cosmos DB for NoSQL that require advanced search capabilities, as well as IT professionals managing global deployments needing localized search support.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Feedback from users during the preview phase will help improve language processing quality. Developers should test and validate search behavior for Italian and Portuguese content to ensure it meets application requirements.

**Details**:

The recent Azure Cosmos DB for NoSQL update introduces public preview support for Italian and Portuguese languages in its full-text search capabilities, expanding the service’s language-aware indexing and querying functionalities. This enhancement allows developers and IT professionals to build more linguistically nuanced and relevant search experiences within Cosmos DB applications targeting users who communicate in these languages.

**Background and Purpose of the Update**  
Azure Cosmos DB’s full-text search feature leverages language-specific analyzers to tokenize, normalize, and index text data, enabling efficient and accurate search queries. Prior to this update, the service supported a subset of languages, limiting the effectiveness of search applications for users of unsupported languages. By adding Italian and Portuguese, Microsoft addresses growing demand from global customers to support these widely spoken languages, enhancing the inclusivity and usability of Cosmos DB’s search capabilities in multilingual environments.

**Specific Features and Detailed Changes**  
- **Language Analyzers for Italian and Portuguese:** The update introduces dedicated language analyzers that handle language-specific linguistic rules such as stemming, stop words, and tokenization tailored to Italian and Portuguese.  
- **Improved Text Normalization:** These analyzers improve the normalization process by accounting for accents, diacritics, and morphological variations common in these languages, resulting in more relevant search results.  
- **Seamless Integration with Existing Search APIs:** Developers can specify the language parameter in their full-text search queries or indexing policies to activate the appropriate analyzer without changing application logic significantly.  

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Cosmos DB’s full-text search uses Lucene-based indexing technology, which supports pluggable language analyzers. The Italian and Portuguese analyzers apply language-specific token filters, stemmers, and stop word lists during the indexing phase. When documents are ingested or updated, the text fields marked for full-text search are processed through these analyzers, creating language-aware inverted indexes. At query time, the search engine applies the same analyzers to the query text to ensure consistent matching. This mechanism improves precision and recall for search operations involving Italian and Portuguese content.

**Use Cases and Application Scenarios**  
- **Multilingual Customer Support Systems:** Enterprises can build support portals that index and search user-generated content, FAQs, or documentation in Italian and Portuguese, improving self-service capabilities.  
- **E-commerce Platforms:** Retailers targeting Italian and Portuguese-speaking markets can implement product search features that understand linguistic nuances, such as plural forms and synonyms.  
- **Content Management Systems:** Publishers and media companies can index articles, blogs, and metadata in these languages, enabling efficient content discovery and recommendation.  
- **Legal and Compliance Applications:** Organizations can perform full-text search on Italian and Portuguese legal documents, contracts, and regulations with higher accuracy.

**Important Considerations and Limitations**  
- **Public Preview Status:** As a preview feature, it may not yet be fully optimized or supported for production workloads. Users should test thoroughly and monitor for any issues.  
- **Language Coverage:** While Italian and Portuguese are now supported, other languages remain unsupported or in preview, so multilingual applications may require fallback strategies.  
- **Indexing Costs and Performance:** Language analyzers add processing overhead during indexing; performance and RU consumption should be evaluated in context.  
- **Customization Limits:** Currently, custom analyzers or user-defined token filters for these languages may not be supported, limiting fine-grained control.

**Integration with Related Azure Services**  
- **Azure Cognitive Search:** While Cosmos DB provides integrated full-text search, for advanced search scenarios, data can be exported to Azure Cognitive Search, which also supports Italian and Portuguese with richer linguistic features.  
- **Azure Functions and Logic Apps:** These can be used to automate data ingestion and indexing workflows, ensuring that Italian and Portuguese content is consistently processed.  
- **Azure Monitor and Application Insights:** Monitoring tools can track search query performance and errors related to language processing, aiding in operational management.  
- **Azure Synapse Analytics:** For

---

### 47. Public Preview: Azure Cosmos DB MCP ToolKit for Microsoft Foundry Agent Service 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Cosmos DB MCP ToolKit for Microsoft Foundry Agent Service ](https://azure.microsoft.com/updates?id=523814)

**Update ID**: 523814
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB for NoSQL introduced the MCP Toolkit integration with Microsoft Foundry Agent Service, now available in public preview.

- Key changes or new features  
The MCP Toolkit enables direct connectivity between Microsoft Foundry Agents and Azure Cosmos DB data. This integration simplifies data access and management by allowing Foundry Agents to interact seamlessly with Cosmos DB, enhancing real-time data processing and operational workflows.

- Target audience affected  
Developers and IT professionals working with Azure Cosmos DB and Microsoft Foundry Agent Service, particularly those involved in building data-driven applications or managing data pipelines requiring low-latency access to Cosmos DB.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Documentation and support resources are available to assist with integration and usage. Users should monitor for updates as the service evolves toward general availability.

For more details, visit: https://azure.microsoft.com/updates?id=523814

**Details**:

The recent public preview release of the Azure Cosmos DB MCP Toolkit for Microsoft Foundry Agent Service introduces a significant enhancement by enabling direct connectivity between Microsoft Foundry Agents and Azure Cosmos DB for NoSQL data stores. This update is designed to streamline data integration workflows and improve real-time data processing capabilities within distributed environments.

**Background and Purpose**  
Azure Cosmos DB is a globally distributed, multi-model database service optimized for low latency and high availability. Microsoft Foundry Agent Service is a platform for deploying lightweight agents that collect, process, and transmit data across hybrid and edge environments. Prior to this update, integrating Foundry Agents with Cosmos DB required custom connectors or intermediate services, which added complexity and latency. The MCP Toolkit addresses this gap by providing a native integration layer, simplifying data ingestion and enabling more efficient data operations.

**Specific Features and Detailed Changes**  
The MCP Toolkit offers a set of libraries and configuration templates that allow Foundry Agents to authenticate, connect, and interact directly with Cosmos DB containers. Key features include:  
- Native support for Cosmos DB’s NoSQL API, enabling CRUD operations on JSON documents.  
- Secure authentication using Azure Active Directory (AAD) or Cosmos DB keys, ensuring compliance with enterprise security standards.  
- Configuration-driven deployment, allowing agents to be easily set up with minimal coding.  
- Support for batching and retry policies to handle transient failures and optimize throughput.  
- Telemetry and logging integration for monitoring data flows and troubleshooting.

**Technical Mechanisms and Implementation Methods**  
Under the hood, the MCP Toolkit leverages Cosmos DB’s SDKs optimized for .NET and other supported languages used by Foundry Agents. The toolkit abstracts connection management, token renewal, and request handling, exposing a simplified API surface for agent developers. Communication between agents and Cosmos DB occurs over HTTPS using RESTful calls, with JSON serialization for data payloads. The toolkit also integrates with Azure Managed Identities when deployed in Azure environments, enabling seamless and secure authentication without manual credential management.

**Use Cases and Application Scenarios**  
This integration is particularly beneficial for scenarios requiring real-time data ingestion and processing at the edge or in hybrid cloud architectures. Examples include:  
- Industrial IoT deployments where Foundry Agents collect sensor data and push it directly to Cosmos DB for analytics and alerting.  
- Retail environments using Foundry Agents to capture transactional data and update customer profiles in Cosmos DB in near real-time.  
- Telemetry aggregation from distributed applications, enabling centralized storage and querying in Cosmos DB.  
- Any scenario requiring low-latency, high-throughput ingestion of JSON document data from edge or on-premises sources into Azure’s globally distributed database.

**Important Considerations and Limitations**  
As this is a public preview release, users should be aware of potential limitations such as:  
- Limited SLA guarantees and possible feature changes before general availability.  
- The toolkit currently supports only the NoSQL API of Cosmos DB; other APIs like MongoDB or Cassandra are not supported.  
- Performance tuning and scaling considerations must be managed carefully, especially in high-throughput scenarios.  
- Security best practices should be followed, including proper management of access keys and use of AAD where possible.  
- Compatibility with existing Foundry Agent versions should be verified to avoid integration issues.

**Integration with Related Azure Services**  
The MCP Toolkit complements other Azure services by enabling seamless data flow into Cosmos DB, which can then be leveraged by:  
- Azure Synapse Analytics for large-scale data analysis.  
- Azure Functions or Logic Apps for event-driven processing triggered by Cosmos DB change feed.  
- Azure Monitor and Azure Security Center for monitoring and securing data operations.  
- Azure IoT Hub and Azure Digital Twins when combined with Foundry Agents for comprehensive IoT solutions.

In summary, the Azure Cosmos DB MCP Toolkit for Microsoft Foundry Agent Service public preview provides a streamlined, secure, and efficient method for integrating Foundry Agents with Cosmos DB NoSQL databases, facilitating real-time data ingestion and processing

---

### 48. Generally Available: Fuzzy search in Azure Cosmos DB for NoSQL full-text search 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Fuzzy search in Azure Cosmos DB for NoSQL full-text search ](https://azure.microsoft.com/updates?id=523809)

**Update ID**: 523809
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB for NoSQL full-text search now generally supports fuzzy search capabilities.

- Key changes or new features  
Fuzzy search enables typo-tolerant and error-resilient querying within Cosmos DB’s native full-text search. This enhancement allows developers to build search experiences that return relevant results even when user queries contain misspellings or minor errors, improving search accuracy and user satisfaction without additional external services.

- Target audience affected  
Developers building search functionality on Azure Cosmos DB for NoSQL and IT professionals managing data solutions that require robust, user-friendly search capabilities.

- Important notes if any  
This feature is now generally available, meaning it is fully supported for production workloads. Developers can integrate fuzzy search directly into their existing Cosmos DB queries, simplifying implementation and reducing the need for custom error-handling logic in search scenarios. For detailed usage and configuration, refer to the official Azure documentation.

**Details**:

The recent general availability of fuzzy search in Azure Cosmos DB for NoSQL full-text search introduces a significant enhancement aimed at improving search accuracy and user experience by enabling typo-tolerant and error-resilient queries directly within Cosmos DB. This update addresses the common challenge of handling user input errors such as misspellings, typographical mistakes, or slight variations in search terms, which traditionally require additional processing or external search services to manage effectively.

**Background and Purpose**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for high availability and low latency. Its integration with full-text search capabilities allows developers to perform rich text queries on JSON documents stored within Cosmos DB. Prior to this update, full-text search supported exact or prefix matching but lacked native support for fuzzy matching, which is essential for improving search relevance in real-world scenarios where user input is imperfect. The introduction of fuzzy search aims to simplify development by embedding typo-tolerance directly into Cosmos DB’s search engine, reducing the need for custom logic or external search platforms.

**Specific Features and Detailed Changes**  
The key feature introduced is the fuzzy search capability within the existing full-text search syntax. This allows queries to tolerate a configurable number of character edits (insertions, deletions, substitutions) when matching search terms. Developers can specify fuzziness parameters in their search queries, enabling the system to return results that approximate the intended search terms rather than requiring exact matches. This is particularly useful for handling common misspellings or variations in user input.

The update extends the Azure Cosmos DB SQL API full-text search syntax to support fuzzy operators, which can be applied to individual search terms. The underlying Lucene-based search engine now supports Levenshtein distance calculations to determine the closeness of terms. This integration is seamless and does not require changes to the data model or indexing strategies.

**Technical Mechanisms and Implementation Methods**  
Fuzzy search is implemented using Levenshtein distance algorithms within the Cosmos DB full-text search engine. When a fuzzy search query is executed, the engine calculates the edit distance between the query term and indexed terms, returning those within the specified fuzziness threshold. This process leverages the existing inverted index structures optimized for text search, ensuring efficient query execution without significant performance degradation.

Developers can enable fuzzy search by appending a tilde (~) and an optional numeric parameter to search terms in their queries (e.g., `"searchTerm~2"`), where the number indicates the maximum allowed edit distance. The feature is fully managed by Cosmos DB, requiring no additional infrastructure or configuration beyond query syntax changes.

**Use Cases and Application Scenarios**  
Fuzzy search is ideal for applications where user-generated input is prone to errors, such as e-commerce product searches, customer support ticketing systems, content management platforms, and any scenario involving natural language queries. It enhances user experience by increasing the likelihood of returning relevant results despite input inaccuracies. For example, an online retailer can ensure that searches for “iphon” still return results for “iPhone,” reducing user frustration and improving conversion rates.

**Important Considerations and Limitations**  
While fuzzy search improves query flexibility, it may increase query processing time and resource consumption due to the additional computation required for edit distance calculations. Users should carefully balance fuzziness levels to avoid overly broad results that reduce precision. The maximum allowed fuzziness is limited (typically up to 2 edits) to maintain performance and relevance.

Additionally, fuzzy search is currently supported only within the Azure Cosmos DB for NoSQL API’s full-text search functionality and may not be available in other APIs or indexing modes. Developers should test their specific workloads to assess performance impact and relevance of results.

**Integration with Related Azure Services**  
This update complements Azure Cognitive Search by providing built-in fuzzy search capabilities directly within Cosmos DB, potentially reducing the need to export data to external search services for typo-tolerant search scenarios. It integrates seamlessly with Azure Functions, Logic Apps, and other services that query Cosmos DB,

---

### 49. Generally Available: Vector indexing performance improvements in Azure Cosmos DB for NoSQL 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Vector indexing performance improvements in Azure Cosmos DB for NoSQL ](https://azure.microsoft.com/updates?id=523803)

**Update ID**: 523803
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB for NoSQL has improved vector indexing performance, now generally available.

- Key changes or new features  
The update delivers faster vector data inserts and accelerated index build times. These enhancements stem from algorithmic improvements in the vector indexing engine, significantly reducing end-to-end ingestion and indexing latency for large-scale AI workloads involving high-dimensional vector data.

- Target audience affected  
Developers and IT professionals working with Azure Cosmos DB for NoSQL, especially those managing AI, machine learning, or similarity search applications that rely on vector data storage and retrieval.

- Important notes if any  
This performance boost enables more efficient handling of large vector datasets, improving throughput and responsiveness in AI-driven scenarios. Users should consider leveraging these improvements to optimize ingestion pipelines and query performance in their vector-based applications. No changes to APIs or client SDKs are indicated, so integration remains seamless.  

For more details, visit: https://azure.microsoft.com/updates?id=523803

**Details**:

The recent general availability update for Azure Cosmos DB for NoSQL introduces significant performance improvements in vector indexing, specifically targeting faster vector inserts and accelerated index builds. This enhancement is designed to optimize end-to-end ingestion and indexing workflows for large-scale AI and machine learning workloads that rely heavily on vector data.

**Background and Purpose:**  
With the increasing adoption of AI-driven applications, vector search and similarity queries have become critical for scenarios such as recommendation engines, image and speech recognition, and natural language processing. Azure Cosmos DB for NoSQL supports vector data types and indexing to facilitate these workloads. However, as datasets grow in size and complexity, the ingestion and indexing phases can become bottlenecks. This update addresses these challenges by improving the efficiency of vector indexing operations, thereby reducing latency and improving throughput.

**Specific Features and Detailed Changes:**  
- **Faster Vector Inserts:** The update optimizes the ingestion pipeline, allowing higher throughput when inserting vector data points into Cosmos DB containers.  
- **Accelerated Index Builds:** Index construction for vector data is now more efficient, reducing the time required to build or rebuild vector indexes after bulk data loads or schema changes.  
- **Algorithmic Enhancements:** Underlying improvements in the vector indexing algorithms contribute to these performance gains, likely involving optimized data structures and parallel processing techniques.

**Technical Mechanisms and Implementation Methods:**  
The performance improvements stem from algorithmic refinements in the vector indexing engine within Cosmos DB. These may include:  
- Enhanced approximate nearest neighbor (ANN) search algorithms that balance accuracy and speed more effectively.  
- Improved concurrency and parallelism in index maintenance tasks, allowing multiple vector inserts and index updates to proceed simultaneously without contention.  
- Optimized memory management and disk I/O patterns to reduce latency during index writes and rebuilds.  
- Possibly leveraging hardware acceleration or low-level optimizations in Cosmos DB’s storage engine.

**Use Cases and Application Scenarios:**  
- **AI and ML Applications:** Applications performing similarity searches on high-dimensional vector embeddings, such as those generated by deep learning models for images, text, or audio.  
- **Recommendation Systems:** Real-time or batch processing of user-item interaction vectors to generate personalized recommendations.  
- **Semantic Search:** Enhancing search experiences by indexing semantic vectors derived from natural language processing models.  
- **Anomaly Detection:** Fast ingestion and indexing of feature vectors for detecting outliers or unusual patterns in streaming data.

**Important Considerations and Limitations:**  
- While performance is improved, the accuracy and consistency guarantees of vector search remain aligned with Cosmos DB’s existing SLAs.  
- Large-scale vector workloads should still consider partitioning strategies and throughput provisioning to maximize performance.  
- The update focuses on indexing performance; query latency improvements may depend on other factors such as query patterns and provisioned RU/s.  
- Users should validate their specific workload performance post-update, as gains may vary based on data distribution and vector dimensionality.

**Integration with Related Azure Services:**  
- **Azure Cognitive Services:** Vector embeddings generated by Cognitive Services (e.g., Text Analytics, Computer Vision) can be efficiently ingested and indexed in Cosmos DB for downstream similarity search.  
- **Azure Machine Learning:** Models trained and deployed in Azure ML can output vector embeddings that are stored and indexed in Cosmos DB, enabling seamless integration of model inference and data storage.  
- **Azure Synapse Analytics:** For large-scale data processing pipelines, Synapse can orchestrate data flows that include vector data ingestion into Cosmos DB.  
- **Azure Functions and Logic Apps:** Event-driven architectures can leverage these services to automate vector data ingestion and indexing workflows in Cosmos DB.

In summary, this update to Azure Cosmos DB for NoSQL delivers enhanced vector indexing performance through algorithmic improvements, enabling faster vector data ingestion and index building. This advancement supports scalable AI and machine learning workloads by reducing latency and improving throughput, while integrating smoothly with Azure’s broader ecosystem of AI, analytics, and serverless services. Technical professionals should consider these improvements

---

### 50. Generally Available: Float16 data type for vector indexes in Azure Cosmos DB 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Float16 data type for vector indexes in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523796)

**Update ID**: 523796
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB now supports the float16 (half-precision) data type for vector indexes.

- Key changes or new features  
Developers can store and query vector data using float16, which reduces storage requirements by approximately 50% compared to float32. This enables more efficient storage and faster retrieval of vector embeddings without significant loss in precision, optimizing performance for similarity search and AI/ML workloads.

- Target audience affected  
Developers and data engineers working with vector search, machine learning embeddings, and AI applications in Azure Cosmos DB. IT professionals managing database storage and performance will also benefit from reduced storage costs and improved query efficiency.

- Important notes if any  
While float16 reduces storage size, users should evaluate precision requirements for their specific use cases to ensure accuracy is maintained. This update is generally available, meaning it is production-ready and supported for all Cosmos DB users leveraging vector indexes.

**Details**:

The recent general availability of the float16 (half-precision floating-point) data type for vector indexes in Azure Cosmos DB introduces a significant enhancement aimed at optimizing storage and query efficiency for vector-based workloads. This update enables IT professionals and developers to store and process vector data using 16-bit floating-point numbers, reducing storage consumption by approximately 50% compared to the traditional float32 (single-precision) format, while still maintaining high retrieval accuracy for similarity search and machine learning applications.

**Background and Purpose**  
Azure Cosmos DB has increasingly supported vector search capabilities to meet the growing demand for AI-driven applications such as recommendation engines, anomaly detection, and natural language processing. Traditionally, vector data in Cosmos DB has been stored using float32 precision, which, while accurate, incurs higher storage costs and memory usage. The introduction of float16 support addresses the need for more efficient storage and faster query performance, especially for large-scale vector datasets, by leveraging half-precision floating-point representation without significantly compromising the quality of vector similarity computations.

**Specific Features and Detailed Changes**  
- **Float16 Data Type Support:** Users can now define vector indexes using the float16 data type, enabling half-precision storage of vector components.  
- **Storage Efficiency:** Float16 reduces the storage footprint of vector data by half compared to float32, directly impacting cost savings and scalability.  
- **Querying and Indexing:** Cosmos DB’s vector search algorithms have been optimized to handle float16 vectors, ensuring that similarity search operations such as cosine similarity or Euclidean distance calculations remain performant and accurate.  
- **Backward Compatibility:** Existing float32 vector indexes remain supported, allowing gradual migration or mixed usage scenarios.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Cosmos DB converts and stores vector data in float16 format, which uses 16 bits per component instead of 32. This half-precision format follows the IEEE 754 standard for binary16 floating-point representation. During query execution, the system performs similarity computations directly on float16 data or internally converts to higher precision if necessary to maintain accuracy. The indexing engine is adapted to efficiently handle the reduced precision format, optimizing memory bandwidth and cache utilization. Developers specify the data type in the vector index definition via the Cosmos DB API or SDK, enabling seamless integration into existing data models.

**Use Cases and Application Scenarios**  
- **Large-Scale Vector Search:** Applications involving millions or billions of vectors, such as image or text embeddings, benefit from reduced storage costs and faster retrieval times.  
- **AI and ML Pipelines:** Embedding storage for natural language processing, recommendation systems, and anomaly detection can leverage float16 to optimize resource usage.  
- **Edge and IoT Scenarios:** Systems with constrained storage or bandwidth can store vector data more compactly without significant loss of precision.  
- **Cost-Sensitive Environments:** Organizations aiming to optimize cloud expenditure on storage and compute resources will find float16 support advantageous.

**Important Considerations and Limitations**  
- **Precision Trade-offs:** Float16 offers less numerical precision and dynamic range than float32, which may impact the accuracy of similarity computations in some edge cases. Testing is recommended to validate acceptable accuracy for specific workloads.  
- **Compatibility:** Some client libraries or SDK versions may require updates to fully support float16 vector indexes.  
- **Migration:** Existing float32 vector data will not automatically convert to float16; manual data transformation and reindexing are necessary.  
- **Query Performance:** While storage and memory usage improve, actual query latency gains depend on workload characteristics and should be benchmarked.

**Integration with Related Azure Services**  
- **Azure Cognitive Search:** Vector data stored in Cosmos DB with float16 can be integrated with Azure Cognitive Search for enhanced AI-powered search experiences.  
- **Azure Machine Learning:** Embeddings generated via Azure ML pipelines can be stored efficiently in Cosmos DB using float16 vectors, facilitating scalable model deployment and inference.  
- **Azure Synapse Analytics

---

### 51. Generally Available: Azure Cosmos DB for Visual Studio Code  

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Cosmos DB for Visual Studio Code  ](https://azure.microsoft.com/updates?id=523782)

**Update ID**: 523782
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB extension for Visual Studio Code has reached general availability (GA).

- Key changes or new features  
The extension enables developers to seamlessly create, manage, and query Azure Cosmos DB resources directly within VS Code. It supports multiple APIs including Core (SQL), MongoDB, Cassandra, Gremlin, and Table. Key features include:  
• Intuitive UI for creating and managing databases, containers, and items  
• Built-in query editor with syntax highlighting and IntelliSense  
• Integration with Azure account for easy resource browsing and connection management  
• Support for local Cosmos DB emulator for development and testing  
• Ability to view and edit JSON documents inline  
• Enhanced productivity with quick actions and command palette support

- Target audience affected  
Developers building cloud-native applications using Azure Cosmos DB who prefer integrated development environments. IT professionals involved in managing Cosmos DB resources can also benefit from streamlined resource management within VS Code.

- Important notes if any  
This GA release ensures production readiness with improved stability and performance. Developers should update to the latest extension version to leverage new capabilities. The extension complements Azure portal and CLI tools, providing a developer-centric experience for Cosmos DB operations.

**Details**:

The Azure Cosmos DB extension for Visual Studio Code has reached general availability, providing developers with a powerful, integrated environment for managing and developing Cosmos DB resources directly within their code editor. This update addresses the growing need for streamlined, efficient workflows in building intelligent and data-driven applications by embedding Cosmos DB capabilities into a widely used development tool.

Background and Purpose  
Modern applications increasingly rely on globally distributed, low-latency, and highly scalable databases to support AI-driven, connected, and autonomous functionalities. Azure Cosmos DB is Microsoft’s multi-model, globally distributed database service designed for such scenarios. Prior to this update, developers typically managed Cosmos DB resources through the Azure portal or separate tools, which could disrupt development flow. The purpose of this update is to bring Cosmos DB management and development closer to the coding experience, reducing context switching and accelerating development cycles.

Specific Features and Detailed Changes  
The general availability release of the Azure Cosmos DB extension for Visual Studio Code introduces several key features:  
- **Resource Management:** Create, update, and delete Cosmos DB accounts, databases, containers, and items directly from VS Code.  
- **Querying and Data Exploration:** Execute SQL queries against Cosmos DB containers with syntax highlighting, IntelliSense, and result visualization within the editor.  
- **Multi-API Support:** Support for Cosmos DB’s multiple APIs including Core (SQL), MongoDB, Cassandra, Gremlin, and Table APIs, enabling developers working with different data models to use a unified tool.  
- **Integrated Emulator Support:** Seamless integration with the Cosmos DB Emulator for local development and testing without incurring cloud costs.  
- **Connection Management:** Securely manage connection strings and keys, with support for Azure Active Directory authentication.  
- **Code Snippets and IntelliSense:** Enhanced productivity through code snippets and IntelliSense for Cosmos DB queries and resource definitions.  

Technical Mechanisms and Implementation Methods  
The extension leverages the Azure Cosmos DB SDKs and REST APIs under the hood to interact with Cosmos DB resources. It uses the Azure Resource Manager (ARM) APIs for provisioning and managing database accounts and resources. Query execution is performed via direct calls to the Cosmos DB query engine, with results streamed back to the VS Code interface. Authentication is handled through Azure identity libraries supporting token-based authentication and integration with Azure AD. The extension is built on the Visual Studio Code Extensions API, enabling a smooth UI/UX with tree views, editors, and command palettes.

Use Cases and Application Scenarios  
- **Development and Testing:** Developers can rapidly prototype and test Cosmos DB queries and data models within their IDE without switching contexts.  
- **Data Exploration:** Data engineers and developers can explore and validate data stored in Cosmos DB containers interactively.  
- **Multi-API Development:** Teams working with different Cosmos DB APIs can use a single tool to manage all their data models.  
- **Local Development:** Using the integrated emulator support, developers can build and test applications offline or in isolated environments.  
- **CI/CD Integration:** The extension can be used in conjunction with VS Code automation and scripting to support continuous integration and deployment pipelines.  

Important Considerations and Limitations  
- The extension requires Visual Studio Code version compatibility and may have dependencies on specific Node.js versions.  
- While supporting multiple APIs, some advanced features specific to certain APIs might not be fully exposed in the extension interface.  
- Performance of query execution and data visualization depends on network latency and resource throughput provisioning in Cosmos DB.  
- Security best practices should be followed when managing connection strings and keys within the IDE to avoid credential exposure.  

Integration with Related Azure Services  
The extension integrates tightly with Azure Active Directory for authentication and with Azure Resource Manager for resource provisioning. It complements Azure DevOps and GitHub workflows by enabling local development and testing. Additionally, it works well alongside Azure Functions and Azure App Service extensions in VS Code, facilitating end-to-end cloud-native application development. The integration with the Cosmos DB Emulator allows seamless transition from local development to cloud deployment.

---

### 52. Generally Available: Azure Cosmos DB Mirroring in Microsoft Fabric 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Cosmos DB Mirroring in Microsoft Fabric ](https://azure.microsoft.com/updates?id=523773)

**Update ID**: 523773
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB Mirroring in Microsoft Fabric is now generally available.

- Key changes or new features  
This feature enables seamless integration of existing Azure Cosmos DB operational workloads with Microsoft Fabric’s analytical environment. Developers and IT professionals can leverage Fabric’s advanced analytics capabilities, such as running SQL queries directly on mirrored Cosmos DB data without impacting the operational database. This integration facilitates real-time analytics and reporting on Cosmos DB data within Fabric, improving data insights and decision-making workflows.

- Target audience affected  
Developers and IT professionals who manage Azure Cosmos DB workloads and require integrated analytics solutions within Microsoft Fabric. This is particularly relevant for teams looking to combine operational and analytical workloads efficiently.

- Important notes if any  
The mirroring process ensures data consistency between Cosmos DB and Fabric, minimizing latency and operational impact. Users should review integration best practices to optimize performance and cost. This GA release marks a stable production-ready option for combining Cosmos DB’s operational data with Fabric’s analytics platform.

For more details, visit: https://azure.microsoft.com/updates?id=523773

**Details**:

Azure Cosmos DB Mirroring in Microsoft Fabric is now generally available, enabling seamless integration of operational data workloads with Fabric’s advanced analytical environment. This update addresses the growing need for real-time analytics on globally distributed, multi-model data stored in Cosmos DB by providing a native, low-latency data mirroring capability directly into Microsoft Fabric’s analytical fabric.

**Background and Purpose**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for mission-critical applications requiring low latency and high availability. Microsoft Fabric is an integrated analytics platform that unifies data engineering, data warehousing, and data science workloads. Prior to this update, integrating Cosmos DB operational data with Fabric analytics required complex ETL pipelines or data movement processes, often introducing latency and operational overhead. The purpose of Cosmos DB Mirroring in Fabric is to simplify and accelerate this integration, enabling near real-time analytics on operational data without impacting transactional workloads.

**Specific Features and Detailed Changes**  
- **Native Mirroring Capability:** Cosmos DB Mirroring creates a continuous, near real-time replica of your Cosmos DB containers inside Microsoft Fabric, eliminating the need for manual data ingestion or batch processing.  
- **SQL Query Support:** The mirrored data can be queried using Fabric’s SQL-based analytical engine, allowing analysts and data scientists to run complex queries and generate insights directly on operational data.  
- **Multi-Model Support:** Supports Cosmos DB’s core data models (document, key-value, graph, column-family) ensuring broad applicability.  
- **Automatic Schema Inference and Updates:** Changes in Cosmos DB container schemas are automatically reflected in the mirrored datasets within Fabric, maintaining schema consistency without manual intervention.  
- **High Throughput and Low Latency:** Designed to handle high-velocity data streams with minimal lag, supporting near real-time analytics scenarios.

**Technical Mechanisms and Implementation Methods**  
The mirroring mechanism leverages Cosmos DB’s change feed feature, which captures inserts and updates in the database. Microsoft Fabric subscribes to this change feed and incrementally applies these changes to a mirrored dataset within Fabric’s storage and compute environment. This approach ensures that data is continuously synchronized with minimal delay. The integration is managed through Fabric’s data pipeline orchestration, which handles schema mapping, error handling, and data consistency checks. Users configure mirroring via the Fabric portal or APIs by specifying the Cosmos DB account, database, and containers to mirror.

**Use Cases and Application Scenarios**  
- **Real-Time Operational Analytics:** Monitor application performance, user behavior, and system health by running analytical queries on live operational data.  
- **Fraud Detection and Anomaly Detection:** Leverage Fabric’s machine learning and AI capabilities on up-to-date transactional data for timely detection of suspicious activities.  
- **Customer 360 and Personalization:** Combine operational customer data with other data sources in Fabric to generate comprehensive customer profiles and personalized experiences.  
- **Data Science and Experimentation:** Provide data scientists with immediate access to fresh operational data for model training and validation without impacting production systems.

**Important Considerations and Limitations**  
- **Latency:** While near real-time, there may be a small delay depending on workload and network conditions; it is not suitable for sub-second latency requirements.  
- **Cost Implications:** Continuous mirroring and increased query workloads in Fabric may incur additional costs; careful monitoring and scaling are advised.  
- **Data Consistency:** The mirrored data reflects eventual consistency aligned with Cosmos DB’s consistency model; applications requiring strict transactional consistency should design accordingly.  
- **Supported Regions and SKUs:** Verify that both Cosmos DB and Microsoft Fabric services are available and supported in your Azure region.  
- **Security and Compliance:** Ensure that data governance policies are maintained, as data is replicated into a new environment; leverage Fabric’s security controls and role-based access.

**Integration with Related Azure Services**  
- **Azure Synapse Link:** While Synapse Link also enables analytical querying of operational data, Cosmos DB Mirroring in Fabric offers tighter integration within

---

### 53. Generally Available: Cosmos DB in Microsoft Fabric 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Cosmos DB in Microsoft Fabric ](https://azure.microsoft.com/updates?id=523768)

**Update ID**: 523768
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Analytics, Azure Cosmos DB, Microsoft Fabric

**Summary**:

- What was updated  
Microsoft has announced the general availability of Cosmos DB integration within Microsoft Fabric.

- Key changes or new features  
This update enables developers and IT professionals to build both operational and analytical workloads seamlessly inside Microsoft Fabric using Cosmos DB. It combines Cosmos DB’s AI-powered capabilities with Fabric’s innovations, allowing users to run SQL queries directly over JSON data. This integration supports real-time data processing and analytics, enhancing the ability to handle large-scale, low-latency applications and complex data scenarios within a unified platform.

- Target audience affected  
Developers building cloud-native applications requiring scalable, globally distributed databases and real-time analytics. IT professionals managing data infrastructure who seek to consolidate operational and analytical workloads within Microsoft Fabric.

- Important notes if any  
This GA release signifies production readiness, encouraging adoption in enterprise environments. Users should consider leveraging the combined AI features and Fabric’s architecture to optimize performance and simplify data workflows. Additional details and best practices can be found in the official Azure update link.

**Details**:

The general availability of Cosmos DB in Microsoft Fabric marks a significant advancement in integrating operational and analytical data workloads within a unified analytics platform. This update enables IT professionals to leverage Azure Cosmos DB’s globally distributed, multi-model NoSQL database capabilities directly inside Microsoft Fabric, facilitating seamless real-time analytics and AI-driven insights over JSON data using familiar SQL queries.

**Background and Purpose**  
Traditionally, operational databases like Cosmos DB and analytical platforms have been managed separately, often requiring complex data movement and synchronization processes. Microsoft Fabric aims to unify data engineering, data warehousing, and analytics into a single SaaS platform. By embedding Cosmos DB into Fabric, Microsoft addresses the need for real-time, low-latency analytics on operational data without ETL overhead, enabling faster decision-making and streamlined data workflows.

**Specific Features and Detailed Changes**  
- **Native Cosmos DB Integration:** Cosmos DB containers can now be directly accessed and queried within Microsoft Fabric’s OneLake data lake, eliminating the need for data export or duplication.  
- **SQL Query over JSON:** Users can run T-SQL-like queries on Cosmos DB JSON documents, leveraging Fabric’s query engine optimized for semi-structured data.  
- **AI-Enhanced Analytics:** Integration with AI features in Cosmos DB, such as anomaly detection and cognitive search, is now accessible within Fabric, enabling enriched analytical models and real-time insights.  
- **Unified Security and Governance:** Cosmos DB data inherits Fabric’s security model, including role-based access control (RBAC), data masking, and auditing, ensuring compliance and data protection.  
- **Real-Time Operational Analytics:** Fabric supports near real-time ingestion and querying of Cosmos DB data, enabling operational dashboards and live monitoring scenarios.

**Technical Mechanisms and Implementation Methods**  
Cosmos DB in Fabric leverages Fabric’s OneLake as a unified data storage layer, where Cosmos DB containers are represented as external tables or views. Fabric’s compute engine translates SQL queries into Cosmos DB’s native query language, optimizing for JSON document structures and partition keys. The integration supports Cosmos DB’s multi-region replication and consistency models, ensuring query results reflect the desired data freshness and availability. AI features are exposed through Fabric’s notebook and pipeline interfaces, allowing data scientists to embed machine learning workflows directly on Cosmos DB data.

**Use Cases and Application Scenarios**  
- **Real-Time Customer 360 Analytics:** Combine operational customer data stored in Cosmos DB with Fabric’s analytical capabilities to generate comprehensive, up-to-date customer profiles.  
- **IoT Telemetry Processing:** Ingest device telemetry into Cosmos DB and use Fabric to run real-time anomaly detection and predictive maintenance analytics.  
- **E-commerce Personalization:** Query Cosmos DB product catalogs and user behavior data in Fabric to power AI-driven recommendations and dynamic pricing models.  
- **Operational Dashboards:** Build live dashboards that query Cosmos DB data directly for monitoring application health, inventory levels, or financial transactions without ETL delays.

**Important Considerations and Limitations**  
- **Query Performance:** While Fabric optimizes SQL queries over JSON, complex or large-scale analytical queries may require tuning of Cosmos DB partition keys and indexing policies.  
- **Consistency Models:** Understanding Cosmos DB’s consistency levels is critical to ensure analytical queries reflect the appropriate data state.  
- **Cost Implications:** Running real-time queries and AI workloads on Cosmos DB data within Fabric may incur additional compute and RU/s charges; careful workload planning is advised.  
- **Data Latency:** Although near real-time, some latency may exist depending on replication and ingestion pipelines, which should be accounted for in time-sensitive applications.

**Integration with Related Azure Services**  
- **Azure Synapse Link:** Cosmos DB in Fabric complements Azure Synapse Link by providing an alternative, integrated analytics experience within Microsoft Fabric.  
- **Azure Data Factory:** Data pipelines can orchestrate data flows between Cosmos DB, Fabric, and other Azure services for ETL/ELT scenarios.  
- **Azure Machine Learning:** AI models developed in Azure ML can

---

### 54. Public Preview: Index Advisor for Azure DocumentDB 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Index Advisor for Azure DocumentDB ](https://azure.microsoft.com/updates?id=523763)

**Update ID**: 523763
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure DocumentDB’s VS Code extension now includes a Public Preview of the Index Advisor feature.

- Key changes or new features  
The Index Advisor provides developers and DBAs with actionable recommendations to optimize indexing strategies for MongoDB workloads on Azure DocumentDB. It leverages natural language processing to analyze query patterns and suggests best practices to improve database performance. Users can view and debug index-related performance issues directly within the VS Code environment.

- Target audience affected  
Developers and IT professionals managing MongoDB workloads on Azure DocumentDB who use Visual Studio Code for development and database management.

- Important notes if any  
This feature is currently in Public Preview, so users should test it in non-production environments and provide feedback. The integration aims to simplify performance tuning by reducing manual index analysis and accelerating query optimization workflows. For more details and updates, refer to the official Azure update page.

**Details**:

The recent Azure update introduces the Public Preview of the Index Advisor for Azure DocumentDB, integrated within the DocumentDB for VS Code extension, designed to enhance the performance tuning and indexing strategy of Azure Cosmos DB’s API for MongoDB workloads. 

Background and Purpose:
Azure Cosmos DB supports multiple APIs, including MongoDB, enabling developers to use familiar MongoDB drivers and tools while benefiting from Cosmos DB’s global distribution and scalability. Indexing is critical for query performance in Cosmos DB, but manually optimizing indexes can be complex and time-consuming. The Index Advisor aims to simplify this process by providing intelligent, actionable recommendations to optimize indexing strategies, thereby improving query performance and reducing RU (Request Unit) consumption.

Specific Features and Detailed Changes:
- Integration with DocumentDB for VS Code extension: The Index Advisor is embedded directly into the developer workflow, allowing users to analyze their MongoDB workloads without leaving the VS Code environment.
- Natural Language Recommendations: The advisor interprets query patterns and workload characteristics, delivering indexing suggestions in natural language that are easy to understand and implement.
- Performance Debugging: Users can view detailed insights into query performance, identify problematic queries, and receive tailored advice on index creation or modification.
- Best Practices Guidance: Beyond indexing, the tool provides recommendations aligned with MongoDB workload best practices on Cosmos DB, helping to optimize overall database performance.

Technical Mechanisms and Implementation Methods:
The Index Advisor analyzes query telemetry and workload patterns collected from the Cosmos DB API for MongoDB. It leverages telemetry data such as query frequency, execution time, and RU consumption to identify indexing gaps or redundancies. Using built-in heuristics and possibly machine learning models, it generates index recommendations that balance performance gains against storage and write overhead. The integration within VS Code allows real-time feedback during development, enabling iterative tuning before deployment. Recommendations are presented in a user-friendly interface that supports direct application of suggested indexes via commands or scripts.

Use Cases and Application Scenarios:
- Developers optimizing MongoDB workloads on Cosmos DB can use the Index Advisor to quickly identify inefficient queries and missing indexes.
- Database administrators can leverage the tool to maintain optimal index configurations in production environments, reducing RU costs and improving latency.
- Teams migrating MongoDB applications to Cosmos DB can utilize the advisor to adapt indexing strategies to Cosmos DB’s indexing model.
- Performance troubleshooting scenarios where query execution times are high or RU consumption spikes can benefit from targeted recommendations.

Important Considerations and Limitations:
- As a Public Preview feature, the Index Advisor may have limitations in coverage or accuracy and should be validated in test environments before production use.
- Recommendations are advisory and should be reviewed in the context of application-specific workload patterns and storage cost implications.
- The tool currently focuses on the MongoDB API for Cosmos DB and may not support other Cosmos DB APIs.
- Index changes can impact write performance and storage costs; thus, changes should be tested and monitored post-implementation.
- Integration requires use of the DocumentDB for VS Code extension, so users must be familiar with this toolchain.

Integration with Related Azure Services:
The Index Advisor complements Azure Cosmos DB’s native monitoring and diagnostic capabilities, such as Azure Monitor and Azure Metrics, by providing actionable indexing insights. It integrates seamlessly with the DocumentDB for VS Code extension, which itself supports development and management of Cosmos DB resources. This update enhances the developer experience by consolidating performance tuning tools within a familiar IDE environment, streamlining workflows that might otherwise require multiple disparate tools or manual analysis.

In summary, the Public Preview of the Index Advisor for Azure DocumentDB embedded in the DocumentDB for VS Code extension offers IT professionals a practical, intelligent tool to optimize indexing and improve the performance of MongoDB workloads on Azure Cosmos DB, leveraging natural language recommendations and integrated debugging capabilities to simplify complex tuning tasks.

---

### 55. Generally Available: Priority-based execution in Azure Cosmos DB 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Priority-based execution in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523754)

**Update ID**: 523754
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB now supports priority-based execution to manage request handling during resource contention.

- Key changes or new features  
Developers and IT professionals can enable priority-based execution to assign priority levels to requests. When the system experiences high load or contention, low-priority requests are throttled first, ensuring that high-priority operations continue with minimal disruption. This feature helps maintain performance for critical workloads by dynamically managing resource allocation based on request priority.

- Target audience affected  
This update primarily benefits developers building applications on Azure Cosmos DB who require differentiated request handling based on workload importance, as well as IT professionals managing database performance and SLAs in multi-tenant or mixed-priority environments.

- Important notes if any  
Priority-based execution must be explicitly enabled and configured. Proper assignment of priority levels to requests is essential to leverage this feature effectively. It is recommended to evaluate workload patterns and define priority policies to optimize throughput and latency during peak usage.

**Details**:

The recent general availability of priority-based execution in Azure Cosmos DB introduces a mechanism to manage request throughput more effectively under resource contention by prioritizing high-priority requests over lower-priority ones. This update addresses the challenge of maintaining performance and responsiveness for critical operations in multi-tenant or high-load environments where request throttling can impact application SLAs.

**Background and Purpose:**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for low-latency and high-throughput workloads. Under heavy load or resource contention, Cosmos DB enforces request rate limiting (throttling) to maintain system stability, typically applying it uniformly across requests. However, in scenarios where some operations are business-critical and others are less urgent, uniform throttling can degrade the performance of high-priority tasks. The priority-based execution feature was introduced to enable differentiated request handling, ensuring that critical workloads maintain higher availability and throughput during contention.

**Specific Features and Detailed Changes:**  
With priority-based execution enabled, Azure Cosmos DB classifies incoming requests based on assigned priority levels. When resource contention occurs, the system selectively throttles lower-priority requests first, preserving throughput for higher-priority operations. This prioritization applies to both read and write requests and integrates with Cosmos DB’s existing rate-limiting and retry policies. The feature is configurable at the client SDK level, allowing developers to specify priority on a per-request basis. This granular control enables fine-tuned workload management without requiring changes to the underlying database infrastructure.

**Technical Mechanisms and Implementation Methods:**  
Priority-based execution leverages Cosmos DB’s request pipeline and resource governance framework. Each request carries metadata indicating its priority level, which the Cosmos DB request router evaluates during contention. The system maintains separate queues or token buckets per priority class, dynamically adjusting throttling thresholds. When throughput limits are approached, the throttling algorithm first applies backpressure to lower-priority queues, preserving tokens for higher-priority requests. This approach ensures fairness while optimizing resource allocation. Client SDKs have been updated to support priority flags, and the feature is backward compatible, defaulting to uniform throttling if priority is not specified.

**Use Cases and Application Scenarios:**  
This feature is particularly beneficial in multi-tenant applications, SaaS platforms, or microservices architectures where different operations have varying criticality. For example, a financial application might prioritize transaction processing requests over analytics queries during peak loads. Similarly, IoT solutions can prioritize telemetry ingestion over bulk data exports. By enabling priority-based execution, organizations can maintain SLAs for mission-critical operations without overprovisioning throughput or manually managing request flows.

**Important Considerations and Limitations:**  
While priority-based execution improves request handling under contention, it does not increase the overall throughput capacity of Cosmos DB. Properly assigning priorities requires understanding workload patterns to avoid starving lower-priority requests. Excessive prioritization can lead to increased latency or failures for non-critical operations. Additionally, this feature requires client SDK support and explicit priority assignment; legacy clients or requests without priority metadata will be treated with default priority. Monitoring and alerting should be adjusted to account for differentiated throttling behavior.

**Integration with Related Azure Services:**  
Priority-based execution complements Azure Monitor and Azure Application Insights by providing telemetry on throttling events segmented by priority, enabling targeted diagnostics. It integrates seamlessly with Azure Functions and Azure Logic Apps when using Cosmos DB triggers or bindings, allowing developers to assign priorities programmatically. Moreover, this feature aligns with Azure API Management policies that can route or modify requests based on priority, facilitating end-to-end priority-aware workflows.

In summary, the general availability of priority-based execution in Azure Cosmos DB empowers technical professionals to optimize throughput management by prioritizing critical requests during contention, enhancing application reliability and performance without requiring infrastructure changes. This update is a strategic enhancement for complex, high-demand environments where differentiated workload handling is essential.

---

### 56. Public Preview: Azure Cosmos DB Fleet Analytics 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Cosmos DB Fleet Analytics ](https://azure.microsoft.com/updates?id=523745)

**Update ID**: 523745
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB introduced Fleet Analytics, now available in public preview.

- Key changes or new features  
Fleet Analytics enables unified monitoring and insights across multiple Cosmos DB accounts, subscriptions, and workloads. It provides large-scale analytics capabilities to help users manage and optimize their entire Cosmos DB environment from a single pane of glass. This includes aggregated metrics, performance trends, and usage patterns across distributed deployments.

- Target audience affected  
Developers and IT professionals managing multiple Azure Cosmos DB accounts or large-scale deployments will benefit from consolidated visibility and operational insights. This is especially useful for teams handling multi-subscription or multi-region Cosmos DB environments.

- Important notes if any  
As a public preview feature, Fleet Analytics may have limited SLA and could undergo changes before general availability. Users should evaluate it in non-production environments and provide feedback to Microsoft. Integration requires appropriate permissions across the Cosmos DB accounts and subscriptions involved.  

For more details and to try the feature, visit the official Azure update page: https://azure.microsoft.com/updates?id=523745

**Details**:

Azure Cosmos DB Fleet Analytics, now available in public preview, introduces a unified analytics solution designed to provide comprehensive insights across multiple Azure Cosmos DB accounts, subscriptions, and workloads at scale. This update addresses the growing complexity of managing distributed, multi-account Cosmos DB environments by enabling centralized monitoring and analysis, which is critical for large enterprises and organizations with extensive Cosmos DB deployments.

**Background and Purpose**  
As organizations increasingly adopt Azure Cosmos DB for globally distributed, mission-critical applications, they often operate numerous Cosmos DB accounts spanning various subscriptions and regions. Traditional monitoring tools focus on single accounts or limited scopes, making it challenging to gain holistic visibility into performance, usage patterns, and operational health across the entire Cosmos DB estate. Fleet Analytics was introduced to fill this gap by aggregating telemetry and metrics from multiple accounts into a unified analytics platform, thereby simplifying management and enabling data-driven decision-making at scale.

**Specific Features and Detailed Changes**  
- **Cross-Account Aggregation:** Fleet Analytics collects and consolidates telemetry data such as request units (RUs) consumption, latency, availability, and throughput metrics from multiple Cosmos DB accounts across subscriptions.  
- **Centralized Dashboard:** Provides a single pane of glass to visualize and analyze fleet-wide metrics, trends, and anomalies.  
- **Customizable Queries and Reports:** Users can run advanced analytics queries over aggregated data to identify usage patterns, optimize resource allocation, and detect potential issues.  
- **Scalability:** Designed to handle large-scale environments with potentially hundreds of Cosmos DB accounts, ensuring performance and responsiveness in analytics workloads.  
- **Public Preview Availability:** The feature is currently in public preview, allowing customers to explore and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
Fleet Analytics leverages Azure Monitor and Azure Data Explorer under the hood to ingest, store, and query telemetry data from Cosmos DB accounts. Each Cosmos DB account emits diagnostic logs and metrics to Azure Monitor, which Fleet Analytics aggregates across subscriptions. The data is then ingested into a centralized Azure Data Explorer cluster optimized for time-series and telemetry data analysis. Users interact with Fleet Analytics through the Azure portal, where pre-built and customizable Kusto Query Language (KQL) queries enable deep insights. Authentication and authorization are managed via Azure Active Directory, ensuring secure access to aggregated data across organizational boundaries.

**Use Cases and Application Scenarios**  
- **Enterprise Monitoring:** Large enterprises with multiple business units can monitor all Cosmos DB deployments centrally, ensuring consistent performance and SLA adherence.  
- **Cost Optimization:** By analyzing RU consumption trends across accounts, organizations can identify over-provisioned or underutilized resources to optimize costs.  
- **Operational Troubleshooting:** Fleet-wide anomaly detection helps quickly pinpoint accounts or regions experiencing latency or availability issues.  
- **Capacity Planning:** Historical usage data aggregated across fleets supports forecasting and scaling decisions.  
- **Compliance and Governance:** Centralized reporting aids in auditing and compliance by providing a comprehensive view of data access and usage patterns.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, Fleet Analytics may have limited SLA guarantees and could undergo significant changes before GA.  
- **Data Latency:** There may be some delay in telemetry data aggregation due to ingestion and processing pipelines.  
- **Permissions:** Users require appropriate Azure RBAC roles across all Cosmos DB accounts and subscriptions to enable data aggregation and access analytics.  
- **Cost Implications:** Additional costs may be incurred for data ingestion, storage, and query processing in Azure Data Explorer and Azure Monitor.  
- **Regional Availability:** Check the Azure region availability for Fleet Analytics as it may initially be limited.

**Integration with Related Azure Services**  
Fleet Analytics integrates tightly with Azure Monitor for telemetry collection and Azure Data Explorer for scalable analytics. It leverages Azure Active Directory for secure access control and can be combined with Azure Logic Apps or Azure Functions for automated alerting and remediation workflows based on fleet-wide insights. Additionally, it complements Azure Cost Management by providing

---

### 57. Generally Available: Azure Cosmos DB fleet pools  

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Cosmos DB fleet pools  ](https://azure.microsoft.com/updates?id=523740)

**Update ID**: 523740
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB introduced the general availability of fleet pools, a new feature designed to simplify large-scale account management.

- Key changes or new features  
Fleet pools enable developers and IT professionals to create and manage a shared pool of capacity across multiple Azure Cosmos DB accounts. This facilitates easier scaling and resource allocation for multitenant SaaS applications. By pooling capacity, organizations can optimize throughput and storage usage, reduce operational overhead, and streamline capacity planning. The feature supports dynamic scaling and better cost management by allowing flexible distribution of resources among tenants.

- Target audience affected  
This update primarily benefits developers building multitenant SaaS applications on Azure Cosmos DB and IT professionals responsible for managing large-scale Cosmos DB deployments.

- Important notes if any  
Fleet pools are now generally available, meaning they are fully supported for production workloads. Users should evaluate their multitenancy and scaling strategies to leverage fleet pools for improved efficiency and cost savings. For detailed implementation guidance, refer to the official Azure Cosmos DB documentation.

**Details**:

The recent general availability of Azure Cosmos DB fleet pools introduces a significant enhancement designed to simplify and optimize capacity management for large-scale, multitenant SaaS applications built on Azure Cosmos DB. This update addresses the operational complexity and cost inefficiencies that arise when managing numerous individual Cosmos DB accounts, enabling IT professionals and developers to streamline resource allocation and scaling.

**Background and Purpose:**  
Azure Cosmos DB is a globally distributed, multi-model database service that offers turnkey global distribution and elastic scaling of throughput and storage. In multitenant SaaS environments, each tenant often requires a dedicated Cosmos DB account or container to isolate data and workloads, which can lead to operational overhead in provisioning, managing, and scaling these accounts individually. The fleet pools feature was introduced to alleviate these challenges by allowing multiple Cosmos DB accounts to share a common pool of provisioned throughput (Request Units per second, or RU/s), thereby simplifying capacity management and improving resource utilization.

**Specific Features and Detailed Changes:**  
- **Fleet Pools Concept:** Fleet pools enable the creation of a shared capacity pool from which multiple Cosmos DB accounts draw throughput. Instead of provisioning RU/s per account, administrators allocate RU/s to the pool, which dynamically distributes capacity to member accounts as needed.  
- **Simplified Capacity Management:** This pooling mechanism reduces the need to estimate and provision throughput for each tenant upfront, allowing for more flexible and efficient scaling.  
- **Dynamic Scaling:** The pool’s throughput can be adjusted independently of individual accounts, enabling centralized control over resource allocation.  
- **Account Membership Management:** Administrators can add or remove Cosmos DB accounts from the fleet pool, facilitating operational agility.  
- **Cost Efficiency:** By sharing throughput across accounts, fleet pools help reduce over-provisioning and optimize cost, especially in scenarios with variable or unpredictable workloads.

**Technical Mechanisms and Implementation Methods:**  
Fleet pools operate by abstracting the throughput provisioning layer. When a fleet pool is created, it is assigned a total RU/s capacity. Cosmos DB accounts linked to this pool do not require individual throughput provisioning; instead, their requests consume RU/s from the shared pool. Internally, Cosmos DB manages the distribution of throughput to ensure fairness and performance isolation as much as possible. The API and Azure Portal provide management capabilities to create fleet pools, assign accounts, and monitor usage metrics. This model leverages Cosmos DB’s existing partitioning and resource governance frameworks to maintain performance SLAs.

**Use Cases and Application Scenarios:**  
- **Multitenant SaaS Applications:** Ideal for SaaS providers who isolate tenant data in separate Cosmos DB accounts but want to reduce the operational burden of managing throughput per tenant.  
- **Variable Workload Patterns:** Applications with tenants exhibiting bursty or unpredictable traffic benefit from the elasticity of shared throughput.  
- **Cost Optimization:** Organizations seeking to optimize database costs by avoiding over-provisioning for low-usage tenants.  
- **Rapid Tenant Onboarding:** Simplifies adding new tenants by associating their accounts with an existing fleet pool without complex throughput provisioning.

**Important Considerations and Limitations:**  
- **Performance Isolation:** While fleet pools provide shared throughput, absolute performance isolation between accounts is not guaranteed; heavy usage by one account may impact others. Proper monitoring and governance are essential.  
- **Throughput Limits:** The total RU/s of the fleet pool must be sized appropriately to meet aggregate demand; insufficient capacity can lead to throttling.  
- **Supported APIs and Regions:** Verify compatibility with the Cosmos DB APIs in use (SQL, MongoDB, Cassandra, etc.) and regional availability of fleet pools.  
- **Billing Model:** Understand how billing is calculated for pooled throughput and individual account usage to avoid unexpected costs.

**Integration with Related Azure Services:**  
Fleet pools integrate seamlessly with Azure Resource Manager (ARM) templates and Azure Policy for governance and automation. Monitoring and alerting can be configured via Azure Monitor and Azure Metrics to track throughput consumption and performance. Additionally, fleet pools complement Azure Cosmos DB’s global distribution

---

### 58. Generally Available: Azure DocumentDB - an open-source, MongoDB-compatible document database service for hybrid and multicloud

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure DocumentDB - an open-source, MongoDB-compatible document database service for hybrid and multicloud](https://azure.microsoft.com/updates?id=523735)

**Update ID**: 523735
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Microsoft has announced the general availability of Azure DocumentDB, a fully managed, MongoDB-compatible document database service. This service is built on the open-source DocumentDB project, now governed by the Linux Foundation, and was formerly known as Azure Cosmos DB for MongoDB.

- Key changes or new features  
Azure DocumentDB offers seamless compatibility with MongoDB APIs, enabling developers to use existing MongoDB drivers and tools without modification. It supports hybrid and multicloud deployments, providing flexibility for data residency and compliance requirements. As a fully managed service, it ensures high availability, automatic scaling, and enterprise-grade security. The open-source foundation under Linux Foundation governance promotes transparency and community-driven innovation.

- Target audience affected  
This update primarily targets developers building document-oriented applications who rely on MongoDB APIs, as well as IT professionals managing hybrid and multicloud database infrastructures seeking a managed, scalable, and secure document database solution.

- Important notes if any  
Existing Azure Cosmos DB for MongoDB users should note the rebranding to Azure DocumentDB and review any migration or compatibility considerations. The open-source governance model may influence long-term support and integration strategies. Users are encouraged to evaluate the service for hybrid and multicloud scenarios to optimize data management and compliance.

**Details**:

Microsoft has announced the general availability of Azure DocumentDB, a fully managed, MongoDB-compatible document database service designed for hybrid and multicloud environments, built on the open-source DocumentDB now governed by the Linux Foundation. This update reflects a strategic evolution from the previous Azure Cosmos DB for MongoDB API, focusing on providing a dedicated, open-source-based document database service that simplifies development and deployment across diverse infrastructures.

**Background and Purpose of the Update**  
Azure DocumentDB emerges from Microsoft’s commitment to open-source and hybrid cloud strategies, addressing the growing demand for flexible, scalable document databases compatible with MongoDB workloads. By transitioning to an open-source core governed by the Linux Foundation, Microsoft aims to enhance community-driven innovation, transparency, and interoperability. The service targets organizations requiring a fully managed document database that supports MongoDB APIs while enabling deployment flexibility across Azure, on-premises, and other clouds.

**Specific Features and Detailed Changes**  
- **MongoDB Compatibility:** Azure DocumentDB supports MongoDB wire protocol and APIs, enabling existing MongoDB applications and tools to work seamlessly without code changes.  
- **Open-Source Foundation:** Built on the open-source DocumentDB project, this service benefits from community contributions and Linux Foundation governance, ensuring long-term sustainability and innovation.  
- **Hybrid and Multicloud Support:** Unlike the previous Cosmos DB MongoDB API, Azure DocumentDB is designed to be deployable not only in Azure but also on-premises and other cloud platforms, facilitating hybrid and multicloud architectures.  
- **Fully Managed Service:** Azure DocumentDB offers automated patching, scaling, backups, and monitoring, reducing operational overhead.  
- **Enterprise-Grade Security and Compliance:** Integration with Azure Active Directory, role-based access control (RBAC), encryption at rest and in transit, and compliance certifications.  
- **Performance and Scalability:** Supports horizontal scaling with sharding and replica sets, optimized for low latency and high throughput workloads.

**Technical Mechanisms and Implementation Methods**  
Azure DocumentDB implements MongoDB wire protocol compatibility by translating MongoDB API calls into its underlying storage engine operations. It uses a distributed architecture with replica sets for high availability and sharding for horizontal scaling. The service leverages Azure infrastructure for compute, storage, and networking, integrating with Azure Monitor and Azure Security Center for observability and security management. Deployment options include Azure-managed instances, Azure Arc-enabled on-premises clusters, and containerized deployments for multicloud scenarios.

**Use Cases and Application Scenarios**  
- **Modern Web and Mobile Applications:** Store JSON-like documents with flexible schemas, ideal for rapidly evolving app data models.  
- **Hybrid Cloud Applications:** Run consistent MongoDB workloads across on-premises and Azure environments, supporting data sovereignty and latency requirements.  
- **Multicloud Deployments:** Enable disaster recovery and workload portability by deploying DocumentDB instances across different cloud providers.  
- **IoT and Real-Time Analytics:** Handle high-velocity, semi-structured data ingestion with scalable, low-latency document storage.  
- **Enterprise SaaS Solutions:** Benefit from managed service capabilities and compliance for secure, scalable multi-tenant applications.

**Important Considerations and Limitations**  
- While Azure DocumentDB offers MongoDB API compatibility, some advanced MongoDB features or specific versions may not be fully supported; verify compatibility for critical workloads.  
- Hybrid and multicloud deployments require network configuration and security considerations, including VPNs or ExpressRoute for private connectivity.  
- Performance tuning and scaling strategies should be planned based on workload patterns, as document databases have different characteristics compared to relational databases.  
- Backup and disaster recovery strategies should leverage Azure-native tools and consider cross-region replication for resilience.

**Integration with Related Azure Services**  
- **Azure Arc:** Enables management and deployment of Azure DocumentDB instances on-premises and across clouds.  
- **Azure Monitor and Azure Log Analytics:** Provide monitoring, alerting, and diagnostics for database health and performance.  
- **Azure Active Directory:** Facilitates

---

### 59. Public Preview: Dynamic data masking with Azure Cosmos DB 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Dynamic data masking with Azure Cosmos DB ](https://azure.microsoft.com/updates?id=523726)

**Update ID**: 523726
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB now supports Dynamic Data Masking (DDM) in public preview, enabling server-side, policy-based masking of sensitive data.

- Key changes or new features  
DDM allows developers and administrators to define masking rules that dynamically obscure sensitive fields when accessed by non-privileged users. This helps prevent unauthorized exposure of confidential information without altering the underlying data. Masking policies are enforced at the database engine level, ensuring consistent protection across applications and APIs.

- Target audience affected  
Developers building applications on Azure Cosmos DB and IT security professionals responsible for data governance and compliance will benefit from this feature. It is particularly relevant for scenarios requiring fine-grained access control to sensitive data in multi-tenant or regulated environments.

- Important notes if any  
As a public preview feature, DDM in Cosmos DB should be tested thoroughly before production deployment. Masking policies can be configured via Azure portal or APIs, and it is essential to review role-based access controls to complement masking. For detailed implementation guidance and limitations, refer to the official Azure documentation.

**Details**:

The recent Azure Cosmos DB update introduces Dynamic Data Masking (DDM) in public preview, a significant enhancement designed to bolster data security by dynamically obfuscating sensitive information at query runtime for non-privileged users. This server-side, policy-driven feature addresses the growing need for granular data protection in multi-tenant and regulated environments without requiring changes to application code.

**Background and Purpose**  
As organizations increasingly leverage Azure Cosmos DB for globally distributed, multi-model databases, protecting sensitive data such as personally identifiable information (PII), financial records, or health data becomes paramount. Traditional data protection methods often rely on encryption at rest or in transit but do not prevent exposure of sensitive fields to authorized users who may not require full data visibility. Dynamic Data Masking fills this gap by enabling real-time masking of data fields based on user roles or permissions, reducing the risk of accidental or malicious data exposure.

**Specific Features and Detailed Changes**  
The DDM feature allows database administrators to define masking policies on specific properties within Cosmos DB containers. These policies specify which fields to mask and the masking rules to apply, such as full masking, partial masking (e.g., showing only last four digits of a credit card), or custom masking formats. Masking is applied transparently during query execution for users without unmasking privileges, while privileged users see the original data. The feature supports role-based access control (RBAC) integration to differentiate privileged and non-privileged users.

**Technical Mechanisms and Implementation Methods**  
DDM operates at the Cosmos DB server layer, intercepting query results before they are returned to the client. Masking policies are defined using Azure CLI, Azure Portal, or ARM templates, specifying container-level or property-level masks. The system leverages Cosmos DB’s native security model and integrates with Azure Active Directory (AAD) for authentication and authorization, ensuring that masking respects user identities and roles. Masking rules are enforced consistently across all supported APIs (SQL, MongoDB, Cassandra, Gremlin, Table) where applicable, maintaining data model integrity.

**Use Cases and Application Scenarios**  
Typical use cases include compliance with data privacy regulations such as GDPR, HIPAA, or CCPA, where sensitive data exposure must be minimized. Organizations can safely provide read access to customer service representatives, analysts, or third-party vendors without revealing full sensitive details. It is also useful in multi-tenant SaaS applications where tenant isolation requires masking of other tenants’ sensitive data. Additionally, DDM supports scenarios involving data analytics and reporting where masked data suffices for insights without compromising privacy.

**Important Considerations and Limitations**  
As a public preview feature, DDM may have limitations in terms of supported data types, API coverage, and performance impact. Masking applies only to query results and does not affect data stored in the database, so encryption and other security measures remain necessary. Privileged users with unmasking rights must be carefully managed to prevent unauthorized data access. Also, complex masking scenarios may require custom logic outside of DDM’s built-in capabilities. Monitoring and auditing access patterns remain essential to detect potential misuse.

**Integration with Related Azure Services**  
DDM integrates seamlessly with Azure Active Directory for identity management and RBAC, enabling fine-grained access control. It complements Azure Defender for Cosmos DB by adding an additional layer of data protection. When combined with Azure Monitor and Azure Policy, organizations can enforce compliance and monitor masking policy adherence. Furthermore, DDM works alongside Cosmos DB’s encryption-at-rest and network security features to provide a comprehensive security posture.

In summary, Azure Cosmos DB’s Dynamic Data Masking in public preview delivers a powerful, policy-driven mechanism to protect sensitive data dynamically at query time, enhancing data privacy and compliance while minimizing application changes. IT professionals can leverage this feature to implement role-based data visibility controls, safeguard sensitive information in multi-user environments, and meet regulatory requirements effectively.

---

### 60. Public Preview: Online and offline migrations in Azure DocumentDB Migration extension 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Online and offline migrations in Azure DocumentDB Migration extension ](https://azure.microsoft.com/updates?id=523721)

**Update ID**: 523721
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure DocumentDB Migration extension for Visual Studio Code is now available in public preview, enabling migration of MongoDB workloads to Azure DocumentDB.

- Key changes or new features  
The extension supports both online and offline migration modes, allowing seamless and zero-cost migration of MongoDB databases. This simplifies the migration process by integrating directly into Visual Studio Code, providing developers and IT professionals with a streamlined tool to move data without downtime or complex configurations.

- Target audience affected  
Developers and IT professionals managing MongoDB workloads who plan to migrate to Azure DocumentDB (now known as Azure Cosmos DB's API for MongoDB).

- Important notes if any  
As this is a public preview, users should test the extension in non-production environments to validate migration workflows. The zero-cost migration feature helps reduce operational expenses during migration, but monitoring and validation post-migration remain essential to ensure data integrity and application compatibility.

**Details**:

The recent public preview release of the Azure DocumentDB Migration extension for Visual Studio Code introduces a streamlined, zero-cost solution for migrating MongoDB workloads to Azure Cosmos DB’s API for MongoDB (formerly known as Azure DocumentDB). This update addresses the growing need for developers and IT professionals to efficiently transition existing MongoDB databases into Azure’s globally distributed, fully managed NoSQL database service with minimal disruption.

**Background and Purpose:**  
As organizations increasingly adopt cloud-native architectures, migrating from self-managed or on-premises MongoDB instances to a fully managed service like Azure Cosmos DB becomes critical for scalability, availability, and operational simplicity. Previously, migration processes often involved complex, manual steps or third-party tools that could incur additional costs and downtime. This update aims to simplify and accelerate MongoDB workload migrations by embedding migration capabilities directly into Visual Studio Code, a widely used development environment.

**Specific Features and Changes:**  
The extension supports both online (live) and offline migration modes:  
- **Online migration** enables continuous data synchronization between the source MongoDB and the target Azure Cosmos DB instance, allowing minimal downtime cutover. This is particularly useful for production environments requiring high availability during migration.  
- **Offline migration** performs a one-time data copy, suitable for development, testing, or scenarios where downtime is acceptable.

The extension provides a guided, wizard-based interface within Visual Studio Code, allowing users to configure source and target connection strings, select databases and collections, and monitor migration progress in real time. It supports schema and data migration, including indexes, ensuring the target Cosmos DB collections maintain query performance characteristics similar to the source MongoDB.

**Technical Mechanisms and Implementation:**  
Under the hood, the extension leverages Azure Cosmos DB’s native MongoDB wire protocol compatibility to ensure seamless data ingestion. For online migrations, it uses change stream listeners on the source MongoDB to capture and replicate ongoing data changes incrementally to Cosmos DB, ensuring data consistency and minimizing downtime. Offline migrations rely on bulk data export and import operations. The extension manages connection authentication securely, supports various MongoDB versions, and handles data type mappings between MongoDB BSON types and Cosmos DB’s JSON-based storage model.

**Use Cases and Application Scenarios:**  
- Enterprises modernizing legacy MongoDB deployments by moving to a fully managed cloud service.  
- Development teams migrating test or staging databases to Azure Cosmos DB for integration with other Azure services.  
- Organizations seeking to reduce operational overhead and improve global distribution and scalability of their MongoDB workloads.  
- Scenarios requiring minimal downtime migrations for mission-critical applications.

**Important Considerations and Limitations:**  
- As a public preview, the extension may have feature limitations or bugs; production use should be carefully evaluated.  
- Online migration requires MongoDB instances that support change streams (MongoDB 3.6+), and network connectivity must allow the extension to access both source and target databases.  
- Certain MongoDB features or data types may have limited or no support due to underlying differences in Cosmos DB’s API for MongoDB implementation.  
- Performance during migration depends on network bandwidth and data volume; large datasets may require extended migration windows.  
- Users must ensure proper indexing strategies post-migration to optimize query performance.

**Integration with Related Azure Services:**  
The extension integrates tightly with Azure Cosmos DB, leveraging its API for MongoDB compatibility. Post-migration, users can utilize Azure Monitor and Azure Advisor for performance monitoring and optimization. Additionally, migrated data can be combined with other Azure services such as Azure Functions for serverless processing, Azure Synapse Analytics for big data insights, and Azure Logic Apps for workflow automation, enabling comprehensive cloud-native application architectures.

In summary, the Azure DocumentDB Migration extension for Visual Studio Code public preview provides IT professionals with a practical, integrated tool to perform both online and offline migrations of MongoDB workloads to Azure Cosmos DB, facilitating cloud adoption with reduced complexity and downtime while leveraging Azure’s ecosystem for enhanced data management and application development.

---

### 61. Generally Available: Online migration from Azure Cosmos DB for MongoDB RU to Azure DocumentDB

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Online migration from Azure Cosmos DB for MongoDB RU to Azure DocumentDB](https://azure.microsoft.com/updates?id=523716)

**Update ID**: 523716
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB

**Summary**:

- What was updated  
Azure Cosmos DB now supports generally available, seamless, self-serve online migrations from the MongoDB API throughput model (RU/s) to the native Azure DocumentDB API throughput model directly via the Azure portal.

- Key changes or new features  
Developers and IT professionals can perform zero-downtime migrations of their MongoDB workloads within Azure Cosmos DB, simplifying modernization efforts. The migration is fully managed and does not require manual data export/import or application downtime. This enables easier optimization of throughput and cost management by transitioning to the DocumentDB API’s RU model.

- Target audience affected  
This update primarily benefits developers and IT professionals managing MongoDB workloads on Azure Cosmos DB who want to modernize their applications, optimize performance, or reduce operational complexity by switching to the DocumentDB API throughput model.

- Important notes if any  
The migration process is online and self-service via the Azure portal, ensuring minimal disruption. Users should review compatibility and test workloads post-migration to confirm application behavior aligns with DocumentDB API semantics. For detailed guidance, refer to Azure documentation linked in the update.

**Details**:

The recent Azure update announces the general availability of a seamless, self-service online migration capability from Azure Cosmos DB for MongoDB API RU (Request Units) to Azure DocumentDB, directly accessible through the Azure portal. This enhancement enables organizations to modernize MongoDB workloads hosted on Azure Cosmos DB with zero downtime and minimal operational complexity.

**Background and Purpose**  
Azure Cosmos DB supports multiple APIs, including MongoDB and DocumentDB (Core SQL API), allowing developers to use their preferred data models and query languages. However, some organizations require transitioning workloads from the MongoDB API to the DocumentDB API to leverage specific features, optimize performance, or unify their data platform. Previously, such migrations involved complex manual data export/import processes or application-level changes, often causing downtime and operational risk. This update addresses these challenges by providing an integrated, online migration path that simplifies and accelerates the transition while maintaining service availability.

**Specific Features and Detailed Changes**  
- **Self-Serve Migration via Azure Portal:** Users can initiate and monitor the migration process through a guided experience in the Azure portal without needing custom scripts or third-party tools.  
- **Online Migration with Zero Downtime:** The migration runs in the background, synchronizing data continuously to ensure the target DocumentDB API account remains up-to-date, enabling seamless cutover.  
- **Automated Schema and Data Transformation:** The service handles necessary data format conversions and schema adjustments between MongoDB API and DocumentDB API models, abstracting complexity from users.  
- **Progress Monitoring and Reporting:** Built-in telemetry provides visibility into migration status, performance, and potential issues, facilitating operational control.  

**Technical Mechanisms and Implementation Methods**  
The migration leverages Azure Cosmos DB's change feed and transactional replication capabilities to capture ongoing data changes from the source MongoDB API account. It incrementally applies these changes to the target DocumentDB API account, ensuring data consistency and minimizing latency. The migration service manages conflict resolution, data type mappings, and index transformations required to adapt MongoDB-specific constructs to DocumentDB’s JSON document model and indexing strategies. The process is orchestrated within Azure’s control plane, ensuring security and compliance with Azure governance policies.

**Use Cases and Application Scenarios**  
- **API Consolidation:** Organizations standardizing on the DocumentDB API for new features such as advanced querying or integration with Azure Synapse Analytics.  
- **Performance Optimization:** Migrating workloads to leverage DocumentDB’s indexing and query optimizations for specific application patterns.  
- **Application Modernization:** Transitioning legacy MongoDB API applications to a more feature-rich or cost-effective Cosmos DB API without downtime.  
- **Data Platform Unification:** Combining multiple data sources under a single API for simplified management and analytics.  

**Important Considerations and Limitations**  
- **Compatibility:** While the migration automates many transformations, some MongoDB-specific features or data types may require manual validation or adjustment post-migration.  
- **Resource Provisioning:** Both source and target Cosmos DB accounts must be provisioned and sized appropriately to handle migration throughput and workload demands.  
- **Cost Implications:** Running dual accounts during migration incurs additional costs; organizations should plan accordingly.  
- **Migration Scope:** The service currently supports migrating data and schema but does not automatically migrate stored procedures, triggers, or certain MongoDB-specific operational configurations.  
- **Rollback and Recovery:** The migration process includes mechanisms for pausing or aborting but requires careful planning to avoid data inconsistencies.  

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Log Analytics:** For enhanced monitoring, alerting, and diagnostics during migration.  
- **Azure Active Directory (AAD):** Ensures secure authentication and authorization for migration operations.  
- **Azure Resource Manager (ARM):** Facilitates deployment automation and policy enforcement.  
- **Azure Synapse Analytics and Power BI:** Post-migration, the unified DocumentDB API data can be integrated for advanced analytics and reporting.  

In summary, this

---

### 62. Public Preview: Oracle to PostgreSQL migration tooling in Visual Studio Code 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Oracle to PostgreSQL migration tooling in Visual Studio Code ](https://azure.microsoft.com/updates?id=523593)

**Update ID**: 523593
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL extension for Visual Studio Code now includes a public preview of Oracle-to-PostgreSQL migration tooling.

- Key changes or new features  
The new tooling streamlines the migration process by enabling developers to convert Oracle database schemas, objects, and data directly within Visual Studio Code. It automates schema translation and data migration tasks, reducing manual effort and potential errors. Integration within VS Code offers a familiar environment for developers to manage migration workflows efficiently.

- Target audience affected  
Developers and database administrators involved in migrating applications and databases from Oracle to PostgreSQL, particularly those using Azure Database for PostgreSQL and Visual Studio Code as part of their development and migration toolset.

- Important notes if any  
This feature is currently in public preview, so users should expect potential limitations and provide feedback to improve the tooling. It is recommended to test migrations in non-production environments before full-scale adoption. Access and installation require the latest version of the Azure Database for PostgreSQL extension in Visual Studio Code.

**Details**:

The recent Azure update introduces a Public Preview of Oracle-to-PostgreSQL migration tooling integrated within the Azure Database for PostgreSQL extension for Visual Studio Code, aiming to streamline and accelerate database migration projects from Oracle to PostgreSQL environments. This tooling addresses the growing demand for cost-effective, open-source database solutions by simplifying the complex process of migrating Oracle databases, which often involves significant manual effort and expertise.

**Background and Purpose:**  
Enterprises increasingly seek to transition from proprietary Oracle databases to PostgreSQL, an open-source alternative known for lower licensing costs and strong community support. However, Oracle-to-PostgreSQL migration is technically challenging due to differences in SQL dialects, data types, procedural languages, and database features. The update’s purpose is to reduce migration complexity by embedding migration capabilities directly into Visual Studio Code, a widely used development environment, thereby enabling developers and DBAs to perform migration tasks within a familiar interface and toolset.

**Specific Features and Detailed Changes:**  
The new migration tooling offers automated schema conversion, data type mapping, and code translation from Oracle PL/SQL to PostgreSQL PL/pgSQL. It includes:  
- **Schema Conversion:** Automatically converts Oracle database schemas, including tables, indexes, constraints, and sequences, into PostgreSQL-compatible formats.  
- **Code Translation:** Translates stored procedures, functions, and triggers from Oracle PL/SQL to PostgreSQL procedural language, reducing manual rewriting.  
- **Data Migration Assistance:** Facilitates data export/import processes with validation checks to ensure data integrity.  
- **Integration with Azure Database for PostgreSQL:** Allows direct deployment of converted schemas and data into Azure-managed PostgreSQL instances.  
- **Visual Studio Code Integration:** Provides an intuitive UI within VS Code for managing migration projects, running conversion tasks, and troubleshooting issues.

**Technical Mechanisms and Implementation Methods:**  
The tooling leverages a combination of static code analysis and rule-based transformation engines to parse Oracle database objects and convert them into PostgreSQL equivalents. It uses a mapping dictionary for data types and SQL constructs, applying transformation rules to procedural code and DDL scripts. The extension interacts with Azure Database for PostgreSQL via REST APIs and database connectors to automate deployment and data loading. It also supports incremental migration workflows, allowing iterative testing and validation.

**Use Cases and Application Scenarios:**  
- Enterprises planning to reduce licensing costs by migrating from Oracle to PostgreSQL.  
- Development teams modernizing legacy Oracle applications to leverage PostgreSQL’s extensibility and cloud-native features.  
- Database administrators seeking to automate and standardize migration processes within their CI/CD pipelines using Visual Studio Code.  
- Organizations adopting Azure Database for PostgreSQL as part of their cloud migration strategy, benefiting from managed services and scalability.

**Important Considerations and Limitations:**  
- As a Public Preview, the tooling may not cover all Oracle features, especially complex PL/SQL constructs or proprietary Oracle extensions. Manual intervention might be required for advanced stored procedures or specialized data types.  
- Performance tuning and optimization post-migration remain the responsibility of the user, as automated conversion focuses primarily on compatibility rather than optimization.  
- Users should conduct thorough testing in non-production environments to validate functional equivalence and data integrity.  
- The tooling currently supports Azure Database for PostgreSQL and may not fully support on-premises PostgreSQL or other cloud providers.

**Integration with Related Azure Services:**  
This migration tooling complements Azure Database Migration Service (DMS) by focusing on schema and code conversion within the developer environment, while DMS handles large-scale data migration and cutover orchestration. It integrates seamlessly with Azure Database for PostgreSQL, enabling direct deployment and management of migrated databases. Additionally, it can be combined with Azure DevOps pipelines for automated migration workflows and continuous integration.

In summary, the Oracle-to-PostgreSQL migration tooling in Visual Studio Code offers IT professionals a practical, integrated solution to simplify database migration projects by automating schema and code conversion, facilitating data migration, and enabling direct deployment to Azure Database for

---

### 63. Generally Available: 2025 REST API for Azure Database for PostgreSQL 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: 2025 REST API for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=523588)

**Update ID**: 523588
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL’s REST API has reached general availability with the release of the 2025 version.

- Key changes or new features  
The 2025 REST API now supports PostgreSQL versions 17 and 18, enabling developers and IT professionals to upgrade to the latest PostgreSQL releases seamlessly without modifying existing automation workflows. Additionally, users can set the default database during resource provisioning, improving deployment flexibility and configuration control.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL instances, especially those automating deployments, upgrades, and configuration through REST APIs.

- Important notes if any  
This update ensures backward-compatible automation while adopting new PostgreSQL versions, reducing operational overhead. Users should review API changes to leverage default database settings and confirm compatibility with their automation scripts. For detailed documentation and migration guidance, refer to the official Azure update link.

**Details**:

The recent general availability of the 2025 REST API for Azure Database for PostgreSQL introduces enhanced management capabilities aligned with the latest PostgreSQL versions, enabling IT professionals to streamline automation and maintain up-to-date database environments efficiently.

**Background and Purpose of the Update**  
Azure Database for PostgreSQL is a managed database service that supports multiple PostgreSQL versions, providing scalability, high availability, and security. As PostgreSQL evolves, Azure must support new versions to allow customers to leverage the latest features, performance improvements, and security patches. The 2025 REST API update addresses this need by incorporating support for PostgreSQL 17 and 18, ensuring that automation workflows and infrastructure-as-code (IaC) solutions remain compatible without requiring significant changes. This update reflects Azure’s commitment to keeping its managed database offerings current and developer-friendly.

**Specific Features and Detailed Changes**  
- **Support for PostgreSQL 17 and 18:** The API now allows provisioning, configuring, and managing PostgreSQL instances running these latest major versions.  
- **Default Database Configuration:** Users can set the default database during server creation or update operations via the REST API, simplifying initial setup and reducing post-deployment configuration steps.  
- **Backward Compatibility:** The API maintains compatibility with existing automation scripts and tools, minimizing disruption during version upgrades.  
- **Enhanced API Endpoints:** New or updated REST endpoints provide granular control over server parameters, firewall rules, and performance configurations tailored to the new PostgreSQL versions.

**Technical Mechanisms and Implementation Methods**  
The 2025 REST API is built on Azure’s consistent API framework, utilizing HTTPS endpoints secured with Azure Active Directory (AAD) tokens or service principals for authentication. It supports standard HTTP methods (GET, POST, PUT, PATCH, DELETE) to perform CRUD operations on PostgreSQL server resources. The API schema has been extended to include version-specific parameters and validation rules corresponding to PostgreSQL 17 and 18 features. Internally, the API integrates with Azure Resource Manager (ARM), enabling declarative resource management and seamless integration with Azure Policy and Role-Based Access Control (RBAC).

**Use Cases and Application Scenarios**  
- **Automated Deployment Pipelines:** DevOps teams can incorporate the new API into CI/CD pipelines to provision PostgreSQL 17/18 servers automatically, ensuring environments are consistent and up-to-date.  
- **Infrastructure as Code (IaC):** Tools like Terraform, Azure CLI, and ARM templates can leverage the updated API to manage PostgreSQL instances programmatically.  
- **Version Upgrades:** Database administrators can script version upgrades and configuration changes without manual intervention, reducing downtime and human error.  
- **Multi-Region Deployments:** Enterprises deploying globally can automate server creation with the latest PostgreSQL versions across regions, maintaining compliance and performance standards.

**Important Considerations and Limitations**  
- **Version-Specific Features:** While the API supports PostgreSQL 17 and 18, some new database features may require additional configuration beyond the API’s scope or client-side adjustments.  
- **Compatibility Testing:** Before upgrading production workloads, thorough testing is recommended to validate application compatibility with the new PostgreSQL versions.  
- **API Rate Limits:** As with all Azure REST APIs, users should be mindful of throttling limits and implement retry logic in automation scripts.  
- **Regional Availability:** Support for PostgreSQL 17 and 18 may initially be limited to specific Azure regions; verify availability in your target deployment area.  
- **Security Practices:** Ensure that API authentication credentials are securely managed, and leverage Azure RBAC to restrict access appropriately.

**Integration with Related Azure Services**  
- **Azure Monitor:** Enhanced monitoring and alerting can be configured for PostgreSQL 17/18 instances using Azure Monitor, enabling proactive performance management.  
- **Azure Security Center:** Security assessments and recommendations extend to the new PostgreSQL versions, helping maintain compliance.  
- **Azure Backup:** Integration with Azure Backup ensures that databases running on PostgreSQL 17

---

### 64. Generally Available: Elastic clusters on Azure Database for PostgreSQL – Flexible Server 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Elastic clusters on Azure Database for PostgreSQL – Flexible Server ](https://azure.microsoft.com/updates?id=523583)

**Update ID**: 523583
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now generally supports elastic clusters.

- Key changes or new features  
Elastic clusters enable horizontal scaling of PostgreSQL databases via row-based and schema-based sharding. This feature simplifies building multitenant applications by automating shard management and operational tasks such as tenant isolation, scaling, and maintenance. Developers can distribute workloads efficiently across multiple servers, improving performance and scalability without manual shard handling.

- Target audience affected  
Developers building scalable, multitenant applications on PostgreSQL and IT professionals managing database infrastructure who require seamless horizontal scaling and simplified shard management.

- Important notes if any  
Elastic clusters are now generally available, indicating production readiness. Users should evaluate their application architecture to leverage sharding strategies effectively. This update enhances flexibility and operational efficiency for PostgreSQL workloads on Azure. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The recent general availability of Elastic Clusters on Azure Database for PostgreSQL – Flexible Server introduces a robust horizontal scaling solution through row-based and schema-based sharding, designed to simplify the development and management of multitenant applications. This update addresses the growing need for scalable, high-performance PostgreSQL deployments that can efficiently handle large datasets and tenant isolation without complex manual shard management.

**Background and Purpose**  
As cloud-native applications grow in scale and complexity, traditional vertical scaling of databases often becomes a bottleneck. Multitenant applications, in particular, require efficient data partitioning to isolate tenant workloads and maintain performance. Prior to this update, implementing sharding in PostgreSQL on Azure required significant manual effort and custom orchestration. The Elastic Clusters feature was introduced to automate shard management, enabling seamless horizontal scaling and operational simplicity.

**Specific Features and Detailed Changes**  
Elastic Clusters enable users to partition their PostgreSQL databases either by rows or schemas, distributing data across multiple Flexible Server instances. Key features include:

- **Row-based sharding:** Data is partitioned by rows, typically based on tenant or customer identifiers, allowing fine-grained distribution.
- **Schema-based sharding:** Each shard corresponds to a separate schema, facilitating logical separation and easier management.
- **Automated shard management:** Azure handles shard creation, balancing, and failover, reducing operational overhead.
- **Tenant isolation:** Each tenant’s data resides in separate shards, improving security and performance isolation.
- **Elastic scaling:** Clusters can dynamically add or remove shards based on workload demands.

**Technical Mechanisms and Implementation Methods**  
Elastic Clusters leverage PostgreSQL’s native capabilities combined with Azure’s orchestration layer. The Flexible Server deployment model provides the underlying compute and storage resources, while the Elastic Clusters framework manages:

- **Shard catalog:** A centralized metadata store tracks shard locations and mappings.
- **Routing layer:** Queries are transparently routed to the appropriate shard based on the sharding key.
- **Shard lifecycle management:** Automated provisioning, scaling, and failover of shards ensure high availability.
- **Data distribution:** Supports both hash and range partitioning strategies depending on the sharding method chosen.

Users interact with the cluster through standard PostgreSQL interfaces, with minimal changes to application logic, primarily involving the inclusion of sharding keys in queries.

**Use Cases and Application Scenarios**  
Elastic Clusters are ideal for:

- **Multitenant SaaS applications:** Efficiently isolate tenant data while maintaining a unified management plane.
- **Large-scale OLTP workloads:** Distribute high-volume transactional data to avoid bottlenecks.
- **Data warehousing and analytics:** Partition large datasets for parallel processing.
- **Geographically distributed applications:** Place shards closer to regional users to reduce latency.

**Important Considerations and Limitations**  
- **Application changes:** While routing is automated, applications must be designed to include sharding keys and handle potential cross-shard queries carefully.
- **Cross-shard transactions:** Distributed transactions across shards have limitations and may require additional design considerations.
- **Consistency model:** Elastic Clusters maintain strong consistency within shards but eventual consistency may apply across shards.
- **Monitoring and troubleshooting:** Requires familiarity with shard-level metrics and Azure monitoring tools.
- **Cost implications:** Running multiple Flexible Server instances increases resource consumption and costs.

**Integration with Related Azure Services**  
Elastic Clusters integrate seamlessly with:

- **Azure Monitor and Azure Log Analytics:** For monitoring shard health, performance, and alerts.
- **Azure Active Directory:** Enables secure authentication and role-based access control across shards.
- **Azure Backup and Azure Site Recovery:** Support for data protection and disaster recovery at the cluster level.
- **Azure Data Factory and Synapse Analytics:** Facilitate ETL and analytics workflows on sharded data.
- **Azure Private Link and Virtual Network:** Ensure secure, private connectivity to cluster resources.

In summary, the GA release of Elastic Clusters on Azure Database for PostgreSQL – Flexible Server provides a powerful, automated

---

### 65. Public Preview: Native Microsoft Foundry support for Azure Database for PostgreSQL

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Native Microsoft Foundry support for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=523578)

**Update ID**: 523578
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Microsoft announced the public preview of native Microsoft Foundry support for Azure Database for PostgreSQL. The Azure PostgreSQL MCP Server is now integrated directly with Microsoft Foundry.

- Key changes or new features  
This integration allows developers to build AI agents that can securely query and analyze data within Azure Database for PostgreSQL using Microsoft Foundry’s capabilities. It streamlines the creation of intelligent applications by enabling seamless, secure data access and AI-driven insights without complex custom connectors or middleware.

- Target audience affected  
Developers and IT professionals working with Azure Database for PostgreSQL who want to leverage AI-driven data analysis and build intelligent agents. Data engineers and AI solution architects will also benefit from simplified integration and enhanced security.

- Important notes if any  
This feature is currently in public preview, so users should expect potential changes and provide feedback. Security and compliance remain a priority, with native integration designed to maintain data protection standards. Users should review preview limitations and monitor Azure updates for GA announcements.

**Details**:

The recent public preview announcement of native Microsoft Foundry support for Azure Database for PostgreSQL marks a significant enhancement in integrating AI-driven data analysis capabilities directly within Azure’s managed PostgreSQL environment. This update introduces the Azure PostgreSQL MCP (Microsoft Cognitive Platform) Server’s native integration with Microsoft Foundry, enabling developers and data professionals to build AI agents that can securely query and analyze PostgreSQL data using advanced cognitive services.

**Background and Purpose**  
Azure Database for PostgreSQL is a fully managed relational database service that supports open-source PostgreSQL workloads. Microsoft Foundry is a platform designed to facilitate the development of AI agents and cognitive applications by providing tools for natural language processing, data querying, and reasoning. Prior to this update, leveraging AI capabilities with Azure Database for PostgreSQL required custom integration or external data pipelines. The purpose of this update is to streamline and secure the process of applying AI-driven queries and analytics directly on PostgreSQL data, reducing complexity and improving efficiency.

**Specific Features and Detailed Changes**  
- **Native Integration:** The Azure PostgreSQL MCP Server is now embedded within Microsoft Foundry, allowing seamless connectivity without additional middleware.  
- **AI Agent Development:** Developers can create AI agents that interact with PostgreSQL data using natural language queries or programmatic interfaces, leveraging Foundry’s cognitive models.  
- **Secure Querying:** The integration ensures secure data access, adhering to Azure’s security standards, including role-based access control (RBAC), encryption in transit and at rest, and compliance certifications.  
- **Real-time Analytics:** Enables near real-time AI-driven insights by directly querying live PostgreSQL databases, eliminating the need for data extraction or replication.

**Technical Mechanisms and Implementation Methods**  
The integration is implemented by embedding the MCP Server within the Foundry environment, which acts as an intermediary cognitive layer. This layer translates natural language or AI-driven queries into optimized SQL commands executed against the Azure Database for PostgreSQL instance. The system uses secure API endpoints and OAuth 2.0-based authentication to ensure that only authorized AI agents can access the data. Additionally, the MCP Server leverages PostgreSQL’s native extensibility and performance features, such as prepared statements and indexing, to optimize query execution. The cognitive models within Foundry are built on Azure’s AI infrastructure, supporting continuous learning and adaptation based on query patterns.

**Use Cases and Application Scenarios**  
- **Business Intelligence:** Analysts can use AI agents to generate complex reports and insights from PostgreSQL data without writing SQL, accelerating decision-making.  
- **Automated Customer Support:** AI agents can query customer data stored in PostgreSQL to provide personalized responses or recommendations.  
- **Operational Monitoring:** Real-time anomaly detection and predictive maintenance can be implemented by querying operational data with AI models.  
- **Data Exploration:** Data scientists can interactively explore datasets using natural language, speeding up hypothesis generation and validation.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview, the feature may have limited SLA guarantees and could undergo changes before general availability.  
- **Performance Impact:** While optimized, AI-driven queries may introduce additional latency compared to direct SQL queries, especially for complex cognitive tasks.  
- **Security Configuration:** Proper configuration of RBAC and network security groups is essential to prevent unauthorized data access.  
- **Data Volume and Complexity:** Extremely large datasets or highly complex queries may require tuning or additional scaling of the PostgreSQL instance.

**Integration with Related Azure Services**  
This update complements other Azure services such as Azure Cognitive Services, Azure Machine Learning, and Azure Synapse Analytics by providing a direct AI interface to PostgreSQL data. It can be combined with Azure Active Directory for identity management and Azure Key Vault for secure credential storage. Additionally, integration with Azure Monitor and Azure Security Center can help track usage and enforce compliance.

In summary, the native Microsoft Foundry support for Azure Database for PostgreSQL in public preview enables IT professionals to build secure, AI-powered agents that interact directly with PostgreSQL

---

### 66. Generally Available: Azure Database for PostgreSQL – Flexible Server anon extension 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL – Flexible Server anon extension ](https://azure.microsoft.com/updates?id=523569)

**Update ID**: 523569
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now generally supports the anon extension.

- Key changes or new features  
The anon extension provides built-in data anonymization capabilities directly within PostgreSQL. It enables developers and DBAs to anonymize sensitive data in tables using various anonymization functions, helping to protect privacy and comply with data protection regulations. This extension simplifies implementing data masking and anonymization workflows without external tools.

- Target audience affected  
Developers, database administrators, and IT professionals managing PostgreSQL workloads on Azure Flexible Server who require data anonymization for compliance, testing, or analytics scenarios.

- Important notes if any  
The anon extension is now fully supported and can be enabled on existing Flexible Server instances. Users should review the extension’s documentation to understand available anonymization functions and best practices. This update helps organizations enhance data privacy directly at the database layer, reducing the need for additional data processing pipelines.  

Learn more: https://azure.microsoft.com/updates?id=523569

**Details**:

The Azure Database for PostgreSQL – Flexible Server anon extension has reached general availability, introducing built-in data anonymization capabilities directly within the managed PostgreSQL environment. This update addresses growing data privacy and compliance requirements by enabling organizations to anonymize sensitive data at the database level without complex external tooling.

**Background and Purpose:**  
With increasing regulatory mandates such as GDPR, HIPAA, and CCPA, organizations must protect personally identifiable information (PII) and sensitive data within their databases. Traditional approaches often rely on application-layer anonymization or external ETL processes, which can be error-prone, inefficient, and difficult to maintain. The anon extension aims to simplify and standardize data anonymization by embedding it natively into Azure Database for PostgreSQL Flexible Server, thereby reducing operational complexity and improving security posture.

**Specific Features and Detailed Changes:**  
The anon extension provides a rich set of anonymization functions that can be applied to database columns containing sensitive information. These functions include pseudonymization, data masking, randomization, and tokenization techniques, allowing customizable anonymization strategies tailored to different data types and compliance needs. The extension supports anonymizing data in-place or during query execution, enabling dynamic anonymization without altering the underlying data permanently if desired. It integrates seamlessly with PostgreSQL’s native extension framework and can be enabled on Flexible Server instances via standard extension management commands.

**Technical Mechanisms and Implementation Methods:**  
Technically, the anon extension operates as a PostgreSQL extension written in C, leveraging PostgreSQL’s extensibility features such as user-defined functions (UDFs) and procedural languages. It exposes anonymization functions callable within SQL queries, stored procedures, or triggers. For example, administrators can define policies that automatically anonymize data upon insert/update or create views that present anonymized data to specific user roles. The extension supports configuration parameters to control anonymization behavior, such as seed values for deterministic pseudonymization or rules for conditional anonymization. Deployment involves enabling the extension on the Flexible Server instance and granting appropriate permissions to users or roles that will execute anonymization functions.

**Use Cases and Application Scenarios:**  
Common use cases include anonymizing customer PII in development and testing environments to prevent exposure of real data, masking sensitive fields in analytics workloads, and complying with data privacy regulations by ensuring that exported or shared datasets do not contain identifiable information. Organizations can implement role-based access controls combined with the anon extension to provide different data views depending on user privileges, supporting secure data sharing and collaboration. Additionally, the extension facilitates data anonymization in data migration or archival scenarios, where sensitive data must be protected before transfer or long-term storage.

**Important Considerations and Limitations:**  
While the anon extension enhances data privacy capabilities, it requires careful planning to avoid unintended data loss or compliance gaps. Anonymization is irreversible in many cases, so backups and data retention policies should be reviewed before applying anonymization functions. Performance impact should be evaluated, especially for large datasets or complex anonymization rules, as additional processing overhead may occur during query execution. The extension currently supports Flexible Server deployment but may have limitations in Hyperscale or Single Server tiers. It is also essential to keep the extension updated to benefit from security patches and feature improvements.

**Integration with Related Azure Services:**  
The anon extension complements Azure’s broader data governance and security ecosystem. It can be integrated with Azure Active Directory for role-based access control, Azure Monitor for auditing anonymization operations, and Azure Policy to enforce compliance standards across database resources. When combined with Azure Data Factory or Azure Synapse Analytics, anonymized data can be securely ingested and analyzed without exposing sensitive information. Additionally, integration with Azure Key Vault can enhance security by managing cryptographic keys used in tokenization or pseudonymization processes.

In summary, the general availability of the anon extension in Azure Database for PostgreSQL Flexible Server provides IT professionals with a powerful, native toolset for implementing robust data anonymization strategies, facilitating compliance with privacy regulations while maintaining operational efficiency and security within Azure

---

### 67. Public Preview: Azure Database for PostgreSQL – Flexible Server v6 series VMs and AMD v6 Confidential Compute

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Database for PostgreSQL – Flexible Server v6 series VMs and AMD v6 Confidential Compute](https://azure.microsoft.com/updates?id=523564)

**Update ID**: 523564
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports deployment on v6-series Azure Virtual Machines, including general purpose and memory-optimized SKUs with local NVMe storage. Additionally, AMD v6 Confidential Compute VM options are introduced in public preview.

- Key changes or new features  
• Introduction of v6-series VMs featuring local NVMe storage, improving I/O performance for PostgreSQL workloads.  
• Availability of both Intel and AMD processor options, allowing customers to choose based on workload requirements and cost considerations.  
• AMD v6 Confidential Compute VMs provide enhanced data protection by enabling confidential computing capabilities, isolating data in hardware-based trusted execution environments.

- Target audience affected  
Developers and IT professionals managing PostgreSQL workloads on Azure Flexible Server who require improved performance, security, and processor choice. This includes those running general purpose or memory-intensive database applications and those with sensitive data needing confidential computing.

- Important notes if any  
• The v6-series VMs and AMD confidential compute options are currently in public preview, so users should evaluate in non-production environments first.  
• Local NVMe storage is ephemeral and intended for temporary data or caching; persistent data should remain on managed disks.  
• Review pricing and regional availability before deployment.  
• Refer to official documentation for configuration details and limitations.

**Details**:

The recent public preview update for Azure Database for PostgreSQL Flexible Server introduces support for the v6-series Azure Virtual Machines (VMs), including both general purpose and memory-optimized SKUs, featuring local NVMe storage and options for Intel or AMD processors, as well as AMD v6 Confidential Compute capabilities. This enhancement aims to provide customers with improved performance, flexibility, and security for PostgreSQL workloads by leveraging the latest generation of Azure infrastructure.

**Background and Purpose**  
Azure Database for PostgreSQL Flexible Server is a managed database service designed to offer greater control and customizability compared to single-server deployments, targeting mission-critical and scalable PostgreSQL applications. The introduction of v6-series VMs addresses the need for higher compute power, faster local storage, and confidential computing to meet evolving enterprise requirements for performance, data protection, and compliance.

**Specific Features and Detailed Changes**  
- **v6-Series VM Support:** The update enables deployment of Flexible Server instances on v6-series VMs, which are the latest generation of Azure VMs optimized for general purpose and memory-intensive workloads. These VMs come with enhanced CPU architectures and faster memory bandwidth.  
- **Local NVMe Storage:** Unlike previous generations that relied primarily on remote storage, v6-series VMs include local NVMe SSDs, significantly reducing I/O latency and improving throughput for database operations. This local storage is ephemeral but ideal for caching and temporary data, accelerating PostgreSQL performance.  
- **Processor Options:** Customers can choose between Intel and AMD processors for v6-series VMs, allowing workload-specific optimization. AMD v6 Confidential Compute VMs provide hardware-based memory encryption using AMD SEV-SNP technology, enhancing data confidentiality during processing.  
- **Confidential Compute:** The AMD v6 Confidential Compute option integrates secure enclaves that protect data in use, mitigating risks from privileged malware or insider threats, which is critical for sensitive workloads requiring compliance with stringent security standards.

**Technical Mechanisms and Implementation Methods**  
Flexible Server instances on v6-series VMs utilize Azure’s underlying infrastructure enhancements, including the Nitro Hypervisor for AMD processors and Intel’s latest CPU microarchitectures. Local NVMe storage is mounted directly on the VM, reducing network hops and latency. Confidential Compute leverages AMD SEV-SNP firmware and hardware extensions to isolate memory pages, ensuring that even the host OS or hypervisor cannot access protected memory regions. Deployment is managed through the Azure portal, CLI, or ARM templates, with options to select VM series, processor type, and confidential compute features during server creation or scaling operations.

**Use Cases and Application Scenarios**  
- **High-Performance OLTP and Analytics:** Workloads requiring low latency and high IOPS benefit from local NVMe storage and faster CPUs.  
- **Security-Sensitive Applications:** Financial, healthcare, or government applications that must protect data in use can leverage AMD v6 Confidential Compute for enhanced security.  
- **Cost-Effective Scaling:** The choice between Intel and AMD processors allows cost-performance optimization tailored to workload characteristics.  
- **Development and Testing:** Flexible Server’s customizable VM options enable realistic performance testing on latest hardware.

**Important Considerations and Limitations**  
- **Ephemeral Storage:** Local NVMe storage is temporary and data is lost if the VM is deallocated or fails; thus, it should not be used for persistent data storage but rather for caching or temporary files.  
- **Preview Status:** As this is a public preview, features may have limitations or changes before general availability; production workloads should be tested thoroughly.  
- **Region Availability:** v6-series VMs and confidential compute options may be limited to specific Azure regions initially.  
- **Cost Implications:** New VM series and confidential compute options may incur different pricing; careful cost analysis is recommended.

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Advisor:** Monitoring and optimization tools support v6-series VMs to provide insights into performance and cost.  
- **Azure Security

---

### 68. Public Preview: Azure Database for PostgreSQL – Flexible Server pg_duckdb extension 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure Database for PostgreSQL – Flexible Server pg_duckdb extension ](https://azure.microsoft.com/updates?id=523559)

**Update ID**: 523559
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports the pg_duckdb extension in public preview.

- Key changes or new features  
Developers can create and use the pg_duckdb extension within Flexible Server instances, enabling accelerated analytics by leveraging DuckDB’s vectorized, columnar execution engine. This integration enhances query performance for analytical workloads directly inside PostgreSQL without external data movement.

- Target audience affected  
Developers and data engineers working with PostgreSQL on Azure who require advanced, high-performance analytical processing. IT professionals managing PostgreSQL Flexible Server deployments will also benefit from the new extension’s capabilities.

- Important notes if any  
The feature is currently in public preview, so it may have limitations and is not recommended for production workloads yet. Users should test and validate the extension in their environments. For detailed usage and setup instructions, refer to the official Azure documentation.

**Details**:

The recent public preview announcement for Azure Database for PostgreSQL – Flexible Server introduces support for the pg_duckdb extension, enabling users to leverage DuckDB’s vectorized, columnar execution engine directly within their PostgreSQL environment. This update aims to enhance in-database analytics performance by integrating DuckDB’s efficient analytical processing capabilities into Azure’s managed PostgreSQL service.

**Background and Purpose**  
Azure Database for PostgreSQL – Flexible Server is a managed database service designed for high availability, scalability, and operational flexibility. Traditionally, PostgreSQL’s row-oriented storage and execution model can limit performance for complex analytical queries, especially on large datasets. DuckDB is an embeddable analytical database engine optimized for OLAP workloads, featuring vectorized execution and columnar storage that significantly accelerates analytical query processing. By enabling the pg_duckdb extension, Azure aims to combine PostgreSQL’s transactional strengths with DuckDB’s analytical efficiency, providing a unified platform for hybrid transactional and analytical processing (HTAP) scenarios.

**Specific Features and Detailed Changes**  
- **pg_duckdb Extension Availability:** Users can now create and enable the pg_duckdb extension within their Flexible Server instances.  
- **Vectorized, Columnar Execution:** Queries that utilize the extension benefit from DuckDB’s vectorized processing, which processes data in batches (vectors) rather than row-by-row, improving CPU cache utilization and reducing instruction overhead.  
- **In-Database Analytics:** Enables running complex analytical queries natively inside PostgreSQL without exporting data to external analytical engines.  
- **Seamless Integration:** The extension operates as a PostgreSQL extension, allowing users to invoke DuckDB’s capabilities through familiar SQL interfaces.

**Technical Mechanisms and Implementation Methods**  
The pg_duckdb extension embeds DuckDB’s engine within the PostgreSQL process space, allowing it to execute analytical queries using DuckDB’s optimized execution paths. When enabled, users can create DuckDB-specific objects and run queries that leverage DuckDB’s columnar storage and vectorized execution. The extension translates SQL queries into DuckDB’s internal query plan, executing them efficiently and returning results within the PostgreSQL session. This approach avoids data movement overhead and leverages Flexible Server’s managed infrastructure, including automated backups, scaling, and security.

**Use Cases and Application Scenarios**  
- **Accelerated Analytics:** Data analysts and engineers can run complex aggregations, window functions, and OLAP queries faster without moving data out of PostgreSQL.  
- **Hybrid Workloads:** Applications requiring both transactional and analytical capabilities benefit from reduced latency and simplified architecture.  
- **Data Science and BI:** Enables integration with BI tools and data science workflows that rely on fast analytical query responses.  
- **Cost Optimization:** Reduces the need for separate analytical databases or data warehouses, consolidating workloads within a single managed service.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, pg_duckdb may have limited SLA guarantees and could undergo changes before general availability.  
- **Compatibility:** Not all PostgreSQL extensions or features may be fully compatible with pg_duckdb; testing is recommended.  
- **Resource Utilization:** Vectorized execution can increase CPU and memory usage; monitoring and appropriate scaling of Flexible Server instances are advised.  
- **Query Scope:** The extension is optimized for analytical queries and may not improve, or could degrade, performance for transactional workloads.

**Integration with Related Azure Services**  
- **Azure Data Factory:** Can orchestrate data pipelines feeding PostgreSQL Flexible Server, enabling end-to-end analytics workflows enhanced by pg_duckdb.  
- **Azure Synapse Analytics:** While Synapse remains a dedicated analytics platform, pg_duckdb allows preliminary analytics within PostgreSQL before data movement.  
- **Azure Monitor and Azure Advisor:** Support monitoring and optimization of Flexible Server resources to ensure efficient use of the extension.  
- **Power BI:** Can connect directly to PostgreSQL Flexible Server, benefiting from accelerated query performance

---

### 69. Public Preview: Azure SQL change event streaming 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure SQL change event streaming ](https://azure.microsoft.com/updates?id=523533)

**Update ID**: 523533
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database

**Summary**:

- What was updated  
Azure SQL Database now supports public preview of Change Event Streaming (CES), enabling near real-time streaming of data changes directly into Azure Event Hubs.

- Key changes or new features  
CES allows developers and IT professionals to capture and stream insert, update, and delete events from Azure SQL Database tables as event streams. This facilitates seamless integration with event-driven architectures, real-time analytics, and downstream processing systems without complex ETL pipelines. The feature simplifies building reactive applications and data pipelines by providing native change data capture with direct Event Hubs integration.

- Target audience affected  
Developers building event-driven or real-time analytics applications, data engineers managing data integration pipelines, and IT professionals responsible for database and event infrastructure.

- Important notes if any  
This capability is currently in public preview, so it should not be used in production environments without caution. Users need to enable CES on their Azure SQL Database and configure Event Hubs as the event sink. Monitoring and scaling considerations apply as with any event streaming solution. For full details and setup instructions, refer to the official Azure update documentation.

**Details**:

The recent public preview of Azure SQL change event streaming (CES) introduces the capability to stream data changes from Azure SQL Database directly into Azure Event Hubs in near real-time, enabling IT professionals to build more responsive, event-driven data architectures and simplify data integration workflows.

**Background and Purpose:**  
Traditionally, capturing and propagating data changes from Azure SQL Database to downstream systems required complex ETL pipelines, change data capture (CDC) setups, or polling mechanisms, often with latency and operational overhead. The CES feature addresses these challenges by providing a native, streamlined method to emit change events as they occur, facilitating real-time analytics, event-driven processing, and integration with modern data platforms without the need for custom change tracking or external tools.

**Specific Features and Detailed Changes:**  
- **Near Real-Time Change Streaming:** Azure SQL Database now supports emitting change events (inserts, updates, deletes) as they happen, with minimal latency.  
- **Direct Integration with Azure Event Hubs:** Change events are published directly to Event Hubs, a highly scalable event ingestion service, enabling downstream consumers to subscribe and process these events efficiently.  
- **Schema and Metadata Included:** Events include detailed information about the changed data, including before and after states where applicable, and metadata such as transaction timestamps and operation types.  
- **Public Preview Availability:** This feature is currently in public preview, allowing users to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods:**  
CES leverages the underlying transaction log of Azure SQL Database to capture data modifications without impacting database performance significantly. When enabled on a database, the system continuously reads change data and formats it into event messages. These messages are then pushed to a configured Azure Event Hub namespace and event hub instance. IT professionals configure CES via Azure portal, PowerShell, CLI, or ARM templates, specifying which tables to track and the target Event Hub. Consumers can then use Event Hubs SDKs or Azure Stream Analytics to process the event stream.

**Use Cases and Application Scenarios:**  
- **Real-Time Analytics:** Stream transactional changes into analytics platforms or data lakes for near real-time insights.  
- **Event-Driven Architectures:** Trigger workflows, microservices, or serverless functions (e.g., Azure Functions) based on data changes.  
- **Data Replication and Synchronization:** Keep multiple systems or databases synchronized by consuming change events.  
- **Audit and Compliance:** Maintain detailed change logs and audit trails by capturing all data modifications.  
- **Hybrid and Multi-Cloud Integration:** Use Event Hubs as a central event bus to integrate Azure SQL data changes with external systems or cloud providers.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview, CES may have limitations in SLA, feature completeness, and support; it is recommended to test thoroughly before production use.  
- **Supported Data Types and Tables:** Certain data types or table configurations may not be supported; users should verify compatibility.  
- **Event Ordering and Delivery Guarantees:** While Event Hubs provides at-least-once delivery, consumers must handle potential duplicates and ordering considerations.  
- **Cost Implications:** Streaming large volumes of change events to Event Hubs incurs costs related to both Azure SQL Database and Event Hubs usage.  
- **Security and Access Controls:** Proper RBAC and network security configurations are necessary to secure data in transit and at rest.

**Integration with Related Azure Services:**  
- **Azure Event Hubs:** Acts as the ingestion point for change events, enabling scalable event streaming.  
- **Azure Stream Analytics:** Can process and analyze change events in real time, enabling filtering, aggregation, and routing.  
- **Azure Functions and Logic Apps:** Facilitate event-driven automation and workflows triggered by data changes.  
- **Azure Data Explorer and Synapse Analytics:** Can consume change streams for advanced analytics and reporting.  
- **Azure Monitor and Security Center:** Can be used to monitor the

---

### 70. Generally Available: PostgreSQL 18 with in-place upgrade on Azure Database for PostgreSQL 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: PostgreSQL 18 with in-place upgrade on Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=523196)

**Update ID**: 523196
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL now supports PostgreSQL version 18, which is generally available.

- Key changes or new features  
This update introduces the latest PostgreSQL 18 features and improvements, enhancing performance, security, and functionality. A significant addition is the seamless in-place upgrade capability, enabling users to upgrade from earlier PostgreSQL versions to 18 without changing the server endpoint or requiring complex migration steps.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure who want to leverage the newest PostgreSQL features while minimizing downtime and operational complexity during upgrades.

- Important notes if any  
The in-place upgrade simplifies version transitions but users should still review compatibility and test workloads before upgrading in production environments. This feature helps maintain connection strings and configurations unchanged, reducing application impact. For detailed upgrade guidance and feature specifics, refer to the official Azure update documentation.

**Details**:

The recent general availability of PostgreSQL 18 on Azure Database for PostgreSQL marks a significant enhancement in managed relational database services by integrating the latest PostgreSQL features with seamless operational improvements. This update enables IT professionals to upgrade their PostgreSQL instances in-place, preserving server endpoints and minimizing downtime, thereby streamlining database modernization efforts on Azure.

**Background and Purpose**  
PostgreSQL, an advanced open-source relational database, continuously evolves with new features, performance optimizations, and security enhancements. Azure Database for PostgreSQL, as a fully managed service, aims to provide customers with the latest PostgreSQL capabilities while ensuring high availability, security, and operational simplicity. Prior to this update, upgrading major PostgreSQL versions often required complex migration steps or creating new instances, which could lead to endpoint changes and application disruptions. The introduction of PostgreSQL 18 support with in-place upgrade capability addresses these challenges by allowing customers to adopt the newest PostgreSQL version more efficiently and with minimal operational impact.

**Specific Features and Detailed Changes**  
- **PostgreSQL 18 Support:** Azure now supports PostgreSQL 18, incorporating its latest features such as enhanced query parallelism, improved JSON and JSONB functionalities, and additional SQL-standard compliance improvements.  
- **In-Place Upgrade:** Customers can upgrade their existing PostgreSQL servers from earlier supported versions (e.g., PostgreSQL 14 or 15) directly to PostgreSQL 18 without provisioning new servers or changing connection strings. This upgrade preserves the server endpoint, firewall rules, and configuration settings.  
- **Minimal Downtime Upgrade Process:** The in-place upgrade process is designed to minimize downtime by orchestrating the upgrade internally within the managed service, handling data format changes and catalog updates transparently.  
- **Backward Compatibility and Extension Support:** The upgrade process ensures compatibility with commonly used PostgreSQL extensions and extensions supported by Azure Database for PostgreSQL, reducing the risk of post-upgrade issues.

**Technical Mechanisms and Implementation Methods**  
The in-place upgrade leverages Azure’s managed service orchestration capabilities to perform a controlled upgrade of the PostgreSQL engine binaries and system catalogs. This involves:  
- Temporarily pausing client connections during the upgrade window to ensure data consistency.  
- Executing PostgreSQL’s internal upgrade utilities (such as `pg_upgrade` or equivalent mechanisms adapted for the managed environment) to migrate system catalogs and data files to the new version format.  
- Validating extension compatibility and applying necessary adjustments.  
- Resuming service with the same server endpoint and configuration, ensuring seamless client connectivity post-upgrade.

**Use Cases and Application Scenarios**  
- Enterprises requiring the latest PostgreSQL features for improved application performance or new SQL capabilities without the overhead of migration.  
- SaaS providers and developers who need to maintain continuous service availability while upgrading database engines.  
- Organizations aiming to standardize on PostgreSQL 18 for compliance, security patches, or feature parity across development, staging, and production environments.  
- Scenarios where endpoint stability is critical, such as applications with hardcoded connection strings or complex network configurations.

**Important Considerations and Limitations**  
- The in-place upgrade is supported only for specific source versions; customers should verify compatibility before initiating the upgrade.  
- Some extensions or custom configurations may require manual intervention or validation post-upgrade.  
- Although downtime is minimized, a brief service interruption is expected during the upgrade window, so scheduling during low-traffic periods is advisable.  
- Backup and restore strategies should be employed prior to upgrade to safeguard against unforeseen issues.  
- Certain deprecated features or behaviors in PostgreSQL 18 may affect legacy applications, necessitating thorough testing.

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Advisor:** Integration allows monitoring of upgrade progress and performance metrics, enabling proactive management.  
- **Azure Backup and Azure Site Recovery:** These services complement upgrade operations by providing data protection and disaster recovery capabilities.  
- **Azure DevOps and CI/CD Pipelines:** PostgreSQL

---

### 71. Generally Available: PostgreSQL extension for Visual Studio Code with GitHub Copilot  

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: PostgreSQL extension for Visual Studio Code with GitHub Copilot  ](https://azure.microsoft.com/updates?id=523187)

**Update ID**: 523187
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
The PostgreSQL extension for Visual Studio Code has reached general availability.

- Key changes or new features  
The extension enables developers and IT professionals to connect directly to PostgreSQL database instances within VS Code. Users can run SQL queries, create and manage multiple connection profiles, and leverage Microsoft Entra ID for secure authentication and access management. This integration streamlines database development and administration workflows by embedding PostgreSQL management capabilities into a familiar code editor environment.

- Target audience affected  
Developers working with PostgreSQL databases, database administrators, and IT professionals managing PostgreSQL instances who use Visual Studio Code for development and operational tasks.

- Important notes if any  
The extension’s support for Microsoft Entra ID enhances security by enabling enterprise-grade identity and access management. This update encourages adoption of VS Code as a unified tool for database development and management, reducing context switching. Users should ensure their VS Code and extension versions are up to date to access the latest features and security improvements.

**Details**:

The PostgreSQL extension for Visual Studio Code has reached general availability, providing developers and database administrators with an integrated, efficient environment to manage PostgreSQL databases directly within VS Code. This update addresses the need for streamlined database development workflows by combining code editing, query execution, and connection management in a single interface, enhanced by GitHub Copilot’s AI-assisted coding capabilities and secure authentication via Microsoft Entra ID.

**Background and Purpose**  
PostgreSQL is a widely adopted open-source relational database system, and Visual Studio Code is a leading lightweight, extensible code editor favored by developers. Prior to this update, managing PostgreSQL databases often required switching between multiple tools or relying on less integrated extensions. The purpose of this update is to unify database management and development tasks within VS Code, improving productivity and reducing context switching. Additionally, integrating GitHub Copilot enables AI-assisted query writing and code generation, accelerating development cycles. Support for Microsoft Entra ID (Azure Active Directory) authentication enhances security and simplifies credential management in enterprise environments.

**Specific Features and Detailed Changes**  
- **Connection Management:** Users can create, edit, and manage multiple PostgreSQL connection profiles within VS Code, supporting both local and cloud-hosted PostgreSQL instances.  
- **Query Execution:** The extension allows running SQL queries directly in the editor with results displayed inline or in a dedicated results pane, supporting syntax highlighting and error diagnostics.  
- **Database Object Exploration:** Users can browse database schemas, tables, views, functions, and other objects, facilitating schema understanding and navigation.  
- **Microsoft Entra ID Authentication:** Enables secure, token-based authentication to Azure Database for PostgreSQL instances using Azure Active Directory identities, eliminating the need for password management.  
- **GitHub Copilot Integration:** Provides AI-driven code suggestions and completions for SQL queries and procedural code, improving developer efficiency and reducing errors.  
- **Cross-Platform Support:** Available on Windows, macOS, and Linux, consistent with VS Code’s cross-platform nature.

**Technical Mechanisms and Implementation Methods**  
The extension leverages VS Code’s extension API to integrate PostgreSQL client capabilities, using standard PostgreSQL wire protocol libraries for communication with database servers. Connection profiles are stored securely within VS Code’s settings, optionally encrypted. Authentication with Microsoft Entra ID utilizes OAuth 2.0 flows and Azure Identity libraries to acquire access tokens, which are then used in place of passwords for database authentication. Query execution is handled asynchronously to maintain editor responsiveness, with results parsed and rendered in VS Code’s UI components. GitHub Copilot integration is achieved through the existing Copilot extension API, enabling contextual AI suggestions based on the SQL code context.

**Use Cases and Application Scenarios**  
- **Database Development:** Developers writing application code and SQL queries can stay within VS Code to develop, test, and optimize queries without switching tools.  
- **DevOps and CI/CD:** Integration into VS Code allows database schema changes and query scripts to be version-controlled and tested as part of development pipelines.  
- **Enterprise Database Management:** DBAs can manage multiple PostgreSQL instances, including Azure Database for PostgreSQL, with secure authentication and centralized profile management.  
- **Learning and Prototyping:** New users can explore PostgreSQL features and experiment with queries in an accessible environment enhanced by AI assistance.

**Important Considerations and Limitations**  
- The extension requires VS Code version compatibility and may depend on the GitHub Copilot subscription for AI features.  
- Microsoft Entra ID authentication is currently supported primarily for Azure Database for PostgreSQL; on-premises PostgreSQL servers may require traditional authentication methods.  
- Performance may vary with very large result sets or complex queries; users should monitor resource usage within VS Code.  
- Security best practices should be followed when storing connection profiles, especially on shared machines.

**Integration with Related Azure Services**  
- **Azure Database for PostgreSQL:** Native support with Microsoft Entra ID authentication simplifies secure access to managed PostgreSQL instances

---

### 72. Generally Available: Mirroring in Fabric for PostgreSQL Flexible Server  

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Mirroring in Fabric for PostgreSQL Flexible Server  ](https://azure.microsoft.com/updates?id=523177)

**Update ID**: 523177
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Microsoft Fabric mirroring support for Azure Database for PostgreSQL Flexible Server is now generally available.

- Key changes or new features  
Fabric mirroring enables seamless integration of PostgreSQL Flexible Server data into Microsoft Fabric’s OneLake, unifying organizational data for simplified analytics. It supports network isolation, enhancing security by allowing data synchronization within isolated network environments. This feature streamlines data consolidation workflows, enabling developers and data engineers to leverage Fabric’s analytics and governance capabilities directly on PostgreSQL data without complex ETL processes.

- Target audience affected  
Developers, data engineers, and IT professionals managing Azure Database for PostgreSQL Flexible Server who require unified data analytics and secure data integration within Microsoft Fabric environments.

- Important notes if any  
General availability indicates production readiness with full support. Users should review network isolation configurations to ensure compliance with organizational security policies when enabling mirroring. This integration reduces data movement overhead and accelerates analytics workflows by leveraging Fabric’s OneLake as a central data hub.

**Details**:

The recent general availability of Mirroring in Microsoft Fabric for Azure Database for PostgreSQL Flexible Server introduces a significant enhancement aimed at unifying organizational data and simplifying analytics workflows by enabling seamless data mirroring into Microsoft Fabric’s OneLake storage. This update addresses the growing need for integrated data environments that support advanced analytics while maintaining strict network isolation and security requirements.

**Background and Purpose**  
Azure Database for PostgreSQL Flexible Server is a managed database service that offers high availability, scalability, and enterprise-grade security for PostgreSQL workloads. Microsoft Fabric is a comprehensive analytics platform that centralizes data management and analytics capabilities, with OneLake serving as its unified data lake storage. Prior to this update, integrating PostgreSQL data into Fabric required complex ETL processes or data movement pipelines, which could introduce latency, operational overhead, and security challenges. The introduction of Mirroring in Fabric aims to streamline this integration by providing a direct, near-real-time mirroring capability that brings PostgreSQL data into OneLake, enabling unified analytics and governance.

**Specific Features and Detailed Changes**  
- **Data Mirroring to OneLake:** The core feature is the ability to mirror data from Azure Database for PostgreSQL Flexible Server directly into OneLake, Microsoft Fabric’s unified data lake storage. This mirroring supports continuous synchronization, ensuring data freshness for analytics workloads.  
- **Network Isolation Support:** The mirroring process respects network isolation boundaries, allowing organizations to maintain secure, private network configurations without exposing data to public endpoints. This is critical for compliance and security-sensitive environments.  
- **Simplified Data Unification:** By integrating PostgreSQL data natively into OneLake, users can leverage Fabric’s analytics tools without complex data ingestion pipelines or manual data movement.  
- **General Availability (GA):** The feature has moved from preview to GA, indicating production readiness, SLA-backed support, and full integration with Azure governance and monitoring tools.

**Technical Mechanisms and Implementation Methods**  
Mirroring in Fabric leverages change data capture (CDC) or logical replication features inherent to PostgreSQL Flexible Server. The service continuously captures data changes and streams them securely into OneLake using Fabric’s ingestion framework. This process is optimized to minimize latency and resource consumption on the source database. Network isolation is enforced through Azure Private Link or Virtual Network (VNet) integration, ensuring that data replication traffic remains within private network boundaries. Administrators configure mirroring through the Azure portal or via Azure CLI/PowerShell, specifying source PostgreSQL Flexible Server instances and target OneLake locations within Fabric.

**Use Cases and Application Scenarios**  
- **Unified Analytics:** Organizations can consolidate operational PostgreSQL data with other enterprise data sources in OneLake, enabling cross-source analytics and machine learning workflows within Fabric.  
- **Real-Time Reporting:** Near-real-time mirroring supports up-to-date dashboards and reports without impacting the performance of the production PostgreSQL database.  
- **Data Governance and Compliance:** Centralizing data in OneLake allows consistent application of data governance policies, auditing, and lineage tracking across datasets.  
- **Secure Data Integration:** Enterprises with strict network security policies can mirror data without exposing databases to public networks, supporting compliance with regulatory standards.

**Important Considerations and Limitations**  
- **Supported PostgreSQL Versions:** Mirroring requires PostgreSQL Flexible Server versions that support logical replication and CDC; users should verify compatibility.  
- **Latency and Throughput:** While designed for near-real-time replication, actual latency depends on workload and network conditions; high-throughput scenarios should be tested.  
- **Schema Changes:** Handling of schema changes during mirroring may require manual intervention or downtime; users should plan accordingly.  
- **Cost Implications:** Additional costs may arise from data egress, storage in OneLake, and Fabric analytics usage; budgeting should consider these factors.

**Integration with Related Azure Services**  
- **Azure Database for PostgreSQL Flexible Server:** Source database service providing the data to be mirrored.  
- **Microsoft Fabric and OneLake:** Target analytics platform and

---

### 73. Generally Available: Azure Database for PostgreSQL storage extension support for Parquet 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL storage extension support for Parquet ](https://azure.microsoft.com/updates?id=523167)

**Update ID**: 523167
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL flexible server now supports the Azure Storage extension with Parquet file format.

- Key changes or new features  
Developers and IT professionals can directly read and write Parquet files from the PostgreSQL database using the storage extension. This includes support for multiple compression options, enabling efficient storage and faster data processing workflows. The integration simplifies handling large-scale data analytics and ETL pipelines by leveraging Parquet’s columnar storage benefits within PostgreSQL.

- Target audience affected  
Database developers, data engineers, and IT professionals managing PostgreSQL workloads on Azure who require efficient data interchange between PostgreSQL and Azure Storage, particularly for analytics and big data scenarios.

- Important notes if any  
This feature is generally available, ensuring production readiness and support. Users should review compression options to optimize performance and storage costs based on their workload. Leveraging this extension can reduce data movement overhead and streamline data lake integration.  

For more details, visit: https://azure.microsoft.com/updates?id=523167

**Details**:

The recent general availability announcement for Azure Database for PostgreSQL flexible server introduces native support for the Azure Storage extension with Parquet file format and multiple compression options, significantly enhancing data interoperability and performance for analytics workloads. This update addresses the growing need for efficient, scalable data exchange between PostgreSQL databases and big data ecosystems by enabling seamless read and write operations on Parquet files stored in Azure Blob Storage directly from the database engine.

**Background and Purpose**  
Traditionally, exporting and importing data between PostgreSQL and external storage formats required complex ETL pipelines or external tools, often resulting in performance bottlenecks and increased operational overhead. Parquet, a columnar storage file format optimized for analytical queries, is widely used in data lakes and big data platforms due to its efficient compression and encoding schemes. By integrating Parquet support directly into Azure Database for PostgreSQL flexible server via the Azure Storage extension, Microsoft aims to simplify data workflows, reduce latency, and improve throughput for analytics and data engineering tasks.

**Specific Features and Detailed Changes**  
- **Parquet Format Support:** Users can now read from and write to Parquet files stored in Azure Blob Storage directly through PostgreSQL queries using the storage extension.  
- **Multiple Compression Options:** The extension supports various compression codecs (e.g., Snappy, Gzip, Brotli), allowing users to balance between compression ratio and CPU usage based on workload requirements.  
- **Seamless Integration:** The extension exposes functions and foreign data wrappers (FDWs) that enable querying Parquet files as if they were regular database tables, facilitating easy integration into existing SQL workflows.  
- **Flexible Server Compatibility:** This feature is available on Azure Database for PostgreSQL flexible server deployment model, ensuring high availability and scalability.

**Technical Mechanisms and Implementation Methods**  
The Azure Storage extension leverages PostgreSQL’s extensibility framework to add foreign data wrappers that interface with Azure Blob Storage. When a Parquet file is queried, the extension translates SQL queries into efficient read operations on the Parquet file, utilizing the columnar format to minimize I/O and memory usage. Writing data involves serializing query results into Parquet format with the selected compression codec and uploading the file to Azure Blob Storage. Authentication and access control are managed via Azure Active Directory or storage account keys, ensuring secure data operations. The extension is installed and managed as a PostgreSQL extension, configurable via standard SQL commands.

**Use Cases and Application Scenarios**  
- **Data Lake Integration:** Analysts and data engineers can query Parquet datasets stored in Azure Data Lake Storage Gen2 directly from PostgreSQL without data movement.  
- **ETL Simplification:** Developers can export query results as compressed Parquet files for downstream processing in Azure Synapse Analytics, Databricks, or other big data platforms.  
- **Hybrid Workloads:** Applications requiring both transactional and analytical processing can leverage PostgreSQL for OLTP and use Parquet files for batch analytics seamlessly.  
- **Cost Optimization:** Efficient compression and direct file access reduce storage costs and improve query performance for large datasets.

**Important Considerations and Limitations**  
- The feature is currently supported only on the flexible server deployment model, not on single server or hyperscale (Citus) models.  
- Performance gains depend on file size, compression codec, and query complexity; benchmarking is recommended for production workloads.  
- Proper configuration of network and firewall rules is necessary to allow PostgreSQL flexible server to access Azure Blob Storage securely.  
- Parquet schema evolution and compatibility should be managed carefully to avoid query errors.  
- The extension requires explicit installation and permission grants within the PostgreSQL instance.

**Integration with Related Azure Services**  
This update enhances interoperability with Azure Blob Storage and Azure Data Lake Storage Gen2, enabling PostgreSQL to act as a query engine over data lake files. It complements Azure Synapse Analytics and Azure Databricks by simplifying data exchange in Parquet format. Additionally, integration with Azure Active Directory and managed identities streamlines secure authentication

---

### 74. Generally Available: Azure SQL Managed Instance Next-gen General Purpose service tier 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure SQL Managed Instance Next-gen General Purpose service tier ](https://azure.microsoft.com/updates?id=523125)

**Update ID**: 523125
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure SQL Managed Instance

**Summary**:

- What was updated  
Azure SQL Managed Instance introduced the Next-gen General Purpose service tier, now generally available.

- Key changes or new features  
This new tier offers a significant performance improvement over the existing General Purpose tier while maintaining cost-effectiveness. It provides enhanced compute power and greater flexibility in resource allocation. Importantly, it retains the fully managed PaaS experience, ensuring ease of use and simplified management without compromising on scalability or performance.

- Target audience affected  
Developers and IT professionals managing SQL workloads on Azure SQL Managed Instance who require improved performance and flexibility without increasing operational complexity or cost.

- Important notes if any  
The Next-gen General Purpose tier is designed to deliver a balance of performance and cost, making it suitable for a wide range of production workloads. Users can expect seamless migration or upgrade paths within Azure SQL Managed Instance. For detailed pricing and migration guidance, refer to the official Azure documentation.

**Details**:

The Azure SQL Managed Instance Next-gen General Purpose service tier is now generally available, offering a significant performance enhancement while maintaining cost efficiency and the fully managed PaaS experience that customers rely on. This update addresses the need for improved compute power and flexibility in Azure SQL Managed Instance deployments without compromising ease of management or scalability.

**Background and Purpose**  
Azure SQL Managed Instance provides a fully managed SQL Server instance in the cloud, combining the rich SQL Server surface area with the benefits of PaaS, such as automated patching, backups, and high availability. The existing General Purpose tier balances performance and cost for most business workloads. However, as cloud applications evolve, there is increasing demand for higher performance and more flexible compute options to handle larger transactional workloads and complex queries. The Next-gen General Purpose tier was introduced to meet these demands by delivering enhanced hardware capabilities and architectural improvements while preserving cost-effectiveness.

**Specific Features and Detailed Changes**  
- **Improved Hardware and Storage Architecture:** The Next-gen General Purpose tier leverages newer hardware generations with faster CPUs and improved memory configurations. It also uses remote storage with enhanced throughput and lower latency, optimizing I/O performance for database operations.  
- **Increased Compute Flexibility:** Customers can now select from a broader range of vCore sizes and memory configurations, enabling more precise tuning of resources to workload requirements.  
- **Maintained PaaS Benefits:** Despite the performance boost, the tier retains all PaaS features such as automated backups, built-in high availability with zone redundancy, automated patching, and security features like Advanced Threat Protection and data encryption.  
- **Compatibility and Migration:** The Next-gen tier is designed to be compatible with existing General Purpose deployments, allowing seamless upgrades without application changes or downtime.

**Technical Mechanisms and Implementation Methods**  
The Next-gen General Purpose tier is implemented on upgraded hardware infrastructure within Azure datacenters, utilizing the latest Intel or AMD processors and NVMe-based remote storage to reduce latency. The architecture separates compute and storage layers, enabling independent scaling and improved resource utilization. Azure SQL Managed Instance orchestrates this through intelligent resource management and workload optimization algorithms built into the service fabric. The platform also continues to leverage Azure’s network fabric for secure and reliable connectivity, including support for Virtual Network (VNet) integration and private endpoints.

**Use Cases and Application Scenarios**  
- **Medium to Large OLTP Workloads:** Applications requiring faster transaction processing and query response times benefit significantly from the enhanced compute and I/O capabilities.  
- **Business-critical Applications:** Enterprises running ERP, CRM, or financial systems that demand high availability and predictable performance can leverage the improved tier for better SLA adherence.  
- **Cloud Migration and Modernization:** Organizations migrating on-premises SQL Server workloads to Azure can achieve near on-premises performance with the simplicity of PaaS.  
- **Development and Testing:** Teams needing flexible compute sizing for variable workloads can optimize costs by scaling resources according to demand.

**Important Considerations and Limitations**  
- **Cost Implications:** While the Next-gen tier is designed to be cost-effective, the increased compute and storage performance may lead to higher charges compared to the original General Purpose tier. Careful sizing and monitoring are recommended.  
- **Region Availability:** Initially, the Next-gen General Purpose tier may be available in select Azure regions; users should verify availability in their target regions.  
- **Migration Path:** Upgrading existing Managed Instances to the Next-gen tier is supported but should be planned to minimize impact, including testing workloads post-upgrade.  
- **Feature Parity:** The Next-gen tier maintains feature parity with the existing General Purpose tier; however, users should verify specific feature support if relying on niche capabilities.

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Advisor:** Enhanced telemetry and recommendations help optimize performance and cost for Next-gen tier instances.  
- **Azure Backup and Azure Security Center:** Continue to provide integrated backup management and security posture monitoring.

---

### 75. Public Preview: Azure SQL Database DiskANN vector indexing 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure SQL Database DiskANN vector indexing ](https://azure.microsoft.com/updates?id=523110)

**Update ID**: 523110
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**Summary**:

- What was updated  
Azure SQL Database, Azure SQL Managed Instance, and SQL database in Microsoft Fabric now support vector indexing using DiskANN, announced in public preview.

- Key changes or new features  
DiskANN, an efficient algorithm for approximate nearest neighbor search on disk, is integrated to enable fast and scalable vector similarity searches directly within these SQL platforms. This enhancement facilitates advanced scenarios such as product recommendations, semantic search, and AI-powered applications by allowing developers to store and query high-dimensional vector data natively. The integration improves performance and scalability for large-scale vector workloads without needing external services.

- Target audience affected  
Developers building AI, machine learning, and recommendation systems; data engineers managing vector data; and IT professionals responsible for database performance and scalability in Azure SQL environments.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Documentation and best practices for implementing DiskANN vector indexing are available to help optimize usage. Being a preview, SLA and support terms may differ from generally available features.

**Details**:

The recent public preview announcement of Azure SQL Database DiskANN vector indexing introduces a significant enhancement for handling high-dimensional vector data within Azure SQL Database, Azure SQL Managed Instance, and SQL database in Microsoft Fabric. This update integrates DiskANN, a state-of-the-art algorithm designed for efficient approximate nearest neighbor (ANN) search on disk, enabling scalable and performant vector similarity queries directly within the SQL ecosystem.

**Background and Purpose**  
With the growing adoption of AI and machine learning workloads, applications increasingly rely on vector representations of data—such as embeddings from natural language processing, image recognition, or recommendation systems—to perform similarity searches. Traditional relational databases are not optimized for these high-dimensional vector operations, often requiring external services or complex architectures. The purpose of this update is to natively support vector indexing and similarity search in Azure SQL environments, simplifying architecture and improving performance for vector-based queries.

**Specific Features and Detailed Changes**  
- **DiskANN Integration:** Azure SQL now supports DiskANN, an algorithm optimized for approximate nearest neighbor search that balances accuracy, speed, and storage efficiency by leveraging disk-based indexing structures.  
- **Vector Data Type Support:** New data types and indexing capabilities allow storage and indexing of vector embeddings directly in SQL tables.  
- **Index Creation and Querying:** Users can create DiskANN vector indexes on columns containing vector data and perform similarity searches using SQL syntax extensions, enabling seamless integration with existing SQL queries.  
- **Support Across Platforms:** This feature is available in Azure SQL Database, Azure SQL Managed Instance, and SQL database within Microsoft Fabric, ensuring broad applicability across Azure’s SQL offerings.

**Technical Mechanisms and Implementation Methods**  
DiskANN operates by building a graph-based index on disk that approximates nearest neighbor relationships among vectors. Unlike in-memory ANN methods, DiskANN efficiently manages large datasets that exceed memory capacity by using SSDs, thus enabling scalable vector search. The integration within Azure SQL involves:  
- Extending the SQL engine to recognize vector data types and manage DiskANN indexes.  
- Implementing query operators that translate SQL similarity search commands into DiskANN index traversals.  
- Optimizing storage and retrieval paths to minimize latency and maximize throughput for vector queries.  
- Providing control over index parameters such as index build time, accuracy trade-offs, and storage footprint.

**Use Cases and Application Scenarios**  
- **Product Recommendations:** Quickly find similar products based on vector embeddings derived from user behavior or product attributes.  
- **Content-Based Search:** Enable semantic search over documents, images, or multimedia by comparing vector embeddings representing content features.  
- **Anomaly Detection:** Identify outliers by measuring vector distances in monitoring or security datasets.  
- **Personalization Engines:** Deliver customized experiences by matching user profiles or preferences encoded as vectors.  
- **AI/ML Model Integration:** Store and query embeddings generated by machine learning models without moving data outside the database.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, DiskANN vector indexing may have limited SLA guarantees and could undergo changes before general availability.  
- **Indexing Overhead:** Building and maintaining DiskANN indexes incurs storage and compute overhead; tuning index parameters is essential for balancing performance and resource usage.  
- **Query Accuracy vs. Performance:** DiskANN uses approximate search; thus, results may not always be exact nearest neighbors, requiring application-level tolerance for approximation.  
- **Data Size and Dimensionality:** While DiskANN is optimized for large-scale data, extremely high-dimensional vectors or very large datasets may require careful resource planning.  
- **Security and Compliance:** Ensure vector data and indexing comply with organizational security policies, especially when embedding sensitive information.

**Integration with Related Azure Services**  
- **Microsoft Fabric:** The feature’s availability in SQL database within Microsoft Fabric facilitates unified analytics and data engineering workflows involving vector data.  
- **Azure Machine Learning:** Embeddings generated by Azure ML models can be directly stored and queried using DiskANN indexes, streamlining

---

### 76. Generally Available: MSSQL extension integration with GitHub Copilot in Visual Studio Code  

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: MSSQL extension integration with GitHub Copilot in Visual Studio Code  ](https://azure.microsoft.com/updates?id=523105)

**Update ID**: 523105
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code has been updated to integrate GitHub Copilot, now generally available.

- Key changes or new features  
This integration embeds AI-powered code completion and suggestions directly within the MSSQL extension, enabling developers to generate SQL queries, database schema designs, and routine SQL code faster. GitHub Copilot assists by reducing repetitive coding tasks and accelerating the development workflow inside VS Code.

- Target audience affected  
Developers and database professionals who use Visual Studio Code for SQL development and database management will benefit from enhanced productivity and smarter coding assistance.

- Important notes if any  
Users need to have GitHub Copilot enabled in their VS Code environment to leverage this feature. This integration streamlines SQL development but still requires developer oversight to ensure generated code meets specific business and security requirements.

For more details, visit: https://azure.microsoft.com/updates?id=523105

**Details**:

The recent general availability of the MSSQL extension integration with GitHub Copilot in Visual Studio Code represents a significant enhancement for database developers and administrators by embedding AI-driven code assistance directly into their SQL development environment. This update aims to streamline SQL coding tasks, reduce manual effort, and accelerate database schema design and query writing through intelligent code suggestions powered by GitHub Copilot.

**Background and Purpose**  
Traditionally, SQL development involves repetitive coding patterns, complex query formulation, and iterative schema design, which can be time-consuming and error-prone. The MSSQL extension for Visual Studio Code has been widely adopted for managing SQL Server and Azure SQL databases within a lightweight, extensible code editor. By integrating GitHub Copilot, an AI pair programmer trained on a vast corpus of code, Microsoft intends to enhance developer productivity by providing context-aware code completions, recommendations, and even generating complex SQL snippets based on natural language prompts. This integration aligns with the broader trend of leveraging AI to improve developer tooling and reduce cognitive load.

**Specific Features and Detailed Changes**  
- **AI-Powered SQL Code Suggestions:** GitHub Copilot now provides inline code completions and suggestions within the MSSQL extension, helping users write SQL queries, stored procedures, and schema definitions faster.  
- **Natural Language to SQL Conversion:** Developers can write comments or prompts in natural language, and Copilot can generate corresponding SQL code snippets, which is particularly useful for complex query generation or unfamiliar syntax.  
- **Schema Design Assistance:** Copilot can assist in designing table schemas by suggesting column definitions, data types, and constraints based on the context.  
- **Error Reduction:** By suggesting syntactically correct and optimized SQL code, the integration reduces common errors and improves code quality.  
- **Seamless Workflow Integration:** The AI assistance is embedded directly within Visual Studio Code’s MSSQL extension, requiring no additional setup beyond enabling GitHub Copilot.

**Technical Mechanisms and Implementation Methods**  
The integration leverages GitHub Copilot’s AI model, which is based on OpenAI Codex, to analyze the current SQL code context within Visual Studio Code. When a developer types SQL code or comments, the extension sends contextual information securely to the Copilot service, which returns relevant code completions or suggestions. These suggestions are rendered inline in the editor, allowing developers to accept, reject, or modify them. The MSSQL extension acts as the interface layer, ensuring that suggestions are contextually appropriate for SQL Server dialects and Azure SQL environments. Authentication and authorization are managed via GitHub accounts, and data privacy is maintained according to GitHub Copilot’s policies.

**Use Cases and Application Scenarios**  
- **Rapid Query Development:** Developers can quickly generate complex SELECT, JOIN, and aggregation queries without manual syntax lookup.  
- **Stored Procedure and Function Creation:** Copilot can assist in scaffolding stored procedures or user-defined functions based on descriptive comments.  
- **Database Schema Evolution:** When modifying or creating new tables, Copilot’s suggestions help define columns, indexes, and constraints efficiently.  
- **Learning and Onboarding:** New SQL developers can learn best practices and SQL idioms by reviewing AI-generated code snippets.  
- **Automation of Repetitive Tasks:** Routine SQL scripting tasks, such as data insertion or update statements, can be accelerated.

**Important Considerations and Limitations**  
- **Accuracy and Validation:** While Copilot provides helpful suggestions, it may occasionally generate incorrect or suboptimal SQL code; developers must review and test all AI-generated code.  
- **Security and Privacy:** Sensitive database schema or query information should be handled carefully, considering that code context is sent to GitHub Copilot’s cloud service.  
- **Dependency on Internet Connectivity:** The AI assistance requires internet access to communicate with GitHub Copilot services.  
- **Licensing and Cost:** GitHub Copilot is a paid service after a trial period; organizations should consider licensing implications.  
- **Dialect Specificity

---

### 77. Generally Available: Azure SQL Database long-term retention (LTR) backup immutability 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure SQL Database long-term retention (LTR) backup immutability ](https://azure.microsoft.com/updates?id=523095)

**Update ID**: 523095
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database

**Summary**:

- What was updated  
Azure SQL Database long-term retention (LTR) backups now support immutability.

- Key changes or new features  
Users can configure immutability policies on LTR backups, ensuring backups cannot be modified or deleted until the retention period expires. This feature enhances data protection by preventing accidental or malicious deletion, including ransomware attacks. It helps organizations meet compliance and regulatory requirements for data retention and immutability.

- Target audience affected  
Developers and IT professionals managing Azure SQL Database backups, especially those in regulated industries requiring strict data retention and protection policies.

- Important notes if any  
Once immutability is enabled on LTR backups, the backups are locked for the configured retention duration and cannot be altered or removed. Plan retention policies carefully to avoid unintended data lock-in. This feature is generally available and can be configured via Azure Portal, PowerShell, CLI, or REST API.

**Details**:

The recent general availability of Azure SQL Database long-term retention (LTR) backup immutability introduces a critical enhancement to Azure’s data protection and compliance capabilities by enabling customers to configure immutable backups that cannot be altered or deleted until a predefined retention period expires. This update addresses growing regulatory and security demands, particularly for organizations subject to stringent data governance, compliance frameworks (e.g., GDPR, HIPAA, SOX), and ransomware resilience requirements.

**Background and Purpose**  
Long-term retention (LTR) backups in Azure SQL Database allow customers to store full database backups for extended periods (up to 10 years), supporting regulatory compliance and archival needs. However, prior to this update, LTR backups could be deleted or modified, either accidentally or maliciously, posing risks to data integrity and compliance adherence. The introduction of immutability ensures that once a backup is marked immutable, it is safeguarded against deletion or tampering, thereby enhancing the trustworthiness and auditability of retained backups.

**Specific Features and Detailed Changes**  
- **Immutability Configuration:** Users can now specify an immutable retention period on LTR backups, during which the backup is locked and cannot be deleted or altered.  
- **Retention Enforcement:** The system enforces the immutability period strictly, preventing any deletion or modification operations on the backup until the retention period elapses.  
- **Policy Integration:** Immutability settings can be configured via Azure Portal, PowerShell, CLI, or ARM templates, allowing automation and integration into existing backup management workflows.  
- **Compliance Alignment:** The feature supports compliance with regulations requiring non-repudiable, tamper-proof data retention.  

**Technical Mechanisms and Implementation Methods**  
Under the hood, immutability leverages Azure Storage’s immutable blob storage capabilities, where LTR backups are stored as blobs with legal hold or time-based retention policies applied. When immutability is enabled, Azure SQL Database applies a retention lock on the underlying backup blob, ensuring that no delete or overwrite operations can be performed until the retention period expires. This lock is cryptographically enforced and audited by Azure’s control plane, preventing unauthorized or accidental removal. The retention period is strictly enforced by the Azure Backup service and cannot be shortened or bypassed once set, ensuring compliance integrity.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Financial services, healthcare, and government sectors can meet strict data retention and audit requirements by ensuring backups remain immutable for mandated durations.  
- **Ransomware Protection:** Immutable backups serve as a reliable recovery point that ransomware cannot encrypt or delete, enabling organizations to restore data without paying ransoms.  
- **Long-Term Archival:** Organizations needing to retain data for years for legal or business reasons can do so with confidence that backups remain intact and unaltered.  
- **Audit and Forensics:** Immutable backups provide a trustworthy source for forensic investigations and compliance audits.  

**Important Considerations and Limitations**  
- **Retention Period Irrevocability:** Once immutability is set, the retention period cannot be shortened or removed, so planning retention duration carefully is critical.  
- **Cost Implications:** Longer retention and immutable storage may increase storage costs; organizations should balance compliance needs with cost management.  
- **Backup Deletion:** Backups cannot be deleted during the immutable period, which may impact storage cleanup strategies.  
- **Scope:** Immutability applies only to LTR backups, not to short-term or automated backups.  

**Integration with Related Azure Services**  
- **Azure Storage:** Utilizes immutable blob storage features for retention enforcement.  
- **Azure Backup:** Coordinates backup lifecycle and retention policies with immutability settings.  
- **Azure Policy:** Can be used to enforce organizational standards around backup immutability configuration.  
- **Azure Monitor and Azure Security Center:** Provide monitoring and alerting capabilities for backup operations and compliance status.  

In summary, the GA release of Azure SQL Database LTR

---

### 78. Generally Available: SQL Server Management Studio (SSMS) 22 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: SQL Server Management Studio (SSMS) 22 ](https://azure.microsoft.com/updates?id=522586)

**Update ID**: 522586
**Data source**: Azure Updates API

**Categories**: Launched

**Summary**:

- What was updated  
SQL Server Management Studio (SSMS) version 22 has been released as Generally Available (GA).

- Key changes or new features  
SSMS 22 is built on Visual Studio 2026, providing enhanced performance and stability. It introduces full support for managing SQL Server 2025 instances, including new features and compatibility improvements. The update also offers improved integration with Azure SQL databases, streamlining cloud database management. Additional enhancements include updated T-SQL editor capabilities, better troubleshooting tools, and refined user interface elements for increased productivity.

- Target audience affected  
Database administrators, developers, and IT professionals who manage and develop on SQL Server environments, especially those working with SQL Server 2025 and Azure SQL databases.

- Important notes if any  
Users should upgrade to SSMS 22 to leverage the latest SQL Server 2025 features and improved Azure integration. The update maintains backward compatibility with earlier SQL Server versions, ensuring a smooth transition. It is recommended to review the official release notes for detailed changes and known issues.  

For more details, visit: https://azure.microsoft.com/updates?id=522586

**Details**:

The release of SQL Server Management Studio (SSMS) 22 marks a significant update to Microsoft’s primary integrated environment for managing SQL Server instances and databases, now generally available and built on the Visual Studio 2026 shell. This update aims to enhance database administrators’ and developers’ productivity by providing compatibility with the latest SQL Server 2025 features, improving tooling integration, and refining performance and usability.

**Background and Purpose**  
SSMS has been the cornerstone tool for SQL Server management, offering a graphical interface for database administration, query writing, and troubleshooting. With the release of SQL Server 2025, there was a need to update SSMS to support new engine features and provide a modernized development environment. SSMS 22 addresses this by leveraging the Visual Studio 2026 platform, enabling better extensibility, improved UI responsiveness, and support for the latest SQL Server capabilities.

**Specific Features and Detailed Changes**  
- **Support for SQL Server 2025:** SSMS 22 introduces full compatibility with SQL Server 2025, allowing users to manage new engine features such as enhanced security options, performance improvements, and new T-SQL constructs.  
- **Built on Visual Studio 2026 Shell:** This upgrade provides a more stable and scalable foundation, enabling faster load times, improved memory management, and a more consistent user interface aligned with modern Visual Studio experiences.  
- **Improved Integration with SQL Databases:** Enhancements include better connectivity options, refined IntelliSense for T-SQL, and improved query execution plans visualization.  
- **Enhanced Troubleshooting Tools:** Diagnostic tools have been updated to provide deeper insights into query performance and server health, facilitating faster root cause analysis.  
- **Updated Extensions and Plug-in Support:** The Visual Studio 2026 base allows for easier extension development and deployment, enabling third-party and custom tools integration.

**Technical Mechanisms and Implementation Methods**  
SSMS 22 is architected on the Visual Studio 2026 shell, which means it inherits the modular design and extensibility framework of Visual Studio. This allows SSMS components to be updated independently, improving maintainability. The integration with SQL Server 2025 is achieved by updating the underlying SMO (SQL Server Management Objects) libraries and T-SQL parsers to recognize new syntax and features. Connectivity improvements leverage updated network protocols and authentication methods supported by SQL Server 2025, including enhanced Azure Active Directory authentication flows.

**Use Cases and Application Scenarios**  
- **Database Administration:** DBAs can manage SQL Server 2025 instances, configure security policies, monitor performance, and automate maintenance tasks.  
- **Development and Testing:** Developers benefit from improved IntelliSense and debugging tools when writing complex T-SQL scripts or stored procedures targeting SQL Server 2025.  
- **Performance Tuning:** The updated query plan visualizer and diagnostic tools help identify bottlenecks and optimize queries in production and development environments.  
- **Hybrid Cloud Scenarios:** Users managing on-premises SQL Server instances alongside Azure SQL databases can leverage improved connectivity and integration features.

**Important Considerations and Limitations**  
- SSMS 22 is backward compatible with earlier SQL Server versions, but some new features may not be available when connected to older instances.  
- The upgrade to Visual Studio 2026 shell may require additional system resources; ensure client machines meet the recommended specifications.  
- Certain third-party extensions built for previous SSMS versions might require updates to be fully compatible with SSMS 22.  
- While SSMS supports Azure SQL Database management, some cloud-specific features may require Azure Data Studio or Azure Portal for full functionality.

**Integration with Related Azure Services**  
SSMS 22 enhances integration with Azure SQL Database and Azure SQL Managed Instance by supporting the latest authentication methods, including Azure Active Directory Multi-Factor Authentication (MFA) and Managed Identity. It also improves connectivity to Azure Synapse Analytics for querying and managing data warehouses. The improved tooling supports hybrid scenarios where databases span

---

### 79. Generally Available: Microsoft Python driver for SQL Server 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Microsoft Python driver for SQL Server ](https://azure.microsoft.com/updates?id=522581)

**Update ID**: 522581
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database

**Summary**:

- What was updated  
Microsoft has announced the general availability (GA) of the mssql-python driver, a new Python driver for SQL Server and Azure SQL Database.

- Key changes or new features  
The mssql-python driver offers a modern, high-performance, and developer-friendly experience tailored for Python applications. It supports core SQL Server features and is designed to improve connectivity, reliability, and efficiency when interacting with SQL Server and Azure SQL Database from Python code.

- Target audience affected  
Python developers building applications that connect to SQL Server or Azure SQL Database, as well as IT professionals managing Python-based data solutions on Microsoft data platforms.

- Important notes if any  
This GA release signifies production readiness, encouraging developers to adopt the mssql-python driver for improved performance and support. Existing users of older drivers like pyodbc may consider migration to leverage enhanced capabilities. Documentation and support resources are available to facilitate integration.

**Details**:

The Microsoft Python driver for SQL Server (mssql-python) has reached general availability, representing a significant advancement in enabling Python developers to efficiently connect and interact with SQL Server and Azure SQL Database environments. This update addresses the growing demand for a modern, high-performance, and developer-centric database connectivity solution tailored specifically for Python applications within the Microsoft data ecosystem.

**Background and Purpose**  
Prior to this release, Python developers primarily relied on third-party ODBC drivers or community-supported libraries such as pyodbc to connect to SQL Server databases. While functional, these options often involved complex configurations, limited feature support, or suboptimal performance. The mssql-python driver was introduced to provide a native, officially supported Python client that simplifies connectivity, enhances performance, and aligns with modern Python development practices. The general availability status confirms its production readiness, stability, and comprehensive support from Microsoft.

**Specific Features and Detailed Changes**  
- **Native Python Support:** The driver is implemented in Python with C extensions, providing a balance between ease of use and performance.  
- **High Performance:** Optimized for reduced latency and efficient data retrieval, supporting bulk operations and asynchronous programming patterns.  
- **Full TDS Protocol Support:** Implements the Tabular Data Stream (TDS) protocol natively, enabling direct communication with SQL Server without relying on ODBC layers.  
- **Advanced Data Types:** Supports a wide range of SQL Server data types, including newer types like datetime2, datetimeoffset, and spatial types.  
- **Integrated Authentication:** Supports Azure Active Directory authentication methods, including managed identities, enabling secure and seamless authentication in Azure environments.  
- **Parameterized Queries and Stored Procedures:** Provides robust support for parameterized queries to prevent SQL injection and execute stored procedures efficiently.  
- **Connection Pooling:** Built-in connection pooling improves scalability for high-throughput applications.  
- **Cross-Platform Compatibility:** Works on Windows, Linux, and macOS, aligning with Python’s cross-platform nature.

**Technical Mechanisms and Implementation Methods**  
The driver communicates directly with SQL Server using the TDS protocol, bypassing the ODBC layer to reduce overhead and improve throughput. It leverages asynchronous I/O capabilities in Python (asyncio) to support non-blocking database operations, which is critical for scalable web applications and microservices. Authentication mechanisms integrate with Azure Active Directory libraries to facilitate token-based authentication, including support for OAuth 2.0 flows and managed identities in Azure-hosted environments. The driver’s architecture modularizes connection management, query execution, and data type conversion to ensure maintainability and extensibility.

**Use Cases and Application Scenarios**  
- **Cloud-Native Applications:** Python applications deployed on Azure App Service, Azure Functions, or Azure Kubernetes Service can use the driver for efficient database access with native Azure AD authentication.  
- **Data Engineering and Analytics:** Data pipelines and ETL processes written in Python can leverage the driver for high-performance data ingestion and transformation from SQL Server sources.  
- **Machine Learning and AI:** Integration with Azure Machine Learning workflows where Python scripts require direct access to SQL Server data stores.  
- **Web and API Development:** Backend services developed with frameworks like Django or Flask can use the driver for secure and performant database interactions.

**Important Considerations and Limitations**  
- While the driver supports a broad set of SQL Server features, some advanced functionalities (e.g., SQL Server-specific bulk copy APIs) may still require additional tooling or libraries.  
- Users migrating from pyodbc or other drivers should review connection string formats and authentication configurations, as these may differ.  
- As a relatively new driver, community ecosystem and third-party tool integrations may be less mature compared to established drivers.  
- Performance tuning and troubleshooting require familiarity with the driver’s logging and diagnostic capabilities, which are documented in the official Microsoft repository.

**Integration with Related Azure Services**  
The mssql-python driver integrates seamlessly with Azure SQL Database and Azure SQL Managed Instance, supporting Azure AD authentication and managed

---

### 80. Generally Available: New SQL Server migration in Azure Arc 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: New SQL Server migration in Azure Arc ](https://azure.microsoft.com/updates?id=522572)

**Update ID**: 522572
**Data source**: Azure Updates API

**Categories**: Launched, Hybrid + multicloud, Azure Arc

**Summary**:

- What was updated  
Azure released a new SQL Server migration solution integrated with Azure Arc, now generally available.  

- Key changes or new features  
This solution leverages Azure Database Migration Service combined with AI-powered Copilot assistance to provide an automated, end-to-end migration experience. It simplifies and accelerates migrating on-premises or hybrid SQL Server instances to Azure SQL Managed Instance within Azure Arc environments. The integration ensures seamless management and migration across diverse infrastructures, enhancing operational consistency and reducing manual effort.  

- Target audience affected  
Developers and IT professionals managing SQL Server workloads in hybrid or multi-cloud environments who are looking to migrate databases to Azure SQL Managed Instance while maintaining Azure Arc management capabilities. Database administrators and cloud architects will benefit from streamlined migration workflows and improved automation.  

- Important notes if any  
The solution supports Azure Arc-enabled servers, enabling migration without requiring full cloud rehosting. Users should ensure their environments are compatible with Azure Arc and Azure Database Migration Service prerequisites. This update reflects Microsoft’s commitment to hybrid cloud database modernization with AI-assisted tooling.  

For detailed guidance and deployment instructions, refer to the official Azure update page.  
https://azure.microsoft.com/updates?id=522572

**Details**:

The recent general availability of the new SQL Server migration solution in Azure Arc represents a significant advancement in hybrid cloud database modernization by enabling seamless, automated migration of on-premises or multi-cloud SQL Server instances to Azure SQL Managed Instance through Azure Arc. This update addresses the growing need for organizations to modernize their SQL Server workloads while maintaining operational consistency across diverse environments.

**Background and Purpose**  
Enterprises often face challenges migrating legacy SQL Server databases to the cloud due to complexity, downtime risks, and heterogeneous infrastructure. Azure Arc extends Azure management and governance capabilities to on-premises and multi-cloud resources, enabling a unified management plane. The purpose of this update is to leverage Azure Arc to orchestrate and simplify the migration of SQL Server instances into Azure SQL Managed Instance, thereby accelerating cloud adoption and reducing manual intervention.

**Specific Features and Detailed Changes**  
- **End-to-End Automated Migration:** The solution integrates Azure Database Migration Service (DMS) with Azure Arc to provide a fully automated migration workflow.  
- **Copilot Assistance:** AI-powered Copilot guidance helps users through the migration process, offering contextual recommendations and reducing the learning curve.  
- **Hybrid and Multi-Cloud Support:** Enables migration from SQL Server instances running on-premises, in Azure Arc-enabled Kubernetes clusters, or other cloud providers.  
- **Unified Management:** Post-migration, the SQL Managed Instances remain connected to Azure Arc, allowing consistent policy enforcement, monitoring, and security management.  
- **Minimal Downtime:** Supports online migration scenarios to minimize downtime during cutover.  

**Technical Mechanisms and Implementation Methods**  
The migration solution operates by first onboarding the source SQL Server instances into Azure Arc, which registers them as connected machines or Kubernetes clusters. Azure Database Migration Service is then provisioned and orchestrated via Azure Arc to perform schema assessment, data replication, and cutover operations. Copilot integrates through Azure Portal or Azure CLI, providing step-by-step migration guidance and automating routine tasks such as network configuration, firewall rule setup, and performance tuning recommendations. The underlying data movement leverages DMS’s native capabilities for transactional replication or backup-restore methods depending on the scenario.

**Use Cases and Application Scenarios**  
- **Hybrid Cloud Modernization:** Organizations with SQL Server workloads on-premises seeking to migrate to Azure SQL Managed Instance without disrupting existing operations.  
- **Multi-Cloud Migration:** Enterprises running SQL Server in other clouds can use Azure Arc to centralize migration management to Azure.  
- **Disaster Recovery and High Availability:** Facilitates migrating to Azure for improved resilience and DR capabilities while maintaining hybrid connectivity.  
- **Dev/Test Environments:** Enables rapid cloning and migration of SQL Server instances for development and testing in Azure.  

**Important Considerations and Limitations**  
- **Prerequisites:** Source SQL Server instances must be compatible with Azure Arc onboarding and meet version requirements for migration.  
- **Network Configuration:** Proper network connectivity and firewall rules must be established between source environments, Azure Arc, and Azure SQL Managed Instance.  
- **Resource Constraints:** Migration performance depends on network bandwidth and resource availability on source and target environments.  
- **Feature Parity:** Some SQL Server features may have limited support or require adjustments when migrating to Azure SQL Managed Instance.  
- **Security and Compliance:** Ensure compliance with organizational policies when extending Azure management to on-premises or other cloud environments.  

**Integration with Related Azure Services**  
- **Azure Database Migration Service:** Core engine for data migration, schema conversion, and replication.  
- **Azure Arc:** Provides the hybrid management layer enabling resource onboarding and governance.  
- **Azure SQL Managed Instance:** Target platform offering fully managed SQL Server capabilities in Azure.  
- **Azure Monitor and Azure Security Center:** Post-migration monitoring and security management integrated through Azure Arc.  
- **Azure CLI and Azure Portal:** Interfaces for managing migration workflows and Copilot assistance.  

In summary, the new SQL Server migration in Azure Arc solution delivers a comprehensive, automated

---

### 81. Generally Availabe: SQL Server 2025 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Availabe: SQL Server 2025 ](https://azure.microsoft.com/updates?id=522559)

**Update ID**: 522559
**Data source**: Azure Updates API

**Categories**: Launched

**Summary**:

- What was updated  
Microsoft has announced the general availability of SQL Server 2025, the latest version of its enterprise database platform.

- Key changes or new features  
SQL Server 2025 introduces built-in AI capabilities designed to enhance data processing and analytics directly within the database engine. It offers seamless integration with Microsoft Fabric, enabling unified data governance and analytics across cloud and on-premises environments. The release focuses on modernizing enterprise data platforms by improving performance, security, and scalability, while embedding AI-driven insights and automation to support intelligent applications and workloads.

- Target audience affected  
This update primarily targets database administrators, developers, and IT professionals managing enterprise data infrastructure who seek to leverage AI-enhanced database features and integrate with Microsoft’s broader data ecosystem.

- Important notes if any  
Organizations should evaluate the new AI features and integration capabilities to optimize their data strategies. Compatibility and migration paths from earlier SQL Server versions are expected to be supported, but testing in development environments is recommended before production deployment. Additional resources and documentation are available via the Microsoft Azure updates portal.

**Details**:

The general availability of SQL Server 2025 represents a significant advancement in Microsoft’s enterprise data platform strategy, emphasizing AI integration and modernization to address evolving data workloads and analytics demands. This release is designed to empower IT professionals and developers by embedding AI capabilities directly within the database engine, streamlining data processing and insight generation without requiring separate AI infrastructure.

**Background and Purpose:**  
SQL Server 2025 arrives as part of Microsoft’s broader vision to modernize enterprise data platforms by combining traditional relational database management with advanced AI functionalities. The goal is to reduce complexity and latency in AI-driven data scenarios by enabling native AI model training, inference, and data processing within the database environment. This approach aligns with industry trends where data platforms are expected to support real-time analytics, machine learning, and intelligent automation natively.

**Specific Features and Detailed Changes:**  
- **Built-in AI Capabilities:** SQL Server 2025 integrates AI model training and inferencing directly into the database engine. This includes support for popular machine learning frameworks and pre-trained models, enabling users to run AI workloads close to the data without moving it externally.  
- **Enhanced Performance and Scalability:** Improvements in query processing, indexing, and storage optimize AI workloads alongside traditional OLTP and OLAP operations.  
- **Seamless Integration with Microsoft Fabric:** SQL Server 2025 is designed to work seamlessly with Microsoft Fabric, facilitating unified data governance, security, and analytics across hybrid and multi-cloud environments.  
- **Advanced Security Features:** Enhanced data protection mechanisms, including AI-driven anomaly detection for security threats and compliance monitoring, are embedded.  
- **Developer Productivity Enhancements:** New T-SQL extensions and APIs support AI model management and deployment, simplifying the development lifecycle for intelligent applications.

**Technical Mechanisms and Implementation Methods:**  
SQL Server 2025 leverages an extensible architecture that embeds AI runtimes within the database engine, allowing AI models to be stored, trained, and executed alongside relational data. The database engine supports containerized AI models and integrates with ONNX (Open Neural Network Exchange) format for interoperability. The system uses in-memory processing and GPU acceleration where available to optimize AI workloads. Additionally, the integration with Microsoft Fabric enables centralized metadata management and policy enforcement, ensuring consistent data governance.

**Use Cases and Application Scenarios:**  
- **Real-time Fraud Detection:** Financial institutions can deploy AI models within SQL Server to analyze transaction data in real time, identifying fraudulent patterns without data egress.  
- **Predictive Maintenance:** Manufacturing companies can integrate sensor data with AI models inside SQL Server to predict equipment failures and schedule maintenance proactively.  
- **Customer Insights and Personalization:** Retailers can leverage embedded AI to analyze customer behavior and personalize offers dynamically.  
- **Operational Analytics:** Enterprises can run complex analytics combining AI and relational data for supply chain optimization, risk assessment, and more.

**Important Considerations and Limitations:**  
- **Resource Management:** Running AI workloads within the database engine requires careful resource allocation to avoid impacting OLTP performance. Proper workload isolation and scaling strategies should be employed.  
- **Model Lifecycle Management:** While SQL Server 2025 supports AI model deployment, organizations must implement robust versioning, monitoring, and retraining processes.  
- **Compatibility:** Existing applications may require updates to leverage new AI capabilities and T-SQL extensions.  
- **Security Compliance:** Embedded AI features must be configured in accordance with organizational security policies and regulatory requirements.

**Integration with Related Azure Services:**  
SQL Server 2025’s integration with Microsoft Fabric enables unified data governance and analytics across Azure Synapse Analytics, Azure Data Factory, and Power BI, facilitating end-to-end data workflows. It also supports Azure Arc for hybrid deployments, allowing consistent management across on-premises, multi-cloud, and edge environments. Furthermore, integration with Azure Machine Learning services enables advanced model development and lifecycle management, complementing the in-database AI capabilities.

In summary, SQL Server 2025’s general availability introduces a transformative AI

---

### 82. Generally Available: Azure SQL updates for November 2025 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure SQL updates for November 2025 ](https://azure.microsoft.com/updates?id=522523)

**Update ID**: 522523
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**Summary**:

- What was updated  
In November 2025, Azure SQL introduced updates related to pricing and reservation discounts for Azure SQL Managed Instances.

- Key changes or new features  
The update enables customers to apply reservation discounts for 1-year or 3-year reservations of zone-redundant Azure SQL Managed Instances in the General Purpose tier. This discount now applies to both the standard compute and storage components, optimizing cost savings for reserved capacity in zone-redundant deployments.

- Target audience affected  
This update primarily affects IT professionals and developers managing Azure SQL Managed Instances, especially those leveraging zone-redundant configurations for high availability and disaster recovery in the General Purpose tier.

- Important notes if any  
Customers should evaluate their usage patterns to benefit from the new reservation discount applicability, potentially reducing costs for long-term, zone-redundant Azure SQL Managed Instances. This enhancement supports better budget planning and cost optimization strategies for enterprise workloads requiring zone redundancy.  

For more details, visit: https://azure.microsoft.com/updates?id=522523

**Details**:

In November 2025, Azure SQL introduced a significant update enabling customers to apply reservation discounts for 1-year or 3-year reservations of zone-redundant Azure SQL Managed Instances (MI) in the General Purpose tier, extending these discounts to both standard compute and storage components. This update aims to optimize cost management for enterprises leveraging high-availability configurations in Azure SQL Managed Instances.

**Background and Purpose:**  
Azure SQL Managed Instance offers a fully managed SQL Server experience with built-in high availability and zone redundancy to ensure resilience against datacenter failures. Prior to this update, reservation discounts—which provide cost savings by committing to long-term usage—were limited in scope and did not fully cover zone-redundant instances or all compute/storage components. The purpose of this update is to enhance cost predictability and reduce operational expenses for customers deploying zone-redundant General Purpose tier instances by allowing reservation discounts to be applied comprehensively.

**Specific Features and Detailed Changes:**  
- Reservation discounts now apply to zone-redundant Azure SQL Managed Instances in the General Purpose tier.  
- Discounts cover both standard compute and storage costs, which were previously billed separately and without reservation pricing benefits.  
- Supported reservation terms include 1-year and 3-year commitments, aligning with Azure’s existing reservation model.  
- This update does not currently extend to Business Critical tier or single-zone instances, focusing on zone-redundant General Purpose tier only.

**Technical Mechanisms and Implementation Methods:**  
Azure SQL Managed Instance in the General Purpose tier uses remote storage and leverages zone redundancy by replicating data synchronously across availability zones within an Azure region. The reservation discount mechanism integrates with Azure Reservations and billing systems, recognizing eligible zone-redundant MIs and applying the discounted rates automatically to both compute and storage usage. Customers can purchase reservations via the Azure portal, CLI, or API, specifying the zone-redundant General Purpose tier MI as the target resource. The billing engine then matches usage against the reservation to apply discounts in real time.

**Use Cases and Application Scenarios:**  
- Enterprises requiring high availability and disaster recovery within a single region can deploy zone-redundant General Purpose MIs and benefit from reduced costs through reservations.  
- Workloads with predictable, steady-state database usage—such as ERP systems, customer relationship management (CRM), and internal line-of-business applications—can optimize budget planning by committing to 1- or 3-year reservations.  
- Organizations seeking to balance cost and resilience without the premium of Business Critical tier can leverage this update to achieve zone redundancy at a more economical price point.

**Important Considerations and Limitations:**  
- Reservation discounts apply only to the General Purpose tier with zone redundancy; Business Critical tier and single-zone instances are excluded.  
- Reservations are region-specific and cannot be transferred across regions or tiers.  
- Early termination or cancellation of reservations is not supported; customers should carefully assess workload requirements before committing.  
- Pricing benefits apply only to the compute and standard storage components; additional features or add-ons may incur separate charges.  
- Customers should monitor usage to ensure reservation coverage matches actual consumption to maximize cost savings.

**Integration with Related Azure Services:**  
- Azure Reservations portal and APIs facilitate the purchase and management of these reservations.  
- Azure Cost Management and Billing tools can track reservation utilization and forecast savings.  
- Integration with Azure Monitor and Azure Advisor can provide recommendations on reservation purchases based on usage patterns.  
- This update complements Azure Availability Zones and Azure SQL’s built-in high availability features, enhancing both resilience and cost efficiency.

In summary, the November 2025 Azure SQL update extends reservation discount applicability to zone-redundant Managed Instances in the General Purpose tier, covering both compute and storage, thereby enabling IT professionals to achieve improved cost optimization for highly available SQL workloads within Azure. This enhancement supports strategic financial planning and operational efficiency for enterprise database deployments requiring zone-level resiliency.

---

### 83. Public Preview: Azure SQL updates for November 2025 

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Azure SQL updates for November 2025 ](https://azure.microsoft.com/updates?id=522514)

**Update ID**: 522514
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance

**Summary**:

- What was updated  
In November 2025, Azure SQL introduced an enhancement to the MSSQL extension for Visual Studio Code, enabling interactive data editing capabilities.

- Key changes or new features  
Developers can now view, modify, and insert rows directly within a table using a graphical Edit Data interface, eliminating the need to manually write T-SQL commands for these operations. This feature streamlines data manipulation workflows inside VS Code, improving productivity and reducing errors.

- Target audience affected  
This update primarily benefits developers and database administrators who use Visual Studio Code for managing Azure SQL databases, providing a more intuitive and efficient way to handle data editing tasks.

- Important notes if any  
The feature is currently in public preview, so users should test it in non-production environments and provide feedback. Familiarity with the MSSQL extension for VS Code is required to leverage this update effectively.

For more details, visit: https://azure.microsoft.com/updates?id=522514

**Details**:

The November 2025 public preview update for Azure SQL introduces an enhanced interactive Edit Data interface within the MSSQL extension for Visual Studio Code, enabling users to view, modify, and insert rows in database tables without manually writing T-SQL code. This update aims to streamline database management workflows by providing a more intuitive, code-free experience directly integrated into a popular developer environment.

**Background and Purpose:**  
Traditionally, managing data in Azure SQL databases requires writing T-SQL queries for CRUD (Create, Read, Update, Delete) operations, which can be time-consuming and error-prone, especially for users less familiar with T-SQL syntax. The update addresses this by embedding a graphical, interactive data editing experience into the MSSQL extension for VS Code, a widely used lightweight IDE. This aligns with Azure’s broader goal of improving developer productivity and lowering the barrier to database management.

**Specific Features and Detailed Changes:**  
- **Interactive Edit Data Interface:** Users can now open a table’s data grid directly within VS Code, enabling inline editing of existing rows and insertion of new rows without writing any SQL commands.  
- **Data Viewing:** The interface supports paging, sorting, and filtering to facilitate easy navigation through large datasets.  
- **Data Modification:** Changes made in the grid are translated into appropriate T-SQL statements executed behind the scenes, ensuring data integrity and transactional consistency.  
- **Insert Rows:** New rows can be added interactively, with the interface validating data types and constraints before submission.  
- **Seamless Integration:** This feature is embedded within the MSSQL extension, leveraging existing connection profiles and authentication methods, including Azure Active Directory and SQL authentication.

**Technical Mechanisms and Implementation Methods:**  
The Edit Data interface operates as a client-side grid component within VS Code, communicating with the Azure SQL database through the MSSQL extension’s established connection. When a user edits or inserts data, the extension dynamically generates parameterized T-SQL statements (e.g., UPDATE, INSERT) to apply changes. Validation occurs both client-side (to enforce data types and constraints) and server-side (to ensure referential integrity and trigger execution). The feature leverages VS Code’s extension API for UI rendering and event handling, while the MSSQL extension manages secure connectivity and command execution via the Tabular Data Stream (TDS) protocol.

**Use Cases and Application Scenarios:**  
- **Rapid Data Corrections:** Database administrators and developers can quickly fix data anomalies without switching tools or writing SQL.  
- **Ad-hoc Data Entry:** Business analysts or support staff with limited SQL knowledge can insert or update records directly.  
- **Development and Testing:** Developers can manipulate test data inline during development cycles, accelerating iteration.  
- **Education and Training:** New users learning Azure SQL can interact with data in a low-barrier environment, improving understanding.

**Important Considerations and Limitations:**  
- **Preview Status:** As a public preview feature, it may have limited support and could undergo significant changes before general availability.  
- **Performance:** Editing large datasets may be constrained by client resource limits and network latency; paging and filtering mitigate this.  
- **Security:** Users must have appropriate database permissions (e.g., UPDATE, INSERT) to modify data; audit logging and compliance remain the user’s responsibility.  
- **Complex Data Types:** Support for certain complex types (e.g., XML, JSON, spatial) or computed columns may be limited or require manual T-SQL.  
- **Transactional Scope:** Each edit or insert is typically executed as an individual transaction, which may impact multi-row atomicity.

**Integration with Related Azure Services:**  
- **Azure Active Directory:** Supports integrated authentication for secure access.  
- **Azure SQL Database and Managed Instance:** Fully compatible with both deployment models.  
- **Azure DevOps and CI/CD Pipelines:** While primarily a manual editing tool, it complements automated deployment workflows by enabling quick data fixes.  
- **Azure Monitor and Security

---

### 84. Public Preview: Dynamic sessions shell environment and MCP support in Azure Container Apps

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Dynamic sessions shell environment and MCP support in Azure Container Apps](https://azure.microsoft.com/updates?id=512949)

**Update ID**: 512949
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Container Apps introduced public preview support for dynamic shell sessions and Microsoft Container Platform (MCP) integration.

- Key changes or new features  
Dynamic shell sessions provide a platform-managed, built-in container that allows developers and operators to run shell commands in an isolated, sandboxed environment within their container apps. This enables on-demand troubleshooting, diagnostics, and management without needing to deploy additional containers or modify app configurations. Additionally, MCP support enhances container orchestration and management capabilities within Azure Container Apps.

- Target audience affected  
Developers and IT professionals managing containerized applications on Azure Container Apps who require streamlined debugging, operational control, and enhanced platform integration.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. The dynamic shell environment improves security by isolating shell sessions from the main app containers. Users should monitor Azure updates for GA announcements and any changes to session limits or permissions.  

For more details, visit: https://azure.microsoft.com/updates?id=512949

**Details**:

Azure Container Apps has introduced a public preview feature enabling dynamic shell sessions and Managed Control Plane (MCP) support, enhancing operational flexibility and management capabilities for containerized applications. This update addresses the need for streamlined, secure, and interactive troubleshooting and management within containerized environments without requiring users to pre-provision debugging containers or expose additional endpoints.

**Background and Purpose**  
Azure Container Apps is a serverless container service designed to simplify deploying microservices and containerized applications without managing complex infrastructure. Traditionally, debugging or running shell commands inside container apps required either embedding debugging tools within the container image or exposing additional management endpoints, which can increase attack surface and operational overhead. The introduction of dynamic shell sessions provides a secure, ephemeral, and platform-managed environment to execute shell commands on running container apps, improving developer productivity and operational agility.

**Specific Features and Detailed Changes**  
- **Dynamic Shell Sessions:** Users can initiate shell sessions dynamically on running container app instances. These sessions run in isolated, sandboxed containers managed by the platform, separate from the application containers, ensuring no interference with application workloads.  
- **Managed Control Plane (MCP) Support:** This feature enhances control plane capabilities by enabling better lifecycle management and orchestration of these dynamic shell environments. MCP manages session creation, isolation, and teardown, ensuring secure and efficient resource utilization.  
- **Public Preview Availability:** The feature is currently in public preview, allowing users to test and provide feedback while Microsoft continues to refine security, performance, and integration aspects.

**Technical Mechanisms and Implementation**  
The dynamic shell environment leverages Azure Container Apps’ underlying Kubernetes-based infrastructure and integrates with Azure’s control plane to provision ephemeral containers on demand. When a shell session is requested, the MCP orchestrates the creation of a sandbox container with a minimal shell environment, isolated via Kubernetes namespaces and network policies to prevent lateral movement or data leakage. The shell session container shares the same network and storage context as the target container app instance to allow meaningful interaction, such as inspecting logs, environment variables, or running diagnostic commands. Once the session ends, the container is automatically destroyed, ensuring no residual state or security risks.

**Use Cases and Application Scenarios**  
- **On-Demand Debugging:** Developers and operators can troubleshoot live container apps without modifying application images or redeploying.  
- **Operational Diagnostics:** Quickly run diagnostic commands or scripts to analyze application health, configuration, or runtime environment.  
- **Security Auditing:** Perform security checks or verify compliance by inspecting container environments dynamically.  
- **Automation and CI/CD Integration:** Integrate shell session commands into automation pipelines for advanced deployment or monitoring tasks.

**Important Considerations and Limitations**  
- As a public preview feature, dynamic shell sessions may have limited regional availability and could undergo breaking changes before general availability.  
- Security best practices must be followed; access to shell sessions should be tightly controlled via Azure RBAC and network policies to prevent unauthorized access.  
- Performance impact is minimal but depends on session duration and command complexity; ephemeral containers consume compute resources temporarily.  
- Currently, the shell environment is minimal and may not include all tools; users may need to customize container images or rely on built-in utilities.

**Integration with Related Azure Services**  
- **Azure Monitor and Log Analytics:** Shell sessions can be used in conjunction with monitoring tools to diagnose issues detected by alerts or logs.  
- **Azure DevOps and GitHub Actions:** Automate shell session commands as part of CI/CD workflows for deployment validation or environment checks.  
- **Azure Active Directory (AAD):** Leverages AAD for authentication and authorization to control access to shell sessions.  
- **Azure Policy:** Enforce governance policies around who can initiate shell sessions and under what conditions.

In summary, the introduction of dynamic shell sessions and MCP support in Azure Container Apps public preview provides a secure, efficient, and flexible mechanism for interactive container management and troubleshooting, significantly enhancing operational capabilities while maintaining the serverless and managed nature of the

---

### 85. Public Preview: Deployment labels in Azure Container Apps

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: Deployment labels in Azure Container Apps](https://azure.microsoft.com/updates?id=512900)

**Update ID**: 512900
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Azure Container Apps, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Container Apps introduced deployment labels as a new deployment mode, now available in public preview.

- Key changes or new features  
Deployment labels allow developers and IT professionals to assign meaningful, custom names to different deployments within a Container App environment. This enhancement simplifies environment management by making deployments easier to identify and track. It also enables advanced deployment strategies such as blue-green and canary deployments by providing clearer visibility and control over deployment versions and stages.

- Target audience affected  
Developers and IT professionals managing containerized applications on Azure Container Apps who require streamlined deployment workflows and improved environment organization.

- Important notes if any  
As this feature is in public preview, it is recommended to test deployment labels in non-production environments before adopting them in critical workloads. Users should monitor Azure updates for GA announcements and any changes to feature capabilities or limitations.

**Details**:

The recent public preview update for Azure Container Apps introduces deployment labels as a new deployment mode, aimed at enhancing environment management and enabling sophisticated deployment strategies. This feature allows users to assign meaningful, customizable labels to deployments within Azure Container Apps, thereby improving the organization, tracking, and control of application deployments.

**Background and Purpose:**  
Azure Container Apps is a serverless container hosting service designed to simplify microservices and containerized application deployment without managing infrastructure. Prior to this update, deployment management primarily relied on default system-generated identifiers, which limited clarity and flexibility in complex environments. The introduction of deployment labels addresses this gap by providing a mechanism to tag deployments with human-readable, descriptive identifiers. This facilitates better environment segmentation, version control, and deployment tracking, especially in multi-environment or multi-stage pipelines.

**Specific Features and Detailed Changes:**  
- **Deployment Labels:** Users can now assign custom labels (key-value pairs) to each deployment, which serve as metadata to identify and categorize deployments.  
- **Label-Based Deployment Mode:** This mode allows deployments to be referenced and managed via their labels rather than opaque system IDs.  
- **Improved Deployment Visibility:** Labels enhance the ability to filter, search, and audit deployments within the Azure Portal, CLI, or API.  
- **Support for Advanced Deployment Strategies:** Labels enable implementation of strategies such as blue-green deployments, canary releases, and environment-specific rollouts by clearly distinguishing deployment instances.

**Technical Mechanisms and Implementation Methods:**  
Deployment labels are implemented as metadata tags attached to deployment resources within the Azure Container Apps control plane. When creating or updating a deployment via Azure CLI, ARM templates, or the Azure Portal, users specify label key-value pairs. The Azure Container Apps service stores these labels alongside deployment metadata, allowing the deployment engine and management APIs to reference deployments by label. This metadata-driven approach integrates with existing deployment workflows, enabling programmatic querying and conditional deployment logic based on labels.

**Use Cases and Application Scenarios:**  
- **Environment Segmentation:** Assign labels such as `environment=staging` or `environment=production` to clearly separate deployments across different lifecycle stages.  
- **Version Tracking:** Use labels like `version=1.2.3` to track application versions deployed in each environment.  
- **Deployment Strategy Implementation:** Facilitate blue-green or canary deployments by labeling active and standby deployments distinctly, enabling seamless traffic switching and rollback.  
- **Audit and Compliance:** Labels provide an audit trail for deployments, improving governance and operational transparency.

**Important Considerations and Limitations:**  
- As this feature is in public preview, it may be subject to changes and should not be used in critical production environments without thorough testing.  
- Label key-value pairs should follow Azure’s tagging conventions and size limits to ensure compatibility.  
- Integration with existing CI/CD pipelines may require updates to deployment scripts and tooling to leverage label-based deployment references.  
- Some Azure Container Apps features or third-party tools may not yet fully support deployment labels, requiring validation before adoption.

**Integration with Related Azure Services:**  
Deployment labels in Azure Container Apps complement Azure DevOps and GitHub Actions by enabling more granular deployment targeting and tracking within CI/CD workflows. They also integrate with Azure Monitor and Azure Policy by allowing filtering and policy enforcement based on deployment metadata. Additionally, labels can be leveraged in Azure Resource Graph queries for comprehensive inventory and compliance reporting across container app deployments.

In summary, the deployment labels feature in Azure Container Apps public preview introduces a metadata-driven approach to deployment management, enhancing clarity, control, and flexibility for containerized application deployments. This update empowers IT professionals to implement advanced deployment strategies and improve operational governance through meaningful deployment identification and segmentation.

---

### 86. Generally Available: Rule-based routing in Azure Container Apps

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Rule-based routing in Azure Container Apps](https://azure.microsoft.com/updates?id=512850)

**Update ID**: 512850
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Container Apps now generally support rule-based routing.

- Key changes or new features  
This feature enables routing traffic based on customizable rules, allowing developers to direct requests to different container app revisions or services. It simplifies microservices architecture by supporting scenarios like A/B testing, blue-green deployments, and canary releases without additional infrastructure. Rule conditions can be defined using HTTP headers, query parameters, or other request attributes, enhancing traffic management flexibility.

- Target audience affected  
Developers building microservices and IT professionals managing containerized applications on Azure Container Apps will benefit from easier deployment strategies and improved traffic control.

- Important notes if any  
Rule-based routing is fully supported and production-ready, encouraging adoption for progressive delivery patterns. Users should review routing rules carefully to avoid unintended traffic flows and ensure proper testing before production rollout.

For more details, visit: https://azure.microsoft.com/updates?id=512850

**Details**:

The general availability of rule-based routing in Azure Container Apps introduces a powerful mechanism to direct incoming traffic based on customizable rules, enhancing microservice architecture flexibility and deployment strategies. This update addresses the need for more granular traffic management within containerized applications without requiring complex external routing infrastructure.

**Background and Purpose**  
Azure Container Apps is a fully managed serverless container service designed to run microservices and containerized applications with ease. Prior to this update, routing traffic between different revisions or versions of container apps was limited to simple percentage-based splits. The introduction of rule-based routing aims to provide developers and operators with more precise control over traffic distribution, enabling scenarios such as targeted A/B testing, canary deployments, and blue-green deployments directly within the platform. This reduces operational complexity and accelerates deployment workflows.

**Specific Features and Detailed Changes**  
Rule-based routing allows users to define routing rules based on HTTP request attributes such as headers, query parameters, and cookies. These rules can be configured to route traffic to specific container app revisions or versions. Key features include:

- **Header-based routing:** Route requests based on the presence or value of HTTP headers.
- **Query parameter routing:** Direct traffic depending on query string parameters.
- **Cookie-based routing:** Enable session affinity or user-specific routing by inspecting cookies.
- **Combination of rules:** Multiple conditions can be combined using logical operators for complex routing logic.
- **Fallback routing:** Define default routes if no rules match.

This feature is integrated into the Azure Container Apps environment, allowing seamless configuration through Azure CLI, ARM templates, or the Azure portal.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Container Apps leverages its built-in Envoy-based ingress controller to implement rule-based routing. Envoy proxies incoming HTTP requests and evaluates them against the defined routing rules. The rules are stored as part of the container app revision configuration and dynamically applied without requiring redeployment of the app itself.

Users define routing rules as part of the container app revision’s ingress configuration, specifying match conditions and target revisions. The platform’s control plane translates these rules into Envoy configurations, which are then enforced at the edge of the container app environment. This approach ensures low latency and high reliability in traffic routing.

**Use Cases and Application Scenarios**  
- **A/B Testing:** Route a subset of users to a new feature version based on headers or cookies to gather performance and usability data before full rollout.  
- **Blue-Green Deployments:** Seamlessly switch traffic between stable and new app revisions by defining routing rules that direct all traffic to the desired version.  
- **Canary Releases:** Gradually increase traffic to a new revision by adjusting routing rules based on query parameters or headers.  
- **Multi-tenant Routing:** Route requests to different container app revisions based on tenant identifiers in headers or cookies.  
- **Session Affinity:** Maintain user sessions by routing based on cookies, improving user experience in stateful applications.

**Important Considerations and Limitations**  
- Rule-based routing applies only to HTTP traffic managed by the container app ingress; non-HTTP protocols are not supported.  
- Complex routing logic should be carefully tested to avoid unintended traffic distribution.  
- Overly granular rules may increase configuration complexity and maintenance overhead.  
- Rate limiting and security policies should be considered in conjunction with routing rules to ensure consistent application behavior.  
- This feature requires the container app to have ingress enabled and configured.

**Integration with Related Azure Services**  
Rule-based routing in Azure Container Apps complements other Azure services such as:

- **Azure Monitor and Application Insights:** For monitoring traffic patterns and validating routing effectiveness during deployments.  
- **Azure DevOps and GitHub Actions:** To automate deployment pipelines that update routing rules as part of CI/CD workflows.  
- **Azure Front Door or Azure Application Gateway:** For global routing and advanced WAF capabilities, which can be combined with container app routing for layered traffic management.  
- **Azure Key Vault:** To

---

### 87. Generally Available: Premium Ingress in Azure Container Apps

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Premium Ingress in Azure Container Apps](https://azure.microsoft.com/updates?id=512813)

**Update ID**: 512813
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Container Apps, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Container Apps now generally support Premium Ingress, enabling enhanced environment-level ingress configuration.

- Key changes or new features  
Premium Ingress introduces customizable ingress scaling, allowing developers and IT professionals to define scaling behaviors specifically for ingress traffic. This improves application responsiveness and resource utilization under varying load conditions. The feature supports more granular control over ingress performance and availability, enhancing the management of external traffic to containerized applications.

- Target audience affected  
Developers building containerized applications on Azure Container Apps and IT professionals managing container app environments will benefit from this update. It is particularly relevant for those requiring advanced ingress traffic management and scaling capabilities.

- Important notes if any  
This feature is now generally available, meaning it is fully supported for production workloads. Users should review their ingress configurations to leverage the new scaling options effectively. Additional documentation and best practices are available to guide implementation.  

For detailed information, visit: https://azure.microsoft.com/updates?id=512813

**Details**:

The Azure Container Apps service has reached a significant milestone with the general availability of Premium Ingress, introducing advanced environment-level ingress configuration and customizable ingress scaling capabilities. This update addresses the need for more granular traffic management and scaling control in containerized microservices architectures.

**Background and Purpose**  
Azure Container Apps is a serverless container hosting service designed for microservices and containerized applications, abstracting infrastructure management while providing built-in scaling and networking features. Prior to this update, ingress configuration was relatively basic, limiting fine-tuned control over how incoming traffic is managed and scaled. The Premium Ingress feature was introduced to enhance operational flexibility and performance by enabling environment-wide ingress settings and more sophisticated scaling options, thereby improving application responsiveness and resource efficiency.

**Specific Features and Detailed Changes**  
- **Environment-Level Ingress Configuration:** Instead of configuring ingress on a per-app basis, Premium Ingress allows ingress settings to be applied at the environment level. This simplifies management when multiple container apps share the same ingress endpoint or domain.  
- **Customizable Ingress Scaling:** The most notable enhancement is the ability to customize ingress scaling parameters independently from the app’s internal scaling. This means the ingress layer can scale based on traffic patterns, providing better handling of sudden spikes or sustained high loads without over-provisioning the app instances themselves.  
- **Improved Traffic Routing and Load Balancing:** Premium Ingress supports more advanced routing rules and load balancing capabilities, enabling scenarios such as path-based routing, weighted traffic distribution, and sticky sessions if needed.  
- **Enhanced Security and TLS Management:** The update includes better integration with TLS certificates and Azure-managed certificates, facilitating secure HTTPS ingress with simplified certificate lifecycle management.

**Technical Mechanisms and Implementation Methods**  
Premium Ingress leverages Azure’s underlying Application Gateway and Front Door technologies to provide a robust ingress layer. The environment-level ingress configuration abstracts these components, allowing users to define ingress rules declaratively via Azure CLI, ARM templates, or Bicep. Customizable scaling is implemented through integration with Azure Monitor metrics and KEDA (Kubernetes Event-driven Autoscaling), enabling the ingress controller to scale out or in based on HTTP request rates, latency, or other custom metrics. This decouples ingress scaling from container app replica scaling, optimizing resource utilization.

**Use Cases and Application Scenarios**  
- **Microservices Architectures:** Environments hosting multiple container apps benefit from unified ingress management, reducing operational overhead.  
- **High-Traffic Applications:** Applications experiencing variable or unpredictable traffic patterns can leverage customizable ingress scaling to maintain performance without unnecessary resource consumption.  
- **Multi-Tenant SaaS Platforms:** Premium Ingress supports complex routing rules required for tenant isolation and traffic segmentation.  
- **Secure Public-Facing APIs:** Simplified TLS management and enhanced security features make it easier to expose APIs securely to external clients.

**Important Considerations and Limitations**  
- Premium Ingress may incur additional costs due to the use of higher-tier networking components and scaling resources.  
- Some legacy ingress configurations might require adjustments to align with environment-level settings.  
- The feature currently supports HTTP/HTTPS protocols; other protocols are not supported through this ingress layer.  
- Users should carefully plan scaling thresholds and metrics to avoid over-scaling or throttling under load.

**Integration with Related Azure Services**  
Premium Ingress integrates seamlessly with Azure Monitor for metrics and alerting, Azure Key Vault for secure certificate storage, and Azure Front Door or Application Gateway for advanced traffic management. It also works in conjunction with Azure DevOps and GitHub Actions for CI/CD pipelines, enabling automated deployment and configuration of ingress settings. Additionally, it complements Azure API Management when exposing APIs requiring advanced ingress capabilities.

In summary, the general availability of Premium Ingress in Azure Container Apps significantly enhances ingress management by providing environment-level configuration and customizable ingress scaling, enabling IT professionals to build more resilient, scalable, and secure containerized applications with simplified operational control.

---

### 88. Public Preview: JWT Validation in Azure Application Gateway

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Public Preview: JWT Validation in Azure Application Gateway](https://azure.microsoft.com/updates?id=489855)

**Update ID**: 489855
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Application Gateway now supports public preview of JSON Web Token (JWT) validation, allowing authentication and token validation at the gateway layer.

- Key changes or new features  
Developers and IT professionals can configure Azure Application Gateway to validate JWTs on incoming requests before forwarding traffic to backend applications or APIs. This offloads authentication tasks from backend services, improving security posture and reducing backend processing overhead. The feature supports validation of token issuer, audience, signature, and expiration. It integrates seamlessly with existing Application Gateway configurations.

- Target audience affected  
This update primarily impacts developers building APIs and web applications, as well as IT professionals managing Azure networking and security infrastructure who want to enforce authentication policies closer to the edge.

- Important notes if any  
As this feature is in public preview, it should be used with caution in production environments. Users should review the preview limitations and provide feedback to Microsoft. Proper configuration of JWT validation parameters is critical to avoid unintended access issues.  

For more details, visit: https://azure.microsoft.com/updates?id=489855

**Details**:

The recent public preview of JSON Web Token (JWT) validation in Azure Application Gateway introduces a significant enhancement by enabling authentication and token validation directly at the gateway layer, before requests reach backend applications or APIs. This update addresses the growing need for centralized, scalable, and secure token-based authentication in modern cloud architectures.

**Background and Purpose**  
As organizations increasingly adopt microservices and API-driven architectures, securing APIs with token-based authentication such as JWT has become standard practice. Traditionally, JWT validation is implemented within backend services or API management layers, which can lead to duplicated logic, increased latency, and inconsistent security enforcement. By integrating JWT validation into Azure Application Gateway, Microsoft aims to offload token verification from backend services, reduce attack surface, and streamline security management at the edge.

**Specific Features and Detailed Changes**  
- **JWT Validation at the Gateway**: Application Gateway can now validate JWT tokens embedded in HTTP headers or query parameters against configured issuer, audience, and signature parameters.  
- **Configurable Validation Parameters**: Users can specify trusted issuers, audiences, token signing keys (via OpenID Connect metadata endpoints), and token claim requirements.  
- **Pre-authentication Enforcement**: Requests with invalid or missing tokens can be blocked or redirected before reaching backend pools.  
- **Integration with WAF Policies**: JWT validation can be combined with Web Application Firewall (WAF) rules to provide layered security.  
- **Support for Multiple JWT Configurations**: Enables different validation rules per listener or path-based routing rules, supporting complex multi-tenant or multi-API scenarios.

**Technical Mechanisms and Implementation Methods**  
The JWT validation feature leverages the Application Gateway’s Layer 7 (HTTP/HTTPS) processing capabilities. Upon receiving a request, the gateway extracts the JWT from the configured location (e.g., Authorization header), then performs cryptographic signature verification using public keys obtained from the issuer’s OpenID Connect metadata endpoint. It validates token claims such as issuer (`iss`), audience (`aud`), expiry (`exp`), and optionally custom claims. If validation fails, the gateway returns an HTTP 401 Unauthorized or other configured response, preventing the request from reaching backend resources. Configuration is done via Azure Resource Manager (ARM) templates, Azure CLI, or Azure Portal, under the Application Gateway’s HTTP settings or listener rules.

**Use Cases and Application Scenarios**  
- **API Security at the Edge**: Protect RESTful APIs by validating JWT tokens at the gateway, reducing backend complexity.  
- **Microservices Architectures**: Centralize authentication for multiple services behind a single Application Gateway instance.  
- **Multi-Tenant SaaS Platforms**: Apply distinct JWT validation policies per tenant or API path.  
- **Zero Trust Security Models**: Enforce strict token validation as part of a defense-in-depth strategy.  
- **Integration with Azure AD and Other Identity Providers**: Validate tokens issued by Azure Active Directory, Auth0, or other OpenID Connect-compliant providers.

**Important Considerations and Limitations**  
- **Preview Status**: As a public preview, this feature may have limited SLA and could undergo changes before general availability.  
- **Performance Impact**: JWT validation adds processing overhead at the gateway; performance testing is recommended for high-throughput scenarios.  
- **Token Size and Complexity**: Large or complex tokens may affect latency; consider token optimization.  
- **Limited to HTTP/HTTPS Traffic**: JWT validation applies only to web traffic routed through Application Gateway.  
- **No Native Token Issuance**: The gateway validates tokens but does not issue or refresh JWTs; integration with identity providers remains necessary.

**Integration with Related Azure Services**  
- **Azure Active Directory (Azure AD)**: Seamlessly validate Azure AD-issued tokens for enterprise applications.  
- **Azure API Management (APIM)**: While APIM also supports JWT validation, Application Gateway’s feature allows offloading validation closer to the edge, potentially in

---

### 89. Generally Available: Azure Application Gateway mTLS passthrough support

**Published**: November 18, 2025 17:01:02 UTC
**Link**: [Generally Available: Azure Application Gateway mTLS passthrough support](https://azure.microsoft.com/updates?id=488990)

**Update ID**: 488990
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Features, Services, Microsoft Ignite

**Summary**:

- What was updated  
Azure Application Gateway now generally supports mTLS passthrough for backend applications.

- Key changes or new features  
This update enables backend services to perform client certificate validation and authorization header checks directly, while still allowing the Web Application Firewall (WAF) to inspect incoming web traffic. Previously, mTLS termination at the gateway prevented backend apps from accessing client certificates. With mTLS passthrough, the gateway forwards encrypted traffic, preserving end-to-end client authentication and authorization capabilities alongside WAF protection.

- Target audience affected  
Developers and IT professionals managing secure web applications that require mutual TLS authentication and advanced traffic inspection via Azure Application Gateway and WAF.

- Important notes if any  
This feature is now generally available, ensuring production readiness and support. It simplifies architectures where backend services need to validate client certificates without sacrificing security monitoring by WAF. Users should verify compatibility with their backend applications and update configurations accordingly to leverage mTLS passthrough.  

For more details, visit: https://azure.microsoft.com/updates?id=488990

**Details**:

The Azure Application Gateway mTLS passthrough support feature, now generally available, enhances secure communication by enabling backend applications to perform mutual TLS (mTLS) client certificate validation and authorization header inspection directly, while still allowing the Application Gateway’s Web Application Firewall (WAF) to inspect incoming web traffic. This update addresses a common challenge in scenarios where backend services require end-to-end client authentication via mTLS, but organizations also want to leverage the Application Gateway’s WAF capabilities for centralized security enforcement.

**Background and Purpose**  
Traditionally, Azure Application Gateway supports TLS termination at the gateway, which decrypts incoming traffic and forwards it to backend pools over HTTP or HTTPS. While this enables WAF inspection of decrypted traffic, it breaks end-to-end TLS, making it impossible for backend applications to perform client certificate validation in mTLS scenarios. Prior to this update, customers had to choose between terminating TLS at the gateway (enabling WAF but losing backend mTLS) or passing encrypted traffic through (preserving mTLS but losing WAF inspection). The mTLS passthrough support resolves this trade-off by allowing the gateway to forward encrypted mTLS traffic to backend pools while still inspecting the traffic at the gateway level.

**Specific Features and Detailed Changes**  
- **mTLS Passthrough Mode:** Application Gateway can now be configured to forward encrypted TLS traffic that includes client certificates directly to backend servers without terminating TLS at the gateway.  
- **WAF Inspection with mTLS Passthrough:** Despite passthrough, the WAF engine inspects the traffic by leveraging TLS record layer inspection and selective decryption techniques, enabling detection of threats and enforcement of WAF policies.  
- **Authorization Header Validation:** Backend applications can validate authorization headers and client certificates as usual, since the TLS session is end-to-end between client and backend.  
- **Seamless Integration:** This feature is supported on both v2 SKU Application Gateway and integrates with existing WAF policies and backend pool configurations.

**Technical Mechanisms and Implementation Methods**  
The core technical mechanism involves the Application Gateway operating in a passthrough mode for TLS connections that use client certificates. Instead of terminating TLS, the gateway forwards the encrypted TLS stream to backend servers, preserving the client certificate exchange. Meanwhile, the WAF component uses deep packet inspection techniques on the TLS record layer metadata and selectively decrypts traffic where possible (e.g., for non-mTLS requests) to apply security policies. Configuration involves enabling mTLS passthrough on the listener and associating backend pools that support mTLS client certificate validation.

**Use Cases and Application Scenarios**  
- **Financial Services and Healthcare:** Where backend services require strict client authentication via mTLS for compliance and security, while still needing centralized WAF protection.  
- **APIs with Client Certificate Authentication:** APIs that enforce client certificate validation at the backend can now be fronted by Application Gateway without losing WAF capabilities.  
- **Hybrid Security Architectures:** Organizations wanting layered security—end-to-end client authentication plus perimeter WAF inspection—benefit from this feature.  
- **Multi-tenant SaaS Platforms:** Where tenant-specific client certificates are validated at backend microservices, with Application Gateway providing unified security enforcement.

**Important Considerations and Limitations**  
- **Backend Compatibility:** Backend servers must be configured to handle mTLS and client certificate validation properly.  
- **Performance Impact:** Passthrough mode may have different performance characteristics; testing is recommended.  
- **WAF Policy Scope:** Some WAF rules that depend on full TLS termination and payload inspection may have limited effectiveness in passthrough mode.  
- **Logging and Diagnostics:** Enhanced logging should be enabled to monitor mTLS traffic and WAF actions.  
- **Supported Protocols:** Currently supports TLS 1.2 and above; legacy protocols may not be supported.

**Integration with Related Azure Services**  
- **Azure Key Vault:** For secure storage and management of backend certificates used in mTLS.

---

### 90. Public Preview: Azure Copilot observability agent

**Published**: November 18, 2025 16:30:36 UTC
**Link**: [Public Preview: Azure Copilot observability agent](https://azure.microsoft.com/updates?id=528538)

**Update ID**: 528538
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Microsoft announced the public preview of the Azure Copilot observability agent, a new tool designed to enhance intelligent observability across Azure resources.

- Key changes or new features  
The Azure Copilot observability agent provides proactive, scalable monitoring by collecting telemetry and delivering actionable insights when services underperform. It integrates AI-driven analysis to move beyond reactive troubleshooting, enabling faster identification and resolution of issues. The agent supports broad resource coverage and aims to simplify cloud operations through intelligent diagnostics and recommendations.

- Target audience affected  
This update primarily targets cloud operations teams, IT professionals, and developers responsible for maintaining and optimizing Azure environments who require advanced observability and troubleshooting capabilities.

- Important notes if any  
The Azure Copilot observability agent is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Integration details and supported resource types are available in the official documentation. Users should monitor updates for GA release and feature enhancements.

For more details, visit: https://azure.microsoft.com/updates?id=528538

**Details**:

The Azure Copilot observability agent, now available in public preview, addresses the growing need for proactive and intelligent observability in cloud operations by providing a scalable, AI-driven monitoring solution that delivers actionable insights across diverse Azure resources. Traditional reactive troubleshooting approaches often fall short in complex, dynamic cloud environments where early detection and context-aware analysis are critical. This update introduces an observability agent designed to integrate deeply with Azure Copilot’s AI capabilities, enabling automated anomaly detection, performance diagnostics, and guided remediation recommendations.

From a feature perspective, the Azure Copilot observability agent collects telemetry data—metrics, logs, and traces—from a wide range of Azure services and on-premises resources, normalizing and correlating this data to provide a unified observability experience. It leverages AI models embedded within Azure Copilot to analyze this telemetry in near real-time, identifying patterns and deviations that indicate potential issues before they impact end users. The agent supports customizable alerting rules and integrates with Azure Monitor, Azure Log Analytics, and Azure Metrics Explorer for seamless visualization and alert management. Additionally, it offers contextual insights that link detected anomalies to probable root causes and suggests actionable next steps, reducing mean time to resolution (MTTR).

Technically, the observability agent is deployed as a lightweight, containerized service or as an extension on virtual machines and Kubernetes clusters. It uses secure, encrypted communication channels to transmit telemetry data to Azure Monitor backend services, where AI-driven analytics are performed. The agent employs adaptive sampling and data compression to optimize network usage and minimize performance overhead on monitored resources. Its modular architecture allows for extensibility and integration with custom telemetry sources via APIs. Configuration and management are facilitated through Azure Policy and Azure Resource Manager templates, enabling automated, scalable deployment across large environments.

Use cases for the Azure Copilot observability agent include proactive monitoring of multi-cloud and hybrid infrastructures, automated detection of performance bottlenecks in microservices architectures, and intelligent alerting for mission-critical applications. IT operations teams can leverage the agent to gain end-to-end visibility into application dependencies, correlate infrastructure health with application performance, and receive AI-powered recommendations that prioritize remediation efforts based on business impact. This capability is particularly valuable in DevOps and SRE workflows where continuous monitoring and rapid incident response are essential.

Important considerations include the current public preview status, which may entail limited SLA guarantees and evolving feature sets. Organizations should evaluate the agent’s compatibility with their existing monitoring tools and data retention policies. Privacy and compliance aspects must be reviewed, especially when telemetry includes sensitive information, as data is processed by Azure AI services. Performance impact on monitored resources should be assessed during pilot deployments, and network bandwidth usage monitored to avoid unintended costs.

Integration with related Azure services is a key strength of this update. The observability agent works natively with Azure Monitor’s data ingestion and analytics pipelines, enhancing existing dashboards and alerting frameworks. It complements Azure Application Insights by adding infrastructure-level context and AI-driven diagnostics. Integration with Azure Security Center can provide correlated security and performance insights, while Azure Automation can consume Copilot’s remediation suggestions to trigger automated runbooks. Furthermore, the agent’s telemetry data can feed into Azure Sentinel for unified security and operational monitoring.

In summary, the Azure Copilot observability agent public preview introduces an AI-enhanced, scalable observability solution that empowers IT professionals to move beyond reactive troubleshooting toward intelligent, proactive cloud operations, integrating seamlessly with Azure’s monitoring ecosystem to deliver actionable insights and improve operational efficiency.

---

### 91. Private Preview: ActiveMQ and JMS connector for Azure Logic Apps

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Private Preview: ActiveMQ and JMS connector for Azure Logic Apps](https://azure.microsoft.com/updates?id=531783)

**Update ID**: 531783
**Data source**: Azure Updates API

**Categories**: In development, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps now includes a private preview of the ActiveMQ and JMS connector.

- Key changes or new features  
This new connector enables seamless integration with enterprise messaging systems based on ActiveMQ and JMS protocols. It supports advanced hybrid integration scenarios by allowing Logic Apps workflows to send and receive messages from these messaging brokers. This expands Logic Apps’ connectivity beyond Azure-native services, facilitating hybrid cloud and on-premises messaging integration.

- Target audience affected  
Developers and IT professionals working on enterprise integration, hybrid cloud architectures, and messaging workflows will benefit from this update. Those leveraging Azure Logic Apps for orchestrating business processes that require connectivity to ActiveMQ or JMS-based systems will find this particularly useful.

- Important notes if any  
The feature is currently in private preview, so access requires enrollment and approval from Microsoft. Users should expect potential limitations and ongoing improvements during this phase. Feedback from preview participants will help shape the final release. For more details and to request access, visit the official Azure update link.

**Details**:

The recent Azure update announces the private preview of the ActiveMQ and JMS connector for Azure Logic Apps, enabling seamless integration with enterprise messaging systems based on ActiveMQ and Java Message Service (JMS) protocols. This enhancement addresses the growing need for hybrid integration solutions that bridge on-premises or third-party messaging infrastructures with cloud-native workflows.

**Background and Purpose**  
Azure Logic Apps is a cloud-based integration platform that allows IT professionals to automate workflows and connect disparate systems through prebuilt connectors. Many enterprises rely on messaging middleware such as ActiveMQ and JMS for asynchronous communication and decoupling of distributed applications. Prior to this update, direct integration with these messaging systems required custom connectors or complex workarounds. The introduction of the ActiveMQ/JMS connector in private preview aims to simplify and standardize connectivity, accelerating hybrid integration scenarios where on-premises or third-party message brokers must interact with Azure services.

**Specific Features and Detailed Changes**  
The connector supports core JMS operations including sending, receiving, and peeking messages from queues and topics. It provides native support for JMS 1.1 and ActiveMQ protocols, enabling Logic Apps to participate directly in enterprise messaging workflows. Key features include:  
- Triggering Logic Apps workflows based on incoming JMS messages.  
- Sending messages to JMS queues or topics as part of automation processes.  
- Support for message properties, headers, and correlation IDs to maintain message context.  
- Configuration options for connection parameters such as broker URL, authentication credentials, and SSL settings.  
- Compatibility with both queue-based point-to-point and topic-based publish-subscribe messaging patterns.

**Technical Mechanisms and Implementation Methods**  
The connector operates as a managed Logic Apps connector that abstracts the JMS client APIs, providing a declarative interface for workflow designers. It leverages the JMS client libraries under the hood to establish connections to ActiveMQ brokers using standard protocols (OpenWire, AMQP, or MQTT depending on broker configuration). Authentication can be configured using username/password or certificate-based methods if supported by the broker. The connector manages message serialization and deserialization, allowing payloads in common formats such as JSON, XML, or plain text. Logic Apps designers can configure triggers and actions within the Logic Apps Designer UI or via ARM templates and API calls for automation.

**Use Cases and Application Scenarios**  
- Hybrid integration where on-premises ActiveMQ brokers relay messages to cloud-based Logic Apps for processing, orchestration, or routing.  
- Migrating legacy JMS-based workflows to Azure by incrementally integrating Logic Apps without replacing existing messaging infrastructure.  
- Event-driven automation where JMS messages trigger business workflows such as order processing, inventory updates, or alerting systems.  
- Multi-cloud or multi-platform messaging scenarios where ActiveMQ brokers in different environments connect to centralized Azure Logic Apps for unified orchestration.  
- Enriching JMS messages with data from other Azure services (e.g., Azure Functions, Cosmos DB) within Logic Apps workflows.

**Important Considerations and Limitations**  
- As a private preview feature, the connector may have limited availability and could undergo significant changes before general availability. Access requires enrollment in the preview program.  
- Performance and scalability characteristics depend on the underlying broker and network latency; testing is recommended for high-throughput scenarios.  
- The connector currently supports JMS 1.1; JMS 2.0 features may not be available.  
- Security configurations must be carefully managed, especially when connecting to on-premises brokers across network boundaries.  
- Error handling and retry policies should be explicitly configured in Logic Apps to handle transient connectivity or message processing failures.  
- Documentation and support resources may be limited during the preview phase.

**Integration with Related Azure Services**  
The ActiveMQ/JMS connector complements other Azure integration services such as Azure Service Bus, Event Grid, and API Management by enabling Logic Apps to act as a bridge between traditional JMS messaging and modern cloud-native event-driven architectures. It can be combined with Azure Functions for custom processing, Azure Monitor for

---

### 92. Public Preview: New healthcare connectors for Azure Logic Apps

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: New healthcare connectors for Azure Logic Apps](https://azure.microsoft.com/updates?id=531778)

**Update ID**: 531778
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps introduced new healthcare connectors, now available in public preview, to enhance interoperability in healthcare data exchange.

- Key changes or new features  
The update includes the HL7 connector, enabling seamless integration and processing of HL7 messaging standards widely used in healthcare systems. These connectors facilitate easier automation and orchestration of healthcare workflows by supporting common healthcare data formats and protocols, improving data exchange between disparate healthcare applications and systems.

- Target audience affected  
Developers and IT professionals working in healthcare IT, particularly those building or managing integration solutions involving healthcare data exchange, interoperability, and workflow automation using Azure Logic Apps.

- Important notes if any  
As these connectors are in public preview, users should evaluate them in non-production environments and provide feedback. Preview features may have limited SLA and support. It is recommended to monitor updates for GA release and enhanced capabilities.

**Details**:

The recent Azure update announces the public preview of new healthcare connectors for Azure Logic Apps, specifically designed to enhance interoperability within healthcare IT systems by facilitating seamless data exchange using industry-standard protocols such as HL7.

Background and Purpose:
Healthcare organizations often face challenges integrating disparate systems due to the complexity and variety of healthcare data formats and protocols. HL7 (Health Level Seven) is a widely adopted messaging standard for clinical and administrative data exchange. Azure Logic Apps, a cloud-based integration service, enables workflow automation across various systems. This update aims to simplify and accelerate healthcare data integration by introducing native connectors that directly support healthcare messaging standards, thereby reducing custom development efforts and improving compliance with healthcare interoperability requirements.

Specific Features and Detailed Changes:
The update introduces the HL7 connector in public preview, which allows Logic Apps workflows to send, receive, and process HL7 messages natively. This connector supports key HL7 message types and operations, enabling parsing, validation, and transformation of HL7 data within Logic Apps. The connectors provide prebuilt triggers and actions tailored to healthcare messaging, such as receiving HL7 messages from on-premises or cloud sources, sending HL7 messages to endpoints, and integrating with other healthcare systems. These connectors extend Logic Apps’ capabilities beyond generic connectors by offering healthcare-specific functionality and protocol support.

Technical Mechanisms and Implementation Methods:
The HL7 connector leverages Azure Integration Services infrastructure and supports HL7 v2.x messaging standards. It can be configured to connect with various endpoints, including on-premises systems via Azure Hybrid Connections or VPN, and cloud-based healthcare applications. The connector parses HL7 messages into JSON for easier manipulation within Logic Apps workflows and supports message validation against HL7 schemas. Developers can implement business logic to route, transform, or enrich HL7 messages using Logic Apps’ visual designer or code view. The connector integrates with Azure API Management and Azure Functions for extended customization and security.

Use Cases and Application Scenarios:
Typical use cases include hospital information system (HIS) integration, electronic health record (EHR) data exchange, lab result processing, patient admission and discharge notifications, and claims processing workflows. Healthcare providers can automate data flows between disparate systems, such as connecting EHRs with billing systems or external labs, ensuring timely and accurate data exchange. The connectors facilitate compliance with healthcare interoperability standards, enabling organizations to meet regulatory requirements and improve patient care coordination.

Important Considerations and Limitations:
As the connectors are in public preview, they may not yet be fully supported for production workloads and could undergo changes before general availability. Users should evaluate the connectors in test environments and monitor for updates. Security and compliance remain critical; therefore, proper configuration of network security, authentication, and data encryption is essential. Additionally, HL7 v3 and FHIR (Fast Healthcare Interoperability Resources) standards are not covered by this specific connector and may require separate integration approaches. Performance considerations should be assessed based on message volume and complexity.

Integration with Related Azure Services:
These healthcare connectors integrate seamlessly with other Azure services such as Azure API Management for secure API exposure, Azure Event Grid for event-driven architectures, Azure Functions for custom processing, and Azure Monitor for logging and diagnostics. They also complement Azure Healthcare APIs, which provide FHIR-based interoperability, enabling hybrid integration scenarios that combine HL7 and FHIR data flows. This integration ecosystem allows healthcare organizations to build comprehensive, scalable, and secure interoperability solutions on Azure.

In summary, the public preview of new healthcare connectors for Azure Logic Apps introduces native HL7 messaging support, empowering healthcare IT professionals to streamline interoperability workflows with reduced complexity and enhanced compliance, leveraging Azure’s integration and security capabilities.

---

### 93. Generally Available: Scheduled Actions 

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Scheduled Actions ](https://azure.microsoft.com/updates?id=530797)

**Update ID**: 530797
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines

**Summary**:

- What was updated  
Azure released the Generally Available (GA) version of Scheduled Actions, a feature that enables automated, periodic management of virtual machine (VM) lifecycles at scale.

- Key changes or new features  
Scheduled Actions allows users to define recurring schedules for VM operations such as start, stop, restart, or deallocate. The service automatically handles subscription throttling and retries on transient errors, reducing manual intervention and operational overhead. This ensures reliable execution of VM lifecycle tasks across large environments.

- Target audience affected  
This update primarily benefits developers and IT professionals managing large-scale Azure VM deployments who require automated, repeatable VM management to optimize costs and operational efficiency.

- Important notes if any  
Scheduled Actions is now generally available, indicating full support and SLA backing. Users can integrate this feature into their automation workflows without needing to build custom retry or throttling logic. For detailed usage and API integration, refer to the official Azure Update link.

**Details**:

The Azure update titled "Generally Available: Scheduled Actions" introduces a robust capability for automating and managing the lifecycle of virtual machines (VMs) at scale through periodic scheduling, designed to enhance operational efficiency and reliability in large-scale environments.

**Background and Purpose**  
Managing VM lifecycles—such as starting, stopping, restarting, or deallocating VMs—at scale has traditionally required custom scripting or manual intervention, which can be error-prone and difficult to maintain. Additionally, handling transient errors and subscription throttling during bulk operations adds complexity. The Scheduled Actions feature addresses these challenges by providing a native, scalable, and reliable mechanism to automate VM lifecycle operations on a recurring schedule, reducing operational overhead and improving consistency.

**Specific Features and Detailed Changes**  
Scheduled Actions enables users to define recurring schedules for VM lifecycle operations directly within Azure, such as start, stop, restart, or deallocate actions. Key features include:  
- **Periodic Scheduling:** Define cron-like schedules or fixed intervals to automate VM state changes.  
- **High-Scale Management:** Designed to handle thousands of VMs in a subscription efficiently.  
- **Automatic Throttling and Retries:** Built-in handling of Azure subscription throttling limits and transient errors ensures reliable execution without manual retry logic.  
- **Centralized Management:** Manage schedules across multiple VMs or VM scale sets from a single interface or API.  
- **Integration with Azure Resource Manager (ARM):** Uses ARM APIs to perform lifecycle operations, ensuring compatibility and security compliance.

**Technical Mechanisms and Implementation Methods**  
Scheduled Actions operates as a managed Azure service that interfaces with the Azure Resource Manager to execute lifecycle commands on VMs according to user-defined schedules. It abstracts the complexity of handling Azure API rate limits by automatically queuing and retrying operations when throttling occurs. The scheduling syntax supports cron expressions, allowing granular control over timing. The service maintains state and execution logs, enabling monitoring and troubleshooting. Users can configure Scheduled Actions via the Azure Portal, Azure CLI, PowerShell, or ARM templates, facilitating integration into existing DevOps workflows.

**Use Cases and Application Scenarios**  
- **Cost Optimization:** Automatically shut down non-production VMs during off-hours to reduce compute costs.  
- **Compliance and Security:** Enforce VM state policies by scheduling regular restarts or shutdowns.  
- **Dev/Test Environments:** Start VMs during business hours and stop them outside working hours without manual intervention.  
- **Large-Scale Operations:** Manage lifecycle operations across hundreds or thousands of VMs in enterprise environments or managed service providers.  
- **Disaster Recovery Drills:** Schedule periodic restarts or failover tests as part of DR validation.

**Important Considerations and Limitations**  
- Scheduled Actions currently supports only VM lifecycle operations; it does not extend to other resource types.  
- The feature relies on Azure Resource Manager permissions; appropriate RBAC roles (e.g., Virtual Machine Contributor) must be assigned to the executing identity.  
- While automatic retries mitigate transient errors, persistent failures due to misconfigurations or VM state conflicts require manual intervention.  
- Scheduling granularity is subject to minimum intervals defined by the service; extremely high-frequency operations may not be supported.  
- Monitoring and alerting should be configured to detect failed or skipped scheduled actions.

**Integration with Related Azure Services**  
Scheduled Actions integrates seamlessly with Azure Monitor and Azure Activity Logs, enabling operational visibility and alerting on scheduled lifecycle events. It complements Azure Automation and Azure Logic Apps by providing a lightweight, native scheduling mechanism specifically optimized for VM lifecycle management. Additionally, it works alongside Azure Policy to enforce compliance by automating remediation actions on VM states. Integration with Azure DevOps pipelines is possible through CLI and REST APIs, supporting infrastructure-as-code and CI/CD scenarios.

In summary, the Generally Available Scheduled Actions feature provides IT professionals with a scalable, reliable, and easy-to-use solution to automate VM lifecycle management, reducing manual effort and operational risk while optimizing

---

### 94. Generally Available: Microsoft Marketplace

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Microsoft Marketplace](https://azure.microsoft.com/updates?id=530614)

**Update ID**: 530614
**Data source**: Azure Updates API

**Categories**: Launched

**Summary**:

- What was updated  
Microsoft Marketplace has reached general availability worldwide, expanding beyond its initial U.S. launch in September.

- Key changes or new features  
All traffic from the legacy Azure Marketplace and AppSource storefronts is now redirected to the unified Microsoft Marketplace platform. This consolidation provides a single, trusted source for cloud solutions, AI applications, and agents, streamlining discovery, purchase, and deployment processes.

- Target audience affected  
Developers, IT professionals, and organizations leveraging Azure services who procure or publish cloud solutions, AI apps, and related agents.

- Important notes if any  
Users and publishers should transition to the Microsoft Marketplace for all transactions and listings as legacy storefronts are deprecated. This update enhances global accessibility and simplifies marketplace interactions, improving solution discoverability and management across Azure environments.

**Details**:

The Microsoft Marketplace has reached general availability worldwide, expanding from its initial U.S. launch in September, and now serves as the unified platform consolidating legacy storefronts—Azure Marketplace and AppSource—into a single, streamlined experience for discovering, purchasing, and deploying cloud solutions, AI applications, and agents. This update reflects Microsoft’s strategic initiative to simplify and enhance the procurement and deployment of third-party and Microsoft-certified solutions across Azure and related ecosystems.

**Background and Purpose:**  
Previously, Azure Marketplace and AppSource operated as separate entities catering to different solution types—Azure Marketplace primarily for IT and developer-focused cloud applications and infrastructure, and AppSource for business applications and SaaS offerings. This bifurcation often led to fragmented user experiences and complexity in solution discovery and management. The Microsoft Marketplace unification aims to provide a centralized, consistent, and scalable platform that improves discoverability, purchase workflows, and deployment processes globally, aligning with Microsoft’s broader cloud ecosystem strategy.

**Specific Features and Changes:**  
- **Unified storefront:** All listings from Azure Marketplace and AppSource are now accessible through a single Microsoft Marketplace portal, with legacy URLs redirecting seamlessly to the new platform.  
- **Global availability:** The service is now accessible worldwide, supporting multiple regions and languages, ensuring compliance with local regulations and data residency requirements.  
- **Enhanced AI and agent offerings:** The Marketplace includes AI apps and intelligent agents, reflecting Microsoft’s investment in AI-driven cloud solutions.  
- **Improved user experience:** Streamlined navigation, advanced search capabilities, and consolidated billing and subscription management enhance usability for IT professionals and procurement teams.  
- **Integrated deployment workflows:** Direct integration with Azure portal and other Microsoft management tools allows for simplified deployment and lifecycle management of purchased solutions.

**Technical Mechanisms and Implementation:**  
The transition to Microsoft Marketplace involves backend integration of catalog services, billing systems, and identity management under a unified platform. The system leverages Azure Active Directory (AAD) for authentication and authorization, ensuring secure access and compliance with enterprise identity policies. Solution publishers must update their offers to comply with the new Marketplace schema and certification requirements, which include metadata standardization and enhanced security validations. The platform supports ARM (Azure Resource Manager) templates and SaaS offer models, enabling automated provisioning and subscription management via APIs.

**Use Cases and Application Scenarios:**  
- **Enterprise IT procurement:** Organizations can discover and acquire certified cloud infrastructure components, security tools, and business applications in a single place, streamlining vendor management and compliance.  
- **DevOps and automation:** Developers and operations teams can integrate Marketplace offerings directly into CI/CD pipelines using ARM templates and APIs, accelerating deployment cycles.  
- **AI solution deployment:** Data scientists and AI engineers can access pre-built AI models and agents to augment applications without extensive custom development.  
- **ISV publishing:** Independent software vendors benefit from a global distribution channel with simplified offer management and analytics.

**Important Considerations and Limitations:**  
- **Offer migration:** Publishers must ensure their existing offers are updated and compliant with the new Marketplace requirements to avoid disruptions.  
- **Regional availability:** While globally available, some offers may have regional restrictions due to compliance or licensing.  
- **Billing integration:** Organizations should verify that their billing and subscription management systems are compatible with the unified Marketplace billing model.  
- **Security and compliance:** IT teams must validate that solutions meet organizational security policies and regulatory standards before deployment.

**Integration with Related Azure Services:**  
Microsoft Marketplace is tightly integrated with the Azure portal, enabling direct deployment of Marketplace solutions into Azure subscriptions. It leverages Azure Active Directory for identity and access management and integrates with Azure Cost Management for billing transparency. Additionally, it supports Azure Policy and Azure Security Center for governance and compliance of deployed solutions. The Marketplace also interfaces with Azure DevOps and GitHub Actions for automation scenarios, facilitating seamless inclusion of third-party solutions in development workflows.

In summary, the global general availability of Microsoft Marketplace consolidates Azure Marketplace and AppSource into a unified,

---

### 95. Generally Available: Resale enabled offers through Microsoft Marketplace  

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Resale enabled offers through Microsoft Marketplace  ](https://azure.microsoft.com/updates?id=530593)

**Update ID**: 530593
**Data source**: Azure Updates API

**Categories**: Launched, Microsoft Ignite, Features

**Summary**:

- What was updated  
Microsoft Marketplace has announced the general availability of resale enabled offers, expanding its channel-led Marketplace capabilities.

- Key changes or new features  
Resale enabled offers allow independent software vendors (ISVs) and partners to list software solutions that can be sold through Microsoft’s commercial marketplace ecosystem, enabling indirect reselling by partners. This facilitates streamlined procurement, billing, and management for commercial customers purchasing through their preferred partners. The update enhances partner collaboration and broadens customer access to innovative Azure-based solutions via reseller channels.

- Target audience affected  
This update primarily impacts ISVs, managed service providers, and reseller partners who leverage Microsoft Marketplace to distribute and sell software solutions. Commercial customers and IT professionals benefit from simplified purchasing and consolidated billing through their trusted partners.

- Important notes if any  
Partners must ensure their offers are configured correctly to support resale transactions. This capability aligns with Microsoft’s broader strategy to empower channel partners and accelerate customer adoption of Azure technologies through partner-led sales models. Developers should consider how resale enabled offers can expand their market reach via partner ecosystems.  

For more details, visit: https://azure.microsoft.com/updates?id=530593

**Details**:

The recent Azure update announcing the general availability of resale enabled offers through Microsoft Marketplace marks a significant advancement in how commercial customers and partners transact and distribute software solutions within the Azure ecosystem. This update is designed to empower channel partners by allowing them to resell software offers directly through the Microsoft commercial marketplace, thereby expanding the reach and flexibility of solution delivery.

**Background and Purpose:**  
Traditionally, Microsoft Marketplace has served as a platform for independent software vendors (ISVs) to list and sell their applications directly to customers. However, many enterprise customers rely on channel partners for procurement, deployment, and management of cloud solutions. The introduction of resale enabled offers addresses this market dynamic by enabling partners to act as intermediaries who can resell software licenses bundled with their own services, fostering a channel-led sales model. This aligns with Microsoft’s broader strategy to enhance partner-led growth and simplify commercial transactions in the cloud ecosystem.

**Specific Features and Detailed Changes:**  
With resale enabled offers, software vendors can configure their Marketplace listings to allow authorized partners to resell their solutions. Key features include:

- **Partner Resale Capability:** Partners can purchase software licenses on behalf of customers and resell them, often bundled with additional services such as consulting, deployment, or managed services.
- **Flexible Pricing and Billing:** The model supports partner-specific pricing and billing arrangements, enabling partners to maintain their margins and customize offers.
- **Integrated Commerce Experience:** Transactions are processed through Microsoft’s commerce platform, ensuring streamlined billing, compliance, and support processes.
- **Offer Configuration:** ISVs can designate which offers are resale enabled and manage partner relationships through the Partner Center.

**Technical Mechanisms and Implementation Methods:**  
From a technical standpoint, resale enabled offers leverage Microsoft’s commercial marketplace infrastructure and Partner Center APIs. Vendors configure their offers with resale enabled flags and define partner permissions. Partners then use Partner Center to discover, purchase, and provision these offers on behalf of customers. The commerce platform handles license assignment, usage metering (if applicable), and billing reconciliation. Integration with Azure Active Directory (AAD) ensures secure identity and access management during the provisioning and consumption phases. Additionally, telemetry and reporting APIs allow partners and vendors to monitor usage and compliance.

**Use Cases and Application Scenarios:**  
- **Managed Service Providers (MSPs):** MSPs can bundle software licenses with their managed Azure services, providing a single invoice and streamlined support.
- **Value-Added Resellers (VARs):** VARs can customize software offers with their own value-added services and resell to enterprise customers.
- **Enterprise Procurement:** Large organizations working with preferred partners can benefit from consolidated billing and simplified license management.
- **ISV Channel Expansion:** Software vendors can rapidly scale their market reach by leveraging partner networks without direct sales overhead.

**Important Considerations and Limitations:**  
- **Partner Onboarding:** Partners must be onboarded and authorized within Partner Center to resell offers, which involves compliance and verification steps.
- **Offer Eligibility:** Not all Marketplace offers are eligible for resale; ISVs must explicitly enable this feature.
- **Pricing Constraints:** While flexible, pricing must comply with Microsoft’s commercial policies and may be subject to regional regulations.
- **Support Model:** Support responsibilities may be shared between ISVs, partners, and Microsoft, requiring clear SLAs.
- **Data Privacy and Compliance:** Partners must ensure compliance with data protection regulations when handling customer data during provisioning and management.

**Integration with Related Azure Services:**  
Resale enabled offers integrate seamlessly with Azure subscription and billing services, leveraging Azure Resource Manager (ARM) for deployment and management of software resources. Identity and access management is handled via Azure Active Directory, ensuring secure authentication and authorization workflows. Additionally, telemetry and usage data can be integrated with Azure Monitor and Azure Cost Management for comprehensive operational insights. Partners can also utilize Azure Lighthouse to manage customer environments at scale, complementing the resale model with delegated management capabilities.

In summary, the general availability of resale enabled offers in Microsoft Marketplace provides a robust

---

### 96. Public Preview: GitHub Copilot app modernization expanded capabilities

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: GitHub Copilot app modernization expanded capabilities](https://azure.microsoft.com/updates?id=530257)

**Update ID**: 530257
**Data source**: Azure Updates API

**Categories**: In preview, Features, Microsoft Ignite

**Summary**:

- What was updated  
GitHub Copilot App Modernization has been enhanced with new capabilities now available in public preview, aimed at simplifying and accelerating the modernization of applications, databases, and containers for Azure migration.

- Key changes or new features  
The update introduces expanded support for analyzing and refactoring legacy applications, improved database modernization tools, and enhanced containerization workflows. These features leverage AI-driven code suggestions to streamline code transformation, optimize cloud-native architecture adoption, and automate migration tasks. Integration with Azure services is deepened to facilitate smoother transitions and reduce manual effort.

- Target audience affected  
Developers, DevOps engineers, and IT professionals involved in application modernization, cloud migration, and container management will benefit from these enhancements. Organizations planning to migrate workloads to Azure or modernize existing applications will find the tools particularly useful.

- Important notes if any  
As the features are in public preview, users should expect ongoing updates and potential changes. It is recommended to test these capabilities in non-production environments before full adoption. Feedback from users during this phase will help shape the final product.

**Details**:

The recent Azure update announces the public preview expansion of GitHub Copilot App Modernization capabilities, designed to streamline and accelerate the modernization of legacy applications, databases, and containerized workloads for migration to Azure. This enhancement leverages AI-driven assistance to simplify complex refactoring and migration tasks, enabling developers and IT professionals to adopt cloud-native architectures more efficiently.

**Background and Purpose**  
As organizations increasingly migrate to cloud environments, modernizing existing applications and infrastructure becomes critical to leverage Azure’s scalability, security, and managed services. Traditional modernization efforts often involve manual, error-prone processes requiring deep expertise in cloud architectures, containerization, and database transformations. The GitHub Copilot App Modernization tool aims to reduce this complexity by providing AI-assisted code and configuration generation, thereby accelerating the migration lifecycle and reducing operational overhead.

**Specific Features and Detailed Changes**  
The public preview introduces expanded capabilities including:  
- **Enhanced application modernization suggestions:** Copilot now offers more comprehensive code refactoring recommendations to convert legacy codebases into cloud-optimized versions, including support for microservices decomposition and API modernization.  
- **Database modernization assistance:** Automated guidance for migrating on-premises databases to Azure SQL Database, Azure Cosmos DB, or other managed database services, including schema transformation and data migration scripts.  
- **Containerization support:** Improved tooling to containerize existing applications with Docker and Kubernetes manifests generation, facilitating deployment to Azure Kubernetes Service (AKS) or Azure Container Instances (ACI).  
- **Migration acceleration:** Integration with Azure Migrate and Azure Database Migration Service to provide end-to-end migration workflows, supported by AI-generated migration plans and scripts.  

**Technical Mechanisms and Implementation Methods**  
GitHub Copilot App Modernization leverages OpenAI’s Codex model integrated within GitHub Codespaces and Visual Studio Code environments. It analyzes existing codebases and infrastructure-as-code templates to generate modernization recommendations and code snippets. The tool uses static code analysis combined with cloud best practices to suggest refactoring patterns, container definitions, and database schema modifications. The generated artifacts can be directly applied or customized by developers, enabling iterative modernization. Integration with Azure DevOps pipelines allows automated testing and deployment of modernized components.

**Use Cases and Application Scenarios**  
- **Legacy web application modernization:** Transform monolithic .NET Framework or Java EE applications into microservices deployed on AKS with managed databases.  
- **Database migration:** Automated schema conversion and data migration from SQL Server on-premises to Azure SQL Database or Cosmos DB for globally distributed applications.  
- **Container adoption:** Containerize legacy applications without deep container expertise, enabling rapid deployment to Azure Container Instances or AKS.  
- **Cloud migration acceleration:** Use AI-generated migration plans to reduce manual effort and risk during lift-and-shift or re-architecting projects.  

**Important Considerations and Limitations**  
- As a public preview feature, the tool may have incomplete support for some legacy languages or complex application architectures.  
- AI-generated recommendations should be reviewed by developers to ensure compliance with organizational security and coding standards.  
- Performance and accuracy may vary depending on codebase complexity and quality of existing documentation.  
- Integration with third-party or proprietary systems may require additional customization beyond the automated suggestions.  

**Integration with Related Azure Services**  
- **Azure Migrate:** Provides discovery and assessment data that Copilot uses to tailor modernization suggestions.  
- **Azure Database Migration Service:** Automates data migration steps recommended by Copilot.  
- **Azure Kubernetes Service (AKS):** Target environment for containerized applications generated by the tool.  
- **Azure DevOps:** Enables CI/CD pipelines for deploying modernized applications and infrastructure.  
- **GitHub Codespaces and Visual Studio Code:** Primary development environments where Copilot App Modernization operates, facilitating seamless developer workflows.  

In summary, the expanded public preview of GitHub Copilot App Modernization introduces AI-driven enhancements that simplify and accelerate the transformation of legacy applications, databases, and containers for

---

### 97. Public Preview: Industry-leading storage performance Ebsv6 VM series

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Industry-leading storage performance Ebsv6 VM series](https://azure.microsoft.com/updates?id=529416)

**Update ID**: 529416
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines

**Summary**:

- What was updated  
Azure announced the public preview of the Ebsv6 and Ebdsv6 VM series, featuring 5th Generation Intel® Xeon® processors.

- Key changes or new features  
These VM series deliver industry-leading storage performance with up to 800,000 IOPS and 14 GBps of remote disk throughput. This represents a significant boost in storage I/O capabilities, ideal for storage-intensive workloads. The VMs support premium storage and are optimized for high-performance applications requiring low latency and high throughput.

- Target audience affected  
Developers and IT professionals running data-intensive applications such as databases, analytics, and large-scale transaction processing will benefit from these VMs. Cloud architects designing high-performance storage solutions and enterprises needing scalable, fast storage access will find these VMs advantageous.

- Important notes if any  
As this is a public preview, users should evaluate the VMs in non-production environments initially. Availability may be limited by region, and pricing details should be reviewed before adoption. Monitoring performance and compatibility with existing workloads is recommended to fully leverage the enhanced storage throughput capabilities.

For more details, visit: https://azure.microsoft.com/updates?id=529416

**Details**:

The Azure public preview of the Ebsv6 VM series introduces a new class of virtual machines powered by 5th Generation Intel® Xeon® processors, designed to deliver industry-leading storage performance with up to 800,000 IOPS and 14 GBps of remote disk throughput. This update addresses the growing demand for high-throughput, low-latency storage in cloud workloads, enabling IT professionals to run data-intensive applications more efficiently.

**Background and Purpose:**  
As enterprise workloads increasingly require faster and more reliable storage access—such as databases, big data analytics, and high-performance computing—Azure has enhanced its VM offerings to meet these demands. The Ebsv6 series aims to provide a balance of compute power and exceptional storage throughput, improving overall application responsiveness and scalability in cloud environments.

**Specific Features and Detailed Changes:**  
- **Processor:** Powered by 5th Gen Intel® Xeon® processors, offering improved CPU performance and efficiency.  
- **Storage Performance:** Up to 800,000 IOPS and 14 GBps throughput on remote managed disks, significantly surpassing previous VM generations.  
- **VM Variants:** Includes Ebsv6 (standard) and Ebdsv6 (premium storage optimized) variants to cater to different workload requirements.  
- **Memory and CPU Configurations:** Multiple sizes available, allowing customization based on workload needs.  
- **Enhanced Networking:** Supports Azure Accelerated Networking for reduced latency and improved packet per second (PPS) performance.

**Technical Mechanisms and Implementation Methods:**  
The Ebsv6 series leverages the latest Intel Xeon processors that incorporate architectural improvements such as higher clock speeds, larger caches, and advanced vector extensions to accelerate compute tasks. Storage performance gains are achieved through optimized VM-to-managed disk connectivity, utilizing Azure’s high-speed RDMA-capable infrastructure and enhanced storage stack optimizations. The VMs support Premium SSD and Ultra Disk storage, enabling high IOPS and throughput with low latency. Azure’s underlying hypervisor and networking stack enhancements facilitate accelerated networking, reducing CPU overhead and improving data transfer rates.

**Use Cases and Application Scenarios:**  
- **Databases:** High transaction rate OLTP databases like SQL Server, Oracle, and NoSQL databases benefit from the high IOPS and throughput.  
- **Big Data and Analytics:** Workloads requiring rapid data ingestion and processing, such as Apache Spark or Hadoop clusters.  
- **High-Performance Computing (HPC):** Compute-intensive simulations and modeling that also require fast access to large datasets.  
- **Enterprise Applications:** ERP, CRM, and other business-critical applications that demand consistent storage performance.  
- **Virtual Desktop Infrastructure (VDI):** Scenarios requiring fast disk access to improve user experience.

**Important Considerations and Limitations:**  
- As this is a public preview, SLAs and support may be limited; production workloads should be carefully evaluated before migration.  
- The high storage performance requires compatible managed disks (Premium SSD or Ultra Disk) and proper configuration to fully leverage throughput capabilities.  
- Network and storage throughput are subject to VM size and region availability; users should verify resource quotas and regional support.  
- Cost implications due to higher performance tiers should be assessed against workload requirements.

**Integration with Related Azure Services:**  
- **Azure Managed Disks:** The Ebsv6 series is optimized for Premium SSD and Ultra Disk managed disks, enabling seamless integration with Azure’s high-performance storage options.  
- **Azure Virtual Network:** Supports Accelerated Networking for enhanced network performance, critical for distributed applications.  
- **Azure Monitor and Azure Advisor:** Can be used to monitor performance metrics and optimize resource utilization for Ebsv6 VMs.  
- **Azure Scale Sets:** The VM series can be deployed in scale sets to support scalable, high-throughput applications.

In summary, the Azure Ebsv6 VM series public preview offers IT professionals a powerful new option for workloads demanding exceptional storage I/O and throughput, leveraging the latest Intel Xeon processors

---

### 98. Public Preview: User and group quota reports in Azure NetApp Files 

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: User and group quota reports in Azure NetApp Files ](https://azure.microsoft.com/updates?id=528899)

**Update ID**: 528899
**Data source**: Azure Updates API

**Categories**: In development, Storage, Azure NetApp Files

**Summary**:

- What was updated  
Azure NetApp Files has introduced a public preview of user and group quota reports, enhancing capacity management for volumes using individual quotas.

- Key changes or new features  
The new reporting feature provides detailed visibility into quota limits, usage, and consumption metrics for users and groups on NFS, SMB, and dual-protocol volumes. This enables administrators to monitor and analyze storage utilization at a granular level, helping to prevent quota overruns and optimize capacity planning. Reports are accessible via API, facilitating integration with existing monitoring and automation workflows.

- Target audience affected  
This update primarily benefits IT administrators and storage engineers managing Azure NetApp Files environments with user/group quota enforcement. Developers building automation or monitoring tools can leverage the API to incorporate quota data into their solutions.

- Important notes if any  
The feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. As it uses API data, familiarity with Azure NetApp Files REST APIs will be helpful for effective utilization. No impact on existing quota enforcement is expected.  

For more details, visit: https://azure.microsoft.com/updates?id=528899

**Details**:

The recent Azure NetApp Files update introduces a Public Preview of user and group quota reports, designed to enhance capacity management and monitoring for organizations using quotas on NFS, SMB, and dual-protocol volumes. This feature addresses the need for granular visibility into storage consumption at the user and group level, enabling more effective quota enforcement and resource planning.

**Background and Purpose:**  
Azure NetApp Files supports individual user and group quotas to control storage usage on file shares, preventing any single user or group from exceeding allocated capacity. Prior to this update, administrators lacked detailed reporting tools to analyze quota usage patterns, making it difficult to track consumption, identify overages, or optimize quota assignments. The introduction of user and group quota reports fills this gap by providing comprehensive metrics and insights, facilitating proactive storage management and cost control.

**Specific Features and Detailed Changes:**  
The update delivers a reporting capability that aggregates quota-related data, including quota limits, current usage, and overage status for both users and groups. Reports are accessible via the Azure portal and can be exported for further analysis. Key metrics include:  
- Quota limits assigned per user or group  
- Actual storage consumption against these limits  
- Identification of users or groups exceeding their quotas  
- Historical usage trends to support capacity planning  

This feature supports all protocol types (NFS, SMB, and dual-protocol volumes), ensuring consistent quota reporting regardless of access method.

**Technical Mechanisms and Implementation Methods:**  
Quota enforcement in Azure NetApp Files is implemented at the volume level using native quota management capabilities integrated with the underlying NetApp ONTAP technology. The reporting feature collects quota metadata and usage statistics from these volumes and aggregates the data in a centralized manner. Data collection occurs periodically, ensuring reports reflect near real-time usage. The reports are generated through Azure NetApp Files’ management plane, leveraging Azure Monitor and Azure Storage analytics for data aggregation and visualization. The preview phase allows users to access these reports through the Azure portal interface, with plans for API integration to enable automation and integration into custom monitoring solutions.

**Use Cases and Application Scenarios:**  
- **Capacity Management:** Administrators can monitor quota consumption to prevent storage over-provisioning or unexpected overages.  
- **Chargeback and Billing:** Organizations using internal chargeback models can allocate costs based on actual user or group storage consumption.  
- **Compliance and Auditing:** Detailed quota reports help ensure adherence to organizational policies regarding storage limits.  
- **Performance Optimization:** Identifying users or groups with high storage usage can guide data lifecycle management and archiving strategies.  

This feature is especially valuable for enterprises with large teams accessing shared file storage, where quota enforcement is critical to maintain service quality and cost predictability.

**Important Considerations and Limitations:**  
- As a Public Preview feature, the quota reporting capability may have limited SLA guarantees and could undergo changes before general availability.  
- Reporting latency means data may not be real-time; administrators should consider this when making immediate operational decisions.  
- Integration with existing monitoring or alerting systems may require custom development until full API support is released.  
- The feature currently supports Azure NetApp Files volumes configured with user and group quotas; volumes without quotas will not generate relevant reports.  

**Integration with Related Azure Services:**  
The quota reporting feature integrates with the Azure portal for visualization and management. It leverages Azure Monitor for metric collection and alerting capabilities, enabling administrators to set up notifications based on quota thresholds. Exported reports can be ingested into Azure Log Analytics or Power BI for advanced analytics and dashboarding. Future enhancements may include REST API support for integration with Azure Automation or third-party ITSM tools, facilitating automated quota management workflows.

In summary, the Public Preview of user and group quota reports in Azure NetApp Files provides IT professionals with a powerful tool to gain detailed insights into storage consumption at a granular level, improving capacity governance, cost management, and operational efficiency across NFS, SMB, and dual-protocol file shares.

---

### 99. Generally Available: New Hybrid Integration Connectors for Azure Logic Apps

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: New Hybrid Integration Connectors for Azure Logic Apps](https://azure.microsoft.com/updates?id=527683)

**Update ID**: 527683
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps introduced new hybrid integration connectors that are now generally available, enhancing connectivity options for hybrid and cloud workflows.

- Key changes or new features  
The update includes the release of the Confluent Kafka connector, enabling Logic Apps to seamlessly connect with Confluent Cloud for event streaming scenarios. This expands the hybrid integration capabilities by allowing event-driven architectures to integrate with Kafka-based systems more easily. The connectors support reliable, scalable, and secure data exchange between on-premises and cloud environments.

- Target audience affected  
Developers and IT professionals building integration workflows using Azure Logic Apps, especially those leveraging event streaming and hybrid cloud architectures, will benefit from these new connectors. Organizations using Confluent Kafka for real-time data processing can now integrate their event streams directly into Logic Apps workflows.

- Important notes if any  
The connectors are generally available, indicating full production readiness and Microsoft support. Users should review connector documentation for configuration details and best practices to optimize performance and security in hybrid scenarios. This update simplifies building complex integrations involving Kafka event streams without custom code.

**Details**:

The recent Azure update announces the general availability of new hybrid integration connectors for Azure Logic Apps, notably including the Confluent Kafka connector, designed to enhance event-driven workflows by enabling seamless connectivity between Logic Apps and Confluent Cloud event streaming services. This update addresses the growing demand for robust hybrid integration solutions that bridge cloud-native applications with on-premises and third-party services, facilitating more agile and scalable enterprise workflows.

**Background and Purpose:**  
Azure Logic Apps is a cloud-based integration platform that enables IT professionals to automate workflows and integrate applications, data, and services across cloud and on-premises environments. Hybrid integration connectors extend this capability by providing prebuilt, managed connectors that simplify connectivity to external systems, including SaaS platforms and event streaming services. The introduction of these new connectors, such as the Confluent Kafka connector, responds to the increasing adoption of event-driven architectures and the need for real-time data processing across hybrid environments.

**Specific Features and Detailed Changes:**  
The update brings several new connectors into general availability, with the Confluent Kafka connector being a highlight. This connector allows Logic Apps to natively connect to Confluent Cloud, a fully managed Apache Kafka service, enabling Logic Apps to consume and produce Kafka events without custom coding or infrastructure management. Key features include:  
- Native support for Kafka topics and partitions, enabling fine-grained event handling.  
- Authentication and secure connectivity using Confluent Cloud credentials and Azure-managed identities.  
- Trigger and action support within Logic Apps workflows, allowing event-driven automation based on Kafka messages.  
- Built-in retry policies and error handling to ensure reliable event processing.

**Technical Mechanisms and Implementation Methods:**  
Under the hood, the Confluent Kafka connector leverages the Kafka protocol to interact with Confluent Cloud clusters. It abstracts the complexity of Kafka client configuration by providing a declarative interface within Logic Apps. Users configure connection parameters such as bootstrap servers, topic names, and authentication details directly in the Logic Apps designer or via ARM templates. The connector supports both triggers (to start workflows on incoming Kafka messages) and actions (to send messages to Kafka topics), enabling bidirectional event flow. Connectivity is secured using TLS encryption and OAuth-based authentication, aligning with enterprise security standards.

**Use Cases and Application Scenarios:**  
This update is particularly valuable for scenarios requiring real-time data integration and event-driven automation, such as:  
- Processing streaming data from IoT devices or telemetry systems via Kafka topics and triggering downstream workflows in Logic Apps.  
- Integrating enterprise applications with Confluent Cloud to enable event-driven microservices architectures.  
- Automating business processes based on event streams, such as fraud detection, order processing, or customer engagement workflows.  
- Bridging on-premises systems with cloud event streams to enable hybrid data pipelines and analytics.

**Important Considerations and Limitations:**  
While the new connectors simplify integration, IT professionals should consider:  
- Network connectivity requirements, including firewall and VNet configurations, to ensure secure access to Confluent Cloud endpoints.  
- Quotas and throttling limits in Logic Apps and Confluent Cloud that may impact high-throughput scenarios.  
- Latency considerations inherent in event streaming and workflow execution times.  
- Proper error handling and retry logic configuration to handle transient failures in event delivery.  
- Compatibility with existing Logic Apps Standard and Consumption tiers, as some features may vary.

**Integration with Related Azure Services:**  
These connectors complement other Azure integration services, such as Azure Event Grid and Azure Service Bus, by providing additional event streaming options. They can be combined with Azure Functions for custom processing, Azure Monitor for observability, and Azure API Management for exposing integrated workflows as APIs. Additionally, integration with Azure Active Directory enables centralized identity and access management across hybrid environments.

In summary, the general availability of new hybrid integration connectors, including the Confluent Kafka connector, significantly enhances Azure Logic Apps’ capabilities for building scalable, event-driven workflows that span cloud and on

---

### 100. Public Preview: Redesigned designer experience for Azure Logic Apps [Standard]

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Redesigned designer experience for Azure Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527673)

**Update ID**: 527673
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps (Standard) introduced a redesigned designer experience now available in public preview.

- Key changes or new features  
The updated designer enhances workflow building, editing, and management with a more intuitive and faster interface. It integrates run history directly within the designer, allowing developers and IT professionals to view and troubleshoot workflow executions without switching contexts. The workflow editing capabilities have been improved for smoother modifications and better usability.

- Target audience affected  
Developers and IT professionals who design, deploy, and maintain Azure Logic Apps workflows, especially those using the Standard tier for enterprise integration scenarios.

- Important notes if any  
As this is a public preview, users should test the new designer in non-production environments and provide feedback. Some features may still be evolving, and full production support will come in a future release. Users can access the preview through the Azure portal as linked in the update.

**Details**:

The public preview of the redesigned designer experience for Azure Logic Apps (Standard) introduces a significant enhancement aimed at improving the efficiency and intuitiveness of workflow development and management within the Azure Logic Apps Standard environment. This update addresses longstanding user feedback on usability and operational visibility, streamlining the process of building, editing, and monitoring workflows.

**Background and Purpose**  
Azure Logic Apps (Standard) provides a scalable, serverless workflow orchestration platform that enables integration across cloud and on-premises systems. The original designer, while functional, presented challenges in terms of navigation, editing flexibility, and real-time operational insights. The redesigned experience seeks to overcome these limitations by offering a unified interface that consolidates workflow creation, editing, and run history inspection, thereby accelerating development cycles and reducing context switching.

**Specific Features and Detailed Changes**  
- **Unified Designer Interface:** The new designer integrates workflow editing and run history viewing within a single pane, allowing developers to seamlessly switch between modifying logic and analyzing execution outcomes without leaving the interface.  
- **Improved Workflow Editing:** Enhanced drag-and-drop capabilities, inline property editing, and contextual menus simplify the construction and modification of complex workflows. The designer supports multi-step selection and bulk actions, improving productivity for large workflows.  
- **Run History Integration:** Real-time access to run history is embedded directly in the designer, providing detailed insights into trigger and action execution, input/output data, and error diagnostics. This facilitates rapid troubleshooting and iterative development.  
- **Performance and Responsiveness:** The updated designer leverages modern web technologies to deliver faster load times and smoother interactions, even for workflows with numerous actions and nested scopes.  
- **Enhanced UX/UI:** The interface adopts a cleaner, more intuitive layout with improved visual cues and accessibility features, reducing the learning curve for new users and enhancing overall user satisfaction.

**Technical Mechanisms and Implementation Methods**  
The redesigned designer is built on a modern web framework that interacts with the Logic Apps Standard runtime APIs. It utilizes RESTful endpoints to fetch and update workflow definitions stored in Azure Storage or integrated source control repositories. Run history data is retrieved via the Logic Apps management API, enabling real-time display of execution metrics and logs. The designer supports ARM template integration and leverages Azure Resource Manager for deployment consistency. Additionally, the interface is designed to be extensible, allowing future integration of custom connectors and actions.

**Use Cases and Application Scenarios**  
- **Rapid Workflow Development:** Developers can quickly prototype and iterate on integration workflows connecting SaaS applications, on-premises systems, and custom APIs.  
- **Operational Monitoring and Troubleshooting:** DevOps teams benefit from immediate access to run history and error details within the same interface used for editing, reducing mean time to resolution (MTTR).  
- **Complex Enterprise Integrations:** Organizations implementing multi-step, conditional logic workflows can manage and update their processes more efficiently, supporting business continuity and agility.  
- **Dev/Test Environments:** The improved designer facilitates testing and validation of workflows before production deployment, enhancing release quality.

**Important Considerations and Limitations**  
- As a public preview feature, the redesigned designer may not yet support all legacy connectors or custom extensions available in the classic designer.  
- Users should validate compatibility with existing CI/CD pipelines and source control integrations, as some workflows may require adjustments to align with the new designer’s metadata schema.  
- Performance improvements may vary depending on workflow complexity and network conditions.  
- Feedback during the preview phase is encouraged to help Microsoft refine features and address any stability issues.

**Integration with Related Azure Services**  
The redesigned designer maintains seamless integration with Azure DevOps and GitHub for source control and CI/CD pipelines, supporting ARM template deployments and versioning. It continues to leverage Azure Monitor and Application Insights for extended telemetry and alerting capabilities. Additionally, it supports connectors across the Azure ecosystem, including Azure Functions, Service Bus, Event Grid, and API Management, enabling comprehensive hybrid integration scenarios.

In summary, the public preview of the redesigned

---

### 101. Public Preview: New Agent Loop capabilities in Azure Logic Apps

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: New Agent Loop capabilities in Azure Logic Apps](https://azure.microsoft.com/updates?id=527663)

**Update ID**: 527663
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps introduced new Agent Loop capabilities, now available in public preview, enhancing the platform’s support for agentic workflows.

- Key changes or new features  
The update expands how organizations can build, secure, and deploy agentic workflows at scale. It enables more flexible orchestration of AI agents within enterprise environments, improving automation and integration scenarios. These capabilities facilitate advanced AI-driven process automation by allowing developers to create workflows that can manage multiple AI agents interacting dynamically.

- Target audience affected  
Developers and IT professionals working with Azure Logic Apps, especially those implementing AI orchestration, automation, and complex workflow integrations, will benefit from these new features.

- Important notes if any  
As this feature is in public preview, users should evaluate it in non-production environments and provide feedback. Documentation and support may be limited compared to generally available features. It is recommended to monitor updates for GA release and best practices.  

For more details, visit: https://azure.microsoft.com/updates?id=527663

**Details**:

The recent public preview release of new Agent Loop capabilities in Azure Logic Apps introduces advanced features designed to enhance the orchestration, security, and deployment of agentic workflows within enterprise environments, thereby enabling more flexible and scalable AI-driven automation solutions.

**Background and Purpose**  
Azure Logic Apps is a cloud-based service that enables developers and IT professionals to design and automate workflows that integrate apps, data, services, and systems. With the growing adoption of AI and autonomous agents, there is a need to manage complex agentic workflows that involve iterative, multi-step interactions often requiring dynamic decision-making and state management. The Agent Loop update addresses this by providing enhanced control over agent orchestration, improving the ability to build workflows that can loop through agent tasks efficiently while maintaining security and governance.

**Specific Features and Detailed Changes**  
The update introduces a new Agent Loop construct within Azure Logic Apps that allows workflows to repeatedly invoke agentic processes with fine-grained control over iteration, branching, and error handling. Key features include:

- **Looping Mechanism:** Enables repeated execution of agent tasks with configurable exit conditions, supporting both fixed and dynamic iteration counts.
- **Stateful Agent Management:** Maintains context and state across loop iterations, allowing agents to make decisions based on previous outcomes.
- **Enhanced Security Controls:** Integration with Azure Active Directory (AAD) and role-based access control (RBAC) to secure agent workflows and restrict execution to authorized identities.
- **Improved Monitoring and Diagnostics:** Extended telemetry and logging capabilities to track loop execution, agent decisions, and exceptions for better observability.
- **Flexible Deployment Options:** Support for deploying agent loops across multi-environment setups including development, staging, and production with environment-specific configurations.

**Technical Mechanisms and Implementation Methods**  
Under the hood, the Agent Loop leverages the existing Logic Apps workflow engine but extends it with new loop control actions and state management primitives. Developers define an Agent Loop as part of the workflow definition using the Logic Apps Designer or ARM templates. The loop action can call AI agents or custom connectors repeatedly, passing updated context parameters each iteration. State persistence is managed via Azure Storage or integrated Cosmos DB, ensuring durability and consistency. Security is enforced through managed identities and integration with Azure Key Vault for secrets management. The telemetry data is emitted to Azure Monitor and Application Insights for real-time analysis.

**Use Cases and Application Scenarios**  
- **AI Orchestration:** Automate multi-step AI workflows such as iterative data enrichment, conversational agent dialogues, or decision-making processes that require repeated agent interactions.
- **Robotic Process Automation (RPA):** Implement complex RPA scenarios where bots perform repetitive tasks with conditional branching and error recovery.
- **IT Operations Automation:** Manage incident response workflows that loop through diagnostic agents until resolution criteria are met.
- **Customer Support:** Enable chatbots and virtual agents to handle multi-turn conversations with stateful context retention.
- **Data Processing Pipelines:** Execute iterative data validation or transformation steps with dynamic loop control.

**Important Considerations and Limitations**  
- Being in public preview, the Agent Loop feature may have limitations in SLA guarantees and could undergo changes before general availability.
- Performance considerations should be evaluated for high-frequency loops, as excessive iterations may lead to increased latency or cost.
- Proper error handling and loop exit conditions must be carefully designed to avoid infinite loops.
- Integration with on-premises systems requires the use of Azure Integration Runtime or hybrid connectors.
- Security configurations must be validated to prevent unauthorized access or privilege escalation within agent workflows.

**Integration with Related Azure Services**  
- **Azure AI Services:** Agent Loop workflows can invoke Azure Cognitive Services, Azure OpenAI, or custom AI models to perform intelligent tasks.
- **Azure Monitor and Application Insights:** For monitoring loop execution, logging, and diagnostics.
- **Azure Key Vault:** To securely manage credentials and secrets used by agents.
- **Azure Active Directory:** For authentication and authorization of workflow executions.
- **Azure Storage and Cosmos DB:** For state

---

### 102. Public Preview: Agent Loop in Azure Logic Apps [Consumption]

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Agent Loop in Azure Logic Apps [Consumption]](https://azure.microsoft.com/updates?id=527658)

**Update ID**: 527658
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps (Consumption) introduced the public preview of Agent Loop, a new capability that integrates agentic intelligence and adaptive workflows into the serverless Logic Apps runtime.

- Key changes or new features  
Agent Loop allows developers to design workflows that go beyond static automation by enabling goal-driven, iterative processes within Logic Apps. This feature supports dynamic decision-making and adaptive task execution, enhancing automation flexibility and responsiveness. It leverages AI-driven agents to monitor, evaluate, and adjust workflow steps in real time, improving efficiency and enabling complex scenario handling without manual intervention.

- Target audience affected  
Developers and IT professionals who build and manage serverless integrations and automation using Azure Logic Apps (Consumption) will benefit from this update. It is particularly useful for those requiring intelligent, adaptive workflow capabilities in cloud-native automation solutions.

- Important notes if any  
Agent Loop is currently in public preview, so users should test it in non-production environments and provide feedback. As a preview feature, it may undergo changes before general availability. Documentation and best practices are evolving to support adoption.

**Details**:

The recent public preview announcement of Agent Loop in Azure Logic Apps (Consumption) introduces a significant advancement in serverless workflow automation by embedding agentic intelligence and adaptive capabilities directly into the Logic Apps runtime. This update aims to transcend traditional static, rule-based automation by enabling dynamic, goal-driven workflows that can iteratively assess and respond to changing conditions or data inputs.

**Background and Purpose**  
Azure Logic Apps has long provided a scalable, serverless platform for orchestrating workflows through pre-defined connectors and triggers. However, many automation scenarios require more flexibility and intelligence to handle complex decision-making, iterative processes, or adaptive task execution. Agent Loop addresses this gap by integrating agentic intelligence—essentially autonomous, goal-oriented agents—into the Logic Apps consumption model. This enables workflows that can dynamically plan, execute, and adjust actions based on intermediate results, rather than following a fixed linear path.

**Specific Features and Detailed Changes**  
- **Agentic Intelligence Integration:** Agent Loop allows embedding intelligent agents that can interpret goals, plan sequences of actions, and adapt based on feedback within a Logic App.  
- **Adaptive Workflow Execution:** Unlike traditional Logic Apps that follow static workflows, Agent Loop supports iterative loops where the agent evaluates outcomes and decides next steps dynamically.  
- **Consumption Model Support:** This feature is available in the Consumption tier, ensuring pay-per-use scalability without requiring dedicated infrastructure.  
- **Enhanced Control Flow:** New constructs and connectors facilitate the implementation of agent loops, including conditional branching based on agent decisions and iterative processing.  
- **Seamless Integration with Existing Connectors:** Agent Loop workflows can invoke existing Logic Apps connectors, APIs, and services, enabling intelligent orchestration across diverse systems.

**Technical Mechanisms and Implementation Methods**  
Agent Loop operates by embedding an intelligent agent runtime within the Logic Apps engine. The agent receives a defined goal and context, then uses built-in reasoning and planning capabilities to determine a sequence of actions. These actions are executed through standard Logic Apps connectors or custom APIs. After each action, the agent evaluates the outcome, updates its internal state, and decides whether to continue, modify, or terminate the loop. This approach leverages serverless compute elasticity, event-driven triggers, and stateful workflow management inherent to Logic Apps Consumption.

**Use Cases and Application Scenarios**  
- **Dynamic Approval Processes:** Automate multi-stage approvals where the agent adapts the workflow based on approver responses or external data changes.  
- **Intelligent Incident Response:** Continuously monitor alerts, gather diagnostics, and escalate or remediate issues dynamically.  
- **Personalized Customer Engagement:** Tailor communication workflows that adapt messaging and channels based on customer interactions in real-time.  
- **Complex Data Processing Pipelines:** Iteratively refine data transformations or validations based on intermediate results without manual intervention.  
- **Automated Compliance Checks:** Continuously evaluate compliance criteria and adapt remediation steps as regulations or data evolve.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, Agent Loop may have limited SLA guarantees and could undergo significant changes before general availability.  
- **Learning Curve:** Implementing agentic workflows requires understanding of goal-oriented automation concepts beyond traditional Logic Apps design.  
- **Performance Implications:** Iterative loops with complex decision-making may increase execution time and cost; careful design is needed to optimize efficiency.  
- **Security and Governance:** Proper access controls and monitoring should be enforced, especially as workflows gain autonomous decision capabilities.  
- **Compatibility:** Some existing Logic Apps features or connectors may require updates to fully leverage Agent Loop capabilities.

**Integration with Related Azure Services**  
Agent Loop workflows can integrate seamlessly with Azure Cognitive Services for enhanced AI capabilities, Azure Functions for custom code execution, and Azure Monitor for telemetry and alerting. It also complements Azure Machine Learning by enabling adaptive workflows that respond to model outputs dynamically. Additionally, integration with Azure API Management allows secure exposure of agent-driven workflows as APIs, facilitating broader enterprise automation strategies.

In

---

### 103. Generally Available: Agent Loop in Azure Logic Apps [Standard]

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Agent Loop in Azure Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527649)

**Update ID**: 527649
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps (Standard) now generally supports the Agent Loop feature.

- Key changes or new features  
Agent Loop introduces a new paradigm for designing and automating business processes by enabling continuous, event-driven loops within Logic Apps workflows. This capability allows workflows to maintain state and react dynamically to ongoing events or data changes without restarting the entire process. It enhances scalability and responsiveness in automation scenarios, supporting complex, long-running processes with improved efficiency.

- Target audience affected  
Developers and IT professionals who design, implement, and manage business process automation using Azure Logic Apps will benefit from this update. It is particularly valuable for those building event-driven, stateful workflows requiring continuous monitoring or iterative processing.

- Important notes if any  
Agent Loop is now generally available, meaning it is production-ready and supported for enterprise use. Users should review updated documentation and best practices to optimize their Logic Apps with this feature. Integration with existing Logic Apps workflows may require adjustments to leverage the new looping and state management capabilities effectively.

For detailed information, visit: https://azure.microsoft.com/updates?id=527649

**Details**:

The recent general availability of Agent Loop in Azure Logic Apps (Standard) introduces a transformative enhancement designed to elevate the automation of complex business processes by enabling iterative and stateful orchestration within workflows. Traditionally, Azure Logic Apps focused on linear or branching workflows triggered by events; Agent Loop extends this paradigm by allowing developers to implement looped, agent-based processing patterns that can manage long-running, multi-step tasks with dynamic decision-making capabilities.

**Background and Purpose**  
Azure Logic Apps has been a cornerstone for integrating disparate systems and automating workflows in the cloud. However, many enterprise scenarios require iterative processing, dynamic task allocation, and stateful interactions that exceed simple linear workflows. Agent Loop addresses these needs by embedding an agent-oriented loop construct directly into Logic Apps (Standard), enabling workflows to manage complex, iterative business logic natively without resorting to external orchestration or custom code.

**Specific Features and Detailed Changes**  
Agent Loop introduces a new workflow construct that allows a Logic App to spawn and manage multiple "agents"—independent units of work that can execute concurrently or sequentially within a loop. Key features include:

- **Stateful Iteration:** Maintain state across iterations, enabling workflows to track progress, handle retries, and manage conditional branching within loops.
- **Dynamic Agent Management:** Create, monitor, and terminate agents dynamically based on runtime conditions.
- **Concurrency Controls:** Configure parallelism levels to optimize throughput and resource utilization.
- **Error Handling and Compensation:** Built-in mechanisms to handle failures within agents and implement compensation logic.
- **Integration with Logic Apps Designer:** Visual tooling support to design Agent Loop workflows intuitively.

**Technical Mechanisms and Implementation Methods**  
Agent Loop leverages the underlying Azure Logic Apps (Standard) runtime, which is built on a containerized, event-driven architecture supporting durable state management. The implementation uses durable task patterns similar to Durable Functions, where each agent represents a durable task that can persist state and resume after interruptions. The loop construct orchestrates these agents, managing their lifecycle through checkpoints stored in Azure Storage or other configured state stores. Developers define the loop logic using the Logic Apps Standard designer or ARM templates, specifying agent creation criteria, iteration conditions, and concurrency parameters.

**Use Cases and Application Scenarios**  
Agent Loop is particularly suited for scenarios requiring complex iterative processing, such as:

- **Order Processing Pipelines:** Sequentially or concurrently process multiple orders, with each agent handling an individual order lifecycle.
- **Batch Data Processing:** Iterate over large datasets, spawning agents to process data chunks in parallel while maintaining overall workflow state.
- **Human-in-the-Loop Workflows:** Manage approval processes where agents represent tasks assigned to different users, with stateful tracking of responses.
- **IoT Device Management:** Orchestrate commands and status checks across fleets of devices, handling retries and conditional logic per device.

**Important Considerations and Limitations**  
While Agent Loop enhances workflow capabilities, users should consider:

- **Resource Consumption:** Running multiple agents concurrently can increase compute and storage costs; concurrency settings should be tuned accordingly.
- **State Management Overhead:** Persisting state for long-running agents requires reliable storage configuration and may introduce latency.
- **Complexity in Debugging:** Iterative and concurrent workflows can be more challenging to debug; leveraging Azure Monitor and Logic Apps diagnostics is recommended.
- **Compatibility:** Agent Loop is currently available only in the Logic Apps (Standard) environment and may not be supported in Consumption-based Logic Apps.

**Integration with Related Azure Services**  
Agent Loop workflows can seamlessly integrate with a broad range of Azure services:

- **Azure Functions:** Invoke serverless functions as part of agent tasks for custom processing.
- **Azure Event Grid and Service Bus:** React to events and messages within loop iterations.
- **Azure Storage and Cosmos DB:** Persist state and intermediate data for agents.
- **Azure Monitor and Application Insights:** Monitor workflow execution, performance, and errors.
- **Azure Active Directory:** Manage secure access and approvals in human-in

---

### 104. Generally Available: Automated Testing Framework for Logic Apps [Standard]

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Automated Testing Framework for Logic Apps [Standard]](https://azure.microsoft.com/updates?id=527644)

**Update ID**: 527644
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps

**Summary**:

- What was updated  
Azure Logic Apps (Standard) now supports automated testing through the Visual Studio Code extension, released as generally available.

- Key changes or new features  
Developers and integration specialists can create, run, and manage automated tests directly within VS Code for Logic Apps (Standard) workflows. This feature streamlines validation of workflow logic, improves reliability, and accelerates development cycles by enabling early detection of issues. The testing framework supports defining test cases, input parameters, expected outputs, and integrates with CI/CD pipelines.

- Target audience affected  
Developers building Logic Apps (Standard) workflows, integration engineers, and DevOps professionals responsible for workflow quality assurance and deployment automation.

- Important notes if any  
This capability is currently available only for Logic Apps (Standard) and requires the latest version of the Azure Logic Apps VS Code extension. Leveraging automated tests can significantly reduce manual testing efforts and improve workflow robustness in production environments.

For more details, visit: https://azure.microsoft.com/updates?id=527644

**Details**:

The Azure update announcing the general availability of the Automated Testing Framework for Logic Apps (Standard) within the Visual Studio Code extension introduces a significant enhancement aimed at improving the development lifecycle and reliability of Logic Apps workflows. This update addresses the need for robust, repeatable testing processes in integration scenarios, enabling developers and integration specialists to validate their workflows early and continuously.

**Background and Purpose**  
Azure Logic Apps (Standard) provides a platform for building scalable, event-driven integration workflows. Prior to this update, testing Logic Apps often involved manual execution or external orchestration, which could be error-prone and time-consuming. The purpose of this update is to embed automated testing capabilities directly into the development environment, streamlining validation and reducing deployment risks by catching issues before production.

**Specific Features and Detailed Changes**  
- **Automated Testing Support in VS Code Extension:** Developers can now create, run, and manage automated tests for Logic Apps (Standard) directly within Visual Studio Code, leveraging the existing extension.  
- **Test Case Definition:** The framework allows defining test cases that specify inputs, expected outputs, and validation criteria for Logic Apps workflows.  
- **Mocking and Dependency Simulation:** It supports mocking connectors and external dependencies, enabling isolated testing of workflow logic without invoking live services.  
- **Test Execution and Reporting:** Tests can be executed locally or as part of CI/CD pipelines, with detailed pass/fail results and logs to facilitate debugging.  
- **Integration with Source Control:** Test definitions and results can be version-controlled alongside Logic Apps code, promoting DevOps best practices.

**Technical Mechanisms and Implementation Methods**  
The automated testing framework leverages the extensibility of the Logic Apps Standard runtime and the VS Code extension to intercept and simulate workflow triggers and actions. It uses JSON-based test definitions that specify input payloads and expected outputs. The framework can mock connectors by substituting real HTTP calls or API invocations with predefined responses, ensuring tests run deterministically and without external dependencies. Test execution is orchestrated through VS Code commands or integrated into Azure DevOps pipelines using CLI commands, enabling automated validation during build and release stages.

**Use Cases and Application Scenarios**  
- **Regression Testing:** Ensuring that changes to Logic Apps workflows do not break existing functionality.  
- **Continuous Integration/Continuous Deployment (CI/CD):** Automated tests can be integrated into CI/CD pipelines to validate workflows before deployment.  
- **Development Validation:** Developers can quickly verify workflow logic locally during development, reducing iteration cycles.  
- **Complex Workflow Validation:** Testing workflows with multiple connectors and conditional logic by mocking external services to isolate and validate specific paths.

**Important Considerations and Limitations**  
- The framework currently supports Logic Apps (Standard) and may not be fully compatible with Logic Apps (Consumption) workflows.  
- Mocking capabilities depend on the connectors and actions used; some complex or custom connectors might require additional configuration.  
- While automated testing improves reliability, it does not replace the need for end-to-end integration testing in staging environments.  
- Test maintenance is required as workflows evolve, necessitating updates to test definitions and mocks.

**Integration with Related Azure Services**  
- **Azure DevOps and GitHub Actions:** The testing framework can be integrated into CI/CD pipelines using Azure DevOps or GitHub Actions, enabling automated validation during deployment workflows.  
- **Azure Monitor and Application Insights:** Test results and logs can be correlated with monitoring data to diagnose issues in production.  
- **Azure API Management:** When Logic Apps expose APIs, automated tests can validate API contracts and behavior as part of the testing suite.  
- **Azure Functions:** Logic Apps that invoke Azure Functions can mock function responses during tests to isolate workflow logic.

In summary, the general availability of the Automated Testing Framework for Logic Apps (Standard) in the Visual Studio Code extension equips developers with a powerful toolset to automate validation of integration workflows, enhancing reliability and accelerating development through integrated, mock-enabled testing and seamless CI/CD integration.

---

### 105. Generally Available: Govern Model Context Protocol (MCP) endpoints using Azure API Management

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Govern Model Context Protocol (MCP) endpoints using Azure API Management](https://azure.microsoft.com/updates?id=527626)

**Update ID**: 527626
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management

**Summary**:

- What was updated  
Azure API Management (APIM) now generally supports governance of Model Context Protocol (MCP) endpoints.

- Key changes or new features  
This update extends APIM’s governance, security, and observability capabilities to MCP endpoints, which are used by AI-driven workloads. It enables enterprises to apply consistent API management policies—such as authentication, throttling, logging, and monitoring—to MCP-based AI services. This integration helps ensure secure, compliant, and manageable AI model interactions within existing API ecosystems.

- Target audience affected  
Developers and IT professionals managing AI workloads and APIs, especially those integrating AI models via MCP endpoints, will benefit from enhanced control and visibility. Enterprises adopting AI at scale can leverage APIM to unify governance across traditional APIs and AI model endpoints.

- Important notes if any  
This feature is now generally available, indicating production readiness. Organizations should evaluate their AI model deployment architectures to incorporate APIM governance for improved security and operational insights. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The recent general availability of Model Context Protocol (MCP) governance endpoints within Azure API Management (APIM) marks a significant enhancement aimed at extending Azure’s robust API governance, security, and observability capabilities to AI-driven workloads. This update addresses the growing need for enterprises to manage and secure interactions with AI models in a standardized, scalable manner.

**Background and Purpose:**  
As AI workloads become increasingly integral to enterprise applications, managing the communication and governance of AI model contexts—such as metadata, input/output schemas, and operational parameters—has become critical. The Model Context Protocol (MCP) defines a standardized way to expose and govern these model interactions. By integrating MCP endpoints into Azure API Management, Microsoft enables organizations to apply consistent API governance policies, security controls, and monitoring to AI model endpoints, similar to traditional APIs. This ensures compliance, reliability, and operational insight across AI services.

**Specific Features and Detailed Changes:**  
- **MCP Endpoint Governance:** Azure API Management now supports the registration, exposure, and governance of MCP endpoints, allowing enterprises to manage AI model context interactions through APIM’s policy framework.  
- **Security Enhancements:** Enterprises can enforce authentication, authorization, rate limiting, and threat protection on MCP endpoints, mitigating risks associated with AI model access.  
- **Observability and Analytics:** Integration with APIM’s telemetry enables detailed logging, metrics, and diagnostics for AI model interactions, facilitating troubleshooting and performance monitoring.  
- **Policy Application:** Existing APIM policies (e.g., validation, transformation, caching) can be applied to MCP endpoints, enabling flexible request/response handling tailored to AI workloads.

**Technical Mechanisms and Implementation Methods:**  
MCP endpoints are exposed as RESTful APIs representing AI model contexts. Within APIM, these endpoints are imported or defined as API entities, allowing administrators to apply policies at various scopes (global, product, API, operation). Authentication mechanisms such as OAuth 2.0, managed identities, or subscription keys can be enforced. APIM’s built-in analytics pipeline collects telemetry data, which can be routed to Azure Monitor, Log Analytics, or third-party SIEM tools. The governance model leverages APIM’s extensible policy expressions to validate and transform MCP payloads, ensuring compliance with enterprise standards.

**Use Cases and Application Scenarios:**  
- **Enterprise AI Governance:** Organizations deploying AI models across multiple teams can centrally manage access, monitor usage, and enforce compliance policies on model context interactions.  
- **Secure AI Model Consumption:** Enterprises exposing AI models as services can protect them from unauthorized or abusive access using APIM’s security features.  
- **Operational Monitoring:** DevOps teams can track AI model performance and usage patterns through integrated telemetry, enabling proactive incident response.  
- **Hybrid AI Architectures:** MCP governance via APIM supports scenarios where AI models are deployed on-premises, in Azure, or at the edge, providing a unified governance layer.

**Important Considerations and Limitations:**  
- **Compatibility:** MCP governance requires AI models to expose context endpoints conforming to the MCP specification; legacy or proprietary AI endpoints may need adaptation.  
- **Policy Complexity:** Applying complex APIM policies to MCP endpoints requires careful design to avoid performance overhead or unintended request transformations.  
- **Latency Impact:** Introducing APIM as a governance layer may add minimal latency; performance testing is recommended for latency-sensitive AI workloads.  
- **Feature Maturity:** As a newly GA feature, ongoing updates may introduce enhancements; staying current with Azure documentation is advised.

**Integration with Related Azure Services:**  
- **Azure Cognitive Services:** MCP governance can be applied to custom AI models integrated with Cognitive Services, enhancing security and observability.  
- **Azure Monitor and Log Analytics:** Telemetry from MCP endpoints managed by APIM can be ingested into Azure Monitor for comprehensive monitoring and alerting.  
- **Azure Active Directory (AAD):** Authentication and authorization for MCP endpoints can leverage AAD identities and roles, enabling enterprise-grade

---

### 106. Announcing: API Center Standard now included at no additional cost for linked Azure API Management Standard and Premium tiers

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Announcing: API Center Standard now included at no additional cost for linked Azure API Management Standard and Premium tiers](https://azure.microsoft.com/updates?id=527621)

**Update ID**: 527621
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Features, Microsoft Ignite, Pricing & Offerings

**Summary**:

- What was updated  
Azure API Management’s API Center Standard, previously a separate paid feature, is now included at no additional cost for linked API Management Standard and Premium tier instances.

- Key changes or new features  
API Center Standard can be enabled and linked directly with Azure API Management Standard and Premium services without additional charges. This integration simplifies API publishing and discovery by providing a centralized developer portal experience. It enhances API lifecycle management and developer engagement capabilities within existing API Management deployments.

- Target audience affected  
Developers and IT professionals managing APIs using Azure API Management Standard and Premium tiers. This update benefits API architects, platform engineers, and DevOps teams responsible for API governance and developer onboarding.

- Important notes if any  
The no-cost inclusion applies only when an API Center instance is linked to a corresponding Azure API Management Standard or Premium service. This does not apply to other tiers or standalone API Center usage. Users should review their existing API Management configurations to enable and leverage the integrated API Center Standard features effectively.

For more details, visit: https://azure.microsoft.com/updates?id=527621

**Details**:

The recent Azure update announces that API Center Standard, previously offered as a separate paid service, is now included at no additional cost for customers using Azure API Management (APIM) Standard and Premium tiers when an API Center instance is linked to the corresponding APIM service. This change aims to streamline API lifecycle management by integrating API Center capabilities directly into existing APIM deployments, enhancing developer productivity and governance without extra licensing fees.

**Background and Purpose**  
Azure API Management is a comprehensive platform for publishing, securing, and analyzing APIs. API Center was introduced as a dedicated environment for API design, collaboration, and governance, but it was previously billed separately, which could complicate cost management and adoption. By bundling API Center Standard with APIM Standard and Premium tiers, Microsoft simplifies the API management ecosystem, encouraging broader use of API design and governance tools within enterprise-grade API deployments.

**Specific Features and Detailed Changes**  
API Center Standard provides a centralized hub for API design, documentation, versioning, and collaboration. Key features include:  
- API specification management (OpenAPI, WSDL, etc.)  
- Collaborative API design and review workflows  
- Version control and change tracking for API definitions  
- Integration with Azure DevOps and Git repositories for CI/CD pipelines  
- Automated policy generation and validation aligned with APIM policies  

With this update, these features are now accessible without additional licensing costs for customers who link an API Center instance to their APIM Standard or Premium service. This linkage enables seamless synchronization of API definitions and policies between API Center and the APIM gateway, ensuring consistency across design and runtime environments.

**Technical Mechanisms and Implementation Methods**  
To utilize the included API Center Standard, customers must create or link an API Center instance to their existing APIM Standard or Premium service. This linkage establishes a secure connection allowing API Center to pull API definitions from APIM and push updates back to the APIM gateway. The synchronization leverages REST APIs and Azure Resource Manager (ARM) templates under the hood, enabling automated deployment and version control. Authentication and authorization are managed via Azure Active Directory (AAD), ensuring enterprise-grade security and compliance.

API Center supports importing existing API specifications from APIM or external sources, enabling iterative design and deployment workflows. Changes made in API Center can be published directly to the APIM service, triggering policy updates and version rollouts without manual intervention.

**Use Cases and Application Scenarios**  
- **Enterprise API Governance:** Organizations can enforce consistent API design standards and lifecycle policies across multiple teams by centralizing API specifications in API Center.  
- **DevOps Integration:** API Center’s integration with Azure DevOps and Git enables automated API deployment pipelines, improving release velocity and reducing errors.  
- **API Collaboration:** Distributed teams can collaborate on API design and documentation within API Center, streamlining feedback and approval processes.  
- **Multi-Environment Management:** API Center facilitates managing API versions and deployments across development, staging, and production environments linked to APIM.  

**Important Considerations and Limitations**  
- The inclusion applies only when an API Center instance is linked to an APIM Standard or Premium tier; standalone API Center instances or those linked to lower-tier APIM services are not covered.  
- While API Center Standard is included, advanced or premium features beyond the Standard tier may still require separate licensing.  
- Customers should evaluate existing API governance workflows to integrate API Center effectively, as it introduces new processes and tooling.  
- Proper role-based access control (RBAC) configuration in AAD is essential to secure API design and deployment operations.  

**Integration with Related Azure Services**  
- **Azure API Management:** Core integration enabling API lifecycle synchronization between design (API Center) and runtime (APIM gateway).  
- **Azure DevOps/GitHub:** Supports CI/CD pipelines for automated API deployment and version control.  
- **Azure Active Directory:** Provides authentication and authorization for secure access to API Center and APIM resources.  
- **Azure Monitor and Application

---

### 107. Generally Available: Premium v2 tier in Azure API Management

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Premium v2 tier in Azure API Management](https://azure.microsoft.com/updates?id=527612)

**Update ID**: 527612
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management

**Summary**:

- What was updated  
Azure API Management Premium v2 tier is now generally available.

- Key changes or new features  
Premium v2 offers enhanced performance and scalability for enterprise-grade API management. It supports the highest entity limits compared to previous tiers and includes unlimited API calls without additional charges. This tier is designed to handle large-scale, mission-critical workloads with improved throughput and reliability.

- Target audience affected  
Developers and IT professionals managing APIs at enterprise scale, especially those requiring high performance, extensive API usage, and robust scalability.

- Important notes if any  
Organizations currently using Premium v1 can consider upgrading to Premium v2 to leverage improved capabilities. Pricing and detailed feature comparisons are available on the Azure portal. This update enables more cost-effective scaling for heavy API traffic scenarios.

**Details**:

The Azure API Management Premium v2 tier has reached general availability, representing Microsoft’s latest enhancement to its enterprise-grade API management platform designed for large-scale, high-throughput environments. This update addresses the growing need for robust, scalable, and high-performance API gateways that support complex organizational requirements.

**Background and Purpose**  
Azure API Management (APIM) enables organizations to publish, secure, transform, maintain, and monitor APIs. The Premium tier has traditionally catered to enterprises requiring multi-region deployment, virtual network integration, and advanced security features. The introduction of the Premium v2 tier responds to increasing demands for improved performance, higher throughput, and expanded capacity limits, helping enterprises manage APIs more efficiently at scale.

**Specific Features and Detailed Changes**  
Premium v2 significantly enhances performance metrics and capacity limits compared to the original Premium tier. Key improvements include:  
- **Superior Performance:** Optimized backend infrastructure and updated runtime components reduce latency and increase request throughput.  
- **Highest Entity Limits:** Premium v2 supports a larger number of APIs, products, and subscriptions within a single APIM instance, enabling more extensive API ecosystems.  
- **Unlimited Included API Calls:** Unlike previous tiers that imposed caps on included API calls, Premium v2 removes these restrictions, allowing enterprises to handle massive API traffic without additional cost concerns.  
- **Enhanced Scalability:** The tier supports larger scale units and improved autoscaling capabilities, facilitating dynamic adjustment to traffic spikes.  
- **Multi-region Deployment:** Continued support for multi-region active-active deployments ensures high availability and low latency for global users.

**Technical Mechanisms and Implementation Methods**  
Premium v2 leverages updated Azure infrastructure components, including enhanced compute and networking resources, to deliver its performance gains. The tier supports deployment within Azure Virtual Networks (VNet), enabling secure, private connectivity to backend services. It also integrates with Azure Private Link for secure API exposure. The autoscaling mechanism is refined to respond more rapidly to traffic changes, using Azure Monitor metrics and Azure Logic Apps or Azure Functions for custom scaling rules. Migration to Premium v2 is supported via the Azure portal or ARM templates, allowing seamless upgrade paths from existing Premium instances.

**Use Cases and Application Scenarios**  
Premium v2 is ideal for:  
- Large enterprises with extensive API portfolios requiring high throughput and low latency.  
- Organizations needing multi-region deployments for global reach and disaster recovery.  
- Scenarios demanding strict network isolation and security via VNet integration.  
- API ecosystems involving thousands of APIs and millions of calls daily, such as financial services, telecommunications, and retail.  
- Environments requiring advanced analytics, monitoring, and developer engagement at scale.

**Important Considerations and Limitations**  
- Premium v2 is a higher-cost tier, intended for enterprise-scale workloads; smaller projects may not justify the expense.  
- While included API calls are unlimited, outbound data transfer and other ancillary costs still apply.  
- Migration requires careful planning to avoid downtime, especially for multi-region deployments.  
- Some legacy features or custom policies may require validation for compatibility with the new runtime.  
- Regional availability should be confirmed, as new tiers may roll out progressively across Azure regions.

**Integration with Related Azure Services**  
Premium v2 integrates tightly with Azure services to enhance API management:  
- **Azure Active Directory (AAD):** For secure authentication and authorization of API consumers.  
- **Azure Monitor and Azure Application Insights:** For detailed telemetry, diagnostics, and alerting.  
- **Azure Key Vault:** To securely manage API secrets, certificates, and keys.  
- **Azure Front Door and Azure Traffic Manager:** To optimize global traffic routing to multi-region APIM deployments.  
- **Azure DevOps and GitHub Actions:** For CI/CD pipelines automating API lifecycle management.  
- **Azure Private Link and VNet Integration:** To secure backend connectivity and API exposure.

In summary, the general availability of Azure API Management Premium v2 tier provides enterprise IT professionals with a highly scalable

---

### 108. Generally Available: OpenShift Virtualization now available on Azure Red Hat OpenShift

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: OpenShift Virtualization now available on Azure Red Hat OpenShift](https://azure.microsoft.com/updates?id=527236)

**Update ID**: 527236
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift

**Summary**:

- What was updated  
Red Hat OpenShift Virtualization is now generally available (GA) on Azure Red Hat OpenShift (ARO).

- Key changes or new features  
This GA release enables seamless management of virtual machines alongside containers within a single cloud-native platform. It integrates virtualization capabilities directly into ARO, allowing developers and IT teams to run and manage VMs and container workloads uniformly. The update incorporates feedback from the previous preview, improving stability, performance, and usability.

- Target audience affected  
Developers and IT professionals using Azure Red Hat OpenShift who require hybrid workload management combining VMs and containers. This is particularly relevant for teams modernizing legacy applications or running mixed workloads in a Kubernetes environment.

- Important notes if any  
Users can now leverage OpenShift Virtualization to simplify infrastructure management and accelerate application modernization on Azure. It is recommended to review the updated documentation and best practices for deploying and managing virtualized workloads within ARO to maximize benefits.

**Details**:

The general availability of Red Hat OpenShift Virtualization on Azure Red Hat OpenShift (ARO) marks a significant enhancement for enterprises seeking unified management of virtual machines (VMs) and containerized workloads within a single cloud-native platform. This update addresses the growing need for hybrid workload orchestration by integrating KubeVirt-based virtualization directly into ARO, enabling IT professionals to run and manage VMs alongside containers using Kubernetes-native tools and APIs.

**Background and Purpose**  
Traditionally, organizations have operated separate environments for virtual machines and containers, leading to operational complexity and silos. Red Hat OpenShift Virtualization, built on the open-source KubeVirt project, extends Kubernetes capabilities to include VM lifecycle management, allowing users to consolidate infrastructure and streamline DevOps workflows. By making OpenShift Virtualization generally available on ARO, Microsoft and Red Hat aim to provide a fully managed, enterprise-grade solution that simplifies hybrid workload management on Azure, leveraging the scalability, security, and compliance features of the cloud.

**Specific Features and Detailed Changes**  
This GA release incorporates feedback from the preview phase, delivering a stable, production-ready experience with enhanced performance and reliability. Key features include:

- **Unified Management:** Ability to create, run, and manage VMs using OpenShift’s web console and CLI alongside container workloads.
- **KubeVirt Integration:** VMs run as custom Kubernetes resources, enabling native Kubernetes scheduling, scaling, and networking.
- **Live Migration:** Support for live migration of VMs to minimize downtime during maintenance or scaling operations.
- **Storage and Networking:** Integration with OpenShift Container Storage and Azure networking services, supporting persistent storage for VMs and advanced network policies.
- **Security and Compliance:** Leverages Azure’s security infrastructure and OpenShift’s role-based access control (RBAC) for secure multi-tenant environments.

**Technical Mechanisms and Implementation Methods**  
OpenShift Virtualization uses KubeVirt to extend Kubernetes with virtualization capabilities by defining VM workloads as Kubernetes custom resources (VirtualMachine, VirtualMachineInstance). The operator-based deployment automates installation and management of virtualization components on ARO clusters. VMs run inside Kubernetes pods with QEMU/KVM as the hypervisor, abstracted by Kubernetes APIs. Storage is provisioned via Container Storage Interface (CSI) drivers, often backed by Azure Disk or Azure Files through OpenShift Container Storage. Networking is managed through OpenShift SDN or Azure CNI, enabling VM connectivity with container workloads and external networks. Live migration leverages KubeVirt’s migration controller to move VM state between nodes without service interruption.

**Use Cases and Application Scenarios**  
- **Legacy Application Modernization:** Run traditional VM-based applications alongside new containerized microservices within the same cluster.
- **Dev/Test Environments:** Quickly provision VM and container workloads for development and testing without managing separate infrastructure.
- **Hybrid Workloads:** Consolidate workloads that require virtualization (e.g., Windows Server VMs) with cloud-native applications for unified monitoring and scaling.
- **Disaster Recovery and Migration:** Use live migration and snapshot capabilities to improve availability and facilitate migration to cloud-native environments.

**Important Considerations and Limitations**  
- **Resource Overhead:** Running VMs inside Kubernetes pods introduces additional resource overhead; capacity planning is essential.
- **Compatibility:** Not all VM workloads may be fully compatible with KubeVirt; testing is recommended before production deployment.
- **Networking Complexity:** Advanced networking scenarios may require detailed configuration of Azure CNI and OpenShift SDN.
- **Operational Expertise:** Teams need familiarity with both Kubernetes and virtualization concepts to effectively manage the environment.

**Integration with Related Azure Services**  
- **Azure Red Hat OpenShift:** Provides the managed Kubernetes platform hosting OpenShift Virtualization.
- **Azure Storage:** Supports persistent volumes for VM disks via Azure Disk and Azure Files integrated through OpenShift Container Storage.
- **Azure Networking:** Enables VM and container networking with Azure CNI, load balancers, and network security groups.
- **Azure Monitor

---

### 109. Public Preview: Microsoft Foundry Fine-Tuning Updates

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Microsoft Foundry Fine-Tuning Updates](https://azure.microsoft.com/updates?id=526742)

**Update ID**: 526742
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry Fine-Tuning has been updated with a complete redesign of its user interface.

- Key changes or new features  
The new UI delivers an agent-first experience tailored for developers and data scientists, simplifying workflows around model creation, evaluation, and deployment. It also introduces integration with Visual Studio (VS), enhancing development productivity and streamlining the fine-tuning process.

- Target audience affected  
Developers, data scientists, and IT professionals involved in building, fine-tuning, and deploying AI models using Microsoft Foundry.

- Important notes if any  
This update is currently in public preview, allowing users to explore the redesigned interface and new features ahead of general availability. Users should provide feedback to help refine the experience. Integration with VS suggests improved support for development environments, which may require updating existing workflows.  

For more details, visit: https://azure.microsoft.com/updates?id=526742

**Details**:

The recent Public Preview update for Microsoft Foundry Fine-Tuning introduces a comprehensive redesign of the Foundry user interface, aimed at enhancing the developer and data scientist experience by adopting an agent-first approach. This update reflects Microsoft’s commitment to simplifying and accelerating the lifecycle of custom AI model development within Azure.

**Background and Purpose**  
Microsoft Foundry Fine-Tuning is a service designed to enable users to customize large language models (LLMs) and AI agents to better fit specific organizational data and use cases. Prior to this update, the UI and workflows were more generalized, which could lead to complexity and inefficiencies for developers and data scientists focusing on agent-based AI solutions. The purpose of this update is to streamline the process of creating, evaluating, and deploying fine-tuned models, making it more intuitive and integrated with common development tools.

**Specific Features and Detailed Changes**  
- **Agent-First UI Redesign:** The new interface centers around building AI agents rather than just models, reflecting the growing trend of agent-based AI applications. This shift allows users to define agent behaviors, interactions, and workflows more naturally.  
- **Streamlined Model Lifecycle:** The update consolidates model creation, evaluation, and deployment into a cohesive workflow, reducing the number of manual steps and context switches.  
- **Integration with Visual Studio (VS):** Developers can now interact with Foundry Fine-Tuning directly within Visual Studio, enabling a seamless development experience that leverages familiar IDE features such as debugging, version control, and code editing.  
- **Enhanced Evaluation Tools:** The UI provides richer evaluation metrics and visualization options to assess model performance and behavior, facilitating more informed fine-tuning decisions.  
- **Improved Deployment Options:** Deployment workflows have been optimized to support faster rollouts and easier management of fine-tuned agents in production environments.

**Technical Mechanisms and Implementation Methods**  
The update leverages Azure’s underlying AI infrastructure, including Azure Machine Learning and Azure Cognitive Services, to manage model training, versioning, and deployment. The agent-first design abstracts complex model tuning parameters into higher-level constructs representing agent capabilities and intents. Integration with Visual Studio is implemented via extensions and APIs that connect the IDE to Foundry’s backend services, enabling direct interaction with model artifacts and deployment pipelines. The UI redesign is built using modern web frameworks ensuring responsiveness and extensibility.

**Use Cases and Application Scenarios**  
- **Custom AI Agents:** Organizations can build specialized conversational agents tailored to their domain knowledge, such as customer support bots or internal knowledge assistants.  
- **Data Scientist Workflows:** Data scientists can rapidly iterate on model fine-tuning with improved evaluation tools, accelerating experimentation cycles.  
- **Developer Integration:** Developers can embed fine-tuned agents into applications with greater ease, leveraging VS integration for streamlined coding and deployment.  
- **Enterprise Automation:** Fine-tuned agents can automate complex workflows by understanding and acting on domain-specific instructions, improving operational efficiency.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview, the update may have limited SLA guarantees and could undergo significant changes before general availability.  
- **Learning Curve:** The agent-first paradigm may require users to adapt existing workflows and understand new abstractions around agent design.  
- **Resource Requirements:** Fine-tuning large models remains resource-intensive; users should plan for adequate compute and storage resources within their Azure subscriptions.  
- **Compliance and Security:** Users must ensure that data used for fine-tuning complies with organizational policies and regulatory requirements, especially when handling sensitive information.

**Integration with Related Azure Services**  
- **Azure Machine Learning:** Provides the compute infrastructure and experiment tracking for model training and fine-tuning.  
- **Azure Cognitive Services:** Supplies foundational AI models that can be fine-tuned within Foundry.  
- **Azure DevOps and GitHub:** Integration with VS supports source control and CI/CD pipelines for managing model lifecycle and deployment.  
- **Azure Kubernetes Service (AKS):** Facilitates scalable

---

### 110. Public Preview: Microsoft Foundry Control Plane & Entra Agent ID

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Microsoft Foundry Control Plane & Entra Agent ID](https://azure.microsoft.com/updates?id=526665)

**Update ID**: 526665
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft announced the public preview of Microsoft Foundry Control Plane and Entra Agent ID, a unified platform designed to enhance enterprise AI agent observability, security, and governance.

- Key changes or new features  
The Control Plane integrates identity management, monitoring, and compliance capabilities into a centralized system. It provides deep observability into AI agents’ behavior and interactions, enabling organizations to enforce security policies and maintain compliance more effectively. The Entra Agent ID component offers identity-based control and authentication for AI agents, improving trust and governance in AI deployments.

- Target audience affected  
This update primarily targets developers building AI agents and IT professionals responsible for enterprise security, compliance, and governance of AI workloads. It is especially relevant for organizations deploying AI at scale who require centralized control and monitoring.

- Important notes if any  
The offering is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Integration with existing Azure security and compliance tools is expected to streamline adoption. Users should monitor updates for GA release and expanded capabilities.

For more details, visit: https://azure.microsoft.com/updates?id=526665

**Details**:

The recent public preview announcement of Microsoft Foundry Control Plane and Entra Agent ID introduces a unified platform designed to enhance enterprise AI agent observability, security, and governance by integrating identity, monitoring, and compliance capabilities into a centralized control plane. This update addresses the growing complexity and risk associated with deploying AI agents at scale within enterprise environments, providing IT professionals with a comprehensive framework to manage AI agents securely and transparently.

**Background and Purpose**  
As enterprises increasingly adopt AI agents for automation, decision-making, and customer engagement, managing these agents’ identities, activities, and compliance requirements becomes critical. Traditional monitoring and governance tools often lack the granularity and integration needed for AI-specific workloads. Microsoft Foundry’s Control Plane aims to fill this gap by offering a unified platform that consolidates identity management, observability, and compliance controls tailored for AI agents, thereby reducing operational risk and improving governance posture.

**Specific Features and Detailed Changes**  
- **Unified Control Plane:** Centralizes management of AI agents’ lifecycle, including provisioning, identity assignment, activity monitoring, and compliance auditing.  
- **Entra Agent ID Integration:** Extends Microsoft Entra’s identity capabilities to AI agents, enabling unique, verifiable identities for each agent instance. This facilitates fine-grained access control and traceability.  
- **Deep Observability:** Provides detailed telemetry and monitoring of agent behavior, interactions, and performance metrics, enabling anomaly detection and operational insights.  
- **Compliance and Governance:** Embeds compliance policies and automated auditing within the platform, ensuring AI agents operate within defined regulatory and organizational boundaries.  
- **Security Enhancements:** Incorporates identity-based security controls, including conditional access and risk-based authentication for AI agents, reducing attack surfaces and insider risks.

**Technical Mechanisms and Implementation Methods**  
The Control Plane leverages Azure-native services and Microsoft Entra identity frameworks to implement its capabilities. AI agents are assigned unique Entra Agent IDs, which are managed through Azure Active Directory (Azure AD) extensions. The platform collects telemetry data via integrated monitoring agents and Azure Monitor, feeding into centralized dashboards and alerting systems. Compliance policies are enforced using Azure Policy and Microsoft Purview integration, enabling automated compliance checks and reporting. Security controls utilize conditional access policies configured specifically for agent identities, supported by continuous risk assessment algorithms.

**Use Cases and Application Scenarios**  
- **Enterprise AI Governance:** Organizations deploying multiple AI agents across departments can centrally manage identities, monitor activities, and enforce compliance policies.  
- **Security Operations:** Security teams can detect anomalous agent behavior or unauthorized access attempts through enhanced observability and identity controls.  
- **Regulatory Compliance:** Industries with strict data governance requirements (e.g., finance, healthcare) can ensure AI agents adhere to policies and generate audit trails for inspections.  
- **Operational Monitoring:** DevOps and AI operations teams gain insights into agent performance and health, facilitating proactive maintenance and troubleshooting.

**Important Considerations and Limitations**  
- As a public preview feature, the platform may have limited regional availability and evolving functionality.  
- Integration requires alignment with existing Azure AD tenant configurations and may necessitate updates to identity governance policies.  
- Organizations must evaluate the impact on existing AI workflows and ensure compatibility with deployed AI agent frameworks.  
- Data privacy and telemetry collection should be reviewed to comply with organizational and regulatory standards.

**Integration with Related Azure Services**  
- **Microsoft Entra (Azure AD):** Core identity management for agent identities and access control.  
- **Azure Monitor:** Telemetry ingestion and observability data collection.  
- **Azure Policy and Microsoft Purview:** Compliance enforcement and auditing capabilities.  
- **Azure Security Center:** Augmented security posture management for AI agents.  
- **Azure DevOps / GitHub Actions:** Potential integration points for CI/CD pipelines managing AI agent deployments.

In summary, the Microsoft Foundry Control Plane combined with Entra Agent ID provides a centralized, identity-driven platform for managing AI agents’ security, observability, and compliance

---

### 111. Generally Available: GitHub Copilot app modernization expanded capabilities

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: GitHub Copilot app modernization expanded capabilities](https://azure.microsoft.com/updates?id=526618)

**Update ID**: 526618
**Data source**: Azure Updates API

**Categories**: Launched

**Summary**:

- What was updated  
GitHub Copilot App Modernization has expanded capabilities that are now Generally Available, enhancing support for modernizing applications, databases, and containers, and accelerating migration to Azure.

- Key changes or new features  
The update introduces improved AI-assisted code suggestions tailored for app modernization tasks, including automated refactoring for cloud-native architectures, enhanced database schema transformation support, and containerization guidance. Developers can now leverage Copilot to generate migration-ready code snippets and configuration files, reducing manual effort. Integration with Azure services is streamlined, enabling faster deployment and testing cycles.

- Target audience affected  
This update primarily benefits developers, DevOps engineers, and IT professionals involved in application modernization, cloud migration, and container management on Azure.

- Important notes if any  
The enhancements are fully Generally Available, ensuring production readiness and support. Users should review updated documentation to maximize the new features and integrate them into existing workflows for improved migration efficiency.

**Details**:

The recent general availability of expanded capabilities in the GitHub Copilot App Modernization toolset marks a significant advancement in simplifying and accelerating the modernization of legacy applications, databases, and containerized workloads for migration to Azure. This update addresses the growing demand among IT professionals and developers for automated, AI-assisted modernization workflows that reduce manual effort and improve accuracy in cloud migration projects.

**Background and Purpose**  
As enterprises increasingly adopt cloud-native architectures, the complexity of refactoring legacy applications and infrastructure for Azure poses a substantial challenge. Traditional modernization efforts require deep expertise in both source and target environments, often leading to prolonged timelines and high costs. The GitHub Copilot App Modernization enhancements aim to leverage AI-driven code analysis and generation to streamline this process, enabling developers to more efficiently transform applications and data assets to Azure-compatible formats and services.

**Specific Features and Detailed Changes**  
The update introduces several key capabilities now generally available:  
- **Automated Application Refactoring:** Enhanced AI models assist in converting legacy application codebases into cloud-native architectures, including microservices and serverless components, with recommendations for Azure App Service, Azure Functions, or AKS deployment.  
- **Database Modernization:** Tools now support automated schema conversion and data migration strategies for common databases (e.g., SQL Server, Oracle) to Azure SQL Database or Azure Cosmos DB, including guidance on indexing and performance tuning.  
- **Container Modernization:** Improved container analysis identifies legacy container images and suggests optimizations for Azure Kubernetes Service (AKS) or Azure Container Apps, including manifest generation and security best practices.  
- **Migration Acceleration:** Integrated workflows facilitate end-to-end migration planning, including dependency mapping, environment assessment, and CI/CD pipeline generation using GitHub Actions tailored for Azure deployments.

**Technical Mechanisms and Implementation Methods**  
GitHub Copilot App Modernization leverages OpenAI’s Codex models fine-tuned on extensive Azure and application modernization datasets. It analyzes source repositories, infrastructure-as-code templates, and container images to generate modernization recommendations and code snippets. The tool integrates directly within GitHub repositories, providing inline suggestions and pull request automation. It also interfaces with Azure Migrate and Azure Database Migration Service APIs to orchestrate migration tasks and validate compatibility.

**Use Cases and Application Scenarios**  
- Enterprises migrating monolithic .NET or Java applications to microservices on AKS or Azure Functions.  
- Database administrators converting on-premises Oracle or SQL Server databases to managed Azure SQL or Cosmos DB with minimal downtime.  
- DevOps teams containerizing legacy applications and optimizing them for cloud-native deployment patterns.  
- Development teams automating CI/CD pipelines for modernized applications using GitHub Actions integrated with Azure DevOps and Azure Resource Manager.

**Important Considerations and Limitations**  
- While AI-assisted modernization accelerates development, manual validation and testing remain critical to ensure functional parity and performance.  
- Certain legacy or proprietary application components may require custom refactoring beyond automated suggestions.  
- Security and compliance assessments should be integrated into the modernization workflow, as automated tools may not fully capture organizational policies.  
- The effectiveness of database schema conversion depends on source database complexity and feature usage; some manual tuning may be necessary.

**Integration with Related Azure Services**  
The expanded GitHub Copilot App Modernization capabilities tightly integrate with:  
- **Azure Migrate:** For discovery, assessment, and migration orchestration.  
- **Azure Database Migration Service:** To automate data transfer and schema conversion.  
- **Azure Kubernetes Service (AKS) and Azure Container Apps:** For hosting containerized workloads.  
- **Azure App Service and Azure Functions:** For deploying refactored applications as PaaS or serverless components.  
- **GitHub Actions:** To automate build, test, and deployment pipelines targeting Azure environments.

In summary, the general availability of these enhanced GitHub Copilot App Modernization features provides IT professionals with a powerful AI-driven toolkit to accelerate application and database modernization, reduce migration complexity, and

---

### 112. Generally Available: Model Router in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Model Router in Microsoft Foundry](https://azure.microsoft.com/updates?id=526330)

**Update ID**: 526330
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry’s Model Router feature is now generally available.

- Key changes or new features  
The Model Router acts as an AI orchestration layer that dynamically selects the most optimal AI model for each prompt, improving response relevance and efficiency. It now supports an expanded set of models including the GPT-4 family, GPT-5 family, GPT-oss, and Deepse, enabling developers to leverage a wider variety of AI capabilities seamlessly within their applications.

- Target audience affected  
Developers building AI-powered applications and IT professionals managing AI workloads on Azure who require flexible, scalable, and intelligent model selection to optimize performance and cost.

- Important notes if any  
With general availability, the Model Router is production-ready, allowing integration into enterprise-grade solutions. Users should evaluate model selection strategies and monitor usage to maximize benefits. Refer to official documentation for configuration details and supported models to ensure compatibility with existing workflows.

Link for more details: https://azure.microsoft.com/updates?id=526330

**Details**:

The recent general availability (GA) of the Model Router in Microsoft Foundry marks a significant advancement in AI model orchestration within Azure’s AI ecosystem. This update introduces a dynamic AI orchestration layer designed to intelligently route user prompts to the most appropriate AI model, optimizing performance, cost, and accuracy based on the request context.

**Background and Purpose**  
As AI adoption grows, organizations often face challenges in selecting the best model for diverse workloads—balancing factors such as latency, cost, and output quality. Traditionally, developers manually select models or build custom routing logic, which can be complex and inefficient. The Model Router addresses this by providing an automated, scalable solution that dynamically selects the optimal model for each prompt, streamlining AI integration and improving overall system responsiveness.

**Specific Features and Detailed Changes**  
- **Dynamic Model Selection:** The Model Router evaluates incoming prompts and routes them to the most suitable model from a supported pool, which now includes the GPT-4 family, GPT-5 family, GPT-oss (open-source models), and Deepse (likely a specialized or domain-specific model).  
- **Broader Model Support:** Expansion beyond GPT-4 to include GPT-5 and open-source models enables users to leverage cutting-edge and customizable AI capabilities within a unified framework.  
- **Performance Optimization:** By selecting models based on prompt characteristics, the router can optimize for speed, cost-efficiency, or output quality dynamically.  
- **Seamless Integration:** The router acts as an abstraction layer, simplifying the developer experience by eliminating the need to manage multiple model endpoints manually.

**Technical Mechanisms and Implementation Methods**  
The Model Router operates as an AI orchestration service within Microsoft Foundry, leveraging metadata and heuristics about prompt content, complexity, and user-defined policies to determine routing. It likely uses a combination of prompt classification, historical performance data, and cost models to make decisions in real-time. The router interfaces with Azure OpenAI Service endpoints and potentially custom or third-party model APIs, abstracting endpoint management and load balancing. Implementation details suggest a microservices architecture with scalable API gateways and telemetry for monitoring model performance and routing efficacy.

**Use Cases and Application Scenarios**  
- **Enterprise AI Applications:** Enterprises can deploy intelligent assistants or content generation tools that automatically leverage the best model for each user query without manual intervention.  
- **Cost-Sensitive Workloads:** Applications can route simpler prompts to less expensive models (e.g., GPT-oss) while reserving premium models (GPT-5) for complex tasks, optimizing cloud spend.  
- **Multi-Domain AI Solutions:** Organizations with diverse AI needs (e.g., customer support, code generation, data analysis) can unify their AI strategy under one routing layer.  
- **Rapid Experimentation:** Data scientists can test new models by adding them to the router’s pool and comparing performance without changing application code.

**Important Considerations and Limitations**  
- **Model Availability and Latency:** While the router optimizes selection, latency may vary depending on the chosen model’s infrastructure and geographic location.  
- **Policy Configuration:** Effective use requires careful configuration of routing policies and thresholds to align with business goals (e.g., prioritizing cost vs. accuracy).  
- **Security and Compliance:** Routing sensitive data through multiple models necessitates adherence to compliance standards and secure data handling practices.  
- **Model Updates:** Continuous updates to underlying models require monitoring to ensure routing logic remains optimal.

**Integration with Related Azure Services**  
The Model Router integrates tightly with Azure OpenAI Service, enabling seamless access to Microsoft’s proprietary GPT models. It can be combined with Azure Cognitive Services for enriched AI capabilities and Azure Monitor for telemetry and diagnostics. Additionally, integration with Azure API Management and Azure Functions allows embedding the router into broader application workflows and automation pipelines. This update complements Azure Machine Learning by providing a production-ready inference orchestration layer, facilitating hybrid AI deployments that mix custom and prebuilt models.

In summary, the GA release of

---

### 113. Private Preview: Foundry Local Android support

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Private Preview: Foundry Local Android support](https://azure.microsoft.com/updates?id=526198)

**Update ID**: 526198
**Data source**: Azure Updates API

**Categories**: In development, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure Foundry Local has expanded its platform support to include Android devices, complementing existing Windows and Mac capabilities.

- Key changes or new features  
Foundry Local now enables advanced on-device AI processing on Android smartphones, tablets, and IoT devices, enhancing performance and reducing latency by processing data locally. Integration of the Whisper model provides robust, privacy-preserving speech and audio processing directly on-device, minimizing data exposure and improving compliance with privacy requirements.

- Target audience affected  
This update primarily benefits developers building AI-powered mobile and IoT applications on Android, as well as IT professionals managing secure, privacy-conscious deployments in enterprise and edge environments.

- Important notes if any  
The Android support is currently in private preview, so access may require enrollment or invitation. Developers should consider testing the Whisper model integration for speech/audio use cases to leverage improved privacy and on-device processing capabilities. This extension aligns with growing demand for edge AI solutions that maintain data sovereignty and reduce cloud dependency.

**Details**:

The recent Azure update announces the private preview of Foundry Local’s extended support for Android devices, complementing its existing Windows and Mac platforms. Foundry Local is a framework designed to enable advanced on-device AI processing, and this update specifically enhances its applicability to smartphones, tablets, and IoT devices running Android, thereby broadening its reach in mobile and edge computing environments.

**Background and Purpose:**  
Foundry Local was initially developed to facilitate AI workloads directly on end-user devices, reducing latency, improving responsiveness, and enhancing privacy by minimizing data sent to the cloud. The extension to Android addresses the growing demand for sophisticated AI capabilities on mobile and embedded devices, which are predominant in consumer and industrial IoT sectors. This move aligns with the industry trend toward edge AI, where processing occurs locally to optimize performance and data governance.

**Specific Features and Detailed Changes:**  
- **Android Platform Support:** Foundry Local now supports Android OS, enabling developers to deploy AI models natively on Android smartphones, tablets, and IoT devices.  
- **On-Device AI Processing:** The update supports advanced AI workloads such as computer vision, natural language processing, and sensor data analysis directly on the device, leveraging local compute resources.  
- **Whisper Model Integration:** Integration of OpenAI’s Whisper model enhances speech and audio processing capabilities, offering robust, privacy-preserving transcription and audio analysis without requiring cloud connectivity. This is critical for applications needing offline or secure voice processing.  
- **Cross-Platform Consistency:** Developers can build AI applications with consistent APIs and tooling across Windows, Mac, and now Android, simplifying multi-platform deployment and maintenance.

**Technical Mechanisms and Implementation Methods:**  
Foundry Local on Android leverages native Android development frameworks and hardware acceleration features such as Neural Networks API (NNAPI) to optimize AI model execution. The integration with Whisper involves embedding the model within the local runtime environment, enabling real-time speech recognition and audio processing. The architecture supports containerized or modular AI components that can be updated independently, ensuring flexibility and scalability. Developers interact with Foundry Local through SDKs and APIs that abstract hardware specifics, facilitating streamlined AI model deployment and lifecycle management on Android devices.

**Use Cases and Application Scenarios:**  
- **Smartphones and Tablets:** Real-time voice assistants, offline transcription services, and personalized AI features that operate without cloud dependency.  
- **IoT Devices:** Industrial sensors, smart home devices, and edge gateways performing local anomaly detection, predictive maintenance, or voice command processing.  
- **Privacy-Sensitive Applications:** Healthcare, finance, and enterprise apps requiring on-device data processing to comply with data protection regulations and minimize data exposure.  
- **Disconnected Environments:** Scenarios where network connectivity is intermittent or unavailable, such as remote field operations or mobile workforce tools.

**Important Considerations and Limitations:**  
- **Private Preview Status:** As a private preview, access is limited and features may evolve based on feedback. Production readiness and SLA guarantees are not yet established.  
- **Hardware Constraints:** Performance depends on the device’s CPU, GPU, and AI accelerator capabilities; older or lower-end devices may experience limitations.  
- **Model Size and Resource Usage:** On-device models must be optimized for size and efficiency to fit within device memory and power constraints.  
- **Security:** While on-device processing enhances privacy, secure model deployment and updates require robust mechanisms to prevent tampering or unauthorized access.

**Integration with Related Azure Services:**  
Foundry Local complements Azure’s broader AI and edge computing ecosystem, including Azure Percept for edge AI hardware, Azure IoT Hub for device management, and Azure Cognitive Services for cloud-based AI capabilities. Developers can orchestrate hybrid AI workflows where Foundry Local handles latency-sensitive or privacy-critical tasks locally, while leveraging cloud services for heavy compute, model training, or analytics. Integration with Azure DevOps and Azure Machine Learning facilitates CI/CD pipelines and model lifecycle management across cloud and edge environments.

In summary, the private preview of Found

---

### 114. Public Preview: Foundry Local updates

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Foundry Local updates](https://azure.microsoft.com/updates?id=526193)

**Update ID**: 526193
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure Foundry Local has been updated in public preview to enhance on-device AI capabilities, now supporting the Whisper model for speech and audio processing.

- Key changes or new features  
The update integrates the Whisper model, enabling robust, privacy-preserving speech recognition and audio processing directly on smartphones, tablets, and IoT devices. This reduces reliance on cloud connectivity and enhances data privacy by processing audio locally. The Foundry Local platform has also been redesigned to optimize performance and usability for edge deployments.

- Target audience affected  
Developers building AI-powered applications on edge devices, including smartphones, tablets, and IoT hardware, as well as IT professionals managing on-device AI deployments and privacy-sensitive workloads.

- Important notes if any  
This update is currently in public preview, so users should evaluate it in non-production environments. The focus on local processing aligns with increasing data privacy requirements and edge computing trends, making it particularly relevant for scenarios with limited connectivity or strict compliance needs.

**Details**:

The recent public preview update for Foundry Local significantly enhances its edge AI capabilities by integrating the Whisper model and advanced on-device AI processing tailored for smartphones, tablets, and IoT devices. This update aims to empower developers and organizations to perform sophisticated speech and audio processing locally, thereby improving privacy, reducing latency, and enabling offline functionality.

**Background and Purpose of the Update**  
Foundry Local is Azure’s solution for deploying AI models directly on edge devices, enabling real-time, low-latency inference without reliance on cloud connectivity. The purpose of this update is to extend Foundry Local’s support to include the Whisper model—an advanced speech recognition and audio processing neural network developed by OpenAI—and to enhance on-device AI capabilities. This aligns with growing industry demands for privacy-preserving AI, especially in scenarios where transmitting sensitive audio data to the cloud is undesirable or impractical.

**Specific Features and Detailed Changes**  
- **Whisper Model Integration:** Foundry Local now supports the Whisper model, enabling robust speech-to-text transcription, language identification, and audio understanding directly on edge devices. This model is known for its high accuracy across multiple languages and noisy environments.  
- **Advanced On-Device AI:** The update includes optimizations for running complex AI workloads on resource-constrained devices such as smartphones, tablets, and IoT endpoints. This involves model quantization, pruning, and efficient runtime environments to balance performance and power consumption.  
- **Redesigned Foundry Architecture:** The platform has been rearchitected to streamline deployment workflows, improve model management, and enhance compatibility with diverse hardware accelerators (e.g., NPUs, GPUs, DSPs).  
- **Privacy-Preserving Processing:** By enabling local inference, audio data remains on the device, mitigating risks associated with data transmission and storage in the cloud.

**Technical Mechanisms and Implementation Methods**  
The integration of the Whisper model into Foundry Local leverages containerized AI runtime environments optimized for edge hardware. The models are converted into lightweight formats compatible with Azure Percept DK and other supported devices, using techniques such as ONNX conversion and TensorRT optimization. Developers can deploy models via Azure IoT Edge modules or directly through Foundry’s deployment pipelines, which support continuous integration and delivery (CI/CD) for AI models. The runtime supports batching, asynchronous processing, and hardware acceleration to maximize throughput and minimize latency.

**Use Cases and Application Scenarios**  
- **Smartphones and Tablets:** Real-time transcription for voice assistants, accessibility features, and language translation apps without cloud dependency.  
- **IoT Devices:** Industrial monitoring, smart home devices, and security systems that require local audio event detection and command recognition with privacy compliance.  
- **Healthcare:** On-device processing of patient speech data for diagnostics or therapy applications where data privacy is paramount.  
- **Retail and Customer Service:** Edge-based voice analytics for kiosks or point-of-sale systems to improve customer interactions without sending sensitive audio data externally.

**Important Considerations and Limitations**  
- **Hardware Constraints:** Performance depends heavily on the device’s computational resources; older or low-power devices may experience reduced throughput or increased latency.  
- **Model Size and Complexity:** The Whisper model is relatively large; while optimized versions are provided, some trade-offs between accuracy and resource usage may be necessary.  
- **Security:** Although local processing enhances privacy, securing the device and runtime environment remains critical to prevent unauthorized access.  
- **Preview Status:** As a public preview, features may evolve, and support could be limited; production deployments should consider potential changes and monitor updates.

**Integration with Related Azure Services**  
Foundry Local integrates seamlessly with Azure IoT Edge for device management and deployment orchestration, allowing centralized control over distributed AI workloads. It also complements Azure Cognitive Services by enabling hybrid AI architectures where sensitive data is processed locally, and aggregated insights are sent to the cloud for further analysis. Additionally, integration with Azure Machine Learning facilitates model training, versioning, and automated

---

### 115. Public Preview: Foundry IQ by Azure AI Search

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Foundry IQ by Azure AI Search](https://azure.microsoft.com/updates?id=526150)

**Update ID**: 526150
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft announced the public preview of Foundry IQ, a knowledge system powered by Azure AI Search.

- Key changes or new features  
Foundry IQ enables intelligent grounding of agents in enterprise data by connecting to a single unified knowledge base that aggregates multiple data sources. This eliminates the need for developers and IT professionals to manage multiple separate APIs for different data repositories. The system leverages Azure AI Search capabilities to provide smarter, context-aware access to organizational knowledge, improving the efficiency and accuracy of AI agents.

- Target audience affected  
Developers building AI agents and applications that require integration with enterprise data, as well as IT professionals responsible for managing and securing enterprise knowledge systems.

- Important notes if any  
As Foundry IQ is currently in public preview, users should evaluate it in non-production environments and provide feedback. Integration simplifies data access but requires proper configuration of the unified knowledge base to ensure comprehensive and secure data coverage across sources.

**Details**:

The Public Preview of Foundry IQ by Azure AI Search introduces an advanced knowledge system designed to streamline enterprise data access for intelligent agents by consolidating multiple data sources into a single unified knowledge base. This update addresses the complexity and overhead associated with managing multiple APIs and disparate data repositories, enabling developers and IT professionals to build smarter, more efficient AI-powered applications.

**Background and Purpose**  
Enterprises typically maintain vast and diverse data stores across various platforms and formats, making it challenging for AI agents—such as chatbots, virtual assistants, or automated workflows—to retrieve relevant information quickly and accurately. Traditionally, integrating these agents required connecting to multiple APIs or data endpoints, increasing development complexity and maintenance efforts. Foundry IQ aims to simplify this by providing a centralized knowledge system that abstracts and unifies access to heterogeneous enterprise data sources, thereby accelerating AI application development and improving data grounding fidelity.

**Specific Features and Detailed Changes**  
- **Unified Knowledge Base:** Foundry IQ allows agents to connect to a single knowledge base that aggregates multiple underlying data sources, including structured and unstructured data.  
- **Powered by Azure AI Search:** It leverages Azure Cognitive Search capabilities such as semantic search, natural language processing, and AI enrichment to enhance data retrieval relevance and contextual understanding.  
- **Simplified API Surface:** Developers interact with a consolidated API endpoint rather than managing multiple disparate APIs, reducing integration complexity.  
- **Dynamic Data Source Management:** The system supports connecting and indexing various enterprise data repositories dynamically, enabling continuous updates and synchronization.  
- **Enhanced Agent Grounding:** By grounding AI agents in a comprehensive and semantically enriched knowledge base, Foundry IQ improves response accuracy and reduces hallucinations in AI-generated outputs.

**Technical Mechanisms and Implementation Methods**  
Foundry IQ is architected on top of Azure Cognitive Search, utilizing its indexing and AI enrichment pipelines to ingest and process data from multiple sources such as databases, document stores, and SaaS applications. The system applies semantic ranking models and natural language understanding to interpret user queries and retrieve contextually relevant information. Developers configure data connectors and define indexing schemas through the Foundry IQ interface or APIs, enabling flexible ingestion pipelines. The unified knowledge base exposes a RESTful API that AI agents can query using natural language or structured queries, with responses enriched by AI-driven relevance scoring and entity recognition.

**Use Cases and Application Scenarios**  
- **Enterprise Virtual Assistants:** Delivering accurate, context-aware responses by grounding conversations in comprehensive enterprise data.  
- **Customer Support Automation:** Enabling chatbots to access product manuals, FAQs, and support tickets from multiple systems through a single knowledge base.  
- **Knowledge Management:** Facilitating internal knowledge discovery by aggregating documents, wikis, and databases for employee self-service portals.  
- **Compliance and Risk Management:** Quickly retrieving regulatory documents and audit logs from diverse repositories to support compliance workflows.

**Important Considerations and Limitations**  
- As a public preview, Foundry IQ may have limited SLA guarantees and could undergo significant changes before general availability.  
- Data privacy and security configurations must be carefully managed, especially when aggregating sensitive enterprise data. Integration with Azure Active Directory and role-based access control is essential.  
- Performance and latency depend on the volume and complexity of indexed data sources; proper indexing strategies and query optimization are recommended.  
- Currently, support for certain data connectors or formats may be limited; verifying compatibility with enterprise data sources is advised.

**Integration with Related Azure Services**  
- **Azure Cognitive Search:** Core technology providing indexing, AI enrichment, and semantic search capabilities.  
- **Azure AI Language Services:** Can be combined for advanced natural language understanding and question answering.  
- **Azure Active Directory (AAD):** For secure authentication and authorization of users and agents accessing the knowledge base.  
- **Azure Data Factory or Logic Apps:** To orchestrate data ingestion and synchronization workflows into Foundry IQ.  
- **Azure Bot Service:** To build conversational AI agents that leverage Foundry

---

### 116. Generally Available: Foundry Tools (rebrand from Azure AI Services)

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Foundry Tools (rebrand from Azure AI Services)](https://azure.microsoft.com/updates?id=526132)

**Update ID**: 526132
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure AI Services has been rebranded and is now generally available as Foundry Tools, a unified suite of prebuilt, production-ready AI capabilities.

- Key changes or new features  
Foundry Tools offer integrated AI functionalities across multiple data types including audio, video, images, documents, and text. These tools are seamlessly embedded within the Microsoft Foundry platform, enabling streamlined development and deployment of AI-powered applications without extensive custom model training. The suite supports common AI scenarios such as content analysis, transcription, image recognition, and document processing.

- Target audience affected  
Developers building AI-enabled applications and IT professionals managing AI services in enterprise environments will benefit from the simplified integration and production readiness of Foundry Tools. It is especially relevant for teams seeking scalable, out-of-the-box AI solutions within the Microsoft ecosystem.

- Important notes if any  
The rebranding to Foundry Tools reflects Microsoft’s strategy to consolidate AI capabilities under the Foundry platform for better coherence and usability. Existing Azure AI Services users should transition to Foundry Tools to leverage the latest updates and support. Detailed documentation and integration guides are available on the Microsoft Foundry platform.

**Details**:

The recent Azure update announces the general availability of Foundry Tools, a rebranding and evolution of the former Azure AI Services, delivering a unified suite of prebuilt, production-ready AI capabilities across multiple data modalities including audio, video, images, documents, and text. These tools are now seamlessly integrated into the Microsoft Foundry platform, designed to streamline AI development and deployment for technical professionals.

**Background and Purpose:**  
The rebranding to Foundry Tools reflects Microsoft’s strategic effort to consolidate and enhance its AI offerings under a single, cohesive platform—Microsoft Foundry. This aims to reduce fragmentation and complexity by providing developers with a consistent, end-to-end environment for building intelligent applications. The update addresses the growing demand for multimodal AI capabilities that can handle diverse data types in production environments, enabling faster time-to-market and improved operational efficiency.

**Specific Features and Detailed Changes:**  
Foundry Tools encompass a broad range of AI functionalities, including but not limited to:  
- Audio processing capabilities such as speech recognition, speaker identification, and audio classification.  
- Video analytics including object detection, activity recognition, and content moderation.  
- Image analysis features like image classification, OCR (optical character recognition), and facial recognition.  
- Document understanding tools that extract structured data from unstructured documents using advanced NLP and computer vision.  
- Text analytics including sentiment analysis, entity recognition, language detection, and summarization.

Compared to the previous Azure AI Services, Foundry Tools offer enhanced integration within the Microsoft Foundry platform, improved scalability, and streamlined APIs that support rapid prototyping and deployment. The update also introduces improved model management, versioning, and monitoring capabilities to facilitate production readiness.

**Technical Mechanisms and Implementation Methods:**  
Foundry Tools are implemented as modular, containerized microservices within the Foundry platform, leveraging Azure Kubernetes Service (AKS) for orchestration and scalability. They utilize pre-trained deep learning models optimized for cloud execution, with options for fine-tuning using custom datasets. The platform supports RESTful APIs and SDKs in multiple languages (e.g., Python, C#) to enable seamless integration into existing applications and workflows. Authentication and access control are managed via Azure Active Directory (AAD), ensuring enterprise-grade security. Data ingress and egress are optimized for low latency and high throughput, supporting real-time and batch processing scenarios.

**Use Cases and Application Scenarios:**  
Foundry Tools are suited for a wide range of enterprise applications, including:  
- Customer service automation through speech-to-text and sentiment analysis.  
- Media and entertainment for automated video content tagging and moderation.  
- Financial services for document processing and fraud detection.  
- Healthcare for medical image analysis and clinical document extraction.  
- Retail and manufacturing for quality inspection using image recognition and anomaly detection.

By providing multimodal AI capabilities within a unified platform, Foundry Tools enable developers to build sophisticated, intelligent applications that can process complex data streams efficiently.

**Important Considerations and Limitations:**  
While Foundry Tools are production-ready, users should consider data privacy and compliance requirements, especially when processing sensitive audio, video, or document data. Model accuracy may vary depending on domain specificity, necessitating custom training or fine-tuning for optimal results. Latency and throughput depend on deployment configurations and workload characteristics; thus, performance testing is recommended. Additionally, integration with legacy systems may require custom adapters or middleware.

**Integration with Related Azure Services:**  
Foundry Tools complement and integrate with several Azure services to provide a comprehensive AI solution:  
- Azure Cognitive Services for additional AI capabilities not covered within Foundry Tools.  
- Azure Machine Learning for custom model training, deployment, and lifecycle management.  
- Azure Data Lake and Azure Synapse Analytics for large-scale data storage and analytics.  
- Azure DevOps for CI/CD pipelines supporting AI model deployment.  
- Azure Security Center and Azure Policy for governance and compliance.

This integration enables organizations to leverage the full Azure ecosystem to build, deploy, and manage intelligent applications

---

### 117. Generally Available: Content Understanding in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Content Understanding in Microsoft Foundry](https://azure.microsoft.com/updates?id=526123)

**Update ID**: 526123
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft has announced the general availability of Content Understanding within Microsoft Foundry, enhancing integration capabilities and security features.

- Key changes or new features  
Content Understanding now supports direct connections to Foundry models, enabling customers to deploy and utilize Foundry model deployments seamlessly. Additional enhancements include support for Virtual Networks (VNETs) for secure network isolation, Managed Identities for streamlined and secure authentication, and Customer Managed Keys (CMK) to provide greater control over data encryption.

- Target audience affected  
This update primarily benefits developers and IT professionals working with AI-driven content processing and document understanding solutions who require secure, scalable, and compliant deployments within Azure environments.

- Important notes if any  
The introduction of VNET support and Managed Identities aligns with enterprise security best practices, facilitating easier integration into existing secure infrastructures. Customer Managed Keys offer enhanced compliance capabilities by allowing organizations to manage encryption keys themselves. Users should review their network and security configurations to leverage these new features effectively.

For more details, visit: https://azure.microsoft.com/updates?id=526123

**Details**:

The recent general availability of Content Understanding in Microsoft Foundry represents a significant enhancement in Azure’s AI-driven content processing capabilities, enabling enterprises to leverage Foundry’s advanced models for extracting insights from unstructured data with improved security and deployment flexibility.

**Background and Purpose of the Update**  
Content Understanding is a cognitive service designed to analyze and extract meaningful information from diverse content types such as documents, images, and videos. Prior to this update, Content Understanding operated primarily as a standalone service with limited integration options. The update’s purpose is to enable seamless connectivity to Microsoft Foundry models, which are specialized AI models deployed within Foundry environments, thus allowing customers to utilize custom or pre-trained Foundry models for content analysis. This aligns with enterprise demands for more customizable, secure, and scalable AI solutions integrated within their existing cloud infrastructure.

**Specific Features and Detailed Changes**  
- **Integration with Foundry Models:** Customers can now connect Content Understanding directly to Foundry model deployments, allowing the use of domain-specific or customized AI models for content extraction and understanding.  
- **VNET Support:** The service now supports Virtual Network (VNET) integration, enabling secure, private network connectivity between Content Understanding and other Azure resources, reducing exposure to the public internet.  
- **Managed Identities:** Support for Azure Managed Identities simplifies authentication and authorization by enabling Content Understanding to securely access other Azure services without managing credentials explicitly.  
- **Customer Managed Keys (CMK):** Customers can now use their own encryption keys to protect data at rest, enhancing compliance and security by maintaining control over cryptographic keys.

**Technical Mechanisms and Implementation Methods**  
Content Understanding connects to Foundry models via secure API endpoints exposed within the customer’s Azure environment. VNET integration is implemented through private endpoints, ensuring traffic between Content Understanding and Foundry models remains within the Azure backbone network. Managed Identities leverage Azure Active Directory (AAD) to provide token-based authentication, eliminating the need for service principals or manual credential management. Customer Managed Keys are integrated through Azure Key Vault, where customers store and manage their encryption keys, which are then referenced by Content Understanding for encrypting stored data.

**Use Cases and Application Scenarios**  
- **Enterprise Document Processing:** Organizations can deploy custom Foundry models trained on proprietary document formats or industry-specific terminology, improving accuracy in extracting structured data from contracts, invoices, or technical manuals.  
- **Secure Content Analysis:** Financial, healthcare, and government sectors benefit from VNET and CMK support to ensure data privacy and compliance with regulatory requirements such as HIPAA or GDPR.  
- **Automated Knowledge Extraction:** Businesses can automate the extraction of insights from multimedia content (e.g., videos, images) using Foundry models tailored to their domain, enhancing searchability and analytics.  
- **Integrated Cloud Workflows:** By leveraging Managed Identities, Content Understanding can be integrated into broader Azure workflows, such as Azure Logic Apps or Azure Data Factory pipelines, enabling automated content processing with secure service-to-service communication.

**Important Considerations and Limitations**  
- **Model Compatibility:** Only Foundry models deployed and accessible within the customer’s Azure environment can be connected; public or external models are not supported.  
- **Network Configuration:** Proper VNET and private endpoint configuration is required to ensure connectivity; misconfiguration can lead to service inaccessibility.  
- **Key Management:** Using Customer Managed Keys requires careful key lifecycle management and understanding of Azure Key Vault policies to avoid data access disruptions.  
- **Latency and Throughput:** Depending on the complexity of Foundry models and network setup, latency may vary; performance testing is recommended for high-throughput scenarios.

**Integration with Related Azure Services**  
Content Understanding’s enhanced capabilities integrate tightly with Azure Key Vault for key management, Azure Active Directory for identity and access management, and Azure Virtual Network for secure networking. It can be orchestrated alongside Azure Data Factory for ETL workflows, Azure Logic Apps for event-driven automation, and Azure Synapse Analytics for

---

### 118. Public Preview: Enrich agents with a unified catalog of prebuilt and custom tools in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Enrich agents with a unified catalog of prebuilt and custom tools in Microsoft Foundry](https://azure.microsoft.com/updates?id=526114)

**Update ID**: 526114
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry introduced a public preview of a unified catalog for Model Context Protocol (MCP) tools, enabling enrichment of agents with enhanced capabilities.

- Key changes or new features  
The update allows developers to integrate prebuilt and custom MCP tools into agents, providing real-time business context, multimodal inputs (e.g., text, images), and custom business logic. This unified catalog streamlines access and management of these tools, improving agent intelligence and adaptability within business workflows.

- Target audience affected  
Developers building intelligent agents and IT professionals managing AI-driven business applications will benefit from the enhanced extensibility and contextual capabilities enabled by this update.

- Important notes if any  
As this is a public preview, features may evolve, and users should test thoroughly before production deployment. Integration requires familiarity with MCP and Microsoft Foundry’s agent development environment.

For detailed information and access, visit: https://azure.microsoft.com/updates?id=526114

**Details**:

The recent public preview update for Microsoft Foundry introduces a unified catalog of prebuilt and custom Model Context Protocol (MCP) tools designed to enrich AI agents with real-time business context, multimodal capabilities, and customizable business logic. This enhancement aims to streamline the development and deployment of intelligent agents by providing a centralized repository of reusable tools that can be leveraged to extend agent functionality dynamically.

**Background and Purpose**  
As AI agents become increasingly integral to enterprise workflows, there is a growing need to embed them with contextual awareness and domain-specific logic to improve relevance and responsiveness. Prior to this update, developers often had to build and integrate disparate tools and services manually, leading to fragmented implementations and increased maintenance overhead. Microsoft Foundry’s unified catalog addresses this by offering a standardized framework for managing and deploying MCP tools, facilitating rapid enrichment of agents with consistent and scalable capabilities.

**Specific Features and Detailed Changes**  
- **Unified Catalog of MCP Tools:** A centralized repository that includes both Microsoft-provided prebuilt tools and user-defined custom tools, accessible through a common interface.  
- **Real-Time Business Context Integration:** Tools can ingest and process live business data streams, enabling agents to respond with up-to-date information and insights.  
- **Multimodal Capabilities:** Support for multiple input and output modalities (e.g., text, voice, images), allowing agents to interact more naturally and flexibly.  
- **Custom Business Logic Embedding:** Developers can create and register custom MCP tools that encapsulate specific business rules or workflows, which agents can invoke dynamically.  
- **Seamless Tool Discovery and Invocation:** Agents can query the catalog to discover relevant tools based on context and invoke them as needed during interactions.

**Technical Mechanisms and Implementation Methods**  
The update leverages the Model Context Protocol (MCP), a standardized interface specification that defines how tools expose their capabilities and how agents interact with them. MCP tools register metadata describing their inputs, outputs, and operational parameters within the catalog. At runtime, agents use this metadata to discover appropriate tools and invoke them via defined APIs or event-driven triggers. The catalog itself is implemented as a scalable, secure service within Microsoft Foundry, supporting versioning, access control, and telemetry for tool usage. Developers can package custom tools as microservices or serverless functions that conform to MCP specifications and register them through the Foundry management portal or CLI.

**Use Cases and Application Scenarios**  
- **Customer Support Automation:** Agents can leverage real-time CRM data and custom escalation workflows to provide personalized support.  
- **Sales and Marketing:** Integration with live sales dashboards and campaign management tools enables agents to deliver timely recommendations and insights.  
- **Operational Monitoring:** Agents can process multimodal sensor data and trigger automated remediation actions based on custom business logic.  
- **Compliance and Risk Management:** Custom tools can enforce policy checks and audit trails dynamically during agent interactions.

**Important Considerations and Limitations**  
- As this feature is in public preview, it may not yet be fully production-ready and could undergo significant changes.  
- Custom MCP tools must strictly adhere to protocol specifications to ensure compatibility and security.  
- Real-time data integration requires appropriate data connectors and permissions, which must be configured carefully to maintain compliance.  
- Performance and scalability depend on the underlying infrastructure and the complexity of custom tools invoked.

**Integration with Related Azure Services**  
Microsoft Foundry’s unified MCP catalog integrates seamlessly with Azure AI services such as Azure OpenAI for natural language processing, Azure Cognitive Services for multimodal inputs, and Azure Functions or Azure Kubernetes Service (AKS) for hosting custom tools. It also interoperates with Azure Event Grid and Azure Logic Apps for event-driven workflows and orchestration. Data integration can leverage Azure Data Factory or Azure Synapse Analytics to feed real-time business context into MCP tools.

In summary, this public preview update to Microsoft Foundry’s unified MCP catalog empowers developers to efficiently enhance AI agents with rich, context-aware, and multimodal capabilities through a standardized

---

### 119. Public Preview: Built-in memory in Foundry Agent Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Built-in memory in Foundry Agent Service](https://azure.microsoft.com/updates?id=526004)

**Update ID**: 526004
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure Foundry Agent Service now includes built-in long-term memory in public preview.

- Key changes or new features  
The integrated memory enables agents to persist information across sessions and workflows, allowing them to remember past interactions, adapt dynamically, and maintain coherent behavior over time. This memory is embedded directly within the Foundry runtime, providing a scalable and robust foundation for stateful agent development without requiring external storage solutions.

- Target audience affected  
Developers building intelligent agents and conversational AI solutions using Azure Foundry Agent Service, as well as IT professionals managing agent deployments and workflows.

- Important notes if any  
As this feature is in public preview, developers should evaluate it in non-production environments and provide feedback. Integration with existing Foundry workflows is seamless, but users should monitor performance and storage implications of long-term memory usage. Documentation and best practices are available to guide implementation.

**Details**:

The Public Preview of built-in memory in the Foundry Agent Service introduces a native, long-term memory capability integrated directly into the Foundry runtime environment, designed to enable developers to build intelligent agents that maintain context and state persistently across multiple sessions and complex workflows. This update addresses the critical need for agents to remember prior interactions, user preferences, and environmental data, thereby enhancing coherence, adaptability, and personalized responses in conversational AI and automation scenarios.

**Background and Purpose:**  
Prior to this update, agents developed using the Foundry Agent Service had limited or no native support for persistent memory, often requiring external storage solutions or custom implementations to maintain state across sessions. This fragmented approach increased development complexity and reduced the agents’ ability to deliver seamless, context-aware interactions. The built-in memory feature aims to simplify state management by embedding a scalable, durable memory layer within the Foundry runtime, thus improving developer productivity and agent intelligence.

**Specific Features and Detailed Changes:**  
- **Long-term Memory Integration:** The memory is persistent and directly accessible by agents, enabling storage and retrieval of information such as user preferences, session history, and workflow states.  
- **Scalability:** Designed to handle large volumes of memory data efficiently, supporting complex multi-turn conversations and workflows without degradation in performance.  
- **Contextual Adaptation:** Agents can dynamically update and reference memory contents to adapt responses based on historical data, improving relevance and user experience.  
- **Seamless Runtime Integration:** Memory operations are embedded within the Foundry runtime lifecycle, allowing developers to interact with memory through standard APIs without managing external databases or caches.

**Technical Mechanisms and Implementation Methods:**  
The built-in memory leverages a persistent storage backend optimized for low-latency read/write operations, integrated tightly with the Foundry Agent Service’s execution engine. Developers interact with memory via declarative constructs or API calls within agent code, enabling CRUD (Create, Read, Update, Delete) operations on memory entries. The memory system supports structured data formats, allowing complex objects and metadata to be stored and queried efficiently. Additionally, memory is versioned and scoped per agent instance or user context, ensuring isolation and consistency.

**Use Cases and Application Scenarios:**  
- **Conversational AI:** Agents can remember user preferences, past queries, and contextual information to provide personalized and coherent multi-turn dialogues.  
- **Workflow Automation:** Memory enables agents to track progress and state across multi-step processes, facilitating error recovery and dynamic decision-making.  
- **Customer Support:** Persistent memory allows agents to recall prior interactions and customer details, reducing friction and improving service quality.  
- **IoT and Monitoring:** Agents can maintain historical sensor data or device states to detect anomalies or trigger context-aware actions.

**Important Considerations and Limitations:**  
- As this feature is in Public Preview, it may have limitations in terms of SLA guarantees, regional availability, and feature completeness.  
- Data privacy and compliance must be carefully managed, especially when storing sensitive user information; developers should implement appropriate encryption and access controls.  
- Memory size and retention policies should be planned to avoid excessive storage costs and ensure performance.  
- Integration with external data sources is still possible but may require synchronization logic to maintain consistency with the built-in memory.

**Integration with Related Azure Services:**  
The built-in memory in Foundry Agent Service complements other Azure cognitive and data services. For example, it can be combined with Azure Cognitive Services for natural language understanding, Azure Cosmos DB for extended storage needs, and Azure Monitor for telemetry and diagnostics. Additionally, integration with Azure Active Directory ensures secure access control, while Azure Functions can be used to extend agent capabilities triggered by memory state changes.

In summary, the introduction of built-in memory in the Foundry Agent Service significantly enhances the ability to build intelligent, stateful agents by providing a native, scalable, and persistent memory layer integrated within the runtime, streamlining development and enabling richer, context-aware applications across diverse scenarios.

---

### 120. Public Preview: Multi-agent workflows in Foundry Agent Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Multi-agent workflows in Foundry Agent Service](https://azure.microsoft.com/updates?id=525999)

**Update ID**: 525999
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure Foundry Agent Service now supports multi-agent workflows in public preview.

- Key changes or new features  
Developers can create complex workflows involving multiple agents using a visual designer or a code-first API. These workflows enable structured orchestration with features such as context sharing between agents, persistent state management, and built-in error recovery mechanisms. This facilitates building resilient, scalable enterprise processes that require coordination across multiple autonomous agents.

- Target audience affected  
Developers building intelligent agent-based applications and IT professionals managing enterprise automation workflows will benefit from these enhancements.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. The modular design allows flexible workflow composition, but developers should consider error handling and state persistence strategies to ensure robustness in complex scenarios.

For more details, visit: https://azure.microsoft.com/updates?id=525999

**Details**:

The recent Azure update introduces the Public Preview of multi-agent workflows in the Foundry Agent Service, enabling developers to design and implement complex, coordinated workflows involving multiple autonomous agents. This enhancement addresses the growing need for orchestrating sophisticated enterprise processes that require concurrent task execution, state persistence, and robust error handling.

**Background and Purpose**  
As enterprise applications increasingly rely on intelligent agents to automate and manage diverse tasks, there is a demand for orchestrating multiple agents working collaboratively within a single workflow. Previously, Foundry Agent Service supported single-agent workflows, limiting the ability to model complex interactions and dependencies. This update aims to empower developers to build multi-agent workflows that facilitate structured orchestration, context sharing, and resilience, thereby improving process automation at scale.

**Specific Features and Detailed Changes**  
- **Multi-agent orchestration:** Developers can now define workflows that coordinate multiple agents, each responsible for distinct tasks or roles within the process.  
- **Visual designer and code-first API:** The update provides both a drag-and-drop visual designer for workflow modeling and a comprehensive code-first API, catering to different developer preferences and enabling fine-grained control.  
- **Context sharing:** Agents within a workflow can share contextual information, enabling dynamic decision-making and data exchange during execution.  
- **Persistent state management:** Workflow states are persisted, allowing workflows to resume from the last known state after interruptions or failures.  
- **Error recovery:** Built-in mechanisms support error detection and recovery, ensuring workflow robustness and minimizing manual intervention.  
- **Modular design:** Workflows can be composed modularly, facilitating reuse and maintainability of workflow components.

**Technical Mechanisms and Implementation Methods**  
The multi-agent workflows leverage Foundry Agent Service’s underlying orchestration engine, which manages agent lifecycle, state persistence, and communication. The visual designer abstracts workflow logic into graphical components representing agents and their interactions, which are translated into executable workflow definitions. The code-first API exposes classes and methods to programmatically define agents, messages, state transitions, and error handlers. Context sharing is implemented via a shared state store accessible to all agents within the workflow scope. Persistent state is maintained using Azure Cosmos DB or other supported durable storage backends, ensuring durability and consistency. Error recovery employs retry policies, compensation actions, and escalation paths defined within the workflow.

**Use Cases and Application Scenarios**  
- **Enterprise process automation:** Coordinating multiple agents to handle complex approval workflows, document processing, or supply chain management.  
- **Customer service orchestration:** Managing multi-agent chatbots or virtual assistants that collaborate to resolve customer queries involving different domains.  
- **IoT device management:** Orchestrating agents that monitor, analyze, and respond to events from distributed IoT devices.  
- **Financial services:** Automating multi-step transaction processing with compliance checks and fraud detection agents working in concert.  
- **DevOps automation:** Coordinating agents that manage CI/CD pipelines, infrastructure provisioning, and incident response.

**Important Considerations and Limitations**  
- As this feature is in Public Preview, it may not be suitable for production workloads without thorough testing.  
- There may be limitations on scale, performance, or supported agent types during the preview phase.  
- Developers should design workflows with idempotency and state consistency in mind to handle retries and failures gracefully.  
- Integration with existing monitoring and logging tools requires configuration to capture multi-agent interactions effectively.  
- Security considerations include managing access controls for shared context and ensuring secure communication between agents.

**Integration with Related Azure Services**  
- **Azure Cosmos DB:** Used for durable state persistence and context storage within workflows.  
- **Azure Monitor and Log Analytics:** For monitoring workflow execution, diagnostics, and alerting on errors or performance issues.  
- **Azure Functions:** Agents can invoke serverless functions to perform discrete tasks or integrate with external systems.  
- **Azure Event Grid and Service Bus:** Facilitate event-driven communication and messaging between agents and external services.  
- **Azure

---

### 121. Public Preview: Hosted agents in Foundry Agent Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Hosted agents in Foundry Agent Service](https://azure.microsoft.com/updates?id=525994)

**Update ID**: 525994
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure announced the public preview of hosted agents in the Foundry Agent Service, enabling streamlined deployment and scaling of custom AI agents.

- Key changes or new features  
Developers can now deploy custom-code agents built using Microsoft Agent Framework, LangGraph, CrewAI, or other open-source frameworks directly on hosted infrastructure. This eliminates the need for local environment management and simplifies moving from experimentation to production. The hosted agents provide scalable, managed compute resources tailored for AI agent workloads.

- Target audience affected  
This update primarily targets developers building AI agents and IT professionals managing deployment environments who seek to accelerate production rollout and reduce operational overhead.

- Important notes if any  
As this is a public preview, users should expect ongoing feature enhancements and possible limitations. Integration with multiple agent frameworks offers flexibility but may require familiarity with respective SDKs. Users should monitor the official documentation and updates for best practices and support details.

Link: https://azure.microsoft.com/updates?id=525994

**Details**:

The recent Azure update announces the public preview of Hosted Agents in the Foundry Agent Service, designed to streamline the transition from local development to scalable production deployment of intelligent agents. This enhancement addresses the complexity and operational overhead traditionally involved in deploying custom AI agents by providing a managed, cloud-hosted environment.

**Background and Purpose**  
Developers and data scientists often prototype intelligent agents locally using frameworks such as Microsoft Agent Framework, LangGraph, or CrewAI, as well as other open-source tools. However, scaling these agents for production typically requires significant infrastructure setup, orchestration, and maintenance efforts. The Foundry Agent Service’s hosted agents aim to eliminate these barriers by offering a fully managed platform that supports seamless deployment and scaling of custom-coded agents, thereby accelerating time to production and reducing operational complexity.

**Specific Features and Detailed Changes**  
- **Hosted Agent Environment:** The service now provides a cloud-hosted runtime environment for agents, removing the need for users to manage their own compute resources or container orchestration systems.  
- **Framework Agnostic Support:** Developers can deploy agents built with Microsoft Agent Framework, LangGraph, CrewAI, or other open-source frameworks, enabling flexibility in development choices.  
- **Seamless Transition from Local to Cloud:** The update supports a smooth migration path from local experimentation to production-grade hosted agents without significant code changes.  
- **Scalability and Reliability:** Hosted agents benefit from Azure’s underlying infrastructure, offering scalability, high availability, and integrated monitoring.  
- **Integrated Deployment Pipelines:** The service supports integration with CI/CD workflows, enabling automated deployment and updates of agents.

**Technical Mechanisms and Implementation Methods**  
Hosted agents run within a managed containerized environment orchestrated by Azure Foundry Agent Service. Developers package their custom agent code, including dependencies, and deploy it via the Foundry portal or CLI tools. The service abstracts away container management, networking, and scaling concerns. It leverages Azure Kubernetes Service (AKS) or similar container orchestration under the hood, combined with Azure Monitor and Application Insights for telemetry. Authentication and secure communication are handled through Azure Active Directory integration and managed identities, ensuring secure agent operation.

**Use Cases and Application Scenarios**  
- **Customer Service Automation:** Deploy conversational AI agents that handle customer queries at scale without infrastructure management.  
- **Intelligent Workflow Orchestration:** Automate complex workflows by deploying agents that integrate with enterprise systems and respond to real-time events.  
- **Data Processing Pipelines:** Run agents that perform data ingestion, transformation, or analysis tasks in a scalable manner.  
- **Research and Development:** Quickly prototype and iterate on AI agents locally, then deploy them to production seamlessly.  
- **Multi-agent Systems:** Coordinate multiple hosted agents to work collaboratively in distributed AI applications.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, hosted agents may have limited SLA guarantees and could undergo changes before general availability.  
- **Resource Constraints:** There may be quotas or limits on compute, memory, or concurrent agent instances during preview.  
- **Framework Compatibility:** While multiple frameworks are supported, some custom or highly specialized agent implementations may require adaptation.  
- **Security and Compliance:** Users must ensure their agent code complies with organizational security policies and data governance standards.  
- **Monitoring and Debugging:** While integrated monitoring is provided, advanced debugging might require additional tooling or local testing.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** Underpins container orchestration for hosted agents.  
- **Azure Active Directory (AAD):** Provides authentication and secure identity management for agents.  
- **Azure Monitor and Application Insights:** Enable telemetry, logging, and performance monitoring of hosted agents.  
- **Azure DevOps / GitHub Actions:** Facilitate CI/CD pipelines for automated agent deployment and updates.  
- **Azure Cognitive Services:** Hosted agents can integrate with cognitive APIs for enhanced AI capabilities such as language understanding

---

### 122. Generally Available: Observability in Foundry Control Plane

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Observability in Foundry Control Plane](https://azure.microsoft.com/updates?id=525985)

**Update ID**: 525985
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure announced the general availability (GA) of Observability in the Foundry Control Plane, transitioning from its prior public preview phase. This update introduces enhanced capabilities for monitoring and evaluating machine learning models within the Foundry environment.

- Key changes or new features  
The GA release offers a comprehensive suite of observability tools that allow developers and IT professionals to evaluate model quality, monitor performance metrics, and ensure operational safety. It includes improved agent integrations for real-time data collection and analysis, enabling proactive optimization and troubleshooting of ML workflows. The update also pre-announces upcoming GA support specifically for model evaluations, signaling expanded functionality soon.

- Target audience affected  
This update primarily targets data scientists, ML engineers, and IT professionals involved in deploying and maintaining machine learning models on Azure Foundry. Developers responsible for model lifecycle management will benefit from enhanced monitoring and diagnostic capabilities.

- Important notes if any  
Users should note that while observability features are now generally available, some advanced model evaluation functionalities remain in preview or are slated for GA soon. It is recommended to review integration requirements for agents and update existing workflows to leverage the new observability tools fully. For detailed guidance, refer to the official Azure update link.

**Details**:

The recent Azure update announces the general availability (GA) of Observability in the Foundry Control Plane, transitioning from its prior public preview phase for agents and including a GA pre-announcement for model evaluations. This enhancement introduces a robust and integrated observability framework designed to empower developers and IT professionals to comprehensively evaluate, monitor, and optimize machine learning models’ quality, performance, and safety within the Foundry environment.

**Background and Purpose:**  
As organizations increasingly deploy machine learning (ML) models at scale, ensuring their reliability, accuracy, and compliance becomes critical. The Foundry Control Plane serves as a centralized management layer for ML lifecycle operations, and the introduction of observability capabilities addresses the need for end-to-end visibility into model behavior and system health. This update aims to reduce operational risks, accelerate troubleshooting, and improve model governance by embedding observability directly into the control plane.

**Specific Features and Detailed Changes:**  
- **Comprehensive Telemetry Collection:** The update enables automatic collection of detailed telemetry data from deployed agents, including metrics, logs, and traces related to model inference and system performance.  
- **Model Evaluation Integration:** It introduces native support for continuous model evaluation, allowing users to track model accuracy, drift, and fairness metrics in real-time. This feature is now approaching GA status, signaling production readiness.  
- **Unified Dashboard and Alerts:** Users gain access to a centralized observability dashboard within the Foundry Control Plane, providing visualizations of key performance indicators (KPIs), anomaly detection, and customizable alerting mechanisms.  
- **Safety and Compliance Monitoring:** The framework supports monitoring for safety-related metrics, such as bias detection and compliance checks, helping organizations adhere to regulatory requirements.  
- **Agent-based Architecture:** Observability is implemented via lightweight agents deployed alongside models, enabling granular data capture without significant overhead.

**Technical Mechanisms and Implementation Methods:**  
The observability framework leverages distributed tracing and metrics aggregation protocols compatible with OpenTelemetry standards, ensuring interoperability and extensibility. Agents collect telemetry data locally and securely transmit it to the Foundry Control Plane’s backend services, where data is aggregated, stored, and analyzed. The control plane integrates with Azure Monitor and Log Analytics for scalable data ingestion and long-term retention. Model evaluation pipelines are orchestrated using Azure Machine Learning services, enabling automated and continuous assessment workflows.

**Use Cases and Application Scenarios:**  
- **Real-time Model Performance Monitoring:** Detect and diagnose model degradation or drift in production environments to trigger retraining or rollback.  
- **Operational Troubleshooting:** Quickly identify infrastructure bottlenecks or failures impacting model inference latency or throughput.  
- **Compliance Reporting:** Generate audit trails and safety reports demonstrating adherence to organizational or regulatory standards.  
- **Optimization of Resource Utilization:** Analyze telemetry to fine-tune compute resources and reduce costs without sacrificing performance.  
- **Multi-model Management:** Oversee multiple models deployed across different environments with consolidated observability data.

**Important Considerations and Limitations:**  
- **Agent Deployment Overhead:** While agents are lightweight, deploying them at scale requires planning to minimize resource consumption and network impact.  
- **Data Privacy and Security:** Telemetry data may contain sensitive information; ensure compliance with data governance policies and apply encryption in transit and at rest.  
- **Integration Complexity:** Organizations with existing observability tools may need to adapt workflows to incorporate Foundry’s observability or manage hybrid monitoring setups.  
- **Feature Maturity:** Although GA for agents is announced, some model evaluation features remain in pre-GA stages, potentially limiting certain advanced capabilities until full release.

**Integration with Related Azure Services:**  
The Observability in Foundry Control Plane tightly integrates with Azure Monitor for metrics and alerting, Azure Log Analytics for log management, and Azure Machine Learning for model lifecycle management. It also supports exporting telemetry data to Azure Event Hubs or Azure Data Explorer for custom analytics. This integration facilitates seamless end-to-end monitoring and operational intelligence within the Azure ecosystem, enabling IT professionals to leverage

---

### 123. Public Preview: Enterprise MCP enhancements in Foundry Agent Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Enterprise MCP enhancements in Foundry Agent Service](https://azure.microsoft.com/updates?id=525976)

**Update ID**: 525976
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry Agent Service has been enhanced with improved integration to Enterprise Managed Control Plane (MCP) in public preview.

- Key changes or new features  
The update enables secure, authenticated connections from Foundry Agent to MCP servers, allowing credentials to be passed securely. This enhancement improves flexibility in managing MCP connections while strengthening security and compliance controls around credential handling.

- Target audience affected  
Developers and IT professionals managing Azure Foundry deployments and Enterprise MCP environments who require secure, compliant connectivity between Foundry agents and MCP servers.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments first. The update focuses on improving security posture and compliance when integrating Foundry Agent with Enterprise MCP, which is critical for regulated or enterprise-grade workloads.

For more details, visit: https://azure.microsoft.com/updates?id=525976

**Details**:

The recent public preview update for Microsoft Foundry introduces significant enhancements to its integration with Enterprise Managed Control Plane (MCP) through the Foundry Agent Service, focusing on secure and authenticated connections to MCP servers. This update addresses critical enterprise requirements for security, flexibility, and compliance in managing cloud resources.

**Background and Purpose of the Update**  
Microsoft Foundry is a cloud-native platform designed to streamline and automate infrastructure and application lifecycle management. The Enterprise MCP acts as a centralized control plane that governs resource provisioning, policy enforcement, and operational consistency across large-scale enterprise environments. Prior to this update, Foundry’s integration with Enterprise MCP had limitations in securely passing credentials and establishing authenticated sessions, which posed challenges for enterprises with stringent security and compliance mandates. The purpose of this update is to enhance the Foundry Agent Service to support secure, authenticated connections that safeguard credential transmission and improve overall integration robustness.

**Specific Features and Detailed Changes**  
- **Secure Credential Transmission:** The update enables the Foundry Agent Service to pass credentials to MCP servers securely, leveraging encrypted channels and token-based authentication mechanisms.  
- **Authenticated Connections:** It introduces support for mutual authentication between Foundry agents and MCP servers, ensuring that both endpoints verify each other’s identity before exchanging sensitive information.  
- **Enhanced Flexibility:** Enterprises can now configure multiple authentication methods and credential types, allowing integration with diverse identity providers and compliance with organizational security policies.  
- **Improved Compliance:** By securing credential handling and connection authentication, the update helps enterprises meet regulatory requirements related to data protection and access control.

**Technical Mechanisms and Implementation Methods**  
The implementation relies on industry-standard security protocols such as TLS 1.2/1.3 for encrypted communication and OAuth 2.0/OpenID Connect for token-based authentication. The Foundry Agent Service acts as an intermediary that securely stores and manages credentials, retrieving tokens from configured identity providers and presenting them to MCP servers during connection establishment. Mutual TLS (mTLS) may be employed to enforce endpoint authentication, preventing man-in-the-middle attacks. Configuration is managed through Foundry’s policy and configuration files, allowing administrators to specify authentication parameters, credential sources, and connection policies.

**Use Cases and Application Scenarios**  
- **Enterprise Resource Management:** Organizations managing large fleets of cloud resources can use this enhanced integration to automate provisioning and policy enforcement securely via MCP.  
- **Compliance-Driven Environments:** Regulated industries such as finance and healthcare benefit from the secure credential handling to comply with standards like GDPR, HIPAA, and SOC 2.  
- **Hybrid and Multi-Cloud Deployments:** Enterprises operating across multiple cloud environments can leverage this update to maintain consistent, secure control planes via Foundry and MCP.  
- **DevOps Automation:** Development teams can integrate secure MCP connections into CI/CD pipelines, ensuring that automated deployments adhere to enterprise security policies.

**Important Considerations and Limitations**  
- As this feature is currently in public preview, it may not yet be fully supported for production workloads and could undergo changes based on user feedback.  
- Proper configuration of identity providers and credential management is critical; misconfigurations could lead to authentication failures or security risks.  
- Enterprises must ensure that their network environments permit the necessary secure communication channels and that certificate management for mTLS is properly handled.  
- Integration complexity may increase depending on the diversity of identity systems and credential types used within the organization.

**Integration with Related Azure Services**  
This update complements Azure Active Directory (Azure AD) by enabling Foundry Agent Service to leverage Azure AD tokens for authentication to MCP servers. It also aligns with Azure Key Vault for secure credential storage and management. Additionally, it integrates well with Azure Policy and Azure Monitor, allowing enterprises to enforce compliance and monitor the health and security of MCP connections established via Foundry. These integrations collectively enhance the security posture and operational visibility of enterprise cloud environments managed through Foundry and MCP.

In summary, the Enterprise MCP enhancements in the Foundry Agent Service public preview provide

---

### 124. Public Preview: Microsoft Foundry one-click deploy channels in Teams, M365 and non-Microsoft

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Microsoft Foundry one-click deploy channels in Teams, M365 and non-Microsoft](https://azure.microsoft.com/updates?id=525971)

**Update ID**: 525971
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry introduced a public preview feature enabling one-click, no-code deployment of custom agents across Microsoft Teams, Microsoft 365 Copilot, and non-Microsoft channels.

- Key changes or new features  
The update removes the need for pro-code deployment processes, simplifying the publishing of custom AI agents. Developers and IT professionals can now instantly deploy these agents to reach millions of users within Teams and Microsoft 365 environments, as well as extend reach to external platforms. This streamlines integration and accelerates time-to-value for organizational AI solutions.

- Target audience affected  
Developers building custom AI agents, IT professionals managing deployment pipelines, and organizations leveraging Microsoft Teams and Microsoft 365 Copilot for productivity enhancements.

- Important notes if any  
This capability is currently in public preview, so users should expect potential updates and provide feedback. The no-code deployment focuses on ease of use but may require appropriate permissions and governance controls to manage agent publishing securely. Integration with non-Microsoft channels expands flexibility but may involve additional configuration.  

Source: https://azure.microsoft.com/updates?id=525971

**Details**:

The recent public preview update for Microsoft Foundry introduces a one-click, no-code deployment capability for custom agents directly to Microsoft Teams, Microsoft 365 Copilot, and non-Microsoft channels, significantly simplifying the distribution and scaling of AI-driven solutions across enterprise environments.

**Background and Purpose**  
Microsoft Foundry is a platform designed to accelerate the development and deployment of AI-powered agents and conversational experiences. Traditionally, deploying custom agents to collaboration platforms like Teams or integrating them with Microsoft 365 services required complex pro-code workflows, including manual packaging, configuration, and compliance checks. This update addresses these challenges by enabling a streamlined, no-code publishing process that reduces deployment time and technical barriers, thereby empowering IT teams and citizen developers to rapidly operationalize AI agents at scale.

**Specific Features and Detailed Changes**  
- **One-Click Deployment:** Users can now publish custom-built agents to Microsoft Teams and Microsoft 365 Copilot with a single click, bypassing the need for custom scripting or manual deployment pipelines.  
- **No-Code Interface:** The deployment process is integrated into the Foundry UI, allowing users without deep coding expertise to configure and launch agents.  
- **Multi-Channel Support:** Beyond Microsoft Teams and M365 Copilot, the update extends deployment capabilities to non-Microsoft channels, facilitating broader reach and integration flexibility.  
- **Instant Reach:** By leveraging the native Microsoft 365 ecosystem, agents can be instantly made available to millions of users within an organization, enhancing adoption and utility.

**Technical Mechanisms and Implementation Methods**  
The deployment leverages Foundry’s backend orchestration services, which package the custom agent logic, metadata, and configuration into standardized deployment artifacts compatible with Microsoft Teams app frameworks and Microsoft 365 Copilot integration points. The no-code interface abstracts the underlying Azure Functions, Azure Bot Service, and Microsoft Graph API calls required for registration, permission assignment, and provisioning. For non-Microsoft channels, Foundry utilizes connector adapters and webhook configurations to enable seamless agent activation without manual endpoint management. Authentication and authorization are managed via Azure Active Directory (AAD), ensuring secure and compliant access control.

**Use Cases and Application Scenarios**  
- **Enterprise Collaboration:** Rapidly deploy helpdesk bots, HR assistants, or workflow automation agents directly into Teams channels to improve employee productivity.  
- **Knowledge Management:** Integrate custom Q&A agents into Microsoft 365 Copilot to enhance document search and contextual assistance within Office apps.  
- **Cross-Platform Customer Support:** Publish agents to external platforms such as web chat or third-party messaging apps without additional coding, enabling consistent support experiences.  
- **Citizen Developer Enablement:** Empower business units to create and deploy AI agents independently, accelerating digital transformation initiatives.

**Important Considerations and Limitations**  
- As this feature is in public preview, some functionality may be subject to change and not recommended for production-critical workloads without thorough testing.  
- Deployment currently supports a defined set of Microsoft 365 tenant configurations; organizations with custom compliance or network policies may require additional validation.  
- Non-Microsoft channel support may have limitations on message formats or interaction models depending on the target platform capabilities.  
- Proper governance and lifecycle management of deployed agents remain the responsibility of IT administrators to ensure security and compliance.

**Integration with Related Azure Services**  
This update tightly integrates with several Azure components:  
- **Azure Bot Service:** Hosts and manages the conversational agents’ runtime environment.  
- **Azure Functions:** Executes serverless backend logic triggered by user interactions.  
- **Azure Active Directory:** Provides identity and access management for secure deployment and usage.  
- **Microsoft Graph API:** Facilitates provisioning and configuration within Microsoft 365 ecosystems.  
- **Azure DevOps or GitHub Actions (optional):** Can be used for CI/CD pipelines if extending beyond no-code deployment scenarios.

In summary, the Microsoft Foundry one-click deploy feature in public preview significantly lowers the technical barriers for publishing AI agents across Microsoft Teams, Microsoft 365 Copilot, and

---

### 125. Public Preview: LLM Speech in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: LLM Speech in Microsoft Foundry](https://azure.microsoft.com/updates?id=525962)

**Update ID**: 525962
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft has announced the public preview of LLM Speech in Microsoft Foundry, integrating advanced large language model (LLM) capabilities into speech services.

- Key changes or new features  
The update delivers highly fluent and contextually aware transcription and translation services. It enhances multilingual support, enabling more accurate recognition and translation across diverse languages. Additionally, advanced prompt tuning allows developers to customize and optimize speech interactions for specific scenarios, improving relevance and user experience.

- Target audience affected  
This update primarily benefits developers building speech-enabled applications and IT professionals managing multilingual communication solutions. It is especially valuable for teams requiring precise transcription and translation with contextual understanding in real time.

- Important notes if any  
As this feature is in public preview, users should evaluate it in non-production environments and provide feedback to Microsoft. Integration requires familiarity with Microsoft Foundry APIs and may involve adapting existing speech workflows to leverage LLM enhancements. Monitoring performance and cost implications is advised during early adoption.

For more details, visit: https://azure.microsoft.com/updates?id=525962

**Details**:

The recent public preview of LLM Speech in Microsoft Foundry introduces advanced large language model (LLM) capabilities to Azure’s speech services, significantly enhancing transcription and translation functionalities with improved fluency, contextual understanding, and multilingual support. This update aims to leverage state-of-the-art LLMs to address limitations in traditional speech-to-text and translation systems by providing more accurate, context-aware, and natural language outputs, thereby improving user experience and enabling new AI-driven speech applications.

**Background and Purpose**  
Traditional speech recognition and translation systems often rely on acoustic and language models that may struggle with context, idiomatic expressions, and multilingual nuances. Microsoft Foundry’s integration of LLMs into speech services is designed to overcome these challenges by applying large-scale pretrained language models that understand context deeply and generate more coherent and accurate transcriptions and translations. This update aligns with the broader industry trend of embedding LLMs into multimodal AI services to enhance natural language understanding and generation.

**Specific Features and Detailed Changes**  
- **Enhanced Transcription:** The LLM-powered speech API delivers transcription with improved fluency and contextual awareness, reducing errors caused by homophones, accents, or ambiguous phrases.  
- **Advanced Translation:** The service supports multilingual translation with better handling of idiomatic expressions and context-dependent meanings, enabling more natural and accurate cross-language communication.  
- **Prompt Tuning:** Users can customize the behavior of the LLM through advanced prompt tuning, allowing fine-grained control over transcription and translation outputs to suit specific domain vocabularies or stylistic preferences.  
- **Multilingual Support:** Expanded language coverage and improved handling of code-switching scenarios where multiple languages appear in the same utterance.

**Technical Mechanisms and Implementation Methods**  
The update integrates large pretrained transformer-based language models (similar to GPT architectures) into the speech processing pipeline. Audio input is first converted into preliminary text via acoustic models; then, the LLM refines this text by leveraging its deep contextual understanding to correct errors, disambiguate phrases, and generate fluent output. For translation, the LLM directly generates target language text conditioned on the source speech transcription and contextual prompts. Prompt tuning is implemented by allowing developers to inject custom instructions or context tokens that guide the LLM’s output style and content. This architecture runs on Azure’s scalable infrastructure, utilizing GPU-accelerated compute for real-time or batch processing scenarios.

**Use Cases and Application Scenarios**  
- **Enterprise Transcription:** Accurate meeting, interview, and call center transcription with contextual understanding of industry-specific jargon.  
- **Multilingual Communication:** Real-time translation for global teams, customer support, and content localization.  
- **Content Creation:** Automated subtitling and translation for video and podcast production with stylistic customization.  
- **Accessibility:** Enhanced speech-to-text for assistive technologies supporting diverse languages and dialects.  
- **Data Analytics:** Improved speech data ingestion for downstream NLP tasks such as sentiment analysis or entity recognition.

**Important Considerations and Limitations**  
- As a public preview, the service may have evolving APIs and feature sets; users should monitor updates and test thoroughly before production deployment.  
- Latency and compute costs may be higher compared to traditional speech services due to the complexity of LLM inference.  
- Prompt tuning requires careful design to avoid unintended biases or output inconsistencies.  
- While multilingual support is enhanced, some less common languages or dialects may still have limited accuracy.  
- Data privacy and compliance should be evaluated, especially when processing sensitive audio content.

**Integration with Related Azure Services**  
LLM Speech in Microsoft Foundry can be integrated with Azure Cognitive Services such as Speech-to-Text, Translator, and Language Understanding (LUIS) to build comprehensive conversational AI solutions. It can also be combined with Azure Media Services for automated video captioning workflows or Azure Bot Service for multilingual conversational agents. The service leverages Azure’s security, scalability, and monitoring tools, enabling seamless deployment within enterprise cloud environments

---

### 126. Public Preview: Bring Your Own AI Gateway to Foundry Agent Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Bring Your Own AI Gateway to Foundry Agent Service](https://azure.microsoft.com/updates?id=525957)

**Update ID**: 525957
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Azure announced the public preview of the Bring Your Own (BYO) AI Model Gateway feature for the Foundry Agent Service.

- Key changes or new features  
This feature enables enterprises to integrate Foundry-hosted AI models with any third-party AI gateway services such as Azure API Management, Mulesoft, and Kong. It allows seamless connectivity between external AI gateways and the Foundry Agent Service. The Agent Service supports pre- and post-LLM (Large Language Model) hooks and enforces policy-based model security and governance, ensuring flexible and secure model invocation workflows.

- Target audience affected  
Developers and IT professionals managing AI deployments and integrations, particularly those using Foundry Agent Service and requiring custom AI gateway solutions for model access and governance.

- Important notes if any  
As this is a public preview feature, users should evaluate it in non-production environments and provide feedback. Integration with external gateways allows enterprises to leverage existing API management and security policies while extending Foundry AI capabilities. Documentation and support details are available on the Azure updates page.

**Details**:

The recent public preview of the Bring Your Own (BYO) AI Gateway feature for the Foundry Agent Service introduces a significant enhancement by enabling enterprises to integrate their Foundry-hosted AI models with external AI gateway services such as Azure API Management, Mulesoft, and Kong. This update addresses the need for greater flexibility and control in managing AI model deployment and access within complex enterprise environments.

**Background and Purpose**  
Foundry Agent Service facilitates interaction with large language models (LLMs) and AI models hosted within the Foundry platform. Previously, enterprises were limited to using the native Foundry Agent Service endpoints to access these models. The BYO AI Gateway feature was introduced to allow organizations to leverage their existing API gateway infrastructure, improving governance, security, traffic management, and policy enforcement without disrupting their AI workflows. This aligns with enterprise demands for centralized API management and consistent operational practices.

**Specific Features and Detailed Changes**  
- **Gateway Integration:** Enterprises can now route requests to Foundry-hosted AI models through third-party API gateways such as Azure API Management, Mulesoft, and Kong.  
- **Pre/Post-LLM Hooks:** The Agent Service continues to honor pre- and post-processing hooks around LLM calls, enabling custom logic execution before and after model invocation.  
- **Policy-Based Model Selection:** Organizations can implement policies at the gateway level to control which AI models are invoked based on request context, user roles, or other criteria.  
- **Seamless Connectivity:** The feature supports secure and reliable connectivity between the external gateway and Foundry Agent Service, ensuring consistent model invocation and response handling.

**Technical Mechanisms and Implementation Methods**  
The BYO AI Gateway feature works by exposing Foundry-hosted AI models as backend services that can be proxied through external API gateways. Enterprises configure their chosen gateway to forward API calls to the Foundry Agent Service endpoints. The gateway handles authentication, rate limiting, logging, and other API management functions. Meanwhile, Foundry Agent Service processes the requests, applies pre/post LLM hooks, and returns responses. This decouples the AI model serving layer from the API management layer, allowing independent scaling and policy enforcement.

Implementation typically involves:  
1. Registering Foundry Agent Service endpoints as backend services in the API gateway.  
2. Defining API routes, methods, and policies in the gateway to manage traffic.  
3. Configuring security mechanisms such as OAuth, API keys, or mutual TLS between the gateway and Foundry.  
4. Testing the end-to-end flow to ensure pre/post hooks and policies behave as expected.

**Use Cases and Application Scenarios**  
- **Enterprise API Governance:** Organizations with strict API governance can enforce consistent security and compliance policies on AI model access.  
- **Multi-Model Management:** Enterprises can route requests dynamically to different AI models based on business logic implemented in the gateway.  
- **Hybrid Cloud Architectures:** Companies using hybrid or multi-cloud setups can centralize AI model access via their preferred API gateway, simplifying integration.  
- **Enhanced Monitoring and Analytics:** By routing through established gateways, enterprises can leverage existing monitoring and analytics tools for AI model usage.

**Important Considerations and Limitations**  
- The feature is currently in public preview; production readiness and SLA guarantees should be evaluated accordingly.  
- Latency may increase slightly due to the additional network hop through the external gateway.  
- Proper security configuration is critical to prevent unauthorized access or data leakage.  
- Compatibility with all API gateway features (e.g., advanced transformations) should be validated in testing.  
- Pre/post LLM hooks are honored within Foundry Agent Service but cannot be extended or modified by the external gateway.

**Integration with Related Azure Services**  
- **Azure API Management:** Acts as a robust, scalable gateway supporting authentication, throttling, and policy enforcement for Foundry AI models.  
- **Azure Active Directory (AAD):** Can be used to secure access to the API

---

### 127. Announcing: Developer Training tier for low-cost fine-tuning training

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Announcing: Developer Training tier for low-cost fine-tuning training](https://azure.microsoft.com/updates?id=525952)

**Update ID**: 525952
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry introduced a new Developer Training tier that provides ultra-low-cost fine-tuning model training by utilizing spot capacity.

- Key changes or new features  
The Developer Training tier offers significantly reduced pricing for the training phase of fine-tuning workflows, aligning the cost efficiency with the existing Developer tier used for model hosting. This enables developers to perform fine-tuning at a fraction of the usual cost, making experimentation and iterative model improvements more accessible.

- Target audience affected  
This update primarily benefits developers and data scientists involved in building and fine-tuning AI models, as well as IT professionals managing AI workloads who seek cost-effective training solutions.

- Important notes if any  
Since the tier leverages spot capacity, training jobs may be subject to interruptions or variability in availability, so it is best suited for non-critical or flexible training tasks. Users should design workflows to handle potential preemptions gracefully. This offering helps lower the barrier to entry for fine-tuning large models in Azure Foundry environments.

**Details**:

The newly announced Developer Training tier in Microsoft Foundry introduces an ultra-low-cost option for fine-tuning model training by utilizing spot capacity, aligning the affordability of training with the existing Developer tier for model hosting. This update addresses the growing demand for cost-effective machine learning workflows, particularly for developers and small teams seeking to customize AI models without incurring high training expenses.

**Background and Purpose**  
Fine-tuning pre-trained models is a critical step in adapting AI solutions to specific business needs, but training costs can be prohibitive, especially for smaller organizations or individual developers. While Microsoft Foundry’s Developer tier previously offered affordable hosting for models, training costs remained relatively high. The introduction of the Developer Training tier aims to democratize access to fine-tuning by significantly lowering training costs, thus enabling broader experimentation and innovation.

**Specific Features and Detailed Changes**  
- **Spot Capacity Utilization:** The Developer Training tier leverages Azure’s spot virtual machines, which are spare compute resources offered at discounted rates but with the possibility of eviction when demand rises. This approach drastically reduces training costs compared to on-demand compute.  
- **Cost Alignment:** The pricing model is designed to be comparable to the Developer tier’s hosting costs, making the entire fine-tuning workflow—from training to deployment—more economically accessible.  
- **Seamless Workflow Integration:** The tier integrates directly into existing fine-tuning pipelines within Microsoft Foundry, allowing developers to select this training option without significant changes to their workflows.

**Technical Mechanisms and Implementation Methods**  
The tier operates by scheduling fine-tuning jobs on Azure spot VMs, which provide the necessary GPU or CPU resources at a fraction of the cost of standard instances. The system includes mechanisms to checkpoint training progress and resume jobs in case of spot instance eviction, minimizing the impact of interruptions. This requires the fine-tuning framework to support incremental training and state persistence. Additionally, the Foundry platform manages job orchestration, resource allocation, and fallback strategies to maintain reliability despite the inherent volatility of spot capacity.

**Use Cases and Application Scenarios**  
- **Startups and Independent Developers:** Those with limited budgets can now afford to fine-tune models tailored to their specific domains, such as niche language models or specialized image recognition.  
- **Proof of Concept and Experimentation:** Teams can rapidly iterate on model customization without incurring high costs, accelerating development cycles.  
- **Educational and Research Projects:** Academic users can leverage this tier for training experiments without requiring large financial resources.  
- **Cost-Sensitive Production Workloads:** For applications where occasional training interruptions are acceptable, this tier offers a cost-efficient training solution.

**Important Considerations and Limitations**  
- **Spot Instance Eviction Risk:** Training jobs may be interrupted if spot capacity is reclaimed, requiring robust checkpointing and job resumption strategies. This tier is thus best suited for workloads tolerant of such interruptions.  
- **Performance Variability:** Since spot VMs are allocated based on availability, training times may vary compared to dedicated instances.  
- **Resource Constraints:** The Developer Training tier may have limits on maximum compute resources or job concurrency to maintain affordability.  
- **Not Ideal for Time-Critical Training:** Workloads requiring guaranteed training completion times should consider higher tiers with dedicated resources.

**Integration with Related Azure Services**  
The Developer Training tier is integrated within the Microsoft Foundry ecosystem, which itself leverages Azure Machine Learning for model management and orchestration. It benefits from Azure’s scalable compute infrastructure, including spot VM pools managed via Azure Batch or Azure Kubernetes Service (AKS) with spot node support. Additionally, checkpointing and storage utilize Azure Blob Storage for persistence. This integration ensures that developers can manage training, deployment, monitoring, and versioning within a unified Azure environment, streamlining the end-to-end AI lifecycle.

In summary, the Developer Training tier in Microsoft Foundry offers a cost-effective, spot-capacity-based fine-tuning training option that complements the affordable Developer hosting tier, enabling broader access

---

### 128. Generally Available: Streamline IT governance, security, and cost management experiences with Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Streamline IT governance, security, and cost management experiences with Microsoft Foundry](https://azure.microsoft.com/updates?id=525942)

**Update ID**: 525942
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry’s AI development and management capabilities are now generally available, enhancing IT governance, security, and cost management for enterprises.

- Key changes or new features  
The update enables IT administrators to deploy and manage AI solutions with built-in enterprise-grade security, compliance, and governance controls. It streamlines workflows for managing AI models, data access, and resource usage, helping ensure adherence to organizational policies and regulatory requirements. Cost management features help monitor and optimize AI-related expenditures.

- Target audience affected  
This update primarily targets IT professionals, security and compliance teams, and developers working on enterprise AI deployments who require robust governance and cost control mechanisms.

- Important notes if any  
Microsoft Foundry’s GA release signifies readiness for production use in enterprise environments, supporting scalable and secure AI initiatives. Organizations should evaluate integration with existing governance frameworks to maximize benefits. For detailed implementation guidance, refer to the official Azure update link.

**Details**:

The recent general availability of Microsoft Foundry marks a significant advancement in streamlining AI development, governance, security, and cost management for enterprise IT environments. This update addresses the growing need for robust, scalable, and compliant AI deployment frameworks within large organizations.

**Background and Purpose**  
As enterprises increasingly adopt AI solutions, IT administrators face challenges in managing AI workloads that must comply with stringent security, governance, and cost control policies. Microsoft Foundry was developed to provide a unified platform that simplifies these complexities, enabling secure, compliant, and cost-effective AI deployment at scale. The GA release signals Microsoft’s commitment to delivering enterprise-grade AI management capabilities integrated with Azure’s ecosystem.

**Specific Features and Detailed Changes**  
Microsoft Foundry offers a comprehensive suite of features including:  
- **Governance and Compliance Controls:** Centralized policy enforcement for AI models and data usage that aligns with organizational and regulatory requirements.  
- **Security Management:** Role-based access controls (RBAC), identity management integration, and secure data handling to protect sensitive AI workloads.  
- **Cost Management:** Tools to monitor, allocate, and optimize AI-related expenditures across departments and projects.  
- **Deployment Automation:** Streamlined pipelines for deploying AI models with built-in compliance checks and security validations.  
- **Monitoring and Reporting:** Real-time insights into AI model performance, usage patterns, and compliance status.

**Technical Mechanisms and Implementation Methods**  
Microsoft Foundry operates as a managed service integrated tightly with Azure Active Directory (Azure AD) for identity and access management, Azure Policy for governance enforcement, and Azure Cost Management for financial oversight. It leverages Azure Resource Manager (ARM) templates and Azure DevOps pipelines to automate AI model deployments, embedding compliance and security validations into CI/CD workflows. The platform supports integration with Azure Machine Learning for model training and deployment, ensuring end-to-end lifecycle management within a governed environment.

**Use Cases and Application Scenarios**  
- **Enterprise AI Governance:** Large organizations deploying multiple AI models across departments can enforce consistent security and compliance policies.  
- **Regulated Industries:** Financial services, healthcare, and government sectors benefit from Foundry’s compliance frameworks to meet standards such as GDPR, HIPAA, and FedRAMP.  
- **Cost-Conscious AI Operations:** IT finance teams can track AI resource consumption and optimize budgets effectively.  
- **Hybrid AI Deployments:** Enterprises using both on-premises and cloud AI resources can maintain governance and security uniformly.

**Important Considerations and Limitations**  
- Microsoft Foundry requires integration with existing Azure services, so organizations must have or plan for Azure AD, Azure Policy, and Azure Cost Management adoption.  
- While Foundry simplifies governance, it does not replace the need for organizational policies and human oversight in AI ethics and risk management.  
- Initial setup and configuration may require collaboration between AI developers, IT security teams, and finance departments to align policies and workflows.  
- The service currently focuses on Azure-centric AI workloads; cross-cloud AI governance may require additional tooling.

**Integration with Related Azure Services**  
Microsoft Foundry is designed to work seamlessly with:  
- **Azure Machine Learning:** For model training, deployment, and lifecycle management.  
- **Azure Active Directory:** For identity and access management.  
- **Azure Policy:** To enforce governance rules across AI resources.  
- **Azure Cost Management + Billing:** To monitor and control AI-related costs.  
- **Azure DevOps:** To automate deployment pipelines with embedded compliance checks.

In summary, the general availability of Microsoft Foundry provides IT professionals with a powerful, integrated platform to manage AI deployments securely, compliantly, and cost-effectively within Azure, addressing critical enterprise governance challenges while enabling scalable AI innovation.

---

### 129. Public Preview: New granular controls for network and integration security in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: New granular controls for network and integration security in Microsoft Foundry](https://azure.microsoft.com/updates?id=525933)

**Update ID**: 525933
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry has introduced new granular controls for network and integration security and resource management, now available in public preview.

- Key changes or new features  
The update enables IT administrators to apply fine-grained policies governing network access and integration points within Microsoft Foundry. This includes enhanced configuration options to restrict or allow specific network traffic and tighter control over how AI workloads connect with other enterprise resources. These controls help enforce enterprise-grade security and compliance requirements while maintaining flexibility in AI solution deployment.

- Target audience affected  
IT administrators, security teams, and developers working with Microsoft Foundry for enterprise AI development and deployment will benefit from these enhanced security and management capabilities.

- Important notes if any  
As this feature is in public preview, users should test configurations in non-production environments before full deployment. Documentation and support resources are available to assist with implementation. These controls aim to help enterprises meet strict governance and security standards when integrating AI solutions at scale.

**Details**:

The recent public preview update for Microsoft Foundry introduces enhanced granular controls for network and integration security alongside improved resource management capabilities, aimed at enabling IT administrators to more securely and efficiently deploy enterprise AI solutions. Microsoft Foundry is a comprehensive platform designed to streamline the development, deployment, and governance of AI models at scale within enterprise environments, addressing the complexities of AI lifecycle management.

**Background and Purpose:**  
As enterprises increasingly adopt AI, ensuring robust security and compliance while maintaining operational agility becomes critical. Prior to this update, Foundry provided foundational security and integration features but lacked fine-grained controls that align with stringent enterprise governance policies. This update addresses these gaps by empowering IT admins with detailed network segmentation, integration permissioning, and resource governance controls, thereby reducing the attack surface and improving compliance posture in AI deployments.

**Specific Features and Detailed Changes:**  
- **Granular Network Controls:** Introduction of fine-tuned network policies that allow administrators to define precise ingress and egress rules for Foundry components. This includes support for virtual network (VNet) integration, subnet isolation, and firewall rule configurations to restrict traffic flows at a micro-segmentation level.  
- **Integration Security Enhancements:** Enhanced permission models for external system integrations, enabling admins to specify exact API scopes, authentication methods, and data access permissions per integration point. This reduces the risk of over-permissioned service connections.  
- **Resource Management Improvements:** New capabilities to allocate and monitor resource quotas (CPU, memory, storage) on a per-project or per-team basis within Foundry, facilitating better cost control and operational governance.  
- **Audit and Monitoring:** Expanded logging and auditing features for network and integration activities, providing detailed telemetry for compliance and incident response.

**Technical Mechanisms and Implementation Methods:**  
The update leverages Azure-native networking constructs such as Azure Virtual Networks, Network Security Groups (NSGs), and Azure Firewall policies, integrated directly into the Foundry platform’s deployment templates and configuration interfaces. Network policies are enforced through Azure Policy and role-based access control (RBAC) mechanisms, ensuring that only authorized changes are applied. Integration security enhancements utilize Azure Active Directory (AAD) conditional access and OAuth 2.0 scopes to tightly control API access. Resource management is implemented via Azure Resource Manager (ARM) templates and Foundry’s internal quota management APIs, enabling dynamic resource allocation and governance.

**Use Cases and Application Scenarios:**  
- Enterprises deploying AI models that handle sensitive data can isolate Foundry workloads within dedicated VNets, ensuring no unauthorized lateral movement.  
- Organizations integrating Foundry with multiple external data sources or SaaS platforms can enforce least-privilege access models, minimizing risk from compromised credentials.  
- IT teams can enforce resource usage policies across departments or projects, preventing resource contention and unexpected cost overruns.  
- Security teams gain enhanced visibility into network and integration activities, facilitating compliance audits and rapid incident investigation.

**Important Considerations and Limitations:**  
- As this is a public preview feature, some functionalities may be subject to change and not recommended for production-critical workloads without thorough testing.  
- Network policies require careful planning to avoid inadvertently blocking necessary traffic; misconfigurations could disrupt AI model training or inference pipelines.  
- Integration permission granularity depends on the external system’s support for scoped access tokens and may vary across connectors.  
- Resource quota enforcement is currently limited to specific resource types and may not cover all Foundry components.

**Integration with Related Azure Services:**  
This update tightly integrates with Azure networking services (VNets, NSGs, Azure Firewall), Azure Active Directory for identity and access management, Azure Policy for governance enforcement, and Azure Monitor for telemetry and auditing. It complements Azure Machine Learning and Azure Synapse Analytics by providing a secure, governed environment for AI workloads that can interoperate with these services through controlled network and integration pathways.

In summary, the new granular network and integration security controls in Microsoft Foundry’s public preview significantly enhance enterprise AI deployment security and governance by enabling precise network

---

### 130. Public Preview: Agent mitigations and guardrail customization 

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Agent mitigations and guardrail customization ](https://azure.microsoft.com/updates?id=525923)

**Update ID**: 525923
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite, Security

**Summary**:

- What was updated  
Microsoft Foundry Control Plane now supports agent-level guardrails (previously called content filters), moving beyond model deployment scope.

- Key changes or new features  
Guardrails can be applied directly to individual agents, enabling more granular control. These include existing mitigation controls designed to reduce prompt injection risks, enhancing security and reliability in agent interactions.

- Target audience affected  
Developers and IT professionals managing AI agents and deployments within Microsoft Foundry Control Plane who require customizable security and operational guardrails.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in test environments before production use. The enhanced guardrail customization allows for better alignment with organizational policies and threat models at the agent level.  

For more details, visit: https://azure.microsoft.com/updates?id=525923

**Details**:

The recent Azure update introduces a public preview for agent mitigations and guardrail customization within the Microsoft Foundry Control Plane, enhancing security and control over AI agent behavior. Previously known as content filters, these guardrails have been extended from model-level application to agent-level enforcement, allowing more granular and flexible management of AI interactions. This update aims to address risks such as prompt injection attacks by embedding mitigation controls directly into agents, thereby improving the robustness and reliability of AI deployments.

From a technical perspective, the update enables administrators and developers to define and customize guardrails that govern agent responses and actions. These guardrails incorporate existing mitigation techniques, including prompt injection detection and filtering mechanisms, but now apply them at the agent scope rather than solely on model deployments. This shift allows for tailored security policies that reflect the specific context and operational parameters of each agent, rather than a one-size-fits-all model-level approach. Implementation leverages the Foundry Control Plane’s policy framework, where guardrails can be configured through declarative settings or APIs, enabling integration into CI/CD pipelines and automated governance workflows.

Use cases for this update are broad and particularly relevant in scenarios where AI agents interact with sensitive data or perform critical tasks. For example, enterprises deploying conversational AI agents for customer support can now enforce stricter input validation and response constraints to prevent malicious prompt manipulation. Similarly, in regulated industries such as finance or healthcare, agent-level guardrails help ensure compliance by restricting outputs that could lead to data leakage or non-compliant advice. The customization capabilities also support multi-agent environments where different agents require distinct security postures based on their roles and access levels.

Important considerations include the preview status of the feature, which means it may not yet be fully production-ready and could undergo changes based on user feedback. Additionally, while guardrails improve security, they do not guarantee absolute protection against all adversarial inputs, so complementary security practices remain necessary. Performance impacts should also be evaluated, as additional filtering and mitigation logic may introduce latency in agent responses. Administrators should carefully test guardrail configurations in staging environments before wide deployment.

This update integrates seamlessly with related Azure services such as Azure OpenAI Service, where agents often interface with large language models, and Azure Policy for governance. By managing guardrails through the Foundry Control Plane, organizations can unify AI agent security policies alongside broader cloud governance strategies. Integration with Azure DevOps and monitoring tools further facilitates continuous compliance and operational insights into agent behavior and mitigation effectiveness.

In summary, the public preview of agent mitigations and guardrail customization in Microsoft Foundry Control Plane empowers IT professionals to implement fine-grained, agent-specific security controls that mitigate prompt injection and other risks, enhancing the safe deployment and management of AI agents within Azure environments.

---

### 131. Public Preview: OpenTelemetry visualizations and enhanced monitoring experience in Azure Monitor for Azure VMs and Arc Servers

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: OpenTelemetry visualizations and enhanced monitoring experience in Azure Monitor for Azure VMs and Arc Servers](https://azure.microsoft.com/updates?id=525536)

**Update ID**: 525536
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Azure Monitor now offers OpenTelemetry-based visualizations in public preview, alongside an enhanced and unified monitoring experience for Azure Virtual Machines (VMs) and Azure Arc-enabled servers.

- Key changes or new features  
The update introduces integrated OpenTelemetry visualizations that provide deeper insights into application telemetry data directly within Azure Monitor. It consolidates multiple monitoring capabilities—metrics, logs, and traces—into a single, streamlined view for Azure VMs and Arc servers. This unified experience simplifies troubleshooting and performance analysis by correlating telemetry data across infrastructure and applications. Additionally, it supports enhanced observability workflows leveraging OpenTelemetry standards.

- Target audience affected  
Developers and IT professionals managing Azure Virtual Machines and Azure Arc-enabled servers who require advanced monitoring and observability solutions. This includes those building distributed applications and hybrid environments needing consolidated telemetry data for diagnostics and performance optimization.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Integration with existing monitoring setups may require configuration updates to leverage OpenTelemetry data sources fully. Documentation and best practices are available on the Azure Monitor portal.

**Details**:

The recent Azure Monitor update introduces a public preview of OpenTelemetry-based visualizations combined with an enhanced, unified monitoring experience specifically designed for Azure Virtual Machines (VMs) and Azure Arc-enabled servers. This update aims to streamline and enrich the monitoring workflow by consolidating telemetry data and visualization capabilities into a single pane of glass, thereby improving observability and operational efficiency for hybrid and cloud-native environments.

**Background and Purpose**  
Azure Monitor has long provided comprehensive monitoring for Azure resources, but as enterprises increasingly adopt hybrid cloud architectures and open standards like OpenTelemetry, there is a growing need for integrated, standardized telemetry ingestion and visualization. OpenTelemetry is an open-source observability framework that standardizes the collection of metrics, logs, and traces. By incorporating OpenTelemetry into Azure Monitor, Microsoft seeks to unify telemetry data sources, reduce vendor lock-in, and enhance cross-platform monitoring consistency. This update specifically targets Azure VMs and Arc Servers, reflecting the hybrid and multi-cloud realities where organizations manage both native Azure and on-premises or other cloud-hosted servers.

**Specific Features and Detailed Changes**  
- **OpenTelemetry Visualizations:** The update enables Azure Monitor to ingest and visualize telemetry data collected via OpenTelemetry SDKs and agents. This includes metrics, traces, and logs, providing richer context for performance and reliability analysis.
- **Unified Monitoring Experience:** A consolidated monitoring interface now presents key telemetry from Azure VMs and Arc Servers in a single view, eliminating the need to switch between disparate tools or portals.
- **Enhanced Dashboards:** Users can leverage pre-built and customizable dashboards that integrate OpenTelemetry data alongside native Azure Monitor metrics, facilitating faster root cause analysis.
- **Simplified Configuration:** The preview includes streamlined onboarding processes for enabling OpenTelemetry data collection on Azure VMs and Arc Servers, reducing setup complexity.
- **Support for Hybrid Environments:** By extending OpenTelemetry support to Azure Arc-enabled servers, the update ensures consistent monitoring across on-premises, edge, and multi-cloud servers.

**Technical Mechanisms and Implementation Methods**  
This update leverages the OpenTelemetry Collector, an extensible agent that can be deployed on Azure VMs and Arc Servers to collect telemetry data from applications and system components. The collector exports this data to Azure Monitor’s backend via the Azure Monitor OpenTelemetry Exporter. Azure Monitor then processes and stores this telemetry in Log Analytics workspaces and Application Insights, enabling rich querying and visualization. The unified monitoring experience is implemented through enhancements in the Azure portal, integrating OpenTelemetry data streams with existing Azure Monitor metrics and logs views. Configuration is managed via Azure Policy and Azure Arc extensions, allowing centralized deployment and management of OpenTelemetry collectors.

**Use Cases and Application Scenarios**  
- **Hybrid Infrastructure Monitoring:** Organizations managing a mix of Azure and on-premises servers can use this update to achieve consistent observability without maintaining separate monitoring stacks.
- **Application Performance Management:** Developers and SREs can instrument applications with OpenTelemetry SDKs to collect distributed traces and metrics, visualized directly within Azure Monitor.
- **Incident Response and Troubleshooting:** The unified dashboard accelerates detection and diagnosis of performance bottlenecks or failures by correlating telemetry across infrastructure and application layers.
- **Compliance and Auditing:** Centralized telemetry collection supports compliance requirements by providing comprehensive logs and metrics from hybrid environments.

**Important Considerations and Limitations**  
- As a public preview feature, some capabilities may be subject to change, and SLAs do not apply. Users should evaluate in non-production environments before full adoption.
- OpenTelemetry support currently focuses on Azure VMs and Arc Servers; other Azure resource types may not yet be supported.
- There may be additional costs associated with increased telemetry ingestion and storage in Log Analytics.
- Integration with custom or legacy telemetry sources may require additional configuration or development effort.

**Integration with Related Azure Services**  
- **Azure Arc:** Enables deployment and management of OpenTelemetry collectors on non-Azure servers, extending Azure Monitor’s reach.
- **Log Analytics:** Serves as

---

### 132. Public Preview: Large volumes up to 7.2 PiB     

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Large volumes up to 7.2 PiB     ](https://azure.microsoft.com/updates?id=525150)

**Update ID**: 525150
**Data source**: Azure Updates API

**Categories**: In development, Storage, Azure NetApp Files

**Summary**:

- What was updated  
Azure NetApp Files now supports creating large volumes up to 7.2 PiB with the Cool Access feature on dedicated capacity.

- Key changes or new features  
This update extends the cool-access capability to much larger volumes, allowing efficient storage of infrequently accessed data at a lower cost. Previously, cool-access support was limited to smaller volumes. The new limit of 7.2 PiB enables handling massive datasets while optimizing storage costs by automatically tiering data based on access patterns.

- Target audience affected  
Developers and IT professionals managing large-scale file storage workloads, especially those dealing with big data, archival, or infrequently accessed datasets, will benefit from this feature. It is particularly relevant for enterprises requiring scalable, high-performance file storage with cost-effective data tiering.

- Important notes if any  
This feature is currently in public preview and available on dedicated capacity pools. Users should evaluate it in test environments before production deployment. Monitoring access patterns is recommended to maximize cost savings and performance benefits. For more details and updates, refer to the official Azure update link.

**Details**:

The recent Azure update introduces the public preview of Large Volumes up to 7.2 PiB with Cool Access for Azure NetApp Files (ANF), significantly expanding the maximum volume size and optimizing storage costs for infrequently accessed data on dedicated capacity. This enhancement is designed to address the growing demand for scalable, high-performance file storage solutions that can efficiently manage massive datasets with varying access patterns.

**Background and Purpose:**  
Azure NetApp Files is a high-performance, enterprise-grade file storage service that supports NFS and SMB protocols, widely used for workloads such as databases, analytics, and large-scale file shares. Prior to this update, the maximum volume size on dedicated capacity was limited to 4.5 PiB, which constrained customers with extremely large datasets. Additionally, many workloads generate large volumes of data that are rarely accessed but still require fast retrieval when needed. The introduction of volumes up to 7.2 PiB with Cool Access aims to meet these scalability needs while optimizing cost by leveraging a storage tier designed for infrequently accessed data.

**Specific Features and Detailed Changes:**  
- **Increased Volume Size:** The maximum volume size on dedicated capacity has been extended from 4.5 PiB to 7.2 PiB, enabling support for larger datasets within a single volume.  
- **Cool Access Tier Support:** The update extends the Cool Access feature to these large volumes, allowing data to be stored on a lower-cost tier optimized for infrequently accessed files. Cool Access automatically manages data placement to balance performance and cost.  
- **Dedicated Capacity Only:** This feature is available exclusively on dedicated capacity pools, ensuring predictable performance and isolation for enterprise workloads.

**Technical Mechanisms and Implementation:**  
The Cool Access feature leverages tiering mechanisms within Azure NetApp Files that transparently move data between performance tiers based on access patterns. When data is infrequently accessed, it is placed on the cool tier, which offers lower storage costs but slightly higher latency compared to the hot tier. The system continuously monitors file access and dynamically adjusts data placement without requiring manual intervention. The increase in volume size is achieved through enhancements in the underlying storage architecture and metadata management, allowing efficient handling of larger namespace and data blocks.

**Use Cases and Application Scenarios:**  
- **Big Data and Analytics:** Organizations managing petabyte-scale datasets for analytics can now consolidate data into fewer, larger volumes, simplifying management and improving throughput.  
- **Media and Entertainment:** Large media files that are archived but occasionally retrieved benefit from cost savings due to cool tier storage.  
- **Backup and Disaster Recovery:** Large backup repositories with infrequent access can leverage cool access to reduce storage costs without sacrificing availability.  
- **Scientific Computing:** Research institutions handling massive datasets can scale storage efficiently while optimizing budget.

**Important Considerations and Limitations:**  
- The feature is currently in public preview; users should evaluate in non-production environments and expect potential changes.  
- Cool Access is designed for workloads with infrequent access patterns; workloads requiring consistently high performance should continue using the hot tier.  
- Only available on dedicated capacity pools; not supported on standard or premium tiers or on shared capacity.  
- Monitoring and understanding access patterns is critical to maximize cost benefits and avoid performance degradation.  
- Pricing and SLAs for cool tier storage differ from hot tier and should be reviewed accordingly.

**Integration with Related Azure Services:**  
- Can be combined with Azure Monitor and Azure NetApp Files metrics to track volume usage, performance, and access patterns for better management.  
- Integrates seamlessly with Azure Active Directory and role-based access control (RBAC) for secure access management.  
- Works alongside Azure Backup and Azure Site Recovery for comprehensive data protection strategies.  
- Compatible with Azure Kubernetes Service (AKS) and Azure Virtual Machines for scalable, high-performance file storage in containerized and VM environments.

In summary, the Large Volumes up to 7.2 PiB with Cool Access public preview for Azure NetApp Files on

---

### 133. Public Preview: Built-in CIS benchmarks for Azure endorsed Linux distros in Machine Config

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Built-in CIS benchmarks for Azure endorsed Linux distros in Machine Config](https://azure.microsoft.com/updates?id=523614)

**Update ID**: 523614
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Azure Policy

**Summary**:

- What was updated  
Azure Machine Configuration now includes built-in Center for Internet Security (CIS) benchmarks for all Azure-endorsed Linux distributions, available in public preview.

- Key changes or new features  
The update introduces customizable security benchmarks powered by the azure-osconfig agent, enabling automated compliance assessment and remediation based on CIS standards directly within Azure Machine Configuration. This integration simplifies applying CIS benchmarks without manual configuration, enhancing security posture management for Linux VMs.

- Target audience affected  
Developers and IT professionals managing Linux workloads on Azure, especially those responsible for security compliance, vulnerability management, and automated configuration enforcement.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments before broad deployment. It supports all Azure-endorsed Linux distros, providing a consistent security baseline aligned with industry best practices. Users need to enable the azure-osconfig agent on their VMs to leverage these benchmarks.

**Details**:

The recent Azure update introduces a public preview of built-in Center for Internet Security (CIS) benchmarks specifically tailored for all Azure-endorsed Linux distributions, integrated within Azure Machine Configuration’s customizable security benchmarks feature and powered by the azure-osconfig agent. This enhancement aims to simplify and standardize the security compliance posture of Linux virtual machines (VMs) in Azure by providing pre-configured, industry-recognized security baselines directly within the Azure platform.

**Background and Purpose:**  
Security compliance is critical for enterprise workloads running on cloud infrastructure. The CIS benchmarks are widely accepted best practices for securing operating systems and applications. Prior to this update, applying CIS benchmarks to Linux VMs in Azure required manual configuration or third-party tools, often resulting in inconsistent implementations and increased operational overhead. By embedding these benchmarks natively into Azure Machine Configuration, Microsoft intends to streamline compliance management, reduce configuration errors, and accelerate security posture assessments for Linux workloads.

**Specific Features and Detailed Changes:**  
- **Built-in CIS Benchmarks:** Azure now includes CIS benchmark profiles for all Azure-endorsed Linux distributions (such as Ubuntu, Red Hat Enterprise Linux, CentOS, SUSE, and Oracle Linux) as part of Machine Configuration’s security baseline options.  
- **Customizable Security Benchmarks:** Users can apply these CIS benchmarks out-of-the-box or customize them to fit organizational policies, enabling flexible security configurations.  
- **Integration with azure-osconfig:** The azure-osconfig agent facilitates the enforcement and reporting of these benchmarks on Linux VMs, handling configuration drift detection and remediation.  
- **Public Preview Availability:** This feature is currently in public preview, allowing customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods:**  
The implementation leverages Azure Machine Configuration, a service that enables declarative configuration management for Azure VMs. The azure-osconfig agent runs on Linux VMs, communicating with Azure to receive configuration policies and execute compliance assessments. When a CIS benchmark is applied:  
1. The Machine Configuration service provisions the benchmark profile to the VM via the agent.  
2. The agent evaluates the VM’s current state against the CIS benchmark rules, which include settings such as file permissions, user account policies, and system services configurations.  
3. Non-compliant settings are reported back to Azure Security Center or Azure Policy for visibility.  
4. Optionally, remediation scripts can be triggered to automatically correct deviations, depending on the configuration.

**Use Cases and Application Scenarios:**  
- **Enterprise Security Compliance:** Organizations can enforce CIS benchmarks to meet internal or regulatory security standards for Linux workloads.  
- **Continuous Compliance Monitoring:** Automated drift detection ensures that VMs remain compliant over time, reducing manual audits.  
- **DevSecOps Pipelines:** Integrate security baseline enforcement into CI/CD workflows for Linux VM deployments.  
- **Hybrid Environments:** Apply consistent security policies across on-premises and Azure Linux servers using Azure Arc and Machine Configuration.

**Important Considerations and Limitations:**  
- As a public preview feature, some functionality may change before general availability; production use should be carefully evaluated.  
- Customization capabilities require understanding of CIS controls to avoid misconfigurations.  
- The azure-osconfig agent must be installed and running on Linux VMs for compliance enforcement.  
- Remediation actions may impact system behavior; testing in non-production environments is recommended.  
- Currently, the feature supports only Azure-endorsed Linux distributions; other distros are not covered.

**Integration with Related Azure Services:**  
- **Azure Security Center:** Compliance results from CIS benchmark assessments feed into Security Center’s compliance dashboards, enabling centralized security posture management.  
- **Azure Policy:** CIS benchmarks can be enforced via Azure Policy initiatives, allowing policy-as-code governance across subscriptions.  
- **Azure Arc:** Extends CIS benchmark enforcement to hybrid and multi-cloud Linux servers connected via Azure Arc.  
- **Azure Monitor and Log Analytics:** Compliance data can be ingested for advanced

---

### 134. Public Preview: New AI templates in Microsoft Foundry

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: New AI templates in Microsoft Foundry](https://azure.microsoft.com/updates?id=522554)

**Update ID**: 522554
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry

**Summary**:

- What was updated  
Microsoft Foundry launched new AI templates currently in public preview.

- Key changes or new features  
The update introduces ready-to-use, customizable AI templates designed for common scenarios including live voice agents, release management workflows, data unification processes, and SharePoint integration applications. These templates streamline development by eliminating repetitive setup tasks, accelerating deployment, and enabling faster iteration on AI-powered solutions.

- Target audience affected  
Developers and IT professionals building AI-driven applications or automations within Microsoft Foundry, especially those working on voice interfaces, release pipelines, data integration, and SharePoint-related solutions.

- Important notes if any  
The templates are in public preview, so users should expect ongoing enhancements and potential changes. Feedback from early adopters will help refine the offerings. Integration with existing Microsoft Foundry environments is seamless, promoting rapid prototyping and reducing time-to-value for AI initiatives.

**Details**:

The recent public preview update for Microsoft Foundry introduces a set of new AI templates designed to accelerate the development and deployment of intelligent applications by providing ready-to-use, customizable frameworks targeting common enterprise scenarios such as live voice agents, release management automation, data unification, and SharePoint integration. This enhancement aims to reduce the overhead of repetitive setup and configuration tasks, enabling IT professionals and developers to focus on tailoring AI solutions to specific business needs rather than building foundational components from scratch.

**Background and Purpose**  
Microsoft Foundry is a low-code/no-code AI development platform that facilitates rapid prototyping and deployment of AI-powered applications. The introduction of these AI templates addresses the growing demand for streamlined AI adoption in enterprises by offering pre-built, extensible blueprints that encapsulate best practices and proven architectures. The purpose is to democratize AI development, reduce time-to-market, and improve consistency and reliability of AI implementations across diverse organizational use cases.

**Specific Features and Detailed Changes**  
The update includes multiple AI templates, each targeting a distinct use case:

- **Live Voice Agents:** Templates that integrate speech-to-text, natural language understanding, and text-to-speech capabilities to build conversational agents capable of handling live voice interactions.
- **Release Management:** Automation templates that leverage AI to monitor, analyze, and optimize software release pipelines, improving deployment efficiency and reducing errors.
- **Data Unification:** Templates designed to ingest, cleanse, and merge data from disparate sources, creating unified datasets for analytics and AI model training.
- **SharePoint Integration:** Templates that embed AI functionalities such as document classification, search enhancement, and workflow automation directly within SharePoint environments.

These templates come with pre-configured workflows, connectors, and AI model integrations, significantly reducing manual setup.

**Technical Mechanisms and Implementation Methods**  
The templates leverage Microsoft Foundry’s modular architecture, which integrates Azure Cognitive Services, Azure Machine Learning models, and Azure Logic Apps for orchestration. Each template includes:

- Pre-built pipelines using Azure Data Factory or Synapse for data ingestion and transformation.
- Integration with Azure Cognitive Services APIs (e.g., Speech Services, Language Understanding) for AI capabilities.
- Use of Azure Functions or Logic Apps to handle event-driven automation and orchestration.
- Connectors for enterprise systems like SharePoint, Azure DevOps, and common data sources.

Developers can customize these templates through Foundry’s visual interface or by extending underlying code components, enabling both low-code and pro-code workflows.

**Use Cases and Application Scenarios**  
- Customer service teams deploying voice bots for call centers.
- DevOps teams automating release validation and monitoring.
- Data engineers consolidating data lakes for unified analytics.
- Knowledge workers enhancing SharePoint document management with AI.

These templates serve as accelerators for organizations aiming to embed AI into existing workflows without extensive AI expertise.

**Important Considerations and Limitations**  
- As a public preview, templates may have limited SLA guarantees and could undergo significant changes.
- Customization beyond provided parameters may require advanced development skills.
- Integration depends on existing Azure subscriptions and permissions for services like Cognitive Services and Azure DevOps.
- Data privacy and compliance must be managed carefully, especially when handling sensitive voice or document data.
- Performance and scalability depend on underlying Azure resource configurations.

**Integration with Related Azure Services**  
The templates tightly integrate with a suite of Azure services:

- **Azure Cognitive Services:** For AI capabilities such as speech recognition, language understanding, and vision.
- **Azure Machine Learning:** To deploy and manage custom AI models within workflows.
- **Azure Data Factory/Synapse:** For data orchestration and transformation.
- **Azure Logic Apps and Functions:** For workflow automation and event handling.
- **Azure DevOps:** For release management automation.
- **SharePoint Online:** For embedding AI-enhanced features in collaboration environments.

This integration ensures that enterprises can leverage their existing Azure investments and scale AI solutions efficiently.

In summary, the new AI templates in Microsoft Foundry’s public preview provide IT

---

### 135. Generally Available: Azure Monitor unified onboarding experience for AKS and VMs

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Azure Monitor unified onboarding experience for AKS and VMs](https://azure.microsoft.com/updates?id=521941)

**Update ID**: 521941
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Azure Monitor introduced a unified, single-click onboarding experience for both Azure Kubernetes Service (AKS) clusters and virtual machines (VMs).

- Key changes or new features  
This update simplifies the monitoring setup process by enabling automatic deployment of the latest Azure Monitor capabilities across AKS and VMs through a consolidated onboarding workflow. Users no longer need separate configurations for containers and VMs, reducing complexity and setup time. The onboarding experience ensures consistent monitoring agent deployment and configuration, improving observability and management.

- Target audience affected  
Developers and IT professionals managing Azure Kubernetes Service clusters and virtual machines who require streamlined monitoring setup and enhanced operational insights.

- Important notes if any  
This unified onboarding is now generally available, meaning it is fully supported for production use. Users should leverage this experience to ensure they are using the most current Azure Monitor features and best practices for monitoring both containerized and VM workloads. For detailed steps and guidance, refer to the official Azure Monitor documentation.

**Details**:

The recent Azure Monitor update introduces a unified onboarding experience for Azure Kubernetes Service (AKS) clusters and virtual machines (VMs), now generally available, designed to streamline and simplify the deployment of monitoring capabilities across these compute resources. 

**Background and Purpose:**  
Traditionally, onboarding AKS clusters and VMs to Azure Monitor required separate processes, often involving multiple steps such as manual agent installation, configuration of monitoring solutions, and linkage to Log Analytics workspaces. This fragmented approach increased complexity and time-to-insight for IT professionals managing hybrid environments. The update addresses this by providing a single-click, unified onboarding workflow that reduces operational overhead and accelerates the deployment of monitoring agents and solutions, ensuring consistent observability across containerized and VM workloads.

**Specific Features and Detailed Changes:**  
- **Unified Onboarding UI:** A consolidated interface within the Azure portal allows users to onboard both AKS clusters and VMs simultaneously or individually with minimal configuration.  
- **Automatic Agent Deployment:** The system automatically deploys the latest Azure Monitor agents—such as the Azure Monitor for containers agent on AKS and the Azure Monitor agent (AMA) on VMs—eliminating manual installation steps.  
- **Latest Monitoring Capabilities:** Ensures that the newest features and performance improvements in Azure Monitor are applied, including enhanced metrics collection, log analytics, and diagnostic settings.  
- **Integrated Configuration:** Automatically configures data collection rules, diagnostic settings, and workspace associations, reducing the need for manual setup and potential misconfigurations.

**Technical Mechanisms and Implementation Methods:**  
The unified onboarding leverages Azure Resource Manager (ARM) templates and Azure Policy to automate the deployment and configuration of monitoring agents. For AKS, the onboarding process deploys the Azure Monitor container insights agent as a DaemonSet within the Kubernetes cluster, ensuring comprehensive telemetry collection from nodes, controllers, and containers. For VMs, the Azure Monitor agent is installed as an extension, configured to send telemetry data to the designated Log Analytics workspace. The onboarding workflow also integrates with Azure Arc for hybrid environments, enabling consistent monitoring across on-premises and multi-cloud VMs.

**Use Cases and Application Scenarios:**  
- **DevOps and SRE Teams:** Quickly enable monitoring for new AKS clusters and VM deployments as part of CI/CD pipelines or infrastructure provisioning, ensuring immediate observability.  
- **Hybrid Cloud Monitoring:** Simplify the onboarding of both cloud-hosted and on-premises VMs managed via Azure Arc, providing a single pane of glass for infrastructure health and performance.  
- **Cost and Performance Optimization:** By standardizing monitoring setup, organizations can more effectively collect and analyze telemetry data to optimize resource utilization and troubleshoot issues proactively.

**Important Considerations and Limitations:**  
- **Workspace Association:** The onboarding process requires an existing or new Log Analytics workspace; careful planning of workspace scope and data retention policies is necessary to manage costs and data governance.  
- **Agent Compatibility:** While the unified experience deploys the latest agents, some legacy or custom monitoring solutions may require manual adjustments.  
- **Role-Based Access Control (RBAC):** Proper permissions are required to deploy agents and configure monitoring settings; users must have contributor or monitoring-specific roles on the target resources.  
- **Resource Scale:** For very large-scale environments, onboarding may take time due to agent deployment and configuration propagation; monitoring deployment status is recommended.

**Integration with Related Azure Services:**  
- **Azure Arc:** Extends the unified onboarding to hybrid and multi-cloud VMs, enabling consistent monitoring beyond Azure-native resources.  
- **Azure Policy:** Can enforce monitoring onboarding compliance across subscriptions and resource groups, automating governance.  
- **Azure Security Center:** Leverages Azure Monitor data for enhanced security posture management and threat detection.  
- **Azure Automation and Logic Apps:** Can be integrated to automate remediation workflows triggered by monitoring alerts.

In summary, the generally available Azure Monitor unified onboarding experience significantly enhances operational efficiency by providing a streamlined, automated, and consistent method

---

### 136. Public Preview: Azure Copilot brings new intelligent agents to support end-to-end lifecycle management of workloads

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Azure Copilot brings new intelligent agents to support end-to-end lifecycle management of workloads](https://azure.microsoft.com/updates?id=520762)

**Update ID**: 520762
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Azure Copilot, Microsoft Ignite, Features

**Summary**:

- What was updated  
Azure Copilot now offers new intelligent agents in public preview designed to support end-to-end lifecycle management of workloads, including migration, operation, and modernization across any environment.

- Key changes or new features  
The update introduces specialized agents (currently in gated preview) that assist developers and IT professionals in workload migration, operational tasks, and modernization efforts. Additionally, Azure Copilot evolves from a chat interface into an immersive, full-screen command center powered by GPT-5 reasoning capabilities, enabling advanced artifact generation and contextual assistance throughout workload management.

- Target audience affected  
Developers, IT professionals, and cloud architects involved in workload migration, management, and modernization on Azure or hybrid environments will benefit from these enhancements.

- Important notes if any  
The specialized agents are in gated preview, requiring sign-up or invitation to access. The full-screen command center with GPT-5 integration is in public preview, allowing broader access for testing and feedback. This update represents a significant step toward AI-driven, integrated workload lifecycle management within Azure.  

For more details, visit: https://azure.microsoft.com/updates?id=520762

**Details**:

Azure has announced the public preview of Azure Copilot, an advanced AI-driven platform designed to enhance end-to-end lifecycle management of workloads through intelligent agents and an immersive command center interface. This update leverages GPT-5 reasoning capabilities to transform workload migration, operation, and modernization processes across diverse environments.

**Background and Purpose**  
As cloud environments grow increasingly complex, IT professionals face challenges in managing workloads spanning on-premises, multi-cloud, and edge locations. Traditional tools often require manual intervention and fragmented workflows. Azure Copilot aims to address these challenges by embedding AI-powered agents that provide contextual assistance, automation, and intelligent recommendations throughout the workload lifecycle, thereby improving operational efficiency and reducing errors.

**Specific Features and Detailed Changes**  
- **Specialized Intelligent Agents (Gated Preview):** Azure Copilot introduces domain-specific agents tailored for workload migration, operational management, and modernization tasks. These agents analyze workload characteristics, dependencies, and performance metrics to recommend optimal migration paths, automate routine operations, and suggest modernization strategies such as containerization or refactoring.  
- **Immersive Full-Screen Command Center (Public Preview):** The user interface evolves from a simple chat experience to a comprehensive command center that supports multi-modal interactions. This interface integrates GPT-5’s advanced reasoning to generate artifacts such as scripts, deployment templates, and diagnostic reports dynamically, enabling users to execute complex commands and visualize workload states in real time.  
- **GPT-5 Reasoning and Artifact Generation:** The underlying AI model not only understands natural language queries but also synthesizes actionable outputs, including code snippets, configuration files, and step-by-step guidance, accelerating decision-making and execution.

**Technical Mechanisms and Implementation Methods**  
Azure Copilot operates by integrating GPT-5-based AI models with Azure’s telemetry and management APIs. The intelligent agents continuously ingest telemetry data from Azure Monitor, Azure Resource Graph, and other diagnostic sources to maintain up-to-date context about workloads. The command center interfaces with Azure Resource Manager (ARM) and Azure Automation to execute generated scripts and orchestrate workflows. Security and compliance are enforced through role-based access control (RBAC) and Azure Policy integration, ensuring that AI-driven actions adhere to organizational governance.

**Use Cases and Application Scenarios**  
- **Workload Migration:** Automated assessment of on-premises or other cloud workloads, generation of migration plans, and execution assistance for lift-and-shift or replatforming strategies.  
- **Operational Management:** Proactive monitoring and troubleshooting through AI-generated diagnostics, automated remediation scripts, and performance tuning recommendations.  
- **Modernization:** Guidance on adopting cloud-native architectures, including containerization, microservices, and serverless computing, with artifact generation to bootstrap modernization efforts.  
- **Cross-Environment Management:** Managing workloads consistently across hybrid and multi-cloud environments using a unified AI-powered interface.

**Important Considerations and Limitations**  
- The specialized intelligent agents are currently in gated preview, requiring enrollment and may have limited availability or feature sets.  
- As a preview feature, users should expect iterative improvements and potential instability; production use should be cautiously evaluated.  
- AI-generated recommendations and artifacts require validation by IT professionals to ensure alignment with organizational policies and technical constraints.  
- Data privacy and security considerations must be addressed, especially when telemetry and workload metadata are processed by AI models.

**Integration with Related Azure Services**  
Azure Copilot tightly integrates with core Azure management services such as Azure Monitor for telemetry ingestion, Azure Resource Manager for resource orchestration, Azure Automation for workflow execution, and Azure Policy for governance enforcement. It also leverages Azure Active Directory for authentication and RBAC, ensuring secure and compliant operations. Additionally, it can interface with Azure DevOps and GitHub for CI/CD pipeline integration, facilitating automated deployment and modernization workflows.

In summary, Azure Copilot’s public preview introduces a transformative AI-powered platform that enhances workload lifecycle management by combining intelligent agents with an immersive command center powered by GPT-5. This update enables IT professionals to automate complex

---

### 137. Public Preview: Dynamic threshold for Log search alerts

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Dynamic threshold for Log search alerts](https://azure.microsoft.com/updates?id=503704)

**Update ID**: 503704
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Features

**Summary**:

- What was updated  
Azure Monitor has introduced dynamic threshold capabilities to Log search alerts, now available in public preview.

- Key changes or new features  
Dynamic thresholds automatically calculate appropriate alert thresholds based on historical log data patterns, eliminating the need for manual threshold configuration. This enhances alert accuracy by adapting to normal fluctuations and reduces false positives and alert fatigue. Developers and IT professionals can now create Log search alerts that intelligently adjust sensitivity over time without constant tuning.

- Target audience affected  
This update primarily benefits developers, IT operations teams, and SREs who rely on Azure Monitor Log alerts to detect anomalies and monitor application or infrastructure health.

- Important notes if any  
As this feature is in public preview, users should evaluate it in non-production environments before full adoption. Integration with existing alerting workflows and action groups remains supported. Users can enable dynamic thresholds via the Azure portal, CLI, or API when configuring Log search alerts. For detailed guidance and limitations, refer to the official Azure update documentation.

**Details**:

Azure Monitor has introduced a public preview feature that extends dynamic threshold capabilities to Log search alerts, enabling more intelligent and adaptive alerting based on log data patterns. Traditionally, setting static thresholds for log-based alerts requires manual tuning and domain expertise to determine appropriate limits, which can be challenging due to fluctuating workloads and varying baseline behaviors. This update addresses these challenges by automatically calculating dynamic thresholds, reducing false positives and improving alert relevance.

**Background and Purpose**  
Azure Monitor’s dynamic threshold alerting was initially available for metric alerts, where it uses machine learning algorithms to analyze historical metric data and establish adaptive thresholds that reflect normal operational patterns. Extending this capability to Log search alerts allows IT professionals to leverage similar intelligence for alerts based on log queries, which often involve complex, multi-dimensional data. The purpose is to simplify alert configuration, reduce alert noise, and enhance proactive monitoring by dynamically adjusting thresholds according to recent log trends.

**Specific Features and Changes**  
- **Dynamic Thresholds for Log Alerts:** Instead of static numeric thresholds, alert rules can now use dynamic thresholds that adapt based on historical log query results.  
- **Automatic Baseline Calculation:** The system analyzes historical log data to determine expected ranges and flags deviations that indicate anomalies.  
- **Support for Kusto Query Language (KQL) Queries:** Dynamic thresholds work with custom log queries, enabling flexible and powerful alert definitions.  
- **Integration with Existing Alert Rules:** Users can convert existing log alert rules to use dynamic thresholds or create new ones with this feature.  
- **Public Preview Availability:** The feature is currently in public preview, allowing users to test and provide feedback before general availability.

**Technical Mechanisms and Implementation**  
The dynamic threshold mechanism for log alerts leverages time-series anomaly detection algorithms applied to the results of KQL queries over a configurable historical window. The process involves:  
1. Executing the log query periodically to collect baseline data points.  
2. Applying statistical and machine learning models to identify normal behavior patterns and calculate upper and lower dynamic thresholds.  
3. Continuously comparing new query results against these thresholds to detect anomalies.  
4. Triggering alerts when the query results exceed the dynamically calculated thresholds.  
This approach requires sufficient historical data to build an accurate baseline and adapts over time as patterns evolve.

**Use Cases and Application Scenarios**  
- **Security Monitoring:** Detect unusual spikes in failed login attempts or suspicious activity without manually setting thresholds.  
- **Application Performance:** Identify anomalies in error rates or latency from application logs dynamically.  
- **Infrastructure Health:** Monitor resource utilization or event counts that fluctuate with workload changes.  
- **Operational Insights:** Alert on unexpected deviations in business metrics derived from logs, such as transaction volumes or customer interactions.

**Important Considerations and Limitations**  
- **Data Volume and Quality:** Effective dynamic thresholding depends on sufficient and consistent historical log data. Sparse or highly irregular data may reduce accuracy.  
- **Learning Period:** There is an initial learning period during which the system collects baseline data before reliable thresholds are established.  
- **Preview Status:** As a public preview feature, it may have limitations in SLA, regional availability, or integration scope. Users should validate in non-production environments.  
- **Configuration Complexity:** While dynamic thresholds reduce manual tuning, understanding query behavior and alert sensitivity remains important to avoid missed or excessive alerts.

**Integration with Related Azure Services**  
- **Azure Monitor Logs:** The feature directly integrates with Azure Monitor Logs, utilizing KQL queries for alert definitions.  
- **Azure Alerts:** Dynamic threshold alerts feed into Azure Alerts infrastructure, enabling action groups, automated responses, and incident management.  
- **Azure Sentinel:** Security teams can leverage dynamic threshold log alerts within Azure Sentinel for enhanced threat detection.  
- **Azure Logic Apps and Automation:** Alerts can trigger workflows or remediation actions via Logic Apps or Azure Automation, enabling automated incident response.

In summary, the introduction of dynamic thresholds for Log search alerts in Azure Monitor public preview empowers IT

---

### 138. Generally Available: Custom error pages on Azure App Service

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Generally Available: Custom error pages on Azure App Service](https://azure.microsoft.com/updates?id=492303)

**Update ID**: 492303
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Mobile, Web, App Service, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure App Service now generally supports custom error pages.

- Key changes or new features  
Developers and IT professionals can configure their web applications hosted on Azure App Service to display custom error pages instead of the default generic error messages. This enables improved user experience by providing branded, informative, or localized error responses tailored to specific HTTP error codes.

- Target audience affected  
Web developers, DevOps engineers, and IT professionals managing Azure App Service applications who want to enhance error handling and user communication during application faults or downtime.

- Important notes if any  
Custom error pages must be configured explicitly within the App Service settings or via application code. This feature is now fully supported in production environments, allowing for consistent error presentation across all supported runtimes and frameworks on Azure App Service. For detailed implementation guidance, refer to the official Azure documentation.  

Link: https://azure.microsoft.com/updates?id=492303

**Details**:

The recent general availability of custom error pages on Azure App Service enables developers and IT professionals to replace default HTTP error responses with tailored error pages, enhancing user experience and brand consistency during fault conditions. Previously, Azure App Service displayed standard error pages (e.g., 404 Not Found, 500 Internal Server Error) that were generic and lacked customization options, which could lead to user confusion or diminished trust. This update addresses that gap by allowing full control over error page content and presentation.

**Background and Purpose**  
Azure App Service hosts web applications and APIs, which inevitably encounter errors such as client-side (4xx) or server-side (5xx) issues. Default error pages, while informative, are generic and do not align with an organization’s branding or provide contextual guidance to end users. The purpose of this update is to empower developers to define custom error pages that improve user engagement, reduce bounce rates, and provide clearer instructions or navigation options during error states.

**Specific Features and Detailed Changes**  
- Support for configuring custom error pages for HTTP status codes, including but not limited to 400, 401, 403, 404, 500, and 503.  
- Ability to specify error page content either via static HTML files or dynamic endpoints within the app or external URLs.  
- Configuration can be done through Azure Portal, Azure CLI, ARM templates, or REST API, enabling automation and infrastructure-as-code practices.  
- Custom error pages are served seamlessly without additional routing logic required in application code, simplifying implementation.  
- The feature supports both Windows and Linux App Service plans, as well as Web Apps for Containers.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure App Service intercepts HTTP error responses generated by the application or platform and substitutes the response body with the configured custom error page. This is achieved at the platform gateway level before the response is sent to the client. To implement, users upload their custom error page files to a designated directory in the App Service file system or specify URLs to external error pages. Configuration settings are applied via the `customErrorPages` property in the App Service configuration, which maps HTTP status codes to the corresponding error page resource. This approach offloads error handling from application code, reducing complexity and potential error propagation.

**Use Cases and Application Scenarios**  
- E-commerce sites can display branded, user-friendly error pages that suggest alternative products or provide customer support links during outages or missing pages.  
- SaaS providers can embed troubleshooting tips or self-service links on error pages to reduce support tickets.  
- Enterprises can maintain compliance and consistent messaging by controlling error content across multiple apps and environments.  
- Applications with international audiences can serve localized error pages to improve accessibility and user satisfaction.

**Important Considerations and Limitations**  
- Custom error pages should be lightweight and optimized for fast loading to avoid exacerbating user frustration during errors.  
- If the custom error page itself encounters errors or is unavailable, the platform falls back to the default error page.  
- HTTPS should be enforced on custom error pages to maintain security and trust.  
- Custom error pages do not replace application-level error handling; they complement it by providing a fallback presentation layer.  
- Monitoring and logging should still be implemented within the app to capture error details for diagnostics, as custom error pages only affect user-facing responses.

**Integration with Related Azure Services**  
- Azure Front Door or Azure Application Gateway can be used in conjunction with custom error pages to provide global load balancing and enhanced security, while still serving custom error content.  
- Azure Monitor and Application Insights remain critical for capturing telemetry and diagnosing the root causes behind errors that trigger custom error pages.  
- Azure DevOps pipelines can automate deployment and configuration of custom error pages as part of CI/CD workflows using ARM templates or CLI scripts.  
- Integration with Azure Blob Storage is possible if custom error pages are hosted externally, enabling centralized management of error content.

In summary, the general availability of

---

### 139. Public Preview: Online container copy in Azure Cosmos DB 

**Published**: November 18, 2025 16:00:16 UTC
**Link**: [Public Preview: Online container copy in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=467471)

**Update ID**: 467471
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Cosmos DB now supports online container copy in public preview, enabling real-time data copying between containers within the same or different Cosmos DB accounts.

- Key changes or new features  
This feature allows developers and IT professionals to copy data from a source container to a target container without taking the source container offline, minimizing downtime. The source container remains fully operational during the copy process, ensuring continuous application availability. The online copy process supports large datasets and maintains data consistency. This capability simplifies data migration, backup, and environment cloning scenarios.

- Target audience affected  
Developers and IT professionals managing Azure Cosmos DB workloads who require seamless data migration, replication, or environment setup with minimal disruption.

- Important notes if any  
The feature is currently in public preview, so it should be used with caution in production environments. Users should monitor performance impacts during the copy operation and review Azure Cosmos DB limits and pricing implications related to data throughput and storage. For detailed guidance and limitations, refer to the official Azure documentation.  

Link: https://azure.microsoft.com/updates?id=467471

**Details**:

The recent Azure Cosmos DB update introduces the public preview of the online container copy feature, enabling near real-time data copying between containers within or across Cosmos DB accounts while minimizing downtime for applications relying on the source container.

**Background and Purpose**  
Traditionally, copying data between Cosmos DB containers required offline operations or complex data migration workflows that often resulted in application downtime or data staleness. This update addresses the need for seamless, low-impact data replication and migration scenarios by allowing continuous data copying without interrupting ongoing read/write operations on the source container. This capability is particularly valuable for scenarios involving data reorganization, scaling, environment cloning, or disaster recovery preparations.

**Specific Features and Detailed Changes**  
- **Online Container Copy:** Enables copying data from a source container to a target container in real time.  
- **Minimal Downtime:** The source container remains fully operational for both reads and writes during the copy process.  
- **Cross-Account Support:** Copying is supported both within the same Cosmos DB account and across different accounts, facilitating flexible data movement.  
- **Incremental Sync:** After the initial bulk copy, ongoing changes (inserts, updates, deletes) are continuously synchronized to the target container until the copy operation is finalized.  
- **Operational Control:** Users can monitor and manage the copy operation via Azure Portal, CLI, or SDKs, with options to pause, resume, or cancel the process.

**Technical Mechanisms and Implementation Methods**  
The online container copy leverages Cosmos DB’s change feed mechanism to track incremental changes in the source container. The process involves two phases:  
1. **Initial Data Copy:** A snapshot of the existing data is bulk copied to the target container using optimized internal pipelines that ensure high throughput and consistency.  
2. **Change Feed Synchronization:** Post initial copy, the change feed continuously streams data modifications from the source container to the target container, ensuring eventual consistency and near real-time synchronization.  

This approach ensures that the target container reflects the source container’s state with minimal lag, without locking or blocking operations on the source. The copy operation uses Cosmos DB’s internal transactional and consistency guarantees to maintain data integrity.

**Use Cases and Application Scenarios**  
- **Zero-Downtime Data Migration:** Seamlessly migrate data to new containers or accounts without impacting live applications.  
- **Data Reorganization:** Restructure data models by copying data into containers with different partition keys or throughput settings.  
- **Disaster Recovery and Backup:** Create near real-time replicas of containers for backup or failover purposes.  
- **Environment Cloning:** Quickly replicate production data to development or testing environments.  
- **Scaling and Performance Optimization:** Move data to containers with optimized configurations for specific workloads.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it may have limitations or changes before general availability. Production use should be carefully evaluated.  
- **Throughput and Cost:** Copy operations consume RU/s on both source and target containers; plan throughput and budget accordingly.  
- **Consistency Model:** The synchronization relies on Cosmos DB’s consistency levels; eventual consistency is typical during incremental sync.  
- **Partition Key Constraints:** Target containers must have compatible partition keys; changes in partition key definitions require careful planning.  
- **Data Types and Features:** Some Cosmos DB features or data types might have restrictions during copy; verify compatibility.  
- **Operation Duration:** Large datasets may require significant time to complete initial copy and synchronization phases.

**Integration with Related Azure Services**  
- **Azure Monitor and Alerts:** Integration allows monitoring the copy operation’s health and performance metrics.  
- **Azure CLI and SDKs:** Supports automation and integration into CI/CD pipelines or operational scripts.  
- **Azure Role-Based Access Control (RBAC):** Ensures secure permission management for initiating and managing copy operations.  
- **Azure Data Factory:** While Data Factory supports data movement, online container copy offers a more native,

---

### 140. Generally Available: The Archive access tier for Azure Blob Storage is now generally available in the Taiwan North region

**Published**: November 18, 2025 14:00:03 UTC
**Link**: [Generally Available: The Archive access tier for Azure Blob Storage is now generally available in the Taiwan North region](https://azure.microsoft.com/updates?id=527181)

**Update ID**: 527181
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage

**Summary**:

- What was updated  
The Archive access tier for Azure Blob Storage has reached general availability in the Taiwan North region.

- Key changes or new features  
This update enables customers in Taiwan to store infrequently accessed data in the Archive tier locally, benefiting from significantly lower storage costs compared to Hot and Cool tiers. The Archive tier is optimized for long-term retention and compliance, with data retrieval times typically measured in hours. This regional availability supports data residency requirements for organizations operating in Taiwan.

- Target audience affected  
Developers and IT professionals managing data storage solutions in Taiwan, particularly those handling large volumes of infrequently accessed data requiring cost-effective, compliant storage options.

- Important notes if any  
Users should plan for the Archive tier’s retrieval latency and potential data access costs when designing storage and data retrieval strategies. This expansion helps meet local data residency and compliance needs while optimizing storage expenditure. For more details, refer to the official Azure update link.

**Details**:

The Azure update announces the general availability of the Archive access tier for Azure Blob Storage in the Taiwan North region, enabling customers in Taiwan to leverage cost-efficient long-term storage for infrequently accessed data while complying with data residency requirements.

**Background and Purpose:**  
Azure Blob Storage offers multiple access tiers—Hot, Cool, and Archive—to optimize storage costs based on data access patterns. The Archive tier is designed for data that is rarely accessed and can tolerate retrieval latency, providing the lowest storage cost. Prior to this update, the Archive tier was not available in the Taiwan North region, limiting local customers’ ability to store cold data cost-effectively within their preferred data residency boundaries. This update addresses that gap by expanding regional availability, supporting compliance with local data governance and residency mandates.

**Specific Features and Detailed Changes:**  
- The Archive tier is now fully supported and generally available in the Taiwan North region.  
- Customers can create new Blob Storage accounts or configure existing ones to use the Archive tier for blob objects.  
- Data stored in the Archive tier benefits from significantly reduced storage costs compared to Hot and Cool tiers, albeit with higher latency and costs for data retrieval and rehydration.  
- The update ensures parity of features and SLAs for Archive tier blobs in Taiwan North with other global regions where Archive is available.

**Technical Mechanisms and Implementation Methods:**  
- The Archive tier stores blob data offline on lower-cost media, requiring explicit rehydration to Hot or Cool tiers before data can be read.  
- Blob objects can be transitioned to Archive tier via lifecycle management policies or manual tier changes using Azure Storage SDKs, CLI, or Portal.  
- Rehydration is an asynchronous operation that can take hours, depending on blob size and priority (Standard or High).  
- The storage system maintains metadata and blob properties to track tier status and manage access control during tier transitions.  
- Integration with Azure Resource Manager enables automation and policy enforcement for tier management.

**Use Cases and Application Scenarios:**  
- Long-term archival of compliance, audit, or legal data that must remain in Taiwan for regulatory reasons.  
- Backup and disaster recovery data sets that are rarely accessed but must be retained for extended periods.  
- Media and scientific data archives where retrieval is infrequent and predictable.  
- Cost optimization for large-scale data lakes and IoT telemetry data that require tiered storage strategies.

**Important Considerations and Limitations:**  
- Data retrieval from Archive tier incurs latency ranging from hours to potentially longer, which is unsuitable for scenarios requiring immediate access.  
- Early deletion charges apply if blobs are deleted or moved out of Archive tier before the minimum retention period (typically 180 days).  
- Archive tier blobs are immutable and cannot be read or modified until rehydrated to an online tier.  
- Lifecycle management policies should be carefully designed to avoid unintended costs or access delays.  
- Network egress and transaction costs apply during rehydration and data access.

**Integration with Related Azure Services:**  
- Azure Blob Storage lifecycle management policies can automate tier transitions between Hot, Cool, and Archive tiers based on custom rules and schedules.  
- Azure Backup and Azure Site Recovery can leverage Archive tier for cost-effective long-term retention.  
- Azure Data Factory and Azure Synapse Analytics can orchestrate data movement workflows that include tier transitions for archival data.  
- Azure Monitor and Azure Policy can be used to monitor storage usage and enforce compliance with organizational data governance policies.

In summary, the general availability of the Archive access tier in the Taiwan North region empowers IT professionals to implement cost-effective, compliant, and scalable cold storage solutions locally, leveraging Azure Blob Storage’s tiering capabilities integrated with Azure’s ecosystem for automated data lifecycle management and governance.

---

### 141. Public preview: Support for large volume breakthrough mode

**Published**: November 18, 2025 14:00:03 UTC
**Link**: [Public preview: Support for large volume breakthrough mode](https://azure.microsoft.com/updates?id=516656)

**Update ID**: 516656
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files introduced public preview support for large volume breakthrough mode.

- Key changes or new features  
Breakthrough mode now supports extremely large volumes up to 2 PiB, enabling unprecedented scalability for high-performance computing (HPC) and electronic design automation (EDA) workloads. It delivers throughput up to 50 GiBps, depending on workload characteristics, significantly boosting performance for demanding applications.

- Target audience affected  
Developers and IT professionals working with HPC, EDA, and other data-intensive workloads that require high throughput and large-scale storage will benefit from this update. Storage architects designing scalable, high-performance file storage solutions on Azure should also take note.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Performance gains depend on workload specifics, so testing is recommended to optimize configurations. Pricing and SLA details may differ from GA features.

**Details**:

The recent public preview update for Azure NetApp Files introduces support for large volume breakthrough mode, significantly enhancing performance and scalability for high-demand workloads such as High-Performance Computing (HPC) and Electronic Design Automation (EDA). This update addresses the growing need for handling extremely large datasets and throughput-intensive applications by enabling volumes up to 2 PiB in size and delivering throughput up to 50 GiBps, depending on workload characteristics.

**Background and Purpose:**  
Azure NetApp Files is a fully managed file storage service designed for enterprise workloads requiring high throughput and low latency. Traditional volume sizes and performance limits constrained some HPC and EDA use cases that demand massive storage capacity combined with extreme performance. The breakthrough mode was introduced to overcome these limitations by providing a new performance tier that scales both capacity and throughput beyond previous limits, enabling customers to run large-scale simulations, complex data analytics, and design workflows more efficiently.

**Specific Features and Detailed Changes:**  
- **Large Volume Support:** Volumes can now scale up to 2 PiB (Pebibytes), a substantial increase over prior limits, facilitating storage of massive datasets without the need to shard across multiple volumes.  
- **High Throughput:** Breakthrough mode supports throughput up to 50 GiBps, which is a significant boost for data-intensive workloads, enabling faster read/write operations and reduced job runtimes.  
- **Dynamic Performance Scaling:** The throughput is workload-dependent, allowing the system to optimize performance based on I/O patterns and concurrency.  
- **Public Preview Availability:** This feature is currently in public preview, allowing customers to test and validate the capabilities in their environments before general availability.

**Technical Mechanisms and Implementation Methods:**  
Breakthrough mode leverages Azure NetApp Files’ underlying architecture optimized for parallelism and low latency. It utilizes advanced caching, network optimizations, and distributed metadata management to maintain consistency and performance at scale. The service integrates with Azure’s high-speed networking infrastructure, including RDMA (Remote Direct Memory Access) capabilities, to minimize latency and maximize throughput. The volume provisioning APIs have been extended to allow creation and management of breakthrough mode volumes, with specific parameters to configure performance targets.

**Use Cases and Application Scenarios:**  
- **HPC Workloads:** Scientific simulations, weather modeling, and seismic analysis that require large datasets and fast I/O to reduce compute time.  
- **EDA Workflows:** Chip design and verification processes that involve massive file sets and require rapid access to design data.  
- **Big Data Analytics:** Processing large-scale datasets with tools that benefit from high throughput file storage.  
- **Media and Entertainment:** Rendering and video processing workloads that need high-speed access to large media files.

**Important Considerations and Limitations:**  
- Being in public preview, breakthrough mode volumes may have limited regional availability and might not be covered by standard SLAs.  
- Workload characteristics significantly influence achievable throughput; not all workloads will reach the 50 GiBps maximum.  
- Pricing and billing models for breakthrough mode volumes may differ from standard tiers and should be reviewed carefully.  
- Integration with backup and disaster recovery solutions should be validated as breakthrough mode volumes may have specific compatibility requirements.

**Integration with Related Azure Services:**  
Breakthrough mode volumes can seamlessly integrate with Azure compute services such as Azure Virtual Machines and Azure Kubernetes Service (AKS) that require high-performance shared storage. They can be mounted using NFS protocols supported by Azure NetApp Files. Additionally, integration with Azure Monitor and Azure Advisor enables performance monitoring and optimization recommendations. For data protection, Azure Backup and third-party solutions compatible with Azure NetApp Files can be used, subject to breakthrough mode support.

In summary, the public preview of large volume breakthrough mode in Azure NetApp Files empowers IT professionals to handle extremely large and performance-intensive workloads by providing volumes up to 2 PiB and throughput up to 50 GiBps, leveraging Azure’s advanced networking and storage technologies to meet the demands of HPC, EDA, and

---

### 142. Public Preview: Threat Detection in Azure Backup powered by MDC

**Published**: November 18, 2025 13:45:04 UTC
**Link**: [Public Preview: Threat Detection in Azure Backup powered by MDC](https://azure.microsoft.com/updates?id=520454)

**Update ID**: 520454
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Storage, Azure Backup

**Summary**:

- What was updated  
Azure Backup now includes threat detection capabilities for Azure VM backups, powered by Microsoft Defender for Cloud (MDC), currently in public preview.

- Key changes or new features  
This update enables continuous monitoring and assessment of Azure VM backup restore points (RPs) to detect malicious activity or anomalies that may indicate ransomware or other threats. It helps ensure the integrity and recoverability of backup data by alerting users to suspicious changes in backup snapshots. Integration with MDC provides centralized threat intelligence and security alerts related to backup data.

- Target audience affected  
Developers, IT professionals, and security teams responsible for managing Azure VM backups and disaster recovery strategies will benefit from enhanced security visibility and proactive threat detection within their backup environment.

- Important notes if any  
This feature is in public preview, so it should be used with caution in production environments. Users need to enable Microsoft Defender for Cloud and configure threat detection policies for Azure Backup to leverage this capability. Monitoring alerts and responding promptly can help prevent data loss from ransomware or other malicious attacks targeting backup data.  

For more details, visit: https://azure.microsoft.com/updates?id=520454

**Details**:

The recent Azure Backup update introduces a public preview feature for threat detection in Azure VM backups, powered by Microsoft Defender for Cloud (MDC), aimed at enhancing backup security by identifying malicious activities and potential compromises within backup restore points (RPs).

**Background and Purpose:**  
As ransomware and cyberattacks increasingly target backup data to prevent recovery, ensuring the integrity and security of backup restore points has become critical. Traditional backup solutions focus on data availability and recovery but often lack integrated threat detection capabilities. This update addresses that gap by embedding threat intelligence and anomaly detection directly into Azure Backup, enabling proactive security monitoring of VM backup data.

**Specific Features and Detailed Changes:**  
- **Threat Detection for Azure VM Backup RPs:** The feature scans backup restore points for signs of compromise, such as ransomware encryption, malware presence, or suspicious modifications.  
- **Integration with Microsoft Defender for Cloud:** Leveraging MDC’s advanced threat analytics, the system correlates backup data with broader security signals to improve detection accuracy.  
- **Health Assessment of Restore Points:** Customers receive alerts and security recommendations when suspicious activity is detected in their backup data, allowing timely investigation and remediation.  
- **Support for Azure VM Backups:** Initially focused on Azure VM backups, this capability extends protection beyond live workloads to their backup copies.

**Technical Mechanisms and Implementation Methods:**  
The threat detection operates by analyzing metadata and content patterns within backup restore points using MDC’s threat intelligence algorithms. It inspects file changes, encryption patterns, and behavioral anomalies indicative of ransomware or malware activity. The detection engine runs as part of the Azure Backup service backend, continuously monitoring new and existing restore points without impacting backup performance. Alerts and findings are surfaced through the Azure portal and integrated MDC dashboards, enabling centralized security management. The implementation relies on secure telemetry from backup storage and leverages Azure Security Center’s infrastructure for threat correlation and alerting.

**Use Cases and Application Scenarios:**  
- **Ransomware Protection:** Detect early signs of ransomware encryption in backup data to prevent restoring compromised backups.  
- **Compliance and Audit:** Provide evidence of backup integrity and security posture for regulatory requirements.  
- **Incident Response:** Quickly identify which restore points are safe to use during recovery operations.  
- **Security Operations Integration:** Feed backup threat alerts into SOC workflows for comprehensive threat management.

**Important Considerations and Limitations:**  
- Currently in public preview, the feature may have limited regional availability and evolving capabilities.  
- Detection is focused on Azure VM backups; other backup types (e.g., SQL, Files) are not yet supported.  
- False positives are possible; security teams should validate alerts before taking action.  
- Requires Microsoft Defender for Cloud enabled with appropriate licensing to access threat detection insights.  
- Data privacy and compliance implications should be reviewed, as backup data metadata is analyzed for threat signals.

**Integration with Related Azure Services:**  
- **Microsoft Defender for Cloud:** Core integration for threat analytics, alerting, and security recommendations.  
- **Azure Security Center:** Centralized dashboard for monitoring backup threat alerts alongside other security signals.  
- **Azure Monitor and Log Analytics:** Potential to route threat detection logs and alerts for custom monitoring and automation workflows.  
- **Azure Policy:** Can be used to enforce Defender for Cloud enablement and backup security configurations across subscriptions.

In summary, the introduction of threat detection in Azure Backup powered by Microsoft Defender for Cloud significantly enhances the security posture of Azure VM backups by enabling proactive identification of malicious activities within backup restore points, thereby supporting ransomware resilience and secure recovery strategies for IT professionals managing Azure environments.

---

### 143. Public Preview: Query-based metric alerts in Azure Monitor

**Published**: November 18, 2025 08:00:28 UTC
**Link**: [Public Preview: Query-based metric alerts in Azure Monitor](https://azure.microsoft.com/updates?id=518469)

**Update ID**: 518469
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Features

**Summary**:

- What was updated  
Azure Monitor metric alerts have been enhanced to support query-based metric alerts in public preview.

- Key changes or new features  
Metric alerts now support all Azure metrics, including platform metrics, Prometheus metrics, and custom metrics, providing comprehensive monitoring coverage. The update introduces powerful query capabilities using PromQL, enabling more flexible and granular alert conditions based on metric queries rather than static thresholds.

- Target audience affected  
Developers, DevOps engineers, and IT professionals responsible for monitoring and alerting in Azure environments, especially those leveraging Prometheus metrics or custom metrics for observability.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. The integration of PromQL query support allows for sophisticated alerting scenarios but may require familiarity with PromQL syntax. For full details and to get started, refer to the official Azure update link.

**Details**:

The recent Azure Monitor update introduces public preview support for query-based metric alerts, significantly enhancing the flexibility and scope of metric monitoring across Azure environments. Previously, Azure Monitor metric alerts primarily relied on predefined metric dimensions and static thresholds, limiting alerting capabilities to platform metrics and some custom metrics. This update addresses these limitations by enabling alerts based on complex queries over all Azure metrics, including platform metrics, Prometheus metrics, and custom metrics, thereby providing comprehensive observability and proactive incident management.

**Background and Purpose**  
Azure Monitor is a central service for collecting, analyzing, and acting on telemetry from cloud and on-premises environments. Traditional metric alerts were constrained to specific metrics and simple threshold conditions, which could be insufficient for complex monitoring scenarios, especially with the growing adoption of Prometheus metrics in Azure Kubernetes Service (AKS) and other containerized workloads. The update aims to unify metric alerting under a powerful query language, PromQL (Prometheus Query Language), enabling more granular and sophisticated alert conditions that reflect real-world operational complexities.

**Specific Features and Detailed Changes**  
- **Query-based Metric Alerts:** Users can now define alerts using PromQL queries, allowing for advanced filtering, aggregation, and mathematical operations on metrics data before triggering alerts.  
- **Support for All Azure Metrics:** This includes native platform metrics (e.g., CPU, memory), Prometheus metrics ingested via Azure Monitor Managed Prometheus, and custom metrics pushed via Azure Monitor APIs or Azure Metrics Advisor.  
- **Unified Alerting Experience:** The alert creation interface in Azure Monitor has been enhanced to support query-based conditions alongside traditional metric alert conditions.  
- **Improved Alert Logic:** Users can specify complex alert logic such as multiple query expressions combined with logical operators, enabling multi-dimensional alerting scenarios.  
- **Public Preview Availability:** This feature is currently in public preview, allowing users to experiment and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Monitor integrates with the Azure Managed Prometheus service, which stores and processes Prometheus metrics at scale. The query-based alerts leverage the PromQL engine to evaluate metric data in near real-time. When an alert rule is created, the query is executed periodically against the metric store, and the results are evaluated against user-defined thresholds or conditions. The alerting pipeline is designed to handle high cardinality and large volumes of metrics efficiently, ensuring timely detection of anomalies or threshold breaches.

**Use Cases and Application Scenarios**  
- **Kubernetes Monitoring:** Use PromQL queries to create alerts on complex container metrics such as pod restarts, CPU throttling, or custom application metrics exposed via Prometheus exporters.  
- **Multi-dimensional Alerting:** Create alerts that combine multiple metrics or dimensions, for example, alerting only when CPU usage exceeds a threshold on specific VM instances or resource groups.  
- **Custom Application Monitoring:** Define alerts on custom metrics emitted by applications, enabling proactive responses to business-specific KPIs or SLIs.  
- **Hybrid Environments:** Monitor both Azure platform metrics and Prometheus metrics from on-premises or multi-cloud environments in a unified alerting framework.

**Important Considerations and Limitations**  
- Being in public preview, query-based metric alerts may have limitations in SLA, regional availability, and feature completeness.  
- Users should validate query performance and cost implications, as complex PromQL queries may increase evaluation time and resource consumption.  
- Alert rule limits and quotas apply, and users should design queries to optimize for cardinality and evaluation frequency.  
- Integration with existing alert management and automation workflows may require adjustments to accommodate query-based alert payloads.

**Integration with Related Azure Services**  
- **Azure Monitor Managed Prometheus:** This service acts as the backend for storing and querying Prometheus metrics, tightly integrated with the new alerting capabilities.  
- **Azure Alerts and Action Groups:** Query-based alerts integrate seamlessly with Azure Alerts infrastructure, enabling notifications, automated remediation, and incident management via Action Groups

---


*This report was automatically generated - 2025-11-19 04:17:15 UTC*