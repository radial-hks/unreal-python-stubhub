## AesModularBuildingAssetTagData Objects

```python
class AesModularBuildingAssetTagData(StructBase)
```

模块化建筑标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesModularBuildingAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area`` (float):  [Read-Only] 轮廓线的面积，单位为平方米
- ``color`` (Color):  [Read-Write] 建筑立面颜色
- ``facade_asset`` (AesAssetChildMetaData):  [Read-Write] 立面资产模板
- ``facade_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 立面资产模板列表
- ``foundation_asset`` (AesAssetChildMetaData):  [Read-Write] 地基资产模板
- ``foundation_depth`` (float):  [Read-Write] 地基深度，用于计算建筑底部到地坑底部的距离
- ``height`` (float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备
- ``land_cover`` (LandCover):  [Read-Write] 用地类型
- ``levels`` (int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数
- ``min_height`` (float):  [Read-Write] 建筑最低点到轮廓线的高度
- ``min_level`` (int32):  [Read-Write] 建筑最低点所在楼层数
- ``mono_assets`` (Array[AesAssetChildMetaData]):  [Read-Write] 单体建筑资产引用列表
- ``outlines`` (Array[Vector]):  [Read-Write] 建筑预制体的轮廓线
- ``parapet_asset`` (AesAssetChildMetaData):  [Read-Write] 女儿墙资产模板
- ``prefab_id`` (str):  [Read-Write] 建筑所用预设编号
- ``prefab_type`` (AesBuildingPrefabType):  [Read-Write] 预设类型
- ``roof_asset`` (AesAssetChildMetaData):  [Read-Write] 屋顶资产模板
- ``roof_color`` (Color):  [Read-Write] 屋顶颜色
- ``roof_height`` (float):  [Read-Write] 屋顶高度
- ``roof_levels`` (int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数
- ``roof_prop_asset`` (AesAssetChildMetaData):  [Read-Write] 屋顶摆件资产模板
- ``roof_shape`` (RoofShape):  [Read-Write] 屋顶形态
- ``type`` (Name):  [Read-Write] 建筑类型

<a id="unreal.AesModularBuildingAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(height: float = 0.000000,
             min_height: float = 0.000000,
             foundation_depth: float = 0.000000,
             levels: int = 0,
             min_level: int = 0,
             land_cover: LandCover = LandCover.CULTIVATED_LAND,
             type: Name = "None",
             color: Color = [0, 0, 0, 0],
             roof_height: float = 0.000000,
             roof_levels: int = 0,
             roof_shape: RoofShape = RoofShape.FLAT,
             roof_color: Color = [0, 0, 0, 0],
             prefab_type: AesBuildingPrefabType = AesBuildingPrefabType.NONE,
             prefab_id: str = "",
             facade_asset: AesAssetChildMetaData = [
                 ["None", 0, 0, "None", False, {}, "",
                  [""]], True, True, AesAssetTransformControlType.NONE,
                 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000, 0.000000],
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [], []
             ],
             facade_assets: Array[AesAssetChildMetaData] = [],
             roof_asset: AesAssetChildMetaData = [
                 ["None", 0, 0, "None", False, {}, "",
                  [""]], True, True, AesAssetTransformControlType.NONE,
                 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000, 0.000000],
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [], []
             ],
             parapet_asset: AesAssetChildMetaData = [
                 ["None", 0, 0, "None", False, {}, "",
                  [""]], True, True, AesAssetTransformControlType.NONE,
                 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000, 0.000000],
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [], []
             ],
             roof_prop_asset: AesAssetChildMetaData = [
                 ["None", 0, 0, "None", False, {}, "",
                  [""]], True, True, AesAssetTransformControlType.NONE,
                 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000, 0.000000],
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [], []
             ],
             foundation_asset: AesAssetChildMetaData = [
                 ["None", 0, 0, "None", False, {}, "",
                  [""]], True, True, AesAssetTransformControlType.NONE,
                 0.000000, 0.000000, 0.000000, [0.000000, 0.000000, 0.000000],
                 [0.000000, 0.000000,
                  0.000000], [0.000000, 0.000000, 0.000000],
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [], []
             ],
             mono_assets: Array[AesAssetChildMetaData] = [],
             outlines: Array[Vector] = [],
             area: float = 0.000000) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 建筑物屋顶最高点到轮廓线的高度，不包括安装在屋顶上的天线、塔尖和其他设备

<a id="unreal.AesModularBuildingAssetTagData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.min_height"></a>

#### min\_height

```python
@property
def min_height() -> float
```

(float):  [Read-Write] 建筑最低点到轮廓线的高度

<a id="unreal.AesModularBuildingAssetTagData.min_height"></a>

#### min\_height

```python
@min_height.setter
def min_height(value: float) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.foundation_depth"></a>

#### foundation\_depth

```python
@property
def foundation_depth() -> float
```

(float):  [Read-Write] 地基深度，用于计算建筑底部到地坑底部的距离

<a id="unreal.AesModularBuildingAssetTagData.foundation_depth"></a>

#### foundation\_depth

```python
@foundation_depth.setter
def foundation_depth(value: float) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 建筑楼层数，不包含屋顶楼层数

<a id="unreal.AesModularBuildingAssetTagData.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.min_level"></a>

#### min\_level

```python
@property
def min_level() -> int
```

(int32):  [Read-Write] 建筑最低点所在楼层数

<a id="unreal.AesModularBuildingAssetTagData.min_level"></a>

#### min\_level

```python
@min_level.setter
def min_level(value: int) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.land_cover"></a>

#### land\_cover

```python
@property
def land_cover() -> LandCover
```

(LandCover):  [Read-Write] 用地类型

<a id="unreal.AesModularBuildingAssetTagData.land_cover"></a>

#### land\_cover

```python
@land_cover.setter
def land_cover(value: LandCover) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write] 建筑类型

<a id="unreal.AesModularBuildingAssetTagData.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] 建筑立面颜色

<a id="unreal.AesModularBuildingAssetTagData.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_height"></a>

#### roof\_height

```python
@property
def roof_height() -> float
```

(float):  [Read-Write] 屋顶高度

<a id="unreal.AesModularBuildingAssetTagData.roof_height"></a>

#### roof\_height

```python
@roof_height.setter
def roof_height(value: float) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_levels"></a>

#### roof\_levels

```python
@property
def roof_levels() -> int
```

(int32):  [Read-Write] 屋顶楼层数，该数值未计入建筑楼层数

<a id="unreal.AesModularBuildingAssetTagData.roof_levels"></a>

#### roof\_levels

```python
@roof_levels.setter
def roof_levels(value: int) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_shape"></a>

#### roof\_shape

```python
@property
def roof_shape() -> RoofShape
```

(RoofShape):  [Read-Write] 屋顶形态

<a id="unreal.AesModularBuildingAssetTagData.roof_shape"></a>

#### roof\_shape

```python
@roof_shape.setter
def roof_shape(value: RoofShape) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_color"></a>

#### roof\_color

```python
@property
def roof_color() -> Color
```

(Color):  [Read-Write] 屋顶颜色

<a id="unreal.AesModularBuildingAssetTagData.roof_color"></a>

#### roof\_color

```python
@roof_color.setter
def roof_color(value: Color) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.prefab_type"></a>

#### prefab\_type

```python
@property
def prefab_type() -> AesBuildingPrefabType
```

(AesBuildingPrefabType):  [Read-Write] 预设类型

<a id="unreal.AesModularBuildingAssetTagData.prefab_type"></a>

#### prefab\_type

```python
@prefab_type.setter
def prefab_type(value: AesBuildingPrefabType) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.prefab_id"></a>

#### prefab\_id

```python
@property
def prefab_id() -> str
```

(str):  [Read-Write] 建筑所用预设编号

<a id="unreal.AesModularBuildingAssetTagData.prefab_id"></a>

#### prefab\_id

```python
@prefab_id.setter
def prefab_id(value: str) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.facade_asset"></a>

#### facade\_asset

```python
@property
def facade_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 立面资产模板

<a id="unreal.AesModularBuildingAssetTagData.facade_asset"></a>

#### facade\_asset

```python
@facade_asset.setter
def facade_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.facade_assets"></a>

#### facade\_assets

```python
@property
def facade_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 立面资产模板列表

<a id="unreal.AesModularBuildingAssetTagData.facade_assets"></a>

#### facade\_assets

```python
@facade_assets.setter
def facade_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_asset"></a>

#### roof\_asset

```python
@property
def roof_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 屋顶资产模板

<a id="unreal.AesModularBuildingAssetTagData.roof_asset"></a>

#### roof\_asset

```python
@roof_asset.setter
def roof_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.parapet_asset"></a>

#### parapet\_asset

```python
@property
def parapet_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 女儿墙资产模板

<a id="unreal.AesModularBuildingAssetTagData.parapet_asset"></a>

#### parapet\_asset

```python
@parapet_asset.setter
def parapet_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.roof_prop_asset"></a>

#### roof\_prop\_asset

```python
@property
def roof_prop_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 屋顶摆件资产模板

<a id="unreal.AesModularBuildingAssetTagData.roof_prop_asset"></a>

#### roof\_prop\_asset

```python
@roof_prop_asset.setter
def roof_prop_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.foundation_asset"></a>

#### foundation\_asset

```python
@property
def foundation_asset() -> AesAssetChildMetaData
```

(AesAssetChildMetaData):  [Read-Write] 地基资产模板

<a id="unreal.AesModularBuildingAssetTagData.foundation_asset"></a>

#### foundation\_asset

```python
@foundation_asset.setter
def foundation_asset(value: AesAssetChildMetaData) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.mono_assets"></a>

#### mono\_assets

```python
@property
def mono_assets() -> Array[AesAssetChildMetaData]
```

(Array[AesAssetChildMetaData]):  [Read-Write] 单体建筑资产引用列表

<a id="unreal.AesModularBuildingAssetTagData.mono_assets"></a>

#### mono\_assets

```python
@mono_assets.setter
def mono_assets(value: Array[AesAssetChildMetaData]) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.outlines"></a>

#### outlines

```python
@property
def outlines() -> Array[Vector]
```

(Array[Vector]):  [Read-Write] 建筑预制体的轮廓线

<a id="unreal.AesModularBuildingAssetTagData.outlines"></a>

#### outlines

```python
@outlines.setter
def outlines(value: Array[Vector]) -> None
```

<a id="unreal.AesModularBuildingAssetTagData.area"></a>

#### area

```python
@property
def area() -> float
```

(float):  [Read-Only] 轮廓线的面积，单位为平方米

<a id="unreal.AesModularBuildingAssetData"></a>