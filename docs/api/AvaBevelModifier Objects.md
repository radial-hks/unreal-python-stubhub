## AvaBevelModifier Objects

```python
class AvaBevelModifier(AvaGeometryBaseModifier)
```

Ava Bevel Modifier

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheModifiers
- **File**: AvaBevelModifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``inset`` (float):  [Read-Write] Distance used on vertices for beveling, clamped between 0 and (min bound size / 2)
- ``iterations`` (int32):  [Read-Write] Amount of subdivisions applied on the bevel, could affect performance the higher this value gets
- ``modifier_enabled`` (bool):  [Read-Write] Is the modifier enabled or disabled
- ``roundness`` (float):  [Read-Write] Roundness of the beveling when multiple iterations are applied : -2 = inner rounded, 0 = flat, 2 = outer rounded

<a id="unreal.AvaBevelModifier.set_roundness"></a>

#### set_roundness

```python
def set_roundness(roundness: float) -> None
```

x.set_roundness(roundness) -> None
Set Roundness

Args:
    roundness (float):

<a id="unreal.AvaBevelModifier.set_iterations"></a>

#### set_iterations

```python
def set_iterations(iterations: int) -> None
```

x.set_iterations(iterations) -> None
Set Iterations

Args:
    iterations (int32):

<a id="unreal.AvaBevelModifier.set_inset"></a>

#### set_inset

```python
def set_inset(bevel: float) -> None
```

x.set_inset(bevel) -> None
Set Inset

Args:
    bevel (float):

<a id="unreal.AvaBevelModifier.get_roundness"></a>

#### get_roundness

```python
def get_roundness() -> float
```

x.get_roundness() -> float
Get Roundness

Returns:
    float:

<a id="unreal.AvaBevelModifier.get_iterations"></a>

#### get_iterations

```python
def get_iterations() -> int
```

x.get_iterations() -> int32
Get Iterations

Returns:
    int32:

<a id="unreal.AvaBevelModifier.get_inset"></a>

#### get_inset

```python
def get_inset() -> float
```

x.get_inset() -> float
Get Inset

Returns:
    float:

<a id="unreal.AvaBooleanModifier"></a>