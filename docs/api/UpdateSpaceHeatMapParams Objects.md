## UpdateSpaceHeatMapParams Objects

```python
class UpdateSpaceHeatMapParams(ParamsBase)
```

Update Space Heat Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: SpaceHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``space_heat_map_data`` (Array[SpaceHeatMapData]):  [Read-Write]
- ``space_heat_map_style`` (SpaceHeatMapStyle):  [Read-Write]

<a id="unreal.UpdateSpaceHeatMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             coord_z_ref: int = 0,
             space_heat_map_style: SpaceHeatMapStyle = [
                 30.000000, [1.000000, 100.000000],
                 ["000000", "000303", "051900", "593A00", "FF0000"]
             ],
             space_heat_map_data: Array[SpaceHeatMapData] = []) -> None
```

<a id="unreal.UpdateSpaceHeatMapParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateSpaceHeatMapParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateSpaceHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateSpaceHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateSpaceHeatMapParams.space_heat_map_style"></a>

#### space\_heat\_map\_style

```python
@property
def space_heat_map_style() -> SpaceHeatMapStyle
```

(SpaceHeatMapStyle):  [Read-Write]

<a id="unreal.UpdateSpaceHeatMapParams.space_heat_map_style"></a>

#### space\_heat\_map\_style

```python
@space_heat_map_style.setter
def space_heat_map_style(value: SpaceHeatMapStyle) -> None
```

<a id="unreal.UpdateSpaceHeatMapParams.space_heat_map_data"></a>

#### space\_heat\_map\_data

```python
@property
def space_heat_map_data() -> Array[SpaceHeatMapData]
```

(Array[SpaceHeatMapData]):  [Read-Write]

<a id="unreal.UpdateSpaceHeatMapParams.space_heat_map_data"></a>

#### space\_heat\_map\_data

```python
@space_heat_map_data.setter
def space_heat_map_data(value: Array[SpaceHeatMapData]) -> None
```

<a id="unreal.Text3DStyle"></a>