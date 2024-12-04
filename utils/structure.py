import os
import logging
import re

class Structure:
    def __init__(self, root_path: str, display_structure: bool=False) -> None:
        self.root_path = os.path.abspath(root_path)
        self.display_structure = display_structure
        self.structure = ""

    def generate_structure(self, output_file_path: str) -> None:
        output_file_path = os.path.abspath(output_file_path)
        try:
            generating_structure_message = f"Generating structure for the root path: '{self.root_path}'..."
            print(generating_structure_message)
            logging.debug(generating_structure_message)
            root_path_name = os.path.basename(self.root_path)
            self.structure = self._build_structure(self.root_path, prefix="")
            self.structure = f"{root_path_name}/\n{self.structure}"
            
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(self.structure)
            save_message = f"Project structure of '{root_path_name}' has been saved to '{output_file_path}'."
            logging.info(save_message)
            print(save_message)
            end_message = "Structure generation process completed."
            logging.info(end_message)
            print(end_message)
        except Exception as e:
            error_message = f"An error occurred while generating the structure of '{root_path_name}': {str(e)}"
            logging.error(error_message)
            print(f"An error occurred: {str(e)}")
            if os.path.exists(output_file_path):
                os.remove(output_file_path)

    def _build_structure(self, current_path, prefix="") -> str:
        structure = ""
        try:
            logging.debug(f"Building structure for the path: {current_path}")
            items = os.listdir(current_path)
            files = [item for item in items if os.path.isfile(os.path.join(current_path, item))]
            dirs = [item for item in items if os.path.isdir(os.path.join(current_path, item))]
            files = sorted(files, key=self._natural_sort_key)
            items = sorted(dirs) + sorted(files, key=self._natural_sort_key_with_original_first)
            for index, item in enumerate(items):
                path = os.path.join(current_path, item)
                connector = "├── " if index < len(items) - 1 else "└── "
                if os.path.isdir(path):
                    logging.debug(f"Adding directory to structure: {path}")
                    structure_line = f"{prefix}{connector}{item}/\n"
                    structure += structure_line
                    extension = "│   " if index < len(items) - 1 else "    "
                    structure += self._build_structure(path, prefix + extension)
                else:
                    logging.debug(f"Adding file to structure: {path}")
                    structure_line = f"{prefix}{connector}{item}\n"
                    structure += structure_line
        except Exception as e:
            error_message = f"An error occurred while building the structure: {str(e)}"
            logging.error(error_message)
            print(f"An error occurred: {str(e)}")
        return structure

    def _natural_sort_key(self, s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

    def _natural_sort_key_with_original_first(self, s):
        base, ext = os.path.splitext(s)
        match = re.match(r"(.*?)(\d+)$", base)
        if match:
            return [match.group(1).lower(), int(match.group(2)), ext.lower()]
        return [base.lower(), 0, ext.lower()]

    def _get_unique_filename(self, filename) -> str:
        base, extension = os.path.splitext(filename)
        counter = 1
        unique_filename = filename
        while os.path.exists(unique_filename):
            unique_filename = f"{base}{counter}{extension}"
            counter += 1
        logging.debug(f"Unique filename generated: {unique_filename}")
        return unique_filename
