## TimecodeProvider Objects

```python
class TimecodeProvider(Object)
```

A class responsible of fetching a timecode from a source.
Note, FApp::GetTimecode and FApp::GetTimecodeFramerate should be used to retrieve
the current system Timecode and Framerate.

**C++ Source:**

- **Module**: Engine
- **File**: TimecodeProvider.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frame_delay`` (float):  [Read-Write] Number of frames to subtract from the qualified frame time when GetDelayedQualifiedFrameTime or GetDelayedTimecode is called.
  see: GetDelayedQualifiedFrameTime, GetDelayedTimecode

<a id="unreal.TimecodeProvider.get_timecode"></a>

#### get_timecode

```python
def get_timecode() -> Timecode
```

x.get_timecode() -> Timecode
Return the frame time converted into a timecode value.

Returns:
    Timecode:

<a id="unreal.TimecodeProvider.get_synchronization_state"></a>

#### get_synchronization_state

```python
def get_synchronization_state() -> TimecodeProviderSynchronizationState
```

x.get_synchronization_state() -> TimecodeProviderSynchronizationState
The state of the TimecodeProvider and if it's currently synchronized and the Timecode and FrameRate getters are valid.

Returns:
    TimecodeProviderSynchronizationState:

<a id="unreal.TimecodeProvider.get_qualified_frame_time"></a>

#### get_qualified_frame_time

```python
def get_qualified_frame_time() -> QualifiedTime
```

x.get_qualified_frame_time() -> QualifiedTime
Return current frame time.
Since it may be called several times per frame, it is suggested to return a cached value.

Returns:
    QualifiedTime:

<a id="unreal.TimecodeProvider.get_frame_rate"></a>

#### get_frame_rate

```python
def get_frame_rate() -> FrameRate
```

x.get_frame_rate() -> FrameRate
Return the frame rate of the frame time.

Returns:
    FrameRate:

<a id="unreal.TimecodeProvider.get_delayed_timecode"></a>

#### get_delayed_timecode

```python
def get_delayed_timecode() -> Timecode
```

x.get_delayed_timecode() -> Timecode
Return the delayed frame time converted into a timecode value.

Returns:
    Timecode:

<a id="unreal.TimecodeProvider.get_delayed_qualified_frame_time"></a>

#### get_delayed_qualified_frame_time

```python
def get_delayed_qualified_frame_time() -> QualifiedTime
```

x.get_delayed_qualified_frame_time() -> QualifiedTime
Return current frame time with FrameDelay applied.
Only assume valid when GetSynchronizationState() returns Synchronized.

Returns:
    QualifiedTime:

<a id="unreal.TimecodeProvider.fetch_timecode"></a>

#### fetch_timecode

```python
def fetch_timecode() -> Optional[QualifiedTime]
```

x.fetch_timecode() -> QualifiedTime or None
Fetch current timecode from its source. e.g. From hardware/network/file/etc.
It is recommended to cache the fetched timecode.

Returns:
    QualifiedTime or None: 

    out_frame_time (QualifiedTime):

<a id="unreal.TimecodeProvider.fetch_and_update"></a>

#### fetch_and_update

```python
def fetch_and_update() -> None
```

x.fetch_and_update() -> None
Update the state of the provider. Call it to ensure timecode and state are updated.
It is suggested to fetch timecode from its source and cache it for the getters.

<a id="unreal.GenlockedTimecodeProvider"></a>