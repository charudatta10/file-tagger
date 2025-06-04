# Frequently Asked Questions for File Tagger

## Installation Issues

### 1. Cannot install dependencies using pip

*   **Solution**: Ensure that you have the latest version of pip installed by running `python -m pip install --upgrade pip` in your terminal.
    *   Example: If you're still facing issues, try upgrading pip by running `python -m pip install --upgrade pip` in your command prompt or terminal.

### 2. Just not found

*   **Solution**: Verify that the `just` executable exists and is accessible in your system's PATH environment variable.
    *   Example: Make sure to add the path of the `just` executable (`C:\Users\korde\Home\Github\file-tagger\bin\just.exe`) to your PATH variable. You can do this by following these steps:
        1.  Right-click on **Computer** or **This PC** and select **Properties**.
        2.  Click on **Advanced system settings** on the left side.
        3.  Click on **Environment Variables**.
        4.  Under **System Variables**, scroll down and find the **Path** variable, then click **Edit**.
        5.  Click **New** and enter the path to the `just` executable (`C:\Users\korde\Home\Github\file-tagger\bin\just.exe`).
        6.  Click **OK** on all windows.

## Configuration Problems

### 1. File tags not being applied correctly

*   **Solution**: Ensure that you have a `.env` file in the project root with the required configuration variables set.
    *   Example: Make sure to add these variables to your `.env` file:

        ```
environment=dev
python_version=3.9
```

### 2. Invalid file paths

*   **Solution**: Double-check that all file paths are correct and valid.

## Usage Questions

### 1. How do I use the `just` command?

*   **Solution**: Use the following command to run the project:
    ```
python main.py
```
    *   Example: You can also use this command to execute specific tasks:

        ```bash
python main.py <task_name>
```

## Troubleshooting Tips

### 1. Error message when running `just`

*   **Solution**: Check the console output for error messages and ensure that you have executed the correct command.
    *   Example: You can use these commands to troubleshoot issues:

        ```bash
python main.py --help
just <task_name> --help
```

### 2. File not found

*   **Solution**: Verify that the file exists in the project root or in one of its subdirectories.
    *   Example: Make sure that you have checked for typos or incorrect directory names.

## Community Resources

*   **GitHub Repository**: [https://github.com/charudatta10/file_tag](https://github.com/charudatta10/file_tag)
*   **Issue Tracker**: [https://github.com/charudatta10/file_tag/issues](https://github.com/charudatta10/file_tag/issues)
*   **Documentation**: [https://github.com/charudatta10/file_tag/blob/main/README.md](https://github.com/charudatta10/file_tag/blob/main/README.md)

Please note that this FAQ document is a general guide and may need to be updated as new issues arise or as the project evolves.