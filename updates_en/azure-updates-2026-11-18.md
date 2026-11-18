# November 18, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 18, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 165 items

## Update List

### 1. Public Preview: Immutable snapshots for Azure Disk Storage 

**Published**: November 18, 2026 00:00:09 UTC
**Link**: [Public Preview: Immutable snapshots for Azure Disk Storage ](https://azure.microsoft.com/updates?id=581503)

**Update ID**: 581503
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Disk Storage, Features, Compliance, Microsoft Ignite, Security

**Summary**:

- What was updated  
Azure Disk Storage now supports immutable snapshots in public preview.

- Key changes or new features  
Immutable snapshots prevent modification or deletion once created, ensuring data integrity and protection against ransomware or accidental changes. They complement Azure Backup immutable vaults by providing short-term backup options with faster recovery times. Developers and IT professionals can leverage immutable snapshots for operational backups, compliance, and enhanced security scenarios.

- Target audience affected  
Developers, IT professionals, and organizations managing Azure Disk Storage who require secure, tamper-proof backups for compliance or operational needs.

- Important notes  
Immutable snapshots are ideal for short-term backup and rapid recovery, while Azure Backup immutable vaults remain the recommended solution for cost-efficient, long-term retention. The feature is currently in public preview, so it may not be suitable for production workloads until general availability. Review Azure documentation for limitations and supported disk types during the preview phase.

**Details**:

**Azure Update Report: Public Preview – Immutable Snapshots for Azure Disk Storage**

**Background and Purpose of the Update**  
The introduction of immutable snapshots for Azure Disk Storage addresses the growing need for enhanced data protection and compliance in cloud environments. Immutable snapshots are designed to prevent modification or deletion of backup data for a specified retention period, thereby supporting regulatory requirements and protecting against accidental or malicious data loss. This feature complements Azure Backup immutable vaults, which are intended for cost-efficient, long-term retention, by providing a solution optimized for short-term backup scenarios requiring rapid recovery.

**Specific Features and Detailed Changes**  
With this update, Azure Disk Storage now supports the creation of immutable snapshots. These snapshots cannot be altered or deleted until their retention period expires, ensuring data integrity during the backup window. The feature is available in public preview, allowing customers to test and evaluate its functionality. Key features include:
- Creation of immutable snapshots directly from Azure Disk Storage.
- Enforcement of immutability, preventing any modification or deletion during the retention period.
- Integration with existing disk management workflows for seamless adoption.

**Technical Mechanisms and Implementation Methods**  
Immutable snapshots leverage Azure’s storage infrastructure to enforce write-once, read-many (WORM) semantics. When a snapshot is created and marked as immutable, Azure applies a retention policy at the storage layer. This policy ensures that the snapshot remains locked and inaccessible for modification or deletion until the retention period lapses. Operations such as snapshot deletion or alteration are blocked by Azure’s access control mechanisms, providing technical assurance of immutability.

**Use Cases and Application Scenarios**  
- **Short-term Backup and Rapid Recovery:** Immutable snapshots are ideal for scenarios where quick restoration of data is required, such as before major application upgrades or patching.
- **Compliance and Regulatory Requirements:** Organizations needing to demonstrate adherence to data retention policies can use immutable snapshots to ensure backup data cannot be tampered with.
- **Protection Against Ransomware and Malicious Deletion:** By preventing deletion or modification, immutable snapshots provide an additional layer of defense against ransomware attacks or insider threats.
- **Complementing Long-term Retention:** While Azure Backup immutable vaults are suited for long-term archival, immutable snapshots offer a solution for short-term, high-speed backup and recovery needs.

**Important Considerations and Limitations**  
- **Retention Policy:** Once set, the retention period cannot be shortened or bypassed; snapshots remain immutable until expiry.
- **Preview Limitations:** As the feature is in public preview, it may not support all regions or disk types, and production workloads should be evaluated carefully.
- **Cost Implications:** Immutable snapshots may incur additional storage costs, especially if used extensively for short-term backups.
- **Operational Restrictions:** No deletion or modification is possible during the retention period, which may impact operational flexibility.

**Integration with Related Azure Services**  
Immutable snapshots are designed to work alongside Azure Backup immutable vaults. While vaults provide cost-efficient, long-term storage, snapshots offer rapid, short-term backup and recovery. This allows IT professionals to architect layered data protection strategies, combining the strengths of both services. Snapshots can be managed via Azure Portal, CLI, or API, ensuring compatibility with existing automation and orchestration workflows.

**Summary Sentence**  
Azure Disk Storage now offers immutable snapshots in public preview, enabling secure, short-term backup solutions that prevent modification or deletion during a defined retention period, and complementing Azure Backup immutable vaults for comprehensive data protection strategies.

---

### 2. Announcing: Azure Boost observability for NVMe disks

**Published**: November 18, 2026 00:00:09 UTC
**Link**: [Announcing: Azure Boost observability for NVMe disks](https://azure.microsoft.com/updates?id=581227)

**Update ID**: 581227
**Data source**: Azure Updates API

**Categories**: Storage, Compute, Azure Disk Storage, Virtual Machines, Announcement

**Summary**:

- What was updated  
Azure Boost observability for NVMe disks has been announced, introducing a new open-source command-line tool for Azure VMs.

- Key changes or new features  
The tool enables users to monitor remote disk I/O and latency metrics for NVMe disks within compatible Azure virtual machines. It also maps each disk inside the VM to its corresponding physical disk, providing granular visibility into disk performance. The solution leverages Azure Boost technology to deliver accurate and real-time observability.

- Target audience affected  
This update is relevant to developers, IT professionals, and cloud administrators who manage workloads on Azure VMs with NVMe disks and require advanced performance monitoring and troubleshooting capabilities.

- Important notes if any  
The tool is open-source and must be run inside compatible Azure VMs. It is especially useful for diagnosing disk performance issues, optimizing workloads, and ensuring high-performance storage configurations. Compatibility and usage instructions are available in the documentation. Early adoption is recommended for teams requiring enhanced disk observability in Azure environments.

**Details**:

**Azure Update Report: Azure Boost Observability for NVMe Disks**

**Background and Purpose of the Update**  
The Azure Boost observability for NVMe disks update introduces an open-source command-line tool designed to enhance disk performance monitoring within Azure virtual machines (VMs) equipped with NVMe storage. The primary purpose is to provide IT professionals with granular visibility into remote disk I/O and latency metrics, leveraging Azure Boost technology. This update addresses the need for improved observability and diagnostics for NVMe disks, enabling users to better understand and optimize disk performance within their Azure environments.

**Specific Features and Detailed Changes**  
The newly announced tool offers the following key features:

- **Remote Disk I/O Metrics**: The tool collects and displays metrics related to disk input/output operations, allowing users to monitor throughput and identify potential bottlenecks.
- **Latency Metrics**: It provides detailed latency measurements for each NVMe disk, helping users pinpoint performance issues.
- **Disk Mapping**: Each disk inside the VM is mapped to its corresponding physical NVMe disk, offering clear visibility into the relationship between logical and physical storage resources.
- **Open-Source CLI**: The tool is distributed as an open-source command-line interface, facilitating easy integration into existing workflows and automation scripts.

These features collectively enable more precise monitoring and troubleshooting of NVMe disk performance within Azure VMs.

**Technical Mechanisms and Implementation Methods**  
The tool operates by running inside compatible Azure VMs, interfacing with Azure Boost—a platform feature that accelerates storage and networking performance. Azure Boost provides the underlying infrastructure support, enabling the tool to remotely access and report disk I/O and latency metrics. The tool leverages APIs and telemetry exposed by Azure Boost to gather real-time performance data, which is then presented to the user via the CLI. Disk mapping functionality ensures that each logical disk within the VM is accurately associated with its physical NVMe counterpart, improving traceability and diagnostic accuracy.

**Use Cases and Application Scenarios**  
Typical use cases for this tool include:

- **Performance Monitoring**: IT professionals can use the tool to continuously monitor NVMe disk performance, ensuring optimal operation and early detection of anomalies.
- **Troubleshooting**: When encountering disk-related issues, the tool’s metrics facilitate root cause analysis by providing detailed I/O and latency data.
- **Capacity Planning**: By analyzing disk usage patterns and performance metrics, users can make informed decisions about scaling storage resources.
- **Integration with Automation**: The CLI nature of the tool allows for integration into automated monitoring and alerting systems, supporting DevOps workflows.

**Important Considerations and Limitations**  
- **VM Compatibility**: The tool must be run inside compatible Azure VMs; not all VM types may support NVMe disks or Azure Boost features.
- **Scope of Metrics**: The tool focuses on remote disk I/O and latency metrics; other performance aspects may require additional monitoring solutions.
- **Open-Source Nature**: As an open-source tool, users should review documentation and community support for updates and troubleshooting.

**Integration with Related Azure Services**  
The tool is backed by Azure Boost, ensuring seamless integration with Azure’s high-performance storage infrastructure. It can complement Azure Monitor and other observability solutions by providing disk-specific metrics that may not be available through standard Azure monitoring tools. Users can incorporate the tool’s output into broader monitoring dashboards or alerting systems for comprehensive infrastructure visibility.

**Summary Sentence**  
Azure Boost observability for NVMe disks provides IT professionals with an open-source CLI tool to monitor remote disk I/O and latency metrics within compatible Azure VMs, enhancing disk performance visibility and troubleshooting capabilities through Azure Boost integration.

---

### 3. Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines

**Published**: November 17, 2026 23:55:53 UTC
**Link**: [Generally Available: Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines](https://azure.microsoft.com/updates?id=581298)

**Update ID**: 581298
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Microsoft Ignite

**Summary**:

- What was updated  
Azure has announced the general availability of new Cobalt 200 Arm-based virtual machine series: Dplsv7, Dpsv7 (general purpose), Epsv7 (memory-optimized), Mpsv4 (high-memory), and Lpsv5 (dense storage).

- Key changes or new features  
These VM series deliver substantial improvements over the previous Cobalt 100 generation, including better performance, scalability, and efficiency. The new Arm-based architecture offers enhanced compute power, improved memory bandwidth, and optimized storage options. Each VM type is tailored for specific workloads:  
  - Dpsv7/Dplsv7: General purpose workloads  
  - Epsv7: Memory-intensive applications  
  - Mpsv4: High-memory requirements  
  - Lpsv5: Dense storage needs  
Developers and IT professionals can leverage these VMs for cost-effective, high-performance cloud solutions, with expanded support for Linux workloads and modern application architectures.

- Target audience affected  
Developers, IT professionals, and cloud architects seeking improved performance, scalability, and cost efficiency for their applications, especially those running Linux or requiring optimized compute, memory, or storage.

- Important notes if any  
Migration from Cobalt 100 to Cobalt 200 VMs is recommended to take advantage of performance and efficiency gains. Ensure application compatibility with Arm architecture. Review VM sizing and workload requirements for optimal selection.  
[Azure Update Link](https://azure.microsoft.com/updates?id=581298)

**Details**:

**Azure Update Report: Generally Available - Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**

**Background and Purpose of the Update**  
Microsoft Azure has announced the general availability of the Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines (VMs). This release is aimed at providing customers with improved performance and efficiency compared to the previous generation Cobalt 100 VMs. The update introduces new VM series tailored to general purpose, memory-optimized, high-memory, and dense storage workloads, leveraging the latest advancements in Arm-based architecture.

**Specific Features and Detailed Changes**  
- **Dpsv7 and Dplsv7-series**: These are general-purpose VMs designed for balanced compute, memory, and storage requirements.  
- **Epsv7-series**: Memory-optimized VMs, suitable for workloads that require higher memory-to-core ratios.  
- **Mpsv4-series**: High-memory VMs, intended for applications with substantial memory demands.  
- **Lpsv5-series**: Dense storage VMs, optimized for workloads needing high storage throughput and capacity.

All these VM series are based on the Cobalt 200 Arm architecture, which delivers notable enhancements in performance, efficiency, and scalability over the previous Cobalt 100 generation. The update includes improvements in compute power, memory bandwidth, and storage capabilities, making these VMs suitable for a broader range of enterprise workloads.

**Technical Mechanisms and Implementation Methods**  
The Cobalt 200 Arm-based VMs utilize advanced Arm processors, which are known for their energy efficiency and high performance. Azure has integrated these processors into its VM infrastructure, allowing customers to deploy workloads on Arm architecture seamlessly. The VMs are provisioned through the Azure portal, CLI, or ARM templates, and support standard Azure features such as managed disks, virtual networking, and availability sets.

**Use Cases and Application Scenarios**  
- **General Purpose (Dpsv7/Dplsv7)**: Suitable for web servers, application servers, and development/test environments.
- **Memory-Optimized (Epsv7)**: Ideal for in-memory databases, analytics workloads, and large caches.
- **High-Memory (Mpsv4)**: Targeted at enterprise databases, SAP workloads, and high-performance computing applications.
- **Dense Storage (Lpsv5)**: Designed for big data, NoSQL databases, and data warehousing solutions that require high storage throughput.

These VM series provide flexibility for IT professionals to select the optimal configuration based on workload requirements, enabling cost-effective scaling and improved resource utilization.

**Important Considerations and Limitations**  
- Customers should evaluate workload compatibility with Arm architecture, as some applications may require x86-specific features.
- Performance characteristics may differ from previous Cobalt 100 VMs; benchmarking is recommended before production deployment.
- Not all Azure regions may support these VM series at launch; availability should be verified in the Azure portal.
- Licensing and pricing models may vary based on VM series and configuration.

**Integration with Related Azure Services**  
The Cobalt 200 Arm-based VMs integrate seamlessly with Azure services such as Azure Storage, Azure Virtual Network, Azure Backup, and Azure Monitor. They can be used in conjunction with Azure Kubernetes Service (AKS), Azure App Services, and other compute-related offerings, supporting modern cloud-native architectures.

**Summary Sentence**  
The general availability of Cobalt 200 Arm-based Dplsv7, Dpsv7, Epsv7, Mpsv4, and Lpsv5-series VMs provides Azure customers with enhanced performance and efficiency across a range of workload types, leveraging advanced Arm architecture for improved scalability and cost-effectiveness.

---

### 4. Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL 

**Published**: November 17, 2026 23:52:49 UTC
**Link**: [Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=579590)

**Update ID**: 579590
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now offers Intel and AMD v6 compute tiers with local temporary disk, available for general use.

- Key changes or new features  
The v6 generation introduces higher performance compute options and larger scale capabilities for PostgreSQL workloads. The addition of local temporary disks enables improved I/O throughput and reduced latency for operations requiring temporary storage, such as sorts and index builds. These tiers are designed for demanding workloads, supporting more concurrent connections and faster processing.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure, especially those requiring high-performance compute, large-scale deployments, or workloads with intensive temporary storage needs.

- Important notes if any  
Migrating to v6 tiers may require configuration changes to leverage temporary disk features. Pricing and regional availability may vary, so review documentation before deployment. The update is relevant for performance-sensitive applications, analytics, and large-scale database operations.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Intel and AMD v6 with temp disk for Azure Database for PostgreSQL  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579590)

---

### Background and Purpose of the Update

Azure Database for PostgreSQL Flexible Server is a managed database service designed for high availability, scalability, and flexible deployment. The introduction of Intel and AMD v6 compute tiers with local temporary disk addresses the growing demand for higher performance and larger-scale database workloads. This update aims to enhance the compute portfolio, offering customers more choices to optimize cost, performance, and workload requirements.

---

### Specific Features and Detailed Changes

- **New Compute Tiers:** The update introduces Intel and AMD v6 generation virtual machines as compute options for PostgreSQL Flexible Server.
- **Local Temporary Disk:** These v6 compute tiers come equipped with local temporary disks, providing fast, ephemeral storage directly attached to the compute node.
- **Performance and Scale:** The v6 generation offers improved CPU performance, increased memory, and larger scale compared to previous generations, supporting more demanding database workloads.

---

### Technical Mechanisms and Implementation Methods

- **Compute Infrastructure:** The v6 compute tiers leverage the latest Intel and AMD processor architectures, delivering enhanced processing power and memory bandwidth.
- **Local Temporary Disk Integration:** The local temporary disk is physically attached to the underlying VM. It is designed for transient data such as temporary tables, sort operations, and query processing, which benefit from low-latency, high-throughput storage.
- **Deployment:** Users can select the v6 compute tiers with temp disk during the provisioning or scaling of Azure Database for PostgreSQL Flexible Server instances via the Azure Portal, CLI, or ARM templates.

---

### Use Cases and Application Scenarios

- **High-Performance OLTP/OLAP Workloads:** Workloads requiring fast temporary storage for intermediate query results, such as analytics, reporting, or complex transactional processing.
- **Large-Scale Databases:** Applications that need to scale up compute and memory resources to handle large datasets or high concurrency.
- **Cost-Optimized Deployments:** Customers seeking to balance performance and cost by selecting the most suitable compute tier for their workload characteristics.

---

### Important Considerations and Limitations

- **Ephemeral Storage:** The local temporary disk is not persistent. Data stored on the temp disk is lost during server reboots, maintenance, or failovers. It should only be used for temporary data that can be regenerated or is not critical.
- **Compatibility:** Existing Flexible Server deployments may require migration or redeployment to leverage the new v6 compute tiers.
- **Resource Sizing:** Proper sizing of compute and temp disk resources is essential to avoid bottlenecks and ensure optimal performance.

---

### Integration with Related Azure Services

- **Azure Monitoring and Management:** The v6 compute tiers with temp disk are fully integrated with Azure’s monitoring, alerting, and management tools, enabling seamless operational oversight.
- **Backup and High Availability:** Persistent data remains protected by Azure’s managed backup and high availability features, as temp disk is only used for non-persistent operations.
- **Ecosystem Compatibility:** The update maintains compatibility with other Azure services and tools commonly used with PostgreSQL Flexible Server, such as Azure Data Studio, Azure CLI, and ARM templates.

---

**Summary Sentence:**  
Azure Database for PostgreSQL Flexible Server now offers generally available Intel and AMD v6 compute tiers with local temporary disk, delivering enhanced performance and scalability for demanding workloads while providing fast, ephemeral storage for temporary data operations.

---

### 5. Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL 

**Published**: November 17, 2026 23:51:44 UTC
**Link**: [Generally Available: Intel and AMD v5 diskless tier for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=579595)

**Update ID**: 579595
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now offers generally available Intel and AMD v5 diskless compute tiers.

- Key changes or new features  
The new diskless compute options expand the v5 portfolio with General Purpose and Memory Optimized SKUs. These SKUs do not include local temporary storage, which can simplify architecture for workloads that do not require local temp storage. The diskless tier provides improved flexibility in selecting compute resources and may offer cost benefits for certain workloads.

- Target audience affected  
Developers and IT professionals managing PostgreSQL workloads on Azure, especially those seeking optimized compute options or cost-effective deployments without the need for local temporary storage.

- Important notes  
Applications relying on local temporary storage should not use diskless SKUs, as these tiers do not provide local temp disks. Evaluate workload requirements before migrating or deploying to diskless compute. This update enables more granular control over resource allocation and can help optimize performance and costs for suitable PostgreSQL workloads.

**Details**:

**Azure Update Report: Intel and AMD v5 Diskless Tier for Azure Database for PostgreSQL (General Availability)**

**Background and Purpose of the Update:**  
Azure Database for PostgreSQL Flexible Server has introduced the general availability of Intel and AMD v5 diskless compute tiers. The purpose of this update is to broaden the v5 compute portfolio by offering new General Purpose and Memory Optimized SKUs that do not include local temporary storage. This enhancement allows customers to select compute resources that better match their workload requirements, particularly for scenarios where local temporary storage is unnecessary.

**Specific Features and Detailed Changes:**  
The update introduces diskless compute options based on Intel and AMD v5 processors. These options are available in both General Purpose and Memory Optimized SKUs. The primary change is the removal of local temporary storage from these SKUs, which distinguishes them from traditional compute tiers that typically include ephemeral disk storage. This enables customers to provision database servers with compute resources only, without allocating local temporary disks.

**Technical Mechanisms and Implementation Methods:**  
The diskless tier leverages Azure’s v5 generation compute infrastructure, utilizing Intel and AMD processors for improved performance and scalability. By omitting local temporary storage, these SKUs streamline the deployment process and reduce potential overhead associated with managing ephemeral storage. The implementation is integrated into the Azure Database for PostgreSQL Flexible Server provisioning workflow, allowing users to select diskless compute SKUs directly from the Azure portal, CLI, or ARM templates.

**Use Cases and Application Scenarios:**  
Diskless compute tiers are ideal for workloads that do not require local temporary storage, such as applications with stateless processing or those relying solely on persistent storage. Common scenarios include:
- Production workloads with strict data durability requirements.
- Environments where temporary storage is managed externally or is unnecessary.
- Cost-sensitive deployments where eliminating local temporary storage reduces resource consumption and potential costs.

**Important Considerations and Limitations:**  
When utilizing diskless compute SKUs, customers should be aware that no local temporary storage is provisioned. This means that operations or workloads that depend on local ephemeral storage for caching, sorting, or temporary file operations will not have access to such resources. It is essential to review workload requirements and ensure that all temporary data needs are met through other means, such as persistent storage or external caching solutions. Additionally, the update applies specifically to the v5 compute portfolio within Azure Database for PostgreSQL Flexible Server.

**Integration with Related Azure Services:**  
The diskless compute SKUs are fully integrated with Azure Database for PostgreSQL Flexible Server and can be managed using standard Azure tools and APIs. They support integration with other Azure services such as Azure Backup, Azure Monitor, and Azure Security Center, ensuring that customers can maintain operational visibility, security, and compliance across their deployments. The diskless tier aligns with Azure’s broader compute and storage offerings, providing flexibility for customers to optimize their database infrastructure.

**Summary Sentence:**  
Azure Database for PostgreSQL Flexible Server now offers generally available Intel and AMD v5 diskless compute tiers, expanding the v5 portfolio with General Purpose and Memory Optimized SKUs that omit local temporary storage, enabling tailored deployments for workloads that do not require ephemeral disk resources.

---

### 6. Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL 

**Published**: November 17, 2026 23:50:40 UTC
**Link**: [Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=579585)

**Update ID**: 579585
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now offers Cobalt 200 ARM-based compute as generally available.

- Key changes or new features  
Cobalt 200 introduces Microsoft-designed ARM64-based compute options to the Flexible Server platform. This expands the available compute architectures beyond traditional x86, enabling improved price-performance and energy efficiency. Customers can now choose Cobalt 200 for their PostgreSQL workloads, benefiting from optimized performance and potentially lower costs.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL Flexible Server instances, especially those seeking cost-effective, scalable, and energy-efficient compute options for their database workloads.

- Important notes  
Cobalt 200 ARM-based compute is fully supported and available for production workloads. It is compatible with PostgreSQL Flexible Server features and offers seamless migration from existing compute options. Users should evaluate workload compatibility with ARM architecture and test performance before migrating. For more details and guidance, refer to the official Azure documentation.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Cobalt 200 compute for Azure Database for PostgreSQL

**Background and Purpose of the Update:**  
Azure Database for PostgreSQL Flexible Server has announced the general availability of Cobalt 200 ARM-based compute. This update is part of Microsoft’s ongoing efforts to diversify and optimize its compute offerings for managed PostgreSQL services. The introduction of Cobalt 200 expands the available compute architectures, allowing customers to leverage Microsoft-designed ARM64-based compute in addition to existing options. The primary purpose is to provide more flexibility, potentially improve performance-to-cost ratios, and support a wider range of workloads and deployment preferences.

**Specific Features and Detailed Changes:**  
- **Cobalt 200 ARM-based Compute:** The update introduces Cobalt 200, a new ARM64-based compute option designed by Microsoft, to the Azure Database for PostgreSQL Flexible Server portfolio.
- **General Availability:** Cobalt 200 is now generally available, meaning it is fully supported and ready for production workloads.
- **Expanded Compute Portfolio:** Customers now have the choice between traditional x86-based compute and ARM64-based Cobalt 200 compute for their PostgreSQL Flexible Server instances.

**Technical Mechanisms and Implementation Methods:**  
- **ARM64 Architecture:** Cobalt 200 utilizes ARM64 architecture, which is known for its energy efficiency and performance characteristics. Microsoft has designed this compute platform to optimize for cloud workloads.
- **Flexible Server Integration:** The Cobalt 200 compute option is seamlessly integrated into the Flexible Server provisioning workflow. When creating or scaling a PostgreSQL Flexible Server, users can select Cobalt 200 as their compute tier.
- **Compatibility:** The ARM64-based Cobalt 200 compute is engineered to be compatible with PostgreSQL workloads, ensuring that applications and extensions supported by Flexible Server continue to function as expected.

**Use Cases and Application Scenarios:**  
- **Cost Optimization:** Organizations seeking to optimize their cloud spending may benefit from ARM64’s improved performance-per-dollar characteristics.
- **Modern Workloads:** Cobalt 200 is suitable for modern, cloud-native applications that can leverage ARM architecture.
- **Development and Testing:** Teams can use Cobalt 200 for development and testing environments to evaluate performance and compatibility before deploying to production.
- **Production Deployments:** With general availability, Cobalt 200 is appropriate for production workloads that require high availability, scalability, and managed PostgreSQL services.

**Important Considerations and Limitations:**  
- **Architecture Differences:** While Cobalt 200 is designed for compatibility, users should validate their applications and extensions for ARM64 architecture, as some third-party software may have x86-specific dependencies.
- **Migration:** Existing Flexible Server instances may require migration or re-provisioning to take advantage of Cobalt 200 compute.
- **Performance Characteristics:** It is recommended to benchmark workloads on Cobalt 200 to ensure optimal performance and compatibility.

**Integration with Related Azure Services:**  
- **Azure Database for PostgreSQL Flexible Server:** Cobalt 200 is directly integrated into the Flexible Server offering, supporting all standard management, backup, scaling, and monitoring features.
- **Azure Portal and CLI:** Users can provision and manage Cobalt 200 compute instances through the Azure Portal, CLI, and ARM templates, ensuring consistent integration with Azure management tools.
- **Ecosystem Compatibility:** Cobalt 200 compute works with other Azure services commonly used with PostgreSQL Flexible Server, such as Azure Monitor, Azure Backup, and networking services.

**Summary Sentence:**  
Azure Database for PostgreSQL Flexible Server now offers the generally available Cobalt 200 ARM64-based compute, expanding architectural choices and enabling customers to leverage Microsoft-designed ARM compute for optimized PostgreSQL workloads in production environments.

---

### 7. Generally Available: Geo-redundant backup and restore for Azure HorizonDB

**Published**: November 17, 2026 23:47:55 UTC
**Link**: [Generally Available: Geo-redundant backup and restore for Azure HorizonDB](https://azure.microsoft.com/updates?id=574168)

**Update ID**: 574168
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Geo-redundant backup and restore functionality is now generally available for Azure HorizonDB.

- Key changes or new features  
This update enables users to create geo-redundant backups of their HorizonDB deployments. These backups can be used to restore HorizonDB instances in a different Azure region, enhancing disaster recovery and business continuity capabilities. The feature provides an additional layer of data protection by ensuring that backups are stored in geographically separate locations.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB databases, especially those responsible for data protection, backup strategies, and disaster recovery planning.

- Important notes if any  
Geo-redundant backup and restore is recommended for organizations requiring high availability and resilience against regional outages. Ensure that backup and restore processes are integrated into your operational workflows. Review Azure documentation for configuration steps and any associated costs with geo-redundant storage.

For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=574168

**Details**:

**Azure Update Report: Geo-redundant backup and restore for Azure HorizonDB (Generally Available)**  
[Source Link](https://azure.microsoft.com/updates?id=574168)

---

**Background and Purpose of the Update**  
This update introduces geo-redundant backup and restore capabilities for Azure HorizonDB, now generally available. The primary purpose is to enhance data protection and business continuity for HorizonDB deployments by enabling organizations to safeguard their data against regional outages and disasters. Geo-redundancy ensures that backup data is stored in multiple Azure regions, allowing for restoration in a different region if the primary region becomes unavailable.

**Specific Features and Detailed Changes**  
- **Geo-redundant Backup:** HorizonDB now supports geo-redundant backups, meaning backup data is replicated across geographically separated Azure regions.
- **Cross-region Restore:** Customers can restore their HorizonDB deployment in another Azure region using these geo-redundant backups, providing a robust disaster recovery solution.
- **Data Protection Enhancement:** The update adds an additional layer of resilience, supplementing existing backup and restore options with cross-region capabilities.

**Technical Mechanisms and Implementation Methods**  
- **Backup Replication:** When geo-redundant backup is enabled, HorizonDB automatically replicates backup data to a secondary Azure region. This replication is managed by Azure’s underlying infrastructure, ensuring data consistency and integrity.
- **Restore Workflow:** In the event of a regional failure or planned migration, administrators can initiate a restore operation in a different Azure region using the geo-redundant backup. The process leverages Azure’s secure transfer mechanisms to ensure data is restored accurately and efficiently.
- **Configuration:** Geo-redundant backup is configurable through HorizonDB management interfaces, allowing IT professionals to specify target regions and manage backup schedules.

**Use Cases and Application Scenarios**  
- **Disaster Recovery:** Organizations can recover HorizonDB deployments in a secondary Azure region if the primary region experiences an outage, minimizing downtime and data loss.
- **Regulatory Compliance:** Geo-redundant backups help meet compliance requirements for data durability and protection across multiple geographic locations.
- **Migration and Testing:** IT teams can use geo-redundant backups to restore HorizonDB in another region for migration, testing, or staging purposes without impacting production workloads.

**Important Considerations and Limitations**  
- **Backup Frequency and Latency:** The frequency and latency of backup replication may affect recovery point objectives (RPO). IT professionals should review HorizonDB documentation for specifics on replication intervals.
- **Cost Implications:** Geo-redundant backups may incur additional storage and transfer costs due to cross-region replication.
- **Restore Limitations:** Restoring to another region is subject to Azure’s regional availability and quota constraints. Ensure the target region supports HorizonDB and has sufficient resources.
- **Security:** Backup data is protected by Azure’s encryption and access controls, but administrators must ensure proper configuration to maintain compliance and security.

**Integration with Related Azure Services**  
- **Azure Backup:** Geo-redundant backup for HorizonDB integrates with Azure’s broader backup ecosystem, leveraging Azure Backup’s infrastructure for replication and recovery.
- **Azure Site Recovery:** While Azure Site Recovery focuses on VM and workload failover, geo-redundant backup for HorizonDB complements these services by providing database-level disaster recovery.
- **Monitoring and Alerts:** Integration with Azure Monitor and Azure Security Center enables tracking of backup status, alerts, and compliance reporting.

---

**Summary Sentence:**  
Geo-redundant backup and restore for Azure HorizonDB is now generally available, providing enhanced data protection and disaster recovery by enabling cross-region backup replication and restoration capabilities for HorizonDB deployments.

---

### 8. Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB

**Published**: November 17, 2026 23:46:26 UTC
**Link**: [Generally Available: Customize backup retention from 1 to 35 days in Azure HorizonDB](https://azure.microsoft.com/updates?id=574163)

**Update ID**: 574163
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now supports customizable backup retention periods.

- Key changes or new features  
You can configure backup retention for Azure HorizonDB deployments anywhere from 1 to 35 days. This allows you to tailor backup retention settings to meet specific application needs and data protection policies.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB deployments, especially those responsible for backup strategies and compliance.

- Important notes  
This update provides greater flexibility for backup management, enabling organizations to optimize storage costs and compliance requirements. Adjusting retention periods can help meet regulatory requirements or internal policies for data retention and recovery. The feature is generally available and can be configured directly in your HorizonDB deployment settings.  
For more details, visit the [Azure Update](https://azure.microsoft.com/updates?id=574163).

**Details**:

**Azure Update Report: Backup Retention Customization in Azure HorizonDB**

**Background and Purpose of the Update**  
Previously, Azure HorizonDB offered limited options for backup retention, which could restrict organizations in tailoring their data protection strategies to specific compliance, operational, or business requirements. The purpose of this update is to provide greater flexibility by allowing users to configure backup retention periods according to their unique needs, enhancing both operational agility and adherence to data governance policies.

**Specific Features and Detailed Changes**  
With this update, Azure HorizonDB now supports configurable backup retention periods ranging from 1 to 35 days. This feature enables administrators to select any retention duration within this range for their HorizonDB deployments. The change is generally available, meaning it is accessible to all users of Azure HorizonDB without restrictions. The configuration can be applied per deployment, allowing granular control over backup policies.

**Technical Mechanisms and Implementation Methods**  
The backup retention setting is managed through the Azure HorizonDB interface, either via the Azure Portal or programmatically using Azure APIs or CLI tools. When a backup is created, the system tags it with the specified retention period. Azure HorizonDB’s backup management subsystem automatically purges backups once their retention period expires, ensuring compliance with the configured policy and optimizing storage usage. The retention configuration is likely stored as metadata associated with each backup, and the cleanup process is handled by Azure’s managed backup lifecycle engine.

**Use Cases and Application Scenarios**  
- **Compliance and Regulatory Requirements:** Organizations subject to strict data retention policies can now configure retention periods to meet legal or regulatory mandates.
- **Development and Testing:** Short retention periods (e.g., 1-7 days) are useful for non-production environments where frequent changes and rapid cleanup are required.
- **Production Workloads:** Longer retention periods (up to 35 days) can be set for critical workloads to ensure data recovery options are available for extended periods.
- **Cost Optimization:** By reducing unnecessary backup retention, organizations can minimize storage costs while maintaining adequate data protection.

**Important Considerations and Limitations**  
- The retention period must be set between 1 and 35 days; values outside this range are not supported.
- Backup deletion is automatic and irreversible once the retention period expires, so administrators must carefully select retention settings to avoid unintended data loss.
- This update does not alter backup frequency or backup creation mechanisms; it solely affects how long backups are retained.
- There is no mention of advanced retention policies (such as tiered or conditional retention), so only fixed-duration retention is supported.

**Integration with Related Azure Services**  
The backup retention customization feature integrates seamlessly with Azure HorizonDB’s managed backup system. It is compatible with Azure’s monitoring and alerting tools, enabling administrators to track backup status and retention compliance. The feature can be managed alongside other Azure services, such as Azure Policy for governance and Azure Resource Manager for automation, ensuring consistent backup management across the Azure ecosystem.

**Summary Sentence**  
Azure HorizonDB now allows users to customize backup retention periods from 1 to 35 days, providing enhanced flexibility to align data protection strategies with specific operational and compliance requirements.

---

### 9. Generally Available: Throughput buckets in Azure Cosmos DB 

**Published**: November 17, 2026 23:44:26 UTC
**Link**: [Generally Available: Throughput buckets in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=571488)

**Update ID**: 571488
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cosmos DB now offers throughput buckets as a generally available feature.

- Key changes or new features  
Throughput buckets allow you to manage and limit the maximum throughput (RU/s) that individual workloads can consume when sharing the same container. This feature helps prevent resource contention and ensures fair allocation of resources across multiple workloads. Developers can configure throughput limits for different workloads using the API, enabling more granular control over resource consumption.

- Target audience affected  
Developers and IT professionals managing multi-tenant or multi-workload applications in Azure Cosmos DB, especially those using shared containers.

- Important notes if any  
Throughput buckets are useful for scenarios where multiple workloads access the same container and you want to avoid one workload monopolizing resources. This feature is accessible via API and can help optimize performance and cost management. Review documentation for implementation details and best practices.

**Details**:

**Azure Update Report: Generally Available – Throughput Buckets in Azure Cosmos DB**

**Background and Purpose of the Update**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for high performance and scalability. Managing resource consumption across multiple workloads sharing the same container has traditionally posed challenges, especially in multi-tenant environments or scenarios with diverse workload profiles. The introduction of throughput buckets addresses the need for granular control over resource allocation, enabling organizations to prevent any single workload from monopolizing container throughput and to optimize overall performance and cost management.

**Specific Features and Detailed Changes**  
With throughput buckets now generally available, Azure Cosmos DB allows administrators to set a maximum throughput limit for individual workloads operating within the same container. This feature provides a mechanism to partition and restrict the throughput (measured in Request Units per second, RU/s) that each workload can consume. By defining throughput boundaries, organizations can ensure fair resource distribution and prevent performance degradation caused by resource-intensive workloads.

**Technical Mechanisms and Implementation Methods**  
Throughput buckets are implemented as configurable limits at the workload level within a Cosmos DB container. Administrators can assign a maximum RU/s value to each workload, effectively creating a logical bucket that caps the throughput consumption. The Cosmos DB engine enforces these limits during runtime, ensuring that requests from each workload do not exceed their allocated throughput. This mechanism is transparent to the application and does not require changes to the underlying data model or container configuration. The enforcement is managed through Cosmos DB’s internal request routing and resource management subsystems.

**Use Cases and Application Scenarios**  
- **Multi-Tenant Applications:** Organizations hosting multiple tenants in a single Cosmos DB container can use throughput buckets to allocate dedicated throughput to each tenant, ensuring isolation and predictable performance.
- **Diverse Workload Management:** When running batch processing, analytics, and transactional workloads concurrently, throughput buckets prevent high-throughput jobs from impacting latency-sensitive operations.
- **Cost Optimization:** By capping throughput per workload, organizations can avoid unexpected spikes in resource usage and associated costs, maintaining budgetary control.
- **Resource Governance:** Throughput buckets enable compliance with internal or external resource usage policies, supporting governance and audit requirements.

**Important Considerations and Limitations**  
- Throughput buckets are limited to controlling maximum throughput per workload; they do not provide minimum guaranteed throughput or reservation.
- Proper configuration is essential to avoid underutilization or bottlenecks; administrators should monitor workload patterns and adjust buckets accordingly.
- The feature is applicable only to workloads sharing the same container; separate containers require independent throughput management.
- Integration and compatibility with existing Cosmos DB features (such as autoscale throughput) should be validated in production environments.

**Integration with Related Azure Services**  
Throughput buckets can be used in conjunction with Azure monitoring tools, such as Azure Monitor and Application Insights, to track workload-specific throughput consumption and optimize bucket configurations. They complement existing Cosmos DB resource management features, providing an additional layer of control for organizations leveraging Azure’s ecosystem for scalable, multi-tenant, or high-performance applications.

**Summary Sentence**  
Throughput buckets in Azure Cosmos DB, now generally available, enable administrators to limit the maximum throughput consumed by individual workloads sharing a container, providing granular resource management, improved performance isolation, and enhanced cost control for multi-tenant and diverse workload scenarios.

---

### 10. Limited Preview: AI model management in Azure HorizonDB

**Published**: November 17, 2026 23:42:10 UTC
**Link**: [Limited Preview: AI model management in Azure HorizonDB](https://azure.microsoft.com/updates?id=563097)

**Update ID**: 563097
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now offers limited preview for integrated AI model management.

- Key changes or new features  
This update introduces a streamlined process to provision fully managed AI models directly within Azure HorizonDB. Supported models cover embeddings, semantic ranking, and generative tasks. Developers can enable these models in their database with a single step, leveraging Microsoft’s managed infrastructure for deployment, scaling, and lifecycle management. The integration allows for enhanced search, ranking, and content generation capabilities within database workloads, reducing the complexity of external AI model orchestration.

- Target audience affected  
This preview is relevant for developers and IT professionals working with Azure HorizonDB, especially those building applications requiring advanced AI features such as semantic search, ranking, and generative AI. Database administrators and architects seeking to integrate AI into data-driven solutions will benefit from simplified model management.

- Important notes  
The feature is currently in limited preview, so access may be restricted and subject to change. Early adopters should review documentation for supported model types, API usage, and pricing. Feedback during the preview will help shape future enhancements. For more details and participation, refer to the official Azure Update link.

**Details**:

**Azure Update Report: Limited Preview – AI Model Management in Azure HorizonDB**

**Background and Purpose of the Update**  
This update introduces AI model management capabilities in Azure HorizonDB, now available in limited preview. The primary purpose is to streamline and simplify the integration of AI functionalities directly within the database environment. By enabling managed AI models, Azure aims to reduce operational complexity for IT professionals and developers, allowing them to leverage AI for data processing and analysis without extensive infrastructure setup or maintenance.

**Specific Features and Detailed Changes**  
The limited preview allows users to provision fully managed AI models in Azure HorizonDB with a single step. Supported AI functionalities include embeddings, semantic ranking, and generation. These features are designed to enhance data processing workflows by enabling advanced AI-driven operations such as semantic search, content ranking, and generative tasks directly within the database. The update eliminates the need for manual model deployment, configuration, and lifecycle management, providing a seamless experience for integrating AI models.

**Technical Mechanisms and Implementation Methods**  
AI model management in HorizonDB is implemented as a managed service, meaning Microsoft handles model hosting, scaling, and maintenance. Users can provision models through the Azure portal or API, with the process abstracted to a single step. The models are integrated natively within HorizonDB, allowing database operations to invoke AI functionalities such as embeddings for vector search, semantic ranking for relevance scoring, and generation for content creation. This is achieved through built-in endpoints or procedures, minimizing the need for external orchestration or custom code.

**Use Cases and Application Scenarios**  
Typical use cases include:  
- **Semantic Search:** Utilizing embeddings to enable vector-based search and retrieval of similar content within the database.  
- **Content Ranking:** Applying semantic ranking models to sort and prioritize results based on relevance, improving user experience in applications such as e-commerce or document management.  
- **Content Generation:** Leveraging generative models to automatically produce summaries, recommendations, or other content directly from database records.  
These scenarios are particularly valuable in applications where AI-driven insights and automation can enhance data-driven decision-making and user engagement.

**Important Considerations and Limitations**  
As this feature is in limited preview, access may be restricted and subject to Microsoft’s approval. The scope of supported AI models and functionalities is limited to embeddings, semantic ranking, and generation as described. Users should be aware of potential constraints regarding scalability, performance, and model customization during the preview phase. Additionally, operational and security best practices should be followed, especially when handling sensitive data or integrating AI models with production workloads.

**Integration with Related Azure Services**  
AI model management in HorizonDB is designed to work seamlessly with other Azure services. It leverages Azure’s managed infrastructure for model hosting and integrates with the Azure portal for provisioning and monitoring. While the update focuses on HorizonDB, it is expected to complement existing Azure AI and data services, enabling unified workflows across Azure’s ecosystem for data storage, processing, and AI-driven analytics.

**Summary Sentence**  
AI model management in Azure HorizonDB, now in limited preview, enables IT professionals to provision fully managed AI models for embeddings, semantic ranking, and generation in a single step, simplifying AI integration and enhancing database-driven applications.

---

### 11. Generally Available: Semantic Reranker in Azure Cosmos DB 

**Published**: November 17, 2026 23:07:42 UTC
**Link**: [Generally Available: Semantic Reranker in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=577520)

**Update ID**: 577520
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Semantic Reranker is now generally available in Azure Cosmos DB.

- Key changes or new features  
The Semantic Reranker feature leverages an AI model to enhance search relevance within Azure Cosmos DB. It reorders candidate search results by analyzing the meaning of the search text and its context, rather than relying solely on keyword matching. This results in more accurate and contextually relevant search outcomes, as documents that best match the user’s intent are promoted in the results.

- Target audience affected  
This update is particularly relevant for developers and IT professionals building applications with Azure Cosmos DB that require advanced search capabilities. Teams working on search-driven user experiences or integrating AI-powered search in their applications will benefit from improved result relevance.

- Important notes if any  
Semantic Reranker can be accessed via API and is designed to work seamlessly with existing Cosmos DB search workloads. It is recommended for scenarios where understanding user intent and delivering high-quality search results is critical. No additional infrastructure changes are required, but developers should review documentation for integration details and best practices.

**Details**:

**Azure Update Report: Semantic Reranker in Azure Cosmos DB (Generally Available)**

**Background and Purpose of the Update**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for high-performance and scalable applications. Traditionally, search operations in Cosmos DB relied on keyword-based ranking, which often failed to capture the true intent or semantic meaning behind user queries. The introduction of the Semantic Reranker addresses this gap by leveraging AI to enhance search relevance, ensuring that results are not only matched by keywords but also by their contextual meaning.

**Specific Features and Detailed Changes**  
The Semantic Reranker feature is now generally available in Azure Cosmos DB. It introduces an AI-driven mechanism that reorders candidate search results based on the semantic meaning of the search text and its surrounding context. Instead of simply returning documents that match keywords, the reranker evaluates the content of candidate documents and promotes those that best align with the user's intent. This results in improved search accuracy and user satisfaction, especially in scenarios where nuanced understanding of queries is required.

**Technical Mechanisms and Implementation Methods**  
The Semantic Reranker utilizes an AI model to process both the search query and the candidate documents. The model analyzes the semantic relationships and context, scoring each candidate for relevance. The reranker then reorders the results, placing the most contextually relevant documents at the top. This process is integrated into the Cosmos DB search workflow, allowing developers to enable semantic reranking as part of their query operations. The implementation is seamless and does not require manual tuning of the AI model, as it is managed by Azure.

**Use Cases and Application Scenarios**  
- **Enterprise Search:** Organizations can use semantic reranking to improve internal document search, ensuring employees find the most relevant information quickly.
- **E-commerce:** Product searches can be enhanced to better match user intent, leading to higher conversion rates.
- **Knowledge Management:** Semantic reranking helps users discover contextually relevant articles, FAQs, or documentation.
- **Customer Support:** Support ticket searches can be optimized to surface the most pertinent solutions or responses.

**Important Considerations and Limitations**  
- The Semantic Reranker is available as a generally available feature, indicating production readiness.
- The feature relies on Azure-managed AI models, so customization of the underlying model is not supported.
- Performance may vary depending on the volume of candidate documents and the complexity of queries.
- Semantic reranking may introduce additional latency compared to traditional keyword-based ranking due to AI processing.
- Users should review documentation for any quota, pricing, or regional availability constraints.

**Integration with Related Azure Services**  
The Semantic Reranker is tightly integrated with Azure Cosmos DB. It complements existing search and indexing capabilities, enabling richer search experiences without external AI infrastructure. While the update does not specify integration with other Azure services, the feature can be used in conjunction with Azure Cognitive Search and other analytics services to build comprehensive, intelligent search solutions across the Azure ecosystem.

**Summary Sentence**  
Semantic Reranker in Azure Cosmos DB is now generally available, providing AI-powered search relevance by reordering results based on semantic meaning and context, thereby enhancing the accuracy and usefulness of search operations for enterprise and application scenarios.

---

### 12. Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class 

**Published**: November 17, 2026 23:00:02 UTC
**Link**: [Public Preview: Pod Sandboxing kata-vm-isolation-v2 runtime class ](https://azure.microsoft.com/updates?id=581120)

**Update ID**: 581120
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite, Feature

**Summary**:

**What was updated**  
Azure Kubernetes Service (AKS) introduces the public preview of the kata-vm-isolation-v2 runtime class for pod sandboxing.

**Key changes or new features**  
- The kata-vm-isolation-v2 runtime class enables improved pod isolation using Kata Containers, without the typical tradeoff between security and startup performance.
- Unlike classic sandboxed pod flows (where each pod boots a new Kata VM, causing cold-start latency and higher memory overhead), the new runtime class optimizes startup times and reduces resource consumption.
- This allows pods to achieve strong VM-level isolation with faster startup and lower memory usage, making it suitable for workloads requiring enhanced security without sacrificing performance.

**Target audience affected**  
- Developers deploying sensitive or multi-tenant workloads on AKS that require strong isolation.
- IT professionals and platform engineers managing AKS clusters and optimizing for security, performance, and resource efficiency.

**Important notes**  
- This feature is currently in public preview and may not be recommended for production workloads.
- Users should review documentation and test compatibility with their applications before adoption.
- For more details and guidance, refer to the official Azure Update: [kata-vm-isolation-v2 runtime class](https://azure.microsoft.com/updates?id=581120).

**Details**:

**Azure Update Technical Report: Public Preview – Pod Sandboxing kata-vm-isolation-v2 Runtime Class**

**Background and Purpose of the Update**  
The update introduces the kata-vm-isolation-v2 runtime class for pod sandboxing in Azure Kubernetes Service (AKS). Traditionally, sandboxed pods have relied on the Kata Containers runtime, which launches a dedicated virtual machine (VM) for each pod. While this approach enhances security by isolating workloads, it imposes a significant cold-start latency and increased memory overhead, as each pod must wait for its VM to boot before application processes can begin. The purpose of this update is to address these performance drawbacks, enabling isolated pods to achieve improved startup times and resource efficiency without compromising security.

**Specific Features and Detailed Changes**  
- **kata-vm-isolation-v2 Runtime Class:** This new runtime class is now available in public preview. It is designed to optimize the pod sandboxing experience by reducing the cold-start latency and memory overhead associated with classic Kata VM flows.
- **Improved Startup Performance:** Unlike the previous model, which boots a new VM for every pod, the v2 runtime class streamlines the initialization process, allowing applications within isolated pods to start faster.
- **Resource Efficiency:** The update minimizes the extra memory consumption typically incurred by launching multiple VMs, making it more scalable for workloads requiring high pod density.

**Technical Mechanisms and Implementation Methods**  
The kata-vm-isolation-v2 runtime class leverages advancements in the Kata Containers technology stack. Instead of spawning a new VM per pod, it likely utilizes optimized VM management and resource sharing techniques (as implied by the reduction in cold-start and memory overhead). This runtime class can be specified in the pod manifest using the `runtimeClassName` field, allowing Kubernetes to schedule the pod with the desired isolation level. The implementation ensures that security boundaries are maintained while improving operational efficiency.

**Use Cases and Application Scenarios**  
- **Multi-Tenant Workloads:** Organizations hosting sensitive workloads from multiple tenants can use the kata-vm-isolation-v2 runtime class to ensure strong isolation without sacrificing performance.
- **Regulated Environments:** Industries requiring compliance with strict security standards (e.g., finance, healthcare) can benefit from secure pod sandboxing with improved startup times.
- **High-Density Deployments:** Applications that require rapid scaling and high pod density, such as microservices or batch processing jobs, can leverage this runtime class to optimize resource utilization.

**Important Considerations and Limitations**  
- **Public Preview:** The kata-vm-isolation-v2 runtime class is currently in public preview, which means it may not be suitable for production workloads until it reaches general availability.
- **Compatibility:** Users should verify compatibility with their existing AKS cluster configurations and ensure that their workloads are tested with the new runtime class.
- **Resource Management:** While memory overhead is reduced, users should monitor resource consumption and performance metrics to ensure optimal operation.

**Integration with Related Azure Services**  
The kata-vm-isolation-v2 runtime class integrates seamlessly with Azure Kubernetes Service (AKS), allowing users to specify pod isolation requirements within their Kubernetes manifests. It supports existing AKS cluster management workflows and can be combined with Azure’s monitoring, security, and compliance solutions to provide end-to-end workload protection and visibility.

**Summary Sentence:**  
The public preview of the kata-vm-isolation-v2 runtime class in Azure Kubernetes Service offers improved pod isolation with enhanced startup performance and reduced memory overhead, enabling secure and efficient deployment of sensitive workloads in AKS environments.

---

### 13. Pulic Preview: Azure Elastic SAN Next Generation

**Published**: November 17, 2026 22:54:18 UTC
**Link**: [Pulic Preview: Azure Elastic SAN Next Generation](https://azure.microsoft.com/updates?id=581634)

**Update ID**: 581634
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Elastic SAN, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Elastic SAN Next Generation is now available in public preview.

- Key changes or new features  
The Next Generation of Azure Elastic SAN retains the core benefits of the original Elastic SAN, including a unified SAN resource hierarchy for consolidating block storage workloads and dynamic performance sharing across workloads. New enhancements focus on improved scalability, simplified management, and optimized performance for large-scale cloud deployments. The update also aims to streamline provisioning and support more advanced storage scenarios, making it easier to manage and allocate resources for multiple applications.

- Target audience affected  
Developers and IT professionals managing large-scale storage workloads in Azure, especially those requiring high-performance block storage for databases, virtual machines, and containerized applications.

- Important notes if any  
The public preview allows users to test and provide feedback on the new features before general availability. Existing Elastic SAN users can evaluate migration paths and compatibility. Azure Elastic SAN Next Generation is designed to support demanding enterprise workloads and offers improved flexibility for scaling storage resources. For more details and participation instructions, refer to the official Azure update announcement.

**Details**:

**Azure Update Technical Report: Public Preview – Azure Elastic SAN Next Generation**

**Background and Purpose of the Update**  
Azure Elastic SAN Next Generation has entered public preview. The purpose of this update is to build upon the existing Azure Elastic SAN offering, preserving its core benefits while introducing enhancements. Elastic SAN is designed to provide a unified SAN resource hierarchy, enabling organizations to consolidate block storage workloads and dynamically share performance across multiple workloads. This update aims to further streamline storage management and optimize resource utilization in cloud environments.

**Specific Features and Detailed Changes**  
The Next Generation of Azure Elastic SAN maintains the foundational features of the current Elastic SAN service. These include:
- **Single SAN Resource Hierarchy:** Centralized management of block storage resources, allowing IT teams to organize and allocate storage efficiently.
- **Consolidation of Block Storage Workloads:** Multiple workloads can be hosted on a single SAN resource, reducing storage silos and simplifying administration.
- **Dynamic Performance Sharing:** Performance resources can be dynamically allocated and shared among workloads, improving overall storage efficiency and responsiveness.

The public preview introduces enhancements that retain these benefits, though specific new features or changes beyond the core capabilities are not detailed in the provided information.

**Technical Mechanisms and Implementation Methods**  
Azure Elastic SAN Next Generation operates as a cloud-native SAN solution within Azure, leveraging Azure’s infrastructure to deliver scalable and flexible block storage. The SAN resource hierarchy allows for logical grouping and management of volumes, enabling dynamic allocation of performance and capacity. The service is designed to support dynamic performance sharing, which means that performance (IOPS and throughput) can be distributed among workloads as needed, rather than being statically assigned.

**Use Cases and Application Scenarios**  
Typical scenarios for Azure Elastic SAN Next Generation include:
- **Enterprise Storage Consolidation:** Organizations can migrate on-premises SAN workloads to Azure, centralizing management and reducing operational overhead.
- **Dynamic Workload Management:** Environments with fluctuating storage performance demands benefit from the ability to dynamically share performance resources.
- **Multi-Application Hosting:** Multiple applications or services can share a single SAN resource, simplifying storage provisioning and scaling.

**Important Considerations and Limitations**  
As this is a public preview, IT professionals should be aware of potential limitations such as:
- **Preview Service Constraints:** Features may be subject to change, and not all production-level capabilities may be available.
- **Support and SLAs:** Preview services typically offer limited support and do not carry the same SLAs as generally available (GA) services.
- **Compatibility:** Integration with existing workloads should be tested to ensure compatibility with the Next Generation features.

**Integration with Related Azure Services**  
Azure Elastic SAN Next Generation integrates with the broader Azure ecosystem, supporting block storage workloads for Azure Virtual Machines and other compute services. The centralized SAN resource can be managed via Azure Portal, CLI, or API, aligning with standard Azure management practices. It is designed to complement other Azure storage offerings, enabling hybrid and cloud-native storage architectures.

**Summary Sentence**  
Azure Elastic SAN Next Generation, now in public preview, enhances the consolidation and dynamic performance sharing of block storage workloads through a unified SAN resource hierarchy, supporting efficient storage management and integration within the Azure ecosystem.

---

### 14. Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent

**Published**: November 17, 2026 22:48:10 UTC
**Link**: [Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent](https://azure.microsoft.com/updates?id=581209)

**Update ID**: 581209
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft announced a limited preview of the Azure Workload Center for SAP and the Azure Copilot Run SAP Agent. This update introduces a workload-aware management experience for SAP workloads on Azure, leveraging Workload Virtual Instance (WVI) technology.

- Key changes or new features  
The Azure Workload Center for SAP provides enhanced visibility and operational insights into SAP workloads running on Azure. It integrates with the Azure Copilot Run SAP Agent, enabling intelligent assistance for SAP workload management. Features include workload health monitoring, guided troubleshooting, and recommendations for optimizing SAP operations. The solution is powered by WVI, which allows for more granular control and management of SAP resources.

- Target audience affected  
This update is relevant for SAP administrators, IT professionals managing SAP environments, and developers working with SAP on Azure. It is particularly useful for teams seeking improved operational efficiency and automation for SAP workloads.

- Important notes if any  
The preview is currently limited and may require registration or approval to access. Users should review documentation for compatibility and prerequisites before onboarding. The integration with Azure Copilot provides AI-driven guidance, but full functionality may depend on the scope of the preview.

**Details**:

**Azure Update Summary: Limited Preview: Azure Workload Center for SAP and Azure Copilot Run SAP Agent**

**Background and Purpose of the Update**  
This update introduces the limited preview of the Azure Workload Center for SAP, in conjunction with the Azure Copilot Run SAP Agent. The primary purpose is to provide a workload-aware operational experience for SAP workloads on Azure. This is achieved by leveraging the Workload Virtual Instance (WVI) framework, which is designed to enhance visibility and manageability of SAP environments hosted on Azure.

**Specific Features and Detailed Changes**  
- **Azure Workload Center for SAP:** Offers a centralized interface tailored for SAP workloads, enabling teams to gain insights into workload health and operational status.
- **Azure Copilot Run SAP Agent:** Integrates with the Workload Center to provide intelligent, context-aware operational assistance for SAP workloads.
- **Workload Virtual Instance (WVI):** Serves as the underlying abstraction layer that models SAP workloads, facilitating workload-centric monitoring and management.

**Technical Mechanisms and Implementation Methods**  
- The solution is powered by the Workload Virtual Instance (WVI), which abstracts SAP workload components running on Azure. This abstraction allows Azure-native tools to interact with SAP workloads in a workload-aware manner.
- The Azure Copilot Run SAP Agent acts as an intelligent assistant, leveraging AI to provide operational guidance and automate routine tasks within the SAP environment.
- Integration between the Workload Center and the Copilot Run SAP Agent ensures that operational insights and recommendations are contextually relevant to the SAP workload’s current state.

**Use Cases and Application Scenarios**  
- **Operational Monitoring:** IT teams can monitor SAP workload health, performance, and operational status from a centralized Azure portal.
- **Guided Operations:** The Copilot Run SAP Agent provides actionable recommendations and automates common operational tasks, reducing manual effort and risk of errors.
- **Incident Response:** When issues are detected, the system can guide operators through remediation steps specific to SAP workloads, leveraging both Azure and SAP best practices.

**Important Considerations and Limitations**  
- **Limited Preview:** The features are currently available in a limited preview, which may restrict access to selected customers or regions.
- **Scope:** The update is focused specifically on SAP workloads and may not extend to other enterprise workloads at this stage.
- **Integration Requirements:** Proper configuration of the Workload Virtual Instance and deployment of the Copilot Run SAP Agent are prerequisites for full functionality.

**Integration with Related Azure Services**  
- The Workload Center for SAP is designed to integrate with core Azure management and monitoring services, leveraging Azure-native capabilities for resource management, monitoring, and automation.
- The WVI framework allows seamless interaction with Azure Monitor, Azure Automation, and other operational tools, ensuring consistent management across SAP and Azure-native resources.
- The Copilot Run SAP Agent enhances the integration by providing AI-driven operational support, further bridging SAP workload management with Azure’s intelligent platform services.

**Summary Sentence**  
The limited preview of Azure Workload Center for SAP and Azure Copilot Run SAP Agent introduces a workload-aware, AI-powered operational experience for SAP workloads on Azure, leveraging the Workload Virtual Instance framework to enhance visibility, guidance, and automation for SAP operations within the Azure ecosystem.

---

### 15. Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent

**Published**: November 17, 2026 22:46:30 UTC
**Link**: [Limited Preview: Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent](https://azure.microsoft.com/updates?id=581214)

**Update ID**: 581214
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite

**Summary**:

**What was updated:**  
Azure announced a limited preview of the Azure Workload Center for Oracle, integrated with the Azure Copilot Run Oracle Agent.

**Key changes or new features:**  
- Introduction of a workload-aware management experience for Oracle workloads on Azure, powered by Workload Virtual Instance (WVI).
- Azure Workload Center for Oracle provides visibility and operational insights specifically tailored for Oracle workloads.
- Azure Copilot Run Oracle Agent offers intelligent assistance, automating routine tasks and improving operational efficiency for Oracle environments.
- Enhanced monitoring, troubleshooting, and optimization capabilities for Oracle workloads running on Azure.

**Target audience affected:**  
- Developers and IT professionals managing Oracle workloads on Azure.
- Teams responsible for migrating, operating, or optimizing Oracle databases and applications in Azure environments.

**Important notes:**  
- This feature is currently in limited preview; access may be restricted and subject to eligibility.
- The update aims to simplify Oracle workload management, reduce manual intervention, and improve reliability and performance on Azure.
- Interested users should monitor Azure announcements for broader availability and additional documentation.

**Details**:

**Azure Update Report: Limited Preview – Azure Workload Center for Oracle and Azure Copilot Run Oracle Agent**

**Background and Purpose of the Update**  
This update introduces the limited preview of the Azure Workload Center for Oracle, enhanced by the Azure Copilot Run Oracle Agent. The primary purpose is to deliver a workload-aware management experience for Oracle workloads hosted on Azure. The solution leverages the Workload Virtual Instance (WVI) model, aiming to streamline operations, monitoring, and management for teams running Oracle databases and applications in the Azure environment.

**Specific Features and Detailed Changes**  
- **Workload-Aware Experience:** The Azure Workload Center for Oracle provides a centralized interface tailored specifically for Oracle workloads, offering visibility and operational insights.
- **Azure Copilot Run Oracle Agent:** This agent integrates with the Workload Center, enabling automated actions, recommendations, and contextual guidance for Oracle workload management.
- **Powered by Workload Virtual Instance (WVI):** WVI abstracts the Oracle workload as a virtual instance, allowing for enhanced workload-centric operations rather than traditional resource-centric management.
- **Operational Insights:** The platform assists teams in understanding the health, performance, and configuration of their Oracle workloads on Azure.

**Technical Mechanisms and Implementation Methods**  
- **Workload Virtual Instance (WVI):** WVI acts as a logical container for Oracle workloads, encapsulating configuration, state, and operational metadata. This abstraction enables workload-aware operations, such as monitoring, patching, and scaling, directly at the workload level.
- **Azure Copilot Run Oracle Agent:** The agent is deployed alongside Oracle workloads and interacts with the Workload Center. It collects telemetry, executes automated tasks, and delivers actionable recommendations based on workload context.
- **Integration Workflow:** The Workload Center and Copilot Agent communicate via Azure APIs, ensuring secure and scalable orchestration of workload operations.

**Use Cases and Application Scenarios**  
- **Database Operations:** Teams managing Oracle databases on Azure can utilize the Workload Center for centralized monitoring, troubleshooting, and lifecycle management.
- **Performance Optimization:** The Copilot Agent provides recommendations and automates routine tasks, such as tuning and patching, based on workload telemetry.
- **Migration and Modernization:** Organizations migrating Oracle workloads to Azure can leverage WVI for seamless workload abstraction and management during and after migration.
- **Compliance and Governance:** The workload-aware insights support compliance monitoring and governance for Oracle environments.

**Important Considerations and Limitations**  
- **Limited Preview:** The update is currently in limited preview, meaning access is restricted and features may be subject to change.
- **Oracle Workload Support:** The solution is specifically designed for Oracle workloads; applicability to other database platforms is not indicated.
- **Agent Deployment:** Successful utilization requires deployment of the Azure Copilot Run Oracle Agent alongside Oracle workloads.
- **Feature Scope:** Only features described in the preview are available; additional capabilities may be introduced in future releases.

**Integration with Related Azure Services**  
- **Azure Compute and Storage:** Oracle workloads managed via the Workload Center are hosted on Azure infrastructure, leveraging compute and storage services.
- **Azure Monitoring and Management:** The Workload Center integrates with Azure’s monitoring and management APIs, enhancing visibility and operational control.
- **Azure Security:** The solution operates within Azure’s security framework, ensuring secure communication and workload isolation.

**Summary Sentence:**  
Azure Workload Center for Oracle, together with the Azure Copilot Run Oracle Agent, introduces a workload-aware management experience powered by Workload Virtual Instance, enabling teams to efficiently operate, monitor, and optimize Oracle workloads on Azure during its limited preview.

---

### 16. Public Preview: Database Agent for SQL with contextual Copilot 

**Published**: November 17, 2026 22:43:01 UTC
**Link**: [Public Preview: Database Agent for SQL with contextual Copilot ](https://azure.microsoft.com/updates?id=580091)

**Update ID**: 580091
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The Database Agent for SQL now includes contextual Copilot capabilities in public preview, providing AI-generated, evidence-based recommendations for database issues.

- Key changes or new features  
The update introduces Copilot-powered recommendations that explain why an issue matters, its likely cause, and actionable next steps. These suggestions are grounded in real issue evidence and Microsoft’s authoritative knowledge. Developers and IT professionals can leverage these insights directly within the Database Agent for SQL, streamlining troubleshooting and remediation processes.

- Target audience affected  
This update is relevant for database administrators, developers, and IT professionals managing SQL databases on Azure. It benefits teams responsible for database health, performance, and incident resolution.

- Important notes if any  
The feature is currently in public preview, so users should expect ongoing improvements and provide feedback. Recommendations are based on available evidence and Microsoft expertise, but users should validate actions in production environments. Integration with contextual Copilot aims to reduce manual investigation and accelerate resolution of database issues. For more details and access, refer to the official Azure Update announcement.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Database Agent for SQL with contextual Copilot  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=580091)

---

**Background and Purpose of the Update**  
The introduction of the Database Agent for SQL with contextual Copilot addresses the need for intelligent, automated assistance in database management and troubleshooting. As SQL databases are critical to enterprise workloads, timely detection and resolution of issues are essential. This update aims to enhance operational efficiency by providing AI-driven recommendations that are grounded in evidence, thereby reducing manual analysis and accelerating problem resolution.

**Specific Features and Detailed Changes**  
The Database Agent now incorporates contextual Copilot capabilities, delivering AI-generated recommendations for detected database issues. Key features include:

- **Evidence-Grounded Recommendations:** For each detected issue, the agent provides recommendations based on available evidence, ensuring that suggestions are relevant and actionable.
- **Contextual Explanations:** Recommendations include explanations of why the issue matters, the likely cause, and the recommended next step, offering clarity and guidance for remediation.
- **Integration with Microsoft Knowledge:** The agent leverages Microsoft-authored content and best practices to inform its recommendations, enhancing reliability and trustworthiness.

**Technical Mechanisms and Implementation Methods**  
The Database Agent utilizes AI models to analyze database telemetry and issue evidence. Upon detecting an issue, the agent:

1. Aggregates relevant evidence from database logs, metrics, and operational signals.
2. Applies contextual Copilot algorithms to interpret the evidence and generate recommendations.
3. Presents the findings, including the rationale, probable cause, and remediation steps, directly to the user.

The agent’s recommendations are dynamically generated, drawing from both real-time evidence and Microsoft’s authoritative database management resources.

**Use Cases and Application Scenarios**  
This update is particularly beneficial in the following scenarios:

- **Proactive Database Monitoring:** IT teams can leverage the agent to receive immediate, actionable insights when issues arise, reducing downtime.
- **Root Cause Analysis:** The contextual explanations assist engineers in understanding the underlying causes of database problems without extensive manual investigation.
- **Operational Automation:** Automated recommendations streamline incident response workflows, enabling faster resolution and improved reliability.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production environments and could be subject to changes or enhancements based on user feedback.
- **Scope of Recommendations:** Recommendations are based on available evidence and Microsoft-authored content; completeness and accuracy depend on the quality of telemetry and issue detection.
- **Integration Requirements:** Users must ensure their SQL databases are configured to provide sufficient telemetry and evidence for the agent to operate effectively.

**Integration with Related Azure Services**  
The Database Agent for SQL with contextual Copilot is designed to work within the Azure ecosystem. It can be integrated with:

- **Azure SQL Database:** For managed SQL workloads, providing seamless issue detection and remediation guidance.
- **Azure Monitor:** Leveraging telemetry and logs for evidence collection and issue analysis.
- **Azure Copilot:** Utilizing Copilot’s AI capabilities for contextual recommendations, aligning with broader Azure AI-driven management tools.

---

**Summary Sentence:**  
The Database Agent for SQL with contextual Copilot, now in public preview, provides AI-generated, evidence-based recommendations for detected database issues, including explanations, likely causes, and actionable next steps, enhancing operational efficiency and troubleshooting within Azure SQL environments.

---

### 17. Generally Available: Database Hub real-time performance dashboards

**Published**: November 17, 2026 22:42:06 UTC
**Link**: [Generally Available: Database Hub real-time performance dashboards](https://azure.microsoft.com/updates?id=579644)

**Update ID**: 579644
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Hybrid + multicloud, Compute, Azure Cosmos DB, Azure Database for PostgreSQL, Azure SQL Database, Azure SQL Managed Instance, SQL Server on Azure Virtual Machines, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
Database Hub in Microsoft Fabric now offers generally available, built-in real-time performance dashboards.

**Key changes or new features:**  
- Unified dashboards provide real-time monitoring for Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB.
- The Performance page enables tracking of key metrics such as CPU, memory, storage, and IO across supported database services.
- Dashboards are integrated directly within Database Hub, eliminating the need for external monitoring tools or manual setup.

**Target audience affected:**  
- Developers and IT professionals managing Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB databases.
- Teams responsible for database performance monitoring, troubleshooting, and optimization.

**Important notes:**  
- The feature streamlines database performance management by consolidating monitoring into a single interface.
- Real-time visibility helps identify and resolve performance issues faster.
- No additional configuration is required; dashboards are available out-of-the-box in Database Hub.
- For more details, refer to the official Azure Update: [Database Hub real-time performance dashboards](https://azure.microsoft.com/updates?id=579644).

**Details**:

**Azure Update Report: Generally Available – Database Hub Real-Time Performance Dashboards**

**Background and Purpose of the Update:**  
The Database Hub in Microsoft Fabric has introduced built-in, real-time performance dashboards that are now generally available. The primary purpose of this update is to consolidate monitoring capabilities for multiple database platforms—including Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB—into a single, unified interface. This enhancement addresses the need for centralized visibility and streamlined performance management across diverse database environments, reducing operational complexity for IT professionals.

**Specific Features and Detailed Changes:**  
With this update, Database Hub provides native dashboards accessible from the Performance page. These dashboards offer real-time tracking of critical performance metrics such as CPU usage, memory consumption, storage utilization, and input/output (IO) operations. The integration covers three major database services:  
- **Microsoft SQL:** Enables monitoring of SQL workloads, resource utilization, and storage metrics.  
- **Azure Database for PostgreSQL Flexible Server:** Offers insights into PostgreSQL server health, performance bottlenecks, and resource allocation.  
- **Azure Cosmos DB:** Provides visibility into throughput, latency, and storage metrics for globally distributed NoSQL workloads.

The dashboards are pre-configured, requiring minimal setup, and are designed for immediate usability. The real-time nature ensures that administrators can quickly detect anomalies and respond to performance issues as they arise.

**Technical Mechanisms and Implementation Methods:**  
The real-time dashboards leverage built-in telemetry and monitoring capabilities within Microsoft Fabric. Data collection is automated and aggregated from the underlying database services. The dashboards utilize Fabric’s visualization components to present performance metrics in an intuitive, graphical format. Metrics are updated continuously, reflecting the current state of each database instance. The implementation ensures secure access to performance data, adhering to Azure’s authentication and authorization protocols.

**Use Cases and Application Scenarios:**  
- **Centralized Monitoring:** IT teams managing multiple database types can use Database Hub to monitor all supported databases from a single location, improving operational efficiency.  
- **Performance Troubleshooting:** Real-time dashboards enable rapid identification of resource bottlenecks, facilitating proactive troubleshooting and optimization.  
- **Capacity Planning:** Continuous visibility into storage and resource usage assists in forecasting and scaling database resources as needed.  
- **Incident Response:** Immediate access to performance metrics allows for faster diagnosis and remediation during outages or performance degradation.

**Important Considerations and Limitations:**  
- The dashboards are limited to Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB. Other database platforms are not currently supported.  
- Real-time metrics are dependent on the underlying telemetry infrastructure; delays or gaps in data collection may impact dashboard accuracy.  
- Access control is governed by Azure security policies; users must have appropriate permissions to view performance data.

**Integration with Related Azure Services:**  
Database Hub’s performance dashboards are tightly integrated with Microsoft Fabric, leveraging its data aggregation and visualization capabilities. The dashboards complement Azure Monitor and other native monitoring tools, providing an additional layer of visibility. Integration with Azure security and identity services ensures secure access and compliance with organizational policies.

**Summary Sentence:**  
Database Hub in Microsoft Fabric now offers generally available, built-in real-time performance dashboards for Microsoft SQL, Azure Database for PostgreSQL flexible server, and Azure Cosmos DB, enabling centralized monitoring and immediate visibility into key resource metrics from a single interface.

---

### 18. Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors 

**Published**: November 17, 2026 22:40:50 UTC
**Link**: [Private Preview: Azure DH/EHasv8 VMs based on 6th Gen AMD EPYC™ (“Venice”) processors ](https://azure.microsoft.com/updates?id=581308)

**Update ID**: 581308
**Data source**: Azure Updates API

**Categories**: In development, Compute, Virtual Machines, Microsoft Ignite

**Summary**:

- What was updated  
Azure announced the private preview of new DHasv8, DHalsv8, and EHasv8-series virtual machines (VMs), powered by 6th Generation AMD EPYC™ (“Venice”) processors.

- Key changes or new features  
These VMs offer expanded compute capabilities, leveraging the performance improvements of the latest AMD EPYC processors. The new series is designed to support next-generation cloud workloads, providing enhanced scalability, improved memory bandwidth, and better price-performance ratios. The DHasv8 and DHalsv8 series target general-purpose and compute-optimized workloads, while the EHasv8 series is optimized for memory-intensive applications.

- Target audience affected  
Developers and IT professionals running compute-intensive, memory-intensive, or general-purpose workloads in Azure, especially those seeking improved performance and scalability for their applications.

- Important notes if any  
The preview is currently private, so access is limited and may require registration or approval. These VMs are ideal for organizations planning to modernize their cloud infrastructure or migrate demanding workloads. Interested users should monitor Azure updates for public preview or general availability announcements.

**Details**:

**Azure Update Report: Private Preview of Azure DHasv8, DHalsv8, and EHasv8 VMs Powered by 6th Gen AMD EPYC™ (“Venice”) Processors**

**Background and Purpose of the Update**  
Microsoft Azure has announced the private preview of new virtual machine (VM) series: DHasv8, DHalsv8, and EHasv8. These VMs are powered by the 6th Generation AMD EPYC™ (“Venice”) processors. The primary purpose of this update is to introduce expanded compute capabilities for next-generation cloud applications, leveraging the latest advancements in AMD processor technology. This move aims to provide customers with improved performance, scalability, and efficiency for demanding workloads.

**Specific Features and Detailed Changes**  
The new VM series—DHasv8, DHalsv8, and EHasv8—are based on the 6th Gen AMD EPYC™ processors, known for their high core counts, advanced memory bandwidth, and enhanced security features. These VMs are designed to deliver expanded compute resources, which likely include increased vCPU counts, higher memory configurations, and improved throughput compared to previous generations. The update specifically targets workloads that require robust compute power, such as large-scale enterprise applications, analytics, and high-performance computing (HPC).

**Technical Mechanisms and Implementation Methods**  
The DHasv8, DHalsv8, and EHasv8 VM series utilize the AMD EPYC™ “Venice” architecture, which is engineered for cloud environments. The implementation involves integrating these processors into Azure’s infrastructure, enabling customers to provision VMs that benefit from the processor’s advanced capabilities. The VMs are deployed and managed through standard Azure mechanisms, including Azure Portal, CLI, and ARM templates. The private preview phase allows selected customers to test and validate these VMs before general availability.

**Use Cases and Application Scenarios**  
These VM series are suitable for a variety of use cases, including:
- Enterprise workloads requiring high compute and memory, such as SAP, SQL Server, and Oracle databases.
- Data analytics and big data processing, where expanded compute resources can accelerate data transformation and analysis.
- High-performance computing (HPC) scenarios, including scientific simulations and financial modeling.
- Cloud-native applications designed to scale horizontally and take advantage of modern processor architectures.

**Important Considerations and Limitations**  
As this is a private preview, access is restricted to selected customers. IT professionals should be aware that features, performance, and availability may change before general release. It is important to validate workload compatibility and performance during the preview phase. Additionally, customers should review Azure documentation for specific VM sizes, regional availability, and supported operating systems.

**Integration with Related Azure Services**  
The new VM series can be integrated with other Azure services such as Azure Virtual Networks, Azure Storage, and Azure Backup. They are compatible with Azure management and monitoring tools, including Azure Monitor and Azure Security Center. These VMs can also be used in conjunction with Azure Kubernetes Service (AKS) for containerized workloads, and with Azure Load Balancer for scalable application deployment.

**Summary Sentence**  
The private preview of Azure DHasv8, DHalsv8, and EHasv8 VMs introduces expanded compute capabilities powered by 6th Gen AMD EPYC™ (“Venice”) processors, offering enhanced performance for next-generation cloud applications and enterprise workloads.

---

### 19. Public Preview: Azure SQL DB Hyperscale Cross Database Querying

**Published**: November 17, 2026 22:35:29 UTC
**Link**: [Public Preview: Azure SQL DB Hyperscale Cross Database Querying](https://azure.microsoft.com/updates?id=579221)

**Update ID**: 579221
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL Database Hyperscale now supports native cross-database querying in public preview.

- Key changes or new features  
Developers and IT professionals can use T-SQL three-part names (e.g., database.schema.object) to access and join data across multiple databases within the same Hyperscale elastic pool and logical server. This eliminates the need for external data sources or linked servers, simplifying multi-database operations and enabling more flexible application architectures.

- Target audience affected  
This update is relevant to developers building applications on Azure SQL Database Hyperscale, database administrators managing multi-database environments, and IT professionals responsible for data integration and analytics across Hyperscale databases.

- Important notes if any  
Cross-database querying is only supported within Hyperscale databases that reside in the same elastic pool and logical server. This feature is currently in public preview, so it may not be suitable for production workloads yet. Users should review documentation for limitations and best practices before adoption.

For more information, visit the official Azure Update: https://azure.microsoft.com/updates?id=579221

**Details**:

**Azure Update Report: Public Preview – Azure SQL DB Hyperscale Cross Database Querying**

**Background and Purpose of the Update:**  
Azure SQL Database Hyperscale is designed for highly scalable, high-performance workloads. Traditionally, Azure SQL Database has limited cross-database querying capabilities, especially in managed environments, which can hinder scenarios where data is distributed across multiple databases. This update introduces native cross-database querying within Hyperscale, aiming to streamline data access and enable more flexible application architectures.

**Specific Features and Detailed Changes:**  
With this public preview, native cross-database queries are now supported for Azure SQL Database Hyperscale when databases are located within the same elastic pool on a logical server. Developers and administrators can use standard T-SQL three-part naming conventions (`database.schema.object`) to reference and join tables or views across databases. This enhancement removes the need for workarounds such as data movement, ETL processes, or external data sources for intra-pool data access.

**Technical Mechanisms and Implementation Methods:**  
The implementation leverages the underlying architecture of Hyperscale elastic pools, which allows multiple databases to share resources on a single logical server. The cross-database querying capability is natively integrated into the T-SQL engine, supporting direct referencing of objects in other databases within the same pool. This is achieved by parsing and resolving three-part object names at query compilation and execution time, ensuring security and performance are maintained. No additional configuration or external data sources are required; access control is enforced according to the security context of the querying user.

**Use Cases and Application Scenarios:**  
- **Multi-Tenant SaaS Applications:** Applications that isolate tenant data into separate databases can now efficiently aggregate or join data across tenants for reporting or analytics without data duplication.
- **Data Warehousing and Analytics:** Organizations can perform federated queries across operational and analytical databases within the same Hyperscale pool, simplifying data integration.
- **Microservices Architectures:** Services with domain-specific databases can query related data across boundaries, enabling richer business logic and reporting.

**Important Considerations and Limitations:**  
- **Scope:** Cross-database querying is only supported for databases within the same Hyperscale elastic pool and logical server. Queries across pools or servers are not supported.
- **Security:** Access to objects in other databases is governed by the permissions of the querying user. Proper access controls must be in place to prevent unauthorized data exposure.
- **Performance:** While native, cross-database queries may introduce additional resource consumption; monitoring and query optimization are recommended.
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads, and support or SLAs may be limited.

**Integration with Related Azure Services:**  
This feature is tightly coupled with Azure SQL Database Hyperscale and elastic pools. It does not require integration with external data sources, Linked Servers, or Azure Synapse. However, it can complement solutions involving Azure Data Factory or Azure Logic Apps by reducing the need for data movement between databases for intra-pool scenarios.

**Summary Sentence:**  
Azure SQL Database Hyperscale now supports native cross-database querying in public preview, enabling secure and efficient T-SQL queries across databases within the same elastic pool and logical server, thereby simplifying multi-database application architectures and data integration scenarios.

---

### 20. Generally Available: Near-instant provisioning for Azure DocumentDB clusters  

**Published**: November 17, 2026 21:57:41 UTC
**Link**: [Generally Available: Near-instant provisioning for Azure DocumentDB clusters  ](https://azure.microsoft.com/updates?id=579349)

**Update ID**: 579349
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DocumentDB now supports near-instant provisioning for M10 to M30 compute tiers.

- Key changes or new features  
Previously, only the free tier offered instant provisioning, allowing users to start using DocumentDB without waiting. With this update, the M10, M20, and M30 compute tiers can now be provisioned almost instantly, eliminating the typical 10-15 minute wait time for cluster setup. This enhancement streamlines the deployment process for production and larger workloads.

- Target audience affected  
Developers and IT professionals who use Azure DocumentDB, especially those deploying clusters in the M10-M30 compute tiers for development, testing, or production environments.

- Important notes if any  
This update improves agility for teams needing rapid cluster setup, enabling faster development cycles and quicker scaling. Existing workflows that relied on longer provisioning times should be reviewed, as provisioning is now significantly faster. The free tier remains available for instant provisioning, but now higher compute tiers benefit from the same speed. For more details, refer to the official Azure update link.

**Details**:

**Azure Update Report: Near-instant provisioning for Azure DocumentDB clusters (M10–M30 tiers)**

**Background and Purpose of the Update**  
Historically, Azure DocumentDB clusters offered instant provisioning only for the free tier, enabling users to quickly deploy and start working without the typical 10–15 minute wait associated with cluster creation. This update extends near-instant provisioning capabilities to the M10, M20, and M30 compute tiers, addressing the need for faster deployment in production and development environments where higher compute resources are required.

**Specific Features and Detailed Changes**  
The update introduces near-instant provisioning for the M10, M20, and M30 compute tiers in Azure DocumentDB. Users can now create clusters in these tiers with minimal waiting time, significantly reducing the deployment time compared to previous provisioning durations. This enhancement ensures that larger, more capable clusters are available almost immediately, aligning the provisioning experience of paid tiers with that of the free tier.

**Technical Mechanisms and Implementation Methods**  
Near-instant provisioning is achieved through improvements in the cluster creation workflow. While the detailed technical mechanisms are not specified in the update, the result is that the infrastructure supporting M10–M30 tiers is optimized to allow rapid allocation and initialization of resources. This likely involves pre-warmed pools or streamlined orchestration processes that minimize the time required to configure and activate clusters at these compute levels.

**Use Cases and Application Scenarios**  
- **Development and Testing:** Teams can quickly spin up M10–M30 clusters for development, testing, or staging environments, reducing wait times and accelerating iteration cycles.
- **Production Deployments:** Organizations deploying DocumentDB clusters for production workloads can benefit from faster provisioning, enabling rapid scaling or migration scenarios.
- **Disaster Recovery and Failover:** Near-instant provisioning supports business continuity by allowing quick cluster creation during failover or disaster recovery events.

**Important Considerations and Limitations**  
- The near-instant provisioning feature is currently available only for the M10, M20, and M30 compute tiers. Other tiers may still require standard provisioning times.
- Users should verify regional availability, as provisioning speed may depend on local infrastructure and capacity.
- The update does not specify changes to cluster configuration options or operational limits; only the provisioning speed is affected.

**Integration with Related Azure Services**  
Azure DocumentDB clusters provisioned via this update can be integrated with other Azure services as usual, including Azure Cosmos DB, Azure Functions, and Azure Logic Apps. Faster provisioning supports scenarios where DocumentDB clusters are part of automated workflows, CI/CD pipelines, or dynamic resource scaling in conjunction with other Azure services.

**Summary Sentence**  
Near-instant provisioning for Azure DocumentDB clusters in the M10–M30 compute tiers is now generally available, enabling rapid deployment and improved agility for development, testing, and production workloads.

---

### 21. Generally Available: Network egress controls for hosted agents in Microsoft Foundry

**Published**: November 17, 2026 21:51:16 UTC
**Link**: [Generally Available: Network egress controls for hosted agents in Microsoft Foundry](https://azure.microsoft.com/updates?id=571821)

**Update ID**: 571821
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft.AspNetCore.OData.Formatter.Value.EdmUntypedCollection

**Summary**:

- What was updated  
Network egress controls for hosted agents in Microsoft Foundry are now generally available.

- Key changes or new features  
This update introduces granular outbound network control for Foundry hosted agents. Administrators can now define ordered rules that match destination hosts using fully qualified domain names (FQDN), including wildcard patterns (e.g., *.contoso.com). Each rule can enforce Allow, Deny, or Rewrite actions, enabling precise management of agent outbound traffic. The Rewrite action lets you redirect outbound requests to alternative destinations.

- Target audience affected  
Developers and IT professionals using Microsoft Foundry hosted agents for CI/CD pipelines or automation tasks.

- Important notes  
This feature enhances security and compliance by restricting agent outbound connectivity to approved endpoints. It allows organizations to prevent data exfiltration, enforce network policies, and meet regulatory requirements. Rules are evaluated in order, so rule priority is important. Review and update your agent network configurations to leverage these controls and ensure your pipelines function as expected.  

For more details, visit: https://azure.microsoft.com/updates?id=571821

**Details**:

**Azure Update Report: Network Egress Controls for Hosted Agents in Microsoft Foundry (General Availability)**

**Background and Purpose of the Update**  
Microsoft Foundry provides hosted agents that execute workloads in managed environments. Traditionally, controlling outbound (egress) network traffic from these agents has been challenging, especially for organizations requiring strict security and compliance. This update introduces network egress controls for Foundry hosted agents, now generally available, enabling administrators to govern and restrict outbound connections directly from the agent environment.

**Specific Features and Detailed Changes**  
The new egress control capability allows administrators to define ordered rules that match outbound traffic based on the destination host. These rules support Fully Qualified Domain Names (FQDN), including wildcard patterns such as *.contoso.com. Each rule specifies an action:  
- **Allow**: Permits outbound connections to the matched destination.  
- **Deny**: Blocks outbound connections to the matched destination.  
- **Rewrite**: Redirects outbound traffic to an alternative destination.

Rules are processed in order, enabling granular control over which external resources hosted agents can access. This feature enhances security by limiting exposure to only approved endpoints and provides flexibility for redirecting traffic as needed.

**Technical Mechanisms and Implementation Methods**  
Egress controls are implemented via ordered rule sets that inspect outbound connection requests from Foundry hosted agents. The mechanism matches the destination host using FQDNs, supporting wildcards for broader domain coverage. When an agent initiates an outbound connection, the system evaluates the rules sequentially:  
- If a rule matches the destination, the specified action (Allow, Deny, or Rewrite) is applied.  
- If no rules match, the default behavior is enforced (not specified in the update).

The Rewrite action enables traffic redirection, which can be used for scenarios such as proxying or enforcing access through specific gateways. The rule configuration is managed within the Foundry environment, providing centralized control.

**Use Cases and Application Scenarios**  
- **Security Hardening**: Restrict hosted agents to only communicate with approved external services, reducing attack surface.  
- **Compliance Enforcement**: Ensure outbound connections comply with regulatory requirements by blocking access to unauthorized domains.  
- **Traffic Redirection**: Redirect agent traffic to internal proxies or monitoring gateways for auditing or inspection.  
- **Environment Isolation**: Prevent agents from accessing public internet resources except those explicitly allowed.

**Important Considerations and Limitations**  
- Rules are matched based on FQDN, and wildcard support enables broad domain control but may require careful configuration to avoid unintended access.  
- Ordered rule processing means rule sequence impacts behavior; administrators must prioritize rules correctly.  
- The update does not specify default behavior for unmatched destinations, so review documentation for fallback actions.  
- Rewrite actions may introduce latency or require additional infrastructure for handling redirected traffic.

**Integration with Related Azure Services**  
Network egress controls for Foundry hosted agents complement existing Azure network security features such as Azure Firewall, Network Security Groups (NSGs), and Private Endpoints. Administrators can use egress controls alongside these services to create layered security architectures, ensuring both agent-level and network-level outbound traffic governance.

**Summary Sentence**  
Network egress controls for Microsoft Foundry hosted agents are now generally available, enabling ordered rule-based governance of outbound connections with Allow, Deny, and Rewrite actions matched on FQDNs, supporting enhanced security, compliance, and traffic management for hosted workloads.

---

### 22. Generally Available: MCP server knowledge sources in Foundry IQ

**Published**: November 17, 2026 21:21:27 UTC
**Link**: [Generally Available: MCP server knowledge sources in Foundry IQ](https://azure.microsoft.com/updates?id=563411)

**Update ID**: 563411
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Ignite, Feature, Microsoft Build

**Summary**:

- What was updated  
Foundry IQ now supports Model Context Protocol (MCP) servers as federated knowledge sources, and this feature is generally available.

- Key changes or new features  
Customers can register MCP servers as read-only knowledge sources within Foundry IQ. These MCP knowledge sources are integrated into Foundry IQ’s cross-source querying and knowledge discovery capabilities, enabling unified access to data across multiple sources.

- Target audience affected  
This update is relevant for developers and IT professionals working with Foundry IQ, especially those managing enterprise knowledge sources or integrating MCP servers for data federation and analytics.

- Important notes  
MCP servers are registered as read-only, meaning data can be queried but not modified from within Foundry IQ. This enhances security and data integrity. The integration allows for more comprehensive data analysis and discovery by leveraging MCP alongside other supported sources. No additional configuration is required beyond standard registration procedures. For more details, refer to the official Azure update link.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: MCP server knowledge sources in Foundry IQ  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563411)

---

### Background and Purpose of the Update

This update announces the general availability (GA) of Model Context Protocol (MCP) server support as federated knowledge sources within Foundry IQ. The primary purpose is to enable customers to register MCP servers as read-only knowledge sources, thereby broadening the data integration and federated search capabilities of Foundry IQ. This enhancement aims to facilitate seamless knowledge discovery across multiple, heterogeneous data repositories.

---

### Specific Features and Detailed Changes

- **MCP Server Registration:** Customers can now register an MCP server as a knowledge source in Foundry IQ. The registration is explicitly read-only, ensuring data integrity and compliance with source system policies.
- **Federated Knowledge Source:** Once registered, the MCP server acts as a federated knowledge source. This means its data can be queried and referenced alongside other knowledge sources within Foundry IQ.
- **Cross-Source Participation:** MCP knowledge sources are fully integrated into Foundry IQ’s cross-source functionalities, allowing for unified search, discovery, and knowledge graph operations across all connected sources.

---

### Technical Mechanisms and Implementation Methods

- **Read-Only Integration:** The integration mechanism is designed to be non-intrusive; Foundry IQ interacts with the MCP server in a read-only mode, ensuring that the underlying data remains unaltered.
- **Federation Protocol:** Foundry IQ leverages the MCP protocol to federate knowledge sources. This protocol standardizes the way context and model information is exchanged, ensuring compatibility and consistent data representation.
- **Registration Workflow:** Administrators register the MCP server through Foundry IQ’s management interface, specifying connection parameters and access credentials as required by the MCP protocol.
- **Cross-Source Querying:** Once registered, Foundry IQ includes the MCP server in its cross-source query execution plans, enabling composite queries and knowledge graph traversals that span multiple sources.

---

### Use Cases and Application Scenarios

- **Enterprise Knowledge Management:** Organizations with existing MCP-compliant servers can now federate these sources into Foundry IQ, enabling unified knowledge discovery across departmental or organizational boundaries.
- **Data Compliance and Governance:** By supporting read-only access, organizations can ensure that sensitive or regulated data remains protected while still being discoverable for knowledge purposes.
- **Cross-Repository Analytics:** Users can perform analytics and knowledge graph operations that span both MCP servers and other Foundry IQ knowledge sources, supporting advanced business intelligence and research scenarios.

---

### Important Considerations and Limitations

- **Read-Only Access:** The integration is strictly read-only. Any operations requiring write-back or data modification on the MCP server are not supported.
- **Protocol Compliance:** Only MCP-compliant servers can be registered. Non-compliant or proprietary knowledge sources are not eligible for this integration.
- **Cross-Source Participation:** While MCP sources participate in cross-source operations, performance and feature parity may depend on the specific MCP server implementation and its compatibility with Foundry IQ’s federation mechanisms.

---

### Integration with Related Azure Services

- **Foundry IQ Ecosystem:** This update enhances the Foundry IQ platform by expanding its ecosystem of federated knowledge sources.
- **Azure Data Services:** While not explicitly mentioned, organizations can leverage this capability alongside other Azure data integration and analytics services to build comprehensive knowledge management solutions.

---

**Summary:**  
The general availability of MCP server knowledge sources in Foundry IQ enables customers to register MCP-compliant servers as read-only federated knowledge sources, allowing seamless participation in cross-source knowledge discovery and analytics within the Foundry IQ platform.

---

### 23. Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search

**Published**: November 17, 2026 21:17:15 UTC
**Link**: [Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search](https://azure.microsoft.com/updates?id=563661)

**Update ID**: 563661
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Content Understanding skill in Azure AI Search is now generally available, offering semantic chunking and AI-generated image descriptions.

- Key changes or new features  
  - Semantic chunking: The skill breaks down content into semantically coherent chunks, improving search relevance and content processing.  
  - AI-generated image descriptions: Automatically generates descriptive text for images, enhancing accessibility and searchability.  
  - Structured Markdown output: The skill produces output in structured Markdown format, facilitating integration and downstream processing.  
  - Integration: Available for use with Foundry IQ and Azure AI Search, supporting advanced content understanding scenarios.

- Target audience affected  
Developers and IT professionals working with Azure AI Search, content indexing, accessibility, and search optimization. Teams building solutions that require enhanced content parsing, semantic search, or image description generation.

- Important notes  
The features are now generally available, meaning they are ready for production use. Semantic chunking improves document indexing and retrieval, while AI-generated image descriptions support accessibility compliance and richer search experiences. Integration with Foundry IQ and Azure AI Search enables streamlined workflows for content understanding. Review documentation for API usage and integration best practices.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Semantic chunking and AI-generated image descriptions with Azure Content Understanding in Azure AI Search

**Background and Purpose of the Update:**  
This update announces the general availability of the Azure Content Understanding skill within Azure AI Search, specifically for semantic chunking and AI-generated image descriptions. The purpose is to enhance the search and indexing capabilities of Azure AI Search by enabling more granular and meaningful content segmentation and automated image metadata generation. This is particularly relevant for organizations seeking to improve content discoverability and relevance in search-driven applications.

**Specific Features and Detailed Changes:**  
- **Semantic Chunking:** The Content Understanding skill now produces semantically coherent chunks from input content. This means that documents or content are segmented into logical, contextually relevant sections, rather than arbitrary splits. The output is structured in Markdown format, facilitating easier integration and downstream processing.
- **AI-Generated Image Descriptions:** The skill can generate descriptive metadata for images using AI, automatically creating textual descriptions that enhance searchability and accessibility.
- **Integration with Foundry IQ and Azure AI Search:** The skill is designed for use with Foundry IQ and Azure AI Search, allowing organizations to leverage advanced content understanding within their search solutions.

**Technical Mechanisms and Implementation Methods:**  
- The Content Understanding skill operates as a cognitive skill within the Azure AI Search pipeline. When content (text or images) is ingested, the skill processes it to generate semantic chunks and image descriptions.
- Semantic chunking leverages AI models to analyze the structure and meaning of the content, producing coherent sections that are output in Markdown. This structured format supports rich text representation and easier downstream consumption.
- For images, AI models generate descriptive text, which can be indexed as metadata to improve search relevance and accessibility (e.g., for visually impaired users).
- The skill can be configured within the Azure AI Search indexer pipeline, enabling automated enrichment of content during indexing.

**Use Cases and Application Scenarios:**  
- **Enterprise Search:** Organizations can improve document search by indexing semantically meaningful chunks, leading to more relevant search results.
- **Knowledge Management:** Automated chunking and image descriptions facilitate better organization and retrieval of information in knowledge bases.
- **Accessibility:** AI-generated image descriptions enhance accessibility for users requiring assistive technologies.
- **Content Analytics:** Structured Markdown output enables advanced content analysis and visualization.

**Important Considerations and Limitations:**  
- The skill produces output in Markdown, which may require downstream systems to support or parse this format.
- It is generally available for use with Foundry IQ and Azure AI Search; compatibility with other Azure services may require additional integration.
- The quality of semantic chunking and image descriptions depends on the underlying AI models and the nature of the input content.

**Integration with Related Azure Services:**  
- The Content Understanding skill integrates directly with Azure AI Search, acting as a cognitive skill in the indexing pipeline.
- It is also designed for use with Foundry IQ, supporting advanced content processing scenarios.
- The skill can complement other Azure Cognitive Services, such as Text Analytics or Computer Vision, for broader enrichment workflows.

**Summary Sentence:**  
Azure Content Understanding skill is now generally available in Azure AI Search, offering semantic chunking and AI-generated image descriptions with structured Markdown output for enhanced search and content enrichment.

---

### 24. Generally Available: Snapshot backup for SQL Server in Azure VMs

**Published**: November 17, 2026 21:15:38 UTC
**Link**: [Generally Available: Snapshot backup for SQL Server in Azure VMs](https://azure.microsoft.com/updates?id=564668)

**Update ID**: 564668
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Storage, Azure Backup, Management, Microsoft Ignite, Security, Services, Feature, Compliance

**Summary**:

- What was updated  
Azure Backup now offers generally available support for snapshot-based backup of SQL Server running on Azure Virtual Machines.

- Key changes or new features  
This update introduces the use of Azure disk snapshots in combination with native SQL Server transaction log backups. The snapshot-based approach enables near-instant, low-impact full backups, especially beneficial for large SQL Server databases. This method reduces backup windows and minimizes performance impact on production workloads. Transaction log backups continue to provide granular restore capabilities.

- Target audience affected  
Developers and IT professionals managing SQL Server workloads on Azure Virtual Machines, including DBAs and cloud infrastructure teams.

- Important notes if any  
Snapshot-based backups can significantly improve backup speed and reduce resource consumption compared to traditional backup methods. This feature is integrated with Azure Backup’s existing management and monitoring tools, ensuring seamless backup and restore operations. Users should review Azure Backup documentation for prerequisites and configuration steps, and verify compatibility with their SQL Server versions and VM configurations. This enhancement is available in all regions where Azure Backup supports SQL Server VM protection.

**Details**:

**Azure Update Report: Generally Available – Snapshot Backup for SQL Server in Azure VMs**

**Background and Purpose of the Update**  
Azure Backup has introduced snapshot-based backup support for SQL Server hosted on Azure Virtual Machines. The primary purpose of this update is to address the challenges of performing full backups for large SQL Server databases, which can be time-consuming and resource-intensive. By leveraging Azure disk snapshots in conjunction with native SQL transaction log backups, the solution aims to provide near-instant, low-impact full backups, improving backup efficiency and reducing performance overhead on production workloads.

**Specific Features and Detailed Changes**  
- **Snapshot-Based Full Backups:** Azure Backup now utilizes Azure disk snapshots to capture the state of SQL Server databases, enabling rapid full backups regardless of database size.
- **Native SQL Transaction Log Backups:** The solution integrates native SQL transaction log backups, ensuring data consistency and enabling point-in-time recovery.
- **Near-Instant Backup:** The combined approach delivers full backups with minimal impact on SQL Server performance, particularly beneficial for large databases.
- **General Availability:** This feature is now generally available, meaning it is production-ready and supported for enterprise workloads.

**Technical Mechanisms and Implementation Methods**  
- **Azure Disk Snapshots:** The backup process initiates a snapshot of the underlying Azure disk attached to the VM hosting SQL Server. This snapshot captures the disk state at a specific point in time, providing a fast and scalable backup mechanism.
- **SQL Transaction Log Integration:** Alongside the disk snapshot, Azure Backup performs native SQL transaction log backups. This ensures that all transactions are captured, maintaining data integrity and enabling granular recovery options.
- **Backup Workflow:** The workflow combines disk-level snapshots for full backups and transaction log backups for incremental changes, optimizing backup speed and minimizing impact on the SQL Server instance.

**Use Cases and Application Scenarios**  
- **Large SQL Server Databases:** Organizations running large SQL Server databases on Azure VMs can leverage this feature to perform full backups quickly and efficiently.
- **High-Performance Production Environments:** Environments requiring minimal backup window and low impact on database performance benefit from snapshot-based backups.
- **Compliance and Disaster Recovery:** Enterprises needing frequent, consistent backups for compliance or disaster recovery purposes can utilize this capability for reliable data protection.

**Important Considerations and Limitations**  
- **Backup Consistency:** While disk snapshots are fast, combining them with transaction log backups is essential for ensuring data consistency and supporting point-in-time restores.
- **Resource Usage:** Although the impact is minimized, administrators should monitor VM and disk performance during backup operations.
- **Supported Configurations:** The feature is specific to SQL Server running on Azure Virtual Machines and may not apply to other SQL Server deployment models or non-Azure environments.
- **Backup Management:** Proper configuration of Azure Backup policies and retention settings is necessary to align with organizational requirements.

**Integration with Related Azure Services**  
- **Azure Backup:** This feature is integrated directly into Azure Backup, allowing centralized management and monitoring of SQL Server backups.
- **Azure VM and Disk Management:** Utilizes native Azure disk snapshot capabilities, ensuring compatibility with Azure VM infrastructure.
- **Azure Portal and Automation:** Backups can be managed via the Azure Portal or automated using Azure Resource Manager templates and PowerShell scripts, supporting streamlined operations.

**Summary Sentence**  
Azure Backup’s snapshot-based backup for SQL Server in Azure VMs is now generally available, providing near-instant, low-impact full backups by combining Azure disk snapshots with native SQL transaction log backups, thereby enhancing backup efficiency and data protection for large SQL Server workloads.

---

### 25. Generally Available: Confidential VMs with Intel TDX support on AKS 

**Published**: November 17, 2026 21:00:05 UTC
**Link**: [Generally Available: Confidential VMs with Intel TDX support on AKS ](https://azure.microsoft.com/updates?id=581130)

**Update ID**: 581130
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now offers generally available support for Confidential Virtual Machines (VMs) with Intel Trust Domain Extensions (TDX) in node pools.

- Key changes or new features  
AKS Confidential VM node pools can now use Intel TDX-enabled hardware, expanding support beyond AMD SEV-SNP. This allows customers who require Intel TDX for attestation and hardware-based confidentiality to run their sensitive workloads securely on AKS. The update provides enhanced security options for containerized workloads, leveraging Intel’s confidential computing capabilities.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those with compliance or security requirements mandating Intel TDX. Organizations standardized on Intel TDX for confidential computing and attestation can now use AKS for these workloads.

- Important notes  
Previously, AKS Confidential VM node pools only supported AMD SEV-SNP, limiting options for customers needing Intel TDX. With this update, customers can select Intel TDX as their confidential VM node pool hardware, enabling broader adoption of confidential computing on AKS. Ensure your workloads and applications are compatible with Intel TDX before migration or deployment.  

For more details, visit: https://azure.microsoft.com/updates?id=581130

**Details**:

**Azure Update: Generally Available – Confidential VMs with Intel TDX support on AKS**

**Background and Purpose of the Update**  
Previously, Azure Kubernetes Service (AKS) Confidential VM (CVM) node pools only supported AMD SEV-SNP technology for hardware-based confidentiality and attestation. This limited customers who have standardized on Intel Trust Domain Extensions (TDX) from running their confidential workloads on AKS, as the required hardware-backed security features were not available for Intel-based environments. The purpose of this update is to extend AKS Confidential VM node pool support to include Intel TDX, enabling organizations with Intel-based security requirements to leverage AKS for confidential computing workloads.

**Specific Features and Detailed Changes**  
- **Intel TDX Support:** AKS Confidential VM node pools now support Intel Trust Domain Extensions (TDX), in addition to the existing AMD SEV-SNP support.
- **GA Availability:** This feature is now generally available, meaning it is fully supported for production workloads.
- **Node Image Compatibility:** Customers can now select node images that are compatible with Intel TDX hardware, allowing them to deploy and manage confidential workloads on AKS using Intel-based VMs.

**Technical Mechanisms and Implementation Methods**  
- **Hardware-based Confidentiality:** Intel TDX provides hardware-enforced isolation for VM memory, ensuring that data in use is protected from access by the host OS, hypervisor, and other VMs.
- **Attestation:** TDX enables attestation mechanisms, allowing workloads to verify the integrity and security posture of the underlying hardware and software stack before execution.
- **AKS Node Pool Configuration:** When creating AKS node pools, users can now specify Intel TDX-enabled VM sizes and images, ensuring that the node pool is provisioned on compatible hardware.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in finance, healthcare, and government sectors that require strict data-in-use protection and have standardized on Intel TDX for compliance and security.
- **Multi-tenant SaaS Platforms:** Providers who need to ensure tenant isolation and confidentiality at the hardware level.
- **Confidential Data Processing:** Workloads that process sensitive information, such as personally identifiable information (PII), intellectual property, or cryptographic keys, can now leverage AKS on Intel TDX-enabled VMs.

**Important Considerations and Limitations**  
- **Hardware Dependency:** This feature requires underlying Azure infrastructure with Intel TDX-capable hardware. Availability may vary by region and VM size.
- **Node Image Selection:** Only specific node images support Intel TDX. Customers must ensure they select the correct image when configuring AKS node pools.
- **Compatibility:** Existing workloads and tooling should be validated for compatibility with Intel TDX-based confidential VMs.

**Integration with Related Azure Services**  
- **Azure Kubernetes Service (AKS):** Seamlessly integrates with AKS, allowing confidential workloads to be orchestrated alongside standard workloads.
- **Azure Attestation:** Can be used in conjunction with Azure Attestation services to verify the trustworthiness of the confidential VM environment.
- **Azure Security and Compliance:** Supports broader Azure security and compliance initiatives by enabling confidential computing on both AMD and Intel hardware platforms.

**Summary Sentence:**  
AKS Confidential VM node pools now generally support Intel TDX, enabling customers standardized on Intel’s hardware-based confidentiality and attestation to run their confidential workloads securely on Azure Kubernetes Service.

---

### 26. Public Preview: Confidential VMs with OS Disk Encryption support on AKS

**Published**: November 17, 2026 21:00:05 UTC
**Link**: [Public Preview: Confidential VMs with OS Disk Encryption support on AKS](https://azure.microsoft.com/updates?id=581125)

**Update ID**: 581125
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite, Feature

**Summary**:

**What was updated**  
Azure Kubernetes Service (AKS) now supports OS disk encryption for Confidential VM node pools in Public Preview.

**Key changes or new features**  
- Ubuntu 22.04 Confidential VM node pools on AKS can now encrypt the OS disk at rest, closing a previous security gap.
- This enhancement enables regulated and security-sensitive customers to protect both workload memory and OS disk data natively within the AKS platform, without needing external solutions.
- OS disk encryption is managed through Azure Disk Encryption, leveraging platform-managed keys.

**Target audience affected**  
- Developers and IT professionals deploying AKS clusters with Confidential VM node pools, especially those in regulated industries (finance, healthcare, government) requiring strict data-at-rest protection.
- Security architects and compliance teams responsible for cloud workload security.

**Important notes**  
- The feature is currently in Public Preview and only available for Ubuntu 22.04 Confidential VM node pools on AKS.
- Customers should validate compatibility and performance impacts before production use.
- This update helps meet compliance requirements for data-at-rest encryption, reducing operational overhead for secure AKS deployments.

[Read more](https://azure.microsoft.com/updates?id=581125)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Confidential VMs with OS Disk Encryption support on AKS  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581125)

---

**Background and Purpose of the Update**

Azure Kubernetes Service (AKS) enables customers to orchestrate containerized workloads with high scalability and security. For regulated industries and customers with strict compliance requirements, AKS offers Confidential VM node pools, which protect workloads in memory using hardware-based security features. However, until now, the OS disk associated with these Confidential VMs was not encrypted at rest by default, leaving a gap in data-at-rest protection. Customers had to implement their own disk encryption solutions outside the platform to meet compliance needs. This update addresses that gap by introducing OS disk encryption support for Confidential VM node pools in AKS, specifically in the Public Preview for Ubuntu 26.04.

---

**Specific Features and Detailed Changes**

- **OS Disk Encryption for Confidential VM Node Pools:**  
  The update introduces native support for encrypting the OS disk at rest for Confidential VM node pools in AKS. This feature is available in Public Preview for node pools running Ubuntu 26.04.
- **Integrated Platform Support:**  
  Customers no longer need to implement external solutions to encrypt the OS disk, as this capability is now provided directly within the AKS platform.
- **Enhanced Compliance:**  
  By encrypting the OS disk at rest, the update closes the data-at-rest protection gap, aligning AKS Confidential VM node pools with regulatory requirements for both in-memory and at-rest data protection.

---

**Technical Mechanisms and Implementation Methods**

- **Confidential VM Technology:**  
  Confidential VMs leverage hardware-based Trusted Execution Environments (TEEs) to protect workloads in memory. With this update, the OS disk is also encrypted at rest, likely using Azure Disk Encryption or similar platform-integrated mechanisms.
- **Ubuntu 26.04 Support:**  
  The OS disk encryption feature is enabled for Confidential VM node pools running Ubuntu 26.04, ensuring compatibility with the latest supported OS version in AKS.
- **Platform Integration:**  
  The encryption process is managed by AKS, reducing operational overhead and ensuring seamless integration with existing node pool provisioning and management workflows.

---

**Use Cases and Application Scenarios**

- **Regulated Industries:**  
  Organizations in sectors such as finance, healthcare, and government can leverage this feature to meet stringent compliance requirements for data protection, both in-memory and at-rest.
- **Sensitive Workloads:**  
  Workloads handling confidential or personally identifiable information (PII) benefit from enhanced security, reducing risk of data exposure from disk theft or unauthorized access.
- **Simplified Compliance:**  
  IT teams can streamline compliance audits and reduce complexity by relying on platform-provided encryption, rather than custom or third-party solutions.

---

**Important Considerations and Limitations**

- **Public Preview Status:**  
  The feature is currently in Public Preview, which may entail limited support and potential changes before General Availability.
- **OS Version Requirement:**  
  OS disk encryption is available only for Ubuntu 26.04 Confidential VM node pools; other OS versions are not supported in this preview.
- **External Solutions May Still Be Needed:**  
  Customers using older OS versions or requiring advanced encryption configurations may still need to implement external disk encryption solutions.

---

**Integration with Related Azure Services**

- **Azure Disk Encryption:**  
  The OS disk encryption is likely integrated with Azure Disk Encryption, providing seamless management and key handling.
- **AKS Platform:**  
  The feature is natively integrated into AKS, simplifying node pool provisioning and lifecycle management.
- **Azure Compliance and Security Services:**  
  Enhanced disk encryption supports integration with Azure Security Center and compliance reporting tools.

---

**Summary Sentence:**  
The Public Preview of OS disk encryption for AKS Confidential VM node pools running Ubuntu 26.04 enables regulated customers to achieve comprehensive data-at

---

### 27. Generally Available: Private endpoint support for Azure HorizonDB clusters

**Published**: November 17, 2026 20:56:06 UTC
**Link**: [Generally Available: Private endpoint support for Azure HorizonDB clusters](https://azure.microsoft.com/updates?id=574153)

**Update ID**: 574153
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Private endpoint support for Azure HorizonDB clusters is now generally available.

- Key changes or new features  
Azure HorizonDB clusters can now be connected privately using Azure Private Link. This enables access via a private IP address from your virtual network, enhancing security by isolating traffic from the public internet. Private DNS integration simplifies connection setup and management. Additionally, you can disable public access to the database, ensuring all traffic remains within your organization's network boundaries.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB clusters, especially those with strict security or compliance requirements, or those deploying HorizonDB in enterprise environments.

- Important notes if any  
To leverage private endpoint support, update your cluster configuration to enable Private Link and adjust DNS settings as needed. Disabling public access is recommended for improved security. Review network and firewall settings to ensure seamless connectivity. This feature helps meet regulatory requirements and reduces exposure to external threats.  
For more information, visit: https://azure.microsoft.com/updates?id=574153

**Details**:

**Azure Update Report: Private Endpoint Support for Azure HorizonDB Clusters (Generally Available)**

**Background and Purpose of the Update:**  
The update introduces generally available support for private endpoints in Azure HorizonDB clusters. This enhancement addresses the need for secure, private connectivity to HorizonDB, eliminating exposure to public internet endpoints. The primary purpose is to strengthen data security and simplify network architecture by enabling access to HorizonDB clusters via Azure Private Link.

**Specific Features and Detailed Changes:**  
- **Private Endpoint Connectivity:** Azure HorizonDB clusters can now be accessed using private endpoints. This allows clients within an Azure Virtual Network (VNet) to connect to HorizonDB using a private IP address, rather than a public one.
- **Private DNS Integration:** The update includes integration with Azure Private DNS, which automates DNS resolution for private endpoints. This simplifies connection setup by ensuring that applications resolve the HorizonDB cluster’s hostname to its private IP address within the VNet.
- **Public Access Control:** Administrators can now disable public access to HorizonDB clusters. This ensures that all traffic is routed through private endpoints, reducing the attack surface and preventing unauthorized access from outside the VNet.

**Technical Mechanisms and Implementation Methods:**  
- **Azure Private Link:** The implementation leverages Azure Private Link, which provides private connectivity between Azure services and VNets. When a private endpoint is created for a HorizonDB cluster, Azure allocates a private IP address from the specified VNet’s address space.
- **DNS Configuration:** With Private DNS integration, Azure automatically updates DNS records so that the HorizonDB cluster’s endpoint resolves to the private IP address. This eliminates manual DNS configuration and reduces operational complexity.
- **Network Security:** By disabling public access, the HorizonDB cluster is only accessible via the private endpoint, enforcing network isolation and compliance with internal security policies.

**Use Cases and Application Scenarios:**  
- **Enterprise Data Security:** Organizations with strict security requirements can use private endpoints to ensure that HorizonDB clusters are only accessible from within their corporate network or trusted Azure VNets.
- **Regulatory Compliance:** This feature supports compliance with regulations that mandate private connectivity and prohibit public exposure of sensitive data stores.
- **Hybrid and Multi-cloud Architectures:** Private endpoint support facilitates secure integration of HorizonDB clusters with on-premises networks via VPN or ExpressRoute, without exposing the database to the public internet.

**Important Considerations and Limitations:**  
- **VNet Configuration:** Proper configuration of VNets and subnet permissions is required to establish private endpoints.
- **DNS Resolution:** Ensure that Private DNS zones are correctly linked to VNets to enable seamless name resolution for HorizonDB clusters.
- **Disabling Public Access:** Once public access is disabled, all clients must connect via the private endpoint; misconfiguration may lead to connectivity issues.
- **Service Limits:** There may be Azure-imposed limits on the number of private endpoints per VNet or per HorizonDB cluster.

**Integration with Related Azure Services:**  
- **Azure Private Link:** The update is built on Azure Private Link, enabling secure connections to HorizonDB from VNets.
- **Azure Private DNS:** Integration with Private DNS zones automates endpoint resolution.
- **Network Security Groups (NSGs):** NSGs can be used to further restrict access to the private endpoint within the VNet.
- **Azure ExpressRoute/VPN Gateway:** For hybrid connectivity, private endpoints can be accessed from on-premises networks via ExpressRoute or VPN Gateway.

**Summary Sentence:**  
Azure HorizonDB clusters now support private endpoints via Azure Private Link, enabling secure, private connectivity with integrated DNS resolution and the option to disable public access, thereby enhancing security and simplifying network management for enterprise workloads.

---

### 28. Public Preview: Service tags for inbound rules in network security perimeter

**Published**: November 17, 2026 20:52:28 UTC
**Link**: [Public Preview: Service tags for inbound rules in network security perimeter](https://azure.microsoft.com/updates?id=579201)

**Update ID**: 579201
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure Private Link, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure announced the public preview of support for using service tags as inbound rules within network security perimeters, specifically for third-party customers.

- Key changes or new features  
This update allows customers to use Azure service tags directly in inbound rules for network security perimeter-protected resources. Service tags represent groups of IP addresses for Azure services, simplifying rule management by avoiding manual IP list updates. Previously, service tags were only supported for outbound rules; now, they can be used for inbound access control, streamlining configuration and maintenance.

- Target audience affected  
This update is relevant to developers, IT professionals, and network administrators managing Azure environments with network security perimeters, especially those integrating third-party solutions or requiring granular access control.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production workloads until general availability. Customers should review documentation for usage guidance and limitations. Using service tags for inbound rules can reduce operational overhead and improve security posture by ensuring access rules stay up-to-date with Azure service IP changes.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Service tags for inbound rules in network security perimeter  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579201)

---

**Background and Purpose of the Update**  
The public preview of "service tags as inbound rules" support for third-party customers in Azure's network security perimeter addresses the need for simplified and scalable access management to perimeter-protected resources. Traditionally, managing inbound access required specifying individual IP addresses or address ranges, which can be complex and error-prone, especially as cloud environments scale and evolve. The introduction of service tags for inbound rules aims to streamline this process, making it easier for customers to define and maintain secure access policies.

**Specific Features and Detailed Changes**  
This update introduces the capability for customers to use Azure service tags directly in inbound rules within the network security perimeter. Service tags represent a group of IP address prefixes for specific Azure services (such as Azure Storage, Azure SQL, etc.), allowing administrators to reference these tags instead of manually managing individual IP addresses. The change specifically extends this functionality to inbound rules, enabling third-party customers to leverage service tags for controlling access to their protected resources.

**Technical Mechanisms and Implementation Methods**  
Service tags are predefined in Azure and automatically updated as the underlying IP addresses change, ensuring that access policies remain current without manual intervention. With this update, customers can configure inbound rules in their network security perimeter by specifying service tags as the source in rule definitions. The Azure platform interprets these tags and applies the corresponding IP address ranges for traffic filtering. This mechanism reduces administrative overhead and minimizes the risk of misconfiguration due to outdated or incorrect IP lists.

**Use Cases and Application Scenarios**  
- **Simplified Access Management:** Organizations can allow inbound traffic from trusted Azure services (e.g., Azure App Service, Azure Key Vault) by referencing their service tags, rather than maintaining extensive IP lists.
- **Scalable Security Policies:** As cloud deployments grow, service tags help maintain consistent and scalable access controls across multiple resources and environments.
- **Third-Party Integrations:** Third-party customers can now more easily integrate their solutions with Azure services, using service tags to securely permit inbound traffic from specific Azure resources.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes based on customer feedback.
- **Scope:** The update is specifically for inbound rules in the network security perimeter and is targeted at third-party customers.
- **Service Tag Coverage:** Customers should verify which Azure services are supported by service tags and ensure that their access requirements align with available tags.
- **Rule Management:** While service tags simplify rule management, customers must still ensure that their overall security posture is maintained and that only necessary services are allowed inbound access.

**Integration with Related Azure Services**  
Service tags are already used in Azure Network Security Groups (NSGs), Azure Firewall, and other network security constructs. This update extends their applicability to inbound rules within the network security perimeter, enhancing integration and consistency across Azure's network security offerings. Customers can leverage service tags in conjunction with other Azure security features to build robust, easily managed access policies.

---

**Summary Sentence:**  
The public preview of service tags for inbound rules in Azure's network security perimeter enables third-party customers to simplify and automate access management to protected resources by referencing Azure service tags, reducing manual IP management and enhancing security policy scalability.

---

### 29. Public Preview: Perimeter link (cross perimeter) in network security perimeter

**Published**: November 17, 2026 20:51:13 UTC
**Link**: [Public Preview: Perimeter link (cross perimeter) in network security perimeter](https://azure.microsoft.com/updates?id=579206)

**Update ID**: 579206
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Azure Private Link, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure announced the public preview of "Perimeter link (cross perimeter)" functionality within network security perimeters.

- Key changes or new features  
This new capability allows secure connectivity between resources that are protected by different network security perimeters. It enables organizations to establish controlled, cross-perimeter communication while maintaining strong perimeter-based access controls. The feature supports scenarios where resources need to interact across separate security boundaries without compromising security policies.

- Target audience affected  
Developers and IT professionals responsible for designing, implementing, and managing Azure network security architectures, especially those leveraging network security perimeters for resource isolation and protection.

- Important notes  
The perimeter link feature is currently in public preview, so it may not be suitable for production workloads yet. Customers can use this capability to adopt network security perimeters more confidently, knowing that secure cross-perimeter connectivity is possible. Review documentation and preview limitations before integrating into critical environments.

**Details**:

**Azure Update Report: Public Preview – Perimeter Link (Cross Perimeter) in Network Security Perimeter**

**Background and Purpose of the Update**  
The introduction of the Perimeter Link (cross perimeter) capability addresses the need for secure connectivity between resources that are protected by distinct network security perimeters within Azure environments. Traditionally, network security perimeters are used to enforce strict access controls, isolating resources and reducing the attack surface. However, as enterprise architectures grow more complex and resources are distributed across multiple perimeters, there is a requirement to enable controlled, secure communication between these isolated environments without compromising security.

**Specific Features and Detailed Changes**  
This update provides a mechanism to establish secure connectivity between resources located in different network security perimeters. The Perimeter Link feature allows customers to maintain strong perimeter-based access controls while facilitating communication across perimeters. The key change is the ability to link perimeters securely, ensuring that access policies and security boundaries are preserved even when resources need to interact across perimeter boundaries.

**Technical Mechanisms and Implementation Methods**  
The Perimeter Link capability is implemented as a controlled connection between two or more network security perimeters. It leverages Azure’s existing perimeter-based access control frameworks to ensure that only authorized traffic can traverse the link. The implementation likely involves configuring explicit rules and policies at the perimeter boundaries, ensuring that traffic is authenticated, authorized, and monitored. The connectivity is designed to be secure, preventing unauthorized access and maintaining the integrity of each perimeter’s security posture.

**Use Cases and Application Scenarios**  
- **Multi-perimeter Enterprise Architectures:** Organizations with multiple network security perimeters (e.g., different business units, environments, or regulatory domains) can use Perimeter Link to enable secure communication between resources without weakening perimeter controls.
- **Hybrid and Multi-cloud Deployments:** Enterprises integrating Azure resources with other cloud providers or on-premises environments can maintain distinct perimeters and use Perimeter Link for secure cross-environment connectivity.
- **Regulatory Compliance:** Businesses subject to strict regulatory requirements can confidently adopt perimeter-based security models and still enable necessary inter-perimeter communication for operational needs.

**Important Considerations and Limitations**  
- **Security Posture:** While Perimeter Link enables cross-perimeter connectivity, it is essential to carefully configure access controls to prevent unintended exposure of resources.
- **Policy Management:** Administrators must ensure that perimeter policies are consistently enforced and updated to reflect changes in connectivity requirements.
- **Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes or limitations in functionality and support.

**Integration with Related Azure Services**  
Perimeter Link is designed to work alongside Azure’s network security perimeter capabilities. It integrates with Azure’s access control, monitoring, and security management services to provide a unified approach to perimeter security. Customers can leverage Azure Policy, Azure Firewall, and other network security tools to define and enforce rules governing cross-perimeter connectivity.

**Summary Sentence**  
The Perimeter Link (cross perimeter) feature in public preview enables secure connectivity between resources in different Azure network security perimeters, maintaining strong access controls and supporting complex enterprise architectures with enhanced perimeter-based security.

---

### 30. Public Preview: Agent Grid helping secure AI agent communications

**Published**: November 17, 2026 20:47:31 UTC
**Link**: [Public Preview: Agent Grid helping secure AI agent communications](https://azure.microsoft.com/updates?id=580684)

**Update ID**: 580684
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Security, Services

**Summary**:

- What was updated  
Agent Grid is now available in public preview, introducing identity-based Zero Trust network security for AI agents in supported Azure environments.

- Key changes or new features  
Agent Grid enables security teams to centrally manage and govern communications between AI agents, models, tools, and external services. It uses identity-based policies to enforce Zero Trust principles, ensuring only authorized entities can interact. This helps prevent unauthorized access and lateral movement between agents, improving the overall security posture of AI workloads.

- Target audience affected  
This update is relevant for developers building AI solutions, IT professionals managing Azure environments, and security teams responsible for securing AI agent communications.

- Important notes if any  
Agent Grid is currently in public preview, so features and support may evolve. Integration is available for supported Azure environments only. Security teams should review and update their network policies to leverage Agent Grid’s capabilities for AI agent communications. Early adoption can help identify potential gaps and provide feedback to Microsoft for future improvements.

Source: [Azure Update: Agent Grid public preview](https://azure.microsoft.com/updates?id=580684)

**Details**:

**Azure Update Report: Public Preview – Agent Grid Helping Secure AI Agent Communications**

**Background and Purpose of the Update**  
The introduction of Agent Grid in public preview addresses the growing need for robust security in AI-driven environments, particularly as organizations increasingly deploy AI agents that interact with various models, tools, and external services. The primary goal is to implement identity-based Zero Trust network security, ensuring that communications between AI agents and related components are strictly governed and protected against unauthorized access or lateral movement.

**Specific Features and Detailed Changes**  
Agent Grid provides a centralized, policy-driven approach to managing the network security of AI agents within supported Azure environments. Key features include:
- **Identity-Based Security:** Communications between agents, models, tools, and external services are governed based on the authenticated identity of each component, rather than relying solely on traditional network boundaries.
- **Zero Trust Principles:** The solution enforces Zero Trust by requiring explicit verification for every communication flow, minimizing implicit trust within the environment.
- **Centralized Policy Management:** Security teams can define, manage, and enforce communication policies from a central location, simplifying governance and reducing the risk of misconfiguration.

**Technical Mechanisms and Implementation Methods**  
Agent Grid operates by integrating with Azure’s identity infrastructure and network security controls. It authenticates each participating entity (agent, model, tool, or service) and applies centrally defined policies to determine whether communication is permitted. This mechanism typically involves:
- Leveraging Azure Active Directory (Azure AD) identities for authentication.
- Applying network segmentation and access controls based on identity, rather than just IP addresses or subnets.
- Monitoring and logging communication flows for audit and compliance purposes.
- Providing APIs or interfaces for security teams to manage and update policies as needed.

**Use Cases and Application Scenarios**  
Agent Grid is particularly valuable in scenarios where multiple AI agents need to interact securely, such as:
- **Multi-Agent AI Workflows:** Where agents collaborate on complex tasks and require secure, policy-driven communication.
- **Integration with External Services:** When AI agents must access third-party APIs or tools, Agent Grid ensures only authorized communications occur.
- **Regulated Environments:** Organizations subject to strict compliance requirements can leverage Agent Grid to demonstrate granular control over AI agent communications.

**Important Considerations and Limitations**  
- **Supported Environments:** Agent Grid is available only on supported Azure environments; compatibility with all Azure services or custom deployments may be limited during the public preview phase.
- **Policy Scope:** The effectiveness of Agent Grid depends on the accuracy and completeness of centrally managed policies; misconfiguration could lead to unintended communication blocks or exposures.
- **Preview Limitations:** As a public preview feature, Agent Grid may not offer full production support, and features or APIs could change before general availability.

**Integration with Related Azure Services**  
Agent Grid is designed to work in conjunction with Azure’s existing identity and security services, such as:
- **Azure Active Directory (Azure AD):** For identity management and authentication.
- **Azure Network Security Groups (NSGs) and Azure Firewall:** For enforcing network-level controls.
- **Azure Monitor and Azure Security Center:** For monitoring, logging, and alerting on communication flows and policy enforcement.

**Summary Sentence**  
Agent Grid, now in public preview, introduces identity-based Zero Trust network security for AI agent communications in supported Azure environments, enabling centralized policy management and enhanced governance over interactions among agents, models, tools, and external services.

---

### 31. Public Preview: Azure Adaptive Virtual Patching

**Published**: November 17, 2026 20:29:13 UTC
**Link**: [Public Preview: Azure Adaptive Virtual Patching](https://azure.microsoft.com/updates?id=580689)

**Update ID**: 580689
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Security, Services

**Summary**:

- What was updated  
Azure Adaptive Virtual Patching has entered Public Preview, introducing a new AI-driven security feature for Azure workloads.

- Key changes or new features  
The Adaptive Shield uses AI orchestration to provide virtual patching for Linux workloads. This feature aims to reduce exposure to zero-day vulnerabilities and newly disclosed threats by offering adaptive protection while customers test and deploy official software patches. The system dynamically applies mitigations, minimizing risk during the patching window.

- Target audience affected  
This update is relevant for developers, IT professionals, and security teams managing Linux workloads on Azure. It is particularly valuable for those responsible for vulnerability management and patching processes.

- Important notes if any  
The feature is currently focused on Linux workloads in Azure and is in Public Preview, meaning it may not be suitable for production environments yet. Adaptive Virtual Patching is intended as a temporary mitigation, not a replacement for official patches. Users should continue to apply vendor patches as soon as they are available. Early adopters can provide feedback to help improve the feature before general availability.

**Details**:

**Azure Update Report: Public Preview – Azure Adaptive Virtual Patching**

**Background and Purpose of the Update**  
Azure Adaptive Virtual Patching has been introduced in public preview to address the critical need for rapid mitigation of zero-day vulnerabilities, especially during the period when customers are testing and deploying official software patches. The update aims to reduce exposure to new, emerging, and newly disclosed vulnerabilities, thereby enhancing security posture for organizations leveraging Azure, with an initial focus on Linux workloads.

**Specific Features and Detailed Changes**  
The core feature of this update is the AI-orchestrated Adaptive Shield, which dynamically applies virtual patches to workloads. This shield operates by identifying vulnerabilities and deploying mitigations in real-time, specifically targeting zero-day threats before official patches are available or fully deployed. The initial release is tailored for Linux environments, providing protection for workloads running on this operating system.

**Technical Mechanisms and Implementation Methods**  
Azure Adaptive Virtual Patching leverages artificial intelligence to orchestrate the deployment of virtual patches. The AI engine continuously monitors workloads, detects vulnerabilities as they emerge, and applies adaptive mitigations without requiring manual intervention. The mechanism is designed to be non-intrusive, allowing organizations to continue their patch testing and deployment cycles while maintaining security. The Adaptive Shield acts as a layer between the workload and potential threats, intercepting exploit attempts and neutralizing them based on the latest threat intelligence and vulnerability disclosures.

**Use Cases and Application Scenarios**  
- **Zero-Day Vulnerability Mitigation:** Organizations can utilize Adaptive Virtual Patching to protect Linux workloads against newly discovered vulnerabilities, especially when official patches are not yet available or are being tested.
- **Patch Deployment Windows:** IT teams can maintain security during patch testing and deployment phases, reducing the risk of exploitation during these critical windows.
- **Continuous Security for Linux Workloads:** Enterprises running mission-critical Linux applications on Azure can benefit from ongoing protection, ensuring that their workloads remain secure even as new threats emerge.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which means it may not be suitable for production environments and could be subject to changes or limitations in functionality.
- **Linux Workload Focus:** The initial implementation is limited to Linux workloads; support for other operating systems is not included in this release.
- **AI-Orchestrated Mitigation:** While AI-driven, the effectiveness of virtual patching depends on the accuracy of vulnerability detection and the timeliness of mitigations. False positives or missed threats may occur.
- **Patch Lifecycle Integration:** Adaptive Virtual Patching is intended as a temporary mitigation measure and does not replace the need for official patch deployment.

**Integration with Related Azure Services**  
Azure Adaptive Virtual Patching can be integrated with existing Azure security services such as Azure Security Center and Azure Defender. This integration enables centralized visibility and management of virtual patching activities, threat detection, and compliance monitoring. The AI-orchestrated shield complements Azure’s broader security ecosystem, providing an additional layer of defense for Linux workloads.

**Summary Sentence**  
Azure Adaptive Virtual Patching in public preview delivers an AI-driven Adaptive Shield for Linux workloads, offering real-time mitigation of zero-day vulnerabilities during patch testing and deployment, thereby enhancing security and reducing risk exposure within Azure environments.

---

### 32. Public Preview: AI Security add-on for Azure Firewall Premium

**Published**: November 17, 2026 20:27:29 UTC
**Link**: [Public Preview: AI Security add-on for Azure Firewall Premium](https://azure.microsoft.com/updates?id=580694)

**Update ID**: 580694
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Firewall, Microsoft Ignite, Services, Feature

**Summary**:

- What was updated  
Azure Firewall Premium now offers a new AI Security add-on, available in public preview.

- Key changes or new features  
The AI Security add-on introduces five new capabilities focused on protecting AI workloads and applications. These include enhanced protection for AI apps, improved safeguarding of sensitive data, advanced malware and application defenses, and additional tools to secure AI-driven environments. The add-on leverages AI-powered threat detection and prevention to address emerging risks specific to AI and machine learning workloads.

- Target audience affected  
This update is relevant for developers building AI applications, IT professionals managing Azure Firewall Premium, and security teams responsible for securing cloud-based AI workloads.

- Important notes if any  
The AI Security add-on is currently in public preview, so features may change before general availability. Early adoption is recommended for organizations seeking to enhance security for AI workloads, but production use should be carefully evaluated. Integration with Azure Firewall Premium is required. For more details and to participate in the preview, visit the official Azure Update [link](https://azure.microsoft.com/updates?id=580694).

**Details**:

**Azure Update Technical Explanation: Public Preview – AI Security add-on for Azure Firewall Premium**

**Background and Purpose of the Update**  
The AI Security add-on for Azure Firewall Premium has been introduced to address the growing need for advanced security controls specifically tailored to AI applications and workloads. With the increasing adoption of AI in enterprise environments, protecting AI models, data, and associated infrastructure from evolving threats has become critical. This update, announced at Microsoft Ignite, aims to enhance the security posture of organizations leveraging AI by providing specialized capabilities within the Azure Firewall Premium offering.

**Specific Features and Detailed Changes**  
The AI Security add-on introduces five new capabilities designed to:  
- Protect AI applications  
- Safeguard sensitive data  
- Strengthen defenses against malware  
- Enhance application security

While the detailed breakdown of each capability is not provided in the announcement, the focus is clearly on augmenting the existing Azure Firewall Premium feature set with AI-specific protections. These enhancements are expected to provide targeted controls and monitoring for AI workloads, addressing unique risks such as data exfiltration, model theft, and adversarial attacks.

**Technical Mechanisms and Implementation Methods**  
The AI Security add-on is delivered as an extension to Azure Firewall Premium, leveraging the platform’s advanced threat intelligence, deep packet inspection, and application filtering capabilities. The add-on likely operates by integrating with the firewall’s rule processing engine, enabling the inspection and enforcement of security policies tailored for AI traffic patterns and data flows. It may utilize machine learning-driven detection algorithms to identify anomalous behavior or threats specific to AI environments.

Deployment is managed through the Azure Portal, CLI, or ARM templates, consistent with other Azure Firewall Premium add-ons. Configuration and policy management are integrated into the existing Azure Firewall management experience, ensuring a unified security operations workflow.

**Use Cases and Application Scenarios**  
- **Securing AI APIs and Endpoints:** Protecting RESTful or gRPC endpoints serving AI models from unauthorized access or abuse.
- **Safeguarding Training Data:** Monitoring and controlling access to sensitive datasets used in AI training pipelines.
- **Defending Against Model Extraction:** Detecting and blocking attempts to exfiltrate AI models or intellectual property.
- **Preventing Malware in AI Workloads:** Enhancing inspection of traffic to and from AI compute resources to block malicious payloads.
- **Compliance for Regulated Industries:** Enabling organizations in healthcare, finance, or government to meet regulatory requirements for AI data protection.

**Important Considerations and Limitations**  
- The AI Security add-on is currently in public preview, which means it may not be suitable for production workloads requiring full SLA-backed support.
- Features and capabilities are subject to change based on customer feedback and ongoing development.
- Integration and compatibility with existing Azure Firewall Premium policies should be validated in test environments before broad deployment.

**Integration with Related Azure Services**  
The add-on is designed to work seamlessly with Azure Firewall Premium and can be used alongside other Azure security services such as Microsoft Defender for Cloud, Azure Sentinel, and Azure Policy. This enables a layered security approach, with the AI Security add-on providing specialized controls at the network perimeter, while other services deliver endpoint, workload, and compliance protections.

**Summary Sentence**  
The AI Security add-on for Azure Firewall Premium, now in public preview, introduces five targeted capabilities to enhance the protection of AI applications and sensitive data, strengthening defenses against malware and application threats within Azure environments.

---

### 33. Public Preview: Azure Bastion RDP and SSH vision

**Published**: November 17, 2026 20:25:18 UTC
**Link**: [Public Preview: Azure Bastion RDP and SSH vision](https://azure.microsoft.com/updates?id=580699)

**Update ID**: 580699
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Bastion, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Bastion RDP and SSH vision is now available in public preview, introducing AI-assisted review capabilities for recorded privileged sessions.

- Key changes or new features  
This update enables AI-driven analysis of RDP and SSH session recordings within Azure Bastion. Security and operations teams can access automated session summaries and receive insights highlighting noteworthy or risky activities performed during administrative access. The AI assists in identifying potential security concerns and unusual behavior, streamlining session review and audit processes.

- Target audience affected  
This update is relevant for developers, IT professionals, and security teams who manage privileged access to Azure resources using Azure Bastion. Organizations with compliance, security, or operational monitoring requirements will benefit from enhanced session visibility and risk assessment.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production environments. AI-assisted session review can help reduce manual effort and improve detection of suspicious activity, but users should validate findings and continue to follow established security best practices. Integration with Azure Bastion requires proper configuration of session recording and access policies.

**Details**:

**Azure Update Report: Public Preview – Azure Bastion RDP and SSH Vision**

**Background and Purpose of the Update**  
Azure Bastion provides secure, seamless RDP and SSH connectivity to virtual machines directly through the Azure portal, without exposing VMs to public IP addresses. The new “RDP and SSH vision” feature, now in public preview, addresses the need for enhanced oversight of privileged access sessions. By leveraging AI-assisted review capabilities, this update aims to help security and operations teams gain deeper visibility into administrative activity, specifically focusing on identifying noteworthy and risky actions within recorded sessions.

**Specific Features and Detailed Changes**  
- **AI-Assisted Session Review:** The update introduces automated session summaries for RDP and SSH connections established via Azure Bastion.  
- **Insights into Activity:** The system highlights notable and potentially risky behaviors detected during privileged sessions, enabling rapid assessment by security teams.  
- **Session Recording Integration:** The feature works with recorded sessions, providing post-session analysis rather than real-time monitoring.  
- **Summarization and Risk Identification:** AI models generate concise summaries and flag actions that may warrant further investigation, such as unusual command execution or access patterns.

**Technical Mechanisms and Implementation Methods**  
- **Session Data Collection:** Azure Bastion records privileged session activity (RDP/SSH) as part of its session recording capabilities.  
- **AI Processing Pipeline:** Recorded session data is processed by AI models, which analyze command histories, user actions, and session metadata to produce summaries and risk insights.  
- **Review Interface:** Security and operations teams access these AI-generated summaries and risk indicators through the Azure portal, streamlining the review process and reducing manual effort.

**Use Cases and Application Scenarios**  
- **Privileged Access Monitoring:** Organizations with strict compliance and security requirements can use AI-assisted reviews to monitor administrative access to critical VMs.  
- **Incident Response:** Security teams can quickly identify risky activity within recorded sessions, aiding in faster response and investigation.  
- **Audit and Compliance:** Automated session summaries facilitate audit processes by providing clear, concise records of privileged actions, supporting regulatory requirements.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which means it may not be suitable for production environments and could be subject to changes or limitations.  
- **Scope of Analysis:** The AI-assisted review is limited to recorded sessions; real-time detection or prevention of risky activity is not included.  
- **Accuracy and Coverage:** As with any AI-driven feature, the accuracy of risk identification and summarization may vary, and manual review is still recommended for critical scenarios.

**Integration with Related Azure Services**  
- **Azure Bastion:** The feature is directly integrated with Azure Bastion’s session recording capabilities, enhancing its security monitoring functions.  
- **Azure Security Center/Defender:** While not explicitly stated, insights generated by this feature can complement broader security monitoring and incident response workflows within Azure’s security ecosystem.  
- **Azure Portal:** All review and analysis functions are accessible through the Azure portal, ensuring seamless integration with existing administrative workflows.

**Summary Sentence**  
Azure Bastion RDP and SSH vision, now in public preview, introduces AI-assisted review of recorded privileged sessions, providing automated summaries and risk insights to help security and operations teams efficiently monitor and understand administrative activity.

---

### 34. Public Preview: Azure API Management Application

**Published**: November 17, 2026 20:15:03 UTC
**Link**: [Public Preview: Azure API Management Application](https://azure.microsoft.com/updates?id=581277)

**Update ID**: 581277
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Ignite

**Summary**:

- What was updated  
Azure API Management has introduced the Applications feature, now available in public preview to all customers without the need for sign-up or registration.

- Key changes or new features  
The Applications feature enables users to organize APIs based on the consuming applications, allowing for improved management and visibility at the application level. It provides a centralized way to group APIs, manage credentials, and monitor usage per application. This streamlines API governance, simplifies access control, and enhances the developer experience by making it easier to track which APIs are used by which applications.

- Target audience affected  
Developers and IT professionals who use Azure API Management to expose, secure, and manage APIs. Teams responsible for API lifecycle management, application integration, and security will benefit from improved organization and control.

- Important notes if any  
The Applications feature is currently in public preview, so it may lack some functionality or stability compared to GA releases. No registration is required to use the feature. Users should review documentation and monitor for updates as the feature evolves. This update supports better API management practices and can help organizations scale their API ecosystem more efficiently.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure API Management Application  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581277)

---

**Background and Purpose of the Update:**  
The Applications feature in Azure API Management (APIM) has entered public preview, now accessible to all customers without the need for sign-up or registration. This update addresses the need for a more organized and application-centric approach to API management, enabling IT professionals to efficiently group APIs based on their consuming applications. The primary purpose is to simplify API governance, enhance visibility, and streamline management at the application level rather than solely at the API or product level.

---

**Specific Features and Detailed Changes:**  
- **Applications Entity:** A new organizational construct within APIM, allowing APIs to be grouped and managed according to the consuming application.
- **Streamlined Management:** Enables centralized control of API access, policies, and lifecycle for each application, reducing complexity in environments with multiple APIs and consumers.
- **No Registration Required:** The feature is available in public preview to all Azure customers, facilitating immediate adoption and experimentation without additional onboarding steps.

---

**Technical Mechanisms and Implementation Methods:**  
- **Application-Centric API Grouping:** APIs can now be associated with specific applications, creating logical boundaries and facilitating easier tracking of usage, access, and permissions.
- **Management Interface:** The APIM portal or API may provide new interfaces or endpoints for creating, viewing, and managing applications, though details on UI or API changes are not specified in the update.
- **Policy Enforcement:** Application-level policies can be applied, enabling fine-grained control over API consumption, quotas, and security for each application grouping.

---

**Use Cases and Application Scenarios:**  
- **Multi-Consumer Environments:** Organizations with numerous internal or external applications consuming APIs can use this feature to segment and manage API access per application.
- **Lifecycle Management:** IT teams can track which APIs are used by which applications, facilitating deprecation, versioning, and migration strategies.
- **Security and Compliance:** Application-level grouping allows for targeted policy enforcement, audit, and compliance tracking for each consuming application.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads requiring full support or SLA guarantees.
- **Feature Scope:** The update does not specify advanced features such as automation, analytics, or integration points, so users should validate current capabilities before adoption.
- **Documentation and Support:** Users should consult official Azure documentation for detailed guidance, as preview features may evolve rapidly.

---

**Integration with Related Azure Services:**  
- **Azure API Management:** The Applications feature is native to APIM and enhances its organizational capabilities.
- **Azure Identity and Access Management:** Application-level grouping may facilitate integration with Azure AD for authentication and authorization, though specifics are not detailed in the update.
- **Monitoring and Analytics:** Application grouping can improve the granularity of monitoring and reporting, allowing IT professionals to analyze API usage by application.

---

**Summary Sentence:**  
The public preview of the Applications feature in Azure API Management introduces a streamlined, application-centric approach to organizing and managing APIs, enabling IT professionals to efficiently control access, policies, and lifecycle at the application level, with immediate availability and no registration required.

---

### 35. Public Preview: Scale ExpressRoute Direct connectivity with link groups

**Published**: November 17, 2026 20:15:03 UTC
**Link**: [Public Preview: Scale ExpressRoute Direct connectivity with link groups](https://azure.microsoft.com/updates?id=580926)

**Update ID**: 580926
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Networking, Azure ExpressRoute, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure ExpressRoute Direct now supports link groups in public preview, allowing users to scale connectivity more efficiently.

- Key changes or new features  
Link groups enable aggregation of multiple ExpressRoute Direct links into a single logical group. This allows high-throughput workloads to utilize combined bandwidth across several links, simplifying management and reducing the need to handle multiple independent ExpressRoute connections. Link groups also streamline configuration, monitoring, and failover processes.

- Target audience affected  
This update is relevant to network architects, IT professionals, and developers managing high-throughput workloads, hybrid cloud environments, or requiring scalable, reliable Azure connectivity via ExpressRoute Direct.

- Important notes if any  
Link groups are currently in public preview and may not be suitable for production workloads until general availability. Users should review documentation for limitations and best practices. This feature is designed to reduce operational complexity and improve scalability for ExpressRoute Direct deployments.

**Details**:

**Azure Update Report: Public Preview – Scale ExpressRoute Direct Connectivity with Link Groups**

**Background and Purpose of the Update**  
Azure ExpressRoute Direct enables customers to connect their on-premises infrastructure directly to Microsoft’s backbone network, supporting high-throughput and mission-critical workloads. Traditionally, scaling ExpressRoute Direct connectivity required managing multiple independent connections, which increased operational complexity and made it difficult to efficiently aggregate bandwidth and manage failover scenarios. The introduction of link groups addresses these challenges by providing a more streamlined approach to scaling and managing ExpressRoute Direct connections.

**Specific Features and Detailed Changes**  
The update introduces "link groups" for ExpressRoute Direct in public preview. Link groups allow customers to aggregate multiple physical links under a single logical group, simplifying the management of high-throughput connections. Instead of configuring and monitoring each ExpressRoute connection separately, IT professionals can now group links together, enabling easier scaling of bandwidth and improved operational efficiency. This feature is particularly beneficial for organizations with large-scale workloads requiring substantial network throughput.

**Technical Mechanisms and Implementation Methods**  
Link groups are implemented as a logical construct within ExpressRoute Direct. When configuring ExpressRoute Direct, users can now create a link group and assign multiple physical links to it. The link group acts as a single entity for configuration, monitoring, and management purposes. This aggregation allows for seamless scaling by simply adding or removing links from the group, without the need to reconfigure individual connections. The mechanism reduces manual intervention and potential configuration errors, as operational tasks are performed at the group level rather than the individual link level.

**Use Cases and Application Scenarios**  
- **High-Throughput Workloads:** Enterprises running data-intensive applications, such as large-scale analytics, backup, or disaster recovery, can leverage link groups to aggregate bandwidth and ensure reliable connectivity.
- **Simplified Operations:** Organizations with multiple ExpressRoute Direct links can reduce operational overhead by managing link groups instead of individual connections.
- **Scalable Network Architecture:** Businesses anticipating growth in network traffic can easily scale their connectivity by adding links to existing groups, supporting dynamic workload requirements.

**Important Considerations and Limitations**  
- The feature is currently in public preview, meaning it may not be suitable for production workloads until general availability.
- Operational processes and monitoring should be adapted to leverage link groups, as traditional individual link management may not be compatible.
- Customers should review ExpressRoute Direct documentation for specific configuration steps and supported limits regarding the number of links per group.
- Integration with existing network monitoring and automation tools may require updates to support the new link group construct.

**Integration with Related Azure Services**  
Link groups in ExpressRoute Direct integrate with Azure networking services, including Virtual Networks (VNets), Network Security Groups (NSGs), and Azure Monitor. The aggregated connectivity provided by link groups can be used to connect multiple VNets or support hybrid cloud scenarios. Monitoring and alerting can be performed at the link group level, providing consolidated visibility into network health and performance.

**Summary Sentence**  
Azure ExpressRoute Direct now supports link groups in public preview, enabling IT professionals to efficiently scale high-throughput connectivity by aggregating multiple links into a single logical group, thereby reducing operational complexity and streamlining network management.

---

### 36. Public Preview: Agent Sandbox cluster extension

**Published**: November 17, 2026 20:15:03 UTC
**Link**: [Public Preview: Agent Sandbox cluster extension](https://azure.microsoft.com/updates?id=580916)

**Update ID**: 580916
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite

**Summary**:

- What was updated  
Azure announced the Public Preview of the Agent Sandbox cluster extension for Kubernetes.

- Key changes or new features  
This extension provides a managed solution for running AI agents that execute untrusted, model-generated code in isolated environments. It automates the creation and lifecycle management of sandboxed sessions, including storage and warm-up logic, reducing operational complexity for teams. The extension integrates with Kubernetes clusters, allowing developers to securely run code with minimal manual setup.

- Target audience affected  
Developers and IT professionals building AI agent solutions on Kubernetes, especially those needing secure, isolated execution environments for untrusted code.

- Important notes  
The Agent Sandbox cluster extension is currently in Public Preview and may not be suitable for production workloads yet. It addresses common pain points such as manual sandbox orchestration and storage management, streamlining secure AI agent deployment. Early adopters should review documentation and test thoroughly before full adoption.

**Details**:

**Azure Update: Public Preview – Agent Sandbox Cluster Extension**

**Background and Purpose of the Update**  
The Agent Sandbox cluster extension addresses a critical need for securely running AI agents that execute untrusted, model-generated code. Traditionally, teams deploying such workloads on Kubernetes must manually construct isolated environments for each session, including sandbox lifecycle management, storage provisioning, and environment warm-up. This manual approach increases operational complexity and overhead, making it challenging to scale and maintain secure, reliable agent execution environments.

**Specific Features and Detailed Changes**  
The Agent Sandbox cluster extension introduces a managed solution for session isolation within Kubernetes clusters. Key features include:

- **Automated Sandbox Lifecycle Management:** The extension automates the creation, management, and teardown of sandbox environments for each agent session, reducing manual intervention.
- **Session Isolation:** Each AI agent session is provisioned with a dedicated, isolated environment, preventing cross-session interference and enhancing security when running untrusted code.
- **Integrated Storage and Warm-Up Logic:** Storage resources and environment initialization are handled by the extension, streamlining the setup process and ensuring consistent session readiness.
- **Cluster-Level Integration:** The extension operates at the cluster level, enabling centralized control and monitoring of sandbox environments across multiple workloads.

**Technical Mechanisms and Implementation Methods**  
The extension is deployed as a cluster-level add-on within Azure Kubernetes Service (AKS) or compatible Kubernetes environments. It leverages Kubernetes primitives such as namespaces, pods, and persistent volumes to enforce isolation and manage resources. The extension orchestrates sandbox lifecycle events (creation, initialization, teardown) through custom controllers and operators, ensuring that each session is provisioned with the necessary resources and security boundaries. Storage integration is achieved via dynamic provisioning of persistent volumes, while warm-up logic is executed as part of the sandbox initialization process.

**Use Cases and Application Scenarios**  
- **AI Agent Execution:** Teams deploying AI agents that generate and execute code (e.g., autonomous scripting, code generation, or data processing) benefit from secure, isolated environments for each session.
- **Model Testing and Evaluation:** Researchers and developers can safely test and evaluate new models that produce executable code without risking cluster-wide security or stability.
- **Multi-Tenant AI Platforms:** Organizations offering AI services to multiple users or teams can ensure session isolation, preventing data leakage and unauthorized access between tenants.

**Important Considerations and Limitations**  
- **Public Preview Status:** The extension is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes or limitations in functionality.
- **Operational Overhead Reduction:** While the extension reduces manual effort, teams should evaluate compatibility with existing workflows and ensure proper integration with their Kubernetes environments.
- **Security Boundaries:** The extension enhances session isolation but does not eliminate the need for broader cluster security practices, such as RBAC, network policies, and vulnerability management.

**Integration with Related Azure Services**  
The Agent Sandbox cluster extension is designed for seamless integration with Azure Kubernetes Service (AKS), leveraging Azure-native storage solutions (such as Azure Disk or Azure Files) for persistent storage provisioning. It can also be combined with Azure monitoring and logging services to track sandbox lifecycle events and resource usage. Teams may integrate the extension with Azure DevOps pipelines for automated deployment and testing of AI agents in isolated environments.

**Summary Sentence**  
The Agent Sandbox cluster extension, now in public preview, provides automated, session-isolated environments for securely running AI agents on Kubernetes, reducing operational overhead and enhancing security when executing untrusted, model-generated code.

---

### 37. Generally Available: IBM Spectrum LSF integration with Azure Compute Fleet

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: IBM Spectrum LSF integration with Azure Compute Fleet](https://azure.microsoft.com/updates?id=581259)

**Update ID**: 581259
**Data source**: Azure Updates API

**Categories**: Launched, Features, Microsoft Ignite

**Summary**:

- What was updated  
IBM Spectrum LSF is now generally available with integration for Azure Compute Fleet, enabling elastic and cost-efficient orchestration of high-performance computing (HPC) workloads in Azure.

- Key changes or new features  
The IBM LSF Resource Connector for Azure Compute Fleet allows automated provisioning and releasing of Azure compute resources based on real-time workload demand. This integration supports dynamic scaling, optimizing resource usage and costs. It also enables seamless extension of on-premises LSF environments into Azure, facilitating hybrid HPC architectures.

- Target audience affected  
Technical professionals managing HPC workloads, including IT administrators, cloud architects, and developers using IBM Spectrum LSF for job scheduling and resource management. Organizations seeking to extend or migrate HPC workloads to Azure will benefit from this update.

- Important notes if any  
This integration streamlines hybrid and cloud-native HPC operations, reducing manual intervention and improving resource efficiency. Developers can leverage Azure’s scalable infrastructure without modifying existing LSF workflows. IT professionals should review Azure Compute Fleet prerequisites and ensure proper configuration for optimal performance and cost management. For detailed guidance and setup instructions, refer to the official Azure documentation.

**Details**:

**Azure Update Report: IBM Spectrum LSF integration with Azure Compute Fleet (Generally Available)**

**Background and Purpose of the Update**  
This update announces the general availability of IBM Spectrum LSF integration with Azure Compute Fleet, targeting organizations running high-performance computing (HPC) workloads. The purpose is to enable elastic and cost-efficient orchestration of HPC jobs by dynamically provisioning and releasing Azure compute resources based on workload demand, thereby extending on-premises LSF environments into the Azure cloud.

**Specific Features and Detailed Changes**  
- **IBM LSF Resource Connector for Azure Compute Fleet:** The integration introduces a resource connector that allows IBM Spectrum LSF to interact directly with Azure Compute Fleet.  
- **Dynamic Provisioning:** Compute resources in Azure are automatically provisioned and released according to the real-time requirements of HPC workloads managed by LSF.  
- **Elastic Scaling:** The connector enables seamless scaling, ensuring that compute capacity is available when needed and deallocated when idle, optimizing cost and resource utilization.  
- **Hybrid Extension:** On-premises LSF environments can now be extended to Azure, allowing organizations to leverage cloud resources for overflow or burst workloads.

**Technical Mechanisms and Implementation Methods**  
- **Resource Connector Architecture:** The IBM LSF Resource Connector acts as an intermediary between LSF and Azure Compute Fleet. It monitors job queues and workload demand within LSF and communicates with Azure APIs to manage compute resources.  
- **API Integration:** The connector utilizes Azure Compute Fleet APIs to request, provision, and release virtual machines (VMs) or compute instances as needed.  
- **Policy-Based Management:** Resource allocation is governed by LSF policies, which determine when and how resources are provisioned based on workload characteristics and priorities.  
- **Automated Lifecycle Management:** The connector automates the lifecycle of compute resources, including startup, shutdown, and deallocation, minimizing manual intervention.

**Use Cases and Application Scenarios**  
- **Bursting HPC Workloads:** Organizations with on-premises LSF clusters can burst into Azure during peak demand periods, ensuring timely completion of computational jobs without over-provisioning local infrastructure.  
- **Cost Optimization:** By dynamically scaling compute resources, users can reduce cloud costs by only paying for resources when they are actively used.  
- **Hybrid HPC Environments:** Enterprises can create hybrid HPC environments, combining on-premises and cloud resources for flexible and scalable workload management.

**Important Considerations and Limitations**  
- **Resource Limits:** Users must be aware of Azure Compute Fleet quotas and limits, which may affect the maximum scale of HPC workloads.  
- **Network Connectivity:** Reliable connectivity between on-premises LSF and Azure is required for seamless integration and resource management.  
- **Security and Compliance:** Proper configuration of authentication, authorization, and compliance policies is necessary when extending LSF environments to Azure.  
- **Cost Management:** While elastic scaling optimizes costs, users should monitor usage and set appropriate policies to avoid unexpected expenses.

**Integration with Related Azure Services**  
- **Azure Compute Fleet:** The integration is directly with Azure Compute Fleet, leveraging its elastic compute provisioning capabilities.  
- **Azure APIs:** The connector interacts with Azure APIs for resource management.  
- **Potential for Integration with Azure Networking and Storage:** While not explicitly mentioned, typical HPC workloads may also require integration with Azure networking and storage services for data transfer and job execution.

**Summary Sentence:**  
The general availability of IBM Spectrum LSF integration with Azure Compute Fleet enables elastic, automated, and cost-efficient orchestration of HPC workloads, allowing organizations to extend their on-premises LSF environments into Azure for dynamic resource scaling and optimized cloud utilization.

---

### 38. Public Preview: Azure Artifact Validation for VM images

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Artifact Validation for VM images](https://azure.microsoft.com/updates?id=581249)

**Update ID**: 581249
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Artifact Validation for VM images is now available in public preview.

- Key changes or new features  
This feature enables VM image publishers and enterprise platform teams to run Azure’s certification-grade quality and security checks directly within their own Azure subscriptions. Validation can be performed at any stage of the image build process, allowing early detection of issues before publishing or deployment. Previously, these checks were only available during the Azure Marketplace publishing process.

- Target audience affected  
Developers, IT professionals, and enterprise platform teams who build, manage, or publish custom VM images in Azure.

- Important notes  
Artifact Validation helps ensure VM images meet Azure’s quality and security standards, reducing risk and improving compliance. It streamlines the image validation workflow, allowing integration into CI/CD pipelines and build processes. This preview is especially beneficial for organizations seeking to maintain high standards for internal or marketplace VM images.  
For more details, visit: https://azure.microsoft.com/updates?id=581249

**Details**:

**Azure Update Report: Public Preview – Azure Artifact Validation for VM Images**

**Background and Purpose of the Update**  
Azure Artifact Validation addresses the need for VM image publishers and enterprise platform teams to ensure their images meet Azure’s certification-grade quality and security standards. Previously, such validation was only available as part of Azure’s centralized processes, limiting flexibility and control for publishers. The update introduces the ability to run these checks within the publisher’s own Azure subscription, at any point during the image build lifecycle, empowering teams to proactively identify and remediate issues before submission or deployment.

**Specific Features and Detailed Changes**  
- **Self-Service Validation**: Publishers and enterprise teams can now execute Azure’s quality and security validation checks directly, rather than relying on post-submission validation.
- **Integration into Build Pipelines**: Validation can be triggered at any stage of the image build process, enabling continuous compliance and early detection of issues.
- **Certification-Grade Checks**: The validation process leverages the same standards and checks used by Azure’s certification workflows, ensuring consistency and reliability.
- **Public Preview Availability**: The feature is currently in public preview, allowing users to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Azure Subscription-Based Execution**: Artifact Validation runs within the user’s own Azure subscription, utilizing Azure resources and permissions.
- **Automated Validation Workflows**: The validation process can be integrated into CI/CD pipelines, using Azure-native tooling or custom scripts to automate checks after image builds.
- **Quality and Security Checks**: The validation encompasses a suite of tests, including security vulnerability scans, configuration compliance, and quality assurance, mirroring Azure’s certification requirements.
- **Reporting and Remediation**: Results are provided to the publisher, allowing for immediate remediation of any issues identified during validation.

**Use Cases and Application Scenarios**  
- **Independent Software Vendors (ISVs)**: ISVs can validate VM images prior to publishing in the Azure Marketplace, ensuring compliance and reducing time-to-market.
- **Enterprise Platform Teams**: Enterprises managing custom VM images for internal use can integrate validation into their DevOps pipelines, maintaining high standards for security and reliability.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Artifact Validation can be embedded in CI/CD workflows, providing automated quality gates before images are deployed to production environments.

**Important Considerations and Limitations**  
- **Public Preview Status**: As the feature is in public preview, it may not be suitable for production-critical workloads and could be subject to changes based on user feedback.
- **Subscription Requirements**: Validation must be executed within the publisher’s Azure subscription, requiring appropriate permissions and resource availability.
- **Scope of Checks**: The validation covers certification-grade quality and security checks, but users should verify the specific tests included and ensure they meet organizational requirements.

**Integration with Related Azure Services**  
- **Azure Marketplace Publishing**: Artifact Validation streamlines the process for ISVs preparing images for Marketplace publication.
- **Azure DevOps and CI/CD Tools**: The feature can be integrated with Azure DevOps pipelines and other CI/CD tools, enhancing automation and compliance.
- **Azure Security Center**: While Artifact Validation focuses on VM image quality and security, it complements ongoing security monitoring provided by Azure Security Center.

**Summary Sentence**  
Azure Artifact Validation, now in public preview, enables VM image publishers and enterprise platform teams to proactively run Azure’s certification-grade quality and security checks within their own Azure subscriptions at any stage of the build process, enhancing image reliability and compliance.

---

### 39. Public Preview: VM adaptive placement

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: VM adaptive placement](https://azure.microsoft.com/updates?id=581244)

**Update ID**: 581244
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure has introduced VM adaptive placement in public preview.

- Key changes or new features  
VM adaptive placement improves the success rate of Azure VM deployments when regional capacity is limited. Traditionally, VM creation requires specifying an exact size, and deployments fail if that size is unavailable. With adaptive placement, Azure will automatically select a similar VM size if the requested one is not available, reducing deployment failures and improving resource utilization. This feature is available during VM creation and can be enabled via API or portal.

- Target audience affected  
Developers and IT professionals who deploy VMs in Azure, especially those managing large-scale or automated deployments in regions with fluctuating capacity.

- Important notes if any  
Adaptive placement is currently in public preview and may not be available in all regions or for all VM sizes. It is recommended to review documentation and test deployments to ensure compatibility with workload requirements. This feature can help minimize downtime and deployment delays caused by capacity constraints, but may result in VMs with slightly different specifications than originally requested.  
[Azure Update Link](https://azure.microsoft.com/updates?id=581244)

**Details**:

**Azure Update Report: Public Preview – VM Adaptive Placement**

**Background and Purpose of the Update**  
Azure VM adaptive placement addresses a common challenge in cloud resource management: deployment failures due to constrained capacity. Traditionally, when deploying a virtual machine (VM) in Azure, users specify a single, exact VM size. If the requested size is unavailable in the target region or availability zone, the deployment fails, causing delays and requiring manual intervention. The purpose of this update is to improve deployment success rates and streamline VM provisioning, especially in environments where capacity is limited or fluctuating.

**Specific Features and Detailed Changes**  
The VM adaptive placement feature introduces a new approach to VM creation. Instead of strictly specifying one VM size, adaptive placement allows Azure to automatically select an alternative VM size if the requested size is unavailable. This increases the likelihood of successful VM deployments by providing flexibility in size selection. The feature is currently available in public preview, enabling customers to test and evaluate its effectiveness in real-world scenarios.

**Technical Mechanisms and Implementation Methods**  
When adaptive placement is enabled during VM creation, Azure’s deployment engine evaluates available capacity across the specified region or availability zone. If the exact requested VM size cannot be provisioned, the system dynamically searches for compatible VM sizes within the same VM family or similar specifications. Azure then selects the next best available size and proceeds with deployment, minimizing the risk of failure due to capacity constraints. This mechanism leverages Azure’s internal resource allocation algorithms and capacity monitoring to optimize placement decisions.

**Use Cases and Application Scenarios**  
VM adaptive placement is particularly beneficial in the following scenarios:
- **Large-scale deployments:** Enterprises deploying hundreds or thousands of VMs can reduce deployment failures and operational overhead.
- **Disaster recovery and high-availability setups:** Adaptive placement ensures that critical workloads can be provisioned even during regional capacity shortages.
- **Dev/Test environments:** Developers can quickly spin up VMs without worrying about size-specific capacity issues.
- **Burst workloads:** Organizations with variable or unpredictable demand can maintain agility and avoid delays in resource provisioning.

**Important Considerations and Limitations**  
- **Preview status:** The feature is in public preview and may not be suitable for production workloads requiring strict VM size specifications.
- **Size compatibility:** Adaptive placement may select a VM size with different resource characteristics (CPU, memory, etc.), which could impact application performance or licensing requirements.
- **Control and transparency:** Users should review deployment logs to understand which VM size was ultimately provisioned.
- **Policy and compliance:** Organizations with strict compliance or performance requirements should evaluate the impact of alternative VM sizes before enabling adaptive placement.

**Integration with Related Azure Services**  
VM adaptive placement integrates seamlessly with Azure’s VM provisioning workflows and can be used alongside other Azure services such as Azure Resource Manager, Azure Automation, and Azure Policy. It complements existing features like VM scale sets and availability sets by enhancing deployment reliability and flexibility.

**Summary Sentence**  
VM adaptive placement, now in public preview, enhances Azure VM deployment reliability by automatically selecting alternative VM sizes when capacity is constrained, thereby reducing deployment failures and improving operational efficiency for IT professionals.

---

### 40. Generally Available: Discover Data Guardian from Sovereign Control Panel

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Discover Data Guardian from Sovereign Control Panel](https://azure.microsoft.com/updates?id=581226)

**Update ID**: 581226
**Data source**: Azure Updates API

**Categories**: Launched, Features, Microsoft Ignite

**Summary**:

- What was updated  
Data Guardian is now discoverable directly from the Sovereign Control Panel, which is in Public Preview.

- Key changes or new features  
Data Guardian offers enhanced operational oversight for qualifying remote access by Microsoft engineers to production systems within the EU data boundary. This integration allows customers to easily locate and utilize Data Guardian features from the Sovereign Control Panel interface, improving transparency and control over Microsoft support activities.

- Target audience affected  
This update is relevant for developers, IT professionals, and compliance teams managing workloads in the EU data boundary, especially those requiring strict oversight of Microsoft engineer access to production environments.

- Important notes  
The Sovereign Control Panel is currently in Public Preview, so features may evolve. Data Guardian is focused on EU data boundary scenarios, supporting organizations with regulatory and compliance requirements. Customers should review documentation to understand qualifying scenarios and operational workflows.

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Discover Data Guardian from Sovereign Control Panel

**Background and Purpose of the Update:**  
This update introduces the ability for customers to discover Data Guardian directly from the Sovereign Control Panel, which is now in Public Preview. The primary purpose is to enhance transparency and operational oversight for customers, specifically regarding remote access by Microsoft engineers to production systems within the EU. This aligns with increasing regulatory and sovereignty requirements, particularly in the European Union, where organizations must maintain strict control and visibility over data access and operations performed by external entities.

**Specific Features and Detailed Changes:**  
- **Discovery Integration:** Data Guardian is now discoverable as a feature within the Sovereign Control Panel interface. This integration streamlines the process for customers to locate and utilize Data Guardian’s capabilities.
- **Operational Oversight:** Data Guardian provides enhanced oversight of qualifying remote access sessions. This means customers can monitor and review instances where Microsoft engineers access in-scope production systems, ensuring compliance with sovereignty and security requirements.
- **Scope:** The feature specifically targets “in-scope” production systems in the EU data centers, reflecting a focus on environments subject to EU regulatory frameworks.

**Technical Mechanisms and Implementation Methods:**  
- **Sovereign Control Panel Integration:** The Sovereign Control Panel acts as a centralized management interface for sovereignty-related controls. By integrating Data Guardian discovery, Microsoft enables direct access to oversight tools without requiring navigation through multiple portals.
- **Remote Access Monitoring:** Data Guardian tracks and logs qualifying remote access events by Microsoft engineers. The technical implementation likely involves event logging, access session recording, and reporting mechanisms, though specifics are not detailed in the update.
- **Public Preview Availability:** The feature is in Public Preview, indicating that it is available for customer use but may still be subject to changes and improvements based on feedback.

**Use Cases and Application Scenarios:**  
- **Regulated Industries:** Organizations in regulated sectors (e.g., finance, healthcare, government) operating in the EU can leverage Data Guardian to fulfill compliance requirements for monitoring third-party access to sensitive production environments.
- **Audit and Compliance:** IT security teams can use the oversight capabilities to generate audit trails and reports for internal or external compliance audits.
- **Operational Security:** Enterprises concerned with operational sovereignty can use this feature to ensure that any remote intervention by Microsoft engineers is visible and accountable.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in Public Preview, it may not yet be suitable for production-critical scenarios without additional validation.
- **Scope Limitation:** The oversight provided by Data Guardian is limited to “qualifying remote access” by Microsoft engineers and only applies to in-scope production systems within the EU. Other types of access or regions are not covered by this update.
- **Discovery Only:** The update specifically mentions the ability to “discover” Data Guardian from the Sovereign Control Panel, not necessarily full management or configuration capabilities.

**Integration with Related Azure Services:**  
- **Sovereign Control Panel:** Acts as the central hub for accessing Data Guardian and potentially other sovereignty-related features.
- **Azure Security and Compliance Solutions:** Data Guardian complements existing Azure security and compliance offerings by providing additional oversight for remote access scenarios.

**Summary Sentence:**  
Customers can now easily discover Data Guardian from the Sovereign Control Panel (in Public Preview), enabling enhanced operational oversight of qualifying remote access by Microsoft engineers to in-scope production systems in the EU.

---

### 41. Announcing: Production Touch Ledger (PTL) Assessment Report

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Announcing: Production Touch Ledger (PTL) Assessment Report](https://azure.microsoft.com/updates?id=581221)

**Update ID**: 581221
**Data source**: Azure Updates API

**Categories**: Microsoft Ignite, Announcement

**Summary**:

- What was updated  
The Production Touch Ledger (PTL) Assessment Report has been released, providing an independent evaluation of PTL’s security and integrity features.

- Key changes or new features  
Capgemini, a third-party assessor, has validated PTL’s design for its ability to ensure completeness, tamper-evidence, and non-repudiation of production-access records. This assessment confirms that PTL reliably logs and protects records of access to production environments, supporting compliance and audit requirements.

- Target audience affected  
This update is relevant for developers, IT professionals, and compliance teams who manage or monitor production environments in Azure. It is particularly important for those responsible for security, auditing, and regulatory compliance.

- Important notes if any  
The independent assessment strengthens trust in PTL’s capabilities for secure production-access logging. Organizations can use the report to support internal and external audits, and to demonstrate compliance with industry standards. For more details and to access the assessment report, visit the Azure Update link: https://azure.microsoft.com/updates?id=581221

**Details**:

**Azure Update Report: Production Touch Ledger (PTL) Assessment Report**

**Background and Purpose of the Update**  
The Production Touch Ledger (PTL) Assessment Report has been released to provide transparency and assurance regarding the security and integrity of production-access records within Azure environments. This update is driven by the need for organizations to demonstrate compliance, auditability, and trustworthiness in their operational processes, particularly concerning access to production systems. Capgemini, acting as an independent third-party assessor, has validated the PTL’s design, focusing on its ability to preserve completeness, tamper-evidence, and non-repudiation of access records.

**Specific Features and Detailed Changes**  
The PTL Assessment Report confirms that the PTL system is architected to ensure:
- **Completeness:** All production-access events are comprehensively recorded, leaving no gaps in the audit trail.
- **Tamper-evidence:** Any attempt to alter, delete, or manipulate access records is detectable, providing assurance against unauthorized modifications.
- **Non-repudiation:** Access records are cryptographically bound to the identity of the actor, preventing denial of actions performed.

This validation by Capgemini does not introduce new features to PTL itself but rather provides an authoritative assessment of its existing design and operational guarantees.

**Technical Mechanisms and Implementation Methods**  
PTL leverages advanced ledger technologies to maintain immutable records of production-access events. The technical mechanisms include:
- **Cryptographic Hashing:** Each access record is hashed and linked, forming a chain that exposes any tampering attempts.
- **Immutable Storage:** Records are stored in a write-once, append-only format, ensuring that historical data cannot be retroactively altered.
- **Identity Binding:** Access events are associated with strong identity verification, often using Azure Active Directory credentials, to ensure non-repudiation.

The assessment report details how these mechanisms collectively meet the requirements for completeness, tamper-evidence, and non-repudiation, as validated by Capgemini.

**Use Cases and Application Scenarios**  
PTL is particularly relevant in scenarios where regulatory compliance, security audits, and operational transparency are critical:
- **Regulated Industries:** Financial services, healthcare, and government organizations can use PTL to meet stringent audit and compliance requirements.
- **Security Operations:** Enterprises seeking to monitor and investigate production-access events for security incident response benefit from PTL’s immutable audit trails.
- **DevOps and SRE:** Teams managing production environments can leverage PTL to ensure accountability and traceability of access actions.

**Important Considerations and Limitations**  
While the assessment report provides assurance about PTL’s design, IT professionals should note:
- The report validates the design, not the operational deployment; organizations must ensure proper configuration and integration.
- PTL’s guarantees are contingent on adherence to recommended operational practices, such as identity management and access control.
- The assessment does not cover integration with third-party tools or custom workflows beyond the PTL’s native capabilities.

**Integration with Related Azure Services**  
PTL is designed to work seamlessly with Azure’s identity and access management solutions, including Azure Active Directory. It can be integrated with Azure Monitor, Security Center, and other logging/auditing services to provide a unified view of production-access activities. Organizations can leverage PTL alongside Azure Policy and Azure Blueprints to enforce and audit access controls in production environments.

**Summary Sentence**  
The Production Touch Ledger (PTL) Assessment Report, independently validated by Capgemini, confirms PTL’s design ensures completeness, tamper-evidence, and non-repudiation of production-access records, providing Azure users with authoritative assurance for compliance and security auditing.

---

### 42. Public Preview: Sovereign Control Panel

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Sovereign Control Panel](https://azure.microsoft.com/updates?id=581220)

**Update ID**: 581220
**Data source**: Azure Updates API

**Categories**: In preview, Features, Microsoft Ignite

**Summary**:

- What was updated  
The Sovereign Control Panel is now available in Public Preview on Azure.

- Key changes or new features  
The Sovereign Control Panel provides a dedicated Azure portal experience for organizations to assess and monitor their sovereignty posture. It enables users to:  
  - Continuously evaluate compliance with sovereignty requirements  
  - Identify and understand gaps in sovereignty controls  
  - Access evidence and documentation related to those gaps  
  - Track progress and remediation actions to improve sovereignty posture

- Target audience affected  
This update is relevant for IT professionals, compliance teams, and developers working in regulated industries or regions with strict data sovereignty requirements (e.g., government, finance, healthcare). Organizations needing to demonstrate compliance with regional or national data sovereignty standards will benefit from this tool.

- Important notes if any  
The Sovereign Control Panel is currently in Public Preview, so features and functionality may change before general availability. Users should review documentation and provide feedback during the preview period. Integration with existing compliance and monitoring workflows may require additional configuration.  
For more details, visit the official Azure update page: https://azure.microsoft.com/updates?id=581220

**Details**:

**Azure Update Report: Public Preview – Sovereign Control Panel**

**Background and Purpose of the Update**  
The release of the Sovereign Control Panel in Public Preview addresses the growing need for organizations to manage and monitor their sovereignty posture within Azure environments. Sovereignty in cloud computing refers to the ability of organizations to maintain control over their data, operations, and compliance requirements, especially in regions with strict regulatory mandates. This update is intended to provide organizations with a dedicated Azure portal experience, enabling them to assess their sovereignty status and continuously monitor compliance with relevant sovereignty requirements.

**Specific Features and Detailed Changes**  
The Sovereign Control Panel introduces a specialized interface within the Azure portal. Key features include:
- **Assessment Tools:** The panel allows organizations to evaluate their current sovereignty posture, identifying areas where their Azure deployments may not meet sovereignty requirements.
- **Continuous Monitoring:** Users can monitor their sovereignty status over time, ensuring ongoing compliance and visibility into their Azure resources.
- **Evidence-Based Gap Analysis:** The panel provides detailed evidence behind any identified gaps in sovereignty, enabling organizations to understand the root causes and take corrective actions.
- **User Experience:** The portal is designed to be intuitive, offering clear dashboards and actionable insights tailored to sovereignty concerns.

**Technical Mechanisms and Implementation Methods**  
The Sovereign Control Panel leverages Azure’s portal infrastructure to deliver a centralized experience for sovereignty management. It integrates with Azure’s resource and compliance management APIs to collect and display relevant data. The panel aggregates evidence from Azure services, presenting it in a structured format to facilitate gap analysis. Continuous monitoring is achieved through automated scans and assessments, with results updated in real time or at scheduled intervals. The technical implementation ensures that sovereignty assessments are based on actual resource configurations and compliance metadata.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in sectors such as government, healthcare, and finance can use the panel to ensure their Azure deployments meet local sovereignty requirements.
- **Global Enterprises:** Companies operating across multiple jurisdictions can monitor sovereignty posture for each region, addressing cross-border compliance challenges.
- **Audit Preparation:** IT teams can utilize the evidence and gap analysis features to prepare for regulatory audits and demonstrate compliance with sovereignty mandates.
- **Continuous Compliance:** The panel supports ongoing compliance initiatives, allowing organizations to proactively address sovereignty gaps as their Azure environments evolve.

**Important Considerations and Limitations**  
- **Preview Status:** The Sovereign Control Panel is currently in Public Preview, meaning it may not offer full functionality or production-level support. Organizations should test its features and validate results before relying on them for critical compliance decisions.
- **Scope of Evidence:** The panel provides evidence behind identified gaps, but the completeness and accuracy of this evidence depend on the underlying Azure services and configurations.
- **Integration Limitations:** Some Azure resources or third-party integrations may not be fully supported in the preview version, potentially limiting the scope of sovereignty assessments.

**Integration with Related Azure Services**  
The Sovereign Control Panel is designed to work within the Azure portal ecosystem, integrating with Azure resource management, compliance tools, and monitoring services. It complements existing Azure compliance solutions by focusing specifically on sovereignty, providing additional insights and evidence for organizations with heightened sovereignty requirements.

**Summary Sentence:**  
The Sovereign Control Panel in Public Preview offers organizations a dedicated Azure portal experience to assess, monitor, and understand their sovereignty posture, providing evidence-based gap analysis and continuous compliance insights tailored to regulatory and operational sovereignty needs.

---

### 43. Private Preview: Azure confidential VMs on 5th Gen AMD EPYC processors (DCasv7 and ECasv7 series)

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Private Preview: Azure confidential VMs on 5th Gen AMD EPYC processors (DCasv7 and ECasv7 series)](https://azure.microsoft.com/updates?id=581199)

**Update ID**: 581199
**Data source**: Azure Updates API

**Categories**: In development, Compute, Virtual Machines, Microsoft Ignite

**Summary**:

- What was updated  
Azure introduced a private preview for its next-generation confidential virtual machines (VMs), specifically the DCasv7, DCadsv7, DCalsv7, DCaldsv7, ECasv7, and ECadsv7 series. These VMs are built on 5th Gen AMD EPYC processors featuring AMD SEV-SNP technology.

- Key changes or new features  
The new confidential VM series leverages AMD SEV-SNP (Secure Encrypted Virtualization – Secure Nested Paging), providing advanced hardware-based memory encryption and isolation. This ensures that data is protected not only at rest and in transit but also during processing, isolating each VM from the hypervisor and other VMs. The update brings enhanced security capabilities for sensitive workloads, supporting compliance and privacy requirements.

- Target audience affected  
Developers and IT professionals working with highly sensitive data, regulated workloads, or those requiring confidential computing environments will benefit most. Organizations in finance, healthcare, government, and other sectors with strict data protection needs are primary targets.

- Important notes if any  
The confidential VM series is currently available in private preview. Interested customers must request access. These VMs are ideal for workloads requiring strong data confidentiality and isolation, such as secure multi-party computation, confidential databases, and privacy-preserving analytics. Review compatibility and migration considerations before adoption.

**Details**:

**Azure Update Report: Private Preview of Azure Confidential VMs on 5th Gen AMD EPYC Processors (DCasv7 and ECasv7 Series)**

**Background and Purpose of the Update**  
This Azure update introduces the private preview of next-generation confidential virtual machines (VMs) in the DCasv7, DCadsv7, DCalsv7, DCaldsv7, ECasv7, and ECadsv7 series. These VMs are built on 5th Gen AMD EPYC processors, leveraging AMD SEV-SNP (Secure Encrypted Virtualization – Secure Nested Paging) technology. The primary purpose is to enhance security by protecting data during processing, addressing the need for confidential computing in regulated industries and sensitive workloads.

**Specific Features and Detailed Changes**  
- **VM Series:** The update covers multiple VM series (DCasv7, DCadsv7, DCalsv7, DCaldsv7, ECasv7, ECadsv7), all based on the latest AMD EPYC processors.
- **Confidential Computing:** These VMs are designed to provide hardware-based isolation for workloads, ensuring that data remains protected not only at rest and in transit but also during processing.
- **AMD SEV-SNP Support:** The integration of AMD SEV-SNP enables advanced memory encryption and VM isolation, preventing unauthorized access from other VMs, the hypervisor, or even Azure operators.

**Technical Mechanisms and Implementation Methods**  
- **Hardware Root of Trust:** The 5th Gen AMD EPYC processors establish a hardware root of trust, ensuring that only authorized code executes within the VM.
- **Memory Encryption:** SEV-SNP encrypts VM memory, isolating it from the hypervisor and other VMs, and providing attestation capabilities to verify VM integrity.
- **VM Isolation:** Each VM is isolated at the hardware level, reducing the attack surface and mitigating risks from privileged system software.
- **Attestation:** SEV-SNP supports remote attestation, allowing customers to verify that their VM is running in a secure, trusted environment.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Ideal for financial services, healthcare, and government workloads requiring strict data confidentiality.
- **Sensitive Data Processing:** Suitable for applications handling personally identifiable information (PII), intellectual property, or cryptographic keys.
- **Multi-tenant Environments:** Enables secure processing in shared environments, ensuring tenant isolation.
- **Zero-Trust Architectures:** Supports organizations adopting zero-trust security models by providing strong guarantees on workload isolation.

**Important Considerations and Limitations**  
- **Private Preview:** Availability is limited to select customers during the private preview phase; production use may require waiting for general availability.
- **Compatibility:** Workloads must be compatible with confidential VM requirements and AMD SEV-SNP features.
- **Performance Impact:** Encryption and isolation features may introduce performance overhead; benchmarking is recommended.
- **Feature Scope:** The update focuses on VM isolation and memory encryption; other confidential computing features (e.g., enclave support) are not mentioned.

**Integration with Related Azure Services**  
- **Azure Confidential Computing Portfolio:** These VMs expand Azure’s confidential computing offerings, complementing existing VM series and enclave-based solutions.
- **Azure Security Services:** Can be integrated with Azure Key Vault, Azure Security Center, and other security monitoring tools for enhanced protection and compliance.
- **Azure Compute Ecosystem:** Compatible with standard Azure VM management and deployment tools, enabling seamless integration into existing workflows.

**Summary Sentence**  
Azure has announced the private preview of confidential VMs built on 5th Gen AMD EPYC processors with SEV-SNP, offering advanced hardware-based isolation and memory encryption to protect data during processing for sensitive and regulated workloads.

---

### 44. Private Preview: Project Nova

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Private Preview: Project Nova](https://azure.microsoft.com/updates?id=581193)

**Update ID**: 581193
**Data source**: Azure Updates API

**Categories**: In development, Microsoft Ignite

**Summary**:

- What was updated  
Azure announced the private preview of Project Nova, a new solution focused on enabling independent verification of claims without exposing underlying sensitive data.

- Key changes or new features  
Project Nova leverages zero-knowledge proof technology to allow organizations to validate specific assertions or compliance requirements while keeping confidential information secure. This approach supports privacy-preserving trust mechanisms, particularly relevant for regulated industries where data protection and compliance are critical. The private preview offers early access to these capabilities for select customers.

- Target audience affected  
Developers and IT professionals working in regulated sectors (such as finance, healthcare, and government) who require secure methods for verifying compliance or other claims without sharing sensitive data. Security architects and compliance teams will also benefit from these features.

- Important notes  
Project Nova is currently available in private preview, meaning access is limited and interested organizations must request participation. The use of zero-knowledge proofs marks a significant advancement in privacy and security for Azure customers, enabling new scenarios for compliance and trust without compromising data confidentiality. Early adopters can provide feedback to shape future releases.

**Details**:

**Azure Update Report: Private Preview – Project Nova**

**Background and Purpose of the Update:**  
Project Nova addresses the growing need for privacy-preserving verification in regulated industries. Organizations are often required to prove compliance, authenticity, or other claims to external parties, but sharing underlying confidential data can violate privacy or regulatory requirements. The purpose of Project Nova is to enable independent verification of specific claims while ensuring the confidentiality of sensitive information.

**Specific Features and Detailed Changes:**  
Project Nova introduces a mechanism for independent claim verification without exposing the actual data. This feature is particularly relevant for scenarios where organizations must demonstrate compliance or validity to auditors, partners, or regulators, but cannot disclose proprietary or personal information. The update is currently available as a private preview, indicating early access for select customers to test and provide feedback on its capabilities.

**Technical Mechanisms and Implementation Methods:**  
The core technical mechanism behind Project Nova is the use of zero-knowledge proofs (ZKP). Zero-knowledge proofs are cryptographic protocols that allow one party (the prover) to demonstrate to another party (the verifier) that a statement is true, without revealing any information beyond the validity of the statement itself. Project Nova leverages ZKP to enable verification workflows where sensitive data remains hidden, but the integrity and correctness of claims can be independently validated. The implementation likely involves generating cryptographic proofs based on the underlying data, which are then shared with verifiers for validation.

**Use Cases and Application Scenarios:**  
Project Nova is designed for regulated industries such as finance, healthcare, and government, where privacy and compliance are paramount. Example use cases include:
- Financial institutions proving regulatory compliance without exposing customer data.
- Healthcare providers demonstrating adherence to privacy standards without sharing patient records.
- Enterprises validating supply chain integrity or audit results while protecting trade secrets.
- Any scenario where confidential information must remain undisclosed, but third-party verification is required.

**Important Considerations and Limitations:**  
As Project Nova is in private preview, access is limited and features may evolve based on user feedback. Organizations should assess compatibility with existing workflows and compliance requirements. The performance and scalability of zero-knowledge proof generation and verification may vary depending on claim complexity and data volume. Additionally, integration with existing systems may require adaptation to support cryptographic proof workflows.

**Integration with Related Azure Services:**  
While the update does not specify direct integration points, Project Nova is positioned within the Azure ecosystem. It can potentially be combined with Azure Confidential Computing, Azure Key Vault, and other security and compliance services to enhance privacy-preserving operations. Integration with Azure Active Directory and Azure Policy may further support identity management and compliance automation.

**Summary Sentence:**  
Project Nova, now in private preview, enables independent verification of specific claims using zero-knowledge proofs, allowing organizations in regulated industries to establish trust and compliance without revealing confidential data.

---

### 45. Generally Available: Azure Policy support for Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Policy support for Azure HorizonDB](https://azure.microsoft.com/updates?id=581180)

**Update ID**: 581180
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Policy support for Azure HorizonDB is now generally available.

- Key changes or new features  
This update introduces built-in Azure Policy definitions for HorizonDB, enabling automated governance and observability across HorizonDB resources. With these policies, you can enforce and automatically deploy diagnostic settings, ensuring consistent monitoring and compliance. The policies help streamline management by applying standards for resource configuration and auditing.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB deployments, especially those responsible for governance, compliance, and monitoring.

- Important notes  
The built-in policies allow for automated enforcement of diagnostic settings, reducing manual configuration and risk of non-compliance. This feature is now generally available, meaning it is ready for production use and supported by Microsoft. For implementation details and policy templates, refer to the official Azure documentation and the update link.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Policy support for Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581180)

---

**Background and Purpose of the Update**  
The update introduces Azure Policy support for Azure HorizonDB, now available in preview. The primary purpose is to enable IT professionals to enforce governance and observability standards across HorizonDB deployments. Azure Policy is a critical service for managing compliance and operational consistency in cloud environments. By extending Azure Policy to HorizonDB, Microsoft aims to streamline the application of organizational standards, particularly for diagnostic settings, across all instances of HorizonDB.

**Specific Features and Detailed Changes**  
- **Built-in Policy for HorizonDB:** The update provides a new built-in Azure Policy specifically designed for HorizonDB resources.  
- **Automatic Deployment of Diagnostic Settings:** The policy enables automatic configuration and deployment of diagnostic settings on HorizonDB instances, ensuring that logging and monitoring are consistently applied.  
- **Preview Availability:** The feature is currently in preview, allowing early access and testing by IT professionals before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Azure Policy Engine:** Azure Policy operates by evaluating resources against defined rules and, where applicable, enforcing compliance through automatic remediation.  
- **Policy Assignment:** Administrators can assign the built-in HorizonDB policy at various scopes (subscription, resource group, or management group) to target all HorizonDB resources within those scopes.  
- **Automatic Remediation:** When HorizonDB resources are created or modified, Azure Policy checks for compliance with the diagnostic settings policy and applies the necessary configurations if they are missing.  
- **Observability Integration:** The policy leverages Azure’s diagnostic settings infrastructure to route logs and metrics from HorizonDB to Azure Monitor, Log Analytics, or other supported endpoints.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations can enforce diagnostic logging requirements for HorizonDB to meet regulatory standards (e.g., GDPR, HIPAA).  
- **Operational Consistency:** Ensures that all HorizonDB instances have uniform observability settings, simplifying troubleshooting and performance monitoring.  
- **Automated Governance:** Reduces manual configuration errors and oversight by automating the deployment of diagnostic settings across all HorizonDB resources.

**Important Considerations and Limitations**  
- **Preview Status:** As the feature is in preview, it may not be suitable for production workloads and could be subject to changes or limitations in functionality.  
- **Scope of Policy:** The built-in policy is focused on diagnostic settings; other governance aspects may require additional custom policies or manual configuration.  
- **Resource Coverage:** Only HorizonDB resources are affected; other Azure services require separate policy assignments.

**Integration with Related Azure Services**  
- **Azure Monitor and Log Analytics:** Diagnostic settings configured via policy can route HorizonDB logs and metrics to Azure Monitor and Log Analytics for centralized monitoring and analysis.  
- **Azure Resource Manager (ARM):** Policy assignments and compliance evaluations are managed through ARM, ensuring seamless integration with existing resource management workflows.  
- **Azure Security Center:** Enhanced observability supports security monitoring and threat detection for HorizonDB resources.

---

**Summary Sentence:**  
Azure Policy support for Azure HorizonDB, now in preview, enables IT professionals to automatically enforce diagnostic settings across HorizonDB deployments, promoting consistent governance and observability through built-in policies and integration with Azure monitoring services.

---

### 46. Public Preview: Azure DDoS Protection peacetime telemetry

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure DDoS Protection peacetime telemetry](https://azure.microsoft.com/updates?id=581175)

**Update ID**: 581175
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure DDoS Protection, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure DDoS Protection now offers peacetime telemetry in public preview.

- Key changes or new features  
Customers can access detailed traffic telemetry for their protected public IP addresses during normal (peacetime) operations, not just during active DDoS mitigation events. This provides visibility into incoming traffic patterns and volume, helping users understand baseline traffic and detect anomalies early. Previously, telemetry was only available during an active DDoS mitigation, limiting insight into day-to-day traffic.

- Target audience affected  
Azure DDoS Protection users, including IT professionals managing network security and developers responsible for application reliability and performance.

- Important notes if any  
Peacetime telemetry enables proactive monitoring and analysis of network traffic, supporting improved security posture and operational awareness. This feature is currently in public preview, so feedback is encouraged and functionality may evolve. Users should review documentation for integration details and consider how this telemetry can enhance their security monitoring and incident response workflows.

Link: [Azure Update](https://azure.microsoft.com/updates?id=581175)

**Details**:

**Azure Update Report: Public Preview – Azure DDoS Protection Peacetime Telemetry**

**Background and Purpose of the Update**  
Azure DDoS Protection is designed to safeguard Azure resources from Distributed Denial of Service (DDoS) attacks by monitoring and mitigating malicious traffic targeting public IP addresses. Historically, telemetry and visibility into traffic patterns were only available during an active DDoS mitigation event. This limited customers’ ability to understand baseline traffic behavior and trends during normal, non-attack periods ("peacetime"). The purpose of this update is to enhance visibility and monitoring capabilities by providing peacetime telemetry for protected public IP addresses, thereby improving situational awareness and proactive security management.

**Specific Features and Detailed Changes**  
With the introduction of peacetime telemetry in public preview, Azure DDoS Protection now enables customers to view traffic statistics for their protected public IP addresses even when no DDoS mitigation is occurring. This feature expands the scope of telemetry from solely attack periods to include regular operational periods. Customers can access data on traffic volume, patterns, and other relevant metrics, helping them to establish normal baselines and detect anomalies before they escalate into full-scale attacks.

**Technical Mechanisms and Implementation Methods**  
Peacetime telemetry is integrated into the Azure DDoS Protection service and leverages Azure’s monitoring infrastructure to collect and display traffic data. The telemetry is accessible for public IP addresses that are actively protected by Azure DDoS Protection. Data is gathered continuously and made available through Azure’s reporting interfaces, allowing for real-time or historical analysis. The implementation ensures that telemetry is only provided for peacetime (non-mitigation) periods, complementing existing attack-time telemetry.

**Use Cases and Application Scenarios**  
- **Baseline Analysis:** IT professionals can use peacetime telemetry to establish normal traffic baselines for protected public IP addresses, aiding in anomaly detection and capacity planning.
- **Proactive Security Monitoring:** Security teams can monitor for unusual spikes or patterns in traffic during peacetime, enabling early detection of potential threats or reconnaissance activities.
- **Operational Reporting:** Network administrators can generate reports on regular traffic flows, supporting compliance, audit, and performance optimization requirements.
- **Incident Response Preparation:** By understanding peacetime traffic, organizations can more effectively distinguish between legitimate increases in traffic and the onset of a DDoS attack.

**Important Considerations and Limitations**  
- Peacetime telemetry is currently in public preview, meaning it may be subject to changes and is not recommended for production-critical decision-making until general availability.
- Telemetry is only available for public IP addresses protected by Azure DDoS Protection; unprotected IPs do not receive this visibility.
- The scope of available metrics and reporting interfaces may be limited during the preview phase, and users should consult Azure documentation for supported features.

**Integration with Related Azure Services**  
Peacetime telemetry is designed to work seamlessly with Azure DDoS Protection and can be accessed alongside other Azure monitoring and reporting tools, such as Azure Monitor and Azure Security Center. This integration allows for consolidated security and operational reporting, supporting holistic visibility across Azure resources.

**Summary Sentence**  
Azure DDoS Protection peacetime telemetry, now in public preview, enables customers to monitor and analyze traffic reaching their protected public IP addresses during normal operation, enhancing visibility and proactive security management beyond active DDoS mitigation events.

---

### 47. Generally Available: Azure HorizonDB System Managed Maintenance Window

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB System Managed Maintenance Window](https://azure.microsoft.com/updates?id=581170)

**Update ID**: 581170
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now supports system-managed maintenance windows for planned service upgrades, and this feature is generally available.

- Key changes or new features  
With system-managed maintenance, Azure HorizonDB automatically handles planned upgrades on clusters. Users no longer need to manually configure or manage maintenance schedules—Azure schedules and executes the upgrades, minimizing operational overhead and ensuring clusters stay up-to-date.

- Target audience affected  
This update impacts developers and IT professionals who manage Azure HorizonDB clusters, particularly those responsible for database maintenance, reliability, and uptime.

- Important notes  
System-managed maintenance is designed to reduce manual intervention and streamline upgrade processes. However, users should review upgrade documentation and monitor cluster health during maintenance windows to ensure application compatibility and performance. This feature is enabled by default for new clusters; existing clusters may require configuration changes to adopt system-managed maintenance. For more details, refer to the official Azure documentation.

**Details**:

**Azure Update Report: Azure HorizonDB System Managed Maintenance Window (Generally Available)**

**Background and Purpose of the Update**  
Azure HorizonDB now supports system-managed maintenance for planned service upgrades. The primary goal of this update is to streamline maintenance operations by automating the upgrade process for HorizonDB clusters. Previously, customers were required to manually configure and manage maintenance schedules, which could lead to increased operational overhead and potential risks of missed upgrades. With this update, Azure aims to reduce administrative burden and ensure clusters remain up-to-date with minimal intervention.

**Specific Features and Detailed Changes**  
The key feature introduced is the system-managed maintenance window for Azure HorizonDB. This allows Azure to automatically perform planned service upgrades on HorizonDB clusters. Users no longer need to set up or manage maintenance schedules; instead, Azure orchestrates the upgrade process. The update is now generally available, meaning it is fully supported and ready for production workloads.

**Technical Mechanisms and Implementation Methods**  
System-managed maintenance leverages Azure’s orchestration capabilities to schedule and execute upgrades on HorizonDB clusters. When a planned service upgrade is due, Azure initiates the maintenance process automatically. The mechanism ensures that the cluster is upgraded in a controlled manner, minimizing downtime and maintaining service availability. The process is fully managed by Azure, and users are abstracted from the underlying scheduling and execution logic. This is achieved through Azure’s internal maintenance orchestration, which coordinates cluster upgrades based on service requirements and best practices.

**Use Cases and Application Scenarios**  
This feature is particularly beneficial for organizations running production workloads on Azure HorizonDB clusters who require high availability and minimal operational overhead. Typical scenarios include:  
- Enterprises with large-scale HorizonDB deployments that need consistent and reliable upgrade processes.  
- IT teams seeking to reduce manual maintenance tasks and focus on core business operations.  
- Environments where compliance and security require timely application of service upgrades without manual intervention.

**Important Considerations and Limitations**  
While system-managed maintenance simplifies upgrade management, IT professionals should be aware that control over scheduling is relinquished to Azure. This means that custom maintenance windows or blackout periods may not be supported unless specifically provided by Azure HorizonDB’s configuration options. It is important to review documentation and understand the upgrade cadence to ensure alignment with business requirements. Additionally, as the update is generally available, it is recommended to monitor cluster health post-upgrade and validate application compatibility.

**Integration with Related Azure Services**  
System-managed maintenance is integrated with Azure’s overall platform management and orchestration services. It works seamlessly with Azure’s monitoring and alerting tools, allowing IT teams to track maintenance events and cluster status. The feature aligns with Azure’s managed service philosophy, providing a consistent experience across other managed database offerings. Integration with Azure Resource Manager and Azure Security Center ensures that maintenance events are logged and can be audited as part of broader governance and compliance strategies.

**Summary Sentence**  
Azure HorizonDB now offers generally available system-managed maintenance windows, enabling automatic, Azure-orchestrated planned service upgrades for clusters without requiring user-configured maintenance schedules, thereby reducing operational overhead and ensuring consistent service reliability.

---

### 48. Generally Available: Azure Linux 4.0

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Linux 4.0](https://azure.microsoft.com/updates?id=581165)

**Update ID**: 581165
**Data source**: Azure Updates API

**Categories**: Launched, Azure Linux, Microsoft Ignite

**Summary**:

- What was updated  
Azure Linux 4.0 is now generally available for Azure Virtual Machines and VM Scale Sets. This marks the release of Microsoft’s first-party, open-source Linux distribution, designed specifically for Azure environments.

- Key changes or new features  
Azure Linux 4.0 delivers a modern, optimized Linux experience tailored for cloud workloads. Key features include improved performance, enhanced security, and seamless integration with Azure services. It supports automated patching, streamlined image management, and is engineered for reliability and scalability in cloud-native scenarios. Developers benefit from compatibility with popular Linux tools and frameworks, while IT professionals gain access to simplified lifecycle management and support for Azure-native monitoring and management.

- Target audience affected  
This update is relevant for developers deploying Linux-based applications on Azure, IT professionals managing Azure VM infrastructure, and organizations seeking a secure, supported Linux OS optimized for Azure.

- Important notes if any  
Azure Linux 4.0 is open source and fully supported by Microsoft. It is recommended for new deployments requiring a secure, reliable, and Azure-integrated Linux platform. Existing workloads can migrate to Azure Linux 4.0 to leverage its enhanced features and support. For more details, visit the official Azure Update page.

**Details**:

**Azure Update Report: Generally Available – Azure Linux 4.0**

**Background and Purpose of the Update**  
Azure Linux 4.0 is now generally available, marking Microsoft's introduction of a first-party, open-source Linux distribution designed specifically for Azure environments. Released as part of Microsoft Ignite, this update aims to provide a modern, optimized Linux platform for Azure Virtual Machines (VMs) and VM Scale Sets. The purpose is to offer customers a Linux OS that is tightly integrated with Azure infrastructure, enabling enhanced performance, security, and support for cloud-native workloads.

**Specific Features and Detailed Changes**  
Azure Linux 4.0 delivers a contemporary Linux experience tailored for Azure. Key features include:
- **Optimized Kernel and User Space:** The distribution is engineered for Azure, ensuring compatibility and performance for VM workloads.
- **Open-Source Foundation:** Azure Linux is fully open-source, allowing transparency and community-driven improvements.
- **Support for VM Scale Sets:** The OS is validated for use in both individual VMs and scalable VM sets, supporting dynamic scaling and orchestration.
- **Modern Security and Management:** Azure Linux incorporates up-to-date security features and management tools, aligning with Azure’s compliance and operational standards.

**Technical Mechanisms and Implementation Methods**  
Azure Linux 4.0 is deployed as an image for Azure VMs and VM Scale Sets. It leverages Azure’s provisioning and management framework, allowing IT professionals to select Azure Linux as the base OS during VM creation. The distribution is maintained by Microsoft, ensuring regular updates, patches, and integration with Azure’s lifecycle management tools. Azure Linux images are available through the Azure Marketplace, and can be managed using Azure CLI, ARM templates, and Azure Portal.

**Use Cases and Application Scenarios**  
Azure Linux 4.0 is ideal for:
- **Cloud-Native Applications:** Developers can deploy containerized workloads and microservices on a Linux OS optimized for Azure.
- **Enterprise VM Deployments:** Organizations seeking a supported, secure Linux platform for their Azure VMs and VM Scale Sets.
- **DevOps and Automation:** Teams can leverage Azure Linux for CI/CD pipelines, infrastructure-as-code, and automated scaling scenarios.
- **Hybrid and Multi-Cloud Strategies:** Azure Linux provides a consistent Linux environment for workloads migrating to Azure or operating in hybrid architectures.

**Important Considerations and Limitations**  
- **Azure-Only Distribution:** Azure Linux 4.0 is purpose-built for Azure and may not be suitable for on-premises or other cloud environments.
- **Support and Maintenance:** As a Microsoft-maintained distribution, updates and support are provided through Azure channels.
- **Compatibility:** Users should verify application compatibility with Azure Linux, especially for workloads requiring specific kernel modules or libraries.

**Integration with Related Azure Services**  
Azure Linux 4.0 integrates seamlessly with:
- **Azure Compute Services:** Supports VM and VM Scale Set deployments.
- **Azure Security and Management Tools:** Works with Azure Security Center, Azure Monitor, and Azure Update Management.
- **Azure Marketplace:** Available as a selectable OS image for new deployments.
- **Azure Automation and DevOps:** Compatible with Azure DevOps, ARM templates, and scripting tools for automated provisioning and management.

**Summary Sentence:**  
Azure Linux 4.0 is now generally available, offering a modern, open-source Linux distribution purpose-built for Azure Virtual Machines and VM Scale Sets, with optimized integration, security, and support for cloud-native workloads.

---

### 49. Generally Available: Azure Ebsv6 and Ebdsv6

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Ebsv6 and Ebdsv6](https://azure.microsoft.com/updates?id=581160)

**Update ID**: 581160
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Microsoft Ignite

**Summary**:

- What was updated  
Azure Ebsv6 and Ebdsv6 virtual machines (VMs) are now generally available.

- Key changes or new features  
These VMs are powered by 5th Gen Intel® Xeon® processors and utilize Azure Boost technology, significantly improving storage performance for I/O-intensive workloads. They are specifically designed to support demanding scenarios such as relational databases, in-memory databases, and other high-throughput applications. The Ebsv6 and Ebdsv6 VMs offer enhanced throughput and lower latency for disk operations, making them ideal for workloads requiring fast and reliable storage access.

- Target audience affected  
Developers and IT professionals running or planning to deploy I/O-intensive applications, including database administrators, architects, and infrastructure teams managing relational or in-memory databases on Azure.

- Important notes if any  
The general availability of these VM series means they are now production-ready and supported across regions. Azure Boost integration provides additional performance benefits, but users should review regional availability and pricing. Migration from older VM series may require application and storage configuration adjustments to fully leverage the new capabilities. For more details, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=581160

**Details**:

**Azure Update Report: General Availability of Azure Ebsv6 and Ebdsv6 VMs**

**Background and Purpose of the Update**  
The general availability of Azure Ebsv6 and Ebdsv6 virtual machines (VMs) marks a significant enhancement in Azure’s VM portfolio, specifically targeting workloads that require high storage performance. This update is driven by the need to support I/O-intensive applications, such as relational databases and in-memory workloads, with improved efficiency and reliability. The introduction of these VM series aims to address performance bottlenecks in storage throughput and latency, ensuring that enterprise workloads can scale and operate seamlessly.

**Specific Features and Detailed Changes**  
Ebsv6 and Ebdsv6 VMs are powered by 5th Generation Intel® Xeon® processors, offering advanced compute capabilities. The integration of Azure Boost technology further elevates storage performance, enabling higher IOPS and throughput for disk operations. These VMs are specifically engineered to deliver enhanced storage performance, making them ideal for scenarios where disk I/O is a critical factor. The update introduces new VM sizes and configurations optimized for storage-heavy workloads, providing flexibility for customers to choose the best fit for their application requirements.

**Technical Mechanisms and Implementation Methods**  
The technical foundation of Ebsv6 and Ebdsv6 VMs lies in the combination of modern Intel Xeon processors and Azure Boost. Azure Boost is a platform innovation that offloads storage and networking processes from the host CPU, thereby reducing contention and improving overall VM performance. This mechanism allows for direct acceleration of disk I/O, resulting in lower latency and higher throughput. The VMs leverage premium SSDs and advanced disk caching techniques to maximize performance for demanding workloads.

**Use Cases and Application Scenarios**  
These VMs are designed for applications where storage performance is paramount. Typical use cases include:
- Relational database management systems (e.g., SQL Server, Oracle, MySQL) that require fast disk access for transaction processing.
- In-memory databases and caching solutions that benefit from high throughput and low latency.
- Data warehousing and analytics workloads that perform frequent read/write operations.
- Enterprise applications with heavy I/O demands, such as ERP and CRM systems.

**Important Considerations and Limitations**  
When deploying Ebsv6 and Ebdsv6 VMs, IT professionals should consider the specific storage requirements of their workloads to select the appropriate VM size and disk configuration. While these VMs offer enhanced storage performance, optimal results depend on proper disk selection and configuration. It is important to review Azure’s documentation for supported disk types, maximum IOPS, and throughput limits for each VM size. Additionally, compatibility with existing application architectures and Azure services should be evaluated to ensure seamless integration.

**Integration with Related Azure Services**  
Ebsv6 and Ebdsv6 VMs are fully integrated with Azure’s ecosystem, supporting managed disks, Azure Backup, Azure Site Recovery, and other storage-related services. They can be deployed in conjunction with Azure SQL Database, Azure Database for PostgreSQL, and other PaaS offerings that benefit from high-performance storage. The VMs also support integration with Azure networking services, enabling secure and scalable deployment architectures.

**Summary Sentence**  
Azure Ebsv6 and Ebdsv6 VMs are now generally available, offering enhanced storage performance for I/O-intensive workloads through 5th Gen Intel® Xeon® processors and Azure Boost, and are optimized for relational databases and in-memory applications.

---

### 50. Public Preview: Azure Compute Spot plus

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Compute Spot plus](https://azure.microsoft.com/updates?id=581145)

**Update ID**: 581145
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines, Microsoft Ignite

**Summary**:

- What was updated  
Azure Compute Spot plus is now available in public preview, introducing an enhanced tier for Azure Spot Virtual Machines.

- Key changes or new features  
Spot plus offers improved runtime consistency and provides earlier eviction signals compared to standard Spot VMs. This allows interruption-tolerant workloads to better anticipate and handle VM evictions, reducing disruption and improving workload reliability. Spot plus is designed for workloads that require more predictable runtime and eviction notifications, while standard Spot remains suitable for highly resilient workloads.

- Target audience affected  
Developers and IT professionals managing cost-sensitive, interruption-tolerant workloads on Azure, such as batch processing, CI/CD pipelines, and large-scale compute jobs, will benefit from Spot plus. Those seeking more predictable performance and eviction handling on Spot VMs should consider this new tier.

- Important notes if any  
Spot plus is currently in public preview and may not be available in all regions. Pricing and availability details should be reviewed before adoption. Developers should update their workload eviction handling logic to leverage the earlier eviction signals provided by Spot plus for optimal performance and reliability.

Data source: Using API data  
[Azure Update Link](https://azure.microsoft.com/updates?id=581145)

**Details**:

**Azure Update Report: Public Preview – Azure Compute Spot plus**

**Background and Purpose of the Update:**  
Azure Compute Spot plus is introduced as an enhanced tier of Azure Spot Virtual Machines (VMs), now available in public preview. The purpose of this update is to address the need for greater runtime consistency and improved eviction signaling in interruption-tolerant workloads. While standard Azure Spot VMs are designed for highly resilient workloads that can tolerate unexpected interruptions, Spot plus aims to provide more predictable behavior and advanced notification mechanisms, thereby expanding the suitability of spot pricing to a broader range of workload types.

**Specific Features and Detailed Changes:**  
Azure Compute Spot plus offers two primary enhancements over standard Spot VMs:
1. **Greater Runtime Consistency:** Spot plus VMs are engineered to deliver more stable and predictable runtime durations, reducing the frequency and randomness of evictions compared to standard Spot VMs.
2. **Earlier Eviction Signals:** This tier provides earlier notification signals before VM eviction, allowing workloads to gracefully handle interruptions, such as saving state or completing critical operations.

These features are specifically targeted at workloads that require some level of interruption tolerance but benefit from improved predictability and the ability to react to eviction events in advance.

**Technical Mechanisms and Implementation Methods:**  
The technical implementation of Spot plus centers on improved eviction signaling and runtime management. While standard Spot VMs can be evicted at any time based on Azure capacity needs, Spot plus introduces mechanisms to notify users earlier when an eviction is imminent. This enables applications to subscribe to eviction signals and implement custom logic for graceful shutdown or migration. The runtime consistency is achieved through enhanced scheduling and allocation algorithms, which prioritize Spot plus VMs for longer uninterrupted periods compared to standard Spot VMs.

**Use Cases and Application Scenarios:**  
Azure Compute Spot plus is ideal for workloads that are interruption-tolerant but require more predictable runtime and the ability to respond to eviction events. Typical use cases include:
- Batch processing jobs that need to save progress before interruption.
- Data analytics workloads where partial results can be checkpointed.
- Machine learning training tasks that benefit from early eviction signals to save model state.
- Distributed computing scenarios where nodes can gracefully exit and rejoin without data loss.

**Important Considerations and Limitations:**  
- Spot plus VMs remain subject to eviction when Azure needs capacity, so workloads must still be designed to tolerate interruptions.
- The earlier eviction signals provided by Spot plus do not guarantee uninterrupted operation; they only offer improved notification and runtime consistency.
- As this feature is in public preview, it may not be available in all regions or VM sizes, and production workloads should be carefully evaluated for suitability.

**Integration with Related Azure Services:**  
Spot plus VMs integrate seamlessly with Azure Compute services, including Azure Virtual Machine Scale Sets, Azure Batch, and orchestration tools that support spot pricing. The enhanced eviction signaling can be leveraged by automation scripts and workload managers to optimize resource usage and minimize disruption. Spot plus can also be used alongside Azure Reserved and On-Demand VMs to balance cost and reliability in hybrid deployment scenarios.

**Summary Sentence:**  
Azure Compute Spot plus, now in public preview, introduces enhanced runtime consistency and earlier eviction signals for interruption-tolerant workloads, offering IT professionals improved predictability and control compared to standard Azure Spot Virtual Machines.

---

### 51. Generally Available: Rename Server in Azure Database for MySQL

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Rename Server in Azure Database for MySQL](https://azure.microsoft.com/updates?id=581140)

**Update ID**: 581140
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure Database for MySQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for MySQL now supports server renaming, which is generally available.

- Key changes or new features  
You can update the name of an existing MySQL server instance directly, without needing to recreate the server, migrate data, or cause application downtime. This feature enables easier adoption of naming conventions and improves management flexibility.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL instances, especially those responsible for database administration, naming standards, and resource organization.

- Important notes  
Renaming a server is a non-disruptive operation—applications and data remain unaffected during the process. This update simplifies resource management and reduces operational overhead when updating server names for compliance or organizational needs.

For more details, visit: https://azure.microsoft.com/updates?id=581140

**Details**:

**Azure Update Report: Generally Available – Rename Server in Azure Database for MySQL**

**Background and Purpose of the Update**  
The general availability of the server renaming feature for Azure Database for MySQL addresses a common operational need for IT professionals and database administrators. Previously, renaming a server instance required recreating the server, migrating data, and potentially causing disruption to applications and services. This update is designed to streamline server management, reduce downtime, and simplify administrative tasks by allowing server renaming without the need for complex migration or recreation processes.

**Specific Features and Detailed Changes**  
The new feature enables users to update the name of an existing Azure Database for MySQL server instance directly. This operation can be performed without impacting the server’s configuration, data, or running applications. The process is seamless and does not require the server to be recreated or data to be migrated. All associated resources and settings remain intact, ensuring continuity and minimizing operational overhead.

**Technical Mechanisms and Implementation Methods**  
Server renaming is implemented as a native operation within the Azure Database for MySQL management interface. Administrators can initiate the rename process through the Azure Portal, Azure CLI, or REST API. The underlying mechanism ensures that the server’s identity is updated across Azure’s internal resource management systems, while preserving all existing connections, configurations, and data integrity. The operation is designed to be non-disruptive, meaning that applications and services connected to the server do not experience downtime or require reconfiguration, unless they reference the server name directly in connection strings.

**Use Cases and Application Scenarios**  
This feature is particularly useful in scenarios such as organizational restructuring, environment standardization, or compliance-driven naming conventions. For example, IT teams can rename servers to align with new project identifiers, departmental codes, or updated naming policies without interrupting service or risking data loss. It also facilitates smoother transitions during mergers, acquisitions, or cloud migration projects where server naming consistency is required.

**Important Considerations and Limitations**  
While the server renaming feature is designed to be non-disruptive, it is important to review application configurations and connection strings. If applications reference the server name directly, these references may need to be updated to reflect the new name. Additionally, any automation scripts, monitoring tools, or third-party integrations that depend on the server name should be reviewed and updated accordingly. The update announcement does not specify any limitations regarding the frequency or conditions under which renaming can occur, so users should consult Azure documentation for any operational constraints.

**Integration with Related Azure Services**  
The server renaming feature integrates seamlessly with Azure’s resource management and monitoring services. All associated resources, such as virtual networks, firewalls, and backup configurations, remain linked to the renamed server instance. This ensures that the server continues to operate within the context of existing Azure infrastructure and services without requiring additional configuration or migration steps.

**Summary Sentence**  
Azure Database for MySQL now supports server renaming as a generally available feature, enabling IT professionals to update server names without recreating instances, migrating data, or disrupting applications, thereby simplifying server management and enhancing operational flexibility.

---

### 52. Public Preview: Windows Server 2028

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Windows Server 2028](https://azure.microsoft.com/updates?id=581135)

**Update ID**: 581135
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Windows Server 2028 is now available in public preview as the next Long-Term Servicing Channel (LTSC) release.

- Key changes or new features  
The update introduces enhanced security features, improved virtualization capabilities, and expanded hybrid cloud management tools. It also integrates hybrid intelligence investments to support mission-critical workloads. Developers and IT professionals can expect improvements in container support, automation, and management experiences, as well as better integration with Azure services for hybrid and multi-cloud scenarios.

- Target audience affected  
This update is relevant for IT professionals managing Windows Server environments, developers building applications on Windows Server, and organizations leveraging hybrid or multi-cloud infrastructure.

- Important notes if any  
The public preview allows early testing and feedback before general availability. Users should review compatibility and migration considerations, as this LTSC release will provide long-term support and stability for enterprise workloads. For more details and access, refer to the official Azure update page: https://azure.microsoft.com/updates?id=581135

**Details**:

**Azure Update Report: Public Preview – Windows Server 2028**

**Background and Purpose of the Update**  
Windows Server 2028 represents the next Long-Term Servicing Channel (LTSC) release, now available in public preview. The purpose of this update is to advance the Windows Server platform by integrating enhanced security, improved virtualization, robust hybrid cloud management, and hybrid intelligence capabilities. This release is designed to support mission-critical workloads, ensuring reliability and scalability for enterprise environments.

**Specific Features and Detailed Changes**  
Windows Server 2028 introduces several key investments:
- **Security Enhancements:** The update consolidates new security features to protect workloads and data, focusing on safeguarding mission-critical operations.
- **Virtualization Improvements:** Enhanced virtualization capabilities are included, enabling more efficient management of virtual machines and resources.
- **Hybrid Cloud Management:** The platform offers improved tools and mechanisms for managing hybrid environments, facilitating seamless integration between on-premises and cloud resources.
- **Hybrid Intelligence:** Investments in hybrid intelligence allow for smarter management and automation, leveraging both local and cloud-based insights.

**Technical Mechanisms and Implementation Methods**  
The public preview enables IT professionals to deploy Windows Server 2028 in test and evaluation environments. The LTSC model ensures stability and long-term support, making it suitable for workloads requiring predictable servicing and minimal feature changes. Security mechanisms are integrated at the OS level, virtualization is managed through updated hypervisor technologies, and hybrid management is achieved via built-in connectors and management tools that interface with Azure services.

**Use Cases and Application Scenarios**  
Windows Server 2028 is tailored for:
- **Mission-Critical Workloads:** Enterprises running applications that require high availability and robust security.
- **Hybrid Cloud Deployments:** Organizations leveraging both on-premises infrastructure and Azure cloud resources.
- **Virtualization Hosts:** Data centers and IT teams managing large-scale virtual machine deployments.
- **Automated Management:** Scenarios where hybrid intelligence can optimize operations and reduce manual intervention.

**Important Considerations and Limitations**  
As a public preview, Windows Server 2028 should not be used in production environments. IT professionals must evaluate compatibility with existing workloads and infrastructure. The LTSC release focuses on stability and long-term support, so feature updates are less frequent compared to Semi-Annual Channel releases. Preview features may change or be removed before general availability.

**Integration with Related Azure Services**  
Windows Server 2028 is designed for seamless integration with Azure:
- **Hybrid Management Tools:** Native connectors and management interfaces allow for unified control across on-premises and Azure environments.
- **Security Integration:** Enhanced security features can be extended to Azure workloads, leveraging Azure Security Center and related services.
- **Virtualization and Automation:** Azure Arc and other hybrid management solutions can be used to orchestrate and automate workloads across both platforms.

**Summary Sentence**  
Windows Server 2028 public preview delivers advanced security, virtualization, hybrid cloud management, and hybrid intelligence capabilities, providing IT professionals with a robust platform for mission-critical workloads and seamless Azure integration.

---

### 53. Public Preview: Native AWS and Google Cloud support in Azure SRE Agent

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Native AWS and Google Cloud support in Azure SRE Agent](https://azure.microsoft.com/updates?id=580975)

**Update ID**: 580975
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

**What was updated**  
Azure SRE Agent now offers native support for AWS and Google Cloud via built-in connectors, available in public preview.

**Key changes or new features**  
- Native integration: The SRE Agent can directly connect to AWS and Google Cloud environments, eliminating the need for custom connectors or manual setup.
- Unified operational evidence: Users can aggregate operational data across Azure, AWS, and Google Cloud, enabling comprehensive investigation of applications and dependencies spanning multiple cloud platforms.
- Simplified troubleshooting: The enhanced agent streamlines cross-cloud incident response and root cause analysis by providing a single view of operational evidence.

**Target audience affected**  
- Developers and IT professionals managing multi-cloud architectures.
- Site Reliability Engineers (SREs) responsible for monitoring and troubleshooting distributed applications across Azure, AWS, and Google Cloud.

**Important notes**  
- The feature is currently in public preview; production use should be approached with caution.
- Built-in connectors reduce integration complexity and accelerate onboarding for multi-cloud environments.
- Feedback from preview users will help shape future enhancements and GA release.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=580975).

**Details**:

**Azure Update Report: Native AWS and Google Cloud Support in Azure SRE Agent (Public Preview)**  
[Source Link](https://azure.microsoft.com/updates?id=580975)

---

**Background and Purpose of the Update**  
The Azure SRE (Site Reliability Engineering) Agent is designed to facilitate operational visibility and incident investigation across cloud environments. Traditionally, its capabilities have focused on Azure resources. With the increasing adoption of multi-cloud strategies, organizations require unified operational evidence and monitoring across diverse platforms. This update introduces native support for AWS and Google Cloud, addressing the need for cross-cloud observability and troubleshooting.

---

**Specific Features and Detailed Changes**  
- **Native Multi-Cloud Support:** The Azure SRE Agent now includes built-in connectors for AWS and Google Cloud, available in public preview.  
- **Unified Operational Evidence:** Users can aggregate operational data from Azure, AWS, and Google Cloud environments, enabling investigation of applications and dependencies across all connected clouds.  
- **Connector Integration:** The update provides out-of-the-box connectors, eliminating the need for custom integration or third-party tooling to bring AWS and Google Cloud data into Azure SRE workflows.

---

**Technical Mechanisms and Implementation Methods**  
- **Built-In Connectors:** The agent leverages native connectors to establish secure connections with AWS and Google Cloud environments.  
- **Data Aggregation:** Operational evidence (logs, metrics, dependencies) from AWS and Google Cloud is ingested and correlated with Azure data, providing a consolidated view for SRE teams.  
- **Agent Configuration:** IT professionals configure the Azure SRE Agent to connect to their AWS and Google Cloud accounts, typically using credentials or service principals, as supported by the connectors.  
- **Public Preview Status:** The connectors are currently in public preview, meaning features and APIs may be subject to change and are intended for evaluation and feedback.

---

**Use Cases and Application Scenarios**  
- **Multi-Cloud Incident Investigation:** SRE teams can trace incidents across Azure, AWS, and Google Cloud, identifying root causes that span multiple platforms.  
- **Dependency Mapping:** Organizations can visualize and analyze application dependencies that are distributed across different cloud providers.  
- **Unified Monitoring:** IT professionals can monitor operational health and performance metrics from all major cloud environments in a single interface.

---

**Important Considerations and Limitations**  
- **Preview Limitations:** As this feature is in public preview, it may lack full production support, and certain functionalities may be limited or subject to change.  
- **Security and Compliance:** Proper configuration of credentials and permissions is required to ensure secure data access across AWS and Google Cloud.  
- **Connector Scope:** The update focuses on AWS and Google Cloud; other cloud providers are not supported natively at this time.  
- **Integration Complexity:** While connectors are built-in, organizations must ensure proper network connectivity and account configuration for seamless integration.

---

**Integration with Related Azure Services**  
- **Azure SRE Workflows:** The new connectors enhance Azure SRE workflows by enabling cross-cloud evidence gathering and analysis.  
- **Azure Monitoring and Diagnostics:** Aggregated data from AWS and Google Cloud can be utilized alongside Azure monitoring tools for comprehensive diagnostics.  
- **Incident Management:** The update supports incident response processes by providing a unified view of operational evidence across multiple clouds.

---

**Summary Sentence**  
Azure SRE Agent now offers native, built-in connectors for AWS and Google Cloud in public preview, enabling IT professionals to aggregate and investigate operational evidence across Azure and connected multi-cloud environments for improved incident analysis and dependency mapping.

---

### 54. Public Preview: Pod snapshot cluster extension

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Pod snapshot cluster extension](https://azure.microsoft.com/updates?id=580921)

**Update ID**: 580921
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite

**Summary**:

- What was updated  
Azure has introduced the Pod Snapshot Cluster Extension in public preview, enabling snapshotting of pod-level state within Kubernetes clusters.

- Key changes or new features  
This extension allows developers and IT professionals to capture and restore the in-memory state of sandboxed workloads running in pods. It addresses the challenge of losing runtime context (such as AI model states, JVM warmup, or cache data) during pod restarts. With pod snapshots, workloads can resume faster without repeating costly initialization or reloading processes. The extension integrates with Azure Kubernetes Service (AKS) and supports automated snapshot management.

- Target audience affected  
This update is relevant for developers and IT professionals managing AI workloads, JVM-based applications, or any sandboxed applications on AKS that require fast recovery and state preservation across pod restarts.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production environments. Users should test thoroughly and monitor for updates as the extension matures. Documentation and API support are available for integration and automation.

For more details, visit: https://azure.microsoft.com/updates?id=580921

**Details**:

**Azure Update Report: Public Preview – Pod Snapshot Cluster Extension**

**Background and Purpose of the Update**  
The Pod Snapshot Cluster Extension addresses a common challenge in managing sandboxed workloads on Azure Kubernetes Service (AKS) and similar environments. When such workloads are restarted, they lose their in-memory state, requiring costly reinitialization processes. This is particularly impactful in AI environments, where models must be reloaded and runtime contexts rebuilt, and in other applications such as those running Java Virtual Machines (JVM), which must repeat warmup cycles or repopulate caches. The update aims to reduce downtime and resource consumption associated with these repetitive initialization tasks.

**Specific Features and Detailed Changes**  
The Pod Snapshot Cluster Extension introduces the capability to capture and restore the in-memory state of running pods. This allows workloads to resume from a previously saved state rather than starting from scratch. The extension operates at the cluster level, enabling administrators to manage snapshots across multiple pods and workloads. Key features include:
- Snapshot creation: Administrators can trigger snapshots of pod memory and runtime context.
- Snapshot restoration: Pods can be restarted from a saved snapshot, bypassing the need for full reinitialization.
- Cluster-wide management: The extension integrates with cluster management tools to provide centralized control over snapshot operations.

**Technical Mechanisms and Implementation Methods**  
The extension leverages Azure’s cluster extension framework to integrate with AKS and other supported Kubernetes environments. It interacts with the container runtime to capture the in-memory state and relevant runtime context of sandboxed pods. Upon restoration, the extension injects the saved state back into the pod, allowing it to resume execution as if it had not been restarted. The implementation ensures consistency and integrity of the restored state, minimizing the risk of errors or data corruption.

**Use Cases and Application Scenarios**  
- AI/ML workloads: Rapidly reload models and runtime context after pod restarts, reducing initialization time and improving availability.
- JVM-based applications: Preserve warmed-up JVM state, including loaded classes and populated caches, to avoid performance penalties from cold starts.
- High-performance computing (HPC): Maintain in-memory computation state across pod restarts for faster recovery and reduced downtime.
- Stateful microservices: Enable faster failover and recovery by restoring service state without full reinitialization.

**Important Considerations and Limitations**  
- The extension is currently in Public Preview, and may not be suitable for production workloads until general availability.
- Only sandboxed workloads and supported runtimes can leverage snapshot and restoration capabilities; compatibility should be verified for each application.
- Snapshots capture in-memory state, but may not include persistent storage or external dependencies; comprehensive recovery strategies should be considered.
- Performance overhead associated with snapshot creation and restoration should be evaluated in the context of workload requirements.

**Integration with Related Azure Services**  
The Pod Snapshot Cluster Extension integrates with Azure Kubernetes Service (AKS) and Azure’s cluster extension management tools. It can be used alongside Azure Monitor for tracking snapshot operations and Azure Backup for broader data protection strategies. The extension complements existing state management solutions, providing a new mechanism for rapid recovery and reduced initialization times.

**Summary Sentence**  
The Pod Snapshot Cluster Extension in Public Preview enables administrators to capture and restore the in-memory state of sandboxed workloads, significantly reducing downtime and initialization costs for AI, JVM, and other high-performance applications on Azure Kubernetes clusters.

---

### 55. Public Preview: Azure DDoS Protection support for NAT Gateway v2 IP

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure DDoS Protection support for NAT Gateway v2 IP](https://azure.microsoft.com/updates?id=580862)

**Update ID**: 580862
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure DDoS Protection, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DDoS Protection now supports public IP addresses associated with Azure NAT Gateway StandardV2, available in public preview.

- Key changes or new features  
Developers and IT professionals can now apply Azure DDoS Protection to both IPv4 and IPv6 public IPs used by NAT Gateway StandardV2 for outbound internet traffic. This extends DDoS mitigation to outbound connections, protecting against network-layer DDoS attacks. The same DDoS Network Protection capabilities previously available for inbound traffic are now applicable to outbound NAT Gateway traffic.

- Target audience affected  
This update is relevant for organizations using Azure NAT Gateway StandardV2 for outbound internet connectivity, especially those requiring enhanced security for public-facing workloads. Developers managing cloud applications and IT professionals responsible for network security and infrastructure will benefit from this expanded protection.

- Important notes if any  
The feature is currently in public preview and supports both IPv4 and IPv6 addresses. Users should review the preview documentation and monitor for any limitations or changes before deploying in production environments. This update helps address outbound DDoS risks, complementing existing inbound protection strategies.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure DDoS Protection support for NAT Gateway v2 IP  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=580862)

---

**Background and Purpose of the Update**  
Azure DDoS Protection is designed to safeguard Azure resources from Distributed Denial of Service (DDoS) attacks at the network layer. Traditionally, DDoS Protection has focused on public IPs directly associated with Azure resources. With the increasing adoption of Azure NAT Gateway StandardV2 for outbound internet connectivity, there was a need to extend DDoS Protection to cover the public IPs managed by NAT Gateway. This update addresses that gap, enabling organizations to secure outbound traffic endpoints against DDoS threats.

---

**Specific Features and Detailed Changes**  
- **Coverage Extension:** Azure DDoS Protection now supports public IPs behind Azure NAT Gateway StandardV2, including both IPv4 and IPv6 addresses.
- **Protection Scope:** The update enables DDoS Protection for outbound internet traffic routed through NAT Gateway, using the same DDoS Network Protection mechanisms previously available for other public IPs.
- **Public Preview:** The feature is currently in public preview, allowing customers to evaluate and provide feedback before general availability.

---

**Technical Mechanisms and Implementation Methods**  
- **Integration with NAT Gateway StandardV2:** When NAT Gateway StandardV2 is configured with public IPs, these IPs become eligible for DDoS Protection. The protection is applied at the network layer, mitigating volumetric, protocol, and resource exhaustion attacks targeting the NAT Gateway’s public endpoints.
- **IPv4 and IPv6 Support:** Both address families are covered, ensuring comprehensive protection for modern application architectures.
- **Activation:** DDoS Protection is enabled using the same configuration and management interfaces as for other Azure public IPs, requiring no changes to existing NAT Gateway deployments except for associating the DDoS Protection plan.

---

**Use Cases and Application Scenarios**  
- **Securing Outbound Traffic:** Organizations using NAT Gateway StandardV2 for outbound internet access can now protect their public IPs from DDoS attacks, ensuring uninterrupted connectivity and service reliability.
- **Hybrid and Multi-cloud Architectures:** Enterprises leveraging Azure NAT Gateway for outbound traffic in hybrid or multi-cloud scenarios benefit from enhanced security for their internet-facing endpoints.
- **IPv6 Adoption:** Applications utilizing IPv6 for outbound traffic can now receive DDoS protection, supporting modern network requirements.

---

**Important Considerations and Limitations**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads requiring guaranteed support and SLAs.
- **Scope of Protection:** The update specifically covers public IPs associated with NAT Gateway StandardV2; other NAT Gateway versions or private IPs are not included.
- **Configuration Requirements:** DDoS Protection must be explicitly associated with the NAT Gateway’s public IPs; existing DDoS Protection plans and policies apply.

---

**Integration with Related Azure Services**  
- **Azure DDoS Protection:** The update leverages Azure’s existing DDoS Protection infrastructure, providing seamless integration with monitoring, alerting, and mitigation workflows.
- **Azure NAT Gateway StandardV2:** The feature is tightly coupled with NAT Gateway StandardV2, requiring customers to use this version for DDoS coverage.
- **Azure Networking:** Works alongside Azure Firewall, Network Security Groups, and other network security services to deliver layered protection.

---

**Summary Sentence:**  
Azure DDoS Protection now supports public IPs behind Azure NAT Gateway StandardV2 in public preview, enabling organizations to secure outbound IPv4 and IPv6 traffic endpoints against network-layer DDoS attacks using existing DDoS Network Protection mechanisms.

---

### 56. Generally Available: Azure DDoS Protection custom policy 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure DDoS Protection custom policy ](https://azure.microsoft.com/updates?id=580852)

**Update ID**: 580852
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure DDoS Protection, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DDoS Protection custom policy is now generally available.

- Key changes or new features  
The new custom policy feature allows users to manually configure DDoS detection thresholds for their protected resources, overriding the default machine-learning auto-tuning. This enables more granular control over DDoS mitigation, particularly for latency-sensitive workloads or scenarios where default thresholds are not optimal. Policies can be tailored per resource, allowing organizations to better align DDoS protection with their specific application requirements.

- Target audience affected  
This update is relevant for IT professionals, security administrators, and developers managing Azure environments with DDoS Protection enabled—especially those supporting mission-critical, latency-sensitive applications or requiring custom security configurations.

- Important notes if any  
Custom policies provide flexibility but require careful configuration to avoid unintended impacts on application availability or performance. Microsoft recommends reviewing workload requirements and monitoring DDoS metrics when implementing custom thresholds. The feature is available for both Azure DDoS Protection Standard and Premium tiers. For more details and implementation guidance, refer to the official Azure documentation.

**Details**:

**Azure DDoS Protection Custom Policy – Comprehensive Technical Explanation**

**Background and Purpose of the Update**  
Azure DDoS Protection is designed to safeguard Azure resources from distributed denial-of-service (DDoS) attacks. Traditionally, the service has relied on machine-learning-driven auto-tuning to set detection thresholds for each protected resource, optimizing protection for most workloads. However, certain latency-sensitive or specialized workloads require more granular control over DDoS mitigation parameters. The introduction of custom policy support addresses this need, allowing IT professionals to tailor DDoS protection settings to the unique requirements of their applications.

**Specific Features and Detailed Changes**  
With this update, Azure DDoS Protection now supports custom policies, which are generally available. Custom policies enable users to override the default, auto-tuned detection thresholds and define specific parameters for DDoS mitigation. This feature allows for precise configuration of protection thresholds, such as specifying the sensitivity for traffic volume, connection rates, or other detection metrics. The change provides flexibility for organizations to optimize protection based on their workload characteristics, especially for applications where default thresholds may not be optimal.

**Technical Mechanisms and Implementation Methods**  
The custom policy feature is implemented by allowing administrators to create and assign bespoke DDoS protection policies to individual Azure resources. These policies are managed through the Azure portal, REST APIs, or ARM templates, enabling automation and integration into existing deployment pipelines. When a custom policy is applied, it supersedes the auto-tuned thresholds, and the DDoS mitigation system uses the specified parameters for attack detection and response. The underlying mechanism leverages Azure’s DDoS mitigation infrastructure, ensuring that custom policies are enforced in real-time and integrated with Azure’s monitoring and alerting capabilities.

**Use Cases and Application Scenarios**  
Custom policies are particularly valuable for:  
- **Latency-sensitive applications:** Where even minor delays caused by auto-tuned thresholds could impact user experience or business operations.  
- **High-throughput workloads:** That require higher thresholds to avoid false positives and unnecessary mitigation actions.  
- **Regulatory or compliance-driven environments:** Where specific detection and mitigation parameters are mandated.  
- **Multi-tenant platforms:** Where differentiated protection levels are needed for various tenants or services.

**Important Considerations and Limitations**  
- **Policy Management:** Custom policies must be carefully managed to avoid misconfiguration, which could either reduce protection effectiveness or increase the risk of false positives.  
- **Resource Scope:** Custom policies are applied per protected resource; administrators must ensure that each resource is assigned the appropriate policy.  
- **Monitoring:** It is essential to monitor the impact of custom policies using Azure’s built-in DDoS analytics and alerting tools to validate their effectiveness and adjust as necessary.  
- **Fallback:** If a custom policy is not specified, the system defaults to machine-learning auto-tuned thresholds.

**Integration with Related Azure Services**  
Azure DDoS Protection custom policies integrate seamlessly with other Azure security services, such as Azure Firewall, Azure Application Gateway, and Azure Security Center. Policies can be managed programmatically via Azure Resource Manager, enabling DevOps teams to incorporate DDoS protection into CI/CD workflows. Custom policy analytics and alerts are accessible through Azure Monitor, facilitating centralized security operations and incident response.

**Summary Sentence**  
Azure DDoS Protection custom policy is now generally available, enabling IT professionals to define and apply tailored DDoS mitigation thresholds for Azure resources, thereby enhancing protection flexibility and optimizing security for specialized workloads.

---

### 57. Private Preview: Slack integration for Azure SRE Agent

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Private Preview: Slack integration for Azure SRE Agent](https://azure.microsoft.com/updates?id=580768)

**Update ID**: 580768
**Data source**: Azure Updates API

**Categories**: In development, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SRE Agent now supports integration with Slack, available in private preview.

- Key changes or new features  
Organizations can interact with the Azure SRE Agent directly within Slack channels. Responders can mention the agent to initiate or follow up on incident investigations and receive relevant information and updates in real time. This integration streamlines incident response workflows by allowing teams to coordinate and manage Azure-related incidents without leaving Slack.

- Target audience affected  
Developers, Site Reliability Engineers (SREs), IT operations teams, and incident response teams who use Slack for collaboration and incident management.

- Important notes  
The Slack integration is currently in private preview, so access is limited. Interested organizations should request participation. This feature is designed to enhance productivity and response times for teams managing Azure incidents in Slack, reducing context-switching and improving communication. Further details and eligibility requirements are available via the Azure Updates page.

**Details**:

**Background and Purpose of the Update**  
The Azure SRE (Site Reliability Engineering) Agent is being extended to integrate with Slack, now available in private preview. This update addresses the need for organizations to streamline incident response workflows within their established communication platforms. Many IT and DevOps teams coordinate incident management and operational tasks in Slack channels; integrating the Azure SRE Agent directly into Slack aims to reduce context switching and improve response times by allowing responders to interact with the agent where they already collaborate.

**Specific Features and Detailed Changes**  
With this update, the Azure SRE Agent can be invoked within Slack channels. Responders can mention the agent to initiate or follow up on investigations, enabling direct engagement with Azure incident response tools from Slack. The integration allows responders to receive feedback and information from the agent in real-time, facilitating faster incident triage and resolution. The private preview focuses on enabling core incident response actions, such as starting investigations and receiving updates, directly within Slack’s messaging interface.

**Technical Mechanisms and Implementation Methods**  
The integration leverages Slack’s API and bot framework to embed the Azure SRE Agent as a Slack bot. Organizations will configure the agent within their Slack workspace, granting it access to designated channels. When a user mentions the agent, Slack’s event system triggers the bot, which communicates with Azure backend services to retrieve or update incident information. The agent’s responses are posted back into the Slack channel, ensuring seamless interaction. Authentication and authorization mechanisms are implemented to ensure only permitted users and channels can interact with the agent, maintaining security and compliance.

**Use Cases and Application Scenarios**  
- **Incident Response Coordination:** Teams can initiate investigations and monitor incident progress without leaving Slack, centralizing communication and reducing delays.
- **Post-Incident Follow-Up:** Responders can request updates or additional information from the Azure SRE Agent to support post-mortem analysis and documentation.
- **Automated Notifications:** The agent can provide automated alerts and updates in Slack channels, keeping all stakeholders informed during ongoing incidents.
- **Collaboration Across Teams:** Multiple teams can collaborate in Slack, leveraging the agent to share incident details and coordinate actions in real time.

**Important Considerations and Limitations**  
- **Private Preview Status:** The Slack integration is currently in private preview, meaning access is limited and features may change before general availability.
- **Security and Permissions:** Proper configuration is required to ensure that only authorized users can interact with the agent, and sensitive incident data is not exposed inappropriately.
- **Slack Workspace Configuration:** Organizations must ensure their Slack workspace supports bot integrations and that necessary permissions are granted.
- **Feature Scope:** The preview may not include all planned features; only core incident response actions are supported at this stage.

**Integration with Related Azure Services**  
The Slack integration extends the Azure SRE Agent’s capabilities, allowing it to interact with Azure’s incident management and monitoring services. The agent acts as a bridge between Slack and Azure, enabling responders to access Azure incident data and perform actions without leaving their Slack environment. This integration complements existing Azure monitoring and alerting tools, providing a unified experience for incident response and collaboration.

**Summary Sentence**  
Azure SRE Agent’s private preview Slack integration enables organizations to initiate and manage incident response workflows directly within Slack channels, streamlining collaboration and response by embedding Azure incident management capabilities into established communication platforms.

---

### 58. Public Preview: Microsoft Entra Agent ID and Agent 365 for Azure SRE Agent

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Microsoft Entra Agent ID and Agent 365 for Azure SRE Agent](https://azure.microsoft.com/updates?id=580763)

**Update ID**: 580763
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SRE Agent now supports Microsoft Entra Agent ID and Microsoft Agent 365, available in public preview.

- Key changes or new features  
Security and IT teams can now view and manage Azure SRE Agents alongside other agents in their organization using Microsoft Entra Agent ID and Agent 365. Each SRE Agent can be assigned a unique Agent ID, improving identity management, governance, and visibility. Integration with Microsoft Agent 365 enables unified agent lifecycle management and policy enforcement.

- Target audience affected  
This update is relevant for developers, IT professionals, and security teams who manage Azure SRE Agents and require enhanced identity and governance capabilities.

- Important notes  
The feature is currently in public preview, so it may not be suitable for production environments. Organizations can begin testing the integration to streamline agent management and improve security posture. Feedback during the preview phase is encouraged to help refine the feature before general availability.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Microsoft Entra Agent ID and Agent 365 for Azure SRE Agent  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=580763)

---

**Background and Purpose of the Update**

This update introduces support for Microsoft Entra Agent ID and Microsoft Agent 365 within the Azure SRE (Site Reliability Engineering) Agent, now available in public preview. The primary purpose is to enhance visibility and governance of SRE agents by integrating them into the broader organizational agent management ecosystem. Security and IT teams can now manage SRE agents alongside other agents, streamlining identity and access management processes.

---

**Specific Features and Detailed Changes**

- **Agent ID Assignment:** Each Azure SRE Agent can now be assigned a unique Microsoft Entra Agent ID. This enables individual identification and management of SRE agents, supplementing their existing identities.
- **Agent 365 Support:** Integration with Microsoft Agent 365 allows SRE agents to be governed using the same tools and policies applied to other agents within the organization.
- **Unified Governance:** Security and IT teams gain the ability to view, monitor, and govern SRE agents in the same context as other organizational agents, improving consistency in policy enforcement and compliance.

---

**Technical Mechanisms and Implementation Methods**

- **Entra Agent ID Integration:** The Azure SRE Agent is now registered within Microsoft Entra, leveraging Entra’s identity management capabilities. Each agent receives an Entra Agent ID, which is used for authentication, authorization, and tracking.
- **Agent 365 Connectivity:** By supporting Microsoft Agent 365, the SRE Agent can be managed through the same interface and APIs as other agents. This includes lifecycle management, access control, and auditing.
- **Governance Tools:** Existing Microsoft Entra and Agent 365 governance tools (such as access reviews, policy assignment, and reporting) can now be applied to SRE agents, enabling centralized management.

---

**Use Cases and Application Scenarios**

- **Security and Compliance:** Organizations can enforce security policies and compliance requirements on SRE agents, ensuring they adhere to the same standards as other agents.
- **Unified Agent Management:** IT teams can manage SRE agents alongside other agents, simplifying administrative tasks and reducing operational complexity.
- **Audit and Reporting:** With unique Agent IDs, SRE agent activity can be tracked and audited, supporting incident response and regulatory reporting.

---

**Important Considerations and Limitations**

- **Public Preview Status:** The features are currently in public preview, which may entail limited support and potential changes before general availability.
- **Agent ID Assignment:** Each agent must be assigned an Agent ID; processes for assignment and management should be reviewed for compatibility with existing workflows.
- **Integration Requirements:** Organizations must ensure their Azure SRE Agents are compatible with Microsoft Entra and Agent 365 for seamless integration.

---

**Integration with Related Azure Services**

- **Microsoft Entra:** Provides identity and access management for SRE agents, enabling centralized authentication and governance.
- **Microsoft Agent 365:** Facilitates lifecycle and policy management for SRE agents, aligning them with other organizational agents.
- **Azure SRE Agent:** Now interoperates with Entra and Agent 365, leveraging their capabilities for improved security and management.

---

**Summary Sentence**

Azure SRE Agent now supports Microsoft Entra Agent ID and Agent 365 in public preview, enabling security and IT teams to view and govern SRE agents alongside other organizational agents with enhanced identity and management capabilities.

---

### 59. Public Preview: Agent-to-Agent (A2A) protocol support in Azure SRE Agent

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Agent-to-Agent (A2A) protocol support in Azure SRE Agent](https://azure.microsoft.com/updates?id=580758)

**Update ID**: 580758
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SRE Agent now supports the open Agent-to-Agent (A2A) protocol in public preview.

- Key changes or new features  
The A2A protocol enables Azure SRE agents to delegate tasks to other agents and accept tasks from them, while maintaining each agent’s original team permissions. This allows for secure cross-team collaboration and task automation. For example, an application team’s agent can request investigation from a platform team’s agent without exposing sensitive permissions or credentials.

- Target audience affected  
Developers and IT professionals managing Azure environments, especially those using Azure SRE Agent for incident response, automation, or cross-team operations.

- Important notes  
The feature is currently in public preview and may not be suitable for production workloads. Teams can leverage A2A for improved automation and collaboration, but should review permission boundaries and integration scenarios. Feedback is encouraged during the preview phase to help refine the protocol and its implementation.

**Details**:

**Azure Update Report: Public Preview of Agent-to-Agent (A2A) Protocol Support in Azure SRE Agent**

**Background and Purpose of the Update:**  
The Azure SRE (Site Reliability Engineering) Agent is a tool designed to automate and orchestrate operational tasks within Azure environments. Traditionally, SRE agents operated independently, limiting the ability to delegate or coordinate tasks across different teams or agents. The introduction of Agent-to-Agent (A2A) protocol support addresses this limitation by enabling direct communication and task delegation between agents. The purpose of this update is to enhance cross-team collaboration and operational efficiency, while maintaining clear boundaries of team permissions and responsibilities.

**Specific Features and Detailed Changes:**  
With the public preview of A2A protocol support, Azure SRE Agents can now:
- **Hand off tasks to other SRE agents:** One agent can delegate specific operational tasks to another agent, facilitating distributed workflows.
- **Accept tasks from other agents:** Agents can receive and process tasks initiated by external agents.
- **Retain team-specific permissions:** Each agent continues to enforce its own team’s access controls and permissions, ensuring that delegation does not compromise security or compliance.

This update introduces interoperability between agents, which was previously unavailable, and enables more flexible and scalable automation scenarios.

**Technical Mechanisms and Implementation Methods:**  
The A2A protocol is an open standard that defines how agents communicate and exchange tasks. When an agent needs to delegate a task, it uses the A2A protocol to securely transmit the task request to the target agent. The receiving agent authenticates the request, verifies permissions, and executes the task if authorized. All communication is governed by each agent’s existing security context, ensuring that only permitted actions are performed.

The protocol implementation in Azure SRE Agent is designed to be extensible and secure, supporting encrypted communication and robust authentication mechanisms. Agents can be configured to accept or reject incoming task requests based on predefined policies.

**Use Cases and Application Scenarios:**  
- **Cross-team incident response:** An application team’s SRE agent can escalate or delegate remediation tasks to a platform or infrastructure team’s agent without manual intervention.
- **Automated workflow orchestration:** Complex operational workflows that span multiple teams or domains can be automated, with each agent handling its respective segment of the process.
- **Separation of duties:** Teams can collaborate on shared incidents or maintenance tasks while maintaining strict boundaries over what actions can be performed by external agents.

**Important Considerations and Limitations:**  
- **Public Preview status:** The A2A protocol support is currently in public preview, which means it is not recommended for production-critical workloads until general availability.
- **Permission boundaries:** While agents retain their own permissions, careful configuration is required to ensure that delegation does not inadvertently grant excessive access.
- **Inter-agent trust:** Organizations should establish clear trust relationships and policies for which agents are allowed to communicate and delegate tasks.

**Integration with Related Azure Services:**  
Azure SRE Agent with A2A protocol support can be integrated into existing Azure automation and monitoring workflows. It complements Azure Monitor, Azure Automation, and other operational tools by enabling more granular and collaborative task management across teams. Integration points may include alert-driven automation, incident management, and workflow orchestration.

**Summary:**  
The public preview of Agent-to-Agent (A2A) protocol support in Azure SRE Agent enables secure, permission-aware task delegation and collaboration between agents, improving cross-team operational efficiency while maintaining strict access controls.

---

### 60. Public Preview: Microsoft Teams integration for Azure SRE Agent

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Microsoft Teams integration for Azure SRE Agent](https://azure.microsoft.com/updates?id=580753)

**Update ID**: 580753
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Microsoft Teams integration for Azure SRE Agent is now available in public preview.

- Key changes or new features  
Azure SRE Agent can participate directly in Microsoft Teams conversations. Engineers can initiate investigations, review findings, and collaborate with the agent within Teams, including one-on-one chats, group chats, channels, and meeting chats. This integration streamlines incident response and troubleshooting workflows by allowing users to interact with the SRE Agent without switching between platforms.

- Target audience affected  
Developers, Site Reliability Engineers (SREs), IT professionals, and operations teams who use Azure SRE Agent and Microsoft Teams for incident management and collaboration.

- Important notes if any  
This feature is currently in public preview, so it may not be fully production-ready and could be subject to changes. Users should test the integration in non-critical environments before full deployment. The update aims to improve efficiency and collaboration during incident investigations by centralizing communication and automation within Teams. For more information and access, refer to the official Azure Update link.

**Details**:

**Background and Purpose of the Update**  
The integration of Azure SRE (Site Reliability Engineering) Agent with Microsoft Teams, now available in public preview, is designed to streamline incident management and operational workflows for engineering teams. The purpose of this update is to enable engineers to interact with the Azure SRE Agent directly within Microsoft Teams, thereby reducing context-switching and improving collaboration during investigations and follow-ups.

**Specific Features and Detailed Changes**  
With this update, the Azure SRE Agent can participate in Microsoft Teams conversations across various communication modes, including one-on-one chats, group chats, channels, and meeting chats. Engineers are empowered to initiate investigations, track findings, and collaborate with the SRE Agent without leaving the Teams environment. This integration supports conversational workflows, allowing users to invoke the agent’s capabilities through chat commands and receive responses within the Teams interface.

**Technical Mechanisms and Implementation Methods**  
The technical implementation leverages Microsoft Teams’ extensibility framework, likely utilizing bots or app integrations to embed the Azure SRE Agent within Teams. The agent operates as a Teams app, responding to user inputs in real-time and facilitating investigation workflows. Communication between Teams and Azure SRE Agent is managed via secure APIs, ensuring that operational data and findings are exchanged efficiently and securely. The integration supports multiple conversation contexts, enabling the agent to maintain state and context across different chat types (individual, group, channel, and meeting).

**Use Cases and Application Scenarios**  
Typical use cases include:
- Initiating incident investigations directly from a Teams channel during an outage or performance issue.
- Collaborating with team members and the SRE Agent in group chats to analyze findings and determine remediation steps.
- Utilizing the agent in meeting chats to provide real-time updates and insights during incident review sessions.
- Following up on previous findings and actions in one-on-one chats with the SRE Agent for detailed analysis or post-mortem discussions.

This integration is particularly valuable for distributed engineering teams who rely on Teams for daily communication and need seamless access to SRE tools during operational events.

**Important Considerations and Limitations**  
As this feature is in public preview, it may have limitations regarding stability, scalability, and feature completeness. Organizations should evaluate the integration in non-production environments before widespread adoption. Security and compliance considerations must be addressed, ensuring that sensitive operational data exchanged with the SRE Agent within Teams adheres to organizational policies. Additionally, integration may require configuration of Teams permissions and app policies to enable the SRE Agent in relevant channels and chats.

**Integration with Related Azure Services**  
The Azure SRE Agent is designed to work in conjunction with other Azure operational tools and services. Its integration with Teams enhances collaboration around Azure resources, incidents, and findings. The agent may interact with Azure Monitor, Azure Resource Manager, and other Azure services to provide contextual insights and automate investigation workflows within Teams. This unified experience enables engineers to leverage Azure’s operational capabilities without leaving their primary communication platform.

**Summary Sentence**  
The public preview of Microsoft Teams integration for Azure SRE Agent enables engineers to initiate investigations, collaborate, and follow up on findings directly within Teams chats and channels, streamlining operational workflows and enhancing incident management without leaving the Teams environment.

---

### 61. Generally Available: Azure Infrastructure Resiliency Manager

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Infrastructure Resiliency Manager](https://azure.microsoft.com/updates?id=580748)

**Update ID**: 580748
**Data source**: Azure Updates API

**Categories**: Launched, Microsoft Ignite

**Summary**:

- What was updated  
Azure Infrastructure Resiliency Manager is now generally available.

- Key changes or new features  
The service provides a unified, goal-driven platform to enhance application resiliency across Azure. It enables users to deploy applications with zonal resiliency using deployment templates, assess application resiliency at scale, and receive actionable recommendations to improve infrastructure reliability. The manager integrates resiliency best practices into the deployment process, helping teams proactively identify and mitigate risks.

- Target audience affected  
Developers and IT professionals responsible for designing, deploying, and maintaining applications on Azure, especially those requiring high availability and disaster recovery.

- Important notes if any  
This release allows teams to start with resilient architectures from the outset and continuously monitor and improve their deployments. Integration with Azure deployment workflows streamlines adoption. Using the manager can help meet compliance and business continuity requirements more efficiently. For more details, visit the official Azure Update page: https://azure.microsoft.com/updates?id=580748

**Details**:

**Azure Update Report: Generally Available – Azure Infrastructure Resiliency Manager**

**Background and Purpose of the Update:**  
The Azure Infrastructure Resiliency Manager has reached general availability, signifying its readiness for production use. This tool is introduced to address the increasing need for robust application resiliency in cloud environments. Its primary purpose is to provide a unified, goal-driven platform that enables organizations to systematically strengthen the resiliency of their applications deployed on Azure infrastructure.

**Specific Features and Detailed Changes:**  
With this release, users gain access to a consolidated experience for managing and improving application resiliency. Key features include:
- **Zonally Resilient Deployment Templates:** The service allows users to initiate deployments using templates specifically designed for zonal resiliency, ensuring that applications are architected to withstand zone-level failures within Azure regions.
- **Application Assessment:** The manager provides capabilities to assess the resiliency of applications at scale, enabling organizations to identify potential vulnerabilities and areas for improvement across their Azure workloads.

**Technical Mechanisms and Implementation Methods:**  
Azure Infrastructure Resiliency Manager leverages Azure’s infrastructure-as-code (IaC) approach through deployment templates that are pre-configured for zonal resiliency. These templates enforce best practices such as distributing resources across multiple availability zones, thereby minimizing the risk of downtime due to localized failures. The assessment functionality likely involves automated analysis of deployed resources, configurations, and dependencies to evaluate adherence to resiliency standards and highlight gaps.

**Use Cases and Application Scenarios:**  
- **Enterprise Cloud Migration:** Organizations migrating critical workloads to Azure can use the Resiliency Manager to ensure that new deployments meet organizational and regulatory resiliency requirements from the outset.
- **Continuous Improvement:** DevOps teams can integrate resiliency assessments into their CI/CD pipelines to continuously monitor and enhance the resiliency posture of their applications.
- **Disaster Recovery Planning:** IT teams can utilize the tool to validate that their disaster recovery strategies are supported by resilient infrastructure configurations.

**Important Considerations and Limitations:**  
- The service is designed to work within the Azure ecosystem and is optimized for applications that can leverage zonal resiliency.
- Users must ensure that their workloads are compatible with zonally resilient architectures and that their deployment processes can incorporate the provided templates.
- The assessment capabilities are intended for applications deployed at scale, and may require integration with existing management and monitoring workflows.

**Integration with Related Azure Services:**  
Azure Infrastructure Resiliency Manager integrates seamlessly with Azure Resource Manager (ARM) for template-based deployments. It complements existing Azure resiliency features such as Availability Zones, Azure Site Recovery, and Azure Monitor by providing a centralized platform for resiliency planning and assessment. This integration enables organizations to align their infrastructure deployments with Azure’s native high-availability and disaster recovery offerings.

**Summary Sentence:**  
Azure Infrastructure Resiliency Manager is now generally available, providing a unified, goal-driven platform for deploying and assessing zonally resilient applications at scale, thereby enhancing the resiliency of workloads across Azure environments.

---

### 62. Public Preview: New integration, hybrid deployment, and observability capabilities in Azure Logic Apps 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: New integration, hybrid deployment, and observability capabilities in Azure Logic Apps ](https://azure.microsoft.com/updates?id=580589)

**Update ID**: 580589
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite

**Summary**:

**Public Preview: New integration, hybrid deployment, and observability capabilities in Azure Logic Apps**

- **What was updated:**  
Azure Logic Apps has released new and enhanced features in public preview to improve integration, hybrid deployment, and observability for enterprise workflows.

- **Key changes or new features:**  
  - Expanded integration options for connecting enterprise systems and modernizing legacy workflows.
  - Enhanced hybrid deployment capabilities, allowing workflows to run seamlessly across cloud, on-premises, and hybrid environments.
  - Improved observability tools for monitoring, troubleshooting, and optimizing Logic Apps workflows.
  - Support for more connectors and triggers, increasing flexibility for developers.
  - Updates to management and deployment experiences, including improved tooling and automation support.

- **Target audience affected:**  
Developers building integration workflows, IT professionals managing hybrid and multi-cloud environments, and organizations needing to modernize legacy systems or connect disparate enterprise applications.

- **Important notes:**  
These features are currently in public preview and may change before general availability. Early adopters can test and provide feedback, but production use should consider preview limitations. Enhanced hybrid and observability features can significantly improve reliability and monitoring for business-critical workflows. For more details, visit the [Azure Update link](https://azure.microsoft.com/updates?id=580589).

**Details**:

**Azure Update Report: Public Preview – New Integration, Hybrid Deployment, and Observability Capabilities in Azure Logic Apps**

**Background and Purpose of the Update**  
Azure Logic Apps is a leading integration platform as a service (iPaaS) within the Azure ecosystem, enabling organizations to automate workflows and orchestrate business processes across diverse systems. The purpose of this update is to extend Logic Apps’ capabilities, allowing organizations to more effectively connect enterprise systems, modernize legacy integrations, and support business-critical workflows that span cloud, on-premises, and hybrid environments. This aligns with the growing demand for flexible integration solutions that bridge legacy and modern systems while providing robust monitoring and management.

**Specific Features and Detailed Changes**  
The update introduces new and enhanced features in three main areas:
1. **Integration**: Expanded capabilities to connect with a broader range of enterprise systems, including both modern cloud services and legacy on-premises applications.
2. **Hybrid Deployment**: Enhanced support for running Logic Apps workflows not only in Azure but also on-premises and across hybrid environments, increasing deployment flexibility and supporting regulatory or data residency requirements.
3. **Observability**: Improved tools and features for monitoring, logging, and diagnosing Logic Apps workflows, enabling better operational visibility and faster troubleshooting for business-critical processes.

**Technical Mechanisms and Implementation Methods**  
- **Integration**: The platform likely leverages new or updated connectors and adapters, enabling seamless communication between Logic Apps and various enterprise systems. This may include support for additional protocols, authentication methods, or data formats.
- **Hybrid Deployment**: Logic Apps can now be deployed and executed in multiple environments. This is typically achieved through containerization (e.g., Docker) or by running Logic Apps on Azure Arc-enabled infrastructure, allowing workflows to execute close to data sources or within specific network boundaries.
- **Observability**: Enhanced observability is generally implemented through deeper integration with Azure Monitor, Application Insights, and Log Analytics. This provides granular telemetry, custom logging, and alerting capabilities for workflow executions, failures, and performance metrics.

**Use Cases and Application Scenarios**  
- **Enterprise Integration**: Connecting ERP, CRM, and other line-of-business systems across cloud and on-premises environments.
- **Legacy Modernization**: Wrapping legacy systems with Logic Apps workflows to enable modern API-driven integrations without replacing existing infrastructure.
- **Hybrid Workflows**: Running workflows that require access to both cloud services and on-premises data sources, such as synchronizing data between on-premises SQL Server and Azure-based applications.
- **Business-Critical Operations**: Implementing mission-critical workflows with enhanced monitoring and alerting to ensure high availability and rapid incident response.

**Important Considerations and Limitations**  
- As this is a public preview, features may not be production-ready and could change before general availability.
- Hybrid deployment scenarios may require additional configuration, such as network connectivity, security policies, and infrastructure prerequisites.
- Observability enhancements may necessitate integration with Azure monitoring tools and possible updates to existing monitoring strategies.

**Integration with Related Azure Services**  
- **Azure Arc**: Facilitates hybrid deployment by enabling Logic Apps to run on-premises or in other clouds.
- **Azure Monitor, Application Insights, and Log Analytics**: Provide the backbone for enhanced observability, enabling centralized monitoring and diagnostics.
- **Azure Connectors and API Management**: Support integration with a wide range of services and APIs, both within and outside Azure.

**Summary Sentence**  
Azure Logic Apps’ public preview introduces expanded integration, hybrid deployment, and observability capabilities, enabling organizations to connect and monitor business-critical workflows across cloud, on-premises, and hybrid environments with greater flexibility and operational insight.

---

### 63. Public Preview: Enhanced developer experience in Azure Logic Apps Automation 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Enhanced developer experience in Azure Logic Apps Automation ](https://azure.microsoft.com/updates?id=580559)

**Update ID**: 580559
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite

**Summary**:

- What was updated  
Azure Logic Apps Automation now offers an enhanced developer experience, available in Public Preview.

- Key changes or new features  
  - Refreshed workflow designer: Improved UI and usability for building automation workflows.  
  - Reusable templates: Developers can create and leverage templates for common automation scenarios, speeding up workflow creation.  
  - Faster environment and application provisioning: Reduced setup time for Logic Apps environments, enabling quicker development and deployment.  
  - Improved management and scaling capabilities: Easier to manage and scale business process automations within Logic Apps.

- Target audience affected  
Developers and IT professionals working with Azure Logic Apps for business process automation, especially those building, managing, or scaling workflows.

- Important notes  
This update is currently in Public Preview, so features may change before general availability. Developers should test the new capabilities and provide feedback. The enhancements aim to streamline workflow development and deployment, making Logic Apps more accessible and efficient for automation projects.

Link: [Azure Update](https://azure.microsoft.com/updates?id=580559)

**Details**:

**Azure Update Report: Public Preview – Enhanced Developer Experience in Azure Logic Apps Automation**

**Background and Purpose of the Update**  
Azure Logic Apps Automation is a cloud-based service designed to automate business processes and workflows. The public preview introduces enhancements aimed at improving the developer experience, specifically targeting the speed and ease of building, managing, and scaling business process automation. The purpose of this update is to streamline workflow development, reduce complexity, and enable faster deployment cycles for automation solutions.

**Specific Features and Detailed Changes**  
The update delivers several key enhancements:

- **Refreshed Workflow Designer:** The workflow designer interface has been updated to provide a more intuitive and efficient experience. This enables developers to visually construct and modify workflows with improved usability, reducing the time required to design and debug automation logic.
- **Reusable Templates:** Logic Apps Automation now supports reusable templates, allowing developers to create, share, and deploy standardized workflow components. This feature promotes consistency, accelerates development, and simplifies maintenance by enabling the reuse of common patterns across multiple automation projects.
- **Faster Environment and Application Provisioning:** The update includes improvements to the provisioning process, enabling quicker setup of environments and applications. This reduces the lead time for initiating new automation projects and facilitates rapid scaling of business process automation.

**Technical Mechanisms and Implementation Methods**  
The enhanced workflow designer leverages updated UI/UX paradigms and underlying engine optimizations to provide a smoother design experience. Reusable templates are implemented as modular workflow definitions that can be instantiated within Logic Apps projects, supporting parameterization and versioning. Faster provisioning is achieved through optimized resource management and deployment pipelines within Azure, reducing latency and improving reliability during environment setup.

**Use Cases and Application Scenarios**  
These enhancements are particularly valuable in scenarios such as:

- **Enterprise Process Automation:** Organizations automating complex business processes (e.g., order processing, HR onboarding) can benefit from reusable templates and improved workflow design, ensuring rapid development and consistent deployment.
- **DevOps and CI/CD Integration:** Teams leveraging Logic Apps for automated deployments or operational workflows can utilize faster provisioning to streamline their pipelines.
- **Integration Solutions:** Developers building integrations between Azure services or external systems can use the refreshed designer and templates to accelerate solution delivery and maintain standardization across projects.

**Important Considerations and Limitations**  
As this update is in public preview, it may not be suitable for production workloads. Users should validate functionality and performance in test environments before widespread adoption. There may be limitations in template customization, designer features, or provisioning speed depending on region or resource constraints. Documentation and support may also be limited during the preview phase.

**Integration with Related Azure Services**  
Logic Apps Automation integrates seamlessly with other Azure services such as Azure Functions, Azure Event Grid, and Azure Service Bus. The enhanced developer experience supports easier orchestration of workflows that span multiple services, enabling robust automation solutions. Reusable templates can be leveraged in conjunction with Azure DevOps for CI/CD pipelines, and faster provisioning aligns with resource management in Azure Resource Manager.

**Summary Sentence**  
Azure Logic Apps Automation’s public preview introduces a refreshed workflow designer, reusable templates, and faster provisioning, significantly improving the developer experience for building, managing, and scaling business process automation in Azure.

---

### 64. Public Preview: Managed AI Models in Logic Apps Automation 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Managed AI Models in Logic Apps Automation ](https://azure.microsoft.com/updates?id=580554)

**Update ID**: 580554
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite

**Summary**:

- What was updated  
Azure Logic Apps Automation now supports Managed AI Models in public preview.

- Key changes or new features  
Developers can integrate AI capabilities directly into Logic Apps workflows and automation agents without needing to provision, deploy, or manage AI model infrastructure. This update streamlines the process of building AI-powered automation by providing ready-to-use managed models, reducing operational overhead and accelerating development. The integration is API-driven, allowing seamless access to AI functions within workflow logic.

- Target audience affected  
Developers and IT professionals working with Azure Logic Apps, particularly those building workflow automation or looking to incorporate AI features (such as classification, prediction, or language processing) into business processes.

- Important notes  
Managed AI Models are in public preview and may not be suitable for production workloads yet. Users should review documentation for supported model types and limitations. This feature simplifies AI integration, but developers should assess compliance and data privacy requirements when using managed AI services.  
Link: https://azure.microsoft.com/updates?id=580554

**Details**:

**Azure Update Technical Explanation: Public Preview – Managed AI Models in Logic Apps Automation**

**Background and Purpose of the Update**  
This update introduces Managed AI Models in public preview for Azure Logic Apps Automation. The primary goal is to enable developers to seamlessly integrate AI capabilities into their automation workflows and agents without the need to provision, deploy, or manage the underlying model infrastructure. This enhancement addresses the complexity and operational overhead traditionally associated with embedding AI into business processes, making AI-powered automation more accessible and efficient.

**Specific Features and Detailed Changes**  
- **Managed AI Models Availability:** Developers can now access and use pre-built, managed AI models directly within Logic Apps workflows.
- **No Infrastructure Management:** There is no requirement to handle model provisioning, deployment, or lifecycle management; Azure handles these aspects automatically.
- **Workflow Integration:** AI model actions can be natively incorporated into Logic Apps workflows, enabling advanced automation scenarios with minimal configuration.
- **Public Preview Scope:** The feature is currently in public preview, meaning it is available for testing and feedback but not yet generally available or recommended for production workloads.

**Technical Mechanisms and Implementation Methods**  
- **Service-Managed Model Hosting:** The AI models are hosted and maintained by Azure, abstracting infrastructure concerns from the user.
- **Logic Apps Designer Integration:** Developers can select and configure managed AI model actions within the Logic Apps Designer, allowing for drag-and-drop workflow composition.
- **No-Code/Low-Code Enablement:** The integration supports both no-code and low-code approaches, making it accessible to a wide range of users, including those without deep AI or data science expertise.
- **Automation Agent Support:** Managed AI models can be invoked as part of automated agents or workflow steps, facilitating intelligent decision-making and automation.

**Use Cases and Application Scenarios**  
- **Document Processing:** Automatically classify, extract, or summarize content from documents as part of a workflow.
- **Email Automation:** Use AI models to analyze, route, or respond to emails based on content or sentiment.
- **Customer Support:** Integrate AI-driven responses or triage actions within support ticketing workflows.
- **Data Enrichment:** Enhance data pipelines by applying AI models for tagging, categorization, or prediction within automated processes.

**Important Considerations and Limitations**  
- **Preview Status:** As a public preview feature, Managed AI Models may have limited support, potential changes, and should not be used for production-critical workloads.
- **Model Selection:** Only the managed models provided by Azure are available; custom model deployment is not covered by this update.
- **Compliance and Data Handling:** Users should review data privacy and compliance implications, as data sent to managed models is processed within Azure’s managed infrastructure.

**Integration with Related Azure Services**  
- **Logic Apps:** Direct integration enables AI actions as part of workflow steps.
- **Azure Automation:** Enhances automation scenarios by embedding AI-driven logic.
- **Other Azure Services:** While not explicitly mentioned, Managed AI Models can complement data flows involving Azure Functions, Azure Data Factory, and other workflow-enabled services through Logic Apps.

**Summary Sentence**  
Azure Logic Apps Automation now offers Managed AI Models in public preview, allowing developers to easily embed AI capabilities into workflows without managing model infrastructure, thereby accelerating the development of intelligent automation solutions.

---

### 65. Public Preview: Virtual network integration in Logic Apps Automation

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Virtual network integration in Logic Apps Automation](https://azure.microsoft.com/updates?id=580549)

**Update ID**: 580549
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite

**Summary**:

- What was updated  
Azure Logic Apps Automation now supports Virtual Network (VNet) integration in public preview.

- Key changes or new features  
Organizations can securely connect Logic Apps workflows and automation agents to resources within their Azure VNets. This enables private communication between Logic Apps and services such as databases, storage accounts, and other internal APIs, without exposing traffic to the public internet. VNet integration enhances security, compliance, and control over network traffic for automated business processes.

- Target audience affected  
Developers building automation workflows with Azure Logic Apps, IT professionals managing network security and connectivity, and organizations requiring secure integration between Logic Apps and internal Azure resources.

- Important notes if any  
VNet integration is currently in public preview, so production use should be approached with caution. Review documentation for supported scenarios and limitations. Existing Logic Apps workflows may require configuration updates to leverage VNet connectivity. This feature is particularly relevant for organizations with strict security or compliance requirements.

**Details**:

**Azure Update Report: Public Preview – Virtual Network Integration in Logic Apps Automation**

**Background and Purpose of the Update**  
Azure Logic Apps Automation enables organizations to automate business processes and workflows. Traditionally, Logic Apps operated in a public network context, which limited secure connectivity to resources residing within private Azure Virtual Networks (VNets). The introduction of VNet integration addresses this gap, allowing organizations to securely connect Logic Apps workflows and automation agents to resources within their Azure VNets. The primary purpose of this update is to enhance security, compliance, and network isolation for automated workflows, aligning with enterprise requirements for secure cloud automation.

**Specific Features and Detailed Changes**  
With this public preview, Logic Apps Automation now supports direct integration with Azure VNets. This feature allows workflows and automation agents to access resources such as databases, storage accounts, or other services that are restricted to a private network. The update introduces configuration options for associating Logic Apps Automation resources with specific VNets, enabling secure communication and access control. This change enhances the ability to automate processes that require interaction with internal systems or services not exposed to the public internet.

**Technical Mechanisms and Implementation Methods**  
VNet integration is achieved by configuring Logic Apps Automation to use a private endpoint within a specified VNet. This mechanism ensures that all traffic between Logic Apps Automation and the target resources is routed securely within the Azure backbone network, avoiding exposure to the public internet. The integration leverages Azure networking constructs such as subnets, private endpoints, and network security groups (NSGs) to control and monitor access. IT professionals can configure VNet integration via the Azure portal, ARM templates, or CLI, specifying the target VNet and subnet for the Logic Apps Automation instance.

**Use Cases and Application Scenarios**  
This update is particularly valuable for scenarios where automated workflows must interact with sensitive or internal resources. Example use cases include:
- Automating database maintenance tasks on SQL servers accessible only within a private VNet.
- Orchestrating workflows that require access to internal APIs or services not exposed publicly.
- Integrating with on-premises resources connected via Azure VPN Gateway or ExpressRoute.
- Ensuring compliance with regulatory requirements by restricting workflow execution to private network boundaries.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not yet be suitable for production workloads requiring full SLA guarantees. Organizations should evaluate the preview status and monitor for updates regarding general availability. Additional considerations include:
- Compatibility with existing Logic Apps Automation configurations and workflows.
- Potential limitations in supported regions or resource types.
- Required permissions for configuring VNet integration.
- Network configuration prerequisites, such as available subnets and proper NSG rules to permit necessary traffic.

**Integration with Related Azure Services**  
VNet integration in Logic Apps Automation enhances interoperability with other Azure services that support private networking, such as Azure SQL Database, Azure Storage, and Azure Key Vault. It enables secure automation of workflows that interact with these services within a VNet. Additionally, it complements Azure networking solutions like VPN Gateway and ExpressRoute, facilitating hybrid connectivity scenarios.

**Summary Sentence**  
Azure Logic Apps Automation now supports public preview of virtual network integration, enabling secure and private connectivity between automated workflows and resources within Azure VNets, thereby enhancing security, compliance, and network isolation for enterprise automation scenarios.

---

### 66. Public Preview: New built-in Azure automation connectors in Logic Apps Automation 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: New built-in Azure automation connectors in Logic Apps Automation ](https://azure.microsoft.com/updates?id=580544)

**Update ID**: 580544
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Logic Apps Automation now offers new built-in connectors for Azure Automation, available in public preview.

- Key changes or new features  
The update introduces connectors that enable seamless automation of workflows across GitHub, Azure DevOps, and Azure management services. Developers and IT professionals can now integrate these platforms directly into Logic Apps, streamlining tasks such as code deployment, CI/CD pipeline management, and cloud resource operations without custom connector development. This enhances automation capabilities and reduces manual intervention in development and cloud operations.

- Target audience affected  
Developers, DevOps engineers, and IT professionals who use Azure Logic Apps for workflow automation, especially those managing code repositories, CI/CD pipelines, and Azure resources.

- Important notes if any  
The connectors are currently in public preview, so production use should be approached with caution. Feedback is encouraged to help improve the feature before general availability. Documentation and sample workflows are available to assist with integration and testing.

**Details**:

**Azure Update Report: Public Preview – New Built-in Azure Automation Connectors in Logic Apps Automation**

**Background and Purpose of the Update**  
This update introduces new built-in connectors for Azure automation within Azure Logic Apps Automation, now available in public preview. The primary purpose is to empower developers and IT professionals to automate workflows that span multiple platforms, including GitHub, Azure DevOps, and Azure management services. This enhancement addresses the growing need for streamlined automation across development and cloud operations, reducing manual intervention and improving operational efficiency.

**Specific Features and Detailed Changes**  
The new built-in connectors are integrated directly into Azure Logic Apps Automation. These connectors facilitate seamless interaction with GitHub, Azure DevOps, and Azure management services, enabling users to automate tasks such as code deployment, repository management, CI/CD pipeline orchestration, and cloud resource administration. The update expands the automation capabilities of Logic Apps by providing native support for these services, eliminating the need for custom connectors or additional integration work.

**Technical Mechanisms and Implementation Methods**  
Technically, the built-in connectors leverage Azure Logic Apps’ workflow engine, allowing users to design and execute automation flows using a visual designer or code-based definitions. The connectors are pre-configured to authenticate and interact with their respective services (GitHub, Azure DevOps, Azure management APIs), supporting actions such as triggering events, managing resources, and updating repositories. The implementation relies on secure API calls and Azure’s identity management to ensure safe and reliable automation. Developers can incorporate these connectors into Logic Apps workflows, chaining actions and conditions to build complex automation scenarios.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Automating code repository management in GitHub (e.g., auto-merging pull requests, updating issues).
- Orchestrating CI/CD pipelines in Azure DevOps (e.g., triggering builds, deploying artifacts).
- Managing Azure resources (e.g., provisioning VMs, updating configurations, monitoring resource states).
- Integrating development workflows with cloud operations, such as automatically deploying code changes to Azure services upon successful builds in DevOps.
- Creating incident response workflows that interact with both development and cloud management platforms.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not be suitable for production workloads due to potential stability or feature limitations. Users should review the preview documentation for supported actions, authentication requirements, and any known issues. It is important to validate workflows in a test environment before deploying to production. Additionally, integration with external services (GitHub, Azure DevOps) may require specific permissions and setup, such as OAuth authentication or service principals.

**Integration with Related Azure Services**  
These connectors are designed to work natively within Azure Logic Apps Automation, leveraging Azure’s workflow orchestration, identity management, and monitoring capabilities. They can be combined with other Logic Apps connectors (e.g., email, notification, database) to build end-to-end automation solutions. Integration with Azure management services enables direct interaction with Azure resources, supporting hybrid automation scenarios across development and operations.

**Summary Sentence**  
The public preview of new built-in Azure automation connectors in Logic Apps Automation enables developers to automate workflows across GitHub, Azure DevOps, and Azure management services, streamlining development and cloud operations through native integration and enhanced workflow orchestration.

---

### 67. Public Preview: Decision actions in Azure Logic Apps Automation 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Decision actions in Azure Logic Apps Automation ](https://azure.microsoft.com/updates?id=580539)

**Update ID**: 580539
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Logic Apps Automation now supports Decision actions in public preview.

- Key changes or new features  
Decision actions allow developers to automate business decisions within Logic Apps using AI capabilities, without the need to deploy or manage custom AI models. This feature enables workflows to make judgment calls—such as customer classification or document triage—directly in Logic Apps, leveraging built-in AI services. Developers can easily integrate these decision points into automated processes, simplifying complex business logic and reducing manual intervention.

- Target audience affected  
Developers and IT professionals who build, manage, or automate workflows using Azure Logic Apps, especially those needing AI-driven decision-making in business processes.

- Important notes  
This is a public preview feature, so it may not be suitable for production workloads yet. Users should monitor for updates and provide feedback to Microsoft. Integration is designed to be low-code, making it accessible for a wide range of technical users. No need to deploy or manage AI models, reducing operational overhead.  
For more details, visit: https://azure.microsoft.com/updates?id=580539

**Details**:

**Azure Update Report: Public Preview – Decision Actions in Azure Logic Apps Automation**

**Background and Purpose of the Update**  
Azure Logic Apps Automation is a cloud-based service designed for automating workflows and integrating applications, data, and services. Many business processes require automated decision-making, such as classifying customer requests or determining workflow branches based on input data. Traditionally, implementing such logic required manual rule definition or custom AI model deployment and management. The introduction of Decision actions addresses this gap by enabling developers to automate business decisions using AI, without the overhead of deploying or managing AI models.

**Specific Features and Detailed Changes**  
The update introduces Decision actions as a new capability within Azure Logic Apps Automation, now available in public preview. Decision actions allow developers to incorporate AI-powered decision-making directly into their Logic Apps workflows. This feature abstracts the complexity of AI model management, providing a simplified interface for automating business judgments. Developers can use Decision actions to classify inputs, route requests, or trigger conditional logic based on AI-driven outcomes, all within the Logic Apps designer.

**Technical Mechanisms and Implementation Methods**  
Decision actions leverage Azure’s built-in AI capabilities, enabling workflow automation that includes intelligent decision points. The technical implementation is integrated within the Logic Apps workflow designer, where users can add Decision actions as steps in their automation flows. These actions utilize pre-configured AI models managed by Azure, eliminating the need for manual model deployment, training, or maintenance. The Decision action receives input data, processes it through Azure’s AI infrastructure, and returns a decision or classification, which can then be used to drive subsequent workflow steps.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Automated classification of customer requests (e.g., routing support tickets based on content).
- Intelligent branching in business workflows (e.g., approving or rejecting transactions based on AI evaluation).
- Conditional routing of documents or data based on AI-driven categorization.
- Automating repetitive judgment calls in HR, finance, or operations workflows.

These scenarios benefit from reduced manual intervention and improved process efficiency, as AI-driven decisions can be made in real-time within automated workflows.

**Important Considerations and Limitations**  
As this feature is in public preview, it is intended for evaluation and testing purposes rather than production workloads. Users should be aware of potential limitations in model accuracy, feature completeness, and support. The Decision actions rely on Azure-managed AI models, so customization or fine-tuning of the underlying models may not be available. Additionally, preview features may be subject to changes or deprecation as Azure gathers feedback and iterates on the implementation.

**Integration with Related Azure Services**  
Decision actions are natively integrated into Azure Logic Apps Automation, enabling seamless workflow automation. They leverage Azure’s AI infrastructure, potentially including services such as Azure Cognitive Services for decision-making. Logic Apps can also connect to other Azure services (e.g., Azure Functions, Azure Data Lake, Azure Service Bus), allowing Decision actions to be part of broader enterprise automation and integration scenarios.

**Summary Sentence**  
Decision actions in Azure Logic Apps Automation, now in public preview, enable developers to automate business decisions using Azure-managed AI models directly within workflow automation, streamlining judgment-based processes without the need for custom model deployment or management.

---

### 68. Public Preview: Next-generation elastic architecture for Azure Application Gateway v2

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Next-generation elastic architecture for Azure Application Gateway v2](https://azure.microsoft.com/updates?id=580428)

**Update ID**: 580428
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Application Gateway v2 now offers a next-generation elastic architecture, available in public preview.

- Key changes or new features  
The new elastic architecture is designed to handle demanding workloads and dynamic traffic patterns more efficiently. It significantly reduces provisioning time (up to 50%) and autoscaling time (up to 70%) compared to previous versions. This enables faster scaling and improved responsiveness for applications experiencing variable or high traffic. The update also enhances the overall reliability and performance of Application Gateway v2.

- Target audience affected  
Developers and IT professionals managing web applications, APIs, or services using Azure Application Gateway v2, especially those requiring rapid scaling and high availability.

- Important notes if any  
The elastic architecture is currently in public preview, so production use should be approached with caution. Users should review documentation for compatibility and limitations during the preview phase. Early adopters can provide feedback to help refine the feature before general availability.

For more details, visit the official Azure Update: [Public Preview: Next-generation elastic architecture for Azure Application Gateway v2](https://azure.microsoft.com/updates?id=580428).

**Details**:

**Azure Update Report: Public Preview – Next-generation Elastic Architecture for Azure Application Gateway v2**

---

**Background and Purpose of the Update**  
The Azure Application Gateway v2 is a managed, scalable web traffic load balancer designed for high-performance and secure application delivery. The introduction of a next-generation elastic architecture addresses the increasing demands of modern workloads and dynamic traffic patterns. The primary purpose of this update is to enhance the agility and efficiency of Application Gateway v2 by significantly reducing provisioning and autoscaling times, thereby improving responsiveness to workload changes.

**Specific Features and Detailed Changes**  
The new elastic architecture offers two key improvements:

1. **Reduced Provisioning Time:**  
   Provisioning time is decreased by up to 50%. This means that when deploying a new Application Gateway v2 instance, the setup process completes much faster, enabling quicker onboarding and deployment of applications.

2. **Accelerated Autoscaling:**  
   Autoscaling time is reduced by up to 70%. When traffic increases or decreases, the gateway can scale its resources more rapidly, ensuring optimal performance and cost efficiency during traffic spikes or drops.

These enhancements are specifically designed for demanding workloads and environments where traffic patterns are highly variable.

**Technical Mechanisms and Implementation Methods**  
While the detailed internal mechanisms are not disclosed in the update, the improvements are realized through architectural changes in the underlying infrastructure of Application Gateway v2. The elastic architecture likely leverages advanced orchestration and resource management techniques to optimize the allocation and scaling of gateway instances. This results in faster provisioning and autoscaling operations, minimizing latency and downtime during scaling events.

**Use Cases and Application Scenarios**  
The next-generation elastic architecture is particularly beneficial in scenarios such as:

- **Large-scale Web Applications:**  
  Applications with unpredictable or highly variable traffic patterns can benefit from faster scaling and provisioning, ensuring consistent performance and availability.

- **DevOps and CI/CD Pipelines:**  
  Rapid provisioning enables quicker testing and deployment cycles, supporting agile development practices.

- **Seasonal or Event-driven Workloads:**  
  Businesses experiencing periodic traffic surges (e.g., retail during sales events) can leverage the improved autoscaling to maintain service levels without over-provisioning.

**Important Considerations and Limitations**  
As this feature is in public preview, it is intended for testing and evaluation purposes. Production workloads should be approached with caution, as preview features may not offer full support or stability. Users should monitor the Azure update page for further announcements regarding general availability and additional details.

**Integration with Related Azure Services**  
Azure Application Gateway v2 integrates seamlessly with other Azure services, such as Azure Web Apps, Azure Kubernetes Service (AKS), and Azure Virtual Machines. The improved elastic architecture enhances these integrations by enabling faster provisioning and scaling, which is critical for services that rely on Application Gateway for secure and scalable traffic management.

---

**Summary Sentence:**  
The public preview of the next-generation elastic architecture for Azure Application Gateway v2 delivers substantial improvements in provisioning and autoscaling times, enabling faster, more responsive deployment and scaling for demanding and dynamic workloads.

---

### 69. Public Preview: Advanced load balancing in Azure Application Gateway

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Advanced load balancing in Azure Application Gateway](https://azure.microsoft.com/updates?id=580423)

**Update ID**: 580423
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Application Gateway now offers advanced load balancing features in public preview.

- Key changes or new features  
The update introduces enhanced traffic distribution controls, allowing for more granular management of how requests are routed to backend servers. This includes new server-level load balancing options, which help optimize performance for diverse workloads such as AI applications and traditional web traffic. Developers and IT professionals can now fine-tune load balancing policies based on backend capabilities and workload requirements, improving reliability and scalability.

- Target audience affected  
This update is relevant for developers, IT professionals, and cloud architects managing web applications, APIs, or AI workloads on Azure Application Gateway. Teams looking to optimize backend resource utilization or support complex traffic patterns will benefit from these new features.

- Important notes  
The advanced load balancing features are currently in public preview, so production use should be approached with caution. Feedback is encouraged to help refine the functionality before general availability. Existing Application Gateway deployments can leverage these features to improve traffic management without major architectural changes.

For more details, visit the official Azure Update: [Public Preview: Advanced load balancing in Azure Application Gateway](https://azure.microsoft.com/updates?id=580423).

**Details**:

**Azure Update Report: Public Preview of Advanced Load Balancing in Azure Application Gateway**

**Background and Purpose of the Update**  
Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. The public preview of advanced load balancing aims to provide IT professionals with enhanced control over traffic distribution across backend pools, supporting diverse workloads such as AI applications and web traffic. This update addresses the need for more granular and flexible load balancing strategies to optimize performance and reliability for modern, heterogeneous application architectures.

**Specific Features and Detailed Changes**  
The advanced load balancing feature introduces new server-level controls within Azure Application Gateway. These controls allow administrators to fine-tune how incoming traffic is distributed among backend servers. This is particularly beneficial for workloads with varying resource requirements and performance characteristics, such as AI inference services and traditional web applications. The update expands the configuration options beyond the standard round-robin or least connections algorithms, enabling more sophisticated load balancing strategies tailored to specific backend needs.

**Technical Mechanisms and Implementation Methods**  
With the advanced load balancing capabilities, Azure Application Gateway now supports more detailed traffic distribution mechanisms. Administrators can configure server-level settings to influence how the gateway routes requests to backend pools. These settings may include custom weighting, health probe enhancements, and advanced routing logic, allowing for differentiated handling of traffic based on server capacity, workload type, or other criteria. The implementation leverages Azure’s scalable infrastructure, ensuring that these advanced configurations are applied consistently and reliably across distributed environments.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations running mixed workloads behind Application Gateway. For example, AI applications often require specialized load balancing to account for GPU resources or inference latency, while web applications may benefit from traditional load balancing strategies. Advanced load balancing enables IT teams to optimize traffic flow for each workload type, improving overall application performance and user experience. It is also useful in multi-tenant environments, where different backend pools may serve distinct customer segments or application tiers.

**Important Considerations and Limitations**  
As this feature is in public preview, it is recommended for testing and evaluation purposes rather than production use. IT professionals should be aware of potential limitations in feature stability, support, and documentation during the preview phase. Additionally, advanced load balancing configurations may introduce complexity in backend management, requiring careful planning and monitoring to ensure optimal operation. Compatibility with existing Application Gateway features and integrations should be validated before deployment.

**Integration with Related Azure Services**  
Advanced load balancing in Application Gateway integrates seamlessly with other Azure services, such as Azure Virtual Machines, Azure Kubernetes Service (AKS), and Azure Functions, which can serve as backend targets. It also complements Azure Front Door for global load balancing and traffic management. The enhanced controls can be used in conjunction with Application Gateway’s existing security features, including Web Application Firewall (WAF), to provide both optimized traffic distribution and robust protection.

**Summary Sentence**  
The public preview of advanced load balancing in Azure Application Gateway offers IT professionals enhanced server-level traffic distribution controls, enabling optimized handling of diverse workloads such as AI and web applications, with expanded configuration options and seamless integration with Azure’s backend services.

---

### 70. Public Preview: Centralized user authentication + JWT validation for Azure Application Gateway

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Centralized user authentication + JWT validation for Azure Application Gateway](https://azure.microsoft.com/updates?id=580418)

**Update ID**: 580418
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Application Gateway now offers centralized user authentication and enhanced JWT validation in public preview.

- Key changes or new features  
Application Gateway can now authenticate users using OpenID Connect before forwarding traffic to backend services. This enables centralized authentication at the gateway layer, reducing the need for individual backend applications to manage user sign-in. The update also improves JWT validation, allowing Application Gateway to validate tokens and enforce authentication policies more efficiently.

- Target audience affected  
Developers and IT professionals managing web applications, APIs, or microservices behind Azure Application Gateway. Teams seeking to simplify authentication workflows and improve security at the gateway level.

- Important notes  
This feature is currently in public preview and may not be suitable for production workloads yet. Centralized authentication can help reduce complexity and improve security posture by offloading authentication from backend services. Integration with OpenID Connect supports modern identity providers. Review documentation for configuration details and limitations before implementation.

**Details**:

**Azure Update Report: Public Preview – Centralized User Authentication + JWT Validation for Azure Application Gateway**

**Background and Purpose of the Update**  
Azure Application Gateway is a web traffic load balancer that enables secure and efficient routing of HTTP(S) traffic. Traditionally, authentication and JWT (JSON Web Token) validation were handled by backend applications, requiring each service to implement its own authentication logic. The purpose of this update is to introduce centralized user authentication and enhanced JWT validation directly within Application Gateway, streamlining authentication workflows and improving security posture by offloading these tasks from backend services.

**Specific Features and Detailed Changes**  
This public preview introduces two key features:
1. **Centralized User Authentication**: Application Gateway now supports user authentication via OpenID Connect (OIDC). This means the gateway can sign users in before forwarding traffic to backend applications, acting as an authentication proxy.
2. **Updated JWT Validation Experience**: The JWT validation process has been enhanced, allowing Application Gateway to validate JWTs as part of the authentication workflow. This ensures that only requests with valid tokens are forwarded to backend services.

These features are accessible through new configuration options in Application Gateway, enabling administrators to define authentication requirements and validation parameters.

**Technical Mechanisms and Implementation Methods**  
- **OpenID Connect Authentication**: Application Gateway integrates with OIDC providers. When a user requests access, the gateway initiates an OIDC authentication flow, redirecting the user to the identity provider and obtaining tokens upon successful authentication.
- **JWT Validation**: After authentication, Application Gateway validates the JWT using parameters such as issuer, audience, and expiration. This is performed at the gateway layer, preventing unauthorized requests from reaching backend applications.
- **Configuration**: Administrators configure authentication and validation settings via Azure portal, ARM templates, or CLI, specifying OIDC endpoints, client IDs, and JWT validation rules.

**Use Cases and Application Scenarios**  
- **Centralized Security Enforcement**: Organizations can enforce consistent authentication policies across multiple backend services without modifying application code.
- **Microservices Architectures**: Simplifies authentication in environments with numerous backend APIs, reducing duplication and potential security gaps.
- **Zero Trust Implementations**: Supports zero trust principles by validating user identity and token integrity at the perimeter, before any traffic reaches internal resources.

**Important Considerations and Limitations**  
- **Public Preview**: Features are in public preview and may not be suitable for production workloads. Stability, performance, and support limitations may apply.
- **Supported Protocols**: Only OpenID Connect is supported for authentication in this preview. Other protocols (e.g., SAML, OAuth2) are not mentioned.
- **Configuration Complexity**: Proper configuration of OIDC and JWT validation parameters is critical. Misconfiguration can lead to authentication failures or security vulnerabilities.
- **Integration with Existing Workflows**: Existing backend authentication logic may need to be adjusted or disabled to avoid redundant authentication.

**Integration with Related Azure Services**  
- **Azure Active Directory (AAD)**: Can be used as an OIDC provider for Application Gateway authentication.
- **Azure Application Gateway WAF**: Works alongside Web Application Firewall features, providing layered security.
- **Azure Monitor and Logging**: Authentication and validation events can be logged and monitored for auditing and troubleshooting.

**Summary Sentence**  
The public preview of centralized user authentication and updated JWT validation for Azure Application Gateway enables organizations to enforce authentication and token validation at the gateway layer using OpenID Connect, streamlining security and reducing backend complexity.

---

### 71. Public Preview: Session-based authentication for Azure Blob and Data Lake Storage

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Session-based authentication for Azure Blob and Data Lake Storage](https://azure.microsoft.com/updates?id=580306)

**Update ID**: 580306
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Blob Storage, Microsoft Ignite, Security, Feature

**Summary**:

- What was updated  
Azure Blob and Data Lake Storage now support session-based authentication in public preview.

- Key changes or new features  
Session-based authentication enables applications and AI agents to authenticate once and establish a session, reducing the overhead of per-request authentication and authorization. This approach maintains existing security controls while improving performance, especially for workloads that require frequent data access.

- Target audience affected  
Developers building applications or AI solutions that interact with Azure Blob or Data Lake Storage, and IT professionals managing storage access and performance.

- Important notes  
Session-based authentication is currently in public preview and may not be suitable for production workloads. It is designed to optimize authentication for scenarios with high-frequency access patterns, such as AI agents or batch processing jobs. Existing security and compliance requirements are preserved. Users should review documentation for integration details and limitations before adoption.

For more information, visit the official Azure Update: https://azure.microsoft.com/updates?id=580306

**Details**:

**Azure Update Report**

**Title:** Public Preview: Session-based authentication for Azure Blob and Data Lake Storage  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=580306)

---

**Background and Purpose of the Update:**  
Azure Blob and Data Lake Storage are foundational services for storing unstructured and structured data in Azure. Traditionally, authentication and authorization for each request to these storage services required per-request validation, which could introduce latency and computational overhead, especially for AI agents and applications that generate high-frequency access patterns. The purpose of this update is to optimize authentication performance by introducing session-based authentication, thereby reducing the time spent on authentication and authorization for each request while maintaining security controls.

---

**Specific Features and Detailed Changes:**  
The public preview introduces session-based authentication for Azure Blob and Data Lake Storage. With this feature, authenticated sessions are established, allowing multiple subsequent requests to reuse the session context instead of performing full authentication and authorization on every individual request. This change is particularly beneficial for workloads that require repeated access to storage resources, as it minimizes redundant authentication operations.

---

**Technical Mechanisms and Implementation Methods:**  
Session-based authentication works by establishing a session after an initial authentication and authorization process. The session context is then used for subsequent requests, reducing the need for repeated authentication checks. The implementation preserves existing security controls, ensuring that session-based access does not compromise organizational security policies. The technical mechanism likely involves issuing a session token or context that is valid for a defined period or until explicitly revoked, but the update does not specify the exact token format or lifecycle management. The session context is managed by Azure Storage, and applications or AI agents must be updated to leverage session-based authentication in their access patterns.

---

**Use Cases and Application Scenarios:**  
- **AI Agents:** AI workloads that require frequent, repeated access to Blob or Data Lake Storage benefit from reduced authentication latency, improving throughput and responsiveness.
- **High-frequency Applications:** Applications that perform batch processing, streaming analytics, or iterative data access can leverage session-based authentication to optimize performance.
- **Data Pipelines:** ETL and data ingestion pipelines that interact with storage services in rapid succession can reduce overhead and improve efficiency.

---

**Important Considerations and Limitations:**  
- **Security Controls:** Session-based authentication is designed to maintain existing security controls, but organizations should review session management policies to ensure compliance with internal and regulatory requirements.
- **Preview Status:** The feature is in public preview, meaning it is not recommended for production workloads until general availability and may be subject to changes.
- **Integration Requirements:** Applications and agents must be updated to utilize session-based authentication; legacy clients may not benefit from this feature without modification.
- **Session Lifecycle:** The update does not specify session expiration, renewal, or revocation mechanisms, so IT professionals should monitor Azure documentation for further details.

---

**Integration with Related Azure Services:**  
Session-based authentication is directly integrated with Azure Blob and Data Lake Storage. It can be used in conjunction with other Azure security features, such as role-based access control (RBAC) and managed identities, to ensure secure and efficient access. The update does not mention integration with other Azure services, but it is expected to enhance performance for any service or application interacting with Blob or Data Lake Storage.

---

**Summary Sentence:**  
Session-based authentication for Azure Blob and Data Lake Storage, now in public preview, streamlines per-request authentication and authorization for AI agents and applications, improving performance while maintaining security controls.

---

### 72. Generally Available: Azure Monitor Health Models 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Monitor Health Models ](https://azure.microsoft.com/updates?id=580261)

**Update ID**: 580261
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Monitor Health Models is now Generally Available.

- Key changes or new features  
Azure Monitor Health Models enables users to define and operationalize workload health as a first-class construct within Azure Monitor. It allows aggregation of signals from metrics, logs, and dependencies into a unified health model. This provides a holistic view of workload health, facilitating easier detection of issues and improved monitoring across distributed resources. The feature supports custom health definitions, enabling tailored monitoring scenarios and automated health assessments.

- Target audience affected  
Developers and IT professionals responsible for monitoring, maintaining, and troubleshooting Azure workloads and applications. Teams managing distributed systems and requiring comprehensive health visibility will benefit most.

- Important notes if any  
Health Models can be integrated into existing Azure Monitor workflows and dashboards. Custom health models can be created to match specific workload requirements. This update enhances operational efficiency by enabling proactive health monitoring and faster incident response. For implementation details and API usage, refer to the official documentation: [Azure Monitor Health Models](https://azure.microsoft.com/updates?id=580261).

**Details**:

**Azure Monitor Health Models: Comprehensive Technical Explanation**

**Background and Purpose of the Update**  
Azure Monitor Health Models are now Generally Available, marking a significant advancement in how workload health is defined and operationalized within Azure Monitor. The purpose of this update is to provide IT professionals with a unified, first-class construct for workload health by aggregating diverse telemetry signals—such as metrics, logs, and dependencies—into a single health model. This approach addresses the complexity of monitoring modern distributed workloads, enabling more holistic and actionable health assessments.

**Specific Features and Detailed Changes**  
With this release, users can build custom Health Models in Azure Monitor. These models allow you to define health states based on aggregated signals from various sources:
- **Metrics:** Quantitative performance indicators from Azure resources.
- **Logs:** Diagnostic and operational logs that capture events and traces.
- **Dependencies:** Relationships and interactions between services and resources.

The Health Model serves as a central point for workload health, moving beyond traditional resource-centric monitoring. It enables operationalization of health as a first-class concept, allowing for more nuanced and workload-specific health definitions.

**Technical Mechanisms and Implementation Methods**  
Azure Monitor Health Models aggregate signals from metrics, logs, and dependencies using configurable rules and logic. IT professionals can specify which signals to include and how to interpret them, such as setting thresholds for metrics, defining log patterns, or mapping dependency health. The model synthesizes these inputs into a single health state, which can be queried, visualized, and acted upon. Implementation typically involves:
- Defining the workload scope and relevant telemetry sources.
- Configuring aggregation logic and health state criteria.
- Integrating the Health Model with alerting and automation workflows.

Health Models are managed through Azure Monitor’s interface, allowing for versioning, updates, and integration with other monitoring features.

**Use Cases and Application Scenarios**  
- **Complex Workload Monitoring:** Aggregate signals across microservices, databases, and APIs to assess overall application health.
- **Custom Health Definitions:** Tailor health models to business-specific SLAs or operational requirements.
- **Incident Response:** Use unified health states to trigger alerts and automate remediation actions.
- **Reporting:** Generate consolidated health reports for stakeholders, improving transparency and operational insight.

**Important Considerations and Limitations**  
- Health Models require careful configuration to ensure relevant signals are aggregated and interpreted correctly.
- The effectiveness of the Health Model depends on the quality and granularity of underlying telemetry data.
- There may be limitations in aggregating signals from non-Azure resources or unsupported telemetry sources.
- Changes to Health Model definitions may impact alerting and operational workflows, requiring thorough testing.

**Integration with Related Azure Services**  
Azure Monitor Health Models integrate seamlessly with other Azure Monitor capabilities, such as:
- **Alerts:** Health states can trigger alerts, enabling proactive incident management.
- **Dashboards:** Health Models can be visualized in Azure Monitor dashboards for real-time monitoring.
- **Log Analytics:** Health Model signals can be analyzed alongside other telemetry in Log Analytics.
- **Automation:** Health state changes can initiate Azure Logic Apps or Automation Runbooks for remediation.

**Summary Sentence**  
Azure Monitor Health Models are now generally available, enabling IT professionals to define and operationalize workload health as a unified construct by aggregating signals from metrics, logs, and dependencies into a single, actionable health model within Azure Monitor.

---

### 73. Public Preview: Azure Monitor traces and Trace Analytics

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Monitor traces and Trace Analytics](https://azure.microsoft.com/updates?id=580184)

**Update ID**: 580184
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
Azure Monitor now offers a public preview of enhanced trace analytics capabilities within Application Insights, introducing Azure Monitor traces and Trace Analytics.

**Key changes or new features:**  
- Dedicated trace data type in Azure Monitor, enabling advanced distributed tracing.
- Ability to analyze and compare thousands of traces efficiently.
- Tools to isolate specific transactions and drill down from trends to root cause.
- Enhanced visualization and querying for trace data, supporting deeper diagnostics and performance monitoring.
- Improved integration with Application Insights, allowing for seamless trace collection and analysis.

**Target audience affected:**  
- Developers building distributed applications and microservices on Azure.
- IT professionals and DevOps teams responsible for application monitoring, diagnostics, and troubleshooting.

**Important notes:**  
- This feature is currently in public preview; production use should be approached with caution.
- Existing Application Insights users can leverage these new trace analytics capabilities to improve observability and root cause analysis.
- Documentation and API support may evolve as the feature moves toward general availability.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=580184).

**Details**:

**Azure Update Report: Public Preview – Azure Monitor Traces and Trace Analytics**

**Background and Purpose of the Update:**  
The introduction of Azure Monitor traces and Trace Analytics in public preview addresses the growing need for advanced distributed tracing capabilities within Azure Monitor Application Insights. As modern applications increasingly rely on microservices and distributed architectures, tracing individual transactions and understanding their flow across services is critical for diagnosing issues, optimizing performance, and ensuring reliability. This update aims to empower IT professionals with tools to analyze and compare large volumes of trace data, facilitating deeper insights into application behavior and enabling rapid identification of root causes.

**Specific Features and Detailed Changes:**  
- **Dedicated Trace Analysis:** Azure Monitor traces (preview) provides a specialized environment for analyzing trace data, distinct from traditional metrics and logs.  
- **Bulk Trace Comparison:** Users can now analyze and compare thousands of traces simultaneously, allowing for trend identification and anomaly detection across large datasets.  
- **Transaction Isolation:** The update enables isolation of specific transactions that are relevant for investigation, helping users focus on critical paths and performance bottlenecks.  
- **Advanced Distributed Tracing:** Enhanced tracing capabilities allow users to follow requests as they traverse multiple services and components, supporting comprehensive end-to-end visibility.  
- **Root Cause Analysis:** The new tools facilitate moving from high-level trends to detailed root cause analysis, streamlining the troubleshooting process.

**Technical Mechanisms and Implementation Methods:**  
Azure Monitor traces leverage Application Insights’ distributed tracing framework, which collects telemetry from instrumented applications. Trace data is ingested, stored, and indexed to support rapid querying and analytics. The preview introduces a dedicated trace analytics interface, optimized for handling large volumes of trace data and providing advanced filtering, comparison, and visualization tools. Integration with Application Insights SDKs ensures seamless collection of trace information from supported platforms and languages.

**Use Cases and Application Scenarios:**  
- **Performance Optimization:** Engineers can identify slow transactions and analyze their trace paths to optimize application performance.  
- **Incident Investigation:** During outages or anomalies, IT teams can isolate affected transactions and trace their journey across services to pinpoint failure points.  
- **Microservices Monitoring:** Distributed tracing is essential for microservices architectures, enabling correlation of requests across service boundaries.  
- **Trend Analysis:** Bulk comparison of traces helps detect emerging patterns, regressions, or improvements over time.

**Important Considerations and Limitations:**  
- **Preview Status:** The feature is currently in public preview, which may imply limited support, evolving functionality, and possible changes before general availability.  
- **Data Volume:** Analyzing thousands of traces requires careful management of data retention and storage costs, as well as attention to performance impacts on query operations.  
- **Instrumentation Requirements:** Applications must be properly instrumented with Application Insights SDKs to generate trace data compatible with the new analytics features.

**Integration with Related Azure Services:**  
Azure Monitor traces and Trace Analytics are tightly integrated with Application Insights, leveraging its telemetry collection and distributed tracing capabilities. The update complements Azure Monitor’s broader observability suite, including metrics, logs, and alerts, enabling holistic monitoring and diagnostics. Trace analytics can be used alongside Log Analytics for unified troubleshooting workflows and can be extended to other Azure services that emit trace telemetry.

**Summary Sentence:**  
Azure Monitor traces and Trace Analytics (public preview) provide IT professionals with advanced tools for analyzing, comparing, and isolating distributed traces within Application Insights, enabling efficient trend identification and root cause analysis across complex application environments.

---

### 74. Generally Available: Azure Red Hat OpenShift with hosted control planes

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift with hosted control planes](https://azure.microsoft.com/updates?id=580136)

**Update ID**: 580136
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Microsoft Ignite, Open Source, Feature

**Summary**:

- What was updated  
Azure Red Hat OpenShift now offers a Generally Available (GA) deployment option with hosted control planes.

- Key changes or new features  
The new hosted control plane model separates the OpenShift control plane from the worker nodes running customer applications. The control plane is managed and hosted by Azure, reducing operational overhead and improving scalability. This architecture enables faster cluster provisioning, simplified upgrades, and enhanced security by isolating the control plane from customer workloads. Customers can also achieve better resource utilization and cost efficiency, as only worker nodes are billed directly.

- Target audience affected  
Developers and IT professionals managing containerized workloads on Azure Red Hat OpenShift, especially those seeking improved scalability, operational simplicity, and security.

- Important notes  
Existing Azure Red Hat OpenShift customers can choose to migrate to the hosted control plane model for improved efficiency. The hosted control plane option is recommended for production workloads requiring high availability and reduced management complexity. Integration with Azure services and compliance standards remains unchanged. For more details, refer to the official Azure Update announcement.

**Details**:

**Azure Update Report: Azure Red Hat OpenShift with Hosted Control Planes (General Availability)**

**Background and Purpose of the Update**  
Microsoft Azure Red Hat OpenShift (ARO) is a managed Kubernetes platform that combines Azure’s infrastructure with Red Hat OpenShift’s enterprise-grade container orchestration. The general availability of Azure Red Hat OpenShift with hosted control planes introduces a new deployment architecture. The purpose of this update is to enhance operational flexibility and resource isolation by separating the OpenShift control plane from the worker nodes that execute customer workloads.

**Specific Features and Detailed Changes**  
The key feature in this update is the hosted control plane model. In this architecture, the OpenShift control plane components (such as API server, scheduler, and controller manager) are provisioned and managed independently from the worker nodes. Worker nodes, which run application containers, are decoupled from the control plane, allowing for improved scalability and resource allocation. This separation enables customers to focus on managing their application workloads while Azure and Red Hat jointly manage the control plane infrastructure.

**Technical Mechanisms and Implementation Methods**  
Azure Red Hat OpenShift with hosted control planes leverages Azure’s managed services to provision and operate the OpenShift control plane in a dedicated, isolated environment. The control plane is hosted and maintained by Azure and Red Hat, ensuring high availability, security, and compliance. Worker nodes are provisioned in the customer’s Azure subscription, allowing for granular control over scaling, networking, and security policies. Communication between the control plane and worker nodes is managed through secure channels, ensuring integrity and confidentiality of cluster operations.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations seeking multi-tenant architectures, resource isolation, and simplified cluster management. Typical scenarios include:  
- Enterprises deploying multiple OpenShift clusters with centralized control plane management for operational consistency.  
- Workloads requiring strict separation between management and application resources, such as regulated industries (finance, healthcare) with compliance requirements.  
- Customers who want to minimize operational overhead by offloading control plane management to Azure and Red Hat, while retaining full control over worker node configuration and scaling.

**Important Considerations and Limitations**  
IT professionals should note that the hosted control plane model introduces new operational boundaries. The control plane is fully managed and may not be directly accessible for customization or troubleshooting. Worker nodes remain under customer control, but integration and communication with the control plane are governed by Azure’s managed service policies. It is important to review Azure’s documentation for supported configurations, networking requirements, and any limitations regarding custom resource definitions or third-party integrations.

**Integration with Related Azure Services**  
Azure Red Hat OpenShift with hosted control planes integrates seamlessly with other Azure services, such as Azure Active Directory for identity management, Azure Monitor for logging and metrics, and Azure Policy for governance. Customers can leverage Azure networking features (VNETs, private endpoints) to secure worker node communication. The managed control plane also supports integration with Azure’s security and compliance frameworks, ensuring end-to-end protection for enterprise workloads.

**Summary Sentence**  
Azure Red Hat OpenShift with hosted control planes is now generally available, offering a managed deployment option that separates the OpenShift control plane from worker nodes, thereby enhancing scalability, operational efficiency, and resource isolation for enterprise Kubernetes workloads on Azure.

---

### 75. Generally Available: Azure AI Gateway 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure AI Gateway ](https://azure.microsoft.com/updates?id=580080)

**Update ID**: 580080
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Ignite

**Summary**:

- What was updated  
Azure AI Gateway is now generally available as a standalone, fully managed Azure service (previously the AI Gateway tier of API Management).

- Key changes or new features  
  - Provides centralized management and secure connectivity for users, applications, and agents to AI models and Machine Learning Control Plane (MCP) tools across multiple providers.  
  - Supports integration with various AI services, including Azure OpenAI, and allows routing, monitoring, and governance of AI traffic.  
  - Offers built-in authentication, authorization, and usage analytics to help platform teams control access and monitor usage.  
  - Enables developers to connect and orchestrate AI models and tools from different vendors through a unified gateway.

- Target audience affected  
  - Developers building AI-powered applications that require access to multiple AI models or providers.  
  - IT professionals and platform teams responsible for managing AI infrastructure, security, and compliance.

- Important notes if any  
  - Azure AI Gateway simplifies integration, governance, and monitoring of AI services, reducing complexity for teams managing multi-provider AI environments.  
  - Existing users of the AI Gateway tier in API Management should consider migrating to the standalone Azure AI Gateway service for enhanced features and support.  
  - For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=580080

**Details**:

**Azure Update Report: Generally Available – Azure AI Gateway**

**Background and Purpose of the Update**  
Azure AI Gateway, previously offered as the AI Gateway tier within Azure API Management, is now generally available as a standalone, fully managed Azure service. The primary purpose of this update is to provide a unified platform for securely connecting users, applications, and agents to AI models and Machine Learning Control Plane (MCP) tools across multiple providers. This transition reflects Azure’s commitment to simplifying AI integration and management, enabling platform teams to centralize and streamline access to diverse AI resources.

**Specific Features and Detailed Changes**  
With general availability, Azure AI Gateway introduces several enhancements:
- **Fully Managed Service:** Azure AI Gateway operates independently from API Management, offering a dedicated service for AI connectivity.
- **Multi-Provider Support:** The gateway facilitates connections to AI models and MCP tools from various providers, not limited to Azure-native solutions.
- **User, Application, and Agent Connectivity:** It enables secure and scalable access for different types of clients, including end users, enterprise applications, and autonomous agents.
- **Centralized Management:** Platform teams can centralize the configuration, monitoring, and governance of AI endpoints and tools, improving operational efficiency.

**Technical Mechanisms and Implementation Methods**  
Azure AI Gateway leverages Azure’s managed infrastructure to provide secure, scalable, and reliable connectivity:
- **Endpoint Abstraction:** The gateway abstracts underlying AI model endpoints, allowing clients to interact with AI resources through a unified interface.
- **Security and Access Control:** Built-in authentication and authorization mechanisms ensure secure access to AI models and MCP tools.
- **Traffic Routing and Load Balancing:** The gateway manages traffic routing, balancing requests across multiple AI endpoints and providers.
- **Monitoring and Logging:** Integrated monitoring and logging capabilities enable platform teams to track usage, performance, and access patterns.

**Use Cases and Application Scenarios**  
Typical scenarios for Azure AI Gateway include:
- **Enterprise AI Integration:** Organizations can connect internal applications to AI models hosted across different cloud providers, simplifying integration and management.
- **Multi-Agent Systems:** Autonomous agents can securely access AI models and MCP tools via the gateway, supporting complex AI-driven workflows.
- **Cross-Provider AI Management:** Teams can manage and monitor AI resources from multiple providers in a centralized manner, reducing operational complexity.

**Important Considerations and Limitations**  
- **Provider Compatibility:** While the gateway supports multiple providers, compatibility depends on the providers’ API and MCP tool interfaces.
- **Security Configuration:** Proper configuration of authentication and authorization policies is critical to ensure secure access.
- **Service Limits:** As a managed service, Azure AI Gateway may have usage limits or quotas; teams should review documentation for specifics.
- **Migration from API Management:** Existing users of the AI Gateway tier in API Management should plan for migration to the standalone service to leverage new features.

**Integration with Related Azure Services**  
Azure AI Gateway integrates seamlessly with other Azure services:
- **Azure Active Directory:** For identity and access management.
- **Azure Monitor:** For logging and monitoring gateway activity.
- **Azure API Management:** While now standalone, it can complement API Management for broader API lifecycle management.
- **Azure Machine Learning:** For connecting to Azure-hosted AI models and MCP tools.

**Summary Sentence**  
Azure AI Gateway is now generally available as a fully managed Azure service, providing centralized, secure, and scalable connectivity to AI models and MCP tools across multiple providers for users, applications, and agents.

---

### 76. Generally Available: Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway ](https://azure.microsoft.com/updates?id=580055)

**Update ID**: 580055
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway is now generally available.

- Key changes or new features  
Organizations can now centrally manage and govern Microsoft Agent 365 AI agents and MCP tools using Azure API Management and Azure AI Gateway. This integration allows enforcement of security and access policies at runtime, providing unified control over API traffic, authentication, and authorization. Developers can leverage API Management to expose, secure, and monitor AI agent endpoints, while IT professionals gain enhanced visibility and governance over agent interactions and data flows.

- Target audience affected  
Developers building AI-powered solutions with Microsoft Agent 365, IT professionals responsible for API security and governance, and organizations deploying MCP tools and AI agents at scale.

- Important notes if any  
This integration streamlines the deployment and management of AI agents, ensuring compliance with organizational security standards. It enables consistent policy enforcement across AI and MCP endpoints, supporting both operational efficiency and regulatory requirements. Existing Azure API Management users can extend their governance to Agent 365 with minimal configuration changes.

**Details**:

**Comprehensive Technical Explanation: Microsoft Agent 365 Integration with Azure API Management and Azure AI Gateway (Generally Available)**

**Background and Purpose of the Update:**  
This update announces the general availability of the integration between Microsoft Agent 365 and Azure API Management, as well as Azure AI Gateway. The primary purpose is to enable organizations to centrally manage and govern AI agents and Microsoft Cloud Platform (MCP) tools. By leveraging Azure API Management, enterprises can enforce security and access policies at runtime, ensuring robust control and compliance over AI-driven interactions and MCP tool usage.

**Specific Features and Detailed Changes:**  
- **Centralized Governance:** Organizations can now use Azure API Management to centrally govern Microsoft Agent 365 AI agents and MCP tools. This includes unified policy enforcement, monitoring, and analytics.
- **Security and Access Policies:** The integration allows runtime enforcement of security and access policies, such as authentication, authorization, throttling, and logging, directly through Azure API Management.
- **Azure AI Gateway Support:** The update extends support to Azure AI Gateway, facilitating secure and scalable access to AI services and agents.
- **General Availability:** The features are now production-ready and supported for enterprise workloads, moving beyond preview or limited release.

**Technical Mechanisms and Implementation Methods:**  
- **API Management Layer:** Microsoft Agent 365 endpoints and MCP tool APIs are exposed via Azure API Management, which acts as a gateway and policy enforcement point.
- **Policy Enforcement:** Runtime policies (e.g., OAuth, JWT validation, IP filtering) are applied to API requests, ensuring only authorized and compliant interactions with AI agents and MCP tools.
- **Integration Workflow:** Organizations configure Agent 365 and MCP tool APIs within Azure API Management, define policies, and route requests through Azure AI Gateway for additional AI-specific controls.
- **Monitoring and Analytics:** Azure API Management provides built-in telemetry, logging, and analytics for all interactions, aiding in operational oversight and troubleshooting.

**Use Cases and Application Scenarios:**  
- **Enterprise AI Governance:** Large organizations deploying multiple AI agents via Microsoft Agent 365 can centrally manage access, monitor usage, and enforce compliance policies.
- **Secure MCP Tool Integration:** Enterprises integrating MCP tools with internal or external applications can ensure secure, policy-driven access via Azure API Management.
- **Regulatory Compliance:** Organizations subject to regulatory requirements can leverage runtime policy enforcement to meet security and audit standards.
- **Scalable AI Service Delivery:** Azure AI Gateway enables scalable and secure delivery of AI services, suitable for high-volume, mission-critical workloads.

**Important Considerations and Limitations:**  
- **Policy Configuration:** Proper configuration of Azure API Management policies is essential to ensure desired security and access controls.
- **Performance Overhead:** Introducing API Management and AI Gateway layers may add latency; performance testing is recommended for high-throughput scenarios.
- **Supported Features:** Only features explicitly supported by Azure API Management and Azure AI Gateway are available; custom or unsupported scenarios may require additional development.
- **Runtime Enforcement:** All security and access policies are enforced at runtime, requiring careful monitoring and maintenance to avoid disruptions.

**Integration with Related Azure Services:**  
- **Azure API Management:** Acts as the central point for API governance, policy enforcement, and analytics.
- **Azure AI Gateway:** Provides secure, scalable access to AI agents and services, complementing API Management.
- **Microsoft Agent 365:** Integrates seamlessly with Azure services for unified AI agent management.
- **MCP Tools:** Managed and governed alongside AI agents via the same Azure API Management infrastructure.

**Summary Sentence:**  
The general availability of Microsoft Agent 365 integration with Azure API Management and Azure AI Gateway empowers organizations to centrally govern AI agents and MCP tools, enforce security and access policies at runtime, and leverage Azure’s robust API management and AI gateway capabilities for secure, scalable, and compliant operations.

---

### 77. Generally Available: Azure API Management Premium v2 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure API Management Premium v2 ](https://azure.microsoft.com/updates?id=580046)

**Update ID**: 580046
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Ignite

**Summary**:

- What was updated  
Azure API Management Premium v2 is now generally available in 35 Azure regions.

- Key changes or new features  
The Premium v2 tier offers expanded regional coverage, enabling organizations to deploy and scale API workloads in more geographic locations. This update provides enhanced flexibility for global API management, supporting enterprise-grade requirements such as high availability, disaster recovery, and multi-region deployments. Developers and IT teams can leverage improved performance, scalability, and security features inherent to the Premium v2 tier.

- Target audience affected  
Developers, IT professionals, and organizations managing enterprise APIs, especially those requiring global reach, high availability, and advanced scaling capabilities.

- Important notes  
With the broader regional availability, customers can optimize API deployments closer to their users, improving latency and compliance with regional data regulations. Existing API Management users may consider upgrading to Premium v2 for enhanced features and expanded coverage. Review pricing and regional availability before migration or deployment.  

For more details, visit: https://azure.microsoft.com/updates?id=580046

**Details**:

**Azure Update Report: Generally Available - Azure API Management Premium v2**

**Background and Purpose of the Update**  
Azure API Management Premium v2 has reached general availability, now accessible in 35 Azure regions. The primary goal of this update is to provide organizations with enhanced flexibility and scalability for deploying enterprise-grade API workloads. By expanding regional coverage, Microsoft enables customers to optimize API deployments for performance, compliance, and proximity to users and backend systems.

**Specific Features and Detailed Changes**  
This update introduces Azure API Management Premium v2, which is now generally available. The most notable change is the expanded regional availability, allowing API Management instances to be provisioned in 35 Azure regions. This broad geographic reach supports global operations, disaster recovery strategies, and regional compliance requirements. The Premium tier is designed for large-scale, mission-critical API scenarios, offering advanced features such as multi-region deployment, high availability, and enhanced scalability.

**Technical Mechanisms and Implementation Methods**  
Azure API Management Premium v2 leverages Azure’s global infrastructure to provide distributed API gateways and management capabilities. Deployment in multiple regions is facilitated through the Azure portal, ARM templates, or REST APIs, allowing organizations to select regions based on latency, regulatory, or business needs. The Premium tier supports scaling out API gateways horizontally across regions, ensuring consistent performance and reliability. API Management integrates with Azure networking, security, and monitoring services to provide enterprise-grade controls and visibility.

**Use Cases and Application Scenarios**  
- **Global API Delivery:** Enterprises with users or backend systems distributed across multiple continents can deploy API Management instances closer to their consumers, reducing latency and improving user experience.
- **Disaster Recovery and High Availability:** Multi-region deployment enables robust failover and disaster recovery strategies, ensuring API availability even in the event of regional outages.
- **Compliance and Data Residency:** Organizations subject to regional data residency or compliance requirements can deploy API Management in specific Azure regions to meet regulatory obligations.
- **Enterprise Scale:** Premium v2 is suitable for scenarios requiring high throughput, advanced security, and integration with other Azure services for mission-critical applications.

**Important Considerations and Limitations**  
- **Regional Selection:** Customers must ensure that the selected Azure regions support Premium v2 and meet their business, compliance, and technical requirements.
- **Cost Implications:** The Premium tier is designed for enterprise workloads and may incur higher costs compared to lower tiers; careful planning is required to optimize resource allocation.
- **Service Limits:** While Premium v2 supports enhanced scalability, customers should review Azure API Management documentation for specific service limits and quotas.
- **Migration:** Existing API Management instances may require migration or configuration updates to leverage Premium v2 features and regional availability.

**Integration with Related Azure Services**  
Azure API Management Premium v2 integrates seamlessly with other Azure services, including Azure Functions, Logic Apps, App Services, and Azure Active Directory for authentication and authorization. It also supports integration with Azure Monitor for logging and diagnostics, Azure Key Vault for secure secrets management, and Azure Virtual Network for network isolation and security.

**Summary Sentence**  
Azure API Management Premium v2 is now generally available in 35 Azure regions, providing organizations with expanded flexibility and scalability for deploying enterprise API workloads across a broader geographic footprint.

---

### 78. Generally Available: Azure Connector Namespace

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Connector Namespace](https://azure.microsoft.com/updates?id=580041)

**Update ID**: 580041
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps, Microsoft Ignite

**Summary**:

- What was updated  
Azure Connector Namespace is now generally available.

- Key changes or new features  
Azure Connector Namespace offers a fully managed integration service, allowing developers to connect applications and AI agents to hundreds of Microsoft, SaaS, and enterprise systems. It features prebuilt, reusable connectors that simplify integration workflows and reduce development time. The service supports secure, scalable, and reliable connectivity, enabling seamless data exchange and automation across diverse platforms.

- Target audience affected  
Developers building cloud-native applications, IT professionals managing enterprise integrations, and teams deploying AI agents or automating business processes.

- Important notes if any  
The general availability means the service is production-ready and supported by Microsoft. Developers can leverage the API to access connectors for rapid integration, while IT professionals benefit from simplified management and enhanced security. Existing integration solutions can be migrated or extended using Connector Namespace for improved scalability and maintainability.  
For more information, visit the official Azure update: https://azure.microsoft.com/updates?id=580041

**Details**:

**Azure Update Report: Generally Available - Azure Connector Namespace**

**Background and Purpose of the Update**  
The Azure Connector Namespace is now generally available, marking its transition from preview to production-ready status. This update addresses the growing need for seamless integration between applications, AI agents, and a wide variety of external systems. The primary purpose is to simplify and accelerate connectivity to Microsoft services, SaaS platforms, and enterprise systems, leveraging prebuilt, reusable connectors to reduce development overhead and integration complexity.

**Specific Features and Detailed Changes**  
Azure Connector Namespace introduces a fully managed integration service. Key features include:

- **Prebuilt, Reusable Connectors:** Hundreds of connectors are available, covering Microsoft products, popular SaaS offerings, and enterprise systems.  
- **Managed Service:** The platform handles connector lifecycle, scaling, and maintenance, eliminating the need for manual infrastructure management.  
- **Unified Namespace:** Developers can organize and manage connectors within a dedicated namespace, streamlining integration workflows and governance.  
- **Developer Experience:** The service is designed for easy consumption by applications and AI agents, facilitating rapid integration without custom connector development.

**Technical Mechanisms and Implementation Methods**  
Azure Connector Namespace operates as a managed service within Azure, abstracting the complexities of connector management. Developers interact with the service via Azure APIs and SDKs, allowing applications and AI agents to invoke connectors programmatically. The namespace acts as a logical container, grouping connectors for easier access control, monitoring, and lifecycle management. The service ensures high availability, scalability, and security by leveraging Azure’s underlying infrastructure.

**Use Cases and Application Scenarios**  
Typical scenarios include:

- **Application Integration:** Connecting Azure-hosted or on-premises applications to external SaaS platforms (e.g., Salesforce, ServiceNow) using prebuilt connectors.
- **AI Agent Connectivity:** Enabling AI agents to access data or trigger actions across multiple systems without custom integration code.
- **Enterprise Automation:** Automating workflows that span Microsoft services and third-party enterprise systems, improving operational efficiency.
- **Rapid Prototyping:** Accelerating proof-of-concept development by leveraging reusable connectors instead of building integrations from scratch.

**Important Considerations and Limitations**  
IT professionals should note:

- **Connector Availability:** The service provides access to hundreds of connectors, but coverage depends on the catalog’s current offerings.
- **Managed Service Constraints:** As a fully managed platform, customization options may be limited compared to self-hosted integration solutions.
- **Namespace Governance:** Proper organization and access control within namespaces are essential for security and compliance.
- **Lifecycle Management:** While the platform handles maintenance, connector updates or deprecations may impact integration stability.

**Integration with Related Azure Services**  
Azure Connector Namespace integrates seamlessly with other Azure services:

- **Azure Logic Apps:** Can leverage connectors within a namespace for workflow automation.
- **Azure Functions:** Enables serverless applications to invoke connectors for external system interactions.
- **Azure AI Services:** Facilitates AI agent connectivity to external data sources and actions.
- **Azure API Management:** Supports secure exposure and management of connector-based APIs.

**Summary Sentence**  
Azure Connector Namespace is now generally available, offering a fully managed integration service with prebuilt, reusable connectors that enable developers to efficiently connect applications and AI agents to a wide range of Microsoft, SaaS, and enterprise systems.

---

### 79. Generally Available: Unified Model API in Azure API Management 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Unified Model API in Azure API Management ](https://azure.microsoft.com/updates?id=580036)

**Update ID**: 580036
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Mobile, Web, API Management, Microsoft Ignite

**Summary**:

- What was updated  
Azure API Management has released the Unified Model API as generally available.

- Key changes or new features  
The Unified Model API provides a standardized interface to connect applications to AI models from various providers (such as OpenAI, Azure AI, and others). Developers can now integrate multiple AI models without handling different API endpoints or custom integration logic. This simplifies application development, reduces code complexity, and streamlines maintenance when working with diverse AI services.

- Target audience affected  
Developers building AI-powered applications, IT professionals managing API integrations, and teams responsible for maintaining API gateways and application architecture.

- Important notes  
The Unified Model API enables easier scaling and switching between AI model providers, supporting rapid experimentation and deployment. Existing applications can be updated to use the new API for improved maintainability. Documentation and migration guidance are available in Azure API Management resources. This update is particularly valuable for organizations leveraging multi-model AI strategies or seeking to minimize vendor lock-in.

**Details**:

**Azure Update Report: Generally Available – Unified Model API in Azure API Management**

**Background and Purpose of the Update**  
The Unified Model API in Azure API Management addresses the complexity of integrating multiple AI models from various providers into applications. Traditionally, developers must manage disparate API interfaces, authentication schemes, and integration requirements, which increases development overhead and complicates maintenance. The purpose of this update is to provide a standardized, unified API layer that abstracts these differences, enabling seamless connectivity to AI models regardless of their source.

**Specific Features and Detailed Changes**  
With this update, Azure API Management introduces the Unified Model API, which acts as a single, consistent interface for accessing AI models from multiple providers. This eliminates the need for developers to interact with provider-specific APIs. Key features include:
- Standardized API endpoints for AI model invocation.
- Uniform request and response formats across different AI providers.
- Centralized management of authentication and authorization.
- Simplified integration workflow for adding or switching AI models.

**Technical Mechanisms and Implementation Methods**  
The Unified Model API is implemented within Azure API Management as a managed API layer. Developers configure the Unified Model API to route requests to the desired AI model provider, leveraging Azure API Management’s policy engine for transformation, authentication, and logging. The API Management service handles protocol translation, payload formatting, and security enforcement, ensuring that application code remains agnostic to provider-specific details. This abstraction is achieved through mapping policies and backend configuration within the API Management portal.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Applications requiring access to multiple AI models (e.g., language, vision, or generative models) from different vendors.
- Enterprises seeking to build AI-powered solutions without vendor lock-in or extensive rework when switching providers.
- Developers aiming to rapidly prototype or deploy AI features by leveraging a unified API surface.
- Integration of AI models into business workflows, chatbots, or analytics platforms with minimal code changes.

**Important Considerations and Limitations**  
When utilizing the Unified Model API, IT professionals should consider:
- The supported AI model providers and types may be limited to those integrated with Azure API Management.
- Performance and latency may vary depending on the underlying provider and network routing.
- Security policies and compliance requirements must be configured within API Management to ensure data protection.
- Any provider-specific features not exposed through the Unified Model API may require custom integration or direct API calls.

**Integration with Related Azure Services**  
The Unified Model API is tightly integrated with Azure API Management, enabling centralized API governance, monitoring, and analytics. It can be combined with Azure Functions, Logic Apps, and Azure Cognitive Services for orchestration and advanced workflows. Additionally, developers can leverage Azure Active Directory for authentication and Azure Monitor for tracking usage and performance metrics.

**Summary Sentence**  
Azure API Management’s Unified Model API provides a standardized interface for connecting applications to AI models from multiple providers, streamlining integration, reducing complexity, and enabling centralized management of authentication, security, and monitoring.

---

### 80. Generally Available:  Azure HorizonDB now integrates with Azure Advisor 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available:  Azure HorizonDB now integrates with Azure Advisor ](https://azure.microsoft.com/updates?id=579938)

**Update ID**: 579938
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now integrates with Azure Advisor, and this feature is generally available.

- Key changes or new features  
Azure Advisor will analyze HorizonDB resources and provide personalized, actionable recommendations. These recommendations focus on optimizing reliability, performance, security, and cost of HorizonDB deployments. Developers and IT professionals can now access tailored guidance directly within the Azure portal, helping them proactively improve their database environment.

- Target audience affected  
The update is relevant to developers, database administrators, and IT professionals who use Azure HorizonDB. Teams responsible for managing and optimizing cloud database infrastructure will benefit from this integration.

- Important notes  
The integration enables users to leverage Azure Advisor’s best practices for HorizonDB, making it easier to identify and address potential issues or inefficiencies. Recommendations are surfaced automatically and can be reviewed in the Azure portal. No additional configuration is required to start receiving guidance, but users should regularly review Advisor insights to maximize the value of their HorizonDB resources.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=579938

**Details**:

**Azure Update Report**

**Title:** Generally Available: Azure HorizonDB now integrates with Azure Advisor  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579938)

---

**Background and Purpose of the Update**  
Azure HorizonDB, a managed database solution, now offers integration with Azure Advisor. The primary purpose of this update is to enable IT professionals to optimize their HorizonDB environments by leveraging Azure Advisor’s personalized recommendations. Azure Advisor is a cloud service that analyzes resource configurations and usage, providing actionable guidance to enhance reliability, performance, and cost efficiency. This integration aims to streamline database management and ensure best practices are followed for HorizonDB deployments.

**Specific Features and Detailed Changes**  
With this update, Azure Advisor can now directly analyze HorizonDB resources. The integration introduces the following features:

- **Personalized Recommendations:** Azure Advisor generates tailored suggestions specific to HorizonDB instances, covering areas such as reliability, performance, security, and cost optimization.
- **Actionable Guidance:** Recommendations are surfaced in the Azure portal, allowing administrators to review and implement improvements for their HorizonDB databases.
- **Continuous Analysis:** Azure Advisor routinely scans HorizonDB configurations and usage patterns, updating recommendations as the environment evolves.

**Technical Mechanisms and Implementation Methods**  
The technical implementation involves Azure Advisor accessing metadata and configuration details from HorizonDB resources. Advisor uses its analytics engine to evaluate these resources against established best practices and operational benchmarks. The integration is seamless within the Azure portal:

- **Resource Discovery:** Azure Advisor identifies HorizonDB instances within the subscription.
- **Analysis Engine:** Advisor processes resource properties, usage statistics, and configuration settings.
- **Recommendation Delivery:** Results are presented in the Advisor dashboard, categorized by reliability, performance, security, and cost.

IT professionals can access these recommendations through the Azure portal, and optionally automate remediation using Azure Resource Manager templates or scripts.

**Use Cases and Application Scenarios**  
This integration is particularly beneficial in the following scenarios:

- **Performance Optimization:** Database administrators can receive guidance on tuning HorizonDB for better throughput and latency.
- **Reliability Improvements:** Recommendations may include configuration changes to enhance availability and disaster recovery.
- **Cost Management:** Advisor may suggest resizing or consolidating HorizonDB resources to reduce operational expenses.
- **Security Enhancements:** Guidance may include enabling encryption, auditing, or access controls.

Organizations managing large-scale HorizonDB deployments can use Advisor’s insights to maintain compliance, optimize resources, and proactively address potential issues.

**Important Considerations and Limitations**  
- **Scope of Recommendations:** Advisor’s guidance is limited to the aspects it can analyze; some advanced or custom HorizonDB configurations may not be fully covered.
- **Actionability:** Not all recommendations may be directly actionable; some may require manual review or approval.
- **Update Frequency:** Recommendations are updated periodically, but may not reflect real-time changes.
- **Portal Dependency:** Access to recommendations requires Azure portal or API access.

**Integration with Related Azure Services**  
Azure Advisor’s integration with HorizonDB complements other Azure services such as Azure Monitor and Azure Security Center. Recommendations may reference actions involving these services, such as enabling monitoring or configuring security policies. The update enhances the overall Azure ecosystem by providing a unified experience for resource optimization across multiple services.

---

**Summary Sentence:**  
Azure HorizonDB’s integration with Azure Advisor is now generally available, offering IT professionals personalized, actionable recommendations to optimize database reliability, performance, and cost directly within the Azure portal.

---

### 81. Generally Available: Azure HorizonDB Monitoring via Alerts

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB Monitoring via Alerts](https://azure.microsoft.com/updates?id=579933)

**Update ID**: 579933
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now supports Azure Monitor alerts, which are generally available.

- Key changes or new features  
You can now set up Azure Monitor alert rules for HorizonDB, leveraging database metrics to trigger notifications when specific conditions or thresholds are met. This enables proactive monitoring, automated alerting, and faster response to potential issues in your HorizonDB environment.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB deployments, particularly those responsible for database health, performance, and operational monitoring.

- Important notes  
Alert rules can be customized based on HorizonDB metrics, allowing for granular control over monitoring scenarios (e.g., performance, availability, resource utilization). Integration with Azure Monitor streamlines incident response and enables automated workflows (such as triggering remediation actions or informing support teams). This update enhances operational visibility and reliability for HorizonDB users.  
For implementation details and supported metrics, refer to the official Azure documentation.

**Details**:

**Azure Update Report: Generally Available – Azure HorizonDB Monitoring via Alerts**

**Background and Purpose of the Update:**  
Azure HorizonDB is a managed database service in the Azure ecosystem. Monitoring database health, performance, and operational metrics is critical for maintaining reliability and meeting business SLAs. Previously, HorizonDB users had limited options for proactive monitoring and alerting. This update introduces native support for Azure Monitor alerts, enabling IT professionals to automate detection and notification of important database events and conditions.

**Specific Features and Detailed Changes:**  
With this update, Azure HorizonDB integrates directly with Azure Monitor’s alerting capabilities. Users can now create alert rules based on HorizonDB-specific metrics. These rules allow for the configuration of thresholds, so alerts are triggered when a metric crosses a defined value. The feature supports the following:

- Selection of HorizonDB metrics (such as CPU usage, storage consumption, query latency, etc.) as alert criteria.
- Customizable alert thresholds for each metric.
- Notification options, including email, SMS, and integration with Azure Action Groups for automated responses.
- Centralized management of alert rules within the Azure portal.

**Technical Mechanisms and Implementation Methods:**  
Azure Monitor collects telemetry and operational data from HorizonDB instances. Users define alert rules in the Azure portal or via ARM templates, specifying the metric, threshold, and evaluation frequency. When a metric breaches the threshold, Azure Monitor triggers an alert, which can be routed to Action Groups for notification or automation. The alerting mechanism leverages Azure Monitor’s native infrastructure, ensuring scalability and reliability.

**Use Cases and Application Scenarios:**  
- **Performance Monitoring:** Set alerts for high CPU or memory usage to detect resource bottlenecks.
- **Availability Management:** Monitor query latency or failed connection attempts to identify potential outages.
- **Capacity Planning:** Receive notifications when storage consumption approaches limits.
- **Security and Compliance:** Alert on unusual access patterns or failed authentication attempts.
- **DevOps Automation:** Integrate alerts with CI/CD pipelines or ITSM tools for automated remediation.

**Important Considerations and Limitations:**  
- Only HorizonDB metrics exposed to Azure Monitor are available for alerting.
- Alert thresholds and evaluation intervals must be carefully configured to avoid false positives or missed events.
- Notification channels depend on Action Group configuration; ensure recipients and automation workflows are correctly set up.
- There may be latency between metric collection and alert triggering, depending on the frequency of metric evaluation.

**Integration with Related Azure Services:**  
- **Azure Monitor:** Provides the core telemetry collection and alerting engine.
- **Azure Action Groups:** Enables notification and automated response actions (email, SMS, webhook, Azure Functions).
- **Azure Portal:** Centralized interface for rule creation and management.
- **Azure Resource Manager (ARM):** Supports programmatic rule deployment and configuration.

**Summary Sentence:**  
Azure HorizonDB now supports Azure Monitor alerts, enabling IT professionals to proactively monitor database metrics, configure custom thresholds, and receive notifications or automate responses when specified conditions are met, thereby enhancing operational visibility and reliability.

---

### 82. Generally Available: Azure HorizonDB Auditing

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB Auditing](https://azure.microsoft.com/updates?id=579928)

**Update ID**: 579928
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now offers general availability of database auditing capabilities using the pgAudit extension.

- Key changes or new features  
The update enables auditing of PostgreSQL database activities, including data access, data modifications, role changes, and DDL (Data Definition Language) operations. Audit logs can be captured and sent directly to Azure Monitor Log Analytics for centralized monitoring and analysis.

- Target audience affected  
This update is relevant to developers, database administrators, and IT professionals managing Azure HorizonDB instances, especially those requiring compliance, security, and activity tracking.

- Important notes  
The integration with pgAudit allows for granular auditing of database actions, supporting regulatory compliance and security requirements. Audit logs in Azure Monitor Log Analytics can be queried, visualized, and integrated with alerting workflows. Ensure proper configuration of pgAudit and Log Analytics to capture desired events and manage log retention. This feature is now generally available and ready for production use.

**Details**:

**Azure Update Report: Generally Available – Azure HorizonDB Auditing**

**Background and Purpose of the Update**  
Azure HorizonDB, a managed PostgreSQL-compatible database service, now offers auditing capabilities. The purpose of this update is to enhance security and compliance by enabling organizations to monitor and record critical database activities. Auditing is essential for regulatory compliance, forensic investigations, and operational transparency, allowing IT professionals to track who accessed or modified data, when, and how.

**Specific Features and Detailed Changes**  
The update introduces support for database auditing via the pgAudit extension. pgAudit is a PostgreSQL extension designed to provide detailed session and/or object-level logging. With this update, Azure HorizonDB users can capture a wide range of database activities, including:

- Data access (SELECT statements)
- Data modifications (INSERT, UPDATE, DELETE)
- Role changes (GRANT, REVOKE, ALTER ROLE)
- DDL operations (CREATE, ALTER, DROP objects)

Audit logs generated by pgAudit can now be sent directly to Azure Monitor Log Analytics, enabling centralized log management, querying, and analysis.

**Technical Mechanisms and Implementation Methods**  
The auditing mechanism leverages the pgAudit extension, which must be enabled on the HorizonDB instance. Once enabled, pgAudit intercepts and logs specified PostgreSQL commands based on configured audit settings. The logs are then exported to Azure Monitor Log Analytics, which provides a scalable and secure platform for storing, querying, and visualizing audit data.

The implementation steps typically involve:
1. Enabling pgAudit on the HorizonDB instance.
2. Configuring pgAudit settings to specify which activities to audit.
3. Setting up the integration to forward logs to Azure Monitor Log Analytics.

**Use Cases and Application Scenarios**  
- **Compliance Monitoring:** Organizations subject to regulations (e.g., GDPR, HIPAA, SOX) can use auditing to demonstrate adherence to data access and modification policies.
- **Security Incident Investigation:** Audit logs provide forensic evidence for investigating unauthorized access or suspicious activity.
- **Operational Oversight:** Administrators can monitor DDL and role changes to ensure proper change management practices.
- **Data Integrity Assurance:** Tracking modifications helps maintain data integrity and supports rollback or remediation actions.

**Important Considerations and Limitations**  
- **Performance Impact:** Enabling auditing may introduce additional overhead on database operations, depending on the volume and granularity of logged activities.
- **Log Retention and Storage:** Audit logs are stored in Azure Monitor Log Analytics, so organizations should plan for log retention policies and associated costs.
- **Configuration Complexity:** Proper configuration of pgAudit is required to ensure relevant activities are captured without excessive logging.
- **Scope:** Only activities supported by pgAudit (as listed) are captured; other types of events may not be audited.

**Integration with Related Azure Services**  
Audit logs are integrated with Azure Monitor Log Analytics, allowing users to leverage Azure’s monitoring and analytics capabilities. This integration enables:

- Centralized log storage and management
- Advanced querying and filtering using Kusto Query Language (KQL)
- Alerting and dashboarding via Azure Monitor
- Integration with Azure Sentinel for security analytics and threat detection

**Summary Sentence**  
Azure HorizonDB auditing is now generally available, enabling IT professionals to capture and analyze PostgreSQL database activities using pgAudit and Azure Monitor Log Analytics for enhanced security, compliance, and operational oversight.

---

### 83. Generally Available: Azure Multicloud Interconnect new cloud service provider support

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Multicloud Interconnect new cloud service provider support](https://azure.microsoft.com/updates?id=579766)

**Update ID**: 579766
**Data source**: Azure Updates API

**Categories**: Launched, Microsoft Ignite, Services, Feature

**Summary**:

- What was updated  
Azure Multicloud Interconnect is now generally available, offering managed private connectivity between Azure and other major cloud providers.

- Key changes or new features  
The service enables secure, high-performance connections between Azure and supported external clouds. Amazon Web Services (AWS) support is now generally available, while Google Cloud Platform (GCP) support is in public preview. This allows organizations to establish private, reliable links across cloud environments, improving data transfer, latency, and security. The service is fully managed, simplifying setup and ongoing operations.

- Target audience affected  
Developers, IT professionals, and cloud architects working in multicloud environments who require seamless, secure, and performant connectivity between Azure and AWS/GCP.

- Important notes if any  
Azure Multicloud Interconnect is ideal for hybrid and multicloud architectures, supporting scenarios like cross-cloud application integration, disaster recovery, and data migration. GCP support is currently in public preview, so production workloads should be limited to AWS and Azure connections until GCP reaches general availability. The service reduces complexity compared to manual network setups and enhances security by avoiding public internet routes. For more details, refer to the official Azure Update link.

**Details**:

**Azure Update Report**

**Title:** Generally Available: Azure Multicloud Interconnect new cloud service provider support  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579766)

---

**Background and Purpose of the Update**  
Azure Multicloud Interconnect is now generally available, marking a significant advancement in Azure’s managed connectivity offerings. The update addresses the growing demand among enterprises for secure, high-performance, and private connectivity between Azure and other major cloud providers. The purpose is to simplify and standardize multicloud network architectures, enabling organizations to leverage Azure alongside other platforms without compromising on security or operational complexity.

---

**Specific Features and Detailed Changes**  
- **General Availability:** Azure Multicloud Interconnect is now a fully supported managed service.
- **Expanded Provider Support:** The service now supports private connectivity to Amazon Web Services (AWS) in general availability and Google Cloud Platform (GCP) in public preview.
- **Private Connectivity:** Provides dedicated, private network links between Azure and supported external cloud providers, bypassing the public internet.
- **Managed Service:** Azure handles provisioning, monitoring, and maintenance of the interconnect, reducing operational overhead for customers.

---

**Technical Mechanisms and Implementation Methods**  
Azure Multicloud Interconnect leverages Azure’s backbone network and partner infrastructure to establish private, high-bandwidth connections between Azure and other cloud environments. The service abstracts complex network configuration and automates the setup of secure tunnels or circuits, ensuring data is transmitted over dedicated links. Connectivity is provisioned via Azure Portal or APIs, allowing for integration into existing infrastructure-as-code workflows. The managed nature of the service means Azure monitors link health, manages failover, and provides visibility into connection status and performance metrics.

---

**Use Cases and Application Scenarios**  
- **Hybrid and Multicloud Architectures:** Enterprises running workloads across Azure, AWS, and GCP can securely interconnect resources, enabling seamless data transfer and application integration.
- **Disaster Recovery and Backup:** Organizations can replicate data between clouds for redundancy and failover, using private links to ensure compliance and minimize latency.
- **Data Analytics and Migration:** Data can be moved or analyzed across platforms without exposure to the public internet, supporting secure migrations and cross-cloud analytics pipelines.
- **Regulatory Compliance:** Private connectivity helps meet strict compliance requirements by avoiding public internet routes and reducing risk of data interception.

---

**Important Considerations and Limitations**  
- **Provider Availability:** AWS connectivity is generally available, while GCP support is currently in public preview, indicating potential feature limitations or evolving support for GCP.
- **Service Boundaries:** The service is designed for private connectivity; it does not provide internet-based or public network routing.
- **Managed Scope:** Azure Multicloud Interconnect is a managed service, so customization may be limited compared to self-managed solutions.
- **Integration Requirements:** Users must configure endpoints in both Azure and the target cloud provider, adhering to each provider’s requirements for private connectivity.

---

**Integration with Related Azure Services**  
Azure Multicloud Interconnect can be integrated with Azure Virtual Network, ExpressRoute, and network security services to further enhance connectivity and security. It complements Azure’s hybrid and multicloud capabilities, allowing IT professionals to build robust, interconnected environments spanning multiple cloud platforms.

---

**Summary Sentence**  
Azure Multicloud Interconnect is now generally available, offering managed, private connectivity between Azure and major cloud providers (AWS and GCP), enabling secure, high-performance multicloud architectures with simplified provisioning and operational management.

---

### 84. Generally Available: Microsoft Foundry Support for Business Applications in Work IQ

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Microsoft Foundry Support for Business Applications in Work IQ](https://azure.microsoft.com/updates?id=579680)

**Update ID**: 579680
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

**What was updated:**  
Microsoft Foundry now offers general availability support for Business Applications in Work IQ.

**Key changes or new features:**  
- Developers can build business-connected agents more efficiently within Microsoft Foundry using Work IQ, minimizing the need for custom integrations.
- The update enables seamless transformation of enterprise data into actionable workflows, streamlining automation and business process management.
- Organizations can leverage their existing business applications and data sources to create intelligent agents that drive workflow automation and insights.

**Target audience affected:**  
- Developers building workflow automation and business-connected agents in Microsoft Foundry.
- IT professionals managing enterprise data integration and business application workflows.
- Organizations seeking to maximize value from their current business applications within the Microsoft ecosystem.

**Important notes:**  
- This update reduces development complexity and accelerates time-to-value by connecting business applications directly to workflow automation tools.
- The feature is now generally available, meaning it is production-ready and supported for enterprise use.
- For more details and implementation guidance, refer to the official Azure update link: [Microsoft Foundry Support for Business Applications in Work IQ](https://azure.microsoft.com/updates?id=579680).

**Details**:

**Background and Purpose of the Update**  
The update announces the general availability of Microsoft Foundry support for Business Applications in Work IQ. The primary goal is to streamline the development of business-connected agents within Microsoft Foundry, enabling organizations to leverage their enterprise data more effectively. By reducing the need for custom integration work, this update aims to accelerate the creation of actionable workflows and enhance the value derived from existing business applications.

**Specific Features and Detailed Changes**  
With this release, developers can utilize Business Applications in Work IQ to build agents that are tightly integrated with enterprise systems through Microsoft Foundry. The key feature is the reduction of manual integration efforts, as the platform now provides native support for connecting business applications to Work IQ agents. This enables the automatic transformation of enterprise data into workflows that can drive business processes, eliminating the need for extensive custom code or middleware.

**Technical Mechanisms and Implementation Methods**  
Microsoft Foundry acts as a development environment for creating intelligent agents and workflows. The integration with Business Applications in Work IQ leverages Foundry’s capabilities to connect to enterprise data sources and applications. Developers can use pre-built connectors and APIs provided by Foundry to access business data, which is then processed by Work IQ agents. These agents can trigger workflows, automate tasks, and deliver actionable insights based on real-time enterprise information. The technical implementation focuses on seamless data flow between business applications and Work IQ, facilitated by Foundry’s integration layer.

**Use Cases and Application Scenarios**  
Typical use cases include automating business processes such as approvals, notifications, and data-driven decision-making. For example, an organization can deploy agents that monitor sales data from CRM systems and automatically initiate follow-up actions in response to specific triggers. Other scenarios involve integrating ERP data to automate inventory management or connecting HR applications to streamline onboarding workflows. The update is particularly valuable for enterprises seeking to maximize the utility of their existing business applications without investing in complex custom integrations.

**Important Considerations and Limitations**  
IT professionals should be aware that while the update reduces custom integration work, the effectiveness of the solution depends on the compatibility of their business applications with Microsoft Foundry’s connectors and APIs. Organizations may need to validate that their enterprise data sources are supported. Additionally, security and compliance considerations must be addressed when connecting sensitive business data to Work IQ agents. Proper configuration of access controls and data governance policies is essential to ensure safe and compliant operation.

**Integration with Related Azure Services**  
This update enhances integration between Microsoft Foundry, Work IQ, and business applications. It can be leveraged alongside Azure services such as Azure Logic Apps for workflow automation, Azure Data Factory for data integration, and Azure Active Directory for identity management. The seamless connectivity provided by Foundry allows Work IQ agents to interact with Azure-based and on-premises business applications, enabling comprehensive enterprise automation solutions.

**Summary Sentence**  
Microsoft Foundry support for Business Applications in Work IQ is now generally available, enabling developers to build business-connected agents faster, reduce custom integration work, and transform enterprise data into actionable workflows for greater organizational value.

---

### 85. Public Preview: Azure SQL Database container provisioning in SQL Server Management Studio

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure SQL Database container provisioning in SQL Server Management Studio](https://azure.microsoft.com/updates?id=579665)

**Update ID**: 579665
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL Database container provisioning is now available in public preview directly from SQL Server Management Studio (SSMS).

- Key changes or new features  
Developers and IT professionals can quickly create an Azure SQL Database development environment within SSMS, without needing an Azure subscription, credit card, or pre-existing database. The new feature leverages Azure SQL Database containers, enabling rapid, isolated, and disposable database instances for development and testing. Provisioning is integrated into SSMS, streamlining workflows and reducing setup time.

- Target audience affected  
This update primarily benefits developers, database administrators, and IT professionals who use SSMS for SQL Server and Azure SQL Database development, testing, and prototyping. It is especially useful for those seeking fast, low-friction access to Azure SQL Database environments without administrative overhead.

- Important notes if any  
The feature is currently in public preview and intended for development and testing purposes only—not for production workloads. No Azure subscription or payment method is required during the preview. Users should monitor for updates regarding general availability and production support. For more details, refer to the official Azure Update announcement.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure SQL Database container provisioning in SQL Server Management Studio

**Background and Purpose of the Update:**  
This update introduces the ability to provision an Azure SQL Database development environment directly from SQL Server Management Studio (SSMS). The primary purpose is to streamline and accelerate the setup process for developers and IT professionals, enabling rapid access to Azure SQL Database containers without the need for an Azure subscription, credit card, or pre-existing database. This addresses common onboarding and development hurdles, making cloud-based SQL development more accessible and efficient.

**Specific Features and Detailed Changes:**  
- **Azure SQL Database Container Provisioning:** Users can now create a containerized Azure SQL Database instance from within SSMS.  
- **No Subscription or Payment Required:** The provisioning process does not require an Azure account, subscription, or credit card, removing barriers for experimentation and development.  
- **Instant Environment Setup:** The environment is provisioned in seconds, allowing for immediate database development and testing.  
- **Integration with SSMS:** The feature is accessible directly from SSMS, leveraging familiar workflows and tools for SQL professionals.

**Technical Mechanisms and Implementation Methods:**  
- **Containerized Deployment:** The Azure SQL Database container is provisioned as a lightweight, isolated environment, likely using container technology to emulate the Azure SQL Database experience.  
- **SSMS Integration:** The provisioning workflow is embedded within SSMS, enabling users to initiate and manage the container directly from the SSMS interface.  
- **No Azure Infrastructure Dependency:** The environment operates independently of Azure infrastructure for the purposes of development, removing the need for authentication or resource management through Azure Portal.

**Use Cases and Application Scenarios:**  
- **Development and Testing:** Ideal for developers needing a quick, disposable SQL environment for prototyping, testing, or learning without impacting production resources.  
- **Training and Education:** Facilitates hands-on training sessions or workshops where participants can access Azure SQL Database environments instantly without administrative overhead.  
- **Proof-of-Concept Work:** Enables rapid proof-of-concept development for SQL-based applications, with minimal setup time and no financial commitment.

**Important Considerations and Limitations:**  
- **Public Preview Status:** The feature is in public preview, indicating that it may not be fully supported or suitable for production workloads.  
- **No Existing Database Required:** The environment can be provisioned without an existing database, but details about persistence, scalability, and feature parity with full Azure SQL Database instances are not provided.  
- **Limited to Development Scenarios:** As no Azure subscription or payment is required, this environment is intended solely for development and testing, not for production use.

**Integration with Related Azure Services:**  
- **Azure SQL Database Experience:** The container provides an experience consistent with Azure SQL Database, enabling developers to build and test applications that will eventually target Azure SQL Database.  
- **SSMS Workflow:** The integration with SSMS ensures compatibility with existing SQL Server workflows, allowing seamless transition between local, containerized, and cloud-based environments.

**Summary Sentence:**  
This public preview enables IT professionals to provision Azure SQL Database containers instantly from SQL Server Management Studio for development and testing, eliminating the need for an Azure subscription or payment, and streamlining cloud SQL onboarding and experimentation.

---

### 86. Generally Available: Improved Apache AGE graph query and ingestion performance on Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Improved Apache AGE graph query and ingestion performance on Azure HorizonDB](https://azure.microsoft.com/updates?id=579660)

**Update ID**: 579660
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now offers generally available improvements to Apache AGE graph query and ingestion performance.

- Key changes or new features  
The update delivers enhanced query planning and optimized graph joins, resulting in faster execution of eligible read queries. Developers and IT professionals will also benefit from improved duplicate detection during data ingestion and better memory management, which together accelerate the building and querying of knowledge graphs.

- Target audience affected  
This update is relevant for developers and IT professionals working with graph databases, knowledge graph solutions, and applications leveraging Apache AGE on Azure HorizonDB.

- Important notes  
These performance enhancements are now generally available and can help reduce query latency and ingestion times for graph workloads. Users should review their current workloads to identify eligible queries and ingestion processes that may benefit from these improvements. For more details and guidance, refer to the official Azure update documentation: https://azure.microsoft.com/updates?id=579660

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Improved Apache AGE graph query and ingestion performance on Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579660)

---

**Background and Purpose of the Update:**

Azure HorizonDB is a managed database service designed for high-performance graph data workloads. Apache AGE (A Graph Extension) is an open-source extension that brings advanced graph query capabilities to PostgreSQL, enabling users to build and query knowledge graphs efficiently. The purpose of this update is to enhance the performance of Apache AGE on Azure HorizonDB, specifically targeting query execution and graph ingestion processes. These improvements address the need for faster and more efficient graph operations, which are critical for applications relying on complex relationships and large-scale graph data.

---

**Specific Features and Detailed Changes:**

- **Enhanced Query Planning:** The update introduces improvements in the query planning phase, allowing Apache AGE to generate more efficient execution plans for graph queries. This results in reduced latency and faster response times for eligible read operations.
- **Optimized Graph Joins:** Graph join operations, which are fundamental to traversing and analyzing relationships within knowledge graphs, have been optimized. The new mechanisms accelerate join processing, improving throughput and scalability for graph workloads.
- **Faster Duplicate Detection:** The ingestion pipeline now features improved duplicate detection algorithms. This enhancement reduces the time required to identify and handle duplicate entries during graph data ingestion, leading to quicker and more reliable data loading.
- **Improved Memory Management:** Memory utilization during query execution and ingestion has been optimized, enabling more stable and efficient processing of large graph datasets.

---

**Technical Mechanisms and Implementation Methods:**

- **Query Planning Enhancements:** The update leverages advanced heuristics and cost-based optimization techniques within Apache AGE to streamline the selection of query execution strategies. This minimizes unnecessary computation and improves query efficiency.
- **Graph Join Optimization:** Internal join algorithms have been refined to reduce computational overhead and memory consumption. This includes better indexing and caching strategies to facilitate rapid traversal and joining of graph nodes and edges.
- **Duplicate Detection Improvements:** The ingestion process now utilizes more efficient hashing and comparison methods to detect duplicates, reducing the impact on overall ingestion performance.
- **Memory Management Upgrades:** Allocation and deallocation routines have been tuned to prevent memory leaks and fragmentation, ensuring sustained performance during intensive graph operations.

---

**Use Cases and Application Scenarios:**

- **Knowledge Graph Construction:** Organizations building large-scale knowledge graphs for semantic search, recommendation systems, or entity resolution will benefit from faster ingestion and query performance.
- **Real-Time Graph Analytics:** Applications requiring real-time analysis of relationships, such as fraud detection or social network analysis, will experience improved responsiveness and scalability.
- **Data Integration Workflows:** ETL processes involving graph data can leverage enhanced duplicate detection and ingestion speed for more efficient data integration.

---

**Important Considerations and Limitations:**

- **Eligible Read Queries:** Performance improvements apply specifically to eligible read queries; users should verify that their workloads align with the optimized query patterns.
- **Resource Management:** While memory management is improved, users should continue to monitor resource consumption for large-scale workloads to avoid bottlenecks.
- **Compatibility:** Ensure that your deployment uses the latest version of Apache AGE on Azure HorizonDB to take advantage of these enhancements.

---

**Integration with Related Azure Services:**

- **Azure Data Factory:** Improved ingestion performance can be integrated with Azure Data Factory pipelines for efficient graph data loading and transformation.
- **Azure Synapse Analytics:** Enhanced query capabilities support advanced analytics scenarios when combined with Azure Synapse for unified data processing.
- **Azure Monitor:** Users can leverage Azure Monitor to track performance metrics and resource utilization for graph workloads on HorizonDB.

---

**Summary Sentence:**  
Azure HorizonDB now offers generally available improvements for Apache AGE, delivering faster graph query execution, optimized joins, enhanced duplicate detection, and better memory management to accelerate knowledge graph workloads and ingestion processes.

---

### 87. Public Preview: Azure Application Gateway confidential compute support

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Application Gateway confidential compute support](https://azure.microsoft.com/updates?id=579649)

**Update ID**: 579649
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Application Gateway now supports confidential compute in public preview.

- Key changes or new features  
The Application Gateway data plane can run in a confidential computing environment, leveraging hardware-based Trusted Execution Environments (TEEs). This enhancement protects sensitive data not only during transit but also while it is being processed and decrypted by the gateway. The feature ensures that decrypted requests and data remain isolated and secure, reducing exposure to potential threats.

- Target audience affected  
Developers and IT professionals responsible for managing application security, especially those handling sensitive or regulated data, benefit from this update. Organizations with strict compliance requirements or those seeking enhanced data privacy for web applications should consider this feature.

- Important notes  
This is a public preview feature and may not be suitable for production workloads yet. Integration with confidential compute may require changes to existing Application Gateway configurations. Review Azure documentation for compatibility and deployment guidance. Confidential compute support is designed to meet advanced security and compliance needs, but performance and cost implications should be evaluated before adoption.

Link: https://azure.microsoft.com/updates?id=579649

**Details**:

**Azure Update Report: Public Preview – Azure Application Gateway Confidential Compute Support**

**Background and Purpose of the Update**  
The Azure Application Gateway is a critical component for secure, scalable web traffic management. Traditionally, it protects data in transit via TLS encryption. However, organizations handling highly sensitive information require enhanced security to protect data during processing. This update introduces confidential compute support for Application Gateway, addressing the need to secure data not only in transit but also while it is being processed within the gateway itself.

**Specific Features and Detailed Changes**  
With this public preview, the Application Gateway data plane now operates within a confidential computing environment. This means that decrypted requests—previously exposed during processing—are now protected using advanced hardware-based isolation. The update ensures that sensitive data remains confidential throughout its lifecycle, including during inspection, routing, and load balancing operations performed by the gateway.

**Technical Mechanisms and Implementation Methods**  
The confidential compute capability leverages secure enclaves, a hardware-based trusted execution environment (TEE). When Application Gateway processes incoming requests, it decrypts them within the enclave, ensuring that plaintext data is never exposed to the underlying host or unauthorized processes. This isolation is enforced at the hardware level, preventing access from Azure operators, malicious actors, or compromised infrastructure. The implementation is seamless from the user perspective, with the data plane transparently running in the confidential environment without requiring application modifications.

**Use Cases and Application Scenarios**  
This feature is particularly valuable for industries with strict regulatory requirements, such as finance, healthcare, and government, where data privacy is paramount. Typical use cases include:
- Protecting sensitive customer information during web application traffic inspection.
- Ensuring compliance with data protection standards by minimizing exposure during processing.
- Securing internal APIs and microservices communications where decrypted data must remain confidential.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not yet be suitable for production workloads requiring full SLA guarantees. IT professionals should evaluate compatibility with their existing Application Gateway configurations and monitor for any performance implications due to enclave processing. Additionally, certain advanced features or integrations may not be supported in confidential compute mode during the preview phase.

**Integration with Related Azure Services**  
Azure Application Gateway confidential compute support can be integrated with other Azure security offerings, such as Azure Key Vault for certificate management and Azure Security Center for monitoring. It complements confidential computing capabilities across Azure, enabling end-to-end protection when combined with confidential VMs and containers. The gateway continues to work seamlessly with backend services hosted on Azure, ensuring secure traffic management without disrupting existing architectures.

**Summary Sentence**  
Azure Application Gateway confidential compute support, now in public preview, enhances data protection by processing decrypted requests within a secure hardware enclave, ensuring sensitive information remains confidential during transit and processing, and is ideal for organizations with stringent data privacy requirements.

---

### 88. Public Preview: Migrate Oracle databases to Azure Database for PostgreSQL using Azure Database Migration Service 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Migrate Oracle databases to Azure Database for PostgreSQL using Azure Database Migration Service ](https://azure.microsoft.com/updates?id=579607)

**Update ID**: 579607
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database Migration Service now supports offline migrations from Oracle databases to Azure Database for PostgreSQL, available in public preview.

- Key changes or new features  
Developers and IT professionals can use Azure Database Migration Service to configure source (Oracle) and target (PostgreSQL) connections, select specific schemas for migration, initiate data transfer, and monitor migration progress. This update enables a streamlined migration path for organizations moving from Oracle to PostgreSQL on Azure, reducing manual effort and complexity.

- Target audience affected  
This update is relevant for database administrators, IT professionals, and developers responsible for database modernization, cloud migration, or platform consolidation projects, especially those seeking to migrate from Oracle to Azure Database for PostgreSQL.

- Important notes if any  
The migration is currently limited to offline scenarios, meaning the source database must be unavailable during migration. This feature is in public preview, so production workloads should be approached with caution. Users should review documentation for supported Oracle and PostgreSQL versions and test migrations in non-production environments before full deployment. 

For more details, visit: https://azure.microsoft.com/updates?id=579607

**Details**:

**Azure Update Technical Summary**

**Title:** Public Preview: Migrate Oracle databases to Azure Database for PostgreSQL using Azure Database Migration Service  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579607)

---

**Background and Purpose of the Update**

This update introduces offline data migration support from Oracle databases to Azure Database for PostgreSQL servers using Azure Database Migration Service (DMS). The purpose is to facilitate organizations in transitioning their workloads from Oracle, a proprietary relational database system, to Azure Database for PostgreSQL, an open-source and cloud-native platform. This capability addresses the need for efficient, managed migration paths for customers seeking to modernize their database infrastructure and reduce licensing costs.

---

**Specific Features and Detailed Changes**

- **Offline Data Migration:** Azure DMS now enables offline migrations, meaning the source Oracle database is not actively updated during the migration process. This is suitable for scenarios where downtime is acceptable.
- **Configurable Connections:** Users can set up both source (Oracle) and target (Azure Database for PostgreSQL) database connections within the DMS interface.
- **Schema Selection:** The service allows selection of specific schemas to migrate, providing granular control over the migration scope.
- **Migration Initiation and Tracking:** Users can initiate the data transfer process and monitor the migration status directly within the Azure DMS portal.

---

**Technical Mechanisms and Implementation Methods**

Azure Database Migration Service orchestrates the migration workflow by connecting to the Oracle source database and the Azure Database for PostgreSQL target. The process involves:

1. **Connection Configuration:** Securely configuring endpoints for both Oracle and PostgreSQL databases.
2. **Schema Mapping:** Selecting schemas to migrate, which may involve mapping Oracle data types and structures to their PostgreSQL equivalents.
3. **Data Transfer:** Initiating the offline migration, where DMS extracts data from Oracle and loads it into PostgreSQL.
4. **Status Tracking:** Providing real-time status updates and logs to monitor progress and troubleshoot issues.

The migration is offline, so changes made to the Oracle database after migration starts are not reflected in the PostgreSQL target.

---

**Use Cases and Application Scenarios**

- **Database Modernization:** Organizations moving from legacy Oracle systems to open-source PostgreSQL on Azure for cost savings and flexibility.
- **Cloud Adoption:** Enterprises migrating on-premises Oracle workloads to Azure cloud infrastructure.
- **Development and Testing:** Teams replicating Oracle environments in PostgreSQL for testing or development purposes.

---

**Important Considerations and Limitations**

- **Offline Migration Only:** The current preview supports only offline migrations; continuous synchronization or minimal downtime migrations are not available.
- **Schema Selection:** Only selected schemas can be migrated, so careful planning is required to ensure all necessary data is included.
- **Data Type Compatibility:** Users must verify compatibility between Oracle and PostgreSQL data types and structures.
- **Migration Status Monitoring:** It is essential to monitor migration status and logs for error handling and validation.

---

**Integration with Related Azure Services**

Azure Database Migration Service integrates with Azure Database for PostgreSQL, providing a managed migration workflow. The service can be accessed via the Azure portal, and migration status can be tracked alongside other Azure resources. This update complements Azure’s broader database modernization offerings, including support for other source/target combinations.

---

**Summary Sentence**

Azure Database Migration Service now enables offline migrations from Oracle to Azure Database for PostgreSQL, allowing IT professionals to configure connections, select schemas, initiate data transfer, and monitor migration status for streamlined database modernization.

---

### 89. Public Preview: Build Knowledge Graphs with AI pipeline in Azure HorizonDB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Build Knowledge Graphs with AI pipeline in Azure HorizonDB ](https://azure.microsoft.com/updates?id=579602)

**Update ID**: 579602
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB introduces a public preview feature enabling the creation of knowledge graphs using AI pipelines directly from PostgreSQL data.

- Key changes or new features  
The new capability leverages AI to automatically extract entities, relationships, and properties from source data, facilitating the construction of knowledge graphs. Developers can build connected, context-rich graph applications without manual data modeling. The integration with PostgreSQL allows seamless use of existing data, and the AI pipeline simplifies graph creation and querying.

- Target audience affected  
This update is relevant for developers building graph-based applications, data engineers working with PostgreSQL in Azure, and IT professionals managing data infrastructure who want to enhance data connectivity and context using AI-driven knowledge graphs.

- Important notes if any  
The feature is currently in public preview and may not be suitable for production workloads. Users should evaluate performance and compatibility with their existing PostgreSQL deployments. Documentation and API support are available for integration and testing. This update can accelerate graph application development and improve data insights by automating entity and relationship extraction.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Build Knowledge Graphs with AI pipeline in Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579602)

---

**Background and Purpose of the Update:**  
This update introduces a public preview feature in Azure HorizonDB, enabling users to build knowledge graphs directly from their PostgreSQL data using AI pipelines. The purpose is to facilitate the creation of connected, context-rich graph applications by leveraging AI to extract structured information from relational data sources. This addresses the need for organizations to derive deeper insights and relationships from their existing data without manual modeling or extensive data transformation.

---

**Specific Features and Detailed Changes:**  
- **Knowledge Graph Capability:** Azure HorizonDB now supports the automatic construction of knowledge graphs from PostgreSQL data.
- **AI-Driven Entity Extraction:** The pipeline utilizes AI to identify entities, relationships, and properties within the source data.
- **Graph Application Enablement:** Users can build applications that utilize the interconnected nature of knowledge graphs for advanced querying and analytics.
- **Direct Integration with PostgreSQL:** The feature operates directly on PostgreSQL data, streamlining the process and minimizing the need for data migration or duplication.

---

**Technical Mechanisms and Implementation Methods:**  
- **AI Pipeline:** The core mechanism is an AI pipeline that processes PostgreSQL data. This pipeline applies machine learning and natural language processing techniques to automatically detect entities (such as people, places, or objects), relationships (such as associations or hierarchies), and properties (attributes or metadata).
- **Graph Construction:** Once entities and relationships are identified, the pipeline constructs a knowledge graph model, which can be queried for complex, context-rich information.
- **Query Generation:** The system enables users to run queries against the knowledge graph, leveraging the AI-extracted structure for enhanced data retrieval and analysis.

---

**Use Cases and Application Scenarios:**  
- **Enterprise Data Integration:** Organizations can unify disparate data sources and uncover hidden relationships within their business data.
- **Contextual Search and Recommendation:** Applications can provide more relevant search results and recommendations by understanding the context and connections within data.
- **Fraud Detection and Risk Analysis:** Knowledge graphs can reveal complex patterns and relationships that are indicative of fraud or risk.
- **Customer 360 Views:** Businesses can build comprehensive profiles of customers by linking data across multiple tables and sources.

---

**Important Considerations and Limitations:**  
- **Public Preview:** The feature is currently in public preview, which may imply limited support, evolving functionality, and possible changes before general availability.
- **Source Data Requirements:** The pipeline operates on PostgreSQL data; compatibility with other data sources is not mentioned.
- **AI Accuracy:** The quality of entity and relationship extraction depends on the AI models and the structure of the source data.
- **Performance and Scalability:** As with any AI-driven process, performance may vary based on data volume and complexity.

---

**Integration with Related Azure Services:**  
- **Azure HorizonDB:** The knowledge graph capability is native to Azure HorizonDB, leveraging its database and AI integration features.
- **PostgreSQL Integration:** Direct support for PostgreSQL data ensures seamless use for organizations already utilizing Azure Database for PostgreSQL.
- **Potential for Azure AI Services:** While not explicitly stated, the AI pipeline may utilize Azure AI services for entity extraction and relationship modeling.

---

**Summary Sentence:**  
Azure HorizonDB now offers a public preview feature that enables IT professionals to build knowledge graphs from PostgreSQL data using AI pipelines, facilitating the development of connected, context-rich graph applications through automated entity and relationship extraction.

---

### 90. Generally Available: Azure HorizonDB Generic Log Analytics Integration

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB Generic Log Analytics Integration](https://azure.microsoft.com/updates?id=579574)

**Update ID**: 579574
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now offers general availability for integration with Azure Monitor diagnostic settings, enabling log and diagnostic data export to Azure Log Analytics.

- Key changes or new features  
Developers and IT professionals can configure HorizonDB to send database logs and diagnostic information directly to Azure Log Analytics. This integration allows for centralized querying, analysis, and troubleshooting of database activity using Log Analytics’ powerful tools and dashboards. The update simplifies monitoring workflows and enhances visibility into database operations and performance.

- Target audience affected  
This update is relevant to developers, database administrators, and IT professionals managing Azure HorizonDB instances, especially those responsible for monitoring, diagnostics, and operational analytics.

- Important notes  
To leverage this feature, users must configure diagnostic settings in Azure Monitor for their HorizonDB resources. This integration supports improved troubleshooting, compliance, and operational insights by consolidating logs and diagnostics in Log Analytics. Review documentation for setup steps and data retention policies.  

[Azure Update Link](https://azure.microsoft.com/updates?id=579574)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure HorizonDB Generic Log Analytics Integration  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579574)

---

**Background and Purpose of the Update**  
Azure HorizonDB has introduced native support for integration with Azure Monitor diagnostic settings. The primary purpose of this update is to enable IT professionals to centralize the collection, querying, and analysis of HorizonDB database logs and diagnostic data. By routing this information to Azure Log Analytics, organizations can enhance their monitoring, troubleshooting, and operational visibility into database activity.

**Specific Features and Detailed Changes**  
- **Diagnostic Settings Integration:** HorizonDB now exposes its diagnostic logs and metrics through Azure Monitor’s diagnostic settings interface.
- **Log Analytics Support:** Users can configure HorizonDB to send logs and diagnostic data directly to Azure Log Analytics workspaces.
- **Centralized Querying:** All database activity logs and diagnostics are accessible in Log Analytics, enabling advanced querying and analysis.
- **Troubleshooting Enhancement:** The integration streamlines issue detection and resolution by providing a unified view of database operations.

**Technical Mechanisms and Implementation Methods**  
- **Configuration:** IT professionals can configure diagnostic settings for HorizonDB via the Azure Portal, ARM templates, or REST APIs. This involves selecting HorizonDB as the resource and specifying Log Analytics as the destination.
- **Data Flow:** Once configured, HorizonDB emits logs and diagnostic data to Azure Monitor, which then routes the data to the specified Log Analytics workspace.
- **Log Analytics Workspace:** The workspace acts as a repository for all incoming HorizonDB logs, supporting Kusto Query Language (KQL) for querying and analysis.
- **Security and Access Control:** Access to logs is managed through Azure RBAC, ensuring only authorized users can view or query the data.

**Use Cases and Application Scenarios**  
- **Operational Monitoring:** Teams can monitor database health, performance, and activity in real-time using Log Analytics dashboards.
- **Incident Response:** When issues arise, engineers can quickly query logs to identify root causes and remediate problems.
- **Compliance and Auditing:** Centralized log storage supports compliance requirements by maintaining a historical record of database activity.
- **Custom Alerting:** Integration with Azure Monitor enables custom alerts based on log data, facilitating proactive management.

**Important Considerations and Limitations**  
- **Data Retention:** Log Analytics workspace retention policies apply; ensure configurations meet organizational requirements.
- **Cost Implications:** Sending large volumes of logs to Log Analytics may incur additional costs based on workspace pricing.
- **Log Types:** Only logs and diagnostic data exposed via HorizonDB’s diagnostic settings are available; ensure required log categories are enabled.
- **Latency:** There may be minimal latency between log generation in HorizonDB and availability in Log Analytics.

**Integration with Related Azure Services**  
- **Azure Monitor:** Acts as the central platform for configuring diagnostic settings and routing logs.
- **Azure Log Analytics:** Provides storage, querying, and analysis capabilities for HorizonDB logs.
- **Azure Security Center:** Can leverage Log Analytics data for security monitoring and threat detection.
- **Azure Automation:** Enables automated responses or workflows based on log data triggers.

---

**Summary Sentence:**  
Azure HorizonDB now supports direct integration with Azure Monitor diagnostic settings, allowing database logs and diagnostic data to be sent to Azure Log Analytics for centralized querying, analysis, and troubleshooting, thereby enhancing operational visibility and incident response capabilities for IT professionals.

---

### 91. Public Preview: Encryption at rest with customer-managed keys in Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Encryption at rest with customer-managed keys in Azure HorizonDB](https://azure.microsoft.com/updates?id=579540)

**Update ID**: 579540
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB now supports encryption at rest using customer-managed keys (CMK), available in public preview.

- Key changes or new features  
Previously, Azure HorizonDB only used service-managed keys (SMK) for encrypting data at rest, with Azure controlling the keys. With this update, customers can supply and manage their own encryption keys stored in Azure Key Vault. This allows organizations to have greater control over their data security and compliance requirements, including key rotation and revocation.

- Target audience affected  
This update is relevant to developers and IT professionals who manage Azure HorizonDB instances, especially those with strict regulatory, compliance, or security needs that require direct control over encryption keys.

- Important notes  
CMK support is currently in public preview, so it may not be suitable for production workloads yet. Integration with Azure Key Vault is required for managing customer keys. Organizations should review their compliance requirements and test the feature before full adoption. For more details, see the official Azure Update announcement: https://azure.microsoft.com/updates?id=579540

**Details**:

**Azure Update Report**

**Title:** Public Preview: Encryption at rest with customer-managed keys in Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579540)

---

**Background and Purpose of the Update**  
Azure HorizonDB previously used service-managed keys (SMK) for encrypting data at rest, meaning Azure handled all aspects of key management and rotation. The purpose of this update is to introduce customer-managed keys (CMK) for encryption at rest, now available in public preview. This enhancement addresses enterprise requirements for greater control over data security and compliance, allowing organizations to manage their own encryption keys and meet regulatory standards that mandate customer control over cryptographic material.

**Specific Features and Detailed Changes**  
The update enables Azure HorizonDB users to configure and use CMK for encrypting data at rest. This is a shift from the default SMK approach, providing customers the ability to supply, manage, and rotate their own keys. The feature is available in public preview, allowing customers to test and validate the CMK functionality within their HorizonDB deployments. The change primarily affects the encryption-at-rest layer, giving customers direct control over the keys used to encrypt their stored data.

**Technical Mechanisms and Implementation Methods**  
With CMK support, Azure HorizonDB integrates with Azure Key Vault, which is the recommended service for storing and managing customer-managed keys. Customers generate or import their own keys into Azure Key Vault and configure HorizonDB to reference these keys for encryption operations. When data is written to HorizonDB, the service uses the specified CMK from Key Vault to encrypt the data at rest. Key rotation and revocation are managed by the customer through Azure Key Vault, and HorizonDB will use the latest version of the key as configured. The implementation ensures that Azure does not have access to the plaintext keys, and all cryptographic operations are performed using the customer-supplied keys.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations with strict regulatory, compliance, or internal security requirements. Typical use cases include:
- Enterprises in regulated industries (finance, healthcare, government) needing to demonstrate control over encryption keys.
- Scenarios requiring key rotation policies aligned with corporate governance.
- Multi-tenant applications where each tenant’s data must be encrypted with separate keys.
- Customers migrating sensitive workloads to Azure HorizonDB and requiring CMK for compliance with standards such as GDPR, HIPAA, or PCI DSS.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not yet be suitable for production workloads. Customers should evaluate the preview for stability, performance, and compatibility with their existing HorizonDB deployments. Key management responsibilities shift to the customer, including key rotation, backup, and recovery. Mismanagement of keys (such as accidental deletion or loss of access) can result in data inaccessibility. Customers must also ensure proper configuration of Azure Key Vault permissions and policies to avoid unauthorized access or operational disruptions.

**Integration with Related Azure Services**  
CMK support in HorizonDB is tightly integrated with Azure Key Vault, which provides secure key storage, access control, and auditing. Customers can leverage Key Vault’s capabilities for key lifecycle management, monitoring, and compliance reporting. The integration enables seamless use of existing Azure security infrastructure and policies, and can be combined with Azure RBAC and managed identities for secure access to keys.

---

**Summary Sentence:**  
Azure HorizonDB now supports customer-managed keys for encryption at rest in public preview, enabling organizations to control their own encryption keys via Azure Key Vault for enhanced security and compliance.

---

### 92. Generally Available: Transparent data encryption (TDE) in Azure SQL Database AES keys 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Transparent data encryption (TDE) in Azure SQL Database AES keys ](https://azure.microsoft.com/updates?id=579531)

**Update ID**: 579531
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Transparent Data Encryption (TDE) in Azure SQL Database now supports AES-256 keys as TDE protectors.

- Key changes or new features  
You can use AES-256 keys stored in Azure Key Vault Premium or Managed HSM to protect data at rest in Azure SQL Database, in addition to the previously supported RSA keys. This provides a cryptographic alternative that is more resilient to potential quantum computing threats, as AES-256 is considered quantum-safe compared to RSA. The update allows organizations to enhance their security posture and meet compliance requirements by leveraging stronger encryption standards.

- Target audience affected  
Developers and IT professionals responsible for database security, compliance, and key management in Azure SQL Database environments.

- Important notes  
AES-256 keys must be stored in Azure Key Vault Premium or Managed HSM to be used as TDE protectors. This feature is now generally available. Organizations should evaluate their encryption strategies, especially in anticipation of future quantum computing risks. Existing TDE implementations using RSA keys remain supported, but migration to AES-256 is recommended for enhanced security.

For more details, see the official update: https://azure.microsoft.com/updates?id=579531

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Transparent data encryption (TDE) in Azure SQL Database AES keys

**Background and Purpose of the Update:**  
Transparent Data Encryption (TDE) is a critical security feature in Azure SQL Database, designed to protect data at rest by encrypting database files. Traditionally, TDE protectors have used RSA keys, which are robust against current classical computing threats. However, with the advancement of quantum computing, RSA encryption may become vulnerable. To address this potential risk and enhance cryptographic resilience, Azure now supports the use of AES-256 keys for TDE protectors, offering a symmetric encryption alternative that is less susceptible to quantum attacks.

**Specific Features and Detailed Changes:**  
This update introduces the capability to use AES-256 keys, stored in Azure Key Vault Premium or Managed HSM, as TDE protectors for Azure SQL Database. Previously, only RSA keys could be used for this purpose. AES-256 keys provide a higher level of security due to their resistance to quantum computing threats and their robust symmetric encryption properties. The update allows customers to select AES-256 keys as the encryption mechanism for TDE, giving them greater flexibility and control over their data protection strategy.

**Technical Mechanisms and Implementation Methods:**  
- **Key Management:** AES-256 keys must be provisioned and stored in Azure Key Vault Premium or Managed HSM. These services provide secure key storage and management capabilities, ensuring that keys are protected and accessible only to authorized entities.
- **TDE Protector Configuration:** Administrators can configure Azure SQL Database to use an AES-256 key as the TDE protector. This involves specifying the key identifier from Azure Key Vault or Managed HSM during the database setup or through subsequent configuration changes.
- **Encryption Process:** Once configured, TDE uses the AES-256 key to encrypt the database files transparently. The encryption and decryption operations are handled by the database engine, ensuring seamless protection without impacting application performance.

**Use Cases and Application Scenarios:**  
- **Quantum-Resistant Security:** Organizations concerned about future quantum threats can leverage AES-256 keys to ensure their data remains secure as cryptographic standards evolve.
- **Regulatory Compliance:** Enterprises subject to strict data protection regulations may require advanced encryption mechanisms, such as AES-256, to meet compliance requirements.
- **Key Management Integration:** Businesses already using Azure Key Vault Premium or Managed HSM for centralized key management can streamline their security operations by using AES-256 keys for TDE.

**Important Considerations and Limitations:**  
- **Key Vault Requirements:** Only AES-256 keys stored in Azure Key Vault Premium or Managed HSM are supported. Standard Key Vault does not provide this capability.
- **Migration:** Existing databases using RSA keys may need to follow specific migration procedures to switch to AES-256 keys, ensuring continuity and data integrity.
- **Compatibility:** Ensure that all applications and systems interacting with the encrypted database are compatible with the new encryption mechanism.

**Integration with Related Azure Services:**  
- **Azure Key Vault Premium/Managed HSM:** These services are integral to the update, providing secure storage, lifecycle management, and access control for AES-256 keys.
- **Azure SQL Database:** The update enhances Azure SQL Database’s encryption capabilities, allowing seamless integration with enterprise key management solutions.
- **Security and Compliance Solutions:** The update supports integration with Azure security and compliance monitoring tools, enabling organizations to audit and validate their encryption practices.

**Summary Sentence:**  
Azure SQL Database now supports AES-256 keys stored in Azure Key Vault Premium or Managed HSM as TDE protectors, offering enhanced data-at-rest encryption and quantum-resistant security options for enterprise workloads.

---

### 93. Public Preview: Build with Azure SQL Database container locally without an Azure subscription or credit card 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Build with Azure SQL Database container locally without an Azure subscription or credit card ](https://azure.microsoft.com/updates?id=579525)

**Update ID**: 579525
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL Database container is now available in Public Preview, allowing developers to run the Azure SQL Database engine locally without needing an Azure subscription or credit card.

- Key changes or new features  
Developers and IT professionals can build and test applications using a containerized version of Azure SQL Database on their local machines. This local instance runs the same engine as the cloud version, ensuring compatibility for development and CI workflows. The container is free for local development and CI use, supporting cross-platform scenarios and simplifying setup for testing and prototyping.

- Target audience affected  
This update is aimed at developers, DevOps engineers, and IT professionals who build, test, or validate applications using Azure SQL Database. It is especially relevant for those who want to streamline local development, CI pipelines, or work in environments without immediate access to Azure resources.

- Important notes if any  
No Azure subscription or credit card is required to use the local container, making it accessible for all developers. The container is intended for local development and CI only, not for production workloads. This preview helps ensure code compatibility and accelerates development cycles before deploying to Azure SQL Database in the cloud.  
For more information, see the official Azure Update: https://azure.microsoft.com/updates?id=579525

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Build with Azure SQL Database container locally without an Azure subscription or credit card  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=579525)

---

**Background and Purpose of the Update**  
This update introduces the ability for developers and IT professionals to build and test applications using the Azure SQL Database engine locally via a containerized environment. The primary purpose is to enable local development and continuous integration (CI) workflows without requiring an Azure subscription or credit card. This addresses a common barrier for developers who wish to prototype, test, or validate applications with Azure SQL Database features but are restricted by cloud access requirements or cost concerns.

**Specific Features and Detailed Changes**  
- **Local Azure SQL Database Container:** The update provides a container image that runs the same Azure SQL Database engine used in the cloud, ensuring consistency between local and cloud environments.
- **No Subscription or Payment Required:** Developers can use this container for free, specifically for local development and CI purposes, removing the need for an Azure account or credit card.
- **Cross-Platform Support:** The containerized approach allows developers to run Azure SQL Database locally on any platform that supports containers, such as Windows, macOS, or Linux.
- **Public Preview Availability:** The feature is currently in public preview, allowing early access and feedback from the community.

**Technical Mechanisms and Implementation Methods**  
- **Containerization:** The Azure SQL Database engine is packaged as a container image, likely compatible with Docker or similar container runtimes. This enables rapid deployment and isolation of the database environment on local machines.
- **Engine Consistency:** The container runs the same engine as the Azure cloud service, ensuring that local development mirrors production environments for schema, query behavior, and compatibility.
- **Local Dev and CI Integration:** The container can be integrated into local development environments and CI pipelines, facilitating automated testing and development workflows without external dependencies.

**Use Cases and Application Scenarios**  
- **Local Application Development:** Developers can build and test applications against a local instance of Azure SQL Database, ensuring compatibility before deploying to the cloud.
- **Continuous Integration Pipelines:** CI/CD workflows can incorporate the Azure SQL Database container for automated testing, schema validation, and migration scripts.
- **Prototyping and Experimentation:** Teams can rapidly prototype database solutions without provisioning cloud resources, accelerating innovation and reducing friction.
- **Training and Education:** The container can be used in educational settings or workshops to demonstrate Azure SQL Database features without requiring cloud access.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes or limitations.
- **Local Only:** The container is intended for local development and CI; it does not provide cloud scalability, managed backups, or high availability features inherent to the Azure cloud service.
- **Feature Parity:** While the engine is the same, some Azure-specific integrations or features may not be available or fully supported in the local container environment.
- **Resource Constraints:** The performance and resource limits are determined by the local host machine, not by Azure’s managed infrastructure.

**Integration with Related Azure Services**  
- **Seamless Transition to Cloud:** Applications developed and tested locally can be deployed to Azure SQL Database in the cloud with minimal changes, leveraging the engine consistency.
- **Azure DevOps and CI/CD:** The container can be incorporated into Azure DevOps pipelines for automated testing and validation, streamlining the development lifecycle.
- **Compatibility with Azure SDKs and Tools:** Developers can use Azure SDKs, tools, and drivers with the local container, ensuring smooth integration and migration to cloud environments.

---

**Summary Sentence:**  
Azure now offers a public preview of Azure SQL Database container for local development and CI, enabling engineers to build and test applications with the same engine as the cloud service, free of charge and without requiring an

---

### 94. Generally Available: Managed Connectors in Azure Functions

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Managed Connectors in Azure Functions](https://azure.microsoft.com/updates?id=579440)

**Update ID**: 579440
**Data source**: Azure Updates API

**Categories**: Launched, Integration, Internet of Things, Logic Apps, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Managed connectors in Azure Functions are now generally available.

- Key changes or new features  
Developers can now use managed connectors within Azure Functions to build event-driven applications that interact with Microsoft 365, SaaS platforms, and business systems. Managed connectors simplify integration by providing pre-built connectivity to various services, allowing developers to trigger functions and automate workflows based on external events. This feature leverages the familiar Azure Functions programming model, enabling seamless integration without managing custom authentication or connection logic.

- Target audience affected  
Developers building serverless, event-driven applications and IT professionals responsible for integrating Azure Functions with external services (e.g., Microsoft 365, SaaS, business systems).

- Important notes if any  
Managed connectors streamline integration scenarios, reducing development overhead and improving security by handling authentication and connection management. This update is ideal for organizations looking to automate business processes or build scalable integrations across cloud and enterprise platforms using Azure Functions. Existing Azure Functions can be enhanced with managed connectors without major code changes. For full details and supported connectors, refer to the official documentation.

**Details**:

**Azure Update Report: Managed Connectors in Azure Functions Now Generally Available**

**Background and Purpose of the Update**  
The general availability of managed connectors in Azure Functions addresses the need for seamless integration between event-driven applications and external systems such as Microsoft 365, SaaS platforms, and business systems. This update is designed to simplify the process of connecting Azure Functions to these services, enabling developers to build reactive workflows without extensive custom integration code.

**Specific Features and Detailed Changes**  
With this release, managed connectors can now be utilized directly within Azure Functions. These connectors provide pre-built integration points to a wide array of external services, allowing developers to trigger functions based on events or data changes, and to perform actions in connected systems. The update enables Azure Functions to leverage connectors that were previously available only in Logic Apps, thus expanding the scope and flexibility of serverless application development.

**Technical Mechanisms and Implementation Methods**  
Managed connectors are implemented as reusable components that abstract the authentication, communication, and data handling required to interact with external services. In Azure Functions, developers can configure these connectors within their function app, using the familiar programming models (such as C#, JavaScript, Python, etc.). The connectors handle secure authentication, manage API calls, and provide standardized input/output bindings, allowing functions to react to events or invoke actions in external systems with minimal code. This integration is managed through Azure’s infrastructure, ensuring reliability and scalability.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Automating business workflows by reacting to events in Microsoft 365 (e.g., new emails, calendar events) and triggering actions in other SaaS applications.
- Integrating with CRM or ERP systems to synchronize data or respond to business events.
- Building notification systems that respond to changes in external services and send alerts via Teams, Slack, or other platforms.
- Creating serverless APIs that interact with third-party services using managed connectors, reducing development time and complexity.

**Important Considerations and Limitations**  
When utilizing managed connectors in Azure Functions, IT professionals should consider:
- Connector availability: Only connectors supported in Azure Functions are usable; not all Logic Apps connectors may be available.
- Authentication and security: Managed connectors handle authentication, but developers must ensure proper configuration and compliance with organizational security policies.
- Performance and scalability: While Azure Functions are highly scalable, connector-specific limitations (such as rate limits or quotas imposed by external services) may affect throughput.
- Cost implications: Usage of managed connectors may incur additional charges, depending on the connector and the volume of operations.

**Integration with Related Azure Services**  
Managed connectors in Azure Functions integrate seamlessly with other Azure services, such as Azure Logic Apps, Azure Event Grid, and Azure API Management. This enables developers to build comprehensive solutions that combine serverless compute, workflow automation, and API integration. Functions using managed connectors can be orchestrated within larger workflows, exposed as APIs, or linked to event-driven architectures using Event Grid.

**Summary Sentence**  
Managed connectors in Azure Functions are now generally available, enabling developers to build event-driven applications that react to events and take actions across Microsoft 365, SaaS, and business systems using the familiar Azure Functions programming model.

---

### 95. Public Preview: Bring-your-own image and Cosmos DB MCP server in Azure Connector Namespace hosted MCP​

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Bring-your-own image and Cosmos DB MCP server in Azure Connector Namespace hosted MCP​](https://azure.microsoft.com/updates?id=579435)

**Update ID**: 579435
**Data source**: Azure Updates API

**Categories**: In preview, Integration, Internet of Things, Logic Apps, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Connector Namespace now supports public preview for bring-your-own image and Cosmos DB MCP server in its hosted MCP server capability.

- Key changes or new features  
Developers can now deploy custom container images ("bring-your-own image") as MCP servers within Azure Connector Namespace, enabling more flexibility and customization for AI agent tool access. Additionally, Cosmos DB MCP server support allows integration of Cosmos DB as a tool for AI agents, managed directly by the platform. The infrastructure provisioning, hosting, and Microsoft Entra authentication are handled automatically, reducing operational overhead.

- Target audience affected  
This update is relevant to developers building AI agents, IT professionals managing infrastructure, and teams integrating custom tools or databases (such as Cosmos DB) into AI solutions using Azure Connector Namespace.

- Important notes if any  
The hosted MCP server capability simplifies deployment and management by eliminating the need for a separate hosting stack. Security and access control are managed via Microsoft Entra. This is a public preview feature, so production use should be approached with caution and feedback is encouraged. For more details, refer to the official Azure Update announcement.

**Details**:

**Azure Update Technical Report: Public Preview – Bring-your-own image and Cosmos DB MCP server in Azure Connector Namespace hosted MCP**

---

**Background and Purpose of the Update**

The Azure Connector Namespace’s hosted MCP (Managed Control Plane) server capability is introduced to streamline the integration of AI agents with external tools. Traditionally, developers needed to build and maintain a dedicated hosting stack to enable tool access for AI agents, which increased operational complexity and overhead. This update aims to simplify this process by allowing Azure to provision and manage the hosting infrastructure, thereby reducing the burden on developers and accelerating solution deployment.

---

**Specific Features and Detailed Changes**

- **Bring-Your-Own Image Support:** Developers can now deploy custom container images to the hosted MCP server within the Azure Connector Namespace. This enables greater flexibility and customization, allowing AI agents to interact with tools tailored to specific business requirements.
- **Cosmos DB MCP Server Integration:** The update introduces support for Cosmos DB as a backend for the MCP server, facilitating scalable and reliable data storage and retrieval for AI agent operations.
- **Platform-Managed Hosting:** Azure provisions and manages the underlying hosting infrastructure for MCP servers, eliminating the need for developers to operate their own hosting stack.
- **Microsoft Entr Integration:** The platform leverages Microsoft Entr for authentication and access control, ensuring secure interactions between AI agents and hosted tools.

---

**Technical Mechanisms and Implementation Methods**

- **Container Deployment:** Developers provide their own container images, which are deployed to the MCP server hosted within the Azure Connector Namespace. Azure manages the lifecycle of these containers, including provisioning, scaling, and monitoring.
- **Cosmos DB Backend:** The MCP server can be configured to use Azure Cosmos DB as its data store, enabling high availability, global distribution, and low-latency access for AI agent data operations.
- **Entr-Based Authentication:** Microsoft Entr is used to authenticate and authorize access to the MCP server, ensuring secure communication between AI agents and the hosted tools.
- **Infrastructure Automation:** Azure automates the provisioning and management of the hosting environment, including networking, storage, and compute resources, through the Connector Namespace.

---

**Use Cases and Application Scenarios**

- **AI Agent Tool Integration:** Enterprises can rapidly integrate custom tools and services with AI agents without building and maintaining a separate hosting stack.
- **Custom Workflows:** Organizations can deploy specialized container images to support unique business workflows, leveraging Cosmos DB for scalable data management.
- **Secure Multi-Agent Collaboration:** Multiple AI agents can securely access shared tools and data through Entr-based authentication and Azure-managed hosting.

---

**Important Considerations and Limitations**

- **Public Preview Status:** The feature is currently in public preview, which may entail limited support and potential changes before general availability.
- **Container Image Requirements:** Developers must ensure their container images are compatible with the hosted MCP server environment.
- **Cosmos DB Configuration:** Proper configuration of Cosmos DB is required for optimal performance and reliability.
- **Entr Integration:** Organizations must have Microsoft Entr configured for secure access control.

---

**Integration with Related Azure Services**

- **Azure Cosmos DB:** Used as the backend data store for MCP server operations.
- **Azure Container Services:** Utilized for deploying and managing custom container images.
- **Microsoft Entr:** Provides authentication and access control for AI agent interactions.
- **Azure Connector Namespace:** Acts as the orchestration layer for hosting MCP servers and managing infrastructure.

---

**Summary Sentence**

Azure Connector Namespace’s hosted MCP server capability in public preview enables developers to deploy custom container images and integrate Cosmos DB as a backend, providing AI agents with secure tool access through platform-managed hosting and Microsoft Entr authentication, thereby reducing operational overhead and accelerating solution deployment.

---

### 96. Generally Available: Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB](https://azure.microsoft.com/updates?id=579388)

**Update ID**: 579388
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB is now generally available. This is Microsoft’s new, fully-managed, cloud-native PostgreSQL service optimized for high-performance, AI-driven, and large-scale workloads.

- Key changes or new features  
HorizonDB offers ultra-low latency and high scalability, supporting demanding workloads such as AI/ML, real-time analytics, and mission-critical applications. It integrates advanced PostgreSQL compatibility, enhanced performance tuning, and built-in support for distributed architectures. The service includes automated scaling, robust security, and seamless integration with Azure ecosystem services (e.g., Azure AI, Data Lake, and Synapse). Developers benefit from native PostgreSQL tooling and APIs, while IT professionals gain simplified management, monitoring, and disaster recovery capabilities.

- Target audience affected  
Developers building AI, analytics, and high-throughput applications; IT professionals managing large-scale databases and cloud infrastructure; organizations requiring enterprise-grade PostgreSQL with Azure-native features.

- Important notes if any  
HorizonDB is designed for workloads that demand ultra-low latency and high concurrency. Migration tools are available for existing PostgreSQL databases. Pricing and regional availability details are published on the Azure website. For optimal use, review compatibility and integration guidelines with Azure services.

**Details**:

**Azure Update Summary: Generally Available: Azure HorizonDB**

**Background and Purpose of the Update**  
Azure HorizonDB is now generally available as Microsoft’s next-generation, fully-managed, cloud-native PostgreSQL service. The primary purpose of this release is to address the growing demand for high-performance, AI-driven, and large-scale database workloads in the cloud. HorizonDB is designed to deliver ultra-low latency and high scalability, targeting modern applications that require robust data processing capabilities and seamless integration with AI workloads.

**Specific Features and Detailed Changes**  
- **Fully-Managed Service**: HorizonDB automates database provisioning, patching, backups, and scaling, reducing operational overhead for IT teams.
- **Cloud-Native Architecture**: Built to leverage Azure’s cloud infrastructure, HorizonDB offers elastic scaling and high availability by default.
- **PostgreSQL Compatibility**: The service provides full compatibility with PostgreSQL, enabling organizations to migrate or extend existing PostgreSQL workloads to Azure without significant code changes.
- **High Performance**: Engineered for ultra-low latency, HorizonDB is optimized for workloads requiring rapid data access and processing.
- **AI-Driven Workloads**: The platform is tailored to support AI and machine learning scenarios, making it suitable for applications that require advanced analytics and real-time inference.
- **Large-Scale Workload Support**: HorizonDB is capable of handling massive datasets and concurrent connections, making it suitable for enterprise-scale deployments.

**Technical Mechanisms and Implementation Methods**  
Azure HorizonDB utilizes a cloud-native, distributed architecture that separates compute and storage layers, allowing for independent scaling and improved resource utilization. The service leverages Azure’s global network and managed infrastructure to ensure high availability and disaster recovery. Automated management features, such as self-healing and intelligent monitoring, are integrated to maintain optimal performance and reliability. PostgreSQL compatibility is maintained through adherence to open-source standards and APIs, ensuring seamless application integration.

**Use Cases and Application Scenarios**  
- **AI and Machine Learning**: HorizonDB is ideal for storing and processing large volumes of data required for training and inference in AI models.
- **Real-Time Analytics**: Applications that demand ultra-low latency analytics, such as financial services or IoT telemetry, benefit from HorizonDB’s performance optimizations.
- **Enterprise Applications**: Large-scale SaaS platforms or business applications requiring high concurrency and scalability can leverage HorizonDB’s managed environment.
- **Migration Projects**: Organizations seeking to modernize legacy PostgreSQL deployments can migrate to HorizonDB to take advantage of cloud-native features.

**Important Considerations and Limitations**  
- **Service Scope**: While HorizonDB offers PostgreSQL compatibility, users should validate support for specific extensions or custom configurations.
- **Operational Boundaries**: As a fully-managed service, certain administrative operations may be restricted compared to self-hosted PostgreSQL.
- **Performance Tuning**: Although optimized for performance, workload-specific tuning and benchmarking are recommended to achieve desired outcomes.

**Integration with Related Azure Services**  
HorizonDB integrates seamlessly with other Azure services, such as Azure AI, Azure Data Factory, and Azure Monitor, enabling end-to-end data pipelines, advanced analytics, and comprehensive monitoring. This integration streamlines the development of data-driven and AI-powered applications within the Azure ecosystem.

**Summary Sentence**  
Azure HorizonDB is now generally available, offering a fully-managed, cloud-native PostgreSQL service optimized for high-performance, AI-driven, and large-scale workloads, with seamless integration into the Azure platform.

---

### 97. Generally Available: Symmetric keys on Azure Key Vault Premium 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Symmetric keys on Azure Key Vault Premium ](https://azure.microsoft.com/updates?id=579374)

**Update ID**: 579374
**Data source**: Azure Updates API

**Categories**: Launched, Security, Key Vault, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Key Vault Premium now offers general availability for symmetric keys, specifically supporting the oct-HSM key type and the Advanced Encryption Standard (AES) algorithm.

- Key changes or new features  
Customers and partners can now generate, store, and use symmetric keys (AES) directly within Azure Key Vault Premium. This enables cryptographic operations such as encryption, decryption, and key wrapping/unwrapping using symmetric keys managed by Azure’s Hardware Security Modules (HSMs). The update moves the feature from public preview (July 2026) to full production support.

- Target audience affected  
Developers and IT professionals who require secure symmetric key management for applications, services, or workloads in Azure. This is particularly relevant for those implementing encryption, secure data exchange, or compliance-driven solutions.

- Important notes  
Symmetric key support is only available in Azure Key Vault Premium, not in Standard. Integration with oct-HSM and AES enables higher security and performance for cryptographic operations. Developers should review updated SDKs and API documentation for implementation details. Existing Key Vaults must be upgraded to Premium to use this feature.

**Details**:

**Azure Update Report: Generally Available - Symmetric Keys on Azure Key Vault Premium**

**Background and Purpose of the Update**  
Azure Key Vault is a core service for managing cryptographic keys, secrets, and certificates in the Azure ecosystem. Previously, Azure Key Vault primarily supported asymmetric keys for encryption and signing operations. With the public preview in July 2026, Microsoft introduced symmetric encryption capabilities, addressing the need for secure management of symmetric keys and cryptographic operations directly within Azure Key Vault. The purpose of this update is to make symmetric key support generally available, enabling customers and partners to leverage AES-based symmetric encryption with enhanced security and compliance.

**Specific Features and Detailed Changes**  
This update introduces the oct-HSM key type, which refers to symmetric keys stored and managed within Azure Key Vault’s Hardware Security Modules (HSMs). The Advanced Encryption Standard (AES) algorithm is now supported for symmetric encryption operations. Customers can generate, store, and use symmetric keys for cryptographic operations such as encryption, decryption, and key wrapping directly within Azure Key Vault Premium. The update transitions the symmetric key feature from public preview to general availability, ensuring production-grade reliability and support.

**Technical Mechanisms and Implementation Methods**  
Symmetric keys are provisioned as oct-HSM key types, meaning the key material is handled exclusively within HSM-backed Key Vaults, providing FIPS 140-2 Level 3 validated security. The AES algorithm is supported for cryptographic operations, allowing users to perform encryption and decryption without exposing key material outside the HSM boundary. Key management operations (creation, rotation, deletion) and cryptographic operations are accessible via Azure Key Vault REST APIs, Azure SDKs, and Azure CLI, ensuring seamless integration into automation and application workflows.

**Use Cases and Application Scenarios**  
- **Data Encryption:** Encrypting sensitive data at rest or in transit using AES symmetric keys managed in Azure Key Vault Premium.
- **Key Wrapping:** Securely wrapping and unwrapping other keys or secrets using AES symmetric keys, supporting scenarios such as secure key exchange.
- **Application Integration:** Applications requiring high-performance symmetric encryption can now utilize Azure Key Vault Premium for secure key management and cryptographic operations.
- **Compliance:** Organizations with strict regulatory requirements can leverage HSM-backed symmetric keys for enhanced security and auditability.

**Important Considerations and Limitations**  
- The symmetric key feature is available only in Azure Key Vault Premium, which is HSM-backed; it is not supported in standard Key Vault offerings.
- Only the AES algorithm is supported for symmetric keys; other symmetric algorithms are not mentioned in this update.
- Key material is never exposed outside the HSM boundary, ensuring compliance and security but requiring applications to use Key Vault APIs for cryptographic operations.
- Customers must ensure their applications and workflows are compatible with the oct-HSM key type and Key Vault Premium endpoints.

**Integration with Related Azure Services**  
Symmetric keys managed in Azure Key Vault Premium can be integrated with other Azure services that support Key Vault for encryption, such as Azure Storage, Azure SQL Database, and Azure Virtual Machines. This enables centralized key management and auditability across the Azure ecosystem. The update enhances the security posture of applications and services by leveraging HSM-backed symmetric keys for cryptographic operations.

**Summary Sentence**  
Azure Key Vault Premium now generally supports symmetric keys with oct-HSM key type and AES algorithm, enabling secure, HSM-backed symmetric encryption and key management for production workloads.

---

### 98. Public Preview: Azure Files NFS shares on HDD

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Files NFS shares on HDD](https://azure.microsoft.com/updates?id=579369)

**Update ID**: 579369
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Files, Microsoft Ignite, Pricing & Offerings, Feature

**Summary**:

- What was updated  
Azure Files now supports NFS (Network File System) shares on HDD storage in public preview.

- Key changes or new features  
Previously, Azure Files NFS shares were only available on SSD storage. This update introduces a cost-effective HDD option for NFS shares, providing fully managed file storage for Linux workloads. The HDD-based NFS shares are suitable for general-purpose applications, shared datasets, and backup scenarios where cost efficiency is prioritized over high performance.

- Target audience affected  
Developers and IT professionals managing Linux workloads on Azure, especially those seeking economical storage solutions for applications, data sharing, or backup use cases.

- Important notes if any  
This feature is currently in public preview, meaning it may not be recommended for production workloads until general availability. Users should evaluate performance characteristics and pricing compared to SSD-based NFS shares. The HDD option is ideal for workloads with moderate performance requirements and high storage capacity needs.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=579369

**Details**:

**Azure Update Report: Public Preview - Azure Files NFS Shares on HDD**

**Background and Purpose of the Update**  
Azure Files previously offered NFS (Network File System) shares exclusively on SSD-backed storage, targeting workloads requiring high performance. The new update introduces NFS shares on HDD-backed storage in public preview, aiming to provide a cost-effective, fully managed file storage solution for Linux workloads. This expansion addresses the needs of customers who prioritize storage capacity and cost efficiency over high IOPS and throughput, such as general-purpose applications, shared datasets, and backup scenarios.

**Specific Features and Detailed Changes**  
- **NFS Support on HDD**: Azure Files now allows creation and management of NFS shares on HDD-based storage accounts, in addition to existing SSD options.
- **Cost Efficiency**: HDD-backed NFS shares are optimized for workloads where lower storage costs are more important than performance, making them suitable for large-scale, less frequently accessed data.
- **Fully Managed Service**: The offering retains Azure Files’ fully managed nature, including automated maintenance, scalability, and integration with Azure’s security and management features.

**Technical Mechanisms and Implementation Methods**  
- **Storage Account Configuration**: Users can provision Azure Files storage accounts with HDD-based performance tiers and enable NFS protocol support during setup.
- **NFS Protocol Version**: The update continues to leverage NFS protocol support, which is essential for Linux-based workloads requiring native file system compatibility.
- **Management and Access**: Shares are managed through Azure Portal, CLI, or REST APIs, and can be mounted directly onto Linux VMs or containers using standard NFS client tools.
- **Performance Characteristics**: HDD-backed shares offer lower IOPS and throughput compared to SSD, but provide larger capacity at reduced cost, suitable for workloads with moderate performance requirements.

**Use Cases and Application Scenarios**  
- **General-Purpose Applications**: Applications that require shared file storage but do not demand high performance, such as content repositories or collaboration tools.
- **Shared Datasets**: Data sets accessed by multiple Linux VMs or containers, where access frequency is moderate and cost is a primary concern.
- **Backup and Archival**: Storage of backup files or archival data where retrieval speed is less critical, but storage capacity and cost efficiency are important.

**Important Considerations and Limitations**  
- **Performance**: HDD-backed NFS shares are not suitable for high-performance workloads; users should evaluate IOPS and throughput requirements before migration.
- **Preview Status**: The feature is in public preview, meaning it may not be recommended for production workloads and could be subject to changes or limitations.
- **Protocol Support**: Only NFS protocol is supported for HDD-backed shares; SMB protocol is not mentioned in this update.
- **Regional Availability**: As with most previews, availability may be limited to specific Azure regions.

**Integration with Related Azure Services**  
- **Azure Virtual Machines and Containers**: NFS shares can be mounted onto Linux-based Azure VMs and container instances, facilitating integration with compute resources.
- **Azure Backup and Data Management Solutions**: HDD-backed NFS shares can serve as storage targets for backup solutions, archival, or data management workflows.
- **Security and Management**: Integration with Azure’s identity, access management, and monitoring capabilities remains consistent with other Azure Files offerings.

**Summary Sentence**  
Azure Files now offers NFS shares on HDD in public preview, providing a cost-effective, fully managed storage solution for Linux workloads where performance is less critical, such as general-purpose applications, shared datasets, and backups.

---

### 99. Public Preview: Azure SQL updates for mid-November 2026 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure SQL updates for mid-November 2026 ](https://azure.microsoft.com/updates?id=579359)

**Update ID**: 579359
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL received updates in mid-November 2026, specifically enhancements to SQL Server Management Studio (SSMS) for handling .dacpac and .bacpac files.

- Key changes or new features  
A new "Create and Apply" wizard was introduced in SSMS, streamlining the process of creating and deploying .dacpac and .bacpac files. This feature consolidates and replaces previous methods, offering a simplified and more intuitive workflow for database deployment and migration tasks.

- Target audience affected  
Developers and IT professionals who use SSMS for Azure SQL database management, especially those involved in database development, deployment, and migration processes.

- Important notes if any  
The new wizard replaces older approaches for working with .dacpac and .bacpac files, so users should familiarize themselves with the updated workflow. This change aims to reduce complexity and improve efficiency in database operations. Existing scripts or automation relying on previous methods may require review and adjustment to align with the new wizard functionality.

**Details**:

**Azure Update Report: Public Preview – Azure SQL Updates for Mid-November 2026**

**Background and Purpose of the Update:**  
The mid-November 2026 update for Azure SQL introduces enhancements to the management of database deployment and migration artifacts within SQL Server Management Studio (SSMS). The primary goal is to streamline and simplify the processes associated with creating and applying Data-tier Application Package (.dacpac) and Backup Package (.bacpac) files. These files are essential for database development, deployment, and migration workflows in Azure SQL environments.

**Specific Features and Detailed Changes:**  
- **New Create and Apply Wizards in SSMS:**  
  The update introduces dedicated wizards in SSMS for both creating and applying .dacpac and .bacpac files. These wizards provide a guided, user-friendly interface, consolidating and replacing previous variable or fragmented workflows.
- **Consolidation of Functionality:**  
  The new wizards unify the process, making it easier for users to generate and utilize .dacpac and .bacpac files without navigating through multiple tools or manual steps.

**Technical Mechanisms and Implementation Methods:**  
- **Wizard-Based Workflow:**  
  The implementation leverages SSMS’s extensibility to provide step-by-step wizards. These wizards abstract the underlying complexity of schema extraction, data export, and deployment, presenting users with a streamlined set of options and validations.
- **File Handling:**  
  The creation wizard facilitates the generation of .dacpac files (containing schema and optionally data) and .bacpac files (containing both schema and data for full database export). The apply wizard enables users to deploy these packages to Azure SQL Database or SQL Server instances, handling compatibility checks and deployment steps internally.
- **Replacement of Legacy Methods:**  
  By consolidating previous methods, the new wizards reduce the risk of errors and inconsistencies that could arise from manual or script-based approaches.

**Use Cases and Application Scenarios:**  
- **Database Development and CI/CD:**  
  Developers can use the new wizards to package database schema changes as .dacpac files for integration into DevOps pipelines, enabling repeatable and automated deployments to Azure SQL environments.
- **Database Migration:**  
  The .bacpac creation and application process is essential for migrating databases from on-premises SQL Server to Azure SQL Database or Azure SQL Managed Instance.
- **Backup and Restore:**  
  The simplified export and import of .bacpac files support backup and restore scenarios, especially for moving databases between environments.

**Important Considerations and Limitations:**  
- **Public Preview Status:**  
  As this feature is in public preview, it may not be suitable for production workloads. Users should validate workflows in test environments and monitor for updates or changes before full adoption.
- **Feature Scope:**  
  The update specifically targets the creation and application of .dacpac and .bacpac files within SSMS. Other deployment or migration tools and methods remain unchanged.

**Integration with Related Azure Services:**  
- **Azure SQL Database and Managed Instance:**  
  The wizards are designed to work seamlessly with Azure SQL Database and Azure SQL Managed Instance, supporting common deployment and migration scenarios.
- **DevOps Integration:**  
  While the wizards are primarily GUI-based, the .dacpac and .bacpac files they produce can be integrated into broader DevOps pipelines using Azure DevOps or GitHub Actions for automated deployments.

**Summary Sentence:**  
In mid-November 2026, Azure SQL introduced new SSMS wizards in public preview to simplify and unify the creation and application of .dacpac and .bacpac files, enhancing database deployment and migration workflows for Azure SQL environments.

---

### 100. Generally Available: Azure DocumentDB elasticity—query from any node 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure DocumentDB elasticity—query from any node ](https://azure.microsoft.com/updates?id=579354)

**Update ID**: 579354
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DocumentDB now supports elasticity by allowing queries to be sent to any node in a multi-shard cluster. This feature is now generally available.

- Key changes or new features  
Nodes in a multi-shard DocumentDB cluster can accept queries from clients and either process them locally or route them to the appropriate shard(s) containing the requested data. This means every node acts as a router, improving query flexibility and reducing dependency on specific nodes. The update enhances scalability and simplifies client-side logic for querying distributed data.

- Target audience affected  
Developers building distributed applications on Azure DocumentDB and IT professionals managing multi-shard DocumentDB clusters.

- Important notes if any  
This update improves cluster resilience and performance by enabling load balancing across all nodes. Developers no longer need to target specific nodes for queries, which simplifies application architecture and reduces operational complexity. Existing APIs and client libraries should be reviewed to ensure compatibility with the new routing behavior.

**Details**:

**Comprehensive Technical Explanation: Azure DocumentDB Elasticity—Query from Any Node (Generally Available)**

**Background and Purpose of the Update**  
Azure DocumentDB, a NoSQL database service, is designed to provide high scalability and performance for document-oriented data. In multi-shard clusters, data is distributed across multiple nodes (shards) to handle large datasets and high throughput. Traditionally, queries needed to be directed to specific nodes or shards containing the relevant data, which could complicate client logic and reduce flexibility. The purpose of this update is to simplify the query process by enabling any node in a multi-shard cluster to accept queries, thereby improving elasticity, scalability, and ease of use.

**Specific Features and Detailed Changes**  
With this update, Azure DocumentDB now allows users to send queries to any node within a multi-shard cluster. Each node is capable of either processing the query locally if the data resides on that node, or routing the query to the appropriate shard(s) that contain the required data. This change transforms every node in the cluster into a router, eliminating the need for clients to be aware of shard locations or to manage query routing themselves.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages a routing mechanism embedded within each node. When a query is received, the node determines whether it can fulfill the request locally. If not, it programmatically forwards the query to the relevant shard(s) using internal cluster communication protocols. This routing is transparent to the client, which interacts with any node as if it were the entry point to the entire cluster. The mechanism ensures that queries are efficiently directed to the correct location, minimizing latency and maximizing throughput.

**Use Cases and Application Scenarios**  
- **Simplified Client Architecture:** Applications no longer need to track shard mappings or implement custom routing logic, reducing development complexity and potential errors.
- **Load Balancing:** Queries can be distributed across all nodes, enabling more effective load balancing and resource utilization.
- **High Availability:** If a node fails, queries can be sent to any other node, improving fault tolerance and system resilience.
- **Scalable Microservices:** Microservices architectures can interact with DocumentDB clusters without shard-awareness, facilitating easier scaling and deployment.

**Important Considerations and Limitations**  
- **Query Routing Overhead:** While routing is transparent, there may be minor overhead associated with forwarding queries between nodes, especially for cross-shard queries.
- **Consistency and Latency:** Depending on the cluster configuration and the nature of the query, there may be differences in latency or consistency guarantees when queries are routed versus processed locally.
- **Security and Access Control:** Ensure that access controls and authentication are properly configured, as any node can now serve as a query entry point.

**Integration with Related Azure Services**  
Azure DocumentDB’s enhanced elasticity integrates seamlessly with other Azure services. For example, it works well with Azure Application Gateway for load balancing, Azure Functions for serverless query processing, and Azure Monitor for tracking query performance and node health. The update also complements Azure’s scaling and high-availability features, making DocumentDB clusters more robust and easier to manage in cloud-native architectures.

**Summary Sentence**  
Azure DocumentDB now allows queries to be sent to any node in a multi-shard cluster, with each node capable of processing or routing the query as needed, thereby simplifying client logic, enhancing elasticity, and improving scalability for distributed applications.

---

### 101. Public Preview: Azure Application Gateway advanced routing rules 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Application Gateway advanced routing rules ](https://azure.microsoft.com/updates?id=579324)

**Update ID**: 579324
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Application Gateway now supports advanced routing rules in public preview.

- Key changes or new features  
Advanced routing rules allow users to define flexible, condition-based routing logic using HTTP request attributes (such as headers, query strings, and cookies). This extends routing capabilities beyond traditional path-based routing, enabling more granular control over how requests are directed to backend targets. Developers and IT professionals can now implement complex routing scenarios, such as routing based on user agent, custom headers, or specific query parameters.

- Target audience affected  
Developers and IT professionals managing web applications, APIs, or microservices behind Azure Application Gateway. Teams requiring advanced traffic management, personalized user experiences, or multi-tenant architectures will benefit most.

- Important notes  
This feature is currently in public preview and may not be suitable for production workloads until general availability. Existing Application Gateway configurations remain compatible, but advanced routing rules require additional setup. Users should review documentation for guidance on implementing and testing new routing logic.  
For more information, visit the official Azure update page: https://azure.microsoft.com/updates?id=579324

**Details**:

**Azure Update Report: Public Preview – Azure Application Gateway Advanced Routing Rules**

**Background and Purpose of the Update**  
Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. Traditionally, routing rules in Application Gateway have been limited to basic path-based or host-based routing. The purpose of this update is to introduce advanced routing rules, allowing for more granular and flexible routing logic based on HTTP request attributes. This enhancement aims to address scenarios where traditional routing mechanisms are insufficient, enabling IT professionals to implement complex routing strategies directly within Application Gateway.

**Specific Features and Detailed Changes**  
With the introduction of advanced routing rules in public preview, users can now define routing logic using a broader set of HTTP request attributes. This includes, but is not limited to, HTTP headers, query strings, and other request parameters. The update extends routing capabilities beyond simple path or host matching, allowing for condition-based routing. For example, you can route requests based on the presence or value of specific headers, query parameters, or combinations thereof. This flexibility enables more precise control over how incoming traffic is directed to backend pools.

**Technical Mechanisms and Implementation Methods**  
The advanced routing rules are implemented as part of the Application Gateway configuration. Administrators can define rules using a declarative syntax that specifies conditions based on HTTP request attributes. When a request is received, Application Gateway evaluates these conditions and applies the corresponding routing logic. The mechanism leverages the Application Gateway’s inspection of HTTP requests at Layer 7, enabling deep packet inspection and conditional routing. Configuration can be performed via Azure Portal, ARM templates, or CLI, ensuring integration with existing infrastructure-as-code workflows.

**Use Cases and Application Scenarios**  
Advanced routing rules are particularly useful in scenarios requiring dynamic routing based on client or request characteristics. Common use cases include:
- Routing requests to specific backend pools based on custom headers (e.g., device type, authentication tokens).
- Implementing A/B testing by routing traffic based on query parameters or cookies.
- Segregating traffic for different API versions using version indicators in headers or query strings.
- Directing traffic based on geographic or language preferences specified in request headers.

These scenarios are prevalent in modern web applications, microservices architectures, and environments where personalized or context-aware routing is required.

**Important Considerations and Limitations**  
As this feature is currently in public preview, it may not be suitable for production workloads. IT professionals should be aware of potential limitations, such as incomplete feature support, possible changes in syntax or behavior before general availability, and limited documentation or support. Additionally, performance implications should be considered, as advanced routing rules may introduce additional processing overhead due to deep inspection of HTTP request attributes.

**Integration with Related Azure Services**  
Advanced routing rules seamlessly integrate with other Azure services commonly used alongside Application Gateway, such as Azure Web Apps, Azure Kubernetes Service (AKS), and Azure Functions. This update enhances the ability to implement sophisticated routing logic in front of these services, supporting scenarios like blue/green deployments, API versioning, and multi-tenant architectures. Configuration and management remain consistent with existing Azure workflows, ensuring compatibility with Azure Resource Manager and automation tools.

**Summary Sentence**  
Azure Application Gateway advanced routing rules, now in public preview, provide IT professionals with enhanced, condition-based routing capabilities using HTTP request attributes, enabling more flexible and granular traffic management for modern application architectures.

---

### 102. Public Preview: AI Assisted Oracle-to-PostgreSQL Application Code Migration

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: AI Assisted Oracle-to-PostgreSQL Application Code Migration](https://azure.microsoft.com/updates?id=579231)

**Update ID**: 579231
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure has released a public preview of an AI-assisted plugin for Oracle-to-PostgreSQL application code migration.

- Key changes or new features  
The new plugin leverages AI to help developers convert application code from Oracle to PostgreSQL, facilitating migration to Azure Database for PostgreSQL. It is accessible via GitHub Copilot CLI and Visual Studio Code, streamlining the migration process by providing automated code conversion and guidance.

- Target audience affected  
This update is relevant for developers and IT professionals involved in database migration projects, particularly those moving applications from Oracle to PostgreSQL on Azure.

- Important notes if any  
The plugin is currently in public preview, so it may not be suitable for production workloads yet. Users should validate converted code and test thoroughly before deployment. The integration with popular developer tools (GitHub Copilot CLI and VS Code) makes it easier to adopt within existing workflows. This feature aims to reduce manual effort and accelerate migration timelines. For more details and access, refer to the official Azure update link.

**Details**:

**Azure Update Report: Public Preview – AI Assisted Oracle-to-PostgreSQL Application Code Migration**

**Background and Purpose of the Update**  
This update introduces a public preview of an AI-assisted plugin designed to facilitate the migration of application code from Oracle to PostgreSQL. The primary purpose is to streamline the process of adapting applications to work with Azure Database for PostgreSQL, addressing the challenges of manual code conversion and reducing migration complexity for organizations transitioning from Oracle-based solutions.

**Specific Features and Detailed Changes**  
The plugin leverages AI-assisted skills to automate and enhance the code conversion process. It is accessible through two main interfaces: GitHub Copilot CLI and Visual Studio Code. This integration allows developers to invoke the plugin directly within their development environments, enabling real-time code conversion and assistance. The plugin specifically targets application code, focusing on transforming Oracle-specific constructs, syntax, and database interactions into their PostgreSQL equivalents.

**Technical Mechanisms and Implementation Methods**  
The plugin utilizes AI models to analyze Oracle application code and generate PostgreSQL-compatible code. When invoked via GitHub Copilot CLI or Visual Studio Code, the plugin scans the source code, identifies Oracle-specific patterns (such as PL/SQL syntax, proprietary functions, and data types), and suggests or applies equivalent PostgreSQL constructs. The AI-assisted approach reduces manual intervention, offering context-aware recommendations and automated code transformations. The plugin is designed to work seamlessly within the developer workflow, leveraging the capabilities of Copilot and VS Code extensions for code editing, review, and migration.

**Use Cases and Application Scenarios**  
Typical use cases include organizations seeking to migrate legacy Oracle applications to Azure Database for PostgreSQL, either as part of cloud modernization initiatives or cost optimization strategies. The plugin is well-suited for scenarios where application code contains significant Oracle-specific logic that must be adapted for PostgreSQL compatibility. It is particularly valuable for development teams tasked with refactoring database interaction layers, stored procedures, and custom business logic during migration projects.

**Important Considerations and Limitations**  
As this feature is in public preview, users should be aware of potential limitations regarding coverage and accuracy. Not all Oracle constructs may be fully supported or converted, and manual review of AI-generated code is recommended to ensure correctness and performance. The plugin's effectiveness depends on the complexity of the source code and the specific Oracle features used. Additionally, preview features may lack production-level support and should be validated in test environments before deployment.

**Integration with Related Azure Services**  
The plugin is designed to support migration to Azure Database for PostgreSQL, enabling seamless integration with Azure’s managed PostgreSQL offerings. By converting application code to be PostgreSQL-compatible, it facilitates the adoption of Azure’s database services, allowing organizations to leverage Azure’s scalability, security, and management capabilities. The integration with GitHub Copilot CLI and Visual Studio Code aligns with Azure’s broader ecosystem of developer tools and services, enhancing productivity and migration efficiency.

**Summary Sentence**  
The public preview of Azure’s AI-assisted Oracle-to-PostgreSQL application code migration plugin provides developers with automated code conversion capabilities via GitHub Copilot CLI and Visual Studio Code, streamlining the transition of Oracle-based applications to Azure Database for PostgreSQL while offering integration with Azure’s developer tools and managed database services.

---

### 103. Public Preview: Migrate Oracle databases to Azure HorizonDB using Azure Database Migration Service

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Migrate Oracle databases to Azure HorizonDB using Azure Database Migration Service](https://azure.microsoft.com/updates?id=579226)

**Update ID**: 579226
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database Migration Service (DMS) now supports public preview for migrating Oracle databases to Azure HorizonDB.

- Key changes or new features  
Developers and IT professionals can use DMS to configure source (Oracle) and target (Azure HorizonDB) connections, select specific schemas for migration, initiate data transfer, and monitor migration progress—all within a unified interface. The migration workflow is streamlined, eliminating the need for multiple tools or manual steps. This update enables end-to-end schema and data migration from Oracle to Azure HorizonDB, supporting both initial data loads and ongoing progress tracking.

- Target audience affected  
Database administrators, IT professionals, and developers responsible for Oracle database migrations to Azure HorizonDB.

- Important notes  
This feature is currently in public preview, so it may not be recommended for production workloads. Users should validate migration outcomes and monitor for any issues during the preview phase. The update simplifies migration processes, reducing complexity and potential downtime. For more details and guidance, refer to the official Azure update documentation: [Azure Update Link](https://azure.microsoft.com/updates?id=579226).

**Details**:

**Azure Update Report: Public Preview – Migrate Oracle Databases to Azure HorizonDB using Azure Database Migration Service**

**Background and Purpose of the Update:**  
This update introduces public preview support for migrating Oracle databases to Azure HorizonDB using Azure Database Migration Service (DMS). The primary objective is to streamline and simplify the migration process for organizations seeking to modernize their data infrastructure by moving from Oracle environments to Azure HorizonDB, leveraging a unified migration experience.

**Specific Features and Detailed Changes:**  
- **Oracle-to-Azure HorizonDB Migration Support:** DMS now allows direct migration from Oracle database sources to Azure HorizonDB targets.
- **Unified Migration Workflow:** Users can configure both source (Oracle) and target (Azure HorizonDB) connections within a single interface.
- **Schema Selection:** The service enables selection of specific schemas to migrate, providing granular control over the migration scope.
- **Data Transfer Initiation:** Migration jobs can be initiated directly from the DMS interface.
- **Progress Tracking:** The migration process can be monitored end-to-end within the same experience, offering visibility into migration status and progress.

**Technical Mechanisms and Implementation Methods:**  
- **Connection Configuration:** DMS requires users to input connection details for both the Oracle source and Azure HorizonDB target. This typically involves specifying hostnames, authentication credentials, and network settings.
- **Schema Mapping and Selection:** The tool presents available schemas from the Oracle source, allowing users to choose which schemas to include in the migration. This step may involve mapping Oracle schema objects to their equivalents in Azure HorizonDB.
- **Data Movement:** Upon initiation, DMS orchestrates the extraction of data from Oracle, transformation as needed, and loading into Azure HorizonDB. The process is managed within the DMS platform, abstracting much of the complexity from the user.
- **Monitoring and Logging:** Progress and status updates are available through the DMS interface, enabling users to track the migration and respond to any issues.

**Use Cases and Application Scenarios:**  
- **Database Modernization:** Organizations seeking to move legacy Oracle workloads to a cloud-native platform like Azure HorizonDB can leverage this capability for a streamlined migration.
- **Consolidation Projects:** Enterprises consolidating disparate Oracle instances into Azure HorizonDB for centralized management and scalability.
- **Cloud Adoption:** Businesses migrating on-premises Oracle databases to Azure as part of broader cloud adoption or digital transformation initiatives.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate and test thoroughly before relying on it for mission-critical migrations.
- **Scope of Migration:** Only data and schemas selected within the DMS interface will be migrated. Users must ensure all necessary objects are included.
- **Feature Completeness:** Some advanced Oracle features or complex schema elements may not be fully supported in the preview. Users should review migration reports and validate post-migration integrity.

**Integration with Related Azure Services:**  
- **Azure HorizonDB:** The migration targets Azure HorizonDB, enabling integration with other Azure data services post-migration.
- **Azure Database Migration Service:** The entire migration process is managed through DMS, which can be orchestrated alongside other Azure migration and management tools.
- **Monitoring and Management:** Post-migration, users can leverage Azure Monitor and other management tools to oversee their HorizonDB instances.

**Summary Sentence:**  
Azure Database Migration Service now offers a unified, preview experience for migrating Oracle databases to Azure HorizonDB, enabling schema selection, data transfer, and progress tracking within a single interface to support database modernization initiatives.

---

### 104. Generally Available: Database Hub in Microsoft Fabric

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Database Hub in Microsoft Fabric](https://azure.microsoft.com/updates?id=579216)

**Update ID**: 579216
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Database Hub in Microsoft Fabric is now generally available.

- Key changes or new features  
Database Hub provides a unified platform for discovering, managing, monitoring, and optimizing databases across multiple sources, including SQL Server, Azure SQL, PostgreSQL, Azure Cosmos DB, and Fabric SQL. The hub integrates AI-powered insights and agents to streamline database operations, offering enhanced visibility and actionable recommendations for performance tuning, security, and cost optimization. Users can access consolidated dashboards, automate routine tasks, and leverage intelligent alerts for proactive management.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals managing multi-cloud or hybrid database environments, especially those using Microsoft Fabric and various database platforms.

- Important notes  
Database Hub simplifies cross-database management and monitoring, reducing operational complexity and improving efficiency. Integration with AI capabilities helps identify issues and optimize resources faster. Organizations can leverage this unified experience to improve database governance and accelerate troubleshooting. For more information, visit the official Azure update page: https://azure.microsoft.com/updates?id=579216

**Details**:

**Azure Update Report: Database Hub in Microsoft Fabric – General Availability**

**Background and Purpose of the Update**  
The general availability of Database Hub in Microsoft Fabric addresses the growing need for centralized database management across hybrid and multi-cloud environments. As organizations increasingly deploy diverse database engines—including SQL Server, Azure SQL, PostgreSQL, Azure Cosmos DB, and Fabric SQL—there is a demand for a unified platform to streamline discovery, management, monitoring, and optimization. This update aims to consolidate database operations, reduce administrative overhead, and enhance data governance by providing a single pane of glass for database lifecycle management.

**Specific Features and Detailed Changes**  
Database Hub introduces a unified experience for IT professionals to interact with multiple database types. Key features include:

- **Discovery:** Automatic identification and cataloging of databases across supported platforms.
- **Management:** Centralized controls for provisioning, configuring, and maintaining databases, regardless of their underlying engine.
- **Monitoring:** Real-time visibility into performance metrics, health status, and resource utilization for all integrated databases.
- **Optimization:** AI-powered insights and agents offer recommendations for performance tuning, cost optimization, and anomaly detection.
- **Support for Multiple Engines:** Native integration with SQL Server, Azure SQL, PostgreSQL, Azure Cosmos DB, and Fabric SQL, enabling consistent operations across heterogeneous environments.

**Technical Mechanisms and Implementation Methods**  
Database Hub leverages Microsoft Fabric’s orchestration layer to aggregate metadata and telemetry from connected database instances. AI-powered agents analyze collected data to generate actionable insights. The platform uses secure connectors and APIs to interface with each database engine, ensuring seamless integration and consistent management workflows. Monitoring and optimization are facilitated through Fabric’s analytics and automation capabilities, which apply machine learning models to identify trends and recommend improvements.

**Use Cases and Application Scenarios**  
- **Hybrid Database Management:** Enterprises managing both on-premises SQL Server and cloud-based Azure SQL can use Database Hub to unify operations and reduce complexity.
- **Cross-Platform Monitoring:** Organizations deploying PostgreSQL and Azure Cosmos DB can leverage centralized monitoring for proactive issue resolution.
- **Performance Optimization:** Database administrators can utilize AI-driven recommendations to tune queries, indexes, and resource allocation across all supported databases.
- **Compliance and Governance:** Database Hub provides visibility and control necessary for regulatory compliance, data protection, and audit requirements.

**Important Considerations and Limitations**  
- **Supported Engines:** The platform currently supports SQL Server, Azure SQL, PostgreSQL, Azure Cosmos DB, and Fabric SQL. Databases outside these engines may require separate management solutions.
- **AI Insights:** The effectiveness of AI-powered recommendations depends on the quality and completeness of telemetry data collected from each database.
- **Security and Access Control:** Proper configuration of permissions and access policies is essential to ensure secure integration and prevent unauthorized operations.

**Integration with Related Azure Services**  
Database Hub is tightly integrated with Microsoft Fabric, leveraging its orchestration, analytics, and automation capabilities. It complements Azure SQL, Azure Cosmos DB, and other Azure database services by providing a unified management interface. The platform can also interface with Azure Monitor for extended telemetry and alerting, and Azure Security Center for enhanced security posture management.

**Summary Sentence**  
Database Hub in Microsoft Fabric is now generally available, offering IT professionals a unified, AI-powered platform for discovering, managing, monitoring, and optimizing databases across SQL Server, Azure SQL, PostgreSQL, Azure Cosmos DB, and Fabric SQL.

---

### 105. Generally Available: Azure Backup for Azure Cosmos DB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Backup for Azure Cosmos DB](https://azure.microsoft.com/updates?id=579147)

**Update ID**: 579147
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Storage, Databases, Internet of Things, Azure Backup, Azure Cosmos DB, Microsoft Ignite

**Summary**:

- What was updated  
Azure Backup for Azure Cosmos DB is now generally available.

- Key changes or new features  
The new feature enables vaulted backup for Azure Cosmos DB accounts, providing immutable, long-term backups stored in a logically air-gapped backup vault. This vault is isolated from the production environment, enhancing data protection against accidental deletion, ransomware, and other threats. The solution supports automated backup scheduling, retention management, and secure restore capabilities.

- Target audience affected  
Developers and IT professionals managing Azure Cosmos DB accounts, especially those responsible for data protection, compliance, and disaster recovery.

- Important notes  
Vaulted backups are isolated from production, offering an extra layer of security. This feature is critical for organizations requiring compliance with strict data retention and immutability standards. Integration with Azure Backup simplifies backup management and ensures reliable recovery options for Cosmos DB data. Review documentation for configuration steps and best practices.

**Details**:

**Azure Update Report: Generally Available – Azure Backup for Azure Cosmos DB**

**Background and Purpose of the Update**  
Azure Backup for Azure Cosmos DB is now generally available. The primary purpose of this update is to provide a robust, enterprise-grade backup solution for Azure Cosmos DB accounts. This addresses the growing need for secure, long-term, and immutable backups of mission-critical NoSQL data in the cloud, ensuring organizations can meet compliance, retention, and disaster recovery requirements.

**Specific Features and Detailed Changes**  
The new Azure Backup for Azure Cosmos DB introduces "vaulted backup," which enables the protection of Cosmos DB accounts through immutable, long-term backups. These backups are stored in a logically air-gapped backup vault, which is isolated from the production environment. This separation enhances data security by preventing unauthorized access or accidental deletion of backup data. The feature set includes:

- Immutable backups: Ensures backup data cannot be altered or deleted before the retention period expires.
- Long-term retention: Supports storing backups for extended periods to meet regulatory and business requirements.
- Logical air-gap: Backups are stored in a backup vault that is logically separated from the source Cosmos DB account.

**Technical Mechanisms and Implementation Methods**  
The vaulted backup mechanism leverages Azure Backup’s architecture, where backup data is transferred from the Cosmos DB account to a dedicated backup vault. This vault is logically isolated from the production environment, providing an additional security boundary. Immutability is enforced at the vault level, ensuring that once a backup is created, it cannot be modified or deleted until the retention policy allows. This approach mitigates risks such as ransomware attacks or insider threats. The backup process is managed through Azure Backup, which orchestrates backup scheduling, retention, and recovery operations.

**Use Cases and Application Scenarios**  
Azure Backup for Azure Cosmos DB is suitable for scenarios including:

- Regulatory compliance: Organizations needing to retain data for long periods to comply with industry regulations.
- Disaster recovery: Rapid restoration of Cosmos DB data in the event of accidental deletion, corruption, or malicious attacks.
- Business continuity: Ensuring data availability and integrity for critical applications relying on Cosmos DB.
- Audit and investigation: Providing immutable backup copies for forensic analysis or legal holds.

**Important Considerations and Limitations**  
- The backup vault is logically air-gapped, not physically isolated; it provides strong security but is not a substitute for physical separation.
- Immutability is enforced by Azure Backup policies; ensure retention settings align with organizational requirements.
- Backup and restore operations may have performance or cost implications depending on data size and frequency.
- Integration with existing backup workflows and monitoring should be planned to ensure operational consistency.

**Integration with Related Azure Services**  
Azure Backup for Azure Cosmos DB integrates with Azure Backup’s centralized management and monitoring capabilities. Backups are managed through the Azure Backup vault, which can also protect other Azure resources, enabling unified backup management across services. The solution complements native Cosmos DB features, such as point-in-time restore, by providing additional layers of protection and retention.

**Summary Sentence**  
Azure Backup for Azure Cosmos DB is now generally available, providing immutable, long-term, and logically air-gapped backups for Cosmos DB accounts, enhancing data protection and compliance capabilities for enterprise workloads.

---

### 106. Generally Available: Smart Tier (Azure Blob and Data Lake Storage) in Azure Government and China regions

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Smart Tier (Azure Blob and Data Lake Storage) in Azure Government and China regions](https://azure.microsoft.com/updates?id=579040)

**Update ID**: 579040
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Smart Tier for Azure Blob Storage and Azure Data Lake Storage (ADLS) is now generally available in Azure Government and China regions.

- Key changes or new features  
Smart Tier provides fully managed, automated data tiering for object storage in standard online tiers. It eliminates the need for manual tier selection by automatically placing data in the most cost-effective tier based on usage patterns. This helps optimize storage costs and simplifies data management.

- Target audience affected  
Developers and IT professionals working with Azure Blob Storage or ADLS in Azure Government and China regions, especially those managing large datasets or requiring cost optimization.

- Important notes  
Smart Tier is now available in these sovereign regions, aligning with compliance and regulatory requirements. No manual intervention is needed for tier placement, reducing operational overhead. Existing APIs and workflows for Blob and ADLS storage remain compatible, so integration is straightforward. For more details, refer to the official Azure Update [link](https://azure.microsoft.com/updates?id=579040).

**Details**:

**Azure Update Report: Generally Available – Smart Tier (Azure Blob and Data Lake Storage) in Azure Government and China Regions**

**Background and Purpose of the Update**  
This update announces the General Availability (GA) of the Smart Tier feature for Azure Blob Storage and Azure Data Lake Storage (ADLS) in the Azure Government and China regions. The purpose of this update is to extend the benefits of automated data tiering to customers in these sovereign clouds, enabling efficient and cost-effective management of object storage without manual intervention in tier placement.

**Specific Features and Detailed Changes**  
Smart Tier is a fully managed, automated data tiering solution for object storage standard online tiers. With this feature, Azure automatically selects the most appropriate access tier (such as Hot, Cool, or Cold) for each object based on usage patterns, eliminating the need for manual tier assignment. This reduces operational overhead and optimizes storage costs by ensuring data is stored in the most cost-effective tier according to its access frequency.

The GA release makes Smart Tier available for both Azure Blob Storage and ADLS, specifically in the Azure Government and China regions. This expands the reach of Smart Tier beyond commercial regions, supporting compliance and regulatory requirements for customers operating in these environments.

**Technical Mechanisms and Implementation Methods**  
Smart Tier leverages Azure’s built-in analytics and automation to monitor access patterns of objects stored in Blob Storage and ADLS. Based on these patterns, the system dynamically moves objects between standard online tiers (e.g., Hot, Cool, Cold) without user intervention. The mechanism is fully managed by Azure, requiring no custom scripts or manual configuration. Users simply enable Smart Tier for their storage accounts, and Azure handles tier assignment and movement transparently.

**Use Cases and Application Scenarios**  
- **Government and Regulated Industries:** Organizations in Azure Government and China regions can now utilize Smart Tier to comply with regulatory requirements while optimizing storage costs.
- **Data Lake Analytics:** Enterprises storing large volumes of data in ADLS can benefit from automated tiering, ensuring frequently accessed data remains in high-performance tiers and infrequently accessed data is moved to lower-cost tiers.
- **Backup and Archive Solutions:** Customers managing backup or archival workloads can reduce costs by leveraging Smart Tier, as data that becomes less active is automatically moved to more economical tiers.

**Important Considerations and Limitations**  
- Smart Tier is only available for standard online tiers; it does not apply to offline or archive tiers.
- The feature is fully managed, so customers have limited control over tier placement decisions.
- Availability is restricted to Azure Government and China regions as per this update.
- Customers should review pricing implications, as automated tier movement may affect storage costs based on access patterns.

**Integration with Related Azure Services**  
Smart Tier integrates seamlessly with Azure Blob Storage and ADLS, requiring no changes to existing APIs or workflows. It complements Azure’s broader storage management capabilities, such as lifecycle management policies and cost optimization tools. Customers can continue to use related services like Azure Data Factory, Azure Synapse Analytics, and Azure Backup without modification, as Smart Tier operates transparently in the background.

**Summary Sentence**  
The Smart Tier feature for Azure Blob and Data Lake Storage is now generally available in Azure Government and China regions, providing fully automated, managed data tiering for standard online object storage tiers, thereby optimizing storage costs and reducing manual management for customers in these sovereign clouds.

---

### 107. Public Preview: Azure Blob Storage turbo tier

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Blob Storage turbo tier](https://azure.microsoft.com/updates?id=579031)

**Update ID**: 579031
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Analytics, Azure Blob Storage, Azure Data Lake Storage, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Blob Storage turbo tier is now available in Public Preview.

- Key changes or new features  
The turbo tier introduces SSD-backed storage to Azure Blob Storage, delivering significantly higher throughput and lower latency for performance-sensitive workloads. It is designed to support demanding use cases such as AI training and inference, advanced analytics, and high-performance data processing. Turbo tier is available for eligible Azure Blob Storage accounts and can be selected as a storage option for new or existing blobs.

- Target audience affected  
Developers and IT professionals working with Azure Blob Storage, especially those managing workloads that require fast data access and high IOPS, such as AI/ML, analytics, and real-time applications.

- Important notes  
Turbo tier is currently in Public Preview and may not be available in all regions or for all account types. Pricing and regional availability should be reviewed before adoption. During the preview, users are encouraged to test performance and provide feedback to Microsoft. For more details and eligibility, refer to the official Azure Update link.

**Details**:

**Azure Update Report: Public Preview – Azure Blob Storage Turbo Tier**

**Background and Purpose of the Update**  
Azure Blob Storage turbo tier has entered Public Preview, introducing SSD-backed performance to Azure Blob Storage accounts. The primary goal of this update is to address the needs of performance-sensitive workloads such as AI training, inference, analytics, and other demanding data operations. Traditional Blob Storage tiers (Hot, Cool, Archive) are optimized for cost and access patterns, but may not deliver the low-latency, high-throughput characteristics required by modern data-intensive applications. The turbo tier is designed to fill this gap by providing a high-performance storage option within Azure Blob Storage.

**Specific Features and Detailed Changes**  
The turbo tier is characterized by SSD-backed storage, which significantly improves input/output operations per second (IOPS) and reduces latency compared to HDD-backed or standard Blob Storage tiers. This enhancement is available for eligible Azure Blob Storage accounts, enabling customers to select turbo tier for blobs that require rapid access and processing. The introduction of turbo tier does not replace existing tiers but adds a new option for workloads that demand superior performance. The tier is specifically engineered for scenarios where data access speed is critical, and it supports performance-sensitive operations without compromising on the scalability and durability of Azure Blob Storage.

**Technical Mechanisms and Implementation Methods**  
The turbo tier leverages SSD hardware at the backend to deliver enhanced performance metrics. Azure manages the allocation and provisioning of SSD resources transparently, allowing users to select the turbo tier via the Azure portal, REST API, or SDKs when configuring their Blob Storage accounts or individual blobs. The tier is integrated into the Blob Storage lifecycle management, enabling automated tiering and policy-based data movement. The implementation ensures compatibility with existing Blob Storage APIs and features, so applications can utilize turbo tier without code changes, provided they specify the desired tier.

**Use Cases and Application Scenarios**  
Turbo tier is ideal for workloads that require high throughput and low latency, such as:
- AI training and inference pipelines, where rapid access to large datasets accelerates model development and deployment.
- Real-time analytics, where immediate data ingestion and processing are essential for business intelligence and operational decision-making.
- High-performance compute scenarios, including scientific simulations and financial modeling, which rely on fast data retrieval.
- Any application where performance bottlenecks in storage can impede overall system efficiency.

**Important Considerations and Limitations**  
As this feature is in Public Preview, it may be subject to regional availability and quota restrictions. Only eligible Blob Storage accounts can access the turbo tier, and customers should review Azure documentation for account eligibility and provisioning guidelines. Pricing for turbo tier is expected to reflect its premium performance characteristics, so cost management is a key consideration. Additionally, preview features may not have full SLA support and could undergo changes before general availability.

**Integration with Related Azure Services**  
Turbo tier is fully integrated with Azure Blob Storage, supporting standard APIs, lifecycle management, and security features. It can be used alongside Azure Data Lake Storage, Azure Machine Learning, and Azure Synapse Analytics, enabling seamless data flow across Azure’s analytics and AI ecosystem. The tier enhances performance for services that depend on Blob Storage, such as Azure Functions, Azure Logic Apps, and Azure Databricks, by reducing storage latency and increasing throughput.

**Summary Sentence:**  
Azure Blob Storage turbo tier, now in Public Preview, offers SSD-backed high-performance storage for eligible Blob Storage accounts, targeting demanding workloads such as AI, analytics, and real-time data processing, with seamless integration into Azure’s data and compute services.

---

### 108. Public Preview: MSSQL extension for Visual Studio Code - local-to-cloud deployment wizard 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: MSSQL extension for Visual Studio Code - local-to-cloud deployment wizard ](https://azure.microsoft.com/updates?id=579014)

**Update ID**: 579014
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now includes a public preview of a local-to-cloud deployment wizard for Azure SQL Database.

- Key changes or new features  
A new guided deployment wizard allows users to migrate a local Azure SQL Database container directly to Azure SQL Database from within Visual Studio Code. The wizard supports both schema-only and schema-and-data migration options, streamlining the deployment process and reducing manual steps.

- Target audience affected  
Developers and IT professionals who use Visual Studio Code for database development and management, especially those working with Azure SQL Database and local containers.

- Important notes  
This feature is currently in public preview. Users can leverage the wizard to simplify and accelerate cloud migration workflows directly from their development environment. It is recommended to test the migration process in non-production environments during the preview phase. For more details and instructions, refer to the official Azure Update announcement.

**Details**:

**Background and Purpose of the Update**  
The MSSQL extension for Visual Studio Code has introduced a new feature in public preview: a local-to-cloud deployment wizard. The primary purpose of this update is to streamline the process of migrating databases from local environments, specifically Azure SQL Database containers, directly to Azure SQL Database in the cloud. This addresses the need for a simplified, integrated workflow for developers and database administrators who use Visual Studio Code as their primary development environment.

**Specific Features and Detailed Changes**  
The update adds a guided deployment wizard to the MSSQL extension. This wizard enables users to initiate and complete the migration of a local Azure SQL Database container to Azure SQL Database in the cloud without leaving Visual Studio Code. The wizard offers two deployment modes:
- **Schema-only deployment:** Transfers only the database schema (tables, views, stored procedures, etc.) to the cloud.
- **Schema-and-data deployment:** Transfers both the schema and the associated data from the local container to the cloud database.

These options provide flexibility depending on whether users want to initialize a new database structure or fully migrate an existing dataset.

**Technical Mechanisms and Implementation Methods**  
The deployment wizard is integrated directly into the MSSQL extension UI within Visual Studio Code. It guides users through the necessary steps, including:
- Selecting the source local Azure SQL Database container.
- Choosing the target Azure SQL Database instance in the cloud.
- Specifying the deployment mode (schema-only or schema-and-data).

The wizard likely leverages standard database migration techniques such as generating SQL scripts for schema deployment or using data export/import utilities for schema-and-data migration. All operations are initiated and managed from within Visual Studio Code, reducing the need for external tools or manual scripting.

**Use Cases and Application Scenarios**  
- **Development to Production Migration:** Developers can build and test databases locally using Azure SQL Database containers, then deploy them to Azure SQL Database in the cloud when ready for production.
- **Rapid Prototyping:** Teams can quickly iterate on database designs locally and push updates to the cloud as needed.
- **Educational and Testing Environments:** Instructors and students can set up local environments and easily migrate their work to cloud instances for demonstration or evaluation purposes.

**Important Considerations and Limitations**  
- The feature is currently in public preview, which means it may not be fully stable and could lack certain functionalities present in mature migration tools.
- Only migrations from local Azure SQL Database containers to Azure SQL Database in the cloud are supported; other source or target types are not mentioned.
- Users should validate the integrity of schema and data post-migration, especially when using schema-and-data mode.
- There may be limitations regarding the size and complexity of databases that can be migrated through the wizard, as well as potential restrictions on supported data types or objects.

**Integration with Related Azure Services**  
This update enhances the integration between Visual Studio Code and Azure SQL Database, allowing for a seamless workflow from local development to cloud deployment. It leverages the MSSQL extension’s capabilities and connects directly to Azure SQL Database, facilitating direct migration without manual intervention or external migration services.

**Summary Sentence**  
The MSSQL extension for Visual Studio Code now offers a public preview of a local-to-cloud deployment wizard, enabling guided migration of Azure SQL Database containers to Azure SQL Database in the cloud with schema-only or schema-and-data options, directly from within the Visual Studio Code environment.

---

### 109. Public Preview: MSSQL extension for Visual Studio Code- Azure SQL Database container provisioning 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: MSSQL extension for Visual Studio Code- Azure SQL Database container provisioning ](https://azure.microsoft.com/updates?id=579009)

**Update ID**: 579009
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now supports provisioning Azure SQL Database containers in public preview.

- Key changes or new features  
Developers can easily create and manage a local Azure SQL Database container environment directly within Visual Studio Code. The extension automatically detects runtime environments including Docker, Windows Subsystem for Linux (WSL), Apple containers, and Podman, streamlining setup and management. This enables rapid development and testing of cloud-aligned SQL databases without needing a full Azure subscription or remote resources.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use Visual Studio Code for SQL development and testing, especially those working with Azure SQL Database or requiring local containerized environments.

- Important notes  
The feature is currently in public preview and may be subject to changes. It simplifies local development workflows by aligning local container environments with Azure SQL Database, supporting cross-platform container runtimes. Users should ensure their local machine meets the requirements for containerization and the MSSQL extension is updated to the latest version.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=579009).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: MSSQL extension for Visual Studio Code- Azure SQL Database container provisioning  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579009)

---

**Background and Purpose of the Update:**  
This update introduces support for Azure SQL Database container provisioning within the MSSQL extension for Visual Studio Code. The primary purpose is to streamline the process of creating and managing local database environments that closely mirror Azure SQL Database, thereby enhancing development workflows and enabling more accurate testing and validation before deployment to the cloud.

---

**Specific Features and Detailed Changes:**  
- **Azure SQL Database Container Support:** The MSSQL extension now allows users to provision Azure SQL Database containers directly from Visual Studio Code.  
- **Automatic Runtime Detection:** The extension automatically detects available container runtimes, including Docker, Windows Subsystem for Linux (WSL), Apple containers, and Podman.  
- **Simplified Management:** Developers can create, start, stop, and manage Azure SQL Database containers without leaving the Visual Studio Code environment.  
- **Cloud-Aligned Local Environment:** The containers are configured to emulate Azure SQL Database, ensuring consistency between local development and cloud deployment.

---

**Technical Mechanisms and Implementation Methods:**  
- **Container Runtime Integration:** The extension leverages runtime detection to identify and interface with Docker, WSL, Apple containers, and Podman, abstracting the complexity of container orchestration from the user.  
- **Provisioning Workflow:** Upon initiating a container, the extension handles the download and setup of the Azure SQL Database container image, configures it according to Azure standards, and exposes connection endpoints for local access.  
- **Visual Studio Code Integration:** All provisioning and management actions are accessible via the MSSQL extension UI and command palette, allowing for seamless interaction and automation within the editor.

---

**Use Cases and Application Scenarios:**  
- **Local Development and Testing:** Developers can spin up Azure SQL Database containers to test code and database schema changes locally, ensuring compatibility with Azure SQL Database before deployment.  
- **CI/CD Pipeline Integration:** Containers can be used in automated build and test pipelines to validate database operations in environments that replicate Azure SQL Database.  
- **Cross-Platform Development:** With support for multiple container runtimes, teams working on Windows, macOS, or Linux can uniformly provision local Azure SQL Database environments.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes or limitations.  
- **Container Runtime Requirements:** Users must have a supported container runtime installed and properly configured (Docker, WSL, Apple containers, or Podman) for the extension to function.  
- **Feature Parity:** While the containers emulate Azure SQL Database, there may be differences in feature support or behavior compared to the actual Azure service; thorough testing is recommended.

---

**Integration with Related Azure Services:**  
- **Azure SQL Database Alignment:** The containers are designed to closely mirror Azure SQL Database, facilitating easy migration and deployment to the cloud.  
- **Azure DevOps and CI/CD:** The extension’s container provisioning capabilities can be integrated into Azure DevOps pipelines for automated testing and validation.  
- **Visual Studio Code Ecosystem:** The MSSQL extension works in conjunction with other Azure extensions in Visual Studio Code, enabling a unified development experience.

---

**Summary Sentence:**  
The MSSQL extension for Visual Studio Code now enables seamless provisioning and management of Azure SQL Database containers, offering developers a cloud-aligned local environment with automatic runtime detection across Docker, WSL, Apple containers, and Podman, thereby enhancing local development, testing, and CI/CD workflows.

---

### 110. Public Preview: MSSQL extension for Visual Studio Code performance dashboard 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: MSSQL extension for Visual Studio Code performance dashboard ](https://azure.microsoft.com/updates?id=579004)

**Update ID**: 579004
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now includes a new query performance dashboard, available in public preview.

- Key changes or new features  
The dashboard leverages SQL Server’s Query Store to provide performance insights directly within VS Code. It enables users to analyze query trends, investigate execution plans, and identify performance bottlenecks. Additionally, integration with GitHub Copilot helps optimize queries by suggesting improvements based on detected issues.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use Visual Studio Code to manage SQL Server databases and are interested in monitoring and optimizing query performance.

- Important notes if any  
The feature is currently in public preview, so feedback is encouraged and some functionality may change before general availability. Users should ensure their SQL Server instance has Query Store enabled to fully utilize the dashboard. The integration with GitHub Copilot requires appropriate licensing and setup. For more details, refer to the official Azure Update announcement.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: MSSQL extension for Visual Studio Code performance dashboard  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579004)

---

**Background and Purpose of the Update**  
The MSSQL extension for Visual Studio Code (VS Code) has introduced a new query performance dashboard, now available in public preview. This update aims to enhance the developer experience by providing integrated performance monitoring and optimization capabilities directly within the VS Code environment. The primary purpose is to empower IT professionals and database developers to gain actionable insights into SQL query performance, streamline troubleshooting, and optimize workloads without leaving their development workspace.

---

**Specific Features and Detailed Changes**  
The performance dashboard is a significant addition to the MSSQL extension. Key features include:

- **Performance Insights:** The dashboard surfaces real-time and historical performance metrics for SQL queries, enabling users to quickly identify bottlenecks and inefficiencies.
- **Trend Analysis:** Users can analyze performance trends over time, helping to detect regressions or improvements in query execution.
- **Execution Plan Investigation:** The dashboard provides detailed access to query execution plans, allowing for in-depth analysis of how SQL Server processes queries.
- **Query Optimization with GitHub Copilot:** Integration with GitHub Copilot offers AI-assisted recommendations for query optimization, helping users improve performance based on best practices and historical data.

These features collectively streamline the process of monitoring, analyzing, and optimizing SQL queries within VS Code.

---

**Technical Mechanisms and Implementation Methods**  
The dashboard leverages SQL Server’s **Query Store** feature, which collects and stores query execution statistics and plans. The MSSQL extension interfaces with Query Store to retrieve relevant performance data and visualize it within VS Code. The integration with GitHub Copilot utilizes AI-driven suggestions to assist in query tuning, directly accessible from the dashboard interface. The extension communicates with SQL Server instances using standard authentication and connection protocols, ensuring secure and efficient data retrieval.

---

**Use Cases and Application Scenarios**  
- **Development and Testing:** Developers can monitor and optimize queries during application development, ensuring efficient SQL code before deployment.
- **Performance Troubleshooting:** Database administrators can use the dashboard to investigate slow-running queries, analyze execution plans, and apply optimizations.
- **Continuous Improvement:** Teams can track performance trends and apply iterative improvements to their database workloads.
- **AI-Assisted Optimization:** Leveraging GitHub Copilot, users can receive automated suggestions for query enhancements, reducing manual tuning efforts.

---

**Important Considerations and Limitations**  
- **Public Preview Status:** As the feature is in public preview, it may not be fully stable or feature-complete. Users should exercise caution when relying on it in production environments.
- **Query Store Dependency:** The dashboard’s functionality requires Query Store to be enabled on the target SQL Server instance.
- **Extension Compatibility:** Ensure the latest version of the MSSQL extension is installed in VS Code to access the performance dashboard.
- **Copilot Integration:** GitHub Copilot recommendations are AI-generated and should be reviewed for accuracy and relevance before implementation.

---

**Integration with Related Azure Services**  
The MSSQL extension is compatible with Azure SQL Database and Azure SQL Managed Instance, allowing users to monitor and optimize queries on cloud-based SQL workloads. The dashboard can be used alongside Azure Monitor and other Azure-native database management tools for comprehensive performance management.

---

**Summary Sentence**  
The new query performance dashboard in the MSSQL extension for Visual Studio Code, now in public preview, provides integrated performance insights, trend analysis, execution plan investigation, and AI-assisted query optimization, leveraging Query Store and GitHub Copilot to enhance SQL development and troubleshooting workflows.

---

### 111. Generally Available: Fuzzy string match is available across Microsoft SQL offerings 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Fuzzy string match is available across Microsoft SQL offerings ](https://azure.microsoft.com/updates?id=578998)

**Update ID**: 578998
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Fuzzy string match functionality is now generally available across Microsoft SQL offerings, including Azure SQL Database, Azure SQL Managed Instance, SQL database in Microsoft Fabric, and SQL Server 2025.

- Key changes or new features  
This update introduces built-in support for fuzzy string matching, allowing users to compare strings based on similarity or difference directly within SQL queries. This feature enables more advanced text analysis, data deduplication, and error-tolerant searches without requiring external libraries or custom code.

- Target audience affected  
Developers and IT professionals working with Microsoft SQL platforms, particularly those involved in data quality, cleansing, migration, and analytics tasks.

- Important notes if any  
Fuzzy string match is now a native feature, simplifying implementation and improving performance for string comparison operations. It is available across cloud and on-premises SQL platforms, ensuring consistency in development and deployment. Developers should review documentation for syntax and usage guidelines to leverage this feature effectively in their applications and workflows.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=578998

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Fuzzy string match is available across Microsoft SQL offerings  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=578998)

---

**Background and Purpose of the Update:**  
The general availability of fuzzy string match across Microsoft SQL offerings addresses the need for advanced string comparison capabilities within SQL environments. Traditional string comparison methods in SQL are typically binary and do not account for typographical errors, variations in spelling, or similar but non-identical text values. Fuzzy string matching enables users to compare and evaluate the similarity or difference between strings, which is essential for data quality, deduplication, and entity resolution tasks.

---

**Specific Features and Detailed Changes:**  
With this update, fuzzy string match functionality is now generally available in the following Microsoft SQL platforms:

- Azure SQL Database
- Azure SQL Managed Instance
- SQL database in Microsoft Fabric
- SQL Server 2025

This feature allows users to perform string comparisons based on similarity metrics rather than exact matches. It provides built-in capabilities to assess how closely two strings resemble each other, facilitating more flexible and intelligent querying and data processing.

---

**Technical Mechanisms and Implementation Methods:**  
The fuzzy string match feature is implemented natively within the SQL engine across the supported platforms. It provides functions or operators that can be used within SQL queries to compare string values and return a similarity score or Boolean result based on a defined threshold. This mechanism abstracts the complexity of implementing custom algorithms for string similarity, such as Levenshtein distance or other phonetic algorithms, and makes it accessible directly through SQL syntax.

Engineers can leverage these functions in SELECT statements, JOIN conditions, or WHERE clauses to identify records with similar text values. The feature is optimized for performance and scalability within the managed SQL environments.

---

**Use Cases and Application Scenarios:**  
Fuzzy string matching is particularly valuable in scenarios such as:

- **Data Deduplication:** Identifying and merging duplicate records that have minor variations in names, addresses, or other text fields.
- **Data Cleansing:** Detecting and correcting inconsistent data entries caused by typographical errors or alternate spellings.
- **Entity Resolution:** Matching entities across disparate datasets where exact string matches are unlikely.
- **Search and Recommendation:** Enhancing user search experiences by returning results that are similar, not just exact matches.

---

**Important Considerations and Limitations:**  
While the feature is generally available, users should consider the following:

- Performance may vary depending on dataset size and the complexity of fuzzy matching operations.
- The specific similarity algorithms and configuration options available are determined by the SQL engine implementation; users should consult the official documentation for details on supported functions and parameters.
- Fuzzy matching may introduce false positives or negatives, so threshold tuning is important for optimal results.
- Security and compliance requirements should be reviewed when using fuzzy matching in sensitive data scenarios.

---

**Integration with Related Azure Services:**  
Fuzzy string match is fully integrated into the supported Microsoft SQL offerings, ensuring compatibility with other Azure services that interact with these databases. This includes Azure Data Factory for ETL processes, Azure Synapse Analytics for big data processing, and Power BI for reporting and analytics. The feature enhances data quality and consistency across the Azure data ecosystem.

---

**Summary Sentence:**  
Fuzzy string match is now generally available across Microsoft SQL offerings, enabling advanced string similarity comparisons for improved data quality, deduplication, and entity resolution directly within Azure SQL Database, Azure SQL Managed Instance, SQL database in Microsoft Fabric, and SQL Server 2025.

---

### 112. Public Preview: Task Queues for Azure Functions durable task scheduler

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Task Queues for Azure Functions durable task scheduler](https://azure.microsoft.com/updates?id=578989)

**Update ID**: 578989
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite

**Summary**:

- What was updated  
Azure Functions durable task scheduler now supports Task Queues in public preview.

- Key changes or new features  
Developers and IT professionals can now create named task queues within a task hub. This allows workloads sharing the same task hub to be isolated based on their throughput requirements and downstream service limits. Task queues can be configured to optimize processing, enabling better control over workload distribution and resource utilization. This feature helps prevent bottlenecks and ensures that high-priority or resource-intensive tasks do not impact other workloads.

- Target audience affected  
Azure Functions developers, architects, and IT professionals managing serverless workflows or orchestrations using Durable Functions.

- Important notes if any  
Task Queues are currently in public preview and may not be suitable for production workloads. Users should test thoroughly and monitor performance. Documentation and best practices are available to guide configuration and integration.  
For more details, visit the official Azure Update page: https://azure.microsoft.com/updates?id=578989

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Task Queues for Azure Functions Durable Task Scheduler

**Background and Purpose of the Update:**  
Azure Functions Durable Task Scheduler traditionally manages orchestration and activity tasks within a single task hub, which can lead to challenges when workloads with varying throughput requirements and downstream service limits share the same hub. The introduction of Task Queues addresses the need for more granular control over task distribution and processing, enabling IT professionals to optimize resource utilization and manage workload isolation within Azure Functions.

**Specific Features and Detailed Changes:**  
The update introduces the capability to create named task queues within a task hub. This enhancement allows users to configure multiple queues, each with its own throughput settings and constraints. By assigning tasks to specific queues, workloads can be segregated based on their performance and service requirements. This provides a mechanism to prevent contention between tasks with different priorities or downstream dependencies, ensuring that critical workloads are not throttled by less important or resource-intensive tasks.

**Technical Mechanisms and Implementation Methods:**  
Task Queues are implemented as configurable entities within the Durable Task Scheduler. IT professionals can define named queues in their task hub configuration and specify throughput limits or other relevant parameters per queue. When orchestrating functions, tasks can be explicitly routed to a designated queue, allowing for targeted scheduling and execution. The scheduler manages queue-specific processing, respecting the configured limits and optimizing task dispatch according to queue assignments. This approach leverages the underlying Azure Functions infrastructure, maintaining compatibility with existing orchestration patterns while introducing queue-based isolation and control.

**Use Cases and Application Scenarios:**  
- **Workload Isolation:** Segregate high-priority or latency-sensitive tasks from bulk or background processing jobs, ensuring that critical workflows are not delayed by less urgent operations.
- **Throughput Management:** Assign workloads with different throughput requirements to separate queues, preventing overloading of downstream services and maintaining compliance with service limits.
- **Resource Optimization:** Balance task execution across multiple queues to maximize utilization of compute resources and minimize bottlenecks.
- **Multi-Tenant Solutions:** Support scenarios where multiple applications or tenants share a task hub, enabling per-tenant queue configuration for customized workload management.

**Important Considerations and Limitations:**  
- Task Queues are currently available in public preview, which may imply limited support and potential changes before general availability.
- Configuration and management of queues require careful planning to avoid misallocation of tasks and ensure optimal throughput.
- Integration with downstream services must account for queue-specific limits to prevent service throttling or failures.
- Existing orchestrations may require updates to leverage named queues, and compatibility with legacy patterns should be validated.

**Integration with Related Azure Services:**  
Task Queues are natively integrated within the Azure Functions Durable Task Scheduler, maintaining seamless operation with Azure Functions orchestration and activity patterns. They can be used alongside other Azure services such as Azure Storage, Azure Service Bus, and Azure Event Grid, depending on the orchestration requirements and downstream dependencies. Queue configuration and management are performed within the Azure Functions environment, ensuring consistent integration with monitoring, logging, and scaling features.

**Summary Sentence:**  
Task Queues for Azure Functions Durable Task Scheduler, now in public preview, enable IT professionals to create named queues within a task hub for granular workload isolation and throughput management, providing enhanced control over task scheduling and resource optimization in shared Azure Functions environments.

---

### 113. Public Preview: Azure Functions Network Troubleshooter v2

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Functions Network Troubleshooter v2](https://azure.microsoft.com/updates?id=578980)

**Update ID**: 578980
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Functions Network Troubleshooter v2 is now available in Public Preview.

- Key changes or new features  
The updated Network Troubleshooter provides a top-down view of Function App dependencies, including Storage, Service Bus, and Azure Files. For each supported dependency, users can inspect connectivity, diagnose issues, and visualize network paths. The tool offers enhanced diagnostics and visibility into how Function Apps interact with their networked resources, helping to quickly identify and resolve connectivity problems.

- Target audience affected  
Developers and IT professionals managing Azure Functions, especially those responsible for troubleshooting network and connectivity issues in serverless environments.

- Important notes if any  
The preview version supports Storage, Service Bus, and Azure Files dependencies. This tool is intended to streamline troubleshooting and reduce downtime by providing actionable insights into network connectivity. Users should note that this is a Public Preview, so features and support may evolve before general availability. For more details and access, visit the official Azure Update page: https://azure.microsoft.com/updates?id=578980

**Details**:

**Azure Update Report: Public Preview – Azure Functions Network Troubleshooter v2**

**Background and Purpose of the Update**  
Azure Functions is a serverless compute service that relies on connectivity to various Azure resources, such as Storage, Service Bus, and Azure Files. Diagnosing network-related issues between Function Apps and their dependencies is critical for ensuring reliability and performance. The release of Azure Functions Network Troubleshooter v2 in Public Preview addresses the need for enhanced visibility and diagnostics, enabling IT professionals to systematically investigate and resolve connectivity problems.

**Specific Features and Detailed Changes**  
Network Troubleshooter v2 introduces a top-down dependency view for Function Apps. This means users can now visualize and inspect the connections between their Function Apps and supported dependencies, specifically Azure Storage, Service Bus, and Azure Files. For each dependency, the tool allows customers to perform inspection tasks, providing granular insight into the health and accessibility of these resources from the Function App’s perspective. Compared to previous versions, v2 expands the scope of supported dependencies and improves the diagnostic capabilities for network troubleshooting.

**Technical Mechanisms and Implementation Methods**  
The Network Troubleshooter v2 operates by analyzing the network paths and connectivity between Function Apps and their dependencies. It leverages Azure’s diagnostic APIs and internal telemetry to gather real-time status and configuration data. The tool presents this information in a structured, top-down format, allowing users to trace connectivity issues from the Function App to each resource. Inspection capabilities may include checking endpoint accessibility, authentication status, and potential configuration mismatches. The implementation is integrated within the Azure portal, providing a seamless experience for users managing Function Apps.

**Use Cases and Application Scenarios**  
- **Root Cause Analysis:** When a Function App fails to access Storage, Service Bus, or Azure Files, IT professionals can use Network Troubleshooter v2 to pinpoint the exact dependency causing the issue.
- **Deployment Validation:** After deploying new Function Apps or updating network configurations, users can verify that all dependencies are reachable and correctly configured.
- **Performance Optimization:** By identifying network bottlenecks or misconfigurations, teams can optimize the connectivity and performance of their serverless workloads.
- **Security Auditing:** Ensuring that network paths and authentication mechanisms are correctly set up helps maintain compliance and security standards.

**Important Considerations and Limitations**  
- The tool is currently in Public Preview, which means it may not support all possible Function App dependencies and scenarios.
- Supported dependencies are limited to Azure Storage, Service Bus, and Azure Files as per the current release.
- Inspection capabilities are restricted to these dependencies; other Azure services or external resources are not covered.
- As a preview feature, stability and completeness may vary, and feedback is encouraged to improve future releases.

**Integration with Related Azure Services**  
Network Troubleshooter v2 is tightly integrated with Azure Functions and its supported dependencies (Storage, Service Bus, Azure Files). It works within the Azure portal, complementing existing diagnostic tools such as Application Insights and Azure Monitor. This integration allows for a unified troubleshooting workflow, enabling IT professionals to combine network diagnostics with broader application monitoring and logging.

**Summary Sentence**  
Azure Functions Network Troubleshooter v2, now in Public Preview, provides IT professionals with a comprehensive top-down diagnostic tool for inspecting Function App connectivity to Azure Storage, Service Bus, and Azure Files, enhancing visibility and troubleshooting capabilities within the Azure portal.

---

### 114. Public Preview: OS-level dependency support via containers for Azure Functions Flex Consumption

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: OS-level dependency support via containers for Azure Functions Flex Consumption](https://azure.microsoft.com/updates?id=578975)

**Update ID**: 578975
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Functions Flex Consumption now supports OS-level dependencies via containers in Public Preview.

- Key changes or new features  
Developers can now deploy Azure Functions Flex Consumption apps using custom containers. This enables inclusion of native executables, system libraries, and other OS-level dependencies that were previously unavailable in the Microsoft-managed worker environment. The update allows greater flexibility for workloads requiring specialized runtime environments or dependencies beyond what is provided by default.

- Target audience affected  
Developers and IT professionals building serverless applications on Azure Functions, especially those needing custom OS-level dependencies or specialized runtimes.

- Important notes  
This feature is currently in Public Preview. Custom containers can be used to package all required dependencies, but users should validate compatibility and performance. Existing Flex Consumption apps not using containers remain unaffected. Review documentation for container requirements and best practices.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: OS-level dependency support via containers for Azure Functions Flex Consumption  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578975)

---

**Background and Purpose of the Update**  
Azure Functions Flex Consumption previously operated within a Microsoft-managed worker environment, which restricted customers from extending the runtime with native executables, system libraries, or other OS-level dependencies. This limitation hindered scenarios where functions required specialized binaries or system-level integrations. The purpose of this update is to address these constraints by introducing OS-level dependency support via containers, enabling greater flexibility and extensibility for serverless workloads.

**Specific Features and Detailed Changes**  
With this update, Azure Functions Flex Consumption now supports deploying functions within containers, allowing customers to package and run their functions alongside any required OS-level dependencies. This includes native executables, custom system libraries, and other software components that must be present at the operating system level. The change provides a significant enhancement over the previous model, where only language-level dependencies could be managed, and system-level customization was not possible.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages containerization technology, enabling customers to build and deploy their Azure Functions as container images. These images encapsulate both the function code and any OS-level dependencies, ensuring that the execution environment matches the requirements of the application. The containers are then orchestrated by Azure Functions Flex Consumption, providing the same serverless scalability and event-driven execution as before, but with the added benefit of a customizable runtime environment.

**Use Cases and Application Scenarios**  
This update is particularly valuable for scenarios where functions require native binaries, custom system libraries, or integration with legacy software components. Typical use cases include:

- Functions that invoke native executables for image processing, data manipulation, or scientific computation.
- Workloads requiring specialized system libraries not available in the default Azure Functions runtime.
- Migration of legacy applications to serverless architectures, where OS-level dependencies must be preserved.
- Integration with third-party software that mandates installation at the OS level.

**Important Considerations and Limitations**  
While container support introduces flexibility, customers must ensure that their container images are optimized for performance and security. It is important to manage image size, minimize unnecessary dependencies, and follow best practices for container security. Additionally, as this feature is in public preview, it may not offer full production-grade guarantees, and customers should validate their workloads accordingly. There may also be limitations regarding supported base images, runtime versions, and integration points, which should be reviewed in the official documentation.

**Integration with Related Azure Services**  
Containerized Azure Functions Flex Consumption can integrate seamlessly with other Azure services such as Azure Container Registry for image storage, Azure Event Grid for event-driven triggers, and Azure Monitor for logging and diagnostics. The update aligns with Azure’s broader container ecosystem, facilitating consistent deployment and management practices across serverless, Kubernetes, and container-based workloads.

---

**Summary Sentence:**  
Azure Functions Flex Consumption now supports OS-level dependencies via containers in public preview, enabling customers to package and run functions with native executables and system libraries, thereby enhancing flexibility and extensibility for serverless applications.

---

### 115. Public Preview: Hosted Skill and Agent Bindings for Azure Functions

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Hosted Skill and Agent Bindings for Azure Functions](https://azure.microsoft.com/updates?id=578845)

**Update ID**: 578845
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Functions now supports Hosted Skill and Agent bindings in public preview.

- Key changes or new features  
Developers can integrate agents (such as AI skills or bots) into Azure Functions with simplified setup. The new bindings handle agent initialization and lifecycle management, reducing boilerplate code and allowing developers to focus on business logic. This streamlines the process of connecting Azure Functions to hosted skills and agents, making it easier to build intelligent, event-driven applications.

- Target audience affected  
Developers building serverless applications with Azure Functions, especially those integrating AI, bots, or other agent-based services. IT professionals managing Azure Functions deployments may also benefit from simplified configuration and maintenance.

- Important notes  
This feature is currently in public preview and may not be production-ready. Developers should test thoroughly before deploying in critical environments. Documentation and support may be limited during the preview phase.  
For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=578845).

**Details**:

**Azure Update Report: Public Preview – Hosted Skill and Agent Bindings for Azure Functions**

**Background and Purpose of the Update**  
The public preview release of Hosted Skill and Agent bindings for Azure Functions addresses the complexity involved in integrating agents into applications. Traditionally, developers must implement extensive setup and lifecycle management code before focusing on core business logic. This update aims to streamline the integration process, reducing boilerplate and plumbing code, thereby accelerating development and improving maintainability.

**Specific Features and Detailed Changes**  
The new bindings provide a simplified mechanism for connecting Azure Functions to hosted skills and agents. By leveraging these bindings, developers can declaratively attach agents to their function apps without manual configuration or lifecycle management. This enhancement reduces the need for repetitive code and allows developers to focus directly on implementing business logic within their Azure Functions.

**Technical Mechanisms and Implementation Methods**  
The Hosted Skill and Agent bindings are implemented as native Azure Functions bindings. Developers can specify these bindings in the function app’s configuration, enabling automatic handling of agent setup, invocation, and lifecycle events. The bindings abstract away the underlying communication and orchestration required to interact with hosted skills and agents, ensuring seamless integration with the Azure Functions runtime. This approach leverages Azure’s extensible binding model, allowing developers to use familiar patterns for input and output bindings while benefiting from the new agent connectivity features.

**Use Cases and Application Scenarios**  
Typical scenarios for these bindings include applications that require integration with conversational AI agents, automation bots, or other hosted skills within Azure. For example, a customer support chatbot hosted as an agent can be directly bound to an Azure Function, enabling streamlined processing of user queries and responses. Similarly, workflow automation tasks that depend on hosted skills can be implemented with minimal setup, allowing rapid prototyping and deployment of intelligent solutions.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not be suitable for production workloads. IT professionals should be aware of potential changes in APIs, binding behavior, and documentation as the feature matures. Additionally, compatibility with existing Azure Functions triggers and bindings should be validated, and developers should monitor Azure’s update channels for guidance on migration or breaking changes. Security and access control for hosted agents should be carefully configured to prevent unauthorized interactions.

**Integration with Related Azure Services**  
The Hosted Skill and Agent bindings are designed to integrate seamlessly with Azure Functions, leveraging its event-driven compute model. They can be used alongside other Azure services such as Azure Bot Service, Azure Cognitive Services, and Azure Logic Apps, enabling rich, multi-service workflows. The bindings facilitate interoperability between function apps and hosted agents, supporting scenarios where functions act as orchestrators or processors for agent-driven tasks.

**Summary Sentence**  
Hosted Skill and Agent bindings for Azure Functions, now in public preview, provide a streamlined and declarative approach to integrating agents and hosted skills into function apps, reducing setup complexity and enabling developers to focus on business logic while leveraging Azure’s extensible binding model.

---

### 116. Public Preview: Geo-redundancy on Azure App Service

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Geo-redundancy on Azure App Service](https://azure.microsoft.com/updates?id=578839)

**Update ID**: 578839
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Mobile, Web, App Service, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure App Service introduces geo-redundancy, now available in public preview.

- Key changes or new features  
Geo-redundancy enables automatic deployment and management of App Service resources across multiple Azure regions. This feature allows web applications to remain available and resilient during regional outages, without requiring customers to manually set up and maintain separate App Service instances in each region. Failover and traffic routing are handled by Azure, simplifying disaster recovery and high availability strategies.

- Target audience affected  
Developers and IT professionals responsible for web application deployment, reliability, and disaster recovery planning on Azure App Service.

- Important notes  
Geo-redundancy is currently in public preview and may not support all App Service features or configurations. Customers should review documentation for limitations and best practices before adopting in production environments. This feature reduces operational complexity for multi-region deployments and is especially valuable for mission-critical applications requiring high availability.  
For more details, visit: https://azure.microsoft.com/updates?id=578839

**Details**:

**Azure Update Report: Public Preview – Geo-redundancy on Azure App Service**

**Background and Purpose of the Update**  
The public preview of geo-redundancy on Azure App Service addresses the need for enhanced application resilience and high availability across multiple Azure regions. Traditionally, customers seeking geo-redundant web applications had to independently deploy and manage App Service instances in each region, which increased operational complexity and overhead. This update aims to streamline the process by providing built-in geo-redundancy capabilities directly within Azure App Service.

**Specific Features and Detailed Changes**  
With geo-redundancy now available in public preview, Azure App Service can automatically create and manage redundant instances of web applications across multiple Azure regions. This eliminates the requirement for manual configuration and deployment in each region. The feature is designed to ensure that applications remain available and operational even if a regional outage occurs, thus improving disaster recovery and business continuity.

**Technical Mechanisms and Implementation Methods**  
The geo-redundancy feature leverages Azure’s native infrastructure to replicate and synchronize App Service resources across selected regions. When enabled, App Service provisions and manages the necessary resources in secondary regions, ensuring that application configurations, content, and settings are consistently maintained. Failover and recovery processes are handled by Azure, reducing the need for custom scripts or manual intervention. The implementation abstracts the complexity of cross-region replication, allowing IT professionals to focus on application logic rather than infrastructure management.

**Use Cases and Application Scenarios**  
Geo-redundancy is particularly valuable for mission-critical web applications that require continuous availability and minimal downtime. Typical scenarios include:  
- E-commerce platforms needing uninterrupted service during regional outages  
- SaaS providers offering global services with strict uptime SLAs  
- Enterprises implementing disaster recovery strategies for customer-facing portals  
- Applications serving geographically dispersed users, where latency and regional failures must be mitigated

**Important Considerations and Limitations**  
As this feature is in public preview, it may not yet be suitable for production workloads with stringent compliance or reliability requirements. Customers should evaluate the preview’s capabilities and limitations, including possible constraints on supported regions, resource types, and failover mechanisms. Monitoring, logging, and troubleshooting tools may also be limited during the preview phase. IT professionals should review Azure documentation and test geo-redundancy in non-production environments before full-scale adoption.

**Integration with Related Azure Services**  
Geo-redundancy on Azure App Service is designed to work seamlessly with other Azure services, such as Azure Traffic Manager for global DNS-based routing and Azure Front Door for application-level load balancing and failover. Integration with these services enables more granular control over traffic distribution and recovery strategies, complementing the built-in redundancy features of App Service.

**Summary Sentence**  
Azure App Service now offers public preview support for geo-redundancy, enabling automated cross-region resilience and simplified disaster recovery for web applications without manual multi-region deployments.

---

### 117. Generally Available: Durable Task extension for Microsoft Agent Framework

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Durable Task extension for Microsoft Agent Framework](https://azure.microsoft.com/updates?id=578829)

**Update ID**: 578829
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The Durable Task extension for Microsoft Agent Framework is now generally available for C# and Python.

- Key changes or new features  
This extension enables developers to build agents, multi-agent orchestrations, and workflows within the Microsoft Agent Framework that can run reliably for extended periods (minutes, days, or weeks). It provides durable state persistence, allowing workflows and orchestrations to survive restarts and failures. The extension supports both C# and Python, broadening language support for agent-based applications.

- Target audience affected  
Developers and IT professionals working with the Microsoft Agent Framework, especially those building long-running, reliable agent workflows in C# or Python.

- Important notes if any  
The general availability release ensures production-ready stability and support. Developers can now leverage durable task patterns in their agent-based solutions, improving reliability and scalability. Existing workflows can be enhanced with state persistence and recovery features. Documentation and SDKs for both languages are available to help integrate the extension into new or existing projects.

For more details, visit: https://azure.microsoft.com/updates?id=578829

**Details**:

**Azure Update Report: Durable Task Extension for Microsoft Agent Framework (General Availability)**

**Background and Purpose of the Update**  
The Durable Task extension for Microsoft Agent Framework has reached general availability for both C# and Python. This update addresses the need for reliable, long-running agent workflows and orchestrations within the Microsoft Agent Framework ecosystem. The extension is designed to enable developers to build agents and orchestrations that persist and execute tasks over extended periods—ranging from minutes to weeks—without loss of state or interruption, thereby improving workflow resilience and reliability.

**Specific Features and Detailed Changes**  
- **General Availability:** The extension is now officially supported and production-ready for C# and Python, expanding accessibility for developers using these languages.
- **Durable Agents:** Enables creation of agents and multi-agent orchestrations that can maintain state and progress across long durations.
- **Workflow Persistence:** The extension ensures that agent workflows and orchestrations are durable, meaning they can survive process restarts, failures, and can resume from their last persisted state.
- **Microsoft Agent Framework Integration:** The extension is tightly integrated with the Microsoft Agent Framework, allowing developers to leverage its capabilities for building complex, distributed workflows.

**Technical Mechanisms and Implementation Methods**  
- **Durable Task Framework:** The extension utilizes the Durable Task Framework, which is a proven mechanism for managing stateful workflows and orchestrations in Azure. It provides checkpointing, state persistence, and replay capabilities.
- **Language Support:** With support for C# and Python, developers can implement durable workflows using their preferred language, leveraging language-specific SDKs and APIs.
- **Persistence Layer:** The extension automatically handles persistence of agent state and workflow progress, ensuring reliability across failures and restarts.

**Use Cases and Application Scenarios**  
- **Long-Running Agent Workflows:** Ideal for scenarios where agents must perform tasks that require extended execution times, such as data processing, batch jobs, or integration workflows.
- **Multi-Agent Orchestration:** Supports orchestrating multiple agents in a coordinated manner, useful for distributed systems, automation pipelines, and complex business processes.
- **Microsoft Agent Framework Workflows:** Enables robust workflow implementations within the Microsoft Agent Framework, suitable for enterprise automation, monitoring, and control systems.

**Important Considerations and Limitations**  
- **Supported Languages:** The extension is available for C# and Python only; other languages are not supported.
- **Workflow Duration:** While the extension supports workflows running for minutes, days, or weeks, developers should ensure proper resource management and monitoring for very long-running tasks.
- **Integration Requirements:** Proper configuration and integration with the Microsoft Agent Framework and underlying Azure services are necessary to leverage durability and persistence features.

**Integration with Related Azure Services**  
- **Azure Durable Task Framework:** The extension builds upon Azure’s Durable Task Framework, inheriting its reliability and scalability features.
- **Microsoft Agent Framework:** Seamless integration with the Agent Framework allows for enhanced workflow orchestration and agent management.
- **Azure Storage and Compute:** The persistence and durability mechanisms may utilize Azure storage and compute resources, ensuring workflows are reliably maintained across distributed environments.

**Summary Sentence**  
The Durable Task extension for Microsoft Agent Framework is now generally available for C# and Python, enabling developers to build reliable, persistent agent workflows and orchestrations that run for extended periods within the Microsoft Agent Framework ecosystem.

---

### 118. Generally Available: Private endpoints for Azure Functions durable task scheduler 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Private endpoints for Azure Functions durable task scheduler ](https://azure.microsoft.com/updates?id=578824)

**Update ID**: 578824
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Private endpoints for Azure Functions durable task scheduler are now generally available.

- Key changes or new features  
Developers and IT professionals can now connect Azure Functions and other workloads using the Durable Task SDK to the scheduler via a private IP address. This feature is supported for both Dedicated and Consumption SKU schedulers. Private endpoints enhance security by enabling traffic to flow privately within your virtual network, eliminating exposure to the public internet.

- Target audience affected  
Azure Functions developers, IT professionals managing secure workloads, and teams using Durable Task SDK for orchestrating workflows.

- Important notes  
This update allows for improved network isolation and compliance by leveraging Azure Private Link. To use private endpoints, ensure your virtual network is properly configured and review Azure documentation for best practices. This feature is especially relevant for organizations with strict security requirements or regulatory compliance needs.

**Details**:

**Azure Update Report: Generally Available – Private Endpoints for Azure Functions Durable Task Scheduler**

**Background and Purpose of the Update:**  
Azure Functions is a serverless compute service that enables event-driven execution of code. The Durable Task Scheduler is a core component supporting Durable Functions, which orchestrates stateful workflows. Traditionally, communication between Azure Functions and the scheduler occurred over public endpoints, potentially exposing traffic to the public internet. The purpose of this update is to enhance security and network isolation by enabling private connectivity to the Durable Task Scheduler.

**Specific Features and Detailed Changes:**  
With this update, private endpoints for the Azure Functions Durable Task Scheduler are now generally available for both Dedicated and Consumption SKU schedulers. This means that customers can now establish a private IP address within their Azure Virtual Network (VNet) to securely connect Azure Functions and other workloads that use the Durable Task SDK to the scheduler, without traversing the public internet.

**Technical Mechanisms and Implementation Methods:**  
Private endpoints in Azure are network interfaces that connect you privately and securely to a service powered by Azure Private Link. When configuring a private endpoint for the Durable Task Scheduler, a private IP address from your VNet is assigned to the scheduler resource. All traffic between your Azure Functions app (or other Durable Task SDK workloads) and the scheduler is routed through this private IP, ensuring data remains within the Azure backbone network. This setup eliminates exposure to the public internet and leverages Azure’s internal DNS resolution for service access.

**Use Cases and Application Scenarios:**  
- **Enterprise Security:** Organizations with strict security and compliance requirements can ensure that all communication between their serverless workflows and the Durable Task Scheduler remains private.
- **Regulated Industries:** Financial, healthcare, and government workloads that require data to stay within a private network can benefit from this feature.
- **Hybrid and Multi-tier Applications:** Applications that span multiple VNets or require secure integration with on-premises resources via VPN or ExpressRoute can utilize private endpoints to maintain end-to-end network isolation.

**Important Considerations and Limitations:**  
- This feature is available for both Dedicated and Consumption SKU schedulers, ensuring broad applicability across different Azure Functions hosting plans.
- Configuration of private endpoints requires appropriate permissions and VNet setup.
- All resources that need to communicate with the Durable Task Scheduler must have access to the VNet where the private endpoint is configured.
- DNS configuration may be necessary to ensure that the service resolves to the private endpoint within the VNet.
- There is no mention of support for other SKUs or regions outside those specified.

**Integration with Related Azure Services:**  
Private endpoints for the Durable Task Scheduler can be integrated with other Azure networking and security services, such as:
- **Azure Virtual Network:** For network isolation and segmentation.
- **Network Security Groups (NSGs):** To control inbound and outbound traffic to the private endpoint.
- **Azure Private DNS:** For seamless name resolution to the private endpoint.
- **ExpressRoute/VPN Gateway:** For secure hybrid connectivity from on-premises environments.

**Summary Sentence:**  
Private endpoints for Azure Functions Durable Task Scheduler are now generally available, enabling secure, private connectivity via private IP addresses for both Dedicated and Consumption SKU schedulers, thereby enhancing network isolation and compliance for serverless workflows.

---

### 119. Public Preview: Azure App Service Builder

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure App Service Builder](https://azure.microsoft.com/updates?id=578817)

**Update ID**: 578817
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Mobile, Web, App Service, Microsoft Ignite, Services, Feature

**Summary**:

- What was updated  
Azure App Service Builder is now available in Public Preview.

- Key changes or new features  
Azure App Service Builder streamlines the process of deploying application code to Azure App Service. It provides a source-connected platform that automates build pipelines, deployment workflows, and hosting infrastructure setup. Developers can connect their code repositories (such as GitHub or Azure DevOps), and App Service Builder will handle code build, deployment, and configuration, reducing manual setup and complexity. The platform offers guided workflows, integrated CI/CD, and simplified resource management for web applications.

- Target audience affected  
Developers and IT professionals who deploy web applications to Azure App Service, especially those seeking to reduce manual configuration and accelerate deployment.

- Important notes if any  
This feature is currently in Public Preview and may not be suitable for production workloads. Users should review documentation for supported frameworks and repository types. Feedback is encouraged to help improve the service before general availability.

**Details**:

**Azure Update Report: Public Preview – Azure App Service Builder**

**Background and Purpose of the Update**  
The Azure App Service Builder is introduced to address the complexities developers face when deploying application code to the cloud. Traditionally, this process involves configuring build pipelines, deployment workflows, and managing hosting infrastructure, which can be time-consuming and error-prone. The purpose of this update is to streamline and automate these steps, enabling a more efficient transition from source code to a running cloud application.

**Specific Features and Detailed Changes**  
Azure App Service Builder offers a source-connected platform, allowing developers to directly link their application code repositories to Azure App Service. Key features include:
- Automated build pipeline creation: The platform automatically generates build pipelines based on the connected source code.
- Simplified deployment workflows: Deployment processes are streamlined, reducing manual configuration and intervention.
- Integrated hosting infrastructure: Developers no longer need to manually provision or configure hosting resources, as the Builder handles these tasks.
- Source connection: Direct integration with code repositories (such as GitHub or Azure Repos) for continuous deployment.

**Technical Mechanisms and Implementation Methods**  
The App Service Builder operates by connecting to a source code repository specified by the developer. Upon connection, it analyzes the codebase to determine the appropriate build and deployment steps. The Builder then automatically provisions the necessary Azure App Service resources, configures build pipelines (potentially using Azure DevOps or GitHub Actions), and establishes deployment workflows. This automation reduces the need for custom scripting and manual setup, leveraging Azure’s native orchestration capabilities.

**Use Cases and Application Scenarios**  
- Rapid prototyping: Developers can quickly deploy proof-of-concept applications without extensive pipeline setup.
- Continuous integration/continuous deployment (CI/CD): Teams benefit from automated build and deployment workflows tied directly to their source code.
- Simplified onboarding: New projects or developers unfamiliar with Azure infrastructure can deploy applications with minimal configuration.
- Application modernization: Legacy applications can be migrated to Azure App Service with reduced friction.

**Important Considerations and Limitations**  
- Public Preview status: The service is currently in public preview, which may include limited features, incomplete documentation, and potential instability.
- Repository compatibility: Ensure that your source code repository is supported by the Builder’s integration capabilities.
- Customization constraints: Automated pipelines and workflows may not accommodate highly customized build or deployment requirements.
- Resource provisioning: The Builder provisions hosting infrastructure automatically, but advanced configuration options may be restricted during preview.

**Integration with Related Azure Services**  
Azure App Service Builder integrates natively with Azure App Service for hosting, and connects with source repositories such as GitHub and Azure Repos. It may leverage Azure DevOps or GitHub Actions for pipeline automation. The Builder also aligns with other Azure services for monitoring, scaling, and security, but the primary focus is on simplifying the build and deployment process for App Service-hosted applications.

**Summary Sentence**  
Azure App Service Builder, now in public preview, offers a source-connected platform that automates build pipelines, deployment workflows, and hosting infrastructure, significantly simplifying the process of turning application code into a running cloud app for developers.

---

### 120. Generally Available: Golang support on Azure Functions Flex Consumption

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Golang support on Azure Functions Flex Consumption](https://azure.microsoft.com/updates?id=578812)

**Update ID**: 578812
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, SDK and Tools, Feature

**Summary**:

- What was updated  
Golang (Go) support is now generally available on Azure Functions Flex Consumption.

- Key changes or new features  
Azure Functions Flex Consumption now offers first-class Go support, enabling developers to build serverless functions using Go. The Go worker provides a code-first programming model with typed Go handlers, utilizes standard Go modules for dependency management, and integrates seamlessly with Azure Functions Core Tools and Azure CLI for local development, deployment, and management.

- Target audience affected  
Developers and IT professionals who use Azure Functions, especially those building serverless applications with Go or considering Go for cloud-native workloads.

- Important notes  
This update allows Go developers to leverage Azure Functions Flex Consumption for scalable, event-driven applications with familiar Go tooling and patterns. It supports local development and CI/CD workflows, making it easier to integrate Go functions into existing Azure environments. For more details and documentation, refer to the official Azure update link.

**Details**:

**Azure Update Report: Golang Support on Azure Functions Flex Consumption Now Generally Available**

**Background and Purpose of the Update**  
Azure Functions is a serverless compute platform that enables developers to run event-driven code without managing infrastructure. Traditionally, Azure Functions supported languages such as C#, JavaScript, Python, and Java. The introduction of first-class Go (Golang) support addresses the growing demand for Go in cloud-native and microservices architectures, allowing Go developers to leverage Azure Functions for scalable, event-driven workloads. This update specifically targets the Flex Consumption plan, which offers enhanced flexibility and scalability compared to the traditional Consumption plan.

**Specific Features and Detailed Changes**  
- **First-Class Go Support:** Azure Functions Flex Consumption now natively supports Go, eliminating the need for custom handlers or workarounds.
- **Code-First Programming Model:** Developers can write Azure Functions using typed Go handlers, providing strong type safety and leveraging Go’s native language features.
- **Standard Go Modules:** The platform supports standard Go modules, enabling dependency management and modular code organization.
- **Integration with Azure Functions Core Tools and Azure CLI:** Developers can use familiar tools for local development, deployment, and management of Go-based functions, streamlining the development workflow.

**Technical Mechanisms and Implementation Methods**  
- **Go Worker:** The Go worker is the runtime component responsible for executing Go functions within Azure Functions. It manages the lifecycle of function executions and integrates with the Azure Functions runtime.
- **Typed Handlers:** Functions are defined using typed Go handlers, allowing for clear definition of input and output types, which enhances reliability and maintainability.
- **Module Support:** By supporting Go modules, the platform ensures compatibility with modern Go project structures and dependency management.
- **Tooling Integration:** Azure Functions Core Tools and Azure CLI provide command-line interfaces for creating, testing, and deploying Go functions, enabling seamless integration into CI/CD pipelines and local development environments.

**Use Cases and Application Scenarios**  
- **Event-Driven Microservices:** Go developers can build lightweight, event-driven microservices that respond to HTTP requests, queue messages, or timer triggers.
- **Cloud Automation:** Go-based functions can automate cloud operations, such as resource provisioning or monitoring, using Azure Functions triggers.
- **API Backends:** Developers can implement RESTful APIs in Go, leveraging Azure Functions for scalable backend processing.
- **Data Processing:** Go functions can process data streams, perform ETL operations, or integrate with other Azure services for analytics.

**Important Considerations and Limitations**  
- **Flex Consumption Plan:** Go support is available only on the Flex Consumption plan, not on the traditional Consumption plan or Premium plan.
- **Tooling Requirements:** Developers must use Azure Functions Core Tools and Azure CLI for Go function development and deployment.
- **Language Support:** Only Go is supported in this update; other languages require their respective runtimes.

**Integration with Related Azure Services**  
- **Azure Functions Triggers and Bindings:** Go functions can utilize standard triggers (HTTP, queue, timer) and bindings to interact with Azure services such as Azure Storage, Event Grid, and Service Bus.
- **Azure CLI and Core Tools:** Integration with these tools ensures that Go functions can be managed alongside other Azure resources, supporting automation and DevOps workflows.

**Summary Sentence:**  
First-class Go support on Azure Functions Flex Consumption is now generally available, offering a code-first programming model with typed Go handlers, standard module support, and integration with Azure Functions Core Tools and Azure CLI for streamlined development and deployment.

---

### 121. Public Preview: Azure Functions support for Node.js 26

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Functions support for Node.js 26](https://azure.microsoft.com/updates?id=578807)

**Update ID**: 578807
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, SDK and Tools, Feature

**Summary**:

- What was updated  
Azure Functions now supports Node.js 26 in public preview.

- Key changes or new features  
Developers can run JavaScript and TypeScript function apps using Node.js 26, leveraging the latest language features and performance improvements. This support is available on Linux in the Flex Consumption, Elastic Premium, and Dedicated (App Service) hosting plans. The Azure Functions programming model remains unchanged, enabling seamless migration and compatibility with existing apps.

- Target audience affected  
This update is relevant for developers building serverless applications with Azure Functions, especially those using JavaScript or TypeScript. IT professionals managing Azure Functions deployments on Linux hosting plans are also affected.

- Important notes  
Node.js 26 support is currently in public preview, so it is recommended for evaluation and testing rather than production workloads. Developers should review compatibility and test their apps before migrating. For more details and updates, refer to the official Azure announcement: https://azure.microsoft.com/updates?id=578807

**Details**:

**Azure Update Report: Public Preview – Azure Functions support for Node.js 26**

**Background and Purpose of the Update**  
Azure Functions is a serverless compute platform that enables developers to run event-driven code without managing infrastructure. The update introduces support for Node.js 26 in public preview, reflecting Azure’s commitment to keeping pace with the latest Node.js releases. This allows developers to leverage recent improvements in JavaScript and TypeScript ecosystems, ensuring compatibility and access to new language features and performance enhancements.

**Specific Features and Detailed Changes**  
With this update, Azure Functions now supports Node.js 26 as a runtime environment. Developers can build and deploy function apps using JavaScript or TypeScript targeting Node.js 26, while retaining the established Azure Functions programming model. The support is currently available on Linux, specifically within the Flex Consumption and Elastic Premium hosting plans. This enables developers to evaluate their applications on the new runtime, test compatibility, and utilize Node.js 26 features such as improved performance, enhanced security, and updated language constructs.

**Technical Mechanisms and Implementation Methods**  
The Node.js 26 runtime is integrated into Azure Functions through the platform’s underlying Linux-based hosting infrastructure. When deploying a function app, developers can specify Node.js 26 as the target runtime in their application configuration. The Azure Functions service provisions the appropriate environment, ensuring the function app executes within a containerized instance running Node.js 26. The programming model remains consistent, allowing developers to use triggers, bindings, and other Azure Functions features without modification. The Flex Consumption and Elastic Premium plans provide scalable, event-driven execution with flexible resource allocation.

**Use Cases and Application Scenarios**  
This update is particularly relevant for teams adopting the latest Node.js features or maintaining applications that require compatibility with Node.js 26. Typical scenarios include:  
- Migrating existing function apps from older Node.js versions to Node.js 26 for improved performance and security.  
- Developing new serverless applications that leverage advanced JavaScript/TypeScript syntax and libraries only available in Node.js 26.  
- Testing and validating application behavior on Node.js 26 before full production rollout.  
- Integrating with modern JavaScript frameworks or libraries that require Node.js 26 as a baseline.

**Important Considerations and Limitations**  
The support for Node.js 26 is currently in public preview, meaning it is intended for evaluation and testing rather than production workloads. It is available only on Linux and limited to the Flex Consumption and Elastic Premium hosting plans. Developers should review compatibility with their existing codebase and dependencies, as some packages may not yet fully support Node.js 26. Additionally, preview features may be subject to change and may not offer the same SLA or stability as generally available runtimes.

**Integration with Related Azure Services**  
Function apps running on Node.js 26 can integrate seamlessly with other Azure services, such as Azure Event Grid, Azure Service Bus, Azure Storage, and Azure Application Insights, using triggers and bindings. The update does not alter the integration mechanisms, ensuring that developers can continue to build event-driven architectures and monitor applications using familiar Azure tools.

**Summary Sentence**  
Azure Functions now offers public preview support for Node.js 26 on Linux in Flex Consumption and Elastic Premium plans, enabling developers to evaluate and build JavaScript and TypeScript function apps using the latest Node.js runtime while maintaining the established Azure Functions programming model.

---

### 122. Public Preview: Azure Functions support for Python 3.15

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Functions support for Python 3.15](https://azure.microsoft.com/updates?id=578802)

**Update ID**: 578802
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, SDK and Tools, Feature

**Summary**:

- What was updated  
Azure Functions now supports Python 3.15 in public preview.

- Key changes or new features  
Developers can build, test, and deploy serverless applications using Python 3.15 on Azure Functions. Both v1 and v2 programming models are supported, enabling evaluation of Python applications, dependencies, native extensions, and deployment workflows. This update allows developers to leverage the latest Python features and improvements within Azure Functions.

- Target audience affected  
Python developers and IT professionals working with Azure Functions, especially those interested in upgrading to or testing Python 3.15 in serverless environments.

- Important notes  
This is a public preview, so production workloads are not recommended until general availability. There may be dependency overlaps between the Python worker and application requirements; developers should review compatibility and test their workflows accordingly. Feedback during the preview is encouraged to help improve the offering.

For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=578802

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure Functions support for Python 3.15  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578802)

---

**Background and Purpose of the Update:**  
Azure Functions is a serverless compute platform that enables developers to execute event-driven code without managing infrastructure. The public preview of Python 3.15 support addresses the growing demand for modern Python environments, allowing developers to leverage the latest language features, security improvements, and performance enhancements. This update aims to facilitate the evaluation and adoption of Python 3.15 for serverless workloads, ensuring compatibility with evolving application requirements.

**Specific Features and Detailed Changes:**  
- **Python 3.15 Runtime Support:** Azure Functions now allows developers to build and deploy functions using Python 3.15, in addition to previous versions.
- **Programming Model Compatibility:** Both v1 and v2 programming models are supported, enabling flexibility in function development and migration.
- **Dependency Management:** Developers can test their Python applications, dependencies, and native extensions with Python 3.15, ensuring compatibility and performance.
- **Deployment Workflows:** Existing deployment workflows for Azure Functions can be used with Python 3.15, streamlining integration and minimizing changes for teams adopting the new runtime.

**Technical Mechanisms and Implementation Methods:**  
- **Runtime Environment:** Azure Functions provides a managed Python 3.15 runtime, allowing code execution in a secure and scalable environment.
- **Dependency Handling:** The platform supports dependency installation via requirements.txt, including native extensions, facilitating complex application scenarios.
- **Programming Models:** The v1 model offers a traditional function-based approach, while v2 introduces improved triggers, bindings, and extensibility. Both are available for Python 3.15 functions.
- **Deployment:** Developers can use familiar deployment tools (such as Azure CLI, Visual Studio Code, and GitHub Actions) to publish Python 3.15 functions, leveraging existing CI/CD pipelines.

**Use Cases and Application Scenarios:**  
- **Modern Python Applications:** Teams can migrate or develop new serverless applications using Python 3.15, taking advantage of the latest language features.
- **Dependency Evaluation:** Organizations can test compatibility of their dependencies and native extensions with Python 3.15 in Azure Functions.
- **Event-Driven Workloads:** Typical scenarios include processing messages from Azure Service Bus, responding to HTTP requests, or automating tasks triggered by Azure Blob Storage events.
- **Rapid Prototyping:** The preview enables experimentation with Python 3.15 features in serverless environments before full production adoption.

**Important Considerations and Limitations:**  
- **Preview Status:** Python 3.15 support is currently in public preview. It may not be suitable for production workloads due to potential stability or feature gaps.
- **Dependency Overlap:** The update notes dependency overlap between the Python workflow and Azure Functions, which may require careful management to avoid conflicts.
- **Migration Path:** Existing Python functions may require testing and adjustments when upgrading to Python 3.15, especially for native extensions or complex dependencies.
- **Documentation and Support:** As this is a preview, documentation and community support may be limited compared to stable releases.

**Integration with Related Azure Services:**  
- **Triggers and Bindings:** Python 3.15 functions can integrate with Azure services such as Event Grid, Service Bus, Blob Storage, and Cosmos DB via triggers and bindings.
- **Monitoring and Diagnostics:** Functions can be monitored using Azure Application Insights and Log Analytics for performance and error tracking.
- **CI/CD Integration:** Python 3.15 functions can be deployed using Azure DevOps, GitHub Actions, and other CI/CD tools, ensuring seamless integration with existing workflows.

---

**Summary Sentence:**  
Azure Functions now supports Python 3.15 in public preview, enabling developers to evaluate modern Python applications, dependencies, and deployment workflows using both v1 and v2 programming models, while

---

### 123. Public Preview: Network Watcher rule recommendation

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Network Watcher rule recommendation](https://azure.microsoft.com/updates?id=578797)

**Update ID**: 578797
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher has introduced a rule recommendation feature in public preview.

- Key changes or new features  
The new rule recommendation capability leverages Traffic Analytics insights to proactively identify opportunities to improve network security based on observed network traffic patterns. It analyzes traffic flows and suggests firewall or NSG (Network Security Group) rule optimizations, helping you strengthen your network posture and reduce unnecessary exposure.

- Target audience affected  
This update is relevant for developers, IT professionals, and network administrators managing Azure network resources, especially those responsible for security and compliance.

- Important notes  
The feature is currently in public preview and may not be suitable for production environments. Recommendations are based on observed traffic and should be reviewed before implementation. Integration with Traffic Analytics is required to utilize this capability. For more information and to participate in the preview, refer to the official Azure update link: https://azure.microsoft.com/updates?id=578797

**Details**:

**Azure Update Report: Public Preview – Network Watcher Rule Recommendation**

**Background and Purpose of the Update**  
Azure Network Watcher is a suite of tools for monitoring and diagnosing network conditions in Azure environments. The new Rule Recommendation feature, now in public preview, aims to enhance network security by proactively identifying opportunities for improvement based on observed network traffic. This update addresses the need for automated, data-driven insights to optimize network security configurations, reducing manual analysis and potential misconfigurations.

**Specific Features and Detailed Changes**  
The Rule Recommendation capability leverages Traffic Analytics insights to analyze network traffic patterns and generate actionable recommendations for network security rules. Key features include:
- Automated identification of potential security rule improvements based on real-time traffic data.
- Integration with Traffic Analytics to provide context-aware suggestions.
- Recommendations are surfaced directly within the Network Watcher interface, streamlining the process for IT professionals to review and apply changes.

This update introduces a new workflow within Network Watcher, where users can view recommended rules and assess their impact before implementation.

**Technical Mechanisms and Implementation Methods**  
The feature utilizes Traffic Analytics, which collects and processes flow logs from Azure resources such as Network Security Groups (NSGs). By analyzing these logs, Network Watcher identifies patterns and anomalies in network traffic. The Rule Recommendation engine applies heuristics and security best practices to suggest modifications to NSG rules, such as tightening access controls or removing redundant rules. Recommendations are generated based on observed traffic, ensuring that suggestions are relevant and tailored to the specific environment.

**Use Cases and Application Scenarios**  
- **Proactive Security Hardening:** IT teams can use recommendations to strengthen NSG configurations, minimizing exposure to unnecessary traffic.
- **Compliance Auditing:** Automated suggestions help maintain compliance with organizational or regulatory security standards.
- **Operational Efficiency:** Reduces manual review of flow logs and NSG rules, allowing network administrators to focus on higher-level tasks.
- **Incident Response:** Insights from Traffic Analytics can be used to quickly identify and remediate risky network paths during security incidents.

**Important Considerations and Limitations**  
- The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- Recommendations are based on observed traffic; environments with limited or atypical traffic patterns may not receive comprehensive suggestions.
- Users should carefully review and validate recommendations before applying changes to production environments to avoid unintended disruptions.
- Integration with Traffic Analytics requires proper configuration and enabling of flow logs for relevant resources.

**Integration with Related Azure Services**  
- **Traffic Analytics:** The Rule Recommendation feature is tightly integrated with Traffic Analytics, leveraging its insights for generating recommendations.
- **Network Security Groups (NSGs):** Recommendations are focused on NSG rule optimization, directly impacting resource-level security.
- **Azure Monitor and Log Analytics:** Flow logs processed by Traffic Analytics are stored in Log Analytics workspaces, facilitating deeper investigation and historical analysis.

**Summary Sentence**  
Azure Network Watcher’s new Rule Recommendation feature, now in public preview, enables IT professionals to proactively enhance network security by leveraging Traffic Analytics insights to identify and optimize network security rules based on observed traffic patterns.

---

### 124. Public Preview: Network Watcher Private Link support

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Network Watcher Private Link support](https://azure.microsoft.com/updates?id=578792)

**Update ID**: 578792
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Management and governance, Azure Private Link, Network Watcher, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher VNet Flow Logs now support flow log enrichment for Azure Private Link Service in Public Preview.

- Key changes or new features  
This update enables flow log enrichment specifically for traffic passing through Azure Private Link Service. With this enhancement, Virtual Network Flow Logs can now retain backend flow information, providing deeper visibility into network traffic associated with Private Link connections. This allows users to monitor, analyze, and troubleshoot traffic flows involving Private Link endpoints and services more effectively.

- Target audience affected  
Developers and IT professionals managing Azure networking, especially those using Private Link Service for secure, private connectivity between services.

- Important notes  
This feature is currently in Public Preview, so it may not be suitable for production workloads yet. The enriched flow logs can help improve security monitoring, compliance, and troubleshooting for environments leveraging Private Link. Users should review documentation for configuration steps and limitations during the preview phase.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Network Watcher Private Link support  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578792)

---

**Background and Purpose of the Update:**  
Azure Network Watcher is a core network monitoring and diagnostic service for Azure Virtual Networks (VNets). The purpose of this update is to enhance Network Watcher’s VNet Flow Logs by introducing support for Azure Private Link Service. This addresses the need for improved visibility into network traffic traversing Private Link Service endpoints, which are increasingly used for secure, private connectivity to Azure services and customer-owned resources.

---

**Specific Features and Detailed Changes:**  
- **Flow Log Enrichment for Private Link Service:**  
  VNet Flow Logs now include enriched data specific to traffic flowing through Azure Private Link Service. This enrichment provides greater granularity and context in the logs, enabling IT professionals to distinguish traffic associated with Private Link endpoints.
- **Retention of Backend Flow Information:**  
  Virtual Network Flow Logs will now retain backend flow information related to Private Link Service, offering deeper insight into the communication between clients and the backend resources accessed via Private Link.

---

**Technical Mechanisms and Implementation Methods:**  
- **Flow Log Enrichment:**  
  The enrichment process augments standard flow log entries with metadata specific to Private Link Service traffic. This includes identifying flows associated with Private Link endpoints and backend resources, allowing for more detailed traffic analysis.
- **Data Retention:**  
  Backend flow information is preserved within the flow logs, ensuring that network administrators can trace and audit traffic patterns involving Private Link Service without losing critical context.

---

**Use Cases and Application Scenarios:**  
- **Security Auditing:**  
  Enhanced flow logs allow security teams to monitor and audit traffic to and from Private Link endpoints, helping detect unauthorized access or anomalous behavior.
- **Network Troubleshooting:**  
  IT professionals can leverage enriched flow logs to diagnose connectivity issues related to Private Link Service, such as misconfigured endpoints or unexpected traffic flows.
- **Compliance Reporting:**  
  Organizations with strict compliance requirements can use the detailed flow logs to demonstrate secure and private access to Azure services via Private Link.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:**  
  This feature is currently in public preview. As such, it may not be suitable for production workloads and could be subject to changes or limitations in functionality.
- **Scope of Enrichment:**  
  The enrichment applies specifically to traffic involving Azure Private Link Service. Flows not associated with Private Link endpoints may not benefit from the enhanced visibility.
- **Data Retention Policies:**  
  Users should review their flow log retention policies to ensure that backend flow information is preserved according to organizational requirements.

---

**Integration with Related Azure Services:**  
- **Azure Private Link:**  
  The update directly integrates with Azure Private Link Service, providing visibility into private connectivity scenarios.
- **Azure Monitor and Log Analytics:**  
  Flow logs can be exported to Azure Monitor and Log Analytics for advanced querying, visualization, and alerting.
- **Network Security Groups (NSGs):**  
  Flow logs enriched with Private Link metadata can be used alongside NSG rules to validate and optimize network security configurations.

---

**Summary Sentence:**  
Azure Network Watcher VNet Flow Logs now support flow log enrichment for Azure Private Link Service in public preview, enabling IT professionals to gain deeper visibility and retain backend flow information for traffic traversing Private Link endpoints.

---

### 125. Public Preview: Network Watcher VNet Flow Logs enriched with networkInterfaceIP field

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Network Watcher VNet Flow Logs enriched with networkInterfaceIP field](https://azure.microsoft.com/updates?id=578787)

**Update ID**: 578787
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
Azure Network Watcher VNet Flow Logs now include the networkInterfaceIP field in public preview.

**Key changes or new features:**  
- The new networkInterfaceIP field records the IP address(es) of the network interface where each flow was captured.
- This enhancement provides more granular context for network traffic analysis, enabling easier identification and correlation of flows to specific network interfaces.
- Developers and IT professionals can leverage this data to improve troubleshooting, security auditing, and compliance reporting.

**Target audience affected:**  
- Developers working with Azure networking and monitoring solutions.
- IT professionals responsible for network security, operations, and auditing in Azure environments.

**Important notes:**  
- The feature is currently in public preview and may be subject to changes before general availability.
- The enriched flow logs can help streamline network diagnostics and improve visibility into traffic patterns across VNets.
- Integration with existing log analytics and monitoring workflows may require updates to parsing logic to utilize the new field.

[Azure Update Link](https://azure.microsoft.com/updates?id=578787)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Network Watcher VNet Flow Logs enriched with networkInterfaceIP field  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578787)

---

**Background and Purpose of the Update**  
Azure Network Watcher provides VNet Flow Logs to enable monitoring and analysis of network traffic within virtual networks. Traditionally, flow logs capture information about traffic flows, such as source and destination IPs, ports, protocols, and flow status. However, identifying the specific network interface where a flow was captured could be challenging, especially in environments with multiple IP addresses or interfaces per VM. The purpose of this update is to enhance the context and granularity of flow logs by introducing the `networkInterfaceIP` field, which records the IP address(es) of the network interface where each flow was captured.

**Specific Features and Detailed Changes**  
With this update, VNet Flow Logs now include an additional field: `networkInterfaceIP`. This field contains the IP address or addresses assigned to the network interface that captured the flow. This enhancement provides direct visibility into which interface was responsible for the traffic, improving traceability and simplifying troubleshooting. The change is available in public preview, and the enriched logs are accessible through the usual log delivery mechanisms (such as storage accounts or Log Analytics).

**Technical Mechanisms and Implementation Methods**  
The `networkInterfaceIP` field is populated during the flow log generation process by Network Watcher. When a flow is detected, Network Watcher records not only the flow metadata but also queries the network interface configuration to retrieve the associated IP address(es). This information is then appended to the flow log entry. The mechanism ensures that each flow log record contains accurate interface context, regardless of whether the interface has multiple IPs (e.g., secondary IPs or IP configurations).

**Use Cases and Application Scenarios**  
- **Enhanced Troubleshooting:** Engineers can pinpoint the exact interface responsible for a flow, which is crucial in multi-homed VMs or complex network setups.
- **Security Auditing:** The additional context aids in identifying which interface was used in suspicious or unauthorized flows.
- **Compliance Reporting:** Improved traceability supports compliance requirements by providing detailed records of network activity.
- **Operational Monitoring:** Network operations teams can correlate flows with specific interfaces, facilitating performance analysis and capacity planning.

**Important Considerations and Limitations**  
- The update is currently in public preview, so it may not be suitable for production environments until general availability.
- Only the IP address(es) of the interface are recorded; other interface metadata (such as NIC name or resource ID) is not included.
- The feature is dependent on the underlying configuration of Network Watcher and VNet Flow Logs; ensure that flow logging is correctly enabled and configured.
- Review log storage and retention policies, as enriched logs may increase log size and storage requirements.

**Integration with Related Azure Services**  
- **Azure Monitor:** Enriched flow logs can be ingested into Log Analytics for querying and visualization.
- **Azure Security Center:** Improved context supports security analytics and threat detection.
- **Azure Storage:** Flow logs, including the new field, can be stored in Azure Storage accounts for long-term retention and offline analysis.
- **Azure Sentinel:** Enhanced logs can be used in SIEM workflows for advanced security operations.

---

**Summary Sentence:**  
Azure Network Watcher VNet Flow Logs now include the `networkInterfaceIP` field in public preview, providing enhanced interface context by recording the IP address(es) of the network interface where each flow was captured, thereby improving traceability, troubleshooting, and security analysis for network traffic within Azure virtual networks.

---

### 126. Generally Available: Customer-managed keys for Azure Functions durable task scheduler 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Customer-managed keys for Azure Functions durable task scheduler ](https://azure.microsoft.com/updates?id=578768)

**Update ID**: 578768
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Customer-managed keys (CMK) support is now generally available for Azure Functions Durable Task Scheduler on Dedicated SKU schedulers.

- Key changes or new features  
Organizations can now use their own encryption keys (customer-managed keys) to protect workflow data managed by the Durable Task Scheduler. This enhancement allows for greater control over data security and compliance, enabling customers to meet regulatory requirements by managing encryption keys in Azure Key Vault.

- Target audience affected  
This update primarily impacts developers and IT professionals who use Azure Functions Durable Task Scheduler, especially those in regulated industries or organizations with strict data security and compliance needs. It is relevant for teams deploying workflows on Dedicated SKU schedulers.

- Important notes if any  
CMK support is only available for Dedicated SKU schedulers, not for Consumption or Premium SKUs. To implement CMK, organizations must use Azure Key Vault to manage their keys. This feature helps organizations align with compliance standards such as GDPR, HIPAA, and other industry regulations. Existing Durable Task Scheduler deployments on Dedicated SKUs can now be configured to use CMK for enhanced data protection.

For more details, visit the [Azure Update](https://azure.microsoft.com/updates?id=578768).

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Customer-managed keys for Azure Functions durable task scheduler  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578768)

---

**Background and Purpose of the Update**  
Azure Functions is a serverless compute service enabling event-driven application development. The Durable Task Scheduler is a core component of Azure Functions Durable Functions, orchestrating workflows and managing state. Previously, encryption of workflow data was managed by Microsoft-controlled keys, limiting organizations with strict compliance or regulatory requirements. This update introduces customer-managed keys (CMKs) for the Durable Task Scheduler in Dedicated SKU environments, allowing organizations to control and manage their own encryption keys for workflow data.

**Specific Features and Detailed Changes**  
- **Customer-managed keys (CMKs):** Organizations can now use their own encryption keys, stored in Azure Key Vault, to encrypt workflow data handled by the Durable Task Scheduler.
- **Dedicated SKU Support:** This feature is available for Durable Task Schedulers deployed on Dedicated SKU, ensuring enterprise-grade security and compliance.
- **General Availability:** The feature has moved from preview to general availability, indicating it is fully supported and ready for production use.

**Technical Mechanisms and Implementation Methods**  
- **Key Management:** CMKs are managed via Azure Key Vault, a secure cloud-based key management service. Customers generate, rotate, and revoke keys as needed.
- **Encryption Process:** The Durable Task Scheduler uses the customer-provided keys to encrypt workflow data at rest. The encryption and decryption operations are performed transparently, ensuring data protection without impacting application logic.
- **Configuration:** Administrators configure the Durable Task Scheduler to reference a specific Key Vault and key identifier. Access policies must be set to allow the scheduler to use the keys for encryption and decryption operations.
- **Dedicated SKU Requirement:** The feature is only available for Durable Task Schedulers running on Dedicated SKU, which provides isolated resources and enhanced security.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations subject to regulations such as GDPR, HIPAA, or financial sector requirements can use CMKs to meet data sovereignty and audit requirements.
- **Enterprise Security:** Enterprises with strict internal security policies can maintain control over encryption keys, reducing risk and improving governance.
- **Workflow Data Protection:** Any scenario where workflow state or orchestration data is sensitive, such as business process automation, financial transactions, or healthcare workflows, benefits from CMK support.

**Important Considerations and Limitations**  
- **SKU Restriction:** CMK support is only available for Dedicated SKU schedulers; it is not available for Consumption or Premium SKUs.
- **Key Vault Management:** Proper configuration and maintenance of Azure Key Vault and access policies are required. Misconfiguration may lead to service disruption or data inaccessibility.
- **Key Rotation:** Organizations must plan for key rotation and ensure that the Durable Task Scheduler can access new keys without interruption.
- **Service Integration:** Only workflow data managed by the Durable Task Scheduler is encrypted with CMKs; other Azure Functions components may have separate encryption mechanisms.

**Integration with Related Azure Services**  
- **Azure Key Vault:** Serves as the central repository for managing CMKs, supporting integration with the Durable Task Scheduler.
- **Azure Functions:** The update enhances Azure Functions Durable Functions by providing advanced encryption options for workflow data.
- **Azure Monitoring and Logging:** Organizations should monitor Key Vault access and Durable Task Scheduler operations for compliance and troubleshooting.

---

**Summary Sentence:**  
Customer-managed keys for Azure Functions Durable Task Scheduler are now generally available for Dedicated SKU schedulers, enabling organizations to use their own encryption keys via Azure Key Vault to protect workflow data and meet compliance requirements.

---

### 127. Public Preview: Native disaster recovery for Azure Functions durable task scheduler

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Native disaster recovery for Azure Functions durable task scheduler](https://azure.microsoft.com/updates?id=578762)

**Update ID**: 578762
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Native disaster recovery support for the Azure Functions durable task scheduler is now available in public preview for the Dedicated SKU.

- Key changes or new features  
This update enables automatic recovery of business-critical workflows managed by Durable Functions from regional outages. Developers and IT teams can restore orchestration state without manual intervention or rebuilding workflows. The disaster recovery feature is integrated natively, providing repeatable and reliable failover capabilities for Durable Functions.

- Target audience affected  
Azure Functions users leveraging Durable Functions on the Dedicated SKU, especially developers building workflow-based applications and IT professionals responsible for business continuity and disaster recovery.

- Important notes  
- The feature is currently in public preview and available only in supported Azure regions.  
- It is exclusive to the Dedicated SKU; Consumption and Premium SKUs are not supported.  
- No need to rebuild orchestration state during recovery, simplifying disaster recovery processes.  
- Review region availability and documentation before implementing in production workloads.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=578762

**Details**:

**Azure Update Report**

**Title:** Public Preview: Native disaster recovery for Azure Functions durable task scheduler  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578762)

---

**Background and Purpose of the Update**  
Azure Functions is a serverless compute platform that enables event-driven application development. The Durable Task Scheduler is a core component for orchestrating long-running workflows and stateful functions. Previously, disaster recovery (DR) capabilities for the Durable Task Scheduler required manual intervention or custom solutions, especially when recovering orchestration state after regional outages. The purpose of this update is to introduce native disaster recovery support for the Durable Task Scheduler in Azure Functions, specifically for the Dedicated SKU, allowing seamless recovery of business-critical workflows without the need to rebuild orchestration state.

**Specific Features and Detailed Changes**  
- **Native Disaster Recovery:** This update provides built-in DR functionality for the Durable Task Scheduler, enabling automatic recovery from regional outages.
- **Public Preview Availability:** The feature is currently in public preview and is limited to the Dedicated SKU in supported Azure regions.
- **State Preservation:** Workflows and orchestration state can be recovered without manual reconstruction, ensuring continuity of business processes.
- **Repeatable Recovery:** The DR mechanism is designed to be repeatable, allowing IT teams to reliably restore workflow execution after disruptions.

**Technical Mechanisms and Implementation Methods**  
- **Integration with Durable Task Scheduler:** The DR capability is natively integrated, meaning no additional custom code or external orchestration is required.
- **State Management:** The orchestration state is preserved and can be recovered directly, minimizing downtime and reducing complexity during failover scenarios.
- **Regional Support:** The feature is available in select Azure regions, and is tied to the Dedicated SKU, which provides enhanced performance and isolation for Azure Functions.

**Use Cases and Application Scenarios**  
- **Business-Critical Workflow Recovery:** Organizations running mission-critical workflows on Azure Functions can leverage this feature to ensure high availability and resilience against regional outages.
- **Automated Failover:** IT teams can implement automated failover strategies for orchestrated functions, reducing manual recovery efforts.
- **Compliance and Continuity:** Enterprises with strict compliance requirements can use native DR to meet business continuity and disaster recovery objectives.

**Important Considerations and Limitations**  
- **SKU Limitation:** The feature is only available for the Dedicated SKU, and is not supported on Consumption or Premium SKUs.
- **Regional Availability:** Only supported Azure regions can utilize this feature; IT professionals should verify regional support before planning deployments.
- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads requiring full SLA guarantees. Testing and validation are recommended before adoption.

**Integration with Related Azure Services**  
- **Azure Functions:** The DR feature is tightly integrated with Azure Functions, specifically enhancing the Durable Task Scheduler.
- **Azure Resource Management:** IT teams can leverage Azure’s resource management and monitoring tools to track DR events and orchestrate recovery.
- **Complementary DR Solutions:** This native capability can be combined with other Azure DR and backup solutions for comprehensive protection.

---

**Summary Sentence:**  
Native disaster recovery for Azure Functions durable task scheduler is now available in public preview for the Dedicated SKU in supported Azure regions, enabling seamless recovery of business-critical workflows from regional outages without rebuilding orchestration state.

---

### 128. Public Preview: Durable Task SDK for Go 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Durable Task SDK for Go ](https://azure.microsoft.com/updates?id=578748)

**Update ID**: 578748
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The Durable Task SDK for Go is now available in public preview on Azure.

- Key changes or new features  
Developers can now write orchestrations, activities, and durable entities using Go, leveraging the Durable Task Scheduler for managing execution history and work dispatch. The SDK supports building workflows with retry logic and stateful coordination, enabling robust distributed applications in Go. This expands Durable Task capabilities beyond .NET and Java, providing native support for Go developers.

- Target audience affected  
Go developers building cloud-native, distributed, or workflow-based applications on Azure. IT professionals managing Azure solutions that require durable task orchestration and workflow automation.

- Important notes if any  
This is a public preview release, so production use is not recommended until general availability. Feedback from early adopters is encouraged to help improve the SDK. Documentation and sample code are available to help developers get started. Integration with Azure services and Durable Task Scheduler is supported, but feature parity with other SDKs may be limited during the preview phase.

For more details, visit: https://azure.microsoft.com/updates?id=578748

**Details**:

**Azure Update Report: Public Preview – Durable Task SDK for Go**

**Background and Purpose of the Update**  
The release of the Durable Task SDK for Go in public preview addresses the growing demand for workflow orchestration capabilities within the Go developer community. Previously, Durable Task frameworks were primarily available for languages such as .NET and Python. By introducing Go support, Azure enables developers to leverage durable task orchestration in their Go-based applications, expanding the ecosystem and facilitating the development of scalable, reliable workflows.

**Specific Features and Detailed Changes**  
The Durable Task SDK for Go allows developers to implement orchestrations, activities, and durable entities directly in Go. Orchestrations define the workflow logic, activities represent discrete units of work, and durable entities are stateful objects that persist across workflow executions. The SDK integrates with the Durable Task Scheduler, which manages execution history and work dispatch, ensuring that tasks are executed reliably and can recover from failures. Key features include:

- Authoring orchestrations, activities, and durable entities in Go.
- Management of execution history and work dispatch by the Durable Task Scheduler.
- Built-in support for workflow retries, enabling robust error handling and resilience.

**Technical Mechanisms and Implementation Methods**  
The Durable Task SDK for Go operates by interfacing with the Durable Task Scheduler, which tracks the execution state of orchestrations and activities. When a workflow is initiated, the scheduler records the execution history, allowing for replay and recovery in case of interruptions. Activities are dispatched to workers, and their results are persisted. Durable entities are managed as stateful objects, with their state maintained across workflow invocations. The SDK abstracts these mechanisms, providing Go APIs for defining and invoking orchestrations, activities, and entities, while the underlying scheduler ensures durability and consistency.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations building distributed applications in Go that require reliable workflow orchestration. Typical scenarios include:

- Automated business process workflows (e.g., order processing, approvals).
- Long-running operations that require state persistence and retries.
- Microservices coordination, where orchestrations manage interactions between services.
- Implementing durable stateful entities for scenarios such as inventory management or user session tracking.

**Important Considerations and Limitations**  
As the Durable Task SDK for Go is in public preview, it is intended for evaluation and testing rather than production use. Users should be aware of potential limitations in stability, feature completeness, and support. The SDK relies on the Durable Task Scheduler for execution management, so proper configuration and monitoring of the scheduler are essential. Additionally, developers should review documentation for any restrictions related to workflow complexity, activity execution, and entity state management.

**Integration with Related Azure Services**  
The Durable Task SDK for Go is designed to integrate seamlessly with Azure’s orchestration infrastructure, leveraging the Durable Task Scheduler. It can be used alongside other Azure services that support workflow execution, such as Azure Functions (Durable Functions), though this update specifically focuses on the SDK for Go. Developers can build workflows that interact with Azure storage, messaging, and compute services, enhancing their applications with durable orchestration capabilities.

**Summary Sentence:**  
The public preview of the Durable Task SDK for Go enables developers to build orchestrations, activities, and durable entities in Go, managed by the Durable Task Scheduler, supporting workflow retries and execution history for robust workflow automation within Azure.

---

### 129. Public Preview: Azure Network Watcher – Resource health and topology in connection monitor tests

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Network Watcher – Resource health and topology in connection monitor tests](https://azure.microsoft.com/updates?id=578623)

**Update ID**: 578623
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Management, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher’s Connection Monitor now includes resource health and key performance metrics within its test topology, available in Public Preview.

- Key changes or new features  
Connection Monitor test topology now displays resource health metrics alongside the network path between source and destination. This enhancement leverages Network Watcher topology to provide real-time visibility into the health and performance of network resources involved in monitored connections. Developers and IT professionals can view not only the connectivity path but also the operational status and performance indicators of each resource (such as VMs, gateways, etc.) directly within the topology visualization.

- Target audience affected  
Network administrators, IT professionals, and developers who use Azure Network Watcher for monitoring and troubleshooting network connectivity and performance.

- Important notes if any  
This feature is currently in Public Preview and may not be available in all regions or for all resource types. It offers improved troubleshooting by correlating resource health with network paths, helping users quickly identify and resolve connectivity or performance issues. Users should review documentation for supported resources and limitations during the preview phase.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Network Watcher – Resource health and topology in connection monitor tests  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578623)

---

### Background and Purpose of the Update

Azure Network Watcher’s Connection Monitor is a critical tool for monitoring network connectivity between Azure resources. Previously, Connection Monitor’s topology visualization was limited to displaying the network path between source and destination endpoints. The purpose of this update is to enhance the Connection Monitor by integrating resource health metrics and key performance indicators directly into the test topology, thereby providing a more comprehensive view of the network’s operational state.

---

### Specific Features and Detailed Changes

- **Resource Health Metrics Integration:** Resource health data is now available within Connection Monitor test topology, allowing users to view the health status of each network resource involved in a connectivity test.
- **Key Performance Metrics:** Performance indicators such as latency, packet loss, and other relevant metrics are displayed alongside resource health, offering deeper insight into network performance.
- **Enhanced Topology Visualization:** The topology view is powered by Network Watcher’s topology engine, now enriched with health and performance overlays for each node and link in the path.

---

### Technical Mechanisms and Implementation Methods

- **Data Aggregation:** Connection Monitor collects health and performance metrics from monitored resources and overlays them onto the topology map.
- **Topology Engine:** The visualization leverages Network Watcher’s topology engine, which dynamically maps the network path and now annotates each resource with real-time health and performance data.
- **Resource Health APIs:** The integration utilizes Azure’s resource health APIs to fetch current health status for each resource participating in the connectivity test.

---

### Use Cases and Application Scenarios

- **Network Troubleshooting:** Engineers can quickly identify unhealthy resources or performance bottlenecks within a network path, streamlining root cause analysis.
- **Operational Monitoring:** Real-time visibility into both connectivity and resource health enables proactive monitoring and faster incident response.
- **Performance Optimization:** By correlating performance metrics with resource health, IT professionals can make informed decisions about network optimization and resource scaling.

---

### Important Considerations and Limitations

- **Public Preview Status:** The feature is currently in public preview, which may imply limited support, possible changes, and non-production readiness.
- **Scope of Metrics:** Only resource health and key performance metrics are integrated; other advanced diagnostics may still require separate tools.
- **Resource Coverage:** The update applies to resources involved in Connection Monitor tests; resources outside these tests are not included in the topology visualization.

---

### Integration with Related Azure Services

- **Azure Resource Health:** Direct integration with Azure Resource Health provides up-to-date status for each resource in the topology.
- **Network Watcher:** The topology and monitoring features are built on Network Watcher, ensuring seamless compatibility with existing network diagnostic tools.
- **Connection Monitor:** The update enhances Connection Monitor’s capabilities, making it a more comprehensive solution for network monitoring and diagnostics.

---

**Summary Sentence:**  
This public preview update for Azure Network Watcher Connection Monitor introduces integrated resource health and performance metrics within test topology visualizations, enabling IT professionals to gain deeper insights into network paths and resource status for improved troubleshooting and operational monitoring.

---

### 130. Public Preview: Azure Network Watcher – Connection analyzer

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Network Watcher – Connection analyzer](https://azure.microsoft.com/updates?id=578617)

**Update ID**: 578617
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Networking, Management and governance, Azure ExpressRoute, Network Watcher, Management, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher has introduced the Connection Analyzer for ExpressRoute Circuit in public preview.

- Key changes or new features  
The Connection Analyzer enables faster, evidence-based diagnostics to pinpoint where packet loss occurs on an ExpressRoute circuit. It provides detailed visibility into the path between Azure and on-premises environments, helping users determine whether packet loss is happening within Azure, the ExpressRoute provider, or their on-premises network. This tool streamlines troubleshooting by offering actionable insights and reducing the time required to identify and resolve connectivity issues.

- Target audience affected  
This update is relevant for developers, IT professionals, and network administrators who manage ExpressRoute circuits and require advanced diagnostics for connectivity and performance issues between Azure and on-premises infrastructure.

- Important notes if any  
The Connection Analyzer is currently in public preview, so features and functionality may change before general availability. Users should test the tool in non-production environments and provide feedback to Microsoft. This update is particularly useful for organizations relying on ExpressRoute for critical workloads, as it enhances troubleshooting and reduces downtime related to packet loss.

**Details**:

**Azure Update Report: Public Preview – Azure Network Watcher Connection Analyzer for ExpressRoute Circuit**

**Background and Purpose of the Update:**  
The introduction of the Connection Analyzer for ExpressRoute Circuit in Azure Network Watcher addresses a common challenge faced by IT professionals: diagnosing packet loss between Azure and on-premises environments. Traditionally, identifying the exact location and cause of packet loss within an ExpressRoute circuit has been difficult, often requiring manual investigation and lacking clear evidence. This update aims to streamline and improve the troubleshooting process by providing a faster, evidence-based method to pinpoint packet loss locations.

**Specific Features and Detailed Changes:**  
The Connection Analyzer is a new feature within Azure Network Watcher specifically designed for ExpressRoute circuits. It enables users to analyze network connections and detect where packet loss occurs along the ExpressRoute path. The tool provides diagnostic insights that help distinguish whether packet loss is happening within Azure, the ExpressRoute circuit, or the on-premises infrastructure. This evidence-based approach reduces ambiguity and accelerates root cause analysis.

**Technical Mechanisms and Implementation Methods:**  
The Connection Analyzer leverages Azure Network Watcher’s monitoring and diagnostic capabilities. It systematically tests connectivity across the ExpressRoute circuit, collecting data on packet transmission and loss at various points. The analyzer uses telemetry and packet inspection to identify the segment where packet loss occurs, presenting this information in a structured and actionable format. The technical workflow involves initiating diagnostic probes from Azure to on-premises endpoints (or vice versa), tracking packet flow, and mapping loss events to specific circuit segments.

**Use Cases and Application Scenarios:**  
- **ExpressRoute Troubleshooting:** IT professionals managing hybrid cloud environments can use the Connection Analyzer to quickly diagnose packet loss issues, minimizing downtime and improving service reliability.
- **Performance Optimization:** Network administrators can leverage the tool to proactively monitor ExpressRoute circuits, ensuring optimal connectivity between Azure and on-premises resources.
- **Evidence-Based Support:** The analyzer provides concrete diagnostic data, which can be shared with internal teams or service providers to expedite support and resolution processes.

**Important Considerations and Limitations:**  
- The Connection Analyzer is currently in Public Preview, which means it may not be suitable for production environments and could be subject to changes.
- The feature is specifically designed for ExpressRoute circuits and may not support other types of Azure network connections.
- Users should review Azure documentation for supported regions, prerequisites, and any limitations regarding data collection or diagnostic scope.

**Integration with Related Azure Services:**  
The Connection Analyzer is integrated within Azure Network Watcher, complementing other network monitoring and diagnostic tools such as Connection Monitor, Traffic Analytics, and topology mapping. It enhances the overall visibility and troubleshooting capabilities for ExpressRoute circuits, enabling seamless workflows alongside existing Azure network management solutions.

**Summary Sentence:**  
Azure Network Watcher’s new Connection Analyzer for ExpressRoute Circuit, now in Public Preview, provides IT professionals with a faster, evidence-based method to pinpoint packet loss locations, streamlining troubleshooting and enhancing network reliability between Azure and on-premises environments.

---

### 131. Public Preview: Azure Network Watcher – Auto-create connection monitor

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Network Watcher – Auto-create connection monitor](https://azure.microsoft.com/updates?id=578611)

**Update ID**: 578611
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Management, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher now offers an auto-create feature for Connection Monitor, available in public preview.

- Key changes or new features  
The new auto-create capability enables faster, automated setup of network monitoring across an entire Azure subscription. Previously, Connection Monitor tests had to be configured individually for each region, source, destination, and test configuration. With this update, users can automatically generate monitoring tests for all relevant connections, significantly reducing manual setup time and complexity. This streamlines the process of monitoring network connectivity, performance, and health at scale.

- Target audience affected  
This update is relevant to developers, IT professionals, and network administrators responsible for Azure infrastructure monitoring and management, especially those overseeing large or multi-region deployments.

- Important notes  
The auto-create feature is currently in public preview, so it may not be suitable for production workloads yet. Users should review documentation and test the feature in non-production environments. This update can help organizations improve visibility and troubleshooting across their Azure networks by simplifying the setup of Connection Monitor tests. For more details and usage instructions, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=578611

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Network Watcher – Auto-create connection monitor  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=578611)

---

### Background and Purpose of the Update

Azure Network Watcher is a suite of network monitoring and diagnostic tools designed to provide visibility into Azure network resources. Traditionally, configuring Connection Monitor required manual creation of tests for each connection, region, source, destination, and test configuration. This process was time-consuming and complex, especially for large-scale environments. The purpose of this update is to streamline and accelerate the setup of network monitoring across an entire Azure subscription, reducing operational overhead and improving scalability.

---

### Specific Features and Detailed Changes

The "Auto-create connection monitor" feature introduces automation to the Connection Monitor setup process. Instead of manually configuring individual tests, users can now automatically generate connection monitors for multiple resources across their subscription. This enhancement enables rapid deployment of monitoring configurations and ensures comprehensive coverage with minimal manual intervention.

Key changes include:
- Automated creation of connection monitor tests for multiple connections.
- Simplified configuration process, eliminating the need to specify each region, source, destination, and test individually.
- Faster setup for monitoring network connectivity across distributed Azure resources.

---

### Technical Mechanisms and Implementation Methods

The auto-create functionality leverages Azure Network Watcher’s API and orchestration capabilities to scan the subscription and identify eligible resources for monitoring. Upon activation, the system automatically provisions connection monitor tests based on predefined criteria and available network endpoints. The mechanism abstracts the complexity of manual configuration, allowing IT professionals to initiate monitoring with a single action.

Technical steps include:
- Initiating the auto-create process via Azure Portal, CLI, or API.
- The system enumerates network resources (such as VMs, VNets, and endpoints) across the subscription.
- Connection monitor tests are generated and deployed for each identified connection.
- Monitoring begins immediately, with results accessible through Network Watcher dashboards and logs.

---

### Use Cases and Application Scenarios

This update is particularly beneficial for:
- Enterprises managing large-scale Azure deployments with multiple regions and network endpoints.
- IT teams seeking to establish baseline connectivity monitoring rapidly during migration or expansion phases.
- Scenarios requiring comprehensive monitoring coverage without manual configuration, such as compliance audits or troubleshooting distributed applications.

---

### Important Considerations and Limitations

- The feature is currently in Public Preview and may be subject to changes or limitations in functionality.
- Users should verify compatibility with existing network architectures and ensure that auto-generated monitors align with organizational monitoring policies.
- Manual customization of individual tests may still be required for specialized scenarios.
- Preview features may not be supported in all Azure regions or may have restricted API access.

---

### Integration with Related Azure Services

Auto-create connection monitor integrates seamlessly with other Azure Network Watcher tools, including topology, traffic analytics, and diagnostic logs. It can be used alongside Azure Monitor for centralized alerting and reporting. The automated monitoring setup complements Azure Security Center by providing additional visibility into network connectivity and potential issues.

---

**Summary Sentence:**  
The auto-create connection monitor feature in Azure Network Watcher, now in public preview, enables rapid and automated deployment of network connectivity monitoring across an entire Azure subscription, significantly reducing manual configuration effort and improving scalability for IT professionals.

---

### 132. Public Preview: Azure Network Watcher – AI summary of connection troubleshoot results

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Network Watcher – AI summary of connection troubleshoot results](https://azure.microsoft.com/updates?id=578602)

**Update ID**: 578602
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Management, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher now offers AI-summarized connection troubleshoot results in Public Preview.

- Key changes or new features  
The new feature uses AI to generate concise summaries of connectivity test results, making it easier and faster to interpret diagnostic data. Connection troubleshoot runs four distinct tests to analyze network paths, and the AI summarizes the findings from these tests, highlighting key issues and actionable insights. This enhancement reduces manual effort required to review complex network diagnostics and helps users quickly identify connectivity problems.

- Target audience affected  
Developers, IT professionals, and network administrators who use Azure Network Watcher for diagnosing and troubleshooting network connectivity issues.

- Important notes if any  
The AI summary feature is currently in Public Preview and may evolve based on user feedback. It streamlines troubleshooting workflows, but users should still review detailed results for comprehensive analysis or compliance requirements. Integration with API data allows automated access to summarized results, supporting programmatic workflows and custom monitoring solutions.

For more information, visit the official Azure Update page: [Azure Network Watcher – AI summary of connection troubleshoot results](https://azure.microsoft.com/updates?id=578602)

**Details**:

**Azure Update Report: Public Preview – Azure Network Watcher: AI Summary of Connection Troubleshoot Results**

**Background and Purpose of the Update**  
Azure Network Watcher provides tools for monitoring and diagnosing network issues within Azure environments. Traditionally, the "Connection Troubleshoot" feature generates detailed diagnostic results from multiple tests, requiring manual interpretation by IT professionals. The purpose of this update is to introduce AI-summarized results, enabling users to quickly and clearly understand the outcome of connectivity tests, thereby reducing the time and expertise needed to analyze complex network paths.

**Specific Features and Detailed Changes**  
The update adds an AI-powered summary layer to the existing Connection Troubleshoot tool in Azure Network Watcher. When a connectivity test is performed, the results from four diagnostic tests are now automatically processed and summarized by AI. This summary provides a concise, actionable overview of the network path and connectivity status, highlighting key findings and potential issues without requiring users to manually review each diagnostic output.

**Technical Mechanisms and Implementation Methods**  
The AI summary feature leverages machine learning models trained on network diagnostic data. After a Connection Troubleshoot operation, the AI processes the outputs from the four diagnostic tests, which may include checks such as reachability, routing, firewall rules, and endpoint status. The AI then synthesizes these results into a human-readable summary, focusing on clarity and relevance. This mechanism is integrated directly into the Network Watcher interface, requiring no additional configuration or deployment from the user.

**Use Cases and Application Scenarios**  
- **Rapid Incident Response:** IT professionals can use the AI summary to quickly identify connectivity issues during outages or performance degradation, accelerating troubleshooting workflows.
- **Routine Network Health Checks:** Automated summaries allow for efficient periodic reviews of network paths, supporting proactive maintenance and compliance checks.
- **Complex Network Environments:** In scenarios involving multi-tier architectures or hybrid cloud setups, the AI summary helps distill complex diagnostic data into actionable insights, reducing cognitive load for engineers.
- **Onboarding and Training:** New team members or less experienced staff can leverage AI summaries to understand network issues without deep expertise in Azure networking diagnostics.

**Important Considerations and Limitations**  
- **Preview Feature:** This capability is currently in public preview, meaning it may not be fully supported or available in all regions, and feedback is encouraged for further refinement.
- **Interpretation Accuracy:** While AI summaries are designed to be clear and actionable, users should validate findings against the full diagnostic outputs for critical or high-impact scenarios.
- **Scope of Analysis:** The AI summary is limited to the results of the four diagnostic tests run by Connection Troubleshoot; it does not incorporate external or custom network monitoring data.
- **Security and Privacy:** Users should ensure that diagnostic data processed by the AI complies with organizational security and privacy policies.

**Integration with Related Azure Services**  
The AI summary feature is natively integrated within Azure Network Watcher and complements existing diagnostic tools such as Network Security Group (NSG) flow logs, topology mapping, and packet capture. It can be used alongside Azure Monitor and Azure Security Center for holistic network visibility and incident management.

**Summary Sentence**  
The AI-summarized connection troubleshoot results in Azure Network Watcher provide IT professionals with a faster, clearer understanding of connectivity test outcomes, streamlining network diagnostics and accelerating issue resolution.

---

### 133. Public Preview: SQL Server 2025 support on Ubuntu 26.04 LTS 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: SQL Server 2025 support on Ubuntu 26.04 LTS ](https://azure.microsoft.com/updates?id=578579)

**Update ID**: 578579
**Data source**: Azure Updates API

**Categories**: In preview, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Public Preview support for SQL Server 2025 on Ubuntu 26.04 LTS.

- Key changes or new features  
SQL Server 2025 can now be installed, evaluated, tested, and deployed on Ubuntu 26.04 LTS, Canonical’s latest long-term supported Linux distribution. This update enables developers and IT professionals to leverage the newest features of SQL Server 2025 on a modern, secure, and stable platform. It also ensures compatibility with the latest Linux kernel and system libraries, improving performance and reliability.

- Target audience affected  
Developers and IT professionals who use SQL Server on Linux, especially those planning to upgrade to Ubuntu 26.04 LTS or adopt SQL Server 2025 in their environments.

- Important notes if any  
This is a Public Preview release, intended for testing and evaluation purposes. Production workloads should wait for General Availability. Users are encouraged to provide feedback and report issues during the preview phase. For installation instructions and known limitations, refer to official documentation.

**Details**:

**Background and Purpose of the Update**  
The announcement introduces the Public Preview of SQL Server 2025 support on Ubuntu 26.04 LTS. This update is aimed at enabling IT professionals and organizations to evaluate, test, and deploy SQL Server on Canonical’s latest long-term supported Linux distribution. The purpose is to ensure compatibility and leverage the stability and security enhancements of Ubuntu 26.04 LTS, aligning SQL Server deployments with modern Linux environments.

**Specific Features and Detailed Changes**  
With this update, SQL Server 2025 can now be installed and operated on Ubuntu 26.04 LTS. This marks a significant expansion in platform support, as previous SQL Server versions were limited to earlier Ubuntu releases. The update allows users to utilize SQL Server’s latest features and improvements on the newest LTS version, which typically includes updated kernel versions, improved package management, and enhanced security features. The Public Preview status indicates that users can begin testing and evaluating SQL Server 2025 on Ubuntu 26.04 LTS, providing feedback and identifying potential issues before general availability.

**Technical Mechanisms and Implementation Methods**  
SQL Server 2025 installation on Ubuntu 26.04 LTS follows standard Linux deployment practices, utilizing Canonical’s package repositories and tools such as apt for installation and updates. The integration leverages Ubuntu’s LTS (Long-Term Support) infrastructure, ensuring extended support and maintenance for both the OS and SQL Server. During the Public Preview, users are encouraged to deploy SQL Server in test environments, validate compatibility with their workloads, and assess performance and reliability on Ubuntu 26.04 LTS.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations that standardize on Ubuntu for their server infrastructure and require the latest SQL Server features. Typical scenarios include development and testing of new applications, migration planning from older Ubuntu versions, and evaluation of SQL Server 2025’s capabilities in a Linux environment. It also benefits enterprises seeking to modernize their database platforms while maintaining the stability and security offered by Ubuntu LTS releases.

**Important Considerations and Limitations**  
As this is a Public Preview, SQL Server 2025 on Ubuntu 26.04 LTS should not be used for production workloads. IT professionals should be aware that preview releases may contain unresolved issues, limited support, and incomplete documentation. It is recommended to thoroughly test all critical workloads and configurations before considering production deployment. Additionally, compatibility with existing tools, extensions, and integrations should be validated during the preview phase.

**Integration with Related Azure Services**  
SQL Server 2025 on Ubuntu 26.04 LTS can be deployed on Azure virtual machines, allowing organizations to leverage Azure’s infrastructure, scalability, and management capabilities. Integration with Azure services such as Azure Backup, Azure Monitor, and Azure Security Center remains consistent, enabling comprehensive management and monitoring of SQL Server instances. This update facilitates hybrid and cloud-native scenarios, supporting seamless migration and deployment strategies within the Azure ecosystem.

**Summary Sentence**  
The Public Preview of SQL Server 2025 support on Ubuntu 26.04 LTS enables IT professionals to evaluate and test the latest SQL Server features on Canonical’s newest long-term supported Linux platform, providing expanded compatibility and integration options within Azure environments.

---

### 134. Generally Available: Azure SQL updates for mid-November 2026 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure SQL updates for mid-November 2026 ](https://azure.microsoft.com/updates?id=578471)

**Update ID**: 578471
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL received new updates and enhancements in mid-November 2026.

- Key changes or new features  
The primary feature introduced is fuzzy string matching. This allows users to compare strings based on similarity, not just exact matches. Built-in functions now support fuzzy matching, enabling more flexible and intelligent text comparison in queries and applications.

- Target audience affected  
Developers and IT professionals working with Azure SQL databases, especially those implementing search, data cleansing, deduplication, or matching logic in their applications.

- Important notes if any  
Fuzzy string matching can improve data quality and user experience in scenarios where exact string matches are insufficient (e.g., handling typos, variant spellings, or inconsistent data). Developers should review the new built-in functions and consider updating their SQL queries or application logic to leverage this feature. For more details and usage examples, refer to the official Azure documentation.

**Details**:

**Azure SQL Update Report – Mid-November 2026**

**Background and Purpose of the Update:**  
The mid-November 2026 Azure SQL update introduces enhancements aimed at improving data comparison capabilities within Azure SQL databases. The primary focus is on enabling fuzzy string matching, which addresses the need for more flexible and intelligent string comparison operations. This update is designed to help IT professionals and developers handle scenarios where exact string matches are insufficient, such as data cleansing, deduplication, and similarity-based queries.

**Specific Features and Detailed Changes:**  
The key feature in this update is the introduction of fuzzy string matching functionality. Azure SQL now provides built-in functions that allow users to compare strings based on similarity rather than strict equality. This enhancement enables the identification of records that are similar but not identical, facilitating tasks such as finding near-duplicate entries or matching user input with existing data despite minor typographical errors.

**Technical Mechanisms and Implementation Methods:**  
Fuzzy string matching is implemented through new built-in functions within Azure SQL. These functions utilize algorithms that calculate similarity scores between strings, enabling queries to return results based on a defined threshold of similarity. The mechanism typically involves comparing character sequences, assessing edit distances (such as Levenshtein distance), or using other similarity metrics. The functions are integrated into T-SQL, allowing seamless use within SQL queries and stored procedures. This implementation ensures that fuzzy matching operations can be performed natively within the database engine, optimizing performance and reducing the need for external processing.

**Use Cases and Application Scenarios:**  
- **Data Deduplication:** Identifying and merging records that are similar but not exactly the same, such as customer names with minor spelling differences.
- **Data Cleansing:** Detecting and correcting inconsistencies in datasets, especially in large-scale ETL processes.
- **User Input Matching:** Enhancing search functionality by matching user queries to database entries despite typographical errors or variations.
- **Fraud Detection:** Recognizing patterns where similar data entries may indicate fraudulent activity.
- **Customer Relationship Management (CRM):** Improving contact matching and reducing duplicate records in CRM systems.

**Important Considerations and Limitations:**  
When utilizing fuzzy string matching, IT professionals should consider the computational overhead associated with similarity calculations, especially on large datasets. Performance may vary depending on the complexity of the matching algorithm and the volume of data processed. It is important to define appropriate similarity thresholds to balance accuracy and result relevance. Additionally, fuzzy matching may not be suitable for all data types or scenarios; careful validation is recommended to avoid false positives or negatives.

**Integration with Related Azure Services:**  
The fuzzy string matching functions are natively available within Azure SQL, ensuring compatibility with other Azure services that interact with SQL databases, such as Azure Data Factory, Azure Synapse Analytics, and Power BI. This integration allows for enhanced data processing and analytics workflows, leveraging fuzzy matching capabilities in ETL pipelines, reporting, and business intelligence solutions.

**Summary:**  
Azure SQL’s mid-November 2026 update introduces built-in fuzzy string matching functions, enabling similarity-based string comparisons for improved data quality, deduplication, and search accuracy. This enhancement is natively integrated into Azure SQL, supporting a wide range of data processing and analytics scenarios for IT professionals.

---

### 135. Generally Available: Azure SQL Managed Instance updates for mid-November 2026 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure SQL Managed Instance updates for mid-November 2026 ](https://azure.microsoft.com/updates?id=578465)

**Update ID**: 578465
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure SQL Managed Instance, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL Managed Instance received performance enhancements in mid-November 2026, specifically for Next-gen General Purpose instances.

- Key changes or new features  
The update boosts transaction throughput by increasing log rates up to 220 MiB/s. This improvement enables higher performance for workloads requiring rapid transaction processing and log-intensive operations.

- Target audience affected  
Developers and IT professionals managing or deploying applications on Azure SQL Managed Instance, especially those using Next-gen General Purpose tier, will benefit from these enhancements. Teams running high-volume transactional systems, such as financial, retail, or telemetry workloads, are particularly impacted.

- Important notes  
The increased log rate directly improves the scalability and responsiveness of database operations. Existing workloads may experience improved performance without requiring code changes, but teams should monitor workloads to optimize resource utilization. Review documentation for any prerequisites or configuration steps to leverage the new log rate capabilities. This update is generally available and can be adopted in production environments.

**Details**:

**Azure Update Report: Azure SQL Managed Instance Updates for Mid-November 2026**

**Background and Purpose of the Update**  
The mid-November 2026 update for Azure SQL Managed Instance focuses on enhancing performance, specifically targeting transaction throughput. The primary goal is to address scalability and efficiency requirements for workloads that demand high-volume transactional processing. This update is part of Azure’s ongoing commitment to improve managed database services, ensuring that customers can handle larger and more complex workloads with greater reliability and speed.

**Specific Features and Detailed Changes**  
The update introduces a significant boost in transaction throughput for the Next-gen General Purpose tier of Azure SQL Managed Instance. The most notable enhancement is the increase in log rates, now supporting up to 220 MiB/s. This improvement directly impacts the speed at which transactions are processed and logged, reducing latency and increasing the overall efficiency of database operations. The update also implies higher performance, though the detailed scope of performance improvements is not specified beyond log rate increases.

**Technical Mechanisms and Implementation Methods**  
The update leverages improvements in the underlying storage and logging architecture of Azure SQL Managed Instance. By increasing the maximum log rate to 220 MiB/s, the platform can accommodate more concurrent transactions and faster commit operations. This is achieved through optimizations in disk I/O, network throughput, and internal database engine processes. The enhancements are applied to the Next-gen General Purpose tier, ensuring that customers using this tier benefit from improved transaction logging without manual intervention.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations running high-throughput transactional workloads, such as financial systems, e-commerce platforms, and real-time analytics applications. Scenarios where rapid transaction processing and logging are critical—such as batch processing, ETL operations, and mission-critical business applications—will see tangible performance gains. The increased log rate allows for faster data ingestion, reduced transaction bottlenecks, and improved responsiveness in applications relying on Azure SQL Managed Instance.

**Important Considerations and Limitations**  
IT professionals should note that the enhanced log rate is specific to the Next-gen General Purpose tier of Azure SQL Managed Instance. Workloads must be provisioned on this tier to take advantage of the update. Additionally, while log rate improvements can significantly boost throughput, overall performance is still subject to other factors such as CPU, memory, and network limits. Proper workload sizing and monitoring remain essential to maximize the benefits of this update. There may also be limitations regarding compatibility with legacy workloads or configurations not optimized for high log rates.

**Integration with Related Azure Services**  
Azure SQL Managed Instance integrates seamlessly with other Azure services, including Azure Backup, Azure Monitor, and Azure Security Center. The increased log rate can improve backup and restore operations, as faster transaction logging may reduce backup windows and enhance data protection strategies. Integration with Azure Monitor allows for real-time tracking of performance metrics, enabling proactive management of throughput and resource utilization. The update also supports advanced security and compliance features, ensuring that high-throughput workloads remain protected within the Azure ecosystem.

**Summary Sentence**  
In mid-November 2026, Azure SQL Managed Instance Next-gen General Purpose tier received an update that increases transaction throughput by boosting log rates up to 220 MiB/s, enabling improved performance for high-volume transactional workloads.

---

### 136. Public Preview:  AI-assisted data modeler and other updates in Azure Cosmos DB extension for VS Code 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview:  AI-assisted data modeler and other updates in Azure Cosmos DB extension for VS Code ](https://azure.microsoft.com/updates?id=578444)

**Update ID**: 578444
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
The Azure Cosmos DB extension for Visual Studio Code has introduced a public preview of the AI-assisted Data Modeler, along with other enhancements.

**Key changes or new features:**  
- **AI-assisted Data Modeler:** This new feature helps developers design optimal Cosmos DB data models early in the development process. It leverages AI to analyze document structure, query patterns, write distribution, expected scale, and anticipated data growth.
- **Enhanced modeling workflow:** The extension now supports more efficient modeling, allowing users to iterate and refine their data models directly within VS Code.
- **Additional updates:** Other improvements to the extension may include usability enhancements and expanded support for Cosmos DB features (see release notes for details).

**Target audience affected:**  
- Developers building applications with Azure Cosmos DB, especially those using VS Code for development.
- IT professionals and database architects responsible for designing and optimizing NoSQL data models.

**Important notes:**  
- The AI-assisted Data Modeler is currently in public preview and may evolve based on user feedback.
- Early adoption can help teams identify potential data modeling issues before production, improving performance and scalability.
- For full details and guidance, refer to the official Azure Update announcement: [link](https://azure.microsoft.com/updates?id=578444).

**Details**:

**Azure Update Report: Public Preview – AI-assisted Data Modeler and Other Updates in Azure Cosmos DB Extension for VS Code**

**Background and Purpose of the Update:**  
This update introduces an AI-assisted Data Modeler within the Azure Cosmos DB extension for Visual Studio Code, now available in public preview. The purpose is to enable developers and database architects to design optimized Azure Cosmos DB data models earlier in the application development lifecycle. By integrating this capability into VS Code, Microsoft aims to streamline the data modeling process, reduce manual effort, and improve the quality and scalability of Cosmos DB solutions from the outset.

**Specific Features and Detailed Changes:**  
The primary feature is the AI-assisted Data Modeler, which provides intelligent recommendations and guidance for designing data models tailored to Cosmos DB. Key aspects include:
- **Document Structure Analysis:** The tool examines the structure of your JSON documents to suggest optimal data organization.
- **Query Pattern Evaluation:** It assesses intended query patterns to recommend data modeling strategies that enhance query performance.
- **Write Distribution Insights:** The modeler analyzes how data writes are distributed, helping to avoid hot partitions and ensure even throughput.
- **Expected Scale and Data Growth Considerations:** It factors in projected data volume and growth, offering guidance to ensure the model remains efficient as the dataset scales.

These features are integrated directly into the Azure Cosmos DB extension for VS Code, allowing users to access them within their existing development environment.

**Technical Mechanisms and Implementation Methods:**  
The AI-assisted Data Modeler leverages machine learning algorithms to analyze user-provided data samples, query definitions, and anticipated usage patterns. It processes this information locally within the VS Code extension, generating recommendations for partition keys, indexing strategies, and document schema design. The tool is designed to be interactive, providing real-time feedback and suggestions as users iterate on their data models.

**Use Cases and Application Scenarios:**  
- **Early-stage Application Design:** Teams can use the AI-assisted Data Modeler during the initial phases of application development to ensure their Cosmos DB data models are well-architected.
- **Performance Optimization:** Developers can refine existing data models based on recommendations that consider actual or expected query and write patterns.
- **Scalability Planning:** Organizations anticipating significant data growth can use the tool to validate that their data models will scale efficiently with Cosmos DB’s distributed architecture.
- **Developer Productivity:** By integrating into VS Code, the feature supports rapid prototyping and iterative development workflows.

**Important Considerations and Limitations:**  
- The AI-assisted Data Modeler is currently in public preview, which may mean limited support and potential changes before general availability.
- Recommendations are based on the information provided (document samples, queries, expected scale). Incomplete or inaccurate input may affect the quality of suggestions.
- The update does not specify support for all Cosmos DB APIs or data types; users should verify compatibility with their specific use case.
- As a preview feature, it may not be suitable for production-critical workloads without additional validation.

**Integration with Related Azure Services:**  
The Data Modeler is part of the Azure Cosmos DB extension for Visual Studio Code, which integrates with Azure Resource Manager for deployment and management of Cosmos DB resources. While the update focuses on Cosmos DB, the extension can be used alongside other Azure development tools within VS Code, supporting end-to-end cloud-native application development workflows.

**Summary Sentence:**  
The public preview of the AI-assisted Data Modeler in the Azure Cosmos DB extension for VS Code provides intelligent, context-aware guidance for designing scalable and performant data models, streamlining the development process and enhancing early-stage architectural decisions for Cosmos DB solutions.

---

### 137. Generally Available: Azure Cosmos DB Shell 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Cosmos DB Shell ](https://azure.microsoft.com/updates?id=578439)

**Update ID**: 578439
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cosmos DB Shell is now generally available.

- Key changes or new features  
The Azure Cosmos DB Shell introduces a command-line interface (CLI) for interacting with Azure Cosmos DB. It offers a consistent, scriptable workflow for database navigation, management, and querying. The shell is designed to simplify tasks for both humans and AI agents, supporting automation and integration scenarios. Users can execute commands, manage resources, and run scripts directly against Cosmos DB, streamlining development and operational processes.

- Target audience affected  
Developers and IT professionals working with Azure Cosmos DB, especially those who prefer or require CLI-based workflows, automation, or integration with DevOps pipelines.

- Important notes if any  
The shell supports common database operations and is suitable for both manual and automated tasks. It enhances productivity by enabling scripting and batch operations, and can be integrated with other tools and workflows. For more information and usage details, refer to the official Azure update: https://azure.microsoft.com/updates?id=578439

**Details**:

**Azure Update Report: Generally Available – Azure Cosmos DB Shell**

**Background and Purpose of the Update**  
The general availability of Azure Cosmos DB Shell marks a significant enhancement in the developer and operational experience for Azure Cosmos DB. The primary purpose of this update is to provide a command-line interface (CLI) that streamlines interactions with Azure Cosmos DB, benefiting both human users and AI agents. By offering a consistent and scriptable workflow, the Cosmos DB Shell aims to simplify database management, query execution, and automation tasks, thereby improving productivity and operational efficiency.

**Specific Features and Detailed Changes**  
Azure Cosmos DB Shell introduces a command-line experience tailored for Azure Cosmos DB. Key features include:
- **Scriptable Workflow:** Users can execute commands and scripts directly within the shell, enabling automation and repeatable database operations.
- **Consistency:** The shell provides a uniform interface for interacting with Cosmos DB, reducing the learning curve and ensuring predictable behavior across environments.
- **AI Agent Compatibility:** The shell is designed to facilitate integration with AI agents, allowing automated processes and intelligent applications to interact with Cosmos DB programmatically.
- **Navigation:** Enhanced navigation capabilities enable users to browse and manage database resources efficiently.

**Technical Mechanisms and Implementation Methods**  
The Cosmos DB Shell operates as a CLI tool, interfacing with Azure Cosmos DB through secure API calls. It leverages Azure authentication mechanisms to ensure secure access and supports scripting languages for automation. The shell abstracts underlying REST API operations, presenting them as intuitive commands that can be chained or scripted. This approach reduces manual effort and minimizes errors associated with direct API usage.

**Use Cases and Application Scenarios**  
- **Database Administration:** IT professionals can use the shell for routine tasks such as provisioning, scaling, and monitoring Cosmos DB resources.
- **Development and Testing:** Developers can automate data setup, schema management, and query testing within CI/CD pipelines using the shell.
- **AI Integration:** AI agents can utilize the shell to perform dynamic data operations, supporting intelligent applications that require real-time database interaction.
- **Scripting and Automation:** The shell is ideal for creating repeatable scripts for backup, migration, or batch processing tasks.

**Important Considerations and Limitations**  
- **Security:** Proper authentication and authorization are required to use the shell, following Azure’s security best practices.
- **Compatibility:** The shell is designed specifically for Azure Cosmos DB and may not support other Azure database services.
- **Script Limitations:** While the shell supports scripting, users should be aware of potential limitations in command syntax or supported operations, especially for complex workflows.
- **Resource Management:** Users must ensure that scripts and commands executed via the shell do not inadvertently impact database performance or incur unexpected costs.

**Integration with Related Azure Services**  
Azure Cosmos DB Shell integrates seamlessly with Azure’s authentication and resource management services. It can be incorporated into broader Azure workflows, such as Azure DevOps pipelines, Azure Functions, and automation scripts, enabling end-to-end management of Cosmos DB resources within the Azure ecosystem. The shell also supports integration with AI agents, facilitating intelligent automation and data-driven applications.

**Summary Sentence:**  
Azure Cosmos DB Shell is now generally available, offering a consistent, scriptable command-line interface that simplifies and automates interactions with Azure Cosmos DB for both IT professionals and AI agents.

---

### 138. Public Preview: Managed MCP Server in Azure Cosmos DB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Managed MCP Server in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=578434)

**Update ID**: 578434
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

**What was updated**  
Azure Cosmos DB now offers a public preview of a managed MCP (Memory and Context Provider) server, enabling a hosted MCP experience.

**Key changes or new features**  
- Enterprise AI agents can securely connect to business data in Cosmos DB via a standard, managed MCP endpoint.  
- Agents can discover database schemas, retrieve documents, and perform full-text and vector search operations.  
- The managed MCP server simplifies integration for AI applications, providing a consistent interface for accessing and interacting with Cosmos DB data.

**Target audience affected**  
- Developers building AI agents or applications that require secure, scalable access to business data stored in Azure Cosmos DB.  
- IT professionals responsible for managing data access, security, and integration with enterprise AI solutions.

**Important notes**  
- The feature is currently in public preview; production workloads should be approached with caution.  
- The managed MCP endpoint streamlines AI agent connectivity and reduces custom integration overhead.  
- Supports advanced search and retrieval capabilities, enhancing AI-driven business solutions.  
- Documentation and API details are available for developers to start integrating with the managed MCP server.

[Azure Update Link](https://azure.microsoft.com/updates?id=578434)

**Details**:

**Azure Update Report: Public Preview – Managed MCP Server in Azure Cosmos DB**

**Background and Purpose of the Update**  
Azure Cosmos DB introduces the public preview of a managed MCP (Managed Connection Protocol) server experience. This update is designed to facilitate enterprise AI agents in securely accessing business data stored in Cosmos DB. The primary goal is to provide a standardized, managed MCP endpoint that simplifies integration and enhances security for AI-driven applications requiring direct interaction with enterprise data.

**Specific Features and Detailed Changes**  
- **Hosted MCP Endpoint:** Azure Cosmos DB now offers a managed MCP endpoint, eliminating the need for customers to deploy or maintain their own MCP servers.
- **Schema Discovery:** AI agents can programmatically discover database schemas, enabling dynamic understanding and interaction with data structures.
- **Document Retrieval:** Agents can retrieve documents from Cosmos DB using the MCP endpoint, supporting both structured and unstructured data access.
- **Full-Text and Vector Search:** The MCP server supports advanced search capabilities, including full-text and vector search, allowing AI agents to perform semantic queries and retrieve relevant information efficiently.

**Technical Mechanisms and Implementation Methods**  
The managed MCP server is hosted directly within Azure Cosmos DB, providing a secure and scalable interface for AI agents. The MCP endpoint adheres to standard protocols, ensuring compatibility with enterprise applications. Security is enforced through Azure-managed authentication and authorization mechanisms, leveraging Azure Active Directory and role-based access control (RBAC). Schema discovery and document retrieval are facilitated via API calls to the MCP endpoint, which abstracts the underlying Cosmos DB data model. Full-text and vector search functionalities are integrated into the MCP server, enabling advanced querying without additional infrastructure.

**Use Cases and Application Scenarios**  
- **Enterprise AI Agents:** AI-powered applications, such as chatbots or virtual assistants, can securely access business data for tasks like answering queries, generating reports, or automating workflows.
- **Data Integration:** Organizations can streamline data access for analytics and reporting tools, reducing complexity and improving data governance.
- **Semantic Search:** Applications requiring semantic understanding of business documents can leverage vector search for enhanced relevance and accuracy.
- **Schema-Aware Automation:** Automated systems can dynamically adapt to evolving data schemas, improving robustness and reducing maintenance overhead.

**Important Considerations and Limitations**  
- **Preview Status:** The managed MCP server is currently in public preview; production workloads should be approached with caution and monitored for stability.
- **Security and Compliance:** While the MCP endpoint is managed and secured by Azure, organizations must ensure proper configuration of authentication and access policies.
- **Feature Scope:** The preview may not support all Cosmos DB features or advanced MCP functionalities; users should consult official documentation for supported capabilities.
- **Performance and Scalability:** As a managed service, performance characteristics may differ from self-hosted MCP solutions; testing is recommended for mission-critical applications.

**Integration with Related Azure Services**  
- **Azure Active Directory:** Authentication and authorization for MCP endpoints are integrated with Azure AD, supporting enterprise identity management.
- **Azure Cosmos DB:** The MCP server operates natively within Cosmos DB, leveraging its scalability, global distribution, and multi-model support.
- **AI and Analytics Services:** The managed MCP endpoint can be consumed by Azure AI services, Power BI, and other analytics platforms for seamless data access.

**Summary Sentence**  
Azure Cosmos DB now offers a managed MCP server in public preview, enabling enterprise AI agents to securely connect to business data via a standardized endpoint with schema discovery, document retrieval, and advanced search capabilities.

---

### 139. Generally Available: Azure HorizonDB now available in 15 regions

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure HorizonDB now available in 15 regions](https://azure.microsoft.com/updates?id=578314)

**Update ID**: 578314
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure HorizonDB is now generally available in 15 Azure regions.

- Key changes or new features  
The regional expansion allows users to deploy HorizonDB (a managed PostgreSQL-compatible database) in more locations worldwide. This enables improved performance, lower latency, and greater flexibility for PostgreSQL workloads by placing databases closer to applications and end-users.

- Target audience affected  
Developers building applications with PostgreSQL, IT professionals managing cloud databases, and organizations seeking scalable, globally distributed database solutions on Azure.

- Important notes  
With HorizonDB available in more regions, customers can optimize their architecture for compliance, disaster recovery, and data residency requirements. The expanded regional support also facilitates easier scaling and integration with other Azure services. Developers and IT teams should review the updated regional list to plan deployments and ensure optimal resource placement.

**Details**:

**Azure Update Report: Azure HorizonDB General Availability in 15 Regions**

**Background and Purpose of the Update**  
Azure HorizonDB, a managed database service optimized for PostgreSQL workloads, is now generally available in 15 Azure regions. The primary purpose of this update is to provide IT professionals and organizations with enhanced flexibility and control over the geographic placement of their database resources. By expanding regional availability, Azure enables users to deploy HorizonDB instances closer to their applications and end-users, thereby reducing latency and improving performance.

**Specific Features and Detailed Changes**  
The key change in this update is the increased regional footprint of Azure HorizonDB. Previously limited to fewer regions, HorizonDB can now be provisioned in 15 distinct Azure regions. This expansion allows customers to select from a broader set of locations when deploying PostgreSQL workloads. The update does not introduce new features to HorizonDB itself but significantly improves deployment options and scalability by leveraging Azure’s global infrastructure.

**Technical Mechanisms and Implementation Methods**  
Azure HorizonDB utilizes Azure’s regional architecture to deliver managed PostgreSQL database services. When deploying HorizonDB, users can select their preferred region from the Azure portal or via API/CLI, ensuring that the database instance is provisioned within the chosen geographic location. This regional selection is critical for optimizing network latency, complying with data residency requirements, and aligning with application architecture. Azure manages the underlying infrastructure, including high availability, automated backups, and security, while customers focus on their PostgreSQL workloads.

**Use Cases and Application Scenarios**  
- **Latency-sensitive Applications:** Deploying HorizonDB in regions closer to application servers or end-users minimizes latency, which is crucial for real-time analytics, transactional systems, and interactive web applications.
- **Global SaaS Deployments:** Organizations with a global customer base can leverage the expanded regional availability to provide localized database services, improving user experience and meeting regional compliance requirements.
- **Disaster Recovery and High Availability:** With HorizonDB available in multiple regions, customers can architect robust disaster recovery solutions and multi-region failover strategies.
- **Regulatory Compliance:** Businesses subject to data residency laws can now deploy HorizonDB in specific regions to ensure compliance with local regulations.

**Important Considerations and Limitations**  
- **Regional Feature Parity:** While HorizonDB is available in 15 regions, IT professionals should verify that all required features and performance tiers are supported in their chosen region, as Azure services sometimes have regional variations.
- **Data Residency and Compliance:** Selecting the appropriate region is essential for compliance with data protection laws. Customers must ensure that their data does not cross regional boundaries if restricted by regulations.
- **Networking and Connectivity:** Deploying HorizonDB in a region geographically distant from application servers may introduce latency. Proper network planning is recommended to optimize performance.
- **Cost Implications:** Pricing may vary by region due to infrastructure and operational costs; customers should review the Azure pricing calculator for region-specific rates.

**Integration with Related Azure Services**  
Azure HorizonDB integrates seamlessly with other Azure services, such as Azure Virtual Machines, Azure Kubernetes Service, and Azure App Service, enabling customers to build scalable, cloud-native applications. It also supports Azure networking features (VNet integration, private endpoints) and can be monitored using Azure Monitor and Azure Security Center. The expanded regional availability enhances these integrations by allowing customers to architect solutions with optimal proximity and performance.

**Summary Sentence**  
Azure HorizonDB is now generally available in 15 Azure regions, providing IT professionals with greater flexibility to deploy PostgreSQL workloads closer to their applications and users, thereby optimizing performance, compliance, and scalability.

---

### 140. Public Preview: Fine-grained role-based access control for databases and collections in Azure DocumentDB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Fine-grained role-based access control for databases and collections in Azure DocumentDB ](https://azure.microsoft.com/updates?id=578262)

**Update ID**: 578262
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DocumentDB introduces fine-grained role-based access control (RBAC) at the database and collection levels, now available in Public Preview.

- Key changes or new features  
Previously, RBAC in DocumentDB was limited to cluster-level permissions. With this update, administrators and developers can assign roles and permissions at the database and collection levels, enabling more precise control over who can access and modify specific data. This allows organizations to enforce least-privilege access, improve security, and better align access policies with business requirements.

- Target audience affected  
Developers and IT professionals managing Azure DocumentDB environments, especially those requiring detailed access control for compliance or security purposes.

- Important notes  
This feature is currently in Public Preview and may undergo changes before general availability. Existing cluster-level RBAC remains supported, but transitioning to database/collection-level RBAC is recommended for enhanced security and flexibility. Review the documentation for guidance on configuring roles and permissions. Integration with Azure Active Directory (AAD) is supported for seamless identity management.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=578262).

**Details**:

**Azure Update Report: Public Preview – Fine-grained Role-Based Access Control for Databases and Collections in Azure DocumentDB**

---

**Background and Purpose of the Update:**

Previously, Azure DocumentDB (now part of Azure Cosmos DB) provided role-based access control (RBAC) primarily at the cluster level. This meant that permissions were broadly applied, limiting the ability to restrict access to specific databases or collections within a cluster. The purpose of this update is to introduce more granular RBAC capabilities, allowing IT professionals and administrators to enforce security policies at the database and collection levels. This enhancement addresses the need for tighter data governance, compliance, and least-privilege access in multi-tenant or complex application environments.

---

**Specific Features and Detailed Changes:**

- **Granular RBAC:** The update enables RBAC not only at the cluster level but also at the database and collection levels. Administrators can now assign roles and permissions with greater specificity.
- **Database-Level Permissions:** Users can be granted access to individual databases within a DocumentDB cluster, restricting visibility and operations to only the assigned database.
- **Collection-Level Permissions:** Access can be further refined to specific collections within a database, enabling scenarios where users or applications only interact with designated data sets.
- **Role Assignment:** Roles can be mapped to users, groups, or service principals, allowing integration with Azure Active Directory (AAD) for identity management.

---

**Technical Mechanisms and Implementation Methods:**

- **RBAC Configuration:** Permissions are defined and assigned using Azure’s RBAC model, typically through the Azure Portal, Azure CLI, or ARM templates.
- **Scope Definition:** The scope for role assignment can now be set at the database or collection level, in addition to the existing cluster level.
- **Integration with AAD:** Role assignments leverage Azure Active Directory identities, enabling centralized authentication and authorization.
- **Access Enforcement:** When a user or application attempts to access a database or collection, DocumentDB evaluates the assigned roles and permissions at the relevant scope, enforcing access controls accordingly.

---

**Use Cases and Application Scenarios:**

- **Multi-Tenant Applications:** Organizations hosting multiple tenants within a single DocumentDB cluster can now restrict each tenant’s access to their own database or collection.
- **Departmental Data Segregation:** Enterprises can enforce access policies so that departments or teams only access their designated collections, improving data security and compliance.
- **Least-Privilege Principle:** Developers and applications can be granted only the necessary permissions to specific collections, reducing the risk of unauthorized data access.

---

**Important Considerations and Limitations:**

- **Public Preview:** This feature is currently in public preview. It may not be suitable for production workloads until general availability and full support are announced.
- **Migration:** Existing cluster-level RBAC configurations may need to be reviewed and updated to leverage database and collection-level controls.
- **Compatibility:** Ensure that client SDKs and application code are compatible with the new RBAC model, especially if leveraging scoped permissions.
- **Audit and Monitoring:** Organizations should update their monitoring and auditing strategies to track access at the finer-grained levels.

---

**Integration with Related Azure Services:**

- **Azure Active Directory:** Fine-grained RBAC integrates with AAD for identity management, supporting user, group, and service principal assignments.
- **Azure Portal and CLI:** Management and configuration of roles and permissions are supported through Azure’s standard administrative tools.
- **Compliance and Security Solutions:** Enhanced RBAC supports integration with Azure security and compliance offerings, such as Azure Policy and Azure Monitor, for improved governance.

---

**Summary Sentence:**

Azure DocumentDB now supports fine-grained role-based access control at the database and collection levels in public preview, enabling more precise data access management and improved security for complex and multi-tenant environments.

---

### 141. Public Preview: DocumentDB on Azure Local 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: DocumentDB on Azure Local ](https://azure.microsoft.com/updates?id=578255)

**Update ID**: 578255
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure has announced the public preview of DocumentDB on Azure Local, enabling MongoDB-compatible document workloads to run on customer-owned infrastructure.

- Key changes or new features  
DocumentDB on Azure Local allows organizations to deploy document database workloads (compatible with MongoDB APIs) directly within their own datacenters, retail locations, or edge environments. This update supports application and data co-location, reducing latency and helping meet data residency or sovereignty requirements. Developers can use familiar MongoDB tools and drivers, while IT professionals gain flexibility in managing data infrastructure outside Azure’s public cloud.

- Target audience affected  
Developers building applications with MongoDB-compatible databases and IT professionals managing infrastructure in on-premises, retail, or edge environments. Organizations with strict latency or data-location requirements will benefit most.

- Important notes  
This is a public preview, so features and performance may evolve. DocumentDB on Azure Local enables hybrid and edge scenarios, but users should review compatibility and support details before production use. Azure Local provides a consistent management experience for local deployments.

Link: [Azure Update](https://azure.microsoft.com/updates?id=578255)

**Details**:

**Azure Update Report: Public Preview – DocumentDB on Azure Local**

**Background and Purpose of the Update**  
The public preview of DocumentDB on Azure Local introduces the capability to run MongoDB-compatible document workloads directly on customer-managed infrastructure. This update addresses the increasing demand for deploying applications and their associated data closer together, which is critical for minimizing latency and meeting data residency requirements. By enabling DocumentDB on Azure Local, organizations can leverage Azure’s document database technology in environments such as datacenters and retail locations, where proximity and control over data are essential.

**Specific Features and Detailed Changes**  
- **MongoDB Compatibility:** DocumentDB on Azure Local supports MongoDB-compatible workloads, allowing applications that use MongoDB drivers and APIs to operate seamlessly without significant code changes.
- **Local Deployment:** The service can be deployed on-premises or in edge environments, enabling organizations to maintain control over their data and application infrastructure.
- **Data Proximity:** Applications and their data can be co-located, reducing network latency and improving performance for data-intensive operations.
- **Public Preview Availability:** The feature is currently in public preview, allowing IT professionals to test and evaluate its capabilities before general availability.

**Technical Mechanisms and Implementation Methods**  
DocumentDB on Azure Local leverages Azure’s hybrid and edge deployment capabilities. The service is designed to run on customer-owned hardware, integrating with local infrastructure while maintaining compatibility with MongoDB protocols. Deployment is managed through Azure Local, which provides orchestration and lifecycle management for Azure services outside the public cloud. The implementation ensures that document workloads are processed locally, with data stored and accessed within the customer’s environment, rather than being transmitted to Azure’s public regions.

**Use Cases and Application Scenarios**  
- **Datacenter Deployments:** Organizations with private datacenters can run document workloads locally, ensuring compliance with data residency regulations and reducing dependency on external cloud connectivity.
- **Retail Environments:** Retailers can deploy DocumentDB on Azure Local in stores or regional hubs, supporting point-of-sale, inventory, and customer analytics applications that require low-latency access to data.
- **Edge Computing:** Scenarios where applications must operate in remote or disconnected environments benefit from local data processing and storage, such as manufacturing sites or healthcare facilities.

**Important Considerations and Limitations**  
- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should evaluate stability, performance, and support limitations before deployment.
- **Infrastructure Requirements:** Customers must provide and manage their own hardware and networking infrastructure to host DocumentDB on Azure Local.
- **Data Management:** Data stored locally is managed by the customer, and integration with Azure’s centralized services may require additional configuration.
- **Compliance and Security:** Organizations must ensure that local deployments meet their internal compliance and security standards, as Azure’s standard controls may not apply outside the public cloud.

**Integration with Related Azure Services**  
DocumentDB on Azure Local is part of Azure’s broader hybrid and edge strategy, complementing services such as Azure Arc and Azure Stack. It enables seamless integration with Azure’s management and monitoring tools, allowing IT professionals to orchestrate, monitor, and manage document workloads alongside other Azure services. Applications can be designed to synchronize data between local and cloud environments, supporting hybrid architectures and disaster recovery scenarios.

**Summary Sentence**  
The public preview of DocumentDB on Azure Local empowers IT professionals to deploy MongoDB-compatible document workloads on their own infrastructure, addressing latency and data-location requirements in datacenters and retail environments, while leveraging Azure’s hybrid capabilities.

---

### 142. Public Preview: DocumentDB enabled by Azure Arc

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: DocumentDB enabled by Azure Arc](https://azure.microsoft.com/updates?id=578242)

**Update ID**: 578242
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Databases, Azure Arc, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure announced the public preview of DocumentDB enabled by Azure Arc.

- Key changes or new features  
DocumentDB can now be deployed on Azure Arc-enabled Kubernetes clusters, allowing you to run MongoDB-compatible document workloads across on-premises, edge, and multicloud environments. This enables flexible data architecture, letting developers and IT teams manage and scale DocumentDB outside of Azure while maintaining cloud-native management, security, and monitoring capabilities.

- Target audience affected  
Developers building applications with MongoDB-compatible workloads, IT professionals managing hybrid or multicloud infrastructure, and organizations seeking to modernize their data estate with Azure Arc.

- Important notes  
This preview lets you leverage DocumentDB’s features in distributed environments, supporting scenarios where data locality, regulatory compliance, or edge processing are required. Integration with Azure Arc ensures unified management and governance. Review supported Kubernetes platforms and prerequisites before deployment.  
For more details, see the official Azure Update: [Public Preview: DocumentDB enabled by Azure Arc](https://azure.microsoft.com/updates?id=578242).

**Details**:

**Azure Update Report: Public Preview – DocumentDB enabled by Azure Arc**

**Background and Purpose of the Update**  
This update introduces DocumentDB enabled by Azure Arc in public preview. The primary goal is to allow IT professionals to deploy DocumentDB on Azure Arc-enabled Kubernetes clusters, extending the reach of DocumentDB beyond Azure’s native cloud environment to on-premises, edge, and multicloud infrastructures. This enables organizations to run MongoDB-compatible document workloads wherever their applications reside, addressing requirements for data locality, regulatory compliance, and hybrid cloud flexibility.

**Specific Features and Detailed Changes**  
- **Deployment Flexibility:** DocumentDB can now be provisioned on any Azure Arc-enabled Kubernetes cluster, not just within Azure. This includes clusters running in private datacenters, edge locations, or other public clouds.
- **MongoDB Compatibility:** The DocumentDB instance supports MongoDB-compatible document workloads, ensuring seamless integration with applications expecting MongoDB APIs.
- **Arc Integration:** The deployment and management of DocumentDB are orchestrated through Azure Arc, providing a unified control plane for hybrid and multicloud environments.

**Technical Mechanisms and Implementation Methods**  
- **Azure Arc-Enabled Kubernetes:** Azure Arc acts as a bridge, connecting non-Azure Kubernetes clusters to Azure’s management and governance capabilities. DocumentDB is deployed as containerized workloads on these clusters.
- **Resource Management:** Once deployed, DocumentDB instances are managed via Azure Portal, CLI, or ARM templates, leveraging Azure Arc’s resource management capabilities.
- **Data Plane Operations:** Applications interact with DocumentDB using MongoDB-compatible drivers and protocols, ensuring compatibility with existing MongoDB-based solutions.
- **Control Plane Operations:** Azure Arc provides lifecycle management, monitoring, and governance for DocumentDB instances, regardless of their physical location.

**Use Cases and Application Scenarios**  
- **On-Premises Deployments:** Enterprises can run DocumentDB in their own datacenters to meet data residency or latency requirements.
- **Edge Computing:** DocumentDB can be deployed at edge locations to support applications that require local data processing and storage.
- **Multicloud Strategies:** Organizations with workloads distributed across multiple public clouds can deploy DocumentDB instances in each environment, maintaining consistent management via Azure Arc.
- **Regulatory Compliance:** Deploying DocumentDB outside Azure enables compliance with strict data sovereignty regulations.

**Important Considerations and Limitations**  
- **Supported Environments:** DocumentDB is only available on Azure Arc-enabled Kubernetes clusters. Ensure your cluster meets Azure Arc’s prerequisites.
- **Preview Status:** This feature is currently in public preview. Production workloads should be approached with caution, and users should monitor for updates regarding general availability.
- **Compatibility:** While DocumentDB is MongoDB-compatible, verify the supported MongoDB API versions and features for your workload.
- **Management Overhead:** Running DocumentDB outside Azure may require additional operational considerations, such as cluster maintenance and network connectivity.

**Integration with Related Azure Services**  
- **Azure Portal and Management Tools:** DocumentDB instances are managed alongside other Azure resources, providing a consistent experience.
- **Azure Arc:** Acts as the foundational integration layer, enabling hybrid and multicloud deployments and management.
- **Azure Monitoring and Governance:** DocumentDB instances benefit from Azure’s monitoring, security, and policy management capabilities via Arc.

**Summary Sentence:**  
The public preview of DocumentDB enabled by Azure Arc allows IT professionals to deploy and manage MongoDB-compatible document workloads on Azure Arc-enabled Kubernetes clusters across on-premises, edge, and multicloud environments, providing flexible data locality and unified management through Azure’s control plane.

---

### 143. Generally Available: DocumentDB extension for VS Code 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: DocumentDB extension for VS Code ](https://azure.microsoft.com/updates?id=578237)

**Update ID**: 578237
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
The DocumentDB extension for Visual Studio Code is now generally available.

- Key changes or new features  
This free, open-source extension enables developers to connect to Azure DocumentDB and the open-source DocumentDB project directly from VS Code. It supports any workload compatible with the MongoDB API, allowing users to manage databases, collections, and documents within the VS Code environment. The extension streamlines development workflows by providing integrated tools for querying, editing, and visualizing DocumentDB data.

- Target audience affected  
Developers and IT professionals working with Azure DocumentDB, open-source DocumentDB, or MongoDB API-compatible databases, especially those using Visual Studio Code as their primary IDE.

- Important notes if any  
The extension is open-source and free to use. It enhances productivity by enabling direct database access and management within VS Code, reducing context switching. Developers can use it for local development, testing, and production workloads. For more details and installation instructions, refer to the official Azure Update link: https://azure.microsoft.com/updates?id=578237

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: DocumentDB extension for VS Code

**Background and Purpose of the Update:**  
The DocumentDB extension for Visual Studio Code (VS Code) has reached general availability. This update is intended to streamline development workflows by enabling direct integration of Azure DocumentDB and the open-source DocumentDB project within the VS Code environment. The extension is designed to support any workload compatible with the MongoDB API, addressing the needs of developers who work with DocumentDB or MongoDB-compatible databases. The purpose is to provide a free, open-source tool that simplifies database management, query execution, and development tasks without leaving the VS Code interface.

**Specific Features and Detailed Changes:**  
- **General Availability:** The extension is now stable and ready for production use, having moved out of preview or beta stages.
- **Azure DocumentDB Support:** Users can connect directly to Azure DocumentDB instances, allowing for management and interaction with cloud-hosted DocumentDB databases.
- **Open-source DocumentDB Project Support:** The extension also supports the open-source DocumentDB project, enabling developers to work with local or self-hosted DocumentDB instances.
- **MongoDB API Compatibility:** Any workload that is compatible with the MongoDB API can be managed through the extension, broadening its applicability to a variety of database scenarios.
- **Integration with VS Code:** The extension operates natively within VS Code, leveraging its UI and workflow for database operations.

**Technical Mechanisms and Implementation Methods:**  
The DocumentDB extension is implemented as a free, open-source plugin for VS Code. It utilizes the MongoDB API compatibility layer to connect to both Azure DocumentDB and open-source DocumentDB instances. The extension likely leverages VS Code’s extension APIs to provide features such as connection management, database browsing, query execution, and result visualization. By operating within VS Code, the extension allows developers to interact with DocumentDB databases using familiar tools and interfaces, reducing context switching and improving productivity.

**Use Cases and Application Scenarios:**  
- **Cloud Database Management:** Developers can manage Azure DocumentDB databases directly from VS Code, including tasks such as viewing collections, running queries, and modifying documents.
- **Local Development:** The extension supports open-source DocumentDB instances, enabling developers to test and develop locally before deploying to Azure.
- **MongoDB-Compatible Workloads:** Any application or workload using the MongoDB API can be managed through the extension, making it suitable for teams migrating from MongoDB to DocumentDB or working in hybrid environments.
- **Integrated Development Workflow:** The extension allows database operations to be performed alongside code editing, debugging, and deployment tasks within VS Code.

**Important Considerations and Limitations:**  
- **API Compatibility:** The extension is specifically designed for MongoDB API-compatible workloads. Non-compatible workloads or databases may not be supported.
- **Connection Requirements:** Users must have appropriate access credentials and network connectivity to connect to Azure DocumentDB or open-source DocumentDB instances.
- **Extension Scope:** The extension’s features are limited to what is provided within VS Code and may not cover all advanced database management tasks available through Azure Portal or other tools.

**Integration with Related Azure Services:**  
The extension facilitates direct integration with Azure DocumentDB, allowing seamless management of cloud-hosted databases from within VS Code. This enhances the developer experience by bridging the gap between Azure services and local development environments. The extension can be used in conjunction with other Azure tools and services, such as Azure Resource Manager, Azure DevOps, and CI/CD pipelines, to streamline database development and deployment workflows.

**Summary Sentence:**  
The DocumentDB extension for VS Code is now generally available, providing a free, open-source solution for managing Azure DocumentDB and MongoDB API-compatible workloads directly within the Visual Studio Code environment.

---

### 144. Public Preview: Full-text search in Azure DocumentDB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Full-text search in Azure DocumentDB ](https://azure.microsoft.com/updates?id=578232)

**Update ID**: 578232
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure DocumentDB now supports full-text search capabilities in public preview.

- Key changes or new features  
Developers can leverage BM25 indexing for improved relevance-based sorting and access to relevance scores when querying documents. The update introduces fuzzy search to handle typos and proximity search to find documents where search terms appear close together. These features enhance search accuracy and user experience within DocumentDB.

- Target audience affected  
This update is relevant for developers building applications on Azure DocumentDB, as well as IT professionals managing DocumentDB instances. Teams implementing search functionality in their applications will benefit from the improved search features.

- Important notes if any  
The full-text search features are currently in public preview, so they may not be suitable for production workloads yet. Users should test and validate these features in development environments. Documentation and API support are available for integration, but feedback is encouraged to help improve the service before general availability.

**Details**:

**Azure Update Report: Public Preview – Full-text Search in Azure DocumentDB**

**Background and Purpose of the Update:**  
Azure DocumentDB, a NoSQL document database service, is introducing full-text search capabilities in public preview. The primary purpose of this update is to enhance DocumentDB’s querying functionality by enabling users to perform advanced text-based searches directly within their document collections. This addresses the need for more sophisticated search operations, such as relevance ranking and typo tolerance, which are increasingly important for applications handling large volumes of unstructured or semi-structured data.

**Specific Features and Detailed Changes:**  
The update introduces several key features:

- **BM25 Indexing:** DocumentDB now supports BM25, a probabilistic-based ranking function widely used in information retrieval. This enables relevance-based sorting of search results, allowing users to retrieve documents most pertinent to their query.
- **Relevance Scores:** Search results include relevance scores, providing quantitative measures of how well each document matches the search criteria.
- **Fuzzy Search:** This feature allows the search engine to handle typographical errors and variations in search terms, improving user experience and result accuracy.
- **Proximity Search:** Users can find documents where search terms occur near one another, supporting more nuanced queries and content discovery.

These features collectively enable richer, more flexible search experiences within DocumentDB collections.

**Technical Mechanisms and Implementation Methods:**  
Full-text search in DocumentDB leverages BM25 indexing for relevance computation. When a document is ingested, the text content is tokenized and indexed according to the BM25 algorithm, which considers term frequency and document length to calculate relevance scores during search operations. Fuzzy search is implemented by allowing approximate matches to query terms, typically using edit distance algorithms. Proximity search is achieved by tracking the positions of terms within documents and enabling queries that specify maximum distances between terms.

The search operations are exposed via new query syntax or API endpoints, allowing developers to specify search parameters such as fuzziness level or proximity constraints. The relevance scores are returned as part of the query response, enabling client-side sorting or filtering.

**Use Cases and Application Scenarios:**  
- **Content Management Systems:** Enables users to search for documents, articles, or records with typo tolerance and relevance ranking.
- **Customer Support Knowledge Bases:** Allows end-users to find relevant support articles even with misspelled queries.
- **E-commerce Catalogs:** Supports product searches where users may enter incomplete or approximate product names.
- **Legal and Compliance Document Repositories:** Facilitates discovery of documents containing related terms in close proximity, useful for contextual searches.

**Important Considerations and Limitations:**  
- The feature is currently in public preview, which implies that it may not be production-ready and could be subject to changes or limitations in functionality and performance.
- Users should evaluate the preview features in non-critical environments and monitor for updates or changes before deploying in production.
- Integration with existing DocumentDB indexing and querying mechanisms may require schema or query adjustments to leverage full-text search capabilities.
- Performance and scalability characteristics should be validated for large datasets, as full-text search can be resource-intensive.

**Integration with Related Azure Services:**  
Full-text search in DocumentDB can complement other Azure services such as Azure Cognitive Search for more advanced search scenarios or analytics. It may also integrate with Azure Functions for automated search workflows and Azure Logic Apps for orchestrating document search and retrieval processes. However, this update is specific to DocumentDB and does not imply direct integration with external search services.

**Summary Sentence:**  
Azure DocumentDB now offers full-text search in public preview, featuring BM25 indexing, relevance-based sorting, fuzzy and proximity search, and access to relevance scores, enabling advanced and flexible text search capabilities within document collections.

---

### 145. Public Preview: Azure Network Watcher – Packet capture insights

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Network Watcher – Packet capture insights](https://azure.microsoft.com/updates?id=578172)

**Update ID**: 578172
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Networking, Network Watcher, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Network Watcher introduces Packet Capture Insights in public preview.

- Key changes or new features  
Packet Capture Insights leverages AI-assisted analysis to automatically highlight key findings from packet captures. It enables ingestion of structured protocol logs into Azure Log Analytics for deeper investigation and correlation. This update improves accessibility and usability of packet capture data, making it easier to identify issues and anomalies without manual inspection.

- Target audience affected  
Developers and IT professionals responsible for network monitoring, troubleshooting, and security analysis in Azure environments.

- Important notes  
This feature streamlines packet analysis by surfacing actionable insights, reducing the time and expertise needed to interpret raw capture data. Integration with Log Analytics allows for advanced querying and visualization, supporting more efficient root cause analysis and incident response. As this is a public preview, users should test and validate the feature in non-production environments before broad adoption.

**Details**:

**Azure Update Report: Public Preview – Azure Network Watcher: Packet Capture Insights**

**Background and Purpose of the Update**  
Azure Network Watcher is a core network diagnostic and monitoring tool within Azure, enabling IT professionals to capture and analyze network traffic for troubleshooting and security purposes. Traditionally, packet capture data is voluminous and complex, requiring manual analysis to extract actionable insights. The purpose of the Packet Capture Insights update is to enhance the accessibility and utility of packet capture data by leveraging AI-assisted analysis, thereby streamlining the identification of key findings and facilitating deeper investigations.

**Specific Features and Detailed Changes**  
The update introduces "Packet Capture Insights" as a new capability within Azure Network Watcher. Key features include:

- **AI-Assisted Analysis**: Automated extraction of significant findings from packet capture files, reducing manual effort and highlighting anomalies, performance issues, or security threats.
- **Structured Protocol Log Ingestion**: Packet capture data can now be ingested as structured protocol logs into Azure Log Analytics, enabling advanced querying, correlation, and visualization.
- **Enhanced Accessibility**: Insights are surfaced directly from packet captures, making raw data more actionable and easier to interpret for IT professionals.

**Technical Mechanisms and Implementation Methods**  
Packet Capture Insights operates by applying AI algorithms to analyze captured network traffic. The system processes packet capture files (such as .pcap), identifies patterns and anomalies, and generates structured insights. These insights are then ingested into Azure Log Analytics, where they are stored as protocol logs. This integration allows users to leverage Log Analytics’ powerful query language (KQL) and dashboarding capabilities for further investigation.

The workflow is as follows:
1. Initiate packet capture via Azure Network Watcher.
2. Packet capture files are processed by the AI engine, which extracts key findings.
3. Structured protocol logs are generated and ingested into Azure Log Analytics.
4. Users access and analyze insights through Log Analytics workspaces.

**Use Cases and Application Scenarios**  
- **Network Troubleshooting**: Rapid identification of connectivity issues, protocol errors, or performance bottlenecks without manual packet inspection.
- **Security Analysis**: Detection of suspicious traffic patterns or potential breaches by surfacing anomalies from packet captures.
- **Compliance Auditing**: Structured logs facilitate auditing and reporting for regulatory compliance.
- **Operational Monitoring**: Continuous packet capture analysis for proactive monitoring of network health.

**Important Considerations and Limitations**  
- **Preview Status**: The feature is currently in public preview, meaning it may not be production-ready and could be subject to changes.
- **Data Privacy**: Packet captures may contain sensitive information; ensure compliance with organizational and regulatory data handling policies.
- **Resource Consumption**: AI processing and log ingestion may incur additional Azure resource costs; monitor usage and optimize as needed.
- **Supported Protocols**: Structured protocol log ingestion may be limited to certain protocols; verify compatibility with your network environment.

**Integration with Related Azure Services**  
Packet Capture Insights is tightly integrated with Azure Network Watcher and Azure Log Analytics. The ingestion of protocol logs into Log Analytics enables seamless use of Azure Monitor, alerting, and dashboarding features. This integration supports cross-service correlation, enabling holistic network and security monitoring across Azure resources.

**Summary Sentence**  
Azure Network Watcher’s Packet Capture Insights, now in public preview, uses AI-assisted analysis to surface key findings from packet captures and ingests structured protocol logs into Log Analytics, enhancing accessibility and enabling deeper network investigations for IT professionals.

---

### 146. Generally Available: Azure Cosmos DB SDK for Rust 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Cosmos DB SDK for Rust ](https://azure.microsoft.com/updates?id=578054)

**Update ID**: 578054
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cosmos DB SDK for Rust is now generally available.

- Key changes or new features  
This release introduces a native Rust client for Azure Cosmos DB for NoSQL. Developers can now perform database operations directly from Rust, benefiting from built-in performance optimizations and robust failure handling. The SDK supports efficient binary serialization, enabling high-performance data access and manipulation. It also integrates seamlessly with Rust’s async ecosystem, allowing for scalable and responsive application development.

- Target audience affected  
Rust developers building cloud-native applications, and IT professionals managing Azure Cosmos DB for NoSQL workloads.

- Important notes if any  
The SDK is production-ready and supports all core database operations. It is recommended for teams looking to leverage Rust’s performance and safety features in Azure Cosmos DB projects. Documentation and samples are available to help accelerate adoption. For more details, visit the official Azure Update [link](https://azure.microsoft.com/updates?id=578054).

**Details**:

**Comprehensive Technical Explanation: Azure Cosmos DB SDK for Rust (Generally Available)**

**Background and Purpose of the Update**  
Azure Cosmos DB is a globally distributed, multi-model database service designed for high performance and scalability. Traditionally, Cosmos DB has offered SDKs for languages such as .NET, Java, Python, and Node.js. The release of the Azure Cosmos DB SDK for Rust addresses the growing demand from developers who prefer Rust for its performance, safety, and concurrency features. The purpose of this update is to provide a native Rust client, enabling Rust applications to interact directly with Azure Cosmos DB for NoSQL workloads, thereby expanding the ecosystem and supporting modern, high-performance application development.

**Specific Features and Detailed Changes**  
The Azure Cosmos DB SDK for Rust introduces the following features:

- **Native Rust Client:** Direct access to Cosmos DB operations from Rust code, eliminating the need for intermediary layers or language bindings.
- **Built-in Performance Optimizations:** The SDK leverages Rust’s efficient memory management and concurrency primitives to optimize database interactions.
- **Failure Handling:** Robust error handling mechanisms are integrated, allowing developers to gracefully manage transient faults and connectivity issues.
- **Efficient Binary Serialization:** The SDK supports efficient serialization and deserialization of data, reducing overhead and improving throughput when communicating with Cosmos DB.

This release marks the SDK as generally available, indicating production readiness and support for enterprise workloads.

**Technical Mechanisms and Implementation Methods**  
The SDK is implemented as a native Rust library, exposing idiomatic Rust APIs for Cosmos DB operations such as CRUD (Create, Read, Update, Delete), query execution, and transaction management. It utilizes Rust’s asynchronous programming model (async/await) to support non-blocking I/O, enabling scalable and performant application architectures. The SDK handles authentication, request signing, and response parsing internally, abstracting these complexities from the developer. Built-in retry logic and error handling ensure resilience against transient failures and network issues.

**Use Cases and Application Scenarios**  
- **High-Performance Microservices:** Rust-based microservices can leverage Cosmos DB for low-latency, scalable data storage and retrieval.
- **IoT and Edge Computing:** Applications requiring efficient resource usage and concurrency, such as IoT gateways or edge processors, benefit from the SDK’s performance optimizations.
- **Data-Intensive Applications:** Real-time analytics, event processing, and other data-intensive workloads can utilize the SDK for direct, efficient access to Cosmos DB.
- **Cloud-Native Rust Applications:** Developers building cloud-native solutions in Rust can now integrate Cosmos DB as a managed NoSQL backend.

**Important Considerations and Limitations**  
- **NoSQL Only:** The SDK is specifically for Azure Cosmos DB for NoSQL. It does not support other Cosmos DB APIs (e.g., MongoDB, Cassandra, Gremlin, Table).
- **Production Readiness:** As the SDK is generally available, it is suitable for production use. However, developers should review documentation for supported features and any limitations.
- **Compatibility:** Ensure that the SDK version aligns with your Rust toolchain and Azure Cosmos DB account configuration.

**Integration with Related Azure Services**  
The SDK can be used in conjunction with other Azure services such as Azure Functions (for serverless Rust applications), Azure Kubernetes Service (AKS) for containerized workloads, and Azure DevOps for CI/CD automation. It enables seamless integration of Cosmos DB into Rust-based cloud architectures, supporting authentication via Azure Active Directory and leveraging Azure’s global distribution and scalability features.

**Summary Sentence:**  
The Azure Cosmos DB SDK for Rust is now generally available, providing a native, performant, and resilient client for Rust applications to interact directly with Azure Cosmos DB for NoSQL, supporting efficient database operations and robust failure handling in production environments.

---

### 147. Public Preview: Embedding generation in Azure Cosmos DB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Embedding generation in Azure Cosmos DB ](https://azure.microsoft.com/updates?id=578049)

**Update ID**: 578049
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cosmos DB now offers embedding generation in public preview, enabling automatic conversion of content into vector embeddings.

- Key changes or new features  
This feature uses specialized Azure Data-developed models to generate vector embeddings from data stored in Cosmos DB. Embeddings capture semantic meaning, allowing applications to perform advanced semantic search and retrieval beyond traditional keyword-based methods. Developers can now leverage these embeddings directly within Cosmos DB, streamlining workflows for building AI-powered search and recommendation systems.

- Target audience affected  
Developers building applications with semantic search, recommendation engines, or generative AI capabilities; IT professionals managing data platforms and looking to integrate vector search into their solutions.

- Important notes  
Embedding generation is currently in public preview and may be subject to changes before general availability. Integration with Cosmos DB simplifies the process of enabling semantic search, reducing the need for external embedding generation pipelines. Developers should review documentation for supported data types and model limitations. This feature is designed to enhance AI-driven workloads and improve information retrieval accuracy in Cosmos DB-based applications.

**Details**:

**Azure Update Report: Public Preview – Embedding Generation in Azure Cosmos DB**

**Background and Purpose of the Update**  
The introduction of embedding generation in Azure Cosmos DB addresses the growing need for semantic search capabilities within cloud-native applications. Traditional keyword-based search methods are limited in their ability to retrieve contextually relevant information, especially as data volumes and complexity increase. Embedding generation transforms content into vector representations, enabling applications to perform searches based on semantic similarity rather than exact keyword matches. This update aims to empower developers and IT professionals to build more intelligent, context-aware search and retrieval solutions directly within Cosmos DB.

**Specific Features and Detailed Changes**  
The public preview of embedding generation in Azure Cosmos DB introduces the ability to convert stored content into vector embeddings. These embeddings are numerical representations that capture the semantic meaning of the data. The feature leverages specialized models developed by Azure Data, ensuring that the embeddings are optimized for semantic search and retrieval tasks. With this capability, Cosmos DB can now support advanced search scenarios, such as finding documents or records that are contextually similar, even if they do not share exact keywords.

**Technical Mechanisms and Implementation Methods**  
Embedding generation is implemented using Azure Data-developed models, which are likely based on state-of-the-art machine learning techniques for natural language processing. When content is ingested or queried in Cosmos DB, these models generate vector embeddings that represent the semantic content of the data. The embeddings can then be indexed and queried using vector search algorithms, allowing for efficient retrieval of semantically relevant information. This process abstracts the complexity of embedding generation and vector management, providing a seamless experience for developers working with Cosmos DB.

**Use Cases and Application Scenarios**  
- **Semantic Search:** Applications can retrieve documents or records based on semantic similarity, improving search relevance in scenarios such as customer support, knowledge management, and content recommendation.
- **Contextual Retrieval:** Embedding generation enables retrieval of information that matches the intent or context of a query, rather than relying solely on keyword matches.
- **AI-Driven Applications:** Integrating embedding generation supports AI-powered features such as chatbots, virtual assistants, and recommendation engines, which require understanding of user intent and context.

**Important Considerations and Limitations**  
- **Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes or limitations in functionality.
- **Model Specificity:** Embedding generation relies on Azure Data-developed models. Users should verify the suitability of these models for their specific data types and use cases.
- **Performance and Cost:** Embedding generation and vector search may introduce additional computational overhead and storage requirements. IT professionals should assess performance impacts and potential cost implications.

**Integration with Related Azure Services**  
Embedding generation in Cosmos DB can be integrated with other Azure services to build end-to-end semantic search solutions. For example, it can complement Azure Cognitive Search for advanced indexing and querying, or be used alongside Azure Machine Learning for custom model development and deployment. The feature also aligns with Azure’s broader AI and data platform capabilities, enabling seamless interoperability across services.

**Summary Sentence**  
Azure Cosmos DB now offers public preview support for embedding generation, enabling semantic search and retrieval by converting content into vector embeddings using specialized Azure Data-developed models.

---

### 148. Generally Available: Azure Backup for Azure Cosmos DB 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Backup for Azure Cosmos DB ](https://azure.microsoft.com/updates?id=578044)

**Update ID**: 578044
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Backup for Azure Cosmos DB is now generally available.

- Key changes or new features  
Vaulted backups are introduced, enabling immutable backup copies to be stored in an Azure Backup vault. These backups are isolated from the source Cosmos DB account and managed via Azure Backup, providing an independent protection layer. This feature supports regulatory compliance by ensuring backup data is protected from accidental or malicious deletion and offers enhanced data recovery options.

- Target audience affected  
Developers and IT professionals responsible for managing Azure Cosmos DB workloads, especially those with regulatory or compliance requirements for data protection and backup.

- Important notes if any  
Vaulted backups are managed separately from native Cosmos DB backups, offering greater security and isolation. Integration with Azure Backup allows centralized management and monitoring of backup policies. This update is critical for organizations needing robust backup strategies and compliance with data retention regulations.

For more information, see the official Azure Update: [Azure Backup for Azure Cosmos DB](https://azure.microsoft.com/updates?id=578044).

**Details**:

**Azure Update Technical Explanation: Generally Available: Azure Backup for Azure Cosmos DB**

**Background and Purpose of the Update**  
This update introduces the general availability of Azure Backup for Azure Cosmos DB, enabling organizations to enhance their data protection strategies. The primary purpose is to provide an independent, robust backup solution that meets regulatory and compliance requirements by offering an additional layer of data protection beyond native Cosmos DB backups.

**Specific Features and Detailed Changes**  
- **Vaulted Backups:** Azure Backup now supports storing backup copies of Azure Cosmos DB data in an Azure Backup vault. These backups are immutable, ensuring that once data is written, it cannot be altered or deleted until the retention period expires.
- **Isolation:** The backup copies are stored separately from the source Cosmos DB account, providing isolation to protect against accidental or malicious data loss.
- **Centralized Management:** Backups are managed through Azure Backup, allowing for consistent backup policies, monitoring, and lifecycle management across multiple Cosmos DB accounts.

**Technical Mechanisms and Implementation Methods**  
- **Backup Vault Integration:** When a backup is triggered, a snapshot of the Cosmos DB data is securely transferred and stored in an Azure Backup vault. The vault enforces immutability and retention settings as configured by the administrator.
- **Immutable Storage:** The backup data is protected against modification and deletion, leveraging Azure Backup’s built-in immutability features.
- **Separation of Duties:** By storing backups in a vault separate from the Cosmos DB account, the solution mitigates risks associated with compromised credentials or insider threats at the Cosmos DB account level.

**Use Cases and Application Scenarios**  
- **Regulatory Compliance:** Organizations subject to strict data retention and protection regulations can use vaulted backups to meet requirements for data immutability and offsite storage.
- **Disaster Recovery:** In the event of accidental deletion, corruption, or ransomware attacks on the primary Cosmos DB account, organizations can restore data from the isolated, immutable backup copies.
- **Long-term Retention:** Enterprises needing to retain data for extended periods can leverage backup vault retention policies to manage data lifecycle efficiently.

**Important Considerations and Limitations**  
- **Backup Isolation:** While backups are isolated from the source account, administrators must ensure proper configuration of access controls and retention policies within the Azure Backup vault.
- **Management Overhead:** Centralized management via Azure Backup introduces additional operational steps, such as configuring vaults, setting retention policies, and monitoring backup jobs.
- **Scope of Protection:** The update specifically addresses backup and recovery for Azure Cosmos DB data. Other aspects, such as application-level consistency or cross-region replication, are not covered in this update.

**Integration with Related Azure Services**  
- **Azure Backup Vault:** The solution leverages Azure Backup vaults for storage, immutability, and lifecycle management.
- **Azure Cosmos DB:** Backup operations are initiated for Cosmos DB accounts, with data securely transferred to the vault.
- **Azure Policy and Monitoring:** Organizations can use Azure Policy to enforce backup configurations and Azure Monitor for tracking backup job status and alerts.

**Summary Sentence**  
Azure Backup for Azure Cosmos DB is now generally available, providing immutable, vaulted backups managed through Azure Backup, enabling enhanced data protection and regulatory compliance by isolating backup copies from the source Cosmos DB account.

---

### 149. Generally Available: Zone-redundant Next-gen GP tier in Azure SQL Managed Instance 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Zone-redundant Next-gen GP tier in Azure SQL Managed Instance ](https://azure.microsoft.com/updates?id=578033)

**Update ID**: 578033
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure SQL Managed Instance, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Zone redundancy is now generally available for the Next-gen General Purpose (GP) service tier in Azure SQL Managed Instance.

- Key changes or new features  
Critical service components of Azure SQL Managed Instance can now be distributed across multiple availability zones in the Next-gen GP tier. This enhances resiliency and protects applications from zonal failures, ensuring higher availability and business continuity. The update leverages Azure’s availability zones to minimize downtime and data loss in the event of a zone outage.

- Target audience affected  
Developers and IT professionals managing Azure SQL Managed Instance deployments, especially those requiring high availability and disaster recovery for mission-critical workloads.

- Important notes  
To use zone redundancy, you must deploy your Next-gen GP tier instance in regions that support availability zones. Existing instances may require migration or redeployment to take advantage of this feature. This update is particularly relevant for organizations with strict uptime requirements and those seeking to improve their disaster recovery strategies. For more details and region availability, refer to the official Azure documentation.

**Details**:

**Comprehensive Technical Explanation: Azure Update – Zone-redundant Next-gen GP tier in Azure SQL Managed Instance**

**Background and Purpose of the Update**  
This update introduces zone redundancy to the Next-gen General Purpose (GP) service tier in Azure SQL Managed Instance. The primary objective is to enhance the resiliency of managed SQL workloads by distributing critical service components across multiple Azure availability zones. This approach is designed to protect applications from zonal failures, which are disruptions affecting a single availability zone within an Azure region.

**Specific Features and Detailed Changes**  
The update makes the Next-gen GP tier zone-redundant, meaning that key infrastructure elements—such as compute, storage, and networking components—are deployed across separate availability zones. This distribution ensures that if one zone experiences an outage, the managed instance remains operational by leveraging resources in other zones. The change is now generally available, allowing customers to configure new or existing Next-gen GP tier instances with zone redundancy.

**Technical Mechanisms and Implementation Methods**  
Zone redundancy is achieved by architecting the managed instance to span multiple availability zones within a region. Azure orchestrates the placement of service components so that failure in one zone does not compromise the entire managed instance. This involves synchronizing data and maintaining high availability at the platform level, without requiring manual intervention from the customer. The underlying mechanisms leverage Azure’s regional infrastructure, including cross-zone networking and resilient storage, to maintain consistency and availability.

**Use Cases and Application Scenarios**  
Zone-redundant Next-gen GP tier is ideal for mission-critical applications requiring high availability and business continuity. Typical scenarios include:  
- Enterprise workloads where downtime can have significant business impact  
- Applications with stringent SLAs for uptime and data integrity  
- Multi-region disaster recovery strategies that require additional intra-region resilience  
- SaaS platforms that must protect against localized infrastructure failures

**Important Considerations and Limitations**  
When utilizing zone redundancy, customers should consider:  
- The feature is specific to the Next-gen GP tier; other tiers may not offer zone redundancy  
- Deployments must be within regions that support availability zones  
- There may be implications for latency and throughput due to cross-zone communication  
- Pricing may differ for zone-redundant configurations, so cost analysis is recommended  
- Existing instances may require migration or reconfiguration to leverage zone redundancy

**Integration with Related Azure Services**  
Zone-redundant Azure SQL Managed Instance integrates seamlessly with other Azure services supporting availability zones, such as Azure Virtual Network, Azure Backup, and Azure Monitor. This enables comprehensive high availability and disaster recovery architectures. Customers can use Azure Resource Manager templates and automation tools to provision zone-redundant instances as part of larger, resilient cloud solutions.

**Summary Sentence**  
Zone redundancy in the Next-gen General Purpose tier for Azure SQL Managed Instance is now generally available, providing enhanced resiliency by distributing critical service components across availability zones to protect applications against zonal failures.

---

### 150. Generally Available: Azure SQL Managed Instance link support for availability groups with multiple databases 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure SQL Managed Instance link support for availability groups with multiple databases ](https://azure.microsoft.com/updates?id=578028)

**Update ID**: 578028
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure SQL Managed Instance, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure SQL Managed Instance link now supports Always On Availability Groups with multiple databases.

- Key changes or new features  
You can use a single Managed Instance link to extend a SQL Server Always On Availability Group containing multiple databases to Azure SQL Managed Instance. This applies to both extending existing availability groups and creating new ones with multiple databases. Previously, support was limited to single-database groups, so this update simplifies migration and disaster recovery scenarios for multi-database workloads.

- Target audience affected  
SQL Server database administrators, IT professionals managing high availability and disaster recovery, and developers working with SQL Server and Azure SQL Managed Instance.

- Important notes  
This feature enables easier migration and hybrid cloud setups for applications requiring multiple databases in an availability group. It streamlines management and reduces complexity for organizations moving multi-database workloads to Azure. Ensure your SQL Server version and Azure SQL Managed Instance are compatible with this feature. Review documentation for configuration steps and prerequisites.

**Details**:

**Azure Update Report: Azure SQL Managed Instance link support for availability groups with multiple databases (Generally Available)**

**Background and Purpose of the Update:**  
Traditionally, extending SQL Server Always On Availability Groups (AGs) from on-premises environments to Azure SQL Managed Instance required separate links for each database, complicating management and increasing operational overhead. The purpose of this update is to streamline the process by enabling support for availability groups containing multiple databases through a single Azure SQL Managed Instance link. This enhancement simplifies hybrid cloud architectures and improves manageability for enterprises leveraging SQL Server high availability features.

**Specific Features and Detailed Changes:**  
- **Single Link for Multiple Databases:** The update allows IT professionals to use one Azure SQL Managed Instance link to extend an entire availability group with multiple databases, rather than configuring individual links per database.
- **Support for Existing and New Availability Groups:** Users can either extend an existing availability group with multiple databases or create a new one, both scenarios now supported by the Managed Instance link.
- **General Availability:** The feature is now generally available, meaning it is production-ready and supported for enterprise workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Azure SQL Managed Instance Link:** This feature leverages the Managed Instance link technology, which facilitates near real-time data replication from SQL Server Always On AGs to Azure SQL Managed Instance.
- **Availability Group Integration:** The link operates at the availability group level, enabling replication and failover for all databases within the group in a unified manner.
- **Configuration Workflow:** Administrators can configure the link by specifying the availability group and Managed Instance as endpoints. The process involves setting up the AG on SQL Server, ensuring network connectivity, and establishing the link through Azure portal or PowerShell.

**Use Cases and Application Scenarios:**  
- **Hybrid Disaster Recovery:** Enterprises can extend their on-premises SQL Server AGs to Azure SQL Managed Instance for disaster recovery, protecting multiple databases with a single configuration.
- **Cloud Migration:** Organizations migrating multiple databases from on-premises SQL Server to Azure can use this feature to simplify and accelerate the migration process.
- **High Availability Across Hybrid Environments:** Businesses requiring high availability for multiple databases across on-premises and Azure environments can leverage this update for unified management and failover.

**Important Considerations and Limitations:**  
- **Supported Database Types:** Only databases included in an Always On Availability Group are supported; ensure all required databases are part of the AG.
- **Network and Security Requirements:** Proper network connectivity and security configurations between on-premises SQL Server and Azure SQL Managed Instance are essential for successful link operation.
- **Operational Impact:** While the feature reduces management complexity, administrators must monitor replication health and failover readiness for all databases in the group.
- **Azure SQL Managed Instance Limitations:** Review Managed Instance documentation for any constraints related to database size, features, or AG compatibility.

**Integration with Related Azure Services:**  
- **Azure Portal and PowerShell:** Configuration and management of the Managed Instance link can be performed via Azure Portal or PowerShell, integrating with existing Azure management workflows.
- **Azure Monitoring and Security:** The link can be monitored using Azure Monitor, and security can be enforced with Azure networking and identity services.

**Summary Sentence:**  
Azure SQL Managed Instance link now supports extending SQL Server Always On Availability Groups with multiple databases to Azure SQL Managed Instance using a single link, simplifying hybrid high availability and disaster recovery configurations for enterprise workloads.

---

### 151. Public Preview: Shard-level metrics in Azure Managed Redis 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Shard-level metrics in Azure Managed Redis ](https://azure.microsoft.com/updates?id=577599)

**Update ID**: 577599
**Data source**: Azure Updates API

**Categories**: In preview, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Managed Redis now supports shard-level metrics in public preview.

- Key changes or new features  
Shard-level metrics provide detailed visibility into the performance of individual Redis shards. This enables monitoring of workload distribution, identification of hotspots, and improved troubleshooting of performance issues. Developers and IT professionals can now analyze metrics such as memory usage, CPU utilization, and command processing at the shard level, rather than only at the instance level.

- Target audience affected  
This update is relevant for developers and IT professionals managing Azure Managed Redis instances, especially those using Redis in clustered configurations or with large-scale, distributed workloads.

- Important notes  
Shard-level metrics are currently available in public preview and may be subject to changes before general availability. Users should review documentation for integration details and monitor for updates regarding production readiness. This feature enhances observability and can help optimize Redis cluster performance and resource allocation.

For more information, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=577599).

**Details**:

**Azure Update Report: Public Preview – Shard-level Metrics in Azure Managed Redis**

**Background and Purpose of the Update**  
Azure Managed Redis is a cloud-based, fully managed Redis service that supports scalable, high-performance caching and data storage. In distributed Redis deployments, data is partitioned across multiple shards to optimize performance and scalability. Traditionally, monitoring was limited to cluster-level metrics, providing only aggregate insights. The purpose of this update is to introduce shard-level metrics, allowing IT professionals to gain granular visibility into the performance of each individual shard within their Redis cluster. This enhancement addresses the need for more detailed monitoring, enabling better workload analysis and troubleshooting.

**Specific Features and Detailed Changes**  
With this update, Azure Managed Redis exposes metrics at the shard level. These metrics include performance indicators such as throughput, latency, memory usage, and connection statistics for each shard. The granularity allows users to observe how data and requests are distributed across shards, identify uneven load distribution, and pinpoint shards experiencing performance issues or resource contention. The update does not change the core functionality of Redis but augments the monitoring capabilities available to users.

**Technical Mechanisms and Implementation Methods**  
Shard-level metrics are collected and surfaced via Azure’s monitoring infrastructure. These metrics are accessible through Azure Monitor, which supports integration with dashboards, alerts, and automated responses. The metrics are gathered from the Redis engine at the shard level and made available through standard Azure interfaces, such as the Azure Portal, REST APIs, and CLI tools. This enables IT professionals to programmatically retrieve, analyze, and visualize shard-specific performance data alongside other Azure resources.

**Use Cases and Application Scenarios**  
- **Workload Distribution Analysis:** Engineers can assess how requests and data are partitioned across shards, helping optimize sharding strategies and balance workloads.
- **Hotspot Identification:** Shard-level metrics make it possible to detect shards that are overloaded or experiencing latency, facilitating targeted troubleshooting and remediation.
- **Performance Optimization:** By monitoring individual shards, teams can tune Redis configurations, scale resources, or adjust partitioning to improve overall cluster performance.
- **Capacity Planning:** Detailed metrics support more accurate forecasting of resource needs and scaling decisions based on shard utilization patterns.

**Important Considerations and Limitations**  
This feature is currently in Public Preview, which means it may not be suitable for production workloads requiring guaranteed stability or support. Users should validate the behavior and reliability of shard-level metrics in their environments before relying on them for critical monitoring or automation. Additionally, the update does not provide new management or configuration capabilities; it strictly enhances observability. The scope of available metrics is limited to shard-level performance indicators as described, and users should consult official documentation for supported metric types and data retention policies.

**Integration with Related Azure Services**  
Shard-level metrics are integrated with Azure Monitor, enabling seamless use with Log Analytics, Application Insights, and Azure dashboards. This allows users to combine Redis shard metrics with other Azure resource metrics for holistic monitoring and alerting. The update supports standard Azure monitoring workflows, including custom alert rules and automated actions based on metric thresholds.

**Summary Sentence**  
Azure Managed Redis now offers shard-level metrics in Public Preview, providing enhanced visibility into individual shard performance to support workload analysis, hotspot detection, and targeted troubleshooting through Azure Monitor integration.

---

### 152. Public Preview: Redis 8 in Azure Managed Redis 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Redis 8 in Azure Managed Redis ](https://azure.microsoft.com/updates?id=577594)

**Update ID**: 577594
**Data source**: Azure Updates API

**Categories**: In preview, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
Azure Managed Redis now supports Redis 8 in public preview.

**Key changes or new features:**  
- **Richer queries:** Enhanced query capabilities allow developers to retrieve and manipulate data more efficiently.
- **Atomic JSON updates:** Redis 8 introduces atomic operations for JSON data, simplifying complex data handling and ensuring consistency.
- **Field-level expiration:** Developers can now set expiration times at the individual field level within Redis objects, improving cache management and data lifecycle control.
- **Fine-grained security:** Improved security features enable more granular access control, supporting enterprise compliance and data protection requirements.

**Target audience affected:**  
- Developers building applications on Azure that use Redis for caching, session management, or real-time data processing.
- IT professionals managing Azure infrastructure and seeking advanced Redis features for performance, security, and scalability.

**Important notes:**  
- Redis 8 is currently available in public preview; production workloads should be carefully evaluated before migration.
- Existing Azure Managed Redis instances will need to be upgraded to leverage Redis 8 features.
- Review documentation for compatibility and migration guidance to ensure smooth adoption.

For more details, visit the [Azure Update](https://azure.microsoft.com/updates?id=577594).

**Details**:

**Azure Update Explanation: Public Preview – Redis 8 in Azure Managed Redis**

**Background and Purpose of the Update**  
Azure Managed Redis is a fully managed, scalable, and secure Redis service on Azure. The introduction of Redis 8 in public preview aims to deliver the latest Redis innovations to Azure customers, enabling them to leverage advanced data structures and operational enhancements without managing infrastructure or updates themselves. This update is designed to simplify development and enhance performance, security, and flexibility for applications relying on Redis as a caching or data store solution.

**Specific Features and Detailed Changes**  
Redis 8 introduces several key features in Azure Managed Redis:

- **Richer Queries:** Enhanced query capabilities allow for more complex and efficient data retrieval, supporting advanced application requirements.
- **Atomic JSON Updates:** Developers can now perform atomic operations on JSON documents, ensuring data consistency and simplifying manipulation of structured data within Redis.
- **Field-Level Expiration:** This feature enables expiration policies to be set at the individual field level within data structures, offering more granular control over data lifecycle management.
- **Fine-Grained Security:** Improved security controls allow for more detailed access management, helping organizations meet compliance and security requirements.

**Technical Mechanisms and Implementation Methods**  
Azure Managed Redis abstracts the operational complexity of deploying and maintaining Redis clusters. With Redis 8, these new features are integrated into the managed service, allowing users to access them via standard Redis clients and commands. Atomic JSON updates are likely supported through the RedisJSON module, while field-level expiration and richer queries are handled natively by the Redis 8 engine. Fine-grained security is managed through Azure’s identity and access management frameworks, integrated with Redis’s own authentication and authorization mechanisms.

**Use Cases and Application Scenarios**  
- **Real-Time Analytics:** The richer query capabilities and atomic JSON updates enable efficient handling of complex, real-time analytical workloads.
- **Session Management:** Field-level expiration allows for precise control over session data, automatically expiring individual fields as needed.
- **Secure Multi-Tenant Applications:** Fine-grained security features support scenarios where multiple tenants or users require isolated and controlled access to Redis data.
- **Caching Layer for Web Applications:** The new features enhance the flexibility and reliability of Redis as a high-performance cache.

**Important Considerations and Limitations**  
- **Public Preview Status:** As Redis 8 is in public preview, it may not be recommended for production workloads. Users should evaluate stability and feature completeness before full adoption.
- **Feature Availability:** Some advanced features may require specific client versions or additional configuration within Azure Managed Redis.
- **Compatibility:** Existing applications may need to be tested for compatibility with Redis 8, especially if they rely on deprecated commands or behaviors.

**Integration with Related Azure Services**  
Azure Managed Redis with Redis 8 continues to integrate seamlessly with other Azure services such as Azure Virtual Network (for secure connectivity), Azure Monitor (for observability and logging), and Azure Active Directory (for identity management). These integrations ensure that Redis 8 can be used as part of larger, secure, and scalable Azure-based architectures.

**Summary Sentence**  
Redis 8 is now available in Azure Managed Redis (public preview), offering enhanced query capabilities, atomic JSON updates, field-level expiration, and fine-grained security to simplify development and improve data management within Azure’s fully managed Redis service.

---

### 153. Public Preview: IP filtering in Azure Managed Redis 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: IP filtering in Azure Managed Redis ](https://azure.microsoft.com/updates?id=577589)

**Update ID**: 577589
**Data source**: Azure Updates API

**Categories**: In preview, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Managed Redis now supports IP filtering in public preview.

- Key changes or new features  
Firewall rules can be configured to restrict access to Redis caches based on source IP addresses or Azure service tags. This allows administrators to permit only approved IPs or Azure services, enhancing security by limiting exposure to unauthorized connections.

- Target audience affected  
Developers and IT professionals managing Azure Managed Redis instances, especially those requiring tighter network security controls for their cache data.

- Important notes if any  
IP filtering is available in public preview, so it may not be suitable for production workloads yet. This feature is particularly important for organizations with compliance or security requirements, as it helps protect publicly accessible Redis caches from unwanted access. Review documentation for configuration details and limitations during the preview phase.

**Details**:

**Azure Update Report: Public Preview – IP Filtering in Azure Managed Redis**

**Background and Purpose of the Update**  
Azure Managed Redis is a fully managed, scalable Redis cache service used to accelerate data access and improve application performance. Traditionally, network access control for Azure Managed Redis was limited, exposing caches to broader connectivity. The purpose of this update is to enhance security by allowing administrators to define explicit firewall rules, thereby restricting access to Redis caches and mitigating risks associated with unauthorized connections.

**Specific Features and Detailed Changes**  
With this update, Azure Managed Redis introduces support for IP filtering through firewall rules. Administrators can now specify approved source IP addresses or Azure service tags that are permitted to connect to their Redis cache instances. This feature enables granular control over inbound connections, ensuring only trusted sources can access the data stored in the cache. The update provides a user interface and API support to configure these rules, allowing for both manual and automated management.

**Technical Mechanisms and Implementation Methods**  
The IP filtering mechanism operates at the network layer, intercepting connection requests to the Redis cache and evaluating them against the configured firewall rules. If a connection originates from an approved IP address or matches an Azure service tag, access is granted; otherwise, the connection is denied. Azure service tags represent groups of IP addresses associated with specific Azure services, simplifying rule management for scenarios where services need to communicate securely. The implementation leverages Azure’s underlying network security infrastructure, ensuring seamless integration with existing Azure networking policies.

**Use Cases and Application Scenarios**  
- **Securing Publicly Accessible Redis Caches:** Organizations can restrict access to Redis caches that are exposed to the internet, allowing only specific IP addresses or Azure services to connect.
- **Compliance and Regulatory Requirements:** Enterprises subject to regulatory controls can enforce network access policies to meet compliance standards.
- **Multi-tier Application Architectures:** Developers can ensure that only application tiers or services with approved IPs can access Redis, preventing lateral movement in case of a breach.
- **DevOps and Automation:** Automated deployment scripts can configure IP filtering rules as part of infrastructure provisioning, ensuring consistent security posture across environments.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes.
- **Rule Management:** Administrators must carefully manage and update firewall rules to avoid inadvertently blocking legitimate access or exposing caches to unauthorized sources.
- **Service Tag Limitations:** The use of Azure service tags simplifies rule configuration but may not cover all scenarios, especially for custom or third-party services.
- **Interoperability:** Existing network security groups (NSGs) and other Azure networking features should be reviewed to ensure compatibility and avoid conflicts.

**Integration with Related Azure Services**  
IP filtering in Azure Managed Redis integrates with Azure networking features such as NSGs, Virtual Networks, and service tags. This allows organizations to align Redis cache access policies with broader network security strategies and leverage Azure’s identity and access management capabilities for comprehensive protection.

**Summary Sentence**  
Azure Managed Redis now supports IP filtering in public preview, enabling administrators to define firewall rules for cache access and providing enhanced network security by restricting connections to approved IP addresses or Azure service tags.

---

### 154. Generally Available: Azure Cache for Redis to Azure Managed Redis migration tooling 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Cache for Redis to Azure Managed Redis migration tooling ](https://azure.microsoft.com/updates?id=577579)

**Update ID**: 577579
**Data source**: Azure Updates API

**Categories**: Launched, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cache for Redis now offers generally available migration tooling to facilitate DNS endpoint migration to Azure Managed Redis.

- Key changes or new features  
The new built-in migration tooling allows seamless redirection of cache endpoints from Azure Cache for Redis (Basic, Standard, and Premium tiers) to Azure Managed Redis. This tool automates DNS hostname migration, enabling existing applications to connect to Azure Managed Redis without manual endpoint updates or downtime. The migration process is streamlined, reducing operational complexity and risk.

- Target audience affected  
Developers and IT professionals managing Azure Cache for Redis instances, especially those planning to upgrade or migrate to Azure Managed Redis.

- Important notes if any  
This tooling supports migrations for Basic, Standard, and Premium tiers only. It is recommended to review application compatibility and test the migration process in a staging environment before production use. The migration tooling is designed to minimize disruption, but thorough validation is advised to ensure seamless transition. More details and guidance are available in the official Azure documentation.

**Details**:

**Azure Update Report: Generally Available – Azure Cache for Redis to Azure Managed Redis Migration Tooling**

**Background and Purpose of the Update**  
This update announces the general availability of built-in DNS migration tooling for Azure Cache for Redis. The primary goal is to streamline and simplify the migration process for customers moving from Azure Cache for Redis (across Basic, Standard, and Premium tiers) to Azure Managed Redis. The update addresses the operational complexity and potential downtime associated with endpoint changes during migration, enabling a smoother transition to the managed service.

**Specific Features and Detailed Changes**  
The newly available migration tooling introduces built-in DNS redirection capabilities. Specifically, it allows users to redirect the existing cache hostname from their current Azure Cache for Redis instance to an Azure Managed Redis instance. This eliminates the need to manually update application connection strings or endpoints, reducing the risk of configuration errors and service interruptions.

Key features include:
- Seamless DNS-level redirection from legacy cache endpoints to the new Azure Managed Redis instance.
- Support for migrations from Basic, Standard, and Premium tiers of Azure Cache for Redis.
- Integration into the Azure platform, providing a guided migration experience.

**Technical Mechanisms and Implementation Methods**  
The migration tooling operates at the DNS level. When invoked, it updates the DNS records associated with the original Azure Cache for Redis instance, so that requests to the old cache hostname are transparently routed to the new Azure Managed Redis instance. This approach abstracts the migration process from application code, as applications continue to use the same cache endpoint.

The implementation likely involves:
- Validation of source and target cache instances.
- Automated DNS record updates within Azure’s internal DNS infrastructure.
- Monitoring and verification steps to ensure successful redirection.

**Use Cases and Application Scenarios**  
This tooling is particularly beneficial in scenarios where:
- Enterprises need to upgrade from legacy Azure Cache for Redis to the fully managed Azure Managed Redis service, leveraging enhanced features or compliance.
- Large-scale applications require zero-downtime or minimal-disruption cache migration.
- Organizations want to avoid the operational overhead of updating application configurations across multiple environments.

**Important Considerations and Limitations**  
- The migration tooling is available for migrations from Basic, Standard, and Premium tiers only.
- The update focuses on DNS endpoint redirection; data migration or synchronization between caches is not explicitly addressed in this announcement.
- Users should ensure that the target Azure Managed Redis instance is fully configured and tested before initiating DNS redirection.
- Any application-level dependencies on cache-specific features or configurations should be validated for compatibility with Azure Managed Redis.

**Integration with Related Azure Services**  
This migration tooling integrates directly with Azure Cache for Redis and Azure Managed Redis services. It leverages Azure’s DNS management capabilities to facilitate endpoint redirection. The tooling can be incorporated into broader migration workflows, potentially alongside Azure Resource Manager (ARM) templates, Azure Automation, or DevOps pipelines for orchestrated deployments.

**Summary Sentence**  
The general availability of built-in DNS migration tooling for Azure Cache for Redis enables seamless endpoint redirection to Azure Managed Redis, simplifying migrations and minimizing application changes for IT professionals.

---

### 155. Public Preview: Azure Managed Redis agent kit

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Managed Redis agent kit](https://azure.microsoft.com/updates?id=577568)

**Update ID**: 577568
**Data source**: Azure Updates API

**Categories**: In preview, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure has released the Azure Managed Redis agent kit in public preview, integrating Redis development guidance directly into AI-assisted development workflows.

- Key changes or new features  
The agent kit provides actionable recommendations for building and operating production-ready Redis applications. It covers best practices for caching, messaging, search, AI integration patterns, and client configuration. Developers can access this guidance within their development environments, streamlining the process of implementing Redis features and optimizing application performance.

- Target audience affected  
This update is aimed at developers and IT professionals working with Azure Managed Redis, especially those building applications that require high-performance caching, messaging, or AI-driven workflows.

- Important notes  
The agent kit is currently in public preview, meaning features and guidance may evolve based on user feedback. Integration with AI-assisted development tools enables faster adoption of Redis best practices and reduces manual research. Users should monitor Azure documentation for updates as the kit matures.

**Details**:

**Azure Update Report: Public Preview – Azure Managed Redis Agent Kit**

**Background and Purpose of the Update:**  
The Azure Managed Redis agent kit is introduced to streamline the development and operation of production-ready Redis applications within Azure environments. Its primary purpose is to embed best-practice guidance and operational recommendations directly into AI-assisted development workflows, thereby enhancing developer productivity and application reliability when leveraging Azure Cache for Redis.

**Specific Features and Detailed Changes:**  
This update delivers a toolkit that provides actionable recommendations for several Redis application patterns, including caching, messaging, search, and AI integration. The agent kit is designed to surface guidance contextually as developers build and operate their applications, ensuring that Redis usage aligns with Azure’s recommended practices. The recommendations cover key areas such as client configuration, data modeling, and operational patterns, aiming to reduce common pitfalls and optimize Redis performance and reliability.

**Technical Mechanisms and Implementation Methods:**  
The agent kit integrates with AI-assisted development environments, likely leveraging code analysis and contextual triggers to deliver relevant Redis guidance. As developers write or modify code, the agent kit identifies Redis-related patterns and surfaces tailored recommendations, such as optimal caching strategies, messaging patterns, or search implementations. The kit also provides guidance on AI pattern integration, helping developers utilize Redis as a backend for AI workloads. The technical delivery is embedded within the development workflow, ensuring recommendations are timely and actionable.

**Use Cases and Application Scenarios:**  
- **Caching:** Developers receive best-practice guidance for implementing high-performance, scalable caching layers using Azure Managed Redis.
- **Messaging:** The kit assists in building distributed messaging solutions with Redis Pub/Sub, ensuring reliability and scalability.
- **Search:** Recommendations for implementing search functionalities using Redis data structures are provided.
- **AI Patterns:** Developers integrating Redis with AI workloads (e.g., as a feature store or inference cache) receive targeted guidance to optimize performance and reliability.
- **Client Configuration:** The kit ensures that client libraries and connection settings are configured for optimal use with Azure Managed Redis.

**Important Considerations and Limitations:**  
- The Azure Managed Redis agent kit is currently in public preview, which means it may not have full feature parity with the planned general availability release and may be subject to changes.
- The scope of recommendations and supported development environments may be limited during the preview phase.
- As with all preview features, production use should be approached with caution, and users should monitor for updates or changes in guidance.

**Integration with Related Azure Services:**  
The agent kit is designed to work seamlessly with Azure Managed Redis, ensuring that all recommendations are tailored for the Azure platform. It is intended to integrate into AI-assisted development workflows, which may include tools like Visual Studio Code, GitHub Copilot, or Azure DevOps, though the specific integrations are not detailed in the update. The guidance provided is aligned with Azure’s operational and security best practices, supporting developers in building robust, cloud-native Redis applications.

**Summary Sentence:**  
The Azure Managed Redis agent kit (public preview) delivers in-workflow, AI-assisted guidance for building and operating production-ready Redis applications on Azure, offering actionable recommendations for caching, messaging, search, and AI integration to optimize client configuration and application reliability.

---

### 156. Generally Available: Azure Managed Redis keyspace notifications 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Managed Redis keyspace notifications ](https://azure.microsoft.com/updates?id=577558)

**Update ID**: 577558
**Data source**: Azure Updates API

**Categories**: Launched, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Managed Redis now supports generally available keyspace notifications.

- Key changes or new features  
Keyspace notifications allow applications to receive real-time events via Redis pub/sub when cache data changes (e.g., key creation, expiration, deletion). Developers can configure which event types to monitor and subscribe to relevant notifications. This feature enables more responsive application designs, such as cache invalidation, auditing, or triggering workflows based on cache activity.

- Target audience affected  
Developers building applications with Azure Managed Redis and IT professionals managing Redis-based caching solutions.

- Important notes  
Keyspace notifications must be explicitly enabled and configured for desired event types. This feature improves integration with event-driven architectures and can help optimize cache management and application responsiveness. Review Azure documentation for guidance on configuring and subscribing to notifications.  
[Azure Update Link](https://azure.microsoft.com/updates?id=577558)

**Details**:

**Comprehensive Technical Explanation: Azure Managed Redis Keyspace Notifications (Generally Available)**

**Background and Purpose of the Update**  
Azure Managed Redis is a fully managed caching service based on Redis, widely used to accelerate application performance by providing fast, in-memory data storage. Keyspace notifications are a Redis feature that allows clients to receive real-time events when data in the cache changes. The general availability of keyspace notifications in Azure Managed Redis addresses the need for event-driven architectures, enabling applications to react promptly to changes in cached data without continuous polling.

**Specific Features and Detailed Changes**  
With this update, Azure Managed Redis now supports keyspace notifications, allowing applications to subscribe to specific event types via Redis pub/sub channels. Users can configure which types of events (such as key creation, deletion, expiration, or modification) are relevant to their application. This feature enhances observability and responsiveness by enabling clients to receive notifications when specified cache operations occur.

**Technical Mechanisms and Implementation Methods**  
Keyspace notifications leverage Redis’s native pub/sub mechanism. When enabled, Redis emits events to designated channels whenever configured operations occur on keys. Applications connect to Azure Managed Redis and subscribe to these channels to receive notifications. Configuration is managed through Redis settings, where users specify the event types to monitor. The implementation ensures compatibility with standard Redis clients, allowing seamless integration into existing application architectures.

**Use Cases and Application Scenarios**  
- **Cache Invalidation:** Applications can automatically invalidate or refresh local caches when data changes in Azure Managed Redis, improving consistency and reducing stale data.
- **Real-Time Monitoring:** Operations teams can monitor cache activity, such as key expirations or deletions, for auditing or alerting purposes.
- **Event-Driven Workflows:** Microservices can trigger downstream processing when specific cache events occur, supporting reactive architectures.
- **Session Management:** Applications can respond to session expiration events, enabling custom handling or cleanup.

**Important Considerations and Limitations**  
- **Configuration:** Only the event types configured by the user will be published; careful selection is required to avoid unnecessary event traffic.
- **Performance Impact:** Excessive notifications may impact Redis performance; it is recommended to subscribe only to essential events.
- **Compatibility:** Ensure that client libraries support Redis pub/sub and keyspace notification features.
- **Security:** Event data is transmitted via pub/sub channels; secure client connections and access controls should be enforced.

**Integration with Related Azure Services**  
Keyspace notifications can be integrated with Azure Event Grid, Azure Functions, or Azure Logic Apps to automate workflows based on cache events. For example, an Azure Function can be triggered when a key expires, enabling further processing or notification. This feature also complements Azure Monitor for enhanced observability and alerting on cache operations.

**Summary Sentence**  
Azure Managed Redis keyspace notifications are now generally available, enabling applications to receive real-time cache event updates via pub/sub, with configurable event types for improved responsiveness and integration with event-driven Azure services.

---

### 157. Generally Available: Azure Managed Redis database integration guidance 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Managed Redis database integration guidance ](https://azure.microsoft.com/updates?id=577553)

**Update ID**: 577553
**Data source**: Azure Updates API

**Categories**: Launched, Azure Managed Redis, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Managed Redis database integration guidance is now generally available, offering improved resources for integrating Redis caching with Azure databases.

- Key changes or new features  
The update provides enhanced practical guidance, reference architectures, and step-by-step instructions for adding Redis caching to applications using Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL. This includes best practices for cache implementation, performance optimization, and architectural patterns for common scenarios.

- Target audience affected  
Developers and IT professionals building applications on Azure that require high-performance caching and integration with Azure database services, specifically those using PostgreSQL flexible server, Cosmos DB, or Azure SQL.

- Important notes if any  
The guidance helps streamline the process of implementing Redis as a cache layer, improving application scalability and responsiveness. It also assists in reducing database load and latency. Reference architectures and practical examples are available to accelerate adoption and ensure best practices. For more details and resources, visit the official Azure update page: https://azure.microsoft.com/updates?id=577553

**Details**:

**Azure Update Report: Generally Available – Azure Managed Redis Database Integration Guidance**

**Background and Purpose of the Update:**  
This update introduces improved integration guidance for Azure Managed Redis, specifically targeting scenarios where caching is added to applications utilizing Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL. The purpose is to streamline the process of implementing Redis caching in conjunction with these Azure database services, thereby enhancing application performance, scalability, and reliability.

**Specific Features and Detailed Changes:**  
The update delivers practical guidance, reference architectures, and step-by-step instructions for integrating Azure Managed Redis with the aforementioned database services. These resources are designed to help IT professionals architect solutions that leverage Redis as a distributed cache, reducing database load and improving response times. The guidance covers best practices for cache design, data consistency, and cache invalidation strategies, ensuring robust and maintainable implementations.

**Technical Mechanisms and Implementation Methods:**  
Azure Managed Redis is deployed as a fully managed cache service within Azure, supporting high availability and scalability. The integration guidance details how to configure Redis as a caching layer for applications interfacing with Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL. Implementation methods include configuring connection strings, setting up cache keys, and employing Redis data structures (such as strings, hashes, and sets) to store frequently accessed data. The guidance also addresses how to synchronize cache and database states, and how to handle cache misses and expiration policies.

**Use Cases and Application Scenarios:**  
Typical use cases include web applications, APIs, and microservices that require low-latency access to data stored in Azure databases. For example, an e-commerce platform using Azure SQL can employ Redis to cache product catalog data, reducing database queries and improving user experience. Similarly, applications built on Azure Database for PostgreSQL flexible server or Azure Cosmos DB can use Redis to cache session state, user profiles, or frequently queried records, optimizing performance and scalability.

**Important Considerations and Limitations:**  
IT professionals should consider cache consistency and invalidation strategies to ensure data accuracy between Redis and the underlying database. The guidance emphasizes the importance of handling cache misses, setting appropriate expiration policies, and monitoring cache performance. Limitations may include the need to manage cache size, avoid stale data, and ensure that Redis is provisioned with sufficient resources to handle application load. Security considerations such as access control, encryption, and network isolation are also addressed in the integration guidance.

**Integration with Related Azure Services:**  
Azure Managed Redis integrates seamlessly with Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL. The guidance provides reference architectures illustrating how to connect these services, configure authentication, and monitor cache performance using Azure Monitor. Additionally, integration with Azure networking and security services ensures that Redis deployments are secure and compliant with organizational policies.

**Summary Sentence:**  
Azure Managed Redis database integration guidance is now generally available, offering practical resources and reference architectures to help IT professionals efficiently implement caching for applications built on Azure Database for PostgreSQL flexible server, Azure Cosmos DB, and Azure SQL.

---

### 158. Generally Available: Azure Cosmos DB full-text search BM25 score projection

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Azure Cosmos DB full-text search BM25 score projection](https://azure.microsoft.com/updates?id=577531)

**Update ID**: 577531
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Cosmos DB full-text search now supports BM25 score projection, which is generally available.

- Key changes or new features  
The BM25 score projection feature enables applications to access the relevance score for each search result directly. This provides transparency into search ranking, allowing developers and IT professionals to understand why results are ordered as they are. The BM25 score is a widely used ranking function in information retrieval, improving the accuracy and interpretability of search results within Cosmos DB.

- Target audience affected  
Developers building search functionality in applications using Azure Cosmos DB, and IT professionals managing or optimizing search experiences in Cosmos DB workloads.

- Important notes  
With BM25 score projection, you can now retrieve the relevance score alongside search results via the API, making it easier to debug, tune, and explain search behavior to end users. This feature enhances search result transparency and ranking control, supporting more advanced search scenarios and analytics. No additional configuration is required to access BM25 scores; simply query the API for score projection.

**Details**:

**Azure Update Report: Azure Cosmos DB Full-Text Search BM25 Score Projection (Generally Available)**

**Background and Purpose of the Update**  
Azure Cosmos DB is a globally distributed, multi-model database service that supports full-text search capabilities for querying textual data. Traditionally, search results are ranked based on their relevance, but the underlying scoring and ranking mechanisms have not always been transparent to developers and users. The purpose of this update is to enhance search transparency by exposing the BM25 relevance score directly within search results, allowing applications to understand and utilize the ranking logic more effectively.

**Specific Features and Detailed Changes**  
With this update, Azure Cosmos DB full-text search now supports BM25 score projection. BM25 (Best Matching 25) is a widely used ranking function in information retrieval, designed to estimate the relevance of documents to a given search query. The update introduces the ability for applications to access the BM25 score for each search result directly. This feature provides clear visibility into why results are ordered as they are, enabling developers to retrieve and display the relevance score alongside each result in their application.

**Technical Mechanisms and Implementation Methods**  
The BM25 score projection is implemented as part of the Cosmos DB full-text search API. When a search query is executed, the engine calculates the BM25 score for each matching document. This score is then included in the result set, accessible through the API. Developers can retrieve the score as a field in the search response, allowing for programmatic access and potential custom handling of search rankings. The mechanism leverages BM25’s probabilistic model, which considers term frequency, document length, and other factors to compute relevance.

**Use Cases and Application Scenarios**  
- **Search Result Transparency:** Applications can display the BM25 score to end-users, providing insight into why a particular result appears at a certain position.
- **Custom Ranking and Filtering:** Developers can use the BM25 score to implement custom ranking logic or filter results based on minimum relevance thresholds.
- **Analytics and Monitoring:** The score can be logged and analyzed to monitor search quality and optimize query performance.
- **Personalized Search Experiences:** By exposing the score, developers can combine BM25 relevance with other business logic to deliver tailored search results.

**Important Considerations and Limitations**  
- The BM25 score projection is available only for full-text search queries in Azure Cosmos DB.
- Applications must be updated to retrieve and handle the BM25 score from the search response.
- The score is calculated based on the BM25 algorithm, which may not align with all custom ranking requirements; additional logic may be needed for specialized scenarios.
- Performance impact should be monitored, as projecting additional fields in search results can affect response times and resource utilization.

**Integration with Related Azure Services**  
BM25 score projection in Cosmos DB full-text search can be integrated with other Azure services such as Azure Functions, Azure Logic Apps, and Azure API Management for building end-to-end search solutions. The exposed score can be used in workflows, analytics pipelines, or combined with Azure Cognitive Search for advanced search scenarios.

**Summary Sentence**  
Azure Cosmos DB full-text search now generally supports BM25 score projection, providing direct access to relevance scores for each result and enhancing transparency and control over search ranking in applications.

---

### 159. Public Preview: Azure Database for MySQL on Premium SSD v2 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Azure Database for MySQL on Premium SSD v2 ](https://azure.microsoft.com/updates?id=577515)

**Update ID**: 577515
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure Database for MySQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for MySQL now supports Premium SSD v2 managed disks in public preview.

- Key changes or new features  
Premium SSD v2 offers improved performance and price-performance compared to previous storage options (such as Premium File Share). It allows independent scaling of storage capacity and performance, providing greater flexibility for database workloads. This enables users to optimize storage and throughput based on workload requirements, potentially reducing costs and improving efficiency.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL instances, especially those requiring high-performance storage or looking to optimize cost and scalability for production workloads.

- Important notes  
The feature is currently in public preview, so it may not be available in all regions or for all configurations. Users should validate compatibility and performance for their workloads before adopting in production environments. For more details and regional availability, refer to the official Azure update link: https://azure.microsoft.com/updates?id=577515

**Details**:

**Azure Update Report: Public Preview – Azure Database for MySQL on Premium SSD v2**

**Background and Purpose of the Update**  
Azure Database for MySQL is a managed database service offering high availability, security, and scalability. The introduction of Premium SSD v2 managed disks in public preview aims to enhance storage performance and optimize price-performance ratios for MySQL workloads. This update addresses the growing demand for scalable, high-throughput storage solutions in cloud-based database environments, moving beyond the limitations of Premium File Share.

**Specific Features and Detailed Changes**  
- **Premium SSD v2 Support:** Azure Database for MySQL now supports Premium SSD v2 managed disks, which offer improved IOPS, throughput, and latency compared to previous storage options.
- **Independent Scaling:** Storage capacity can be scaled independently, allowing for flexible resource allocation tailored to workload requirements.
- **Enhanced Price-Performance:** Premium SSD v2 provides better cost efficiency, delivering higher performance at a lower price point relative to Premium File Share.

**Technical Mechanisms and Implementation Methods**  
- **Managed Disk Integration:** Premium SSD v2 is integrated as a managed disk option within Azure Database for MySQL. Managed disks abstract storage management, providing reliability and simplified operations.
- **Storage Scaling:** Administrators can adjust storage capacity without impacting compute resources, enabling granular scaling and minimizing downtime.
- **Performance Optimization:** Premium SSD v2 disks leverage Azure’s next-generation storage architecture, supporting higher IOPS and throughput, which is critical for database workloads with intensive read/write operations.

**Use Cases and Application Scenarios**  
- **High-Performance OLTP Applications:** Applications requiring low latency and high transaction rates benefit from the improved performance characteristics of Premium SSD v2.
- **Scalable Web Applications:** Web apps with fluctuating storage demands can leverage independent scaling to optimize resource usage and cost.
- **Data Analytics and Reporting:** Workloads involving large volumes of data processing and reporting can utilize the enhanced throughput and IOPS for faster query execution.
- **Migration Scenarios:** Organizations migrating from on-premises or other cloud storage solutions can take advantage of the improved price-performance and flexibility.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which may involve limited regional availability, support, and potential changes before general release.
- **Compatibility:** Users should verify compatibility with their existing MySQL configurations and workloads, as not all features may be available or supported during the preview phase.
- **Cost Management:** While Premium SSD v2 offers improved price-performance, administrators should monitor storage usage and scaling to avoid unexpected costs.

**Integration with Related Azure Services**  
- **Azure Resource Management:** Premium SSD v2 managed disks are provisioned and managed through Azure Resource Manager, enabling integration with automation, monitoring, and governance tools.
- **Backup and Disaster Recovery:** The update maintains compatibility with Azure’s backup and disaster recovery solutions for MySQL, ensuring data protection and business continuity.
- **Security and Compliance:** Managed disks inherit Azure’s security features, including encryption at rest and integration with Azure Active Directory for access control.

**Summary Sentence**  
Azure Database for MySQL now supports Premium SSD v2 managed disks in public preview, offering higher performance, improved price-performance, and flexible storage scaling to meet the demands of modern database workloads.

---

### 160. Generally Available: Microsoft Entra authentication for Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: Microsoft Entra authentication for Azure HorizonDB](https://azure.microsoft.com/updates?id=575111)

**Update ID**: 575111
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Microsoft Entra authentication is now generally available for Azure HorizonDB.

- Key changes or new features  
Azure HorizonDB now supports Microsoft Entra authentication, enabling secure, identity-based access to the database. This feature allows organizations to centrally manage user identities and access permissions using Microsoft Entra, replacing traditional authentication methods such as local database accounts or connection strings with embedded credentials. Entra authentication improves security by leveraging modern identity management and conditional access policies.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB deployments, especially those responsible for database security, access control, and identity management.

- Important notes  
To use Microsoft Entra authentication, you must configure your HorizonDB instance and grant appropriate permissions to Entra users or groups. This update streamlines access management, enhances security, and supports compliance requirements. Existing authentication methods remain supported, but Microsoft recommends transitioning to Entra authentication for improved security and centralized management. Review documentation for configuration steps and best practices.

**Details**:

**Azure Update Report: Microsoft Entra Authentication for Azure HorizonDB (General Availability)**

**Background and Purpose of the Update**  
Microsoft Entra authentication is now generally available for Azure HorizonDB. This update aims to enhance database security by moving from traditional authentication methods (such as local database credentials) to a modern, identity-based approach. The purpose is to enable centralized identity and access management, reducing the risks associated with credential sprawl and simplifying compliance with organizational security policies.

**Specific Features and Detailed Changes**  
With this update, Azure HorizonDB supports Microsoft Entra authentication for database access. Key features include:

- **Centralized Identity Management:** Users and applications can authenticate to HorizonDB using Microsoft Entra identities, eliminating the need for managing separate database credentials.
- **Role-Based Access Control (RBAC):** Access permissions can be managed via Microsoft Entra, allowing fine-grained control over who can access HorizonDB resources.
- **Seamless Integration:** Authentication is handled through Microsoft Entra, enabling organizations to leverage existing identity infrastructure and policies.

**Technical Mechanisms and Implementation Methods**  
The technical implementation involves configuring Azure HorizonDB to accept Microsoft Entra tokens for authentication. When a user or application attempts to connect to HorizonDB, they present a token issued by Microsoft Entra. HorizonDB validates the token and grants access based on the associated identity and its assigned roles.

- **Token-Based Authentication:** Microsoft Entra issues secure tokens (such as OAuth 2.0 or OpenID Connect tokens) that are used to authenticate users/applications.
- **Configuration Steps:** Administrators must configure HorizonDB to trust Microsoft Entra as an identity provider and define access policies within Microsoft Entra.
- **Access Management:** Permissions are managed centrally in Microsoft Entra, streamlining user onboarding/offboarding and access reviews.

**Use Cases and Application Scenarios**  
- **Enterprise Security:** Organizations can enforce corporate security policies and compliance requirements by managing database access through Microsoft Entra.
- **Application Integration:** Applications deployed in Azure can use managed identities or service principals to authenticate to HorizonDB without storing credentials.
- **User Access Control:** IT teams can grant or revoke user access to HorizonDB directly from Microsoft Entra, simplifying administration.

**Important Considerations and Limitations**  
- **Migration Planning:** Existing users authenticated via legacy methods may need to be migrated to Microsoft Entra identities.
- **Policy Configuration:** Proper configuration of Microsoft Entra access policies is essential to ensure secure and appropriate access.
- **Service Dependencies:** The availability and performance of Microsoft Entra directly impact authentication to HorizonDB.
- **Compatibility:** Only features and scenarios supported by Microsoft Entra authentication are available; legacy authentication methods may be deprecated.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** Acts as the central identity provider for HorizonDB authentication.
- **Azure RBAC:** Access to HorizonDB can be managed using Azure RBAC policies defined in Microsoft Entra.
- **Azure Security Center:** Enhanced monitoring and compliance reporting for HorizonDB access via Microsoft Entra.

**Summary Sentence**  
Microsoft Entra authentication for Azure HorizonDB is now generally available, enabling secure, centralized, identity-based access management for database resources.

---

### 161. Generally Available: User-assigned managed identity for Azure HorizonDB

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Generally Available: User-assigned managed identity for Azure HorizonDB](https://azure.microsoft.com/updates?id=575069)

**Update ID**: 575069
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
User-assigned managed identity (UMI) support is now generally available for Azure HorizonDB.

- Key changes or new features  
Azure HorizonDB clusters can now use user-assigned managed identities for authentication and access control. This allows you to assign a managed identity to a HorizonDB cluster, enabling secure access to Azure resources without managing credentials. UMIs can be centrally managed and reused across multiple clusters, improving security and simplifying identity management.

- Target audience affected  
Developers and IT professionals managing Azure HorizonDB clusters, especially those responsible for security, access control, and automation.

- Important notes  
UMI support eliminates the need for storing credentials in application code or configuration files, reducing risk and operational overhead. Existing clusters can be updated to use UMIs, and new clusters can be configured with UMIs during deployment. Ensure proper role assignments for the managed identity to enable required access to Azure resources. This feature aligns with best practices for secure, scalable identity management in Azure environments.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: User-assigned managed identity for Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=575069)

---

**Background and Purpose of the Update**  
This update introduces general availability for user-assigned managed identity (UMI) support in Azure HorizonDB. The primary purpose is to enable secure, credential-free access management for HorizonDB clusters by allowing administrators to assign Azure identities centrally. This reduces the operational overhead associated with managing credentials and enhances security posture by leveraging Azure’s managed identity framework.

**Specific Features and Detailed Changes**  
With this update, Azure HorizonDB clusters can now be configured to use user-assigned managed identities. Previously, HorizonDB may have relied on system-assigned managed identities or manual credential management. The new feature allows administrators to create and assign one or more user-assigned managed identities to HorizonDB clusters. These identities are managed independently of the resource lifecycle, providing greater flexibility and control over identity management.

**Technical Mechanisms and Implementation Methods**  
User-assigned managed identities are Azure resources that can be created and managed separately from the HorizonDB cluster. Once a UMI is created, it can be assigned to a HorizonDB cluster through Azure Resource Manager (ARM) templates, Azure CLI, or the Azure Portal. The HorizonDB cluster then uses the assigned UMI to authenticate securely with other Azure services, such as Azure Key Vault or Azure Storage, without requiring explicit credentials. Access permissions are controlled via Azure Role-Based Access Control (RBAC), ensuring that only authorized resources can access sensitive data or services.

**Use Cases and Application Scenarios**  
- **Centralized Identity Management:** Enterprises can centrally manage identities for multiple HorizonDB clusters, simplifying governance and compliance.
- **Credential-Free Access:** HorizonDB clusters can access Azure services securely without storing or rotating credentials.
- **Multi-Cluster Operations:** Assigning the same UMI to multiple clusters enables consistent access policies and simplifies permission management.
- **Integration with Secure Services:** HorizonDB clusters can use UMIs to access Azure Key Vault for secrets management or Azure Storage for data persistence.

**Important Considerations and Limitations**  
- **Identity Lifecycle:** User-assigned managed identities are independent resources; deleting a UMI will impact all clusters using it.
- **RBAC Configuration:** Proper configuration of RBAC roles and permissions is essential to ensure secure access.
- **Resource Limits:** Azure imposes limits on the number of managed identities that can be assigned to a resource; consult Azure documentation for specifics.
- **Service Integration:** Only Azure services that support managed identities can be accessed using UMIs.

**Integration with Related Azure Services**  
UMIs for HorizonDB clusters integrate seamlessly with Azure Active Directory, Azure Key Vault, Azure Storage, and other services supporting managed identities. This enables secure, scalable, and centralized access management across the Azure ecosystem, leveraging existing identity and access management practices.

---

**Summary Sentence:**  
User-assigned managed identity support is now generally available for Azure HorizonDB, enabling centralized and credential-free identity management for secure access to Azure services by HorizonDB clusters.

---

### 162. Public Preview: Windows Trusted Launch 

**Published**: November 17, 2026 20:00:32 UTC
**Link**: [Public Preview: Windows Trusted Launch ](https://azure.microsoft.com/updates?id=572591)

**Update ID**: 572591
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Microsoft Ignite, Feature

**Summary**:

- What was updated  
Windows Trusted Launch is now in public preview for Windows node pools on Azure Kubernetes Service (AKS), specifically with Windows Server 2025.

- Key changes or new features  
Trusted Launch provides enhanced security for Windows workloads on AKS by enabling secure boot and virtual Trusted Platform Module (vTPM) support. This ensures stronger boot-chain protection, helping safeguard against rootkits and boot-level malware. Previously, Trusted Launch was only available for Linux node pools; now, Windows node pools can benefit from these security features.

- Target audience affected  
This update is relevant to developers and IT professionals managing Windows workloads on AKS, especially those in regulated or security-sensitive industries requiring advanced security measures.

- Important notes  
Trusted Launch support is currently in public preview and available only for Windows Server 2025 node pools on AKS. Users should test and validate workloads in this preview environment before deploying to production. This feature helps meet compliance and security requirements for organizations running Windows containers in AKS.  

For more details, see the Azure Update: [Windows Trusted Launch Public Preview](https://azure.microsoft.com/updates?id=572591).

**Details**:

**Azure Update Report: Public Preview – Windows Trusted Launch for AKS Windows Node Pools**

**Background and Purpose of the Update:**  
Azure Kubernetes Service (AKS) is widely used to orchestrate containerized workloads, including those running on Windows. Many organizations, especially those operating in regulated or security-sensitive environments, require enhanced boot-chain protection to ensure the integrity of their infrastructure. Historically, Trusted Launch—a feature that provides secure boot and virtual Trusted Platform Module (vTPM) capabilities—has been available only for Linux node pools in AKS. The lack of Trusted Launch support for Windows node pools has been a gap for teams needing robust security assurances for Windows workloads.

**Specific Features and Detailed Changes:**  
With the introduction of Windows Server 2025, AKS now enters public preview for Trusted Launch support on Windows node pools. This update enables Windows workloads in AKS to benefit from advanced boot-chain protection mechanisms previously limited to Linux. Key features include:

- **Secure Boot:** Ensures that only signed and trusted code is executed during the VM boot process, preventing rootkits and boot-level malware.
- **Virtual TPM (vTPM):** Provides hardware-backed cryptographic functions and secure storage for secrets, keys, and certificates, enhancing workload security.
- **Integration with Windows Server 2025:** Trusted Launch is enabled specifically for node pools running Windows Server 2025, leveraging the latest OS security enhancements.

**Technical Mechanisms and Implementation Methods:**  
Trusted Launch operates by combining Secure Boot and vTPM within the Azure infrastructure:

- **Secure Boot:** Utilizes UEFI firmware to validate the integrity of the bootloader and OS kernel, ensuring that only Microsoft-signed binaries are loaded.
- **vTPM:** Each VM is provisioned with a virtual TPM, which emulates hardware TPM functionality. This allows workloads to securely store secrets and perform cryptographic operations, supporting BitLocker and other TPM-dependent features.
- **AKS Node Pool Configuration:** When creating or updating a Windows node pool in AKS, administrators can enable Trusted Launch, provided the node pool is based on Windows Server 2025 images.

**Use Cases and Application Scenarios:**  
This update is particularly relevant for:

- **Regulated Industries:** Organizations in finance, healthcare, and government sectors requiring compliance with strict security standards.
- **Security-Sensitive Workloads:** Applications handling confidential data or intellectual property, where boot-chain integrity is critical.
- **Hybrid and Multi-cloud Deployments:** Teams seeking consistent security postures across Linux and Windows workloads in AKS.

**Important Considerations and Limitations:**  
- **Preview Status:** The feature is currently in public preview, which means it is not recommended for production workloads until general availability.
- **Windows Server 2025 Requirement:** Trusted Launch is only supported for node pools running Windows Server 2025; earlier versions are not eligible.
- **Feature Scope:** Trusted Launch is limited to boot-chain protection and vTPM capabilities; additional security features may require separate configuration.
- **Compatibility:** Ensure that applications and workloads are compatible with Secure Boot and vTPM, especially if they rely on custom drivers or boot configurations.

**Integration with Related Azure Services:**  
Trusted Launch for Windows node pools integrates seamlessly with other Azure security offerings:

- **Azure Security Center:** Monitors and reports on the security posture of AKS clusters, including Trusted Launch status.
- **Azure Policy:** Enables enforcement of Trusted Launch configurations across AKS deployments.
- **Azure Key Vault:** Works in conjunction with vTPM for secure key management and storage.

**Summary Sentence:**  
The public preview of Trusted Launch for Windows node pools in AKS, leveraging Windows Server 2025, introduces advanced boot-chain protection and vTPM support, addressing the security needs of regulated and sensitive environments.

---

### 163. Limited Preview: Compute templates for Azure

**Published**: November 17, 2026 20:00:24 UTC
**Link**: [Limited Preview: Compute templates for Azure](https://azure.microsoft.com/updates?id=580624)

**Update ID**: 580624
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure announced a limited preview of compute templates, a new feature for managing virtual machine (VM) configurations.

- Key changes or new features  
Compute templates allow users to define, version, and reuse standardized VM configurations. This streamlines VM deployment and configuration management by enabling consistent setups across environments. Templates can be easily updated and shared, reducing manual errors and improving operational efficiency. The feature supports integration with existing Azure tools and workflows.

- Target audience affected  
Developers, IT professionals, and cloud administrators responsible for VM provisioning, configuration, and management in Azure environments.

- Important notes  
The compute templates feature is currently available in limited preview. Interested users must sign up for access. Early adopters can provide feedback to help shape future enhancements. This capability is especially useful for organizations seeking to enforce configuration standards, automate VM deployments, and maintain compliance across multiple projects or teams.

**Details**:

**Azure Update Report: Limited Preview – Compute Templates for Azure**

**Background and Purpose of the Update**  
The limited preview of Azure compute templates introduces a new capability designed to streamline and standardize virtual machine (VM) configuration management. The primary objective is to enable customers to define, version, and reuse VM configurations, thereby reducing manual configuration errors, improving consistency across deployments, and simplifying operational overhead. This update addresses the need for scalable and repeatable VM provisioning processes in enterprise environments.

**Specific Features and Detailed Changes**  
Azure compute templates allow users to create standardized configuration definitions for VMs. Key features include:
- **Template Definition:** Users can specify VM parameters such as OS type, size, networking, storage, and other configuration settings in a template format.
- **Versioning:** Each template can be versioned, enabling tracking of changes and rollback to previous configurations if necessary.
- **Reusability:** Templates can be reused across multiple deployments, ensuring uniformity and reducing the time required to configure VMs for different projects or environments.
- **Simplified Management:** The templates provide a centralized mechanism for managing VM configurations, reducing the need for custom scripts or manual setup.

**Technical Mechanisms and Implementation Methods**  
The compute templates are implemented as a new Azure resource type, accessible through the Azure portal, CLI, or ARM (Azure Resource Manager) templates. Users define templates using a declarative syntax, specifying all relevant VM configuration parameters. These templates are stored and managed within Azure, enabling version control and easy retrieval for subsequent deployments. When deploying a VM, users reference the desired template and version, and Azure automatically provisions the VM according to the defined settings.

**Use Cases and Application Scenarios**  
- **Enterprise Standardization:** Organizations can enforce standardized VM configurations across departments, ensuring compliance and security.
- **Dev/Test Environments:** Developers and testers can quickly spin up VMs with consistent settings, reducing setup time and minimizing configuration drift.
- **Multi-region Deployments:** Templates facilitate rapid deployment of identical VM configurations across multiple Azure regions, supporting global operations.
- **Disaster Recovery:** Versioned templates enable quick restoration of VM environments to known-good states.

**Important Considerations and Limitations**  
- **Limited Preview:** The feature is currently in limited preview, which may restrict access and functionality. Not all Azure customers may be eligible to participate.
- **Supported Configurations:** Only certain VM configuration parameters may be supported during the preview phase; users should consult official documentation for details.
- **Integration Constraints:** Some advanced features or integrations with other Azure services may not be fully available in the preview.
- **Change Management:** Users must manage template versions carefully to avoid unintended configuration changes across deployments.

**Integration with Related Azure Services**  
Compute templates are designed to work alongside existing Azure deployment tools, such as ARM templates and Azure DevOps pipelines. They can be integrated into automated workflows for VM provisioning, and may interact with services like Azure Policy for compliance enforcement, Azure Resource Manager for orchestration, and Azure Monitor for tracking deployments.

**Summary Sentence**  
Azure has announced a limited preview of compute templates, enabling customers to define, version, and reuse standardized VM configurations, thereby simplifying and centralizing virtual machine configuration management across deployments.

---

### 164. Public Preview: Migrate Azure Database for PostgreSQL to Azure HorizonDB with Azure Database Migration Service (DMS) 

**Published**: November 17, 2026 20:00:24 UTC
**Link**: [Public Preview: Migrate Azure Database for PostgreSQL to Azure HorizonDB with Azure Database Migration Service (DMS) ](https://azure.microsoft.com/updates?id=579612)

**Update ID**: 579612
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Migration, Azure Database for PostgreSQL, Azure Database Migration Service, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

**What was updated:**  
Azure Database Migration Service (DMS) now supports migrating Azure Database for PostgreSQL workloads to Azure HorizonDB in public preview.

**Key changes or new features:**  
- Seamless migration path from Azure Database for PostgreSQL to Azure HorizonDB using DMS.  
- Extension of DMS V2 architecture to include HorizonDB as a migration target.  
- Managed migration experience, reducing manual steps and minimizing downtime.

**Target audience affected:**  
- Developers and database administrators managing PostgreSQL workloads on Azure.  
- IT professionals planning database modernization or platform upgrades.

**Important notes:**  
- This feature is currently in public preview; production workloads should be evaluated carefully before migration.  
- Migration leverages DMS V2, so users should ensure compatibility and review migration prerequisites.  
- HorizonDB is a new Azure database offering; review its features and limitations before migrating.  
- Documentation and support for this migration path are available via Azure updates and DMS resources.

[Azure Update Link](https://azure.microsoft.com/updates?id=579612)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Migrate Azure Database for PostgreSQL to Azure HorizonDB with Azure Database Migration Service (DMS)

**Background and Purpose of the Update:**  
This update introduces the capability to migrate existing Azure Database for PostgreSQL workloads directly to Azure HorizonDB using Azure Database Migration Service (DMS). The primary purpose is to provide a seamless, managed migration path for customers looking to transition their PostgreSQL databases to HorizonDB, leveraging the robust migration tooling offered by DMS. This aligns with Azure’s strategy to simplify database modernization and enable customers to adopt new database technologies with minimal disruption.

**Specific Features and Detailed Changes:**  
- **Migration Support:** Azure DMS now supports migrations from Azure Database for PostgreSQL to Azure HorizonDB, expanding its portfolio of supported source and target database combinations.
- **Managed Experience:** The migration process is fully managed, reducing manual intervention and complexity for IT teams.
- **DMS V2 Architecture Extension:** The update extends the DMS V2 architecture, allowing HorizonDB to be used as a migration target, which means customers benefit from the improved scalability, reliability, and performance enhancements of DMS V2.

**Technical Mechanisms and Implementation Methods:**  
- **Migration Workflow:** The migration is orchestrated through Azure DMS, which automates schema and data transfer from PostgreSQL to HorizonDB.
- **Seamless Integration:** The process is designed to be seamless, with DMS handling the connectivity, schema mapping, data movement, and validation steps.
- **Managed Service:** Azure DMS operates as a managed service, abstracting the underlying infrastructure and providing a consistent migration experience through the Azure portal or API.
- **Architecture:** By leveraging the DMS V2 architecture, migrations benefit from improved throughput, parallelism, and error handling, ensuring efficient and reliable data transfer.

**Use Cases and Application Scenarios:**  
- **Database Modernization:** Organizations seeking to modernize their database infrastructure by moving from Azure Database for PostgreSQL to Azure HorizonDB.
- **Consolidation:** Enterprises consolidating workloads onto HorizonDB for performance, scalability, or cost reasons.
- **Cloud-Native Adoption:** Teams adopting HorizonDB for its cloud-native features, while retaining the ability to migrate existing PostgreSQL workloads without downtime or data loss.

**Important Considerations and Limitations:**  
- **Public Preview:** The feature is currently in public preview, which means it may not be suitable for production workloads and could have limited support or features.
- **Supported Scenarios:** Only migrations from Azure Database for PostgreSQL to Azure HorizonDB are supported; other source or target combinations may not be available.
- **Preview Limitations:** Customers should review Azure’s documentation for any preview-specific limitations, such as supported PostgreSQL versions, migration throughput, or feature gaps.

**Integration with Related Azure Services:**  
- **Azure Database Migration Service (DMS):** The migration process is fully integrated with DMS, utilizing its orchestration, monitoring, and reporting capabilities.
- **Azure Portal:** Migration workflows can be initiated and managed via the Azure portal, providing visibility and control.
- **HorizonDB Integration:** Once migrated, workloads can leverage HorizonDB’s features and integrate with other Azure services as required.

**Summary Sentence:**  
Azure Database Migration Service now enables managed, seamless migrations of Azure Database for PostgreSQL workloads to Azure HorizonDB, extending DMS V2 architecture and supporting database modernization scenarios in public preview.

---

### 165. Public Preview: Migrate PostgreSQL servers to Azure HorizonDB 

**Published**: November 17, 2026 20:00:24 UTC
**Link**: [Public Preview: Migrate PostgreSQL servers to Azure HorizonDB ](https://azure.microsoft.com/updates?id=579564)

**Update ID**: 579564
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database Migration Service now supports migrations of PostgreSQL workloads to Azure HorizonDB in public preview.

- Key changes or new features  
A new guided migration experience is available in the Azure portal, enabling users to migrate supported PostgreSQL servers—including Azure Database for PostgreSQL—to Azure HorizonDB. This update streamlines the migration process, providing step-by-step guidance and reducing manual intervention. The service supports both online and offline migrations, allowing flexibility based on business requirements.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases, especially those considering modernization or transitioning to Azure HorizonDB. Teams responsible for database infrastructure, cloud migration, and application modernization will benefit from this update.

- Important notes  
This feature is currently in public preview, so production workloads should be migrated with caution. Review supported PostgreSQL versions and workloads before starting migration. Azure HorizonDB offers enhanced scalability and performance, making it a strategic option for organizations looking to modernize their database platform. For more details and prerequisites, refer to the official Azure documentation and the update link.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Migrate PostgreSQL servers to Azure HorizonDB

**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579564)

---

**Background and Purpose of the Update**  
This update introduces public preview support for migrating PostgreSQL servers to Azure HorizonDB using Azure Database Migration Service (DMS). The primary purpose is to facilitate seamless migration of supported PostgreSQL workloads, including those hosted on Azure Database for PostgreSQL, to Azure HorizonDB. This aligns with Microsoft’s ongoing strategy to provide robust migration pathways for customers seeking to modernize their database infrastructure within Azure.

**Specific Features and Detailed Changes**  
- **Azure Portal-Based Guided Experience:** The migration process is now integrated into the Azure portal, offering step-by-step guidance for IT professionals.  
- **Support for PostgreSQL Workloads:** The update specifically enables migration of supported PostgreSQL workloads, which includes Azure Database for PostgreSQL instances, to Azure HorizonDB.  
- **Public Preview Availability:** The feature is currently in public preview, allowing users to test and evaluate the migration process before general availability.

**Technical Mechanisms and Implementation Methods**  
- **Azure Database Migration Service (DMS):** The migration leverages Azure DMS, which orchestrates the data transfer and schema conversion from PostgreSQL to Azure HorizonDB.  
- **Portal Workflow:** Users initiate and manage migrations directly through the Azure portal, utilizing a guided workflow that covers source selection, target configuration, and migration execution.  
- **Supported Workloads:** Only workloads supported by the migration service are eligible; unsupported features or extensions may require manual intervention or are not migrated.

**Use Cases and Application Scenarios**  
- **Cloud Modernization:** Organizations running PostgreSQL workloads on-premises or on Azure Database for PostgreSQL can use this feature to migrate to Azure HorizonDB, potentially benefiting from improved performance, scalability, or new HorizonDB capabilities.  
- **Consolidation and Optimization:** Enterprises seeking to consolidate databases or optimize their cloud footprint can leverage this guided migration to streamline transitions to HorizonDB.  
- **Testing and Evaluation:** The public preview allows IT teams to evaluate the migration process and HorizonDB’s compatibility with their PostgreSQL workloads.

**Important Considerations and Limitations**  
- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should validate migrations in test environments before full-scale adoption.  
- **Supported Workloads:** Only supported PostgreSQL workloads can be migrated; unsupported features, custom extensions, or specific configurations may not be handled automatically.  
- **Migration Complexity:** Depending on workload complexity, schema differences, and data volume, migration may require additional planning and post-migration validation.

**Integration with Related Azure Services**  
- **Azure Database Migration Service:** The update is tightly integrated with Azure DMS, leveraging its capabilities for schema and data migration.  
- **Azure Portal:** The migration workflow is accessible via the Azure portal, ensuring a unified management experience.  
- **Azure Database for PostgreSQL:** The service supports migration from Azure Database for PostgreSQL, facilitating transitions within Azure’s database ecosystem.

---

**Summary Sentence:**  
Azure Database Migration Service now offers a public preview for guided, portal-based migration of supported PostgreSQL workloads—including Azure Database for PostgreSQL—to Azure HorizonDB, enabling IT professionals to evaluate and streamline database modernization within Azure.

---


*This report was automatically generated - 2026-11-18 04:22:51 UTC*