## DCPNodePickResult Objects

```python
class DCPNodePickResult(EventArgsBase)
```

DCPNode Pick Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``gis_coord`` (str):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]
- ``ue_coord`` (str):  [Read-Write]

<a id="unreal.DCPNodePickResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             node_id: int = 0,
             ue_coord: str = "",
             gis_coord: str = "") -> None
```

<a id="unreal.DCPNodePickResult.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePickResult.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.DCPNodePickResult.node_id"></a>

#### node\_id

```python
@property
def node_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.DCPNodePickResult.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: int) -> None
```

<a id="unreal.DCPNodePickResult.ue_coord"></a>

#### ue\_coord

```python
@property
def ue_coord() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePickResult.ue_coord"></a>

#### ue\_coord

```python
@ue_coord.setter
def ue_coord(value: str) -> None
```

<a id="unreal.DCPNodePickResult.gis_coord"></a>

#### gis\_coord

```python
@property
def gis_coord() -> str
```

(str):  [Read-Write]

<a id="unreal.DCPNodePickResult.gis_coord"></a>

#### gis\_coord

```python
@gis_coord.setter
def gis_coord(value: str) -> None
```

<a id="unreal.DCPNodeMouseEventArgs"></a>