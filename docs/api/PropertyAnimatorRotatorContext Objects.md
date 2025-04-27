## PropertyAnimatorRotatorContext Objects

```python
class PropertyAnimatorRotatorContext(PropertyAnimatorCoreContext)
```

Property context used by animator for rotator properties

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorRotatorContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``amplitude_max`` (Rotator):  [Read-Write] The maximum value should be remapped to that values
- ``amplitude_min`` (Rotator):  [Read-Write] The minimum value should be remapped to that values
- ``animated`` (bool):  [Read-Write] Animation is enabled for this property
- ``converter_rule`` (InstancedStruct):  [Read-Write] If a converter is used, rules may be used to convert the property
- ``magnitude`` (float):  [Read-Write] Magnitude of the effect on this property
- ``mode`` (PropertyAnimatorCoreMode):  [Read-Write] Current mode used for this property
- ``resolver`` (PropertyAnimatorCoreResolver):  [Read-Only] Custom resolver for the property
- ``time_offset`` (double):  [Read-Write] Time offset to evaluate this property

<a id="unreal.PropertyAnimatorSoundWave"></a>