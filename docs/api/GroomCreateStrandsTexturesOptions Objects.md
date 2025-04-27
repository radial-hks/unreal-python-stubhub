## GroomCreateStrandsTexturesOptions Objects

```python
class GroomCreateStrandsTexturesOptions(Object)
```

Groom Create Strands Textures Options

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomCreateStrandsTexturesOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dilation`` (int32):  [Read-Write] Number pixels expanded by the post-process dilation (0..64).
- ``group_index`` (Array[int32]):  [Read-Write] Groom index which should be baked into the textures. When the array is empty, all groups will be included (Default).
- ``layout`` (HairTextureLayout):  [Read-Write] Resolution of the output texture maps (tangent, coverage, ...)
- ``lod_index`` (int32):  [Read-Write] LOD of the mesh, on which the texture projection is done
- ``mesh_type`` (StrandsTexturesMeshType):  [Read-Write] Select which mesh should be used for tracing
- ``resolution`` (int32):  [Read-Write] Resolution of the output texture maps (tangent, coverage, ...)
- ``section_index`` (int32):  [Read-Write] Section of the mesh, on which the texture projection is done
- ``skeletal_mesh`` (SkeletalMesh):  [Read-Write] Mesh on which the groom strands will be projected on. If non empty, the skeletal mesh will be used for generating the textures.
- ``static_mesh`` (StaticMesh):  [Read-Write] Mesh on which the groom strands will be projected on. If non empty and if the skeletal mesh entry is empty, the static mesh will be used for generating the textures.
- ``trace_distance`` (float):  [Read-Write] Distance from the mesh surface until hair are projected onto the mesh.
- ``trace_type`` (StrandsTexturesTraceType):  [Read-Write] Direction in which the tracing will be done: either from the mesh's surface to the outside, or from the mesh's surface to the inside.
- ``uv_channel_index`` (int32):  [Read-Write] UV channel to use

<a id="unreal.GroomCreateStrandsTexturesOptions.layout"></a>

#### layout

```python
@property
def layout() -> HairTextureLayout
```

(HairTextureLayout):  [Read-Write] Resolution of the output texture maps (tangent, coverage, ...)

<a id="unreal.GroomCreateStrandsTexturesOptions.layout"></a>

#### layout

```python
@layout.setter
def layout(value: HairTextureLayout) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.resolution"></a>

#### resolution

```python
@property
def resolution() -> int
```

(int32):  [Read-Write] Resolution of the output texture maps (tangent, coverage, ...)

<a id="unreal.GroomCreateStrandsTexturesOptions.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: int) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.trace_type"></a>

#### trace_type

```python
@property
def trace_type() -> StrandsTexturesTraceType
```

(StrandsTexturesTraceType):  [Read-Write] Direction in which the tracing will be done: either from the mesh's surface to the outside, or from the mesh's surface to the inside.

<a id="unreal.GroomCreateStrandsTexturesOptions.trace_type"></a>

#### trace_type

```python
@trace_type.setter
def trace_type(value: StrandsTexturesTraceType) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.trace_distance"></a>

#### trace_distance

```python
@property
def trace_distance() -> float
```

(float):  [Read-Write] Distance from the mesh surface until hair are projected onto the mesh.

<a id="unreal.GroomCreateStrandsTexturesOptions.trace_distance"></a>

#### trace_distance

```python
@trace_distance.setter
def trace_distance(value: float) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.mesh_type"></a>

#### mesh_type

```python
@property
def mesh_type() -> StrandsTexturesMeshType
```

(StrandsTexturesMeshType):  [Read-Write] Select which mesh should be used for tracing

<a id="unreal.GroomCreateStrandsTexturesOptions.mesh_type"></a>

#### mesh_type

```python
@mesh_type.setter
def mesh_type(value: StrandsTexturesMeshType) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] Mesh on which the groom strands will be projected on. If non empty and if the skeletal mesh entry is empty, the static mesh will be used for generating the textures.

<a id="unreal.GroomCreateStrandsTexturesOptions.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.skeletal_mesh"></a>

#### skeletal_mesh

```python
@property
def skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write] Mesh on which the groom strands will be projected on. If non empty, the skeletal mesh will be used for generating the textures.

<a id="unreal.GroomCreateStrandsTexturesOptions.skeletal_mesh"></a>

#### skeletal_mesh

```python
@skeletal_mesh.setter
def skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.lod_index"></a>

#### lod_index

```python
@property
def lod_index() -> int
```

(int32):  [Read-Write] LOD of the mesh, on which the texture projection is done

<a id="unreal.GroomCreateStrandsTexturesOptions.lod_index"></a>

#### lod_index

```python
@lod_index.setter
def lod_index(value: int) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.section_index"></a>

#### section_index

```python
@property
def section_index() -> int
```

(int32):  [Read-Write] Section of the mesh, on which the texture projection is done

<a id="unreal.GroomCreateStrandsTexturesOptions.section_index"></a>

#### section_index

```python
@section_index.setter
def section_index(value: int) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.uv_channel_index"></a>

#### uv_channel_index

```python
@property
def uv_channel_index() -> int
```

(int32):  [Read-Write] UV channel to use

<a id="unreal.GroomCreateStrandsTexturesOptions.uv_channel_index"></a>

#### uv_channel_index

```python
@uv_channel_index.setter
def uv_channel_index(value: int) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.group_index"></a>

#### group_index

```python
@property
def group_index() -> Array[int]
```

(Array[int32]):  [Read-Write] Groom index which should be baked into the textures. When the array is empty, all groups will be included (Default).

<a id="unreal.GroomCreateStrandsTexturesOptions.group_index"></a>

#### group_index

```python
@group_index.setter
def group_index(value: Array[int]) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions.dilation"></a>

#### dilation

```python
@property
def dilation() -> int
```

(int32):  [Read-Write] Number pixels expanded by the post-process dilation (0..64).

<a id="unreal.GroomCreateStrandsTexturesOptions.dilation"></a>

#### dilation

```python
@dilation.setter
def dilation(value: int) -> None
```

<a id="unreal.GroomImportOptions"></a>