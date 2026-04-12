## FloorWayInfo Objects

```python
class FloorWayInfo(StructBase)
```

Floor Way Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``align_z`` (bool):  [Read-Write]
- ``corner_radius`` (float):  [Read-Write]
- ``corner_split_seg_num`` (int32):  [Read-Write]
- ``inner_brightness`` (float):  [Read-Write]
- ``inner_height`` (float):  [Read-Write]
- ``inner_mat_name`` (AssetName):  [Read-Write]
- ``inner_normal`` (float):  [Read-Write]
- ``inner_roughness`` (float):  [Read-Write]
- ``inner_uv_transform`` (Transform):  [Read-Write]
- ``inverse_normal`` (bool):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``nodes`` (Array[FloorNodeInfo]):  [Read-Write]
- ``outer_brightness`` (float):  [Read-Write]
- ``outer_height`` (float):  [Read-Write]
- ``outer_mat_name`` (AssetName):  [Read-Write]
- ``outer_normal`` (float):  [Read-Write]
- ``outer_roughness`` (float):  [Read-Write]
- ``outer_uv_transform`` (Transform):  [Read-Write]
- ``outer_width`` (float):  [Read-Write]
- ``use_global_rounded_corner`` (bool):  [Read-Write]

<a id="unreal.FloorWayInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             inner_mat_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             outer_mat_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             inner_height: float = 0.000000,
             outer_height: float = 0.000000,
             outer_width: float = 0.000000,
             corner_radius: float = 0.000000,
             corner_split_seg_num: int = 0,
             outer_uv_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                              [-0.000000, 0.000000, 0.000000],
                                              [1.000000, 1.000000, 1.000000]],
             inner_uv_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                              [-0.000000, 0.000000, 0.000000],
                                              [1.000000, 1.000000, 1.000000]],
             use_global_rounded_corner: bool = False,
             align_z: bool = False,
             inverse_normal: bool = False,
             inner_roughness: float = 0.000000,
             outer_roughness: float = 0.000000,
             inner_normal: float = 0.000000,
             outer_normal: float = 0.000000,
             inner_brightness: float = 0.000000,
             outer_brightness: float = 0.000000,
             nodes: Array[FloorNodeInfo] = []) -> None
```

<a id="unreal.FloorWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FloorWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.FloorWayInfo.inner_mat_name"></a>

#### inner\_mat\_name

```python
@property
def inner_mat_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_mat_name"></a>

#### inner\_mat\_name

```python
@inner_mat_name.setter
def inner_mat_name(value: AssetName) -> None
```

<a id="unreal.FloorWayInfo.outer_mat_name"></a>

#### outer\_mat\_name

```python
@property
def outer_mat_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_mat_name"></a>

#### outer\_mat\_name

```python
@outer_mat_name.setter
def outer_mat_name(value: AssetName) -> None
```

<a id="unreal.FloorWayInfo.inner_height"></a>

#### inner\_height

```python
@property
def inner_height() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_height"></a>

#### inner\_height

```python
@inner_height.setter
def inner_height(value: float) -> None
```

<a id="unreal.FloorWayInfo.outer_height"></a>

#### outer\_height

```python
@property
def outer_height() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_height"></a>

#### outer\_height

```python
@outer_height.setter
def outer_height(value: float) -> None
```

<a id="unreal.FloorWayInfo.outer_width"></a>

#### outer\_width

```python
@property
def outer_width() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_width"></a>

#### outer\_width

```python
@outer_width.setter
def outer_width(value: float) -> None
```

<a id="unreal.FloorWayInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.FloorWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@property
def corner_split_seg_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.FloorWayInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@corner_split_seg_num.setter
def corner_split_seg_num(value: int) -> None
```

<a id="unreal.FloorWayInfo.outer_uv_transform"></a>

#### outer\_uv\_transform

```python
@property
def outer_uv_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_uv_transform"></a>

#### outer\_uv\_transform

```python
@outer_uv_transform.setter
def outer_uv_transform(value: Transform) -> None
```

<a id="unreal.FloorWayInfo.inner_uv_transform"></a>

#### inner\_uv\_transform

```python
@property
def inner_uv_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_uv_transform"></a>

#### inner\_uv\_transform

```python
@inner_uv_transform.setter
def inner_uv_transform(value: Transform) -> None
```

<a id="unreal.FloorWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@property
def use_global_rounded_corner() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FloorWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@use_global_rounded_corner.setter
def use_global_rounded_corner(value: bool) -> None
```

<a id="unreal.FloorWayInfo.align_z"></a>

#### align\_z

```python
@property
def align_z() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FloorWayInfo.align_z"></a>

#### align\_z

```python
@align_z.setter
def align_z(value: bool) -> None
```

<a id="unreal.FloorWayInfo.inverse_normal"></a>

#### inverse\_normal

```python
@property
def inverse_normal() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FloorWayInfo.inverse_normal"></a>

#### inverse\_normal

```python
@inverse_normal.setter
def inverse_normal(value: bool) -> None
```

<a id="unreal.FloorWayInfo.inner_roughness"></a>

#### inner\_roughness

```python
@property
def inner_roughness() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_roughness"></a>

#### inner\_roughness

```python
@inner_roughness.setter
def inner_roughness(value: float) -> None
```

<a id="unreal.FloorWayInfo.outer_roughness"></a>

#### outer\_roughness

```python
@property
def outer_roughness() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_roughness"></a>

#### outer\_roughness

```python
@outer_roughness.setter
def outer_roughness(value: float) -> None
```

<a id="unreal.FloorWayInfo.inner_normal"></a>

#### inner\_normal

```python
@property
def inner_normal() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_normal"></a>

#### inner\_normal

```python
@inner_normal.setter
def inner_normal(value: float) -> None
```

<a id="unreal.FloorWayInfo.outer_normal"></a>

#### outer\_normal

```python
@property
def outer_normal() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_normal"></a>

#### outer\_normal

```python
@outer_normal.setter
def outer_normal(value: float) -> None
```

<a id="unreal.FloorWayInfo.inner_brightness"></a>

#### inner\_brightness

```python
@property
def inner_brightness() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.inner_brightness"></a>

#### inner\_brightness

```python
@inner_brightness.setter
def inner_brightness(value: float) -> None
```

<a id="unreal.FloorWayInfo.outer_brightness"></a>

#### outer\_brightness

```python
@property
def outer_brightness() -> float
```

(float):  [Read-Write]

<a id="unreal.FloorWayInfo.outer_brightness"></a>

#### outer\_brightness

```python
@outer_brightness.setter
def outer_brightness(value: float) -> None
```

<a id="unreal.FloorWayInfo.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[FloorNodeInfo]
```

(Array[FloorNodeInfo]):  [Read-Write]

<a id="unreal.FloorWayInfo.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[FloorNodeInfo]) -> None
```

<a id="unreal.FloorMeshInfo"></a>