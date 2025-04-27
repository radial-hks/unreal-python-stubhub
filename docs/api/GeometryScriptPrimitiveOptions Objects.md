## GeometryScriptPrimitiveOptions Objects

```python
class GeometryScriptPrimitiveOptions(StructBase)
```

Geometry Script Primitive Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshPrimitiveFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_orientation`` (bool):  [Read-Write]
- ``material_id`` (int32):  [Read-Write] Material ID to set on primitive mesh triangles
- ``polygroup_mode`` (GeometryScriptPrimitivePolygroupMode):  [Read-Write]
- ``uv_mode`` (GeometryScriptPrimitiveUVMode):  [Read-Write]

<a id="unreal.GeometryScriptPrimitiveOptions.__init__"></a>

#### __init__

```python
def __init__(
        polygroup_mode:
    GeometryScriptPrimitivePolygroupMode = GeometryScriptPrimitivePolygroupMode
    .SINGLE_GROUP,
        flip_orientation: bool = False,
        uv_mode: GeometryScriptPrimitiveUVMode = GeometryScriptPrimitiveUVMode.
    UNIFORM,
        material_id: int = 0) -> None
```

<a id="unreal.GeometryScriptPrimitiveOptions.polygroup_mode"></a>

#### polygroup_mode

```python
@property
def polygroup_mode() -> GeometryScriptPrimitivePolygroupMode
```

(GeometryScriptPrimitivePolygroupMode):  [Read-Write]

<a id="unreal.GeometryScriptPrimitiveOptions.polygroup_mode"></a>

#### polygroup_mode

```python
@polygroup_mode.setter
def polygroup_mode(value: GeometryScriptPrimitivePolygroupMode) -> None
```

<a id="unreal.GeometryScriptPrimitiveOptions.flip_orientation"></a>

#### flip_orientation

```python
@property
def flip_orientation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptPrimitiveOptions.flip_orientation"></a>

#### flip_orientation

```python
@flip_orientation.setter
def flip_orientation(value: bool) -> None
```

<a id="unreal.GeometryScriptPrimitiveOptions.uv_mode"></a>

#### uv_mode

```python
@property
def uv_mode() -> GeometryScriptPrimitiveUVMode
```

(GeometryScriptPrimitiveUVMode):  [Read-Write]

<a id="unreal.GeometryScriptPrimitiveOptions.uv_mode"></a>

#### uv_mode

```python
@uv_mode.setter
def uv_mode(value: GeometryScriptPrimitiveUVMode) -> None
```

<a id="unreal.GeometryScriptPrimitiveOptions.material_id"></a>

#### material_id

```python
@property
def material_id() -> int
```

(int32):  [Read-Write] Material ID to set on primitive mesh triangles

<a id="unreal.GeometryScriptPrimitiveOptions.material_id"></a>

#### material_id

```python
@material_id.setter
def material_id(value: int) -> None
```

<a id="unreal.GeometryScriptRevolveOptions"></a>