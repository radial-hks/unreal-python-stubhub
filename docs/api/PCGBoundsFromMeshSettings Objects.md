## PCGBoundsFromMeshSettings Objects

```python
class PCGBoundsFromMeshSettings(PCGSettings)
```

Sets the bounds on the points according to the mesh(es) provided in the mesh pin.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGBoundsFromMesh.h

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
- ``mesh_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute from which to source the meshes to use.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``silence_attribute_not_found_errors`` (bool):  [Read-Write] Will not produce warnings when the input data does not have the required attribute.
- ``synchronous_load`` (bool):  [Read-Write] By default, will use async loading for the meshes.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGBoundsFromMeshSettings.mesh_attribute"></a>

#### mesh_attribute

```python
@property
def mesh_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute from which to source the meshes to use.

<a id="unreal.PCGBoundsFromMeshSettings.mesh_attribute"></a>

#### mesh_attribute

```python
@mesh_attribute.setter
def mesh_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGBoundsFromMeshSettings.silence_attribute_not_found_errors"></a>

#### silence_attribute_not_found_errors

```python
@property
def silence_attribute_not_found_errors() -> bool
```

(bool):  [Read-Write] Will not produce warnings when the input data does not have the required attribute.

<a id="unreal.PCGBoundsFromMeshSettings.silence_attribute_not_found_errors"></a>

#### silence_attribute_not_found_errors

```python
@silence_attribute_not_found_errors.setter
def silence_attribute_not_found_errors(value: bool) -> None
```

<a id="unreal.PCGBoundsFromMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] By default, will use async loading for the meshes.

<a id="unreal.PCGBoundsFromMeshSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGBranchSettings"></a>