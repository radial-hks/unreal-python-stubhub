## PCGProjectionSettings Objects

```python
class PCGProjectionSettings(PCGSettings)
```

PCGProjection Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGProjectionElement.h

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
- ``force_collapse_to_point`` (bool):  [Read-Write] Force the result to be sampled to points, equivalent to having a To Point node after the projection node.
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``projection_params`` (PCGProjectionParams):  [Read-Write]
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGProjectionSettings.projection_params"></a>

#### projection_params

```python
@property
def projection_params() -> PCGProjectionParams
```

(PCGProjectionParams):  [Read-Write]

<a id="unreal.PCGProjectionSettings.projection_params"></a>

#### projection_params

```python
@projection_params.setter
def projection_params(value: PCGProjectionParams) -> None
```

<a id="unreal.PCGProjectionSettings.params"></a>

#### params

```python
@property
def params() -> PCGProjectionParams
```

deprecated: 'params' was renamed to 'projection_params'.

<a id="unreal.PCGProjectionSettings.params"></a>

#### params

```python
@params.setter
def params(value: PCGProjectionParams) -> None
```

<a id="unreal.PCGProjectionSettings.force_collapse_to_point"></a>

#### force_collapse_to_point

```python
@property
def force_collapse_to_point() -> bool
```

(bool):  [Read-Write] Force the result to be sampled to points, equivalent to having a To Point node after the projection node.

<a id="unreal.PCGProjectionSettings.force_collapse_to_point"></a>

#### force_collapse_to_point

```python
@force_collapse_to_point.setter
def force_collapse_to_point(value: bool) -> None
```

<a id="unreal.PCGProjectionSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@property
def keep_zero_density_points() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGProjectionSettings.keep_zero_density_points"></a>

#### keep_zero_density_points

```python
@keep_zero_density_points.setter
def keep_zero_density_points(value: bool) -> None
```

<a id="unreal.PCGSelectPointsSettings"></a>