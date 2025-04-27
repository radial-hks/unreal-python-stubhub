## ChaosRemovalEvent Objects

```python
class ChaosRemovalEvent(StructBase)
```

Chaos Removal Event

**C++ Source:**

- **Module**: Engine
- **File**: ChaosEventType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component`` (PrimitiveComponent):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``mass`` (float):  [Read-Write]

<a id="unreal.ChaosRemovalEvent.__init__"></a>

#### __init__

```python
def __init__(component: PrimitiveComponent = None,
             location: Vector = [0.000000, 0.000000, 0.000000],
             mass: float = 0.000000) -> None
```

<a id="unreal.ChaosRemovalEvent.component"></a>

#### component

```python
@property
def component() -> PrimitiveComponent
```

(PrimitiveComponent):  [Read-Only]

<a id="unreal.ChaosRemovalEvent.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.ChaosRemovalEvent.mass"></a>

#### mass

```python
@property
def mass() -> float
```

(float):  [Read-Only]

<a id="unreal.InterpControlPoint"></a>