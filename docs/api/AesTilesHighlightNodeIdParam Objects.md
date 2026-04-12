## AesTilesHighlightNodeIdParam Objects

```python
class AesTilesHighlightNodeIdParam(AesTilesHighlightParam)
```

Aes Tiles Highlight Node Id Param

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``aes_tiles_eid`` (int64):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``highlight`` (bool):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]
- ``style_name`` (Name):  [Read-Write]

<a id="unreal.AesTilesHighlightNodeIdParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(aes_tiles_eid: int = 0,
             highlight: bool = False,
             style_name: Name = "None",
             node_ids: Array[int] = []) -> None
```

<a id="unreal.AesTilesHighlightNodeIdParam.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.AesTilesHighlightNodeIdParam.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.AesTilesHighlightLayerParam"></a>