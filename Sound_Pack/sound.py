#  Copyright (c) Ioannis E. Kommas 2025. All Rights Reserved
import pygame
import os


class SoundManager:
    _instance = None  # Στατική μεταβλητή για την ενιαία instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Αν δεν υπάρχει instance, δημιουργούμε μία
            cls._instance = super(SoundManager, cls).__new__(cls, *args, **kwargs)
            pygame.mixer.init()  # Αρχικοποίησε το mixer μόνο μία φορά
        return cls._instance

    def play_sound(self, file_path):
        if not os.path.exists(file_path):  # Έλεγχος αν το αρχείο υπάρχει
            print(f"Το αρχείο {file_path} δεν βρέθηκε.")
            return
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(
                    10
                )  # Αποφυγή συνεχούς loop, χρησιμοποιούμε sleep
        except pygame.error as e:
            print(f"Σφάλμα κατά την αναπαραγωγή ήχου: {e}")

    def quit(self):
        pygame.mixer.quit()



# Δημιουργία αντικειμένου για τη διαχείριση των ήχων
sound_manager = SoundManager()


def run():
    SOUND = f"{os.getcwd()}/Sound_Pack/c.mp3"
    sound_manager.play_sound(SOUND)


def done():
    SOUND = f"{os.getcwd()}/Sound_Pack/b.mp3"
    sound_manager.play_sound(SOUND)


def error():
    SOUND = f"{os.getcwd()}/Sound_Pack/error.mp3"
    sound_manager.play_sound(SOUND)


def exit():
    sound_manager.quit()