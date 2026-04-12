## SetGeoLayerOffsetParams Objects

```python
class SetGeoLayerOffsetParams(EidParams)
```

Set Geo Layer Offset Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (Eid):  [Read-Write]
- ``geo_layer_offset`` (Vector):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.SetGeoLayerOffsetParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        geo_layer_offset: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.SetGeoLayerOffsetParams.geo_layer_offset"></a>

#### geo\_layer\_offset

```python
@property
def geo_layer_offset() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SetGeoLayerOffsetParams.geo_layer_offset"></a>

#### geo\_layer\_offset

```python
@geo_layer_offset.setter
def geo_layer_offset(value: Vector) -> None
```

<a id="unreal.GetGeoLayerLocationParams"></a>