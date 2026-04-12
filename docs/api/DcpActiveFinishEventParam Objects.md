## DcpActiveFinishEventParam Objects

```python
class DcpActiveFinishEventParam(EventArgsBase)
```

Dcp Active Finish Event Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPModelAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active`` (bool):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DcpActiveFinishEventParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(success: bool = False,
             active: bool = False,
             eid: str = "") -> None
```

<a id="unreal.DcpActiveFinishEventParam.success"></a>

#### success

```python
@property
def success() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DcpActiveFinishEventParam.success"></a>

#### success

```python
@success.setter
def success(value: bool) -> None
```

<a id="unreal.DcpActiveFinishEventParam.active"></a>

#### active

```python
@property
def active() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DcpActiveFinishEventParam.active"></a>

#### active

```python
@active.setter
def active(value: bool) -> None
```

<a id="unreal.DcpActiveFinishEventParam.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.DcpActiveFinishEventParam.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.NodeOutlineStyleParam"></a>