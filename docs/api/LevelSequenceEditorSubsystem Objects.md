## LevelSequenceEditorSubsystem Objects

```python
class LevelSequenceEditorSubsystem(EditorSubsystem)
```

ULevelSequenceEditorSubsystem
Subsystem for level sequence editor related utilities to scripts

**C++ Source:**

- **Plugin**: LevelSequenceEditor
- **Module**: LevelSequenceEditor
- **File**: LevelSequenceEditorSubsystem.h

<a id="unreal.LevelSequenceEditorSubsystem.sync_sections_using_source_timecode"></a>

#### sync_sections_using_source_timecode

```python
def sync_sections_using_source_timecode(
        sections: Array[MovieSceneSection]) -> None
```

x.sync_sections_using_source_timecode(sections) -> None
Sync section using source timecode

Args:
    sections (Array[MovieSceneSection]):

<a id="unreal.LevelSequenceEditorSubsystem.snap_sections_to_timeline_using_source_timecode"></a>

#### snap_sections_to_timeline_using_source_timecode

```python
def snap_sections_to_timeline_using_source_timecode(
        sections: Array[MovieSceneSection]) -> None
```

x.snap_sections_to_timeline_using_source_timecode(sections) -> None
Snap sections to timeline using source timecode

Args:
    sections (Array[MovieSceneSection]):

<a id="unreal.LevelSequenceEditorSubsystem.save_default_spawnable_state"></a>

#### save_default_spawnable_state

```python
def save_default_spawnable_state(
        object_binding: MovieSceneBindingProxy) -> None
```

x.save_default_spawnable_state(object_binding) -> None
Save the default state of the spawnable.

Args:
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.replace_binding_with_actors"></a>

#### replace_binding_with_actors

```python
def replace_binding_with_actors(
        actors: Array[Actor], object_binding: MovieSceneBindingProxy) -> None
```

x.replace_binding_with_actors(actors, object_binding) -> None
Replaces the binding with the given actors

Args:
    actors (Array[Actor]): 
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.remove_invalid_bindings"></a>

#### remove_invalid_bindings

```python
def remove_invalid_bindings(object_binding: MovieSceneBindingProxy) -> None
```

x.remove_invalid_bindings(object_binding) -> None
Remove missing objects bound to this track

Args:
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.remove_all_bindings"></a>

#### remove_all_bindings

```python
def remove_all_bindings(object_binding: MovieSceneBindingProxy) -> None
```

x.remove_all_bindings(object_binding) -> None
Remove all bound actors from this track

Args:
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.remove_actors_from_binding"></a>

#### remove_actors_from_binding

```python
def remove_actors_from_binding(actors: Array[Actor],
                               object_binding: MovieSceneBindingProxy) -> None
```

x.remove_actors_from_binding(actors, object_binding) -> None
Removes the given actors from the binding

Args:
    actors (Array[Actor]): 
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.rebind_component"></a>

#### rebind_component

```python
def rebind_component(component_bindings: Array[MovieSceneBindingProxy],
                     component_name: Name) -> None
```

x.rebind_component(component_bindings, component_name) -> None
Rebind the component binding to the requested component

Args:
    component_bindings (Array[MovieSceneBindingProxy]): 
    component_name (Name):

<a id="unreal.LevelSequenceEditorSubsystem.paste_tracks"></a>

#### paste_tracks

```python
def paste_tracks(
    text_to_import: str, paste_tracks_params: MovieScenePasteTracksParams
) -> Optional[Array[MovieSceneTrack]]
```

x.paste_tracks(text_to_import, paste_tracks_params) -> Array[MovieSceneTrack] or None
Paste tracks
Paste tracks from the given TextToImport string (used in conjunction with CopyTracks).
If TextToImport is empty, the contents of the clipboard will be used.

Args:
    text_to_import (str): 
    paste_tracks_params (MovieScenePasteTracksParams): 

Returns:
    Array[MovieSceneTrack] or None: 

    out_tracks (Array[MovieSceneTrack]):

<a id="unreal.LevelSequenceEditorSubsystem.paste_sections"></a>

#### paste_sections

```python
def paste_sections(
    text_to_import: str, paste_sections_params: MovieScenePasteSectionsParams
) -> Optional[Array[MovieSceneSection]]
```

x.paste_sections(text_to_import, paste_sections_params) -> Array[MovieSceneSection] or None
Paste sections
Paste sections from the given TextToImport string (used in conjunction with CopySections).
If TextToImport is empty, the contents of the clipboard will be used.

Args:
    text_to_import (str): 
    paste_sections_params (MovieScenePasteSectionsParams): 

Returns:
    Array[MovieSceneSection] or None: 

    out_sections (Array[MovieSceneSection]):

<a id="unreal.LevelSequenceEditorSubsystem.paste_folders"></a>

#### paste_folders

```python
def paste_folders(
    text_to_import: str, paste_folders_params: MovieScenePasteFoldersParams
) -> Optional[Array[MovieSceneFolder]]
```

x.paste_folders(text_to_import, paste_folders_params) -> Array[MovieSceneFolder] or None
Paste folders
Paste folders from the given TextToImport string (used in conjunction with CopyFolders).
If TextToImport is empty, the contents of the clipboard will be used.

Args:
    text_to_import (str): 
    paste_folders_params (MovieScenePasteFoldersParams): 

Returns:
    Array[MovieSceneFolder] or None: 

    out_folders (Array[MovieSceneFolder]):

<a id="unreal.LevelSequenceEditorSubsystem.paste_bindings"></a>

#### paste_bindings

```python
def paste_bindings(
    text_to_import: str, paste_bindings_params: MovieScenePasteBindingsParams
) -> Optional[Array[MovieSceneBindingProxy]]
```

x.paste_bindings(text_to_import, paste_bindings_params) -> Array[MovieSceneBindingProxy] or None
Paste bindings
Paste bindings from the given TextToImport string (used in conjunction with CopyBindings).
If TextToImport is empty, the contents of the clipboard will be used.

Args:
    text_to_import (str): 
    paste_bindings_params (MovieScenePasteBindingsParams): 

Returns:
    Array[MovieSceneBindingProxy] or None: 

    out_object_bindings (Array[MovieSceneBindingProxy]):

<a id="unreal.LevelSequenceEditorSubsystem.get_scripting_layer"></a>

#### get_scripting_layer

```python
def get_scripting_layer() -> SequencerModuleScriptingLayer
```

x.get_scripting_layer() -> SequencerModuleScriptingLayer
Retrieve the scripting layer

Returns:
    SequencerModuleScriptingLayer:

<a id="unreal.LevelSequenceEditorSubsystem.get_custom_binding_type"></a>

#### get_custom_binding_type

```python
def get_custom_binding_type(object_binding: MovieSceneBindingProxy) -> Class
```

x.get_custom_binding_type(object_binding) -> type(Class)
Returns the custom binding type for the given binding, or nullptr for possessables

Args:
    object_binding (MovieSceneBindingProxy): 

Returns:
    type(Class):

<a id="unreal.LevelSequenceEditorSubsystem.get_custom_bindings_of_type"></a>

#### get_custom_bindings_of_type

```python
def get_custom_bindings_of_type(
        custom_binding_type: Class) -> Array[MovieSceneBindingProxy]
```

x.get_custom_bindings_of_type(custom_binding_type) -> Array[MovieSceneBindingProxy]
Returns all of the bindings in the sequence of the given custom type.

Args:
    custom_binding_type (type(Class)): 

Returns:
    Array[MovieSceneBindingProxy]:

<a id="unreal.LevelSequenceEditorSubsystem.get_custom_binding_objects"></a>

#### get_custom_binding_objects

```python
def get_custom_binding_objects(
        object_binding: MovieSceneBindingProxy
) -> Array[MovieSceneCustomBinding]
```

x.get_custom_binding_objects(object_binding) -> Array[MovieSceneCustomBinding]
In the case that the given binding proxy holds custom bindings, returns an array of the binding objects so properties can be accessed.

Args:
    object_binding (MovieSceneBindingProxy): 

Returns:
    Array[MovieSceneCustomBinding]:

<a id="unreal.LevelSequenceEditorSubsystem.get_curve_editor"></a>

#### get_curve_editor

```python
def get_curve_editor() -> SequencerCurveEditorObject
```

x.get_curve_editor() -> SequencerCurveEditorObject
Retrieve the curve editor

Returns:
    SequencerCurveEditorObject:

<a id="unreal.LevelSequenceEditorSubsystem.fix_actor_references"></a>

#### fix_actor_references

```python
def fix_actor_references() -> None
```

x.fix_actor_references() -> None
Attempts to automatically fix up broken actor references in the current scene

<a id="unreal.LevelSequenceEditorSubsystem.create_camera"></a>

#### create_camera

```python
def create_camera(
        spawnable: bool) -> Tuple[MovieSceneBindingProxy, CineCameraActor]
```

x.create_camera(spawnable) -> (MovieSceneBindingProxy, out_actor=CineCameraActor)
Create a cine camera actor and add it to Sequencer

Args:
    spawnable (bool): 

Returns:
    CineCameraActor: 

    out_actor (CineCameraActor):

<a id="unreal.LevelSequenceEditorSubsystem.copy_tracks"></a>

#### copy_tracks

```python
def copy_tracks(tracks: Array[MovieSceneTrack]) -> str
```

x.copy_tracks(tracks) -> str
Copy tracks
The copied tracks will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteTracks if, for example, pasting copy/pasting multiple
tracks without relying on a single clipboard.

Args:
    tracks (Array[MovieSceneTrack]): 

Returns:
    str: 

    exported_text (str):

<a id="unreal.LevelSequenceEditorSubsystem.copy_sections"></a>

#### copy_sections

```python
def copy_sections(sections: Array[MovieSceneSection]) -> str
```

x.copy_sections(sections) -> str
Copy sections
The copied sections will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteSections if, for example, pasting copy/pasting multiple
sections without relying on a single clipboard.

Args:
    sections (Array[MovieSceneSection]): 

Returns:
    str: 

    exported_text (str):

<a id="unreal.LevelSequenceEditorSubsystem.copy_folders"></a>

#### copy_folders

```python
def copy_folders(folders: Array[MovieSceneFolder]) -> str
```

x.copy_folders(folders) -> str
Copy folders
The copied folders will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteFolders if, for example, pasting copy/pasting multiple
folders without relying on a single clipboard.

Args:
    folders (Array[MovieSceneFolder]): 

Returns:
    str: 

    exported_text (str):

<a id="unreal.LevelSequenceEditorSubsystem.copy_bindings"></a>

#### copy_bindings

```python
def copy_bindings(bindings: Array[MovieSceneBindingProxy]) -> str
```

x.copy_bindings(bindings) -> str
Copy bindings
The copied bindings will be saved to the clipboard as well as assigned to the ExportedText string.
The ExportedTest string can be used in conjunction with PasteBindings if, for example, pasting copy/pasting multiple
bindings without relying on a single clipboard.

Args:
    bindings (Array[MovieSceneBindingProxy]): 

Returns:
    str: 

    exported_text (str):

<a id="unreal.LevelSequenceEditorSubsystem.convert_to_spawnable"></a>

#### convert_to_spawnable

```python
def convert_to_spawnable(
        object_binding: MovieSceneBindingProxy
) -> Array[MovieSceneBindingProxy]
```

x.convert_to_spawnable(object_binding) -> Array[MovieSceneBindingProxy]
Convert to spawnable. If there are multiple objects assigned to the possessable, multiple spawnables will be created.
For level sequences, the bindings created will be custom bindings of type UMovieSceneSpawnableActorBinding.

Args:
    object_binding (MovieSceneBindingProxy): 

Returns:
    Array[MovieSceneBindingProxy]:

<a id="unreal.LevelSequenceEditorSubsystem.convert_to_possessable"></a>

#### convert_to_possessable

```python
def convert_to_possessable(
        object_binding: MovieSceneBindingProxy) -> MovieSceneBindingProxy
```

x.convert_to_possessable(object_binding) -> MovieSceneBindingProxy
Convert to possessable. If there are multiple objects assigned to the spawnable.

Args:
    object_binding (MovieSceneBindingProxy): 

Returns:
    MovieSceneBindingProxy:

<a id="unreal.LevelSequenceEditorSubsystem.convert_to_custom_binding"></a>

#### convert_to_custom_binding

```python
def convert_to_custom_binding(object_binding: MovieSceneBindingProxy,
                              binding_type: Class) -> MovieSceneBindingProxy
```

x.convert_to_custom_binding(object_binding, binding_type) -> MovieSceneBindingProxy
Convert to a custom binding of the given binding type

Args:
    object_binding (MovieSceneBindingProxy): 
    binding_type (type(Class)): 

Returns:
    MovieSceneBindingProxy:

<a id="unreal.LevelSequenceEditorSubsystem.change_actor_template_class"></a>

#### change_actor_template_class

```python
def change_actor_template_class(object_binding: MovieSceneBindingProxy,
                                actor_class: Class) -> bool
```

x.change_actor_template_class(object_binding, actor_class) -> bool
Sets the actor class for the spawnable or replaceable template, in the case those binding types support templates.

Args:
    object_binding (MovieSceneBindingProxy): 
    actor_class (type(Class)): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorSubsystem.bake_transform_with_settings"></a>

#### bake_transform_with_settings

```python
def bake_transform_with_settings(
    object_bindings: Array[MovieSceneBindingProxy],
    settings: BakingAnimationKeySettings,
    params: MovieSceneScriptingParams = [MovieSceneTimeUnit.DISPLAY_RATE
                                         ]) -> bool
```

x.bake_transform_with_settings(object_bindings, settings, params=[MovieSceneTimeUnit.DISPLAY_RATE]) -> bool
Bake Transform with Settings

Args:
    object_bindings (Array[MovieSceneBindingProxy]): 
    settings (BakingAnimationKeySettings): 
    params (MovieSceneScriptingParams): 

Returns:
    bool:

<a id="unreal.LevelSequenceEditorSubsystem.bake_transform"></a>

#### bake_transform

```python
def bake_transform(
    object_bindings: Array[MovieSceneBindingProxy],
    bake_in_time: FrameTime,
    bake_out_time: FrameTime,
    bake_interval: FrameTime,
    params: MovieSceneScriptingParams = [MovieSceneTimeUnit.DISPLAY_RATE
                                         ]) -> None
```

x.bake_transform(object_bindings, bake_in_time, bake_out_time, bake_interval, params=[MovieSceneTimeUnit.DISPLAY_RATE]) -> None
Bake Transform

Args:
    object_bindings (Array[MovieSceneBindingProxy]): 
    bake_in_time (FrameTime): 
    bake_out_time (FrameTime): 
    bake_interval (FrameTime): 
    params (MovieSceneScriptingParams):

<a id="unreal.LevelSequenceEditorSubsystem.add_actors_to_binding"></a>

#### add_actors_to_binding

```python
def add_actors_to_binding(actors: Array[Actor],
                          object_binding: MovieSceneBindingProxy) -> None
```

x.add_actors_to_binding(actors, object_binding) -> None
Assigns the given actors to the binding

Args:
    actors (Array[Actor]): 
    object_binding (MovieSceneBindingProxy):

<a id="unreal.LevelSequenceEditorSubsystem.add_actors"></a>

#### add_actors

```python
def add_actors(actors: Array[Actor]) -> Array[MovieSceneBindingProxy]
```

x.add_actors(actors) -> Array[MovieSceneBindingProxy]
Add existing actors to Sequencer. Tracks will be automatically added based on default track settings.

Args:
    actors (Array[Actor]): 

Returns:
    Array[MovieSceneBindingProxy]:

<a id="unreal.LevelSequenceWithShotsSettings"></a>