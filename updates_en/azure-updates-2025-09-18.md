# September 18, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 18, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: Azure Functions .NET 10 support 

**Published**: September 17, 2025 17:15:04 UTC
**Link**: [Public Preview: Azure Functions .NET 10 support ](https://azure.microsoft.com/updates?id=503134)

**Update ID**: 503134
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions now supports .NET 10 in Public Preview.

- Key changes or new features  
Developers can target .NET 10 by updating their Functions project’s target framework and upgrading the Microsoft.Azure.Functions.Worker.Sdk package to version 2.0.5 or later. This enables building and deploying Azure Functions using the latest .NET 10 runtime, benefiting from its performance improvements and new language features.

- Target audience affected  
Developers building serverless applications with Azure Functions, and IT professionals managing Azure Functions deployments who want to leverage the latest .NET runtime capabilities.

- Important notes if any  
This support is currently in Public Preview, so it should be used with caution in production environments. Ensure all dependencies are compatible with .NET 10 and test thoroughly before deployment. Deployment workflows remain unchanged, supporting standard Azure Functions app deployment processes.  

For more details, visit: https://azure.microsoft.com/updates?id=503134

**Details**:

The recent Azure Functions update introduces public preview support for .NET 10, enabling developers to build and deploy serverless applications using the latest .NET runtime. This enhancement aligns Azure Functions with the evolving .NET ecosystem, providing improved performance, new language features, and long-term support benefits inherent to .NET 10.

**Background and Purpose:**  
Azure Functions is a serverless compute service that allows developers to run event-driven code without managing infrastructure. Historically, Azure Functions supported multiple .NET versions, but with the release of .NET 10, Microsoft aims to ensure that serverless workloads can leverage the latest runtime improvements, security patches, and language enhancements. This update facilitates modernization of existing functions and encourages adoption of the newest .NET capabilities within serverless architectures.

**Specific Features and Detailed Changes:**  
- **.NET 10 Target Framework Support:** Developers can now set their Azure Functions projects to target `net10.0`, enabling use of .NET 10 APIs and language features.  
- **Updated SDK Version:** The update requires upgrading the `Microsoft.Azure.Functions.Worker.Sdk` package to version 2.0.5 or later, which includes necessary tooling and runtime support for .NET 10.  
- **Deployment Compatibility:** Functions targeting .NET 10 can be deployed to Azure Functions apps configured to run on the new runtime, ensuring seamless integration with Azure’s serverless infrastructure.

**Technical Mechanisms and Implementation Methods:**  
To adopt .NET 10 in Azure Functions:  
1. Modify the project file (`.csproj`) to change the `<TargetFramework>` element to `net10.0`.  
2. Update the `Microsoft.Azure.Functions.Worker.Sdk` package reference to version 2.0.5 or newer via NuGet.  
3. Rebuild the project to ensure compatibility and resolve any API changes or deprecations introduced in .NET 10.  
4. Deploy the function app to Azure, ensuring the Azure Functions runtime environment supports .NET 10 (this is managed by Azure during the public preview phase).  

The underlying Azure Functions runtime leverages the .NET 10 runtime environment, allowing functions to execute with the latest runtime optimizations, garbage collection improvements, and enhanced security features.

**Use Cases and Application Scenarios:**  
- **Modernizing Legacy Functions:** Existing Azure Functions projects can be upgraded to .NET 10 to benefit from improved performance and new language constructs such as enhanced pattern matching, record structs, and improved async streams.  
- **High-Performance Serverless APIs:** Developers building APIs or microservices using Azure Functions can utilize .NET 10’s runtime enhancements to reduce cold start times and improve throughput.  
- **Cloud-Native Applications:** Applications requiring long-term support and compatibility with the latest .NET ecosystem tools and libraries can adopt this update to future-proof their serverless components.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads due to potential instability or incomplete feature support.  
- **Runtime Availability:** Ensure the Azure Functions host environment supports .NET 10; this may require selecting specific runtime stacks or regions where the preview is enabled.  
- **Dependency Compatibility:** Third-party libraries and NuGet packages used within functions must be compatible with .NET 10 to avoid runtime errors.  
- **Breaking Changes:** Developers should review .NET 10 breaking changes to identify any necessary code modifications.

**Integration with Related Azure Services:**  
Azure Functions running on .NET 10 can seamlessly integrate with other Azure services such as:  
- **Azure Event Grid and Azure Service Bus:** For event-driven triggers and messaging.  
- **Azure Cosmos DB and Azure Storage:** For data persistence and state management.  
- **Azure Application Insights:** For monitoring and telemetry, which supports .NET 10-based functions without additional configuration.  
- **Azure DevOps and GitHub Actions:** For CI

---

### 2. Generally Available: Introducing the new Network Security Hub experience

**Published**: September 17, 2025 16:30:45 UTC
**Link**: [Generally Available: Introducing the new Network Security Hub experience](https://azure.microsoft.com/updates?id=503617)

**Update ID**: 503617
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure DDoS Protection, Azure Firewall, Azure Firewall Manager, Web Application Firewall, Services, Features

**Summary**:

- What was updated  
The Azure Firewall Manager experience has been expanded and rebranded as the Network Security Hub.

- Key changes or new features  
The Network Security Hub provides a centralized management interface that consolidates Azure Firewall, Web Application Firewall (WAF), and DDoS Protection. This unified experience simplifies the deployment, configuration, and monitoring of network security services across Azure environments. It enhances visibility and control by bringing these critical security components into a single pane of glass, improving operational efficiency and security posture management.

- Target audience affected  
Developers, network security engineers, and IT professionals responsible for managing Azure network security services will benefit from this update. Organizations leveraging Azure Firewall, WAF, and DDoS Protection can streamline their security operations using the new hub.

- Important notes if any  
This update is generally available, signaling full production readiness. Users should plan to transition to the Network Security Hub interface to take advantage of the integrated capabilities and improved management experience. Existing Azure Firewall Manager users will find the new hub familiar but more comprehensive.

**Details**:

The recent Azure update announces the general availability of the Network Security Hub, an evolution and rebranding of the Azure Firewall Manager experience, designed to provide a unified and centralized management interface for network security services including Azure Firewall, Web Application Firewall (WAF), and DDoS Protection.

**Background and Purpose**  
Traditionally, Azure Firewall Manager served as a centralized management tool primarily for Azure Firewall policies and deployments. However, as organizations increasingly adopt layered security strategies, managing disparate security controls such as WAF and DDoS Protection alongside firewall policies became operationally complex. The Network Security Hub addresses this by consolidating these critical network security services into a single pane of glass. This enhancement aims to simplify security posture management, improve visibility, and streamline policy enforcement across Azure environments.

**Specific Features and Detailed Changes**  
- **Unified Interface:** The Network Security Hub integrates Azure Firewall, WAF (including Application Gateway WAF and Azure Front Door WAF), and DDoS Protection management into one dashboard, enabling centralized monitoring and configuration.  
- **Policy Management:** Users can create, assign, and manage security policies across multiple subscriptions and resource groups, supporting large-scale enterprise deployments.  
- **Security Posture Insights:** The hub provides enhanced visibility into the security posture of network resources, including threat analytics and compliance status.  
- **Simplified Onboarding:** The experience guides users through onboarding and configuration of network security controls, reducing setup complexity.  
- **Cross-Service Coordination:** It facilitates coordinated policy enforcement and incident response across firewall rules, WAF policies, and DDoS mitigation settings.

**Technical Mechanisms and Implementation Methods**  
The Network Security Hub is implemented as a centralized Azure portal experience that leverages Azure Resource Manager (ARM) APIs to aggregate and manage policies and configurations across multiple security services. It uses role-based access control (RBAC) to ensure secure delegation of management privileges. Under the hood, it orchestrates policy deployment by interacting with the respective service control planes: Azure Firewall Manager for firewall rules, WAF policy APIs for application gateway and front door, and DDoS Protection plans for attack mitigation settings. The hub supports policy inheritance and overrides, enabling hierarchical policy management aligned with organizational structures.

**Use Cases and Application Scenarios**  
- **Enterprise Security Operations:** Large organizations managing multiple subscriptions can use the hub to enforce consistent network security policies and monitor threats across all workloads.  
- **Multi-Region Deployments:** Centralized management simplifies security configuration for applications deployed across multiple Azure regions.  
- **Compliance and Governance:** Security teams can leverage the hub’s insights and policy controls to maintain compliance with regulatory standards by ensuring all network security controls are properly configured and active.  
- **Incident Response:** Coordinated visibility into firewall, WAF, and DDoS alerts enables faster detection and remediation of security incidents.

**Important Considerations and Limitations**  
- The Network Security Hub currently supports integration with Azure Firewall, WAF (Application Gateway and Front Door), and DDoS Protection but does not yet include other network security services such as Network Security Groups (NSGs) or third-party firewall solutions.  
- Role assignments and permissions must be carefully managed to prevent unauthorized policy changes.  
- Some advanced configurations may still require direct interaction with individual service portals or APIs until fully integrated into the hub experience.  
- Organizations should assess the impact of centralized policy enforcement on existing decentralized security management workflows.

**Integration with Related Azure Services**  
The Network Security Hub tightly integrates with Azure Firewall Manager, Azure Application Gateway, Azure Front Door, and Azure DDoS Protection plans. It complements Azure Security Center (Microsoft Defender for Cloud) by providing focused network security management, while Defender for Cloud continues to offer broader threat detection and security posture management. The hub also works with Azure Policy for governance and compliance automation, enabling policy-as-code deployment models.

In summary, the Network Security Hub represents a strategic enhancement to Azure’s network security management capabilities by consolidating firewall, WAF, and

---

### 3. Public Preview: Databricks One in Azure Databricks 

**Published**: September 17, 2025 16:30:45 UTC
**Link**: [Public Preview: Databricks One in Azure Databricks ](https://azure.microsoft.com/updates?id=503408)

**Update ID**: 503408
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks introduced Databricks One in public preview, a unified platform that consolidates data engineering, analytics, and AI development workflows.

- Key changes or new features  
Databricks One offers a simplified, integrated experience combining collaborative workflows with enterprise-grade governance and performance optimizations. It enables teams to work seamlessly across data pipelines, analytics, and machine learning projects within a single environment. The platform emphasizes streamlined management, security, and compliance suitable for enterprise needs.

- Target audience affected  
Data engineers, data scientists, AI developers, and IT professionals managing data platforms in Azure Databricks will benefit from this update. Organizations seeking to unify their data and AI workflows under governed, scalable infrastructure are the primary users.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Enterprises should monitor governance and compliance capabilities as they integrate Databricks One into their workflows. Further enhancements and updates are expected as the preview progresses.

For more details, visit: https://azure.microsoft.com/updates?id=503408

**Details**:

The Azure update titled "Public Preview: Databricks One in Azure Databricks" introduces a unified platform designed to streamline data engineering, analytics, and AI development workflows within a single, governed environment. This update addresses the growing complexity faced by enterprises managing disparate tools and processes for data and AI projects, aiming to enhance collaboration, governance, and performance in Azure Databricks.

**Background and Purpose**  
Enterprises increasingly rely on data-driven insights and AI to drive business value, but often face challenges due to fragmented toolchains and governance gaps. Traditional workflows separate data engineering, analytics, and AI development, leading to inefficiencies and security risks. Databricks One is introduced to consolidate these workflows into one integrated platform, simplifying management and accelerating time-to-insight while ensuring compliance and governance at scale.

**Specific Features and Detailed Changes**  
Databricks One delivers a unified workspace that integrates data engineering pipelines, analytics dashboards, and AI model development tools. Key features include:  
- **Collaborative Workflows:** Enables data engineers, data scientists, and analysts to work together seamlessly using shared notebooks, version control, and real-time collaboration.  
- **Enterprise-grade Governance:** Incorporates fine-grained access controls, audit logging, and compliance policies to meet organizational and regulatory requirements.  
- **Performance Optimization:** Provides optimized compute resource management and workload orchestration to improve job execution times and cost efficiency.  
- **Simplified User Experience:** Offers a consistent UI and API surface that reduces context switching and accelerates development cycles.

**Technical Mechanisms and Implementation Methods**  
Databricks One leverages the underlying Azure Databricks architecture, built on Apache Spark, and extends it with enhanced governance layers and collaborative features. It integrates with Azure Active Directory for identity and access management, enabling role-based access controls (RBAC) and single sign-on (SSO). The platform supports Git integration for version control and CI/CD pipelines, facilitating DevOps practices. Performance improvements are achieved through adaptive query execution and autoscaling clusters managed by the Databricks Runtime engine.

**Use Cases and Application Scenarios**  
- **End-to-End Data Pipelines:** Data engineers can build, test, and deploy ETL/ELT pipelines collaboratively with data scientists who develop machine learning models using the same platform.  
- **Cross-Functional Analytics:** Business analysts can directly access governed datasets and create dashboards without needing to switch tools or request data extracts.  
- **AI Model Lifecycle Management:** Teams can manage the entire AI lifecycle from data preparation to model training, validation, and deployment within a single environment.  
- **Regulated Industries:** Organizations in finance, healthcare, and government can enforce strict governance policies while enabling innovation with AI and analytics.

**Important Considerations and Limitations**  
As this update is currently in public preview, users should be aware that some features may still be evolving and subject to change. Integration with certain third-party tools or legacy systems may require additional configuration. Performance gains depend on workload characteristics and cluster configurations. Governance capabilities require careful planning to align with organizational policies. Users should also monitor cost implications of unified compute resources and autoscaling features.

**Integration with Related Azure Services**  
Databricks One tightly integrates with Azure services such as:  
- **Azure Data Lake Storage Gen2:** For scalable, secure data storage accessible within Databricks notebooks and pipelines.  
- **Azure Synapse Analytics:** Enables hybrid analytics scenarios combining Databricks’ data engineering with Synapse’s data warehousing.  
- **Azure Machine Learning:** Supports model training and deployment workflows integrated with Databricks compute.  
- **Azure Monitor and Azure Security Center:** For monitoring, logging, and security compliance across Databricks workloads.  
- **Azure DevOps and GitHub:** For source control and CI/CD pipeline integration supporting collaborative development and deployment.

In summary, the Databricks One public preview in Azure Databricks offers a comprehensive, governed platform that unifies data engineering, analytics,

---

### 4. Generally Available: Confidential computing for Azure Database for PostgreSQL flexible server 

**Published**: September 17, 2025 15:45:39 UTC
**Link**: [Generally Available: Confidential computing for Azure Database for PostgreSQL flexible server ](https://azure.microsoft.com/updates?id=500795)

**Update ID**: 500795
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL flexible server now generally supports confidential computing.

- Key changes or new features  
This update enables data encryption within hardware-based Trusted Execution Environments (TEEs), ensuring that data remains encrypted not only at rest and in transit but also during processing. Confidential computing protects sensitive workloads by isolating data in secure enclaves, mitigating risks from compromised cloud infrastructure or privileged users. Developers and IT professionals can now deploy PostgreSQL flexible servers with enhanced security guarantees, suitable for highly regulated industries or sensitive data scenarios.

- Target audience affected  
Database administrators, developers building data-intensive applications, security architects, and IT professionals managing PostgreSQL workloads in Azure who require advanced data protection and compliance.

- Important notes if any  
Confidential computing support is available for Azure Database for PostgreSQL flexible server in supported regions. Users should verify compatibility with their existing applications and consider potential performance impacts due to enclave processing. This feature complements existing encryption and security controls, providing a comprehensive data protection strategy in Azure.

**Details**:

The recent general availability of Confidential Computing for Azure Database for PostgreSQL flexible server introduces hardware-based trusted execution environments (TEEs) to protect data in use, significantly enhancing data security by enabling encryption during processing within the database engine. This update addresses the critical need for stronger data protection in cloud environments, particularly for sensitive workloads subject to stringent compliance and privacy requirements.

**Background and Purpose**  
Traditional data security measures primarily focus on data at rest and in transit, leaving data vulnerable when actively processed in memory. Confidential Computing fills this gap by encrypting data during computation, ensuring that data remains protected even from cloud infrastructure administrators or malicious software. By integrating Confidential Computing with Azure Database for PostgreSQL flexible server, Microsoft aims to provide customers with a higher trust boundary for their database workloads, enabling secure processing of sensitive information in multi-tenant cloud environments.

**Specific Features and Detailed Changes**  
This update enables PostgreSQL flexible servers to run within hardware-based TEEs, such as Intel SGX or AMD SEV, depending on the underlying infrastructure. Key features include:  
- Transparent encryption of data in use within the database engine, without requiring application changes.  
- Isolation of cryptographic keys and sensitive data inside the enclave, inaccessible to the host OS or hypervisor.  
- Integration with Azure Key Vault for secure key management and attestation.  
- Support for common PostgreSQL workloads with minimal performance overhead due to optimized enclave operations.  

**Technical Mechanisms and Implementation Methods**  
Confidential Computing leverages TEEs that create isolated execution environments within the CPU, protecting code and data from unauthorized access or modification. When a PostgreSQL flexible server instance is provisioned with confidential computing enabled, the database engine runs inside the enclave. Data is decrypted only within this enclave, and all computations occur in this protected memory region. Azure Key Vault attestation services verify the integrity of the enclave before releasing cryptographic keys, ensuring that keys are only accessible to trusted code. This process involves:  
- Secure bootstrapping of the enclave environment.  
- Remote attestation to verify enclave identity and integrity.  
- Secure key provisioning from Azure Key Vault.  
- Encrypted data processing within the enclave memory.  

**Use Cases and Application Scenarios**  
Confidential Computing for PostgreSQL flexible server is particularly valuable for:  
- Financial services handling personally identifiable information (PII) or payment data requiring compliance with regulations like GDPR, PCI-DSS, or HIPAA.  
- Healthcare applications processing sensitive patient data.  
- Multi-tenant SaaS providers needing to isolate customer data even from cloud administrators.  
- Government and defense workloads demanding high assurance of data confidentiality during processing.  

**Important Considerations and Limitations**  
- Performance overhead: While optimized, enclave operations may introduce latency; benchmarking is recommended for latency-sensitive applications.  
- Feature parity: Some PostgreSQL extensions or features may not be fully supported within the enclave environment.  
- Regional availability: Confidential Computing-enabled flexible servers may initially be available in select Azure regions.  
- Key management: Proper configuration of Azure Key Vault and attestation policies is critical for secure operation.  
- Backup and restore processes should be reviewed to ensure data remains protected throughout the lifecycle.  

**Integration with Related Azure Services**  
This update integrates closely with:  
- **Azure Key Vault**: For secure storage and management of encryption keys and attestation policies.  
- **Azure Attestation Service**: To verify the integrity of the confidential computing environment before key release.  
- **Azure Monitor and Azure Security Center**: For monitoring the health, performance, and security posture of confidential computing instances.  
- **Azure Policy**: To enforce governance around the deployment of confidential computing-enabled PostgreSQL servers.  

In summary, the general availability of Confidential Computing for Azure Database for PostgreSQL flexible server provides a robust, hardware-enforced security boundary that protects data during processing, complementing existing encryption at rest and in transit. This capability empowers organizations to meet stringent compliance demands and

---


*This report was automatically generated - 2025-09-18 03:02:31 UTC*