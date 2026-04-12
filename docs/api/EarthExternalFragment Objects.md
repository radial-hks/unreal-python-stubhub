## EarthExternalFragment Objects

```python
class EarthExternalFragment(EarthFragment)
```

外部片段基类：定义驱动生成流程的控制指令或外部数据源标识
通常由外部系统（如GIS服务或生成子系统）注入，不建议预制体直接持有
必能覆盖子资产的同类型外部片段
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthExternalFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthSeedFragment"></a>