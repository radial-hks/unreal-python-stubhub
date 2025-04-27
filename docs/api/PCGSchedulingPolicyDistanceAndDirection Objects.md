## PCGSchedulingPolicyDistanceAndDirection Objects

```python
class PCGSchedulingPolicyDistanceAndDirection(PCGSchedulingPolicyBase)
```

SchedulingPolicyDistanceAndDirection uses distance from the generating volume
and alignment with view direction to choose the most important volumes to generate.

Distance and Direction are calculated with respect to the Generation Source.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSchedulingPolicyDistanceAndDirection.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction_weight`` (float):  [Read-Write] Scalar value used to increase/decrease the impact of direction in the scheduling priority.
- ``distance_weight`` (float):  [Read-Write] Scalar value used to increase/decrease the impact of distance in the scheduling priority.
- ``use_direction`` (bool):  [Read-Write] Toggle whether or not direction is used to calculate the scheduling priority.
- ``use_distance`` (bool):  [Read-Write] Toggle whether or not distance is used to calculate the scheduling priority.

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.use_distance"></a>

#### use_distance

```python
@property
def use_distance() -> bool
```

(bool):  [Read-Write] Toggle whether or not distance is used to calculate the scheduling priority.

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.use_distance"></a>

#### use_distance

```python
@use_distance.setter
def use_distance(value: bool) -> None
```

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.distance_weight"></a>

#### distance_weight

```python
@property
def distance_weight() -> float
```

(float):  [Read-Write] Scalar value used to increase/decrease the impact of distance in the scheduling priority.

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.distance_weight"></a>

#### distance_weight

```python
@distance_weight.setter
def distance_weight(value: float) -> None
```

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.use_direction"></a>

#### use_direction

```python
@property
def use_direction() -> bool
```

(bool):  [Read-Write] Toggle whether or not direction is used to calculate the scheduling priority.

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.use_direction"></a>

#### use_direction

```python
@use_direction.setter
def use_direction(value: bool) -> None
```

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.direction_weight"></a>

#### direction_weight

```python
@property
def direction_weight() -> float
```

(float):  [Read-Write] Scalar value used to increase/decrease the impact of direction in the scheduling priority.

<a id="unreal.PCGSchedulingPolicyDistanceAndDirection.direction_weight"></a>

#### direction_weight

```python
@direction_weight.setter
def direction_weight(value: float) -> None
```

<a id="unreal.PCGDeterminismTestBlueprintBase"></a>