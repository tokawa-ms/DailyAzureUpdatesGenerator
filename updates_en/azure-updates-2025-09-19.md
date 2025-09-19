# September 19, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 19, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Retirement: Licensing changes for future Azure VMware Solution subscriptions starting October 16, 2025.

**Published**: September 18, 2025 20:45:29 UTC
**Link**: [Retirement: Licensing changes for future Azure VMware Solution subscriptions starting October 16, 2025.](https://azure.microsoft.com/updates?id=503878)

**Update ID**: 503878
**Data source**: Azure Updates API

**Categories**: Compute, Azure VMware Solution, Retirements

**Summary**:

- What was updated  
Broadcom announced changes to VMware licensing policies affecting Azure VMware Solution (AVS) subscriptions starting October 16, 2025.

- Key changes or new features  
New customers subscribing to AVS on Azure must bring their own portable VMware Cloud Foundation (VCF) licenses. Microsoft will no longer provide bundled VMware licenses with AVS subscriptions for new customers. Existing AVS customers can continue using their current licensing arrangements without disruption.

- Target audience affected  
This update primarily impacts new AVS customers and developers or IT professionals planning to deploy VMware workloads on Azure after October 16, 2025. Existing AVS customers are not affected immediately but should plan for future licensing compliance.

- Important notes if any  
Organizations must procure portable VCF subscriptions directly from VMware or authorized resellers to use AVS after the cutoff date. This change aligns with Broadcom’s broader licensing strategy for hyperscaler platforms and may affect cost planning and procurement processes. Early planning is recommended to avoid service interruptions or compliance issues.  

For more details, visit: https://azure.microsoft.com/updates?id=503878

**Details**:

The Azure update titled "Retirement: Licensing changes for future Azure VMware Solution subscriptions starting October 16, 2025" reflects a significant shift in VMware licensing policy that impacts how new Azure VMware Solution (AVS) customers will procure and manage their VMware Cloud Foundation (VCF) licenses on Azure. This change is driven by Broadcom’s updated licensing model, which mandates that new customers must bring their own portable VCF subscriptions when deploying VMware workloads on hyperscaler platforms such as Azure.

**Background and Purpose of the Update**  
Broadcom, the owner of VMware, has revised its licensing strategy to require customers to independently acquire VMware Cloud Foundation licenses outside of hyperscaler-managed offerings. Previously, AVS subscriptions included bundled VMware licenses, simplifying procurement and management for customers. The update aims to align VMware licensing with Broadcom’s broader commercial policies, ensuring license portability and compliance across multi-cloud environments. This change affects only new AVS subscriptions starting October 16, 2025; existing customers with active AVS deployments can continue under their current licensing terms without disruption.

**Specific Features and Detailed Changes**  
- **Bring Your Own License (BYOL) Requirement:** New AVS customers must purchase portable VMware Cloud Foundation licenses directly from VMware or authorized resellers.  
- **No Bundled VMware Licenses:** Unlike current AVS offerings, new subscriptions will not include VMware licenses as part of the Azure service package.  
- **License Portability:** Customers gain the flexibility to use their VMware licenses across different hyperscalers or on-premises environments, supporting hybrid and multi-cloud strategies.  
- **Subscription Start Date:** The licensing change applies strictly to new AVS subscriptions initiated on or after October 16, 2025.

**Technical Mechanisms and Implementation Methods**  
From a technical perspective, customers will need to manage VMware license keys and compliance independently of Azure’s subscription management. During AVS deployment, customers must provide valid VMware Cloud Foundation license keys to activate and operate the VMware stack on Azure infrastructure. Azure will continue to provide the underlying infrastructure, networking, and management plane for AVS, but VMware license enforcement and compliance will be the customer’s responsibility. Azure portal and APIs may be updated to support license key input and validation workflows, but the core licensing enforcement remains within VMware’s software layer.

**Use Cases and Application Scenarios**  
- **Enterprises with Existing VMware Investments:** Organizations with existing VMware licenses can leverage BYOL to optimize costs and maintain license consistency across on-premises and cloud environments.  
- **Hybrid and Multi-Cloud Deployments:** Customers aiming for workload mobility across clouds benefit from portable licenses that are not tied to a single hyperscaler.  
- **New AVS Customers Post-October 2025:** These customers must plan license procurement separately and ensure compliance before deploying AVS workloads.

**Important Considerations and Limitations**  
- **License Procurement Complexity:** Customers must engage with VMware or resellers to acquire licenses, adding procurement overhead compared to the previous bundled model.  
- **Compliance Responsibility:** Customers bear full responsibility for license compliance, audits, and renewals.  
- **No Impact on Existing Customers:** Current AVS users are unaffected until they create new subscriptions after the cutoff date.  
- **Potential Cost Implications:** BYOL may affect total cost of ownership depending on licensing agreements and usage patterns.

**Integration with Related Azure Services**  
Azure VMware Solution will continue to integrate seamlessly with Azure networking (ExpressRoute, Azure Virtual WAN), Azure security services (Azure Security Center, Azure Sentinel), and Azure management tools (Azure Monitor, Azure Automation). The licensing change does not affect these integrations but requires customers to separately manage VMware licenses while leveraging Azure’s cloud-native services for infrastructure, monitoring, and security. Customers can also integrate AVS with Azure Arc for hybrid management, ensuring consistent governance across environments despite the licensing shift.

---

In summary, starting October 16, 2025, new Azure VMware Solution subscriptions will require customers to bring their own portable

---

### 2. Generally Available: DCa/ECa v6 series AMD based confidential virtual machines (VMs) 

**Published**: September 18, 2025 19:00:07 UTC
**Link**: [Generally Available: DCa/ECa v6 series AMD based confidential virtual machines (VMs) ](https://azure.microsoft.com/updates?id=502874)

**Update ID**: 502874
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Virtual Machines, Features

**Summary**:

- What was updated  
Microsoft has announced the general availability of the DCa/ECa v6 series AMD-based confidential virtual machines (VMs) in additional Azure regions.

- Key changes or new features  
The DCa/ECa v6 series VMs leverage 4th generation AMD EPYC processors and provide confidential computing capabilities using AMD SEV-SNP technology. These VMs enable hardware-based memory encryption to protect data in use, enhancing security for sensitive workloads. The update expands availability to UAE North, Korea Central, West Central US, South Africa North, Switzerland North, and UK South regions.

- Target audience affected  
Developers and IT professionals working with confidential computing, secure cloud workloads, and data protection in Azure will benefit from these new AMD-based confidential VM options. This is particularly relevant for industries with strict compliance and data privacy requirements.

- Important notes if any  
Users should consider the DCa/ECa v6 series for workloads requiring enhanced security without compromising performance. Availability in new regions improves geographic diversity for confidential computing deployments. For detailed pricing and sizing, consult the Azure portal or documentation.

**Details**:

Microsoft has announced the general availability of the DCa/ECa v6 series AMD-based confidential virtual machines (VMs) across multiple Azure regions including UAE North, Korea Central, West Central US, South Africa North, Switzerland North, and UK South. These VMs leverage 4th generation AMD EPYC processors and Azure confidential computing technologies to provide enhanced security and performance for sensitive workloads.

**Background and Purpose**  
Confidential computing addresses the growing need for protecting data in use, complementing data-at-rest and data-in-transit encryption. By enabling hardware-based Trusted Execution Environments (TEEs), confidential VMs isolate code and data from the host OS, hypervisor, and even Azure administrators, mitigating risks from insider threats and sophisticated attacks. The DCa/ECa v6 series expands Azure’s confidential computing portfolio by introducing AMD-based options, offering customers more choice and flexibility in confidential workload deployments.

**Specific Features and Detailed Changes**  
- **Processor:** Powered by 4th generation AMD EPYC processors, the DCa/ECa v6 VMs deliver improved compute performance, memory bandwidth, and energy efficiency compared to previous generations.  
- **Confidential Computing:** These VMs utilize AMD SEV-SNP (Secure Encrypted Virtualization - Secure Nested Paging) technology, which encrypts VM memory and enforces strong integrity protections, ensuring that data and code remain confidential and tamper-proof during execution.  
- **VM Sizes:** The DCa series targets general-purpose confidential workloads with balanced CPU-to-memory ratios, while the ECa series is optimized for memory-intensive confidential applications.  
- **Regional Availability:** The launch expands confidential VM availability to new Azure regions, enabling customers to deploy secure workloads closer to their users and comply with data residency requirements.

**Technical Mechanisms and Implementation Methods**  
AMD SEV-SNP extends AMD SEV by adding integrity protection and replay attack prevention to encrypted memory pages. This is implemented at the hardware level within the AMD EPYC CPU, enabling the hypervisor to run untrusted code while protecting guest VM memory confidentiality and integrity. Azure’s confidential VM infrastructure integrates with the Azure Attestation service to provide remote attestation capabilities, allowing customers to verify the VM’s trusted state before provisioning sensitive workloads. The VMs support standard Azure VM management and networking features, making integration with existing Azure environments seamless.

**Use Cases and Application Scenarios**  
- **Financial Services:** Securely processing sensitive financial transactions and confidential analytics without exposing data to cloud operators.  
- **Healthcare:** Protecting patient data and running compliance-sensitive workloads in a confidential environment.  
- **Government and Defense:** Meeting stringent security and compliance requirements by isolating classified workloads.  
- **Multi-Party Collaboration:** Enabling confidential data sharing and joint analytics across organizational boundaries without revealing underlying data.  
- **Intellectual Property Protection:** Safeguarding proprietary algorithms and models during cloud execution.

**Important Considerations and Limitations**  
- **Supported OS and Software:** Confidential VMs require guest OS support for SEV-SNP; currently, specific Linux distributions are supported, and Windows support is evolving.  
- **Performance Overhead:** While AMD SEV-SNP is efficient, some performance overhead exists due to encryption and integrity checks; benchmarking is recommended for workload suitability.  
- **Feature Parity:** Certain Azure VM features or extensions may have limited support on confidential VMs; verify compatibility before deployment.  
- **Attestation Dependency:** Remote attestation relies on Azure Attestation service availability and correct configuration to ensure trustworthiness.

**Integration with Related Azure Services**  
- **Azure Attestation:** Provides cryptographic verification of VM trustworthiness, essential for confidential computing workflows.  
- **Azure Key Vault:** Can be integrated to securely manage cryptographic keys used within confidential VMs.  
- **Azure Monitor and Security Center:** Support monitoring and security posture management for confidential VMs, although some telemetry may be limited due to isolation.  
- **Azure Kubernetes Service (AK

---

### 3. Public Preview: Azure Kubernetes Fleet Manager – update run approval gates

**Published**: September 18, 2025 17:30:18 UTC
**Link**: [Public Preview: Azure Kubernetes Fleet Manager – update run approval gates](https://azure.microsoft.com/updates?id=503245)

**Update ID**: 503245
**Data source**: Azure Updates API

**Categories**: In preview, Containers, Compute, Azure Kubernetes Fleet Manager, Azure Kubernetes Service (AKS), Features

**Summary**:

- What was updated  
Azure Kubernetes Fleet Manager’s update run process now supports approval gates in public preview.

- Key changes or new features  
Approval gates can be inserted before and after update groups and stages within an update run. These gates enable manual approval controls, allowing operators to pause the update workflow and explicitly approve continuation. This adds granular control over the update sequence, improving governance and risk management during cluster fleet updates.

- Target audience affected  
Developers and IT professionals responsible for managing and orchestrating updates across multiple Kubernetes clusters using Azure Kubernetes Fleet Manager. This feature benefits those requiring stricter update validation and compliance controls in multi-cluster environments.

- Important notes if any  
The feature is currently in public preview, so it may be subject to change. Users should test approval gates in non-production environments before full adoption. This enhancement helps enforce operational policies and reduces the risk of unintended disruptions during fleet-wide Kubernetes updates.  

Reference: https://azure.microsoft.com/updates?id=503245

**Details**:

The recent public preview update for Azure Kubernetes Fleet Manager introduces approval gates within update runs, enhancing control and governance over cluster update workflows across large-scale Kubernetes environments.

**Background and Purpose**  
Azure Kubernetes Fleet Manager is designed to simplify management of multiple Azure Kubernetes Service (AKS) clusters by enabling centralized orchestration of updates, configuration, and policy enforcement across a fleet of clusters. As organizations scale their Kubernetes deployments, ensuring safe, controlled, and auditable update processes becomes critical to maintain cluster stability and compliance. Prior to this update, update runs executed sequentially without built-in mechanisms for pausing or requiring manual validation between update stages or groups. The introduction of approval gates addresses this gap by allowing administrators to insert manual checkpoints, thereby reducing risk and increasing operational oversight during complex update workflows.

**Specific Features and Detailed Changes**  
This update adds the capability to define approval gates at two key points within an update run: before and after update groups and stages. An update run in Fleet Manager typically consists of multiple stages (logical phases of the update process) and groups (sets of clusters or nodes targeted together). With approval gates, administrators can:

- Pause the update run at predefined points.
- Require manual approval to proceed, ensuring human validation before continuing.
- Implement gates both before initiating a stage/group and after its completion, allowing verification of successful updates or rollback decisions.

This granular control enables a more deliberate and auditable update process, reducing the likelihood of propagating errors or issues across the fleet.

**Technical Mechanisms and Implementation Methods**  
Approval gates are implemented as configurable checkpoints within the update run orchestration engine of Fleet Manager. When an update run reaches a gate, the system transitions into a waiting state, halting further execution until an authorized user explicitly approves continuation via the Azure portal, CLI, or API. This mechanism leverages Azure Role-Based Access Control (RBAC) to ensure only designated approvers can authorize progression. The update run’s state and gate status are tracked and logged within Fleet Manager’s operational telemetry, providing visibility and audit trails. Integration with Azure Monitor and Azure Activity Logs allows organizations to monitor gate events and approvals programmatically.

**Use Cases and Application Scenarios**  
- **Enterprise Governance:** Large organizations managing hundreds of AKS clusters can enforce compliance by requiring security or operations teams to validate updates before rollout to production clusters.  
- **Staged Rollouts:** Teams can deploy updates first to non-critical clusters, use approval gates to verify stability, and then manually approve progression to critical production clusters.  
- **Incident Response:** If an update group encounters issues, teams can halt progression at a gate, perform remediation, and only proceed after confirming resolution.  
- **Cross-team Collaboration:** Different teams responsible for various cluster groups can coordinate update approvals, ensuring accountability and shared responsibility.

**Important Considerations and Limitations**  
- As this feature is currently in public preview, it may not be recommended for production-critical environments without thorough testing.  
- Manual approval introduces operational latency; organizations should balance control with update velocity requirements.  
- Proper RBAC configuration is essential to prevent unauthorized approvals or accidental update halts.  
- Integration with automated CI/CD pipelines may require additional scripting or tooling to handle manual approval steps.  
- The feature currently supports approval gates only within Fleet Manager update runs and may not extend to other AKS update mechanisms.

**Integration with Related Azure Services**  
- **Azure RBAC:** Controls who can approve gates, ensuring secure and compliant update workflows.  
- **Azure Monitor and Azure Activity Logs:** Provide observability into gate events, approvals, and update run progress for auditing and alerting.  
- **Azure CLI and REST API:** Allow programmatic interaction with approval gates, enabling integration with custom automation or ITSM tools.  
- **Azure Policy:** Can be used in conjunction to enforce update compliance and cluster configuration standards across the fleet.

In summary, the introduction of approval gates in Azure Kubernetes Fleet Manager update runs empowers IT professionals with enhanced operational control

---

### 4. Generally Available: Distributed tracing for Durable Functions 

**Published**: September 18, 2025 17:00:27 UTC
**Link**: [Generally Available: Distributed tracing for Durable Functions ](https://azure.microsoft.com/updates?id=503139)

**Update ID**: 503139
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Features

**Summary**:

- What was updated  
Azure Durable Functions now generally supports Distributed Tracing V2, offering an enhanced tracing model.

- Key changes or new features  
Distributed Tracing V2 enables comprehensive correlation of operations across orchestrations, activities, and durable entities within Durable Functions. This improved tracing facilitates end-to-end visibility into function executions, helping developers diagnose issues and understand workflow behavior more effectively. The update supports integration with popular tracing systems, allowing seamless propagation of trace context and improved observability.

- Target audience affected  
Developers building serverless workflows with Durable Functions and IT professionals responsible for monitoring, diagnosing, and maintaining Azure serverless applications.

- Important notes if any  
This feature is now generally available, meaning it is production-ready and supported. Developers should update their Durable Functions SDK to leverage the new tracing capabilities. Proper configuration of tracing exporters and instrumentation is required to fully utilize distributed tracing insights. This enhancement significantly improves troubleshooting and performance monitoring in complex Durable Functions applications.

For more details, visit: https://azure.microsoft.com/updates?id=503139

**Details**:

The recent general availability of Distributed Tracing V2 for Azure Durable Functions marks a significant enhancement in observability and diagnostics for serverless workflows by introducing a comprehensive tracing model that correlates operations across orchestrations, activities, and durable entities. This update addresses longstanding challenges in monitoring complex, stateful function executions by enabling end-to-end visibility into the execution flow and dependencies within Durable Functions.

**Background and Purpose**  
Durable Functions extend Azure Functions by enabling stateful orchestration of serverless workflows, which often involve multiple asynchronous activities and durable entities. Prior to this update, tracing and diagnostics were fragmented, making it difficult to correlate events and diagnose issues across the distributed components of a durable orchestration. The purpose of Distributed Tracing V2 is to provide a unified, robust tracing framework that captures and correlates telemetry data seamlessly, thereby improving troubleshooting, performance monitoring, and operational insights.

**Specific Features and Detailed Changes**  
Distributed Tracing V2 introduces a standardized tracing model based on OpenTelemetry principles, enabling correlation of telemetry across orchestrations, activity functions, and durable entities. Key features include:  
- Automatic propagation of trace context across function boundaries within Durable Functions.  
- Enhanced telemetry correlation that links parent orchestrations with child activities and entity operations.  
- Support for distributed trace identifiers that integrate with Azure Monitor and Application Insights, facilitating end-to-end trace visualization.  
- Improved instrumentation that captures lifecycle events such as orchestration start, completion, retries, and entity state changes.  
- Compatibility with existing Durable Functions codebases with minimal configuration changes.

**Technical Mechanisms and Implementation Methods**  
The implementation leverages OpenTelemetry SDKs integrated into the Durable Functions runtime to automatically generate and propagate trace context. Trace identifiers (trace ID, span ID) are injected into orchestration and activity function calls, ensuring that telemetry emitted by these components is linked. The tracing system hooks into the Durable Task Framework’s orchestration scheduler and entity operations to capture detailed execution metadata. This data is then exported to Azure Monitor and Application Insights using native exporters, enabling seamless integration with Azure’s observability stack. Developers can also extend or customize telemetry collection via OpenTelemetry APIs if needed.

**Use Cases and Application Scenarios**  
- **Complex Workflow Monitoring:** Developers can trace multi-step orchestrations involving numerous activities and entities, identifying bottlenecks or failures in specific steps.  
- **Performance Optimization:** By analyzing trace spans and durations, teams can optimize function execution times and resource utilization.  
- **Root Cause Analysis:** Correlated traces help pinpoint the exact function or entity causing errors or delays, reducing mean time to resolution (MTTR).  
- **Compliance and Auditing:** Detailed trace logs provide an audit trail of workflow executions and state changes for compliance requirements.  
- **Integration Testing and Debugging:** Enhanced tracing aids in validating orchestration logic and diagnosing issues during development and testing phases.

**Important Considerations and Limitations**  
- The tracing model requires Azure Monitor or Application Insights to fully leverage visualization and analytics capabilities.  
- There may be a slight increase in telemetry volume and associated costs due to more granular trace data collection.  
- Existing Durable Functions applications may require updating to the latest Durable Functions extension version to enable Distributed Tracing V2.  
- While automatic instrumentation covers most scenarios, custom activities or third-party integrations may require manual instrumentation to propagate trace context correctly.  
- Distributed tracing is primarily designed for Durable Functions running on the Consumption and Premium plans; behavior on other hosting models should be validated.

**Integration with Related Azure Services**  
Distributed Tracing V2 tightly integrates with Azure Monitor and Application Insights, leveraging their telemetry ingestion, storage, and visualization capabilities. Trace data is accessible via Application Insights’ End-to-End Transaction Diagnostics and Azure Monitor Workbooks, enabling rich analysis and alerting. The update complements Azure Functions’ native diagnostics and logging features, and works alongside Azure Event Grid and Azure Logic Apps when Durable Functions are part of broader event-driven architectures. Additionally, the use of OpenTelemetry standards

---


*This report was automatically generated - 2025-09-19 03:02:28 UTC*