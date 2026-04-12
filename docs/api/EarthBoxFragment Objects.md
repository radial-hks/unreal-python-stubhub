## EarthBoxFragment Objects

```python
class EarthBoxFragment(EarthPointFragment)
```

长方体数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``box_size`` (Vector):  [Read-Write] 长方体尺寸
- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``transform`` (Transform):  [Read-Write] 点数据
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthBoxFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             owned_component: ActorComponent = None,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             box_size: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EarthBoxFragment.box_size"></a>

#### box\_size

```python
@property
def box_size() -> Vector
```

(Vector):  [Read-Write] 长方体尺寸

<a id="unreal.EarthBoxFragment.box_size"></a>

#### box\_size

```python
@box_size.setter
def box_size(value: Vector) -> None
```

<a id="unreal.EarthPrimitiveFragment"></a>