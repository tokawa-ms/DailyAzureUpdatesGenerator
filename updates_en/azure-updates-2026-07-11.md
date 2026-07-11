# July 11, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: July 11, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Support for Python-2.7; 3.8 and PowerShell- 7.1; 7.2 will be retired on September 30, 2026

**Published**: July 10, 2026 21:33:34 UTC
**Link**: [Retirement: Support for Python-2.7; 3.8 and PowerShell- 7.1; 7.2 will be retired on September 30, 2026](https://azure.microsoft.com/updates?id=567556)

**Update ID**: 567556
**Data source**: Azure Updates API

**Categories**: Management and governance, Automation, Retirements, Compliance, Security

**Summary**:

- What was updated  
Azure Automation will retire support for Python 2.7, Python 3.8, PowerShell 7.1, and PowerShell 7.2 runtime versions.

- Key changes or new features  
Starting October 1, 2026, these runtime versions will no longer be supported in Azure Automation. Runbooks using these versions may continue to execute but will not receive security updates, bug fixes, or technical support. Users are encouraged to migrate runbooks to newer, supported runtime versions to ensure continued security and support.

- Target audience affected  
Developers and IT professionals who use Azure Automation runbooks with Python 2.7, Python 3.8, PowerShell 7.1, or PowerShell 7.2.

- Important notes if any  
It is critical to review and update existing runbooks to use supported Python and PowerShell versions before September 30, 2026. Continuing to use unsupported runtimes after this date may expose workloads to security risks and operational issues due to lack of updates and support. For migration guidance and supported versions, refer to Azure Automation documentation.

**Details**:

**Azure Update Report: Retirement of Support for Python 2.7, Python 3.8, PowerShell 7.1, and PowerShell 7.2 in Automation (Effective September 30, 2026)**

**Background and Purpose of the Update**  
Microsoft Azure is announcing the retirement of support for specific runtime versions in Azure Automation: Python 2.7, Python 3.8, PowerShell 7.1, and PowerShell 7.2. The purpose of this update is to ensure that Azure Automation environments remain secure, maintainable, and aligned with industry standards by discontinuing support for older runtime versions that no longer receive upstream security updates or enhancements.

**Specific Features and Detailed Changes**  
Starting October 1, 2026, Azure Automation will no longer support the aforementioned runtime versions. Runbooks utilizing these versions may continue to execute, but they will not benefit from any further security updates, bug fixes, or official support. This change affects the execution environment for Automation runbooks, which are scripts and workflows used to automate operational tasks within Azure.

**Technical Mechanisms and Implementation Methods**  
Azure Automation relies on managed runtime environments to execute runbooks. The retirement means that the platform will cease to provide maintenance and patching for Python 2.7, Python 3.8, PowerShell 7.1, and PowerShell 7.2. While the execution of existing runbooks is not immediately blocked, the underlying runtime environments will become static and unsupported, exposing potential risks due to unpatched vulnerabilities and incompatibilities with newer Azure features.

**Use Cases and Application Scenarios**  
Typical use cases affected include:
- Automation of cloud resource management (e.g., VM provisioning, scaling, and deprovisioning)
- Scheduled maintenance tasks (e.g., patching, backups)
- Integration workflows across Azure services (e.g., Logic Apps, Event Grid)
- Custom operational scripts written in Python or PowerShell for infrastructure orchestration

Runbooks written in the retiring versions will continue to function, but organizations are strongly advised to migrate scripts to supported runtime versions to ensure ongoing reliability and security.

**Important Considerations and Limitations**  
- **Security Risks:** Unsupported runtimes will not receive security updates, increasing exposure to vulnerabilities.
- **Compliance:** Organizations with regulatory requirements may be unable to use unsupported runtimes.
- **Migration Requirement:** IT teams must plan to refactor and test runbooks in newer, supported versions of Python and PowerShell prior to the retirement date.
- **No Blocking:** Execution is not blocked, but lack of support means no assistance from Microsoft for issues arising after retirement.
- **Dependency Management:** Scripts relying on deprecated libraries or syntax may require significant updates for compatibility with newer runtime versions.

**Integration with Related Azure Services**  
Azure Automation is often integrated with services such as Azure Logic Apps, Azure Functions, Azure Monitor, and Azure Resource Manager. The retirement of these runtimes may impact workflows and integrations that depend on Automation runbooks. It is essential to review dependencies and ensure that all integrations are compatible with updated runtime environments.

**Summary Sentence**  
Azure Automation will retire support for Python 2.7, Python 3.8, PowerShell 7.1, and PowerShell 7.2 on September 30, 2026; after this date, runbooks using these versions will not receive security updates or bug fixes, and IT professionals should migrate scripts to supported runtime versions to maintain security and compliance.

---


*This report was automatically generated - 2026-07-11 03:01:02 UTC*