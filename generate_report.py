#!/usr/bin/env python3

import csv
import argparse

INVENTORY_FILE = "inventory.csv"

def generate_report(report_type):
    """Generates reports based on the specified report type."""

    try:
        with open(INVENTORY_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Read header row
            assets = list(reader)

        if report_type == "offline_servers":
            offline_servers = [dict(zip(header, asset)) for asset in assets if asset[6].lower() == "offline" and asset[1].lower() == "server"] #asset[6] is the status, asset[1] is the type
            if offline_servers:
                print("Offline Servers:")
                for server in offline_servers:
                    for key, value in server.items():
                        print(f"{key}: {value}")
                    print("-" * 20)
            else:
                print("No offline servers found.")

        elif report_type == "inventory_by_location":
            inventory_by_location = {}
            for asset in assets:
                location = asset[5].lower() #asset[5] is the location
                if location not in inventory_by_location:
                    inventory_by_location[location] = []
                inventory_by_location[location].append(dict(zip(header, asset)))

            if inventory_by_location:
                print("Inventory by Location:")
                for location, assets_list in inventory_by_location.items():
                    print(f"\nLocation: {location.title()}")
                    for asset in assets_list:
                        for key, value in asset.items():
                            print(f"{key}: {value}")
                        print("-" * 20)
            else:
                print("No inventory found.")

        else:
            print(f"Invalid report type: {report_type}")

    except FileNotFoundError:
        print(f"Error: Inventory file '{INVENTORY_FILE}' not found.")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    parser = argparse.ArgumentParser(description="Generate reports from the inventory.")
    parser.add_argument("report_type", choices=["offline_servers", "inventory_by_location"], help="Type of report to generate.")
    args = parser.parse_args()
    generate_report(args.report_type)

if __name__ == "__main__":
    main()
