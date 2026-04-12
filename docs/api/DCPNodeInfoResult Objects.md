## DCPNodeInfoResult Objects

```python
class DCPNodeInfoResult(ResultBase)
```

DCPNode Info Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``message`` (str):  [Read-Write]
- ``nodes`` (Array[DCPNodeSingleInfoResult]):  [Read-Write]
- ``root_node`` (DCPNodeSingleInfoResult):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPNodeInfoResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             root_node: DCPNodeSingleInfoResult = [
                 -1, -1, -1, "none", False, "", [[], [], []], False
             ],
             nodes: Array[DCPNodeSingleInfoResult] = []) -> None
```

<a id="unreal.DCPNodeInfoResult.root_node"></a>

#### root\_node

```python
@property
def root_node() -> DCPNodeSingleInfoResult
```

(DCPNodeSingleInfoResult):  [Read-Write]

<a id="unreal.DCPNodeInfoResult.root_node"></a>

#### root\_node

```python
@root_node.setter
def root_node(value: DCPNodeSingleInfoResult) -> None
```

<a id="unreal.DCPNodeInfoResult.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[DCPNodeSingleInfoResult]
```

(Array[DCPNodeSingleInfoResult]):  [Read-Write]

<a id="unreal.DCPNodeInfoResult.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[DCPNodeSingleInfoResult]) -> None
```

<a id="unreal.DCPNodePropertyResult"></a>