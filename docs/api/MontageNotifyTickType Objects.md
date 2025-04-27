## MontageNotifyTickType Objects

```python
class MontageNotifyTickType(EnumBase)
```

Ticking method for AnimNotifies in AnimMontages.

**C++ Source:**

- **Module**: Engine
- **File**: AnimTypes.h

<a id="unreal.MontageNotifyTickType.QUEUED"></a>

#### QUEUED

0: Queue notifies, and trigger them at the end of the evaluation phase (faster). Not suitable for changing sections or montage position.

<a id="unreal.MontageNotifyTickType.BRANCHING_POINT"></a>

#### BRANCHING_POINT

1: Trigger notifies as they are encountered (Slower). Suitable for changing sections or montage position.

<a id="unreal.NotifyFilterType"></a>