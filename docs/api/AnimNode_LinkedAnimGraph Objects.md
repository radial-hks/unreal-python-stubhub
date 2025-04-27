## AnimNode_LinkedAnimGraph Objects

```python
class AnimNode_LinkedAnimGraph(AnimNode_CustomProperty)
```

Anim Node Linked Anim Graph

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_LinkedAnimGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instance_class`` (type(Class)):  [Read-Write] The class spawned for this linked instance
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether named notifies will be propagated from this linked instance to other instances (outer or other linked instances)
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether named notifies will be received by this linked instance from other instances (outer or other linked instances)

<a id="unreal.AnimNode_LinkedAnimGraph.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_SubInstance"></a>