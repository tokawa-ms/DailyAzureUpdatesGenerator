# January 31, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: January 31, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: "Send data to Event Hubs & Storage (Preview)" retiring July 31, 2026

**Published**: January 30, 2026 18:30:02 UTC
**Link**: [Retirement: "Send data to Event Hubs & Storage (Preview)" retiring July 31, 2026](https://azure.microsoft.com/updates?id=551523)

**Update ID**: 551523
**Data source**: Azure Updates API

**Categories**: DevOps, Management and governance, Azure Monitor

**Summary**:

- What was updated  
Microsoft announced the retirement of the preview feature “Send virtual machine client data to Event Hubs and Storage (Preview)” effective July 31, 2026.

- Key changes or new features  
After this date, the feature will no longer be supported. Users will be unable to create new data collection rules leveraging this capability. Existing configurations using this preview feature may cease to function or receive support.

- Target audience affected  
Developers and IT professionals who use Azure Monitor or related services to route VM client data to Event Hubs or Azure Storage via this preview feature will be impacted. Those relying on this for data ingestion, analytics, or integration workflows must plan accordingly.

- Important notes if any  
Microsoft recommends transitioning to supported alternatives for sending VM client data to Event Hubs or Storage before the retirement date to avoid disruption. Review current data collection rules and update architectures to ensure continuity. No new data collection rules using this preview feature can be created after the retirement date.

**Details**:

The Azure update announces the retirement of the preview feature “Send virtual machine client data to Event Hubs and Storage (Preview)” effective July 31, 2026. This feature, introduced to facilitate direct streaming of VM client data to Azure Event Hubs and Azure Storage, will no longer be supported, and creation of new data collection rules using this capability will be disabled prior to retirement.

**Background and Purpose**  
This preview feature was designed to enable IT professionals and developers to collect and stream telemetry and diagnostic data directly from Azure virtual machines to Event Hubs and Storage accounts. The primary goal was to simplify data ingestion pipelines for monitoring, analytics, and custom processing scenarios by allowing VM client data to be sent seamlessly to these endpoints. The retirement indicates a strategic shift, possibly due to the feature’s preview status, evolving platform capabilities, or the availability of more robust alternatives.

**Specific Features and Detailed Changes**  
While active, the feature allowed users to create data collection rules that specify VM client data sources and direct their output to Event Hubs or Storage accounts. This enabled real-time or batch processing scenarios leveraging Event Hubs’ event streaming capabilities or Storage’s durable data retention. Post-retirement, no new data collection rules utilizing this feature can be created, and existing rules will cease to function after July 31, 2026. Microsoft will discontinue support, meaning no further updates, bug fixes, or technical assistance will be provided.

**Technical Mechanisms and Implementation Methods**  
The feature operated by configuring data collection rules within Azure Monitor or related management layers, which then installed or configured agents or extensions on the target VMs. These agents collected client-side telemetry—such as performance counters, logs, or custom metrics—and forwarded them to Event Hubs or Storage endpoints as specified. Event Hubs acted as a high-throughput, low-latency event ingestion service, suitable for streaming analytics or integration with services like Azure Stream Analytics, while Storage provided persistent blob storage for archival or batch processing.

**Use Cases and Application Scenarios**  
Typical use cases included centralized monitoring of VM health and performance, custom telemetry ingestion pipelines, integration with SIEM (Security Information and Event Management) systems, and feeding data into big data analytics platforms. Organizations leveraging real-time event processing or long-term storage of VM-generated data benefited from this direct data routing capability. The retirement necessitates migrating these workflows to alternative supported methods.

**Important Considerations and Limitations**  
IT professionals must plan to transition away from this preview feature well before the July 31, 2026 deadline. Existing data collection rules should be reviewed and replaced with supported configurations to avoid data loss or monitoring gaps. Since the feature was in preview, it may have had limitations in scalability, feature completeness, or integration depth compared to GA services. The lack of ongoing support post-retirement means any operational issues cannot be escalated to Microsoft.

**Integration with Related Azure Services**  
This feature was closely integrated with Azure Monitor’s data collection framework, Azure Event Hubs for event streaming, and Azure Storage for data persistence. Post-retirement, users are encouraged to utilize Azure Monitor’s fully supported data collection rules and diagnostic settings, Azure Monitor Agent (AMA), and native integrations with Event Hubs and Storage. Alternatives such as Azure Diagnostics extension, Azure Monitor Logs, and Azure Data Factory pipelines may provide more robust and supported mechanisms for VM telemetry ingestion and processing.

**Summary**  
Microsoft will retire the “Send virtual machine client data to Event Hubs and Storage (Preview)” feature on July 31, 2026, ceasing support and disabling new data collection rule creation for this capability; IT professionals should proactively migrate existing telemetry ingestion workflows to supported Azure Monitor and data integration services to ensure continuity of VM client data streaming and storage.

---


*This report was automatically generated - 2026-01-31 03:01:23 UTC*