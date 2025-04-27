## PCGAppendMeshesFromPointsSettings Objects

```python
class PCGAppendMeshesFromPointsSettings(PCGDynamicMeshBaseSettings)
```

Append meshes at the points transforms. Mesh can be a single static mesh, multiple meshes coming from the points or another dynamic mesh.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGAppendMeshesFromPoints.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
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
- ``extract_materials`` (bool):  [Read-Write] Allows to extract materials from the static mesh and set them in the resulting append.
- ``mesh_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``mode`` (PCGAppendMeshesFromPointsMode):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``requested_lod_index`` (int32):  [Read-Write]
- ``requested_lod_type`` (GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.
- ``seed`` (int32):  [Read-Write]
- ``static_mesh`` (StaticMesh):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAppendMeshesFromPointsSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGAppendMeshesFromPointsMode
```

(PCGAppendMeshesFromPointsMode):  [Read-Write]

<a id="unreal.PCGAppendMeshesFromPointsSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGAppendMeshesFromPointsMode) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.PCGAppendMeshesFromPointsSettings.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.mesh_attribute"></a>

#### mesh_attribute

```python
@property
def mesh_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAppendMeshesFromPointsSettings.mesh_attribute"></a>

#### mesh_attribute

```python
@mesh_attribute.setter
def mesh_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.extract_materials"></a>

#### extract_materials

```python
@property
def extract_materials() -> bool
```

(bool):  [Read-Write] Allows to extract materials from the static mesh and set them in the resulting append.

<a id="unreal.PCGAppendMeshesFromPointsSettings.extract_materials"></a>

#### extract_materials

```python
@extract_materials.setter
def extract_materials(value: bool) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@property
def requested_lod_type() -> GeometryScriptLODType
```

(GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.

<a id="unreal.PCGAppendMeshesFromPointsSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@requested_lod_type.setter
def requested_lod_type(value: GeometryScriptLODType) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@property
def requested_lod_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGAppendMeshesFromPointsSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@requested_lod_index.setter
def requested_lod_index(value: int) -> None
```

<a id="unreal.PCGAppendMeshesFromPointsSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAppendMeshesFromPointsSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGBooleanOperationSettings"></a>