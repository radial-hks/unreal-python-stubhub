## GetSpaceHeatMapParams Objects

```python
class GetSpaceHeatMapParams(ResultBase)
```

Get Space Heat Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SpaceHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``space_heat_map_data`` (Array[SpaceHeatMapData]):  [Read-Write]
- ``space_heat_map_style`` (SpaceHeatMapStyle):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.GetSpaceHeatMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             coord_z_ref: int = 0,
             space_heat_map_style: SpaceHeatMapStyle = [
                 30.000000, [1.000000, 100.000000],
                 ["000000", "000303", "051900", "593A00", "FF0000"]
             ],
             space_heat_map_data: Array[SpaceHeatMapData] = []) -> None
```

<a id="unreal.GetSpaceHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.GetSpaceHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.GetSpaceHeatMapParams.space_heat_map_style"></a>

#### space\_heat\_map\_style

```python
@property
def space_heat_map_style() -> SpaceHeatMapStyle
```

(SpaceHeatMapStyle):  [Read-Write]

<a id="unreal.GetSpaceHeatMapParams.space_heat_map_style"></a>

#### space\_heat\_map\_style

```python
@space_heat_map_style.setter
def space_heat_map_style(value: SpaceHeatMapStyle) -> None
```

<a id="unreal.GetSpaceHeatMapParams.space_heat_map_data"></a>

#### space\_heat\_map\_data

```python
@property
def space_heat_map_data() -> Array[SpaceHeatMapData]
```

(Array[SpaceHeatMapData]):  [Read-Write]

<a id="unreal.GetSpaceHeatMapParams.space_heat_map_data"></a>

#### space\_heat\_map\_data

```python
@space_heat_map_data.setter
def space_heat_map_data(value: Array[SpaceHeatMapData]) -> None
```

<a id="unreal.CreateSpaceHeatMapsParams"></a>