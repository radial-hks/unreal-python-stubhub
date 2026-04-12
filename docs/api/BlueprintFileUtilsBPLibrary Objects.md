## BlueprintFileUtilsBPLibrary Objects

```python
class BlueprintFileUtilsBPLibrary(BlueprintFunctionLibrary)
```

Blueprint File Utils BPLibrary

**C++ Source:**

- **Plugin**: BlueprintFileUtils
- **Module**: BlueprintFileUtils
- **File**: BlueprintFileUtilsBPLibrary.h

<a id="unreal.BlueprintFileUtilsBPLibrary.move_file"></a>

#### move\_file

```python
@classmethod
def move_file(cls,
              dest_filename: str,
              src_filename: str,
              replace: bool = True,
              even_if_read_only: bool = False) -> bool
```

X.move_file(dest_filename, src_filename, replace=True, even_if_read_only=False) -> bool
Move File

Args:
    dest_filename (str): 
    src_filename (str): 
    replace (bool): 
    even_if_read_only (bool): 

Returns:
    bool:

<a id="unreal.BlueprintFileUtilsBPLibrary.make_directory"></a>

#### make\_directory

```python
@classmethod
def make_directory(cls, path: str, create_tree: bool = False) -> bool
```

X.make_directory(path, create_tree=False) -> bool
Makes a new directory, and optionally sub-directories

Args:
    path (str): The directory path to make
    create_tree (bool): If true, the entire directory tree will be created if it doesnt exist.  Otherwise only the leaft most directory will be created if possible

Returns:
    bool: true if the directory was created, false otherwise

<a id="unreal.BlueprintFileUtilsBPLibrary.get_user_directory"></a>

#### get\_user\_directory

```python
@classmethod
def get_user_directory(cls) -> str
```

X.get_user_directory() -> str
Get the users directory.  Platform specific (usually something like MyDocuments or the users home directory

Returns:
    str:

<a id="unreal.BlueprintFileUtilsBPLibrary.find_recursive"></a>

#### find\_recursive

```python
@classmethod
def find_recursive(cls,
                   start_directory: str,
                   wildcard: str = "",
                   find_files: bool = True,
                   find_directories: bool = False) -> Optional[Array[str]]
```

X.find_recursive(start_directory, wildcard="", find_files=True, find_directories=False) -> Array[str] or None
Finds all the files and/or directories within the given directory and any sub-directories.  Files can be found with anoptional file extension filter.

Args:
    start_directory (str): The absolute path to the directory to start the search. Ex: "C:\UnrealEditor\Pictures"
    wildcard (str): Wildcard that can be used to find files or directories with specific text in their name. E.g *.png to find all files ending with the png extension, *images* to find anything with the word "images" in it Otherwise FileExtension can be of the form .EXT or just EXT and only files with that extension will be returned. Does not apply to directories
    find_files (bool): Whether or not to find files
    find_directories (bool): Whether or not to find directories

Returns:
    Array[str] or None: true if anything was found, false otherwise

    found_paths (Array[str]): All the paths (directories and/or files) found

<a id="unreal.BlueprintFileUtilsBPLibrary.find_files"></a>

#### find\_files

```python
@classmethod
def find_files(cls,
               directory: str,
               file_extension: str = "") -> Optional[Array[str]]
```

X.find_files(directory, file_extension="") -> Array[str] or None
Finds all the files within the given directory, with optional file extension filter.

Args:
    directory (str): The absolute path to the directory to search. Ex: "C:\UnrealEditor\Pictures"
    file_extension (str): If FileExtension is empty string "" then all files are found. Otherwise FileExtension can be of the form .EXT or just EXT and only files with that extension will be returned.

Returns:
    Array[str] or None: true if anything was found, false otherwise

    found_files (Array[str]): All the files found that matched the optional FileExtension filter, or all files if none was specified.

<a id="unreal.BlueprintFileUtilsBPLibrary.file_exists"></a>

#### file\_exists

```python
@classmethod
def file_exists(cls, filename: str) -> bool
```

X.file_exists(filename) -> bool
Checks if a file exists

Args:
    filename (str): The filename to check

Returns:
    bool: true if Filename exists, false otherwise

<a id="unreal.BlueprintFileUtilsBPLibrary.directory_exists"></a>

#### directory\_exists

```python
@classmethod
def directory_exists(cls, directory: str) -> bool
```

X.directory_exists(directory) -> bool
Checks if a directory exists

Args:
    directory (str): The directory path to check

Returns:
    bool: true if Directory exists, false otherwise

<a id="unreal.BlueprintFileUtilsBPLibrary.delete_file"></a>

#### delete\_file

```python
@classmethod
def delete_file(cls,
                filename: str,
                must_exist: bool = False,
                even_if_read_only: bool = False) -> bool
```

X.delete_file(filename, must_exist=False, even_if_read_only=False) -> bool
Deletes a file.

Args:
    filename (str): 
    must_exist (bool): 
    even_if_read_only (bool): 

Returns:
    bool:

<a id="unreal.BlueprintFileUtilsBPLibrary.delete_directory"></a>

#### delete\_directory

```python
@classmethod
def delete_directory(cls,
                     directory: str,
                     must_exist: bool = False,
                     delete_recursively: bool = False) -> bool
```

X.delete_directory(directory, must_exist=False, delete_recursively=False) -> bool
Deletes a directory and all the files in it and optionally all sub-directories and files within it

Args:
    directory (str): The Directory to delete
    must_exist (bool): If true, the directory must exist or the return value will be false
    delete_recursively (bool): If true, all sub-directories will be deleted as well. If false and there are contents in the directory, the delete operation will fail.

Returns:
    bool: true if the directory was succesfully deleted, false otherwise

<a id="unreal.BlueprintFileUtilsBPLibrary.copy_file"></a>

#### copy\_file

```python
@classmethod
def copy_file(cls,
              dest_filename: str,
              src_filename: str,
              replace: bool = True,
              even_if_read_only: bool = False) -> bool
```

X.copy_file(dest_filename, src_filename, replace=True, even_if_read_only=False) -> bool
Copies a file.

Args:
    dest_filename (str): 
    src_filename (str): 
    replace (bool): 
    even_if_read_only (bool): 

Returns:
    bool:

<a id="unreal.ChaosVDSolverDataComponent"></a>