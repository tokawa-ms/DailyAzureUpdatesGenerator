# October 22, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 22, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 2 items

## Update List

### 1. Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra

**Published**: October 21, 2026 17:38:32 UTC
**Link**: [Announcing: Choose Your Own Telephony (CYOT) for Microsoft Entra](https://azure.microsoft.com/updates?id=577273)

**Update ID**: 577273
**Data source**: Azure Updates API

**Categories**: Identity, Microsoft Entra ID (formerly Azure AD), Announcement

**Summary**:

- What was updated  
Microsoft announced the upcoming "Choose Your Own Telephony (CYOT)" feature for Microsoft Entra ID, allowing organizations to select third-party telephony providers for SMS and voice authentication.

- Key changes or new features  
Starting October 30, 2026, organizations can configure Microsoft Entra ID to use supported third-party telecommunications providers for delivering SMS and voice-based multi-factor authentication (MFA) messages. This expands beyond the default Microsoft-managed telephony service, offering flexibility in provider selection and potentially addressing regional or compliance requirements.

- Target audience affected  
This update is relevant for IT professionals, identity and access administrators, and developers managing authentication and security for organizations using Microsoft Entra ID (formerly Azure Active Directory).

- Important notes if any  
Organizations should evaluate their authentication workflows and begin planning for possible integration with third-party telephony providers ahead of the October 2026 availability. This feature may help address cost, reliability, or regulatory needs related to telephony-based authentication. Detailed guidance on supported providers and integration steps will be provided closer to the release date.

**Details**:

**Azure Update Report: Choose Your Own Telephony (CYOT) for Microsoft Entra**

**Background and Purpose of the Update**  
Microsoft Entra ID is introducing the "Choose Your Own Telephony Provider" (CYOT) feature, effective October 30, 2026. The primary purpose of this update is to allow organizations greater flexibility and control over their authentication workflows by enabling the use of supported third-party telecommunications providers for SMS and voice authentication. This change addresses the need for customizable telephony solutions, especially for enterprises with specific compliance, cost, or regional requirements.

**Specific Features and Detailed Changes**  
The CYOT feature will allow organizations to select from a list of supported third-party telephony providers for delivering SMS and voice-based authentication messages. Previously, Microsoft Entra ID relied on Microsoft-managed telephony services for these communications. With CYOT, administrators can configure their Entra ID tenant to route authentication messages through their chosen provider, provided it is supported by Microsoft.

Key changes include:
- Configuration options within Microsoft Entra ID to select and integrate a third-party telephony provider.
- Support for both SMS and voice authentication methods.
- Enhanced flexibility for organizations to meet unique operational or regulatory needs.

**Technical Mechanisms and Implementation Methods**  
The implementation of CYOT involves integration points within Microsoft Entra ID’s authentication workflows. Administrators will be able to configure their tenant to use a supported provider via the Azure portal or relevant APIs. The technical mechanism likely includes:
- Secure API endpoints for message delivery between Entra ID and the third-party provider.
- Authentication and authorization controls to ensure only approved providers are used.
- Logging and monitoring capabilities for message delivery status and troubleshooting.

Organizations must ensure their chosen provider is supported by Microsoft, and follow the prescribed integration steps to enable CYOT within their Entra ID environment.

**Use Cases and Application Scenarios**  
CYOT is particularly beneficial in scenarios such as:
- Organizations operating in regions where Microsoft’s telephony services may not be optimal or available.
- Enterprises with existing contracts or relationships with local telephony providers.
- Businesses with strict compliance requirements mandating the use of specific telecommunications providers.
- Companies seeking cost optimization by leveraging preferred telephony vendors.

Typical application scenarios include multi-factor authentication (MFA) workflows, password reset processes, and other identity verification steps requiring SMS or voice communication.

**Important Considerations and Limitations**  
- Only supported third-party providers can be used; organizations must verify provider compatibility.
- The feature becomes available starting October 30, 2026; prior to this date, Microsoft-managed telephony remains the default.
- Organizations are responsible for the configuration, maintenance, and monitoring of their chosen provider’s integration.
- Potential limitations in message delivery, quality, or regional coverage depend on the selected provider.
- Compliance and security requirements must be carefully evaluated when integrating external telephony services.

**Integration with Related Azure Services**  
CYOT integrates directly with Microsoft Entra ID, impacting authentication-related services such as Azure Active Directory, Azure MFA, and password reset workflows. It does not alter the core identity management features but enhances the telephony component of authentication. Administrators should ensure compatibility with other Azure security and identity services when configuring CYOT.

**Summary Sentence**  
Starting October 30, 2026, Microsoft Entra ID will enable organizations to select supported third-party telephony providers for SMS and voice authentication, offering greater flexibility and control over authentication workflows.

---

### 2. Generally Available: Azure Cosmos DB Safe Key Rotation

**Published**: October 21, 2026 17:13:16 UTC
**Link**: [Generally Available: Azure Cosmos DB Safe Key Rotation](https://azure.microsoft.com/updates?id=576716)

**Update ID**: 576716
**Data source**: Azure Updates API

**Categories**: Launched, Databases, Internet of Things, Azure Cosmos DB, Feature

**Summary**:

- What was updated  
Azure Cosmos DB Safe Key Rotation is now generally available.

- Key changes or new features  
Safe Key Rotation introduces timestamp metadata for each account key, displaying when each key was last used. This feature enables users to identify which keys are actively in use before performing key rotation or retiring credentials, improving the safety and reliability of key management.

- Target audience affected  
Developers and IT professionals responsible for managing Azure Cosmos DB security, especially those handling access keys and credential rotation.

- Important notes if any  
The ability to view last-used timestamps for account keys helps reduce the risk of accidental service disruption during key rotation. This feature supports best practices for credential management and enhances compliance and security posture. Integrating Safe Key Rotation into operational workflows is recommended for organizations with strict security or compliance requirements.

For more details, see the official update: https://azure.microsoft.com/updates?id=576716

**Details**:

**Azure Update Report: Generally Available – Azure Cosmos DB Safe Key Rotation**

**Background and Purpose of the Update**  
Safe Key Rotation for Azure Cosmos DB addresses a critical security need for organizations managing sensitive data in cloud environments. Key rotation is a best practice for minimizing the risk of credential compromise, but without visibility into key usage, rotating or retiring keys can inadvertently disrupt applications or services. This update aims to enhance operational security by providing metadata that informs administrators about key activity, thereby facilitating safer credential management.

**Specific Features and Detailed Changes**  
The update introduces the ability to view timestamp metadata for each Cosmos DB account key. This metadata records when each key was last used, allowing administrators to distinguish between active and inactive keys. The feature is now generally available, meaning it is fully supported and ready for production use across all Azure regions.

**Technical Mechanisms and Implementation Methods**  
Azure Cosmos DB now maintains and exposes timestamp metadata associated with account keys. When a key is used—such as for authentication or accessing the database—the system updates the last-used timestamp. Administrators can access this information through the Azure Portal, REST APIs, or SDKs, depending on their operational workflow. This mechanism enables informed decision-making during key rotation: before retiring or replacing a key, administrators can verify whether it is still in use by any applications or services.

**Use Cases and Application Scenarios**  
- **Credential Rotation:** Organizations can safely rotate keys without risking service outages, as they can confirm which keys are actively being used.
- **Security Auditing:** Security teams can audit key usage patterns, ensuring compliance with internal policies or regulatory requirements.
- **Incident Response:** In the event of a suspected credential leak, administrators can quickly identify and retire unused keys, minimizing exposure.
- **Operational Maintenance:** DevOps teams can schedule regular key rotations and use the metadata to validate that new keys have been adopted by all relevant applications.

**Important Considerations and Limitations**  
- The feature provides visibility into key usage but does not automate rotation or retirement; administrators must take manual action based on the metadata.
- Timestamp metadata is only available for account keys; other credential types (such as resource tokens or managed identities) are not covered by this feature.
- Applications must be designed to handle key rotation gracefully, ensuring that they can switch to new keys without interruption.
- The accuracy of the last-used timestamp depends on the frequency and nature of key usage; infrequently used keys may appear inactive but could still be required for legacy systems.

**Integration with Related Azure Services**  
Safe Key Rotation complements Azure’s broader security ecosystem, including Azure Key Vault for centralized credential management and Azure Monitor for auditing and alerting. Administrators can integrate key usage data with monitoring solutions to trigger alerts when keys are used unexpectedly or remain unused for extended periods. The feature also aligns with Azure’s security best practices, supporting secure development and operational workflows across cloud-native and hybrid environments.

**Summary Sentence**  
Azure Cosmos DB Safe Key Rotation is now generally available, providing timestamp metadata for account keys to help administrators safely identify active credentials before rotation or retirement, thereby reducing operational risk and enhancing security management.

---


*This report was automatically generated - 2026-10-22 03:01:43 UTC*