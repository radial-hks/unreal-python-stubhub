## AvaSequenceDirector Objects

```python
class AvaSequenceDirector(LevelSequenceDirector)
```

Ava Sequence Director

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequenceDirector.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``player`` (LevelSequencePlayer):  [Read-Write] Pointer to the player that's playing back this director's sequence. Only valid in game or in PIE/Simulate.

<a id="unreal.AvaSequenceDirector.play_sequences_by_label"></a>

#### play_sequences_by_label

```python
def play_sequences_by_label(sequence_label: Name,
                            play_settings: AvaSequencePlayParams) -> None
```

x.play_sequences_by_label(sequence_label, play_settings) -> None
Play Sequences by Label

Args:
    sequence_label (Name): 
    play_settings (AvaSequencePlayParams):

<a id="unreal.AvaSequenceDirector.play_scheduled_sequences"></a>

#### play_scheduled_sequences

```python
def play_scheduled_sequences() -> None
```

x.play_scheduled_sequences() -> None
Play Scheduled Sequences

<a id="unreal.AvaSequenceDirector.get_playback_object"></a>

#### get_playback_object

```python
def get_playback_object() -> AvaSequencePlaybackObject
```

x.get_playback_object() -> AvaSequencePlaybackObject
Get Playback Object

Returns:
    AvaSequencePlaybackObject:

<a id="unreal.MotionDesignSequenceLibrary"></a>