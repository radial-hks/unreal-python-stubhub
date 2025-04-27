## PlaneConstraintAxisSetting Objects

```python
class PlaneConstraintAxisSetting(EnumBase)
```

Setting that controls behavior when movement is restricted to a 2D plane defined by a specific axis/normal,
so that movement along the locked axis is not be possible.

**C++ Source:**

- **Module**: Engine
- **File**: MovementComponent.h

<a id="unreal.PlaneConstraintAxisSetting.CUSTOM"></a>

#### CUSTOM

0: Lock movement to a user-defined axis.

<a id="unreal.PlaneConstraintAxisSetting.X"></a>

#### X

1: Lock movement in the X axis.

<a id="unreal.PlaneConstraintAxisSetting.Y"></a>

#### Y

2: Lock movement in the Y axis.

<a id="unreal.PlaneConstraintAxisSetting.Z"></a>

#### Z

3: Lock movement in the Z axis.

<a id="unreal.PlaneConstraintAxisSetting.USE_GLOBAL_PHYSICS_SETTING"></a>

#### USE_GLOBAL_PHYSICS_SETTING

4: Use the global physics project setting.

<a id="unreal.InterpToBehaviourType"></a>