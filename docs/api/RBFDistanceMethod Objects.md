## RBFDistanceMethod Objects

```python
class RBFDistanceMethod(EnumBase)
```

Method for determining distance from input to targets

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: RBFSolver.h

<a id="unreal.RBFDistanceMethod.EUCLIDEAN"></a>

#### EUCLIDEAN

0: Standard n-dimensional distance measure

<a id="unreal.RBFDistanceMethod.QUATERNION"></a>

#### QUATERNION

1: Treat inputs as quaternion

<a id="unreal.RBFDistanceMethod.SWING_ANGLE"></a>

#### SWING_ANGLE

2: Treat inputs as quaternion, and find distance between rotated TwistAxis direction

<a id="unreal.RBFDistanceMethod.TWIST_ANGLE"></a>

#### TWIST_ANGLE

3: Treat inputs as quaternion, and find distance between rotations around the TwistAxis direction

<a id="unreal.RBFDistanceMethod.DEFAULT_METHOD"></a>

#### DEFAULT_METHOD

4: Uses the setting of the parent container

<a id="unreal.RBFNormalizeMethod"></a>