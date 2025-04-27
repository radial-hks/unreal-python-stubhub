## BlueprintAsyncActionBase Objects

```python
class BlueprintAsyncActionBase(Object)
```

BlueprintCallable factory functions for classes which inherit from UBlueprintAsyncActionBase will have a special blueprint node created for it: UK2Node_AsyncAction
You can stop this node spawning and create a more specific one by adding the UCLASS metadata "HasDedicatedAsyncNode"

**C++ Source:**

- **Module**: Engine
- **File**: BlueprintAsyncActionBase.h

<a id="unreal.AsyncTaskDownloadImage"></a>