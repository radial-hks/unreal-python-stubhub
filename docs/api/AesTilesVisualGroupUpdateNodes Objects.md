## AesTilesVisualGroupUpdateNodes Objects

```python
class AesTilesVisualGroupUpdateNodes(AesTilesVisualGroupParam)
```

Aes Tiles Visual Group Update Nodes

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``group_name`` (Name):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``nodes`` (Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisualGroupUpdateNodes.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             nodes: Array[int] = []) -> None
```

<a id="unreal.AesTilesVisualGroupUpdateNodes.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisualGroupUpdateNodes.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisualGroupUpdateName"></a>