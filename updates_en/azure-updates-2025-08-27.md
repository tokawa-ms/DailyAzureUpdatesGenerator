# August 27, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 27, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Generally Available: Entra ID and RBAC support for GetAccountInfo and other supplemental APIs for Azure Storage

**Published**: August 26, 2025 17:45:29 UTC
**Link**: [Generally Available: Entra ID and RBAC support for GetAccountInfo and other supplemental APIs for Azure Storage](https://azure.microsoft.com/updates?id=496287)

**Update ID**: 496287
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage, Security

**Summary**:

- What was updated  
Azure Storage now generally supports Entra ID and Role-Based Access Control (RBAC) for several supplemental APIs, including GetAccountInfo, Get/Set Container ACL, Get/Set Queue ACL, and Get/Set Table ACL.

- Key changes or new features  
These APIs, previously limited in authentication options, can now leverage Entra ID identities and RBAC permissions to enforce fine-grained access control. This enhancement aligns with Azure security best practices by enabling centralized identity management and least-privilege access for storage resource operations.

- Target audience affected  
Developers and IT professionals managing Azure Storage security and access control will benefit from this update. Those integrating storage APIs into applications or automating storage management can now use Entra ID and RBAC for improved security and compliance.

- Important notes if any  
Organizations should review and update their access policies to utilize Entra ID and RBAC for these APIs, replacing legacy authentication methods where applicable. This change enhances security posture but may require permission adjustments to ensure uninterrupted access. For detailed implementation guidance, refer to the official Azure documentation linked in the update.

**Details**:

The recent general availability of Entra ID and Role-Based Access Control (RBAC) support for supplemental Azure Storage APIs—including GetAccountInfo, Get/Set Container ACL, Get/Set Queue ACL, and Get/Set Table ACL—represents a significant enhancement in securing and managing access to Azure Storage resources. This update aligns Azure Storage with modern identity and access management best practices by integrating Azure Active Directory (now Entra ID) authentication and fine-grained RBAC authorization into these previously limited APIs.

**Background and Purpose**  
Historically, many Azure Storage management operations, especially those involving Access Control Lists (ACLs) on containers, queues, and tables, relied on shared keys or SAS tokens for authentication and authorization. While functional, these methods pose security risks such as key leakage and lack of granular permission control. To improve security posture and operational governance, Microsoft has extended Entra ID and RBAC support to supplemental APIs like GetAccountInfo and ACL management operations, enabling centralized identity management, least privilege access, and auditability.

**Specific Features and Detailed Changes**  
- **Entra ID Authentication:** These APIs now accept OAuth 2.0 bearer tokens issued by Entra ID, enabling authentication via service principals, managed identities, or user accounts.  
- **RBAC Authorization:** Access to these APIs is governed by Azure RBAC roles assigned at the subscription, resource group, or storage account level. This replaces or supplements previous key-based access, allowing fine-grained permission assignments such as Storage Blob Data Contributor or Storage Queue Data Contributor roles.  
- **APIs Covered:**  
  - `GetAccountInfo`: Retrieves properties about the storage account.  
  - `GetContainerACL` / `SetContainerACL`: Manage access control lists on blob containers.  
  - `GetQueueACL` / `SetQueueACL`: Manage ACLs on storage queues.  
  - `GetTableACL` / `SetTableACL`: Manage ACLs on storage tables.  
- **Backward Compatibility:** Existing key and SAS token authentication methods remain supported, ensuring smooth migration.

**Technical Mechanisms and Implementation Methods**  
Under the hood, when a client calls these supplemental APIs with an OAuth token, Azure Storage validates the token signature and checks the token’s claims against assigned RBAC roles. The RBAC engine evaluates whether the caller has the required permissions to perform the requested operation. This process leverages Azure’s centralized identity platform, allowing consistent enforcement of access policies. The APIs themselves have been updated to accept Authorization headers with bearer tokens and respond with appropriate HTTP status codes (e.g., 403 Forbidden if unauthorized).

**Use Cases and Application Scenarios**  
- **Enterprise Security Compliance:** Organizations requiring strict identity governance can now eliminate shared keys for ACL management, reducing risk.  
- **Automation and DevOps:** Scripts and automation tools using service principals or managed identities can securely manage ACLs without embedding secrets.  
- **Multi-tenant SaaS Applications:** SaaS providers can assign scoped RBAC roles to tenant-specific identities, enabling secure delegation of ACL management.  
- **Auditing and Monitoring:** Integration with Azure Monitor and Azure AD logs enables tracking of who accessed or modified ACLs.

**Important Considerations and Limitations**  
- **Role Assignments Required:** To use Entra ID authentication for these APIs, appropriate RBAC roles must be assigned in advance; otherwise, calls will fail authorization.  
- **Partial API Coverage:** This update covers supplemental APIs related to ACLs and account info but does not extend to all storage operations; key and SAS remain relevant for other scenarios.  
- **Latency and Throttling:** Token validation and RBAC checks add minimal latency but should be considered in high-throughput scenarios.  
- **Migration Planning:** Existing applications using shared keys or SAS tokens for these APIs should plan for gradual migration to Entra ID authentication to leverage enhanced security.

**Integration with Related Azure Services**  
- **Azure Active Directory (Entra ID):**

---

### 2. Public Preview: Custom block response code and body for Application Gateway WAF 

**Published**: August 26, 2025 17:00:18 UTC
**Link**: [Public Preview: Custom block response code and body for Application Gateway WAF ](https://azure.microsoft.com/updates?id=501323)

**Update ID**: 501323
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Web Application Firewall, Features

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) now supports customizable HTTP response status codes and response bodies for blocked requests, currently in public preview.

- Key changes or new features  
Developers and IT professionals can configure custom block responses instead of the default 403 Forbidden status and generic message. This allows tailoring the response code and content to better align with application requirements, improve user experience, or integrate with monitoring and automation workflows.

- Target audience affected  
This update primarily benefits developers managing web applications behind Azure Application Gateway WAF and IT security teams responsible for configuring and maintaining WAF policies.

- Important notes if any  
The feature is in public preview, so it should be used with caution in production environments. Users need to explicitly enable and configure custom block responses via WAF policy settings. This enhancement improves flexibility in handling blocked traffic but does not change the underlying blocking logic or security posture of the WAF.  

For more details and configuration guidance, refer to the official Azure update: https://azure.microsoft.com/updates?id=501323

**Details**:

The recent public preview announcement for Azure Application Gateway Web Application Firewall (WAF) introduces the capability to customize the HTTP response status code and response body returned when a request is blocked by the WAF. This enhancement addresses a key operational need for organizations to tailor security responses to align with their application behavior, user experience, and compliance requirements.

**Background and Purpose**  
Azure Application Gateway WAF protects web applications from common threats and vulnerabilities by inspecting incoming HTTP/HTTPS traffic and blocking malicious requests based on OWASP core rule sets and custom rules. Previously, when the WAF blocked a request, it returned a fixed HTTP 403 Forbidden status code with a generic response body. While effective for security, this default behavior limited flexibility in how applications handle blocked requests, potentially impacting user experience or integration with custom monitoring and logging systems. The update aims to provide IT professionals and developers with greater control over the WAF’s blocking responses, enabling them to customize both the HTTP status code and the response body content.

**Specific Features and Detailed Changes**  
- **Custom Block Response Code**: Users can now specify any valid HTTP status code to be returned when a request is blocked by the WAF. This allows differentiation between types of blocks or integration with client-side logic that reacts differently to various status codes.  
- **Custom Response Body**: Alongside the status code, users can define a custom response body, which can be plain text, HTML, or JSON. This enables organizations to provide more informative messages to end-users or to conform to specific API response formats.  
- **Configuration Scope**: These customizations are configured at the WAF policy level associated with the Application Gateway, allowing granular control per application or environment.

**Technical Mechanisms and Implementation Methods**  
The customization is implemented through the Azure portal, Azure CLI, or ARM templates by modifying the WAF policy’s custom block response settings. When a request triggers a WAF rule and is blocked, the Application Gateway intercepts the response generation process and substitutes the default 403 status code and body with the user-defined values. This substitution occurs before the response is sent back to the client, ensuring seamless integration with existing traffic flow. The feature supports both Prevention mode (blocking) and Detection mode (logging only) configurations, but the custom response applies only when blocking is active.

**Use Cases and Application Scenarios**  
- **Improved User Experience**: Applications can return user-friendly error pages or localized messages instead of generic 403 errors, reducing confusion and support tickets.  
- **API Gateways**: For APIs protected by Application Gateway WAF, customized JSON error responses can be returned, enabling client applications to handle errors programmatically.  
- **Compliance and Branding**: Organizations can embed compliance notices or branding elements in the response body to maintain consistent messaging.  
- **Differentiated Blocking Responses**: By using different status codes, security teams can signal various block reasons or severity levels to downstream systems or monitoring tools.

**Important Considerations and Limitations**  
- The feature is currently in public preview, so it should be used with caution in production environments until GA (General Availability) is announced.  
- Custom response bodies should be carefully crafted to avoid leaking sensitive information about the WAF rules or internal infrastructure.  
- The maximum size and content type of the custom response body may be subject to Azure Application Gateway limits; users should refer to official documentation for constraints.  
- This customization does not affect the underlying blocking logic or detection capabilities of the WAF; it only changes the response sent to clients.  
- Integration with other Application Gateway features such as URL-based routing or SSL termination remains unaffected.

**Integration with Related Azure Services**  
- **Azure Monitor and Log Analytics**: Custom block responses can be correlated with WAF logs and metrics to provide richer context in security monitoring dashboards.  
- **Azure Policy**: Organizations can enforce the use of custom block responses across subscriptions or resource groups by defining policies that require

---

### 3. Generally Available: CNI Overlay for Application Gateway for Containers and AGIC

**Published**: August 26, 2025 16:00:15 UTC
**Link**: [Generally Available: CNI Overlay for Application Gateway for Containers and AGIC](https://azure.microsoft.com/updates?id=500991)

**Update ID**: 500991
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Services, Features

**Summary**:

- What was updated  
Azure CNI Overlay support for Application Gateway for Containers (AGIC) is now generally available.

- Key changes or new features  
The Azure CNI Overlay allows AKS clusters to assign pod IPs from a separate CIDR block distinct from the VNet IP space. This conserves IP address space within the VNet and simplifies networking for multi-cluster deployments. When combined with AGIC, it enables seamless ingress traffic management using Application Gateway while maintaining efficient IP utilization and network isolation.

- Target audience affected  
Developers and IT professionals managing AKS clusters with Application Gateway ingress, especially those dealing with IP address constraints or multi-cluster networking scenarios.

- Important notes if any  
This GA release ensures production-ready stability and support. Users should plan network CIDR allocations accordingly to leverage the overlay benefits. Integration with AGIC requires configuration updates to support the overlay networking model. This feature helps optimize IP usage and simplifies complex cluster networking architectures.  

For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=500991

**Details**:

The Azure update announcing the general availability of the CNI Overlay for Application Gateway for Containers (AGIC) introduces a significant enhancement to networking in Azure Kubernetes Service (AKS) environments, particularly for scenarios involving Application Gateway as an ingress controller.

**Background and Purpose**  
Traditionally, AKS clusters using Azure CNI allocate pod IP addresses directly from the cluster’s virtual network (VNet) subnet, which can rapidly consume IP address space in large or multi-cluster deployments. This limitation complicates network management and scaling, especially when integrating with Application Gateway for Containers (AGIC), which requires stable and scalable ingress networking. The CNI Overlay addresses these challenges by decoupling pod IP allocation from the VNet subnet, enabling more efficient IP space utilization and simplified multi-cluster networking.

**Specific Features and Detailed Changes**  
The key feature of this update is the introduction of an overlay network for Azure CNI that allows pods to receive IP addresses from a dedicated CIDR block separate from the VNet subnet. This overlay network is implemented on top of the existing Azure CNI, preserving native network performance and compatibility with Azure networking features. When combined with AGIC, this overlay enables Application Gateway to route traffic to pods using these overlay IPs seamlessly, without requiring additional complex routing or NAT configurations.

**Technical Mechanisms and Implementation Methods**  
The CNI Overlay leverages encapsulation techniques to route pod traffic from the overlay CIDR to the underlying VNet. Essentially, pods are assigned IPs from the overlay CIDR, and their traffic is encapsulated and tunneled through the VNet to reach other resources or ingress points. This encapsulation is transparent to the pods and the Application Gateway, which continues to operate using standard IP routing semantics. Deployment involves configuring the AKS cluster to enable the overlay mode during cluster creation or upgrade, specifying the overlay CIDR range, and integrating AGIC to recognize and route traffic to overlay IPs.

**Use Cases and Application Scenarios**  
This update is particularly beneficial for organizations managing multiple AKS clusters within a single VNet or across VNets with peering, where IP address conservation is critical. It simplifies multi-cluster ingress architectures by allowing AGIC to manage traffic across clusters without IP conflicts or complex network topologies. Additionally, it supports large-scale AKS deployments where the native Azure CNI IP allocation would otherwise exhaust subnet capacity. Use cases include microservices architectures requiring scalable ingress, hybrid cloud scenarios with interconnected clusters, and environments demanding strict IP management and security segmentation.

**Important Considerations and Limitations**  
While the overlay network provides IP space efficiency, it introduces an additional encapsulation layer, which may have minor performance implications compared to native Azure CNI pod IPs. Network troubleshooting may require familiarity with overlay networking concepts and tools. Also, existing network policies and security groups must be reviewed to ensure compatibility with overlay IP ranges. The feature requires AKS clusters to be on supported Kubernetes versions and may necessitate cluster upgrades or reconfiguration. It is essential to plan the overlay CIDR carefully to avoid overlaps with existing network ranges.

**Integration with Related Azure Services**  
The CNI Overlay integrates tightly with Application Gateway for Containers (AGIC), enabling seamless ingress traffic management using overlay pod IPs. It also works in conjunction with Azure Virtual Network, Azure Network Policies, and Azure Monitor for comprehensive network management and observability. This update complements Azure Arc-enabled Kubernetes by facilitating consistent networking across hybrid and multi-cloud clusters. Additionally, it supports Azure Policy enforcement for network configurations and can be combined with Azure Firewall or Network Virtual Appliances for enhanced security.

In summary, the general availability of Azure CNI Overlay for Application Gateway for Containers and AGIC provides a robust solution to optimize IP address utilization and simplify ingress networking in AKS, enabling scalable, multi-cluster deployments with efficient and manageable network architectures.

---

### 4. Public Preview: Azure NetApp Files short-term clones 

**Published**: August 26, 2025 16:00:15 UTC
**Link**: [Public Preview: Azure NetApp Files short-term clones ](https://azure.microsoft.com/updates?id=500914)

**Update ID**: 500914
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure NetApp Files, Features, Services, SDK and Tools

**Summary**:

- What was updated  
Azure NetApp Files now offers short-term clones in public preview.

- Key changes or new features  
Short-term clones provide instant, space-efficient read/write access by creating temporary thin clones from existing volume snapshots. This eliminates the need for full data duplication, significantly reducing storage consumption and accelerating data provisioning. Clones are ideal for scenarios requiring rapid, temporary data copies such as software development, testing, and data analytics workflows.

- Target audience affected  
Developers, DevOps engineers, and IT professionals managing storage and application environments that require fast, ephemeral data copies will benefit from this feature. It is particularly useful for teams needing quick environment spin-ups without incurring high storage costs.

- Important notes if any  
This feature is currently in public preview, so users should evaluate it in non-production environments and provide feedback. Integration with existing Azure NetApp Files snapshots is required, and there may be limitations on clone lifespan or performance during preview. Check the official documentation for detailed usage guidelines and regional availability.

**Details**:

The recent public preview of Azure NetApp Files short-term clones introduces a significant enhancement aimed at optimizing storage efficiency and accelerating data access workflows by enabling the creation of temporary, space-efficient writable clones derived from existing volume snapshots. This feature addresses the common challenge of provisioning full data copies for development, testing, or data analysis scenarios, which traditionally consume substantial storage capacity and time.

**Background and Purpose**  
Azure NetApp Files (ANF) is a high-performance, enterprise-grade file storage service designed for demanding workloads requiring low latency and high throughput. Prior to this update, creating writable clones typically involved full volume copies or long-term clones, which consume considerable storage and take time to provision. The short-term clones feature was introduced to provide instant, space-efficient writable copies that leverage snapshot technology, thereby reducing storage overhead and accelerating deployment cycles for ephemeral workloads.

**Specific Features and Detailed Changes**  
- **Instantaneous Writable Clones**: Short-term clones can be created instantly from existing snapshots without duplicating the entire data set.  
- **Space Efficiency**: These clones are thin-provisioned, meaning they only consume additional storage as changes are made, significantly reducing capacity usage compared to full clones.  
- **Temporary Lifecycle**: Designed for transient use cases, these clones have a limited lifespan and are automatically deleted after a configurable retention period, helping manage storage costs and resource cleanup.  
- **Read/Write Access**: Unlike snapshot copies which are read-only, these clones support full read/write access, enabling realistic testing and development scenarios.

**Technical Mechanisms and Implementation Methods**  
Short-term clones utilize the underlying snapshot technology of Azure NetApp Files. When a clone is created, it references the snapshot metadata, sharing the same physical storage blocks initially. As changes occur on the clone, copy-on-write mechanisms allocate new storage blocks for modified data, preserving the original snapshot state. This approach minimizes storage consumption and accelerates clone creation. The lifecycle management is integrated into the ANF control plane, allowing users to specify retention periods and automate cleanup. The clones are managed via Azure CLI, REST API, and Azure Portal, providing flexibility in automation and integration.

**Use Cases and Application Scenarios**  
- **Software Development and Testing**: Developers can spin up isolated writable environments quickly without incurring the cost of full data duplication.  
- **Data Analytics and Machine Learning**: Analysts can create temporary data copies for experimentation without impacting production data or storage budgets.  
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated pipelines can provision ephemeral environments for testing new builds against realistic datasets.  
- **Disaster Recovery Drills**: Short-term clones enable rapid environment setup for failover testing without long-term storage commitments.

**Important Considerations and Limitations**  
- **Retention Period**: Clones are temporary and subject to retention policies; users must plan for data persistence accordingly.  
- **Performance Impact**: While clones provide near-instant access, heavy write workloads may incur some performance overhead due to copy-on-write operations.  
- **Snapshot Dependency**: Clones depend on the underlying snapshot; deleting the snapshot invalidates the clone.  
- **Preview Status**: As a public preview feature, it may have limited regional availability and is subject to change; production use should be carefully evaluated.

**Integration with Related Azure Services**  
Short-term clones integrate seamlessly with Azure NetApp Files’ existing ecosystem and management tools, including Azure Portal, Azure CLI, and REST APIs, facilitating automation and orchestration. They complement Azure DevOps pipelines by enabling rapid environment provisioning. Additionally, these clones can be used alongside Azure Kubernetes Service (AKS) for stateful application testing, and with Azure Monitor for performance and usage tracking. Integration with Azure Policy can help enforce governance on clone creation and retention.

In summary, Azure NetApp Files short-term clones provide IT professionals with a powerful tool to create instant, writable, and space-efficient data copies from snapshots, optimizing storage utilization and accelerating workflows in

---


*This report was automatically generated - 2025-08-27 03:02:18 UTC*