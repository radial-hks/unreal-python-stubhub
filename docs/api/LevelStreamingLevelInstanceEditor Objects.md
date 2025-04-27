## LevelStreamingLevelInstanceEditor Objects

```python
class LevelStreamingLevelInstanceEditor(LevelStreamingAlwaysLoaded)
```

Level Streaming Level Instance Editor

**C++ Source:**

- **Module**: Engine
- **File**: LevelInstanceEditorLevelStreaming.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disable_distance_streaming`` (bool):  [Read-Write] Whether this level streaming object should be ignored by world composition distance streaming,
  so streaming state can be controlled by other systems (ex: in blueprints)
- ``draw_on_level_status_map`` (bool):  [Read-Write] If true, will be drawn on the 'level streaming status' map (STAT LEVELMAP console command)
- ``editor_streaming_volumes`` (Array[LevelStreamingVolume]):  [Read-Write] The level streaming volumes bound to this level.
- ``is_static`` (bool):  [Read-Write] Whether this level only contains static actors that aren't affected by gameplay or replication.
  If true, the engine can make certain optimizations and will add this level to the StaticLevels collection.
- ``level_color`` (LinearColor):  [Read-Write] The level color used for visualization. (Show -> Advanced -> Level Coloration)
- ``level_lod_index`` (int32):  [Read-Write] Requested LOD. Non LOD sub-levels have Index = -1
- ``level_transform`` (Transform):  [Read-Write] Transform applied to actors after loading.
- ``min_time_between_volume_unload_requests`` (float):  [Read-Write] Cooldown time in seconds between volume-based unload requests.  Used in preventing spurious unload requests.
- ``on_level_hidden`` (LevelStreamingVisibilityStatus):  [Read-Write] Called when level is no longer visible, may not be removed from world yet
- ``on_level_loaded`` (LevelStreamingLoadedStatus):  [Read-Write] Called when level is streamed in
- ``on_level_shown`` (LevelStreamingVisibilityStatus):  [Read-Write] Called when level is added to the world and is visible
- ``on_level_unloaded`` (LevelStreamingLoadedStatus):  [Read-Write] Called when level is streamed out
- ``should_be_loaded`` (bool):  [Read-Write] Whether the level should be loaded
- ``should_be_visible`` (bool):  [Read-Write] Whether the level should be visible if it is loaded
- ``should_block_on_load`` (bool):  [Read-Write] Whether we want to force a blocking load
- ``should_block_on_unload`` (bool):  [Read-Write] Whether we want to force a blocking unload
- ``streaming_priority`` (int32):  [Read-Write] The relative priority of considering the streaming level. Changing the priority will not interrupt the currently considered level, but will affect the next time a level is being selected for evaluation.
- ``world_asset`` (World):  [Read-Only] The reference to the world containing the level to load

<a id="unreal.LevelInstancePivot"></a>