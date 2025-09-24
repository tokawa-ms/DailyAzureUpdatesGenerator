# September 24, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 24, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Azure Site Recovery Support for Virtual Machines with Premium SSD v2 disks

**Published**: September 23, 2025 17:30:13 UTC
**Link**: [Generally Available: Azure Site Recovery Support for Virtual Machines with Premium SSD v2 disks](https://azure.microsoft.com/updates?id=502998)

**Update ID**: 502998
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery, Features, Management

**Summary**:

- What was updated  
Azure Site Recovery (ASR) now generally supports Virtual Machines (VMs) using Premium SSD v2 disks.

- Key changes or new features  
ASR’s disaster recovery capabilities have been extended to VMs with Premium SSD v2 managed disks, enabling seamless replication and failover across Azure regions and from on-premises environments to Azure. This update ensures improved performance and cost-efficiency for protected workloads leveraging the latest Premium SSD v2 storage tier.

- Target audience affected  
Developers and IT professionals managing disaster recovery and business continuity for Azure VMs, especially those utilizing Premium SSD v2 disks for high-performance storage needs.

- Important notes if any  
Organizations can now confidently include VMs with Premium SSD v2 disks in their disaster recovery plans without compatibility concerns. Ensure that your ASR configurations and replication policies are updated to leverage this support. For detailed implementation guidance, refer to the official Azure documentation.

**Details**:

The recent General Availability (GA) announcement of Azure Site Recovery (ASR) support for Virtual Machines (VMs) utilizing Premium SSD v2 disks marks a significant enhancement in Azure’s disaster recovery capabilities. This update enables seamless replication and failover of Azure VMs that leverage the latest generation of Premium SSD storage, Premium SSD v2, across Azure regions or from on-premises environments to Azure, thereby strengthening business continuity strategies for enterprises.

**Background and Purpose**  
Azure Site Recovery is a core Azure service designed to ensure business continuity by orchestrating replication, failover, and recovery of workloads in the event of planned or unplanned outages. Previously, ASR supported VMs with Premium SSD (v1) and other disk types, but support for Premium SSD v2 disks was in preview or unavailable. Premium SSD v2 disks offer improved performance scalability, lower latency, and cost efficiency compared to their predecessors, making them attractive for I/O-intensive workloads. The GA of ASR support for Premium SSD v2 disks addresses the growing demand for disaster recovery solutions that accommodate these high-performance storage options, enabling customers to protect modernized workloads without compromising on storage performance or cost.

**Specific Features and Detailed Changes**  
- **Support for Premium SSD v2 Disks:** ASR now fully supports replication and failover of VMs with Premium SSD v2 disks, including both OS and data disks.  
- **Seamless Integration:** The replication process respects the performance tiers and scalability characteristics of Premium SSD v2, ensuring that recovery VMs maintain comparable disk performance profiles.  
- **Cross-Region and On-Premises to Azure Replication:** Customers can replicate workloads using Premium SSD v2 disks across Azure regions or from on-premises VMware, Hyper-V, or physical servers to Azure, expanding disaster recovery options.  
- **Enhanced Monitoring and Reporting:** ASR’s monitoring tools and alerts now incorporate metrics and health status specific to Premium SSD v2 disk replication, aiding in proactive management.

**Technical Mechanisms and Implementation Methods**  
ASR leverages Azure’s replication engine to capture changes at the disk level and asynchronously replicate them to the recovery region or Azure environment. For Premium SSD v2 disks, ASR integrates with the Azure Storage subsystem to handle the disk’s variable performance tiers and dynamic scalability. The replication engine tracks write operations and synchronizes them while maintaining consistency for crash-consistent and application-consistent recovery points. During failover, ASR provisions VMs in the target region with Premium SSD v2 disks configured to match the source VM’s disk size and performance tier, ensuring minimal performance degradation post-failover.

**Use Cases and Application Scenarios**  
- **Disaster Recovery for Mission-Critical Applications:** Enterprises running latency-sensitive, I/O-intensive applications on Premium SSD v2 disks can now implement robust DR strategies using ASR without sacrificing disk performance.  
- **Hybrid Cloud DR:** Organizations with on-premises workloads using VMware or Hyper-V can replicate VMs with Premium SSD v2 disks to Azure, facilitating cloud-based DR and migration pathways.  
- **Cross-Region High Availability:** Businesses can maintain geographically dispersed recovery sites with consistent disk performance, supporting compliance and resilience requirements.

**Important Considerations and Limitations**  
- **Supported VM Sizes:** Ensure that the VM sizes in the recovery region support Premium SSD v2 disks and match the source VM’s configuration to avoid compatibility issues.  
- **Replication Latency:** While ASR provides near real-time replication, network bandwidth and latency can impact replication lag, which should be factored into Recovery Point Objective (RPO) planning.  
- **Cost Implications:** Premium SSD v2 disks have tiered pricing based on performance levels; replication and failover may incur additional costs depending on the selected tiers in the recovery region.  
- **Feature Parity:** Some advanced Premium SSD v2 features (e.g., ultra-performance tiers) may have specific constraints or may not be fully supported in all regions at

---

### 2. Retirement: NVv3-series Azure Virtual Machines will be retired on September 30 ,2026

**Published**: September 23, 2025 16:00:30 UTC
**Link**: [Retirement: NVv3-series Azure Virtual Machines will be retired on September 30 ,2026](https://azure.microsoft.com/updates?id=500573)

**Update ID**: 500573
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft Azure announced the retirement of NVv3-series virtual machines (VMs), specifically the Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3 models, effective September 30, 2026.

- Key changes or new features  
These NVv3-series VMs, which are GPU-optimized and commonly used for visualization, simulation, and AI workloads, will no longer be available after the retirement date. No direct replacement VMs were specified in the update, so users should plan migration strategies to newer VM series that support similar GPU capabilities.

- Target audience affected  
Developers and IT professionals who currently deploy or manage workloads on NVv3-series VMs, particularly those leveraging GPU acceleration for graphics-intensive or compute-heavy applications, will be impacted. This includes teams running AI, machine learning, rendering, or visualization workloads.

- Important notes if any  
Users should begin planning migration well in advance to avoid service disruption. It is recommended to evaluate alternative Azure VM series such as NVv4 or newer GPU-enabled VMs that offer improved performance and features. Review application compatibility and performance requirements before transitioning. For more details, consult the official Azure update link.

**Details**:

The Azure update announces the planned retirement of the NVv3-series virtual machines (VMs)—specifically Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3—effective September 30, 2026. This retirement reflects Microsoft’s ongoing efforts to optimize and modernize its VM offerings by phasing out older GPU-enabled VM sizes in favor of newer, more efficient, and cost-effective alternatives.

**Background and Purpose:**  
The NVv3-series VMs have been widely used for GPU-accelerated workloads such as visualization, simulation, and AI inferencing. However, with rapid advancements in GPU technology and Azure infrastructure, these VMs are becoming less efficient compared to newer generations that provide better performance, scalability, and cost benefits. The retirement aims to encourage customers to migrate to newer VM series that leverage updated GPU architectures and enhanced capabilities, ensuring improved workload performance and security compliance.

**Specific Features and Changes:**  
The NVv3-series VMs are based on NVIDIA Tesla M60 GPUs, offering GPU capabilities primarily for graphics-intensive applications and compute workloads. The retirement means these specific VM sizes will no longer be available for deployment or resizing after the cutoff date. Customers currently using these VMs must plan to migrate workloads to supported VM families such as the NVv4-series, which utilize AMD Radeon Instinct GPUs, or the newer ND-series optimized for AI and HPC workloads. These newer VMs provide better GPU performance, enhanced scalability, and support for the latest Azure features.

**Technical Mechanisms and Implementation:**  
The retirement process involves disabling the provisioning and resizing of the NVv3-series VMs in Azure’s backend infrastructure. Existing VMs will continue to function until the retirement date, but post-September 30, 2026, these VMs cannot be restarted if deallocated or newly created. Microsoft recommends customers to proactively migrate workloads by redeploying on supported VM sizes and updating any automation scripts, ARM templates, or infrastructure-as-code configurations that reference NVv3-series VMs. Migration may involve reconfiguring GPU drivers, validating application compatibility with newer GPU architectures, and performance tuning.

**Use Cases and Application Scenarios:**  
NVv3-series VMs have been commonly used for remote visualization (e.g., Windows Virtual Desktop with GPU acceleration), 3D rendering, video encoding, and AI inferencing tasks that require moderate GPU power. Post-retirement, workloads requiring GPU acceleration should transition to NVv4-series for graphics workloads or ND-series for deep learning and HPC scenarios. This ensures continued support for GPU-accelerated applications with improved performance and cost efficiency.

**Important Considerations and Limitations:**  
- Customers must plan migration well before the retirement date to avoid service disruption.  
- Some legacy applications may require testing and possible modification to ensure compatibility with newer GPU architectures.  
- Pricing and VM availability may differ in target regions for replacement VM sizes.  
- Backup and disaster recovery plans should be updated to reflect the new VM configurations.  
- Monitoring and alerting systems should be adjusted to track the new VM types.

**Integration with Related Azure Services:**  
The NVv3-series VMs integrate with services such as Azure Virtual Desktop, Azure Batch, and Azure Machine Learning for GPU-accelerated workloads. Post-retirement, these services will continue to support newer GPU VM families, offering enhanced integration with Azure Monitor, Azure Security Center, and Azure Policy for governance and compliance. Customers leveraging containerized GPU workloads via Azure Kubernetes Service (AKS) should also update node pools to supported VM sizes to maintain GPU support.

In summary, the retirement of NVv3-series VMs by September 30, 2026, requires IT professionals to proactively plan and execute migration strategies to newer GPU-enabled VM families within Azure, ensuring uninterrupted service, improved performance, and alignment with Azure’s evolving infrastructure capabilities.

---

### 3. Generally Available: GitHub Copilot app modernization capabilities for Java and .NET are now available

**Published**: September 23, 2025 15:00:40 UTC
**Link**: [Generally Available: GitHub Copilot app modernization capabilities for Java and .NET are now available](https://azure.microsoft.com/updates?id=503603)

**Update ID**: 503603
**Data source**: Azure Updates API

**Categories**: Launched, Features

**Summary**:

- What was updated  
GitHub Copilot’s app modernization capabilities for Java and .NET have reached general availability.

- Key changes or new features  
The update introduces AI-powered assistance specifically tailored to help developers modernize Java and .NET applications. This includes automated code suggestions and refactoring guidance that reduce repetitive and complex tasks involved in updating legacy codebases. The tool helps improve code quality, security, and scalability by enabling faster adoption of modern frameworks and best practices.

- Target audience affected  
Java and .NET developers focused on application modernization, as well as IT professionals overseeing enterprise app lifecycle management and modernization initiatives.

- Important notes if any  
This capability integrates seamlessly with existing developer workflows, allowing teams to accelerate modernization efforts without sacrificing innovation. Enterprises can leverage these AI-driven features to reduce technical debt and improve maintainability while focusing on delivering new business value. For more details, visit the official Azure update page.

**Details**:

The recent Azure update announces the general availability of GitHub Copilot app modernization capabilities specifically tailored for Java and .NET development environments. This enhancement aims to streamline and accelerate the modernization of legacy applications, a critical process for enterprises seeking to maintain security, scalability, and innovation in their software portfolios.

**Background and Purpose:**  
Application modernization is a strategic priority for many organizations to leverage cloud-native architectures, improve maintainability, and reduce technical debt. However, modernization efforts often involve repetitive, complex tasks such as refactoring code, updating dependencies, and adopting new frameworks or design patterns. The purpose of integrating GitHub Copilot’s AI-driven code assistance into app modernization workflows is to reduce manual effort, minimize errors, and enable developers to focus on higher-value innovation rather than boilerplate or migration code.

**Specific Features and Detailed Changes:**  
The update introduces AI-powered code suggestions and automated refactoring capabilities within GitHub Copilot that are optimized for Java and .NET applications. Key features include:  
- Intelligent code generation to convert legacy constructs into modern equivalents (e.g., migrating from older Java EE APIs to Jakarta EE or Spring Boot, or from .NET Framework to .NET Core/.NET 6+).  
- Automated recommendations for adopting cloud-native patterns such as microservices, containerization, and asynchronous programming models.  
- Context-aware code completions that understand existing codebases and suggest modernization steps inline within IDEs like Visual Studio and Visual Studio Code.  
- Support for updating dependencies and configuration files to align with modern frameworks and cloud environments.

**Technical Mechanisms and Implementation Methods:**  
GitHub Copilot leverages OpenAI’s Codex model, fine-tuned on extensive code repositories and modernization patterns specific to Java and .NET ecosystems. It integrates directly into developers’ IDEs via extensions, providing real-time AI-assisted code completions and refactoring suggestions. The modernization capabilities work by analyzing the existing code context, identifying legacy patterns, and proposing syntactically and semantically correct modern alternatives. Developers can accept, modify, or reject suggestions, maintaining control over the modernization process. The tool also supports batch modernization workflows by integrating with CI/CD pipelines to automate repetitive code transformations.

**Use Cases and Application Scenarios:**  
- Migrating monolithic Java EE applications to microservices architectures using Spring Boot or Quarkus.  
- Upgrading .NET Framework applications to .NET 6+ to leverage improved performance and cross-platform support.  
- Refactoring legacy synchronous code to asynchronous patterns to improve scalability.  
- Updating deprecated APIs and libraries to supported versions to enhance security and maintainability.  
- Assisting developers in cloud migration projects by generating infrastructure-as-code snippets and containerization scripts.

**Important Considerations and Limitations:**  
- While GitHub Copilot accelerates modernization, it does not replace the need for thorough testing, architectural review, and manual adjustments, especially for complex business logic.  
- AI-generated code should be reviewed carefully to ensure compliance with organizational coding standards and security policies.  
- The tool’s effectiveness depends on the quality and structure of the existing codebase; highly entangled or poorly documented legacy code may require additional manual intervention.  
- Licensing and data privacy considerations apply when using AI-assisted tools, particularly in regulated industries.

**Integration with Related Azure Services:**  
GitHub Copilot app modernization capabilities complement Azure’s broader modernization ecosystem. Developers can seamlessly integrate modernized applications with Azure services such as:  
- **Azure Kubernetes Service (AKS)** for container orchestration of microservices.  
- **Azure App Service** for hosting modern web applications with built-in scaling.  
- **Azure DevOps and GitHub Actions** for automated CI/CD pipelines incorporating modernization workflows.  
- **Azure Monitor and Application Insights** for observability of modernized applications.  
- **Azure Spring Apps** for managed Spring Boot application hosting.  
This synergy enables end-to-end modernization from code refactoring to deployment and monitoring in Azure’s cloud environment.

In summary, the general

---


*This report was automatically generated - 2025-09-24 03:01:59 UTC*