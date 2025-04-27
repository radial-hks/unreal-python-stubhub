## PCGDensityRemapSettings Objects

```python
class PCGDensityRemapSettings(PCGSettings)
```

PCGDensity Remap Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDensityRemapElement.h

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
- ``exclude_values_outside_input_range`` (bool):  [Read-Write] Density values outside of the input range will be unaffected by the remapping
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``out_range_max`` (float):  [Read-Write]
- ``out_range_min`` (float):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``range_max`` (float):  [Read-Write] If InRangeMin = InRangeMax, then that density value is mapped to the average of OutRangeMin and OutRangeMax
- ``range_min`` (float):  [Read-Write] If InRangeMin = InRangeMax, then that density value is mapped to the average of OutRangeMin and OutRangeMax
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDensityRemapSettings.range_min"></a>

#### range_min

```python
@property
def range_min() -> float
```

(float):  [Read-Write] If InRangeMin = InRangeMax, then that density value is mapped to the average of OutRangeMin and OutRangeMax

<a id="unreal.PCGDensityRemapSettings.range_min"></a>

#### range_min

```python
@range_min.setter
def range_min(value: float) -> None
```

<a id="unreal.PCGDensityRemapSettings.range_max"></a>

#### range_max

```python
@property
def range_max() -> float
```

(float):  [Read-Write] If InRangeMin = InRangeMax, then that density value is mapped to the average of OutRangeMin and OutRangeMax

<a id="unreal.PCGDensityRemapSettings.range_max"></a>

#### range_max

```python
@range_max.setter
def range_max(value: float) -> None
```

<a id="unreal.PCGDensityRemapSettings.out_range_min"></a>

#### out_range_min

```python
@property
def out_range_min() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGDensityRemapSettings.out_range_min"></a>

#### out_range_min

```python
@out_range_min.setter
def out_range_min(value: float) -> None
```

<a id="unreal.PCGDensityRemapSettings.out_range_max"></a>

#### out_range_max

```python
@property
def out_range_max() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGDensityRemapSettings.out_range_max"></a>

#### out_range_max

```python
@out_range_max.setter
def out_range_max(value: float) -> None
```

<a id="unreal.PCGDensityRemapSettings.exclude_values_outside_input_range"></a>

#### exclude_values_outside_input_range

```python
@property
def exclude_values_outside_input_range() -> bool
```

(bool):  [Read-Write] Density values outside of the input range will be unaffected by the remapping

<a id="unreal.PCGDensityRemapSettings.exclude_values_outside_input_range"></a>

#### exclude_values_outside_input_range

```python
@exclude_values_outside_input_range.setter
def exclude_values_outside_input_range(value: bool) -> None
```

<a id="unreal.PCGDifferenceSettings"></a>