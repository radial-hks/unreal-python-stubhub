## EarthGridLayoutSubAsset Objects

```python
class EarthGridLayoutSubAsset(EarthWeightedSubAssetInfo)
```

网格排布子资产信息

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthGridLayoutFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``max_count`` (int32):  [Read-Write] 最大可生成数量，0为不设上限
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息
- ``use_as_placeholder`` (bool):  [Read-Write] 是否作为占位符使用
- ``weight`` (float):  [Read-Write] 子资产权重

<a id="unreal.EarthGridLayoutSubAsset.__init__"></a>

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
             weight: float = 0.000000,
             use_as_placeholder: bool = False,
             max_count: int = 0) -> None
```

<a id="unreal.EarthGridLayoutSubAsset.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@property
def use_as_placeholder() -> bool
```

(bool):  [Read-Write] 是否作为占位符使用

<a id="unreal.EarthGridLayoutSubAsset.use_as_placeholder"></a>

#### use\_as\_placeholder

```python
@use_as_placeholder.setter
def use_as_placeholder(value: bool) -> None
```

<a id="unreal.EarthGridLayoutSubAsset.max_count"></a>

#### max\_count

```python
@property
def max_count() -> int
```

(int32):  [Read-Write] 最大可生成数量，0为不设上限

<a id="unreal.EarthGridLayoutSubAsset.max_count"></a>

#### max\_count

```python
@max_count.setter
def max_count(value: int) -> None
```

<a id="unreal.EarthGridLayoutFragment"></a>