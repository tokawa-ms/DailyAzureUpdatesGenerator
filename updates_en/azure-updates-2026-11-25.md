# November 25, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 25, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 8 items

## Update List

### 1. Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks

**Published**: November 24, 2026 17:48:22 UTC
**Link**: [Generally Available: Azure Site Recovery support for zonal disaster recovery for Ultra disks](https://azure.microsoft.com/updates?id=582171)

**Update ID**: 582171
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Site Recovery, Management, Feature

**Summary**:

- What was updated  
Azure Site Recovery now supports Zone-to-Zone Disaster Recovery (Zonal DR) for Azure Ultra disks.

- Key changes or new features  
The update enables replication and recovery of performance-intensive virtual machines (VMs) using Ultra disks across Azure Availability Zones. This allows customers to protect workloads against zonal failures by replicating Ultra disk data to another zone and recovering VMs in the event of a disruption.

- Target audience affected  
This update is relevant for IT professionals and developers managing high-performance workloads on Azure VMs with Ultra disks, especially those requiring enhanced disaster recovery and business continuity across Availability Zones.

- Important notes  
Ultra disk support for zonal DR ensures minimal downtime and data loss for critical applications. Customers should review Azure Site Recovery documentation for prerequisites and configuration steps. This feature is generally available and can be leveraged in supported Azure regions. For optimal use, ensure VM and disk configurations meet Ultra disk requirements and Site Recovery best practices.

**Details**:

**Azure Update Report: Generally Available – Azure Site Recovery support for zonal disaster recovery for Ultra disks**

**Background and Purpose of the Update**  
Azure Site Recovery (ASR) is a disaster recovery solution that enables replication, failover, and recovery of workloads running on Azure virtual machines (VMs). Azure Ultra disks are high-performance, low-latency storage options designed for I/O-intensive workloads. Previously, ASR did not support Ultra disks for zonal disaster recovery, limiting the protection of VMs using Ultra disks to single-zone scenarios. The purpose of this update is to extend ASR’s capabilities, enabling customers to protect VMs with Ultra disks across Azure Availability Zones, thereby enhancing resilience against zonal disruptions.

**Specific Features and Detailed Changes**  
With this update, ASR now supports Zone-to-Zone Disaster Recovery (Zonal DR) for Azure Ultra disks. This means that VMs utilizing Ultra disks can be replicated from one Availability Zone to another within the same Azure region. In the event of a zonal failure, customers can recover their performance-intensive VMs—including their Ultra disk data—in a different zone, minimizing downtime and data loss.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages ASR’s replication technology, which continuously synchronizes the VM’s state—including Ultra disk data—from the source zone to the target zone. During normal operations, ASR maintains consistency between the disks in both zones. If a zonal disruption occurs, ASR orchestrates the failover process, bringing up the VM in the target zone with the replicated Ultra disk. The recovery process is managed through the ASR portal, where administrators can initiate failover and monitor replication health. The solution is designed to meet the performance characteristics of Ultra disks, ensuring low-latency and high-throughput replication.

**Use Cases and Application Scenarios**  
This update is particularly relevant for enterprises running mission-critical, performance-intensive workloads on Azure VMs with Ultra disks, such as databases, transactional systems, and real-time analytics. By enabling zonal disaster recovery, organizations can achieve higher availability and business continuity for these workloads. Typical scenarios include financial services, healthcare, and e-commerce platforms where downtime or data loss can have significant operational impacts.

**Important Considerations and Limitations**  
- The feature is available only for Azure Ultra disks and applies to VMs deployed across Availability Zones within the same region.
- Customers must ensure that both source and target zones support Ultra disks.
- Replication and failover operations may incur additional costs, including storage and network charges.
- ASR’s zonal DR for Ultra disks does not extend to cross-region disaster recovery; it is limited to zone-to-zone within a region.
- Compatibility with other Azure features (such as managed identities, network configurations, and VM sizes) should be verified as part of deployment planning.

**Integration with Related Azure Services**  
ASR’s zonal DR for Ultra disks integrates seamlessly with Azure VM management, Availability Zones, and Azure Ultra disk provisioning. It complements Azure Backup for data protection and can be used alongside Azure Monitor for operational insights. The update enhances the overall disaster recovery strategy for workloads using Ultra disks, ensuring alignment with Azure’s high-availability architecture.

**Summary Sentence**  
Azure Site Recovery now enables zone-to-zone disaster recovery for Azure Ultra disks, allowing IT professionals to protect and recover performance-intensive VMs across Availability Zones, thereby improving resilience and business continuity for critical workloads.

---

### 2. Public Preview: Optimize agents from insights in Foundry Agent Service

**Published**: November 24, 2026 16:52:07 UTC
**Link**: [Public Preview: Optimize agents from insights in Foundry Agent Service](https://azure.microsoft.com/updates?id=581483)

**Update ID**: 581483
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
The Foundry Agent Service now offers a public preview feature enabling optimization of agents based on insights directly within the Foundry portal.

- Key changes or new features  
Developers and IT professionals can start from an eligible insight in a prompt-agent trace and use the portal to automatically generate and evaluate candidate changes to agent instructions and function-calling tool descriptions. This streamlines the process of improving agent performance and behavior by leveraging trace data and actionable insights.

- Target audience affected  
This update is relevant for developers and IT professionals working with Azure Foundry Agent Service, especially those responsible for building, maintaining, and optimizing AI agents and their workflows.

- Important notes  
The feature is currently in public preview and may not be available in all regions or for all agent types. Users should review eligibility criteria for insights and ensure their agents are compatible with the optimization workflow. This update aims to reduce manual tuning and accelerate agent improvement cycles by providing data-driven recommendations and automated evaluation tools.

For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=581483).

**Details**:

**Azure Update Explanation: Public Preview – Optimize Agents from Insights in Foundry Agent Service**

**Background and Purpose of the Update**  
This update introduces the public preview of the “Optimization from Insights” feature within the Foundry Agent Service. The primary goal is to enhance the efficiency and effectiveness of prompt-based agents by leveraging actionable insights derived from agent traces. By enabling optimization directly from these insights, the update aims to streamline the iterative improvement process for agents, reducing manual effort and accelerating development cycles.

**Specific Features and Detailed Changes**  
- **Insight-Driven Optimization:** Users can now initiate optimization workflows directly from eligible insights identified in prompt-agent traces within the Foundry portal.
- **Candidate Generation and Evaluation:** The system facilitates the generation and evaluation of candidate changes to both the agent’s instructions and the descriptions of function-calling tools. This allows for rapid experimentation and refinement based on real-world trace data.
- **Portal Integration:** All optimization actions are accessible through the Foundry portal, providing a unified interface for tracing, insight review, and agent optimization.

**Technical Mechanisms and Implementation Methods**  
- **Trace Analysis:** The Foundry Agent Service analyzes prompt-agent traces to surface actionable insights. These insights highlight potential areas for improvement in agent behavior or tool usage.
- **Automated Candidate Generation:** Upon selecting an eligible insight, the service generates candidate modifications to agent instructions and tool descriptions. This may involve altering prompt phrasing, adjusting parameters, or refining tool invocation logic.
- **Evaluation Workflow:** Users can evaluate the effectiveness of these candidate changes within the portal, enabling data-driven decision-making for agent optimization.

**Use Cases and Application Scenarios**  
- **Prompt Engineering:** Developers iteratively refining prompt-based agents can use this feature to quickly identify and address suboptimal agent responses or tool interactions.
- **Function-Calling Tool Optimization:** Teams managing agents that rely on external function-calling tools can optimize tool descriptions and invocation logic based on trace-derived insights.
- **Continuous Improvement:** Organizations seeking to implement continuous improvement pipelines for their agents benefit from streamlined, insight-driven optimization workflows.

**Important Considerations and Limitations**  
- **Eligibility of Insights:** Only insights deemed eligible by the system can be used to initiate the optimization process. Not all trace data may result in actionable insights.
- **Preview Limitations:** As this feature is in public preview, it may be subject to change and may not support all agent types or tool configurations.
- **Portal Dependency:** Optimization actions are currently accessible only through the Foundry portal interface.

**Integration with Related Azure Services**  
- **Foundry Agent Service:** This feature is tightly integrated with the Foundry Agent Service, leveraging its tracing and insight capabilities.
- **Azure Portal Ecosystem:** The optimization workflow is embedded within the Foundry portal, aligning with Azure’s broader portal-based management and monitoring tools.

**Summary Sentence**  
The public preview of optimization from insights in Foundry Agent Service enables users to generate and evaluate candidate changes to agent instructions and function-calling tool descriptions directly from eligible insights in prompt-agent traces, streamlining agent improvement workflows within the Foundry portal.

---

### 3. Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service

**Published**: November 24, 2026 16:50:47 UTC
**Link**: [Public Preview: Govern MCP tools with your own gateway in Microsoft Foundry Agent Service](https://azure.microsoft.com/updates?id=581498)

**Update ID**: 581498
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry Agent Service now supports public preview for routing Managed Control Plane (MCP) tool traffic through your organization’s own AI Gateway or Azure API Management endpoints.

- Key changes or new features  
Organizations can configure their own gateway to manage and govern MCP tool traffic, rather than relying solely on Microsoft-managed endpoints. The process involves setting up the MCP route in your gateway and then providing the gateway-routed endpoint within Foundry Agent Service. This enables custom governance, monitoring, and security controls for MCP traffic.

- Target audience affected  
This update is relevant for developers and IT professionals managing AI and API integrations, especially those responsible for governance, compliance, and security of MCP tools within enterprise environments.

- Important notes  
To use this feature, you must first configure the MCP route in your AI Gateway or Azure API Management instance before entering the gateway-routed endpoint in Foundry Agent Service. This allows for greater control and visibility over MCP tool traffic, supporting organizational policies and compliance requirements. The feature is currently in public preview, so it may not be suitable for production workloads yet.  
For more details, see the [Azure Update announcement](https://azure.microsoft.com/updates?id=581498).

**Details**:

**Background and Purpose of the Update:**  
The public preview of the Microsoft Foundry Agent Service introduces enhanced governance capabilities for MCP (Managed Control Plane) tools by allowing organizations to route MCP tool traffic through their own managed endpoints. This update addresses the need for organizations to maintain control, visibility, and compliance over AI and API traffic by leveraging existing infrastructure, such as AI Gateway or Azure API Management, rather than relying solely on default routing mechanisms.

**Specific Features and Detailed Changes:**  
With this update, organizations can now configure MCP tool traffic to be routed through their own AI Gateway or Azure API Management endpoints. The process involves first setting up the MCP route within the gateway, then specifying the gateway-routed endpoint in the Foundry Agent Service configuration. This enables organizations to apply their own governance policies, monitor traffic, and enforce security controls directly on MCP tool interactions.

**Technical Mechanisms and Implementation Methods:**  
The technical implementation centers on the integration of the Foundry Agent Service with existing gateway solutions. Administrators must configure the MCP route within their AI Gateway or Azure API Management, ensuring that the endpoint is prepared to handle MCP tool traffic. Once the gateway is configured, the endpoint is registered in the Foundry Agent Service, effectively redirecting MCP tool traffic through the organization’s managed gateway. This allows for centralized policy enforcement, logging, and monitoring at the gateway level, leveraging the capabilities of AI Gateway or Azure API Management.

**Use Cases and Application Scenarios:**  
- **Compliance and Security:** Organizations with strict regulatory requirements can enforce custom security policies and audit trails for MCP tool traffic.
- **Traffic Monitoring and Analytics:** By routing traffic through managed endpoints, IT teams gain visibility into MCP tool usage and can analyze patterns for optimization or anomaly detection.
- **Custom Policy Enforcement:** Enterprises can apply rate limiting, authentication, or other custom policies to MCP tool traffic using their existing gateway infrastructure.
- **Integration with Enterprise Architecture:** This feature enables seamless integration of MCP tools into broader enterprise API management strategies, supporting unified governance.

**Important Considerations and Limitations:**  
- The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- Proper configuration of the gateway and MCP route is required; misconfiguration may result in traffic disruption or governance gaps.
- Organizations must ensure their AI Gateway or Azure API Management endpoints are capable of handling the expected MCP tool traffic volume and security requirements.
- Only endpoints managed by the organization are supported; default routing mechanisms are bypassed.

**Integration with Related Azure Services:**  
This update directly integrates with Azure API Management and AI Gateway, leveraging their capabilities for traffic routing, policy enforcement, and monitoring. It also extends the governance model of the Microsoft Foundry Agent Service, allowing MCP tools to be managed within the context of existing Azure infrastructure. This facilitates unified management and compliance across AI and API workloads.

**Summary Sentence:**  
The public preview of Microsoft Foundry Agent Service enables organizations to govern MCP tool traffic by routing it through their own AI Gateway or Azure API Management endpoints, providing enhanced control, monitoring, and policy enforcement capabilities within existing infrastructure.

---

### 4. Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ

**Published**: November 24, 2026 16:49:39 UTC
**Link**: [Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ](https://azure.microsoft.com/updates?id=581303)

**Update ID**: 581303
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure AI Search and Foundry IQ now support Azure Storage permissions for access control.

- Key changes or new features  
Search applications and AI agents integrated with Azure AI Search and Foundry IQ can now enforce Azure Storage permissions when returning search results. This means content is filtered based on each user's access rights, ensuring users only see data they are authorized to view. This update reduces the need to create custom access control logic within applications.

- Target audience affected  
Developers building search solutions and AI agents using Azure AI Search and Foundry IQ, as well as IT professionals managing data access and security in Microsoft Foundry environments.

- Important notes  
To leverage this feature, proper configuration of Azure Storage permissions is required. The update streamlines security and compliance by aligning search result access with existing Azure Storage access controls. This is particularly beneficial for organizations with complex data access requirements or those seeking to minimize custom code for authorization. Review documentation to ensure correct permission setup and integration.  

Link: [Azure Update](https://azure.microsoft.com/updates?id=581303)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Use Azure Storage permissions in Azure AI Search and Foundry IQ  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581303)

---

**Background and Purpose of the Update**

This update introduces the general availability of integrating Azure Storage permissions directly into Azure AI Search and Foundry IQ within Microsoft Foundry. The primary purpose is to enhance access control for search results by leveraging existing Azure Storage permissions, thereby streamlining security management and reducing the need for redundant access control configurations across multiple services.

---

**Specific Features and Detailed Changes**

- **Permission-Based Access Control:** Azure AI Search and Foundry IQ now support Azure Storage permissions for controlling access to search results.
- **User-Specific Content Delivery:** Once permissions are configured, search applications and AI agents only return content that each user is authorized to access, based on their Azure Storage permissions.
- **Simplified Security Management:** The update reduces the administrative overhead by eliminating the need to create and maintain separate access control lists or policies specifically for Azure AI Search and Foundry IQ.

---

**Technical Mechanisms and Implementation Methods**

- **Integration with Azure Storage ACLs:** The mechanism relies on Azure Storage’s built-in access control lists (ACLs) and permissions. When a user initiates a search query, Azure AI Search and Foundry IQ reference the user’s Azure Storage permissions to filter search results.
- **Authentication and Authorization:** The system utilizes Azure Active Directory (AAD) for user authentication and authorization. User identity is mapped to their storage permissions, ensuring that only permitted content is surfaced.
- **Configuration Steps:**
  - Administrators configure Azure Storage permissions using standard methods (e.g., role assignments, ACLs).
  - Azure AI Search and Foundry IQ are set to recognize and enforce these permissions during search operations.
  - Applications and AI agents interacting with these services inherit the access controls automatically.

---

**Use Cases and Application Scenarios**

- **Enterprise Document Search:** Organizations can deploy search solutions where employees only see documents they have access to, as defined by Azure Storage permissions.
- **AI Agent Content Retrieval:** AI agents can retrieve and present content to users in compliance with organizational security policies, without custom access control logic.
- **Compliance and Data Security:** The update supports compliance requirements by ensuring sensitive data is only accessible to authorized users, leveraging existing storage security models.

---

**Important Considerations and Limitations**

- **Permission Configuration:** Proper configuration of Azure Storage permissions is critical; misconfigured permissions may lead to unauthorized access or restricted search results.
- **Supported Storage Types:** Only supported Azure Storage types and permission models are applicable; unsupported storage or custom access control mechanisms may not be recognized.
- **Performance Impact:** Filtering search results based on permissions may introduce additional latency, depending on the complexity of permission checks.
- **No Redundant Access Controls:** The update is designed to reduce the need for separate access controls, but organizations must ensure that all relevant permissions are managed within Azure Storage.

---

**Integration with Related Azure Services**

- **Azure Storage:** Acts as the primary source of access control, with permissions directly influencing search result visibility.
- **Azure AI Search:** Integrates with Azure Storage to enforce permission-based filtering of search results.
- **Foundry IQ:** Leverages the same mechanism for content retrieval and presentation.
- **Azure Active Directory:** Provides identity management and authentication, ensuring secure mapping between users and their storage permissions.

---

**Summary Sentence**

Azure AI Search and Foundry IQ now generally support Azure Storage permissions for search result access control, enabling secure, user-specific content delivery and reducing the need for separate access management configurations.

---

### 5. Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service

**Published**: November 24, 2026 16:48:25 UTC
**Link**: [Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service](https://azure.microsoft.com/updates?id=581313)

**Update ID**: 581313
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Foundry Agent Service now supports native Agent2Agent (A2A) passthrough for hosted agents in Public Preview.

- Key changes or new features  
Previously, Agent Service required a protocol conversion layer, translating incoming A2A requests to the Responses protocol. With this update, Agent Service can now forward native A2A requests directly to hosted agents, eliminating the need for protocol conversion. This streamlines communication between agents and reduces latency and complexity.

- Target audience affected  
Developers and IT professionals who use Agent Service to host A2A agents, especially those integrating custom or legacy A2A agents into Azure Foundry workflows.

- Important notes  
This feature is currently in Public Preview and may not be suitable for production workloads yet. The update allows easier migration of existing A2A agents to Agent Service without requiring protocol changes. Review documentation for compatibility and implementation details before enabling passthrough in your environment.

For more information, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=581313).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Native A2A passthrough for hosted agents in Foundry Agent Service  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581313)

---

**Background and Purpose of the Update**

The Foundry Agent Service previously required a protocol conversion layer for incoming Agent2Agent (A2A) requests, translating them into the Responses protocol before processing. This conversion introduced complexity and potential latency for organizations utilizing their own A2A agents. The purpose of this update is to streamline agent integration by allowing native A2A requests to be forwarded directly, eliminating the need for protocol conversion and simplifying agent onboarding and communication.

---

**Specific Features and Detailed Changes**

- **Native A2A Passthrough:** Hosted agents in Foundry Agent Service now support direct forwarding of native A2A requests. This feature bypasses the previous protocol conversion to the Responses protocol.
- **Agent Compatibility:** Organizations can bring their existing A2A agents to the Agent Service without modification or the need for a conversion layer.
- **Public Preview Availability:** This feature is currently in public preview, allowing IT professionals to test and validate the passthrough functionality in their environments.

---

**Technical Mechanisms and Implementation Methods**

- **Direct Request Forwarding:** The Agent Service acts as a transparent proxy for A2A requests, forwarding them in their original format to the hosted agent. No intermediate translation or conversion occurs.
- **Protocol Handling:** The service maintains the integrity of the A2A protocol, ensuring that requests and responses are processed natively by the agent, preserving protocol semantics and reducing processing overhead.
- **Hosted Agent Integration:** Existing A2A agents can be registered with the Agent Service and will receive requests in their native protocol, allowing seamless migration and integration.

---

**Use Cases and Application Scenarios**

- **Legacy Agent Migration:** Organizations with established A2A agents can migrate to the Foundry Agent Service without refactoring agent communication protocols.
- **Performance Optimization:** By removing the conversion layer, latency is reduced and throughput is improved for scenarios requiring rapid agent-to-agent communication.
- **Simplified Development:** Developers can focus on core agent functionality without accommodating protocol translation requirements, accelerating deployment cycles.

---

**Important Considerations and Limitations**

- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should validate compatibility and stability in test environments.
- **Protocol Support:** Only native A2A requests are supported in passthrough mode. Agents relying on the Responses protocol or other conversion mechanisms may require adjustment.
- **Service Integration:** Ensure that hosted agents are properly registered and configured to handle native A2A requests for optimal operation.

---

**Integration with Related Azure Services**

- **Foundry Agent Service:** The update directly enhances the Foundry Agent Service, improving agent onboarding and communication.
- **Azure Automation and Orchestration:** Agents integrated via native A2A passthrough can participate in automated workflows and orchestration scenarios with reduced complexity.
- **Monitoring and Management:** Azure monitoring tools can be used to track agent communication and performance, leveraging the improved efficiency of native A2A passthrough.

---

**Summary Sentence**

This update enables hosted agents in Foundry Agent Service to receive and process native Agent2Agent requests directly, eliminating the protocol conversion layer and simplifying agent integration, currently available in public preview.

---

### 6. Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools

**Published**: November 24, 2026 16:45:59 UTC
**Link**: [Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools](https://azure.microsoft.com/updates?id=581318)

**Update ID**: 581318
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
A new Azure Developer CLI (azd) extension for Azure Document Intelligence and Content Understanding is now available in public preview within Microsoft Foundry Tools.

- Key changes or new features  
The extension introduces azd ai cu commands, enabling developers and IT professionals to analyze documents using Azure Document Intelligence and Content Understanding directly from the CLI. Analysis results can be exported in Markdown or JSON formats, streamlining integration with workflows and documentation. This feature enhances automation and simplifies document processing within Foundry Tools.

- Target audience affected  
Developers and IT professionals working with Microsoft Foundry Tools, especially those leveraging Azure Document Intelligence and requiring automated document analysis and content extraction in their development workflows.

- Important notes if any  
This feature is currently in public preview, so it may be subject to changes and improvements. Users should review documentation and provide feedback during the preview phase. Export options (Markdown and JSON) offer flexibility for downstream processing and integration. Ensure you have the latest Azure Developer CLI installed to access these new commands.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581318)

---

### Background and Purpose of the Update

This update introduces a public preview of an Azure Developer CLI (azd) extension designed to integrate Azure Document Intelligence and Content Understanding capabilities directly into Foundry Tools within Microsoft Foundry. The primary purpose is to streamline the process of document analysis by enabling developers and IT professionals to use command-line operations for extracting and understanding content from documents, thereby enhancing automation and developer productivity within the Foundry environment.

---

### Specific Features and Detailed Changes

- **New azd Extension:** A dedicated extension for the Azure Developer CLI (azd) is now available, specifically targeting document analysis workflows.
- **Command Set:** The extension introduces the `azd ai cu` command group, which provides direct access to Azure Document Intelligence and Content Understanding features.
- **Output Formats:** Analysis results can be exported in either Markdown or JSON formats, supporting both human-readable documentation and machine-processable data pipelines.
- **Integration with Foundry Tools:** The extension is tailored for use within Foundry Tools, allowing seamless workflow integration for users operating in the Microsoft Foundry ecosystem.

---

### Technical Mechanisms and Implementation Methods

- **CLI-Based Workflow:** The extension leverages the Azure Developer CLI, enabling users to invoke document analysis directly from the command line using `azd ai cu` commands.
- **Document Intelligence Integration:** The extension interfaces with Azure Document Intelligence services, which provide advanced document parsing, extraction, and content understanding capabilities.
- **Result Serialization:** After analysis, results are programmatically serialized into Markdown or JSON, supporting downstream consumption in documentation systems or automated workflows.
- **Foundry Tools Compatibility:** The extension is designed to operate within the context of Foundry Tools, ensuring compatibility and optimized user experience for Foundry-based projects.

---

### Use Cases and Application Scenarios

- **Automated Document Processing:** IT professionals can automate the extraction and analysis of information from large volumes of documents (e.g., contracts, invoices, reports) within Foundry-based solutions.
- **Integration in DevOps Pipelines:** The CLI extension can be incorporated into CI/CD pipelines to validate, extract, or transform document content as part of automated build or deployment processes.
- **Content Understanding for Knowledge Management:** Organizations can use the tool to convert unstructured document data into structured formats (Markdown/JSON), facilitating knowledge base creation or compliance documentation.
- **Developer Productivity:** Developers can quickly analyze and understand document content without leaving the command-line environment, reducing context switching and manual processing.

---

### Important Considerations and Limitations

- **Public Preview Status:** As the extension is in public preview, features may be subject to change, and production use should be approached with caution.
- **Supported Environments:** The extension is specifically designed for use within Microsoft Foundry and Foundry Tools; applicability outside this context is not indicated.
- **Output Format Selection:** Users should choose the output format (Markdown or JSON) based on their downstream integration or consumption requirements.
- **Service Dependencies:** Proper configuration and access to Azure Document Intelligence services are required for the extension to function.

---

### Integration with Related Azure Services

- **Azure Document Intelligence:** The extension directly utilizes Azure Document Intelligence, leveraging its capabilities for document parsing and content extraction.
- **Azure Developer CLI (azd):** The solution is built as an extension to the Azure Developer CLI, ensuring familiar command-line operations for Azure developers.
- **Foundry Tools:** Deep integration with Foundry Tools ensures that document analysis workflows are embedded within the broader Foundry development and automation ecosystem.

---

**Summary:**  
The public preview of the Azure Developer CLI extension for Azure Document Intelligence and Content Understanding in Foundry Tools enables IT professionals to analyze documents via command-line operations, output results in Markdown or JSON, and integrate document analysis seamlessly

---

### 7. Public Preview: Cost controls for model and agent spending in Microsoft Foundry

**Published**: November 24, 2026 16:43:40 UTC
**Link**: [Public Preview: Cost controls for model and agent spending in Microsoft Foundry](https://azure.microsoft.com/updates?id=581323)

**Update ID**: 581323
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry now supports cost controls for model and agent spending, available in Public Preview.

- Key changes or new features  
You can set spending or token budgets for Foundry resources or projects. When usage reaches your defined threshold, cost controls will either send alerts via Azure Event Grid or block new requests to prevent overspending. Budgets can be applied at different scopes, enabling granular management of costs for models and agents within Foundry.

- Target audience affected  
Developers and IT professionals managing AI workloads, models, and agents in Microsoft Foundry.

- Important notes  
This feature helps teams proactively monitor and control costs, reducing the risk of unexpected expenses. Integration with Azure Event Grid allows automated workflows or notifications when thresholds are met. Blocking new requests ensures strict budget adherence. This is a Public Preview, so functionality may change before general availability. For implementation details, refer to the official documentation.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Cost controls for model and agent spending in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581323)

---

**Background and Purpose of the Update:**  
Microsoft Foundry is a platform for developing and deploying AI models and agents. As usage of these resources can lead to unpredictable or escalating costs, especially in large-scale or experimental projects, organizations require robust mechanisms to monitor and control spending. This update introduces cost controls to address these needs, enabling IT administrators and project owners to manage budgets proactively and prevent cost overruns.

---

**Specific Features and Detailed Changes:**  
- **Budget Setting:** Administrators can now define a spending or token budget for individual Foundry resources or entire projects.
- **Threshold Alerts:** When usage approaches a pre-defined threshold, the system triggers an alert. This alert is delivered via Azure Event Grid, allowing for automated or manual intervention.
- **Request Blocking:** Upon reaching the budget limit, the system can automatically block new requests to the Foundry resource or project, enforcing strict cost containment.
- **Granular Application:** Budgets can be applied at different scopes—either at the resource level or project level—offering flexibility for various organizational structures and project requirements.

---

**Technical Mechanisms and Implementation Methods:**  
- **Budget Enforcement:** The cost control mechanism tracks resource consumption (either in monetary spend or token usage) in near real-time.
- **Event Grid Integration:** Alerts are sent through Azure Event Grid, which can be configured to trigger downstream workflows, such as sending notifications, invoking automation scripts, or integrating with ITSM systems.
- **Blocking Logic:** Once the budget is exhausted, the system enforces a hard stop on new requests, ensuring no further consumption occurs until the budget is adjusted or reset.

---

**Use Cases and Application Scenarios:**  
- **Development and Testing Environments:** Prevent runaway costs in experimental or development projects by setting strict spending limits.
- **Multi-team Projects:** Allocate specific budgets to different teams or projects within a shared Foundry environment, ensuring fair resource distribution and financial accountability.
- **Enterprise Governance:** Integrate cost controls into broader cloud governance strategies, aligning AI resource usage with organizational financial policies.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production-critical workloads and could be subject to changes or limitations in functionality.
- **Scope of Application:** Cost controls currently apply to Foundry resources and projects; applicability to other Azure AI services is not indicated in this update.
- **Alerting and Blocking:** Ensure that downstream systems and users are prepared for automated blocking of requests, which could impact service availability or user experience.

---

**Integration with Related Azure Services:**  
- **Azure Event Grid:** Native integration with Event Grid enables seamless alerting and automation, supporting a wide range of notification and remediation scenarios.
- **Azure Cost Management:** While not explicitly mentioned, these controls can complement existing Azure Cost Management practices by providing resource-level enforcement within Foundry.

---

**Summary Sentence:**  
This update introduces public preview cost controls in Microsoft Foundry, enabling administrators to set spending or token budgets, receive threshold alerts via Azure Event Grid, and automatically block new requests upon budget exhaustion, thereby enhancing financial governance and operational control for AI model and agent workloads.

---

### 8. Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service

**Published**: November 24, 2026 16:42:20 UTC
**Link**: [Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service](https://azure.microsoft.com/updates?id=581328)

**Update ID**: 581328
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Foundry Agent Service now supports central governance of outbound domains for hosted agents via Azure Policy, available in public preview.

- Key changes or new features  
Administrators can define and enforce egress policies using Azure Policy to control which outbound domains hosted agents can access. Agent authors must configure and attach a compliant egress policy before creating a new agent version. This ensures outbound requests from agents are restricted to approved destinations, improving security and compliance.

- Target audience affected  
IT administrators responsible for Azure governance and security, and developers/agent authors working with Foundry Agent Service.

- Important notes  
This feature enables centralized management of outbound connectivity for hosted agents, reducing risk of unauthorized data exfiltration. All agent versions must comply with the defined egress policy before deployment. This update is currently in public preview and may be subject to changes before general availability.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Central governance of hosted-agent outbound domains in Foundry Agent Service  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581328)

---

**Background and Purpose of the Update**  
The Foundry Agent Service in Azure enables organizations to run hosted agents for automation and integration tasks. Previously, managing and controlling the outbound network traffic from these hosted agents was challenging, leading to potential security and compliance risks. The purpose of this update is to introduce centralized governance over outbound domains accessed by hosted agents, leveraging Azure Policy. This enhancement aims to provide administrators with greater control, ensuring that agent egress is compliant with organizational security standards.

---

**Specific Features and Detailed Changes**  
- **Azure Policy Integration:** Administrators can now use Azure Policy to define and enforce which outbound domains hosted agents in Foundry Agent Service may access.
- **Egress Policy Configuration:** Agent authors are required to configure and attach an egress policy that specifies allowed outbound destinations before creating a new agent version.
- **Policy Enforcement:** The attached egress policy governs outbound requests, ensuring that agents only communicate with compliant destinations as defined by the policy.

---

**Technical Mechanisms and Implementation Methods**  
- **Policy Definition:** Administrators create Azure Policy definitions specifying permitted outbound domains for hosted agents.
- **Policy Attachment:** When an agent author prepares a new agent version, they must attach a compliant egress policy to the agent configuration.
- **Policy Evaluation:** The Foundry Agent Service evaluates outbound requests against the attached egress policy. Only requests to domains listed in the policy are permitted; all others are blocked.
- **Centralized Management:** Azure Policy provides a centralized interface for managing and updating egress policies across multiple agents, simplifying governance and compliance tracking.

---

**Use Cases and Application Scenarios**  
- **Security Compliance:** Organizations with strict regulatory requirements can ensure hosted agents only communicate with approved external services.
- **Data Loss Prevention:** By restricting outbound domains, administrators can prevent agents from sending data to unauthorized locations.
- **Operational Control:** Enterprises can centrally manage and update allowed domains for all hosted agents, responding quickly to changing business needs or threat landscapes.

---

**Important Considerations and Limitations**  
- **Policy Attachment Requirement:** Agent authors must attach a compliant egress policy before creating a new agent version, which may require process changes in agent development workflows.
- **Scope of Enforcement:** The update governs outbound domains only; it does not address other aspects such as inbound traffic or protocol-level restrictions.
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to changes or limitations in functionality.

---

**Integration with Related Azure Services**  
- **Azure Policy:** The update leverages Azure Policy for defining, managing, and enforcing egress policies.
- **Foundry Agent Service:** The governance mechanism is integrated directly into the Foundry Agent Service, affecting hosted agents managed within this service.
- **Azure Security and Compliance Solutions:** This feature can complement existing Azure security tools, such as Azure Firewall and Azure Monitor, by providing additional outbound traffic control.

---

**Summary Sentence:**  
This update introduces centralized governance of outbound domains for hosted agents in Foundry Agent Service using Azure Policy, enabling administrators to enforce compliant egress policies and enhance security and compliance controls.

---


*This report was automatically generated - 2026-11-25 03:05:08 UTC*