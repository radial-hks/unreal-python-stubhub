## EarthInstanceTransformsFragment Objects

```python
class EarthInstanceTransformsFragment(EarthPropertyFragment)
```

定义实例变换数组片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthInstancedStaticMeshFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``transforms`` (Array[Transform]):  [Read-Write] 实例变换数组
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthInstanceTransformsFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             transforms: Array[Transform] = []) -> None
```

<a id="unreal.EarthInstanceTransformsFragment.transforms"></a>

#### transforms

```python
@property
def transforms() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] 实例变换数组

<a id="unreal.EarthInstanceTransformsFragment.transforms"></a>

#### transforms

```python
@transforms.setter
def transforms(value: Array[Transform]) -> None
```

<a id="unreal.EarthInstancedStaticMeshFragment"></a>