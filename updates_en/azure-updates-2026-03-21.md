# March 21, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 21, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Public Preview: Azure SQL updates for mid-March 2026

**Published**: March 20, 2026 19:15:35 UTC
**Link**: [Public Preview: Azure SQL updates for mid-March 2026](https://azure.microsoft.com/updates?id=558116)

**Update ID**: 558116
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Azure SQL Managed Instance, Features

**Summary**:

- What was updated  
Azure SQL received several updates and enhancements in public preview as of mid-March 2026.

- Key changes or new features  
The main improvements focus on reducing storage space, I/O, and memory consumption, thereby enhancing overall database performance. Notably, these optimizations are achieved without requiring developers or DBAs to spend time on manual index maintenance jobs. Additionally, new configuration options have been introduced to streamline performance tuning and resource management.

- Target audience affected  
These updates are relevant for database administrators, IT professionals managing Azure SQL environments, and developers building or maintaining applications that rely on Azure SQL databases.

- Important notes if any  
The enhancements are in public preview, so they may not yet be suitable for production workloads. Users are encouraged to test the new features and provide feedback. The reduction in resource consumption and elimination of manual index maintenance can lead to cost savings and simplified operations, but users should review documentation for compatibility and best practices.  
For more details, refer to the official update: https://azure.microsoft.com/updates?id=558116

**Details**:

**Azure Update Report: Public Preview – Azure SQL Updates for Mid-March 2026**

**Background and Purpose of the Update**  
The mid-March 2026 Azure SQL update is designed to address common challenges related to resource consumption and performance in SQL database environments. Traditionally, maintaining optimal performance in Azure SQL databases requires regular index maintenance jobs, which can be resource-intensive and time-consuming. The purpose of this update is to reduce the consumption of storage space, I/O, and memory, and to improve overall database performance, all without the need for manual or scheduled index maintenance operations.

**Specific Features and Detailed Changes**  
This update introduces enhancements that automatically optimize resource usage within Azure SQL. The changes specifically target the reduction of storage space, input/output (I/O) operations, and memory utilization. By minimizing these resource demands, the update aims to streamline database operations and improve performance. Notably, these improvements are achieved without requiring users to invest time and effort into managing index maintenance jobs, which are typically necessary for maintaining query performance and data integrity in relational databases.

**Technical Mechanisms and Implementation Methods**  
While the update summary does not provide explicit details on the underlying mechanisms, it indicates that Azure SQL now includes built-in capabilities to manage and optimize indexes or data structures automatically. This likely involves enhancements to the Azure SQL engine that allow it to monitor and adjust storage and memory allocation dynamically, and to optimize I/O patterns. The automation of these maintenance tasks removes the need for scheduled index rebuilds or reorganizations, which are common in traditional SQL Server environments.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations running large-scale or high-transactional Azure SQL databases where manual index maintenance can be disruptive or costly. Scenarios include:  
- Multi-tenant SaaS applications with unpredictable workloads  
- Mission-critical OLTP systems requiring consistent performance  
- Environments with limited DBA resources, where automation reduces operational overhead  
- Databases with frequent data modifications, where index fragmentation is a concern

**Important Considerations and Limitations**  
IT professionals should note that this update is currently in Public Preview, which means it may not yet be suitable for all production workloads. Users should evaluate the feature in test or development environments before broad deployment. Additionally, as the update summary does not specify, it is important to consult the official Azure documentation for any configuration requirements, feature limitations, or compatibility notes.

**Integration with Related Azure Services**  
The enhancements are native to Azure SQL and are expected to integrate seamlessly with other Azure services that interact with Azure SQL databases, such as Azure Data Factory, Azure Logic Apps, and Power BI. The reduction in resource consumption can also lead to cost savings and improved performance for workloads orchestrated across multiple Azure services.

**Summary Sentence**  
The mid-March 2026 Azure SQL public preview update introduces automated optimizations that reduce storage, I/O, and memory usage, and improve performance without manual index maintenance, streamlining database management for IT professionals.

---

### 2. Retirement: Azure SQL Elastic query - Shard_Map_Manager mode

**Published**: March 20, 2026 19:00:50 UTC
**Link**: [Retirement: Azure SQL Elastic query - Shard_Map_Manager mode](https://azure.microsoft.com/updates?id=558086)

**Update ID**: 558086
**Data source**: Azure Updates API

**Categories**: Databases, Hybrid + multicloud, Azure SQL Database, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of Azure SQL Elastic Query using the Shard_Map_Manager external data source type.

- Key changes or new features  
Support for Elastic Query with Shard_Map_Manager mode will end on March 31, 2027. After this date, no updates or technical support will be provided for workloads using this mode. Existing workloads will continue to function but will not receive bug fixes, security updates, or assistance from Microsoft.

- Target audience affected  
Developers and IT professionals managing solutions that use Azure SQL Elastic Query with Shard_Map_Manager for sharding and cross-database queries.

- Important notes if any  
Microsoft recommends migrating to alternative solutions before the retirement date to ensure continued support and security. Review your current usage of Shard_Map_Manager and plan for migration to supported options, such as Elastic Query with other external data source types or other sharding/data partitioning strategies. Early planning is advised to avoid disruption.  
For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=558086

**Details**:

**Azure Update Report: Retirement of Azure SQL Elastic Query - Shard_Map_Manager Mode**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of the Azure SQL Elastic Query feature when used with the Shard_Map_Manager external data source type. Effective March 31, 2027, this mode will reach its end of support. The purpose of this update is to inform users that while existing workloads utilizing this feature may continue to operate, they will not receive further updates or technical support from Microsoft after the retirement date.

**Specific Features and Detailed Changes**  
The affected feature is the Azure SQL Elastic Query capability that leverages Shard_Map_Manager as its external data source type. After March 31, 2027, this specific configuration will no longer be supported. No new features, bug fixes, or security updates will be provided for this mode. Other Elastic Query modes or configurations are not mentioned as being affected by this retirement.

**Technical Mechanisms and Implementation Methods**  
Azure SQL Elastic Query enables querying across multiple Azure SQL Databases, often used in sharded database architectures. The Shard_Map_Manager is a component that manages metadata about the distribution of data across shards, facilitating the routing of queries to the appropriate databases. In the Shard_Map_Manager mode, Elastic Query uses this metadata to resolve and execute cross-shard queries efficiently. The retirement means that the integration between Elastic Query and Shard_Map_Manager for external data sources will no longer be maintained or supported by Microsoft.

**Use Cases and Application Scenarios**  
Typical use cases for Elastic Query with Shard_Map_Manager include:  
- Applications with horizontal partitioning (sharding) of data across multiple Azure SQL Databases.
- Scenarios requiring federated queries that aggregate or join data from multiple shards.
- Multi-tenant SaaS applications where each tenant’s data is stored in a separate shard, and cross-tenant reporting or analytics is required.

**Important Considerations and Limitations**  
- After March 31, 2027, existing solutions using Elastic Query with Shard_Map_Manager will continue to function but will be unsupported.
- There will be no further updates, bug fixes, or security patches for this mode.
- Organizations relying on this feature should begin planning migration strategies to supported alternatives to ensure continued support and security compliance.
- The retirement does not impact other Elastic Query modes unless they specifically use Shard_Map_Manager as the external data source type.

**Integration with Related Azure Services**  
Elastic Query with Shard_Map_Manager is typically used in conjunction with Azure SQL Database and the sharding pattern. It may also interact with other Azure services involved in data management, analytics, or application hosting. After retirement, integration scenarios that depend on Shard_Map_Manager for cross-shard querying will require redesign or migration to alternative supported solutions.

**Summary Sentence**  
Starting March 31, 2027, Azure SQL Elastic Query using the Shard_Map_Manager external data source type will reach end of support, meaning existing workloads can continue to run but will no longer receive updates or support from Microsoft.

---

### 3. Retirement: Azure Sphere will be retired on July 31, 2031

**Published**: March 20, 2026 17:15:50 UTC
**Link**: [Retirement: Azure Sphere will be retired on July 31, 2031](https://azure.microsoft.com/updates?id=557123)

**Update ID**: 557123
**Data source**: Azure Updates API

**Categories**: Internet of Things, Azure Sphere, Retirements

**Summary**:

- What was updated  
Azure Sphere, Microsoft’s integrated security solution for IoT devices, will be retired on July 31, 2031.

- Key changes or new features  
After July 31, 2031, Azure Sphere will no longer provide support for customer applications, operating system (OS) updates, bug fixes, security updates, or Device Authentication Authority (DAA) certificate issuance. No new features are being introduced; this is a retirement notice.

- Target audience affected  
This update impacts developers, IT professionals, and organizations currently using Azure Sphere for IoT device security and management.

- Important notes if any  
Customers must plan to migrate away from Azure Sphere before the retirement date to ensure continued security and compliance. After July 31, 2031, devices will no longer receive critical updates or certificates, increasing security risks. Microsoft recommends evaluating alternative IoT security solutions and beginning migration planning as soon as possible. For more details and ongoing updates, refer to the official Azure update page: https://azure.microsoft.com/updates?id=557123

**Details**:

**Azure Update Report: Retirement of Azure Sphere on July 31, 2031**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of the Azure Sphere service, effective July 31, 2031. Azure Sphere was introduced as a comprehensive solution for securing Internet of Things (IoT) devices, integrating hardware, operating system, and cloud services to provide end-to-end security. The retirement notice indicates that Microsoft will discontinue all support for Azure Sphere, including application, OS, bug, and security updates, as well as DAA (Device Attestation Authority) certificate issuance, after the specified date.

**Specific Features and Detailed Changes:**  
- **End of Support:** After July 31, 2031, Azure Sphere will no longer provide updates for customer applications, the Azure Sphere OS, or any bug and security patches.
- **DAA Certificate Issuance:** The service will cease issuing DAA certificates, which are critical for device authentication and secure communications.
- **No Further Updates:** There will be no further enhancements or maintenance releases for the Azure Sphere platform.

**Technical Mechanisms and Implementation Methods:**  
Azure Sphere’s architecture consists of three main components:  
1. **Certified MCU Hardware:** Specialized microcontrollers designed with security in mind.
2. **Azure Sphere OS:** A custom Linux-based operating system tailored for IoT security.
3. **Azure Sphere Security Service:** A cloud-based service responsible for certificate management, device authentication, and delivering OS and application updates.

The retirement means that the cloud-based security service will be decommissioned, disabling the mechanisms for secure device authentication, remote updates, and certificate renewals. Devices relying on Azure Sphere will no longer be able to receive critical updates or validate their identity with the Azure Sphere Security Service.

**Use Cases and Application Scenarios:**  
Azure Sphere has been widely used in scenarios requiring secure IoT deployments, such as:
- Industrial automation and control systems
- Smart building and facility management
- Connected consumer devices
- Secure gateways and edge devices

Organizations leveraging Azure Sphere for these scenarios must plan for migration to alternative security solutions before the retirement date.

**Important Considerations and Limitations:**  
- **Security Risks:** Post-retirement, devices will be exposed to security vulnerabilities due to the lack of updates and certificate renewals.
- **Compliance:** Organizations with regulatory or compliance requirements for device security must transition to supported solutions to maintain compliance.
- **Device Lifecycle Management:** Devices dependent on Azure Sphere will require re-engineering or replacement to ensure continued secure operation.
- **No Extended Support:** There is no mention of extended support or migration tools; all support ceases after July 31, 2031.

**Integration with Related Azure Services:**  
Azure Sphere has been designed to integrate with other Azure IoT services, such as Azure IoT Hub and Azure IoT Central, for device management, telemetry, and analytics. The retirement of Azure Sphere will impact these integrations, as device authentication and secure connectivity will no longer be supported through the Sphere platform. Organizations must evaluate alternative device security and management solutions within the Azure ecosystem or from third-party providers.

**Summary:**  
Azure Sphere will be retired on July 31, 2031, ending all support for updates, security patches, and certificate issuance, requiring organizations to transition to alternative IoT security solutions before this date to maintain device security and compliance.

---


*This report was automatically generated - 2026-03-21 03:02:29 UTC*