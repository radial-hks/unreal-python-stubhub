## MovieSceneMetaData Objects

```python
class MovieSceneMetaData(Object)
```

Movie scene meta-data that is stored on UMovieScene assets
Meta-data is retrieved through ULevelSequence::FindMetaData<ULevelSequenceMetaData>()

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneMetaData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``author`` (str):  [Read-Write] The author that created this metadata
- ``created`` (DateTime):  [Read-Write] The created date at which the metadata was initiated
- ``notes`` (str):  [Read-Write] Notes for the metadata

<a id="unreal.MovieSceneMetaData.set_notes"></a>

#### set_notes

```python
def set_notes(notes: str) -> None
```

x.set_notes(notes) -> None
Set this metadata's notes

Args:
    notes (str):

<a id="unreal.MovieSceneMetaData.set_created"></a>

#### set_created

```python
def set_created(created: DateTime) -> None
```

x.set_created(created) -> None
Set this metadata's created date

Args:
    created (DateTime):

<a id="unreal.MovieSceneMetaData.set_author"></a>

#### set_author

```python
def set_author(author: str) -> None
```

x.set_author(author) -> None
Set this metadata's author

Args:
    author (str):

<a id="unreal.MovieSceneMetaData.get_notes"></a>

#### get_notes

```python
def get_notes() -> str
```

x.get_notes() -> str


Returns:
    str: The notes for this metadata

<a id="unreal.MovieSceneMetaData.get_created"></a>

#### get_created

```python
def get_created() -> DateTime
```

x.get_created() -> DateTime


Returns:
    DateTime: The created date for this metadata

<a id="unreal.MovieSceneMetaData.get_author"></a>

#### get_author

```python
def get_author() -> str
```

x.get_author() -> str


Returns:
    str: The author for this metadata

<a id="unreal.MovieSceneSequencePlayer"></a>