# February 24, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 24, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Windows Server Annual Channel (preview) 

**Published**: February 23, 2026 18:15:17 UTC
**Link**: [Retirement: Windows Server Annual Channel (preview) ](https://azure.microsoft.com/updates?id=557224)

**Update ID**: 557224
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS)

**Summary**:

- What was updated  
The Windows Server Annual Channel (Preview) on Azure Kubernetes Service (AKS) will be retired on May 15, 2026.

- Key changes or new features  
The Annual Channel (Preview) will no longer be supported on AKS after the retirement date. Users are advised to transition their workloads to the Windows Server Long Term Servicing Channel (LTSC), which will continue to be supported.

- Target audience affected  
Developers and IT professionals running Windows Server containers on AKS using the Annual Channel (Preview).

- Important notes if any  
To avoid service disruption, plan and execute migration to the LTSC before May 15, 2026. The LTSC provides a stable and supported environment for production workloads. Early transition is recommended to ensure continued support and security updates. Review your AKS clusters and update your deployment pipelines accordingly.  
For more details, refer to the official announcement: https://azure.microsoft.com/updates?id=557224

**Details**:

**Azure Update Report: Retirement of Windows Server Annual Channel (Preview) on AKS**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of the Windows Server Annual Channel (Preview) on Azure Kubernetes Service (AKS), effective May 15, 2026. This update is intended to inform users that the Annual Channel (Preview) will no longer be supported for AKS node pools after this date. The purpose is to encourage customers to transition their workloads to the Windows Server Long Term Servicing Channel (LTSC), which offers a more stable and supported platform for production environments.

**Specific Features and Detailed Changes:**  
- The Windows Server Annual Channel (Preview) images, which have been available for AKS node pools, will be deprecated.
- After May 15, 2026, AKS clusters will no longer support node pools running Windows Server Annual Channel (Preview) images.
- Customers are required to migrate their Windows-based AKS workloads to Windows Server LTSC images prior to the retirement date to ensure continued support and security updates.

**Technical Mechanisms and Implementation Methods:**  
- The Annual Channel (Preview) provided more frequent, short-term releases of Windows Server for AKS, allowing users to test new features and updates in a preview capacity.
- LTSC releases, in contrast, are designed for long-term stability and support, with a typical support lifecycle of 5 years of mainstream support and 5 years of extended support.
- Transitioning involves updating AKS node pools to use LTSC-based Windows Server images. This can be performed through the Azure Portal, CLI, or ARM templates by specifying the appropriate LTSC image version for Windows node pools.

**Use Cases and Application Scenarios:**  
- The Annual Channel (Preview) was primarily used by organizations seeking early access to new Windows Server features in AKS or for testing and validation purposes.
- Production workloads and mission-critical applications are recommended to run on LTSC images due to their stability and long-term support guarantees.
- After the retirement date, only LTSC images should be used for all Windows-based AKS node pools to maintain compliance and receive updates.

**Important Considerations and Limitations:**  
- Any AKS node pools or clusters still running Windows Server Annual Channel (Preview) images after May 15, 2026, will be unsupported and may not receive security updates or technical assistance.
- Migration to LTSC should be planned and executed well before the retirement date to avoid service disruption.
- Users should validate application compatibility with LTSC images before migration, as there may be differences in features or APIs between Annual Channel and LTSC releases.

**Integration with Related Azure Services:**  
- AKS integrates with various Azure services such as Azure Monitor, Azure Policy, and Azure Active Directory. These integrations are fully supported with LTSC-based Windows Server node pools.
- Transitioning to LTSC ensures continued compatibility and support with the broader Azure ecosystem and compliance with Microsoft’s support policies.

**Summary:**  
Windows Server Annual Channel (Preview) on AKS will be retired on May 15, 2026; users must transition their AKS Windows node pools to Long Term Servicing Channel (LTSC) images before this date to maintain support and receive updates.

---

### 2. Public Preview: WAF Insights for Application Gateway 

**Published**: February 23, 2026 16:15:47 UTC
**Link**: [Public Preview: WAF Insights for Application Gateway ](https://azure.microsoft.com/updates?id=557416)

**Update ID**: 557416
**Data source**: Azure Updates API

**Categories**: In preview, Networking, Security, Application Gateway, Web Application Firewall, Features

**Summary**:

- What was updated  
Azure Application Gateway Web Application Firewall (WAF) now offers WAF Insights in public preview.

- Key changes or new features  
WAF Insights provides an interactive dashboard for visualizing WAF logs and metrics. It enables users to quickly investigate blocked requests, analyze attack patterns, and monitor WAF activity. The feature includes drill-down capabilities for detailed request inspection, trend analysis, and actionable insights to optimize WAF policies.

- Target audience affected  
Developers and IT professionals managing web applications behind Azure Application Gateway, particularly those responsible for security monitoring, incident response, and WAF policy tuning.

- Important notes if any  
WAF Insights is currently in public preview and may not be suitable for production-critical environments. Integration with Azure Monitor and Log Analytics allows for enhanced analysis and alerting. Users should review preview documentation and test features before broad adoption. Access is available through the Azure Portal for supported Application Gateway WAF deployments.

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=557416

**Details**:

**Azure Update Report: Public Preview – WAF Insights for Application Gateway**

**Background and Purpose of the Update:**  
Azure Application Gateway’s Web Application Firewall (WAF) is a critical component for protecting web applications from common threats and vulnerabilities. Traditionally, analyzing WAF activity required manual log inspection and custom dashboard creation, which could be time-consuming and inefficient. The introduction of WAF Insights addresses the need for a streamlined, interactive, and comprehensive monitoring experience, enabling IT professionals to quickly investigate security events and optimize their WAF configurations.

**Specific Features and Detailed Changes:**  
With the public preview of WAF Insights, Azure Application Gateway WAF now provides an interactive interface for viewing WAF logs and metrics. Key features include:
- **Interactive Log and Metric Visualization:** Users can access a graphical and filterable view of WAF activity, including blocked requests and attack patterns.
- **Quick Investigation Tools:** The interface allows for rapid identification and analysis of blocked requests, enabling faster incident response and troubleshooting.
- **Attack Pattern Analysis:** WAF Insights surfaces trends and patterns in incoming threats, helping teams understand attack vectors and adjust security rules accordingly.

**Technical Mechanisms and Implementation Methods:**  
WAF Insights leverages Azure’s monitoring and analytics infrastructure to aggregate and visualize WAF logs and metrics. The solution likely integrates with Azure Monitor and Log Analytics workspaces, providing a dashboard-driven experience. Data is collected from Application Gateway WAF diagnostic logs and performance metrics, which are then processed and presented in an interactive format. This enables users to filter, search, and drill down into specific events or timeframes directly from the Azure portal.

**Use Cases and Application Scenarios:**  
- **Security Incident Investigation:** Security teams can quickly identify and analyze blocked requests, reducing the mean time to detect (MTTD) and respond (MTTR) to web attacks.
- **Threat Pattern Analysis:** IT professionals can monitor and report on attack trends, such as SQL injection or cross-site scripting attempts, to inform security posture adjustments.
- **Compliance and Reporting:** Organizations can generate detailed reports on WAF activity for compliance audits or internal security reviews.
- **Operational Monitoring:** DevOps and IT operations teams can proactively monitor WAF effectiveness and ensure that legitimate traffic is not being inadvertently blocked.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As WAF Insights is in public preview, features may be subject to change, and production workloads should be monitored accordingly.
- **Feature Scope:** The update specifically enhances visibility into WAF logs and metrics for Application Gateway; it does not introduce new WAF rules or detection capabilities.
- **Data Retention and Access:** Users should ensure that diagnostic logging is enabled and that appropriate permissions are configured for accessing WAF Insights.
- **Integration Requirements:** Full functionality may require integration with Azure Monitor and Log Analytics, and associated costs may apply.

**Integration with Related Azure Services:**  
WAF Insights is designed to work seamlessly with Azure Application Gateway and its WAF capabilities. It likely integrates with Azure Monitor for metric collection and Log Analytics for log aggregation and querying. This enables IT professionals to leverage existing Azure monitoring tools and workflows, including alerting, dashboarding, and automation, to enhance their security operations.

**Summary Sentence:**  
The public preview of WAF Insights for Azure Application Gateway introduces an interactive, integrated interface for visualizing WAF logs and metrics, enabling IT professionals to efficiently investigate blocked requests, analyze attack patterns, and enhance their web application security monitoring within the Azure ecosystem.

---


*This report was automatically generated - 2026-02-24 03:02:18 UTC*