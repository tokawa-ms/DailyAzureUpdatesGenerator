# July 24, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 24, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Azure DDoS Protection custom policy

**Published**: July 23, 2026 16:47:24 UTC
**Link**: [Public Preview: Azure DDoS Protection custom policy](https://azure.microsoft.com/updates?id=568063)

**Update ID**: 568063
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Azure DDoS Protection, Services, Feature

**Summary**:

- What was updated  
Azure DDoS Protection now supports custom policy configuration, available in public preview.

- Key changes or new features  
This update introduces the ability to set custom DDoS mitigation thresholds on a per-resource basis for Standard Load Balancer frontend IP configurations. Developers and IT admins can now configure fixed inbound detection thresholds, allowing more granular control over when DDoS mitigation is triggered for each protected resource.

- Target audience affected  
Azure customers using DDoS Protection with Standard Load Balancers, particularly network administrators, security teams, and developers responsible for application availability and resilience.

- Important notes if any  
Custom DDoS policies enable fine-tuning of protection settings to better align with specific application traffic patterns and risk profiles. This can help reduce false positives and optimize mitigation responses. The feature is currently in public preview, so it is recommended for testing and evaluation in non-production environments before full deployment. For more information, refer to the official [Azure Update announcement](https://azure.microsoft.com/updates?id=568063).

**Details**:

**Azure Update Report: Public Preview – Azure DDoS Protection Custom Policy**

**Background and Purpose of the Update**  
Azure DDoS Protection is designed to safeguard Azure resources against Distributed Denial of Service (DDoS) attacks. Traditionally, DDoS mitigation thresholds were managed at a broader level, limiting granular control for individual resources. The introduction of custom policy in public preview addresses this gap by enabling per-resource configuration, specifically for Standard Load Balancer frontend IPs. This update aims to provide customers with enhanced flexibility and precision in managing DDoS mitigation, allowing tailored protection strategies for different workloads.

**Specific Features and Detailed Changes**  
The key feature of this update is the ability to configure custom DDoS mitigation thresholds on a per-resource basis. Customers can now set fixed inbound detection thresholds for protected Standard Load Balancer frontend IP configurations. This means that instead of relying on default, global settings, IT professionals can define specific thresholds that trigger DDoS mitigation actions, optimizing protection for each resource according to its risk profile and traffic patterns.

**Technical Mechanisms and Implementation Methods**  
Technically, the custom policy is implemented by associating configuration settings directly with the Standard Load Balancer’s frontend IP resources. These settings allow the definition of fixed inbound detection thresholds, which are used by Azure’s DDoS Protection service to monitor traffic and determine when to initiate mitigation. The custom policy is managed through Azure’s interface, enabling administrators to specify the desired thresholds and apply them to individual frontend IPs. This granular control is achieved without altering the underlying DDoS Protection infrastructure, ensuring seamless integration with existing protection mechanisms.

**Use Cases and Application Scenarios**  
This feature is particularly useful for organizations with diverse workloads hosted behind Standard Load Balancers, where each workload may have different sensitivity to DDoS attacks and varying normal traffic volumes. For example, a mission-critical application with low normal traffic but high sensitivity to disruption can be assigned a lower threshold, ensuring rapid mitigation. Conversely, a high-traffic application can have a higher threshold to avoid unnecessary mitigation during legitimate traffic spikes. This flexibility supports scenarios such as multi-tenant environments, differentiated service levels, and compliance-driven protection strategies.

**Important Considerations and Limitations**  
As this feature is in public preview, it may not be suitable for production environments where stability and support are critical. Customers should carefully evaluate the impact of custom thresholds, as misconfiguration could lead to either insufficient protection or excessive mitigation, potentially affecting legitimate traffic. The feature currently applies only to Standard Load Balancer frontend IP configurations, and does not extend to other resource types or Azure load balancer variants. It is important to monitor and review threshold settings regularly to ensure optimal protection.

**Integration with Related Azure Services**  
Azure DDoS Protection custom policy integrates directly with Standard Load Balancer, leveraging its frontend IP configuration as the point of control. It works alongside existing DDoS Protection capabilities, complementing Azure’s security ecosystem. Administrators can use Azure’s management tools and APIs to configure, monitor, and adjust custom policies, ensuring compatibility with automation and governance workflows.

**Summary Sentence**  
Azure DDoS Protection custom policy, now in public preview, enables per-resource configuration of fixed inbound detection thresholds for Standard Load Balancer frontend IPs, providing granular control and enhanced flexibility in DDoS mitigation strategies.

---


*This report was automatically generated - 2026-07-24 03:01:24 UTC*