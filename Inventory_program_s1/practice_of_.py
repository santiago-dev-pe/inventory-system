from pathlib import Path

def get_validated_path() -> Path:
    while True:
        try:
            entry = input("Enter a directory path or press Enter for current directory:\n").strip()
            
            if not entry:
                current_path = Path.cwd().resolve()
                print(f"Using current directory: {current_path}")
                return current_path
            
            target_path = Path(entry).resolve()

            if target_path.exists() and target_path.is_dir():
                print(f"Directory confirmed: {target_path}")
                return target_path
            
            print("Error: The path does not exist or is not a directory.")
                
        except OSError as e:
            print(f"System Error: Illegal characters or restricted access. {e}")
        
def create_dir() -> Path:
    pass
      




