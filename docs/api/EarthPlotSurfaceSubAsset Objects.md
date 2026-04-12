## EarthPlotSurfaceSubAsset Objects

```python
class EarthPlotSurfaceSubAsset(EarthSubAssetInfo)
```

定义地块面子资产信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPlotFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``curve_subdivision_count`` (int32):  [Read-Write] 曲线细分段数
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``override_material`` (bool):  [Read-Write] 是否覆盖地块面材质
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``surface_expand`` (float):  [Read-Write] 地块面扩展距离
- ``surface_height`` (float):  [Read-Write] 地块面高度
- ``surface_material`` (EarthMaterialInfo):  [Read-Write] 地块面材质
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息

<a id="unreal.EarthPlotSurfaceSubAsset.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset: EarthPrefabAsset = None,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             size_extend: Vector2D = [0.000000, 0.000000],
             seed: int = 0,
             lod_config: Map[int, int] = {},
             allow_scale: bool = False,
             surface_expand: float = 0.000000,
             surface_height: float = 0.000000,
             override_material: bool = False,
             surface_material: EarthMaterialInfo = [
                 "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000,
                 [0, 0]
             ],
             curve_subdivision_count: int = 0) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset.surface_expand"></a>

#### surface\_expand

```python
@property
def surface_expand() -> float
```

(float):  [Read-Write] 地块面扩展距离

<a id="unreal.EarthPlotSurfaceSubAsset.surface_expand"></a>

#### surface\_expand

```python
@surface_expand.setter
def surface_expand(value: float) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset.surface_height"></a>

#### surface\_height

```python
@property
def surface_height() -> float
```

(float):  [Read-Write] 地块面高度

<a id="unreal.EarthPlotSurfaceSubAsset.surface_height"></a>

#### surface\_height

```python
@surface_height.setter
def surface_height(value: float) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset.override_material"></a>

#### override\_material

```python
@property
def override_material() -> bool
```

(bool):  [Read-Write] 是否覆盖地块面材质

<a id="unreal.EarthPlotSurfaceSubAsset.override_material"></a>

#### override\_material

```python
@override_material.setter
def override_material(value: bool) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset.surface_material"></a>

#### surface\_material

```python
@property
def surface_material() -> EarthMaterialInfo
```

(EarthMaterialInfo):  [Read-Write] 地块面材质

<a id="unreal.EarthPlotSurfaceSubAsset.surface_material"></a>

#### surface\_material

```python
@surface_material.setter
def surface_material(value: EarthMaterialInfo) -> None
```

<a id="unreal.EarthPlotSurfaceSubAsset.curve_subdivision_count"></a>

#### curve\_subdivision\_count

```python
@property
def curve_subdivision_count() -> int
```

(int32):  [Read-Write] 曲线细分段数

<a id="unreal.EarthPlotSurfaceSubAsset.curve_subdivision_count"></a>

#### curve\_subdivision\_count

```python
@curve_subdivision_count.setter
def curve_subdivision_count(value: int) -> None
```

<a id="unreal.EarthPlotEdgeSubAsset"></a>