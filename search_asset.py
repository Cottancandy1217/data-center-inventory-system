#!/usr/bin/env python3

import csv
import argparse

INVENTORY_FILE = "inventory.csv"

def search_assets(search_term):
    """Searches for assets in the inventory based on a search term."""

    try:
        with open(INVENTORY_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            found_assets = []
            for row in reader:
                for field in row:
                    if search_term.lower() in field.lower():
                        found_assets.append(dict(zip(header, row)))
                        break  # Avoid duplicates if search term matches multiple fields

        if found_assets:
            print("Found Assets:")
            for asset in found_assets:
                for key, value in asset.items():
                    print(f"{key}: {value}")
                print("-" * 20)  # Separator between assets
        else:
            print(f"No assets found matching '{search_term}'.")

    except FileNotFoundError:
        print(f"Error: Inventory file '{INVENTORY_FILE}' not found.")
    except Exception as e:
        print(f"Error searching assets: {e}")

def main():
    parser = argparse.ArgumentParser(description="Search for assets in the inventory.")
    parser.add_argument("search_term", help="The search term to use.")
    args = parser.parse_args()
    search_assets(args.search_term)

if __name__ == "__main__":
    main()
