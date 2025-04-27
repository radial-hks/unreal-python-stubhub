## PCGAttributeRemapSettings Objects

```python
class PCGAttributeRemapSettings(PCGMetadataSettingsBase)
```

Remap attribute values from one range to another.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeRemap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_inverse_range`` (bool):  [Read-Write] Allow remapping when Min is larger than Max, e.g. from [0.0, 1.0] -> [1.0, 0.0].
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``clamp_to_unit_range`` (bool):  [Read-Write] If checked, outside values will be clamped between 0 and 1.
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
- ``ignore_values_outside_input_range`` (bool):  [Read-Write] Attribute values outside of the input range will be unaffected by the remapping
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``out_range_max`` (double):  [Read-Write]
- ``out_range_min`` (double):  [Read-Write]
- ``output_data_from_pin`` (Name):  [Read-Write] By default, output is taken from first non-param pin (aka if the second pin is a point data, the output will be this point data). You can change it to any available input pin.
- ``output_target`` (PCGAttributePropertyOutputSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``range_max`` (double):  [Read-Write] If InRangeMin = InRangeMax, then that attribute value is mapped to the average of OutRangeMin and OutRangeMax
- ``range_min`` (double):  [Read-Write] If InRangeMin = InRangeMax, then that attribute value is mapped to the average of OutRangeMin and OutRangeMax
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeRemapSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeRemapSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeRemapSettings.range_min"></a>

#### range_min

```python
@property
def range_min() -> float
```

(double):  [Read-Write] If InRangeMin = InRangeMax, then that attribute value is mapped to the average of OutRangeMin and OutRangeMax

<a id="unreal.PCGAttributeRemapSettings.range_min"></a>

#### range_min

```python
@range_min.setter
def range_min(value: float) -> None
```

<a id="unreal.PCGAttributeRemapSettings.range_max"></a>

#### range_max

```python
@property
def range_max() -> float
```

(double):  [Read-Write] If InRangeMin = InRangeMax, then that attribute value is mapped to the average of OutRangeMin and OutRangeMax

<a id="unreal.PCGAttributeRemapSettings.range_max"></a>

#### range_max

```python
@range_max.setter
def range_max(value: float) -> None
```

<a id="unreal.PCGAttributeRemapSettings.out_range_min"></a>

#### out_range_min

```python
@property
def out_range_min() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGAttributeRemapSettings.out_range_min"></a>

#### out_range_min

```python
@out_range_min.setter
def out_range_min(value: float) -> None
```

<a id="unreal.PCGAttributeRemapSettings.out_range_max"></a>

#### out_range_max

```python
@property
def out_range_max() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGAttributeRemapSettings.out_range_max"></a>

#### out_range_max

```python
@out_range_max.setter
def out_range_max(value: float) -> None
```

<a id="unreal.PCGAttributeRemapSettings.clamp_to_unit_range"></a>

#### clamp_to_unit_range

```python
@property
def clamp_to_unit_range() -> bool
```

(bool):  [Read-Write] If checked, outside values will be clamped between 0 and 1.

<a id="unreal.PCGAttributeRemapSettings.clamp_to_unit_range"></a>

#### clamp_to_unit_range

```python
@clamp_to_unit_range.setter
def clamp_to_unit_range(value: bool) -> None
```

<a id="unreal.PCGAttributeRemapSettings.ignore_values_outside_input_range"></a>

#### ignore_values_outside_input_range

```python
@property
def ignore_values_outside_input_range() -> bool
```

(bool):  [Read-Write] Attribute values outside of the input range will be unaffected by the remapping

<a id="unreal.PCGAttributeRemapSettings.ignore_values_outside_input_range"></a>

#### ignore_values_outside_input_range

```python
@ignore_values_outside_input_range.setter
def ignore_values_outside_input_range(value: bool) -> None
```

<a id="unreal.PCGAttributeRemapSettings.allow_inverse_range"></a>

#### allow_inverse_range

```python
@property
def allow_inverse_range() -> bool
```

(bool):  [Read-Write] Allow remapping when Min is larger than Max, e.g. from [0.0, 1.0] -> [1.0, 0.0].

<a id="unreal.PCGAttributeRemapSettings.allow_inverse_range"></a>

#### allow_inverse_range

```python
@allow_inverse_range.setter
def allow_inverse_range(value: bool) -> None
```

<a id="unreal.PCGAttributeRemoveDuplicatesSettings"></a>