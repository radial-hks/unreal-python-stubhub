## MVVMBlueprintViewModelContextCreationType Objects

```python
class MVVMBlueprintViewModelContextCreationType(EnumBase)
```

EMVVMBlueprint View Model Context Creation Type

**C++ Source:**

- **Plugin**: ModelViewViewModel
- **Module**: ModelViewViewModelBlueprint
- **File**: MVVMBlueprintViewModelContext.h

<a id="unreal.MVVMBlueprintViewModelContextCreationType.MANUAL"></a>

#### MANUAL

0: // The viewmodel will be assigned later.

<a id="unreal.MVVMBlueprintViewModelContextCreationType.CREATE_INSTANCE"></a>

#### CREATE_INSTANCE

1: A new instance of the viewmodel will be created when the widget is created.

<a id="unreal.MVVMBlueprintViewModelContextCreationType.GLOBAL_VIEW_MODEL_COLLECTION"></a>

#### GLOBAL_VIEW_MODEL_COLLECTION

2: The viewmodel exists and is added to the MVVMSubsystem. It will be fetched there.

<a id="unreal.MVVMBlueprintViewModelContextCreationType.PROPERTY_PATH"></a>

#### PROPERTY_PATH

3: The viewmodel will be fetched by evaluating a function or a property path.

<a id="unreal.MVVMBlueprintViewModelContextCreationType.RESOLVER"></a>

#### RESOLVER

4: The viewmodel will be fetched by evaluating the resolver object.

<a id="unreal.AnimPhysLinearConstraintType"></a>