## SimulationSpace Objects

```python
class SimulationSpace(EnumBase)
```

Determines in what space the simulation should run

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RigidBody.h

<a id="unreal.SimulationSpace.COMPONENT_SPACE"></a>

#### COMPONENT_SPACE

0: Simulate in component space. Moving the entire skeletal mesh will have no affect on velocities

<a id="unreal.SimulationSpace.WORLD_SPACE"></a>

#### WORLD_SPACE

1: Simulate in world space. Moving the skeletal mesh will generate velocity changes

<a id="unreal.SimulationSpace.BASE_BONE_SPACE"></a>

#### BASE_BONE_SPACE

2: Simulate in another bone space. Moving the entire skeletal mesh and individually modifying the base bone will have no affect on velocities

<a id="unreal.SimulationTiming"></a>