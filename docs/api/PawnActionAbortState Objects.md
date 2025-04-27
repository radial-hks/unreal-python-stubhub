## PawnActionAbortState Objects

```python
class PawnActionAbortState(EnumBase)
```

EPawn Action Abort State

**C++ Source:**

- **Module**: AIModule
- **File**: AITypes.h

<a id="unreal.PawnActionAbortState.NEVER_STARTED"></a>

#### NEVER_STARTED

0

<a id="unreal.PawnActionAbortState.NOT_BEING_ABORTED"></a>

#### NOT_BEING_ABORTED

1

<a id="unreal.PawnActionAbortState.MARK_PENDING_ABORT"></a>

#### MARK_PENDING_ABORT

2: This means waiting for child to abort before aborting self.

<a id="unreal.PawnActionAbortState.LATENT_ABORT_IN_PROGRESS"></a>

#### LATENT_ABORT_IN_PROGRESS

3

<a id="unreal.PawnActionAbortState.ABORT_DONE"></a>

#### ABORT_DONE

4

<a id="unreal.PawnActionFailHandling"></a>