## TreeSamplerEntityInfo Objects

```python
class TreeSamplerEntityInfo(StructBase)
```

Tree Sampler Entity Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``ways`` (Array[TreeSamplerWayInfo]):  [Read-Write]

<a id="unreal.TreeSamplerEntityInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             ways: Array[TreeSamplerWayInfo] = []) -> None
```

<a id="unreal.TreeSamplerEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.TreeSamplerEntityInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.TreeSamplerEntityInfo.ways"></a>

#### ways

```python
@property
def ways() -> Array[TreeSamplerWayInfo]
```

(Array[TreeSamplerWayInfo]):  [Read-Write]

<a id="unreal.TreeSamplerEntityInfo.ways"></a>

#### ways

```python
@ways.setter
def ways(value: Array[TreeSamplerWayInfo]) -> None
```

<a id="unreal.RiverNodeInfo"></a>