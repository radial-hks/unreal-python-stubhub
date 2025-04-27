## LODSyncComponent Objects

```python
class LODSyncComponent(ActorComponent)
```

Implement an Actor component for LOD Sync of different components

This is a component that allows multiple different components to sync together of their LOD

This allows to find the highest LOD of all the parts, and sync to that LOD

**C++ Source:**

- **Module**: Engine
- **File**: LODSyncComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``components_to_sync`` (Array[ComponentSync]):  [Read-Write] Array of components whose LOD may drive or be driven by this component.
  Components that are flagged as 'Drive' are treated as being in priority order, with the last component having highest priority. The highest priority
  visible component will set the LOD for all other components. If no components are visible, then the highest priority non-visible component will set LOD.
- ``custom_lod_mapping`` (Map[Name, LODMappingData]):  [Read-Write] by default, the mapping will be one to one
  but if you want custom, add here.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``forced_lod`` (int32):  [Read-Write] if -1, it's automatically switching
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``min_lod`` (int32):  [Read-Write] Minimum LOD to use when syncing components
- ``num_lo_ds`` (int32):  [Read-Write] if -1, it's default and it will calculate the max number of LODs from all sub components
  if not, it is a number of LODs (not the max index of LODs)
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!

<a id="unreal.LODSyncComponent.num_lo_ds"></a>

#### num_lo_ds

```python
@property
def num_lo_ds() -> int
```

(int32):  [Read-Write] if -1, it's default and it will calculate the max number of LODs from all sub components
if not, it is a number of LODs (not the max index of LODs)

<a id="unreal.LODSyncComponent.num_lo_ds"></a>

#### num_lo_ds

```python
@num_lo_ds.setter
def num_lo_ds(value: int) -> None
```

<a id="unreal.LODSyncComponent.forced_lod"></a>

#### forced_lod

```python
@property
def forced_lod() -> int
```

(int32):  [Read-Write] if -1, it's automatically switching

<a id="unreal.LODSyncComponent.forced_lod"></a>

#### forced_lod

```python
@forced_lod.setter
def forced_lod(value: int) -> None
```

<a id="unreal.LODSyncComponent.min_lod"></a>

#### min_lod

```python
@property
def min_lod() -> int
```

(int32):  [Read-Write] Minimum LOD to use when syncing components

<a id="unreal.LODSyncComponent.min_lod"></a>

#### min_lod

```python
@min_lod.setter
def min_lod(value: int) -> None
```

<a id="unreal.LODSyncComponent.components_to_sync"></a>

#### components_to_sync

```python
@property
def components_to_sync() -> Array[ComponentSync]
```

(Array[ComponentSync]):  [Read-Write] Array of components whose LOD may drive or be driven by this component.
Components that are flagged as 'Drive' are treated as being in priority order, with the last component having highest priority. The highest priority
visible component will set the LOD for all other components. If no components are visible, then the highest priority non-visible component will set LOD.

<a id="unreal.LODSyncComponent.components_to_sync"></a>

#### components_to_sync

```python
@components_to_sync.setter
def components_to_sync(value: Array[ComponentSync]) -> None
```

<a id="unreal.LODSyncComponent.custom_lod_mapping"></a>

#### custom_lod_mapping

```python
@property
def custom_lod_mapping() -> Map[Name, LODMappingData]
```

(Map[Name, LODMappingData]):  [Read-Write] by default, the mapping will be one to one
but if you want custom, add here.

<a id="unreal.LODSyncComponent.custom_lod_mapping"></a>

#### custom_lod_mapping

```python
@custom_lod_mapping.setter
def custom_lod_mapping(value: Map[Name, LODMappingData]) -> None
```

<a id="unreal.LODSyncComponent.get_lod_sync_debug_text"></a>

#### get_lod_sync_debug_text

```python
def get_lod_sync_debug_text() -> str
```

x.get_lod_sync_debug_text() -> str
Returns a string detailing

Returns:
    str:

<a id="unreal.MaterialBillboardComponent"></a>