## GameplayModOp Objects

```python
class GameplayModOp(EnumBase)
```

Defines the ways that mods will modify attributes. Values of the same type are aggregated, and then applied in the following equation:
((BaseValue + AddBase) * MultiplyAdditive / DivideAdditive * MultiplyCompound) + AddFinal

**C++ Source:**

- **Plugin**: GameplayAbilities
- **Module**: GameplayAbilities
- **File**: GameplayEffectTypes.h

<a id="unreal.GameplayModOp.ADD_BASE"></a>

#### ADD\_BASE

0: Adds to the Base value. This happens first, before all other mods are considered.

<a id="unreal.GameplayModOp.MULTIPLY_ADDITIVE"></a>

#### MULTIPLY\_ADDITIVE

1: Multipliers are added together first, then multiplied against prev result. E.g. 50% + 50% = 100% in values is 1.5 + 1.5 = 2.0.

<a id="unreal.GameplayModOp.DIVIDE_ADDITIVE"></a>

#### DIVIDE\_ADDITIVE

2: Divisors are added together, then divided against the prev result. E.g. 1/2 + 1/2 = 1/3 in values is 2 + 2 = 3.

<a id="unreal.GameplayModOp.MULTIPLY_COMPOUND"></a>

#### MULTIPLY\_COMPOUND

4: Multiply the prev result by this value. E.g. two values of 1.5 compounded: 1.5 * 1.5 = 2.25.

<a id="unreal.GameplayModOp.ADD_FINAL"></a>

#### ADD\_FINAL

5: Add this value to the final computed result.

<a id="unreal.GameplayModOp.OVERRIDE"></a>

#### OVERRIDE

3: Override the value, regardless of what the computation provides.

<a id="unreal.GameplayTagEventType"></a>