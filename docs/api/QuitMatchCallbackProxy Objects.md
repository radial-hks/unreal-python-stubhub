## QuitMatchCallbackProxy Objects

```python
class QuitMatchCallbackProxy(OnlineBlueprintCallProxyBase)
```

Quit Match Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: QuitMatchCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (EmptyOnlineDelegate):  [Read-Write] Called when there is an unsuccessful query
- ``on_success`` (EmptyOnlineDelegate):  [Read-Write] Called when there is a successful query

<a id="unreal.QuitMatchCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when there is a successful query

<a id="unreal.QuitMatchCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.QuitMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when there is an unsuccessful query

<a id="unreal.QuitMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.ShowLoginUICallbackProxy"></a>