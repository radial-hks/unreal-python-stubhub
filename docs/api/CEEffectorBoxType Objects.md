## CEEffectorBoxType Objects

```python
class CEEffectorBoxType(CEEffectorBoundType)
```

CEEffector Box Type

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEEffectorBoxType.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``easing`` (CEClonerEasing):  [Read-Write] Weight easing function applied to lerp transforms
- ``inner_extent`` (Vector):  [Read-Write] Inner extent of box, all clones inside will be affected with a maximum weight
- ``invert_type`` (bool):  [Read-Write] Invert the type effect, instead of affecting the inside of a zone, will affect the outside
- ``outer_extent`` (Vector):  [Read-Write] Outer extent of box, all clones outside will not be affected

<a id="unreal.CEEffectorBoxType.set_outer_extent"></a>

#### set_outer_extent

```python
def set_outer_extent(extent: Vector) -> None
```

x.set_outer_extent(extent) -> None
Set Outer Extent

Args:
    extent (Vector):

<a id="unreal.CEEffectorBoxType.set_inner_extent"></a>

#### set_inner_extent

```python
def set_inner_extent(extent: Vector) -> None
```

x.set_inner_extent(extent) -> None
Set Inner Extent

Args:
    extent (Vector):

<a id="unreal.CEEffectorBoxType.get_outer_extent"></a>

#### get_outer_extent

```python
def get_outer_extent() -> Vector
```

x.get_outer_extent() -> Vector
Get Outer Extent

Returns:
    Vector:

<a id="unreal.CEEffectorBoxType.get_inner_extent"></a>

#### get_inner_extent

```python
def get_inner_extent() -> Vector
```

x.get_inner_extent() -> Vector
Get Inner Extent

Returns:
    Vector:

<a id="unreal.CEEffectorForceExtension"></a>