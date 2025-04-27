## PCGAttributeNoiseSettings Objects

```python
class PCGAttributeNoiseSettings(PCGSettings)
```

Apply some noise to an attribute/property. You can select the mode you want and a noise range.
Support all numerical types and vectors/rotators.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeNoise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``clamp_result`` (bool):  [Read-Write] Clamp the result between 0 and 1. Always applied if we apply noise to the density.
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
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``invert_source`` (bool):  [Read-Write] Attribute = 1 - Attribute before applying the operation
- ``mode`` (PCGAttributeNoiseMode):  [Read-Write] Attribute = (Original op Noise), Noise in [NoiseMin, NoiseMax]
- ``noise_max`` (float):  [Read-Write]
- ``noise_min`` (float):  [Read-Write]
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeNoiseSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeNoiseSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write]

<a id="unreal.PCGAttributeNoiseSettings.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGAttributeNoiseMode
```

(PCGAttributeNoiseMode):  [Read-Write] Attribute = (Original op Noise), Noise in [NoiseMin, NoiseMax]

<a id="unreal.PCGAttributeNoiseSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGAttributeNoiseMode) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.noise_min"></a>

#### noise_min

```python
@property
def noise_min() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGAttributeNoiseSettings.noise_min"></a>

#### noise_min

```python
@noise_min.setter
def noise_min(value: float) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.noise_max"></a>

#### noise_max

```python
@property
def noise_max() -> float
```

(float):  [Read-Write]

<a id="unreal.PCGAttributeNoiseSettings.noise_max"></a>

#### noise_max

```python
@noise_max.setter
def noise_max(value: float) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.invert_source"></a>

#### invert_source

```python
@property
def invert_source() -> bool
```

(bool):  [Read-Write] Attribute = 1 - Attribute before applying the operation

<a id="unreal.PCGAttributeNoiseSettings.invert_source"></a>

#### invert_source

```python
@invert_source.setter
def invert_source(value: bool) -> None
```

<a id="unreal.PCGAttributeNoiseSettings.clamp_result"></a>

#### clamp_result

```python
@property
def clamp_result() -> bool
```

(bool):  [Read-Write] Clamp the result between 0 and 1. Always applied if we apply noise to the density.

<a id="unreal.PCGAttributeNoiseSettings.clamp_result"></a>

#### clamp_result

```python
@clamp_result.setter
def clamp_result(value: bool) -> None
```

<a id="unreal.PCGDensityNoiseSettings"></a>