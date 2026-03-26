# March 26, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 26, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 8 items

## Update List

### 1. Generally Available: Cosmos DB Mirroring in Microsoft Fabric with private endpoints 

**Published**: March 25, 2026 20:00:39 UTC
**Link**: [Generally Available: Cosmos DB Mirroring in Microsoft Fabric with private endpoints ](https://azure.microsoft.com/updates?id=558836)

**Update ID**: 558836
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Features

**Summary**:

- What was updated  
Private endpoint support for Azure Cosmos DB Mirroring in Microsoft Fabric is now generally available.

- Key changes or new features  
Developers and IT professionals can now use private endpoints to securely connect Microsoft Fabric to Azure Cosmos DB when using the Mirroring feature. This enables secure, private network connectivity (via Azure Private Link) for analytics workloads on operational data, reducing exposure to the public internet and enhancing data security.

- Target audience affected  
Azure Cosmos DB users, Microsoft Fabric administrators, developers building analytics solutions, and IT professionals managing data security and network configurations.

- Important notes if any  
Enabling private endpoints helps organizations meet strict security and compliance requirements by ensuring data traffic remains within the Azure backbone network. This update allows seamless integration of operational and analytical workloads without compromising network security. Existing Cosmos DB Mirroring setups can now be enhanced with private endpoints; configuration may require updates to network and DNS settings.

[Read more on the official update page.](https://azure.microsoft.com/updates?id=558836)

**Details**:

**Background and Purpose of the Update**  
This update announces the general availability of private endpoint support for Azure Cosmos DB Mirroring in Microsoft Fabric. The primary purpose is to enhance network security for organizations leveraging Cosmos DB Mirroring within Microsoft Fabric by enabling private connectivity, thus allowing secure analytics on operational data without exposing resources to the public internet.

**Specific Features and Detailed Changes**  
With this release, users can now configure private endpoints for Cosmos DB Mirroring in Microsoft Fabric. This means that data traffic between Microsoft Fabric and Azure Cosmos DB can traverse a secure, private Azure network path rather than the public internet. This update enables organizations to maintain a strong security posture while performing analytics on their operational data mirrored from Azure Cosmos DB.

**Technical Mechanisms and Implementation Methods**  
Private endpoints in Azure are network interfaces that connect you privately and securely to a service powered by Azure Private Link. When private endpoint support is enabled for Cosmos DB Mirroring in Microsoft Fabric, the mirrored data is accessed over a private IP address within your Azure Virtual Network (VNet). This ensures that data in transit remains within the Azure backbone network, minimizing exposure to potential threats from the public internet. The implementation involves configuring private endpoints for both the source Cosmos DB account and the Microsoft Fabric workspace, ensuring that all data synchronization and analytics operations are routed securely via Azure Private Link.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in finance, healthcare, or government sectors that require strict data access controls can now mirror Cosmos DB data into Microsoft Fabric for analytics without violating compliance requirements.
- **Enterprise Security:** Enterprises with stringent network security policies can leverage this feature to prevent data exfiltration risks by ensuring all analytics traffic remains within their private Azure network.
- **Operational Analytics:** Teams can perform advanced analytics on operational data from Cosmos DB using Microsoft Fabric’s analytics capabilities while ensuring that data never leaves the trusted network boundary.

**Important Considerations and Limitations**  
- **Configuration Complexity:** Setting up private endpoints requires proper configuration of Azure VNets, DNS, and network security groups to ensure seamless and secure connectivity.
- **Network Costs:** Using private endpoints may incur additional network costs associated with Azure Private Link.
- **Access Control:** Ensure that only authorized users and services within the VNet can access the private endpoint, as misconfiguration could inadvertently expose data.
- **Service Limits:** Be aware of any service-specific limitations regarding the number of private endpoints or throughput when using Cosmos DB Mirroring with private endpoints.

**Integration with Related Azure Services**  
This update strengthens integration between Azure Cosmos DB, Microsoft Fabric, and Azure networking services such as Private Link and Virtual Networks. It allows organizations to build end-to-end secure analytics pipelines, leveraging Cosmos DB as the operational data store, Microsoft Fabric for analytics, and Azure networking for secure data transport.

**Summary Sentence**  
Private endpoint support for Azure Cosmos DB Mirroring in Microsoft Fabric is now generally available, enabling secure, private analytics on operational data while maintaining enhanced network security.

---

### 2. Public Preview: Blue-green agent pool upgrade in AKS 

**Published**: March 25, 2026 20:00:39 UTC
**Link**: [Public Preview: Blue-green agent pool upgrade in AKS ](https://azure.microsoft.com/updates?id=557862)

**Update ID**: 557862
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now offers a public preview of blue-green agent pool upgrades.

- Key changes or new features  
This update introduces blue-green upgrade support for AKS node pools. Instead of upgrading nodes in-place, AKS creates a parallel (green) node pool with the desired configuration. Workloads can be validated on the new pool before traffic is shifted from the existing (blue) pool. This approach reduces upgrade risks and allows for easy rollback if issues are detected.

- Target audience affected  
AKS cluster administrators, DevOps engineers, and developers managing Kubernetes workloads on Azure.

- Important notes if any  
The blue-green upgrade process provides a safer and more controlled upgrade path for AKS node pools, minimizing downtime and disruption. It is currently in public preview, so it is not recommended for production workloads yet. Users should review AKS documentation for limitations and best practices before adoption.

For more details, see the [official update](https://azure.microsoft.com/updates?id=557862).

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Blue-green agent pool upgrade in AKS  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=557862)

---

### Background and Purpose of the Update

Traditionally, in-place node pool upgrades in Azure Kubernetes Service (AKS) apply updates directly to existing nodes within a running environment. This process can introduce operational risk, as any misconfiguration or failure during the upgrade may impact live workloads. The blue-green agent pool upgrade feature addresses this risk by enabling a safer, more controlled upgrade path for AKS node pools.

---

### Specific Features and Detailed Changes

- **Blue-Green Upgrade Process:** Instead of upgrading nodes in place, AKS now supports creating a parallel (green) node pool with the desired new configuration, while the original (blue) node pool continues to run the current workloads.
- **Validation Before Cutover:** The new node pool can be validated independently, allowing IT teams to test and ensure the new configuration meets requirements before shifting production workloads.
- **Controlled Workload Transition:** Once validation is complete, workloads can be migrated from the blue (original) node pool to the green (new) node pool, minimizing downtime and reducing the risk of disruption.
- **Rollback Capability:** If issues are detected during validation or after migration, workloads can remain on or be reverted to the original node pool, providing a clear rollback path.

---

### Technical Mechanisms and Implementation Methods

- **Parallel Node Pool Creation:** During an upgrade, AKS provisions a new agent pool (green) alongside the existing one (blue), with the updated configuration (such as a new Kubernetes version or VM size).
- **Workload Migration:** After successful validation, workloads are shifted from the blue to the green node pool, typically using Kubernetes deployment strategies (e.g., rolling updates or re-scheduling pods).
- **Resource Management:** Both node pools coexist temporarily, requiring sufficient cluster resources and quota to accommodate the additional nodes during the upgrade window.

---

### Use Cases and Application Scenarios

- **Production Cluster Upgrades:** Enterprises can use blue-green upgrades to minimize risk when updating critical production clusters, ensuring new node configurations are validated before impacting live services.
- **Testing New Configurations:** Teams can test new Kubernetes versions, OS patches, or VM SKUs in the green pool, validating compatibility and performance before cutover.
- **Regulatory Compliance:** Organizations with strict change control requirements can use this feature to document and validate upgrades in a controlled manner.

---

### Important Considerations and Limitations

- **Resource Requirements:** Temporary duplication of node pools increases resource consumption and may require quota adjustments.
- **Operational Complexity:** Managing multiple node pools and orchestrating workload migration adds operational steps compared to in-place upgrades.
- **Preview Feature:** As this is a public preview, it may not be suitable for all production workloads and may lack full support or integration with all AKS features.

---

### Integration with Related Azure Services

- **Azure Monitor and Log Analytics:** Use these services to monitor both blue and green node pools during validation and migration.
- **Azure Policy:** Enforce compliance and configuration policies across both node pools.
- **Azure DevOps and CI/CD Pipelines:** Integrate blue-green upgrades into automated deployment workflows for continuous delivery and zero-downtime upgrades.

---

**Summary:**  
The blue-green agent pool upgrade feature in AKS (public preview) enables safer, parallel node pool upgrades by allowing validation of new configurations before shifting workloads, reducing operational risk and providing a clear rollback path.

---

### 3. Public Preview: Fabric Mirroring integration for Azure Database for MySQL 

**Published**: March 25, 2026 17:45:33 UTC
**Link**: [Public Preview: Fabric Mirroring integration for Azure Database for MySQL ](https://azure.microsoft.com/updates?id=558841)

**Update ID**: 558841
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure Database for MySQL, Features

**Summary**:

- What was updated  
Public preview of Fabric Mirroring integration for Azure Database for MySQL – Flexible Server.

- Key changes or new features  
Developers and IT professionals can now replicate MySQL operational data into Microsoft Fabric in near real time. This integration eliminates the need to build or maintain custom ETL pipelines, streamlining data movement from Azure Database for MySQL to Microsoft Fabric. The mirroring process is managed natively, enabling faster and more reliable data synchronization for analytics and reporting.

- Target audience affected  
Developers, data engineers, and IT professionals who manage data integration, analytics, or reporting workflows using Azure Database for MySQL and Microsoft Fabric.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. Users can leverage this integration to simplify data replication scenarios and accelerate time-to-insight. Review the official documentation for setup instructions, supported scenarios, and any preview limitations.  

[Learn more](https://azure.microsoft.com/updates?id=558841)

**Details**:

**Background and Purpose of the Update**  
This Azure update introduces the public preview of Fabric Mirroring integration for Azure Database for MySQL – Flexible Server. The primary goal is to enable seamless replication of MySQL operational data into Microsoft Fabric environments in near real time. This integration is designed to eliminate the need for building or maintaining custom ETL (Extract, Transform, Load) pipelines, thereby simplifying data movement and accelerating analytics workflows.

**Specific Features and Detailed Changes**  
- **Fabric Mirroring Integration:** Azure Database for MySQL – Flexible Server now supports direct integration with Microsoft Fabric through Fabric Mirroring.
- **Near Real-Time Data Replication:** MySQL operational data can be mirrored into Microsoft Fabric with minimal latency, supporting up-to-date analytics and reporting.
- **No ETL Pipeline Maintenance:** Users are not required to develop or manage separate ETL processes, reducing operational overhead and complexity.

**Technical Mechanisms and Implementation Methods**  
- **Data Replication:** The integration leverages Fabric Mirroring to continuously replicate changes from the MySQL database to Microsoft Fabric.
- **Operational Simplicity:** The process abstracts away the traditional ETL steps, providing a managed and automated data movement solution.
- **Preview Availability:** As this is a public preview, the feature is available for evaluation and testing in supported regions and configurations.

**Use Cases and Application Scenarios**  
- **Operational Analytics:** Organizations can perform near real-time analytics on MySQL data using Microsoft Fabric’s analytical capabilities without delay.
- **Reporting and Dashboards:** IT teams can build up-to-date dashboards and reports that reflect the latest MySQL data, supporting business intelligence initiatives.
- **Data Consolidation:** Enterprises can centralize MySQL data within Microsoft Fabric for unified analytics alongside other data sources.

**Important Considerations and Limitations**  
- **Preview Feature:** As this integration is in public preview, it may not be suitable for production workloads and could be subject to changes or limitations.
- **Supported Environments:** The feature is specific to Azure Database for MySQL – Flexible Server and may have regional or configuration constraints.
- **No ETL Customization:** While the removal of ETL pipelines simplifies operations, it may limit advanced transformation or data cleansing options typically available in custom ETL solutions.

**Integration with Related Azure Services**  
- **Microsoft Fabric:** The integration is tightly coupled with Microsoft Fabric, enabling users to leverage Fabric’s analytics and data processing capabilities.
- **Azure Database for MySQL – Flexible Server:** The source database is Azure’s managed MySQL offering, ensuring compatibility and managed service benefits.
- **Azure Data Ecosystem:** This feature complements other Azure data integration and analytics services by streamlining data ingestion into Microsoft Fabric.

**Summary Sentence**  
The public preview of Fabric Mirroring integration for Azure Database for MySQL – Flexible Server enables near real-time replication of MySQL operational data into Microsoft Fabric, streamlining analytics and reporting workflows by eliminating the need for custom ETL pipelines.

---

### 4. Public Preview: Azure SQL Managed Instance change event streaming 

**Published**: March 25, 2026 17:30:45 UTC
**Link**: [Public Preview: Azure SQL Managed Instance change event streaming ](https://azure.microsoft.com/updates?id=558884)

**Update ID**: 558884
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Features

**Summary**:

- What was updated  
Azure SQL Managed Instance now supports change event streaming (CES) to Azure Event Hubs in public preview.

- Key changes or new features  
You can stream row-level data changes—including inserts, updates, and deletes—from Azure SQL Managed Instance directly to Azure Event Hubs in near real time. Changes are published as transactions commit, minimizing latency and reducing the need for custom polling or ETL solutions. This enables seamless integration with downstream analytics, monitoring, or event-driven applications.

- Target audience affected  
Developers building real-time data pipelines, analytics solutions, or event-driven architectures; IT professionals managing data integration, replication, or monitoring between SQL Managed Instance and other Azure services.

- Important notes if any  
This feature is currently in public preview and may not be suitable for production workloads. It simplifies real-time data movement but requires configuration of both SQL Managed Instance and Event Hubs. Review preview limitations and pricing implications before adoption.

[More details](https://azure.microsoft.com/updates?id=558884)

**Details**:

**Azure Update Report: Public Preview – Azure SQL Managed Instance Change Event Streaming**

**Background and Purpose of the Update**  
This update introduces change event streaming (CES) for Azure SQL Managed Instance, enabling the streaming of row-level data changes—specifically inserts, updates, and deletes—to Azure Event Hubs in near real time. The primary purpose is to facilitate low-latency, scalable integration between transactional SQL data and downstream event-driven architectures or analytics platforms. By publishing changes as transactions commit, the solution minimizes latency and supports modern data processing requirements.

**Specific Features and Detailed Changes**  
- **Row-Level Change Streaming:** CES allows for the capture and streaming of individual row changes (inserts, updates, deletes) as they occur within Azure SQL Managed Instance.
- **Near Real-Time Delivery:** Changes are published to Azure Event Hubs immediately upon transaction commit, ensuring minimal delay between data modification and downstream consumption.
- **Event Hub Integration:** The update provides native connectivity to Azure Event Hubs, enabling seamless event ingestion for further processing or integration with other Azure services.

**Technical Mechanisms and Implementation Methods**  
- **Change Tracking:** CES leverages internal mechanisms within Azure SQL Managed Instance to detect and capture row-level changes as part of transaction processing.
- **Event Publication:** Upon transaction commit, the detected changes are formatted as events and pushed to Azure Event Hubs, which acts as a scalable event ingestion and distribution platform.
- **Streaming Architecture:** The solution is designed for high-throughput, low-latency streaming, supporting real-time data pipelines and event-driven workflows.

**Use Cases and Application Scenarios**  
- **Real-Time Analytics:** Stream SQL data changes to analytics platforms for up-to-the-minute insights and dashboards.
- **Data Synchronization:** Enable near real-time synchronization between SQL databases and other systems or services.
- **Event-Driven Applications:** Trigger business logic or workflows in response to database changes, such as updating caches or sending notifications.
- **Data Lake Ingestion:** Feed data changes directly into Azure Data Lake or other storage solutions for further processing.

**Important Considerations and Limitations**  
- **Latency:** While CES minimizes latency by publishing changes as transactions commit, actual end-to-end latency may depend on Event Hub throughput and downstream processing.
- **Data Scope:** Only inserts, updates, and deletes are streamed; schema changes or other database events are not included.
- **Preview Limitations:** As this feature is in public preview, it may be subject to changes, limited support, or restrictions on scalability and reliability.
- **Security and Compliance:** Ensure proper configuration of Event Hubs and SQL Managed Instance to maintain data security and compliance with organizational policies.

**Integration with Related Azure Services**  
- **Azure Event Hubs:** Acts as the primary destination for change events, supporting integration with Azure Stream Analytics, Azure Functions, and custom event consumers.
- **Azure Data Lake, Azure Synapse Analytics:** CES enables real-time data ingestion into analytics and storage platforms for further processing.
- **Azure Functions and Logic Apps:** Event-driven applications can consume change events to trigger workflows or business logic.

**Summary Sentence**  
Azure SQL Managed Instance now supports streaming row-level data changes to Azure Event Hubs in near real time, enabling low-latency integration with event-driven architectures and analytics platforms through change event streaming in public preview.

---

### 5. Generally Available: Custom time zone support for pg_cron via cron.timezone in Azure Database for PostgreSQL 

**Published**: March 25, 2026 17:30:45 UTC
**Link**: [Generally Available: Custom time zone support for pg_cron via cron.timezone in Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=558870)

**Update ID**: 558870
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Custom time zone support for pg_cron is now generally available in Azure Database for PostgreSQL. You can now configure the cron.timezone server parameter.

- Key changes or new features  
The new cron.timezone parameter allows you to set the time zone used by pg_cron for scheduled jobs. Previously, pg_cron jobs always used the database server’s time zone, but now you can specify a custom time zone for job evaluation and execution. This enables more flexible and region-specific scheduling for automated tasks.

- Target audience affected  
Developers and IT professionals who use Azure Database for PostgreSQL and rely on pg_cron for scheduling maintenance, data processing, or other automated jobs.

- Important notes if any  
Changing the cron.timezone parameter affects all pg_cron jobs on the server. Ensure that scheduled job timings are reviewed and updated as needed to align with the new time zone setting. This feature helps support global applications with region-specific scheduling requirements.

For more details, see the official update: https://azure.microsoft.com/updates?id=558870

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Custom time zone support for pg_cron via cron.timezone in Azure Database for PostgreSQL  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=558870)

---

**Background and Purpose of the Update**  
Azure Database for PostgreSQL provides managed PostgreSQL database services, including support for the pg_cron extension, which enables scheduling of database jobs. Previously, scheduled jobs using pg_cron operated based on the server’s default time zone, which could lead to discrepancies for global teams or applications requiring job execution aligned with specific local times. The purpose of this update is to introduce flexibility by allowing users to modify the time zone used by pg_cron, ensuring scheduled jobs run according to the desired local time zone.

---

**Specific Features and Detailed Changes**  
The update introduces the ability to configure the `cron.timezone` server parameter in Azure Database for PostgreSQL. This parameter directly controls the time zone reference for pg_cron job scheduling. Users can now set `cron.timezone` to any valid time zone supported by PostgreSQL, such as 'UTC', 'America/New_York', or 'Asia/Kolkata'. This change enables jobs scheduled via pg_cron to be evaluated and executed according to the specified time zone, rather than the server’s default.

---

**Technical Mechanisms and Implementation Methods**  
- The `cron.timezone` parameter is a server-level setting that can be modified through the Azure portal, Azure CLI, or ARM templates.
- When a user sets the `cron.timezone` parameter, pg_cron internally uses this value to interpret the timing of scheduled jobs.
- The parameter is applied immediately or after a server restart, depending on the configuration method and the underlying PostgreSQL version.
- The mechanism leverages PostgreSQL’s built-in time zone support, ensuring compatibility with standard time zone identifiers.

---

**Use Cases and Application Scenarios**  
- **Global Applications:** Organizations operating in multiple regions can schedule maintenance, backups, or data processing jobs to run at local business hours, improving operational alignment.
- **Compliance and Reporting:** Businesses with regulatory requirements to execute jobs at specific local times can ensure adherence by configuring the appropriate time zone.
- **Daylight Saving Adjustments:** By setting the time zone to one that observes daylight saving, scheduled jobs will automatically adjust without manual intervention.
- **Multi-Tenant Solutions:** SaaS providers can align job execution for tenants based on their respective time zones, enhancing user experience.

---

**Important Considerations and Limitations**  
- The `cron.timezone` parameter affects all pg_cron jobs on the server; individual jobs cannot have separate time zones.
- Only valid PostgreSQL time zone identifiers are supported; incorrect values will result in errors.
- Changes to `cron.timezone` may require a server restart, depending on the configuration method.
- Existing jobs scheduled before changing the time zone will execute according to the new setting, which may impact job timing.
- This feature is available only for Azure Database for PostgreSQL instances with pg_cron enabled.

---

**Integration with Related Azure Services**  
- The update is fully compatible with Azure Database for PostgreSQL’s managed service features, including automated backups, monitoring, and scaling.
- Integration with Azure CLI and ARM templates allows for automated deployment and configuration of the `cron.timezone` parameter as part of infrastructure-as-code workflows.
- Scheduled jobs can interact with other Azure services (e.g., Azure Storage, Azure Functions) via PostgreSQL extensions and custom scripts, ensuring time zone alignment across workflows.

---

**Summary Sentence**  
Azure Database for PostgreSQL now supports custom time zone configuration for pg_cron scheduled jobs via the cron.timezone parameter, enabling precise control over job execution timing to match local requirements and operational needs.

---

### 6. Generally Available: PostgreSQL migration service supports compatible EDB workloads into Azure Database for PostgreSQL 

**Published**: March 25, 2026 17:30:45 UTC
**Link**: [Generally Available: PostgreSQL migration service supports compatible EDB workloads into Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=558865)

**Update ID**: 558865
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL migration service now supports migrations from EDB PostgreSQL (including EDB Postgres Extended Server) to Azure Database for PostgreSQL.

- Key changes or new features  
Developers and IT professionals can now securely and reliably migrate EDB PostgreSQL workloads to Azure Database for PostgreSQL. This update enables consolidation of PostgreSQL estates, including those running on EDB Postgres Extended Server, using Azure’s migration workflows.

- Target audience affected  
This update is relevant for database administrators, IT professionals, and developers managing EDB PostgreSQL databases who are planning to move workloads to Azure Database for PostgreSQL.

- Important notes if any  
The migration service supports secure and reliable workflows, helping organizations streamline their move to Azure. Ensure compatibility and review migration prerequisites before starting. This feature is generally available, so it is recommended for production use.

For more details, see the official update:  
https://azure.microsoft.com/updates?id=558865

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: PostgreSQL migration service supports compatible EDB workloads into Azure Database for PostgreSQL  
**Source:** [Azure Updates](https://azure.microsoft.com/updates?id=558865)

---

### Background and Purpose of the Update

This update announces the general availability of support for migrating EDB PostgreSQL workloads into Azure Database for PostgreSQL. The primary objective is to enable organizations to seamlessly migrate and consolidate their PostgreSQL estates, specifically those running on EDB Postgres Extended Server, into Azure’s managed PostgreSQL platform. This enhancement addresses the need for secure, reliable, and streamlined migration workflows for enterprises leveraging EDB PostgreSQL in their on-premises or other cloud environments.

---

### Specific Features and Detailed Changes

- **EDB PostgreSQL as a Supported Source:** The migration service now officially supports EDB Postgres Extended Server as a source database for migrations into Azure Database for PostgreSQL.
- **Consolidation Capabilities:** Organizations can consolidate multiple PostgreSQL workloads, including those from EDB Postgres Extended Server, into Azure’s managed database service.
- **Secure and Reliable Migration Workflows:** The migration process is designed to ensure data security and reliability, aligning with enterprise requirements for mission-critical database migrations.

---

### Technical Mechanisms and Implementation Methods

- **Migration Service Integration:** The update leverages Azure’s PostgreSQL migration service, which orchestrates the end-to-end migration process from EDB Postgres Extended Server to Azure Database for PostgreSQL.
- **Workflow Automation:** The migration service provides automated workflows to handle schema and data transfer, minimizing manual intervention and reducing the risk of errors.
- **Security Protocols:** Secure migration channels and protocols are used to protect data in transit during the migration process.
- **Reliability Features:** The service incorporates mechanisms for data validation and consistency checks to ensure the integrity of migrated data.

---

### Use Cases and Application Scenarios

- **Cloud Modernization:** Enterprises running EDB Postgres Extended Server on-premises or in other clouds can now migrate to Azure Database for PostgreSQL to benefit from a fully managed, scalable, and secure database platform.
- **Database Consolidation:** Organizations with distributed PostgreSQL workloads can consolidate them into Azure, simplifying management and reducing operational overhead.
- **Business Continuity and Disaster Recovery:** The migration service can be used as part of a broader strategy to enhance business continuity by moving critical workloads to Azure’s resilient infrastructure.

---

### Important Considerations and Limitations

- **Source Compatibility:** Only compatible EDB Postgres Extended Server workloads are supported as sources for migration. Ensure your source environment meets the compatibility requirements outlined by Azure.
- **Migration Scope:** The service is designed for migration into Azure Database for PostgreSQL; it does not support migrations to other Azure database offerings.
- **Workflow Limitations:** The migration workflows are tailored for EDB Postgres Extended Server to Azure Database for PostgreSQL scenarios. Custom configurations or unsupported extensions may require additional validation.

---

### Integration with Related Azure Services

- **Azure Database for PostgreSQL:** The migration targets Azure’s managed PostgreSQL service, enabling integration with other Azure data and analytics services post-migration.
- **Security and Compliance:** The migration service aligns with Azure’s security and compliance frameworks, facilitating secure data transfer and governance.
- **Automation and Monitoring:** Post-migration, organizations can leverage Azure’s automation, monitoring, and management tools to optimize and maintain their PostgreSQL workloads.

---

**Summary:**  
Azure Database for PostgreSQL now supports secure, reliable migration of compatible EDB Postgres Extended Server workloads, enabling organizations to consolidate and modernize their PostgreSQL estates using Azure’s managed database platform.

---

### 7. Generally Available: PostgreSQL migration service supports for Google AlloyDB into Azure Database for PostgreSQL 

**Published**: March 25, 2026 17:30:45 UTC
**Link**: [Generally Available: PostgreSQL migration service supports for Google AlloyDB into Azure Database for PostgreSQL ](https://azure.microsoft.com/updates?id=558851)

**Update ID**: 558851
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL migration service now generally supports migrations from Google AlloyDB.

- Key changes or new features  
Google AlloyDB can now be used as a source for migrating PostgreSQL workloads directly into Azure Database for PostgreSQL. This update enables secure and reliable migration workflows, allowing organizations to consolidate their PostgreSQL databases from Google AlloyDB to Azure. The migration service supports minimal downtime and is designed to handle enterprise-scale migrations efficiently.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals managing PostgreSQL workloads who are planning to move databases from Google AlloyDB to Azure Database for PostgreSQL.

- Important notes if any  
Ensure compatibility between the source (Google AlloyDB) and target (Azure Database for PostgreSQL) versions before migration. Review Azure’s migration documentation for best practices and prerequisites. This feature streamlines cloud migration projects, especially for organizations consolidating multi-cloud PostgreSQL estates into Azure. For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=558851).

**Details**:

**Background and Purpose of the Update**

This update announces the general availability of support for Google AlloyDB as a source in Azure’s PostgreSQL migration service. The primary purpose is to enable organizations to migrate and consolidate their PostgreSQL workloads from Google AlloyDB to Azure Database for PostgreSQL. This enhancement addresses the need for seamless and secure migration paths for enterprises seeking to transition from Google Cloud’s managed PostgreSQL-compatible databases to Azure’s managed PostgreSQL offerings.

**Specific Features and Detailed Changes**

- **Source Support Expansion:** The migration service now officially supports Google AlloyDB as a source, in addition to existing PostgreSQL sources.
- **Workflow Enhancements:** The migration process leverages secure and reliable workflows, ensuring data integrity and minimizing downtime during migrations from AlloyDB to Azure Database for PostgreSQL.
- **Consolidation Capability:** Organizations can now consolidate their PostgreSQL estates, including those hosted on Google AlloyDB, into Azure, simplifying management and operational overhead.

**Technical Mechanisms and Implementation Methods**

- **Migration Workflow:** The migration service utilizes secure workflows, likely involving data extraction, transformation, and loading (ETL) processes tailored for compatibility between Google AlloyDB and Azure Database for PostgreSQL.
- **Security:** The migration process is designed to be secure, ensuring that data is transferred over encrypted channels and that access controls are maintained throughout the migration.
- **Reliability:** The workflows are built to be reliable, likely including mechanisms for error handling, retry logic, and validation to ensure successful and consistent data migration.

**Use Cases and Application Scenarios**

- **Cloud Platform Transition:** Enterprises moving workloads from Google Cloud to Azure can now migrate PostgreSQL databases from AlloyDB directly to Azure Database for PostgreSQL.
- **Database Estate Consolidation:** Organizations with multi-cloud PostgreSQL deployments can consolidate their databases on Azure, streamlining administration and reducing complexity.
- **Modernization Projects:** Businesses modernizing their data infrastructure can leverage this service to transition from Google AlloyDB to Azure’s managed PostgreSQL environment with minimal disruption.

**Important Considerations and Limitations**

- **Supported Source:** This update specifically adds support for Google AlloyDB as a migration source; other non-PostgreSQL sources are not covered.
- **Workflow Scope:** The details specify secure and reliable workflows but do not elaborate on advanced features such as online migration, minimal downtime, or support for complex schema transformations.
- **Migration Target:** The supported target is Azure Database for PostgreSQL. Migration to other Azure database services is not indicated in this update.
- **Service Availability:** The feature is generally available, meaning it is production-ready and supported by Azure.

**Integration with Related Azure Services**

- **Azure Database for PostgreSQL:** The migration service integrates directly with Azure’s managed PostgreSQL offering, enabling a streamlined transition.
- **Azure Security and Monitoring:** While not explicitly mentioned, migrations typically integrate with Azure’s security and monitoring tools to ensure compliance and operational visibility during and after migration.
- **Azure Migration Tools:** This update complements Azure’s broader suite of migration tools, providing a specialized path for PostgreSQL workloads from Google AlloyDB.

**Summary Sentence**

Google AlloyDB is now generally supported as a migration source for Azure Database for PostgreSQL, enabling secure and reliable workflows for organizations to migrate and consolidate their PostgreSQL workloads from Google Cloud to Azure.

---

### 8. Generally Available: Online migration now uses the pgoutput plugin 

**Published**: March 25, 2026 17:30:45 UTC
**Link**: [Generally Available: Online migration now uses the pgoutput plugin ](https://azure.microsoft.com/updates?id=558846)

**Update ID**: 558846
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Features

**Summary**:

- What was updated  
Azure Database for PostgreSQL online migration now uses the pgoutput plugin for logical replication.

- Key changes or new features  
The migration process now leverages PostgreSQL’s native pgoutput logical replication plugin, enhancing reliability and performance for online (minimal-downtime) migrations. This change improves compatibility with modern PostgreSQL deployments and tooling, aligning Azure’s migration process with the broader PostgreSQL ecosystem.

- Target audience affected  
Developers and IT professionals responsible for database migrations to Azure Database for PostgreSQL, especially those requiring minimal downtime and compatibility with PostgreSQL-native tools and workflows.

- Important notes if any  
Switching to pgoutput may require reviewing your migration workflows to ensure compatibility with the new logical replication method. This update is generally available, so it is recommended for all new online migrations. Existing migrations using older plugins may consider transitioning to benefit from improved performance and ecosystem alignment.

For more details, see the official update: https://azure.microsoft.com/updates?id=558846

**Details**:

**Azure Update: Generally Available – Online migration now uses the pgoutput plugin**

**Background and Purpose of the Update**  
This update introduces the use of the pgoutput plugin for online (minimal-downtime) migrations in Azure Database for PostgreSQL. The primary goal is to enhance migration reliability and performance by leveraging PostgreSQL’s native logical replication framework. This aligns Azure’s migration tooling with the standard mechanisms used in modern PostgreSQL deployments, improving compatibility and reducing friction during migration processes.

**Specific Features and Detailed Changes**  
- **pgoutput Plugin Integration:** Online migrations now utilize the pgoutput logical decoding plugin, which is the default logical replication output plugin in PostgreSQL.
- **Improved Reliability and Performance:** The adoption of pgoutput provides a more robust and performant migration experience, reducing downtime and increasing data consistency during migration.
- **Ecosystem Compatibility:** By aligning with PostgreSQL’s native logical replication, migrations are now more compatible with a broader range of PostgreSQL tools and extensions, facilitating smoother integration with existing PostgreSQL-based solutions.

**Technical Mechanisms and Implementation Methods**  
- **Logical Replication Framework:** The pgoutput plugin operates within PostgreSQL’s logical replication system, capturing and streaming changes (inserts, updates, deletes) from the source database to the target.
- **Minimal Downtime Migration:** The migration process involves setting up logical replication between the source and target PostgreSQL instances, keeping them synchronized until the cutover, thereby minimizing application downtime.
- **Native Protocols:** By using pgoutput, the migration process adheres to PostgreSQL’s native logical replication protocols, ensuring data integrity and compatibility.

**Use Cases and Application Scenarios**  
- **Production Database Migrations:** Organizations can migrate production PostgreSQL databases to Azure with minimal downtime, ensuring business continuity.
- **Cloud Modernization:** Enterprises modernizing their infrastructure by moving on-premises or self-hosted PostgreSQL databases to Azure Database for PostgreSQL can benefit from seamless, low-impact migrations.
- **Cross-Region or Cross-Instance Migrations:** The update supports scenarios where databases need to be moved across Azure regions or between different Azure PostgreSQL instances.

**Important Considerations and Limitations**  
- **Plugin Requirement:** Both source and target PostgreSQL instances must support the pgoutput plugin, which is available in PostgreSQL 10 and later.
- **Logical Replication Constraints:** Logical replication may not capture certain schema changes or DDL operations, so pre-migration planning is essential.
- **Version Compatibility:** Ensure that both source and target databases are compatible with the logical replication framework and the pgoutput plugin.

**Integration with Related Azure Services**  
- **Azure Database Migration Service (DMS):** The update is likely integrated with Azure DMS, which orchestrates the migration process and now leverages pgoutput for logical replication.
- **Azure Database for PostgreSQL:** The enhanced migration capability is directly applicable to Azure Database for PostgreSQL, facilitating migrations into this managed service.
- **Ecosystem Tools:** Improved compatibility with PostgreSQL-native tools and extensions allows for better integration with third-party migration and replication solutions.

**Summary Sentence:**  
Azure Database for PostgreSQL online migrations now use the pgoutput plugin, enabling minimal-downtime migrations with improved reliability, performance, and native PostgreSQL compatibility.

---


*This report was automatically generated - 2026-03-26 03:05:02 UTC*