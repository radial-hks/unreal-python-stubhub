## HeatMapAPI Objects

```python
class HeatMapAPI(ApiClassBase)
```

Heat Map API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPI.h

<a id="unreal.HeatMapAPI.un_filter_heat_map_entity"></a>

#### un\_filter\_heat\_map\_entity

```python
def un_filter_heat_map_entity(
        un_filter_params: UnHeatMapFilterParam) -> Optional[EidResult]
```

x.un_filter_heat_map_entity(un_filter_params) -> EidResult or None
Un Filter Heat Map Entity

Args:
    un_filter_params (UnHeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HeatMapAPI.un_clip_heat_map_entity"></a>

#### un\_clip\_heat\_map\_entity

```python
def un_clip_heat_map_entity(
        un_clip_heat_map_param: EidParams) -> Optional[EidResult]
```

x.un_clip_heat_map_entity(un_clip_heat_map_param) -> EidResult or None
Un Clip Heat Map Entity

Args:
    un_clip_heat_map_param (EidParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HeatMapAPI.outline_heat_map_entity"></a>

#### outline\_heat\_map\_entity

```python
def outline_heat_map_entity(
        params: HeatMapOutlineParam) -> Optional[EidResult]
```

x.outline_heat_map_entity(params) -> EidResult or None
Outline Heat Map Entity

Args:
    params (HeatMapOutlineParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HeatMapAPI.modify_heat_map"></a>

#### modify\_heat\_map

```python
def modify_heat_map(params: ModifyHeatMapParam) -> Optional[EidResult]
```

x.modify_heat_map(params) -> EidResult or None
APIs

Args:
    params (ModifyHeatMapParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HeatMapAPI.get_heat_map_entity"></a>

#### get\_heat\_map\_entity

```python
def get_heat_map_entity(params: HeatMapInfoParam) -> Optional[EidValueResult]
```

x.get_heat_map_entity(params) -> EidValueResult or None
Get Heat Map Entity

Args:
    params (HeatMapInfoParam): 

Returns:
    EidValueResult or None: 

    out_result (EidValueResult):

<a id="unreal.HeatMapAPI.filter_heat_map_entity"></a>

#### filter\_heat\_map\_entity

```python
def filter_heat_map_entity(params: HeatMapFilterParam) -> Optional[EidResult]
```

x.filter_heat_map_entity(params) -> EidResult or None
Filter Heat Map Entity

Args:
    params (HeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HeatMapAPI.clip_heat_map_entity"></a>

#### clip\_heat\_map\_entity

```python
def clip_heat_map_entity(
        clip_heat_map_param: ClipHeatMapParam) -> Optional[EidResult]
```

x.clip_heat_map_entity(clip_heat_map_param) -> EidResult or None
UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
               bool CreateHeatMapEntity(const FCreateHeatMapParams& CreateEntityParams, FEidResult& OutResult);

       UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
               bool CreateHeatMapEntity_Batch(const FCreateHeatMapParams_Batch& CreateEntityParams, FEidArrayResult& OutResult);

       UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
               bool UpdateHeatMapEntity(const FUpdateHeatMapParams& UpdateParams, FResultBase& OutResult);

       UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
               bool GetHeatMapInfo(const FEidParams& HeatMapEidParms, FGetHeatMapParams& OutResult);

Args:
    clip_heat_map_param (ClipHeatMapParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.HighlightAreaAPI"></a>