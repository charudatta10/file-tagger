# File Tagger Technical Reference Document

## Table of Contents

1. [API Documentation](#api-documentation)
2. [Configuration Options](#configuration-options)
3. [Command-Line Interface Reference](#command-line-interface-reference)
4. [File Formats and Data Structures](#file-formats-and-data-structures)
5. [Architectural Overview](#architectural-overview)

## API Documentation

The File Tagger project uses a simple API to add, manage, and sort files by tags. The API is built using the following endpoints:

### Add Tag

*   **Endpoint:** `POST /api/tags`
*   **Request Body:**
    *   `tag`: The name of the tag.
    *   `description`: An optional description for the tag.
*   **Response:**
    *   `id`: The ID of the newly created tag.
    *   `name`: The name of the tag.
    *   `description`: The description of the tag.

### Add File Tag

*   **Endpoint:** `POST /api/files/{fileId}/tags`
*   **Request Body:**
    *   `tagIds`: A list of IDs for the tags to be added.
*   **Response:**
    *   `message`: A success message indicating that the file has been tagged.

### Get File Tags

*   **Endpoint:** `GET /api/files/{fileId}/tags`
*   **Query Parameters:**
    *   `sort`: An optional parameter to sort the tags by name.
    *   `order`: An optional parameter to order the tags in ascending or descending order.

### Example Request
```bash
curl -X POST \
  https://example.com/api/files/123/tags \
  -H 'Content-Type: application/json' \
  -d '{"tagIds": [1, 2, 3]}'
```

## Configuration Options

The File Tagger project can be configured using the following options:

*   **`file_tags.json`**: The file containing the list of tags.
*   **`pyproject.toml`**: The Python project configuration file.

### `file_tags.json`
```json
[
    {"id": 1, "name": "tag1", "description": "This is tag1"},
    {"id": 2, "name": "tag2", "description": "This is tag2"}
]
```

### `pyproject.toml`
```toml
[tool.pyproject.toml]
python-version = '3.9'
```

## Command-Line Interface Reference

The File Tagger project can be run using the following command:

*   **`just`**: Run the file tagger using the `just` command.
*   **`-t` or `--tag`**: Add a tag to a file.
*   **`-f` or `--file`**: Specify the ID of the file to be tagged.
*   **`-v` or `--verbose`**: Enable verbose mode.

### Example Command
```bash
just -t my_tag -f 123
```

## File Formats and Data Structures

The File Tagger project uses the following file formats and data structures:

*   **`.env`**: Environment variables.
*   **`.gitattribute`**: Git attributes.
*   **`.gitattributes`**: Git attribute mappings.
*   **`.gitignore`**: Git ignore patterns.
*   **`.log`**: Log files.
*   **`.pre-commit-config.yaml`**: Pre-commit configuration.
*   **`.python-version`**: Python version information.

### Example Data Structure
```json
{
    "tags": [
        {"id": 1, "name": "tag1", "description": "This is tag1"},
        {"id": 2, "name": "tag2", "description": "This is tag2"}
    ]
}
```

## Architectural Overview

The File Tagger project uses the following architectural components:

*   **API**: A RESTful API for adding, managing, and sorting files by tags.
*   **Database**: A lightweight database to store tag information.
*   **Python Script**: A Python script to handle file tagging and sorting.

### Component Interaction Diagram
```mermaid
graph LR
    API -->|Add Tag| Database
    API -->|Get Tags| Database
    File -->|Tagged with| API
    API -->|File Tagger| Python Script
```

This technical reference document provides comprehensive information about the File Tagger project, including API documentation, configuration options, command-line interface references, file formats and data structures, and architectural overview.