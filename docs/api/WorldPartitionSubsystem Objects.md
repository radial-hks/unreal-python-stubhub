## WorldPartitionSubsystem Objects

```python
class WorldPartitionSubsystem(TickableWorldSubsystem)
```

UWorldPartitionSubsystem

**C++ Source:**

- **Module**: Engine
- **File**: WorldPartitionSubsystem.h

<a id="unreal.WorldPartitionSubsystem.is_streaming_completed"></a>

#### is_streaming_completed

```python
def is_streaming_completed(
        query_state: WorldPartitionRuntimeCellState,
        query_sources: Array[WorldPartitionStreamingQuerySource],
        exact_state: bool) -> bool
```

x.is_streaming_completed(query_state, query_sources, exact_state) -> bool
Is Streaming Completed

Args:
    query_state (WorldPartitionRuntimeCellState): 
    query_sources (Array[WorldPartitionStreamingQuerySource]): 
    exact_state (bool): 

Returns:
    bool:

<a id="unreal.WorldPartitionSubsystem.is_all_streaming_completed"></a>

#### is_all_streaming_completed

```python
def is_all_streaming_completed() -> bool
```

x.is_all_streaming_completed() -> bool
Returns true if world partition is done streaming levels, adding them to the world or removing them from the world.

Returns:
    bool:

<a id="unreal.WorldPartitionVolume"></a>