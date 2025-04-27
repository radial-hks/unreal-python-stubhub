## PCGAttractSettings Objects

```python
class PCGAttractSettings(PCGSettings)
```

Attracts points (interpolates) from the source towards points from the target.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttractElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attractor_index_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Index attribute on the source that maps a point to a point from the target.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``distance`` (double):  [Read-Write] Will be used to determine which points to attract.
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``mode`` (PCGAttractMode):  [Read-Write] Controls the criteria used for the attract operation.
- ``output_attract_index`` (bool):  [Read-Write]
- ``output_attract_index_attribute`` (PCGAttributePropertyOutputNoSourceSelector):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``remove_unattracted_points`` (bool):  [Read-Write] Can optionally remove points that weren't attracted to points on the target. Will have no effect when the source is the target.
- ``seed`` (int32):  [Read-Write]
- ``source_and_target_attribute_mapping`` (Map[PCGAttributePropertyInputSelector, PCGAttributePropertyInputSelector]):  [Read-Write]
- ``source_weight_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] This attribute will determine the weight of the fusion result for the source point. It will be normalized to the range of [0..1].
- ``target_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The target attribute used when attracted by attribute value.
- ``target_weight_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] This attribute will determine the weight of the fusion result for the target point. It will be normalized to the range of [0..1].
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_source_weight`` (bool):  [Read-Write]
- ``use_target_weight`` (bool):  [Read-Write]
- ``weight`` (double):  [Read-Write]

<a id="unreal.PCGAttractSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGAttractMode
```

(PCGAttractMode):  [Read-Write] Controls the criteria used for the attract operation.

<a id="unreal.PCGAttractSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGAttractMode) -> None
```

<a id="unreal.PCGAttractSettings.attractor_index_attribute"></a>

#### attractor_index_attribute

```python
@property
def attractor_index_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Index attribute on the source that maps a point to a point from the target.

<a id="unreal.PCGAttractSettings.attractor_index_attribute"></a>

#### attractor_index_attribute

```python
@attractor_index_attribute.setter
def attractor_index_attribute(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttractSettings.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(double):  [Read-Write] Will be used to determine which points to attract.

<a id="unreal.PCGAttractSettings.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.PCGAttractSettings.remove_unattracted_points"></a>

#### remove_unattracted_points

```python
@property
def remove_unattracted_points() -> bool
```

(bool):  [Read-Write] Can optionally remove points that weren't attracted to points on the target. Will have no effect when the source is the target.

<a id="unreal.PCGAttractSettings.remove_unattracted_points"></a>

#### remove_unattracted_points

```python
@remove_unattracted_points.setter
def remove_unattracted_points(value: bool) -> None
```

<a id="unreal.PCGAttractSettings.target_attribute"></a>

#### target_attribute

```python
@property
def target_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The target attribute used when attracted by attribute value.

<a id="unreal.PCGAttractSettings.target_attribute"></a>

#### target_attribute

```python
@target_attribute.setter
def target_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttractSettings.use_source_weight"></a>

#### use_source_weight

```python
@property
def use_source_weight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAttractSettings.use_source_weight"></a>

#### use_source_weight

```python
@use_source_weight.setter
def use_source_weight(value: bool) -> None
```

<a id="unreal.PCGAttractSettings.source_weight_attribute"></a>

#### source_weight_attribute

```python
@property
def source_weight_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] This attribute will determine the weight of the fusion result for the source point. It will be normalized to the range of [0..1].

<a id="unreal.PCGAttractSettings.source_weight_attribute"></a>

#### source_weight_attribute

```python
@source_weight_attribute.setter
def source_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttractSettings.use_target_weight"></a>

#### use_target_weight

```python
@property
def use_target_weight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAttractSettings.use_target_weight"></a>

#### use_target_weight

```python
@use_target_weight.setter
def use_target_weight(value: bool) -> None
```

<a id="unreal.PCGAttractSettings.target_weight_attribute"></a>

#### target_weight_attribute

```python
@property
def target_weight_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] This attribute will determine the weight of the fusion result for the target point. It will be normalized to the range of [0..1].

<a id="unreal.PCGAttractSettings.target_weight_attribute"></a>

#### target_weight_attribute

```python
@target_weight_attribute.setter
def target_weight_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttractSettings.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGAttractSettings.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.PCGAttractSettings.source_and_target_attribute_mapping"></a>

#### source_and_target_attribute_mapping

```python
@property
def source_and_target_attribute_mapping(
) -> Map[PCGAttributePropertyInputSelector, PCGAttributePropertyInputSelector]
```

(Map[PCGAttributePropertyInputSelector, PCGAttributePropertyInputSelector]):  [Read-Write]

<a id="unreal.PCGAttractSettings.source_and_target_attribute_mapping"></a>

#### source_and_target_attribute_mapping

```python
@source_and_target_attribute_mapping.setter
def source_and_target_attribute_mapping(
    value: Map[PCGAttributePropertyInputSelector,
               PCGAttributePropertyInputSelector]
) -> None
```

<a id="unreal.PCGAttractSettings.output_attract_index"></a>

#### output_attract_index

```python
@property
def output_attract_index() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAttractSettings.output_attract_index"></a>

#### output_attract_index

```python
@output_attract_index.setter
def output_attract_index(value: bool) -> None
```

<a id="unreal.PCGAttractSettings.output_attract_index_attribute"></a>

#### output_attract_index_attribute

```python
@property
def output_attract_index_attribute(
) -> PCGAttributePropertyOutputNoSourceSelector
```

(PCGAttributePropertyOutputNoSourceSelector):  [Read-Write]

<a id="unreal.PCGAttractSettings.output_attract_index_attribute"></a>

#### output_attract_index_attribute

```python
@output_attract_index_attribute.setter
def output_attract_index_attribute(
        value: PCGAttributePropertyOutputNoSourceSelector) -> None
```

<a id="unreal.PCGAttributeCastSettings"></a>