# March 18, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 18, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Default Rule Set 2.2 and updates to ruleset support policy

**Published**: March 17, 2026 17:45:45 UTC
**Link**: [Generally Available: Default Rule Set 2.2 and updates to ruleset support policy](https://azure.microsoft.com/updates?id=558016)

**Update ID**: 558016
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Application Gateway, Azure Front Door, Web Application Firewall, Features

**Summary**:

- What was updated  
Azure Web Application Firewall (WAF) has announced the general availability of Default Rule Set (DRS) 2.2 on Azure Application Gateway and Azure Front Door. Additionally, the managed ruleset support policy has been updated.

- Key changes or new features  
  - DRS 2.2 introduces enhanced security rules for better protection against web vulnerabilities and threats.  
  - The managed ruleset support policy is now clearer and more predictable, outlining how long each ruleset version will be supported.  
  - Customers can plan upgrades and security posture improvements with more confidence, knowing the lifecycle of each ruleset.

- Target audience affected  
  - Developers and IT professionals managing web applications on Azure Application Gateway or Azure Front Door using WAF.  
  - Security teams responsible for web application protection and compliance.

- Important notes if any  
  - It is recommended to review and migrate to DRS 2.2 to benefit from the latest security enhancements and ensure ongoing support.  
  - Review the updated ruleset support policy to align your application security strategy and maintenance schedules.  
  - Existing deployments using older DRS versions should plan for future upgrades based on the new support timelines.

For more details, see the official update: https://azure.microsoft.com/updates?id=558016

**Details**:

**Comprehensive Technical Explanation: Azure Web Application Firewall (WAF) Default Rule Set 2.2 General Availability and Ruleset Support Policy Update**

**Background and Purpose of the Update:**  
The Azure Web Application Firewall (WAF) is a critical security component for protecting web applications from common threats and vulnerabilities. The release of Default Rule Set (DRS) 2.2 marks its general availability on both Azure Application Gateway and Azure Front Door. Alongside this, Microsoft is updating the managed ruleset support policy. The primary purpose of this update is to provide a clearer and more predictable framework for ruleset support, ensuring that organizations can plan their security posture with greater confidence and transparency.

**Specific Features and Detailed Changes:**  
- **General Availability of DRS 2.2:** The Default Rule Set 2.2 is now generally available for use with Azure Application Gateway and Azure Front Door. This means it is production-ready and fully supported by Microsoft.
- **Updated Ruleset Support Policy:** The managed ruleset support policy has been revised to clarify support timelines and provide predictability regarding the lifecycle of rulesets. This update helps customers understand how long each ruleset version will be supported and when deprecation or end-of-support will occur.

**Technical Mechanisms and Implementation Methods:**  
- **Deployment:** DRS 2.2 can be enabled and configured through the Azure Portal, ARM templates, or automation tools such as Azure CLI and PowerShell. It is applied at the WAF policy level, which is then associated with Application Gateway or Front Door resources.
- **Policy Enforcement:** The managed ruleset policy update ensures that the latest security rules are enforced consistently across environments. The ruleset is maintained and updated by Microsoft, reducing the operational burden on IT teams.

**Use Cases and Application Scenarios:**  
- **Web Application Protection:** Organizations deploying web applications on Azure Application Gateway or Azure Front Door can leverage DRS 2.2 to protect against OWASP Top 10 threats and other common web vulnerabilities.
- **Regulatory Compliance:** The clarified ruleset support policy assists organizations in meeting compliance requirements by ensuring that their security controls are up-to-date and supported.
- **Operational Predictability:** IT teams can plan upgrades and maintenance activities with greater certainty due to the predictable ruleset lifecycle.

**Important Considerations and Limitations:**  
- **Ruleset Selection:** Customers must ensure that their WAF policies are updated to use DRS 2.2 to benefit from the latest protections and support policy.
- **Lifecycle Management:** It is important to monitor the support timelines for each ruleset version and plan migrations accordingly to avoid running unsupported configurations.
- **Compatibility:** Before enabling DRS 2.2, organizations should test their applications for compatibility with the new ruleset to prevent false positives or unintended blocking of legitimate traffic.

**Integration with Related Azure Services:**  
- **Azure Application Gateway and Azure Front Door:** DRS 2.2 is directly integrated with these services, allowing seamless application-layer protection.
- **Azure Security Center:** WAF logs and alerts generated by DRS 2.2 can be ingested into Azure Security Center for centralized monitoring and incident response.
- **Automation and DevOps:** The ruleset can be managed programmatically via ARM templates, Azure CLI, and PowerShell, supporting infrastructure-as-code and DevOps workflows.

**Summary:**  
The general availability of Default Rule Set 2.2 and the updated managed ruleset support policy for Azure Web Application Firewall provide enhanced security, clearer lifecycle management, and improved operational predictability for organizations using Azure Application Gateway and Azure Front Door.

---

### 2. Generally Available: Foundry Agent Service

**Published**: March 17, 2026 17:45:45 UTC
**Link**: [Generally Available: Foundry Agent Service](https://azure.microsoft.com/updates?id=557141)

**Update ID**: 557141
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Microsoft Foundry, Features

**Summary**:

- What was updated  
The Foundry Agent Service is now generally available (GA) on Azure. This release introduces a redesigned API format and enhanced runtime experience for building and managing agents.

- Key changes or new features  
  - Redesigned API format for improved usability and integration.
  - Enhanced runtime environment for more reliable agent deployment and operations.
  - Focus on supporting the full lifecycle of agents, from prototyping to production.
  - Improved tools and documentation to help teams transition agents into production environments confidently.

- Target audience affected  
Developers and IT professionals building, deploying, or managing agent-based solutions on Azure, especially those moving from proof-of-concept to production.

- Important notes if any  
  - Existing prototypes may require updates to align with the new API format.
  - The GA release ensures production-level support and stability.
  - Teams are encouraged to review the updated documentation and migration guidance to leverage the new features and runtime improvements.

For more details, refer to the official [Azure Update](https://azure.microsoft.com/updates?id=557141).

**Details**:

**Azure Update Technical Report: Generally Available – Foundry Agent Service**

**Background and Purpose of the Update:**  
The Foundry Agent Service has reached General Availability (GA), marking its transition from preview to a fully supported Azure service. This update introduces a next-generation platform specifically designed to help teams efficiently build, deploy, and manage agents. The primary goal is to enable seamless movement from prototyping to production, ensuring reliability and scalability for agent-based solutions.

**Specific Features and Detailed Changes:**  
- **Redesigned API Format:** The Foundry Agent Service now offers a restructured API, providing a more robust and developer-friendly interface for interacting with agents. This redesign aims to simplify integration and enhance consistency across agent operations.
- **Enhanced Runtime Experience:** The service delivers an improved runtime environment, optimizing the execution and lifecycle management of agents. This includes better support for deployment, monitoring, and operational control.
- **Production-Readiness:** With GA, the service is now fully supported by Azure, including SLA-backed reliability, support channels, and compliance with Azure’s security and operational standards.

**Technical Mechanisms and Implementation Methods:**  
- **API-Driven Architecture:** The Foundry Agent Service leverages a modern API-driven approach, allowing developers to programmatically manage agent lifecycles, configurations, and interactions.
- **Runtime Environment:** The service provides a managed runtime that abstracts infrastructure complexities, enabling teams to focus on agent logic rather than underlying resource management.
- **Operational Tooling:** Integrated monitoring and diagnostics tools are available to track agent performance and health, facilitating rapid troubleshooting and continuous improvement.

**Use Cases and Application Scenarios:**  
- **Prototyping to Production:** Teams can use the Foundry Agent Service to quickly prototype agent-based solutions and seamlessly transition them to production without re-architecting.
- **Automated Workflows:** The service is suitable for scenarios requiring autonomous agents, such as process automation, data collection, or intelligent orchestration within enterprise environments.
- **Scalable Agent Management:** Organizations can manage large fleets of agents across distributed environments, leveraging Azure’s scalability and reliability.

**Important Considerations and Limitations:**  
- **GA Support:** With the service now generally available, users benefit from Azure’s full support model, but must ensure their solutions comply with any updated operational or security guidelines.
- **API Changes:** Teams migrating from earlier versions or previews should review the redesigned API format to accommodate any breaking changes or new integration patterns.
- **Runtime Dependencies:** While the managed runtime simplifies deployment, teams should validate compatibility with their existing agent codebases and operational requirements.

**Integration with Related Azure Services:**  
- **Azure Monitoring and Diagnostics:** The Foundry Agent Service integrates with Azure’s monitoring tools, enabling unified observability across agent deployments.
- **Security and Compliance:** The service adheres to Azure’s security standards, facilitating integration with Azure Active Directory and other identity management solutions.
- **Ecosystem Compatibility:** Foundry Agent Service can be used alongside other Azure services (e.g., Azure Functions, Logic Apps) to build comprehensive, agent-driven workflows.

**Summary Sentence:**  
The Foundry Agent Service is now generally available, offering a redesigned API and enhanced runtime to help teams confidently build, operate, and scale agent-based solutions from prototype to production within the Azure ecosystem.

---

### 3. Retirement: Azure VMware Solution AV36P and AV52 node retirement on June 30, 2029

**Published**: March 17, 2026 17:30:11 UTC
**Link**: [Retirement: Azure VMware Solution AV36P and AV52 node retirement on June 30, 2029](https://azure.microsoft.com/updates?id=557094)

**Update ID**: 557094
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Azure VMware Solution (AVS) AV36P and AV52 node types, effective June 30, 2029.

- Key changes or new features  
The AV36P and AV52 node types will no longer be available for provisioning after June 30, 2029. Existing Reserved Instances (RIs) for these node types will remain valid until their expiration, and current terms are not impacted by this announcement.

- Target audience affected  
This update affects IT professionals and developers managing Azure VMware Solution environments, particularly those utilizing AV36P or AV52 nodes, and those responsible for capacity planning, infrastructure lifecycle management, and RI purchasing.

- Important notes if any  
Customers should review the expiration dates of their current AV36P and AV52 RIs and plan migrations or transitions to supported node types before the retirement date. No immediate action is required, but early planning is recommended to avoid service disruption. Microsoft will provide further guidance as the retirement date approaches.

For more details, visit the official [Azure Update](https://azure.microsoft.com/updates?id=557094).

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Azure VMware Solution AV36P and AV52 node retirement on June 30, 2029  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=557094)

---

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of the AV36P and AV52 node types within the Azure VMware Solution (AVS) platform, effective June 30, 2029. This update is part of Microsoft’s ongoing lifecycle management for Azure infrastructure components, ensuring that customers are informed well in advance about the deprecation of specific node SKUs. The purpose is to provide customers with ample time to plan for migration or transition strategies, minimizing disruption to workloads running on these node types.

**Specific Features and Detailed Changes:**  
The AV36P and AV52 nodes are specific compute SKUs offered in Azure VMware Solution, designed to provide dedicated VMware infrastructure on Azure. The retirement announcement means that after June 30, 2029, these node types will no longer be available for provisioning or renewal. Existing Reserved Instances (RI) for AV36P and AV52 nodes will continue to operate as per their current terms and are not affected by this announcement until their expiration. Customers are advised to review their RI expiration dates and plan accordingly for future capacity needs.

**Technical Mechanisms and Implementation Methods:**  
The retirement process will be managed through Azure’s standard lifecycle management procedures. After the retirement date, the Azure portal and APIs will no longer permit the creation or extension of AV36P and AV52 nodes. Existing nodes will continue to function until the end of their RI term, after which customers will need to migrate workloads to supported node types. Microsoft will provide tools and guidance for migration to newer node SKUs within the Azure VMware Solution platform, ensuring compatibility and continuity of service.

**Use Cases and Application Scenarios:**  
AV36P and AV52 nodes are typically used by enterprises running VMware workloads in Azure, leveraging dedicated infrastructure for high-performance, scalable, and secure virtualization. Common scenarios include datacenter extension, disaster recovery, and cloud migration of VMware-based applications. The retirement impacts customers who have standardized on these node types for their AVS deployments and will require them to evaluate alternative node SKUs for future workloads.

**Important Considerations and Limitations:**  
- The retirement does not affect the terms of current AV36P and AV52 Reserved Instances; they will remain operational until expiration.
- After June 30, 2029, new deployments or renewals of AV36P and AV52 nodes will not be possible.
- Customers must plan for migration to supported node types prior to the retirement date to avoid service disruption.
- It is recommended to review current RI expiration dates and assess migration strategies well in advance.

**Integration with Related Azure Services:**  
Azure VMware Solution integrates with a broad range of Azure services, including Azure networking, storage, and security solutions. The retirement of AV36P and AV52 nodes may require customers to update their integration points, such as reconfiguring network connectivity or adjusting storage mappings, when migrating to new node types. Microsoft will continue to support AVS integration with other Azure services, ensuring that customers can maintain seamless operations during and after migration.

---

**Summary Sentence:**  
Microsoft will retire the AV36P and AV52 node types in Azure VMware Solution on June 30, 2029, and recommends customers review their Reserved Instance expiration dates and plan for migration to supported node SKUs to ensure uninterrupted service.

---


*This report was automatically generated - 2026-03-18 03:02:33 UTC*