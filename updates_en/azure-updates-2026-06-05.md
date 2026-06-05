# June 05, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 05, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 13 items

## Update List

### 1. Public Preview: Voice sync for avatar support in Voice Live API in Microsoft Foundry

**Published**: June 04, 2026 22:15:50 UTC
**Link**: [Public Preview: Voice sync for avatar support in Voice Live API in Microsoft Foundry](https://azure.microsoft.com/updates?id=564176)

**Update ID**: 564176
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry’s Voice Live API now supports avatar voice synchronization with custom voices, available in public preview.

- Key changes or new features  
Developers can now pair branded or persona-specific text-to-speech (TTS) voices with real-time avatar experiences. This enables avatars to speak with custom voices that match brand identity or character personas, enhancing user engagement in interactive applications. The feature supports real-time voice sync, improving the realism and personalization of avatar interactions.

- Target audience affected  
This update is relevant for developers and IT professionals building applications with real-time avatars, such as virtual assistants, customer service bots, interactive training, or entertainment experiences. Teams focused on branding, user engagement, or conversational AI will benefit most.

- Important notes if any  
The feature is currently in public preview and may be subject to changes. Integration requires use of the Voice Live API and custom TTS voices. Developers should review documentation for compatibility and implementation details. Feedback during the preview phase is encouraged to help improve the feature before general availability.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=564176

**Details**:

**Background and Purpose of the Update**  
This update introduces public preview support for avatar voice synchronization with custom voices in the Voice Live API, as part of Microsoft Foundry. The primary purpose is to enable developers to pair branded or persona-specific text-to-speech (TTS) voices with real-time avatar experiences. This enhancement is aimed at teams building interactive applications where avatars communicate using synthesized speech, ensuring that the avatar’s visual speech movements are synchronized with the audio output.

**Specific Features and Detailed Changes**  
- **Avatar Voice Sync:** The Voice Live API now supports synchronizing avatar mouth movements (visemes) with custom TTS voices, including branded or persona-specific voices.
- **Custom Voice Integration:** Developers can use custom voices created or configured for their brand or application, rather than being limited to standard voice options.
- **Real-Time Experience:** The API is designed for real-time applications, allowing immediate synchronization between voice output and avatar animation.

**Technical Mechanisms and Implementation Methods**  
- **Voice Live API Enhancement:** The update extends the Voice Live API to handle both audio stream generation and the corresponding viseme data required for avatar animation.
- **Custom Voice Support:** Developers can specify custom voice models when invoking the API, ensuring the generated audio matches the desired persona.
- **Synchronization Data:** The API provides the necessary timing and phoneme/viseme mapping data to drive avatar lip-sync in real time.
- **Integration Workflow:** Applications send TTS requests with custom voice parameters to the API and receive both the audio stream and synchronization metadata, which can be fed into avatar rendering engines.

**Use Cases and Application Scenarios**  
- **Branded Virtual Assistants:** Enterprises can deploy avatars with voices that match their brand identity in customer service bots or kiosks.
- **Interactive Training and Education:** Real-time avatars with custom voices can enhance engagement in e-learning platforms.
- **Gaming and Entertainment:** Developers can create in-game characters with unique voices and synchronized facial animations for immersive storytelling.
- **Accessibility Solutions:** Avatars with synchronized speech can assist users with hearing impairments by providing visual cues.

**Important Considerations and Limitations**  
- **Public Preview:** The feature is in public preview, which means it may not be production-ready and could be subject to changes.
- **Custom Voice Requirements:** Using custom voices may require prior setup and configuration within the Azure ecosystem.
- **Performance and Latency:** Real-time synchronization depends on network and processing latency; developers should test for acceptable performance in their scenarios.
- **Compatibility:** Integration with avatar rendering engines requires proper handling of viseme synchronization data.

**Integration with Related Azure Services**  
- **Azure Cognitive Services Speech:** The Voice Live API builds on Azure’s TTS capabilities, including custom voice models.
- **Azure Bot Services:** Avatars with synchronized speech can be integrated into conversational bots.
- **Azure Media Services:** For applications involving media streaming or recording, integration with media services may be required for end-to-end solutions.

**Summary Sentence**  
The public preview of avatar voice sync with custom voices in the Voice Live API for Microsoft Foundry enables developers to deliver real-time, persona-specific text-to-speech experiences with synchronized avatar animations, enhancing the realism and brand alignment of interactive applications.

---

### 2. Generally Available: Azure Files assessments are now available worldwide using Azure Migrate

**Published**: June 04, 2026 21:45:11 UTC
**Link**: [Generally Available: Azure Files assessments are now available worldwide using Azure Migrate](https://azure.microsoft.com/updates?id=564563)

**Update ID**: 564563
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Migration, Azure Migrate, Services, Feature

**Summary**:

- What was updated  
Azure Migrate now offers general availability of Azure Files assessments for SMB and NFS file shares worldwide.

- Key changes or new features  
Azure Migrate can now discover and assess SMB and NFS file shares hosted on both Windows and Linux servers. This enhancement provides a comprehensive, data-driven view of file share environments, enabling customers to plan migrations to Azure Files more effectively. The assessment includes compatibility checks, sizing recommendations, and cost estimates, streamlining the migration process.

- Target audience affected  
This update is relevant to IT professionals, infrastructure architects, and developers responsible for managing or migrating on-premises file shares to Azure. Organizations planning to modernize or consolidate file storage in the cloud will benefit most.

- Important notes if any  
The feature supports both SMB and NFS protocols, covering a wide range of file share scenarios. Assessments help identify potential migration blockers and provide actionable recommendations, reducing migration risk and effort. The update is now available globally through Azure Migrate.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=564563

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Files assessments are now available worldwide using Azure Migrate  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=564563)

---

**Background and Purpose of the Update:**  
This update announces the general availability of Azure Files assessments within Azure Migrate, now accessible globally. The primary objective is to enable organizations to discover and assess SMB (Server Message Block) and NFS (Network File System) file shares hosted on both Windows and Linux servers. The update addresses the need for a comprehensive, data-driven approach to inventorying and evaluating on-premises file share environments as part of cloud migration planning.

---

**Specific Features and Detailed Changes:**  
- **Discovery and Assessment Support:** Azure Migrate now supports automated discovery and assessment of SMB and NFS file shares.
- **Cross-Platform Compatibility:** The feature covers file shares hosted on both Windows and Linux servers, expanding the scope of supported environments.
- **Data-Driven Insights:** The assessment provides a detailed view of the file share environment, including inventory, usage patterns, and readiness for migration to Azure Files.
- **Global Availability:** The capability is now generally available worldwide, removing previous geographic restrictions.

---

**Technical Mechanisms and Implementation Methods:**  
- **Azure Migrate Integration:** The feature is integrated into the Azure Migrate platform, leveraging its existing discovery and assessment workflows.
- **Discovery Process:** Agents or appliances deployed as part of Azure Migrate scan the target environment to identify SMB and NFS file shares.
- **Assessment Engine:** Collected data is analyzed to generate reports on file share inventory, utilization, and suitability for migration to Azure Files.
- **Reporting:** The assessment results are presented within the Azure Migrate portal, enabling IT professionals to review findings and plan migration strategies.

---

**Use Cases and Application Scenarios:**  
- **Migration Planning:** Organizations planning to migrate on-premises SMB or NFS file shares to Azure Files can use this feature to assess their current environment and estimate migration effort.
- **Hybrid Cloud Deployments:** Enterprises with a mix of Windows and Linux file servers can inventory and evaluate all file shares in a unified manner.
- **Data Consolidation:** IT teams can identify redundant or underutilized file shares, supporting data consolidation and optimization initiatives before migration.
- **Compliance and Reporting:** The assessment provides documentation of the file share landscape, aiding in compliance audits and IT reporting.

---

**Important Considerations and Limitations:**  
- **Supported Protocols:** Only SMB and NFS file shares are covered by this assessment; other file sharing protocols are not included.
- **Source Environments:** The feature is limited to file shares hosted on Windows and Linux servers.
- **Assessment Scope:** The update focuses on discovery and assessment; actual migration of file shares to Azure Files is a separate process.

---

**Integration with Related Azure Services:**  
- **Azure Files:** The assessment is designed to facilitate migration to Azure Files, Azure’s managed file share service.
- **Azure Migrate:** The feature is a native part of Azure Migrate, allowing users to leverage existing migration project workflows and dashboards.
- **Complementary Assessments:** Users can combine file share assessments with other Azure Migrate assessments (e.g., server, database) for holistic migration planning.

---

**Summary Sentence:**  
Azure Migrate now offers global, generally available support for automated discovery and assessment of SMB and NFS file shares on Windows and Linux servers, providing IT professionals with comprehensive, data-driven insights to streamline migration planning to Azure Files.

---

### 3. Public Preview: AI pipelines in Azure HorizonDB

**Published**: June 04, 2026 19:45:40 UTC
**Link**: [Public Preview: AI pipelines in Azure HorizonDB](https://azure.microsoft.com/updates?id=565182)

**Update ID**: 565182
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure HorizonDB, Features, Microsoft Build

**Summary**:

- What was updated  
Public preview release of AI pipelines in Azure HorizonDB.

- Key changes or new features  
AI pipelines now allow users to define and execute end-to-end AI data workflows directly within Azure HorizonDB using declarative SQL. Supported pipeline steps include data ingestion, chunking, embedding, extraction, generation, and ranking. These workflows are executed as fault-tolerant pipelines within the database environment, streamlining the integration of AI processing with data operations.

- Target audience affected  
Developers and IT professionals working with Azure HorizonDB, particularly those building AI-powered applications or managing large-scale data processing and analytics workflows.

- Important notes if any  
This feature enables seamless integration of AI tasks into data workflows using SQL, reducing the need for external orchestration or custom code. As this is a public preview, it is recommended for development and testing purposes, not for production workloads. Users should review preview documentation for limitations and provide feedback to Microsoft.  

Link: [Azure Update - AI pipelines in Azure HorizonDB (Public Preview)](https://azure.microsoft.com/updates?id=565182)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: AI pipelines in Azure HorizonDB  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=565182)

---

**Background and Purpose of the Update:**  
The introduction of AI pipelines in Azure HorizonDB, now available in public preview, addresses the growing need for integrated, declarative AI data processing within database environments. As organizations increasingly leverage AI for data-driven applications, there is a demand for streamlined workflows that handle data ingestion, transformation, and AI-driven operations directly within the data platform. This update aims to simplify and standardize the orchestration of complex AI data workflows by embedding them natively in HorizonDB using SQL.

---

**Specific Features and Detailed Changes:**  
- **Declarative AI Workflow Definition:** Users can now define end-to-end AI data workflows—including ingestion, chunking, embedding, extraction, generation, and ranking—directly in SQL statements.
- **Integrated Pipeline Execution:** These AI pipelines are executed as fault-tolerant processes within the HorizonDB environment, ensuring reliability and resilience.
- **Expanded SQL Capabilities:** The SQL interface is extended to support declarative definitions of AI tasks, enabling users to manage both traditional data operations and AI workflows in a unified manner.

---

**Technical Mechanisms and Implementation Methods:**  
- **Declarative SQL Syntax:** AI pipelines are described in SQL, allowing users to specify each stage of the workflow (such as chunking or embedding) as part of their queries or procedures.
- **Fault-Tolerant Pipeline Execution:** The underlying execution engine in HorizonDB manages the orchestration and error handling of each pipeline stage, ensuring that failures are managed gracefully and do not compromise the overall workflow.
- **In-Database Processing:** All AI pipeline operations are executed inside HorizonDB, reducing data movement and latency, and leveraging the database’s native scalability and security features.

---

**Use Cases and Application Scenarios:**  
- **AI-Driven Data Ingestion:** Automate the process of ingesting raw data, applying chunking and embedding techniques for downstream AI applications such as search or recommendation systems.
- **Text and Data Extraction:** Extract structured information from unstructured data sources using AI models, directly within the database.
- **Content Generation and Ranking:** Implement generative AI workflows for content creation or ranking outputs (e.g., document summarization, response generation) as part of the data processing pipeline.
- **Operationalizing AI in Data Workflows:** Seamlessly integrate AI processing into ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) pipelines for analytics and business intelligence.

---

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should expect potential changes and limited support.
- **SQL Syntax and Compatibility:** The specific SQL extensions and supported AI operations are limited to what is provided in the preview; users should review documentation for supported features.
- **Resource Management:** Running AI pipelines within the database may impact resource utilization; careful planning and monitoring are recommended.

---

**Integration with Related Azure Services:**  
- **Azure HorizonDB Ecosystem:** AI pipelines are natively integrated into HorizonDB, allowing seamless use alongside existing database features.
- **Potential for Broader Azure Integration:** While not explicitly stated, this update lays the foundation for tighter integration with Azure AI services and data platforms, facilitating end-to-end AI data workflows within the Azure ecosystem.

---

**Summary Sentence:**  
The public preview of AI pipelines in Azure HorizonDB enables IT professionals to define and execute comprehensive AI data workflows declaratively in SQL, providing fault-tolerant, in-database processing for ingestion, transformation, and AI-driven operations.

---

### 4. Generally Available: Ingest OTLP signals into Azure Monitor with the OpenTelemetry Collector

**Published**: June 04, 2026 19:45:40 UTC
**Link**: [Generally Available: Ingest OTLP signals into Azure Monitor with the OpenTelemetry Collector](https://azure.microsoft.com/updates?id=565090)

**Update ID**: 565090
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Microsoft Build, Open Source

**Summary**:

- What was updated  
Azure Monitor now offers general availability for native ingestion of OpenTelemetry Protocol (OTLP) signals via the OpenTelemetry Collector.

- Key changes or new features  
Developers and IT professionals can now send telemetry data (traces, metrics, logs) directly from OpenTelemetry-instrumented applications and platforms to Azure Monitor using the OTLP protocol. This eliminates the need for custom exporters or additional data transformation layers. The integration supports both OTLP/gRPC and OTLP/HTTP protocols, streamlining observability workflows and enabling unified monitoring across distributed systems.

- Target audience affected  
Application developers, DevOps engineers, and IT professionals responsible for monitoring, observability, and diagnostics in cloud-native or distributed environments.

- Important notes if any  
To leverage this feature, configure your OpenTelemetry Collector to use Azure Monitor as an OTLP endpoint. This update simplifies integration with Azure Monitor for organizations already using OpenTelemetry, reducing operational overhead and accelerating troubleshooting. Review Azure Monitor documentation for configuration details and best practices.

Link: https://azure.microsoft.com/updates?id=565090

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Ingest OTLP signals into Azure Monitor with the OpenTelemetry Collector  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=565090)

---

### Background and Purpose of the Update

This update marks the general availability of native ingestion of OpenTelemetry Protocol (OTLP) signals into Azure Monitor. The primary goal is to streamline the process of collecting telemetry data—such as traces, metrics, and logs—from applications and platforms that are instrumented with OpenTelemetry. By supporting OTLP natively, Azure Monitor enables direct integration with the OpenTelemetry ecosystem, reducing the need for custom adapters or intermediary exporters.

---

### Specific Features and Detailed Changes

- **Native OTLP Ingestion:** Azure Monitor now accepts telemetry data in OTLP format, which is the standard protocol for OpenTelemetry.
- **Direct Data Pipeline:** Telemetry can be sent directly from OpenTelemetry-instrumented sources to Azure Monitor without additional transformation layers.
- **OpenTelemetry Collector Integration:** The update supports configuration of the OpenTelemetry Collector to forward signals to Azure Monitor, facilitating centralized and scalable telemetry data management.

---

### Technical Mechanisms and Implementation Methods

- **OTLP Protocol Support:** Azure Monitor endpoints now natively accept data in the OTLP format, which is typically transmitted over gRPC or HTTP.
- **Collector Configuration:** IT professionals can configure the OpenTelemetry Collector to use Azure Monitor as an exporter. This involves specifying Azure Monitor as a destination in the collector’s pipeline, ensuring seamless data flow from instrumented applications to Azure Monitor.
- **Signal Types:** The ingestion supports various telemetry signals, such as distributed traces, metrics, and logs, as defined by the OpenTelemetry specification.

---

### Use Cases and Application Scenarios

- **Cloud-Native Application Monitoring:** Organizations using OpenTelemetry for distributed tracing and metrics collection can now centralize their observability data in Azure Monitor.
- **Hybrid and Multi-Cloud Environments:** Enterprises standardizing on OpenTelemetry for telemetry collection can leverage Azure Monitor as a unified backend, even when applications run across different environments.
- **DevOps and SRE Workflows:** Teams can leverage Azure Monitor’s analytics, alerting, and visualization capabilities on telemetry data ingested via OTLP, enhancing incident detection and root cause analysis.

---

### Important Considerations and Limitations

- **Collector Configuration Required:** Proper setup of the OpenTelemetry Collector is necessary to route OTLP signals to Azure Monitor.
- **Supported Signal Types:** Only signals supported by both OpenTelemetry and Azure Monitor can be ingested; unsupported data types may be dropped.
- **Data Security and Compliance:** Ensure that telemetry data sent to Azure Monitor complies with organizational and regulatory requirements for data handling and storage.

---

### Integration with Related Azure Services

- **Azure Monitor Ecosystem:** Ingested OTLP data becomes available for use with Azure Monitor features such as Application Insights, Log Analytics, and alerting.
- **Unified Observability:** This integration allows organizations to consolidate observability data from diverse sources into Azure Monitor, leveraging its dashboards, analytics, and automation capabilities.

---

**Summary:**  
Azure Monitor now supports the native ingestion of OpenTelemetry Protocol (OTLP) signals, enabling direct telemetry data transfer from OpenTelemetry-instrumented applications and platforms via the OpenTelemetry Collector, thereby streamlining observability workflows and enhancing integration with Azure’s monitoring ecosystem.

---

### 5. Public Preview: Tool search in Microsoft Foundry toolboxes

**Published**: June 04, 2026 19:30:58 UTC
**Link**: [Public Preview: Tool search in Microsoft Foundry toolboxes](https://azure.microsoft.com/updates?id=563506)

**Update ID**: 563506
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry has introduced a tool search feature within Foundry toolboxes, now available in public preview.

- Key changes or new features  
The new tool search capability enables developers and administrators to quickly locate specific tools within large, multi-team tool catalogs. This feature addresses performance and usability challenges by allowing users to search and filter tools, rather than loading all tool definitions at once, which can be resource-intensive as toolboxes grow in size.

- Target audience affected  
This update is relevant to developers and IT professionals who use Microsoft Foundry toolboxes, particularly those managing or working with extensive tool catalogs across multiple teams.

- Important notes if any  
The tool search feature is currently in public preview, so functionality and performance may evolve based on user feedback. This enhancement is designed to improve efficiency and reduce overhead in environments with large or complex tool inventories. Users are encouraged to test the new search capabilities and provide feedback to Microsoft during the preview phase.

Data source: Using API data  
For more details, see the official update: https://azure.microsoft.com/updates?id=563506

**Details**:

**Azure Update Report: Public Preview – Tool Search in Microsoft Foundry Toolboxes**

**Background and Purpose of the Update**  
Microsoft Foundry is a platform designed to facilitate tool management and discovery within organizations, especially those with large, multi-team catalogs. As these catalogs expand, the process of sending every tool definition for each interaction becomes resource-intensive and inefficient. The introduction of tool search in Foundry toolboxes addresses this scalability challenge by enabling developers and administrators to quickly locate the appropriate tools without incurring the overhead of processing the entire catalog.

**Specific Features and Detailed Changes**  
The update introduces a dedicated tool search capability within Foundry toolboxes, now available in public preview. This feature allows users to perform targeted searches across extensive tool catalogs, streamlining the process of finding relevant tools. The search functionality is integrated directly into the toolbox interface, providing a fast and intuitive method for filtering and accessing tool definitions. This enhancement reduces the need to manually browse through large lists and eliminates the inefficiency of loading all tool definitions with every user interaction.

**Technical Mechanisms and Implementation Methods**  
The tool search feature leverages optimized indexing and query mechanisms to enable rapid retrieval of tool definitions. Instead of transmitting the entire catalog on every request, the system now processes search queries that return only the relevant tool metadata. This approach minimizes network traffic and reduces latency, especially in environments with large catalogs and multiple teams. The implementation likely involves backend improvements to catalog storage and retrieval logic, ensuring that search operations are efficient and scalable.

**Use Cases and Application Scenarios**  
- **Large Enterprises:** Organizations with hundreds or thousands of tools can use the search feature to quickly locate specific tools across multi-team catalogs, enhancing productivity and reducing time spent on manual searches.
- **Multi-Team Collaboration:** Teams working in shared environments can benefit from the search functionality to discover tools developed by other groups, fostering cross-team collaboration.
- **Tool Management:** Administrators managing tool inventories can efficiently audit, update, or retire tools by leveraging the search capability to filter and access tool definitions based on criteria such as name, category, or metadata.

**Important Considerations and Limitations**  
- **Public Preview Status:** The tool search feature is currently in public preview, meaning it may not be fully production-ready. Users should be aware of potential limitations in functionality, performance, or reliability.
- **Catalog Size and Complexity:** While the search feature is designed to improve performance in large catalogs, organizations should monitor its effectiveness and report any issues encountered during the preview phase.
- **Security and Access Control:** The update does not specify changes to access control mechanisms. Users should ensure that tool search operations comply with existing security policies and permissions.

**Integration with Related Azure Services**  
The tool search capability is integrated within Microsoft Foundry toolboxes and is intended to enhance the user experience for developers and administrators working with Azure-based tool catalogs. While the update does not detail direct integration with other Azure services, it is likely to complement Azure DevOps, Azure Resource Manager, and other catalog-driven workflows by improving tool discovery and management.

**Summary Sentence**  
Microsoft Foundry’s public preview of tool search in toolboxes provides developers and administrators with a fast, efficient way to locate tools within large, multi-team catalogs, reducing resource overhead and improving productivity.

---

### 6. Public Preview: APIM Support for Foundry Models in Azure AI Search

**Published**: June 04, 2026 19:30:58 UTC
**Link**: [Public Preview: APIM Support for Foundry Models in Azure AI Search](https://azure.microsoft.com/updates?id=563451)

**Update ID**: 563451
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure API Management (APIM) now supports Foundry model integrations in Azure AI Search, available in public preview.

- Key changes or new features  
  - Enterprises can now manage, secure, and monitor Foundry and Azure OpenAI model endpoints through APIM.  
  - This enables seamless integration of large language models (LLMs) into Retrieval-Augmented Generation (RAG) pipelines at scale.  
  - APIM provides centralized control, policy enforcement, and analytics for Foundry model APIs in Azure AI Search.

- Target audience affected  
  - Enterprise platform engineers  
  - AI solution teams  
  - Developers and IT professionals building or maintaining large-scale RAG pipelines using Azure AI Search and Foundry models

- Important notes if any  
  - This feature is currently in public preview and may not be suitable for production workloads.  
  - Integration with APIM simplifies governance and security for AI model endpoints, streamlining deployment and management.  
  - Developers can use standard APIM features (e.g., authentication, throttling, logging) with Foundry model APIs.  
  - Review the official documentation for limitations and onboarding steps during the preview phase.

Data source: Using API data  
[Azure Update link](https://azure.microsoft.com/updates?id=563451)

**Details**:

**Azure Update Report**

**Title:** Public Preview: APIM Support for Foundry Models in Azure AI Search  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563451)

---

**Background and Purpose of the Update:**  
Microsoft Foundry is a platform that facilitates advanced AI model integrations. This update introduces Azure API Management (APIM) support for all Foundry model integrations within Azure AI Search, now available in public preview. The primary purpose is to enable enterprise platform engineers and AI solution teams to efficiently manage and expose Foundry and Azure OpenAI model endpoints, particularly in large-scale Retrieval-Augmented Generation (RAG) pipelines.

**Specific Features and Detailed Changes:**  
- **APIM Integration:** Foundry models integrated with Azure AI Search can now be managed and exposed via Azure API Management. This allows for secure, scalable, and governed access to AI model endpoints.
- **Expanded Model Support:** The update extends APIM support to all Foundry models, not limited to Azure OpenAI models, providing broader flexibility for AI solution architects.
- **Public Preview Availability:** The feature is currently in public preview, allowing early access and feedback from enterprise users.

**Technical Mechanisms and Implementation Methods:**  
- **API Management Layer:** APIM acts as a proxy between client applications and Foundry model endpoints, enabling centralized management of authentication, authorization, throttling, and monitoring.
- **Integration Workflow:** Platform engineers can register Foundry model endpoints within APIM, configure policies (such as rate limiting or IP filtering), and publish APIs for consumption by internal or external applications.
- **Azure AI Search Compatibility:** The integration is specifically designed for scenarios where Foundry models are used as part of Azure AI Search workflows, ensuring seamless interoperability and endpoint exposure.

**Use Cases and Application Scenarios:**  
- **Enterprise RAG Pipelines:** Teams running large-scale Retrieval-Augmented Generation pipelines can leverage APIM to securely expose Foundry and Azure OpenAI endpoints, facilitating controlled access and monitoring.
- **AI Solution Management:** Organizations deploying multiple AI models can use APIM to standardize endpoint management, enforce security policies, and enable analytics across all Foundry model integrations.
- **Platform Engineering:** Engineers can streamline the deployment and governance of AI-powered search solutions by integrating APIM with Foundry models, reducing operational complexity.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should evaluate stability and support before full-scale deployment.
- **Supported Models:** The update applies to all Foundry models integrated with Azure AI Search. Compatibility with other AI services or custom models is not specified.
- **APIM Configuration:** Proper configuration of APIM policies and security settings is essential to ensure compliance and prevent unauthorized access.

**Integration with Related Azure Services:**  
- **Azure API Management:** Provides centralized API governance, security, and monitoring for Foundry model endpoints.
- **Azure AI Search:** Acts as the primary context for Foundry model integration, enabling advanced search and AI capabilities.
- **Azure OpenAI:** Foundry and Azure OpenAI models can be jointly managed and exposed via APIM, supporting hybrid AI solution architectures.

---

**Summary Sentence:**  
This public preview update enables Azure API Management support for all Foundry model integrations in Azure AI Search, allowing enterprise teams to securely manage and expose AI model endpoints for large-scale RAG pipelines and advanced search solutions.

---

### 7. Public Preview: Azure SQL as a knowledge source in Foundry IQ

**Published**: June 04, 2026 19:30:58 UTC
**Link**: [Public Preview: Azure SQL as a knowledge source in Foundry IQ](https://azure.microsoft.com/updates?id=563446)

**Update ID**: 563446
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure SQL Database is now available as a first-class Knowledge Source in Azure AI Search within Microsoft Foundry, currently in public preview.

- Key changes or new features  
Developers and solution architects can now directly connect Azure SQL Database tables to Azure AI Search for use in Copilot, Retrieval-Augmented Generation (RAG), and agentic AI solutions. This integration allows for seamless exposure of authoritative enterprise data, improving the accuracy and relevance of AI-driven applications. The update simplifies connecting structured SQL data to AI search and knowledge management workflows.

- Target audience affected  
Enterprise developers, solution architects, and IT professionals building AI-powered applications (such as Copilot, RAG, and agentic experiences) who utilize Azure SQL Database and Azure AI Search.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. Users should monitor for updates regarding general availability and review documentation for any limitations or configuration requirements during the preview phase.

Link: [Azure Update Details](https://azure.microsoft.com/updates?id=563446)

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure SQL as a knowledge source in Foundry IQ  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563446)

---

**Background and Purpose of the Update**

Microsoft Foundry has introduced Azure SQL Database as a first-class Knowledge Source within Azure AI Search, now available in public preview. The primary purpose of this update is to enable enterprise developers and solution architects to leverage authoritative data stored in Azure SQL Database for advanced AI-driven solutions, such as Copilot, Retrieval-Augmented Generation (RAG), and agentic experiences. This integration addresses the need for seamless access to structured enterprise data for generative AI and search applications.

---

**Specific Features and Detailed Changes**

- **Azure SQL Database Integration:** Azure SQL Database is now recognized as a first-class Knowledge Source in Azure AI Search, allowing direct exposure of tables for search and AI scenarios.
- **Public Preview Availability:** The feature is currently in public preview, enabling early access for developers to test and provide feedback.
- **Authoritative Table Exposure:** Developers can expose specific tables from Azure SQL Database, ensuring that AI applications utilize reliable, structured data.

---

**Technical Mechanisms and Implementation Methods**

- **Knowledge Source Configuration:** Azure SQL Database can be configured as a Knowledge Source within Foundry IQ, which is part of Azure AI Search. This setup allows the search service to index and retrieve data directly from SQL tables.
- **Data Access and Indexing:** The mechanism involves connecting to Azure SQL Database, selecting relevant tables, and enabling them for search and AI consumption. The indexing process ensures that data remains synchronized and up-to-date for query and retrieval operations.
- **Integration with Copilot and RAG:** By exposing SQL tables as knowledge sources, developers can build solutions where Copilot or RAG models retrieve contextually relevant data from SQL databases, enhancing the accuracy and reliability of AI-generated responses.

---

**Use Cases and Application Scenarios**

- **Copilot Experiences:** Integrate Azure SQL Database as a backend for Copilot solutions, enabling natural language queries against enterprise data.
- **Retrieval-Augmented Generation (RAG):** Use SQL tables as authoritative sources for RAG workflows, improving the factual grounding of generative AI outputs.
- **Agentic Applications:** Build agent-based systems that require access to structured data for decision-making, reporting, or workflow automation.
- **Enterprise Search:** Implement enterprise search solutions that index and retrieve data from Azure SQL Database, supporting business intelligence and analytics.

---

**Important Considerations and Limitations**

- **Preview Status:** As the feature is in public preview, it may not be suitable for production workloads. Users should monitor for updates and provide feedback during the preview phase.
- **Data Security and Access Control:** Proper configuration of access permissions and security policies is essential when exposing SQL tables as knowledge sources.
- **Supported Table Types and Query Complexity:** Only specific table types or query patterns may be supported during the preview; users should consult documentation for compatibility details.
- **Performance and Scalability:** Preview features may have limitations regarding performance and scalability, which should be evaluated in test environments.

---

**Integration with Related Azure Services**

- **Azure AI Search:** The integration is directly with Azure AI Search, leveraging its indexing and retrieval capabilities.
- **Foundry IQ:** Foundry IQ acts as the orchestration layer, managing knowledge sources and facilitating AI-driven search experiences.
- **Azure SQL Database:** The update enhances Azure SQL Database’s role in AI and search scenarios, making it a foundational data provider for Copilot and RAG solutions.

---

**Summary Sentence:**  
Azure SQL Database is now available as a first-class Knowledge Source in Azure AI Search via Foundry IQ public preview, enabling enterprise developers to expose authoritative tables for advanced Copilot, RAG, and agentic AI experiences.

---

### 8. Generally Available: Microsoft Discovery

**Published**: June 04, 2026 19:30:58 UTC
**Link**: [Generally Available: Microsoft Discovery](https://azure.microsoft.com/updates?id=562733)

**Update ID**: 562733
**Data source**: Azure Updates API

**Categories**: Launched, Microsoft Build

**Summary**:

- What was updated  
Microsoft Discovery is now generally available.

- Key changes or new features  
Microsoft Discovery offers an enterprise platform for building, managing, and governing agentic AI workflows, specifically designed for research and development (R&D) organizations. The platform supports scientific and engineering disciplines, enabling teams to accelerate innovation using AI-powered agents. Additionally, a new feature is available in preview (details truncated in the source).

- Target audience affected  
This update is relevant to developers, data scientists, and IT professionals working in R&D, particularly within scientific and engineering domains. Organizations seeking to leverage AI for workflow automation and governance will benefit most.

- Important notes if any  
Microsoft Discovery provides enterprise-grade governance, security, and compliance capabilities for AI workflows. IT professionals should review integration options with existing Azure services and ensure alignment with organizational security policies. Developers can use the platform to streamline the development and deployment of agentic AI solutions. The preview feature mentioned may offer additional capabilities—monitor the official update page for further details.

**Details**:

**Comprehensive Technical Explanation of "Generally Available: Microsoft Discovery"**

**Background and Purpose of the Update**  
Microsoft Discovery has reached general availability, marking its readiness for production use by research and development organizations. The primary purpose of this platform is to provide an enterprise-grade solution for constructing and managing agentic AI workflows, specifically tailored for scientific and engineering disciplines. This addresses the growing need for robust governance and streamlined workflow orchestration in environments where AI-driven agents are increasingly used to automate and accelerate research processes.

**Specific Features and Detailed Changes**  
With this update, Microsoft Discovery delivers a platform designed for enterprise-scale workflow management. Key features include:  
- **Agentic AI Workflow Construction:** Enables organizations to build complex AI workflows involving multiple autonomous agents that can collaborate or operate independently within scientific and engineering tasks.  
- **Governance Capabilities:** Provides tools and controls for governing the lifecycle of AI workflows, ensuring compliance, traceability, and reproducibility of research activities.  
- **Cross-Disciplinary Support:** The platform is optimized for a wide range of scientific and engineering domains, facilitating interdisciplinary collaboration and workflow standardization.  
- **Enterprise Integration:** Designed to meet the scalability, security, and reliability requirements of large organizations.

**Technical Mechanisms and Implementation Methods**  
Microsoft Discovery leverages Azure’s cloud infrastructure to deliver its platform as a service. Technical mechanisms include:  
- **Workflow Orchestration:** Utilizes Azure-native orchestration tools to manage the execution, scheduling, and monitoring of agentic AI workflows.  
- **Agent Management:** Provides APIs and interfaces for registering, configuring, and deploying AI agents within workflows.  
- **Governance Framework:** Implements policy-driven governance, including audit trails, access controls, and workflow versioning, to ensure compliance and reproducibility.  
- **Data Integration:** Supports integration with Azure data services for seamless access to scientific datasets and engineering data repositories.

**Use Cases and Application Scenarios**  
Microsoft Discovery is applicable in scenarios such as:  
- **Automated Scientific Research:** Deploying AI agents to automate data analysis, hypothesis generation, and experiment management in laboratory environments.  
- **Engineering Workflow Automation:** Orchestrating multi-agent workflows for simulation, modeling, and optimization tasks in engineering projects.  
- **Collaborative Research Projects:** Enabling teams across disciplines to build, share, and govern AI-driven workflows for joint research initiatives.

**Important Considerations and Limitations**  
Technical professionals should consider the following:  
- **Compliance and Security:** Ensuring that workflow governance aligns with organizational and regulatory requirements.  
- **Workflow Complexity:** The platform is designed for complex, agentic workflows; simpler workflows may not fully leverage its capabilities.  
- **Integration Requirements:** Users must ensure compatibility with existing Azure services and data sources for optimal workflow performance.

**Integration with Related Azure Services**  
Microsoft Discovery integrates with various Azure services, including:  
- **Azure Data Services:** For data storage, retrieval, and processing within AI workflows.  
- **Azure AI and Machine Learning:** For leveraging pre-built AI models and training custom agents.  
- **Azure Governance Tools:** For policy management, access control, and auditing.

**Summary Sentence**  
Microsoft Discovery is now generally available, offering research and development organizations an enterprise platform for building and governing agentic AI workflows across scientific and engineering disciplines.

---

### 9. Generally Available: Private Connectivity for Azure AI Search and Foundry Knowledge Bases

**Published**: June 04, 2026 19:15:11 UTC
**Link**: [Generally Available: Private Connectivity for Azure AI Search and Foundry Knowledge Bases](https://azure.microsoft.com/updates?id=563516)

**Update ID**: 563516
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Private, end-to-end network connectivity is now generally available for Azure AI Search and Foundry Knowledge Bases.

- Key changes or new features  
Azure AI Search and Foundry Knowledge Bases now support private connectivity options, allowing all data traffic—including ingestion, enrichment, retrieval, and agent operations—to be routed securely over Shared Private Link or Network Security Groups (NSGs). This enhancement ensures that communication between Azure AI Search resources and Foundry services remains within the Azure backbone network, eliminating exposure to the public internet.

- Target audience affected  
Developers and IT professionals managing Azure AI Search, Foundry Knowledge Bases, or building AI-powered applications that require secure data flows and compliance with strict network security policies.

- Important notes if any  
To leverage private connectivity, configuration of Shared Private Link or NSGs is required. This update helps organizations meet regulatory and security requirements by preventing data from traversing the public internet. Review your current network architecture and update configurations to take advantage of these new private connectivity options.  
More details: [Azure Update Link](https://azure.microsoft.com/updates?id=563516)

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update**  
This update makes private, end-to-end network connectivity generally available for Azure AI Search and Foundry Knowledge Bases. The primary goal is to enhance security and compliance by enabling customers to route all traffic—including ingestion, enrichment, retrieval, and agent communications—over private network paths, rather than exposing resources to the public internet.

**Specific Features and Detailed Changes**  
- **Private Connectivity Support:** Azure AI Search and Foundry Knowledge Bases now support private connectivity using Shared Private Link or Network Security mechanisms.
- **Traffic Routing:** All operational traffic (ingestion, enrichment, retrieval, and agent traffic) between search resources and Foundry services can be routed securely over these private connections.
- **General Availability:** These features are now generally available, indicating full production support and SLA coverage.

**Technical Mechanisms and Implementation Methods**  
- **Shared Private Link:** This mechanism allows Azure resources to communicate privately over the Azure backbone network. Shared Private Link provides a secure, scalable way to connect services without traversing the public internet.
- **Network Security:** While not detailed, this likely refers to the use of network security controls such as Network Security Groups (NSGs) and firewalls to further restrict and monitor traffic between resources.
- **End-to-End Security:** By leveraging these mechanisms, all data flows between Azure AI Search and Foundry Knowledge Bases remain within the trusted Azure network, reducing exposure to external threats.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in finance, healthcare, or government sectors can use these features to comply with strict data privacy and residency requirements.
- **Enterprise Security:** Enterprises with stringent security policies can ensure that sensitive search and knowledge base operations are not exposed to the public internet.
- **Hybrid Architectures:** Customers integrating on-premises networks with Azure can maintain private connectivity for AI-powered search and knowledge base solutions.

**Important Considerations and Limitations**  
- **Configuration Required:** Customers must configure Shared Private Link or appropriate network security settings to enable private connectivity.
- **Service Dependencies:** Only traffic between Azure AI Search and Foundry Knowledge Bases is covered; other integrations or external access may require additional configuration.
- **No Public Access:** Once private connectivity is enabled, public access to these resources may be restricted or disabled, impacting existing workflows that rely on public endpoints.

**Integration with Related Azure Services**  
- **Azure Virtual Network (VNet):** Shared Private Link integrates with Azure VNets, allowing seamless extension of private connectivity to other Azure services.
- **Network Security Groups (NSGs):** NSGs can be used to define granular access controls for traffic between search and knowledge base resources.
- **Azure Monitor and Security Center:** These services can be leveraged to monitor and audit traffic patterns, ensuring compliance and detecting anomalies.

**Summary Sentence:**  
Private, end-to-end network connectivity for Azure AI Search and Foundry Knowledge Bases is now generally available, enabling secure routing of all operational traffic over Shared Private Link or network security mechanisms for enhanced security and compliance.

---

### 10. Public Preview: Fabric IQ Ontology Knowledge Source in Microsoft Foundry IQ

**Published**: June 04, 2026 19:15:11 UTC
**Link**: [Public Preview: Fabric IQ Ontology Knowledge Source in Microsoft Foundry IQ](https://azure.microsoft.com/updates?id=563416)

**Update ID**: 563416
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry IQ now supports Microsoft Fabric Ontology as a federated knowledge source in public preview.

- Key changes or new features  
  - Foundry IQ agents can query the semantic layer curated in Microsoft Fabric using natural language.  
  - Natural language questions are translated into ontology queries, enabling seamless access to structured business data.  
  - This integration allows leveraging existing ontologies in Fabric without additional data modeling or duplication.

- Target audience affected  
  - Developers building AI-powered applications or agents that interact with enterprise data in Microsoft Fabric.  
  - IT professionals managing data governance, semantic models, and knowledge sources within Fabric environments.

- Important notes if any  
  - This feature is in public preview and may not be suitable for production workloads.  
  - It streamlines access to curated business knowledge, reducing the need for custom connectors or manual query translation.  
  - Integration with Fabric Ontology can improve consistency and accuracy of AI-driven insights by referencing a single source of truth.  
  - Review documentation for supported query types and limitations during preview.

[More details](https://azure.microsoft.com/updates?id=563416)

**Details**:

**Background and Purpose of the Update**  
This update introduces the public preview of the Fabric IQ Ontology Knowledge Source within Microsoft Foundry IQ. The primary goal is to enable Foundry IQ agents to treat a Microsoft Fabric Ontology as a federated knowledge source. This allows organizations to leverage the semantic layer they have curated in Microsoft Fabric, making it accessible for querying and knowledge extraction through Foundry IQ.

**Specific Features and Detailed Changes**  
- **Federated Knowledge Source Integration:** Microsoft Fabric Ontology can now be registered and used as a federated knowledge source within Foundry IQ.
- **Natural Language Querying:** Foundry IQ agents are capable of translating natural language questions into ontology-based queries, allowing users to interact with the semantic model using plain language.
- **Public Preview Availability:** This feature is currently in public preview, enabling early access and feedback from customers.

**Technical Mechanisms and Implementation Methods**  
- **Ontology as a Knowledge Source:** The update allows Foundry IQ to connect to a Microsoft Fabric Ontology, which is a semantic model curated by the customer within Microsoft Fabric.
- **Query Translation:** When a user submits a natural language question, Foundry IQ translates this input into queries that target the semantic definitions and relationships specified in the Fabric Ontology.
- **Federation Architecture:** The integration is implemented as a federated knowledge source, meaning that the ontology is treated as one of potentially multiple sources that Foundry IQ can query, aggregate, and reason over.

**Use Cases and Application Scenarios**  
- **Enterprise Knowledge Management:** Organizations can use this feature to expose curated business ontologies to agents and users, enabling semantic search and discovery across enterprise data.
- **Data Analytics and Reporting:** Data analysts and business users can ask natural language questions about business metrics, definitions, and relationships, with Foundry IQ retrieving answers directly from the Fabric Ontology.
- **AI-Driven Automation:** Agents can leverage the ontology to automate processes that require understanding of business concepts and relationships defined in the semantic layer.

**Important Considerations and Limitations**  
- **Public Preview Status:** As the feature is in public preview, it may not be suitable for production workloads and could be subject to change.
- **Ontology Curation Required:** Customers must have an existing, curated Microsoft Fabric Ontology to utilize this capability effectively.
- **Scope of Natural Language Understanding:** The accuracy of query translation depends on the quality and completeness of the underlying ontology and the natural language processing capabilities of Foundry IQ.

**Integration with Related Azure Services**  
- **Microsoft Fabric:** The update directly integrates with Microsoft Fabric, leveraging its semantic layer as a knowledge source.
- **Foundry IQ:** The feature is part of Microsoft Foundry IQ, enhancing its ability to federate knowledge from multiple sources, including ontologies.
- **Potential for Broader Azure Ecosystem Integration:** While not explicitly stated, this integration lays the groundwork for connecting semantic models in Fabric with other Azure AI and data services through Foundry IQ’s federated architecture.

**Summary Sentence**  
Microsoft Foundry IQ now supports Microsoft Fabric Ontology as a federated knowledge source in public preview, enabling agents to translate natural language queries into ontology-based queries and leverage curated semantic models within the Fabric environment.

---

### 11. Generally Available: Microsoft Foundry IQ

**Published**: June 04, 2026 19:15:11 UTC
**Link**: [Generally Available: Microsoft Foundry IQ](https://azure.microsoft.com/updates?id=563222)

**Update ID**: 563222
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Microsoft Foundry IQ is now generally available.

- Key changes or new features  
Foundry IQ provides a managed knowledge layer that enables developers to ground AI agents and applications in enterprise data without the need to rebuild retrieval pipelines for each project. It supports seamless integration with data sources such as SharePoint, OneLake, Azure Blob Storage, and others. This service streamlines the process of connecting and managing enterprise data for AI and automation use cases.

- Target audience affected  
Developers and IT professionals building AI-powered applications, chatbots, or automation solutions that require access to enterprise data across multiple sources.

- Important notes if any  
Foundry IQ simplifies the process of connecting agents and applications to enterprise data, reducing development time and operational overhead. Teams can leverage existing data sources without duplicating integration efforts for each project. This update is particularly relevant for organizations standardizing AI solutions across multiple business units or projects.

**Details**:

**Comprehensive Technical Explanation: Microsoft Foundry IQ General Availability**

**Background and Purpose of the Update:**  
Microsoft Foundry IQ has reached general availability, marking its transition from preview to a fully supported Azure service. The primary purpose of Foundry IQ is to provide developers with a managed knowledge layer that enables intelligent agents to access and utilize enterprise data efficiently. This eliminates the need for teams to rebuild data retrieval pipelines for each new project, streamlining development and reducing redundant engineering efforts.

**Specific Features and Detailed Changes:**  
With this release, Foundry IQ offers a managed environment where developers can connect various enterprise data sources, such as SharePoint, OneLake, and Azure Blob Storage. The service abstracts the complexities of data retrieval, allowing agents to be "grounded" in up-to-date organizational knowledge without custom integration work for each data source or project. The general availability status means the service is now production-ready, with support and SLAs in place.

**Technical Mechanisms and Implementation Methods:**  
Foundry IQ operates as a managed knowledge layer. Technically, it connects to supported data sources (e.g., SharePoint, OneLake, Azure Blob) and provides a unified interface for intelligent agents or applications to query and retrieve relevant information. This managed layer handles the ingestion, indexing, and retrieval of enterprise data, ensuring that agents are always referencing the latest and most authoritative information. Developers interact with Foundry IQ through standardized APIs, minimizing the need for custom data connectors or retrieval logic.

**Use Cases and Application Scenarios:**  
- **Enterprise Chatbots and Virtual Agents:** Developers can quickly ground chatbots in enterprise knowledge bases without building custom retrieval pipelines for each data source.
- **Knowledge Management Applications:** Teams can aggregate data from multiple sources (SharePoint, OneLake, Azure Blob) into a single knowledge layer, improving search and discovery capabilities.
- **AI-Powered Automation:** Intelligent agents can access and reason over enterprise data for workflow automation, compliance checks, or business process optimization.

**Important Considerations and Limitations:**  
- **Supported Data Sources:** At general availability, Foundry IQ supports SharePoint, OneLake, Azure Blob, and potentially other sources as specified in the service documentation.
- **Data Security and Compliance:** As with any managed service handling enterprise data, IT professionals should review Foundry IQ’s security, compliance, and access control mechanisms to ensure alignment with organizational policies.
- **Migration and Integration:** Existing projects with custom retrieval pipelines may require refactoring to leverage the managed knowledge layer and maximize the benefits of Foundry IQ.

**Integration with Related Azure Services:**  
Foundry IQ is designed to integrate seamlessly with other Azure data services, particularly those used for storage and collaboration (e.g., SharePoint, OneLake, Azure Blob). It can be used in conjunction with Azure AI services, such as Azure OpenAI Service or Azure Cognitive Search, to enhance the capabilities of intelligent agents and applications. The managed nature of Foundry IQ simplifies integration, allowing developers to focus on building solutions rather than managing data pipelines.

**Summary:**  
Microsoft Foundry IQ is now generally available, providing a managed knowledge layer that enables developers to ground intelligent agents in enterprise data from sources like SharePoint, OneLake, and Azure Blob, streamlining data retrieval and integration across projects.

---

### 12. Public Preview: Content Understanding chunking and image verbalization in Azure AI Search

**Published**: June 04, 2026 19:00:34 UTC
**Link**: [Public Preview: Content Understanding chunking and image verbalization in Azure AI Search](https://azure.microsoft.com/updates?id=563661)

**Update ID**: 563661
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Microsoft Foundry, Microsoft Build, Feature

**Summary**:

- What was updated  
Azure AI Search has introduced Content Understanding chunking and image verbalization features in public preview, enhancing its built-in skillset for parsing rich documents during indexing.

- Key changes or new features  
  - **Content Understanding Chunking:** Indexers can now split documents into semantically meaningful chunks, improving the granularity and relevance of search results.
  - **Image Verbalization:** The service can generate textual descriptions for images embedded in documents, making visual content searchable and accessible.
  - Both features are available as part of the Content Understanding skillset during the indexing process.

- Target audience affected  
  - Developers integrating Azure AI Search for document and knowledge management solutions.
  - IT professionals managing enterprise search and content indexing pipelines.
  - Teams working with unstructured or multimedia-rich content who require improved search accuracy and accessibility.

- Important notes  
  - These features are in public preview and may be subject to changes before general availability.
  - API integration is required to leverage these capabilities within indexing pipelines.
  - Image verbalization can enhance accessibility and compliance by providing alt-text for images.
  - Review documentation for limitations and best practices during the preview phase.

[More details](https://azure.microsoft.com/updates?id=563661)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Content Understanding Chunking and Image Verbalization in Azure AI Search  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=563661)

---

### 1. Background and Purpose of the Update

Azure AI Search is continually evolving to enhance the discoverability and usability of content within enterprise search solutions. The introduction of Content Understanding chunking and image verbalization in public preview addresses the need for more granular and semantically rich indexing of complex documents. This update aims to improve search relevance and accessibility by enabling the extraction of meaningful text segments and generating descriptive text from images during the indexing process.

---

### 2. Specific Features and Detailed Changes

- **Content Understanding Chunking:**  
  The built-in skill for document parsing can now segment documents into semantically meaningful "chunks" during indexing. Instead of treating an entire document as a single block, the indexer identifies logical sections or topics, allowing for more precise retrieval and contextual understanding in search results.

- **Image Verbalization:**  
  The skillset now includes the ability to generate textual descriptions (verbalizations) of images embedded within documents. This feature enhances the search index by making visual content discoverable through text-based queries, supporting scenarios where image content is relevant to search intent.

---

### 3. Technical Mechanisms and Implementation Methods

- **Indexers and Built-in Skills:**  
  The update leverages Azure AI Search indexers, which orchestrate the extraction and transformation of content from data sources. The enhanced built-in skill applies advanced content understanding models to:
    - Automatically detect semantic boundaries within documents for chunking.
    - Analyze images and generate descriptive text using AI-powered image captioning models.

- **Index Schema Impact:**  
  The output of chunking and image verbalization is incorporated into the search index as additional fields or enriched content, enabling more granular filtering, highlighting, and relevance ranking.

- **Integration with Enrichment Pipelines:**  
  These features are integrated into the cognitive enrichment pipeline, allowing seamless combination with other AI skills (e.g., entity recognition, key phrase extraction) during the indexing process.

---

### 4. Use Cases and Application Scenarios

- **Enterprise Knowledge Management:**  
  Organizations can improve searchability of large, complex documents (e.g., technical manuals, legal contracts) by indexing semantically meaningful sections, enabling users to find relevant information more efficiently.

- **Accessibility Enhancement:**  
  Image verbalization supports accessibility by providing text alternatives for images, benefiting users with visual impairments and improving compliance with accessibility standards.

- **Content Discovery in Multimedia Archives:**  
  Archives containing mixed text and images (e.g., research papers, news articles) become more searchable, as both textual and visual content are represented in the index.

---

### 5. Important Considerations and Limitations

- **Public Preview Status:**  
  As this feature is in public preview, it may not be suitable for production workloads. Users should monitor for updates regarding general availability and be aware of potential changes in API behavior or feature set.

- **Performance and Cost:**  
  Additional processing for chunking and image analysis may impact indexing performance and incur additional cognitive services costs.

- **Data Privacy:**  
  Ensure that the processing of document content and images complies with organizational data privacy and compliance requirements.

---

### 6. Integration with Related Azure Services

- **Azure Cognitive Services:**  
  The image verbalization capability relies on underlying Azure Cognitive Services for image analysis and captioning.

- **Azure Data Sources:**  
  The enrichment pipeline can be applied to content ingested from various Azure data sources, such as Azure Blob Storage, Azure SQL Database, or Cosmos DB.

- **Custom Skillsets:**  
  These new features can be combined with custom skills to further tailor the enrichment and indexing process to specific business needs.

---

**Summary:**  
Azure AI Search now offers public preview support for Content Understanding chunking

---

### 13. Generally Available: Azure Monitor Service Level Indicators (SLI)

**Published**: June 04, 2026 16:30:52 UTC
**Link**: [Generally Available: Azure Monitor Service Level Indicators (SLI)](https://azure.microsoft.com/updates?id=565159)

**Update ID**: 565159
**Data source**: Azure Updates API

**Categories**: Launched, DevOps, Management and governance, Azure Monitor, Features, Management, Microsoft Build, Services, Feature

**Summary**:

- What was updated  
Azure Monitor now offers generally available support for Service Level Indicators (SLIs) and Service Level Objectives (SLOs).

- Key changes or new features  
  - Teams can define and track SLIs and SLOs directly in Azure Monitor, enabling measurement of application reliability and user experience based on real customer impact rather than only infrastructure metrics (e.g., CPU, memory).
  - SLIs can be based on custom metrics, logs, or standard Azure Monitor signals.
  - SLOs can be set and monitored to ensure compliance with business or operational targets.
  - Built-in dashboards and alerting help teams visualize and respond to SLO breaches.

- Target audience affected  
  - Developers and DevOps teams responsible for application reliability and performance.
  - IT professionals managing service health and operational SLAs.

- Important notes if any  
  - This feature enables more meaningful monitoring aligned with end-user experience, supporting Site Reliability Engineering (SRE) practices.
  - Integration with Azure Monitor’s alerting and visualization tools streamlines incident response and reporting.
  - Teams can now shift from infrastructure-centric to customer-centric reliability metrics, improving service quality and accountability.

For more details, see the official update: https://azure.microsoft.com/updates?id=565159

**Details**:

**Azure Update Report: Generally Available – Azure Monitor Service Level Indicators (SLI)**

**Background and Purpose of the Update**  
Azure Monitor’s latest update introduces Service Level Indicators (SLIs) and Service Level Objectives (SLOs) as generally available features. The primary goal of this enhancement is to provide IT teams and application owners with more precise, customer-centric metrics for measuring application performance and reliability. Traditionally, monitoring has focused on infrastructure-level signals such as CPU utilization or isolated metrics, which may not accurately reflect the end-user experience. By incorporating SLIs and SLOs, Azure Monitor enables organizations to align their monitoring practices with the actual service quality perceived by customers.

**Specific Features and Detailed Changes**  
- **Service Level Indicators (SLIs):** SLIs are quantitative measures that reflect specific aspects of service performance, such as request latency, error rates, or availability. With this update, Azure Monitor allows users to define and track SLIs that are most relevant to their application's customer experience.
- **Service Level Objectives (SLOs):** SLOs represent the target values or thresholds for SLIs, defining the acceptable level of service quality. Teams can now set, monitor, and report against these objectives within Azure Monitor.
- **Enhanced Reporting:** The update provides built-in capabilities to visualize, report, and alert on SLI and SLO metrics, enabling proactive management of service health.

**Technical Mechanisms and Implementation Methods**  
Azure Monitor’s SLI/SLO functionality is integrated into its existing telemetry and analytics pipeline. Users can define SLIs based on telemetry data collected from applications, such as HTTP request success rates or response times. These definitions are configurable through the Azure Portal or via ARM templates and APIs, allowing for automation and integration into CI/CD workflows. SLOs are then set as target thresholds for these SLIs, and Azure Monitor continuously evaluates real-time data against these objectives. The platform supports alerting and dashboarding based on SLO compliance, facilitating rapid incident response and root cause analysis.

**Use Cases and Application Scenarios**  
- **Customer Experience Monitoring:** Organizations can measure how actual users experience their applications, going beyond infrastructure health to focus on service reliability and responsiveness.
- **SLA Compliance Tracking:** Teams can use SLOs to ensure their services meet contractual or internal service level agreements, with automated reporting and alerting on breaches.
- **DevOps and SRE Practices:** The SLI/SLO model supports Site Reliability Engineering (SRE) methodologies, enabling error budgeting and data-driven operational decisions.
- **Incident Management:** Real-time SLO monitoring helps prioritize incidents based on customer impact, improving mean time to resolution (MTTR).

**Important Considerations and Limitations**  
- **Scope of Metrics:** SLIs are only as meaningful as the underlying telemetry. Accurate and comprehensive instrumentation of applications is required to fully leverage these features.
- **Configuration Complexity:** Defining appropriate SLIs and SLOs requires a clear understanding of application behavior and customer expectations.
- **Resource Consumption:** Additional telemetry and analytics may increase data ingestion and storage costs within Azure Monitor.

**Integration with Related Azure Services**  
Azure Monitor’s SLI/SLO capabilities integrate seamlessly with other Azure services:
- **Azure Application Insights:** Provides the underlying telemetry for defining application-level SLIs.
- **Azure Alerts:** Enables automated notifications based on SLO breaches.
- **Azure Dashboards and Workbooks:** Supports visualization and reporting of SLI/SLO metrics for stakeholders.
- **Azure Resource Manager (ARM):** Allows for programmatic management and deployment of SLI/SLO configurations.

**Summary Sentence:**  
Azure Monitor’s general availability of Service Level Indicators and Objectives empowers technical teams to define, monitor, and report on customer-centric service quality metrics, enabling more effective management of application reliability and user experience within the Azure ecosystem.

---


*This report was automatically generated - 2026-06-05 03:06:38 UTC*