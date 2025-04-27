## PathFollowingResult Objects

```python
class PathFollowingResult(EnumBase)
```

EPath Following Result

**C++ Source:**

- **Module**: AIModule
- **File**: PathFollowingComponent.h

<a id="unreal.PathFollowingResult.SUCCESS"></a>

#### SUCCESS

0: Reached destination

<a id="unreal.PathFollowingResult.BLOCKED"></a>

#### BLOCKED

1: Movement was blocked

<a id="unreal.PathFollowingResult.OFF_PATH"></a>

#### OFF_PATH

2: Agent is not on path

<a id="unreal.PathFollowingResult.ABORTED"></a>

#### ABORTED

3: Aborted and stopped (failure)

<a id="unreal.PathFollowingResult.INVALID"></a>

#### INVALID

5: Request was invalid

<a id="unreal.EnvQueryStatus"></a>