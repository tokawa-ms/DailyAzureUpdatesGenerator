# November 13, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: November 13, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Public Preview: JWT validation with Azure Front Door Auth Policy 

**Published**: November 12, 2026 22:36:37 UTC
**Link**: [Public Preview: JWT validation with Azure Front Door Auth Policy ](https://azure.microsoft.com/updates?id=577673)

**Update ID**: 577673
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure Front Door, Features

**Summary**:

- What was updated  
Azure Front Door Premium now supports JWT (JSON Web Token) validation via Auth Policy, available in public preview.

- Key changes or new features  
You can configure Azure Front Door to validate bearer tokens (JWTs) issued by Microsoft Entra ID (formerly Azure AD) at the network edge. This means authentication occurs before requests reach your backend APIs or web applications. The feature allows you to enforce access control policies and reject unauthorized requests early, reducing load on your origin servers and improving security posture.

- Target audience affected  
Developers and IT professionals managing APIs or web applications behind Azure Front Door, especially those using Microsoft Entra ID for authentication.

- Important notes if any  
- This feature is currently in public preview and available only on Azure Front Door Premium.  
- JWT validation at the edge helps centralize authentication and can simplify backend application logic.  
- You must configure the Auth Policy and ensure your applications issue or accept tokens from Microsoft Entra ID.  
- Review documentation for integration steps and limitations during the preview phase.

For more details, see the [official update](https://azure.microsoft.com/updates?id=577673).

**Details**:

**Azure Update Report: Public Preview – JWT Validation with Azure Front Door Auth Policy**

**Background and Purpose of the Update**  
Azure Front Door Premium now introduces the public preview of JSON Web Token (JWT) validation through its Auth Policy feature. The primary purpose of this update is to enable IT professionals to validate bearer tokens, specifically those issued by Microsoft Entra ID, directly at the edge. By performing authentication checks before requests reach APIs or web applications, organizations can enhance security, reduce unnecessary backend load, and ensure only authenticated traffic is processed further.

**Specific Features and Detailed Changes**  
This update adds JWT validation capabilities to Azure Front Door Auth Policy. Key features include:
- Edge-level validation of bearer tokens issued by Microsoft Entra ID.
- Enforcement of authentication policies before requests are forwarded to backend services.
- Integration with Azure Front Door Premium, leveraging its global edge network for distributed authentication.

This change allows administrators to configure authentication policies that inspect incoming HTTP requests for valid JWTs, ensuring that only requests with properly issued and unexpired tokens are allowed through.

**Technical Mechanisms and Implementation Methods**  
The JWT validation mechanism works as follows:
- Azure Front Door Auth Policy intercepts incoming HTTP requests at the edge.
- It checks for the presence of a bearer token in the Authorization header.
- The token is validated against Microsoft Entra ID, confirming its authenticity, issuer, and expiration.
- Only requests with valid tokens are forwarded to the backend APIs or web applications; invalid or missing tokens result in an authentication failure response.

Configuration is managed through Azure Front Door Premium, where administrators can define authentication policies specifying the required token issuer (Microsoft Entra ID) and validation parameters.

**Use Cases and Application Scenarios**  
Practical application scenarios include:
- Securing public-facing APIs and web applications by enforcing authentication at the edge, reducing exposure to unauthorized traffic.
- Offloading authentication logic from backend services, improving performance and scalability.
- Integrating with Microsoft Entra ID for seamless identity management across enterprise applications.
- Protecting sensitive endpoints from unauthenticated access, especially in distributed or multi-region deployments.

**Important Considerations and Limitations**  
- The feature is currently in public preview and available only on Azure Front Door Premium.
- JWT validation is limited to tokens issued by Microsoft Entra ID; tokens from other issuers are not supported in this preview.
- As with all preview features, production use should be approached with caution, and organizations should monitor for changes or updates.
- Edge validation may require updates to client applications to ensure bearer tokens are included in requests.

**Integration with Related Azure Services**  
This update tightly integrates Azure Front Door Premium with Microsoft Entra ID (formerly Azure Active Directory), enabling seamless authentication workflows. It complements existing security features such as Web Application Firewall (WAF) and integrates with Azure API Management and backend services, allowing for a layered security approach.

**Summary Sentence**  
Azure Front Door Premium now offers public preview support for JWT validation via Auth Policy, enabling edge-level authentication of Microsoft Entra ID bearer tokens to enhance security and streamline access control for APIs and web applications.

---

### 2. Generally Available: Azure Front Door mutual TLS authentication

**Published**: November 12, 2026 22:27:35 UTC
**Link**: [Generally Available: Azure Front Door mutual TLS authentication](https://azure.microsoft.com/updates?id=577678)

**Update ID**: 577678
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Front Door, Features

**Summary**:

- What was updated  
Azure Front Door Premium now offers General Availability (GA) support for mutual TLS (mTLS) authentication.

- Key changes or new features  
Mutual TLS (mTLS), also known as client certificate authentication, enables Azure Front Door to require and validate X.509 client certificates from connecting clients. This feature strengthens security by ensuring both the client and server authenticate each other during the TLS handshake. It is particularly useful for protecting sensitive applications and APIs, especially in business-to-business (B2B), Internet of Things (IoT), and financial services scenarios.

- Target audience affected  
Developers and IT professionals managing secure web applications, APIs, or services that require strong client authentication. This includes teams working in regulated industries or handling sensitive data, such as finance, healthcare, and IoT solutions.

- Important notes if any  
To use mTLS, you must configure your Azure Front Door Premium instance to require client certificates and manage trusted certificate authorities. This feature is only available in the Premium SKU. Proper certificate lifecycle management and secure storage are essential. Review Azure documentation for implementation guidance and best practices to avoid service disruptions.

For more details, see the official update: https://azure.microsoft.com/updates?id=577678

**Details**:

**Azure Update Report: Azure Front Door Mutual TLS Authentication (Generally Available)**

**Background and Purpose of the Update**  
Azure Front Door Premium now offers mutual TLS (mTLS) authentication, also known as client certificate authentication, as a generally available feature. The primary purpose of this update is to enhance security for sensitive applications and APIs, particularly in business-to-business (B2B), Internet of Things (IoT), and financial scenarios. mTLS enables both the client and server to authenticate each other, providing a higher level of trust compared to traditional TLS, which only authenticates the server.

**Specific Features and Detailed Changes**  
With this update, Azure Front Door Premium supports X.509 client certificates for mTLS authentication. This allows organizations to require clients to present a valid certificate during the TLS handshake, ensuring that only authorized clients can access protected endpoints. The feature is integrated natively within Azure Front Door, eliminating the need for custom authentication logic or additional infrastructure.

**Technical Mechanisms and Implementation Methods**  
Mutual TLS is implemented by configuring Azure Front Door to require client certificates for incoming HTTPS connections. During the TLS handshake, the client presents its X.509 certificate, which Azure Front Door validates against a trusted certificate authority (CA) or a specified set of certificates. If the certificate is valid, the connection proceeds; otherwise, access is denied. This mechanism leverages standard TLS protocols and X.509 certificate formats, ensuring compatibility with existing certificate management solutions.

**Use Cases and Application Scenarios**  
This feature is particularly relevant for:  
- **Business-to-Business (B2B) Applications:** Ensuring that only trusted partners can access APIs or services.  
- **Internet of Things (IoT):** Securing device-to-cloud communication by requiring devices to authenticate with certificates.  
- **Financial Services:** Protecting sensitive financial APIs and data exchanges with strong client authentication.  
- **Enterprise APIs:** Restricting access to internal APIs for authenticated clients, reducing the risk of unauthorized access.

**Important Considerations and Limitations**  
- **Certificate Management:** Organizations must manage client certificates, including issuance, renewal, and revocation, to maintain security.  
- **Compatibility:** Only Azure Front Door Premium supports mTLS; Standard or Classic tiers do not offer this feature.  
- **Performance Impact:** mTLS may introduce additional overhead during the TLS handshake due to certificate validation.  
- **Configuration:** Proper configuration of trusted certificate authorities and certificate validation policies is critical to ensure secure operation.  
- **Client Support:** Clients must be capable of presenting X.509 certificates during the TLS handshake.

**Integration with Related Azure Services**  
Azure Front Door mTLS authentication can be integrated with other Azure security and networking services, such as Azure Key Vault for certificate storage and management, Azure Application Gateway for additional layer 7 security, and Azure API Management for API-level access control. This integration enables a comprehensive security posture across distributed applications and services hosted on Azure.

**Summary Sentence**  
Azure Front Door Premium now generally supports mutual TLS authentication using X.509 client certificates, enabling secure client authentication for sensitive applications and APIs in B2B, IoT, and financial scenarios.

---

### 3. Public Preview: Auto scaling of ingestion limits in Azure Monitor workspace

**Published**: November 12, 2026 18:23:52 UTC
**Link**: [Public Preview: Auto scaling of ingestion limits in Azure Monitor workspace](https://azure.microsoft.com/updates?id=578207)

**Update ID**: 578207
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, DevOps, Management and governance, Azure Kubernetes Service (AKS), Azure Monitor, Feature

**Summary**:

- What was updated  
Azure Monitor Workspace (AMW) now supports auto scaling of data ingestion limits, available in Public Preview.

- Key changes or new features  
A new per-workspace auto scaling feature dynamically adjusts ingestion limits (quota ceilings) based on real-time usage patterns. When enabled, Azure Monitor automatically increases or decreases the data ingestion quota to maintain system health and accommodate workload fluctuations, reducing the need for manual quota management.

- Target audience affected  
Developers and IT professionals managing Azure Monitor Workspaces, especially those dealing with variable or unpredictable telemetry and log data volumes.

- Important notes if any  
Auto scaling must be enabled per workspace; it is not on by default. This feature helps prevent data loss or throttling during usage spikes but may impact cost, as higher ingestion can lead to increased charges. Users should monitor their usage and costs accordingly. This is a Public Preview feature, so it may not be suitable for production workloads requiring strict SLAs.

Data source: Using API data  
For more details, see the official update: https://azure.microsoft.com/updates?id=578207

**Details**:

**Azure Update Technical Explanation: Public Preview – Auto Scaling of Ingestion Limits in Azure Monitor Workspace**

**Background and Purpose of the Update**  
Azure Monitor Workspace (AMW) is a central component for collecting, analyzing, and acting on telemetry data from cloud and on-premises environments. Traditionally, ingestion limits (the maximum amount of data that can be ingested per workspace) have been statically set. This static configuration can lead to operational challenges: either over-provisioning (wasting resources and cost) or under-provisioning (risking dropped data and service disruptions during usage spikes). The purpose of this update is to introduce an automatic, per-workspace scaling mechanism for ingestion limits, enabling more adaptive and resilient monitoring operations.

**Specific Features and Detailed Changes**  
- **Per-Workspace Auto Scaling:** The feature allows each Azure Monitor Workspace to automatically adjust its ingestion limits based on real-time usage patterns.
- **Dynamic Quota Ceiling:** When auto scaling is enabled, the system dynamically modifies the ingestion quota ceiling, ensuring that the workspace can handle variable telemetry loads without manual intervention.
- **Public Preview Availability:** This capability is now available in public preview, allowing customers to test and evaluate the feature in their environments.

**Technical Mechanisms and Implementation Methods**  
- **Usage Pattern Analysis:** The system continuously observes ingestion patterns within each workspace.
- **Automated Adjustment:** Based on these observations, the ingestion quota ceiling is programmatically increased or decreased to maintain healthy workspace operation.
- **Configuration:** Administrators can enable or disable auto scaling for each workspace, providing granular control over ingestion management.
- **No Manual Scaling Required:** The automation eliminates the need for manual quota requests or adjustments, reducing operational overhead.

**Use Cases and Application Scenarios**  
- **Variable Workload Environments:** Organizations with fluctuating telemetry data volumes (e.g., during incident spikes, seasonal events, or dynamic scaling of monitored resources) benefit from automatic scaling, ensuring no data loss or ingestion throttling.
- **Cost Optimization:** By avoiding over-provisioning, organizations can optimize monitoring costs, only scaling ingestion limits as needed.
- **Operational Resilience:** Ensures continuous data collection during unexpected surges, supporting critical monitoring and alerting workflows.

**Important Considerations and Limitations**  
- **Preview Feature:** As this is a public preview, it may not be suitable for production-critical workloads without proper validation.
- **Per-Workspace Scope:** Auto scaling applies at the workspace level; it does not aggregate or coordinate limits across multiple workspaces.
- **Quota Management:** While auto scaling adjusts limits dynamically, there may still be upper bounds or constraints defined by Azure Monitor service policies.

**Integration with Related Azure Services**  
- **Azure Monitor Ecosystem:** The feature integrates natively with Azure Monitor Workspace, supporting all telemetry sources routed through AMW.
- **Compatibility:** It complements other Azure Monitor features such as data collection rules, alerting, and visualization, by ensuring ingestion capacity dynamically matches operational needs.
- **No Impact on Data Sources:** The ingestion auto scaling is transparent to upstream data sources and does not require changes to agents or telemetry emitters.

**Summary Sentence**  
The public preview of auto scaling ingestion limits in Azure Monitor Workspace introduces a per-workspace capability to dynamically adjust data ingestion quotas based on observed usage patterns, enhancing operational resilience and cost efficiency for monitoring solutions.

---

### 4. Public Preview: SQL performance monitoring for Azure SQL Managed Instance

**Published**: November 12, 2026 16:59:40 UTC
**Link**: [Public Preview: SQL performance monitoring for Azure SQL Managed Instance](https://azure.microsoft.com/updates?id=574158)

**Update ID**: 574158
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Azure SQL Managed Instance, Feature

**Summary**:

- What was updated  
Public preview of Microsoft-managed SQL performance monitoring for Azure SQL Managed Instance.

- Key changes or new features  
A new, built-in performance monitoring solution is now available for Azure SQL Managed Instance. This feature provides integrated monitoring capabilities directly within the Azure portal, eliminating the need for custom scripts or third-party/disconnected tools. It offers real-time and historical insights into SQL performance metrics, including resource utilization, query performance, and potential bottlenecks.

- Target audience affected  
Developers and IT professionals who manage or monitor business-critical workloads on Azure SQL Managed Instance.

- Important notes if any  
The feature is currently in public preview and may not yet be suitable for production environments. Users can access performance data natively in the Azure portal, simplifying monitoring and troubleshooting processes. This update helps reduce operational overhead and improves visibility into SQL Managed Instance workloads. Feedback during the preview phase is encouraged to help shape the final release.

For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=574158).

**Details**:

**Azure Update Report: Public Preview – SQL Performance Monitoring for Azure SQL Managed Instance**

**Background and Purpose of the Update:**  
Traditionally, monitoring performance for Azure SQL Managed Instance workloads has required IT professionals to rely on custom scripts and third-party, disconnected monitoring tools. This approach can lead to fragmented visibility, increased operational complexity, and challenges in maintaining consistent monitoring standards across business-critical environments. The public preview of Microsoft-managed performance monitoring aims to address these challenges by providing a unified, integrated solution directly within the Azure ecosystem.

**Specific Features and Detailed Changes:**  
The update introduces a Microsoft-managed performance monitoring capability for Azure SQL Managed Instance. This feature allows customers to monitor SQL performance without the need for custom scripts or external tools. Key features include:

- Centralized performance monitoring for SQL Managed Instance workloads.
- Native integration with Azure, reducing reliance on disconnected solutions.
- Enhanced visibility into workload performance metrics, enabling proactive management.

These changes streamline the monitoring process, providing IT professionals with a consistent and reliable method to track and analyze SQL performance within their managed instances.

**Technical Mechanisms and Implementation Methods:**  
The performance monitoring solution is implemented as a Microsoft-managed service within Azure SQL Managed Instance. It leverages Azure’s native monitoring infrastructure to collect, aggregate, and display performance metrics. The technical mechanisms likely involve:

- Automated collection of SQL performance data from managed instances.
- Integration with Azure monitoring dashboards for real-time visibility.
- Use of standardized telemetry and logging to ensure data consistency.

This approach eliminates the need for manual script deployment and maintenance, allowing IT teams to focus on interpreting performance data rather than managing monitoring infrastructure.

**Use Cases and Application Scenarios:**  
This update is particularly beneficial for organizations running business-critical workloads on Azure SQL Managed Instance. Typical use cases include:

- Monitoring high-transaction databases to ensure optimal performance.
- Detecting and diagnosing performance bottlenecks in production environments.
- Supporting compliance and audit requirements with standardized monitoring.
- Reducing operational overhead by consolidating monitoring within Azure.

Application scenarios span industries such as finance, healthcare, and retail, where SQL Managed Instance is used for mission-critical applications requiring robust performance monitoring.

**Important Considerations and Limitations:**  
As this feature is in public preview, IT professionals should be aware of potential limitations:

- The preview may not support all SQL performance metrics or advanced customization.
- Integration with existing monitoring workflows may require adjustments.
- Preview features may be subject to change based on customer feedback and further development.

It is recommended to review Microsoft’s documentation and support channels for up-to-date information on supported metrics and limitations during the preview phase.

**Integration with Related Azure Services:**  
The Microsoft-managed performance monitoring solution is designed for seamless integration with Azure’s broader monitoring ecosystem. This includes:

- Azure Monitor: Centralized dashboarding and alerting capabilities.
- Azure Log Analytics: Advanced querying and analysis of performance data.
- Azure Security Center: Correlation of performance metrics with security events.

This integration ensures that performance monitoring for SQL Managed Instance aligns with enterprise-wide monitoring and management strategies within Azure.

**Summary Sentence:**  
The public preview of Microsoft-managed performance monitoring for Azure SQL Managed Instance provides IT professionals with a unified, integrated solution for tracking SQL performance, reducing reliance on custom scripts and external tools, and enhancing visibility into business-critical workloads within the Azure ecosystem.

---


*This report was automatically generated - 2026-11-13 03:02:59 UTC*