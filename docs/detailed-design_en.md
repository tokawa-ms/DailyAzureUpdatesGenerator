# Daily Azure Updates Generator - Detailed Design (English)

> For the full Japanese specification, see [detailed-design.md](./detailed-design.md).

## 1. System Overview

This system retrieves Azure Updates from RSS feeds, optionally enriches each item using the Azure Updates details API, and generates Markdown summaries with Azure OpenAI.

## 2. External API Connections

### 2.1 Azure Updates RSS API
- Endpoint:
  - `https://www.microsoft.com/releasecommunications/api/v2/azure/rss`
  - `https://azurecomcdn.azureedge.net/en-us/updates/feed/`
  - `https://azure.microsoft.com/en-us/updates/feed/`
- Auth: Not required

### 2.2 Azure Updates Details API
- Endpoint: `https://www.microsoft.com/releasecommunications/api/v2/azure/{id}`
- Method: GET
- Auth: Not required

### 2.3 Azure OpenAI API
- Endpoint: `{AOAI_ENDPOINT}/openai/deployments/{DEPLOYMENT}/chat/completions`
- Method: POST
- Auth: Azure AD token via `DefaultAzureCredential`
- API version default: `2025-01-01-preview`

## 3. Configuration

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| AOAI_ENDPOINT | Yes | - | Azure OpenAI endpoint |
| DEPLOYMENT | Yes | - | Azure OpenAI deployment name |
| API_VER | No | 2025-01-01-preview | Azure OpenAI API version |
| CHECK_HOURS | No | 24 | Time window for updates |
| AZURE_TENANT_ID | No | - | Azure AD tenant ID (service principal/managed identity) |
| AZURE_CLIENT_ID | No | - | Client ID (service principal/managed identity) |
| AZURE_CLIENT_SECRET | No | - | Client secret (service principal only) |

Authentication behavior:
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID` + `AZURE_CLIENT_SECRET`: Service principal
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID`: Managed identity
- Local development: Azure CLI credential after `az login`

## 4. Security Design

- `DefaultAzureCredential` automatically selects the available credential source.
- Credentials/secrets should be managed in environment variables or GitHub Secrets.
- Tokens and secrets must never be output in logs.
