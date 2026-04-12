## EarthPrimitiveDataFragment Objects

```python
class EarthPrimitiveDataFragment(EarthPropertyFragment)
```

定义图元数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``primitive_data`` (Map[Name, float]):  [Read-Write] 图元数据
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthPrimitiveDataFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             primitive_data: Map[Name, float] = {}) -> None
```

<a id="unreal.EarthPrimitiveDataFragment.primitive_data"></a>

#### primitive\_data

```python
@property
def primitive_data() -> Map[Name, float]
```

(Map[Name, float]):  [Read-Write] 图元数据

<a id="unreal.EarthPrimitiveDataFragment.primitive_data"></a>

#### primitive\_data

```python
@primitive_data.setter
def primitive_data(value: Map[Name, float]) -> None
```

<a id="unreal.EarthMaterialFragment"></a>