## MovieSceneAnimationTrackRecorderEditorSettings Objects

```python
class MovieSceneAnimationTrackRecorderEditorSettings(
        MovieSceneTrackRecorderSettings)
```

Movie Scene Animation Track Recorder Editor Settings

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeTrackRecorders
- **File**: MovieSceneAnimationTrackRecorderSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation_asset_name`` (str):  [Read-Write] The name of the animation asset.
  Supports any of the following format specifiers that will be substituted when a take is recorded:
  {day}       - The day of the timestamp for the start of the recording.
  {month}     - The month of the timestamp for the start of the recording.
  {year}      - The year of the timestamp for the start of the recording.
  {hour}      - The hour of the timestamp for the start of the recording.
  {minute}    - The minute of the timestamp for the start of the recording.
  {second}    - The second of the timestamp for the start of the recording.
  {take}      - The take number.
  {slate}     - The slate string.
  {actor}     - The name of the actor being recorded.
- ``animation_sub_directory`` (str):  [Read-Write] The name of the subdirectory animations will be placed in. Leave this empty to place into the same directory as the sequence base path.
  Supports any of the following format specifiers that will be substituted when a take is recorded:
  {day}       - The day of the timestamp for the start of the recording.
  {month}     - The month of the timestamp for the start of the recording.
  {year}      - The year of the timestamp for the start of the recording.
  {hour}      - The hour of the timestamp for the start of the recording.
  {minute}    - The minute of the timestamp for the start of the recording.
  {second}    - The second of the timestamp for the start of the recording.
  {take}      - The take number.
  {slate}     - The slate string.
  {actor}     - The name of the actor being recorded.
- ``animation_track_name`` (Text):  [Read-Write] Name of the recorded animation track.
- ``interp_mode`` (RichCurveInterpMode):  [Read-Write] Interpolation mode for the recorded keys.
- ``remove_root_animation`` (bool):  [Read-Write] If true we remove the root animation and move it to a transform track, if false we leave it on the root bone in the anim sequence
- ``tangent_mode`` (RichCurveTangentMode):  [Read-Write] Tangent mode for the recorded keys.
- ``timecode_bone_method`` (TimecodeBoneMethod):  [Read-Write] The method to record timecode values onto bones

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_track_name"></a>

#### animation_track_name

```python
@property
def animation_track_name() -> Text
```

(Text):  [Read-Write] Name of the recorded animation track.

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_track_name"></a>

#### animation_track_name

```python
@animation_track_name.setter
def animation_track_name(value: Text) -> None
```

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_asset_name"></a>

#### animation_asset_name

```python
@property
def animation_asset_name() -> str
```

(str):  [Read-Write] The name of the animation asset.
Supports any of the following format specifiers that will be substituted when a take is recorded:
{day}       - The day of the timestamp for the start of the recording.
{month}     - The month of the timestamp for the start of the recording.
{year}      - The year of the timestamp for the start of the recording.
{hour}      - The hour of the timestamp for the start of the recording.
{minute}    - The minute of the timestamp for the start of the recording.
{second}    - The second of the timestamp for the start of the recording.
{take}      - The take number.
{slate}     - The slate string.
{actor}     - The name of the actor being recorded.

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_asset_name"></a>

#### animation_asset_name

```python
@animation_asset_name.setter
def animation_asset_name(value: str) -> None
```

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_sub_directory"></a>

#### animation_sub_directory

```python
@property
def animation_sub_directory() -> str
```

(str):  [Read-Write] The name of the subdirectory animations will be placed in. Leave this empty to place into the same directory as the sequence base path.
Supports any of the following format specifiers that will be substituted when a take is recorded:
{day}       - The day of the timestamp for the start of the recording.
{month}     - The month of the timestamp for the start of the recording.
{year}      - The year of the timestamp for the start of the recording.
{hour}      - The hour of the timestamp for the start of the recording.
{minute}    - The minute of the timestamp for the start of the recording.
{second}    - The second of the timestamp for the start of the recording.
{take}      - The take number.
{slate}     - The slate string.
{actor}     - The name of the actor being recorded.

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.animation_sub_directory"></a>

#### animation_sub_directory

```python
@animation_sub_directory.setter
def animation_sub_directory(value: str) -> None
```

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.remove_root_animation"></a>

#### remove_root_animation

```python
@property
def remove_root_animation() -> bool
```

(bool):  [Read-Write] If true we remove the root animation and move it to a transform track, if false we leave it on the root bone in the anim sequence

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.remove_root_animation"></a>

#### remove_root_animation

```python
@remove_root_animation.setter
def remove_root_animation(value: bool) -> None
```

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.timecode_bone_method"></a>

#### timecode_bone_method

```python
@property
def timecode_bone_method() -> TimecodeBoneMethod
```

(TimecodeBoneMethod):  [Read-Write] The method to record timecode values onto bones

<a id="unreal.MovieSceneAnimationTrackRecorderEditorSettings.timecode_bone_method"></a>

#### timecode_bone_method

```python
@timecode_bone_method.setter
def timecode_bone_method(value: TimecodeBoneMethod) -> None
```

<a id="unreal.MovieSceneAnimationTrackRecorderSettings"></a>