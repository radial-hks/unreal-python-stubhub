## InterchangeLodSceneNodeContainer Objects

```python
class InterchangeLodSceneNodeContainer(StructBase)
```

* This container exists only because UPROPERTY cannot support nested container. See FInterchangeMeshInstance.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangePipelines
- **File**: InterchangePipelineMeshesUtilities.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``scene_nodes`` (Array[InterchangeSceneNode]):  [Read-Write] Each scene node here represents a mesh scene node. If it represents a LOD group, there may be more then one mesh scene node for a specific LOD index.

<a id="unreal.InterchangeLodSceneNodeContainer.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.InterchangeMeshInstance"></a>