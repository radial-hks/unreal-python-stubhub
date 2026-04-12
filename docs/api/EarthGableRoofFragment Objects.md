## EarthGableRoofFragment Objects

```python
class EarthGableRoofFragment(EarthHipRoofFragment)
```

定义山墙屋顶数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoofFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write] 坡顶坡度（角度），当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度
- ``color`` (LinearColor):  [Read-Write] 屋顶颜色
- ``even_ridge`` (bool):  [Read-Write] 屋脊线是否保持水平
- ``expand_offset`` (float):  [Read-Write] 坡顶厚度
- ``gable_material`` (EarthMaterialInfo):  [Read-Write] 山墙材质
- ``height`` (float):  [Read-Write] 坡顶高度，当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度
- ``height_max`` (float):  [Read-Write] 使用“坡顶坡度”参数控制坡度是，坡顶的最大高度
- ``over_hang`` (float):  [Read-Write] 挑檐长度
- ``ridge_spline_asset`` (EarthSubAssetInfo):  [Read-Write] 阳脊线（凸起）样条线子资产配置
- ``roof_material`` (EarthMaterialInfo):  [Read-Write] 屋顶材质
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``valley_ridge_spline_asset`` (EarthSubAssetInfo):  [Read-Write] 阴脊线（凹陷）样条线子资产配置

<a id="unreal.EarthGableRoofFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    validated: bool = False,
    valid: bool = False,
    color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000],
    over_hang: float = 0.000000,
    roof_material: EarthMaterialInfo = [
        "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000, [0, 0]
    ],
    height: float = 0.000000,
    angle: float = 0.000000,
    height_max: float = 0.000000,
    even_ridge: bool = False,
    expand_offset: float = 0.000000,
    ridge_spline_asset: EarthSubAssetInfo = [
        None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
    ],
    valley_ridge_spline_asset: EarthSubAssetInfo = [
        None,
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
    ],
    gable_material: EarthMaterialInfo = [
        "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000, [0, 0]
    ]
) -> None
```

<a id="unreal.EarthGableRoofFragment.gable_material"></a>

#### gable\_material

```python
@property
def gable_material() -> EarthMaterialInfo
```

(EarthMaterialInfo):  [Read-Write] 山墙材质

<a id="unreal.EarthGableRoofFragment.gable_material"></a>

#### gable\_material

```python
@gable_material.setter
def gable_material(value: EarthMaterialInfo) -> None
```

<a id="unreal.EarthFlatRoofPrefab"></a>