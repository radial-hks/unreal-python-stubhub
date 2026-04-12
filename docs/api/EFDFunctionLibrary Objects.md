## EFDFunctionLibrary Objects

```python
class EFDFunctionLibrary(BlueprintFunctionLibrary)
```

EFDFunction Library

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EasyFileDialog
- **File**: EFDFunctionLibrary.h

<a id="unreal.EFDFunctionLibrary.save_file_dialog"></a>

#### save\_file\_dialog

```python
@classmethod
def save_file_dialog(cls, dialog_title: str, default_path: str,
                     default_file: str, file_type_description: str,
                     file_type: str,
                     flags: EasyFileDialogFlags) -> Optional[Array[str]]
```

X.save_file_dialog(dialog_title, default_path, default_file, file_type_description, file_type, flags) -> Array[str] or None
Save File Dialog

Args:
    dialog_title (str): 
    default_path (str): 
    default_file (str): 
    file_type_description (str): 
    file_type (str): 
    flags (EasyFileDialogFlags): 

Returns:
    Array[str] or None: 

    out_filenames (Array[str]):

<a id="unreal.EFDFunctionLibrary.open_folder_dialog"></a>

#### open\_folder\_dialog

```python
@classmethod
def open_folder_dialog(cls, dialog_title: str,
                       default_path: str) -> Optional[str]
```

X.open_folder_dialog(dialog_title, default_path) -> str or None
Open Folder Dialog

Args:
    dialog_title (str): 
    default_path (str): 

Returns:
    str or None: 

    out_folder_name (str):

<a id="unreal.EFDFunctionLibrary.open_file_dialog"></a>

#### open\_file\_dialog

```python
@classmethod
def open_file_dialog(cls, dialog_title: str, default_path: str,
                     default_file: str, file_types: str,
                     flags: EasyFileDialogFlags) -> Optional[Array[str]]
```

X.open_file_dialog(dialog_title, default_path, default_file, file_types, flags) -> Array[str] or None
Open File Dialog

Args:
    dialog_title (str): 
    default_path (str): 
    default_file (str): 
    file_types (str): 
    flags (EasyFileDialogFlags): 

Returns:
    Array[str] or None: 

    out_filenames (Array[str]):

<a id="unreal.OctreeDynamicMeshComponent"></a>