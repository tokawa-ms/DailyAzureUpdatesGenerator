# September 17, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 17, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 6 items

## Update List

### 1. Generally Available: At-cost data transfer between Azure and an external endpoint

**Published**: September 16, 2025 21:30:32 UTC
**Link**: [Generally Available: At-cost data transfer between Azure and an external endpoint](https://azure.microsoft.com/updates?id=501915)

**Update ID**: 501915
**Data source**: Azure Updates API

**Categories**: Launched, Pricing & Offerings, Management

**Summary**:

- What was updated  
Azure now offers at-cost data transfer pricing for data moved between Azure and external endpoints over the internet within Europe.

- Key changes or new features  
Customers and Cloud Solution Provider (CSP) partners in Europe can transfer data between Azure and non-Azure environments at cost, reducing expenses compared to standard data transfer rates. This update supports greater flexibility and cost efficiency for hybrid and multi-cloud scenarios involving data movement across network boundaries.

- Target audience affected  
Developers and IT professionals managing data integration, hybrid cloud architectures, or multi-cloud deployments in Europe. CSP partners reselling Azure services will also benefit from reduced data transfer costs.

- Important notes if any  
This at-cost pricing applies specifically to internet-based data transfers between Azure and external endpoints within Europe. It encourages customer choice and supports scenarios where data must flow between Azure and other environments without incurring premium data transfer fees. Users should verify regional applicability and consider this option when architecting data flows to optimize cost.  

For more details, visit: https://azure.microsoft.com/updates?id=501915

**Details**:

The recent Azure update announces the general availability of at-cost data transfer pricing for data moved between Azure and external endpoints over the internet, specifically targeting customers and Cloud Solution Provider (CSP) partners in Europe. This update reflects Microsoft’s commitment to supporting customer choice and cost transparency when transferring data between Azure and non-Azure environments.

**Background and Purpose**  
Traditionally, data egress from Azure to external networks incurs standard bandwidth charges, which can be significant and unpredictable for enterprises managing hybrid or multi-cloud architectures. Customers and CSPs often require frequent data exchanges between Azure and on-premises systems, other cloud providers, or external endpoints. The purpose of this update is to provide a more cost-effective and transparent pricing model—charging only the actual cost incurred by Microsoft for data transfer—thus enabling customers to optimize their network expenditure and improve budgeting accuracy.

**Specific Features and Detailed Changes**  
- Introduction of at-cost pricing for outbound data transfers from Azure to external internet endpoints within Europe.  
- This pricing model applies to customers and CSP partners transferring data over the internet, not via private or ExpressRoute connections.  
- The at-cost rate is lower than the standard egress bandwidth charges, reflecting Microsoft’s actual network costs without additional margin.  
- The update is currently limited to European regions, aligning with regional data sovereignty and compliance considerations.

**Technical Mechanisms and Implementation Methods**  
From a technical standpoint, data transfer pricing is managed at the Azure subscription and billing layer. When data packets exit Azure datacenters to external IP addresses over the internet, the network monitoring and metering systems track the volume of data transferred. The billing system then applies the at-cost rate to these outbound transfers for eligible customers and CSP partners in Europe. There is no change required in user configuration or network setup; the pricing adjustment is transparent and automatic. The data transfer itself continues to use standard Azure networking infrastructure, including Azure Virtual Network (VNet) gateways, Azure Firewall, or load balancers, depending on the customer’s architecture.

**Use Cases and Application Scenarios**  
- Enterprises replicating data from Azure-hosted applications or storage accounts to on-premises data centers or third-party cloud services can reduce operational costs.  
- CSP partners managing multi-tenant environments can offer more competitive pricing to their customers by leveraging at-cost data transfer rates.  
- Organizations running hybrid cloud architectures with frequent data synchronization between Azure and external systems benefit from predictable and lower network egress costs.  
- Data-intensive workloads such as media streaming, backup, disaster recovery, and analytics pipelines that involve cross-environment data movement will see cost efficiencies.

**Important Considerations and Limitations**  
- The at-cost data transfer pricing currently applies only to internet-based transfers in European Azure regions; transfers in other regions or via private connectivity (ExpressRoute) are not covered.  
- Inbound data transfers to Azure remain free, consistent with existing policies.  
- Customers should verify their subscription eligibility and regional applicability to benefit from this pricing.  
- Monitoring and cost management tools should be updated to reflect the new pricing model for accurate forecasting.  
- This pricing model does not affect data transfers within Azure regions or between Azure services, which continue to follow existing pricing rules.

**Integration with Related Azure Services**  
- Azure Cost Management and Billing: Updated to reflect at-cost data transfer charges, enabling detailed cost analysis and budgeting.  
- Azure Network Watcher and Traffic Analytics: Can be used to monitor data transfer volumes and patterns to optimize usage under the new pricing.  
- Azure Virtual Network and VPN Gateway: Facilitate secure data transfers to external endpoints, with cost benefits now aligned with at-cost pricing.  
- Azure Firewall and Azure Front Door: When used as data egress points, the at-cost pricing applies to outbound traffic routed through these services.

In summary, the general availability of at-cost data transfer pricing for Azure-to-external internet transfers in Europe offers IT professionals a practical means to reduce network egress expenses, improve cost predictability

---

### 2. Retirement: Azure Kubernetes Service on VMware will be retired on March 16, 2026 - Replace with Azure Kubernetes Service on Azure Local 

**Published**: September 16, 2025 19:45:51 UTC
**Link**: [Retirement: Azure Kubernetes Service on VMware will be retired on March 16, 2026 - Replace with Azure Kubernetes Service on Azure Local ](https://azure.microsoft.com/updates?id=500294)

**Update ID**: 500294
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Azure Kubernetes Service (AKS) on VMware (preview) effective March 16, 2026.

- Key changes or new features  
The AKS on VMware preview will no longer be supported after the retirement date. Microsoft recommends transitioning workloads to Azure Kubernetes Service on Azure Local, a fully supported AKS deployment option that provides a consistent Kubernetes experience closer to your on-premises environment.

- Target audience affected  
Developers and IT professionals currently using or evaluating AKS on VMware for container orchestration in hybrid or on-premises VMware environments.

- Important notes if any  
Plan your migration to AKS on Azure Local well before March 16, 2026 to avoid service disruption. Azure Local offers enhanced support and integration compared to the preview VMware offering. Review your current AKS on VMware workloads and dependencies to ensure a smooth transition. For more details, visit the official Azure update link.

**Details**:

The announced retirement of Azure Kubernetes Service (AKS) on VMware, effective March 16, 2026, signals a strategic shift by Microsoft to consolidate Kubernetes container orchestration offerings and streamline support towards Azure Kubernetes Service on Azure Local. AKS on VMware, introduced as a preview, enabled customers to deploy and manage AKS clusters directly on VMware infrastructure within their on-premises or hybrid environments, facilitating containerized application modernization without migrating workloads to the public cloud. The retirement notice advises users to transition to AKS on Azure Local, a fully supported service designed to run AKS clusters on Azure Stack HCI or Azure Stack Edge devices, providing a consistent Kubernetes experience closer to the edge or on-premises with full integration into Azure management and security frameworks.

From a feature perspective, AKS on VMware provided Kubernetes cluster lifecycle management, integrated Azure Active Directory (AAD) authentication, and Azure Monitor integration while running on VMware vSphere environments. Its retirement means these capabilities will no longer receive updates or support after the cutoff date. AKS on Azure Local offers comparable and enhanced features, including seamless integration with Azure Arc for hybrid management, Azure Policy enforcement for governance, and native support for Azure Container Registry and Azure DevOps pipelines. Technically, AKS on Azure Local leverages Azure Stack HCI infrastructure, utilizing Windows Server 2022 and Kubernetes distributions optimized for edge and on-premises scenarios, with automated cluster provisioning, upgrades, and scaling managed via Azure Portal or CLI.

Implementation of the transition involves assessing existing AKS on VMware workloads and migrating containerized applications and configurations to AKS on Azure Local clusters. This may require reconfiguring network settings, storage classes, and identity integration to align with Azure Local’s architecture. Tools such as Azure Migrate and Kubernetes-native utilities (e.g., Velero for backup/restore) can facilitate workload migration. The use cases for AKS on Azure Local encompass edge computing scenarios, disconnected or intermittently connected environments, and organizations requiring data residency or low-latency processing near the data source, while still benefiting from Azure’s cloud management capabilities.

Important considerations include planning the migration timeline well before the retirement date to avoid service disruption, validating compatibility of existing workloads with AKS on Azure Local’s Kubernetes version and supported features, and ensuring that operational teams are trained on the new environment’s management tools and security model. Limitations may arise from differences in underlying infrastructure capabilities between VMware and Azure Stack HCI platforms, such as storage options, networking plugins, or hardware compatibility, which must be evaluated during migration planning.

Integration with related Azure services is a key advantage of AKS on Azure Local. It supports Azure Arc-enabled Kubernetes for unified management across hybrid and multi-cloud environments, Azure Monitor for observability, Azure Policy for compliance enforcement, and Azure Security Center for threat protection. Additionally, it integrates with Azure DevOps and GitHub Actions for CI/CD pipelines, enabling streamlined DevOps workflows. This integration enhances operational efficiency and governance compared to the AKS on VMware preview, which had limited Azure service connectivity.

In summary, the retirement of AKS on VMware by March 16, 2026, requires IT professionals to proactively plan and execute migration to AKS on Azure Local to maintain supported Kubernetes container orchestration capabilities on-premises or at the edge. AKS on Azure Local offers a robust, fully supported platform with deeper Azure ecosystem integration, optimized for hybrid and edge scenarios, ensuring continuity, enhanced security, and management consistency within Azure’s cloud-native framework.

---

### 3. Generally Available: Azure File Sync in Poland Central and Spain Central

**Published**: September 16, 2025 17:45:04 UTC
**Link**: [Generally Available: Azure File Sync in Poland Central and Spain Central](https://azure.microsoft.com/updates?id=503421)

**Update ID**: 503421
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Storage, Cloud Services, Storage Accounts, Features

**Summary**:

- What was updated  
Azure File Sync is now generally available in the Poland Central and Spain Central regions.

- Key changes or new features  
This update extends Azure File Sync’s regional availability, enabling seamless synchronization and tiering of data between on-premises Windows Servers and Azure Files in these new locations. Organizations can now leverage hybrid cloud scenarios with improved data locality, reduced latency, and compliance benefits by keeping data closer to end users in Poland and Spain.

- Target audience affected  
Developers and IT professionals managing file server infrastructure, hybrid cloud storage solutions, and data migration projects in Poland, Spain, or nearby regions will benefit from this update. It is particularly relevant for those looking to optimize on-premises file server performance while integrating with Azure Files for backup, disaster recovery, or cloud tiering.

- Important notes if any  
Ensure your environment meets Azure File Sync prerequisites and consider network bandwidth and latency when deploying in these new regions. This regional expansion supports compliance with data residency requirements and can improve performance for local users accessing synchronized files. For detailed deployment guidance, refer to Azure File Sync documentation.

**Details**:

The recent general availability of Azure File Sync in the Poland Central and Spain Central regions extends Microsoft's hybrid cloud storage capabilities by enabling organizations in these geographies to seamlessly synchronize and tier data between on-premises Windows Servers and Azure Files. Azure File Sync is designed to simplify data migration, enhance data availability, and optimize storage costs by combining the performance and compatibility of local file servers with the scalability and durability of Azure cloud storage.

**Background and Purpose of the Update**  
Azure File Sync was introduced to address challenges faced by enterprises managing large volumes of file data across distributed environments. Traditionally, organizations rely on on-premises file servers for low-latency access but face limitations in scalability, backup complexity, and disaster recovery. Azure Files provides cloud-based SMB/NFS file shares with high durability but may introduce latency for local users. Azure File Sync bridges this gap by enabling a hybrid approach: local file servers cache frequently accessed data while less-used files are tiered to Azure Files, providing a unified namespace and centralized management. The expansion to Poland Central and Spain Central regions reflects Microsoft’s commitment to regional data residency, compliance, and performance optimization for customers in these areas.

**Specific Features and Detailed Changes**  
With this update, customers can now deploy Azure File Sync endpoints and sync groups in Poland Central and Spain Central, benefiting from local Azure infrastructure. Key features include:  
- **Multi-server sync:** Synchronize multiple Windows Servers with a single Azure File share, enabling centralized data management and collaboration.  
- **Cloud tiering:** Automatically tier cold data to Azure Files, freeing up local disk space while maintaining metadata locally for transparent access.  
- **Fast local access:** Frequently accessed files remain cached on-premises, ensuring low-latency performance for end users.  
- **Backup and disaster recovery:** Integration with Azure Backup allows snapshot-based backups of Azure File shares, simplifying data protection.  
- **Centralized management:** Use Azure Portal, PowerShell, or REST APIs to configure and monitor sync groups and endpoints.

**Technical Mechanisms and Implementation Methods**  
Azure File Sync operates by installing an agent on Windows Server (2012 R2, 2016, 2019, or later) that communicates with the Azure File Sync service. The service manages sync groups, which link one or more server endpoints to an Azure File share. The agent monitors file changes locally and synchronizes them to the cloud asynchronously. Cloud tiering uses a file attribute called the “hydration state” to determine whether a file is cached locally or tiered in the cloud. When a user accesses a tiered file, the agent transparently downloads the file on-demand. The sync engine uses a change journal and a cloud change log to track and reconcile changes, supporting conflict resolution and ensuring data consistency.

**Use Cases and Application Scenarios**  
- **Branch office file sharing:** Multiple branch offices can sync files to a central Azure File share, ensuring data consistency and availability across locations.  
- **Data migration:** Organizations can migrate on-premises file shares to Azure Files with minimal downtime by syncing data first and then switching clients to the cloud share.  
- **Backup optimization:** Tiering cold data reduces backup storage requirements and speeds up backup windows.  
- **Disaster recovery:** Local servers can be restored from Azure snapshots, enabling rapid recovery from hardware failures or ransomware attacks.  
- **Cloud bursting:** Applications requiring large datasets can access data locally or in the cloud without manual data movement.

**Important Considerations and Limitations**  
- **Supported Windows Server versions:** Ensure servers meet minimum OS requirements and have the Azure File Sync agent installed.  
- **Network bandwidth and latency:** Initial sync and large data transfers require sufficient bandwidth; tiering reduces ongoing bandwidth needs.  
- **File system limitations:** Azure File Sync supports NTFS file systems; certain file attributes and reparse points may not be supported.  
- **Data residency and compliance:** Using Poland Central and Spain Central regions helps meet local data sovereignty requirements.

---

### 4. Public Preview: Azure HBv5-series VMs

**Published**: September 16, 2025 17:45:04 UTC
**Link**: [Public Preview: Azure HBv5-series VMs](https://azure.microsoft.com/updates?id=503129)

**Update ID**: 503129
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Linux Virtual Machines, Virtual Machines, Windows Virtual Machines, Services

**Summary**:

- What was updated  
Azure announced the public preview availability of HBv5-series virtual machines (VMs) in the South Central US region.

- Key changes or new features  
HBv5 VMs are designed for high-performance computing (HPC) workloads that require high memory bandwidth. They feature AMD EPYC 7003-series processors with up to 120 vCPUs, large memory capacity, and support for RDMA over InfiniBand for low-latency, high-throughput networking. These VMs are optimized for applications such as computational fluid dynamics, automotive and aerospace simulations, weather modeling, and other memory bandwidth-intensive HPC scenarios.

- Target audience affected  
Developers and IT professionals working on HPC workloads, scientific simulations, engineering applications, and other compute- and memory-intensive tasks will benefit from these new VM options.

- Important notes if any  
The HBv5-series VMs are currently in public preview and available only in the South Central US region. Users should consider preview limitations and regional availability when planning deployments. Integration with Azure HPC networking features like RDMA is a key advantage for scaling HPC applications efficiently.

**Details**:

The Azure HBv5-series virtual machines (VMs) have entered public preview in the South Central US region, targeting high-performance computing (HPC) workloads that demand exceptional memory bandwidth and computational power. This update introduces a new VM SKU optimized specifically for memory bandwidth-intensive applications such as computational fluid dynamics (CFD), automotive and aerospace simulations, and weather modeling, expanding Azure’s HPC capabilities.

**Background and Purpose**  
Azure’s HPC offerings continuously evolve to meet the growing computational and memory bandwidth requirements of scientific and engineering workloads. The HBv5-series VMs build upon the previous HB-series by incorporating the latest AMD EPYC 7003 “Milan” processors, which provide a significant increase in memory bandwidth and core count. The purpose of this update is to enable customers running memory-bound HPC applications to achieve better performance and scalability on Azure’s cloud infrastructure, reducing time-to-solution and improving cost efficiency.

**Specific Features and Detailed Changes**  
- **Processor:** HBv5 VMs leverage AMD EPYC 7003 series CPUs, featuring up to 64 cores per VM with a base clock speed around 2.35 GHz and boost capabilities, optimized for HPC workloads.  
- **Memory Bandwidth:** These VMs offer enhanced memory bandwidth, critical for applications that require rapid data movement between CPU and memory, such as CFD and large-scale simulations.  
- **VM Sizes:** Multiple VM sizes are available within the HBv5 series, allowing users to select configurations that best fit their workload requirements in terms of CPU cores, memory, and network bandwidth.  
- **Network:** HBv5 VMs support Azure’s high-throughput, low-latency InfiniBand networking, enabling efficient MPI (Message Passing Interface) communication for tightly coupled HPC clusters.  
- **Storage:** They integrate with Azure Ultra Disk and Premium SSD storage options to support high IOPS and throughput needed for HPC data storage and scratch space.

**Technical Mechanisms and Implementation Methods**  
The HBv5-series VMs utilize AMD’s latest EPYC “Milan” processors, which implement the Zen 3 microarchitecture. This architecture improves instructions per cycle (IPC) and memory subsystem efficiency, delivering higher memory bandwidth per core. Azure pairs these CPUs with RDMA-capable InfiniBand networking, enabling low-latency, high-bandwidth inter-node communication essential for distributed HPC workloads using MPI or similar frameworks. The VMs are deployed on Azure’s HPC-optimized infrastructure, ensuring dedicated hardware resources and isolation for predictable performance.

**Use Cases and Application Scenarios**  
- **Computational Fluid Dynamics (CFD):** Simulations requiring high memory throughput to process large meshes and fluid dynamics calculations benefit from HBv5’s enhanced memory bandwidth.  
- **Automotive and Aerospace Simulations:** Complex finite element analysis (FEA) and multi-physics simulations that are memory bandwidth-bound can run more efficiently.  
- **Weather Modeling:** Large-scale atmospheric simulations that process vast datasets in memory-intensive operations gain performance improvements.  
- **Molecular Dynamics and Life Sciences:** Workloads involving large datasets and memory-intensive computations can leverage these VMs.  
- **Financial Risk Modeling:** Scenarios requiring fast in-memory calculations and large datasets also benefit.

**Important Considerations and Limitations**  
- **Preview Availability:** Currently, HBv5-series VMs are in public preview only in the South Central US region, which may limit geographic availability and SLA guarantees.  
- **Pricing:** Preview pricing may differ from GA pricing; users should monitor cost implications.  
- **Compatibility:** Existing HPC applications may require tuning or recompilation to fully exploit the new CPU architecture and memory bandwidth.  
- **Networking:** To maximize performance, workloads should be architected to use InfiniBand and MPI, which may require additional configuration.  
- **Quota:** Users may need to request quota increases for HBv5 VMs in their subscription.

**Integration with Related Azure Services**  
- **Azure CycleCloud

---

### 5. Generally Available: AKS Automatic 

**Published**: September 16, 2025 17:30:21 UTC
**Link**: [Generally Available: AKS Automatic ](https://azure.microsoft.com/updates?id=503235)

**Update ID**: 503235
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) Automatic is now generally available, providing enhanced automation for cluster management.

- Key changes or new features  
AKS Automatic simplifies Kubernetes operations by automating cluster lifecycle management tasks such as provisioning, scaling, patching, and upgrades. It reduces the operational overhead by handling infrastructure tuning and security updates automatically. This helps teams focus more on application development rather than cluster maintenance. The service also improves reliability and security by proactively managing risks and ensuring clusters are up-to-date with best practices.

- Target audience affected  
Developers and IT professionals managing Kubernetes workloads on Azure, especially those seeking to reduce complexity and operational burden in AKS cluster management.

- Important notes if any  
Teams adopting AKS Automatic should review their existing cluster configurations to align with automated management policies. While automation reduces manual intervention, monitoring and governance remain critical to ensure compliance and performance. This update is part of Azure’s ongoing efforts to streamline Kubernetes adoption and operational excellence.  

For more details, visit: https://azure.microsoft.com/updates?id=503235

**Details**:

The Azure Kubernetes Service (AKS) Automatic Update feature has reached general availability, addressing the operational complexity and maintenance overhead commonly associated with managing Kubernetes clusters. This update is designed to streamline cluster management by automating the patching and upgrading of AKS nodes and control plane components, thereby enhancing security, reliability, and operational efficiency for IT teams.

**Background and Purpose**  
Kubernetes, while powerful for orchestrating containerized applications, presents challenges in cluster lifecycle management, including frequent updates to address security vulnerabilities, bug fixes, and feature enhancements. Manual updates are time-consuming and error-prone, often requiring downtime or complex coordination. The AKS Automatic Update feature aims to reduce this operational burden by enabling automated, controlled, and seamless updates to AKS clusters, allowing teams to focus more on application development rather than infrastructure maintenance.

**Specific Features and Detailed Changes**  
- **Automated Node and Control Plane Updates:** The feature automates patching and version upgrades for both the AKS control plane and the underlying node pools.  
- **Configurable Update Windows:** Users can specify maintenance windows to control when updates occur, minimizing disruption to workloads.  
- **Intelligent Orchestration:** Updates are orchestrated to maintain cluster availability by sequentially updating nodes and leveraging Kubernetes’ self-healing capabilities.  
- **Version Management:** Supports automatic upgrades within defined version ranges, ensuring compatibility and stability.  
- **Security and Compliance:** Frequent patching reduces exposure to vulnerabilities and aligns with compliance requirements for timely software updates.

**Technical Mechanisms and Implementation Methods**  
The Automatic Update feature integrates with AKS’s existing cluster management APIs and Azure Resource Manager (ARM) to schedule and execute updates. It leverages Kubernetes’ native rolling update mechanisms to drain and update nodes without impacting running workloads significantly. The control plane updates are managed by Azure as a managed service, ensuring minimal downtime. Users configure update policies via Azure CLI, Azure Portal, or ARM templates, specifying parameters such as maintenance windows, version constraints, and node pool selection. The system monitors cluster health during updates, with rollback capabilities if issues are detected.

**Use Cases and Application Scenarios**  
- **Production Environments:** Enterprises running critical applications can maintain high availability while ensuring clusters are up-to-date with security patches and feature improvements.  
- **DevOps Automation:** Teams adopting GitOps or CI/CD pipelines benefit from reduced manual intervention in cluster maintenance.  
- **Regulated Industries:** Organizations with strict compliance requirements can demonstrate adherence to patch management policies.  
- **Multi-Cluster Management:** Large-scale deployments with multiple AKS clusters can standardize update policies to reduce operational complexity.

**Important Considerations and Limitations**  
- **Version Compatibility:** Automatic updates occur within configured version ranges; major version upgrades may still require manual intervention.  
- **Maintenance Window Adherence:** Updates outside specified windows may not be supported, requiring careful scheduling.  
- **Workload Sensitivity:** Although rolling updates minimize downtime, stateful or latency-sensitive applications should be tested for update impact.  
- **Custom Node Configurations:** Nodes with custom configurations or extensions may require validation to ensure compatibility with automated updates.  
- **Rollback Scenarios:** While rollback is supported, complex failure modes may require manual troubleshooting.

**Integration with Related Azure Services**  
- **Azure Monitor and Azure Log Analytics:** Integration allows monitoring of update progress and cluster health metrics during and after updates.  
- **Azure Policy:** Can enforce update policies across multiple clusters for governance.  
- **Azure DevOps and GitHub Actions:** Facilitate automation of update configurations as part of infrastructure-as-code workflows.  
- **Azure Security Center:** Benefits from timely patching to reduce security alerts related to vulnerable Kubernetes components.

In summary, the general availability of AKS Automatic Update significantly simplifies Kubernetes cluster maintenance by automating patching and upgrades within controlled parameters, improving security posture and operational efficiency while integrating seamlessly with Azure’s ecosystem of monitoring, governance, and DevOps tools. This enables IT professionals to

---

### 6. Generally Available: Azure Container Storage v2.0.0 now with NVMe performance boost, open source, and no service fees

**Published**: September 16, 2025 14:30:41 UTC
**Link**: [Generally Available: Azure Container Storage v2.0.0 now with NVMe performance boost, open source, and no service fees](https://azure.microsoft.com/updates?id=502853)

**Update ID**: 502853
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Compute, Azure Container Storage, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure Container Storage (ACStor) has reached general availability with version 2.0.0.

- Key changes or new features  
ACStor v2.0.0 introduces a significant performance boost by leveraging local NVMe storage, delivering up to 7× higher IOPS and 4× lower latency compared to the previous version 1.3.1. This makes it the fastest storage option for Azure Kubernetes Service (AKS). Additionally, the solution is now open source and offered with no service fees, reducing cost and increasing transparency for users.

- Target audience affected  
Developers and IT professionals working with containerized applications on Azure Kubernetes Service will benefit from improved storage performance and cost efficiency. DevOps teams managing AKS clusters can leverage faster persistent storage for stateful workloads.

- Important notes if any  
The update emphasizes local NVMe storage integration, so workloads requiring high IOPS and low latency will see the most benefit. Being open source allows for community contributions and customization. No service fees mean organizations can optimize costs when scaling container storage in AKS environments.

For more details, visit: https://azure.microsoft.com/updates?id=502853

**Details**:

Azure Container Storage (ACStor) v2.0.0 has reached general availability, introducing significant performance improvements, an open-source model, and the removal of service fees, positioning it as a high-performance, cost-effective storage solution for Azure Kubernetes Service (AKS) workloads. This update addresses the growing demand for low-latency, high-throughput storage in containerized environments by leveraging local NVMe storage technology.

**Background and Purpose**  
The update aims to enhance the storage performance and cost-efficiency for containerized applications running on AKS. Previous versions of ACStor provided persistent storage but were limited by traditional storage media and incurred service fees. As containerized workloads increasingly require faster I/O to support stateful applications such as databases, caching layers, and real-time analytics, ACStor v2.0.0 introduces NVMe-based local storage to meet these demands while simplifying cost structures through open-source availability and zero service fees.

**Specific Features and Detailed Changes**  
- **Performance Boost:** ACStor v2.0.0 delivers up to 7× higher IOPS and 4× lower latency compared to version 1.3.1 by utilizing local NVMe SSDs on AKS nodes. This results in significantly faster read/write operations, improving application responsiveness and throughput.  
- **Open Source:** The entire ACStor codebase is now open source, enabling community contributions, transparency, and customization. This fosters innovation and allows organizations to tailor the storage solution to their specific needs.  
- **No Service Fees:** Microsoft has removed service fees associated with ACStor, reducing the total cost of ownership for persistent container storage in AKS. Users pay only for the underlying Azure infrastructure resources consumed.  
- **Compatibility:** ACStor continues to support Kubernetes Container Storage Interface (CSI), ensuring seamless integration with AKS and compatibility with Kubernetes storage management tools.

**Technical Mechanisms and Implementation**  
ACStor v2.0.0 leverages local NVMe SSDs attached to AKS nodes to provide ultra-low latency and high throughput storage. It implements a CSI driver that exposes these NVMe devices as persistent volumes to Kubernetes pods. The local NVMe storage is managed by ACStor’s control plane, which handles volume provisioning, lifecycle management, and data persistence. By using local storage rather than network-attached storage, ACStor minimizes I/O path length, reducing latency and increasing IOPS. The open-source nature allows users to inspect and modify the storage controller and CSI driver components.

**Use Cases and Application Scenarios**  
- **Stateful Applications:** Databases (e.g., PostgreSQL, MySQL), NoSQL stores, and caching systems benefit from the low latency and high IOPS of NVMe storage.  
- **Real-Time Analytics:** Applications requiring rapid data ingestion and processing can leverage the improved throughput.  
- **CI/CD Pipelines:** Faster storage accelerates build and test cycles in containerized environments.  
- **Edge and IoT:** Local NVMe storage supports scenarios where network connectivity is limited or latency-sensitive.  
- **Development and Testing:** Cost savings from no service fees make ACStor ideal for non-production environments requiring persistent storage.

**Important Considerations and Limitations**  
- **Node Affinity:** Since storage is local to AKS nodes, pods using ACStor volumes must be scheduled on the same node to maintain data locality, which can impact pod scheduling flexibility and high availability strategies.  
- **Data Durability:** Local NVMe storage is ephemeral relative to network-attached storage; node failures can result in data loss unless additional replication or backup strategies are implemented.  
- **Capacity Constraints:** Storage capacity is limited by the size of NVMe drives attached to the AKS nodes, requiring careful capacity planning.  
- **Cluster Configuration:** Proper AKS node sizing and NVMe-enabled VM SKU selection are necessary to leverage the performance benefits.

**Integration with Related Azure Services**  
ACStor v2.0.0 integrates tightly with

---


*This report was automatically generated - 2025-09-17 03:03:16 UTC*