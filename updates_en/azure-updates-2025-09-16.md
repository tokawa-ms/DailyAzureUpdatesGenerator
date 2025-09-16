# September 16, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 16, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 6 items

## Update List

### 1. Retirement: Azure Databricks Standard tier will retire by October 2026

**Published**: September 16, 2025 00:15:32 UTC
**Link**: [Retirement: Azure Databricks Standard tier will retire by October 2026](https://azure.microsoft.com/updates?id=502623)

**Update ID**: 502623
**Data source**: Azure Updates API

**Categories**: AI + machine learning, Analytics, Azure Databricks, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of the Azure Databricks Standard tier.

- Key changes or new features  
Starting April 1, 2026, Azure subscriptions will no longer support the creation of new Azure Databricks Standard tier workspaces. From October 1, 2026, all existing Standard tier workspaces will be retired and no longer supported.

- Target audience affected  
Developers and IT professionals who currently use or plan to use Azure Databricks Standard tier workspaces in their data analytics and AI workloads.

- Important notes if any  
Users should plan to migrate workloads from the Standard tier to other supported Azure Databricks tiers (such as Premium or Enterprise) well before the retirement dates to avoid service disruption. Early migration is recommended to ensure continuity and access to enhanced features available in higher tiers.

**Details**:

The announced retirement of the Azure Databricks Standard tier by October 2026 reflects Microsoft’s strategic effort to streamline and enhance the Azure Databricks service offerings, encouraging users to transition to more advanced tiers that provide improved performance, security, and feature sets. Effective April 1, 2026, Azure subscriptions will no longer permit the creation of new Standard tier workspaces, and from October 1, 2026, all existing Standard tier workspaces will be retired, necessitating migration to Premium or Enterprise tiers.

**Background and Purpose:**  
The Standard tier of Azure Databricks has historically served as an entry-level option for data engineering and analytics workloads, offering core Databricks functionalities at a lower cost. However, as data workloads grow in complexity and security requirements intensify, Microsoft aims to consolidate its offerings to tiers that better support enterprise-grade features such as role-based access control (RBAC), enhanced security, compliance certifications, and advanced collaboration tools. This retirement encourages customers to leverage the Premium or Enterprise tiers, which provide richer capabilities aligned with modern data governance and operational needs.

**Specific Features and Detailed Changes:**  
The key change is the cessation of the Standard tier workspace creation from April 1, 2026, and the complete retirement of existing Standard tier workspaces by October 1, 2026. The Standard tier lacks several advanced features present in Premium and Enterprise tiers, such as:

- Fine-grained access controls via Azure Active Directory integration  
- Audit logs and compliance monitoring  
- Advanced cluster security features (e.g., cluster log delivery, secure cluster connectivity)  
- Enhanced collaboration with role-based permissions on notebooks and jobs  

Users currently on the Standard tier will need to plan migration strategies to upgrade their workspaces to Premium or Enterprise tiers to maintain uninterrupted service and access to advanced features.

**Technical Mechanisms and Implementation Methods:**  
Migration involves workspace upgrade procedures supported by Azure Databricks, which typically include exporting notebooks, jobs, and configurations from the Standard tier workspace and importing them into a Premium or Enterprise tier workspace. Azure Databricks provides APIs and CLI tools to facilitate this process. Additionally, administrators should review cluster configurations, libraries, and integration points to ensure compatibility with the target tier’s capabilities.

From a technical standpoint, the Premium and Enterprise tiers leverage enhanced Azure Active Directory integration for authentication and authorization, enabling RBAC and conditional access policies. They also support integration with Azure Monitor and Azure Security Center for comprehensive monitoring and threat detection, which are not fully available in the Standard tier.

**Use Cases and Application Scenarios:**  
This update primarily impacts organizations using Azure Databricks for data engineering, machine learning, and analytics workloads on the Standard tier. Use cases involving sensitive data, regulatory compliance, or requiring collaboration across multiple teams will benefit from migrating to Premium or Enterprise tiers. For example:

- Enterprises implementing data governance frameworks will utilize RBAC and audit logging features.  
- Data science teams requiring collaborative notebook sharing with controlled access will leverage enhanced collaboration tools.  
- Organizations integrating Databricks with Azure Synapse Analytics, Azure Data Factory, or Azure Purview will find improved interoperability and security in higher tiers.

**Important Considerations and Limitations:**  
- Migration requires careful planning to avoid downtime or data loss; thorough testing in non-production environments is recommended.  
- Cost implications should be evaluated, as Premium and Enterprise tiers have higher pricing reflecting their advanced capabilities.  
- Some legacy workloads or scripts may require modification to align with new security or API requirements in upgraded tiers.  
- Customers should monitor the retirement timeline closely to ensure compliance and avoid service disruption.

**Integration with Related Azure Services:**  
Upgrading to Premium or Enterprise tiers enhances integration with Azure ecosystem services. For instance:  

- Azure Active Directory integration enables seamless identity management and conditional access policies.  
- Azure Monitor and Log Analytics provide detailed telemetry and diagnostics for Databricks clusters and jobs.  
- Azure Policy can enforce compliance standards across Databricks resources.  
- Integration with

---

### 2. Retirement: hsmPlatform 1 Keys in Azure Key Vault

**Published**: September 15, 2025 21:30:04 UTC
**Link**: [Retirement: hsmPlatform 1 Keys in Azure Key Vault](https://azure.microsoft.com/updates?id=494676)

**Update ID**: 494676
**Data source**: Azure Updates API

**Categories**: Security, Key Vault, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of support for hsmPlatform 1 keys in Azure Key Vault, effective September 15, 2028.

- Key changes or new features  
Support for hsmPlatform 1 keys will be discontinued. Users must transition their cryptographic keys to newer, supported key types or platforms within Azure Key Vault to maintain security and operational functionality.

- Target audience affected  
Developers and IT professionals who manage cryptographic keys in Azure Key Vault, particularly those using hsmPlatform 1 keys for hardware security module (HSM)-backed key operations.

- Important notes if any  
The retirement date is set well in advance (September 15, 2028) to allow ample time for migration. It is strongly recommended to plan and execute key migration to supported platforms promptly to avoid service disruptions and ensure compliance with security best practices. Review your current key inventory and update your key management processes accordingly. For detailed guidance, refer to Azure Key Vault documentation and migration resources.

**Details**:

The Azure update announces the planned retirement of support for hsmPlatform 1 keys in Azure Key Vault, effective September 15, 2028, as part of Microsoft’s ongoing efforts to enhance security and performance within its cryptographic key management services.

**Background and Purpose:**  
hsmPlatform 1 keys refer to a legacy hardware security module (HSM) platform used within Azure Key Vault for generating and storing cryptographic keys. Over time, advancements in HSM technology and cryptographic standards have rendered the original hsmPlatform 1 architecture less optimal in terms of security features, performance, and compliance with modern cryptographic requirements. The retirement aims to phase out this older platform to encourage customers to migrate to newer, more secure HSM platforms (such as hsmPlatform 2 or later), which provide improved cryptographic algorithms, enhanced key protection mechanisms, and better integration with Azure’s evolving security ecosystem.

**Specific Features and Detailed Changes:**  
The key change is the cessation of support for keys created or managed under the hsmPlatform 1 environment within Azure Key Vault. After September 15, 2028, any cryptographic operations involving these keys—such as encryption, decryption, signing, or key wrapping—will no longer be supported. Customers must migrate their keys to supported HSM platforms before this deadline to avoid service disruption. This update does not affect keys created on newer HSM platforms or software-protected keys.

**Technical Mechanisms and Implementation Methods:**  
Azure Key Vault’s HSM-backed keys are stored and managed within FIPS 140-2 Level 2 validated hardware security modules. The hsmPlatform 1 keys are tied to a specific generation of HSM hardware and firmware. The retirement involves disabling backend support for these keys, effectively preventing cryptographic operations on them. Migration typically involves exporting key material (where allowed by key type and policy) or re-creating keys on newer HSM platforms, followed by updating applications to reference the new keys. Azure provides tooling and APIs to facilitate key migration, including Key Vault’s key rotation and backup/restore features, though direct export of HSM-protected keys is generally restricted to maintain security.

**Use Cases and Application Scenarios:**  
This update primarily impacts organizations using Azure Key Vault for key management in scenarios such as data encryption at rest, secure key storage for application authentication, digital signing, and certificate management where keys are backed by hsmPlatform 1. Industries with stringent compliance requirements—such as finance, healthcare, and government—must ensure migration to maintain compliance with security standards and avoid operational risks. Applications relying on legacy keys for cryptographic operations need to plan and execute migration well ahead of the retirement date.

**Important Considerations and Limitations:**  
- Migration complexity depends on key type and exportability; some HSM-protected keys cannot be exported and must be recreated.  
- Applications must be updated to reference new key identifiers post-migration.  
- Testing is critical to ensure cryptographic operations continue seamlessly after migration.  
- Backup and recovery plans should be validated to prevent data loss.  
- The retirement timeline provides a multi-year window, but early planning is essential to avoid last-minute disruptions.  
- Customers should review their compliance requirements to ensure new HSM platforms meet necessary certifications.

**Integration with Related Azure Services:**  
Azure Key Vault integrates with numerous Azure services such as Azure Storage, Azure SQL Database, Azure Virtual Machines, and Azure App Service for key management and encryption. The retirement of hsmPlatform 1 keys necessitates coordinated updates across these services to reference migrated keys. Additionally, Azure Security Center and Azure Policy can be leveraged to monitor key usage and enforce migration policies. Azure Key Vault’s integration with Azure Active Directory for access control remains unchanged, but role assignments may need review if key identifiers change during migration.

In summary, the retirement of hsmPlatform 1 keys in Azure Key Vault by September 15, 2028, reflects Microsoft’s commitment to advancing cryptographic

---

### 3. Generally Available: Enabling dedicated connections to backends in Azure Application Gateway

**Published**: September 15, 2025 16:45:57 UTC
**Link**: [Generally Available: Enabling dedicated connections to backends in Azure Application Gateway](https://azure.microsoft.com/updates?id=503398)

**Update ID**: 503398
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Services, Features, Management

**Summary**:

- What was updated  
Azure Application Gateway V2 now supports enabling dedicated connections from the gateway to backend servers.

- Key changes or new features  
Previously, Application Gateway reused idle backend TCP connections to optimize resource usage. With this update, developers and IT professionals can configure dedicated connections that persist exclusively between the gateway and specific backend servers. This feature enhances connection stability and performance for workloads requiring consistent backend connectivity, such as stateful applications or those sensitive to connection reuse.

- Target audience affected  
Developers and IT professionals managing Azure Application Gateway deployments, particularly those running stateful or connection-sensitive backend applications, will benefit from this capability.

- Important notes if any  
Enabling dedicated connections may increase the number of TCP connections and resource consumption on both the Application Gateway and backend servers. It is recommended to evaluate the impact on resource utilization and performance before enabling this feature in production environments. The feature is generally available and can be configured via Azure Portal, CLI, or ARM templates.

**Details**:

The recent Azure update announces the general availability of a new feature in Azure Application Gateway V2 that enables dedicated connections from the Application Gateway to backend servers. This enhancement addresses connection management by allowing IT professionals to configure persistent, non-shared TCP connections between the gateway and backend pools, diverging from the previous default behavior of connection reuse.

**Background and Purpose**  
Azure Application Gateway, a Layer 7 load balancer, optimizes traffic routing to backend servers. Traditionally, it reuses idle backend connections to conserve TCP resources and improve performance by reducing connection establishment overhead. However, certain backend applications or protocols may require dedicated connections for reasons such as session affinity, transaction consistency, or compliance with backend server connection policies. This update introduces the ability to explicitly enable dedicated connections, providing finer control over backend connectivity and improving compatibility with such scenarios.

**Specific Features and Detailed Changes**  
- **Dedicated Backend Connections:** Users can now configure Application Gateway to establish dedicated TCP connections to backend servers instead of reusing idle connections.  
- **Granular Control:** This setting can be applied per backend pool, allowing selective use of dedicated connections where needed.  
- **Backward Compatibility:** The default behavior remains connection reuse, ensuring existing deployments are unaffected unless explicitly changed.  
- **Improved Session Handling:** Dedicated connections help maintain session state and improve reliability for backends sensitive to connection sharing.

**Technical Mechanisms and Implementation Methods**  
Under the hood, enabling dedicated connections modifies the connection pooling logic within the Application Gateway’s backend HTTP(S) connection management. Instead of placing backend connections into a shared idle pool for reuse, the gateway maintains persistent, exclusive TCP connections per client request or session as configured. This reduces connection multiplexing but increases isolation between client sessions and backend connections. The feature is exposed via the Application Gateway configuration API and Azure Portal, allowing administrators to toggle dedicated connection settings on backend pools. The gateway continues to support HTTP/2 and WebSocket protocols with this feature enabled.

**Use Cases and Application Scenarios**  
- **Stateful Applications:** Applications requiring session affinity or sticky sessions that depend on dedicated TCP connections benefit from this feature.  
- **Compliance and Security:** Backends enforcing strict connection policies or requiring dedicated channels for auditing or security reasons can leverage dedicated connections.  
- **Legacy Systems:** Older backend systems that do not handle connection reuse gracefully can maintain stability with dedicated connections.  
- **High Transaction Consistency:** Financial or transactional applications where connection reuse might cause issues with transaction isolation.

**Important Considerations and Limitations**  
- **Resource Utilization:** Dedicated connections increase the number of open TCP connections, potentially increasing resource consumption on both the Application Gateway and backend servers. Capacity planning should account for this.  
- **Scalability Impact:** The reduction in connection reuse may affect scalability under high load, requiring performance testing.  
- **Compatibility:** While generally beneficial, some backend architectures optimized for connection reuse might see degraded performance.  
- **Configuration Scope:** The feature applies at the backend pool level and cannot be set per individual backend server or request.  
- **No Impact on Frontend Connections:** This feature only affects backend connections; frontend client connections remain managed separately.

**Integration with Related Azure Services**  
This update integrates seamlessly with Azure Monitor and Azure Network Watcher, enabling monitoring of connection metrics and diagnostics for dedicated backend connections. It complements Azure Front Door and Azure Traffic Manager by providing enhanced backend connection control within Application Gateway’s regional load balancing. When combined with Azure Web Application Firewall (WAF) on Application Gateway, dedicated connections can improve inspection accuracy for stateful traffic. Additionally, this feature aligns with Azure Private Link and Virtual Network service endpoints by maintaining dedicated, secure backend connectivity within private networks.

In summary, the general availability of dedicated backend connections in Azure Application Gateway V2 empowers IT professionals with enhanced control over TCP connection management to backend servers, improving compatibility with stateful and compliance-sensitive applications while requiring mindful resource and scalability considerations.

---

### 4. Generally Available: Backend TLS validation controls in Azure Application Gateway

**Published**: September 15, 2025 16:30:18 UTC
**Link**: [Generally Available: Backend TLS validation controls in Azure Application Gateway](https://azure.microsoft.com/updates?id=503393)

**Update ID**: 503393
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Services, Features, Management

**Summary**:

- What was updated  
Azure Application Gateway V2 now generally supports customer-controlled backend TLS validation.

- Key changes or new features  
When configuring HTTPS in Backend Settings, customers can customize TLS validation parameters for backend servers. Previously, Application Gateway performed default TLS certificate and hostname validations automatically. With this update, developers and IT professionals gain granular control over TLS handshake validations, enabling scenarios such as custom certificate authorities, relaxed hostname checks, or stricter validation policies tailored to backend environments.

- Target audience affected  
Developers and IT professionals managing secure application delivery with Azure Application Gateway, especially those requiring advanced TLS validation configurations for backend HTTPS endpoints.

- Important notes if any  
This feature is generally available, ensuring production readiness and support. It enhances security posture and flexibility but requires careful configuration to avoid weakening TLS protections unintentionally. Users should review backend certificate management and validation needs before customizing these settings.

For more details, visit: https://azure.microsoft.com/updates?id=503393

**Details**:

The recent general availability of backend TLS validation controls in Azure Application Gateway V2 introduces enhanced security and configurability for HTTPS backend communication by allowing customers to explicitly manage TLS validation behavior during backend connection establishment.

**Background and Purpose:**  
Azure Application Gateway is a Layer 7 load balancer that supports secure end-to-end HTTPS communication between clients and backend pools. Previously, when HTTPS was selected for backend settings, the Application Gateway performed standard TLS validations automatically during the TLS handshake with backend servers. However, these validations were fixed and not configurable by customers, limiting flexibility in scenarios such as custom certificate chains, private CAs, or specific compliance requirements. The update addresses this by enabling customer-controlled backend TLS validation, enhancing security posture and operational control.

**Specific Features and Detailed Changes:**  
- Customers can now explicitly configure backend TLS validation parameters, including enabling or disabling certificate chain validation, hostname verification, and trusted root CA selection.  
- This control is available when HTTPS is selected as the backend protocol in the Application Gateway’s backend HTTP settings.  
- The update supports granular validation policies, allowing scenarios where backend certificates may be self-signed or issued by private CAs, which previously could cause connection failures due to strict default validation.  
- The feature is integrated into the Application Gateway V2 SKU, leveraging its improved performance and scalability.

**Technical Mechanisms and Implementation Methods:**  
- During the TLS handshake initiated by the Application Gateway to the backend pool, the gateway’s TLS client stack performs certificate validation based on configured policies.  
- Customers configure validation settings via Azure Portal, ARM templates, or Azure CLI by specifying parameters such as trusted root certificates (uploading custom CA certificates), enabling/disabling hostname verification, and toggling certificate revocation checks.  
- The Application Gateway uses these settings to validate the backend server’s presented certificate chain, ensuring it matches the expected trust anchors and hostname, or bypassing checks as configured.  
- This flexibility is implemented at the TLS client layer within the Application Gateway’s backend connection management module.

**Use Cases and Application Scenarios:**  
- Enterprises using private or internal PKI infrastructures can configure Application Gateway to trust internal CA certificates, enabling secure HTTPS backend communication without exposing private keys or certificates externally.  
- Applications with backend services using self-signed certificates can selectively disable strict validation to maintain encrypted communication while avoiding connection failures.  
- Compliance-driven environments can enforce strict hostname and certificate chain validation to meet regulatory requirements for secure communications.  
- Multi-tenant or hybrid cloud architectures where backend services have diverse certificate management policies benefit from tailored TLS validation controls.

**Important Considerations and Limitations:**  
- Disabling certificate validation or hostname verification can expose backend communication to man-in-the-middle attacks; thus, these options should be used cautiously and only when necessary.  
- Custom trusted root certificates must be managed securely and updated as needed to avoid service disruptions due to expired or revoked certificates.  
- The feature is available only on Application Gateway V2 SKU; older versions do not support these controls.  
- Changes to TLS validation settings may require Application Gateway restart or reconfiguration to take effect.  
- Monitoring and logging should be enhanced to detect TLS validation failures or misconfigurations.

**Integration with Related Azure Services:**  
- Integration with Azure Key Vault allows secure storage and management of custom trusted root certificates uploaded for backend TLS validation.  
- Azure Monitor and Azure Network Watcher can be used to track Application Gateway health and TLS handshake metrics, aiding in troubleshooting validation issues.  
- When used with Azure Front Door or Azure Firewall, Application Gateway’s backend TLS validation complements end-to-end security strategies by ensuring encrypted and validated backend connections.  
- Azure Policy can enforce governance around Application Gateway configurations, including TLS validation settings, to maintain organizational security standards.

In summary, the general availability of backend TLS validation controls in Azure Application Gateway V2 empowers IT professionals to finely tune HTTPS backend security by managing certificate validation policies, enabling secure, compliant, and flexible backend communication tailored to diverse enterprise environments.

---

### 5. Generally Available: Azure SQL hub experience in Azure portal 

**Published**: September 15, 2025 16:30:18 UTC
**Link**: [Generally Available: Azure SQL hub experience in Azure portal ](https://azure.microsoft.com/updates?id=502014)

**Update ID**: 502014
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Azure SQL, Features

**Summary**:

- What was updated  
Azure SQL hub experience is now generally available in the Azure portal.

- Key changes or new features  
The Azure SQL hub provides a centralized, unified interface for managing all Azure SQL resources, including Azure SQL Database, Managed Instance, and SQL Virtual Machines. It simplifies service selection and management by consolidating monitoring, deployment, and configuration tools into a single pane of glass. The hub offers guided workflows, resource recommendations, and quick access to performance insights and security features.

- Target audience affected  
Developers and IT professionals who deploy, manage, or monitor Azure SQL services will benefit from this streamlined experience. It is especially useful for users who work across multiple Azure SQL deployment options or are evaluating which service best fits their needs.

- Important notes if any  
The hub is designed to reduce complexity and improve productivity by providing consistent tooling and visibility across Azure SQL offerings. Users should explore the hub to leverage integrated features like performance tuning recommendations and security management. Existing workflows remain supported, but the hub is recommended for a more efficient management experience.

For more details, visit: https://azure.microsoft.com/updates?id=502014

**Details**:

The Azure SQL hub experience, now generally available in the Azure portal, consolidates all Azure SQL-related services and management capabilities into a unified, streamlined interface designed to simplify service selection, deployment, and administration for IT professionals. This update addresses the complexity and fragmentation previously encountered when navigating multiple Azure SQL offerings—such as Azure SQL Database, Managed Instance, and SQL Server on Azure VMs—by providing a centralized entry point that enhances productivity and governance.

**Background and Purpose:**  
Azure offers several SQL-based data platform services tailored to different workload requirements, including single databases, elastic pools, managed instances, and SQL Server VMs. Historically, managing these disparate services required navigating separate blades or portals, which could lead to confusion, inefficiencies, and increased learning curves. The Azure SQL hub was introduced to unify these experiences, enabling users to discover, provision, monitor, and manage all Azure SQL resources from a single, coherent portal experience. This update aims to reduce complexity, improve discoverability of features, and accelerate time-to-value for database professionals.

**Specific Features and Detailed Changes:**  
- **Centralized Dashboard:** The hub provides a consolidated dashboard that displays all Azure SQL resources across subscriptions and regions, with filtering and grouping capabilities to facilitate resource management at scale.  
- **Simplified Service Selection:** Users can compare and select the most appropriate Azure SQL service based on workload needs, performance tiers, and pricing options, aided by contextual guidance and recommendations embedded within the hub.  
- **Unified Management Tools:** Integrated tools for performance monitoring, query performance insights, vulnerability assessments, and backup management are accessible directly from the hub, eliminating the need to switch contexts.  
- **Quick Start and Learning Resources:** The hub includes links to documentation, tutorials, and best practices, supporting both new and experienced users in optimizing their Azure SQL deployments.  
- **Resource Creation and Migration:** Streamlined workflows for creating new databases or migrating existing SQL Server workloads into Azure SQL services are embedded, with guided steps and validation checks.

**Technical Mechanisms and Implementation Methods:**  
The Azure SQL hub leverages the Azure Resource Manager (ARM) framework to aggregate and manage SQL resources across subscriptions. It uses REST APIs and Azure Monitor integration to pull real-time telemetry and health data, which is then visualized within the portal using Azure portal’s extensible UX framework. Role-Based Access Control (RBAC) and Azure Active Directory (AAD) authentication ensure secure access aligned with organizational policies. The hub also integrates with Azure Advisor and Azure Cost Management APIs to provide optimization recommendations and cost insights.

**Use Cases and Application Scenarios:**  
- **Enterprise Database Administrators:** Gain a holistic view of all SQL workloads, enabling proactive monitoring and management across hybrid environments.  
- **Developers and DevOps Teams:** Quickly provision appropriate SQL services aligned with application requirements without deep expertise in each service variant.  
- **Migration Projects:** Simplify assessment and migration of on-premises SQL Server databases to Azure SQL Database or Managed Instance using guided workflows.  
- **Cost and Performance Optimization:** Continuously monitor resource utilization and receive actionable recommendations to optimize performance and reduce costs.

**Important Considerations and Limitations:**  
- The hub experience requires users to have appropriate permissions (e.g., Contributor or higher) to view and manage SQL resources across subscriptions.  
- Some advanced configurations or niche features may still require navigation to specific service blades or use of PowerShell/CLI tools.  
- The hub currently focuses on Azure SQL services and does not integrate with non-SQL Azure data services such as Cosmos DB or Azure Database for PostgreSQL/MySQL.  
- Real-time telemetry depends on Azure Monitor and diagnostic settings being properly configured on the SQL resources.

**Integration with Related Azure Services:**  
The Azure SQL hub tightly integrates with Azure Monitor for performance and health metrics, Azure Security Center for vulnerability assessments, Azure Advisor for optimization recommendations, and Azure Cost Management for budgeting and cost tracking. It also interoperates with Azure Data Factory and Azure Migrate services to facilitate

---

### 6. Retirement: Azure Linux 2.0 on AKS 

**Published**: September 15, 2025 13:45:52 UTC
**Link**: [Retirement: Azure Linux 2.0 on AKS ](https://azure.microsoft.com/updates?id=500645)

**Update ID**: 500645
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Linux 2.0 on Azure Kubernetes Service (AKS), effective November 30, 2025.

- Key changes or new features  
Azure Linux 2.0 is being fully replaced by Azure Linux 3.0, which is the current supported version offering improved security, performance, and updated package support for AKS nodes.

- Target audience affected  
Developers and IT professionals managing AKS clusters using Azure Linux 2.0 node images must plan and execute migration to Azure Linux 3.0 before the retirement date to ensure continued support and security updates.

- Important notes if any  
Transitioning to Azure Linux 3.0 ahead of the November 30, 2025 deadline is strongly recommended to avoid disruptions. Azure Linux 3.0 provides ongoing support and enhancements, while Azure Linux 2.0 will no longer receive updates post-retirement. Review your AKS cluster configurations and update node images accordingly. For detailed guidance, refer to the official Azure update link.

**Details**:

The Azure update announces the retirement of Azure Linux 2.0 on Azure Kubernetes Service (AKS) effective November 30, 2025, urging users to transition to Azure Linux 3.0, which is the current supported and enhanced version. This update reflects Microsoft’s ongoing commitment to maintaining a secure, performant, and feature-rich Linux base image for AKS nodes.

**Background and Purpose:**  
Azure Linux 2.0 has served as a foundational OS image for AKS node pools, providing optimized Linux distributions tailored for Azure’s cloud environment. Over time, advancements in security, kernel improvements, and container runtime enhancements have necessitated a newer base OS. Azure Linux 3.0 replaces 2.0 to deliver improved security patches, updated software packages, and better integration with Azure infrastructure. The retirement aims to phase out older, less secure, and potentially unsupported OS versions to maintain compliance and operational excellence.

**Specific Features and Detailed Changes:**  
Azure Linux 3.0 introduces updated kernel versions, enhanced security features such as improved SELinux/AppArmor profiles, and updated container runtimes compatible with the latest Kubernetes versions. It also includes newer versions of system libraries and tools, better performance optimizations, and support for the latest Azure VM capabilities. Compared to Azure Linux 2.0, version 3.0 provides a more robust platform for running containerized workloads with improved stability and security.

**Technical Mechanisms and Implementation Methods:**  
Transitioning from Azure Linux 2.0 to 3.0 involves updating the node image version in AKS node pools. This can be done via the Azure CLI or Azure Portal by specifying the new node image SKU during node pool creation or upgrade. AKS supports node pool upgrades that allow rolling updates with minimal downtime. Users should plan to cordon and drain nodes running Azure Linux 2.0 workloads, then upgrade or recreate node pools with Azure Linux 3.0 images. Automation scripts leveraging Azure Resource Manager (ARM) templates or Terraform can facilitate this migration at scale.

**Use Cases and Application Scenarios:**  
This update is critical for organizations running containerized applications on AKS that require a secure and supported OS base. It is particularly relevant for production workloads demanding compliance with security standards, performance-sensitive applications benefiting from kernel and runtime improvements, and environments leveraging the latest Kubernetes features. Migrating to Azure Linux 3.0 ensures compatibility with new AKS capabilities and future Azure enhancements.

**Important Considerations and Limitations:**  
IT professionals should carefully test workloads on Azure Linux 3.0 in staging environments before production migration to identify any compatibility issues with custom software or drivers. Some legacy applications may require adjustments due to updated libraries or kernel changes. Additionally, the retirement deadline means that after November 30, 2025, Azure Linux 2.0 images will no longer receive security updates or support, potentially exposing workloads to vulnerabilities. Planning and executing the migration well in advance is essential to avoid service disruptions.

**Integration with Related Azure Services:**  
Azure Linux 3.0 integrates seamlessly with AKS and benefits from Azure’s security and monitoring services such as Azure Security Center, Azure Monitor, and Azure Policy. The updated OS supports enhanced telemetry and diagnostic capabilities, enabling better observability of containerized workloads. It also aligns with Azure’s managed identity and networking features, ensuring secure and efficient communication within Azure virtual networks and with other Azure services.

In summary, the retirement of Azure Linux 2.0 on AKS by November 30, 2025, requires IT professionals to transition to Azure Linux 3.0 to leverage improved security, performance, and compatibility. This involves updating node pool images through AKS management tools, thorough testing, and integration with Azure’s monitoring and security ecosystem to maintain a resilient and compliant Kubernetes environment.

---


*This report was automatically generated - 2025-09-16 03:03:13 UTC*