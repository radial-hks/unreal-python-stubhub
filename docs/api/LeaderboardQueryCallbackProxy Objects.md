## LeaderboardQueryCallbackProxy Objects

```python
class LeaderboardQueryCallbackProxy(Object)
```

Leaderboard Query Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: LeaderboardQueryCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (LeaderboardQueryResult):  [Read-Write] Called when there is an unsuccessful leaderboard query
- ``on_success`` (LeaderboardQueryResult):  [Read-Write] Called when there is a successful leaderboard query

<a id="unreal.LeaderboardQueryCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> LeaderboardQueryResult
```

(LeaderboardQueryResult):  [Read-Write] Called when there is a successful leaderboard query

<a id="unreal.LeaderboardQueryCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: LeaderboardQueryResult) -> None
```

<a id="unreal.LeaderboardQueryCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> LeaderboardQueryResult
```

(LeaderboardQueryResult):  [Read-Write] Called when there is an unsuccessful leaderboard query

<a id="unreal.LeaderboardQueryCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: LeaderboardQueryResult) -> None
```

<a id="unreal.LogoutCallbackProxy"></a>