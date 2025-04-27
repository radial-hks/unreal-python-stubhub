## GeometryScriptBoneInfo Objects

```python
class GeometryScriptBoneInfo(StructBase)
```

Geometry Script Bone Info

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: MeshBoneWeightFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] Bone color.
- ``index`` (int32):  [Read-Write] Index of the bone in the skeletal hierarchy.
- ``local_transform`` (Transform):  [Read-Write] Local/bone space reference transform.
- ``name`` (Name):  [Read-Write] Bone name.
- ``parent_index`` (int32):  [Read-Write] Parent bone index.
- ``world_transform`` (Transform):  [Read-Write] Global/world space reference transform.

<a id="unreal.GeometryScriptBoneInfo.__init__"></a>

#### __init__

```python
def __init__(
        index: int = 0,
        name: Name = "None",
        parent_index: int = 0,
        local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                      [-0.000000, 0.000000, 0.000000],
                                      [1.000000, 1.000000, 1.000000]],
        world_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                      [-0.000000, 0.000000, 0.000000],
                                      [1.000000, 1.000000, 1.000000]],
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GeometryScriptBoneInfo.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Write] Index of the bone in the skeletal hierarchy.

<a id="unreal.GeometryScriptBoneInfo.index"></a>

#### index

```python
@index.setter
def index(value: int) -> None
```

<a id="unreal.GeometryScriptBoneInfo.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] Bone name.

<a id="unreal.GeometryScriptBoneInfo.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.GeometryScriptBoneInfo.parent_index"></a>

#### parent_index

```python
@property
def parent_index() -> int
```

(int32):  [Read-Write] Parent bone index.

<a id="unreal.GeometryScriptBoneInfo.parent_index"></a>

#### parent_index

```python
@parent_index.setter
def parent_index(value: int) -> None
```

<a id="unreal.GeometryScriptBoneInfo.local_transform"></a>

#### local_transform

```python
@property
def local_transform() -> Transform
```

(Transform):  [Read-Write] Local/bone space reference transform.

<a id="unreal.GeometryScriptBoneInfo.local_transform"></a>

#### local_transform

```python
@local_transform.setter
def local_transform(value: Transform) -> None
```

<a id="unreal.GeometryScriptBoneInfo.world_transform"></a>

#### world_transform

```python
@property
def world_transform() -> Transform
```

(Transform):  [Read-Write] Global/world space reference transform.

<a id="unreal.GeometryScriptBoneInfo.world_transform"></a>

#### world_transform

```python
@world_transform.setter
def world_transform(value: Transform) -> None
```

<a id="unreal.GeometryScriptBoneInfo.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] Bone color.

<a id="unreal.GeometryScriptBoneInfo.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.GeometryScriptCopyBonesFromMeshOptions"></a>