## ConnectionCallbackProxy Objects

```python
class ConnectionCallbackProxy(OnlineBlueprintCallProxyBase)
```

Connection Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: ConnectionCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineConnectionResult):  [Read-Write] Called when there is an unsuccessful query
- ``on_success`` (OnlineConnectionResult):  [Read-Write] Called when there is a successful query

<a id="unreal.ConnectionCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnlineConnectionResult
```

(OnlineConnectionResult):  [Read-Write] Called when there is a successful query

<a id="unreal.ConnectionCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnlineConnectionResult) -> None
```

<a id="unreal.ConnectionCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnlineConnectionResult
```

(OnlineConnectionResult):  [Read-Write] Called when there is an unsuccessful query

<a id="unreal.ConnectionCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnlineConnectionResult) -> None
```

<a id="unreal.CreateSessionCallbackProxy"></a>