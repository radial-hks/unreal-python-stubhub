## InputChord Objects

```python
class InputChord(StructBase)
```

An Input Chord is a key and the modifier keys that are to be held with it.

**C++ Source:**

- **Module**: Slate
- **File**: InputChord.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alt`` (bool):  [Read-Write] Whether the alt key is part of the chord.
- ``cmd`` (bool):  [Read-Write] Whether the command key is part of the chord.
- ``ctrl`` (bool):  [Read-Write] Whether the control key is part of the chord.
- ``key`` (Key):  [Read-Write] The Key is the core of the chord.
- ``shift`` (bool):  [Read-Write] Whether the shift key is part of the chord.

<a id="unreal.InputChord.__init__"></a>

#### __init__

```python
def __init__(key: Key = [],
             shift: bool = False,
             ctrl: bool = False,
             alt: bool = False,
             cmd: bool = False) -> None
```

<a id="unreal.InputChord.key"></a>

#### key

```python
@property
def key() -> Key
```

(Key):  [Read-Write] The Key is the core of the chord.

<a id="unreal.InputChord.key"></a>

#### key

```python
@key.setter
def key(value: Key) -> None
```

<a id="unreal.InputChord.shift"></a>

#### shift

```python
@property
def shift() -> bool
```

(bool):  [Read-Write] Whether the shift key is part of the chord.

<a id="unreal.InputChord.shift"></a>

#### shift

```python
@shift.setter
def shift(value: bool) -> None
```

<a id="unreal.InputChord.ctrl"></a>

#### ctrl

```python
@property
def ctrl() -> bool
```

(bool):  [Read-Write] Whether the control key is part of the chord.

<a id="unreal.InputChord.ctrl"></a>

#### ctrl

```python
@ctrl.setter
def ctrl(value: bool) -> None
```

<a id="unreal.InputChord.alt"></a>

#### alt

```python
@property
def alt() -> bool
```

(bool):  [Read-Write] Whether the alt key is part of the chord.

<a id="unreal.InputChord.alt"></a>

#### alt

```python
@alt.setter
def alt(value: bool) -> None
```

<a id="unreal.InputChord.cmd"></a>

#### cmd

```python
@property
def cmd() -> bool
```

(bool):  [Read-Write] Whether the command key is part of the chord.

<a id="unreal.InputChord.cmd"></a>

#### cmd

```python
@cmd.setter
def cmd(value: bool) -> None
```

<a id="unreal.SpinBoxStyle"></a>