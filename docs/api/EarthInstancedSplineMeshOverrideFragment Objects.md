## EarthInstancedSplineMeshOverrideFragment Objects

```python
class EarthInstancedSplineMeshOverrideFragment(EarthInstanceSplineFragment)
```

Earth Instanced Spline Mesh Override Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInstancedSplineMeshFragment.h

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

<a id="unreal.EarthInstancedSplineMeshOverrideFragment.__init__"></a>

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

<a id="unreal.EarthCustomDataPackerFragment"></a>