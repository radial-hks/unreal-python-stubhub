## EarthZoneShapeFragment Objects

```python
class EarthZoneShapeFragment(EarthPrimitiveFragment)
```

区域形状数据片段

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthSpatialFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area`` (double):  [Read-Write] 面积，单位为平方米
- ``bounds_rotation`` (Rotator):  [Read-Write] 最小面积包围盒的旋转值
- ``clockwise`` (bool):  [Read-Write] 是否是顺时针的点序
- ``closed_loop`` (bool):  [Read-Write] 是否为闭环
- ``earth_zone_shape`` (EarthZoneShapes):  [Read-Write] ZoneShape
- ``min_area_bounds`` (Box):  [Read-Write] 最小面积包围盒
- ``owned_component`` (ActorComponent):  [Read-Write] 空间片段所拥有的组件
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``vertices`` (Array[Vector]):  [Read-Write] 顶点数组

<a id="unreal.EarthZoneShapeFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        owned_component: ActorComponent = None,
        vertices: Array[Vector] = [],
        area: float = 0.000000,
        closed_loop: bool = False,
        clockwise: bool = False,
        min_area_bounds: Box = [[0.000000, 0.000000, 0.000000],
                                [0.000000, 0.000000, 0.000000], False],
        bounds_rotation: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EarthZoneShapes"></a>