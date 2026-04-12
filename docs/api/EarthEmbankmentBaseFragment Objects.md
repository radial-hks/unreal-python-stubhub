## EarthEmbankmentBaseFragment Objects

```python
class EarthEmbankmentBaseFragment(EarthEntityFragment)
```

定义堤坝基础数据片段结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthEmbankmentFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chamfer_corner`` (bool):  [Read-Write] 启用节点倒角
- ``chamfer_length`` (float):  [Read-Write] 默认倒角长度
- ``chamfer_lengths`` (Array[float]):  [Read-Write] 节点倒角长度数组
- ``crest_height`` (float):  [Read-Write] 堤顶高度
- ``crest_offset_z`` (float):  [Read-Write] 堤顶偏移Z
- ``crest_width`` (float):  [Read-Write] 堤顶宽度
- ``land_slope_height`` (float):  [Read-Write] 背水坡高度
- ``land_slope_offset_z`` (float):  [Read-Write] 背水坡偏移Z
- ``land_slope_width`` (float):  [Read-Write] 背水坡宽度
- ``prefab_asset_id`` (str):  [Read-Write] 预制体资产ID
- ``type`` (Name):  [Read-Write] 堤岸类型
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证
- ``water_side`` (EarthEmbankmentWaterSide):  [Read-Write] 迎水侧方向
- ``water_slope_height`` (float):  [Read-Write] 迎水坡高度
- ``water_slope_offset_z`` (float):  [Read-Write] 迎水坡偏移Z
- ``water_slope_width`` (float):  [Read-Write] 迎水坡宽度

<a id="unreal.EarthEmbankmentBaseFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        validated: bool = False,
        valid: bool = False,
        type: Name = "None",
        water_side: EarthEmbankmentWaterSide = EarthEmbankmentWaterSide.RIGHT,
        crest_width: float = 0.000000,
        crest_height: float = 0.000000,
        crest_offset_z: float = 0.000000,
        water_slope_width: float = 0.000000,
        water_slope_height: float = 0.000000,
        water_slope_offset_z: float = 0.000000,
        land_slope_width: float = 0.000000,
        land_slope_height: float = 0.000000,
        land_slope_offset_z: float = 0.000000,
        prefab_asset_id: str = "",
        chamfer_corner: bool = False,
        chamfer_length: float = 0.000000,
        chamfer_lengths: Array[float] = []) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write] 堤岸类型

<a id="unreal.EarthEmbankmentBaseFragment.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.water_side"></a>

#### water\_side

```python
@property
def water_side() -> EarthEmbankmentWaterSide
```

(EarthEmbankmentWaterSide):  [Read-Write] 迎水侧方向

<a id="unreal.EarthEmbankmentBaseFragment.water_side"></a>

#### water\_side

```python
@water_side.setter
def water_side(value: EarthEmbankmentWaterSide) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.crest_width"></a>

#### crest\_width

```python
@property
def crest_width() -> float
```

(float):  [Read-Write] 堤顶宽度

<a id="unreal.EarthEmbankmentBaseFragment.crest_width"></a>

#### crest\_width

```python
@crest_width.setter
def crest_width(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.crest_height"></a>

#### crest\_height

```python
@property
def crest_height() -> float
```

(float):  [Read-Write] 堤顶高度

<a id="unreal.EarthEmbankmentBaseFragment.crest_height"></a>

#### crest\_height

```python
@crest_height.setter
def crest_height(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.crest_offset_z"></a>

#### crest\_offset\_z

```python
@property
def crest_offset_z() -> float
```

(float):  [Read-Write] 堤顶偏移Z

<a id="unreal.EarthEmbankmentBaseFragment.crest_offset_z"></a>

#### crest\_offset\_z

```python
@crest_offset_z.setter
def crest_offset_z(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_width"></a>

#### water\_slope\_width

```python
@property
def water_slope_width() -> float
```

(float):  [Read-Write] 迎水坡宽度

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_width"></a>

#### water\_slope\_width

```python
@water_slope_width.setter
def water_slope_width(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_height"></a>

#### water\_slope\_height

```python
@property
def water_slope_height() -> float
```

(float):  [Read-Write] 迎水坡高度

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_height"></a>

#### water\_slope\_height

```python
@water_slope_height.setter
def water_slope_height(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_offset_z"></a>

#### water\_slope\_offset\_z

```python
@property
def water_slope_offset_z() -> float
```

(float):  [Read-Write] 迎水坡偏移Z

<a id="unreal.EarthEmbankmentBaseFragment.water_slope_offset_z"></a>

#### water\_slope\_offset\_z

```python
@water_slope_offset_z.setter
def water_slope_offset_z(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_width"></a>

#### land\_slope\_width

```python
@property
def land_slope_width() -> float
```

(float):  [Read-Write] 背水坡宽度

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_width"></a>

#### land\_slope\_width

```python
@land_slope_width.setter
def land_slope_width(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_height"></a>

#### land\_slope\_height

```python
@property
def land_slope_height() -> float
```

(float):  [Read-Write] 背水坡高度

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_height"></a>

#### land\_slope\_height

```python
@land_slope_height.setter
def land_slope_height(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_offset_z"></a>

#### land\_slope\_offset\_z

```python
@property
def land_slope_offset_z() -> float
```

(float):  [Read-Write] 背水坡偏移Z

<a id="unreal.EarthEmbankmentBaseFragment.land_slope_offset_z"></a>

#### land\_slope\_offset\_z

```python
@land_slope_offset_z.setter
def land_slope_offset_z(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.prefab_asset_id"></a>

#### prefab\_asset\_id

```python
@property
def prefab_asset_id() -> str
```

(str):  [Read-Write] 预制体资产ID

<a id="unreal.EarthEmbankmentBaseFragment.prefab_asset_id"></a>

#### prefab\_asset\_id

```python
@prefab_asset_id.setter
def prefab_asset_id(value: str) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@property
def chamfer_corner() -> bool
```

(bool):  [Read-Write] 启用节点倒角

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_corner"></a>

#### chamfer\_corner

```python
@chamfer_corner.setter
def chamfer_corner(value: bool) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_length"></a>

#### chamfer\_length

```python
@property
def chamfer_length() -> float
```

(float):  [Read-Write] 默认倒角长度

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_length"></a>

#### chamfer\_length

```python
@chamfer_length.setter
def chamfer_length(value: float) -> None
```

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_lengths"></a>

#### chamfer\_lengths

```python
@property
def chamfer_lengths() -> Array[float]
```

(Array[float]):  [Read-Write] 节点倒角长度数组

<a id="unreal.EarthEmbankmentBaseFragment.chamfer_lengths"></a>

#### chamfer\_lengths

```python
@chamfer_lengths.setter
def chamfer_lengths(value: Array[float]) -> None
```

<a id="unreal.EarthEmbankmentFragment"></a>