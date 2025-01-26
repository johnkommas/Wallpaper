# Wallpaper - Realtime Data from Your ERP

This repository allows you to integrate real-time data directly from your ERP system into wallpaper images. By following the steps below, you can set up and customize the wallpapers for your use. 

---

## Overview

This project initially uses 3 default wallpaper images, which can be replaced with your own. The script processes these to generate additional images based on real-time data, which will output into a designated folder.

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

- **`in/`:** This folder contains the input images you want to use as wallpapers.  
- **`roll/`:** Output folder for the processed images with your real-time data.  
- **`in/OFFLINE/`:** A subfolder for offline management of wallpaper-related resources.

---

### 2. Adding Your Images

Place your custom wallpaper files in the `in/` folder with the following naming convention:

1. `wallpaper_1.jpg`
2. `wallpaper_2.jpg`
3. `wallpaper_3.jpg`

#### Example of Default Images
Here are the sample default images:

- ![wallpaper_1](https://github.com/user-attachments/assets/8b1a7205-74c7-4d67-951c-0b69c14afb7c)
- ![wallpaper_2](https://github.com/user-attachments/assets/67ba81de-c246-4e40-8a7d-8bd4a2182c53)
- ![wallpaper_3](https://github.com/user-attachments/assets/0e49d58c-308e-4951-a24c-bf0fa251b3d2)

You can replace these images with your choices in the same folder structure.

---

### 3. Running the Application

Once your folders and images are in place, run the `minimalist_main.py` script from the project. When executed, the script will process the input images and generate four new images that will appear in the `roll/` directory.

#### Example Output Images
Here are the types of images you can expect in the output folder (`roll/`):

- ![wallpaper_1](https://github.com/user-attachments/assets/164c579c-1210-40a4-96cb-e37be4c422df)
- ![wallpaper_2](https://github.com/user-attachments/assets/e013a179-92fb-4a73-a4ea-f061d87f9977)
- ![wallpaper_3](https://github.com/user-attachments/assets/2f4a79ba-a50d-4dc8-adf5-109c5f90cd38)
- ![wallpaper_4](https://github.com/user-attachments/assets/0d99b09d-77e1-4cab-a90c-6782c6e74fa8)

---

#### Example How Your Wallpaper Look Like
Here is a short Video representing the look and feel of your Wallpaper:



https://github.com/user-attachments/assets/64ae8612-7972-4f12-8d33-70b6243996ed


---

### Additional Notes

- **Compatibility:** Works seamlessly with OneDrive for folder structure. Ensure your OneDrive is properly configured for the folders to sync.
- **ERP:** Wallpaper Returns Data From Entersoft ERP Database consider replacing SQL Queries in case of different ERP System.
- **Customization:** Replace the default wallpapers with your own by naming them appropriately as indicated in the folder structure.
- **Photoshop** Feel Free to Open Files inside Photoshop Folder and Make Your changes there.

---

Enjoy the dynamic customization of your wallpaper experience with real-time ERP data! For any questions or troubleshooting, refer to the included documentation or contact support.
