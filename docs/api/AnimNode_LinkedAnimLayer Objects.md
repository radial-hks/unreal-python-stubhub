## AnimNode_LinkedAnimLayer Objects

```python
class AnimNode_LinkedAnimLayer(AnimNode_LinkedAnimGraph)
```

Anim Node Linked Anim Layer

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_LinkedAnimLayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``instance_class`` (type(Class)):  [Read-Write] The class spawned for this linked instance
- ``layer`` (Name):  [Read-Write] The layer in the interface to use
- ``propagate_notifies_to_linked_instances`` (bool):  [Read-Write] Whether named notifies will be propagated from this linked instance to other instances (outer or other linked instances)
- ``receive_notifies_from_linked_instances`` (bool):  [Read-Write] Whether named notifies will be received by this linked instance from other instances (outer or other linked instances)

<a id="unreal.AnimNode_LinkedAnimLayer.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNode_Layer"></a>