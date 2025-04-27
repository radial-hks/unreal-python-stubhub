## GeometryScriptMeshBevelOptions Objects

```python
class GeometryScriptMeshBevelOptions(StructBase)
```

Geometry Script Mesh Bevel Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshModelingFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_filter_box`` (bool):  [Read-Write] If true the set of beveled PolyGroup edges is limited to those that
  are fully or partially contained within the (transformed) FilterBox
- ``bevel_distance`` (float):  [Read-Write] Distance that each beveled mesh edge is inset from it's initial position
- ``filter_box`` (Box):  [Read-Write] Bounding Box used for edge filtering
- ``filter_box_transform`` (Transform):  [Read-Write] Transform applied to the FilterBox
- ``fully_contained`` (bool):  [Read-Write] If true, then only PolyGroup edges that are fully contained within the filter box will be beveled,
  otherwise the edge will be beveled if any vertex is within the filter box.
- ``infer_material_id`` (bool):  [Read-Write] If true, when faces on either side of a beveled mesh edges have the same Material ID, beveled edge will be set to that Material ID. Otherwise SetMaterialID is used.
- ``round_weight`` (float):  [Read-Write] Roundness of the bevel. Ignored if Subdivisions = 0.
- ``set_material_id`` (int32):  [Read-Write] Material ID to set on the new faces introduced by bevel operation, unless bInferMaterialID=true and non-ambiguous MaterialID can be inferred from adjacent faces
- ``subdivisions`` (int32):  [Read-Write] Number of edge loops added along the bevel faces

<a id="unreal.GeometryScriptMeshBevelOptions.__init__"></a>

#### __init__

```python
def __init__(bevel_distance: float = 0.000000,
             infer_material_id: bool = False,
             set_material_id: int = 0,
             subdivisions: int = 0,
             round_weight: float = 0.000000,
             apply_filter_box: bool = False,
             filter_box: Box = [[0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000], False],
             filter_box_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                                [
                                                    -0.000000, 0.000000,
                                                    0.000000
                                                ],
                                                [1.000000, 1.000000,
                                                 1.000000]],
             fully_contained: bool = False) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.bevel_distance"></a>

#### bevel_distance

```python
@property
def bevel_distance() -> float
```

(float):  [Read-Write] Distance that each beveled mesh edge is inset from it's initial position

<a id="unreal.GeometryScriptMeshBevelOptions.bevel_distance"></a>

#### bevel_distance

```python
@bevel_distance.setter
def bevel_distance(value: float) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.infer_material_id"></a>

#### infer_material_id

```python
@property
def infer_material_id() -> bool
```

(bool):  [Read-Write] If true, when faces on either side of a beveled mesh edges have the same Material ID, beveled edge will be set to that Material ID. Otherwise SetMaterialID is used.

<a id="unreal.GeometryScriptMeshBevelOptions.infer_material_id"></a>

#### infer_material_id

```python
@infer_material_id.setter
def infer_material_id(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.set_material_id"></a>

#### set_material_id

```python
@property
def set_material_id() -> int
```

(int32):  [Read-Write] Material ID to set on the new faces introduced by bevel operation, unless bInferMaterialID=true and non-ambiguous MaterialID can be inferred from adjacent faces

<a id="unreal.GeometryScriptMeshBevelOptions.set_material_id"></a>

#### set_material_id

```python
@set_material_id.setter
def set_material_id(value: int) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.subdivisions"></a>

#### subdivisions

```python
@property
def subdivisions() -> int
```

(int32):  [Read-Write] Number of edge loops added along the bevel faces

<a id="unreal.GeometryScriptMeshBevelOptions.subdivisions"></a>

#### subdivisions

```python
@subdivisions.setter
def subdivisions(value: int) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.round_weight"></a>

#### round_weight

```python
@property
def round_weight() -> float
```

(float):  [Read-Write] Roundness of the bevel. Ignored if Subdivisions = 0.

<a id="unreal.GeometryScriptMeshBevelOptions.round_weight"></a>

#### round_weight

```python
@round_weight.setter
def round_weight(value: float) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.apply_filter_box"></a>

#### apply_filter_box

```python
@property
def apply_filter_box() -> bool
```

(bool):  [Read-Write] If true the set of beveled PolyGroup edges is limited to those that
are fully or partially contained within the (transformed) FilterBox

<a id="unreal.GeometryScriptMeshBevelOptions.apply_filter_box"></a>

#### apply_filter_box

```python
@apply_filter_box.setter
def apply_filter_box(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.filter_box"></a>

#### filter_box

```python
@property
def filter_box() -> Box
```

(Box):  [Read-Write] Bounding Box used for edge filtering

<a id="unreal.GeometryScriptMeshBevelOptions.filter_box"></a>

#### filter_box

```python
@filter_box.setter
def filter_box(value: Box) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.filter_box_transform"></a>

#### filter_box_transform

```python
@property
def filter_box_transform() -> Transform
```

(Transform):  [Read-Write] Transform applied to the FilterBox

<a id="unreal.GeometryScriptMeshBevelOptions.filter_box_transform"></a>

#### filter_box_transform

```python
@filter_box_transform.setter
def filter_box_transform(value: Transform) -> None
```

<a id="unreal.GeometryScriptMeshBevelOptions.fully_contained"></a>

#### fully_contained

```python
@property
def fully_contained() -> bool
```

(bool):  [Read-Write] If true, then only PolyGroup edges that are fully contained within the filter box will be beveled,
otherwise the edge will be beveled if any vertex is within the filter box.

<a id="unreal.GeometryScriptMeshBevelOptions.fully_contained"></a>

#### fully_contained

```python
@fully_contained.setter
def fully_contained(value: bool) -> None
```

<a id="unreal.GeometryScriptMeshBevelSelectionOptions"></a>