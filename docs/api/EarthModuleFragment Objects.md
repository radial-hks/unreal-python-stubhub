## EarthModuleFragment Objects

```python
class EarthModuleFragment(EarthPropertyFragment)
```

Earth Module Fragment

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoadFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``module_definition`` (EarthSubAssetInfo):  [Read-Write] 键为模块的唯一名称，值为模块信息
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthModuleFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    module_definition: EarthSubAssetInfo = [
        None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
    ]
) -> None
```

<a id="unreal.EarthModuleFragment.module_definition"></a>

#### module\_definition

```python
@property
def module_definition() -> EarthSubAssetInfo
```

(EarthSubAssetInfo):  [Read-Write] 键为模块的唯一名称，值为模块信息

<a id="unreal.EarthModuleFragment.module_definition"></a>

#### module\_definition

```python
@module_definition.setter
def module_definition(value: EarthSubAssetInfo) -> None
```

<a id="unreal.EarthLaneInfo"></a>