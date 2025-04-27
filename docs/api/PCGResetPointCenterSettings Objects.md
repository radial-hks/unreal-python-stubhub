## PCGResetPointCenterSettings Objects

```python
class PCGResetPointCenterSettings(PCGSettings)
```

Modify the position of a point within its bounds, while keeping its bounds the same.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGResetPointCenter.h

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
- ``point_center_location`` (Vector):  [Read-Write] Set the normalized center of the point
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGResetPointCenterSettings.point_center_location"></a>

#### point_center_location

```python
@property
def point_center_location() -> Vector
```

(Vector):  [Read-Write] Set the normalized center of the point

<a id="unreal.PCGResetPointCenterSettings.point_center_location"></a>

#### point_center_location

```python
@point_center_location.setter
def point_center_location(value: Vector) -> None
```

<a id="unreal.PCGSampleTextureSettings"></a>