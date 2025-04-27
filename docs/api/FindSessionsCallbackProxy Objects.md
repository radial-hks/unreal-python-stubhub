## FindSessionsCallbackProxy Objects

```python
class FindSessionsCallbackProxy(OnlineBlueprintCallProxyBase)
```

Find Sessions Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: FindSessionsCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (BlueprintFindSessionsResultDelegate):  [Read-Write] Called when there is an unsuccessful query
- ``on_success`` (BlueprintFindSessionsResultDelegate):  [Read-Write] Called when there is a successful query

<a id="unreal.FindSessionsCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> BlueprintFindSessionsResultDelegate
```

(BlueprintFindSessionsResultDelegate):  [Read-Write] Called when there is a successful query

<a id="unreal.FindSessionsCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: BlueprintFindSessionsResultDelegate) -> None
```

<a id="unreal.FindSessionsCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> BlueprintFindSessionsResultDelegate
```

(BlueprintFindSessionsResultDelegate):  [Read-Write] Called when there is an unsuccessful query

<a id="unreal.FindSessionsCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: BlueprintFindSessionsResultDelegate) -> None
```

<a id="unreal.FindSessionsCallbackProxy.get_server_name"></a>

#### get_server_name

```python
@classmethod
def get_server_name(cls, result: BlueprintSessionResult) -> str
```

X.get_server_name(result) -> str
Get Server Name

Args:
    result (BlueprintSessionResult): 

Returns:
    str:

<a id="unreal.FindSessionsCallbackProxy.get_ping_in_ms"></a>

#### get_ping_in_ms

```python
@classmethod
def get_ping_in_ms(cls, result: BlueprintSessionResult) -> int
```

X.get_ping_in_ms(result) -> int32
Get Ping in Ms

Args:
    result (BlueprintSessionResult): 

Returns:
    int32:

<a id="unreal.FindSessionsCallbackProxy.get_max_players"></a>

#### get_max_players

```python
@classmethod
def get_max_players(cls, result: BlueprintSessionResult) -> int
```

X.get_max_players(result) -> int32
Get Max Players

Args:
    result (BlueprintSessionResult): 

Returns:
    int32:

<a id="unreal.FindSessionsCallbackProxy.get_current_players"></a>

#### get_current_players

```python
@classmethod
def get_current_players(cls, result: BlueprintSessionResult) -> int
```

X.get_current_players(result) -> int32
Get Current Players

Args:
    result (BlueprintSessionResult): 

Returns:
    int32:

<a id="unreal.FindTurnBasedMatchCallbackProxy"></a>