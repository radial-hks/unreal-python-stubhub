## PCGAttributeFilteringSettings Objects

```python
class PCGAttributeFilteringSettings(PCGSettings)
```

Attribute filter that allows to do "A op B" type filtering, where A is the input spatial data or Attribute set,
and B is either a constant, another spatial data (if input is a spatial data), an Attribute set (in filter) or the input itself.
The filtering can be done either on properties or attributes.
Some examples:
- Threshold on property by constant (A.Density > 0.5)
- Threshold on attribute by constant (A.aaa != "bob")
- Threshold on property by metadata attribute(A.density >= B.bbb)
- Threshold on property by property(A.density <= B.steepness)
- Threshold on attribute by metadata attribute(A.aaa < B.bbb)
- Threshold on attribute by property(A.aaa == B.color)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_types`` (PCGMetadataTypesConstantStruct):  [Read-Write]
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
- ``operator`` (PCGAttributeFilterOperator):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``target_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Target property/attribute related properties
- ``threshold_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``use_constant_threshold`` (bool):  [Read-Write] Threshold property/attribute/constant related properties
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_spatial_query`` (bool):  [Read-Write] If the threshold data is Point data, it will sample input points in threshold data. Always true with Spatial data.
- ``warn_on_data_missing_attribute`` (bool):  [Read-Write] Controls whether the node will emit a warning when the input data or the filter data doesn't have the attribute to filter on.

<a id="unreal.PCGAttributeFilteringSettings.operator"></a>

#### operator

```python
@property
def operator() -> PCGAttributeFilterOperator
```

(PCGAttributeFilterOperator):  [Read-Write]

<a id="unreal.PCGAttributeFilteringSettings.operator"></a>

#### operator

```python
@operator.setter
def operator(value: PCGAttributeFilterOperator) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.target_attribute"></a>

#### target_attribute

```python
@property
def target_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Target property/attribute related properties

<a id="unreal.PCGAttributeFilteringSettings.target_attribute"></a>

#### target_attribute

```python
@target_attribute.setter
def target_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.use_constant_threshold"></a>

#### use_constant_threshold

```python
@property
def use_constant_threshold() -> bool
```

(bool):  [Read-Write] Threshold property/attribute/constant related properties

<a id="unreal.PCGAttributeFilteringSettings.use_constant_threshold"></a>

#### use_constant_threshold

```python
@use_constant_threshold.setter
def use_constant_threshold(value: bool) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.threshold_attribute"></a>

#### threshold_attribute

```python
@property
def threshold_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeFilteringSettings.threshold_attribute"></a>

#### threshold_attribute

```python
@threshold_attribute.setter
def threshold_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.use_spatial_query"></a>

#### use_spatial_query

```python
@property
def use_spatial_query() -> bool
```

(bool):  [Read-Write] If the threshold data is Point data, it will sample input points in threshold data. Always true with Spatial data.

<a id="unreal.PCGAttributeFilteringSettings.use_spatial_query"></a>

#### use_spatial_query

```python
@use_spatial_query.setter
def use_spatial_query(value: bool) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.attribute_types"></a>

#### attribute_types

```python
@property
def attribute_types() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGAttributeFilteringSettings.attribute_types"></a>

#### attribute_types

```python
@attribute_types.setter
def attribute_types(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGAttributeFilteringSettings.warn_on_data_missing_attribute"></a>

#### warn_on_data_missing_attribute

```python
@property
def warn_on_data_missing_attribute() -> bool
```

(bool):  [Read-Write] Controls whether the node will emit a warning when the input data or the filter data doesn't have the attribute to filter on.

<a id="unreal.PCGAttributeFilteringSettings.warn_on_data_missing_attribute"></a>

#### warn_on_data_missing_attribute

```python
@warn_on_data_missing_attribute.setter
def warn_on_data_missing_attribute(value: bool) -> None
```

<a id="unreal.PCGPointFilterSettings"></a>