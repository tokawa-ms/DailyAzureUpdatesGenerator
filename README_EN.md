# Azure Updates Automatic Summary

## Overview

Automatic summaries of Azure Updates are stored in the [updates_en](./updates_en) directory.
The automatic summary feature runs daily at noon Japan time via GitHub Actions, collecting Azure Updates information from the past day and generating Japanese summaries.

## Disclaimer

The automatic summary reports are generated based on information obtained from RSS feeds and do not guarantee accuracy or completeness. Users should use the provided information at their own risk.
If you find content of interest, we recommend checking the original information by referring to the links included in the reports.

# Azure Updates RSS Feed Processing Application

This application reads Azure Updates RSS feeds, summarizes Azure Update information that has been updated within a specified time period using Azure OpenAI's GPT-4.1-mini model in Japanese, and outputs the results in Markdown format.

## Features

- **Robust RSS feed retrieval**: Tries multiple URLs to ensure reliable feed acquisition
- Filtering of new updates within specified time periods
- Japanese summary generation using Azure OpenAI
- Detailed report output in Markdown format
- Comprehensive error handling and retry functionality
- Detailed logging and monitoring
- **Test mode**: Feed retrieval testing functionality

## Required Environment Variables

Before running the application, set the following environment variables:

- `AOAI_ENDPOINT`: Azure OpenAI endpoint URL
- `AOAI_KEY`: Azure OpenAI API key
- `DEPLOYMENT`: Azure OpenAI deployment name
- `API_VER`: Azure OpenAI API version (default: 2024-02-15-preview)
- `CHECK_HOURS`: Target check time (in hours, default: 24)

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
python getlatestupdate.py --test-feed --verbose
```

## Usage

### Test Execution (Recommended: Run First)

```cmd
# Test RSS feed retrieval
python getlatestupdate.py --test-feed --verbose

# Test execution with batch file
test_feed.bat
```

### Basic Usage

```cmd
python getlatestupdate.py
```

### Execution with Options

```cmd
# Check updates from the past 12 hours
python getlatestupdate.py --hours 12

# Specify output directory
python getlatestupdate.py --output-dir reports

# Output detailed logs
python getlatestupdate.py --verbose

# Run RSS feed test only
python getlatestupdate.py --test-feed

# Combine multiple options
python getlatestupdate.py --hours 6 --output-dir reports --verbose
```

### Environment Variable Setup Example (Windows)

```cmd
set AOAI_ENDPOINT=https://your-openai-resource.openai.azure.com
set AOAI_KEY=your-api-key-here
set DEPLOYMENT=gpt-4-mini
set API_VER=2024-02-15-preview
set CHECK_HOURS=24
```

## Troubleshooting

### RSS Feed Retrieval Errors

1. **Check with test mode**:

   ```cmd
   python getlatestupdate.py --test-feed --verbose
   ```

2. **Check log file**: `azure_updates.log`

3. **Verify network connection**: Internet connection and proxy settings

4. **Multiple URL attempts**: The application automatically tries multiple RSS URLs

### Common Errors and Solutions

- **"No entries in feed"**: RSS URL may have been changed
- **"not well-formed (invalid token)"**: XML parse error. Trying alternative URLs
- **HTTP connection errors**: Check network settings and firewall

## Output

The application generates:

1. **Markdown report**: `updates/azure-updates-YYYY-MM-DD.md`
2. **Log file**: `azure_updates.log`

## Report Contents

- Generation date/time and target period
- Summary of update count
- Details of each update:
  - Title
  - Publication date/time
  - Link
  - Category
  - AI-generated Japanese summary
  - Original detailed description

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
