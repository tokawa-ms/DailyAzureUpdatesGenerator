# October 17, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 17, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Prescaling in Azure Firewall 

**Published**: October 16, 2025 16:15:32 UTC
**Link**: [Generally Available: Prescaling in Azure Firewall ](https://azure.microsoft.com/updates?id=515452)

**Update ID**: 515452
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall now generally supports prescaling, allowing capacity units to be provisioned and reserved ahead of time.

- Key changes or new features  
Prescaling enables administrators to allocate firewall throughput capacity in advance to handle predictable traffic surges, such as seasonal spikes or planned business events. This proactive capacity reservation helps maintain consistent throughput and reduces latency during high-demand periods.

- Target audience affected  
This update primarily benefits network administrators, security engineers, and IT professionals responsible for managing Azure Firewall deployments, as well as developers who rely on predictable firewall performance for their applications.

- Important notes if any  
Prescaling must be configured proactively based on expected traffic patterns; it is not an automatic scaling feature. Proper planning is required to optimize cost and performance. This feature enhances reliability during peak loads but does not replace dynamic scaling capabilities. For detailed configuration guidance, refer to the official Azure Firewall documentation.

**Details**:

Azure Firewall’s newly introduced prescaling feature, now generally available, addresses the critical need for predictable and consistent network throughput during periods of anticipated high traffic by allowing administrators to proactively provision and reserve capacity units. Traditionally, Azure Firewall scales automatically based on traffic demand; however, this reactive scaling can introduce latency or throughput variability during sudden traffic surges, such as seasonal peaks, marketing campaigns, or large-scale business events. Prescaling empowers IT professionals to mitigate these challenges by pre-allocating firewall capacity, ensuring performance stability and reducing the risk of bottlenecks.

Technically, prescaling enables explicit reservation of Azure Firewall capacity units ahead of time, decoupling capacity provisioning from real-time traffic fluctuations. Administrators can specify the desired capacity units via Azure Portal, CLI, or ARM templates, effectively instructing the service to allocate and maintain the requested throughput level regardless of current load. This capacity reservation is implemented through Azure Firewall’s underlying autoscaling architecture, which now supports a “minimum capacity” threshold that remains active until manually adjusted or the reservation period ends. The feature integrates seamlessly with Azure Firewall’s existing autoscale capabilities, allowing dynamic scaling above the reserved baseline as needed, thus providing both guaranteed minimum capacity and elasticity.

Use cases for prescaling include scenarios where predictable firewall performance is critical, such as during Black Friday sales, product launches, or compliance-driven traffic surges. Enterprises running mission-critical applications can leverage prescaling to avoid transient throughput degradation, ensuring uninterrupted security inspection and traffic filtering. Additionally, organizations with strict SLAs can use prescaling to align firewall capacity with contractual performance guarantees. This feature is particularly beneficial in hybrid cloud architectures where on-premises systems connect to Azure via VPN or ExpressRoute, and traffic patterns are well understood and predictable.

Important considerations include the potential cost implications of reserving capacity units, as prescaling involves paying for allocated throughput regardless of actual usage during the reservation period. IT teams should carefully analyze traffic forecasts and balance cost versus performance benefits. Furthermore, prescaling reservations should be managed proactively, with automation or scheduling to align capacity with known event timelines. Currently, prescaling applies to Azure Firewall Premium and Standard SKUs, and administrators should verify compatibility with their deployment model and region availability. Monitoring tools within Azure Monitor and Firewall logs should be utilized to track capacity utilization and adjust prescaling settings accordingly.

From an integration standpoint, prescaling complements Azure Firewall’s native capabilities and works cohesively with Azure Monitor for telemetry, Azure Policy for governance, and Azure Automation for operational management. It also supports deployments behind Azure Application Gateway or in conjunction with Azure Front Door, ensuring that front-end scaling strategies align with firewall throughput provisioning. Additionally, prescaling can be integrated into CI/CD pipelines via ARM templates or Terraform scripts, enabling infrastructure-as-code practices for predictable and repeatable capacity management.

In summary, Azure Firewall prescaling is a strategic enhancement that allows IT professionals to reserve firewall capacity proactively, ensuring consistent throughput and performance during predictable traffic surges, while maintaining flexibility through autoscaling above the reserved baseline; this feature requires careful planning around cost and usage patterns and integrates smoothly with Azure’s broader network security and management ecosystem.

---

### 2. Retirement: Confidential Containers preview on AKS is Closing Down

**Published**: October 16, 2025 16:15:32 UTC
**Link**: [Retirement: Confidential Containers preview on AKS is Closing Down](https://azure.microsoft.com/updates?id=502044)

**Update ID**: 502044
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Features, Retirements

**Summary**:

- What was updated  
The public preview of Confidential Containers on Azure Kubernetes Service (AKS) is being retired and will be shut down.

- Key changes or new features  
No new features are introduced; instead, the existing Confidential Containers preview on AKS is discontinued as part of Azure’s effort to streamline its confidential computing offerings.

- Target audience affected  
Developers and IT professionals using AKS for deploying confidential workloads with Confidential Containers will be impacted. Organizations relying on this preview feature for secure containerized applications need to plan migration or alternative solutions.

- Important notes if any  
Since the feature was in preview since 2023, users should transition away from Confidential Containers on AKS before the shutdown to avoid disruptions. Azure recommends evaluating other confidential computing options available within the Azure ecosystem to maintain secure and reliable container workloads. Further details and timelines can be found in the official Azure update link.

**Details**:

The recent Azure update announces the retirement of the Confidential Containers public preview on Azure Kubernetes Service (AKS), which has been available since 2023. This decision reflects Microsoft’s strategic move to streamline its confidential computing offerings and focus on delivering secure, reliable, and fully supported services.

**Background and Purpose of the Update**  
Confidential Containers on AKS was introduced as a public preview to enable developers and IT professionals to run containerized workloads with enhanced confidentiality and integrity guarantees, leveraging hardware-based Trusted Execution Environments (TEEs). The feature aimed to protect sensitive data and code from exposure even to cloud administrators by isolating container workloads within secure enclaves. The retirement signals a shift from experimental preview features toward more mature, integrated confidential computing solutions within Azure’s ecosystem.

**Specific Features and Detailed Changes**  
During its preview, Confidential Containers on AKS allowed users to deploy containers that utilized Intel SGX or AMD SEV technologies to create isolated execution environments. This ensured that containerized applications could process sensitive information securely without risk of data leakage or tampering. With the retirement, the preview environment and associated APIs will no longer be supported, and users must transition away from this feature. Microsoft recommends exploring alternative confidential computing options that are generally available and supported.

**Technical Mechanisms and Implementation Methods**  
Confidential Containers leveraged hardware-based TEEs embedded in modern CPUs to create isolated memory regions inaccessible to the host OS or hypervisor. The AKS integration enabled seamless orchestration of these containers using Kubernetes primitives, with additional runtime components managing enclave attestation, secure provisioning, and encrypted memory. The preview required specific node SKUs and configurations to support the underlying hardware capabilities. With the retirement, these specialized runtime components and node configurations will be deprecated.

**Use Cases and Application Scenarios**  
Confidential Containers targeted scenarios requiring strong data protection in multi-tenant or regulated environments, such as financial services processing sensitive transactions, healthcare applications handling protected health information (PHI), or government workloads requiring compliance with strict confidentiality standards. The feature was particularly useful for customers needing to run unmodified containerized applications while ensuring runtime confidentiality without redesigning applications for confidential computing frameworks.

**Important Considerations and Limitations**  
As a preview feature, Confidential Containers on AKS had limitations including restricted regional availability, limited hardware SKU support, and evolving API stability. Performance overhead due to enclave transitions and memory constraints inherent to TEEs were also considerations. With the retirement, workloads relying on this preview must migrate to supported confidential computing solutions to maintain security guarantees and receive ongoing support and updates.

**Integration with Related Azure Services**  
Confidential Containers preview integrated with AKS for orchestration and Azure Attestation for verifying enclave integrity. It complemented Azure Confidential Computing services such as Azure Confidential VMs and Azure Confidential Ledger. Post-retirement, Microsoft encourages users to adopt these mature services, which provide broader hardware support, enhanced tooling, and integration with Azure Key Vault for secure key management, Azure Policy for compliance, and Azure Monitor for observability.

**Summary**  
The retirement of the Confidential Containers public preview on AKS marks the end of this experimental feature, urging users to transition to fully supported Azure confidential computing services that offer robust security, compliance, and operational capabilities. IT professionals should plan migration strategies to leverage Azure Confidential VMs and related services, ensuring continued protection of sensitive workloads with enterprise-grade support and integration.

---

### 3. Generally Available: Observed capacity metric in Azure Firewall 

**Published**: October 16, 2025 16:00:55 UTC
**Link**: [Generally Available: Observed capacity metric in Azure Firewall ](https://azure.microsoft.com/updates?id=516002)

**Update ID**: 516002
**Data source**: Azure Updates API

**Categories**: Launched, Networking, Security, Azure Firewall, Features

**Summary**:

- What was updated  
Azure Firewall now includes the Observed Capacity metric, which is generally available.

- Key changes or new features  
The Observed Capacity metric provides real-time visibility into the number of capacity units actively utilized by the firewall over time. This new observability signal helps administrators monitor how their Azure Firewall scales in practice, enabling better capacity planning and performance optimization.

- Target audience affected  
This update primarily benefits IT administrators, network engineers, and developers responsible for managing and scaling Azure Firewall deployments in enterprise environments.

- Important notes if any  
The metric can be accessed via Azure Monitor and integrated into custom dashboards or alerting systems using API data. Leveraging this metric allows proactive scaling decisions and improved troubleshooting of firewall throughput and capacity issues. No additional configuration is required to start using the Observed Capacity metric.

**Details**:

The recent Azure Firewall update introduces the generally available Observed Capacity metric, a significant enhancement aimed at improving operational visibility and capacity management for firewall deployments. This metric provides IT professionals with a real-time, data-driven insight into how Azure Firewall scales under actual workload conditions, enabling more precise resource planning and performance optimization.

**Background and Purpose of the Update**  
Azure Firewall is a cloud-native, stateful firewall service that protects Azure Virtual Network resources. It operates on a capacity unit model, where capacity units represent the firewall’s throughput and concurrent connection handling capabilities. Prior to this update, administrators primarily relied on provisioned capacity units and indirect performance indicators to estimate firewall usage and scaling needs. The Observed Capacity metric addresses the need for a direct, observable measurement of how many capacity units are actively consumed, reflecting real-world firewall utilization rather than theoretical or provisioned limits. This enhances transparency, reduces guesswork in scaling decisions, and helps avoid overprovisioning or underprovisioning.

**Specific Features and Detailed Changes**  
The Observed Capacity metric is now available as a built-in telemetry signal within Azure Monitor for Azure Firewall. It tracks the number of capacity units actively utilized by the firewall over time, providing a continuous and granular view of firewall load. This metric is exposed via Azure Monitor metrics and can be queried using Azure Monitor Logs (Log Analytics), enabling integration with dashboards, alerts, and automated scaling workflows. The metric updates dynamically, reflecting changes in traffic patterns and firewall processing demands.

**Technical Mechanisms and Implementation Methods**  
Under the hood, Azure Firewall’s control plane continuously monitors packet processing, connection states, and throughput to calculate the effective capacity units consumed. This involves aggregating data on concurrent connections, throughput, and rule evaluations, then normalizing these against the capacity unit definition. The Observed Capacity metric is emitted as a standard Azure Monitor metric, adhering to Azure’s telemetry conventions, allowing seamless integration with existing monitoring and alerting tools. No additional configuration is required to enable this metric; it is available by default for all Azure Firewall instances.

**Use Cases and Application Scenarios**  
- **Capacity Planning:** Administrators can track actual firewall utilization trends to inform scaling decisions, ensuring that capacity units provisioned align with real demand.  
- **Performance Troubleshooting:** Sudden spikes or sustained high observed capacity can indicate traffic surges or misconfigurations, prompting timely investigation.  
- **Cost Optimization:** By correlating observed capacity with provisioned capacity, teams can identify overprovisioned firewalls and adjust capacity units to reduce costs without compromising security.  
- **Automation:** Integration with Azure Monitor alerts enables automated notifications or scaling actions when observed capacity crosses defined thresholds.  
- **Reporting:** Historical observed capacity data supports capacity usage reporting for audits and operational reviews.

**Important Considerations and Limitations**  
- The Observed Capacity metric reflects active usage but does not directly measure firewall rule efficiency or security posture. It should be used in conjunction with other security and performance metrics.  
- Since capacity units relate to throughput and concurrent connections, workloads with highly variable traffic patterns may show fluctuating observed capacity; trend analysis is recommended over isolated data points.  
- The metric is available only for Azure Firewall Standard and Premium SKUs that support capacity units. Legacy or unsupported SKUs may not emit this metric.  
- Observed Capacity does not automatically trigger scaling; it requires integration with monitoring and automation tools to enable proactive capacity management.

**Integration with Related Azure Services**  
- **Azure Monitor:** Observed Capacity is integrated as a native metric, enabling visualization in Azure Monitor dashboards and queries via Log Analytics.  
- **Azure Automation and Logic Apps:** These services can consume Observed Capacity alerts to implement automated scaling or remediation workflows.  
- **Azure Cost Management:** By correlating observed capacity with billing data, organizations can optimize firewall spend.  
- **Azure Security Center:** While primarily focused on security posture, Security Center can complement Observed Capacity insights by correlating capacity usage with security alerts

---


*This report was automatically generated - 2025-10-17 03:02:21 UTC*