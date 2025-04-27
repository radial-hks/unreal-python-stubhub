## InstancedStruct Objects

```python
class InstancedStruct(StructBase)
```

FInstancedStruct works similarly as instanced UObject* property but is USTRUCTs.

Example:

    UPROPERTY(EditAnywhere, Category = Foo, meta = (BaseStruct = "/Script/ModuleName.TestStructBase"))
    FInstancedStruct Test;

    UPROPERTY(EditAnywhere, Category = Foo, meta = (BaseStruct = "/Script/ModuleName.TestStructBase"))
    TArray<FInstancedStruct> TestArray;

**C++ Source:**

- **Module**: CoreUObject
- **File**: InstancedStruct.h

<a id="unreal.InstancedStruct.__init__"></a>

#### __init__

```python
def __init__(value: int = 0) -> None
```

<a id="unreal.UniqueScriptStructPtr"></a>