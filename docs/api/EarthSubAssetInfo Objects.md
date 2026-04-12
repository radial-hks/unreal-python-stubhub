## EarthSubAssetInfo Objects

```python
class EarthSubAssetInfo(StructBase)
```

定义预制体子资产信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息

<a id="unreal.EarthSubAssetInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(asset: EarthPrefabAsset = None,
             transform: Transform = [[0.000000, 0.000000, 0.000000],
                                     [-0.000000, 0.000000, 0.000000],
                                     [1.000000, 1.000000, 1.000000]],
             size_extend: Vector2D = [0.000000, 0.000000],
             seed: int = 0,
             lod_config: Map[int, int] = {},
             allow_scale: bool = False) -> None
```

<a id="unreal.EarthSubAssetInfo.asset"></a>

#### asset

```python
@property
def asset() -> EarthPrefabAsset
```

(EarthPrefabAsset):  [Read-Write] 子资产引用

<a id="unreal.EarthSubAssetInfo.asset"></a>

#### asset

```python
@asset.setter
def asset(value: EarthPrefabAsset) -> None
```

<a id="unreal.EarthSubAssetInfo.transform"></a>

#### transform

```python
@property
def transform() -> Transform
```

(Transform):  [Read-Write] 子资产的实例变换信息

<a id="unreal.EarthSubAssetInfo.transform"></a>

#### transform

```python
@transform.setter
def transform(value: Transform) -> None
```

<a id="unreal.EarthSubAssetInfo.size_extend"></a>

#### size\_extend

```python
@property
def size_extend() -> Vector2D
```

(Vector2D):  [Read-Write] 子资产尺寸扩展值

<a id="unreal.EarthSubAssetInfo.size_extend"></a>

#### size\_extend

```python
@size_extend.setter
def size_extend(value: Vector2D) -> None
```

<a id="unreal.EarthSubAssetInfo.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write] 子资产随机种子偏移值

<a id="unreal.EarthSubAssetInfo.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.EarthSubAssetInfo.lod_config"></a>

#### lod\_config

```python
@property
def lod_config() -> Map[int, int]
```

(Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用

<a id="unreal.EarthSubAssetInfo.lod_config"></a>

#### lod\_config

```python
@lod_config.setter
def lod_config(value: Map[int, int]) -> None
```

<a id="unreal.EarthSubAssetInfo.allow_scale"></a>

#### allow\_scale

```python
@property
def allow_scale() -> bool
```

(bool):  [Read-Write] 是否允许缩放子资产

<a id="unreal.EarthSubAssetInfo.allow_scale"></a>

#### allow\_scale

```python
@allow_scale.setter
def allow_scale(value: bool) -> None
```

<a id="unreal.EarthBuildingSubAsset"></a>