# May 20, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 20, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Public Preview: Evaluate feature rollouts with Azure App Configuration Scorecards

**Published**: May 19, 2026 17:15:23 UTC
**Link**: [Public Preview: Evaluate feature rollouts with Azure App Configuration Scorecards](https://azure.microsoft.com/updates?id=561049)

**Update ID**: 561049
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Developer tools, Mobile, Security, Web, App Configuration, Features

**Summary**:

- What was updated  
Azure App Configuration has introduced a new "scorecards" capability, now available in public preview.

- Key changes or new features  
Scorecards provide telemetry-driven insights into the performance of feature flag variants in production. This feature enables teams to automatically track and visualize key metrics associated with feature rollouts, helping to quickly identify the impact of new features or changes without manual data analysis. Scorecards aggregate relevant telemetry data, making it easier to evaluate the success or issues of a rollout and inform decisions about further deployments or rollbacks.

- Target audience affected  
This update is relevant for developers, DevOps engineers, and IT professionals who use Azure App Configuration and feature management to control feature rollouts in their applications.

- Important notes if any  
Scorecards are currently in public preview and may undergo changes before general availability. Integration with telemetry sources (such as Azure Monitor or Application Insights) is required to leverage scorecard insights. This feature streamlines the process of monitoring feature flag performance, reducing manual effort and improving rollout safety and decision-making.

For more details, see the official update: https://azure.microsoft.com/updates?id=561049

**Details**:

**Azure Update Report: Public Preview – Evaluate feature rollouts with Azure App Configuration Scorecards**

**Background and Purpose of the Update:**  
Azure App Configuration is a centralized service for managing application settings and feature flags. Feature management using feature flags is a common DevOps practice, enabling controlled rollouts and experimentation. However, evaluating the impact of feature flag rollouts in production environments has traditionally required manual analysis of telemetry data, which can be time-consuming and error-prone. The introduction of scorecards addresses this gap by providing a built-in, telemetry-driven view to assess the performance of feature flag variants, streamlining post-deployment evaluation.

**Specific Features and Detailed Changes:**  
With this update, Azure App Configuration introduces a new scorecards capability, now available in public preview. Scorecards aggregate telemetry data related to feature flag variants, presenting a consolidated view of how each variant is performing in production. This enables teams to quickly identify measurable changes and outcomes following a feature rollout, without manual data collection or analysis. The scorecards feature is designed to support continuous delivery and progressive rollout strategies by providing actionable insights directly within the Azure App Configuration experience.

**Technical Mechanisms and Implementation Methods:**  
The scorecards capability leverages telemetry data to evaluate feature flag performance. While the detailed telemetry sources and integration methods are not specified in the provided update, the feature is described as “telemetry-driven,” indicating that it collects and processes relevant metrics associated with feature flag usage and outcomes. Scorecards likely visualize this data in a structured format, enabling users to compare the impact of different feature flag variants over time. The implementation is integrated into the Azure App Configuration service, allowing seamless access for users managing their feature flags within Azure.

**Use Cases and Application Scenarios:**  
- **Progressive Feature Rollouts:** Teams can monitor the impact of new features released to subsets of users, ensuring that changes do not negatively affect key metrics before expanding the rollout.
- **A/B Testing:** Scorecards provide a mechanism to compare the performance of different feature flag variants, supporting data-driven decision-making for product improvements.
- **Incident Response:** In the event of unexpected issues, scorecards help quickly identify whether a feature flag change correlates with observed problems in production.
- **Continuous Delivery:** By automating the evaluation of feature rollouts, scorecards support rapid iteration and deployment cycles, reducing the risk associated with frequent releases.

**Important Considerations and Limitations:**  
- The scorecards feature is currently in public preview, which means it may not be fully supported for production workloads and could be subject to changes.
- As with any preview feature, there may be limitations in terms of scalability, reliability, and available functionality.
- The update does not specify the exact telemetry sources or the types of metrics visualized, so users should consult the official documentation for integration requirements and supported scenarios.

**Integration with Related Azure Services:**  
Scorecards are integrated within Azure App Configuration, which itself can be used alongside other Azure services such as Azure Functions, Azure App Service, and Azure DevOps for end-to-end feature management. While the update does not detail direct integrations with other telemetry or monitoring services, the telemetry-driven nature of scorecards suggests potential synergy with Azure Monitor or Application Insights for advanced analytics.

**Summary Sentence:**  
Azure App Configuration now offers a public preview of scorecards, providing telemetry-driven insights into feature flag variant performance to streamline post-rollout evaluation and support data-driven feature management.

---

### 2. Generally Available: Azure NetApp Files cache volumes 

**Published**: May 19, 2026 17:00:29 UTC
**Link**: [Generally Available: Azure NetApp Files cache volumes ](https://azure.microsoft.com/updates?id=562259)

**Update ID**: 562259
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features

**Summary**:

- What was updated  
Azure NetApp Files cache volumes are now Generally Available.

- Key changes or new features  
Azure NetApp Files now supports cache volumes, which act as cloud-based caches for external origin volumes. These cache volumes store only the most frequently accessed data, enabling faster access to critical files and reducing latency. This feature is particularly useful for hybrid and multi-region scenarios, as it allows data to be cached closer to the compute resources or users that need it most.

- Target audience affected  
This update is relevant for IT professionals managing storage solutions, cloud architects designing hybrid or multi-region architectures, and developers building applications that require high-performance access to large datasets stored externally.

- Important notes if any  
Cache volumes can help optimize performance and cost by minimizing data transfer and storage requirements for less frequently accessed data. They are ideal for scenarios where fast access to a subset of data is critical, such as analytics, media rendering, or engineering workloads. Proper configuration and monitoring are recommended to ensure cache efficiency and data consistency between the cache and the origin volume.

For more details, refer to the official Azure Update: https://azure.microsoft.com/updates?id=562259

**Details**:

**Azure Update Report: Azure NetApp Files Cache Volumes (General Availability)**

**Background and Purpose of the Update**  
Azure NetApp Files cache volumes are now generally available, introducing a new capability that allows organizations to leverage cloud-based caches for external origin volumes. The primary purpose of this update is to optimize data access by storing only the most actively accessed data in the cache volume. This enhancement addresses scenarios where frequent access to specific subsets of data is required, reducing latency and improving performance for workloads that depend on rapid file retrieval.

**Specific Features and Detailed Changes**  
With this release, Azure NetApp Files supports the creation of cache volumes. These volumes act as a cloud-based cache, containing only the most frequently accessed data from an external origin volume. The cache volume does not store the entire dataset but dynamically maintains a subset based on access patterns. This feature is designed to bring data and files closer to compute resources in Azure, thereby accelerating access times and reducing the need for repeated data transfers from external sources.

**Technical Mechanisms and Implementation Methods**  
The cache volume operates by monitoring access patterns to the external origin volume and selectively caching the most active files or data blocks. Data is synchronized between the cache volume and the origin volume, ensuring consistency for cached items. The mechanism relies on intelligent caching algorithms to determine which data should reside in the cache, optimizing storage utilization and performance. Azure NetApp Files manages the lifecycle of the cache volume, including cache population, eviction, and synchronization with the origin volume.

**Use Cases and Application Scenarios**  
Typical use cases for Azure NetApp Files cache volumes include:  
- High-performance computing workloads where only a subset of data is frequently accessed.
- Analytics applications that require rapid access to hot data while minimizing latency.
- Migration scenarios where data remains on-premises or in another cloud, but active files are cached in Azure for faster processing.
- Collaborative environments where multiple users or applications need quick access to shared files without replicating the entire dataset.

**Important Considerations and Limitations**  
When utilizing cache volumes, IT professionals should consider the following:  
- Only actively accessed data is stored in the cache; infrequently accessed files remain on the origin volume.
- Cache volumes are not intended for full data replication or backup purposes.
- Data consistency between the cache and origin volume is managed by Azure NetApp Files, but changes to non-cached data may not be immediately reflected in Azure.
- Proper configuration and monitoring are required to ensure optimal cache performance and to avoid cache misses for critical workloads.

**Integration with Related Azure Services**  
Azure NetApp Files cache volumes integrate seamlessly with other Azure services, particularly those requiring high-performance file storage. They can be used alongside Azure compute resources, such as Virtual Machines and Azure Kubernetes Service, to accelerate access to external datasets. The cache volumes also complement Azure networking solutions, enabling efficient data transfer and access across hybrid and multi-cloud environments.

**Summary Sentence**  
Azure NetApp Files cache volumes, now generally available, provide a cloud-based caching solution for external origin volumes, enabling faster access to actively used data and improving performance for workloads that require rapid file retrieval in Azure.

---

### 3. Generally Available: Azure Virtual Network updates – default limits increased for NSGs and route tables 

**Published**: May 19, 2026 16:45:42 UTC
**Link**: [Generally Available: Azure Virtual Network updates – default limits increased for NSGs and route tables ](https://azure.microsoft.com/updates?id=562695)

**Update ID**: 562695
**Data source**: Azure Updates API

**Categories**: Launched, Features, Management, Security, Services

**Summary**:

- What was updated  
Azure Virtual Network has increased the default limits for network security groups (NSGs) and route tables.

- Key changes or new features  
  - The maximum number of security rules per NSG is now 2,000 (previously lower).  
  - Each NSG rule can now specify up to 6,000 addresses or ports.  
  - The maximum number of routes per route table is now 1,000.  
  - Each route table can now support up to 600 route entries.

- Target audience affected  
This update is relevant for developers, network architects, and IT professionals who design, deploy, or manage Azure virtual networks, especially those with complex security or routing requirements.

- Important notes if any  
  - These increased limits are now the default for new and existing deployments, allowing for more granular security and routing configurations without requiring special requests.  
  - Organizations with large-scale or multi-tenant environments can benefit from simplified management and improved scalability.  
  - Review your current NSG and route table configurations to determine if you can consolidate or optimize your network architecture in light of these new limits.

For more details, see the official update: https://azure.microsoft.com/updates?id=562695

**Details**:

**Azure Update Report: Azure Virtual Network – Default Limits Increased for NSGs and Route Tables (General Availability)**

**Background and Purpose of the Update**  
Azure Virtual Network is a foundational service for securely connecting Azure resources. Network Security Groups (NSGs) and route tables are critical for defining and enforcing network security and traffic flow. As customer deployments scale, the need for more granular security rules and complex routing increases. This update addresses customer demand for higher scalability by increasing the default platform limits for NSGs and route tables, enabling more sophisticated network designs without requiring support requests for limit increases.

**Specific Features and Detailed Changes**  
The update introduces the following new default limits:
- **NSG Security Rules**: Increased from previous limits to 2,000 security rules per NSG.
- **Addresses or Ports per NSG Rule**: Increased to 6,000 addresses or ports per rule.
- **Routes per Route Table**: Increased to 1,000 routes per route table.
- **Routes per Route Table per VM NIC/Subnet**: Increased to 600 routes.

These changes are now generally available and apply to all Azure regions.

**Technical Mechanisms and Implementation Methods**  
The increased limits are implemented at the Azure platform level. No manual intervention or configuration changes are required from customers to benefit from these new defaults. The Azure control plane and data plane have been optimized to support the higher rule and route counts, ensuring that network performance and reliability are maintained as customers scale their configurations.

**Use Cases and Application Scenarios**  
- **Large-Scale Segmentation**: Enterprises with complex segmentation requirements can now define more granular NSG rules, supporting zero-trust architectures and multi-tier applications.
- **Microservices and Service Meshes**: Deployments with many microservices or containers can leverage the increased address/port limits per NSG rule for simplified management.
- **Advanced Routing**: Organizations with intricate routing needs, such as hybrid connectivity, custom traffic engineering, or service chaining, can define more routes per route table, supporting larger and more complex topologies.
- **Multi-Tenant Environments**: Service providers and SaaS platforms hosting multiple tenants can better isolate and control traffic at scale.

**Important Considerations and Limitations**  
- These are default platform limits; customers should still monitor their configurations to avoid approaching limits, which could impact deployment or management operations.
- While the limits have increased, best practices for rule and route optimization should still be followed to maintain manageability and performance.
- There is no mention of changes to maximum supported limits (hard limits) or any impact on existing NSGs or route tables.

**Integration with Related Azure Services**  
- **Azure Firewall and Azure Application Gateway**: These services can be used in conjunction with NSGs and route tables for layered security and traffic management.
- **Azure Policy and Azure Monitor**: Use these services to audit, enforce, and monitor NSG and route table configurations at scale.
- **Virtual Network Peering and VPN Gateways**: The increased limits facilitate more complex peering and hybrid connectivity scenarios.

**Summary**  
Azure Virtual Network now supports increased default limits for NSGs and route tables, enabling up to 2,000 security rules per NSG, 6,000 addresses or ports per rule, 1,000 routes per route table, and 600 routes per VM NIC/subnet, allowing for greater scalability and flexibility in network security and routing configurations.

---

### 4. Generally Available: Network Watcher rule impact analyser 

**Published**: May 19, 2026 16:45:42 UTC
**Link**: [Generally Available: Network Watcher rule impact analyser ](https://azure.microsoft.com/updates?id=562690)

**Update ID**: 562690
**Data source**: Azure Updates API

**Categories**: Launched, Features

**Summary**:

- What was updated  
Azure Network Watcher rule impact analyzer is now generally available.

- Key changes or new features  
The rule impact analyzer allows users to evaluate the potential effects of changes to Network Security Group (NSG) rules or security admin rules on live network traffic before those changes are applied. This feature analyzes proposed rule modifications and predicts which network flows will be affected, helping to prevent accidental disruptions or security issues.

- Target audience affected  
This update is relevant for network administrators, IT professionals, and developers who manage Azure network security groups or security admin rules and need to assess the impact of rule changes in advance.

- Important notes if any  
The rule impact analyzer helps reduce the risk of outages or unintended access by providing visibility into how rule changes will affect network traffic. This can improve change management processes and enhance overall network security posture. The feature is now generally available in all public Azure regions. For more information, refer to the official Azure Update: https://azure.microsoft.com/updates?id=562690

**Details**:

**Azure Update Report: Network Watcher Rule Impact Analyzer – General Availability**

**Background and Purpose of the Update**  
Azure Network Watcher is a suite of tools designed to monitor and diagnose network conditions in Azure environments. Network security groups (NSGs) and security admin rules are critical for controlling traffic flow and enforcing security policies. However, modifying these rules can inadvertently disrupt live network traffic or introduce vulnerabilities. The purpose of this update is to provide IT professionals with a mechanism to assess the potential impact of NSG or security admin rule changes before they are applied, thereby reducing risk and improving operational confidence.

**Specific Features and Detailed Changes**  
The Network Watcher rule impact analyzer is now generally available. This feature allows users to evaluate how proposed changes to NSG or security admin rules will affect live network traffic. Key capabilities include:

- Pre-deployment analysis: Assess the impact of rule changes on current network flows without applying them.
- Visualization: Identify affected flows and endpoints, enabling targeted troubleshooting and validation.
- Integration with existing Network Watcher workflows: Seamlessly incorporate impact analysis into routine network management tasks.

This update introduces a proactive assessment tool, moving beyond traditional post-change troubleshooting.

**Technical Mechanisms and Implementation Methods**  
The rule impact analyzer leverages real-time traffic data and existing NSG/security admin rule configurations. When a user proposes a rule change, the analyzer simulates the effect of the new rule set against live traffic patterns. It identifies which flows would be allowed or denied as a result of the change, providing actionable insights before deployment. The mechanism operates within the Azure portal and can be invoked through Network Watcher interfaces, ensuring ease of access and integration with Azure-native management tools.

**Use Cases and Application Scenarios**  
- Change management: IT teams can validate rule changes during maintenance windows, minimizing downtime and service disruption.
- Security audits: Security professionals can assess the impact of tightening or loosening NSG rules, ensuring compliance without affecting legitimate traffic.
- Troubleshooting: Engineers can use the analyzer to diagnose connectivity issues related to rule misconfigurations before implementing fixes.
- DevOps workflows: Automated pipelines can incorporate impact analysis as a pre-deployment step, enhancing CI/CD reliability for network configurations.

**Important Considerations and Limitations**  
- The analyzer assesses impact based on live traffic at the time of analysis; it may not account for future or intermittent flows.
- Only NSG and security admin rules are supported; other network controls (e.g., Azure Firewall, Application Gateway) are not included in this analysis.
- The tool is intended for pre-deployment validation and does not apply changes automatically; manual review and approval are required.
- Integration and data visibility depend on Network Watcher being enabled in the relevant Azure regions and subscriptions.

**Integration with Related Azure Services**  
The rule impact analyzer is tightly integrated with Azure Network Watcher, leveraging its traffic monitoring and diagnostic capabilities. It complements NSG management workflows and can be used alongside Azure Monitor for broader visibility. The tool fits into Azure’s security and compliance ecosystem, supporting best practices for change management and operational governance.

**Summary Sentence**  
Azure Network Watcher rule impact analyzer is now generally available, enabling IT professionals to proactively assess the potential effects of NSG or security admin rule changes on live network traffic before deployment, thereby enhancing network reliability and security.

---

### 5. Generally Available: Mock runs for Azure Storage Actions – Validate before you execute

**Published**: May 19, 2026 16:00:11 UTC
**Link**: [Generally Available: Mock runs for Azure Storage Actions – Validate before you execute](https://azure.microsoft.com/updates?id=559494)

**Update ID**: 559494
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Storage Actions, Features

**Summary**:

- What was updated  
Azure Storage Actions now supports mock runs, which are generally available.

- Key changes or new features  
Mock runs allow users to simulate the execution of data management tasks (such as moving, deleting, or tagging blobs and files) at full scale without actually modifying any data. This feature helps validate task logic, scope, and potential impact before running actions in production. Mock runs provide detailed reports on what would happen, enabling safer and more predictable automation.

- Target audience affected  
Developers and IT professionals who automate data management tasks in Azure Blob Storage and Azure Data Lake Storage using Azure Storage Actions.

- Important notes if any  
Mock runs are useful for testing and validating automation workflows, reducing risk of unintended data changes. They can be integrated into CI/CD pipelines or used during planning phases to ensure actions are safe and effective. No data is changed during mock runs, making them ideal for production environments.  
For more details, see the official Azure Update: [Mock runs for Azure Storage Actions](https://azure.microsoft.com/updates?id=559494).

**Details**:

**Azure Update Report: Mock Runs for Azure Storage Actions – General Availability**

**Background and Purpose of the Update**  
Azure Storage Actions is a fully managed platform designed to automate data management tasks for Azure Blob Storage and Azure Data Lake Storage. Automation is critical for managing large-scale data environments, but executing automation tasks directly on production data can introduce risks such as accidental data modification or deletion. The introduction of "mock runs" addresses this challenge by enabling organizations to validate and simulate task execution at scale before making any actual changes to their data.

**Specific Features and Detailed Changes**  
The key feature introduced is support for "mock runs" within Azure Storage Actions. Mock runs allow users to simulate the execution of data management tasks—such as moving, copying, or deleting blobs—without modifying any actual data. This simulation operates at full scale, meaning it processes the same scope and volume of data as a real execution, but all operations are non-destructive and do not alter the underlying storage objects.

**Technical Mechanisms and Implementation Methods**  
Mock runs are implemented as a simulation layer within Azure Storage Actions. When a mock run is initiated, the platform processes the defined automation workflow, evaluates all rules, filters, and actions, and generates a detailed report of what would have happened if the task had been executed for real. No write, delete, or update operations are performed on the actual data. Instead, the system logs intended actions, providing visibility into the workflow's impact, including which blobs or files would have been affected and the sequence of operations.

**Use Cases and Application Scenarios**  
- **Change Validation:** Before applying data lifecycle policies or bulk operations, administrators can use mock runs to ensure that only the intended data will be affected.
- **Workflow Testing:** Developers and DevOps teams can test new or updated automation workflows in a production-like environment without risk.
- **Audit and Compliance:** Mock runs provide an audit trail of potential changes, supporting compliance verification and change management processes.
- **Training and Onboarding:** New team members can practice running automation tasks safely using mock runs.

**Important Considerations and Limitations**  
- Mock runs do not modify any data; they are strictly for simulation and validation purposes.
- The accuracy of a mock run depends on the current state of the data at the time of simulation; subsequent changes to data may affect actual execution outcomes.
- Mock runs are supported for Azure Blob Storage and Azure Data Lake Storage, as per the scope of Azure Storage Actions.
- There may be limitations on the types of actions or workflows that can be simulated, depending on the underlying implementation (refer to Azure documentation for specifics).

**Integration with Related Azure Services**  
Azure Storage Actions, including mock runs, integrates with Azure Blob Storage and Azure Data Lake Storage. The platform can be orchestrated alongside other Azure automation and monitoring tools, such as Azure Logic Apps, Azure Functions, and Azure Monitor, to build comprehensive data management and governance solutions. Mock run reports can be used as input for approval workflows or integrated into CI/CD pipelines for automated validation.

---

**Summary:**  
Azure Storage Actions now supports mock runs, enabling organizations to simulate and validate data management tasks for Azure Blob and Data Lake Storage at full scale without modifying any data, thereby enhancing operational safety and workflow reliability.

---


*This report was automatically generated - 2026-05-20 03:02:32 UTC*