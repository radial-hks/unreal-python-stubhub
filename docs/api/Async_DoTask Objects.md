## Async_DoTask Objects

```python
class Async_DoTask(BlueprintAsyncActionBase)
```

Async Do Task

**C++ Source:**

- **Plugin**: SunFunctionLibrary
- **Module**: AsyncNode
- **File**: Async_DoTask.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_fail`` (TaskDelegate):  [Read-Write]
- ``on_success`` (TaskDelegate):  [Read-Write]

<a id="unreal.Async_DoTask.on_success"></a>

#### on_success

```python
@property
def on_success() -> TaskDelegate
```

(TaskDelegate):  [Read-Write]

<a id="unreal.Async_DoTask.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: TaskDelegate) -> None
```

<a id="unreal.Async_DoTask.on_fail"></a>

#### on_fail

```python
@property
def on_fail() -> TaskDelegate
```

(TaskDelegate):  [Read-Write]

<a id="unreal.Async_DoTask.on_fail"></a>

#### on_fail

```python
@on_fail.setter
def on_fail(value: TaskDelegate) -> None
```

<a id="unreal.Async_SetTimer"></a>