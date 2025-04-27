## AnimSequenceLevelSequenceLink Objects

```python
class AnimSequenceLevelSequenceLink(AssetUserData)
```

Link To Level Sequence That may be driving the anim sequence

**C++ Source:**

- **Module**: LevelSequence
- **File**: AnimSequenceLevelSequenceLink.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``path_to_level_sequence`` (SoftObjectPath):  [Read-Write]
- ``skel_track_guid`` (Guid):  [Read-Write]

<a id="unreal.AnimSequenceLevelSequenceLink.skel_track_guid"></a>

#### skel_track_guid

```python
@property
def skel_track_guid() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.AnimSequenceLevelSequenceLink.skel_track_guid"></a>

#### skel_track_guid

```python
@skel_track_guid.setter
def skel_track_guid(value: Guid) -> None
```

<a id="unreal.AnimSequenceLevelSequenceLink.path_to_level_sequence"></a>

#### path_to_level_sequence

```python
@property
def path_to_level_sequence() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.AnimSequenceLevelSequenceLink.path_to_level_sequence"></a>

#### path_to_level_sequence

```python
@path_to_level_sequence.setter
def path_to_level_sequence(value: SoftObjectPath) -> None
```

<a id="unreal.LevelSequence"></a>