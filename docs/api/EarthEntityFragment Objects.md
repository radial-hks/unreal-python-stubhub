## EarthEntityFragment Objects

```python
class EarthEntityFragment(EarthFragment)
```

实体片段基类：定义预制体的核心属性，与GIS数据源的要素关联，如地形、建筑、道路等
由外部传入时，会覆盖预制体内的实体片段的属性值
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthEntityFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthBuildingFragment"></a>