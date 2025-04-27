## ChaosClothingInteractor Objects

```python
class ChaosClothingInteractor(ClothingInteractor)
```

Chaos Clothing Interactor

**C++ Source:**

- **Plugin**: ChaosCloth
- **Module**: ChaosCloth
- **File**: ChaosClothingSimulationInteractor.h

<a id="unreal.ChaosClothingInteractor.set_wind"></a>

#### set_wind

```python
def set_wind(drag: Vector2D = [0.070000, 0.500000],
             lift: Vector2D = [0.070000, 0.500000],
             air_density: float = 0.000001,
             wind_velocity: Vector = [0.000000, 0.000000, 0.000000],
             outer_drag: Vector2D = [0.070000, 0.500000],
             outer_lift: Vector2D = [0.070000, 0.500000]) -> None
```

x.set_wind(drag=[0.070000, 0.500000], lift=[0.070000, 0.500000], air_density=0.000001, wind_velocity=[0.000000, 0.000000, 0.000000], outer_drag=[0.070000, 0.500000], outer_lift=[0.070000, 0.500000]) -> None
Set Wind

Args:
    drag (Vector2D): 
    lift (Vector2D): 
    air_density (float): 
    wind_velocity (Vector): 
    outer_drag (Vector2D): 
    outer_lift (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_velocity_scale"></a>

#### set_velocity_scale

```python
def set_velocity_scale(linear_velocity_scale: Vector = [
    0.750000, 0.750000, 0.750000
],
                       angular_velocity_scale: float = 0.750000,
                       fictitious_angular_scale: float = 1.000000) -> None
```

x.set_velocity_scale(linear_velocity_scale=[0.750000, 0.750000, 0.750000], angular_velocity_scale=0.750000, fictitious_angular_scale=1.000000) -> None
Set Velocity Scale

Args:
    linear_velocity_scale (Vector): 
    angular_velocity_scale (float): 
    fictitious_angular_scale (float):

<a id="unreal.ChaosClothingInteractor.set_pressure"></a>

#### set_pressure

```python
def set_pressure(pressure: Vector2D = [0.000000, 1.000000]) -> None
```

x.set_pressure(pressure=[0.000000, 1.000000]) -> None
Set Pressure

Args:
    pressure (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_material_linear"></a>

#### set_material_linear

```python
def set_material_linear(edge_stiffness: float = 1.000000,
                        bending_stiffness: float = 1.000000,
                        area_stiffness: float = 1.000000) -> None
```

x.set_material_linear(edge_stiffness=1.000000, bending_stiffness=1.000000, area_stiffness=1.000000) -> None
Set Material Linear

Args:
    edge_stiffness (float): 
    bending_stiffness (float): 
    area_stiffness (float):

<a id="unreal.ChaosClothingInteractor.set_material_buckling"></a>

#### set_material_buckling

```python
def set_material_buckling(
        buckling_ratio: Vector2D = [0.000000, 0.000000],
        buckling_stiffness: Vector2D = [1.000000, 1.000000]) -> None
```

x.set_material_buckling(buckling_ratio=[0.000000, 0.000000], buckling_stiffness=[1.000000, 1.000000]) -> None
Set Material Buckling

Args:
    buckling_ratio (Vector2D): 
    buckling_stiffness (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_material"></a>

#### set_material

```python
def set_material(edge_stiffness: Vector2D = [1.000000, 1.000000],
                 bending_stiffness: Vector2D = [1.000000, 1.000000],
                 area_stiffness: Vector2D = [1.000000, 1.000000]) -> None
```

x.set_material(edge_stiffness=[1.000000, 1.000000], bending_stiffness=[1.000000, 1.000000], area_stiffness=[1.000000, 1.000000]) -> None
Set Material

Args:
    edge_stiffness (Vector2D): 
    bending_stiffness (Vector2D): 
    area_stiffness (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_long_range_attachment_linear"></a>

#### set_long_range_attachment_linear

```python
def set_long_range_attachment_linear(tether_stiffness: float = 1.000000,
                                     tether_scale: float = 1.000000) -> None
```

x.set_long_range_attachment_linear(tether_stiffness=1.000000, tether_scale=1.000000) -> None
Set Long Range Attachment Linear

Args:
    tether_stiffness (float): 
    tether_scale (float):

<a id="unreal.ChaosClothingInteractor.set_long_range_attachment"></a>

#### set_long_range_attachment

```python
def set_long_range_attachment(
        tether_stiffness: Vector2D = [1.000000, 1.000000],
        tether_scale: Vector2D = [1.000000, 1.000000]) -> None
```

x.set_long_range_attachment(tether_stiffness=[1.000000, 1.000000], tether_scale=[1.000000, 1.000000]) -> None
Set Long Range Attachment

Args:
    tether_stiffness (Vector2D): 
    tether_scale (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_gravity"></a>

#### set_gravity

```python
def set_gravity(
        gravity_scale: float = 1.000000,
        is_gravity_overridden: bool = False,
        gravity_override: Vector = [0.000000, 0.000000, -981.000000]) -> None
```

x.set_gravity(gravity_scale=1.000000, is_gravity_overridden=False, gravity_override=[0.000000, 0.000000, -981.000000]) -> None
Set Gravity

Args:
    gravity_scale (float): 
    is_gravity_overridden (bool): 
    gravity_override (Vector):

<a id="unreal.ChaosClothingInteractor.set_damping"></a>

#### set_damping

```python
def set_damping(damping_coefficient: float = 0.010000,
                local_damping_coefficient: float = 0.000000) -> None
```

x.set_damping(damping_coefficient=0.010000, local_damping_coefficient=0.000000) -> None
Set Damping

Args:
    damping_coefficient (float): 
    local_damping_coefficient (float):

<a id="unreal.ChaosClothingInteractor.set_collision"></a>

#### set_collision

```python
def set_collision(collision_thickness: float = 1.000000,
                  friction_coefficient: float = 0.800000,
                  use_ccd: bool = False,
                  self_collision_thickness: float = 2.000000) -> None
```

x.set_collision(collision_thickness=1.000000, friction_coefficient=0.800000, use_ccd=False, self_collision_thickness=2.000000) -> None
Set Collision

Args:
    collision_thickness (float): 
    friction_coefficient (float): 
    use_ccd (bool): 
    self_collision_thickness (float):

<a id="unreal.ChaosClothingInteractor.set_backstop"></a>

#### set_backstop

```python
def set_backstop(enabled: bool = True) -> None
```

x.set_backstop(enabled=True) -> None
Set Backstop

Args:
    enabled (bool):

<a id="unreal.ChaosClothingInteractor.set_anim_drive_linear"></a>

#### set_anim_drive_linear

```python
def set_anim_drive_linear(anim_drive_stiffness: float = 0.000000) -> None
```

x.set_anim_drive_linear(anim_drive_stiffness=0.000000) -> None
Set Anim Drive Linear

Args:
    anim_drive_stiffness (float):

<a id="unreal.ChaosClothingInteractor.set_anim_drive"></a>

#### set_anim_drive

```python
def set_anim_drive(
        anim_drive_stiffness: Vector2D = [0.000000, 1.000000],
        anim_drive_damping: Vector2D = [0.000000, 1.000000]) -> None
```

x.set_anim_drive(anim_drive_stiffness=[0.000000, 1.000000], anim_drive_damping=[0.000000, 1.000000]) -> None
Set Anim Drive

Args:
    anim_drive_stiffness (Vector2D): 
    anim_drive_damping (Vector2D):

<a id="unreal.ChaosClothingInteractor.set_aerodynamics"></a>

#### set_aerodynamics

```python
def set_aerodynamics(
        drag_coefficient: float = 0.070000,
        lift_coefficient: float = 0.035000,
        wind_velocity: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

x.set_aerodynamics(drag_coefficient=0.070000, lift_coefficient=0.035000, wind_velocity=[0.000000, 0.000000, 0.000000]) -> None
Deprecated. This function cannot set different Low and High values for the Drag and Lift weight maps. Use SetWind instead.

Args:
    drag_coefficient (float): 
    lift_coefficient (float): 
    wind_velocity (Vector):

<a id="unreal.ChaosClothingInteractor.reset_and_teleport"></a>

#### reset_and_teleport

```python
def reset_and_teleport(reset: bool = False, teleport: bool = False) -> None
```

x.reset_and_teleport(reset=False, teleport=False) -> None
Reset and Teleport

Args:
    reset (bool): 
    teleport (bool):

<a id="unreal.ChaosClothingSimulationInteractor"></a>