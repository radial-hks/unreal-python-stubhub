## AttributeCurve Objects

```python
class AttributeCurve(IndexedCurve)
```

Attribute Curve

**C++ Source:**

- **Module**: Engine
- **File**: AttributeCurve.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``keys`` (Array[AttributeKey]):  [Read-Write] The keys, ordered by time
- ``script_struct`` (ScriptStruct):  [Read-Write] Transient UScriptStruct instance representing the underlying value type for the curve
- ``script_struct_path`` (SoftObjectPath):  [Read-Only] Path to UScriptStruct to be loaded
- ``should_interpolate`` (bool):  [Read-Write] Whether or not to interpolate between keys of ScripStruct type

<a id="unreal.AttributeCurve.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InputDevicePropertyHandle"></a>