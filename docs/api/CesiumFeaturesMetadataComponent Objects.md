## CesiumFeaturesMetadataComponent Objects

```python
class CesiumFeaturesMetadataComponent(ActorComponent)
```

brief: A component that can be added to Cesium3DTileset actors to dictate what metadata to encode for access on the GPU. The selection can be automatically populated based on available metadata by clicking the "Auto Fill" button. Once a selection of desired metadata is made, the boiler-plate material code to access the selected properties can be auto-generated using the "Generate Material" button.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumFeaturesMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``feature_id_sets`` (Array[CesiumFeatureIdSetDescription]):  [Read-Write] Description of the feature ID sets in the visible glTF primitives across
  the tileset.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``property_tables`` (Array[CesiumPropertyTableDescription]):  [Read-Write] Descriptions of the property tables in the visible glTF
  models across the tileset.
- ``property_texture_names`` (Set[str]):  [Read-Write] Names of the property textures used by the glTF primitives across the
  tileset.

  This should be a subset of the property textures listed in the model
  metadata. Property textures can be passed to the material even if they are
  not explicitly used by a glTF primitive, but the primitive may lack the
  corresponding sets of texture coordinates intended to sample them.
- ``property_textures`` (Array[CesiumPropertyTextureDescription]):  [Read-Write] Descriptions of property textures in the visible glTF models across
  the tileset.
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``target_material_layer`` (MaterialFunctionMaterialLayer):  [Read-Write] This is the target UMaterialFunctionMaterialLayer that the
  boiler-plate material generation will use. When pressing
  "Generate Material", nodes will be added to this material to enable access
  to the requested metadata. If this is left blank, a new material layer
  will be created in the /Game/ folder.

<a id="unreal.CesiumGlobeAnchoredActorComponent"></a>