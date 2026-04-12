## EarthSeedFragment Objects

```python
class EarthSeedFragment(EarthExternalFragment)
```

定义随机种子数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``seed`` (int32):  [Read-Write] 随机种子
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthSeedFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             seed: int = 0) -> None
```

<a id="unreal.EarthSeedFragment.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write] 随机种子

<a id="unreal.EarthSeedFragment.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.EarthCustomPropertiesFragment"></a>