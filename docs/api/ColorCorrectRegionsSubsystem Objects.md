## ColorCorrectRegionsSubsystem Objects

```python
class ColorCorrectRegionsSubsystem(TickableWorldSubsystem)
```

World Subsystem responsible for managing AColorCorrectRegion classes in level.
This subsystem handles:
            Level Loaded, Undo/Redo, Added to level, Removed from level events.
Unfortunately AActor class itself is not aware of when it is added/removed, Undo/Redo etc in the level.

This is the only way (that we found) that was handling all region aggregation cases in more or less efficient way.
            Covered cases: Region added to a level, deleted from level, level loaded, undo, redo, level closed, editor closed:
            World subsystem keeps track of all Regions in a level via three events OnLevelActorAdded, OnLevelActorDeleted, OnLevelActorListChanged.
            Actor classes are unaware of when they are added/deleted/undo/redo etc in the level, therefore this is the best place to manage this.
Alternative strategies (All tested):
            World's AddOnActorSpawnedHandler. Flawed. Invoked in some cases we don't need, but does not get called during UNDO/REDO
            AActor's PostSpawnInitialize, PostActorCreated  and OnConstruction are also flawed.
            AActor does not have an internal event for when its deleted (EndPlay is the closest we have).

**C++ Source:**

- **Plugin**: ColorCorrectRegions
- **Module**: ColorCorrectRegions
- **File**: ColorCorrectRegionsSubsystem.h

<a id="unreal.ColorCorrectRegionsSubsystem.refresh_stenci_id_assignment_for_all_ccr"></a>

#### refresh_stenci_id_assignment_for_all_ccr

```python
def refresh_stenci_id_assignment_for_all_ccr() -> None
```

x.refresh_stenci_id_assignment_for_all_ccr() -> None
Refresh Stenci Id Assignment for All CCR

<a id="unreal.ColorCorrectionWindow"></a>