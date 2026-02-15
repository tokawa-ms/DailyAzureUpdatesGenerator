# Azure Updates Automatic Summary

## Japanese version

Japanese Version is [here](./README.md)

## Overview

Automatic summaries of Azure Updates are stored in the [updates_en](./updates_en) directory.
The automatic summary feature runs daily at noon Japan time via GitHub Actions, collecting Azure Updates information from the past day and generating English summaries.

## Disclaimer

The automatic summary reports are generated based on information obtained from RSS feeds and do not guarantee accuracy or completeness. Users should use the provided information at their own risk.
If you find content of interest, we recommend checking the original information by referring to the links included in the reports.

# Azure Updates RSS Feed Processing Application

This application reads Azure Updates RSS feeds, summarizes Azure Update information that has been updated within a specified time period using Azure OpenAI's GPT-4.1-mini model in English, and outputs the results in Markdown format.

## Features

- **Robust RSS feed retrieval**: Tries multiple URLs to ensure reliable feed acquisition
- **Details mode**: Retrieve detailed information from Azure Updates API (`--details` option)
- Filtering of new updates within specified time periods
- English summary generation using Azure OpenAI
- Detailed report output in Markdown format
- Comprehensive error handling and retry functionality
- Detailed logging and monitoring
- **Test mode**: Feed retrieval testing functionality

## Required Environment Variables (DefaultAzureCredential Authentication)

Before running the application, set the following environment variables:

- `AOAI_ENDPOINT`: Azure OpenAI endpoint URL
- `DEPLOYMENT`: Azure OpenAI deployment name
- `API_VER`: Azure OpenAI API version (default: 2025-01-01-preview)
- `CHECK_HOURS`: Target check time (in hours, default: 24)
- `AZURE_TENANT_ID`: Azure AD tenant ID (optional)
- `AZURE_CLIENT_ID`: Client ID (optional)
- `AZURE_CLIENT_SECRET`: Client secret (used for service principal authentication)

Authentication is auto-detected by `DefaultAzureCredential`.
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID` + `AZURE_CLIENT_SECRET`: service principal authentication
- `AZURE_TENANT_ID` + `AZURE_CLIENT_ID` (+ managed identity-enabled environment): managed identity authentication
- Local development: Azure CLI authentication after `az login`

## Installation

1. Install required packages:

```cmd
pip install -r requirements.txt
```

2. Test RSS feed:

```cmd
test_feed.bat
```

or

```cmd
python getlatestupdate_en_mid.py --test-feed --verbose
```

## Usage

### Test Execution (Recommended: Run First)

```cmd
# Test RSS feed retrieval
python getlatestupdate_en_mid.py --test-feed --verbose

# Test execution with batch file
test_feed.bat
```

### Basic Usage

```cmd
python getlatestupdate_en_mid.py
```

### Execution with Options

```cmd
# Check updates from the past 12 hours
python getlatestupdate_en_mid.py --hours 12

# Details mode (retrieve detailed information from Azure Updates API)
python getlatestupdate_en_mid.py --details

# Specify output directory
python getlatestupdate_en_mid.py --output-dir reports

# Output detailed logs
python getlatestupdate_en_mid.py --verbose

# Run RSS feed test only
python getlatestupdate_en_mid.py --test-feed

# Combine multiple options (details mode + detailed logs + 72 hours)
python getlatestupdate_en_mid.py --details --verbose --hours 72
```

### Using Details Mode

Details mode (`--details`) retrieves detailed information from the Azure Updates API in addition to RSS feed information:

```cmd
# Run in details mode
python getlatestupdate_en_mid.py --details

# Batch file example with details mode
run_details_example.bat
```

**Details mode features:**

- Retrieve detailed information for each article from Azure Updates API
- Use more accurate and complete article titles and content
- Display information retrieved from API in reports
- Detailed information source tracking and log output

### Environment Variable Setup Example (Windows)

```cmd
set AOAI_ENDPOINT=https://your-openai-resource.openai.azure.com
set DEPLOYMENT=gpt-4-mini
set API_VER=2025-01-01-preview
set CHECK_HOURS=24
set AZURE_TENANT_ID=your-tenant-id
set AZURE_CLIENT_ID=your-client-id
set AZURE_CLIENT_SECRET=your-client-secret
```

## Troubleshooting

### RSS Feed Retrieval Errors

1. **Check with test mode**:

   ```cmd
   python getlatestupdate_en_mid.py --test-feed --verbose
   ```

2. **Check log file**: `azure_updates.log`

3. **Verify network connection**: Internet connection and proxy settings

4. **Multiple URL attempts**: The application automatically tries multiple RSS URLs

### Details Mode Related Troubleshooting

1. **Test details mode**:

   ```cmd
   python test_details.py
   ```

2. **API access errors**: If Azure Updates API is temporarily unavailable, processing continues in standard mode

3. **Update ID extraction failure**: When ID cannot be extracted for some articles, RSS information is used

### Common Errors and Solutions

- **"No entries in feed"**: RSS URL may have been changed
- **"not well-formed (invalid token)"**: XML parse error. Trying alternative URLs
- **HTTP connection errors**: Check network settings and firewall

## Output

The application generates:

1. **Markdown report**: `updates/azure-updates-YYYY-MM-DD.md`
2. **Log file**: `azure_updates.log`

## Report Contents

### Standard Mode

- Generation date/time and target period
- Summary of update count
- Details of each update:
  - Title (from RSS feed)
  - Publication date/time
  - Link
  - Category
  - AI-generated English summary
  - Original detailed description (from RSS feed)

### Details Mode (`--details`)

In addition to the above:

- **Update ID**: Individual article identifier
- **Data source**: Clear indication of Azure Updates API usage
- **Enhanced title**: More accurate title retrieved from API
- **Detailed content**: Complete article content retrieved from API
- **Improved summary**: Summary based on more detailed and accurate information

## Error Handling

- **Multiple RSS URLs**: Automatic fallback when primary URL fails
- **Network errors**: Automatic retry and timeout settings
- **XML parse errors**: Minor errors are ignored to continue processing
- **API rate limiting**: Appropriate wait time settings
- **Detailed logs**: Comprehensive logging for troubleshooting

## Security Considerations

- API keys retrieved from environment variables
- Use of HTTPS communication
- Appropriate timeout settings
- Session management and resource cleanup
- Proper User-Agent configuration

## Limitations

- Dependent on Azure OpenAI rate limits
- Dependent on RSS feed availability
- Date parsing accuracy depends on feed format
