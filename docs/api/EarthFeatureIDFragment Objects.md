## EarthFeatureIDFragment Objects

```python
class EarthFeatureIDFragment(EarthExternalFragment)
```

定义要素识别码片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_id`` (int64):  [Read-Write] 实体识别码
- ``feature_id`` (int64):  [Read-Write] 要素识别码
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFeatureIDFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             entity_id: int = 0,
             feature_id: int = 0) -> None
```

<a id="unreal.EarthFeatureIDFragment.entity_id"></a>

#### entity\_id

```python
@property
def entity_id() -> int
```

(int64):  [Read-Write] 实体识别码

<a id="unreal.EarthFeatureIDFragment.entity_id"></a>

#### entity\_id

```python
@entity_id.setter
def entity_id(value: int) -> None
```

<a id="unreal.EarthFeatureIDFragment.feature_id"></a>

#### feature\_id

```python
@property
def feature_id() -> int
```

(int64):  [Read-Write] 要素识别码

<a id="unreal.EarthFeatureIDFragment.feature_id"></a>

#### feature\_id

```python
@feature_id.setter
def feature_id(value: int) -> None
```

<a id="unreal.EarthOuterFragment"></a>