## EarthPointFragment Objects

```python
class EarthPointFragment(EarthSpatialFragment)
```

点数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``transform`` (Transform):  [Read-Write] 点数据
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthPointFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    owned_component: ActorComponent = None,
    transform: Transform = [[0.000000, 0.000000, 0.000000],
                            [-0.000000, 0.000000, 0.000000],
                            [1.000000, 1.000000, 1.000000]]
) -> None
```

<a id="unreal.EarthPointFragment.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 点数据

<a id="unreal.EarthPointFragment.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthBoxFragment"></a>