## TransitionRequestOverwriteMode Objects

```python
class TransitionRequestOverwriteMode(EnumBase)
```

ETransition Request Overwrite Mode

**C++ Source:**

- **Module**: Engine
- **File**: AnimStateMachineTypes.h

<a id="unreal.TransitionRequestOverwriteMode.APPEND"></a>

#### APPEND

0: This request is added whether or not another with the same name is already queued

<a id="unreal.TransitionRequestOverwriteMode.IGNORE"></a>

#### IGNORE

1: This request is ignored if another request with the same name is already queued

<a id="unreal.TransitionRequestOverwriteMode.OVERWRITE"></a>

#### OVERWRITE

2: This request overwrites another request with the same name if one exists

<a id="unreal.TransformCurveChannel"></a>