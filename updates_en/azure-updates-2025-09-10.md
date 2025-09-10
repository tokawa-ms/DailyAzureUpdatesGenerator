# September 10, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 10, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Private Preview: Azure AMD-based Dasv7, Easv7, and Fasv7-series Virtual Machines

**Published**: September 09, 2025 20:45:15 UTC
**Link**: [Private Preview: Azure AMD-based Dasv7, Easv7, and Fasv7-series Virtual Machines](https://azure.microsoft.com/updates?id=500175)

**Update ID**: 500175
**Data source**: Azure Updates API

**Categories**: In development, Compute, Linux Virtual Machines, Windows Virtual Machines, Pricing & Offerings, Services

**Summary**:

- What was updated  
Azure has introduced a private preview of new AMD-based virtual machines: Dasv7 and Dalsv7 (general purpose), Easv7 (memory-optimized), and Fasv7, Falsv7, Famsv7 (compute-optimized). These VM series come with options for local disk support or without it.

- Key changes or new features  
These VM families leverage AMD processors to provide cost-effective and performant compute options across general purpose, memory-optimized, and compute-optimized workloads. The preview includes availability in three Azure regions: East US 2, North Europe, and West US 3. The inclusion of local disk support offers flexibility for scenarios requiring temporary storage.

- Target audience affected  
Developers and IT professionals looking for AMD-based VM options for diverse workload needs, including general compute, memory-intensive applications, and compute-heavy tasks. This is particularly relevant for those aiming to optimize cost and performance or test AMD VM capabilities in preview.

- Important notes if any  
This offering is currently in private preview, so access requires enrollment and approval. Availability is limited to specific regions. Users should evaluate workload compatibility with AMD architecture and preview limitations before production use. Further updates will follow as the preview progresses.  

Reference: https://azure.microsoft.com/updates?id=500175

**Details**:

The recent Azure update announces the private preview availability of AMD-based Dasv7, Easv7, and Fasv7-series virtual machines (VMs), expanding Azure’s VM portfolio with new general-purpose, memory-optimized, and compute-optimized options that support configurations both with and without local disk storage, currently accessible in East US 2, North Europe, and West US 3 regions.

**Background and Purpose:**  
This update addresses the growing demand for diversified VM options that leverage AMD’s latest EPYC processors, providing enhanced performance and cost-efficiency compared to previous generations. By introducing Dasv7 (general purpose), Easv7 (memory-optimized), and Fasv7 (compute-optimized) series, Azure aims to offer customers more tailored VM choices that balance CPU, memory, and storage performance for varied workloads, while also enabling local disk configurations for scenarios requiring ephemeral storage.

**Specific Features and Changes:**  
- **VM Series:**  
  - *Dasv7 and Dalsv7*: General-purpose VMs suitable for balanced CPU-to-memory workloads.  
  - *Easv7*: Memory-optimized VMs designed for high memory throughput and capacity, ideal for in-memory analytics and databases.  
  - *Fasv7, Falsv7, Famsv7*: Compute-optimized VMs targeting CPU-intensive applications such as batch processing, gaming, and high-performance computing (HPC).  
- **Local Disk Support:** These VMs can be provisioned with or without local ephemeral storage, providing flexibility for workloads that benefit from low-latency temporary storage.  
- **Regions:** Currently available in private preview in East US 2, North Europe, and West US 3, enabling regional testing and validation.

**Technical Mechanisms and Implementation:**  
These VM series utilize AMD EPYC 7003 series processors, offering up to 64 vCPUs per VM with improved instructions per cycle (IPC) and energy efficiency. The local disk support leverages NVMe-based ephemeral storage directly attached to the host hardware, providing high IOPS and low latency but without data persistence after VM deallocation or shutdown. Azure’s underlying hypervisor and resource scheduler manage these VMs, ensuring isolation, security, and performance consistency. Integration with Azure Resource Manager (ARM) templates and Azure CLI/PowerShell allows automated provisioning and configuration.

**Use Cases and Application Scenarios:**  
- *Dasv7/Dalsv7*: Web servers, small to medium databases, development and test environments requiring balanced compute and memory.  
- *Easv7*: Large-scale in-memory databases (e.g., SAP HANA), real-time analytics, and caching layers.  
- *Fasv7/Falsv7/Famsv7*: CPU-bound workloads such as video encoding, scientific simulations, gaming servers, and HPC tasks.  
- Local disk-enabled VMs are suitable for temporary data processing, caching, or scratch space where data persistence is not critical.

**Important Considerations and Limitations:**  
- As a private preview, access is limited and requires registration or invitation from Microsoft.  
- Local ephemeral disks do not persist data through VM deallocation or host maintenance; customers must architect for data durability accordingly.  
- Availability is currently restricted to specific regions, which may impact deployment strategies.  
- Pricing and SLA details are subject to change upon general availability.  
- Compatibility with existing Azure services and VM extensions should be validated during preview.

**Integration with Related Azure Services:**  
These VMs integrate seamlessly with Azure Virtual Network, Azure Load Balancer, and Azure Monitor for networking, scaling, and telemetry. They support Azure Disk Storage for persistent data needs alongside local ephemeral disks. Azure Backup and Azure Site Recovery can be used for data protection, although ephemeral disks require special handling. Additionally, these VMs can be orchestrated via Azure Kubernetes Service (AKS) or Azure Batch for containerized or batch workloads, respectively, leveraging the compute and

---

### 2. Generally Available: Multitenant Managed Logging in Container Insights

**Published**: September 09, 2025 16:30:49 UTC
**Link**: [Generally Available: Multitenant Managed Logging in Container Insights](https://azure.microsoft.com/updates?id=502561)

**Update ID**: 502561
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features, Management

**Summary**:

- What was updated  
The Multitenant Managed Logging feature in Azure Monitor Container Insights for AKS clusters is now generally available.

- Key changes or new features  
This update enables customers running shared Azure Kubernetes Service (AKS) clusters to segregate container logs by team or tenant. Each team can independently manage and access their own logs without interference, improving security and operational efficiency. The feature supports multitenant environments by isolating log data, simplifying troubleshooting and monitoring for each team.  

- Target audience affected  
Developers and IT professionals managing shared or multitenant AKS clusters who need granular log segregation and access control. This is especially relevant for organizations with multiple teams or departments sharing the same AKS infrastructure.

- Important notes if any  
The feature requires configuration within Container Insights and may involve role-based access control (RBAC) adjustments to enforce log access segregation. Users should review their logging and monitoring setup to leverage this capability fully. This GA release ensures production readiness and Microsoft support.  

For more details, visit: https://azure.microsoft.com/updates?id=502561

**Details**:

The recent general availability of Multitenant Managed Logging in Azure Monitor Container Insights addresses a critical need for organizations operating shared Azure Kubernetes Service (AKS) clusters by enabling secure and efficient segregation of container logs at the team level. Traditionally, Container Insights aggregates logs from all containers within an AKS cluster into a single workspace, which can complicate log management, access control, and compliance in multiteam or multidepartment environments. This update introduces a structured approach to isolate and manage logs per tenant or team, enhancing operational security and governance.

**Background and Purpose**  
As enterprises increasingly adopt shared AKS clusters to optimize resource utilization and reduce operational overhead, the challenge of providing isolated observability data to multiple teams without cross-access arises. Prior to this update, teams had to rely on complex query filters or separate workspaces per cluster, which could be inefficient and costly. The Multitenant Managed Logging feature is designed to simplify this by enabling native support for multitenancy within a single Container Insights workspace, facilitating granular log segregation and access control.

**Specific Features and Detailed Changes**  
- **Tenant-aware log segregation:** Logs from containers are tagged with tenant or team identifiers, allowing queries and dashboards to be scoped accordingly.  
- **Role-based access control (RBAC) integration:** Access to logs is enforced via Azure RBAC, ensuring that teams can only view and manage their own logs.  
- **Centralized management:** Administrators can configure and monitor logging policies for multiple tenants from a single pane of glass without deploying separate monitoring stacks.  
- **Support for multiple data streams:** The system supports segregating logs not only by namespaces but also by labels or annotations that define tenant boundaries.  

**Technical Mechanisms and Implementation Methods**  
Under the hood, Container Insights leverages Azure Monitor Logs and Log Analytics workspaces. The multitenant feature extends the existing data collection pipeline by injecting tenant metadata into the log records at ingestion time. This is typically achieved by configuring the Azure Monitor Container Insights agent (based on the Azure Monitor for containers solution) to recognize tenant identifiers from Kubernetes metadata such as namespaces, labels, or annotations. The logs are then indexed with these tenant tags, enabling scoped queries. Azure RBAC policies are applied at the workspace or resource level to restrict access, and Azure Monitor workbooks and alerts can be customized per tenant.

**Use Cases and Application Scenarios**  
- **Shared AKS clusters in large organizations:** Different business units or development teams share a cluster but require isolated logging for compliance and troubleshooting.  
- **Managed service providers (MSPs):** MSPs hosting AKS clusters for multiple customers can segregate logs to ensure data privacy and simplify billing and support.  
- **DevOps teams:** Enable team-specific dashboards and alerts without exposing logs from other teams, improving operational efficiency and security.  

**Important Considerations and Limitations**  
- The feature requires proper tagging and labeling of Kubernetes resources to accurately identify tenants. Misconfiguration can lead to incorrect log segregation.  
- RBAC policies must be carefully designed to avoid privilege escalation or unintended access.  
- While multitenant logging reduces the need for multiple workspaces, very large clusters with complex tenant structures may still require additional scaling considerations.  
- This feature currently supports AKS clusters monitored via Azure Monitor Container Insights; on-premises or other Kubernetes distributions may not be supported.  

**Integration with Related Azure Services**  
- **Azure Monitor Logs and Log Analytics:** The core platform for log ingestion, storage, and querying.  
- **Azure RBAC:** Enforces access control policies on logs and monitoring data.  
- **Azure Policy:** Can be used to enforce tagging standards and monitor compliance for tenant identification.  
- **Azure Monitor Workbooks and Alerts:** Provide tenant-scoped visualization and alerting capabilities.  
- **Azure Arc:** For hybrid environments, integration may be considered for future enhancements.  

In summary, the general availability of Multitenant Managed Logging in Container Insights significantly enhances

---

### 3. Retirement: Microsoft Playwright Testing (Preview) will be retired on March 8, 2026

**Published**: September 09, 2025 11:15:09 UTC
**Link**: [Retirement: Microsoft Playwright Testing (Preview) will be retired on March 8, 2026](https://azure.microsoft.com/updates?id=499860)

**Update ID**: 499860
**Data source**: Azure Updates API

**Categories**: Developer tools, DevOps, Web, Microsoft Playwright Testing, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Microsoft Playwright Testing (Preview) within Azure App Testing, effective March 8, 2026.

- Key changes or new features  
Azure App Testing initially combined Azure Load Testing and Microsoft Playwright Testing to provide unified functional and performance testing capabilities. With this update, the Playwright Testing preview will be discontinued, while Azure Load Testing continues as a standalone service. Developers and QA teams will need to transition away from Playwright Testing in Azure App Testing before the retirement date.

- Target audience affected  
Developers, QA engineers, and IT professionals who use Azure App Testing for browser-based functional testing with Microsoft Playwright will be impacted. Those relying on Playwright Testing in Azure for automated UI testing should plan migration strategies.

- Important notes if any  
The retirement is scheduled well in advance (March 8, 2026), allowing ample time for customers to adapt. Users should review their testing workflows and consider alternative Playwright testing solutions outside Azure App Testing or other Azure services. Azure Load Testing remains supported for performance testing needs. For more details, refer to the official Azure update link.

**Details**:

The announced retirement of Microsoft Playwright Testing (Preview) on March 8, 2026, reflects Microsoft’s strategic consolidation of testing services under the unified Azure App Testing platform, which integrates Azure Load Testing and Playwright Testing to streamline functional and performance testing workflows. This update aims to simplify and enhance the developer and QA experience by providing a single, cohesive service for large-scale testing scenarios.

**Background and Purpose:**  
Microsoft Playwright Testing (Preview) was introduced to offer developers and QA teams a cloud-based solution for automated browser testing using the Playwright framework, enabling cross-browser functional testing at scale. However, with the launch of Azure App Testing, Microsoft sought to unify testing capabilities, combining load and functional testing into one service to reduce fragmentation, improve usability, and provide a more integrated testing ecosystem. The retirement announcement signals the full transition towards Azure App Testing as the primary testing platform.

**Specific Features and Detailed Changes:**  
- **Retirement Date:** Microsoft Playwright Testing (Preview) will be officially retired on March 8, 2026.  
- **Service Consolidation:** Existing Playwright Testing capabilities are now available within Azure App Testing, which supports both functional testing (via Playwright scripts) and performance/load testing.  
- **Migration Path:** Users are encouraged to migrate their Playwright test scripts and workflows to Azure App Testing to continue leveraging cloud-based browser testing with enhanced management, scalability, and integration features.  
- **Deprecation of Standalone Playwright Testing:** Post-retirement, the standalone Playwright Testing service will no longer be available, and all testing activities should be conducted through Azure App Testing.

**Technical Mechanisms and Implementation Methods:**  
Azure App Testing supports Playwright scripts by allowing users to upload or author test scripts that run across multiple browsers and devices in the cloud. The service manages infrastructure provisioning, test execution, and result aggregation. It leverages containerized browser instances and scalable compute resources to run tests in parallel, enabling large-scale functional testing. Integration with Azure DevOps and GitHub Actions facilitates CI/CD pipeline incorporation. The unified service also provides detailed analytics, logs, and failure diagnostics to aid in troubleshooting.

**Use Cases and Application Scenarios:**  
- **Cross-Browser Functional Testing:** Validate web application behavior across Chromium, Firefox, and WebKit browsers at scale.  
- **Regression Testing:** Automate repeated test suites during development cycles to catch UI regressions early.  
- **Performance and Load Testing Integration:** Combine functional tests with load testing scenarios to assess application behavior under stress.  
- **CI/CD Pipelines:** Integrate automated Playwright tests into continuous integration and deployment workflows for rapid feedback.  
- **QA Team Collaboration:** Centralize test management and reporting within Azure App Testing for improved team visibility.

**Important Considerations and Limitations:**  
- **Migration Planning:** Organizations using the standalone Playwright Testing Preview must plan migration well before the retirement date to avoid disruption.  
- **Feature Parity:** While Azure App Testing includes Playwright Testing capabilities, users should verify that all specific features and customizations are supported post-migration.  
- **Cost Implications:** Consolidation may affect pricing models; users should review Azure App Testing pricing to understand cost impacts.  
- **Preview Status:** As Playwright Testing was in preview, some features might have evolved; Azure App Testing represents the production-ready environment.  
- **Deprecation Impact:** Scripts and integrations relying on the standalone service will require updates to target Azure App Testing endpoints and APIs.

**Integration with Related Azure Services:**  
Azure App Testing integrates seamlessly with Azure DevOps, GitHub Actions, and Azure Monitor, enabling automated test execution within CI/CD pipelines and centralized monitoring of application health. It also complements Azure Load Testing by allowing combined functional and performance testing strategies. Integration with Azure Application Insights provides telemetry correlation between test results and application performance metrics, enhancing root cause analysis.

In summary, the retirement of Microsoft Playwright Testing (Preview) on March 8

---


*This report was automatically generated - 2025-09-10 03:01:58 UTC*