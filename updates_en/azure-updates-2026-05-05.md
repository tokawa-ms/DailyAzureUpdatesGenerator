# May 05, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 05, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Cleanup legacy AlternateId usage to ensure continued service

**Published**: May 04, 2026 17:45:58 UTC
**Link**: [Generally Available: Cleanup legacy AlternateId usage to ensure continued service](https://azure.microsoft.com/updates?id=561432)

**Update ID**: 561432
**Data source**: Azure Updates API

**Categories**: Launched, Mobile, Web, Azure Communication Services, Features

**Summary**:

**What was updated**  
Azure Communication Services (ACS) and Teams Phone Multi-line feature now require cleanup of legacy AlternateId usage to ensure continued service.

**Key changes or new features**  
Microsoft has identified an issue where legacy AlternateId implementations in customer environments can impact the Multi-line (Multiple Number Assignment) feature for Teams Phone enablement. The update mandates customers to remove or update legacy AlternateId usage in their internal ACS implementations to prevent service disruptions.

**Target audience affected**  
This update is relevant for developers and IT professionals managing Azure Communication Services, especially those integrating Teams Phone with Multi-line capabilities and using AlternateId in their solutions.

**Important notes**  
- Continued use of legacy AlternateId may cause issues with Teams Phone Multi-line functionality.
- Immediate action is recommended: review and clean up any legacy AlternateId usage in your ACS implementations.
- This update is now generally available, and failure to comply may result in service interruptions or degraded functionality for Teams Phone features.
- Refer to Microsoft documentation for guidance on proper AlternateId usage and migration steps.

[Read more](https://azure.microsoft.com/updates?id=561432)

**Details**:

**Azure Update Technical Explanation**

**Title:** Generally Available: Cleanup legacy AlternateId usage to ensure continued service

**Background and Purpose of the Update:**  
This update addresses an identified issue affecting the Multi-line (Multiple Number Assignment) feature for Teams Phone enablement, specifically related to the use of AlternateId in customer internal implementations for Azure Communication Services (ACS). AlternateId is a Microsoft identifier mechanism previously used in certain integration scenarios. The purpose of this update is to prompt customers to clean up legacy usage of AlternateId to ensure uninterrupted service and compatibility with current Azure Communication Services and Teams Phone features.

**Specific Features and Detailed Changes:**  
- The update marks the general availability of guidance and tools to assist customers in identifying and removing legacy AlternateId dependencies from their ACS implementations.
- It specifically targets scenarios where AlternateId is used for managing multiple phone numbers (Multi-line) within Teams Phone, which can lead to service issues if not addressed.
- The update does not introduce new features but focuses on remediation and compliance with the latest service requirements.

**Technical Mechanisms and Implementation Methods:**  
- Customers are expected to audit their internal ACS implementations for any reference or reliance on AlternateId.
- The remediation process involves replacing or removing AlternateId usage according to Microsoft’s latest integration patterns for Teams Phone and ACS.
- Detailed steps and best practices for the cleanup process are provided in the official guidance linked in the update.
- The update ensures that after cleanup, services will continue to operate as intended without disruption due to deprecated identifier mechanisms.

**Use Cases and Application Scenarios:**  
- Organizations that have enabled Teams Phone with Multi-line support using Azure Communication Services and have implemented custom logic involving AlternateId.
- IT professionals managing telephony integrations, number assignment, and identity management within Teams and ACS environments.
- Enterprises preparing for future enhancements or compliance checks related to Teams Phone and ACS interoperability.

**Important Considerations and Limitations:**  
- Failure to remove legacy AlternateId usage may result in service disruptions or loss of Multi-line functionality in Teams Phone.
- The update is relevant only to customers who have implemented custom solutions using AlternateId within ACS; standard deployments without such customizations are not affected.
- It is critical to follow the official guidance to avoid accidental service interruptions during the cleanup process.

**Integration with Related Azure Services:**  
- The update directly impacts Azure Communication Services and Microsoft Teams Phone integrations.
- It may also affect related identity management and telephony services that interact with ACS or Teams Phone through custom implementations.
- No changes are required for other Azure services unless they are part of the affected integration scenario.

**Summary:**  
Microsoft has announced the general availability of guidance to help customers clean up legacy AlternateId usage in Azure Communication Services implementations, ensuring continued and uninterrupted service for Teams Phone Multi-line features.

---

### 2. Generally Available: Azure Functions durable task scheduler Consumption SKU

**Published**: May 04, 2026 17:45:58 UTC
**Link**: [Generally Available: Azure Functions durable task scheduler Consumption SKU](https://azure.microsoft.com/updates?id=560957)

**Update ID**: 560957
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
The Azure Functions Durable Task Scheduler Consumption SKU is now generally available.

- Key changes or new features  
This release enables developers to run durable workflows and AI agent orchestrations on Azure using a pay-per-use (consumption-based) pricing model. There is no need to provision or manage underlying storage, plan for capacity, or pay for idle resources. Billing is based solely on actual usage, making it cost-effective for variable workloads.

- Target audience affected  
Developers building serverless workflows, AI agent orchestrations, and event-driven applications; IT professionals managing Azure Functions and workflow automation.

- Important notes if any  
The Consumption SKU removes the overhead of managing storage and capacity, simplifying operations and reducing costs for dynamic or unpredictable workloads. It is particularly beneficial for teams looking to scale durable workflows without pre-provisioning infrastructure. Existing Durable Task Scheduler users can consider migrating to the Consumption SKU for improved cost efficiency and operational simplicity.

For more details, see the official update: https://azure.microsoft.com/updates?id=560957

**Details**:

**Azure Update Report: Generally Available – Azure Functions Durable Task Scheduler Consumption SKU**

**Background and Purpose of the Update**  
The general availability of the Azure Functions Durable Task Scheduler Consumption SKU addresses the need for scalable, cost-efficient orchestration of durable workflows and AI agent orchestrations in the cloud. Previously, running durable workflows often required managing dedicated resources, planning capacity, and handling storage, which introduced complexity and potential idle costs. This update aims to simplify the deployment and operation of durable workflows by introducing a pay-per-use pricing model, eliminating the need for infrastructure management.

**Specific Features and Detailed Changes**  
- **Consumption-Based Pricing:** The Consumption SKU introduces a pay-per-use billing model, ensuring users are only charged for actual resource consumption during workflow execution. There are no charges for idle time or unused capacity.
- **No Storage Management:** Users are relieved from provisioning or managing storage resources for workflow state management, as this is abstracted by the platform.
- **No Capacity Planning:** The platform automatically handles scaling, so there is no need to estimate or reserve execution capacity in advance.
- **No Idle Costs:** Costs are incurred only when workflows are actively running, reducing unnecessary expenditure.

**Technical Mechanisms and Implementation Methods**  
The Durable Task Scheduler Consumption SKU leverages the serverless architecture of Azure Functions. When a durable workflow or AI agent orchestration is triggered, the platform dynamically allocates compute resources and manages the execution lifecycle. State management, checkpointing, and orchestration are handled internally, removing the need for explicit storage configuration. The system automatically scales resources up or down based on workload, ensuring efficient execution without manual intervention.

**Use Cases and Application Scenarios**  
- **Durable Workflows:** Automate long-running, stateful business processes such as order processing, approval workflows, and data integration pipelines.
- **AI Agent Orchestrations:** Coordinate multiple AI agents or microservices in complex decision-making or data processing scenarios, leveraging the orchestrator pattern.
- **Event-Driven Automation:** Implement event-driven architectures where workflows are triggered by external events, requiring reliable state management and execution without persistent infrastructure.
- **Cost-Optimized Batch Processing:** Run batch jobs or periodic tasks that do not require dedicated resources, benefiting from the absence of idle costs.

**Important Considerations and Limitations**  
- **Billing Model:** Users should understand the pay-per-use billing structure to accurately estimate costs based on workflow execution patterns.
- **Resource Abstraction:** While storage and capacity management are simplified, users have less control over the underlying infrastructure, which may impact advanced customization scenarios.
- **Platform Constraints:** The SKU is designed for scenarios where dynamic scaling and minimal management overhead are priorities; it may not be suitable for workloads requiring fixed resource allocation or specialized storage configurations.

**Integration with Related Azure Services**  
The Durable Task Scheduler Consumption SKU integrates seamlessly with other Azure Functions capabilities, enabling event-driven workflows triggered by Azure Event Grid, Service Bus, or HTTP requests. It can also be combined with Azure Logic Apps, Azure Storage, and other Azure services to build comprehensive, serverless automation and orchestration solutions.

**Summary Sentence**  
The Azure Functions Durable Task Scheduler Consumption SKU is now generally available, offering a serverless, pay-per-use solution for running durable workflows and AI agent orchestrations on Azure without the need for storage management, capacity planning, or incurring idle costs.

---


*This report was automatically generated - 2026-05-05 03:01:21 UTC*