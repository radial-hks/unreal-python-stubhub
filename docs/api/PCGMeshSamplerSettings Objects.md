## PCGMeshSamplerSettings Objects

```python
class PCGMeshSamplerSettings(PCGSettings)
```

Sample points on a mesh.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGMeshSampler.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``color_channel_as_density`` (PCGColorChannel):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``extract_mesh_from_input`` (bool):  [Read-Write] Can provide a list of inputs to sample the meshes from. It can be a list of StaticMeshes, a list of Actors that have a Scene Component (like a Static Mesh Component), or a list of Scene Components directly.
  Geometry Script needs to be able to extract a dynamic mesh from this scene component (so won't work for ISMCs for example) and for now will work only with a single scene component.
  Each entry (either in the same data or seperate data) will produce a unique output data.
- ``extract_uv_as_attribute`` (bool):  [Read-Write]
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write] Selector to read data from.
- ``material_attribute_name`` (Name):  [Read-Write]
- ``material_id_attribute_name`` (Name):  [Read-Write]
- ``non_uniform_sampling_options`` (GeometryScriptNonUniformPointSamplingOptions):  [Read-Write]
- ``output_material_info`` (bool):  [Read-Write]
- ``output_triangle_ids`` (bool):  [Read-Write]
- ``point_steepness`` (float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
  1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
  increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
  represent a binary box function with the size of the point's bounds.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``remove_hidden_triangles`` (bool):  [Read-Write] Post-processing pass after voxelization to remove hidden triangles.
- ``requested_lod_index`` (int32):  [Read-Write]
- ``requested_lod_type`` (GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.
- ``sampling_method`` (PCGMeshSamplingMethod):  [Read-Write]
- ``sampling_options`` (GeometryScriptMeshPointSamplingOptions):  [Read-Write] Poisson Sampling parameters
- ``seed`` (int32):  [Read-Write]
- ``static_mesh`` (StaticMesh):  [Read-Write] Soft Object Path to the mesh to sample from. Will be loaded.
- ``synchronous_load`` (bool):  [Read-Write]
- ``triangle_id_attribute_name`` (Name):  [Read-Write]
- ``use_color_channel_as_density`` (bool):  [Read-Write] Will extract the color channel into the density.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``uv_attribute_name`` (Name):  [Read-Write]
- ``uv_channel`` (int32):  [Read-Write]
- ``voxel_size`` (float):  [Read-Write] Size of a voxel for the voxelization.
- ``voxelize`` (bool):  [Read-Write] Enable voxelisation as a preparation pass. Can be more expensive given the VoxelSize.

<a id="unreal.PCGMeshSamplerSettings.extract_mesh_from_input"></a>

#### extract_mesh_from_input

```python
@property
def extract_mesh_from_input() -> bool
```

(bool):  [Read-Write] Can provide a list of inputs to sample the meshes from. It can be a list of StaticMeshes, a list of Actors that have a Scene Component (like a Static Mesh Component), or a list of Scene Components directly.
Geometry Script needs to be able to extract a dynamic mesh from this scene component (so won't work for ISMCs for example) and for now will work only with a single scene component.
Each entry (either in the same data or seperate data) will produce a unique output data.

<a id="unreal.PCGMeshSamplerSettings.extract_mesh_from_input"></a>

#### extract_mesh_from_input

```python
@extract_mesh_from_input.setter
def extract_mesh_from_input(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write] Soft Object Path to the mesh to sample from. Will be loaded.

<a id="unreal.PCGMeshSamplerSettings.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.PCGMeshSamplerSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Selector to read data from.

<a id="unreal.PCGMeshSamplerSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMeshSamplerSettings.sampling_method"></a>

#### sampling_method

```python
@property
def sampling_method() -> PCGMeshSamplingMethod
```

(PCGMeshSamplingMethod):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.sampling_method"></a>

#### sampling_method

```python
@sampling_method.setter
def sampling_method(value: PCGMeshSamplingMethod) -> None
```

<a id="unreal.PCGMeshSamplerSettings.use_color_channel_as_density"></a>

#### use_color_channel_as_density

```python
@property
def use_color_channel_as_density() -> bool
```

(bool):  [Read-Write] Will extract the color channel into the density.

<a id="unreal.PCGMeshSamplerSettings.use_color_channel_as_density"></a>

#### use_color_channel_as_density

```python
@use_color_channel_as_density.setter
def use_color_channel_as_density(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.color_channel_as_density"></a>

#### color_channel_as_density

```python
@property
def color_channel_as_density() -> PCGColorChannel
```

(PCGColorChannel):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.color_channel_as_density"></a>

#### color_channel_as_density

```python
@color_channel_as_density.setter
def color_channel_as_density(value: PCGColorChannel) -> None
```

<a id="unreal.PCGMeshSamplerSettings.voxelize"></a>

#### voxelize

```python
@property
def voxelize() -> bool
```

(bool):  [Read-Write] Enable voxelisation as a preparation pass. Can be more expensive given the VoxelSize.

<a id="unreal.PCGMeshSamplerSettings.voxelize"></a>

#### voxelize

```python
@voxelize.setter
def voxelize(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.voxel_size"></a>

#### voxel_size

```python
@property
def voxel_size() -> float
```

(float):  [Read-Write] Size of a voxel for the voxelization.

<a id="unreal.PCGMeshSamplerSettings.voxel_size"></a>

#### voxel_size

```python
@voxel_size.setter
def voxel_size(value: float) -> None
```

<a id="unreal.PCGMeshSamplerSettings.remove_hidden_triangles"></a>

#### remove_hidden_triangles

```python
@property
def remove_hidden_triangles() -> bool
```

(bool):  [Read-Write] Post-processing pass after voxelization to remove hidden triangles.

<a id="unreal.PCGMeshSamplerSettings.remove_hidden_triangles"></a>

#### remove_hidden_triangles

```python
@remove_hidden_triangles.setter
def remove_hidden_triangles(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@property
def requested_lod_type() -> GeometryScriptLODType
```

(GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.

<a id="unreal.PCGMeshSamplerSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@requested_lod_type.setter
def requested_lod_type(value: GeometryScriptLODType) -> None
```

<a id="unreal.PCGMeshSamplerSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@property
def requested_lod_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@requested_lod_index.setter
def requested_lod_index(value: int) -> None
```

<a id="unreal.PCGMeshSamplerSettings.sampling_options"></a>

#### sampling_options

```python
@property
def sampling_options() -> GeometryScriptMeshPointSamplingOptions
```

(GeometryScriptMeshPointSamplingOptions):  [Read-Write] Poisson Sampling parameters

<a id="unreal.PCGMeshSamplerSettings.sampling_options"></a>

#### sampling_options

```python
@sampling_options.setter
def sampling_options(value: GeometryScriptMeshPointSamplingOptions) -> None
```

<a id="unreal.PCGMeshSamplerSettings.non_uniform_sampling_options"></a>

#### non_uniform_sampling_options

```python
@property
def non_uniform_sampling_options(
) -> GeometryScriptNonUniformPointSamplingOptions
```

(GeometryScriptNonUniformPointSamplingOptions):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.non_uniform_sampling_options"></a>

#### non_uniform_sampling_options

```python
@non_uniform_sampling_options.setter
def non_uniform_sampling_options(
        value: GeometryScriptNonUniformPointSamplingOptions) -> None
```

<a id="unreal.PCGMeshSamplerSettings.extract_uv_as_attribute"></a>

#### extract_uv_as_attribute

```python
@property
def extract_uv_as_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.extract_uv_as_attribute"></a>

#### extract_uv_as_attribute

```python
@extract_uv_as_attribute.setter
def extract_uv_as_attribute(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.uv_attribute_name"></a>

#### uv_attribute_name

```python
@property
def uv_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.uv_attribute_name"></a>

#### uv_attribute_name

```python
@uv_attribute_name.setter
def uv_attribute_name(value: Name) -> None
```

<a id="unreal.PCGMeshSamplerSettings.uv_channel"></a>

#### uv_channel

```python
@property
def uv_channel() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.uv_channel"></a>

#### uv_channel

```python
@uv_channel.setter
def uv_channel(value: int) -> None
```

<a id="unreal.PCGMeshSamplerSettings.output_triangle_ids"></a>

#### output_triangle_ids

```python
@property
def output_triangle_ids() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.output_triangle_ids"></a>

#### output_triangle_ids

```python
@output_triangle_ids.setter
def output_triangle_ids(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.triangle_id_attribute_name"></a>

#### triangle_id_attribute_name

```python
@property
def triangle_id_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.triangle_id_attribute_name"></a>

#### triangle_id_attribute_name

```python
@triangle_id_attribute_name.setter
def triangle_id_attribute_name(value: Name) -> None
```

<a id="unreal.PCGMeshSamplerSettings.output_material_info"></a>

#### output_material_info

```python
@property
def output_material_info() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.output_material_info"></a>

#### output_material_info

```python
@output_material_info.setter
def output_material_info(value: bool) -> None
```

<a id="unreal.PCGMeshSamplerSettings.material_id_attribute_name"></a>

#### material_id_attribute_name

```python
@property
def material_id_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.material_id_attribute_name"></a>

#### material_id_attribute_name

```python
@material_id_attribute_name.setter
def material_id_attribute_name(value: Name) -> None
```

<a id="unreal.PCGMeshSamplerSettings.material_attribute_name"></a>

#### material_attribute_name

```python
@property
def material_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.material_attribute_name"></a>

#### material_attribute_name

```python
@material_attribute_name.setter
def material_attribute_name(value: Name) -> None
```

<a id="unreal.PCGMeshSamplerSettings.point_steepness"></a>

#### point_steepness

```python
@property
def point_steepness() -> float
```

(float):  [Read-Write] Each PCG point represents a discretized, volumetric region of world space. The points' Steepness value [0.0 to
1.0] establishes how "hard" or "soft" that volume will be represented. From 0, it will ramp up linearly
increasing its influence over the density from the point's center to up to two times the bounds. At 1, it will
represent a binary box function with the size of the point's bounds.

<a id="unreal.PCGMeshSamplerSettings.point_steepness"></a>

#### point_steepness

```python
@point_steepness.setter
def point_steepness(value: float) -> None
```

<a id="unreal.PCGMeshSamplerSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMeshSamplerSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGPrimitiveCrossSectionSettings"></a>