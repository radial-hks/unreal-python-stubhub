## TakeRecorderLevelSequenceSource Objects

```python
class TakeRecorderLevelSequenceSource(TakeRecorderSource)
```

Plays level sequence actors when recording starts

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderLevelSequenceSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``level_sequences_to_trigger`` (Array[LevelSequence]):  [Read-Write]
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderLevelSequenceSource.level_sequences_to_trigger"></a>

#### level_sequences_to_trigger

```python
@property
def level_sequences_to_trigger() -> Array[LevelSequence]
```

(Array[LevelSequence]):  [Read-Write]

<a id="unreal.TakeRecorderLevelSequenceSource.level_sequences_to_trigger"></a>

#### level_sequences_to_trigger

```python
@level_sequences_to_trigger.setter
def level_sequences_to_trigger(value: Array[LevelSequence]) -> None
```

<a id="unreal.TakeRecorderLevelVisibilitySourceSettings"></a>