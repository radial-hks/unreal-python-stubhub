## GeometryScriptMeshPlaneCutOptions Objects

```python
class GeometryScriptMeshPlaneCutOptions(StructBase)
```

Geometry Script Mesh Plane Cut Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBooleanFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``fill_holes`` (bool):  [Read-Write]
- ``fill_spans`` (bool):  [Read-Write]
- ``flip_cut_side`` (bool):  [Read-Write]
- ``hole_fill_material_id`` (int32):  [Read-Write] If non-negative and bFillHoles is true, specify the material ID to set on hole fill triangles
- ``uv_world_dimension`` (float):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneCutOptions.__init__"></a>

#### __init__

```python
def __init__(fill_holes: bool = False,
             hole_fill_material_id: int = 0,
             fill_spans: bool = False,
             flip_cut_side: bool = False,
             uv_world_dimension: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions.fill_holes"></a>

#### fill_holes

```python
@property
def fill_holes() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneCutOptions.fill_holes"></a>

#### fill_holes

```python
@fill_holes.setter
def fill_holes(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions.hole_fill_material_id"></a>

#### hole_fill_material_id

```python
@property
def hole_fill_material_id() -> int
```

(int32):  [Read-Write] If non-negative and bFillHoles is true, specify the material ID to set on hole fill triangles

<a id="unreal.GeometryScriptMeshPlaneCutOptions.hole_fill_material_id"></a>

#### hole_fill_material_id

```python
@hole_fill_material_id.setter
def hole_fill_material_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions.fill_spans"></a>

#### fill_spans

```python
@property
def fill_spans() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneCutOptions.fill_spans"></a>

#### fill_spans

```python
@fill_spans.setter
def fill_spans(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions.flip_cut_side"></a>

#### flip_cut_side

```python
@property
def flip_cut_side() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneCutOptions.flip_cut_side"></a>

#### flip_cut_side

```python
@flip_cut_side.setter
def flip_cut_side(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshPlaneCutOptions.uv_world_dimension"></a>

#### uv_world_dimension

```python
@property
def uv_world_dimension() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptMeshPlaneCutOptions.uv_world_dimension"></a>

#### uv_world_dimension

```python
@uv_world_dimension.setter
def uv_world_dimension(value: float) -> None
```

<a id="unreal.GeometryScriptMeshPlaneSliceOptions"></a>