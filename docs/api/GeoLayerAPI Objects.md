## GeoLayerAPI Objects

```python
class GeoLayerAPI(ApiClassBase)
```

Geo Layer API

**C++ Source:**

- **Plugin**: GISDataAPI
- **Module**: MagicGISAPI
- **File**: GeoLayerAPI.h

<a id="unreal.GeoLayerAPI.update_geo_layer"></a>

#### update\_geo\_layer

```python
def update_geo_layer(params: GeoLayerUpdateParams) -> Optional[ResultBase]
```

x.update_geo_layer(params) -> ResultBase or None
Update Geo Layer

Args:
    params (GeoLayerUpdateParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_local_georeference"></a>

#### set\_local\_georeference

```python
def set_local_georeference(
        params: LocalGeoReferenceParams) -> Optional[ResultBase]
```

x.set_local_georeference(params) -> ResultBase or None
Set Local Georeference

Args:
    params (LocalGeoReferenceParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_layer_visibility"></a>

#### set\_layer\_visibility

```python
def set_layer_visibility(params: SetVisibleParams) -> Optional[EidResult]
```

x.set_layer_visibility(params) -> EidResult or None
Set Layer Visibility

Args:
    params (SetVisibleParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.GeoLayerAPI.set_layer_global_setting"></a>

#### set\_layer\_global\_setting

```python
def set_layer_global_setting(
        params: LayerGlobalSettingParams) -> Optional[ResultBase]
```

x.set_layer_global_setting(params) -> ResultBase or None
Set Layer Global Setting

Args:
    params (LayerGlobalSettingParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_rotation"></a>

#### set\_geo\_layer\_rotation

```python
def set_geo_layer_rotation(
        params: GeoLayerRotationParams) -> Optional[ResultBase]
```

x.set_geo_layer_rotation(params) -> ResultBase or None
Set Geo Layer Rotation

Args:
    params (GeoLayerRotationParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_out_line"></a>

#### set\_geo\_layer\_out\_line

```python
def set_geo_layer_out_line(
        params: SetGeoLayerOutLineParams) -> Optional[ResultBase]
```

x.set_geo_layer_out_line(params) -> ResultBase or None
Set Geo Layer Out Line

Args:
    params (SetGeoLayerOutLineParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_offset"></a>

#### set\_geo\_layer\_offset

```python
def set_geo_layer_offset(
        params: SetGeoLayerOffsetParams) -> Optional[ResultBase]
```

x.set_geo_layer_offset(params) -> ResultBase or None
Set Geo Layer Offset

Args:
    params (SetGeoLayerOffsetParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_location"></a>

#### set\_geo\_layer\_location

```python
def set_geo_layer_location(
        params: SetGeoLayerLocationParams) -> Optional[ResultBase]
```

x.set_geo_layer_location(params) -> ResultBase or None
Set Geo Layer Location

Args:
    params (SetGeoLayerLocationParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_highlight"></a>

#### set\_geo\_layer\_highlight

```python
def set_geo_layer_highlight(
        params: SetGeoLayerHighlightParams) -> Optional[ResultBase]
```

x.set_geo_layer_highlight(params) -> ResultBase or None
Set Geo Layer Highlight

Args:
    params (SetGeoLayerHighlightParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.set_geo_layer_height"></a>

#### set\_geo\_layer\_height

```python
def set_geo_layer_height(params: GeoLayerHeightParams) -> Optional[ResultBase]
```

x.set_geo_layer_height(params) -> ResultBase or None
Set Geo Layer Height

Args:
    params (GeoLayerHeightParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.run_geo_layer_action"></a>

#### run\_geo\_layer\_action

```python
def run_geo_layer_action(params: GeoLayerActionParams) -> Optional[ResultBase]
```

x.run_geo_layer_action(params) -> ResultBase or None
Run Geo Layer Action

Args:
    params (GeoLayerActionParams): 

Returns:
    ResultBase or None: 

    out_result (ResultBase):

<a id="unreal.GeoLayerAPI.process_feature_clicked"></a>

#### process\_feature\_clicked

```python
def process_feature_clicked(feature_id: int,
                            view_model: MagicGISViewModelInterface,
                            basic_info: str) -> None
```

x.process_feature_clicked(feature_id, view_model, basic_info) -> None
Process Feature Clicked

Args:
    feature_id (int64): 
    view_model (MagicGISViewModelInterface): 
    basic_info (str):

<a id="unreal.GeoLayerAPI.on_geo_layer_entity_finished_event"></a>

#### on\_geo\_layer\_entity\_finished\_event

```python
def on_geo_layer_entity_finished_event(succes: bool) -> None
```

x.on_geo_layer_entity_finished_event(succes) -> None
On Geo Layer Entity Finished Event

Args:
    succes (bool):

<a id="unreal.GeoLayerAPI.get_geo_layer_location"></a>

#### get\_geo\_layer\_location

```python
def get_geo_layer_location(
        params: EidParams) -> Optional[GetGeoLayerLocationParams]
```

x.get_geo_layer_location(params) -> GetGeoLayerLocationParams or None
Get Geo Layer Location

Args:
    params (EidParams): 

Returns:
    GetGeoLayerLocationParams or None: 

    out_result (GetGeoLayerLocationParams):

<a id="unreal.GeoLayerAPI.get_geo_layer_info"></a>

#### get\_geo\_layer\_info

```python
def get_geo_layer_info(params: EidParams) -> Optional[GeoLayerInfoParams]
```

x.get_geo_layer_info(params) -> GeoLayerInfoParams or None
Get Geo Layer Info

Args:
    params (EidParams): 

Returns:
    GeoLayerInfoParams or None: 

    out_result (GeoLayerInfoParams):

<a id="unreal.GeoLayerAPI.create_geo_layer_entity"></a>

#### create\_geo\_layer\_entity

```python
def create_geo_layer_entity(
        params: GeoLayerCreateParams) -> Optional[EidResult]
```

x.create_geo_layer_entity(params) -> EidResult or None
APIs

Args:
    params (GeoLayerCreateParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.GeoLayerBlueLibrary"></a>