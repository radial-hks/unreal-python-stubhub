## FieldFalloffType Objects

```python
class FieldFalloffType(EnumBase)
```

EField Falloff Type

**C++ Source:**

- **Module**: Chaos
- **File**: FieldSystemTypes.h

<a id="unreal.FieldFalloffType.FIELD_FALL_OFF_NONE"></a>

#### FIELD_FALL_OFF_NONE

0: No falloff function is used

<a id="unreal.FieldFalloffType.FIELD_FALLOFF_LINEAR"></a>

#### FIELD_FALLOFF_LINEAR

1: The falloff function will be proportional to x

<a id="unreal.FieldFalloffType.FIELD_FALLOFF_INVERSE"></a>

#### FIELD_FALLOFF_INVERSE

2: The falloff function will be proportional to 1.0/x

<a id="unreal.FieldFalloffType.FIELD_FALLOFF_SQUARED"></a>

#### FIELD_FALLOFF_SQUARED

3: The falloff function will be proportional to x*x

<a id="unreal.FieldFalloffType.FIELD_FALLOFF_LOGARITHMIC"></a>

#### FIELD_FALLOFF_LOGARITHMIC

4: The falloff function will be proportional to log(x)

<a id="unreal.FieldPhysicsType"></a>