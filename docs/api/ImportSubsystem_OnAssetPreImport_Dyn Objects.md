## ImportSubsystem_OnAssetPreImport_Dyn Objects

```python
class ImportSubsystem_OnAssetPreImport_Dyn(MulticastDelegateBase)
```

delegate type fired when new assets are being (re-)imported. Params: UFactory* InFactory, UClass* InClass, UObject* InParent, const FName& Name, const TCHAR* Type

Args:
    factory (Factory): 
    class_ (type(Class)): 
    parent (Object): 
    name (Name): 
    type (str):

**C++ Source:**

- **Module**: UnrealEd
- **File**: ImportSubsystem.h

<a id="unreal.ImportSubsystem_OnAssetPreImport_Dyn.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.ImportSubsystem_OnAssetReimport_Dyn"></a>