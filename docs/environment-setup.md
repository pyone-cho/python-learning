# Python Development Environment Setup (macOS)

This guide prepares Visual Studio Code and Python 3 for the Python Learning course. The steps are written for macOS, including Intel-based Mac computers.

## 1. Check whether Python 3 is already installed

Open Terminal and run:

```bash
python3 --version
```

If a Python 3 version appears, Python is available. If not, install a macOS-compatible installer from [python.org/downloads/macos](https://www.python.org/downloads/macos/).

## 2. Install Visual Studio Code

1. Visit [code.visualstudio.com](https://code.visualstudio.com/).
2. Download the macOS build compatible with your Mac's processor (Intel).
3. Move Visual Studio Code into Applications and launch it.

## 3. Install the Python extension

1. Open Extensions in VS Code with `Shift + Command + X`.
2. Search for **Python**.
3. Install **Python**, published by **Microsoft**.
4. Install **Pylance** if recommended.

## 4. Create the learning folder and test file

Open your `python-learning` folder in VS Code. Create `hello.py` and enter:

```python
print("Hello, Python!")
print("My Python environment is ready.")
```

Save with `Command + S`.

## 5. Run the program

Choose **Terminal → New Terminal** in VS Code and run:

```bash
python3 hello.py
```

Expected output:

```text
Hello, Python!
My Python environment is ready.
```

## 6. Select the Python interpreter

If needed, press `Command + Shift + P`, choose **Python: Select Interpreter**, and select the Python 3 interpreter you want to use.

## 7. Git (later)

Check Git with:

```bash
git --version
```

Git configuration and daily Git commands will be covered later.

## Verified setup result

The learner reported these successful checks:

- Python: `Python 3.9.6`
- Git: `git version 2.50.1 (Apple Git-155)`
- `python3 hello.py` successfully printed:
  - `Hello, Python!`
  - `My Python environment is ready.`

**Version note:** Python 3.9 reached end of life in October 2025 and no longer receives upstream security updates. It is sufficient for introductory exercises, but plan to install a supported release such as Python 3.12 or 3.13 before using newer libraries and larger projects.

## Setup checklist

- [x] Python 3 version displays in Terminal.
- [x] VS Code integrated Terminal successfully ran the program.
- [ ] Microsoft Python extension is installed (not yet confirmed).
- [ ] Pylance is installed if recommended (not yet confirmed).
- [x] `hello.py` is created and saved.
- [x] `python3 hello.py` runs successfully.
- [x] Git is available in Terminal.

## Troubleshooting

If something does not work, share the exact command and complete error message. Avoid installing multiple Python versions before checking the issue.
