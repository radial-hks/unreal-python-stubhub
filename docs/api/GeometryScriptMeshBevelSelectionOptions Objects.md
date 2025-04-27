## GeometryScriptMeshBevelSelectionOptions Objects

```python
class GeometryScriptMeshBevelSelectionOptions(StructBase)
```

Geometry Script Mesh Bevel Selection Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bevel_distance`` (float):  [Read-Write] Distance that each beveled mesh edge is inset from it's initial position
- ``infer_material_id`` (bool):  [Read-Write] If true, when faces on either side of a beveled mesh edges have the same Material ID, beveled edge will be set to that Material ID. Otherwise SetMaterialID is used.
- ``round_weight`` (float):  [Read-Write] Roundness of the bevel. Ignored if Subdivisions = 0.
- ``set_material_id`` (int32):  [Read-Write] Material ID to set on the new faces introduced by bevel operation, unless bInferMaterialID=true and non-ambiguous MaterialID can be inferred from adjacent faces
- ``subdivisions`` (int32):  [Read-Write] Number of edge loops added along the bevel faces

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.__init__"></a>

#### __init__

```python
def __init__(bevel_distance: float = 0.000000,
             infer_material_id: bool = False,
             set_material_id: int = 0,
             subdivisions: int = 0,
             round_weight: float = 0.000000) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.bevel_distance"></a>

#### bevel_distance

```python
@property
def bevel_distance() -> float
```

(float):  [Read-Write] Distance that each beveled mesh edge is inset from it's initial position

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.bevel_distance"></a>

#### bevel_distance

```python
@bevel_distance.setter
def bevel_distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.infer_material_id"></a>

#### infer_material_id

```python
@property
def infer_material_id() -> bool
```

(bool):  [Read-Write] If true, when faces on either side of a beveled mesh edges have the same Material ID, beveled edge will be set to that Material ID. Otherwise SetMaterialID is used.

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.infer_material_id"></a>

#### infer_material_id

```python
@infer_material_id.setter
def infer_material_id(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.set_material_id"></a>

#### set_material_id

```python
@property
def set_material_id() -> int
```

(int32):  [Read-Write] Material ID to set on the new faces introduced by bevel operation, unless bInferMaterialID=true and non-ambiguous MaterialID can be inferred from adjacent faces

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.set_material_id"></a>

#### set_material_id

```python
@set_material_id.setter
def set_material_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.subdivisions"></a>

#### subdivisions

```python
@property
def subdivisions() -> int
```

(int32):  [Read-Write] Number of edge loops added along the bevel faces

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.subdivisions"></a>

#### subdivisions

```python
@subdivisions.setter
def subdivisions(value: int) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.round_weight"></a>

#### round_weight

```python
@property
def round_weight() -> float
```

(float):  [Read-Write] Roundness of the bevel. Ignored if Subdivisions = 0.

<a id="unreal.GeometryScriptMeshBevelSelectionOptions.round_weight"></a>

#### round_weight

```python
@round_weight.setter
def round_weight(value: float) -> None
```

<a id="unreal.GeometryScriptCalculateNormalsOptions"></a>