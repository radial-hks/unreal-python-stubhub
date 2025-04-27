## InterchangeAnimSequenceFactoryNode Objects

```python
class InterchangeAnimSequenceFactoryNode(InterchangeFactoryBaseNode)
```

Interchange Anim Sequence Factory Node

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeFactoryNodes
- **File**: InterchangeAnimSequenceFactoryNode.h

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_skeleton_soft_object_path"></a>

#### set_custom_skeleton_soft_object_path

```python
def set_custom_skeleton_soft_object_path(
        attribute_value: SoftObjectPath) -> bool
```

x.set_custom_skeleton_soft_object_path(attribute_value) -> bool
Set the optional existing USkeleton this animation must use. If this attribute is set and the skeleton is valid,
the AnimSequence factory uses this skeleton instead of the one imported from GetCustomSkeletonFactoryNodeUid.
Pipelines set this attribute when the user wants to specify an existing skeleton.

Args:
    attribute_value (SoftObjectPath): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_skeleton_factory_node_uid"></a>

#### set_custom_skeleton_factory_node_uid

```python
def set_custom_skeleton_factory_node_uid(attribute_value: str) -> bool
```

x.set_custom_skeleton_factory_node_uid(attribute_value) -> bool
Set the unique ID of the skeleton factory node. Return false if the attribute cannot be set.

Args:
    attribute_value (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_remove_curve_redundant_keys"></a>

#### set_custom_remove_curve_redundant_keys

```python
def set_custom_remove_curve_redundant_keys(attribute_value: bool) -> bool
```

x.set_custom_remove_curve_redundant_keys(attribute_value) -> bool
Set the custom attribute RemoveCurveRedundantKeys. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_material_drive_parameter_on_custom_attribute"></a>

#### set_custom_material_drive_parameter_on_custom_attribute

```python
def set_custom_material_drive_parameter_on_custom_attribute(
        attribute_value: bool) -> bool
```

x.set_custom_material_drive_parameter_on_custom_attribute(attribute_value) -> bool
Set the custom attribute MaterialDriveParameterOnCustomAttribute. Return false if the attribute could not be set.

Note: If true, sets Material Curve Type for all custom attributes.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_sample_rate"></a>

#### set_custom_import_bone_tracks_sample_rate

```python
def set_custom_import_bone_tracks_sample_rate(attribute_value: float) -> bool
```

x.set_custom_import_bone_tracks_sample_rate(attribute_value) -> bool
Set the import bone tracks sample rate. Return false if the attribute could not be set.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_range_stop"></a>

#### set_custom_import_bone_tracks_range_stop

```python
def set_custom_import_bone_tracks_range_stop(attribute_value: float) -> bool
```

x.set_custom_import_bone_tracks_range_stop(attribute_value) -> bool
Set the import bone tracks end time in seconds. Return false if the attribute could not be set.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks_range_start"></a>

#### set_custom_import_bone_tracks_range_start

```python
def set_custom_import_bone_tracks_range_start(attribute_value: float) -> bool
```

x.set_custom_import_bone_tracks_range_start(attribute_value) -> bool
Set the import bone tracks start time in seconds. Return false if the attribute could not be set.

Args:
    attribute_value (double): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_bone_tracks"></a>

#### set_custom_import_bone_tracks

```python
def set_custom_import_bone_tracks(attribute_value: bool) -> bool
```

x.set_custom_import_bone_tracks(attribute_value) -> bool
Set the import bone tracks state. Pass true to import bone tracks, or false to not import bone tracks.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_import_attribute_curves"></a>

#### set_custom_import_attribute_curves

```python
def set_custom_import_attribute_curves(attribute_value: bool) -> bool
```

x.set_custom_import_attribute_curves(attribute_value) -> bool
Set the import attribute curves state. Return false if the attribute could not be set.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_do_not_import_curve_with_zero"></a>

#### set_custom_do_not_import_curve_with_zero

```python
def set_custom_do_not_import_curve_with_zero(attribute_value: bool) -> bool
```

x.set_custom_do_not_import_curve_with_zero(attribute_value) -> bool
Set the custom attribute DoNotImportCurveWithZero. Return false if the attribute could not be set.

Note - If this attribute is enabled, only curves that have a value other than zero will be imported. This is to avoid adding extra curves to evaluate.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_non_curve_custom_attributes"></a>

#### set_custom_delete_existing_non_curve_custom_attributes

```python
def set_custom_delete_existing_non_curve_custom_attributes(
        attribute_value: bool) -> bool
```

x.set_custom_delete_existing_non_curve_custom_attributes(attribute_value) -> bool
Set the custom attribute DeleteExistingNonCurveCustomAttributes. Return false if the attribute could not be set.

Note - If true, all previous non-curve custom attributes are deleted if you reimport.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_morph_target_curves"></a>

#### set_custom_delete_existing_morph_target_curves

```python
def set_custom_delete_existing_morph_target_curves(
        attribute_value: bool) -> bool
```

x.set_custom_delete_existing_morph_target_curves(attribute_value) -> bool
Set the custom attribute DeleteExistingMorphTargetCurves. Return false if the attribute could not be set.

Note: If true, all previous morph target curves are deleted if you reimport.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_delete_existing_custom_attribute_curves"></a>

#### set_custom_delete_existing_custom_attribute_curves

```python
def set_custom_delete_existing_custom_attribute_curves(
        attribute_value: bool) -> bool
```

x.set_custom_delete_existing_custom_attribute_curves(attribute_value) -> bool
Set the custom attribute DeleteExistingCustomAttributeCurves. Return false if the attribute could not be set.

Note - If true, all previous custom attribute curves are deleted if you reimport.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_custom_add_curve_metadata_to_skeleton"></a>

#### set_custom_add_curve_metadata_to_skeleton

```python
def set_custom_add_curve_metadata_to_skeleton(attribute_value: bool) -> bool
```

x.set_custom_add_curve_metadata_to_skeleton(attribute_value) -> bool
Set the custom attribute AddCurveMetadataToSkeleton. Return false if the attribute could not be set.

Note - If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

Args:
    attribute_value (bool): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_animation_payload_keys_for_scene_node_uids"></a>

#### set_animation_payload_keys_for_scene_node_uids

```python
def set_animation_payload_keys_for_scene_node_uids(
        scene_node_animation_payload_key_uids: Map[str, str],
        scene_node_animation_payload_key_types: Map[str, int]) -> None
```

x.set_animation_payload_keys_for_scene_node_uids(scene_node_animation_payload_key_uids, scene_node_animation_payload_key_types) -> None
Set Animation Payload Keys for Scene Node Uids

Args:
    scene_node_animation_payload_key_uids (Map[str, str]): 
    scene_node_animation_payload_key_types (Map[str, uint8]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_animation_payload_keys_for_morph_target_node_uids"></a>

#### set_animation_payload_keys_for_morph_target_node_uids

```python
def set_animation_payload_keys_for_morph_target_node_uids(
        morph_target_animation_payload_key_uids: Map[str, str],
        morph_target_animation_payload_key_types: Map[str, int]) -> None
```

x.set_animation_payload_keys_for_morph_target_node_uids(morph_target_animation_payload_key_uids, morph_target_animation_payload_key_types) -> None
Set Animation Payload Keys for Morph Target Node Uids

Args:
    morph_target_animation_payload_key_uids (Map[str, str]): 
    morph_target_animation_payload_key_types (Map[str, uint8]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_animated_material_curve_suffixe"></a>

#### set_animated_material_curve_suffixe

```python
def set_animated_material_curve_suffixe(material_curve_suffixe: str) -> bool
```

x.set_animated_material_curve_suffixe(material_curve_suffixe) -> bool
Add an animated material curve suffix.

Args:
    material_curve_suffixe (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_animated_attribute_step_curve_name"></a>

#### set_animated_attribute_step_curve_name

```python
def set_animated_attribute_step_curve_name(
        attribute_step_curve_name: str) -> bool
```

x.set_animated_attribute_step_curve_name(attribute_step_curve_name) -> bool
Add an animated attribute step curve name.

Args:
    attribute_step_curve_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.set_animated_attribute_curve_name"></a>

#### set_animated_attribute_curve_name

```python
def set_animated_attribute_curve_name(attribute_curve_name: str) -> bool
```

x.set_animated_attribute_curve_name(attribute_curve_name) -> bool
Add an animated attribute curve name.

Args:
    attribute_curve_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.remove_animated_material_curve_suffixe"></a>

#### remove_animated_material_curve_suffixe

```python
def remove_animated_material_curve_suffixe(
        material_curve_suffixe: str) -> bool
```

x.remove_animated_material_curve_suffixe(material_curve_suffixe) -> bool
Remove the specified animated material curve suffix.

Args:
    material_curve_suffixe (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.remove_animated_attribute_step_curve_name"></a>

#### remove_animated_attribute_step_curve_name

```python
def remove_animated_attribute_step_curve_name(
        attribute_step_curve_name: str) -> bool
```

x.remove_animated_attribute_step_curve_name(attribute_step_curve_name) -> bool
Remove the specified animated attribute step curve name.

Args:
    attribute_step_curve_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.remove_animated_attribute_curve_name"></a>

#### remove_animated_attribute_curve_name

```python
def remove_animated_attribute_curve_name(attribute_curve_name: str) -> bool
```

x.remove_animated_attribute_curve_name(attribute_curve_name) -> bool
Remove the specified animated attribute curve name.

Args:
    attribute_curve_name (str): 

Returns:
    bool:

<a id="unreal.InterchangeAnimSequenceFactoryNode.initialize_anim_sequence_node"></a>

#### initialize_anim_sequence_node

```python
def initialize_anim_sequence_node(unique_id: str, display_label: str) -> None
```

x.initialize_anim_sequence_node(unique_id, display_label) -> None
Initialize node data.

Args:
    unique_id (str): The unique ID for this node.
    display_label (str): The name of the node.

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_scene_node_animation_payload_keys"></a>

#### get_scene_node_animation_payload_keys

```python
def get_scene_node_animation_payload_keys(
) -> Map[str, InterchangeAnimationPayLoadKey]
```

x.get_scene_node_animation_payload_keys() -> Map[str, InterchangeAnimationPayLoadKey]
Get Scene Node Animation Payload Keys

Returns:
    Map[str, InterchangeAnimationPayLoadKey]: 

    out_scene_node_animation_payload_keys (Map[str, InterchangeAnimationPayLoadKey]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_object_class"></a>

#### get_object_class

```python
def get_object_class() -> Class
```

x.get_object_class() -> type(Class)
Get the class this node creates.

Returns:
    type(Class):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_morph_target_node_animation_payload_keys"></a>

#### get_morph_target_node_animation_payload_keys

```python
def get_morph_target_node_animation_payload_keys(
) -> Map[str, InterchangeAnimationPayLoadKey]
```

x.get_morph_target_node_animation_payload_keys() -> Map[str, InterchangeAnimationPayLoadKey]
Get Morph Target Node Animation Payload Keys

Returns:
    Map[str, InterchangeAnimationPayLoadKey]: 

    out_morph_target_node_animation_payloads (Map[str, InterchangeAnimationPayLoadKey]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_skeleton_soft_object_path"></a>

#### get_custom_skeleton_soft_object_path

```python
def get_custom_skeleton_soft_object_path() -> Optional[SoftObjectPath]
```

x.get_custom_skeleton_soft_object_path() -> SoftObjectPath or None
Query the optional existing USkeleton this animation must use. If this attribute is set and the skeleton is valid,
the AnimSequence factory uses this skeleton instead of the one imported from GetCustomSkeletonFactoryNodeUid.
Pipelines set this attribute when the user wants to specify an existing skeleton.
Return false if the attribute was not set.

Returns:
    SoftObjectPath or None: 

    attribute_value (SoftObjectPath):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_skeleton_factory_node_uid"></a>

#### get_custom_skeleton_factory_node_uid

```python
def get_custom_skeleton_factory_node_uid() -> Optional[str]
```

x.get_custom_skeleton_factory_node_uid() -> str or None
Get the unique ID of the skeleton factory node. Return false if the attribute is not set.

Returns:
    str or None: 

    attribute_value (str):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_remove_curve_redundant_keys"></a>

#### get_custom_remove_curve_redundant_keys

```python
def get_custom_remove_curve_redundant_keys() -> Optional[bool]
```

x.get_custom_remove_curve_redundant_keys() -> bool or None
Get the custom attribute RemoveCurveRedundantKeys. Return false if the attribute is not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_material_drive_parameter_on_custom_attribute"></a>

#### get_custom_material_drive_parameter_on_custom_attribute

```python
def get_custom_material_drive_parameter_on_custom_attribute(
) -> Optional[bool]
```

x.get_custom_material_drive_parameter_on_custom_attribute() -> bool or None
Get the custom attribute MaterialDriveParameterOnCustomAttribute. Return false if the attribute is not set.

Note: If true, sets Material Curve Type for all custom attributes.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_sample_rate"></a>

#### get_custom_import_bone_tracks_sample_rate

```python
def get_custom_import_bone_tracks_sample_rate() -> Optional[float]
```

x.get_custom_import_bone_tracks_sample_rate() -> double or None
Get the import bone tracks sample rate. Return false if the attribute is not set.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_range_stop"></a>

#### get_custom_import_bone_tracks_range_stop

```python
def get_custom_import_bone_tracks_range_stop() -> Optional[float]
```

x.get_custom_import_bone_tracks_range_stop() -> double or None
Get the import bone tracks end time in seconds. Return false if the attribute is not set.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks_range_start"></a>

#### get_custom_import_bone_tracks_range_start

```python
def get_custom_import_bone_tracks_range_start() -> Optional[float]
```

x.get_custom_import_bone_tracks_range_start() -> double or None
Get the import bone tracks start time in seconds. Return false if the attribute is not set.

Returns:
    double or None: 

    attribute_value (double):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_bone_tracks"></a>

#### get_custom_import_bone_tracks

```python
def get_custom_import_bone_tracks() -> Optional[bool]
```

x.get_custom_import_bone_tracks() -> bool or None
Get the import bone tracks state. If the attribute is true, bone tracks are imported. If the attribute
is false, bone tracks are not imported.

Return false if the attribute is not set. Return true if the attribute exists and can be queried.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_import_attribute_curves"></a>

#### get_custom_import_attribute_curves

```python
def get_custom_import_attribute_curves() -> Optional[bool]
```

x.get_custom_import_attribute_curves() -> bool or None
Get the import attribute curves state. If true, all user custom attributes on nodes are imported.

Return false if the attribute is not set.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_do_not_import_curve_with_zero"></a>

#### get_custom_do_not_import_curve_with_zero

```python
def get_custom_do_not_import_curve_with_zero() -> Optional[bool]
```

x.get_custom_do_not_import_curve_with_zero() -> bool or None
Get the custom attribute DoNotImportCurveWithZero. Return false if the attribute is not set.

Note - If this attribute is enabled, only curves that have a value other than zero will be imported. This is to avoid adding extra curves to evaluate.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_non_curve_custom_attributes"></a>

#### get_custom_delete_existing_non_curve_custom_attributes

```python
def get_custom_delete_existing_non_curve_custom_attributes() -> Optional[bool]
```

x.get_custom_delete_existing_non_curve_custom_attributes() -> bool or None
Get the custom attribute DeleteExistingNonCurveCustomAttributes. Return false if the attribute is not set.

Note - If true, all previous non-curve custom attributes are deleted if you reimport.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_morph_target_curves"></a>

#### get_custom_delete_existing_morph_target_curves

```python
def get_custom_delete_existing_morph_target_curves() -> Optional[bool]
```

x.get_custom_delete_existing_morph_target_curves() -> bool or None
Get the custom attribute DeleteExistingMorphTargetCurves. Return false if the attribute is not set.

Note: If true, all previous morph target curves are deleted if you reimport.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_delete_existing_custom_attribute_curves"></a>

#### get_custom_delete_existing_custom_attribute_curves

```python
def get_custom_delete_existing_custom_attribute_curves() -> Optional[bool]
```

x.get_custom_delete_existing_custom_attribute_curves() -> bool or None
Get the custom attribute DeleteExistingCustomAttributeCurves. Return false if the attribute is not set.

Note - If true, all previous custom attribute curves are deleted if you reimport.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_custom_add_curve_metadata_to_skeleton"></a>

#### get_custom_add_curve_metadata_to_skeleton

```python
def get_custom_add_curve_metadata_to_skeleton() -> Optional[bool]
```

x.get_custom_add_curve_metadata_to_skeleton() -> bool or None
Get the custom attribute AddCurveMetadataToSkeleton. Return false if the attribute is not set.

Note - If this setting is disabled, curve metadata will be added to skeletal meshes for morph targets, but no metadata entry will be created for general curves.

Returns:
    bool or None: 

    attribute_value (bool):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixes_count"></a>

#### get_animated_material_curve_suffixes_count

```python
def get_animated_material_curve_suffixes_count() -> int
```

x.get_animated_material_curve_suffixes_count() -> int32
Return the number of animated material curve suffixes this anim sequence drives. Curves are FRichCurve of type float.

Returns:
    int32:

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixes"></a>

#### get_animated_material_curve_suffixes

```python
def get_animated_material_curve_suffixes() -> Array[str]
```

x.get_animated_material_curve_suffixes() -> Array[str]
Get all animated material curve suffixes.

Returns:
    Array[str]: 

    out_material_curve_suffixes (Array[str]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_material_curve_suffixe"></a>

#### get_animated_material_curve_suffixe

```python
def get_animated_material_curve_suffixe(index: int) -> str
```

x.get_animated_material_curve_suffixe(index) -> str
Get the animated material curve suffix with the specified index.

Args:
    index (int32): 

Returns:
    str: 

    out_material_curve_suffixe (str):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_names_count"></a>

#### get_animated_attribute_step_curve_names_count

```python
def get_animated_attribute_step_curve_names_count() -> int
```

x.get_animated_attribute_step_curve_names_count() -> int32
Return the number of animated attribute step curve names this anim sequence drives.

Returns:
    int32:

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_names"></a>

#### get_animated_attribute_step_curve_names

```python
def get_animated_attribute_step_curve_names() -> Array[str]
```

x.get_animated_attribute_step_curve_names() -> Array[str]
Get all animated attribute step curve names.

Returns:
    Array[str]: 

    out_attribute_step_curve_names (Array[str]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_step_curve_name"></a>

#### get_animated_attribute_step_curve_name

```python
def get_animated_attribute_step_curve_name(index: int) -> str
```

x.get_animated_attribute_step_curve_name(index) -> str
Get the animated attribute step curve name at the specified index.

Args:
    index (int32): 

Returns:
    str: 

    out_attribute_step_curve_name (str):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_names_count"></a>

#### get_animated_attribute_curve_names_count

```python
def get_animated_attribute_curve_names_count() -> int
```

x.get_animated_attribute_curve_names_count() -> int32
Return the number of animated attribute curve names this anim sequence drives. Curves are FRichCurve of type float.

Returns:
    int32:

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_names"></a>

#### get_animated_attribute_curve_names

```python
def get_animated_attribute_curve_names() -> Array[str]
```

x.get_animated_attribute_curve_names() -> Array[str]
Get all animated attribute curve names.

Returns:
    Array[str]: 

    out_attribute_curve_names (Array[str]):

<a id="unreal.InterchangeAnimSequenceFactoryNode.get_animated_attribute_curve_name"></a>

#### get_animated_attribute_curve_name

```python
def get_animated_attribute_curve_name(index: int) -> str
```

x.get_animated_attribute_curve_name(index) -> str
Get the animated attribute curve name at the specified index.

Args:
    index (int32): 

Returns:
    str: 

    out_attribute_curve_name (str):

<a id="unreal.InterchangeCommonPipelineDataFactoryNode"></a>