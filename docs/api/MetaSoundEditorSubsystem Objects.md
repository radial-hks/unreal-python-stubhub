## MetaSoundEditorSubsystem Objects

```python
class MetaSoundEditorSubsystem(EditorSubsystem)
```

The subsystem in charge of editor MetaSound functionality

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEditor
- **File**: MetasoundEditorSubsystem.h

<a id="unreal.MetaSoundEditorSubsystem.set_node_location"></a>

#### set_node_location

```python
def set_node_location(builder: MetaSoundBuilderBase, node: MetaSoundNodeHandle,
                      location: Vector2D) -> MetaSoundBuilderResult
```

x.set_node_location(builder, node, location) -> MetaSoundBuilderResult
Sets the visual location to InLocation of a given node InNode of a given builder's document.

Args:
    builder (MetaSoundBuilderBase): 
    node (MetaSoundNodeHandle): 
    location (Vector2D): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundEditorSubsystem.set_focused_page"></a>

#### set_focused_page

```python
def set_focused_page(builder: MetaSoundBuilderBase, page_name: Name,
                     open_editor: bool) -> MetaSoundBuilderResult
```

x.set_focused_page(builder, page_name, open_editor) -> MetaSoundBuilderResult
If the given page name is implemented on the provided builder, sets the focused page of
the provided builder to the associated page and sets the audition page to
the provided name. If the given builder has an asset editor open, optionally opens or brings
that editor's associated PageID into user focus.

Args:
    builder (MetaSoundBuilderBase): 
    page_name (Name): 
    open_editor (bool): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundEditorSubsystem.find_or_create_graph_input_metadata"></a>

#### find_or_create_graph_input_metadata

```python
def find_or_create_graph_input_metadata(
    builder: MetaSoundBuilderBase, input_name: Name
) -> Tuple[MetaSoundFrontendMemberMetadata, MetaSoundBuilderResult]
```

x.find_or_create_graph_input_metadata(builder, input_name) -> (MetaSoundFrontendMemberMetadata, out_result=MetaSoundBuilderResult)
Find graph input metadata (which includes editor only range information for floats) for a given input. If the metadata does not exist, create it.

Args:
    builder (MetaSoundBuilderBase): 
    input_name (Name): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundEditorSubsystem.find_or_begin_building"></a>

#### find_or_begin_building

```python
def find_or_begin_building(
    meta_sound: MetaSoundDocumentInterface
) -> Tuple[MetaSoundBuilderBase, MetaSoundBuilderResult]
```

x.find_or_begin_building(meta_sound) -> (MetaSoundBuilderBase, out_result=MetaSoundBuilderResult)
Returns a builder for the given MetaSound asset. Returns null if provided a transient MetaSound. For finding builders for transient
MetaSounds, use the UMetaSoundBuilderSubsystem's API (FindPatchBuilder, FindSourceBuilder, FindBuilderByName etc.)

Args:
    meta_sound (MetaSoundDocumentInterface): 

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundEditorSubsystem.build_to_asset"></a>

#### build_to_asset

```python
def build_to_asset(
    builder: MetaSoundBuilderBase,
    author: str,
    asset_name: str,
    package_path: str,
    template_sound_wave: SoundWave = None
) -> Tuple[MetaSoundDocumentInterface, MetaSoundBuilderResult]
```

x.build_to_asset(builder, author, asset_name, package_path, template_sound_wave=None) -> (MetaSoundDocumentInterface, out_result=MetaSoundBuilderResult)
Build the given builder to a MetaSound asset

Args:
    builder (MetaSoundBuilderBase): 
    author (str): Sets the author on the given builder's document.
    asset_name (str): Name of the asset to build.
    package_path (str): Path of package to build asset to.
    template_sound_wave (SoundWave): SoundWave settings such as attenuation, modulation, and sound class will be copied from the optional TemplateSoundWave. For preset builders, TemplateSoundWave will override the template values from the referenced asset.

Returns:
    MetaSoundBuilderResult: 

    out_result (MetaSoundBuilderResult):

<a id="unreal.MetaSoundBaseFactory"></a>