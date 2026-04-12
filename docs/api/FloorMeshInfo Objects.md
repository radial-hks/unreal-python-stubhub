## FloorMeshInfo Objects

```python
class FloorMeshInfo(StructBase)
```

Floor Mesh Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``ways`` (Array[FloorWayInfo]):  [Read-Write]

<a id="unreal.FloorMeshInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             ways: Array[FloorWayInfo] = []) -> None
```

<a id="unreal.FloorMeshInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FloorMeshInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.FloorMeshInfo.ways"></a>

#### ways

```python
@property
def ways() -> Array[FloorWayInfo]
```

(Array[FloorWayInfo]):  [Read-Write]

<a id="unreal.FloorMeshInfo.ways"></a>

#### ways

```python
@ways.setter
def ways(value: Array[FloorWayInfo]) -> None
```

<a id="unreal.FenceNodeInfo"></a>