## NiagaraID Objects

```python
class NiagaraID(StructBase)
```

Niagara ID

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``acquire_tag`` (int32):  [Read-Write] A unique tag for when this ID was acquired.
  Allows us to differentiate between particles when one dies and another reuses it's Index.
- ``index`` (int32):  [Read-Write] Index in the indirection table for this particle. Allows fast access to this particles data.
  Is always unique among currently living particles but will be reused after the particle dies.

<a id="unreal.NiagaraID.__init__"></a>

#### __init__

```python
def __init__(index: int = 0, acquire_tag: int = 0) -> None
```

<a id="unreal.NiagaraID.index"></a>

#### index

```python
@property
def index() -> int
```

(int32):  [Read-Write] Index in the indirection table for this particle. Allows fast access to this particles data.
Is always unique among currently living particles but will be reused after the particle dies.

<a id="unreal.NiagaraID.index"></a>

#### index

```python
@index.setter
def index(value: int) -> None
```

<a id="unreal.NiagaraID.acquire_tag"></a>

#### acquire_tag

```python
@property
def acquire_tag() -> int
```

(int32):  [Read-Write] A unique tag for when this ID was acquired.
Allows us to differentiate between particles when one dies and another reuses it's Index.

<a id="unreal.NiagaraID.acquire_tag"></a>

#### acquire_tag

```python
@acquire_tag.setter
def acquire_tag(value: int) -> None
```

<a id="unreal.BrushEffectBlurring"></a>