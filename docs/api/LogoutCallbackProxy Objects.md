## LogoutCallbackProxy Objects

```python
class LogoutCallbackProxy(BlueprintAsyncActionBase)
```

Logout Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: LogoutCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineLogoutResult):  [Read-Write] Called when the logout completed unsuccessfully
- ``on_success`` (OnlineLogoutResult):  [Read-Write] Called when the logout completed successfully

<a id="unreal.LogoutCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnlineLogoutResult
```

(OnlineLogoutResult):  [Read-Write] Called when the logout completed successfully

<a id="unreal.LogoutCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnlineLogoutResult) -> None
```

<a id="unreal.LogoutCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnlineLogoutResult
```

(OnlineLogoutResult):  [Read-Write] Called when the logout completed unsuccessfully

<a id="unreal.LogoutCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnlineLogoutResult) -> None
```

<a id="unreal.OnlineBeacon"></a>