## CompositeSection Objects

```python
class CompositeSection(AnimLinkableElement)
```

Section data for each track. Reference of data will be stored in the child class for the way they want
AnimComposite vs AnimMontage have different requirement for the actual data reference
This only contains composite section information. (vertical sequences)

**C++ Source:**

- **Module**: Engine
- **File**: AnimMontage.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``link_method`` (AnimLinkMethod):  [Read-Write] The method we are using to calculate our times
- ``linked_sequence`` (AnimSequenceBase):  [Read-Only] The Animation Sequence that this montage element will link to, when the sequence changes
  in either length or rate; the element will correctly place itself in relation to the sequence
- ``meta_data`` (Array[AnimMetaData]):  [Read-Write] Meta data that can be saved with the asset

  You can query by GetMetaData function
- ``next_section_name`` (Name):  [Read-Only] Should this animation loop.
- ``section_name`` (Name):  [Read-Write] Section Name
- ``slot_index`` (int32):  [Read-Write] The slot index we are currently using within LinkedMontage

<a id="unreal.CompositeSection.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.EditorParameterGroup"></a>