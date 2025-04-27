## World Objects

```python
class World(Object)
```

The World is the top level object representing a map or a sandbox in which Actors and Components will exist and be rendered.

A World can be a single Persistent Level with an optional list of streaming levels that are loaded and unloaded via volumes and blueprint functions
or it can be a collection of levels organized with a World Composition.

In a standalone game, generally only a single World exists except during seamless area transitions when both a destination and current world exists.
In the editor many Worlds exist: The level being edited, each PIE instance, each editor tool which has an interactive rendered viewport, and many more.

**C++ Source:**

- **Module**: Engine
- **File**: World.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``thumbnail_info`` (ThumbnailInfo):  [Read-Only] Information for thumbnail rendering

<a id="unreal.World.get_world_settings"></a>

#### get_world_settings

```python
def get_world_settings() -> WorldSettings
```

x.get_world_settings() -> WorldSettings
Returns the AWorldSettings actor associated with this world.

Returns:
    WorldSettings: AWorldSettings actor associated with this world

<a id="unreal.World.get_data_layer_manager"></a>

#### get_data_layer_manager

```python
def get_data_layer_manager() -> DataLayerManager
```

x.get_data_layer_manager() -> DataLayerManager
Returns the UDataLayerManager associated with this world.

Returns:
    DataLayerManager: UDataLayerManager object associated with this world

<a id="unreal.NavigationSystemBase"></a>