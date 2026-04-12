## DCPNodeSingleInfoResult Objects

```python
class DCPNodeSingleInfoResult(ResultBase)
```

DCPNode Single Info Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``father_id`` (int32):  [Read-Write]
- ``level`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]
- ``title`` (str):  [Read-Write]
- ``visibility`` (bool):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             level: int = 0,
             father_id: int = 0,
             node_id: int = 0,
             title: str = "",
             visibility: bool = False) -> None
```

<a id="unreal.DCPNodeSingleInfoResult.level"></a>

#### level

```python
@property
def level() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.level"></a>

#### level

```python
@level.setter
def level(value: int) -> None
```

<a id="unreal.DCPNodeSingleInfoResult.father_id"></a>

#### father\_id

```python
@property
def father_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.father_id"></a>

#### father\_id

```python
@father_id.setter
def father_id(value: int) -> None
```

<a id="unreal.DCPNodeSingleInfoResult.node_id"></a>

#### node\_id

```python
@property
def node_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: int) -> None
```

<a id="unreal.DCPNodeSingleInfoResult.title"></a>

#### title

```python
@property
def title() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.title"></a>

#### title

```python
@title.setter
def title(value: str) -> None
```

<a id="unreal.DCPNodeSingleInfoResult.visibility"></a>

#### visibility

```python
@property
def visibility() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPNodeSingleInfoResult.visibility"></a>

#### visibility

```python
@visibility.setter
def visibility(value: bool) -> None
```

<a id="unreal.DCPNodeInfoResult"></a>