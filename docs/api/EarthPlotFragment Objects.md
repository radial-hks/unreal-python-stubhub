## EarthPlotFragment Objects

```python
class EarthPlotFragment(EarthEntityFragment)
```

定义地块数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPlotFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``edge_assets`` (Array[EarthPlotEdgeSubAsset]):  [Read-Write] 包边资产列表，必须选择PrefabType为InstanceSpline的资产
- ``linear_mode`` (bool):  [Read-Write] 直线模式开关 - 开启时创建 Linear 类型的样条线，关闭时创建 Curve 类型
- ``outline_expand`` (float):  [Read-Write] 轮廓线外扩距离
- ``surface_asset`` (EarthPlotSurfaceSubAsset):  [Read-Write] 地块面资产，必须选择PrefabType为FlatRoofPrefab的资产
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthPlotFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             outline_expand: float = 0.000000,
             linear_mode: bool = False,
             surface_asset: EarthPlotSurfaceSubAsset = [
                 0.000000, 0.000000, False,
                 [
                     "None", None, 0, False, 255, [0.000000, 0.000000],
                     0.000000, [0, 0]
                 ], 10, None,
                 [[0.000000, 0.000000, 0.000000],
                  [-0.000000, 0.000000, 0.000000],
                  [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {},
                 True
             ],
             edge_assets: Array[EarthPlotEdgeSubAsset] = []) -> None
```

<a id="unreal.EarthPlotFragment.outline_expand"></a>

#### outline\_expand

```python
@property
def outline_expand() -> float
```

(float):  [Read-Write] 轮廓线外扩距离

<a id="unreal.EarthPlotFragment.outline_expand"></a>

#### outline\_expand

```python
@outline_expand.setter
def outline_expand(value: float) -> None
```

<a id="unreal.EarthPlotFragment.linear_mode"></a>

#### linear\_mode

```python
@property
def linear_mode() -> bool
```

(bool):  [Read-Write] 直线模式开关 - 开启时创建 Linear 类型的样条线，关闭时创建 Curve 类型

<a id="unreal.EarthPlotFragment.linear_mode"></a>

#### linear\_mode

```python
@linear_mode.setter
def linear_mode(value: bool) -> None
```

<a id="unreal.EarthPlotFragment.surface_asset"></a>

#### surface\_asset

```python
@property
def surface_asset() -> EarthPlotSurfaceSubAsset
```

(EarthPlotSurfaceSubAsset):  [Read-Write] 地块面资产，必须选择PrefabType为FlatRoofPrefab的资产

<a id="unreal.EarthPlotFragment.surface_asset"></a>

#### surface\_asset

```python
@surface_asset.setter
def surface_asset(value: EarthPlotSurfaceSubAsset) -> None
```

<a id="unreal.EarthPlotFragment.edge_assets"></a>

#### edge\_assets

```python
@property
def edge_assets() -> Array[EarthPlotEdgeSubAsset]
```

(Array[EarthPlotEdgeSubAsset]):  [Read-Write] 包边资产列表，必须选择PrefabType为InstanceSpline的资产

<a id="unreal.EarthPlotFragment.edge_assets"></a>

#### edge\_assets

```python
@edge_assets.setter
def edge_assets(value: Array[EarthPlotEdgeSubAsset]) -> None
```

<a id="unreal.EarthPlotPrefab"></a>