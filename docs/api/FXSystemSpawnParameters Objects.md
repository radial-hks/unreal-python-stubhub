## FXSystemSpawnParameters Objects

```python
class FXSystemSpawnParameters(StructBase)
```

Parameters controlling the spawning behavior of FX systems via the SpawnSystemAtLocation and SpawnSystemAttached.

**C++ Source:**

- **Module**: Engine
- **File**: ParticleSystemComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attach_point_name`` (Name):  [Read-Write]
- ``attach_to_component`` (SceneComponent):  [Read-Write]
- ``auto_activate`` (bool):  [Read-Write]
- ``auto_destroy`` (bool):  [Read-Write]
- ``is_player_effect`` (bool):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``location_type`` (AttachLocation):  [Read-Write]
- ``pooling_method`` (PSCPoolMethod):  [Read-Write]
- ``pre_cull_check`` (bool):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``system_template`` (FXSystemAsset):  [Read-Write]
- ``world_context_object`` (Object):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.__init__"></a>

#### __init__

```python
def __init__(
        world_context_object: Object = None,
        system_template: FXSystemAsset = None,
        location: Vector = [0.000000, 0.000000, 0.000000],
        rotation: Rotator = [0.000000, 0.000000, 0.000000],
        scale: Vector = [0.000000, 0.000000, 0.000000],
        attach_to_component: SceneComponent = None,
        attach_point_name: Name = "None",
        location_type: AttachLocation = AttachLocation.KEEP_RELATIVE_OFFSET,
        auto_destroy: bool = False,
        auto_activate: bool = False,
        pooling_method: PSCPoolMethod = PSCPoolMethod.NONE,
        pre_cull_check: bool = False,
        is_player_effect: bool = False) -> None
```

<a id="unreal.FXSystemSpawnParameters.world_context_object"></a>

#### world_context_object

```python
@property
def world_context_object() -> Object
```

(Object):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.world_context_object"></a>

#### world_context_object

```python
@world_context_object.setter
def world_context_object(value: Object) -> None
```

<a id="unreal.FXSystemSpawnParameters.system_template"></a>

#### system_template

```python
@property
def system_template() -> FXSystemAsset
```

(FXSystemAsset):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.system_template"></a>

#### system_template

```python
@system_template.setter
def system_template(value: FXSystemAsset) -> None
```

<a id="unreal.FXSystemSpawnParameters.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.FXSystemSpawnParameters.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.FXSystemSpawnParameters.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.FXSystemSpawnParameters.attach_to_component"></a>

#### attach_to_component

```python
@property
def attach_to_component() -> SceneComponent
```

(SceneComponent):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.attach_to_component"></a>

#### attach_to_component

```python
@attach_to_component.setter
def attach_to_component(value: SceneComponent) -> None
```

<a id="unreal.FXSystemSpawnParameters.attach_point_name"></a>

#### attach_point_name

```python
@property
def attach_point_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.attach_point_name"></a>

#### attach_point_name

```python
@attach_point_name.setter
def attach_point_name(value: Name) -> None
```

<a id="unreal.FXSystemSpawnParameters.location_type"></a>

#### location_type

```python
@property
def location_type() -> AttachLocation
```

(AttachLocation):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.location_type"></a>

#### location_type

```python
@location_type.setter
def location_type(value: AttachLocation) -> None
```

<a id="unreal.FXSystemSpawnParameters.auto_destroy"></a>

#### auto_destroy

```python
@property
def auto_destroy() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.auto_destroy"></a>

#### auto_destroy

```python
@auto_destroy.setter
def auto_destroy(value: bool) -> None
```

<a id="unreal.FXSystemSpawnParameters.auto_activate"></a>

#### auto_activate

```python
@property
def auto_activate() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.auto_activate"></a>

#### auto_activate

```python
@auto_activate.setter
def auto_activate(value: bool) -> None
```

<a id="unreal.FXSystemSpawnParameters.pooling_method"></a>

#### pooling_method

```python
@property
def pooling_method() -> PSCPoolMethod
```

(PSCPoolMethod):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.pooling_method"></a>

#### pooling_method

```python
@pooling_method.setter
def pooling_method(value: PSCPoolMethod) -> None
```

<a id="unreal.FXSystemSpawnParameters.pre_cull_check"></a>

#### pre_cull_check

```python
@property
def pre_cull_check() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.pre_cull_check"></a>

#### pre_cull_check

```python
@pre_cull_check.setter
def pre_cull_check(value: bool) -> None
```

<a id="unreal.FXSystemSpawnParameters.is_player_effect"></a>

#### is_player_effect

```python
@property
def is_player_effect() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FXSystemSpawnParameters.is_player_effect"></a>

#### is_player_effect

```python
@is_player_effect.setter
def is_player_effect(value: bool) -> None
```

<a id="unreal.TViewTarget"></a>