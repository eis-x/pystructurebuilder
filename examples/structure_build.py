"""
File: structure_builder.py
Creation Date: 2024-11-28
Last Update: 2024-11-28
Creator: eis-x
Git Repository: https://github.com/eis-x/pystructurebuilder
"""

import os
import sys
import logging

# Add the directory containing the pystructurebuilder module to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    """
    Main function to generate the project structure.
    This function sets up logging, determines the root path and output file path,
    and uses the PyStructureBuilder class to generate the project structure.
    """
    from pystructurebuilder import PyStructureBuilder
    from utils import setup_logging

    # Set up logging
    setup_logging()

    # Determine the root path and output file path
    root_path = os.getcwd()
    output_file_path = os.path.join(root_path, os.path.basename(root_path) + "_structure.txt")

    logging.debug(f"Root path: {root_path}")
    logging.debug(f"Output file path: {output_file_path}")

    # Generate the project structure
    builder = PyStructureBuilder(root_path, output_file_path=output_file_path, open_file=True, display_structure=True)
    builder.generate_structure()

    logging.info(f"Project structure saved to {output_file_path}")

if __name__ == "__main__":
    main()
