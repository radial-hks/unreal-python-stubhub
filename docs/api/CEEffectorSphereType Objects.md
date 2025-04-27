## CEEffectorSphereType Objects

```python
class CEEffectorSphereType(CEEffectorBoundType)
```

CEEffector Sphere Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorSphereType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``inner_radius`` (float):  [Read-Write] Inner radius of sphere, all clones inside will be affected with a maximum weight
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside
- ``outer_radius`` (float):  [Read-Write] Outer radius of sphere, all clones outside will not be affected

<a id="unreal.CEEffectorSphereType.set_outer_radius"></a>

#### set_outer_radius

```python
def set_outer_radius(radius: float) -> None
```

x.set_outer_radius(radius) -> None
Set Outer Radius

Args:
    radius (float):

<a id="unreal.CEEffectorSphereType.set_inner_radius"></a>

#### set_inner_radius

```python
def set_inner_radius(radius: float) -> None
```

x.set_inner_radius(radius) -> None
Set Inner Radius

Args:
    radius (float):

<a id="unreal.CEEffectorSphereType.get_outer_radius"></a>

#### get_outer_radius

```python
def get_outer_radius() -> float
```

x.get_outer_radius() -> float
Get Outer Radius

Returns:
    float:

<a id="unreal.CEEffectorSphereType.get_inner_radius"></a>

#### get_inner_radius

```python
def get_inner_radius() -> float
```

x.get_inner_radius() -> float
Get Inner Radius

Returns:
    float:

<a id="unreal.CEEffectorStepMode"></a>