## NodesTrParams Objects

```python
class NodesTrParams(EidParams)
```

Nodes Tr Params

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: WdpInstanceEntityAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``nodes_transform_info`` (Array[NodesTrInfo]):  [Read-Write]

<a id="unreal.NodesTrParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(nodes_transform_info: Array[NodesTrInfo] = []) -> None
```

<a id="unreal.NodesTrParams.nodes_transform_info"></a>

#### nodes\_transform\_info

```python
@property
def nodes_transform_info() -> Array[NodesTrInfo]
```

(Array[NodesTrInfo]):  [Read-Write]

<a id="unreal.NodesTrParams.nodes_transform_info"></a>

#### nodes\_transform\_info

```python
@nodes_transform_info.setter
def nodes_transform_info(value: Array[NodesTrInfo]) -> None
```

<a id="unreal.FocusToNodesParams"></a>