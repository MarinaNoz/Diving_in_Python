
from create_json import create_json
from pathlib import Path
from add_name_to_json import ui

if __name__ == '__main__':
    create_json(Path('../seminar_8/result.txt'))
    ui()