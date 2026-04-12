## EarthFragment Objects

```python
class EarthFragment(StructBase)
```

所有轻量级数据片段的基类，不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthFragment.validated"></a>

#### validated

```python
@property
def validated() -> bool
```

(bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthFragment.validated"></a>

#### validated

```python
@validated.setter
def validated(value: bool) -> None
```

<a id="unreal.EarthFragment.valid"></a>

#### valid

```python
@property
def valid() -> bool
```

(bool):  [Read-Write] 数据片段是否有效

<a id="unreal.EarthFragment.valid"></a>

#### valid

```python
@valid.setter
def valid(value: bool) -> None
```

<a id="unreal.EarthOutputFragment"></a>