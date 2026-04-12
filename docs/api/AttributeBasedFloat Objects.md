## AttributeBasedFloat Objects

```python
class AttributeBasedFloat(StructBase)
```

Struct representing a float whose magnitude is dictated by a backing attribute and a calculation policy, follows basic form of:
(Coefficient * (PreMultiplyAdditiveValue + [Eval'd Attribute Value According to Policy])) + PostMultiplyAdditiveValue

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_calculation_type`` (AttributeBasedFloatCalculationType):  [Read-Write] Calculation policy in regards to the attribute
- ``attribute_curve`` (CurveTableRowHandle):  [Read-Write] If a curve table entry is specified, the attribute will be used as a lookup into the curve instead of using the attribute directly.
- ``backing_attribute`` (GameplayEffectAttributeCaptureDefinition):  [Read-Write] Attribute backing the calculation
- ``coefficient`` (ScalableFloat):  [Read-Write] Coefficient to the attribute calculation
- ``final_channel`` (GameplayModEvaluationChannel):  [Read-Write] Channel to terminate evaluation on when using AttributeEvaluatedUpToChannel calculation type
- ``post_multiply_additive_value`` (ScalableFloat):  [Read-Write] Additive value to the attribute calculation, added in after the coefficient applies
- ``pre_multiply_additive_value`` (ScalableFloat):  [Read-Write] Additive value to the attribute calculation, added in before the coefficient applies
- ``source_tag_filter`` (GameplayTagContainer):  [Read-Write] Filter to use on source tags; If specified, only modifiers applied with all of these tags will factor into the calculation
- ``target_tag_filter`` (GameplayTagContainer):  [Read-Write] Filter to use on target tags; If specified, only modifiers applied with all of these tags will factor into the calculation

<a id="unreal.AttributeBasedFloat.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.CustomCalculationBasedFloat"></a>