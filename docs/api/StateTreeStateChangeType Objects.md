## StateTreeStateChangeType Objects

```python
class StateTreeStateChangeType(EnumBase)
```

State change type. Passed to EnterState() and ExitState() to indicate how the state change affects the state and Evaluator or Task is on.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeExecutionTypes.h

<a id="unreal.StateTreeStateChangeType.NONE"></a>

#### NONE

0: Not an activation

<a id="unreal.StateTreeStateChangeType.CHANGED"></a>

#### CHANGED

1: The state became activated or deactivated.

<a id="unreal.StateTreeStateChangeType.SUSTAINED"></a>

#### SUSTAINED

2: The state is parent of new active state and sustained previous active state.

<a id="unreal.StateTreePropertyRefType"></a>