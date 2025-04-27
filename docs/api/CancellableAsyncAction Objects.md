## CancellableAsyncAction Objects

```python
class CancellableAsyncAction(BlueprintAsyncActionBase)
```

base class for asynchronous actions that can be spawned from UK2Node_AsyncAction or C++ code.
These actions register themselves with the game instance and need to be explicitly canceled or ended normally to go away.
The ExposedAsyncProxy metadata specifies the blueprint node will return this object for later canceling.

**C++ Source:**

- **Module**: Engine
- **File**: CancellableAsyncAction.h

<a id="unreal.CancellableAsyncAction.is_active"></a>

#### is_active

```python
def is_active() -> bool
```

x.is_active() -> bool
Returns true if this action is still active and has not completed or been cancelled

Returns:
    bool:

<a id="unreal.CancellableAsyncAction.cancel"></a>

#### cancel

```python
def cancel() -> None
```

x.cancel() -> None
Cancel an asynchronous action, this attempts to cancel any lower level processes and also prevents delegates from being fired

<a id="unreal.ServerStatReplicator"></a>