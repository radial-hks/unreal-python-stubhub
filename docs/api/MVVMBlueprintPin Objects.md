## MVVMBlueprintPin Objects

```python
class MVVMBlueprintPin(StructBase)
```

MVVMBlueprint Pin

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintPin.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_object`` (Object):  [Read-Only] If the default value for this pin should be an object, we store a pointer to it
- ``default_string`` (str):  [Read-Only] Default value for this pin (used if the pin has no connections), stored as a string
- ``default_text`` (Text):  [Read-Only] If the default value for this pin should be an FText, it is stored here.
- ``id`` (MVVMBlueprintPinId):  [Read-Only]
- ``path`` (MVVMBlueprintPropertyPath):  [Read-Only]
- ``split`` (bool):  [Read-Only] The pin is split.
- ``status`` (MVVMBlueprintPinStatus):  [Read-Only] The pin could not be set.

<a id="unreal.MVVMBlueprintPin.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AssetMapping"></a>