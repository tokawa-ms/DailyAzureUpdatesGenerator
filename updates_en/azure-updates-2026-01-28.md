# January 28, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: January 28, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: Azure NetApp Files support in OpenShift Virtualization 

**Published**: January 27, 2026 17:00:06 UTC
**Link**: [Public Preview: Azure NetApp Files support in OpenShift Virtualization ](https://azure.microsoft.com/updates?id=550466)

**Update ID**: 550466
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files

**Summary**:

- What was updated  
Azure NetApp Files now supports integration with OpenShift Virtualization in public preview.

- Key changes or new features  
This update enables fast virtual machine provisioning, instant cloning, and live migration capabilities within OpenShift Virtualization environments. It provides seamlessly scalable, high-performance storage optimized for VM workloads, along with enterprise-grade data management features such as snapshots, backups, and replication.

- Target audience affected  
Developers and IT professionals managing containerized VM workloads on OpenShift, especially those requiring high-performance, scalable storage solutions with advanced data management in Azure.

- Important notes if any  
As this feature is in public preview, users should evaluate it in non-production environments and provide feedback. Integration with Azure NetApp Files can significantly improve VM lifecycle operations in OpenShift but requires appropriate Azure NetApp Files capacity and configuration.  

For more details, visit: https://azure.microsoft.com/updates?id=550466

**Details**:

The recent public preview announcement of Azure NetApp Files (ANF) support in OpenShift Virtualization introduces a significant enhancement for enterprises running virtual machine (VM) workloads within Red Hat OpenShift environments on Azure. This update enables advanced storage capabilities such as fast VM provisioning, instant cloning, and live migration, leveraging ANF’s high-performance, scalable, and enterprise-grade storage platform.

**Background and Purpose:**  
OpenShift Virtualization allows users to run VMs alongside containerized workloads on OpenShift clusters, facilitating hybrid application architectures and modernization efforts. However, VM storage performance and management have traditionally been challenges, especially at scale. Azure NetApp Files, a fully managed file storage service offering high throughput and low latency, addresses these challenges by providing a robust storage backend. The integration aims to streamline VM lifecycle operations, improve performance predictability, and simplify data management for VM workloads in OpenShift.

**Specific Features and Detailed Changes:**  
- **Fast VM Provisioning:** ANF’s snapshot and cloning capabilities enable rapid deployment of new VMs by instantly creating writable clones from existing VM images or templates without duplicating data. This significantly reduces provisioning time compared to traditional storage solutions.  
- **Instant Cloning:** Leveraging ANF snapshots, OpenShift Virtualization can create VM clones instantly, facilitating rapid scaling and testing scenarios.  
- **Live Migration Support:** The integration supports live migration of VMs between nodes without downtime, made possible by ANF’s consistent performance and shared storage architecture.  
- **Seamless Scalability:** ANF provides scalable storage volumes that can be dynamically resized to meet changing workload demands, ensuring consistent performance.  
- **Enterprise Data Management:** Features such as data replication, backup integration, and encryption are natively supported, enhancing data protection and compliance for VM workloads.

**Technical Mechanisms and Implementation Methods:**  
ANF uses the NFSv3 protocol to present storage volumes to OpenShift clusters. OpenShift Virtualization leverages Container Storage Interface (CSI) drivers to provision and manage ANF volumes dynamically. The fast provisioning and cloning capabilities rely on ANF’s snapshot technology, which creates point-in-time, space-efficient copies of data. Live migration is facilitated by the shared storage model where VM disk files reside on ANF volumes accessible by multiple cluster nodes, allowing VM state to move without data transfer delays. Integration requires configuring ANF volumes as persistent volumes (PVs) within OpenShift and associating them with virtual machine instances.

**Use Cases and Application Scenarios:**  
- **Development and Testing:** Rapid VM cloning accelerates environment setup for developers and testers, enabling quick iteration cycles.  
- **Hybrid Workloads:** Enterprises running mixed container and VM workloads on OpenShift can unify storage management and improve resource utilization.  
- **Disaster Recovery and High Availability:** Live migration and snapshot capabilities support resilient VM operations and simplified DR strategies.  
- **Data-Intensive Applications:** Applications requiring high IOPS and low latency, such as databases or analytics workloads running in VMs, benefit from ANF’s performance guarantees.

**Important Considerations and Limitations:**  
- As a public preview feature, users should expect potential limitations or changes before general availability.  
- NFSv3 protocol support may impose certain constraints compared to block storage options, such as lack of native SMB or iSCSI support.  
- Proper network configuration and permissions are required to ensure secure and performant access to ANF volumes from OpenShift clusters.  
- Cost implications of using premium ANF tiers should be evaluated against workload requirements.

**Integration with Related Azure Services:**  
This update complements Azure Kubernetes Service (AKS) and OpenShift on Azure by enhancing VM workload support. It integrates with Azure NetApp Files’ existing ecosystem, including Azure Backup for data protection and Azure Monitor for performance insights. The solution also aligns with Azure Active Directory for access control and Azure Policy for governance, enabling enterprises to maintain security and compliance standards while managing hybrid cloud workloads.

In summary, the Azure Net

---

### 2. Public Preview: 7th generation Intel-based VMs – Dlsv7/Dsv7/Esv7 

**Published**: January 27, 2026 17:00:06 UTC
**Link**: [Public Preview: 7th generation Intel-based VMs – Dlsv7/Dsv7/Esv7 ](https://azure.microsoft.com/updates?id=529407)

**Update ID**: 529407
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines

**Summary**:

- What was updated  
Azure announced the public preview of the 7th generation Intel-based virtual machines: Dlsv7, Dsv7 (General Purpose), and Esv7 (Memory Optimized) series.

- Key changes or new features  
These new VM series are powered by the latest Intel® Xeon® 6 processors (Granite Rapids), offering improved compute performance and efficiency. They provide enhanced memory bandwidth and support for advanced Intel technologies, enabling better workload handling for general-purpose and memory-intensive applications. The VMs are designed to support scalable enterprise applications, databases, and analytics workloads with improved price-performance ratios.

- Target audience affected  
Developers and IT professionals running compute and memory-intensive workloads on Azure, including those managing enterprise applications, large databases, and analytics platforms, will benefit from these new VM options.

- Important notes if any  
These VMs are currently in public preview, so users should test workloads accordingly before production deployment. Availability may vary by region, and pricing details are subject to change upon general availability. Users should review compatibility with existing software and consider performance benchmarking to optimize workload placement.  

Link for details: https://azure.microsoft.com/updates?id=529407

**Details**:

The Azure update announces the public preview of the 7th generation Intel-based virtual machines—specifically the Dlsv7, Dsv7, and Esv7 series—featuring the latest Intel® Xeon® 6 processors (Granite Rapids). These new VM families are designed to deliver enhanced compute performance, memory capacity, and security capabilities to support increasingly demanding enterprise workloads.

**Background and Purpose:**  
As cloud workloads grow in complexity and scale, there is a continuous need for more powerful and efficient VM options. The introduction of the 7th generation Intel-based VMs addresses this demand by leveraging Intel’s latest Granite Rapids architecture, which offers improved CPU performance, energy efficiency, and advanced security features. This update aims to provide Azure customers with VMs optimized for general-purpose and memory-intensive applications, enabling better performance per core and cost efficiency.

**Specific Features and Detailed Changes:**  
- **Processor:** The VMs utilize Intel Xeon 6th generation processors (Granite Rapids), which bring architectural improvements such as higher core counts, increased instructions per cycle (IPC), and enhanced vector processing capabilities.  
- **VM Series:**  
  - *Dlsv7* – General purpose VMs optimized for balanced CPU-to-memory ratio with local NVMe storage options.  
  - *Dsv7* – General purpose VMs with a focus on balanced compute and memory, suitable for a wide range of enterprise applications.  
  - *Esv7* – Memory optimized VMs designed for workloads requiring large memory footprints, such as SAP HANA, databases, and analytics.  
- **Memory and Storage:** These VMs support larger memory sizes and faster local NVMe storage, improving data throughput and reducing latency for I/O intensive applications.  
- **Security:** Enhanced security features include Intel’s latest hardware-based security technologies, such as Intel Total Memory Encryption (TME) and advanced cryptographic acceleration, providing improved data protection and compliance capabilities.  
- **Networking:** Integration with Azure’s accelerated networking capabilities ensures low latency and high throughput for network-intensive workloads.

**Technical Mechanisms and Implementation:**  
The VMs are built on Azure’s hypervisor platform, optimized to leverage the new processor microarchitecture. The Granite Rapids CPUs support advanced vector extensions and improved cache hierarchies, which Azure’s VM provisioning and scheduling systems utilize to maximize workload efficiency. Local NVMe storage is directly attached to the VM host, providing high IOPS and low latency storage access. The security enhancements are implemented at the silicon level and exposed through Azure’s trusted computing environment, ensuring transparent encryption and secure boot processes.

**Use Cases and Application Scenarios:**  
- Enterprise applications requiring balanced compute and memory resources, such as web servers, application servers, and mid-tier databases (Dsv7, Dlsv7).  
- High-performance computing (HPC) and analytics workloads that benefit from faster CPU and memory throughput.  
- Memory-intensive applications including large-scale SAP HANA deployments, in-memory databases, and real-time analytics platforms (Esv7).  
- Workloads requiring enhanced security and compliance, such as financial services and healthcare applications.

**Important Considerations and Limitations:**  
- As these VMs are currently in public preview, they may not be covered by standard Azure SLA and could have limited regional availability.  
- Compatibility testing is recommended before production deployment, especially for legacy applications sensitive to CPU architecture changes.  
- Pricing and billing details for the new VM sizes may differ from previous generations and should be reviewed accordingly.  
- Some Azure services or third-party software integrations may require updates to fully leverage the new hardware capabilities.

**Integration with Related Azure Services:**  
- These VMs can be deployed within Azure Virtual Machine Scale Sets (VMSS) to enable scalable and resilient application architectures.  
- Integration with Azure Disk Storage, including Premium SSD and Ultra Disk, complements the local NVMe storage for persistent data needs.  
- Azure Security Center and Azure Defender can leverage the

---

### 3. Public Preview: Azure Command Launcher for Java

**Published**: January 27, 2026 14:00:07 UTC
**Link**: [Public Preview: Azure Command Launcher for Java](https://azure.microsoft.com/updates?id=543994)

**Update ID**: 543994
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Mobile, Web, Containers, App Service, Azure Container Apps, Azure Container Instances, Azure Kubernetes Service (AKS), Azure Red Hat OpenShift, Virtual Machines

**Summary**:

- What was updated  
Microsoft announced the Public Preview of the Azure Command Launcher for Java, a new JVM launcher optimized for Azure environments.

- Key changes or new features  
The Azure Command Launcher for Java improves default ergonomics for Java applications running in containers and virtual machines on Azure. It streamlines startup performance and resource utilization, enhancing Java app deployment and management in cloud-native scenarios.

- Target audience affected  
Java developers deploying applications on Azure, DevOps engineers managing Java workloads in containers or VMs, and IT professionals responsible for optimizing Java app performance in Azure environments.

- Important notes if any  
This feature is currently in Public Preview, so users should evaluate it in non-production environments first. Feedback during the preview phase will help improve the launcher before general availability. Further documentation and usage guidance are available via the official Azure update link.

**Details**:

The Azure Command Launcher for Java, announced in Public Preview at Microsoft Ignite 2025, is a specialized JVM launcher designed to optimize Java application performance and developer experience specifically within Azure environments, particularly for containerized and virtual machine deployments. This update addresses common challenges faced by Java applications running in cloud-native contexts by improving startup times, resource utilization, and configuration simplicity.

**Background and Purpose:**  
Java applications deployed on Azure, especially within containers or virtual machines, often encounter suboptimal startup latency, memory overhead, and complex JVM tuning requirements. Traditional JVM launchers are generic and do not cater to the unique constraints and operational models of cloud platforms. The Azure Command Launcher for Java was developed to provide an Azure-optimized JVM launcher that simplifies these aspects, enabling smoother Java app deployment and scaling in cloud-native architectures.

**Specific Features and Detailed Changes:**  
- **Optimized JVM Startup:** The launcher reduces JVM startup time by pre-configuring JVM options tailored for Azure container and VM environments, enhancing application responsiveness.  
- **Automatic Resource Configuration:** It dynamically adjusts heap sizes and garbage collection parameters based on the detected Azure environment and available resources, minimizing manual tuning.  
- **Simplified Command Syntax:** The launcher abstracts complex JVM command-line arguments into a streamlined interface, reducing configuration errors and improving developer ergonomics.  
- **Container and VM Awareness:** It detects whether the Java application is running inside an Azure container or VM and applies environment-specific optimizations accordingly.  
- **Enhanced Logging and Diagnostics:** Integrated telemetry hooks provide detailed JVM and application performance metrics compatible with Azure Monitor and Application Insights.

**Technical Mechanisms and Implementation Methods:**  
The Azure Command Launcher for Java operates as a wrapper around the standard JVM executable. Upon invocation, it inspects the runtime environment, including container metadata (such as cgroup limits) and Azure VM characteristics, to determine optimal JVM parameters. It then constructs the JVM launch command with these parameters, incorporating best practices for memory management (e.g., setting -Xmx and -Xms based on container memory limits), garbage collection tuning (favoring G1GC or ZGC depending on Java version and workload), and startup flags that reduce class loading overhead. The launcher is implemented in native code with integration hooks to Azure SDKs for environment detection and telemetry emission.

**Use Cases and Application Scenarios:**  
- **Containerized Java Microservices:** Deploying Java microservices in Azure Kubernetes Service (AKS) or Azure Container Instances benefits from faster startup and optimized memory usage, improving scalability and cost-efficiency.  
- **Java Applications on Azure VMs:** Applications running on Azure Virtual Machines gain from environment-aware tuning without manual JVM parameter configuration.  
- **DevOps Pipelines:** The launcher simplifies CI/CD pipeline scripts by reducing JVM configuration complexity, enabling consistent runtime behavior across development, staging, and production.  
- **Performance-Sensitive Applications:** Applications requiring rapid scaling or low-latency startup, such as serverless or event-driven Java workloads, see improved responsiveness.

**Important Considerations and Limitations:**  
- The launcher currently supports Java 11 and later versions; legacy Java versions may not be fully compatible.  
- As a preview feature, some JVM tuning parameters may require manual overrides for specialized workloads.  
- Integration with custom JVM agents or native libraries should be tested, as the launcher modifies JVM startup commands.  
- The launcher is optimized for Azure environments and may not provide benefits or could behave unexpectedly outside Azure or on non-containerized platforms.

**Integration with Related Azure Services:**  
- **Azure Monitor and Application Insights:** The launcher’s telemetry hooks enable seamless integration with Azure monitoring tools, providing JVM-level metrics alongside application logs.  
- **Azure Kubernetes Service (AKS):** The launcher complements AKS by optimizing Java container workloads, improving pod startup times and resource utilization.  
- **Azure DevOps:** Simplifies pipeline configurations for Java applications by standardizing JVM launch parameters.  
- **Azure Virtual Machines:** Enhances Java workloads running on VMs

---


*This report was automatically generated - 2026-01-28 03:02:14 UTC*