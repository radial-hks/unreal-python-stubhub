## OnMontageBlendingOutStartedMCDelegate Objects

```python
class OnMontageBlendingOutStartedMCDelegate(MulticastDelegateBase)
```

Delegate for when Montage started to blend out, whether interrupted or finished
DesiredWeight of this montage becomes 0.f, but this still contributes to the output pose

bInterrupted = true if it was not property finished

Args:
    montage (AnimMontage): 
    interrupted (bool):

**C++ Source:**

- **Module**: Engine
- **File**: AnimInstance.h

<a id="unreal.OnMontageBlendingOutStartedMCDelegate.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.OnMontageEndedMCDelegate"></a>