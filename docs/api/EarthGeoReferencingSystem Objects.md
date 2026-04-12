## EarthGeoReferencingSystem Objects

```python
class EarthGeoReferencingSystem(StructBase)
```

FAesGeoreferencingSystem的USTRUCT容器

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesGeoreference
- **File**: AesGeoreferencingSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_level`` (int32):  [Read-Write]
- ``origin_at_planet_center`` (bool):  [Read-Write]
- ``origin_level`` (int32):  [Read-Write]
- ``origin_location`` (Vector):  [Read-Write]
- ``origin_range`` (Vector4):  [Read-Write]
- ``planet_scope`` (AesPlanetScope):  [Read-Write]
- ``planet_shape`` (AesPlanetShape):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        planet_shape: AesPlanetShape = AesPlanetShape.MERCATOR_FLAT,
        planet_scope: AesPlanetScope = AesPlanetScope.GLOBAL_SCOPE,
        origin_at_planet_center: bool = False,
        origin_location: Vector = [0.000000, 0.000000, 0.000000],
        origin_level: int = 0,
        max_level: int = 0,
        origin_range: Vector4 = [0.000000, 0.000000, 0.000000,
                                 0.000000]) -> None
```

<a id="unreal.EarthGeoReferencingSystem.planet_shape"></a>

#### planet\_shape

```python
@property
def planet_shape() -> AesPlanetShape
```

(AesPlanetShape):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.planet_shape"></a>

#### planet\_shape

```python
@planet_shape.setter
def planet_shape(value: AesPlanetShape) -> None
```

<a id="unreal.EarthGeoReferencingSystem.planet_scope"></a>

#### planet\_scope

```python
@property
def planet_scope() -> AesPlanetScope
```

(AesPlanetScope):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.planet_scope"></a>

#### planet\_scope

```python
@planet_scope.setter
def planet_scope(value: AesPlanetScope) -> None
```

<a id="unreal.EarthGeoReferencingSystem.origin_at_planet_center"></a>

#### origin\_at\_planet\_center

```python
@property
def origin_at_planet_center() -> bool
```

(bool):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.origin_at_planet_center"></a>

#### origin\_at\_planet\_center

```python
@origin_at_planet_center.setter
def origin_at_planet_center(value: bool) -> None
```

<a id="unreal.EarthGeoReferencingSystem.origin_location"></a>

#### origin\_location

```python
@property
def origin_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.origin_location"></a>

#### origin\_location

```python
@origin_location.setter
def origin_location(value: Vector) -> None
```

<a id="unreal.EarthGeoReferencingSystem.origin_level"></a>

#### origin\_level

```python
@property
def origin_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.origin_level"></a>

#### origin\_level

```python
@origin_level.setter
def origin_level(value: int) -> None
```

<a id="unreal.EarthGeoReferencingSystem.max_level"></a>

#### max\_level

```python
@property
def max_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.max_level"></a>

#### max\_level

```python
@max_level.setter
def max_level(value: int) -> None
```

<a id="unreal.EarthGeoReferencingSystem.origin_range"></a>

#### origin\_range

```python
@property
def origin_range() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.EarthGeoReferencingSystem.origin_range"></a>

#### origin\_range

```python
@origin_range.setter
def origin_range(value: Vector4) -> None
```

<a id="unreal.DynamicMeshChangeInfo"></a>