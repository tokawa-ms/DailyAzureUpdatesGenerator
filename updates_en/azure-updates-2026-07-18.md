# July 18, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 18, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 4 items

## Update List

### 1. Generally Available: Azure Functions support for Python 3.14

**Published**: July 17, 2026 17:47:00 UTC
**Link**: [Generally Available: Azure Functions support for Python 3.14](https://azure.microsoft.com/updates?id=567646)

**Update ID**: 567646
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Open Source, Services, Feature

**Summary**:

- What was updated  
Azure Functions now supports Python 3.14 in general availability.

- Key changes or new features  
Developers can build and test Azure Functions locally using Python 3.14 and deploy them to Azure Functions plans running on Linux. Python 3.14 brings enhanced security features, an extended support lifecycle, and ensures ongoing compatibility with Azure Functions tooling and runtime.

- Target audience affected  
Developers building serverless applications with Azure Functions, IT professionals managing Azure Functions deployments, and teams maintaining Python-based workloads in Azure.

- Important notes  
It is recommended to upgrade existing Python Azure Functions apps to Python 3.14 to benefit from improved security and longer support. Ensure that your local development environment and CI/CD pipelines are updated to use Python 3.14. This update applies only to Linux-based Azure Functions plans; Windows support is not mentioned. Review your dependencies for compatibility with Python 3.14 before upgrading.

For more details, see the official Azure Update: https://azure.microsoft.com/updates?id=567646

**Details**:

**Azure Update Technical Explanation: Azure Functions Support for Python 3.14 (Generally Available)**

**Background and Purpose of the Update:**  
This update announces the general availability of Python 3.14 support in Azure Functions. Azure Functions is a serverless compute service that enables event-driven application development. The primary purpose of this update is to allow developers to build, test, and deploy Azure Functions using Python 3.14, both locally and on Azure Functions plans running on Linux. This ensures that applications can leverage the latest Python language features, improved security, and extended support lifecycles.

**Specific Features and Detailed Changes:**  
- **Python 3.14 Runtime Support:** Developers can now create and run Azure Functions using Python 3.14. This includes full compatibility with the Python 3.14 runtime for both local development and cloud deployment.
- **Linux Plan Availability:** Python 3.14 is supported on all Azure Functions hosting plans that run on Linux, including Consumption, Premium, and Dedicated (App Service) plans.
- **Security and Support Enhancements:** By upgrading to Python 3.14, users benefit from the latest security patches, performance improvements, and a longer support window compared to previous Python versions.
- **Continued Azure Functions Compatibility:** The update ensures that Python 3.14-based functions remain compatible with the Azure Functions runtime and its features.

**Technical Mechanisms and Implementation Methods:**  
- **Local Development:** Developers can set up their local environment with Python 3.14 and the Azure Functions Core Tools to build and test functions before deployment.
- **Deployment:** Functions written in Python 3.14 can be deployed to Azure using standard deployment pipelines (e.g., Azure CLI, GitHub Actions, or Azure DevOps).
- **Runtime Integration:** The Azure Functions runtime on Linux has been updated to recognize and execute Python 3.14 code, ensuring seamless integration with the platform’s event-driven model.

**Use Cases and Application Scenarios:**  
- **Modernization of Existing Functions:** Organizations can upgrade their existing Azure Functions from older Python versions to 3.14 to maintain compliance and security standards.
- **New Function Development:** Developers can leverage new Python 3.14 features for building serverless APIs, event-driven data processing, automation scripts, and integration workflows.
- **CI/CD Pipelines:** Teams can integrate Python 3.14-based function deployment into their continuous integration and deployment pipelines for automated testing and release.

**Important Considerations and Limitations:**  
- **Linux-Only Support:** Python 3.14 support is available exclusively on Linux-based Azure Functions plans. Windows-based plans are not supported for this runtime.
- **Upgrade Planning:** Before upgrading, validate that your code and dependencies are compatible with Python 3.14 to avoid runtime issues.
- **Support Lifecycle:** Using Python 3.14 ensures a longer support window, but users should monitor Azure and Python release notes for future deprecation timelines.

**Integration with Related Azure Services:**  
- **Event Sources and Bindings:** Python 3.14 functions can interact with various Azure services through triggers and bindings, such as Azure Blob Storage, Event Grid, Service Bus, and Cosmos DB.
- **Monitoring and Diagnostics:** Integration with Azure Monitor and Application Insights remains consistent, allowing for logging, metrics, and diagnostics for Python 3.14 functions.
- **DevOps Integration:** Python 3.14 support is compatible with Azure DevOps, GitHub Actions, and other CI/CD tools for automated deployment and testing.

**Summary:**  
Azure Functions now supports Python 3.14 on Linux plans, enabling developers to build and deploy secure, modern serverless applications with the latest Python features and extended support.

---

### 2. Public Preview: Azure Functions Support for PowerShell 7.6 

**Published**: July 17, 2026 17:44:00 UTC
**Link**: [Public Preview: Azure Functions Support for PowerShell 7.6 ](https://azure.microsoft.com/updates?id=567651)

**Update ID**: 567651
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Security, Services, Feature

**Summary**:

- What was updated  
Azure Functions now supports PowerShell 7.6 in public preview.

- Key changes or new features  
Developers can build and test Azure Functions using PowerShell 7.6 locally, then deploy them to Azure Functions plans. This update allows leveraging the latest PowerShell features and improvements within serverless workloads. Existing PowerShell function apps can be upgraded to 7.6 for enhanced compatibility and performance.

- Target audience affected  
Developers and IT professionals who use Azure Functions with PowerShell, especially those maintaining automation, orchestration, or serverless solutions in Azure.

- Important notes  
This is a public preview, so PowerShell 7.6 support may not be fully production-ready. Users should review compatibility and test thoroughly before migrating critical workloads. For more information, refer to the official documentation on PowerShell versions in Azure Functions.

**Details**:

**Azure Update Report: Public Preview – Azure Functions Support for PowerShell 7.6**

**Background and Purpose of the Update**  
Azure Functions is a serverless compute service that enables event-driven execution of code. Historically, Azure Functions has supported various versions of PowerShell, allowing IT professionals to automate operational tasks and workflows in the cloud. The release of PowerShell 7.6 introduces new language features, performance improvements, and security enhancements. This update aims to provide developers and IT professionals with the ability to leverage PowerShell 7.6 within Azure Functions, ensuring compatibility with the latest PowerShell capabilities and facilitating modern automation scenarios.

**Specific Features and Detailed Changes**  
With this public preview, Azure Functions now supports the PowerShell 7.6 runtime. Developers can build and test their Azure Functions locally using PowerShell 7.6, then deploy these functions to Azure Functions plans in the cloud. This update includes:

- Support for PowerShell 7.6 syntax and modules within Azure Functions.
- Ability to use PowerShell 7.6 features such as improved error handling, enhanced cmdlets, and updated security mechanisms.
- Compatibility with local development environments, allowing seamless transition from local testing to cloud deployment.
- Updated documentation and tooling to facilitate migration from earlier PowerShell versions to 7.6.

**Technical Mechanisms and Implementation Methods**  
The Azure Functions runtime now incorporates PowerShell 7.6 as an execution environment. Developers can specify PowerShell 7.6 as the target runtime in their function app configuration. Local development is enabled by installing PowerShell 7.6 and the Azure Functions Core Tools, allowing for consistent testing and debugging. Deployment to Azure Functions plans is supported via standard deployment pipelines, including Azure DevOps, GitHub Actions, or direct publishing from Visual Studio Code. The runtime ensures isolation and manages dependencies, leveraging PowerShell modules and scripts as part of the function app package.

**Use Cases and Application Scenarios**  
Typical use cases for PowerShell 7.6 in Azure Functions include:

- Automation of Azure resource management (e.g., provisioning, scaling, monitoring).
- Integration with external systems via REST APIs or PowerShell modules.
- Scheduled tasks and event-driven workflows triggered by Azure Event Grid, Service Bus, or HTTP requests.
- Security and compliance automation, such as auditing and remediation scripts.
- Custom operational logic for DevOps pipelines and IT management.

**Important Considerations and Limitations**  
As this is a public preview, the PowerShell 7.6 runtime may not be fully supported in production environments. IT professionals should review the Azure Functions documentation for known issues, limitations, and compatibility notes. Existing function apps using earlier PowerShell versions may require code updates to leverage new features or resolve breaking changes. Module compatibility and dependency management should be carefully validated during migration. Additionally, preview features may be subject to change and should be monitored for updates.

**Integration with Related Azure Services**  
Azure Functions with PowerShell 7.6 can be integrated with a wide range of Azure services, including Azure Logic Apps, Azure Event Grid, Azure Service Bus, Azure Storage, and Azure Monitor. This enables comprehensive automation and orchestration scenarios, leveraging PowerShell’s scripting capabilities to interact with Azure APIs and resources. Integration with Azure DevOps and GitHub Actions supports CI/CD workflows for function app deployment and management.

**Summary Sentence**  
Azure Functions now supports PowerShell 7.6 in public preview, enabling IT professionals to develop, test, and deploy serverless automation solutions using the latest PowerShell features, with seamless integration across Azure services and enhanced local development capabilities.

---

### 3. Generally Available: Microsoft Defender security assessments for Azure Database for PostgreSQL Flexible Server 

**Published**: July 17, 2026 14:55:28 UTC
**Link**: [Generally Available: Microsoft Defender security assessments for Azure Database for PostgreSQL Flexible Server ](https://azure.microsoft.com/updates?id=567527)

**Update ID**: 567527
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure Database for PostgreSQL, Feature

**Summary**:

- What was updated  
Microsoft Defender Cloud Security Posture Management (CSPM) assessments are now generally available for Azure Database for PostgreSQL Flexible Server.

- Key changes or new features  
This update enables continuous security assessments for Azure PostgreSQL Flexible Server instances. Developers and IT professionals can now leverage Microsoft Defender CSPM to automatically evaluate and monitor the security posture of their PostgreSQL databases. The assessments provide actionable recommendations to address security risks, improve compliance, and enhance overall database protection.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals managing Azure Database for PostgreSQL Flexible Server environments. Organizations seeking to strengthen their cloud database security and compliance will benefit from these new capabilities.

- Important notes if any  
The assessments are integrated into Microsoft Defender for Cloud, allowing users to view security recommendations directly within the Azure portal. Continuous monitoring helps identify misconfigurations and vulnerabilities, supporting proactive remediation. No additional setup is required for existing Defender for Cloud users; assessments are available out-of-the-box for supported PostgreSQL Flexible Server resources. For more details, visit the official Azure Update [link](https://azure.microsoft.com/updates?id=567527).

**Details**:

**Comprehensive Technical Explanation:**

**Background and Purpose of the Update:**  
Microsoft Defender Cloud Security Posture Management (CSPM) assessments are now generally available for Azure Database for PostgreSQL Flexible Server. The purpose of this update is to enable continuous evaluation of the security posture for PostgreSQL Flexible Server instances within Azure, helping organizations identify and remediate potential security risks proactively.

**Specific Features and Detailed Changes:**  
With this update, CSPM assessments are integrated directly into Azure Database for PostgreSQL Flexible Server. These assessments provide automated security checks and recommendations tailored to PostgreSQL Flexible Server configurations. The assessments cover a range of security controls, such as authentication settings, network access, encryption, and compliance with best practices. The update ensures that IT professionals can access real-time security status and actionable guidance for their PostgreSQL Flexible Server resources.

**Technical Mechanisms and Implementation Methods:**  
The CSPM assessments are powered by Microsoft Defender and operate through continuous monitoring of PostgreSQL Flexible Server resources. The mechanism involves scanning server configurations and operational parameters against a set of predefined security baselines. Assessment results are surfaced within the Azure portal, typically under the Microsoft Defender for Cloud dashboard, where users can review findings, receive prioritized recommendations, and track remediation progress. The assessments leverage Azure-native APIs and telemetry to ensure minimal performance impact and seamless integration.

**Use Cases and Application Scenarios:**  
- **Continuous Security Monitoring:** Organizations can use CSPM assessments to maintain ongoing visibility into the security posture of their PostgreSQL Flexible Server instances, ensuring compliance with internal and external security standards.
- **Automated Remediation Guidance:** Security teams can leverage the recommendations provided by the assessments to quickly address misconfigurations or vulnerabilities, reducing manual effort and response time.
- **Regulatory Compliance:** Enterprises subject to regulatory requirements can utilize CSPM assessments to demonstrate adherence to security controls and generate audit-ready reports.
- **Integration into DevOps Pipelines:** The assessments can be incorporated into CI/CD workflows, enabling security checks as part of the deployment process for PostgreSQL Flexible Server resources.

**Important Considerations and Limitations:**  
- The CSPM assessments are specific to Azure Database for PostgreSQL Flexible Server and may not cover other PostgreSQL deployment types or third-party managed services.
- The scope of assessments is limited to the security controls and baselines defined by Microsoft Defender; custom security requirements may require additional validation.
- Assessment results are dependent on the accuracy and completeness of server configuration data; misconfigured or incomplete resources may yield false positives or negatives.
- Organizations should review assessment findings regularly and ensure that remediation actions are tracked and implemented.

**Integration with Related Azure Services:**  
The CSPM assessments are tightly integrated with Microsoft Defender for Cloud, allowing centralized management of security posture across multiple Azure resources. Findings from PostgreSQL Flexible Server assessments can be correlated with other Defender insights, supporting unified security operations and incident response. Additionally, assessment results can be exported or integrated with Azure Policy, Azure Security Center, and other monitoring solutions for broader governance and compliance workflows.

**Summary Sentence:**  
Microsoft Defender CSPM assessments for Azure Database for PostgreSQL Flexible Server are now generally available, providing automated, continuous security evaluation and actionable recommendations to enhance the security posture of PostgreSQL Flexible Server resources within Azure.

---

### 4. Generally Available: Encryption in Transit for Azure Files NFS Shares in Azure Kubernetes Service (AKS)

**Published**: July 17, 2026 14:54:09 UTC
**Link**: [Generally Available: Encryption in Transit for Azure Files NFS Shares in Azure Kubernetes Service (AKS)](https://azure.microsoft.com/updates?id=567787)

**Update ID**: 567787
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Compute, Containers, Azure Files, Azure Kubernetes Service (AKS), Security, Feature

**Summary**:

- What was updated  
Encryption in Transit (EiT) is now generally available for Azure Files NFS v4.1 shares used in Azure Kubernetes Service (AKS) via the Azure File CSI driver.

- Key changes or new features  
AKS workloads can now securely access Azure Files NFS shares with data encrypted during transit using TLS. This enhancement applies to NFS v4.1 volumes provisioned through the Azure File CSI driver. EiT ensures that all data exchanged between AKS pods and Azure Files NFS shares is protected against interception and unauthorized access.

- Target audience affected  
Developers and IT professionals deploying containerized workloads in AKS that utilize Azure Files NFS v4.1 shares for persistent storage. Teams responsible for security, compliance, and storage architecture in Kubernetes environments.

- Important notes  
EiT is enabled by default for new NFS shares provisioned via the Azure File CSI driver. Existing NFS shares may require configuration updates to enable EiT. This feature helps meet regulatory and organizational security requirements for protecting data in transit. For implementation details and compatibility, refer to Azure documentation and the linked update.  

Link: [Azure Update](https://azure.microsoft.com/updates?id=567787)

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Encryption in Transit for Azure Files NFS Shares in Azure Kubernetes Service (AKS)

**Background and Purpose of the Update:**  
Azure Kubernetes Service (AKS) is widely used for orchestrating containerized workloads, often requiring persistent storage solutions. Azure Files provides managed file shares, and NFS v4.1 support enables Linux-based workloads to access these shares. Previously, data transferred between AKS workloads and Azure Files NFS shares was not encrypted in transit, which posed potential security risks, especially for sensitive or regulated data. The purpose of this update is to address these risks by introducing Encryption in Transit (EiT), ensuring data confidentiality during transmission.

**Specific Features and Detailed Changes:**  
This update makes Encryption in Transit generally available for Azure Files NFS v4.1 volumes mounted in AKS via the Azure File CSI (Container Storage Interface) driver. With EiT enabled, all data exchanged between AKS pods and Azure Files NFS shares is encrypted using TLS (Transport Layer Security). This enhancement applies specifically to NFS v4.1 volumes provisioned through the Azure File CSI driver, aligning with industry best practices for securing data in transit.

**Technical Mechanisms and Implementation Methods:**  
EiT is implemented by leveraging TLS encryption for all communication between AKS workloads and Azure Files NFS shares. The Azure File CSI driver facilitates the mounting of NFS v4.1 volumes, and when EiT is enabled, it ensures that the NFS protocol operates over a secure TLS channel. This prevents unauthorized access or interception of data during transit. The implementation requires configuration of the Azure File CSI driver to enable EiT, which may involve specifying relevant parameters in the Kubernetes persistent volume and persistent volume claim definitions.

**Use Cases and Application Scenarios:**  
- **Securing Sensitive Workloads:** Organizations running workloads that handle confidential or regulated data (e.g., healthcare, finance) in AKS can now ensure compliance by encrypting data in transit to Azure Files NFS shares.
- **Multi-tenant Environments:** In scenarios where AKS clusters are shared among multiple teams or tenants, EiT prevents data leakage between workloads.
- **Hybrid and Distributed Applications:** Applications that span multiple regions or require secure communication between AKS and Azure Files benefit from enhanced security.

**Important Considerations and Limitations:**  
- **Scope:** EiT is available only for Azure Files NFS v4.1 volumes accessed via the Azure File CSI driver in AKS. It does not apply to SMB shares or other storage drivers.
- **Configuration:** Enabling EiT may require updates to existing Kubernetes storage manifests and CSI driver settings.
- **Performance Impact:** TLS encryption may introduce additional CPU overhead and latency, which should be evaluated for performance-sensitive workloads.
- **Compatibility:** Ensure that AKS nodes and workloads support the required TLS versions and that the CSI driver is updated to the latest supported version.

**Integration with Related Azure Services:**  
EiT for Azure Files NFS shares integrates seamlessly with AKS and the Azure File CSI driver. It complements other Azure security features such as Encryption at Rest, Azure Active Directory authentication, and network security controls. This update strengthens the overall security posture of AKS deployments using Azure Files for persistent storage.

**Summary Sentence:**  
Encryption in Transit for Azure Files NFS v4.1 volumes in AKS is now generally available, enabling secure, TLS-encrypted communication between AKS workloads and Azure Files shares via the Azure File CSI driver.

---


*This report was automatically generated - 2026-07-18 03:02:45 UTC*