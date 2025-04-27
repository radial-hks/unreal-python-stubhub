## InputMappingRebuildType Objects

```python
class InputMappingRebuildType(EnumBase)
```

EInput Mapping Rebuild Type

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputSubsystemInterface.h

<a id="unreal.InputMappingRebuildType.NONE"></a>

#### NONE

0: No rebuild required.

<a id="unreal.InputMappingRebuildType.REBUILD"></a>

#### REBUILD

1: Standard mapping rebuild. Retains existing triggers and modifiers for actions that were previously mapped.

<a id="unreal.InputMappingRebuildType.REBUILD_WITH_FLUSH"></a>

#### REBUILD_WITH_FLUSH

2: If you have made changes to the triggers/modifiers associated with a UInputAction that was previously mapped a flush is required to reset the tracked data for that action.

<a id="unreal.InputActionAccumulationBehavior"></a>