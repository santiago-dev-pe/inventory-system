from pathlib import Path
from typing import Union

def get_validated_path(base_path : Path) -> Path: 
    entry = base_path       
    if not entry:
        current_path = Path.cwd()
        return current_path
            
    target_path = Path(entry)

    if target_path.exists() and target_path.is_dir():
        return target_path

        
def get_new_folder_name(name_path : Path) -> Path:
        entry = name_path

        if not entry:
            file_name = Path("New_folder")
            return file_name
        else:
            file_name = Path(entry)
            return file_name


def build_full_path(base_path : Path , adition_path : Path) -> Path:
    
     full_path = base_path / adition_path
     return full_path

def create_dir(data: Path) -> tuple[bool, str]:
    try:
        data.mkdir(parents=True, exist_ok=True)
        return True, "OK"
    except Exception as e:
        return False, str(e)


        



    
      




