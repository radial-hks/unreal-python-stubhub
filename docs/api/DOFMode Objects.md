## DOFMode Objects

```python
class DOFMode(EnumBase)
```

EDOFMode

**C++ Source:**

- **Module**: Engine
- **File**: BodyInstance.h

<a id="unreal.DOFMode.DEFAULT"></a>

#### DEFAULT

0: Inherits the degrees of freedom from the project settings.

<a id="unreal.DOFMode.SIX_DOF"></a>

#### SIX\_DOF

1: Specifies which axis to freeze rotation and movement along.

<a id="unreal.DOFMode.YZ_PLANE"></a>

#### YZ\_PLANE

2: Allows 2D movement along the Y-Z plane.

<a id="unreal.DOFMode.XZ_PLANE"></a>

#### XZ\_PLANE

3: Allows 2D movement along the X-Z plane.

<a id="unreal.DOFMode.XY_PLANE"></a>

#### XY\_PLANE

4: Allows 2D movement along the X-Y plane.

<a id="unreal.DOFMode.CUSTOM_PLANE"></a>

#### CUSTOM\_PLANE

5: Allows 2D movement along the plane of a given normal

<a id="unreal.DOFMode.NONE"></a>

#### NONE

6: No constraints.

<a id="unreal.LockedAxis"></a>