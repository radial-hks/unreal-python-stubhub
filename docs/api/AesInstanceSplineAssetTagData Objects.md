## AesInstanceSplineAssetTagData Objects

```python
class AesInstanceSplineAssetTagData(StructBase)
```

实例样条线资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesInstanceSplineAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alignment_type`` (SplineAlignmentType):  [Read-Write] 资产Z轴对齐类型
- ``build_end_mesh`` (bool):  [Read-Write] 是否生成终点模型
- ``build_start_mesh`` (bool):  [Read-Write] 是否生成起点模型
- ``chamfer_corner`` (bool):  [Read-Write] 点是否倒角
- ``chamfer_length`` (float):  [Read-Write] 切角长度
- ``closed_loop`` (bool):  [Read-Write] 是否为封闭曲线
- ``control_type`` (AesSplineSizeControlType):  [Read-Write] 样条线缩放控制类型
- ``custom_data`` (Map[Name, float]):  [Read-Write] 自定义数据
- ``end_extension`` (float):  [Read-Write] 样条线终点延长距离
- ``end_height`` (Vector2f):  [Read-Write] 样条线终点高度
- ``end_mesh`` (AesMeshData):  [Read-Write] 终点资产引用
- ``end_offset`` (Vector2f):  [Read-Write] 样条线终点偏移值
- ``end_roll`` (float):  [Read-Write] 样条线终点翻滚值
- ``end_scale`` (Vector2f):  [Read-Write] 样条线终点缩放值
- ``end_scale_x`` (float):  [Read-Write] 样条线终点X轴方向缩放值
- ``end_tan`` (Vector):  [Read-Write] 终点切线值
- ``end_width`` (Vector2f):  [Read-Write] 样条线终点宽度
- ``flip_end_mesh`` (bool):  [Read-Write] 是否翻转终点资产
- ``flip_start_mesh`` (bool):  [Read-Write] 是否翻转起点资产
- ``forward_axis`` (SplineMeshAxis):  [Read-Write] 样条线模型前进朝向所在轴
- ``gap_between_bounds`` (float):  [Read-Write] 资产包围盒的间距
- ``keep_tan_value`` (bool):  [Read-Write] 是否改变起始点Tan值
- ``local_smooth_interp_roll_scale`` (bool):  [Read-Write] 是否在每一段平滑差值翻滚和缩放值
- ``mid_meshes`` (Array[AesMeshData]):  [Read-Write] 中间资产引用序列
- ``placement_type`` (SplinePlacementType):  [Read-Write] 资产放置类型
- ``resample_by_edge`` (bool):  [Read-Write] 是否基于边来重采样
- ``resample_type`` (SplineResampleType):  [Read-Write] 样条线重采样类型
- ``reverse`` (bool):  [Read-Write] 是否调转曲线前进方向
- ``section_length`` (float):  [Read-Write] 重采样段长
- ``spline_deform_type`` (SplineDeformType):  [Read-Write] 是否为线性插值形变的样条线
- ``spline_point_type`` (SplinePointType):  [Read-Write] 样条线点位类型
- ``spline_up_dir`` (Vector3f):  [Read-Write] 样条线模型向上朝向
- ``start_extension`` (float):  [Read-Write] 样条线起点延长距离
- ``start_height`` (Vector2f):  [Read-Write] 样条线起点高度
- ``start_mesh`` (AesMeshData):  [Read-Write] 起点资产引用
- ``start_offset`` (Vector2f):  [Read-Write] 样条线起点偏移值
- ``start_roll`` (float):  [Read-Write] 样条线起点翻滚值
- ``start_scale`` (Vector2f):  [Read-Write] 样条线起点缩放值
- ``start_scale_x`` (float):  [Read-Write] 样条线起点X轴方向缩放值
- ``start_tan`` (Vector):  [Read-Write] 起点切线值
- ``start_width`` (Vector2f):  [Read-Write] 样条线起点宽度
- ``world_smooth_interp_roll_scale`` (bool):  [Read-Write] 是否在全线段平滑差值翻滚和缩放值

<a id="unreal.AesInstanceSplineAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        closed_loop: bool = False,
        reverse: bool = False,
        spline_point_type: SplinePointType = SplinePointType.LINEAR,
        start_extension: float = 0.000000,
        end_extension: float = 0.000000,
        start_mesh: AesMeshData = [[
            ""
        ], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [],
                                   []],
        mid_meshes: Array[AesMeshData] = [],
        end_mesh: AesMeshData = [[
            ""
        ], ["/Script/AesRenderResource.AesInstancedStaticMeshComponent"], [],
                                 []],
        flip_start_mesh: bool = False,
        flip_end_mesh: bool = False,
        spline_deform_type: SplineDeformType = SplineDeformType.LINEAR,
        forward_axis: SplineMeshAxis = SplineMeshAxis.X,
        spline_up_dir: Vector3f = [0.000000, 0.000000, 0.000000],
        world_smooth_interp_roll_scale: bool = False,
        local_smooth_interp_roll_scale: bool = False,
        control_type: AesSplineSizeControlType = AesSplineSizeControlType.
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
        resample_type: SplineResampleType = SplineResampleType.INTERPOLATING,
        resample_by_edge: bool = False,
        placement_type: SplinePlacementType = SplinePlacementType.CONTINUOUS,
        section_length: float = 0.000000,
        gap_between_bounds: float = 0.000000,
        alignment_type: SplineAlignmentType = SplineAlignmentType.NORMAL,
        start_scale_x: float = 0.000000,
        end_scale_x: float = 0.000000,
        keep_tan_value: bool = False,
        start_tan: Vector = [0.000000, 0.000000, 0.000000],
        end_tan: Vector = [0.000000, 0.000000, 0.000000],
        build_start_mesh: bool = False,
        build_end_mesh: bool = False,
        chamfer_corner: bool = False,
        chamfer_length: float = 0.000000,
        custom_data: Map[Name, float] = {}) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.closed_loop"></a>

#### closed\_loop

```python
@property
def closed_loop() -> bool
```

(bool):  [Read-Write] 是否为封闭曲线

<a id="unreal.AesInstanceSplineAssetTagData.closed_loop"></a>

#### closed\_loop

```python
@closed_loop.setter
def closed_loop(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write] 是否调转曲线前进方向

<a id="unreal.AesInstanceSplineAssetTagData.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.spline_point_type"></a>

#### spline\_point\_type

```python
@property
def spline_point_type() -> SplinePointType
```

(SplinePointType):  [Read-Write] 样条线点位类型

<a id="unreal.AesInstanceSplineAssetTagData.spline_point_type"></a>

#### spline\_point\_type

```python
@spline_point_type.setter
def spline_point_type(value: SplinePointType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_extension"></a>

#### start\_extension

```python
@property
def start_extension() -> float
```

(float):  [Read-Write] 样条线起点延长距离

<a id="unreal.AesInstanceSplineAssetTagData.start_extension"></a>

#### start\_extension

```python
@start_extension.setter
def start_extension(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_extension"></a>

#### end\_extension

```python
@property
def end_extension() -> float
```

(float):  [Read-Write] 样条线终点延长距离

<a id="unreal.AesInstanceSplineAssetTagData.end_extension"></a>

#### end\_extension

```python
@end_extension.setter
def end_extension(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_mesh"></a>

#### start\_mesh

```python
@property
def start_mesh() -> AesMeshData
```

(AesMeshData):  [Read-Write] 起点资产引用

<a id="unreal.AesInstanceSplineAssetTagData.start_mesh"></a>

#### start\_mesh

```python
@start_mesh.setter
def start_mesh(value: AesMeshData) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.mid_meshes"></a>

#### mid\_meshes

```python
@property
def mid_meshes() -> Array[AesMeshData]
```

(Array[AesMeshData]):  [Read-Write] 中间资产引用序列

<a id="unreal.AesInstanceSplineAssetTagData.mid_meshes"></a>

#### mid\_meshes

```python
@mid_meshes.setter
def mid_meshes(value: Array[AesMeshData]) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_mesh"></a>

#### end\_mesh

```python
@property
def end_mesh() -> AesMeshData
```

(AesMeshData):  [Read-Write] 终点资产引用

<a id="unreal.AesInstanceSplineAssetTagData.end_mesh"></a>

#### end\_mesh

```python
@end_mesh.setter
def end_mesh(value: AesMeshData) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.flip_start_mesh"></a>

#### flip\_start\_mesh

```python
@property
def flip_start_mesh() -> bool
```

(bool):  [Read-Write] 是否翻转起点资产

<a id="unreal.AesInstanceSplineAssetTagData.flip_start_mesh"></a>

#### flip\_start\_mesh

```python
@flip_start_mesh.setter
def flip_start_mesh(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.flip_end_mesh"></a>

#### flip\_end\_mesh

```python
@property
def flip_end_mesh() -> bool
```

(bool):  [Read-Write] 是否翻转终点资产

<a id="unreal.AesInstanceSplineAssetTagData.flip_end_mesh"></a>

#### flip\_end\_mesh

```python
@flip_end_mesh.setter
def flip_end_mesh(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.spline_deform_type"></a>

#### spline\_deform\_type

```python
@property
def spline_deform_type() -> SplineDeformType
```

(SplineDeformType):  [Read-Write] 是否为线性插值形变的样条线

<a id="unreal.AesInstanceSplineAssetTagData.spline_deform_type"></a>

#### spline\_deform\_type

```python
@spline_deform_type.setter
def spline_deform_type(value: SplineDeformType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.forward_axis"></a>

#### forward\_axis

```python
@property
def forward_axis() -> SplineMeshAxis
```

(SplineMeshAxis):  [Read-Write] 样条线模型前进朝向所在轴

<a id="unreal.AesInstanceSplineAssetTagData.forward_axis"></a>

#### forward\_axis

```python
@forward_axis.setter
def forward_axis(value: SplineMeshAxis) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.spline_up_dir"></a>

#### spline\_up\_dir

```python
@property
def spline_up_dir() -> Vector3f
```

(Vector3f):  [Read-Write] 样条线模型向上朝向

<a id="unreal.AesInstanceSplineAssetTagData.spline_up_dir"></a>

#### spline\_up\_dir

```python
@spline_up_dir.setter
def spline_up_dir(value: Vector3f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.world_smooth_interp_roll_scale"></a>

#### world\_smooth\_interp\_roll\_scale

```python
@property
def world_smooth_interp_roll_scale() -> bool
```

(bool):  [Read-Write] 是否在全线段平滑差值翻滚和缩放值

<a id="unreal.AesInstanceSplineAssetTagData.world_smooth_interp_roll_scale"></a>

#### world\_smooth\_interp\_roll\_scale

```python
@world_smooth_interp_roll_scale.setter
def world_smooth_interp_roll_scale(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.local_smooth_interp_roll_scale"></a>

#### local\_smooth\_interp\_roll\_scale

```python
@property
def local_smooth_interp_roll_scale() -> bool
```

(bool):  [Read-Write] 是否在每一段平滑差值翻滚和缩放值

<a id="unreal.AesInstanceSplineAssetTagData.local_smooth_interp_roll_scale"></a>

#### local\_smooth\_interp\_roll\_scale

```python
@local_smooth_interp_roll_scale.setter
def local_smooth_interp_roll_scale(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.control_type"></a>

#### control\_type

```python
@property
def control_type() -> AesSplineSizeControlType
```

(AesSplineSizeControlType):  [Read-Write] 样条线缩放控制类型

<a id="unreal.AesInstanceSplineAssetTagData.control_type"></a>

#### control\_type

```python
@control_type.setter
def control_type(value: AesSplineSizeControlType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_scale"></a>

#### start\_scale

```python
@property
def start_scale() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点缩放值

<a id="unreal.AesInstanceSplineAssetTagData.start_scale"></a>

#### start\_scale

```python
@start_scale.setter
def start_scale(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_offset"></a>

#### start\_offset

```python
@property
def start_offset() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点偏移值

<a id="unreal.AesInstanceSplineAssetTagData.start_offset"></a>

#### start\_offset

```python
@start_offset.setter
def start_offset(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_width"></a>

#### start\_width

```python
@property
def start_width() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点宽度

<a id="unreal.AesInstanceSplineAssetTagData.start_width"></a>

#### start\_width

```python
@start_width.setter
def start_width(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_height"></a>

#### start\_height

```python
@property
def start_height() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线起点高度

<a id="unreal.AesInstanceSplineAssetTagData.start_height"></a>

#### start\_height

```python
@start_height.setter
def start_height(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_roll"></a>

#### start\_roll

```python
@property
def start_roll() -> float
```

(float):  [Read-Write] 样条线起点翻滚值

<a id="unreal.AesInstanceSplineAssetTagData.start_roll"></a>

#### start\_roll

```python
@start_roll.setter
def start_roll(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_scale"></a>

#### end\_scale

```python
@property
def end_scale() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点缩放值

<a id="unreal.AesInstanceSplineAssetTagData.end_scale"></a>

#### end\_scale

```python
@end_scale.setter
def end_scale(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_offset"></a>

#### end\_offset

```python
@property
def end_offset() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点偏移值

<a id="unreal.AesInstanceSplineAssetTagData.end_offset"></a>

#### end\_offset

```python
@end_offset.setter
def end_offset(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_width"></a>

#### end\_width

```python
@property
def end_width() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点宽度

<a id="unreal.AesInstanceSplineAssetTagData.end_width"></a>

#### end\_width

```python
@end_width.setter
def end_width(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_height"></a>

#### end\_height

```python
@property
def end_height() -> Vector2f
```

(Vector2f):  [Read-Write] 样条线终点高度

<a id="unreal.AesInstanceSplineAssetTagData.end_height"></a>

#### end\_height

```python
@end_height.setter
def end_height(value: Vector2f) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_roll"></a>

#### end\_roll

```python
@property
def end_roll() -> float
```

(float):  [Read-Write] 样条线终点翻滚值

<a id="unreal.AesInstanceSplineAssetTagData.end_roll"></a>

#### end\_roll

```python
@end_roll.setter
def end_roll(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.resample_type"></a>

#### resample\_type

```python
@property
def resample_type() -> SplineResampleType
```

(SplineResampleType):  [Read-Write] 样条线重采样类型

<a id="unreal.AesInstanceSplineAssetTagData.resample_type"></a>

#### resample\_type

```python
@resample_type.setter
def resample_type(value: SplineResampleType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.resample_by_edge"></a>

#### resample\_by\_edge

```python
@property
def resample_by_edge() -> bool
```

(bool):  [Read-Write] 是否基于边来重采样

<a id="unreal.AesInstanceSplineAssetTagData.resample_by_edge"></a>

#### resample\_by\_edge

```python
@resample_by_edge.setter
def resample_by_edge(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.placement_type"></a>

#### placement\_type

```python
@property
def placement_type() -> SplinePlacementType
```

(SplinePlacementType):  [Read-Write] 资产放置类型

<a id="unreal.AesInstanceSplineAssetTagData.placement_type"></a>

#### placement\_type

```python
@placement_type.setter
def placement_type(value: SplinePlacementType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.section_length"></a>

#### section\_length

```python
@property
def section_length() -> float
```

(float):  [Read-Write] 重采样段长

<a id="unreal.AesInstanceSplineAssetTagData.section_length"></a>

#### section\_length

```python
@section_length.setter
def section_length(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.gap_between_bounds"></a>

#### gap\_between\_bounds

```python
@property
def gap_between_bounds() -> float
```

(float):  [Read-Write] 资产包围盒的间距

<a id="unreal.AesInstanceSplineAssetTagData.gap_between_bounds"></a>

#### gap\_between\_bounds

```python
@gap_between_bounds.setter
def gap_between_bounds(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.alignment_type"></a>

#### alignment\_type

```python
@property
def alignment_type() -> SplineAlignmentType
```

(SplineAlignmentType):  [Read-Write] 资产Z轴对齐类型

<a id="unreal.AesInstanceSplineAssetTagData.alignment_type"></a>

#### alignment\_type

```python
@alignment_type.setter
def alignment_type(value: SplineAlignmentType) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_scale_x"></a>

#### start\_scale\_x

```python
@property
def start_scale_x() -> float
```

(float):  [Read-Write] 样条线起点X轴方向缩放值

<a id="unreal.AesInstanceSplineAssetTagData.start_scale_x"></a>

#### start\_scale\_x

```python
@start_scale_x.setter
def start_scale_x(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_scale_x"></a>

#### end\_scale\_x

```python
@property
def end_scale_x() -> float
```

(float):  [Read-Write] 样条线终点X轴方向缩放值

<a id="unreal.AesInstanceSplineAssetTagData.end_scale_x"></a>

#### end\_scale\_x

```python
@end_scale_x.setter
def end_scale_x(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.keep_tan_value"></a>

#### keep\_tan\_value

```python
@property
def keep_tan_value() -> bool
```

(bool):  [Read-Write] 是否改变起始点Tan值

<a id="unreal.AesInstanceSplineAssetTagData.keep_tan_value"></a>

#### keep\_tan\_value

```python
@keep_tan_value.setter
def keep_tan_value(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.start_tan"></a>

#### start\_tan

```python
@property
def start_tan() -> Vector
```

(Vector):  [Read-Write] 起点切线值

<a id="unreal.AesInstanceSplineAssetTagData.start_tan"></a>

#### start\_tan

```python
@start_tan.setter
def start_tan(value: Vector) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.end_tan"></a>

#### end\_tan

```python
@property
def end_tan() -> Vector
```

(Vector):  [Read-Write] 终点切线值

<a id="unreal.AesInstanceSplineAssetTagData.end_tan"></a>

#### end\_tan

```python
@end_tan.setter
def end_tan(value: Vector) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.build_start_mesh"></a>

#### build\_start\_mesh

```python
@property
def build_start_mesh() -> bool
```

(bool):  [Read-Write] 是否生成起点模型

<a id="unreal.AesInstanceSplineAssetTagData.build_start_mesh"></a>

#### build\_start\_mesh

```python
@build_start_mesh.setter
def build_start_mesh(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.build_end_mesh"></a>

#### build\_end\_mesh

```python
@property
def build_end_mesh() -> bool
```

(bool):  [Read-Write] 是否生成终点模型

<a id="unreal.AesInstanceSplineAssetTagData.build_end_mesh"></a>

#### build\_end\_mesh

```python
@build_end_mesh.setter
def build_end_mesh(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 点是否倒角

<a id="unreal.AesInstanceSplineAssetTagData.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 切角长度

<a id="unreal.AesInstanceSplineAssetTagData.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.AesInstanceSplineAssetTagData.custom_data"></a>

#### custom\_data

```python
@property
def custom_data() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 自定义数据

<a id="unreal.AesInstanceSplineAssetTagData.custom_data"></a>

#### custom\_data

```python
@custom_data.setter
def custom_data(value: Map[Name, float]) -> None
```

<a id="unreal.AesInstanceSplineAssetData"></a>