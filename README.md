
![logo](https://github.com/user-attachments/assets/69f4f1d9-43ea-454e-b560-f9b245d26767)

[![MIT licensed](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](LICENSE)
[![GitHub code size in bytes](https://img.shields.io/github/repo-size/johnkommas/Wallpaper?style=for-the-badge)](CODE_SIZE)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/johnkommas/Wallpaper?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/johnkommas/Wallpaper?style=for-the-badge)](FORKS)
[![GitHub issues](https://img.shields.io/github/issues/johnkommas/Wallpaper?style=for-the-badge)](ISSUES)
[![GitHub last commit](https://img.shields.io/github/last-commit/johnkommas/Wallpaper?style=for-the-badge)](COMMIT)
[![GitHub language count](https://img.shields.io/github/languages/count/johnkommas/Wallpaper?style=for-the-badge)](LANGUAGES)
[![GitHub top language](https://img.shields.io/github/languages/top/johnkommas/Wallpaper?style=for-the-badge)](lang)
[![Discord](https://img.shields.io/discord/583993547792056321?style=for-the-badge)](https://discord.gg/PJAT7XNshB)

# Wallpaper - Realtime Data Integration from Your ERP

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Quick Start](#quick-start)
- [Setup](#setup)
  - [Folder Structure](#1-folder-structure)
  - [Adding Your Images](#2-adding-your-images)
  - [Create a `.env` File](#3-create-a-env-file)
  - [Setting Rolling Wallpapers](#4-setting-rolling-wallpapers)
- [Example of Output](#example-of-output)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Testing Guidance](#testing-guidance)
- [License](#license)
- [Maintainers](#maintainers)

### Retina-Ready Wallpapers

The wallpaper images in this project are designed for **Retina displays**, ensuring optimal visual quality on high-resolution screens. If you are using a non-Retina display, the images will still work, but you may notice a slight quality difference due to downscaling.

#### Example Devices:
- **MacBooks** (Pro, Air, and Standard) with Retina displays
- **iMacs** with Retina 4K or 5K displays
- External Retina or high-resolution monitors

#### Recommendations:
- Use images with a resolution of **2880x1800** pixels or higher to match the quality of Retina screens.
- If customizing the wallpapers, ensure the images match or exceed these dimensions for the best results.

This repository allows you to integrate real-time data directly from your ERP system into wallpaper images. By following the steps below, you can set up and customize the wallpapers to fit your needs. 

---

## Key Features

- Retina-ready wallpapers optimized for high-definition displays.
- Allows real-time ERP data integration into wallpapers.
- Cross-platform compatibility with Windows and macOS.
- Fully customizable and supports dynamic wallpaper generation.
- Integration with OneDrive for file and folder management.

---

## Overview

This project uses 3 default wallpaper images, which can be replaced with your own. The application processes these input images and generates dynamic wallpapers incorporating real-time ERP data. The output images are saved into a designated folder for immediate use.

---

## Quick Start

To quickly set up and start using this project, follow these steps:

1. Clone the repository and ensure the dependencies are installed.
2. Create the necessary folder structure in your OneDrive directory.
3. Add your input images to the `in/` folder using the naming conventions provided.
4. Create a `.env` file with your specific system and connection details.
5. Follow the instructions to set up rolling wallpapers for Windows or macOS.

---

## Setup

### 1. Folder Structure

You need to create the following folder structure within your OneDrive directory (`{OneDrive}`):

```plaintext
{OneDrive}/Pictures/Wallpaper
    ├── in/
    ├── roll/
    └── in/OFFLINE/
```

- **`in/`**: Contains the input images you want to use as wallpapers.  
- **`roll/`**: Output folder for the processed images with real-time ERP data.  
- **`in/OFFLINE/`**: Subfolder for offline management of wallpaper-related resources.

---

### 2. Adding Your Images

Place your custom wallpaper files in the `in/` folder using the following naming convention:

1. `wallpaper_1.jpg`
2. `wallpaper_2.jpg`
3. `wallpaper_3.jpg`

#### Example of Default Images
Here are examples of the default images (you can replace these with your own):

- ![wallpaper_1](https://github.com/user-attachments/assets/8b1a7205-74c7-4d67-951c-0b69c14afb7c)
- ![wallpaper_2](https://github.com/user-attachments/assets/67ba81de-c246-4e40-8a7d-8bd4a2182c53)
- ![wallpaper_3](https://github.com/user-attachments/assets/0e49d58c-308e-4951-a24c-bf0fa251b3d2)

Simply ensure that your images follow the same naming structure and are saved in the correct location.

---

### 3. Create a `.env` File

For the application to function correctly, you need to create a `.env` file to store essential environment variables. The `.env` file is used to securely configure application settings such as IPs and connection details.

1. **Locate the Root Directory**:  
   Place the `.env` file in the root directory of the project (where the Python scripts are located).

2. **Add the Following Content to the `.env` File**:  

.env Configuration variables are divided into the following groups:

---

**Database Variables:**

- **`SQL_SERVER`**: The IP address or hostname of the SQL Server.
- **`UID`**: The username used for authentication with the SQL Server.
- **`SQL_PWD`**: The password for the specified SQL Server user. Enclose in quotes if it contains special characters.
- **`DATABASE`**: The name of the database being accessed (e.g., your ERP database name).
- **`SQL_COMPANY_CODE`**: The company-specific code used within your SQL database (if multiple companies are used).

---

**VPN/Network Configuration:**

- **`VPN`**: The IP address of the VPN server for remote access.
- **`ROUTER`**: The IP address of the router used in the VPN setup.
- **`VPN_NAME`**: The name of the VPN connection (for identification purposes).
- **`VPN_PWD`**: The password for the VPN connection.

---

**File Paths and System Configuration:**

- **`ONEDRIVE`**: The OneDrive folder path where the application will read/write files (e.g., wallpapers). Make sure the path is correct and accessible from the application.
- **`TSC`**: Indicates whether to use Transport Security (e.g., `yes` or `no`).

---

**Environment IP Configuration:**

- **`IP_EM`**: General-use IP address for the environment.
- **`IP_L1`**: Layer 1 or specific-use IP in the network setup.
- **`IP_L2`**: Layer 2 or specific-use IP in the network setup.
- **`IP_EM_SQL`**: IP address of the SQL server related to the `Elounda Market` setup.
- **`IP_EM_FTP`**: IP address of the FTP server used for file operations.
- **`IP_EM_ROUTER`**: The router's IP address within the Elounda Market setup.

---

Make sure the `.env` file is structured as follows:

# .env File Configuration

To ensure the application operates correctly, you need to configure a `.env` file with the required system and connection details. Below is the list of essential variables you need to include and descriptions of their purpose. Replace placeholder descriptions with your actual values.

---

### **Environment Variables**

- **`SQL_SERVER`**: The IP address or hostname of the SQL Server.
- **`UID`**: The username used for authentication with the SQL Server.
- **`SQL_PWD`**: The password for the specified SQL Server user. Enclose in quotes if it contains special characters.
- **`DATABASE`**: The name of the database being accessed (e.g., your ERP database name).
- **`TSC`**: Indicates whether to use Transport Security (e.g., `yes` or `no`).
- **`VPN`**: The IP address of the VPN server for remote access.
- **`ROUTER`**: The IP address of the router used in the VPN setup.
- **`VPN_NAME`**: The name of the VPN connection (for identification purposes).
- **`VPN_PWD`**: The password for the VPN connection.
- **`SQL_COMPANY_CODE`**: The company-specific code used within your SQL database (if multiple companies are used).

---

### **File Paths**

- **`ONEDRIVE`**: The OneDrive folder path where the application will read/write files (e.g., wallpapers). Make sure the path is correct and accessible from the application.

---

### **IP Configuration**

- **`IP_EM`**: General-use IP address for the environment.
- **`IP_L1`**: Layer 1 or specific-use IP in the network setup.
- **`IP_L2`**: Layer 2 or specific-use IP in the network setup.
- **`IP_EM_SQL`**: IP address of the SQL server related to the `Elounda Market` setup.
- **`IP_EM_FTP`**: IP address of the FTP server used for file operations.
- **`IP_EM_ROUTER`**: The router's IP address within the Elounda Market setup.

---

### **Sample .env File Structure**

Below is how your `.env` file should look (here i use descriptive placeholders instead of sensitive information):

```dotenv
SQL_SERVER=<sql_server_ip_or_hostname>
UID=<sql_username>
SQL_PWD="<sql_password>"
DATABASE=<database_name>
TSC=<yes_or_no>
VPN=<vpn_server_ip>
ROUTER=<router_ip>
VPN_NAME="<vpn_connection_name>"
VPN_PWD=<vpn_password>
SQL_COMPANY_CODE=<company_code>

ONEDRIVE=<your_onedrive_path>

IP_EM=<general_ip>
IP_L1=<layer_1_ip>
IP_L2=<layer_2_ip>
IP_EM_SQL=<sql_server_ip>
IP_EM_FTP=<ftp_server_ip>
IP_EM_ROUTER=<router_ip>
```

---

### **Important Notes**
1. Replace all placeholders (`<...>`) with your actual values required for your system.
2. Do not share your `.env` file publicly, as it contains sensitive information such as IPs, passwords, and database credentials.
3. Ensure that your `.env` file is located in the root directory of the project where your Python scripts are executed.

---


3. **Replace Placeholders**:  
   - Replace `your_database_user`, `your_database_password`, etc., with the correct credentials and connection details required for your ERP system.
   - Ensure that the IP addresses are valid for your setup.

4. **Ensure Security**:  
   - Do **not** share your `.env` file publicly, as it contains sensitive information.

---

### 4.1 Setting 5-Second Rolling Wallpapers on Windows

> **Note:** By default, Windows does not support intervals shorter than 1 minute. Follow these steps to modify the Windows Registry for supporting a 5-second interval.

1. **Open "Settings":**  
   - Right-click on the desktop and select **Personalize**.  
   - In the Background section, choose **Slideshow**.  
   - Select the `roll/` folder (e.g., `{OneDrive}/Pictures/Wallpaper/roll/`) as the picture location.  
   - Set the interval to any value (e.g., 1 minute) as a placeholder for now.  
   - Click **Save**.  

2. **Edit the Registry:**  
   - Press `Win + R`, type **`regedit`**, and press **Enter**.  
   - Navigate to the following key in the Registry Editor:  

     ```plaintext
     HKEY_CURRENT_USER\Control Panel\Personalization\Desktop Slideshow
     ```  
   - Locate the key named **`Interval`**.  
   - Double-click `Interval` and set its value to **5000** (milliseconds for a 5-second interval).  
   - Click **OK** to save the changes.  
---

## Troubleshooting

### SQL Connection Issues
- Ensure that the `SQL_SERVER`, `UID`, and `SQL_PWD` values in your `.env` file are correct.
- Confirm that your database is running and accessible on the specified IP/hostname.
- Use a tool like SSMS or a Python script to test the connection before running the application.

### OneDrive Sync Issues
- Verify that your OneDrive folder is properly configured and synced locally.
- Right-click the folder and select **"Always Keep on This Device"** to avoid offloading.

### Wallpaper Updating Issues
- For Windows:
  - Make sure the rolling wallpapers are added to the correct `roll/` folder.
  - Double-check that the registry values are properly updated for 5-second intervals.
- For macOS:
  - Ensure the folder has been selected in the **Desktop & Screen Saver** settings.
---


### 4.2 Setting Rolling Wallpapers on macOS
   - Locate **Windows Explorer** in the list of processes.  
   - Right-click **Windows Explorer** and select **Restart**.  

4. **Verify the Change:**  
   - Your desktop backgrounds should now change every 5 seconds using the images in the `roll/` folder.  

### 4.2 Setting Rolling Wallpapers on macOS

1. **Open "System Preferences":**  
   - Navigate to **"System Preferences > Desktop & Screen Saver"**.

2. **Select the `roll/` Folder as the Source:**  
   - Click the "+" button to add a folder.
   - Locate and select your `roll/` folder, which should contain the dynamically generated wallpapers.

3. **Enable Wallpaper Slideshow:**  
   - Choose the folder and enable **"Change Picture"** to create a slideshow.
   - Set the change interval to any value (e.g., 5 seconds).

4. **Apply Changes:**  
   - Your desktop wallpapers will now rotate based on the order in the selected folder.

#### Example Output Images
Here is an example of the types of images generated and saved in the `roll/` folder:

- ![wallpaper_1](https://github.com/user-attachments/assets/164c579c-1210-40a4-96cb-e37be4c422df)
- ![wallpaper_2](https://github.com/user-attachments/assets/e013a179-92fb-4a73-a4ea-f061d87f9977)
- ![wallpaper_3](https://github.com/user-attachments/assets/2f4a79ba-a50d-4dc8-adf5-109c5f90cd38)
- ![wallpaper_4](https://github.com/user-attachments/assets/0d99b09d-77e1-4cab-a90c-6782c6e74fa8)

---

### Example of Output

#### Folder Structure Diagram:

```plaintext

{OneDrive}/Pictures/Wallpaper
    ├── in/
    ├── roll/
    └── in/OFFLINE/
```

![Folder Structure Example](https://github.com/user-attachments/assets/example-folder-diagram.png)

---

Here is a short video showcasing the dynamic look and feel of the processed wallpapers:

[![Watch the Video](https://github.com/user-attachments/assets/64ae8612-7972-4f12-8d33-70b6243996ed)](https://github.com/user-attachments/assets/64ae8612-7972-4f12-8d33-70b6243996ed)

---

## Additional Notes

- **Compatibility:** The application works seamlessly with OneDrive for folder management. Ensure OneDrive is active and properly configured to allow folder synchronization.

## Dependencies

This project uses two sets of dependencies: core dependencies (for running the application) and development dependencies (for testing, debugging, and visualization).

### Testing Guidance

#### Verifying SQL Database Connection
Add and run the following Python script:
```python
import pyodbc

connection_str = (
    "DRIVER={SQL Server};"
    "SERVER=your_sql_server;"
    "UID=your_username;"
    "PWD=your_password;"
    "DATABASE=your_database;"
)

try:
    conn = pyodbc.connect(connection_str)
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)
```

#### Verifying OneDrive Path Access
Add and run this script:

```python
import os

one_drive_path = "<your-onedrive-path>"

if os.path.exists(one_drive_path):
    print(f"OneDrive path found: {one_drive_path}")
else:
    print(f"OneDrive path not found: {one_drive_path}")
```

### Installing Core Dependencies:
To install the core dependencies required for running the application, use the following command:
```bash
pip install -r requirements.txt
```

### Installing Development Dependencies:
For development, testing, or additional tools, install the development dependencies using:
```bash
pip install -r requirements-dev.txt
```
- **ERP Systems:** The application integrates with the Entersoft ERP database by default. If you are using a different ERP system, consider modifying the SQL queries in the code to match your requirements.
- **Customization:** You can customize the default wallpapers by replacing the input files in the `in/` folder. Ensure that the file naming follows the conventions outlined above.
- **Photoshop Files:** Editable Photoshop files are included in the `Photoshop` folder. Feel free to open them and make any additional changes for enhanced customization.

---

Enjoy the dynamic customization of your wallpapers, enriched with real-time data from your ERP. For further help or troubleshooting, refer to the included documentation or contact the project's support team.


---

## Maintainers

This project is actively maintained by:

- **John Kommas**  
  - Role: Project Lead  
  - Email: [johnkommas@gmail.com](mailto:johnkommas@gmail.com)

If you’re interested in contributing or would like to collaborate, feel free to reach out!
