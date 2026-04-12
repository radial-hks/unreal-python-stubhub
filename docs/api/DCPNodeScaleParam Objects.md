## DCPNodeScaleParam Objects

```python
class DCPNodeScaleParam(DCPNodeBaseParam)
```

DCPNode Scale Param

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]

<a id="unreal.DCPNodeScaleParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(node_id: int = 0,
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPNodeScaleParam.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPNodeScaleParam.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.DCPSectionTransformParams"></a>