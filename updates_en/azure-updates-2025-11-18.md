# November 18, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 18, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 6 items

## Update List

### 1. Public Preview: Introducing SDK Stats to the Azure Monitor OpenTelemetry Distro

**Published**: November 17, 2025 20:00:46 UTC
**Link**: [Public Preview: Introducing SDK Stats to the Azure Monitor OpenTelemetry Distro](https://azure.microsoft.com/updates?id=529528)

**Update ID**: 529528
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Azure Monitor OpenTelemetry Distro now includes a Public Preview feature called SDK Stats, enabling enhanced observability into the Application Insights data collection pipeline.

- Key changes or new features  
SDK Stats provides detailed telemetry about the SDK’s internal operations, such as data ingestion, processing, and export metrics. This helps identify bottlenecks or failures within the telemetry pipeline, improving troubleshooting and performance tuning. The feature surfaces SDK-level metrics that were previously opaque, allowing better insight into how telemetry data flows from applications to Azure Monitor.

- Target audience affected  
Developers and IT professionals using Azure Monitor with OpenTelemetry SDKs for application monitoring and diagnostics will benefit from this update. It is particularly useful for those managing complex telemetry setups or troubleshooting data collection issues.

- Important notes if any  
This feature is currently in Public Preview, so users should evaluate it in non-production environments first. It complements existing monitoring capabilities but requires enabling within the OpenTelemetry SDK configuration. Feedback from the community during this preview phase will help refine the feature before general availability.  

For more details, visit: https://azure.microsoft.com/updates?id=529528

**Details**:

The recent Azure update titled "Public Preview: Introducing SDK Stats to the Azure Monitor OpenTelemetry Distro" enhances observability by integrating SDK-level telemetry into the Azure Monitor Application Insights data collection pipeline. This update addresses common customer challenges in diagnosing data ingestion and telemetry pipeline issues by providing granular insights into the SDK’s internal operations.

**Background and Purpose:**  
Azure Monitor Application Insights is widely used for collecting telemetry from applications, leveraging the OpenTelemetry standard for instrumentation. However, customers often encounter difficulties troubleshooting data loss, delays, or configuration issues within the telemetry pipeline, leading to support tickets. To improve transparency and ease diagnostics, Microsoft introduced SDK Stats within the Azure Monitor OpenTelemetry Distro. This feature aims to expose detailed telemetry about the SDK’s own performance and behavior, enabling users to monitor the health and efficiency of their telemetry collection processes.

**Specific Features and Detailed Changes:**  
The update introduces SDK Stats as a new telemetry category emitted by the Azure Monitor OpenTelemetry SDK. These stats include metrics such as telemetry item counts, dropped items, retry attempts, export durations, and internal queue sizes. By capturing these internal SDK metrics, users gain visibility into how well their telemetry data is being processed before it reaches Azure Monitor. The SDK Stats are automatically collected and sent alongside application telemetry without requiring manual instrumentation changes, simplifying adoption.

**Technical Mechanisms and Implementation Methods:**  
Under the hood, the Azure Monitor OpenTelemetry Distro now instruments its own telemetry pipeline components to generate SDK Stats. These stats are collected via internal counters and diagnostic events within the SDK’s telemetry pipeline. The SDK then exports these metrics as part of the standard telemetry stream to Application Insights, tagged distinctly to differentiate SDK-generated telemetry from application telemetry. This approach leverages OpenTelemetry’s extensibility for custom instrumentation and ensures minimal performance overhead. The feature is currently in public preview, allowing users to opt-in and provide feedback before general availability.

**Use Cases and Application Scenarios:**  
- **Troubleshooting Telemetry Pipeline Issues:** IT professionals can use SDK Stats to identify bottlenecks, dropped telemetry, or export failures within the SDK, enabling faster root cause analysis.  
- **Performance Monitoring:** By monitoring export durations and queue sizes, teams can optimize telemetry throughput and adjust SDK configurations accordingly.  
- **Reliability Engineering:** SDK Stats help ensure telemetry reliability by tracking retry attempts and failures, informing resilience improvements.  
- **Support and Diagnostics:** When engaging Microsoft support, customers can provide SDK Stats telemetry to facilitate deeper analysis.  

**Important Considerations and Limitations:**  
- As a public preview feature, SDK Stats may undergo changes before general availability and should be used with caution in production environments.  
- The additional telemetry data increases the volume of telemetry sent to Application Insights, which could impact costs and ingestion limits; users should monitor usage accordingly.  
- SDK Stats currently focus on the Azure Monitor OpenTelemetry Distro and may not cover all third-party or custom OpenTelemetry SDK implementations.  
- Proper tagging and filtering are necessary to separate SDK Stats from application telemetry in analysis and dashboards.  

**Integration with Related Azure Services:**  
SDK Stats telemetry integrates seamlessly with Azure Monitor Application Insights, allowing users to query and visualize SDK performance metrics using Kusto Query Language (KQL) in Azure Monitor Logs. This integration facilitates correlation between application telemetry and SDK health metrics. Additionally, SDK Stats can be combined with Azure Monitor Alerts to proactively notify teams about telemetry pipeline anomalies. The feature complements other Azure observability tools such as Azure Monitor Metrics and Azure Dashboards, providing a holistic view of application and telemetry pipeline health.

In summary, the introduction of SDK Stats in the Azure Monitor OpenTelemetry Distro public preview significantly enhances the observability of telemetry collection pipelines by providing detailed internal SDK metrics. This empowers IT professionals to diagnose, monitor, and optimize telemetry ingestion processes more effectively, improving overall reliability and supportability of Azure Monitor Application Insights deployments.

---

### 2. Generally Available: Visual Studio 2026

**Published**: November 17, 2025 18:45:44 UTC
**Link**: [Generally Available: Visual Studio 2026](https://azure.microsoft.com/updates?id=526900)

**Update ID**: 526900
**Data source**: Azure Updates API

**Categories**: Launched, Developer tools, Visual Studio

**Summary**:

- What was updated  
Microsoft has released Visual Studio 2026, the latest version of its integrated development environment (IDE).

- Key changes or new features  
Visual Studio 2026 introduces deep AI integration throughout the development workflow, prominently featuring GitHub Copilot for AI-assisted coding. It supports agentic workflows, enabling developers to automate complex tasks and improve productivity. The update focuses on enhancing developer efficiency by embedding AI-driven code suggestions, refactoring, and debugging tools directly into the IDE. Additionally, it offers improved collaboration features aligned with GitHub services, streamlining source control and team workflows.

- Target audience affected  
Professional developers, software engineers, and IT professionals involved in application development and DevOps processes will benefit from the enhanced AI capabilities and integrated GitHub tooling.

- Important notes if any  
Adopting Visual Studio 2026 may require updating existing development environments and workflows to leverage AI features fully. Organizations should evaluate compatibility with current projects and consider training to maximize productivity gains from the new AI-driven tools.

For more details, visit: https://azure.microsoft.com/updates?id=526900

**Details**:

The general availability of Visual Studio 2026 marks a significant milestone in the evolution of Microsoft’s integrated development environment (IDE), designed to enhance developer productivity through deep AI integration and modernized workflows. This update aims to address the increasing complexity of software development by embedding advanced AI capabilities directly into the IDE, thereby streamlining coding, debugging, and deployment processes for professional developers.

**Background and Purpose**  
Visual Studio has long been a cornerstone IDE for developers working across multiple languages and platforms. With the rapid advancement of AI technologies and the growing adoption of AI-assisted coding, Microsoft’s purpose with Visual Studio 2026 is to modernize the development experience by embedding AI as a core component rather than an add-on. This update reflects the industry trend toward intelligent development environments that reduce manual effort, improve code quality, and accelerate delivery cycles.

**Specific Features and Detailed Changes**  
Visual Studio 2026 introduces seamless integration with GitHub Copilot, an AI pair programmer powered by OpenAI’s Codex models, enabling context-aware code suggestions, completions, and even generation of entire functions or classes based on natural language prompts. Additionally, the IDE incorporates agentic workflows—AI-driven task automation agents that can autonomously perform multi-step development tasks such as code refactoring, testing, and deployment orchestration.

Other notable enhancements include:

- AI-assisted debugging that can predict potential runtime errors and suggest fixes before code execution.
- Intelligent code reviews powered by machine learning models that analyze pull requests for security vulnerabilities, performance issues, and adherence to best practices.
- Enhanced support for cloud-native development with integrated Azure DevOps pipelines and container orchestration tools.
- Improved collaboration features leveraging GitHub’s ecosystem for real-time code sharing and pair programming.

**Technical Mechanisms and Implementation Methods**  
The AI capabilities in Visual Studio 2026 are implemented through tight integration with cloud-based AI services hosted on Azure, leveraging scalable machine learning models and natural language processing APIs. GitHub Copilot operates by sending anonymized code context to Azure-hosted AI models, which return relevant code completions. Agentic workflows utilize Azure Logic Apps and Azure Functions under the hood to automate complex sequences of development tasks, triggered either manually or by specific code events.

The IDE architecture has been optimized to handle AI inference with minimal latency, employing local caching and asynchronous calls to cloud services to maintain responsiveness. Security and privacy are enforced through encrypted communication channels and strict data handling policies compliant with enterprise standards.

**Use Cases and Application Scenarios**  
Visual Studio 2026 is suited for a wide range of development scenarios, including:

- Enterprise software development teams seeking to improve code quality and reduce review cycles.
- Cloud-native application development with integrated Azure resource provisioning and CI/CD pipelines.
- Rapid prototyping and proof-of-concept projects where AI-generated code accelerates initial development.
- DevOps teams automating testing and deployment workflows using agentic AI agents.
- Educational environments where AI assistance helps new developers learn coding patterns and best practices.

**Important Considerations and Limitations**  
While AI integration offers significant productivity gains, users should be aware of potential limitations such as:

- AI-generated code may require careful review to avoid subtle bugs or security flaws.
- Dependence on cloud connectivity for AI features means offline development scenarios have reduced functionality.
- Privacy concerns around code data sent to AI services necessitate compliance checks, especially for proprietary or sensitive codebases.
- The learning curve associated with new AI-driven workflows and the need for team training.

**Integration with Related Azure Services**  
Visual Studio 2026 tightly integrates with multiple Azure services to provide a seamless development-to-deployment experience:

- Azure DevOps for source control, build pipelines, and release management.
- Azure AI services for hosting and scaling the underlying machine learning models powering Copilot and agentic workflows.
- Azure Functions and Logic Apps for implementing automated task agents within the IDE.
- Azure Kubernetes Service (AKS) and Azure Container Registry for containerized application development and deployment.
- Azure Monitor and

---

### 3. Generally Available: Seamless failback for HyperV-to-Azure: Managed Disk support in Azure Site Recovery 

**Published**: November 17, 2025 16:30:12 UTC
**Link**: [Generally Available: Seamless failback for HyperV-to-Azure: Managed Disk support in Azure Site Recovery ](https://azure.microsoft.com/updates?id=530092)

**Update ID**: 530092
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery

**Summary**:

- What was updated  
Azure Site Recovery (ASR) now supports seamless failback from Azure virtual machines (VMs) to on-premises Hyper-V environments when the original replication was to Azure storage accounts, and the failed-over Azure VM uses managed disks.

- Key changes or new features  
Previously, failback scenarios were limited when replication targeted Azure storage accounts and the Azure VM utilized managed disks. With this update, ASR enables failback without requiring complex manual steps or disk conversions, simplifying disaster recovery workflows. This enhancement ensures that VMs replicated from on-premises Hyper-V to Azure can be failed back smoothly, regardless of whether the Azure VM runs on managed disks.

- Target audience affected  
Developers and IT professionals managing disaster recovery and business continuity for Hyper-V workloads using Azure Site Recovery will benefit. This is especially relevant for organizations leveraging managed disks in Azure and requiring reliable failback capabilities to on-premises infrastructure.

- Important notes if any  
This feature is generally available, indicating production readiness. Users should review their replication configurations to ensure compatibility and test failback processes to validate seamless recovery. For detailed guidance, refer to the official Azure documentation linked in the update.

**Details**:

The recent Azure Site Recovery (ASR) update introduces general availability of seamless failback support from Azure virtual machines (VMs) to on-premises Hyper-V environments when the failed-over Azure VMs utilize managed disks, even if the original replication from on-premises to Azure was configured using storage accounts. This enhancement addresses a critical gap in disaster recovery workflows by enabling consistent and reliable bi-directional replication and failover scenarios involving Hyper-V and Azure managed disks.

**Background and Purpose**  
Azure Site Recovery is a disaster recovery solution that orchestrates replication, failover, and failback of workloads between on-premises environments and Azure. Traditionally, failback from Azure VMs to on-premises Hyper-V was limited or complex when the Azure VM was backed by managed disks, especially if the initial replication used storage accounts rather than managed disks. This limitation complicated recovery plans and extended downtime during failback operations. The update aims to simplify and streamline failback processes, ensuring business continuity and reducing operational overhead.

**Specific Features and Detailed Changes**  
- **Seamless Failback Support:** Enables failback from Azure VMs with managed disks to on-premises Hyper-V hosts, even if the initial replication used storage accounts.  
- **Managed Disk Compatibility:** Supports Azure managed disks during failback, allowing organizations to leverage managed disk benefits (such as scalability, performance, and simplified management) without losing failback capabilities.  
- **Unified Replication Handling:** Abstracts the underlying storage type differences between Azure managed disks and storage accounts, providing a transparent failback experience.  
- **General Availability (GA):** The feature is production-ready, supported, and fully documented for enterprise use.

**Technical Mechanisms and Implementation Methods**  
Azure Site Recovery orchestrates replication by capturing changes at the source Hyper-V VM and replicating them to Azure storage. Initially, replication to Azure could target either unmanaged disks (storage accounts) or managed disks. When a failover occurs, ASR creates an Azure VM from the replicated data. Failback involves replicating changes from the Azure VM back to the on-premises Hyper-V host.

With this update, ASR now supports converting the managed disk-backed Azure VM’s data into a format compatible with Hyper-V during failback. The process involves:  
- Capturing incremental changes on the Azure managed disk.  
- Translating and synchronizing these changes back to the on-premises Hyper-V storage infrastructure.  
- Ensuring consistency and integrity of the VM’s disk state during the failback synchronization.  
- Automating the failback orchestration to minimize manual intervention.

This is achieved through enhancements in the ASR replication engine and integration with Azure managed disk APIs, enabling efficient data transfer and disk format compatibility.

**Use Cases and Application Scenarios**  
- **Disaster Recovery for Hyper-V Workloads:** Enterprises running critical Hyper-V workloads can replicate to Azure for DR and confidently fail back to their on-premises environment after resolving issues.  
- **Hybrid Cloud Operations:** Organizations leveraging hybrid cloud architectures benefit from flexible workload mobility between on-premises Hyper-V and Azure managed disk-backed VMs.  
- **Testing and Maintenance:** IT teams can failover to Azure for testing or maintenance and then fail back seamlessly without reconfiguring storage or replication settings.  
- **Cost Optimization:** Enables temporary cloud failover during on-premises infrastructure upgrades or outages, with smooth return to local infrastructure.

**Important Considerations and Limitations**  
- **Supported Configurations:** This feature specifically applies to Hyper-V to Azure replication scenarios where failback is required; other hypervisors or replication topologies may not be supported.  
- **Network and Bandwidth:** Failback operations require sufficient network bandwidth and connectivity between Azure and on-premises environments to synchronize data efficiently.  
- **Downtime and Recovery Point Objective (RPO):** While failback is seamless, some downtime may occur during final synchronization; RPO and Recovery Time Objective (RTO) should be planned

---

### 4. Public Preview: Support for Linux major OS upgrades with Azure Site Recovery

**Published**: November 17, 2025 16:30:12 UTC
**Link**: [Public Preview: Support for Linux major OS upgrades with Azure Site Recovery](https://azure.microsoft.com/updates?id=530087)

**Update ID**: 530087
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Site Recovery

**Summary**:

- What was updated  
Azure Site Recovery now supports major Linux OS version upgrades during replication without disruption.

- Key changes or new features  
Developers and IT professionals can perform in-place major version upgrades on supported Linux distributions—specifically Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES)—while Azure Site Recovery continues to replicate without disabling protection or losing recovery points. For example, upgrading from RHEL 8 to RHEL 9 is now supported seamlessly. This enhancement reduces downtime and operational complexity during planned OS upgrades.

- Target audience affected  
IT administrators, cloud architects, and developers managing disaster recovery and business continuity for Linux workloads on Azure, particularly those using Azure Site Recovery for replication and failover.

- Important notes if any  
This feature is currently in public preview. Users should validate upgrade paths and test in non-production environments before applying in production. Supported distributions are limited to RHEL and SLES at this time. Refer to official Azure documentation for detailed upgrade procedures and compatibility considerations.  

Link: https://azure.microsoft.com/updates?id=530087

**Details**:

The recent Azure update introduces public preview support for performing major Linux OS version upgrades on protected virtual machines (VMs) using Azure Site Recovery (ASR) without disabling replication, interrupting data synchronization, or losing existing recovery points. This enhancement currently supports Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES), enabling seamless in-place upgrades such as migrating from RHEL 8 to RHEL 9 while maintaining business continuity and disaster recovery readiness.

**Background and Purpose:**  
Traditionally, major OS upgrades on protected Linux VMs required temporarily disabling ASR replication to avoid inconsistencies or data loss, which introduced downtime and increased operational complexity. This update addresses these challenges by allowing continuous replication during major OS version upgrades, thereby reducing planned downtime and simplifying maintenance workflows for enterprise environments relying on ASR for disaster recovery.

**Specific Features and Detailed Changes:**  
- Support for major Linux OS version upgrades on RHEL and SLES distributions without disabling ASR replication.  
- Preservation of existing recovery points during the upgrade process, ensuring rollback options remain intact.  
- Continuous replication and synchronization of changes during the upgrade, minimizing data loss risk.  
- Support for in-place upgrades, such as RHEL 8 to RHEL 9 and SLES 15 SP2 to SP3, aligning with supported upgrade paths from the respective OS vendors.

**Technical Mechanisms and Implementation Methods:**  
Azure Site Recovery achieves this by enhancing its replication engine to handle the state changes and file system modifications introduced during major OS upgrades. The replication process now intelligently tracks and synchronizes changes at the block level, even as system files and kernel components are updated. ASR coordinates with the guest OS upgrade process to maintain replication consistency, leveraging integration with the Linux OS upgrade tools and lifecycle management commands. This ensures that replication checkpoints and recovery points remain valid and consistent throughout the upgrade.

**Use Cases and Application Scenarios:**  
- Enterprises running critical Linux workloads on Azure VMs that require major OS version upgrades without incurring downtime or risking data loss.  
- Organizations with strict disaster recovery SLAs that cannot afford replication interruptions during maintenance windows.  
- DevOps teams automating OS lifecycle management while maintaining continuous disaster recovery readiness.  
- Scenarios involving compliance-driven environments where maintaining recovery points and audit trails during upgrades is mandatory.

**Important Considerations and Limitations:**  
- Currently, this feature is in public preview and limited to RHEL and SLES distributions; other Linux distributions are not yet supported.  
- Supported upgrade paths must align with vendor-recommended in-place upgrade procedures to ensure compatibility.  
- It is recommended to validate upgrade plans in test environments before production deployment to verify replication behavior.  
- Certain custom kernel modules or third-party drivers may affect upgrade success and replication consistency.  
- Users should monitor replication health and recovery point status closely during the upgrade process.

**Integration with Related Azure Services:**  
- Azure Monitor and Azure Log Analytics can be used to track replication health and OS upgrade events for proactive issue detection.  
- Integration with Azure Automation and Azure DevOps pipelines enables orchestration of upgrade workflows alongside replication status checks.  
- Azure Backup can complement ASR by providing additional data protection layers during the upgrade lifecycle.  
- Azure Security Center can help assess security posture before and after OS upgrades to ensure compliance.

In summary, this update significantly enhances Azure Site Recovery’s capabilities by enabling uninterrupted major Linux OS version upgrades on RHEL and SLES VMs, preserving recovery points and continuous replication. This reduces operational complexity and downtime, supporting enterprise-grade disaster recovery strategies during critical system maintenance. Technical professionals should plan upgrades carefully, validate supported scenarios, and leverage Azure monitoring and automation tools to maximize the benefits of this new functionality.

---

### 5. Public Preview: Support 5x churn in Azure Site Recovery 

**Published**: November 17, 2025 16:30:12 UTC
**Link**: [Public Preview: Support 5x churn in Azure Site Recovery ](https://azure.microsoft.com/updates?id=530078)

**Update ID**: 530078
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Site Recovery

**Summary**:

- What was updated  
Azure Site Recovery now supports up to 5x churn, enabling replication speeds of up to 500 MB/s per VM.

- Key changes or new features  
This update significantly increases the data throughput capacity for VM replication, allowing Azure Site Recovery to handle high IOPS workloads more efficiently. It enhances disaster recovery capabilities for demanding applications by supporting faster and more reliable data replication.

- Target audience affected  
Developers and IT professionals managing disaster recovery and business continuity for performance-intensive workloads on Azure VMs will benefit from this improvement.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in test environments before production deployment. The increased throughput helps ensure minimal downtime and data loss for critical applications requiring high replication performance.

For more details, visit: https://azure.microsoft.com/updates?id=530078

**Details**:

The recent Azure Site Recovery (ASR) update introduces public preview support for up to 5x churn, enabling replication throughput of 500 MB/s per virtual machine (VM). This enhancement significantly boosts ASR’s capability to handle high Input/Output Operations Per Second (IOPS) workloads, addressing the increasing demand for resilient disaster recovery solutions in environments running performance-intensive applications.

**Background and Purpose:**  
Azure Site Recovery is a critical disaster recovery (DR) service that orchestrates replication, failover, and recovery of workloads across on-premises, Azure, and other cloud environments. Traditionally, ASR’s replication throughput per VM was limited, constraining its suitability for high-performance workloads such as large databases, transactional systems, and analytics platforms. This update aims to remove those bottlenecks by increasing the maximum allowed churn rate, thus enabling customers to protect demanding applications without compromising on replication speed or recovery point objectives (RPOs).

**Specific Features and Detailed Changes:**  
The key feature of this update is the increase in supported churn rate by 5 times, now allowing up to 500 MB/s per VM. Churn refers to the volume of data changes that ASR can replicate continuously. By supporting higher churn, ASR can replicate more frequent and larger data changes, which is essential for workloads with high write intensity. This enhancement is currently in public preview, allowing customers to test and validate the improved throughput before general availability.

**Technical Mechanisms and Implementation Methods:**  
ASR achieves this increased throughput by optimizing its data replication pipeline, including improvements in compression, network utilization, and parallel data processing. The update likely involves enhancements to the ASR Mobility Service agent installed on VMs, which captures and transfers changed blocks more efficiently. Additionally, Azure’s backend infrastructure, including storage and networking components, has been tuned to handle the increased data flow without impacting stability or latency. Customers may need to ensure their network bandwidth and Azure subscription limits align with the higher throughput to fully leverage this capability.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for enterprises running mission-critical, high-transactional applications such as SQL Server, SAP HANA, Oracle databases, and real-time analytics platforms. Organizations with stringent RPO and Recovery Time Objective (RTO) requirements can now confidently replicate these workloads to Azure, knowing that ASR can keep pace with data changes. It also supports scenarios involving large-scale migrations or hybrid cloud architectures where minimizing downtime and data loss is paramount.

**Important Considerations and Limitations:**  
While the increased churn support is a significant improvement, it is currently in public preview, which means it may not yet be fully supported for all workload types or regions. Customers should conduct thorough testing in non-production environments to validate performance and stability. Network bandwidth and VM sizing must be adequate to handle the increased replication load. Additionally, higher churn rates may increase storage consumption and costs due to more frequent data transfers and snapshots. Monitoring and alerting should be configured to track replication health and performance metrics closely.

**Integration with Related Azure Services:**  
This enhancement integrates seamlessly with Azure Monitor and Azure Automation, enabling improved observability and automated management of disaster recovery workflows. It complements Azure Backup by providing a comprehensive data protection strategy. Furthermore, it aligns with Azure Networking improvements such as ExpressRoute and Azure Virtual WAN, which can be leveraged to optimize replication traffic. Customers using Azure SQL or Azure Database services can combine ASR’s enhanced replication with native database replication features for layered resilience.

In summary, the public preview of 5x churn support in Azure Site Recovery represents a substantial advancement for disaster recovery of high-IOPS workloads, enabling faster, more reliable replication and recovery for demanding enterprise applications while requiring careful planning around network and resource capacity.

---

### 6. Generally Available: Capacity guidance for Azure Site Recovery

**Published**: November 17, 2025 16:30:12 UTC
**Link**: [Generally Available: Capacity guidance for Azure Site Recovery](https://azure.microsoft.com/updates?id=530073)

**Update ID**: 530073
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery

**Summary**:

- What was updated  
Azure Site Recovery (ASR) now provides capacity guidance by recommending alternative VM sizes during failover scenarios when the originally targeted VM size has limited allocation availability due to capacity constraints.

- Key changes or new features  
The update introduces intelligent VM size recommendations to improve failover success rates. When the preferred VM size is unavailable in the target region or availability zone, ASR suggests alternative VM sizes that meet the workload requirements. This helps ensure disaster recovery plans execute smoothly without manual intervention or delays caused by capacity shortages.

- Target audience affected  
This update primarily benefits IT professionals and developers responsible for disaster recovery planning and execution using Azure Site Recovery. It is especially relevant for organizations with strict RTO (Recovery Time Objective) requirements and those operating in regions with variable VM capacity availability.

- Important notes if any  
Users should review and validate the recommended alternative VM sizes to ensure compatibility with their applications and licensing. This feature enhances resilience but does not replace the need for thorough DR testing and planning. The guidance is available during failover operations and aims to minimize failover failures due to capacity limitations.

For more details, visit: https://azure.microsoft.com/updates?id=530073

**Details**:

The recent Generally Available update for Azure Site Recovery (ASR) introduces capacity guidance by recommending alternative VM sizes during failover operations when the originally targeted VM size faces allocation constraints in the target region. This enhancement addresses capacity availability challenges inherent in disaster recovery scenarios, ensuring more reliable and flexible failover execution.

**Background and Purpose**  
Azure Site Recovery is a critical disaster recovery service that orchestrates replication, failover, and recovery of virtual machines (VMs) to maintain business continuity. One operational challenge arises when the target Azure region or availability zone has limited capacity for the specific VM size configured for failover, potentially causing failover delays or failures. This update aims to mitigate such risks by proactively suggesting alternative VM sizes that are available in the target region, thereby improving failover success rates and reducing recovery time objectives (RTO).

**Specific Features and Detailed Changes**  
- **Alternative VM Size Recommendations:** During the failover planning or execution phase, ASR now evaluates the capacity availability of the configured target VM size. If capacity is constrained, ASR provides a list of alternative VM sizes that meet or exceed the original VM’s compute, memory, and storage requirements.  
- **Automated Guidance:** The recommendations are integrated into the ASR portal and failover workflows, allowing administrators to select or automatically apply alternative sizes without manual capacity checks.  
- **Capacity Awareness:** The feature leverages real-time capacity data from Azure’s infrastructure to ensure the suggested VM sizes are currently allocatable in the target region or availability zone.

**Technical Mechanisms and Implementation Methods**  
The implementation relies on Azure’s internal capacity telemetry and VM SKU availability APIs. When a failover is initiated, ASR queries these APIs to assess the availability of the target VM size SKU. If insufficient capacity is detected, ASR cross-references a catalog of VM sizes with similar or better performance characteristics and filters those available in the target location. This process is embedded within the ASR failover orchestration engine, ensuring seamless integration without requiring additional user intervention. The system also respects the original VM’s configuration constraints, such as disk size, network interfaces, and performance tiers, to maintain workload compatibility.

**Use Cases and Application Scenarios**  
- **Disaster Recovery in Capacity-Constrained Regions:** Enterprises with critical workloads replicated to regions with fluctuating capacity can rely on ASR’s guidance to avoid failover failures due to VM size unavailability.  
- **Planned Failovers and DR Drills:** During scheduled failovers or testing, administrators can pre-validate alternative VM sizes to ensure smooth execution.  
- **Multi-Region Replication Strategies:** Organizations employing multi-region replication can leverage this feature to dynamically adapt to regional capacity variations without manual intervention.

**Important Considerations and Limitations**  
- **Performance and Cost Implications:** Alternative VM sizes may differ in cost and performance characteristics; administrators should evaluate the trade-offs before accepting recommendations.  
- **Compatibility Checks:** While ASR attempts to match VM capabilities, some workloads may have specific hardware or software dependencies that require manual validation.  
- **Regional SKU Availability Variability:** The feature depends on accurate and up-to-date capacity data; sudden changes in regional capacity might still impact failover outcomes.  
- **Not a Guarantee of Allocation:** Recommendations improve the likelihood of successful allocation but do not guarantee it under extreme capacity constraints.

**Integration with Related Azure Services**  
- **Azure Compute and VM SKU APIs:** The feature integrates closely with Azure Compute services to query VM size availability and capacity telemetry.  
- **Azure Monitor and Capacity Insights:** It may leverage monitoring data to assess capacity trends, aiding in proactive failover planning.  
- **Azure Automation and Runbooks:** Organizations can integrate alternative VM size recommendations into automated DR runbooks for streamlined failover processes.  
- **Azure Policy and Governance:** Policies can be configured to restrict or allow certain VM sizes during failover, complementing the recommendation engine.

In summary, the capacity guidance feature in Azure Site Recovery enhances

---


*This report was automatically generated - 2025-11-18 03:04:16 UTC*