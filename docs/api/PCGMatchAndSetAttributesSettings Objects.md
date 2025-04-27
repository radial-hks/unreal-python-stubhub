## PCGMatchAndSetAttributesSettings Objects

```python
class PCGMatchAndSetAttributesSettings(PCGSettings)
```

This class creates a PCG node that can match, select by weight or match & select by weight
a 'matching' entry in a provided Attribute Set with multiple entries.
E.g. for a given point, if the point has the same specified attribute as the matching attribute in the attribute set,
then we will copy all the other non-selection attributes to the point.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetAttributes.h

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
- ``find_nearest`` (bool):  [Read-Write] Controls whether the match operation will return the nearest match and not only match on equality.
- ``input_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute from the point data to select & match.
- ``input_weight_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Input weight from the points, assumed to be in the [0, 1] range.
- ``keep_unmatched`` (bool):  [Read-Write] Controls whether points that have no valid match in the attribute set are kept as is (default values) or removed from the output.
- ``match_attribute`` (Name):  [Read-Write] Attribute from the attribute set to match against.
- ``match_attributes`` (bool):  [Read-Write] Controls whether selection of the attribute set values to copy will be done by matching point-to-attribute set (true) or done randomly (false).
- ``max_distance_for_nearest_match`` (PCGMetadataTypesConstantStruct):  [Read-Write] Constant value that establishes the maximum distance an entry can be from its nearest match to be selected
- ``max_distance_input_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``max_distance_mode`` (PCGMatchMaxDistanceMode):  [Read-Write] Controls whether the match operation has a maximum distance on which to reject points that would be too far from the nearest value.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_input_weight_attribute`` (bool):  [Read-Write] Controls whether we will use the attribute provided in the Input Weight Attribute to perform entry selection.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_weight_attribute`` (bool):  [Read-Write] Controls whether we will consider the weights, as determined by the Weight Attribute values on the attribute set.
- ``warn_if_no_match_data`` (bool):  [Read-Write] Controls whether we will emit a warning and return nothing if there is no provided attribute set.
- ``weight_attribute`` (Name):  [Read-Write] Attribute to weight more or less some entries from the attribute set.

<a id="unreal.PCGMatchAndSetAttributesSettings.match_attributes"></a>

#### match_attributes

```python
@property
def match_attributes() -> bool
```

(bool):  [Read-Write] Controls whether selection of the attribute set values to copy will be done by matching point-to-attribute set (true) or done randomly (false).

<a id="unreal.PCGMatchAndSetAttributesSettings.match_attributes"></a>

#### match_attributes

```python
@match_attributes.setter
def match_attributes(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.input_attribute"></a>

#### input_attribute

```python
@property
def input_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute from the point data to select & match.

<a id="unreal.PCGMatchAndSetAttributesSettings.input_attribute"></a>

#### input_attribute

```python
@input_attribute.setter
def input_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.match_attribute"></a>

#### match_attribute

```python
@property
def match_attribute() -> Name
```

(Name):  [Read-Write] Attribute from the attribute set to match against.

<a id="unreal.PCGMatchAndSetAttributesSettings.match_attribute"></a>

#### match_attribute

```python
@match_attribute.setter
def match_attribute(value: Name) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.keep_unmatched"></a>

#### keep_unmatched

```python
@property
def keep_unmatched() -> bool
```

(bool):  [Read-Write] Controls whether points that have no valid match in the attribute set are kept as is (default values) or removed from the output.

<a id="unreal.PCGMatchAndSetAttributesSettings.keep_unmatched"></a>

#### keep_unmatched

```python
@keep_unmatched.setter
def keep_unmatched(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.find_nearest"></a>

#### find_nearest

```python
@property
def find_nearest() -> bool
```

(bool):  [Read-Write] Controls whether the match operation will return the nearest match and not only match on equality.

<a id="unreal.PCGMatchAndSetAttributesSettings.find_nearest"></a>

#### find_nearest

```python
@find_nearest.setter
def find_nearest(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_mode"></a>

#### max_distance_mode

```python
@property
def max_distance_mode() -> PCGMatchMaxDistanceMode
```

(PCGMatchMaxDistanceMode):  [Read-Write] Controls whether the match operation has a maximum distance on which to reject points that would be too far from the nearest value.

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_mode"></a>

#### max_distance_mode

```python
@max_distance_mode.setter
def max_distance_mode(value: PCGMatchMaxDistanceMode) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_for_nearest_match"></a>

#### max_distance_for_nearest_match

```python
@property
def max_distance_for_nearest_match() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write] Constant value that establishes the maximum distance an entry can be from its nearest match to be selected

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_for_nearest_match"></a>

#### max_distance_for_nearest_match

```python
@max_distance_for_nearest_match.setter
def max_distance_for_nearest_match(
        value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_input_attribute"></a>

#### max_distance_input_attribute

```python
@property
def max_distance_input_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGMatchAndSetAttributesSettings.max_distance_input_attribute"></a>

#### max_distance_input_attribute

```python
@max_distance_input_attribute.setter
def max_distance_input_attribute(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.use_input_weight_attribute"></a>

#### use_input_weight_attribute

```python
@property
def use_input_weight_attribute() -> bool
```

(bool):  [Read-Write] Controls whether we will use the attribute provided in the Input Weight Attribute to perform entry selection.

<a id="unreal.PCGMatchAndSetAttributesSettings.use_input_weight_attribute"></a>

#### use_input_weight_attribute

```python
@use_input_weight_attribute.setter
def use_input_weight_attribute(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.input_weight_attribute"></a>

#### input_weight_attribute

```python
@property
def input_weight_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Input weight from the points, assumed to be in the [0, 1] range.

<a id="unreal.PCGMatchAndSetAttributesSettings.input_weight_attribute"></a>

#### input_weight_attribute

```python
@input_weight_attribute.setter
def input_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.use_weight_attribute"></a>

#### use_weight_attribute

```python
@property
def use_weight_attribute() -> bool
```

(bool):  [Read-Write] Controls whether we will consider the weights, as determined by the Weight Attribute values on the attribute set.

<a id="unreal.PCGMatchAndSetAttributesSettings.use_weight_attribute"></a>

#### use_weight_attribute

```python
@use_weight_attribute.setter
def use_weight_attribute(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.weight_attribute"></a>

#### weight_attribute

```python
@property
def weight_attribute() -> Name
```

(Name):  [Read-Write] Attribute to weight more or less some entries from the attribute set.

<a id="unreal.PCGMatchAndSetAttributesSettings.weight_attribute"></a>

#### weight_attribute

```python
@weight_attribute.setter
def weight_attribute(value: Name) -> None
```

<a id="unreal.PCGMatchAndSetAttributesSettings.warn_if_no_match_data"></a>

#### warn_if_no_match_data

```python
@property
def warn_if_no_match_data() -> bool
```

(bool):  [Read-Write] Controls whether we will emit a warning and return nothing if there is no provided attribute set.

<a id="unreal.PCGMatchAndSetAttributesSettings.warn_if_no_match_data"></a>

#### warn_if_no_match_data

```python
@warn_if_no_match_data.setter
def warn_if_no_match_data(value: bool) -> None
```

<a id="unreal.PCGMergeSettings"></a>