## RiverWayInfo Objects

```python
class RiverWayInfo(StructBase)
```

River Way Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closed`` (bool):  [Read-Write]
- ``corner_radius`` (float):  [Read-Write]
- ``corner_split_seg_num`` (int32):  [Read-Write]
- ``inverse_normal`` (bool):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``merge_length`` (float):  [Read-Write]
- ``nodes`` (Array[RiverNodeInfo]):  [Read-Write]
- ``ripple_scale`` (float):  [Read-Write]
- ``river_body_height`` (float):  [Read-Write]
- ``river_width`` (float):  [Read-Write]
- ``transparent_depth`` (float):  [Read-Write]
- ``use_global_rounded_corner`` (bool):  [Read-Write]
- ``use_global_width`` (bool):  [Read-Write]
- ``water_color`` (str):  [Read-Write]
- ``water_mat_name`` (AssetName):  [Read-Write] RiverMatParameter
- ``water_transparency`` (float):  [Read-Write]
- ``wave_height`` (float):  [Read-Write]
- ``wave_rotate`` (float):  [Read-Write]
- ``wave_speed_x`` (float):  [Read-Write]

<a id="unreal.RiverWayInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             merge_length: float = 0.000000,
             river_width: float = 0.000000,
             river_body_height: float = 0.000000,
             corner_radius: float = 0.000000,
             corner_split_seg_num: int = 0,
             inverse_normal: bool = False,
             use_global_rounded_corner: bool = False,
             use_global_width: bool = False,
             closed: bool = False,
             water_mat_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             ripple_scale: float = 0.000000,
             wave_rotate: float = 0.000000,
             wave_speed_x: float = 0.000000,
             water_color: str = "",
             wave_height: float = 0.000000,
             transparent_depth: float = 0.000000,
             water_transparency: float = 0.000000,
             nodes: Array[RiverNodeInfo] = []) -> None
```

<a id="unreal.RiverWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RiverWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.RiverWayInfo.merge_length"></a>

#### merge\_length

```python
@property
def merge_length() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.merge_length"></a>

#### merge\_length

```python
@merge_length.setter
def merge_length(value: float) -> None
```

<a id="unreal.RiverWayInfo.river_width"></a>

#### river\_width

```python
@property
def river_width() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.river_width"></a>

#### river\_width

```python
@river_width.setter
def river_width(value: float) -> None
```

<a id="unreal.RiverWayInfo.river_body_height"></a>

#### river\_body\_height

```python
@property
def river_body_height() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.river_body_height"></a>

#### river\_body\_height

```python
@river_body_height.setter
def river_body_height(value: float) -> None
```

<a id="unreal.RiverWayInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.RiverWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@property
def corner_split_seg_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.RiverWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@corner_split_seg_num.setter
def corner_split_seg_num(value: int) -> None
```

<a id="unreal.RiverWayInfo.inverse_normal"></a>

#### inverse\_normal

```python
@property
def inverse_normal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RiverWayInfo.inverse_normal"></a>

#### inverse\_normal

```python
@inverse_normal.setter
def inverse_normal(value: bool) -> None
```

<a id="unreal.RiverWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@property
def use_global_rounded_corner() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RiverWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@use_global_rounded_corner.setter
def use_global_rounded_corner(value: bool) -> None
```

<a id="unreal.RiverWayInfo.use_global_width"></a>

#### use\_global\_width

```python
@property
def use_global_width() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RiverWayInfo.use_global_width"></a>

#### use\_global\_width

```python
@use_global_width.setter
def use_global_width(value: bool) -> None
```

<a id="unreal.RiverWayInfo.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RiverWayInfo.closed"></a>

#### closed

```python
@closed.setter
def closed(value: bool) -> None
```

<a id="unreal.RiverWayInfo.water_mat_name"></a>

#### water\_mat\_name

```python
@property
def water_mat_name() -> AssetName
```

(AssetName):  [Read-Write] RiverMatParameter

<a id="unreal.RiverWayInfo.water_mat_name"></a>

#### water\_mat\_name

```python
@water_mat_name.setter
def water_mat_name(value: AssetName) -> None
```

<a id="unreal.RiverWayInfo.ripple_scale"></a>

#### ripple\_scale

```python
@property
def ripple_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.ripple_scale"></a>

#### ripple\_scale

```python
@ripple_scale.setter
def ripple_scale(value: float) -> None
```

<a id="unreal.RiverWayInfo.wave_rotate"></a>

#### wave\_rotate

```python
@property
def wave_rotate() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.wave_rotate"></a>

#### wave\_rotate

```python
@wave_rotate.setter
def wave_rotate(value: float) -> None
```

<a id="unreal.RiverWayInfo.wave_speed_x"></a>

#### wave\_speed\_x

```python
@property
def wave_speed_x() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.wave_speed_x"></a>

#### wave\_speed\_x

```python
@wave_speed_x.setter
def wave_speed_x(value: float) -> None
```

<a id="unreal.RiverWayInfo.water_color"></a>

#### water\_color

```python
@property
def water_color() -> str
```

(str):  [Read-Write]

<a id="unreal.RiverWayInfo.water_color"></a>

#### water\_color

```python
@water_color.setter
def water_color(value: str) -> None
```

<a id="unreal.RiverWayInfo.wave_height"></a>

#### wave\_height

```python
@property
def wave_height() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.wave_height"></a>

#### wave\_height

```python
@wave_height.setter
def wave_height(value: float) -> None
```

<a id="unreal.RiverWayInfo.transparent_depth"></a>

#### transparent\_depth

```python
@property
def transparent_depth() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.transparent_depth"></a>

#### transparent\_depth

```python
@transparent_depth.setter
def transparent_depth(value: float) -> None
```

<a id="unreal.RiverWayInfo.water_transparency"></a>

#### water\_transparency

```python
@property
def water_transparency() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverWayInfo.water_transparency"></a>

#### water\_transparency

```python
@water_transparency.setter
def water_transparency(value: float) -> None
```

<a id="unreal.RiverWayInfo.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[RiverNodeInfo]
```

(Array[RiverNodeInfo]):  [Read-Write]

<a id="unreal.RiverWayInfo.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[RiverNodeInfo]) -> None
```

<a id="unreal.RiverMeshInfo"></a>