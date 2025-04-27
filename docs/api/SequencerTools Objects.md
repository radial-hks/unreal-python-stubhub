## SequencerTools Objects

```python
class SequencerTools(BlueprintFunctionLibrary)
```

This is a set of helper functions to access various parts of the Sequencer API via Python. Because Sequencer itself is not suitable for exposing, most functionality
gets wrapped by UObjects that have an easier API to work with. This UObject provides access to these wrapper UObjects where needed.

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerTools.h

<a id="unreal.SequencerTools.render_movie"></a>

#### render_movie

```python
@classmethod
def render_movie(cls, capture_settings: MovieSceneCapture,
                 on_finished_callback: OnRenderMovieStopped) -> bool
```

X.render_movie(capture_settings, on_finished_callback) -> bool
Render Movie
deprecated: Function 'RenderMovie' is deprecated.

Args:
    capture_settings (MovieSceneCapture): 
    on_finished_callback (OnRenderMovieStopped): 

Returns:
    bool:

<a id="unreal.SequencerTools.link_anim_sequence"></a>

#### link_anim_sequence

```python
@classmethod
def link_anim_sequence(cls, sequence: LevelSequence,
                       anim_sequence: AnimSequence,
                       export_options: AnimSeqExportOption,
                       binding: MovieSceneBindingProxy) -> bool
```

X.link_anim_sequence(sequence, anim_sequence, export_options, binding) -> bool
* Links a LevelSequence's SkeletalMesh binding to an existing anim sequence.
*
*
InSequence: Sequence to link from *
AnimSequence: The AnimSequence to link to. *
ExportOption: The export options that should be used when baking the LevelSequence. *
InBinding: Binding that has a skelmesh component on it

Args:
    sequence (LevelSequence): 
    anim_sequence (AnimSequence): 
    export_options (AnimSeqExportOption): 
    binding (MovieSceneBindingProxy): 

Returns:
    bool:

<a id="unreal.SequencerTools.is_rendering_movie"></a>

#### is_rendering_movie

```python
@classmethod
def is_rendering_movie(cls) -> bool
```

X.is_rendering_movie() -> bool
Is Rendering Movie
deprecated: Function 'IsRenderingMovie' is deprecated.

Returns:
    bool:

<a id="unreal.SequencerTools.is_event_endpoint_valid"></a>

#### is_event_endpoint_valid

```python
@classmethod
def is_event_endpoint_valid(cls,
                            endpoint: SequencerQuickBindingResult) -> bool
```

X.is_event_endpoint_valid(endpoint) -> bool
Check if an endpoint is valid and can be used to create movie scene event.

Args:
    endpoint (SequencerQuickBindingResult): Endpoint to check.

Returns:
    bool:

<a id="unreal.SequencerTools.import_level_sequence_fbx"></a>

#### import_level_sequence_fbx

```python
@classmethod
def import_level_sequence_fbx(
        cls, world: World, sequence: LevelSequence,
        bindings: Array[MovieSceneBindingProxy],
        import_fbx_settings: MovieSceneUserImportFBXSettings,
        import_filename: str) -> bool
```

X.import_level_sequence_fbx(world, sequence, bindings, import_fbx_settings, import_filename) -> bool
* Import FBX onto Passed in Bindings
*
*
InWorld: World to import to *
InSequence: InSequence to import *
InBindings: InBindings to import *
InImportFBXSettings: Settings to control import. *
InImportFileName: Path to fbx file to import from *
InPlayer: Player to bind to

Args:
    world (World): 
    sequence (LevelSequence): 
    bindings (Array[MovieSceneBindingProxy]): 
    import_fbx_settings (MovieSceneUserImportFBXSettings): 
    import_filename (str): 

Returns:
    bool:

<a id="unreal.SequencerTools.import_fbx_to_control_rig"></a>

#### import_fbx_to_control_rig

```python
@classmethod
def import_fbx_to_control_rig(cls, world: World, sequence: LevelSequence,
                              actor_with_control_rig_track: str,
                              selected_control_rig_names: Array[str],
                              import_fbx_control_rig_settings:
                              MovieSceneUserImportFBXControlRigSettings,
                              import_filename: str) -> bool
```

X.import_fbx_to_control_rig(world, sequence, actor_with_control_rig_track, selected_control_rig_names, import_fbx_control_rig_settings, import_filename) -> bool
* Import FBX onto a control rig with the specified track name
*
*
InWorld: World to import to *
InSequence: InSequence to import *
ActorWithControlRigTrack: ActorWithControlRigTrack The name of the actor with the control rig track we are importing onto *
SelectedControlRigNames: List of selected control rig names. Will use them if  ImportFBXControlRigSettings->bImportOntoSelectedControls is true *
ImportFBXControlRigSettings: Settings to control import. *
InImportFileName: Path to fbx file to create

Args:
    world (World): 
    sequence (LevelSequence): 
    actor_with_control_rig_track (str): 
    selected_control_rig_names (Array[str]): 
    import_fbx_control_rig_settings (MovieSceneUserImportFBXControlRigSettings): 
    import_filename (str): 

Returns:
    bool:

<a id="unreal.SequencerTools.get_object_bindings"></a>

#### get_object_bindings

```python
@classmethod
def get_object_bindings(
        cls, world: World, sequence: LevelSequence, object: Array[Object],
        range: SequencerScriptingRange) -> Array[SequencerBoundObjects]
```

X.get_object_bindings(world, sequence, object, range) -> Array[SequencerBoundObjects]
Get Object Bindings
deprecated: Function 'GetObjectBindings' is deprecated.

Args:
    world (World): 
    sequence (LevelSequence): 
    object (Array[Object]): 
    range (SequencerScriptingRange): 

Returns:
    Array[SequencerBoundObjects]:

<a id="unreal.SequencerTools.get_level_sequence_link_from_anim_sequence"></a>

#### get_level_sequence_link_from_anim_sequence

```python
@classmethod
def get_level_sequence_link_from_anim_sequence(
        cls, anim_sequence: AnimSequence) -> AnimSequenceLevelSequenceLink
```

X.get_level_sequence_link_from_anim_sequence(anim_sequence) -> AnimSequenceLevelSequenceLink
* Get the link to the level sequence if it exists on this anim sequence
*
*
InAnimSequence: AnimSequence to get links from *

Args:
    anim_sequence (AnimSequence): 

Returns:
    AnimSequenceLevelSequenceLink: Returns the link object if it exists, nullptr if it doesn't

<a id="unreal.SequencerTools.get_bound_objects"></a>

#### get_bound_objects

```python
@classmethod
def get_bound_objects(
        cls, world: World, sequence: LevelSequence,
        bindings: Array[MovieSceneBindingProxy],
        range: SequencerScriptingRange) -> Array[SequencerBoundObjects]
```

X.get_bound_objects(world, sequence, bindings, range) -> Array[SequencerBoundObjects]
Get Bound Objects
deprecated: Function 'GetBoundObjects' is deprecated.

Args:
    world (World): 
    sequence (LevelSequence): 
    bindings (Array[MovieSceneBindingProxy]): 
    range (SequencerScriptingRange): 

Returns:
    Array[SequencerBoundObjects]:

<a id="unreal.SequencerTools.get_anim_sequence_link_from_level_sequence"></a>

#### get_anim_sequence_link_from_level_sequence

```python
@classmethod
def get_anim_sequence_link_from_level_sequence(
        cls, level_sequence: LevelSequence) -> LevelSequenceAnimSequenceLink
```

X.get_anim_sequence_link_from_level_sequence(level_sequence) -> LevelSequenceAnimSequenceLink
* Get the links to the anim sequences if they exist on this level sequence
*
*
InLevelSequence: LevelSequence to get links from *

Args:
    level_sequence (LevelSequence): 

Returns:
    LevelSequenceAnimSequenceLink: Returns the link object if it exists, nullptr if it doesn't

<a id="unreal.SequencerTools.export_level_sequence_fbx"></a>

#### export_level_sequence_fbx

```python
@classmethod
def export_level_sequence_fbx(cls, params: SequencerExportFBXParams) -> bool
```

X.export_level_sequence_fbx(params) -> bool
* Export Passed in Bindings and Tracks to FBX

Args:
    params (SequencerExportFBXParams): 

Returns:
    bool:

<a id="unreal.SequencerTools.export_fbx_from_control_rig"></a>

#### export_fbx_from_control_rig

```python
@classmethod
def export_fbx_from_control_rig(
    cls, sequence: LevelSequence, actor_with_control_rig_track: str,
    export_fbx_control_rig_settings: MovieSceneUserExportFBXControlRigSettings
) -> bool
```

X.export_fbx_from_control_rig(sequence, actor_with_control_rig_track, export_fbx_control_rig_settings) -> bool
Exports an FBX from the section to key of the control rig track of the actor with the given name.

Args:
    sequence (LevelSequence): 
    actor_with_control_rig_track (str): 
    export_fbx_control_rig_settings (MovieSceneUserExportFBXControlRigSettings): 

Returns:
    bool:

<a id="unreal.SequencerTools.export_anim_sequence"></a>

#### export_anim_sequence

```python
@classmethod
def export_anim_sequence(cls, world: World, sequence: LevelSequence,
                         anim_sequence: AnimSequence,
                         export_option: AnimSeqExportOption,
                         binding: MovieSceneBindingProxy,
                         create_link: bool) -> bool
```

X.export_anim_sequence(world, sequence, anim_sequence, export_option, binding, create_link) -> bool
* Export Passed in Binding as an Anim Seqquence.
*
*
InWorld: World to export *
InSequence: Sequence to export *
AnimSequence: The AnimSequence to save into. *
ExportOption: The export options for the sequence. *
InBinding: Binding to export that has a skelmesh component on it *
InAnimSequenceFilename: File to create *
bCreateLink: If true will create a link between the animation sequence and the level sequence

Args:
    world (World): 
    sequence (LevelSequence): 
    anim_sequence (AnimSequence): 
    export_option (AnimSeqExportOption): 
    binding (MovieSceneBindingProxy): 
    create_link (bool): 

Returns:
    bool:

<a id="unreal.SequencerTools.create_quick_binding"></a>

#### create_quick_binding

```python
@classmethod
def create_quick_binding(cls, sequence: MovieSceneSequence, object: Object,
                         function_name: str,
                         call_in_editor: bool) -> SequencerQuickBindingResult
```

X.create_quick_binding(sequence, object, function_name, call_in_editor) -> SequencerQuickBindingResult
Create a quick binding to an actor's member method to be used in an event sequence.

Args:
    sequence (MovieSceneSequence): 
    object (Object): 
    function_name (str): Name of the method, as it is displayed in the Blueprint Editor. eg. "Set Actor Scale 3D"
    call_in_editor (bool): Should the event be callable in editor.

Returns:
    SequencerQuickBindingResult: The created binding.

<a id="unreal.SequencerTools.create_event"></a>

#### create_event

```python
@classmethod
def create_event(cls, sequence: MovieSceneSequence,
                 section: MovieSceneEventSectionBase,
                 endpoint: SequencerQuickBindingResult,
                 payload: Array[str]) -> MovieSceneEvent
```

X.create_event(sequence, section, endpoint, payload) -> MovieSceneEvent
Create an event from a previously created blueprint endpoint and a payload. The resulting event should be added only
to a channel of the section that was given as a parameter.
InEndpoint.: 
see: CreateQuickBinding

Args:
    sequence (MovieSceneSequence): Main level sequence that holds the event track and to which the resulting event should be added.
    section (MovieSceneEventSectionBase): Section of the event track of the main sequence.
    endpoint (SequencerQuickBindingResult): Previously created endpoint.
    payload (Array[str]): Values passed as payload to event, count must match the numbers of payload variable names in

Returns:
    MovieSceneEvent: The created movie event.

<a id="unreal.SequencerTools.clear_linked_anim_sequences"></a>

#### clear_linked_anim_sequences

```python
@classmethod
def clear_linked_anim_sequences(cls, level_sequence: LevelSequence) -> None
```

X.clear_linked_anim_sequences(level_sequence) -> None
* Clear all linked anim sequences between this level sequence and any linked anim sequences
*
*
InLevelSequence: LevelSequence to clean links for

Args:
    level_sequence (LevelSequence):

<a id="unreal.SequencerTools.cancel_movie_render"></a>

#### cancel_movie_render

```python
@classmethod
def cancel_movie_render(cls) -> None
```

X.cancel_movie_render() -> None
Cancel Movie Render
deprecated: Function 'CancelMovieRender' is deprecated.

<a id="unreal.LevelSequenceFactoryNew"></a>