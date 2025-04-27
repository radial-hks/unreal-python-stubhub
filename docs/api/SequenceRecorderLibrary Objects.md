## SequenceRecorderLibrary Objects

```python
class SequenceRecorderLibrary(BlueprintFunctionLibrary)
```

Sequence Recorder Blueprint Library

**C++ Source:**

- **Module**: SequenceRecorder
- **File**: SequenceRecorderBlueprintLibrary.h

<a id="unreal.SequenceRecorderLibrary.stop_recording_sequence"></a>

#### stop_recording_sequence

```python
@classmethod
def stop_recording_sequence(cls) -> None
```

X.stop_recording_sequence() -> None
Stop recording the current sequence, if any

<a id="unreal.SequenceRecorderLibrary.start_recording_sequence"></a>

#### start_recording_sequence

```python
@classmethod
def start_recording_sequence(cls, actors_to_record: Array[Actor]) -> None
```

X.start_recording_sequence(actors_to_record) -> None
Start recording the passed-in actors to a level sequence.

Args:
    actors_to_record (Array[Actor]): The actors to record

<a id="unreal.SequenceRecorderLibrary.is_recording_sequence"></a>

#### is_recording_sequence

```python
@classmethod
def is_recording_sequence(cls) -> bool
```

X.is_recording_sequence() -> bool
Are we currently recording a sequence

Returns:
    bool:

<a id="unreal.CurveEditorFilterBase"></a>