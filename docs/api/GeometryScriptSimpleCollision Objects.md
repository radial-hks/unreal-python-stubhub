## GeometryScriptSimpleCollision Objects

```python
class GeometryScriptSimpleCollision(StructBase)
```

Holds simple shapes that can be used for collision

**C++ Source:**

- **Plugin**: GeometryScripting
- **Module**: GeometryScriptingCore
- **File**: GeometryScriptTypes.h

<a id="unreal.GeometryScriptSimpleCollision.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

<a id="unreal.GeometryScriptSimpleCollision.simplify_convex_hulls"></a>

#### simplify\_convex\_hulls

```python
def simplify_convex_hulls(
        simplify_options: GeometryScriptConvexHullSimplificationOptions,
        debug: GeometryScriptDebug = None) -> bool
```

x.simplify_convex_hulls(simplify_options, debug=None) -> bool
Simplify any convex hulls in the given simple collision representation. Updates the passed-in Simple Collision.

Args:
    simplify_options (GeometryScriptConvexHullSimplificationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    has_simplified (bool): Indicates whether any convex hulls were modified

<a id="unreal.GeometryScriptSimpleCollision.get_simple_collision_shape_count"></a>

#### get\_simple\_collision\_shape\_count

```python
def get_simple_collision_shape_count() -> int
```

x.get_simple_collision_shape_count() -> int32
* Count of number of simple collision shapes

Returns:
    int32:

<a id="unreal.GeometryScriptSimpleCollision.combine_simple_collision"></a>

#### combine\_simple\_collision

```python
def combine_simple_collision(append_collision: GeometryScriptSimpleCollision,
                             debug: GeometryScriptDebug = None) -> None
```

x.combine_simple_collision(append_collision, debug=None) -> None
* Add simple collision shapes from AppendCollision to CollisionToUpdate

Args:
    append_collision (GeometryScriptSimpleCollision): 
    debug (GeometryScriptDebug):

<a id="unreal.GeometryScriptSimpleCollision.approximate_convex_hulls_with_simpler_collision_shapes"></a>

#### approximate\_convex\_hulls\_with\_simpler\_collision\_shapes

```python
def approximate_convex_hulls_with_simpler_collision_shapes(
        approximate_options: GeometryScriptConvexHullApproximationOptions,
        debug: GeometryScriptDebug = None) -> bool
```

x.approximate_convex_hulls_with_simpler_collision_shapes(approximate_options, debug=None) -> bool
Attempt to approximate any convex hulls in the given simple collision representation. Updates the passed-in Simple Collision.
Convex hulls that aren't well approximated (to tolerances set in ApproximateOptions) will remain as convex hulls.

Args:
    approximate_options (GeometryScriptConvexHullApproximationOptions): 
    debug (GeometryScriptDebug): 

Returns:
    bool: 

    has_approximated (bool): Indicates whether any convex hulls were replaced with simpler approximations

<a id="unreal.GeometryScriptSphereCovering"></a>