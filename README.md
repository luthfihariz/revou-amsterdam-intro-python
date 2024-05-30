## Intro to Python
Learning Goal: Students will learn the basics of Python syntax and control flow, understand and utilize core data structures, grasp the principles of object-oriented programming, and apply common design patterns to write efficient and maintainable code.

### Day 1
- What is python
- Basic syntax
- Variable and data type
- Conditionals and iteration
- Type casting
- Exceptions

### Day 2
- Functions, builtin functions
- Lambda functions
- Intro to data structure
- List, tuples, Sets, Dictionaries


### Day 3
- Intro to OOP
- Classes
- Inheritance
- Dunder
- Methods
- Polymorphism


### Day 4
- Design Patterns
- Virtualenv


### Installing Pipenv

Make sure you have python and pip installed in your local
```python --version```
or 
```python3 --version```

Additionally, make sure you have pip available. Check this by running:

```pip --version```

If you installed Python from source, with an installer from python.org or via Homebrew, you likely already have pip. If you’re on Linux and installed using your OS package manager, you may have to install pip manually.

It is recommended that users on most platforms install pipenv from pypi.org using:

```pip install pipenv --user```

If pipenv isn’t available in your shell after installation, you’ll need to add the user site-packages binary directory to your PATH.

On Linux and macOS you can find the user base binary directory by running python -m site --user-base and appending bin to the end. For example, this will typically print ~/.local (with ~ expanded to the absolute path to your home directory), so you’ll need to add ~/.local/bin to your PATH. You can set your PATH permanently by modifying ~/.profile.

On Windows you can find the user base binary directory by running python -m site --user-site and replacing site-packages with Scripts. For example, this could return C:\Users\Username\AppData\Roaming\Python37\site-packages, so you would need to set your PATH to include C:\Users\Username\AppData\Roaming\Python37\Scripts. You can set your user PATH permanently in the Control Panel.

You may need to log out for the PATH changes to take effect.

Make sure it properly installed by running:

```pipenv --version```

Reference: https://pipenv.pypa.io/en/latest/installation.html