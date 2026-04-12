## AbilityTask\_WaitOverlap Objects

```python
class AbilityTask_WaitOverlap(AbilityTask)
```

Fixme: this is still incomplete and probablyh not what most games want for melee systems.
        -Only actually activates on Blocking hits
        -Uses first PrimitiveComponent instead of being able to specify arbitrary component.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: AbilityTask_WaitOverlap.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_overlap`` (WaitOverlapDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitOverlap.on_overlap"></a>

#### on\_overlap

```python
@property
def on_overlap() -> WaitOverlapDelegate
```

(WaitOverlapDelegate):  [Read-Write]

<a id="unreal.AbilityTask_WaitOverlap.on_overlap"></a>

#### on\_overlap

```python
@on_overlap.setter
def on_overlap(value: WaitOverlapDelegate) -> None
```

<a id="unreal.AbilityTask_WaitTargetData"></a>