## CesiumEncodedMetadataComponent Objects

```python
class CesiumEncodedMetadataComponent(ActorComponent)
```

brief: An actor component that can be added to Cesium3DTileset actors to dictate what metadata to encode for access on the GPU. The selection can be automatically populated based on available metadata by clicking the "Auto Fill" button. Once a selection of desired metadata is made, the boiler-plate material code to access the selected properties can be auto-generated using the "Generate Material" button.

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumEncodedMetadataComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``asset_user_data`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``asset_user_data_editor_only`` (Array[AssetUserData]):  [Read-Write] Array of user data stored with the component
- ``auto_activate`` (bool):  [Read-Write] Whether the component is activated at creation or must be explicitly activated.
- ``can_ever_affect_navigation`` (bool):  [Read-Write] Whether this component can potentially influence navigation
- ``component_tags`` (Array[Name]):  [Read-Write] Array of tags that can be used for grouping and categorizing. Can also be accessed from scripting.
- ``editable_when_inherited`` (bool):  [Read-Write] True if this component can be modified when it was inherited from a parent actor class
- ``feature_tables`` (Array[FeatureTableDescription]):  [Read-Write]
  deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
  brief: Descriptions of feature tables to upload to the GPU.
- ``feature_textures`` (Array[FeatureTextureDescription]):  [Read-Write]
  deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
  brief: Descriptions of feature textures to upload to the GPU.
- ``is_editor_only`` (bool):  [Read-Write] If true, the component will be excluded from non-editor builds
- ``on_component_activated`` (ActorComponentActivatedSignature):  [Read-Write] Called when the component has been activated, with parameter indicating if it was from a reset
- ``on_component_deactivated`` (ActorComponentDeactivateSignature):  [Read-Write] Called when the component has been deactivated
- ``primary_component_tick`` (ActorComponentTickFunction):  [Read-Write] Main tick function for the Component
- ``replicate_using_registered_sub_object_list`` (bool):  [Read-Write] When true the replication system will only replicate the registered subobjects list
  When false the replication system will instead call the virtual ReplicateSubObjects() function where the subobjects need to be manually replicated.
- ``replicates`` (bool):  [Read-Write] Is this component currently replicating? Should the network code consider it for replication? Owning Actor must be replicating first!
- ``target_material_layer`` (MaterialFunctionMaterialLayer):  [Read-Write]
  deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
  brief: This is the target UMaterialFunctionMaterialLayer that the boiler-plate material generation will use. When pressing "Generate Material", nodes will be added to this material to enable access to the requested metadata. If this is left blank, a new material layer will be created in the /Game/ folder.

<a id="unreal.CesiumEncodedMetadataComponent.target_material_layer"></a>

#### target\_material\_layer

```python
@property
def target_material_layer() -> MaterialFunctionMaterialLayer
```

(MaterialFunctionMaterialLayer):  [Read-Write]
deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
brief: This is the target UMaterialFunctionMaterialLayer that the boiler-plate material generation will use. When pressing "Generate Material", nodes will be added to this material to enable access to the requested metadata. If this is left blank, a new material layer will be created in the /Game/ folder.

<a id="unreal.CesiumEncodedMetadataComponent.target_material_layer"></a>

#### target\_material\_layer

```python
@target_material_layer.setter
def target_material_layer(value: MaterialFunctionMaterialLayer) -> None
```

<a id="unreal.CesiumEncodedMetadataComponent.feature_tables"></a>

#### feature\_tables

```python
@property
def feature_tables() -> Array[FeatureTableDescription]
```

(Array[FeatureTableDescription]):  [Read-Write]
deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
brief: Descriptions of feature tables to upload to the GPU.

<a id="unreal.CesiumEncodedMetadataComponent.feature_tables"></a>

#### feature\_tables

```python
@feature_tables.setter
def feature_tables(value: Array[FeatureTableDescription]) -> None
```

<a id="unreal.CesiumEncodedMetadataComponent.feature_textures"></a>

#### feature\_textures

```python
@property
def feature_textures() -> Array[FeatureTextureDescription]
```

(Array[FeatureTextureDescription]):  [Read-Write]
deprecated: CesiumEncodedMetadataComponent is deprecated. Use CesiumFeaturesMetadataComponent instead.
brief: Descriptions of feature textures to upload to the GPU.

<a id="unreal.CesiumEncodedMetadataComponent.feature_textures"></a>

#### feature\_textures

```python
@feature_textures.setter
def feature_textures(value: Array[FeatureTextureDescription]) -> None
```

<a id="unreal.CesiumFeatureIdAttributeBlueprintLibrary"></a>