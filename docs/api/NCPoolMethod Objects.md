## NCPoolMethod Objects

```python
class NCPoolMethod(EnumBase)
```

ENCPool Method

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraComponentPoolMethodEnum.h

<a id="unreal.NCPoolMethod.NONE"></a>

#### NONE

0: The component will be created fresh and not allocated from the pool.

<a id="unreal.NCPoolMethod.AUTO_RELEASE"></a>

#### AUTO_RELEASE

1: The component is allocated from the pool and will be automatically released back to it.
User need not handle this any more that other NCs but interaction with the NC after the tick it's spawned in are unsafe.
This method is useful for one-shot fx that you don't need to keep a reference to and can fire and forget.

<a id="unreal.NCPoolMethod.MANUAL_RELEASE"></a>

#### MANUAL_RELEASE

2: NC is allocated from the pool but will NOT be automatically released back to it. User has ownership of the NC and must call ReleaseToPool when finished with it otherwise the NC will leak.
Interaction with the NC after it has been released are unsafe.
This method is useful for persistent FX that you need to modify parameters upon etc over it's lifetime.

<a id="unreal.NiagaraRendererMotionVectorSetting"></a>