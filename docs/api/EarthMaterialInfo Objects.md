## EarthMaterialInfo Objects

```python
class EarthMaterialInfo(StructBase)
```

定义材质信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthCommonFragments.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material`` (MaterialInterface):  [Read-Write] 材质资产引用
- ``max_texture_index`` (int32):  [Read-Write] 最大随机贴图索引值，仅当勾选"使用随机贴图索引值"时才有效
- ``random_texture_index`` (bool):  [Read-Write] 是否使用随机贴图索引值
- ``symbol`` (Name):  [Read-Write] 材质的符号表示，仅在形状语法时使用
- ``texture_index`` (int32):  [Read-Write] 材质所用贴图索引值
- ``unit_uv_size`` (Vector2f):  [Read-Write] 贴图的UV单位尺寸
- ``uv_rotation`` (float):  [Read-Write] UV贴图旋转角度
- ``uv_tile_precision`` (IntPoint):  [Read-Write] UV贴图平铺精度（控制贴图在UV方向的最小可重复单元）
  定义贴图被分割的最小单元数量：
  - 默认值{0,0}表示贴图可以随意重复
  - 值{1,1}表示必须完整贴图重复（1个完整单元）
  - 值{5,5}表示贴图被划分为5×5网格，可基于单个网格单元重复
  值越大表示允许的重复精度越高（对应更小的最小重复区域）

<a id="unreal.EarthMaterialInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(symbol: Name = "None",
             material: MaterialInterface = None,
             texture_index: int = 0,
             random_texture_index: bool = False,
             max_texture_index: int = 0,
             unit_uv_size: Vector2f = [0.000000, 0.000000],
             uv_rotation: float = 0.000000,
             uv_tile_precision: IntPoint = [0, 0]) -> None
```

<a id="unreal.EarthMaterialInfo.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] 材质的符号表示，仅在形状语法时使用

<a id="unreal.EarthMaterialInfo.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.EarthMaterialInfo.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write] 材质资产引用

<a id="unreal.EarthMaterialInfo.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.EarthMaterialInfo.texture_index"></a>

#### texture\_index

```python
@property
def texture_index() -> int
```

(int32):  [Read-Write] 材质所用贴图索引值

<a id="unreal.EarthMaterialInfo.texture_index"></a>

#### texture\_index

```python
@texture_index.setter
def texture_index(value: int) -> None
```

<a id="unreal.EarthMaterialInfo.random_texture_index"></a>

#### random\_texture\_index

```python
@property
def random_texture_index() -> bool
```

(bool):  [Read-Write] 是否使用随机贴图索引值

<a id="unreal.EarthMaterialInfo.random_texture_index"></a>

#### random\_texture\_index

```python
@random_texture_index.setter
def random_texture_index(value: bool) -> None
```

<a id="unreal.EarthMaterialInfo.max_texture_index"></a>

#### max\_texture\_index

```python
@property
def max_texture_index() -> int
```

(int32):  [Read-Write] 最大随机贴图索引值，仅当勾选"使用随机贴图索引值"时才有效

<a id="unreal.EarthMaterialInfo.max_texture_index"></a>

#### max\_texture\_index

```python
@max_texture_index.setter
def max_texture_index(value: int) -> None
```

<a id="unreal.EarthMaterialInfo.unit_uv_size"></a>

#### unit\_uv\_size

```python
@property
def unit_uv_size() -> Vector2f
```

(Vector2f):  [Read-Write] 贴图的UV单位尺寸

<a id="unreal.EarthMaterialInfo.unit_uv_size"></a>

#### unit\_uv\_size

```python
@unit_uv_size.setter
def unit_uv_size(value: Vector2f) -> None
```

<a id="unreal.EarthMaterialInfo.uv_rotation"></a>

#### uv\_rotation

```python
@property
def uv_rotation() -> float
```

(float):  [Read-Write] UV贴图旋转角度

<a id="unreal.EarthMaterialInfo.uv_rotation"></a>

#### uv\_rotation

```python
@uv_rotation.setter
def uv_rotation(value: float) -> None
```

<a id="unreal.EarthMaterialInfo.uv_tile_precision"></a>

#### uv\_tile\_precision

```python
@property
def uv_tile_precision() -> IntPoint
```

(IntPoint):  [Read-Write] UV贴图平铺精度（控制贴图在UV方向的最小可重复单元）
定义贴图被分割的最小单元数量：
- 默认值{0,0}表示贴图可以随意重复
- 值{1,1}表示必须完整贴图重复（1个完整单元）
- 值{5,5}表示贴图被划分为5×5网格，可基于单个网格单元重复
值越大表示允许的重复精度越高（对应更小的最小重复区域）

<a id="unreal.EarthMaterialInfo.uv_tile_precision"></a>

#### uv\_tile\_precision

```python
@uv_tile_precision.setter
def uv_tile_precision(value: IntPoint) -> None
```

<a id="unreal.EarthExternalFragment"></a>