## BlackboardEntry Objects

```python
class BlackboardEntry(StructBase)
```

blackboard entry definition

**C++ Source:**

- **Module**: AIModule
- **File**: BlackboardData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entry_category`` (Name):  [Read-Write]
- ``entry_description`` (str):  [Read-Write] Optional description to explain what this blackboard entry does.
- ``entry_name`` (Name):  [Read-Write]
- ``instance_synced`` (bool):  [Read-Write] if set to true then this field will be synchronized across all instances of this blackboard
- ``key_type`` (BlackboardKeyType):  [Read-Write] key type and additional properties

<a id="unreal.BlackboardEntry.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.IntervalCountdown"></a>