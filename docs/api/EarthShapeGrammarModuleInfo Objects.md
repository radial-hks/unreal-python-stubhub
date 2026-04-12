## EarthShapeGrammarModuleInfo Objects

```python
class EarthShapeGrammarModuleInfo(StructBase)
```

定义用于形状语法的模块信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_scale`` (bool):  [Read-Write] 模块是否应用缩放
- ``asset`` (EarthPrefabAsset):  [Read-Write] 模块资产引用
- ``custom_length`` (float):  [Read-Write] 自定义模块长度
- ``flip_mesh`` (bool):  [Read-Write] 模块是否翻转
- ``min_scale_factor`` (float):  [Read-Write] 最小缩放因子
- ``pivot_location`` (Vector):  [Read-Write] 基于模块的包围盒尺寸，设置归一化的轴心位置
  例：全0表示移动轴心到包围盒最小点，全0.5表示移动轴心到包围盒中心点，全1表示移动轴心到包围盒最大点
- ``position_offset`` (Vector):  [Read-Write] 模块偏移值
- ``replacement_module`` (Name):  [Read-Write] 模块长度替代
- ``scalable`` (bool):  [Read-Write] 模块是否可以缩放以适应剩余空间
- ``symbol`` (Name):  [Read-Write] 模块在形状语法中的符号
- ``use_as_placeholder`` (bool):  [Read-Write] 是否作为占位符使用
- ``use_custom_length`` (bool):  [Read-Write] 是否使用自定义模块尺寸
- ``use_custom_pivot_location`` (bool):  [Read-Write] 是否使用自定义的归一化的轴心位置
- ``variations`` (Map[Name, float]):  [Read-Write] 模块变体列表
- ``weight`` (float):  [Read-Write] 模块权重

<a id="unreal.EarthShapeGrammarModuleInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(symbol: Name = "None",
             asset: EarthPrefabAsset = None,
             use_custom_length: bool = False,
             custom_length: float = 0.000000,
             weight: float = 0.000000,
             min_scale_factor: float = 0.000000,
             use_as_placeholder: bool = False,
             scalable: bool = False,
             apply_scale: bool = False,
             flip_mesh: bool = False,
             position_offset: Vector = [0.000000, 0.000000, 0.000000],
             use_custom_pivot_location: bool = False,
             pivot_location: Vector = [0.000000, 0.000000, 0.000000],
             variations: Map[Name, float] = {},
             replacement_module: Name = "None") -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 模块在形状语法中的符号

<a id="unreal.EarthShapeGrammarModuleInfo.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.asset"></a>

#### asset

```python
@property
def asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 模块资产引用

<a id="unreal.EarthShapeGrammarModuleInfo.asset"></a>

#### asset

```python
@asset.setter
def asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.use_custom_length"></a>

#### use\_custom\_length

```python
@property
def use_custom_length() -> bool
```

(bool):  [Read-Write] 是否使用自定义模块尺寸

<a id="unreal.EarthShapeGrammarModuleInfo.use_custom_length"></a>

#### use\_custom\_length

```python
@use_custom_length.setter
def use_custom_length(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.custom_length"></a>

#### custom\_length

```python
@property
def custom_length() -> float
```

(float):  [Read-Write] 自定义模块长度

<a id="unreal.EarthShapeGrammarModuleInfo.custom_length"></a>

#### custom\_length

```python
@custom_length.setter
def custom_length(value: float) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] 模块权重

<a id="unreal.EarthShapeGrammarModuleInfo.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.min_scale_factor"></a>

#### min\_scale\_factor

```python
@property
def min_scale_factor() -> float
```

(float):  [Read-Write] 最小缩放因子

<a id="unreal.EarthShapeGrammarModuleInfo.min_scale_factor"></a>

#### min\_scale\_factor

```python
@min_scale_factor.setter
def min_scale_factor(value: float) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@property
def use_as_placeholder() -> bool
```

(bool):  [Read-Write] 是否作为占位符使用

<a id="unreal.EarthShapeGrammarModuleInfo.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@use_as_placeholder.setter
def use_as_placeholder(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.scalable"></a>

#### scalable

```python
@property
def scalable() -> bool
```

(bool):  [Read-Write] 模块是否可以缩放以适应剩余空间

<a id="unreal.EarthShapeGrammarModuleInfo.scalable"></a>

#### scalable

```python
@scalable.setter
def scalable(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.apply_scale"></a>

#### apply\_scale

```python
@property
def apply_scale() -> bool
```

(bool):  [Read-Write] 模块是否应用缩放

<a id="unreal.EarthShapeGrammarModuleInfo.apply_scale"></a>

#### apply\_scale

```python
@apply_scale.setter
def apply_scale(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.flip_mesh"></a>

#### flip\_mesh

```python
@property
def flip_mesh() -> bool
```

(bool):  [Read-Write] 模块是否翻转

<a id="unreal.EarthShapeGrammarModuleInfo.flip_mesh"></a>

#### flip\_mesh

```python
@flip_mesh.setter
def flip_mesh(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.position_offset"></a>

#### position\_offset

```python
@property
def position_offset() -> Vector
```

(Vector):  [Read-Write] 模块偏移值

<a id="unreal.EarthShapeGrammarModuleInfo.position_offset"></a>

#### position\_offset

```python
@position_offset.setter
def position_offset(value: Vector) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.use_custom_pivot_location"></a>

#### use\_custom\_pivot\_location

```python
@property
def use_custom_pivot_location() -> bool
```

(bool):  [Read-Write] 是否使用自定义的归一化的轴心位置

<a id="unreal.EarthShapeGrammarModuleInfo.use_custom_pivot_location"></a>

#### use\_custom\_pivot\_location

```python
@use_custom_pivot_location.setter
def use_custom_pivot_location(value: bool) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.pivot_location"></a>

#### pivot\_location

```python
@property
def pivot_location() -> Vector
```

(Vector):  [Read-Write] 基于模块的包围盒尺寸，设置归一化的轴心位置
例：全0表示移动轴心到包围盒最小点，全0.5表示移动轴心到包围盒中心点，全1表示移动轴心到包围盒最大点

<a id="unreal.EarthShapeGrammarModuleInfo.pivot_location"></a>

#### pivot\_location

```python
@pivot_location.setter
def pivot_location(value: Vector) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.variations"></a>

#### variations

```python
@property
def variations() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 模块变体列表

<a id="unreal.EarthShapeGrammarModuleInfo.variations"></a>

#### variations

```python
@variations.setter
def variations(value: Map[Name, float]) -> None
```

<a id="unreal.EarthShapeGrammarModuleInfo.replacement_module"></a>

#### replacement\_module

```python
@property
def replacement_module() -> Name
```

(Name):  [Read-Write] 模块长度替代

<a id="unreal.EarthShapeGrammarModuleInfo.replacement_module"></a>

#### replacement\_module

```python
@replacement_module.setter
def replacement_module(value: Name) -> None
```

<a id="unreal.EarthPointParametersBase"></a>