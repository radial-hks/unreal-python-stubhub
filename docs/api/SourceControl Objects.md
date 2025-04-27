## SourceControl Objects

```python
class SourceControl(Object)
```

Editor source control common functionality.
note: Many of these source control methods use *smart* file strings which can be one of: - fully qualified path - relative path - long package name - asset path - export text path (often stored on clipboard) For example: - D:\Epic\Dev-Ent\Projects\Python3rdBP\Content\Mannequin\Animations\ThirdPersonIdle.uasset - Content\Mannequin\Animations\ThirdPersonIdle.uasset - /Game/Mannequin/Animations/ThirdPersonIdle - /Game/Mannequin/Animations/ThirdPersonIdle.ThirdPersonIdle - AnimSequence'/Game/Mannequin/Animations/ThirdPersonIdle.ThirdPersonIdle'

**C++ Source:**

- **Module**: SourceControl
- **File**: SourceControlHelpers.h

<a id="unreal.SourceControl.sync_files"></a>

#### sync_files

```python
@classmethod
def sync_files(cls, files: Array[str], silent: bool = False) -> bool
```

X.sync_files(files, silent=False) -> bool
Use currently set source control provider to sync files or directories to the head revision.
note: Blocks until action is complete.

Args:
    files (Array[str]): Files or directories to sync - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.sync_file"></a>

#### sync_file

```python
@classmethod
def sync_file(cls, file: str, silent: bool = False) -> bool
```

X.sync_file(file, silent=False) -> bool
Use currently set source control provider to sync a file or directory to the head revision.
note: Blocks until action is complete.

Args:
    file (str): The file or directory to sync - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.revert_unchanged_files"></a>

#### revert_unchanged_files

```python
@classmethod
def revert_unchanged_files(cls,
                           files: Array[str],
                           silent: bool = False) -> bool
```

X.revert_unchanged_files(files, silent=False) -> bool
Use currently set source control provider to revert files provided no changes have been made.
note: Blocks until action is complete.

Args:
    files (Array[str]): Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.revert_unchanged_file"></a>

#### revert_unchanged_file

```python
@classmethod
def revert_unchanged_file(cls, file: str, silent: bool = False) -> bool
```

X.revert_unchanged_file(file, silent=False) -> bool
Use currently set source control provider to revert a file provided no changes have been made.
note: Blocks until action is complete.

Args:
    file (str): File to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.revert_files"></a>

#### revert_files

```python
@classmethod
def revert_files(cls, files: Array[str], silent: bool = False) -> bool
```

X.revert_files(files, silent=False) -> bool
Use currently set source control provider to revert files regardless whether any changes will be lost or not.
note: Blocks until action is complete.

Args:
    files (Array[str]): Files to revert - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.revert_file"></a>

#### revert_file

```python
@classmethod
def revert_file(cls, file: str, silent: bool = False) -> bool
```

X.revert_file(file, silent=False) -> bool
Use currently set source control provider to revert a file regardless whether any changes will be lost or not.
note: Blocks until action is complete.

Args:
    file (str): The file to revert - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.revert_and_reload_packages"></a>

#### revert_and_reload_packages

```python
@classmethod
def revert_and_reload_packages(cls,
                               packages_to_revert: Array[str],
                               revert_all: bool = False,
                               reload_world: bool = False) -> bool
```

X.revert_and_reload_packages(packages_to_revert, revert_all=False, reload_world=False) -> bool
Reverts the provided files then reloads packages.

Args:
    packages_to_revert (Array[str]): The packages to revert
    revert_all (bool): Whether to revert all files
    reload_world (bool): Reload the world

Returns:
    bool: true if succeeded.

<a id="unreal.SourceControl.query_file_state"></a>

#### query_file_state

```python
@classmethod
def query_file_state(cls,
                     file: str,
                     silent: bool = False) -> SourceControlState
```

X.query_file_state(file, silent=False) -> SourceControlState
Use currently set source control provider to query a file's source control state.
note: Blocks until action is complete.

Args:
    file (str): The file to query - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    SourceControlState: Source control state - see USourceControlState. It will have bIsValid set to false if it could not have its values set.

<a id="unreal.SourceControl.mark_files_for_delete"></a>

#### mark_files_for_delete

```python
@classmethod
def mark_files_for_delete(cls,
                          files: Array[str],
                          silent: bool = False) -> bool
```

X.mark_files_for_delete(files, silent=False) -> bool
Use currently set source control provider to remove files from source control and delete the files.
note: Blocks until action is complete.

Args:
    files (Array[str]): 
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.mark_files_for_add"></a>

#### mark_files_for_add

```python
@classmethod
def mark_files_for_add(cls, files: Array[str], silent: bool = False) -> bool
```

X.mark_files_for_add(files, silent=False) -> bool
Use currently set source control provider to mark files for add. Does nothing (and returns true) for any file that is already under SC
note: Blocks until action is complete.

Args:
    files (Array[str]): Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.mark_file_for_delete"></a>

#### mark_file_for_delete

```python
@classmethod
def mark_file_for_delete(cls, file: str, silent: bool = False) -> bool
```

X.mark_file_for_delete(file, silent=False) -> bool
Use currently set source control provider to remove file from source control and
delete the file.
note: Blocks until action is complete.

Args:
    file (str): The file to delete - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.mark_file_for_add"></a>

#### mark_file_for_add

```python
@classmethod
def mark_file_for_add(cls, file: str, silent: bool = False) -> bool
```

X.mark_file_for_add(file, silent=False) -> bool
Use currently set source control provider to mark a file for add. Does nothing (and returns true) if the file is already under SC
note: Blocks until action is complete.

Args:
    file (str): The file to add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.last_error_msg"></a>

#### last_error_msg

```python
@classmethod
def last_error_msg(cls) -> Text
```

X.last_error_msg() -> Text
Get status text set by SourceControl system if an error occurs regardless whether bSilent is set or not.
Only set if there was an error.

Returns:
    Text:

<a id="unreal.SourceControl.is_enabled"></a>

#### is_enabled

```python
@classmethod
def is_enabled(cls) -> bool
```

X.is_enabled() -> bool
Determine if there is a source control system enabled

Returns:
    bool: true if enabled, false if not

<a id="unreal.SourceControl.is_available"></a>

#### is_available

```python
@classmethod
def is_available(cls) -> bool
```

X.is_available() -> bool
Quick check if currently set source control provider is enabled and available for use
(server-based providers can use this to return whether the server is available or not)

Returns:
    bool: true if source control is available, false if it is not

<a id="unreal.SourceControl.current_provider"></a>

#### current_provider

```python
@classmethod
def current_provider(cls) -> str
```

X.current_provider() -> str
Determine the name of the current source control provider.

Returns:
    str: the name of the current source control provider. If one is not set then "None" is returned.

<a id="unreal.SourceControl.copy_file"></a>

#### copy_file

```python
@classmethod
def copy_file(cls,
              source_file: str,
              dest_file: str,
              silent: bool = False) -> bool
```

X.copy_file(source_file, dest_file, silent=False) -> bool
Use currently set source control provider to copy a file.
note: Blocks until action is complete.

Args:
    source_file (str): Source file string to copy from - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    dest_file (str): Source file string to copy to - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard). If package, then uses same extension as source file.
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_out_or_add_files"></a>

#### check_out_or_add_files

```python
@classmethod
def check_out_or_add_files(cls,
                           files: Array[str],
                           silent: bool = False) -> bool
```

X.check_out_or_add_files(files, silent=False) -> bool
Use currently set source control provider to check out files or mark them for add.
note: Blocks until action is complete.

Args:
    files (Array[str]): The files to check out/add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_out_or_add_file"></a>

#### check_out_or_add_file

```python
@classmethod
def check_out_or_add_file(cls, file: str, silent: bool = False) -> bool
```

X.check_out_or_add_file(file, silent=False) -> bool
Use currently set source control provider to check out file or mark it for add.
note: Blocks until action is complete.

Args:
    file (str): The file to check out/add - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_out_files"></a>

#### check_out_files

```python
@classmethod
def check_out_files(cls, files: Array[str], silent: bool = False) -> bool
```

X.check_out_files(files, silent=False) -> bool
Use currently set source control provider to check out specified files.
note: Blocks until action is complete.

Args:
    files (Array[str]): Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_out_file"></a>

#### check_out_file

```python
@classmethod
def check_out_file(cls, file: str, silent: bool = False) -> bool
```

X.check_out_file(file, silent=False) -> bool
Use currently set source control provider to check out a file.
note: Blocks until action is complete.

Args:
    file (str): The file to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_in_files"></a>

#### check_in_files

```python
@classmethod
def check_in_files(cls,
                   files: Array[str],
                   description: str,
                   silent: bool = False,
                   keep_checked_out: bool = False) -> bool
```

X.check_in_files(files, description, silent=False, keep_checked_out=False) -> bool
Use currently set source control provider to check in specified files.
note: Blocks until action is complete.

Args:
    files (Array[str]): Files to check out - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    description (str): Description for check in
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
    keep_checked_out (bool): Keep files checked-out after checking in. This is helpful for maintaining "ownership" of files if further operations are needed.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.check_in_file"></a>

#### check_in_file

```python
@classmethod
def check_in_file(cls,
                  file: str,
                  description: str,
                  silent: bool = False,
                  keep_checked_out: bool = False) -> bool
```

X.check_in_file(file, description, silent=False, keep_checked_out=False) -> bool
Use currently set source control provider to check in a file.
note: Blocks until action is complete.

Args:
    file (str): The file to check in - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    description (str): Description for check in
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.
    keep_checked_out (bool): Keep files checked-out after checking in. This is helpful for maintaining "ownership" of files if further operations are needed.

Returns:
    bool: true if succeeded, false if failed and can call LastErrorMsg() for more info.

<a id="unreal.SourceControl.async_query_file_state"></a>

#### async_query_file_state

```python
@classmethod
def async_query_file_state(cls,
                           file_state_callback: QueryFileStateDelegate,
                           file: str,
                           silent: bool = False) -> None
```

X.async_query_file_state(file_state_callback, file, silent=False) -> None
Query the source control state of the specified file, asynchronously.

Args:
    file_state_callback (QueryFileStateDelegate): Source control state - see USourceControlState. It will have bIsValid set to false if it could not have its values set.
    file (str): The file to query - can be either fully qualified path, relative path, long package name, asset path or export text path (often stored on clipboard)
    silent (bool): if false (default) then write out any error info to the Log. Any error text can be retrieved by LastErrorMsg() regardless.

<a id="unreal.BlueprintEditorToolMenuContext"></a>