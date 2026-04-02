# April 02, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 02, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Retirement: Service Fabric support for Windows Server 2022 ends on March 31, 2027 - upgrade to Windows Server 2025

**Published**: April 01, 2026 21:00:19 UTC
**Link**: [Retirement: Service Fabric support for Windows Server 2022 ends on March 31, 2027 - upgrade to Windows Server 2025](https://azure.microsoft.com/updates?id=558247)

**Update ID**: 558247
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Service Fabric, Retirements

**Summary**:

- What was updated  
Azure Service Fabric will retire support for clusters running on Windows Server 2022 as of March 31, 2027.

- Key changes or new features  
Support for Service Fabric clusters on Windows Server 2022 will end. Customers must upgrade their clusters to Windows Server 2025 to continue receiving support and updates. This change is part of aligning Service Fabric’s support lifecycle with Windows OS image support policies.

- Target audience affected  
This update impacts IT professionals and developers managing or deploying Service Fabric clusters on Windows Server 2022.

- Important notes if any  
To avoid unsupported configurations and potential security or compliance risks, all Service Fabric clusters must be upgraded to Windows Server 2025 before March 31, 2027. Begin planning migration and testing processes early to ensure a smooth transition. Failure to upgrade will result in loss of support, including critical updates and security patches. For more information, refer to the official Azure update: https://azure.microsoft.com/updates?id=558247

**Details**:

**Azure Update Report: Retirement of Service Fabric Support for Windows Server 2022**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Service Fabric support for Windows Server 2022, effective March 31, 2027. After this date, Service Fabric clusters running on Windows Server 2022 will no longer be supported. The purpose of this update is to align Service Fabric’s Windows operating system (OS) image support lifecycle with Microsoft’s broader OS support policies and to encourage customers to upgrade to Windows Server 2025 for continued support and security.

**Specific Features and Detailed Changes:**  
- **Retirement Date:** Support for Service Fabric clusters on Windows Server 2022 ends on March 31, 2027.
- **Upgrade Requirement:** Customers must migrate their Service Fabric clusters to Windows Server 2025 before this date to maintain a supported environment.
- **Support Alignment:** This change brings Service Fabric’s OS image support in line with Microsoft’s standard support mode for Windows OS images.

**Technical Mechanisms and Implementation Methods:**  
- **Cluster Upgrade Path:** IT professionals managing Service Fabric clusters on Windows Server 2022 must plan and execute an in-place upgrade or redeployment to Windows Server 2025. This typically involves:
  - Assessing cluster compatibility with Windows Server 2025.
  - Testing application workloads on Windows Server 2025 in a staging environment.
  - Rolling upgrade of cluster nodes to minimize downtime and ensure high availability.
- **Image Support Mode:** Service Fabric will update its supported OS image list, and after the retirement date, new deployments or upgrades using Windows Server 2022 images will not be supported.

**Use Cases and Application Scenarios:**  
- **Current Deployments:** Organizations running mission-critical microservices or stateful applications on Service Fabric clusters hosted on Windows Server 2022.
- **Planned Migrations:** Enterprises planning infrastructure refresh cycles or aligning with internal OS lifecycle management policies.
- **Compliance:** Scenarios where maintaining a supported OS and platform is required for regulatory compliance or security standards.

**Important Considerations and Limitations:**  
- **End of Support Risks:** After March 31, 2027, clusters running on Windows Server 2022 will not receive technical support, security updates, or bug fixes from Microsoft for Service Fabric.
- **Upgrade Planning:** Migration to Windows Server 2025 may require application compatibility testing and validation of custom extensions or integrations.
- **Downtime Minimization:** Rolling upgrades and blue-green deployment strategies are recommended to reduce service disruption.
- **No Extended Support:** There is no mention of extended support or exceptions for Windows Server 2022 clusters in Service Fabric environments.

**Integration with Related Azure Services:**  
- **Azure Service Fabric Clusters:** This update directly impacts Service Fabric clusters deployed on Azure virtual machines or on-premises infrastructure using Windows Server 2022.
- **Azure Update Management:** Integration with Azure Update Management and Azure Automation can facilitate OS upgrades and compliance tracking.
- **Azure Security and Compliance:** Upgrading to a supported OS ensures continued integration with Azure security features, monitoring, and compliance reporting.

**Summary:**  
Service Fabric support for Windows Server 2022 will end on March 31, 2027; customers must upgrade their clusters to Windows Server 2025 by this date to remain supported.

---

### 2. Retirement: Service Fabric support for Windows Server 2019 ends on March 31, 2027 - upgrade to Windows Server 2025

**Published**: April 01, 2026 20:30:41 UTC
**Link**: [Retirement: Service Fabric support for Windows Server 2019 ends on March 31, 2027 - upgrade to Windows Server 2025](https://azure.microsoft.com/updates?id=558246)

**Update ID**: 558246
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Service Fabric, Retirements

**Summary**:

- What was updated  
Azure Service Fabric will retire support for clusters running on Windows Server 2019 as of March 31, 2027.

- Key changes or new features  
Support for Service Fabric clusters on Windows Server 2019 will end. Customers must upgrade their clusters to Windows Server 2025 to continue receiving support and updates. This aligns Service Fabric’s OS image support lifecycle with Microsoft’s broader support policies.

- Target audience affected  
Developers and IT professionals managing Service Fabric clusters on Windows Server 2019, including those responsible for infrastructure planning, cluster maintenance, and application deployment.

- Important notes if any  
All Service Fabric clusters running on Windows Server 2019 must be upgraded to Windows Server 2025 by March 31, 2027, to remain in a supported state. Failure to upgrade will result in loss of support, including security updates and technical assistance. Begin planning your migration to avoid service disruptions. Review your current cluster deployments and update your infrastructure roadmap accordingly. For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=558246

**Details**:

**Azure Update Report: Retirement of Service Fabric Support for Windows Server 2019**

**Background and Purpose of the Update:**  
Microsoft Azure Service Fabric is a distributed systems platform used to build scalable, reliable, and easily managed applications for the cloud. The announced update states that Service Fabric will retire support for clusters running on Windows Server 2019 as of March 31, 2027. The purpose of this update is to align Service Fabric’s Windows OS image support mode with the latest Windows Server releases, ensuring continued security, performance, and compatibility. Customers are required to upgrade their Service Fabric clusters to Windows Server 2025 by the specified date to remain in a supported state.

**Specific Features and Detailed Changes:**  
The key change is the end of official support for Service Fabric clusters operating on Windows Server 2019. After March 31, 2027, Microsoft will no longer provide updates, security patches, or technical support for Service Fabric clusters on this OS version. The update mandates migration to Windows Server 2025, which will become the minimum supported OS for Service Fabric clusters. No new features or enhancements for Service Fabric clusters on Windows Server 2019 will be released post-retirement.

**Technical Mechanisms and Implementation Methods:**  
To comply with this update, IT professionals must plan and execute an upgrade of their Service Fabric clusters from Windows Server 2019 to Windows Server 2025. This involves provisioning new nodes with Windows Server 2025, migrating workloads, and updating cluster configurations. The upgrade process should follow Microsoft’s best practices for Service Fabric cluster upgrades, including validating application compatibility, ensuring backup and recovery procedures, and testing cluster stability post-migration. The OS image support mode refers to the underlying operating system images used for Service Fabric cluster nodes, which must be updated to Windows Server 2025.

**Use Cases and Application Scenarios:**  
This update is relevant for organizations running mission-critical workloads, microservices, or containerized applications on Service Fabric clusters deployed on Windows Server 2019. Typical scenarios include enterprise applications, IoT solutions, and cloud-native services that rely on Service Fabric for orchestration and lifecycle management. Upgrading to Windows Server 2025 ensures continued access to Azure support, security updates, and compatibility with new Service Fabric features.

**Important Considerations and Limitations:**  
- **Deadline:** All Service Fabric clusters must be upgraded to Windows Server 2025 by March 31, 2027.
- **Support:** Clusters on Windows Server 2019 will not receive support, updates, or security patches after the retirement date.
- **Compatibility:** Applications and workloads must be validated for compatibility with Windows Server 2025 prior to migration.
- **Downtime:** Plan for potential downtime during the upgrade process and ensure proper backup and recovery strategies.
- **Cluster Configuration:** Review and update cluster configuration files and deployment scripts to reference Windows Server 2025 OS images.

**Integration with Related Azure Services:**  
Service Fabric clusters are often integrated with other Azure services such as Azure Monitor for telemetry, Azure Active Directory for authentication, and Azure DevOps for CI/CD pipelines. The upgrade to Windows Server 2025 may require updates to integration points, such as monitoring agents or security configurations. Ensure that all related services and dependencies are compatible with Windows Server 2025 to maintain seamless operations.

**Summary Sentence:**  
Service Fabric support for Windows Server 2019 will end on March 31, 2027, requiring customers to upgrade clusters to Windows Server 2025 to maintain a supported and secure environment.

---

### 3. Public Preview: Unlock Client-Side Configuration at Scale with Azure App Configuration and Azure Front Door

**Published**: April 01, 2026 19:00:05 UTC
**Link**: [Public Preview: Unlock Client-Side Configuration at Scale with Azure App Configuration and Azure Front Door](https://azure.microsoft.com/updates?id=537234)

**Update ID**: 537234
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Developer tools, Mobile, Security, Web, App Configuration, Features, Microsoft Ignite

**Summary**:

- What was updated  
Azure App Configuration now integrates with Azure Front Door, enabling secure, CDN-scale delivery of dynamic configuration data directly to client-side applications. This feature is available in Public Preview.

- Key changes or new features  
  - Client-side applications can fetch configuration data from Azure App Configuration via Azure Front Door, leveraging global CDN distribution for low-latency access.  
  - Secure delivery ensures configuration data is protected while being accessible at scale.  
  - Supports dynamic updates, allowing modern apps to adapt configuration without redeployment or backend changes.

- Target audience affected  
  - Front-end and full-stack developers building modern web or mobile applications that require dynamic configuration.  
  - IT professionals and DevOps teams managing application configuration and deployment at scale.

- Important notes if any  
  - This integration is currently in Public Preview and may not be suitable for production workloads.  
  - Developers should review security and access controls to ensure sensitive configuration data is properly protected.  
  - This feature can help reduce backend load and improve app responsiveness by offloading configuration delivery to Azure’s global CDN network.  

For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=537234).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Unlock Client-Side Configuration at Scale with Azure App Configuration and Azure Front Door  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=537234)

---

**Background and Purpose of the Update**  
Modern cloud applications increasingly require dynamic configuration capabilities, especially for client-side applications such as Single Page Applications (SPAs) and mobile apps. Traditionally, configuration management has been server-centric, limiting flexibility and scalability for client-side scenarios. This update introduces a public preview of Azure App Configuration’s integration with Azure Front Door, enabling secure and scalable delivery of dynamic configuration directly to client-side applications. The purpose is to provide a robust mechanism for distributing configuration data at CDN scale, enhancing flexibility and operational efficiency for modern application architectures.

**Specific Features and Detailed Changes**  
- **Direct Client-Side Configuration Delivery:** Azure App Configuration can now serve configuration data directly to client-side applications via Azure Front Door, leveraging CDN capabilities for global distribution and performance.
- **Secure Access:** The integration ensures that configuration data is delivered securely, mitigating risks associated with exposing sensitive configuration information.
- **Scalability:** By utilizing Azure Front Door’s CDN infrastructure, configuration data can be delivered at scale, supporting high-traffic scenarios and geographically distributed users.
- **Dynamic Updates:** Applications can retrieve up-to-date configuration values without redeployment, enabling real-time feature toggling, environment-specific settings, and other dynamic behaviors.

**Technical Mechanisms and Implementation Methods**  
- **Integration Workflow:** Azure App Configuration is configured as a backend for Azure Front Door. Client-side applications make requests to Azure Front Door, which proxies these requests to Azure App Configuration.
- **CDN Distribution:** Azure Front Door caches configuration responses, reducing latency and load on the App Configuration service.
- **Security Controls:** Access to configuration data is managed through Azure Front Door’s security features, such as custom domains, HTTPS enforcement, and Web Application Firewall (WAF) rules.
- **Configuration Retrieval:** Client-side applications use HTTP requests to fetch configuration data, which can be versioned or segmented as needed.

**Use Cases and Application Scenarios**  
- **Feature Management:** Enable feature flags and toggles in client-side applications, allowing for real-time rollout and rollback of features without redeployment.
- **Environment-Specific Settings:** Deliver environment-specific configuration (e.g., API endpoints, branding, localization) to client apps based on deployment context.
- **Global Application Distribution:** Support applications with users across multiple regions by delivering configuration data efficiently via CDN.
- **Mobile and SPA Configuration:** Provide dynamic configuration updates to mobile apps and SPAs, improving user experience and operational agility.

**Important Considerations and Limitations**  
- **Security:** Ensure sensitive configuration data is not exposed to unauthorized clients; use Azure Front Door’s security features to restrict access.
- **Cache Invalidation:** Consider cache duration and invalidation strategies to ensure clients receive timely updates to configuration data.
- **Data Size and Format:** Optimize configuration payloads for client-side consumption, avoiding excessive data transfer.
- **Preview Limitations:** As this feature is in public preview, it may not be suitable for production workloads and could be subject to change.

**Integration with Related Azure Services**  
- **Azure App Configuration:** Centralized configuration management, supporting versioning, labeling, and feature flags.
- **Azure Front Door:** Global CDN and application acceleration, providing secure and scalable access to backend services.
- **Azure Security Services:** Integration with Azure WAF, custom domains, and HTTPS for secure configuration delivery.

---

**Summary Sentence:**  
Azure App Configuration’s integration with Azure Front Door, now in public preview, enables secure and scalable delivery of dynamic configuration directly to client-side applications, providing enhanced flexibility and operational efficiency for modern cloud architectures.

---

### 4. Generally Available: Azure Data Box enhances compliance with automatic Secure Erasure Certificates

**Published**: April 01, 2026 18:30:16 UTC
**Link**: [Generally Available: Azure Data Box enhances compliance with automatic Secure Erasure Certificates](https://azure.microsoft.com/updates?id=559772)

**Update ID**: 559772
**Data source**: Azure Updates API

**Categories**: Launched, Migration, Storage, Azure Data Box, Features

**Summary**:

- What was updated  
Azure Data Box now provides automatic generation of Secure Erasure Certificates for every completed order.

- Key changes or new features  
A Secure Erasure Certificate is now automatically generated and available for download after each Data Box order is completed. This certificate verifies that all data on the device has been securely erased in compliance with NIST 800-88 Revision 2 standards. This enhancement streamlines compliance documentation and audit processes by providing official proof of secure data erasure.

- Target audience affected  
This update primarily impacts IT professionals, compliance officers, and developers who manage data migration or transfer projects using Azure Data Box and require evidence of secure data destruction for regulatory or organizational compliance.

- Important notes if any  
The Secure Erasure Certificate is downloadable and can be retained for audit and compliance purposes. This feature helps organizations meet strict data protection and regulatory requirements, reducing manual tracking and paperwork. No additional configuration is required; the certificate is provided automatically after order completion.

**Details**:

**Azure Update Report: Generally Available – Azure Data Box Enhances Compliance with Automatic Secure Erasure Certificates**

**Background and Purpose of the Update:**  
Azure Data Box is a physical device solution for secure, large-scale data transfer to and from Azure. Data security and compliance are critical concerns, especially when handling sensitive or regulated data. To address compliance requirements and provide assurance to customers, Azure Data Box now includes an enhancement that automatically generates a Secure Erasure Certificate for every completed order. This certificate verifies that all data on the device has been securely erased in accordance with the NIST 800-88 Revision 2 standard, a widely recognized guideline for media sanitization.

**Specific Features and Detailed Changes:**  
- **Automatic Certificate Generation:** Upon completion of each Data Box order, Azure now automatically creates a Secure Erasure Certificate.
- **Downloadable Certificate:** The certificate is made available for download, allowing organizations to retain official documentation for audit and compliance purposes.
- **NIST 800-88 Rev. 2 Compliance:** The certificate explicitly confirms that the erasure process adheres to the NIST 800-88 Revision 2 standard, which is a benchmark for secure data destruction.

**Technical Mechanisms and Implementation Methods:**  
- **Automated Workflow:** After the Data Box device is returned to Microsoft and the offload process is complete, Azure initiates an automated secure erasure process on the device.
- **Erasure Process:** The data on the device is sanitized following the NIST 800-88 Rev. 2 guidelines, which specify methods for overwriting, purging, or destroying data to prevent recovery.
- **Certificate Generation:** Once erasure is verified, the system generates a Secure Erasure Certificate, which is then linked to the specific Data Box order and made available for download through the Azure portal or relevant management interface.

**Use Cases and Application Scenarios:**  
- **Regulated Industries:** Organizations in finance, healthcare, government, or any sector with strict data handling regulations can use the certificate as proof of compliance during audits.
- **Data Lifecycle Management:** Enterprises with internal data governance policies can leverage the certificate to document secure data destruction as part of their data lifecycle management.
- **Third-Party Data Transfers:** When transferring data between entities, the certificate provides assurance to all stakeholders that no residual data remains on the device post-transfer.

**Important Considerations and Limitations:**  
- **Scope:** The certificate is generated only for completed Data Box orders after the secure erasure process is finished.
- **Certificate Access:** Users must ensure they download and retain the certificate for their records, as required by their compliance or audit processes.
- **Standard Compliance:** The certificate attests to compliance with NIST 800-88 Rev. 2 only; organizations with additional or different regulatory requirements should verify if this standard is sufficient for their needs.

**Integration with Related Azure Services:**  
- **Azure Data Box Management:** The certificate is integrated into the Data Box management workflow, accessible via the Azure portal.
- **Audit and Compliance Tools:** The downloadable certificate can be incorporated into broader compliance documentation or integrated with third-party compliance management solutions as evidence of secure data erasure.

**Summary Sentence:**  
Azure Data Box now automatically provides a downloadable Secure Erasure Certificate for every completed order, verifying NIST 800-88 Rev. 2-compliant data erasure and enhancing compliance documentation for secure data transfers.

---

### 5. Generally Available: Azure Data Box now supports Azure Files Provisioned v2

**Published**: April 01, 2026 18:15:44 UTC
**Link**: [Generally Available: Azure Data Box now supports Azure Files Provisioned v2](https://azure.microsoft.com/updates?id=559767)

**Update ID**: 559767
**Data source**: Azure Updates API

**Categories**: Launched, Migration, Storage, Azure Data Box, Features

**Summary**:

- What was updated  
Azure Data Box now supports data ingestion into Azure Files Provisioned v2 storage accounts.

- Key changes or new features  
Azure Data Box can now be used to transfer data directly into Azure Files Provisioned v2 accounts. Azure Files Provisioned v2 is a new billing model that allows customers to provision and pay for specific storage capacity, IOPS, and throughput, offering greater flexibility and predictable performance.

- Target audience affected  
Developers, IT professionals, and storage administrators who use Azure Data Box for large-scale data migration and require integration with Azure Files Provisioned v2 storage accounts.

- Important notes if any  
This update enables seamless migration of large datasets into Azure Files Provisioned v2, supporting scenarios that require predictable performance and cost management. Customers can now use Data Box for initial bulk data transfer to these accounts, streamlining onboarding and migration workflows.

For more details, see the [official update](https://azure.microsoft.com/updates?id=559767).

**Details**:

**Azure Update Report: Azure Data Box Now Supports Azure Files Provisioned v2 (Generally Available)**

**Background and Purpose of the Update:**  
Azure Data Box is a physical device solution designed for secure, large-scale offline data transfer to Azure. Traditionally, Data Box supported ingestion into standard Azure Files storage accounts. With the introduction of Azure Files Provisioned v2, Microsoft has responded to customer demand for more granular control over storage performance and cost. The purpose of this update is to enable Data Box users to ingest data directly into Azure Files Provisioned v2 storage accounts, thereby leveraging the new billing and performance model.

**Specific Features and Detailed Changes:**  
The update enables Azure Data Box devices to ingest data into Azure Files Provisioned v2 storage accounts. Azure Files Provisioned v2 is a new billing model that allows customers to provision and pay for specific capacity, IOPS (Input/Output Operations Per Second), and throughput values. This model differs from the traditional pay-as-you-go approach by offering predictable performance and cost management. The change ensures that data imported via Data Box can be stored in accounts configured with Provisioned v2, supporting scenarios where performance and capacity requirements are predefined.

**Technical Mechanisms and Implementation Methods:**  
When configuring an Azure Data Box job, users can now select Azure Files Provisioned v2 storage accounts as the target destination for their data. The ingestion process remains consistent with standard Data Box workflows: data is copied onto the device, shipped to Azure, and then uploaded to the specified storage account. The underlying mechanism ensures compatibility with the Provisioned v2 model, which allocates resources based on the provisioned values set by the customer. Data Box interacts with the Azure Files APIs to facilitate seamless data transfer, ensuring that the provisioned capacity, IOPS, and throughput are respected during ingestion.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for organizations migrating large datasets to Azure Files with strict performance or capacity requirements. Typical scenarios include:
- Enterprise file share migrations where predictable performance is required.
- Lift-and-shift of on-premises file servers to Azure Files Provisioned v2.
- Data archival projects needing guaranteed throughput.
- Workloads with consistent IOPS demands, such as application hosting or analytics.

By supporting Provisioned v2, Data Box enables customers to plan migrations with confidence, knowing their storage will meet performance SLAs.

**Important Considerations and Limitations:**  
IT professionals should be aware of the following:
- Only Azure Files Provisioned v2 storage accounts are supported for this feature; classic or standard accounts are not eligible.
- Customers must provision capacity, IOPS, and throughput before initiating the Data Box job to ensure optimal ingestion performance.
- Billing is based on provisioned values, not actual usage, so over-provisioning may lead to unnecessary costs.
- Ensure that the Data Box device firmware and Azure portal are updated to the latest versions to access this feature.

**Integration with Related Azure Services:**  
Azure Data Box integrates seamlessly with Azure Files Provisioned v2, allowing for direct ingestion. This update enhances Data Box’s compatibility with Azure Files, supporting hybrid cloud scenarios and aligning with Azure’s broader storage ecosystem. Data Box jobs can be managed via the Azure portal, and ingested data can be accessed through Azure Files SMB/NFS protocols, enabling integration with Azure Virtual Machines, Azure Kubernetes Service, and other Azure services that consume file shares.

**Summary:**  
Azure Data Box now supports ingestion into Azure Files Provisioned v2 storage accounts, allowing customers to provision and pay for specific capacity, IOPS, and throughput values, thereby offering greater flexibility and predictable performance for large-scale data migrations.

---

### 6. Public Preview: Azure NetApp Files storage with cool access enhancement 

**Published**: April 01, 2026 18:15:44 UTC
**Link**: [Public Preview: Azure NetApp Files storage with cool access enhancement ](https://azure.microsoft.com/updates?id=559504)

**Update ID**: 559504
**Data source**: Azure Updates API

**Categories**: In development, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files now supports storage with cool access enhancement in Public Preview, specifically for Premium and Ultra service levels.

- Key changes or new features  
A new QoS (Quality of Service) update enables automatic throughput adjustment when cool access is enabled. As data transitions from hot to cool storage, throughput is dynamically managed to maintain hot-tier performance for active data while optimizing costs for less frequently accessed (cool) data. This enhancement allows for more efficient handling of mixed hot and cool workloads without manual intervention.

- Target audience affected  
Developers and IT professionals managing storage-intensive applications, especially those leveraging Azure NetApp Files for workloads with varying data access patterns (e.g., analytics, backup, or tiered storage scenarios).

- Important notes if any  
The feature is currently in Public Preview and available for Premium and Ultra service levels only. Users should evaluate the feature in non-production environments and monitor performance and cost impacts. This update helps balance performance and cost, making it easier to optimize storage usage for workloads with both hot and cool data requirements.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=559504

**Details**:

**Azure Update Report: Public Preview – Azure NetApp Files Storage with Cool Access Enhancement**

**Background and Purpose of the Update**  
This update introduces a public preview of cool access enhancement for Azure NetApp Files (ANF) storage, specifically targeting Premium and Ultra service levels. The primary purpose is to optimize the balance between performance and cost for workloads that contain both hot and cool data. Traditionally, managing mixed-access workloads required manual intervention or resulted in suboptimal performance or higher costs. This enhancement aims to automate and streamline the process, ensuring efficient resource utilization.

**Specific Features and Detailed Changes**  
- **QoS Update with Cool Access:** The update brings a Quality of Service (QoS) enhancement that enables cool access on Premium and Ultra ANF service tiers.
- **Automatic Throughput Adjustment:** As data transitions to cool storage, the system automatically adjusts throughput allocations. This ensures that hot data continues to receive high performance, while cool data is managed more cost-effectively.
- **Mixed Workload Optimization:** The enhancement is specifically designed for environments where both hot (frequently accessed) and cool (infrequently accessed) data coexist, allowing seamless performance management without manual tuning.

**Technical Mechanisms and Implementation Methods**  
- **Throughput Management:** The underlying mechanism automatically scales throughput based on the access tier of the data. When data is identified as cool and moved to the cool storage tier, the system dynamically reduces the throughput allocated to that data, optimizing costs.
- **Service Level Integration:** These enhancements are available on the Premium and Ultra service levels, leveraging their existing high-performance capabilities while introducing cost-saving measures for cool data.
- **No Manual Intervention Required:** The process is automated, reducing the need for administrators to manually reconfigure storage or performance settings as data access patterns change.

**Use Cases and Application Scenarios**  
- **Data Lifecycle Management:** Organizations with workloads that experience changing data access patterns (e.g., analytics, backup, or archival scenarios) can benefit from automated tiering and throughput management.
- **Cost Optimization for Mixed Workloads:** Enterprises running applications with both hot and cool data (such as media repositories, financial records, or scientific data sets) can achieve lower storage costs without sacrificing performance for hot data.
- **Dynamic Workload Environments:** Environments where data access frequency is unpredictable or changes over time can leverage this feature for operational efficiency.

**Important Considerations and Limitations**  
- **Public Preview Status:** The feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes.
- **Service Level Availability:** The enhancement is limited to Premium and Ultra service levels; Standard tier users are not included in this update.
- **Performance Guarantees:** While hot-tier performance is maintained, throughput for cool data is reduced, which may impact access times for infrequently accessed data.

**Integration with Related Azure Services**  
- **Azure NetApp Files Ecosystem:** The enhancement is fully integrated with ANF, leveraging its existing management and monitoring tools.
- **Azure Data Management Solutions:** This feature can complement Azure data lifecycle and cost management strategies, especially when used alongside Azure services that classify or move data based on access patterns.

**Summary Sentence**  
Azure NetApp Files now offers a public preview of cool access enhancement on Premium and Ultra tiers, enabling automatic throughput adjustment for mixed hot and cool workloads to optimize performance and cost without manual intervention.

---

### 7. Retirement: Select Azure AI Language Features 

**Published**: April 01, 2026 18:00:10 UTC
**Link**: [Retirement: Select Azure AI Language Features ](https://azure.microsoft.com/updates?id=557394)

**Update ID**: 557394
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Azure AI Language, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of eight Azure AI Language features, effective March 20, 2027.

- Key changes or new features  
The following features will be retired and no longer supported after the retirement date:  
1. Key Phrase Extraction  
2. Sentiment Analysis and Opinion Mining  
3. Custom Text Classification  
4. Conversational Language Understanding (CLU)  
5. Custom Question Answering (CQA)  
6. Orchestrator (partial list; see link for full details)

No new features are being introduced; this is a deprecation notice.

- Target audience affected  
Developers and IT professionals using the affected Azure AI Language features in their applications, workflows, or services.

- Important notes if any  
- After March 20, 2027, these features will be unavailable and API calls will fail.  
- Microsoft recommends planning migration to alternative Azure AI services or solutions before the retirement date.  
- Review your current dependencies on these features and consult the official documentation for migration guidance.  
- Early planning is critical to avoid service disruption.

For more details and the full list of affected features, visit the official [Azure Update](https://azure.microsoft.com/updates?id=557394).

**Details**:

**Azure Update Report: Retirement of Select Azure AI Language Features**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of eight Azure AI Language features, effective March 20, 2027. This update is part of Microsoft’s ongoing strategy to streamline its AI offerings, focusing on evolving technologies and consolidating feature sets. The retirement aims to encourage customers to transition to newer, more advanced AI solutions within Azure, ensuring continued innovation and support.

**Specific Features and Detailed Changes**  
The following Azure AI Language features will be retired:

1. **Key Phrase Extraction**  
   Automatically identifies the most relevant phrases in a text document.
2. **Sentiment Analysis and Opinion Mining**  
   Determines sentiment (positive, negative, neutral) and extracts opinions from text.
3. **Custom Text Classification**  
   Enables users to build custom models for classifying text into user-defined categories.
4. **Conversational Language Understanding (CLU)**  
   Processes conversational input to extract intents and entities.
5. **Custom Question Answering (CQA)**  
   Allows creation of custom Q&A models based on user-provided data.
6. **Orchestrator**  
   Manages and routes language tasks across multiple AI models.

After March 20, 2027, these features will no longer be available in Azure. Customers using these features must plan migration strategies to alternative Azure AI services or update their applications accordingly.

**Technical Mechanisms and Implementation Methods**  
These features are currently accessed via Azure AI Language APIs, which provide REST endpoints for text analytics, classification, conversational understanding, and orchestration. Retirement means that API endpoints, SDKs, and related resources for these features will be deprecated and eventually removed from the Azure platform. Existing deployments, workflows, and integrations relying on these APIs will cease to function unless migrated to supported alternatives.

**Use Cases and Application Scenarios**  
The retiring features are commonly used in:

- **Document Analysis:** Extracting key phrases and sentiment from business documents, emails, and reports.
- **Customer Feedback Processing:** Analyzing sentiment and opinions in customer reviews and surveys.
- **Chatbots and Virtual Assistants:** Using CLU for intent detection and entity extraction in conversational interfaces.
- **Custom Content Moderation:** Employing custom text classification for automated moderation.
- **Enterprise Q&A Systems:** Implementing CQA for internal knowledge bases.
- **Multi-model AI Workflows:** Using Orchestrator to route tasks between language models.

Organizations leveraging these scenarios must evaluate alternative Azure AI services to maintain functionality.

**Important Considerations and Limitations**  
- **Migration Planning:** Users must identify affected workloads and plan migration before the retirement date.
- **API Deprecation:** Applications calling retired APIs will fail post-retirement.
- **Feature Availability:** No further updates or support will be provided for these features after retirement.
- **Data Handling:** Ensure data migration and compliance with organizational policies during transition.

**Integration with Related Azure Services**  
These features are often integrated with other Azure services such as Azure Cognitive Services, Azure Bot Service, Azure Functions, and Azure Logic Apps. Retirement may impact workflows that depend on these integrations. Customers should review documentation for alternative Azure AI offerings, such as newer Text Analytics, Language Studio, or custom AI models via Azure Machine Learning, to ensure continued interoperability.

**Summary Sentence**  
Microsoft will retire eight Azure AI Language features—including Key Phrase Extraction, Sentiment Analysis, Custom Text Classification, CLU, CQA, and Orchestrator—on March 20, 2027, requiring customers to migrate affected workloads to alternative Azure AI solutions to maintain application functionality.

---


*This report was automatically generated - 2026-04-02 03:04:27 UTC*