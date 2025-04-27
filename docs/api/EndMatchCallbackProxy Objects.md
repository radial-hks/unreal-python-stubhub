## EndMatchCallbackProxy Objects

```python
class EndMatchCallbackProxy(OnlineBlueprintCallProxyBase)
```

End Match Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: EndMatchCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (EmptyOnlineDelegate):  [Read-Write] Called when ending the match fails
- ``on_success`` (EmptyOnlineDelegate):  [Read-Write] Called when the match ends successfully

<a id="unreal.EndMatchCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when the match ends successfully

<a id="unreal.EndMatchCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.EndMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> EmptyOnlineDelegate
```

(EmptyOnlineDelegate):  [Read-Write] Called when ending the match fails

<a id="unreal.EndMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: EmptyOnlineDelegate) -> None
```

<a id="unreal.EndTurnCallbackProxy"></a>