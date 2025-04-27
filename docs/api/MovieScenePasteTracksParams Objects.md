## MovieScenePasteTracksParams Objects

```python
class MovieScenePasteTracksParams(StructBase)
```

Paste tracks params

**C++ Source:**

- **Module**: Sequencer
- **File**: SequencerUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bindings`` (Array[MovieSceneBindingProxy]):  [Read-Write]
- ``folders`` (Array[MovieSceneFolder]):  [Read-Write]
- ``parent_folder`` (MovieSceneFolder):  [Read-Write]
- ``sequence`` (MovieSceneSequence):  [Read-Write]

<a id="unreal.MovieScenePasteTracksParams.__init__"></a>

#### __init__

```python
def __init__(sequence: MovieSceneSequence = None,
             bindings: Array[MovieSceneBindingProxy] = [],
             parent_folder: MovieSceneFolder = None,
             folders: Array[MovieSceneFolder] = []) -> None
```

<a id="unreal.MovieScenePasteTracksParams.sequence"></a>

#### sequence

```python
@property
def sequence() -> MovieSceneSequence
```

(MovieSceneSequence):  [Read-Write]

<a id="unreal.MovieScenePasteTracksParams.sequence"></a>

#### sequence

```python
@sequence.setter
def sequence(value: MovieSceneSequence) -> None
```

<a id="unreal.MovieScenePasteTracksParams.bindings"></a>

#### bindings

```python
@property
def bindings() -> Array[MovieSceneBindingProxy]
```

(Array[MovieSceneBindingProxy]):  [Read-Write]

<a id="unreal.MovieScenePasteTracksParams.bindings"></a>

#### bindings

```python
@bindings.setter
def bindings(value: Array[MovieSceneBindingProxy]) -> None
```

<a id="unreal.MovieScenePasteTracksParams.parent_folder"></a>

#### parent_folder

```python
@property
def parent_folder() -> MovieSceneFolder
```

(MovieSceneFolder):  [Read-Write]

<a id="unreal.MovieScenePasteTracksParams.parent_folder"></a>

#### parent_folder

```python
@parent_folder.setter
def parent_folder(value: MovieSceneFolder) -> None
```

<a id="unreal.MovieScenePasteTracksParams.folders"></a>

#### folders

```python
@property
def folders() -> Array[MovieSceneFolder]
```

(Array[MovieSceneFolder]):  [Read-Write]

<a id="unreal.MovieScenePasteTracksParams.folders"></a>

#### folders

```python
@folders.setter
def folders(value: Array[MovieSceneFolder]) -> None
```

<a id="unreal.MovieSceneBindingProxy"></a>