from concurrent.futures import ThreadPoolExecutor
from typing import Any
from ex_3.HomeworkHandler import HomeworkHandler
from ex_3.helper import normalize, OTHER_FOLDER, FOLDERS_DATA
from pathlib import Path
import os
     
class DirectoryCreator():
    def __init__(self, path: Path, folders_data: dict) -> None:
        self.PATH = path
        self.FOLDERS_DATA = folders_data
    
    def __call__(self) -> None:
        for name in self.FOLDERS_DATA:
            folder_path = f"{self.PATH.parent}/{self.PATH.name}/{name}"
            
            if not Path(folder_path).exists():
                os.mkdir(folder_path)

class FileHandler():
    def __init__(self, path: Path, default_path: Path):
        name_parts = path.name.split('.')
        self.default_path = default_path
        self.path = path
        self.ext = name_parts.pop()
        self.name = normalize('.'.join(name_parts))
        
    def use_file_name(self, path: str, ext: str, counter: int = 0):
        file_name = f"{path}{ext}" if not counter else f"{path}_{counter}{ext}"
        return self.use_file_name(path, ext, counter + 1) if os.path.exists(file_name) else file_name    
        
    def __call__(self, default_parent_folder: str, folders_data: dict) -> str:
        parent_folder_name = default_parent_folder
        for name, list in folders_data.items():
            if self.ext.upper() in list:
                parent_folder_name = name
                break
        
        file_name = self.use_file_name(f"{self.default_path}/{parent_folder_name}/{self.name}", self.path.suffix)
        os.rename(self.path, file_name)
        print(f"{self.path} --> {file_name}")      

class Arrange():
    def __init__(self, base_path: Path, folders_data: dict, directory_creator: DirectoryCreator, default_parent_folder: str = OTHER_FOLDER) -> None:
        directory_creator()
        self.DEFAULT_PARENT_FOLDER = default_parent_folder
        self.BASE_PATH = base_path
        self.FOLDERS_DATA = folders_data
        
    def run(self, path: Path) -> None:
        if not path.exists():
            print(f"Folder '{path.name}' in '{path.parent}' doesn't exists!")
        elif path.is_file():
            print(f"'{path.name}' is not a folder!")
        else:
            files = []
            folders = []
            for sub_path in path.iterdir():
                if sub_path.is_dir() and sub_path.name not in self.FOLDERS_DATA:
                    folders.append(FolderHandler(path=sub_path, arrange=self))
                elif sub_path.is_file():
                    files.append(FileHandler(path=sub_path, default_path=self.BASE_PATH))
        with ThreadPoolExecutor(max_workers=100) as executor:
            executor.map(lambda handler: handler(self.DEFAULT_PARENT_FOLDER, self.FOLDERS_DATA), files)
            executor.map(lambda handler: handler(), folders)
            
class FolderHandler():
    def __init__(self, path: Path, arrange: Arrange) -> None:
        self.PATH = path
        self.arrange = arrange
    
    def __call__(self) -> Any:
        self.arrange(self.PATH)
        try:
            os.rmdir(self.PATH)
        except OSError as error:
            print(error)
            print(f"Path {self.PATH} can't be removed")
      
class Cleaner(HomeworkHandler):
    def __init__(self):
        super().__init__(1, "Folder cleaner, using Treads")     
        
    def run(self):
        base_path_str = input('Please enter path to folder: ').strip()
        base_path = Path(base_path_str)
        arrange = Arrange(
            base_path=Path(base_path), 
            folders_data=FOLDERS_DATA,
            directory_creator=DirectoryCreator(path=base_path, folders_data=FOLDERS_DATA)
            )
        arrange.run(base_path)