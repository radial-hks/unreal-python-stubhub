## EarthOutputMergeConfigFragment Objects

```python
class EarthOutputMergeConfigFragment(EarthExternalFragment)
```

定义输出片段合并行为配置片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthOutputTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_instance_count`` (int32):  [Read-Write] 单个 ISM Fragment 允许合并的最大实例数上限
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthOutputMergeConfigFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             max_instance_count: int = 0) -> None
```

<a id="unreal.EarthOutputMergeConfigFragment.max_instance_count"></a>

#### max\_instance\_count

```python
@property
def max_instance_count() -> int
```

(int32):  [Read-Write] 单个 ISM Fragment 允许合并的最大实例数上限

<a id="unreal.EarthOutputMergeConfigFragment.max_instance_count"></a>

#### max\_instance\_count

```python
@max_instance_count.setter
def max_instance_count(value: int) -> None
```

<a id="unreal.EarthOutputFragments"></a>