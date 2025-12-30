# December 30, 2025 - Azure Updates Summary Report (Details Mode)

**Generated on**: December 30, 2025
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Deprecation of Custom Resource Providers

**Published**: December 29, 2025 17:30:40 UTC
**Link**: [Retirement: Deprecation of Custom Resource Providers](https://azure.microsoft.com/updates?id=513892)

**Update ID**: 513892
**Data source**: Azure Updates API

**Categories**: Management and governance, Azure Resource Manager, Retirements

**Summary**:

- What was updated  
Azure announced the deprecation and retirement timeline for the Custom Resource Provider (CuRP) service within Azure Resource Manager.

- Key changes or new features  
The CuRP service will be retired by October 31, 2026. A “scream test” (a warning test to identify issues) will be conducted on October 27, 2025. After July 31, 2026, creation of new CuRP instances will no longer be supported.

- Target audience affected  
Developers and IT professionals who build, manage, or rely on Custom Resource Providers in their Azure environments will be impacted. This includes teams using CuRP for extending Azure Resource Manager capabilities with custom resources.

- Important notes if any  
Users should plan to migrate away from CuRP before the retirement date to avoid service disruption. It is recommended to explore alternative Azure services or native resource providers that can fulfill similar requirements. Monitoring the October 2025 scream test will be critical to identify potential issues early. Detailed migration guidance is expected to be provided by Microsoft ahead of the retirement.  

For more information, visit: https://azure.microsoft.com/updates?id=513892

**Details**:

The Azure update titled "Retirement: Deprecation of Custom Resource Providers" announces the planned deprecation and retirement of the Custom Resource Provider (CuRP) service within Azure Resource Manager (ARM), effective October 31, 2026. This update is critical for IT professionals managing custom resource integrations in Azure, as it impacts how custom resources are provisioned and managed via ARM.

**Background and Purpose of the Update**  
Custom Resource Providers have historically enabled organizations to extend Azure Resource Manager by defining and managing custom resources that are not natively supported by Azure. This capability allowed enterprises to integrate proprietary or third-party services into ARM’s declarative deployment model, enabling consistent infrastructure-as-code practices. However, with evolving Azure native capabilities, improved extensibility models, and the introduction of alternative integration mechanisms, Microsoft is retiring CuRP to streamline ARM and encourage adoption of more modern, scalable approaches.

**Specific Features and Detailed Changes**  
The update specifies a phased deprecation timeline:  
- October 27, 2025: A "scream test" will be conducted to identify and notify users of any breaking changes or dependencies on CuRP.  
- July 31, 2026: Creation of new Custom Resource Providers will be disabled.  
- October 31, 2026: Full retirement of CuRP, including disabling existing CuRP instances and associated APIs.

This means that after July 31, 2026, no new CuRPs can be registered, and by October 31, 2026, all existing CuRPs will cease functioning. Users must plan migration strategies well in advance.

**Technical Mechanisms and Implementation Methods**  
CuRP operates by allowing users to define custom resource types and implement RESTful endpoints that ARM calls during deployment operations. ARM treats these endpoints as first-class resources, enabling CRUD operations on custom-defined resource types within ARM templates or Bicep files.

With the deprecation, these RESTful endpoints and the CuRP registration mechanism will no longer be supported. Microsoft recommends transitioning to alternative extensibility options such as:  
- Azure Resource Manager extensions like Azure Managed Applications or Azure Blueprints for packaging and deploying complex solutions.  
- Azure Functions or Logic Apps integrated with ARM templates for custom provisioning logic.  
- Azure Policy and Azure Automation for governance and operational automation.  
- Azure Arc-enabled services for hybrid and multi-cloud resource management.

**Use Cases and Application Scenarios**  
CuRP was primarily used in scenarios where organizations needed to:  
- Integrate proprietary or third-party services into ARM’s deployment lifecycle.  
- Provide custom provisioning logic that ARM did not natively support.  
- Enable declarative management of non-Azure resources via ARM templates.

Common examples included managing on-premises resources, third-party SaaS configurations, or bespoke internal services as ARM resources.

**Important Considerations and Limitations**  
- Migration Planning: Organizations must audit their ARM templates and deployment pipelines to identify CuRP dependencies and develop migration plans to alternative solutions before the cutoff dates.  
- Feature Parity: Alternative approaches may require re-architecting deployment logic and may not provide identical functionality or seamless ARM integration.  
- Testing: The October 2025 scream test provides an opportunity to detect breaking changes early; thorough testing is essential.  
- Compliance and Governance: Ensure that any new approach complies with organizational policies and governance frameworks.

**Integration with Related Azure Services**  
The retirement of CuRP encourages deeper integration with other Azure services:  
- Azure Functions and Logic Apps can replace CuRP endpoints for custom provisioning workflows.  
- Azure Managed Applications provide a packaged deployment model with lifecycle management.  
- Azure Policy can enforce compliance during resource deployment.  
- Azure Blueprints enable repeatable environment deployments incorporating governance.  
- Azure Arc extends resource management beyond Azure, offering hybrid cloud capabilities that may substitute some CuRP use cases.

In summary, the deprecation of Custom Resource Providers reflects Microsoft’s strategic shift towards more robust, scalable, and integrated extensibility

---


*This report was automatically generated - 2025-12-30 03:01:16 UTC*