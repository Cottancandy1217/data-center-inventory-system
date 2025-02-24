#!/usr/bin/env python3

import csv
import argparse
import os

INVENTORY_FILE = "inventory.csv"

def add_asset(asset_id, asset_type, manufacturer, model, serial_number, location, status, ip_address, power_consumption):
    """Adds a new asset to the inventory."""

    header = ["Asset ID", "Type", "Manufacturer", "Model", "Serial Number", "Location", "Status", "IP Address", "Power Consumption"]
    new_asset = [asset_id, asset_type, manufacturer, model, serial_number, location, status, ip_address, power_consumption]

    file_exists = os.path.isfile(INVENTORY_FILE)

    try:
        with open(INVENTORY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)  # Write header if file is newly created
            writer.writerow(new_asset)
        print(f"Asset '{asset_id}' added successfully.")

    except Exception as e:
        print(f"Error adding asset: {e}")

def main():
    parser = argparse.ArgumentParser(description="Add a new asset to the inventory.")
    parser.add_argument("--asset_id", required=True, help="Asset ID")
    parser.add_argument("--type", required=True, help="Asset Type")
    parser.add_argument("--manufacturer", required=True, help="Manufacturer")
    parser.add_argument("--model", required=True, help="Model")
    parser.add_argument("--serial_number", required=True, help="Serial Number")
    parser.add_argument("--location", required=True, help="Location")
    parser.add_argument("--status", required=True, help="Status")
    parser.add_argument("--ip_address", required=True, help="IP Address")
    parser.add_argument("--power_consumption", required=True, type=int, help="Power Consumption (Watts)")

    args = parser.parse_args()

    add_asset(args.asset_id, args.type, args.manufacturer, args.model, args.serial_number, args.location, args.status, args.ip_address, args.power_consumption)

if __name__ == "__main__":
    main()
