## TakeRecorder Objects

```python
class TakeRecorder(Object)
```

Take Recorder

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorder
- **File**: TakeRecorder.h

<a id="unreal.TakeRecorder.get_state"></a>

#### get_state

```python
def get_state() -> TakeRecorderState
```

x.get_state() -> TakeRecorderState
Get the current state of this recorder

Returns:
    TakeRecorderState:

<a id="unreal.TakeRecorder.get_sequence"></a>

#### get_sequence

```python
def get_sequence() -> LevelSequence
```

x.get_sequence() -> LevelSequence
Access the sequence asset that this recorder is recording into

Returns:
    LevelSequence:

<a id="unreal.TakeRecorder.get_countdown_seconds"></a>

#### get_countdown_seconds

```python
def get_countdown_seconds() -> float
```

x.get_countdown_seconds() -> float
Access the number of seconds remaining before this recording will start

Returns:
    float:

<a id="unreal.TakeRecorderBlueprintLibrary"></a>