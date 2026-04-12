## CustomCalculationBasedFloat Objects

```python
class CustomCalculationBasedFloat(StructBase)
```

Structure to encapsulate magnitudes that are calculated via custom calculation

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``calculation_class_magnitude`` (type(Class)):  [Read-Write]
- ``coefficient`` (ScalableFloat):  [Read-Write] Coefficient to the custom calculation
- ``final_lookup_curve`` (CurveTableRowHandle):  [Read-Write] If a curve table entry is specified, the OUTPUT of this custom class magnitude (including the pre and post additive values) lookup into the curve instead of using the attribute directly.
- ``post_multiply_additive_value`` (ScalableFloat):  [Read-Write] Additive value to the attribute calculation, added in after the coefficient applies
- ``pre_multiply_additive_value`` (ScalableFloat):  [Read-Write] Additive value to the attribute calculation, added in before the coefficient applies

<a id="unreal.CustomCalculationBasedFloat.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.SetByCallerFloat"></a>