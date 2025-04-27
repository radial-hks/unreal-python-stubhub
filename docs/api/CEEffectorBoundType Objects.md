## CEEffectorBoundType Objects

```python
class CEEffectorBoundType(CEEffectorTypeBase)
```

CEEffector Bound Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorBoundType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside

<a id="unreal.CEEffectorBoundType.set_invert_type"></a>

#### set_invert_type

```python
def set_invert_type(invert: bool) -> None
```

x.set_invert_type(invert) -> None
Set Invert Type

Args:
    invert (bool):

<a id="unreal.CEEffectorBoundType.set_easing"></a>

#### set_easing

```python
def set_easing(easing: CEClonerEasing) -> None
```

x.set_easing(easing) -> None
Set Easing

Args:
    easing (CEClonerEasing):

<a id="unreal.CEEffectorBoundType.get_invert_type"></a>

#### get_invert_type

```python
def get_invert_type() -> bool
```

x.get_invert_type() -> bool
Get Invert Type

Returns:
    bool:

<a id="unreal.CEEffectorBoundType.get_easing"></a>

#### get_easing

```python
def get_easing() -> CEClonerEasing
```

x.get_easing() -> CEClonerEasing
Get Easing

Returns:
    CEClonerEasing:

<a id="unreal.CEEffectorBoxType"></a>