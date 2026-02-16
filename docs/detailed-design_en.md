# Daily Azure Updates Generator - Detailed Design (English)

> For the full Japanese specification, see [detailed-design.md](./detailed-design.md).

## 1. System Overview

This system retrieves Azure Updates from RSS feeds, optionally enriches each item using the Azure Updates details API, and generates Markdown summaries with Azure OpenAI.

Current production scripts:

- `getlatestupdate_mid.py` (Japanese)
- `getlatestupdate_en_mid.py` (English)
- `generate_readme.py` / `generate_readme_en.py` (index README generation for output folders)

Execution in GitHub Actions is driven by `repository_dispatch` (`daily-update`) via `.github/workflows/dailycheck.yaml`.

## 2. Core Modes

- **Standard mode**: Filter updates within `CHECK_HOURS` and generate per-day report for current run date.
- **Details mode (`--details`)**: Enrich RSS items with Azure Updates details API (`/releasecommunications/api/v2/azure/{id}`), then generate both summary and detailed narrative.
- **Backfill mode (`--backfill-days` / `--backfill-startdate` / `--backfill-enddate`)**: Regenerate day-based historical files for a date range.

## 3. Processing Flow

1. Fetch RSS feed (with URL fallback and retry).
2. Parse/normalize dates and filter by cutoff.
3. (Optional) Fetch details API content by extracted update ID.
4. Generate summary text through Azure OpenAI Chat Completions.
5. Write `azure-updates-YYYY-MM-DD.md` into output directory.
6. Regenerate output directory `README.md` via generator scripts.

## 4. External API Connections

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

## 5. Configuration

| Variable            | Required | Default            | Description                                             |
| ------------------- | -------- | ------------------ | ------------------------------------------------------- |
| AOAI_ENDPOINT       | Yes      | -                  | Azure OpenAI endpoint                                   |
| DEPLOYMENT          | Yes      | -                  | Azure OpenAI deployment name                            |
| API_VER             | No       | 2025-01-01-preview | Azure OpenAI API version                                |
| CHECK_HOURS         | No       | 24                 | Time window for updates                                 |
| AZURE_TENANT_ID     | No       | -                  | Azure AD tenant ID (service principal/managed identity) |
| AZURE_CLIENT_ID     | No       | -                  | Client ID (service principal/managed identity)          |
| AZURE_CLIENT_SECRET | No       | -                  | Client secret (service principal only)                  |

Authentication behavior:

- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID` + `AZURE_CLIENT_SECRET`: Service principal
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID` + OIDC context: OIDC / Workload Identity
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID`: Managed identity
- Local development: Azure CLI credential after `az login`

## 6. Security Design

- `DefaultAzureCredential` automatically selects the available credential source.
- Credentials/secrets should be managed in environment variables or GitHub Secrets.
- Tokens and secrets must never be output in logs.

_Last updated: 2026-02-16_
