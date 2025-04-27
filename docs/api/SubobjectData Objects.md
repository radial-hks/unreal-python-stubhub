## SubobjectData Objects

```python
class SubobjectData(StructBase)
```

A struct that represents a single subobject. This can be anything, but are
most commonly components attached to an actor instance or blueprint. Keeps track
of the handles to its parent object and any child that it has.

If you wish to modify a subobject, use the SubobjectDataSubsystem.

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectData.h

<a id="unreal.SubobjectData.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SubobjectDataHandle"></a>