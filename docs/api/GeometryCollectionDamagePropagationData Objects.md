## GeometryCollectionDamagePropagationData Objects

```python
class GeometryCollectionDamagePropagationData(StructBase)
```

Geometry Collection Damage Propagation Data

**C++ Source:**

- **Module**: GeometryCollectionEngine
- **File**: GeometryCollectionDamagePropagationData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_damage_propagation_factor`` (float):  [Read-Write] factor of the remaining strain propagated through the connection graph after a piece breaks.
- ``enabled`` (bool):  [Read-Write] Whether or not damage propagation is enabled.
- ``shock_damage_propagation_factor`` (float):  [Read-Write] factor of the received strain propagated throug the connection graph if the piece did not break.

<a id="unreal.GeometryCollectionDamagePropagationData.__init__"></a>

#### __init__

```python
def __init__(enabled: bool = False,
             break_damage_propagation_factor: float = 0.000000,
             shock_damage_propagation_factor: float = 0.000000) -> None
```

<a id="unreal.GeometryCollectionDamagePropagationData.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write] Whether or not damage propagation is enabled.

<a id="unreal.GeometryCollectionDamagePropagationData.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.GeometryCollectionDamagePropagationData.break_damage_propagation_factor"></a>

#### break_damage_propagation_factor

```python
@property
def break_damage_propagation_factor() -> float
```

(float):  [Read-Write] factor of the remaining strain propagated through the connection graph after a piece breaks.

<a id="unreal.GeometryCollectionDamagePropagationData.break_damage_propagation_factor"></a>

#### break_damage_propagation_factor

```python
@break_damage_propagation_factor.setter
def break_damage_propagation_factor(value: float) -> None
```

<a id="unreal.GeometryCollectionDamagePropagationData.shock_damage_propagation_factor"></a>

#### shock_damage_propagation_factor

```python
@property
def shock_damage_propagation_factor() -> float
```

(float):  [Read-Write] factor of the received strain propagated throug the connection graph if the piece did not break.

<a id="unreal.GeometryCollectionDamagePropagationData.shock_damage_propagation_factor"></a>

#### shock_damage_propagation_factor

```python
@shock_damage_propagation_factor.setter
def shock_damage_propagation_factor(value: float) -> None
```

<a id="unreal.Geometry"></a>