## GameplayEffectModifierMagnitude Objects

```python
class GameplayEffectModifierMagnitude(StructBase)
```

Struct representing the magnitude of a gameplay effect modifier, potentially calculated in numerous different ways

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_based_magnitude`` (AttributeBasedFloat):  [Read-Write] Magnitude value represented by an attribute-based float
        (Coefficient * (PreMultiplyAdditiveValue + [Eval'd Attribute Value According to Policy])) + PostMultiplyAdditiveValue
- ``custom_magnitude`` (CustomCalculationBasedFloat):  [Read-Write] Magnitude value represented by a custom calculation class
- ``magnitude_calculation_type`` (GameplayEffectMagnitudeCalculation):  [Read-Write] Type of calculation to perform to derive the magnitude
- ``scalable_float_magnitude`` (ScalableFloat):  [Read-Write] Magnitude value represented by a scalable float
- ``set_by_caller_magnitude`` (SetByCallerFloat):  [Read-Write] Magnitude value represented by a SetByCaller magnitude

<a id="unreal.GameplayEffectModifierMagnitude.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GameplayModEvaluationChannelSettings"></a>