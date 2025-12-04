# December 04, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: December 04, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 6 items

## Update List

### 1. Retirement: Remove dependency on these Azure ML SDKs before June 30, 2026

**Published**: December 03, 2025 21:00:12 UTC
**Link**: [Retirement: Remove dependency on these Azure ML SDKs before June 30, 2026](https://azure.microsoft.com/updates?id=501668)

**Update ID**: 501668
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Internet of Things, Azure Machine Learning, Retirements, Features

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Machine Learning SDK V1 and several associated SDK packages, effective June 30, 2026.

- Key changes or new features  
AzureML SDK V1 will reach end of life on June 30, 2026. Alongside this, the following SDKs that depend on SDK V1 will also be retired: azureml-train-core, azureml-pipeline, azureml-pipeline-core, azureml-pipeline-internal, and azureml-pipeline-steps. Developers must migrate to the latest Azure ML SDK V2 to continue receiving support and updates.

- Target audience affected  
Developers and IT professionals who build, deploy, or maintain machine learning workflows using Azure Machine Learning SDK V1 and its related pipeline and training SDKs.

- Important notes if any  
Migration to Azure ML SDK V2 is strongly recommended well before the retirement date to avoid disruption. SDK V2 offers improved functionality, better integration, and ongoing support. Review existing codebases and pipelines to identify dependencies on the retiring SDKs and plan migration accordingly. For detailed guidance, refer to the official Azure ML migration documentation.

**Details**:

The Azure update announces the planned retirement of Azure Machine Learning SDK V1 and its associated SDK components—azureml-train-core, azureml-pipeline, azureml-pipeline-core, azureml-pipeline-internal, and azureml-pipeline-steps—effective June 30, 2026. This deprecation mandates that IT professionals and data scientists migrate their machine learning workflows to the newer Azure ML SDK V2 or alternative supported frameworks well before this deadline to ensure uninterrupted service and access to the latest features.

**Background and Purpose:**  
Azure ML SDK V1 has been foundational for building, training, and deploying machine learning models on Azure. However, with evolving cloud-native architectures and the need for more streamlined, scalable, and maintainable ML pipelines, Microsoft introduced Azure ML SDK V2. The retirement aims to consolidate development efforts around the newer SDK, which offers improved performance, enhanced usability, and better integration with modern Azure services. This transition encourages adoption of updated APIs and tooling that align with current best practices in MLOps.

**Specific Features and Detailed Changes:**  
The retiring SDKs include core training libraries and pipeline components that enable model training orchestration and pipeline construction in SDK V1. These components facilitated defining pipeline steps, managing dependencies, and executing workflows on Azure ML compute targets. With retirement, these packages will no longer receive updates or support, and their APIs may cease functioning post end-of-life. The new SDK V2 introduces a redesigned pipeline SDK with declarative YAML-based pipeline definitions, improved modularity, and enhanced CLI and Python SDK support, enabling more flexible and maintainable pipeline management.

**Technical Mechanisms and Implementation Methods:**  
Migration involves refactoring existing Python codebases that depend on the deprecated SDKs. Developers need to replace SDK V1 pipeline constructs with SDK V2 equivalents, which leverage a more declarative approach and support richer pipeline orchestration features. The SDK V2 uses REST APIs under the hood with better versioning and backward compatibility. Additionally, SDK V2 supports integration with Azure DevOps, GitHub Actions, and other CI/CD tools more seamlessly. Implementation requires reviewing pipeline step definitions, data input/output handling, and compute target configurations to align with SDK V2 paradigms.

**Use Cases and Application Scenarios:**  
This update primarily impacts organizations running production ML workflows on Azure ML that rely on SDK V1 for model training, pipeline orchestration, and deployment automation. Use cases include automated retraining pipelines, batch scoring jobs, and complex multi-step workflows involving data preprocessing, model training, validation, and deployment. Migrating to SDK V2 ensures continued support for these scenarios with enhanced capabilities such as pipeline versioning, parameterization, and easier reproducibility.

**Important Considerations and Limitations:**  
- Migration requires thorough testing to validate that pipelines behave identically post-transition.  
- Some SDK V1 features may have changed or been deprecated in SDK V2, necessitating code adjustments.  
- Existing pipeline artifacts and metadata may need conversion or recreation.  
- Teams should plan migration well ahead of the June 30, 2026 deadline to avoid disruption.  
- Documentation and training on SDK V2 should be incorporated into team workflows.  
- Legacy systems tightly coupled with SDK V1 may require significant refactoring.

**Integration with Related Azure Services:**  
The SDK V2 enhances integration with Azure services such as Azure DevOps for CI/CD pipelines, Azure Data Factory for data orchestration, and Azure Monitor for pipeline telemetry and logging. It also supports improved interaction with Azure Kubernetes Service (AKS) for scalable model deployment and Azure Container Registry (ACR) for containerized model images. The updated SDK aligns with Azure’s broader push towards infrastructure-as-code and GitOps methodologies, enabling more robust and automated ML lifecycle management.

In summary, the announced retirement of Azure ML SDK V1 and its associated pipeline SDKs by June 30, 2026, signals a strategic shift towards the modernized Azure ML SDK V2, requiring

---

### 2. Generally Available: Azure Database for PostgreSQL Flexible Server in Belgium Central 

**Published**: December 03, 2025 17:30:15 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL Flexible Server in Belgium Central ](https://azure.microsoft.com/updates?id=534523)

**Update ID**: 534523
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server is now generally available in the Belgium Central Azure region.

- Key changes or new features  
This update enables customers to deploy fully managed PostgreSQL Flexible Server instances closer to their users in Belgium Central, improving latency and compliance with regional data residency requirements. Flexible Server offers enhanced control over server configuration, high availability options, and cost-optimized burstable compute tiers.

- Target audience affected  
Developers and IT professionals managing PostgreSQL workloads who require regional deployment in Belgium for performance, compliance, or data sovereignty reasons. Enterprises and ISVs targeting European customers will benefit from reduced latency and localized data storage.

- Important notes if any  
Existing Flexible Server features such as zone-redundant high availability, stop/start capabilities, and custom maintenance windows are available in this region. Users should consider network architecture and backup strategies aligned with regional deployment. For detailed pricing and service limits, refer to the official Azure documentation.

**Details**:

The recent general availability of Azure Database for PostgreSQL Flexible Server in the Belgium Central region expands Azure’s global footprint, enabling customers in or near Belgium to deploy managed PostgreSQL instances with reduced latency and data residency compliance. This update addresses growing demand for flexible, scalable, and fully managed PostgreSQL database services in Europe, particularly for organizations with data sovereignty requirements or those seeking to optimize performance by locating resources closer to end users.

Azure Database for PostgreSQL Flexible Server is a managed database service that offers enhanced control and customization compared to the Single Server deployment option. It supports features such as zone-redundant high availability, burstable and scalable compute tiers, and customizable maintenance windows. By launching Flexible Server in Belgium Central, Microsoft provides customers with the ability to deploy PostgreSQL instances in a region that complies with EU data protection regulations, while leveraging the service’s flexible compute and storage scaling, built-in high availability, and automated backups.

Technically, Flexible Server uses a decoupled compute and storage architecture, allowing independent scaling of CPU, memory, and storage resources. It supports both single-zone and zone-redundant high availability configurations, leveraging Azure Availability Zones to ensure resilience against data center failures. The service automates patching, backups, and monitoring, while exposing PostgreSQL parameters for fine-tuning performance. Deployment in Belgium Central is implemented by provisioning resources within that Azure region’s infrastructure, ensuring data locality and compliance with regional governance policies.

Typical use cases for this update include European enterprises and ISVs requiring managed PostgreSQL databases with low latency for applications hosted in or near Belgium, such as financial services, healthcare, and government workloads subject to GDPR. It also benefits SaaS providers targeting European customers who need regional data residency and high availability. Additionally, developers building cloud-native applications with microservices architectures can leverage Flexible Server’s scaling and maintenance capabilities to optimize cost and performance.

Important considerations include verifying that the Belgium Central region supports all required Flexible Server features and SKUs, as some advanced capabilities or instance sizes may have phased rollouts. Customers should also evaluate network connectivity options, such as Virtual Network integration and Private Link, to secure database access. Backup retention policies, maintenance windows, and failover behavior should be configured according to application SLAs. As with any regional deployment, customers must assess compliance requirements and ensure that data residency in Belgium Central aligns with organizational policies.

Integration with other Azure services is seamless: Flexible Server can be connected to Azure App Service, Azure Kubernetes Service (AKS), and Azure Functions for application hosting; Azure Monitor and Azure Log Analytics for observability; Azure Active Directory for identity management; and Azure Private Link for secure connectivity. Additionally, customers can use Azure Data Factory or Azure Synapse Analytics for data integration and analytics scenarios involving PostgreSQL data.

In summary, the general availability of Azure Database for PostgreSQL Flexible Server in Belgium Central enables IT professionals to deploy scalable, highly available, and fully managed PostgreSQL databases within a European region that supports data residency and compliance requirements, while benefiting from the Flexible Server’s architectural advantages and integration with the broader Azure ecosystem. This update facilitates optimized performance and governance for cloud applications targeting Belgian and European markets.

---

### 3. Generally Available: Update pg_squeeze to version 1.9.1 in Azure Database for PostgreSQL Flexible Server 

**Published**: December 03, 2025 17:30:15 UTC
**Link**: [Generally Available: Update pg_squeeze to version 1.9.1 in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534518)

**Update ID**: 534518
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now supports upgrading the pg_squeeze extension to version 1.9.1.

- Key changes or new features  
pg_squeeze 1.9.1 improves table bloat management by enabling more efficient and less intrusive table reorganization. This update includes bug fixes and performance enhancements that help maintain database health and optimize storage without heavy locking or downtime.

- Target audience affected  
Developers and database administrators using Azure Database for PostgreSQL Flexible Server who rely on pg_squeeze for automated table bloat reduction and maintenance.

- Important notes if any  
Upgrading to pg_squeeze 1.9.1 requires manual intervention to update the extension in your Flexible Server instance. Review compatibility and test in non-production environments before applying in production to ensure stability. For detailed upgrade instructions and feature specifics, refer to the official Azure documentation.

**Details**:

The Azure Database for PostgreSQL Flexible Server now supports upgrading the pg_squeeze extension to version 1.9.1, enabling users to optimize table bloat management more effectively within their PostgreSQL environments. 

**Background and Purpose:**  
Table bloat is a common issue in PostgreSQL databases caused by dead tuples accumulating after updates and deletes, which can degrade performance and increase storage usage. The pg_squeeze extension automates the process of reclaiming this wasted space by performing online table rewrites without requiring exclusive locks, thus minimizing downtime. Updating pg_squeeze to version 1.9.1 in Azure Database for PostgreSQL Flexible Server aims to provide users with the latest improvements and bug fixes, enhancing database maintenance efficiency and overall performance.

**Specific Features and Detailed Changes:**  
Version 1.9.1 of pg_squeeze introduces several enhancements over previous versions, including improved handling of partitioned tables, better concurrency control during squeeze operations, and refined heuristics for detecting bloat thresholds. It also addresses known issues related to index maintenance and reduces the risk of transaction conflicts during the squeeze process. These updates allow for more reliable and less intrusive table maintenance, especially in high-transaction environments.

**Technical Mechanisms and Implementation Methods:**  
pg_squeeze works by performing an online table rewrite that compacts tables and indexes to remove dead tuples without requiring heavy locks that block concurrent reads and writes. It leverages PostgreSQL’s native capabilities such as `CREATE TABLE AS` and `ALTER TABLE SWAP` operations under the hood, ensuring minimal impact on database availability. The extension monitors table statistics to decide when to trigger squeeze operations based on configurable thresholds. In Azure Database for PostgreSQL Flexible Server, upgrading to version 1.9.1 is performed via the standard extension management commands (`ALTER EXTENSION pg_squeeze UPDATE TO '1.9.1';`), supported by the platform’s managed environment.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for workloads with frequent updates and deletes, such as OLTP applications, SaaS platforms, and data ingestion pipelines, where table bloat can quickly accumulate. By automating bloat reduction, pg_squeeze helps maintain consistent query performance and reduces storage costs. It is also useful in scenarios requiring minimal downtime maintenance windows, as its online operation model avoids heavy locking.

**Important Considerations and Limitations:**  
While pg_squeeze 1.9.1 improves concurrency and bloat detection, users should still monitor its impact on system resources during squeeze operations, as it involves table rewrites that consume CPU and I/O. It is recommended to schedule squeeze operations during off-peak hours or configure thresholds carefully to balance maintenance with workload demands. Additionally, certain complex table structures or extensions may have compatibility considerations; thorough testing in staging environments is advised before production deployment.

**Integration with Related Azure Services:**  
Azure Database for PostgreSQL Flexible Server’s managed environment complements pg_squeeze by providing automated backups, monitoring, and scaling capabilities, which together enhance database reliability and performance. Integration with Azure Monitor allows tracking of squeeze operation metrics and alerting on resource utilization. Furthermore, combining pg_squeeze with Azure Automation or Azure Logic Apps can enable scheduled maintenance workflows, improving operational efficiency.

In summary, the availability of pg_squeeze version 1.9.1 in Azure Database for PostgreSQL Flexible Server equips IT professionals with advanced tools to manage table bloat effectively through online, low-impact maintenance, thereby optimizing database performance and storage utilization in production environments.

---

### 4. Generally Available: The ip4r extension in Azure Database for PostgreSQL Flexible Server 

**Published**: December 03, 2025 17:30:15 UTC
**Link**: [Generally Available: The ip4r extension in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534509)

**Update ID**: 534509
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
Azure Database for PostgreSQL Flexible Server now supports the ip4r extension.

- Key changes or new features  
The ip4r extension enables efficient storage, querying, and indexing of IPv4 and IPv6 addresses and IP ranges. This enhances performance for applications managing IP data by providing specialized data types and operators optimized for IP address manipulation.

- Target audience affected  
Developers and IT professionals working with Azure Database for PostgreSQL Flexible Server who need to store and query IP addresses or ranges efficiently, such as those building network management, security, or geolocation applications.

- Important notes if any  
The ip4r extension must be installed explicitly on your Flexible Server instance. Ensure compatibility with your application’s PostgreSQL version and test queries leveraging ip4r data types for optimal performance. For detailed installation and usage guidance, refer to the official Azure documentation.

**Details**:

The recent general availability of the ip4r extension in Azure Database for PostgreSQL Flexible Server introduces native support for efficient storage, querying, and indexing of IPv4 and IPv6 addresses and ranges, addressing a critical need for network-centric applications to manage IP data with high performance and flexibility.

**Background and Purpose:**  
Managing IP addresses and ranges is a common requirement in network management, security analytics, and geolocation services. Traditional PostgreSQL data types (e.g., inet, cidr) provide basic IP address support but lack advanced indexing and range query capabilities optimized for large-scale IP data. The ip4r extension enhances PostgreSQL by offering specialized data types and indexes tailored for IP addresses and ranges, enabling faster and more efficient operations. By making ip4r generally available in Azure Database for PostgreSQL Flexible Server, Microsoft empowers developers and DBAs to build scalable, IP-aware applications without needing external tools or complex custom implementations.

**Specific Features and Detailed Changes:**  
- **New Data Types:** ip4r introduces custom data types such as `ip4r` for single IP addresses and `ip4r` range types that can represent contiguous IP ranges, supporting both IPv4 and IPv6.  
- **Efficient Indexing:** It supports GiST and SP-GiST indexes optimized for IP range queries, significantly improving query performance on large datasets involving IP address containment, overlap, and adjacency operations.  
- **Rich Operators:** The extension provides a comprehensive set of operators for comparing IP addresses and ranges, including containment (`@>`), overlap (`&&`), adjacency, and equality, facilitating complex network queries.  
- **Seamless Installation:** Users can now install ip4r via the standard PostgreSQL extension management commands (`CREATE EXTENSION ip4r;`) in Flexible Server instances, simplifying deployment and management.

**Technical Mechanisms and Implementation Methods:**  
ip4r extends PostgreSQL’s type system by defining new composite types and range types for IP addresses. It leverages PostgreSQL’s extensible indexing framework to implement GiST and SP-GiST indexes that use tree structures optimized for spatial and range queries. Internally, IP addresses are stored in a compact binary format, allowing fast bitwise operations and comparisons. The extension hooks into PostgreSQL’s query planner to optimize execution plans for IP-related queries, ensuring efficient use of indexes and minimizing I/O.

**Use Cases and Application Scenarios:**  
- **Network Security and Monitoring:** Efficiently store and query firewall rules, IP blacklists/whitelists, and intrusion detection data.  
- **Geolocation and IP Mapping:** Manage IP ranges assigned to different geographic regions or customers for analytics and compliance.  
- **Cloud Infrastructure Management:** Track and audit IP allocations within virtual networks and subnets in hybrid cloud environments.  
- **Telecommunications:** Handle large datasets of IP addresses for routing, billing, and subscriber management.  
- **Application Access Control:** Implement IP-based access policies with fast lookup and range matching.

**Important Considerations and Limitations:**  
- The ip4r extension is supported only on Azure Database for PostgreSQL Flexible Server, not on Single Server or Hyperscale (Citus) tiers as of now.  
- While ip4r supports both IPv4 and IPv6, users should validate compatibility with existing application logic and data models.  
- Index maintenance overhead should be considered in write-heavy workloads, as GiST and SP-GiST indexes can impact insert/update performance.  
- Backup and restore operations involving ip4r data types require PostgreSQL version compatibility and extension presence on target instances.  
- Users should monitor extension version updates and Azure service announcements for ongoing support and improvements.

**Integration with Related Azure Services:**  
- **Azure Monitor and Azure Sentinel:** IP data stored using ip4r can be integrated with security analytics pipelines for enhanced threat detection.  
- **Azure Virtual Network (VNet):** IP range data can be correlated with VNet address spaces for network management

---

### 5. Generally Available: The credcheck extension in Azure Database for PostgreSQL Flexible Server 

**Published**: December 03, 2025 17:30:15 UTC
**Link**: [Generally Available: The credcheck extension in Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=534504)

**Update ID**: 534504
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL

**Summary**:

- What was updated  
The credcheck extension is now generally available for Azure Database for PostgreSQL Flexible Server.

- Key changes or new features  
Developers and DBAs can install the credcheck extension to enforce password and credential validation policies natively within PostgreSQL. This enables stronger security controls by validating password complexity and credential rules directly at the database level, helping to prevent weak or non-compliant passwords.

- Target audience affected  
This update primarily benefits developers, database administrators, and IT security professionals managing PostgreSQL Flexible Server instances who require enhanced credential security and compliance enforcement.

- Important notes if any  
The extension must be explicitly installed and configured on the Flexible Server instance. Leveraging credcheck helps align with organizational security policies and regulatory requirements by embedding password validation into the database authentication process. For detailed installation and usage guidance, refer to the official Azure documentation.

**Details**:

The recent general availability of the credcheck extension in Azure Database for PostgreSQL Flexible Server introduces a native mechanism to enforce password and credential validation policies directly within the PostgreSQL environment, enhancing security posture and compliance capabilities for database administrators and developers.

**Background and Purpose of the Update**  
Credential management and enforcement of strong password policies are critical components of database security. Traditionally, enforcing such policies in PostgreSQL required external tools or manual processes, which could lead to inconsistent enforcement and increased administrative overhead. The introduction of the credcheck extension addresses this gap by embedding credential validation logic inside the PostgreSQL server itself, enabling automated, consistent enforcement of password complexity, expiration, and reuse policies. This update aligns with Azure’s commitment to providing secure, compliant, and manageable database services.

**Specific Features and Detailed Changes**  
The credcheck extension provides a set of functions and hooks that validate user credentials during password changes or user creation events. Key features include:  
- Enforcement of password complexity rules (e.g., minimum length, character classes, prohibited patterns).  
- Password expiration policies to mandate periodic password changes.  
- Prevention of password reuse by maintaining a history of previous passwords.  
- Integration with PostgreSQL’s native authentication workflows to ensure seamless operation without requiring external scripts or manual checks.  
- Configurable policy parameters allowing customization to meet organizational security standards.

**Technical Mechanisms and Implementation Methods**  
Technically, credcheck operates as a PostgreSQL extension that hooks into the password change lifecycle. When a user attempts to set or change a password, credcheck intercepts the request and runs the configured validation rules. If the password does not comply with the defined policies, the operation is rejected with detailed error messages. The extension stores password history hashes securely within the database to enforce reuse policies without exposing sensitive information. Configuration is managed via PostgreSQL’s standard extension and parameter settings, allowing administrators to enable, disable, or tune policies dynamically.

**Use Cases and Application Scenarios**  
- Enterprises requiring compliance with internal or regulatory password policies (e.g., PCI-DSS, HIPAA).  
- Organizations aiming to reduce the risk of credential-related breaches by enforcing strong password standards.  
- Managed service providers who need to ensure consistent security policies across multiple PostgreSQL Flexible Server instances.  
- Development and testing environments where password policies must reflect production security requirements.  
- Automated DevOps pipelines that include database user provisioning with enforced credential policies.

**Important Considerations and Limitations**  
- The extension currently supports only Azure Database for PostgreSQL Flexible Server and may not be available for Single Server or Hyperscale (Citus) deployments.  
- Proper configuration is essential; overly restrictive policies might disrupt application connectivity if password changes are not coordinated.  
- Password history storage increases metadata size; administrators should monitor storage and performance impacts in high-change environments.  
- Credential validation occurs at the PostgreSQL server level; integration with external identity providers or Azure AD authentication is not directly affected by this extension.  
- Backup and restore operations should consider the extension’s state to maintain policy enforcement consistency.

**Integration with Related Azure Services**  
While credcheck operates within the PostgreSQL Flexible Server, it complements Azure’s broader security ecosystem:  
- Azure Active Directory (AAD) integration for PostgreSQL Flexible Server provides identity management but does not replace password policy enforcement for native PostgreSQL users; credcheck fills this gap.  
- Azure Security Center and Azure Defender can monitor and alert on suspicious activities, with credcheck reducing risk by preventing weak credential usage.  
- Azure Policy can be used to enforce deployment standards that include enabling security extensions like credcheck.  
- Integration with Azure Monitor enables logging and alerting on credential validation failures, supporting operational security workflows.

In summary, the general availability of the credcheck extension in Azure Database for PostgreSQL Flexible Server empowers IT professionals to enforce robust, customizable password and credential policies natively within PostgreSQL, enhancing security, compliance, and operational efficiency without relying on external tools. This update is particularly valuable for

---

### 6. Generally Available: Azure Load Balancer bandwidth metrics now support Protocol dimension

**Published**: December 03, 2025 17:00:27 UTC
**Link**: [Generally Available: Azure Load Balancer bandwidth metrics now support Protocol dimension](https://azure.microsoft.com/updates?id=536747)

**Update ID**: 536747
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Load Balancer

**Summary**:

- What was updated  
Azure Load Balancer bandwidth metrics now include a new metric dimension called Protocol.

- Key changes or new features  
Bandwidth-related metrics such as Byte count, Packet count, and SYN count are enhanced to show traffic breakdown by Protocol dimension. Specifically, TCP traffic is identified with Protocol=6. This allows more granular monitoring and analysis of network traffic by protocol type directly in the Azure portal and via API queries.

- Target audience affected  
Developers and IT professionals managing Azure Load Balancer configurations, monitoring network performance, or building custom telemetry and alerting solutions will benefit from this update. It enables improved diagnostics and traffic segmentation.

- Important notes if any  
The Protocol dimension is now visible in the Azure portal metrics explorer and accessible through Azure Monitor APIs. Users should update their metric queries and dashboards to leverage this new dimension for deeper insights into load balancer traffic patterns. This feature is generally available and ready for production use.

**Details**:

The recent Azure update announces the general availability of enhanced bandwidth metrics for Azure Load Balancer, now including the Protocol dimension. This enhancement enables more granular monitoring and analysis of network traffic by protocol type, specifically distinguishing TCP traffic with Protocol=6.

**Background and Purpose of the Update**  
Azure Load Balancer is a foundational networking service that distributes incoming traffic across virtual machines or instances to ensure high availability and reliability. Monitoring its bandwidth usage is critical for performance tuning, capacity planning, and troubleshooting. Previously, bandwidth metrics such as Bytes, Packets, and SYN Count were aggregated without protocol-level granularity. The update addresses the need for deeper insights into traffic composition by protocol, enabling IT professionals to better understand traffic patterns, detect anomalies, and optimize network configurations.

**Specific Features and Detailed Changes**  
- **Protocol Dimension Added:** Bandwidth metrics now include a new dimension named "Protocol." This dimension categorizes traffic by the IP protocol number, with TCP traffic explicitly identified as Protocol=6.  
- **Metrics Affected:** The metrics enhanced with this dimension include Byte Count, Packet Count, and SYN Count, which are essential for measuring throughput, packet flow, and connection attempts respectively.  
- **Azure Portal Visualization:** When viewing these metrics in the Azure portal’s monitoring blade, users can filter and segment data by protocol, enabling visual differentiation of TCP traffic from other protocols.  
- **API and SDK Support:** The Protocol dimension is also exposed in Azure Monitor APIs and SDKs, allowing programmatic access for custom dashboards, alerts, and automation workflows.

**Technical Mechanisms and Implementation Methods**  
Azure Load Balancer collects telemetry data at the datapath level, where it inspects network packets flowing through the load balancer. The update leverages packet inspection to extract the IP protocol field from each packet header. This protocol information is then appended as a dimension to the existing metrics emitted to Azure Monitor. The metrics pipeline aggregates these values over the configured time intervals, maintaining protocol-specific counters. This approach ensures minimal performance overhead while providing richer metric granularity.

**Use Cases and Application Scenarios**  
- **Traffic Analysis and Troubleshooting:** Network engineers can identify which protocols dominate traffic, helping to pinpoint unusual protocol usage or potential security threats.  
- **Capacity Planning:** By understanding protocol-specific bandwidth consumption, IT teams can optimize load balancer rules and backend pool configurations to better handle expected traffic types.  
- **Security Monitoring:** SYN Count metrics segmented by protocol can help detect SYN flood attacks or other protocol-specific anomalies.  
- **Custom Alerting:** Users can configure alerts based on protocol-specific thresholds, for example, triggering notifications when TCP traffic exceeds expected limits.  
- **Cost Management:** Protocol-level insights can inform decisions on scaling and resource allocation, potentially reducing unnecessary costs.

**Important Considerations and Limitations**  
- **Protocol Coverage:** Currently, the update explicitly mentions TCP (Protocol=6). Other protocols may be included but are not detailed; users should verify supported protocols in their environment.  
- **Metric Latency:** As with all Azure Monitor metrics, there may be a slight delay (typically up to a few minutes) before protocol-dimensioned metrics are available for analysis.  
- **Data Volume:** Adding the Protocol dimension increases the cardinality of metrics, which could impact storage and query performance in large-scale environments. Proper metric retention and aggregation strategies should be considered.  
- **Compatibility:** Existing monitoring solutions consuming Azure Load Balancer metrics should be reviewed and potentially updated to leverage the new dimension.

**Integration with Related Azure Services**  
- **Azure Monitor and Log Analytics:** Protocol-dimensioned metrics integrate seamlessly with Azure Monitor, enabling advanced queries in Log Analytics and visualization in Azure dashboards.  
- **Azure Network Watcher:** While Network Watcher provides packet capture and flow logs, the Load Balancer metrics complement these by offering aggregated, protocol-specific telemetry.  
- **Azure Automation and Logic Apps:** The enhanced metrics can be used as triggers or conditions in automation run

---


*This report was automatically generated - 2025-12-04 03:03:49 UTC*