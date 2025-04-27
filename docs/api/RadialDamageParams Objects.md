## RadialDamageParams Objects

```python
class RadialDamageParams(StructBase)
```

Parameters used to compute radial damage

**C++ Source:**

- **Module**: Engine
- **File**: DamageEvents.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``base_damage`` (float):  [Read-Write] Max damage done
- ``damage_falloff`` (float):  [Read-Write] Describes amount of exponential damage falloff
- ``inner_radius`` (float):  [Read-Write] Within InnerRadius, do max damage
- ``minimum_damage`` (float):  [Read-Write] Damage will not fall below this if within range
- ``outer_radius`` (float):  [Read-Write] Outside OuterRadius, do no damage

<a id="unreal.RadialDamageParams.__init__"></a>

#### __init__

```python
def __init__(base_damage: float = 0.000000,
             minimum_damage: float = 0.000000,
             inner_radius: float = 0.000000,
             outer_radius: float = 0.000000,
             damage_falloff: float = 0.000000) -> None
```

<a id="unreal.RadialDamageParams.base_damage"></a>

#### base_damage

```python
@property
def base_damage() -> float
```

(float):  [Read-Write] Max damage done

<a id="unreal.RadialDamageParams.base_damage"></a>

#### base_damage

```python
@base_damage.setter
def base_damage(value: float) -> None
```

<a id="unreal.RadialDamageParams.minimum_damage"></a>

#### minimum_damage

```python
@property
def minimum_damage() -> float
```

(float):  [Read-Write] Damage will not fall below this if within range

<a id="unreal.RadialDamageParams.minimum_damage"></a>

#### minimum_damage

```python
@minimum_damage.setter
def minimum_damage(value: float) -> None
```

<a id="unreal.RadialDamageParams.inner_radius"></a>

#### inner_radius

```python
@property
def inner_radius() -> float
```

(float):  [Read-Write] Within InnerRadius, do max damage

<a id="unreal.RadialDamageParams.inner_radius"></a>

#### inner_radius

```python
@inner_radius.setter
def inner_radius(value: float) -> None
```

<a id="unreal.RadialDamageParams.outer_radius"></a>

#### outer_radius

```python
@property
def outer_radius() -> float
```

(float):  [Read-Write] Outside OuterRadius, do no damage

<a id="unreal.RadialDamageParams.outer_radius"></a>

#### outer_radius

```python
@outer_radius.setter
def outer_radius(value: float) -> None
```

<a id="unreal.RadialDamageParams.damage_falloff"></a>

#### damage_falloff

```python
@property
def damage_falloff() -> float
```

(float):  [Read-Write] Describes amount of exponential damage falloff

<a id="unreal.RadialDamageParams.damage_falloff"></a>

#### damage_falloff

```python
@damage_falloff.setter
def damage_falloff(value: float) -> None
```

<a id="unreal.RadialDamageEvent"></a>