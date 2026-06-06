# June 06, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 06, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: Ingestion Volume Change dashboard in Metrics Usage Insights

**Published**: June 05, 2026 20:45:48 UTC
**Link**: [Public Preview: Ingestion Volume Change dashboard in Metrics Usage Insights](https://azure.microsoft.com/updates?id=565286)

**Update ID**: 565286
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Features, Microsoft Build

**Summary**:

- What was updated  
Azure Metrics Usage Insights now offers a new Ingestion Volume Change dashboard, available in public preview.

- Key changes or new features  
The new dashboard allows users to visualize and compare ingestion volume trends over time. It helps quickly identify spikes or drops in time series counts and event ingestion rates. This feature supports faster root cause analysis for unexpected cost changes and usage anomalies.

- Target audience affected  
This update is relevant for developers, IT professionals, and operations teams who monitor and manage Azure resource metrics, especially those concerned with cost management, usage analytics, and troubleshooting.

- Important notes if any  
The feature is currently in public preview, so it may be subject to changes and improvements. Users can leverage this dashboard to proactively monitor ingestion patterns and optimize resource usage and costs.

Data source: Using API data  
For more details, see the official update: https://azure.microsoft.com/updates?id=565286

**Details**:

**Azure Update Report: Public Preview – Ingestion Volume Change Dashboard in Metrics Usage Insights**

**Background and Purpose of the Update:**  
The Ingestion Volume Change dashboard has been introduced in public preview within Metrics Usage Insights. This update addresses the need for enhanced visibility into metrics ingestion patterns over time. By enabling users to monitor and compare ingestion volumes, the dashboard supports proactive management of telemetry data flows, helping organizations quickly identify anomalies such as spikes or drops in time series counts and event ingestion rates. The primary goal is to facilitate faster investigation of cost fluctuations and optimize resource utilization.

**Specific Features and Detailed Changes:**  
- **New Dashboard Addition:** The Ingestion Volume Change dashboard is now available within Metrics Usage Insights.
- **Comparative Visualization:** Users can view and compare ingestion volumes across different time intervals, allowing for temporal analysis of data ingestion trends.
- **Anomaly Detection:** The dashboard provides immediate visibility into significant changes, such as sudden increases (spikes) or decreases (drops) in time series data and event ingestion rates.
- **Cost Investigation Support:** By correlating ingestion volume changes with cost metrics, users can more efficiently investigate and attribute cost variations to specific telemetry patterns.

**Technical Mechanisms and Implementation Methods:**  
- The dashboard leverages existing telemetry and metrics collection infrastructure within Azure, aggregating ingestion volume data over configurable time windows.
- Visualization components present ingestion trends, enabling users to filter and drill down into specific periods or data sources.
- The system likely utilizes backend analytics to detect and highlight significant deviations in ingestion rates, though the precise detection algorithms are not detailed in the update.

**Use Cases and Application Scenarios:**  
- **Cost Management:** IT professionals can use the dashboard to correlate ingestion volume changes with billing data, identifying the root causes of unexpected cost increases or decreases.
- **Operational Monitoring:** Operations teams can monitor for abnormal ingestion patterns that may indicate issues such as misconfigured telemetry, application errors, or sudden changes in user activity.
- **Capacity Planning:** By understanding historical ingestion trends, teams can forecast future needs and adjust resource allocations accordingly.
- **Incident Response:** Rapid detection of ingestion anomalies enables faster troubleshooting and resolution of incidents affecting telemetry pipelines.

**Important Considerations and Limitations:**  
- The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- The update focuses specifically on ingestion volume; it does not provide direct insights into data quality, schema changes, or downstream processing performance.
- The scope and granularity of available metrics and the retention period for historical data are not specified in the update.

**Integration with Related Azure Services:**  
- The dashboard is part of Metrics Usage Insights, which integrates with Azure Monitor and related telemetry services.
- It complements existing monitoring, alerting, and cost management tools within the Azure ecosystem, providing an additional layer of visibility for data ingestion patterns.
- Users can leverage the dashboard alongside Azure Cost Management and Azure Monitor to achieve end-to-end observability and cost optimization.

**Summary Sentence:**  
The public preview of the Ingestion Volume Change dashboard in Metrics Usage Insights provides IT professionals with enhanced tools to monitor, compare, and investigate telemetry ingestion volumes over time, supporting faster detection of anomalies and more effective cost management within Azure environments.

---

### 2. Private Preview: Guest RDMA on Azure Boost

**Published**: June 05, 2026 20:30:12 UTC
**Link**: [Private Preview: Guest RDMA on Azure Boost](https://azure.microsoft.com/updates?id=564981)

**Update ID**: 564981
**Data source**: Azure Updates API

**Categories**: In development, Features, Microsoft Build

**Summary**:

- What was updated  
Azure has introduced a private preview of Guest RDMA (Remote Direct Memory Access) support on Azure Boost, initially available in the UK South region.

- Key changes or new features  
Guest RDMA enables high-throughput, ultra-low latency networking directly within guest VMs, allowing applications to bypass the host OS for network traffic. This is achieved by leveraging Azure Boost, which offloads virtualization processes to dedicated hardware, now extending RDMA capabilities to the guest operating system. This feature is particularly valuable for workloads requiring rapid data transfer, such as HPC (High Performance Computing), AI/ML training, and large-scale data analytics.

- Target audience affected  
This update is relevant for developers and IT professionals managing performance-sensitive workloads on Azure, especially those working with HPC, AI/ML, or distributed databases that benefit from RDMA networking.

- Important notes if any  
- The feature is currently in private preview and only available in the UK South region.
- Guest RDMA is supported on select VM sizes that are compatible with Azure Boost.
- Interested customers need to register for the private preview to gain access.
- Applications must be configured to use RDMA within the guest OS to realize performance benefits.
- For more details and registration, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=564981).

**Details**:

**Azure Update: Private Preview – Guest RDMA on Azure Boost**

**Background and Purpose of the Update**  
Remote Direct Memory Access (RDMA) is a technology that enables high-throughput, ultra-low latency networking by allowing direct memory access from the memory of one computer into that of another without involving either one's operating system. Traditionally, Azure has supported RDMA at the host level, primarily for specialized workloads such as high-performance computing (HPC). The purpose of this update is to extend RDMA capabilities directly into guest virtual machines (VMs) via Azure Boost, starting with the UK South region. This enhancement empowers applications running inside guest VMs to achieve superior networking performance, which is critical for data-intensive and latency-sensitive workloads.

**Specific Features and Detailed Changes**  
- **Guest RDMA Preview:** RDMA is now available within the guest operating system, not just at the host or infrastructure level.
- **Regional Availability:** The feature is initially available in the UK South region as a private preview.
- **Azure Boost Integration:** RDMA is enabled through Azure Boost, Azure’s platform for offloading and accelerating storage and networking operations.
- **Intra-Region Networking:** The feature supports high-throughput, low-latency networking between guest VMs within the same region.

**Technical Mechanisms and Implementation Methods**  
- **Azure Boost Enablement:** Azure Boost is leveraged to offload networking operations, allowing RDMA traffic to bypass the host OS and hypervisor layers. This direct path reduces overhead and latency, enabling near-native network performance for guest VMs.
- **Guest OS RDMA Stack:** With this update, the RDMA stack is exposed directly to the guest operating system, allowing applications to utilize RDMA verbs and APIs natively from within the VM.
- **Network Path Optimization:** By bypassing traditional network virtualization layers, the solution minimizes jitter and maximizes throughput, which is essential for HPC, AI, and other demanding workloads.

**Use Cases and Application Scenarios**  
- **High-Performance Computing (HPC):** Scientific simulations, computational fluid dynamics, and other HPC workloads that require rapid data exchange between compute nodes.
- **AI and Machine Learning:** Distributed training of machine learning models where low-latency communication between VMs accelerates convergence times.
- **Financial Services:** Real-time risk analysis and high-frequency trading platforms that demand minimal latency.
- **Big Data Analytics:** Scenarios where large datasets are processed in parallel across multiple VMs.

**Important Considerations and Limitations**  
- **Preview Status:** The feature is in private preview and only available in the UK South region. Access may be limited and subject to change.
- **Intra-Region Only:** RDMA support is currently limited to VMs within the same region; inter-region RDMA is not supported.
- **Guest OS Support:** Only guest operating systems with RDMA support can leverage this feature. Application compatibility with RDMA APIs is required.
- **Azure Boost Dependency:** RDMA enablement depends on Azure Boost, which may have its own prerequisites or supported VM families.

**Integration with Related Azure Services**  
- **Azure Virtual Machines:** Guest RDMA can be used with VMs that support Azure Boost.
- **Azure HPC Solutions:** Seamless integration with Azure’s HPC and AI services, enhancing performance for tightly-coupled workloads.
- **Azure Networking:** Works alongside existing Azure networking features, but with a focus on ultra-low latency and high throughput within the region.

**Summary:**  
Azure has introduced Guest RDMA in private preview via Azure Boost in the UK South region, enabling high-throughput, ultra-low latency networking directly within guest VMs for advanced workloads such as HPC and AI, with initial support for intra-region communication and integration with Azure’s acceleration platform.

---


*This report was automatically generated - 2026-06-06 03:01:20 UTC*