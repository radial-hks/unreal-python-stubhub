## GeometryScriptMeshPlaneSliceOptions Objects

```python
class GeometryScriptMeshPlaneSliceOptions(StructBase)
```

Geometry Script Mesh Plane Slice Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBooleanFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_holes`` (bool):  [Read-Write]
- ``fill_spans`` (bool):  [Read-Write]
- ``gap_width`` (float):  [Read-Write]
- ``hole_fill_material_id`` (int32):  [Read-Write] If non-negative and bFillHoles is true, specify the material ID to set on hole fill triangles
- ``uv_world_dimension`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.__init__"></a>

#### __init__

```python
def __init__(fill_holes: bool = False,
             hole_fill_material_id: int = 0,
             fill_spans: bool = False,
             gap_width: float = 0.000000,
             uv_world_dimension: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.fill_holes"></a>

#### fill_holes

```python
@property
def fill_holes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.fill_holes"></a>

#### fill_holes

```python
@fill_holes.setter
def fill_holes(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.hole_fill_material_id"></a>

#### hole_fill_material_id

```python
@property
def hole_fill_material_id() -> int
```

(int32):  [Read-Write] If non-negative and bFillHoles is true, specify the material ID to set on hole fill triangles

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.hole_fill_material_id"></a>

#### hole_fill_material_id

```python
@hole_fill_material_id.setter
def hole_fill_material_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.fill_spans"></a>

#### fill_spans

```python
@property
def fill_spans() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.fill_spans"></a>

#### fill_spans

```python
@fill_spans.setter
def fill_spans(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.gap_width"></a>

#### gap_width

```python
@property
def gap_width() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.gap_width"></a>

#### gap_width

```python
@gap_width.setter
def gap_width(value: float) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.uv_world_dimension"></a>

#### uv_world_dimension

```python
@property
def uv_world_dimension() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneSliceOptions.uv_world_dimension"></a>

#### uv_world_dimension

```python
@uv_world_dimension.setter
def uv_world_dimension(value: float) -> None
```

<a id="unreal.GeometryScriptMeshMirrorOptions"></a>