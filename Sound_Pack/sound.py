#  Copyright (c) Ioannis E. Kommas 2025. All Rights Reserved
import pygame
import os


class SoundManager:
    _instance = None  # Στατική μεταβλητή για την ενιαία instance

    def __new__(cls, *args, **kwargs):
        """
        Creates and returns a singleton instance of the class. The method guarantees that only one instance
        of the class is created during the application's lifecycle. If an instance already exists, the
        existing one is returned. Additionally, initializes the `pygame.mixer` library once for audio
        management.

        :param cls: The class for which the singleton instance is to be created.
        :param args: Positional arguments passed to the class constructor, if applicable.
        :param kwargs: Keyword arguments passed to the class constructor, if applicable.

        :return: A singleton instance of the class.
        :rtype: SoundManager
        """
        if not cls._instance:
            # Αν δεν υπάρχει instance, δημιουργούμε μία
            cls._instance = super(SoundManager, cls).__new__(cls, *args, **kwargs)
            pygame.mixer.init()  # Αρχικοποίησε το mixer μόνο μία φορά
        return cls._instance

    def play_sound(self, file_path):
        """
        Plays a sound file from the given file path if the file exists. The function uses the
        pygame library to load and play the sound. If the file does not exist, a message is
        printed to notify the user. The playback runs until the sound effect is completed,
        avoiding resource-intensive continuous loops.

        :param file_path: Path to the audio file to be played.
        :type file_path: str
        :return: None
        """
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
        """
        Quits the currently running Pygame mixer.

        The method terminates the Pygame mixer module.
        This should be called when the mixer is no longer needed,
        typically to free up audio-related resources.

        :return: None
        """
        pygame.mixer.quit()


# Δημιουργία αντικειμένου για τη διαχείριση των ήχων
sound_manager = SoundManager()


def run():
    """
    Executes the main run logic for playing a sound.

    This function plays a sound file located in the Sound_Pack directory, using
    the `sound_manager` module's `play_sound` method. It constructs the proper
    path to the sound file by concatenating the current working directory with
    the relative path to the target sound file. It is assumed that the
    `sound_manager` module is already imported and contains a `play_sound`
    function that handles the playback.

    :raises FileNotFoundError: Raised if the sound file is not found in the
        specified path.
    :raises OSError: Raised if there is an issue accessing the file or playing
        the sound.
    """
    SOUND = f"{os.getcwd()}/Sound_Pack/c.mp3"
    sound_manager.play_sound(SOUND)


def done():
    """
    Plays a predefined sound file.

    This function retrieves the absolute path of a sound file located under
    "Sound_Pack" in the current working directory and plays it using the
    `sound_manager.play_sound` method.

    :return: None
    """
    SOUND = f"{os.getcwd()}/Sound_Pack/b.mp3"
    sound_manager.play_sound(SOUND)


def error():
    """
    Plays an error sound from a specific file path.

    The function identifies the path of the error sound file using the current
    working directory and plays it using the sound manager. This provides
    auditory feedback to notify the user of an error condition.

    :return: None
    """
    SOUND = f"{os.getcwd()}/Sound_Pack/c.mp3"
    sound_manager.play_sound(SOUND)


def get_notified():
    """
    Plays a notification sound using the sound_manager module. This function retrieves
    the current working directory, constructs the path to the notification sound file,
    and invokes the `play_sound` function of the `sound_manager`.

    :return: None
    """
    SOUND = f"{os.getcwd()}/Sound_Pack/attention.mp3"
    sound_manager.play_sound(SOUND)


def exit():
    """
    Exit the application and quit the sound manager.

    This function is responsible for terminating the application by
    cleanly shutting down the sound manager. It ensures all resources
    used by the sound manager are released properly.

    :return: None
    :rtype: None
    """
    sound_manager.quit()
