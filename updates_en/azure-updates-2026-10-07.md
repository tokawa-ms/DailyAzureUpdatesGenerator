# October 07, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 07, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 5 items

## Update List

### 1. Retirement: Pod name dimension in AKS pod platform metrics

**Published**: October 06, 2026 22:37:54 UTC
**Link**: [Retirement: Pod name dimension in AKS pod platform metrics](https://azure.microsoft.com/updates?id=570232)

**Update ID**: 570232
**Data source**: Azure Updates API

**Categories**: Compute, Containers, Azure Kubernetes Service (AKS), Retirements

**Summary**:

- What was updated  
Azure announced the retirement of the "pod name" dimension in Azure Monitor platform metrics for AKS (Azure Kubernetes Service) pods, effective September 30, 2027.

- Key changes or new features  
The "pod name" dimension will no longer be available for the following metrics:  
  - Number of pods by phase (kube_pod_status_phase)  
  - Number of pods in Ready state (kube_pod_status_ready)  
These metrics will transition to aggregate pod counters, meaning metrics will be reported at an aggregate level (e.g., by namespace or cluster), not by individual pod name.

- Target audience affected  
Developers, DevOps engineers, and IT professionals who monitor AKS workloads using Azure Monitor and rely on pod-level granularity in these metrics.

- Important notes if any  
If you currently use the "pod name" dimension for monitoring, alerting, or automation, you must update your solutions to use aggregate metrics instead. After September 30, 2027, queries or alerts referencing the "pod name" dimension in these metrics will no longer work. Plan your migration to aggregate-based monitoring before the retirement date to avoid disruptions.  
[More details](https://azure.microsoft.com/updates?id=570232)

**Details**:

**Azure Update Technical Report**

**Title:** Retirement: Pod name dimension in AKS pod platform metrics  
**Source:** [Azure Update Link](https://azure.microsoft.com/updates?id=570232)  
**Retirement Date:** September 30, 2027

---

**Background and Purpose of the Update**

Azure Kubernetes Service (AKS) leverages Azure Monitor to provide platform metrics for monitoring pod health and status. Historically, these metrics included a "pod name" dimension, enabling granular visibility into individual pod states. The update announces the retirement of the pod name dimension from specific AKS pod platform metrics, transitioning to aggregate pod counters. The purpose is to streamline metric collection and reporting, likely to improve performance, scalability, and reduce complexity in metric management.

---

**Specific Features and Detailed Changes**

The retirement affects the following Azure Monitor platform metrics:

- **Number of pods by phase (`kube_pod_status_phase`)**
- **Number of pods in Re** (the full metric name is truncated in the provided content)

Currently, these metrics include a "pod name" dimension, allowing users to filter and analyze metrics at the individual pod level. After September 30, 2027, this dimension will be removed. Metrics will report aggregate values (e.g., total number of pods in each phase) rather than per-pod statistics.

---

**Technical Mechanisms and Implementation Methods**

Azure Monitor collects AKS platform metrics via Prometheus-style counters and exposes them through the Azure Metrics API. The "pod name" dimension is a metadata field attached to each metric, enabling fine-grained filtering. The retirement will involve removing this dimension from the metric schema, so queries and dashboards using this dimension will no longer return per-pod data.

Aggregate pod counters will continue to be available, providing summarized data such as the total number of pods in each phase (e.g., Running, Pending, Failed). This change simplifies metric ingestion and reduces storage and query overhead, as fewer unique time series will be generated and stored.

---

**Use Cases and Application Scenarios**

- **Current Use:** IT professionals and DevOps teams use the pod name dimension for troubleshooting, performance analysis, and alerting on individual pod states.
- **Post-Update Use:** After retirement, users must rely on aggregate metrics for cluster-wide or namespace-level monitoring. Individual pod-level insights will require alternative methods, such as querying Kubernetes APIs directly or using custom Prometheus metrics.

---

**Important Considerations and Limitations**

- **Impact on Monitoring Solutions:** Any dashboards, alerts, or reports relying on the pod name dimension will need to be updated before September 30, 2027. Failure to do so may result in broken queries or incomplete monitoring.
- **Loss of Granularity:** The removal of the pod name dimension means loss of per-pod visibility in platform metrics. Users must plan for alternative approaches if per-pod monitoring is required.
- **Transition Period:** IT teams should begin migrating to aggregate metrics and review their monitoring and alerting configurations to ensure continuity.

---

**Integration with Related Azure Services**

- **Azure Monitor:** Continues to provide aggregate AKS metrics. Custom metrics and logs can be used for more granular monitoring.
- **Log Analytics:** For detailed pod-level analysis, consider leveraging Log Analytics with Kubernetes audit logs or custom telemetry.
- **Prometheus Integration:** Users requiring pod-level metrics can deploy Prometheus within AKS clusters and configure scraping for custom metrics.

---

**Summary Sentence**

Beginning September 30, 2027, Azure Monitor will retire the pod name dimension from AKS pod platform metrics, transitioning to aggregate pod counters and requiring IT professionals to update their monitoring solutions to maintain visibility and functionality.

---

### 2. Retirement: Azure App Service on Azure Stack Hub

**Published**: October 06, 2026 18:24:43 UTC
**Link**: [Retirement: Azure App Service on Azure Stack Hub](https://azure.microsoft.com/updates?id=568178)

**Update ID**: 568178
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, Hybrid + multicloud, App Service, Azure Stack Hub, Retirements

**Summary**:

- What was updated  
Azure App Service on Azure Stack Hub is being retired.

- Key changes or new features  
No new installations of Azure App Service on Azure Stack Hub will be supported after September 30, 2026. There will be no further product releases, features, or enhancements from that date. Full retirement of the service is scheduled for September 30, 2029. Existing deployments will continue to be supported until the retirement date.

- Target audience affected  
Developers and IT professionals managing workloads on Azure App Service for Azure Stack Hub, especially those responsible for hybrid cloud or on-premises solutions.

- Important notes if any  
Customers should begin planning migration strategies for workloads running on Azure App Service on Azure Stack Hub. After September 30, 2026, only existing deployments will be supported, with no new features or updates. After September 30, 2029, the service will be fully retired and unsupported. Consider moving workloads to alternative Azure services or other supported platforms before the retirement date to avoid service disruption.

For more details, see the official update: https://azure.microsoft.com/updates?id=568178

**Details**:

**Azure Update Report: Retirement of Azure App Service on Azure Stack Hub**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of Azure App Service on Azure Stack Hub, effective September 30, 2029. The primary purpose of this update is to inform customers and partners about the end-of-life timeline for this hybrid cloud service, enabling organizations to plan migration strategies and avoid disruption. Azure App Service on Azure Stack Hub has enabled customers to run web applications, APIs, and mobile backends in their own datacenters, providing hybrid capabilities and local compliance. The retirement aligns with Microsoft’s lifecycle management policies and focus on evolving Azure services.

**Specific Features and Detailed Changes**  
- **Retirement Date:** Azure App Service on Azure Stack Hub will be fully retired on September 30, 2029.  
- **End of New Installations:** Starting September 30, 2026, new installations of Azure App Service on Azure Stack Hub will no longer be supported.  
- **Product Releases and Enhancements:** After September 30, 2026, there will be no new product releases, features, or enhancements for this service.  
- **Existing Deployments:** Existing supported deployments will continue to operate until the retirement date, but will not receive new features or enhancements.

**Technical Mechanisms and Implementation Methods**  
Azure App Service on Azure Stack Hub is deployed as a resource provider on Azure Stack Hub, enabling local hosting of App Service environments. The update will be implemented by ceasing support for new installations and halting development of new features after the specified date. Existing installations will remain operational, but customers should anticipate eventual deprecation and plan for migration to alternative solutions, such as Azure App Service in public Azure or other hybrid offerings.

**Use Cases and Application Scenarios**  
Typical use cases include:  
- Hosting web applications and APIs in environments with strict data residency or compliance requirements.  
- Providing local development and testing environments for applications intended for Azure App Service.  
- Enabling hybrid cloud scenarios where applications span both on-premises and Azure public cloud environments.  
With the retirement, organizations relying on these scenarios must evaluate alternative architectures and migration paths.

**Important Considerations and Limitations**  
- **No New Installations:** After September 30, 2026, new deployments cannot be initiated.  
- **No Feature Updates:** No new features or enhancements will be delivered after this date.  
- **Operational Continuity:** Existing supported deployments will continue to function until September 30, 2029, but will not benefit from ongoing innovation or improvements.  
- **Migration Planning:** Customers must plan for migration to supported platforms before retirement to avoid service disruption.

**Integration with Related Azure Services**  
Azure App Service on Azure Stack Hub has historically integrated with Azure Stack Hub for hybrid cloud scenarios, leveraging local compute and storage resources while maintaining compatibility with Azure App Service APIs and development workflows. After retirement, customers are encouraged to transition workloads to Azure App Service in the public cloud or explore other Azure hybrid solutions, such as Azure Arc-enabled App Services, to maintain continuity and leverage ongoing innovation.

**Summary Sentence**  
Azure App Service on Azure Stack Hub will be retired on September 30, 2029, with new installations unsupported after September 30, 2026, and no further product releases or enhancements, requiring customers to plan migration strategies for hybrid web application workloads.

---

### 3. Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027

**Published**: October 06, 2026 18:21:59 UTC
**Link**: [Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027](https://azure.microsoft.com/updates?id=568585)

**Update ID**: 568585
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements

**Summary**:

- What was updated  
Azure App Service is retiring support for Java 8, 11, and 17 on September 1, 2027.

- Key changes or new features  
After September 1, 2027, Java 8, 11, and 17 runtimes on Azure App Service will no longer receive security updates or customer support. Applications using these Java versions will continue to run, but Microsoft will not provide patches or assistance for any issues related to these runtimes.

- Target audience affected  
Developers and IT professionals managing Java applications on Azure App Service, especially those using Java 8, 11, or 17.

- Important notes if any  
To maintain security and support, plan to upgrade your applications to a supported Java version before September 1, 2027. Continuing to use these versions after the retirement date exposes applications to potential security risks and lack of vendor support. Review your application dependencies and update your deployment pipelines to ensure compatibility with newer Java versions ahead of the deadline.

[More information](https://azure.microsoft.com/updates?id=568585)

**Details**:

**Azure Update Technical Explanation**

**Title:** Retirement: Support for Java 8, 11 and 17 will end on September 1, 2027  
**Source:** [Azure Update Link](https://azure.microsoft.com/updates?id=568585)

---

### Background and Purpose of the Update

This update announces the end of support for Java 8, 11, and 17 on Azure App Service, effective September 1, 2027. The primary purpose is to inform customers that these Java versions will no longer receive security updates or customer service from Microsoft on App Service after this date. This aligns with standard software lifecycle practices, ensuring that only supported and secure runtime environments are maintained on Azure.

---

### Specific Features and Detailed Changes

- **End of Support:** Java 8, 11, and 17 will reach end-of-support status on Azure App Service as of September 1, 2027.
- **Continued Operation:** Applications currently running on these Java versions will not be forcibly stopped or removed; they will continue to run as-is.
- **Cessation of Updates:** No further security updates, patches, or bug fixes will be provided for these Java versions on App Service.
- **End of Customer Service:** Microsoft will no longer provide technical support or assistance for issues related to Java 8, 11, or 17 on App Service.

---

### Technical Mechanisms and Implementation Methods

Azure App Service manages the runtime environments for hosted applications, including the underlying Java versions. After the retirement date, the platform will not update or patch the Java 8, 11, or 17 runtimes. This means that any vulnerabilities discovered after September 1, 2027, will remain unpatched, and any operational issues specific to these Java versions will not receive support from Microsoft. The retirement is enforced at the platform level, affecting all App Service plans and deployment models utilizing these Java versions.

---

### Use Cases and Application Scenarios

- **Current Deployments:** Applications currently deployed on App Service using Java 8, 11, or 17 will remain operational but will be running on unsupported runtimes.
- **Migration Planning:** Organizations must plan to migrate their applications to supported Java versions before the retirement date to maintain security and support.
- **Long-Term Application Maintenance:** Applications with long-term maintenance requirements should be prioritized for migration to ensure compliance and security.

---

### Important Considerations and Limitations

- **Security Risk:** Running applications on unsupported Java versions increases exposure to unpatched vulnerabilities.
- **Compliance:** Organizations with regulatory or compliance requirements may be impacted by the use of unsupported software.
- **No Support:** After the retirement date, any issues related to Java 8, 11, or 17 will not be addressed by Microsoft support channels.
- **No Automatic Upgrade:** Applications will not be automatically upgraded to newer Java versions; manual intervention is required.

---

### Integration with Related Azure Services

- **App Service Integration:** The update specifically applies to Java runtimes managed by Azure App Service. Other Azure services or custom container deployments may have different support policies.
- **DevOps Pipelines:** Teams using CI/CD pipelines for App Service deployments should update their build and deployment configurations to target supported Java versions.
- **Monitoring and Alerts:** Integration with Azure Monitor or Application Insights should include checks for runtime versions to proactively identify applications at risk.

---

**Summary:**  
Support for Java 8, 11, and 17 on Azure App Service will end on September 1, 2027; while applications will continue to run, no further security updates or customer support will be provided for these Java versions.

---

### 4. Retirement: Always Encrypted with Intel SGX Enclaves

**Published**: October 06, 2026 16:42:33 UTC
**Link**: [Retirement: Always Encrypted with Intel SGX Enclaves](https://azure.microsoft.com/updates?id=569236)

**Update ID**: 569236
**Data source**: Azure Updates API

**Categories**: Databases, Hybrid + multicloud, Azure SQL Database, Retirements

**Summary**:

- What was updated  
The Always Encrypted with Intel SGX enclaves feature in Azure SQL Database is being retired.

- Key changes or new features  
Support for Always Encrypted with Intel SGX enclaves will end on October 31, 2027, as Azure phases out SGX-enabled DC-series hardware. Customers are advised to migrate to Virtualization-Based Security (VBS) enclaves, which provide a hardware-independent solution for secure data processing in Azure SQL Database.

- Target audience affected  
Developers and IT professionals using Always Encrypted with Intel SGX enclaves in Azure SQL Database, especially those relying on DC-series hardware for confidential computing workloads.

- Important notes if any  
- After October 31, 2027, Always Encrypted with Intel SGX enclaves will no longer be supported; workloads depending on this feature must transition to VBS enclaves to maintain secure enclave capabilities.  
- VBS enclaves offer similar security benefits without dependency on specific hardware, simplifying migration and future-proofing applications.  
- Review your current use of Always Encrypted with enclaves and plan migration to VBS enclaves before the retirement date to avoid service disruption.

For more details, see the official Azure update: https://azure.microsoft.com/updates?id=569236

**Details**:

**Azure Update Report: Retirement of Always Encrypted with Intel SGX Enclaves in Azure SQL Database**

**Background and Purpose of the Update:**  
Azure SQL Database has supported Always Encrypted with Intel SGX (Software Guard Extensions) enclaves, leveraging DC-series hardware to provide secure, isolated environments for sensitive data processing. Microsoft is announcing the retirement of this feature, effective October 31, 2027, as support for SGX-enabled DC-series hardware is being phased out. The purpose of this update is to inform customers of the transition plan and recommend moving to Virtualization-Based Security (VBS) enclaves, which are hardware-independent.

**Specific Features and Detailed Changes:**  
The primary change is the deprecation of Always Encrypted with SGX enclaves. After October 31, 2027, customers will no longer be able to use SGX-based enclaves for Always Encrypted operations in Azure SQL Database. The recommended alternative is VBS enclaves, which provide similar data protection capabilities without relying on specific hardware (SGX/DC-series). VBS enclaves are designed to be hardware-agnostic, simplifying deployment and future-proofing security investments.

**Technical Mechanisms and Implementation Methods:**  
Always Encrypted with SGX enclaves used Intel SGX technology to create secure, hardware-based enclaves within DC-series Azure VMs. These enclaves enabled confidential computations on encrypted columns, supporting operations such as secure data comparisons and computations without exposing plaintext data to the database engine.  
With the transition to VBS enclaves, the security boundary shifts from hardware-based SGX to virtualization-based isolation. VBS enclaves leverage virtualization technologies to create secure, isolated memory regions within the VM, protecting sensitive computations from the rest of the system. This approach removes dependency on specialized hardware and allows broader compatibility across Azure VM types.

**Use Cases and Application Scenarios:**  
Always Encrypted with SGX enclaves has been used in scenarios requiring high assurance for data confidentiality, such as processing sensitive financial, healthcare, or personally identifiable information (PII) within Azure SQL Database. Typical use cases include secure data analytics, regulated industry workloads, and applications where compliance mandates strict data protection.  
With VBS enclaves, these use cases can continue to be supported, but with improved flexibility and scalability, as VBS is not limited to DC-series hardware.

**Important Considerations and Limitations:**  
- Customers must plan migration from SGX enclaves to VBS enclaves before October 31, 2027, to avoid service disruption.
- VBS enclaves are hardware-independent, but customers should review compatibility and performance implications for their workloads.
- Existing applications using Always Encrypted with SGX enclaves may require code or configuration changes to leverage VBS enclaves.
- The retirement affects only SGX-based enclaves; Always Encrypted as a feature and VBS enclaves remain supported.

**Integration with Related Azure Services:**  
Always Encrypted with enclaves is tightly integrated with Azure SQL Database, providing enhanced data protection for sensitive columns. The transition to VBS enclaves ensures continued compatibility with Azure SQL Database features and simplifies integration with other Azure services, as VBS is not tied to specific VM series. Customers can leverage VBS enclaves across a broader range of Azure infrastructure, facilitating easier scaling and deployment.

**Summary Sentence:**  
Always Encrypted with Intel SGX enclaves in Azure SQL Database will retire on October 31, 2027, and customers are advised to migrate to hardware-independent Virtualization-Based Security (VBS) enclaves to ensure continued secure data processing and compliance.

---

### 5. Public Preview: AKS on bare metal now on Ubuntu

**Published**: October 06, 2026 15:44:06 UTC
**Link**: [Public Preview: AKS on bare metal now on Ubuntu](https://azure.microsoft.com/updates?id=573782)

**Update ID**: 573782
**Data source**: Azure Updates API

**Categories**: In preview, Feature

**Summary**:

- What was updated  
Azure Kubernetes Service (AKS) on bare metal is now available in public preview on Ubuntu.

- Key changes or new features  
AKS can now be deployed directly on bare metal servers running Ubuntu, removing the need for a virtualization layer. This enables direct access to hardware resources, which is especially beneficial for workloads requiring high performance, such as AI and machine learning. The update offers improved performance, lower latency, and more control over hardware and software configurations.

- Target audience affected  
Developers and IT professionals managing on-premises Kubernetes clusters, especially those running performance-sensitive workloads (e.g., AI/ML, data analytics), and organizations seeking greater control over their infrastructure.

- Important notes if any  
This public preview is focused on Ubuntu as the supported operating system for AKS on bare metal. Users can leverage familiar AKS management tools and APIs while benefiting from direct hardware access. Evaluate compatibility with your existing infrastructure and workloads before adoption. Production workloads should consider preview limitations and support scope.  

Data source: Using API data  
Link: https://azure.microsoft.com/updates?id=573782

**Details**:

**Azure Update Report: Public Preview – AKS on Bare Metal Now on Ubuntu**

**Background and Purpose of the Update**  
Traditionally, running Kubernetes clusters on-premises requires organizations to either deploy a virtualization layer or adapt to infrastructure that may not be familiar or optimal. This often results in reduced control over hardware and software, which can be particularly problematic for workloads with demanding requirements, such as AI and machine learning. The public preview of Azure Kubernetes Service (AKS) on bare metal, now available on Ubuntu, addresses these challenges by enabling direct deployment of AKS clusters onto physical servers without the overhead of virtualization. This update aims to provide greater control, performance, and flexibility for organizations seeking to leverage Kubernetes in their own datacenters.

**Specific Features and Detailed Changes**  
- **AKS Bare Metal Support:** AKS can now be deployed directly onto bare metal servers running Ubuntu, eliminating the need for a hypervisor or virtual machines.
- **Operating System:** Ubuntu is the supported OS for this deployment, aligning with industry standards for container workloads.
- **Public Preview:** The feature is currently in public preview, allowing IT professionals to evaluate and test AKS on bare metal with Ubuntu in their environments.

**Technical Mechanisms and Implementation Methods**  
- **Direct Hardware Access:** By running AKS on bare metal, the Kubernetes control plane and worker nodes have direct access to physical resources, reducing latency and improving performance.
- **Deployment Model:** The AKS deployment process is adapted for Ubuntu, leveraging native OS capabilities for container orchestration and management.
- **No Virtualization Layer:** The absence of a virtualization layer simplifies the stack, reduces resource overhead, and enables more efficient utilization of hardware.

**Use Cases and Application Scenarios**  
- **AI and Machine Learning Workloads:** These workloads often require high-performance access to local GPUs, storage, and networking. AKS on bare metal enables optimal resource utilization for such scenarios.
- **On-Premises Kubernetes Management:** Organizations with strict compliance, data residency, or performance requirements can maintain full control over their infrastructure while using Azure-managed Kubernetes.
- **Hybrid Cloud Deployments:** Enterprises can integrate on-premises AKS clusters with Azure cloud services, facilitating seamless hybrid and edge computing strategies.

**Important Considerations and Limitations**  
- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. IT professionals should evaluate stability, support, and feature completeness before widespread adoption.
- **OS Limitation:** Ubuntu is the only supported operating system for AKS on bare metal in this preview, which may impact organizations using other Linux distributions.
- **Hardware Compatibility:** Organizations must ensure their bare metal hardware meets the requirements for AKS and Ubuntu deployments.

**Integration with Related Azure Services**  
- **Azure Arc:** AKS on bare metal can be integrated with Azure Arc for unified management, governance, and monitoring across hybrid and multi-cloud environments.
- **Azure AI Services:** Enhanced performance for AI workloads enables better integration with Azure’s AI and machine learning offerings, allowing for local processing and cloud-based analytics.
- **Azure DevOps and Monitoring:** Standard Azure tools for CI/CD, monitoring, and security can be leveraged with AKS on bare metal, ensuring consistent operational practices.

**Summary Sentence:**  
AKS on bare metal for Ubuntu, now in public preview, enables direct Kubernetes deployment on physical servers, offering improved control and performance for demanding workloads and facilitating seamless integration with Azure’s hybrid and AI services.

---


*This report was automatically generated - 2026-10-07 03:03:29 UTC*