#!/usr/bin/env python3
"""
Azure Updates File List Generation Script

Lists azure-updates-yyyy-mm-dd.md files in the specified directory
in descending order by date and outputs as README.md.
"""

import os
import sys
import re
from datetime import datetime
from typing import List, Tuple
import argparse


def find_azure_update_files(directory: str) -> List[Tuple[str, datetime]]:
    """
    Find azure-updates-yyyy-mm-dd.md files in the specified directory and
    return a list of tuples containing filename and date

    Args:
        directory (str): Directory path to search

    Returns:
        List[Tuple[str, datetime]]: List of tuples containing (filename, date)
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return []

    pattern = re.compile(r"^azure-updates-(\d{4}-\d{2}-\d{2})\.md$")
    files_with_dates = []

    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                match = pattern.match(filename)
                if match:
                    date_str = match.group(1)
                    try:
                        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                        files_with_dates.append((filename, date_obj))
                    except ValueError:
                        print(
                            f"Warning: Date format in file '{filename}' is incorrect. Skipping."
                        )
    except Exception as e:
        print(f"Error: An error occurred while reading directory '{directory}': {e}")
        return []

    return files_with_dates


def generate_readme_content(
    files_with_dates: List[Tuple[str, datetime]], directory_name: str
) -> str:
    """
    Generate README.md content

    Args:
        files_with_dates (List[Tuple[str, datetime]]): List of tuples containing (filename, date)
        directory_name (str): Directory name

    Returns:
        str: README.md content
    """
    # Sort by date in descending order (newest first)
    sorted_files = sorted(files_with_dates, key=lambda x: x[1], reverse=True)

    current_time = datetime.now().strftime("%B %d, %Y %H:%M:%S")

    content = f"""# Azure Updates File List

Last Updated: {current_time}

This directory contains the following Azure Updates files:

## Daily Azure Updates (Newest First)

"""

    if not sorted_files:
        content += (
            "Currently, there are no files in azure-updates-yyyy-mm-dd.md format.\n"
        )
    else:
        content += f"Total files: {len(sorted_files)}\n\n"

        for i, (filename, date_obj) in enumerate(sorted_files, 1):
            formatted_date = date_obj.strftime("%B %d, %Y")
            content += f"{i}. [{filename}](./{filename}) - {formatted_date}\n"

    return content


def write_readme(directory: str, content: str) -> bool:
    """
    Write README.md file

    Args:
        directory (str): Output directory
        content (str): README.md content

    Returns:
        bool: True if successful
    """
    readme_path = os.path.join(directory, "README.md")

    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error: An error occurred while writing README.md: {e}")
        return False


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="Generate a list of Azure Updates files and output as README.md"
    )
    parser.add_argument(
        "directory", help="Path to the directory containing Azure Updates files"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Display detailed output"
    )

    args = parser.parse_args()

    target_directory = os.path.abspath(args.directory)

    if args.verbose:
        print(f"Target directory: {target_directory}")

    # Search for Azure Updates files
    files_with_dates = find_azure_update_files(target_directory)

    if args.verbose:
        print(f"Files found: {len(files_with_dates)}")
        for filename, date_obj in files_with_dates:
            print(f"  - {filename} ({date_obj.strftime('%Y-%m-%d')})")

    # Generate README.md content
    directory_name = os.path.basename(target_directory)
    readme_content = generate_readme_content(files_with_dates, directory_name)

    # Write README.md
    if write_readme(target_directory, readme_content):
        readme_path = os.path.join(target_directory, "README.md")
        print(f"README.md generated successfully: {readme_path}")

        if args.verbose:
            print("\nGenerated content:")
            print("-" * 50)
            print(readme_content)
    else:
        print("Failed to generate README.md.")
        sys.exit(1)


if __name__ == "__main__":
    main()
