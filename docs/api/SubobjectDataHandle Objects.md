## SubobjectDataHandle Objects

```python
class SubobjectDataHandle(StructBase)
```

A subobject handle is a globally unique identifier for subobjects
Upon construction, the handle will be invalid. It is the responsibility
of the owning FSubobjectData to set the DataPtr once the subobject
data has validated that it has a good context.

**C++ Source:**

- **Module**: SubobjectDataInterface
- **File**: SubobjectDataHandle.h

<a id="unreal.SubobjectDataHandle.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AddNewSubobjectParams"></a>