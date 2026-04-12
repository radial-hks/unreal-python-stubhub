## EarthRoadModelerJunctionFragment Objects

```python
class EarthRoadModelerJunctionFragment(EarthEntityFragment)
```

Earth Road Modeler Junction Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``junction_circle_center`` (Vector):  [Read-Write] 子资产引用
- ``junction_circle_radius`` (float):  [Read-Write] 子资产引用
- ``junction_connection_infos`` (Array[EarthJunctionConnectionInfo]):  [Read-Write] 子资产引用
- ``junction_level`` (int32):  [Read-Write] HashValueParameter
- ``junction_module_definition`` (Map[EarthJunctionLaneType, EarthModuleAsset]):  [Read-Write] 键为路口特殊模块种类，值为路口特殊模块定义
- ``junction_road_module_definition`` (Map[EarthModelerRoadLaneType, EarthModuleAsset]):  [Read-Write] 键为路口道路模块种类，值为路口道路通用模块定义
- ``junction_round_lane_info`` (EarthModelerLaneProfileFragment):  [Read-Write] 子资产引用
- ``junction_surface_asset`` (EarthSubAssetInfo):  [Read-Write] 子资产引用
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``outer_type`` (str):  [Read-Write]
- ``road_junction_builder_type`` (EarthRoadJunctionBuilderType):  [Read-Write] Junction生成类型
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthRoadModelerJunctionFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        lod_config: Map[int, int] = {},
        road_junction_builder_type:
    EarthRoadJunctionBuilderType = EarthRoadJunctionBuilderType.REGULAR,
        junction_connection_infos: Array[EarthJunctionConnectionInfo] = [],
        junction_surface_asset: EarthSubAssetInfo = [
            None,
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
        ],
        junction_module_definition: Map[EarthJunctionLaneType,
                                        EarthModuleAsset] = {},
        junction_road_module_definition: Map[EarthModelerRoadLaneType,
                                             EarthModuleAsset] = {},
        junction_circle_radius: float = 0.000000,
        junction_circle_center: Vector = [0.000000, 0.000000, 0.000000],
        junction_round_lane_info: EarthModelerLaneProfileFragment = [
            "None", [], [], False, False
        ],
        junction_level: int = 0,
        outer_type: str = "") -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.lod_config"></a>

#### lod\_config

```python
@property
def lod_config() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用

<a id="unreal.EarthRoadModelerJunctionFragment.lod_config"></a>

#### lod\_config

```python
@lod_config.setter
def lod_config(value: Map[int, int]) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.road_junction_builder_type"></a>

#### road\_junction\_builder\_type

```python
@property
def road_junction_builder_type() -> EarthRoadJunctionBuilderType
```

(EarthRoadJunctionBuilderType):  [Read-Write] Junction生成类型

<a id="unreal.EarthRoadModelerJunctionFragment.road_junction_builder_type"></a>

#### road\_junction\_builder\_type

```python
@road_junction_builder_type.setter
def road_junction_builder_type(value: EarthRoadJunctionBuilderType) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_connection_infos"></a>

#### junction\_connection\_infos

```python
@property
def junction_connection_infos() -> Array[EarthJunctionConnectionInfo]
```

(Array[EarthJunctionConnectionInfo]):  [Read-Write] 子资产引用

<a id="unreal.EarthRoadModelerJunctionFragment.junction_connection_infos"></a>

#### junction\_connection\_infos

```python
@junction_connection_infos.setter
def junction_connection_infos(
        value: Array[EarthJunctionConnectionInfo]) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_surface_asset"></a>

#### junction\_surface\_asset

```python
@property
def junction_surface_asset() -> EarthSubAssetInfo
```

(EarthSubAssetInfo):  [Read-Write] 子资产引用

<a id="unreal.EarthRoadModelerJunctionFragment.junction_surface_asset"></a>

#### junction\_surface\_asset

```python
@junction_surface_asset.setter
def junction_surface_asset(value: EarthSubAssetInfo) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_module_definition"></a>

#### junction\_module\_definition

```python
@property
def junction_module_definition(
) -> Map[EarthJunctionLaneType, EarthModuleAsset]
```

(Map[EarthJunctionLaneType, EarthModuleAsset]):  [Read-Write] 键为路口特殊模块种类，值为路口特殊模块定义

<a id="unreal.EarthRoadModelerJunctionFragment.junction_module_definition"></a>

#### junction\_module\_definition

```python
@junction_module_definition.setter
def junction_module_definition(
        value: Map[EarthJunctionLaneType, EarthModuleAsset]) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_road_module_definition"></a>

#### junction\_road\_module\_definition

```python
@property
def junction_road_module_definition(
) -> Map[EarthModelerRoadLaneType, EarthModuleAsset]
```

(Map[EarthModelerRoadLaneType, EarthModuleAsset]):  [Read-Write] 键为路口道路模块种类，值为路口道路通用模块定义

<a id="unreal.EarthRoadModelerJunctionFragment.junction_road_module_definition"></a>

#### junction\_road\_module\_definition

```python
@junction_road_module_definition.setter
def junction_road_module_definition(
        value: Map[EarthModelerRoadLaneType, EarthModuleAsset]) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_circle_radius"></a>

#### junction\_circle\_radius

```python
@property
def junction_circle_radius() -> float
```

(float):  [Read-Write] 子资产引用

<a id="unreal.EarthRoadModelerJunctionFragment.junction_circle_radius"></a>

#### junction\_circle\_radius

```python
@junction_circle_radius.setter
def junction_circle_radius(value: float) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_circle_center"></a>

#### junction\_circle\_center

```python
@property
def junction_circle_center() -> Vector
```

(Vector):  [Read-Write] 子资产引用

<a id="unreal.EarthRoadModelerJunctionFragment.junction_circle_center"></a>

#### junction\_circle\_center

```python
@junction_circle_center.setter
def junction_circle_center(value: Vector) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_round_lane_info"></a>

#### junction\_round\_lane\_info

```python
@property
def junction_round_lane_info() -> EarthModelerLaneProfileFragment
```

(EarthModelerLaneProfileFragment):  [Read-Write] 子资产引用

<a id="unreal.EarthRoadModelerJunctionFragment.junction_round_lane_info"></a>

#### junction\_round\_lane\_info

```python
@junction_round_lane_info.setter
def junction_round_lane_info(value: EarthModelerLaneProfileFragment) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.junction_level"></a>

#### junction\_level

```python
@property
def junction_level() -> int
```

(int32):  [Read-Write] HashValueParameter

<a id="unreal.EarthRoadModelerJunctionFragment.junction_level"></a>

#### junction\_level

```python
@junction_level.setter
def junction_level(value: int) -> None
```

<a id="unreal.EarthRoadModelerJunctionFragment.outer_type"></a>

#### outer\_type

```python
@property
def outer_type() -> str
```

(str):  [Read-Write]

<a id="unreal.EarthRoadModelerJunctionFragment.outer_type"></a>

#### outer\_type

```python
@outer_type.setter
def outer_type(value: str) -> None
```

<a id="unreal.EarthJunctionOverrideFragment"></a>