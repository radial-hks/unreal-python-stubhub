## RBFNormalizeMethod Objects

```python
class RBFNormalizeMethod(EnumBase)
```

Method to normalize weights

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: RBFSolver.h

<a id="unreal.RBFNormalizeMethod.ONLY_NORMALIZE_ABOVE_ONE"></a>

#### ONLY_NORMALIZE_ABOVE_ONE

0: Only normalize above one

<a id="unreal.RBFNormalizeMethod.ALWAYS_NORMALIZE"></a>

#### ALWAYS_NORMALIZE

1: Always normalize.
Zero distribution weights stay zero.

<a id="unreal.RBFNormalizeMethod.NORMALIZE_WITHIN_MEDIAN"></a>

#### NORMALIZE_WITHIN_MEDIAN

2: Normalize only within reference median. The median
is a cone with a minimum and maximum angle within
which the value will be interpolated between
non-normalized and normalized. This helps to define
the volume in which normalization is always required.

<a id="unreal.RBFNormalizeMethod.NO_NORMALIZATION"></a>

#### NO_NORMALIZATION

3: Don't normalize at all. This should only be used with
the interpolative method, if it is known that all input
values will be within the area bounded by the targets.

<a id="unreal.SnapshotSourceMode"></a>