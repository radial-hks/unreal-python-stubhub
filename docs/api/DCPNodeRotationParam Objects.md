## DCPNodeRotationParam Objects

```python
class DCPNodeRotationParam(DCPNodeBaseParam)
```

DCPNode Rotation Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]

<a id="unreal.DCPNodeRotationParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: int = 0,
             rotation: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPNodeRotationParam.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.DCPNodeRotationParam.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.DCPNodeScaleParam"></a>