## MassMovableVisualizationTrait Objects

```python
class MassMovableVisualizationTrait(MassVisualizationTrait)
```

Mass Movable Visualization Trait

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassRepresentation
- **File**: MassMovableVisualizationTrait.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``allow_server_side_visualization`` (bool):  [Read-Write] If set to true will result in the visualization-related fragments being added to server-size entities as well.
  By default only the clients require visualization fragments
- ``can_modify_representation_subsystem_class`` (bool):  [Read-Write] the property is marked like this to ensure it won't show up in UI
- ``high_res_template_actor`` (type(Class)):  [Read-Write] Actor class of this agent when spawned in high resolution
- ``lod_params`` (MassVisualizationLODParameters):  [Read-Write] Configuration parameters for the visualization LOD processor
- ``low_res_template_actor`` (type(Class)):  [Read-Write] Actor class of this agent when spawned in low resolution
- ``params`` (MassRepresentationParameters):  [Read-Write] Configuration parameters for the representation processor
- ``representation_subsystem_class`` (type(Class)):  [Read-Write] Allow subclasses to override the representation subsystem to use
- ``static_mesh_instance_desc`` (StaticMeshInstanceVisualizationDesc):  [Read-Write] Instanced static mesh information for this agent

<a id="unreal.MassStationaryDistanceVisualizationTrait"></a>