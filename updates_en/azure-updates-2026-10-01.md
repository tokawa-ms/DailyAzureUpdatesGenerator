# October 01, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 01, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines 

**Published**: September 30, 2026 21:13:13 UTC
**Link**: [Public Preview: SQL performance monitoring for SQL Server on Azure Virtual Machines ](https://azure.microsoft.com/updates?id=571894)

**Update ID**: 571894
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Databases, SQL Server on Azure Virtual Machines, Feature

**Summary**:

- What was updated  
Microsoft has released a public preview of Microsoft-managed SQL performance monitoring for SQL Server running on Azure Virtual Machines.

- Key changes or new features  
This update introduces a built-in, managed solution for monitoring SQL Server performance on Azure VMs. Developers and IT professionals can now access performance telemetry without creating custom scripts or manually correlating data from multiple sources. The monitoring solution provides insights into SQL Server health, resource utilization, and performance metrics directly within the Azure portal.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who deploy and manage SQL Server workloads on Azure Virtual Machines.

- Important notes  
The feature is currently in public preview and may not be suitable for production workloads. Users can leverage this managed monitoring to streamline troubleshooting and optimize SQL Server performance, reducing operational overhead. No additional configuration is required beyond enabling the feature in the Azure portal. For more details and to participate in the preview, visit the official Azure Update page: https://azure.microsoft.com/updates?id=571894

**Details**:

**Comprehensive Technical Explanation of Azure Update: Public Preview – SQL Performance Monitoring for SQL Server on Azure Virtual Machines**

**Background and Purpose of the Update**  
Traditionally, monitoring SQL Server performance on Azure Virtual Machines (VMs) required IT professionals to develop custom scripts and manually correlate telemetry data from disparate sources. This process was labor-intensive and often led to gaps in visibility or delayed troubleshooting. The purpose of this update is to simplify and standardize SQL Server performance monitoring by introducing a Microsoft-managed solution, thereby reducing operational overhead and improving the reliability of monitoring workflows.

**Specific Features and Detailed Changes**  
The public preview introduces native, Microsoft-managed performance monitoring capabilities for SQL Server instances running on Azure VMs. Key features include:

- **Automated Telemetry Collection:** Performance data is collected automatically, eliminating the need for custom collection scripts.
- **Integrated Monitoring Experience:** Telemetry from SQL Server is correlated and presented in a unified manner, streamlining diagnostics and performance analysis.
- **No Manual Configuration Required:** The monitoring solution is managed by Microsoft, reducing the complexity of setup and ongoing maintenance.

**Technical Mechanisms and Implementation Methods**  
The monitoring solution leverages Azure’s built-in telemetry infrastructure to collect and aggregate performance metrics from SQL Server on Azure VMs. This is achieved through:

- **Microsoft-managed Agents:** These agents are deployed to the VM and configured to collect relevant SQL Server performance metrics.
- **Centralized Data Aggregation:** Collected telemetry is sent to Azure’s monitoring backend, where it is processed and made available for analysis.
- **Unified Dashboard:** Performance data is accessible through Azure’s monitoring interfaces, providing a consolidated view of SQL Server health and activity.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for:

- **Production Workloads:** Enterprises running mission-critical SQL Server workloads on Azure VMs can leverage automated monitoring for proactive performance management.
- **DevOps and Operations Teams:** Teams responsible for maintaining SQL Server environments can reduce manual effort and focus on higher-level optimization tasks.
- **Incident Response:** Faster access to correlated telemetry enables quicker root cause analysis and resolution of performance issues.

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for all production environments. Users should evaluate its reliability and completeness before widespread adoption.
- **Scope:** The monitoring solution is specifically designed for SQL Server on Azure VMs and may not support other database platforms or VM configurations.
- **Customization:** While the solution eliminates the need for custom scripts, it may not offer the same level of customization as bespoke monitoring setups.

**Integration with Related Azure Services**  
The Microsoft-managed performance monitoring integrates seamlessly with Azure’s broader monitoring ecosystem, including:

- **Azure Monitor:** Performance data can be visualized and analyzed alongside other Azure resources.
- **Azure Security and Compliance Tools:** Telemetry can be used to support security audits and compliance reporting.
- **Automation and Alerting:** Integration with Azure’s automation and alerting frameworks enables proactive response to performance anomalies.

**Summary Sentence**  
Microsoft has released a public preview of managed SQL Server performance monitoring for Azure Virtual Machines, enabling IT professionals to monitor SQL Server instances without custom scripts and providing a unified, automated telemetry experience.

---

### 2. Retirement: NVv3-series Azure Virtual Machines

**Published**: September 30, 2026 18:26:47 UTC
**Link**: [Retirement: NVv3-series Azure Virtual Machines](https://azure.microsoft.com/updates?id=573414)

**Update ID**: 573414
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft Azure announced the retirement of the NVv3-series Virtual Machines (VMs), specifically the Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3 VM sizes.

- Key changes or new features  
These NVv3-series VMs will be retired on September 30, 2026. After this date, any remaining NVv3-series VMs will be deallocated and no longer available for use. No new features are introduced; this is a deprecation notice.

- Target audience affected  
Developers and IT professionals who use NVv3-series VMs for GPU-accelerated workloads, including graphics rendering, visualization, and compute-intensive applications.

- Important notes if any  
Users must migrate workloads running on NVv3-series VMs to alternative Azure VM series before the retirement date to avoid service disruption. Microsoft recommends evaluating newer GPU-enabled VM series (such as NVv4, NC, ND, or other options) for migration. Planning and testing migrations ahead of the deadline is critical to ensure continuity and performance. For more details and migration guidance, refer to the official Azure update link: https://azure.microsoft.com/updates?id=573414

**Details**:

**Comprehensive Technical Explanation: Retirement of NVv3-series Azure Virtual Machines**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of the NVv3-series Virtual Machines (VMs) on September 30, 2026. This update specifically affects the following VM sizes: Standard_NV12s_v3, Standard_NV12hs_v3, Standard_NV24s_v3, Standard_NV24ms_v3, Standard_NV32ms_v3, and Standard_NV48s_v3. The purpose of this retirement is to phase out older GPU-accelerated VM offerings, likely to streamline the Azure VM portfolio and encourage migration to newer, more performant, and supported VM series.

**Specific Features and Detailed Changes**  
The NVv3-series VMs are GPU-enabled instances designed for visualization and compute workloads that benefit from hardware-accelerated graphics. The retirement impacts all remaining VMs in this series, meaning that after September 30, 2026, these VM sizes will no longer be available for deployment, and any existing instances will be decommissioned. Users will not be able to create, start, or resize NVv3-series VMs after this date.

**Technical Mechanisms and Implementation Methods**  
The retirement process will be enforced at the Azure platform level. Azure Resource Manager (ARM) will block the provisioning of new NVv3-series VMs and the resizing of existing VMs to these sizes after the retirement date. Any running NVv3-series VMs will be stopped and deallocated. Customers are expected to migrate workloads to alternative VM series before the cutoff date to avoid service disruption.

**Use Cases and Application Scenarios**  
NVv3-series VMs are typically used for scenarios requiring GPU acceleration, such as remote visualization, CAD applications, rendering, and other graphics-intensive workloads. Organizations leveraging these VMs for development, testing, or production workloads must identify suitable replacement VM series that offer equivalent or superior GPU capabilities.

**Important Considerations and Limitations**  
- All NVv3-series VMs will be retired on September 30, 2026, with no exceptions.
- After the retirement date, these VM sizes will be unavailable for all operations, including creation, resizing, and starting.
- Customers must proactively plan and execute migration strategies to supported VM series to prevent downtime or loss of service.
- Workloads dependent on the specific hardware or driver configurations of NVv3-series VMs may require validation and testing on the target VM series.

**Integration with Related Azure Services**  
NVv3-series VMs are often integrated with Azure services such as Azure Virtual Desktop, Azure Batch for rendering, and Azure Machine Learning for GPU-accelerated compute. Migration to newer VM series may require updates to integration configurations, driver installations, and validation of compatibility with these services. It is essential to review the documentation for the target VM series to ensure seamless integration and optimal performance.

**Summary Sentence**  
Microsoft Azure will retire the NVv3-series GPU-enabled Virtual Machines on September 30, 2026, requiring customers to migrate affected workloads to supported VM series to maintain service continuity and integration with related Azure services.

---

### 3. Retirement: NVv4-series Azure Virtual Machines

**Published**: September 30, 2026 18:24:01 UTC
**Link**: [Retirement: NVv4-series Azure Virtual Machines](https://azure.microsoft.com/updates?id=573415)

**Update ID**: 573415
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft Azure announced the retirement of the NVv4-series Virtual Machines (VMs), including Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Standard_NV32ahs_v4. The retirement date is September 30, 2026.

- Key changes or new features  
After September 30, 2026, these NVv4-series VMs will no longer be available for deployment, and existing instances will not be supported. Customers must migrate workloads to alternative VM series, such as NVadsA10 v5 or NVadsA10 v6, which offer improved performance and updated GPU capabilities.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently using NVv4-series VMs for GPU-accelerated workloads, including graphics, visualization, and compute-intensive applications.

- Important notes if any  
It is crucial to plan and execute migration strategies before the retirement date to avoid service disruption. Review your current VM usage, evaluate alternative VM series, and update deployment scripts and infrastructure accordingly. Microsoft recommends leveraging newer VM series for enhanced performance and support. For further guidance, refer to Azure’s documentation and migration tools.

**Details**:

**Azure Update Report: Retirement of NVv4-series Azure Virtual Machines**

**Background and Purpose of the Update:**  
Microsoft Azure has announced the retirement of the NVv4-series virtual machines (VMs), specifically the Standard_NV4as_v4, Standard_NV4ahs_v4, Standard_NV8as_v4, Standard_NV8ahs_v4, Standard_NV16as_v4, Standard_NV16ahs_v4, Standard_NV32as_v4, and Standard_NV32ahs_v4 SKUs. The retirement date is set for September 30, 2026. The purpose of this update is to notify users that these VM sizes will no longer be available after this date, as part of Azure’s ongoing efforts to streamline its VM offerings and to encourage migration to newer, supported VM series.

**Specific Features and Detailed Changes:**  
The NVv4-series VMs are GPU-enabled instances designed for graphics-intensive workloads, leveraging AMD Radeon Instinct MI25 GPUs with partitioning capabilities. The retirement affects all listed NVv4-series SKUs, which will be fully decommissioned and unavailable for provisioning or scaling after the specified date. Existing deployments must be migrated to alternative VM series before the retirement deadline to avoid service disruption.

**Technical Mechanisms and Implementation Methods:**  
After September 30, 2026, Azure will disable the ability to create, scale, or redeploy any of the affected NVv4-series VMs. Existing VMs of these types will be deallocated and removed from the platform, and any associated resources (such as managed disks or network interfaces) will need to be managed or migrated accordingly. Azure will likely provide migration tools or guidance to assist with transitioning workloads to supported GPU-enabled VM series, but users are responsible for planning and executing their migration strategies.

**Use Cases and Application Scenarios:**  
The NVv4-series VMs have been commonly used for virtual desktop infrastructure (VDI), remote visualization, CAD applications, and other GPU-accelerated workloads that benefit from partitioned GPU resources. Organizations using these VMs for Windows Virtual Desktop, graphics rendering, or GPU-accelerated computing must identify alternative VM series that meet their performance and compatibility requirements.

**Important Considerations and Limitations:**  
- After the retirement date, all affected NVv4-series VMs will be decommissioned, resulting in loss of service if workloads are not migrated.
- Users must review their current deployments and plan for migration to supported VM series well in advance of the retirement date.
- There may be differences in GPU architecture, performance characteristics, and pricing between NVv4-series and alternative VM types, requiring thorough testing and validation during migration.
- Any automation or scripts referencing these VM sizes will need to be updated to prevent deployment failures.

**Integration with Related Azure Services:**  
NVv4-series VMs are often integrated with services such as Azure Virtual Desktop, Azure Batch, and Azure Machine Learning for GPU-accelerated workloads. Migration to newer VM series may require updates to service configurations, scaling policies, and integration points to ensure continued compatibility and optimal performance.

**Summary Sentence:**  
Microsoft Azure will retire the NVv4-series virtual machines, including all listed SKUs, on September 30, 2026, requiring users to migrate affected GPU-enabled workloads to supported VM series to maintain service continuity.

---

### 4. Public Preview: Ubuntu 26.04 support in AKS

**Published**: September 30, 2026 17:11:11 UTC
**Link**: [Public Preview: Ubuntu 26.04 support in AKS](https://azure.microsoft.com/updates?id=573214)

**Update ID**: 573214
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now supports Ubuntu 26.04 (Ubuntu2604 OS SKU) in node pools, available in Public Preview.

- Key changes or new features  
AKS users can provision node pools using Ubuntu 26.04 Minimal, aligning with the latest Ubuntu LTS release. This update helps teams stay current with security patches and package updates. The Ubuntu Minimal image reduces the OS footprint, potentially improving performance and security. Developers and IT admins can test workloads for compatibility with Ubuntu 26.04 before general availability.

- Target audience affected  
AKS users managing Ubuntu-based node pools, including developers, DevOps engineers, and IT professionals responsible for Kubernetes cluster maintenance and security.

- Important notes if any  
Transitioning to Ubuntu 26.04 may introduce changes in package versions, security configurations, and compatibility. Teams should validate their workloads and dependencies on Ubuntu 26.04 before migrating production clusters. The update is currently in Public Preview, so production use is not recommended until General Availability. Review documentation for guidance on upgrading node pools and compatibility considerations.

**Details**:

**Azure Update Technical Explanation: Public Preview: Ubuntu 26.04 support in AKS**

**Background and Purpose of the Update:**  
Azure Kubernetes Service (AKS) enables organizations to run containerized workloads on managed Kubernetes clusters. Node pools in AKS are typically provisioned with specific operating system images, and many teams rely on Ubuntu Long Term Support (LTS) releases for their stability, security, and support lifecycle. As Ubuntu LTS versions reach end-of-life, it is critical for teams to migrate to newer releases to maintain security compliance and access to the latest features. This update introduces support for Ubuntu 26.04 in AKS node pools, allowing teams to stay current with the latest Ubuntu LTS offering.

**Specific Features and Detailed Changes:**  
- **Ubuntu 26.04 Support:** AKS now offers a new OS SKU, `Ubuntu2604`, based on Ubuntu Minimal 26.04, in public preview.
- **Node Pool Configuration:** Users can select the `Ubuntu2604` OS SKU when creating or upgrading AKS node pools.
- **Package Footprint:** The use of Ubuntu Minimal images reduces the base package footprint, which can improve security and performance by minimizing the attack surface and resource consumption.
- **Security and Compatibility:** By supporting the latest Ubuntu LTS, AKS ensures that node pools benefit from the most recent security patches, updated libraries, and improved compatibility with modern workloads.

**Technical Mechanisms and Implementation Methods:**  
- **OS SKU Selection:** During node pool creation or upgrade, users specify the desired OS SKU (`Ubuntu2604`). This triggers AKS to provision nodes using the Ubuntu Minimal 26.04 image.
- **Lifecycle Management:** The AKS platform manages the lifecycle of the Ubuntu 26.04 images, including updates and security patching, in alignment with Ubuntu’s LTS support policies.
- **Integration with Kubernetes:** The Ubuntu 26.04 image is validated for compatibility with supported Kubernetes versions in AKS, ensuring seamless operation of cluster workloads.

**Use Cases and Application Scenarios:**  
- **Security-First Workloads:** Organizations with strict security and compliance requirements can leverage the latest LTS image to ensure up-to-date security patches.
- **Modern Application Deployments:** Teams deploying applications that depend on recent versions of system libraries or tools included in Ubuntu 26.04 can benefit from this support.
- **Resource-Constrained Environments:** The minimal image footprint is advantageous for workloads where resource efficiency is a priority.

**Important Considerations and Limitations:**  
- **Preview Status:** Ubuntu 26.04 support is currently in public preview. Production workloads should consider the preview nature and associated support limitations.
- **Compatibility Testing:** Teams should validate application compatibility with Ubuntu 26.04 before migrating production workloads, as package versions and system behavior may differ from previous LTS releases.
- **Upgrade Planning:** Transitioning node pools to Ubuntu 26.04 may require updates to deployment scripts, container images, or runtime dependencies.

**Integration with Related Azure Services:**  
- **Azure Monitor and Security Center:** The new OS SKU integrates with Azure’s monitoring and security services, enabling visibility and compliance tracking for Ubuntu 26.04-based node pools.
- **AKS Features:** All standard AKS features, such as autoscaling, managed updates, and network integration, are available for node pools running Ubuntu 26.04.

**Summary Sentence:**  
Azure Kubernetes Service now offers public preview support for Ubuntu 26.04 Minimal as a node pool OS SKU, enabling teams to leverage the latest Ubuntu LTS features, enhanced security, and reduced package footprint in their AKS clusters.

---

### 5. Announcing: Azure canvases for GitHub Copilot

**Published**: September 30, 2026 17:09:51 UTC
**Link**: [Announcing: Azure canvases for GitHub Copilot](https://azure.microsoft.com/updates?id=573385)

**Update ID**: 573385
**Data source**: Azure Updates API

**Categories**: Management and governance, Azure Copilot, SDK and Tools, Announcement

**Summary**:

- What was updated  
Azure canvases for GitHub Copilot have been announced, introducing interactive shared workspaces integrated with Copilot.

- Key changes or new features  
Azure canvases provide a unified environment where developers and IT professionals can access Azure tools, dashboards, and guided workflows directly within their Copilot conversations. Users can explore Azure resources, analyze costs, and build hosted skills collaboratively. The canvases enable seamless context sharing, allowing teams to work together on Azure tasks without switching between multiple interfaces. Integration with GitHub Copilot means AI-driven assistance is available throughout the workspace, enhancing productivity and decision-making.

- Target audience affected  
Developers, DevOps engineers, and IT professionals who use Azure and GitHub Copilot for cloud resource management, cost analysis, and workflow automation.

- Important notes if any  
Azure canvases aim to streamline cloud operations and development by combining Copilot’s AI capabilities with Azure’s management tools in a single workspace. This feature is designed to improve collaboration, reduce context switching, and accelerate cloud project workflows. Early adopters should review documentation for integration steps and supported scenarios.

**Details**:

**Azure Update Technical Report**

**Title:** Announcing: Azure canvases for GitHub Copilot  
**Source:** [Azure Update Link](https://azure.microsoft.com/updates?id=573385)

---

### Background and Purpose of the Update

Azure canvases for GitHub Copilot are introduced to enhance the developer and IT professional experience by providing interactive, shared workspaces. The primary purpose is to seamlessly integrate Azure tools, dashboards, and guided workflows directly within the Copilot environment, enabling users to interact with Azure resources and workflows without context switching. This aims to streamline collaboration, resource management, and automation tasks by leveraging the conversational interface of GitHub Copilot.

---

### Specific Features and Detailed Changes

- **Interactive Shared Workspaces:** Azure canvases create collaborative environments where multiple users can interact with Azure resources and tools in real time.
- **Embedded Azure Tools and Dashboards:** Users can access and manipulate Azure dashboards and tools directly within the canvas, providing a unified interface for resource management and monitoring.
- **Guided Workflows:** The update introduces step-by-step workflows that guide users through common Azure tasks, reducing the learning curve and improving operational efficiency.
- **Copilot Integration:** All features are accessible alongside GitHub Copilot conversations, allowing users to ask questions, receive suggestions, and execute tasks contextually.
- **Cost Analysis and Resource Exploration:** Users can analyze Azure costs and explore resources interactively, supporting better financial and operational decision-making.
- **Hosted Skills Building:** The canvas allows users to build and deploy hosted skills (custom automations or scripts) directly within the workspace.

---

### Technical Mechanisms and Implementation Methods

Azure canvases operate as interactive layers within the GitHub Copilot environment. They leverage Azure APIs and service endpoints to fetch, display, and manipulate resource data in real time. The integration is designed to be context-aware, enabling Copilot to provide relevant suggestions and automate workflows based on the current canvas activity. The shared workspace model supports concurrent collaboration, with changes and insights reflected instantly for all participants.

---

### Use Cases and Application Scenarios

- **DevOps Collaboration:** Teams can collaboratively manage infrastructure, monitor deployments, and troubleshoot issues using shared dashboards and guided workflows.
- **Cost Management:** Financial analysts and engineers can jointly analyze Azure spending, identify cost drivers, and optimize resource usage in real time.
- **Skill Development and Automation:** Developers can build, test, and deploy hosted skills (e.g., automation scripts or custom integrations) directly from the canvas, accelerating development cycles.
- **Onboarding and Training:** New team members can follow guided workflows to learn Azure operations, supported by Copilot’s conversational assistance.

---

### Important Considerations and Limitations

- **Access Control:** Ensure appropriate permissions are configured for users accessing shared canvases to prevent unauthorized resource manipulation.
- **Data Privacy:** Sensitive information displayed or manipulated within the canvas should be protected according to organizational policies.
- **Feature Scope:** The current update highlights integration with Azure tools, dashboards, and workflows; advanced or custom integrations may require additional configuration.
- **Performance:** Real-time collaboration and resource manipulation depend on network connectivity and Azure service availability.

---

### Integration with Related Azure Services

Azure canvases are tightly integrated with core Azure services, including resource management APIs, cost analysis tools, and automation frameworks. They also leverage GitHub Copilot’s conversational AI to enhance productivity and streamline workflow execution. This integration ensures that users can manage, monitor, and automate Azure resources without leaving the collaborative Copilot environment.

---

**Summary Sentence:**  
Azure canvases for GitHub Copilot provide interactive, shared workspaces that integrate Azure tools, dashboards, and guided workflows directly alongside Copilot conversations, enabling collaborative resource management, cost analysis, and skill building within a unified environment.

---

### 6. Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs 

**Published**: September 30, 2026 17:07:30 UTC
**Link**: [Retirement: Dv3, Dsv3, Ev3, and Esv3 Azure VMs ](https://azure.microsoft.com/updates?id=572346)

**Update ID**: 572346
**Data source**: Azure Updates API

**Categories**: Compute, Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft has announced the retirement of the Dv3, Dsv3, Ev3, and Esv3 Azure VM series in public cloud Azure regions.

- Key changes or new features  
These VM series will reach End-of-Life and be fully retired on November 15, 2029. After this date, these VM types will no longer be available for deployment or scaling operations. Existing workloads must be migrated to newer VM series before the retirement deadline.

- Target audience affected  
This update impacts developers, IT professionals, and cloud architects who currently use Dv3, Dsv3, Ev3, or Esv3 VM series for their applications, services, or infrastructure in Azure public cloud regions.

- Important notes  
Microsoft recommends planning migrations to newer VM series (such as Dv4/Dv5, Ev4/Ev5, etc.) to ensure continued support and optimal performance. Review your current deployments and update automation scripts, templates, and scaling policies accordingly. Early migration is advised to avoid service disruption and to leverage improved features and performance from newer VM families. For further details and migration guidance, refer to the official Azure documentation and the retirement announcement.

**Details**:

**Azure Update: Retirement of Dv3, Dsv3, Ev3, and Esv3 Azure VM Series**

**Background and Purpose of the Update**  
Microsoft has announced the planned retirement of the Dv3, Dsv3, Ev3, and Esv3 series of Azure Virtual Machines (VMs) in public cloud Azure regions. This action is part of the standard Azure VM lifecycle policy, which ensures that Azure’s compute offerings remain current, secure, and optimized for performance. The retirement date for these VM series is set for November 15, 2029. The purpose of this update is to inform customers and IT professionals about the end-of-life (EOL) timeline, so they can plan migrations and avoid service disruptions.

**Specific Features and Detailed Changes**  
The affected VM series—Dv3, Dsv3, Ev3, and Esv3—will no longer be available for deployment or scaling operations after the retirement date. These VM families are based on earlier hardware generations and may lack the latest advancements in CPU, memory, and storage technologies. The retirement means that:

- No new deployments or scaling of these VM types will be possible after November 15, 2029.
- Existing instances may need to be migrated to newer VM series before the EOL date to ensure continued support and access to security updates.

**Technical Mechanisms and Implementation Methods**  
The retirement process is governed by Azure’s VM lifecycle management. When a VM series reaches EOL, Azure disables the ability to create new instances or scale existing deployments using those SKUs. Customers are expected to proactively migrate workloads to supported VM series. Azure provides migration tools and documentation to facilitate this process, but the technical migration itself typically involves:

- Assessing current deployments of Dv3, Dsv3, Ev3, and Esv3 VMs.
- Selecting appropriate replacement VM series (such as Dv4, Dsv4, Ev4, Esv4, or newer).
- Testing compatibility and performance on new VM types.
- Scheduling and executing migration activities before the retirement deadline.

**Use Cases and Application Scenarios**  
The Dv3 and Ev3 VM series have been widely used for general-purpose and memory-optimized workloads, respectively. Common scenarios include hosting enterprise applications, databases, development/test environments, and other compute-intensive tasks. Organizations using these VMs in production, staging, or test environments must plan to transition to newer VM series to maintain service continuity.

**Important Considerations and Limitations**  
- After November 15, 2029, no support or security updates will be provided for the retired VM series.
- Workloads running on these VMs must be migrated before the EOL date to avoid service interruptions.
- There may be differences in hardware, performance characteristics, and pricing between the retired and replacement VM series, which should be evaluated during migration planning.
- Automation scripts, templates, or infrastructure-as-code (IaC) definitions referencing the retired VM SKUs will require updates.

**Integration with Related Azure Services**  
These VM series are integrated with a wide range of Azure services, including Azure Virtual Networks, Managed Disks, Azure Backup, and monitoring solutions. Migration to newer VM series should be validated for compatibility with all dependent services and configurations. Azure’s migration tools and best practices can help ensure a smooth transition with minimal impact on service integrations.

**Summary:**  
Microsoft is retiring the Dv3, Dsv3, Ev3, and Esv3 Azure VM series in public cloud regions, with end-of-life scheduled for November 15, 2029; customers must plan to migrate workloads to supported VM series before this date to maintain support and service continuity.

---

### 7. Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028

**Published**: September 30, 2026 16:18:26 UTC
**Link**: [Retirement: Transition to using standard tests for single-step availability testing in Azure Monitor application insights by September 30, 2028](https://azure.microsoft.com/updates?id=transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september)

**Update ID**: transition-to-using-standard-tests-for-singlestep-availability-testing-in-azure-monitor-application-insights-by-30-september
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Application Insights, Azure Monitor, Retirements

**Summary**:

- What was updated  
The retirement date for URL ping tests in Azure Monitor Application Insights has been extended. Originally planned for September 30, 2026, the new retirement date is now September 30, 2028.

- Key changes or new features  
Developers and IT professionals must transition from legacy URL ping tests to standard tests for single-step availability monitoring in Application Insights. Standard tests provide enhanced monitoring capabilities and are the recommended approach moving forward. The extension gives organizations an additional 24 months to complete their migration.

- Target audience affected  
This update impacts developers, IT professionals, and Azure administrators who use Application Insights for availability monitoring, specifically those relying on URL ping tests.

- Important notes if any  
After September 30, 2028, URL ping tests will no longer be supported or available in Application Insights. Organizations should plan and execute their migration to standard tests well before this deadline to avoid disruption in monitoring workflows. Microsoft recommends reviewing documentation and updating monitoring strategies to leverage the improved features of standard tests. No immediate action is required, but early migration is encouraged to ensure continuity and take advantage of enhanced functionality.

**Details**:

**Azure Update Report: Retirement of URL Ping Tests in Application Insights and Transition to Standard Tests for Single-Step Availability Testing by September 30, 2028**

**Background and Purpose of the Update**  
Azure Monitor Application Insights has historically provided URL ping tests as a method for single-step availability monitoring. These tests allow users to verify the availability of web endpoints by sending HTTP requests and checking for successful responses. Originally, Microsoft announced the retirement of URL ping tests for September 30, 2026. However, based on customer feedback requesting additional time for migration, the retirement date has been extended by 24 months to September 30, 2028. The purpose of this update is to encourage customers to transition to standard tests for single-step availability monitoring, which offer improved functionality and alignment with Azure’s evolving monitoring capabilities.

**Specific Features and Detailed Changes**  
The core change is the deprecation of URL ping tests in Application Insights. After September 30, 2028, URL ping tests will no longer be supported or available. Users are required to migrate to standard tests for single-step availability monitoring. Standard tests provide enhanced features compared to legacy URL ping tests, including more robust configuration options, improved reliability, and better integration with Azure Monitor’s broader ecosystem.

**Technical Mechanisms and Implementation Methods**  
URL ping tests operate by periodically sending HTTP GET requests to specified endpoints and evaluating the response for availability and latency. Standard tests, which will replace URL ping tests, are implemented within the Azure Monitor Application Insights framework. They offer more granular control over test parameters, support for additional HTTP methods, and advanced validation criteria. Migration involves reconfiguring existing availability monitoring setups to use standard tests instead of URL ping tests. This can be accomplished through the Azure portal, ARM templates, or programmatically via Azure Monitor APIs.

**Use Cases and Application Scenarios**  
Typical use cases for single-step availability testing include monitoring the uptime of public-facing web applications, APIs, and service endpoints. Organizations leverage these tests to ensure critical services are accessible and to receive alerts in case of outages or performance degradation. Standard tests are suitable for scenarios requiring more flexible monitoring configurations, such as custom headers, authentication, or advanced response validation, which are increasingly necessary in modern cloud architectures.

**Important Considerations and Limitations**  
IT professionals must note the extended retirement date of September 30, 2028, and plan migration activities accordingly. After this date, URL ping tests will cease to function, potentially leaving monitored endpoints unprotected if migration is not completed. It is essential to review existing monitoring configurations, identify dependencies on URL ping tests, and transition to standard tests well in advance. There may be differences in configuration and operational behavior between URL ping tests and standard tests, so thorough testing is recommended during migration.

**Integration with Related Azure Services**  
Standard tests in Application Insights integrate seamlessly with other Azure Monitor features, such as alerting, dashboards, and log analytics. This enables unified monitoring, reporting, and incident management across Azure resources. Standard tests also support integration with Azure Resource Manager for automated deployments and with Azure DevOps for continuous monitoring in CI/CD pipelines.

**Summary Sentence**  
The retirement of URL ping tests in Azure Monitor Application Insights has been extended to September 30, 2028, requiring users to migrate to standard tests for single-step availability monitoring to ensure continued and enhanced endpoint monitoring capabilities.

---


*This report was automatically generated - 2026-10-01 03:04:57 UTC*