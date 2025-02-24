# Data Center Inventory Management System

## Project Overview

This project implements a simplified inventory management system for data center assets using Python and a CSV (Comma Separated Values) file. The system allows users to add, search, update, list, and remove assets, simulating real-world data center inventory management.

## Features

* **Add Assets:** Add new data center assets to the inventory with details like Asset ID, Type, Manufacturer, Model, Serial Number, Location, Status, IP Address, and Power Consumption.
* **Search Assets:** Search for assets based on various criteria such as Asset ID, Type, or Location.
* **Update Assets:** Modify the attributes of existing assets in the inventory.
* **List Assets:** Display a list of all assets or filter assets based on specific criteria.
* **Remove Assets:** Remove assets from the inventory.
* **Generate Reports (Optional):** Generate reports such as a list of offline servers or inventory by location.

## Usage

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd data-center-inventory-system
    ```

2.  **Install Python 3 (if not already installed):**

    Ensure you have Python 3 installed on your system.

3.  **Run the Scripts:**

    Use the following command-line arguments to interact with the scripts:

    * **Add Asset:**

        ```bash
        python3 add_asset.py --asset_id SERVER001 --type server --manufacturer Dell --model PowerEdgeR740 --serial_number ABC123XYZ --location "Rack A1" --status online --ip_address 192.168.1.10 --power_consumption 500
        ```

    * **Search Asset:**

        ```bash
        python3 search_asset.py --search_term SERVER001
        ```

    * **Update Asset:**

        ```bash
        python3 update_asset.py --asset_id SERVER001 --status offline
        ```

    * **List Assets:**

        ```bash
        python3 list_assets.py
        ```

    * **Remove Asset:**

        ```bash
        python3 remove_asset.py --asset_id SERVER001
        ```

    * **Generate Report (Optional):**

        ```bash
        python3 generate_report.py --report_type offline_servers
        ```

4.  **Data Storage:**

    The inventory data is stored in a CSV file named `inventory.csv`.

## Data Structure (inventory.csv)

The `inventory.csv` file uses the following structure:

```csv
Asset ID,Type,Manufacturer,Model,Serial Number,Location,Status,IP Address,Power Consumption
SERVER001,server,Dell,PowerEdgeR740,ABC123XYZ,Rack A1,online,192.168.1.10,500
SWITCH001,switch,Cisco,Catalyst 2960,DEF456UVW,Rack A2,online,192.168.1.20,100
...# Data Center Inventory Management System

## Project Overview

This project implements a simplified inventory management system for data center assets using Python and a CSV (Comma Separated Values) file. The system allows users to add, search, update, list, and remove assets, simulating real-world data center inventory management.

## Features

* **Add Assets:** Add new data center assets to the inventory with details like Asset ID, Type, Manufacturer, Model, Serial Number, Location, Status, IP Address, and Power Consumption.
* **Search Assets:** Search for assets based on various criteria such as Asset ID, Type, or Location.
* **Update Assets:** Modify the attributes of existing assets in the inventory.
* **List Assets:** Display a list of all assets or filter assets based on specific criteria.
* **Remove Assets:** Remove assets from the inventory.
* **Generate Reports (Optional):** Generate reports such as a list of offline servers or inventory by location.

## Usage

1.  **Clone the Repository:**

    ```bash
    git clone [repository URL]
    cd data-center-inventory-system
    ```

2.  **Install Python 3 (if not already installed):**

    Ensure you have Python 3 installed on your system.

3.  **Run the Scripts:**

    Use the following command-line arguments to interact with the scripts:

    * **Add Asset:**

        ```bash
        python3 add_asset.py --asset_id SERVER001 --type server --manufacturer Dell --model PowerEdgeR740 --serial_number ABC123XYZ --location "Rack A1" --status online --ip_address 192.168.1.10 --power_consumption 500
        ```

    * **Search Asset:**

        ```bash
        python3 search_asset.py --search_term SERVER001
        ```

    * **Update Asset:**

        ```bash
        python3 update_asset.py --asset_id SERVER001 --status offline
        ```

    * **List Assets:**

        ```bash
        python3 list_assets.py
        ```

    * **Remove Asset:**

        ```bash
        python3 remove_asset.py --asset_id SERVER001
        ```

    * **Generate Report (Optional):**

        ```bash
        python3 generate_report.py --report_type offline_servers
        ```

4.  **Data Storage:**

    The inventory data is stored in a CSV file named `inventory.csv`.

## Data Structure (inventory.csv)

The `inventory.csv` file uses the following structure:

```csv
Asset ID,Type,Manufacturer,Model,Serial Number,Location,Status,IP Address,Power Consumption
SERVER001,server,Dell,PowerEdgeR740,ABC123XYZ,Rack A1,online,192.168.1.10,500
SWITCH001,switch,Cisco,Catalyst 2960,DEF456UVW,Rack A2,online,192.168.1.20,100
...


Dependencies 
* **Python 3*

 Author
Angelee Morquin 

Contact
Email: sweety.angel1217@gmail.com
LinkedIn: https://www.linkedin.com/in/angelee-morquin-934b51125/
