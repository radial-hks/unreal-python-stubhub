## PCGDensityFilterSettings Objects

```python
class PCGDensityFilterSettings(PCGSettings)
```

PCGDensity Filter Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDensityFilter.h

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
- ``invert_filter`` (bool):  [Read-Write]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``lower_bound`` (float):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``upper_bound`` (float):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDensityFilterSettings.lower_bound"></a>

#### lower_bound

```python
@property
def lower_bound() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGDensityFilterSettings.lower_bound"></a>

#### lower_bound

```python
@lower_bound.setter
def lower_bound(value: float) -> None
```

<a id="unreal.PCGDensityFilterSettings.upper_bound"></a>

#### upper_bound

```python
@property
def upper_bound() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGDensityFilterSettings.upper_bound"></a>

#### upper_bound

```python
@upper_bound.setter
def upper_bound(value: float) -> None
```

<a id="unreal.PCGDensityFilterSettings.invert_filter"></a>

#### invert_filter

```python
@property
def invert_filter() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDensityFilterSettings.invert_filter"></a>

#### invert_filter

```python
@invert_filter.setter
def invert_filter(value: bool) -> None
```

<a id="unreal.PCGDensityFilterSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDensityFilterSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGDensityRemapSettings"></a>