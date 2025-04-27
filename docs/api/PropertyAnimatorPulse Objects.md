## PropertyAnimatorPulse Objects

```python
class PropertyAnimatorPulse(PropertyAnimatorNumericBase)
```

Applies an additive pulse movement with various options on supported float properties

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorPulse.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``active_time_source`` (PropertyAnimatorCoreTimeSourceBase):  [Read-Only] Active time source with its options, determined by its name
- ``animator_display_name`` (Name):  [Read-Only] Display name as title property for component array, hide it but must be visible to editor for array title property
- ``animator_enabled`` (bool):  [Read-Write] Enable control of properties linked to this Animator
- ``cycle_duration`` (float):  [Read-Write] Duration of one cycle for the effect = period of the effect
- ``cycle_gap_duration`` (float):  [Read-Write] Time gap between each cycle
- ``cycle_mode`` (PropertyAnimatorCycleMode):  [Read-Write] Cycle mode for the effect
- ``easing_function`` (PropertyAnimatorEasingFunction):  [Read-Write] The easing function to use to modify the base effect
- ``easing_type`` (PropertyAnimatorEasingType):  [Read-Write] The type of effect for easing function
- ``linked_properties`` (Array[PropertyAnimatorCoreContext]):  [Read-Write] Context for properties linked to this Animator
- ``magnitude`` (float):  [Read-Write] Magnitude for the effect on all properties
- ``override_time_source`` (bool):  [Read-Write] Use the global time source or override it on this animator
- ``random_time_offset`` (bool):  [Read-Write] Use random time offset to add variation in animation
- ``seed`` (int32):  [Read-Write] Seed to generate per property time offset
- ``time_source_name`` (Name):  [Read-Write] The time source to use
- ``time_sources_instances`` (Map[Name, PropertyAnimatorCoreTimeSourceBase]):  [Read-Write]
  deprecated: Use TimeSources instead

<a id="unreal.PropertyAnimatorPulse.easing_function"></a>

#### easing_function

```python
@property
def easing_function() -> PropertyAnimatorEasingFunction
```

(PropertyAnimatorEasingFunction):  [Read-Write] The easing function to use to modify the base effect

<a id="unreal.PropertyAnimatorPulse.easing_function"></a>

#### easing_function

```python
@easing_function.setter
def easing_function(value: PropertyAnimatorEasingFunction) -> None
```

<a id="unreal.PropertyAnimatorPulse.easing_type"></a>

#### easing_type

```python
@property
def easing_type() -> PropertyAnimatorEasingType
```

(PropertyAnimatorEasingType):  [Read-Write] The type of effect for easing function

<a id="unreal.PropertyAnimatorPulse.easing_type"></a>

#### easing_type

```python
@easing_type.setter
def easing_type(value: PropertyAnimatorEasingType) -> None
```

<a id="unreal.PropertyControllerBlink"></a>