## EarthCustomPropertiesFragment Objects

```python
class EarthCustomPropertiesFragment(EarthPropertyFragment)
```

定义自定义属性数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``custom_properties`` (InstancedPropertyBag):  [Read-Write] 自定义属性
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthCustomPropertiesFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthTransformFragment"></a>