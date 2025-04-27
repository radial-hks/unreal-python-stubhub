## TakeRecorderPanel Objects

```python
class TakeRecorderPanel(Object)
```

Take recorder UI panel interop object

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderPanel.h

<a id="unreal.TakeRecorderPanel.stop_recording"></a>

#### stop_recording

```python
def stop_recording() -> None
```

x.stop_recording() -> None
Stop recording with the current take

<a id="unreal.TakeRecorderPanel.start_recording"></a>

#### start_recording

```python
def start_recording() -> None
```

x.start_recording() -> None
Start recording with the current take

<a id="unreal.TakeRecorderPanel.setup_for_viewing"></a>

#### setup_for_viewing

```python
def setup_for_viewing(level_sequence_asset: LevelSequence) -> None
```

x.setup_for_viewing(level_sequence_asset) -> None
Setup this panel as a viewer for a previously recorded take.

Args:
    level_sequence_asset (LevelSequence):

<a id="unreal.TakeRecorderPanel.setup_for_recording_into_level_sequence"></a>

#### setup_for_recording_into_level_sequence

```python
def setup_for_recording_into_level_sequence(
        level_sequence_asset: LevelSequence) -> None
```

x.setup_for_recording_into_level_sequence(level_sequence_asset) -> None
Setup this panel such that it is ready to start recording using the specified
level sequence asset to record into.

Args:
    level_sequence_asset (LevelSequence):

<a id="unreal.TakeRecorderPanel.setup_for_recording_take_preset"></a>

#### setup_for_recording_take_preset

```python
def setup_for_recording_take_preset(take_preset_asset: TakePreset) -> None
```

x.setup_for_recording_take_preset(take_preset_asset) -> None
Setup this panel such that it is ready to start recording using the specified
take preset as a template for the recording.

Args:
    take_preset_asset (TakePreset):

<a id="unreal.TakeRecorderPanel.setup_for_recording_level_sequence"></a>

#### setup_for_recording_level_sequence

```python
def setup_for_recording_level_sequence(
        level_sequence_asset: LevelSequence) -> None
```

x.setup_for_recording_level_sequence(level_sequence_asset) -> None
Setup this panel such that it is ready to start recording using the specified
level sequence asset as a template for the recording.

Args:
    level_sequence_asset (LevelSequence):

<a id="unreal.TakeRecorderPanel.setup_for_editing"></a>

#### setup_for_editing

```python
def setup_for_editing(take_preset: TakePreset) -> None
```

x.setup_for_editing(take_preset) -> None
Setup this panel as an editor for the specified take preset asset.

Args:
    take_preset (TakePreset):

<a id="unreal.TakeRecorderPanel.set_frame_rate_from_timecode"></a>

#### set_frame_rate_from_timecode

```python
def set_frame_rate_from_timecode(from_timecode: bool) -> None
```

x.set_frame_rate_from_timecode(from_timecode) -> None
Set if the frame rate is set from the Timecode frame rate

Args:
    from_timecode (bool):

<a id="unreal.TakeRecorderPanel.set_frame_rate"></a>

#### set_frame_rate

```python
def set_frame_rate(frame_rate: FrameRate) -> None
```

x.set_frame_rate(frame_rate) -> None
Set the frame rate for this take

Args:
    frame_rate (FrameRate):

<a id="unreal.TakeRecorderPanel.get_take_meta_data"></a>

#### get_take_meta_data

```python
def get_take_meta_data() -> TakeMetaData
```

x.get_take_meta_data() -> TakeMetaData
Access take meta data for this take

Returns:
    TakeMetaData:

<a id="unreal.TakeRecorderPanel.get_sources"></a>

#### get_sources

```python
def get_sources() -> TakeRecorderSources
```

x.get_sources() -> TakeRecorderSources
Access the sources that are to be (or were) used for recording this take

Returns:
    TakeRecorderSources:

<a id="unreal.TakeRecorderPanel.get_mode"></a>

#### get_mode

```python
def get_mode() -> TakeRecorderPanelMode
```

x.get_mode() -> TakeRecorderPanelMode
Get the mode that the panel is currently in

Returns:
    TakeRecorderPanelMode:

<a id="unreal.TakeRecorderPanel.get_level_sequence"></a>

#### get_level_sequence

```python
def get_level_sequence() -> LevelSequence
```

x.get_level_sequence() -> LevelSequence
Access the level sequence for this take

Returns:
    LevelSequence:

<a id="unreal.TakeRecorderPanel.get_last_recorded_level_sequence"></a>

#### get_last_recorded_level_sequence

```python
def get_last_recorded_level_sequence() -> LevelSequence
```

x.get_last_recorded_level_sequence() -> LevelSequence
Access the last level sequence that was recorded

Returns:
    LevelSequence:

<a id="unreal.TakeRecorderPanel.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate
Access the frame rate for this take

Returns:
    FrameRate:

<a id="unreal.TakeRecorderPanel.clear_pending_take"></a>

#### clear_pending_take

```python
def clear_pending_take() -> None
```

x.clear_pending_take() -> None
* Clear the pending take level sequence

<a id="unreal.TakeRecorderPanel.can_start_recording"></a>

#### can_start_recording

```python
def can_start_recording() -> Optional[Text]
```

x.can_start_recording() -> Text or None
Whether the panel is ready to start recording

Returns:
    Text or None: 

    out_error_text (Text):

<a id="unreal.TakeRecorderOverlayWidget"></a>