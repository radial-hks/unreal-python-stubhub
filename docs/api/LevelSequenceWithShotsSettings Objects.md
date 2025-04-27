## LevelSequenceWithShotsSettings Objects

```python
class LevelSequenceWithShotsSettings(Object)
```

Level Sequence With Shots Settings.

**C++ Source:**

- **Plugin**: LevelSequenceEditor
- **Module**: LevelSequenceEditor
- **File**: LevelSequenceEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_path`` (DirectoryPath):  [Read-Write] Sequence With Shots path.
- ``instance_sub_sequences`` (bool):  [Read-Write] Whether to instance sub sequences based on the first created sub sequences.
- ``name`` (str):  [Read-Write] Sequence With Shots name.
- ``num_shots`` (uint32):  [Read-Write] Sequence With Shots number of shots.
- ``sequence_to_duplicate`` (LevelSequence):  [Read-Write] Sequence With Shots level sequence to duplicate when creating shots.
- ``sub_sequence_names`` (Array[Name]):  [Read-Write] Array of sub sequence names, each will result in a level sequence asset in the shot.
- ``suffix`` (str):  [Read-Write] Sequence With Shots suffix.

<a id="unreal.LevelSequenceWithShotsSettings.sub_sequence_names"></a>

#### sub_sequence_names

```python
@property
def sub_sequence_names() -> Array[Name]
```

(Array[Name]):  [Read-Write] Array of sub sequence names, each will result in a level sequence asset in the shot.

<a id="unreal.LevelSequenceWithShotsSettings.sub_sequence_names"></a>

#### sub_sequence_names

```python
@sub_sequence_names.setter
def sub_sequence_names(value: Array[Name]) -> None
```

<a id="unreal.MediaPlate"></a>