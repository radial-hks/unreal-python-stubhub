## SetGeoLayerLocationParams Objects

```python
class SetGeoLayerLocationParams(EidParams)
```

Set Geo Layer Location Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``geo_layer_location`` (Vector):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.SetGeoLayerLocationParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        geo_layer_location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.SetGeoLayerLocationParams.geo_layer_location"></a>

#### geo\_layer\_location

```python
@property
def geo_layer_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SetGeoLayerLocationParams.geo_layer_location"></a>

#### geo\_layer\_location

```python
@geo_layer_location.setter
def geo_layer_location(value: Vector) -> None
```

<a id="unreal.SetGeoLayerOffsetParams"></a>