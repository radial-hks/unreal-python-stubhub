## MassEntitySpawnDataGeneratorBase Objects

```python
class MassEntitySpawnDataGeneratorBase(Object)
```

Base class for Mass Entity Spawn Points Generator.
A Mass Spawn Points Generator can be of several type (EQS, ZoneGraph, Volume, Area, etc.)
The concept is to override the GenerateSpawnPoints() method and requesting a certain number of Spawn Point Locations to the method.

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassSpawner
- **File**: MassEntitySpawnDataGeneratorBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``random_selection_seed`` (int32):  [Read-Write]

<a id="unreal.MassEntityEQSSpawnPointsGenerator"></a>