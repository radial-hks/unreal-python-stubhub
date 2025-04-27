## PCGSubdivisionSubmodule Objects

```python
class PCGSubdivisionSubmodule(StructBase)
```

PCGSubdivision Submodule

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSubdivisionBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``debug_color`` (Vector4):  [Read-Write] For easier debugging, using Point color in conjunction with PCG Debug Color Material.
- ``scalable`` (bool):  [Read-Write] If the volume can be scaled to fit the remaining space or not.
- ``size`` (double):  [Read-Write] Size of the block, aligned on the segment direction.
- ``symbol`` (Name):  [Read-Write] Symbol for the grammar.

<a id="unreal.PCGSubdivisionSubmodule.__init__"></a>

#### __init__

```python
def __init__(
        symbol: Name = "None",
        size: float = 0.000000,
        scalable: bool = False,
        debug_color: Vector4 = [0.000000, 0.000000, 0.000000,
                                0.000000]) -> None
```

<a id="unreal.PCGSubdivisionSubmodule.symbol"></a>

#### symbol

```python
@property
def symbol() -> Name
```

(Name):  [Read-Write] Symbol for the grammar.

<a id="unreal.PCGSubdivisionSubmodule.symbol"></a>

#### symbol

```python
@symbol.setter
def symbol(value: Name) -> None
```

<a id="unreal.PCGSubdivisionSubmodule.size"></a>

#### size

```python
@property
def size() -> float
```

(double):  [Read-Write] Size of the block, aligned on the segment direction.

<a id="unreal.PCGSubdivisionSubmodule.size"></a>

#### size

```python
@size.setter
def size(value: float) -> None
```

<a id="unreal.PCGSubdivisionSubmodule.scalable"></a>

#### scalable

```python
@property
def scalable() -> bool
```

(bool):  [Read-Write] If the volume can be scaled to fit the remaining space or not.

<a id="unreal.PCGSubdivisionSubmodule.scalable"></a>

#### scalable

```python
@scalable.setter
def scalable(value: bool) -> None
```

<a id="unreal.PCGSubdivisionSubmodule.debug_color"></a>

#### debug_color

```python
@property
def debug_color() -> Vector4
```

(Vector4):  [Read-Write] For easier debugging, using Point color in conjunction with PCG Debug Color Material.

<a id="unreal.PCGSubdivisionSubmodule.debug_color"></a>

#### debug_color

```python
@debug_color.setter
def debug_color(value: Vector4) -> None
```

<a id="unreal.PCGSubdivisionModuleAttributeNames"></a>