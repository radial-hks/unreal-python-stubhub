## PCGStaticMeshToDynamicMeshSettings Objects

```python
class PCGStaticMeshToDynamicMeshSettings(PCGDynamicMeshBaseSettings)
```

Convert a static mesh into a dynamic mesh data.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGStaticMeshToDynamicMeshElement.h

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
- ``extract_materials`` (bool):  [Read-Write] Allows to extract materials from the static mesh and store them in the PCG Dynamic Mesh Data.
- ``override_materials`` (Array[MaterialInterface]):  [Read-Write] If it extracts materials, we can specify override materials. It needs to have the same number of material overrides than there are materials on the static mesh.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``requested_lod_index`` (int32):  [Read-Write]
- ``requested_lod_type`` (GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.
- ``seed`` (int32):  [Read-Write]
- ``static_mesh`` (StaticMesh):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.extract_materials"></a>

#### extract_materials

```python
@property
def extract_materials() -> bool
```

(bool):  [Read-Write] Allows to extract materials from the static mesh and store them in the PCG Dynamic Mesh Data.

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.extract_materials"></a>

#### extract_materials

```python
@extract_materials.setter
def extract_materials(value: bool) -> None
```

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@property
def requested_lod_type() -> GeometryScriptLODType
```

(GeometryScriptLODType):  [Read-Write] LOD type to use when creating DynamicMesh from specified StaticMesh.

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_type"></a>

#### requested_lod_type

```python
@requested_lod_type.setter
def requested_lod_type(value: GeometryScriptLODType) -> None
```

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@property
def requested_lod_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.requested_lod_index"></a>

#### requested_lod_index

```python
@requested_lod_index.setter
def requested_lod_index(value: int) -> None
```

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGStaticMeshToDynamicMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.AppleImageUtilsBaseAsyncTaskBlueprintProxy"></a>