## PCGBlurElementMode Objects

```python
class PCGBlurElementMode(EnumBase)
```

EPCGBlur Element Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGBlurElement.h

<a id="unreal.PCGBlurElementMode.CONSTANT"></a>

#### CONSTANT

0: Same weight for each point, which will be 1 / N, N being the number of points found in the given distance.

<a id="unreal.PCGBlurElementMode.LINEAR"></a>

#### LINEAR

1: Weight for Point will be 1 - Dist(Point, Center) / SearchDistance.

<a id="unreal.PCGBlurElementMode.GAUSSIAN"></a>

#### GAUSSIAN

2: Weight will be a gaussian distribution.

<a id="unreal.PCGControlPointFuseMode"></a>