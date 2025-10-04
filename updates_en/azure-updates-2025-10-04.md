# October 04, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 04, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 7 items

## Update List

### 1. Retirement: Azure Monitor SCOM Managed Instance will be retired on Sep 30, 2026

**Published**: October 03, 2025 18:15:20 UTC
**Link**: [Retirement: Azure Monitor SCOM Managed Instance will be retired on Sep 30, 2026](https://azure.microsoft.com/updates?id=501673)

**Update ID**: 501673
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Azure Monitor, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure Monitor SCOM Managed Instance, effective September 30, 2026.

- Key changes or new features  
After this date, the Azure Monitor SCOM Managed Instance service will no longer be accessible. No new features or updates will be provided as the service phases out.

- Target audience affected  
This update primarily affects IT professionals and developers who use Azure Monitor SCOM Managed Instance to monitor on-premises workloads integrated with Azure.

- Important notes if any  
Customers currently relying on Azure Monitor SCOM Managed Instance should plan to transition their on-premises monitoring workloads to Operations Manager on-premises solutions before the retirement date. It is essential to review the official retirement documentation to understand migration paths and avoid service disruption. Early planning is recommended to ensure continuity of monitoring capabilities beyond September 30, 2026.

For more details, visit: https://azure.microsoft.com/updates?id=501673

**Details**:

The Azure update announces the planned retirement of the Azure Monitor SCOM Managed Instance service effective September 30, 2026. This service currently enables integration between Azure Monitor and System Center Operations Manager (SCOM) by providing a managed instance that facilitates monitoring of on-premises workloads through Azure’s monitoring capabilities.

**Background and Purpose**  
Azure Monitor SCOM Managed Instance was introduced to bridge on-premises infrastructure monitoring with Azure Monitor, allowing organizations to leverage cloud-based analytics and alerting for their hybrid environments. Over time, Microsoft has evolved its hybrid monitoring strategy, emphasizing direct use of Operations Manager on-premises and enhanced Azure-native monitoring tools. The retirement aligns with this strategic shift, encouraging customers to transition away from the managed instance model toward more direct and supported monitoring solutions.

**Specific Features and Detailed Changes**  
The service retirement means that after September 30, 2026, the Azure Monitor SCOM Managed Instance will no longer be accessible or supported. Features such as automatic data ingestion from SCOM to Azure Monitor via the managed instance will cease. Customers relying on this integration will need to migrate their monitoring workflows to alternative solutions. The recommended path is to use Operations Manager directly on-premises for workload monitoring, potentially combined with Azure Monitor’s agent-based solutions or Azure Arc for hybrid environments.

**Technical Mechanisms and Implementation Methods**  
Azure Monitor SCOM Managed Instance functioned as a managed Azure resource that connected to an on-premises SCOM environment, receiving monitoring data and forwarding it to Azure Monitor. It abstracted the complexity of managing the integration infrastructure. Post-retirement, organizations must configure Operations Manager agents and management servers on-premises without relying on the managed instance. For hybrid monitoring, Azure Arc-enabled servers can be used to onboard on-premises machines directly into Azure Monitor, providing a more modern and flexible monitoring architecture.

**Use Cases and Application Scenarios**  
This service primarily served enterprises with hybrid environments needing centralized monitoring dashboards and alerting that combined on-premises and cloud resources. Typical scenarios included monitoring Windows and Linux servers, applications, and infrastructure components managed by SCOM, with data visualized and analyzed in Azure Monitor. After retirement, these use cases will be fulfilled by native Operations Manager deployments supplemented by Azure Arc and Azure Monitor agents, ensuring continuity of monitoring and alerting capabilities.

**Important Considerations and Limitations**  
Customers must plan their migration well before the retirement date to avoid monitoring disruptions. The transition involves reconfiguring monitoring agents, dashboards, and alert rules. There may be differences in data collection and visualization capabilities between the managed instance and direct Operations Manager or Azure Arc approaches, requiring validation and potential adaptation of monitoring strategies. Additionally, any automation or integrations dependent on the managed instance API will need to be refactored.

**Integration with Related Azure Services**  
Post-retirement, integration will rely more heavily on Azure Arc, which extends Azure management and governance to on-premises and multi-cloud environments, enabling direct onboarding of servers into Azure Monitor without intermediary managed instances. Azure Monitor agents (Log Analytics agents or Azure Monitor Agent) will collect telemetry data directly from on-premises resources. Operations Manager remains the core on-premises monitoring tool, and its integration with Azure Monitor via Azure Arc and agents will be the primary hybrid monitoring architecture going forward.

In summary, the retirement of Azure Monitor SCOM Managed Instance by September 30, 2026, signals a strategic shift towards direct on-premises Operations Manager use combined with Azure Arc-enabled hybrid monitoring. IT professionals should proactively plan migration to these supported architectures to maintain comprehensive monitoring coverage across hybrid environments. Detailed migration guidance is available in Microsoft’s retirement documentation.

---

### 2. Generally Available: CLI command for migration from Availability Sets and basic load balancer on AKS 

**Published**: October 03, 2025 16:45:25 UTC
**Link**: [Generally Available: CLI command for migration from Availability Sets and basic load balancer on AKS ](https://azure.microsoft.com/updates?id=503258)

**Update ID**: 503258
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) now provides a generally available Azure CLI command to migrate clusters from deprecated Availability Sets and the basic load balancer to the new Virtual Machines node pool model.

- Key changes or new features  
The update introduces a streamlined CLI command that automates the migration process of AKS clusters currently using Availability Sets and the basic load balancer. This migration moves clusters to use Virtual Machines node pools and upgraded load balancing infrastructure, improving scalability and future-proofing clusters ahead of the deprecation deadline.

- Target audience affected  
Developers and IT professionals managing AKS clusters that still rely on Availability Sets and the basic load balancer. This includes DevOps engineers responsible for cluster maintenance and upgrades.

- Important notes if any  
Availability Sets and the basic load balancer will be deprecated on September 30, 2025. It is critical to plan and execute the migration before this date to avoid service disruptions. The new CLI command simplifies the migration, reducing manual effort and potential errors. Users should test the migration in non-production environments before applying it to critical workloads.  

For detailed guidance and usage, refer to the official Azure update link: https://azure.microsoft.com/updates?id=503258

**Details**:

The Azure Kubernetes Service (AKS) update introduces a generally available Azure CLI command designed to facilitate the migration of AKS clusters from the deprecated Availability Sets and basic load balancer to the newer Virtual Machines node pool infrastructure, addressing the upcoming deprecation deadline of September 30, 2025.

**Background and Purpose:**  
Availability Sets and the basic load balancer have historically been used in AKS to provide high availability and load distribution for cluster nodes. However, these components are being deprecated to encourage adoption of more scalable, performant, and feature-rich alternatives such as Virtual Machine Scale Sets (VMSS) for node pools and the Standard Load Balancer. The update’s primary purpose is to streamline the migration process, reducing manual effort and minimizing downtime or configuration errors by providing a dedicated CLI command that automates the transition.

**Specific Features and Detailed Changes:**  
The key feature is a new Azure CLI command that automates the migration of existing AKS clusters from Availability Sets to VMSS-based node pools. This command handles the underlying infrastructure changes, including node reprovisioning and load balancer upgrades. It also upgrades the cluster configuration to leverage VMSS capabilities, such as improved scaling, rolling upgrades, and better integration with Azure monitoring and autoscaling features. The migration also replaces the basic load balancer with the Standard Load Balancer, which supports enhanced features like zone redundancy, higher throughput, and better health probe mechanisms.

**Technical Mechanisms and Implementation Methods:**  
Technically, the migration command orchestrates the creation of new VMSS node pools alongside or in replacement of existing Availability Set nodes. It coordinates draining and cordoning of pods, reprovisioning of nodes on VMSS, and seamless transfer of workloads. The command updates the AKS cluster’s control plane configuration to reference the new VMSS node pools and switches the networking components from the basic load balancer to the Standard Load Balancer. This process leverages Azure Resource Manager (ARM) templates and AKS APIs to ensure consistency and atomicity of changes. The migration is designed to be minimally disruptive, supporting rolling node replacements to maintain workload availability.

**Use Cases and Application Scenarios:**  
This update is critical for organizations running production AKS clusters on Availability Sets and basic load balancers who must comply with the deprecation timeline. It is especially relevant for clusters requiring improved scalability, reliability, and integration with advanced Azure features such as zone redundancy and autoscaling. Enterprises looking to modernize their Kubernetes infrastructure with minimal operational overhead will benefit from this automated migration. It also supports scenarios where clusters need to be upgraded to leverage newer AKS capabilities that depend on VMSS node pools.

**Important Considerations and Limitations:**  
Before initiating migration, it is important to verify cluster compatibility, including Kubernetes version and node pool configurations. Some custom configurations or third-party integrations might require validation post-migration. The migration command requires appropriate Azure RBAC permissions to modify cluster and infrastructure resources. Downtime is expected to be minimal but not zero; workloads should be prepared for transient disruptions during node reprovisioning. Additionally, the migration is irreversible; once moved to VMSS, reverting to Availability Sets is not supported. Users should also review any network security group (NSG) or load balancer rule customizations to ensure they persist or are reapplied correctly.

**Integration with Related Azure Services:**  
Post-migration, AKS clusters benefit from deeper integration with Azure Monitor for containers, Azure Autoscale, and Azure Policy due to VMSS support. The Standard Load Balancer enables zone-redundant deployments and improved network performance, enhancing resilience in multi-availability zone architectures. This update aligns AKS with Azure’s broader infrastructure modernization strategy, enabling better use of Azure Compute and Networking services and facilitating future AKS feature enhancements that depend on VMSS and Standard Load Balancer capabilities.

In summary, this Azure CLI migration command provides a streamlined, automated path for AKS clusters to transition from deprecated Availability Sets and basic load balancers to modern VMSS node

---

### 3. Generally Available: Cross-tenant customer-managed keys for Azure NetApp Files volume encryption

**Published**: October 03, 2025 16:15:04 UTC
**Link**: [Generally Available: Cross-tenant customer-managed keys for Azure NetApp Files volume encryption](https://azure.microsoft.com/updates?id=501340)

**Update ID**: 501340
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files now supports generally available cross-tenant Customer-Managed Keys (CMK) for volume encryption.

- Key changes or new features  
Customers can use their own encryption keys stored in Azure Key Vaults across different Azure Active Directory tenants to encrypt Azure NetApp Files volumes. This cross-tenant CMK capability provides enhanced security control and flexibility for organizations managing resources in multiple Azure tenancies. It enables centralized key management and compliance adherence by allowing developers and IT teams to maintain ownership of encryption keys independent of the Azure NetApp Files resource tenant.

- Target audience affected  
Developers, IT professionals, and security teams managing Azure NetApp Files in multi-tenant or multi-organization environments who require stringent encryption key control and compliance.

- Important notes if any  
Implementing cross-tenant CMK requires proper configuration of Azure Key Vault access policies and permissions across tenants. Ensure coordination between tenant administrators to establish secure key access. This feature supports improved data protection strategies but adds complexity in key lifecycle management that teams should plan for accordingly.  

For more details, visit: https://azure.microsoft.com/updates?id=501340

**Details**:

The recent general availability of Cross-tenant Customer-Managed Keys (CMK) for Azure NetApp Files volume encryption introduces a significant enhancement in encryption key management by enabling customers to use their own encryption keys across different Azure Active Directory (AAD) tenants. This update addresses the need for greater control, compliance, and flexibility in multi-tenant environments where organizations manage resources spanning multiple Azure subscriptions and directories.

**Background and Purpose**  
Azure NetApp Files is a high-performance file storage service optimized for enterprise workloads. By default, data at rest in Azure NetApp Files is encrypted using Microsoft-managed keys. However, many organizations require the ability to manage their own encryption keys to meet strict regulatory, compliance, or internal security policies. Previously, customer-managed keys were limited to the same tenant where the Azure NetApp Files resource resided. This limitation posed challenges for enterprises operating across multiple tenants, such as managed service providers or large organizations with segmented IT environments. The introduction of cross-tenant CMK support allows these customers to centralize key management in a single tenant while encrypting volumes in other tenants, enhancing security governance and operational efficiency.

**Specific Features and Detailed Changes**  
- **Cross-tenant Key Vault Integration:** Customers can now configure Azure NetApp Files volumes in one tenant to use CMKs stored in Azure Key Vaults located in a different tenant.  
- **Support for Azure Key Vault Managed HSM and Software Vaults:** Both Azure Key Vault software-protected and hardware security module (HSM)-protected keys can be used across tenants.  
- **Granular Access Control:** The feature requires precise Azure RBAC and Key Vault access policies to authorize the Azure NetApp Files service principal in the key vault tenant, ensuring secure key usage.  
- **Seamless Volume Encryption:** Once configured, volumes are encrypted at rest with the cross-tenant CMK without impacting performance or requiring application changes.

**Technical Mechanisms and Implementation Methods**  
To implement cross-tenant CMK encryption:  
1. **Key Vault Setup:** In the key vault tenant, create or import the encryption key and configure access policies to grant the Azure NetApp Files service principal from the resource tenant the necessary permissions (e.g., wrapKey, unwrapKey).  
2. **Service Principal and RBAC:** The Azure NetApp Files resource tenant must grant the appropriate RBAC roles to the service principal to access the key vault in the other tenant.  
3. **Configuration of Encryption:** When creating or updating an Azure NetApp Files volume, specify the key URI from the cross-tenant key vault. The NetApp Files service then uses this key for volume encryption operations.  
4. **Key Rotation and Management:** Customers maintain full control over key lifecycle, including rotation and revocation, from the key vault tenant, with immediate effect on volume encryption.

**Use Cases and Application Scenarios**  
- **Managed Service Providers (MSPs):** MSPs can centralize key management in their tenant while provisioning Azure NetApp Files volumes encrypted with their keys in customer tenants.  
- **Multi-tenant Enterprises:** Large organizations with multiple subsidiaries or business units operating in separate tenants can enforce uniform encryption policies.  
- **Compliance and Regulatory Requirements:** Organizations subject to strict data sovereignty and encryption mandates can demonstrate key custody separation and control.  
- **Disaster Recovery and Backup:** Cross-tenant CMK enables secure replication scenarios where encrypted data moves across tenants without compromising key control.

**Important Considerations and Limitations**  
- **Complexity in Access Management:** Proper configuration of cross-tenant permissions and RBAC is critical; misconfiguration can lead to key access failures or security risks.  
- **Latency and Performance:** While encryption is transparent to applications, network latency between tenants and key vault regions should be considered for high-throughput workloads.  
- **Key Vault Limits:** Azure Key Vault limits on key operations and throughput apply and should be planned accordingly.  
- **Supported Regions and SKUs:** Verify that both

---

### 4. Retirement: Azure Static Web Apps database connection feature

**Published**: October 03, 2025 16:15:04 UTC
**Link**: [Retirement: Azure Static Web Apps database connection feature](https://azure.microsoft.com/updates?id=500848)

**Update ID**: 500848
**Data source**: Azure Updates API

**Categories**: Compute, Web, Static Web Apps, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of the database connections feature in Azure Static Web Apps, which is currently in public preview.

- Key changes or new features  
The database connections feature will be deprecated and no longer supported effective November 30, 2025, due to changes in the underlying infrastructure. Developers and IT professionals using this feature need to plan for migration or refactoring of their applications to avoid deployment issues.

- Target audience affected  
This update primarily affects developers and IT professionals who use Azure Static Web Apps with the integrated database connections feature for backend data access.

- Important notes if any  
Users should begin refactoring applications that rely on this feature well before the retirement date to ensure smooth deployments and uninterrupted service. Alternative database connection methods or architectures should be considered as part of the migration strategy. Further details and guidance can be found in the official Azure update link.

**Details**:

The Azure update announces the planned retirement of the database connections feature in Azure Static Web Apps, currently in public preview, effective November 30, 2025, due to changes in the underlying infrastructure. This feature allowed developers to simplify backend integration by directly connecting Static Web Apps to databases without managing separate API layers. With its deprecation, users must refactor applications to use alternative methods for database connectivity to ensure continued functionality and deployment stability.

**Background and Purpose of the Update**  
Azure Static Web Apps is a service designed to streamline the deployment of full-stack web applications by hosting static frontends alongside serverless APIs. The database connections feature was introduced in public preview to enable developers to connect their static apps directly to databases, reducing the need for custom backend code or API management. However, changes in the underlying Azure infrastructure and platform architecture have made maintaining this feature unsustainable. The retirement aims to align the service with the evolving Azure ecosystem and encourage adoption of more robust, scalable, and maintainable database integration patterns.

**Specific Features and Detailed Changes**  
The deprecated feature provided a simplified declarative configuration to connect Static Web Apps directly to supported databases, such as Azure SQL Database or Cosmos DB, enabling seamless data access within the app’s API routes. Post-November 30, 2025, this direct database connection capability will no longer be supported. Developers currently using this feature must transition to alternative approaches, such as implementing dedicated API services or leveraging Azure Functions to handle database interactions explicitly.

**Technical Mechanisms and Implementation Methods**  
Originally, the feature abstracted database connectivity by managing connection strings and authentication within the Static Web Apps environment, automatically injecting these into serverless API functions. With the retirement, developers will need to manually configure database connections within their backend code, typically hosted as Azure Functions or other API services. This involves securely managing connection strings via Azure Key Vault or Static Web Apps secrets, implementing connection pooling, error handling, and query logic explicitly in the API layer. This shift returns control and responsibility for database interactions to the developer, enabling more customized and optimized implementations.

**Use Cases and Application Scenarios**  
The database connections feature was particularly useful for rapid prototyping, small to medium applications, and scenarios where minimal backend complexity was desired. Typical use cases included content-driven websites, dashboards, and simple CRUD applications where direct database access simplified development. Post-deprecation, these scenarios will require developers to architect explicit API layers, which, while adding complexity, also provide greater flexibility, security, and scalability for production-grade applications.

**Important Considerations and Limitations**  
- Migration Planning: Developers must audit existing Static Web Apps using this feature and plan refactoring well before the November 2025 deadline to avoid deployment failures.  
- Security: Direct database connections managed by the platform will no longer be available, so secure handling of credentials and access control becomes the developer’s responsibility.  
- Performance and Scalability: Custom API implementations allow for better optimization but require careful design to maintain performance.  
- Compatibility: Some legacy applications tightly coupled to the deprecated feature may require significant rework.  
- Preview Status: As the feature was in public preview, it was not recommended for production workloads, and this update reinforces the need for production-ready alternatives.

**Integration with Related Azure Services**  
Post-retirement, developers are encouraged to leverage Azure Functions or Azure App Service to host backend APIs that interact with databases. Azure Key Vault should be used for secure secret management. Additionally, Azure API Management can be integrated for advanced API governance. For database services, Azure SQL Database, Cosmos DB, and other Azure data platforms remain fully supported but require explicit connection management. This update aligns Static Web Apps with broader Azure best practices, promoting modular, secure, and scalable application architectures.

In summary, the retirement of the Azure Static Web Apps database connections feature by November 30, 2025, necessitates that developers refactor their applications to implement explicit backend API layers for database interactions, enhancing control, security, and

---

### 5. Public Preview:  Azure NetApp Files Support for OpenLDAP, FreeIPA, and Red Hat Directory Server LDAP services    

**Published**: October 03, 2025 16:01:01 UTC
**Link**: [Public Preview:  Azure NetApp Files Support for OpenLDAP, FreeIPA, and Red Hat Directory Server LDAP services    ](https://azure.microsoft.com/updates?id=508748)

**Update ID**: 508748
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files now supports integration with FreeIPA, OpenLDAP, and Red Hat Directory Server LDAP services, available in public preview.

- Key changes or new features  
This update enables secure LDAP over TLS authentication for NFSv3 and NFSv4.1 volumes, allowing enterprises to leverage these popular LDAP directory services for identity management and access control. It expands Azure NetApp Files’ compatibility beyond Active Directory, enhancing flexibility in heterogeneous environments.

- Target audience affected  
Developers and IT professionals managing Azure NetApp Files deployments who require LDAP-based authentication for NFS workloads, especially those using FreeIPA, OpenLDAP, or Red Hat Directory Server. This is particularly relevant for organizations with non-AD directory infrastructures.

- Important notes if any  
Since this feature is in public preview, it should be used with caution in production environments. Users should review documentation for configuration details and TLS requirements to ensure secure LDAP connectivity. Feedback during the preview phase is encouraged to improve the service.

**Details**:

The recent Azure NetApp Files public preview introduces support for integrating with FreeIPA, OpenLDAP, and Red Hat Directory Server LDAP services, enabling secure LDAP over TLS authentication for NFSv3 and NFSv4.1 volumes. This update addresses the need for enterprises to leverage widely adopted open-source and commercial LDAP directory services to manage identity and access control for file shares hosted on Azure NetApp Files, enhancing security and interoperability in hybrid and cloud-native environments.

**Background and Purpose**  
Azure NetApp Files is a high-performance, enterprise-grade file storage service that supports multiple protocols including NFS and SMB. Traditionally, Azure NetApp Files supported Active Directory (AD) for identity management and access control. However, many organizations use alternative LDAP directory services such as FreeIPA, OpenLDAP, or Red Hat Directory Server to manage users and groups, especially in Linux-centric or heterogeneous environments. The purpose of this update is to extend Azure NetApp Files’ authentication capabilities beyond AD by enabling integration with these LDAP services, thereby broadening customer choice and simplifying migration or hybrid deployments.

**Specific Features and Detailed Changes**  
- Support for FreeIPA, OpenLDAP, and Red Hat Directory Server as LDAP identity providers is now available in public preview.  
- Secure LDAP (LDAPS) over TLS is supported, ensuring encrypted authentication traffic between Azure NetApp Files and the LDAP servers.  
- This LDAP integration applies to both NFSv3 and NFSv4.1 protocol volumes, enabling consistent identity-based access control across these widely used file protocols.  
- The feature allows enterprises to map LDAP users and groups to file share permissions, facilitating granular access control without relying solely on Active Directory.  
- Configuration options include specifying LDAP server endpoints, binding methods, base distinguished names (DNs), and TLS certificate validation parameters.

**Technical Mechanisms and Implementation Methods**  
Azure NetApp Files acts as an LDAP client that authenticates user access requests against the configured LDAP directory service. When a client attempts to access an NFS volume, Azure NetApp Files queries the LDAP server over a secure LDAPS connection to validate user credentials and retrieve group membership information. This information is then used to enforce POSIX-style permissions on the file system. The integration requires administrators to provide LDAP server details, including hostnames, ports (typically 636 for LDAPS), and service account credentials for binding. TLS certificates must be trusted by Azure NetApp Files to establish secure connections. The service supports standard LDAP schema attributes for user and group identification, allowing compatibility with common LDAP deployments.

**Use Cases and Application Scenarios**  
- Enterprises with existing FreeIPA or OpenLDAP infrastructures can now extend their identity management to Azure NetApp Files without deploying additional AD services.  
- Organizations migrating Linux workloads to Azure that rely on non-AD LDAP directories can maintain consistent access control policies.  
- Hybrid environments where on-premises LDAP servers are used alongside cloud storage can leverage this integration for seamless authentication.  
- DevOps teams managing containerized or Linux-based applications requiring NFS storage with LDAP-based access control benefit from simplified identity management.  

**Important Considerations and Limitations**  
- This feature is currently in public preview; production use should be approached with caution and thorough testing.  
- Only LDAP over TLS (LDAPS) is supported to ensure secure authentication; unsecured LDAP is not supported.  
- The integration supports NFSv3 and NFSv4.1 protocols but does not extend to SMB protocol volumes, which continue to rely on Active Directory.  
- Proper network connectivity and firewall rules must be configured to allow Azure NetApp Files to communicate with the LDAP servers on the required ports.  
- Administrators must ensure LDAP schema compatibility and correct attribute mappings for user and group resolution.  
- High availability and failover configurations for LDAP servers should be planned to avoid authentication disruptions.

**Integration with Related Azure Services**  
- This LDAP integration complements Azure NetApp Files’ existing Active Directory support, enabling hybrid identity strategies.

---

### 6. Retirement: Azure VPN Gateway support for SSTP Protocol will be retired on March 31, 2027

**Published**: October 03, 2025 16:01:01 UTC
**Link**: [Retirement: Azure VPN Gateway support for SSTP Protocol will be retired on March 31, 2027](https://azure.microsoft.com/updates?id=499923)

**Update ID**: 499923
**Data source**: Azure Updates API

**Categories**: Networking, Security, VPN Gateway, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure VPN Gateway support for the SSTP (Secure Socket Tunneling Protocol) protocol, effective March 31, 2027.

- Key changes or new features  
SSTP support will be phased out due to its limited scalability and suboptimal performance. Azure recommends migrating VPN connections to IKEv2 or OpenVPN protocols, which provide significantly improved capabilities, including support for up to 10,000 concurrent connections and better overall performance and reliability.

- Target audience affected  
Developers and IT professionals managing Azure VPN Gateway configurations and VPN client connectivity using SSTP will be impacted. Organizations currently relying on SSTP for VPN access need to plan and execute migration strategies to supported protocols before the retirement date.

- Important notes if any  
The retirement date is March 31, 2027, providing a transition period for customers. Migrating to IKEv2 or OpenVPN not only ensures continued support but also benefits from enhanced scalability and security features. It is advisable to start testing and implementing these protocols well in advance to avoid service disruptions.  

Reference: https://azure.microsoft.com/updates?id=499923

**Details**:

The Azure update announces the planned retirement of Azure VPN Gateway support for the Secure Socket Tunneling Protocol (SSTP) on March 31, 2027. This deprecation is driven by SSTP’s inherent limitations in scalability and performance, prompting Microsoft to encourage users to migrate to more robust VPN protocols such as IKEv2 and OpenVPN.

**Background and Purpose:**  
SSTP has historically been used for VPN connections due to its ability to traverse firewalls by encapsulating traffic over HTTPS (TCP port 443). However, SSTP’s architecture limits its scalability and throughput, making it less suitable for modern enterprise environments requiring high connection counts and performance. To align with evolving network demands and enhance VPN gateway efficiency, Microsoft is retiring SSTP support and steering customers toward protocols that better support large-scale, high-performance VPN deployments.

**Specific Features and Detailed Changes:**  
Post-retirement, Azure VPN Gateway will no longer accept SSTP-based VPN connections. Instead, users should adopt IKEv2 or OpenVPN protocols, which Azure VPN Gateway supports natively. These protocols provide advanced features such as:  
- Support for up to 10,000 concurrent VPN connections per gateway, significantly surpassing SSTP’s capabilities.  
- Improved connection stability and throughput due to UDP-based tunneling (OpenVPN can operate over UDP or TCP, IKEv2 uses UDP).  
- Enhanced security features, including stronger encryption algorithms and better resistance to network interruptions.  

**Technical Mechanisms and Implementation Methods:**  
IKEv2 (Internet Key Exchange version 2) is a widely adopted VPN protocol that establishes and maintains secure VPN tunnels using IPsec for encryption. It supports rapid reconnection and mobility, making it suitable for mobile clients. OpenVPN is an open-source VPN protocol that uses SSL/TLS for key exchange and can operate over UDP or TCP, providing flexibility in firewall traversal and network environments. Both protocols leverage modern cryptographic standards and support multi-factor authentication integration.

To implement the transition:  
- Configure Azure VPN Gateway with IKEv2 or OpenVPN client configurations.  
- Update client VPN software to support these protocols. Azure provides configuration files and documentation for both.  
- Test connectivity and performance before decommissioning SSTP connections.  

**Use Cases and Application Scenarios:**  
This update impacts organizations using Azure VPN Gateway for remote access or site-to-site VPNs relying on SSTP. Typical scenarios include:  
- Enterprises providing remote worker access via SSTP VPN clients.  
- Hybrid cloud architectures connecting on-premises networks with Azure VNets using SSTP tunnels.  
- Scenarios requiring high availability and scalability of VPN connections, which SSTP cannot efficiently support.  

Transitioning to IKEv2 or OpenVPN enables these use cases to scale securely and reliably, supporting larger user bases and more demanding workloads.

**Important Considerations and Limitations:**  
- Migration planning is critical to avoid service disruption; SSTP connections will cease functioning after March 31, 2027.  
- Client compatibility must be verified; some legacy clients may not support IKEv2 or OpenVPN without updates.  
- Firewall and network configurations may require adjustments to allow UDP traffic (commonly UDP ports 500 and 4500 for IKEv2, and UDP/TCP ports for OpenVPN).  
- Monitoring and logging configurations should be updated to reflect the new protocols for effective troubleshooting and compliance.  

**Integration with Related Azure Services:**  
Azure VPN Gateway integrates with Azure Active Directory and Azure Multi-Factor Authentication (MFA) for enhanced security, both of which support IKEv2 and OpenVPN protocols. Additionally, Azure Monitor and Network Watcher can be used to track VPN gateway health and performance post-migration. Organizations leveraging Azure Firewall or Azure Security Center should update their policies to accommodate the new VPN protocols and traffic patterns.

In summary, the retirement of SSTP support in Azure VPN Gateway reflects a strategic move to improve VPN scalability, performance,

---

### 7. Retirement: General Purpose v1 (GPv1) and legacy blob storage accounts  

**Published**: October 03, 2025 14:15:21 UTC
**Link**: [Retirement: General Purpose v1 (GPv1) and legacy blob storage accounts  ](https://azure.microsoft.com/updates?id=496964)

**Update ID**: 496964
**Data source**: Azure Updates API

**Categories**: Storage, Storage Accounts, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of all General Purpose v1 (GPv1) storage accounts, including legacy blob storage accounts, as part of streamlining the Azure Storage portfolio.

- Key changes or new features  
GPv1 accounts will no longer be supported or available for creation. Customers are encouraged to migrate to General Purpose v2 (GPv2) or Blob Storage accounts, which offer improved performance, scalability, and cost efficiency. The update emphasizes enhanced features such as tiering, lifecycle management, and advanced security options available in newer storage account types.

- Target audience affected  
Developers and IT professionals managing Azure Storage accounts, especially those using GPv1 or legacy blob storage accounts, are directly impacted. Organizations with existing GPv1 accounts must plan migrations to avoid service disruptions.

- Important notes if any  
Microsoft recommends assessing current storage usage and initiating migration to GPv2 or Blob Storage accounts promptly. Legacy GPv1 accounts will eventually be disabled, so proactive transition is critical. Review Azure Storage pricing and feature differences to optimize cost and performance during migration. Detailed migration guidance and tools are available in Azure documentation.

**Details**:

The Azure update announces the retirement of all General Purpose v1 (GPv1) storage accounts, including legacy blob storage accounts, as part of Microsoft’s initiative to optimize the Azure Storage portfolio by enhancing performance, scalability, and cost efficiency.

**Background and Purpose:**  
GPv1 storage accounts were the original generation of Azure Storage accounts offering a mix of standard performance and pricing options. Over time, Azure introduced General Purpose v2 (GPv2) accounts and other specialized storage tiers that provide better performance, more features, and improved cost models. The retirement of GPv1 aims to simplify the storage offerings, encourage migration to more modern storage accounts, and enable customers to benefit from newer capabilities such as tiering, advanced security, and enhanced scalability.

**Specific Features and Detailed Changes:**  
- **Retirement Scope:** All GPv1 storage accounts and legacy blob storage accounts will be retired, meaning they will no longer be supported or available for new deployments after the retirement date.  
- **Migration Path:** Customers are encouraged to migrate to GPv2 accounts, which support all the features of GPv1 plus additional benefits such as access tiers (hot, cool, archive), improved performance, and better cost efficiency.  
- **Feature Differences:** GPv2 supports Azure Blob Storage features like lifecycle management, soft delete, blob versioning, and advanced security features (e.g., Azure AD integration, customer-managed keys) that GPv1 does not.  
- **Cost and Performance:** GPv2 accounts offer more granular pricing options and better throughput and scalability, making them suitable for a wider range of workloads.

**Technical Mechanisms and Implementation Methods:**  
- **Migration Process:** Microsoft provides tools and guidance for migrating data from GPv1 to GPv2 accounts. This typically involves creating a new GPv2 account and copying data using Azure Storage tools such as AzCopy, Azure Data Factory, or Azure Storage Explorer.  
- **Compatibility:** GPv2 accounts maintain backward compatibility with GPv1 APIs, minimizing application changes. However, customers should validate their applications against GPv2 to leverage new features and ensure compatibility.  
- **Automation:** Scripts and Azure CLI commands can automate the migration process, including data replication and validation.  
- **Monitoring:** Azure Monitor and Storage Analytics can be used to track migration progress and performance metrics.

**Use Cases and Application Scenarios:**  
- **Legacy Applications:** Applications currently using GPv1 accounts should plan migration to avoid service disruption and to take advantage of enhanced features.  
- **New Deployments:** New storage deployments should use GPv2 accounts exclusively for better performance and cost management.  
- **Data Archiving and Tiering:** GPv2 supports tiering, enabling cost-effective storage of infrequently accessed data, which is critical for big data, backup, and archival scenarios.  
- **Security-Sensitive Workloads:** Enhanced security features in GPv2 accounts benefit compliance-heavy industries.

**Important Considerations and Limitations:**  
- **Migration Timing:** Customers must plan migration before the retirement date to avoid service interruptions.  
- **Data Transfer Costs:** Data egress and transfer costs may apply during migration.  
- **Feature Parity:** While GPv2 supports all GPv1 features, some legacy behaviors may differ; thorough testing is recommended.  
- **Service Impact:** During migration, ensure minimal downtime by using asynchronous data copy methods and validating data integrity.  
- **Automation Complexity:** Large-scale migrations may require orchestration and monitoring to handle volume and consistency.

**Integration with Related Azure Services:**  
- **Azure Backup and Site Recovery:** These services integrate seamlessly with GPv2 accounts, enabling better backup and disaster recovery options.  
- **Azure Security Center:** Enhanced security monitoring and threat detection are available for GPv2 accounts.  
- **Azure Data Factory:** Facilitates data movement and transformation during migration.  
- **Azure Monitor and Log Analytics:** Provide insights into storage performance and migration status

---


*This report was automatically generated - 2025-10-04 03:03:16 UTC*