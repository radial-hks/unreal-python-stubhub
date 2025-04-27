## PCGVisualizeAttributeSettings Objects

```python
class PCGVisualizeAttributeSettings(PCGSettings)
```

Visualizes a selected attribute on screen at each point's transform.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGVisualizeAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_source`` (PCGAttributePropertyInputSelector):  [Read-Write] This attribute will be have it's value printed in proximity to each input point's transform.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``color`` (Color):  [Read-Write] The color of the on displayed value.
- ``custom_prefix_string`` (str):  [Read-Write] A custom added prefix to which the attribute value will be appended.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``duration`` (double):  [Read-Write] The duration (in seconds) of the displayed value.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``local_offset`` (Vector):  [Read-Write] A local offset from the point's location to draw the text.
- ``point_limit`` (int32):  [Read-Write] The limit of points to draw debug messages.
- ``prefix_with_attribute_name`` (bool):  [Read-Write] Prefix the printed value with the attribute's name.
- ``prefix_with_index`` (bool):  [Read-Write] Prefix the printed value with the point's index.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``visualize_enabled`` (bool):  [Read-Write] The visualizer is enabled. Useful for dynamically overriding.

<a id="unreal.PCGVisualizeAttributeSettings.attribute_source"></a>

#### attribute_source

```python
@property
def attribute_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] This attribute will be have it's value printed in proximity to each input point's transform.

<a id="unreal.PCGVisualizeAttributeSettings.attribute_source"></a>

#### attribute_source

```python
@attribute_source.setter
def attribute_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.custom_prefix_string"></a>

#### custom_prefix_string

```python
@property
def custom_prefix_string() -> str
```

(str):  [Read-Write] A custom added prefix to which the attribute value will be appended.

<a id="unreal.PCGVisualizeAttributeSettings.custom_prefix_string"></a>

#### custom_prefix_string

```python
@custom_prefix_string.setter
def custom_prefix_string(value: str) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.prefix_with_index"></a>

#### prefix_with_index

```python
@property
def prefix_with_index() -> bool
```

(bool):  [Read-Write] Prefix the printed value with the point's index.

<a id="unreal.PCGVisualizeAttributeSettings.prefix_with_index"></a>

#### prefix_with_index

```python
@prefix_with_index.setter
def prefix_with_index(value: bool) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.prefix_with_attribute_name"></a>

#### prefix_with_attribute_name

```python
@property
def prefix_with_attribute_name() -> bool
```

(bool):  [Read-Write] Prefix the printed value with the attribute's name.

<a id="unreal.PCGVisualizeAttributeSettings.prefix_with_attribute_name"></a>

#### prefix_with_attribute_name

```python
@prefix_with_attribute_name.setter
def prefix_with_attribute_name(value: bool) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.local_offset"></a>

#### local_offset

```python
@property
def local_offset() -> Vector
```

(Vector):  [Read-Write] A local offset from the point's location to draw the text.

<a id="unreal.PCGVisualizeAttributeSettings.local_offset"></a>

#### local_offset

```python
@local_offset.setter
def local_offset(value: Vector) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write] The color of the on displayed value.

<a id="unreal.PCGVisualizeAttributeSettings.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(double):  [Read-Write] The duration (in seconds) of the displayed value.

<a id="unreal.PCGVisualizeAttributeSettings.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.point_limit"></a>

#### point_limit

```python
@property
def point_limit() -> int
```

(int32):  [Read-Write] The limit of points to draw debug messages.

<a id="unreal.PCGVisualizeAttributeSettings.point_limit"></a>

#### point_limit

```python
@point_limit.setter
def point_limit(value: int) -> None
```

<a id="unreal.PCGVisualizeAttributeSettings.visualize_enabled"></a>

#### visualize_enabled

```python
@property
def visualize_enabled() -> bool
```

(bool):  [Read-Write] The visualizer is enabled. Useful for dynamically overriding.

<a id="unreal.PCGVisualizeAttributeSettings.visualize_enabled"></a>

#### visualize_enabled

```python
@visualize_enabled.setter
def visualize_enabled(value: bool) -> None
```

<a id="unreal.PCGWaitLandscapeReadySettings"></a>