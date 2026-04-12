## EarthExtensionFragment Objects

```python
class EarthExtensionFragment(EarthFragment)
```

扩展片段基类：预留给第三方工具或自定义生成算法的扩展类型
不可直接使用

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthFragmentTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthExtensionFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False, valid: bool = False) -> None
```

<a id="unreal.EarthGridLayoutSubAsset"></a>