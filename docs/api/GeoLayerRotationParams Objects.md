## GeoLayerRotationParams Objects

```python
class GeoLayerRotationParams(ParamsBase)
```

Geo Layer Rotation Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``geo_layer_rotation`` (Vector):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.GeoLayerRotationParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        eid: str = "",
        geo_layer_rotation: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GeoLayerRotationParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.GeoLayerRotationParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.GeoLayerRotationParams.geo_layer_rotation"></a>

#### geo\_layer\_rotation

```python
@property
def geo_layer_rotation() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GeoLayerRotationParams.geo_layer_rotation"></a>

#### geo\_layer\_rotation

```python
@geo_layer_rotation.setter
def geo_layer_rotation(value: Vector) -> None
```

<a id="unreal.SetGeoLayerLocationParams"></a>