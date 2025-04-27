## PCGDistanceSettings Objects

```python
class PCGDistanceSettings(PCGSettings)
```

Calculates the distance between two points (inherently a n*n operation)

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDistance.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_name`` (Name):  [Read-Write]
  deprecated: Use OutputAttribute selector instead.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``check_source_against_respective_target`` (bool):  [Read-Write] If this option is on, each source will be tested against its respective target (for a N:N operation). Source and Target num must be the same (or 1).
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
- ``maximum_distance`` (double):  [Read-Write] A maximum distance to search, which is used as an optimization
- ``output_attribute`` (PCGAttributePropertySelector):  [Read-Write] The attribute output for the resulting distance value.
- ``output_distance_vector`` (bool):  [Read-Write] Controls whether the attribute will be a scalar or a vector
- ``output_to_attribute`` (bool):  [Read-Write] Output the distance or distance vector to an attribute.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``set_density`` (bool):  [Read-Write] If true, will also set the density to be 0 - 1 based on MaximumDistance
- ``source_shape`` (PCGDistanceShape):  [Read-Write] What shape is used on the 'source' points
- ``target_shape`` (PCGDistanceShape):  [Read-Write] What shape is used on the 'target' points
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDistanceSettings.output_to_attribute"></a>

#### output_to_attribute

```python
@property
def output_to_attribute() -> bool
```

(bool):  [Read-Write] Output the distance or distance vector to an attribute.

<a id="unreal.PCGDistanceSettings.output_to_attribute"></a>

#### output_to_attribute

```python
@output_to_attribute.setter
def output_to_attribute(value: bool) -> None
```

<a id="unreal.PCGDistanceSettings.output_attribute"></a>

#### output_attribute

```python
@property
def output_attribute() -> PCGAttributePropertySelector
```

(PCGAttributePropertySelector):  [Read-Write] The attribute output for the resulting distance value.

<a id="unreal.PCGDistanceSettings.output_attribute"></a>

#### output_attribute

```python
@output_attribute.setter
def output_attribute(value: PCGAttributePropertySelector) -> None
```

<a id="unreal.PCGDistanceSettings.output_distance_vector"></a>

#### output_distance_vector

```python
@property
def output_distance_vector() -> bool
```

(bool):  [Read-Write] Controls whether the attribute will be a scalar or a vector

<a id="unreal.PCGDistanceSettings.output_distance_vector"></a>

#### output_distance_vector

```python
@output_distance_vector.setter
def output_distance_vector(value: bool) -> None
```

<a id="unreal.PCGDistanceSettings.set_density"></a>

#### set_density

```python
@property
def set_density() -> bool
```

(bool):  [Read-Write] If true, will also set the density to be 0 - 1 based on MaximumDistance

<a id="unreal.PCGDistanceSettings.set_density"></a>

#### set_density

```python
@set_density.setter
def set_density(value: bool) -> None
```

<a id="unreal.PCGDistanceSettings.maximum_distance"></a>

#### maximum_distance

```python
@property
def maximum_distance() -> float
```

(double):  [Read-Write] A maximum distance to search, which is used as an optimization

<a id="unreal.PCGDistanceSettings.maximum_distance"></a>

#### maximum_distance

```python
@maximum_distance.setter
def maximum_distance(value: float) -> None
```

<a id="unreal.PCGDistanceSettings.source_shape"></a>

#### source_shape

```python
@property
def source_shape() -> PCGDistanceShape
```

(PCGDistanceShape):  [Read-Write] What shape is used on the 'source' points

<a id="unreal.PCGDistanceSettings.source_shape"></a>

#### source_shape

```python
@source_shape.setter
def source_shape(value: PCGDistanceShape) -> None
```

<a id="unreal.PCGDistanceSettings.target_shape"></a>

#### target_shape

```python
@property
def target_shape() -> PCGDistanceShape
```

(PCGDistanceShape):  [Read-Write] What shape is used on the 'target' points

<a id="unreal.PCGDistanceSettings.target_shape"></a>

#### target_shape

```python
@target_shape.setter
def target_shape(value: PCGDistanceShape) -> None
```

<a id="unreal.PCGDistanceSettings.check_source_against_respective_target"></a>

#### check_source_against_respective_target

```python
@property
def check_source_against_respective_target() -> bool
```

(bool):  [Read-Write] If this option is on, each source will be tested against its respective target (for a N:N operation). Source and Target num must be the same (or 1).

<a id="unreal.PCGDistanceSettings.check_source_against_respective_target"></a>

#### check_source_against_respective_target

```python
@check_source_against_respective_target.setter
def check_source_against_respective_target(value: bool) -> None
```

<a id="unreal.PCGDistanceSettings.attribute_name"></a>

#### attribute_name

```python
@property
def attribute_name() -> Name
```

(Name):  [Read-Write]
deprecated: Use OutputAttribute selector instead.

<a id="unreal.PCGDistanceSettings.attribute_name"></a>

#### attribute_name

```python
@attribute_name.setter
def attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings"></a>