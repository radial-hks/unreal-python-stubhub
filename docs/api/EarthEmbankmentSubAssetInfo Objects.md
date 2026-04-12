## EarthEmbankmentSubAssetInfo Objects

```python
class EarthEmbankmentSubAssetInfo(EarthSubAssetInfo)
```

堤坝子资产配置结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthEmbankmentFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_scale`` (bool):  [Read-Write] 是否允许缩放子资产
- ``asset`` (EarthPrefabAsset):  [Read-Write] 子资产引用
- ``height_override`` (float):  [Read-Write] 高度值
- ``lod_config`` (Map[int32, int32]):  [Read-Write] 子资产细节级别设置，针对不同的最大细节级别X，需设置子资产在细节级别Y使用，若为空，则子资产在任意细节级别都使用
- ``offset_override`` (Vector2f):  [Read-Write] 偏移覆盖值
- ``seed`` (int32):  [Read-Write] 子资产随机种子偏移值
- ``size_extend`` (Vector2D):  [Read-Write] 子资产尺寸扩展值
- ``transform`` (Transform):  [Read-Write] 子资产的实例变换信息
- ``use_height_override`` (bool):  [Read-Write] 是否覆盖高度
- ``use_width_override`` (bool):  [Read-Write] 是否覆盖宽度
- ``width_override`` (float):  [Read-Write] 宽度值

<a id="unreal.EarthEmbankmentSubAssetInfo.__init__"></a>

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
             use_width_override: bool = False,
             width_override: float = 0.000000,
             use_height_override: bool = False,
             height_override: float = 0.000000,
             offset_override: Vector2f = [0.000000, 0.000000]) -> None
```

<a id="unreal.EarthEmbankmentSubAssetInfo.use_width_override"></a>

#### use\_width\_override

```python
@property
def use_width_override() -> bool
```

(bool):  [Read-Write] 是否覆盖宽度

<a id="unreal.EarthEmbankmentSubAssetInfo.use_width_override"></a>

#### use\_width\_override

```python
@use_width_override.setter
def use_width_override(value: bool) -> None
```

<a id="unreal.EarthEmbankmentSubAssetInfo.width_override"></a>

#### width\_override

```python
@property
def width_override() -> float
```

(float):  [Read-Write] 宽度值

<a id="unreal.EarthEmbankmentSubAssetInfo.width_override"></a>

#### width\_override

```python
@width_override.setter
def width_override(value: float) -> None
```

<a id="unreal.EarthEmbankmentSubAssetInfo.use_height_override"></a>

#### use\_height\_override

```python
@property
def use_height_override() -> bool
```

(bool):  [Read-Write] 是否覆盖高度

<a id="unreal.EarthEmbankmentSubAssetInfo.use_height_override"></a>

#### use\_height\_override

```python
@use_height_override.setter
def use_height_override(value: bool) -> None
```

<a id="unreal.EarthEmbankmentSubAssetInfo.height_override"></a>

#### height\_override

```python
@property
def height_override() -> float
```

(float):  [Read-Write] 高度值

<a id="unreal.EarthEmbankmentSubAssetInfo.height_override"></a>

#### height\_override

```python
@height_override.setter
def height_override(value: float) -> None
```

<a id="unreal.EarthEmbankmentSubAssetInfo.offset_override"></a>

#### offset\_override

```python
@property
def offset_override() -> Vector2f
```

(Vector2f):  [Read-Write] 偏移覆盖值

<a id="unreal.EarthEmbankmentSubAssetInfo.offset_override"></a>

#### offset\_override

```python
@offset_override.setter
def offset_override(value: Vector2f) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment"></a>