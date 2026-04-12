## AesTilesVisibilityGroupResult Objects

```python
class AesTilesVisibilityGroupResult(ResultBase)
```

Aes Tiles Visibility Group Result

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: AesTilesAPI
- **File**: AesTilesVisualAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``group_to_nodes`` (Map[Name, VisualGroupNodes]):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             group_to_nodes: Map[Name, VisualGroupNodes] = {}) -> None
```

<a id="unreal.AesTilesVisibilityGroupResult.group_to_nodes"></a>

#### group\_to\_nodes

```python
@property
def group_to_nodes() -> Map[Name, VisualGroupNodes]
```

(Map[Name, VisualGroupNodes]):  [Read-Write]

<a id="unreal.AesTilesVisibilityGroupResult.group_to_nodes"></a>

#### group\_to\_nodes

```python
@group_to_nodes.setter
def group_to_nodes(value: Map[Name, VisualGroupNodes]) -> None
```

<a id="unreal.AesTilesVisibilityLayerStatus"></a>