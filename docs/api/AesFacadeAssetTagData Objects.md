## AesFacadeAssetTagData Objects

```python
class AesFacadeAssetTagData(StructBase)
```

立面资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesFacadeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (Color):  [Read-Write] 立面颜色
- ``facade_materials`` (Map[AesFacadeDirectionType, AesFacadeMaterialInfo]):  [Read-Write] 立面模型的材质列表
- ``height`` (float):  [Read-Write] 立面高度
- ``height_offset`` (float):  [Read-Write] 立面高度偏移值
- ``layout_type`` (AesFacadeLayoutType):  [Read-Write] 立面布局类型
- ``level_corners`` (str):  [Read-Write]
- ``level_definition`` (Map[Name, AesFacadeLevelData]):  [Read-Write]
- ``level_grammar`` (str):  [Read-Write]
- ``levels`` (int32):  [Read-Write] 立面层数
- ``module_definition`` (Map[Name, AesFacadeModuleData]):  [Read-Write]
- ``shape_grammars`` (Map[AesFacadeDirectionType, AesFacadeShapeGrammar]):  [Read-Write] 形状语法列表
- ``wall_asset`` (AesAssetMetaData):  [Read-Write] 默认墙面资产模板
- ``wall_assets`` (Map[AesFacadeDirectionType, AesAssetMetaData]):  [Read-Write] 墙面资产模板列表

<a id="unreal.AesFacadeAssetTagData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    height: float = 0.000000,
    height_offset: float = 0.000000,
    levels: int = 0,
    color: Color = [0, 0, 0, 0],
    layout_type: AesFacadeLayoutType = AesFacadeLayoutType.SINGLE,
    wall_asset: AesAssetMetaData = ["None", 0, 0, "None", False, {}, "", [""]],
    wall_assets: Map[AesFacadeDirectionType, AesAssetMetaData] = {},
    module_definition: Map[Name, AesFacadeModuleData] = {},
    level_definition: Map[Name, AesFacadeLevelData] = {},
    level_grammar: str = "",
    shape_grammars: Map[AesFacadeDirectionType, AesFacadeShapeGrammar] = {},
    facade_materials: Map[AesFacadeDirectionType, AesFacadeMaterialInfo] = {}
) -> None
```

<a id="unreal.AesFacadeAssetTagData.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 立面高度

<a id="unreal.AesFacadeAssetTagData.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesFacadeAssetTagData.height_offset"></a>

#### height\_offset

```python
@property
def height_offset() -> float
```

(float):  [Read-Write] 立面高度偏移值

<a id="unreal.AesFacadeAssetTagData.height_offset"></a>

#### height\_offset

```python
@height_offset.setter
def height_offset(value: float) -> None
```

<a id="unreal.AesFacadeAssetTagData.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] 立面层数

<a id="unreal.AesFacadeAssetTagData.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesFacadeAssetTagData.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] 立面颜色

<a id="unreal.AesFacadeAssetTagData.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.AesFacadeAssetTagData.layout_type"></a>

#### layout\_type

```python
@property
def layout_type() -> AesFacadeLayoutType
```

(AesFacadeLayoutType):  [Read-Write] 立面布局类型

<a id="unreal.AesFacadeAssetTagData.layout_type"></a>

#### layout\_type

```python
@layout_type.setter
def layout_type(value: AesFacadeLayoutType) -> None
```

<a id="unreal.AesFacadeAssetTagData.wall_asset"></a>

#### wall\_asset

```python
@property
def wall_asset() -> AesAssetMetaData
```

(AesAssetMetaData):  [Read-Write] 默认墙面资产模板

<a id="unreal.AesFacadeAssetTagData.wall_asset"></a>

#### wall\_asset

```python
@wall_asset.setter
def wall_asset(value: AesAssetMetaData) -> None
```

<a id="unreal.AesFacadeAssetTagData.wall_assets"></a>

#### wall\_assets

```python
@property
def wall_assets() -> Map[AesFacadeDirectionType, AesAssetMetaData]
```

(Map[AesFacadeDirectionType, AesAssetMetaData]):  [Read-Write] 墙面资产模板列表

<a id="unreal.AesFacadeAssetTagData.wall_assets"></a>

#### wall\_assets

```python
@wall_assets.setter
def wall_assets(value: Map[AesFacadeDirectionType, AesAssetMetaData]) -> None
```

<a id="unreal.AesFacadeAssetTagData.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> Map[Name, AesFacadeModuleData]
```

(Map[Name, AesFacadeModuleData]):  [Read-Write]

<a id="unreal.AesFacadeAssetTagData.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: Map[Name, AesFacadeModuleData]) -> None
```

<a id="unreal.AesFacadeAssetTagData.level_definition"></a>

#### level\_definition

```python
@property
def level_definition() -> Map[Name, AesFacadeLevelData]
```

(Map[Name, AesFacadeLevelData]):  [Read-Write]

<a id="unreal.AesFacadeAssetTagData.level_definition"></a>

#### level\_definition

```python
@level_definition.setter
def level_definition(value: Map[Name, AesFacadeLevelData]) -> None
```

<a id="unreal.AesFacadeAssetTagData.level_grammar"></a>

#### level\_grammar

```python
@property
def level_grammar() -> str
```

(str):  [Read-Write]

<a id="unreal.AesFacadeAssetTagData.level_grammar"></a>

#### level\_grammar

```python
@level_grammar.setter
def level_grammar(value: str) -> None
```

<a id="unreal.AesFacadeAssetTagData.shape_grammars"></a>

#### shape\_grammars

```python
@property
def shape_grammars() -> Map[AesFacadeDirectionType, AesFacadeShapeGrammar]
```

(Map[AesFacadeDirectionType, AesFacadeShapeGrammar]):  [Read-Write] 形状语法列表

<a id="unreal.AesFacadeAssetTagData.shape_grammars"></a>

#### shape\_grammars

```python
@shape_grammars.setter
def shape_grammars(
        value: Map[AesFacadeDirectionType, AesFacadeShapeGrammar]) -> None
```

<a id="unreal.AesFacadeAssetTagData.facade_materials"></a>

#### facade\_materials

```python
@property
def facade_materials() -> Map[AesFacadeDirectionType, AesFacadeMaterialInfo]
```

(Map[AesFacadeDirectionType, AesFacadeMaterialInfo]):  [Read-Write] 立面模型的材质列表

<a id="unreal.AesFacadeAssetTagData.facade_materials"></a>

#### facade\_materials

```python
@facade_materials.setter
def facade_materials(
        value: Map[AesFacadeDirectionType, AesFacadeMaterialInfo]) -> None
```

<a id="unreal.AesFacadeAssetData"></a>