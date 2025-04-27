## PCGSpawnSplineSettings Objects

```python
class PCGSpawnSplineSettings(PCGSettings)
```

Spawn a spline component from a spline data.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSpawnSpline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``component_reference_attribute_name`` (Name):  [Read-Write] Can output the spawned component reference in an attribute.
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
- ``output_spline_component_reference`` (bool):  [Read-Write]
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_override_descriptions`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Overrides to apply on the spawned component.
- ``seed`` (int32):  [Read-Write]
- ``spawn_component_from_attribute`` (bool):  [Read-Write]
- ``spawn_component_from_attribute_name`` (PCGAttributePropertyInputSelector):  [Read-Write] If the class of the component to spawn is coming from an attribute.
- ``spline_component`` (type(Class)):  [Read-Write] Class of the component to spawn, must be a subclass of Spline Component.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSpawnSplineSettings.spline_component"></a>

#### spline_component

```python
@property
def spline_component() -> Class
```

(type(Class)):  [Read-Write] Class of the component to spawn, must be a subclass of Spline Component.

<a id="unreal.PCGSpawnSplineSettings.spline_component"></a>

#### spline_component

```python
@spline_component.setter
def spline_component(value: Class) -> None
```

<a id="unreal.PCGSpawnSplineSettings.spawn_component_from_attribute"></a>

#### spawn_component_from_attribute

```python
@property
def spawn_component_from_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSpawnSplineSettings.spawn_component_from_attribute"></a>

#### spawn_component_from_attribute

```python
@spawn_component_from_attribute.setter
def spawn_component_from_attribute(value: bool) -> None
```

<a id="unreal.PCGSpawnSplineSettings.spawn_component_from_attribute_name"></a>

#### spawn_component_from_attribute_name

```python
@property
def spawn_component_from_attribute_name() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] If the class of the component to spawn is coming from an attribute.

<a id="unreal.PCGSpawnSplineSettings.spawn_component_from_attribute_name"></a>

#### spawn_component_from_attribute_name

```python
@spawn_component_from_attribute_name.setter
def spawn_component_from_attribute_name(
        value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSpawnSplineSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after spline creation. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGSpawnSplineSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGSpawnSplineSettings.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property
def property_override_descriptions(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Overrides to apply on the spawned component.

<a id="unreal.PCGSpawnSplineSettings.property_override_descriptions"></a>

#### property_override_descriptions

```python
@property_override_descriptions.setter
def property_override_descriptions(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGSpawnSplineSettings.output_spline_component_reference"></a>

#### output_spline_component_reference

```python
@property
def output_spline_component_reference() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSpawnSplineSettings.output_spline_component_reference"></a>

#### output_spline_component_reference

```python
@output_spline_component_reference.setter
def output_spline_component_reference(value: bool) -> None
```

<a id="unreal.PCGSpawnSplineSettings.component_reference_attribute_name"></a>

#### component_reference_attribute_name

```python
@property
def component_reference_attribute_name() -> Name
```

(Name):  [Read-Write] Can output the spawned component reference in an attribute.

<a id="unreal.PCGSpawnSplineSettings.component_reference_attribute_name"></a>

#### component_reference_attribute_name

```python
@component_reference_attribute_name.setter
def component_reference_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSpawnSplineMeshSettings"></a>