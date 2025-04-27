## StateTreeStructRef Objects

```python
class StateTreeStructRef(StructBase)
```

StateTree struct ref allows to get a reference/pointer to a specified type via property binding.
It is useful for referencing larger properties to avoid copies of the data, or to be able to write to a bounds property.

The expected type of the reference should be set in "BaseStruct" meta tag.

Example:

    USTRUCT()
    struct FAwesomeTaskInstanceData
    {
            GENERATED_BODY()

            UPROPERTY(VisibleAnywhere, Category = Input, meta = (BaseStruct = "/Script/AwesomeModule.AwesomeData"))
            FStateTreeStructRef Data;
    };


    if (const FAwesomeData* Awesome = InstanceData.Data.GetPtr<FAwesomeData>())
    {
            ...
    }

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeTypes.h

<a id="unreal.StateTreeStructRef.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeStateLink"></a>