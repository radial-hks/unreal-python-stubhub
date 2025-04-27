## ResponseChannel Objects

```python
class ResponseChannel(StructBase)
```

Describes response for a single collision response channel

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``channel`` (Name):  [Read-Write] This should match DisplayName of ECollisionChannel
      Meta data of custom channels can be used as well
- ``response`` (CollisionResponseType):  [Read-Write] Describes how the channel behaves

<a id="unreal.ResponseChannel.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.BranchFilter"></a>