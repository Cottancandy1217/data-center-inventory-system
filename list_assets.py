#!/usr/bin/env python3

import csv
import argparse

INVENTORY_FILE = "inventory.csv"

def list_assets(asset_type=None, location=None, status=None):
    """Lists assets in the inventory, optionally filtered by type, location, or status."""

    try:
        with open(INVENTORY_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            assets = list(reader)

        filtered_assets = []
        for asset in assets:
            asset_dict = dict(zip(header, asset))
            if (asset_type is None or asset_dict["Type"].lower() == asset_type.lower()) and \
               (location is None or asset_dict["Location"].lower() == location.lower()) and \
               (status is None or asset_dict["Status"].lower() == status.lower()):
                filtered_assets.append(asset_dict)

        if filtered_assets:
            print("Assets:")
            for asset in filtered_assets:
                for key, value in asset.items():
                    print(f"{key}: {value}")
                print("-" * 20)  # Separator between assets
        else:
            print("No assets found matching the criteria.")

    except FileNotFoundError:
        print(f"Error: Inventory file '{INVENTORY_FILE}' not found.")
    except Exception as e:
        print(f"Error listing assets: {e}")

def main():
    parser = argparse.ArgumentParser(description="List assets in the inventory.")
    parser.add_argument("--type", help="Filter by asset type.")
    parser.add_argument("--location", help="Filter by location.")
    parser.add_argument("--status", help="Filter by status.")
    args = parser.parse_args()
    list_assets(args.type, args.location, args.status)

if __name__ == "__main__":
    main()
