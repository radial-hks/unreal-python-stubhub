## Guid Objects

```python
class Guid(StructBase)
```

A globally unique identifier (mirrored from Guid.h)

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (int32):  [Read-Write]
- ``b`` (int32):  [Read-Write]
- ``c`` (int32):  [Read-Write]
- ``d`` (int32):  [Read-Write]

<a id="unreal.Guid.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Guid.to_string"></a>

#### to_string

```python
def to_string() -> str
```

x.to_string() -> str
Converts a GUID value to a string, in the form 'A-B-C-D'

Returns:
    str:

<a id="unreal.DateTime"></a>