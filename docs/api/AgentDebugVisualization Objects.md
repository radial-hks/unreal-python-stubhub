## AgentDebugVisualization Objects

```python
class AgentDebugVisualization(TableRowBase)
```

Agent Debug Visualization

**C++ Source:**

- **Plugin**: MassGameplay
- **Module**: MassGameplayDebug
- **File**: MassGameplayDebugTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_override`` (MaterialInterface):  [Read-Write]
- ``mesh`` (StaticMesh):  [Read-Write]
- ``visual_far_cull_distance`` (uint32):  [Read-Write] Far cull distance to override default value for that agent type
- ``visual_near_cull_distance`` (uint32):  [Read-Write] Near cull distance to override default value for that agent type
- ``wire_shape`` (MassEntityDebugShape):  [Read-Write] If Mesh is not set this WireShape will be used for debug drawing via GameplayDebugger

<a id="unreal.AgentDebugVisualization.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.PCGLoadAlembicBPData"></a>