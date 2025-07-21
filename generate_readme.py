#!/usr/bin/env python3
"""
Azure Updates ファイルリスト生成スクリプト

指定されたディレクトリ内の azure-updates-yyyy-mm-dd.md ファイルを
日付が新しい順にリスト化し、README.md として出力します。
"""

import os
import sys
import re
from datetime import datetime
from typing import List, Tuple
import argparse


def find_azure_update_files(directory: str) -> List[Tuple[str, datetime]]:
    """
    指定されたディレクトリから azure-updates-yyyy-mm-dd.md ファイルを見つけて
    ファイル名と日付のタプルのリストを返す

    Args:
        directory (str): 検索対象のディレクトリパス

    Returns:
        List[Tuple[str, datetime]]: (ファイル名, 日付) のタプルのリスト
    """
    if not os.path.exists(directory):
        print(f"エラー: ディレクトリ '{directory}' が存在しません。")
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
                            f"警告: ファイル '{filename}' の日付形式が正しくありません。スキップします。"
                        )
    except Exception as e:
        print(
            f"エラー: ディレクトリ '{directory}' の読み取り中にエラーが発生しました: {e}"
        )
        return []

    return files_with_dates


def generate_readme_content(
    files_with_dates: List[Tuple[str, datetime]], directory_name: str
) -> str:
    """
    README.md の内容を生成する

    Args:
        files_with_dates (List[Tuple[str, datetime]]): (ファイル名, 日付) のタプルのリスト
        directory_name (str): ディレクトリ名

    Returns:
        str: README.md の内容
    """
    # 日付が新しい順にソート
    sorted_files = sorted(files_with_dates, key=lambda x: x[1], reverse=True)

    # 日本時間（JST）で現在時刻を取得
    try:
        # zoneinfo を使用（Python 3.9+）
        from zoneinfo import ZoneInfo

        current_time = datetime.now(ZoneInfo("Asia/Tokyo")).strftime(
            "%Y年%m月%d日 %H:%M:%S JST"
        )
    except (ImportError, Exception):
        # zoneinfo が使用できない場合は、UTC+9の固定オフセットを使用
        from datetime import timezone, timedelta

        jst = timezone(timedelta(hours=9))
        current_time = datetime.now(jst).strftime("%Y年%m月%d日 %H:%M:%S JST")

    content = f"""# Azure Updates ファイル一覧

最終更新: {current_time}

このディレクトリには、以下の Azure Updates ファイルが含まれています：

## Daily Azure Updates （新しい順）

"""

    if not sorted_files:
        content += "現在、azure-updates-yyyy-mm-dd.md 形式のファイルはありません。\n"
    else:
        content += f"総ファイル数: {len(sorted_files)}\n\n"

        for i, (filename, date_obj) in enumerate(sorted_files, 1):
            formatted_date = date_obj.strftime("%Y年%m月%d日")
            content += f"{i}. [{filename}](./{filename}) - {formatted_date}\n"

    return content


def write_readme(directory: str, content: str) -> bool:
    """
    README.md ファイルを書き込む

    Args:
        directory (str): 出力先ディレクトリ
        content (str): README.md の内容

    Returns:
        bool: 成功した場合 True
    """
    readme_path = os.path.join(directory, "README.md")

    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"エラー: README.md の書き込み中にエラーが発生しました: {e}")
        return False


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="Azure Updates ファイルの一覧を生成し、README.md として出力します"
    )
    parser.add_argument(
        "directory", help="Azure Updates ファイルが含まれているディレクトリのパス"
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="詳細な出力を表示")

    args = parser.parse_args()

    target_directory = os.path.abspath(args.directory)

    if args.verbose:
        print(f"対象ディレクトリ: {target_directory}")

    # Azure Updates ファイルを検索
    files_with_dates = find_azure_update_files(target_directory)

    if args.verbose:
        print(f"発見されたファイル数: {len(files_with_dates)}")
        for filename, date_obj in files_with_dates:
            print(f"  - {filename} ({date_obj.strftime('%Y-%m-%d')})")

    # README.md の内容を生成
    directory_name = os.path.basename(target_directory)
    readme_content = generate_readme_content(files_with_dates, directory_name)

    # README.md を書き込み
    if write_readme(target_directory, readme_content):
        readme_path = os.path.join(target_directory, "README.md")
        print(f"README.md を正常に生成しました: {readme_path}")

        if args.verbose:
            print("\n生成された内容:")
            print("-" * 50)
            print(readme_content)
    else:
        print("README.md の生成に失敗しました。")
        sys.exit(1)


if __name__ == "__main__":
    main()
