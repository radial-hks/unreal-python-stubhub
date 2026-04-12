## EarthBuildingFragment Objects

```python
class EarthBuildingFragment(EarthEntityFragment)
```

定义建筑数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthBuildingFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additional_types`` (Array[Name]):  [Read-Write] 额外的可适配建筑类型列表
- ``color`` (LinearColor):  [Read-Write] 建筑立面颜色
- ``foundation_depth`` (float):  [Read-Write] 地基深度，用于计算建筑底部到地坑底部的距离，单位为米
- ``height`` (float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备，单位为米
- ``height_offset_range`` (Vector2f):  [Read-Write] 高度适配时的偏移范围，单位为米，需叠加Height - MinHeight而得到的建筑实际高度使用
- ``land_cover`` (EarthLandCover):  [Read-Write] 用地类型
- ``land_use`` (Name):  [Read-Write] 土地用途
- ``levels`` (int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数
- ``min_height`` (float):  [Read-Write] 建筑最低点到轮廓线的高度，单位为米
- ``min_level`` (int32):  [Read-Write] 建筑最低点所在楼层数
- ``roof_color`` (LinearColor):  [Read-Write] 屋顶颜色
- ``roof_height`` (float):  [Read-Write] 屋顶高度，单位为米
- ``roof_levels`` (int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数
- ``roof_shape`` (EarthRoofShape):  [Read-Write] 屋顶形态
- ``supported_footprint_types`` (Array[EarthBuildingFootprintType]):  [Read-Write] 可适配的建筑轮廓类型列表
- ``type`` (Name):  [Read-Write] 建筑类型
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthBuildingFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        height: float = 0.000000,
        min_height: float = 0.000000,
        foundation_depth: float = 0.000000,
        levels: int = 0,
        min_level: int = 0,
        land_cover: EarthLandCover = EarthLandCover.CULTIVATED_LAND,
        land_use: Name = "None",
        type: Name = "None",
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        roof_height: float = 0.000000,
        roof_levels: int = 0,
        roof_shape: EarthRoofShape = EarthRoofShape.FLAT,
        roof_color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
        height_offset_range: Vector2f = [0.000000, 0.000000],
        additional_types: Array[Name] = [],
        supported_footprint_types: Array[EarthBuildingFootprintType] = []
) -> None
```

<a id="unreal.EarthBuildingFragment.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备，单位为米

<a id="unreal.EarthBuildingFragment.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthBuildingFragment.min_height"></a>

#### min\_height

```python
@property
def min_height() -> float
```

(float):  [Read-Write] 建筑最低点到轮廓线的高度，单位为米

<a id="unreal.EarthBuildingFragment.min_height"></a>

#### min\_height

```python
@min_height.setter
def min_height(value: float) -> None
```

<a id="unreal.EarthBuildingFragment.foundation_depth"></a>

#### foundation\_depth

```python
@property
def foundation_depth() -> float
```

(float):  [Read-Write] 地基深度，用于计算建筑底部到地坑底部的距离，单位为米

<a id="unreal.EarthBuildingFragment.foundation_depth"></a>

#### foundation\_depth

```python
@foundation_depth.setter
def foundation_depth(value: float) -> None
```

<a id="unreal.EarthBuildingFragment.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数

<a id="unreal.EarthBuildingFragment.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.EarthBuildingFragment.min_level"></a>

#### min\_level

```python
@property
def min_level() -> int
```

(int32):  [Read-Write] 建筑最低点所在楼层数

<a id="unreal.EarthBuildingFragment.min_level"></a>

#### min\_level

```python
@min_level.setter
def min_level(value: int) -> None
```

<a id="unreal.EarthBuildingFragment.land_cover"></a>

#### land\_cover

```python
@property
def land_cover() -> EarthLandCover
```

(EarthLandCover):  [Read-Write] 用地类型

<a id="unreal.EarthBuildingFragment.land_cover"></a>

#### land\_cover

```python
@land_cover.setter
def land_cover(value: EarthLandCover) -> None
```

<a id="unreal.EarthBuildingFragment.land_use"></a>

#### land\_use

```python
@property
def land_use() -> Name
```

(Name):  [Read-Write] 土地用途

<a id="unreal.EarthBuildingFragment.land_use"></a>

#### land\_use

```python
@land_use.setter
def land_use(value: Name) -> None
```

<a id="unreal.EarthBuildingFragment.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write] 建筑类型

<a id="unreal.EarthBuildingFragment.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EarthBuildingFragment.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write] 建筑立面颜色

<a id="unreal.EarthBuildingFragment.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.EarthBuildingFragment.roof_height"></a>

#### roof\_height

```python
@property
def roof_height() -> float
```

(float):  [Read-Write] 屋顶高度，单位为米

<a id="unreal.EarthBuildingFragment.roof_height"></a>

#### roof\_height

```python
@roof_height.setter
def roof_height(value: float) -> None
```

<a id="unreal.EarthBuildingFragment.roof_levels"></a>

#### roof\_levels

```python
@property
def roof_levels() -> int
```

(int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数

<a id="unreal.EarthBuildingFragment.roof_levels"></a>

#### roof\_levels

```python
@roof_levels.setter
def roof_levels(value: int) -> None
```

<a id="unreal.EarthBuildingFragment.roof_shape"></a>

#### roof\_shape

```python
@property
def roof_shape() -> EarthRoofShape
```

(EarthRoofShape):  [Read-Write] 屋顶形态

<a id="unreal.EarthBuildingFragment.roof_shape"></a>

#### roof\_shape

```python
@roof_shape.setter
def roof_shape(value: EarthRoofShape) -> None
```

<a id="unreal.EarthBuildingFragment.roof_color"></a>

#### roof\_color

```python
@property
def roof_color() -> LinearColor
```

(LinearColor):  [Read-Write] 屋顶颜色

<a id="unreal.EarthBuildingFragment.roof_color"></a>

#### roof\_color

```python
@roof_color.setter
def roof_color(value: LinearColor) -> None
```

<a id="unreal.EarthBuildingFragment.height_offset_range"></a>

#### height\_offset\_range

```python
@property
def height_offset_range() -> Vector2f
```

(Vector2f):  [Read-Write] 高度适配时的偏移范围，单位为米，需叠加Height - MinHeight而得到的建筑实际高度使用

<a id="unreal.EarthBuildingFragment.height_offset_range"></a>

#### height\_offset\_range

```python
@height_offset_range.setter
def height_offset_range(value: Vector2f) -> None
```

<a id="unreal.EarthBuildingFragment.additional_types"></a>

#### additional\_types

```python
@property
def additional_types() -> Array[Name]
```

(Array[Name]):  [Read-Write] 额外的可适配建筑类型列表

<a id="unreal.EarthBuildingFragment.additional_types"></a>

#### additional\_types

```python
@additional_types.setter
def additional_types(value: Array[Name]) -> None
```

<a id="unreal.EarthBuildingFragment.supported_footprint_types"></a>

#### supported\_footprint\_types

```python
@property
def supported_footprint_types() -> Array[EarthBuildingFootprintType]
```

(Array[EarthBuildingFootprintType]):  [Read-Write] 可适配的建筑轮廓类型列表

<a id="unreal.EarthBuildingFragment.supported_footprint_types"></a>

#### supported\_footprint\_types

```python
@supported_footprint_types.setter
def supported_footprint_types(
        value: Array[EarthBuildingFootprintType]) -> None
```

<a id="unreal.EarthDataBase"></a>