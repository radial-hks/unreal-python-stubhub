## InterchangeFilePickerParameters Objects

```python
class InterchangeFilePickerParameters(StructBase)
```

Interchange File Picker Parameters

**C++ Source:**

- **Module**: InterchangeEngine
- **File**: InterchangeFilePickerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_multiple_files`` (bool):  [Read-Write] If true, the user will be able to select multiple files.
- ``default_path`` (str):  [Read-Write] Set the default open path that the dialog will show to the user.
- ``extra_formats`` (Array[str]):  [Read-Write] Add some extension to the picker. Format text item that way TEXT("fbx;Filmbox")
- ``show_all_factories_extension`` (bool):  [Read-Write] If true, the user will be able to select any unreal editor factory + interchange file types.
- ``title`` (Text):  [Read-Write] If not empty, this will override the default title.

<a id="unreal.InterchangeFilePickerParameters.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InterchangeStackInfo"></a>