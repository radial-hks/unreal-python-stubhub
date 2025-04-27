## PropertyAnimatorCoreContext Objects

```python
class PropertyAnimatorCoreContext(Object)
```

Context for properties linked to an animator

**C++ Source:**

- **Plugin**: PropertyAnimatorCore
- **Module**: PropertyAnimatorCore
- **File**: PropertyAnimatorCoreContext.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animated`` (bool):  [Read-Write] Animation is enabled for this property
- ``converter_rule`` (InstancedStruct):  [Read-Write] If a converter is used, rules may be used to convert the property
- ``magnitude`` (float):  [Read-Write] Magnitude of the effect on this property
- ``mode`` (PropertyAnimatorCoreMode):  [Read-Write] Current mode used for this property
- ``resolver`` (PropertyAnimatorCoreResolver):  [Read-Only] Custom resolver for the property
- ``time_offset`` (double):  [Read-Write] Time offset to evaluate this property

<a id="unreal.PropertyAnimatorCorePropertyPreset"></a>