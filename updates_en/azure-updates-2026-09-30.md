# September 30, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 30, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 27 items

## Update List

### 1. Retirement: Azure Functions v1 hosting model on Azure Container Apps

**Published**: September 29, 2026 19:41:09 UTC
**Link**: [Retirement: Azure Functions v1 hosting model on Azure Container Apps](https://azure.microsoft.com/updates?id=570800)

**Update ID**: 570800
**Data source**: Azure Updates API

**Categories**: Containers, Azure Container Apps, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of the Azure Functions v1 hosting model on Azure Container Apps, effective September 29, 2027.

- Key changes or new features  
After the retirement date, Azure Functions v1 apps deployed on Azure Container Apps will stop running and will no longer process requests or event-driven triggers. There are no new features introduced; this is a deprecation notice.

- Target audience affected  
Developers and IT professionals who currently use Azure Functions v1 within Azure Container Apps are directly impacted. Teams maintaining legacy serverless workloads on this platform should take note.

- Important notes  
Existing Functions v1 apps will cease to operate after September 29, 2027. Microsoft recommends migrating to newer Azure Functions runtime versions (v4 or later) or alternative hosting models before the retirement date to ensure continued service availability. Planning and testing migrations early is advised to avoid service disruption.

For more information and migration guidance, refer to the official Azure update: https://azure.microsoft.com/updates?id=570800

**Details**:

**Azure Update Report: Retirement of Azure Functions v1 Hosting Model on Azure Container Apps**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of the Azure Functions v1 hosting model on Azure Container Apps, effective September 29, 2027. This update is part of Microsoft’s ongoing strategy to streamline and modernize its serverless offerings, ensuring customers leverage newer, more performant, and secure hosting models. The retirement aims to encourage migration to later versions of Azure Functions and to optimize the use of Azure Container Apps for scalable, event-driven workloads.

**Specific Features and Detailed Changes**  
The retirement specifically affects Azure Functions v1 applications hosted within Azure Container Apps. After the retirement date, any Functions v1 apps deployed to Azure Container Apps will cease operation; they will no longer process HTTP requests or event-driven triggers. No new deployments or executions of Functions v1 will be possible in this environment. The update does not affect other versions of Azure Functions (such as v2 or v3) or other hosting models (e.g., Consumption, Premium, or Dedicated plans).

**Technical Mechanisms and Implementation Methods**  
Azure Functions v1 is based on the .NET Framework and was originally designed for Windows-based environments. Azure Container Apps, however, is a modern container orchestration platform built on Kubernetes and optimized for Linux workloads and microservices architectures. The retirement is implemented by deprecating the runtime support for Functions v1 within the Container Apps platform, meaning the underlying infrastructure will no longer provision or execute v1 function containers. Existing v1 deployments will be stopped, and the platform will reject any new v1 deployments after the cutoff date.

**Use Cases and Application Scenarios**  
Historically, Azure Functions v1 on Container Apps was used for legacy .NET Framework-based serverless workloads that required containerized deployment, such as migrating older business logic or integrating with legacy systems. Typical scenarios included event-driven automation, backend processing, and API endpoints. With the retirement, customers are encouraged to migrate these workloads to newer Azure Functions versions (v2/v3/v4), which support .NET Core/.NET 6+ and are better aligned with containerized, cross-platform environments.

**Important Considerations and Limitations**  
- After September 29, 2027, Functions v1 apps on Container Apps will stop running and will not process any requests or triggers.
- There is no automatic migration; customers must manually upgrade their codebase to a supported Functions version and redeploy.
- The retirement does not affect Functions v1 hosted on other Azure platforms (e.g., App Service), but those platforms may have their own lifecycle policies.
- Applications relying on .NET Framework-specific features must be refactored for .NET Core/.NET 6+ compatibility before migration.
- Monitoring, alerting, and operational continuity must be reviewed to ensure no disruption after the retirement date.

**Integration with Related Azure Services**  
Azure Functions integrates with a wide range of Azure services, including Azure Event Grid, Azure Service Bus, Azure Storage, and Azure Logic Apps. The retirement of v1 hosting on Container Apps does not impact these integrations for newer Functions versions. Migrated workloads can continue to leverage these services, often with improved performance and security. Azure Container Apps remains a robust platform for hosting modern Functions workloads, microservices, and event-driven applications, supporting newer runtimes and frameworks.

**Summary Sentence**  
The Azure Functions v1 hosting model on Azure Container Apps will be retired on September 29, 2027, requiring customers to migrate legacy workloads to newer Functions versions to ensure continued operation and support.

---

### 2. Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series 

**Published**: September 29, 2026 19:27:09 UTC
**Link**: [Generally Available: Storage optimized Lasv5 and Laosv5 Azure VM series ](https://azure.microsoft.com/updates?id=572630)

**Update ID**: 572630
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Pricing & Offerings, Services

**Summary**:

- What was updated  
The Lasv5 and Laosv5 storage optimized Azure VM series, powered by 5th Gen AMD EPYC™ (Turin) processors, are now generally available.

- Key changes or new features  
These VM series offer a wide range of sizes (2–160 vCPUs), each providing 8 GiB memory and 720 GB local NVMe disk per vCPU. The storage optimization enables high-performance workloads requiring fast local disk access, such as databases, big data analytics, and caching solutions. The use of AMD EPYC™ Turin processors delivers improved compute and storage performance, energy efficiency, and scalability.

- Target audience affected  
Developers and IT professionals managing storage-intensive workloads, such as database administrators, big data engineers, and those deploying high-performance applications on Azure.

- Important notes if any  
The Lasv5 and Laosv5 VMs are ideal for workloads that demand high local storage throughput and low latency. When selecting VM sizes, consider the per-vCPU memory and NVMe disk allocations to optimize performance and cost. These VMs are now available in multiple Azure regions; check regional availability before deployment. For migration or scaling, review compatibility with existing workloads and storage requirements.

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
The release of the Lasv5 and Laosv5 Azure VM series marks the general availability of storage-optimized virtual machines built on the 5th Generation AMD EPYC™ processor (Turin). This update aims to provide customers with high-performance VM options specifically tuned for workloads requiring substantial local storage throughput and capacity, addressing the growing demand for scalable, storage-intensive compute resources in cloud environments.

**Specific Features and Detailed Changes:**  
- **VM Series:** Lasv5 and Laosv5 are new storage-optimized VM families.
- **Processor:** Both series utilize the 5th Gen AMD EPYC™ (Turin) CPUs, offering improved performance and efficiency compared to previous generations.
- **Size Range:** VMs are available in configurations from 2 to 160 vCPUs, enabling granular scaling for diverse workload requirements.
- **Memory:** Each vCPU is paired with 8 GiB of memory, ensuring balanced compute and memory resources.
- **Local Storage:** Each vCPU is provisioned with 720 GB of local NVMe disk capacity, delivering high-speed, low-latency storage directly attached to the VM for optimal throughput.

**Technical Mechanisms and Implementation Methods:**  
The Lasv5 and Laosv5 VM series leverage the advanced architecture of AMD EPYC™ Turin processors, which provide enhanced core density and memory bandwidth. NVMe local disks are physically attached to the host, offering direct access for the VM and minimizing storage latency. The allocation of NVMe storage per vCPU is fixed, ensuring predictable performance scaling as VM sizes increase. These VMs are provisioned through the Azure portal, CLI, or ARM templates, and integrate seamlessly into existing Azure deployment workflows.

**Use Cases and Application Scenarios:**  
- **High-Performance Databases:** Ideal for workloads such as NoSQL and relational databases that require fast local disk access and high IOPS.
- **Big Data Analytics:** Suitable for processing large datasets where local storage speed and capacity are critical, such as Hadoop or Spark clusters.
- **Cache and Temporary Storage:** Useful for applications needing high-speed temporary storage, such as caching layers or scratch space for scientific computing.
- **Data Processing Pipelines:** Beneficial for ETL workloads and batch processing tasks that rely on rapid local disk access.

**Important Considerations and Limitations:**  
- **Local Storage Persistence:** NVMe disks are local to the VM and are not persistent; data will be lost if the VM is deallocated or redeployed. Users must ensure critical data is backed up or replicated to persistent Azure storage services.
- **Scaling:** The fixed ratio of memory and NVMe storage per vCPU may require careful sizing to match workload requirements.
- **Availability:** The Lasv5 and Laosv5 series are generally available, but regional availability may vary. Users should verify availability in their target Azure regions.
- **Cost:** Storage-optimized VMs typically incur higher costs due to enhanced hardware resources; cost planning is recommended.

**Integration with Related Azure Services:**  
Lasv5 and Laosv5 VMs can be integrated with Azure managed services such as Azure Backup, Azure Site Recovery, and Azure Monitor for operational management. For persistent storage needs, users can combine these VMs with Azure Disk Storage or Azure Blob Storage. They are also compatible with Azure networking and security services, enabling deployment within Virtual Networks, use of Network Security Groups, and integration with Azure Active Directory.

**Summary Sentence:**  
The Lasv5 and Laosv5 Azure VM series, now generally available, provide storage-optimized compute options with up to 160 vCPUs, 8 GiB memory per vCPU, and 720 GB NVMe local disk per vCPU, leveraging 5th Gen AMD EPYC™ processors to deliver high-performance solutions for storage-intensive workloads.

---

### 3. Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets

**Published**: September 29, 2026 19:17:59 UTC
**Link**: [Public Preview: Automatic Zone Placement for Virtual Machine Scale Sets](https://azure.microsoft.com/updates?id=571075)

**Update ID**: 571075
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Virtual Machines, Features

**Summary**:

- What was updated  
Azure introduced Automatic Zone Placement for Virtual Machine Scale Sets in Public Preview.

- Key changes or new features  
This feature allows Azure to automatically assign the optimal availability zones for VM Scale Sets based on SKU availability, regional capacity, and placement constraints. Developers and IT professionals no longer need to manually specify or update zone lists for their scale sets. Azure handles zone selection dynamically, improving deployment reliability and scalability.

- Target audience affected  
Developers and IT professionals managing VM Scale Sets, especially those deploying workloads across multiple availability zones for high availability and resilience.

- Important notes  
Automatic Zone Placement is currently in Public Preview. Users should validate workloads and monitor performance during this phase. Manual zone selection is still available if specific placement is required. This feature simplifies zone management, reduces operational overhead, and helps ensure deployments utilize available resources efficiently.

For more details, visit: https://azure.microsoft.com/updates?id=571075

**Details**:

**Azure Update Report: Public Preview - Automatic Zone Placement for Virtual Machine Scale Sets**

**Background and Purpose of the Update**  
Azure Virtual Machine Scale Sets (VMSS) are widely used for deploying and managing large-scale VM clusters. Traditionally, IT professionals have been required to manually specify availability zones for VMSS deployments to ensure high availability and fault tolerance. This manual process can be complex, especially when considering SKU availability, regional capacity, and placement constraints. The purpose of this update is to simplify and optimize zone selection by introducing Automatic Zone Placement, allowing Azure to determine the most suitable availability zones for VMSS deployments.

**Specific Features and Detailed Changes**  
The Automatic Zone Placement feature, now in Public Preview, enables Azure to automatically select availability zones for VMSS based on real-time evaluation of SKU availability, regional capacity, and placement requirements. Users no longer need to maintain or update zone lists manually. When deploying a VMSS, Azure will dynamically allocate instances across the optimal zones, ensuring the best possible distribution for resilience and performance.

**Technical Mechanisms and Implementation Methods**  
Automatic Zone Placement leverages Azure’s internal algorithms and telemetry to assess the current state of availability zones within a region. The system evaluates SKU availability (whether the requested VM size is supported in each zone), checks for sufficient capacity, and considers placement requirements such as proximity and fault domain separation. When a VMSS is deployed with Automatic Zone Placement enabled, Azure orchestrates the placement of VMs across zones, abstracting the complexity from the user and ensuring compliance with best practices for high availability.

**Use Cases and Application Scenarios**  
This feature is particularly beneficial for organizations deploying large-scale, mission-critical applications that require high availability and disaster recovery. It is ideal for scenarios where VMSS are used to host web frontends, API services, or batch processing workloads, and where manual zone management would be cumbersome or error-prone. Automatic Zone Placement is also useful for teams that need to scale rapidly or operate in regions with fluctuating capacity, as it reduces operational overhead and risk of misconfiguration.

**Important Considerations and Limitations**  
As this feature is in Public Preview, it may not be available in all regions or for all VM SKUs. IT professionals should verify support for their specific workloads and regions before adopting Automatic Zone Placement. Additionally, reliance on Azure’s automated selection means users have less direct control over zone assignments, which may impact custom disaster recovery or compliance strategies. Monitoring and auditing zone placement should be incorporated into deployment workflows to ensure alignment with organizational policies.

**Integration with Related Azure Services**  
Automatic Zone Placement integrates seamlessly with VMSS and leverages Azure’s availability zone infrastructure. It can be used alongside other Azure services that depend on VMSS, such as Azure Load Balancer, Azure Application Gateway, and Azure Autoscale. The feature supports existing deployment pipelines and templates, allowing for straightforward adoption without significant changes to infrastructure-as-code or automation scripts.

**Summary Sentence**  
Automatic Zone Placement for Virtual Machine Scale Sets (Public Preview) streamlines VMSS deployments by enabling Azure to automatically select optimal availability zones based on SKU availability, capacity, and placement requirements, reducing manual overhead and enhancing high availability for mission-critical workloads.

---

### 4. Generally Available: Azure Arc-enabled SQL Server in Germany West Central

**Published**: September 29, 2026 19:07:44 UTC
**Link**: [Generally Available: Azure Arc-enabled SQL Server in Germany West Central](https://azure.microsoft.com/updates?id=570696)

**Update ID**: 570696
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
Azure Arc-enabled SQL Server is now generally available in the Germany West Central region.

- Key changes or new features  
SQL Server instances in Germany West Central can now be connected to Azure Arc. This enables centralized Azure-based inventory, governance, security, assessment, and license management for SQL Server, regardless of whether the servers are on-premises, in other clouds, or in Azure. Features include unified management, security policy enforcement, compliance assessments, and streamlined license tracking.

- Target audience affected  
Developers and IT professionals managing SQL Server workloads in Germany West Central, especially those seeking hybrid or multi-cloud management solutions.

- Important notes  
This update allows organizations in Germany West Central to leverage Azure Arc for enhanced visibility and control over their SQL Server infrastructure. It is particularly relevant for enterprises with compliance or data residency requirements in Germany. Existing SQL Server instances can be onboarded to Azure Arc without migration. For more details, see the official Azure Update announcement.

**Details**:

**Azure Arc-enabled SQL Server Now Generally Available in Germany West Central**

**Background and Purpose of the Update:**  
This update announces the general availability of Azure Arc-enabled SQL Server in the Germany West Central region. The primary purpose is to extend Azure’s management and governance capabilities to SQL Server instances running outside Azure, specifically for organizations with data residency or compliance requirements in Germany West Central. By connecting on-premises or multi-cloud SQL Server instances to Azure Arc, customers can leverage centralized Azure-based management tools while maintaining data locality.

**Specific Features and Detailed Changes:**  
With this release, organizations can now register their SQL Server instances located in Germany West Central with Azure Arc. Key features include:
- **Inventory Management:** Centralized visibility of all connected SQL Server instances within the Azure Portal.
- **Governance:** Application of Azure Policy for compliance and configuration management across hybrid environments.
- **Security:** Integration with Azure Security Center for unified security posture management and threat detection.
- **Assessment:** Access to Azure’s assessment tools for SQL Server health, configuration, and best practice recommendations.
- **License Management:** Streamlined tracking and management of SQL Server licenses via Azure, supporting compliance and cost optimization.

**Technical Mechanisms and Implementation Methods:**  
Azure Arc-enabled SQL Server operates by deploying a lightweight Azure Arc agent on the host machine where SQL Server is installed. This agent securely connects the SQL Server instance to Azure, enabling telemetry, policy enforcement, and management operations. All communication is encrypted, and data remains within the customer’s environment unless explicitly configured otherwise. The solution leverages Azure Resource Manager (ARM) to represent on-premises SQL Server instances as Azure resources, enabling seamless integration with Azure-native services and management workflows.

**Use Cases and Application Scenarios:**  
- **Regulated Industries:** Organizations in Germany with strict data residency requirements can manage SQL Server assets centrally without moving data to the cloud.
- **Hybrid and Multi-cloud Management:** Enterprises operating SQL Server workloads across on-premises, edge, and other cloud environments can standardize governance and security using Azure Arc.
- **License Optimization:** Businesses seeking to optimize SQL Server licensing and ensure compliance benefit from centralized license tracking and reporting.
- **Security and Compliance:** IT teams can enforce consistent security policies and monitor for vulnerabilities across all SQL Server instances, regardless of location.

**Important Considerations and Limitations:**  
- **Regional Availability:** This update specifically enables support in the Germany West Central region; organizations must ensure their workloads are within this geographic boundary to leverage the feature.
- **Agent Deployment:** The Azure Arc agent must be installed and maintained on each SQL Server host, which may require changes to existing operational processes.
- **Data Residency:** While management data is sent to Azure, customer data remains on-premises unless explicitly configured otherwise; however, organizations should review compliance requirements and Azure’s data handling policies.
- **Supported SQL Server Versions:** Only supported versions of SQL Server are eligible for Azure Arc integration; organizations should verify compatibility.

**Integration with Related Azure Services:**  
Azure Arc-enabled SQL Server integrates with core Azure services such as Azure Policy, Azure Security Center, and Azure Monitor. This enables unified policy enforcement, security monitoring, and operational insights across hybrid environments. Additionally, integration with Azure Resource Manager allows SQL Server instances to be managed alongside native Azure resources, streamlining operations and reporting.

**Summary:**  
Azure Arc-enabled SQL Server is now generally available in Germany West Central, providing organizations with the ability to connect SQL Server instances to Azure Arc and utilize Azure-based inventory, governance, security, assessment, and license management capabilities.

---

### 5. Generally Available: Azure Arc-enabled SQL Server Available in Italy North

**Published**: September 29, 2026 19:06:50 UTC
**Link**: [Generally Available: Azure Arc-enabled SQL Server Available in Italy North](https://azure.microsoft.com/updates?id=570763)

**Update ID**: 570763
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
Azure Arc-enabled SQL Server is now generally available in the Italy North region.

- Key changes or new features  
SQL Server instances in Italy North can now be connected to Azure Arc. This enables Azure-based inventory management, governance, security controls, assessments, and license management for SQL Server workloads running outside of Azure. Developers and IT professionals can leverage unified management and monitoring capabilities through Azure, regardless of where their SQL Server is deployed.

- Target audience affected  
This update impacts organizations running SQL Server workloads in Italy North, including IT administrators, database managers, and developers seeking hybrid or multi-cloud management solutions.

- Important notes if any  
Connecting SQL Server instances to Azure Arc allows for centralized control and compliance, streamlining operations for hybrid environments. Ensure your SQL Server version and infrastructure meet Azure Arc prerequisites before onboarding. For more details and guidance, refer to the official Azure documentation.

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Azure Arc-enabled SQL Server Available in Italy North

**Background and Purpose of the Update:**  
This update announces the general availability of Azure Arc-enabled SQL Server in the Italy North Azure region. The primary purpose is to extend Azure’s management and governance capabilities to on-premises and multi-cloud SQL Server instances located in or serving workloads from Italy North. By enabling Azure Arc for SQL Server in this region, Microsoft aims to provide organizations with unified management, enhanced security, and streamlined compliance for their SQL Server infrastructure, regardless of where it is hosted.

**Specific Features and Detailed Changes:**  
With this release, IT professionals can now connect their SQL Server instances—whether on-premises, in virtual machines, or in other clouds—to Azure Arc within the Italy North region. Key features include:
- **Azure-based Inventory:** Centralized visibility of all connected SQL Server instances through the Azure portal.
- **Governance:** Application of Azure Policy for consistent configuration and compliance across hybrid environments.
- **Security:** Integration with Azure Security Center for advanced threat protection and security recommendations.
- **Assessment:** Access to Azure’s assessment tools for evaluating SQL Server configurations and health.
- **License Management:** Simplified and centralized management of SQL Server licenses via Azure.

**Technical Mechanisms and Implementation Methods:**  
Azure Arc-enabled SQL Server works by installing the Azure Arc agent on the host machine where SQL Server is running. This agent securely connects the instance to Azure, registering it as a resource within the Azure Resource Manager (ARM) framework. Once connected, the SQL Server instance can be managed, monitored, and governed using native Azure services. Communication between the on-premises environment and Azure is secured using encrypted channels, and all management operations are performed through the Azure portal or ARM APIs.

**Use Cases and Application Scenarios:**  
- **Hybrid Cloud Management:** Organizations with SQL Server workloads spread across on-premises datacenters, Azure, and other clouds can manage all instances from a single pane of glass.
- **Regulatory Compliance:** Enterprises in Italy North can ensure compliance with local data residency and governance requirements while leveraging Azure’s policy and security features.
- **Security Operations:** Security teams can monitor, assess, and respond to threats across their SQL Server estate using Azure Security Center.
- **License Optimization:** Centralized license management helps optimize costs and ensure compliance with Microsoft licensing terms.

**Important Considerations and Limitations:**  
- This update is specific to the Italy North region; organizations with workloads in other regions should verify availability accordingly.
- The solution requires installation and configuration of the Azure Arc agent on each SQL Server host.
- Only the features explicitly mentioned (inventory, governance, security, assessment, license management) are guaranteed; additional Azure Arc features may require separate validation.
- Network connectivity between the SQL Server hosts and Azure is required for ongoing management and monitoring.

**Integration with Related Azure Services:**  
Azure Arc-enabled SQL Server integrates with several Azure services, including:
- **Azure Policy:** For governance and compliance management.
- **Azure Security Center:** For unified security management and threat protection.
- **Azure Monitor:** For centralized monitoring and alerting (if configured).
- **Azure Resource Manager:** For resource organization and role-based access control.

**Summary:**  
Azure Arc-enabled SQL Server is now generally available in Italy North, providing organizations with unified Azure-based management, governance, security, assessment, and license management for their SQL Server instances across hybrid and multi-cloud environments.

---

### 6. Public Preview: Azure Database for PostgreSQL Ultra Disk 

**Published**: September 29, 2026 18:14:46 UTC
**Link**: [Public Preview: Azure Database for PostgreSQL Ultra Disk ](https://azure.microsoft.com/updates?id=571909)

**Update ID**: 571909
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

**What was updated:**  
Azure Database for PostgreSQL Flexible Server now supports Ultra Disk in public preview.

**Key changes or new features:**  
- Ultra Disk, Azure’s highest-performance managed disk, is available for PostgreSQL flexible server.
- Designed for I/O-intensive and transaction-heavy workloads, Ultra Disk offers consistently low latency and high throughput.
- Developers and IT professionals can now provision PostgreSQL servers with Ultra Disk to optimize performance for demanding database applications.

**Target audience affected:**  
- Developers building high-performance, data-intensive applications on PostgreSQL.
- IT professionals and database administrators managing large-scale or mission-critical PostgreSQL workloads in Azure.

**Important notes:**  
- Ultra Disk support is currently in public preview; production use should be evaluated carefully.
- Ultra Disk can help reduce performance bottlenecks for workloads requiring high IOPS and low latency.
- Pricing and regional availability may vary; check Azure documentation for details.

[Read more](https://azure.microsoft.com/updates?id=571909)

**Details**:

**Azure Update Report: Public Preview – Azure Database for PostgreSQL Ultra Disk**

**Background and Purpose of the Update:**  
Azure Database for PostgreSQL flexible server now supports Ultra Disk in public preview. This update addresses the need for high-performance, low-latency storage for PostgreSQL workloads that are I/O-intensive and transaction-heavy. The purpose is to enable customers to leverage Azure’s highest-performance managed disk option, thereby improving throughput and consistency for demanding database operations.

**Specific Features and Detailed Changes:**  
Ultra Disk support introduces the ability to provision Ultra Disk as the storage backend for PostgreSQL flexible server instances. Ultra Disk offers configurable performance parameters, including IOPS (Input/Output Operations Per Second), throughput, and disk size, allowing precise tailoring to workload requirements. This is a significant change from previous disk options, such as Premium or Standard SSD, which have fixed performance profiles. With Ultra Disk, users can achieve consistently low latency and higher throughput, which is critical for workloads with frequent and intensive data access patterns.

**Technical Mechanisms and Implementation Methods:**  
Ultra Disk is implemented as a managed disk resource within Azure, designed for high-end performance scenarios. When configuring a PostgreSQL flexible server, users can select Ultra Disk as the storage type. The disk’s performance characteristics (IOPS and throughput) can be adjusted independently of disk size, providing granular control. Azure manages the provisioning, scaling, and maintenance of the Ultra Disk, ensuring high availability and durability. Integration with the flexible server architecture allows seamless attachment and management of Ultra Disk resources, leveraging Azure’s underlying storage infrastructure.

**Use Cases and Application Scenarios:**  
Ultra Disk is ideal for PostgreSQL workloads with high transaction rates, such as financial systems, real-time analytics, and mission-critical applications requiring consistent performance. Typical scenarios include OLTP (Online Transaction Processing), large-scale data ingestion, and workloads with unpredictable or spiky I/O patterns. Organizations seeking to minimize latency and maximize throughput for their PostgreSQL databases will benefit from this update, especially when running performance-sensitive applications.

**Important Considerations and Limitations:**  
As Ultra Disk support is currently in public preview, it may not be suitable for production workloads requiring full SLA guarantees. Users should evaluate performance and stability in their test environments before adoption. Ultra Disk may incur higher costs compared to other managed disk types due to its premium performance characteristics. Compatibility with existing backup, restore, and scaling operations should be verified, and users should consult Azure documentation for region availability and any preview-specific limitations.

**Integration with Related Azure Services:**  
Ultra Disk integrates with Azure Database for PostgreSQL flexible server, leveraging Azure’s managed disk infrastructure. It can be used alongside other Azure services, such as Azure Backup, Azure Monitor, and Azure Security Center, for comprehensive management, monitoring, and protection. The flexible server model allows for easy scaling and configuration changes, ensuring that Ultra Disk can be adopted without disrupting existing workflows.

**Summary Sentence:**  
Azure Database for PostgreSQL flexible server now supports Ultra Disk in public preview, enabling I/O-intensive and transaction-heavy workloads to leverage Azure’s highest-performance managed disk option for consistently low latency and high throughput.

---

### 7. Public Preview: SQL Performance Monitoring for Azure SQL Database

**Published**: September 29, 2026 18:13:31 UTC
**Link**: [Public Preview: SQL Performance Monitoring for Azure SQL Database](https://azure.microsoft.com/updates?id=571867)

**Update ID**: 571867
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Microsoft has released the public preview of SQL Performance Monitoring for Azure SQL Database, offering a built-in, Microsoft-managed solution for monitoring database performance.

- Key changes or new features  
This update introduces integrated performance monitoring, eliminating the need for custom scripts or manual telemetry correlation across multiple tools. The solution provides consolidated data collection, visualization, and analysis directly within the Azure portal. Developers and IT professionals can now access performance metrics, detect issues, and analyze trends more efficiently using native Azure capabilities.

- Target audience affected  
The update is relevant to developers, database administrators, and IT professionals who manage or develop applications using Azure SQL Database. It simplifies performance monitoring workflows and reduces operational overhead.

- Important notes if any  
This feature is currently in public preview, so it may not be suitable for production workloads. Users are encouraged to test and provide feedback. The monitoring solution is Microsoft-managed, ensuring consistent updates and support. No additional setup or custom integration is required; monitoring is accessible directly in the Azure portal. For more details, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=571867

**Details**:

**Azure Update Report**

**Title:** Public Preview: SQL Performance Monitoring for Azure SQL Database  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=571867)

---

**Background and Purpose of the Update:**  
Microsoft has introduced a public preview of performance monitoring for Azure SQL Database that is managed directly by Microsoft. The primary purpose of this update is to simplify the monitoring process for Azure SQL Database users by eliminating the need for custom collection scripts and manual correlation of telemetry across disparate tools. This enhancement aims to provide a unified, built-in monitoring experience, improving operational efficiency and reducing the complexity associated with database performance diagnostics.

---

**Specific Features and Detailed Changes:**  
- **Built-in Performance Monitoring:** Azure SQL Database now offers native performance monitoring capabilities managed by Microsoft, available directly within the platform.
- **No Custom Scripts Required:** Users can monitor database performance without developing or maintaining custom telemetry collection scripts.
- **Unified Data Collection:** The monitoring solution consolidates performance data, removing the need to manually correlate metrics from disconnected sources.
- **Microsoft-Managed Solution:** The monitoring infrastructure is provisioned and maintained by Microsoft, ensuring reliability and consistency.

---

**Technical Mechanisms and Implementation Methods:**  
- **Integrated Telemetry Collection:** Performance data is collected natively by the Azure SQL Database service, leveraging Microsoft’s internal telemetry mechanisms.
- **Centralized Monitoring Interface:** The collected data is accessible through built-in Azure tools, streamlining access and visualization.
- **Automated Data Correlation:** The system automatically correlates relevant performance metrics, reducing manual effort and potential errors.
- **Public Preview Availability:** The feature is currently in public preview, allowing users to evaluate its functionality and provide feedback.

---

**Use Cases and Application Scenarios:**  
- **Operational Monitoring:** IT teams can use the built-in monitoring to track database health, identify performance bottlenecks, and optimize resource utilization.
- **Troubleshooting and Diagnostics:** The unified telemetry enables faster root cause analysis for performance issues, supporting quicker resolution.
- **Performance Tuning:** Database administrators can leverage the collected metrics to make informed decisions about scaling, indexing, and query optimization.
- **Compliance and Reporting:** Organizations can utilize the monitoring data for compliance audits and performance reporting without additional tooling.

---

**Important Considerations and Limitations:**  
- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads requiring full support or guaranteed stability.
- **Feature Scope:** The update focuses on performance monitoring; other aspects such as security or backup monitoring are not addressed.
- **Integration Constraints:** Users should verify compatibility with existing monitoring workflows and tools, as the preview may have limitations in extensibility or export capabilities.
- **Feedback Opportunity:** Organizations are encouraged to test the feature and provide feedback to Microsoft for future enhancements.

---

**Integration with Related Azure Services:**  
- **Azure SQL Database:** The monitoring is tightly integrated with Azure SQL Database, leveraging its native telemetry.
- **Azure Portal:** Users can access performance metrics and monitoring dashboards directly through the Azure Portal, ensuring seamless integration with existing Azure management workflows.
- **Potential for Integration:** While not explicitly stated, the built-in monitoring may complement other Azure services such as Azure Monitor, though users should confirm integration details during the preview phase.

---

**Summary Sentence:**  
The public preview of Microsoft-managed performance monitoring for Azure SQL Database offers IT professionals a streamlined, built-in solution for tracking and diagnosing database performance without custom scripts, enhancing operational efficiency and simplifying telemetry management.

---

### 8. Public Preview: Performance monitoring for Azure Arc–enabled SQL Server 

**Published**: September 29, 2026 18:11:15 UTC
**Link**: [Public Preview: Performance monitoring for Azure Arc–enabled SQL Server ](https://azure.microsoft.com/updates?id=571904)

**Update ID**: 571904
**Data source**: Azure Updates API

**Categories**: In preview, Hybrid + multicloud, Azure Arc, Feature

**Summary**:

- What was updated  
Azure Arc–enabled SQL Server now offers expanded performance monitoring capabilities in public preview.

- Key changes or new features  
The update introduces more flexible options for exploring and visualizing SQL Server performance data. Developers and IT professionals can now directly query Microsoft-managed monitoring data via a telemetry endpoint, enabling custom analysis and integration with other tools. The built-in monitoring experience is enhanced, providing deeper insights into server performance and resource utilization.

- Target audience affected  
This update primarily impacts developers, database administrators, and IT professionals managing SQL Server instances through Azure Arc. It is especially relevant for those seeking advanced monitoring, troubleshooting, and optimization capabilities across hybrid and multi-cloud environments.

- Important notes  
The feature is currently in public preview, so production use should be approached with caution. Integration with the telemetry endpoint allows for more granular access to performance metrics, supporting custom dashboards and alerting scenarios. Users should review documentation for endpoint access and security considerations.

**Details**:

**Azure Update Report: Public Preview – Performance Monitoring for Azure Arc–enabled SQL Server**

**Background and Purpose of the Update**  
This update introduces a public preview for enhanced performance monitoring capabilities for SQL Server instances enabled by Azure Arc. Azure Arc allows organizations to extend Azure management and governance to on-premises, multi-cloud, and edge environments. The purpose of this update is to provide IT professionals with more flexible and comprehensive tools to monitor SQL Server performance, regardless of where the server is deployed, thereby improving operational visibility and troubleshooting efficiency.

**Specific Features and Detailed Changes**  
- **Expanded Performance Monitoring:** The preview expands performance monitoring options for Azure Arc–enabled SQL Server, allowing users to explore and visualize performance data with greater flexibility.
- **Direct Data Querying:** IT professionals can now query Microsoft-managed monitoring data directly through a telemetry endpoint. This enables more granular access to performance metrics without relying solely on pre-built dashboards.
- **Built-in Visualization Tools:** The update includes built-in tools for visualizing performance data, making it easier to interpret key metrics and trends.

**Technical Mechanisms and Implementation Methods**  
- **Telemetry Endpoint:** The core mechanism is a Microsoft-managed telemetry endpoint, which aggregates and exposes performance data collected from Azure Arc–enabled SQL Server instances. This endpoint can be queried directly, allowing integration with custom monitoring solutions or advanced analytics platforms.
- **Data Collection:** Performance metrics are collected from SQL Server instances via Azure Arc agents, which securely transmit telemetry to Azure for centralized monitoring and analysis.
- **Visualization:** Built-in visualization capabilities are provided within the Azure portal or other supported interfaces, enabling users to interactively explore performance data.

**Use Cases and Application Scenarios**  
- **Hybrid and Multi-Cloud Monitoring:** Organizations running SQL Server across on-premises, edge, and multi-cloud environments can leverage this feature to unify performance monitoring under Azure’s management umbrella.
- **Custom Reporting and Analytics:** IT teams can query telemetry data directly for integration with custom reporting tools or to perform advanced analytics, supporting proactive performance management and troubleshooting.
- **Operational Insights:** Enhanced visualization tools help DBAs and IT professionals quickly identify performance bottlenecks, optimize resource allocation, and maintain high availability.

**Important Considerations and Limitations**  
- **Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes or limitations in functionality.
- **Data Privacy and Security:** As telemetry data is transmitted to Microsoft-managed endpoints, organizations should review compliance and data privacy requirements to ensure alignment with internal policies.
- **Integration Requirements:** Azure Arc agents must be properly deployed and configured on SQL Server instances to enable telemetry collection and monitoring.

**Integration with Related Azure Services**  
- **Azure Arc:** This update builds on Azure Arc’s capabilities to manage and monitor hybrid SQL Server environments.
- **Azure Monitor:** The telemetry endpoint and visualization tools may integrate with Azure Monitor, allowing for consolidated alerting and dashboarding across cloud and hybrid resources.
- **Custom Analytics Solutions:** Direct querying of telemetry data facilitates integration with third-party analytics and reporting platforms.

**Summary Sentence**  
The public preview of performance monitoring for Azure Arc–enabled SQL Server introduces flexible querying and visualization of Microsoft-managed telemetry data, empowering IT professionals to gain deeper operational insights across hybrid environments.

---

### 9. Generally Available: Azure SQL updates for late-September 2026

**Published**: September 29, 2026 18:05:11 UTC
**Link**: [Generally Available: Azure SQL updates for late-September 2026](https://azure.microsoft.com/updates?id=571643)

**Update ID**: 571643
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Azure SQL Database Hyperscale Premium series received new compute options.

- Key changes or new features  
Two new high-performance compute tiers—160-vCore and 192-vCore—are now generally available. These tiers offer up to 50% greater compute capacity compared to previous maximums, enabling support for larger and more demanding workloads in Azure SQL Database Hyperscale.

- Target audience affected  
Developers and IT professionals managing large-scale, mission-critical applications or databases in Azure SQL Database Hyperscale. Teams requiring increased compute resources for performance-intensive workloads will benefit most.

- Important notes  
These new vCore options are intended for scenarios where scaling compute is critical, such as high-volume transaction processing, advanced analytics, or complex data processing. Consider reviewing pricing and resource allocation to optimize for cost and performance. Existing workloads can be scaled up to these new tiers with minimal downtime. For more information, refer to the official Azure documentation and update page.

**Details**:

**Azure Update Report: Azure SQL Updates for Late-September 2026**

**Background and Purpose of the Update**  
Azure SQL Database continues to evolve to meet the demands of enterprise-scale workloads and high-performance applications. The late-September 2026 update focuses on expanding the scalability of Azure SQL Database Hyperscale Premium series, specifically targeting organizations that require substantial compute resources for their database operations. The purpose of this update is to enable larger workloads and improve performance, ensuring Azure SQL remains a robust platform for mission-critical applications.

**Specific Features and Detailed Changes**  
The update introduces new compute options for Azure SQL Database Hyperscale Premium series:  
- **160-vCore and 192-vCore configurations**  
These new options provide up to 50% greater compute capacity compared to previous offerings. This enhancement allows customers to provision databases with significantly more CPU resources, supporting larger concurrent workloads and more intensive data processing tasks.

**Technical Mechanisms and Implementation Methods**  
The Hyperscale architecture in Azure SQL Database is designed to separate compute, storage, and log components, enabling elastic scaling and high availability. With the introduction of 160-vCore and 192-vCore options, the platform leverages Azure’s underlying virtual machine infrastructure to allocate more CPU cores to database compute nodes.  
- **Provisioning**: Customers can select the new vCore sizes during database creation or scale-up operations via the Azure Portal, CLI, PowerShell, or ARM templates.
- **Performance**: The increased vCore count directly translates to higher parallelism, improved query throughput, and better support for CPU-intensive operations such as analytics, batch processing, and complex transactions.

**Use Cases and Application Scenarios**  
These enhancements are particularly beneficial for:  
- **Enterprise applications** with high transaction volumes or complex queries.
- **Data warehousing and analytics workloads** that require substantial compute power for ETL, reporting, and real-time analytics.
- **Multi-tenant SaaS platforms** where resource isolation and performance guarantees are critical.
- **Migration scenarios** where legacy on-premises databases with large compute footprints are moved to Azure SQL Hyperscale.

**Important Considerations and Limitations**  
- **Cost**: Higher vCore configurations will incur increased compute charges. Organizations should assess workload requirements and optimize resource allocation to balance performance and cost.
- **Resource limits**: While compute capacity is increased, other resource limits (such as storage or IOPS) should be reviewed to ensure they align with the new vCore sizes.
- **Compatibility**: Not all workloads may benefit from increased vCores; performance tuning and workload profiling are recommended to maximize ROI.
- **Scaling**: Scaling up to 160 or 192 vCores may require downtime or brief service interruptions, depending on the current configuration and workload.

**Integration with Related Azure Services**  
Azure SQL Database Hyperscale Premium series integrates seamlessly with other Azure services:  
- **Azure Monitor and Azure Advisor**: For performance monitoring, cost analysis, and optimization recommendations.
- **Azure Data Factory and Azure Synapse Analytics**: For orchestrating data movement and analytics workloads.
- **Azure Active Directory**: For secure authentication and access control.
- **Azure Backup and Disaster Recovery**: For data protection and business continuity.

**Summary Sentence**  
Azure SQL Database Hyperscale Premium series now offers 160-vCore and 192-vCore compute options, delivering up to 50% greater capacity for large-scale workloads, enabling higher performance and scalability for enterprise applications and data-intensive scenarios.

---

### 10. Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK) 

**Published**: September 29, 2026 17:57:36 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK) ](https://azure.microsoft.com/updates?id=571783)

**Update ID**: 571783
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now supports cross-tenant customer-managed keys (CMK) for data encryption.

- Key changes or new features  
You can encrypt PostgreSQL Flexible Server data using keys stored in Azure Key Vault or Azure Managed HSM located in a different Microsoft Entra tenant than your PostgreSQL server. This enables organizations to manage encryption keys separately from their database resources, supporting scenarios like centralized key management across multiple tenants or subsidiaries.

- Target audience affected  
Developers and IT professionals responsible for database security, compliance, and key management in multi-tenant or complex organizational environments. This is especially relevant for enterprises with multiple Microsoft Entra tenants or those needing strict separation of duties.

- Important notes  
To use cross-tenant CMK, you must configure access policies and permissions between tenants for Azure Key Vault or Managed HSM. This feature enhances security and compliance options, allowing greater flexibility in key management. Ensure your organization’s processes support cross-tenant resource access and review documentation for setup details and best practices.

For more information, see the official Azure Update: https://azure.microsoft.com/updates?id=571783

**Details**:

**Azure Update Report: Generally Available – Azure Database for PostgreSQL Flexible Server supports cross-tenant customer-managed keys (CMK)**  
[Reference: Azure Update Link](https://azure.microsoft.com/updates?id=571783)

---

### Background and Purpose of the Update

Azure Database for PostgreSQL Flexible Server previously supported encryption at rest using customer-managed keys (CMK) stored in Azure Key Vault or Azure Managed HSM. However, the key vault or managed HSM had to reside in the same Microsoft Entra tenant as the PostgreSQL Flexible Server instance. This update introduces support for cross-tenant CMK, enabling organizations to use encryption keys stored in a different Microsoft Entra tenant than the one hosting their PostgreSQL Flexible Server. The purpose is to address scenarios where key management and database resources are intentionally separated across tenants for security, compliance, or organizational reasons.

---

### Specific Features and Detailed Changes

- **Cross-Tenant CMK Support:**  
  PostgreSQL Flexible Server instances can now be configured to use customer-managed keys stored in an Azure Key Vault or Azure Managed HSM located in a different Microsoft Entra tenant.
- **Encryption at Rest:**  
  Data at rest in the PostgreSQL Flexible Server is encrypted using the specified CMK, regardless of the tenant in which the key is managed.
- **Key Storage Options:**  
  Both Azure Key Vault and Azure Managed HSM are supported as key storage backends for cross-tenant scenarios.

---

### Technical Mechanisms and Implementation Methods

- **Key Reference:**  
  When configuring encryption, you provide the URI of the key in the Azure Key Vault or Managed HSM, including the tenant context.
- **Access Control:**  
  The PostgreSQL Flexible Server’s managed identity (system-assigned or user-assigned) must be granted appropriate permissions (e.g., `get`, `unwrapKey`, `wrapKey`) on the key in the external tenant’s Key Vault or HSM.
- **Tenant Trust:**  
  Cross-tenant access requires explicit trust and permission configuration between the two Microsoft Entra tenants, ensuring that only authorized managed identities can access the CMK.
- **Encryption Lifecycle:**  
  All encryption and decryption operations for data at rest are performed using the CMK, with Azure handling key retrieval and cryptographic operations securely across tenants.

---

### Use Cases and Application Scenarios

- **Centralized Key Management:**  
  Enterprises with centralized security teams can manage all encryption keys in a dedicated tenant, while application workloads run in separate tenants.
- **Mergers and Acquisitions:**  
  Organizations undergoing mergers can maintain existing key management practices while migrating or integrating PostgreSQL Flexible Server resources across tenants.
- **Regulatory Compliance:**  
  Scenarios requiring strict separation of duties or key management by a third party (e.g., managed security service providers) can leverage cross-tenant CMK.

---

### Important Considerations and Limitations

- **Permissions:**  
  Proper configuration of access policies and permissions is critical. The managed identity of the PostgreSQL Flexible Server must have the necessary rights on the key in the external tenant.
- **Key Rotation:**  
  Key rotation processes must account for cross-tenant dependencies and ensure continued access for the database server.
- **Network and Security:**  
  Network access to the Key Vault or Managed HSM must be configured to allow secure communication from the PostgreSQL Flexible Server’s tenant.
- **Service Limits:**  
  Review Azure documentation for any service-specific limitations or quotas related to cross-tenant key usage.

---

### Integration with Related Azure Services

- **Azure Key Vault & Azure Managed HSM:**  
  Both services are supported as key repositories, providing flexibility in key management strategies.
- **Microsoft Entra ID (formerly Azure AD):**  
  Cross-tenant access relies on Entra ID for identity and access management, requiring careful configuration of trust relationships and permissions.
- **Azure Resource Manager (ARM):**  
  Resource deployment and

---

### 11. Public preview: Script-based deployment for SQL Server on Linux Azure VM 

**Published**: September 29, 2026 17:52:59 UTC
**Link**: [Public preview: Script-based deployment for SQL Server on Linux Azure VM ](https://azure.microsoft.com/updates?id=571810)

**Update ID**: 571810
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Databases, SQL Server on Azure Virtual Machines, Feature

**Summary**:

- What was updated  
Azure has introduced a public preview of script-based deployment for SQL Server on Linux Azure Virtual Machines, replacing the previous marketplace image-based approach.

- Key changes or new features  
The new deployment method uses automated scripts to provision SQL Server on Linux VMs. This enables greater flexibility and customization during installation, allowing users to tailor configurations to their specific requirements. Management is simplified, and the deployment process is more streamlined compared to legacy marketplace images. The script-based approach also supports automation scenarios, making it easier to integrate SQL Server deployments into CI/CD pipelines or infrastructure-as-code workflows.

- Target audience affected  
Developers and IT professionals who deploy and manage SQL Server on Linux Azure VMs, especially those requiring custom configurations or automated deployments.

- Important notes  
The legacy SQL Server on Linux marketplace images will be phased out in favor of this script-based provisioning. Users should begin adopting the new method to benefit from enhanced flexibility and automation. During the public preview, feedback is encouraged to help improve the deployment experience. Existing workloads on marketplace images are not immediately affected, but planning for migration is recommended.  

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=571810

**Details**:

**Azure Update Report: Public Preview – Script-based Deployment for SQL Server on Linux Azure VM**

**Background and Purpose of the Update**  
The update introduces a new deployment experience for SQL Server on Linux Azure Virtual Machines (VMs), moving away from legacy marketplace images. The primary purpose is to modernize and streamline the provisioning process, offering IT professionals greater flexibility, simplified management, and improved customization capabilities compared to the previous image-based approach.

**Specific Features and Detailed Changes**  
- **Automated Script-based Provisioning:** Deployment is now handled via scripts rather than pre-configured marketplace images. This allows for dynamic configuration during the VM setup process.
- **Enhanced Customization:** Users can tailor the SQL Server installation parameters, including version selection, configuration options, and post-deployment settings, directly within the script.
- **Simplified Management:** The script-based approach reduces complexity by automating repetitive tasks and enabling easier updates or modifications to the SQL Server environment.
- **Legacy Image Replacement:** Marketplace images, which previously provided a fixed, pre-installed SQL Server environment, are deprecated in favor of this more flexible and maintainable method.

**Technical Mechanisms and Implementation Methods**  
- **Script Execution:** Provisioning scripts are executed during VM deployment, either as part of the Azure Resource Manager (ARM) template or through custom deployment pipelines.
- **Automation Integration:** Scripts can be integrated with Azure automation tools, such as Azure CLI, PowerShell, or DevOps pipelines, to facilitate repeatable and consistent deployments.
- **Configuration Management:** Scripts can include logic for environment-specific configuration, such as networking, storage, authentication, and SQL Server settings, ensuring deployments meet organizational standards.

**Use Cases and Application Scenarios**  
- **Custom SQL Server Deployments:** Organizations requiring specific SQL Server configurations (e.g., tuning, extensions, or integration with other services) benefit from script-based deployment.
- **DevOps and CI/CD Pipelines:** Automated script-based provisioning fits seamlessly into continuous integration and deployment workflows, supporting rapid and consistent environment creation.
- **Migration and Modernization Projects:** Teams migrating from legacy SQL Server instances or modernizing their infrastructure can leverage scripts for tailored deployments and easier transition management.
- **Multi-environment Management:** IT professionals managing multiple environments (development, staging, production) can use scripts to ensure consistent SQL Server setups across all VMs.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate stability and support before widespread adoption.
- **Deprecation of Marketplace Images:** Existing workflows based on marketplace images will need to be updated to utilize script-based provisioning.
- **Script Maintenance:** Organizations must maintain and update their deployment scripts to ensure compatibility with future SQL Server and Azure VM changes.
- **Security and Compliance:** Scripts must be reviewed for security best practices, especially regarding credentials, network configuration, and compliance requirements.

**Integration with Related Azure Services**  
- **Azure Resource Manager (ARM):** Script-based deployment can be incorporated into ARM templates for infrastructure-as-code scenarios.
- **Azure Automation and DevOps:** Integration with Azure DevOps, Azure CLI, and PowerShell enables automated, repeatable deployments and management.
- **Azure Monitoring and Management Tools:** Scripts can be extended to configure monitoring, backup, and other management features during SQL Server setup.

**Summary Sentence**  
The public preview of script-based deployment for SQL Server on Linux Azure VMs replaces legacy marketplace images with an automated, flexible, and customizable provisioning experience, streamlining management and enabling advanced integration with Azure automation and DevOps workflows.

---

### 12. Generally Available: SQL Server on Azure Local Disconnected (ALDO) 

**Published**: September 29, 2026 17:51:34 UTC
**Link**: [Generally Available: SQL Server on Azure Local Disconnected (ALDO) ](https://azure.microsoft.com/updates?id=571836)

**Update ID**: 571836
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
SQL Server on Azure Local Disconnected (ALDO) is now generally available.

- Key changes or new features  
ALDO enables SQL Server workloads to run in environments without continuous internet connectivity to Azure. This feature is specifically designed for highly regulated, secure, remote, or air-gapped locations. It allows organizations to benefit from Azure capabilities while maintaining local control and compliance, supporting disconnected operations and periodic synchronization with Azure when connectivity is available.

- Target audience affected  
IT professionals managing infrastructure in secure, regulated, or remote environments; developers deploying SQL Server solutions where internet access is restricted or intermittent; organizations requiring compliance with strict data residency or security policies.

- Important notes  
ALDO is ideal for scenarios where Azure-connected services are not feasible due to connectivity constraints. It supports periodic updates and synchronization with Azure, but does not require always-on connectivity. This update expands SQL Server deployment options for customers with unique operational or regulatory requirements. For more details, visit the official Azure Update announcement: https://azure.microsoft.com/updates?id=571836

**Details**:

**Azure Update Report: SQL Server on Azure Local Disconnected (ALDO) – General Availability**

**Background and Purpose of the Update**  
The general availability of SQL Server on Azure Local Disconnected (ALDO) addresses the need for SQL Server deployments in environments where continuous connectivity to Azure is not feasible. This update is specifically targeted at highly regulated, secure, remote, or air-gapped environments, such as government, defense, industrial, and isolated data centers, where internet access is restricted or unavailable. The purpose is to extend the benefits of Azure-managed SQL Server to these disconnected scenarios, ensuring organizations can leverage Azure capabilities without compromising compliance or operational requirements.

**Specific Features and Detailed Changes**  
ALDO introduces a deployment model for SQL Server that operates independently from Azure’s cloud connectivity. Key features include:

- **Disconnected Operations:** SQL Server instances can be provisioned, managed, and operated locally without requiring persistent internet connectivity to Azure.
- **Extended Support:** Enables organizations to receive support and updates for SQL Server in environments that cannot maintain a continuous connection to Azure.
- **Compliance and Security:** Designed to meet the stringent requirements of regulated and secure environments, supporting operations in air-gapped networks.

**Technical Mechanisms and Implementation Methods**  
ALDO leverages local deployment and management mechanisms to enable SQL Server functionality in disconnected environments. Technical implementation involves:

- **Local Provisioning:** SQL Server is installed and configured on-premises or in local infrastructure, with management tools adapted for offline use.
- **Update and Support Workflow:** Updates and support are facilitated through mechanisms that do not require constant Azure connectivity, possibly using periodic or manual synchronization when connectivity is available.
- **Isolation:** The deployment is architected to ensure that all operations, including data processing and management, remain within the local environment, adhering to isolation requirements.

**Use Cases and Application Scenarios**  
ALDO is suitable for scenarios where data sovereignty, security, and regulatory compliance necessitate isolation from public cloud infrastructure. Typical use cases include:

- **Government and Defense:** Secure facilities with strict air-gap policies.
- **Industrial and Manufacturing:** Remote plants or sites with limited or no internet access.
- **Healthcare and Research:** Environments handling sensitive data under regulatory constraints.
- **Disaster Recovery and Edge Deployments:** Locations where intermittent connectivity is expected.

**Important Considerations and Limitations**  
When utilizing ALDO, IT professionals should consider:

- **Connectivity Constraints:** ALDO is intended for environments with restricted or no internet access; features dependent on real-time Azure connectivity may be unavailable.
- **Update Management:** Updates and patches may require manual intervention or scheduled connectivity windows.
- **Integration Limitations:** Some Azure-native features, such as cloud-based analytics or automated scaling, may not be fully supported in disconnected mode.

**Integration with Related Azure Services**  
ALDO is designed to extend SQL Server support to disconnected environments, but integration with other Azure services is limited by connectivity constraints. Where possible, synchronization or integration with Azure services can be performed during scheduled connectivity periods or via manual processes. The primary focus is on maintaining local operations while enabling Azure-level support and management.

**Summary Sentence**  
SQL Server on Azure Local Disconnected (ALDO) is now generally available, enabling secure, compliant, and fully supported SQL Server deployments in environments with restricted or no internet connectivity to Azure.

---

### 13. Generally Available: SQL Server support on Azure Local connected mode 

**Published**: September 29, 2026 17:50:20 UTC
**Link**: [Generally Available: SQL Server support on Azure Local connected mode ](https://azure.microsoft.com/updates?id=571841)

**Update ID**: 571841
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
SQL Server support is now generally available on Azure Local in connected mode.

- Key changes or new features  
Developers and IT professionals can now run SQL Server workloads directly on Azure Local infrastructure, with the ability to connect to Azure for centralized management, governance, monitoring, security, and licensing. This integration allows organizations to leverage Azure Arc for seamless connection and management of SQL Server instances, providing consistent experiences across hybrid and multi-cloud environments.

- Target audience affected  
This update is relevant for IT professionals managing SQL Server deployments, database administrators, and developers who require hybrid or edge solutions with centralized Azure control. Organizations looking to modernize their SQL Server infrastructure while maintaining local data residency and compliance will benefit.

- Important notes  
Azure Local connected mode enables SQL Server workloads to be managed through Azure services, improving operational efficiency and security. Licensing and monitoring are streamlined via Azure, and governance policies can be enforced centrally. This feature is ideal for scenarios where local infrastructure is required but Azure’s management capabilities are desired. Ensure your Azure Local infrastructure is configured for connected mode to take advantage of these features.

**Details**:

**Comprehensive Technical Explanation: SQL Server Support on Azure Local Connected Mode (Generally Available)**

**Background and Purpose of the Update**  
This update introduces general availability for SQL Server support on Azure Local in connected mode. The primary purpose is to enable organizations to run SQL Server workloads directly on Azure Local infrastructure while maintaining access to Azure’s centralized management, governance, monitoring, security, and licensing capabilities. This approach is designed to address scenarios where data residency, latency, or regulatory requirements necessitate local deployment, but organizations still wish to leverage Azure’s cloud-based operational advantages.

**Specific Features and Detailed Changes**  
- **SQL Server Workload Deployment:** Users can now deploy and operate SQL Server instances on Azure Local infrastructure, which may be physically located closer to the organization or within a specific jurisdiction.
- **Connected Mode:** The infrastructure operates in a connected mode, meaning it maintains a persistent connection to Azure, enabling seamless integration with Azure services.
- **Centralized Management:** Administrators can manage SQL Server instances via Azure’s unified portal, applying policies, monitoring performance, and handling updates centrally.
- **Governance and Security:** Azure’s governance tools (such as Azure Policy and Azure Security Center) can be applied to SQL Server running on Azure Local, ensuring compliance and security standards are maintained.
- **Licensing Integration:** Licensing for SQL Server on Azure Local is streamlined through Azure, simplifying procurement and compliance processes.

**Technical Mechanisms and Implementation Methods**  
- **Azure Arc Integration:** SQL Server on Azure Local leverages Azure Arc, which extends Azure’s management capabilities to infrastructure outside the core Azure cloud. Through Azure Arc, SQL Server instances are registered and managed as Azure resources, enabling consistent policy enforcement, monitoring, and automation.
- **Connected Mode Operation:** The infrastructure maintains continuous connectivity to Azure, allowing real-time synchronization of management, monitoring, and security data.
- **Resource Management:** SQL Server instances are surfaced in the Azure portal as manageable resources, allowing IT professionals to use familiar Azure tools for configuration, monitoring, and lifecycle management.

**Use Cases and Application Scenarios**  
- **Data Residency Compliance:** Organizations with strict data residency requirements can deploy SQL Server locally while still benefiting from Azure’s management and security features.
- **Low-Latency Applications:** Workloads requiring minimal latency can run on Azure Local infrastructure, reducing round-trip times compared to remote cloud deployments.
- **Regulatory Environments:** Industries such as finance, healthcare, or government can meet regulatory mandates by keeping data local, while maintaining centralized oversight.
- **Hybrid Cloud Strategies:** Enterprises pursuing hybrid cloud architectures can unify their SQL Server management across both Azure Local and Azure public cloud environments.

**Important Considerations and Limitations**  
- **Connectivity Requirement:** The connected mode necessitates a persistent connection to Azure; disruptions may impact management and monitoring capabilities.
- **Feature Parity:** While Azure Local provides many Azure cloud features, there may be differences or limitations compared to running SQL Server directly in Azure’s public cloud.
- **Licensing:** Licensing is managed through Azure, and organizations should ensure compliance with Microsoft’s licensing terms for SQL Server on Azure Local.

**Integration with Related Azure Services**  
- **Azure Arc:** Central to the implementation, Azure Arc enables SQL Server instances on Azure Local to be managed as Azure resources.
- **Azure Security Center and Azure Policy:** These services provide security, compliance, and governance for SQL Server workloads, regardless of their physical location.
- **Azure Monitor:** Enables centralized monitoring and alerting for SQL Server performance and health on Azure Local infrastructure.

**Summary Sentence:**  
SQL Server support on Azure Local in connected mode is now generally available, enabling organizations to run SQL Server workloads on local infrastructure while leveraging Azure’s centralized management, governance, monitoring, security, and licensing through Azure Arc integration.

---

### 14. Public Preview: Azure SQL updates for late-September 2026 

**Published**: September 29, 2026 17:49:15 UTC
**Link**: [Public Preview: Azure SQL updates for late-September 2026 ](https://azure.microsoft.com/updates?id=571846)

**Update ID**: 571846
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Feature

**Summary**:

**Azure Update Summary: Public Preview – Azure SQL updates for late-September 2026**

- **What was updated:**  
  Azure SQL received enhancements in late September 2026, introducing new features and improvements, particularly around database management and monitoring.

- **Key changes or new features:**  
  - **Database Hub in Microsoft Fabric:** A unified interface for discovering, managing, monitoring, and optimizing databases across SQL Server and Azure SQL.  
  - Centralized visibility and control for multiple database environments, streamlining operational workflows.  
  - Improved monitoring and optimization tools, enabling faster troubleshooting and performance tuning.  
  - Enhanced integration with Microsoft Fabric, allowing seamless access to database resources alongside other data services.

- **Target audience affected:**  
  - Developers working with SQL Server or Azure SQL databases.  
  - IT professionals responsible for database administration, monitoring, and optimization.  
  - Data engineers and architects leveraging Microsoft Fabric for data solutions.

- **Important notes:**  
  - The Database Hub feature is currently in public preview; feedback is encouraged for further improvements.  
  - Users should review documentation for compatibility and migration considerations, especially when consolidating database management workflows.  
  - Enhanced monitoring and optimization tools may require updated permissions or roles within Azure and Microsoft Fabric environments.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=571846).

**Details**:

**Azure Update Report: Public Preview – Azure SQL Updates for Late-September 2026**

**Background and Purpose of the Update:**  
In late September 2026, Microsoft introduced updates and enhancements to Azure SQL, focusing on improving database management and operational efficiency. The primary objective of this update is to provide a unified experience for database discovery, management, monitoring, and optimization, addressing the needs of organizations managing diverse SQL workloads across both on-premises and cloud environments.

**Specific Features and Detailed Changes:**  
The core feature introduced is the Database Hub within Microsoft Fabric. This hub offers a consolidated interface that allows users to discover, manage, monitor, and optimize databases across SQL Server and Azure SQL. The unified experience streamlines database lifecycle operations, reduces administrative overhead, and enhances visibility into database assets regardless of their deployment location.

**Technical Mechanisms and Implementation Methods:**  
The Database Hub leverages Microsoft Fabric’s integration capabilities to aggregate metadata and operational data from SQL Server (on-premises) and Azure SQL (cloud). Through secure connectors and APIs, the hub collects and presents information about database instances, performance metrics, and configuration settings. The monitoring and optimization functionalities are likely powered by telemetry data and built-in analytics within Microsoft Fabric, enabling real-time insights and actionable recommendations for database administrators.

**Use Cases and Application Scenarios:**  
- **Hybrid Database Management:** Organizations with both on-premises SQL Server and Azure SQL deployments can manage all databases from a single pane of glass, simplifying hybrid cloud operations.
- **Centralized Monitoring:** Database administrators can monitor health, performance, and usage patterns across all SQL assets, enabling proactive maintenance and issue resolution.
- **Optimization Workflows:** The hub provides tools for analyzing and optimizing database performance, supporting tasks such as index tuning, query analysis, and resource allocation.
- **Discovery and Inventory:** Enterprises can maintain an up-to-date inventory of all SQL databases, aiding in compliance, security audits, and capacity planning.

**Important Considerations and Limitations:**  
- The update is currently in Public Preview, which means features may be subject to change and are not recommended for production-critical workloads without proper validation.
- Integration and data collection from on-premises SQL Server instances require appropriate network connectivity and permissions.
- The scope of supported features may vary between SQL Server and Azure SQL, and users should review documentation for compatibility and feature parity.
- Security and compliance requirements must be evaluated, especially when aggregating data from multiple environments into Microsoft Fabric.

**Integration with Related Azure Services:**  
The Database Hub is a component of Microsoft Fabric, which is designed to unify data management and analytics across Microsoft’s ecosystem. This integration allows seamless interoperability with other Azure services such as Azure Monitor, Azure Security Center, and Azure Policy, enabling end-to-end governance, security, and operational management for SQL databases.

**Summary Sentence:**  
In late September 2026, Azure SQL introduced a Public Preview of the Database Hub in Microsoft Fabric, providing a unified platform for discovering, managing, monitoring, and optimizing SQL Server and Azure SQL databases, thereby streamlining hybrid database operations and enhancing administrative efficiency.

---

### 15. Generally Available: Database DevOps in SSMS powered by SQL projects 

**Published**: September 29, 2026 17:42:47 UTC
**Link**: [Generally Available: Database DevOps in SSMS powered by SQL projects ](https://azure.microsoft.com/updates?id=571852)

**Update ID**: 571852
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Database DevOps capabilities in SQL Server Management Studio (SSMS) are now generally available, powered by Microsoft.Build.Sql projects.

- Key changes or new features  
Developers and IT professionals can now use SQL projects directly within SSMS to implement, manage, and collaborate on database changes. SQL projects provide a local definition of database objects (tables, views, procedures, etc.), enabling version control, repeatable deployments, and easier collaboration. Integration with Microsoft.Build.Sql allows for streamlined build and deployment processes, supporting modern DevOps workflows for SQL databases.

- Target audience affected  
SQL developers, database administrators (DBAs), and DevOps engineers who use SSMS for database development and management.

- Important notes if any  
This update enables better source control and CI/CD integration for database projects, reducing manual scripting and deployment errors. Teams can now leverage familiar SSMS tooling to adopt DevOps practices for SQL databases, improving collaboration and consistency across environments. Existing SSMS users should ensure they have the latest version to access these features.  
[More details](https://azure.microsoft.com/updates?id=571852)

**Details**:

**Azure Update Report: Generally Available – Database DevOps in SSMS powered by SQL projects**

**Background and Purpose of the Update**  
This update introduces the general availability of Database DevOps capabilities in SQL Server Management Studio (SSMS) using Microsoft.Build.Sql projects. The primary purpose is to enable IT professionals and database developers to implement, manage, and collaborate on database changes directly within SSMS. By leveraging SQL projects, users gain a local definition of database objects, facilitating version control, repeatable deployments, and improved collaboration in database development workflows.

**Specific Features and Detailed Changes**  
- **SQL Project Integration:** SSMS now supports SQL projects powered by Microsoft.Build.Sql. This allows users to create, edit, and manage SQL projects within SSMS, representing the schema and objects of a database locally.
- **Local Database Object Definition:** SQL projects provide a local representation of SQL objects (tables, views, stored procedures, etc.), enabling developers to work offline and maintain a consistent schema definition.
- **DevOps Workflow Enablement:** The update streamlines DevOps practices for databases by supporting source control integration, change tracking, and deployment automation within SSMS.
- **Collaboration Support:** Multiple team members can work on the same SQL project, facilitating collaborative development and reducing conflicts during schema changes.

**Technical Mechanisms and Implementation Methods**  
- **Microsoft.Build.Sql Projects:** These projects are based on the Microsoft.Build.Sql framework, which structures SQL objects as files within a project, allowing for modular development and easy integration with build and deployment pipelines.
- **SSMS Integration:** The update embeds SQL project management capabilities into SSMS, providing a familiar interface for database professionals to create and manage projects without leaving their primary tool.
- **Local Representation:** By maintaining a local definition of database objects, developers can validate changes, run scripts, and test deployments before applying them to production environments.

**Use Cases and Application Scenarios**  
- **Database Schema Version Control:** Teams can use SQL projects in SSMS to version database schemas, track changes, and roll back to previous states as needed.
- **Automated Deployments:** SQL projects facilitate automated deployment workflows, enabling CI/CD pipelines for database changes.
- **Collaborative Development:** Multiple developers can contribute to a single SQL project, ensuring consistent schema management and reducing merge conflicts.
- **Offline Development:** Developers can work on database objects locally, even without access to the target database, and synchronize changes when ready.

**Important Considerations and Limitations**  
- **Project Structure:** Proper organization of SQL projects is essential for maintainability and scalability.
- **Source Control Integration:** While SQL projects support source control, teams must ensure their workflows are compatible with their chosen version control systems.
- **Deployment Validation:** Local changes should be thoroughly validated before deployment to avoid introducing errors into production databases.
- **Feature Scope:** The update focuses on SQL project management within SSMS; advanced deployment scenarios or integration with external tools may require additional configuration.

**Integration with Related Azure Services**  
- **Azure SQL Database:** SQL projects can be used to manage and deploy schema changes to Azure SQL Database instances, supporting cloud-based database DevOps workflows.
- **Azure DevOps:** Integration with Azure DevOps pipelines is possible, allowing for automated build and deployment of SQL projects as part of broader application delivery processes.

**Summary Sentence**  
Database DevOps in SSMS powered by SQL projects is now generally available, enabling IT professionals to implement, manage, and collaborate on database changes with local definitions of SQL objects, thereby streamlining DevOps workflows and enhancing team productivity within SSMS.

---

### 16. Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume 

**Published**: September 29, 2026 17:40:40 UTC
**Link**: [Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume ](https://azure.microsoft.com/updates?id=571857)

**Update ID**: 571857
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Azure SQL Database Hyperscale now supports auto-pause and auto-resume features in the Serverless compute tier, available in public preview.

- Key changes or new features  
Databases can be configured to automatically pause during periods of inactivity, reducing compute costs. When activity resumes (such as a connection or query), the database automatically resumes operation. This feature is designed to optimize resource usage and cost efficiency for workloads with variable or intermittent usage patterns.

- Target audience affected  
Developers and IT professionals managing Azure SQL Hyperscale databases, especially those using the Serverless compute tier for development, testing, or production workloads with unpredictable or infrequent activity.

- Important notes if any  
Auto-pause and auto-resume settings can be customized based on inactivity timeout requirements. During the paused state, only storage costs are incurred; compute charges resume when the database becomes active. This feature is currently in public preview and may not be suitable for workloads requiring immediate responsiveness at all times. Review documentation for limitations and best practices before enabling in production environments.

For more details, visit: https://azure.microsoft.com/updates?id=571857

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure SQL Database Hyperscale Serverless auto-pause and auto-resume  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=571857)

---

**Background and Purpose of the Update:**  
Azure SQL Database Hyperscale is designed to deliver high performance and scalability for demanding workloads. The Serverless compute tier allows databases to automatically scale compute resources based on workload demand. The introduction of auto-pause and auto-resume features in public preview addresses the need for further cost optimization and operational efficiency by enabling databases to suspend compute resources during periods of inactivity and resume them when activity is detected.

---

**Specific Features and Detailed Changes:**  
This update introduces two key features for Azure SQL Hyperscale databases using the Serverless compute tier:

- **Auto-pause:** Databases can be configured to automatically pause when they are inactive, meaning no user connections or activity are detected for a specified duration.
- **Auto-resume:** Databases automatically resume and allocate compute resources when new activity or connections are detected.

These features are configurable, allowing administrators to set inactivity thresholds and control the auto-pause behavior. The update is currently available in public preview, enabling customers to test and provide feedback before general availability.

---

**Technical Mechanisms and Implementation Methods:**  
The auto-pause and auto-resume mechanisms are integrated into the Serverless compute tier of Azure SQL Hyperscale. When a database is idle (no active connections or queries), the system monitors the inactivity period. Upon reaching the configured threshold, the database’s compute resources are deallocated, effectively pausing the database. Storage remains intact, ensuring data persistence and integrity.

When a new connection or activity is detected, the database automatically resumes, re-allocating compute resources and restoring connectivity. This process is managed by Azure’s orchestration layer, ensuring seamless transitions between paused and active states without manual intervention.

---

**Use Cases and Application Scenarios:**  
- **Development and Test Environments:** Ideal for workloads with intermittent usage, such as development or QA databases, where compute resources are only needed during active development hours.
- **Seasonal or Event-driven Applications:** Applications with unpredictable or infrequent access patterns benefit from reduced costs during idle periods.
- **Cost Optimization for Non-critical Workloads:** Organizations can minimize compute costs for databases that do not require 24/7 availability.

---

**Important Considerations and Limitations:**  
- **Preview Status:** The feature is in public preview and may not be suitable for production workloads until general availability.
- **Configuration Requirements:** Administrators must configure inactivity thresholds and understand the impact of auto-pausing on application connectivity and latency during resume.
- **Resume Latency:** There may be a brief delay when resuming a paused database, which could affect user experience for latency-sensitive applications.
- **Billing Implications:** While compute costs are reduced during paused periods, storage costs continue to accrue.

---

**Integration with Related Azure Services:**  
Auto-pause and auto-resume are native to the Serverless compute tier in Azure SQL Hyperscale and can be managed via Azure Portal, ARM templates, or Azure CLI. These features complement other Azure cost optimization tools and can be integrated with monitoring and alerting solutions to track database state and activity.

---

**Summary Sentence:**  
Azure SQL Database Hyperscale Serverless now supports configurable auto-pause and auto-resume features in public preview, enabling automatic suspension and resumption of compute resources for cost-efficient management of intermittent workloads.

---

### 17. Generally Available: SQL Formatter 

**Published**: September 29, 2026 17:39:36 UTC
**Link**: [Generally Available: SQL Formatter ](https://azure.microsoft.com/updates?id=571872)

**Update ID**: 571872
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
SQL Formatter is now generally available in Visual Studio Code.

- Key changes or new features  
Developers can format SQL scripts directly within VS Code using SQL Formatter, improving code consistency and readability. The tool offers customizable formatting options, allowing users to tailor the style to their coding preferences. This eliminates the need for manual reformatting of SQL queries and supports cleaner, more maintainable code.

- Target audience affected  
SQL developers, database administrators, and IT professionals who use Visual Studio Code for writing and managing SQL scripts.

- Important notes if any  
The SQL Formatter extension can be configured to match individual or team coding standards. It streamlines SQL script editing, making it easier to enforce formatting rules across projects. No additional tools are required—functionality is integrated directly into VS Code. For more details and installation instructions, see the official Azure Update [here](https://azure.microsoft.com/updates?id=571872).

**Details**:

**Azure Update Report: Generally Available – SQL Formatter**

**Background and Purpose of the Update**  
The release of SQL Formatter for Visual Studio Code addresses the common challenge of maintaining consistent and readable SQL code within development environments. Manual formatting of SQL scripts can be time-consuming and error-prone, leading to inconsistencies across teams and projects. The purpose of this update is to automate SQL formatting, enabling developers to produce tidy, standardized queries efficiently and reliably.

**Specific Features and Detailed Changes**  
SQL Formatter is now generally available as an integrated feature in Visual Studio Code. Key features include:

- **Direct Formatting:** Users can format SQL scripts directly within the VS Code editor, eliminating the need for external tools or manual adjustments.
- **Customizable Formatting Options:** Developers can tailor formatting settings to align with their preferred coding style, such as indentation, capitalization, and line breaks.
- **Consistency and Readability:** The formatter ensures that SQL code adheres to defined formatting rules, improving readability and maintainability across codebases.

**Technical Mechanisms and Implementation Methods**  
The SQL Formatter operates as an extension or built-in feature within Visual Studio Code. When a SQL script is opened or edited, users can invoke the formatter via command palette, context menu, or keyboard shortcuts. The formatter parses the SQL code and applies the selected formatting rules, restructuring the script to match the configured style. Customization is managed through settings within VS Code, allowing users to specify preferences for formatting behavior.

**Use Cases and Application Scenarios**  
- **Team Collaboration:** Ensures consistent SQL formatting across team members, reducing merge conflicts and improving code reviews.
- **Database Development:** Streamlines formatting for stored procedures, queries, and scripts, enhancing productivity for database developers.
- **Code Quality Assurance:** Facilitates adherence to organizational coding standards, supporting maintainability and scalability of SQL projects.

**Important Considerations and Limitations**  
- **Customization Scope:** Formatting options are customizable, but users should verify that the available settings meet their specific requirements.
- **Manual Reformatting Reduction:** While the formatter automates most formatting tasks, edge cases may require manual adjustments.
- **Script Compatibility:** Users should ensure that formatted scripts remain compatible with their target database engines and do not introduce syntax errors.

**Integration with Related Azure Services**  
SQL Formatter enhances workflows for Azure-related database development, including Azure SQL Database and Azure Synapse Analytics. By improving SQL script readability and consistency, it supports integration with Azure DevOps pipelines, source control, and other database management tools. Developers working with Azure data services can leverage SQL Formatter to maintain high-quality scripts throughout the development lifecycle.

**Summary Sentence**  
SQL Formatter is now generally available in Visual Studio Code, enabling automated, customizable formatting of SQL scripts for improved code consistency and readability, streamlining database development and team collaboration.

---

### 18. Generally Available: SQL Migration Agent Skills for assessment, migration, and validation 

**Published**: September 29, 2026 17:38:16 UTC
**Link**: [Generally Available: SQL Migration Agent Skills for assessment, migration, and validation ](https://azure.microsoft.com/updates?id=571899)

**Update ID**: 571899
**Data source**: Azure Updates API

**Categories**: Launched, Feature

**Summary**:

- What was updated  
SQL Migration Agent Skills are now generally available, providing automated and AI-powered tools for SQL Server to Azure migration.

- Key changes or new features  
This update introduces reusable skills that automate and streamline the entire migration process, including:  
  - Pre-migration assessment of SQL Server workloads  
  - Intelligent target selection for Azure SQL destinations  
  - Automated migration execution  
  - Post-migration validation to ensure data integrity and performance  
These skills leverage AI to guide users through each step, reducing manual effort and minimizing migration risks.

- Target audience affected  
Developers, database administrators, and IT professionals responsible for migrating SQL Server databases to Azure SQL services.

- Important notes if any  
The SQL Migration Agent Skills are designed to be integrated into existing migration workflows, supporting both small-scale and enterprise migrations. They help ensure a smoother transition with reduced downtime and improved reliability. Users should review documentation for compatibility and best practices before implementation.  
For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=571899

**Details**:

**Azure Update Report: Generally Available – SQL Migration Agent Skills for Assessment, Migration, and Validation**

**Background and Purpose of the Update**  
This update announces the general availability of SQL Migration Agent Skills, designed to automate and streamline the migration process from SQL Server to Azure. The purpose is to enhance the migration experience by leveraging AI-powered, reusable skills that guide users through each phase: assessment, target selection, migration execution, and post-migration validation. This addresses the complexity and manual effort traditionally involved in database migrations, providing a more efficient and reliable pathway to Azure.

**Specific Features and Detailed Changes**  
The SQL Migration Agent Skills introduce several key features:
- **Automated Assessment**: AI-driven analysis of existing SQL Server environments to identify readiness and potential migration issues.
- **Target Selection Guidance**: Intelligent recommendations for optimal Azure targets based on workload characteristics and compatibility.
- **Migration Execution Automation**: Streamlined orchestration of the migration process, reducing manual intervention and minimizing downtime.
- **Post-Migration Validation**: Automated verification of migrated data and configurations to ensure integrity and operational continuity.

These skills are reusable, meaning they can be applied across multiple migration projects, enhancing consistency and reducing repetitive tasks.

**Technical Mechanisms and Implementation Methods**  
The SQL Migration Agent Skills are powered by AI algorithms integrated within the migration agent framework. The agent interacts with source SQL Server instances, collects metadata and configuration details, and applies AI models to assess migration readiness. During migration, the agent automates data transfer, schema conversion, and configuration adjustments. Post-migration, validation routines compare source and target environments to confirm successful migration. The skills are modular, allowing IT professionals to invoke specific functions as needed throughout the migration lifecycle.

**Use Cases and Application Scenarios**  
- **Enterprise Database Modernization**: Organizations migrating legacy SQL Server workloads to Azure SQL Database or Azure SQL Managed Instance can leverage these skills for a seamless transition.
- **Cloud Adoption Projects**: IT teams tasked with moving on-premises databases to Azure benefit from automated assessment and validation, reducing risk and effort.
- **Multi-Project Migration Programs**: Reusable skills support consistent execution across multiple migration initiatives, improving efficiency and standardization.

**Important Considerations and Limitations**  
- The skills are designed specifically for migrations from SQL Server to Azure; applicability to other database platforms is not indicated.
- AI-driven recommendations depend on the quality and completeness of source environment data collected by the agent.
- While automation reduces manual effort, IT professionals should review assessment and validation results to ensure alignment with business and compliance requirements.
- The update does not specify support for hybrid or cross-cloud migrations.

**Integration with Related Azure Services**  
SQL Migration Agent Skills integrate with Azure’s database migration ecosystem, including Azure SQL Database and Azure SQL Managed Instance. They complement existing migration tools and services, such as Azure Database Migration Service (DMS), by providing enhanced automation and intelligence. The skills can be orchestrated alongside Azure monitoring and management solutions for end-to-end visibility and control.

**Summary Sentence**  
SQL Migration Agent Skills, now generally available, offer AI-powered automation for assessment, migration, and validation, streamlining the end-to-end process of moving SQL Server workloads to Azure with reusable and intelligent capabilities.

---

### 19. Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029

**Published**: September 29, 2026 17:36:13 UTC
**Link**: [Retirement: Azure Arc enabled System Center Virtual Machine Manager will be retired September 30, 2029](https://azure.microsoft.com/updates?id=570283)

**Update ID**: 570283
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Arc-enabled System Center Virtual Machine Manager (SCVMM), effective September 30, 2029.

- Key changes or new features  
Azure Arc-enabled SCVMM will no longer be supported after the retirement date. No new features or updates will be released for this integration. Customers using SCVMM to connect on-premises virtual machines to Azure services via Azure Arc must transition to alternative solutions before the deadline.

- Target audience affected  
This update impacts IT professionals and developers managing hybrid environments with Azure Arc-enabled SCVMM, especially those leveraging SCVMM for Azure services integration, VM management, and hybrid cloud scenarios.

- Important notes if any  
Microsoft recommends planning migration strategies well ahead of the retirement date. Evaluate other Azure Arc-supported platforms or native Azure management tools for future hybrid and multi-cloud management needs. Continued use of Azure Arc-enabled SCVMM after September 2029 will not be supported, potentially affecting security, compliance, and operational continuity. For more details and migration guidance, refer to the official Azure update link.

**Details**:

**Azure Update Report: Retirement of Azure Arc-enabled System Center Virtual Machine Manager (SCVMM) – Effective September 30, 2029**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of Azure Arc-enabled System Center Virtual Machine Manager (SCVMM), effective September 30, 2029. This update is part of Microsoft’s ongoing lifecycle management and modernization strategy, encouraging customers to transition from legacy management solutions to more current and supported technologies. The purpose is to provide ample notice to organizations leveraging Azure Arc-enabled SCVMM, enabling them to plan and execute migration strategies to alternative solutions before the retirement date.

**Specific Features and Detailed Changes**  
Azure Arc-enabled SCVMM is a hybrid management solution that allows organizations to project their on-premises SCVMM-managed virtual machines into Azure, enabling management and governance through Azure services. The retirement means that after September 30, 2029, Microsoft will discontinue support, updates, and technical assistance for this integration. Users will no longer be able to use Azure Arc to onboard SCVMM-managed resources or leverage Azure services such as policy, monitoring, and security extensions on these resources via this pathway.

**Technical Mechanisms and Implementation Methods**  
Currently, Azure Arc-enabled SCVMM works by connecting System Center Virtual Machine Manager environments to Azure Arc, registering SCVMM-managed VMs as Azure resources. This integration enables the application of Azure governance, security, and management capabilities to on-premises VMs. The retirement will deprecate all mechanisms that facilitate this connection, including the onboarding process, resource projection, and the use of Azure management extensions on SCVMM-managed VMs.

**Use Cases and Application Scenarios**  
Typical use cases for Azure Arc-enabled SCVMM include hybrid cloud management, centralized policy enforcement, unified monitoring, and security management for on-premises virtual machines managed by SCVMM. Organizations with significant investments in SCVMM and hybrid architectures have used this integration to extend Azure capabilities to their datacenter workloads without full migration to Azure.

**Important Considerations and Limitations**  
- After September 30, 2029, all support and updates for Azure Arc-enabled SCVMM will cease.
- Organizations must identify workloads and management processes dependent on this integration and plan for migration to supported alternatives.
- Failure to transition may result in loss of management, monitoring, and governance capabilities for SCVMM-managed VMs via Azure.
- There is no information in the update about automated migration tools or direct replacement solutions; customers must evaluate their options based on their specific environment and requirements.

**Integration with Related Azure Services**  
Azure Arc-enabled SCVMM serves as a bridge between on-premises SCVMM environments and Azure services, enabling integration with Azure Policy, Azure Monitor, Azure Security Center, and other governance and management tools. The retirement will impact any workflows or automation relying on this integration. Organizations should assess dependencies on these Azure services and plan to transition to supported management solutions, such as Azure Arc-enabled servers (for non-SCVMM VMs) or direct Azure-native management for cloud-based workloads.

**Summary Sentence**  
Microsoft will retire Azure Arc-enabled System Center Virtual Machine Manager on September 30, 2029, and customers using this integration must plan to transition to alternative solutions before support ends.

---

### 20. Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale

**Published**: September 29, 2026 17:34:44 UTC
**Link**: [Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale](https://azure.microsoft.com/updates?id=571795)

**Update ID**: 571795
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

**What was updated:**  
Azure now supports direct migration from Azure Arc-enabled SQL Server to Azure SQL Database, including the Hyperscale tier, in public preview.

**Key changes or new features:**  
- Developers and IT professionals can select Azure SQL Database (including Hyperscale) as a migration target directly within the Azure Arc database migration workflow.  
- The migration process integrates Azure Database Migration Service (DMS) and Self-hosted Integration Runtime setup into a guided experience, simplifying migration steps and reducing manual configuration.  
- The update enables seamless migration from hybrid or on-premises environments managed by Azure Arc to fully managed Azure SQL Database offerings.

**Target audience affected:**  
- Developers and IT professionals managing SQL Server workloads in hybrid or on-premises environments via Azure Arc.  
- Teams planning to modernize or migrate their database infrastructure to Azure SQL Database, especially those requiring Hyperscale capabilities.

**Important notes:**  
- This feature is currently in public preview; production workloads should be evaluated carefully before migration.  
- The guided workflow aims to minimize migration complexity and downtime, but users should review prerequisites and compatibility for Hyperscale migrations.  
- For more details and instructions, refer to the official Azure Update [link](https://azure.microsoft.com/updates?id=571795).

**Details**:

**Azure Update Report**

**Title:** Public Preview: Migrate directly from Azure Arc to Azure SQL Database, including Hyperscale  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=571795)

---

**Background and Purpose of the Update:**  
This update introduces the capability to migrate databases managed via Azure Arc directly to Azure SQL Database, including the Hyperscale tier. Azure Arc enables organizations to manage databases across hybrid and multi-cloud environments using Azure tools. Previously, migration workflows may have required intermediate steps or manual configurations. The purpose of this update is to streamline and simplify the migration process, allowing IT professionals to move workloads from Azure Arc-enabled environments to Azure SQL Database with minimal friction.

**Specific Features and Detailed Changes:**  
- **Direct Migration Target Selection:** Users can now select Azure SQL Database (including Hyperscale) as the migration destination directly within the Azure Arc database migration experience.
- **Integrated Workflow:** The migration workflow now incorporates Azure Database Migration Service (DMS) and Self-hosted Integration Runtime setup into a guided process, reducing manual setup and configuration.
- **Hyperscale Support:** The inclusion of Hyperscale as a migration target allows for migration to a highly scalable Azure SQL Database tier, supporting large-scale workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Azure Database Migration Service Integration:** The workflow leverages Azure DMS, which automates the migration of schema, data, and objects from source databases to Azure SQL Database.
- **Self-hosted Integration Runtime:** The setup for Self-hosted Integration Runtime is embedded within the guided migration workflow. This runtime facilitates secure data movement from on-premises or Arc-enabled sources to Azure SQL Database.
- **Guided Experience:** The migration process is presented as a step-by-step workflow within the Azure Arc portal, minimizing manual intervention and configuration errors.

**Use Cases and Application Scenarios:**  
- **Hybrid Cloud Database Modernization:** Organizations managing databases in hybrid environments via Azure Arc can now migrate directly to Azure SQL Database for modernization, scalability, and managed service benefits.
- **Large-scale Data Migration:** Enterprises with large datasets can leverage Hyperscale as a migration target, ensuring performance and scalability during and after migration.
- **Simplified Migration for IT Teams:** IT professionals can use the integrated workflow to reduce complexity and accelerate migration projects from Arc-enabled sources to Azure SQL Database.

**Important Considerations and Limitations:**  
- **Public Preview Status:** The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- **Guided Workflow Dependency:** Migration relies on the guided workflow, which may have specific prerequisites or limitations regarding supported source database types, versions, or configurations.
- **Self-hosted Integration Runtime Requirements:** Proper setup and connectivity for the Self-hosted Integration Runtime are necessary for successful migration, especially from on-premises sources.

**Integration with Related Azure Services:**  
- **Azure Arc:** Acts as the management layer for hybrid and multi-cloud database resources.
- **Azure Database Migration Service:** Provides the core migration engine for schema and data movement.
- **Azure SQL Database (Hyperscale):** Serves as the destination platform, offering managed database capabilities and high scalability.
- **Self-hosted Integration Runtime:** Enables secure and reliable data transfer across environments.

---

**Summary Sentence:**  
This update enables IT professionals to migrate databases managed via Azure Arc directly to Azure SQL Database, including Hyperscale, using a guided workflow that integrates Azure Database Migration Service and Self-hosted Integration Runtime setup, thereby simplifying and accelerating hybrid cloud database modernization projects.

---

### 21. Public Preview: Microsoft SQL Agent Skills

**Published**: September 29, 2026 17:31:11 UTC
**Link**: [Public Preview: Microsoft SQL Agent Skills](https://azure.microsoft.com/updates?id=573003)

**Update ID**: 573003
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Microsoft announced the public preview of Microsoft SQL Agent Skills, a set of AI-powered capabilities designed to provide more accurate, SQL-specific guidance for building, operating, and migrating SQL workloads.

- Key changes or new features  
SQL Agent Skills enhance AI agents with product-specific knowledge for Azure SQL Database, Azure SQL Database container, and SQL Server migration to Azure. These skills help users receive tailored recommendations and troubleshooting assistance, improving efficiency and accuracy when working with SQL workloads. Developers and IT professionals can leverage these skills to streamline migration processes, optimize operations, and resolve issues faster.

- Target audience affected  
Developers and IT professionals working with Azure SQL Database, SQL Server, and related migration scenarios. Teams planning or executing SQL Server migrations to Azure will benefit from improved AI-driven guidance.

- Important notes if any  
The feature is currently in public preview, so it may not be suitable for production environments yet. Feedback from early adopters will help refine the capabilities. Integration with AI agents is intended to make SQL workload management and migration more seamless and reliable. For more details and to participate in the preview, visit the official Azure update page.

**Details**:

**Azure Update Report: Public Preview – Microsoft SQL Agent Skills**

**Background and Purpose of the Update**  
Microsoft has introduced SQL Agent Skills in public preview to enhance the accuracy and relevance of guidance provided by AI agents when working with SQL workloads. The primary goal is to deliver product-specific expertise for Azure SQL Database, Azure SQL Database container, and SQL Server to Azure migration scenarios. This update addresses the need for more tailored, actionable support for IT professionals leveraging AI-driven solutions in SQL environments.

**Specific Features and Detailed Changes**  
The SQL Agent Skills are designed to integrate with AI agents, enabling them to offer precise recommendations and operational guidance specific to Microsoft SQL products. Key features include:

- Product-specific guidance: AI agents can now provide recommendations and best practices tailored to Azure SQL Database, Azure SQL Database container, and SQL Server migration to Azure.
- Enhanced accuracy: The skills improve the quality of AI-driven support, reducing generic or irrelevant advice.
- Support for build, operate, and migrate workflows: The skills cover the full lifecycle of SQL workloads, from initial deployment to ongoing management and migration.

**Technical Mechanisms and Implementation Methods**  
Microsoft SQL Agent Skills are implemented as modular capabilities that can be invoked by AI agents during interactions with SQL workloads. These skills leverage underlying product knowledge and operational best practices to inform AI-driven responses. Integration is achieved through APIs or skill invocation mechanisms, allowing AI agents to access up-to-date guidance for specific SQL scenarios. The skills are compatible with Azure SQL Database, Azure SQL Database container, and migration workflows from SQL Server to Azure, ensuring broad applicability across Microsoft’s SQL portfolio.

**Use Cases and Application Scenarios**  
Typical use cases include:

- Building new SQL workloads: AI agents equipped with SQL Agent Skills can guide engineers through optimal configuration, deployment, and scaling of Azure SQL Database or containers.
- Operating existing SQL environments: The skills enable AI agents to assist with performance tuning, security configuration, and maintenance tasks, providing context-aware recommendations.
- Migrating SQL Server to Azure: During migration projects, AI agents can offer step-by-step guidance, highlight potential pitfalls, and suggest best practices specific to the migration process.

These scenarios benefit IT professionals by streamlining operations, reducing manual research, and minimizing errors during complex SQL tasks.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not offer full coverage for all SQL scenarios and could be subject to change based on user feedback. IT professionals should validate AI agent recommendations against official documentation and production requirements. Additionally, integration with existing workflows may require updates to AI agent configurations to utilize the new skills effectively.

**Integration with Related Azure Services**  
Microsoft SQL Agent Skills are designed to work seamlessly with Azure SQL Database and Azure SQL Database container services. They also support migration workflows from SQL Server to Azure, complementing Azure’s broader database migration tools and services. This integration ensures that AI-driven guidance is consistent with Azure’s platform capabilities and best practices.

**Summary Sentence**  
Microsoft SQL Agent Skills in public preview provide AI agents with product-specific expertise for Azure SQL Database, Azure SQL Database container, and SQL Server migration to Azure, enabling more accurate guidance for building, operating, and migrating SQL workloads.

---

### 22. Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL

**Published**: September 29, 2026 17:28:57 UTC
**Link**: [Public Preview: Long-term retention (LTR) v2 for Azure Database for PostgreSQL](https://azure.microsoft.com/updates?id=571914)

**Update ID**: 571914
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL now offers Long-term Retention (LTR) v2 in public preview.

- Key changes or new features  
LTR v2 replaces the previous logical backup approach (pg_dump/pg_restore) with physical, snapshot-based backups. These snapshots are integrated with Azure Backup Vaults, enabling more efficient, scalable, and secure long-term backup storage and management. The new solution supports automated backup scheduling, retention policies, and easier restore operations. LTR v2 also improves backup reliability and performance compared to LTR v1.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL instances, especially those with compliance or business requirements for long-term data retention and backup management.

- Important notes if any  
LTR v2 is currently in public preview and may not have full production support. Existing LTR v1 users should evaluate migration options, as the backup mechanism has changed significantly. Integration with Azure Backup Vaults allows centralized management and monitoring of backups across multiple databases and workloads. Review documentation for limitations and compatibility before adoption.

For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=571914

**Details**:

**Azure Update Report: Public Preview – Long-term retention (LTR) v2 for Azure Database for PostgreSQL**

**Background and Purpose of the Update:**  
LTR v2 introduces a next-generation long-term backup solution for Azure Database for PostgreSQL. The primary motivation behind this update is to enhance backup reliability, efficiency, and integration with Azure-native backup management tools. The previous version, LTR v1, relied on logical backups using `pg_dump` and `pg_restore`, which could be time-consuming and less efficient for large databases. LTR v2 addresses these limitations by moving to a physical snapshot-based approach, aligning with modern backup and disaster recovery requirements.

**Specific Features and Detailed Changes:**  
- **Physical Snapshot-Based Backups:** LTR v2 replaces logical backups with physical, storage-level snapshots. This method captures the entire database state at a specific point in time, improving backup speed and restore reliability.
- **Integration with Azure Backup Vaults:** Backups are now stored in Azure Backup Vaults, providing centralized management, enhanced security, and compliance capabilities.
- **Next-Generation Backup Architecture:** This update leverages Azure’s native backup infrastructure, offering improved scalability and operational efficiency compared to the previous logical backup method.

**Technical Mechanisms and Implementation Methods:**  
- **Snapshot Technology:** Physical snapshots are taken at the storage layer, ensuring that all database files are captured in a consistent state. This reduces backup windows and minimizes performance impact on the running PostgreSQL instance.
- **Azure Backup Vault Integration:** Backups are managed through Azure Backup Vaults, which offer features such as role-based access control (RBAC), backup policy management, and long-term retention configuration.
- **Automated Backup Scheduling and Retention:** Administrators can define backup schedules and retention policies directly within the Azure portal or via automation tools, ensuring compliance with organizational data retention requirements.

**Use Cases and Application Scenarios:**  
- **Regulatory Compliance:** Organizations with strict data retention policies (e.g., financial, healthcare, or government sectors) can leverage LTR v2 to retain backups for extended periods.
- **Disaster Recovery:** Physical snapshots enable faster and more reliable restores in the event of data corruption, accidental deletion, or other disaster scenarios.
- **Centralized Backup Management:** Enterprises managing multiple PostgreSQL instances can benefit from the centralized visibility and control offered by Azure Backup Vaults.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As LTR v2 is in public preview, it may not be suitable for production workloads requiring full support and SLAs.
- **Migration from LTR v1:** Existing users of logical backup-based LTR v1 should evaluate migration strategies, as backup formats and restore processes differ between logical and physical backups.
- **Feature Parity:** Not all features from LTR v1 may be available in v2 during the preview phase; users should review documentation for any functional gaps.

**Integration with Related Azure Services:**  
- **Azure Backup Vaults:** LTR v2 is tightly integrated with Azure Backup Vaults, leveraging their security, policy management, and monitoring capabilities.
- **Azure Portal and Automation:** Backup management, scheduling, and retention configuration are accessible through the Azure portal, CLI, and automation scripts, enabling seamless integration into existing DevOps workflows.

**Summary Sentence:**  
LTR v2 for Azure Database for PostgreSQL introduces a robust, snapshot-based long-term backup solution integrated with Azure Backup Vaults, offering improved performance, centralized management, and enhanced compliance capabilities for enterprise database workloads.

---

### 23. Retirement: Microsoft HPC Pack

**Published**: September 29, 2026 17:26:50 UTC
**Link**: [Retirement: Microsoft HPC Pack](https://azure.microsoft.com/updates?id=570046)

**Update ID**: 570046
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of all versions of Microsoft HPC Pack, its high-performance computing cluster management solution.

- Key changes or new features  
HPC Pack will no longer be supported after August 27, 2027. Starting now, HPC Pack enters a one-year retirement period, during which Microsoft will provide only limited, retirement-only support. No new features or enhancements will be released, and support will focus solely on critical issues as defined by Microsoft.

- Target audience affected  
Developers and IT professionals who use Microsoft HPC Pack for managing and deploying HPC clusters, including those integrating with Azure or on-premises environments.

- Important notes if any  
Users must plan to migrate workloads and cluster management to alternative solutions before the end of support date. After August 27, 2027, no security updates, bug fixes, or technical support will be available. It is recommended to review Microsoft’s guidance for migration and consider Azure-native HPC services or other supported cluster management tools. Early planning is essential to ensure continued support and avoid disruptions.

**Details**:

**Azure Update Report: Retirement of Microsoft HPC Pack**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of all versions of Microsoft HPC Pack, with end of support scheduled for August 27, 2027. HPC Pack, a solution for managing and running high-performance computing (HPC) workloads, is entering a one-year retirement period. The purpose of this update is to inform users and IT professionals about the timeline and scope of support during the retirement phase, enabling organizations to plan migration or transition strategies accordingly.

**Specific Features and Detailed Changes:**  
The key change is the cessation of mainstream support for Microsoft HPC Pack. During the one-year retirement period, Microsoft will provide limited, retirement-only support. This means that while the product will not receive new features, enhancements, or regular security updates, some essential support may be available as defined by Microsoft. After August 27, 2027, all support for HPC Pack will be discontinued, and the product will no longer be maintained or updated.

**Technical Mechanisms and Implementation Methods:**  
The retirement process involves the gradual reduction of support services for HPC Pack. During the retirement-only support period, Microsoft will address only critical issues as per their defined scope, and no further development or bug fixes will be provided. Technical professionals should note that the mechanisms for support will be limited to essential maintenance, with no guarantee of resolution for non-critical issues. Organizations must begin planning for migration to alternative solutions, as continued operation of HPC Pack beyond the end-of-support date will expose workloads to potential risks due to lack of updates.

**Use Cases and Application Scenarios:**  
HPC Pack has been used to orchestrate and manage HPC clusters, enabling parallel processing and distributed computing for workloads such as scientific simulations, financial modeling, and engineering analysis. Typical application scenarios include on-premises or hybrid HPC environments where compute nodes are managed centrally. With the announced retirement, organizations relying on HPC Pack for these scenarios must evaluate alternative solutions for HPC workload management, such as Azure CycleCloud or other cloud-native HPC orchestration tools.

**Important Considerations and Limitations:**  
IT professionals must consider the following limitations:
- After August 27, 2027, Microsoft HPC Pack will no longer be supported, and no updates or patches will be released.
- During the retirement period, support is limited and defined by Microsoft; no new features or enhancements will be provided.
- Continued use of HPC Pack post-retirement may expose systems to security vulnerabilities and operational risks.
- Migration planning should begin immediately to ensure continuity of HPC workloads and compliance with organizational IT policies.

**Integration with Related Azure Services:**  
While HPC Pack has traditionally supported hybrid and on-premises HPC workloads, its retirement encourages migration to Azure-native solutions. Azure CycleCloud is recommended for orchestrating and managing HPC workloads in the cloud, offering scalability, integration with Azure compute resources, and support for modern HPC architectures. Integration with Azure services such as Azure Virtual Machines, Azure Batch, and Azure Storage will provide enhanced flexibility and performance for HPC workloads previously managed by HPC Pack.

**Summary Sentence:**  
Microsoft HPC Pack is entering a one-year retirement period with limited support, culminating in full end-of-support on August 27, 2027; IT professionals must plan migration to alternative HPC solutions, as no further updates or maintenance will be provided beyond this date.

---

### 24. Retirement: Azure IoT Central will be retired on September 20, 2029

**Published**: September 29, 2026 17:25:10 UTC
**Link**: [Retirement: Azure IoT Central will be retired on September 20, 2029](https://azure.microsoft.com/updates?id=569914)

**Update ID**: 569914
**Data source**: Azure Updates API

**Categories**: Internet of Things, Azure IoT Central, Retirements

**Summary**:

- What was updated  
Azure IoT Central will be retired on September 20, 2029.

- Key changes or new features  
No new features are being introduced. The key change is the announcement of the retirement date for Azure IoT Central. Microsoft is shifting its focus to other Azure IoT solutions as part of its evolving IoT strategy.

- Target audience affected  
Developers and IT professionals who currently use Azure IoT Central for device management, monitoring, and IoT solution development are directly affected. Organizations with active IoT Central deployments should take note.

- Important notes  
Users can continue to use Azure IoT Central until September 20, 2029. Microsoft recommends starting transition planning early to migrate workloads and solutions to alternative Azure IoT services, such as Azure IoT Hub or Azure Digital Twins. There will be no further feature development for IoT Central, and support will be limited as the retirement date approaches. Review your current IoT Central usage and begin evaluating migration options to ensure continuity and minimize disruption. For more information and guidance, refer to the official Azure Update announcement.

**Details**:

**Retirement: Azure IoT Central will be retired on September 20, 2029**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Azure IoT Central, effective September 20, 2029. This update is part of Microsoft’s ongoing evolution of its Azure IoT portfolio, with a shift in focus toward other IoT solutions and services. The retirement notice is intended to give customers ample time to plan and execute migration strategies for their IoT workloads.

**Specific Features and Detailed Changes:**  
Azure IoT Central is a fully managed IoT application platform that provides a ready-to-use environment for connecting, monitoring, and managing IoT assets at scale. With this retirement, all features and functionalities of Azure IoT Central—including device connectivity, device templates, dashboards, rules, data export, and integration capabilities—will no longer be available after the specified date. No new features or enhancements are expected, and support will be phased out in accordance with Microsoft’s retirement policies.

**Technical Mechanisms and Implementation Methods:**  
The retirement process means that, after September 20, 2029, all Azure IoT Central resources and applications will be decommissioned. Existing deployments will continue to function until the retirement date, but users should not expect ongoing platform improvements or long-term support. Microsoft recommends that customers begin transition planning as soon as possible to ensure business continuity and compliance with internal and external requirements.

**Use Cases and Application Scenarios:**  
Azure IoT Central has been widely used for rapid IoT solution development, especially in scenarios where organizations require a managed platform to quickly connect devices, visualize telemetry, and automate actions without building custom backend infrastructure. Common use cases include remote monitoring, predictive maintenance, connected product management, and smart building solutions. Organizations relying on these scenarios must now evaluate alternative Azure IoT offerings or other platforms.

**Important Considerations and Limitations:**  
- **Service Availability:** Azure IoT Central will remain operational until September 20, 2029, after which all services will be discontinued.
- **Transition Planning:** Early migration planning is strongly recommended to avoid service disruption.
- **Data Migration:** Customers must ensure that all necessary data is exported and migrated before the retirement date, as data will not be accessible after decommissioning.
- **Support:** No new features will be added, and support will be limited as the retirement date approaches.
- **Compliance:** Organizations should assess the impact on compliance and regulatory requirements, particularly if IoT Central is part of critical business processes.

**Integration with Related Azure Services:**  
Azure IoT Central integrates with various Azure services, such as Azure IoT Hub, Azure Stream Analytics, Azure Logic Apps, and Azure Data Explorer, to provide end-to-end IoT solutions. With the retirement of IoT Central, customers must review their architecture and consider direct use of these underlying services or migrate to alternative managed IoT platforms within Azure. This may involve re-architecting device connectivity, data ingestion, processing, and integration workflows.

**Summary:**  
Azure IoT Central will be retired on September 20, 2029; customers should begin transition planning to alternative solutions to ensure continuity of IoT operations and integrations.

---

### 25. Generally Available: Support for large volume breakthrough mode

**Published**: September 29, 2026 17:12:40 UTC
**Link**: [Generally Available: Support for large volume breakthrough mode](https://azure.microsoft.com/updates?id=573027)

**Update ID**: 573027
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Feature

**Summary**:

- What was updated  
Azure NetApp Files now offers General Availability for "large volume breakthrough mode," supporting extreme performance and scalability for high-demand workloads.

- Key changes or new features  
This update enables Azure NetApp Files to support volumes up to 2 PiB (Pebibytes) and deliver throughput up to 80 GiBps, depending on workload characteristics. The feature is designed to meet the needs of high-performance computing (HPC) and electronic design automation (EDA) workloads, allowing users to handle larger datasets and achieve faster data processing.

- Target audience affected  
Developers and IT professionals managing HPC, EDA, or other data-intensive workloads in Azure environments. Organizations requiring high throughput and large storage volumes for applications such as simulation, modeling, and analytics will benefit from this update.

- Important notes if any  
To leverage breakthrough mode, ensure your workloads are compatible with the new volume and throughput limits. Review Azure NetApp Files documentation for configuration guidelines and performance best practices. This feature may impact quota management and pricing, so verify your subscription’s eligibility and plan accordingly. For more details, visit the official Azure Update announcement.

**Details**:

**Azure Update Report: Generally Available – Support for Large Volume Breakthrough Mode in Azure NetApp Files**

**Background and Purpose of the Update:**  
Azure NetApp Files is a high-performance, enterprise-grade storage solution designed for demanding workloads. This update introduces the "large volume breakthrough mode," targeting scenarios where extreme performance and scalability are required, such as high-performance computing (HPC) and electronic design automation (EDA). The purpose is to address the growing need for massive storage volumes and higher throughput in complex, data-intensive workloads.

**Specific Features and Detailed Changes:**  
The large volume breakthrough mode enables Azure NetApp Files to support volumes up to 2 PiB (Pebibytes), a significant increase from previous volume limits. Throughput capabilities are also enhanced, with the mode delivering up to 80 GiBps (Gibibytes per second), depending on workload characteristics. This update is now generally available, meaning it is fully supported and ready for production use.

**Technical Mechanisms and Implementation Methods:**  
The breakthrough mode leverages Azure NetApp Files’ underlying architecture, which is built on NetApp ONTAP technology. By optimizing the storage backend and network pathways, it allows for aggregation of multiple storage pools and improved parallelism. This results in higher throughput and larger volume sizes. The mode is enabled through configuration settings within Azure NetApp Files, allowing users to provision and manage large volumes seamlessly via the Azure portal, CLI, or API.

**Use Cases and Application Scenarios:**  
- **HPC Workloads:** Scientific simulations, modeling, and analytics that require rapid access to large datasets benefit from the increased volume size and throughput.
- **EDA Workflows:** Chip design and verification processes often involve massive files and concurrent access, making the breakthrough mode ideal for these workloads.
- **Media and Entertainment:** High-resolution rendering and editing tasks that demand fast, scalable storage.
- **Financial Services:** Real-time analytics and risk modeling with large data sets.

**Important Considerations and Limitations:**  
- Throughput is workload-dependent; actual performance may vary based on access patterns and volume configuration.
- Not all workloads may require the maximum volume size or throughput; careful assessment is needed to optimize cost and performance.
- The mode is intended for demanding, large-scale workloads; smaller or less intensive workloads may not benefit from the increased limits.
- Users must ensure compatibility with their application and infrastructure requirements when configuring large volumes.

**Integration with Related Azure Services:**  
Azure NetApp Files integrates natively with Azure’s ecosystem, supporting virtual machines, containers, and other compute resources. The large volume breakthrough mode can be used in conjunction with Azure HPC clusters, Azure Kubernetes Service (AKS), and Azure Virtual Machines to provide high-performance shared storage. It also supports standard Azure security, backup, and monitoring features, ensuring enterprise-grade reliability and manageability.

**Summary Sentence:**  
Azure NetApp Files’ large volume breakthrough mode is now generally available, offering support for volumes up to 2 PiB and throughput up to 80 GiBps, enabling extreme performance and scalability for demanding HPC and EDA workloads.

---

### 26. Generally Available: Storage with cool access enhancement 

**Published**: September 29, 2026 17:09:58 UTC
**Link**: [Generally Available: Storage with cool access enhancement ](https://azure.microsoft.com/updates?id=573032)

**Update ID**: 573032
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Feature

**Summary**:

- What was updated  
Azure NetApp Files now offers a generally available enhancement: Quality of Service (QoS) updates with cool access enabled for Premium and Ultra service levels.

- Key changes or new features  
The update allows Azure NetApp Files to automatically adjust throughput as data transitions between hot and cool storage tiers. This ensures that performance remains consistent for hot-tier data while optimizing costs for cool-tier workloads. Developers and IT professionals can now efficiently manage mixed hot and cool workloads without manual intervention, leveraging improved cost-performance balance.

- Target audience affected  
This update is relevant for developers, IT professionals, and storage administrators using Azure NetApp Files, especially those managing applications with varying data access patterns (hot and cool workloads) on Premium or Ultra service levels.

- Important notes if any  
The enhancement is now generally available and applies specifically to Premium and Ultra service levels. Throughput adjustments are automatic, requiring no manual configuration. This feature helps optimize storage costs while maintaining high performance for frequently accessed data. For further details and implementation guidance, refer to the official Azure Update link.

**Details**:

**Azure Update Report: Generally Available – Storage with Cool Access Enhancement for Azure NetApp Files**

**Background and Purpose of the Update**  
This update addresses the need for efficient management of mixed hot and cool workloads in Azure NetApp Files. Traditionally, storage tiers are optimized either for performance (hot data) or for cost (cool data), but balancing these requirements in dynamic environments has been challenging. The purpose of this enhancement is to improve the Quality of Service (QoS) for workloads that require both high performance and cost efficiency, particularly as data transitions between hot and cool access patterns.

**Specific Features and Detailed Changes**  
The update introduces cool access capabilities on Premium and Ultra service levels for Azure NetApp Files. Key features include:

- **QoS Update:** The Quality of Service mechanism now supports automatic throughput adjustment as data moves to cool storage.
- **Cool Access Enablement:** Premium and Ultra tiers can now handle cool workloads, not just hot workloads.
- **Performance and Cost Balance:** The system maintains hot-tier performance even as data transitions to cool storage, optimizing both throughput and storage costs.

**Technical Mechanisms and Implementation Methods**  
The technical implementation centers on dynamic throughput management:

- **Automatic Throughput Adjustment:** As data is identified and moved to cool storage, Azure NetApp Files automatically adjusts the throughput allocation, ensuring that performance remains consistent for hot workloads while optimizing for cost on cool workloads.
- **QoS Integration:** The QoS system is enhanced to recognize workload patterns and adjust storage tiering and throughput accordingly, without manual intervention.
- **Service Level Extension:** Cool access is now natively supported in Premium and Ultra service levels, expanding their capabilities beyond hot data scenarios.

**Use Cases and Application Scenarios**  
This update is particularly beneficial in the following scenarios:

- **Mixed Workload Environments:** Organizations running applications with both frequently accessed (hot) and infrequently accessed (cool) data can leverage this feature to optimize performance and cost.
- **Data Lifecycle Management:** Enterprises with data that transitions from hot to cool (e.g., analytics, backup, archival) can benefit from seamless throughput adjustments.
- **Cost Optimization Projects:** IT teams seeking to reduce storage costs without sacrificing performance for critical workloads will find this enhancement valuable.

**Important Considerations and Limitations**  
- **Service Level Availability:** Cool access enhancement is available only on Premium and Ultra service levels; Standard tier is not included.
- **Automatic Adjustment:** Throughput adjustments are managed automatically; manual control over throughput for cool workloads is not specified.
- **Performance Maintenance:** While hot-tier performance is maintained, actual throughput for cool workloads may differ based on system optimization.

**Integration with Related Azure Services**  
- **Azure NetApp Files Ecosystem:** This enhancement is fully integrated into Azure NetApp Files, allowing seamless operation with existing file storage solutions.
- **Azure Storage Management:** IT professionals can incorporate this feature into their broader Azure storage strategies, aligning with lifecycle management and cost optimization initiatives.
- **Compatibility:** The update is designed to work within the Azure platform, ensuring compatibility with other Azure services that interact with NetApp Files.

**Summary Sentence**  
The Storage with cool access enhancement for Azure NetApp Files, now generally available on Premium and Ultra service levels, automatically adjusts throughput to optimize performance and cost for mixed hot and cool workloads, maintaining hot-tier performance as data transitions to cool storage.

---

### 27. Public Preview : Microsoft entra kerberos authentication for Azure NetApp Files   

**Published**: September 29, 2026 17:07:55 UTC
**Link**: [Public Preview : Microsoft entra kerberos authentication for Azure NetApp Files   ](https://azure.microsoft.com/updates?id=573041)

**Update ID**: 573041
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files, Feature

**Summary**:

- What was updated  
Azure NetApp Files now supports Microsoft Entra Kerberos authentication for SMB volumes in Public Preview.

- Key changes or new features  
This update enables users to authenticate to Azure NetApp Files SMB volumes using Microsoft Entra ID (formerly Azure AD) with cloud-issued Kerberos tickets. Both hybrid and cloud-only identities are supported, allowing seamless authentication without relying on traditional on-premises Active Directory. This simplifies identity management and enhances security for file shares in Azure.

- Target audience affected  
Developers and IT professionals managing Azure NetApp Files, especially those working with SMB volumes and requiring modern identity solutions. Organizations with hybrid or cloud-only environments looking to streamline authentication processes will benefit.

- Important notes  
This feature is currently in Public Preview and may not be suitable for production workloads. It removes the dependency on on-premises AD for SMB authentication, facilitating easier integration with cloud-native architectures. Review documentation for configuration steps and limitations before adoption.

**Details**:

**Azure Update Report: Public Preview – Microsoft Entra Kerberos Authentication for Azure NetApp Files**

**Background and Purpose of the Update**  
Azure NetApp Files is a high-performance, enterprise-grade file storage solution in Azure, commonly used for workloads requiring SMB protocol support. Traditionally, authentication for SMB volumes relied on on-premises Active Directory (AD) or Azure AD Domain Services. The introduction of Microsoft Entra Kerberos authentication addresses the growing need for secure, seamless authentication in hybrid and cloud-only environments. The purpose of this update is to enable users—regardless of whether their identities are managed on-premises or solely in the cloud—to authenticate to Azure NetApp Files SMB volumes using Microsoft Entra ID (formerly Azure AD), leveraging cloud-issued Kerberos tickets.

**Specific Features and Detailed Changes**  
- **Microsoft Entra Kerberos Authentication:** Azure NetApp Files now supports authentication for SMB volumes using Kerberos tickets issued by Microsoft Entra ID.  
- **Hybrid and Cloud-Only Identity Support:** Users with identities managed in hybrid (on-premises + cloud) or cloud-only environments can authenticate without dependency on traditional AD infrastructure.  
- **Public Preview Availability:** This feature is currently in public preview, allowing IT professionals to test and evaluate the integration in their environments.

**Technical Mechanisms and Implementation Methods**  
- **Kerberos Ticket Issuance:** When a user attempts to access an SMB volume hosted on Azure NetApp Files, Microsoft Entra ID issues a Kerberos ticket. This ticket is used to authenticate the user against the SMB volume, ensuring secure access.  
- **Cloud-Based Authentication Workflow:** The authentication process is managed entirely through Microsoft Entra ID, eliminating the need for on-premises domain controllers or Azure AD Domain Services.  
- **SMB Protocol Integration:** The SMB volumes are configured to accept Kerberos tickets from Microsoft Entra ID, ensuring compatibility and secure access.

**Use Cases and Application Scenarios**  
- **Cloud-Only Environments:** Organizations that have migrated their identity management to Microsoft Entra ID can now leverage Azure NetApp Files SMB volumes without deploying additional AD infrastructure.  
- **Hybrid Identity Scenarios:** Enterprises with both on-premises and cloud identities can provide seamless access to SMB volumes, simplifying authentication and reducing complexity.  
- **Lift-and-Shift Workloads:** Applications migrated to Azure that require SMB file shares can now use Microsoft Entra Kerberos authentication, streamlining integration with cloud identity services.

**Important Considerations and Limitations**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. IT professionals should evaluate and test thoroughly before widespread adoption.  
- **Supported Scenarios:** Only SMB volumes are supported for Microsoft Entra Kerberos authentication at this time.  
- **Identity Requirements:** Users must have identities managed in Microsoft Entra ID to utilize this feature.  
- **Potential Feature Gaps:** As with any preview feature, there may be limitations or missing functionality compared to GA releases.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** The update leverages Microsoft Entra ID for identity management and Kerberos ticket issuance, providing a unified authentication platform.  
- **Azure NetApp Files:** The integration enhances Azure NetApp Files by enabling modern authentication mechanisms for SMB volumes.  
- **Azure Security and Compliance:** By removing dependency on on-premises AD, organizations can streamline their security and compliance posture in Azure.

**Summary Sentence**  
Azure NetApp Files now supports Microsoft Entra Kerberos authentication for SMB volumes in public preview, enabling secure access for hybrid and cloud-only identities using cloud-issued Kerberos tickets through Microsoft Entra ID.

---


*This report was automatically generated - 2026-09-30 03:16:39 UTC*