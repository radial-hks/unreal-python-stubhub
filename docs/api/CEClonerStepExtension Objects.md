## CEClonerStepExtension Objects

```python
class CEClonerStepExtension(CEClonerExtensionBase)
```

Extension dealing with delta step accumulated options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerStepExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``delta_step_enabled`` (bool):  [Read-Write] Enable steps to add delta variation on each clone instance
- ``delta_step_position`` (Vector):  [Read-Write] Amount of position difference between one step and the next one
- ``delta_step_rotation`` (Rotator):  [Read-Write] Amount of rotation difference between one step and the next one
- ``delta_step_scale`` (Vector):  [Read-Write] Amount of scale difference between one step and the next one

<a id="unreal.CEClonerStepExtension.set_delta_step_scale"></a>

#### set_delta_step_scale

```python
def set_delta_step_scale(scale: Vector) -> None
```

x.set_delta_step_scale(scale) -> None
Set Delta Step Scale

Args:
    scale (Vector):

<a id="unreal.CEClonerStepExtension.set_delta_step_rotation"></a>

#### set_delta_step_rotation

```python
def set_delta_step_rotation(rotation: Rotator) -> None
```

x.set_delta_step_rotation(rotation) -> None
Set Delta Step Rotation

Args:
    rotation (Rotator):

<a id="unreal.CEClonerStepExtension.set_delta_step_position"></a>

#### set_delta_step_position

```python
def set_delta_step_position(position: Vector) -> None
```

x.set_delta_step_position(position) -> None
Set Delta Step Position

Args:
    position (Vector):

<a id="unreal.CEClonerStepExtension.set_delta_step_enabled"></a>

#### set_delta_step_enabled

```python
def set_delta_step_enabled(enabled: bool) -> None
```

x.set_delta_step_enabled(enabled) -> None
Set Delta Step Enabled

Args:
    enabled (bool):

<a id="unreal.CEClonerStepExtension.get_delta_step_scale"></a>

#### get_delta_step_scale

```python
def get_delta_step_scale() -> Vector
```

x.get_delta_step_scale() -> Vector
Get Delta Step Scale

Returns:
    Vector:

<a id="unreal.CEClonerStepExtension.get_delta_step_rotation"></a>

#### get_delta_step_rotation

```python
def get_delta_step_rotation() -> Rotator
```

x.get_delta_step_rotation() -> Rotator
Get Delta Step Rotation

Returns:
    Rotator:

<a id="unreal.CEClonerStepExtension.get_delta_step_position"></a>

#### get_delta_step_position

```python
def get_delta_step_position() -> Vector
```

x.get_delta_step_position() -> Vector
Get Delta Step Position

Returns:
    Vector:

<a id="unreal.CEClonerStepExtension.get_delta_step_enabled"></a>

#### get_delta_step_enabled

```python
def get_delta_step_enabled() -> bool
```

x.get_delta_step_enabled() -> bool
Get Delta Step Enabled

Returns:
    bool:

<a id="unreal.CEEffectorActor"></a>