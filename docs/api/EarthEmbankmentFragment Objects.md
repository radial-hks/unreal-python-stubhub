## EarthEmbankmentFragment Objects

```python
class EarthEmbankmentFragment(EarthEntityFragment)
```

定义堤坝数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthEmbankmentFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chamfer_corner`` (bool):  [Read-Write] 启用节点倒角
- ``chamfer_length`` (float):  [Read-Write] 默认倒角长度
- ``chamfer_lengths`` (Array[float]):  [Read-Write] 节点倒角长度数组
- ``crest`` (EarthEmbankmentSubAssetInfo):  [Read-Write] 堤顶资产
- ``land_slope`` (EarthEmbankmentSubAssetInfo):  [Read-Write] 背水坡资产
- ``type`` (Name):  [Read-Write] 堤岸类型
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``water_side`` (EarthEmbankmentWaterSide):  [Read-Write] 迎水侧方向
- ``water_slope`` (EarthEmbankmentSubAssetInfo):  [Read-Write] 迎水坡资产

<a id="unreal.EarthEmbankmentFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        type: Name = "None",
        water_side: EarthEmbankmentWaterSide = EarthEmbankmentWaterSide.RIGHT,
        crest: EarthEmbankmentSubAssetInfo = [
            True, 200.000000, True, 300.000000, [0.000000, 0.000000], None,
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
        ],
        water_slope: EarthEmbankmentSubAssetInfo = [
            True, 200.000000, True, 300.000000, [0.000000, 0.000000], None,
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
        ],
        land_slope: EarthEmbankmentSubAssetInfo = [
            True, 200.000000, True, 300.000000, [0.000000, 0.000000], None,
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]], [0.000000, 0.000000], 0, {}, True
        ],
        chamfer_corner: bool = False,
        chamfer_length: float = 0.000000,
        chamfer_lengths: Array[float] = []) -> None
```

<a id="unreal.EarthEmbankmentFragment.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write] 堤岸类型

<a id="unreal.EarthEmbankmentFragment.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EarthEmbankmentFragment.water_side"></a>

#### water\_side

```python
@property
def water_side() -> EarthEmbankmentWaterSide
```

(EarthEmbankmentWaterSide):  [Read-Write] 迎水侧方向

<a id="unreal.EarthEmbankmentFragment.water_side"></a>

#### water\_side

```python
@water_side.setter
def water_side(value: EarthEmbankmentWaterSide) -> None
```

<a id="unreal.EarthEmbankmentFragment.crest"></a>

#### crest

```python
@property
def crest() -> EarthEmbankmentSubAssetInfo
```

(EarthEmbankmentSubAssetInfo):  [Read-Write] 堤顶资产

<a id="unreal.EarthEmbankmentFragment.crest"></a>

#### crest

```python
@crest.setter
def crest(value: EarthEmbankmentSubAssetInfo) -> None
```

<a id="unreal.EarthEmbankmentFragment.water_slope"></a>

#### water\_slope

```python
@property
def water_slope() -> EarthEmbankmentSubAssetInfo
```

(EarthEmbankmentSubAssetInfo):  [Read-Write] 迎水坡资产

<a id="unreal.EarthEmbankmentFragment.water_slope"></a>

#### water\_slope

```python
@water_slope.setter
def water_slope(value: EarthEmbankmentSubAssetInfo) -> None
```

<a id="unreal.EarthEmbankmentFragment.land_slope"></a>

#### land\_slope

```python
@property
def land_slope() -> EarthEmbankmentSubAssetInfo
```

(EarthEmbankmentSubAssetInfo):  [Read-Write] 背水坡资产

<a id="unreal.EarthEmbankmentFragment.land_slope"></a>

#### land\_slope

```python
@land_slope.setter
def land_slope(value: EarthEmbankmentSubAssetInfo) -> None
```

<a id="unreal.EarthEmbankmentFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 启用节点倒角

<a id="unreal.EarthEmbankmentFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.EarthEmbankmentFragment.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 默认倒角长度

<a id="unreal.EarthEmbankmentFragment.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.EarthEmbankmentFragment.chamfer_lengths"></a>

#### chamfer\_lengths

```python
@property
def chamfer_lengths() -> Array[float]
```

(Array[float]):  [Read-Write] 节点倒角长度数组

<a id="unreal.EarthEmbankmentFragment.chamfer_lengths"></a>

#### chamfer\_lengths

```python
@chamfer_lengths.setter
def chamfer_lengths(value: Array[float]) -> None
```

<a id="unreal.EarthEmbankmentPrefab"></a>