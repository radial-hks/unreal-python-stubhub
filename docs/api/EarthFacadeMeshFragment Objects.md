## EarthFacadeMeshFragment Objects

```python
class EarthFacadeMeshFragment(EarthFacadeBaseFragment)
```

定义立面网格体数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write] 立面颜色
- ``default_material_symbol`` (Name):  [Read-Write] 立面默认材质符号
- ``facade_materials`` (Array[EarthMaterialInfo]):  [Read-Write] 立面所用材质的定义集
- ``footprint_offset`` (float):  [Read-Write] 轮廓线偏移距离，正值为放大，负值为缩小
- ``height`` (float):  [Read-Write] 立面高度，单位为米
- ``height_offset`` (float):  [Read-Write] 立面高度偏移值，单位为米
- ``levels`` (int32):  [Read-Write] 立面层数
- ``symbol_selectors`` (Array[EarthShapeGrammarSelector]):  [Read-Write] 材质符号匹配器，可在匹配条件下将一种材质符号映射为另一种材质符号
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFacadeMeshFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             height: float = 0.000000,
             height_offset: float = 0.000000,
             levels: int = 0,
             color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
             footprint_offset: float = 0.000000,
             facade_materials: Array[EarthMaterialInfo] = [],
             default_material_symbol: Name = "None",
             symbol_selectors: Array[EarthShapeGrammarSelector] = []) -> None
```

<a id="unreal.EarthFacadeMeshFragment.facade_materials"></a>

#### facade\_materials

```python
@property
def facade_materials() -> Array[EarthMaterialInfo]
```

(Array[EarthMaterialInfo]):  [Read-Write] 立面所用材质的定义集

<a id="unreal.EarthFacadeMeshFragment.facade_materials"></a>

#### facade\_materials

```python
@facade_materials.setter
def facade_materials(value: Array[EarthMaterialInfo]) -> None
```

<a id="unreal.EarthFacadeMeshFragment.default_material_symbol"></a>

#### default\_material\_symbol

```python
@property
def default_material_symbol() -> Name
```

(Name):  [Read-Write] 立面默认材质符号

<a id="unreal.EarthFacadeMeshFragment.default_material_symbol"></a>

#### default\_material\_symbol

```python
@default_material_symbol.setter
def default_material_symbol(value: Name) -> None
```

<a id="unreal.EarthFacadeMeshFragment.symbol_selectors"></a>

#### symbol\_selectors

```python
@property
def symbol_selectors() -> Array[EarthShapeGrammarSelector]
```

(Array[EarthShapeGrammarSelector]):  [Read-Write] 材质符号匹配器，可在匹配条件下将一种材质符号映射为另一种材质符号

<a id="unreal.EarthFacadeMeshFragment.symbol_selectors"></a>

#### symbol\_selectors

```python
@symbol_selectors.setter
def symbol_selectors(value: Array[EarthShapeGrammarSelector]) -> None
```

<a id="unreal.EarthShapeGrammarSelector"></a>