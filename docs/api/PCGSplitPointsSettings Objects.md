## PCGSplitPointsSettings Objects

```python
class PCGSplitPointsSettings(PCGSettings)
```

Splits each point into two separate points, and sets bounds based on the position and axis of the cut.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSplitPoints.h

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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``split_axis`` (PCGSplitAxis):  [Read-Write]
- ``split_position`` (float):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSplitPointsSettings.split_position"></a>

#### split_position

```python
@property
def split_position() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGSplitPointsSettings.split_position"></a>

#### split_position

```python
@split_position.setter
def split_position(value: float) -> None
```

<a id="unreal.PCGSplitPointsSettings.split_axis"></a>

#### split_axis

```python
@property
def split_axis() -> PCGSplitAxis
```

(PCGSplitAxis):  [Read-Write]

<a id="unreal.PCGSplitPointsSettings.split_axis"></a>

#### split_axis

```python
@split_axis.setter
def split_axis(value: PCGSplitAxis) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings"></a>