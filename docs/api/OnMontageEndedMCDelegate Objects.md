## OnMontageEndedMCDelegate Objects

```python
class OnMontageEndedMCDelegate(MulticastDelegateBase)
```

Delegate for when Montage is completed, whether interrupted or finished
Weight of this montage is 0.f, so it stops contributing to output pose

bInterrupted = true if it was not property finished

Args:
    montage (AnimMontage): 
    interrupted (bool):

**C++ Source:**

- **Module**: Engine
- **File**: AnimInstance.h

<a id="unreal.OnMontageEndedMCDelegate.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnMontageStartedMCDelegate"></a>