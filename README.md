# Wybthon VLC Video Player

This is a basic video-player application built using wxPython and VLC. The app allows you to play videos from a specified URL, with the option to play or pause the video.

## Project Structure

```plaintext
wybthon-vlc/
├── main.py
└── requirements.txt
```

- **main.py**: The main application file that contains the implementation of the video player.
- **requirements.txt**: A list of dependencies required to run the application.

## Prerequisites

- Python 3.x
- wxPython
- python-vlc

You can install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Run the application with the following command:

```bash
python main.py
```

The application will open a window with a text field to input a video URL and a play/pause button. By default, it will load a sample video (`Big Buck Bunny`).

## Supported Platforms

- Linux
- Windows
- macOS

The appropriate display method is automatically selected based on your platform.
