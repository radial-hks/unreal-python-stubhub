## LocalGeoReferenceParams Objects

```python
class LocalGeoReferenceParams(ParamsBase)
```

Local Geo Reference Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_reference`` (Vector2D):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.LocalGeoReferenceParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(geo_reference: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.LocalGeoReferenceParams.geo_reference"></a>

#### geo\_reference

```python
@property
def geo_reference() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.LocalGeoReferenceParams.geo_reference"></a>

#### geo\_reference

```python
@geo_reference.setter
def geo_reference(value: Vector2D) -> None
```

<a id="unreal.GeoLayerHeightParams"></a>