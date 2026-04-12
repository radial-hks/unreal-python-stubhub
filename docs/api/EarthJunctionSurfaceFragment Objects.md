## EarthJunctionSurfaceFragment Objects

```python
class EarthJunctionSurfaceFragment(EarthPropertyFragment)
```

Earth Junction Surface Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset_width`` (int32):  [Read-Write]
- ``resample_num`` (int32):  [Read-Write]
- ``road_connection_infos`` (Array[int32]):  [Read-Write] 连接道路的收尾
- ``road_surface_material`` (EarthMaterialInfo):  [Read-Write] 路面材质路径
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthJunctionSurfaceFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             road_surface_material: EarthMaterialInfo = [
                 "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000,
                 [0, 0]
             ],
             road_connection_infos: Array[int] = [],
             resample_num: int = 0,
             offset_width: int = 0) -> None
```

<a id="unreal.EarthJunctionSurfaceFragment.road_surface_material"></a>

#### road\_surface\_material

```python
@property
def road_surface_material() -> EarthMaterialInfo
```

(EarthMaterialInfo):  [Read-Write] 路面材质路径

<a id="unreal.EarthJunctionSurfaceFragment.road_surface_material"></a>

#### road\_surface\_material

```python
@road_surface_material.setter
def road_surface_material(value: EarthMaterialInfo) -> None
```

<a id="unreal.EarthJunctionSurfaceFragment.road_connection_infos"></a>

#### road\_connection\_infos

```python
@property
def road_connection_infos() -> Array[int]
```

(Array[int32]):  [Read-Write] 连接道路的收尾

<a id="unreal.EarthJunctionSurfaceFragment.road_connection_infos"></a>

#### road\_connection\_infos

```python
@road_connection_infos.setter
def road_connection_infos(value: Array[int]) -> None
```

<a id="unreal.EarthJunctionSurfaceFragment.resample_num"></a>

#### resample\_num

```python
@property
def resample_num() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthJunctionSurfaceFragment.resample_num"></a>

#### resample\_num

```python
@resample_num.setter
def resample_num(value: int) -> None
```

<a id="unreal.EarthJunctionSurfaceFragment.offset_width"></a>

#### offset\_width

```python
@property
def offset_width() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthJunctionSurfaceFragment.offset_width"></a>

#### offset\_width

```python
@offset_width.setter
def offset_width(value: int) -> None
```

<a id="unreal.EarthZoneLaneData"></a>