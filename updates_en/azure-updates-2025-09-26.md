# September 26, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 26, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Azure NetApp Files Flexible service level

**Published**: September 25, 2025 17:00:08 UTC
**Link**: [Generally Available: Azure NetApp Files Flexible service level](https://azure.microsoft.com/updates?id=503687)

**Update ID**: 503687
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure NetApp Files, Features, Pricing & Offerings, SDK and Tools

**Summary**:

- What was updated  
Azure NetApp Files introduced the Flexible service level, now generally available.

- Key changes or new features  
The Flexible service level enables independent configuration of storage capacity and throughput, allowing users to right-size resources based on actual workload requirements. This customization helps optimize costs and performance by avoiding the traditional fixed ratio of capacity to throughput, reducing overprovisioning. Users can scale throughput without needing to increase storage capacity, providing greater operational flexibility.

- Target audience affected  
Developers and IT professionals managing file storage workloads in Azure who require fine-grained control over performance and cost optimization, especially for applications with variable or unpredictable throughput demands.

- Important notes if any  
Flexible service level is designed to improve cost efficiency and performance tuning for Azure NetApp Files deployments. Users should evaluate their workload patterns to leverage this new capability effectively. Existing service levels remain available for use, allowing gradual migration or mixed deployment strategies.

For more details, visit: https://azure.microsoft.com/updates?id=503687

**Details**:

The Azure NetApp Files Flexible service level, now generally available, introduces a significant enhancement by allowing independent configuration of storage capacity and throughput, enabling precise right-sizing of resources to optimize both cost and performance. Traditionally, Azure NetApp Files service levels—Standard, Premium, and Ultra—coupled throughput and capacity, often leading to overprovisioning when workloads required high throughput but not proportional storage capacity, or vice versa. The Flexible service level addresses this inefficiency by decoupling these parameters, providing granular control to IT professionals.

Specifically, the Flexible service level permits users to specify throughput (measured in MiB/s) independently from storage capacity (measured in TiB). This is achieved through a customizable throughput setting that can be scaled up or down without altering the provisioned storage size. The underlying technical mechanism involves dynamic allocation of network and storage resources within the Azure NetApp Files infrastructure, leveraging QoS (Quality of Service) policies and resource scheduling to guarantee the requested throughput. This flexibility is implemented via the Azure portal, CLI, and REST APIs, allowing seamless integration into existing automation and deployment workflows.

From a use case perspective, this update is particularly beneficial for workloads with variable or unpredictable throughput demands, such as databases, analytics platforms, and high-performance computing applications, where storage requirements remain relatively stable but throughput needs fluctuate. For example, a SQL Server workload with a fixed database size but varying query loads can now be provisioned with a fixed storage capacity and dynamically adjusted throughput, reducing costs associated with overprovisioned storage or throughput. Additionally, development and test environments can benefit from this flexibility by scaling throughput on-demand without incurring unnecessary storage costs.

Important considerations include understanding the minimum and maximum throughput limits per TiB of storage, which are documented in Azure NetApp Files service specifications. While Flexible service level offers throughput customization, it is essential to monitor performance metrics to avoid bottlenecks or underutilization. Also, certain legacy features or integrations might require validation for compatibility with the Flexible service level. Billing is adjusted to reflect the decoupled model, with throughput and capacity billed separately, so IT professionals should update cost management practices accordingly.

Integration with related Azure services remains robust; Azure NetApp Files Flexible service level continues to support mounting via SMB and NFS protocols, enabling use with Azure Kubernetes Service (AKS), Azure Virtual Machines, and Azure App Services. It also integrates with Azure Monitor for performance and health telemetry, and Azure Policy for governance. The decoupled throughput model complements Azure’s broader push towards flexible, consumption-based resource management, aligning well with autoscaling and cost optimization strategies.

In summary, the Azure NetApp Files Flexible service level empowers IT professionals to optimize storage and throughput independently, reducing overprovisioning and costs while maintaining high performance, supported by dynamic resource allocation and seamless integration with Azure’s ecosystem.

---

### 2. Retirement: The Insights blade in AKS is now called Monitor

**Published**: September 25, 2025 12:00:02 UTC
**Link**: [Retirement: The Insights blade in AKS is now called Monitor](https://azure.microsoft.com/updates?id=497368)

**Update ID**: 497368
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Azure Monitor, Retirements

**Summary**:

- What was updated  
The Insights blade within Azure Kubernetes Service (AKS) has been renamed to Monitor and moved from the Monitoring section to the top-level menu in the AKS portal.

- Key changes or new features  
The primary change is the renaming and repositioning of the blade for better visibility and easier access. All existing monitoring data, metrics, and features remain unchanged and fully accessible under the new Monitor blade.

- Target audience affected  
Developers and IT professionals managing AKS clusters who use the Azure portal for monitoring and diagnostics will be affected by this UI update.

- Important notes if any  
No functionality or data access has been altered; this is purely a UI/UX update to improve discoverability of AKS monitoring tools. Users should look for “Monitor” instead of “Insights” when navigating the AKS portal. Existing monitoring configurations and integrations continue to work without modification.

**Details**:

The Azure Kubernetes Service (AKS) update renames the existing "Insights" blade to "Monitor" and moves it from the Monitoring section to the top level of the Azure portal’s AKS resource menu, aiming to enhance its visibility and accessibility without altering its underlying functionality or data.

**Background and Purpose of the Update**  
The Insights blade in AKS has long served as the primary interface for monitoring cluster health, performance, and diagnostics by leveraging Azure Monitor capabilities. However, its placement within the Monitoring section of the AKS resource menu limited discoverability for users who need quick access to monitoring data. Renaming it to "Monitor" and elevating it to the top-level menu aligns with Azure’s broader portal design principles to improve user experience by making critical operational tools more prominent. This update reflects a strategic effort to unify monitoring experiences and terminology across Azure services, reducing confusion and streamlining navigation.

**Specific Features and Detailed Changes**  
- **Renaming:** The blade formerly known as "Insights" is now labeled "Monitor."  
- **Relocation:** It has been moved from the nested Monitoring section to the top-level menu of the AKS resource in the Azure portal.  
- **Functionality:** All existing monitoring features remain intact, including access to cluster performance metrics, node and pod health, container insights, and diagnostic logs.  
- **No Data or API Changes:** The update does not affect the underlying data collection, storage, or APIs; it is purely a UI/UX enhancement.

**Technical Mechanisms and Implementation Methods**  
This update is implemented as a portal UI change within the Azure Resource Manager (ARM) framework. The AKS resource provider’s portal blade metadata has been updated to rename and reposition the blade. Since the monitoring data is sourced from Azure Monitor and Log Analytics workspaces connected to AKS clusters, no backend changes are necessary. The monitoring pipeline continues to ingest telemetry via the Azure Monitor Container Insights agent deployed as DaemonSets within AKS clusters. The update leverages existing ARM portal extensibility and resource provider configurations to reflect the new blade name and location.

**Use Cases and Application Scenarios**  
- **Cluster Health Monitoring:** Operators can quickly access the Monitor blade to view node and pod status, resource utilization, and alerts.  
- **Performance Troubleshooting:** Developers and SREs use the blade to analyze CPU, memory, and network metrics to diagnose performance bottlenecks.  
- **Security and Compliance:** Teams review audit logs and diagnostic data to ensure cluster security and compliance with organizational policies.  
- **Capacity Planning:** Insights into resource consumption trends help in scaling decisions and cost optimization.  
- **Incident Response:** The improved visibility facilitates faster access during incident investigations.

**Important Considerations and Limitations**  
- **No Functional Changes:** Users should expect no changes in data availability or monitoring capabilities; only the UI label and location have changed.  
- **Documentation Updates:** Scripts or documentation referencing the "Insights" blade may need updating to reflect the new "Monitor" terminology.  
- **Access Permissions:** Existing role-based access controls (RBAC) and Azure Active Directory (AAD) permissions remain unchanged.  
- **Portal Cache:** Users may need to refresh or clear browser cache to see the updated blade name and location immediately.

**Integration with Related Azure Services**  
- **Azure Monitor:** The Monitor blade continues to surface data collected by Azure Monitor, including metrics, logs, and alerts.  
- **Log Analytics:** Diagnostic data from AKS clusters is stored in connected Log Analytics workspaces, accessible via the Monitor blade.  
- **Azure Advisor and Alerts:** Integration with Azure Advisor recommendations and alerting mechanisms remains seamless for proactive cluster management.  
- **Azure Policy:** Monitoring data can be correlated with Azure Policy compliance reports for governance.  
- **Azure DevOps and CI/CD Pipelines:** Teams can integrate monitoring insights into deployment pipelines for continuous feedback.

In summary, the renaming and repositioning of the AKS

---


*This report was automatically generated - 2025-09-26 03:01:43 UTC*