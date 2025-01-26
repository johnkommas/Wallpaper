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

### 3. Running the Application

Once your folders and images are correctly set up, run the **`minimalist_main.py`** script included in the project. When executed, the script processes the images in the `in/` folder and generates four new images containing real-time data. These output images will be saved in the `roll/` directory.

#### Example Output Images
Here is an example of the types of images generated and saved in the `roll/` folder:

- ![wallpaper_1](https://github.com/user-attachments/assets/164c579c-1210-40a4-96cb-e37be4c422df)
- ![wallpaper_2](https://github.com/user-attachments/assets/e013a179-92fb-4a73-a4ea-f061d87f9977)
- ![wallpaper_3](https://github.com/user-attachments/assets/2f4a79ba-a50d-4dc8-adf5-109c5f90cd38)
- ![wallpaper_4](https://github.com/user-attachments/assets/0d99b09d-77e1-4cab-a90c-6782c6e74fa8)

---

### 4. Example of Wallpaper Appearance

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