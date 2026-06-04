# June 04, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 04, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 19 items

## Update List

### 1. Public Preview: MAI-Voice-2 in Microsoft Foundry

**Published**: June 03, 2026 23:00:57 UTC
**Link**: [Public Preview: MAI-Voice-2 in Microsoft Foundry](https://azure.microsoft.com/updates?id=563217)

**Update ID**: 563217
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has released MAI-Voice-2, a new first-party voice model from the Microsoft AI team, into public preview.

- Key changes or new features  
  - MAI-Voice-2 enables natural-sounding speech generation in over 10 languages.  
  - Supports voice cloning from a short reference sample, allowing users to replicate a specific voice.  
  - Includes voice prompting capabilities for more flexible and context-aware speech synthesis.

- Target audience affected  
  - Developers building applications that require multilingual text-to-speech or custom voice experiences.  
  - IT professionals managing AI-powered voice solutions and integrating advanced voice models into enterprise systems.

- Important notes  
  - As a public preview, MAI-Voice-2 may not be production-ready and could be subject to changes.  
  - Early access allows developers and IT teams to experiment and provide feedback before general availability.  
  - Integration is available via Microsoft Foundry, so familiarity with Foundry APIs and services is recommended.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=563217

**Details**:

**Azure Update Technical Report: Public Preview of MAI-Voice-2 in Microsoft Foundry**

**Background and Purpose of the Update**  
Microsoft Foundry has introduced MAI-Voice-2 in public preview, marking the availability of a first-party voice model developed by the Microsoft AI team. The primary objective of this update is to enhance the platform’s capabilities in natural speech generation and voice cloning, supporting multilingual scenarios and advanced voice personalization for enterprise and developer use.

**Specific Features and Detailed Changes**  
MAI-Voice-2 is distinguished by its ability to generate natural-sounding speech in over 10 languages, broadening accessibility and localization options for global applications. A key feature is voice cloning, which enables the model to replicate a user’s voice from a short reference sample. This allows for rapid creation of personalized voice assets without extensive data collection. Additionally, the model supports voice prompting, facilitating dynamic and context-aware speech synthesis.

**Technical Mechanisms and Implementation Methods**  
The MAI-Voice-2 model leverages advanced neural network architectures for speech synthesis, likely utilizing deep learning techniques such as sequence-to-sequence models and attention mechanisms. Voice cloning is achieved through analysis of a brief reference audio sample, extracting unique vocal characteristics and timbre to generate a synthetic voice that closely matches the original. Multilingual support is implemented via language-specific training datasets and model adaptation strategies, ensuring accurate pronunciation and prosody across supported languages. Integration with Microsoft Foundry provides API endpoints and SDKs for developers to access these capabilities programmatically.

**Use Cases and Application Scenarios**  
MAI-Voice-2 is suitable for a variety of enterprise and developer scenarios, including:  
- Automated customer service agents and chatbots that require natural, multilingual speech output.  
- Content creation platforms needing rapid voiceover generation in multiple languages.  
- Accessibility solutions, such as personalized text-to-speech for users with speech impairments.  
- Interactive voice applications, including virtual assistants and gaming NPCs, where voice cloning enhances user engagement.  
- Localization workflows, enabling efficient adaptation of spoken content for international audiences.

**Important Considerations and Limitations**  
As MAI-Voice-2 is in public preview, it may be subject to limitations such as restricted language coverage, evolving API stability, and potential constraints on voice cloning accuracy or sample length. Users should review documentation for supported languages and cloning requirements. Privacy and ethical considerations are paramount when using voice cloning, particularly regarding consent for voice replication and compliance with data protection regulations. Performance and scalability may vary during the preview phase, and production workloads should be monitored accordingly.

**Integration with Related Azure Services**  
MAI-Voice-2 in Microsoft Foundry can be integrated with other Azure services to build comprehensive solutions. For example, it can be combined with Azure Cognitive Services for speech recognition and translation, Azure Bot Service for conversational AI, and Azure Media Services for content delivery. Developers can leverage Foundry’s APIs to orchestrate workflows involving speech synthesis, voice cloning, and multilingual output, ensuring seamless interoperability across Azure’s AI ecosystem.

**Summary Sentence**  
Microsoft Foundry’s public preview of MAI-Voice-2 introduces advanced, multilingual natural speech generation and voice cloning capabilities, enabling developers and enterprises to create personalized, context-aware voice solutions with integration options across Azure’s AI services.

---

### 2. General Availability: Backup your ledger files for audit with Azure confidential ledger’s new tool 

**Published**: June 03, 2026 22:15:24 UTC
**Link**: [General Availability: Backup your ledger files for audit with Azure confidential ledger’s new tool ](https://azure.microsoft.com/updates?id=560810)

**Update ID**: 560810
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Security, Storage, Azure confidential ledger, Features, SDK and Tools, Services

**Summary**:

**What was updated**  
Azure Confidential Ledger has released a new tool for securely backing up ledger files, now generally available.

**Key changes or new features**  
- Introduction of a localized, web-based ledger file backup tool.
- Enables secure backup of ledger files for audit and compliance purposes.
- Auditing personas (e.g., security analysts, external auditors) can independently access and verify ledger files.
- Provides cryptographic proofs to establish trust in the integrity and authenticity of the backed-up data.

**Target audience affected**  
- Developers integrating Azure Confidential Ledger into applications requiring audit trails.
- IT professionals responsible for compliance, security, and audit processes.
- Security analysts and external auditors needing independent access to ledger data.

**Important notes if any**  
- The tool supports secure, tamper-evident backups, enhancing compliance with regulatory and internal audit requirements.
- It simplifies the process of sharing ledger data with auditors while maintaining data confidentiality and integrity.
- No changes are required to existing ledger workflows; the tool operates alongside current Azure Confidential Ledger deployments.

[Read more on the Azure Update page.](https://azure.microsoft.com/updates?id=560810)

**Details**:

**Azure Update Report**

**Title:** General Availability: Backup your ledger files for audit with Azure confidential ledger’s new tool  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=560810)

---

**Background and Purpose of the Update**

Azure Confidential Ledger (ACL) is designed to provide tamper-proof, cryptographically verifiable records for sensitive business operations. The update addresses the need for organizations to enable auditing personas—such as internal security analysts or external security assessment contractors—to access ledger files and independently verify cryptographic proofs. This capability is crucial for compliance, regulatory audits, and establishing trust in the integrity of ledger data.

---

**Specific Features and Detailed Changes**

This update introduces a new localized, web ledger tool for Azure Confidential Ledger, now generally available. The tool allows users to backup ledger files specifically for audit purposes. Key features include:

- **Backup Functionality:** Enables secure extraction and storage of ledger files from ACL for external review.
- **Audit Accessibility:** Provides a mechanism for authorized auditing personas to view ledger files without compromising ledger integrity.
- **Cryptographic Proof Verification:** Facilitates independent validation of cryptographic proofs embedded in ledger files, ensuring the authenticity and immutability of records.

---

**Technical Mechanisms and Implementation Methods**

The new tool operates as a web-based interface, allowing localized access to ledger files stored within Azure Confidential Ledger. The technical workflow involves:

- **Ledger File Export:** The tool securely exports ledger files from ACL, preserving their cryptographic signatures and proofs.
- **Proof Verification:** Auditors can use the tool to verify cryptographic proofs (such as hash chains or digital signatures) associated with each ledger entry, confirming that records have not been tampered with.
- **Access Controls:** The tool is designed to ensure only authorized auditing personas can access the exported ledger files, maintaining confidentiality and compliance with organizational security policies.

---

**Use Cases and Application Scenarios**

- **Regulatory Compliance Audits:** Organizations can provide auditors with access to ledger files and cryptographic proofs, streamlining compliance verification.
- **Internal Security Reviews:** Security analysts can independently validate ledger integrity as part of routine security assessments.
- **Third-Party Security Assessments:** Contractors and external auditors can review ledger files without direct access to the ACL environment, reducing risk and simplifying audit processes.

---

**Important Considerations and Limitations**

- **Access Management:** Proper configuration of access controls is essential to ensure only authorized auditing personas can use the tool.
- **Data Confidentiality:** While the tool facilitates backup and export, organizations must ensure that exported ledger files are stored securely and handled in accordance with data protection policies.
- **Scope of Audit:** The tool is intended for audit purposes; it does not alter or modify ledger files, preserving the integrity of the original records.
- **Cryptographic Proofs:** Auditors must have the necessary technical understanding to verify cryptographic proofs using the tool.

---

**Integration with Related Azure Services**

The new tool is tightly integrated with Azure Confidential Ledger, leveraging its secure, immutable ledger infrastructure. It can be used alongside other Azure security and compliance services, such as Azure Key Vault for cryptographic key management and Azure Active Directory for access control and authentication.

---

**Summary Sentence**

Azure Confidential Ledger’s new localized, web ledger tool now enables secure backup and audit of ledger files, allowing authorized auditing personas to independently verify cryptographic proofs and establish trust in ledger integrity for compliance and security assessments.

---

### 3. Generally Available: Text Analytics for Health NextGen Playground in Azure AI Language

**Published**: June 03, 2026 21:15:57 UTC
**Link**: [Generally Available: Text Analytics for Health NextGen Playground in Azure AI Language](https://azure.microsoft.com/updates?id=563671)

**Update ID**: 563671
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Text Analytics for Health (TA4H) NextGen Playground is now generally available within the Microsoft Foundry portal as part of Azure AI Language.

- Key changes or new features  
The NextGen Playground enables users to interactively test and evaluate the latest TA4H models. Users can paste clinical texts such as discharge summaries, doctor’s notes, or research abstracts to extract structured medical information (e.g., medical conditions, medications, procedures, and relationships) using the latest AI models. The playground offers an improved user interface and access to advanced model capabilities for healthcare text analytics.

- Target audience affected  
This update is relevant for clinical informatics teams, independent software vendors (ISVs), developers, and IT professionals working with healthcare data, especially those building or integrating healthcare applications with Azure AI Language services.

- Important notes if any  
The playground is accessible via the Microsoft Foundry portal and supports hands-on experimentation with real-world clinical data. This enables rapid prototyping and evaluation of healthcare NLP scenarios before integrating the TA4H API into production solutions. Developers should review documentation for API usage and compliance with healthcare data privacy regulations.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=563671

**Details**:

**Azure Update Report: Generally Available – Text Analytics for Health NextGen Playground in Azure AI Language**

**Background and Purpose of the Update:**  
The general availability (GA) of the next-generation Text Analytics for Health (TA4H) playground in Azure AI Language, accessible via the Microsoft Foundry portal, marks a significant milestone in the evolution of healthcare-focused natural language processing (NLP) on Azure. This update is designed to empower clinical informatics teams and independent software vendors (ISVs) with advanced tools to extract structured information from unstructured clinical text, such as discharge summaries, doctor’s notes, and research abstracts. The purpose is to streamline the exploration and evaluation of Azure’s healthcare NLP capabilities in a user-friendly, interactive environment.

**Specific Features and Detailed Changes:**  
- **General Availability:** The TA4H NextGen playground is now fully supported and production-ready within the Microsoft Foundry portal.
- **Interactive Interface:** Users can directly paste clinical documents (e.g., discharge summaries, doctor’s notes, research abstracts) into the playground for immediate analysis.
- **Healthcare NLP Models:** The playground leverages Azure AI Language’s latest Text Analytics for Health models, which are optimized for extracting medical entities, relationships, and key clinical information from free-text data.
- **No-code Exploration:** The playground offers a no-code, browser-based interface, lowering the barrier for technical and non-technical users to evaluate healthcare text analytics capabilities.

**Technical Mechanisms and Implementation Methods:**  
- **Azure AI Language Service:** The playground is built on top of Azure AI Language, utilizing the Text Analytics for Health API endpoints.
- **Data Processing:** When users paste clinical text into the playground, the underlying service processes the input using pre-trained healthcare NLP models to identify and extract relevant medical entities (e.g., conditions, medications, procedures) and their relationships.
- **Microsoft Foundry Portal Integration:** The playground is hosted within the Microsoft Foundry portal, providing a secure, web-based environment for experimentation without the need for local installation or configuration.

**Use Cases and Application Scenarios:**  
- **Clinical Informatics:** Rapid prototyping and evaluation of NLP models on real-world clinical documents to support downstream analytics, decision support, or research.
- **ISV Solution Development:** Independent software vendors can assess Azure’s healthcare NLP capabilities for integration into their own health IT solutions.
- **Research:** Researchers can analyze research abstracts or clinical trial summaries to extract structured data for further study or meta-analysis.

**Important Considerations and Limitations:**  
- **Data Privacy:** Users should ensure that any clinical text pasted into the playground complies with organizational and regulatory privacy requirements, as the data is processed in the cloud.
- **Scope of Analysis:** The playground is intended for exploration and evaluation; production-scale processing should leverage the full Azure AI Language APIs with appropriate security and compliance configurations.
- **Supported Document Types:** The playground is optimized for typical clinical narratives (discharge summaries, doctor’s notes, research abstracts); performance on other document types may vary.

**Integration with Related Azure Services:**  
- **Azure AI Language:** The playground directly utilizes the Text Analytics for Health capabilities within Azure AI Language.
- **Microsoft Foundry Portal:** Provides the hosting and user interface for the playground.
- **Potential Downstream Integration:** Results from the playground can inform further integration with Azure Data Lake, Azure Synapse Analytics, or custom healthcare applications via the full Azure AI Language APIs.

**Summary Sentence:**  
The general availability of the Text Analytics for Health NextGen playground in Azure AI Language provides clinical informatics teams and ISVs with an interactive, no-code environment in the Microsoft Foundry portal to evaluate and extract structured clinical information from unstructured healthcare text using Azure’s advanced NLP models.

---

### 4. Public Preview: User feedback logging in Microsoft Foundry

**Published**: June 03, 2026 21:15:57 UTC
**Link**: [Public Preview: User feedback logging in Microsoft Foundry](https://azure.microsoft.com/updates?id=563431)

**Update ID**: 563431
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry now supports public preview of user feedback logging, allowing structured feedback collection from end users interacting with AI agents.

- Key changes or new features  
Developers can now capture and log real-time user feedback signals—such as thumbs up/down, ratings, and custom annotations—directly from AI agent interactions. This feedback is automatically associated with relevant data, enabling easier tracking and analysis of user sentiment and agent performance. The feature is accessible via API, supporting integration into existing workflows.

- Target audience affected  
Developers building AI agents and IT professionals managing AI solutions with Microsoft Foundry.

- Important notes if any  
This feature is in public preview and may be subject to changes. It enables more effective monitoring, debugging, and continuous improvement of AI agents based on real user input. Developers should review API documentation for integration details and ensure compliance with data privacy requirements when handling user feedback.

Data source: Using API data  
[Azure Update: User feedback logging in Microsoft Foundry (Public Preview)](https://azure.microsoft.com/updates?id=563431)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: User feedback logging in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563431)

---

**Background and Purpose of the Update:**  
The introduction of user feedback logging in Microsoft Foundry addresses the growing need for developers to systematically collect and analyze end user feedback on AI agent interactions. As AI-driven applications become more prevalent, capturing real-world user responses is critical for iterative improvement, model evaluation, and ensuring alignment with user expectations. This update aims to provide a structured mechanism for gathering actionable feedback directly from users, thereby enhancing the development lifecycle of AI agents.

**Specific Features and Detailed Changes:**  
- **Structured Feedback Capture:** Developers can now log various types of user feedback, including binary signals (thumbs up/down), scalar ratings, and custom annotations.  
- **Automatic Association:** The feedback collected is automatically linked to the relevant AI agent interactions, ensuring context is preserved for downstream analysis.  
- **Semantics for Feedback Logging:** The update introduces standardized semantics for capturing and storing feedback, enabling consistent data collection across different AI agent implementations within Microsoft Foundry.

**Technical Mechanisms and Implementation Methods:**  
- **Feedback Logging API/Interface:** The feature provides an interface (likely via SDK or API) that developers can integrate into their AI agents to capture user feedback events.  
- **Data Structuring:** Feedback is captured in a structured format, supporting both predefined (e.g., thumbs up/down, ratings) and custom annotation schemes.  
- **Automatic Contextual Linking:** When feedback is submitted, it is programmatically associated with the corresponding AI agent session or interaction, ensuring traceability and facilitating later analysis.

**Use Cases and Application Scenarios:**  
- **Model Evaluation and Tuning:** Developers can use real user feedback to assess AI agent performance, identify failure points, and prioritize areas for improvement.  
- **User Experience Optimization:** Continuous feedback enables rapid iteration on conversational flows, response accuracy, and overall agent usability.  
- **Compliance and Monitoring:** Structured feedback logs can be used for compliance tracking, auditing, and monitoring user satisfaction trends over time.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may be subject to changes, limited support, and potential instability.  
- **Data Privacy and Compliance:** Developers must ensure that the collection and storage of user feedback comply with organizational and regulatory privacy requirements.  
- **Integration Scope:** The feature is currently specific to Microsoft Foundry and may not be directly portable to other platforms or AI frameworks.

**Integration with Related Azure Services:**  
- **Microsoft Foundry Ecosystem:** The feedback logging feature is designed to integrate seamlessly within the Microsoft Foundry platform, supporting AI agent development workflows.  
- **Potential for Analytics Integration:** While not explicitly stated, structured feedback data can be exported or connected to Azure analytics services (such as Azure Monitor or Azure Synapse Analytics) for deeper insights, provided such integrations are supported within Foundry.

---

**Summary Sentence:**  
The public preview of user feedback logging in Microsoft Foundry enables developers to systematically capture and associate structured end user feedback—such as ratings and annotations—with AI agent interactions, supporting data-driven improvement and analysis within the Foundry platform.

---

### 5. Generally Available: Self-serve custom photo avatar creation in Microsoft Foundry

**Published**: June 03, 2026 20:45:02 UTC
**Link**: [Generally Available: Self-serve custom photo avatar creation in Microsoft Foundry](https://azure.microsoft.com/updates?id=563491)

**Update ID**: 563491
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Self-serve custom photo avatar creation is now generally available in the Microsoft Foundry NextGen fine-tuning portal.

- Key changes or new features  
Enterprise customers can now independently create custom photo avatars using a self-service workflow within the Foundry portal. This enables organizations to generate branded avatars for use in voice agents or content production, without requiring manual intervention from Microsoft. The feature streamlines avatar creation, allowing for faster and more scalable deployment of personalized avatars.

- Target audience affected  
This update is relevant for developers, IT professionals, and enterprise teams building conversational AI solutions, virtual agents, or content experiences that require custom avatars and speech synthesis.

- Important notes if any  
The self-serve capability removes dependency on Microsoft support for avatar creation, accelerating development cycles. Organizations can maintain brand consistency by generating avatars tailored to their requirements. Access is available through the Foundry NextGen fine-tuning portal. For further details and prerequisites, refer to the official documentation.

**Details**:

**Azure Update Explanation: Generally Available: Self-serve custom photo avatar creation in Microsoft Foundry**

**Background and Purpose of the Update:**  
This update announces the general availability (GA) of self-serve custom photo avatar creation within the Microsoft Foundry NextGen fine-tuning portal. The primary purpose is to empower enterprise customers to create branded, custom avatars for use in voice agents or content production scenarios where avatars and speech synthesis are required. Previously, organizations often relied on generic avatars or required manual processes to generate custom avatars, which could be time-consuming and less aligned with their branding needs.

**Specific Features and Detailed Changes:**  
- **Self-serve Custom Avatar Creation:** Users can now independently generate custom photo avatars directly within the Foundry NextGen portal, streamlining the process and reducing dependency on external support.
- **General Availability:** The feature is now fully supported and production-ready, moving beyond preview or limited-access phases.
- **Integration in Fine-tuning Portal:** The capability is embedded in the fine-tuning portal, ensuring a unified workflow for avatar creation and subsequent model customization.

**Technical Mechanisms and Implementation Methods:**  
- **Portal-based Workflow:** The self-serve functionality is accessible through the Foundry NextGen fine-tuning portal, providing a web-based interface for uploading photos and configuring avatar parameters.
- **Photo-based Avatar Generation:** The system utilizes user-provided photos to generate digital avatars, likely leveraging advanced AI and image processing pipelines (as inferred from the context of "photo avatar creation"), though specific algorithms or model details are not disclosed in the update.
- **Seamless Integration with Voice and Speech:** The created avatars are designed for immediate use in scenarios involving voice agents and speech synthesis, ensuring compatibility with downstream content production and conversational AI workflows.

**Use Cases and Application Scenarios:**  
- **Branded Voice Agents:** Enterprises can deploy voice agents with avatars that reflect their brand identity, enhancing user engagement and trust.
- **Content Production:** Organizations producing multimedia content can incorporate custom avatars with synchronized speech, improving personalization and consistency across digital assets.
- **Rapid Prototyping and Deployment:** The self-serve model accelerates the creation and iteration of avatars, supporting agile development cycles for conversational AI and digital assistant projects.

**Important Considerations and Limitations:**  
- **Photo Input Requirements:** While not detailed in the update, users should ensure that input photos meet any specified quality or format guidelines to achieve optimal avatar results.
- **Enterprise Focus:** The feature is targeted at enterprise customers, which may imply licensing or access restrictions for non-enterprise users.
- **Data Privacy and Compliance:** Organizations should consider compliance with internal and external privacy policies when uploading and processing user or employee photos.

**Integration with Related Azure Services:**  
- **Microsoft Foundry Ecosystem:** The avatar creation feature is part of the broader Foundry platform, which supports fine-tuning and deployment of AI models, including those for conversational AI and digital content.
- **Speech and Voice Services:** Avatars created can be integrated with Azure’s speech synthesis and voice agent services, facilitating end-to-end solutions for interactive digital experiences.

**Summary Sentence:**  
Self-serve custom photo avatar creation in Microsoft Foundry is now generally available, enabling enterprise customers to efficiently generate branded avatars for voice agents and content production directly within the Foundry NextGen fine-tuning portal.

---

### 6. Generally Available: Azure Red Hat OpenShift in Belgium Central

**Published**: June 03, 2026 19:15:46 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift in Belgium Central](https://azure.microsoft.com/updates?id=564849)

**Update ID**: 564849
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Feature

**Summary**:

- What was updated  
Azure Red Hat OpenShift (ARO) is now generally available in the Azure Belgium Central region.

- Key changes or new features  
This update expands ARO’s regional availability, allowing customers to deploy fully managed OpenShift clusters in Belgium Central. Organizations can now leverage ARO’s integrated Kubernetes platform with enterprise-grade security, compliance, and scalability, hosted in Microsoft’s first Azure region in Belgium.

- Target audience affected  
Developers and IT professionals who manage containerized applications, DevOps teams, and organizations with regulatory or data residency requirements in Belgium or the broader European region.

- Important notes if any  
Customers can now deploy ARO clusters closer to end users in Belgium, improving performance and meeting local compliance needs. This launch supports scenarios requiring high availability, disaster recovery, and hybrid cloud integration within the region. Existing ARO features and SLAs apply. Review region-specific pricing and service availability before deployment.

**Details**:

**Azure Update Report: General Availability of Azure Red Hat OpenShift in Belgium Central**

**Background and Purpose of the Update**  
Azure Red Hat OpenShift (ARO) is now generally available in the Azure Belgium Central region. This update aligns with the launch of Microsoft’s first Azure region in Belgium, aiming to expand the regional availability of OpenShift-based Kubernetes deployments across Europe. The purpose is to provide Belgian and European customers with local access to a fully managed OpenShift service, supporting data residency, compliance, and reduced latency requirements.

**Specific Features and Detailed Changes**  
With this update, customers can deploy and operate Azure Red Hat OpenShift clusters directly in the Belgium Central region. The service delivers a fully managed, production-grade OpenShift environment, including automated updates, integrated security, and compliance features. The general availability status ensures that the service is supported under Microsoft’s standard SLA and is ready for production workloads.

**Technical Mechanisms and Implementation Methods**  
Azure Red Hat OpenShift is a jointly engineered, fully managed service by Microsoft and Red Hat. It provides automated cluster provisioning, scaling, patching, and integrated monitoring. The platform leverages Azure infrastructure to host OpenShift clusters, with Microsoft handling the underlying VM, networking, and storage resources. Customers interact with the OpenShift API and console for application lifecycle management, while operational tasks such as cluster upgrades and security patching are managed by Microsoft and Red Hat.

**Use Cases and Application Scenarios**  
Typical use cases include:  
- Enterprises requiring a managed Kubernetes platform with OpenShift’s developer and operational tooling.  
- Organizations with compliance or data residency requirements needing to keep workloads within Belgium.  
- Customers migrating or modernizing Java, .NET, or containerized applications using OpenShift’s CI/CD and DevOps integrations.  
- Multi-region or disaster recovery architectures leveraging Belgium Central for high availability.

**Important Considerations and Limitations**  
- The service is now generally available, meaning it is suitable for production workloads and covered by Azure’s support and SLA.  
- Customers should verify that their required Azure services and SKUs are available in Belgium Central, as regional availability may vary.  
- Data residency and compliance requirements can now be met by deploying in Belgium Central, but customers remain responsible for their own application-level compliance.

**Integration with Related Azure Services**  
Azure Red Hat OpenShift in Belgium Central integrates with other Azure services, such as Azure Active Directory for authentication, Azure Monitor for logging and metrics, and Azure Policy for governance. Customers can leverage Azure’s networking, storage, and security services to build comprehensive solutions around their OpenShift clusters.

**Summary**  
Azure Red Hat OpenShift is now generally available in the Belgium Central region, enabling customers to deploy fully managed OpenShift clusters locally and benefit from Azure’s compliance, security, and integration capabilities.

---

### 7. Public Preview: Agent-to-agent (A2A) support for Prompt agents and Hosted agents in Foundry

**Published**: June 03, 2026 19:15:46 UTC
**Link**: [Public Preview: Agent-to-agent (A2A) support for Prompt agents and Hosted agents in Foundry](https://azure.microsoft.com/updates?id=563716)

**Update ID**: 563716
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry Agent Service now supports agent-to-agent (A2A) communication in public preview for Prompt agents and Hosted agents using the responses protocol.

- Key changes or new features  
  - Agents can now directly call other agents by name via a managed endpoint.  
  - The communication is secured with built-in identity and content safety controls.  
  - This enables more complex, multi-agent workflows and orchestration scenarios.  
  - The feature is available for both Prompt agents and Hosted agents.

- Target audience affected  
  - Developers building solutions with Microsoft Foundry Agent Service, especially those leveraging Prompt agents or Hosted agents.  
  - IT professionals managing agent-based automation or orchestration in Azure environments.

- Important notes if any  
  - This feature is currently in public preview and may be subject to changes.  
  - Ensure agents use the responses protocol to leverage A2A communication.  
  - Review security and content safety implications when enabling inter-agent communication.  
  - For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=563716).

This update enables more flexible and scalable agent-based architectures, supporting advanced automation and integration scenarios within the Foundry platform.

**Details**:

**Azure Update Report: Public Preview – Agent-to-agent (A2A) Support for Prompt Agents and Hosted Agents in Foundry**

**Background and Purpose of the Update**  
The Microsoft Foundry Agent Service is designed to facilitate intelligent agent orchestration and communication within Azure environments. The introduction of agent-to-agent (A2A) communication in public preview addresses the need for scalable, modular, and collaborative agent architectures. This update specifically targets Prompt agents and Hosted agents that utilize the responses protocol, enabling direct interaction between agents to streamline workflows and enhance automation capabilities.

**Specific Features and Detailed Changes**  
The key feature of this update is A2A communication, allowing agents to invoke other agents by name through a managed endpoint. This capability is now available for Prompt agents and Hosted agents, which are agent types supported by Foundry and operate using the responses protocol. The update includes:
- Managed endpoints for agent invocation, abstracting the complexity of direct communication.
- Identity management, ensuring secure and authenticated agent calls.
- Content safety mechanisms, providing safeguards for exchanged information.

**Technical Mechanisms and Implementation Methods**  
A2A communication is implemented via managed endpoints, which serve as intermediaries for agent requests. When an agent needs to call another, it specifies the target agent by name, and the Foundry Agent Service routes the request through a secure, managed endpoint. The responses protocol governs the format and handling of messages between agents, ensuring consistency and reliability. Identity is managed as part of the endpoint invocation, likely involving authentication tokens or service principals, while content safety features are integrated to monitor and filter exchanged data.

**Use Cases and Application Scenarios**  
This update enables several practical scenarios:
- Modular agent orchestration: Agents can delegate tasks to specialized agents, improving scalability and maintainability.
- Workflow automation: Complex workflows can be broken down into agent-driven steps, with agents calling each other as needed.
- Multi-agent collaboration: Agents can share information and coordinate actions, enhancing overall system intelligence.
- Integration with external systems: Hosted agents can act as bridges to external APIs or services, invoked by Prompt agents as required.

**Important Considerations and Limitations**  
As this feature is in public preview, it may be subject to changes and is not recommended for production workloads without thorough testing. Only Prompt agents and Hosted agents using the responses protocol are supported; other agent types or protocols are not included in this release. Security and content safety are managed, but users should review and configure these features according to their organizational requirements. The managed endpoint approach abstracts direct communication, which may introduce latency or require additional configuration.

**Integration with Related Azure Services**  
The Foundry Agent Service is part of the broader Azure ecosystem and can be integrated with Azure Identity services for authentication, Azure Monitor for logging and diagnostics, and Azure Policy for governance. Agents may interact with other Azure services via Hosted agents, enabling seamless automation and orchestration across Azure resources.

**Summary Sentence**  
Microsoft Foundry Agent Service now supports agent-to-agent communication in public preview for Prompt agents and Hosted agents using the responses protocol, enabling secure, managed, and content-safe agent interactions through named endpoints.

---

### 8. Public Preview: Conversational PII NextGen Playground in Microsoft Foundry

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: Conversational PII NextGen Playground in Microsoft Foundry](https://azure.microsoft.com/updates?id=564246)

**Update ID**: 564246
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has released the Conversational PII (ConvPII) NextGen Playground in public preview.

- Key changes or new features  
The ConvPII NextGen Playground introduces:  
  - A transcript input feature allowing users to test and validate PII (Personally Identifiable Information) detection in multi-speaker dialogues.  
  - An API Configuration Panel to customize and experiment with API settings before integration.  
  - The ability for developers to evaluate PII detection accuracy and behavior in real-world conversational scenarios prior to production use.

- Target audience affected  
Developers and IT professionals working with conversational AI, transcription services, or any application processing multi-speaker dialogue that requires PII detection and redaction.

- Important notes if any  
This is a public preview, so features may change before general availability. The Playground helps teams validate PII detection workflows and fine-tune API configurations, reducing integration risk. Early feedback from users is encouraged to improve the service. For more details, visit the [Azure Update page](https://azure.microsoft.com/updates?id=564246).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Conversational PII NextGen Playground in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=564246)

---

**Background and Purpose of the Update**  
The Conversational PII (ConvPII) NextGen Playground is introduced in Microsoft Foundry as a public preview to address the growing need for robust Personally Identifiable Information (PII) detection in conversational data. With the proliferation of multi-speaker dialogues in applications such as customer support, transcription services, and chatbots, ensuring compliance with privacy regulations and protecting sensitive information is critical. This update aims to provide developers with a dedicated environment to validate and fine-tune PII detection capabilities before API integration.

**Specific Features and Detailed Changes**  
The NextGen Playground includes two primary enhancements:

1. **Transcript Input:**  
   Developers can now input multi-speaker transcripts directly into the Playground. This allows for realistic testing scenarios, reflecting actual conversational data, including speaker turns and overlapping dialogue.

2. **API Configuration Panel:**  
   The Playground features an API Configuration Panel, enabling developers to customize and validate API parameters for PII detection. This panel facilitates experimentation with different settings, such as detection thresholds, entity types, and output formats, without the need to deploy or integrate the API into production environments.

**Technical Mechanisms and Implementation Methods**  
The Playground leverages Microsoft Foundry’s underlying conversational AI and PII detection models. The transcript input is processed using advanced natural language processing (NLP) techniques to identify PII entities across multiple speakers. The API Configuration Panel interacts with the ConvPII API endpoints, allowing real-time adjustments and immediate feedback on detection results. This iterative approach supports rapid prototyping and validation of PII detection logic.

**Use Cases and Application Scenarios**  
- **Customer Support Transcripts:** Developers can validate PII detection in call center logs, ensuring sensitive data is masked or redacted before storage or analysis.
- **Meeting Transcriptions:** Organizations can test PII detection in business meeting transcripts, protecting participant information.
- **Chatbot Conversations:** Teams can simulate multi-user chatbot interactions to ensure compliance with privacy standards.
- **Compliance Auditing:** IT professionals can use the Playground to demonstrate and document PII detection efficacy for regulatory audits.

**Important Considerations and Limitations**  
- **Public Preview Status:** The Playground is in public preview, meaning it may not be fully stable or feature-complete. Production usage should be approached cautiously.
- **Transcript Format:** The effectiveness of PII detection depends on the quality and format of the transcript input. Developers should ensure transcripts accurately represent speaker turns and conversational context.
- **API Configuration:** While the API Configuration Panel allows for parameter adjustments, not all advanced features or customizations may be available in preview.
- **Privacy and Security:** Data entered into the Playground should not contain actual sensitive information during testing, as preview environments may not offer full security guarantees.

**Integration with Related Azure Services**  
The ConvPII NextGen Playground is part of Microsoft Foundry, which integrates with Azure’s broader suite of AI and compliance tools. Developers can use the Playground to validate PII detection before connecting with Azure Cognitive Services APIs for production deployment. The API Configuration Panel streamlines the transition from testing to integration, ensuring consistent parameter settings and detection logic across environments.

---

**Summary Sentence:**  
Microsoft Foundry’s public preview of the Conversational PII NextGen Playground provides developers with a configurable environment to validate PII detection in multi-speaker transcripts, supporting secure and compliant conversational AI solutions before API integration.

---

### 9. Public Preview: TextPII NextGen Playground updates in Microsoft Foundry

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: TextPII NextGen Playground updates in Microsoft Foundry](https://azure.microsoft.com/updates?id=564241)

**Update ID**: 564241
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

**What was updated:**  
Microsoft Foundry’s TextPII NextGen Playground has been updated and is now in public preview. The update includes enhancements to the API Configuration Panel and introduces new preview features.

**Key changes or new features:**  
- Refreshed API Configuration Panel for improved usability.
- Ability to test predefined Personally Identifiable Information (PII) categories directly in the Playground.
- Support for different redaction modes, allowing developers to evaluate and customize how PII is detected and handled.
- Preview features introduced at Ignite 2025 are now accessible for early evaluation.

**Target audience affected:**  
- Developers working with PII detection and redaction in text data.
- IT professionals responsible for data privacy, compliance, and integration of PII protection into applications.

**Important notes:**  
- This is a public preview, so features may change before general availability.
- The update enables faster prototyping and testing of PII redaction scenarios using Microsoft Foundry’s tools.
- Early adoption is encouraged for feedback, especially for teams integrating PII protection into their workflows.

[Learn more](https://azure.microsoft.com/updates?id=564241)

**Details**:

**Azure Update Technical Explanation: Public Preview – TextPII NextGen Playground Updates in Microsoft Foundry**

**Background and Purpose of the Update**  
The TextPII NextGen Playground is a component within Microsoft Foundry designed to facilitate the detection and redaction of Personally Identifiable Information (PII) in textual content. The public preview update aims to enhance the developer experience by providing a more intuitive and feature-rich interface for configuring and testing PII processing scenarios. This aligns with ongoing efforts to help organizations comply with privacy regulations and protect sensitive data during application development and testing.

**Specific Features and Detailed Changes**  
The update introduces a refreshed API Configuration Panel within the TextPII NextGen Playground. This panel incorporates preview features that were first introduced at Ignite 2025. Key enhancements include:
- The ability to test predefined PII categories, enabling users to quickly evaluate how different types of sensitive information are identified and processed.
- Support for redaction modes, allowing developers to experiment with various methods of masking or removing PII from sample text.
- An improved user interface that streamlines the configuration and testing workflow, making it easier to adjust settings and observe results in real time.

**Technical Mechanisms and Implementation Methods**  
The Playground leverages backend APIs that expose PII detection and redaction capabilities. The updated API Configuration Panel serves as a front-end interface for interacting with these APIs. Developers can select PII categories (such as names, addresses, or financial data) and choose redaction modes (such as masking, removal, or replacement). The Playground sends these configurations to the underlying APIs, which process the input text and return the redacted output. This interactive approach allows for rapid prototyping and validation of PII handling logic.

**Use Cases and Application Scenarios**  
- **Application Development:** Developers building applications that handle user-generated content can use the Playground to test how their systems will process and protect PII before deploying to production.
- **Compliance Validation:** Security and compliance teams can validate that PII detection and redaction meet organizational and regulatory requirements.
- **Integration Testing:** Teams integrating PII redaction into data pipelines or analytics workflows can simulate various scenarios and fine-tune their configurations.

**Important Considerations and Limitations**  
- The features are in public preview, which means they are subject to change and may not be fully supported for production workloads.
- Only predefined PII categories and redaction modes are available for testing; custom categories or advanced configurations may not be supported in this version.
- The update is limited to the Playground environment within Microsoft Foundry and may not reflect the full capabilities of production APIs.

**Integration with Related Azure Services**  
While the update is specific to Microsoft Foundry, the TextPII NextGen Playground can be used in conjunction with other Azure data protection and compliance services. For example, insights gained from the Playground can inform configurations for Azure Cognitive Services Text Analytics or Azure Purview Data Loss Prevention policies. This facilitates a cohesive approach to PII management across the Azure ecosystem.

**Summary**  
The public preview of the updated TextPII NextGen Playground in Microsoft Foundry introduces a refreshed API Configuration Panel and new preview features, enabling developers to efficiently test PII detection and redaction scenarios using predefined categories and redaction modes.

---

### 10. Public Preview: Observability developer experience in Azure Developer CLI (azd)

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: Observability developer experience in Azure Developer CLI (azd)](https://azure.microsoft.com/updates?id=563736)

**Update ID**: 563736
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Azure Developer CLI (azd) now includes a public preview of enhanced observability features for the developer experience, specifically supporting the evaluation of agents created with Microsoft Foundry.

- Key changes or new features  
Developers can now use azd to add a "measured quality loop" to agents built with Microsoft Foundry. This includes new CLI commands and workflows for creating, provisioning, deploying, and initializing evaluation assets directly within the azd tool. The update streamlines the process of integrating observability and evaluation into the agent lifecycle, making it easier to monitor, measure, and improve agent quality during development.

- Target audience affected  
This update is targeted at developers and DevOps engineers using Azure Developer CLI (azd) to build, deploy, and manage AI agents with Microsoft Foundry. IT professionals involved in application lifecycle management and observability will also benefit.

- Important notes if any  
This feature is in public preview and may be subject to changes. Users are encouraged to test the new workflows and provide feedback. Integration with observability and evaluation tools is designed to help teams maintain higher quality and reliability for AI agents throughout the development lifecycle.

Link: https://azure.microsoft.com/updates?id=563736

**Details**:

**Azure Update Report: Public Preview – Observability Developer Experience in Azure Developer CLI (azd)**

**Background and Purpose of the Update**  
This update introduces a public preview of enhanced observability features in the Azure Developer CLI (azd), specifically targeting the developer experience for agents created with Microsoft Foundry. The primary goal is to enable a measured quality loop within the development lifecycle, allowing developers to evaluate and improve the quality of their agents directly through the CLI. This aligns with the increasing demand for integrated observability and quality assessment tools in cloud-native application development.

**Specific Features and Detailed Changes**  
- **CLI Evaluation Experience**: The update adds new commands and workflows to the azd CLI, enabling users to initiate and manage evaluation processes for agents.
- **Measured Quality Loop**: Developers can now incorporate evaluation assets into the agent lifecycle, supporting continuous quality measurement and feedback.
- **Lifecycle Integration**: The update supports the full hosted-agent lifecycle within azd, including creation, provisioning, deployment, and initialization of evaluation assets.

**Technical Mechanisms and Implementation Methods**  
- **Evaluation Asset Initialization**: As part of the agent lifecycle, users can initialize evaluation assets, which are resources or configurations used to assess agent quality.
- **CLI-Driven Workflow**: All new features are accessible via the Azure Developer CLI, streamlining the process for developers who prefer command-line tooling.
- **Integration with Microsoft Foundry**: The features are designed to work with agents created using Microsoft Foundry, ensuring compatibility and a seamless workflow for Foundry-based projects.

**Use Cases and Application Scenarios**  
- **Continuous Quality Assessment**: Teams building agents with Microsoft Foundry can now automate quality checks as part of their CI/CD pipelines using azd.
- **Developer Productivity**: Developers can quickly evaluate agents during development, reducing feedback loops and improving overall code quality.
- **Lifecycle Management**: Organizations managing multiple hosted agents can standardize evaluation processes across their development teams using the CLI.

**Important Considerations and Limitations**  
- **Public Preview Status**: As this feature is in public preview, it may be subject to changes and should not be used in production environments without caution.
- **Scope**: The observability features are specifically designed for agents created with Microsoft Foundry and may not be applicable to other types of resources or workloads.
- **CLI Dependency**: All functionality is accessed through the Azure Developer CLI, requiring users to be familiar with command-line operations.

**Integration with Related Azure Services**  
- **Microsoft Foundry**: The update is tightly integrated with Microsoft Foundry, leveraging its agent creation and management capabilities.
- **Azure Resource Management**: Provisioning and deployment steps are managed through azd, ensuring compatibility with Azure’s resource management and deployment pipelines.
- **Potential for CI/CD Integration**: While not explicitly stated, the CLI-based approach facilitates integration with existing CI/CD workflows and automation tools commonly used in Azure environments.

**Summary Sentence**  
This public preview update enhances the Azure Developer CLI (azd) by introducing integrated observability and evaluation features for Microsoft Foundry agents, enabling developers to implement a measured quality loop throughout the hosted-agent lifecycle directly from the CLI.

---

### 11. Public Preview: Domain filter for specialized model discovery in Foundry model catalog

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: Domain filter for specialized model discovery in Foundry model catalog](https://azure.microsoft.com/updates?id=563731)

**Update ID**: 563731
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry model catalog now includes a domain filter feature, available in public preview.

- Key changes or new features  
A new domain filter allows users to quickly narrow down the catalog of over 1,900 AI/ML models to those relevant to specific industries or use cases. Domains covered include robotics, biomedical sciences, materials science, and more. This enhancement streamlines model discovery by letting users focus on models trained for their particular sector or application.

- Target audience affected  
Developers, data scientists, and IT professionals who use the Foundry model catalog to discover and deploy specialized AI/ML models for industry-specific solutions.

- Important notes if any  
The domain filter is currently in public preview, so features may change before general availability. Users are encouraged to provide feedback to help improve the filtering experience. This update can significantly reduce the time spent searching for relevant models, improving productivity and accelerating project development.

Data source: Using API data  
[Learn more](https://azure.microsoft.com/updates?id=563731)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Domain filter for specialized model discovery in Foundry model catalog  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563731)

---

**Background and Purpose of the Update:**  
The Microsoft Foundry model catalog is a centralized repository offering access to over 1,900 machine learning models. As the catalog has grown, users have faced challenges in efficiently identifying models tailored to specific industries or use cases. The introduction of a domain filter addresses this challenge by enabling developers and data scientists to quickly narrow down the catalog to models relevant to their particular domain, such as robotics, biomedical sciences, or materials science. The primary purpose of this update is to streamline model discovery, reduce search time, and improve the relevance of results for specialized applications.

**Specific Features and Detailed Changes:**  
The update introduces a domain filter feature in the Foundry model catalog, currently available in public preview. This filter allows users to select one or more domains from a predefined list, thereby restricting catalog search results to models that have been trained for those domains. Domains covered by the filter include, but are not limited to, robotics, biomedical sciences, and materials science. The filter is integrated into the catalog’s user interface, providing an intuitive mechanism for refining searches. This enhancement is particularly valuable given the catalog’s extensive size, ensuring users can focus on models with domain-specific applicability.

**Technical Mechanisms and Implementation Methods:**  
The domain filter is implemented as a metadata-driven search refinement tool within the Foundry model catalog. Each model in the catalog is tagged with domain-specific metadata, which is leveraged by the filter to categorize and display relevant models. The filter operates at the query layer, modifying search parameters to include domain constraints. This approach ensures that only models with matching domain tags are returned in search results. The filter is accessible through the catalog’s web interface and may also be exposed via API endpoints for programmatic access, depending on catalog capabilities.

**Use Cases and Application Scenarios:**  
- **Industry-Specific Model Selection:** A robotics engineer can use the domain filter to quickly locate models trained for robotics applications, such as object detection or motion planning.
- **Biomedical Research:** Researchers in biomedical sciences can filter for models relevant to genomics, medical imaging, or drug discovery, ensuring they access models with appropriate training data and domain expertise.
- **Materials Science:** Scientists working on materials simulation or analysis can restrict their search to models designed for materials science, improving the efficiency of model selection and integration.
- **Enterprise AI Deployment:** Organizations deploying AI solutions across multiple domains can use the filter to ensure compliance and relevance, selecting models that meet industry standards.

**Important Considerations and Limitations:**  
- The domain filter is currently in public preview, which may imply limited support or evolving functionality.
- The accuracy of filtering depends on the completeness and correctness of domain metadata tagging for each model.
- Not all domains may be represented equally; some specialized domains may have fewer models available.
- Integration with external workflows or automation may require API support, which should be verified in the catalog documentation.

**Integration with Related Azure Services:**  
The Foundry model catalog is designed to complement Azure’s broader AI and machine learning ecosystem. Models discovered using the domain filter can be integrated into Azure Machine Learning pipelines, deployed as endpoints in Azure AI services, or used in conjunction with Azure Data services for analytics and inference. The domain filter enhances interoperability by ensuring that selected models are relevant to the target application domain, facilitating smoother integration and deployment within Azure-based solutions.

---

**Summary Sentence:**  
The public preview of the domain filter in the Foundry model catalog enables developers to efficiently discover specialized models for specific industries or use cases, streamlining model selection and enhancing relevance in large-scale AI deployments.

---

### 12. Generally Available: Microsoft Foundry for Visual Studio Code (June Build 2026 refresh)

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Generally Available: Microsoft Foundry for Visual Studio Code (June Build 2026 refresh)](https://azure.microsoft.com/updates?id=563721)

**Update ID**: 563721
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Microsoft Foundry extension for Visual Studio Code is now generally available, featuring the June Build 2026 refresh.

- Key changes or new features  
  - Full model catalog: Developers can now browse and access the entire catalog of available models directly within Visual Studio Code.  
  - Model playground: Integrated tools allow users to test and experiment with models in the editor before deployment.  
  - Hosted agent deployment: Supports deploying models to hosted agents from within Visual Studio Code, streamlining the development-to-deployment workflow.  
  - Azure account integration: Developers can sign in with their Azure account for seamless access to resources and deployment capabilities.

- Target audience affected  
  - Developers building AI/ML solutions using Visual Studio Code.  
  - IT professionals managing model deployment and integration with Azure services.

- Important notes  
  - The extension is now generally available and ready for production use.  
  - Integration with Azure accounts simplifies resource management and deployment.  
  - The update enhances productivity by centralizing model management, testing, and deployment within the Visual Studio Code environment.

For more details, see the official update: https://azure.microsoft.com/updates?id=563721

**Details**:

**Background and Purpose of the Update**  
The Microsoft Foundry extension for Visual Studio Code has reached general availability with the Build 2026 refresh. This update is designed to enhance the developer experience by integrating advanced machine learning model management and deployment capabilities directly within the Visual Studio Code environment. The purpose is to streamline workflows for Azure-based AI development, allowing developers to access, test, and deploy models efficiently without leaving their code editor.

**Specific Features and Detailed Changes**  
The Build 2026 refresh introduces several key features:

- **Full Model Catalog**: Developers can now access the complete catalog of available machine learning models directly within Visual Studio Code. This catalog provides a centralized view of models, facilitating discovery and selection for various AI tasks.
- **Model Playground**: The extension includes an interactive playground where developers can experiment with models, test inputs, and observe outputs in real time. This feature supports rapid prototyping and validation of model behavior.
- **Hosted Agent Deployment**: Deployment capabilities have been integrated, enabling developers to deploy models to hosted agents directly from the editor. This streamlines the process of moving from development to production, reducing manual steps and potential errors.
- **Azure Account Integration**: Developers can sign in using their Azure account, ensuring secure access to resources and seamless integration with Azure services.

**Technical Mechanisms and Implementation Methods**  
The extension leverages Visual Studio Code’s extensibility framework to embed Azure-specific functionalities. Authentication is handled via Azure Active Directory, allowing secure access to model catalogs and deployment targets. The model catalog is likely powered by Azure Machine Learning or a similar backend, exposing APIs that the extension consumes to list, retrieve, and manage models. The model playground uses local or cloud-based inference endpoints to execute test runs, while hosted agent deployment utilizes Azure’s infrastructure for scalable and managed model serving.

**Use Cases and Application Scenarios**  
- **AI Model Development**: Developers can browse, select, and test models for integration into applications, accelerating the prototyping phase.
- **Model Validation**: The playground allows for quick validation of model performance and suitability for specific tasks.
- **Production Deployment**: Direct deployment to hosted agents enables rapid transition from development to production, supporting CI/CD workflows for machine learning projects.
- **Collaboration**: Teams can share access to the model catalog and deployment targets, improving collaboration across development and operations.

**Important Considerations and Limitations**  
- **Azure Account Requirement**: Access to features requires authentication with an Azure account, which may limit usage to organizations with Azure subscriptions.
- **Editor Dependency**: The extension is specific to Visual Studio Code; users of other IDEs will not benefit from these enhancements.
- **Resource Management**: Deployment to hosted agents may incur Azure resource costs and requires appropriate permissions and quota management.

**Integration with Related Azure Services**  
The extension is tightly integrated with Azure services, particularly Azure Machine Learning for model catalog and deployment, Azure Active Directory for authentication, and Azure-hosted agents for managed deployment. This enables developers to leverage Azure’s scalable infrastructure and security features directly from their development environment, supporting end-to-end AI workflows.

**Summary Sentence**  
The Microsoft Foundry extension for Visual Studio Code is now generally available, offering developers integrated access to a full model catalog, interactive playground, and hosted agent deployment within the editor, with seamless Azure account integration to streamline AI development and deployment workflows.

---

### 13. Public Preview: Evaluations with Intelligent Trace Sampling

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: Evaluations with Intelligent Trace Sampling](https://azure.microsoft.com/updates?id=563696)

**Update ID**: 563696
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry observability now supports intelligent trace filtering and sampling for evaluations, available in public preview.

- Key changes or new features  
  - Evaluations no longer run against all production traces.  
  - Foundry uses a multi-stage machine learning-based approach to select a representative subset of traces.  
  - This intelligent sampling improves the efficiency and relevance of evaluations, reducing resource consumption and noise from redundant data.

- Target audience affected  
  - Developers and IT professionals using Microsoft Foundry for observability and trace analysis.  
  - Teams responsible for application monitoring, diagnostics, and performance evaluation in production environments.

- Important notes if any  
  - The feature is currently in public preview and may evolve based on user feedback.  
  - Intelligent sampling can help reduce costs and improve the signal-to-noise ratio in trace-based evaluations, but users should validate that critical traces are still being captured for their scenarios.  
  - Integration and configuration details are available in the official documentation.  

For more information, see the [Azure Update](https://azure.microsoft.com/updates?id=563696).

**Details**:

**Azure Update Report: Public Preview – Evaluations with Intelligent Trace Sampling**

**Background and Purpose of the Update:**  
Microsoft Foundry observability has introduced intelligent trace filtering and sampling for evaluations, now available in public preview. Traditionally, evaluations were performed against all production traces, which could be resource-intensive and inefficient. The primary purpose of this update is to optimize the evaluation process by selecting a representative subset of traces, thereby reducing computational overhead and improving the efficiency of observability workflows.

**Specific Features and Detailed Changes:**  
The update enables Foundry to perform evaluations using a subset of traces rather than the entire production dataset. This subset is chosen through a multi-stage mechanism, which intelligently filters and samples traces to ensure that the selected data is representative of the overall trace population. The change shifts the evaluation paradigm from exhaustive analysis to targeted sampling, allowing for faster and more scalable observability processes.

**Technical Mechanisms and Implementation Methods:**  
The intelligent trace sampling is implemented via a multi-stage mechanism. While the detailed algorithm is not specified in the provided content, the mechanism involves filtering traces based on defined criteria and then sampling from the filtered set to create a subset for evaluation. This approach leverages statistical and heuristic methods to maintain the representativeness of the sampled traces, ensuring that evaluations yield meaningful insights without requiring full dataset analysis. The process is integrated into the Foundry observability platform, allowing seamless adoption for existing workflows.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial in scenarios where production environments generate large volumes of trace data, such as microservices architectures, distributed systems, or high-traffic web applications. IT professionals can use intelligent trace sampling to perform performance evaluations, anomaly detection, and root cause analysis more efficiently. The feature is suited for organizations seeking to optimize their observability pipelines, reduce infrastructure costs, and maintain high evaluation accuracy without exhaustive data processing.

**Important Considerations and Limitations:**  
While intelligent sampling improves efficiency, it is important to recognize that evaluations are conducted on a subset of traces rather than the full dataset. This may introduce sampling bias if the subset is not adequately representative. IT professionals should review sampling configurations and ensure that the selected traces align with their observability goals. Additionally, as this feature is in public preview, it may be subject to changes and may not offer full production support or SLA guarantees.

**Integration with Related Azure Services:**  
The intelligent trace sampling feature is integrated within the Microsoft Foundry observability platform, which is designed to work with Azure-based workloads. Foundry can ingest trace data from Azure services such as Azure Application Insights, Azure Monitor, and other telemetry sources. The sampling mechanism enhances Foundry’s interoperability with these services by enabling more efficient trace evaluations, thereby complementing existing observability and monitoring solutions within the Azure ecosystem.

**Summary Sentence:**  
Microsoft Foundry observability now offers intelligent trace filtering and sampling for evaluations in public preview, enabling IT professionals to perform efficient and scalable trace analysis using a representative subset of production traces through a multi-stage mechanism.

---

### 14. Generally Available: Custom Voice portal experience in Microsoft Foundry

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Generally Available: Custom Voice portal experience in Microsoft Foundry](https://azure.microsoft.com/updates?id=563691)

**Update ID**: 563691
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
The Custom Voice authoring experience for Azure AI Speech is now generally available within the Microsoft Foundry portal.

- Key changes or new features  
  - Custom Voice customers can now use the Microsoft Foundry portal to:
    - Upload voice talent recordings and consent statements.
    - Perform data quality checks.
    - Train neural voice models.
    - Manage and deploy custom voice models directly from the portal.
  - The portal streamlines the end-to-end workflow for creating and managing custom neural voices.

- Target audience affected  
  - Developers and IT professionals working with Azure AI Speech, especially those building applications that require custom neural voice models.
  - Organizations with approved access to Custom Voice features.

- Important notes if any  
  - Only approved Custom Voice customers can access these features in the Microsoft Foundry portal.
  - This update centralizes and simplifies the Custom Voice workflow, improving efficiency and model management.
  - Existing users should transition their authoring activities to the Microsoft Foundry portal for the latest capabilities and support.

Data source: Using API data  
More info: [Azure Update link](https://azure.microsoft.com/updates?id=563691)

**Details**:

**Comprehensive Technical Explanation: Generally Available: Custom Voice portal experience in Microsoft Foundry**

**Background and Purpose of the Update**  
This update announces the general availability of the Custom Voice authoring experience within the Microsoft Foundry portal for Azure AI Speech. The primary purpose is to streamline and centralize the workflow for Custom Voice customers, allowing them to manage all aspects of voice model creation and deployment in a unified portal environment.

**Specific Features and Detailed Changes**  
With this update, approved Custom Voice customers gain access to the following capabilities directly within the Microsoft Foundry portal:
- Uploading voice talent recordings and consent statements.
- Running data quality checks on submitted recordings.
- Training neural voice models using the provided data.

This transition moves the authoring experience from previous interfaces into the Microsoft Foundry portal, providing a consolidated and enhanced user experience for voice model management.

**Technical Mechanisms and Implementation Methods**  
The Microsoft Foundry portal serves as the new interface for Custom Voice operations. Customers interact with the portal to upload required audio data and consent documentation. The system then performs automated data quality checks to ensure recordings meet the necessary standards for neural voice training. Once validated, the portal enables the initiation of neural voice training jobs, leveraging Azure AI Speech’s backend infrastructure for model creation.

**Use Cases and Application Scenarios**  
This update is particularly relevant for organizations developing custom neural voice models for applications such as:
- Interactive voice response (IVR) systems.
- Virtual assistants and chatbots.
- Accessibility tools (e.g., text-to-speech for visually impaired users).
- Content creation and media production requiring unique branded voices.

The streamlined portal experience supports efficient management of voice data and model training workflows, reducing operational overhead and improving time-to-market for voice-enabled solutions.

**Important Considerations and Limitations**  
- Access to the Custom Voice features in Microsoft Foundry is limited to approved customers only. Organizations must undergo an approval process to utilize these capabilities.
- The portal enforces the requirement for consent statements, ensuring compliance with ethical and legal standards for voice data usage.
- Data quality checks are mandatory and must be passed before training can proceed, which may require customers to adhere to specific recording guidelines.

**Integration with Related Azure Services**  
The Custom Voice capabilities in Microsoft Foundry are part of the broader Azure AI Speech service ecosystem. Trained neural voice models can be integrated with other Azure services such as:
- Azure Cognitive Services for speech synthesis and recognition.
- Azure Bot Service for conversational AI scenarios.
- Azure Media Services for content production workflows.

This integration enables seamless deployment of custom voices across diverse Azure-powered applications.

**Summary Sentence**  
The Custom Voice authoring experience is now generally available in the Microsoft Foundry portal, enabling approved customers to upload voice recordings and consent statements, perform data quality checks, and train neural voice models within a unified Azure AI Speech workflow.

---

### 15. Public Preview: Rubric evaluator in Microsoft Foundry

**Published**: June 03, 2026 19:00:25 UTC
**Link**: [Public Preview: Rubric evaluator in Microsoft Foundry](https://azure.microsoft.com/updates?id=563656)

**Update ID**: 563656
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has released rubric evaluators in public preview, enabling the measurement of agent quality for both single-turn and multi-turn agent flows.

- Key changes or new features  
Rubric evaluators allow developers to define custom, context-specific evaluation criteria for agents using prompts. This feature supports more granular and relevant quality assessment of conversational agents, improving testing and validation workflows. The evaluators can be integrated into production pipelines, facilitating automated and repeatable agent quality checks.

- Target audience affected  
Developers and IT professionals building, testing, or maintaining conversational agents using Microsoft Foundry, especially those focused on agent quality assurance and evaluation.

- Important notes if any  
The feature is currently in public preview, so it may not be suitable for production-critical scenarios. Developers can leverage rubric evaluators to automate agent quality assessments and tailor evaluation criteria to specific use cases, enhancing both development and operational workflows. Early adoption feedback is encouraged to help refine the feature before general availability.

Data source: Using API data  
More details: [Azure Update](https://azure.microsoft.com/updates?id=563656)

**Details**:

**Azure Update Report: Public Preview – Rubric Evaluator in Microsoft Foundry**

**Background and Purpose of the Update:**  
Microsoft Foundry has introduced rubric evaluators in public preview to address the need for systematic and context-specific measurement of agent quality. As conversational and autonomous agents become more prevalent in enterprise applications, ensuring their outputs meet defined quality standards is critical. This update aims to provide developers with a structured mechanism to evaluate agent performance, both in single-turn (one interaction) and multi-turn (multi-step conversation) agent flows.

**Specific Features and Detailed Changes:**  
The public preview of rubric evaluators in Microsoft Foundry introduces the following capabilities:
- **Customizable Evaluation Criteria:** Developers can define context-specific rubrics using agent prompts. This allows for granular assessment tailored to the agent’s intended use case.
- **Support for Single-Turn and Multi-Turn Flows:** The evaluator can be applied to both isolated agent responses and extended conversational exchanges, covering a broad spectrum of agent interaction patterns.
- **Integration with Production Workflows:** The rubric evaluators are designed to be used in production environments, enabling ongoing quality assurance as agents are deployed and evolve.

**Technical Mechanisms and Implementation Methods:**  
Rubric evaluators function by allowing developers to specify evaluation rubrics—structured sets of criteria—within Microsoft Foundry. These rubrics are then used to automatically or semi-automatically assess agent outputs. The evaluation process leverages agent prompts to contextualize the assessment, ensuring that the evaluation criteria are relevant to the specific task or conversation flow. The mechanism supports both pre-deployment testing and post-deployment monitoring, facilitating continuous improvement of agent quality.

**Use Cases and Application Scenarios:**  
- **Conversational AI Quality Assurance:** Teams deploying chatbots or virtual assistants can use rubric evaluators to ensure responses meet organizational standards for accuracy, relevance, and tone.
- **Iterative Agent Development:** During the development lifecycle, rubric evaluators help developers identify and address quality gaps before production deployment.
- **Compliance and Governance:** Organizations with regulatory or compliance requirements can define rubrics that enforce adherence to specific guidelines, using the evaluator to monitor and report on agent behavior.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may be subject to change and may not be suitable for all production workloads. Users should monitor for updates and be prepared for potential modifications in functionality.
- **Scope of Evaluation:** The effectiveness of the rubric evaluator depends on the quality and specificity of the rubrics defined by the developer. Poorly defined criteria may result in inadequate assessments.
- **Integration Requirements:** Users should ensure compatibility with their existing agent frameworks and workflows within Microsoft Foundry.

**Integration with Related Azure Services:**  
While the update specifically pertains to Microsoft Foundry, rubric evaluators can be integrated into broader Azure-based agent development pipelines. They complement Azure’s suite of AI and agent development tools by providing an additional layer of quality control. Developers leveraging Azure Cognitive Services or Azure Bot Services can incorporate rubric evaluators as part of their agent validation and monitoring processes within the Foundry environment.

**Summary Sentence:**  
Microsoft Foundry’s public preview of rubric evaluators enables developers to define and apply context-specific evaluation criteria for measuring agent quality in both single-turn and multi-turn flows, supporting systematic quality assurance and continuous improvement of conversational and autonomous agents.

---

### 16. Announcing: Confidential Live Migration for Intel TDX confidential VMs in Azure

**Published**: June 03, 2026 18:15:04 UTC
**Link**: [Announcing: Confidential Live Migration for Intel TDX confidential VMs in Azure](https://azure.microsoft.com/updates?id=565000)

**Update ID**: 565000
**Data source**: Azure Updates API

**Categories**: In development, Compute, Virtual Machines, Microsoft Build

**Summary**:

- What was updated  
Microsoft announced Confidential Live Migration support for Intel TDX-based Confidential VMs in Azure.

- Key changes or new features  
Confidential Live Migration enables seamless migration of running Intel TDX Confidential VMs between physical hosts during platform servicing or maintenance, without exposing VM memory or data to the underlying Azure infrastructure. This feature maintains the confidentiality and integrity of VM workloads throughout the migration process, leveraging Intel TDX hardware-based security. It ensures minimal downtime and improved availability for sensitive workloads.

- Target audience affected  
This update is relevant for developers, IT professionals, and organizations running or planning to deploy Intel TDX Confidential VMs in Azure, especially those with strict security and compliance requirements.

- Important notes if any  
Confidential Live Migration is designed to support operational continuity during Azure platform updates and servicing, reducing the need for planned downtime. It is currently available for Intel TDX-based Confidential VMs. Customers should review Azure documentation for supported VM sizes and regions. No application changes are required to benefit from this feature, but VM configuration and compliance requirements should be validated.

**Details**:

**Azure Update Report: Confidential Live Migration for Intel TDX Confidential VMs**

**Background and Purpose of the Update**  
Microsoft has introduced Confidential Live Migration in Azure, specifically targeting Intel® TDX Confidential Virtual Machines (VMs). This update addresses the need for enhanced operational flexibility and improved availability during platform servicing events. Traditionally, live migration is a critical feature in cloud environments for maintaining uptime and supporting infrastructure maintenance, but it poses challenges for confidential computing workloads due to the need to preserve data confidentiality during migration. The purpose of this update is to enable seamless migration of Intel TDX Confidential VMs without compromising their security guarantees.

**Specific Features and Detailed Changes**  
The Confidential Live Migration capability allows Intel TDX Confidential VMs to be moved between physical hosts in Azure during platform servicing, such as hardware upgrades, maintenance, or fault mitigation, without exposing sensitive data. This feature ensures that the VM’s confidential state, including memory contents and CPU registers, remains protected throughout the migration process. The update introduces mechanisms that maintain the VM’s confidentiality during migration, aligning with the security requirements of confidential computing workloads.

**Technical Mechanisms and Implementation Methods**  
Confidential Live Migration leverages Intel TDX (Trusted Domain Extensions) technology, which provides hardware-based isolation for VM memory and state. During migration, Azure orchestrates the transfer of the VM’s encrypted state between hosts, ensuring that data remains encrypted and inaccessible to the hypervisor, Azure operators, or other tenants. The migration process is designed to preserve the VM’s integrity and confidentiality, utilizing secure channels and cryptographic protections inherent to Intel TDX. The VM’s memory is encrypted in transit, and the destination host’s TDX environment validates and securely restores the VM state.

**Use Cases and Application Scenarios**  
This feature is particularly relevant for organizations running sensitive workloads on Azure, such as financial services, healthcare, and government agencies, where data confidentiality is paramount. Confidential Live Migration enables these customers to maintain high availability and operational continuity during platform maintenance without downtime or security risk. It is also useful for scenarios requiring dynamic resource allocation or scaling, as VMs can be moved securely to optimize resource utilization.

**Important Considerations and Limitations**  
IT professionals should note that Confidential Live Migration is currently applicable only to Intel TDX Confidential VMs. The migration process is tightly integrated with Azure’s platform servicing workflows and may not be available for all VM types or configurations. It is essential to verify compatibility and ensure that workloads are running on supported Intel TDX hardware. Additionally, while migration preserves confidentiality, performance impacts and migration duration should be considered when planning maintenance windows.

**Integration with Related Azure Services**  
Confidential Live Migration is integrated with Azure’s confidential computing offerings and VM management services. It complements existing features such as Azure VM availability sets, scale sets, and maintenance controls, providing a secure migration path for confidential workloads. IT professionals can leverage this capability alongside Azure’s monitoring and automation tools to orchestrate secure, high-availability operations for Intel TDX Confidential VMs.

**Summary Sentence**  
Microsoft has announced Confidential Live Migration for Intel TDX Confidential VMs in Azure, enabling secure, encrypted migration of confidential workloads during platform servicing to enhance operational flexibility and availability without compromising data confidentiality.

---

### 17. Public Preview: Azure Infrastructure Resiliency Manager

**Published**: June 03, 2026 17:15:25 UTC
**Link**: [Public Preview: Azure Infrastructure Resiliency Manager](https://azure.microsoft.com/updates?id=564759)

**Update ID**: 564759
**Data source**: Azure Updates API

**Categories**: In preview, Management, Microsoft Build

**Summary**:

- What was updated  
Azure Infrastructure Resiliency Manager is now available in public preview.

- Key changes or new features  
This new service provides a unified, goal-driven interface to help users design, assess, and improve the resiliency of their Azure applications. It integrates multiple Azure capabilities, including Availability Zones, Azure Advisor, and Chaos Studio, into a single experience. Users can evaluate their application's resiliency posture, receive actionable recommendations, and simulate real-world outages to validate recovery strategies.

- Target audience affected  
Developers, solution architects, and IT professionals responsible for application reliability and business continuity on Azure.

- Important notes if any  
The public preview allows users to proactively identify and address resiliency gaps before they impact production workloads. Integration with existing Azure tools streamlines the process of building and maintaining highly available applications. Feedback during the preview phase is encouraged to help shape the final release. For more details and access, visit the [Azure Update page](https://azure.microsoft.com/updates?id=564759).

**Details**:

**Azure Update Summary: Public Preview: Azure Infrastructure Resiliency Manager**

**Background and Purpose of the Update:**  
The Azure Infrastructure Resiliency Manager has entered public preview to address the growing need for robust application resiliency in cloud environments. As organizations increasingly rely on Azure for mission-critical workloads, ensuring high availability and minimizing downtime is essential. This update introduces a unified, goal-driven platform to streamline the design, assessment, and continuous improvement of application resiliency across Azure resources.

**Specific Features and Detailed Changes:**  
Azure Infrastructure Resiliency Manager consolidates multiple resiliency-related capabilities into a single experience. Key features include:
- **Unified Resiliency Management:** Centralized interface for managing and monitoring resiliency across Azure deployments.
- **Goal-Driven Workflows:** Users can define resiliency objectives and track progress toward meeting these goals.
- **Integration with Availability Zones:** Direct support for designing and validating workloads to leverage Azure’s Availability Zones for fault isolation.
- **Azure Advisor Integration:** Incorporates recommendations from Azure Advisor to proactively address resiliency risks.
- **Chaos Engineering Integration:** (Partial content) Suggests integration with Azure Chaos Studio or similar tools for simulating failures and validating recovery strategies.

**Technical Mechanisms and Implementation Methods:**  
The Resiliency Manager operates by aggregating telemetry and configuration data from Azure resources. It analyzes deployments against best practices for high availability, leveraging built-in integrations with Azure Advisor and Availability Zones. The platform likely uses policy-driven assessments to identify gaps and provide actionable recommendations. The goal-driven approach allows users to set specific resiliency targets, which the system continuously evaluates using collected metrics and simulated failure scenarios (via chaos engineering tools).

**Use Cases and Application Scenarios:**  
- **Enterprise Application Architects:** Design and validate resilient architectures for line-of-business applications.
- **DevOps Teams:** Continuously assess and improve resiliency posture as part of CI/CD pipelines.
- **Disaster Recovery Planning:** Evaluate and enhance failover strategies using integrated chaos engineering.
- **Regulated Industries:** Demonstrate compliance with high-availability and resiliency requirements through documented assessments.

**Important Considerations and Limitations:**  
- **Public Preview Status:** Features and integrations may be limited or subject to change; not recommended for production-critical workloads without additional validation.
- **Scope of Integration:** While the tool brings together multiple resiliency features, coverage may be incomplete for all Azure services or regions during the preview phase.
- **Dependency on Other Services:** Effectiveness relies on proper configuration of Availability Zones, Azure Advisor, and chaos engineering tools.

**Integration with Related Azure Services:**  
- **Availability Zones:** Ensures workloads are architected for zone redundancy and fault tolerance.
- **Azure Advisor:** Surfaces and tracks resiliency recommendations directly within the manager.
- **Chaos Engineering Tools:** (Implied) Enables validation of recovery strategies through controlled failure simulations.
- **Azure Resource Manager (ARM):** Likely integrates with ARM for resource discovery and policy enforcement.

**Summary:**  
Azure Infrastructure Resiliency Manager (public preview) provides a unified, goal-driven platform to design, assess, and enhance application resiliency across Azure, integrating capabilities from Availability Zones, Azure Advisor, and chaos engineering tools to help organizations proactively manage and improve their resiliency posture.

---

### 18. Generally Available: Azure Database for PostgreSQL - Flexible Server: DuckDB extension

**Published**: June 03, 2026 17:00:49 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL - Flexible Server: DuckDB extension](https://azure.microsoft.com/updates?id=563766)

**Update ID**: 563766
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL – Flexible Server now supports the DuckDB extension as a generally available feature.

- Key changes or new features  
The DuckDB extension can now be installed directly on Azure Database for PostgreSQL Flexible Server instances. DuckDB is an in-process SQL OLAP database management system designed for fast analytical query processing. This integration allows users to perform advanced analytics and data processing workloads within their PostgreSQL environment, leveraging DuckDB’s high-performance capabilities.

- Target audience affected  
Developers, data engineers, and IT professionals who use Azure Database for PostgreSQL Flexible Server and require advanced analytical processing or OLAP workloads within their PostgreSQL databases.

- Important notes if any  
To use the DuckDB extension, you may need to enable and install it on your PostgreSQL Flexible Server instance. Review the official documentation for installation steps and compatibility details. This feature enables more complex analytics scenarios without the need to move data to external systems, streamlining workflows for data-intensive applications.

**Details**:

**Comprehensive Technical Explanation: Azure Database for PostgreSQL - Flexible Server: DuckDB Extension (Generally Available)**

**Background and Purpose of the Update:**  
This update announces the general availability of the DuckDB extension for Azure Database for PostgreSQL - Flexible Server. The purpose of this update is to enable users to install and utilize the DuckDB extension within their managed PostgreSQL flexible server environments on Azure. DuckDB is an in-process SQL OLAP database management system, and its integration as an extension provides enhanced analytical capabilities directly within PostgreSQL.

**Specific Features and Detailed Changes:**  
With this update, users can now install the DuckDB extension on their Azure Database for PostgreSQL - Flexible Server instances. This extension allows PostgreSQL databases to leverage DuckDB’s analytical processing engine, which is optimized for complex analytical queries and columnar data processing. The update does not specify additional changes beyond the availability and installability of the DuckDB extension.

**Technical Mechanisms and Implementation Methods:**  
The DuckDB extension is delivered as a PostgreSQL extension package, which can be installed using standard PostgreSQL extension management commands (e.g., `CREATE EXTENSION duckdb;`). Once installed, the extension operates within the PostgreSQL server process, enabling users to execute DuckDB-specific SQL queries and leverage its analytical engine from within their PostgreSQL environment. The extension is managed and maintained as part of the Azure Database for PostgreSQL - Flexible Server platform, ensuring compatibility and support within the managed service.

**Use Cases and Application Scenarios:**  
- **Advanced Analytics:** Users can perform complex analytical queries and OLAP workloads directly within their PostgreSQL databases, reducing the need to export data to external analytical engines.
- **Data Science Workflows:** Data scientists and analysts can utilize DuckDB’s efficient columnar processing for rapid prototyping and data exploration within the Azure PostgreSQL environment.
- **ETL and Data Transformation:** The extension can be used for in-database transformations and aggregations, improving the performance of ETL pipelines by leveraging DuckDB’s optimized query execution.
- **Hybrid Workloads:** Applications requiring both transactional and analytical processing can benefit from the combined capabilities of PostgreSQL and DuckDB in a single managed environment.

**Important Considerations and Limitations:**  
- The update specifies that the DuckDB extension is now installable, but does not provide further details on version compatibility, feature set, or limitations; users should consult official documentation for operational constraints.
- As with any extension, users should validate compatibility with their PostgreSQL version and ensure that the extension meets their workload requirements.
- Resource consumption by the DuckDB extension may impact overall server performance; monitoring and tuning may be necessary for production workloads.

**Integration with Related Azure Services:**  
The DuckDB extension operates within Azure Database for PostgreSQL - Flexible Server, which is a managed database service integrated with other Azure services such as Azure Monitor, Azure Backup, and Azure Security Center. This allows users to leverage the analytical capabilities of DuckDB while benefiting from Azure’s managed service features, including automated backups, high availability, and security controls.

**Summary:**  
The DuckDB extension is now generally available for installation in Azure Database for PostgreSQL - Flexible Server, enabling enhanced analytical processing capabilities directly within managed PostgreSQL environments on Azure.

---

### 19. Public Preview: Advanced full-text search in Azure DocumentDB

**Published**: June 03, 2026 17:00:49 UTC
**Link**: [Public Preview: Advanced full-text search in Azure DocumentDB](https://azure.microsoft.com/updates?id=563077)

**Update ID**: 563077
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure DocumentDB, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure DocumentDB has introduced advanced full-text search features in public preview.

- Key changes or new features  
  - Fuzzy search: Enables matching on terms with minor misspellings or variations.  
  - Proximity search: Allows finding words within a specified distance from each other in documents.  
  - Expanded language support: Improves search accuracy across more languages.  
  - BM25 ranking: Implements a modern relevance ranking algorithm for more accurate search results.  
  - Unified search: Combines vector and advanced text search operations within a single database.

- Target audience affected  
Developers and IT professionals building search-driven applications on Azure DocumentDB, especially those requiring advanced text search, multi-language support, or integrating AI-driven search scenarios.

- Important notes if any  
These features are currently in public preview and may be subject to change. Developers can now consolidate search and data operations in DocumentDB, reducing the need for separate search engines. Review the documentation for API changes and compatibility considerations before adopting in production.

**Details**:

**Azure Update Report: Public Preview – Advanced Full-Text Search in Azure DocumentDB**

**Background and Purpose of the Update**  
This update introduces advanced full-text search capabilities to Azure DocumentDB, aiming to unify search operations within a single database environment. The enhancement addresses the growing need for sophisticated search features directly within DocumentDB, reducing the need for external search engines or complex integration layers.

**Specific Features and Detailed Changes**  
The update includes several key features:
- **Fuzzy Search:** Enables search queries to return results that match terms approximately, accommodating typographical errors or similar spellings.
- **Proximity Search:** Allows users to find documents where specified terms appear within a certain distance from each other, improving contextual relevance.
- **Expanded Language Support:** Increases the range of languages that DocumentDB’s full-text search can process, supporting more global and multilingual applications.
- **BM25 Ranking:** Implements the BM25 ranking algorithm, a state-of-the-art relevance scoring method, to improve the quality of search result ordering.
- **Integration of Vector and Advanced Text Search:** Combines vector-based search (for semantic similarity) with advanced text search operations, offering a unified approach to both structured and unstructured data retrieval.

**Technical Mechanisms and Implementation Methods**  
These features are natively integrated into Azure DocumentDB’s query engine. Fuzzy and proximity search are typically implemented through tokenization and edit-distance algorithms, while language support relies on language analyzers and stemming. BM25 ranking is applied during result scoring to prioritize documents based on term frequency and document length. The combination of vector and text search suggests that DocumentDB now supports hybrid search queries, enabling both semantic and lexical matching within the same database context.

**Use Cases and Application Scenarios**  
- **Content Management Systems:** Enhance user experience by providing typo-tolerant and context-aware search across large document repositories.
- **Multilingual Applications:** Support global user bases by enabling search in multiple languages without external processing.
- **Knowledge Bases and Support Portals:** Improve retrieval of relevant articles or documents using BM25 ranking and proximity search.
- **Semantic Search Applications:** Leverage vector search for intent-based queries alongside traditional keyword search.

**Important Considerations and Limitations**  
- This feature is currently in Public Preview, which may imply certain limitations in terms of SLA, support, or feature completeness.
- Users should evaluate the performance and accuracy of new search features in their specific workloads before deploying to production.
- Integration with existing DocumentDB indexes and queries may require schema or query modifications to fully leverage advanced search capabilities.

**Integration with Related Azure Services**  
- The enhanced search features are built into Azure DocumentDB, reducing the need for separate search services such as Azure Cognitive Search for many scenarios.
- Workloads that require both vector and text search can now consolidate data and queries within DocumentDB, simplifying architecture and reducing operational overhead.
- For advanced analytics or AI-driven applications, this update facilitates seamless integration with other Azure services that consume or enrich DocumentDB data.

**Summary**  
Azure DocumentDB now supports advanced full-text search features—including fuzzy and proximity search, expanded language support, BM25 ranking, and unified vector/text search—enabling more powerful, context-aware, and multilingual search operations within a single database environment.

---


*This report was automatically generated - 2026-06-04 03:09:00 UTC*