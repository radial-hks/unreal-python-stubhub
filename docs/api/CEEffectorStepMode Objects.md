## CEEffectorStepMode Objects

```python
class CEEffectorStepMode(CEEffectorModeBase)
```

CEEffector Step Mode

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorStepMode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``step_position`` (Vector):  [Read-Write] Interpolates from 0 to this position offset based on the particle index and particle count
- ``step_rotation`` (Rotator):  [Read-Write] Interpolates from 0 to this rotation based on the particle index and particle count
- ``step_scale`` (Vector):  [Read-Write] Interpolates from 1 to this scale based on the particle index and particle count

<a id="unreal.CEEffectorStepMode.set_step_scale"></a>

#### set_step_scale

```python
def set_step_scale(scale: Vector) -> None
```

x.set_step_scale(scale) -> None
Set Step Scale

Args:
    scale (Vector):

<a id="unreal.CEEffectorStepMode.set_step_rotation"></a>

#### set_step_rotation

```python
def set_step_rotation(rotation: Rotator) -> None
```

x.set_step_rotation(rotation) -> None
Set Step Rotation

Args:
    rotation (Rotator):

<a id="unreal.CEEffectorStepMode.set_step_position"></a>

#### set_step_position

```python
def set_step_position(position: Vector) -> None
```

x.set_step_position(position) -> None
Set Step Position

Args:
    position (Vector):

<a id="unreal.CEEffectorStepMode.get_step_scale"></a>

#### get_step_scale

```python
def get_step_scale() -> Vector
```

x.get_step_scale() -> Vector
Get Step Scale

Returns:
    Vector:

<a id="unreal.CEEffectorStepMode.get_step_rotation"></a>

#### get_step_rotation

```python
def get_step_rotation() -> Rotator
```

x.get_step_rotation() -> Rotator
Get Step Rotation

Returns:
    Rotator:

<a id="unreal.CEEffectorStepMode.get_step_position"></a>

#### get_step_position

```python
def get_step_position() -> Vector
```

x.get_step_position() -> Vector
Get Step Position

Returns:
    Vector:

<a id="unreal.CEEffectorTargetMode"></a>