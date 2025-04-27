## WaveTableSettings Objects

```python
class WaveTableSettings(StructBase)
```

Wave Table Settings

**C++ Source:**

- **Plugin**: WaveTable
- **Module**: WaveTable
- **File**: WaveTableSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel_index`` (int32):  [Read-Write] Index of channel in file to build WaveTable from (wraps if channel is greater than number in file)
- ``fade_in`` (float):  [Read-Write] Percent to fade in over.
- ``fade_out`` (float):  [Read-Write] Percent to fade out over.
- ``file_path`` (FilePath):  [Read-Write] File to import
- ``normalize`` (bool):  [Read-Write] Whether or not to normalize the WaveTable.
- ``phase`` (float):  [Read-Write] Percent to phase shift of table
- ``remove_offset`` (bool):  [Read-Write] Whether or not to remove offset from original file
  (analogous to "DC offset" in circuit theory).
- ``source_data`` (WaveTableData):  [Read-Write] Source data last imported from the source file
- ``source_sample_rate`` (int32):  [Read-Only] Source sample rate from last imported source file
- ``tail`` (float):  [Read-Write] Percent to remove from end of sampled WaveTable.
- ``top`` (float):  [Read-Write] Percent to remove from beginning of sampled WaveTable.

<a id="unreal.WaveTableSettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PCGKernelAttributeKey"></a>