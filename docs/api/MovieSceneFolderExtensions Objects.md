## MovieSceneFolderExtensions Objects

```python
class MovieSceneFolderExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneFolders for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneFolderExtensions.h

<a id="unreal.MovieSceneFolderExtensions.set_folder_name"></a>

#### set_folder_name

```python
@classmethod
def set_folder_name(cls, folder: MovieSceneFolder, folder_name: Name) -> bool
```

X.set_folder_name(folder, folder_name) -> bool
Set the name of the given folder

Args:
    folder (MovieSceneFolder): The folder to set the name of
    folder_name (Name): The new name for the folder

Returns:
    bool: True if the setting of the folder name succeeds

<a id="unreal.MovieSceneFolderExtensions.set_folder_color"></a>

#### set_folder_color

```python
@classmethod
def set_folder_color(cls, folder: MovieSceneFolder,
                     folder_color: Color) -> bool
```

X.set_folder_color(folder, folder_color) -> bool
Set the display color of the given folder

Args:
    folder (MovieSceneFolder): The folder to set the display color of
    folder_color (Color): The new display color for the folder

Returns:
    bool: True if the folder's display color is set successfully

<a id="unreal.MovieSceneFolderExtensions.remove_child_track"></a>

#### remove_child_track

```python
@classmethod
def remove_child_track(cls, folder: MovieSceneFolder,
                       track: MovieSceneTrack) -> bool
```

X.remove_child_track(folder, track) -> bool
Remove a track from the given folder

Args:
    folder (MovieSceneFolder): The folder from which to remove a track
    track (MovieSceneTrack): The track to remove

Returns:
    bool: True if the removal succeeds

<a id="unreal.MovieSceneFolderExtensions.remove_child_object_binding"></a>

#### remove_child_object_binding

```python
@classmethod
def remove_child_object_binding(
        cls, folder: MovieSceneFolder,
        object_binding: MovieSceneBindingProxy) -> bool
```

X.remove_child_object_binding(folder, object_binding) -> bool
Remove an object binding from the given folder

Args:
    folder (MovieSceneFolder): The folder from which to remove an object binding
    object_binding (MovieSceneBindingProxy): The object binding to remove

Returns:
    bool: True if the operation succeeds

<a id="unreal.MovieSceneFolderExtensions.remove_child_folder"></a>

#### remove_child_folder

```python
@classmethod
def remove_child_folder(cls, target_folder: MovieSceneFolder,
                        folder_to_remove: MovieSceneFolder) -> bool
```

X.remove_child_folder(target_folder, folder_to_remove) -> bool
Remove a child folder from the given folder

Args:
    target_folder (MovieSceneFolder): The folder from which to remove a child folder
    folder_to_remove (MovieSceneFolder): The child folder to be removed

Returns:
    bool: True if the removal succeeds

<a id="unreal.MovieSceneFolderExtensions.get_folder_name"></a>

#### get_folder_name

```python
@classmethod
def get_folder_name(cls, folder: MovieSceneFolder) -> Name
```

X.get_folder_name(folder) -> Name
Get the given folder's display name

Args:
    folder (MovieSceneFolder): The folder to use

Returns:
    Name: The target folder's name

<a id="unreal.MovieSceneFolderExtensions.get_folder_color"></a>

#### get_folder_color

```python
@classmethod
def get_folder_color(cls, folder: MovieSceneFolder) -> Color
```

X.get_folder_color(folder) -> Color
Get the display color of the given folder

Args:
    folder (MovieSceneFolder): The folder to get the display color of

Returns:
    Color: The display color of the given folder

<a id="unreal.MovieSceneFolderExtensions.get_child_tracks"></a>

#### get_child_tracks

```python
@classmethod
def get_child_tracks(cls, folder: MovieSceneFolder) -> Array[MovieSceneTrack]
```

X.get_child_tracks(folder) -> Array[MovieSceneTrack]
Get the tracks contained by this folder

Args:
    folder (MovieSceneFolder): The folder to get the tracks of

Returns:
    Array[MovieSceneTrack]: The tracks under the given folder

<a id="unreal.MovieSceneFolderExtensions.get_child_object_bindings"></a>

#### get_child_object_bindings

```python
@classmethod
def get_child_object_bindings(
        cls, folder: MovieSceneFolder) -> Array[MovieSceneBindingProxy]
```

X.get_child_object_bindings(folder) -> Array[MovieSceneBindingProxy]
Get the object bindings contained by this folder

Args:
    folder (MovieSceneFolder): The folder to get the bindings of

Returns:
    Array[MovieSceneBindingProxy]: The object bindings under the given folder

<a id="unreal.MovieSceneFolderExtensions.get_child_folders"></a>

#### get_child_folders

```python
@classmethod
def get_child_folders(cls,
                      folder: MovieSceneFolder) -> Array[MovieSceneFolder]
```

X.get_child_folders(folder) -> Array[MovieSceneFolder]
Get the child folders of a given folder

Args:
    folder (MovieSceneFolder): The folder to get the child folders of

Returns:
    Array[MovieSceneFolder]: The child folders associated with the given folder

<a id="unreal.MovieSceneFolderExtensions.add_child_track"></a>

#### add_child_track

```python
@classmethod
def add_child_track(cls, folder: MovieSceneFolder,
                    track: MovieSceneTrack) -> bool
```

X.add_child_track(folder, track) -> bool
Add a track to this folder

Args:
    folder (MovieSceneFolder): The folder to add a child track to
    track (MovieSceneTrack): The track to add to the folder

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneFolderExtensions.add_child_object_binding"></a>

#### add_child_object_binding

```python
@classmethod
def add_child_object_binding(cls, folder: MovieSceneFolder,
                             object_binding: MovieSceneBindingProxy) -> bool
```

X.add_child_object_binding(folder, object_binding) -> bool
Add a guid for an object binding to this folder

Args:
    folder (MovieSceneFolder): The folder to add a child object to
    object_binding (MovieSceneBindingProxy): The binding to add to the folder

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneFolderExtensions.add_child_folder"></a>

#### add_child_folder

```python
@classmethod
def add_child_folder(cls, target_folder: MovieSceneFolder,
                     folder_to_add: MovieSceneFolder) -> bool
```

X.add_child_folder(target_folder, folder_to_add) -> bool
Add a child folder to the target folder

Args:
    target_folder (MovieSceneFolder): The folder to add a child folder to
    folder_to_add (MovieSceneFolder): The child folder to be added

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneMaterialTrackExtensions"></a>