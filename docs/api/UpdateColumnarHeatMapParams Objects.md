## UpdateColumnarHeatMapParams Objects

```python
class UpdateColumnarHeatMapParams(ParamsBase)
```

Update Columnar Heat Map Params

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: ColumnarHeatMapAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``columnar_heat_map_data`` (Array[ColumnarHeatMapData]):  [Read-Write]
- ``columnar_heat_map_style`` (ColumnarHeatMapStyle):  [Read-Write]
- ``coord_z`` (double):  [Read-Write]
- ``coord_z_ref`` (int32):  [Read-Write]
- ``eid`` (str):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             coord_z_ref: int = 0,
             coord_z: float = 0.000000,
             columnar_heat_map_style: ColumnarHeatMapStyle = [
                 "cube", 30.000000, [1.000000, 100.000000], 10.000000,
                 [1.000000, 100.000000], False,
                 ["00ffff", "00ff00", "ffff00", "ff8900", "ff0000"]
             ],
             columnar_heat_map_data: Array[ColumnarHeatMapData] = []) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> int
```

(int32):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: int) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams.coord_z"></a>

#### coord\_z

```python
@property
def coord_z() -> float
```

(double):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.coord_z"></a>

#### coord\_z

```python
@coord_z.setter
def coord_z(value: float) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams.columnar_heat_map_style"></a>

#### columnar\_heat\_map\_style

```python
@property
def columnar_heat_map_style() -> ColumnarHeatMapStyle
```

(ColumnarHeatMapStyle):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.columnar_heat_map_style"></a>

#### columnar\_heat\_map\_style

```python
@columnar_heat_map_style.setter
def columnar_heat_map_style(value: ColumnarHeatMapStyle) -> None
```

<a id="unreal.UpdateColumnarHeatMapParams.columnar_heat_map_data"></a>

#### columnar\_heat\_map\_data

```python
@property
def columnar_heat_map_data() -> Array[ColumnarHeatMapData]
```

(Array[ColumnarHeatMapData]):  [Read-Write]

<a id="unreal.UpdateColumnarHeatMapParams.columnar_heat_map_data"></a>

#### columnar\_heat\_map\_data

```python
@columnar_heat_map_data.setter
def columnar_heat_map_data(value: Array[ColumnarHeatMapData]) -> None
```

<a id="unreal.Polygon_ColumnarHeatMapClip"></a>