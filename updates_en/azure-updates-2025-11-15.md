# November 15, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 15, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Retirement: Support for Python 3.10 ends on October 1st, 2026

**Published**: November 14, 2025 21:15:14 UTC
**Link**: [Retirement: Support for Python 3.10 ends on October 1st, 2026](https://azure.microsoft.com/updates?id=509686)

**Update ID**: 509686
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of support for Python 3.10 on Azure App Service, effective October 1, 2026.

- Key changes or new features  
After this date, extended support for Python 3.10 will end. While existing applications running on App Service with Python 3.10 will continue to operate, Microsoft will no longer provide security updates or customer support for this runtime version.

- Target audience affected  
Developers and IT professionals who deploy and maintain Python applications on Azure App Service using Python 3.10 are directly impacted. This includes teams responsible for application security, maintenance, and compliance.

- Important notes if any  
It is recommended to plan migration to a supported Python version before the cutoff date to ensure continued security updates and support. Running unsupported Python versions may expose applications to security vulnerabilities and lack of assistance from Microsoft support. For more details, refer to the official Azure update page.

**Details**:

The Azure update announces the retirement of extended support for Python 3.10 on Azure App Service effective October 1, 2026. This means that after this date, while existing applications running Python 3.10 will continue to operate on App Service, Microsoft will cease providing security updates and customer support specifically for Python 3.10 environments.

**Background and Purpose:**  
Python 3.10, released in October 2021, introduced numerous language enhancements but, like all software, has a defined lifecycle. Azure App Service aligns its runtime support lifecycle with Python’s own support policies to ensure customers run secure, stable, and performant applications. The retirement reflects the natural progression toward newer Python versions that receive active maintenance, security patches, and feature improvements. This update informs IT professionals to plan migration strategies to supported Python versions before the cutoff date to maintain compliance and security.

**Specific Features and Detailed Changes:**  
- Official extended support for Python 3.10 on Azure App Service ends on October 1, 2026.  
- Post this date, no further security patches or updates will be issued for Python 3.10 runtime images on App Service.  
- Customer support related to Python 3.10 runtime issues will no longer be available.  
- Applications currently running Python 3.10 will continue to function but without guaranteed security or support.  
- Azure encourages migration to newer Python versions (e.g., Python 3.11 or later) which will continue to receive updates and support.

**Technical Mechanisms and Implementation Methods:**  
Azure App Service provides managed runtime stacks, including Python, through containerized environments or platform-managed runtimes. The retirement means that the underlying Python 3.10 runtime images will no longer be updated or patched by Microsoft. Customers relying on the built-in Python 3.10 runtime should plan to:  
- Test application compatibility with newer Python versions.  
- Update their application dependencies and codebase to support the newer Python runtime.  
- Redeploy applications using updated runtime stacks provided by Azure App Service.  
- Alternatively, use custom container images with a supported Python version to maintain control over runtime updates.

**Use Cases and Application Scenarios:**  
- Web applications, APIs, and backend services hosted on Azure App Service using Python 3.10.  
- DevOps pipelines and CI/CD workflows that deploy Python 3.10-based applications.  
- Enterprises maintaining legacy Python applications that have yet to upgrade from Python 3.10.  
- Customers using Azure App Service for rapid development and deployment of Python apps who must plan for runtime upgrades.

**Important Considerations and Limitations:**  
- Running Python 3.10 applications post-retirement exposes environments to unpatched security vulnerabilities.  
- Lack of official support means troubleshooting runtime-specific issues may require internal expertise or third-party support.  
- Migration efforts may involve code refactoring, dependency upgrades, and regression testing.  
- Some third-party libraries may have varying support for newer Python versions, requiring compatibility verification.  
- Customers should review Azure App Service runtime deprecation schedules regularly to align their upgrade plans.

**Integration with Related Azure Services:**  
- Azure DevOps and GitHub Actions workflows deploying Python apps should update build and deployment pipelines to target supported Python versions.  
- Azure Monitor and Application Insights can be used to track application performance and errors during and after migration.  
- Azure Security Center can help identify security risks associated with running deprecated runtimes.  
- Azure Container Registry and Azure Kubernetes Service (AKS) provide alternative hosting options using custom containers with updated Python versions.  
- Azure Functions users should also review Python runtime support timelines as they may differ from App Service.

In summary, the retirement of Python 3.10 support on Azure App Service by October 1, 2026, requires IT professionals to proactively plan and execute migration to supported Python versions to ensure continued security, supportability, and compliance of their Python-based applications running on Azure.

---

### 2. Retirement: Windows Server 2022 on Azure Kubernetes Service enabled by Azure Arc

**Published**: November 14, 2025 18:00:13 UTC
**Link**: [Retirement: Windows Server 2022 on Azure Kubernetes Service enabled by Azure Arc](https://azure.microsoft.com/updates?id=499906)

**Update ID**: 499906
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Windows Server 2022 on Azure Kubernetes Service (AKS) enabled by Azure Arc, effective October 2026.

- Key changes or new features  
This update is a deprecation notice rather than a feature update. After October 2026, Windows Server 2022 workloads running on AKS clusters managed via Azure Arc will no longer be supported. Customers will need to plan migration or upgrade strategies ahead of this date.

- Target audience affected  
Developers and IT professionals using Azure Arc to manage Windows Server 2022 containers on AKS clusters, particularly those leveraging hybrid or multicloud Kubernetes deployments.

- Important notes if any  
Users should begin assessing their current deployments to ensure continuity beyond the retirement date. Consider migrating workloads to supported Windows Server versions or alternative container hosting solutions within AKS or Azure Arc. Microsoft recommends reviewing the lifecycle and support policies to align with this change and avoid service disruptions.

**Details**:

The announced retirement of Windows Server 2022 on Azure Kubernetes Service (AKS) enabled by Azure Arc, effective October 2026, signals the planned end of support and availability for this specific deployment model, allowing organizations to plan migrations and updates accordingly.

**Background and Purpose**  
Azure Arc extends Azure management and governance capabilities to on-premises, multi-cloud, and edge environments, enabling Azure services such as AKS to run outside Azure datacenters. Windows Server 2022 on AKS via Azure Arc was introduced to allow containerized Windows workloads to run in Kubernetes clusters managed through Azure Arc, providing hybrid cloud flexibility. The retirement announcement reflects evolving customer usage patterns, platform optimizations, and a strategic focus on alternative solutions for Windows container orchestration.

**Specific Features and Detailed Changes**  
This retirement means that after October 2026, Microsoft will no longer provide updates, patches, or support for Windows Server 2022 container workloads running on AKS clusters managed through Azure Arc. The underlying Azure Arc-enabled Kubernetes infrastructure will continue to support Linux-based workloads, but the Windows Server 2022 container images and related integration specific to this scenario will be deprecated. Customers will need to transition to supported alternatives before the retirement date.

**Technical Mechanisms and Implementation Methods**  
Azure Arc-enabled AKS allows Kubernetes clusters running outside Azure to be connected and managed through Azure, enabling deployment of Azure Kubernetes workloads on-premises or in other clouds. Windows Server containers require Windows nodes in the Kubernetes cluster, which Azure Arc facilitated by enabling Windows Server 2022 nodes to join the Arc-enabled Kubernetes cluster. The retirement implies that this Windows node integration and associated container image support will no longer be maintained. Technically, this affects the lifecycle management of Windows container nodes, Azure Arc agents on Windows nodes, and the compatibility of Windows container images with AKS on Arc.

**Use Cases and Application Scenarios**  
Typical use cases included hybrid applications requiring Windows container workloads managed centrally via Azure, such as legacy .NET Framework applications containerized for Kubernetes, or edge scenarios where Windows Server workloads needed to run close to data sources but managed via Azure. Organizations using Azure Arc to unify management of Windows containerized workloads across environments will need to evaluate migration paths, such as moving workloads to native AKS in Azure, Azure Stack HCI with Kubernetes, or alternative container orchestration platforms supporting Windows containers.

**Important Considerations and Limitations**  
- Customers must plan migration well before October 2026 to avoid disruption.  
- Windows container workloads on Arc-enabled AKS will not receive security updates or feature improvements post-retirement.  
- Compatibility with existing CI/CD pipelines and monitoring tools integrated via Azure Arc may require adjustment.  
- Linux container workloads on Arc-enabled AKS remain supported, so mixed OS cluster strategies should be reviewed.  
- Evaluate the impact on compliance and security policies relying on Azure Arc management for Windows workloads.

**Integration with Related Azure Services**  
Azure Arc integrates with Azure Monitor, Azure Policy, and Azure Security Center to provide unified governance and observability. The retirement affects Windows container nodes managed through these services in Arc-enabled AKS clusters. Customers leveraging Azure DevOps or GitHub Actions for CI/CD pipelines deploying Windows containers via Azure Arc will need to update deployment targets. Additionally, integration with Azure Active Directory for identity and access management on Windows container nodes may require reassessment. Alternative Azure services such as Azure Kubernetes Service (AKS) in Azure, Azure Stack HCI with Kubernetes support, or Azure Container Apps may provide supported paths forward for Windows container workloads.

In summary, the October 2026 retirement of Windows Server 2022 on Azure Kubernetes Service enabled by Azure Arc marks the end of support for this hybrid Windows container orchestration model, necessitating proactive migration planning and evaluation of alternative Azure and hybrid container solutions to maintain secure, supported Windows container deployments.

---

### 3. Public Preview: Pod CIDR expansion in Azure CNI Overlay for AKS

**Published**: November 14, 2025 16:30:37 UTC
**Link**: [Public Preview: Pod CIDR expansion in Azure CNI Overlay for AKS](https://azure.microsoft.com/updates?id=523086)

**Update ID**: 523086
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now supports Pod CIDR expansion in Azure CNI Overlay mode, available in public preview.

- Key changes or new features  
This update enables dynamic expansion of Pod CIDR ranges for AKS clusters using the Azure CNI Overlay network plugin. It addresses limitations in scaling Kubernetes workloads by allowing clusters to increase their pod IP address capacity without needing to recreate or extensively reconfigure the cluster. This facilitates better handling of large-scale and dynamic workloads by providing more flexible IP address management.

- Target audience affected  
Developers and IT professionals managing AKS clusters with Azure CNI Overlay networking, especially those running large or rapidly scaling Kubernetes workloads, will benefit from this feature.

- Important notes if any  
As this feature is in public preview, it should be used with caution in production environments. Users should review the documentation for any limitations or prerequisites before enabling Pod CIDR expansion. This feature currently applies only to clusters configured with Azure CNI Overlay, not other networking modes.  

For more details, visit: https://azure.microsoft.com/updates?id=523086

**Details**:

The recent public preview release of Pod CIDR expansion in the Azure CNI Overlay for Azure Kubernetes Service (AKS) addresses critical scalability challenges faced by dynamic and large-scale Kubernetes workloads by enabling clusters to expand their Pod IP address ranges without requiring cluster recreation or node pool replacement. Traditionally, AKS clusters configured with Azure CNI Overlay had a fixed Pod CIDR assigned at cluster creation, limiting the maximum number of Pods per node and overall cluster size. This update introduces the capability to dynamically increase the Pod CIDR range, thereby allowing more Pods to be scheduled and improving cluster elasticity and resource utilization.

Technically, this feature extends the Azure CNI Overlay networking model by allowing administrators to expand the Pod CIDR block associated with the cluster’s virtual network subnet. The implementation leverages enhancements in the Azure CNI plugin and AKS control plane to support incremental allocation of additional IP address ranges to the overlay network. When a Pod CIDR expansion is triggered, the Azure CNI Overlay dynamically updates routing and IP address management configurations across nodes, ensuring seamless IP assignment for new Pods without disrupting existing workloads. This avoids the need for disruptive operations such as cluster re-creation or node pool re-configuration, which were previously required to accommodate larger Pod IP address spaces.

From a practical standpoint, this update is particularly useful for organizations running large-scale microservices architectures or multi-tenant Kubernetes environments where Pod density per node or cluster size frequently grows beyond initial estimates. It enables IT professionals to plan and scale their AKS clusters more flexibly, accommodating workload spikes or expansion without downtime or complex migration procedures. For example, a SaaS provider hosting multiple customer environments on a single AKS cluster can now expand Pod CIDR ranges to onboard additional tenants or services dynamically.

However, there are important considerations and limitations to note. Since this feature is currently in public preview, it should be used in non-production or test environments until it reaches general availability. The expansion is supported only for clusters using the Azure CNI Overlay networking mode; clusters using other networking models such as Kubenet or Azure CNI underlay do not support this feature. Additionally, the maximum Pod CIDR size is constrained by the underlying subnet and virtual network address space, so proper IP address planning remains essential. Network policies and security group configurations may also need review to accommodate the expanded IP ranges.

This capability integrates tightly with Azure Virtual Network and Azure CNI plugin components, leveraging Azure’s native IP address management and routing infrastructure. It complements other AKS networking features such as advanced network policies and Azure Firewall integration by maintaining consistent network segmentation and security post-expansion. Furthermore, it aligns with Azure Monitor and Azure Policy for observability and governance over dynamically scaling cluster networks.

In summary, the Pod CIDR expansion in Azure CNI Overlay for AKS public preview empowers IT professionals to scale Kubernetes cluster IP address capacity dynamically and non-disruptively, enhancing operational agility and supporting large-scale, evolving workloads while maintaining integration with Azure’s networking and security ecosystem.

---

### 4. Public Preview: eBPF host routing in Advanced Container Networking Services (ACNS) for AKS

**Published**: November 14, 2025 16:00:47 UTC
**Link**: [Public Preview: eBPF host routing in Advanced Container Networking Services (ACNS) for AKS](https://azure.microsoft.com/updates?id=523100)

**Update ID**: 523100
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
Azure released a public preview of eBPF host routing support within Advanced Container Networking Services (ACNS) for Azure Kubernetes Service (AKS).

- Key changes or new features  
This update introduces eBPF-based host routing to improve network packet processing efficiency in AKS clusters. By leveraging eBPF, ACNS can reduce latency and increase throughput for containerized applications running at scale across distributed environments. This approach optimizes network path handling on the host, bypassing some traditional kernel networking overhead, resulting in better performance for container networking.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those running high-scale or latency-sensitive containerized workloads, will benefit from this feature. Network engineers focusing on Kubernetes networking and performance optimization will find this update relevant.

- Important notes if any  
This feature is currently in public preview, so it should be tested in non-production environments before adoption. Users should review compatibility and configuration details in the official documentation to ensure proper integration with existing AKS networking setups. Monitoring and validation of network performance improvements are recommended during evaluation.

For more details, visit: https://azure.microsoft.com/updates?id=523100

**Details**:

The public preview of eBPF host routing in Advanced Container Networking Services (ACNS) for Azure Kubernetes Service (AKS) introduces a significant enhancement in container networking by leveraging extended Berkeley Packet Filter (eBPF) technology to optimize host-level routing. This update addresses the performance bottlenecks inherent in traditional networking models for containerized workloads, especially as applications scale across distributed and multi-node environments.

**Background and Purpose**  
In AKS, networking traditionally relies on Azure CNI (Container Networking Interface), which configures IP routing and network policies for pods. However, as containerized applications grow in scale and complexity, conventional routing mechanisms—often based on Linux kernel IP routing tables and iptables—can introduce latency and throughput degradation due to the overhead of context switches and packet processing in user space. The purpose of integrating eBPF host routing into ACNS is to reduce this overhead by enabling more efficient, programmable packet processing directly within the Linux kernel, thereby improving network performance and scalability for AKS clusters.

**Specific Features and Detailed Changes**  
- **eBPF-based Host Routing:** Instead of relying solely on traditional routing tables, host routing decisions are offloaded to eBPF programs that run in kernel space. This allows for faster packet inspection and forwarding without transitioning to user space.  
- **Improved Network Throughput and Reduced Latency:** By minimizing the number of context switches and leveraging kernel-level packet processing, eBPF host routing reduces network latency and increases throughput for pod-to-pod and pod-to-service communication.  
- **Integration with Azure CNI:** The update extends Azure CNI capabilities by embedding eBPF programs that dynamically manage routing rules and policies at the host level, maintaining compatibility with existing CNI configurations.  
- **Public Preview Availability:** This feature is currently in public preview, enabling users to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
eBPF is a powerful Linux kernel technology that allows safe, sandboxed execution of custom bytecode for packet processing, tracing, and monitoring. In ACNS for AKS:  
- eBPF programs are loaded into the kernel at runtime to handle routing decisions for packets destined to or from pods on the host.  
- These programs intercept packets early in the kernel networking stack, enabling efficient routing without expensive user-space transitions.  
- The eBPF maps maintain state and routing information, updated dynamically by the ACNS control plane to reflect pod IP assignments and network policies.  
- This approach leverages XDP (eXpress Data Path) and TC (Traffic Control) hooks for high-performance packet processing.  
- The integration is transparent to the user, requiring minimal configuration changes while providing significant performance gains.

**Use Cases and Application Scenarios**  
- **High-Performance Microservices:** Applications requiring low-latency communication between microservices benefit from reduced network overhead.  
- **Large-Scale AKS Clusters:** Clusters with many nodes and pods experience improved network scalability and throughput.  
- **Latency-Sensitive Workloads:** Real-time data processing, gaming, financial services, and telemetry applications gain from faster packet routing.  
- **Multi-Tenant Environments:** Enhanced routing efficiency supports better isolation and policy enforcement in multi-tenant AKS clusters.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, it is not recommended for production workloads without thorough testing.  
- **Kernel Version Dependency:** eBPF functionality depends on Linux kernel versions; ensure node OS images support required eBPF features.  
- **Monitoring and Debugging:** eBPF programs add complexity; operators should familiarize themselves with eBPF tooling and diagnostics.  
- **Compatibility:** While designed to be compatible with existing Azure CNI configurations, some custom networking setups may require validation.  
- **Security:** eBPF programs run in kernel space; Azure ensures safety through verification, but users should monitor for potential security

---


*This report was automatically generated - 2025-11-15 03:02:39 UTC*