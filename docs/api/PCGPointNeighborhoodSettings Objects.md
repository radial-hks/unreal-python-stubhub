## PCGPointNeighborhoodSettings Objects

```python
class PCGPointNeighborhoodSettings(PCGSettings)
```

Computes quantities from nearby neighbor points, such as average density, color, and position.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPointNeighborhood.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``average_position_attribute`` (Name):  [Read-Write] The output attribute name to write the average positions, if not "None".
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``distance_attribute`` (Name):  [Read-Write] The output attribute name to write the non-normalized distance, if not "None".
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``search_distance`` (double):  [Read-Write]
- ``seed`` (int32):  [Read-Write]
- ``set_average_color`` (bool):  [Read-Write] Writes the target color to the point color if true, otherwise keeps the source color.
- ``set_average_position`` (bool):  [Read-Write] Writes the average position to the point transform.
- ``set_average_position_to_attribute`` (bool):  [Read-Write] Allows the average position to be output into a user-generated attribute.
- ``set_density`` (PCGPointNeighborhoodDensityMode):  [Read-Write] Writes either the normalized distance or the average density to the point density.
- ``set_distance_to_attribute`` (bool):  [Read-Write] Allows the non-normalized distance to be output into a user-generated attribute.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``weighted_average`` (bool):  [Read-Write] Takes the bounds into account when projecting points.

<a id="unreal.PCGPointNeighborhoodSettings.search_distance"></a>

#### search_distance

```python
@property
def search_distance() -> float
```

(double):  [Read-Write]

<a id="unreal.PCGPointNeighborhoodSettings.search_distance"></a>

#### search_distance

```python
@search_distance.setter
def search_distance(value: float) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.set_distance_to_attribute"></a>

#### set_distance_to_attribute

```python
@property
def set_distance_to_attribute() -> bool
```

(bool):  [Read-Write] Allows the non-normalized distance to be output into a user-generated attribute.

<a id="unreal.PCGPointNeighborhoodSettings.set_distance_to_attribute"></a>

#### set_distance_to_attribute

```python
@set_distance_to_attribute.setter
def set_distance_to_attribute(value: bool) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.distance_attribute"></a>

#### distance_attribute

```python
@property
def distance_attribute() -> Name
```

(Name):  [Read-Write] The output attribute name to write the non-normalized distance, if not "None".

<a id="unreal.PCGPointNeighborhoodSettings.distance_attribute"></a>

#### distance_attribute

```python
@distance_attribute.setter
def distance_attribute(value: Name) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.set_average_position_to_attribute"></a>

#### set_average_position_to_attribute

```python
@property
def set_average_position_to_attribute() -> bool
```

(bool):  [Read-Write] Allows the average position to be output into a user-generated attribute.

<a id="unreal.PCGPointNeighborhoodSettings.set_average_position_to_attribute"></a>

#### set_average_position_to_attribute

```python
@set_average_position_to_attribute.setter
def set_average_position_to_attribute(value: bool) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.average_position_attribute"></a>

#### average_position_attribute

```python
@property
def average_position_attribute() -> Name
```

(Name):  [Read-Write] The output attribute name to write the average positions, if not "None".

<a id="unreal.PCGPointNeighborhoodSettings.average_position_attribute"></a>

#### average_position_attribute

```python
@average_position_attribute.setter
def average_position_attribute(value: Name) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.set_density"></a>

#### set_density

```python
@property
def set_density() -> PCGPointNeighborhoodDensityMode
```

(PCGPointNeighborhoodDensityMode):  [Read-Write] Writes either the normalized distance or the average density to the point density.

<a id="unreal.PCGPointNeighborhoodSettings.set_density"></a>

#### set_density

```python
@set_density.setter
def set_density(value: PCGPointNeighborhoodDensityMode) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.set_average_position"></a>

#### set_average_position

```python
@property
def set_average_position() -> bool
```

(bool):  [Read-Write] Writes the average position to the point transform.

<a id="unreal.PCGPointNeighborhoodSettings.set_average_position"></a>

#### set_average_position

```python
@set_average_position.setter
def set_average_position(value: bool) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.set_average_color"></a>

#### set_average_color

```python
@property
def set_average_color() -> bool
```

(bool):  [Read-Write] Writes the target color to the point color if true, otherwise keeps the source color.

<a id="unreal.PCGPointNeighborhoodSettings.set_average_color"></a>

#### set_average_color

```python
@set_average_color.setter
def set_average_color(value: bool) -> None
```

<a id="unreal.PCGPointNeighborhoodSettings.weighted_average"></a>

#### weighted_average

```python
@property
def weighted_average() -> bool
```

(bool):  [Read-Write] Takes the bounds into account when projecting points.

<a id="unreal.PCGPointNeighborhoodSettings.weighted_average"></a>

#### weighted_average

```python
@weighted_average.setter
def weighted_average(value: bool) -> None
```

<a id="unreal.PCGManagedDebugStringMessageKey"></a>