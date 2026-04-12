## StateTreeReferenceOverrideItem Objects

```python
class StateTreeReferenceOverrideItem(StructBase)
```

Item describing a state tree override for a state with a specific tag.

**C++ Source:**

- **Plugin**: StateTree
- **Module**: StateTreeModule
- **File**: StateTreeReference.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``state_tag`` (GameplayTag):  [Read-Write] Exact tag used to match against a tag on a linked State Tree state.
- ``state_tree_reference`` (StateTreeReference):  [Read-Write] State Tree and parameters to replace the linked state asset with.

<a id="unreal.StateTreeReferenceOverrideItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.MetasoundFrontendDocumentMetadata"></a>