## AvaSequencePlaybackObject Objects

```python
class AvaSequencePlaybackObject(Interface)
```

Ava Sequence Playback Object

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheSequence
- **File**: AvaSequencePlaybackObject.h

<a id="unreal.AvaSequencePlaybackObject.play_sequences_by_tag"></a>

#### play_sequences_by_tag

```python
def play_sequences_by_tag(
        tag_handle: AvaTagHandle, exact_match: bool,
        play_settings: AvaSequencePlayParams) -> Array[AvaSequencePlayer]
```

x.play_sequences_by_tag(tag_handle, exact_match, play_settings) -> Array[AvaSequencePlayer]
Plays all the Sequences that match the given gameplay tag(s)

Args:
    tag_handle (AvaTagHandle): the tag to match
    exact_match (bool): whether to only consider sequences that have the tag exactly
    play_settings (AvaSequencePlayParams): the play settings to use for playback

Returns:
    Array[AvaSequencePlayer]: an array of the Sequence Players with only valid entries kept

<a id="unreal.AvaSequencePlaybackObject.play_sequences_by_soft_reference"></a>

#### play_sequences_by_soft_reference

```python
def play_sequences_by_soft_reference(
        sequences: Array[AvaSequence],
        play_settings: AvaSequencePlayParams) -> Array[AvaSequencePlayer]
```

x.play_sequences_by_soft_reference(sequences, play_settings) -> Array[AvaSequencePlayer]
Plays multiple Sequences by their Soft Reference

Args:
    sequences (Array[AvaSequence]): the array of soft reference sequences to play
    play_settings (AvaSequencePlayParams): the play settings to use for playback

Returns:
    Array[AvaSequencePlayer]: an array of the Sequence Players with possible invalid/null entries kept so that each Player matches in Index with the input Sequence it is playing

<a id="unreal.AvaSequencePlaybackObject.play_sequences_by_labels"></a>

#### play_sequences_by_labels

```python
def play_sequences_by_labels(
        sequence_labels: Array[Name],
        play_settings: AvaSequencePlayParams) -> Array[AvaSequencePlayer]
```

x.play_sequences_by_labels(sequence_labels, play_settings) -> Array[AvaSequencePlayer]
Plays multiple Sequences by an array of sequence labels

Args:
    sequence_labels (Array[Name]): the array of sequence labels to play
    play_settings (AvaSequencePlayParams): the play settings to use for playback

Returns:
    Array[AvaSequencePlayer]: an array of the Sequence Players with possible invalid/null entries kept so that each Player matches in Index with the input Sequence it is playing

<a id="unreal.AvaSequencePlaybackObject.play_sequences_by_label"></a>

#### play_sequences_by_label

```python
def play_sequences_by_label(
        sequence_label: Name,
        play_settings: AvaSequencePlayParams) -> Array[AvaSequencePlayer]
```

x.play_sequences_by_label(sequence_label, play_settings) -> Array[AvaSequencePlayer]
Plays all the sequences that have the provided label

Args:
    sequence_label (Name): the label of the sequences to play
    play_settings (AvaSequencePlayParams): the play settings to use for playback

Returns:
    Array[AvaSequencePlayer]: an array of the Sequence Players with possible invalid/null entries kept so that each Player matches in Index with the input Sequence it is playing

<a id="unreal.AvaSequencePlaybackObject.play_sequence_by_soft_reference"></a>

#### play_sequence_by_soft_reference

```python
def play_sequence_by_soft_reference(
        sequence: AvaSequence,
        play_settings: AvaSequencePlayParams) -> AvaSequencePlayer
```

x.play_sequence_by_soft_reference(sequence, play_settings) -> AvaSequencePlayer
Plays a single sequence by its soft reference

Args:
    sequence (AvaSequence): soft reference of the sequence to play
    play_settings (AvaSequencePlayParams): the play settings to use for playback

Returns:
    AvaSequencePlayer: the player instantiated for the Sequence, or null if Sequence was not valid for playback

<a id="unreal.AvaSequencePlaybackObject.play_scheduled_sequences"></a>

#### play_scheduled_sequences

```python
def play_scheduled_sequences() -> Array[AvaSequencePlayer]
```

x.play_scheduled_sequences() -> Array[AvaSequencePlayer]
Plays the Scheduled Sequences with the Scheduled Play Settings

Returns:
    Array[AvaSequencePlayer]: an array of the Sequence Players with possible invalid/null entries kept so that each Player matches in Index with the Scheduled Sequence it is playing

<a id="unreal.AvaSequencePlaybackObject.has_active_sequence_players"></a>

#### has_active_sequence_players

```python
def has_active_sequence_players() -> bool
```

x.has_active_sequence_players() -> bool
Returns true if there are any Active Sequence Players

Returns:
    bool:

<a id="unreal.AvaSequencePlaybackObject.get_all_sequence_players"></a>

#### get_all_sequence_players

```python
def get_all_sequence_players() -> Array[AvaSequencePlayer]
```

x.get_all_sequence_players() -> Array[AvaSequencePlayer]
Retrieves all Active Sequence Players

Returns:
    Array[AvaSequencePlayer]:

<a id="unreal.AvaSequencePlaybackObject.continue_sequences_by_tag"></a>

#### continue_sequences_by_tag

```python
def continue_sequences_by_tag(tag_handle: AvaTagHandle,
                              exact_match: bool) -> Array[AvaSequencePlayer]
```

x.continue_sequences_by_tag(tag_handle, exact_match) -> Array[AvaSequencePlayer]
Triggers Continues in all the sequences matching the provided tag

Args:
    tag_handle (AvaTagHandle): the tag to match
    exact_match (bool): whether to only consider sequences that have the tag exactly

Returns:
    Array[AvaSequencePlayer]: the array of the Sequence Players with only valid entries that fired the continue

<a id="unreal.AvaSequencePlaybackObject.continue_sequences_by_labels"></a>

#### continue_sequences_by_labels

```python
def continue_sequences_by_labels(
        sequence_labels: Array[Name]) -> Array[AvaSequencePlayer]
```

x.continue_sequences_by_labels(sequence_labels) -> Array[AvaSequencePlayer]
Triggers Continues in multiple playing sequences given by an array of sequence labels

Args:
    sequence_labels (Array[Name]): the array of sequence labels to trigger continue (must be an active sequence playing)

Returns:
    Array[AvaSequencePlayer]: the sequence player array that fired the continue. It might have possible invalid/null entries so that each Player matches in Index with the input Sequence labels

<a id="unreal.AvaSequencePlaybackObject.continue_sequences_by_label"></a>

#### continue_sequences_by_label

```python
def continue_sequences_by_label(
        sequence_label: Name) -> Array[AvaSequencePlayer]
```

x.continue_sequences_by_label(sequence_label) -> Array[AvaSequencePlayer]
Triggers Continue for the playing sequences that match the given label

Args:
    sequence_label (Name): the label of the sequences to continue

Returns:
    Array[AvaSequencePlayer]: the sequence players that fired the continue, or null if there were no active players

<a id="unreal.AvaSequencePlayer"></a>