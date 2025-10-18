# October 18, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 18, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Private Preview: New planned datacenter region in Malaysia (Southeast Asia 3)

**Published**: October 17, 2025 15:15:35 UTC
**Link**: [Private Preview: New planned datacenter region in Malaysia (Southeast Asia 3)](https://azure.microsoft.com/updates?id=513752)

**Update ID**: 513752
**Data source**: Azure Updates API

**Categories**: In development, Hybrid + multicloud, Compute, Azure Modular Datacenter, Cloud Services, Regions & Datacenters

**Summary**:

- What was updated  
Microsoft announced a private preview for a new planned Azure datacenter region, Southeast Asia 3, located in Malaysia.

- Key changes or new features  
The new region will expand Azure’s digital infrastructure in Southeast Asia, offering Microsoft’s most comprehensive and strategic cloud services. This includes core Azure services designed to enhance performance, availability, and compliance for customers in Malaysia and nearby markets.

- Target audience affected  
Developers and IT professionals operating in Southeast Asia, particularly those with workloads requiring low latency, data residency, and compliance within Malaysia. Enterprises planning regional expansion or disaster recovery strategies will also benefit.

- Important notes if any  
The Southeast Asia 3 region is currently in private preview, so access is limited. Organizations interested in early access or more information should engage with Microsoft representatives. This expansion underscores Microsoft’s commitment to regional cloud growth and data sovereignty compliance in Malaysia.

**Details**:

Microsoft has announced a private preview of a new planned Azure datacenter region, Southeast Asia 3, located in Malaysia, marking a strategic expansion of its cloud infrastructure in the Southeast Asia market. This update reflects Microsoft’s ongoing commitment to meet growing regional demand for cloud services by providing enhanced data residency, improved latency, and compliance with local regulations.

**Background and Purpose**  
The Southeast Asia region, encompassing countries like Singapore, Malaysia, Indonesia, and the Philippines, has seen rapid digital transformation and cloud adoption. Existing Azure regions such as Southeast Asia (Singapore) have served the market well but face capacity and latency constraints as demand grows. The introduction of Southeast Asia 3 in Malaysia aims to alleviate these constraints by providing additional capacity and localized infrastructure. It also addresses data sovereignty requirements by enabling customers to keep data within Malaysian jurisdiction, which is critical for industries such as government, finance, healthcare, and telecommunications.

**Specific Features and Detailed Changes**  
The Southeast Asia 3 region will offer Microsoft’s full portfolio of cloud services, including but not limited to:  
- Compute (Azure Virtual Machines, Azure Kubernetes Service)  
- Storage (Blob, Files, Disks)  
- Networking (Virtual Network, ExpressRoute, Azure Firewall)  
- Databases (Azure SQL Database, Cosmos DB)  
- AI and Analytics services  
- Identity and Security services (Azure Active Directory, Azure Security Center)  

As a new region, it will be built with Microsoft’s latest datacenter technologies, including energy-efficient hardware, advanced cooling systems, and robust physical and cyber security measures. The region will integrate with Azure’s global backbone network to ensure high availability and disaster recovery capabilities.

**Technical Mechanisms and Implementation Methods**  
The new region will be implemented as a standard Azure region with multiple availability zones to ensure fault tolerance and high availability. It will support Azure Resource Manager (ARM) for infrastructure as code deployments and integrate seamlessly with Azure’s global management and monitoring tools such as Azure Monitor and Azure Policy. Customers can deploy resources in Southeast Asia 3 using the Azure portal, CLI, PowerShell, or APIs once the region becomes generally available. The private preview phase allows select customers to test workloads and provide feedback on performance, compliance, and feature support.

**Use Cases and Application Scenarios**  
- **Data Residency and Compliance:** Organizations subject to Malaysian data protection laws can store and process data locally.  
- **Latency-Sensitive Applications:** Applications serving Malaysian users, such as e-commerce platforms, gaming, and media streaming, will benefit from reduced network latency.  
- **Disaster Recovery and Business Continuity:** Southeast Asia 3 can serve as a secondary region for geo-redundancy for workloads running in other Southeast Asian regions.  
- **Government and Regulated Industries:** Enables deployment of sensitive workloads with compliance to local regulations and certifications.  
- **Hybrid Cloud Scenarios:** Integration with on-premises environments in Malaysia via ExpressRoute or VPN for hybrid deployments.

**Important Considerations and Limitations**  
- As the region is currently in private preview, access is limited and requires Microsoft approval.  
- Not all Azure services may be immediately available in the preview phase; service availability will expand over time.  
- Pricing and SLAs for the new region will be published upon general availability.  
- Customers should evaluate network connectivity options and latency benchmarks during the preview.  
- Migration strategies should consider data transfer costs and potential downtime during cutover.

**Integration with Related Azure Services**  
Southeast Asia 3 will be fully integrated with Azure’s global ecosystem, supporting:  
- Azure Arc for hybrid and multi-cloud resource management.  
- Azure Security Center and Sentinel for unified security management and threat detection.  
- Azure DevOps and GitHub Actions for CI/CD pipelines targeting the new region.  
- Azure Policy and Blueprints for governance and compliance enforcement.  
- Azure Cost Management for budgeting and cost optimization in the new region.

In summary, the planned Southeast Asia 3 Azure region

---

### 2. Generally Available: New OS SKU enum to migrate to Azure Linux 3.0 

**Published**: October 17, 2025 15:15:35 UTC
**Link**: [Generally Available: New OS SKU enum to migrate to Azure Linux 3.0 ](https://azure.microsoft.com/updates?id=512396)

**Update ID**: 512396
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now supports a new OS SKU enum, ‘AzureLinux3’, enabling migration to Azure Linux 3.0 for Kubernetes versions 1.28 through 1.36.

- Key changes or new features  
The introduction of the ‘AzureLinux3’ SKU allows decoupling of the underlying OS upgrades from Kubernetes version upgrades. This provides greater flexibility and control over OS lifecycle management. Customers running LTS Kubernetes versions 1.28 to 1.31 can adopt this new OS SKU to benefit from improved stability and update cadence.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those responsible for OS and Kubernetes version upgrades, will benefit from this update. It is particularly relevant for teams prioritizing stability and controlled upgrade processes in production environments.

- Important notes if any  
Migration to Azure Linux 3.0 requires specifying the new OS SKU enum ‘AzureLinux3’ during cluster or node pool creation or upgrade. This change is available starting with Kubernetes version 1.28 and supports up to 1.36. Users should plan their upgrade strategy accordingly to leverage the decoupled OS and Kubernetes upgrade model.

Reference: https://azure.microsoft.com/updates?id=512396

**Details**:

The recent Azure update introduces a new OS SKU enumeration, ‘AzureLinux3’, enabling migration to Azure Linux 3.0 for Kubernetes clusters running versions 1.28 through 1.36. This enhancement is designed to improve operating system lifecycle management by decoupling OS upgrades from Kubernetes version upgrades, thereby granting IT professionals greater flexibility and control over their cluster maintenance processes.

**Background and Purpose:**  
Historically, Azure Kubernetes Service (AKS) node operating system upgrades have been closely tied to Kubernetes version upgrades, which can complicate maintenance schedules and increase operational risk. The introduction of the ‘AzureLinux3’ SKU addresses this by allowing customers to independently upgrade the underlying OS to Azure Linux 3.0 without mandating a simultaneous Kubernetes version upgrade. This separation aligns with best practices for minimizing downtime and reducing upgrade complexity in production environments.

**Specific Features and Detailed Changes:**  
- **New OS SKU Enum ‘AzureLinux3’:** This SKU represents nodes running Azure Linux 3.0, a modernized OS image optimized for AKS workloads.  
- **Supported Kubernetes Versions:** The feature supports Kubernetes versions from 1.28 through 1.36, including the Long-Term Support (LTS) versions 1.28 to 1.31, ensuring broad applicability for current and near-future clusters.  
- **Decoupled Upgrades:** Operators can now perform OS upgrades independently of Kubernetes upgrades, allowing for more granular control over patching and security updates.  
- **Improved Stability and Security:** Azure Linux 3.0 includes updated kernel versions, security patches, and performance enhancements tailored for containerized workloads.

**Technical Mechanisms and Implementation Methods:**  
Migration to the ‘AzureLinux3’ SKU involves specifying the new OS SKU during node pool creation or upgrade operations within AKS. The upgrade process leverages Azure’s managed node pool infrastructure, which orchestrates rolling upgrades to minimize downtime. The decoupling is implemented by separating the OS image versioning from the Kubernetes versioning metadata, enabling independent lifecycle management. Under the hood, Azure Linux 3.0 nodes run a hardened Linux kernel with optimized container runtime support, ensuring compatibility and performance with Kubernetes workloads.

**Use Cases and Application Scenarios:**  
- **Security Compliance:** Organizations requiring timely OS security patches without waiting for Kubernetes version upgrades can benefit from this decoupled upgrade path.  
- **Operational Flexibility:** Teams managing multiple AKS clusters with varying Kubernetes versions can standardize on Azure Linux 3.0 for consistent OS baseline without forced Kubernetes upgrades.  
- **Long-Term Support Environments:** Customers using LTS Kubernetes versions can maintain OS currency and stability, extending cluster lifecycle and reducing upgrade complexity.

**Important Considerations and Limitations:**  
- **Version Compatibility:** While the feature supports Kubernetes 1.28 to 1.36, clusters running versions outside this range cannot leverage the ‘AzureLinux3’ SKU.  
- **Upgrade Strategy:** Operators must plan node pool upgrades carefully to avoid disruption, as OS upgrades still involve node reimaging and rolling restarts.  
- **Testing:** It is recommended to validate workloads on Azure Linux 3.0 in staging environments before production migration to identify any compatibility issues.  
- **Feature Availability:** This SKU is currently available for AKS managed node pools and may not be supported in custom or self-managed Kubernetes environments.

**Integration with Related Azure Services:**  
- **Azure Kubernetes Service (AKS):** The primary integration point, with enhanced node pool management capabilities.  
- **Azure Monitor and Azure Security Center:** Benefit from improved OS telemetry and security posture management due to updated OS features.  
- **Azure Policy:** Can be used to enforce compliance and upgrade policies related to node OS versions.  
- **Azure Automation and Azure DevOps:** Facilitate automated upgrade workflows leveraging the new SKU for continuous delivery pipelines.

In summary, the introduction of the ‘AzureLinux3’ OS SKU in AKS allows IT professionals to

---

### 3. Generally Available: Azure Functions support for Python 3.13 

**Published**: October 17, 2025 15:00:03 UTC
**Link**: [Generally Available: Azure Functions support for Python 3.13 ](https://azure.microsoft.com/updates?id=512374)

**Update ID**: 512374
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions now supports Python 3.13 for local development and deployment.

- Key changes or new features  
Developers can build and run Azure Functions using Python 3.13, enabling access to the latest language features and improvements. Additionally, a new opt-in runtime version control feature has been introduced starting with Python 3.13. This allows developers to specify and lock the Functions Python runtime version, improving consistency and reducing runtime compatibility issues across environments.

- Target audience affected  
Python developers building serverless applications on Azure Functions and IT professionals managing Azure Functions deployments.

- Important notes if any  
The runtime version control is an opt-in feature, so developers must explicitly enable it to target specific Python runtime versions. This update helps ensure smoother upgrades and better control over function runtime behavior in production environments.

For more details, visit: https://azure.microsoft.com/updates?id=512374

**Details**:

The recent Azure Functions update announces general availability of Python 3.13 support, enabling developers to build and deploy serverless functions using the latest Python runtime, along with the introduction of runtime version control for Python functions.

**Background and Purpose:**  
Azure Functions is a serverless compute service that allows developers to run event-driven code without managing infrastructure. Python has been a popular language choice for Azure Functions due to its simplicity and extensive ecosystem. With Python 3.13 officially supported, Microsoft aims to provide developers access to the latest Python language features, performance improvements, and security updates, ensuring modern and efficient function development. Additionally, the introduction of runtime version control addresses the need for greater stability and compatibility by allowing developers to specify and lock the Functions Python runtime version their code targets.

**Specific Features and Detailed Changes:**  
- **Python 3.13 Runtime Support:** Developers can now author Azure Functions locally using Python 3.13, test them, and deploy directly to Azure Functions without compatibility issues. This includes support for new language syntax, standard library enhancements, and performance optimizations introduced in Python 3.13.  
- **Runtime Version Control (Opt-in):** This new feature allows developers to opt-in to specify the exact Functions Python runtime version their function app uses. This granular control helps mitigate risks from automatic runtime upgrades that might introduce breaking changes, thus improving deployment predictability and stability.  
- **Local Development and Tooling:** Updated Azure Functions Core Tools and Azure Functions extensions for VS Code and other IDEs now support Python 3.13, enabling seamless local development, debugging, and deployment workflows.

**Technical Mechanisms and Implementation:**  
Azure Functions runtime for Python is built on top of a managed Python environment hosted in Azure App Service infrastructure. With this update, the underlying Python environment has been upgraded to 3.13. The runtime version control feature works by allowing function apps to specify a runtime version in their configuration (e.g., in `host.json` or app settings), which the Azure Functions platform respects during function execution and deployment. This decouples the function app from the platform’s default runtime version, enabling side-by-side runtime versions and smoother upgrade paths.

**Use Cases and Application Scenarios:**  
- **Modern Python Applications:** Developers leveraging new Python 3.13 features such as enhanced error handling, improved typing, or new standard library modules can now deploy these directly in serverless functions.  
- **Stable Production Environments:** Organizations requiring strict runtime version control for compliance, testing, or stability reasons can lock their function apps to a specific Python runtime version, reducing unexpected runtime changes.  
- **Rapid Development and Prototyping:** Local development with Python 3.13 support accelerates iteration cycles, allowing developers to test new language features before deploying to production.  
- **Event-Driven Architectures:** Python 3.13 functions can be triggered by various Azure services such as Event Grid, Service Bus, HTTP requests, or Timer triggers, enabling flexible serverless workflows.

**Important Considerations and Limitations:**  
- **Opt-in Runtime Version Control:** Runtime version control is not enabled by default; developers must explicitly configure it to benefit from version pinning.  
- **Dependency Compatibility:** While Python 3.13 is supported, some third-party Python packages may not yet be fully compatible with 3.13, requiring validation before deployment.  
- **Platform Updates:** Although runtime version control mitigates breaking changes, underlying platform updates (e.g., Azure Functions host updates) may still affect function behavior and should be monitored.  
- **Regional Availability:** Python 3.13 support and runtime version control features are generally available but may have phased regional rollouts; verify availability in your Azure region.

**Integration with Related Azure Services:**  
- **Azure Functions Core Tools:** Updated tooling supports Python 3.13 for local development and deployment.  
- **Azure DevOps and GitHub Actions:** CI/CD pipelines can now target Python

---


*This report was automatically generated - 2025-10-18 03:02:14 UTC*