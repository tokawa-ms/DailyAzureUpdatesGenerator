# September 23, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 23, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Using Server-sent events with Application Gateway

**Published**: September 22, 2025 17:00:22 UTC
**Link**: [Generally Available: Using Server-sent events with Application Gateway](https://azure.microsoft.com/updates?id=503909)

**Update ID**: 503909
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Management, Features

**Summary**:

- What was updated  
Azure Application Gateway now generally supports Server-sent events (SSE), enabling real-time, one-way data streaming from server to client over a persistent HTTP connection.

- Key changes or new features  
The update brings GA support for SSE, allowing applications behind Application Gateway to push continuous updates to clients without requiring client polling. This enhances scenarios like live notifications, real-time feeds, and streaming data. The gateway efficiently manages persistent connections and ensures seamless SSE traffic handling.

- Target audience affected  
Developers building real-time web applications and IT professionals managing Azure networking infrastructure who require reliable, scalable server push capabilities through Application Gateway.

- Important notes if any  
Ensure your backend services and clients are configured to use SSE protocols correctly. This feature improves performance and scalability for real-time data delivery but requires proper connection management. Review Application Gateway documentation for configuration details and best practices to optimize SSE usage.

**Details**:

The recent Azure update announces the general availability of Server-Sent Events (SSE) support in Azure Application Gateway, enabling IT professionals to implement efficient, real-time, unidirectional data streaming from servers to clients over HTTP connections. This enhancement addresses the growing demand for scalable, low-latency event-driven web applications by integrating SSE natively into the Application Gateway's Layer 7 load balancing capabilities.

**Background and Purpose**  
Server-Sent Events provide a standardized way for servers to push continuous updates to clients over a single, long-lived HTTP connection without requiring clients to poll repeatedly. Prior to this update, Application Gateway did not fully support SSE, which limited its use in scenarios requiring real-time streaming such as live dashboards, notifications, or telemetry data feeds. By enabling SSE support, Azure Application Gateway now facilitates seamless, persistent server-to-client communication, improving performance and reducing resource consumption compared to traditional polling or WebSocket fallback mechanisms.

**Specific Features and Detailed Changes**  
- **SSE Protocol Support:** Application Gateway now fully supports the HTTP/1.1 SSE protocol, including handling of the `text/event-stream` content type and maintaining persistent connections without premature termination.  
- **Connection Management:** It manages long-lived HTTP connections efficiently, ensuring that SSE streams remain open and stable through the gateway.  
- **Load Balancing and SSL Termination:** SSE streams benefit from Application Gateway’s existing Layer 7 load balancing, SSL offloading, and Web Application Firewall (WAF) capabilities without disruption to event streams.  
- **Health Probes and Timeouts:** The gateway intelligently handles health probes and connection timeouts to maintain SSE stream integrity.

**Technical Mechanisms and Implementation Methods**  
Application Gateway acts as a reverse proxy that terminates client connections and forwards requests to backend servers. With SSE support, it recognizes and preserves the `text/event-stream` response headers and keeps the HTTP connection open indefinitely, forwarding server push events to clients as they occur. The gateway’s connection timeout settings are adjusted to accommodate long-lived SSE connections, preventing premature closure. Additionally, Application Gateway’s WAF inspects SSE traffic without interfering with the event stream format, maintaining security compliance.

**Use Cases and Application Scenarios**  
- **Real-time Dashboards:** Streaming live metrics or analytics data to web clients without polling overhead.  
- **Notification Systems:** Delivering instant notifications or alerts in web applications.  
- **Telemetry and Monitoring:** Continuous streaming of logs or system health data to client consoles.  
- **Financial Services:** Streaming stock prices or market data updates in near real-time.  
- **IoT Applications:** Pushing sensor data updates to dashboards or control panels.

**Important Considerations and Limitations**  
- **Unidirectional Streaming:** SSE supports only server-to-client streaming; bidirectional communication requires WebSockets or other protocols.  
- **Connection Limits:** Long-lived connections consume resources; capacity planning is essential to avoid gateway saturation.  
- **Timeout Configuration:** Default idle timeouts may need adjustment to accommodate persistent SSE connections.  
- **Browser Compatibility:** SSE is widely supported but may require fallback mechanisms for legacy clients.  
- **Security:** Ensure WAF policies are tuned to allow legitimate SSE traffic without false positives.

**Integration with Related Azure Services**  
- **Azure Web Apps and Azure Kubernetes Service (AKS):** Backend services hosted on these platforms can leverage SSE through Application Gateway for scalable real-time streaming.  
- **Azure Monitor and Azure Event Hubs:** SSE can be used to stream monitoring or event data to client dashboards.  
- **Azure Front Door:** While Application Gateway handles SSE at regional scale, Front Door can complement global routing strategies.  
- **Azure Active Directory (AAD):** Authentication and authorization can be enforced at the gateway level for SSE endpoints.

In summary, the general availability of Server-Sent Events support in Azure Application Gateway empowers IT professionals to build scalable, secure, and efficient real-time web applications by leveraging persistent HTTP connections for server-to-client

---

### 2. Public Preview: Signed request on Azure Front Door 

**Published**: September 22, 2025 17:00:22 UTC
**Link**: [Public Preview: Signed request on Azure Front Door ](https://azure.microsoft.com/updates?id=501169)

**Update ID**: 501169
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Front Door, Features

**Summary**:

- What was updated  
Azure Front Door introduced a public preview of the signed request feature to enhance secure access control for content delivery.

- Key changes or new features  
This feature enables organizations to restrict access to their content—such as media streams, files, or APIs—by requiring requests to be signed with a token or signature. It helps prevent unauthorized access and URL tampering by validating the authenticity and integrity of requests at the edge. Developers can configure signed URLs or headers with expiration times and custom policies, improving security for content distribution scenarios.

- Target audience affected  
Developers and IT professionals managing content delivery and security via Azure Front Door, especially those delivering media, files, or APIs who need fine-grained access control and protection against unauthorized access.

- Important notes if any  
This feature is currently in public preview, so it should be used with caution in production environments. Users should review the documentation for configuration details and limitations. Integration with existing Azure Front Door routing and security policies is supported, enabling seamless adoption.  

For more details, visit: https://azure.microsoft.com/updates?id=501169

**Details**:

The public preview of Azure Front Door’s signed request feature introduces a robust mechanism to enforce fine-grained access control over content delivery, addressing the need for secure and controlled distribution of digital assets such as media streams, files, and APIs. This update enhances Azure Front Door’s capability to protect content by enabling organizations to generate cryptographically signed URLs or requests that clients must present to access protected resources, thereby preventing unauthorized access and mitigating risks such as URL sharing or hotlinking.

**Background and Purpose:**  
Azure Front Door is a global, scalable entry point for web applications and content delivery that provides high availability, low latency, and security features. Prior to this update, controlling access to content often relied on IP restrictions, authentication tokens, or custom logic at the origin. However, these methods can be complex to manage and may not prevent direct URL sharing. The signed request feature was introduced to provide a standardized, secure, and scalable way to restrict content access by embedding cryptographic signatures within URLs or HTTP headers, ensuring that only requests with valid signatures and within specified constraints (such as expiration time or IP ranges) are honored.

**Specific Features and Detailed Changes:**  
- **Signed URL and Signed Header Support:** Organizations can configure Azure Front Door to require signed requests either via query string parameters or HTTP headers.  
- **Expiration and Validity Controls:** Signed requests include expiration timestamps, limiting the window during which the request is valid, reducing the risk of replay attacks.  
- **Customizable Access Policies:** Policies can specify parameters such as allowed IP ranges, HTTP methods, and request paths to further restrict access.  
- **Integration with Azure Front Door Rules Engine:** The signed request validation is integrated into the rules engine, allowing conditional enforcement based on request attributes.  
- **Key Management:** Signing keys are managed securely within Azure Front Door, supporting key rotation and multiple keys to ensure operational security.

**Technical Mechanisms and Implementation Methods:**  
The signed request feature works by generating a signature using a shared secret key and request-specific parameters (e.g., URL path, expiration time). This signature is appended to the request as a query parameter or included in a header. When Azure Front Door receives a request, it validates the signature by recomputing it using the configured secret keys and comparing it against the signature presented. If the signature is invalid, expired, or does not meet policy criteria, the request is rejected with an HTTP 403 Forbidden status. The validation process is performed at the edge, ensuring unauthorized requests are blocked before reaching backend origins, optimizing security and reducing backend load.

**Use Cases and Application Scenarios:**  
- **Secure Media Streaming:** Restricting access to video or audio streams to authorized users or clients for a limited time.  
- **File Download Protection:** Ensuring that downloadable assets such as software installers or documents are accessed only through signed URLs distributed via authenticated channels.  
- **API Access Control:** Protecting APIs exposed through Azure Front Door by requiring signed requests to prevent unauthorized or automated access.  
- **Temporary Access Grants:** Providing time-limited access to resources for partners or customers without requiring full authentication infrastructure.

**Important Considerations and Limitations:**  
- As a public preview feature, signed request functionality may have limitations in SLA guarantees and could undergo changes before general availability.  
- Key management requires careful handling to avoid exposure of signing secrets; Azure Front Door provides secure storage but operational best practices must be followed.  
- The feature currently supports specific signing algorithms and may have constraints on request size or complexity.  
- Integration with other authentication mechanisms (e.g., Azure AD) is complementary but not replaced by signed requests; organizations should design layered security accordingly.

**Integration with Related Azure Services:**  
- **Azure Front Door Rules Engine:** Enables conditional application of signed request validation based on request attributes.  
- **Azure Key Vault (indirectly):** While Azure Front Door manages signing keys internally, integration with Azure Key Vault for key lifecycle management may be part of

---

### 3. Generally Available: Vaulted backup for Azure Files (Premium)

**Published**: September 22, 2025 16:15:14 UTC
**Link**: [Generally Available: Vaulted backup for Azure Files (Premium)](https://azure.microsoft.com/updates?id=503806)

**Update ID**: 503806
**Data source**: Azure Updates API

**Categories**: Launched, Management and governance, Storage, Azure Backup, Management, Security, Features

**Summary**:

- What was updated  
Azure Backup now supports vaulted backup for Azure Files Premium shares, reaching general availability.

- Key changes or new features  
This update enables enterprise-grade, long-term backup and recovery for Azure Files Premium shares using vaulted backup. It protects against accidental deletion, ransomware, and other threats by storing backups in a secure, isolated vault. The feature ensures compliance and business continuity with point-in-time restore capabilities and retention policies.

- Target audience affected  
Developers and IT professionals managing Azure Files Premium shares who require robust backup solutions for critical file data, especially in scenarios demanding high performance and compliance.

- Important notes if any  
Vaulted backup for Azure Files Premium shares is now fully supported and production-ready. Users should review backup policies and retention settings to align with organizational compliance and recovery objectives. This enhancement complements existing Azure Backup capabilities, providing a unified backup experience across Azure storage services.

For more details, visit: https://azure.microsoft.com/updates?id=503806

**Details**:

The recent Azure update announces the general availability of vaulted backup support for Azure Files Premium shares, enhancing data protection and recovery capabilities for high-performance file storage workloads. This feature extends Azure Backup’s robust, scalable, and secure backup solution to premium-tier Azure Files, addressing critical business continuity and compliance requirements.

**Background and Purpose**  
Azure Files Premium offers high-throughput, low-latency file shares backed by SSD storage, optimized for IO-intensive enterprise applications such as databases, analytics, and media workloads. Prior to this update, backup options for premium file shares were limited or required manual configurations, potentially exposing organizations to data loss risks from accidental deletion, corruption, or ransomware attacks. The introduction of vaulted backup support brings enterprise-grade, automated backup and restore capabilities natively integrated with Azure Backup, ensuring consistent data protection aligned with organizational SLAs and regulatory compliance.

**Specific Features and Detailed Changes**  
- **Vaulted Backup Support:** Premium Azure Files shares can now be protected using Recovery Services vaults, enabling centralized management of backup policies and retention.  
- **Policy-Based Scheduling:** Users can define backup schedules and retention policies to automate snapshot creation and long-term retention, reducing operational overhead.  
- **Instant Restore and Point-in-Time Recovery:** Enables rapid recovery of file shares to a specific backup point, minimizing downtime in disaster scenarios.  
- **Cross-Region Restore:** Supports restoring backups to different regions for enhanced disaster recovery strategies.  
- **Encryption and Security:** Backups are encrypted at rest and in transit, leveraging Azure Backup’s security features including role-based access control (RBAC) and multi-factor authentication (MFA).

**Technical Mechanisms and Implementation Methods**  
Vaulted backup for Azure Files Premium leverages Azure Backup’s snapshot-based backup technology. When a backup job is triggered, Azure Backup creates a snapshot of the Azure Files share at the storage layer, capturing a point-in-time consistent state without impacting ongoing operations. These snapshots are then stored securely within the Recovery Services vault, which acts as a centralized repository for backup data. The integration uses the Azure Resource Manager (ARM) model, allowing users to configure backup policies and initiate restores via the Azure portal, CLI, PowerShell, or REST APIs. The backup process is optimized to minimize performance impact on premium shares by leveraging incremental snapshots, which only capture changes since the last backup.

**Use Cases and Application Scenarios**  
- **Enterprise File Shares:** Organizations running critical applications on Azure Files Premium can ensure data durability and quick recovery from accidental deletions or corruption.  
- **Regulatory Compliance:** Businesses subject to data retention regulations can automate long-term retention of file share backups.  
- **Ransomware Protection:** Enables point-in-time recovery to mitigate ransomware or malicious data modifications.  
- **Disaster Recovery:** Supports cross-region restore scenarios to maintain business continuity during regional outages or disasters.  
- **Dev/Test Environments:** Facilitates cloning of production file shares from backups for development and testing purposes without impacting live data.

**Important Considerations and Limitations**  
- **Backup Frequency and Retention:** While policy-based scheduling is flexible, organizations must balance backup frequency and retention duration against storage costs and recovery objectives.  
- **Performance Impact:** Although incremental snapshots minimize disruption, heavy backup operations may still introduce latency; scheduling backups during off-peak hours is recommended.  
- **Supported Regions:** Vaulted backup availability for Azure Files Premium may vary by region; verify regional support before deployment.  
- **Restore Granularity:** Currently, restores are performed at the share level; file-level restore is not natively supported and may require mounting restored shares.  
- **Pricing:** Backup storage and operations incur additional costs; review Azure Backup pricing details to estimate expenses.

**Integration with Related Azure Services**  
- **Azure Recovery Services Vault:** Acts as the centralized backup management and storage entity.  
- **Azure Monitor and Alerts:** Can be configured to monitor backup job status and trigger alerts on failures or anomalies.  
- **Azure Policy

---


*This report was automatically generated - 2025-09-23 03:01:59 UTC*