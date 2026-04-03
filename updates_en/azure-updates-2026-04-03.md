# April 03, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: April 03, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Retirement: Python support for Azure App Service and Azure Functions on Windows will be retired on March 31, 2027 

**Published**: April 02, 2026 16:45:52 UTC
**Link**: [Retirement: Python support for Azure App Service and Azure Functions on Windows will be retired on March 31, 2027 ](https://azure.microsoft.com/updates?id=558027)

**Update ID**: 558027
**Data source**: Azure Updates API

**Categories**: Compute, Mobile, Web, App Service, Retirements

**Summary**:

- What was updated  
Microsoft announced the retirement of Python support for Azure App Service and Azure Functions running on Windows, effective March 31, 2027.

- Key changes or new features  
After March 31, 2027, Python applications deployed on Azure App Service (Windows) and Azure Functions (Windows) will no longer execute. While application configuration and content will remain, the apps themselves will stop running. There are no new features—this is a deprecation notice.

- Target audience affected  
Developers and IT professionals who deploy or manage Python applications using Azure App Service (Windows) or Azure Functions (Windows).

- Important notes if any  
To avoid service disruption, migrate your Python workloads to supported platforms, such as Azure App Service on Linux or Azure Functions on Linux, before the retirement date. Review your current deployments and plan migration strategies as soon as possible. No immediate action is required, but applications will cease to run after the retirement date if not migrated.

For more details, refer to the official update: https://azure.microsoft.com/updates?id=558027

**Details**:

**Azure Update Report: Retirement of Python Support for Azure App Service and Azure Functions on Windows (Effective March 31, 2027)**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of Python support for Azure App Service and Azure Functions on Windows, effective March 31, 2027. This update is part of Azure’s ongoing platform evolution and lifecycle management, ensuring that resources are allocated to maintaining and enhancing supported features. The retirement aims to streamline the platform and encourage customers to migrate to supported environments.

**Specific Features and Detailed Changes:**  
- After March 31, 2027, any Python applications deployed on Azure App Service (Windows) or Azure Functions (Windows) will no longer execute.  
- The application configuration and content will remain available within the Azure environment, but the applications themselves will cease to run.  
- There is no indication of automatic migration or conversion; the update solely affects the runtime availability of Python workloads on these Windows-based services.

**Technical Mechanisms and Implementation Methods:**  
- The retirement is enforced at the platform level. Azure will disable the execution of Python runtimes for both App Service and Functions hosted on Windows OS.  
- Existing deployments will not be deleted; however, the runtime environment required to execute Python code will be removed or disabled, resulting in application downtime for affected workloads.  
- No changes are made to the underlying file storage or configuration; only the runtime execution is impacted.

**Use Cases and Application Scenarios:**  
- This update directly impacts organizations running Python-based web applications or serverless functions on Azure App Service (Windows) or Azure Functions (Windows).  
- Typical use cases include REST APIs, web applications, data processing jobs, and event-driven automation written in Python and hosted on the Windows variant of these services.  
- Applications running on Linux-based App Service or Functions are not mentioned in this update and are therefore not affected.

**Important Considerations and Limitations:**  
- Applications will stop running after the retirement date, even though their content and configuration remain.  
- There is no mention of migration tooling or automated assistance; customers are responsible for migrating their workloads to supported platforms before the retirement date.  
- The update does not affect other languages or workloads on Windows App Service/Functions, nor does it affect Python workloads on Linux-based hosting.  
- Customers must plan for migration to avoid service disruption, such as redeploying Python applications to App Service (Linux) or Azure Functions (Linux).

**Integration with Related Azure Services:**  
- Integrations with other Azure services (e.g., Azure Storage, Azure SQL Database, Azure Key Vault) are not directly impacted, but any Python-based logic interacting with these services via App Service (Windows) or Functions (Windows) must be migrated to a supported environment to maintain operational continuity.  
- Azure provides equivalent Linux-based hosting options for both App Service and Functions, which support Python and can be leveraged as migration targets.

**Summary:**  
Python support for Azure App Service and Azure Functions on Windows will be retired on March 31, 2027; after this date, Python applications on these services will stop running, though configuration and content will remain intact.

---

### 2. Retirement: AzureDnsEndpoints for Azure storage accounts will be retired March 2027

**Published**: April 02, 2026 16:30:09 UTC
**Link**: [Retirement: AzureDnsEndpoints for Azure storage accounts will be retired March 2027](https://azure.microsoft.com/updates?id=558276)

**Update ID**: 558276
**Data source**: Azure Updates API

**Categories**: Storage, Azure Blob Storage, Retirements

**Summary**:

- What was updated  
AzureDnsZone endpoints (preview) for Azure Blob storage accounts will be retired in March 2027.

- Key changes or new features  
The AzureDnsZone endpoints feature, currently in preview, will no longer be supported after March 2027. Microsoft recommends transitioning to Standard endpoints for all new and existing Azure Blob storage account deployments. No new features are being introduced; this is a deprecation notice.

- Target audience affected  
Developers and IT professionals managing Azure Blob storage accounts that utilize AzureDnsZone endpoints (preview). This includes those responsible for storage account configuration, network integration, and DNS management in Azure environments.

- Important notes if any  
- All workloads using AzureDnsZone endpoints (preview) must be migrated to Standard endpoints before March 2027 to avoid service disruption.  
- Existing deployments relying on AzureDnsZone endpoints should be reviewed and updated as part of ongoing maintenance.  
- No action is required for storage accounts already using Standard endpoints.  
- Review the official retirement notice and plan migration strategies accordingly to ensure business continuity.

For more details, see the official update: https://azure.microsoft.com/updates?id=558276

**Details**:

**Azure Update Report**

**Title:** Retirement: AzureDnsEndpoints for Azure storage accounts will be retired March 2027  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=558276)

---

**Background and Purpose of the Update:**  
AzureDnsZone endpoints (preview) for Azure Blob storage accounts are scheduled for retirement in March 2027. The purpose of this update is to inform customers that the AzureDnsZone endpoint feature, which has been available in preview, will no longer be supported after this date. Microsoft recommends that customers transition to Standard endpoints for all new and existing Blob storage account deployments to ensure continued support and compatibility.

**Specific Features and Detailed Changes:**  
The primary change is the deprecation of AzureDnsZone endpoints (preview) for Blob storage accounts. This means that after March 2027, customers will not be able to use AzureDnsZone endpoints for Blob storage and must utilize Standard endpoints instead. The Standard endpoint is the default endpoint type for Azure Blob storage and provides stable, production-ready DNS addressing for storage account access.

**Technical Mechanisms and Implementation Methods:**  
AzureDnsZone endpoints (preview) allowed customers to leverage custom DNS zone endpoints for Blob storage accounts, potentially offering more granular DNS management and integration with Azure DNS. With the retirement, customers must revert to using Standard endpoints, which are typically in the format:  
`https://<storage-account-name>.blob.core.windows.net`  
Transitioning involves updating application configurations, scripts, and any automation to reference the Standard endpoint format. Existing deployments using AzureDnsZone endpoints should be reconfigured to use Standard endpoints before the retirement date to avoid service disruption.

**Use Cases and Application Scenarios:**  
AzureDnsZone endpoints (preview) were primarily used in scenarios requiring custom DNS integration or advanced DNS management for Blob storage accounts, such as multi-region deployments or environments with specific DNS requirements. With the retirement, these use cases must be re-evaluated and migrated to Standard endpoints, which are suitable for most production workloads and offer robust compatibility with Azure networking and security features.

**Important Considerations and Limitations:**  
- After March 2027, AzureDnsZone endpoints (preview) will no longer be available or supported for Blob storage accounts.
- Customers must ensure all new and existing Blob storage deployments use Standard endpoints.
- Any application, script, or automation referencing AzureDnsZone endpoints must be updated to avoid connectivity issues.
- The transition may require coordination with DNS management, application development, and operational teams to ensure seamless migration.

**Integration with Related Azure Services:**  
Standard endpoints for Blob storage accounts are fully compatible with Azure networking, Azure DNS, Azure Private Link, and other Azure services. Transitioning to Standard endpoints ensures continued integration with security features such as firewalls, virtual networks, and access control mechanisms. Customers leveraging Azure DNS or custom DNS solutions should review their integration strategies to align with Standard endpoint usage.

---

**Summary Sentence:**  
AzureDnsZone endpoints (preview) for Azure Blob storage accounts will be retired in March 2027, and customers should transition to Standard endpoints for all new and existing Blob storage deployments to maintain support and compatibility.

---


*This report was automatically generated - 2026-04-03 03:02:02 UTC*