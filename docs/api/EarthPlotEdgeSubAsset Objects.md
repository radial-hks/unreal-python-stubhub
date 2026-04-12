## EarthPlotEdgeSubAsset Objects

```python
class EarthPlotEdgeSubAsset(EarthSubAssetInfo)
```

定义地块包边子资产信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthPlotFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``edge_depth`` (float):  [Read-Write] 地块包边的深度
- ``edge_height`` (float):  [Read-Write] 地块包边的高度
- ``edge_width`` (float):  [Read-Write] 地块包边的宽度
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息

<a id="unreal.EarthPlotEdgeSubAsset.__init__"></a>

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
             edge_width: float = 0.000000,
             edge_height: float = 0.000000,
             edge_depth: float = 0.000000) -> None
```

<a id="unreal.EarthPlotEdgeSubAsset.edge_width"></a>

#### edge\_width

```python
@property
def edge_width() -> float
```

(float):  [Read-Write] 地块包边的宽度

<a id="unreal.EarthPlotEdgeSubAsset.edge_width"></a>

#### edge\_width

```python
@edge_width.setter
def edge_width(value: float) -> None
```

<a id="unreal.EarthPlotEdgeSubAsset.edge_height"></a>

#### edge\_height

```python
@property
def edge_height() -> float
```

(float):  [Read-Write] 地块包边的高度

<a id="unreal.EarthPlotEdgeSubAsset.edge_height"></a>

#### edge\_height

```python
@edge_height.setter
def edge_height(value: float) -> None
```

<a id="unreal.EarthPlotEdgeSubAsset.edge_depth"></a>

#### edge\_depth

```python
@property
def edge_depth() -> float
```

(float):  [Read-Write] 地块包边的深度

<a id="unreal.EarthPlotEdgeSubAsset.edge_depth"></a>

#### edge\_depth

```python
@edge_depth.setter
def edge_depth(value: float) -> None
```

<a id="unreal.EarthPlotFragment"></a>