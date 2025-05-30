

# Wallpaper - Realtime Data Integration from Your ERP

![logo](https://github.com/user-attachments/assets/69f4f1d9-43ea-454e-b560-f9b245d26767)

[![MIT licensed](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=for-the-badge)](LICENSE)
[![GitHub code size in bytes](https://img.shields.io/github/repo-size/johnkommas/Wallpaper?style=for-the-badge)](https://github.com/johnkommas/Wallpaper)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/johnkommas/Wallpaper?style=for-the-badge)
[![GitHub last commit](https://img.shields.io/github/last-commit/johnkommas/Wallpaper?style=for-the-badge)](COMMIT)
[![GitHub language count](https://img.shields.io/github/languages/count/johnkommas/Wallpaper?style=for-the-badge)](LANGUAGES)
[![GitHub top language](https://img.shields.io/github/languages/top/johnkommas/Wallpaper?style=for-the-badge)](lang)
[![Discord](https://img.shields.io/discord/583993547792056321?style=for-the-badge)](https://discord.gg/PJAT7XNshB)

## 📚 Table of Contents
- [Overview](#-overview)
- [Demo Video](#-demo-video)
- [Business Impact](#-business-impact)
- [Quick Start](#-quick-start)
- [Key Features](#-key-features)
- [Setting Up Rolling Wallpapers](#-setting-up-rolling-wallpapers)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)
- [Maintainers](#-maintainers)
- [Contributing](#-contributing)

---

## 📌 Overview

**Wallpaper** transforms how businesses visualize real-time data by integrating insights from **Entersoft ERP** into dynamic, high-quality wallpapers. This tool is perfect for **Marketing, HR, Payroll, Sales, and Management teams**, ensuring key metrics are **always visible** without requiring logins or extra dashboards.

### **Why Use Wallpaper?**
✅ **Instant Insights** – See critical KPIs directly on your desktop wallpaper.  
✅ **Automated Updates** – Data refreshes every X minutes without user intervention.  
✅ **Department-Specific Views** – Each team gets its own customized metrics.  
✅ **OneDrive Integration** – Seamless syncing across devices for real-time updates.  
✅ **Zero Extra ERP Licenses** – No need for additional user access in Entersoft ERP.

---


📺 Demo With more than 10 DataSet

![2E13F2D1-9165-45DE-AAB6-C4D87B30C62E_1_105_c](https://github.com/user-attachments/assets/4cabed69-1cde-41d1-a588-09d7dfd62bbd)

![IMG_2453](https://github.com/user-attachments/assets/abfe9f26-d6ac-462c-bb93-77e894ae7782)

## 🛠️ Tool Kit Color Pallete Examples
![1](https://github.com/user-attachments/assets/3b18ab72-562f-46ea-8a67-d643b52374d4)
![2](https://github.com/user-attachments/assets/3d30a5de-05a2-404a-b6cc-1ba34bcc9d83)
![3](https://github.com/user-attachments/assets/e7276208-c7b4-4bc6-8495-a1df478b395b)


---

## 📈 Business Impact

Implementing the Wallpaper solution can lead to significant improvements in your organization:

- **Enhanced Productivity**: By providing instant access to key metrics directly on desktops, employees can make informed decisions faster, reducing time spent searching for information.
  
- **Improved Decision-Making**: With real-time insights readily available, teams can respond quickly to changes in data, leading to more agile and effective decision-making processes.
  
- **Increased Employee Engagement**: Customizable wallpapers that reflect departmental goals foster a sense of ownership and accountability among team members.

- **Cost Efficiency**: Reduces reliance on expensive BI tools and minimizes manual reporting efforts, saving both time and resources.

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
**Note**: Don’t commit your .env to version control for security reasons.

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

---

## 👥 Maintainers

**John Kommas**  
📧 [johnkommas@gmail.com](mailto:johnkommas@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/ioannis-e-kommas-6a8004a6/)  

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request or open an Issue to discuss improvements or report bugs.

---
💡 **Like this project?** ⭐ Star it on GitHub and spread the word!

