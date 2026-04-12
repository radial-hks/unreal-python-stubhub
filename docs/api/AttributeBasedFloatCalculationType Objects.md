## AttributeBasedFloatCalculationType Objects

```python
class AttributeBasedFloatCalculationType(EnumBase)
```

Enumeration outlining the possible attribute based float calculation policies.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.AttributeBasedFloatCalculationType.ATTRIBUTE_MAGNITUDE"></a>

#### ATTRIBUTE\_MAGNITUDE

0: Use the final evaluated magnitude of the attribute.

<a id="unreal.AttributeBasedFloatCalculationType.ATTRIBUTE_BASE_VALUE"></a>

#### ATTRIBUTE\_BASE\_VALUE

1: Use the base value of the attribute.

<a id="unreal.AttributeBasedFloatCalculationType.ATTRIBUTE_BONUS_MAGNITUDE"></a>

#### ATTRIBUTE\_BONUS\_MAGNITUDE

2: Use the "bonus" evaluated magnitude of the attribute: Equivalent to (FinalMag - BaseValue).

<a id="unreal.WorldConditionOperator"></a>