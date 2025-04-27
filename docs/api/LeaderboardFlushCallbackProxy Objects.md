## LeaderboardFlushCallbackProxy Objects

```python
class LeaderboardFlushCallbackProxy(Object)
```

Leaderboard Flush Callback Proxy

**C++ Source:**

- **Plugin**: OnlineSubsystemUtils
- **Module**: OnlineSubsystemUtils
- **File**: LeaderboardFlushCallbackProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_failure`` (OnLeaderboardFlushed):  [Read-Write] Called when there is an unsuccessful leaderboard flush
- ``on_success`` (OnLeaderboardFlushed):  [Read-Write] Called when there is a successful leaderboard flush

<a id="unreal.LeaderboardFlushCallbackProxy.on_success"></a>

#### on_success

```python
@property
def on_success() -> OnLeaderboardFlushed
```

(OnLeaderboardFlushed):  [Read-Write] Called when there is a successful leaderboard flush

<a id="unreal.LeaderboardFlushCallbackProxy.on_success"></a>

#### on_success

```python
@on_success.setter
def on_success(value: OnLeaderboardFlushed) -> None
```

<a id="unreal.LeaderboardFlushCallbackProxy.on_failure"></a>

#### on_failure

```python
@property
def on_failure() -> OnLeaderboardFlushed
```

(OnLeaderboardFlushed):  [Read-Write] Called when there is an unsuccessful leaderboard flush

<a id="unreal.LeaderboardFlushCallbackProxy.on_failure"></a>

#### on_failure

```python
@on_failure.setter
def on_failure(value: OnLeaderboardFlushed) -> None
```

<a id="unreal.LeaderboardQueryCallbackProxy"></a>