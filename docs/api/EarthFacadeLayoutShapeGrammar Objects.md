## EarthFacadeLayoutShapeGrammar Objects

```python
class EarthFacadeLayoutShapeGrammar(EarthFacadeLayoutBase)
```

定义由形状语法组成的立面布局的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFacadeFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction_type`` (uint8):  [Read-Write] 立面方位类型
- ``grid_definition`` (Array[EarthShapeGrammarGridInfo]):  [Read-Write] 立面网格信息定义集

<a id="unreal.EarthFacadeLayoutShapeGrammar.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction_type: int = 0,
             grid_definition: Array[EarthShapeGrammarGridInfo] = []) -> None
```

<a id="unreal.EarthFacadeLayoutShapeGrammar.grid_definition"></a>

#### grid\_definition

```python
@property
def grid_definition() -> Array[EarthShapeGrammarGridInfo]
```

(Array[EarthShapeGrammarGridInfo]):  [Read-Write] 立面网格信息定义集

<a id="unreal.EarthFacadeLayoutShapeGrammar.grid_definition"></a>

#### grid\_definition

```python
@grid_definition.setter
def grid_definition(value: Array[EarthShapeGrammarGridInfo]) -> None
```

<a id="unreal.EarthShapeGrammarGridInfo"></a>