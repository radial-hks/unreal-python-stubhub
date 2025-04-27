## FilePath Objects

```python
class FilePath(StructBase)
```

Structure for file paths that are displayed in the editor with a picker UI.

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``file_path`` (str):  [Read-Write] The path to the file.

<a id="unreal.FilePath.__init__"></a>

#### __init__

```python
def __init__(file_path: str = "") -> None
```

<a id="unreal.FilePath.file_path"></a>

#### file_path

```python
@property
def file_path() -> str
```

(str):  [Read-Write] The path to the file.

<a id="unreal.FilePath.file_path"></a>

#### file_path

```python
@file_path.setter
def file_path(value: str) -> None
```

<a id="unreal.FloatInterval"></a>