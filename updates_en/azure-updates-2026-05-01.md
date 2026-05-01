# May 01, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: May 01, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Generally Available: Prefix-scoped access for User Delegation SAS 

**Published**: April 30, 2026 18:00:11 UTC
**Link**: [Generally Available: Prefix-scoped access for User Delegation SAS ](https://azure.microsoft.com/updates?id=561257)

**Update ID**: 561257
**Data source**: Azure Updates API

**Categories**: Launched, Storage, Azure Blob Storage, Features

**Summary**:

- What was updated  
Prefix-scoped access for User Delegation Shared Access Signatures (SAS) in Azure Blob Storage is now generally available in all Azure regions.

- Key changes or new features  
Previously, SAS tokens for Blob Storage only supported container-level or individual blob-level access. With this update, developers and IT professionals can now create User Delegation SAS tokens scoped to a specific prefix (i.e., a virtual folder or subset of blobs within a container). This enables more granular access control, allowing access to all blobs with a specified prefix without granting permissions to the entire container.

- Target audience affected  
Developers and IT professionals managing Azure Blob Storage security and access, especially those implementing fine-grained access controls in applications or automation scripts.

- Important notes if any  
Prefix-scoped SAS enhances security by reducing the scope of permissions granted, supporting the principle of least privilege. Existing SAS tokens at the container or blob level continue to work as before. No changes are required to existing applications unless you wish to adopt the new prefix-scoped capability. For more information, see the official documentation: https://azure.microsoft.com/updates?id=561257

**Details**:

**Azure Update Report: Prefix-scoped Access for User Delegation SAS in Azure Blob Storage**

**Background and Purpose of the Update**  
Historically, Shared Access Signature (SAS) tokens for Azure Blob Storage have allowed access to either an entire container or an individual blob. This binary scope limited flexibility for scenarios where granular access to a subset of blobs was required. The purpose of this update is to introduce prefix-scoped access for User Delegation SAS, enabling more precise and secure access control within Blob Storage.

**Specific Features and Detailed Changes**  
With this release, SAS tokens can now be scoped to a specific prefix within a container. This means that instead of granting access to all blobs in a container or a single blob, administrators can grant access to all blobs whose names start with a specified prefix. This feature is generally available in all Azure regions and applies specifically to User Delegation SAS, which leverages Azure Active Directory (AAD) for authentication.

**Technical Mechanisms and Implementation Methods**  
Prefix-scoped access is implemented by specifying a blob name prefix when generating a User Delegation SAS token. The SAS token is then valid for any blob within the container whose name matches the defined prefix. This mechanism leverages Azure’s existing SAS infrastructure, but extends the granularity of access control. User Delegation SAS tokens are created using Azure AD credentials, ensuring that access is managed through modern identity and access management practices.

To generate a prefix-scoped User Delegation SAS, IT professionals can use Azure SDKs, CLI, or REST APIs, specifying the desired prefix in the SAS parameters. The token will then enforce access restrictions at the prefix level, allowing operations such as read, write, or delete only on blobs matching the prefix.

**Use Cases and Application Scenarios**  
- **Multi-tenant applications:** Grant each tenant access to blobs with a unique prefix, isolating their data without creating separate containers.
- **Data lifecycle management:** Provide access to blobs with a prefix corresponding to a date or category, facilitating automated workflows.
- **Delegated access:** Enable third-party services or users to interact only with blobs relevant to their function, improving security and compliance.
- **Batch processing:** Allow batch jobs to process blobs with a specific prefix, streamlining data operations.

**Important Considerations and Limitations**  
- Prefix-scoped access is available only for User Delegation SAS, not for account SAS.
- The prefix must be accurately defined to avoid unintended access; improper prefix selection may result in broader access than intended.
- All operations permitted by the SAS token will apply to blobs matching the prefix, so permissions should be carefully scoped.
- As with all SAS tokens, expiration and revocation must be managed to maintain security.

**Integration with Related Azure Services**  
Prefix-scoped User Delegation SAS tokens integrate seamlessly with Azure Blob Storage and Azure Active Directory. They can be used in conjunction with Azure Functions, Logic Apps, and other services that require delegated access to blob subsets. This feature enhances security and operational flexibility in scenarios where Azure AD-based access control is required.

**Summary Sentence**  
Prefix-scoped access for User Delegation SAS in Azure Blob Storage is now generally available, enabling granular, prefix-based access control for blobs within a container, thereby enhancing security and flexibility for delegated access scenarios across all Azure regions.

---

### 2. Generally Available: Azure Functions support for Java 25

**Published**: April 30, 2026 17:15:44 UTC
**Link**: [Generally Available: Azure Functions support for Java 25](https://azure.microsoft.com/updates?id=560879)

**Update ID**: 560879
**Data source**: Azure Updates API

**Categories**: In preview, Compute, Containers, Internet of Things, Azure Functions, Features, Open Source

**Summary**:

- What was updated  
Azure Functions now generally supports Java 25 for app development and deployment.

- Key changes or new features  
Developers can use Java 25 to build Azure Functions locally and deploy them to Azure Functions plans on both Linux and Windows platforms. This includes support for the Flex Consumption plan, enabling more flexible scaling and cost optimization options.

- Target audience affected  
Java developers building serverless applications, IT professionals managing Azure Functions environments, and DevOps teams deploying Java-based workloads to Azure.

- Important notes  
To leverage Java 25, ensure your local development environment and deployment pipelines are updated accordingly. Compatibility with Linux and Windows plans, including Flex Consumption, allows for broader deployment scenarios. Review your application dependencies for Java 25 readiness and refer to official documentation for migration guidance.

**Details**:

**Azure Update Technical Report: Generally Available – Azure Functions support for Java 25**

**Background and Purpose of the Update:**  
Azure Functions is Microsoft’s serverless compute platform, enabling event-driven execution of code in a variety of programming languages. Java is a widely adopted enterprise language, and Azure Functions has historically supported multiple Java versions. The general availability of Java 25 support reflects Azure’s commitment to keeping pace with the Java ecosystem, ensuring that developers can leverage the latest language features, security updates, and performance improvements in their serverless applications.

**Specific Features and Detailed Changes:**  
With this update, Azure Functions now officially supports Java 25 as a runtime for developing and deploying serverless applications. This support is available across both Linux and Windows hosting environments, including the Flex Consumption plan. Developers can now build Azure Functions projects targeting Java 25 locally and deploy them directly to Azure Functions without compatibility concerns. The update ensures that the Azure Functions runtime, build tools, and deployment pipelines are compatible with Java 25 bytecode and libraries.

**Technical Mechanisms and Implementation Methods:**  
- **Local Development:** Developers can use their preferred Java 25-compatible IDEs and build tools (such as Maven or Gradle) to create and test Azure Functions projects locally.
- **Deployment:** Once developed, these Java 25-based functions can be deployed to Azure Functions using standard deployment methods (e.g., Azure CLI, Visual Studio Code, GitHub Actions, or Azure DevOps pipelines).
- **Runtime Support:** The Azure Functions runtime on both Linux and Windows hosts has been updated to include Java 25, ensuring that function apps execute in an environment with the correct Java version and dependencies.
- **Flex Consumption Plan:** Java 25 support is extended to the Flex Consumption plan, which offers enhanced scaling and cost efficiency for serverless workloads.

**Use Cases and Application Scenarios:**  
- **Modern Java Applications:** Organizations adopting the latest Java features can now build serverless APIs, event-driven processing, and automation tasks using Java 25.
- **Enterprise Migration:** Enterprises maintaining Java-based workloads can migrate or modernize their existing functions to leverage Java 25’s enhancements.
- **Cross-Platform Deployments:** Teams can deploy Java 25 functions to both Linux and Windows environments, supporting diverse infrastructure requirements.
- **Cost-Optimized Serverless Computing:** By utilizing the Flex Consumption plan, developers can optimize costs for workloads with variable or unpredictable execution patterns.

**Important Considerations and Limitations:**  
- **Supported Plans:** Java 25 support is available on both Linux and Windows, including the Flex Consumption plan. Compatibility with other hosting plans should be verified based on official documentation.
- **Dependency Management:** Developers must ensure that all dependencies and libraries used in their function apps are compatible with Java 25.
- **Migration:** Existing Java function apps targeting earlier Java versions may require code or configuration updates to ensure compatibility with Java 25.
- **Documentation:** It is recommended to review the official Azure Functions documentation for any additional prerequisites or configuration steps specific to Java 25.

**Integration with Related Azure Services:**  
Azure Functions with Java 25 can be integrated with a wide range of Azure services, such as Azure Event Grid, Azure Service Bus, Azure Storage, and Azure Logic Apps, enabling robust event-driven architectures. The update ensures that Java 25-based functions can participate fully in these integrations, leveraging the latest Java runtime for improved performance and security.

**Summary Sentence:**  
Azure Functions now offers general availability support for Java 25, enabling developers to build and deploy serverless applications using the latest Java version across Linux and Windows environments, including the Flex Consumption plan.

---


*This report was automatically generated - 2026-05-01 03:01:14 UTC*