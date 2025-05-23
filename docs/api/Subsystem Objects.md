## Subsystem Objects

```python
class Subsystem(Object)
```

Subsystems are auto instanced classes that share the lifetime of certain engine constructs

   Currently supported Subsystem lifetimes are:
           Engine           -> inherit UEngineSubsystem
           Editor           -> inherit UEditorSubsystem
           GameInstance -> inherit UGameInstanceSubsystem
           World            -> inherit UWorldSubsystem
           LocalPlayer      -> inherit ULocalPlayerSubsystem


   Normal Example:
           class UMySystem : public UGameInstanceSubsystem
   Which can be accessed by:
           UGameInstance* GameInstance = ...;
           UMySystem* MySystem = GameInstance->GetSubsystem<UMySystem>();

   or the following if you need protection from a null GameInstance
           UGameInstance* GameInstance = ...;
           UMyGameSubsystem* MySubsystem = UGameInstance::GetSubsystem<MyGameSubsystem>(GameInstance);


   You can get also define interfaces that can have multiple implementations.
   Interface Example :
    MySystemInterface
  With 2 concrete derivative classes:
    MyA : public MySystemInterface
    MyB : public MySystemInterface

   Which can be accessed by:
           UGameInstance* GameInstance = ...;
           const TArray<UMyGameSubsystem*>& MySubsystems = GameInstance->GetSubsystemArray<MyGameSubsystem>();

**C++ Source:**

- **Module**: Engine
- **File**: Subsystem.h

<a id="unreal.DynamicSubsystem"></a>