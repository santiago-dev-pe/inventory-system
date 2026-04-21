from pathlib import Path
from typing import Union, Optional, Tuple

def get_validated_path(base_path: Union[str, Path, None] = None) -> Optional[Path]: 
    # If the input is empty, null, or a dot, default to the current working directory
    if not base_path or str(base_path).strip() in ("", "."):
        return Path.cwd()

    # Convert to a Path object and resolve to an absolute path to clean up the string
    path_obj = Path(base_path).resolve()

    # Validate that the path exists and is actually a directory
    if path_obj.exists() and path_obj.is_dir():
        return path_obj
    
    # Return None instead of False to maintain type consistency and avoid TypeErrors
    return None

        
def get_new_folder_name(name_path: Union[str, Path, None] = None) -> Path:
    # If no name is provided or it's empty, use a default fallback
    if not name_path or str(name_path).strip() in ("", "."):
        return Path("New_folder")
    
    # Ensure the return value is always a Path object
    return Path(name_path)


def build_full_path(base_path: Optional[Path], addition_path: Union[str, Path]) -> Optional[Path]:
    # Prevent operations if the base_path validation failed previously
    if base_path is None:
        return None
        
    # Join paths safely using the / operator
    return Path(base_path) / Path(addition_path)


def create_dir(data: Optional[Path]) -> Tuple[bool, str]:
    # Check if the path object is valid before attempting creation
    if data is None:
        return False, "Error: The provided path is invalid or None."

    try:
        # parents=True: creates intermediate directories if they don't exist
        # exist_ok=True: prevents an error if the directory already exists
        data.mkdir(parents=True, exist_ok=True)
        return True, "Success: Directory created or already exists."
        
    except PermissionError:
        return False, "Error: Insufficient system permissions to create this directory."
    except OSError as e:
        return False, f"Error: System-level issue occurred: {e}"
    except Exception as e:
        return False, f"Error: An unexpected error occurred: {str(e)}"


        



    
      




