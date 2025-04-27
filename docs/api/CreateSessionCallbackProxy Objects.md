## CreateSessionCallbackProxy Objects

```python
class CreateSessionCallbackProxy(OnlineBlueprintCallProxyBase)
```

Create Session Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: CreateSessionCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (EmptyOnlineDelegate):  [Read-Write] Called when there was an error creating the session
- ``on_success`` (EmptyOnlineDelegate):  [Read-Write] Called when the session was created successfully

<a id="unreal.CreateSessionCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when the session was created successfully

<a id="unreal.CreateSessionCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.CreateSessionCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when there was an error creating the session

<a id="unreal.CreateSessionCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.DestroySessionCallbackProxy"></a>