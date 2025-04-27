## TakeMetaData Objects

```python
class TakeMetaData(Object)
```

Take meta-data that is stored on ULevelSequence assets that are recorded through the Take Recorder.
Meta-data is retrieved through ULevelSequence::FindMetaData<UTakeMetaData>()

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakesCore
- **File**: TakeMetaData.h

<a id="unreal.TakeMetaData.unlock"></a>

#### unlock

```python
def unlock() -> None
```

x.unlock() -> None
Unlock this take if it is read-only, allowing it to be modified once again

<a id="unreal.TakeMetaData.set_timestamp"></a>

#### set_timestamp

```python
def set_timestamp(timestamp: DateTime) -> None
```

x.set_timestamp(timestamp) -> None
Set this take's timestamp
note:: Only valid for takes that have not been locked

Args:
    timestamp (DateTime):

<a id="unreal.TakeMetaData.set_timecode_out"></a>

#### set_timecode_out

```python
def set_timecode_out(timecode_out: Timecode) -> None
```

x.set_timecode_out(timecode_out) -> None
Set this take's timecode out
note:: Only valid for takes that have not been locked

Args:
    timecode_out (Timecode):

<a id="unreal.TakeMetaData.set_timecode_in"></a>

#### set_timecode_in

```python
def set_timecode_in(timecode_in: Timecode) -> None
```

x.set_timecode_in(timecode_in) -> None
Set this take's timecode in
note:: Only valid for takes that have not been locked

Args:
    timecode_in (Timecode):

<a id="unreal.TakeMetaData.set_take_number"></a>

#### set_take_number

```python
def set_take_number(take_number: int, emit_changed: bool = True) -> None
```

x.set_take_number(take_number, emit_changed=True) -> None
Set this take's take number. Take numbers are always clamped to be >= 1.
note:: Only valid for takes that have not been locked

Args:
    take_number (int32): 
    emit_changed (bool): Whether or not to send a take number changed event

<a id="unreal.TakeMetaData.set_slate"></a>

#### set_slate

```python
def set_slate(slate: str, emit_changed: bool = True) -> None
```

x.set_slate(slate, emit_changed=True) -> None
Set the slate for this take and reset its take number to 1
note:: Only valid for takes that have not been locked

Args:
    slate (str): 
    emit_changed (bool): Whether or not to send a slate changed event

<a id="unreal.TakeMetaData.set_preset_origin"></a>

#### set_preset_origin

```python
def set_preset_origin(preset_origin: TakePreset) -> None
```

x.set_preset_origin(preset_origin) -> None
Set the preset on which the take is based
note:: Only valid for takes that have not been locked

Args:
    preset_origin (TakePreset):

<a id="unreal.TakeMetaData.set_level_origin"></a>

#### set_level_origin

```python
def set_level_origin(level_origin: Level) -> None
```

x.set_level_origin(level_origin) -> None
Set the map used to create this recording

Args:
    level_origin (Level):

<a id="unreal.TakeMetaData.set_frame_rate_from_timecode"></a>

#### set_frame_rate_from_timecode

```python
def set_frame_rate_from_timecode(from_timecode: bool) -> None
```

x.set_frame_rate_from_timecode(from_timecode) -> None
Set if we get frame rate from time code

Args:
    from_timecode (bool):

<a id="unreal.TakeMetaData.set_frame_rate"></a>

#### set_frame_rate

```python
def set_frame_rate(frame_rate: FrameRate) -> None
```

x.set_frame_rate(frame_rate) -> None
Set this take's frame-rate
note:: Only valid for takes that have not been locked

Args:
    frame_rate (FrameRate):

<a id="unreal.TakeMetaData.set_duration"></a>

#### set_duration

```python
def set_duration(duration: FrameTime) -> None
```

x.set_duration(duration) -> None
Set this take's duration
note:: Only valid for takes that have not been locked

Args:
    duration (FrameTime):

<a id="unreal.TakeMetaData.set_description"></a>

#### set_description

```python
def set_description(description: str) -> None
```

x.set_description(description) -> None
Set this take's user-provided description
note:: Only valid for takes that have not been locked

Args:
    description (str):

<a id="unreal.TakeMetaData.recorded"></a>

#### recorded

```python
def recorded() -> bool
```

x.recorded() -> bool
Check if this take was recorded (as opposed
to being setup for recording)

Returns:
    bool:

<a id="unreal.TakeMetaData.lock"></a>

#### lock

```python
def lock() -> None
```

x.lock() -> None
Lock this take, causing it to become read-only

<a id="unreal.TakeMetaData.is_locked"></a>

#### is_locked

```python
def is_locked() -> bool
```

x.is_locked() -> bool
Check whether this take is locked

Returns:
    bool:

<a id="unreal.TakeMetaData.get_timestamp"></a>

#### get_timestamp

```python
def get_timestamp() -> DateTime
```

x.get_timestamp() -> DateTime


Returns:
    DateTime: The timestamp for this take

<a id="unreal.TakeMetaData.get_timecode_out"></a>

#### get_timecode_out

```python
def get_timecode_out() -> Timecode
```

x.get_timecode_out() -> Timecode


Returns:
    Timecode: The timecode out for this take

<a id="unreal.TakeMetaData.get_timecode_in"></a>

#### get_timecode_in

```python
def get_timecode_in() -> Timecode
```

x.get_timecode_in() -> Timecode


Returns:
    Timecode: The timecode in for this take

<a id="unreal.TakeMetaData.get_take_number"></a>

#### get_take_number

```python
def get_take_number() -> int
```

x.get_take_number() -> int32


Returns:
    int32: The take number for this take

<a id="unreal.TakeMetaData.get_slate"></a>

#### get_slate

```python
def get_slate() -> str
```

x.get_slate() -> str


Returns:
    str: The slate for this take

<a id="unreal.TakeMetaData.get_preset_origin"></a>

#### get_preset_origin

```python
def get_preset_origin() -> TakePreset
```

x.get_preset_origin() -> TakePreset


Returns:
    TakePreset: The preset on which the take was originally based

<a id="unreal.TakeMetaData.get_level_path"></a>

#### get_level_path

```python
def get_level_path() -> str
```

x.get_level_path() -> str


Returns:
    str: The AssetPath of the Level used to create a Recorded Level Sequence

<a id="unreal.TakeMetaData.get_level_origin"></a>

#### get_level_origin

```python
def get_level_origin() -> Level
```

x.get_level_origin() -> Level


Returns:
    Level: The Map used to create this recording

<a id="unreal.TakeMetaData.get_frame_rate_from_timecode"></a>

#### get_frame_rate_from_timecode

```python
def get_frame_rate_from_timecode() -> bool
```

x.get_frame_rate_from_timecode() -> bool


Returns:
    bool: Get if we get frame rate from time code

<a id="unreal.TakeMetaData.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate


Returns:
    FrameRate: The frame-rate for this take

<a id="unreal.TakeMetaData.get_duration"></a>

#### get_duration

```python
def get_duration() -> FrameTime
```

x.get_duration() -> FrameTime


Returns:
    FrameTime: The duration for this take

<a id="unreal.TakeMetaData.get_description"></a>

#### get_description

```python
def get_description() -> str
```

x.get_description() -> str


Returns:
    str: The user-provided description for this take

<a id="unreal.TakeMetaData.generate_asset_path"></a>

#### generate_asset_path

```python
def generate_asset_path(path_format_string: str) -> str
```

x.generate_asset_path(path_format_string) -> str
Generate the desired asset path for this take meta-data

Args:
    path_format_string (str): 

Returns:
    str:

<a id="unreal.TakePreset"></a>