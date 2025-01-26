
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

This repository allows you to integrate real-time data directly from your ERP system into wallpaper images. By following the steps below, you can set up and customize the wallpapers to fit your needs. 

---

## Overview

This project uses 3 default wallpaper images, which can be replaced with your own. The application processes these input images and generates dynamic wallpapers incorporating real-time ERP data. The output images are saved into a designated folder for immediate use.

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

### 4. Running the Application

Once your folders, images, and `.env` settings are correctly configured, run the **`minimalist_main.py`** script included in the project. When executed, the script processes the images in the `in/` folder and generates four new images containing real-time data. These output images will be saved in the `roll/` directory.

#### Example Output Images
Here is an example of the types of images generated and saved in the `roll/` folder:

- ![wallpaper_1](https://github.com/user-attachments/assets/164c579c-1210-40a4-96cb-e37be4c422df)
- ![wallpaper_2](https://github.com/user-attachments/assets/e013a179-92fb-4a73-a4ea-f061d87f9977)
- ![wallpaper_3](https://github.com/user-attachments/assets/2f4a79ba-a50d-4dc8-adf5-109c5f90cd38)
- ![wallpaper_4](https://github.com/user-attachments/assets/0d99b09d-77e1-4cab-a90c-6782c6e74fa8)

---

### 5. Example of Wallpaper Appearance

Here is a short video showcasing the dynamic look and feel of the processed wallpapers:

[![Watch the Video](https://github.com/user-attachments/assets/64ae8612-7972-4f12-8d33-70b6243996ed)](https://github.com/user-attachments/assets/64ae8612-7972-4f12-8d33-70b6243996ed)

---

## Additional Notes

- **Compatibility:** The application works seamlessly with OneDrive for folder management. Ensure OneDrive is active and properly configured to allow folder synchronization.
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
