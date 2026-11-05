# November 05, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 05, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01

**Published**: November 04, 2026 18:42:12 UTC
**Link**: [Generally Available: Azure Database for PostgreSQL stable REST API version 2026-10-01](https://azure.microsoft.com/updates?id=579300)

**Update ID**: 579300
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

- What was updated  
The Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 is now generally available.

- Key changes or new features  
This stable API release introduces several enhancements:
  - Expanded maintenance management capabilities, allowing more granular control over server maintenance operations.
  - Support for immutable backups, improving data protection and compliance by preventing backup modification or deletion.
  - Multi-tenant encryption, enabling cross-tenant customer-managed keys for enhanced security in multi-tenant environments.

- Target audience affected  
Developers and IT professionals who manage or integrate with Azure Database for PostgreSQL Flexible Server, especially those automating operations via the REST API or requiring advanced security and compliance features.

- Important notes  
The new API version is recommended for all new integrations and automation workflows. Existing users should review documentation for migration guidance and to leverage new features. The expanded maintenance and backup capabilities can help organizations meet stricter regulatory requirements and improve operational resilience.

Data source: Using API data  
For more details, visit the official Azure Update: https://azure.microsoft.com/updates?id=579300

**Details**:

**Comprehensive Technical Explanation: Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 (General Availability)**

**Background and Purpose of the Update:**  
The release of the Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 marks its transition to general availability. This stable API version is designed to provide enhanced programmatic control and integration capabilities for Azure PostgreSQL Flexible Server deployments. The update aims to address evolving operational requirements, particularly in maintenance management, backup integrity, and advanced security scenarios such as multi-tenant encryption.

**Specific Features and Detailed Changes:**  
The 2026-10-01 REST API version introduces several key features:
- **Expanded Maintenance Management:** The API now offers more granular controls for scheduling, monitoring, and managing maintenance operations on PostgreSQL Flexible Servers. This allows IT teams to automate maintenance workflows and minimize downtime.
- **Immutable Backups:** Support for immutable backups ensures that backup data cannot be altered or deleted, providing stronger guarantees for data protection and compliance. This feature is critical for organizations with strict regulatory requirements.
- **Multi-Tenant Encryption (Cross-Tenant Customer Encryption):** The API enables encryption scenarios where data is protected across multiple tenants, allowing customers to manage encryption keys and policies in environments with shared infrastructure.

**Technical Mechanisms and Implementation Methods:**  
- The REST API is accessed via HTTPS endpoints, adhering to Azure’s standard authentication and authorization mechanisms, such as Azure Active Directory (AAD) OAuth tokens.
- Maintenance management enhancements are implemented through new or updated API endpoints that allow querying and configuring maintenance windows, retrieving maintenance histories, and triggering maintenance actions.
- Immutable backups leverage Azure’s underlying storage infrastructure, enforcing write-once-read-many (WORM) policies at the backup layer. API endpoints provide operations for creating, listing, and restoring immutable backups.
- Multi-tenant encryption is facilitated by integrating with Azure Key Vault and customer-managed keys (CMK), with API endpoints to configure encryption settings and manage cross-tenant key assignments.

**Use Cases and Application Scenarios:**  
- **Automated Maintenance:** Enterprises can use the API to automate maintenance scheduling, integrate with CI/CD pipelines, and ensure consistent operational practices across multiple PostgreSQL servers.
- **Regulatory Compliance:** Organizations subject to regulations such as GDPR, HIPAA, or financial standards can leverage immutable backups to meet audit and retention requirements.
- **SaaS Providers:** Multi-tenant encryption enables SaaS providers to offer secure, isolated data environments for customers, with customer-managed keys ensuring data sovereignty.

**Important Considerations and Limitations:**  
- The API version is stable and generally available, but users should review documentation for endpoint-specific limitations, such as supported backup sizes, maintenance window constraints, and encryption key management policies.
- Immutable backups may incur additional storage costs and require careful planning for backup retention and lifecycle management.
- Multi-tenant encryption scenarios require proper configuration of Azure Key Vault and may necessitate cross-tenant permissions and policy management.

**Integration with Related Azure Services:**  
- The REST API integrates seamlessly with Azure Key Vault for encryption key management.
- It can be used in conjunction with Azure Monitor for operational insights and alerting.
- Backup and maintenance operations can be orchestrated alongside Azure Automation and Logic Apps for end-to-end workflow automation.

**Summary Sentence:**  
The Azure Database for PostgreSQL Flexible Server REST API version 2026-10-01 is now generally available, providing expanded maintenance management, immutable backup support, and multi-tenant encryption capabilities for enhanced operational control and security.

---

### 2. Generally Available: Route maps for Azure Route Server

**Published**: November 04, 2026 18:39:41 UTC
**Link**: [Generally Available: Route maps for Azure Route Server](https://azure.microsoft.com/updates?id=578966)

**Update ID**: 578966
**Data source**: Azure Updates API

**Categories**: Networking, Azure Route Server, Features

**Summary**:

- What was updated  
Route maps for Azure Route Server are now generally available in the Azure public cloud.

- Key changes or new features  
Route maps enable fine-grained control over both inbound and outbound routing for hybrid network connections. With route maps, customers can filter, modify, and manage routes advertised to and from Azure Route Server, allowing for advanced routing scenarios such as route filtering, prepending, and setting route attributes. This enhances flexibility and control in managing BGP routes between on-premises networks and Azure.

- Target audience affected  
Network architects, IT professionals, and developers responsible for hybrid cloud networking, especially those using Azure Route Server for BGP-based routing between Azure and on-premises environments.

- Important notes if any  
Route maps are now fully supported in production environments. This feature is particularly valuable for organizations requiring customized routing policies, improved security, and optimized traffic flows in their hybrid network setups. Existing Azure Route Server deployments can leverage route maps without major changes to their infrastructure. For implementation details, refer to the official documentation.

**Details**:

**Azure Update Report: Route Maps for Azure Route Server – General Availability**

**Background and Purpose of the Update:**  
Azure Route Server enables seamless integration between Azure virtual networks and network appliances, facilitating dynamic routing via Border Gateway Protocol (BGP). The general availability of route maps for Azure Route Server addresses the need for granular control over routing policies in hybrid cloud environments, allowing organizations to fine-tune how routes are exchanged between Azure and on-premises or partner networks.

**Specific Features and Detailed Changes:**  
With this update, route maps are now fully supported in the Azure public cloud for Azure Route Server. Route maps allow customers to define precise rules for manipulating routes advertised to and from the Route Server. This includes filtering routes, modifying route attributes, and controlling the propagation of routing information based on specific criteria. The feature provides both inbound and outbound route map capabilities, enabling users to:

- Filter routes based on prefix, AS path, or other BGP attributes.
- Modify route attributes such as local preference, metric, or next hop.
- Control which routes are advertised to Azure Route Server from peer devices and vice versa.

**Technical Mechanisms and Implementation Methods:**  
Route maps are implemented as a set of ordered rules that match specific route attributes and apply actions such as permit, deny, or modify. Administrators configure route maps through the Azure portal, CLI, or ARM templates, associating them with BGP peerings on the Route Server. The mechanism leverages BGP policy constructs, enabling real-time manipulation of route advertisements without requiring changes to the underlying network infrastructure.

**Use Cases and Application Scenarios:**  
- **Hybrid Connectivity:** Enterprises connecting Azure with on-premises data centers can use route maps to limit route propagation, ensuring only necessary prefixes are exchanged.
- **Multi-cloud Routing:** Organizations with multi-cloud architectures can control route advertisements between Azure and other cloud providers, optimizing routing paths and preventing route leaks.
- **Network Segmentation:** Route maps facilitate segmentation by restricting route visibility between different Azure virtual networks or between Azure and external networks.
- **Custom Routing Policies:** Businesses can implement advanced routing policies, such as preferring certain paths or avoiding specific prefixes, to meet compliance or performance requirements.

**Important Considerations and Limitations:**  
- Route maps are only available for Azure Route Server in the Azure public cloud.
- Careful configuration is required to avoid unintended route filtering or modification, which could impact connectivity.
- Route maps must be associated with specific BGP peerings; incorrect associations may result in incomplete routing policies.
- The feature does not replace network security controls; it is intended for routing policy management only.

**Integration with Related Azure Services:**  
Route maps for Azure Route Server integrate seamlessly with Azure Virtual Network, ExpressRoute, and VPN Gateway, enhancing hybrid and multi-cloud connectivity scenarios. They complement Azure’s network security and monitoring tools, such as Network Security Groups (NSGs) and Azure Monitor, by providing additional routing control without interfering with security policies.

**Summary Sentence:**  
Route maps for Azure Route Server are now generally available, offering Azure customers fine-grained control over inbound and outbound routing across hybrid connections, enabling precise management of routes advertised to and from Azure Route Server in the public cloud.

---

### 3. Public Preview: Azure Firewall IPv6 now supports application rules

**Published**: November 04, 2026 18:09:43 UTC
**Link**: [Public Preview: Azure Firewall IPv6 now supports application rules](https://azure.microsoft.com/updates?id=579507)

**Update ID**: 579507
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall now supports application rules for IPv6 traffic in Public Preview.

- Key changes or new features  
This update enables layer 7 (application-level) filtering for HTTP and HTTPS traffic over IPv6. Developers and IT professionals can now define application rules for IPv6 and dual-stack (IPv4/IPv6) deployments, allowing granular control of outbound web traffic based on domain names and protocols. This extends Azure Firewall’s application-level security capabilities to environments using IPv6, not just IPv4.

- Target audience affected  
Azure Firewall users, including developers and IT professionals managing network security, especially those deploying or planning dual-stack or IPv6-only architectures.

- Important notes  
This feature is currently in Public Preview and may not be suitable for production workloads until General Availability. Customers can now maintain consistent application rule policies across both IPv4 and IPv6 traffic, simplifying security management in modern cloud environments. Review Azure Firewall documentation for configuration details and limitations during the preview phase.

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Azure Firewall IPv6 now supports application rules

**Background and Purpose of the Update**  
Azure Firewall previously supported application rules for IPv4 traffic, enabling layer 7 filtering for HTTP and HTTPS. With the increasing adoption of IPv6 and dual-stack network architectures, organizations require consistent security controls across both IP versions. This update introduces application rule support for IPv6 traffic, addressing the need for advanced filtering and security in modern network environments.

**Specific Features and Detailed Changes**  
The update, now in Public Preview, enables Azure Firewall to apply application rules to IPv6 traffic. Application rules provide layer 7 filtering capabilities, specifically for HTTP and HTTPS protocols. Administrators can now define rules that inspect and control outbound IPv6 traffic based on fully qualified domain names (FQDNs), URLs, and web categories. This enhancement extends application-level controls to both IPv6-only and dual-stack (IPv4/IPv6) deployments, ensuring uniform policy enforcement regardless of IP version.

**Technical Mechanisms and Implementation Methods**  
Azure Firewall’s application rules operate at the application layer (OSI layer 7), inspecting HTTP and HTTPS requests. With this update, the firewall parses IPv6 packets, extracts relevant application data, and applies configured rules to determine whether to allow or deny traffic. The rules are managed via Azure Portal, ARM templates, or REST APIs, and are integrated into the firewall’s rule processing engine. The firewall maintains stateful inspection and supports logging and diagnostics for IPv6 application rule events.

**Use Cases and Application Scenarios**  
- **Dual-stack deployments:** Enterprises migrating to IPv6 or operating dual-stack environments can enforce consistent outbound web access policies across both IPv4 and IPv6.
- **Regulatory compliance:** Organizations requiring granular control over web traffic for compliance can now extend these controls to IPv6.
- **Security hardening:** Application rules help prevent unauthorized access to web resources, mitigating risks associated with IPv6 traffic.
- **Cloud-native architectures:** Modern applications leveraging IPv6 connectivity benefit from enhanced security without compromising performance or flexibility.

**Important Considerations and Limitations**  
- The feature is currently in Public Preview, which may involve limited support and potential changes before general availability.
- Only HTTP and HTTPS protocols are supported for IPv6 application rules; other protocols may require network rules.
- Customers should validate rule configurations in test environments before production deployment, as preview features may have undocumented behaviors.
- Monitoring and diagnostics for IPv6 application rules should be reviewed to ensure visibility and compliance.

**Integration with Related Azure Services**  
Azure Firewall application rules for IPv6 integrate seamlessly with other Azure networking services, including Virtual Networks, Azure Monitor for logging and diagnostics, and Azure Policy for governance. Administrators can leverage Azure Resource Manager (ARM) templates and REST APIs to automate rule deployment and management. The feature also supports integration with Azure Security Center for unified threat detection and response.

**Summary Sentence**  
Azure Firewall now supports application rules for IPv6 traffic in Public Preview, enabling layer 7 HTTP and HTTPS filtering for both IPv6 and dual-stack deployments, thereby extending consistent application-level security controls across modern network environments.

---

### 4. Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027

**Published**: November 04, 2026 17:40:28 UTC
**Link**: [Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027](https://azure.microsoft.com/updates?id=transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026)

**Update ID**: transition-to-azure-ad-to-query-data-from-azure-monitor-application-insights-by-31-march-2026
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Application Insights, Azure Monitor, Retirements

**Summary**:

- What was updated  
The retirement date for API keys used to query Azure Monitor Application Insights has been extended to March 31, 2027. After this date, API keys will no longer be supported for querying Application Insights data.

- Key changes or new features  
Developers and IT professionals must transition from using API keys to Microsoft Entra ID (formerly Azure Active Directory) for authentication when querying Application Insights data. Entra ID provides equivalent functionality and improved security and management capabilities.

- Target audience affected  
This update affects developers, DevOps engineers, and IT professionals who use API keys to access Application Insights data programmatically, including those integrating monitoring and analytics into custom applications, dashboards, or automation workflows.

- Important notes if any  
Begin planning your migration to Entra ID-based authentication as soon as possible to avoid service disruptions. Review your existing integrations and update them to use Entra ID before March 31, 2027. Microsoft recommends leveraging Entra ID for enhanced security, centralized identity management, and compliance. For detailed migration guidance, refer to the official documentation and the Azure Update link.

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Transition to Entra ID (formerly known as Azure AD) to query data from Azure Monitor application insights by March 31, 2027

**Background and Purpose of the Update:**  
Microsoft has announced an extension of the retirement date for API keys used to query Azure Monitor Application Insights data. The new retirement date is March 31, 2027. The purpose of this update is to enhance security and streamline authentication mechanisms by transitioning from legacy API keys to Microsoft Entra ID (formerly Azure Active Directory, Azure AD). Entra ID offers robust identity and access management capabilities, aligning with industry standards for secure data access.

**Specific Features and Detailed Changes:**  
The primary change is the deprecation of API keys for querying Application Insights data. After March 31, 2027, API keys will no longer be supported for this purpose. Users must transition to using Microsoft Entra ID for authentication. Entra ID provides all the functionality previously available via API keys, ensuring continuity in querying Application Insights data. This change affects all integrations, scripts, and applications that currently rely on API keys for accessing telemetry and analytics data from Application Insights.

**Technical Mechanisms and Implementation Methods:**  
The transition involves replacing API key-based authentication with Entra ID-based authentication. Entra ID uses OAuth 2.0 and OpenID Connect protocols, enabling secure, token-based access to Azure resources. To implement this change, technical professionals must:

- Register their applications in Entra ID to obtain client credentials.
- Configure permissions for Application Insights data access within Entra ID.
- Update code and scripts to use Entra ID tokens for authentication when querying Application Insights APIs.
- Utilize Microsoft identity libraries (such as MSAL) to facilitate token acquisition and management.

This approach provides enhanced security through centralized identity management, conditional access policies, and improved auditing capabilities.

**Use Cases and Application Scenarios:**  
Typical scenarios affected include:

- Automated monitoring solutions that query Application Insights for telemetry data.
- Custom dashboards and reporting tools that retrieve analytics from Application Insights.
- Integration with third-party services that require access to Application Insights data.
- DevOps pipelines and scripts that use Application Insights APIs for operational insights.

All these use cases must migrate to Entra ID authentication before the retirement date to ensure uninterrupted access.

**Important Considerations and Limitations:**  
- All existing API keys will cease to function after March 31, 2027.
- Migration to Entra ID may require code changes and updates to deployment configurations.
- Proper permission management in Entra ID is essential to maintain least privilege access.
- Organizations should review and update their security policies to leverage Entra ID’s advanced features.
- Testing and validation of new authentication flows are recommended to avoid disruptions.

**Integration with Related Azure Services:**  
Entra ID is tightly integrated with other Azure services, providing unified identity management across Azure Monitor, Application Insights, Log Analytics, and more. Transitioning to Entra ID simplifies authentication for cross-service scenarios, supports single sign-on, and enables centralized access control for all Azure resources.

**Summary Sentence:**  
Microsoft is retiring API keys for querying Azure Monitor Application Insights data and extending the transition deadline to March 31, 2027, requiring all users to migrate to Microsoft Entra ID authentication to ensure secure and uninterrupted access.

---

### 5. Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller

**Published**: November 04, 2026 17:13:51 UTC
**Link**: [Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller](https://azure.microsoft.com/updates?id=579162)

**Update ID**: 579162
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Compute, Azure Disk Storage, Virtual Machines, Compliance, Management, Feature

**Summary**:

- What was updated  
Azure has introduced public preview support for multi-disk crash-consistent VM restore points for virtual machines using Premium SSD v2 and Ultra Disks, specifically on VMs with SCSI disk controllers.

- Key changes or new features  
Developers and IT professionals can now create agent-less, crash-consistent restore points across multiple data disks (Premium SSD v2 and Ultra Disks) attached to a VM. This ensures that all disks are captured in a consistent state, simplifying backup and disaster recovery scenarios. The feature leverages the SCSI disk controller, enabling efficient and reliable restore point creation without requiring guest agents.

- Target audience affected  
This update is relevant to Azure users managing VMs with Premium SSD v2 or Ultra Disks, especially those responsible for backup, disaster recovery, and data protection. Developers and IT professionals working with high-performance workloads and multi-disk configurations will benefit from improved consistency and reliability.

- Important notes if any  
The feature is currently in public preview and only available for VMs with SCSI disk controllers. It supports agent-less restore point creation, but does not provide application consistency (crash-consistent only). Users should validate compatibility and performance in their environments before production use. For more details, refer to the official Azure update link.

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Multi-disk crash-consistent VM restore points for Premium SSD v2 and Ultra Disks on VMs with SCSI disk controller  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=579162)

---

### Background and Purpose of the Update

This update introduces the public preview of multi-disk crash-consistent restore points for Azure virtual machines (VMs) that utilize Premium SSD v2 and Ultra data disks, specifically on VMs equipped with SCSI disk controllers. The primary purpose is to enhance data protection and recovery capabilities by enabling users to capture crash-consistent restore points across multiple disks without relying on in-guest agents. This addresses the need for consistent backup and recovery in scenarios where VMs use high-performance storage and SCSI controllers.

---

### Specific Features and Detailed Changes

- **Multi-disk Crash-Consistent Restore Points:** Users can now create restore points that capture the state of all attached Premium SSD v2 and Ultra disks at a single moment, ensuring crash consistency across these disks.
- **Agent-less Operation:** The solution does not require any backup or snapshot agents to be installed inside the VM, simplifying management and reducing dependencies.
- **Support for SCSI Disk Controllers:** This capability is specifically available for VMs configured with SCSI disk controllers, aligning with common configurations for high-performance and scalable workloads.

---

### Technical Mechanisms and Implementation Methods

- **Crash-Consistent Restore Points:** The mechanism captures the data on all attached Premium SSD v2 and Ultra disks at the exact same point in time, ensuring that the disk states are consistent as if the VM had experienced a sudden power loss. This is crucial for applications that write data across multiple disks.
- **Agent-less Snapshotting:** The process leverages Azure’s native snapshot capabilities at the storage layer, removing the need for in-guest agents and reducing operational complexity.
- **SCSI Controller Requirement:** The feature is enabled only on VMs with SCSI disk controllers, which is a common configuration for attaching multiple high-performance disks.

---

### Use Cases and Application Scenarios

- **Backup and Disaster Recovery:** Enterprises can use this feature to create consistent restore points for VMs running critical workloads on Premium SSD v2 and Ultra disks, facilitating reliable backup and disaster recovery operations.
- **Application Consistency Across Multiple Disks:** Workloads that distribute data across several disks, such as databases or large-scale transactional systems, benefit from crash-consistent restore points to ensure data integrity during restores.
- **Agent-less Environments:** Scenarios where installing agents is not feasible (e.g., due to compliance or OS restrictions) can now leverage native Azure capabilities for backup.

---

### Important Considerations and Limitations

- **Public Preview:** The feature is currently in public preview, which means it is not recommended for production workloads without thorough validation.
- **Disk and Controller Support:** Only Premium SSD v2 and Ultra disks attached to VMs with SCSI controllers are supported. Other disk types or controller configurations are not included in this preview.
- **Crash Consistency:** The restore points are crash-consistent, not application-consistent. Applications with in-memory data or ongoing transactions may require additional steps to ensure full consistency.

---

### Integration with Related Azure Services

- **Azure Backup and Restore:** The new restore points can be integrated into backup and restore workflows, enhancing recovery options for supported VMs.
- **Azure Resource Manager (ARM):** Restore points can be managed via ARM templates, CLI, or PowerShell, aligning with infrastructure-as-code practices.
- **Snapshot Management:** The feature complements Azure’s existing snapshot and backup services, providing more granular and consistent recovery points for advanced storage configurations.

---

**Summary:**  
Azure now offers public preview support for agent-less, multi-disk crash-consistent restore points on VMs with Premium SSD v2 and Ultra disks using SCSI controllers, enabling enhanced backup and recovery scenarios for high

---


*This report was automatically generated - 2026-11-05 03:03:11 UTC*