#!/usr/bin/env python3

import csv
import argparse
import os

INVENTORY_FILE = "inventory.csv"

def remove_asset(asset_id):
    """Removes an asset from the inventory based on its Asset ID."""

    try:
        if not os.path.isfile(INVENTORY_FILE):
            print(f"Error: Inventory file '{INVENTORY_FILE}' not found.")
            return

        with open(INVENTORY_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            assets = list(reader)

        removed = False
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header back

            for asset in assets:
                if asset[0] != asset_id:  # Asset ID is the first column
                    writer.writerow(asset)
                else:
                    removed = True

        if removed:
            print(f"Asset '{asset_id}' removed successfully.")
        else:
            print(f"Asset '{asset_id}' not found.")

    except Exception as e:
        print(f"Error removing asset: {e}")

def main():
    parser = argparse.ArgumentParser(description="Remove an asset from the inventory.")
    parser.add_argument("asset_id", help="Asset ID to remove.")
    args = parser.parse_args()
    remove_asset(args.asset_id)

if __name__ == "__main__":
    main()
