## HealthSnapshotBlueprintLibrary Objects

```python
class HealthSnapshotBlueprintLibrary(BlueprintFunctionLibrary)
```

Health Snapshot Blueprint Library

**C++ Source:**

- **Module**: Engine
- **File**: HealthSnapshot.h

<a id="unreal.HealthSnapshotBlueprintLibrary.stop_performance_snapshots"></a>

#### stop_performance_snapshots

```python
@classmethod
def stop_performance_snapshots(cls) -> None
```

X.stop_performance_snapshots() -> None
Stops capturing FPS charts only if StartHealthSnapshotChart has first been called. Does nothing if FPS charts are not running. HealthSnapshots captured after this is called will not include performance stats.

<a id="unreal.HealthSnapshotBlueprintLibrary.start_performance_snapshots"></a>

#### start_performance_snapshots

```python
@classmethod
def start_performance_snapshots(cls) -> None
```

X.start_performance_snapshots() -> None
Begins capturing FPS charts that can be used to include performance data in a HealthSnapshot. If snapshots are already running clears all accumulated performance data

<a id="unreal.HealthSnapshotBlueprintLibrary.log_performance_snapshot"></a>

#### log_performance_snapshot

```python
@classmethod
def log_performance_snapshot(cls,
                             snapshot_title: str,
                             reset_stats: bool = True) -> None
```

X.log_performance_snapshot(snapshot_title, reset_stats=True) -> None
Writes a snapshot to the log. Captures memory stats by default. Also captures performance stats if called after StartHealthSnapshotChart and before SopHealthSnapshotChart.

Args:
    snapshot_title (str): The name to be given to the new HealthSnapshot.
    reset_stats (bool):

<a id="unreal.RectLight"></a>