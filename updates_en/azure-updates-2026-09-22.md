# September 22, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: September 22, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 3 items

## Update List

### 1. Generally Available: Azure Sphere OS version 26.09 is now available

**Published**: September 21, 2026 18:44:49 UTC
**Link**: [Generally Available: Azure Sphere OS version 26.09 is now available](https://azure.microsoft.com/updates?id=572579)

**Update ID**: 572579
**Data source**: Azure Updates API

**Categories**: Launched, Internet of Things, Azure Sphere, Operating System

**Summary**:

**- What was updated:**  
Azure Sphere OS version 26.09 is now generally available in the Retail feed.

**- Key changes or new features:**  
This release includes updates to the Azure Sphere operating system only. There are no changes or updates to the Azure Sphere SDK in this release. Devices connected to the internet will automatically receive the new OS version from the cloud.

**- Target audience affected:**  
Developers and IT professionals managing Azure Sphere devices and solutions, particularly those responsible for device security, OS maintenance, and deployment.

**- Important notes if any:**  
- No SDK update is required for this OS release; existing development workflows remain unchanged.
- Ensure your devices are connected to the internet to receive the update automatically.
- Review the official release notes for any device-specific considerations or known issues.
- This update is relevant for maintaining device security and compliance with the latest Azure Sphere OS standards.

For more details, refer to the official update: [Azure Update: Azure Sphere OS version 26.09](https://azure.microsoft.com/updates?id=572579)

**Details**:

**Azure Sphere OS version 26.09 Now Generally Available: Technical Report**

**Background and Purpose of the Update**  
Azure Sphere is Microsoft’s end-to-end security platform for IoT devices, combining a secure microcontroller unit (MCU), a Linux-based OS, and a cloud-based security service. The release of Azure Sphere OS version 26.09 in the Retail feed is part of Microsoft’s ongoing commitment to maintaining and improving the security, reliability, and performance of Azure Sphere devices. This update focuses exclusively on the OS, with no changes to the SDK, ensuring device firmware remains current and protected against emerging threats.

**Specific Features and Detailed Changes**  
Azure Sphere OS version 26.09 delivers updates solely to the operating system. While the detailed change log is not provided in the announcement, typical OS updates may include security patches, bug fixes, stability improvements, and optimizations for device performance. There are no modifications to the SDK, so development workflows and APIs remain unchanged. Devices connected to the internet will automatically receive the updated OS, ensuring seamless and consistent deployment across managed fleets.

**Technical Mechanisms and Implementation Methods**  
The update is distributed via the Azure Sphere Retail feed, which is Microsoft’s cloud-based delivery channel for production OS releases. Devices configured for the Retail feed and connected to the internet will automatically download and install the new OS version. This process leverages Azure Sphere’s built-in secure update mechanism, which validates the integrity and authenticity of the OS package before installation, minimizing the risk of unauthorized or corrupted updates. No manual intervention is required for devices already set to receive updates from the Retail feed.

**Use Cases and Application Scenarios**  
Azure Sphere OS updates are critical for organizations deploying IoT solutions in environments where security and reliability are paramount, such as industrial automation, smart buildings, and connected consumer devices. The automatic update process ensures that devices remain compliant with the latest security standards, reducing operational risk and maintenance overhead. IT professionals can leverage this update to maintain device health and minimize vulnerabilities in their IoT infrastructure.

**Important Considerations and Limitations**  
- The update applies only to the OS; there are no changes to the SDK. Developers do not need to update their development tools or modify application code for compatibility with this OS release.
- Devices must be connected to the internet and configured for the Retail feed to receive the update automatically.
- Organizations should verify device connectivity and update policies to ensure timely adoption of the new OS version.
- No information is provided regarding deprecated features or breaking changes, but it is recommended to monitor device behavior post-update and review Microsoft’s documentation for any additional guidance.

**Integration with Related Azure Services**  
Azure Sphere OS updates are tightly integrated with Azure Sphere’s cloud-based security services, which provide ongoing threat detection, device health monitoring, and secure update delivery. The update mechanism ensures that devices remain synchronized with Azure’s security infrastructure, enabling seamless integration with Azure IoT Hub, Azure Defender for IoT, and other Azure services. This alignment supports comprehensive device management, security monitoring, and compliance reporting within the Azure ecosystem.

**Summary Sentence**  
Azure Sphere OS version 26.09 is now generally available in the Retail feed, providing automatic, cloud-delivered OS updates to connected devices, with no changes to the SDK, thereby enhancing security and reliability for IoT deployments.

---

### 2. Public Preview: Introducing a Guided Copilot Experience for Building Azure Apps in VS Code

**Published**: September 21, 2026 16:58:19 UTC
**Link**: [Public Preview: Introducing a Guided Copilot Experience for Building Azure Apps in VS Code](https://azure.microsoft.com/updates?id=572214)

**Update ID**: 572214
**Data source**: Azure Updates API

**Categories**: In preview, Developer tools, Visual Studio Code, Features, SDK and Tools, Feature

**Summary**:

- What was updated  
A new guided Copilot experience for building and deploying Azure applications in Visual Studio Code (VS Code) is now available in public preview.

- Key changes or new features  
This update introduces a structured, step-by-step workflow within VS Code, powered by GitHub Copilot, to help users move from app idea to deployment on Azure. Unlike the previous free-form chat approach, this guided experience provides a predictable and repeatable process for building cloud apps. It integrates Copilot’s AI assistance directly into common Azure development tasks, including code generation, configuration, and deployment.

- Target audience affected  
Developers and IT professionals who use VS Code for Azure application development, especially those leveraging GitHub Copilot for AI-assisted coding and deployment.

- Important notes if any  
The guided Copilot experience is currently in public preview and may be subject to changes before general availability. Users can expect improved productivity and reduced friction when building Azure apps, but should be aware of potential limitations or bugs typical of preview releases. Feedback is encouraged to help refine the experience.  
For more details, see the official update: https://azure.microsoft.com/updates?id=572214

**Details**:

**Azure Update Report**

**Title:** Public Preview: Introducing a Guided Copilot Experience for Building Azure Apps in VS Code  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=572214)

---

**Background and Purpose of the Update:**  
This update introduces a public preview of a new workflow for building cloud applications on Azure using GitHub Copilot within Visual Studio Code (VS Code). The primary purpose is to enhance the developer experience by providing a structured, guided process for app creation and deployment, moving away from the less predictable free-form chat sessions typically associated with Copilot. This aims to streamline the journey from initial idea to deployed Azure app, making it more efficient and reliable for developers.

**Specific Features and Detailed Changes:**  
- A new guided Copilot experience is available in VS Code, specifically tailored for Azure app development.
- The workflow is structured and predictable, offering step-by-step guidance rather than open-ended chat interactions.
- The experience covers the entire lifecycle: from ideation, through coding, to deployment on Azure.
- This preview replaces the traditional Copilot chat interface with a workflow-driven approach, ensuring developers follow best practices and standardized procedures for Azure app deployment.

**Technical Mechanisms and Implementation Methods:**  
- The guided Copilot experience is integrated directly into VS Code, leveraging GitHub Copilot’s AI capabilities.
- The workflow is implemented as a series of interactive steps or prompts, each designed to guide the developer through specific tasks such as project setup, code generation, configuration, and deployment.
- The experience is tightly coupled with Azure deployment mechanisms, enabling seamless transition from local development to cloud deployment.
- The structured workflow reduces ambiguity and helps developers avoid common pitfalls by providing context-aware suggestions and actions.

**Use Cases and Application Scenarios:**  
- Rapid prototyping and deployment of Azure cloud applications by developers using VS Code.
- Onboarding new developers to Azure app development with a simplified, guided process.
- Ensuring consistent and repeatable deployment workflows for teams building Azure solutions.
- Educational scenarios where developers can learn Azure app development through a hands-on, guided experience.

**Important Considerations and Limitations:**  
- This feature is currently in public preview, so it may not be suitable for production environments.
- The workflow is designed for Azure app development; it may not support other cloud platforms or non-Azure deployment scenarios.
- As a preview feature, there may be limitations in supported app types, deployment options, or integration depth.
- Developers should be aware of potential changes or enhancements as the feature evolves towards general availability.

**Integration with Related Azure Services:**  
- The guided Copilot experience is optimized for Azure, ensuring compatibility with Azure deployment pipelines and services.
- It leverages Azure APIs and deployment tools within the VS Code environment, enabling end-to-end app creation and deployment.
- The workflow is expected to integrate with Azure resource provisioning, configuration, and monitoring tools, providing a cohesive development and deployment experience.

---

**Summary Sentence:**  
This public preview introduces a structured, guided Copilot workflow in VS Code for building and deploying Azure apps, offering developers a predictable and efficient process from ideation to cloud deployment, with integrated Azure service support.

---

### 3. Generally Available: Azure Functions support for PowerShell 7.6

**Published**: September 21, 2026 16:55:34 UTC
**Link**: [Generally Available: Azure Functions support for PowerShell 7.6](https://azure.microsoft.com/updates?id=572219)

**Update ID**: 572219
**Data source**: Azure Updates API

**Categories**: Launched, Compute, Containers, Internet of Things, Azure Functions, Security, Services, Feature

**Summary**:

- What was updated  
Azure Functions now generally supports PowerShell 7.6.

- Key changes or new features  
Developers can build and run Azure Functions apps using PowerShell 7.6 both locally and in the cloud. This update enables access to the latest PowerShell features, performance improvements, and security updates introduced in version 7.6. Apps can be developed locally with PowerShell 7.6 and deployed seamlessly to any Azure Functions plan.

- Target audience affected  
This update is relevant for developers and IT professionals who use Azure Functions with PowerShell for automation, serverless workflows, or integration tasks.

- Important notes if any  
Existing Azure Functions apps using earlier PowerShell versions can be updated to 7.6 to take advantage of new features and security enhancements. Review the official documentation for guidance on updating your app to PowerShell 7.6 and to learn about the changes in this version. Testing is recommended to ensure compatibility with your scripts and dependencies before upgrading in production environments.

Learn more: [Updating your app to PowerShell 7.6](https://learn.microsoft.com/azure/azure-functions/update-your-app-to-powershell-7-6) | [What's new in PowerShell 7.6?](https://learn.microsoft.com/powershell/scripting/whats-new/what-s-new-in-powershell-76)

**Details**:

**Azure Update Report: Azure Functions support for PowerShell 7.6 (Generally Available)**

**Background and Purpose of the Update:**  
Azure Functions is a serverless compute service that enables users to run event-driven code without managing infrastructure. PowerShell support in Azure Functions allows IT professionals to automate tasks and orchestrate workflows using familiar scripting tools. The general availability of PowerShell 7.6 support addresses the need for up-to-date scripting environments, ensuring compatibility with the latest PowerShell features and improvements. This update enables developers and IT professionals to leverage PowerShell 7.6 for local development and deployment to Azure Functions, aligning with modern scripting standards and enhancing automation capabilities.

**Specific Features and Detailed Changes:**  
With this update, Azure Functions now supports PowerShell 7.6 as a runtime environment. Users can develop Azure Functions apps using PowerShell 7.6 locally and deploy them to Azure Functions plans. This includes access to new cmdlets, language enhancements, and performance improvements introduced in PowerShell 7.6. The update ensures that function apps can utilize the latest PowerShell modules and features, providing a consistent experience between local development and cloud deployment.

**Technical Mechanisms and Implementation Methods:**  
The implementation involves updating the Azure Functions runtime to recognize and execute PowerShell 7.6 scripts. Developers can select PowerShell 7.6 as the runtime version when creating function apps. Local development is facilitated by installing PowerShell 7.6 on the developer’s machine, ensuring compatibility with the Azure Functions runtime. Deployment to Azure Functions plans is seamless, as the platform now includes PowerShell 7.6 as a supported environment. This allows for streamlined CI/CD workflows and integration with Azure DevOps or other automation tools.

**Use Cases and Application Scenarios:**  
Typical use cases include automation of cloud resource management, scheduled maintenance tasks, and orchestration of complex workflows across Azure services. IT professionals can use PowerShell 7.6 in Azure Functions to automate provisioning, configuration, and monitoring of Azure resources. The update is particularly beneficial for organizations standardizing on PowerShell 7.6 for their scripting needs, enabling consistent automation practices across local and cloud environments.

**Important Considerations and Limitations:**  
When updating function apps to PowerShell 7.6, it is important to verify compatibility with existing scripts and modules. Some older modules may require updates to function correctly in PowerShell 7.6. Developers should review the official documentation for guidance on updating apps and understanding what’s new in PowerShell 7.6. Additionally, the update is applicable to Azure Functions plans, so users should ensure their deployment targets are compatible. Testing locally before deployment is recommended to avoid runtime issues.

**Integration with Related Azure Services:**  
Azure Functions with PowerShell 7.6 can be integrated with other Azure services such as Azure Logic Apps, Azure Event Grid, and Azure Monitor for comprehensive automation and event-driven workflows. Function apps can interact with Azure Resource Manager APIs, manage Azure resources, and trigger actions based on events from various Azure services. The update enhances interoperability and enables advanced automation scenarios leveraging the latest PowerShell capabilities.

**Summary:**  
Azure Functions now generally supports PowerShell 7.6, enabling IT professionals to develop and deploy serverless automation solutions using the latest PowerShell features, with seamless integration across Azure services and improved compatibility for modern scripting workflows.

---


*This report was automatically generated - 2026-09-22 03:02:32 UTC*