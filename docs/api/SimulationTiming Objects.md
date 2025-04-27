## SimulationTiming Objects

```python
class SimulationTiming(EnumBase)
```

Determines behaviour regarding deferral of simulation tasks.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RigidBody.h

<a id="unreal.SimulationTiming.DEFAULT"></a>

#### DEFAULT

0: Use the default project setting as defined by p.RigidBodyNode.DeferredSimulationDefault.

<a id="unreal.SimulationTiming.SYNCHRONOUS"></a>

#### SYNCHRONOUS

1: Always run the simulation to completion during animation evaluation.

<a id="unreal.SimulationTiming.DEFERRED"></a>

#### DEFERRED

2: Always run the simulation in the background and retrieve the result on the next animation evaluation.

<a id="unreal.SplineBoneAxis"></a>