## UAnimNotifyMirrorInspectionLibrary Objects

```python
class UAnimNotifyMirrorInspectionLibrary(BlueprintFunctionLibrary)
```

A library of commonly used functionality for Notifies related to mirroring, exposed to blueprint.

**C++ Source:**

- **Module**: Engine
- **File**: AnimNotifyMirrorInspectionLibrary.h

<a id="unreal.UAnimNotifyMirrorInspectionLibrary.is_triggered_by_mirrored_animation"></a>

#### is_triggered_by_mirrored_animation

```python
@classmethod
def is_triggered_by_mirrored_animation(
        cls, event_reference: AnimNotifyEventReference) -> bool
```

X.is_triggered_by_mirrored_animation(event_reference) -> bool
Get whether the animation which triggered this notify was mirrored.

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    bool:

<a id="unreal.UAnimNotifyMirrorInspectionLibrary.get_mirror_data_table"></a>

#### get_mirror_data_table

```python
@classmethod
def get_mirror_data_table(
        cls, event_reference: AnimNotifyEventReference) -> MirrorDataTable
```

X.get_mirror_data_table(event_reference) -> MirrorDataTable
If the notify is mirrored, return the mirror data table that was active.

Args:
    event_reference (AnimNotifyEventReference): The event to inspect

Returns:
    MirrorDataTable:

<a id="unreal.UAnimNotifyStateMachineInspectionLibrary"></a>