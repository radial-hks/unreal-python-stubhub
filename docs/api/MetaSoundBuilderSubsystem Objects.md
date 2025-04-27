## MetaSoundBuilderSubsystem Objects

```python
class MetaSoundBuilderSubsystem(EngineSubsystem)
```

The subsystem in charge of tracking MetaSound builders

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundBuilderSubsystem.h

<a id="unreal.MetaSoundBuilderSubsystem.unregister_source_builder"></a>

#### unregister_source_builder

```python
def unregister_source_builder(builder_name: Name) -> bool
```

x.unregister_source_builder(builder_name) -> bool
Unregister Source Builder

Args:
    builder_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderSubsystem.unregister_patch_builder"></a>

#### unregister_patch_builder

```python
def unregister_patch_builder(builder_name: Name) -> bool
```

x.unregister_patch_builder(builder_name) -> bool
Unregister Patch Builder

Args:
    builder_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderSubsystem.unregister_builder"></a>

#### unregister_builder

```python
def unregister_builder(builder_name: Name) -> bool
```

x.unregister_builder(builder_name) -> bool
Unregister Builder

Args:
    builder_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderSubsystem.set_target_page"></a>

#### set_target_page

```python
def set_target_page(page_name: Name) -> bool
```

x.set_target_page(page_name) -> bool
Sets the targeted page for all MetaSound graph & input default to resolve against.
If target page is not implemented (or cooked in a runtime build) for the active platform,
uses order of cooked pages(see 'Page Settings' for order) falling back to lower index - ordered page
implemented in MetaSound asset. If no fallback is found, uses default graph/input default.

Args:
    page_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderSubsystem.register_source_builder"></a>

#### register_source_builder

```python
def register_source_builder(builder_name: Name,
                            builder: MetaSoundSourceBuilder) -> None
```

x.register_source_builder(builder_name, builder) -> None
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

Args:
    builder_name (Name): 
    builder (MetaSoundSourceBuilder):

<a id="unreal.MetaSoundBuilderSubsystem.register_patch_builder"></a>

#### register_patch_builder

```python
def register_patch_builder(builder_name: Name,
                           builder: MetaSoundPatchBuilder) -> None
```

x.register_patch_builder(builder_name, builder) -> None
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

Args:
    builder_name (Name): 
    builder (MetaSoundPatchBuilder):

<a id="unreal.MetaSoundBuilderSubsystem.register_builder"></a>

#### register_builder

```python
def register_builder(builder_name: Name,
                     builder: MetaSoundBuilderBase) -> None
```

x.register_builder(builder_name, builder) -> None
Adds builder to subsystem's registry to make it persistent and easily accessible by multiple systems or Blueprints

Args:
    builder_name (Name): 
    builder (MetaSoundBuilderBase):

<a id="unreal.MetaSoundBuilderSubsystem.is_interface_registered"></a>

#### is_interface_registered

```python
def is_interface_registered(interface_name: Name) -> bool
```

x.is_interface_registered(interface_name) -> bool
Is Interface Registered

Args:
    interface_name (Name): 

Returns:
    bool:

<a id="unreal.MetaSoundBuilderSubsystem.find_source_builder"></a>

#### find_source_builder

```python
def find_source_builder(builder_name: Name) -> MetaSoundSourceBuilder
```

x.find_source_builder(builder_name) -> MetaSoundSourceBuilder
Returns the source builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

Args:
    builder_name (Name): 

Returns:
    MetaSoundSourceBuilder:

<a id="unreal.MetaSoundBuilderSubsystem.find_patch_builder"></a>

#### find_patch_builder

```python
def find_patch_builder(builder_name: Name) -> MetaSoundPatchBuilder
```

x.find_patch_builder(builder_name) -> MetaSoundPatchBuilder
Returns the patch builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

Args:
    builder_name (Name): 

Returns:
    MetaSoundPatchBuilder:

<a id="unreal.MetaSoundBuilderSubsystem.find_builder_of_document"></a>

#### find_builder_of_document

```python
def find_builder_of_document(
        meta_sound: MetaSoundDocumentInterface) -> MetaSoundBuilderBase
```

x.find_builder_of_document(meta_sound) -> MetaSoundBuilderBase
Returns the builder associated with the given MetaSound (if one exists, transient or asset).

Args:
    meta_sound (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderBase:

<a id="unreal.MetaSoundBuilderSubsystem.find_builder"></a>

#### find_builder

```python
def find_builder(builder_name: Name) -> MetaSoundBuilderBase
```

x.find_builder(builder_name) -> MetaSoundBuilderBase
Returns the builder manually registered with the MetaSound Builder Subsystem with the provided custom name (if previously registered)

Args:
    builder_name (Name): 

Returns:
    MetaSoundBuilderBase:

<a id="unreal.MetaSoundBuilderSubsystem.create_string_meta_sound_literal"></a>

#### create_string_meta_sound_literal

```python
def create_string_meta_sound_literal(
        value: str) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_string_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create String Meta Sound Literal

Args:
    value (str): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_string_array_meta_sound_literal"></a>

#### create_string_array_meta_sound_literal

```python
def create_string_array_meta_sound_literal(
        value: Array[str]) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_string_array_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create String Array Meta Sound Literal

Args:
    value (Array[str]): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_source_preset_builder"></a>

#### create_source_preset_builder

```python
def create_source_preset_builder(
    builder_name: Name, referenced_source_class: MetaSoundDocumentInterface
) -> Tuple[MetaSoundSourceBuilder, MetaSoundBuilderResult]
```

x.create_source_preset_builder(builder_name, referenced_source_class) -> (MetaSoundSourceBuilder, out_result=MetaSoundBuilderResult)
Create Source Preset Builder

Args:
    builder_name (Name): 
    referenced_source_class (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderSubsystem.create_source_builder"></a>

#### create_source_builder

```python
def create_source_builder(
    builder_name: Name,
    output_format: MetaSoundOutputAudioFormat = MetaSoundOutputAudioFormat.
    MONO,
    is_one_shot: bool = True
) -> Tuple[MetaSoundSourceBuilder, MetaSoundBuilderNodeOutputHandle,
           MetaSoundBuilderNodeInputHandle,
           Array[MetaSoundBuilderNodeInputHandle], MetaSoundBuilderResult]
```

x.create_source_builder(builder_name, output_format=MetaSoundOutputAudioFormat.MONO, is_one_shot=True) -> (MetaSoundSourceBuilder, on_play_node_output=MetaSoundBuilderNodeOutputHandle, on_finished_node_input=MetaSoundBuilderNodeInputHandle, audio_out_node_inputs=Array[MetaSoundBuilderNodeInputHandle], out_result=MetaSoundBuilderResult)
Create Source Builder

Args:
    builder_name (Name): 
    output_format (MetaSoundOutputAudioFormat): 
    is_one_shot (bool): 

Returns:
    tuple: 

    on_play_node_output (MetaSoundBuilderNodeOutputHandle): 

    on_finished_node_input (MetaSoundBuilderNodeInputHandle): 

    audio_out_node_inputs (Array[MetaSoundBuilderNodeInputHandle]): 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderSubsystem.create_patch_preset_builder"></a>

#### create_patch_preset_builder

```python
def create_patch_preset_builder(
    builder_name: Name, referenced_patch_class: MetaSoundDocumentInterface
) -> Tuple[MetaSoundPatchBuilder, MetaSoundBuilderResult]
```

x.create_patch_preset_builder(builder_name, referenced_patch_class) -> (MetaSoundPatchBuilder, out_result=MetaSoundBuilderResult)
Create Patch Preset Builder

Args:
    builder_name (Name): 
    referenced_patch_class (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderSubsystem.create_patch_builder"></a>

#### create_patch_builder

```python
def create_patch_builder(
    builder_name: Name
) -> Tuple[MetaSoundPatchBuilder, MetaSoundBuilderResult]
```

x.create_patch_builder(builder_name) -> (MetaSoundPatchBuilder, out_result=MetaSoundBuilderResult)
Create Patch Builder

Args:
    builder_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBuilderSubsystem.create_object_meta_sound_literal"></a>

#### create_object_meta_sound_literal

```python
def create_object_meta_sound_literal(
        value: Object) -> MetasoundFrontendLiteral
```

x.create_object_meta_sound_literal(value) -> MetasoundFrontendLiteral
Create Object Meta Sound Literal

Args:
    value (Object): 

Returns:
    MetasoundFrontendLiteral:

<a id="unreal.MetaSoundBuilderSubsystem.create_object_array_meta_sound_literal"></a>

#### create_object_array_meta_sound_literal

```python
def create_object_array_meta_sound_literal(
        value: Array[Object]) -> MetasoundFrontendLiteral
```

x.create_object_array_meta_sound_literal(value) -> MetasoundFrontendLiteral
Create Object Array Meta Sound Literal

Args:
    value (Array[Object]): 

Returns:
    MetasoundFrontendLiteral:

<a id="unreal.MetaSoundBuilderSubsystem.create_meta_sound_literal_from_param"></a>

#### create_meta_sound_literal_from_param

```python
def create_meta_sound_literal_from_param(
        param: AudioParameter) -> MetasoundFrontendLiteral
```

x.create_meta_sound_literal_from_param(param) -> MetasoundFrontendLiteral
Create Meta Sound Literal from Param

Args:
    param (AudioParameter): 

Returns:
    MetasoundFrontendLiteral:

<a id="unreal.MetaSoundBuilderSubsystem.create_int_meta_sound_literal"></a>

#### create_int_meta_sound_literal

```python
def create_int_meta_sound_literal(
        value: int) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_int_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Int Meta Sound Literal

Args:
    value (int32): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_int_array_meta_sound_literal"></a>

#### create_int_array_meta_sound_literal

```python
def create_int_array_meta_sound_literal(
        value: Array[int]) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_int_array_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Int Array Meta Sound Literal

Args:
    value (Array[int32]): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_float_meta_sound_literal"></a>

#### create_float_meta_sound_literal

```python
def create_float_meta_sound_literal(
        value: float) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_float_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Float Meta Sound Literal

Args:
    value (float): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_float_array_meta_sound_literal"></a>

#### create_float_array_meta_sound_literal

```python
def create_float_array_meta_sound_literal(
        value: Array[float]) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_float_array_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Float Array Meta Sound Literal

Args:
    value (Array[float]): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_bool_meta_sound_literal"></a>

#### create_bool_meta_sound_literal

```python
def create_bool_meta_sound_literal(
        value: bool) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_bool_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Bool Meta Sound Literal

Args:
    value (bool): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundBuilderSubsystem.create_bool_array_meta_sound_literal"></a>

#### create_bool_array_meta_sound_literal

```python
def create_bool_array_meta_sound_literal(
        value: Array[bool]) -> Tuple[MetasoundFrontendLiteral, Name]
```

x.create_bool_array_meta_sound_literal(value) -> (MetasoundFrontendLiteral, data_type=Name)
Create Bool Array Meta Sound Literal

Args:
    value (Array[bool]): 

Returns:
    Name: 

    data_type (Name):

<a id="unreal.MetaSoundSource"></a>