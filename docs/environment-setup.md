# Python Development Environment Setup (macOS)

This guide prepares Visual Studio Code and Python 3 for the Python Learning course. The steps are written for macOS, including Intel-based Mac computers.

## 1. Check Python

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

## Verified setup results

The learner first verified:

- Python 3.9.6 was installed.
- Git: `git version 2.50.1 (Apple Git-155)`.
- `python3 hello.py` printed the expected two lines.

The learner then upgraded Python and reported:

- `python3.14 --version` → `Python 3.14.10`
- `python3 --version` → `Python 3.14.10`
- `which -a python3` listed these paths in resolution order:
  1. `/Users/kpc/Ai/projects/kpc/python-learning/.venv/bin/python3`
  2. `/usr/local/bin/python3`
  3. `/usr/bin/python3`

The learner activated the project virtual environment and confirmed:

- `python --version` → `Python 3.14.10`
- `sys.executable` → `/Users/kpc/Ai/projects/kpc/python-learning/.venv/bin/python`

The learner then ran `python hello.py` using the active virtual environment and confirmed the output:

```text
Hello, Python!
My Python environment is ready.
```

This confirms that the active interpreter and test program both work. Keep using this environment for the course.

## 8. Activate the project virtual environment

From the `python-learning` project directory, activate the environment when opening a new terminal:

```bash
source .venv/bin/activate
```

When active, the terminal prompt usually shows `(.venv)`. Check:

```bash
python --version
python -c "import sys; print(sys.executable)"
```

To leave the virtual environment:

```bash
deactivate
```

Do not delete the old system Python at `/usr/bin/python3`; macOS may rely on its own tools.

## Setup checklist

- [x] Python 3.14.10 is available through `python3.14`.
- [x] `python3` reports Python 3.14.10 in the learner's terminal.
- [x] Project `.venv/bin/python3` appears first in `which -a python3`.
- [x] Active virtual environment reports Python 3.14.10.
- [x] Active interpreter path points inside the project `.venv`.
- [x] Git is available (version 2.50.1).
- [x] `hello.py` ran successfully before the Python upgrade.
- [x] `hello.py` ran successfully with the active Python 3.14 virtual environment.
- [ ] Microsoft Python extension is installed (not yet confirmed).
- [ ] Pylance is installed if recommended (not yet confirmed).

## Troubleshooting

If something does not work, share the exact command and complete error message. Avoid deleting macOS's system Python or changing symlinks manually.
