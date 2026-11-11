# Python Development Environment Setup (macOS)

This guide prepares Visual Studio Code and Python 3 for the Python Learning course. The steps are written for macOS, including Intel-based Mac computers.

## 1. Check whether Python 3 is already installed

1. Open **Terminal**. You can use Spotlight Search with `Command + Space`, type `Terminal`, and press Enter.
2. Run:

```bash
python3 --version
```

If the terminal prints a Python 3 version (for example, `Python 3.x.x`), Python 3 is available. Continue to the VS Code setup.

If the command is not found, install Python 3 from the official Python website:

- Visit [python.org/downloads/macos](https://www.python.org/downloads/macos/).
- Download the macOS installer that supports your Mac.
- Open the downloaded `.pkg` file and follow the installer steps.
- Close and reopen Terminal, then check again:

```bash
python3 --version
```

Use the `python3` command on macOS for this course.

## 2. Install Visual Studio Code

1. Visit [code.visualstudio.com](https://code.visualstudio.com/).
2. Download Visual Studio Code for macOS.
3. Choose the build compatible with your Mac's processor (Intel or Apple silicon).
4. Open the downloaded file and move Visual Studio Code into **Applications**.
5. Launch Visual Studio Code.

## 3. Install the Python extension

1. In VS Code, open **Extensions** from the left sidebar, or press `Shift + Command + X`.
2. Search for **Python**.
3. Install **Python**, published by **Microsoft**.
4. If VS Code recommends installing **Pylance**, install it too. It provides Python language support such as code completion and error hints.

## 4. Create or open the learning folder

In VS Code:

1. Select **File → Open Folder**.
2. Create or select your `python-learning` folder.
3. Create a file named `hello.py` inside it.

Enter this first test program:

```python
print("Hello, Python!")
print("My Python environment is ready.")
```

Save the file with `Command + S`.

## 5. Run Python from the VS Code Terminal

1. In VS Code, select **Terminal → New Terminal**.
2. Make sure the terminal is in the folder containing `hello.py`.
3. Run:

```bash
python3 hello.py
```

Expected output:

```text
Hello, Python!
My Python environment is ready.
```

You can also use the Run button provided by the Python extension. For this course, learn to run programs from the terminal as well.

## 6. Select the Python interpreter in VS Code

If VS Code asks you to select an interpreter:

1. Press `Command + Shift + P` to open the Command Palette.
2. Search for **Python: Select Interpreter**.
3. Select the installed Python 3 interpreter.

If more than one interpreter appears, choose the Python 3 installation you intend to use for this course.

## 7. Git (later)

Git is used to track code changes and work with the GitHub repository. It is part of the learning environment, but Git configuration and daily Git commands will be covered later in the course.

You can check whether Git is already available:

```bash
git --version
```

Do not worry if you have not configured Git yet.

## Setup checklist

- [ ] Python 3 version displays in Terminal.
- [ ] Visual Studio Code is installed and opens.
- [ ] Microsoft Python extension is installed.
- [ ] Pylance is installed if recommended.
- [ ] `hello.py` is created and saved.
- [ ] `python3 hello.py` runs successfully in the VS Code Terminal.
- [ ] Git setup can wait until a later lesson.

## If something does not work

Copy the exact command you ran and the complete error message from Terminal, and share it for troubleshooting. Do not guess at commands or install multiple Python versions to fix an error before checking it.
