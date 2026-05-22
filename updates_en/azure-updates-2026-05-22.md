# May 22, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 22, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Generally Available: Entra-only identities with Azure Files

**Published**: May 21, 2026 22:00:20 UTC
**Link**: [Generally Available: Entra-only identities with Azure Files](https://azure.microsoft.com/updates?id=562359)

**Update ID**: 562359
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Files, Features, Microsoft Build, Security

**Summary**:

- What was updated  
Azure Files now supports generally available Entra-only identities for SMB access.

- Key changes or new features  
Organizations can use Microsoft Entra (formerly Azure Active Directory) cloud-native identities to securely access Azure file shares via SMB protocol. This eliminates the need for on-premises Active Directory or hybrid identity setups. Entra-only identities simplify authentication and management for Azure Files, supporting modern cloud-first environments.

- Target audience affected  
Developers and IT professionals managing file storage in Azure, especially those looking to reduce dependency on traditional Active directory or hybrid identity solutions.

- Important notes  
This update streamlines identity management for Azure Files and enhances security by leveraging Microsoft Entra. It is especially beneficial for organizations moving to cloud-only architectures or those seeking to simplify their infrastructure. Existing solutions using Active Directory or hybrid identities are still supported, but Entra-only identities offer a cloud-native alternative. Review documentation for compatibility and migration guidance.

**Details**:

**Azure Update Report: Generally Available – Entra-only identities with Azure Files**

**Background and Purpose of the Update**  
Azure Files has announced the general availability of Entra-only identities for SMB access. This update addresses the need for organizations to securely access Azure file shares using cloud-native identities, specifically Microsoft Entra identities, without the dependency on traditional Active Directory (AD) or hybrid identity infrastructure. The primary purpose is to streamline identity management and authentication for Azure Files, reducing complexity and improving security by eliminating the requirement for on-premises or hybrid AD setups.

**Specific Features and Detailed Changes**  
- **Entra-only Identity Support:** Azure Files now allows access to file shares via SMB protocol using Microsoft Entra identities exclusively.  
- **No AD Dependency:** Organizations can authenticate users directly with Entra identities, bypassing the need for Windows Server AD or Azure AD DS.  
- **Cloud-native Authentication:** The update enables fully cloud-based authentication scenarios for Azure Files, supporting modern identity management practices.

**Technical Mechanisms and Implementation Methods**  
- **SMB Access with Entra Identities:** Users authenticate to Azure Files over SMB using their Microsoft Entra credentials.  
- **Identity Management:** Entra-only authentication leverages Microsoft Entra ID (formerly Azure AD) for managing user identities and access permissions.  
- **Access Control:** Permissions to Azure file shares are managed through Entra identity assignments, ensuring granular access control without AD group policies or hybrid configurations.

**Use Cases and Application Scenarios**  
- **Cloud-native Environments:** Ideal for organizations that have fully migrated to cloud-based identity management and do not maintain on-premises AD infrastructure.  
- **Simplified File Share Access:** Enables secure access to Azure file shares for remote or distributed teams using only Entra identities.  
- **Modern Workloads:** Supports scenarios where legacy AD dependencies are impractical, such as in cloud-first or cloud-only deployments.

**Important Considerations and Limitations**  
- **No AD or Hybrid Required:** This update is specifically for environments where AD or hybrid identity infrastructure is not present or needed.  
- **SMB Protocol:** The Entra-only identity feature is available for SMB access; organizations must ensure their workloads are compatible with SMB and Entra authentication.  
- **Security and Compliance:** IT professionals should review their security policies to ensure Entra-only authentication aligns with organizational compliance requirements.

**Integration with Related Azure Services**  
- **Microsoft Entra ID:** Azure Files integrates natively with Microsoft Entra ID for authentication and access management.  
- **Azure Files:** The update enhances Azure Files by providing a new authentication method, broadening its applicability in cloud-native scenarios.  
- **No Dependency on Azure AD DS:** Unlike previous configurations, Azure Files does not require Azure AD Domain Services for identity management when using Entra-only identities.

**Summary Sentence**  
Azure Files now supports general availability of Entra-only identities for SMB access, enabling organizations to securely access file shares using cloud-native Microsoft Entra identities without the need for Active Directory or hybrid identity infrastructure.

---

### 2. Generally Available: Azure NetApp Files object REST API 

**Published**: May 21, 2026 21:45:32 UTC
**Link**: [Generally Available: Azure NetApp Files object REST API ](https://azure.microsoft.com/updates?id=562254)

**Update ID**: 562254
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files now offers a Generally Available (GA) Object REST API, which is S3-compatible.

- Key changes or new features  
The Object REST API enables S3-compatible access to Azure NetApp Files, allowing integration of traditional file-based storage with modern cloud services. Developers can use familiar S3 REST operations to interact with data stored in Azure NetApp Files, facilitating new use cases such as cloud-native applications, analytics, and hybrid workloads. The API supports seamless integration, enabling existing tools and applications that use S3 to work with Azure NetApp Files without major changes.

- Target audience affected  
This update is relevant for developers building cloud-native or hybrid applications, IT professionals managing storage infrastructure, and organizations seeking to modernize legacy workloads or leverage S3-compatible tools in Azure.

- Important notes if any  
The Object REST API is now generally available and production-ready. It provides a bridge between file-based and object-based storage paradigms, helping organizations maximize their data utility in Azure. Review the documentation for supported operations and compatibility considerations before integrating into production environments.

Link: [Azure Update](https://azure.microsoft.com/updates?id=562254)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure NetApp Files object REST API  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=562254)

---

**Background and Purpose of the Update**

Azure NetApp Files (ANF) is a managed file storage service designed for enterprise workloads requiring high performance and reliability. Traditionally, ANF has provided file-based access protocols such as NFS and SMB. The introduction of the Object REST API, which is S3-compatible, addresses the growing need for cloud-native applications to access data using object storage paradigms. This update bridges the gap between legacy file-based storage and modern cloud services, allowing organizations to leverage their existing data in new ways without migration or duplication.

---

**Specific Features and Detailed Changes**

- **S3-Compatible REST API:** The Object REST API enables S3-compatible access to Azure NetApp Files, allowing applications and services that use S3 protocols to interact directly with ANF storage.
- **Seamless Integration:** Users can access their existing file-based data through object storage APIs, facilitating hybrid access models.
- **General Availability:** The API is now generally available, ensuring production-grade support and reliability for enterprise workloads.

---

**Technical Mechanisms and Implementation Methods**

- **API Endpoint:** The Object REST API exposes endpoints compatible with S3 operations, such as PUT, GET, DELETE, and LIST, enabling CRUD operations on objects stored within ANF volumes.
- **Data Access Translation:** The API translates object storage requests into underlying file system operations, allowing data stored in ANF to be accessed as objects without restructuring or migration.
- **Authentication and Security:** The API supports authentication mechanisms aligned with Azure security standards, ensuring secure access and integration with Azure Active Directory and role-based access control (RBAC).
- **Performance and Scalability:** The API leverages ANF’s high-performance infrastructure, ensuring low latency and high throughput for object operations.

---

**Use Cases and Application Scenarios**

- **Cloud-Native Application Integration:** Applications designed for S3 object storage can now interact with ANF without modification, enabling rapid adoption of cloud-native architectures.
- **Data Analytics and AI:** Data stored in ANF can be accessed by analytics and AI platforms that require object storage interfaces, facilitating advanced processing and insights.
- **Hybrid Workloads:** Organizations can maintain legacy file-based access while enabling object-based access for modern workloads, supporting a hybrid IT environment.
- **Backup and Archiving:** The API enables efficient backup and archival workflows by allowing object-based tools to interact with ANF storage.

---

**Important Considerations and Limitations**

- **Compatibility:** While the API is S3-compatible, users should verify specific feature support and limitations compared to AWS S3, especially for advanced operations or integrations.
- **Performance Tuning:** Optimal performance may require configuration adjustments based on workload characteristics and access patterns.
- **Security Configuration:** Proper authentication and authorization setup is essential to prevent unauthorized access, especially in multi-tenant environments.
- **Data Consistency:** Users should understand the consistency model provided by the API, particularly when accessing data concurrently via file and object protocols.

---

**Integration with Related Azure Services**

- **Azure Active Directory:** The API integrates with Azure AD for authentication and RBAC, supporting enterprise security requirements.
- **Azure Data Services:** The Object REST API enables interoperability with Azure data services such as Azure Data Lake, Azure Synapse Analytics, and Azure Machine Learning, which often require object storage interfaces.
- **Azure Backup and Recovery Solutions:** The API facilitates integration with Azure-native and third-party backup tools that leverage S3-compatible APIs.

---

**Summary Sentence**

The general availability of the S3-compatible Object REST API for Azure NetApp Files enables seamless object-based access to file storage, supporting hybrid workloads and modern cloud integrations while maintaining enterprise-grade performance and security.

---

### 3. Retirement:  TLS 1.0 and TLS 1.1 in Azure App Service, Azure Functions, and Azure Logic Apps

**Published**: May 21, 2026 21:45:32 UTC
**Link**: [Retirement:  TLS 1.0 and TLS 1.1 in Azure App Service, Azure Functions, and Azure Logic Apps](https://azure.microsoft.com/updates?id=557852)

**Update ID**: 557852
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, Containers, Internet of Things, Integration, App Service, Azure Functions, Logic Apps, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of TLS 1.0 and TLS 1.1 support for Azure App Service, Azure Functions, and Azure Logic Apps.

- Key changes or new features  
Starting June 1, 2027, these Azure services will no longer accept connections using TLS 1.0 or TLS 1.1. Only TLS 1.2 and above will be supported for secure communications. Any client, application, or service attempting to connect using the deprecated TLS versions will be blocked.

- Target audience affected  
Developers, IT professionals, and application owners using Azure App Service, Azure Functions, or Azure Logic Apps, especially those managing legacy systems or clients that rely on TLS 1.0 or 1.1.

- Important notes if any  
It is critical to review and update all client applications, integrations, and dependencies to ensure they use TLS 1.2 or higher before May 31, 2027. Failure to update will result in connectivity issues and potential service disruptions. This change aligns with industry best practices for security and compliance. For more information, visit the official Azure Update: https://azure.microsoft.com/updates?id=557852

**Details**:

**Azure Update Report: Retirement of TLS 1.0 and TLS 1.1 in Azure App Service, Azure Functions, and Azure Logic Apps**

**Background and Purpose of the Update**  
This update is part of Azure’s ongoing commitment to enhance security across its cloud platform. Transport Layer Security (TLS) protocols are foundational for encrypting data in transit. TLS 1.0 and TLS 1.1 are legacy protocols with known vulnerabilities and are no longer considered secure by industry standards. The retirement of these protocols in Azure App Service, Azure Functions, and Azure Logic Apps is intended to mitigate security risks and align with best practices for secure communications.

**Specific Features and Detailed Changes**  
Effective after May 31, 2027, Azure App Service, Azure Functions, and Azure Logic Apps will reject all connections using TLS 1.0 and TLS 1.1. Only connections using TLS 1.2 or higher will be accepted. This change affects inbound connections to these services, meaning any client, application, or service attempting to connect using the deprecated TLS versions will fail to establish a secure session.

**Technical Mechanisms and Implementation Methods**  
Azure will enforce this update at the platform level. The underlying infrastructure for App Service, Functions, and Logic Apps will be configured to disable support for TLS 1.0 and TLS 1.1. This is typically achieved by updating the SSL/TLS configuration on load balancers, web servers, and gateway endpoints to only negotiate TLS 1.2 or above. No manual intervention is required from users to disable these protocols; the enforcement is automatic and global across affected services.

**Use Cases and Application Scenarios**  
This update impacts any scenario where clients or integrations connect to Azure App Service, Azure Functions, or Azure Logic Apps using TLS 1.0 or TLS 1.1. Common examples include legacy applications, outdated SDKs, or older devices and browsers that do not support TLS 1.2. Organizations must ensure that all client applications, APIs, and third-party integrations are updated to use TLS 1.2 or higher before the retirement date to avoid service disruptions.

**Important Considerations and Limitations**  
- **Deadline:** Connections using TLS 1.0 or TLS 1.1 will be blocked after May 31, 2027.
- **Compatibility:** All client software, libraries, and devices must support TLS 1.2 or higher.
- **Testing:** IT professionals should audit their environments and test connectivity using TLS 1.2 to ensure compatibility.
- **No Exception:** There will be no option to re-enable TLS 1.0 or TLS 1.1 after the retirement date.
- **Security Compliance:** This change supports compliance with PCI DSS, HIPAA, and other security standards that require strong encryption.

**Integration with Related Azure Services**  
This update is consistent with similar deprecations across Azure services, including Azure SQL Database, Azure Storage, and Azure Virtual Machines, which have also phased out legacy TLS protocols. Organizations using integrated solutions (e.g., Logic Apps calling Functions or App Service APIs) must ensure all components in the workflow support TLS 1.2 or higher. Azure monitoring tools and diagnostic logs can be used to identify and remediate affected connections.

**Summary Sentence**  
Azure will retire support for TLS 1.0 and TLS 1.1 in App Service, Functions, and Logic Apps after May 31, 2027, requiring all connections to use TLS 1.2 or higher to enhance platform security and align with industry standards.

---

### 4. Generally Available: User Groups and IP address pools for P2S connections

**Published**: May 21, 2026 18:45:42 UTC
**Link**: [Generally Available: User Groups and IP address pools for P2S connections](https://azure.microsoft.com/updates?id=564460)

**Update ID**: 564460
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, VPN Gateway, Feature

**Summary**:

- What was updated  
Azure VPN Gateway now supports User Groups and IP Address Pools for Point-to-Site (P2S) connections, and this feature is generally available.

- Key changes or new features  
Customers can now assign distinct IP address pools to remote users based on their credentials. This allows administrators to organize remote users into separate groups and allocate specific IP ranges to each group. This enables more granular control over network access, improved segmentation, and easier management of user connectivity.

- Target audience affected  
This update impacts IT professionals managing Azure networking infrastructure and developers building solutions that require secure remote access via VPN Gateway. Organizations with large or diverse remote user bases will benefit from enhanced control and security.

- Important notes if any  
To leverage this feature, administrators must configure user groups and IP address pools within the VPN Gateway settings. This update enhances security and compliance by allowing differentiated access and easier tracking of user activity. It is recommended to review and update existing P2S configurations to take advantage of these new capabilities.

**Details**:

**Azure Update: Generally Available – User Groups and IP Address Pools for Point-to-Site (P2S) Connections in VPN Gateway**

**Background and Purpose of the Update:**  
This update introduces the general availability of User Groups and IP Address Pools for Point-to-Site (P2S) connections in Azure VPN Gateway. The primary purpose is to enhance network segmentation and access control for remote users by allowing administrators to assign distinct IP address pools to users based on their credentials. This addresses the need for more granular management of remote user connections, improving security, compliance, and operational flexibility.

**Specific Features and Detailed Changes:**  
- **User Group Assignment:** Administrators can now organize remote users into separate groups. These groups are defined based on user credentials, typically integrated with Azure Active Directory or other identity providers.
- **Distinct IP Address Pools:** Each user group can be assigned a unique IP address pool. When a user connects via P2S VPN, they are dynamically allocated an IP address from the pool associated with their group.
- **Policy-Based IP Allocation:** The VPN Gateway enforces IP allocation policies based on user group membership, ensuring that users receive IP addresses from the correct pool.

**Technical Mechanisms and Implementation Methods:**  
- **Integration with Authentication:** User group membership is determined during the authentication process, leveraging credentials provided by the user. This is compatible with supported authentication methods such as Azure AD, RADIUS, or certificate-based authentication.
- **Configuration:** Administrators configure user groups and map them to IP address pools within the VPN Gateway settings. This is managed via the Azure Portal, PowerShell, or ARM templates.
- **Dynamic IP Assignment:** Upon successful authentication, the VPN Gateway references the user’s group and assigns an IP address from the corresponding pool. This process is transparent to the end user.

**Use Cases and Application Scenarios:**  
- **Network Segmentation:** Organizations can segment remote user traffic by department, role, or project, assigning different IP ranges to each group for improved security and monitoring.
- **Access Control:** By associating IP pools with firewall rules or network security groups, administrators can enforce differentiated access policies based on user group.
- **Compliance:** Enterprises with regulatory requirements can isolate sensitive user groups and audit their network activity more effectively.

**Important Considerations and Limitations:**  
- **Credential Dependency:** Accurate group assignment depends on the integrity of user credentials and proper configuration of authentication providers.
- **IP Pool Management:** Administrators must ensure that IP address pools do not overlap and are sized appropriately to accommodate expected group membership.
- **Compatibility:** This feature is specific to Point-to-Site connections and may not apply to Site-to-Site or VNet-to-VNet scenarios.

**Integration with Related Azure Services:**  
- **Azure Active Directory:** User group definitions can be synchronized with Azure AD, enabling seamless integration with existing identity management workflows.
- **Network Security Groups (NSGs) and Azure Firewall:** Assigned IP pools can be used as source criteria in NSG or firewall rules, allowing for group-based security policies.
- **Monitoring and Logging:** IP address allocation by group can be tracked using Azure Monitor and Network Watcher for auditing and troubleshooting.

**Summary:**  
User Groups and IP Address Pools for P2S connections in Azure VPN Gateway are now generally available, enabling administrators to assign distinct IP address pools to remote users based on their credentials, thereby enhancing network segmentation, security, and policy enforcement for remote access scenarios.

---

### 5. Public Preview: TLS/SSL certificate support for Azure Functions Flex Consumption 

**Published**: May 21, 2026 18:45:42 UTC
**Link**: [Public Preview: TLS/SSL certificate support for Azure Functions Flex Consumption ](https://azure.microsoft.com/updates?id=562808)

**Update ID**: 562808
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Functions Flex Consumption now supports TLS/SSL certificates in public preview, introducing a site-scoped certificate model.

- Key changes or new features  
The new site-scoped certificate model allows each Azure Function app on Flex Consumption to have its own dedicated TLS/SSL certificate. This differs from webspace-scoped certificates used in other hosting plans, which are shared across apps within the same region and resource group. The update provides improved isolation and security for individual apps, making certificate management more granular and flexible.

- Target audience affected  
Developers and IT professionals deploying Azure Functions on the Flex Consumption plan, especially those requiring custom TLS/SSL certificates for enhanced security or compliance.

- Important notes if any  
This feature is currently in public preview and available in all regions where Flex Consumption is supported. Users should note that the certificate model is unique to Flex Consumption and may require adjustments to existing deployment or certificate management workflows. For production workloads, monitor for updates as the feature matures beyond preview.  
Link: [Azure Update](https://azure.microsoft.com/updates?id=562808)

**Details**:

**Azure Update Report: Public Preview – TLS/SSL Certificate Support for Azure Functions Flex Consumption**

**Background and Purpose of the Update:**  
Azure Functions Flex Consumption is a hosting plan designed to provide enhanced flexibility and scalability for serverless workloads. Traditionally, TLS/SSL certificates in Azure App Service environments have been managed at the webspace scope, meaning certificates are shared across all applications within the same region and resource group. This update introduces site-scoped certificate support specifically for Flex Consumption, addressing the need for more granular and isolated certificate management at the individual application (site) level.

**Specific Features and Detailed Changes:**  
With this public preview, Flex Consumption now supports a site-scoped certificate model. This means that each Azure Function app deployed on Flex Consumption can have its own dedicated TLS/SSL certificate, rather than relying on a certificate shared across multiple apps in the same region and resource group. This model enhances security and operational flexibility, as certificate lifecycle management (issuance, renewal, and revocation) can be handled per app.

**Technical Mechanisms and Implementation Methods:**  
The site-scoped certificate model is implemented such that certificates are bound directly to the individual Function app instance. This is a departure from the webspace-scoped model, where certificates are associated with a logical grouping of apps (webspace) within a region and resource group. The new mechanism ensures that certificate bindings, storage, and management are isolated to the specific app, reducing the risk of cross-app certificate exposure and simplifying automation for certificate operations.

**Use Cases and Application Scenarios:**  
- **Multi-tenant Environments:** Organizations hosting multiple tenants or customers on separate Function apps can now provision unique certificates per tenant, ensuring isolation and compliance with security policies.
- **Zero Trust and Compliance:** Enterprises with strict regulatory requirements can enforce per-app certificate policies, supporting zero trust architectures.
- **Automated Certificate Management:** Teams leveraging CI/CD pipelines for app deployment can automate certificate provisioning and rotation at the app level, reducing operational overhead and risk.

**Important Considerations and Limitations:**  
- **Preview Availability:** This feature is in public preview and is available only in regions where Flex Consumption is supported.
- **Scope Restriction:** The site-scoped certificate model is exclusive to Flex Consumption and does not apply to other hosting plans or legacy webspace-scoped certificate configurations.
- **Operational Impact:** Migration from webspace-scoped to site-scoped certificates may require updates to deployment scripts and certificate automation processes.

**Integration with Related Azure Services:**  
Site-scoped certificates for Flex Consumption integrate with Azure’s existing certificate management workflows, including Azure Key Vault for secure certificate storage and Azure Resource Manager (ARM) for automated deployments. This enables seamless integration with other Azure security and automation services, such as Azure Policy for compliance enforcement and Azure DevOps for CI/CD.

**Summary:**  
The public preview of site-scoped TLS/SSL certificate support for Azure Functions Flex Consumption enables per-app certificate management, enhancing security, isolation, and operational flexibility for serverless workloads.

---


*This report was automatically generated - 2026-05-22 03:02:28 UTC*