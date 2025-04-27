## PCGOuterIntersectionSettings Objects

```python
class PCGOuterIntersectionSettings(PCGSettingsWithDynamicInputs)
```

PCGOuter Intersection Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGOuterIntersectionElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``density_function`` (PCGIntersectionDensityFunction):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``ignore_pins_with_no_input`` (bool):  [Read-Write] If enabled, dynamic input pins that have no incoming data will be bypassed during the intersection operation
  calculation, which would otherwise result in an empty result.
- ``keep_zero_density_points`` (bool):  [Read-Write] If enabled, output points with a density value of 0 will NOT be automatically filtered out.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGOuterIntersectionSettings.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGIntersectionDensityFunction
```

(PCGIntersectionDensityFunction):  [Read-Write]

<a id="unreal.PCGOuterIntersectionSettings.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGIntersectionDensityFunction) -> None
```

<a id="unreal.PCGOuterIntersectionSettings.ignore_pins_with_no_input"></a>

#### ignore_pins_with_no_input

```python
@property
def ignore_pins_with_no_input() -> bool
```

(bool):  [Read-Write] If enabled, dynamic input pins that have no incoming data will be bypassed during the intersection operation
calculation, which would otherwise result in an empty result.

<a id="unreal.PCGOuterIntersectionSettings.ignore_pins_with_no_input"></a>

#### ignore_pins_with_no_input

```python
@ignore_pins_with_no_input.setter
def ignore_pins_with_no_input(value: bool) -> None
```

<a id="unreal.PCGOuterIntersectionSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write] If enabled, output points with a density value of 0 will NOT be automatically filtered out.

<a id="unreal.PCGOuterIntersectionSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGParseStringSettings"></a>