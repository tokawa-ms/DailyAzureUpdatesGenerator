# September 23, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 23, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Support for Node.js 22 ends on April 30, 2027

**Published**: September 22, 2026 19:22:34 UTC
**Link**: [Retirement: Support for Node.js 22 ends on April 30, 2027](https://azure.microsoft.com/updates?id=572771)

**Update ID**: 572771
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Internet of Things, Azure Functions, Retirements, Compliance, Security

**Summary**:

- What was updated  
Azure announced the retirement of support for Node.js 22 in Azure Functions.

- Key changes or new features  
Support for Node.js 22 in Azure Functions will end on April 30, 2027. After this date, security patches, updates, and customer support for Node.js 22 will no longer be available. Users are advised to transition their Azure Function apps to Node.js 24 before the retirement date to ensure continued support and security.

- Target audience affected  
Developers and IT professionals maintaining Azure Function apps that currently use Node.js 22.

- Important notes if any  
Existing Function apps using Node.js 22 will continue to run after April 30, 2027, but without security updates or customer support, which could expose applications to vulnerabilities and compliance risks. It is strongly recommended to plan and execute migration to Node.js 24 ahead of the retirement date to maintain supportability and security. Review your application dependencies and test thoroughly after upgrading to Node.js 24 to avoid runtime issues.

For more details, refer to the official Azure update: https://azure.microsoft.com/updates?id=572771

**Details**:

**Azure Update Report: Retirement of Node.js 22 Support on April 30, 2027**

**Background and Purpose of the Update**  
Microsoft Azure has announced the retirement of support for Node.js 22 on April 30, 2027. This update aligns with Azure’s lifecycle management policies, ensuring that customers are using supported, secure, and up-to-date runtime environments. The primary purpose is to encourage migration to Node.js 24, which will continue to receive security patches, updates, and customer support after Node.js 22 reaches end-of-support.

**Specific Features and Detailed Changes**  
The key change is the discontinuation of security patches, updates, and customer support for Node.js 22 in Azure Function apps after the specified date. While existing Azure Function apps running Node.js 22 will not be forcibly stopped, they will no longer benefit from ongoing maintenance or technical assistance. Customers are advised to transition their workloads to Node.js 24 to maintain compliance and security.

**Technical Mechanisms and Implementation Methods**  
Azure Functions provides runtime support for various Node.js versions. The retirement process involves removing Node.js 22 from the list of supported runtimes in Azure Functions. After April 30, 2027, Azure will not release further updates or security patches for Node.js 22, and customer support requests related to this version will be declined. Migration to Node.js 24 typically involves updating the runtime configuration in the Azure Function app settings (e.g., `FUNCTIONS_WORKER_RUNTIME` and `WEBSITE_NODE_DEFAULT_VERSION`) and validating application compatibility with the newer Node.js version.

**Use Cases and Application Scenarios**  
This update primarily impacts organizations running serverless workloads using Azure Functions with Node.js 22. Typical scenarios include API backends, event-driven processing, and automation tasks. IT professionals managing these workloads must plan for migration to Node.js 24 to ensure continued support and security. The transition is relevant for both production and development environments, as unsupported runtimes expose applications to potential vulnerabilities and compliance risks.

**Important Considerations and Limitations**  
- **Security Risks:** Continuing to run Node.js 22 after its retirement exposes applications to unpatched vulnerabilities.
- **Support Limitations:** Azure customer support will not assist with issues related to Node.js 22 post-retirement.
- **Migration Requirements:** Application code may require updates to accommodate breaking changes or new features in Node.js 24.
- **No Forced Shutdown:** Azure Function apps using Node.js 22 will not be automatically stopped, but lack of updates and support may impact reliability and compliance.

**Integration with Related Azure Services**  
Azure Functions is tightly integrated with other Azure services such as Azure Logic Apps, Azure Event Grid, and Azure Storage. Migrating to Node.js 24 ensures seamless interoperability with these services, as they rely on supported runtimes for secure and reliable operation. Updating the Node.js runtime in Azure Functions is a straightforward process and does not disrupt integration with other Azure services, provided application dependencies are compatible with Node.js 24.

**Summary Sentence**  
Support for Node.js 22 in Azure Function apps will end on April 30, 2027; customers should migrate to Node.js 24 to maintain security, updates, and customer support, as applications running Node.js 22 will continue to operate but without further maintenance or assistance.

---

### 2. Public Preview: Flex Nodes for AKS

**Published**: September 22, 2026 18:51:48 UTC
**Link**: [Public Preview: Flex Nodes for AKS](https://azure.microsoft.com/updates?id=571919)

**Update ID**: 571919
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Azure Kubernetes Service (AKS), Feature

**Summary**:

- What was updated  
Public Preview of Flex Nodes for Azure Kubernetes Service (AKS).

- Key changes or new features  
Flex Nodes introduce a new deployment option allowing hybrid and edge infrastructure to function as connected worker nodes managed by the AKS control plane in Azure. This enables organizations to run Kubernetes workloads on-premises or at the edge while maintaining a consistent, cloud-managed Kubernetes control plane. Flex Nodes support seamless integration with Azure management, security, and monitoring features, and facilitate workload portability across cloud, hybrid, and edge environments.

- Target audience affected  
Developers and IT professionals managing Kubernetes workloads across hybrid or edge environments, especially those seeking unified management and deployment using AKS.

- Important notes if any  
Flex Nodes are currently in public preview and may not be suitable for production workloads. This feature is ideal for scenarios requiring consistent Kubernetes management across diverse infrastructure, such as retail, manufacturing, or remote locations. Teams should review documentation for supported configurations and limitations during the preview phase.

Data source: Using API data  
More information: [Azure Update: Flex Nodes for AKS](https://azure.microsoft.com/updates?id=571919)

**Details**:

**Background and Purpose of the Update**  
The introduction of Flex Nodes for Azure Kubernetes Service (AKS) in Public Preview aims to address the need for application and platform teams to leverage hybrid and edge infrastructure as part of their Kubernetes deployments. Traditionally, AKS worker nodes are provisioned within Azure-managed environments. Flex Nodes expand this capability by allowing organizations to connect worker nodes running outside of Azure—such as on-premises or edge hardware—to an AKS-managed control plane in Azure. This update is designed to provide a consistent Kubernetes management experience across diverse infrastructure environments.

**Specific Features and Detailed Changes**  
Flex Nodes for AKS introduce a new deployment option where hybrid and edge infrastructure can be registered as connected worker nodes to an AKS cluster. This enables teams to run containerized workloads on hardware outside of Azure while maintaining centralized control and management via the Azure-hosted Kubernetes control plane. The main feature is the ability to extend the AKS cluster's node pool with nodes that reside in non-Azure environments, thus supporting hybrid and edge computing scenarios.

**Technical Mechanisms and Implementation Methods**  
With Flex Nodes, the AKS control plane remains hosted and managed within Azure, ensuring consistent Kubernetes API compatibility, security, and lifecycle management. The connected worker nodes (Flex Nodes) communicate with the AKS control plane over secure channels. These nodes are registered as part of the AKS cluster, allowing standard Kubernetes scheduling, monitoring, and management operations. The mechanism relies on secure connectivity between the external infrastructure and Azure, and the nodes must meet the requirements for integration with the AKS control plane.

**Use Cases and Application Scenarios**  
Flex Nodes are particularly suitable for scenarios where workloads need to run close to physical devices, data sources, or users, such as in manufacturing plants, retail stores, or remote branch offices. Common use cases include:
- Running latency-sensitive applications at the edge while maintaining centralized control.
- Leveraging existing on-premises hardware as part of a cloud-managed Kubernetes cluster.
- Supporting hybrid cloud strategies where workloads span both Azure and non-Azure environments.

**Important Considerations and Limitations**  
As Flex Nodes are in Public Preview, they may not be recommended for production workloads. Users should consider the following:
- Network connectivity between the external nodes and the Azure control plane must be reliable and secure.
- The feature may have limitations in terms of supported node operating systems, hardware configurations, or integration with certain AKS features.
- Monitoring, logging, and security policies must account for the hybrid nature of the deployment.

**Integration with Related Azure Services**  
Flex Nodes integrate directly with the AKS control plane, leveraging Azure’s managed Kubernetes capabilities. This allows organizations to use Azure-native tools for cluster management, monitoring, and security, even for workloads running outside of Azure. Integration with other Azure services (such as Azure Monitor, Azure Policy, or Azure Arc) may be possible, depending on the specific capabilities enabled during the Public Preview.

**Summary Sentence**  
Flex Nodes for AKS (Public Preview) enable organizations to connect hybrid and edge infrastructure as worker nodes to an Azure-managed Kubernetes control plane, providing a consistent and centralized Kubernetes management experience across both Azure and non-Azure environments.

---


*This report was automatically generated - 2026-09-23 03:01:49 UTC*