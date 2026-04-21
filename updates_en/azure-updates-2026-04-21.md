# April 21, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 21, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Azure Monitor supports native OTLP ingestion using the Azure Monitor Agent 

**Published**: April 20, 2026 17:30:53 UTC
**Link**: [Public Preview: Azure Monitor supports native OTLP ingestion using the Azure Monitor Agent ](https://azure.microsoft.com/updates?id=560530)

**Update ID**: 560530
**Data source**: Azure Updates API

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Open Source

**Summary**:

- What was updated  
Azure Monitor now supports native ingestion of OpenTelemetry Protocol (OTLP) signals via the Azure Monitor Agent (AMA), currently in public preview.

- Key changes or new features  
Developers can now send telemetry data (traces, metrics, and logs) directly from OpenTelemetry-instrumented applications to Azure Monitor using OTLP, without needing additional exporters or conversion layers. The Azure Monitor Agent acts as the receiver for OTLP data and forwards it to Azure Monitor for analysis and visualization.

- Target audience affected  
This update primarily impacts developers and IT professionals who use OpenTelemetry for application monitoring, as well as those managing observability and telemetry pipelines in Azure environments.

- Important notes if any  
- This feature is in public preview and may not be suitable for production workloads yet.  
- Native OTLP support simplifies integration with OpenTelemetry SDKs and agents, reducing operational overhead and complexity.  
- Existing applications using OpenTelemetry can now send data directly to Azure Monitor, streamlining observability workflows.  
- Review Azure Monitor Agent and OTLP documentation for setup instructions and supported scenarios.

[Read more](https://azure.microsoft.com/updates?id=560530)

**Details**:

**Background and Purpose of the Update**  
Azure Monitor is a comprehensive monitoring solution for collecting, analyzing, and acting on telemetry from cloud and on-premises environments. With the increasing adoption of OpenTelemetry, a popular open-source observability framework, organizations require seamless integration between their instrumented applications and Azure Monitor. The purpose of this update is to enable native ingestion of OpenTelemetry Protocol (OTLP) signals directly into Azure Monitor, simplifying telemetry collection and enhancing observability for modern applications.

**Specific Features and Detailed Changes**  
This update introduces native support for OTLP ingestion via the Azure Monitor Agent (AMA). Key features include:
- **Direct OTLP Ingestion:** Applications instrumented with OpenTelemetry can now send telemetry data (traces, metrics, logs) directly to Azure Monitor through AMA without the need for additional collectors or protocol translation layers.
- **Simplified Telemetry Pipeline:** The process of exporting telemetry from applications to Azure Monitor is streamlined, reducing operational complexity and potential points of failure.

**Technical Mechanisms and Implementation Methods**  
- **Azure Monitor Agent (AMA):** AMA is the unified agent for data collection in Azure Monitor. With this update, AMA can now receive OTLP signals natively from applications.
- **OTLP Protocol Support:** The agent listens for OTLP signals over supported transport protocols, processes the telemetry, and exports it to Azure Monitor.
- **Application Instrumentation:** Developers instrument their applications using OpenTelemetry SDKs, configuring them to export telemetry to the endpoint exposed by AMA.

**Use Cases and Application Scenarios**  
- **Cloud-Native Applications:** Teams building microservices or distributed systems with OpenTelemetry can now export telemetry directly to Azure Monitor, enabling end-to-end observability.
- **Hybrid Environments:** Organizations running workloads across cloud and on-premises can standardize on OpenTelemetry for instrumentation and leverage Azure Monitor for centralized monitoring.
- **DevOps and SRE:** Operations teams can use this integration to gain unified visibility into application performance, reliability, and usage patterns.

**Important Considerations and Limitations**  
- **Public Preview:** This feature is currently in public preview, which means it may not be suitable for production workloads and could be subject to changes.
- **Supported Signals and Protocols:** Only OTLP signals are supported natively; other telemetry formats may require separate ingestion paths.
- **Agent Configuration:** Proper configuration of AMA and network settings is required to ensure secure and reliable telemetry delivery.
- **Compatibility:** Ensure that the OpenTelemetry SDKs and exporters in use are compatible with the supported OTLP versions by AMA.

**Integration with Related Azure Services**  
- **Azure Monitor:** Ingested telemetry is available within Azure Monitor for analysis, alerting, and visualization.
- **Log Analytics:** Collected data can be queried and analyzed using Log Analytics workspaces.
- **Azure Application Insights:** Telemetry can be surfaced in Application Insights for application performance monitoring.
- **Azure Security and Compliance:** Data collected via AMA adheres to Azure’s security and compliance standards.

**Summary**  
Azure Monitor now supports native ingestion of OpenTelemetry Protocol (OTLP) signals via the Azure Monitor Agent, enabling direct telemetry export from OpenTelemetry-instrumented applications to Azure Monitor for enhanced observability.

---


*This report was automatically generated - 2026-04-21 03:01:42 UTC*