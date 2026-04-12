## EarthPropertyFragment Objects

```python
class EarthPropertyFragment(EarthFragment)
```

属性片段基类：定义可传递给子资产或生成物的次要属性
预制体和外部皆可用
默认允许覆盖子资产的同类型片段
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthPropertyFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthBuildingSubAssetsFragment"></a>