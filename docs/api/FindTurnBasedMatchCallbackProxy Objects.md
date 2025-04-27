## FindTurnBasedMatchCallbackProxy Objects

```python
class FindTurnBasedMatchCallbackProxy(OnlineBlueprintCallProxyBase)
```

Find Turn Based Match Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: FindTurnBasedMatchCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnlineTurnBasedMatchResult):  [Read-Write] Called when matchmaking failed
- ``on_success`` (OnlineTurnBasedMatchResult):  [Read-Write] Called when matchmaking succeeded.

<a id="unreal.FindTurnBasedMatchCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnlineTurnBasedMatchResult
```

(OnlineTurnBasedMatchResult):  [Read-Write] Called when matchmaking succeeded.

<a id="unreal.FindTurnBasedMatchCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnlineTurnBasedMatchResult) -> None
```

<a id="unreal.FindTurnBasedMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnlineTurnBasedMatchResult
```

(OnlineTurnBasedMatchResult):  [Read-Write] Called when matchmaking failed

<a id="unreal.FindTurnBasedMatchCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnlineTurnBasedMatchResult) -> None
```

<a id="unreal.InAppPurchaseCallbackProxy2"></a>