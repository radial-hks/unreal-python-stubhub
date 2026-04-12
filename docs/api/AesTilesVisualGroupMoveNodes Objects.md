## AesTilesVisualGroupMoveNodes Objects

```python
class AesTilesVisualGroupMoveNodes(AesTilesVisualGroupParam)
```

Aes Tiles Visual Group Move Nodes

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
- ``target_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesVisualGroupMoveNodes.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             group_name: Name = "None",
             target_name: Name = "None",
             nodes: Array[int] = []) -> None
```

<a id="unreal.AesTilesVisualGroupMoveNodes.target_name"></a>

#### target\_name

```python
@property
def target_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesTilesVisualGroupMoveNodes.target_name"></a>

#### target\_name

```python
@target_name.setter
def target_name(value: Name) -> None
```

<a id="unreal.AesTilesVisualGroupMoveNodes.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisualGroupMoveNodes.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisualGroupVisibility"></a>