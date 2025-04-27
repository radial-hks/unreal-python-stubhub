## RigUnit_IsInteracting Objects

```python
class RigUnit_IsInteracting(RigUnit)
```

Returns true if the Control Rig is being interacted

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigUnit_IsInteracting.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_interacting`` (bool):  [Read-Write] True if there is currently an interaction happening
- ``is_rotating`` (bool):  [Read-Write] True if the current interaction is a rotation
- ``is_scaling`` (bool):  [Read-Write] True if the current interaction is scaling
- ``is_translating`` (bool):  [Read-Write] True if the current interaction is a translation
- ``items`` (Array[RigElementKey]):  [Read-Write] The items being interacted on

<a id="unreal.RigUnit_IsInteracting.__init__"></a>

#### __init__

```python
def __init__(is_interacting: bool = False,
             is_translating: bool = False,
             is_rotating: bool = False,
             is_scaling: bool = False,
             items: Array[RigElementKey] = []) -> None
```

<a id="unreal.RigUnit_IsInteracting.is_interacting"></a>

#### is_interacting

```python
@property
def is_interacting() -> bool
```

(bool):  [Read-Only] True if there is currently an interaction happening

<a id="unreal.RigUnit_IsInteracting.is_translating"></a>

#### is_translating

```python
@property
def is_translating() -> bool
```

(bool):  [Read-Only] True if the current interaction is a translation

<a id="unreal.RigUnit_IsInteracting.is_rotating"></a>

#### is_rotating

```python
@property
def is_rotating() -> bool
```

(bool):  [Read-Only] True if the current interaction is a rotation

<a id="unreal.RigUnit_IsInteracting.is_scaling"></a>

#### is_scaling

```python
@property
def is_scaling() -> bool
```

(bool):  [Read-Only] True if the current interaction is scaling

<a id="unreal.RigUnit_IsInteracting.items"></a>

#### items

```python
@property
def items() -> Array[RigElementKey]
```

(Array[RigElementKey]):  [Read-Only] The items being interacted on

<a id="unreal.RigUnit_ItemBase"></a>