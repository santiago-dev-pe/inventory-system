from pathlib import Path

def select_path() -> Path:
    while True:
        try:
            user_inp = input("Write a direction to continue or press Enter to continue in the current path:\n").strip()
            
            if user_inp == "":
                base_path = Path.cwd()
                print(f"The folder that will be used to create subfolders is {base_path}.")
                return base_path
            
            selected_path = Path(user_inp)

            if selected_path.exists() and selected_path.is_dir():
                print("The folder specified by the user will be used.")
                return selected_path
            else:
                print("The path does not exist or is not a directory.")
                
        except OSError as e:
            print(f"Error: Invalid system operation or illegal characters. Details: {e}")
        
def create_dir() -> Path:
    pass
      




