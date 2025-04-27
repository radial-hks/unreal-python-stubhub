## LevelStreamingDynamic Objects

```python
class LevelStreamingDynamic(LevelStreaming)
```

Level Streaming Dynamic

**C++ Source:**

- **Module**: Engine
- **File**: LevelStreamingDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``disable_distance_streaming`` (bool):  [Read-Write] Whether this level streaming object should be ignored by world composition distance streaming,
  so streaming state can be controlled by other systems (ex: in blueprints)
- ``draw_on_level_status_map`` (bool):  [Read-Write] If true, will be drawn on the 'level streaming status' map (STAT LEVELMAP console command)
- ``editor_streaming_volumes`` (Array[LevelStreamingVolume]):  [Read-Write] The level streaming volumes bound to this level.
- ``initially_loaded`` (bool):  [Read-Write] Whether the level should be loaded at startup
- ``initially_visible`` (bool):  [Read-Write] Whether the level should be visible at startup if it is loaded
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

<a id="unreal.LevelStreamingDynamic.load_level_instance_by_soft_object_ptr"></a>

#### load_level_instance_by_soft_object_ptr

```python
@classmethod
def load_level_instance_by_soft_object_ptr(
        cls,
        world_context_object: Object,
        level: World,
        location: Vector,
        rotation: Rotator,
        optional_level_name_override: str = "",
        optional_level_streaming_class: Class = None,
        load_as_temp_package: bool = False
) -> Tuple[LevelStreamingDynamic, bool]
```

X.load_level_instance_by_soft_object_ptr(world_context_object, level, location, rotation, optional_level_name_override="", optional_level_streaming_class=None, load_as_temp_package=False) -> (LevelStreamingDynamic, out_success=bool)
Load Level Instance by Soft Object Ptr

Args:
    world_context_object (Object): 
    level (World): 
    location (Vector): 
    rotation (Rotator): 
    optional_level_name_override (str): 
    optional_level_streaming_class (type(Class)): 
    load_as_temp_package (bool): 

Returns:
    bool: 

    out_success (bool):

<a id="unreal.LevelStreamingDynamic.load_level_instance"></a>

#### load_level_instance

```python
@classmethod
def load_level_instance(
        cls,
        world_context_object: Object,
        level_name: str,
        location: Vector,
        rotation: Rotator,
        optional_level_name_override: str = "",
        optional_level_streaming_class: Class = None,
        load_as_temp_package: bool = False
) -> Tuple[LevelStreamingDynamic, bool]
```

X.load_level_instance(world_context_object, level_name, location, rotation, optional_level_name_override="", optional_level_streaming_class=None, load_as_temp_package=False) -> (LevelStreamingDynamic, out_success=bool)
Stream in a level with a specific location and rotation. You can create multiple instances of the same level!

The level to be loaded does not have to be in the persistent map's Levels list, however to ensure that the .umap does get
packaged, please be sure to include the .umap in your Packaging Settings:

  Project Settings -> Packaging -> List of Maps to Include in a Packaged Build (you may have to show advanced or type in filter)

Args:
    world_context_object (Object): 
    level_name (str): Level package name to load, ex: /Game/Maps/MyMapName, specifying short name like MyMapName will force very slow search on disk
    location (Vector): World space location where the level should be spawned
    rotation (Rotator): World space rotation for rotating the entire level
    optional_level_name_override (str): If set, the loaded level package have this name, which is used by other functions like UnloadStreamLevel. Note this is necessary for server and client networking because the level must have the same name on both.
    optional_level_streaming_class (type(Class)): If set, the level streaming class will be used instead of ULevelStreamingDynamic
    load_as_temp_package (bool): If set, package path is prefixed by /Temp

Returns:
    bool: Streaming level object for a level instance

    out_success (bool): Whether operation was successful (map was found and added to the sub-levels list)

<a id="unreal.LevelStreamingKismet"></a>