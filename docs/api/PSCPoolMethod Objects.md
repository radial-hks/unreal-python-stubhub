## PSCPoolMethod Objects

```python
class PSCPoolMethod(EnumBase)
```

EPSCPool Method

**C++ Source:**

- **Module**: Engine
- **File**: WorldPSCPool.h

<a id="unreal.PSCPoolMethod.NONE"></a>

#### NONE

0: PSC is will be created fresh and not allocated from the pool.

<a id="unreal.PSCPoolMethod.AUTO_RELEASE"></a>

#### AUTO_RELEASE

1: PSC is allocated from the pool and will be automatically released back to it.
User need not handle this any more that other PSCs but interaction with the PSC after the tick it's spawned in are unsafe.
This method is useful for one-shot fx that you don't need to keep a reference to and can fire and forget.

<a id="unreal.PSCPoolMethod.MANUAL_RELEASE"></a>

#### MANUAL_RELEASE

2: PSC is allocated from the pool but will NOT be automatically released back to it. User has ownership of the PSC and must call ReleaseToPool when finished with it otherwise the PSC will leak.
Interaction with the PSC after it has been released are unsafe.
This method is useful for persistent FX that you need to modify parameters upon etc over it's lifetime.

<a id="unreal.ViewTargetBlendFunction"></a>