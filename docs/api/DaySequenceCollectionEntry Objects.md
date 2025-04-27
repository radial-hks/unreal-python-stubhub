## DaySequenceCollectionEntry Objects

```python
class DaySequenceCollectionEntry(StructBase)
```

Day Sequence Collection Entry

**C++ Source:**

- **Plugin**: DaySequence
- **Module**: DaySequence
- **File**: DaySequenceCollectionAsset.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bias_offset`` (int32):  [Read-Write] The offset hierarchical bias assigned to this collection entry.
- ``conditions`` (DaySequenceConditionSet):  [Read-Write] The set of conditions which must evaluate to their expected values for this entry to be active.
- ``sequence`` (DaySequence):  [Read-Write] The day sequence asset for this collection entry.

<a id="unreal.DaySequenceCollectionEntry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MVVMBlueprintViewModelContext"></a>