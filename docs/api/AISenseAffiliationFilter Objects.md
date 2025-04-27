## AISenseAffiliationFilter Objects

```python
class AISenseAffiliationFilter(StructBase)
```

AISense Affiliation Filter

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``detect_enemies`` (bool):  [Read-Write]
- ``detect_friendlies`` (bool):  [Read-Write]
- ``detect_neutrals`` (bool):  [Read-Write]

<a id="unreal.AISenseAffiliationFilter.__init__"></a>

#### __init__

```python
def __init__(detect_enemies: bool = False,
             detect_neutrals: bool = False,
             detect_friendlies: bool = False) -> None
```

<a id="unreal.AISenseAffiliationFilter.detect_enemies"></a>

#### detect_enemies

```python
@property
def detect_enemies() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AISenseAffiliationFilter.detect_neutrals"></a>

#### detect_neutrals

```python
@property
def detect_neutrals() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AISenseAffiliationFilter.detect_friendlies"></a>

#### detect_friendlies

```python
@property
def detect_friendlies() -> bool
```

(bool):  [Read-Only]

<a id="unreal.AIDamageEvent"></a>