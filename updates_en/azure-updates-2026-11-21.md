# November 21, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 21, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Generally Available: Governance policy guidance in Foundry Canvas and VS Code

**Published**: November 21, 2026 00:45:13 UTC
**Link**: [Generally Available: Governance policy guidance in Foundry Canvas and VS Code](https://azure.microsoft.com/updates?id=581463)

**Update ID**: 581463
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Governance policy guidance is now generally available in Microsoft Foundry Canvas and the Foundry Toolkit for Visual Studio Code.

- Key changes or new features  
Developers can now access real-time governance policy guidance directly within Foundry Canvas and VS Code as they build agents. The guidance surfaces relevant policies for agent types, models, toolboxes, and guardrails, providing warnings and recommendations to ensure compliance and best practices. This integration streamlines agent development by proactively alerting users to potential policy violations and offering actionable insights.

- Target audience affected  
This update primarily impacts developers and IT professionals working with Microsoft Foundry to build AI agents, especially those using Foundry Canvas or the Foundry Toolkit for Visual Studio Code.

- Important notes if any  
The policy guidance helps enforce organizational and regulatory standards during agent development, reducing risk and improving security and compliance. Developers should ensure they are using the latest versions of Foundry Canvas and the Foundry Toolkit for VS Code to benefit from these features. For more information, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=581463

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Governance policy guidance in Foundry Canvas and VS Code  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581463)

---

**Background and Purpose of the Update**  
Microsoft Foundry is a platform designed to streamline agent development, focusing on compliance, security, and operational governance. As organizations increasingly build and deploy agents (such as AI-powered bots or automation routines), ensuring adherence to organizational and regulatory policies becomes critical. This update addresses the need for integrated governance guidance during the development lifecycle, reducing risks and improving policy compliance.

**Specific Features and Detailed Changes**  
With this release, governance policy guidance is now generally available within two key development environments:  
- **Foundry Canvas:** A visual interface for designing and configuring agents.  
- **Foundry Toolkit for Visual Studio Code:** An extension that brings Foundry agent development capabilities directly into the VS Code IDE.

Both environments now surface relevant governance policies as developers build agents. These policies cover agent types, models, toolboxes, and guardrails. The guidance includes warnings and actionable information, helping developers understand and comply with organizational requirements as they select components and configure agent behaviors.

**Technical Mechanisms and Implementation Methods**  
The governance guidance is integrated into the agent development workflow. As developers interact with agent components (such as selecting a model or adding a toolbox), the system dynamically checks for applicable policies and displays warnings or recommendations. This is achieved through:  
- **Policy Engine Integration:** The Foundry platform queries a policy repository and applies rules based on agent configuration choices.  
- **Contextual UI Feedback:** In both Canvas and VS Code, the user interface provides real-time feedback, highlighting policy violations or suggesting compliant alternatives.  
- **Guardrail Enforcement:** The system enforces guardrails, which are predefined boundaries or constraints, ensuring agents do not exceed permitted operational parameters.

**Use Cases and Application Scenarios**  
- **Enterprise Compliance:** Organizations with strict governance requirements can ensure agents are built in accordance with internal policies, reducing audit overhead and risk of non-compliance.
- **Regulatory Adherence:** Developers in regulated industries (e.g., finance, healthcare) can use the guidance to avoid deploying agents that violate legal or industry standards.
- **Security and Operational Control:** By surfacing guardrails and toolbox restrictions, the update helps prevent the use of insecure or unsupported models and tools.

**Important Considerations and Limitations**  
- **Policy Scope:** The guidance is limited to policies defined within the Foundry governance framework. Custom or external policies may require additional integration.
- **Warning-Driven Guidance:** The system provides warnings and recommendations but may not block all non-compliant actions; developers must review and act on guidance as appropriate.
- **Environment Support:** The update is available only in Foundry Canvas and the Foundry Toolkit for VS Code. Other development environments are not covered.

**Integration with Related Azure Services**  
- **Azure Policy:** While not explicitly mentioned, the governance guidance in Foundry Canvas and VS Code may complement broader Azure Policy enforcement for resource and agent governance.
- **Azure DevOps:** Developers can leverage the guidance during CI/CD workflows, ensuring agents meet governance standards before deployment.

---

**Summary Sentence:**  
Governance policy guidance is now generally available in Foundry Canvas and the Foundry Toolkit for Visual Studio Code, providing developers with real-time policy information and warnings for agent types, models, toolboxes, and guardrails to enhance compliance and operational governance during agent development.

---

### 2. Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code

**Published**: November 21, 2026 00:43:13 UTC
**Link**: [Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code](https://azure.microsoft.com/updates?id=581468)

**Update ID**: 581468
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Agent Builder in the Microsoft Foundry Toolkit for Visual Studio Code now supports prompt agents using the Microsoft Copilot harness, available in public preview.

- Key changes or new features  
Developers can now leverage the Copilot harness within Agent Builder to configure tools and skills for prompt agents. The update allows editing local YAML definitions, deploying changes directly to Foundry, and running/debugging agents in the VS Code environment. This integration streamlines the development workflow for Copilot-based agents, enabling rapid iteration and testing.

- Target audience affected  
This update is relevant to developers building AI agents, especially those working with Microsoft Copilot and Foundry Toolkit in Visual Studio Code. IT professionals managing agent deployments and workflows may also benefit from improved integration and deployment capabilities.

- Important notes if any  
The Copilot harness support is currently in public preview, so features may evolve and stability may not be guaranteed. Developers should review documentation for best practices and monitor for future updates as the integration matures. This enhancement aims to simplify agent development and deployment within the VS Code ecosystem.

**Details**:

**Azure Update Report**

**Title:** Public Preview: Microsoft Copilot harness support in Foundry Toolkit for VS Code  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581468)

---

### Background and Purpose of the Update

This update introduces public preview support for the Microsoft Copilot harness within the Agent Builder component of the Microsoft Foundry Toolkit for Visual Studio Code (VS Code). The primary purpose is to enable developers to build, configure, and deploy prompt agents that leverage Microsoft Copilot harness capabilities directly from their development environment. This enhancement aims to streamline agent development workflows and facilitate integration with Copilot-powered functionalities.

---

### Specific Features and Detailed Changes

- **Copilot Harness Integration:** The Agent Builder now supports prompt agents that utilize the Microsoft Copilot harness, allowing developers to create agents that interact with Copilot services.
- **Tool and Skill Configuration:** Developers can configure agent tools and skills within the toolkit, tailoring agent capabilities to specific requirements.
- **Local YAML Editing:** The update enables editing of local YAML definitions, providing a structured and version-controlled approach to agent configuration.
- **Deployment to Foundry:** Changes made to agents can be deployed directly to Microsoft Foundry, ensuring that updates are reflected in the production environment.
- **Agent Execution:** Developers can run agents within the toolkit, facilitating testing and validation of agent behavior before deployment.

---

### Technical Mechanisms and Implementation Methods

- **VS Code Extension:** The Foundry Toolkit operates as an extension within Visual Studio Code, offering an integrated development experience.
- **YAML-Based Configuration:** Agent definitions and configurations are managed via YAML files, which are editable locally and can be versioned using standard source control practices.
- **Copilot Harness Support:** The toolkit provides mechanisms to connect prompt agents to the Microsoft Copilot harness, enabling agents to utilize Copilot’s capabilities for enhanced interactions.
- **Deployment Pipeline:** The toolkit supports deployment workflows that push agent configurations and updates to the Foundry platform, ensuring seamless transition from development to production.

---

### Use Cases and Application Scenarios

- **Agent Development:** IT professionals and developers can use the toolkit to build prompt agents that leverage Copilot for advanced conversational or automation scenarios.
- **Skill Customization:** Organizations can configure agent skills and tools to meet specific business needs, such as automating support tasks or integrating with internal systems.
- **Rapid Iteration:** The ability to edit YAML locally and deploy changes quickly supports agile development and rapid prototyping of agent functionality.
- **Testing and Validation:** Running agents within the toolkit allows for thorough testing before deployment, reducing the risk of production issues.

---

### Important Considerations and Limitations

- **Public Preview:** The Copilot harness support is currently in public preview, which may entail limited functionality, potential instability, or incomplete documentation.
- **YAML Management:** Proper handling of YAML files is essential to avoid configuration errors; version control is recommended.
- **Deployment Scope:** Only changes made within the toolkit are deployable to Foundry; external modifications may require manual integration.
- **Skill and Tool Compatibility:** Ensure that configured tools and skills are compatible with the Copilot harness and Foundry deployment requirements.

---

### Integration with Related Azure Services

- **Microsoft Foundry:** The toolkit is tightly integrated with Microsoft Foundry, facilitating agent deployment and management.
- **Copilot Services:** Agents built with the toolkit can leverage Microsoft Copilot harness capabilities, enabling advanced AI-driven interactions.
- **VS Code Ecosystem:** The extension operates within VS Code, allowing integration with other Azure extensions and development tools.

---

**Summary Sentence:**  
The public preview of Microsoft Copilot harness support in the Foundry Toolkit for Visual Studio Code enables developers to configure, edit, deploy, and run prompt agents with Copilot capabilities, streamlining agent development and integration within the Microsoft Foundry platform.

---

### 3. Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027

**Published**: November 20, 2026 23:16:31 UTC
**Link**: [Retirement: Support for Azure Functions OpenAI Extension ends on April 20, 2027](https://azure.microsoft.com/updates?id=579952)

**Update ID**: 579952
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Internet of Things, Azure Functions, Retirements, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft announced the retirement of support for the Azure Functions OpenAI extension, effective April 20, 2027.

- Key changes or new features  
Support for the Azure Functions OpenAI extension will end. Developers and IT professionals are advised to migrate their workloads to the OpenAI SDK, Microsoft Foundry SDK, or Azure AI Search SDKs, depending on their application requirements. No new features will be added to the extension, and after the retirement date, it will no longer receive updates or support.

- Target audience affected  
This update impacts developers and IT professionals who use the Azure Functions OpenAI extension in their .NET applications or serverless workloads.

- Important notes if any  
Migration to the recommended SDKs should be completed before April 20, 2027, to avoid disruption. Existing applications using the extension will continue to function until the retirement date, but ongoing support and maintenance will cease after that. Review your current implementations and plan migration to ensure continued functionality and support. For detailed migration guidance, refer to official documentation and the Azure Update link provided.

**Details**:

**Azure Update Report: Retirement of Azure Functions OpenAI Extension Support (April 20, 2027)**

**Background and Purpose of the Update:**
Microsoft has announced the retirement of support for the Azure Functions OpenAI extension, effective April 20, 2027. This update is part of Microsoft’s ongoing efforts to streamline and modernize its AI integration capabilities within Azure, encouraging customers to transition to more robust and directly supported SDKs such as OpenAI, Microsoft Foundry, or Azure AI Search SDKs. The purpose of this update is to ensure that developers leverage the latest tools and frameworks for integrating AI functionalities, thereby improving performance, security, and maintainability.

**Specific Features and Detailed Changes:**
The Azure Functions OpenAI extension currently allows developers to integrate OpenAI-powered AI capabilities within Azure Functions, enabling serverless execution of AI workflows. With the announced retirement, this extension will no longer receive support, updates, or security patches after April 20, 2027. Developers are advised to migrate their workloads to the official OpenAI SDK, Microsoft Foundry SDK, or Azure AI Search SDK, depending on their specific use case. The change affects all Azure Functions projects utilizing the OpenAI extension, particularly those built with .NET.

**Technical Mechanisms and Implementation Methods:**
The Azure Functions OpenAI extension operates as a middleware layer, facilitating communication between Azure Functions and OpenAI services. It abstracts API calls and manages authentication, request formatting, and response parsing. Post-retirement, developers must implement direct integration using the recommended SDKs. This involves updating function code to utilize the OpenAI SDK (for direct OpenAI API access), Microsoft Foundry SDK (for advanced AI orchestration), or Azure AI Search SDK (for AI-powered search scenarios). Migration will require refactoring function bindings, updating authentication mechanisms, and ensuring compatibility with the chosen SDK’s API surface.

**Use Cases and Application Scenarios:**
Typical use cases for the Azure Functions OpenAI extension include serverless AI-powered chatbots, content generation, document summarization, and intelligent data processing workflows. After retirement, these scenarios should be implemented using the recommended SDKs. For example, a chatbot previously built with the extension should be migrated to use the OpenAI SDK directly within Azure Functions, ensuring continued access to OpenAI models. Similarly, AI-driven search solutions should transition to Azure AI Search SDK for enhanced search capabilities.

**Important Considerations and Limitations:**
- **Migration Deadline:** All workloads must be migrated by April 20, 2027, to avoid unsupported code and potential security risks.
- **SDK Selection:** Choose the appropriate SDK based on your scenario—OpenAI SDK for direct AI model access, Microsoft Foundry SDK for orchestration, or Azure AI Search SDK for search.
- **Compatibility:** Review SDK documentation for compatibility with your existing .NET applications and Azure Functions runtime.
- **Security:** Unsupported extensions may expose vulnerabilities; timely migration is critical.
- **Testing:** Comprehensive testing is required post-migration to ensure functional parity and performance.

**Integration with Related Azure Services:**
The recommended SDKs integrate seamlessly with Azure Functions, Azure App Services, Azure Logic Apps, and other Azure AI services. Direct SDK integration enhances flexibility, allowing developers to leverage advanced features, improved authentication, and tighter coupling with Azure’s monitoring and deployment pipelines.

**Summary Sentence:**
Support for the Azure Functions OpenAI extension will end on April 20, 2027; IT professionals should migrate to OpenAI, Microsoft Foundry, or Azure AI Search SDKs directly by that date to ensure continued functionality and support for AI-powered serverless applications.

---

### 4. Public Preview: Programmed Training in Microsoft Foundry

**Published**: November 20, 2026 22:58:28 UTC
**Link**: [Public Preview: Programmed Training in Microsoft Foundry](https://azure.microsoft.com/updates?id=581713)

**Update ID**: 581713
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry has released the Programmed Training API in public preview, enabling developers to build custom post-training loops for open-weight models.

- Key changes or new features  
The Programmed Training API allows users to programmatically manage and customize training workflows beyond standard managed training jobs. This feature is designed for scenarios where developers require more granular control over the training process, such as iterative fine-tuning or advanced experimentation. Access to the API is available by request via a preview sign-up form.

- Target audience affected  
This update is primarily relevant to developers, data scientists, and IT professionals working with machine learning models on Microsoft Foundry, especially those who need to implement custom training logic or integrate open-weight models into their workflows.

- Important notes if any  
Programmed Training is currently in public preview and may not be suitable for production workloads. Interested users must request access through the preview sign-up form. Managed training jobs remain recommended for standard training scenarios, while Programmed Training is intended for advanced use cases requiring custom post-training loops. Users should review documentation and preview limitations before integrating this feature into their projects.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=581713

**Details**:

**Azure Update Report: Public Preview – Programmed Training in Microsoft Foundry**

**Background and Purpose of the Update**  
The introduction of Programmed Training in Microsoft Foundry addresses the need for greater flexibility and control in the post-training phase of machine learning workflows, particularly for open-weight models. Traditional managed training jobs are optimized for straightforward training scenarios, but advanced users often require custom post-training loops to fine-tune, evaluate, or further process models beyond initial training. This update provides an API to facilitate such customizations, enabling organizations and developers to build tailored post-training workflows.

**Specific Features and Detailed Changes**  
- **Programmed Training API:** The core feature is an API that allows users to construct their own post-training loops. This means users can define custom logic and operations to be executed after the initial training phase, such as additional evaluation, fine-tuning, or integration with other processes.
- **Open-Weight Model Support:** The API is specifically designed for open-weight models, which are models whose weights are accessible and modifiable, allowing for deeper customization and experimentation.
- **Public Preview Availability:** The feature is currently in public preview and can be accessed by submitting a request through the preview sign-up form. This allows early adopters to experiment and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
- **API-Based Workflow:** The Programmed Training API is exposed through Microsoft Foundry, enabling developers to programmatically define and execute post-training operations. This API likely supports integration with various programming languages and frameworks commonly used in machine learning.
- **Custom Post-Training Loops:** Users can implement custom loops that interact with open-weight models, potentially including operations such as iterative refinement, batch evaluation, or integration with external data sources.
- **Managed vs. Programmed Training:** While managed training jobs are suitable for standard workflows, the programmed training approach empowers users to go beyond default pipelines, offering granular control over the training lifecycle.

**Use Cases and Application Scenarios**  
- **Advanced Model Fine-Tuning:** Organizations can use programmed training to apply domain-specific post-training adjustments to open-weight models, improving accuracy or adapting models to specialized tasks.
- **Automated Evaluation Pipelines:** Developers can build automated evaluation loops that continuously assess model performance against new data or benchmarks.
- **Custom Post-Processing:** Teams can integrate additional post-processing steps, such as pruning, quantization, or integration with downstream systems, directly into the training workflow.

**Important Considerations and Limitations**  
- **Preview Status:** The feature is in public preview, which means it may not be fully stable or feature-complete. Users should be aware of potential changes and limitations during this phase.
- **Access by Request:** Access is not open to all users; it requires submission through the preview sign-up form, which may limit immediate adoption.
- **Open-Weight Model Requirement:** The API is designed for open-weight models; it may not be applicable to closed or proprietary models where weights are not accessible.

**Integration with Related Azure Services**  
- **Microsoft Foundry:** Programmed Training is integrated within Microsoft Foundry, leveraging its infrastructure for model management and training orchestration.
- **Azure Machine Learning:** While not explicitly mentioned, the API may complement Azure Machine Learning workflows, especially for teams using open-weight models and requiring custom post-training logic.

**Summary Sentence**  
Programmed Training in Microsoft Foundry, now in public preview, introduces an API for building custom post-training loops over open-weight models, offering enhanced flexibility for advanced machine learning workflows and accessible by request through a preview sign-up form.

---

### 5. Public Preview: Multi-turn evaluation in Microsoft Foundry

**Published**: November 20, 2026 22:56:51 UTC
**Link**: [Public Preview: Multi-turn evaluation in Microsoft Foundry](https://azure.microsoft.com/updates?id=581746)

**Update ID**: 581746
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry has introduced a public preview of multi-turn evaluation, enabling users to assess entire agent conversations rather than just individual responses.

- Key changes or new features  
The new multi-turn evaluation feature allows developers and IT professionals to evaluate the quality of agent interactions across the full conversation flow. This helps ensure that conversational agents meet quality standards not only at the response level but also in the context of the overall dialogue. It addresses scenarios where individual responses may appear correct but do not contribute effectively to the conversation as a whole.

- Target audience affected  
This update is relevant for developers, conversational AI designers, and IT professionals who use Microsoft Foundry to build, test, and evaluate agent-based solutions.

- Important notes if any  
Multi-turn evaluation provides a more comprehensive approach to quality assurance for conversational agents. It is currently available in public preview, so feedback from users is encouraged to help refine the feature. This enhancement can improve agent performance and user experience by identifying issues that may not be apparent in single-response evaluations.

For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=581746

**Details**:

**Azure Update Report: Public Preview – Multi-turn Evaluation in Microsoft Foundry**

**Background and Purpose of the Update**  
Microsoft Foundry is a platform for building, deploying, and evaluating conversational agents. Traditionally, evaluation methods have focused on single-turn responses, assessing the quality of individual agent replies in isolation. However, conversational agents often operate in multi-turn scenarios, where the context and flow across multiple exchanges are critical to overall performance and user satisfaction. The purpose of this update is to enable IT professionals and developers to evaluate entire agent conversations against their quality standards, rather than limiting assessments to individual responses.

**Specific Features and Detailed Changes**  
The public preview introduces multi-turn evaluation capabilities within Microsoft Foundry. This feature allows users to analyze and assess complete agent conversations, taking into account the sequence and context of multiple exchanges. The evaluation is not restricted to single responses; instead, it considers the agent’s ability to maintain context, coherence, and quality throughout the conversation. This enables a more holistic assessment of conversational agents, ensuring that responses are not only correct individually but also contribute to a high-quality overall interaction.

**Technical Mechanisms and Implementation Methods**  
Multi-turn evaluation is implemented as an integrated feature within Microsoft Foundry’s evaluation workflow. Users can submit conversation logs or agent transcripts for assessment. The platform provides tools to review the entire conversation, applying quality standards across multiple turns. Evaluation criteria can include context retention, logical progression, user intent recognition, and overall conversational flow. The mechanism leverages Foundry’s existing infrastructure for agent evaluation, extending it to support multi-turn scenarios without requiring significant changes to agent deployment or logging processes.

**Use Cases and Application Scenarios**  
This update is particularly valuable in scenarios where conversational agents are expected to handle complex, multi-step interactions, such as customer support, troubleshooting, onboarding, and guided workflows. IT professionals can use multi-turn evaluation to identify issues that may not be apparent in single-turn assessments, such as context loss, inconsistent responses, or conversational breakdowns. The feature supports iterative improvement of agent logic and dialog management, leading to more robust and user-friendly conversational solutions.

**Important Considerations and Limitations**  
As the feature is in public preview, it may not yet support all evaluation criteria or integration scenarios. Users should be aware of potential limitations in customization and reporting capabilities. The evaluation is designed to assess conversations against predefined quality standards, so careful definition of these standards is essential for meaningful results. Additionally, the preview status indicates that feedback and feature requests are encouraged, and production use should be approached with caution.

**Integration with Related Azure Services**  
Multi-turn evaluation in Microsoft Foundry can be used alongside other Azure services for conversational AI, such as Azure Bot Service and Azure Cognitive Services. Conversation logs generated by agents deployed on these platforms can be imported into Foundry for evaluation. This integration streamlines the assessment process for agents built and managed within the Azure ecosystem, supporting end-to-end development, deployment, and quality assurance workflows.

**Summary Sentence**  
Multi-turn evaluation in Microsoft Foundry, now in public preview, enables IT professionals to assess entire agent conversations against quality standards, providing a comprehensive approach to conversational agent evaluation beyond individual responses.

---

### 6. Public Preview: Azure Firewall for Containers

**Published**: November 20, 2026 20:05:17 UTC
**Link**: [Public Preview: Azure Firewall for Containers](https://azure.microsoft.com/updates?id=581963)

**Update ID**: 581963
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Compute, Containers, Azure Firewall, Azure Kubernetes Service (AKS), Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure Firewall for Containers is now available in Public Preview.

- Key changes or new features  
This update extends Azure Firewall’s protection to containerized workloads, allowing centralized security management for network traffic within container environments. Developers and IT professionals can leverage Azure Firewall’s advanced capabilities—such as threat intelligence, filtering, and logging—for containers, integrating these features directly into their container networking workflows. This enables consistent policy enforcement and visibility across both traditional and containerized applications.

- Target audience affected  
Developers and IT professionals managing containerized workloads in Azure, especially those seeking enhanced network security and centralized policy management for containers.

- Important notes  
Azure Firewall for Containers is currently in Public Preview, meaning it may not be suitable for production workloads yet. Users should review documentation for limitations and best practices. This feature helps simplify security operations for container environments, reducing complexity and improving compliance. Integration with Azure Firewall allows for unified security policies across all workloads, streamlining management and monitoring.

**Details**:

**Background and Purpose of the Update**  
The introduction of Azure Firewall for Containers in Public Preview aims to extend the robust network security capabilities of Azure Firewall to containerized workloads. As organizations increasingly adopt containerized applications, there is a growing need for centralized and consistent network security controls that can protect both traditional and container-based environments. This update addresses the demand for unified security management by enabling Azure Firewall to secure network traffic within container environments.

**Specific Features and Detailed Changes**  
Azure Firewall for Containers brings the established features of Azure Firewall—such as threat intelligence, filtering, and logging—to containerized workloads. This allows customers to leverage Azure Firewall’s centralized policy management and enforcement mechanisms directly within their container networks. The update introduces the ability to apply Azure Firewall rulesets to container traffic, ensuring that security policies are consistently enforced across both VM-based and containerized resources.

**Technical Mechanisms and Implementation Methods**  
The technical implementation involves extending Azure Firewall’s inspection and filtering capabilities to the network overlays and virtual networks used by container orchestrators (such as Kubernetes). Azure Firewall for Containers integrates with the container network infrastructure, enabling it to monitor, filter, and log traffic to and from containerized applications. This centralized approach simplifies the deployment and management of network security policies, reducing the complexity associated with securing dynamic and ephemeral container environments.

**Use Cases and Application Scenarios**  
Typical use cases include securing microservices architectures running on Azure Kubernetes Service (AKS) or other container platforms hosted in Azure. Organizations can use Azure Firewall for Containers to enforce egress and ingress controls, prevent lateral movement between containers, and ensure compliance with organizational security standards. It is particularly beneficial in scenarios where multiple containerized workloads need to be governed by consistent security policies, or where regulatory requirements mandate centralized logging and auditing of network traffic.

**Important Considerations and Limitations**  
As this feature is in Public Preview, it may not yet support all production workloads or advanced scenarios. Customers should evaluate the preview’s capabilities in test environments before broad deployment. Integration with existing Azure Firewall configurations and compatibility with specific container orchestrators or network plugins should be carefully reviewed. Additionally, organizations should monitor for updates regarding general availability and any changes to feature sets or supported environments.

**Integration with Related Azure Services**  
Azure Firewall for Containers is designed to work seamlessly with other Azure security and networking services. It can be integrated into existing Azure Virtual Networks, and complements services such as Azure Monitor for logging and analytics, Azure Policy for governance, and Azure Security Center for unified security management. This integration enables organizations to maintain a holistic security posture across both traditional and containerized workloads within the Azure ecosystem.

**Summary Sentence**  
Azure Firewall for Containers (Public Preview) extends centralized Azure Firewall protection to containerized workloads, enabling consistent network security policy enforcement and management for container environments within Azure.

---

### 7. Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines 

**Published**: November 20, 2026 18:50:52 UTC
**Link**: [Generally Available: Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines ](https://azure.microsoft.com/updates?id=564451)

**Update ID**: 564451
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Features, Microsoft Build, Microsoft Ignite

**Summary**:

**What was updated:**  
Azure has announced the general availability of new Arm-based Cobalt 200 virtual machine series: Dpsv7, Dplsv7 (general purpose), Epsv7 (memory-optimized), Mpsv4 (high-memory), and Lpsv5 (dense storage).

**Key changes or new features:**  
- These VM series are built on the Cobalt 200 Arm architecture, offering significant performance and efficiency improvements compared to previous Cobalt 100 VMs.
- Enhanced compute, memory, and storage capabilities across the new VM types, supporting a broader range of workloads.
- Improved price-performance ratios, making them more cost-effective for both general and specialized workloads.
- Expanded VM options for developers and IT teams to optimize for specific workload requirements (general purpose, memory-intensive, high-memory, and dense storage).
- Native support for Arm-based applications, enabling better performance for workloads optimized for Arm architecture.

**Target audience affected:**  
- Developers building or migrating applications to Arm-based infrastructure.
- IT professionals managing Azure VM deployments, especially those requiring optimized compute, memory, or storage.
- Organizations seeking cost-effective cloud solutions for diverse workloads.

**Important notes:**  
- These VMs are now generally available and can be provisioned in supported Azure regions.
- Workload migration from Cobalt 100 to Cobalt 200 VMs is recommended for improved performance and efficiency.
- Ensure application compatibility with Arm architecture before migrating or deploying workloads.

**Details**:

**Azure Update Report: Generally Available – Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series Virtual Machines**

**Background and Purpose of the Update:**  
Microsoft Azure has announced the general availability of new Arm-based virtual machine (VM) series powered by Cobalt 200 processors. The update introduces Dpsv7 and Dplsv7 (general purpose), Epsv7 (memory-optimized), Mpsv4 (high-memory), and Lpsv5 (dense storage) VM families. The primary purpose is to deliver significant enhancements over the previous generation Cobalt 100 VMs, offering improved performance, scalability, and efficiency for a broad range of workloads.

**Specific Features and Detailed Changes:**  
- **Dpsv7 and Dplsv7-series:** These are general-purpose VMs designed for balanced CPU and memory workloads.  
- **Epsv7-series:** Memory-optimized VMs suitable for applications requiring high memory-to-CPU ratios.  
- **Mpsv4-series:** High-memory VMs tailored for workloads that demand substantial memory resources.  
- **Lpsv5-series:** Dense storage VMs optimized for storage-intensive applications, providing enhanced disk throughput and capacity.  
All these VM series are based on the Cobalt 200 Arm architecture, which offers improved compute performance, energy efficiency, and cost-effectiveness compared to the previous Cobalt 100 generation.

**Technical Mechanisms and Implementation Methods:**  
The new VM series leverage Arm-based Cobalt 200 processors, which are designed for cloud-native workloads and provide higher performance per watt. Azure’s VM provisioning and management system supports these new series, enabling seamless deployment and scaling. The VMs are integrated into Azure’s infrastructure, allowing users to select the desired VM size and configuration directly from the Azure portal, CLI, or API. The underlying hardware improvements translate to better throughput, lower latency, and optimized resource utilization.

**Use Cases and Application Scenarios:**  
- **Dpsv7/Dplsv7:** Ideal for web servers, application servers, and development/test environments requiring balanced resources.  
- **Epsv7:** Suitable for in-memory databases, caching solutions, and analytics workloads needing high memory capacity.  
- **Mpsv4:** Designed for large-scale enterprise applications, SAP workloads, and other high-memory scenarios.  
- **Lpsv5:** Best for big data, NoSQL databases, and storage-heavy applications where disk performance is critical.  
These VM series enable IT professionals to optimize workload placement based on specific performance and resource requirements.

**Important Considerations and Limitations:**  
- The new VM series are Arm-based, so compatibility with existing software stacks must be verified, especially for applications not natively supporting Arm architecture.
- Migration from Cobalt 100 VMs may require testing and validation to ensure performance and stability.
- Availability may vary by region; users should confirm regional support before planning deployments.
- Licensing and pricing models may differ from previous VM generations; review Azure documentation for updated cost structures.

**Integration with Related Azure Services:**  
The Cobalt 200 VM series are fully integrated with Azure’s ecosystem, supporting Azure Virtual Machine Scale Sets, Azure Backup, Azure Monitor, and other management and security services. They can be used in conjunction with Azure networking, storage, and identity solutions, ensuring seamless operation within hybrid and cloud-native architectures.

**Summary Sentence:**  
The Azure Cobalt 200 Arm-based Dpsv7, Dplsv7, Epsv7, Mpsv4, and Lpsv5-series virtual machines are now generally available, offering improved performance, efficiency, and specialized configurations for a wide range of workloads compared to the previous Cobalt 100 generation.

---


*This report was automatically generated - 2026-11-21 03:04:12 UTC*