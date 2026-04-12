## GetRoadHeatMapParams Objects

```python
class GetRoadHeatMapParams(ResultBase)
```

Get Road Heat Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: RoadHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``road_heat_map_data`` (Array[RoadHeatMapData]):  [Read-Write]
- ``road_heat_map_style`` (RoadHeatMapStyle):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetRoadHeatMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             coord_z_ref: int = 0,
             road_heat_map_style: RoadHeatMapStyle = [
                 "fit", 30.000000, [1.000000, 100.000000],
                 ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"], ["water"]
             ],
             road_heat_map_data: Array[RoadHeatMapData] = []) -> None
```

<a id="unreal.GetRoadHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.GetRoadHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.GetRoadHeatMapParams.road_heat_map_style"></a>

#### road\_heat\_map\_style

```python
@property
def road_heat_map_style() -> RoadHeatMapStyle
```

(RoadHeatMapStyle):  [Read-Write]

<a id="unreal.GetRoadHeatMapParams.road_heat_map_style"></a>

#### road\_heat\_map\_style

```python
@road_heat_map_style.setter
def road_heat_map_style(value: RoadHeatMapStyle) -> None
```

<a id="unreal.GetRoadHeatMapParams.road_heat_map_data"></a>

#### road\_heat\_map\_data

```python
@property
def road_heat_map_data() -> Array[RoadHeatMapData]
```

(Array[RoadHeatMapData]):  [Read-Write]

<a id="unreal.GetRoadHeatMapParams.road_heat_map_data"></a>

#### road\_heat\_map\_data

```python
@road_heat_map_data.setter
def road_heat_map_data(value: Array[RoadHeatMapData]) -> None
```

<a id="unreal.CreateRoadHeatMapsParams"></a>