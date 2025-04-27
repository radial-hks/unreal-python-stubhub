## ImportSubsystem_OnAssetPostImport_Dyn Objects

```python
class ImportSubsystem_OnAssetPostImport_Dyn(MulticastDelegateBase)
```

delegate type fired when new assets have been (re-)imported. Note: InCreatedObject can be NULL if import failed. Params: UFactory* InFactory, UObject* InCreatedObject

Args:
    factory (Factory): 
    created_object (Object):

**C++ Source:**

- **Module**: UnrealEd
- **File**: ImportSubsystem.h

<a id="unreal.ImportSubsystem_OnAssetPostImport_Dyn.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.ImportSubsystem_OnAssetPostLODImport_Dyn"></a>