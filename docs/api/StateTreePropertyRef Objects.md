## StateTreePropertyRef Objects

```python
class StateTreePropertyRef(StructBase)
```

Property ref allows to get a pointer to selected property in StateTree.
The expected type of the reference should be set in "RefType" meta specifier.

Meta specifiers for the type:
 - RefType = "<type>"
            - Specifies a comma separated list of type of property to reference
            - Supported types are: bool, byte, int32, int64, float, double, Name, String, Text, UObject pointers, and structs
            - Structs and Objects must use full path name
            - If multiple types are specified, GetMutablePtrTuple can be used to access the correct type
 - IsRefToArray
            - If specified, the reference is to an TArray<RefType>
    - CanRefToArray
            - If specified, the reference can bind to a Reftype or TArray<RefType>
 - Optional
            - If specified, the reference can be left unbound, otherwise the compiler report error if the reference is not bound

Example:

 // Reference to float
    UPROPERTY(EditAnywhere, meta = (RefType = "float"))
    FStateTreePropertyRef RefToFloat;

 // Reference to FTestStructBase
    UPROPERTY(EditAnywhere, meta = (RefType = "/Script/ModuleName.TestStructBase"))
    FStateTreePropertyRef RefToTest;

 // Reference to TArray<FTestStructBase>
    UPROPERTY(EditAnywhere, meta = (RefType = "/Script/ModuleName.TestStructBase", IsRefToArray))
    FStateTreePropertyRef RefToArrayOfTests;

 // Reference to Vector, TArray<FVector>, AActor*, TArray<AActor*>
    UPROPERTY(EditAnywhere, meta = (RefType = "/Script/CoreUObject.Vector, /Script/Engine.Actor", CanRefToArray))
    FStateTreePropertyRef RefToLocationLikeTypes;

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreePropertyRef.h

<a id="unreal.StateTreePropertyRef.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.StateTreeBlueprintPropertyRef"></a>