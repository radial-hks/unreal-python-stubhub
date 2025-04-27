## ControlRigComponentMappedComponent Objects

```python
class ControlRigComponentMappedComponent(StructBase)
```

Control Rig Component Mapped Component

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component`` (SceneComponent):  [Read-Write]
- ``direction`` (ControlRigComponentMapDirection):  [Read-Write]
- ``element_name`` (Name):  [Read-Write]
- ``element_type`` (RigElementType):  [Read-Write] The type of element this is mapped to

<a id="unreal.ControlRigComponentMappedComponent.__init__"></a>

#### __init__

```python
def __init__(
    component: SceneComponent = None,
    element_name: Name = "None",
    element_type: RigElementType = RigElementType.NONE,
    direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection
    .INPUT
) -> None
```

<a id="unreal.ControlRigComponentMappedComponent.component"></a>

#### component

```python
@property
def component() -> SceneComponent
```

(SceneComponent):  [Read-Write]

<a id="unreal.ControlRigComponentMappedComponent.component"></a>

#### component

```python
@component.setter
def component(value: SceneComponent) -> None
```

<a id="unreal.ControlRigComponentMappedComponent.element_name"></a>

#### element_name

```python
@property
def element_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ControlRigComponentMappedComponent.element_name"></a>

#### element_name

```python
@element_name.setter
def element_name(value: Name) -> None
```

<a id="unreal.ControlRigComponentMappedComponent.element_type"></a>

#### element_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write] The type of element this is mapped to

<a id="unreal.ControlRigComponentMappedComponent.element_type"></a>

#### element_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.ControlRigComponentMappedComponent.direction"></a>

#### direction

```python
@property
def direction() -> ControlRigComponentMapDirection
```

(ControlRigComponentMapDirection):  [Read-Write]

<a id="unreal.ControlRigComponentMappedComponent.direction"></a>

#### direction

```python
@direction.setter
def direction(value: ControlRigComponentMapDirection) -> None
```

<a id="unreal.ControlRigComponentMappedBone"></a>