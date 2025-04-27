## PCGCreateSplineSettings Objects

```python
class PCGCreateSplineSettings(PCGSettings)
```

PCG node that creates a spline presentation from the input points data, with optional tangents

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCreateSpline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``apply_custom_tangents`` (bool):  [Read-Write] Allow to specify custom tangents for each point, as an attribute. Can't be set if the spline is linear.
- ``arrive_tangent_attribute`` (Name):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``closed_loop`` (bool):  [Read-Write]
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
- ``leave_tangent_attribute`` (Name):  [Read-Write]
- ``linear`` (bool):  [Read-Write] Controls whether the segment between control points is a curve (when false) or a straight line (when true).
- ``mode`` (PCGCreateSplineMode):  [Read-Write]
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGCreateSplineSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGCreateSplineMode
```

(PCGCreateSplineMode):  [Read-Write]

<a id="unreal.PCGCreateSplineSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGCreateSplineMode) -> None
```

<a id="unreal.PCGCreateSplineSettings.closed_loop"></a>

#### closed_loop

```python
@property
def closed_loop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGCreateSplineSettings.closed_loop"></a>

#### closed_loop

```python
@closed_loop.setter
def closed_loop(value: bool) -> None
```

<a id="unreal.PCGCreateSplineSettings.linear"></a>

#### linear

```python
@property
def linear() -> bool
```

(bool):  [Read-Write] Controls whether the segment between control points is a curve (when false) or a straight line (when true).

<a id="unreal.PCGCreateSplineSettings.linear"></a>

#### linear

```python
@linear.setter
def linear(value: bool) -> None
```

<a id="unreal.PCGCreateSplineSettings.apply_custom_tangents"></a>

#### apply_custom_tangents

```python
@property
def apply_custom_tangents() -> bool
```

(bool):  [Read-Write] Allow to specify custom tangents for each point, as an attribute. Can't be set if the spline is linear.

<a id="unreal.PCGCreateSplineSettings.apply_custom_tangents"></a>

#### apply_custom_tangents

```python
@apply_custom_tangents.setter
def apply_custom_tangents(value: bool) -> None
```

<a id="unreal.PCGCreateSplineSettings.arrive_tangent_attribute"></a>

#### arrive_tangent_attribute

```python
@property
def arrive_tangent_attribute() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGCreateSplineSettings.arrive_tangent_attribute"></a>

#### arrive_tangent_attribute

```python
@arrive_tangent_attribute.setter
def arrive_tangent_attribute(value: Name) -> None
```

<a id="unreal.PCGCreateSplineSettings.leave_tangent_attribute"></a>

#### leave_tangent_attribute

```python
@property
def leave_tangent_attribute() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGCreateSplineSettings.leave_tangent_attribute"></a>

#### leave_tangent_attribute

```python
@leave_tangent_attribute.setter
def leave_tangent_attribute(value: Name) -> None
```

<a id="unreal.PCGCreateSplineSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGCreateSplineSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGCreateSurfaceFromSplineSettings"></a>