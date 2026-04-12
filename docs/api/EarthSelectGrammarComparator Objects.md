## EarthSelectGrammarComparator Objects

```python
class EarthSelectGrammarComparator(EnumBase)
```

形状语法匹配器的数值比较操作符类型
支持二元比较操作符和三元比较操作符

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthShapeGrammarSelector.h

<a id="unreal.EarthSelectGrammarComparator.SELECT"></a>

#### SELECT

33: 直接选择此语法规则，条件始终为真

<a id="unreal.EarthSelectGrammarComparator.LESS_THAN"></a>

#### LESS\_THAN

34: 当A小于B时选择(A < B)

<a id="unreal.EarthSelectGrammarComparator.LESS_THAN_EQUAL_TO"></a>

#### LESS\_THAN\_EQUAL\_TO

35: 当A小于等于B时选择(A <= B)

<a id="unreal.EarthSelectGrammarComparator.EQUAL_TO"></a>

#### EQUAL\_TO

36: 当A等于B时选择(A == B)

<a id="unreal.EarthSelectGrammarComparator.GREATER_THAN_EQUAL_TO"></a>

#### GREATER\_THAN\_EQUAL\_TO

37: 当A大于等于B时选择(A >= B)

<a id="unreal.EarthSelectGrammarComparator.GREATER_THAN"></a>

#### GREATER\_THAN

38: 当A大于B时选择(A > B)

<a id="unreal.EarthSelectGrammarComparator.RANGE_EXCLUSIVE"></a>

#### RANGE\_EXCLUSIVE

65: 当A在B和C之间的开区间时选择(B < A < C)

<a id="unreal.EarthSelectGrammarComparator.RANGE_INCLUSIVE"></a>

#### RANGE\_INCLUSIVE

66: 当A在B和C之间的闭区间时选择(B <= A <= C)

<a id="unreal.EarthTerrainPrecisionMode"></a>