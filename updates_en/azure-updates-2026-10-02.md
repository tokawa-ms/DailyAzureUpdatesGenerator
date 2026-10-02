# October 02, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 02, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Public Preview: Reader Endpoint for Azure Database for MySQL 

**Published**: October 01, 2026 17:57:11 UTC
**Link**: [Public Preview: Reader Endpoint for Azure Database for MySQL ](https://azure.microsoft.com/updates?id=569653)

**Update ID**: 569653
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure Database for MySQL, Feature

**Summary**:

- What was updated  
Azure Database for MySQL – Flexible Server now supports a reader endpoint in public preview.

- Key changes or new features  
A new reader endpoint is available for servers with multiple read replicas. This endpoint automatically load-balances incoming read-only connections across all replicas, simplifying connection management for applications that require high availability and scalability for read operations. Developers no longer need to manually manage connections to individual replicas.

- Target audience affected  
Developers and IT professionals managing Azure Database for MySQL – Flexible Server deployments with multiple read replicas, especially those building applications with heavy read workloads or requiring improved performance and scalability.

- Important notes  
The reader endpoint is currently in public preview and may not be suitable for production workloads until general availability. Existing applications can leverage this feature to optimize read operations and reduce management overhead. Review documentation for integration details and limitations during the preview phase.

For more information, visit the [Azure Update announcement](https://azure.microsoft.com/updates?id=569653).

**Details**:

**Azure Update Report: Public Preview – Reader Endpoint for Azure Database for MySQL**

**Background and Purpose of the Update**  
Azure Database for MySQL – Flexible Server supports read replicas to improve scalability and performance for read-heavy workloads. Traditionally, managing connections to multiple replicas required manual configuration and application-side logic to distribute read-only queries. The introduction of the reader endpoint aims to simplify this process by providing a single connection point for read-only workloads, automating load balancing across available replicas.

**Specific Features and Detailed Changes**  
The update introduces a *reader endpoint* in public preview for Azure Database for MySQL – Flexible Server. This endpoint is a dedicated DNS address that applications can use to connect for read-only operations. When clients connect to the reader endpoint, their read-only queries are automatically distributed among all configured read replicas. This eliminates the need for manual connection management and custom load-balancing logic within applications.

**Technical Mechanisms and Implementation Methods**  
The reader endpoint functions as a proxy layer within Azure Database for MySQL – Flexible Server. When a client establishes a connection to the reader endpoint, the service transparently routes the connection to one of the available read replicas. The routing mechanism ensures load balancing, optimizing resource utilization and query performance. The endpoint is designed for read-only workloads; write operations are not supported and must continue to use the primary server endpoint.

**Use Cases and Application Scenarios**  
- **Reporting and Analytics:** Applications generating reports or performing analytics can connect to the reader endpoint, ensuring that read queries are distributed across replicas without impacting the primary server.
- **Web Applications:** High-traffic web applications can offload read operations to replicas via the reader endpoint, improving scalability and reducing latency.
- **Business Intelligence Tools:** BI tools can use the reader endpoint for read-intensive data extraction, benefiting from automatic load balancing.
- **Microservices Architectures:** Services requiring read-only access to MySQL data can connect to the reader endpoint, simplifying connection management.

**Important Considerations and Limitations**  
- The reader endpoint is designed exclusively for read-only workloads. Any attempt to perform write operations through this endpoint will fail.
- The feature is currently in public preview, which may entail limitations in terms of support, stability, or feature completeness.
- Applications must ensure that only read queries are sent to the reader endpoint to avoid errors.
- Connection management and failover behavior should be tested during the preview phase to understand performance and reliability characteristics.

**Integration with Related Azure Services**  
The reader endpoint integrates seamlessly with Azure Database for MySQL – Flexible Server’s existing read replica functionality. It can be used in conjunction with Azure App Service, Azure Functions, and other Azure compute services to optimize read-heavy workloads. The endpoint can also be leveraged by Azure Data Factory, Azure Logic Apps, and other data integration tools that require efficient, scalable read access to MySQL databases.

**Summary Sentence**  
The public preview of the reader endpoint for Azure Database for MySQL – Flexible Server introduces an automated, load-balanced connection mechanism for read-only workloads, streamlining connection management and enhancing scalability across multiple replicas.

---

### 2. Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029

**Published**: October 01, 2026 17:02:55 UTC
**Link**: [Retirement: DCsv3 and DCdsv3-series Azure Virtual Machines will be retired on October 31, 2029](https://azure.microsoft.com/updates?id=569592)

**Update ID**: 569592
**Data source**: Azure Updates API

**Categories**: Compute, Linux Virtual Machines, Virtual Machines, Windows Virtual Machines, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of DCsv3 and DCdsv3-series Azure Virtual Machines (VMs), including Linux, Windows, and Dedicated Host variants. These VM series will no longer be available after October 31, 2029.

- Key changes or new features  
No new features are introduced. The update is a deprecation notice. After October 31, 2029, DCsv3 and DCdsv3-series VMs cannot be used or purchased. Customers are advised to migrate workloads to supported VM series before the retirement date.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently using DCsv3 and DCdsv3-series Azure VMs for confidential computing workloads, as well as those managing Azure Dedicated Hosts.

- Important notes if any  
- Plan migration strategies well ahead of the October 31, 2029 deadline to avoid service disruption.  
- Review alternative VM series for confidential computing and ensure compatibility with your workloads.  
- Microsoft recommends evaluating the latest confidential computing VM offerings for migration.  
- After the retirement date, existing DCsv3 and DCdsv3-series VMs will be shut down and unavailable.  
- For more details and guidance, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=569592

**Details**:

**Azure Update Report: Retirement of DCsv3 and DCdsv3-series Azure Virtual Machines on October 31, 2029**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of the DCsv3 and DCdsv3-series Azure Virtual Machines (VMs), including Linux, Windows, and Dedicated Host variants, effective October 31, 2029. This update is part of Azure’s ongoing lifecycle management strategy, which ensures that customers are using the most secure, performant, and supported VM offerings. The retirement encourages migration to newer VM series that provide enhanced features and ongoing support.

**Specific Features and Detailed Changes:**  
- **Retirement Scope:** The update affects all DCsv3 and DCdsv3-series VMs, regardless of operating system or deployment on dedicated hosts.
- **Availability:** After October 31, 2029, these VM sizes will no longer be available for new deployments or purchases.
- **Migration Requirement:** Customers must migrate any workloads running on affected VM series to alternative VM families before the retirement date to avoid service disruption.

**Technical Mechanisms and Implementation Methods:**  
- **Resource Decommissioning:** Microsoft will deprecate the DCsv3 and DCdsv3-series SKUs in the Azure platform, removing them from the VM size catalog and disabling the ability to provision new instances.
- **Migration Process:** IT professionals should plan and execute migration strategies, such as redeploying workloads to supported VM series using Azure Migrate, Azure Site Recovery, or manual VM image migration.
- **Notification and Monitoring:** Azure will likely provide notifications and guidance through the Azure Portal and service health alerts as the retirement date approaches.

**Use Cases and Application Scenarios:**  
- **Current Usage:** DCsv3 and DCdsv3-series VMs are typically used for confidential computing workloads, leveraging hardware-based security features for data protection.
- **Migration Scenarios:** Workloads requiring confidential computing capabilities should be evaluated and migrated to alternative Azure VM series that offer similar or improved security and performance characteristics.

**Important Considerations and Limitations:**  
- **Service Continuity:** Failure to migrate workloads before the retirement date will result in loss of access to the affected VM types, potentially causing application downtime or data loss.
- **Compatibility:** IT teams must assess workload compatibility with newer VM series, ensuring that security, performance, and feature requirements are met.
- **Licensing and Cost Implications:** Migrating to newer VM series may have implications for licensing, pricing, and resource allocation, which should be evaluated during migration planning.

**Integration with Related Azure Services:**  
- **Azure Migrate:** Facilitates assessment and migration of workloads from retired VM series to supported alternatives.
- **Azure Site Recovery:** Provides disaster recovery and migration capabilities for VMs.
- **Azure Resource Manager (ARM):** Supports template-based redeployment to new VM series.
- **Azure Security Center:** Assists in maintaining security posture during and after migration.

**Summary Sentence:**  
The DCsv3 and DCdsv3-series Azure Virtual Machines, including Linux, Windows, and Dedicated Host options, will be retired on October 31, 2029, requiring customers to migrate their workloads to supported VM series before this date to maintain service continuity and support.

---


*This report was automatically generated - 2026-10-02 03:02:26 UTC*