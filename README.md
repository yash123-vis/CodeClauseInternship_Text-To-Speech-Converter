# Text-to-Speech Converter

This Text-to-Speech (TTS) converter application is built using Python, featuring a user-friendly interface with Tkinter. It allows users to convert text into speech using the Google Text-to-Speech API. The app includes options to select different voices and adjust speech rates.

## Features

- **Text-to-Speech Conversion:** Converts the entered text into spoken words using Google Text-to-Speech.
- **Voice Selection:** Choose from various English voices (US, UK, Australian, Canadian, Indian).
- **Speech Rate Adjustment:** Adjust the rate of speech from slow to fast.
- **User Interface:** Designed with Tkinter for a clean and simple graphical interface.
- **Dark Blue Theme:** Stylish dark blue background with white and light gray text.

## Prerequisites

Ensure you have Python 3.x installed. You will also need the following Python packages:

- `gtts` (Google Text-to-Speech)
- `pygame` (for audio playback)
- `tkinter` (usually included with Python)

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/Convert-Text-to-Speech-in-Python.git
   cd Convert-Text-to-Speech-in-Python
2. **Install Required Packages:**

   pip install gtts pygame
3. **Run the Application:**

   python Text-to-Speech.py

**Usage**
Enter Text: Type the text you want to convert to speech in the text entry field.
Select Voice: Choose the desired voice from the dropdown menu.
Adjust Speech Rate: Use the slider to set the speech rate (slow to fast).
Play: Click the "PLAY" button to convert the text to speech and play the audio.
Reset: Click the "RESET" button to clear the text entry field and stop the audio if playing.
Exit: Click the "EXIT" button to close the application.

**Screenshot**
<img width="448" alt="image" src="https://github.com/user-attachments/assets/ec7a1391-bf6e-4146-829f-3f8c6245c0f7">

**Contributing**
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open issues or submit pull requests.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgments**
The application uses the gtts library for converting text to speech.
pygame is used for audio playback.
Tkinter is utilized for creating the graphical user interface.


