## AesRoadLaneAssetTagData Objects

```python
class AesRoadLaneAssetTagData(StructBase)
```

道路资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesRoadLaneAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``affect_terrain`` (bool):  [Read-Write] 是否压地形
- ``assets_array`` (Array[AesRoadLaneAssetInfo]):  [Read-Write] 默认资产模板
- ``build_end_mesh`` (bool):  [Read-Write]
- ``build_start_mesh`` (bool):  [Read-Write] 收尾端缩进长度
- ``build_traffic_light`` (bool):  [Read-Write] 道路是否生成交通信号灯
- ``builder_type`` (BuilderType):  [Read-Write]
- ``chamfer_corner`` (bool):  [Read-Write] 点是否倒角
- ``chamfer_length`` (float):  [Read-Write] 切角长度
- ``closed_loop`` (bool):  [Read-Write] 是否为封闭曲线
- ``end_biking_width`` (Vector2f):  [Read-Write]
- ``end_emergency_width`` (Vector2f):  [Read-Write]
- ``end_extension`` (float):  [Read-Write]
- ``end_guardrail_width`` (Vector2f):  [Read-Write]
- ``end_lane_width`` (Vector2f):  [Read-Write]
- ``end_lanes`` (IntPoint):  [Read-Write]
- ``end_median_width`` (Vector2f):  [Read-Write]
- ``end_parking_width`` (Vector2f):  [Read-Write]
- ``end_shoulder_width`` (Vector2f):  [Read-Write]
- ``end_sidewalk_width`` (Vector2f):  [Read-Write]
- ``end_tan`` (Vector):  [Read-Write]
- ``end_width`` (Vector2f):  [Read-Only]
- ``f_class`` (str):  [Read-Write] 道路类型
- ``guide_meshes`` (Map[Name, AesMeshData]):  [Read-Write] 箭头引用序列
- ``junction_prefab_id`` (str):  [Read-Write] 指定路口PrefabID
- ``keep_reference_line_centered`` (bool):  [Read-Write] 是否保证参考线位于路面正中间
- ``keep_tan_value`` (bool):  [Read-Write] 是否改变起始点Tan值
- ``lane_x_direction`` (Array[LaneDirection]):  [Read-Write] 车道X转向方向
- ``lane_y_direction`` (Array[LaneDirection]):  [Read-Write] 车道Y转向方向
- ``level`` (int32):  [Read-Write] 道路总宽度
- ``resample_type`` (SplineResampleType):  [Read-Write] 样条线重采样类型
- ``reverse`` (bool):  [Read-Write] 是否调转曲线前进方向
- ``road_surface_material_path`` (SoftObjectPath):  [Read-Write] 路面材质路径
- ``side`` (DrivingDirection):  [Read-Write] 道路行驶方向
- ``spline_point_type`` (SplinePointType):  [Read-Write] 样条线点位类型
- ``start_biking_width`` (Vector2f):  [Read-Write] 自行车宽度
- ``start_emergency_width`` (Vector2f):  [Read-Write] 应急车道宽度
- ``start_extension`` (float):  [Read-Write] 收尾端缩进长度
- ``start_guardrail_width`` (Vector2f):  [Read-Write] 护栏宽度
- ``start_lane_width`` (Vector2f):  [Read-Write] 车道路宽度
- ``start_lanes`` (IntPoint):  [Read-Write] 左右车道数
- ``start_median_width`` (Vector2f):  [Read-Write] 中央隔离带宽度
- ``start_parking_width`` (Vector2f):  [Read-Write] 停车道路宽度
- ``start_shoulder_width`` (Vector2f):  [Read-Write] 路肩宽度
- ``start_sidewalk_width`` (Vector2f):  [Read-Write] 人行道宽度
- ``start_tan`` (Vector):  [Read-Write]
- ``start_width`` (Vector2f):  [Read-Only] 道路总宽度
- ``two_side`` (bool):  [Read-Write] 是否生成双边

<a id="unreal.AesRoadLaneAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        builder_type: BuilderType = BuilderType.LANE,
        closed_loop: bool = False,
        reverse: bool = False,
        two_side: bool = False,
        affect_terrain: bool = False,
        spline_point_type: SplinePointType = SplinePointType.LINEAR,
        resample_type: SplineResampleType = SplineResampleType.INTERPOLATING,
        f_class: str = "",
        side: DrivingDirection = DrivingDirection.RIGHT,
        start_lanes: IntPoint = [0, 0],
        end_lanes: IntPoint = [0, 0],
        start_lane_width: Vector2f = [0.000000, 0.000000],
        end_lane_width: Vector2f = [0.000000, 0.000000],
        start_width: Vector2f = [0.000000, 0.000000],
        end_width: Vector2f = [0.000000, 0.000000],
        level: int = 0,
        keep_reference_line_centered: bool = False,
        keep_tan_value: bool = False,
        end_tan: Vector = [0.000000, 0.000000, 0.000000],
        start_tan: Vector = [0.000000, 0.000000, 0.000000],
        start_guardrail_width: Vector2f = [0.000000, 0.000000],
        end_guardrail_width: Vector2f = [0.000000, 0.000000],
        start_emergency_width: Vector2f = [0.000000, 0.000000],
        end_emergency_width: Vector2f = [0.000000, 0.000000],
        start_shoulder_width: Vector2f = [0.000000, 0.000000],
        end_shoulder_width: Vector2f = [0.000000, 0.000000],
        start_biking_width: Vector2f = [0.000000, 0.000000],
        end_biking_width: Vector2f = [0.000000, 0.000000],
        start_parking_width: Vector2f = [0.000000, 0.000000],
        end_parking_width: Vector2f = [0.000000, 0.000000],
        start_sidewalk_width: Vector2f = [0.000000, 0.000000],
        end_sidewalk_width: Vector2f = [0.000000, 0.000000],
        start_median_width: Vector2f = [0.000000, 0.000000],
        end_median_width: Vector2f = [0.000000, 0.000000],
        start_extension: float = 0.000000,
        end_extension: float = 0.000000,
        build_start_mesh: bool = False,
        build_end_mesh: bool = False,
        chamfer_corner: bool = False,
        chamfer_length: float = 0.000000,
        lane_x_direction: Array[LaneDirection] = [],
        lane_y_direction: Array[LaneDirection] = [],
        assets_array: Array[AesRoadLaneAssetInfo] = [],
        guide_meshes: Map[Name, AesMeshData] = {},
        build_traffic_light: bool = False,
        junction_prefab_id: str = "",
        road_surface_material_path: SoftObjectPath = [""]) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.builder_type"></a>

#### builder\_type

```python
@property
def builder_type() -> BuilderType
```

(BuilderType):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.builder_type"></a>

#### builder\_type

```python
@builder_type.setter
def builder_type(value: BuilderType) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.closed_loop"></a>

#### closed\_loop

```python
@property
def closed_loop() -> bool
```

(bool):  [Read-Write] 是否为封闭曲线

<a id="unreal.AesRoadLaneAssetTagData.closed_loop"></a>

#### closed\_loop

```python
@closed_loop.setter
def closed_loop(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] 是否调转曲线前进方向

<a id="unreal.AesRoadLaneAssetTagData.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.two_side"></a>

#### two\_side

```python
@property
def two_side() -> bool
```

(bool):  [Read-Write] 是否生成双边

<a id="unreal.AesRoadLaneAssetTagData.two_side"></a>

#### two\_side

```python
@two_side.setter
def two_side(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.affect_terrain"></a>

#### affect\_terrain

```python
@property
def affect_terrain() -> bool
```

(bool):  [Read-Write] 是否压地形

<a id="unreal.AesRoadLaneAssetTagData.affect_terrain"></a>

#### affect\_terrain

```python
@affect_terrain.setter
def affect_terrain(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.spline_point_type"></a>

#### spline\_point\_type

```python
@property
def spline_point_type() -> SplinePointType
```

(SplinePointType):  [Read-Write] 样条线点位类型

<a id="unreal.AesRoadLaneAssetTagData.spline_point_type"></a>

#### spline\_point\_type

```python
@spline_point_type.setter
def spline_point_type(value: SplinePointType) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.resample_type"></a>

#### resample\_type

```python
@property
def resample_type() -> SplineResampleType
```

(SplineResampleType):  [Read-Write] 样条线重采样类型

<a id="unreal.AesRoadLaneAssetTagData.resample_type"></a>

#### resample\_type

```python
@resample_type.setter
def resample_type(value: SplineResampleType) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.f_class"></a>

#### f\_class

```python
@property
def f_class() -> str
```

(str):  [Read-Write] 道路类型

<a id="unreal.AesRoadLaneAssetTagData.f_class"></a>

#### f\_class

```python
@f_class.setter
def f_class(value: str) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.side"></a>

#### side

```python
@property
def side() -> DrivingDirection
```

(DrivingDirection):  [Read-Write] 道路行驶方向

<a id="unreal.AesRoadLaneAssetTagData.side"></a>

#### side

```python
@side.setter
def side(value: DrivingDirection) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_lanes"></a>

#### start\_lanes

```python
@property
def start_lanes() -> IntPoint
```

(IntPoint):  [Read-Write] 左右车道数

<a id="unreal.AesRoadLaneAssetTagData.start_lanes"></a>

#### start\_lanes

```python
@start_lanes.setter
def start_lanes(value: IntPoint) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_lanes"></a>

#### end\_lanes

```python
@property
def end_lanes() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_lanes"></a>

#### end\_lanes

```python
@end_lanes.setter
def end_lanes(value: IntPoint) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_lane_width"></a>

#### start\_lane\_width

```python
@property
def start_lane_width() -> Vector2f
```

(Vector2f):  [Read-Write] 车道路宽度

<a id="unreal.AesRoadLaneAssetTagData.start_lane_width"></a>

#### start\_lane\_width

```python
@start_lane_width.setter
def start_lane_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_lane_width"></a>

#### end\_lane\_width

```python
@property
def end_lane_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_lane_width"></a>

#### end\_lane\_width

```python
@end_lane_width.setter
def end_lane_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_width"></a>

#### start\_width

```python
@property
def start_width() -> Vector2f
```

(Vector2f):  [Read-Only] 道路总宽度

<a id="unreal.AesRoadLaneAssetTagData.end_width"></a>

#### end\_width

```python
@property
def end_width() -> Vector2f
```

(Vector2f):  [Read-Only]

<a id="unreal.AesRoadLaneAssetTagData.level"></a>

#### level

```python
@property
def level() -> int
```

(int32):  [Read-Write] 道路总宽度

<a id="unreal.AesRoadLaneAssetTagData.level"></a>

#### level

```python
@level.setter
def level(value: int) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.keep_reference_line_centered"></a>

#### keep\_reference\_line\_centered

```python
@property
def keep_reference_line_centered() -> bool
```

(bool):  [Read-Write] 是否保证参考线位于路面正中间

<a id="unreal.AesRoadLaneAssetTagData.keep_reference_line_centered"></a>

#### keep\_reference\_line\_centered

```python
@keep_reference_line_centered.setter
def keep_reference_line_centered(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.keep_tan_value"></a>

#### keep\_tan\_value

```python
@property
def keep_tan_value() -> bool
```

(bool):  [Read-Write] 是否改变起始点Tan值

<a id="unreal.AesRoadLaneAssetTagData.keep_tan_value"></a>

#### keep\_tan\_value

```python
@keep_tan_value.setter
def keep_tan_value(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_tan"></a>

#### end\_tan

```python
@property
def end_tan() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_tan"></a>

#### end\_tan

```python
@end_tan.setter
def end_tan(value: Vector) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_tan"></a>

#### start\_tan

```python
@property
def start_tan() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.start_tan"></a>

#### start\_tan

```python
@start_tan.setter
def start_tan(value: Vector) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_guardrail_width"></a>

#### start\_guardrail\_width

```python
@property
def start_guardrail_width() -> Vector2f
```

(Vector2f):  [Read-Write] 护栏宽度

<a id="unreal.AesRoadLaneAssetTagData.start_guardrail_width"></a>

#### start\_guardrail\_width

```python
@start_guardrail_width.setter
def start_guardrail_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_guardrail_width"></a>

#### end\_guardrail\_width

```python
@property
def end_guardrail_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_guardrail_width"></a>

#### end\_guardrail\_width

```python
@end_guardrail_width.setter
def end_guardrail_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_emergency_width"></a>

#### start\_emergency\_width

```python
@property
def start_emergency_width() -> Vector2f
```

(Vector2f):  [Read-Write] 应急车道宽度

<a id="unreal.AesRoadLaneAssetTagData.start_emergency_width"></a>

#### start\_emergency\_width

```python
@start_emergency_width.setter
def start_emergency_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_emergency_width"></a>

#### end\_emergency\_width

```python
@property
def end_emergency_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_emergency_width"></a>

#### end\_emergency\_width

```python
@end_emergency_width.setter
def end_emergency_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_shoulder_width"></a>

#### start\_shoulder\_width

```python
@property
def start_shoulder_width() -> Vector2f
```

(Vector2f):  [Read-Write] 路肩宽度

<a id="unreal.AesRoadLaneAssetTagData.start_shoulder_width"></a>

#### start\_shoulder\_width

```python
@start_shoulder_width.setter
def start_shoulder_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_shoulder_width"></a>

#### end\_shoulder\_width

```python
@property
def end_shoulder_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_shoulder_width"></a>

#### end\_shoulder\_width

```python
@end_shoulder_width.setter
def end_shoulder_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_biking_width"></a>

#### start\_biking\_width

```python
@property
def start_biking_width() -> Vector2f
```

(Vector2f):  [Read-Write] 自行车宽度

<a id="unreal.AesRoadLaneAssetTagData.start_biking_width"></a>

#### start\_biking\_width

```python
@start_biking_width.setter
def start_biking_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_biking_width"></a>

#### end\_biking\_width

```python
@property
def end_biking_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_biking_width"></a>

#### end\_biking\_width

```python
@end_biking_width.setter
def end_biking_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_parking_width"></a>

#### start\_parking\_width

```python
@property
def start_parking_width() -> Vector2f
```

(Vector2f):  [Read-Write] 停车道路宽度

<a id="unreal.AesRoadLaneAssetTagData.start_parking_width"></a>

#### start\_parking\_width

```python
@start_parking_width.setter
def start_parking_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_parking_width"></a>

#### end\_parking\_width

```python
@property
def end_parking_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_parking_width"></a>

#### end\_parking\_width

```python
@end_parking_width.setter
def end_parking_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_sidewalk_width"></a>

#### start\_sidewalk\_width

```python
@property
def start_sidewalk_width() -> Vector2f
```

(Vector2f):  [Read-Write] 人行道宽度

<a id="unreal.AesRoadLaneAssetTagData.start_sidewalk_width"></a>

#### start\_sidewalk\_width

```python
@start_sidewalk_width.setter
def start_sidewalk_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_sidewalk_width"></a>

#### end\_sidewalk\_width

```python
@property
def end_sidewalk_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_sidewalk_width"></a>

#### end\_sidewalk\_width

```python
@end_sidewalk_width.setter
def end_sidewalk_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_median_width"></a>

#### start\_median\_width

```python
@property
def start_median_width() -> Vector2f
```

(Vector2f):  [Read-Write] 中央隔离带宽度

<a id="unreal.AesRoadLaneAssetTagData.start_median_width"></a>

#### start\_median\_width

```python
@start_median_width.setter
def start_median_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_median_width"></a>

#### end\_median\_width

```python
@property
def end_median_width() -> Vector2f
```

(Vector2f):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_median_width"></a>

#### end\_median\_width

```python
@end_median_width.setter
def end_median_width(value: Vector2f) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.start_extension"></a>

#### start\_extension

```python
@property
def start_extension() -> float
```

(float):  [Read-Write] 收尾端缩进长度

<a id="unreal.AesRoadLaneAssetTagData.start_extension"></a>

#### start\_extension

```python
@start_extension.setter
def start_extension(value: float) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.end_extension"></a>

#### end\_extension

```python
@property
def end_extension() -> float
```

(float):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.end_extension"></a>

#### end\_extension

```python
@end_extension.setter
def end_extension(value: float) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.build_start_mesh"></a>

#### build\_start\_mesh

```python
@property
def build_start_mesh() -> bool
```

(bool):  [Read-Write] 收尾端缩进长度

<a id="unreal.AesRoadLaneAssetTagData.build_start_mesh"></a>

#### build\_start\_mesh

```python
@build_start_mesh.setter
def build_start_mesh(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.build_end_mesh"></a>

#### build\_end\_mesh

```python
@property
def build_end_mesh() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesRoadLaneAssetTagData.build_end_mesh"></a>

#### build\_end\_mesh

```python
@build_end_mesh.setter
def build_end_mesh(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 点是否倒角

<a id="unreal.AesRoadLaneAssetTagData.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 切角长度

<a id="unreal.AesRoadLaneAssetTagData.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.lane_x_direction"></a>

#### lane\_x\_direction

```python
@property
def lane_x_direction() -> Array[LaneDirection]
```

(Array[LaneDirection]):  [Read-Write] 车道X转向方向

<a id="unreal.AesRoadLaneAssetTagData.lane_x_direction"></a>

#### lane\_x\_direction

```python
@lane_x_direction.setter
def lane_x_direction(value: Array[LaneDirection]) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.lane_y_direction"></a>

#### lane\_y\_direction

```python
@property
def lane_y_direction() -> Array[LaneDirection]
```

(Array[LaneDirection]):  [Read-Write] 车道Y转向方向

<a id="unreal.AesRoadLaneAssetTagData.lane_y_direction"></a>

#### lane\_y\_direction

```python
@lane_y_direction.setter
def lane_y_direction(value: Array[LaneDirection]) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.assets_array"></a>

#### assets\_array

```python
@property
def assets_array() -> Array[AesRoadLaneAssetInfo]
```

(Array[AesRoadLaneAssetInfo]):  [Read-Write] 默认资产模板

<a id="unreal.AesRoadLaneAssetTagData.assets_array"></a>

#### assets\_array

```python
@assets_array.setter
def assets_array(value: Array[AesRoadLaneAssetInfo]) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.guide_meshes"></a>

#### guide\_meshes

```python
@property
def guide_meshes() -> Map[Name, AesMeshData]
```

(Map[Name, AesMeshData]):  [Read-Write] 箭头引用序列

<a id="unreal.AesRoadLaneAssetTagData.guide_meshes"></a>

#### guide\_meshes

```python
@guide_meshes.setter
def guide_meshes(value: Map[Name, AesMeshData]) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.build_traffic_light"></a>

#### build\_traffic\_light

```python
@property
def build_traffic_light() -> bool
```

(bool):  [Read-Write] 道路是否生成交通信号灯

<a id="unreal.AesRoadLaneAssetTagData.build_traffic_light"></a>

#### build\_traffic\_light

```python
@build_traffic_light.setter
def build_traffic_light(value: bool) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.junction_prefab_id"></a>

#### junction\_prefab\_id

```python
@property
def junction_prefab_id() -> str
```

(str):  [Read-Write] 指定路口PrefabID

<a id="unreal.AesRoadLaneAssetTagData.junction_prefab_id"></a>

#### junction\_prefab\_id

```python
@junction_prefab_id.setter
def junction_prefab_id(value: str) -> None
```

<a id="unreal.AesRoadLaneAssetTagData.road_surface_material_path"></a>

#### road\_surface\_material\_path

```python
@property
def road_surface_material_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 路面材质路径

<a id="unreal.AesRoadLaneAssetTagData.road_surface_material_path"></a>

#### road\_surface\_material\_path

```python
@road_surface_material_path.setter
def road_surface_material_path(value: SoftObjectPath) -> None
```

<a id="unreal.AesRoadLaneAssetData"></a>