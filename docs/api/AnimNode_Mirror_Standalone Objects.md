## AnimNode_Mirror_Standalone Objects

```python
class AnimNode_Mirror_Standalone(AnimNode_MirrorBase)
```

Anim Node Mirror Standalone

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_Mirror.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_mirroring`` (bool):  [Read-Write]
- ``blend_time`` (float):  [Read-Write] Inertialization blend time to use when transitioning between mirrored and unmirrored states
- ``bone_mirroring`` (bool):  [Read-Write]
- ``curve_mirroring`` (bool):  [Read-Write]
- ``mirror`` (bool):  [Read-Write]
- ``mirror_data_table`` (MirrorDataTable):  [Read-Write]
- ``reset_child`` (bool):  [Read-Write] Whether to reset (reinitialize) the child (source) pose when the mirror state changes
- ``source`` (PoseLink):  [Read-Write]

<a id="unreal.AnimNode_Mirror_Standalone.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_ModifyCurve"></a>