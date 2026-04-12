## AesFacadeMaterialInfo Objects

```python
class AesFacadeMaterialInfo(StructBase)
```

立面材质信息的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesFacadeAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material`` (SoftObjectPath):  [Read-Write] 材质资产引用
- ``max_texture_index`` (int32):  [Read-Write] 最大随机贴图索引值
- ``random_texture_index`` (bool):  [Read-Write] 是否使用随机贴图索引值
- ``texture_index`` (int32):  [Read-Write] 材质所用贴图索引值
- ``unit_uv_size`` (Vector2f):  [Read-Write] 贴图的UV单位尺寸
- ``uv_tile_precision`` (IntPoint):  [Read-Write] UV贴图平铺精度（控制贴图在UV方向的最小可重复单元）
  定义贴图被分割的最小单元数量：
  - 默认值{1,1}表示必须完整贴图重复（1个完整单元）
  - 值{5,5}表示贴图被划分为5×5网格，可基于单个网格单元重复
  - 值{0,0}表示贴图可以随意重复
  值越大表示允许的重复精度越高（对应更小的最小重复区域）

<a id="unreal.AesFacadeMaterialInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(material: SoftObjectPath = [""],
             texture_index: int = 0,
             random_texture_index: bool = False,
             max_texture_index: int = 0,
             unit_uv_size: Vector2f = [0.000000, 0.000000],
             uv_tile_precision: IntPoint = [0, 0]) -> None
```

<a id="unreal.AesFacadeMaterialInfo.material"></a>

#### material

```python
@property
def material() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write] 材质资产引用

<a id="unreal.AesFacadeMaterialInfo.material"></a>

#### material

```python
@material.setter
def material(value: SoftObjectPath) -> None
```

<a id="unreal.AesFacadeMaterialInfo.texture_index"></a>

#### texture\_index

```python
@property
def texture_index() -> int
```

(int32):  [Read-Write] 材质所用贴图索引值

<a id="unreal.AesFacadeMaterialInfo.texture_index"></a>

#### texture\_index

```python
@texture_index.setter
def texture_index(value: int) -> None
```

<a id="unreal.AesFacadeMaterialInfo.random_texture_index"></a>

#### random\_texture\_index

```python
@property
def random_texture_index() -> bool
```

(bool):  [Read-Write] 是否使用随机贴图索引值

<a id="unreal.AesFacadeMaterialInfo.random_texture_index"></a>

#### random\_texture\_index

```python
@random_texture_index.setter
def random_texture_index(value: bool) -> None
```

<a id="unreal.AesFacadeMaterialInfo.max_texture_index"></a>

#### max\_texture\_index

```python
@property
def max_texture_index() -> int
```

(int32):  [Read-Write] 最大随机贴图索引值

<a id="unreal.AesFacadeMaterialInfo.max_texture_index"></a>

#### max\_texture\_index

```python
@max_texture_index.setter
def max_texture_index(value: int) -> None
```

<a id="unreal.AesFacadeMaterialInfo.unit_uv_size"></a>

#### unit\_uv\_size

```python
@property
def unit_uv_size() -> Vector2f
```

(Vector2f):  [Read-Write] 贴图的UV单位尺寸

<a id="unreal.AesFacadeMaterialInfo.unit_uv_size"></a>

#### unit\_uv\_size

```python
@unit_uv_size.setter
def unit_uv_size(value: Vector2f) -> None
```

<a id="unreal.AesFacadeMaterialInfo.uv_tile_precision"></a>

#### uv\_tile\_precision

```python
@property
def uv_tile_precision() -> IntPoint
```

(IntPoint):  [Read-Write] UV贴图平铺精度（控制贴图在UV方向的最小可重复单元）
定义贴图被分割的最小单元数量：
- 默认值{1,1}表示必须完整贴图重复（1个完整单元）
- 值{5,5}表示贴图被划分为5×5网格，可基于单个网格单元重复
- 值{0,0}表示贴图可以随意重复
值越大表示允许的重复精度越高（对应更小的最小重复区域）

<a id="unreal.AesFacadeMaterialInfo.uv_tile_precision"></a>

#### uv\_tile\_precision

```python
@uv_tile_precision.setter
def uv_tile_precision(value: IntPoint) -> None
```

<a id="unreal.AesFacadeAssetTagData"></a>