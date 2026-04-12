## DCPNodeLocationParam Objects

```python
class DCPNodeLocationParam(DCPNodeBaseParam)
```

DCPNode Location Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.DCPNodeLocationParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: int = 0,
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPNodeLocationParam.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPNodeLocationParam.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.DCPNodeRotationParam"></a>