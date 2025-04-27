## PCGSpawnSplineMeshSettings Objects

```python
class PCGSpawnSplineMeshSettings(PCGSettings)
```

Create a USplineMeshComponent for each segment along a given spline.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpawnSplineMesh.h

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
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline mesh creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``spline_mesh_descriptor`` (SoftSplineMeshComponentDescriptor):  [Read-Write]
- ``spline_mesh_override_descriptions`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Overrides for spline mesh descriptor. For now it is only support data wide attributes. Does not work for per-control point overrides for now.
- ``spline_mesh_params`` (PCGSplineMeshParams):  [Read-Write]
- ``synchronous_load`` (bool):  [Read-Write] Force meshes/materials to load synchronously.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSpawnSplineMeshSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline mesh creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGSpawnSplineMeshSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGSpawnSplineMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] Force meshes/materials to load synchronously.

<a id="unreal.PCGSpawnSplineMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGSpawnSplineMeshSettings.spline_mesh_override_descriptions"></a>

#### spline_mesh_override_descriptions

```python
@property
def spline_mesh_override_descriptions(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Overrides for spline mesh descriptor. For now it is only support data wide attributes. Does not work for per-control point overrides for now.

<a id="unreal.PCGSpawnSplineMeshSettings.spline_mesh_override_descriptions"></a>

#### spline_mesh_override_descriptions

```python
@spline_mesh_override_descriptions.setter
def spline_mesh_override_descriptions(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGCreateSplineMeshSettings"></a>