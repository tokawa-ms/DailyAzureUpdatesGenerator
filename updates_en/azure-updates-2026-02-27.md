# February 27, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: February 27, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Public Preview: Restrict usage of user delegation SAS to an Entra ID identity 

**Published**: February 26, 2026 19:45:06 UTC
**Link**: [Public Preview: Restrict usage of user delegation SAS to an Entra ID identity ](https://azure.microsoft.com/updates?id=557694)

**Update ID**: 557694
**Data source**: Azure Updates API

**Categories**: In preview, Storage, Azure Blob Storage, Features, Security

**Summary**:

- What was updated  
Azure Storage now supports restricting user delegation Shared Access Signatures (SAS) to specific Entra ID (formerly Azure AD) identities. This feature is available in public preview.

- Key changes or new features  
  - User delegation SAS tokens can now be bound to a particular Entra ID user or service principal.
  - Access using the SAS token is only permitted if the request is made by the same Entra ID identity that generated the SAS.
  - This enhancement provides stronger security by preventing token misuse if the SAS is leaked or intercepted.

- Target audience affected  
  - Developers integrating Azure Storage with applications that use SAS for delegated access.
  - IT professionals and security administrators managing storage access policies and compliance.

- Important notes if any  
  - This feature is currently in public preview and may not be recommended for production workloads.
  - Existing user delegation SAS tokens without identity binding will continue to work as before.
  - Adoption of this feature can help meet stricter security and compliance requirements by ensuring SAS tokens are only usable by intended Entra ID identities.

For more details, see the official update: https://azure.microsoft.com/updates?id=557694

**Details**:

**Azure Update Technical Report**

**Title:** Public Preview: Restrict usage of user delegation SAS to an Entra ID identity  
**Link:** [Azure Update](https://azure.microsoft.com/updates?id=557694)

---

**Background and Purpose of the Update**

Azure Storage has traditionally offered Shared Access Signatures (SAS) as a flexible mechanism for granting limited access to storage resources. User delegation SAS, introduced previously, leverages Azure Entra ID (formerly Azure Active Directory) to provide enhanced security by tying SAS tokens to user identities. However, prior to this update, user delegation SAS tokens could be used by any entity possessing the token, regardless of the original Entra ID identity. The purpose of this update is to further strengthen authentication by restricting the usage of user delegation SAS tokens strictly to the Entra ID identity that was used to generate them, thereby reducing the risk of token misuse and unauthorized access.

---

**Specific Features and Detailed Changes**

- **User-Bound User Delegation SAS:** The update introduces a new capability where user delegation SAS tokens are bound to a specific Entra ID identity. Only the identity that generated the SAS token can use it to access Azure Storage resources.
- **Public Preview Availability:** This feature is currently available in public preview, allowing IT professionals and developers to test and validate its functionality in their environments.
- **Enhanced Authentication:** Combines the flexibility of SAS with the security of Entra ID, ensuring that SAS tokens cannot be used by unintended users or services.

---

**Technical Mechanisms and Implementation Methods**

- **Token Binding:** When a user delegation SAS is created, it is cryptographically linked to the Entra ID identity. Azure Storage validates the identity of the caller at the time of access, ensuring it matches the identity associated with the SAS token.
- **Integration with Entra ID Authentication:** Access attempts using the SAS token require authentication against Entra ID. If the identity does not match, access is denied.
- **Backward Compatibility:** Existing user delegation SAS tokens (not bound to identity) continue to function as before, unless explicitly configured to use the new user-bound feature.

---

**Use Cases and Application Scenarios**

- **Secure Data Sharing:** Organizations can securely share Azure Storage resources with internal users, ensuring that only the intended Entra ID identity can access the data, even if the SAS token is leaked or intercepted.
- **Compliance and Auditing:** Meets compliance requirements for user-specific access control, enabling detailed auditing of storage access by individual users.
- **Application Integration:** Applications that generate SAS tokens for users can now enforce user-specific access, reducing the risk of privilege escalation or lateral movement.

---

**Important Considerations and Limitations**

- **Preview Status:** As this feature is in public preview, it may not be suitable for production workloads. Users should monitor for changes and updates before full deployment.
- **Identity Requirement:** The feature requires the use of Entra ID for authentication. Non-Entra ID identities or anonymous access are not supported.
- **Token Management:** Applications and scripts must be updated to handle user-bound SAS tokens and ensure proper identity authentication.

---

**Integration with Related Azure Services**

- **Azure Storage:** The feature is directly integrated into Azure Storage, enhancing its security model.
- **Azure Entra ID:** Relies on Entra ID for authentication and identity binding.
- **Azure RBAC:** Complements existing role-based access control by providing granular, user-specific access via SAS.

---

**Summary Sentence**

This Azure Storage update in public preview introduces user-bound user delegation SAS, enabling secure, Entra ID-specific access to storage resources and strengthening authentication by ensuring SAS tokens can only be used by the identity that generated them.

---


*This report was automatically generated - 2026-02-27 03:01:46 UTC*