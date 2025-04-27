## PCGPointFromMeshSettings Objects

```python
class PCGPointFromMeshSettings(PCGSettings)
```

PointFromMesh creates a single point at the origin with an attribute containing a SoftObjectPath to the selected UStaticMesh

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPointFromMeshElement.h

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
- ``mesh_path_attribute_name`` (Name):  [Read-Write] Name of the string attribute to be created and hold a SoftObjectPath to the StaticMesh
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``static_mesh`` (StaticMesh):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write] By default, mesh loading is asynchronous, can force it synchronous if needed.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGPointFromMeshSettings.static_mesh"></a>

#### static_mesh

```python
@property
def static_mesh() -> StaticMesh
```

(StaticMesh):  [Read-Write]

<a id="unreal.PCGPointFromMeshSettings.static_mesh"></a>

#### static_mesh

```python
@static_mesh.setter
def static_mesh(value: StaticMesh) -> None
```

<a id="unreal.PCGPointFromMeshSettings.mesh_path_attribute_name"></a>

#### mesh_path_attribute_name

```python
@property
def mesh_path_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the string attribute to be created and hold a SoftObjectPath to the StaticMesh

<a id="unreal.PCGPointFromMeshSettings.mesh_path_attribute_name"></a>

#### mesh_path_attribute_name

```python
@mesh_path_attribute_name.setter
def mesh_path_attribute_name(value: Name) -> None
```

<a id="unreal.PCGPointFromMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, mesh loading is asynchronous, can force it synchronous if needed.

<a id="unreal.PCGPointFromMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGPointMatchAndSetSettings"></a>