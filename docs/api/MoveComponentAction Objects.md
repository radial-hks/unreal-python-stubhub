## MoveComponentAction Objects

```python
class MoveComponentAction(EnumBase)
```

Enum used to indicate desired behavior for MoveComponentTo latent function.

**C++ Source:**

- **Module**: Engine
- **File**: KismetSystemLibrary.h

<a id="unreal.MoveComponentAction.MOVE"></a>

#### MOVE

0: Move to target over specified time.

<a id="unreal.MoveComponentAction.STOP"></a>

#### STOP

1: If currently moving, stop.

<a id="unreal.MoveComponentAction.RETURN"></a>

#### RETURN

2: If currently moving, return to where you started, over the time elapsed so far.

<a id="unreal.EditorPropertyValueState"></a>