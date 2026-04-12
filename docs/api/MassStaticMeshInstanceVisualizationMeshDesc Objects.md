## MassStaticMeshInstanceVisualizationMeshDesc Objects

```python
class MassStaticMeshInstanceVisualizationMeshDesc(StructBase)
```

Mass Static Mesh Instance Visualization Mesh Desc

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassRepresentationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cast_shadows`` (bool):  [Read-Write] Controls whether the ISM can cast shadow or not
- ``ism_component_class`` (type(Class)):  [Read-Write] InstancedStaticMeshComponent class to use to manage instances described by this struct instance
- ``material_overrides`` (Array[MaterialInterface]):  [Read-Write] Material overrides for the static mesh visual representation.

  Array indices correspond to material slot indices on the static mesh.
- ``max_lod_significance`` (float):  [Read-Write] The maximum exclusive LOD significance to stop using this static mesh
- ``mesh`` (StaticMesh):  [Read-Write] The static mesh visual representation
- ``min_lod_significance`` (float):  [Read-Write] The minimum inclusive LOD significance to start using this static mesh

<a id="unreal.MassStaticMeshInstanceVisualizationMeshDesc.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.StaticMeshInstanceVisualizationMeshDesc"></a>