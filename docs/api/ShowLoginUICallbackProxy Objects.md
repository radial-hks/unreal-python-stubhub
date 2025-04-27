## ShowLoginUICallbackProxy Objects

```python
class ShowLoginUICallbackProxy(BlueprintAsyncActionBase)
```

Show Login UICallback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: ShowLoginUICallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineShowLoginUIResult):  [Read-Write] Called when there is an unsuccessful query
- ``on_success`` (OnlineShowLoginUIResult):  [Read-Write] Called when there is a successful query

<a id="unreal.ShowLoginUICallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnlineShowLoginUIResult
```

(OnlineShowLoginUIResult):  [Read-Write] Called when there is a successful query

<a id="unreal.ShowLoginUICallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnlineShowLoginUIResult) -> None
```

<a id="unreal.ShowLoginUICallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnlineShowLoginUIResult
```

(OnlineShowLoginUIResult):  [Read-Write] Called when there is an unsuccessful query

<a id="unreal.ShowLoginUICallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnlineShowLoginUIResult) -> None
```

<a id="unreal.SpectatorBeaconClient"></a>