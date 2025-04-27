## PCGDataFromActorSettings Objects

```python
class PCGDataFromActorSettings(PCGSettings)
```

Builds a collection of PCG-compatible data from the selected actors.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDataFromActor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_selector`` (PCGActorSelectorSettings):  [Read-Write] Describes which actors to select for data collection.
- ``allowed_grids`` (int32):  [Read-Write] Select which grid sizes to consider when collecting data from partitioned PCG components.
- ``also_output_single_point_data`` (bool):  [Read-Write] Also produces a single point data at the actor location.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``component_selector`` (PCGComponentSelectorSettings):  [Read-Write] Describes which components to select for the data collection.
- ``components_must_overlap_self`` (bool):  [Read-Write] Only get data from components which overlap with the bounds of your source component.
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expected_pins`` (Array[Name]):  [Read-Write] Provide pin names to match against the found component output pins. Data will automatically be wired to the expected pin if the name comparison succeeds. All unmatched pins will go into the standard out pin.
- ``expose_to_library`` (bool):  [Read-Write]
- ``get_data_on_all_grids`` (bool):  [Read-Write] Get data from all grid sizes if there is a partitioned PCG component on the actor, instead of a specific set of grid sizes.
- ``ignore_pcg_generated_components`` (bool):  [Read-Write] Ignores any component that was spawned by PCG.
- ``merge_single_point_data`` (bool):  [Read-Write] Merges all the single point data outputs into a single point data.
- ``mode`` (PCGGetDataFromActorMode):  [Read-Write] Describes what kind of data we will collect from the found actor(s).
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``property_name`` (Name):  [Read-Write] The property name on the found actor to create a data collection from.
- ``seed`` (int32):  [Read-Write]
- ``silence_sanitized_attribute_name_warnings`` (bool):  [Read-Write] Silence warnings that attribute names were sanitized to replace invalid characters.
- ``track_actors_only_within_bounds`` (bool):  [Read-Write] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGDataFromActorSettings.actor_selector"></a>

#### actor_selector

```python
@property
def actor_selector() -> PCGActorSelectorSettings
```

(PCGActorSelectorSettings):  [Read-Write] Describes which actors to select for data collection.

<a id="unreal.PCGDataFromActorSettings.actor_selector"></a>

#### actor_selector

```python
@actor_selector.setter
def actor_selector(value: PCGActorSelectorSettings) -> None
```

<a id="unreal.PCGDataFromActorSettings.component_selector"></a>

#### component_selector

```python
@property
def component_selector() -> PCGComponentSelectorSettings
```

(PCGComponentSelectorSettings):  [Read-Write] Describes which components to select for the data collection.

<a id="unreal.PCGDataFromActorSettings.component_selector"></a>

#### component_selector

```python
@component_selector.setter
def component_selector(value: PCGComponentSelectorSettings) -> None
```

<a id="unreal.PCGDataFromActorSettings.mode"></a>

#### mode

```python
@property
def mode() -> PCGGetDataFromActorMode
```

(PCGGetDataFromActorMode):  [Read-Write] Describes what kind of data we will collect from the found actor(s).

<a id="unreal.PCGDataFromActorSettings.mode"></a>

#### mode

```python
@mode.setter
def mode(value: PCGGetDataFromActorMode) -> None
```

<a id="unreal.PCGDataFromActorSettings.ignore_pcg_generated_components"></a>

#### ignore_pcg_generated_components

```python
@property
def ignore_pcg_generated_components() -> bool
```

(bool):  [Read-Write] Ignores any component that was spawned by PCG.

<a id="unreal.PCGDataFromActorSettings.ignore_pcg_generated_components"></a>

#### ignore_pcg_generated_components

```python
@ignore_pcg_generated_components.setter
def ignore_pcg_generated_components(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.also_output_single_point_data"></a>

#### also_output_single_point_data

```python
@property
def also_output_single_point_data() -> bool
```

(bool):  [Read-Write] Also produces a single point data at the actor location.

<a id="unreal.PCGDataFromActorSettings.also_output_single_point_data"></a>

#### also_output_single_point_data

```python
@also_output_single_point_data.setter
def also_output_single_point_data(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.components_must_overlap_self"></a>

#### components_must_overlap_self

```python
@property
def components_must_overlap_self() -> bool
```

(bool):  [Read-Write] Only get data from components which overlap with the bounds of your source component.

<a id="unreal.PCGDataFromActorSettings.components_must_overlap_self"></a>

#### components_must_overlap_self

```python
@components_must_overlap_self.setter
def components_must_overlap_self(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.get_data_on_all_grids"></a>

#### get_data_on_all_grids

```python
@property
def get_data_on_all_grids() -> bool
```

(bool):  [Read-Write] Get data from all grid sizes if there is a partitioned PCG component on the actor, instead of a specific set of grid sizes.

<a id="unreal.PCGDataFromActorSettings.get_data_on_all_grids"></a>

#### get_data_on_all_grids

```python
@get_data_on_all_grids.setter
def get_data_on_all_grids(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.allowed_grids"></a>

#### allowed_grids

```python
@property
def allowed_grids() -> int
```

(int32):  [Read-Write] Select which grid sizes to consider when collecting data from partitioned PCG components.

<a id="unreal.PCGDataFromActorSettings.allowed_grids"></a>

#### allowed_grids

```python
@allowed_grids.setter
def allowed_grids(value: int) -> None
```

<a id="unreal.PCGDataFromActorSettings.merge_single_point_data"></a>

#### merge_single_point_data

```python
@property
def merge_single_point_data() -> bool
```

(bool):  [Read-Write] Merges all the single point data outputs into a single point data.

<a id="unreal.PCGDataFromActorSettings.merge_single_point_data"></a>

#### merge_single_point_data

```python
@merge_single_point_data.setter
def merge_single_point_data(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.expected_pins"></a>

#### expected_pins

```python
@property
def expected_pins() -> Array[Name]
```

(Array[Name]):  [Read-Write] Provide pin names to match against the found component output pins. Data will automatically be wired to the expected pin if the name comparison succeeds. All unmatched pins will go into the standard out pin.

<a id="unreal.PCGDataFromActorSettings.expected_pins"></a>

#### expected_pins

```python
@expected_pins.setter
def expected_pins(value: Array[Name]) -> None
```

<a id="unreal.PCGDataFromActorSettings.property_name"></a>

#### property_name

```python
@property
def property_name() -> Name
```

(Name):  [Read-Write] The property name on the found actor to create a data collection from.

<a id="unreal.PCGDataFromActorSettings.property_name"></a>

#### property_name

```python
@property_name.setter
def property_name(value: Name) -> None
```

<a id="unreal.PCGDataFromActorSettings.silence_sanitized_attribute_name_warnings"></a>

#### silence_sanitized_attribute_name_warnings

```python
@property
def silence_sanitized_attribute_name_warnings() -> bool
```

(bool):  [Read-Write] Silence warnings that attribute names were sanitized to replace invalid characters.

<a id="unreal.PCGDataFromActorSettings.silence_sanitized_attribute_name_warnings"></a>

#### silence_sanitized_attribute_name_warnings

```python
@silence_sanitized_attribute_name_warnings.setter
def silence_sanitized_attribute_name_warnings(value: bool) -> None
```

<a id="unreal.PCGDataFromActorSettings.track_actors_only_within_bounds"></a>

#### track_actors_only_within_bounds

```python
@property
def track_actors_only_within_bounds() -> bool
```

(bool):  [Read-Only] If this is checked, found actors that are outside component bounds will not trigger a refresh. Only works for tags for now in editor.

<a id="unreal.PCGDataNumSettings"></a>