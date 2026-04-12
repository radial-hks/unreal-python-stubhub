## EarthTerraformingSplineFragment Objects

```python
class EarthTerraformingSplineFragment(EarthEntityFragment)
```

定义基于样条线的地形改造数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthTerraformingFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (float):  [Read-Write] 地形改造深度
- ``edge_offset_z`` (float):  [Read-Write] 边缘在Z轴上的偏移值
- ``edge_width`` (float):  [Read-Write] 地形改造边缘宽度
- ``edge_widths`` (Array[float]):  [Read-Write] 逐点位裙边宽度数组
- ``mask_width`` (float):  [Read-Write] 地形改造蒙版宽度
- ``min_width`` (float):  [Read-Write] 最小宽度限制（防止退化几何）
- ``offset_z`` (float):  [Read-Write] 轮廓线点位在Z轴上的偏移值
- ``spline_width`` (float):  [Read-Write] 地形改造样条线默认宽度
- ``surface_widths`` (Array[float]):  [Read-Write] 逐点位表面宽度数组（对应样条线每个点）
- ``use_uniform_width`` (bool):  [Read-Write] 是否使用统一宽度（忽略逐点位数组）
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthTerraformingSplineFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             spline_width: float = 0.000000,
             offset_z: float = 0.000000,
             edge_width: float = 0.000000,
             edge_offset_z: float = 0.000000,
             mask_width: float = 0.000000,
             depth: float = 0.000000,
             surface_widths: Array[float] = [],
             edge_widths: Array[float] = [],
             use_uniform_width: bool = False,
             min_width: float = 0.000000) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.spline_width"></a>

#### spline\_width

```python
@property
def spline_width() -> float
```

(float):  [Read-Write] 地形改造样条线默认宽度

<a id="unreal.EarthTerraformingSplineFragment.spline_width"></a>

#### spline\_width

```python
@spline_width.setter
def spline_width(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.offset_z"></a>

#### offset\_z

```python
@property
def offset_z() -> float
```

(float):  [Read-Write] 轮廓线点位在Z轴上的偏移值

<a id="unreal.EarthTerraformingSplineFragment.offset_z"></a>

#### offset\_z

```python
@offset_z.setter
def offset_z(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.edge_width"></a>

#### edge\_width

```python
@property
def edge_width() -> float
```

(float):  [Read-Write] 地形改造边缘宽度

<a id="unreal.EarthTerraformingSplineFragment.edge_width"></a>

#### edge\_width

```python
@edge_width.setter
def edge_width(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.edge_offset_z"></a>

#### edge\_offset\_z

```python
@property
def edge_offset_z() -> float
```

(float):  [Read-Write] 边缘在Z轴上的偏移值

<a id="unreal.EarthTerraformingSplineFragment.edge_offset_z"></a>

#### edge\_offset\_z

```python
@edge_offset_z.setter
def edge_offset_z(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.mask_width"></a>

#### mask\_width

```python
@property
def mask_width() -> float
```

(float):  [Read-Write] 地形改造蒙版宽度

<a id="unreal.EarthTerraformingSplineFragment.mask_width"></a>

#### mask\_width

```python
@mask_width.setter
def mask_width(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write] 地形改造深度

<a id="unreal.EarthTerraformingSplineFragment.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.surface_widths"></a>

#### surface\_widths

```python
@property
def surface_widths() -> Array[float]
```

(Array[float]):  [Read-Write] 逐点位表面宽度数组（对应样条线每个点）

<a id="unreal.EarthTerraformingSplineFragment.surface_widths"></a>

#### surface\_widths

```python
@surface_widths.setter
def surface_widths(value: Array[float]) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.edge_widths"></a>

#### edge\_widths

```python
@property
def edge_widths() -> Array[float]
```

(Array[float]):  [Read-Write] 逐点位裙边宽度数组

<a id="unreal.EarthTerraformingSplineFragment.edge_widths"></a>

#### edge\_widths

```python
@edge_widths.setter
def edge_widths(value: Array[float]) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.use_uniform_width"></a>

#### use\_uniform\_width

```python
@property
def use_uniform_width() -> bool
```

(bool):  [Read-Write] 是否使用统一宽度（忽略逐点位数组）

<a id="unreal.EarthTerraformingSplineFragment.use_uniform_width"></a>

#### use\_uniform\_width

```python
@use_uniform_width.setter
def use_uniform_width(value: bool) -> None
```

<a id="unreal.EarthTerraformingSplineFragment.min_width"></a>

#### min\_width

```python
@property
def min_width() -> float
```

(float):  [Read-Write] 最小宽度限制（防止退化几何）

<a id="unreal.EarthTerraformingSplineFragment.min_width"></a>

#### min\_width

```python
@min_width.setter
def min_width(value: float) -> None
```

<a id="unreal.EarthTerraformingMeshGenerator"></a>