# April 29, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 29, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Public Preview: Memory in Foundry Agent Service 

**Published**: April 29, 2026 00:00:55 UTC
**Link**: [Public Preview: Memory in Foundry Agent Service ](https://azure.microsoft.com/updates?id=560992)

**Update ID**: 560992
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features

**Summary**:

- What was updated  
The Foundry Agent Service now offers a public preview of its integrated "memory" feature—a managed long-term memory capability.

- Key changes or new features  
  - Foundry’s memory is now natively built into the Agent Service, eliminating the need for external databases for long-term memory storage.  
  - Native integration with Microsoft Agent Framework and LangGraph enables seamless use of memory in agent workflows.  
  - No additional provisioning, scaling, or security management is required for external memory stores.

- Target audience affected  
  - Developers building AI agents or applications using Foundry Agent Service, Microsoft Agent Framework, or LangGraph.  
  - IT professionals responsible for managing agent infrastructure and security.

- Important notes if any  
  - This feature is currently in public preview and may not be suitable for production workloads.  
  - The integrated memory simplifies architecture and reduces operational overhead, but users should review preview limitations and monitor for updates before full adoption.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=560992

**Details**:

**Azure Update Report: Public Preview – Memory in Foundry Agent Service**

**Background and Purpose of the Update**  
The introduction of memory (preview) in Foundry Agent Service addresses the need for managed, long-term memory capabilities within agent-based applications. Traditionally, implementing persistent memory for conversational or agent workflows required provisioning and managing external databases, which introduced additional operational overhead, complexity, and security considerations. This update aims to streamline the development and deployment of intelligent agents by embedding memory management directly into the Foundry Agent Service, thereby reducing infrastructure dependencies and simplifying the architecture.

**Specific Features and Detailed Changes**  
- **Managed Long-Term Memory:** The new memory feature is a fully managed, persistent memory store built into the Foundry Agent Service.  
- **Native Integration:** Memory now integrates natively with both the Microsoft Agent Framework and LangGraph, eliminating the need for external database configuration or management.  
- **No External Database Required:** Developers no longer need to provision, scale, or secure separate database services for agent memory, as all memory operations are handled within the Foundry Agent Service environment.

**Technical Mechanisms and Implementation Methods**  
- **Embedded Memory Store:** The memory capability is implemented as a native component of the Foundry Agent Service. This means that memory operations (such as storing, retrieving, and updating conversational or agent state) are handled internally by the service itself.  
- **Integration Points:** Through direct integration with Microsoft Agent Framework and LangGraph, agents can leverage memory functions via standard APIs or SDKs provided by these frameworks, ensuring seamless access and management of persistent state.  
- **Managed Service Model:** As a managed feature, memory benefits from the scalability, reliability, and security controls inherent to Azure-managed services, without requiring manual intervention for capacity planning or maintenance.

**Use Cases and Application Scenarios**  
- **Conversational AI Agents:** Agents that require context retention across sessions, such as chatbots or virtual assistants, can use the built-in memory to recall previous interactions, user preferences, or historical data.  
- **Workflow Automation:** Agents orchestrating multi-step business processes can persist workflow state and intermediate results without relying on external storage.  
- **Personalization:** Applications that tailor responses or actions based on long-term user behavior or history can leverage the native memory for efficient state management.

**Important Considerations and Limitations**  
- **Preview Status:** The memory feature is currently in public preview, which may imply limited support, potential changes to APIs, or evolving feature sets.  
- **No External Database Integration:** While simplifying architecture, this approach may not be suitable for scenarios requiring advanced database features, custom scaling, or integration with existing enterprise data stores.  
- **Security and Compliance:** As memory is managed within the Foundry Agent Service, organizations should review Azure’s security and compliance documentation to ensure alignment with their requirements.

**Integration with Related Azure Services**  
- **Microsoft Agent Framework:** Native memory integration allows agents built on this framework to persist and retrieve state without external dependencies.  
- **LangGraph:** Developers using LangGraph for agent orchestration can utilize the memory feature directly, streamlining state management within their workflows.  
- **Azure Security and Management:** As a managed service, memory benefits from Azure’s built-in security, monitoring, and compliance capabilities, simplifying operational oversight.

**Summary Sentence**  
The public preview of memory in Foundry Agent Service introduces a managed, natively integrated long-term memory capability for agent applications, eliminating the need for external databases and simplifying persistent state management within the Microsoft Agent Framework and LangGraph environments.

---

### 2. Public Preview: Container Network Insights Agent

**Published**: April 28, 2026 21:30:30 UTC
**Link**: [Public Preview: Container Network Insights Agent](https://azure.microsoft.com/updates?id=561020)

**Update ID**: 561020
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure has released the Container Network Insights Agent in Public Preview. This tool is designed to simplify and accelerate troubleshooting of Kubernetes networking issues.

- Key changes or new features  
  - Introduction of a lightweight, web-based agent for Kubernetes clusters.
  - Centralized collection and visualization of network logs and metrics, reducing the need to manually correlate data from multiple sources.
  - Enhanced troubleshooting capabilities for common networking issues such as connectivity failures, DNS resolution problems, and network policy enforcement.
  - Integration with Azure Monitor for seamless monitoring and diagnostics.

- Target audience affected  
  - Kubernetes developers and DevOps engineers managing containerized workloads on Azure Kubernetes Service (AKS).
  - IT professionals responsible for cluster networking, monitoring, and incident response.

- Important notes if any  
  - The agent is currently in Public Preview and may not be suitable for production workloads.
  - Deployment and usage instructions are available in the Azure documentation.
  - Feedback from early adopters is encouraged to help improve the tool before general availability.

For more details, visit the official [Azure Update page](https://azure.microsoft.com/updates?id=561020).

**Details**:

**Azure Update Report: Public Preview – Container Network Insights Agent**

**Background and Purpose of the Update**  
Kubernetes networking issues are complex to troubleshoot due to the dispersion of logs and metrics across multiple monitoring tools. This fragmentation forces engineers to manually correlate disparate signals during incidents, resulting in slower root cause analysis and increased mean time to resolution (MTTR). The introduction of the Container Network Insights Agent aims to address these challenges by centralizing and streamlining network diagnostics for Kubernetes environments.

**Specific Features and Detailed Changes**  
The Container Network Insights Agent is a lightweight, web-based solution designed for Kubernetes clusters. Its primary feature is the aggregation and visualization of networking logs and metrics in a unified interface. This agent reduces the need for manual data collection and correlation by providing a consolidated view of network activity and issues. The web-based interface enables quick access to relevant diagnostic information, improving the efficiency of troubleshooting workflows.

**Technical Mechanisms and Implementation Methods**  
The agent operates by deploying as a component within the Kubernetes cluster. It collects network-related telemetry from the cluster nodes and pods, including logs and metrics relevant to container networking. This data is then processed and made available through a web-based dashboard, which can be accessed by engineers for real-time insights. The lightweight nature of the agent ensures minimal resource overhead on the cluster, making it suitable for production environments.

**Use Cases and Application Scenarios**  
- **Incident Response:** During network outages or performance degradations, engineers can use the agent to quickly identify and diagnose issues without switching between multiple monitoring tools.
- **Proactive Monitoring:** The agent enables continuous visibility into network health, allowing teams to detect and address anomalies before they escalate into major incidents.
- **Root Cause Analysis:** By correlating network logs and metrics in a single interface, the agent simplifies the process of tracing issues back to their source, whether they stem from misconfigurations, policy violations, or infrastructure failures.
- **Performance Optimization:** Teams can use the insights provided to optimize network configurations and improve overall cluster performance.

**Important Considerations and Limitations**  
- The agent is currently in public preview, which means it may not be suitable for all production workloads and could be subject to changes before general availability.
- As a lightweight solution, the agent is designed to minimize resource consumption, but users should monitor its impact on cluster performance, especially in large-scale environments.
- The scope of supported Kubernetes distributions and Azure regions may be limited during the preview phase; users should consult the official documentation for compatibility details.

**Integration with Related Azure Services**  
The Container Network Insights Agent is designed to complement existing Azure Kubernetes Service (AKS) deployments. It can be integrated with Azure Monitor and other Azure-native observability tools to provide a holistic monitoring and diagnostics solution. The agent’s web-based interface can serve as a standalone diagnostic tool or be used in conjunction with Azure’s broader monitoring ecosystem for enhanced visibility and incident management.

**Summary Sentence**  
The Container Network Insights Agent, now in public preview, offers a lightweight, web-based solution for centralized collection and visualization of Kubernetes networking logs and metrics, streamlining troubleshooting and incident response for Azure Kubernetes Service environments.

---

### 3. Generally Available: Connect to Elastic SAN from Windows VM via VM Extension 

**Published**: April 28, 2026 20:30:56 UTC
**Link**: [Generally Available: Connect to Elastic SAN from Windows VM via VM Extension ](https://azure.microsoft.com/updates?id=560914)

**Update ID**: 560914
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Elastic SAN, Features

**Summary**:

- What was updated  
Azure Elastic SAN now supports connecting volumes to Windows Virtual Machines using the Elastic SAN VM extension, which is generally available.

- Key changes or new features  
The Elastic SAN VM extension enables direct volume connectivity from Windows VMs via the Azure Portal. Customers can attach Elastic SAN volumes during VM deployment, streamlining the provisioning and setup process. This eliminates the need for manual configuration or custom scripts to connect SAN volumes post-deployment.

- Target audience affected  
Developers and IT professionals managing Windows Virtual Machines and storage solutions in Azure, especially those using Elastic SAN for scalable storage.

- Important notes if any  
The new VM extension simplifies SAN volume management and integration with Windows VMs, improving automation and reducing deployment complexity. This feature is accessible directly from the Azure Portal, making it easier to incorporate Elastic SAN into VM workflows. Ensure your Windows VM images and deployments are compatible with the Elastic SAN VM extension for optimal use.

**Details**:

**Azure Update Report: Generally Available – Connect to Elastic SAN from Windows VM via VM Extension**

**Background and Purpose of the Update:**  
Azure Elastic SAN is a cloud-native storage solution designed to provide scalable, high-performance storage for Azure Virtual Machines (VMs) and other compute resources. Traditionally, connecting VMs to Elastic SAN volumes required manual configuration, which could be time-consuming and error-prone, especially at scale. The purpose of this update is to streamline and automate the process of connecting Windows Virtual Machines to Elastic SAN volumes by introducing support through a dedicated VM extension, accessible directly from the Azure Portal.

**Specific Features and Detailed Changes:**  
- **Elastic SAN VM Extension for Windows:** The update introduces a VM extension specifically for Windows VMs, enabling direct connectivity to Elastic SAN volumes.
- **Portal Integration:** The extension can be configured and deployed directly from the Azure Portal, allowing users to attach Elastic SAN volumes during the VM deployment process.
- **Automated Volume Connectivity:** The process of connecting a VM to Elastic SAN storage is automated, reducing the need for manual intervention and scripting.

**Technical Mechanisms and Implementation Methods:**  
- **VM Extension Deployment:** The Elastic SAN VM extension is installed on Windows VMs as part of the provisioning workflow. Extensions in Azure are small applications that provide post-deployment configuration and automation tasks.
- **Portal-Based Workflow:** During VM creation or management in the Azure Portal, users can select Elastic SAN volumes to attach. The portal orchestrates the deployment of the extension and the necessary configuration steps.
- **Volume Attachment:** The extension handles the discovery and mounting of Elastic SAN volumes to the Windows VM, ensuring that the storage is available to the operating system without additional manual configuration.

**Use Cases and Application Scenarios:**  
- **Simplified VM Deployment:** Organizations deploying new Windows VMs that require high-performance, scalable storage can now attach Elastic SAN volumes as part of the initial deployment process.
- **Automated Infrastructure Provisioning:** Enterprises using Infrastructure-as-Code (IaC) or automated deployment pipelines can leverage this extension to ensure consistent and repeatable storage connectivity.
- **Large-Scale Environments:** Environments with many VMs benefit from reduced operational overhead, as the extension standardizes and automates the connection process.

**Important Considerations and Limitations:**  
- **Windows VM Support:** This update specifically targets Windows Virtual Machines. There is no mention of support for Linux VMs in the provided information.
- **Portal-Driven Configuration:** The feature is accessed via the Azure Portal, which may limit automation options for users relying solely on CLI or API-based workflows unless further integration is provided.
- **Extension Lifecycle Management:** As with all VM extensions, administrators should monitor extension health and ensure compatibility with their VM images and OS versions.

**Integration with Related Azure Services:**  
- **Elastic SAN:** The update enhances the integration between Azure Virtual Machines and Elastic SAN, making it easier to leverage Elastic SAN’s scalable storage capabilities.
- **Azure Portal:** Direct integration with the Azure Portal simplifies the user experience and centralizes management tasks.
- **VM Extensions Ecosystem:** This update adds to the suite of Azure VM extensions, providing additional automation and configuration options for storage connectivity.

**Summary Sentence:**  
Azure Elastic SAN now offers a generally available VM extension for Windows Virtual Machines, enabling automated and streamlined connectivity to Elastic SAN volumes directly from the Azure Portal during VM deployment, thereby simplifying storage management and reducing manual configuration efforts for IT professionals.

---

### 4. Public Preview: Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium

**Published**: April 28, 2026 17:45:04 UTC
**Link**: [Public Preview: Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium](https://azure.microsoft.com/updates?id=561148)

**Update ID**: 561148
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure DDoS Protection, Azure Front Door, Web Application Firewall, Features, Services

**Summary**:

- What was updated  
Microsoft has announced the public preview of the Microsoft HTTP DDoS Ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium.

- Key changes or new features  
The new HTTP DDoS Ruleset provides enhanced protection against HTTP-layer DDoS attacks, which are a major cause of application downtime. Unlike traditional static controls, this ruleset leverages adaptive threat detection to identify and mitigate evolving attack patterns, including those from large-scale botnets. The ruleset is integrated with Azure Front Door Premium’s WAF, enabling real-time detection and automatic mitigation of malicious HTTP traffic.

- Target audience affected  
This update is relevant to developers and IT professionals responsible for securing web applications and APIs hosted on Azure Front Door Premium. Organizations with high-traffic web applications, especially those susceptible to DDoS attacks, will benefit most.

- Important notes if any  
The HTTP DDoS Ruleset is currently in public preview and available only on Azure Front Door Premium. Users can enable the feature through the Azure portal. As a preview feature, it may not be suitable for production workloads requiring full SLA guarantees. Microsoft recommends monitoring application performance and security logs after enabling the ruleset.

[Learn more](https://azure.microsoft.com/updates?id=561148)

**Details**:

**Azure Update Report: Public Preview – Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium**

**Background and Purpose of the Update**  
HTTP-layer Distributed Denial of Service (DDoS) attacks are a significant threat to web applications, frequently causing downtime and service disruption. Traditional static security controls, such as IP-based blocking or rate limiting, often fail to mitigate sophisticated attacks that leverage evolving botnets and dynamic attack patterns. To address these challenges, Microsoft has introduced the HTTP DDoS Ruleset for Azure Web Application Firewall (WAF) on Azure Front Door Premium, now available in public preview. The purpose of this update is to enhance application protection against HTTP-layer DDoS attacks by providing advanced, dynamic detection and mitigation capabilities.

**Specific Features and Detailed Changes**  
The HTTP DDoS Ruleset is a new feature integrated into Azure WAF on Azure Front Door Premium. It specifically targets HTTP-layer DDoS attacks, which are characterized by high volumes of malicious HTTP requests intended to overwhelm application resources. The ruleset operates by analyzing incoming HTTP traffic and applying specialized logic to identify and block attack patterns. This update introduces a set of rules designed to detect abnormal traffic behaviors, such as sudden spikes in request rates or suspicious request headers, and respond automatically to mitigate the impact.

**Technical Mechanisms and Implementation Methods**  
The HTTP DDoS Ruleset leverages Microsoft’s threat intelligence and advanced traffic analysis algorithms. It inspects HTTP request characteristics, including frequency, patterns, and anomalies, to distinguish legitimate traffic from attack traffic. When an attack is detected, the ruleset dynamically applies mitigation actions, such as blocking or rate-limiting malicious requests, without manual intervention. The ruleset is managed within the Azure WAF policy configuration for Azure Front Door Premium, allowing administrators to enable or customize protection as needed. The implementation is cloud-native, ensuring seamless integration and scalability for global applications.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations hosting critical web applications on Azure Front Door Premium that are exposed to the internet and susceptible to HTTP-layer DDoS attacks. Typical use cases include e-commerce platforms, financial services portals, and SaaS applications where uptime and performance are essential. The HTTP DDoS Ruleset provides automated protection, reducing the risk of downtime and minimizing operational overhead for security teams.

**Important Considerations and Limitations**  
As the HTTP DDoS Ruleset is in public preview, it may not offer full production-level support or all planned features. IT professionals should evaluate the ruleset in non-production environments and monitor its effectiveness before widespread deployment. The ruleset is currently available only on Azure Front Door Premium and must be configured within the Azure WAF policy. Compatibility with other Azure services or legacy WAF configurations may be limited during the preview phase.

**Integration with Related Azure Services**  
The HTTP DDoS Ruleset is tightly integrated with Azure Front Door Premium and Azure WAF, leveraging their global edge infrastructure for traffic inspection and mitigation. It complements existing Azure DDoS Protection services, which focus on network-layer attacks, by providing application-layer defense. Administrators can manage the ruleset through Azure Portal, REST APIs, or ARM templates, ensuring consistent policy enforcement across distributed environments.

**Summary Sentence**  
The public preview of the Microsoft HTTP DDoS Ruleset for Azure WAF on Azure Front Door Premium introduces advanced, automated protection against HTTP-layer DDoS attacks, enhancing application resilience and reducing operational complexity for IT professionals.

---

### 5. Generally Available: Cross-region IPAM pool association in Azure Virtual Network Manager

**Published**: April 28, 2026 17:45:04 UTC
**Link**: [Generally Available: Cross-region IPAM pool association in Azure Virtual Network Manager](https://azure.microsoft.com/updates?id=561067)

**Update ID**: 561067
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure Virtual Network Manager, Features, Management, Services

**Summary**:

- What was updated  
Azure Virtual Network Manager now offers General Availability of cross-region IPAM (IP Address Management) pool association.

- Key changes or new features  
You can now associate a single IPAM pool with virtual networks (VNets) across multiple Azure regions. This feature simplifies IP address management by allowing centralized control and allocation of IP address space, reducing the risk of configuration errors and improving scalability for multi-region deployments.

- Target audience affected  
This update is relevant for network architects, IT professionals, and developers managing large-scale or multi-region Azure environments, especially those responsible for IP address planning and network configuration.

- Important notes if any  
Cross-region IPAM pool association enables more efficient and error-resistant IP address management. It is particularly useful for organizations with global or multi-region Azure footprints, as it streamlines IP allocation and reduces administrative overhead. Review your current IPAM strategy to leverage this feature for better scalability and management.  
For more details, refer to the official update: https://azure.microsoft.com/updates?id=561067

**Details**:

**Azure Update Report: Generally Available – Cross-region IPAM Pool Association in Azure Virtual Network Manager**

**Background and Purpose of the Update:**  
Managing IP address space efficiently across multiple Azure regions has traditionally been a complex and error-prone process, especially for organizations with global footprints or distributed workloads. The challenge lies in scaling IP address management (IPAM) while minimizing configuration mistakes and ensuring consistent network policies. This update introduces cross-region IPAM pool association, aiming to simplify and centralize IP address management for virtual networks (VNets) deployed in different Azure regions.

**Specific Features and Detailed Changes:**  
With this update, Azure Virtual Network Manager (AVNM) now supports the association of a single IPAM pool with VNets that span multiple Azure regions. Previously, IPAM pools were typically scoped to a single region, requiring separate pools and management overhead for each region. The new feature allows administrators to create an IPAM pool once and associate it with VNets regardless of their regional location, streamlining the allocation and tracking of IP address space.

**Technical Mechanisms and Implementation Methods:**  
The cross-region IPAM pool association is implemented within the Azure Virtual Network Manager’s IPAM capabilities. When defining an IPAM pool, administrators can now specify that the pool is available for cross-region use. The AVNM service manages the allocation of subnets from this pool to VNets in different regions, ensuring that address spaces do not overlap and are assigned according to organizational policies. This mechanism leverages Azure’s control plane to enforce consistency and prevent configuration drift, reducing the risk of IP conflicts and misconfigurations.

**Use Cases and Application Scenarios:**  
- **Global Enterprises:** Organizations with VNets in multiple regions can centralize their IP address management, reducing administrative overhead and improving governance.
- **Disaster Recovery and High Availability:** Workloads that require failover or replication across regions benefit from consistent IPAM policies, simplifying network configuration during failover events.
- **Mergers and Acquisitions:** Businesses integrating networks from different regions can more easily consolidate IP address space using a unified pool.
- **DevOps and Automation:** Automated provisioning of VNets across regions can reference a single IPAM pool, streamlining infrastructure-as-code deployments.

**Important Considerations and Limitations:**  
- **Scope of Association:** Only VNets managed by Azure Virtual Network Manager can leverage cross-region IPAM pool association.
- **Policy Enforcement:** Administrators must ensure that organizational policies for IP address allocation are reflected in the configuration of the cross-region IPAM pool.
- **Regional Constraints:** While the feature allows cross-region association, there may be region-specific networking features or limitations not addressed by the IPAM pool itself.
- **Change Management:** Updates to the IPAM pool or its associations should be carefully managed to avoid unintended network disruptions.

**Integration with Related Azure Services:**  
- **Azure Virtual Network Manager:** The feature is natively integrated, allowing seamless management of IPAM pools and their associations.
- **Azure Policy:** Organizations can use Azure Policy to enforce compliance on IPAM pool usage and VNet associations.
- **Automation and DevOps Tools:** Integration with Azure Resource Manager templates, Azure CLI, and PowerShell enables automated deployment and management of cross-region IPAM pools.
- **Monitoring and Governance:** Azure Monitor and Azure Network Watcher can be used to track IP address usage and diagnose network issues across regions.

**Summary Sentence:**  
The general availability of cross-region IPAM pool association in Azure Virtual Network Manager enables centralized and scalable IP address management for VNets across multiple regions, reducing configuration complexity and supporting consistent network governance for distributed Azure environments.

---


*This report was automatically generated - 2026-04-29 03:02:29 UTC*