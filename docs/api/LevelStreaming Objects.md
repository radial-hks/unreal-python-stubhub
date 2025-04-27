## LevelStreaming Objects

```python
class LevelStreaming(Object)
```

Abstract base class of container object encapsulating data required for streaming and providing
interface for when a level should be streamed in and out of memory.

**C++ Source:**

- **Module**: Engine
- **File**: LevelStreaming.h

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

<a id="unreal.LevelStreaming.world_asset"></a>

#### world_asset

```python
@property
def world_asset() -> World
```

(World):  [Read-Only] The reference to the world containing the level to load

<a id="unreal.LevelStreaming.streaming_priority"></a>

#### streaming_priority

```python
@property
def streaming_priority() -> int
```

(int32):  [Read-Write] The relative priority of considering the streaming level. Changing the priority will not interrupt the currently considered level, but will affect the next time a level is being selected for evaluation.

<a id="unreal.LevelStreaming.streaming_priority"></a>

#### streaming_priority

```python
@streaming_priority.setter
def streaming_priority(value: int) -> None
```

<a id="unreal.LevelStreaming.level_transform"></a>

#### level_transform

```python
@property
def level_transform() -> Transform
```

(Transform):  [Read-Write] Transform applied to actors after loading.

<a id="unreal.LevelStreaming.level_transform"></a>

#### level_transform

```python
@level_transform.setter
def level_transform(value: Transform) -> None
```

<a id="unreal.LevelStreaming.level_lod_index"></a>

#### level_lod_index

```python
@property
def level_lod_index() -> int
```

(int32):  [Read-Write] Requested LOD. Non LOD sub-levels have Index = -1

<a id="unreal.LevelStreaming.level_lod_index"></a>

#### level_lod_index

```python
@level_lod_index.setter
def level_lod_index(value: int) -> None
```

<a id="unreal.LevelStreaming.should_be_visible"></a>

#### should_be_visible

```python
@property
def should_be_visible() -> bool
```

(bool):  [Read-Write] Whether the level should be visible if it is loaded

<a id="unreal.LevelStreaming.should_be_visible"></a>

#### should_be_visible

```python
@should_be_visible.setter
def should_be_visible(value: bool) -> None
```

<a id="unreal.LevelStreaming.should_be_loaded"></a>

#### should_be_loaded

```python
@property
def should_be_loaded() -> bool
```

(bool):  [Read-Write] Whether the level should be loaded

<a id="unreal.LevelStreaming.should_be_loaded"></a>

#### should_be_loaded

```python
@should_be_loaded.setter
def should_be_loaded(value: bool) -> None
```

<a id="unreal.LevelStreaming.should_block_on_load"></a>

#### should_block_on_load

```python
@property
def should_block_on_load() -> bool
```

(bool):  [Read-Write] Whether we want to force a blocking load

<a id="unreal.LevelStreaming.should_block_on_load"></a>

#### should_block_on_load

```python
@should_block_on_load.setter
def should_block_on_load(value: bool) -> None
```

<a id="unreal.LevelStreaming.should_block_on_unload"></a>

#### should_block_on_unload

```python
@property
def should_block_on_unload() -> bool
```

(bool):  [Read-Write] Whether we want to force a blocking unload

<a id="unreal.LevelStreaming.should_block_on_unload"></a>

#### should_block_on_unload

```python
@should_block_on_unload.setter
def should_block_on_unload(value: bool) -> None
```

<a id="unreal.LevelStreaming.disable_distance_streaming"></a>

#### disable_distance_streaming

```python
@property
def disable_distance_streaming() -> bool
```

(bool):  [Read-Write] Whether this level streaming object should be ignored by world composition distance streaming,
so streaming state can be controlled by other systems (ex: in blueprints)

<a id="unreal.LevelStreaming.disable_distance_streaming"></a>

#### disable_distance_streaming

```python
@disable_distance_streaming.setter
def disable_distance_streaming(value: bool) -> None
```

<a id="unreal.LevelStreaming.on_level_loaded"></a>

#### on_level_loaded

```python
@property
def on_level_loaded() -> LevelStreamingLoadedStatus
```

(LevelStreamingLoadedStatus):  [Read-Write] Called when level is streamed in

<a id="unreal.LevelStreaming.on_level_loaded"></a>

#### on_level_loaded

```python
@on_level_loaded.setter
def on_level_loaded(value: LevelStreamingLoadedStatus) -> None
```

<a id="unreal.LevelStreaming.on_level_unloaded"></a>

#### on_level_unloaded

```python
@property
def on_level_unloaded() -> LevelStreamingLoadedStatus
```

(LevelStreamingLoadedStatus):  [Read-Write] Called when level is streamed out

<a id="unreal.LevelStreaming.on_level_unloaded"></a>

#### on_level_unloaded

```python
@on_level_unloaded.setter
def on_level_unloaded(value: LevelStreamingLoadedStatus) -> None
```

<a id="unreal.LevelStreaming.on_level_shown"></a>

#### on_level_shown

```python
@property
def on_level_shown() -> LevelStreamingVisibilityStatus
```

(LevelStreamingVisibilityStatus):  [Read-Write] Called when level is added to the world and is visible

<a id="unreal.LevelStreaming.on_level_shown"></a>

#### on_level_shown

```python
@on_level_shown.setter
def on_level_shown(value: LevelStreamingVisibilityStatus) -> None
```

<a id="unreal.LevelStreaming.on_level_hidden"></a>

#### on_level_hidden

```python
@property
def on_level_hidden() -> LevelStreamingVisibilityStatus
```

(LevelStreamingVisibilityStatus):  [Read-Write] Called when level is no longer visible, may not be removed from world yet

<a id="unreal.LevelStreaming.on_level_hidden"></a>

#### on_level_hidden

```python
@on_level_hidden.setter
def on_level_hidden(value: LevelStreamingVisibilityStatus) -> None
```

<a id="unreal.LevelStreaming.set_is_requesting_unload_and_removal"></a>

#### set_is_requesting_unload_and_removal

```python
def set_is_requesting_unload_and_removal(
        is_requesting_unload_and_removal: bool) -> None
```

x.set_is_requesting_unload_and_removal(is_requesting_unload_and_removal) -> None
Sets if the streaming level should be unloaded and removed.

Args:
    is_requesting_unload_and_removal (bool):

<a id="unreal.LevelStreaming.is_streaming_state_pending"></a>

#### is_streaming_state_pending

```python
def is_streaming_state_pending() -> bool
```

x.is_streaming_state_pending() -> bool
Returns whether level has streaming state change pending

Returns:
    bool:

<a id="unreal.LevelStreaming.is_level_visible"></a>

#### is_level_visible

```python
def is_level_visible() -> bool
```

x.is_level_visible() -> bool
Returns whether streaming level is visible

Returns:
    bool:

<a id="unreal.LevelStreaming.is_level_loaded"></a>

#### is_level_loaded

```python
def is_level_loaded() -> bool
```

x.is_level_loaded() -> bool
Returns whether streaming level is loaded

Returns:
    bool:

<a id="unreal.LevelStreaming.get_world_asset_package_f_name"></a>

#### get_world_asset_package_f_name

```python
def get_world_asset_package_f_name() -> Name
```

x.get_world_asset_package_f_name() -> Name
Gets the package name for the world asset referred to by this level streaming as an FName

Returns:
    Name:

<a id="unreal.LevelStreaming.get_loaded_level"></a>

#### get_loaded_level

```python
def get_loaded_level() -> Level
```

x.get_loaded_level() -> Level
Gets a pointer to the LoadedLevel value

Returns:
    Level:

<a id="unreal.LevelStreaming.get_is_requesting_unload_and_removal"></a>

#### get_is_requesting_unload_and_removal

```python
def get_is_requesting_unload_and_removal() -> bool
```

x.get_is_requesting_unload_and_removal() -> bool
Returns if the streaming level has requested to be unloaded and removed.

Returns:
    bool:

<a id="unreal.LevelStreaming.create_instance"></a>

#### create_instance

```python
def create_instance(unique_instance_name: str) -> LevelStreaming
```

x.create_instance(unique_instance_name) -> LevelStreaming
Creates a new instance of this streaming level with a provided unique instance name

Args:
    unique_instance_name (str): 

Returns:
    LevelStreaming:

<a id="unreal.LevelStreamingAlwaysLoaded"></a>