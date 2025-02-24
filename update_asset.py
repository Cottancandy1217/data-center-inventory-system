#!/usr/bin/env python3

import csv
import argparse

INVENTORY_FILE = "inventory.csv"

def update_asset(**kwargs):
    """Updates the attributes of an existing asset in the inventory."""
    asset_id = kwargs.get("asset_id")

    try:
        with open(INVENTORY_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            assets = list(reader)

        updated = False
        with open(INVENTORY_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Write header back

            for asset in assets:
                if asset[0] == asset_id:
                    for key, value in kwargs.items():
                        if value is not None and key != "asset_id": #asset_id already used, so do not use it again.
                            index = header.index(key.replace("_", " ").title())
                            asset[index] = str(value)
                    writer.writerow(asset)
                    updated = True
                else:
                    writer.writerow(asset)

        if updated:
            print(f"Asset '{asset_id}' updated successfully.")
        else:
            print(f"Asset '{asset_id}' not found.")

    except FileNotFoundError:
        print(f"Error: Inventory file '{INVENTORY_FILE}' not found.")
    except ValueError as e:
        print(f"Error: Invalid field name: {e}")
    except Exception as e:
        print(f"Error updating asset: {e}")

def main():
    parser = argparse.ArgumentParser(description="Update an asset in the inventory.")
    parser.add_argument("--asset_id", required=True, help="Asset ID to update.")
    parser.add_argument("--type", help="Asset Type")
    parser.add_argument("--manufacturer", help="Manufacturer")
    parser.add_argument("--model", help="Model")
    parser.add_argument("--serial_number", help="Serial Number")
    parser.add_argument("--location", help="Location")
    parser.add_argument("--status", help="Status")
    parser.add_argument("--ip_address", help="IP Address")
    parser.add_argument("--power_consumption", type=int, help="Power Consumption (Watts)")

    args = parser.parse_args()

    update_asset(**vars(args)) #only pass the dictionary of values.

if __name__ == "__main__":
    main()
