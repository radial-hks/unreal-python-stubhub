## EarthShapeGrammarSelector Objects

```python
class EarthShapeGrammarSelector(StructBase)
```

形状语法匹配器

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarSelector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``compared_value_attribute`` (Name):  [Read-Write] 【匹配属性】用于比较的数值型参数字段名
- ``criteria`` (Array[EarthSelectGrammarCriterion]):  [Read-Write] 【规则列表】按数组顺序评估匹配规则（优先级从上到下）

<a id="unreal.EarthShapeGrammarSelector.__init__"></a>

#### \_\_init\_\_

```python
def __init__(compared_value_attribute: Name = "None",
             criteria: Array[EarthSelectGrammarCriterion] = []) -> None
```

<a id="unreal.EarthShapeGrammarSelector.compared_value_attribute"></a>

#### compared\_value\_attribute

```python
@property
def compared_value_attribute() -> Name
```

(Name):  [Read-Write] 【匹配属性】用于比较的数值型参数字段名

<a id="unreal.EarthShapeGrammarSelector.compared_value_attribute"></a>

#### compared\_value\_attribute

```python
@compared_value_attribute.setter
def compared_value_attribute(value: Name) -> None
```

<a id="unreal.EarthShapeGrammarSelector.criteria"></a>

#### criteria

```python
@property
def criteria() -> Array[EarthSelectGrammarCriterion]
```

(Array[EarthSelectGrammarCriterion]):  [Read-Write] 【规则列表】按数组顺序评估匹配规则（优先级从上到下）

<a id="unreal.EarthShapeGrammarSelector.criteria"></a>

#### criteria

```python
@criteria.setter
def criteria(value: Array[EarthSelectGrammarCriterion]) -> None
```

<a id="unreal.EarthSelectGrammarCriterion"></a>