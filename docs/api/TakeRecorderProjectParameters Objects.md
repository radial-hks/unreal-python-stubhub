## TakeRecorderProjectParameters Objects

```python
class TakeRecorderProjectParameters(StructBase)
```

Take Recorder Project Parameters

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorderParameters.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``default_slate`` (str):  [Read-Write] The default name to use for the Slate information
- ``default_tracks`` (Array[TakeRecorderTrackSettings]):  [Read-Write] List of property names for which movie scene tracks will always record.
- ``record_sources_into_sub_sequences`` (bool):  [Read-Write] If enabled, each Source will be recorded into a separate Sequence and embedded in the Root Sequence will link to them via Subscenes track.
  If disabled, all Sources will be recorded into the Root Sequence, and you will not be able to swap between various takes of specific source
  using the Sequencer Take ui. This can still be done via copying and pasting between sequences if needed.
- ``record_timecode`` (bool):  [Read-Write] If enabled, timecode will be recorded into each actor track
- ``record_to_possessable`` (bool):  [Read-Write] * If enabled, all recorded actors will be recorded to possessable object bindings in Sequencer. If disabled, all recorded actors will be
  * recorded to spawnable object bindings in Sequencer. This can be overridden per actor source.
- ``recording_clock_source`` (UpdateClockSource):  [Read-Write] The clock source to use when recording
- ``root_take_save_dir`` (DirectoryPath):  [Read-Write] The root of the directory in which to save recorded takes.
- ``show_notifications`` (bool):  [Read-Write] Whether to show notification windows or not when recording
- ``start_at_current_timecode`` (bool):  [Read-Write] If enabled, track sections will start at the current timecode. Otherwise, 0.
- ``take_save_dir`` (str):  [Read-Write] The name of the directory in which to save recorded takes. Supports any of the following format specifiers that will be substituted when a take is recorded:
  {day}       - The day of the timestamp for the start of the recording.
  {month}     - The month of the timestamp for the start of the recording.
  {year}      - The year of the timestamp for the start of the recording.
  {hour}      - The hour of the timestamp for the start of the recording.
  {minute}    - The minute of the timestamp for the start of the recording.
  {second}    - The second of the timestamp for the start of the recording.
  {take}      - The take number.
  {slate}     - The slate string.

<a id="unreal.TakeRecorderProjectParameters.__init__"></a>

#### __init__

```python
def __init__(
        root_take_save_dir: DirectoryPath = [""],
        take_save_dir: str = "",
        default_slate: str = "",
        recording_clock_source: UpdateClockSource = UpdateClockSource.TICK,
        start_at_current_timecode: bool = False,
        record_timecode: bool = False,
        record_sources_into_sub_sequences: bool = False,
        record_to_possessable: bool = False,
        show_notifications: bool = False) -> None
```

<a id="unreal.TakeRecorderProjectParameters.root_take_save_dir"></a>

#### root_take_save_dir

```python
@property
def root_take_save_dir() -> DirectoryPath
```

(DirectoryPath):  [Read-Write] The root of the directory in which to save recorded takes.

<a id="unreal.TakeRecorderProjectParameters.root_take_save_dir"></a>

#### root_take_save_dir

```python
@root_take_save_dir.setter
def root_take_save_dir(value: DirectoryPath) -> None
```

<a id="unreal.TakeRecorderProjectParameters.take_save_dir"></a>

#### take_save_dir

```python
@property
def take_save_dir() -> str
```

(str):  [Read-Write] The name of the directory in which to save recorded takes. Supports any of the following format specifiers that will be substituted when a take is recorded:
{day}       - The day of the timestamp for the start of the recording.
{month}     - The month of the timestamp for the start of the recording.
{year}      - The year of the timestamp for the start of the recording.
{hour}      - The hour of the timestamp for the start of the recording.
{minute}    - The minute of the timestamp for the start of the recording.
{second}    - The second of the timestamp for the start of the recording.
{take}      - The take number.
{slate}     - The slate string.

<a id="unreal.TakeRecorderProjectParameters.take_save_dir"></a>

#### take_save_dir

```python
@take_save_dir.setter
def take_save_dir(value: str) -> None
```

<a id="unreal.TakeRecorderProjectParameters.default_slate"></a>

#### default_slate

```python
@property
def default_slate() -> str
```

(str):  [Read-Write] The default name to use for the Slate information

<a id="unreal.TakeRecorderProjectParameters.default_slate"></a>

#### default_slate

```python
@default_slate.setter
def default_slate(value: str) -> None
```

<a id="unreal.TakeRecorderProjectParameters.recording_clock_source"></a>

#### recording_clock_source

```python
@property
def recording_clock_source() -> UpdateClockSource
```

(UpdateClockSource):  [Read-Write] The clock source to use when recording

<a id="unreal.TakeRecorderProjectParameters.recording_clock_source"></a>

#### recording_clock_source

```python
@recording_clock_source.setter
def recording_clock_source(value: UpdateClockSource) -> None
```

<a id="unreal.TakeRecorderProjectParameters.start_at_current_timecode"></a>

#### start_at_current_timecode

```python
@property
def start_at_current_timecode() -> bool
```

(bool):  [Read-Write] If enabled, track sections will start at the current timecode. Otherwise, 0.

<a id="unreal.TakeRecorderProjectParameters.start_at_current_timecode"></a>

#### start_at_current_timecode

```python
@start_at_current_timecode.setter
def start_at_current_timecode(value: bool) -> None
```

<a id="unreal.TakeRecorderProjectParameters.record_timecode"></a>

#### record_timecode

```python
@property
def record_timecode() -> bool
```

(bool):  [Read-Write] If enabled, timecode will be recorded into each actor track

<a id="unreal.TakeRecorderProjectParameters.record_timecode"></a>

#### record_timecode

```python
@record_timecode.setter
def record_timecode(value: bool) -> None
```

<a id="unreal.TakeRecorderProjectParameters.record_sources_into_sub_sequences"></a>

#### record_sources_into_sub_sequences

```python
@property
def record_sources_into_sub_sequences() -> bool
```

(bool):  [Read-Write] If enabled, each Source will be recorded into a separate Sequence and embedded in the Root Sequence will link to them via Subscenes track.
If disabled, all Sources will be recorded into the Root Sequence, and you will not be able to swap between various takes of specific source
using the Sequencer Take ui. This can still be done via copying and pasting between sequences if needed.

<a id="unreal.TakeRecorderProjectParameters.record_sources_into_sub_sequences"></a>

#### record_sources_into_sub_sequences

```python
@record_sources_into_sub_sequences.setter
def record_sources_into_sub_sequences(value: bool) -> None
```

<a id="unreal.TakeRecorderProjectParameters.record_to_possessable"></a>

#### record_to_possessable

```python
@property
def record_to_possessable() -> bool
```

(bool):  [Read-Write] * If enabled, all recorded actors will be recorded to possessable object bindings in Sequencer. If disabled, all recorded actors will be
* recorded to spawnable object bindings in Sequencer. This can be overridden per actor source.

<a id="unreal.TakeRecorderProjectParameters.record_to_possessable"></a>

#### record_to_possessable

```python
@record_to_possessable.setter
def record_to_possessable(value: bool) -> None
```

<a id="unreal.TakeRecorderProjectParameters.show_notifications"></a>

#### show_notifications

```python
@property
def show_notifications() -> bool
```

(bool):  [Read-Write] Whether to show notification windows or not when recording

<a id="unreal.TakeRecorderProjectParameters.show_notifications"></a>

#### show_notifications

```python
@show_notifications.setter
def show_notifications(value: bool) -> None
```

<a id="unreal.TakeRecorderParameters"></a>