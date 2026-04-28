# April 28, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 28, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Bring your own AI Gateway in Foundry Agent Service 

**Published**: April 27, 2026 18:00:52 UTC
**Link**: [Generally Available: Bring your own AI Gateway in Foundry Agent Service ](https://azure.microsoft.com/updates?id=561002)

**Update ID**: 561002
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features

**Summary**:

- What was updated  
The Foundry Agent Service is now generally available with support for "bring your own AI Gateway" scenarios.

- Key changes or new features  
Agents in Foundry Agent Service can now interact with AI models that are deployed and managed outside of the Foundry environment. This includes support for models hosted behind enterprise AI gateways, such as Azure API Management. Organizations can leverage their existing AI infrastructure and governance policies while integrating with Foundry agents.

- Target audience affected  
This update is relevant for developers and IT professionals who manage AI models, especially those working in organizations with established AI deployment pipelines, custom models, or strict data governance requirements. It is also significant for teams using Azure API Management or similar gateways to secure and monitor AI endpoints.

- Important notes if any  
This enhancement allows organizations to maintain control over their AI models, apply custom compliance and security policies, and integrate external AI endpoints seamlessly with Foundry agents. Developers should ensure their external AI endpoints are properly secured and accessible to the Foundry Agent Service. Review documentation for integration requirements and best practices.

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
The Foundry Agent Service in Azure is designed to enable the deployment and management of AI agents that can interact with various data and services. Traditionally, these agents relied on AI models that were natively managed within the Foundry environment. The purpose of this update is to expand the flexibility of the Foundry Agent Service by supporting "bring-your-own-model" (BYOM) scenarios. This means organizations can now leverage AI models that are deployed and managed outside of Foundry, particularly those secured behind enterprise AI gateways such as Azure API Management.

**Specific Features and Detailed Changes:**  
With this update, the Foundry Agent Service now allows agents to connect to external AI models, rather than being limited to models hosted within Foundry. The key feature is the ability to route agent requests to AI endpoints that are managed outside of the Foundry ecosystem. This includes support for models that are exposed via enterprise-grade gateways, such as Azure API Management, which can provide additional layers of security, monitoring, and policy enforcement.

**Technical Mechanisms and Implementation Methods:**  
Technically, this update introduces integration points within the Foundry Agent Service configuration, enabling agents to specify external endpoints for AI inference. When an agent requires an AI model for a task, it can now invoke an HTTP-based API endpoint, such as one published through Azure API Management. This allows organizations to use custom models, third-party models, or models hosted in other environments, as long as they are accessible via a compliant API endpoint. The mechanism relies on standard RESTful API calls, and organizations can use Azure API Management to handle authentication, authorization, throttling, and logging for these model endpoints.

**Use Cases and Application Scenarios:**  
- **Custom Model Integration:** Enterprises with proprietary AI models can deploy them on their own infrastructure or in other Azure services, then expose them via API Management for use by Foundry agents.
- **Multi-Model Orchestration:** Organizations can orchestrate multiple models, possibly from different vendors or environments, and manage them centrally through Azure API Management.
- **Compliance and Security:** Sensitive industries can enforce strict access controls and auditing by placing their AI models behind API gateways, ensuring only authorized Foundry agents can access them.

**Important Considerations and Limitations:**  
- **Endpoint Compatibility:** External AI models must be exposed via APIs compatible with the Foundry Agent Service’s integration requirements.
- **Network and Security:** Proper network configuration and security policies must be in place to allow secure communication between Foundry agents and the external AI endpoints.
- **Performance:** Latency and throughput will depend on the external endpoint’s performance and the network path between Foundry and the AI gateway.
- **Management Overhead:** Organizations are responsible for the lifecycle management, scaling, and monitoring of external models.

**Integration with Related Azure Services:**  
This update is particularly synergistic with Azure API Management, which can serve as the enterprise AI gateway. API Management provides robust features such as authentication (OAuth, JWT, etc.), rate limiting, analytics, and policy enforcement, which can be leveraged to secure and manage access to external AI models. This integration enables seamless and secure connectivity between Foundry agents and a broad range of AI models hosted across Azure or on-premises environments.

**Summary Sentence:**  
The Foundry Agent Service now supports bring-your-own-model scenarios, enabling agents to utilize AI models deployed outside of Foundry—including those secured behind enterprise AI gateways like Azure API Management—thereby enhancing flexibility, security, and integration options for organizations.

---

### 2. Retirement: Prompt Flow in Azure ML and Foundry

**Published**: April 27, 2026 16:15:55 UTC
**Link**: [Retirement: Prompt Flow in Azure ML and Foundry](https://azure.microsoft.com/updates?id=502936)

**Update ID**: 502936
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Prompt Flow in Azure Machine Learning and Microsoft Foundry, effective April 20, 2027. Prompt Flow will be replaced by the Microsoft Agent Framework, a new orchestration platform.

- Key changes or new features  
The Microsoft Agent Framework will provide a unified, modern orchestration solution for AI workflows, replacing Prompt Flow. This new platform is designed to unlock advanced capabilities, streamline development, and support future innovations in AI orchestration.

- Target audience affected  
Developers and IT professionals using Prompt Flow in Azure Machine Learning or Foundry for AI workflow orchestration are directly impacted. Teams building, deploying, or managing AI solutions should prepare for migration to the Microsoft Agent Framework.

- Important notes if any  
Prompt Flow will remain supported until April 20, 2027, after which it will be fully retired. Users should begin planning migration strategies to the Microsoft Agent Framework to ensure continuity and take advantage of new features. Further guidance and migration tools are expected to be provided by Microsoft as the retirement date approaches.

**Details**:

**Azure Update Report: Retirement of Prompt Flow in Azure ML and Foundry**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Prompt Flow from both Microsoft Foundry and Azure Machine Learning (Azure ML), effective April 20, 2027. The primary purpose of this update is to transition users to a unified, modern orchestration platform—Microsoft Agent Framework. This strategic move aims to consolidate orchestration capabilities, streamline development workflows, and provide enhanced features for AI solution development.

**Specific Features and Detailed Changes:**  
- **Retirement Date:** Prompt Flow will no longer be available in Azure ML and Foundry after April 20, 2027.
- **Replacement Platform:** The Microsoft Agent Framework will serve as the new orchestration platform, offering a single, consolidated environment for building and managing AI-driven workflows.
- **Feature Enhancements:** The transition to Microsoft Agent Framework is designed to unlock new capabilities, including a unified orchestration experience and future-proofing for evolving AI workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Migration Path:** Users leveraging Prompt Flow for workflow orchestration in Azure ML or Foundry will need to migrate their solutions to the Microsoft Agent Framework before the retirement date.
- **Orchestration Model:** The Microsoft Agent Framework provides a modernized orchestration mechanism, likely supporting more advanced workflow definitions, integration points, and extensibility compared to Prompt Flow.
- **Platform Integration:** The Agent Framework is positioned as a central orchestration layer, facilitating seamless integration with Azure ML, Foundry, and potentially other Azure AI services.

**Use Cases and Application Scenarios:**  
- **Current Use Cases:** Prompt Flow is commonly used for orchestrating prompt engineering, managing AI workflow pipelines, and automating machine learning tasks within Azure ML and Foundry environments.
- **Future Use Cases:** After migration, these scenarios will be supported and enhanced by the Microsoft Agent Framework, which is expected to cater to similar and expanded orchestration requirements for AI agents, workflow automation, and integration with other Azure AI services.

**Important Considerations and Limitations:**  
- **Migration Deadline:** All workflows and solutions using Prompt Flow must be migrated to the Microsoft Agent Framework by April 20, 2027, to ensure continued support and access to orchestration capabilities.
- **Feature Parity:** Users should evaluate the feature set of the Microsoft Agent Framework to ensure it meets their current and future orchestration needs, as there may be differences in workflow definitions, APIs, or integration patterns.
- **Operational Impact:** Planning and testing migration strategies ahead of the retirement date is critical to avoid service disruptions.

**Integration with Related Azure Services:**  
- **Azure Machine Learning:** The Microsoft Agent Framework will become the primary orchestration tool within Azure ML, replacing Prompt Flow for managing AI and ML workflows.
- **Microsoft Foundry:** Similarly, Foundry users will transition to the Agent Framework for workflow orchestration, benefiting from unified capabilities across both platforms.
- **Broader Azure Ecosystem:** The unified orchestration approach is expected to facilitate deeper integration with other Azure AI and automation services, streamlining end-to-end solution development.

**Summary Sentence:**  
Prompt Flow will be retired from Microsoft Foundry and Azure Machine Learning on April 20, 2027, and replaced by the Microsoft Agent Framework, providing a unified and modern orchestration platform with enhanced capabilities for AI workflow management.

---


*This report was automatically generated - 2026-04-28 03:01:13 UTC*