## MovieSceneTrackExtensions Objects

```python
class MovieSceneTrackExtensions(BlueprintFunctionLibrary)
```

Function library containing methods that should be hoisted onto UMovieSceneTracks for scripting

**C++ Source:**

- **Plugin**: SequencerScripting
- **Module**: SequencerScripting
- **File**: MovieSceneTrackExtensions.h

<a id="unreal.MovieSceneTrackExtensions.set_track_row_display_name"></a>

#### set_track_row_display_name

```python
@classmethod
def set_track_row_display_name(cls, track: MovieSceneTrack, name: Text,
                               row_index: int) -> None
```

X.set_track_row_display_name(track, name, row_index) -> None
Set this track row's display name

Args:
    track (MovieSceneTrack): The track to use
    name (Text): The name for this track
    row_index (int32): The row index for the track

<a id="unreal.MovieSceneTrackExtensions.set_sorting_order"></a>

#### set_sorting_order

```python
@classmethod
def set_sorting_order(cls, track: MovieSceneTrack, sorting_order: int) -> None
```

X.set_sorting_order(track, sorting_order) -> None
Set the sorting order for this track

Args:
    track (MovieSceneTrack): The track to get the sorting order from
    sorting_order (int32): The sorting order to set

<a id="unreal.MovieSceneTrackExtensions.set_section_to_key"></a>

#### set_section_to_key

```python
@classmethod
def set_section_to_key(cls, track: MovieSceneTrack,
                       section: MovieSceneSection) -> None
```

X.set_section_to_key(track, section) -> None
Set the section to key for this track. When properties for this section are modified externally,
this section will receive those modifications and act accordingly (add/update keys). This is
especially useful when there are multiple overlapping sections.

Args:
    track (MovieSceneTrack): The track to set the section to key for
    section (MovieSceneSection): The section to key for this track

<a id="unreal.MovieSceneTrackExtensions.set_display_name"></a>

#### set_display_name

```python
@classmethod
def set_display_name(cls, track: MovieSceneTrack, name: Text) -> None
```

X.set_display_name(track, name) -> None
Set this track's display name

Args:
    track (MovieSceneTrack): The track to use
    name (Text): The name for this track

<a id="unreal.MovieSceneTrackExtensions.set_color_tint"></a>

#### set_color_tint

```python
@classmethod
def set_color_tint(cls, track: MovieSceneTrack, color_tint: Color) -> None
```

X.set_color_tint(track, color_tint) -> None
Set the color tint for this track

Args:
    track (MovieSceneTrack): The track to set the color tint for
    color_tint (Color): The color tint to set

<a id="unreal.MovieSceneTrackExtensions.remove_section"></a>

#### remove_section

```python
@classmethod
def remove_section(cls, track: MovieSceneTrack,
                   section: MovieSceneSection) -> None
```

X.remove_section(track, section) -> None
Remove the specified section

Args:
    track (MovieSceneTrack): The track to remove the section from, if present
    section (MovieSceneSection): The section to remove

<a id="unreal.MovieSceneTrackExtensions.get_track_row_display_name"></a>

#### get_track_row_display_name

```python
@classmethod
def get_track_row_display_name(cls, track: MovieSceneTrack,
                               row_index: int) -> Text
```

X.get_track_row_display_name(track, row_index) -> Text
Get this track row's display name

Args:
    track (MovieSceneTrack): The track to use
    row_index (int32): The row index for the track

Returns:
    Text: This track's display name

<a id="unreal.MovieSceneTrackExtensions.get_sorting_order"></a>

#### get_sorting_order

```python
@classmethod
def get_sorting_order(cls, track: MovieSceneTrack) -> int
```

X.get_sorting_order(track) -> int32
Get the sorting order for this track

Args:
    track (MovieSceneTrack): The track to get the sorting order from

Returns:
    int32: The sorting order of the requested track

<a id="unreal.MovieSceneTrackExtensions.get_section_to_key"></a>

#### get_section_to_key

```python
@classmethod
def get_section_to_key(cls, track: MovieSceneTrack) -> MovieSceneSection
```

X.get_section_to_key(track) -> MovieSceneSection
Get the section to key for this track

Args:
    track (MovieSceneTrack): The track to get the section to key for

Returns:
    MovieSceneSection: The section to key for the requested track

<a id="unreal.MovieSceneTrackExtensions.get_sections"></a>

#### get_sections

```python
@classmethod
def get_sections(cls, track: MovieSceneTrack) -> Array[MovieSceneSection]
```

X.get_sections(track) -> Array[MovieSceneSection]
Access all this track's sections

Args:
    track (MovieSceneTrack): The track to use

Returns:
    Array[MovieSceneSection]: An array of this track's sections

<a id="unreal.MovieSceneTrackExtensions.get_display_name"></a>

#### get_display_name

```python
@classmethod
def get_display_name(cls, track: MovieSceneTrack) -> Text
```

X.get_display_name(track) -> Text
Get this track's display name

Args:
    track (MovieSceneTrack): The track to use

Returns:
    Text: This track's display name

<a id="unreal.MovieSceneTrackExtensions.get_color_tint"></a>

#### get_color_tint

```python
@classmethod
def get_color_tint(cls, track: MovieSceneTrack) -> Color
```

X.get_color_tint(track) -> Color
Get the color tint for this track

Args:
    track (MovieSceneTrack): The track to get the color tint from

Returns:
    Color: The color tint of the requested track

<a id="unreal.MovieSceneTrackExtensions.add_section"></a>

#### add_section

```python
@classmethod
def add_section(cls, track: MovieSceneTrack) -> MovieSceneSection
```

X.add_section(track) -> MovieSceneSection
Add a new section to this track

Args:
    track (MovieSceneTrack): The track to use

Returns:
    MovieSceneSection: The newly create section if successful

<a id="unreal.MovieSceneFloatVectorTrackExtensions"></a>