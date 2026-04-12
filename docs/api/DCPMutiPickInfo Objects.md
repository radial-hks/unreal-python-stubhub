## DCPMutiPickInfo Objects

```python
class DCPMutiPickInfo(StructBase)
```

DCPMuti Pick Info

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPCommonAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (int64):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPMutiPickInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: int = 0, node_ids: Array[int] = []) -> None
```

<a id="unreal.DCPMutiPickInfo.eid"></a>

#### eid

```python
@property
def eid() -> int
```

(int64):  [Read-Write]

<a id="unreal.DCPMutiPickInfo.eid"></a>

#### eid

```python
@eid.setter
def eid(value: int) -> None
```

<a id="unreal.DCPMutiPickInfo.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPMutiPickInfo.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPMutiPickResult"></a>