# March 19, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: March 19, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 10 items

## Update List

### 1. Retirement: Emissions Impact Dashboard for Azure

**Published**: March 18, 2026 18:45:54 UTC
**Link**: [Retirement: Emissions Impact Dashboard for Azure](https://azure.microsoft.com/updates?id=558278)

**Update ID**: 558278
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
The Emissions Impact Dashboard for Azure, hosted on Power BI, will be retired.

- Key changes or new features  
Effective March 31, 2027, the dashboard will no longer be accessible and technical support will end. No new features are being added; this is a retirement notice.

- Target audience affected  
Azure customers, developers, and IT professionals who use the Emissions Impact Dashboard to track and report cloud-related carbon emissions.

- Important notes  
Users should export any required data from the dashboard before March 31, 2027, as access and support will cease after this date. Organizations relying on the dashboard for sustainability reporting or compliance should begin planning for alternative solutions. No direct replacement or migration path has been announced, so users may need to explore other tools or custom reporting options for emissions tracking. For further details, refer to the official Azure Update announcement.

**Details**:

**Azure Update Report: Retirement of Emissions Impact Dashboard for Azure (Effective March 31, 2027)**

**Background and Purpose of the Update:**  
Microsoft has announced the retirement of the Emissions Impact Dashboard for Azure, which is currently hosted on Power BI. This dashboard has served as a tool for customers to visualize and analyze the carbon emissions associated with their Azure usage. The retirement is scheduled to take effect on March 31, 2027. The primary purpose of this update is to inform users of the discontinuation of both access to the dashboard and the cessation of technical support after the specified date.

**Specific Features and Detailed Changes:**  
- The Emissions Impact Dashboard for Azure, accessible via Power BI, will be decommissioned.
- After March 31, 2027, users will no longer be able to access the dashboard interface or its underlying data visualizations.
- Technical support for the dashboard will also be discontinued as of the retirement date.
- Microsoft strongly encourages customers to export their data from the dashboard before the retirement date to avoid data loss.

**Technical Mechanisms and Implementation Methods:**  
- The dashboard is currently implemented as a Power BI solution, which connects to Azure usage data to calculate and visualize emissions impact.
- Upon retirement, the Power BI workspace and any associated datasets, reports, or dashboards related to the Emissions Impact Dashboard for Azure will be removed or rendered inaccessible.
- Customers are advised to use Power BI’s export functionalities (such as exporting reports to Excel, PDF, or CSV) to retain historical emissions data for compliance, reporting, or internal analysis purposes.

**Use Cases and Application Scenarios:**  
- Organizations have used the Emissions Impact Dashboard to monitor, report, and optimize the carbon footprint of their Azure workloads.
- The dashboard has supported sustainability initiatives, compliance reporting, and internal environmental impact assessments.
- IT professionals and sustainability officers have leveraged the dashboard to inform decision-making regarding workload placement, resource optimization, and sustainability goals.

**Important Considerations and Limitations:**  
- After March 31, 2027, all access to the Emissions Impact Dashboard and its data will be permanently discontinued.
- No technical support or troubleshooting will be available for the dashboard after the retirement date.
- Customers must proactively export any required data before the cutoff date, as Microsoft will not provide access to historical dashboard data after retirement.
- The update does not specify any direct replacement or migration path for the dashboard’s functionality.

**Integration with Related Azure Services:**  
- The Emissions Impact Dashboard has been integrated with Azure services by leveraging Azure usage data to calculate emissions.
- The dashboard’s data sources typically include Azure billing and resource consumption metrics.
- The retirement may impact workflows that depend on automated or manual integration of emissions data with other Azure reporting or sustainability tools.

**Summary Sentence:**  
The Emissions Impact Dashboard for Azure, hosted on Power BI, will be retired on March 31, 2027, after which access and technical support will end; customers should export any necessary data before this date to ensure continued access to their emissions information.

---

### 2. General availability: Azure SQL updates for mid-March 2026 

**Published**: March 18, 2026 18:30:05 UTC
**Link**: [General availability: Azure SQL updates for mid-March 2026 ](https://azure.microsoft.com/updates?id=558121)

**Update ID**: 558121
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Azure SQL received several updates and enhancements in mid-March 2026.

- Key changes or new features  
  - Developers can now publish SQL database projects directly from Visual Studio Code, streamlining database deployment workflows and reducing the need for external tools or manual steps.  
  - Users can view and edit SQL table data directly within the Microsoft SQL extension for Visual Studio Code (MSSQ), improving productivity and simplifying data management tasks.

- Target audience affected  
  - Application developers and database administrators (DBAs) who use Azure SQL and Visual Studio Code for database development, deployment, and management.

- Important notes if any  
  - These updates enhance the developer experience by integrating critical database deployment and data management features into Visual Studio Code.  
  - Teams can expect improved efficiency and reduced context switching between tools when working with Azure SQL databases.  
  - No additional installation is required if you are already using the latest Microsoft SQL extension for Visual Studio Code.

For more details, refer to the official update: https://azure.microsoft.com/updates?id=558121

**Details**:

**Azure Update Report: General availability – Azure SQL updates for mid-March 2026**

**Background and Purpose of the Update**  
The mid-March 2026 Azure SQL update introduces enhancements aimed at streamlining database development and management workflows. The primary objective is to improve developer productivity and operational efficiency by enabling more direct and integrated interactions with Azure SQL databases, particularly within familiar development environments.

**Specific Features and Detailed Changes**  
1. **Publish SQL Database Projects Directly from Visual Studio Code**  
   - Developers can now deploy SQL database projects (.sqlproj) directly from Visual Studio Code (VS Code) to Azure SQL.  
   - This feature eliminates the need for intermediate tools or manual deployment steps, allowing for a more seamless and efficient database deployment workflow.

2. **View and Edit SQL Table Data Directly in MSSQ**  
   - Users gain the ability to view and edit SQL table data directly within the Microsoft SQL (MSSQ) environment.  
   - This enhancement provides a more interactive and immediate way to manage and manipulate table data without leaving the development or management interface.

**Technical Mechanisms and Implementation Methods**  
- The direct publishing capability leverages Visual Studio Code extensions that integrate with Azure SQL deployment APIs. This allows developers to connect to Azure SQL instances, validate schema changes, and execute deployment scripts from within VS Code.
- The view and edit functionality in MSSQ is likely implemented via enhanced data grid interfaces, enabling CRUD (Create, Read, Update, Delete) operations directly on table data. This reduces reliance on external SQL query editors or management portals for routine data operations.

**Use Cases and Application Scenarios**  
- **Continuous Integration/Continuous Deployment (CI/CD):** Teams can incorporate direct project publishing from VS Code into their CI/CD pipelines, reducing friction and manual steps during database deployment.
- **Agile Development:** Developers can quickly iterate on database schema and data changes, test modifications, and deploy updates without switching tools or contexts.
- **Data Management:** Database administrators and data engineers can efficiently inspect and update table data during development, testing, or troubleshooting scenarios.

**Important Considerations and Limitations**  
- Role-based access controls (RBAC) and permissions must be properly configured to allow publishing and data editing from development environments.
- Direct editing of table data should be carefully managed in production environments to avoid accidental data modification or loss.
- The update does not specify support for advanced deployment scenarios such as data masking, versioning, or rollback; users should validate these requirements separately.

**Integration with Related Azure Services**  
- The new features are designed to work seamlessly with Azure SQL Database and Azure SQL Managed Instance.
- Integration with Visual Studio Code aligns with Azure’s broader developer tooling ecosystem, supporting extensions for Azure Resource Manager, Azure DevOps, and GitHub Actions for end-to-end DevOps workflows.
- The ability to view and edit data in MSSQ complements existing Azure Portal and SQL Server Management Studio (SSMS) capabilities, offering more flexibility in how users interact with their data.

**Summary**  
The mid-March 2026 Azure SQL update enhances developer and administrator productivity by enabling direct publishing of SQL database projects from Visual Studio Code and providing in-place table data editing within MSSQ, streamlining database deployment and management workflows.

---

### 3. Generally Available: Azure Red Hat OpenShift Managed Identity and Workload Identity

**Published**: March 18, 2026 18:30:05 UTC
**Link**: [Generally Available: Azure Red Hat OpenShift Managed Identity and Workload Identity](https://azure.microsoft.com/updates?id=557917)

**Update ID**: 557917
**Data source**: Azure Updates API

**Categories**: Launched, Containers, Azure Red Hat OpenShift, Compliance, Management

**Summary**:

- What was updated  
Azure Red Hat OpenShift now offers general availability support for managed identities and workload identities.

- Key changes or new features  
Managed identities and workload identities can now be used for authentication in OpenShift clusters and applications running on Azure. This eliminates the need for long-lived service principal credentials, improving security and simplifying identity management. The update aligns Azure Red Hat OpenShift with Azure’s native identity and access management practices, enabling seamless integration with Azure resources and services.

- Target audience affected  
Developers deploying applications on Azure Red Hat OpenShift, IT professionals managing OpenShift clusters, and DevOps teams responsible for identity and access management in cloud environments.

- Important notes  
Existing OpenShift clusters can be updated to use managed identities and workload identities, reducing credential management overhead and risk. Adoption of these features is recommended to enhance security and compliance. Review Azure documentation for migration guidance and best practices. Managed identities are now the preferred method for authenticating workloads to Azure services from OpenShift.

**Details**:

**Azure Update Technical Report**

**Title:** Generally Available: Azure Red Hat OpenShift Managed Identity and Workload Identity  
**Link:** [Azure Update #557917](https://azure.microsoft.com/updates?id=557917)

---

### Background and Purpose of the Update

This update announces the general availability of managed identities and workload identities support in Azure Red Hat OpenShift (ARO). The primary objective is to enhance security and simplify identity management for OpenShift clusters and workloads running on Azure. Previously, service principal credentials—often long-lived and manually managed—were required for authentication between OpenShift workloads and Azure resources. This update eliminates the need for such credentials, reducing operational overhead and the risk associated with credential leakage or mismanagement.

---

### Specific Features and Detailed Changes

- **Managed Identity Support:** ARO clusters can now leverage Azure Managed Identities, allowing cluster components to securely authenticate to Azure services without explicit credentials.
- **Workload Identity Support:** OpenShift workloads (pods/applications) can use Azure Workload Identity, enabling them to access Azure resources securely using short-lived tokens, rather than static service principal secrets.
- **General Availability:** These features are now fully supported and recommended for production use.

---

### Technical Mechanisms and Implementation Methods

- **Managed Identities:** Azure Managed Identities are automatically managed Azure Active Directory (AAD) identities assigned to ARO clusters. When enabled, the cluster infrastructure (e.g., controllers, operators) can authenticate to Azure resources (such as Azure Key Vault, Storage, or SQL Database) using these identities. The Azure platform handles credential rotation and lifecycle management.
- **Workload Identities:** Workload Identity integrates Kubernetes Service Accounts with Azure AD. When a pod needs to access an Azure resource:
  - The pod is associated with a Kubernetes Service Account.
  - The Service Account is mapped to an Azure AD identity.
  - The pod obtains a short-lived token via the Azure AD Workload Identity webhook, which it uses to authenticate to Azure resources.
- **No Long-Lived Service Principals:** Both mechanisms remove the need to create, distribute, and manage long-lived service principal secrets within cluster configurations or application code.

---

### Use Cases and Application Scenarios

- **Secure Access to Azure Resources:** OpenShift applications (e.g., microservices, operators) can securely access Azure services such as Azure Key Vault, Azure Storage, or Azure SQL Database without embedding credentials.
- **Automated Identity Management:** Organizations can streamline identity lifecycle management for both infrastructure and workloads, reducing manual intervention and risk.
- **Regulatory Compliance:** Short-lived tokens and automated credential rotation help meet compliance requirements for credential management and access control.

---

### Important Considerations and Limitations

- **Configuration Required:** Enabling managed and workload identities requires proper configuration of ARO clusters and Azure AD permissions.
- **Role Assignments:** Appropriate Azure RBAC (Role-Based Access Control) assignments must be made to managed identities and mapped workload identities for resource access.
- **Compatibility:** Only supported on Azure Red Hat OpenShift clusters; not applicable to other OpenShift environments or non-Azure Kubernetes clusters.
- **No Backward Compatibility:** Existing clusters using service principals may require migration steps to adopt managed or workload identities.

---

### Integration with Related Azure Services

- **Azure Active Directory:** Central to both managed and workload identity mechanisms, providing identity federation and token issuance.
- **Azure RBAC:** Used to grant permissions to managed and workload identities for resource access.
- **Azure Key Vault, Storage, SQL, and More:** Common Azure services accessed securely by OpenShift workloads using these identities.

---

**Summary:**  
Azure Red Hat OpenShift now provides generally available support for managed identities and workload identities, enabling secure, credential-free authentication for clusters and workloads accessing Azure resources, thereby enhancing security and simplifying identity management for production environments.

---

### 4. Public preview: GitHub Copilot integration in Schema Designer for the MSSQL extension 

**Published**: March 18, 2026 18:15:04 UTC
**Link**: [Public preview: GitHub Copilot integration in Schema Designer for the MSSQL extension ](https://azure.microsoft.com/updates?id=558169)

**Update ID**: 558169
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now offers GitHub Copilot integration within its Schema Designer, available in public preview.

- Key changes or new features  
Developers can leverage GitHub Copilot’s AI-powered suggestions directly in the Schema Designer to streamline and enhance database schema creation and modification. This integration enables context-aware code completions, intelligent recommendations, and assistance with SQL syntax and schema design tasks. The feature aims to improve productivity and reduce manual errors by providing real-time guidance as users build or update database structures visually.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use Visual Studio Code and the MSSQL extension for SQL Server development and management. Teams working on database schema design, especially those seeking to accelerate workflows or adopt AI-driven development tools, will benefit most.

- Important notes  
The GitHub Copilot integration is currently in public preview, so feedback is encouraged to help refine the experience. Users should ensure they have the latest MSSQL extension and a valid Copilot subscription or access. As this is a preview feature, expect ongoing improvements and potential changes based on user input and evolving requirements.

**Details**:

**Azure Update Technical Report**

**Title:** Public preview: GitHub Copilot integration in Schema Designer for the MSSQL extension  
**Link:** [Azure Update Details](https://azure.microsoft.com/updates?id=558169)

---

### Background and Purpose of the Update

The MSSQL extension for Visual Studio Code is a widely used tool for database development and management, enabling developers to interact with Microsoft SQL Server and Azure SQL databases directly from their code editor. The integration of GitHub Copilot into the Schema Designer addresses the need for enhanced productivity and AI-assisted workflows in database schema design. This update is driven by developer feedback and the evolution of modern development practices, aiming to streamline the schema design process by leveraging artificial intelligence.

---

### Specific Features and Detailed Changes

- **GitHub Copilot Integration:** The Schema Designer within the MSSQL extension now supports GitHub Copilot, providing AI-powered assistance during the visual schema design process.
- **AI-Assisted Capabilities:** Developers can receive context-aware suggestions, code completions, and design recommendations directly within the schema designer interface, enhancing both the speed and accuracy of schema creation and modification.
- **Expanded Visual Experience:** The integration augments the traditional visual schema design workflow with intelligent prompts and guidance, making it easier to understand and implement complex database structures.

---

### Technical Mechanisms and Implementation Methods

- **Extension Enhancement:** The MSSQL extension for Visual Studio Code has been updated to embed GitHub Copilot’s AI engine within the Schema Designer component.
- **Contextual AI Assistance:** As users interact with the schema designer—such as creating tables, defining relationships, or modifying fields—Copilot analyzes the context and provides relevant suggestions or code snippets.
- **Seamless Workflow Integration:** The integration is designed to work natively within Visual Studio Code, requiring no additional configuration for users who have access to both the MSSQL extension and GitHub Copilot.

---

### Use Cases and Application Scenarios

- **Accelerated Schema Design:** Developers can rapidly prototype and iterate on database schemas with AI-generated suggestions, reducing manual effort and potential errors.
- **Learning and Onboarding:** New team members or less experienced database designers can leverage Copilot’s recommendations to understand best practices and common schema patterns.
- **Complex Schema Modifications:** When making intricate changes to existing database structures, Copilot can assist by suggesting appropriate modifications, constraints, or relationships.

---

### Important Considerations and Limitations

- **Public Preview Status:** This feature is currently in public preview, which means it may not be fully stable or feature-complete. Users should evaluate it in non-production environments before widespread adoption.
- **Copilot Subscription Required:** Access to GitHub Copilot features within the MSSQL extension may require an active Copilot subscription.
- **Data Privacy and Security:** As with all AI-powered tools, users should be aware of what data is sent to external services for processing and ensure compliance with organizational policies.

---

### Integration with Related Azure Services

- **Azure SQL Database:** The enhanced MSSQL extension can be used to design and manage schemas for Azure SQL Database instances, leveraging Copilot’s AI assistance for cloud-based database solutions.
- **Azure DevOps Workflows:** By integrating schema design with AI assistance directly in Visual Studio Code, teams can streamline their development and deployment pipelines for Azure-based data solutions.

---

**Summary:**  
The public preview of GitHub Copilot integration in the Schema Designer for the MSSQL extension in Visual Studio Code introduces AI-assisted capabilities to the visual schema design process, enhancing productivity and accuracy for database developers through context-aware suggestions and intelligent guidance.

---

### 5. Public Preview: Database DevOps in SSMS powered by SQL projects 

**Published**: March 18, 2026 18:15:04 UTC
**Link**: [Public Preview: Database DevOps in SSMS powered by SQL projects ](https://azure.microsoft.com/updates?id=558155)

**Update ID**: 558155
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Database DevOps capabilities are now available in SQL Server Management Studio (SSMS) through SQL projects, currently in Public Preview.

- Key changes or new features  
Developers can now use SQL projects directly within SSMS to manage database schema as code. This integration allows for source control of database schemas, reliable deployments to any environment, and the ability to incorporate code quality checks into the database development lifecycle. These features bring DevOps best practices to SQL database development, supporting versioning, automated testing, and CI/CD workflows.

- Target audience affected  
Database developers, DevOps engineers, and IT professionals who manage SQL Server or Azure SQL databases and use SSMS in their development workflows.

- Important notes if any  
This feature is in Public Preview, so it may not yet be suitable for production environments. Users should test thoroughly before adopting in critical workflows. Integration with source control and CI/CD pipelines can streamline collaboration and deployment processes. For more details and to get started, refer to the official [Azure Update announcement](https://azure.microsoft.com/updates?id=558155).

**Details**:

**Azure Update Report: Public Preview – Database DevOps in SSMS powered by SQL Projects**

**Background and Purpose of the Update:**  
This update introduces the public preview of Database DevOps capabilities within SQL Server Management Studio (SSMS), leveraging SQL database projects. The primary objective is to bring the advantages of schema-as-code to database development workflows. By enabling database schema management through source control, this update aims to enhance reliability, repeatability, and integration of quality checks in database development and deployment processes.

**Specific Features and Detailed Changes:**  
- **SQL Database Projects Integration:** SSMS now supports SQL database projects, allowing users to define and manage database schema as code within their familiar SSMS environment.
- **Source Control Support:** Database schemas can be versioned and managed using source control systems, facilitating collaborative development and change tracking.
- **Reliable Deployments:** The update provides mechanisms for consistent and reliable deployments of database schema to any environment, minimizing risks associated with manual changes.
- **Code Quality Checks:** Developers can integrate code quality checks directly into their workflow, ensuring that schema changes meet organizational standards before deployment.

**Technical Mechanisms and Implementation Methods:**  
- **Schema-as-Code Approach:** Database schema definitions are stored in SQL project files, which can be managed and edited within SSMS. These files are compatible with source control systems such as Git, enabling versioning and collaborative development.
- **Deployment Automation:** SQL projects support deployment scripts and tools that automate the process of applying schema changes to target environments, reducing manual intervention and errors.
- **Quality Integration:** Code quality checks can be incorporated into the development process, either through built-in SSMS features or external tools, ensuring that schema changes are validated before deployment.

**Use Cases and Application Scenarios:**  
- **Collaborative Database Development:** Teams can work together on database schema changes, track modifications, and resolve conflicts using source control.
- **Continuous Integration/Continuous Deployment (CI/CD):** SQL projects facilitate integration with CI/CD pipelines, enabling automated testing and deployment of database changes alongside application code.
- **Environment Consistency:** Organizations can ensure that development, testing, and production environments remain consistent by deploying schema changes from source-controlled projects.
- **Regulatory Compliance:** Source control and quality checks help maintain audit trails and enforce standards required for compliance.

**Important Considerations and Limitations:**  
- **Public Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should evaluate stability and compatibility before widespread adoption.
- **SSMS Dependency:** The functionality is currently available within SSMS, so users must use this tool to leverage the new features.
- **Integration Scope:** The update focuses on schema-as-code and may not cover other aspects of database DevOps, such as data migration or advanced deployment scenarios.

**Integration with Related Azure Services:**  
- **Azure SQL Database:** SQL projects can be deployed to Azure SQL Database, enabling cloud-based database DevOps workflows.
- **Azure DevOps:** Source control and CI/CD capabilities can be integrated with Azure DevOps pipelines, allowing automated build, test, and deployment processes for database projects.

**Summary Sentence:**  
This public preview enables database DevOps workflows in SSMS by integrating SQL projects, allowing IT professionals to manage database schema as code, leverage source control, automate deployments, and incorporate code quality checks for enhanced reliability and collaboration.

---

### 6. Public Preview: SQL MCP Server

**Published**: March 18, 2026 18:15:04 UTC
**Link**: [Public Preview: SQL MCP Server](https://azure.microsoft.com/updates?id=558150)

**Update ID**: 558150
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Public preview release of SQL MCP Server, a Model Context Protocol (MCP) connector for production databases, as part of Data API Builder (DAB).

- Key changes or new features  
  - SQL MCP Server enables secure, predictable integration of AI agents with your SQL databases.  
  - Provides a feature-rich connector that allows AI agents to interact with production data using the MCP standard.  
  - Simplifies the process of bringing AI-driven workflows to enterprise data scenarios.  
  - Designed to work seamlessly with Data API Builder, facilitating API-based data access.

- Target audience affected  
  - Developers building AI-powered applications that require secure access to SQL data.  
  - IT professionals managing data workflows and API integrations in enterprise environments.

- Important notes if any  
  - This is a public preview; not recommended for production workloads yet.  
  - The SQL MCP Server focuses on secure, role-based access, and predictable data interactions for AI agents.  
  - Integration with Data API Builder streamlines API management and AI agent connectivity.  
  - Feedback from early adopters is encouraged to improve future releases.

For more details, see the official [Azure Update](https://azure.microsoft.com/updates?id=558150).

**Details**:

**Azure Update Summary: Public Preview – SQL MCP Server**

**Background and Purpose of the Update**  
The SQL MCP Server is introduced as a new connector based on the Model Context Protocol (MCP) for production databases. This update aims to streamline the integration of AI agents into data workflows by providing a secure, predictable, and straightforward mechanism for connecting AI-driven processes to SQL databases. The feature is part of the Data API Builder (DAB) suite, reflecting Azure’s ongoing commitment to enhancing data accessibility and automation in enterprise environments.

**Specific Features and Detailed Changes**  
- **MCP Connector for SQL**: SQL MCP Server acts as a bridge between production SQL databases and AI agents, leveraging the MCP standard.
- **Feature-Rich Component**: As part of DAB, it offers a comprehensive set of features designed to facilitate secure and reliable data access.
- **Production-Ready Integration**: The connector is designed for use with production databases, emphasizing stability and security for mission-critical workloads.
- **AI Workflow Enablement**: The primary focus is to enable AI agents to interact with data workflows, supporting automation and advanced analytics scenarios.

**Technical Mechanisms and Implementation Methods**  
- **Model Context Protocol (MCP)**: MCP is a protocol that standardizes the way AI agents communicate with data sources. SQL MCP Server implements this protocol, ensuring consistent and predictable interactions.
- **Data API Builder (DAB) Integration**: The server is a component within DAB, leveraging its existing infrastructure for API management, security, and data access.
- **Security**: The connector is built with security as a core principle, supporting secure authentication and authorization mechanisms to protect production data.

**Use Cases and Application Scenarios**  
- **AI-Driven Data Automation**: Organizations can use SQL MCP Server to allow AI agents to automate data processing tasks, such as data extraction, transformation, and reporting.
- **Predictable Data Access for AI**: Enterprises can ensure that AI agents access data in a controlled and predictable manner, reducing risks associated with ad-hoc queries.
- **Integration with Existing Workflows**: The connector can be used to enhance existing data workflows by embedding AI capabilities without significant changes to the underlying database infrastructure.

**Important Considerations and Limitations**  
- **Public Preview**: The feature is currently in public preview, which means it may not be suitable for all production workloads and could be subject to changes.
- **Security and Compliance**: While designed for secure access, organizations should evaluate the connector’s security features in the context of their compliance requirements.
- **Dependency on DAB**: As a component of Data API Builder, the SQL MCP Server requires DAB to be deployed and configured appropriately.

**Integration with Related Azure Services**  
- **Data API Builder (DAB)**: The SQL MCP Server is tightly integrated with DAB, leveraging its capabilities for API management and data access.
- **AI and Machine Learning Services**: The connector is designed to facilitate integration with AI agents, which may be part of Azure’s AI and machine learning ecosystem.
- **Azure SQL and Other Production Databases**: The server is intended for use with production-grade SQL databases, ensuring compatibility with Azure SQL and similar services.

**Summary Sentence**  
SQL MCP Server, now in public preview, is a secure and feature-rich MCP connector within Data API Builder that enables seamless integration of AI agents into production SQL database workflows, supporting predictable, automated, and secure data access for advanced analytics and automation scenarios.

---

### 7. Generally Available: GitHub Copilot in SQL Server Management Studio 22 

**Published**: March 18, 2026 18:15:04 UTC
**Link**: [Generally Available: GitHub Copilot in SQL Server Management Studio 22 ](https://azure.microsoft.com/updates?id=558134)

**Update ID**: 558134
**Data source**: Azure Updates API

**Categories**: Launched, Features

**Summary**:

- What was updated  
GitHub Copilot is now generally available in SQL Server Management Studio (SSMS) 22.

- Key changes or new features  
The integration of GitHub Copilot brings AI-powered code assistance directly into SSMS. Developers and database professionals can use natural language to generate, explain, and fix SQL code within the SSMS environment. Copilot can help automate repetitive tasks, suggest code snippets, and provide explanations for complex queries, improving productivity and code quality.

- Target audience affected  
This update is relevant for developers, database administrators, and IT professionals who use SSMS 22 for SQL Server management and development.

- Important notes if any  
To access GitHub Copilot features in SSMS 22, users need a valid Copilot subscription. The AI assistance is designed to streamline SQL development and troubleshooting, but users should review generated code for accuracy and compliance with organizational standards. This update enhances SSMS usability, making it easier to leverage AI for database tasks directly within the familiar SQL Server tooling.

**Details**:

**Azure Update Technical Explanation: Generally Available: GitHub Copilot in SQL Server Management Studio 22**

**Background and Purpose of the Update**  
This update announces the general availability of GitHub Copilot within SQL Server Management Studio (SSMS) 22. The primary purpose is to integrate AI-powered coding assistance directly into the SSMS environment, which is widely used by database administrators and developers for managing SQL Server instances. By embedding GitHub Copilot, Microsoft aims to streamline and enhance the productivity of users working with SQL through natural language interactions.

**Specific Features and Detailed Changes**  
With this release, GitHub Copilot is natively accessible within SSMS 22. Key features include:
- **Natural Language Querying:** Users can write prompts in natural language, and Copilot will generate corresponding T-SQL code.
- **Code Explanation:** Copilot can explain existing SQL code, aiding in understanding complex queries or unfamiliar scripts.
- **Code Fixing:** The AI assistant can suggest fixes for SQL code, helping to identify and resolve errors or inefficiencies.
- **Integrated Workflow:** All Copilot features are available directly within the SSMS interface, eliminating the need to switch between tools.

This integration represents a significant enhancement over previous versions of SSMS, which did not include AI-assisted development features.

**Technical Mechanisms and Implementation Methods**  
GitHub Copilot is powered by advanced AI models that process natural language input and generate code suggestions. In SSMS 22, Copilot is implemented as an extension or built-in feature, seamlessly connecting to the Copilot service. When a user enters a prompt or requests an explanation, SSMS sends this data to the Copilot backend, which returns the generated SQL code or explanation. The integration ensures that the user experience remains consistent with other Copilot-enabled environments, such as Visual Studio Code.

**Use Cases and Application Scenarios**  
- **Query Generation:** Accelerate the creation of complex T-SQL queries by describing requirements in plain English.
- **Code Review and Onboarding:** Quickly understand legacy SQL code or scripts written by others through AI-generated explanations.
- **Error Resolution:** Identify and fix issues in SQL scripts with Copilot’s suggestions, reducing debugging time.
- **Learning and Training:** New users can learn SQL syntax and best practices interactively by leveraging Copilot’s code generation and explanation features.

**Important Considerations and Limitations**  
- **Data Privacy:** Prompts and code may be sent to external Copilot services for processing. Users should avoid submitting sensitive or confidential information.
- **Accuracy:** While Copilot provides helpful suggestions, all generated code should be reviewed for correctness, security, and compliance with organizational standards.
- **Licensing:** Access to GitHub Copilot may require a valid subscription or license, which is managed separately from SSMS.
- **Feature Scope:** The update does not specify support for advanced SQL Server features (e.g., CLR integration, advanced security), so users should validate Copilot’s effectiveness for specialized scenarios.

**Integration with Related Azure Services**  
Although the update does not detail direct integration with Azure services, SSMS is commonly used to manage Azure SQL Database and other Azure data services. The availability of Copilot in SSMS 22 can enhance productivity when working with Azure-hosted databases, supporting tasks such as query development, troubleshooting, and code review in hybrid or cloud-first environments.

**Summary Sentence**  
GitHub Copilot is now generally available in SQL Server Management Studio 22, providing AI-powered natural language assistance for SQL code development, explanation, and fixing directly within the SSMS interface.

---

### 8. Generally Available: Lakeflow Connect Free Tier now available in Azure Databricks  

**Published**: March 18, 2026 17:00:05 UTC
**Link**: [Generally Available: Lakeflow Connect Free Tier now available in Azure Databricks  ](https://azure.microsoft.com/updates?id=558810)

**Update ID**: 558810
**Data source**: Azure Updates API

**Categories**: Launched, AI + machine learning, Analytics, Azure Databricks, Features

**Summary**:

- What was updated  
Azure Databricks has introduced the Lakeflow Connect Free Tier, which is now generally available.

- Key changes or new features  
The Free Tier provides each Databricks workspace with 100 free Databricks Units (DBUs) per day specifically for ingesting data from SaaS applications and databases. This enables ingestion of approximately 100 million records per workspace per day without incurring additional costs. The feature is designed to simplify and accelerate data integration workflows using Lakeflow Connect.

- Target audience affected  
Developers and IT professionals working with Azure Databricks, particularly those responsible for data ingestion, integration, and ETL processes from external SaaS sources and databases.

- Important notes if any  
The free DBUs are allocated per workspace per day and are only applicable to Lakeflow Connect ingestion workloads. This update allows teams to prototype, test, and run production ingestion jobs at no cost up to the daily limit, making it easier to evaluate and scale data integration solutions. For larger workloads, usage beyond the free tier will incur standard charges.  
Link: [Azure Update](https://azure.microsoft.com/updates?id=558810)

**Details**:

**Azure Update Report: Generally Available – Lakeflow Connect Free Tier now available in Azure Databricks**

**Background and Purpose of the Update:**  
This update introduces the general availability of the Lakeflow Connect Free Tier within Azure Databricks. The primary objective is to lower the entry barrier for organizations and developers seeking to ingest data from SaaS applications and databases into Databricks Lakehouse. By providing a free allocation of Data Bricks Units (DBUs) for ingestion, Microsoft aims to facilitate easier onboarding, experimentation, and proof-of-concept development without immediate cost concerns.

**Specific Features and Detailed Changes:**  
- **Lakeflow Connect Free Tier:** Each Azure Databricks workspace now receives 100 free DBUs per day, specifically allocated for data ingestion tasks from SaaS sources and databases.
- **Data Ingestion Capacity:** The free tier supports the ingestion of approximately 100 million records per workspace per day, enabling substantial data movement for evaluation and development purposes.
- **Workspace Scope:** The allocation is per workspace, ensuring that multiple teams or projects can benefit independently within the same Azure subscription.

**Technical Mechanisms and Implementation Methods:**  
- **DBU Allocation:** The free DBUs are automatically provisioned to each workspace daily. These units are consumed exclusively for Lakeflow Connect ingestion activities.
- **Ingestion Pipeline:** Users can configure data pipelines to connect to supported SaaS applications and databases. The ingestion process leverages Databricks’ scalable compute infrastructure, utilizing the allocated DBUs to execute data extraction, transformation, and loading (ETL) operations.
- **Monitoring and Management:** Usage of the free DBUs can be tracked via the Azure Databricks workspace, allowing administrators to monitor consumption and plan for scale-up if needed.

**Use Cases and Application Scenarios:**  
- **Proof-of-Concept Development:** Teams can experiment with data ingestion from various SaaS and database sources without incurring costs, accelerating innovation and prototyping.
- **Data Integration Testing:** Developers can validate and test ETL workflows and data integration strategies in a real-world environment before committing to larger-scale deployments.
- **Small-Scale Production Loads:** For organizations with modest data ingestion needs, the free tier may suffice for ongoing operational requirements.

**Important Considerations and Limitations:**  
- **Daily DBU Limit:** The free tier is capped at 100 DBUs per workspace per day. Ingesting data beyond this limit will require additional, billable DBUs.
- **Ingestion-Only Scope:** The free DBUs are designated solely for Lakeflow Connect ingestion tasks and cannot be used for other Databricks workloads.
- **Workspace Isolation:** The allocation is not cumulative across workspaces; each workspace operates independently within its daily limit.

**Integration with Related Azure Services:**  
- **Azure Databricks Lakehouse:** Ingested data is seamlessly integrated into the Databricks Lakehouse platform, supporting advanced analytics, machine learning, and BI workloads.
- **Azure Data Services:** The ingested data can be further processed or shared with other Azure services such as Azure Data Factory, Azure Synapse Analytics, and Power BI for downstream analytics and reporting.

**Summary:**  
The Lakeflow Connect Free Tier in Azure Databricks provides each workspace with 100 free DBUs per day for ingesting data from SaaS applications and databases, supporting up to 100 million records daily and enabling cost-effective data integration, testing, and prototyping.

---

### 9. Generally Available: Versionless key support for transparent data encryption in Azure SQL Database 

**Published**: March 18, 2026 17:00:05 UTC
**Link**: [Generally Available: Versionless key support for transparent data encryption in Azure SQL Database ](https://azure.microsoft.com/updates?id=558183)

**Update ID**: 558183
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
Azure SQL Database now supports versionless keys for Transparent Data Encryption (TDE).

- Key changes or new features  
With this update, you can configure TDE to use encryption keys from Azure Key Vault or Managed HSM without specifying a particular key version. This simplifies key management, as applications and databases will automatically use the latest key version available. It reduces operational overhead and the risk of referencing outdated keys, streamlining key rotation and compliance processes.

- Target audience affected  
Developers and IT professionals responsible for database security, compliance, and key management in Azure SQL Database environments.

- Important notes if any  
Existing TDE configurations referencing specific key versions can be updated to use versionless keys for easier management. This feature enhances security and reliability by ensuring databases always use the latest key version. No application changes are required to benefit from versionless key support, but review your key management policies to take full advantage of this update.

[Read the official update](https://azure.microsoft.com/updates?id=558183)

**Details**:

**Comprehensive Technical Explanation: Generally Available: Versionless key support for transparent data encryption in Azure SQL Database**

**Background and Purpose of the Update**  
Transparent Data Encryption (TDE) is a critical security feature in Azure SQL Database, enabling encryption of data at rest. Traditionally, when using customer-managed keys (CMK) for TDE, users were required to reference a specific key version stored in Azure Key Vault or Managed HSM. This version-specific referencing introduced operational overhead, especially during key rotation or lifecycle management. The purpose of this update is to simplify and enhance the reliability of encryption key management by introducing support for versionless keys in TDE.

**Specific Features and Detailed Changes**  
With this update, Azure SQL Database now allows users to configure TDE using versionless keys. Instead of specifying a particular version of a key in Azure Key Vault or Managed HSM, users can reference the key by its name or URI without including the version identifier. This means that when a key is rotated (i.e., a new version is created), Azure SQL Database will automatically use the latest version of the key without requiring manual updates to the TDE configuration.

**Technical Mechanisms and Implementation Methods**  
The versionless key support is implemented by allowing the TDE protector configuration in Azure SQL Database to accept a key URI that omits the version segment. When the database engine requires access to the encryption key, it queries Azure Key Vault or Managed HSM for the latest enabled version of the specified key. This mechanism ensures seamless key rotation and reduces the risk of misconfiguration or service disruption during key updates. The integration leverages Azure’s native identity and access management to securely access the keys.

**Use Cases and Application Scenarios**  
- **Key Rotation:** Enterprises with strict compliance requirements can rotate keys regularly without service interruption or the need to update TDE settings for each database.
- **Centralized Key Management:** Organizations managing multiple databases can streamline their encryption key lifecycle by referencing keys versionlessly, reducing administrative complexity.
- **Disaster Recovery and Automation:** Automated deployment scripts and templates no longer need to track or update key versions, improving reliability and reducing operational errors.

**Important Considerations and Limitations**  
- **Backward Compatibility:** Existing databases configured with version-specific keys will continue to function, but administrators are encouraged to transition to versionless keys for simplified management.
- **Access Control:** Proper permissions must be maintained in Azure Key Vault or Managed HSM to ensure the SQL Database can access the latest key version.
- **Key Deletion or Disabling:** If the latest key version is deleted or disabled, database access may be impacted. Key lifecycle policies should be carefully managed.

**Integration with Related Azure Services**  
- **Azure Key Vault and Managed HSM:** Versionless key support is directly integrated with these services, leveraging their capabilities for secure key storage and access control.
- **Azure Identity Management:** Managed identities can be used to grant the necessary permissions for SQL Database to access keys without embedding credentials.
- **Azure Policy and Compliance:** This feature supports compliance initiatives by making key rotation and management more straightforward and auditable.

**Summary Sentence**  
Azure SQL Database now supports versionless keys for transparent data encryption, enabling simpler and more reliable customer-managed key management by automatically using the latest key version from Azure Key Vault or Managed HSM without requiring manual updates to TDE configurations.

---

### 10. Public Preview: Data API builder with built-in GitHub Copilot in MSSQL extension 

**Published**: March 18, 2026 17:00:05 UTC
**Link**: [Public Preview: Data API builder with built-in GitHub Copilot in MSSQL extension ](https://azure.microsoft.com/updates?id=558178)

**Update ID**: 558178
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Features

**Summary**:

- What was updated  
The MSSQL extension for Visual Studio Code now offers Data API builder in public preview, featuring integrated GitHub Copilot support.

- Key changes or new features  
Developers can now use Data API builder directly within the MSSQL extension to generate REST and GraphQL APIs from SQL data sources. The built-in GitHub Copilot integration provides AI-powered guidance and code suggestions, streamlining backend API creation. This enables a more efficient, guided workflow for building APIs without leaving the VS Code environment.

- Target audience affected  
This update is relevant to developers and IT professionals working with Microsoft SQL Server in Visual Studio Code, especially those building backend services or APIs.

- Important notes  
The feature is currently in public preview, so it may not be fully stable for production use. Users should test and provide feedback. The integration with GitHub Copilot enhances productivity by offering contextual code suggestions and guidance during API generation. REST and GraphQL endpoints can be quickly scaffolded, accelerating development cycles. For more details and to participate in the preview, visit the official Azure update page: https://azure.microsoft.com/updates?id=558178

**Details**:

**Azure Update Technical Explanation**

**Title:** Public Preview: Data API builder with built-in GitHub Copilot in MSSQL extension

**Background and Purpose of the Update:**  
This update introduces the Data API builder into the MSSQL extension for Visual Studio Code, now available in public preview. The primary goal is to streamline and enhance the backend development experience for SQL Server developers by integrating guided API generation capabilities directly into the familiar Visual Studio Code environment. By embedding GitHub Copilot, developers benefit from AI-assisted code suggestions, which can accelerate backend development and reduce manual coding errors.

**Specific Features and Detailed Changes:**  
- **Data API builder Integration:** The MSSQL extension now includes Data API builder functionality, enabling developers to generate REST and GraphQL endpoints directly from their SQL Server databases within Visual Studio Code.
- **Built-in GitHub Copilot:** The extension leverages GitHub Copilot to provide AI-powered code completions and recommendations during the API generation process, offering contextual guidance and reducing the learning curve for backend API creation.
- **Guided Backend Generation:** The workflow is designed to be interactive and user-friendly, guiding developers through the process of exposing database objects (such as tables and views) as REST or GraphQL APIs without the need for extensive manual configuration or boilerplate code.

**Technical Mechanisms and Implementation Methods:**  
- The Data API builder operates within the MSSQL extension, utilizing the underlying database schema to scaffold API endpoints.
- GitHub Copilot is integrated into the extension, providing real-time code suggestions and best practices as developers define their APIs.
- The extension supports both REST and GraphQL API generation, allowing developers to select the preferred protocol based on their application requirements.
- All operations are performed within Visual Studio Code, leveraging its extensibility and integration capabilities.

**Use Cases and Application Scenarios:**  
- **Rapid API Prototyping:** Developers can quickly expose SQL Server data as REST or GraphQL APIs for frontend or mobile applications, accelerating prototyping and development cycles.
- **Internal Tools and Dashboards:** Teams building internal tools can use the extension to generate secure, standardized APIs for data access without extensive backend development.
- **Learning and Onboarding:** New team members or less experienced developers can leverage the guided experience and Copilot assistance to learn best practices for API development with SQL Server.

**Important Considerations and Limitations:**  
- This feature is currently in public preview, which may imply limited support and potential changes before general availability.
- The update is specific to the MSSQL extension in Visual Studio Code and may not be available in other environments or editors.
- Developers should review the security and access controls of the generated APIs, especially when exposing sensitive data.

**Integration with Related Azure Services:**  
- The Data API builder is designed to work with SQL Server databases, which can include Azure SQL Database and Azure SQL Managed Instance as backend data sources.
- Generated APIs can be integrated with other Azure services such as Azure App Service, Azure Functions, or Azure API Management for deployment, scaling, and security.
- The workflow aligns with Azure’s broader ecosystem for cloud-native application development and DevOps practices.

**Summary Sentence:**  
The public preview of Data API builder with built-in GitHub Copilot in the MSSQL extension for Visual Studio Code introduces a guided, AI-assisted experience for generating REST and GraphQL APIs from SQL Server databases, streamlining backend development workflows and enhancing productivity for developers.

---


*This report was automatically generated - 2026-03-19 03:06:22 UTC*