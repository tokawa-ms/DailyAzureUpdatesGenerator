# February 06, 2026 - Azure Updates Summary Report (Standard Mode)

**Generated on**: February 06, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Standard Mode
**Number of updates**: 5 items

## Update List

### 1. [In development] Private Preview: Vaulted Backups for Azure Disk

**Published**: February 06, 2026 23:00:02 UTC
**Link**: [[In development] Private Preview: Vaulted Backups for Azure Disk](https://azure.microsoft.com/updates?id=555184)

**Categories**: In development, Management and governance, Storage, Azure Backup, Features

**Summary**:

- What was updated  
Azure is introducing a Private Preview for Vaulted Backups for Azure Disk.

- Key changes or new features  
Previously, Azure Disk Backup protected data using crash-consistent snapshots stored within the same subscription and tenant (Operational Tier). The new Vaulted Backups feature allows backups of Azure Disks to be stored in an Azure Recovery Services vault, providing an additional layer of protection. This enables long-term retention, enhanced security, and protection against accidental deletion or ransomware attacks. Vaulted Backups are managed separately from the source disks and support backup and restore operations independent of the original resource group or subscription.

- Target audience affected  
Developers and IT professionals managing Azure Disk resources, especially those with compliance, long-term retention, or advanced data protection requirements.

- Important notes if any  
Vaulted Backups for Azure Disk is currently in Private Preview and may require registration to access. This feature is particularly relevant for organizations needing to meet regulatory compliance, implement disaster recovery strategies, or enhance data security. Existing backup workflows using the Operational Tier remain unchanged; Vaulted Backups offer an additional, more secure backup option. For more details and to request access, refer to the official Azure Update page.

**Details**:

Today, Azure Disk Backup protects data by taking regular, crash-consistent snapshots of Azure Disks. These snapshots are stored within your subscription and tenant in a resource group, referred to as the Operational Tier in Azure Backup. This enables fast

---

### 2. [In preview] Public Preview: Azure Monitor pipeline transformations

**Published**: February 06, 2026 22:45:47 UTC
**Link**: [[In preview] Public Preview: Azure Monitor pipeline transformations](https://azure.microsoft.com/updates?id=555488)

**Categories**: In preview, DevOps, Management and governance, Azure Monitor, Security, Features

**Summary**:

- What was updated  
Azure Monitor has introduced the pipeline transformations feature in Public Preview.

- Key changes or new features  
The new pipeline transformations feature allows users to modify and shape telemetry data before it is ingested into Azure Monitor. This enables filtering, transformation, and enrichment of telemetry at the data pipeline level. Key benefits include better control over data ingestion costs, improved data quality, and simplified analytics by ensuring only relevant and well-structured data is stored and analyzed.

- Target audience affected  
This update is relevant to developers, IT professionals, and DevOps teams who use Azure Monitor for collecting and analyzing telemetry data from applications and infrastructure.

- Important notes if any  
Pipeline transformations are currently in Public Preview and may not be suitable for production workloads. Users can leverage this feature to optimize monitoring costs and streamline data management. Review the documentation for supported transformation scenarios and limitations during the preview phase.

Data source: Using RSS data  
Link: https://azure.microsoft.com/updates?id=555488

**Details**:

Azure Monitor pipeline transformations feature
is now Public Preview! This feature enables users to shape telemetry before
it’s ingested into Azure Monitor, helping them control ingestion costs, improve
data quality, and simplify analytics at scale.Built

---

### 3. [Launched] ​Generally Available: Claude Opus 4.6 now available on Azure Databricks

**Published**: February 06, 2026 19:00:01 UTC
**Link**: [[Launched] ​Generally Available: Claude Opus 4.6 now available on Azure Databricks](https://azure.microsoft.com/updates?id=555981)

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks now offers general availability of Anthropic Claude Opus 4.6 via Mosaic AI Model Serving.

- Key changes or new features  
Claude Opus 4.6, Anthropic’s most advanced AI model, is now integrated with Azure Databricks. It provides state-of-the-art capabilities in agentic coding, complex reasoning, and advanced knowledge work. Developers can now access and deploy this model directly within Databricks workflows, enabling enhanced AI-powered applications, automation, and analytics.

- Target audience affected  
Developers, data scientists, and IT professionals using Azure Databricks, especially those building AI/ML solutions or integrating advanced language models into their data pipelines and applications.

- Important notes if any  
To leverage Claude Opus 4.6, users must utilize Mosaic AI Model Serving within Azure Databricks. This update enables seamless integration of cutting-edge AI capabilities, supporting advanced use cases such as code generation, reasoning tasks, and complex knowledge work. Review Azure Databricks documentation for deployment details and best practices.  
More information: [Azure Update Link](https://azure.microsoft.com/updates?id=555981)

**Details**:

Azure Databricks now supports Anthropic Claude Opus 4.6 through Mosaic AI Model serving. Claude Opus 4.6 is Anthropic's most advanced model, delivering state-of-the-art performance on agentic coding, complex reasoning, and knowledge work tasks. The model

---

### 4. [In development] Private Preview: New planned datacenter region in Thailand (Thailand South)

**Published**: February 06, 2026 19:00:01 UTC
**Link**: [[In development] Private Preview: New planned datacenter region in Thailand (Thailand South)](https://azure.microsoft.com/updates?id=553999)

**Categories**: In development, Regions & Datacenters

**Summary**:

- What was updated  
Microsoft has announced the intent to establish a new Azure datacenter region in Thailand (Thailand South), currently in private preview.

- Key changes or new features  
The new Thailand South region will provide local access to Microsoft’s hyperscale cloud services, including Azure, Microsoft 365, and Dynamics 365. This expansion aims to deliver improved enterprise-grade reliability, performance, and compliance for customers in Thailand and the broader Southeast Asia region.

- Target audience affected  
Developers, IT professionals, and organizations operating in or serving customers in Thailand and Southeast Asia who require local data residency, lower latency, and enhanced compliance capabilities.

- Important notes if any  
The Thailand South datacenter region is in private preview, with general availability timelines to be announced. Customers interested in early access or migration planning should monitor future updates. This expansion supports data residency, business continuity, and regulatory compliance needs for industries such as finance, government, and healthcare. For more details, refer to the official Azure updates page: https://azure.microsoft.com/updates?id=553999

**Details**:

Microsoft is announcing our intent to establish
a new datacenter region in Thailand. The datacenter region will expand the
availability of Microsoft’s hyperscale cloud services in the region,
facilitating enterprise-grade reliability, performance, and com

---

### 5. [Launched] Generally Available: AMD v6 confidential VMs in new regions for January 2026

**Published**: February 06, 2026 01:00:02 UTC
**Link**: [[Launched] Generally Available: AMD v6 confidential VMs in new regions for January 2026](https://azure.microsoft.com/updates?id=553966)

**Categories**: Launched, Compute, Virtual Machines, Regions & Datacenters

**Summary**:

- What was updated  
The AMD-based DCa/ECa v6 series confidential virtual machines (VMs) are now generally available in 11 additional Azure regions as of January 2026.

- Key changes or new features  
These confidential VMs, designed for enhanced security and data protection, are now available in the following regions: Canada Central, Canada East, Norway East, Norway West, Italy North, Germany North, France South, Australia East, West US, West US 3, and Germany West Central. The VMs leverage AMD hardware-based security features, enabling confidential computing workloads with memory encryption and isolation.

- Target audience affected  
Developers and IT professionals who require confidential computing capabilities for sensitive workloads, especially those needing regional availability for compliance or latency reasons.

- Important notes if any  
The expanded regional availability allows organizations to deploy confidential workloads closer to their users or in compliance with data residency requirements. Developers can use these VMs for applications that handle sensitive data, such as financial, healthcare, or regulated industry solutions. Review the official documentation for supported features and best practices when deploying confidential VMs in these regions.

[More details](https://azure.microsoft.com/updates?id=553966)

**Details**:

DCa/ECa v6 series AMD based confidential virtual machines are now generally available in 11 new regions: Canada Central, Canada East, Norway East, Norway West, Italy North, Germany North, France South, Australia East, West US, West US 3, Germany West Cent

---


*This report was automatically generated - 2026-02-15 16:34:56 UTC*