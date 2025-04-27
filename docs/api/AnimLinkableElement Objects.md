## AnimLinkableElement Objects

```python
class AnimLinkableElement(StructBase)
```

Used to describe an element that can be linked to a segment in a montage or sequence.
   Usage:
           Inherit from FAnimLinkableElement and make sure to call LinkMontage or LinkSequence
           both on creation and on loading the element. From there SetTime and GetTime should be
           used to control where this element is in the montage or sequence.

           For more advanced usage, see this implementation used in FAnimNotifyEvent where
           we have a secondary link to handle a duration
see: FAnimNotifyEvent

**C++ Source:**

- **Module**: Engine
- **File**: AnimLinkableElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``link_method`` (AnimLinkMethod):  [Read-Write] The method we are using to calculate our times
- ``linked_sequence`` (AnimSequenceBase):  [Read-Only] The Animation Sequence that this montage element will link to, when the sequence changes
  in either length or rate; the element will correctly place itself in relation to the sequence
- ``slot_index`` (int32):  [Read-Write] The slot index we are currently using within LinkedMontage

<a id="unreal.AnimLinkableElement.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.AnimNotifyEvent"></a>