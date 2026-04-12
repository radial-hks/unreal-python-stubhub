## DCPModelActiveParams Objects

```python
class DCPModelActiveParams(EidParams)
```

DCPModel Active Params

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPModelAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``status`` (bool):  [Read-Write]

<a id="unreal.DCPModelActiveParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(status: bool = False) -> None
```

<a id="unreal.DCPModelActiveParams.status"></a>

#### status

```python
@property
def status() -> bool
```

(bool):  [Read-Write]

<a id="unreal.DCPModelActiveParams.status"></a>

#### status

```python
@status.setter
def status(value: bool) -> None
```

<a id="unreal.DcpActiveFinishEventParam"></a>