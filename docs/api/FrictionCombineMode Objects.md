## FrictionCombineMode Objects

```python
class FrictionCombineMode(EnumBase)
```

EFriction Combine Mode

**C++ Source:**

- **Module**: PhysicsCore
- **File**: PhysicsSettingsEnums.h

<a id="unreal.FrictionCombineMode.AVERAGE"></a>

#### AVERAGE

0: Uses the average value of the materials touching: (a+b)/2

<a id="unreal.FrictionCombineMode.MIN"></a>

#### MIN

1: Uses the minimum value of the materials touching: min(a,b)

<a id="unreal.FrictionCombineMode.MULTIPLY"></a>

#### MULTIPLY

2: Uses the product of the values of the materials touching: a*b

<a id="unreal.FrictionCombineMode.MAX"></a>

#### MAX

3: Uses the maximum value of materials touching: max(a,b)

<a id="unreal.PhysicalMaterialSoftCollisionMode"></a>