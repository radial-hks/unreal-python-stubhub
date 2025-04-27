## Async_SetTimer Objects

```python
class Async_SetTimer(BlueprintAsyncActionBase)
```

// UCLASS(meta = (HideThen = false))

**C++ Source:**

- **Plugin**: SunFunctionLibrary
- **Module**: AsyncNode
- **File**: Async_SetTimer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``completed`` (TimerHandleDelegate):  [Read-Write] Generate Exec Outpin, named Completed
- ``then`` (TimerHandleDelegate):  [Read-Write] Generate Exec Outpin, named Then

<a id="unreal.Async_SetTimer.then"></a>

#### then

```python
@property
def then() -> TimerHandleDelegate
```

(TimerHandleDelegate):  [Read-Write] Generate Exec Outpin, named Then

<a id="unreal.Async_SetTimer.then"></a>

#### then

```python
@then.setter
def then(value: TimerHandleDelegate) -> None
```

<a id="unreal.Async_SetTimer.completed"></a>

#### completed

```python
@property
def completed() -> TimerHandleDelegate
```

(TimerHandleDelegate):  [Read-Write] Generate Exec Outpin, named Completed

<a id="unreal.Async_SetTimer.completed"></a>

#### completed

```python
@completed.setter
def completed(value: TimerHandleDelegate) -> None
```

<a id="unreal.VersionInfoHandler"></a>