# August 25, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: August 25, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Announcing: Extended Support for Azure Database for PostgreSQL Flexible Server 

**Published**: August 24, 2026 19:15:05 UTC
**Link**: [Announcing: Extended Support for Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=569526)

**Update ID**: 569526
**Data source**: Azure Updates API

**Categories**: Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Announcement

**Summary**:

- What was updated  
Microsoft announced Extended Support for Azure Database for PostgreSQL Flexible Server.

- Key changes or new features  
Extended Support provides continued access to critical security updates, bug fixes, and technical support for PostgreSQL versions that have reached end-of-life (EOL). This enables customers to maintain secure and supported workloads while planning and executing upgrades to newer PostgreSQL versions. The Extended Support option helps minimize disruption and risk during migration and ensures compliance and security for legacy PostgreSQL deployments.

- Target audience affected  
Developers and IT professionals managing Azure Database for PostgreSQL Flexible Server instances, especially those running workloads on PostgreSQL versions approaching or past EOL.

- Important notes if any  
Extended Support is a paid offering and is intended as a temporary solution to facilitate migration to newer PostgreSQL versions. Customers are encouraged to upgrade to supported versions as soon as possible to benefit from full feature updates and long-term support. Extended Support ensures continued security and reliability but does not include new feature enhancements for legacy versions. For more details, visit the official Azure Update announcement.

**Details**:

**Azure Update Report: Extended Support for Azure Database for PostgreSQL Flexible Server**

**Background and Purpose of the Update**  
The Extended Support for Azure Database for PostgreSQL Flexible Server is introduced to assist organizations in maintaining secure and supported PostgreSQL workloads during their transition to newer PostgreSQL versions. This update addresses the challenge of managing legacy PostgreSQL deployments that may not be immediately upgraded, ensuring continued operational security and compliance.

**Specific Features and Detailed Changes**  
The Extended Support offering includes the following key features:
- **Critical Security Updates:** Ongoing delivery of security patches to mitigate vulnerabilities in supported PostgreSQL versions.
- **Critical Bug Fixes:** Resolution of major issues that could impact database stability or data integrity.
- **Technical Support:** Access to Azure technical support for troubleshooting and guidance related to PostgreSQL Flexible Server during the extended support period.

These features are specifically designed to cover PostgreSQL versions that have reached their end-of-life (EOL) according to community standards but are still in use within Azure Database for PostgreSQL Flexible Server.

**Technical Mechanisms and Implementation Methods**  
Extended Support is implemented as an additional service layer within the Azure Database for PostgreSQL Flexible Server platform. Azure engineers curate and apply security patches and critical bug fixes directly to the managed PostgreSQL instances. Customers do not need to manually apply these updates; instead, updates are seamlessly integrated into the managed service lifecycle. Technical support is provided through standard Azure support channels, ensuring continuity of assistance for extended support workloads.

**Use Cases and Application Scenarios**  
- **Regulated Industries:** Organizations in finance, healthcare, or government sectors that require strict security and compliance, but cannot immediately upgrade their PostgreSQL versions due to application dependencies.
- **Legacy Application Support:** Enterprises running legacy applications that depend on specific PostgreSQL versions, enabling them to maintain operational continuity while planning migration strategies.
- **Transition Planning:** Businesses that need additional time to test and validate newer PostgreSQL versions before performing upgrades in production environments.

**Important Considerations and Limitations**  
- **Scope of Support:** Extended Support is limited to critical security updates, critical bug fixes, and technical support. It does not include feature enhancements or non-critical bug fixes.
- **Version Eligibility:** Only specific PostgreSQL versions that have reached EOL are eligible for Extended Support within Azure Database for PostgreSQL Flexible Server.
- **Migration Planning:** Extended Support is intended as a temporary measure. Customers are encouraged to plan and execute migrations to newer PostgreSQL versions to benefit from full support and new features.
- **Cost Implications:** Extended Support may incur additional charges; customers should review Azure pricing documentation for details.

**Integration with Related Azure Services**  
Extended Support is fully integrated with Azure Database for PostgreSQL Flexible Server, leveraging Azure’s managed database infrastructure. It works seamlessly with Azure security, monitoring, and backup services, ensuring that extended support workloads continue to benefit from Azure’s operational capabilities. Customers can use Azure Resource Manager, Azure Monitor, and other native tools to manage and observe their PostgreSQL instances under Extended Support.

**Summary Sentence**  
Azure Database for PostgreSQL Flexible Server now offers Extended Support, providing critical security updates, bug fixes, and technical support for workloads running on legacy PostgreSQL versions, enabling secure and compliant operations during migration to newer versions.

---

### 2. Generally Available: eBPF host routing in Advanced Container Networking Services for AKS

**Published**: August 24, 2026 18:36:01 UTC
**Link**: [Generally Available: eBPF host routing in Advanced Container Networking Services for AKS](https://azure.microsoft.com/updates?id=569873)

**Update ID**: 569873
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Azure Kubernetes Service (AKS), Features, Microsoft Build, Services

**Summary**:

- What was updated  
eBPF Host Routing is now generally available in Advanced Container Networking Services for Azure Kubernetes Service (AKS).

- Key changes or new features  
This update leverages eBPF (extended Berkeley Packet Filter) technology to optimize host routing within AKS clusters. Packet forwarding and routing decisions are now handled directly in the Linux kernel, reducing overhead and improving network performance. This enhancement enables faster pod-to-pod communication, lower latency, and increased throughput for containerized workloads.

- Target audience affected  
Developers and IT professionals managing AKS clusters, especially those deploying large-scale or performance-sensitive applications, will benefit from these improvements. Networking and DevOps teams responsible for cluster configuration and optimization are particularly impacted.

- Important notes if any  
To take advantage of eBPF Host Routing, clusters must use Advanced Container Networking Services. Existing AKS clusters may require configuration updates to enable this feature. The update is compatible with Linux-based nodes and may not be available for Windows nodes. For further details and implementation guidance, refer to the official Azure documentation.  
Link: https://azure.microsoft.com/updates?id=569873

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: eBPF host routing in Advanced Container Networking Services for AKS  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=569873)

---

**Background and Purpose of the Update**  
The general availability of eBPF Host Routing in Advanced Container Networking Services for Azure Kubernetes Service (AKS) addresses the need for improved Kubernetes networking performance. Traditionally, packet forwarding and routing decisions in AKS environments rely on kernel-level mechanisms that can introduce latency and limit scalability. The purpose of this update is to leverage eBPF (extended Berkeley Packet Filter) technology to optimize these operations, thereby enhancing the efficiency and speed of network traffic management within AKS clusters.

---

**Specific Features and Detailed Changes**  
This update introduces eBPF Host Routing as a feature within Advanced Container Networking Services for AKS. The key change is the migration of packet forwarding and routing logic from conventional kernel space into the Linux kernel via eBPF programs. This enables direct, programmable control over network packets at the host level, reducing the overhead associated with traditional routing tables and network stack processing.

---

**Technical Mechanisms and Implementation Methods**  
eBPF is a powerful Linux kernel technology that allows safe, efficient execution of custom code in response to network events. With eBPF Host Routing, AKS nodes utilize eBPF programs to make routing and forwarding decisions directly within the kernel. This bypasses the need for user-space processing and minimizes context switches, resulting in lower latency and higher throughput. The implementation is tightly integrated with the Advanced Container Networking Services, ensuring compatibility and seamless operation within AKS environments.

---

**Use Cases and Application Scenarios**  
- **High-Performance Microservices:** Applications requiring low-latency, high-throughput communication between containers benefit from eBPF Host Routing, as it streamlines network operations.
- **Large-Scale AKS Deployments:** Clusters with significant east-west traffic (pod-to-pod communication) will see improved performance due to reduced packet processing overhead.
- **Network-Intensive Workloads:** Scenarios such as real-time analytics, financial trading platforms, and gaming backends can leverage the enhanced networking capabilities for better responsiveness.

---

**Important Considerations and Limitations**  
- **Kernel Compatibility:** eBPF relies on specific Linux kernel versions and capabilities; ensure AKS nodes are running supported kernels.
- **Operational Monitoring:** While eBPF improves performance, monitoring and debugging may require updated tools compatible with eBPF-based routing.
- **Feature Scope:** This update is specific to Advanced Container Networking Services; standard AKS networking may not benefit unless explicitly configured.

---

**Integration with Related Azure Services**  
eBPF Host Routing is designed to work seamlessly within AKS clusters that utilize Advanced Container Networking Services. It complements Azure’s existing networking stack, including Azure Virtual Network integration, and can be used alongside other Azure networking features such as network policies and service meshes. The feature is managed through AKS configuration, ensuring consistent deployment and lifecycle management within Azure environments.

---

**Summary Sentence**  
eBPF Host Routing is now generally available in Advanced Container Networking Services for AKS, providing improved Kubernetes networking performance by moving packet forwarding and routing decisions directly into the Linux kernel.

---

### 3. Retirement: Support for Node 22 LTS ends on April 30, 2027

**Published**: August 24, 2026 17:30:43 UTC
**Link**: [Retirement: Support for Node 22 LTS ends on April 30, 2027](https://azure.microsoft.com/updates?id=567334)

**Update ID**: 567334
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements

**Summary**:

- What was updated  
Azure announced the retirement of support for Node.js 22 LTS on App Service, effective April 30, 2027.

- Key changes or new features  
After April 30, 2027, Node.js 22 LTS will no longer receive security updates or customer support on Azure App Service. Applications using this runtime will continue to operate, but will be exposed to potential security risks due to lack of updates.

- Target audience affected  
Developers and IT professionals managing applications on Azure App Service that use Node.js 22 LTS.

- Important notes if any  
To maintain security and support, you must upgrade your applications to a newer, supported Node.js LTS version before the retirement date. Failure to do so may result in unsupported and potentially vulnerable applications. Review your application dependencies and plan migration accordingly to avoid disruptions and ensure compliance with Azure's support policies.

**Details**:

**Azure Update Report: Retirement of Node 22 LTS Support on App Service (Effective April 30, 2027)**

---

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of support for Node 22 LTS (Long-Term Support) on App Service, effective April 30, 2027. This update is part of Azure’s lifecycle management policy, which ensures that platform-supported runtimes remain current and secure. The purpose is to notify customers that, after the specified date, Node 22 LTS will no longer receive security updates or customer support on Azure App Service.

**Specific Features and Detailed Changes**  
- **End of Support Date:** April 30, 2027.
- **Affected Runtime:** Node 22 LTS.
- **Platform Impact:** Applications hosted on Azure App Service using Node 22 LTS.
- **Post-Retirement Behavior:** Applications will continue to run, but:
  - No further security patches or bug fixes will be provided for Node 22 LTS.
  - Azure customer support will not be available for issues related to Node 22 LTS.

**Technical Mechanisms and Implementation Methods**  
Azure App Service manages runtime versions through its platform image updates. When a runtime version reaches end-of-support, Azure stops updating the platform images with new patches for that version. The retirement process involves:
- Discontinuation of automated security updates for Node 22 LTS.
- Removal of Node 22 LTS from supported runtime lists in App Service configuration options.
- Customer support teams will no longer address tickets related to Node 22 LTS after the retirement date.

**Use Cases and Application Scenarios**  
This update directly affects:
- Web applications, APIs, and backend services deployed on Azure App Service using Node 22 LTS.
- Organizations relying on Node 22 LTS for production workloads, CI/CD pipelines, or development environments hosted on App Service.

**Important Considerations and Limitations**  
- **Security Risks:** Continuing to use Node 22 LTS after April 30, 2027 exposes applications to potential vulnerabilities, as no new security patches will be provided.
- **Support Limitations:** Azure will not offer troubleshooting or assistance for Node 22 LTS-related issues post-retirement.
- **Migration Requirement:** Customers are advised to plan migration to a newer, supported Node LTS version before the retirement date to maintain security and support.
- **Operational Continuity:** Applications will not be forcibly stopped or removed; however, lack of updates and support may impact reliability and compliance.

**Integration with Related Azure Services**  
- **Azure App Service:** The runtime retirement affects all App Service plans (Windows and Linux) using Node 22 LTS.
- **DevOps Pipelines:** CI/CD workflows deploying Node 22 LTS applications to App Service should be updated to target a supported Node version.
- **Monitoring and Security:** Azure Monitor and Security Center will continue to monitor applications, but flagged vulnerabilities in Node 22 LTS will not be resolved by Azure.
- **Application Gateway, Azure Functions, and Logic Apps:** If these services depend on Node 22 LTS hosted on App Service, migration plans should be coordinated across all dependent components.

---

**Summary Sentence:**  
Support for Node 22 LTS on Azure App Service will end on April 30, 2027; after this date, applications will continue running but will no longer receive security updates or customer support, requiring customers to migrate to a newer Node version to maintain security and support.

---

### 4. Generally Available: Custom block response code and body for Application Gateway WAF 

**Published**: August 24, 2026 17:25:03 UTC
**Link**: [Generally Available: Custom block response code and body for Application Gateway WAF ](https://azure.microsoft.com/updates?id=569504)

**Update ID**: 569504
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Web Application Firewall, Feature

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) now supports custom block response codes and bodies for blocked requests. This feature is generally available.

- Key changes or new features  
Developers and IT professionals can configure the WAF to return specific HTTP status codes and custom response bodies when requests are blocked. Previously, WAF only returned a default 403 status code and a generic response. Now, users can tailor the error code (e.g., 403, 404, 429, etc.) and provide a custom message or JSON body, improving client experience and integration with applications.

- Target audience affected  
This update is relevant for developers, DevOps teams, and IT professionals managing web applications behind Azure Application Gateway WAF, especially those requiring custom error handling or enhanced client communication when blocking malicious or unwanted traffic.

- Important notes if any  
Custom block responses can help improve user experience, provide clearer messaging, and support integration scenarios (such as API clients expecting specific error codes). Configuration is available via Azure Portal, ARM templates, and REST API. Review documentation for implementation details and potential impacts on application behavior.

**Details**:

**Azure Update Report: Custom Block Response Code and Body for Application Gateway WAF (General Availability)**

**Background and Purpose of the Update:**  
Azure Application Gateway Web Application Firewall (WAF) is a critical component for securing web applications against common threats and vulnerabilities. Traditionally, when WAF blocks a request, it returns a default HTTP response code and body, which may not align with customer requirements for user experience, compliance, or integration with downstream systems. The purpose of this update is to provide IT professionals with greater control over the response sent to clients when a request is blocked, thereby enhancing flexibility, user feedback, and compliance capabilities.

**Specific Features and Detailed Changes:**  
With this update, Azure Application Gateway WAF now supports the configuration of custom HTTP response status codes and response bodies for blocked requests. This means administrators can define both the numeric status code (such as 403, 404, or 429) and the content of the response body (such as a custom error message or JSON object) that is returned when WAF blocks a request. This feature is generally available and can be configured via the Azure portal, ARM templates, or REST API.

**Technical Mechanisms and Implementation Methods:**  
The implementation involves new configuration options within the Application Gateway WAF policy. Administrators can specify:
- The HTTP status code to be returned for blocked requests.
- The response body content, which can be plain text, HTML, or JSON, depending on requirements.

These settings are applied at the WAF policy level and are enforced whenever a request is blocked based on WAF rules. The custom response is generated by the Application Gateway and sent directly to the client, replacing the default block response.

**Use Cases and Application Scenarios:**  
- **User Experience:** Organizations can provide clear, branded error messages to users when their requests are blocked, improving transparency and reducing confusion.
- **Compliance:** Custom responses can include specific information required for regulatory compliance, such as contact details or incident tracking codes.
- **Integration:** Custom status codes and bodies can be used to trigger specific actions in client applications or downstream monitoring systems, such as logging or alerting.
- **Localization:** Responses can be tailored to different languages or regions, supporting global applications.

**Important Considerations and Limitations:**  
- The custom response applies only to requests blocked by WAF rules; it does not affect other types of Application Gateway responses.
- Care must be taken to avoid exposing sensitive information in custom response bodies.
- There may be limits on the size and format of the response body; refer to Azure documentation for specifics.
- Custom responses should be tested to ensure they do not inadvertently interfere with legitimate client behavior or application workflows.

**Integration with Related Azure Services:**  
This feature is integrated directly into Application Gateway WAF policies and works seamlessly with existing Application Gateway deployments. It complements other Azure security services, such as Azure Front Door and Azure Security Center, by providing enhanced customization for web application protection. Configuration can be managed via Azure Resource Manager (ARM), Azure CLI, and Azure portal, enabling automation and integration with DevOps workflows.

**Summary Sentence:**  
Azure Application Gateway WAF now generally supports customizable block response codes and bodies, enabling IT professionals to tailor blocked request responses for improved user experience, compliance, and integration with client applications.

---


*This report was automatically generated - 2026-08-25 03:02:54 UTC*