# October 31, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 31, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL 

**Published**: October 30, 2026 17:16:27 UTC
**Link**: [Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL ](https://azure.microsoft.com/updates?id=577491)

**Update ID**: 577491
**Data source**: Azure Updates API

**Categories**: In preview, Databases, Hybrid + multicloud, Azure SQL Database, Feature

**Summary**:

**What was updated:**  
Azure SQL Database now supports database-level managed identities (including Federated Identity Credential, FIC) in the CREATE DATABASE SCOPED CREDENTIAL T-SQL statement, available in Public Preview.

**Key changes or new features:**  
- You can assign a user-managed identity at the database level, not just at the server level.
- This identity can be used to access external data sources like Azure Blob Storage and Azure Data Lake Storage Gen2 via external tables and the OPENROWSET function.
- Authentication for external data queries can now be handled per database, allowing more granular security and isolation.
- Support for Federated Identity Credential (FIC) enables integration with external identity providers, expanding authentication scenarios.

**Target audience affected:**  
- Developers working with Azure SQL Database who need secure, granular access to external data sources.
- IT professionals managing database security and identity configurations in multi-tenant or complex environments.

**Important notes:**  
- This feature is currently in Public Preview; not recommended for production workloads yet.
- Enables improved security and flexibility for multi-database or multi-tenant architectures.
- Review documentation for limitations and setup requirements during the preview phase.

[Azure Update Link](https://azure.microsoft.com/updates?id=577491)

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Support database-level managed identity (including FIC) in Create Database Scoped Credential T-SQL  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=577491)

---

**Background and Purpose of the Update**  
Azure SQL Database previously supported managed identities primarily at the server level, limiting granular control over authentication when accessing external resources such as Azure Blob Storage and Azure Data Lake Storage Gen2. The purpose of this update is to introduce database-level managed identity support, enabling each database to use a distinct user-assigned managed identity. This enhancement provides improved security isolation, flexibility, and compliance, particularly for multi-tenant environments or scenarios requiring fine-grained access control.

---

**Specific Features and Detailed Changes**  
- **Database-Level Managed Identity:** Users can now assign a user-managed identity specifically to an individual Azure SQL Database, rather than being restricted to server-level managed identities.
- **Create Database Scoped Credential T-SQL Enhancement:** The T-SQL statement `CREATE DATABASE SCOPED CREDENTIAL` now supports specifying a user-assigned managed identity at the database level, including support for Federated Identity Credential (FIC).
- **External Data Access:** Databases can authenticate using their assigned managed identity to access files in Azure Blob Storage and Azure Data Lake Storage Gen2 through external tables and the `OPENROWSET` function.

---

**Technical Mechanisms and Implementation Methods**  
- **Managed Identity Assignment:** A user-assigned managed identity is created in Azure Active Directory and linked to the specific Azure SQL Database.
- **Credential Creation:** Using the enhanced `CREATE DATABASE SCOPED CREDENTIAL` T-SQL, administrators specify the managed identity to be used for authenticating external data access.
- **Authentication Flow:** When querying external storage (e.g., via `OPENROWSET`), the database uses its scoped managed identity to obtain tokens from Azure AD, which are then used to securely access the storage resources.
- **Federated Identity Credential (FIC):** FIC support allows for advanced scenarios where federated authentication is required, further extending the flexibility of managed identity usage.

---

**Use Cases and Application Scenarios**  
- **Multi-Tenant Applications:** Each tenant’s database can have its own managed identity, ensuring strict isolation and compliance.
- **Data Integration Workloads:** ETL processes or data pipelines that require secure, granular access to external storage from individual databases.
- **Compliance-Driven Environments:** Organizations needing to enforce least privilege and separation of duties at the database level.
- **Federated Authentication Scenarios:** Workloads requiring federated identity support for external data access.

---

**Important Considerations and Limitations**  
- **Public Preview:** This feature is currently in public preview; production use should be approached with caution and awareness of potential changes.
- **Scope of Identity:** Managed identities are scoped at the database level, but proper configuration and assignment in Azure AD are required.
- **Supported Storage Types:** The feature is specifically for Azure Blob Storage and Azure Data Lake Storage Gen2.
- **T-SQL Syntax:** Only the `CREATE DATABASE SCOPED CREDENTIAL` statement is enhanced; other credential management methods are not affected.

---

**Integration with Related Azure Services**  
- **Azure Active Directory:** Managed identities are provisioned and managed via Azure AD.
- **Azure Blob Storage & Data Lake Storage Gen2:** Databases authenticate to these services using their scoped managed identity.
- **Azure SQL Database:** The update applies directly to Azure SQL Database, enhancing its integration capabilities with external storage.

---

**Summary Sentence**  
This update enables Azure SQL Database to use database-level user-assigned managed identities, including Federated Identity Credential support, for secure and granular authentication to Azure Blob Storage and Azure Data Lake Storage Gen2 via enhanced T-SQL credential creation.

---


*This report was automatically generated - 2026-10-31 03:01:08 UTC*