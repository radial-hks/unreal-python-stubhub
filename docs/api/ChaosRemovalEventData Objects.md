## ChaosRemovalEventData Objects

```python
class ChaosRemovalEventData(StructBase)
```

A Removal event data structure.

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: ChaosRemovalEventFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write] Current removal location.
- ``mass`` (float):  [Read-Write] The mass of the removal.
- ``particle_index`` (int32):  [Read-Write] The particle index of the removal.

<a id="unreal.ChaosRemovalEventData.__init__"></a>

#### __init__

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000,
             particle_index: int = 0) -> None
```

<a id="unreal.ChaosRemovalEventData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write] Current removal location.

<a id="unreal.ChaosRemovalEventData.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.ChaosRemovalEventData.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Write] The mass of the removal.

<a id="unreal.ChaosRemovalEventData.mass"></a>

#### mass

```python
@mass.setter
def mass(value: float) -> None
```

<a id="unreal.ChaosRemovalEventData.particle_index"></a>

#### particle_index

```python
@property
def particle_index() -> int
```

(int32):  [Read-Write] The particle index of the removal.

<a id="unreal.ChaosRemovalEventData.particle_index"></a>

#### particle_index

```python
@particle_index.setter
def particle_index(value: int) -> None
```

<a id="unreal.ChaosTrailingEventData"></a>