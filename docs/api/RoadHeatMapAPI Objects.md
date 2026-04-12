## RoadHeatMapAPI Objects

```python
class RoadHeatMapAPI(ApiClassBase)
```

Road Heat Map API

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPI.h

<a id="unreal.RoadHeatMapAPI.un_filter_road_heat_map_entity"></a>

#### un\_filter\_road\_heat\_map\_entity

```python
def un_filter_road_heat_map_entity(
        un_filter_params: UnRoadHeatMapFilterParam) -> Optional[EidResult]
```

x.un_filter_road_heat_map_entity(un_filter_params) -> EidResult or None
Un Filter Road Heat Map Entity

Args:
    un_filter_params (UnRoadHeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.RoadHeatMapAPI.outline_road_heat_map_entity"></a>

#### outline\_road\_heat\_map\_entity

```python
def outline_road_heat_map_entity(
        params: RoadHeatMapOutlineParam) -> Optional[EidResult]
```

x.outline_road_heat_map_entity(params) -> EidResult or None
Outline Road Heat Map Entity

Args:
    params (RoadHeatMapOutlineParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.RoadHeatMapAPI.modify_road_heat_map"></a>

#### modify\_road\_heat\_map

```python
def modify_road_heat_map(
        modify_road_params: ModifyRoadHeatMapParam) -> Optional[EidResult]
```

x.modify_road_heat_map(modify_road_params) -> EidResult or None
UFUNCTION(BlueprintCallable, Category = "Wdp Scene")
       bool GetRoadHeatMapInfo(const FEidParams& RoadHeatMapEidParms, FGetRoadHeatMapParams& OutResult);

Args:
    modify_road_params (ModifyRoadHeatMapParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.RoadHeatMapAPI.get_road_heat_map_entity"></a>

#### get\_road\_heat\_map\_entity

```python
def get_road_heat_map_entity(
        params: RoadHeatMapInfoParam) -> Optional[RoadEidValueResult]
```

x.get_road_heat_map_entity(params) -> RoadEidValueResult or None
Get Road Heat Map Entity

Args:
    params (RoadHeatMapInfoParam): 

Returns:
    RoadEidValueResult or None: 

    out_result (RoadEidValueResult):

<a id="unreal.RoadHeatMapAPI.filter_road_heat_map_entity"></a>

#### filter\_road\_heat\_map\_entity

```python
def filter_road_heat_map_entity(
        params: RoadHeatMapFilterParam) -> Optional[EidResult]
```

x.filter_road_heat_map_entity(params) -> EidResult or None
Filter Road Heat Map Entity

Args:
    params (RoadHeatMapFilterParam): 

Returns:
    EidResult or None: 

    out_result (EidResult):

<a id="unreal.SectionAPI"></a>