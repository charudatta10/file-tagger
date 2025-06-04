# Getting Started
===============

Welcome to File Tag, a Python-based tool for adding custom tags to files and sorting them by these tags. This guide will walk you through setting up and using the tool.

## Prerequisites and System Requirements
-------------------------------------

### Operating System
File Tag is compatible with Windows, macOS, and Linux operating systems.

### Python Version
This project requires Python 3.7 or later for installation.

### Additional Dependencies
- The `just` command line tool (install using pip: `pip install just`)
- A JSON file parser

## Installation Instructions
-------------------------

1. Clone this repository using Git:
   ```bash
git clone https://github.com/charudatta10/file_tag.git
```

2. Navigate to the cloned repository:
   ```bash
cd file_tag
```

3. Install all required dependencies, including `just`:
   ```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root of the project directory with your API keys.

## Basic Configuration
-------------------

1. Set up your custom tags using the `add_tags.py` script provided within this repository's "tags" folder.
2. To sort and order files based on these tags, run:
   ```bash
python main.py --sort-by-tag
```

3. Use `python main.py --list-tags` to view all available tags.

## Running a Simple Example
---------------------------

1. Create a new file within the project directory named "example.txt".

2. Add some text to this file:
```markdown
This is an example.
```

3. Tag this file with your preferred tag(s):
   ```bash
python main.py add-tag example.txt "example"
```

4. Run `python main.py --sort-by-tag` to view the sorted list of files.

## Where to Go Next
------------------

- Check out the project's [README](README.md) for more information.
- Review the [contribution guidelines](CONTRIBUTING.md).
- Read through the project's documentation in the [doc](doc) folder.
- Explore the [archive](archives.7z) for example projects and tutorials.

For questions, concerns, or suggestions, please reach out to us at:
`charudatta10@gmail.com`
or visit our portfolio website: [https://charudatta10.github.io/Portfolio/](https://charudatta10.github.io/Portfolio/)