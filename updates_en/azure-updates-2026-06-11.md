# June 11, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: June 11, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Microsoft Entra server principals on Azure SQL Database 

**Published**: June 10, 2026 20:45:26 UTC
**Link**: [Generally Available: Microsoft Entra server principals on Azure SQL Database ](https://azure.microsoft.com/updates?id=565154)

**Update ID**: 565154
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

- What was updated  
Microsoft Entra server principals (logins) are now generally available for Azure SQL Database.

- Key changes or new features  
You can now create Microsoft Entra (formerly Azure AD) logins directly in the virtual master database of Azure SQL Database using the statement CREATE LOGIN ... FROM EXTERNAL PROVIDER. This feature brings parity with traditional SQL logins, allowing centralized identity management and enhanced security for database authentication. It simplifies the process of granting and managing access for Microsoft Entra identities at the server level.

- Target audience affected  
Developers and IT professionals managing Azure SQL Database authentication and access control, especially those using Microsoft Entra ID for identity management.

- Important notes if any  
This update enables seamless integration with Microsoft Entra ID, supporting modern authentication scenarios and reducing the need for SQL authentication. It is recommended to review your database access policies and consider migrating existing SQL logins to Microsoft Entra logins for improved security and manageability. For implementation details and best practices, refer to the official documentation.

Link: https://azure.microsoft.com/updates?id=565154

**Details**:

**Azure Update Report: Generally Available – Microsoft Entra Server Principals on Azure SQL Database**

**Background and Purpose of the Update**  
This update introduces the general availability of Microsoft Entra server principals (logins) for Azure SQL Database. Traditionally, Azure SQL Database supported SQL logins and Microsoft Entra identities for database-level authentication. However, there was a gap in parity between SQL logins and Entra identities at the server level. The purpose of this update is to enable organizations to leverage Microsoft Entra identities as server principals, thereby aligning authentication and access management practices with modern identity solutions and enhancing security and manageability.

**Specific Features and Detailed Changes**  
With this update, administrators can now create server-level logins for Microsoft Entra identities in the virtual master database of Azure SQL Database. The new syntax introduced is:  
`CREATE LOGIN ... FROM EXTERNAL PROVIDER`  
This command allows the creation of logins mapped to Microsoft Entra identities, similar to how SQL logins are created. The feature brings parity between SQL logins and Microsoft Entra logins, enabling consistent management of authentication at the server level for Azure SQL Database.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages the virtual master database in Azure SQL Database, which acts as the central point for managing server-level security objects. By executing `CREATE LOGIN ... FROM EXTERNAL PROVIDER` in the master database, administrators can register Microsoft Entra identities as server principals. These logins are authenticated via Microsoft Entra ID (formerly Azure Active Directory), ensuring secure and centralized identity management. The mechanism integrates with existing authentication flows, allowing seamless use of Entra identities for server-level access.

**Use Cases and Application Scenarios**  
- **Enterprise Authentication:** Organizations can use Microsoft Entra identities for server-level access, aligning with corporate identity management policies.
- **Role-Based Access Control:** Administrators can assign server-level roles to Entra logins, facilitating granular access control across databases.
- **Multi-Tenant Applications:** SaaS providers can manage tenant access using Entra identities, improving scalability and security.
- **Compliance and Auditing:** Using Entra logins enhances traceability and compliance by leveraging centralized identity management.

**Important Considerations and Limitations**  
- **Scope:** The feature is available for Azure SQL Database and is managed via the virtual master database.
- **Syntax Requirement:** Only the `CREATE LOGIN ... FROM EXTERNAL PROVIDER` syntax is supported for Entra logins; traditional SQL logins use different syntax.
- **Identity Source:** Logins must be based on Microsoft Entra identities; other external providers are not supported.
- **Security Practices:** Administrators should ensure proper assignment of roles and permissions to Entra logins to avoid privilege escalation.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** The update directly integrates with Microsoft Entra ID, providing unified identity management across Azure services.
- **Azure SQL Database:** Enhances authentication options for Azure SQL Database, enabling modern identity solutions.
- **Azure Role-Based Access Control (RBAC):** Complements RBAC by allowing server-level access management using Entra identities.

**Summary Sentence**  
Microsoft Entra server principals (logins) for Azure SQL Database are now generally available, enabling administrators to create server-level logins for Entra identities in the virtual master database using `CREATE LOGIN ... FROM EXTERNAL PROVIDER`, thereby achieving parity with SQL logins and enhancing authentication and access management.

---

### 2. Retirement: Azure Synapse Link for Azure Cosmos DB NoSQL

**Published**: June 10, 2026 17:00:06 UTC
**Link**: [Retirement: Azure Synapse Link for Azure Cosmos DB NoSQL](https://azure.microsoft.com/updates?id=558560)

**Update ID**: 558560
**Data source**: Azure Updates API

**Categories**: Databases, Internet of Things, Analytics, Azure Cosmos DB, Azure Synapse Analytics, Retirements, Services

**Summary**:

- What was updated  
Azure Synapse Link for Azure Cosmos DB NoSQL is being retired.

- Key changes or new features  
Starting March 31, 2026, new Azure Cosmos DB NoSQL accounts will not be able to enable Azure Synapse Link. Existing accounts with Synapse Link enabled will continue to be supported until March 31, 2029, after which the feature will be fully retired and no longer available.

- Target audience affected  
Developers and IT professionals using Azure Cosmos DB NoSQL with Azure Synapse Link for analytics or integration scenarios.

- Important notes if any  
Customers currently using Azure Synapse Link for Azure Cosmos DB NoSQL should begin planning their migration to alternative solutions before the end-of-support date (March 31, 2029). Microsoft recommends evaluating other analytics integration options. No immediate action is required for existing users, but no new enablements will be possible after March 31, 2026. For more information and migration guidance, refer to the official Azure update link: https://azure.microsoft.com/updates?id=558560

**Details**:

**Azure Update Report: Retirement of Azure Synapse Link for Azure Cosmos DB NoSQL**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of Azure Synapse Link for Azure Cosmos DB NoSQL. The update specifies that after March 31, 2026, new Azure Cosmos DB NoSQL accounts will not be able to enable Azure Synapse Link. The purpose of this update is to inform customers of the phased retirement plan and to encourage migration planning. Existing customers will continue to have full support for Azure Synapse Link until March 31, 2029, at which point the feature will reach end of life.

**Specific Features and Detailed Changes**  
The primary change is the discontinuation of Azure Synapse Link for new Azure Cosmos DB NoSQL accounts post-March 31, 2026. Azure Synapse Link is a feature that enables near real-time analytics on operational data stored in Azure Cosmos DB NoSQL by seamlessly integrating with Azure Synapse Analytics. Existing accounts with Synapse Link enabled will retain access and support until March 31, 2029. After this date, the feature will be fully retired, and no accounts will be able to utilize Azure Synapse Link for Cosmos DB NoSQL.

**Technical Mechanisms and Implementation Methods**  
Azure Synapse Link operates by creating a seamless bridge between Azure Cosmos DB NoSQL and Azure Synapse Analytics. It leverages a native integration that allows data from Cosmos DB NoSQL to be automatically available in Synapse Analytics without the need for ETL (Extract, Transform, Load) processes. This is achieved through a managed analytical store within Cosmos DB, which Synapse Analytics can query directly. The retirement means that this integration mechanism will no longer be available for new accounts after the specified date, and will cease entirely after March 31, 2029.

**Use Cases and Application Scenarios**  
Typical use cases for Azure Synapse Link include real-time analytics, operational reporting, and business intelligence on data stored in Azure Cosmos DB NoSQL. Organizations have used Synapse Link to build dashboards, perform ad-hoc queries, and generate insights from their operational data without impacting transactional workloads. The retirement will affect scenarios where customers plan to leverage Synapse Link for new Cosmos DB NoSQL deployments, requiring them to seek alternative solutions for real-time analytics.

**Important Considerations and Limitations**  
- New Cosmos DB NoSQL accounts cannot enable Synapse Link after March 31, 2026.
- Existing accounts with Synapse Link enabled will continue to be supported until March 31, 2029.
- After the end-of-life date, Synapse Link will be unavailable for all Cosmos DB NoSQL accounts.
- Customers are encouraged to begin migration planning to alternative analytics solutions before support ends.
- The update does not affect other Azure Synapse Link integrations (e.g., with Cosmos DB for MongoDB or other data sources), unless specified in separate announcements.

**Integration with Related Azure Services**  
Azure Synapse Link has been a critical integration point between Azure Cosmos DB NoSQL and Azure Synapse Analytics, enabling seamless data movement and analytics. The retirement will require customers to evaluate other Azure services for similar functionality, such as Azure Data Factory for ETL, or direct integration between Cosmos DB and other analytics platforms.

**Summary Sentence**  
Azure Synapse Link for Azure Cosmos DB NoSQL will be retired, with new accounts unable to enable the feature after March 31, 2026, and full end-of-life support ending on March 31, 2029; customers should begin migration planning to alternative analytics solutions.

---

### 3. Retirement: Azure VPN Client for Linux (Preview) will be retired on August 31, 2026 

**Published**: June 10, 2026 16:15:16 UTC
**Link**: [Retirement: Azure VPN Client for Linux (Preview) will be retired on August 31, 2026 ](https://azure.microsoft.com/updates?id=565393)

**Update ID**: 565393
**Data source**: Azure Updates API

**Categories**: Networking, Security, Virtual WAN, VPN Gateway, Retirements

**Summary**:

- What was updated  
The Azure VPN Client for Linux (Preview) will be retired on August 31, 2026. This client has remained in public preview and will not reach general availability (GA).

- Key changes or new features  
No new features are being introduced. The key change is the official retirement announcement of the Azure VPN Client for Linux (Preview). After August 31, 2026, the client will no longer be supported or available.

- Target audience affected  
Developers, IT professionals, and organizations currently using or planning to use the Azure VPN Client for Linux (Preview) to connect to Azure Virtual Networks are directly affected.

- Important notes if any  
Users should plan to transition to alternative VPN solutions before the retirement date. Microsoft recommends using other supported VPN clients for Linux to maintain secure connectivity to Azure resources. There is no migration path from the preview client, and continued use after retirement may pose security and reliability risks. Review your current deployments and update documentation and processes accordingly.  
For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=565393).

**Details**:

**Azure Update Report: Retirement of Azure VPN Client for Linux (Preview) – Effective August 31, 2026**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of the Azure VPN Client for Linux (Preview), effective August 31, 2026. This client has remained in public preview and will not progress to general availability (GA). The retirement aligns with Microsoft’s ongoing efforts to ensure Azure networking services meet current security and reliability standards, and to streamline service offerings by discontinuing preview features that do not meet these criteria.

**Specific Features and Detailed Changes**  
The Azure VPN Client for Linux (Preview) enables Linux-based devices to connect to Azure Virtual Network (VNet) gateways using VPN protocols. The retirement notice means that after August 31, 2026, this client will no longer be supported or available for use. No new features, security updates, or technical support will be provided for the Linux VPN client beyond this date. Existing deployments relying on this client must transition to alternative solutions before the retirement deadline to maintain secure and supported VPN connectivity.

**Technical Mechanisms and Implementation Methods**  
The Azure VPN Client for Linux (Preview) facilitates secure point-to-site (P2S) VPN connections, typically leveraging protocols such as OpenVPN or IKEv2, to connect Linux endpoints to Azure VNets. The client is installed on Linux distributions and configured to authenticate and establish encrypted tunnels with Azure VPN gateways. With the retirement, the technical mechanism for Linux-based P2S VPN connectivity via this specific client will be deprecated, requiring users to adopt other supported VPN clients or methods.

**Use Cases and Application Scenarios**  
The primary use case for the Azure VPN Client for Linux (Preview) is enabling secure remote access for Linux users, developers, or automated workloads to resources within Azure VNets. This is common in hybrid cloud scenarios, development and testing environments, or for remote administration of Azure resources from Linux endpoints. After retirement, organizations must evaluate alternative VPN solutions to maintain these scenarios, such as using native Linux VPN clients compatible with Azure-supported protocols.

**Important Considerations and Limitations**  
- After August 31, 2026, the Azure VPN Client for Linux (Preview) will be unsupported and may become unavailable for download or use.
- No further security patches or bug fixes will be released, increasing potential risk if the client is used beyond the retirement date.
- Organizations must plan migration strategies to alternative VPN solutions for Linux endpoints to ensure continued secure access to Azure VNets.
- The retirement only affects the Linux (Preview) client; other Azure VPN clients (e.g., for Windows) are not impacted.

**Integration with Related Azure Services**  
The Azure VPN Client for Linux (Preview) integrates with Azure Virtual Network Gateway to provide P2S VPN connectivity. It is typically used in conjunction with Azure Active Directory for authentication and Azure Network Security Groups for access control. With the retirement, integration workflows involving this client must be updated to use supported VPN clients or methods that are compatible with Azure’s networking and security services.

**Summary**  
The Azure VPN Client for Linux (Preview) will be retired on August 31, 2026, and will no longer be supported or available; organizations should transition to alternative VPN solutions for Linux endpoints to maintain secure connectivity to Azure Virtual Networks.

---


*This report was automatically generated - 2026-06-11 03:01:54 UTC*