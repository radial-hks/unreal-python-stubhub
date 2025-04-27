## AsyncActionHandleSaveGame Objects

```python
class AsyncActionHandleSaveGame(BlueprintAsyncActionBase)
```

Async action to handle async load/save of a USaveGame. This can be subclassed by a specific game

**C++ Source:**

- **Module**: Engine
- **File**: AsyncActionHandleSaveGame.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``completed`` (OnAsyncHandleSaveGame):  [Read-Write] Delegate called when the save/load completes

<a id="unreal.AsyncActionHandleSaveGame.completed"></a>

#### completed

```python
@property
def completed() -> OnAsyncHandleSaveGame
```

(OnAsyncHandleSaveGame):  [Read-Write] Delegate called when the save/load completes

<a id="unreal.AsyncActionHandleSaveGame.completed"></a>

#### completed

```python
@completed.setter
def completed(value: OnAsyncHandleSaveGame) -> None
```

<a id="unreal.ForceFeedbackEffect"></a>