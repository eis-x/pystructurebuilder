# PyStructureBuilder

**PyStructureBuilder** is a powerful and flexible tool designed to automatically and systematically generate the structure of projects. Whether you're a developer looking to document your project's structure or an educator wanting to showcase examples of project structures, PyStructureBuilder is the ideal tool for you.

## Features

- **Automatic Structure Generation**: Automatically scan the root directory of your project and generate a text file describing the project's structure.
- **Structure Display**: Display the generated structure directly in the terminal for quick visualization.
- **Unique Output Files**: Generate unique file names to avoid conflicts with existing files.
- **Logging**: Record actions and errors in a log file for easy tracking and debugging.
- **Customization**: Customize output paths and display options according to your needs.

## Installation

### Installation via PyPI

You can install PyStructureBuilder via pip:

```bash
pip install pystructurebuilder
```

### Local Installation

To install PyStructureBuilder locally, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/eis-x/pystructurebuilder.git
```

2. Navigate to the project directory:

```bash
cd pystructurebuilder
```

3. Create a virtual environment to isolate the project's dependencies:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

- On Windows:

```bash
.venv\Scripts\activate
```

- On macOS and Linux:

```bash
source .venv/bin/activate
```

5. Install the module locally with pip:

```bash
pip install .
```

## Usage

Here's an example of how to use PyStructureBuilder in your project:

```python
from pystructurebuilder import PyStructureBuilder

# Define the root path and the output file path
root_path = "/path/to/your/project"
output_file_path = "/path/to/your/project_structure.txt"

# Create an instance of PyStructureBuilder
builder = PyStructureBuilder(root_path, output_file_path=output_file_path, open_file=False, display_structure=True)

# Generate the project structure
builder.generate_structure()
```

## Command Line Execution

You can also run PyStructureBuilder from the command line:

```bash
python -m pystructurebuilder -r /path/to/your/project -o /path/to/your/project_structure.txt -d
```

## Script Arguments

The `pystructurebuilder` script accepts several arguments that allow you to customize its behavior. Here are the details:

### `-r` or `--root-path`

- **Description**: Specifies the root directory path to scan for generating the project structure.
- **Initial State**: The current working directory (`os.getcwd()`).
- **Functionality**: This argument sets the root path from which the script will start scanning and generating the project structure.

### `-o` or `--output-file-path`

- **Description**: Specifies the path to the output file where the generated project structure will be saved.
- **Initial State**: A file named `<root-directory-name>_structure.txt` in the root directory.
- **Functionality**: This argument sets the path to the output file where the generated structure will be written. If not provided, the script will create a default output file in the root directory.

### `--version`

- **Description**: Displays the version number of the script and exits.
- **Initial State**: Not applicable.
- **Functionality**: When this argument is provided, the script will print the version number and exit without performing any other actions.

### `--no-open`

- **Description**: Prevents the script from opening the output file in the default program after generating the structure.
- **Initial State**: `False` (the output file will be opened by default).
- **Functionality**: When this argument is provided, the script will not open the output file after generating the structure.

### `-d` or `--display-structure`

- **Description**: Displays the generated project structure in the terminal.
- **Initial State**: `False` (the structure will not be displayed by default).
- **Functionality**: When this argument is provided, the script will print the generated project structure to the terminal.

## Log File

PyStructureBuilder records actions and errors in a log file for easy tracking and debugging. The log file is created in the user's home directory. The default log file name is `pystructurebuilder.log`.

### Log File Location

Based on the code provided in `logger.py`, the log file will be located at:

- **Windows**: `C:\Users\<Username>\AppData\Roaming\.pystructurebuilder\logs\pystructurebuilder.log`
- **macOS**: `/Users/<Username>/.pystructurebuilder/logs/pystructurebuilder.log`
- **Linux**: `/home/<Username>/.pystructurebuilder/logs/pystructurebuilder.log`

### Log File Contents

The log file contains detailed information about the execution of the module, including:

- Timestamps of actions performed.
- Information about the directories and files scanned.
- Any errors or exceptions encountered during execution.

If you encounter any issues or anomalies while running the module, you can check the log file for more information. This can help you diagnose and resolve any problems.

## Tests

To run the tests, follow these steps:

1. Ensure you have cloned the repository and are in the project directory.
2. Create and activate a virtual environment (see instructions above).
3. Run the tests with `unittest`:

```bash
python -m unittest discover tests
```

## Examples

You can find examples of how to use PyStructureBuilder in the `examples` directory. Here's how to run an example:

```bash
python examples/structure_build.py
```

## Example of Generated Project Structure

Here's an example of a project structure generated by PyStructureBuilder:

<pre>
    <code class="language-plaintext">
pystructurebuilder/
&#9500;&#9472;&#9472; examples/
&#9474;   &#9492;&#9472;&#9472; structure_build.py
&#9500;&#9472;&#9472; pystructurebuilder/
&#9474;   &#9500;&#9472;&#9472; __init__.py
&#9474;   &#9500;&#9472;&#9472; pystructurebuilder.py
&#9474;   &#9492;&#9472;&#9472; utils.py
&#9500;&#9472;&#9472; tests/
&#9474;   &#9500;&#9472;&#9472; __init__.py
&#9474;   &#9500;&#9472;&#9472; test_pystructurebuilder.py
&#9474;   &#9492;&#9472;&#9472; test_structure.py
&#9500;&#9472;&#9472; utils/
&#9474;   &#9500;&#9472;&#9472; __init__.py
&#9474;   &#9500;&#9472;&#9472; logger.py
&#9474;   &#9500;&#9472;&#9472; structure.py
&#9474;   &#9492;&#9472;&#9472; utils.py
&#9500;&#9472;&#9472; .gitignore
&#9500;&#9472;&#9472; LICENSE
&#9500;&#9472;&#9472; pyproject.toml
&#9500;&#9472;&#9472; README.md
&#9492;&#9472;&#9472; setup.cfg
    </code>
</pre>

This example shows a typical Python project structure with directories for examples (`examples/`), the main project code (`pystructurebuilder/`), tests (`tests/`), and utilities (`utils/`). Each directory contains relevant files, such as `__init__.py` for package initialization, `pystructurebuilder.py` for the main script, and various utility modules. The directories and files are listed in alphabetical order within their respective levels.

## Contributions

Contributions are welcome! If you would like to contribute to PyStructureBuilder, please follow these steps:

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -am 'Add my feature'`).
4. Push your branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue on GitHub or contact me directly at [eis-x@hotmail.com](mailto:eis-x@hotmail.com).