

# Wallpaper - Realtime Data Integration from Your ERP

![logo](https://github.com/user-attachments/assets/69f4f1d9-43ea-454e-b560-f9b245d26767)

[![MIT licensed](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](LICENSE)
[![GitHub code size in bytes](https://img.shields.io/github/repo-size/johnkommas/Wallpaper?style=for-the-badge)](CODE_SIZE)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/johnkommas/Wallpaper?style=for-the-badge)
[![GitHub last commit](https://img.shields.io/github/last-commit/johnkommas/Wallpaper?style=for-the-badge)](COMMIT)
[![GitHub language count](https://img.shields.io/github/languages/count/johnkommas/Wallpaper?style=for-the-badge)](LANGUAGES)
[![GitHub top language](https://img.shields.io/github/languages/top/johnkommas/Wallpaper?style=for-the-badge)](lang)
[![Discord](https://img.shields.io/discord/583993547792056321?style=for-the-badge)](https://discord.gg/PJAT7XNshB)

## 📌 Overview

**Wallpaper** transforms how businesses visualize real-time data by integrating insights from **Entersoft ERP** into dynamic, high-quality wallpapers. This tool is perfect for **Marketing, HR, Payroll, Sales, and Management teams**, ensuring key metrics are **always visible** without requiring logins or extra dashboards.

### **Why Use Wallpaper?**
✅ **Instant Insights** – See critical KPIs directly on your desktop wallpaper.  
✅ **Automated Updates** – Data refreshes every X minutes without user intervention.  
✅ **Department-Specific Views** – Each team gets its own customized metrics.  
✅ **OneDrive Integration** – Seamless syncing across devices for real-time updates.  
✅ **Zero Extra ERP Licenses** – No need for additional user access in Entersoft ERP.

---

## 🚀 Quick Start

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Environment
Create a `.env` file in the project root and add:
```ini
SQL_SERVER=your_sql_server
UID=your_username
SQL_PWD=your_password
DATABASE=your_database
ONEDRIVE=your_onedrive_path
```

### 3️⃣ Setup Folder Structure
Ensure you have the following folders in **OneDrive**:
```plaintext
{OneDrive}/Pictures/Wallpaper
    ├── in/          # Input images folder
    ├── roll/        # Processed wallpaper folder
    ├── in/OFFLINE/  # Backup folder for old wallpapers
```

### 4️⃣ Run the Application
```bash
python wallpaper_generator.py
```

🎉 **That’s it! Your dynamic wallpaper is now active.**

---

## 🎨 Key Features

### ✅ **Real-Time KPI Display**
Turn any wallpaper into a **live dashboard** by embedding real-time data updates directly into the image.

### 📊 **Dynamic Refresh (Custom Intervals)**
Choose between **1, 5, 10, or 60-minute refresh intervals** depending on your business needs.

### 🎯 **Multi-Department Support**
- **Marketing** – Track campaign performance & engagement.
- **Sales** – Monitor revenue growth & sales trends.
- **HR** – View employee engagement metrics & hiring status.
- **Finance** – Stay updated on financial health & key figures.

### 🔗 **Cloud-Based Syncing**
Using **OneDrive**, all updates are stored and synced automatically for seamless integration across teams and locations.

---

## 🖥️ Setting Up Rolling Wallpapers

### **Windows Setup (5-Second Interval)**
Windows doesn’t support intervals under 1 minute by default, so modify the **Registry**:
1. Open `regedit` and navigate to:
   ```plaintext
   HKEY_CURRENT_USER\Control Panel\Personalization\Desktop Slideshow
   ```
2. Locate `Interval`, double-click, and set the value to **5000** (milliseconds).
3. Restart your system.

### **MacOS Setup**
1. Open **System Preferences > Desktop & Screen Saver**.
2. Select your `roll/` folder as the wallpaper source.
3. Enable "Change Picture Every" and select **5 seconds**.

---

## 🛠️ Troubleshooting

### 🔴 **Wallpaper Not Updating?**
✔ Ensure **OneDrive** is fully synced.  
✔ Check if your `.env` file has the correct paths.  
✔ Verify that images are being generated in the `roll/` folder.

### ⚠️ **SQL Connection Issues?**
Test manually using:
```python
import pyodbc
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=your_sql_server;UID=your_username;PWD=your_password;DATABASE=your_database")
print("Connected Successfully!")
```

---

## 📜 License
This project is **MIT Licensed** – free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

## 👥 Maintainers

**John Kommas**  
📧 [johnkommas@gmail.com](mailto:johnkommas@gmail.com)  
💼 [LinkedIn](https://linkedin.com/in/johnkommas)  

---

💡 **Like this project?** ⭐ Star it on GitHub and spread the word!

