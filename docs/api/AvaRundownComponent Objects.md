## AvaRundownComponent Objects

```python
class AvaRundownComponent(ActorComponent)
```

Add this actor component to blueprint actor to expose the API to control an
Motion Design Rundown in game.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheMedia
- **File**: AvaRundownComponent.h

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
- ``rundown`` (AvaRundown):  [Read-Write]

<a id="unreal.AvaRundownComponent.stop_page"></a>

#### stop_page

```python
def stop_page(page_id: int) -> bool
```

x.stop_page(page_id) -> bool
Stop Page

Args:
    page_id (int32): 

Returns:
    bool:

<a id="unreal.AvaRundownComponent.play_page"></a>

#### play_page

```python
def play_page(page_id: int) -> bool
```

x.play_page(page_id) -> bool
Play Page

Args:
    page_id (int32): 

Returns:
    bool:

<a id="unreal.AvaRundownComponent.get_page_id_for_index"></a>

#### get_page_id_for_index

```python
def get_page_id_for_index(page_index: int) -> int
```

x.get_page_id_for_index(page_index) -> int32
Get Page Id for Index

Args:
    page_index (int32): 

Returns:
    int32:

<a id="unreal.AvaRundownComponent.get_number_of_pages"></a>

#### get_number_of_pages

```python
def get_number_of_pages() -> int
```

x.get_number_of_pages() -> int32
Get Number Of Pages

Returns:
    int32:

<a id="unreal.AvalanchePlaylistComponent"></a>