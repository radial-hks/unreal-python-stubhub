## PCGAttributeFilteringRangeSettings Objects

```python
class PCGAttributeFilteringRangeSettings(PCGSettings)
```

Attribute filter on range that allows to do "A op B" type filtering, where A is the input spatial data or Attribute set,
and B is either a constant, another spatial data (if input is a spatial data), an Attribute set (in filter) or the input itself.
The filtering can be done either on properties or attributes.
Some examples (that might not make sense, but are valid):
- Threshold on property by constant (A.Density in [0.2, 0.5])
- Threshold on attribute by constant (A.aaa in [0.4, 0.6])
- Threshold on property by metadata attribute(A.density in [B.bbmin, B.bbmax])
- Threshold on property by property(A.density in [B.position.x, B.steepness])
- Threshold on attribute by metadata attribute(A.aaa in [B.bbmin, B.bbmax])
- Threshold on attribute by property(A.aaa in [B.position, B.scale])

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeFilter.h

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
- ``max_threshold`` (PCGAttributeFilterThresholdSettings):  [Read-Write]
- ``min_threshold`` (PCGAttributeFilterThresholdSettings):  [Read-Write] Threshold property/attribute/constant related properties
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``target_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Target property/attribute related properties
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``warn_on_data_missing_attribute`` (bool):  [Read-Write] Controls whether the node will emit a warning when the input data or the filter data doesn't have the attribute to filter on.

<a id="unreal.PCGAttributeFilteringRangeSettings.target_attribute"></a>

#### target_attribute

```python
@property
def target_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Target property/attribute related properties

<a id="unreal.PCGAttributeFilteringRangeSettings.target_attribute"></a>

#### target_attribute

```python
@target_attribute.setter
def target_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeFilteringRangeSettings.min_threshold"></a>

#### min_threshold

```python
@property
def min_threshold() -> PCGAttributeFilterThresholdSettings
```

(PCGAttributeFilterThresholdSettings):  [Read-Write] Threshold property/attribute/constant related properties

<a id="unreal.PCGAttributeFilteringRangeSettings.min_threshold"></a>

#### min_threshold

```python
@min_threshold.setter
def min_threshold(value: PCGAttributeFilterThresholdSettings) -> None
```

<a id="unreal.PCGAttributeFilteringRangeSettings.max_threshold"></a>

#### max_threshold

```python
@property
def max_threshold() -> PCGAttributeFilterThresholdSettings
```

(PCGAttributeFilterThresholdSettings):  [Read-Write]

<a id="unreal.PCGAttributeFilteringRangeSettings.max_threshold"></a>

#### max_threshold

```python
@max_threshold.setter
def max_threshold(value: PCGAttributeFilterThresholdSettings) -> None
```

<a id="unreal.PCGAttributeFilteringRangeSettings.warn_on_data_missing_attribute"></a>

#### warn_on_data_missing_attribute

```python
@property
def warn_on_data_missing_attribute() -> bool
```

(bool):  [Read-Write] Controls whether the node will emit a warning when the input data or the filter data doesn't have the attribute to filter on.

<a id="unreal.PCGAttributeFilteringRangeSettings.warn_on_data_missing_attribute"></a>

#### warn_on_data_missing_attribute

```python
@warn_on_data_missing_attribute.setter
def warn_on_data_missing_attribute(value: bool) -> None
```

<a id="unreal.PCGPointFilterRangeSettings"></a>