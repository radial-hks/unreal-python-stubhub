## StateTreeRunStatus Objects

```python
class StateTreeRunStatus(EnumBase)
```

Status describing current run status of a State Tree.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeExecutionTypes.h

<a id="unreal.StateTreeRunStatus.RUNNING"></a>

#### RUNNING

0: Tree is still running.

<a id="unreal.StateTreeRunStatus.FAILED"></a>

#### FAILED

1: Tree execution has stopped on failure.

<a id="unreal.StateTreeRunStatus.SUCCEEDED"></a>

#### SUCCEEDED

2: Tree execution has stopped on success.

<a id="unreal.StateTreeRunStatus.STOPPED"></a>

#### STOPPED

3: The State Tree was requested to stop without a particular success or failure state.

<a id="unreal.StateTreeRunStatus.UNSET"></a>

#### UNSET

4: Status not set.

<a id="unreal.StateTreeNodeFormatting"></a>