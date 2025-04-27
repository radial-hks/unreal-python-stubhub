## PCGCullPointsOutsideActorBoundsSettings Objects

```python
class PCGCullPointsOutsideActorBoundsSettings(PCGSettings)
```

Removes points that lie outside the current actor bounds.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCullPointsOutsideActorBounds.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bounds_expansion`` (float):  [Read-Write]
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
- ``mode`` (PCGCullPointsMode):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCullPointsOutsideActorBoundsSettings.bounds_expansion"></a>

#### bounds_expansion

```python
@property
def bounds_expansion() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGCullPointsOutsideActorBoundsSettings.bounds_expansion"></a>

#### bounds_expansion

```python
@bounds_expansion.setter
def bounds_expansion(value: float) -> None
```

<a id="unreal.PCGCullPointsOutsideActorBoundsSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGCullPointsMode
```

(PCGCullPointsMode):  [Read-Write]

<a id="unreal.PCGCullPointsOutsideActorBoundsSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGCullPointsMode) -> None
```

<a id="unreal.PCGDataAsset"></a>