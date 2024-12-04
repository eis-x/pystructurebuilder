import os
from datetime import datetime
from utils import name

first_time = False

def setup_logging():
    global first_time
    user_home_dir = os.getenv('APPDATA')
    if user_home_dir is None:
        user_home_dir = os.path.expanduser("~")
    module_name = name
    log_dir_path = os.path.join(user_home_dir, "."+module_name, 'logs')
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
    log_file_path = os.path.join(log_dir_path, f'{module_name}.log')

    def log_message(message: str) -> None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{timestamp}: {message}\n")
            
    def log_separator(message: str) -> None:
        with open(log_file_path, 'a', encoding='utf-8') as log_file:
            log_file.write(f"{message}\n")

    start_message = f"{module_name.title()} initialized successfully."
    if not first_time:
        first_time = True
        print(start_message)
        log_message(start_message)
        
    return log_message, log_separator
