## CesiumTileExcluder Objects

```python
class CesiumTileExcluder(ActorComponent)
```

An actor component for excluding Cesium Tiles.
This class provides an interface for excluding Cesium Tiles from a tileset.
You can create a blueprint that derives from this class and override the
`ShouldExclude` function to implement custom logic for determining whether a
tile should be excluded. This function can be implemented in either C++ or
Blueprints.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumTileExcluder.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.CesiumTileExcluder.should_exclude"></a>

#### should\_exclude

```python
def should_exclude(tile_object: CesiumTile) -> bool
```

x.should_exclude(tile_object) -> bool
Determines whether a tile should be excluded.
This function is called to determine whether a tile should be excluded from
the tileset. You can override this function in a derived class or blueprint
to implement custom exclusion logic.

Args:
    tile_object (CesiumTile): 

Returns:
    bool:

<a id="unreal.CesiumTileExcluder.remove_from_tileset"></a>

#### remove\_from\_tileset

```python
def remove_from_tileset() -> None
```

x.remove_from_tileset() -> None
Removes this tile excluder from its owning Cesium 3D Tileset Actor. If the
excluder is not yet added or if this component's Owner is not a Cesium 3D
Tileset, this method does nothing.

<a id="unreal.CesiumTileExcluder.refresh"></a>

#### refresh

```python
def refresh() -> None
```

x.refresh() -> None
Refreshes this tile excluderby removing from its owning Cesium 3D Tileset
Actor and re-adding it. If this component's Owner is not a Cesium 3D
Tileset Actor, this method does nothing.

<a id="unreal.CesiumTileExcluder.add_to_tileset"></a>

#### add\_to\_tileset

```python
def add_to_tileset() -> None
```

x.add_to_tileset() -> None
Adds this tile excluder to its owning Cesium 3D Tileset Actor. If the
excluder is already added or if this component's Owner is not a Cesium 3D
Tileset, this method does nothing.

<a id="unreal.CesiumTileMapServiceRasterOverlay"></a>