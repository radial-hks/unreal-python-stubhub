## PCGDifferenceSettings Objects

```python
class PCGDifferenceSettings(PCGSettings)
```

PCGDifference Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDifferenceElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``density_function`` (PCGDifferenceDensityFunction):  [Read-Write] The density function to use when recalculating the density after the operation.
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``diff_metadata`` (bool):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``keep_zero_density_points`` (bool):  [Read-Write] If enabled, the output will not automatically filter out points with zero density.
- ``mode`` (PCGDifferenceMode):  [Read-Write] Describes how the difference operation will treat the output data:
  Continuous - Non-destructive data output will be maintained.
  Discrete - Output data will be discrete points, or explicitly converted to points.
  Inferred - Output data will choose from Continuous or Discrete, based on the source and operation.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDifferenceSettings.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGDifferenceDensityFunction
```

(PCGDifferenceDensityFunction):  [Read-Write] The density function to use when recalculating the density after the operation.

<a id="unreal.PCGDifferenceSettings.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGDifferenceDensityFunction) -> None
```

<a id="unreal.PCGDifferenceSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGDifferenceMode
```

(PCGDifferenceMode):  [Read-Write] Describes how the difference operation will treat the output data:
Continuous - Non-destructive data output will be maintained.
Discrete - Output data will be discrete points, or explicitly converted to points.
Inferred - Output data will choose from Continuous or Discrete, based on the source and operation.

<a id="unreal.PCGDifferenceSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGDifferenceMode) -> None
```

<a id="unreal.PCGDifferenceSettings.diff_metadata"></a>

#### diff_metadata

```python
@property
def diff_metadata() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDifferenceSettings.diff_metadata"></a>

#### diff_metadata

```python
@diff_metadata.setter
def diff_metadata(value: bool) -> None
```

<a id="unreal.PCGDifferenceSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write] If enabled, the output will not automatically filter out points with zero density.

<a id="unreal.PCGDifferenceSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGBlueprintElement"></a>