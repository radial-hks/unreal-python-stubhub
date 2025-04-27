## GeometryScriptTransformCollisionOptions Objects

```python
class GeometryScriptTransformCollisionOptions(StructBase)
```

Geometry Script Transform Collision Options

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: CollisionFunctions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center_transform_pivot_per_shape`` (bool):  [Read-Write] If true, we apply the Transform to each collision shape separately, and pivot the Transform around the local center of each shape.
  Otherwise, we apply the Transform to all shapes in the same space, with the pivot at the origin of the origin of that space.

  For example, if we apply a uniform 2x scale to a sphere w/ center (1,1,1), with this enabled, the center will not move and only the radius will scale.
  If this setting is not enabled, the 2x scale will move the sphere center to (2,2,2)
- ``warn_on_invalid_transforms`` (bool):  [Read-Write] Whether to log a warning when a requested transform is not compatible with the simple collision shapes

<a id="unreal.GeometryScriptTransformCollisionOptions.__init__"></a>

#### __init__

```python
def __init__(warn_on_invalid_transforms: bool = False,
             center_transform_pivot_per_shape: bool = False) -> None
```

<a id="unreal.GeometryScriptTransformCollisionOptions.warn_on_invalid_transforms"></a>

#### warn_on_invalid_transforms

```python
@property
def warn_on_invalid_transforms() -> bool
```

(bool):  [Read-Write] Whether to log a warning when a requested transform is not compatible with the simple collision shapes

<a id="unreal.GeometryScriptTransformCollisionOptions.warn_on_invalid_transforms"></a>

#### warn_on_invalid_transforms

```python
@warn_on_invalid_transforms.setter
def warn_on_invalid_transforms(value: bool) -> None
```

<a id="unreal.GeometryScriptTransformCollisionOptions.center_transform_pivot_per_shape"></a>

#### center_transform_pivot_per_shape

```python
@property
def center_transform_pivot_per_shape() -> bool
```

(bool):  [Read-Write] If true, we apply the Transform to each collision shape separately, and pivot the Transform around the local center of each shape.
Otherwise, we apply the Transform to all shapes in the same space, with the pivot at the origin of the origin of that space.

For example, if we apply a uniform 2x scale to a sphere w/ center (1,1,1), with this enabled, the center will not move and only the radius will scale.
If this setting is not enabled, the 2x scale will move the sphere center to (2,2,2)

<a id="unreal.GeometryScriptTransformCollisionOptions.center_transform_pivot_per_shape"></a>

#### center_transform_pivot_per_shape

```python
@center_transform_pivot_per_shape.setter
def center_transform_pivot_per_shape(value: bool) -> None
```

<a id="unreal.GeometryScriptConvexHullOptions"></a>