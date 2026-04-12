## AesTilesVisibilityNodesParam Objects

```python
class AesTilesVisibilityNodesParam(AesTilesVisualApiParamBase)
```

Aes Tiles Visibility Nodes Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``nodes`` (Array[int32]):  [Read-Write]
- ``visible`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityNodesParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             nodes: Array[int] = [],
             visible: bool = False) -> None
```

<a id="unreal.AesTilesVisibilityNodesParam.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesVisibilityNodesParam.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[int]) -> None
```

<a id="unreal.AesTilesVisibilityNodesParam.visible"></a>

#### visible

```python
@property
def visible() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityNodesParam.visible"></a>

#### visible

```python
@visible.setter
def visible(value: bool) -> None
```

<a id="unreal.AesTilesVisibilityGroupAddParam"></a>