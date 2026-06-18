# June 18, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 18, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: Azure Migrate – GitHub Copilot Modernization integration for at scale code assessments

**Published**: June 17, 2026 18:00:18 UTC
**Link**: [Public Preview: Azure Migrate – GitHub Copilot Modernization integration for at scale code assessments](https://azure.microsoft.com/updates?id=566145)

**Update ID**: 566145
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Migrate, Feature

**Summary**:

- What was updated  
Azure Migrate now integrates with GitHub Copilot Modernization (public preview) to enable large-scale code assessments as part of migration projects.

- Key changes or new features  
This integration combines Azure Migrate’s portfolio-level discovery and assessment capabilities with GitHub Copilot’s context-aware code analysis. Users can now perform automated, at-scale code assessments to identify modernization opportunities, technical debt, and migration blockers across multiple applications and repositories. The solution provides actionable insights to accelerate cloud migration and modernization efforts.

- Target audience affected  
This update is relevant for developers, IT professionals, and cloud architects involved in application modernization, migration planning, and portfolio assessments. Organizations managing large codebases or planning cloud migrations will benefit most.

- Important notes if any  
The integration is currently in public preview, so features and functionality may change before general availability. Users should evaluate the preview in non-production environments. Access to GitHub Copilot Modernization features may require appropriate GitHub licensing. For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=566145

**Details**:

**Azure Update Report**

**Title:** Public Preview: Azure Migrate – GitHub Copilot Modernization integration for at scale code assessments

**Background and Purpose of the Update:**  
This update introduces a public preview integration between Azure Migrate and GitHub Copilot Modernization, aimed at enhancing the modernization process for enterprise applications. The purpose is to streamline large-scale code assessments by combining Azure Migrate’s portfolio-level discovery and assessment capabilities with GitHub Copilot’s context-aware code analysis. This integration addresses the need for automated, scalable, and intelligent code evaluation during migration and modernization projects, reducing manual effort and improving accuracy.

**Specific Features and Detailed Changes:**  
- **Portfolio-Level Discovery:** Azure Migrate continues to provide comprehensive discovery of application portfolios, identifying workloads and dependencies across environments.
- **At Scale Code Insights:** The integration enables code assessments at scale, leveraging GitHub Copilot Modernization to analyze codebases efficiently.
- **Context-Aware Analysis:** GitHub Copilot Modernization offers advanced code analysis, understanding context to deliver actionable insights for modernization.
- **Unified Assessment Workflow:** Users can access code insights directly within Azure Migrate, facilitating a seamless workflow for migration planning and modernization.
- **Public Preview Availability:** The feature is currently in public preview, allowing IT professionals to evaluate and provide feedback on the integration.

**Technical Mechanisms and Implementation Methods:**  
- **Integration Layer:** Azure Migrate communicates with GitHub Copilot Modernization through API-driven mechanisms, enabling automated code analysis as part of the migration assessment process.
- **Data Flow:** Application portfolios discovered by Azure Migrate are passed to GitHub Copilot Modernization, which performs context-aware code analysis and returns modernization insights.
- **Assessment Output:** The results are presented within Azure Migrate’s assessment reports, providing detailed recommendations for code changes, modernization opportunities, and potential migration blockers.
- **Scalability:** The integration is designed to handle large-scale codebases, supporting enterprise-level migration scenarios.

**Use Cases and Application Scenarios:**  
- **Enterprise Application Modernization:** Organizations planning to migrate legacy applications to Azure can leverage this integration to assess code readiness and modernization needs at scale.
- **Portfolio Assessment:** IT teams managing multiple applications can utilize unified discovery and code analysis to prioritize modernization efforts.
- **Migration Planning:** The integration assists in identifying code-level challenges and opportunities, informing migration strategies and timelines.

**Important Considerations and Limitations:**  
- **Preview Status:** As the integration is in public preview, features may be subject to change and are not recommended for production environments.
- **Scope of Analysis:** The update focuses on code assessment and modernization insights; it does not perform code transformation or remediation.
- **Feedback Loop:** Users should provide feedback to Microsoft to influence future enhancements and stability.
- **Dependency on GitHub Copilot Modernization:** Successful code analysis requires access to GitHub Copilot Modernization, which may have its own prerequisites and licensing requirements.

**Integration with Related Azure Services:**  
- **Azure Migrate:** Serves as the primary platform for discovery and assessment, orchestrating the modernization workflow.
- **GitHub Copilot Modernization:** Acts as the code analysis engine, delivering context-aware insights.
- **Potential for Extended Integration:** While not specified in this update, the integration may complement other Azure services such as Azure DevOps and Azure App Service during migration and modernization processes.

**Summary Sentence:**  
Azure Migrate’s integration with GitHub Copilot Modernization in public preview enables scalable, context-aware code assessments, streamlining the modernization process for enterprise application portfolios and enhancing migration planning with actionable insights.

---

### 2. Generally Available: Azure Databricks native read access to Microsoft OneLake 

**Published**: June 17, 2026 18:00:18 UTC
**Link**: [Generally Available: Azure Databricks native read access to Microsoft OneLake ](https://azure.microsoft.com/updates?id=565733)

**Update ID**: 565733
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks now offers generally available native read access to data stored in Microsoft OneLake via Unity Catalog.

- Key changes or new features  
Developers and data teams can directly query and analyze data in Microsoft OneLake from Azure Databricks without the need to move or copy data. This integration leverages Unity Catalog for secure, unified data governance and access management. The update streamlines analytics workflows, reduces data duplication, and improves performance by enabling direct access to OneLake datasets.

- Target audience affected  
This update impacts data engineers, data scientists, and IT professionals using Azure Databricks and Microsoft OneLake for analytics, data engineering, and machine learning workloads.

- Important notes if any  
To use this feature, ensure your Azure Databricks workspace is enabled for Unity Catalog and that appropriate permissions are configured for OneLake access. This enhancement supports more efficient data lakehouse architectures and simplifies compliance and security management by centralizing access control through Unity Catalog.

For more details, see the official update: https://azure.microsoft.com/updates?id=565733

**Details**:

**Azure Update Technical Explanation: Azure Databricks Native Read Access to Microsoft OneLake (Generally Available)**

**Background and Purpose of the Update**  
This update introduces general availability for native read access from Azure Databricks to data stored in Microsoft OneLake, facilitated through Unity Catalog. The primary purpose is to streamline data analytics workflows by enabling direct querying and analysis of data in OneLake, eliminating the need for data movement or duplication. This enhancement supports organizations seeking to optimize data access patterns, reduce data latency, and simplify data governance across their analytics estate.

**Specific Features and Detailed Changes**  
- **Native Read Access:** Azure Databricks users can now directly access and read data stored in Microsoft OneLake without requiring intermediate data transfers or copies.
- **Unity Catalog Integration:** Access control and data governance are managed via Unity Catalog, ensuring consistent security and compliance policies when interacting with OneLake data.
- **General Availability:** This feature is now fully supported and recommended for production workloads.

**Technical Mechanisms and Implementation Methods**  
- **Direct Data Querying:** Databricks clusters, when configured with Unity Catalog, can connect to OneLake as a data source. This connection leverages native integration, ensuring optimized performance and compatibility.
- **Security and Governance:** Unity Catalog acts as the central layer for managing permissions, auditing, and cataloging of datasets accessed in OneLake, providing a unified governance model.
- **No Data Movement:** Data remains in OneLake throughout the analytics process, reducing complexity and potential inconsistencies associated with data duplication.

**Use Cases and Application Scenarios**  
- **Data Lake Analytics:** Organizations with large datasets in OneLake can leverage Databricks for scalable analytics, machine learning, and data engineering tasks without the overhead of data migration.
- **Unified Data Governance:** Enterprises requiring strict data access controls can benefit from Unity Catalog’s governance features while accessing OneLake data from Databricks.
- **Real-Time and Near-Real-Time Analytics:** Direct access enables faster insights by minimizing data latency, supporting scenarios such as dashboarding, reporting, and ad-hoc analysis.

**Important Considerations and Limitations**  
- **Unity Catalog Dependency:** Access is managed through Unity Catalog, so proper configuration and permissions are required for seamless operation.
- **Read Access Only:** The update specifically enables native read access; write-back or modification capabilities are not described in this release.
- **Supported Data Formats and Performance:** For optimal performance and compatibility, ensure that data stored in OneLake adheres to supported formats and best practices as recommended by Azure Databricks and OneLake documentation.

**Integration with Related Azure Services**  
- **Microsoft OneLake:** Serves as the centralized data lake storage, supporting multi-cloud and hybrid data scenarios.
- **Azure Databricks:** Provides the analytics and data engineering platform, now with direct connectivity to OneLake.
- **Unity Catalog:** Acts as the unified data governance and access management layer, ensuring secure and compliant access to OneLake datasets from Databricks.

**Summary**  
Azure Databricks now offers generally available native read access to Microsoft OneLake via Unity Catalog, enabling direct, secure, and governed data analytics without the need for data movement.

---

### 3. Public Preview: Azure Databricks natively storing data in Microsoft OneLake 

**Published**: June 17, 2026 18:00:18 UTC
**Link**: [Public Preview: Azure Databricks natively storing data in Microsoft OneLake ](https://azure.microsoft.com/updates?id=565706)

**Update ID**: 565706
**Data source**: Azure Updates API

**Categories**: In preview, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks now supports native writing of managed Delta tables directly to Microsoft OneLake, currently in public preview.

- Key changes or new features  
Developers and data teams can use OneLake as the unified storage layer for Azure Databricks workloads. This eliminates the need to manage separate storage accounts for Databricks data. Delta tables managed by Databricks can be stored directly in OneLake, streamlining data architecture and simplifying data management.

- Target audience affected  
This update is relevant for data engineers, developers, and IT professionals using Azure Databricks and Microsoft OneLake, especially those building data lakehouse solutions or managing large-scale analytics workloads.

- Important notes if any  
- The feature is in public preview and may not be recommended for production workloads yet.  
- This integration helps centralize data governance and security by leveraging OneLake’s unified storage capabilities.  
- Existing Databricks workloads can be migrated to use OneLake for storage, reducing operational overhead.  
- Review the official documentation for setup instructions and limitations during the preview phase.

For more details, visit: https://azure.microsoft.com/updates?id=565706

**Details**:

**Azure Update Report: Public Preview – Azure Databricks Natively Storing Data in Microsoft OneLake**

**Background and Purpose of the Update**  
This update introduces the capability for Azure Databricks to natively write managed Delta tables directly to Microsoft OneLake. The primary purpose is to streamline data storage for Databricks workloads by enabling OneLake as a unified storage layer. Traditionally, customers needed to manage separate storage accounts (such as Azure Data Lake Storage or Azure Blob Storage) for Databricks data. This update eliminates that requirement, simplifying data architecture and management.

**Specific Features and Detailed Changes**  
- Azure Databricks now supports native integration with Microsoft OneLake for writing managed Delta tables.
- Users can leverage OneLake as the default storage location for Databricks-managed tables, removing the need for manual configuration of external storage accounts.
- The integration supports managed Delta tables, which are Databricks’ optimized storage format for analytics workloads, providing ACID transactions and scalable metadata handling.

**Technical Mechanisms and Implementation Methods**  
- The integration is achieved by enabling Databricks clusters and workspaces to directly interface with OneLake APIs for data storage operations.
- When creating managed Delta tables, Databricks writes the underlying data files and metadata directly into OneLake, utilizing its native storage capabilities.
- This process abstracts storage management from the user, allowing seamless data access and management within Databricks without manual provisioning or connection of storage accounts.
- The implementation leverages Delta Lake’s transactional storage engine, ensuring data consistency and reliability within OneLake.

**Use Cases and Application Scenarios**  
- Enterprises seeking a unified data lake for analytics, machine learning, and reporting can use OneLake as the central repository for Databricks workloads.
- Organizations aiming to reduce operational overhead associated with managing multiple storage accounts benefit from simplified storage architecture.
- Data engineering teams can streamline ETL pipelines, data warehousing, and real-time analytics by consolidating data storage in OneLake.
- The integration supports scenarios where data needs to be shared or accessed across multiple Azure services, leveraging OneLake’s centralization.

**Important Considerations and Limitations**  
- The feature is currently in Public Preview, which may imply limited support, evolving functionality, and potential changes before general availability.
- Only managed Delta tables are supported for native OneLake storage; external tables or other formats may require separate configuration.
- Customers should review OneLake’s performance, scalability, and security features to ensure alignment with their workload requirements.
- Integration specifics, such as authentication, access control, and data governance, should be validated according to organizational policies.

**Integration with Related Azure Services**  
- OneLake serves as the unified storage layer, facilitating interoperability with other Azure analytics services such as Microsoft Fabric, Azure Synapse Analytics, and Power BI.
- Databricks users can leverage OneLake’s centralization to enable cross-service data sharing and analytics.
- The update enhances the Azure ecosystem by promoting seamless data flow and management between Databricks and other Azure services that utilize OneLake.

**Summary Sentence**  
Azure Databricks now supports native writing of managed Delta tables to Microsoft OneLake, enabling customers to use OneLake as a unified storage layer for Databricks workloads and simplifying data management by eliminating the need for separate storage accounts.

---

### 4. Generally Available: ICMP Support for Azure Standard V2 NAT Gateway

**Published**: June 17, 2026 16:30:04 UTC
**Link**: [Generally Available: ICMP Support for Azure Standard V2 NAT Gateway](https://azure.microsoft.com/updates?id=565487)

**Update ID**: 565487
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Azure NAT Gateway, Features, Services

**Summary**:

- What was updated  
Azure StandardV2 NAT Gateway now generally supports outbound ICMP Echo Request and Echo Reply traffic.

- Key changes or new features  
With this update, workloads behind a StandardV2 NAT Gateway can send and receive ICMP Echo (ping) traffic for outbound connections. This enables the use of common network troubleshooting tools like ping to validate outbound connectivity and diagnose network issues.

- Target audience affected  
This update is relevant for developers, network engineers, and IT professionals managing Azure workloads that use StandardV2 NAT Gateway for outbound internet access.

- Important notes if any  
Previously, outbound ICMP traffic was not supported, limiting troubleshooting options. Now, users can leverage ICMP-based tools for faster network diagnostics. This feature is generally available and does not require additional configuration for existing StandardV2 NAT Gateways.

For more details, see the official update: https://azure.microsoft.com/updates?id=565487

**Details**:

**Azure Update Report: Generally Available – ICMP Support for Azure Standard V2 NAT Gateway**

**Background and Purpose of the Update**  
The Azure StandardV2 NAT Gateway is a critical component for managing outbound connectivity from workloads deployed within Azure Virtual Networks. Historically, NAT Gateway did not support outbound ICMP (Internet Control Message Protocol) Echo Request and Echo Reply traffic, which limited the ability of IT professionals to use common network diagnostic tools such as ping. The purpose of this update is to enhance troubleshooting and connectivity validation capabilities by enabling outbound ICMP traffic, thereby improving operational efficiency and network visibility.

**Specific Features and Detailed Changes**  
With this update, Azure StandardV2 NAT Gateway now supports outbound ICMP Echo Request and Echo Reply traffic. This means that workloads behind the NAT Gateway can initiate ping operations to external endpoints and receive responses, facilitating real-time connectivity checks. The change specifically applies to the StandardV2 SKU of NAT Gateway, ensuring that outbound ICMP traffic is translated and routed correctly through the NAT Gateway, just as with TCP and UDP traffic.

**Technical Mechanisms and Implementation Methods**  
The NAT Gateway operates by translating private IP addresses of workloads within a Virtual Network to public IP addresses for outbound traffic. With the new ICMP support, the NAT Gateway now recognizes and processes ICMP Echo Request packets, performs address translation, and forwards them to the destination. When an Echo Reply is received, the gateway reverses the translation and delivers the response to the originating workload. This implementation ensures that ICMP traffic is handled securely and efficiently, maintaining the same level of isolation and scalability as other supported protocols.

**Use Cases and Application Scenarios**  
- **Network Troubleshooting:** IT professionals can use ping from workloads behind the NAT Gateway to verify connectivity to external resources, such as public IP addresses or internet endpoints.
- **Monitoring and Validation:** Automated scripts and monitoring tools that rely on ICMP can now be used to validate outbound network paths and detect connectivity issues.
- **Operational Diagnostics:** In scenarios where outbound connectivity is intermittent or failing, ICMP support allows for rapid diagnosis without requiring additional network configuration or exposing workloads directly to the internet.

**Important Considerations and Limitations**  
- The ICMP support is limited to Echo Request and Echo Reply types, which are used by ping. Other ICMP message types (such as Destination Unreachable or Time Exceeded) are not mentioned as supported in this update.
- The feature is available only for the StandardV2 NAT Gateway SKU; earlier versions or other NAT solutions may not provide this functionality.
- Security policies and NSG (Network Security Group) rules should be reviewed to ensure that outbound ICMP traffic is permitted as required.
- This update does not affect inbound ICMP traffic; only outbound connectivity from workloads behind the NAT Gateway is enhanced.

**Integration with Related Azure Services**  
The StandardV2 NAT Gateway is commonly used in conjunction with Azure Virtual Networks, Virtual Machines, and network security services such as NSGs and Azure Firewall. With ICMP support, these integrations remain seamless, allowing workloads to maintain secure outbound connectivity while benefiting from improved diagnostic capabilities. The update does not require changes to existing integrations, but administrators should ensure that relevant security rules allow outbound ICMP traffic.

**Summary Sentence**  
Azure StandardV2 NAT Gateway now supports outbound ICMP Echo Request and Echo Reply traffic, enabling IT professionals to use tools like ping for enhanced connectivity validation and network troubleshooting from workloads behind the NAT Gateway.

---


*This report was automatically generated - 2026-06-18 03:03:29 UTC*