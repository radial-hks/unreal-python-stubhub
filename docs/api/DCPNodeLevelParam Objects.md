## DCPNodeLevelParam Objects

```python
class DCPNodeLevelParam(DCPNodeBaseParam)
```

DCPNode Level Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``level`` (int32):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.DCPNodeLevelParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: int = 0, level: int = 0) -> None
```

<a id="unreal.DCPNodeLevelParam.level"></a>

#### level

```python
@property
def level() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodeLevelParam.level"></a>

#### level

```python
@level.setter
def level(value: int) -> None
```

<a id="unreal.DCPNodeSingleInfoResult"></a>