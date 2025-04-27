## GeometryMaskWriteParameters Objects

```python
class GeometryMaskWriteParameters(StructBase)
```

Geometry Mask Write Parameters

**C++ Source:**

- **Plugin**: GeometryMask
- **Module**: GeometryMask
- **File**: GeometryMaskTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``canvas_name`` (Name):  [Read-Write] Specifies the GeometryMaskCanvas to reference.
- ``color_channel`` (GeometryMaskColorChannel):  [Read-Write]
- ``inner_radius`` (double):  [Read-Write] The inner offset of the shapes extent in world units. Smoothly interpolates between the shape/outer radius and this.
- ``invert`` (bool):  [Read-Write]
- ``operation_type`` (GeometryMaskCompositeOperation):  [Read-Write]
- ``outer_radius`` (double):  [Read-Write] The outer offset of the shapes extent in world units. Smoothly interpolates between the shape/inner radius and this.
- ``priority`` (int32):  [Read-Write] Higher values draw above lower.

<a id="unreal.GeometryMaskWriteParameters.__init__"></a>

#### __init__

```python
def __init__(canvas_name: Name = "None") -> None
```

<a id="unreal.GeometryMaskWriteParameters.canvas_name"></a>

#### canvas_name

```python
@property
def canvas_name() -> Name
```

(Name):  [Read-Write] Specifies the GeometryMaskCanvas to reference.

<a id="unreal.GeometryMaskWriteParameters.canvas_name"></a>

#### canvas_name

```python
@canvas_name.setter
def canvas_name(value: Name) -> None
```

<a id="unreal.NiagaraVariableBase"></a>