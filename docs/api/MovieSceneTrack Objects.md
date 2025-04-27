## MovieSceneTrack Objects

```python
class MovieSceneTrack(MovieSceneSignedObject)
```

Base class for a track in a Movie Scene

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``condition_container`` (MovieSceneConditionContainer):  [Read-Write] Optional dynamic condition for whether this track/any of the sections on this track evaluates at runtime.
- ``display_options`` (MovieSceneTrackDisplayOptions):  [Read-Write] General display options for a given track
- ``eval_options`` (MovieSceneTrackEvalOptions):  [Read-Write] General evaluation options for a given track
- ``track_tint`` (Color):  [Read-Write] This track's tint color

<a id="unreal.MovieSceneTrack.set_track_row_display_name"></a>

#### set_track_row_display_name

```python
def set_track_row_display_name(name: Text, row_index: int) -> None
```

x.set_track_row_display_name(name, row_index) -> None
Set this track row's display name

Args:
    name (Text): The name for this track
    row_index (int32): The row index for the track

<a id="unreal.MovieSceneTrack.set_sorting_order"></a>

#### set_sorting_order

```python
def set_sorting_order(sorting_order: int) -> None
```

x.set_sorting_order(sorting_order) -> None
Set the sorting order for this track

Args:
    sorting_order (int32): The sorting order to set

<a id="unreal.MovieSceneTrack.set_section_to_key"></a>

#### set_section_to_key

```python
def set_section_to_key(section: MovieSceneSection) -> None
```

x.set_section_to_key(section) -> None
Set the section to key for this track. When properties for this section are modified externally,
this section will receive those modifications and act accordingly (add/update keys). This is
especially useful when there are multiple overlapping sections.

Args:
    section (MovieSceneSection): The section to key for this track

<a id="unreal.MovieSceneTrack.set_display_name"></a>

#### set_display_name

```python
def set_display_name(name: Text) -> None
```

x.set_display_name(name) -> None
Set this track's display name

Args:
    name (Text): The name for this track

<a id="unreal.MovieSceneTrack.set_color_tint"></a>

#### set_color_tint

```python
def set_color_tint(color_tint: Color) -> None
```

x.set_color_tint(color_tint) -> None
Set the color tint for this track

Args:
    color_tint (Color): The color tint to set

<a id="unreal.MovieSceneTrack.remove_section"></a>

#### remove_section

```python
def remove_section(section: MovieSceneSection) -> None
```

x.remove_section(section) -> None
Remove the specified section

Args:
    section (MovieSceneSection): The section to remove

<a id="unreal.MovieSceneTrack.get_track_row_display_name"></a>

#### get_track_row_display_name

```python
def get_track_row_display_name(row_index: int) -> Text
```

x.get_track_row_display_name(row_index) -> Text
Get this track row's display name

Args:
    row_index (int32): The row index for the track

Returns:
    Text: This track's display name

<a id="unreal.MovieSceneTrack.get_sorting_order"></a>

#### get_sorting_order

```python
def get_sorting_order() -> int
```

x.get_sorting_order() -> int32
Get the sorting order for this track

Returns:
    int32: The sorting order of the requested track

<a id="unreal.MovieSceneTrack.get_section_to_key"></a>

#### get_section_to_key

```python
def get_section_to_key() -> MovieSceneSection
```

x.get_section_to_key() -> MovieSceneSection
Get the section to key for this track

Returns:
    MovieSceneSection: The section to key for the requested track

<a id="unreal.MovieSceneTrack.get_sections"></a>

#### get_sections

```python
def get_sections() -> Array[MovieSceneSection]
```

x.get_sections() -> Array[MovieSceneSection]
Access all this track's sections

Returns:
    Array[MovieSceneSection]: An array of this track's sections

<a id="unreal.MovieSceneTrack.get_display_name"></a>

#### get_display_name

```python
def get_display_name() -> Text
```

x.get_display_name() -> Text
Get this track's display name

Returns:
    Text: This track's display name

<a id="unreal.MovieSceneTrack.get_color_tint"></a>

#### get_color_tint

```python
def get_color_tint() -> Color
```

x.get_color_tint() -> Color
Get the color tint for this track

Returns:
    Color: The color tint of the requested track

<a id="unreal.MovieSceneTrack.add_section"></a>

#### add_section

```python
def add_section() -> MovieSceneSection
```

x.add_section() -> MovieSceneSection
Add a new section to this track

Returns:
    MovieSceneSection: The newly create section if successful

<a id="unreal.MovieSceneNameableTrack"></a>