## GameplayEffectMagnitudeCalculation Objects

```python
class GameplayEffectMagnitudeCalculation(EnumBase)
```

Enumeration outlining the possible gameplay effect magnitude calculation policies.

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffect.h

<a id="unreal.GameplayEffectMagnitudeCalculation.SCALABLE_FLOAT"></a>

#### SCALABLE\_FLOAT

0: Use a simple, scalable float for the calculation.

<a id="unreal.GameplayEffectMagnitudeCalculation.ATTRIBUTE_BASED"></a>

#### ATTRIBUTE\_BASED

1: Perform a calculation based upon an attribute.

<a id="unreal.GameplayEffectMagnitudeCalculation.CUSTOM_CALCULATION_CLASS"></a>

#### CUSTOM\_CALCULATION\_CLASS

2: Perform a custom calculation, capable of capturing and acting on multiple attributes, in either BP or native.

<a id="unreal.GameplayEffectMagnitudeCalculation.SET_BY_CALLER"></a>

#### SET\_BY\_CALLER

3: This magnitude will be set explicitly by the code/blueprint that creates the spec.

<a id="unreal.GameplayModEvaluationChannel"></a>