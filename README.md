Photo Capture App with Kivy

This Python application is a simple photo capture app using the Kivy framework. It allows users to capture photos using the device's camera and provides a user interface for camera control.
Requirements

    Python 3.x
    Kivy

Installation

    Install the required dependencies:

    bash

pip install kivy

Run the application:

bash

    python main.py

Usage

    Upon launching the app, the main screen will appear with the camera preview.

    If running on an Android device, the app will request camera and storage permissions.

    The app provides the following features:

        Capture Photo: Press the camera icon button to capture a photo.

        Toggle Camera: Press the camera flip icon button to switch between front and rear cameras.

        Toggle Flash: Press the flash icon button to toggle the flash mode (on, off, auto).

Code Structure
main.py

This script initializes the Kivy application and sets up the screen manager. It also handles Android-specific permissions.
photoscreen1.py

Contains the PhotoScreen1 class, which represents the main screen of the app. It uses the Preview class from camera4kivy for camera preview and includes a ButtonsLayout1 for control buttons.
photolayout1.py

Defines the layout for the main screen, including the camera preview, background, and control buttons.
toast.py

Includes a Toast class that displays a short-lived popup notification. On Android, it uses native Android Toast messages; on other platforms, it uses a Kivy Popup for a similar effect.
Platform-Specific Implementations
android.py

Contains Android-specific code for displaying Toast messages using the Android API.
Notes

    The app is designed to run on both Android and other platforms, with platform-specific code separated for clarity.

    The camera permissions are requested on Android to ensure proper functionality.

    The layout is responsive, adapting to changes in window size.