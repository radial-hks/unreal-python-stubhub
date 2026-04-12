## GetGeoLayerLocationParams Objects

```python
class GetGeoLayerLocationParams(EidResult)
```

Get Geo Layer Location Params

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPIParamsDefine.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``geo_layer_location`` (Vector):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetGeoLayerLocationParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        message: str = "",
        scene_change_info: WdpSceneChangeInfo = [[], [], []],
        success: bool = False,
        geo_layer_location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GetGeoLayerLocationParams.geo_layer_location"></a>

#### geo\_layer\_location

```python
@property
def geo_layer_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.GetGeoLayerLocationParams.geo_layer_location"></a>

#### geo\_layer\_location

```python
@geo_layer_location.setter
def geo_layer_location(value: Vector) -> None
```

<a id="unreal.SetVisibleParams"></a>