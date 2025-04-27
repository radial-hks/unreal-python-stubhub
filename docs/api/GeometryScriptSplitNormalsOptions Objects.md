## GeometryScriptSplitNormalsOptions Objects

```python
class GeometryScriptSplitNormalsOptions(StructBase)
```

Geometry Script Split Normals Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshNormalsFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_layer`` (GeometryScriptGroupLayer):  [Read-Write]
- ``opening_angle_deg`` (float):  [Read-Write]
- ``split_by_face_group`` (bool):  [Read-Write]
- ``split_by_opening_angle`` (bool):  [Read-Write]

<a id="unreal.GeometryScriptSplitNormalsOptions.__init__"></a>

#### __init__

```python
def __init__(split_by_opening_angle: bool = False,
             opening_angle_deg: float = 0.000000,
             split_by_face_group: bool = False,
             group_layer: GeometryScriptGroupLayer = [True, 0]) -> None
```

<a id="unreal.GeometryScriptSplitNormalsOptions.split_by_opening_angle"></a>

#### split_by_opening_angle

```python
@property
def split_by_opening_angle() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSplitNormalsOptions.split_by_opening_angle"></a>

#### split_by_opening_angle

```python
@split_by_opening_angle.setter
def split_by_opening_angle(value: bool) -> None
```

<a id="unreal.GeometryScriptSplitNormalsOptions.opening_angle_deg"></a>

#### opening_angle_deg

```python
@property
def opening_angle_deg() -> float
```

(float):  [Read-Write]

<a id="unreal.GeometryScriptSplitNormalsOptions.opening_angle_deg"></a>

#### opening_angle_deg

```python
@opening_angle_deg.setter
def opening_angle_deg(value: float) -> None
```

<a id="unreal.GeometryScriptSplitNormalsOptions.split_by_face_group"></a>

#### split_by_face_group

```python
@property
def split_by_face_group() -> bool
```

(bool):  [Read-Write]

<a id="unreal.GeometryScriptSplitNormalsOptions.split_by_face_group"></a>

#### split_by_face_group

```python
@split_by_face_group.setter
def split_by_face_group(value: bool) -> None
```

<a id="unreal.GeometryScriptSplitNormalsOptions.group_layer"></a>

#### group_layer

```python
@property
def group_layer() -> GeometryScriptGroupLayer
```

(GeometryScriptGroupLayer):  [Read-Write]

<a id="unreal.GeometryScriptSplitNormalsOptions.group_layer"></a>

#### group_layer

```python
@group_layer.setter
def group_layer(value: GeometryScriptGroupLayer) -> None
```

<a id="unreal.GeometryScriptTangentsOptions"></a>