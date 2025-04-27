## LocatorResolveFlags Objects

```python
class LocatorResolveFlags(EnumBase)
```

ELocator Resolve Flags

**C++ Source:**

- **Module**: UniversalObjectLocator
- **File**: UniversalObjectLocatorResolveParams.h

<a id="unreal.LocatorResolveFlags.NONE"></a>

#### NONE

0

<a id="unreal.LocatorResolveFlags.LOAD"></a>

#### LOAD

1: Flag to indicate whether the object should be loaded if it is not currently findable

<a id="unreal.LocatorResolveFlags.UNLOAD"></a>

#### UNLOAD

2: Flag to indicate whether the object should be unloaded or destroyed. Mutually exclusive with bLoad.

<a id="unreal.LocatorResolveFlags.ASYNC"></a>

#### ASYNC

4: Indicates that the operation should be performed asynchronously if possible.
  When not combined with WillWait, the caller will never block waiting for the result.
  When combined with WillWait, the caller will block on this thread until the result is available,
   so care needs to be taken avoid a deadlock if there are additional threading constraints on the load.

<a id="unreal.LocatorResolveFlags.WILL_WAIT"></a>

#### WILL_WAIT

8: Indicates the calling code is going to block waiting for the result.

<a id="unreal.LocatorResolveFlags.ASYNC_WAIT"></a>

#### ASYNC_WAIT

12: Combination of Async and WillWait.

<a id="unreal.CoreOnlineDummy"></a>