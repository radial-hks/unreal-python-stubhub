## EarthComponentClassFragment Objects

```python
class EarthComponentClassFragment(EarthPropertyFragment)
```

定义组件类片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_class`` (SoftClassPath):  [Read-Write] 组件类引用
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthComponentClassFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             component_class: SoftClassPath = [""]) -> None
```

<a id="unreal.EarthComponentClassFragment.component_class"></a>

#### component\_class

```python
@property
def component_class() -> SoftClassPath
```

(SoftClassPath):  [Read-Write] 组件类引用

<a id="unreal.EarthComponentClassFragment.component_class"></a>

#### component\_class

```python
@component_class.setter
def component_class(value: SoftClassPath) -> None
```

<a id="unreal.EarthDebugFragment"></a>