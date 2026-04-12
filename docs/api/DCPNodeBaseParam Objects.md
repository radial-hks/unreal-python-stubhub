## DCPNodeBaseParam Objects

```python
class DCPNodeBaseParam(ParamsBase)
```

DCPNode Base Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.DCPNodeBaseParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: int = 0) -> None
```

<a id="unreal.DCPNodeBaseParam.node_id"></a>

#### node\_id

```python
@property
def node_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodeBaseParam.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: int) -> None
```

<a id="unreal.GetDCPNodeTransformParam"></a>