## FbxSceneImportOptions Objects

```python
class FbxSceneImportOptions(Object)
```

Fbx_AddToBlueprint UMETA(DisplayName = "Add to an existing Blueprint asset"),

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxSceneImportOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bake_pivot_in_vertex`` (bool):  [Read-Write] - Experimental - If this option is true the inverse node pivot will be apply to the mesh vertices. The pivot from the DCC will then be the origin of the mesh. This option only work with static meshes.
- ``create_content_folder_hierarchy`` (bool):  [Read-Write] If checked, a folder's hierarchy will be created under the import asset path. All the created folders will match the actor hierarchy. In case there is more than one actor that links to an asset, the shared asset will be placed at the first actor's place.
- ``force_front_x_axis`` (bool):  [Read-Write] Whether to force the front axis to be align with X instead of -Y.
- ``hierarchy_type`` (FBXSceneOptionsCreateHierarchyType):  [Read-Write] Choose if you want to generate the scene hierarchy with normal level actors, one actor with multiple components, or one blueprint asset with multiple components.
- ``import_as_dynamic`` (bool):  [Read-Write] If checked, the mobility of all actors or components will be dynamic. If unchecked, they will be static.
- ``import_skeletal_mesh_lo_ds`` (bool):  [Read-Write] If enabled, creates LOD models for Unreal skeletal meshes from LODs in the import file; If not enabled, only the base skeletal mesh from the LOD group is imported.
- ``import_static_mesh_lo_ds`` (bool):  [Read-Write] If enabled, creates LOD models for Unreal static meshes from LODs in the import file; If not enabled, only the base static mesh from the LOD group is imported.
- ``invert_normal_maps`` (bool):  [Read-Write] If enabled, this option will cause normal map Y (Green) values to be inverted when importing textures

<a id="unreal.FbxSceneImportOptionsSkeletalMesh"></a>