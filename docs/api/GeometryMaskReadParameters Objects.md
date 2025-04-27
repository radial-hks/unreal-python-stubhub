## GeometryMaskReadParameters Objects

```python
class GeometryMaskReadParameters(StructBase)
```

Geometry Mask Read Parameters

**C++ Source:**

- **Plugin**: GeometryMask
- **Module**: GeometryMask
- **File**: GeometryMaskTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``canvas_name`` (Name):  [Read-Write] Specifies the GeometryMaskCanvas to read from.
- ``color_channel`` (GeometryMaskColorChannel):  [Read-Write]
- ``invert`` (bool):  [Read-Write]

<a id="unreal.GeometryMaskReadParameters.__init__"></a>

#### __init__

```python
def __init__(canvas_name: Name = "None") -> None
```

<a id="unreal.GeometryMaskReadParameters.canvas_name"></a>

#### canvas_name

```python
@property
def canvas_name() -> Name
```

(Name):  [Read-Write] Specifies the GeometryMaskCanvas to read from.

<a id="unreal.GeometryMaskReadParameters.canvas_name"></a>

#### canvas_name

```python
@canvas_name.setter
def canvas_name(value: Name) -> None
```

<a id="unreal.GeometryMaskWriteParameters"></a>