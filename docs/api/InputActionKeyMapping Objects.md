## InputActionKeyMapping Objects

```python
class InputActionKeyMapping(StructBase)
```

Defines a mapping between an action and key
see: https://docs.unrealengine.com/latest/INT/Gameplay/Input/index.html

**C++ Source:**

- **Module**: Engine
- **File**: PlayerInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``action_name`` (Name):  [Read-Write] Friendly name of action, e.g "jump"
- ``alt`` (bool):  [Read-Write] true if one of the Alt keys must be down when the KeyEvent is received to be acknowledged
- ``cmd`` (bool):  [Read-Write] true if one of the Cmd keys must be down when the KeyEvent is received to be acknowledged
- ``ctrl`` (bool):  [Read-Write] true if one of the Ctrl keys must be down when the KeyEvent is received to be acknowledged
- ``key`` (Key):  [Read-Write] Key to bind it to.
- ``shift`` (bool):  [Read-Write] true if one of the Shift keys must be down when the KeyEvent is received to be acknowledged

<a id="unreal.InputActionKeyMapping.__init__"></a>

#### __init__

```python
def __init__(action_name: Name = "None",
             shift: bool = False,
             ctrl: bool = False,
             alt: bool = False,
             cmd: bool = False,
             key: Key = []) -> None
```

<a id="unreal.InputActionKeyMapping.action_name"></a>

#### action_name

```python
@property
def action_name() -> Name
```

(Name):  [Read-Write] Friendly name of action, e.g "jump"

<a id="unreal.InputActionKeyMapping.action_name"></a>

#### action_name

```python
@action_name.setter
def action_name(value: Name) -> None
```

<a id="unreal.InputActionKeyMapping.shift"></a>

#### shift

```python
@property
def shift() -> bool
```

(bool):  [Read-Write] true if one of the Shift keys must be down when the KeyEvent is received to be acknowledged

<a id="unreal.InputActionKeyMapping.shift"></a>

#### shift

```python
@shift.setter
def shift(value: bool) -> None
```

<a id="unreal.InputActionKeyMapping.ctrl"></a>

#### ctrl

```python
@property
def ctrl() -> bool
```

(bool):  [Read-Write] true if one of the Ctrl keys must be down when the KeyEvent is received to be acknowledged

<a id="unreal.InputActionKeyMapping.ctrl"></a>

#### ctrl

```python
@ctrl.setter
def ctrl(value: bool) -> None
```

<a id="unreal.InputActionKeyMapping.alt"></a>

#### alt

```python
@property
def alt() -> bool
```

(bool):  [Read-Write] true if one of the Alt keys must be down when the KeyEvent is received to be acknowledged

<a id="unreal.InputActionKeyMapping.alt"></a>

#### alt

```python
@alt.setter
def alt(value: bool) -> None
```

<a id="unreal.InputActionKeyMapping.cmd"></a>

#### cmd

```python
@property
def cmd() -> bool
```

(bool):  [Read-Write] true if one of the Cmd keys must be down when the KeyEvent is received to be acknowledged

<a id="unreal.InputActionKeyMapping.cmd"></a>

#### cmd

```python
@cmd.setter
def cmd(value: bool) -> None
```

<a id="unreal.InputActionKeyMapping.key"></a>

#### key

```python
@property
def key() -> Key
```

(Key):  [Read-Write] Key to bind it to.

<a id="unreal.InputActionKeyMapping.key"></a>

#### key

```python
@key.setter
def key(value: Key) -> None
```

<a id="unreal.InputAxisKeyMapping"></a>