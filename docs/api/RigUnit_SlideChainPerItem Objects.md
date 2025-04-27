## RigUnit_SlideChainPerItem Objects

```python
class RigUnit_SlideChainPerItem(RigUnit_HighlevelBaseMutable)
```

Slides an existing chain along itself with control over extrapolation.

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_SlideChain.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``execute_context`` (ControlRigExecuteContext):  [Read-Write] * This property is used to chain multiple mutable units together
- ``items`` (RigElementKeyCollection):  [Read-Write] The items to slide
- ``propagate_to_children`` (bool):  [Read-Only] If set to true all of the global transforms of the children
  of this bone will be recalculated based on their local transforms.
  Note: This is computationally more expensive than turning it off.
- ``slide_amount`` (float):  [Read-Write] The amount of sliding. This unit is multiple of the chain length.

<a id="unreal.RigUnit_SlideChainPerItem.__init__"></a>

#### __init__

```python
def __init__(execute_context: ControlRigExecuteContext = [],
             items: RigElementKeyCollection = [[]],
             slide_amount: float = 0.000000,
             propagate_to_children: bool = False) -> None
```

<a id="unreal.RigUnit_SlideChainPerItem.items"></a>

#### items

```python
@property
def items() -> RigElementKeyCollection
```

(RigElementKeyCollection):  [Read-Write] The items to slide

<a id="unreal.RigUnit_SlideChainPerItem.items"></a>

#### items

```python
@items.setter
def items(value: RigElementKeyCollection) -> None
```

<a id="unreal.RigUnit_SlideChainPerItem.slide_amount"></a>

#### slide_amount

```python
@property
def slide_amount() -> float
```

(float):  [Read-Write] The amount of sliding. This unit is multiple of the chain length.

<a id="unreal.RigUnit_SlideChainPerItem.slide_amount"></a>

#### slide_amount

```python
@slide_amount.setter
def slide_amount(value: float) -> None
```

<a id="unreal.RigUnit_SlideChainPerItem.propagate_to_children"></a>

#### propagate_to_children

```python
@property
def propagate_to_children() -> bool
```

(bool):  [Read-Only] If set to true all of the global transforms of the children
of this bone will be recalculated based on their local transforms.
Note: This is computationally more expensive than turning it off.

<a id="unreal.RigUnit_SlideChainItemArray"></a>