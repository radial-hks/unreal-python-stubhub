## EarthHipRoofFragment Objects

```python
class EarthHipRoofFragment(EarthRoofBaseFragment)
```

定义坡顶屋顶数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthRoofFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``angle`` (float):  [Read-Write] 坡顶坡度（角度），当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度
- ``color`` (LinearColor):  [Read-Write] 屋顶颜色
- ``even_ridge`` (bool):  [Read-Write] 屋脊线是否保持水平
- ``expand_offset`` (float):  [Read-Write] 坡顶厚度
- ``height`` (float):  [Read-Write] 坡顶高度，当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度
- ``height_max`` (float):  [Read-Write] 使用“坡顶坡度”参数控制坡度是，坡顶的最大高度
- ``over_hang`` (float):  [Read-Write] 挑檐长度
- ``ridge_spline_asset`` (EarthSubAssetInfo):  [Read-Write] 阳脊线（凸起）样条线子资产配置
- ``roof_material`` (EarthMaterialInfo):  [Read-Write] 屋顶材质
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``valley_ridge_spline_asset`` (EarthSubAssetInfo):  [Read-Write] 阴脊线（凹陷）样条线子资产配置

<a id="unreal.EarthHipRoofFragment.__init__"></a>

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
    ]
) -> None
```

<a id="unreal.EarthHipRoofFragment.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write] 坡顶高度，当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度

<a id="unreal.EarthHipRoofFragment.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.EarthHipRoofFragment.angle"></a>

#### angle

```python
@property
def angle() -> float
```

(float):  [Read-Write] 坡顶坡度（角度），当坡顶高度为0时，则采样“坡顶坡度”参数控制坡度

<a id="unreal.EarthHipRoofFragment.angle"></a>

#### angle

```python
@angle.setter
def angle(value: float) -> None
```

<a id="unreal.EarthHipRoofFragment.height_max"></a>

#### height\_max

```python
@property
def height_max() -> float
```

(float):  [Read-Write] 使用“坡顶坡度”参数控制坡度是，坡顶的最大高度

<a id="unreal.EarthHipRoofFragment.height_max"></a>

#### height\_max

```python
@height_max.setter
def height_max(value: float) -> None
```

<a id="unreal.EarthHipRoofFragment.even_ridge"></a>

#### even\_ridge

```python
@property
def even_ridge() -> bool
```

(bool):  [Read-Write] 屋脊线是否保持水平

<a id="unreal.EarthHipRoofFragment.even_ridge"></a>

#### even\_ridge

```python
@even_ridge.setter
def even_ridge(value: bool) -> None
```

<a id="unreal.EarthHipRoofFragment.expand_offset"></a>

#### expand\_offset

```python
@property
def expand_offset() -> float
```

(float):  [Read-Write] 坡顶厚度

<a id="unreal.EarthHipRoofFragment.expand_offset"></a>

#### expand\_offset

```python
@expand_offset.setter
def expand_offset(value: float) -> None
```

<a id="unreal.EarthHipRoofFragment.ridge_spline_asset"></a>

#### ridge\_spline\_asset

```python
@property
def ridge_spline_asset() -> EarthSubAssetInfo
```

(EarthSubAssetInfo):  [Read-Write] 阳脊线（凸起）样条线子资产配置

<a id="unreal.EarthHipRoofFragment.ridge_spline_asset"></a>

#### ridge\_spline\_asset

```python
@ridge_spline_asset.setter
def ridge_spline_asset(value: EarthSubAssetInfo) -> None
```

<a id="unreal.EarthHipRoofFragment.valley_ridge_spline_asset"></a>

#### valley\_ridge\_spline\_asset

```python
@property
def valley_ridge_spline_asset() -> EarthSubAssetInfo
```

(EarthSubAssetInfo):  [Read-Write] 阴脊线（凹陷）样条线子资产配置

<a id="unreal.EarthHipRoofFragment.valley_ridge_spline_asset"></a>

#### valley\_ridge\_spline\_asset

```python
@valley_ridge_spline_asset.setter
def valley_ridge_spline_asset(value: EarthSubAssetInfo) -> None
```

<a id="unreal.EarthGableRoofFragment"></a>