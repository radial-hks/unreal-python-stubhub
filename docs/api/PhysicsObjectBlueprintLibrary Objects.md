## PhysicsObjectBlueprintLibrary Objects

```python
class PhysicsObjectBlueprintLibrary(BlueprintFunctionLibrary)
```

Physics Object Blueprint Library

**C++ Source:**

- **Module**: Engine
- **File**: PhysicsObjectBlueprintLibrary.h

<a id="unreal.PhysicsObjectBlueprintLibrary.get_physics_object_world_transform"></a>

#### get_physics_object_world_transform

```python
@classmethod
def get_physics_object_world_transform(cls, component: PrimitiveComponent,
                                       bone_name: Name) -> Transform
```

X.get_physics_object_world_transform(component, bone_name) -> Transform
Get Physics Object World Transform

Args:
    component (PrimitiveComponent): 
    bone_name (Name): 

Returns:
    Transform:

<a id="unreal.PhysicsObjectBlueprintLibrary.get_closest_physics_object_from_world_location"></a>

#### get_closest_physics_object_from_world_location

```python
@classmethod
def get_closest_physics_object_from_world_location(
        cls, component: PrimitiveComponent,
        world_location: Vector) -> ClosestPhysicsObjectResult
```

X.get_closest_physics_object_from_world_location(component, world_location) -> ClosestPhysicsObjectResult
Get Closest Physics Object from World Location

Args:
    component (PrimitiveComponent): 
    world_location (Vector): 

Returns:
    ClosestPhysicsObjectResult:

<a id="unreal.PhysicsObjectBlueprintLibrary.extract_closest_physics_object_results"></a>

#### extract_closest_physics_object_results

```python
@classmethod
def extract_closest_physics_object_results(
        cls, result: ClosestPhysicsObjectResult) -> Optional[Name]
```

X.extract_closest_physics_object_results(result) -> Name or None
Extract Closest Physics Object Results

Args:
    result (ClosestPhysicsObjectResult): 

Returns:
    Name or None: 

    out_name (Name):

<a id="unreal.PhysicsObjectBlueprintLibrary.apply_radial_impulse"></a>

#### apply_radial_impulse

```python
@classmethod
def apply_radial_impulse(cls,
                         component: PrimitiveComponent,
                         origin: Vector,
                         radius: float,
                         strength: float,
                         falloff: RadialImpulseFalloff,
                         apply_strain: bool,
                         strain: float,
                         vel_change: bool = False,
                         min_value: float = 0.000000,
                         max_value: float = 1.000000) -> None
```

X.apply_radial_impulse(component, origin, radius, strength, falloff, apply_strain, strain, vel_change=False, min_value=0.000000, max_value=1.000000) -> None
Apply a physics radial impulse with an optional strain on a specific component
Effect is applied within a sphere. When using linear falloff the effect will be minimum at the outer edge of the sphere and maximum at its center

Args:
    component (PrimitiveComponent): Primitive component to apply the impulse / strain on
    origin (Vector): Positition of the origin of the radial effect in world space
    radius (float): Radius of the radial effect ( beyond the radius, impulse will not be applied )
    strength (float): Strength of the impulse to apply ( Unit : (Kg * m / s) or ( m /s ) if bVelChange is true
    falloff (RadialImpulseFalloff): Type of falloff to use ( constant, linear )
    apply_strain (bool): Whether or not to apply strain on top of the impulse ( for destructible objects )
    strain (float): If bApplyStrain is true, Strain to apply to the physics particles ( for destructible objects )
    vel_change (bool): If true, impulse Strength parameter is interpretation as a change of velocity
    min_value (float): When using linear falloff, this define the falloff value at the outer edge of the sphere
    max_value (float): When using linear falloff, this define the falloff value at the center of the sphere

<a id="unreal.PhysicsSpringComponent"></a>