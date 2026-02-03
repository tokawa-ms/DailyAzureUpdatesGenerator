# February 03, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 03, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Retirement: Azure Front Door and Azure CDN profiles will end support for DHE cipher suites on April 1, 2026

**Published**: February 02, 2026 18:15:39 UTC
**Link**: [Retirement: Azure Front Door and Azure CDN profiles will end support for DHE cipher suites on April 1, 2026](https://azure.microsoft.com/updates?id=553527)

**Update ID**: 553527
**Data source**: Azure Updates API

**Categories**: Networking, Security, Azure Front Door

**Summary**:

- What was updated  
Azure announced the retirement of support for certain Diffie-Hellman Ephemeral (DHE) cipher suites in Azure Front Door (Standard, Premium, Classic) and Azure CDN from Microsoft (Classic) services, effective April 1, 2026.

- Key changes or new features  
Support for the weak TLS cipher suites TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 and TLS_DHE_RSA_WITH_AES_128_GCM_SHA384 will be discontinued. These cipher suites are considered less secure compared to modern alternatives.

- Target audience affected  
Developers and IT professionals managing applications and services using Azure Front Door and Azure CDN Classic profiles that rely on these DHE cipher suites for TLS encryption.

- Important notes if any  
Customers should review and update their TLS configurations to use stronger cipher suites before the cutoff date to ensure uninterrupted secure connectivity. This change aligns with industry best practices to enhance cryptographic security and mitigate vulnerabilities associated with weak cipher suites. Testing environments should validate compatibility with updated cipher suites ahead of the retirement date.  

Reference: https://azure.microsoft.com/updates?id=553527

**Details**:

The announced retirement of support for the TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 and TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 cipher suites in Azure Front Door (Standard, Premium, Classic) and Azure CDN from Microsoft (Classic) effective April 1, 2026, reflects Microsoft’s proactive security enhancement strategy aimed at deprecating weaker cryptographic algorithms to maintain robust, modern TLS security standards.

**Background and Purpose:**  
This update addresses the security risks associated with the Diffie-Hellman Ephemeral (DHE) cipher suites, which, despite providing forward secrecy, have known vulnerabilities and performance drawbacks compared to newer elliptic-curve-based cipher suites (ECDHE). The move aligns with industry best practices to phase out legacy cryptographic protocols and cipher suites that are susceptible to cryptanalysis or downgrade attacks, thereby enhancing the confidentiality and integrity of TLS connections managed by Azure Front Door and Azure CDN services.

**Specific Features and Detailed Changes:**  
Starting April 1, 2026, Azure Front Door and Azure CDN will no longer negotiate TLS sessions using the specified DHE cipher suites:  
- TLS_DHE_RSA_WITH_AES_256_GCM_SHA384  
- TLS_DHE_RSA_WITH_AES_128_GCM_SHA256  

These cipher suites will be removed from the list of supported TLS cipher suites during the TLS handshake process. Consequently, clients attempting to connect using only these cipher suites will fail to establish a secure connection. The services will continue to support stronger and more efficient cipher suites, primarily those based on Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange mechanisms, such as TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 and TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384.

**Technical Mechanisms and Implementation Methods:**  
Azure Front Door and Azure CDN implement TLS termination at the edge nodes, where the TLS handshake and cipher suite negotiation occur. The update involves modifying the TLS configuration on these edge nodes to exclude the specified DHE cipher suites from the supported cipher suite list. This change is transparent to customers and does not require manual intervention but necessitates that clients and backend services interacting with these endpoints support alternative, stronger cipher suites.

**Use Cases and Application Scenarios:**  
This update primarily affects scenarios where clients or backend services rely on legacy TLS configurations that include DHE cipher suites. For example, enterprises using Azure Front Door for global load balancing and Azure CDN for content delivery must ensure that their client applications, browsers, and backend servers support modern TLS cipher suites to maintain uninterrupted secure connectivity. This is particularly relevant for environments with strict compliance requirements or those exposed to high-security risk profiles.

**Important Considerations and Limitations:**  
- Clients or devices limited to only the deprecated DHE cipher suites will be unable to connect post-retirement, potentially causing service disruptions.  
- Organizations should audit their TLS configurations and client compatibility well in advance of the retirement date to identify and remediate any dependencies on the deprecated cipher suites.  
- Legacy systems or IoT devices with outdated TLS stacks may require updates or replacements.  
- This update does not affect Azure Front Door or Azure CDN features unrelated to TLS cipher suite negotiation.

**Integration with Related Azure Services:**  
Azure Front Door and Azure CDN often integrate with Azure Application Gateway, Azure Web Application Firewall (WAF), and Azure Traffic Manager for comprehensive application delivery and security solutions. Ensuring consistent TLS cipher suite support across these services is critical. For example, Application Gateway’s TLS policies should be aligned with Front Door’s updated cipher suite support to avoid handshake failures in end-to-end TLS scenarios. Additionally, customers leveraging Azure Monitor and Azure Security Center can track TLS-related telemetry and security alerts to proactively manage compliance with this update.

In summary, the planned deprecation of DHE cipher suites in Azure Front Door and Azure CDN by April 1, 2026, is a strategic security enhancement that requires IT professionals to validate and update their TLS

---

### 2. Generally Available: Serverless workspaces in Azure Databricks

**Published**: February 02, 2026 18:15:39 UTC
**Link**: [Generally Available: Serverless workspaces in Azure Databricks](https://azure.microsoft.com/updates?id=550845)

**Update ID**: 550845
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks

**Summary**:

- What was updated  
Azure Databricks now offers Serverless Workspaces as a generally available feature.

- Key changes or new features  
Serverless Workspaces provide a fully managed, SaaS-style environment preconfigured with serverless compute and default storage. This eliminates the need for users to manage infrastructure, enabling faster setup and simplified operations. The serverless compute automatically scales based on workload demands, optimizing performance and cost efficiency. The workspace includes enterprise-grade security and compliance features out of the box.

- Target audience affected  
Developers, data engineers, and IT professionals who use Azure Databricks for big data analytics, machine learning, and data engineering workloads will benefit from simplified management and improved scalability. IT teams gain reduced operational overhead with a fully managed environment.

- Important notes if any  
Serverless Workspaces are designed to streamline deployment and management but may have different pricing and feature considerations compared to traditional Azure Databricks clusters. Users should review the service limits and SLA details to align with their workload requirements. This update supports organizations aiming for a cloud-native, infrastructure-free analytics platform.  

For more details, visit: https://azure.microsoft.com/updates?id=550845

**Details**:

The general availability of serverless workspaces in Azure Databricks introduces a fully managed workspace model designed to simplify and accelerate data analytics and AI workflows by abstracting infrastructure management. Traditionally, Azure Databricks users provision and manage clusters explicitly, which requires capacity planning, cluster configuration, and ongoing maintenance. This update addresses these challenges by offering a serverless compute environment integrated directly into the workspace, enabling users to focus solely on data processing and analytics without managing underlying compute resources.

**Background and Purpose:**  
Azure Databricks has been a leading unified analytics platform combining Apache Spark with Azure’s cloud capabilities. However, managing clusters—scaling, patching, and tuning—can be operationally intensive and requires expertise. The serverless workspace model was introduced to reduce operational overhead, improve agility, and provide an enterprise-grade SaaS experience where compute resources are dynamically allocated and managed by Azure Databricks itself. This aligns with broader cloud trends emphasizing serverless architectures to enhance developer productivity and cost efficiency.

**Specific Features and Changes:**  
- **Preconfigured Serverless Compute:** Serverless workspaces come with built-in serverless compute that automatically scales based on workload demands, eliminating the need for manual cluster provisioning.  
- **Default Storage Integration:** These workspaces include default storage configurations, simplifying data access and management.  
- **Enterprise-Ready SaaS Experience:** The environment is fully managed by Microsoft, including patching, updates, and security compliance, ensuring high availability and reliability.  
- **Zero Infrastructure Management:** Users do not manage VMs, clusters, or autoscaling policies; the platform handles all compute lifecycle operations transparently.  
- **Simplified User Experience:** The workspace interface remains consistent with traditional Azure Databricks, but with reduced configuration complexity.

**Technical Mechanisms and Implementation:**  
Serverless workspaces leverage a multi-tenant, containerized compute architecture abstracted from the user. When a job or interactive session is initiated, the platform dynamically provisions ephemeral compute resources optimized for Apache Spark workloads. This is achieved through integration with Azure’s underlying infrastructure services, such as Azure Kubernetes Service (AKS) for container orchestration and Azure Blob Storage or Azure Data Lake Storage for persistent data storage. The serverless model uses workload-aware autoscaling and resource pooling to optimize performance and cost. Security and compliance are enforced via Azure Active Directory integration, role-based access control (RBAC), and network isolation features.

**Use Cases and Application Scenarios:**  
- **Data Engineering Pipelines:** Automate ETL/ELT processes without managing clusters, improving agility and reducing operational overhead.  
- **Data Science and Machine Learning:** Rapidly prototype and run experiments with scalable compute that adjusts to workload needs.  
- **Business Intelligence and Analytics:** Enable analysts to run ad hoc queries and dashboards with minimal setup.  
- **Event-Driven Processing:** Integrate with Azure Event Hubs or IoT Hub for real-time analytics without pre-provisioning resources.

**Important Considerations and Limitations:**  
- **Workload Suitability:** Serverless workspaces are optimized for typical Spark workloads but may have limitations for highly customized cluster configurations or specialized hardware requirements (e.g., GPU workloads).  
- **Cost Model:** While serverless compute can reduce idle costs, understanding the pricing model is essential as dynamic scaling can lead to variable costs.  
- **Feature Parity:** Some advanced cluster customization features available in traditional workspaces may not be supported in serverless mode.  
- **Data Residency and Compliance:** Ensure that default storage and compute regions comply with organizational data governance policies.

**Integration with Related Azure Services:**  
Serverless workspaces seamlessly integrate with Azure Data Lake Storage Gen2 and Azure Blob Storage for persistent data management. They support Azure Synapse Link for Databricks to enable near real-time analytics. Integration with Azure Active Directory ensures secure authentication and authorization. Additionally, serverless workspaces can connect with Azure Machine Learning for model management and deployment, and with Azure Monitor and Azure

---

### 3. Generally Available: Default Ruleset 2.2 in WAF for Azure Application Gateway

**Published**: February 02, 2026 17:45:01 UTC
**Link**: [Generally Available: Default Ruleset 2.2 in WAF for Azure Application Gateway](https://azure.microsoft.com/updates?id=553532)

**Update ID**: 553532
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Web Application Firewall

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) now generally supports the Default Rule Set (DRS) version 2.2.

- Key changes or new features  
DRS 2.2 enhances protection by updating and refining detection rules against common web vulnerabilities and exploits. It integrates Microsoft Threat Intelligence to improve threat detection accuracy and reduce false positives. The update includes improved handling of modern web application patterns and better coverage of emerging threats.

- Target audience affected  
Developers and IT professionals managing web applications behind Azure Application Gateway WAF will benefit from improved security posture and simplified rule management through this updated default ruleset.

- Important notes if any  
Existing WAF policies using earlier DRS versions can upgrade to 2.2 to leverage enhanced protection. Testing in staging environments is recommended before production rollout to ensure compatibility with application traffic patterns. The update is fully managed by Azure, requiring no manual rule configuration, streamlining ongoing WAF maintenance.  

For detailed information and upgrade guidance, refer to the official Azure update page.

**Details**:

The Azure update announces the general availability of Default Rule Set (DRS) 2.2 for the Web Application Firewall (WAF) on Azure Application Gateway, enhancing the platform’s ability to protect web applications from common vulnerabilities and exploits through an updated, Microsoft-managed rule set.

**Background and Purpose:**  
Azure Application Gateway’s WAF uses managed rule sets to provide centralized, automated protection against OWASP Top 10 vulnerabilities and other web threats. The release of DRS 2.2 reflects ongoing efforts to improve detection accuracy, reduce false positives, and address emerging threats by updating the underlying rule definitions. This update ensures that customers benefit from the latest threat intelligence and security best practices without manual intervention.

**Specific Features and Detailed Changes:**  
DRS 2.2 introduces refined detection logic and new rules that enhance protection against SQL injection, cross-site scripting (XSS), remote file inclusion, and other common attack vectors. It incorporates Microsoft Threat Intelligence to dynamically adjust protections based on current threat landscapes. The update also improves anomaly scoring and rule tuning to minimize false positives, thereby reducing unnecessary blocking of legitimate traffic. Additionally, some deprecated or less effective rules from previous versions have been removed or replaced to optimize performance and accuracy.

**Technical Mechanisms and Implementation Methods:**  
The WAF on Application Gateway operates as a reverse proxy, inspecting inbound HTTP/HTTPS traffic against the managed rule sets. With DRS 2.2, the rule engine uses updated ModSecurity Core Rule Set (CRS) patterns and Microsoft-specific custom rules. These rules are signature and behavior-based, leveraging pattern matching, anomaly scoring, and heuristic analysis to detect malicious payloads. The update is applied seamlessly by Azure as part of the platform’s managed service model, requiring no manual rule updates from customers. Administrators can enable or disable specific rules or rule groups via WAF policy configurations to tailor protection based on application needs.

**Use Cases and Application Scenarios:**  
DRS 2.2 is ideal for organizations deploying web applications behind Azure Application Gateway that require robust, continuously updated protection against evolving web threats. It is particularly beneficial for scenarios involving sensitive data processing, compliance requirements (e.g., PCI DSS, HIPAA), or high-traffic public-facing websites where security and uptime are critical. By leveraging DRS 2.2, IT teams can reduce the operational overhead of manual rule management while maintaining strong defense against injection attacks, cross-site scripting, and other OWASP Top 10 threats.

**Important Considerations and Limitations:**  
While DRS 2.2 improves detection and reduces false positives, tuning may still be necessary to align with specific application behaviors and avoid blocking legitimate requests. Some complex or zero-day attacks may require additional custom rules or integration with Azure Sentinel for advanced threat detection. The update applies only to WAF v2 SKU on Application Gateway; legacy WAF versions or other WAF solutions require separate updates. Performance impact is minimal but should be monitored in high-throughput environments. Customers should review the updated rule set documentation and test in staging environments before production deployment.

**Integration with Related Azure Services:**  
DRS 2.2 integrates seamlessly with Azure Application Gateway’s WAF v2, benefiting from Azure’s global infrastructure and autoscaling capabilities. It complements Azure Security Center recommendations and can feed logs into Azure Monitor and Azure Sentinel for centralized security analytics and incident response. Combined with Azure Front Door or Azure CDN, it provides layered security for distributed web applications. The managed rule set update aligns with Azure’s security posture management, enabling automated compliance and threat mitigation workflows.

In summary, the general availability of Default Rule Set 2.2 for Azure Application Gateway WAF delivers enhanced, Microsoft-managed protection against web vulnerabilities through updated detection rules, improved accuracy, and integration with Azure’s security ecosystem, enabling IT professionals to secure web applications effectively with minimal operational overhead.

---


*This report was automatically generated - 2026-02-03 03:02:16 UTC*