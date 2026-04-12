## EarthDerivedPrefabActorFragment Objects

```python
class EarthDerivedPrefabActorFragment(EarthExternalFragment)
```

定义调试用片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``derived_prefab_class`` (Array[ScriptStruct]):  [Read-Write] 要派生为预制体Actor的预制体类
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthDerivedPrefabActorFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             derived_prefab_class: Array[ScriptStruct] = []) -> None
```

<a id="unreal.EarthDerivedPrefabActorFragment.derived_prefab_class"></a>

#### derived\_prefab\_class

```python
@property
def derived_prefab_class() -> Array[ScriptStruct]
```

(Array[ScriptStruct]):  [Read-Write] 要派生为预制体Actor的预制体类

<a id="unreal.EarthDerivedPrefabActorFragment.derived_prefab_class"></a>

#### derived\_prefab\_class

```python
@derived_prefab_class.setter
def derived_prefab_class(value: Array[ScriptStruct]) -> None
```

<a id="unreal.EarthDuplicateCrossSectionsHelpers"></a>