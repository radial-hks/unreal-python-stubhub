## RiverNodeInfo Objects

```python
class RiverNodeInfo(StructBase)
```

BP_RiverMesh

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``corner_radius`` (float):  [Read-Write]
- ``corner_split_seg_num`` (int32):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``river_width`` (float):  [Read-Write]

<a id="unreal.RiverNodeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             corner_radius: float = 0.000000,
             corner_split_seg_num: int = 0,
             river_width: float = 0.000000) -> None
```

<a id="unreal.RiverNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.RiverNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.RiverNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.RiverNodeInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@property
def corner_split_seg_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.RiverNodeInfo.corner_split_seg_num"></a>

#### corner\_split\_seg\_num

```python
@corner_split_seg_num.setter
def corner_split_seg_num(value: int) -> None
```

<a id="unreal.RiverNodeInfo.river_width"></a>

#### river\_width

```python
@property
def river_width() -> float
```

(float):  [Read-Write]

<a id="unreal.RiverNodeInfo.river_width"></a>

#### river\_width

```python
@river_width.setter
def river_width(value: float) -> None
```

<a id="unreal.RiverWayInfo"></a>