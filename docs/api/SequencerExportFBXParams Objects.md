## SequencerExportFBXParams Objects

```python
class SequencerExportFBXParams(StructBase)
```

Sequencer Export FBXParams

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScriptingEditor
- **File**: SequencerTools.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bindings`` (Array[MovieSceneBindingProxy]):  [Read-Write]
- ``fbx_file_name`` (str):  [Read-Write]
- ``override_options`` (FbxExportOption):  [Read-Write]
- ``root_sequence`` (LevelSequence):  [Read-Write]
- ``sequence`` (LevelSequence):  [Read-Write]
- ``tracks`` (Array[MovieSceneTrack]):  [Read-Write]
- ``world`` (World):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.__init__"></a>

#### __init__

```python
def __init__(world: World = None,
             sequence: LevelSequence = None,
             root_sequence: LevelSequence = None,
             bindings: Array[MovieSceneBindingProxy] = [],
             tracks: Array[MovieSceneTrack] = [],
             override_options: FbxExportOption = None,
             fbx_file_name: str = "") -> None
```

<a id="unreal.SequencerExportFBXParams.world"></a>

#### world

```python
@property
def world() -> World
```

(World):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.world"></a>

#### world

```python
@world.setter
def world(value: World) -> None
```

<a id="unreal.SequencerExportFBXParams.sequence"></a>

#### sequence

```python
@property
def sequence() -> LevelSequence
```

(LevelSequence):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.sequence"></a>

#### sequence

```python
@sequence.setter
def sequence(value: LevelSequence) -> None
```

<a id="unreal.SequencerExportFBXParams.root_sequence"></a>

#### root_sequence

```python
@property
def root_sequence() -> LevelSequence
```

(LevelSequence):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.root_sequence"></a>

#### root_sequence

```python
@root_sequence.setter
def root_sequence(value: LevelSequence) -> None
```

<a id="unreal.SequencerExportFBXParams.bindings"></a>

#### bindings

```python
@property
def bindings() -> Array[MovieSceneBindingProxy]
```

(Array[MovieSceneBindingProxy]):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.bindings"></a>

#### bindings

```python
@bindings.setter
def bindings(value: Array[MovieSceneBindingProxy]) -> None
```

<a id="unreal.SequencerExportFBXParams.tracks"></a>

#### tracks

```python
@property
def tracks() -> Array[MovieSceneTrack]
```

(Array[MovieSceneTrack]):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.tracks"></a>

#### tracks

```python
@tracks.setter
def tracks(value: Array[MovieSceneTrack]) -> None
```

<a id="unreal.SequencerExportFBXParams.override_options"></a>

#### override_options

```python
@property
def override_options() -> FbxExportOption
```

(FbxExportOption):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.override_options"></a>

#### override_options

```python
@override_options.setter
def override_options(value: FbxExportOption) -> None
```

<a id="unreal.SequencerExportFBXParams.fbx_file_name"></a>

#### fbx_file_name

```python
@property
def fbx_file_name() -> str
```

(str):  [Read-Write]

<a id="unreal.SequencerExportFBXParams.fbx_file_name"></a>

#### fbx_file_name

```python
@fbx_file_name.setter
def fbx_file_name(value: str) -> None
```

<a id="unreal.MovieSceneScriptingParams"></a>