## ControlRigComponentMappedElement Objects

```python
class ControlRigComponentMappedElement(StructBase)
```

Control Rig Component Mapped Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: ControlRigComponent.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_reference`` (SoftComponentReference):  [Read-Write] The component to map to the Control Rig
- ``direction`` (ControlRigComponentMapDirection):  [Read-Write] The direction (input / output) to be used for mapping an element
- ``element_name`` (Name):  [Read-Write] The name of the element to map to
- ``element_type`` (RigElementType):  [Read-Write] The type of element this is mapped to
- ``offset`` (Transform):  [Read-Write] The offset transform to apply
- ``space`` (ControlRigComponentSpace):  [Read-Write] space in which the mapping happens
- ``transform_index`` (int32):  [Read-Write] An optional index that can be used with components
  with multiple transforms (for example the InstancedStaticMeshComponent)
- ``transform_name`` (Name):  [Read-Write] An optional name that can be used with components
  that have sockets (for example the SkeletalMeshComponent)
- ``weight`` (float):  [Read-Write] defines how much the mapped element should be driven

<a id="unreal.ControlRigComponentMappedElement.__init__"></a>

#### __init__

```python
def __init__(
    component_reference: SoftComponentReference = [None, "None"],
    transform_index: int = 0,
    transform_name: Name = "None",
    element_type: RigElementType = RigElementType.NONE,
    element_name: Name = "None",
    direction: ControlRigComponentMapDirection = ControlRigComponentMapDirection
    .INPUT,
    offset: Transform = [[0.000000, 0.000000, 0.000000],
                         [-0.000000, 0.000000, 0.000000],
                         [1.000000, 1.000000, 1.000000]],
    weight: float = 0.000000,
    space: ControlRigComponentSpace = ControlRigComponentSpace.WORLD_SPACE
) -> None
```

<a id="unreal.ControlRigComponentMappedElement.component_reference"></a>

#### component_reference

```python
@property
def component_reference() -> SoftComponentReference
```

(SoftComponentReference):  [Read-Write] The component to map to the Control Rig

<a id="unreal.ControlRigComponentMappedElement.component_reference"></a>

#### component_reference

```python
@component_reference.setter
def component_reference(value: SoftComponentReference) -> None
```

<a id="unreal.ControlRigComponentMappedElement.transform_index"></a>

#### transform_index

```python
@property
def transform_index() -> int
```

(int32):  [Read-Write] An optional index that can be used with components
with multiple transforms (for example the InstancedStaticMeshComponent)

<a id="unreal.ControlRigComponentMappedElement.transform_index"></a>

#### transform_index

```python
@transform_index.setter
def transform_index(value: int) -> None
```

<a id="unreal.ControlRigComponentMappedElement.transform_name"></a>

#### transform_name

```python
@property
def transform_name() -> Name
```

(Name):  [Read-Write] An optional name that can be used with components
that have sockets (for example the SkeletalMeshComponent)

<a id="unreal.ControlRigComponentMappedElement.transform_name"></a>

#### transform_name

```python
@transform_name.setter
def transform_name(value: Name) -> None
```

<a id="unreal.ControlRigComponentMappedElement.element_type"></a>

#### element_type

```python
@property
def element_type() -> RigElementType
```

(RigElementType):  [Read-Write] The type of element this is mapped to

<a id="unreal.ControlRigComponentMappedElement.element_type"></a>

#### element_type

```python
@element_type.setter
def element_type(value: RigElementType) -> None
```

<a id="unreal.ControlRigComponentMappedElement.element_name"></a>

#### element_name

```python
@property
def element_name() -> Name
```

(Name):  [Read-Write] The name of the element to map to

<a id="unreal.ControlRigComponentMappedElement.element_name"></a>

#### element_name

```python
@element_name.setter
def element_name(value: Name) -> None
```

<a id="unreal.ControlRigComponentMappedElement.direction"></a>

#### direction

```python
@property
def direction() -> ControlRigComponentMapDirection
```

(ControlRigComponentMapDirection):  [Read-Write] The direction (input / output) to be used for mapping an element

<a id="unreal.ControlRigComponentMappedElement.direction"></a>

#### direction

```python
@direction.setter
def direction(value: ControlRigComponentMapDirection) -> None
```

<a id="unreal.ControlRigComponentMappedElement.offset"></a>

#### offset

```python
@property
def offset() -> Transform
```

(Transform):  [Read-Write] The offset transform to apply

<a id="unreal.ControlRigComponentMappedElement.offset"></a>

#### offset

```python
@offset.setter
def offset(value: Transform) -> None
```

<a id="unreal.ControlRigComponentMappedElement.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] defines how much the mapped element should be driven

<a id="unreal.ControlRigComponentMappedElement.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.ControlRigComponentMappedElement.space"></a>

#### space

```python
@property
def space() -> ControlRigComponentSpace
```

(ControlRigComponentSpace):  [Read-Write] space in which the mapping happens

<a id="unreal.ControlRigComponentMappedElement.space"></a>

#### space

```python
@space.setter
def space(value: ControlRigComponentSpace) -> None
```

<a id="unreal.ControlRigComponentMappedComponent"></a>