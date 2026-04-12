## EmbankNodeInfo Objects

```python
class EmbankNodeInfo(StructBase)
```

BP_EmBankmentTool

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_width`` (float):  [Read-Write]
- ``corner_radius`` (float):  [Read-Write]
- ``corner_split_seg_num`` (int32):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``side_width_scale`` (float):  [Read-Write]

<a id="unreal.EmbankNodeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             corner_radius: float = 0.000000,
             corner_split_seg_num: int = 0,
             base_width: float = 0.000000,
             side_width_scale: float = 0.000000) -> None
```

<a id="unreal.EmbankNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.EmbankNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.EmbankNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.EmbankNodeInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@property
def corner_split_seg_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EmbankNodeInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@corner_split_seg_num.setter
def corner_split_seg_num(value: int) -> None
```

<a id="unreal.EmbankNodeInfo.base_width"></a>

#### base\_width

```python
@property
def base_width() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankNodeInfo.base_width"></a>

#### base\_width

```python
@base_width.setter
def base_width(value: float) -> None
```

<a id="unreal.EmbankNodeInfo.side_width_scale"></a>

#### side\_width\_scale

```python
@property
def side_width_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.EmbankNodeInfo.side_width_scale"></a>

#### side\_width\_scale

```python
@side_width_scale.setter
def side_width_scale(value: float) -> None
```

<a id="unreal.EmbankWayInfo"></a>