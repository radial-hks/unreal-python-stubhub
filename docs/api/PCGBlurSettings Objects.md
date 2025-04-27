## PCGBlurSettings Objects

```python
class PCGBlurSettings(PCGSettings)
```

Select an attribute on a point data and blur it using the values from neighbors within some distance, center to center, and can be done over multiple iterations.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGBlurElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blur_mode`` (PCGBlurElementMode):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``custom_standard_deviation`` (double):  [Read-Write]
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
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use as a base value. Needs to be numerical.
- ``num_iterations`` (int32):  [Read-Write] Number of iterations to apply the blur.
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write] Attribute where the result will be written.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``search_distance`` (double):  [Read-Write] Radius for search.
- ``seed`` (int32):  [Read-Write]
- ``use_custom_standard_deviation`` (bool):  [Read-Write] By default, the standard deviation will be SearchDistance / 3, so that at search distance from the point it corresponds to 3 std deviation.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGBlurSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use as a base value. Needs to be numerical.

<a id="unreal.PCGBlurSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGBlurSettings.output_target"></a>

#### output_target

```python
@property
def output_target() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write] Attribute where the result will be written.

<a id="unreal.PCGBlurSettings.output_target"></a>

#### output_target

```python
@output_target.setter
def output_target(value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGBlurSettings.num_iterations"></a>

#### num_iterations

```python
@property
def num_iterations() -> int
```

(int32):  [Read-Write] Number of iterations to apply the blur.

<a id="unreal.PCGBlurSettings.num_iterations"></a>

#### num_iterations

```python
@num_iterations.setter
def num_iterations(value: int) -> None
```

<a id="unreal.PCGBlurSettings.search_distance"></a>

#### search_distance

```python
@property
def search_distance() -> float
```

(double):  [Read-Write] Radius for search.

<a id="unreal.PCGBlurSettings.search_distance"></a>

#### search_distance

```python
@search_distance.setter
def search_distance(value: float) -> None
```

<a id="unreal.PCGBlurSettings.blur_mode"></a>

#### blur_mode

```python
@property
def blur_mode() -> PCGBlurElementMode
```

(PCGBlurElementMode):  [Read-Write]

<a id="unreal.PCGBlurSettings.blur_mode"></a>

#### blur_mode

```python
@blur_mode.setter
def blur_mode(value: PCGBlurElementMode) -> None
```

<a id="unreal.PCGBlurSettings.use_custom_standard_deviation"></a>

#### use_custom_standard_deviation

```python
@property
def use_custom_standard_deviation() -> bool
```

(bool):  [Read-Write] By default, the standard deviation will be SearchDistance / 3, so that at search distance from the point it corresponds to 3 std deviation.

<a id="unreal.PCGBlurSettings.use_custom_standard_deviation"></a>

#### use_custom_standard_deviation

```python
@use_custom_standard_deviation.setter
def use_custom_standard_deviation(value: bool) -> None
```

<a id="unreal.PCGBlurSettings.custom_standard_deviation"></a>

#### custom_standard_deviation

```python
@property
def custom_standard_deviation() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGBlurSettings.custom_standard_deviation"></a>

#### custom_standard_deviation

```python
@custom_standard_deviation.setter
def custom_standard_deviation(value: float) -> None
```

<a id="unreal.PCGBooleanSelectSettings"></a>