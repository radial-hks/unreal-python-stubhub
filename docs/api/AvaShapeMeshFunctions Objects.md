## AvaShapeMeshFunctions Objects

```python
class AvaShapeMeshFunctions(BlueprintFunctionLibrary)
```

FunctionLibrary to Create Ava Shape Meshes and apply them to a Shape Actor.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapePrimitiveFunctions.h

<a id="unreal.AvaShapeMeshFunctions.set_rectangle"></a>

#### set_rectangle

```python
@classmethod
def set_rectangle(cls, shape_actor: AvaShapeActor, size: Vector2D,
                  transform: Transform) -> AvaShapeRectangleDynamicMesh
```

X.set_rectangle(shape_actor, size, transform) -> AvaShapeRectangleDynamicMesh
Sets the Shape Actor mesh to Rectangle.

Args:
    shape_actor (AvaShapeActor): 
    size (Vector2D): 
    transform (Transform): 

Returns:
    AvaShapeRectangleDynamicMesh:

<a id="unreal.AvaShapeRectangleDynamicMesh"></a>