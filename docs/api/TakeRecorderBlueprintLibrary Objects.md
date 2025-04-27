## TakeRecorderBlueprintLibrary Objects

```python
class TakeRecorderBlueprintLibrary(BlueprintFunctionLibrary)
```

Take Recorder Blueprint Library

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderBlueprintLibrary.h

<a id="unreal.TakeRecorderBlueprintLibrary.stop_recording"></a>

#### stop_recording

```python
@classmethod
def stop_recording(cls) -> None
```

X.stop_recording() -> None
Stop recording if there is a recorder currently active

<a id="unreal.TakeRecorderBlueprintLibrary.start_recording"></a>

#### start_recording

```python
@classmethod
def start_recording(cls, level_sequence: LevelSequence,
                    sources: TakeRecorderSources, meta_data: TakeMetaData,
                    parameters: TakeRecorderParameters) -> TakeRecorder
```

X.start_recording(level_sequence, sources, meta_data, parameters) -> TakeRecorder
Start a new recording using the specified parameters. Will fail if a recording is currently in progress

Args:
    level_sequence (LevelSequence): The base level sequence to use for the recording. Will be played back during the recording and duplicated to create the starting point for the resulting asset.
    sources (TakeRecorderSources): The sources to use for the recording
    meta_data (TakeMetaData): Meta-data pertaining to this recording, duplicated into the resulting recorded sequence
    parameters (TakeRecorderParameters): Configurable parameters for this recorder instance

Returns:
    TakeRecorder: The recorder responsible for the recording, or None if a a recording could not be started

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_stopped"></a>

#### set_on_take_recorder_stopped

```python
@classmethod
def set_on_take_recorder_stopped(
        cls, on_take_recorder_stopped: OnTakeRecorderStopped) -> None
```

X.set_on_take_recorder_stopped(on_take_recorder_stopped) -> None
Set on Take Recorder Stopped
deprecated: Please use TakeRecorderSubsystem::TakeRecorderStopped

Args:
    on_take_recorder_stopped (OnTakeRecorderStopped):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_started"></a>

#### set_on_take_recorder_started

```python
@classmethod
def set_on_take_recorder_started(
        cls, on_take_recorder_started: OnTakeRecorderStarted) -> None
```

X.set_on_take_recorder_started(on_take_recorder_started) -> None
Set on Take Recorder Started
deprecated: Please use TakeRecorderSubsystem::TakeRecorderStarted

Args:
    on_take_recorder_started (OnTakeRecorderStarted):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_pre_initialize"></a>

#### set_on_take_recorder_pre_initialize

```python
@classmethod
def set_on_take_recorder_pre_initialize(
        cls,
        on_take_recorder_pre_initialize: OnTakeRecorderPreInitialize) -> None
```

X.set_on_take_recorder_pre_initialize(on_take_recorder_pre_initialize) -> None
Set on Take Recorder Pre Initialize
deprecated: Please use TakeRecorderSubsystem::TakeRecorderPreInitialize

Args:
    on_take_recorder_pre_initialize (OnTakeRecorderPreInitialize):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_panel_changed"></a>

#### set_on_take_recorder_panel_changed

```python
@classmethod
def set_on_take_recorder_panel_changed(
        cls,
        on_take_recorder_panel_changed: OnTakeRecorderPanelChanged) -> None
```

X.set_on_take_recorder_panel_changed(on_take_recorder_panel_changed) -> None
Called when a Take Panel is constructed or destroyed.

Args:
    on_take_recorder_panel_changed (OnTakeRecorderPanelChanged):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_marked_frame_added"></a>

#### set_on_take_recorder_marked_frame_added

```python
@classmethod
def set_on_take_recorder_marked_frame_added(
    cls, on_take_recorder_marked_frame_added: OnTakeRecorderMarkedFrameAdded
) -> None
```

X.set_on_take_recorder_marked_frame_added(on_take_recorder_marked_frame_added) -> None
Set on Take Recorder Marked Frame Added
deprecated: Please use TakeRecorderSubsystem::TakeRecorderMarkedFrameAdded

Args:
    on_take_recorder_marked_frame_added (OnTakeRecorderMarkedFrameAdded):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_finished"></a>

#### set_on_take_recorder_finished

```python
@classmethod
def set_on_take_recorder_finished(
        cls, on_take_recorder_finished: OnTakeRecorderFinished) -> None
```

X.set_on_take_recorder_finished(on_take_recorder_finished) -> None
Set on Take Recorder Finished
deprecated: Please use TakeRecorderSubsystem::TakeRecorderFinished

Args:
    on_take_recorder_finished (OnTakeRecorderFinished):

<a id="unreal.TakeRecorderBlueprintLibrary.set_on_take_recorder_cancelled"></a>

#### set_on_take_recorder_cancelled

```python
@classmethod
def set_on_take_recorder_cancelled(
        cls, on_take_recorder_cancelled: OnTakeRecorderCancelled) -> None
```

X.set_on_take_recorder_cancelled(on_take_recorder_cancelled) -> None
Set on Take Recorder Cancelled
deprecated: Please use TakeRecorderSubsystem::TakeRecorderCancelled

Args:
    on_take_recorder_cancelled (OnTakeRecorderCancelled):

<a id="unreal.TakeRecorderBlueprintLibrary.set_default_parameters"></a>

#### set_default_parameters

```python
@classmethod
def set_default_parameters(cls,
                           default_parameters: TakeRecorderParameters) -> None
```

X.set_default_parameters(default_parameters) -> None
Set the default recorder parameters

Args:
    default_parameters (TakeRecorderParameters):

<a id="unreal.TakeRecorderBlueprintLibrary.open_take_recorder_panel"></a>

#### open_take_recorder_panel

```python
@classmethod
def open_take_recorder_panel(cls) -> TakeRecorderPanel
```

X.open_take_recorder_panel() -> TakeRecorderPanel
Get the currently open take recorder panel, if one is open, opening a new one if not

Returns:
    TakeRecorderPanel:

<a id="unreal.TakeRecorderBlueprintLibrary.is_take_recorder_enabled"></a>

#### is_take_recorder_enabled

```python
@classmethod
def is_take_recorder_enabled(cls) -> bool
```

X.is_take_recorder_enabled() -> bool
Is the Take Recorder enabled in the build

Returns:
    bool:

<a id="unreal.TakeRecorderBlueprintLibrary.is_recording"></a>

#### is_recording

```python
@classmethod
def is_recording(cls) -> bool
```

X.is_recording() -> bool
Check whether a recording is currently active

Returns:
    bool:

<a id="unreal.TakeRecorderBlueprintLibrary.get_take_recorder_panel"></a>

#### get_take_recorder_panel

```python
@classmethod
def get_take_recorder_panel(cls) -> TakeRecorderPanel
```

X.get_take_recorder_panel() -> TakeRecorderPanel
Get the currently open take recorder panel, if one is open

Returns:
    TakeRecorderPanel:

<a id="unreal.TakeRecorderBlueprintLibrary.get_default_parameters"></a>

#### get_default_parameters

```python
@classmethod
def get_default_parameters(cls) -> TakeRecorderParameters
```

X.get_default_parameters() -> TakeRecorderParameters
Get the default recorder parameters according to the project and user settings

Returns:
    TakeRecorderParameters:

<a id="unreal.TakeRecorderBlueprintLibrary.get_active_recorder"></a>

#### get_active_recorder

```python
@classmethod
def get_active_recorder(cls) -> TakeRecorder
```

X.get_active_recorder() -> TakeRecorder
Retrieve the currently active recorder, or None if there none are active

Returns:
    TakeRecorder:

<a id="unreal.TakeRecorderBlueprintLibrary.cancel_recording"></a>

#### cancel_recording

```python
@classmethod
def cancel_recording(cls) -> None
```

X.cancel_recording() -> None
Cancel recording if there is a recorder currently active

<a id="unreal.TakeRecorderPanel"></a>