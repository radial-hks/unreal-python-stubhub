## AesVegetationSpecie Objects

```python
class AesVegetationSpecie(TableRowBase)
```

植被树种资产标签数据

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesAsset
- **File**: AesVegetationAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``align_normal`` (bool):  [Read-Write] 对齐地表法线
- ``height_limit_range`` (Vector2f):  [Read-Write] 高度限制
- ``mesh`` (SoftObjectPath):  [Read-Write]
- ``ratio`` (float):  [Read-Write] 散布权重
- ``scale_range`` (Vector2f):  [Read-Write] 缩放值范围
- ``slope_limit_range`` (Vector2f):  [Read-Write] 坡度踢除度数
- ``vgm_edge_scale_range`` (Vector2f):  [Read-Write] Vgm边缘缩放值
- ``z_offset`` (float):  [Read-Write] 植被树种 Z Offset

<a id="unreal.AesVegetationSpecie.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mesh: SoftObjectPath = [""],
             ratio: float = 0.000000,
             scale_range: Vector2f = [0.000000, 0.000000],
             vgm_edge_scale_range: Vector2f = [0.000000, 0.000000],
             slope_limit_range: Vector2f = [0.000000, 0.000000],
             align_normal: bool = False,
             height_limit_range: Vector2f = [0.000000, 0.000000],
             z_offset: float = 0.000000) -> None
```

<a id="unreal.AesVegetationSpecie.mesh"></a>

#### mesh

```python
@property
def mesh() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.AesVegetationSpecie.mesh"></a>

#### mesh

```python
@mesh.setter
def mesh(value: SoftObjectPath) -> None
```

<a id="unreal.AesVegetationSpecie.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write] 散布权重

<a id="unreal.AesVegetationSpecie.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.AesVegetationSpecie.scale_range"></a>

#### scale\_range

```python
@property
def scale_range() -> Vector2f
```

(Vector2f):  [Read-Write] 缩放值范围

<a id="unreal.AesVegetationSpecie.scale_range"></a>

#### scale\_range

```python
@scale_range.setter
def scale_range(value: Vector2f) -> None
```

<a id="unreal.AesVegetationSpecie.vgm_edge_scale_range"></a>

#### vgm\_edge\_scale\_range

```python
@property
def vgm_edge_scale_range() -> Vector2f
```

(Vector2f):  [Read-Write] Vgm边缘缩放值

<a id="unreal.AesVegetationSpecie.vgm_edge_scale_range"></a>

#### vgm\_edge\_scale\_range

```python
@vgm_edge_scale_range.setter
def vgm_edge_scale_range(value: Vector2f) -> None
```

<a id="unreal.AesVegetationSpecie.slope_limit_range"></a>

#### slope\_limit\_range

```python
@property
def slope_limit_range() -> Vector2f
```

(Vector2f):  [Read-Write] 坡度踢除度数

<a id="unreal.AesVegetationSpecie.slope_limit_range"></a>

#### slope\_limit\_range

```python
@slope_limit_range.setter
def slope_limit_range(value: Vector2f) -> None
```

<a id="unreal.AesVegetationSpecie.align_normal"></a>

#### align\_normal

```python
@property
def align_normal() -> bool
```

(bool):  [Read-Write] 对齐地表法线

<a id="unreal.AesVegetationSpecie.align_normal"></a>

#### align\_normal

```python
@align_normal.setter
def align_normal(value: bool) -> None
```

<a id="unreal.AesVegetationSpecie.height_limit_range"></a>

#### height\_limit\_range

```python
@property
def height_limit_range() -> Vector2f
```

(Vector2f):  [Read-Write] 高度限制

<a id="unreal.AesVegetationSpecie.height_limit_range"></a>

#### height\_limit\_range

```python
@height_limit_range.setter
def height_limit_range(value: Vector2f) -> None
```

<a id="unreal.AesVegetationSpecie.z_offset"></a>

#### z\_offset

```python
@property
def z_offset() -> float
```

(float):  [Read-Write] 植被树种 Z Offset

<a id="unreal.AesVegetationSpecie.z_offset"></a>

#### z\_offset

```python
@z_offset.setter
def z_offset(value: float) -> None
```

<a id="unreal.AesVegetationSpeciesArray"></a>