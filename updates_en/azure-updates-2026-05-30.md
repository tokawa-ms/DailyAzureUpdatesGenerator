# May 30, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 30, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: AI Services Metrics Advisor is retired as of May 18, 2026

**Published**: May 29, 2026 19:00:24 UTC
**Link**: [Retirement: AI Services Metrics Advisor is retired as of May 18, 2026](https://azure.microsoft.com/updates?id=ai-services-metrics-advisor-will-be-retired-on-1-october-2026)

**Update ID**: ai-services-metrics-advisor-will-be-retired-on-1-october-2026
**Data source**: Azure Updates API

**Categories**: Services, Retirements

**Summary**:

- What was updated  
Azure AI Metrics Advisor has been officially retired as of May 18, 2026.

- Key changes or new features  
The Metrics Advisor service will no longer be available or supported after this date. Microsoft recommends transitioning to Azure Monitor, which offers anomaly detection and analysis capabilities through various interfaces.

- Target audience affected  
Developers and IT professionals currently using Azure AI Metrics Advisor for time-series data monitoring, anomaly detection, and diagnostics.

- Important notes if any  
Existing Metrics Advisor users must migrate their solutions to Azure Monitor or other alternatives before the retirement date to avoid service disruption. Azure Monitor provides similar anomaly detection and analytics features and is the recommended path forward. Review your current dependencies on Metrics Advisor and plan your migration strategy accordingly. For more details and migration guidance, refer to the official Azure documentation.  
[More information](https://azure.microsoft.com/updates?id=ai-services-metrics-advisor-will-be-retired-on-1-october-2026)

**Details**:

**Azure Update Report: Retirement of AI Services Metrics Advisor as of May 18, 2026**

**Background and Purpose of the Update**  
As of May 18, 2026, Azure AI Metrics Advisor has been officially retired. This update is part of Azure’s ongoing service lifecycle management, ensuring that customers transition to more current and supported solutions. The retirement aims to streamline Azure’s AI service offerings and direct users toward alternative solutions that provide robust anomaly detection and analysis capabilities.

**Specific Features and Detailed Changes**  
The primary change is the discontinuation of the Azure AI Metrics Advisor service. After the retirement date, users will no longer be able to access or utilize Metrics Advisor for anomaly detection, time-series monitoring, or root cause analysis. Existing integrations, APIs, and dashboards dependent on Metrics Advisor will cease to function. Microsoft recommends transitioning to Azure Monitor, which now offers anomaly detection and analysis through several interfaces.

**Technical Mechanisms and Implementation Methods**  
Azure AI Metrics Advisor previously provided advanced time-series anomaly detection, incident management, and diagnostics using AI models tailored for telemetry data. With its retirement, users are directed to Azure Monitor, which integrates anomaly detection capabilities via built-in features and APIs. Azure Monitor leverages machine learning models to analyze telemetry data, detect anomalies, and generate alerts. The transition involves reconfiguring data pipelines, updating alerting mechanisms, and potentially refactoring custom integrations to utilize Azure Monitor’s APIs and interfaces.

**Use Cases and Application Scenarios**  
Typical use cases for Metrics Advisor included monitoring application performance, detecting anomalies in business metrics, and automating incident response for operational telemetry. Post-retirement, these scenarios should be migrated to Azure Monitor. Azure Monitor supports similar application monitoring, infrastructure telemetry analysis, and alerting workflows, ensuring continuity for IT operations, DevOps, and business intelligence teams.

**Important Considerations and Limitations**  
- **Service Discontinuation:** After May 18, 2026, Metrics Advisor will be inaccessible. All dependent applications and workflows must be migrated before this date to avoid service disruption.
- **Feature Parity:** While Azure Monitor provides anomaly detection, users should verify that all required features and integrations are supported in Azure Monitor, as some advanced diagnostics or root cause analysis features may differ.
- **Migration Planning:** Transitioning to Azure Monitor may require changes to data ingestion, alert configuration, and dashboarding. Testing and validation are essential to ensure operational continuity.
- **Documentation and Support:** Users should consult Azure’s official migration guides and support resources for best practices and detailed migration steps.

**Integration with Related Azure Services**  
Azure Monitor integrates seamlessly with other Azure services such as Azure Log Analytics, Application Insights, and Azure Alerts. This enables centralized monitoring, unified alerting, and comprehensive telemetry analysis across Azure resources. Existing data sources and monitoring agents can be reconfigured to send telemetry to Azure Monitor, ensuring minimal disruption during migration.

**Summary**  
Azure AI Metrics Advisor is retired as of May 18, 2026; users are advised to migrate to Azure Monitor for continued anomaly detection and analysis capabilities.

---

### 2. Public Preview: Azure Site Recovery Support for Performance Plus Managed Disks

**Published**: May 29, 2026 15:15:43 UTC
**Link**: [Public Preview: Azure Site Recovery Support for Performance Plus Managed Disks](https://azure.microsoft.com/updates?id=564644)

**Update ID**: 564644
**Data source**: Azure Updates API

**Categories**: In preview, Management and governance, Migration, Azure Site Recovery, Features, Management

**Summary**:

- What was updated  
Azure Site Recovery (ASR) now supports the replication of virtual machines (VMs) using Performance Plus enabled managed disks in Public Preview.

- Key changes or new features  
ASR can now replicate VMs that use Premium SSD, Standard SSD, or Standard HDD managed disks with the Performance Plus capability. Performance Plus disks offer enhanced throughput and IOPS, making them suitable for high-performance workloads. This update enables disaster recovery for VMs leveraging these high-performance disks, ensuring business continuity for critical applications.

- Target audience affected  
This update is relevant to IT professionals and developers responsible for business continuity, disaster recovery, and high-performance workloads in Azure. Organizations using or planning to use Performance Plus managed disks for their VMs can now include these resources in their ASR-based disaster recovery strategies.

- Important notes if any  
This feature is currently in Public Preview and may not be recommended for production workloads until General Availability. Users should review the official documentation for any limitations or prerequisites before enabling replication for Performance Plus disks. For more details, refer to the official Azure Update announcement: https://azure.microsoft.com/updates?id=564644

**Details**:

**Azure Update Report: Public Preview – Azure Site Recovery Support for Performance Plus Managed Disks**

**Background and Purpose of the Update**  
Azure Site Recovery (ASR) is a disaster recovery solution that enables replication, failover, and recovery of workloads running on Azure virtual machines (VMs). The introduction of Performance Plus managed disks addresses the need for enhanced disk performance and scalability in cloud environments. This update extends ASR’s replication capabilities to include VMs utilizing Performance Plus enabled managed disks, specifically Premium SSD, Standard SSD, and Standard HDD disks. The purpose is to ensure that organizations leveraging Performance Plus disks for high-performance workloads can now protect these workloads using ASR’s disaster recovery features.

**Specific Features and Detailed Changes**  
With this update, ASR now supports replication of Azure VMs that are provisioned with Performance Plus enabled managed disks. The supported disk types include:
- Premium SSD (with Performance Plus capability)
- Standard SSD (with Performance Plus capability)
- Standard HDD (with Performance Plus capability)

This enhancement allows organizations to configure replication for VMs that require higher throughput and IOPS, as provided by Performance Plus disks, ensuring that these VMs can be included in disaster recovery plans without compromising on performance.

**Technical Mechanisms and Implementation Methods**  
ASR leverages Azure’s native disk replication mechanisms to facilitate disaster recovery. When Performance Plus managed disks are enabled on a VM, ASR can now replicate the disk data to a secondary region or recovery site. This is achieved by integrating the Performance Plus disk features into the ASR replication pipeline, ensuring that disk performance characteristics are preserved during replication and failover operations. The replication process is managed through the ASR portal, where users can select VMs with Performance Plus disks and configure replication policies as usual.

**Use Cases and Application Scenarios**  
- **High-performance workloads:** Enterprises running mission-critical applications that require high disk throughput and low latency can now use ASR for disaster recovery without sacrificing performance.
- **Database servers:** SQL Server, Oracle, or other database workloads using Performance Plus disks can be protected with ASR.
- **Large-scale analytics:** VMs processing large datasets with Performance Plus disks can be replicated for business continuity.
- **General VM protection:** Any VM using Premium SSD, Standard SSD, or Standard HDD with Performance Plus can be included in ASR recovery plans.

**Important Considerations and Limitations**  
- This feature is currently in Public Preview, which means it may not be suitable for production environments until General Availability.
- Only managed disks with Performance Plus capability are supported; ensure that your VM disks are provisioned accordingly.
- As with all ASR features, replication may incur additional costs based on storage and network usage.
- Compatibility with other Azure features and services should be verified, especially if custom configurations or advanced disk features are used.

**Integration with Related Azure Services**  
ASR integrates seamlessly with Azure managed disks and VM infrastructure. The update ensures that Performance Plus disk capabilities are supported in disaster recovery scenarios. ASR can be used alongside Azure Backup, Azure Monitor, and other management services to provide comprehensive protection and monitoring for VMs using Performance Plus disks.

**Summary Sentence**  
Azure Site Recovery now supports replication of virtual machines using Performance Plus enabled managed disks (Premium SSD, Standard SSD, Standard HDD), allowing organizations to include high-performance workloads in their disaster recovery plans during the Public Preview phase.

---


*This report was automatically generated - 2026-05-30 03:01:14 UTC*