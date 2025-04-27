## PCGCollapseComparisonMode Objects

```python
class PCGCollapseComparisonMode(EnumBase)
```

EPCGCollapse Comparison Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGCollapsePoints.h

<a id="unreal.PCGCollapseComparisonMode.POSITION"></a>

#### POSITION

0: Uses point position only for distance testing, regardless of bounds.

<a id="unreal.PCGCollapseComparisonMode.CENTER"></a>

#### CENTER

1: Uses point centers (e.g. center of bounds) for distance testing, and ignore bounds otherwise.

<a id="unreal.PCGCollapseVisitOrder"></a>