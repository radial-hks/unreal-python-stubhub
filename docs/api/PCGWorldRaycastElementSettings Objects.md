## PCGWorldRaycastElementSettings Objects

```python
class PCGWorldRaycastElementSettings(PCGSettings)
```

Casts rays from provided points along a given direction and transform points to the impact point.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGWorldRaycast.h

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
- ``end_point_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray terminal point.
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``keep_original_point_on_miss`` (bool):  [Read-Write] Will keep the original points at their location if the raycast misses or if the hit result is out of bounds.
- ``origin_input_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray origin.
- ``override_ray_directions`` (bool):  [Read-Write] Use a selected attribute as the ray direction.
- ``override_ray_lengths`` (bool):  [Read-Write] Use a selected attribute as the ray length.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``ray_direction`` (Vector):  [Read-Write] A ray direction that will be used for all raycasts.
- ``ray_direction_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray direction.
- ``ray_length`` (double):  [Read-Write] A ray length that will be used for all raycasts.
- ``ray_length_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray length.
- ``raycast_mode`` (PCGWorldRaycastMode):  [Read-Write] Determines how the ray's direction and distance will be calculated.
- ``seed`` (int32):  [Read-Write]
- ``unbounded`` (bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``world_query_params`` (PCGWorldRaycastQueryParams):  [Read-Write] World ray trace parameters.

<a id="unreal.PCGWorldRaycastElementSettings.raycast_mode"></a>

#### raycast_mode

```python
@property
def raycast_mode() -> PCGWorldRaycastMode
```

(PCGWorldRaycastMode):  [Read-Write] Determines how the ray's direction and distance will be calculated.

<a id="unreal.PCGWorldRaycastElementSettings.raycast_mode"></a>

#### raycast_mode

```python
@raycast_mode.setter
def raycast_mode(value: PCGWorldRaycastMode) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.origin_input_attribute"></a>

#### origin_input_attribute

```python
@property
def origin_input_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray origin.

<a id="unreal.PCGWorldRaycastElementSettings.origin_input_attribute"></a>

#### origin_input_attribute

```python
@origin_input_attribute.setter
def origin_input_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.override_ray_directions"></a>

#### override_ray_directions

```python
@property
def override_ray_directions() -> bool
```

(bool):  [Read-Write] Use a selected attribute as the ray direction.

<a id="unreal.PCGWorldRaycastElementSettings.override_ray_directions"></a>

#### override_ray_directions

```python
@override_ray_directions.setter
def override_ray_directions(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.ray_direction"></a>

#### ray_direction

```python
@property
def ray_direction() -> Vector
```

(Vector):  [Read-Write] A ray direction that will be used for all raycasts.

<a id="unreal.PCGWorldRaycastElementSettings.ray_direction"></a>

#### ray_direction

```python
@ray_direction.setter
def ray_direction(value: Vector) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.ray_direction_attribute"></a>

#### ray_direction_attribute

```python
@property
def ray_direction_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray direction.

<a id="unreal.PCGWorldRaycastElementSettings.ray_direction_attribute"></a>

#### ray_direction_attribute

```python
@ray_direction_attribute.setter
def ray_direction_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.end_point_attribute"></a>

#### end_point_attribute

```python
@property
def end_point_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray terminal point.

<a id="unreal.PCGWorldRaycastElementSettings.end_point_attribute"></a>

#### end_point_attribute

```python
@end_point_attribute.setter
def end_point_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.override_ray_lengths"></a>

#### override_ray_lengths

```python
@property
def override_ray_lengths() -> bool
```

(bool):  [Read-Write] Use a selected attribute as the ray length.

<a id="unreal.PCGWorldRaycastElementSettings.override_ray_lengths"></a>

#### override_ray_lengths

```python
@override_ray_lengths.setter
def override_ray_lengths(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.ray_length"></a>

#### ray_length

```python
@property
def ray_length() -> float
```

(double):  [Read-Write] A ray length that will be used for all raycasts.

<a id="unreal.PCGWorldRaycastElementSettings.ray_length"></a>

#### ray_length

```python
@ray_length.setter
def ray_length(value: float) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.ray_length_attribute"></a>

#### ray_length_attribute

```python
@property
def ray_length_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The selected attribute determines the ray length.

<a id="unreal.PCGWorldRaycastElementSettings.ray_length_attribute"></a>

#### ray_length_attribute

```python
@ray_length_attribute.setter
def ray_length_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.world_query_params"></a>

#### world_query_params

```python
@property
def world_query_params() -> PCGWorldRaycastQueryParams
```

(PCGWorldRaycastQueryParams):  [Read-Write] World ray trace parameters.

<a id="unreal.PCGWorldRaycastElementSettings.world_query_params"></a>

#### world_query_params

```python
@world_query_params.setter
def world_query_params(value: PCGWorldRaycastQueryParams) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.keep_original_point_on_miss"></a>

#### keep_original_point_on_miss

```python
@property
def keep_original_point_on_miss() -> bool
```

(bool):  [Read-Write] Will keep the original points at their location if the raycast misses or if the hit result is out of bounds.

<a id="unreal.PCGWorldRaycastElementSettings.keep_original_point_on_miss"></a>

#### keep_original_point_on_miss

```python
@keep_original_point_on_miss.setter
def keep_original_point_on_miss(value: bool) -> None
```

<a id="unreal.PCGWorldRaycastElementSettings.unbounded"></a>

#### unbounded

```python
@property
def unbounded() -> bool
```

(bool):  [Read-Write] If no Bounding Shape input is provided, the actor bounds are used to limit the sample generation domain.

<a id="unreal.PCGWorldRaycastElementSettings.unbounded"></a>

#### unbounded

```python
@unbounded.setter
def unbounded(value: bool) -> None
```

<a id="unreal.PCGGridLinkageSettings"></a>