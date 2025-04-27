## PropertyAnimatorBounce Objects

```python
class PropertyAnimatorBounce(PropertyAnimatorNumericBase)
```

Applies an additive bounce movement with various options on supported float properties

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorBounce.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animator_display_name`` (Name):  [Read-Only] Display name as title property for component array, hide it but must be visible to editor for array title property
- ``animator_enabled`` (bool):  [Read-Write] Enable control of properties linked to this Animator
- ``cycle_duration`` (float):  [Read-Write] Duration of one cycle for the effect = period of the effect
- ``cycle_gap_duration`` (float):  [Read-Write] Time gap between each cycle
- ``cycle_mode`` (PropertyAnimatorCycleMode):  [Read-Write] Cycle mode for the effect
- ``invert_effect`` (bool):  [Read-Write] Invert the effect result
- ``linked_properties`` (Array[PropertyAnimatorCoreContext]):  [Read-Write] Context for properties linked to this Animator
- ``magnitude`` (float):  [Read-Write] Magnitude for the effect on all properties
- ``override_time_source`` (bool):  [Read-Write] Use the global time source or override it on this animator
- ``random_time_offset`` (bool):  [Read-Write] Use random time offset to add variation in animation
- ``seed`` (int32):  [Read-Write] Seed to generate per property time offset
- ``time_source_name`` (Name):  [Read-Write] The time source to use
- ``time_sources_instances`` (Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
  deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorBounce.invert_effect"></a>

#### invert_effect

```python
@property
def invert_effect() -> bool
```

(bool):  [Read-Write] Invert the effect result

<a id="unreal.PropertyAnimatorBounce.invert_effect"></a>

#### invert_effect

```python
@invert_effect.setter
def invert_effect(value: bool) -> None
```

<a id="unreal.PropertyControllerBounce"></a>