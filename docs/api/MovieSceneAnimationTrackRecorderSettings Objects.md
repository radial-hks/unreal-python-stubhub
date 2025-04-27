## MovieSceneAnimationTrackRecorderSettings Objects

```python
class MovieSceneAnimationTrackRecorderSettings(
        MovieSceneAnimationTrackRecorderEditorSettings)
```

Movie Scene Animation Track Recorder Settings

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

<a id="unreal.MovieSceneParticleTrackRecorder"></a>