## SamplerMeshSettingInfo Objects

```python
class SamplerMeshSettingInfo(StructBase)
```

Bp_TreeSamplerTool

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``individual_z_offset`` (float):  [Read-Write]
- ``mesh_width`` (float):  [Read-Write]
- ``overlap_ratio`` (float):  [Read-Write]
- ``random_rotate_range`` (Vector):  [Read-Write]
- ``random_scale_range`` (Vector):  [Read-Write]
- ``ratio`` (float):  [Read-Write]
- ``sampler_mesh`` (StaticMesh):  [Read-Write]
- ``use_individual_mesh_width`` (bool):  [Read-Write]
- ``use_individual_z_offset`` (bool):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(sampler_mesh: StaticMesh = None,
             mesh_width: float = 0.000000,
             use_individual_mesh_width: bool = False,
             ratio: float = 0.000000,
             overlap_ratio: float = 0.000000,
             random_scale_range: Vector = [0.000000, 0.000000, 0.000000],
             random_rotate_range: Vector = [0.000000, 0.000000, 0.000000],
             use_individual_z_offset: bool = False,
             individual_z_offset: float = 0.000000) -> None
```

<a id="unreal.SamplerMeshSettingInfo.sampler_mesh"></a>

#### sampler\_mesh

```python
@property
def sampler_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.sampler_mesh"></a>

#### sampler\_mesh

```python
@sampler_mesh.setter
def sampler_mesh(value: StaticMesh) -> None
```

<a id="unreal.SamplerMeshSettingInfo.mesh_width"></a>

#### mesh\_width

```python
@property
def mesh_width() -> float
```

(float):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.mesh_width"></a>

#### mesh\_width

```python
@mesh_width.setter
def mesh_width(value: float) -> None
```

<a id="unreal.SamplerMeshSettingInfo.use_individual_mesh_width"></a>

#### use\_individual\_mesh\_width

```python
@property
def use_individual_mesh_width() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.use_individual_mesh_width"></a>

#### use\_individual\_mesh\_width

```python
@use_individual_mesh_width.setter
def use_individual_mesh_width(value: bool) -> None
```

<a id="unreal.SamplerMeshSettingInfo.ratio"></a>

#### ratio

```python
@property
def ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.ratio"></a>

#### ratio

```python
@ratio.setter
def ratio(value: float) -> None
```

<a id="unreal.SamplerMeshSettingInfo.overlap_ratio"></a>

#### overlap\_ratio

```python
@property
def overlap_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.overlap_ratio"></a>

#### overlap\_ratio

```python
@overlap_ratio.setter
def overlap_ratio(value: float) -> None
```

<a id="unreal.SamplerMeshSettingInfo.random_scale_range"></a>

#### random\_scale\_range

```python
@property
def random_scale_range() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.random_scale_range"></a>

#### random\_scale\_range

```python
@random_scale_range.setter
def random_scale_range(value: Vector) -> None
```

<a id="unreal.SamplerMeshSettingInfo.random_rotate_range"></a>

#### random\_rotate\_range

```python
@property
def random_rotate_range() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.random_rotate_range"></a>

#### random\_rotate\_range

```python
@random_rotate_range.setter
def random_rotate_range(value: Vector) -> None
```

<a id="unreal.SamplerMeshSettingInfo.use_individual_z_offset"></a>

#### use\_individual\_z\_offset

```python
@property
def use_individual_z_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.use_individual_z_offset"></a>

#### use\_individual\_z\_offset

```python
@use_individual_z_offset.setter
def use_individual_z_offset(value: bool) -> None
```

<a id="unreal.SamplerMeshSettingInfo.individual_z_offset"></a>

#### individual\_z\_offset

```python
@property
def individual_z_offset() -> float
```

(float):  [Read-Write]

<a id="unreal.SamplerMeshSettingInfo.individual_z_offset"></a>

#### individual\_z\_offset

```python
@individual_z_offset.setter
def individual_z_offset(value: float) -> None
```

<a id="unreal.TreeSamplerNodeInfo"></a>