## MovieSceneObjectBindingID Objects

```python
class MovieSceneObjectBindingID(StructBase)
```

Persistent identifier to a specific object binding within a sequence hierarchy.

Binding IDs come in 3 flavors with Local and External being preferred as they are reslilient towards sequences being authored in isolation or included in other root sequences:
    Local: (ResolveParentIndex == 0) SequenceID relates to _this sequence's_ local hierarchy; represents an object binding within the same sequence as the ID is resolved, or inside one of its sub-sequences. Sequence ID must be remapped at runtime.
    External: (ResolveParentIndex > 0) SequenceID is local to the parent sequence of this one denoted by the parent index (ie, 1 = parent, 2 = grandparent etc). Sequence ID must be remapped at runtime.
    Fixed: Represents a binding anywhere in the sequence; always resolved from the root sequence.

Fixed bindings will break if the sequence is evaluated inside a different root sequence.

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneObjectBindingID.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``guid`` (Guid):  [Read-Write] Identifier for the object binding within the sequence

<a id="unreal.MovieSceneObjectBindingID.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.MovieSceneObjectBindingPtr"></a>