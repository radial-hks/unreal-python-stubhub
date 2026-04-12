## ColumnarHeatMapAPI Objects

```python
class ColumnarHeatMapAPI(ApiClassBase)
```

Columnar Heat Map API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPI.h

<a id="unreal.ColumnarHeatMapAPI.un_filter_columnar_heat_map_entity"></a>

#### un\_filter\_columnar\_heat\_map\_entity

```python
def un_filter_columnar_heat_map_entity(
        un_filter_params: UnColumnarHeatMapFilterParam) -> Optional[EidResult]
```

x.un_filter_columnar_heat_map_entity(un_filter_params) -> EidResult or None
Un Filter Columnar Heat Map Entity

Args:
    un_filter_params (UnColumnarHeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.ColumnarHeatMapAPI.un_clip_columnar_heat_map_entity"></a>

#### un\_clip\_columnar\_heat\_map\_entity

```python
def un_clip_columnar_heat_map_entity(
        un_clip_heat_map_param: EidParams) -> Optional[EidResult]
```

x.un_clip_columnar_heat_map_entity(un_clip_heat_map_param) -> EidResult or None
Un Clip Columnar Heat Map Entity

Args:
    un_clip_heat_map_param (EidParams): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.ColumnarHeatMapAPI.outline_columnar_heat_map_entity"></a>

#### outline\_columnar\_heat\_map\_entity

```python
def outline_columnar_heat_map_entity(
        params: ColumnarHeatMapOutlineParam) -> Optional[EidResult]
```

x.outline_columnar_heat_map_entity(params) -> EidResult or None
Outline Columnar Heat Map Entity

Args:
    params (ColumnarHeatMapOutlineParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.ColumnarHeatMapAPI.modify_columnar_heat_map"></a>

#### modify\_columnar\_heat\_map

```python
def modify_columnar_heat_map(
        params: ModifyHeatMapParam) -> Optional[EidResult]
```

x.modify_columnar_heat_map(params) -> EidResult or None
/ APIs

Args:
    params (ModifyHeatMapParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.ColumnarHeatMapAPI.get_columnar_heat_map_entity"></a>

#### get\_columnar\_heat\_map\_entity

```python
def get_columnar_heat_map_entity(
        params: ColumnarHeatMapInfoParam) -> Optional[ColumnarEidValueResult]
```

x.get_columnar_heat_map_entity(params) -> ColumnarEidValueResult or None
Get Columnar Heat Map Entity

Args:
    params (ColumnarHeatMapInfoParam): 

Returns:
    ColumnarEidValueResult or None: 

    out_result (ColumnarEidValueResult):

<a id="unreal.ColumnarHeatMapAPI.filter_columnar_heat_map_entity"></a>

#### filter\_columnar\_heat\_map\_entity

```python
def filter_columnar_heat_map_entity(
        params: ColumnarHeatMapFilterParam) -> Optional[EidResult]
```

x.filter_columnar_heat_map_entity(params) -> EidResult or None
Filter Columnar Heat Map Entity

Args:
    params (ColumnarHeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.ColumnarHeatMapAPI.clip_columnar_heat_map_entity"></a>

#### clip\_columnar\_heat\_map\_entity

```python
def clip_columnar_heat_map_entity(
        clip_heat_map_param: ClipColumnarHeatMapParam) -> Optional[EidResult]
```

x.clip_columnar_heat_map_entity(clip_heat_map_param) -> EidResult or None
UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
       bool GetColumnarHeatMapInfo(const FEidParams& ParticleEidParms, FGetColumnarHeatMapParams& OutResult);

Args:
    clip_heat_map_param (ClipColumnarHeatMapParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.CompassAPI"></a>