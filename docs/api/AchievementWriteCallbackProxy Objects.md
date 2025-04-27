## AchievementWriteCallbackProxy Objects

```python
class AchievementWriteCallbackProxy(OnlineBlueprintCallProxyBase)
```

Achievement Write Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: AchievementWriteCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (AchievementWriteDelegate):  [Read-Write]
  deprecated: Use OnWriteFailure instead.
- ``on_success`` (AchievementWriteDelegate):  [Read-Write]
  deprecated: Use OnWriteSuccess instead.
- ``on_write_failure`` (AchievementWriteCompleteDelegate):  [Read-Write] Called when there is an unsuccessful achievement write
- ``on_write_success`` (AchievementWriteCompleteDelegate):  [Read-Write] Called when there is a successful achievement write

<a id="unreal.AchievementWriteCallbackProxy.on_write_success"></a>

#### on_write_success

```python
@property
def on_write_success() -> AchievementWriteCompleteDelegate
```

(AchievementWriteCompleteDelegate):  [Read-Write] Called when there is a successful achievement write

<a id="unreal.AchievementWriteCallbackProxy.on_write_success"></a>

#### on_write_success

```python
@on_write_success.setter
def on_write_success(value: AchievementWriteCompleteDelegate) -> None
```

<a id="unreal.AchievementWriteCallbackProxy.on_write_failure"></a>

#### on_write_failure

```python
@property
def on_write_failure() -> AchievementWriteCompleteDelegate
```

(AchievementWriteCompleteDelegate):  [Read-Write] Called when there is an unsuccessful achievement write

<a id="unreal.AchievementWriteCallbackProxy.on_write_failure"></a>

#### on_write_failure

```python
@on_write_failure.setter
def on_write_failure(value: AchievementWriteCompleteDelegate) -> None
```

<a id="unreal.AchievementWriteCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> AchievementWriteDelegate
```

(AchievementWriteDelegate):  [Read-Write]
deprecated: Use OnWriteSuccess instead.

<a id="unreal.AchievementWriteCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: AchievementWriteDelegate) -> None
```

<a id="unreal.AchievementWriteCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> AchievementWriteDelegate
```

(AchievementWriteDelegate):  [Read-Write]
deprecated: Use OnWriteFailure instead.

<a id="unreal.AchievementWriteCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: AchievementWriteDelegate) -> None
```

<a id="unreal.ConnectionCallbackProxy"></a>