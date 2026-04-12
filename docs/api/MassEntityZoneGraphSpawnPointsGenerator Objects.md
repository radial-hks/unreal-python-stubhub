## MassEntityZoneGraphSpawnPointsGenerator Objects

```python
class MassEntityZoneGraphSpawnPointsGenerator(MassEntitySpawnDataGeneratorBase
                                              )
```

Describes the SpawnPoints Generator when we want to spawn directly on Zone Graph

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSpawner
- **File**: MassEntityZoneGraphSpawnPointsGenerator.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_gap`` (float):  [Read-Write] Maximum gap for spawning entities on a given lanes
- ``min_gap`` (float):  [Read-Write] Minimum gap for spawning entities on a given lanes
- ``random_selection_seed`` (int32):  [Read-Write]
- ``tag_filter`` (ZoneGraphTagFilter):  [Read-Write] Tags to filter which lane to use to generate points on

<a id="unreal.MassSpawner"></a>