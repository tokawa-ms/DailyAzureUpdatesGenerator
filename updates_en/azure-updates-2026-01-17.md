# January 17, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: January 17, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: User delegation SAS for Azure Tables, Azure Files, and Azure Queues

**Published**: January 16, 2026 17:00:49 UTC
**Link**: [Public Preview: User delegation SAS for Azure Tables, Azure Files, and Azure Queues](https://azure.microsoft.com/updates?id=548987)

**Update ID**: 548987
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Databases, Azure Files, Queue Storage, Table Storage

**Summary**:

- What was updated  
Azure has introduced public preview support for User Delegation Shared Access Signatures (SAS) on Azure Tables, Azure Files, and Azure Queues. Previously, User Delegation SAS was generally available only for Azure Blob storage.

- Key changes or new features  
This update extends the security model of User Delegation SAS—where SAS tokens are secured via Azure Active Directory credentials—to additional storage services beyond blobs. Developers and IT professionals can now generate SAS tokens for tables, files, and queues using Azure AD credentials, enhancing security by eliminating the need to use storage account keys directly. This aligns with best practices for least privilege and centralized identity management.

- Target audience affected  
Developers building applications that interact with Azure Tables, Files, and Queues, as well as IT professionals managing secure access to Azure Storage resources, will benefit from this update. It is particularly relevant for teams aiming to improve security posture by leveraging Azure AD authentication for SAS token generation.

- Important notes if any  
This feature is currently in public preview and should be used with caution in production environments. Users should monitor the official documentation and Azure updates for GA announcements and any changes in feature behavior or limitations. Existing User Delegation SAS for blobs remains generally available and unchanged.

**Details**:

The recent Azure update announces the public preview availability of User Delegation Shared Access Signatures (SAS) for Azure Tables, Azure Files, and Azure Queues, extending the existing User Delegation SAS support previously limited to Azure Blob storage. This enhancement enables more secure, flexible, and manageable delegated access to these additional storage services by leveraging Azure Active Directory (Azure AD) credentials.

**Background and Purpose**  
Shared Access Signatures (SAS) provide delegated, time-bound, and permission-scoped access to Azure Storage resources without exposing the account key. Traditionally, SAS tokens were either account SAS or service SAS, both relying on storage account keys, which pose security risks if keys are compromised. User Delegation SAS (UDSAS) improves security by using Azure AD credentials to generate SAS tokens, thereby enabling fine-grained access control aligned with organizational identity and access management policies. Until now, UDSAS was only available for Blob storage. This update addresses the need for consistent, secure delegated access across other storage services—Tables, Files, and Queues—facilitating unified security models and improved compliance.

**Specific Features and Detailed Changes**  
- **User Delegation SAS Support Extended:** UDSAS can now be generated for Azure Tables, Azure Files, and Azure Queues, in addition to Blobs.  
- **Azure AD Integration:** SAS tokens are created based on Azure AD user or service principal credentials, eliminating the need to share or manage storage account keys.  
- **Granular Permissions:** Permissions such as read, write, delete, and list can be scoped per service and resource, consistent with each service’s capabilities.  
- **Time-bound Access:** Tokens include start and expiry times, allowing temporary access aligned with security policies.  
- **Public Preview Status:** This feature is currently in public preview, allowing customers to test and provide feedback before general availability.

**Technical Mechanisms and Implementation Methods**  
User Delegation SAS relies on Azure AD OAuth 2.0 tokens to authenticate the user or service principal requesting the SAS. The process involves:  
1. **Authentication:** The client authenticates to Azure AD and obtains an OAuth 2.0 access token with appropriate permissions to the storage account.  
2. **User Delegation Key Request:** Using the access token, the client requests a user delegation key from the Azure Storage service. This key is scoped to the authenticated identity and has a validity period.  
3. **SAS Token Generation:** The client uses the user delegation key to cryptographically sign the SAS token, specifying permissions, resource types, and expiry.  
4. **Resource Access:** The SAS token is then used by clients or applications to access the specified storage resources without needing the account key.  

This mechanism leverages Azure AD’s centralized identity management and conditional access policies, enhancing security and auditability.

**Use Cases and Application Scenarios**  
- **Secure Delegated Access:** Applications requiring temporary, scoped access to Tables, Files, or Queues can now use UDSAS, reducing key exposure risk.  
- **Enterprise Identity Integration:** Organizations using Azure AD for identity management can enforce access policies consistently across all storage services.  
- **Multi-tenant SaaS Applications:** SaaS providers can issue SAS tokens tied to tenant identities without sharing account keys.  
- **Compliance and Auditing:** Access via Azure AD identities enables better logging and compliance tracking.  
- **Automation and DevOps:** Scripts and automation tools can generate SAS tokens securely using service principals with least privilege.  

**Important Considerations and Limitations**  
- **Public Preview:** As a preview feature, it may have limited SLA and could undergo changes before GA. Testing in non-production environments is recommended.  
- **Azure AD Dependency:** Requires Azure AD authentication; legacy authentication methods or anonymous access are not supported.  
- **Permission Scope:** The permissions model aligns with each service’s capabilities but may differ from Blob storage; users should review service-specific permission sets

---


*This report was automatically generated - 2026-01-17 03:01:20 UTC*