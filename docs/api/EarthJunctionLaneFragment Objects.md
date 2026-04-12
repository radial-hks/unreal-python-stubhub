## EarthJunctionLaneFragment Objects

```python
class EarthJunctionLaneFragment(EarthPropertyFragment)
```

Earth Junction Lane Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``junction_module_definition`` (Map[Name, EarthRoadSubAssetInfo]):  [Read-Write] 键为路口模块的唯一名称，值为模块信息
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthJunctionLaneFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        junction_module_definition: Map[Name,
                                        EarthRoadSubAssetInfo] = {}) -> None
```

<a id="unreal.EarthJunctionLaneFragment.junction_module_definition"></a>

#### junction\_module\_definition

```python
@property
def junction_module_definition() -> Map[Name, EarthRoadSubAssetInfo]
```

(Map[Name, EarthRoadSubAssetInfo]):  [Read-Write] 键为路口模块的唯一名称，值为模块信息

<a id="unreal.EarthJunctionLaneFragment.junction_module_definition"></a>

#### junction\_module\_definition

```python
@junction_module_definition.setter
def junction_module_definition(
        value: Map[Name, EarthRoadSubAssetInfo]) -> None
```

<a id="unreal.EarthJunctionConnectionInfo"></a>