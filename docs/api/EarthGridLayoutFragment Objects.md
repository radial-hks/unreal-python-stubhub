## EarthGridLayoutFragment Objects

```python
class EarthGridLayoutFragment(EarthEntityFragment)
```

定义网格排布资产数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthGridLayoutFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``area_range`` (Vector2f):  [Read-Write] 资产可散布的面积区间，单位为平方米
- ``grid_assets`` (Array[EarthGridLayoutSubAsset]):  [Read-Write] 参与排布的资产信息列表
- ``max_layout_depth`` (int32):  [Read-Write] 网格排布最大细分深度
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthGridLayoutFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             max_layout_depth: int = 0,
             area_range: Vector2f = [0.000000, 0.000000],
             grid_assets: Array[EarthGridLayoutSubAsset] = []) -> None
```

<a id="unreal.EarthGridLayoutFragment.max_layout_depth"></a>

#### max\_layout\_depth

```python
@property
def max_layout_depth() -> int
```

(int32):  [Read-Write] 网格排布最大细分深度

<a id="unreal.EarthGridLayoutFragment.max_layout_depth"></a>

#### max\_layout\_depth

```python
@max_layout_depth.setter
def max_layout_depth(value: int) -> None
```

<a id="unreal.EarthGridLayoutFragment.area_range"></a>

#### area\_range

```python
@property
def area_range() -> Vector2f
```

(Vector2f):  [Read-Write] 资产可散布的面积区间，单位为平方米

<a id="unreal.EarthGridLayoutFragment.area_range"></a>

#### area\_range

```python
@area_range.setter
def area_range(value: Vector2f) -> None
```

<a id="unreal.EarthGridLayoutFragment.grid_assets"></a>

#### grid\_assets

```python
@property
def grid_assets() -> Array[EarthGridLayoutSubAsset]
```

(Array[EarthGridLayoutSubAsset]):  [Read-Write] 参与排布的资产信息列表

<a id="unreal.EarthGridLayoutFragment.grid_assets"></a>

#### grid\_assets

```python
@grid_assets.setter
def grid_assets(value: Array[EarthGridLayoutSubAsset]) -> None
```

<a id="unreal.EarthGridLayoutPrefab"></a>