## InterchangePipelineMeshesUtilitiesContext Objects

```python
class InterchangePipelineMeshesUtilitiesContext(StructBase)
```

* Represents the context UInterchangePipelineMeshesUtilities will use when the client queries data.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangePipelineMeshesUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``convert_skeletal_mesh_to_static_mesh`` (bool):  [Read-Write] If enabled, all skeletal meshes are converted to static meshes.
- ``convert_static_mesh_to_skeletal_mesh`` (bool):  [Read-Write] If enabled, all static meshes are converted to skeletal meshes.
- ``convert_statics_with_morph_targets_to_skeletals`` (bool):  [Read-Write] If enabled, all static meshes that have morph targets will be imported as skeletal meshes instead.
- ``ignore_static_meshes`` (bool):  [Read-Write] If enabled, all static meshes will be ignored. The mesh utility will not return any static meshes.
- ``import_meshes_in_bone_hierarchy`` (bool):  [Read-Write] If enabled, meshes nested in bone hierarchies are imported as meshes instead of being converted to bones. If the meshes are not skinned, they are
  added to the skeletal mesh and removed from the list of static meshes.
- ``query_geometry_only_if_no_instance`` (bool):  [Read-Write] When querying geometry, this flag will not add MeshGeometry if there is a scene node that points to a geometry.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.__init__"></a>

#### __init__

```python
def __init__(convert_static_mesh_to_skeletal_mesh: bool = False,
             convert_skeletal_mesh_to_static_mesh: bool = False,
             convert_statics_with_morph_targets_to_skeletals: bool = False,
             import_meshes_in_bone_hierarchy: bool = False,
             query_geometry_only_if_no_instance: bool = False,
             ignore_static_meshes: bool = False) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_static_mesh_to_skeletal_mesh"></a>

#### convert_static_mesh_to_skeletal_mesh

```python
@property
def convert_static_mesh_to_skeletal_mesh() -> bool
```

(bool):  [Read-Write] If enabled, all static meshes are converted to skeletal meshes.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_static_mesh_to_skeletal_mesh"></a>

#### convert_static_mesh_to_skeletal_mesh

```python
@convert_static_mesh_to_skeletal_mesh.setter
def convert_static_mesh_to_skeletal_mesh(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_skeletal_mesh_to_static_mesh"></a>

#### convert_skeletal_mesh_to_static_mesh

```python
@property
def convert_skeletal_mesh_to_static_mesh() -> bool
```

(bool):  [Read-Write] If enabled, all skeletal meshes are converted to static meshes.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_skeletal_mesh_to_static_mesh"></a>

#### convert_skeletal_mesh_to_static_mesh

```python
@convert_skeletal_mesh_to_static_mesh.setter
def convert_skeletal_mesh_to_static_mesh(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_statics_with_morph_targets_to_skeletals"></a>

#### convert_statics_with_morph_targets_to_skeletals

```python
@property
def convert_statics_with_morph_targets_to_skeletals() -> bool
```

(bool):  [Read-Write] If enabled, all static meshes that have morph targets will be imported as skeletal meshes instead.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.convert_statics_with_morph_targets_to_skeletals"></a>

#### convert_statics_with_morph_targets_to_skeletals

```python
@convert_statics_with_morph_targets_to_skeletals.setter
def convert_statics_with_morph_targets_to_skeletals(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.import_meshes_in_bone_hierarchy"></a>

#### import_meshes_in_bone_hierarchy

```python
@property
def import_meshes_in_bone_hierarchy() -> bool
```

(bool):  [Read-Write] If enabled, meshes nested in bone hierarchies are imported as meshes instead of being converted to bones. If the meshes are not skinned, they are
added to the skeletal mesh and removed from the list of static meshes.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.import_meshes_in_bone_hierarchy"></a>

#### import_meshes_in_bone_hierarchy

```python
@import_meshes_in_bone_hierarchy.setter
def import_meshes_in_bone_hierarchy(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.query_geometry_only_if_no_instance"></a>

#### query_geometry_only_if_no_instance

```python
@property
def query_geometry_only_if_no_instance() -> bool
```

(bool):  [Read-Write] When querying geometry, this flag will not add MeshGeometry if there is a scene node that points to a geometry.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.query_geometry_only_if_no_instance"></a>

#### query_geometry_only_if_no_instance

```python
@query_geometry_only_if_no_instance.setter
def query_geometry_only_if_no_instance(value: bool) -> None
```

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.ignore_static_meshes"></a>

#### ignore_static_meshes

```python
@property
def ignore_static_meshes() -> bool
```

(bool):  [Read-Write] If enabled, all static meshes will be ignored. The mesh utility will not return any static meshes.

<a id="unreal.InterchangePipelineMeshesUtilitiesContext.ignore_static_meshes"></a>

#### ignore_static_meshes

```python
@ignore_static_meshes.setter
def ignore_static_meshes(value: bool) -> None
```

<a id="unreal.IntMargin"></a>