## TakeRecorderNearbySpawnedActorSource Objects

```python
class TakeRecorderNearbySpawnedActorSource(TakeRecorderSource)
```

A recording source that detects actors spawned close to the current camera, and captures them as spawnables

**C++ Source:**

- **Plugin**: Takes
- **Module**: TakeRecorderSources
- **File**: TakeRecorderNearbySpawnedActorSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write] True if this source is cued for recording or not
- ``filter_spawned_actors`` (bool):  [Read-Write] Should we only record actors that pass the filter list?
- ``filter_types`` (Array[type(Class)]):  [Read-Write] A type filter to apply to spawned objects
- ``proximity`` (float):  [Read-Write] The proximity to the current camera that an actor must be spawned in order to be recorded as a spawnable. If 0, proximity is disregarded.
- ``take_number`` (int32):  [Read-Write]
- ``track_tint`` (Color):  [Read-Write]

<a id="unreal.TakeRecorderNearbySpawnedActorSource.proximity"></a>

#### proximity

```python
@property
def proximity() -> float
```

(float):  [Read-Write] The proximity to the current camera that an actor must be spawned in order to be recorded as a spawnable. If 0, proximity is disregarded.

<a id="unreal.TakeRecorderNearbySpawnedActorSource.proximity"></a>

#### proximity

```python
@proximity.setter
def proximity(value: float) -> None
```

<a id="unreal.TakeRecorderNearbySpawnedActorSource.filter_spawned_actors"></a>

#### filter_spawned_actors

```python
@property
def filter_spawned_actors() -> bool
```

(bool):  [Read-Write] Should we only record actors that pass the filter list?

<a id="unreal.TakeRecorderNearbySpawnedActorSource.filter_spawned_actors"></a>

#### filter_spawned_actors

```python
@filter_spawned_actors.setter
def filter_spawned_actors(value: bool) -> None
```

<a id="unreal.TakeRecorderNearbySpawnedActorSource.filter_types"></a>

#### filter_types

```python
@property
def filter_types() -> Array[Class]
```

(Array[type(Class)]):  [Read-Write] A type filter to apply to spawned objects

<a id="unreal.TakeRecorderNearbySpawnedActorSource.filter_types"></a>

#### filter_types

```python
@filter_types.setter
def filter_types(value: Array[Class]) -> None
```

<a id="unreal.TakeRecorderPlayerSource"></a>