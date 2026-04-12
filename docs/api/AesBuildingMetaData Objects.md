## AesBuildingMetaData Objects

```python
class AesBuildingMetaData(StructBase)
```

建筑数据元信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEarth
- **File**: AesBuildingCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (Color):  [Read-Write] 建筑立面颜色
- ``height`` (float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备
- ``id`` (int64):  [Read-Only] 建筑数据Id
- ``land_cover`` (LandCover):  [Read-Write] 用地类型
- ``levels`` (int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数
- ``min_height`` (float):  [Read-Write] 建筑最低点到轮廓线的高度
- ``min_level`` (int32):  [Read-Write] 建筑最低点所在楼层数
- ``name`` (Name):  [Read-Write] 建筑名称
- ``roof_color`` (Color):  [Read-Write] 屋顶颜色
- ``roof_height`` (float):  [Read-Write] 屋顶高度
- ``roof_levels`` (int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数
- ``roof_shape`` (RoofShape):  [Read-Write] 屋顶形态
- ``type`` (Name):  [Read-Write] 建筑类型

<a id="unreal.AesBuildingMetaData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name: Name = "None",
             height: float = 0.000000,
             min_height: float = 0.000000,
             levels: int = 0,
             min_level: int = 0,
             land_cover: LandCover = LandCover.CULTIVATED_LAND,
             type: Name = "None",
             color: Color = [0, 0, 0, 0],
             roof_height: float = 0.000000,
             roof_levels: int = 0,
             roof_shape: RoofShape = RoofShape.FLAT,
             roof_color: Color = [0, 0, 0, 0]) -> None
```

<a id="unreal.AesBuildingMetaData.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Write] 建筑名称

<a id="unreal.AesBuildingMetaData.name"></a>

#### name

```python
@name.setter
def name(value: Name) -> None
```

<a id="unreal.AesBuildingMetaData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备

<a id="unreal.AesBuildingMetaData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesBuildingMetaData.min_height"></a>

#### min\_height

```python
@property
def min_height() -> float
```

(float):  [Read-Write] 建筑最低点到轮廓线的高度

<a id="unreal.AesBuildingMetaData.min_height"></a>

#### min\_height

```python
@min_height.setter
def min_height(value: float) -> None
```

<a id="unreal.AesBuildingMetaData.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数

<a id="unreal.AesBuildingMetaData.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesBuildingMetaData.min_level"></a>

#### min\_level

```python
@property
def min_level() -> int
```

(int32):  [Read-Write] 建筑最低点所在楼层数

<a id="unreal.AesBuildingMetaData.min_level"></a>

#### min\_level

```python
@min_level.setter
def min_level(value: int) -> None
```

<a id="unreal.AesBuildingMetaData.land_cover"></a>

#### land\_cover

```python
@property
def land_cover() -> LandCover
```

(LandCover):  [Read-Write] 用地类型

<a id="unreal.AesBuildingMetaData.land_cover"></a>

#### land\_cover

```python
@land_cover.setter
def land_cover(value: LandCover) -> None
```

<a id="unreal.AesBuildingMetaData.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write] 建筑类型

<a id="unreal.AesBuildingMetaData.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.AesBuildingMetaData.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] 建筑立面颜色

<a id="unreal.AesBuildingMetaData.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.AesBuildingMetaData.roof_height"></a>

#### roof\_height

```python
@property
def roof_height() -> float
```

(float):  [Read-Write] 屋顶高度

<a id="unreal.AesBuildingMetaData.roof_height"></a>

#### roof\_height

```python
@roof_height.setter
def roof_height(value: float) -> None
```

<a id="unreal.AesBuildingMetaData.roof_levels"></a>

#### roof\_levels

```python
@property
def roof_levels() -> int
```

(int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数

<a id="unreal.AesBuildingMetaData.roof_levels"></a>

#### roof\_levels

```python
@roof_levels.setter
def roof_levels(value: int) -> None
```

<a id="unreal.AesBuildingMetaData.roof_shape"></a>

#### roof\_shape

```python
@property
def roof_shape() -> RoofShape
```

(RoofShape):  [Read-Write] 屋顶形态

<a id="unreal.AesBuildingMetaData.roof_shape"></a>

#### roof\_shape

```python
@roof_shape.setter
def roof_shape(value: RoofShape) -> None
```

<a id="unreal.AesBuildingMetaData.roof_color"></a>

#### roof\_color

```python
@property
def roof_color() -> Color
```

(Color):  [Read-Write] 屋顶颜色

<a id="unreal.AesBuildingMetaData.roof_color"></a>

#### roof\_color

```python
@roof_color.setter
def roof_color(value: Color) -> None
```

<a id="unreal.AesBuildingDimensionData"></a>