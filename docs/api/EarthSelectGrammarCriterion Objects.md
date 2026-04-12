## EarthSelectGrammarCriterion Objects

```python
class EarthSelectGrammarCriterion(StructBase)
```

形状语法匹配规则

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarSelector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``comparator`` (EarthSelectGrammarComparator):  [Read-Write] 【比较方式】选择判断逻辑（Select为无条件匹配）
- ``first_value`` (double):  [Read-Write] 【比较参考值】基础阈值（当比较方式为Select时不生效）
- ``result`` (str):  [Read-Write] 【匹配结果】满足条件时应用的符号名称
- ``second_value`` (double):  [Read-Write] 【范围限制】附加阈值（仅Range类型比较时生效）
  用于RangeExclusive时：基础阈值 < Value < 附加阈值
  用于RangeInclusive时：基础阈值 <= Value <= 附加阈值
- ``symbol`` (Name):  [Read-Write] 当前匹配规则所适用的符号名称

<a id="unreal.EarthSelectGrammarCriterion.__init__"></a>

#### \_\_init\_\_

```python
def __init__(symbol: Name = "None",
             comparator: EarthSelectGrammarComparator = 0,
             first_value: float = 0.000000,
             second_value: float = 0.000000,
             result: str = "") -> None
```

<a id="unreal.EarthSelectGrammarCriterion.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 当前匹配规则所适用的符号名称

<a id="unreal.EarthSelectGrammarCriterion.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthSelectGrammarCriterion.comparator"></a>

#### comparator

```python
@property
def comparator() -> EarthSelectGrammarComparator
```

(EarthSelectGrammarComparator):  [Read-Write] 【比较方式】选择判断逻辑（Select为无条件匹配）

<a id="unreal.EarthSelectGrammarCriterion.comparator"></a>

#### comparator

```python
@comparator.setter
def comparator(value: EarthSelectGrammarComparator) -> None
```

<a id="unreal.EarthSelectGrammarCriterion.first_value"></a>

#### first\_value

```python
@property
def first_value() -> float
```

(double):  [Read-Write] 【比较参考值】基础阈值（当比较方式为Select时不生效）

<a id="unreal.EarthSelectGrammarCriterion.first_value"></a>

#### first\_value

```python
@first_value.setter
def first_value(value: float) -> None
```

<a id="unreal.EarthSelectGrammarCriterion.second_value"></a>

#### second\_value

```python
@property
def second_value() -> float
```

(double):  [Read-Write] 【范围限制】附加阈值（仅Range类型比较时生效）
用于RangeExclusive时：基础阈值 < Value < 附加阈值
用于RangeInclusive时：基础阈值 <= Value <= 附加阈值

<a id="unreal.EarthSelectGrammarCriterion.second_value"></a>

#### second\_value

```python
@second_value.setter
def second_value(value: float) -> None
```

<a id="unreal.EarthSelectGrammarCriterion.result"></a>

#### result

```python
@property
def result() -> str
```

(str):  [Read-Write] 【匹配结果】满足条件时应用的符号名称

<a id="unreal.EarthSelectGrammarCriterion.result"></a>

#### result

```python
@result.setter
def result(value: str) -> None
```

<a id="unreal.EarthFacadeFragment"></a>