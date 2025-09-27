# September 27, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 27, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Azure VMware Solution AV36 Node Retirement on June 30, 2028

**Published**: September 27, 2025 00:30:39 UTC
**Link**: [Azure VMware Solution AV36 Node Retirement on June 30, 2028](https://azure.microsoft.com/updates?id=503883)

**Update ID**: 503883
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the Azure VMware Solution (AVS) AV36 node type, effective June 30, 2028.

- Key changes or new features  
The AV36 node type will no longer be available after the retirement date. Existing AV36 Reserved Instances (RIs) remain valid and unaffected until their expiration. No new AV36 nodes can be provisioned post-retirement.

- Target audience affected  
Developers and IT professionals currently using or planning to use AV36 node types in Azure VMware Solution. Particularly those managing capacity planning, reserved instances, and workload migrations on AV36 nodes.

- Important notes if any  
Customers are advised to review their AV36 RI expiration timelines to align with the retirement date and plan migrations or upgrades to supported node types accordingly. Early planning will help avoid service disruptions and ensure continuity of VMware workloads on Azure.  
For more details, visit the official update page: https://azure.microsoft.com/updates?id=503883

**Details**:

The Azure VMware Solution (AVS) update announces the planned retirement of the AV36 node type effective June 30, 2028. This advance notice allows IT professionals and Azure VMware Solution customers to strategically plan their infrastructure lifecycle and capacity management within AVS environments.

**Background and Purpose:**  
The AV36 node type is a specific hardware configuration within Azure VMware Solution, designed to deliver dedicated VMware compute resources on Azure infrastructure. Over time, Microsoft evolves its hardware offerings to incorporate newer technologies, improve performance, and optimize cost-efficiency. The retirement of AV36 nodes aligns with this lifecycle management, ensuring that customers transition to more current node types with enhanced capabilities. This update serves to inform customers well in advance, enabling them to review their Reserved Instances (RIs) and plan migrations or upgrades accordingly.

**Specific Features and Detailed Changes:**  
The key change is the formal deprecation and retirement date for AV36 nodes, set for June 30, 2028. Importantly, existing AV36 Reserved Instances remain valid until their expiration and are not immediately impacted by this announcement. However, no new AV36 nodes will be provisioned after this date, and customers will need to migrate workloads to supported node types before retirement. This update does not introduce new features but rather communicates the end-of-life timeline for AV36 hardware within AVS.

**Technical Mechanisms and Implementation Methods:**  
From a technical standpoint, the AV36 node retirement involves the phased decommissioning of the underlying physical infrastructure supporting these nodes in Azure datacenters. Customers running AV36 nodes should monitor their environment’s health and capacity and plan workload migrations using VMware vMotion or other supported VMware tools to newer node types such as AV36m or AV36x, if available, or other node SKUs that Microsoft offers. The Reserved Instance contracts remain honored until their expiration, ensuring no immediate billing disruptions. Microsoft recommends reviewing RI expiration dates to align migration schedules and avoid capacity gaps.

**Use Cases and Application Scenarios:**  
This update primarily affects enterprises leveraging AVS for hybrid cloud deployments, disaster recovery, or VMware workload modernization on Azure. Organizations running legacy AV36 nodes in production or test environments will need to plan upgrades or migrations to maintain support and benefit from improved hardware capabilities. Scenarios include migrating VMware vSphere clusters, updating disaster recovery plans, or scaling environments with newer node types that offer better performance or cost efficiency.

**Important Considerations and Limitations:**  
- Customers must proactively plan migration well before the June 30, 2028 deadline to avoid service interruptions.  
- Reserved Instances for AV36 remain valid until expiration, but no new AV36 RIs will be sold post-retirement.  
- Migration may require downtime or resource planning depending on workload criticality and cluster configurations.  
- Compatibility of VMware versions and integrations should be validated with newer node types to ensure seamless migration.  
- Monitoring tools and Azure VMware Solution management portals should be used to track node health and capacity.

**Integration with Related Azure Services:**  
The AV36 node retirement impacts integrations with Azure services such as Azure Site Recovery, Azure Monitor, and Azure Backup, which rely on the underlying AVS infrastructure. Customers should verify that these services continue to function correctly post-migration to newer node types. Additionally, networking configurations involving Azure ExpressRoute or VPN gateways connected to AV36 nodes should be reviewed to ensure compatibility and performance continuity. Azure Policy and Azure Cost Management tools can assist in governance and cost tracking during the transition.

In summary, the AV36 node retirement announcement provides a clear timeline for customers to plan their VMware workload migration within Azure VMware Solution, ensuring continuity, compliance, and access to modern infrastructure capabilities while maintaining existing Reserved Instance benefits until expiration.

---

### 2. Retirement: Entity Linking from Azure AI Language

**Published**: September 26, 2025 22:00:37 UTC
**Link**: [Retirement: Entity Linking from Azure AI Language](https://azure.microsoft.com/updates?id=499851)

**Update ID**: 499851
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Azure AI Language, Retirements, Services

**Summary**:

- What was updated  
Microsoft announced the planned retirement of the Entity Linking feature from Azure AI Language.

- Key changes or new features  
Entity Linking, which provided the capability to identify and link entities to a knowledge base, will no longer be supported. As a replacement, developers and IT professionals are advised to use Named Entity Recognition (NER) within Azure AI Language, which continues to support entity identification but without linking to external knowledge bases.

- Target audience affected  
Developers and IT professionals who currently use or plan to use Azure AI Language’s Entity Linking feature for entity disambiguation and linking in their applications.

- Important notes if any  
Microsoft will provide full support until the retirement date (not specified in the update). Users should plan migration strategies to transition from Entity Linking to Named Entity Recognition to avoid disruptions. Since NER does not provide entity linking, alternative solutions or custom implementations may be needed for scenarios requiring knowledge base linking. Monitoring official Azure updates for the exact retirement timeline and guidance is recommended.

**Details**:

Microsoft has announced the planned retirement of the Entity Linking feature within Azure AI Language, signaling a strategic shift in how entity identification capabilities are offered in the Azure Cognitive Services ecosystem. This update is critical for IT professionals managing natural language processing (NLP) workflows, as it impacts existing applications relying on Entity Linking for semantic enrichment and knowledge graph integration.

**Background and Purpose of the Update**  
Entity Linking has traditionally enabled applications to not only recognize named entities (such as people, organizations, locations) in unstructured text but also to disambiguate and link these entities to unique identifiers in a knowledge base, facilitating richer semantic understanding and downstream analytics. Microsoft’s decision to retire this feature is part of a broader effort to streamline Azure AI Language services, consolidate capabilities, and encourage adoption of more versatile and actively supported features, such as Named Entity Recognition (NER).

**Specific Features and Detailed Changes**  
The retirement means that the Entity Linking API endpoint will no longer be available after the announced deprecation date. Users will need to migrate to Named Entity Recognition, which continues to support entity detection but without explicit linking to external knowledge bases. NER identifies and classifies entities into predefined categories (e.g., Person, Location, Organization) but does not resolve these entities to unique identifiers or knowledge graph entries.

**Technical Mechanisms and Implementation Methods**  
Entity Linking combined entity recognition with disambiguation algorithms that leveraged a curated knowledge base to resolve ambiguities—e.g., distinguishing "Apple" the company from "apple" the fruit. This involved context-aware models and entity resolution pipelines. With the retirement, developers will rely solely on NER models, which use transformer-based architectures (such as those built on BERT or similar) to detect and classify entities in text. Implementation involves calling the Azure AI Language NER endpoint via REST API or SDKs, submitting text documents, and receiving JSON responses with entity types and offsets.

**Use Cases and Application Scenarios**  
Entity Linking was particularly useful in scenarios requiring semantic enrichment, such as knowledge graph population, content recommendation, and advanced search indexing where entity disambiguation is critical. Post-retirement, applications focused on entity recognition, sentiment analysis, or text classification can continue using NER. However, scenarios requiring entity disambiguation will need to explore custom solutions, third-party services, or build in-house linking mechanisms possibly leveraging Azure’s other services like Azure Cognitive Search or custom ML models.

**Important Considerations and Limitations**  
- Migration: Existing applications must plan migration before the retirement date to avoid service disruption.  
- Feature Gap: NER does not provide entity linking, so applications relying on unique entity IDs or knowledge base integration will lose this capability.  
- Custom Solutions: To replicate linking functionality, developers might need to integrate NER output with external knowledge bases or graph databases manually.  
- Support and SLA: Microsoft will continue to support the feature until retirement but recommends transitioning to supported features for long-term reliability.

**Integration with Related Azure Services**  
While Entity Linking is retired, Azure AI Language’s NER can be integrated with other Azure services to approximate linking functionality:  
- **Azure Cognitive Search:** Enrich indexed documents with recognized entities to improve search relevance.  
- **Azure Synapse Analytics:** Combine NER output with big data processing for advanced analytics.  
- **Azure Cosmos DB or Azure SQL:** Store recognized entities and build custom linking logic.  
- **Azure Machine Learning:** Train custom disambiguation models using NER outputs as input features.

In summary, the retirement of Entity Linking from Azure AI Language requires IT professionals to transition to Named Entity Recognition for entity identification tasks and to architect alternative solutions for entity disambiguation and linking, leveraging Azure’s broader ecosystem and custom development to maintain semantic enrichment capabilities.

---

### 3. Retirement: The Linux Consumption hosting plan of Azure Functions will be retired on September 30, 2028. Migrate to Flex Consumption.

**Published**: September 26, 2025 16:30:29 UTC
**Link**: [Retirement: The Linux Consumption hosting plan of Azure Functions will be retired on September 30, 2028. Migrate to Flex Consumption.](https://azure.microsoft.com/updates?id=499451)

**Update ID**: 499451
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Internet of Things, Azure Functions, Retirements, Pricing & Offerings

**Summary**:

- What was updated  
Microsoft announced the retirement of the Azure Functions Linux Consumption hosting plan, effective September 30, 2028.

- Key changes or new features  
Customers currently using the Linux Consumption plan are encouraged to migrate to the Flex Consumption plan. Flex Consumption provides enhanced capabilities including faster scaling, improved advanced networking options, cold start mitigation to reduce latency, and concurrency control for better workload management.

- Target audience affected  
This update primarily affects developers and IT professionals managing Azure Functions on Linux Consumption plans. Organizations running serverless workloads on this plan need to plan migration to avoid service disruption.

- Important notes if any  
The retirement date is set well in advance, giving ample time for migration. Users should identify affected resources and start transitioning to Flex Consumption to leverage improved performance and networking features. Review application dependencies and test workloads on Flex Consumption to ensure compatibility and optimal operation before the deadline.  

For more details and migration guidance, visit the official Azure update page: https://azure.microsoft.com/updates?id=499451

**Details**:

The Azure Functions Linux Consumption hosting plan is scheduled for retirement on September 30, 2028, prompting customers to migrate to the Azure Functions Flex Consumption plan, which is designed to provide enhanced performance, scalability, and networking capabilities. This update reflects Microsoft’s strategic shift to offer a more advanced and flexible serverless hosting environment for Linux-based Azure Functions workloads.

**Background and Purpose of the Update**  
The Linux Consumption plan has been a popular choice for running serverless functions on Linux, offering a cost-effective, event-driven compute model with automatic scaling. However, as serverless workloads grow in complexity and demand, limitations in scaling speed, cold start latency, and networking flexibility have become apparent. The Flex Consumption plan addresses these challenges by delivering improved infrastructure and capabilities, enabling developers to build more responsive and resilient applications. The retirement timeline provides ample time for customers to plan and execute migration strategies.

**Specific Features and Detailed Changes**  
- **Faster Scaling:** Flex Consumption offers quicker scale-out and scale-in times, reducing latency during traffic spikes and improving overall application responsiveness.  
- **Advanced Networking:** Unlike the Linux Consumption plan, Flex Consumption supports Virtual Network (VNet) integration, allowing secure, private connectivity to on-premises or other Azure resources.  
- **Cold Start Mitigation:** Flex Consumption includes features to reduce cold start delays, such as pre-warmed instances and improved runtime optimizations, enhancing user experience for latency-sensitive applications.  
- **Concurrency Control:** The plan supports configurable concurrency settings, enabling better throughput management and resource utilization per function instance.  
- **Extended Runtime Support:** Flex Consumption supports a broader range of runtime versions and custom container images, providing greater flexibility in development and deployment.

**Technical Mechanisms and Implementation Methods**  
Migration involves transitioning existing Linux Consumption plan functions to the Flex Consumption plan within the Azure Functions service. This typically requires:  
- Reviewing current function app configurations and dependencies.  
- Updating the hosting plan SKU to Flex Consumption via Azure Portal, CLI, or ARM templates.  
- Validating VNet integration and adjusting network security groups or firewall rules if applicable.  
- Testing function performance to leverage concurrency and cold start improvements.  
- Monitoring and adjusting scaling parameters as needed.  
Azure provides tools and documentation to identify affected resources and automate parts of the migration process.

**Use Cases and Application Scenarios**  
- **Event-driven APIs:** Applications requiring low-latency responses under variable loads benefit from faster scaling and cold start improvements.  
- **Secure Enterprise Integrations:** Functions needing access to private networks or on-premises systems can leverage VNet integration.  
- **High-throughput Processing:** Workloads with high concurrency demands can optimize resource usage with concurrency controls.  
- **Custom Runtime Environments:** Developers using custom containers or specific runtime versions gain flexibility in deployment options.

**Important Considerations and Limitations**  
- Migration requires careful planning to avoid downtime, especially for production workloads.  
- Some legacy configurations or third-party dependencies may need updates to be compatible with Flex Consumption.  
- Pricing models differ; while Flex Consumption may offer better performance, cost implications should be evaluated based on workload patterns.  
- Monitoring and alerting configurations should be reviewed post-migration to ensure operational visibility.  
- The retirement date is several years away, but early migration is recommended to leverage new features and avoid last-minute disruptions.

**Integration with Related Azure Services**  
Flex Consumption’s enhanced networking capabilities improve integration with Azure Virtual Network, Azure Private Link, and Azure Firewall, enabling secure and compliant architectures. It also works seamlessly with Azure Monitor for enhanced telemetry, Azure API Management for API gateway scenarios, and Azure DevOps or GitHub Actions for CI/CD pipelines. Additionally, it supports Azure Event Grid, Service Bus, and Storage triggers with improved reliability and performance.

In summary, the retirement of the Azure Functions Linux Consumption hosting plan by September 30, 2028, necessitates migration to the Flex Consumption plan, which delivers significant advancements in scaling speed,

---

### 4. Retirement: Upgrade BlobFuse v1 to latest version of Blobfuse v2 

**Published**: September 26, 2025 16:00:55 UTC
**Link**: [Retirement: Upgrade BlobFuse v1 to latest version of Blobfuse v2 ](https://azure.microsoft.com/updates?id=498563)

**Update ID**: 498563
**Data source**: Azure Updates API

**Categories**: Storage, Azure Blob Storage, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of BlobFuse v1 and recommends upgrading to BlobFuse v2 for accessing Azure Blob Storage as a file system.

- Key changes or new features  
BlobFuse v2 offers improved performance, enhanced stability, and ongoing feature development. All future innovations and support will be exclusively for BlobFuse v2, ensuring better integration and functionality with Azure Blob Storage.

- Target audience affected  
Developers and IT professionals who use BlobFuse v1 to mount Azure Blob Storage containers as file systems in Linux environments.

- Important notes if any  
Support for BlobFuse v1 will be discontinued, so continuing to use v1 may lead to lack of security updates, bug fixes, and compatibility issues. It is strongly advised to upgrade to BlobFuse v2 promptly to benefit from ongoing enhancements and maintain support.  

For more details, visit: https://azure.microsoft.com/updates?id=498563

**Details**:

The Azure update announces the retirement of BlobFuse v1 and strongly recommends upgrading to BlobFuse v2, as all future development, enhancements, and support for Azure Blob Storage file system access will be exclusively focused on BlobFuse v2.

**Background and Purpose of the Update**  
BlobFuse is an open-source virtual file system driver for Azure Blob Storage, enabling Linux clients to mount a Blob Storage container as a local file system. BlobFuse v1 was introduced to simplify access to blob storage using standard file system APIs. However, BlobFuse v1 has limitations in performance, scalability, and feature support. BlobFuse v2 was developed to address these issues by redesigning the architecture for better reliability, extensibility, and performance. This update signals the official retirement of BlobFuse v1, encouraging users to migrate to BlobFuse v2 to benefit from ongoing improvements and ensure continued support.

**Specific Features and Detailed Changes**  
BlobFuse v2 introduces several key enhancements over v1:  
- **Improved Performance:** BlobFuse v2 uses a new caching mechanism and optimized I/O operations to reduce latency and increase throughput when accessing blobs.  
- **Enhanced Scalability:** It supports larger file sizes and higher concurrency, making it suitable for enterprise workloads.  
- **Better Consistency and Reliability:** BlobFuse v2 implements stronger consistency models and improved error handling to reduce data corruption and access failures.  
- **Extensibility:** The architecture is modular, allowing easier integration of new features such as encryption, compression, and telemetry.  
- **Compatibility:** BlobFuse v2 supports the latest Azure Blob Storage APIs and authentication methods, including Azure AD and managed identities.  
- **Cross-platform Support:** While BlobFuse v1 was primarily Linux-focused, BlobFuse v2 is designed with broader platform compatibility in mind.

**Technical Mechanisms and Implementation Methods**  
BlobFuse v2 is implemented as a FUSE (Filesystem in Userspace) driver that interacts with Azure Blob Storage REST APIs. It uses an advanced local caching layer to store frequently accessed data and metadata, reducing network calls. The caching is intelligently synchronized with the blob storage to maintain consistency. BlobFuse v2 supports OAuth 2.0 token-based authentication, enabling integration with Azure Active Directory for secure access. It also supports container-level mounts with granular access controls. The modular design separates the caching, network communication, and file system layers, facilitating maintenance and feature updates.

**Use Cases and Application Scenarios**  
- **Big Data and Analytics:** BlobFuse v2 allows data scientists and engineers to mount blob storage containers as local file systems, enabling seamless access to large datasets for processing with tools like Apache Spark or Hadoop.  
- **DevOps and CI/CD Pipelines:** Developers can use BlobFuse v2 to mount blob storage in build agents or containers, simplifying artifact storage and retrieval.  
- **Backup and Archival:** Organizations can mount blob storage as a file system for backup solutions that require file system semantics.  
- **Web and Media Applications:** BlobFuse v2 facilitates streaming and serving media files directly from blob storage with improved performance.  
- **Hybrid Cloud Scenarios:** Enterprises using Linux VMs or on-premises servers can integrate blob storage into their workflows transparently.

**Important Considerations and Limitations**  
- **Migration Effort:** Upgrading from BlobFuse v1 to v2 may require configuration changes and testing to ensure compatibility with existing workflows.  
- **Feature Parity:** While BlobFuse v2 adds many features, some behaviors may differ from v1, necessitating validation.  
- **Resource Usage:** BlobFuse v2’s caching and concurrency improvements may increase local resource consumption; adequate system resources should be provisioned.  
- **Support Lifecycle:** BlobFuse v1 will no longer receive updates or support, so continued use may expose systems to security and reliability risks.  
- **Platform Support:** Verify that the target environment supports BlobFuse v2, especially if using non-Linux

---

### 5. Retirement: Azure App Service on Azure Arc enabled Kubernetes

**Published**: September 26, 2025 11:45:02 UTC
**Link**: [Retirement: Azure App Service on Azure Arc enabled Kubernetes](https://azure.microsoft.com/updates?id=500016)

**Update ID**: 500016
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements, Features

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure App Service on Azure Arc enabled Kubernetes, effective September 30, 2025.

- Key changes or new features  
After this date, customers will no longer be able to install or use the Azure App Service extension on Azure Arc enabled Kubernetes clusters. The service will be fully retired, requiring migration to alternative hosting solutions for application workloads.

- Target audience affected  
Developers and IT professionals managing applications deployed via Azure App Service on Azure Arc enabled Kubernetes clusters will be impacted. Organizations leveraging this service for hybrid or multi-cloud app hosting need to plan accordingly.

- Important notes if any  
Customers should begin planning migration strategies well before the retirement date to avoid service disruption. Microsoft recommends evaluating other Azure services or third-party solutions for hosting applications currently running on Azure Arc enabled Kubernetes with App Service. No direct replacement or upgrade path is provided, so early assessment and testing are critical. For more details, refer to the official update link.

**Details**:

The announced retirement of Azure App Service on Azure Arc enabled Kubernetes, effective September 30, 2025, marks a significant change in how customers deploy and manage web applications on Kubernetes clusters connected via Azure Arc. This update reflects Microsoft’s strategic shift to streamline its hybrid application hosting offerings and encourages migration to alternative solutions better aligned with evolving cloud-native architectures.

**Background and Purpose of the Update**  
Azure App Service on Azure Arc enabled Kubernetes was introduced to extend Azure App Service capabilities—such as simplified app deployment, scaling, and management—to Kubernetes clusters running outside of Azure, including on-premises or other cloud environments, via Azure Arc. This hybrid model enabled organizations to leverage Azure’s PaaS features while maintaining workloads closer to their data or within specific regulatory boundaries. The retirement signals Microsoft’s intent to consolidate and optimize its hybrid app hosting portfolio, likely focusing on more integrated or container-native approaches such as Azure Container Apps, Azure Kubernetes Service (AKS), and Azure Arc-enabled Kubernetes with direct container orchestration.

**Specific Features and Detailed Changes**  
The key feature being retired is the ability to install the Azure App Service extension on Azure Arc enabled Kubernetes clusters, which facilitated running App Service web apps on these clusters. Post-retirement, customers will no longer be able to install or update this extension, effectively ending support for hosting App Service workloads in this manner. Existing deployments will require migration before the cutoff date to avoid service disruption.

**Technical Mechanisms and Implementation Methods**  
Azure App Service on Azure Arc enabled Kubernetes functioned by deploying a set of controllers and components onto the Kubernetes cluster via the Azure Arc agent. These components translated App Service configurations into Kubernetes-native resources and managed lifecycle operations such as scaling, health monitoring, and deployment rollouts. The extension integrated with Azure Resource Manager (ARM) to provide a unified management plane, enabling users to deploy and manage apps through Azure Portal, CLI, or ARM templates while the actual runtime operated on the Kubernetes cluster.

With retirement, this extension and its associated controllers will no longer receive updates or support. Customers will need to transition to alternatives that may involve directly managing containerized workloads on Kubernetes or leveraging other Azure services that provide PaaS-like capabilities on Kubernetes.

**Use Cases and Application Scenarios**  
This service was primarily used by enterprises requiring hybrid or multi-cloud web app hosting with Azure’s developer productivity features but needing to keep workloads on-premises or in specific cloud environments for compliance, latency, or data sovereignty reasons. Typical scenarios included internal line-of-business apps, edge computing deployments, and regulated industry applications.

Post-retirement, these use cases can be addressed by migrating to AKS with custom containerized app deployments, Azure Container Apps for serverless container hosting, or other hybrid solutions like Azure Arc-enabled Kubernetes with GitOps-based app deployment, depending on the organization’s operational model and cloud strategy.

**Important Considerations and Limitations**  
- **Migration Planning:** Customers must inventory existing App Service on Azure Arc workloads and plan migration well before the September 2025 deadline to avoid downtime.  
- **Feature Parity:** Alternative solutions may not offer exact feature parity, especially around integrated App Service capabilities like built-in authentication, deployment slots, and scaling abstractions. Additional engineering effort may be required to replicate these functionalities.  
- **Operational Complexity:** Moving from a PaaS-like model to container-native or serverless container platforms may increase operational complexity and require upskilling in Kubernetes management or container orchestration.  
- **Support and Updates:** Post-retirement, no security patches or feature updates will be provided, increasing risk if the service is used beyond the cutoff date.

**Integration with Related Azure Services**  
The retirement encourages leveraging other Azure services that integrate with Azure Arc and Kubernetes:  
- **Azure Kubernetes Service (AKS):** For fully managed Kubernetes clusters in Azure with deep integration and PaaS capabilities.  
- **Azure Container Apps:** For serverless container hosting with built-in scaling and event-driven architecture, suitable for

---


*This report was automatically generated - 2025-09-27 03:02:46 UTC*