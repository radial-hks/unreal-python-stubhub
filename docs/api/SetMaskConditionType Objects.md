## SetMaskConditionType Objects

```python
class SetMaskConditionType(EnumBase)
```

ESet Mask Condition Type

**C++ Source:**

- **Module**: Chaos
- **File**: FieldSystemTypes.h

<a id="unreal.SetMaskConditionType.FIELD_SET_ALWAYS"></a>

#### FIELD_SET_ALWAYS

0: The particle output value will be equal to Interior-value if the particle position is inside a sphere / Exterior-value otherwise.

<a id="unreal.SetMaskConditionType.FIELD_SET_IFF_NOT_INTERIOR"></a>

#### FIELD_SET_IFF_NOT_INTERIOR

1: The particle output value will be equal to Interior-value if the particle position is inside the sphere or if the particle input value is already Interior-Value / Exterior-value otherwise.

<a id="unreal.SetMaskConditionType.FIELD_SET_IFF_NOT_EXTERIOR"></a>

#### FIELD_SET_IFF_NOT_EXTERIOR

2: The particle output value will be equal to Exterior-value if the particle position is outside the sphere or if the particle input value is already Exterior-Value / Interior-value otherwise.

<a id="unreal.WaveFunctionType"></a>