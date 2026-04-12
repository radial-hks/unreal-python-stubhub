## PCGBlueprintSettings Objects

```python
class PCGBlueprintSettings(PCGSettings)
```

PCGBlueprint Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGExecuteBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blueprint_element_instance`` (PCGBlueprintElement):  [Read-Only]
- ``blueprint_element_type`` (type(Class)):  [Read-Write]
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
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``track_actors_only_within_bounds`` (bool):  [Read-Write] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.
- ``tracked_actor_tags`` (Array[Name]):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGBlueprintSettings.blueprint_element_type"></a>

#### blueprint\_element\_type

```python
@property
def blueprint_element_type() -> Class
```

(type(Class)):  [Read-Only]

<a id="unreal.PCGBlueprintSettings.blueprint_element_instance"></a>

#### blueprint\_element\_instance

```python
@property
def blueprint_element_instance() -> PCGBlueprintElement
```

(PCGBlueprintElement):  [Read-Only]

<a id="unreal.PCGBlueprintSettings.tracked_actor_tags"></a>

#### tracked\_actor\_tags

```python
@property
def tracked_actor_tags() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.PCGBlueprintSettings.tracked_actor_tags"></a>

#### tracked\_actor\_tags

```python
@tracked_actor_tags.setter
def tracked_actor_tags(value: Array[Name]) -> None
```

<a id="unreal.PCGBlueprintSettings.track_actors_only_within_bounds"></a>

#### track\_actors\_only\_within\_bounds

```python
@property
def track_actors_only_within_bounds() -> bool
```

(bool):  [Read-Only] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.

<a id="unreal.PCGBlueprintSettings.set_element_type"></a>

#### set\_element\_type

```python
def set_element_type(element_type: Class) -> PCGBlueprintElement
```

x.set_element_type(element_type) -> PCGBlueprintElement
Set Element Type

Args:
    element_type (type(Class)): 

Returns:
    PCGBlueprintElement: 

    element_instance (PCGBlueprintElement):

<a id="unreal.PCGBlueprintSettings.get_element_type"></a>

#### get\_element\_type

```python
def get_element_type() -> Class
```

x.get_element_type() -> type(Class)
Get Element Type

Returns:
    type(Class):

<a id="unreal.PCGFilterByIndexSettings"></a>