## PCGControlPointFuseMode Objects

```python
class PCGControlPointFuseMode(EnumBase)
```

EPCGControl Point Fuse Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCleanSpline.h

<a id="unreal.PCGControlPointFuseMode.KEEP_FIRST"></a>

#### KEEP_FIRST

0: Keep the first of two control points.

<a id="unreal.PCGControlPointFuseMode.KEEP_SECOND"></a>

#### KEEP_SECOND

1: Keep the second of two control points.

<a id="unreal.PCGControlPointFuseMode.MERGE"></a>

#### MERGE

2: Fuse the two control points into a new control point, located halfway between the original two.

<a id="unreal.PCGControlPointFuseMode.AUTO"></a>

#### AUTO

3: Will generally keep the second of both control points, except keep the first when it would otherwise alter the length of the spline--ie. final control point.

<a id="unreal.PCGClusterAlgorithm"></a>