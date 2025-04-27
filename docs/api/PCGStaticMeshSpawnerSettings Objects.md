## PCGStaticMeshSpawnerSettings Objects

```python
class PCGStaticMeshSpawnerSettings(PCGSettings)
```

PCGStatic Mesh Spawner Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGStaticMeshSpawner.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_descriptor_changes`` (bool):  [Read-Write] Allows PCG to make some changes on the descriptors as situation arises (using ISM instead of HISM for nanite meshes, etc.)
- ``apply_mesh_bounds_to_points`` (bool):  [Read-Write] Sets the BoundsMin and BoundsMax attributes of each point to reflect the StaticMesh spawned at its location
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
- ``instance_data_packer_parameters`` (PCGInstanceDataPackerBase):  [Read-Only]
- ``instance_data_packer_type`` (type(Class)):  [Read-Write] Defines the method of custom data packing for spawned (H)ISMCs. Note, Rotators are treated as 3 floats, while Quaternions are
  treated as 4 floats. You can see an attribute's type in the 'Attribute List View' window, and use an 'Attribute Cast' node to cast to the desired type.
- ``mesh_selector_parameters`` (PCGMeshSelectorBase):  [Read-Only]
- ``mesh_selector_type`` (type(Class)):  [Read-Write] Defines the method of mesh selection per input data
- ``out_attribute_name`` (Name):  [Read-Write] Attribute name to store mesh SoftObjectPaths inside if the output pin is connected. Note: Will overwrite existing data if the attribute name already exists.
- ``post_process_function_names`` (Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after instances are spawned. Functions need to be parameter-less and with "CallInEditor" flag enabled.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``silence_override_attribute_not_found_errors`` (bool):  [Read-Write] Opt-in option to silence errors when the property override attributes are not found.
- ``static_mesh_component_property_overrides`` (Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Map an attribute directly to an ISM Descriptor property, the value of which will be overriden when generated.
  Note: Currently only enabled using SelectByAttribute mesh selection.
- ``synchronous_load`` (bool):  [Read-Write] Meshes/Materials will be synchronously loaded before spawning instead of asynchronously.
- ``target_actor`` (Actor):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``warn_on_identical_spawn`` (bool):  [Read-Write] Adds a warning to the node on repeated spawning with identical conditions (ie. same mesh descriptor at same spawn location, etc).

<a id="unreal.PCGStaticMeshSpawnerSettings.mesh_selector_type"></a>

#### mesh_selector_type

```python
@property
def mesh_selector_type() -> Class
```

(type(Class)):  [Read-Only] Defines the method of mesh selection per input data

<a id="unreal.PCGStaticMeshSpawnerSettings.mesh_selector_parameters"></a>

#### mesh_selector_parameters

```python
@property
def mesh_selector_parameters() -> PCGMeshSelectorBase
```

(PCGMeshSelectorBase):  [Read-Only]

<a id="unreal.PCGStaticMeshSpawnerSettings.mesh_selector_instance"></a>

#### mesh_selector_instance

```python
@property
def mesh_selector_instance() -> PCGMeshSelectorBase
```

deprecated: 'mesh_selector_instance' was renamed to 'mesh_selector_parameters'.

<a id="unreal.PCGStaticMeshSpawnerSettings.allow_descriptor_changes"></a>

#### allow_descriptor_changes

```python
@property
def allow_descriptor_changes() -> bool
```

(bool):  [Read-Only] Allows PCG to make some changes on the descriptors as situation arises (using ISM instead of HISM for nanite meshes, etc.)

<a id="unreal.PCGStaticMeshSpawnerSettings.instance_data_packer_type"></a>

#### instance_data_packer_type

```python
@property
def instance_data_packer_type() -> Class
```

(type(Class)):  [Read-Only] Defines the method of custom data packing for spawned (H)ISMCs. Note, Rotators are treated as 3 floats, while Quaternions are
treated as 4 floats. You can see an attribute's type in the 'Attribute List View' window, and use an 'Attribute Cast' node to cast to the desired type.

<a id="unreal.PCGStaticMeshSpawnerSettings.instance_packer_type"></a>

#### instance_packer_type

```python
@property
def instance_packer_type() -> Class
```

deprecated: 'instance_packer_type' was renamed to 'instance_data_packer_type'.

<a id="unreal.PCGStaticMeshSpawnerSettings.instance_data_packer_parameters"></a>

#### instance_data_packer_parameters

```python
@property
def instance_data_packer_parameters() -> PCGInstanceDataPackerBase
```

(PCGInstanceDataPackerBase):  [Read-Only]

<a id="unreal.PCGStaticMeshSpawnerSettings.instance_packer_instance"></a>

#### instance_packer_instance

```python
@property
def instance_packer_instance() -> PCGInstanceDataPackerBase
```

deprecated: 'instance_packer_instance' was renamed to 'instance_data_packer_parameters'.

<a id="unreal.PCGStaticMeshSpawnerSettings.static_mesh_component_property_overrides"></a>

#### static_mesh_component_property_overrides

```python
@property
def static_mesh_component_property_overrides(
) -> Array[PCGObjectPropertyOverrideDescription]
```

(Array[PCGObjectPropertyOverrideDescription]):  [Read-Write] Map an attribute directly to an ISM Descriptor property, the value of which will be overriden when generated.
Note: Currently only enabled using SelectByAttribute mesh selection.

<a id="unreal.PCGStaticMeshSpawnerSettings.static_mesh_component_property_overrides"></a>

#### static_mesh_component_property_overrides

```python
@static_mesh_component_property_overrides.setter
def static_mesh_component_property_overrides(
        value: Array[PCGObjectPropertyOverrideDescription]) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.out_attribute_name"></a>

#### out_attribute_name

```python
@property
def out_attribute_name() -> Name
```

(Name):  [Read-Write] Attribute name to store mesh SoftObjectPaths inside if the output pin is connected. Note: Will overwrite existing data if the attribute name already exists.

<a id="unreal.PCGStaticMeshSpawnerSettings.out_attribute_name"></a>

#### out_attribute_name

```python
@out_attribute_name.setter
def out_attribute_name(value: Name) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.apply_mesh_bounds_to_points"></a>

#### apply_mesh_bounds_to_points

```python
@property
def apply_mesh_bounds_to_points() -> bool
```

(bool):  [Read-Write] Sets the BoundsMin and BoundsMax attributes of each point to reflect the StaticMesh spawned at its location

<a id="unreal.PCGStaticMeshSpawnerSettings.apply_mesh_bounds_to_points"></a>

#### apply_mesh_bounds_to_points

```python
@apply_mesh_bounds_to_points.setter
def apply_mesh_bounds_to_points(value: bool) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.target_actor"></a>

#### target_actor

```python
@property
def target_actor() -> Actor
```

(Actor):  [Read-Write]

<a id="unreal.PCGStaticMeshSpawnerSettings.target_actor"></a>

#### target_actor

```python
@target_actor.setter
def target_actor(value: Actor) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@property
def post_process_function_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Specify a list of functions to be called on the target actor after instances are spawned. Functions need to be parameter-less and with "CallInEditor" flag enabled.

<a id="unreal.PCGStaticMeshSpawnerSettings.post_process_function_names"></a>

#### post_process_function_names

```python
@post_process_function_names.setter
def post_process_function_names(value: Array[Name]) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.synchronous_load"></a>

#### synchronous_load

```python
@property
def synchronous_load() -> bool
```

(bool):  [Read-Write] Meshes/Materials will be synchronously loaded before spawning instead of asynchronously.

<a id="unreal.PCGStaticMeshSpawnerSettings.synchronous_load"></a>

#### synchronous_load

```python
@synchronous_load.setter
def synchronous_load(value: bool) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.silence_override_attribute_not_found_errors"></a>

#### silence_override_attribute_not_found_errors

```python
@property
def silence_override_attribute_not_found_errors() -> bool
```

(bool):  [Read-Write] Opt-in option to silence errors when the property override attributes are not found.

<a id="unreal.PCGStaticMeshSpawnerSettings.silence_override_attribute_not_found_errors"></a>

#### silence_override_attribute_not_found_errors

```python
@silence_override_attribute_not_found_errors.setter
def silence_override_attribute_not_found_errors(value: bool) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.warn_on_identical_spawn"></a>

#### warn_on_identical_spawn

```python
@property
def warn_on_identical_spawn() -> bool
```

(bool):  [Read-Write] Adds a warning to the node on repeated spawning with identical conditions (ie. same mesh descriptor at same spawn location, etc).

<a id="unreal.PCGStaticMeshSpawnerSettings.warn_on_identical_spawn"></a>

#### warn_on_identical_spawn

```python
@warn_on_identical_spawn.setter
def warn_on_identical_spawn(value: bool) -> None
```

<a id="unreal.PCGStaticMeshSpawnerSettings.set_mesh_selector_type"></a>

#### set_mesh_selector_type

```python
def set_mesh_selector_type(mesh_selector_type: Class) -> None
```

x.set_mesh_selector_type(mesh_selector_type) -> None
Set Mesh Selector Type

Args:
    mesh_selector_type (type(Class)):

<a id="unreal.PCGStaticMeshSpawnerSettings.set_instance_packer_type"></a>

#### set_instance_packer_type

```python
def set_instance_packer_type(instance_packer_type: Class) -> None
```

x.set_instance_packer_type(instance_packer_type) -> None
Set Instance Packer Type

Args:
    instance_packer_type (type(Class)):

<a id="unreal.PCGSurfaceSamplerSettings"></a>