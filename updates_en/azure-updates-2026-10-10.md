# October 10, 2026 - Azure Updates Summary Report (Details Mode)

**Generated on**: October 10, 2026
**Target period**: Within the last 24 hours
**Processing mode**: Details Mode
**Number of updates**: 1 items

## Update List

### 1. Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters

**Published**: October 09, 2026 20:27:17 UTC
**Link**: [Retirement: Azure Key Vault Secrets Provider Extension for Azure Arc enabled Kubernetes clusters](https://azure.microsoft.com/updates?id=570313)

**Update ID**: 570313
**Data source**: Azure Updates API

**Categories**: Retirements

**Summary**:

- What was updated  
The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes clusters is being retired.

- Key changes or new features  
Microsoft announced that the Azure Key Vault Secrets Provider Extension will be retired on October 9, 2027. Users are advised to migrate to the Azure Key Vault Secret Store Extension, which is the recommended alternative. The new extension offers improved capabilities and ongoing support.

- Target audience affected  
This update impacts developers and IT professionals managing secrets in Azure Arc-enabled Kubernetes clusters using the Key Vault Secrets Provider Extension.

- Important notes if any  
Existing deployments of the Azure Key Vault Secrets Provider Extension will continue to work until the retirement date, but no new features or enhancements will be provided. After October 9, 2027, the extension will no longer be supported, and users may experience service disruptions if they have not migrated. It is recommended to begin planning and testing migration to the Azure Key Vault Secret Store Extension as soon as possible to ensure continuity and take advantage of the latest features and security updates.

For more information, see the official announcement: https://azure.microsoft.com/updates?id=570313

**Details**:

**Azure Update Report: Retirement of Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes Clusters**

**Background and Purpose of the Update**  
Microsoft has announced the retirement of the Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes clusters, effective October 9, 2027. This update is intended to inform customers and IT professionals that the current extension will no longer be supported after the retirement date. The purpose is to encourage migration to the Azure Key Vault Secret Store Extension, which is the recommended successor.

**Specific Features and Detailed Changes**  
The primary change is the deprecation and eventual discontinuation of the Azure Key Vault Secrets Provider Extension. Users must transition to the Azure Key Vault Secret Store Extension. The Secret Store Extension is designed to provide similar functionality for securely accessing secrets stored in Azure Key Vault from Kubernetes workloads, but it is more modern and aligns with current Azure Arc and Kubernetes integration best practices.

**Technical Mechanisms and Implementation Methods**  
The retiring extension enabled Kubernetes clusters managed by Azure Arc to retrieve secrets from Azure Key Vault and inject them into pods as environment variables or mounted files. The mechanism involved installing the extension on the Arc-enabled cluster, configuring access policies in Key Vault, and referencing secrets in Kubernetes manifests.

The Azure Key Vault Secret Store Extension, which customers are advised to migrate to, is based on the Kubernetes Secrets Store CSI (Container Storage Interface) driver. This approach allows secrets to be mounted as files within pods, providing enhanced flexibility and security. The migration process involves uninstalling the old extension, installing the Secret Store Extension, and updating Kubernetes manifests to reference secrets using the new CSI driver syntax.

**Use Cases and Application Scenarios**  
Typical use cases include:
- Securely injecting credentials, API keys, certificates, or other sensitive configuration data into applications running in Azure Arc-enabled Kubernetes clusters.
- Centralized secret management using Azure Key Vault, while maintaining compliance and governance.
- Supporting hybrid and multi-cloud scenarios where Kubernetes clusters are not running directly in Azure but are managed via Azure Arc.

**Important Considerations and Limitations**  
- After October 9, 2027, the Azure Key Vault Secrets Provider Extension will no longer receive updates, support, or security patches.
- Migration to the Azure Key Vault Secret Store Extension is mandatory to maintain continued access to Key Vault secrets in Arc-enabled Kubernetes clusters.
- The migration may require changes to Kubernetes manifests and cluster configuration, as the Secret Store Extension uses the CSI driver model.
- Customers should review compatibility and test their workloads with the new extension to ensure seamless operation.

**Integration with Related Azure Services**  
Both extensions integrate with Azure Key Vault for secret management and Azure Arc for cluster management. The Secret Store Extension also leverages the Kubernetes CSI driver framework, improving integration with native Kubernetes features. This ensures that secrets are managed in accordance with Azure security policies and can be accessed by workloads running in Arc-enabled clusters regardless of their physical location.

**Summary Sentence**  
The Azure Key Vault Secrets Provider Extension for Azure Arc-enabled Kubernetes clusters will be retired on October 9, 2027; customers should migrate to the Azure Key Vault Secret Store Extension to ensure continued secure access to Azure Key Vault secrets in their Kubernetes workloads.

---


*This report was automatically generated - 2026-10-10 03:01:10 UTC*