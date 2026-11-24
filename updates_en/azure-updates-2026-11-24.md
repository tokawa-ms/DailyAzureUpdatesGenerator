# November 24, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 24, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 18 items

## Update List

### 1. Public Preview: Enterprise Knowledge Graph in Foundry IQ

**Published**: November 23, 2026 21:16:32 UTC
**Link**: [Public Preview: Enterprise Knowledge Graph in Foundry IQ](https://azure.microsoft.com/updates?id=581333)

**Update ID**: 581333
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Enterprise Knowledge Graph is now available in Public Preview as a knowledge source within Foundry IQ.

- Key changes or new features  
Foundry IQ can now index unstructured content using a user-provided ontology to extract entities and relationships, forming an Enterprise Knowledge Graph. This enables agents to answer questions that require understanding complex relationships across organizational content. The update supports advanced semantic search and knowledge-driven applications by leveraging structured data extracted from unstructured sources.

- Target audience affected  
Developers building knowledge-driven applications, IT professionals managing enterprise content, and organizations seeking to enhance search and discovery capabilities in Foundry IQ.

- Important notes  
The Enterprise Knowledge Graph feature requires an ontology to guide entity and relationship extraction during indexing. This preview is ideal for scenarios where answers depend on interconnected data across various content types. Integration with Foundry IQ agents allows for improved contextual responses and richer knowledge experiences. Users should review documentation for ontology requirements and best practices for content indexing.

**Details**:

**Azure Update Report: Public Preview – Enterprise Knowledge Graph in Foundry IQ**

**Background and Purpose of the Update:**
The introduction of Enterprise Knowledge Graph as a knowledge source in Foundry IQ addresses the need for advanced semantic understanding across enterprise content. Many organizations possess vast amounts of unstructured data, making it challenging to extract meaningful relationships and entities for downstream applications such as search, analytics, and intelligent agents. This update aims to improve the quality and relevance of answers to questions that depend on complex relationships within enterprise content.

**Specific Features and Detailed Changes:**
- **Enterprise Knowledge Graph Integration:** Foundry IQ now supports Enterprise Knowledge Graph as a knowledge source, enabling it to answer questions that require understanding relationships across diverse content.
- **Ontology-Guided Indexing:** During the indexing phase, Foundry IQ leverages an ontology provided by the user to guide the extraction of entities and relationships from unstructured documents. This ensures that the knowledge graph is tailored to the organization’s domain and business logic.
- **Entity and Relationship Extraction:** The system automatically identifies relevant entities and their interconnections within the content, supporting richer semantic queries and reasoning.
- **Agent Support:** Agents within Foundry IQ can utilize the knowledge graph to deliver more accurate and contextually relevant answers, enhancing user experience and operational efficiency.

**Technical Mechanisms and Implementation Methods:**
- **Ontology-Driven Extraction:** The update relies on a user-supplied ontology to inform the extraction process. Ontologies define the types of entities and relationships that are important for the business, ensuring that the knowledge graph reflects organizational priorities.
- **Unstructured Content Processing:** Foundry IQ processes unstructured data (such as documents, emails, and reports) to extract entities and relationships, using advanced natural language processing (NLP) techniques.
- **Indexing Pipeline:** The extracted entities and relationships are indexed and stored in the Enterprise Knowledge Graph, making them available for semantic search and agent-driven queries.
- **Integration with Foundry IQ Agents:** Agents can query the knowledge graph to retrieve answers that depend on complex relationships, rather than simple keyword matching.

**Use Cases and Application Scenarios:**
- **Semantic Search:** Users can perform searches that leverage entity relationships, improving the relevance of results in scenarios such as legal discovery, research, and customer support.
- **Intelligent Agents:** Agents can answer questions that require understanding of business context, such as identifying connections between projects, personnel, or assets.
- **Data Analytics:** Analysts can explore relationships within enterprise data to uncover insights, trends, and anomalies.
- **Compliance and Risk Management:** Organizations can track relationships between entities to ensure compliance and manage risk across interconnected data.

**Important Considerations and Limitations:**
- **Ontology Requirement:** Effective use of this feature depends on the quality and completeness of the provided ontology. Organizations must invest in developing and maintaining ontologies that accurately reflect their domain.
- **Unstructured Data Quality:** The accuracy of entity and relationship extraction is influenced by the quality and consistency of unstructured content.
- **Preview Limitations:** As this feature is in public preview, it may not support all enterprise scenarios and could be subject to changes or enhancements before general availability.

**Integration with Related Azure Services:**
- **Foundry IQ Platform:** The Enterprise Knowledge Graph is integrated within Foundry IQ, leveraging its agent framework and indexing capabilities.
- **Azure Cognitive Services:** While not explicitly mentioned, NLP and entity extraction may utilize Azure Cognitive Services for processing unstructured data.
- **Azure Data Storage:** Extracted knowledge is likely stored in Azure-managed data stores, supporting scalability and security.

**Summary Sentence:**
Foundry IQ now offers Enterprise Knowledge Graph as a knowledge source in public preview, enabling ontology-guided extraction of entities and relationships from unstructured content to enhance agent-driven answers and semantic search across enterprise data.

---

### 2. Public Preview: Updated Guardrails experience in Microsoft Foundry

**Published**: November 23, 2026 21:15:04 UTC
**Link**: [Public Preview: Updated Guardrails experience in Microsoft Foundry](https://azure.microsoft.com/updates?id=581338)

**Update ID**: 581338
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry has released an updated Guardrails experience in public preview.

- Key changes or new features  
The new Guardrails experience enables developers to configure runtime safety controls for agents more easily. This includes support for classifiers, deterministic rules, and LLM-based judges. Guardrails now automatically surfaces required controls when an administrator policy mandates them for a project, streamlining compliance and safety configuration. The update improves integration and visibility of safety controls within Foundry projects.

- Target audience affected  
Developers building agent-based solutions in Microsoft Foundry, and IT professionals responsible for enforcing runtime safety policies.

- Important notes  
This update is currently in public preview. Organizations using Foundry should review their agent projects to ensure compliance with administrator policies and take advantage of the improved Guardrails configuration. Developers can leverage the enhanced controls to better manage agent safety and policy adherence.  
For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=581338).

**Details**:

**Azure Update Report: Public Preview – Updated Guardrails Experience in Microsoft Foundry**

**Background and Purpose of the Update**  
The updated Guardrails experience in Microsoft Foundry is designed to enhance the runtime safety controls available to developers working with agents. The purpose of this update is to provide a more robust and configurable mechanism for enforcing safety policies, particularly when administrator policies mandate specific controls for projects. This ensures that agent behavior remains compliant with organizational requirements and industry standards.

**Specific Features and Detailed Changes**  
The update introduces an improved Guardrails interface within Microsoft Foundry, focusing on the configuration of runtime safety controls. Key features include:

- **Support for Multiple Control Types:** Developers can now configure classifiers, deterministic rules, and LLM-based judges as part of the safety controls for agents.
- **Administrator Policy Integration:** When a project is subject to administrator-enforced policies, Guardrails automatically surfaces the required controls, streamlining compliance and reducing manual configuration.
- **Enhanced Developer Experience:** The updated experience provides clearer guidance and easier access to safety controls, making it more straightforward for developers to implement and manage runtime safeguards.

**Technical Mechanisms and Implementation Methods**  
Guardrails operates by integrating various safety control mechanisms directly into the agent runtime environment:

- **Classifiers:** These are machine learning models that evaluate agent outputs or actions, flagging or blocking content that violates predefined criteria.
- **Deterministic Rules:** These are explicit, rule-based checks that enforce specific behaviors or restrictions, ensuring predictable agent responses.
- **LLM-Based Judges:** Leveraging large language models, these judges assess agent actions in real-time, providing nuanced evaluations based on context and policy requirements.

When administrator policies are in place, Guardrails programmatically identifies and applies the necessary controls to the project, ensuring that all agent interactions adhere to organizational safety standards.

**Use Cases and Application Scenarios**  
This update is particularly relevant for:

- **Enterprise Projects:** Where strict compliance and safety requirements are enforced by administrators.
- **AI Agent Development:** Developers building agents that interact with sensitive data or perform critical operations can leverage Guardrails to mitigate risks.
- **Regulated Industries:** Organizations in healthcare, finance, or government sectors can use Guardrails to ensure agents operate within legal and ethical boundaries.

**Important Considerations and Limitations**  
- **Policy Enforcement:** The effectiveness of Guardrails depends on the accuracy and completeness of administrator policies.
- **Control Coverage:** While classifiers, deterministic rules, and LLM-based judges provide comprehensive coverage, gaps may exist if policies are not regularly updated.
- **Preview Status:** As this feature is in public preview, it may be subject to changes and may not be suitable for production environments without thorough testing.

**Integration with Related Azure Services**  
Guardrails is integrated within Microsoft Foundry, which is part of the broader Azure ecosystem. It can be used alongside other Azure services such as Azure Machine Learning for model training and evaluation, and Azure Policy for broader governance. The updated experience ensures seamless interoperability with these services, enabling consistent safety and compliance across Azure-based agent deployments.

**Summary Sentence**  
The updated Guardrails experience in Microsoft Foundry, now in public preview, streamlines the configuration and enforcement of runtime safety controls for agents, supporting classifiers, deterministic rules, and LLM-based judges, and automatically applying administrator-mandated policies to enhance compliance and developer productivity.

---

### 3. Public Preview: IQ Retriever Zero in Foundry IQ

**Published**: November 23, 2026 21:13:44 UTC
**Link**: [Public Preview: IQ Retriever Zero in Foundry IQ](https://azure.microsoft.com/updates?id=581343)

**Update ID**: 581343
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Public Preview of IQ Retriever Zero in Foundry IQ.

- Key changes or new features  
IQ Retriever Zero introduces an iterative retrieval model within Foundry IQ. This model breaks down complex questions into smaller, focused searches. It reviews initial search results and, if needed, performs additional searches within a configurable resource budget. The retrieved evidence is then passed to the answering model, improving the accuracy and relevance of responses.

- Target audience affected  
Developers and IT professionals working with Foundry IQ, especially those building solutions requiring advanced question answering and search capabilities.

- Important notes  
This feature is currently in Public Preview, meaning it may change before general availability. The iterative retrieval process can be configured to optimize performance and resource usage. Developers should review documentation for integration details and monitor for updates as the preview evolves. This enhancement can help improve the quality of automated responses in applications leveraging Foundry IQ’s search and answer capabilities.

**Details**:

**Azure Update Report: Public Preview – IQ Retriever Zero in Foundry IQ**

**Background and Purpose of the Update:**  
The introduction of IQ Retriever Zero in Foundry IQ addresses the need for enhanced retrieval capabilities when handling complex queries. Traditional retrieval models often struggle with multi-faceted questions, leading to incomplete or less relevant results. This update aims to improve the accuracy and relevance of answers by employing an iterative retrieval mechanism, enabling Foundry IQ to break down complex questions and conduct focused searches.

**Specific Features and Detailed Changes:**  
- **Iterative Retrieval Model:** Foundry IQ now uses an iterative approach, decomposing complex questions into smaller, more manageable sub-queries.  
- **Focused Searches:** Each sub-query triggers a targeted search, allowing the system to gather more precise evidence for each aspect of the original question.  
- **Review and Re-search:** The model reviews the results of each search and, if necessary, initiates additional searches to refine the evidence collected.  
- **Configurable Budget:** The iterative process is governed by a configurable budget, which likely refers to constraints such as the number of iterations, resource usage, or time limits, ensuring efficient operation and preventing excessive resource consumption.  
- **Evidence Passing:** The retrieved evidence is systematically passed to the answering model, which synthesizes the final response based on the accumulated data.

**Technical Mechanisms and Implementation Methods:**  
IQ Retriever Zero leverages an iterative retrieval loop within Foundry IQ. The process begins by parsing the initial complex question and generating sub-queries. Each sub-query is executed as a focused search against the available data sources. After each search, the results are evaluated for completeness and relevance. If gaps or ambiguities remain, the model can trigger additional searches within the defined budget. This iterative refinement continues until sufficient evidence is gathered or the budget is exhausted. The evidence is then handed off to the answering model, which constructs a comprehensive answer.

**Use Cases and Application Scenarios:**  
- **Enterprise Knowledge Management:** Organizations can use Foundry IQ to answer complex internal queries, such as policy compliance or multi-step operational procedures, by breaking down questions and retrieving targeted evidence.  
- **Technical Support Automation:** Automated support systems can leverage iterative retrieval to resolve intricate customer issues that require multi-layered evidence gathering.  
- **Research and Data Analysis:** Analysts can utilize Foundry IQ for research tasks that involve synthesizing information from multiple sources, ensuring thorough and accurate answers.

**Important Considerations and Limitations:**  
- **Configurable Budget Constraints:** The iterative retrieval process is limited by a configurable budget, which may impact the depth and breadth of evidence gathered. IT professionals should carefully set these parameters to balance performance and resource utilization.  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should monitor for updates and changes as the feature matures.  
- **Evidence Quality:** The effectiveness of the model depends on the quality and accessibility of underlying data sources.

**Integration with Related Azure Services:**  
Foundry IQ is part of the broader Azure ecosystem. IQ Retriever Zero can be integrated with Azure data storage solutions and knowledge bases, enhancing its ability to access and retrieve relevant information. IT professionals should ensure proper connectivity and permissions between Foundry IQ and Azure data repositories to maximize retrieval performance.

**Summary:**  
IQ Retriever Zero in Foundry IQ introduces an iterative retrieval model, enabling the system to break down complex questions into focused searches, review results, and refine evidence within a configurable budget, thereby enhancing answer accuracy and relevance in enterprise and research scenarios.

---

### 4. Public Preview: Style and instruction control for HD V3 voices in Azure Speech in Foundry Tools

**Published**: November 23, 2026 21:12:25 UTC
**Link**: [Public Preview: Style and instruction control for HD V3 voices in Azure Speech in Foundry Tools](https://azure.microsoft.com/updates?id=581353)

**Update ID**: 581353
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

**What was updated**  
Azure Speech in Foundry Tools now offers HD V3 voices with style and instruction control, available in public preview.

**Key changes or new features**  
- Developers can use new controls to modify the style and delivery of HD V3 voices, enabling more expressive and tailored speech output for applications.  
- Supported controls allow customization for voice agents, narration, and other speech-driven experiences, improving user engagement and interaction quality.  
- The update enhances flexibility in voice synthesis, making it easier to create natural and context-appropriate speech.

**Target audience affected**  
- Developers building conversational AI, voice agents, or narration features using Azure Speech services.  
- IT professionals managing Azure-based applications that require advanced speech synthesis capabilities.

**Important notes**  
- This feature is currently in public preview and may not be fully supported for production workloads.  
- For implementation details and supported styles/instructions, refer to the official documentation.  
- Feedback during the preview phase is encouraged to help shape the final release.

Learn more: [Azure Update link](https://azure.microsoft.com/updates?id=581353)

**Details**:

**Azure Update Report: Public Preview – Style and Instruction Control for HD V3 Voices in Azure Speech in Foundry Tools**

**Background and Purpose of the Update**  
This update introduces style and instruction control for HD V3 voices within Azure Speech in Foundry Tools, now available in public preview. The primary purpose is to enable developers and IT professionals to fine-tune the voice delivery of synthesized speech, enhancing the expressiveness and adaptability of voice agents, narration, and other speech-driven experiences. The update addresses the need for more natural and contextually appropriate voice outputs in enterprise applications.

**Specific Features and Detailed Changes**  
- **HD V3 Voices:** The update focuses on HD V3 voices, which are high-definition, neural text-to-speech models designed for improved clarity and realism.
- **Style Control:** Users can modify the speaking style of HD V3 voices, allowing for adjustments such as conversational, formal, cheerful, or other supported styles. This enables the voice output to match the intended emotional tone or context.
- **Instruction Control:** Developers can provide specific instructions to further shape the voice delivery, such as emphasizing certain phrases, adjusting pacing, or controlling prosody. Supported controls are accessible within Foundry Tools, offering granular customization for speech synthesis.

**Technical Mechanisms and Implementation Methods**  
- **Foundry Tools Integration:** The new controls are implemented within Foundry Tools, which serve as a platform for configuring and deploying Azure Speech services. The controls are likely exposed via APIs or UI elements, enabling developers to select styles and provide instructions programmatically or through configuration interfaces.
- **Speech Synthesis Pipeline:** When generating speech, the HD V3 engine processes the provided style and instruction parameters, dynamically adjusting the neural model’s output to reflect the desired characteristics. This mechanism leverages Azure’s underlying neural TTS technology for real-time adaptation.

**Use Cases and Application Scenarios**  
- **Voice Agents:** Enhance customer service bots or virtual assistants by tailoring their speech style to suit different interaction contexts (e.g., friendly for onboarding, formal for business inquiries).
- **Narration:** Improve audiobook or video narration by adjusting the style for dramatic, informative, or engaging delivery, ensuring the voice matches the content’s mood.
- **Accessibility Tools:** Provide more expressive and context-aware speech for screen readers or assistive technologies, improving user experience for individuals with disabilities.
- **Interactive Applications:** Use instruction control to emphasize important information, adjust pacing for tutorials, or create more immersive gaming experiences.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, indicating it may not be fully production-ready and could be subject to changes or limitations in supported styles and instructions.
- **Supported Controls:** Only certain styles and instructions are supported; developers should consult documentation for the exact list and syntax.
- **Performance and Compatibility:** As this feature is integrated within Foundry Tools, compatibility with existing workflows and APIs should be evaluated. There may be constraints on voice selection or control granularity depending on the HD V3 model.

**Integration with Related Azure Services**  
- **Azure Speech Service:** The update builds on Azure’s core Speech service, leveraging its neural TTS capabilities.
- **Foundry Tools:** Acts as the configuration and deployment hub for these new controls, facilitating integration with broader Azure solutions such as conversational AI, cognitive services, and custom app development.

**Summary Sentence**  
Azure Speech in Foundry Tools now offers public preview support for style and instruction control with HD V3 voices, enabling developers to customize voice delivery for enhanced speech experiences in various applications.

---

### 5. Public Preview: Human annotation for agent evaluations in Microsoft Foundry

**Published**: November 23, 2026 21:11:23 UTC
**Link**: [Public Preview: Human annotation for agent evaluations in Microsoft Foundry](https://azure.microsoft.com/updates?id=581358)

**Update ID**: 581358
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

**What was updated:**  
Microsoft Foundry now offers human annotation capabilities for agent evaluations, available in public preview.

**Key changes or new features:**  
- Reviewers can annotate agent conversation traces with ratings, tags, comments, and expected outputs.
- Annotated traces can be used to build evaluation datasets for agent performance analysis and improvement.
- This feature supports more granular and qualitative assessment of conversational agents, complementing automated evaluation methods.

**Target audience affected:**  
- Developers building conversational agents or AI-powered bots using Microsoft Foundry.
- IT professionals managing or evaluating agent performance in enterprise environments.

**Important notes:**  
- Human annotation enables richer feedback and more accurate evaluation of agent responses, which is crucial for iterative model improvement.
- The feature is currently in public preview, so it may evolve based on user feedback and is not recommended for production-critical workflows yet.
- Integration with Microsoft IQ is highlighted, suggesting alignment with broader AI evaluation and monitoring capabilities.

For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=581358).

**Details**:

**Azure Update Report: Public Preview – Human Annotation for Agent Evaluations in Microsoft Foundry**

**Background and Purpose of the Update**  
This update introduces the public preview of human annotation capabilities for agent evaluations within Microsoft Foundry, as announced in the Microsoft IQ launch blog. The purpose is to enhance the evaluation process of conversational agents by enabling human reviewers to directly annotate agent traces. This allows for more nuanced and qualitative assessment of agent performance, supplementing automated evaluation methods.

**Specific Features and Detailed Changes**  
The new annotation functionality provides reviewers with the ability to:
- Add ratings to agent traces, quantifying the agent’s performance.
- Attach tags for categorization or identification of specific behaviors or issues.
- Insert comments to provide qualitative feedback or context.
- Specify expected outputs, clarifying what the agent should have produced in a given scenario.

These features collectively enable a richer dataset for agent evaluation, facilitating both manual and automated analysis.

**Technical Mechanisms and Implementation Methods**  
Human annotation is implemented within Microsoft Foundry’s agent evaluation workflow. Reviewers interact with conversation traces—records of agent interactions—and annotate them using the provided interface. The annotated traces are stored and can be utilized for building evaluation datasets (“evals”). These datasets can then be used to benchmark agent performance, train models, or refine agent logic based on human feedback.

The annotation process is integrated into Foundry’s trace management system, ensuring that all metadata (ratings, tags, comments, expected outputs) are associated with the correct conversation trace and are accessible for downstream processing.

**Use Cases and Application Scenarios**  
- **Agent Quality Assurance:** Human reviewers can systematically evaluate agent responses in production or testing environments, identifying areas for improvement.
- **Model Training and Fine-Tuning:** Annotated traces serve as labeled data for supervised learning, enabling more targeted training of conversational models.
- **Performance Benchmarking:** Organizations can use human-annotated evals to compare agent versions or configurations, supporting iterative development and deployment.
- **Compliance and Audit:** Annotations provide an audit trail of agent behavior and reviewer assessments, useful for regulatory compliance or internal governance.

**Important Considerations and Limitations**  
- The feature is currently in public preview, which may imply limited support and potential changes before general availability.
- Annotation quality depends on reviewer expertise and consistency; organizations should establish guidelines for annotation to ensure reliability.
- There may be constraints on the volume of traces that can be annotated or stored, depending on Foundry’s current preview limitations.
- Integration with automated evaluation pipelines may require additional configuration to leverage human-annotated data.

**Integration with Related Azure Services**  
Human annotation for agent evaluations is part of Microsoft Foundry, which is integrated with Azure’s broader AI and agent development ecosystem. Annotated traces can be used in conjunction with Azure Machine Learning for model training, Azure Cognitive Services for conversational AI, and Azure DevOps for workflow automation. The update enhances the interoperability of Foundry with these services by providing high-quality, human-labeled evaluation data.

**Summary Sentence**  
Human annotation for agent evaluations in Microsoft Foundry, now in public preview, enables reviewers to enrich agent traces with ratings, tags, comments, and expected outputs, supporting improved evaluation, training, and benchmarking of conversational agents within Azure’s AI ecosystem.

---

### 6. Generally Available: Agent insights in Microsoft Foundry

**Published**: November 23, 2026 21:10:07 UTC
**Link**: [Generally Available: Agent insights in Microsoft Foundry](https://azure.microsoft.com/updates?id=581363)

**Update ID**: 581363
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Agent insights in Microsoft Foundry are now generally available.

- Key changes or new features  
Agent insights analyze agent traces to identify recurring patterns and group related issues. Users can review insights and supporting trace data to investigate common failures and prioritize improvements. The agent optimizer feature allows testing of potential fixes directly within Foundry, streamlining the troubleshooting and optimization process.

- Target audience affected  
Developers and IT professionals working with Microsoft Foundry, especially those responsible for monitoring, debugging, and optimizing agent-based applications.

- Important notes if any  
This update enhances visibility into agent behavior, helping teams quickly pinpoint and address frequent failures. The integration of agent optimizer supports iterative testing and improvement, reducing manual effort and accelerating resolution times. Reviewing insights and traces can help prioritize which issues to fix first, improving overall application reliability and performance. No additional configuration is required to access these features if you are already using Microsoft Foundry.

**Details**:

**Comprehensive Technical Explanation: Agent Insights in Microsoft Foundry (Generally Available)**

**Background and Purpose of the Update**  
This update announces the general availability of Agent Insights within Microsoft Foundry. The primary objective is to enhance observability and operational intelligence for users managing agents in Foundry by providing automated analysis of agent traces. This capability is designed to help IT professionals quickly identify, group, and prioritize recurring issues, thereby streamlining the troubleshooting and optimization process.

**Specific Features and Detailed Changes**  
- **Automated Trace Analysis:** Agent Insights now analyzes agent traces to detect and surface recurring patterns. This automated grouping of related issues enables users to efficiently review clusters of similar failures.
- **Insight Review:** Users can review each surfaced insight along with its supporting traces. This provides context and evidence for each identified issue, facilitating deeper investigation.
- **Prioritization of Improvements:** By highlighting common failures, the feature assists teams in deciding which issues to address first, optimizing resource allocation and remediation efforts.
- **Agent Optimizer Integration:** The update introduces the ability to use the agent optimizer tool to test potential fixes. This allows for rapid validation of remediation strategies directly within the Foundry environment.

**Technical Mechanisms and Implementation Methods**  
- **Trace Collection:** Agent traces are collected during agent operation within Microsoft Foundry.
- **Pattern Analysis:** These traces are processed by an insights engine that applies analytical algorithms to identify recurring patterns and group related issues.
- **Insight Generation:** The system generates actionable insights, each linked to a set of supporting traces, which can be reviewed in the Foundry interface.
- **Optimizer Workflow:** The agent optimizer provides a mechanism to apply and test fixes, likely leveraging the same trace data to validate improvements.

**Use Cases and Application Scenarios**  
- **Incident Response:** Operations teams can use Agent Insights to quickly pinpoint the root causes of frequent agent failures, reducing mean time to resolution (MTTR).
- **Continuous Improvement:** Development teams can leverage grouped insights to prioritize bug fixes and enhancements based on the frequency and impact of observed issues.
- **Change Validation:** After deploying a fix, teams can use the agent optimizer to test its effectiveness against historical trace data, ensuring issues are resolved before full rollout.

**Important Considerations and Limitations**  
- **Data Scope:** Insights are only as comprehensive as the trace data collected; ensure agents are properly instrumented and traces are complete.
- **Insight Accuracy:** The effectiveness of pattern recognition depends on the quality and volume of trace data; rare or unique issues may not be grouped or surfaced.
- **Operational Overhead:** While automated, reviewing and acting on insights still requires human oversight to validate findings and implement fixes.

**Integration with Related Azure Services**  
- **Microsoft Foundry Ecosystem:** Agent Insights is natively integrated within Microsoft Foundry, leveraging its trace collection and agent management capabilities.
- **Agent Optimizer:** Direct integration with the agent optimizer streamlines the workflow from issue detection to fix validation.
- **Potential for Broader Azure Integration:** While not explicitly stated, insights generated could be used alongside other Azure monitoring and diagnostic tools for comprehensive operational management.

**Summary Sentence**  
Agent Insights in Microsoft Foundry is now generally available, providing automated analysis of agent traces to surface recurring patterns, group related issues, and support rapid investigation and optimization through integrated insight review and agent optimizer workflows.

---

### 7. Generally Available: Files knowledge source for Foundry IQ

**Published**: November 23, 2026 21:08:46 UTC
**Link**: [Generally Available: Files knowledge source for Foundry IQ](https://azure.microsoft.com/updates?id=581368)

**Update ID**: 581368
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
The Files knowledge source feature in Foundry IQ is now generally available.

- Key changes or new features  
Developers and IT professionals can now upload files directly to a managed knowledge source within Foundry IQ. The platform automatically processes and indexes these files, making them accessible through a knowledge base. There is no need to manually provision an Azure Storage account or configure a scheduled indexer, simplifying setup and maintenance.

- Target audience affected  
This update is relevant for developers and IT professionals building applications or solutions with Foundry IQ, especially those who need to integrate document-based knowledge sources for retrieval and search.

- Important notes  
The new feature streamlines file ingestion and indexing workflows, reducing infrastructure overhead and operational complexity. Users should review documentation for supported file types and best practices for knowledge base integration.  
Learn more: [Azure Update link](https://azure.microsoft.com/updates?id=581368)

**Details**:

**Azure Update Report: Generally Available - Files Knowledge Source for Foundry IQ**

**Background and Purpose of the Update:**  
This update introduces the general availability of a files knowledge source for Foundry IQ, a service designed to facilitate knowledge management and retrieval. The purpose is to streamline the ingestion and indexing of files as knowledge sources, eliminating the need for external storage provisioning or manual indexing workflows. This enhancement aims to simplify the process of building and maintaining a knowledge base within Foundry IQ.

**Specific Features and Detailed Changes:**  
With this update, users can now upload files directly to a managed knowledge source within Foundry IQ. The service automatically processes and indexes these files, making their contents retrievable through the Foundry IQ knowledge base. Previously, users may have needed to provision an Azure Storage account and configure scheduled indexers to enable document ingestion and indexing. The new feature removes these requirements, providing a more integrated and automated experience for file-based knowledge management.

**Technical Mechanisms and Implementation Methods:**  
The files knowledge source is managed natively within Foundry IQ. When a file is uploaded, Foundry IQ handles the storage, processing, and indexing internally. The indexing process extracts relevant metadata and content from the files, enabling efficient retrieval and search within the knowledge base. This is achieved without the need for external storage accounts or custom indexing schedules, as Foundry IQ abstracts these operations and provides a managed backend for file ingestion and indexing.

**Use Cases and Application Scenarios:**  
- Organizations seeking to centralize document-based knowledge (such as manuals, policies, or technical guides) can leverage this feature to upload files directly into Foundry IQ for immediate indexing and retrieval.
- IT teams building knowledge bases for internal support or customer-facing solutions can use the managed files knowledge source to reduce operational overhead and accelerate deployment.
- Scenarios where rapid onboarding of new knowledge sources is required, such as project documentation or compliance materials, benefit from the simplified upload and indexing workflow.

**Important Considerations and Limitations:**  
- The update removes the need for provisioning Azure Storage accounts and scheduled indexers, but users should ensure that files uploaded comply with Foundry IQ’s supported formats and size limitations.
- Since the storage and indexing are managed by Foundry IQ, users may have limited control over underlying storage configurations or indexing parameters compared to custom solutions.
- Security and access controls are governed by Foundry IQ’s managed environment; users should review documentation to understand how permissions and data privacy are handled.

**Integration with Related Azure Services:**  
This update enhances Foundry IQ’s native capabilities and reduces dependency on external Azure services such as Azure Storage and Azure Cognitive Search indexers for file-based knowledge ingestion. The managed files knowledge source is tightly integrated within Foundry IQ, providing a seamless experience for knowledge base creation and retrieval. Users can focus on content management and retrieval without managing auxiliary Azure resources.

**Summary Sentence:**  
The general availability of the files knowledge source in Foundry IQ enables direct file uploads to a managed knowledge base, with automated processing and indexing, streamlining knowledge management by removing the need for external storage accounts and scheduled indexers.

---

### 8. Public Preview: Call model router without a deployment in Microsoft Foundry

**Published**: November 23, 2026 20:32:57 UTC
**Link**: [Public Preview: Call model router without a deployment in Microsoft Foundry](https://azure.microsoft.com/updates?id=581378)

**Update ID**: 581378
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

**What was updated**  
Microsoft Foundry now supports using the model router without requiring a prior deployment. This feature is available in regions where the model router is supported.

**Key changes or new features**  
- Developers can set the model parameter to "auto" in Responses or Chat Completions API requests to Foundry resources.
- The "auto" setting enables Balanced routing mode by default, automatically selecting the best available model for the request.
- No need to manually deploy or configure the model router before use, simplifying integration and reducing setup time.

**Target audience affected**  
- Developers building AI applications with Microsoft Foundry.
- IT professionals managing Foundry resources and API integrations.

**Important notes**  
- This feature is currently in public preview and may be subject to changes.
- Ensure your Foundry resource is in a region that supports the model router.
- Using "auto" routing can optimize performance and reduce operational overhead, but review documentation for region-specific support and limitations.

[Read more](https://azure.microsoft.com/updates?id=581378)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Call model router without a deployment in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581378)

---

**Background and Purpose of the Update:**  
Previously, Microsoft Foundry required IT professionals to deploy the model router component before it could be utilized for routing AI model requests. This deployment step added operational overhead and complexity, especially when quickly prototyping or scaling AI solutions. The update introduces the ability to call the model router directly, without prior deployment, streamlining access and reducing setup time for Foundry users.

---

**Specific Features and Detailed Changes:**  
- **Direct Invocation:** Users can now invoke the model router in Microsoft Foundry without deploying it as a separate resource.
- **Auto Model Selection:** When submitting a Responses or Chat Completions request to a Foundry resource in a supported region, setting the `model` parameter to `auto` enables automatic routing.
- **Balanced Routing Mode:** By default, the `auto` setting utilizes the Balanced routing mode, which distributes requests across available models to optimize performance and reliability.

---

**Technical Mechanisms and Implementation Methods:**  
- **Request Configuration:** In supported regions, IT professionals can configure their API requests to Foundry by specifying `model: auto` in either Responses or Chat Completions endpoints.
- **Routing Logic:** The model router, operating in Balanced mode, dynamically selects the most appropriate model for each request based on internal criteria (such as load balancing and model availability).
- **No Deployment Required:** The router is managed as a platform service, eliminating the need for manual deployment or resource management. This is handled transparently by Microsoft Foundry.

---

**Use Cases and Application Scenarios:**  
- **Rapid Prototyping:** Developers can quickly test and iterate on AI-powered applications without the delay of deploying routing infrastructure.
- **Dynamic Model Selection:** Applications requiring flexible model selection benefit from the auto routing feature, which adapts to available models and optimizes response handling.
- **Simplified Operations:** Organizations can reduce operational complexity and maintenance by relying on Foundry’s managed routing service.

---

**Important Considerations and Limitations:**  
- **Regional Availability:** The feature is only available in regions that support model router functionality. IT professionals must verify regional support before implementation.
- **Default Routing Mode:** The routing mode is set to Balanced by default when using `auto`. Custom routing modes or advanced configurations may not be available in this preview.
- **Preview Status:** As a public preview, the feature may have limitations in terms of stability, performance, or feature completeness. Production use should be evaluated accordingly.

---

**Integration with Related Azure Services:**  
- **Microsoft Foundry:** The update is native to Foundry resources, allowing seamless integration with existing Foundry-based AI workflows.
- **Azure AI Services:** The model router can be used in conjunction with Azure’s AI APIs, such as Responses and Chat Completions, to enhance model selection and routing efficiency.
- **Resource Management:** The elimination of deployment requirements aligns with Azure’s managed service philosophy, reducing administrative overhead and facilitating integration with other Azure platform services.

---

**Summary Sentence:**  
Microsoft Foundry now allows IT professionals to call the model router directly without deployment, enabling automatic and balanced model selection in supported regions by simply setting the model parameter to auto in Responses or Chat Completions requests.

---

### 9. Public Preview: Use the Messages API with model router in Microsoft Foundry

**Published**: November 23, 2026 20:31:40 UTC
**Link**: [Public Preview: Use the Messages API with model router in Microsoft Foundry](https://azure.microsoft.com/updates?id=581383)

**Update ID**: 581383
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
The model router in Microsoft Foundry now supports the Messages API in public preview.

- Key changes or new features  
Developers can use the Messages API with the model router to enable automatic selection of AI models for messages-based applications and coding tools. The integration maintains compatibility with the Anthropic request and response format. Messages requests are routed only to supported models, ensuring proper handling and format consistency.

- Target audience affected  
This update is relevant for developers building messages-based applications, coding tools, and those integrating AI models via Microsoft Foundry. IT professionals managing AI infrastructure or APIs in Foundry environments will also benefit.

- Important notes  
The Messages API support is currently in public preview, so it may not be suitable for production workloads. Only models that support the Messages API will receive routed requests. Developers should verify model compatibility and monitor for future updates as the feature matures.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Use the Messages API with model router in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581383)

---

**Background and Purpose of the Update**

The update introduces public preview support for the Messages API within the model router component of Microsoft Foundry. The goal is to enable messages-based applications and coding tools to leverage automatic model selection while maintaining compatibility with the Anthropic request and response format. This enhancement is designed to streamline integration for developers building conversational AI solutions, allowing them to utilize multiple models efficiently through a unified API interface.

---

**Specific Features and Detailed Changes**

- **Messages API Support:** The model router now accepts and processes requests formatted according to the Messages API, which is commonly used for conversational AI and chat-based applications.
- **Automatic Model Selection:** Applications can send messages-based requests, and the model router will automatically select the most appropriate supported model for processing, abstracting away manual model management.
- **Anthropic Format Compatibility:** The update ensures that both requests and responses adhere to the Anthropic format, facilitating seamless integration for tools and applications already using this structure.
- **Routing Scope:** Messages requests are routed exclusively to models that are supported by the router, ensuring compatibility and reliability.

---

**Technical Mechanisms and Implementation Methods**

- **Model Router Functionality:** The model router acts as an intermediary, receiving Messages API requests and determining which underlying model to invoke based on request parameters and available models.
- **API Handling:** Incoming requests must conform to the Anthropic request format, and responses are returned in the same format, ensuring consistency for developers.
- **Routing Logic:** The router’s automatic model selection is based on internal criteria, which may include request content, model capabilities, and availability. Only models compatible with the Messages API and Anthropic format are considered for routing.
- **Public Preview Status:** The feature is currently in public preview, indicating that it is available for testing and feedback but may not be fully production-ready.

---

**Use Cases and Application Scenarios**

- **Conversational AI Applications:** Developers building chatbots, virtual assistants, or customer support tools can utilize the Messages API with the model router to simplify model management and improve response quality.
- **Coding Tools:** IDE plugins or code generation tools that rely on conversational interfaces can benefit from automatic model selection, reducing integration complexity.
- **Multi-Model Environments:** Organizations deploying multiple AI models can centralize their messaging workflows, allowing the router to handle model selection and routing transparently.

---

**Important Considerations and Limitations**

- **Supported Models Only:** Routing is limited to models that are supported by the router and compatible with the Messages API and Anthropic format. Unsupported models will not be invoked.
- **Preview Limitations:** As the feature is in public preview, it may be subject to changes, limited support, and potential instability. Production use should be approached with caution.
- **Format Requirements:** Both requests and responses must strictly adhere to the Anthropic format, which may require adjustments for applications using different formats.

---

**Integration with Related Azure Services**

- **Microsoft Foundry Integration:** The update is specific to Microsoft Foundry’s model router, allowing applications already using Foundry to adopt the Messages API seamlessly.
- **Azure AI Ecosystem:** While the update focuses on Foundry, it may complement other Azure AI services by enabling easier routing and model selection for conversational workloads, provided those services support the Anthropic format.

---

**Summary Sentence**

The public preview of Messages API support in Microsoft Foundry’s model router enables messages-based applications to leverage automatic model selection with Anthropic format compatibility, streamlining conversational AI integration and routing to supported models.

---

### 10. Public Preview: Use your model deployments with model router in Microsoft Foundry

**Published**: November 23, 2026 20:29:36 UTC
**Link**: [Public Preview: Use your model deployments with model router in Microsoft Foundry](https://azure.microsoft.com/updates?id=581388)

**Update ID**: 581388
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Microsoft Foundry's model router now supports using your existing model deployments to serve routed requests, available in public preview.

- Key changes or new features  
The model router can leverage models you have already deployed, allowing you to utilize existing compute capacity. When a request is received, the router selects the most appropriate model from your deployments and forwards the request accordingly. This enables dynamic routing and efficient use of resources without requiring new model deployments specifically for routing scenarios.

- Target audience affected  
Developers and IT professionals working with Microsoft Foundry, especially those managing multiple model deployments or building applications that require intelligent model selection and routing.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. It helps optimize resource utilization and simplifies integration with existing models. Users should monitor performance and compatibility as the feature evolves. For more details, visit the official Azure Update page: https://azure.microsoft.com/updates?id=581388

**Details**:

**Azure Update Report**

**Title:** Public Preview: Use your model deployments with model router in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581388)

---

**Background and Purpose of the Update**  
Microsoft Foundry introduces a public preview feature allowing users to leverage their existing model deployments with the model router. The primary goal is to optimize resource utilization by enabling routed requests to be served by models already deployed, rather than requiring new deployments. This update addresses the need for flexible, efficient model serving in environments where multiple models are available and capacity management is critical.

**Specific Features and Detailed Changes**  
- **Model Router Integration:** The model router can now utilize any existing model deployment within Microsoft Foundry to serve incoming requests.
- **Routed Request Handling:** When a request is received, the model router dynamically selects an appropriate model from the available deployments to process the request.
- **Capacity Utilization:** This feature ensures that the capacity of existing model deployments is used efficiently, reducing redundant resource allocation and improving operational cost-effectiveness.

**Technical Mechanisms and Implementation Methods**  
- **Routing Logic:** The model router employs selection logic to determine which deployed model should handle each request. The selection criteria are not specified in the update, but the router acts as an intermediary, abstracting the routing process from the client application.
- **Deployment Reference:** Users do not need to redeploy models; the router references existing deployments directly, streamlining integration and minimizing setup overhead.
- **Request Forwarding:** After selecting a model, the router forwards the request to the chosen deployment, ensuring seamless communication between the client and the model endpoint.

**Use Cases and Application Scenarios**  
- **Multi-Model Environments:** Organizations with several models deployed (e.g., for A/B testing, versioning, or specialized tasks) can use the model router to dynamically allocate requests based on availability or other criteria.
- **Resource Optimization:** Enterprises seeking to maximize their existing compute and model deployment resources benefit from this feature by reducing idle capacity and avoiding unnecessary redeployments.
- **Scalable AI Solutions:** Developers building scalable AI services can leverage the model router to manage request distribution across multiple models, supporting high-availability and load balancing scenarios.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, indicating that it may not be fully production-ready and could be subject to changes or limitations in functionality.
- **Model Selection Details:** The update does not specify the selection algorithm or criteria used by the model router, so users should validate routing behavior in their environment.
- **Compatibility:** Only existing model deployments within Microsoft Foundry are supported; external models or deployments outside Foundry are not referenced.

**Integration with Related Azure Services**  
- **Microsoft Foundry:** The model router is a component within Microsoft Foundry, leveraging its deployment infrastructure.
- **Azure Machine Learning:** While not explicitly mentioned, the model router’s approach aligns with Azure Machine Learning’s deployment and routing paradigms, potentially facilitating integration with ML workflows and pipelines.
- **Monitoring and Management:** Users can continue to use Foundry’s monitoring and management tools to oversee model deployments and routed request performance.

---

**Summary Sentence:**  
The public preview of model router in Microsoft Foundry enables users to efficiently serve routed requests using their existing model deployments, optimizing capacity and simplifying model selection and request handling within AI solutions.

---

### 11. Generally Available: Model router now supports the Responses API protocol in Microsoft Foundry

**Published**: November 23, 2026 20:28:24 UTC
**Link**: [Generally Available: Model router now supports the Responses API protocol in Microsoft Foundry](https://azure.microsoft.com/updates?id=581393)

**Update ID**: 581393
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
The Model Router in Microsoft Foundry is now generally available with support for the Responses API protocol on both resource and project endpoints.

- Key changes or new features  
Model Router can now handle the Responses API protocol, enabling automatic model selection for applications using Responses-based APIs. Developers can set the model parameter to their model router deployment name, streamlining integration and routing for multiple models. This update applies to both resource and project endpoints, offering flexibility in deployment and usage.

- Target audience affected  
Developers building AI applications with Microsoft Foundry, and IT professionals managing model deployments and API integrations.

- Important notes if any  
To leverage automatic model selection in Responses-based applications, ensure you set the model parameter to your model router deployment name. This enhancement simplifies model management and routing, reducing manual configuration and improving scalability for AI workloads. For further details, refer to the official Azure update documentation.

**Details**:

**Azure Update Report**

**Title:** Generally Available: Model router now supports the Responses API protocol in Microsoft Foundry  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=581393)

---

**Background and Purpose of the Update**  
Microsoft Foundry’s model router is a core component for managing and orchestrating AI model deployments. The update addresses the need for seamless integration between model routing and application-level APIs, specifically the Responses API protocol. By enabling support for the Responses API protocol, Microsoft Foundry aims to simplify the development and deployment of AI-powered applications, ensuring consistent and automatic model selection for applications that rely on the Responses API.

---

**Specific Features and Detailed Changes**  
- **General Availability:** The Responses API protocol support is now generally available for the model router, meaning it is production-ready and supported for all users.
- **Endpoint Coverage:** Support is provided on both resource and project endpoints, allowing flexibility in how applications interact with the model router.
- **Automatic Model Selection:** By setting the model parameter to the model router deployment name, developers can enable automatic model selection for Responses-based applications. This reduces manual configuration and streamlines the integration process.

---

**Technical Mechanisms and Implementation Methods**  
- **Responses API Protocol Support:** The model router now interprets and responds to requests using the Responses API protocol, which standardizes how applications communicate with AI models and receive responses.
- **Deployment Name Parameterization:** Applications specify the model router deployment name in their API calls. The router then automatically selects the appropriate model based on the deployment configuration, ensuring that applications always interact with the optimal model version.
- **Resource and Project Endpoints:** The model router exposes both resource-level and project-level endpoints, allowing for granular control over model selection and routing based on organizational or project-specific requirements.

---

**Use Cases and Application Scenarios**  
- **AI Application Development:** Developers building applications that use the Responses API protocol can now leverage the model router for automatic model selection, reducing operational overhead.
- **Multi-Model Management:** Organizations managing multiple AI models across projects can use the model router to route requests dynamically, ensuring that each application receives responses from the most appropriate model.
- **Streamlined Deployment:** The update simplifies the process of deploying and updating AI models within Microsoft Foundry, as applications no longer need to be manually reconfigured when models are updated or replaced.

---

**Important Considerations and Limitations**  
- **Deployment Naming:** Correct configuration of the model router deployment name is essential for automatic model selection. Misconfiguration may result in incorrect model routing.
- **Protocol Compatibility:** Applications must be designed to use the Responses API protocol to benefit from this update. Other protocols are not covered by this enhancement.
- **Endpoint Selection:** Developers should choose between resource and project endpoints based on their organizational structure and access control requirements.

---

**Integration with Related Azure Services**  
- **Microsoft Foundry:** The update is native to Microsoft Foundry, enhancing its AI model orchestration capabilities.
- **Azure AI Services:** Applications leveraging Azure AI services can now integrate more seamlessly with Foundry’s model router, provided they use the Responses API protocol.
- **Resource and Project Management:** The model router’s support for both resource and project endpoints allows integration with Azure’s resource management and project tracking features.

---

**Summary Sentence:**  
The model router in Microsoft Foundry is now generally available with support for the Responses API protocol, enabling automatic model selection for Responses-based applications via both resource and project endpoints, thereby streamlining AI model integration and management for developers and organizations.

---

### 12. Public Preview: Use model router with AI Gateway

**Published**: November 23, 2026 20:15:53 UTC
**Link**: [Public Preview: Use model router with AI Gateway](https://azure.microsoft.com/updates?id=581398)

**Update ID**: 581398
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure AI Gateway now supports automatic model selection via the model router from Microsoft Foundry in public preview.

- Key changes or new features  
The AI Gateway uses the model router to dynamically rank and select backend models associated with a model alias for each API request. This ranking is combined with the alias’s configured priorities and weights, enabling intelligent routing to the optimal model backend. The gateway continues to enforce access controls and usage quotas as usual.

- Target audience affected  
Developers integrating AI models via Azure AI Gateway, and IT professionals managing AI infrastructure and APIs.

- Important notes  
This update streamlines model selection for multi-model deployments, reducing manual configuration and improving performance and reliability. Developers can leverage automatic routing to optimize inference requests without changing client code. IT professionals should review access controls and quotas to ensure compliance as routing logic becomes more dynamic. The feature is currently in public preview; production use should be evaluated accordingly.

**Details**:

**Background and Purpose of the Update**  
This update introduces the public preview of automatic model selection in AI Gateway, leveraging the model router from Microsoft Foundry. The primary goal is to optimize AI model management by automating the selection process for backend models associated with a model alias. This enhancement aims to streamline model deployment, improve request routing efficiency, and maximize the effectiveness of AI workloads by dynamically choosing the most suitable model for each request.

**Specific Features and Detailed Changes**  
- **Model Router Integration:** AI Gateway now incorporates the model router from Microsoft Foundry. This component automatically ranks the available models behind a given model alias for each incoming request.
- **Dynamic Model Selection:** The gateway uses the model router’s ranking in conjunction with the alias’s configured priorities and weights to determine the optimal backend model for each request.
- **Enhanced Routing Logic:** The update refines the backend selection process, moving from static or manual routing to a more intelligent, automated approach.

**Technical Mechanisms and Implementation Methods**  
- **Model Alias Configuration:** Users can define a model alias that represents multiple backend models. Each backend can be assigned specific priorities and weights, influencing selection probability.
- **Request Handling:** Upon receiving a request, the AI Gateway invokes the model router, which evaluates and ranks the candidate models based on criteria managed by Microsoft Foundry.
- **Combined Decision Logic:** The gateway synthesizes the model router’s ranking with the user-defined priorities and weights to select the backend model that will process the request.
- **Access Control:** The gateway maintains its access control mechanisms throughout the selection and routing process, ensuring that only authorized requests are processed.

**Use Cases and Application Scenarios**  
- **A/B Testing of AI Models:** Organizations can deploy multiple versions of a model behind a single alias and use the model router to automatically direct traffic, facilitating comparative performance analysis.
- **Model Version Management:** Teams can seamlessly introduce new model versions or rollback to previous ones without manual routing changes, improving operational agility.
- **Load Balancing and Optimization:** The system can dynamically distribute requests to the most appropriate model, optimizing resource usage and model performance.

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to change.
- **Access Control Continuity:** The gateway’s access control remains in effect, but users should verify compatibility with their security and compliance requirements.
- **Dependency on Microsoft Foundry:** The model router functionality is tied to Microsoft Foundry, and users must ensure proper integration and configuration.

**Integration with Related Azure Services**  
- **AI Gateway:** This update directly enhances the AI Gateway service, improving its model management and routing capabilities.
- **Microsoft Foundry:** The model router is a component of Microsoft Foundry, and its integration is central to the new functionality.
- **Model Deployment Pipelines:** The feature can be incorporated into existing Azure-based model deployment and inference pipelines, supporting more flexible and automated AI operations.

**Summary**  
The public preview of automatic model selection in AI Gateway, powered by the Microsoft Foundry model router, enables intelligent, dynamic backend model selection for each request, enhancing efficiency and flexibility in AI model management.

---

### 13. Generally Available: Deploy hosted agents from your own container registry in Foundry Toolkit for VS Code

**Published**: November 23, 2026 20:13:42 UTC
**Link**: [Generally Available: Deploy hosted agents from your own container registry in Foundry Toolkit for VS Code](https://azure.microsoft.com/updates?id=581478)

**Update ID**: 581478
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features, Microsoft Ignite

**Summary**:

- What was updated  
Foundry Toolkit for Visual Studio Code now supports deploying hosted agents from prebuilt container images stored in customer-managed container registries.

- Key changes or new features  
Developers can use container registries other than Azure Container Registry (ACR), including third-party or self-hosted registries, to source prebuilt agent images. When configuring a Foundry project, users can select the appropriate registry connection for their agents, enabling greater flexibility and control over image management and deployment.

- Target audience affected  
This update is relevant for developers and IT professionals using Foundry Toolkit for VS Code, especially those who manage their own container registries or require integration with non-ACR solutions.

- Important notes if any  
Ensure your registry connection is properly configured in the Foundry project settings to enable agent deployment from your chosen registry. This feature allows organizations to leverage their existing container image workflows and security policies, improving compatibility and governance for DevOps teams.  
For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=581478

**Details**:

**Azure Update Report: Deploy Hosted Agents from Customer-Managed Container Registries in Foundry Toolkit for Visual Studio Code**

**Background and Purpose of the Update**  
Previously, Foundry Toolkit for Visual Studio Code primarily supported deploying hosted agents using prebuilt images stored in Azure Container Registry (ACR). This update addresses the need for greater flexibility and control by enabling customers to deploy hosted agents from prebuilt images located in their own container registries, including registries other than ACR. The purpose is to allow organizations to leverage their existing container registry infrastructure, streamline agent deployment, and comply with organizational policies or regulatory requirements regarding image storage and management.

**Specific Features and Detailed Changes**  
- **Registry Selection:** Users can now select a registry connection within their Foundry project, allowing the toolkit to deploy hosted agents from prebuilt images in customer-managed container registries.
- **Registry Support:** The update expands support beyond Azure Container Registry, enabling compatibility with other container registries (e.g., Docker Hub, private registries).
- **Agent Deployment:** Hosted agents can be deployed directly from these registries, facilitating the use of custom or organization-specific agent images.

**Technical Mechanisms and Implementation Methods**  
- **Registry Connection Configuration:** Within the Foundry project settings in Visual Studio Code, users configure a connection to their preferred container registry. This involves specifying authentication credentials and registry endpoints.
- **Image Retrieval:** The Foundry Toolkit retrieves prebuilt agent images from the specified registry using secure protocols and authentication mechanisms.
- **Deployment Workflow:** Once the registry connection is established, the toolkit orchestrates the deployment of hosted agents using the selected images, ensuring compatibility with the Foundry environment.

**Use Cases and Application Scenarios**  
- **Custom Agent Images:** Organizations can maintain custom agent images in their own registries, ensuring that hosted agents are deployed with specific tooling, security configurations, or compliance requirements.
- **Multi-Registry Environments:** Enterprises operating multiple registries (on-premises or cloud-based) can integrate Foundry Toolkit with their preferred registry, supporting diverse development and deployment workflows.
- **Regulatory Compliance:** Companies with strict data residency or security policies can use their own registries to store agent images, avoiding external dependencies.

**Important Considerations and Limitations**  
- **Registry Authentication:** Proper configuration of authentication credentials is required to access customer-managed registries. Failure to do so may result in deployment errors.
- **Image Compatibility:** Prebuilt agent images must be compatible with the Foundry Toolkit’s requirements. Unsupported or improperly configured images may cause deployment failures.
- **Network Access:** Ensure that the Foundry environment has network access to the specified registry, particularly for private or on-premises registries.

**Integration with Related Azure Services**  
- **Azure Container Registry (ACR):** While ACR remains supported, this update allows seamless integration with other registries, providing flexibility in agent image sourcing.
- **Azure DevOps and CI/CD Pipelines:** Hosted agents deployed from custom registries can be used in Azure DevOps pipelines, enabling tailored build and deployment environments.
- **Azure Security and Networking:** Integration with Azure networking and security services may be necessary to facilitate secure access to private registries.

**Summary Sentence**  
Foundry Toolkit for Visual Studio Code now enables deployment of hosted agents from prebuilt images in customer-managed container registries, including registries beyond Azure Container Registry, providing enhanced flexibility and control for organizations managing their own agent images.

---

### 14. Generally Available: Wildcard domain support in Azure Firewall network rules 

**Published**: November 23, 2026 18:51:31 UTC
**Link**: [Generally Available: Wildcard domain support in Azure Firewall network rules ](https://azure.microsoft.com/updates?id=582030)

**Update ID**: 582030
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall network rules now support wildcard domain patterns in FQDN-based rules, and this feature is generally available.

- Key changes or new features  
You can now define network rules using wildcard domains (e.g., *.contoso.com) instead of listing individual FQDNs. This simplifies rule management and enhances security by allowing broader, flexible domain matching within firewall policies.

- Target audience affected  
This update impacts IT professionals managing Azure Firewall configurations and developers responsible for network security and application connectivity in Azure environments.

- Important notes  
Wildcard domain support streamlines rule creation and maintenance, especially for environments where destination domains change frequently or include multiple subdomains. It is recommended to review existing firewall rules and consider migrating to wildcard-based rules where appropriate to improve scalability and manageability. This feature is available in all regions where Azure Firewall is deployed.

**Details**:

**Comprehensive Technical Explanation: Azure Update – Wildcard Domain Support in Azure Firewall Network Rules (Generally Available)**

**Background and Purpose of the Update**  
Azure Firewall is a managed, cloud-based network security service that protects Azure Virtual Network resources. Traditionally, Azure Firewall network rules allowed customers to specify Fully Qualified Domain Names (FQDNs) for outbound traffic filtering. However, this approach required explicit listing of each domain, which was cumbersome when dealing with multiple subdomains or dynamic domain structures. The purpose of this update is to simplify and enhance the management of network rules by introducing wildcard domain support, allowing administrators to define rules using wildcard patterns (e.g., *.contoso.com).

**Specific Features and Detailed Changes**  
With this update, Azure Firewall network rules now support wildcard domain patterns in FQDN-based rules. Administrators can specify domains using wildcards such as *.contoso.com, enabling the rule to match any subdomain under contoso.com. This feature is generally available, meaning it is fully supported and recommended for production environments. The change specifically impacts the way FQDNs are defined in network rules, allowing for broader and more flexible domain matching without the need to enumerate each possible subdomain.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages Azure Firewall’s DNS resolution capabilities. When a network rule is defined with a wildcard domain, Azure Firewall dynamically resolves outbound traffic destinations using DNS queries. If the destination matches the wildcard pattern specified in the rule, the traffic is allowed or denied according to the rule’s action. The firewall maintains a cache of resolved domains and updates it periodically to ensure accuracy and performance. This mechanism ensures that wildcard rules are enforced efficiently, without introducing significant latency or complexity to rule processing.

**Use Cases and Application Scenarios**  
- **Securing SaaS Applications:** Many SaaS providers use multiple subdomains for service endpoints (e.g., api.contoso.com, login.contoso.com). Wildcard domain support allows organizations to permit access to all relevant subdomains with a single rule.
- **Dynamic Domain Environments:** For environments where subdomains are frequently added or changed, wildcard rules reduce administrative overhead and ensure consistent security coverage.
- **Simplified Rule Management:** Enterprises can streamline their firewall rule sets by replacing numerous individual FQDN rules with a single wildcard rule, improving manageability and reducing the risk of missing critical endpoints.

**Important Considerations and Limitations**  
- **DNS Dependency:** Wildcard domain rules rely on DNS resolution. If DNS records change or if domains are not resolvable at the time of rule processing, traffic may not be matched as expected.
- **Granularity:** While wildcard rules offer flexibility, they may inadvertently allow access to unintended subdomains. Administrators should carefully evaluate the scope of wildcard patterns to avoid over-permissive rules.
- **Performance:** Azure Firewall manages DNS caching and resolution internally, but large numbers of wildcard rules or high-frequency DNS changes may impact performance. Monitoring and tuning may be necessary in complex environments.

**Integration with Related Azure Services**  
Wildcard domain support in Azure Firewall network rules integrates seamlessly with other Azure security and networking services. It complements Azure Firewall’s application rules and threat intelligence filtering, and can be used alongside Azure Virtual Network, Azure DNS, and Azure Policy for comprehensive security management. This feature enhances the overall flexibility and control of outbound traffic filtering in Azure environments.

**Summary Sentence:**  
Wildcard domain support in Azure Firewall network rules is now generally available, enabling customers to use wildcard patterns such as *.contoso.com for FQDN-based outbound traffic filtering, thereby simplifying rule management and enhancing security coverage across dynamic domain environments.

---

### 15. Retirement: Azure AI Content Safety selected features will be retired on April 30, 2027

**Published**: November 23, 2026 18:11:31 UTC
**Link**: [Retirement: Azure AI Content Safety selected features will be retired on April 30, 2027](https://azure.microsoft.com/updates?id=577474)

**Update ID**: 577474
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Azure AI Content Safety, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of selected preview features in Azure AI Content Safety, effective April 30, 2027.

- Key changes or new features  
The following capabilities will be retired:  
  - Analyze Multimodal  
  - Custom categories (rapid), including text and image  
  - Connected containers for Text, Image, and Prompt Shields  
  - Disconnected containers for Text and Image  
These features are currently in preview and will no longer be supported after the retirement date. No new features were introduced in this update.

- Target audience affected  
Developers and IT professionals using Azure AI Content Safety preview features, especially those integrating multimodal analysis, custom categories, or containerized deployments for content safety.

- Important notes  
If you are using any of the listed preview capabilities, plan to migrate your workloads to supported alternatives before April 30, 2027. After this date, these features will be unavailable and unsupported. Review your current implementations and consult Azure documentation for guidance on migration paths and supported features.  
For more information, visit the official Azure Update: https://azure.microsoft.com/updates?id=577474

**Details**:

**Azure Update Report: Retirement of Azure AI Content Safety Selected Features (April 30, 2027)**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of several preview capabilities within the Azure AI Content Safety suite, effective April 30, 2027. This update is part of Azure’s ongoing lifecycle management process, aiming to streamline service offerings and focus on stable, production-ready features. The retirement targets features that are currently in preview, indicating they may not have reached general availability or broad adoption.

**Specific Features and Detailed Changes**  
The following Azure AI Content Safety preview features will be retired:

- **Analyze Multimodal**: This capability enables content analysis across multiple modalities, such as text and images, for detecting harmful or unsafe content.
- **Custom Categories (Rapid)**: Allows users to define and rapidly deploy custom content safety categories for both text and image analysis.
- **Connected Containers for Text, Image, and Prompt Shields**: These containers provide integrated content safety protection for text, image, and prompt inputs, facilitating real-time content moderation.
- **Disconnected Containers for Text, Image**: These containers operate independently for content safety analysis on text and image data, without integration to other Azure services.
- **Em**: The update mentions “Em,” but no further details are provided in the announcement.

**Technical Mechanisms and Implementation Methods**  
These preview features leverage containerized deployments, enabling users to run Azure AI Content Safety models in isolated environments. Connected containers allow for seamless integration with Azure services, while disconnected containers provide standalone operation. The multimodal analysis uses AI models to process and evaluate content across different formats, and custom categories (rapid) offer flexible configuration for specific organizational needs.

**Use Cases and Application Scenarios**  
Typical use cases for these features include:

- **Content Moderation**: Automated detection and filtering of harmful or inappropriate content in user-generated text and images.
- **Compliance and Safety**: Ensuring content adheres to organizational or regulatory standards.
- **Prompt Shielding**: Protecting AI-driven conversational interfaces from unsafe or malicious prompts.
- **Custom Policy Enforcement**: Rapid deployment of custom moderation rules tailored to specific business requirements.

**Important Considerations and Limitations**  
- **End-of-Life Date**: All listed preview features will be unavailable after April 30, 2027. Users must plan migration strategies to alternative solutions before this date to avoid service disruption.
- **Preview Status**: These features are not generally available and may lack full support, stability, or integration compared to production-grade offerings.
- **Migration Path**: The announcement does not specify replacement features or migration guidance. Users should monitor Azure updates for future announcements regarding alternative solutions or enhancements to the AI Content Safety suite.

**Integration with Related Azure Services**  
The connected containers are designed for integration with Azure services, such as Azure AI, Azure Kubernetes Service (AKS), and Azure Cognitive Services. Disconnected containers offer flexibility for on-premises or hybrid deployments. The retirement may impact workflows that rely on these integrations, requiring review and potential re-architecture of content safety pipelines.

**Summary Sentence**  
Azure will retire selected preview features of Azure AI Content Safety—including Analyze Multimodal, Custom Categories (rapid), and container-based deployments—on April 30, 2027, requiring users to plan for migration and review their content safety implementations.

---

### 16. Public Preview: Azure Database for PostgreSQL enhanced Burstable tier (Basv2) 

**Published**: November 23, 2026 18:09:39 UTC
**Link**: [Public Preview: Azure Database for PostgreSQL enhanced Burstable tier (Basv2) ](https://azure.microsoft.com/updates?id=574535)

**Update ID**: 574535
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Microsoft Ignite, Feature

**Summary**:

- What was updated  
Azure Database for PostgreSQL now offers an enhanced Burstable tier (Basv2) in public preview.

- Key changes or new features  
The Basv2 tier improves upon the previous burstable model by providing greater performance predictability and more efficient burst utilization. This allows for better cost-performance optimization, enabling steady workloads to run more economically while still supporting occasional spikes in resource demand. Basv2 is designed to deliver consistent baseline performance with the ability to burst when needed, making it suitable for variable workloads.

- Target audience affected  
Developers and IT professionals managing PostgreSQL databases on Azure, especially those with workloads that are typically steady but occasionally require higher performance, will benefit from this update. It is particularly relevant for teams seeking cost-effective solutions without sacrificing performance during peak times.

- Important notes if any  
The Basv2 tier is currently available in public preview. Users should evaluate its suitability for production workloads and monitor performance during the preview phase. Pricing and regional availability may differ from the existing burstable tier. For more details, visit the official Azure update page: https://azure.microsoft.com/updates?id=574535

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Database for PostgreSQL Enhanced Burstable Tier (Basv2)

**Background and Purpose of the Update:**  
The Enhanced Burstable tier (Basv2) for Azure Database for PostgreSQL is introduced to address the need for improved performance predictability and cost efficiency in cloud-hosted PostgreSQL workloads. Traditional burstable tiers allowed temporary performance boosts but often lacked consistent predictability and efficient resource utilization. The Basv2 tier is designed to optimize both steady-state and burst workloads, providing a more balanced approach to cost and performance for customers running PostgreSQL databases on Azure.

**Specific Features and Detailed Changes:**  
The Basv2 tier builds upon the existing burstable model with several enhancements:
- **Improved Performance Predictability:** Basv2 offers more consistent performance during both baseline and burst periods, reducing variability and ensuring workloads behave as expected.
- **Efficient Burst Utilization:** The mechanism for utilizing burst credits is optimized, enabling workloads to leverage bursts more effectively without excessive overhead or unpredictable throttling.
- **Cost-Performance Balance:** Customers can run steady workloads more economically, as Basv2 is tailored to minimize costs while maintaining sufficient performance for typical PostgreSQL operations.

**Technical Mechanisms and Implementation Methods:**  
Basv2 utilizes an enhanced burst credit system, where compute resources are allocated based on workload demands. Credits accumulate during periods of low activity and are consumed during bursts, allowing for temporary performance increases. The improved algorithm ensures that credit accrual and consumption are more tightly aligned with actual workload requirements, reducing the risk of performance degradation during sustained activity. The tier is integrated into the Azure Database for PostgreSQL provisioning workflow, allowing customers to select Basv2 during database creation or scaling operations.

**Use Cases and Application Scenarios:**  
Basv2 is ideal for:
- **Steady Workloads:** Applications with predictable, moderate resource requirements benefit from the cost savings and performance consistency.
- **Variable Workloads:** Workloads that experience occasional spikes (e.g., reporting, batch processing) can utilize burst credits efficiently without over-provisioning.
- **Development and Testing:** Environments where cost control is critical and workloads are not consistently heavy can leverage Basv2 for optimal resource utilization.

**Important Considerations and Limitations:**  
- **Public Preview:** Basv2 is currently in public preview, which means it may not be suitable for production workloads requiring full SLA guarantees.
- **Workload Suitability:** Workloads with sustained high resource demands may exhaust burst credits quickly, leading to throttling and reduced performance.
- **Feature Availability:** Some advanced features or integrations may not be fully supported in the preview phase; users should verify compatibility with their requirements.

**Integration with Related Azure Services:**  
Basv2 is fully integrated with Azure Database for PostgreSQL, supporting standard management, monitoring, and scaling operations through the Azure portal, CLI, and API. It can be combined with Azure Backup, Azure Monitor, and other ecosystem services for comprehensive database management and observability.

**Summary Sentence:**  
The Enhanced Burstable tier (Basv2) for Azure Database for PostgreSQL, now in public preview, offers improved performance predictability and efficient burst utilization, enabling IT professionals to achieve a better cost-performance balance for steady and variable workloads on Azure.

---

### 17. Generally Available: WAF Insights for Azure Application Gateway

**Published**: November 23, 2026 18:02:38 UTC
**Link**: [Generally Available: WAF Insights for Azure Application Gateway](https://azure.microsoft.com/updates?id=579280)

**Update ID**: 579280
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Web Application Firewall, Features

**Summary**:

- What was updated  
WAF Insights for Azure Application Gateway Web Application Firewall (WAF) is now generally available.

- Key changes or new features  
WAF Insights provides a built-in dashboard experience within the WAF policy, consolidating WAF logs and metrics into interactive visualizations. This enables users to quickly investigate blocked requests, analyze attack patterns, and monitor WAF activity without needing external tools or manual log analysis. The dashboards support drill-down capabilities for detailed inspection and facilitate faster troubleshooting and security response.

- Target audience affected  
Developers and IT professionals responsible for managing Azure Application Gateway and WAF policies, particularly those focused on application security, monitoring, and incident response.

- Important notes  
WAF Insights is natively integrated and does not require additional setup or third-party solutions. It streamlines log analysis and security monitoring, improving operational efficiency and reducing time-to-resolution for security incidents. Users should ensure their WAF policies are up to date to leverage these new capabilities. For more information, visit the official Azure Update [link](https://azure.microsoft.com/updates?id=579280).

**Details**:

**Azure Update Report: Generally Available – WAF Insights for Azure Application Gateway**

**Background and Purpose of the Update**  
The release of WAF Insights for Azure Application Gateway Web Application Firewall (WAF) addresses the need for enhanced visibility and analytics regarding WAF activity. Previously, IT professionals had to manually aggregate logs and metrics from disparate sources to analyze WAF events, which could be time-consuming and error-prone. The purpose of this update is to provide a unified, built-in experience within the WAF policy, streamlining the process of monitoring, investigating, and responding to WAF-related incidents.

**Specific Features and Detailed Changes**  
WAF Insights introduces interactive dashboards that consolidate WAF logs and metrics. These dashboards are integrated directly into the WAF policy interface, enabling users to visualize and analyze security events such as block actions, detection events, and traffic patterns. The update provides the following features:
- Centralized access to WAF logs and metrics within the Azure portal.
- Interactive dashboards for real-time investigation of WAF activity.
- Visualization of blocked requests, attack types, and rule triggers.
- Enhanced filtering and drill-down capabilities for detailed event analysis.

**Technical Mechanisms and Implementation Methods**  
WAF Insights leverages Azure’s native logging and monitoring infrastructure. It aggregates WAF logs and metrics generated by the Application Gateway and presents them through built-in dashboards. The technical implementation involves:
- Automatic collection of WAF logs (such as request details, rule matches, and block actions) and metrics (such as request rates and error counts).
- Integration with the WAF policy configuration, allowing users to access insights without external tools or manual log parsing.
- Use of Azure portal’s dashboard and visualization components for interactive analysis.

**Use Cases and Application Scenarios**  
WAF Insights is particularly useful for IT professionals responsible for web application security and compliance. Typical scenarios include:
- Rapid investigation of blocked requests to determine false positives or true threats.
- Monitoring attack trends and rule effectiveness to optimize WAF policies.
- Compliance reporting by exporting dashboard data for audit purposes.
- Troubleshooting application access issues related to WAF rule enforcement.

**Important Considerations and Limitations**  
While WAF Insights provides a built-in experience for log and metric analysis, IT professionals should consider the following:
- The feature is available only for Azure Application Gateway WAF.
- Insights are limited to the data collected by WAF logs and metrics; deeper analysis may require integration with Azure Monitor or external SIEM solutions.
- Proper configuration of WAF logging is necessary to ensure comprehensive data coverage.
- The dashboards are designed for interactive investigation; automated alerting and custom reporting may require additional Azure services.

**Integration with Related Azure Services**  
WAF Insights operates within the Azure Application Gateway ecosystem and complements other Azure security and monitoring services:
- Can be used alongside Azure Monitor for advanced alerting and analytics.
- Supports integration with Azure Security Center for broader threat detection.
- Data from WAF Insights can be exported or correlated with logs from other Azure resources for holistic security analysis.

**Summary Sentence**  
WAF Insights for Azure Application Gateway is now generally available, offering IT professionals a built-in, interactive dashboard experience that consolidates WAF logs and metrics for streamlined investigation and monitoring of web application firewall activity.

---

### 18. Generally Available: WAF Insights for Azure Front Door

**Published**: November 23, 2026 18:01:19 UTC
**Link**: [Generally Available: WAF Insights for Azure Front Door](https://azure.microsoft.com/updates?id=579285)

**Update ID**: 579285
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Front Door, Web Application Firewall, Features

**Summary**:

- What was updated  
WAF Insights is now generally available for Azure Front Door Web Application Firewall (WAF).

- Key changes or new features  
WAF Insights provides a built-in dashboard experience within the WAF policy. It consolidates WAF logs and metrics into interactive dashboards, enabling users to easily investigate blocked requests, analyze attack patterns, and monitor WAF effectiveness. The dashboards offer visualizations and drill-down capabilities for detailed analysis, reducing the need for manual log parsing or external tools.

- Target audience affected  
Developers and IT professionals managing web applications with Azure Front Door and WAF policies. Security teams responsible for monitoring and responding to web attacks will benefit from improved visibility and analytics.

- Important notes  
WAF Insights is integrated directly into the Azure portal, requiring no additional setup or external dependencies. This release enhances operational efficiency and security posture by streamlining access to WAF data and actionable insights. Users should review their WAF policies to leverage the new dashboard features for improved threat detection and response.  
For more details, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=579285).

**Details**:

**Azure Update Report**

**Title:** Generally Available: WAF Insights for Azure Front Door  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=579285)

---

**Background and Purpose of the Update:**  
Azure Front Door provides global, scalable, and secure entry points for web applications. Its Web Application Firewall (WAF) protects applications from common threats and vulnerabilities. Previously, monitoring WAF activity required manual log analysis or external tools, which could be cumbersome and slow. The purpose of this update is to streamline security monitoring by introducing WAF Insights—a built-in experience that consolidates WAF logs and metrics into interactive dashboards. This enables IT professionals to investigate blocked requests and security events more efficiently and directly within the Azure portal.

**Specific Features and Detailed Changes:**  
- **WAF Insights Dashboard:** A new interactive dashboard is integrated into the WAF policy experience for Azure Front Door.  
- **Unified Logs and Metrics:** WAF logs (such as blocked requests, rule matches, and threat detections) and operational metrics are aggregated and visualized together.  
- **Investigation Tools:** The dashboard allows users to drill down into specific security events, analyze patterns, and identify potential threats or misconfigurations.  
- **General Availability:** The feature is now generally available, meaning it is fully supported and recommended for production use.

**Technical Mechanisms and Implementation Methods:**  
- **Built-In Integration:** WAF Insights is embedded within the Azure Front Door WAF policy interface, eliminating the need for external analytics solutions or custom dashboards.  
- **Data Aggregation:** WAF logs and metrics are collected from the Azure Front Door service and processed to provide real-time and historical views.  
- **Interactive Visualization:** The dashboard leverages Azure portal visualization capabilities, allowing users to filter, sort, and analyze data interactively.  
- **Security Event Investigation:** IT professionals can use the dashboard to trace blocked requests, review rule triggers, and correlate events with application traffic patterns.

**Use Cases and Application Scenarios:**  
- **Security Monitoring:** Quickly identify and investigate blocked requests, suspicious activity, or abnormal traffic patterns.  
- **Incident Response:** Accelerate root cause analysis for security incidents by providing immediate access to relevant WAF logs and metrics.  
- **Policy Optimization:** Review WAF rule effectiveness and adjust policies based on observed trends and false positives.  
- **Compliance Reporting:** Generate visual reports for compliance audits and demonstrate proactive security management.

**Important Considerations and Limitations:**  
- **Scope:** WAF Insights is specific to Azure Front Door WAF policies and does not apply to other Azure WAF implementations (e.g., Application Gateway).  
- **Data Retention:** The dashboard displays logs and metrics as processed by Azure Front Door; retention policies and granularity may depend on Azure’s logging configuration.  
- **Customization:** The built-in dashboard offers predefined visualizations; advanced customization may require exporting logs to Azure Monitor or Log Analytics for further analysis.

**Integration with Related Azure Services:**  
- **Azure Portal:** WAF Insights is accessed directly through the Azure portal, providing seamless integration with other Azure management tools.  
- **Azure Monitor and Log Analytics:** For extended analytics, logs can be exported to Azure Monitor or Log Analytics, enabling deeper investigation and custom reporting.  
- **Security Center:** Insights can complement Azure Security Center’s threat detection and compliance features.

---

**Summary Sentence:**  
WAF Insights for Azure Front Door is now generally available, providing IT professionals with an integrated, interactive dashboard that consolidates WAF logs and metrics for streamlined security monitoring and investigation directly within the Azure portal.

---


*This report was automatically generated - 2026-11-24 03:09:38 UTC*