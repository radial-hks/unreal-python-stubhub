## FenceNodeInfo Objects

```python
class FenceNodeInfo(StructBase)
```

BP_FenceTool

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``corner_radius`` (float):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]

<a id="unreal.FenceNodeInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             corner_radius: float = 0.000000) -> None
```

<a id="unreal.FenceNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FenceNodeInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.FenceNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.FenceNodeInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.FenceWayInfo"></a>