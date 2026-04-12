## FenceEntityInfo Objects

```python
class FenceEntityInfo(StructBase)
```

Fence Entity Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``ways`` (Array[FenceWayInfo]):  [Read-Write]

<a id="unreal.FenceEntityInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             ways: Array[FenceWayInfo] = []) -> None
```

<a id="unreal.FenceEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FenceEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.FenceEntityInfo.ways"></a>

#### ways

```python
@property
def ways() -> Array[FenceWayInfo]
```

(Array[FenceWayInfo]):  [Read-Write]

<a id="unreal.FenceEntityInfo.ways"></a>

#### ways

```python
@ways.setter
def ways(value: Array[FenceWayInfo]) -> None
```

<a id="unreal.WaterNodeInfo"></a>