## GeometryMaskWriteMeshComponent Objects

```python
class GeometryMaskWriteMeshComponent(GeometryMaskCanvasReferenceComponentBase)
```

Geometry Mask Write Mesh Component

**C++ Source:**

- **Plugin**: GeometryMask
- **Module**: GeometryMask
- **File**: GeometryMaskWriteComponent.h

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
- ``parameters`` (GeometryMaskWriteParameters):  [Read-Write]
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``write_when_hidden`` (bool):  [Read-Write] Write to the mask even when this or it's owner is hidden.

<a id="unreal.GeometryMaskWriteMeshComponent.parameters"></a>

#### parameters

```python
@property
def parameters() -> GeometryMaskWriteParameters
```

(GeometryMaskWriteParameters):  [Read-Write]

<a id="unreal.GeometryMaskWriteMeshComponent.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: GeometryMaskWriteParameters) -> None
```

<a id="unreal.GeometryMaskWriteMeshComponent.write_when_hidden"></a>

#### write_when_hidden

```python
@property
def write_when_hidden() -> bool
```

(bool):  [Read-Write] Write to the mask even when this or it's owner is hidden.

<a id="unreal.GeometryMaskWriteMeshComponent.write_when_hidden"></a>

#### write_when_hidden

```python
@write_when_hidden.setter
def write_when_hidden(value: bool) -> None
```

<a id="unreal.NiagaraDataChannelReader"></a>