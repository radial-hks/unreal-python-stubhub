## EarthFacadeFragment Objects

```python
class EarthFacadeFragment(EarthFacadeBaseFragment)
```

定义立面数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 立面颜色
- ``footprint_offset`` (float):  [Read-Write] 轮廓线偏移距离，正值为放大，负值为缩小
- ``grammars`` (Array[str]):  [Read-Write] 立面的层语法集
- ``height`` (float):  [Read-Write] 立面高度，单位为米
- ``height_offset`` (float):  [Read-Write] 立面高度偏移值，单位为米
- ``level_definition`` (Array[EarthFacadeLevelInfo]):  [Read-Write] 立面所用层的定义集
- ``level_symbol_selectors`` (Array[EarthShapeGrammarSelector]):  [Read-Write] 层符号匹配器，可在匹配条件下将一种层符号映射为另一种层符号
- ``levels`` (int32):  [Read-Write] 立面层数
- ``module_definition`` (Array[EarthFacadeModuleInfo]):  [Read-Write] 立面所用模块的定义集
- ``recompute_seed_by_edge`` (bool):  [Read-Write] 是否为每条边重新计算随机种子
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFacadeFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             height: float = 0.000000,
             height_offset: float = 0.000000,
             levels: int = 0,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             footprint_offset: float = 0.000000,
             module_definition: Array[EarthFacadeModuleInfo] = [],
             level_definition: Array[EarthFacadeLevelInfo] = [],
             level_symbol_selectors: Array[EarthShapeGrammarSelector] = [],
             grammars: Array[str] = [],
             recompute_seed_by_edge: bool = False) -> None
```

<a id="unreal.EarthFacadeFragment.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> Array[EarthFacadeModuleInfo]
```

(Array[EarthFacadeModuleInfo]):  [Read-Write] 立面所用模块的定义集

<a id="unreal.EarthFacadeFragment.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: Array[EarthFacadeModuleInfo]) -> None
```

<a id="unreal.EarthFacadeFragment.level_definition"></a>

#### level\_definition

```python
@property
def level_definition() -> Array[EarthFacadeLevelInfo]
```

(Array[EarthFacadeLevelInfo]):  [Read-Write] 立面所用层的定义集

<a id="unreal.EarthFacadeFragment.level_definition"></a>

#### level\_definition

```python
@level_definition.setter
def level_definition(value: Array[EarthFacadeLevelInfo]) -> None
```

<a id="unreal.EarthFacadeFragment.level_symbol_selectors"></a>

#### level\_symbol\_selectors

```python
@property
def level_symbol_selectors() -> Array[EarthShapeGrammarSelector]
```

(Array[EarthShapeGrammarSelector]):  [Read-Write] 层符号匹配器，可在匹配条件下将一种层符号映射为另一种层符号

<a id="unreal.EarthFacadeFragment.level_symbol_selectors"></a>

#### level\_symbol\_selectors

```python
@level_symbol_selectors.setter
def level_symbol_selectors(value: Array[EarthShapeGrammarSelector]) -> None
```

<a id="unreal.EarthFacadeFragment.grammars"></a>

#### grammars

```python
@property
def grammars() -> Array[str]
```

(Array[str]):  [Read-Write] 立面的层语法集

<a id="unreal.EarthFacadeFragment.grammars"></a>

#### grammars

```python
@grammars.setter
def grammars(value: Array[str]) -> None
```

<a id="unreal.EarthFacadeFragment.recompute_seed_by_edge"></a>

#### recompute\_seed\_by\_edge

```python
@property
def recompute_seed_by_edge() -> bool
```

(bool):  [Read-Write] 是否为每条边重新计算随机种子

<a id="unreal.EarthFacadeFragment.recompute_seed_by_edge"></a>

#### recompute\_seed\_by\_edge

```python
@recompute_seed_by_edge.setter
def recompute_seed_by_edge(value: bool) -> None
```

<a id="unreal.EarthFacadeLayoutBase"></a>