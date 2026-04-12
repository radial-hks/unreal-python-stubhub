## UpdateHeatMapParams Objects

```python
class UpdateHeatMapParams(ParamsBase)
```

Update Heat Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: HeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``heat_map_data`` (Array[HeatMapData]):  [Read-Write]
- ``heat_map_style`` (HeatMapStyle):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             coord_z_ref: int = 0,
             coord_z: float = 0.000000,
             heat_map_style: HeatMapStyle = [
                 "fit", 30.000000, [-1000000.000000, 1000000.000000],
                 [1.000000, 100.000000],
                 ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
             ],
             heat_map_data: Array[HeatMapData] = []) -> None
```

<a id="unreal.UpdateHeatMapParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateHeatMapParams.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.UpdateHeatMapParams.heat_map_style"></a>

#### heat\_map\_style

```python
@property
def heat_map_style() -> HeatMapStyle
```

(HeatMapStyle):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.heat_map_style"></a>

#### heat\_map\_style

```python
@heat_map_style.setter
def heat_map_style(value: HeatMapStyle) -> None
```

<a id="unreal.UpdateHeatMapParams.heat_map_data"></a>

#### heat\_map\_data

```python
@property
def heat_map_data() -> Array[HeatMapData]
```

(Array[HeatMapData]):  [Read-Write]

<a id="unreal.UpdateHeatMapParams.heat_map_data"></a>

#### heat\_map\_data

```python
@heat_map_data.setter
def heat_map_data(value: Array[HeatMapData]) -> None
```

<a id="unreal.Polygon_HeatMapClip"></a>