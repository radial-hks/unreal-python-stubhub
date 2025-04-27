## ActorInstanceHandle Objects

```python
class ActorInstanceHandle(StructBase)
```

Handle to a unique object. This may specify a full weigh actor or it may only specify the actor instance that represents the same object.
note: The handle has game thread constraints related to UObjects and should be used carefully from other threads. Can only be used on the game thread -       all constructors -       all getters (GetXYZ, FetchActor, IsActorValid, DoesRepresent) * -       comparison operators against live AActor pointer Can be used on any thread -       MakeActorHandleToResolve to create a handle that will be lazily resolved on the game thread since it only stores a weak object ptr without any access to the live object -       handle validity and comparison operators against another handle (i.e. IsValid(), operator==|!=(const FActorInstanceHandle& Other))

**C++ Source:**

- **Module**: Engine
- **File**: ActorInstanceHandle.h

<a id="unreal.ActorInstanceHandle.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.Vector_NetQuantize"></a>