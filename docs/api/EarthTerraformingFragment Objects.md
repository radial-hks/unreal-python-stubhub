## EarthTerraformingFragment Objects

```python
class EarthTerraformingFragment(EarthEntityFragment)
```

定义地形改造数据片段的结构体

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: EarthPrefab
- **File**: EarthTerraformingFragment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (float):  [Read-Write] 地形改造深度
- ``edge_offset_z`` (float):  [Read-Write] 边缘在Z轴上的偏移值
- ``edge_width`` (float):  [Read-Write] 地形改造边缘宽度
- ``fuse_near_edge`` (bool):  [Read-Write] 是否融合邻近轮廓线的边缘
- ``inner_edge`` (bool):  [Read-Write] 边缘是否生成在轮廓内
- ``mask_width`` (float):  [Read-Write] 地形改造蒙版宽度
- ``material`` (EarthMaterialInfo):  [Read-Write] 地形改造材质
- ``offset_z`` (float):  [Read-Write] 轮廓线点位在Z轴上的偏移值
- ``optimize_triangulation`` (bool):  [Read-Write] 是否优化三角面排布
- ``outline_expand`` (float):  [Read-Write] 轮廓线扩展距离
- ``valid`` (bool):  [Read-Write] 数据片段是否有效
- ``validated`` (bool):  [Read-Write] 是否已执行数据有效性验证

<a id="unreal.EarthTerraformingFragment.__init__"></a>

#### \_\_init\_\_

```python
def __init__(validated: bool = False,
             valid: bool = False,
             outline_expand: float = 0.000000,
             offset_z: float = 0.000000,
             inner_edge: bool = False,
             edge_width: float = 0.000000,
             edge_offset_z: float = 0.000000,
             mask_width: float = 0.000000,
             depth: float = 0.000000,
             fuse_near_edge: bool = False,
             material: EarthMaterialInfo = [
                 "None", None, 0, False, 255, [0.000000, 0.000000], 0.000000,
                 [0, 0]
             ],
             optimize_triangulation: bool = False) -> None
```

<a id="unreal.EarthTerraformingFragment.outline_expand"></a>

#### outline\_expand

```python
@property
def outline_expand() -> float
```

(float):  [Read-Write] 轮廓线扩展距离

<a id="unreal.EarthTerraformingFragment.outline_expand"></a>

#### outline\_expand

```python
@outline_expand.setter
def outline_expand(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.offset_z"></a>

#### offset\_z

```python
@property
def offset_z() -> float
```

(float):  [Read-Write] 轮廓线点位在Z轴上的偏移值

<a id="unreal.EarthTerraformingFragment.offset_z"></a>

#### offset\_z

```python
@offset_z.setter
def offset_z(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.inner_edge"></a>

#### inner\_edge

```python
@property
def inner_edge() -> bool
```

(bool):  [Read-Write] 边缘是否生成在轮廓内

<a id="unreal.EarthTerraformingFragment.inner_edge"></a>

#### inner\_edge

```python
@inner_edge.setter
def inner_edge(value: bool) -> None
```

<a id="unreal.EarthTerraformingFragment.edge_width"></a>

#### edge\_width

```python
@property
def edge_width() -> float
```

(float):  [Read-Write] 地形改造边缘宽度

<a id="unreal.EarthTerraformingFragment.edge_width"></a>

#### edge\_width

```python
@edge_width.setter
def edge_width(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.edge_offset_z"></a>

#### edge\_offset\_z

```python
@property
def edge_offset_z() -> float
```

(float):  [Read-Write] 边缘在Z轴上的偏移值

<a id="unreal.EarthTerraformingFragment.edge_offset_z"></a>

#### edge\_offset\_z

```python
@edge_offset_z.setter
def edge_offset_z(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.mask_width"></a>

#### mask\_width

```python
@property
def mask_width() -> float
```

(float):  [Read-Write] 地形改造蒙版宽度

<a id="unreal.EarthTerraformingFragment.mask_width"></a>

#### mask\_width

```python
@mask_width.setter
def mask_width(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.depth"></a>

#### depth

```python
@property
def depth() -> float
```

(float):  [Read-Write] 地形改造深度

<a id="unreal.EarthTerraformingFragment.depth"></a>

#### depth

```python
@depth.setter
def depth(value: float) -> None
```

<a id="unreal.EarthTerraformingFragment.fuse_near_edge"></a>

#### fuse\_near\_edge

```python
@property
def fuse_near_edge() -> bool
```

(bool):  [Read-Write] 是否融合邻近轮廓线的边缘

<a id="unreal.EarthTerraformingFragment.fuse_near_edge"></a>

#### fuse\_near\_edge

```python
@fuse_near_edge.setter
def fuse_near_edge(value: bool) -> None
```

<a id="unreal.EarthTerraformingFragment.material"></a>

#### material

```python
@property
def material() -> EarthMaterialInfo
```

(EarthMaterialInfo):  [Read-Write] 地形改造材质

<a id="unreal.EarthTerraformingFragment.material"></a>

#### material

```python
@material.setter
def material(value: EarthMaterialInfo) -> None
```

<a id="unreal.EarthTerraformingFragment.optimize_triangulation"></a>

#### optimize\_triangulation

```python
@property
def optimize_triangulation() -> bool
```

(bool):  [Read-Write] 是否优化三角面排布

<a id="unreal.EarthTerraformingFragment.optimize_triangulation"></a>

#### optimize\_triangulation

```python
@optimize_triangulation.setter
def optimize_triangulation(value: bool) -> None
```

<a id="unreal.EarthTerraformingSplineFragment"></a>