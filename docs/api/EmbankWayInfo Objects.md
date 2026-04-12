## EmbankWayInfo Objects

```python
class EmbankWayInfo(StructBase)
```

Embank Way Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_height`` (float):  [Read-Write]
- ``base_mesh_type_name`` (AssetName):  [Read-Write]
- ``base_width`` (float):  [Read-Write]
- ``corner_radius`` (float):  [Read-Write]
- ``corner_split_seg_num`` (int32):  [Read-Write]
- ``fence_height`` (float):  [Read-Write]
- ``fence_mesh_type_name`` (AssetName):  [Read-Write]
- ``fence_off_set`` (float):  [Read-Write]
- ``fence_width`` (float):  [Read-Write]
- ``is_closed`` (bool):  [Read-Write]
- ``is_reverse_side`` (bool):  [Read-Write]
- ``is_two_side`` (bool):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``nodes`` (Array[EmbankNodeInfo]):  [Read-Write]
- ``side_mesh_type_name`` (AssetName):  [Read-Write]
- ``side_width`` (float):  [Read-Write]
- ``side_width_scale`` (float):  [Read-Write]
- ``use_global_base_width`` (bool):  [Read-Write]
- ``use_global_rounded_corner`` (bool):  [Read-Write]
- ``use_global_side_width_scale`` (bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             is_reverse_side: bool = False,
             is_closed: bool = False,
             is_two_side: bool = False,
             base_mesh_type_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             side_mesh_type_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             fence_mesh_type_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             fence_width: float = 0.000000,
             fence_height: float = 0.000000,
             fence_off_set: float = 0.000000,
             side_width: float = 0.000000,
             corner_radius: float = 0.000000,
             corner_split_seg_num: int = 0,
             base_height: float = 0.000000,
             base_width: float = 0.000000,
             side_width_scale: float = 0.000000,
             use_global_base_width: bool = False,
             use_global_side_width_scale: bool = False,
             use_global_rounded_corner: bool = False,
             nodes: Array[EmbankNodeInfo] = []) -> None
```

<a id="unreal.EmbankWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.EmbankWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.EmbankWayInfo.is_reverse_side"></a>

#### is\_reverse\_side

```python
@property
def is_reverse_side() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.is_reverse_side"></a>

#### is\_reverse\_side

```python
@is_reverse_side.setter
def is_reverse_side(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.is_closed"></a>

#### is\_closed

```python
@property
def is_closed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.is_closed"></a>

#### is\_closed

```python
@is_closed.setter
def is_closed(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.is_two_side"></a>

#### is\_two\_side

```python
@property
def is_two_side() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.is_two_side"></a>

#### is\_two\_side

```python
@is_two_side.setter
def is_two_side(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.base_mesh_type_name"></a>

#### base\_mesh\_type\_name

```python
@property
def base_mesh_type_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.EmbankWayInfo.base_mesh_type_name"></a>

#### base\_mesh\_type\_name

```python
@base_mesh_type_name.setter
def base_mesh_type_name(value: AssetName) -> None
```

<a id="unreal.EmbankWayInfo.side_mesh_type_name"></a>

#### side\_mesh\_type\_name

```python
@property
def side_mesh_type_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.EmbankWayInfo.side_mesh_type_name"></a>

#### side\_mesh\_type\_name

```python
@side_mesh_type_name.setter
def side_mesh_type_name(value: AssetName) -> None
```

<a id="unreal.EmbankWayInfo.fence_mesh_type_name"></a>

#### fence\_mesh\_type\_name

```python
@property
def fence_mesh_type_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.EmbankWayInfo.fence_mesh_type_name"></a>

#### fence\_mesh\_type\_name

```python
@fence_mesh_type_name.setter
def fence_mesh_type_name(value: AssetName) -> None
```

<a id="unreal.EmbankWayInfo.fence_width"></a>

#### fence\_width

```python
@property
def fence_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.fence_width"></a>

#### fence\_width

```python
@fence_width.setter
def fence_width(value: float) -> None
```

<a id="unreal.EmbankWayInfo.fence_height"></a>

#### fence\_height

```python
@property
def fence_height() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.fence_height"></a>

#### fence\_height

```python
@fence_height.setter
def fence_height(value: float) -> None
```

<a id="unreal.EmbankWayInfo.fence_off_set"></a>

#### fence\_off\_set

```python
@property
def fence_off_set() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.fence_off_set"></a>

#### fence\_off\_set

```python
@fence_off_set.setter
def fence_off_set(value: float) -> None
```

<a id="unreal.EmbankWayInfo.side_width"></a>

#### side\_width

```python
@property
def side_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.side_width"></a>

#### side\_width

```python
@side_width.setter
def side_width(value: float) -> None
```

<a id="unreal.EmbankWayInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.EmbankWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@property
def corner_split_seg_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EmbankWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@corner_split_seg_num.setter
def corner_split_seg_num(value: int) -> None
```

<a id="unreal.EmbankWayInfo.base_height"></a>

#### base\_height

```python
@property
def base_height() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.base_height"></a>

#### base\_height

```python
@base_height.setter
def base_height(value: float) -> None
```

<a id="unreal.EmbankWayInfo.base_width"></a>

#### base\_width

```python
@property
def base_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.base_width"></a>

#### base\_width

```python
@base_width.setter
def base_width(value: float) -> None
```

<a id="unreal.EmbankWayInfo.side_width_scale"></a>

#### side\_width\_scale

```python
@property
def side_width_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankWayInfo.side_width_scale"></a>

#### side\_width\_scale

```python
@side_width_scale.setter
def side_width_scale(value: float) -> None
```

<a id="unreal.EmbankWayInfo.use_global_base_width"></a>

#### use\_global\_base\_width

```python
@property
def use_global_base_width() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.use_global_base_width"></a>

#### use\_global\_base\_width

```python
@use_global_base_width.setter
def use_global_base_width(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.use_global_side_width_scale"></a>

#### use\_global\_side\_width\_scale

```python
@property
def use_global_side_width_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.use_global_side_width_scale"></a>

#### use\_global\_side\_width\_scale

```python
@use_global_side_width_scale.setter
def use_global_side_width_scale(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@property
def use_global_rounded_corner() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EmbankWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@use_global_rounded_corner.setter
def use_global_rounded_corner(value: bool) -> None
```

<a id="unreal.EmbankWayInfo.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[EmbankNodeInfo]
```

(Array[EmbankNodeInfo]):  [Read-Write]

<a id="unreal.EmbankWayInfo.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[EmbankNodeInfo]) -> None
```

<a id="unreal.EmbankEntityInfo"></a>