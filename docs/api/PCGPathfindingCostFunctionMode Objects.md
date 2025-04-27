## PCGPathfindingCostFunctionMode Objects

```python
class PCGPathfindingCostFunctionMode(EnumBase)
```

EPCGPathfinding Cost Function Mode

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGPathfindingElement.h

<a id="unreal.PCGPathfindingCostFunctionMode.DISTANCE"></a>

#### DISTANCE

0: Pathfinding cost will be the distance only.

<a id="unreal.PCGPathfindingCostFunctionMode.FITNESS_SCORE"></a>

#### FITNESS_SCORE

1: Pathfinding cost will be driven by a fitness score (0-1 range), with a maximum penalty applied at fitness = 0.

<a id="unreal.PCGPathfindingCostFunctionMode.COST_MULTIPLIER"></a>

#### COST_MULTIPLIER

2: Pathfinding cost will be the distance multiplied by the provided factor. Note that multipliers below 1 will be clamped to 1.

<a id="unreal.PCGCollisionQueryFlag"></a>