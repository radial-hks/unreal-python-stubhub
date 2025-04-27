## MovieScenePasteBindingsParams Objects

```python
class MovieScenePasteBindingsParams(StructBase)
```

Paste bindings params

**C++ Source:**

- **Module**: Sequencer
- **File**: SequencerUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bindings`` (Array[MovieSceneBindingProxy]):  [Read-Write]
- ``duplicate_existing_actors`` (bool):  [Read-Write]
- ``folders`` (Array[MovieSceneFolder]):  [Read-Write]
- ``parent_folder`` (MovieSceneFolder):  [Read-Write]
- ``pasted_actors`` (Map[Name, Actor]):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.__init__"></a>

#### __init__

```python
def __init__(bindings: Array[MovieSceneBindingProxy] = [],
             parent_folder: MovieSceneFolder = None,
             folders: Array[MovieSceneFolder] = [],
             duplicate_existing_actors: bool = False,
             pasted_actors: Map[Name, Actor] = {}) -> None
```

<a id="unreal.MovieScenePasteBindingsParams.bindings"></a>

#### bindings

```python
@property
def bindings() -> Array[MovieSceneBindingProxy]
```

(Array[MovieSceneBindingProxy]):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.bindings"></a>

#### bindings

```python
@bindings.setter
def bindings(value: Array[MovieSceneBindingProxy]) -> None
```

<a id="unreal.MovieScenePasteBindingsParams.parent_folder"></a>

#### parent_folder

```python
@property
def parent_folder() -> MovieSceneFolder
```

(MovieSceneFolder):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.parent_folder"></a>

#### parent_folder

```python
@parent_folder.setter
def parent_folder(value: MovieSceneFolder) -> None
```

<a id="unreal.MovieScenePasteBindingsParams.folders"></a>

#### folders

```python
@property
def folders() -> Array[MovieSceneFolder]
```

(Array[MovieSceneFolder]):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.folders"></a>

#### folders

```python
@folders.setter
def folders(value: Array[MovieSceneFolder]) -> None
```

<a id="unreal.MovieScenePasteBindingsParams.duplicate_existing_actors"></a>

#### duplicate_existing_actors

```python
@property
def duplicate_existing_actors() -> bool
```

(bool):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.duplicate_existing_actors"></a>

#### duplicate_existing_actors

```python
@duplicate_existing_actors.setter
def duplicate_existing_actors(value: bool) -> None
```

<a id="unreal.MovieScenePasteBindingsParams.pasted_actors"></a>

#### pasted_actors

```python
@property
def pasted_actors() -> Map[Name, Actor]
```

(Map[Name, Actor]):  [Read-Write]

<a id="unreal.MovieScenePasteBindingsParams.pasted_actors"></a>

#### pasted_actors

```python
@pasted_actors.setter
def pasted_actors(value: Map[Name, Actor]) -> None
```

<a id="unreal.TimecodeBoneMethod"></a>