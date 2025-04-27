## BasedPosition Objects

```python
class BasedPosition(StructBase)
```

Struct for handling positions relative to a base actor, which is potentially moving

**C++ Source:**

- **Module**: Engine
- **File**: EngineTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base`` (Actor):  [Read-Write] Actor that is the base
- ``position`` (Vector):  [Read-Write] Position relative to the base actor

<a id="unreal.BasedPosition.__init__"></a>

#### __init__

```python
def __init__(base: Actor = None,
             position: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.BasedPosition.base"></a>

#### base

```python
@property
def base() -> Actor
```

(Actor):  [Read-Write] Actor that is the base

<a id="unreal.BasedPosition.base"></a>

#### base

```python
@base.setter
def base(value: Actor) -> None
```

<a id="unreal.BasedPosition.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write] Position relative to the base actor

<a id="unreal.BasedPosition.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.POV"></a>