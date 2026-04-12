## EarthInstanceSplineFragment Objects

```python
class EarthInstanceSplineFragment(EarthEntityFragment)
```

实例化样条线片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment_type`` (EarthSplineAlignmentType):  [Read-Write] 资产Z轴对齐类型
- ``chamfer_corner`` (bool):  [Read-Write] 点是否倒角
- ``chamfer_length`` (float):  [Read-Write] 切角长度
- ``control_type`` (EarthSplineSizeControlType):  [Read-Write] 样条线缩放控制类型
- ``end_extension`` (float):  [Read-Write] 样条线终点延长距离
- ``end_height`` (Vector2f):  [Read-Write] 样条线终点高度
- ``end_offset`` (Vector2f):  [Read-Write] 样条线终点偏移值
- ``end_roll`` (float):  [Read-Write] 样条线终点翻滚值
- ``end_scale`` (Vector2f):  [Read-Write] 样条线终点缩放值
- ``end_scale_x`` (float):  [Read-Write] 样条线终点X轴方向缩放值
- ``end_width`` (Vector2f):  [Read-Write] 样条线终点宽度
- ``forward_axis`` (SplineMeshAxis):  [Read-Write] 样条线模型前进朝向所在轴
- ``gap_between_bounds`` (float):  [Read-Write] 资产包围盒的间距
- ``instance_mesh_list`` (EarthRoadInstanceShapeGrammar):  [Read-Write] 模块自定义排列
- ``local_smooth_interp_roll_scale`` (bool):  [Read-Write] 是否在每一段平滑差值翻滚和缩放值
- ``multi_width_params`` (Array[WidthParam]):  [Read-Write] 样条线多宽度控制
- ``placement_type`` (EarthSplinePlacementType):  [Read-Write] 资产放置类型
- ``points_order`` (EarthPointsOrder):  [Read-Write] 样条线点序类型
- ``remove_ratios`` (ModifyRanges):  [Read-Write] 样条线去除区域控制
- ``resample_by_edge`` (bool):  [Read-Write] 是否基于边来重采样
- ``rotation_range`` (Vector2f):  [Read-Write] 随机旋转值调度范围
- ``scale_range`` (Vector2f):  [Read-Write] 随机缩放值调度范围
- ``spline_deform_type`` (EarthSplineDeformType):  [Read-Write] 是否为线性插值形变的样条线
- ``spline_up_dir`` (Vector3f):  [Read-Write] 样条线模型向上朝向
- ``start_extension`` (float):  [Read-Write] 样条线起点延长距离
- ``start_height`` (Vector2f):  [Read-Write] 样条线起点高度
- ``start_offset`` (Vector2f):  [Read-Write] 样条线起点偏移值
- ``start_roll`` (float):  [Read-Write] 样条线起点翻滚值
- ``start_scale`` (Vector2f):  [Read-Write] 样条线起点缩放值
- ``start_scale_x`` (float):  [Read-Write] 样条线起点X轴方向缩放值
- ``start_width`` (Vector2f):  [Read-Write] 样条线起点宽度
- ``use_random_parameter`` (bool):  [Read-Write] 是否使用随机参数
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``world_smooth_interp_roll_scale`` (bool):  [Read-Write] 是否在全线段平滑差值翻滚和缩放值

<a id="unreal.EarthInstanceSplineFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        points_order: EarthPointsOrder = EarthPointsOrder.KEEP,
        start_extension: float = 0.000000,
        end_extension: float = 0.000000,
        spline_deform_type: EarthSplineDeformType = EarthSplineDeformType.
    CURVE,
        forward_axis: SplineMeshAxis = SplineMeshAxis.X,
        spline_up_dir: Vector3f = [0.000000, 0.000000, 0.000000],
        world_smooth_interp_roll_scale: bool = False,
        local_smooth_interp_roll_scale: bool = False,
        control_type: EarthSplineSizeControlType = EarthSplineSizeControlType.
    SCALE,
        start_scale: Vector2f = [0.000000, 0.000000],
        start_offset: Vector2f = [0.000000, 0.000000],
        start_width: Vector2f = [0.000000, 0.000000],
        start_height: Vector2f = [0.000000, 0.000000],
        start_roll: float = 0.000000,
        end_scale: Vector2f = [0.000000, 0.000000],
        end_offset: Vector2f = [0.000000, 0.000000],
        end_width: Vector2f = [0.000000, 0.000000],
        end_height: Vector2f = [0.000000, 0.000000],
        end_roll: float = 0.000000,
        resample_by_edge: bool = False,
        placement_type: EarthSplinePlacementType = EarthSplinePlacementType.
    CONTINUOUS,
        gap_between_bounds: float = 0.000000,
        alignment_type: EarthSplineAlignmentType = EarthSplineAlignmentType.
    NORMAL,
        use_random_parameter: bool = False,
        rotation_range: Vector2f = [0.000000, 0.000000],
        scale_range: Vector2f = [0.000000, 0.000000],
        start_scale_x: float = 0.000000,
        end_scale_x: float = 0.000000,
        chamfer_corner: bool = False,
        chamfer_length: float = 0.000000,
        instance_mesh_list: EarthRoadInstanceShapeGrammar = [{}, "", "", ""],
        multi_width_params: Array[WidthParam] = [],
        remove_ratios: ModifyRanges = [[]]) -> None
```

<a id="unreal.EarthInstanceSplineFragment.points_order"></a>

#### points\_order

```python
@property
def points_order() -> EarthPointsOrder
```

(EarthPointsOrder):  [Read-Write] 样条线点序类型

<a id="unreal.EarthInstanceSplineFragment.points_order"></a>

#### points\_order

```python
@points_order.setter
def points_order(value: EarthPointsOrder) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_extension"></a>

#### start\_extension

```python
@property
def start_extension() -> float
```

(float):  [Read-Write] 样条线起点延长距离

<a id="unreal.EarthInstanceSplineFragment.start_extension"></a>

#### start\_extension

```python
@start_extension.setter
def start_extension(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_extension"></a>

#### end\_extension

```python
@property
def end_extension() -> float
```

(float):  [Read-Write] 样条线终点延长距离

<a id="unreal.EarthInstanceSplineFragment.end_extension"></a>

#### end\_extension

```python
@end_extension.setter
def end_extension(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.spline_deform_type"></a>

#### spline\_deform\_type

```python
@property
def spline_deform_type() -> EarthSplineDeformType
```

(EarthSplineDeformType):  [Read-Write] 是否为线性插值形变的样条线

<a id="unreal.EarthInstanceSplineFragment.spline_deform_type"></a>

#### spline\_deform\_type

```python
@spline_deform_type.setter
def spline_deform_type(value: EarthSplineDeformType) -> None
```

<a id="unreal.EarthInstanceSplineFragment.forward_axis"></a>

#### forward\_axis

```python
@property
def forward_axis() -> SplineMeshAxis
```

(SplineMeshAxis):  [Read-Write] 样条线模型前进朝向所在轴

<a id="unreal.EarthInstanceSplineFragment.forward_axis"></a>

#### forward\_axis

```python
@forward_axis.setter
def forward_axis(value: SplineMeshAxis) -> None
```

<a id="unreal.EarthInstanceSplineFragment.spline_up_dir"></a>

#### spline\_up\_dir

```python
@property
def spline_up_dir() -> Vector3f
```

(Vector3f):  [Read-Write] 样条线模型向上朝向

<a id="unreal.EarthInstanceSplineFragment.spline_up_dir"></a>

#### spline\_up\_dir

```python
@spline_up_dir.setter
def spline_up_dir(value: Vector3f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.world_smooth_interp_roll_scale"></a>

#### world\_smooth\_interp\_roll\_scale

```python
@property
def world_smooth_interp_roll_scale() -> bool
```

(bool):  [Read-Write] 是否在全线段平滑差值翻滚和缩放值

<a id="unreal.EarthInstanceSplineFragment.world_smooth_interp_roll_scale"></a>

#### world\_smooth\_interp\_roll\_scale

```python
@world_smooth_interp_roll_scale.setter
def world_smooth_interp_roll_scale(value: bool) -> None
```

<a id="unreal.EarthInstanceSplineFragment.local_smooth_interp_roll_scale"></a>

#### local\_smooth\_interp\_roll\_scale

```python
@property
def local_smooth_interp_roll_scale() -> bool
```

(bool):  [Read-Write] 是否在每一段平滑差值翻滚和缩放值

<a id="unreal.EarthInstanceSplineFragment.local_smooth_interp_roll_scale"></a>

#### local\_smooth\_interp\_roll\_scale

```python
@local_smooth_interp_roll_scale.setter
def local_smooth_interp_roll_scale(value: bool) -> None
```

<a id="unreal.EarthInstanceSplineFragment.control_type"></a>

#### control\_type

```python
@property
def control_type() -> EarthSplineSizeControlType
```

(EarthSplineSizeControlType):  [Read-Write] 样条线缩放控制类型

<a id="unreal.EarthInstanceSplineFragment.control_type"></a>

#### control\_type

```python
@control_type.setter
def control_type(value: EarthSplineSizeControlType) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_scale"></a>

#### start\_scale

```python
@property
def start_scale() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点缩放值

<a id="unreal.EarthInstanceSplineFragment.start_scale"></a>

#### start\_scale

```python
@start_scale.setter
def start_scale(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_offset"></a>

#### start\_offset

```python
@property
def start_offset() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点偏移值

<a id="unreal.EarthInstanceSplineFragment.start_offset"></a>

#### start\_offset

```python
@start_offset.setter
def start_offset(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_width"></a>

#### start\_width

```python
@property
def start_width() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点宽度

<a id="unreal.EarthInstanceSplineFragment.start_width"></a>

#### start\_width

```python
@start_width.setter
def start_width(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_height"></a>

#### start\_height

```python
@property
def start_height() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点高度

<a id="unreal.EarthInstanceSplineFragment.start_height"></a>

#### start\_height

```python
@start_height.setter
def start_height(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_roll"></a>

#### start\_roll

```python
@property
def start_roll() -> float
```

(float):  [Read-Write] 样条线起点翻滚值

<a id="unreal.EarthInstanceSplineFragment.start_roll"></a>

#### start\_roll

```python
@start_roll.setter
def start_roll(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_scale"></a>

#### end\_scale

```python
@property
def end_scale() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点缩放值

<a id="unreal.EarthInstanceSplineFragment.end_scale"></a>

#### end\_scale

```python
@end_scale.setter
def end_scale(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_offset"></a>

#### end\_offset

```python
@property
def end_offset() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点偏移值

<a id="unreal.EarthInstanceSplineFragment.end_offset"></a>

#### end\_offset

```python
@end_offset.setter
def end_offset(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_width"></a>

#### end\_width

```python
@property
def end_width() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点宽度

<a id="unreal.EarthInstanceSplineFragment.end_width"></a>

#### end\_width

```python
@end_width.setter
def end_width(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_height"></a>

#### end\_height

```python
@property
def end_height() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点高度

<a id="unreal.EarthInstanceSplineFragment.end_height"></a>

#### end\_height

```python
@end_height.setter
def end_height(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_roll"></a>

#### end\_roll

```python
@property
def end_roll() -> float
```

(float):  [Read-Write] 样条线终点翻滚值

<a id="unreal.EarthInstanceSplineFragment.end_roll"></a>

#### end\_roll

```python
@end_roll.setter
def end_roll(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.resample_by_edge"></a>

#### resample\_by\_edge

```python
@property
def resample_by_edge() -> bool
```

(bool):  [Read-Write] 是否基于边来重采样

<a id="unreal.EarthInstanceSplineFragment.resample_by_edge"></a>

#### resample\_by\_edge

```python
@resample_by_edge.setter
def resample_by_edge(value: bool) -> None
```

<a id="unreal.EarthInstanceSplineFragment.placement_type"></a>

#### placement\_type

```python
@property
def placement_type() -> EarthSplinePlacementType
```

(EarthSplinePlacementType):  [Read-Write] 资产放置类型

<a id="unreal.EarthInstanceSplineFragment.placement_type"></a>

#### placement\_type

```python
@placement_type.setter
def placement_type(value: EarthSplinePlacementType) -> None
```

<a id="unreal.EarthInstanceSplineFragment.gap_between_bounds"></a>

#### gap\_between\_bounds

```python
@property
def gap_between_bounds() -> float
```

(float):  [Read-Write] 资产包围盒的间距

<a id="unreal.EarthInstanceSplineFragment.gap_between_bounds"></a>

#### gap\_between\_bounds

```python
@gap_between_bounds.setter
def gap_between_bounds(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.alignment_type"></a>

#### alignment\_type

```python
@property
def alignment_type() -> EarthSplineAlignmentType
```

(EarthSplineAlignmentType):  [Read-Write] 资产Z轴对齐类型

<a id="unreal.EarthInstanceSplineFragment.alignment_type"></a>

#### alignment\_type

```python
@alignment_type.setter
def alignment_type(value: EarthSplineAlignmentType) -> None
```

<a id="unreal.EarthInstanceSplineFragment.use_random_parameter"></a>

#### use\_random\_parameter

```python
@property
def use_random_parameter() -> bool
```

(bool):  [Read-Write] 是否使用随机参数

<a id="unreal.EarthInstanceSplineFragment.use_random_parameter"></a>

#### use\_random\_parameter

```python
@use_random_parameter.setter
def use_random_parameter(value: bool) -> None
```

<a id="unreal.EarthInstanceSplineFragment.rotation_range"></a>

#### rotation\_range

```python
@property
def rotation_range() -> Vector2f
```

(Vector2f):  [Read-Write] 随机旋转值调度范围

<a id="unreal.EarthInstanceSplineFragment.rotation_range"></a>

#### rotation\_range

```python
@rotation_range.setter
def rotation_range(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.scale_range"></a>

#### scale\_range

```python
@property
def scale_range() -> Vector2f
```

(Vector2f):  [Read-Write] 随机缩放值调度范围

<a id="unreal.EarthInstanceSplineFragment.scale_range"></a>

#### scale\_range

```python
@scale_range.setter
def scale_range(value: Vector2f) -> None
```

<a id="unreal.EarthInstanceSplineFragment.start_scale_x"></a>

#### start\_scale\_x

```python
@property
def start_scale_x() -> float
```

(float):  [Read-Write] 样条线起点X轴方向缩放值

<a id="unreal.EarthInstanceSplineFragment.start_scale_x"></a>

#### start\_scale\_x

```python
@start_scale_x.setter
def start_scale_x(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.end_scale_x"></a>

#### end\_scale\_x

```python
@property
def end_scale_x() -> float
```

(float):  [Read-Write] 样条线终点X轴方向缩放值

<a id="unreal.EarthInstanceSplineFragment.end_scale_x"></a>

#### end\_scale\_x

```python
@end_scale_x.setter
def end_scale_x(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 点是否倒角

<a id="unreal.EarthInstanceSplineFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.EarthInstanceSplineFragment.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 切角长度

<a id="unreal.EarthInstanceSplineFragment.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.EarthInstanceSplineFragment.instance_mesh_list"></a>

#### instance\_mesh\_list

```python
@property
def instance_mesh_list() -> EarthRoadInstanceShapeGrammar
```

(EarthRoadInstanceShapeGrammar):  [Read-Write] 模块自定义排列

<a id="unreal.EarthInstanceSplineFragment.instance_mesh_list"></a>

#### instance\_mesh\_list

```python
@instance_mesh_list.setter
def instance_mesh_list(value: EarthRoadInstanceShapeGrammar) -> None
```

<a id="unreal.EarthInstanceSplineFragment.multi_width_params"></a>

#### multi\_width\_params

```python
@property
def multi_width_params() -> Array[WidthParam]
```

(Array[WidthParam]):  [Read-Write] 样条线多宽度控制

<a id="unreal.EarthInstanceSplineFragment.multi_width_params"></a>

#### multi\_width\_params

```python
@multi_width_params.setter
def multi_width_params(value: Array[WidthParam]) -> None
```

<a id="unreal.EarthInstanceSplineFragment.remove_ratios"></a>

#### remove\_ratios

```python
@property
def remove_ratios() -> ModifyRanges
```

(ModifyRanges):  [Read-Write] 样条线去除区域控制

<a id="unreal.EarthInstanceSplineFragment.remove_ratios"></a>

#### remove\_ratios

```python
@remove_ratios.setter
def remove_ratios(value: ModifyRanges) -> None
```

<a id="unreal.ModifyRanges"></a>