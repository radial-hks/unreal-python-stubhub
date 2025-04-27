## MovieSceneFolder Objects

```python
class MovieSceneFolder(Object)
```

Represents a folder used for organizing objects in tracks in a movie scene.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneFolder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``folder_color`` (Color):  [Read-Write] This folder's color

<a id="unreal.MovieSceneFolder.set_folder_name"></a>

#### set_folder_name

```python
def set_folder_name(folder_name: Name) -> bool
```

x.set_folder_name(folder_name) -> bool
Set the name of the given folder

Args:
    folder_name (Name): The new name for the folder

Returns:
    bool: True if the setting of the folder name succeeds

<a id="unreal.MovieSceneFolder.set_folder_color"></a>

#### set_folder_color

```python
def set_folder_color(folder_color: Color) -> bool
```

x.set_folder_color(folder_color) -> bool
Set the display color of the given folder

Args:
    folder_color (Color): The new display color for the folder

Returns:
    bool: True if the folder's display color is set successfully

<a id="unreal.MovieSceneFolder.remove_child_track"></a>

#### remove_child_track

```python
def remove_child_track(track: MovieSceneTrack) -> bool
```

x.remove_child_track(track) -> bool
Remove a track from the given folder

Args:
    track (MovieSceneTrack): The track to remove

Returns:
    bool: True if the removal succeeds

<a id="unreal.MovieSceneFolder.remove_child_object_binding"></a>

#### remove_child_object_binding

```python
def remove_child_object_binding(
        object_binding: MovieSceneBindingProxy) -> bool
```

x.remove_child_object_binding(object_binding) -> bool
Remove an object binding from the given folder

Args:
    object_binding (MovieSceneBindingProxy): The object binding to remove

Returns:
    bool: True if the operation succeeds

<a id="unreal.MovieSceneFolder.remove_child_folder"></a>

#### remove_child_folder

```python
def remove_child_folder(folder_to_remove: MovieSceneFolder) -> bool
```

x.remove_child_folder(folder_to_remove) -> bool
Remove a child folder from the given folder

Args:
    folder_to_remove (MovieSceneFolder): The child folder to be removed

Returns:
    bool: True if the removal succeeds

<a id="unreal.MovieSceneFolder.get_folder_name"></a>

#### get_folder_name

```python
def get_folder_name() -> Name
```

x.get_folder_name() -> Name
Get the given folder's display name

Returns:
    Name: The target folder's name

<a id="unreal.MovieSceneFolder.get_folder_color"></a>

#### get_folder_color

```python
def get_folder_color() -> Color
```

x.get_folder_color() -> Color
Get the display color of the given folder

Returns:
    Color: The display color of the given folder

<a id="unreal.MovieSceneFolder.get_child_tracks"></a>

#### get_child_tracks

```python
def get_child_tracks() -> Array[MovieSceneTrack]
```

x.get_child_tracks() -> Array[MovieSceneTrack]
Get the tracks contained by this folder

Returns:
    Array[MovieSceneTrack]: The tracks under the given folder

<a id="unreal.MovieSceneFolder.get_child_object_bindings"></a>

#### get_child_object_bindings

```python
def get_child_object_bindings() -> Array[MovieSceneBindingProxy]
```

x.get_child_object_bindings() -> Array[MovieSceneBindingProxy]
Get the object bindings contained by this folder

Returns:
    Array[MovieSceneBindingProxy]: The object bindings under the given folder

<a id="unreal.MovieSceneFolder.get_child_folders"></a>

#### get_child_folders

```python
def get_child_folders() -> Array[MovieSceneFolder]
```

x.get_child_folders() -> Array[MovieSceneFolder]
Get the child folders of a given folder

Returns:
    Array[MovieSceneFolder]: The child folders associated with the given folder

<a id="unreal.MovieSceneFolder.add_child_track"></a>

#### add_child_track

```python
def add_child_track(track: MovieSceneTrack) -> bool
```

x.add_child_track(track) -> bool
Add a track to this folder

Args:
    track (MovieSceneTrack): The track to add to the folder

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneFolder.add_child_object_binding"></a>

#### add_child_object_binding

```python
def add_child_object_binding(object_binding: MovieSceneBindingProxy) -> bool
```

x.add_child_object_binding(object_binding) -> bool
Add a guid for an object binding to this folder

Args:
    object_binding (MovieSceneBindingProxy): The binding to add to the folder

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneFolder.add_child_folder"></a>

#### add_child_folder

```python
def add_child_folder(folder_to_add: MovieSceneFolder) -> bool
```

x.add_child_folder(folder_to_add) -> bool
Add a child folder to the target folder

Args:
    folder_to_add (MovieSceneFolder): The child folder to be added

Returns:
    bool: True if the addition is successful

<a id="unreal.MovieSceneMetaData"></a>