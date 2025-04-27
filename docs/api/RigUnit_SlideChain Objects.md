## RigUnit_SlideChain Objects

```python
class RigUnit_SlideChain(RigUnit_HighlevelBaseMutable)
```

Slides an existing chain along itself with control over extrapolation.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SlideChain.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``end_bone`` (Name):  [Read-Write] The name of the last bone to slide
- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``slide_amount`` (float):  [Read-Write] The amount of sliding. This unit is multiple of the chain length.
- ``start_bone`` (Name):  [Read-Write] The name of the first bone to slide

<a id="unreal.RigUnit_SlideChain.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             start_bone: Name = "None",
             end_bone: Name = "None",
             slide_amount: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SlideChain.start_bone"></a>

#### start_bone

```python
@property
def start_bone() -> Name
```

(Name):  [Read-Write] The name of the first bone to slide

<a id="unreal.RigUnit_SlideChain.start_bone"></a>

#### start_bone

```python
@start_bone.setter
def start_bone(value: Name) -> None
```

<a id="unreal.RigUnit_SlideChain.end_bone"></a>

#### end_bone

```python
@property
def end_bone() -> Name
```

(Name):  [Read-Write] The name of the last bone to slide

<a id="unreal.RigUnit_SlideChain.end_bone"></a>

#### end_bone

```python
@end_bone.setter
def end_bone(value: Name) -> None
```

<a id="unreal.RigUnit_SlideChain.slide_amount"></a>

#### slide_amount

```python
@property
def slide_amount() -> float
```

(float):  [Read-Write] The amount of sliding. This unit is multiple of the chain length.

<a id="unreal.RigUnit_SlideChain.slide_amount"></a>

#### slide_amount

```python
@slide_amount.setter
def slide_amount(value: float) -> None
```

<a id="unreal.RigUnit_SlideChain.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_SlideChainPerItem"></a>