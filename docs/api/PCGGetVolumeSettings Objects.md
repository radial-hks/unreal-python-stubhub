## PCGGetVolumeSettings Objects

```python
class PCGGetVolumeSettings(PCGDataFromActorSettings)
```

Builds a collection of volume data from the selected actors.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGTypedGetter.h

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

<a id="unreal.PCGGetPrimitiveSettings"></a>