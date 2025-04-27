## PCGGeometryBlueprintElement Objects

```python
class PCGGeometryBlueprintElement(PCGBlueprintElement)
```

Subclass of PCG Blueprint Element, it comes with pre-configured pins as input and output for Dynamic meshes and force to be non-cacheable.
The function CopyOrStealInputData is a helper to either steal (efficient) or copy the input data (less efficient) so work can be done in place on the Dynamic Mesh.
More importantly, a user deriving from this class will want to implement ProcessDynamicMesh, the only thing needed to streamline the process and
removes all the boilerplate when in a simple input->output case.

**C++ Source:**

- **Plugin**: PCGGeometryScriptInterop
- **Module**: PCGGeometryScriptInterop
- **File**: PCGGeometryBlueprintElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write]
- ``compute_full_data_crc`` (bool):  [Read-Write] In cases where your node is non-cacheable but is likely to yield the same results on subsequent executions, this controls whether we will do a deep & computationally intensive CRC computation (true),
  which will allow cache usage in downstream nodes in your graph, or, by default (false), a shallow but quick crc computation which will not be cache-friendly.
- ``custom_input_pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``custom_output_pins`` (Array[PCGPinProperties]):  [Read-Write]
- ``dependency_parsing_depth`` (int32):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``enable_preconfigured_settings`` (bool):  [Read-Write]
- ``expose_to_library`` (bool):  [Read-Write]
- ``has_default_in_pin`` (bool):  [Read-Write]
- ``has_default_out_pin`` (bool):  [Read-Write]
- ``has_dynamic_pins`` (bool):  [Read-Write] If enabled, by default, the Out pin type will have the union of In pin types. Default only works if the pins are In and Out. For custom behavior, implement DynamicPinTypesOverride.
- ``input_pin_labels`` (Set[Name]):  [Read-Write]
  deprecated: Property 'InputPinLabels' is deprecated.
- ``is_cacheable`` (bool):  [Read-Write] Controls whether results can be cached so we can bypass execution if the inputs & settings are the same in a subsequent execution.
  If you have implemented the IsCacheableOverride function, then this value is ignored.
  Note that if your node relies on data that is not directly tracked by PCG or creates any kind of artifact (adds components, creates actors, etc.) then it should not be cacheable.
- ``only_expose_preconfigured_settings`` (bool):  [Read-Write]
- ``output_pin_labels`` (Set[Name]):  [Read-Write]
- ``preconfigured_info`` (Array[PCGPreConfiguredSettingsInfo]):  [Read-Write]
- ``requires_game_thread`` (bool):  [Read-Write] Controls whether this node execution can be run from a non-game thread. This is not related to the Loop functions provided/implemented in this class, which should always run on any thread.

<a id="unreal.PCGGeometryBlueprintElement.process_dynamic_mesh"></a>

#### process_dynamic_mesh

```python
def process_dynamic_mesh(dyn_mesh: DynamicMesh) -> Array[str]
```

x.process_dynamic_mesh(dyn_mesh) -> Array[str]
Streamlined version of the Execute function, to only process the dynamic meshes.
For each input that is a dynamic mesh, we will call this function, and it will create as many output data as there are inputs.

Args:
    dyn_mesh (DynamicMesh): Dynamic mesh to process. Can be used as is and do operation in place.

Returns:
    Array[str]: 

    out_tags (Array[str]): Optional tags to add to the output. By default, it will inherit the tags of the input.

<a id="unreal.PCGGeometryBlueprintElement.copy_or_steal_input_data"></a>

#### copy_or_steal_input_data

```python
def copy_or_steal_input_data(tagged_data: PCGTaggedData) -> PCGDynamicMeshData
```

x.copy_or_steal_input_data(tagged_data) -> PCGDynamicMeshData
Allows to steal the data and work in place if the data is not used elsewhere. If this element is cacheable, it will automatically copy.

Args:
    tagged_data (PCGTaggedData): 

Returns:
    PCGDynamicMeshData:

<a id="unreal.PCGGetDynamicMeshDataSettings"></a>