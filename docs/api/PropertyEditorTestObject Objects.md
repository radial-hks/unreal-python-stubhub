## PropertyEditorTestObject Objects

```python
class PropertyEditorTestObject(Object)
```

Property Editor Test Object

**C++ Source:**

- **Module**: UnrealEd
- **File**: PropertyEditorTestObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_property_array`` (Array[Actor]):  [Read-Write]
- ``actor_set`` (Set[Actor]):  [Read-Write]
- ``actor_with_meta_class`` (SoftObjectPath):  [Read-Write]
- ``always_disabled`` (int32):  [Read-Write]
- ``anim_class_interface`` (AnimClassInterface):  [Read-Write]
- ``any_material_interface`` (MaterialInterface):  [Read-Write]
- ``array_of_edit_inline_new_sm_cs`` (Array[StaticMeshComponent]):  [Read-Write]
- ``array_of_structs`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``array_of_structs_with_edit_condition`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``array_of_structs_with_inline_condition`` (Array[PropertyEditorTestEditCondition]):  [Read-Write]
- ``array_with_edit_condition`` (Array[Texture2D]):  [Read-Write]
- ``asset_pointer_with_allowed_and_whitespace`` (Object):  [Read-Write]
- ``asset_reference_custom_struct_with_edit_condition`` (SoftObjectPath):  [Read-Write]
- ``asset_reference_custom_struct_with_thumbnail`` (SoftObjectPath):  [Read-Write]
- ``blendable_interface`` (BlendableInterface):  [Read-Write]
- ``bool_property`` (bool):  [Read-Write]
- ``bool_property_array`` (Array[bool]):  [Read-Write]
- ``byte_property`` (uint8):  [Read-Write]
- ``byte_property_array`` (Array[uint8]):  [Read-Write] Byte
- ``category_inline_edit_condition`` (bool):  [Read-Write]
- ``class_property`` (type(Class)):  [Read-Write]
- ``class_property_with_allowed`` (type(Class)):  [Read-Write]
- ``class_property_with_disallowed`` (type(Class)):  [Read-Write]
- ``color_property`` (Color):  [Read-Write]
- ``color_property_array`` (Array[Color]):  [Read-Write]
- ``component_reference`` (ComponentReference):  [Read-Write]
- ``date_time`` (DateTime):  [Read-Write]
- ``directory_path`` (DirectoryPath):  [Read-Write]
- ``disabled_by_can_edit_change`` (SoftObjectPath):  [Read-Write]
- ``disabled_when_flags_is_odd`` (bool):  [Read-Write]
- ``double_property`` (double):  [Read-Write]
- ``edit_color_set`` (Set[PropertyEditorTestEditColor]):  [Read-Write]
- ``edit_condition`` (bool):  [Read-Write]
- ``edit_condition_asset_reference_custom_struct_with_edit_condition`` (bool):  [Read-Write]
- ``edit_condition_flags`` (int64):  [Read-Write]
- ``edit_condition_for_arrays`` (bool):  [Read-Write]
- ``edit_condition_for_directory_path`` (bool):  [Read-Write]
- ``edit_condition_for_fixed_array`` (bool):  [Read-Write]
- ``edit_condition_struct_with_multiple_instances2`` (bool):  [Read-Write]
- ``edit_inline_new_static_mesh_component`` (StaticMeshComponent):  [Read-Write]
- ``enabled_by_previous`` (bool):  [Read-Write]
- ``enabled_when_blue`` (bool):  [Read-Write]
- ``enabled_when_category_checked`` (float):  [Read-Write]
- ``enabled_when_enum_is2`` (bool):  [Read-Write]
- ``enabled_when_enum_is4`` (bool):  [Read-Write]
- ``enabled_when_flags_has_two_or_four`` (bool):  [Read-Write]
- ``enabled_when_float_greater_than5`` (bool):  [Read-Write]
- ``enabled_when_float_less_than10`` (bool):  [Read-Write]
- ``enabled_when_int_greater_or_equal5`` (bool):  [Read-Write]
- ``enabled_when_int_less_or_equal10`` (bool):  [Read-Write]
- ``enabled_when_pink`` (bool):  [Read-Write]
- ``enables_next`` (bool):  [Read-Write]
- ``enum_as_byte_edit_condition`` (PropertyEditorTestEnum):  [Read-Write]
- ``enum_bitflags`` (int32):  [Read-Write]
- ``enum_byte_property`` (PropertyEditorTestEnum):  [Read-Write]
- ``enum_edit_condition`` (PropertyEditorTestEditColor):  [Read-Write]
- ``enum_property`` (PropertyEditorTestEditColor):  [Read-Write]
- ``enum_property_array`` (Array[PropertyEditorTestEnum]):  [Read-Write]
- ``enum_underscores`` (PropertyEditorTestUnderscores):  [Read-Write]
- ``exact_point_or_spot_light_actor_reference`` (SoftObjectPath):  [Read-Write]
- ``exactly_point_light_actor_reference`` (SoftObjectPath):  [Read-Write]
- ``fixed_array_of_ints`` (Array[int32]):  [Read-Write]
- ``fixed_array_with_edit_condition`` (str):  [Read-Write]
- ``float_edit_condition`` (float):  [Read-Write]
- ``float_property`` (float):  [Read-Write]
- ``float_property_array`` (Array[float]):  [Read-Write]
- ``float_property_with_clamped_range`` (float):  [Read-Write] This is a custom tooltip that should be shown
- ``float_range`` (FloatRange):  [Read-Only]
- ``float_set`` (Set[float]):  [Read-Write]
- ``gigabyte_property`` (double):  [Read-Write]
- ``guid`` (Guid):  [Read-Write]
- ``has_non_editable_inline_condition`` (float):  [Read-Write]
- ``inline_edit_condition_with_meta`` (float):  [Read-Write]
- ``inline_edit_condition_with_meta_toggle`` (bool):  [Read-Write]
- ``inline_edit_condition_without_meta`` (float):  [Read-Write]
- ``inline_property`` (ComponentMobility):  [Read-Write]
- ``instanced_struct_array`` (Array[PropertyEditorTestInstancedStruct]):  [Read-Write]
- ``instanced_u_object_array`` (Array[PropertyEditorTestInstancedObject]):  [Read-Write]
- ``int16_property`` (int16):  [Read-Write]
- ``int32_property`` (int32):  [Read-Write]
- ``int32_set`` (Set[int32]):  [Read-Write]
- ``int32_to_string_map`` (Map[int32, str]):  [Read-Write]
- ``int32_to_struct_map`` (Map[int32, PropertyEditorTestBasicStruct]):  [Read-Write]
- ``int64_property`` (int64):  [Read-Write]
- ``int8_property`` (int8):  [Read-Write]
- ``int_point_property`` (IntPoint):  [Read-Write]
- ``int_property32_array`` (Array[int32]):  [Read-Write] Integer
- ``int_property_with_clamped_range`` (int32):  [Read-Write]
- ``int_that_cannot_be_changed`` (int32):  [Read-Only]
- ``int_to_custom_map`` (Map[int32, PropertyEditorTestBasicStruct]):  [Read-Write]
- ``int_to_enum_map`` (Map[int32, PropertyEditorTestEnum]):  [Read-Write]
- ``int_to_sub_struct_map`` (Map[int32, PropertyEditorTestSubStruct]):  [Read-Write]
- ``integer_edit_condition`` (int32):  [Read-Write]
- ``light_actor_reference`` (SoftObjectPath):  [Read-Write]
- ``light_or_static_mesh_actor_reference`` (SoftObjectPath):  [Read-Write] NOTE: intentionally misplaced space in AllowedClasses
- ``light_propagation_volume_blendable`` (BlendableInterface):  [Read-Write] This is an IBlendableInterface that only allows for ULightPropagationVolumeBlendable objects
- ``linear_color_property`` (LinearColor):  [Read-Write]
- ``linear_color_property_array`` (Array[LinearColor]):  [Read-Write]
- ``linear_color_set`` (Set[LinearColor]):  [Read-Write]
- ``linear_color_to_string_map`` (Map[LinearColor, str]):  [Read-Write]
- ``linear_color_to_vector_map`` (Map[LinearColor, Vector]):  [Read-Write]
- ``material_no_thumbnail`` (MaterialInterface):  [Read-Write]
- ``material_or_texture_asset_reference`` (SoftObjectPath):  [Read-Write]
- ``matrix_property`` (Matrix):  [Read-Write]
- ``name_property`` (Name):  [Read-Write]
- ``name_property_array`` (Array[Name]):  [Read-Write]
- ``name_set`` (Set[Name]):  [Read-Write]
- ``name_to_color_map`` (Map[Name, LinearColor]):  [Read-Write]
- ``name_to_custom_map`` (Map[Name, PropertyEditorTestBasicStruct]):  [Read-Write]
- ``name_to_name_map`` (Map[Name, Name]):  [Read-Write]
- ``name_to_object_map`` (Map[Name, Object]):  [Read-Write]
- ``nested_array_of_ints`` (int32):  [Read-Write]
- ``not_light_actor_reference`` (SoftObjectPath):  [Read-Write]
- ``object_property`` (Object):  [Read-Write]
- ``object_property_array`` (Array[Object]):  [Read-Write]
- ``object_property_array_with_title`` (Array[PropertyEditorTestInstancedObject]):  [Read-Write]
- ``object_set`` (Set[Object]):  [Read-Write]
- ``object_that_cannot_be_changed`` (PrimitiveComponent):  [Read-Only]
- ``object_to_color_map`` (Map[Object, LinearColor]):  [Read-Write]
- ``object_to_int32_map`` (Map[Object, int32]):  [Read-Write]
- ``only_actors_allowed`` (Actor):  [Read-Write]
- ``per_platform_float`` (PerPlatformFloat):  [Read-Write]
- ``per_platform_int`` (PerPlatformInt):  [Read-Write]
- ``primary_asset_id`` (PrimaryAssetId):  [Read-Write]
- ``primary_asset_id_without_thumbnail`` (PrimaryAssetId):  [Read-Write]
- ``property_that_hides`` (ComponentMobility):  [Read-Write]
- ``rich_curve`` (RichCurve):  [Read-Write]
- ``rotator_property`` (Rotator):  [Read-Write]
- ``rotator_property_array`` (Array[Rotator]):  [Read-Write]
- ``shared_edit_condition`` (bool):  [Read-Write]
- ``simple_property_with_edit_condition`` (int32):  [Read-Write]
- ``soft_object_path`` (SoftObjectPath):  [Read-Write]
- ``static_array_of_ints`` (int32):  [Read-Write]
- ``static_array_of_ints_with_enum_labels`` (int32):  [Read-Write]
- ``static_mesh_prop`` (StaticMesh):  [Read-Write]
- ``string_password_property`` (str):  [Read-Write]
- ``string_property`` (str):  [Read-Write]
- ``string_property_array`` (Array[str]):  [Read-Write]
- ``string_set`` (Set[str]):  [Read-Write]
- ``string_that_cannot_be_changed`` (str):  [Read-Only]
- ``string_to_actor_map`` (Map[str, Actor]):  [Read-Write]
- ``string_to_color_map`` (Map[str, LinearColor]):  [Read-Write]
- ``string_to_float_map`` (Map[str, float]):  [Read-Write]
- ``string_to_multiline_text_map`` (Map[str, Text]):  [Read-Write]
- ``string_to_object_map`` (Map[str, Object]):  [Read-Write]
- ``struct`` (PropertyEditTestTextStruct):  [Read-Write]
- ``struct_property_array`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``struct_property_array_with_formatted_title`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``struct_property_array_with_formatted_title_error`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``struct_property_array_with_title`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``struct_property_array_with_title_error`` (Array[PropertyEditorTestBasicStruct]):  [Read-Write]
- ``struct_with_inline_condition`` (PropertyEditorTestEditCondition):  [Read-Write]
- ``struct_with_multiple_instances1`` (PropertyEditorTestBasicStruct):  [Read-Write]
- ``struct_with_multiple_instances2`` (PropertyEditorTestBasicStruct):  [Read-Write]
- ``subcategory`` (bool):  [Read-Write]
- ``subcategory_advanced`` (bool):  [Read-Write]
- ``subcategory_bar_advanced`` (bool):  [Read-Write]
- ``subcategory_bar_simple`` (bool):  [Read-Write]
- ``subcategory_foo_advanced`` (bool):  [Read-Write]
- ``subcategory_foo_simple`` (bool):  [Read-Write]
- ``subcategory_last`` (bool):  [Read-Write]
- ``subclass_of_texture`` (type(Class)):  [Read-Write]
- ``subclass_of_with_allowed`` (type(Class)):  [Read-Write]
- ``subclass_of_with_disallowed`` (type(Class)):  [Read-Write]
- ``text_password_property`` (Text):  [Read-Write]
- ``text_property`` (Text):  [Read-Write]
- ``text_property_array`` (Array[Text]):  [Read-Write]
- ``texture_or_blendable_interface`` (Object):  [Read-Write] Allows either an object that's derived from UTexture or IBlendableInterface, to ensure that Object Property handles know how to
  filter for AllowedClasses correctly.
- ``texture_prop`` (Texture):  [Read-Write]
- ``this_is_broken_if_its_visible_in_a_details_view`` (PropertyEditorTestBasicStruct):  [Read-Write]
- ``timecode_property_array`` (Array[Timecode]):  [Read-Write]
- ``timespan`` (Timespan):  [Read-Write]
- ``transform_property`` (Transform):  [Read-Write]
- ``unsigned_int16_property`` (uint16):  [Read-Write]
- ``unsigned_int32_property`` (uint32):  [Read-Write]
- ``unsigned_int64_property`` (uint64):  [Read-Write]
- ``uses_shared_edit_condition1`` (float):  [Read-Write]
- ``uses_shared_edit_condition2`` (float):  [Read-Write]
- ``vector2_property`` (Vector2D):  [Read-Write]
- ``vector2_property_array`` (Array[Vector2D]):  [Read-Write]
- ``vector3_property`` (Vector):  [Read-Write]
- ``vector3_property_array`` (Array[Vector]):  [Read-Write]
- ``vector4_property`` (Vector4):  [Read-Write]
- ``vector4_property_array`` (Array[Vector4]):  [Read-Write]
- ``vector_set`` (Set[Vector]):  [Read-Write]
- ``vector_to_float_map`` (Map[Vector, float]):  [Read-Write]
- ``visible_when_static`` (bool):  [Read-Write]
- ``visible_when_stationary`` (int32):  [Read-Write]

<a id="unreal.BlueprintPropertyTestObject"></a>