## ConstraintsScriptingLibrary Objects

```python
class ConstraintsScriptingLibrary(BlueprintFunctionLibrary)
```

This is a set of helper functions to access various parts of the Sequencer and Control Rig API via Python and Blueprints.

**C++ Source:**

- **Module**: Constraints
- **File**: ConstraintsScripting.h

<a id="unreal.ConstraintsScriptingLibrary.remove_this_constraint"></a>

#### remove_this_constraint

```python
@classmethod
def remove_this_constraint(cls, world: World,
                           tickable_constraint: TickableConstraint) -> bool
```

X.remove_this_constraint(world, tickable_constraint) -> bool
Remove specified constraint

Args:
    world (World): World to remove the constraint
    tickable_constraint (TickableConstraint): Constraint to remove

Returns:
    bool: return If constraint removed correctly

<a id="unreal.ConstraintsScriptingLibrary.remove_constraint"></a>

#### remove_constraint

```python
@classmethod
def remove_constraint(cls, world: World, index: int) -> bool
```

X.remove_constraint(world, index) -> bool
Remove constraint at specified index

Args:
    world (World): World to remove the constraint
    index (int32): Index to remove from

Returns:
    bool: return If constraint removed correctly

<a id="unreal.ConstraintsScriptingLibrary.get_constraints_array"></a>

#### get_constraints_array

```python
@classmethod
def get_constraints_array(cls, world: World) -> Array[TickableConstraint]
```

X.get_constraints_array(world) -> Array[TickableConstraint]
Get a copy of the constraints in the current world

Args:
    world (World): World we are in

Returns:
    Array[TickableConstraint]: Copy of the constraints in the level

<a id="unreal.ConstraintsScriptingLibrary.create_transformable_handle"></a>

#### create_transformable_handle

```python
@classmethod
def create_transformable_handle(
        cls,
        world: World,
        object: Object,
        attachment_name: Name = "None") -> TransformableHandle
```

X.create_transformable_handle(world, object, attachment_name="None") -> TransformableHandle
Create the transformable handle that deals with getting and setting transforms on this object

Args:
    world (World): 
    object (Object): World to create the constraint
    attachment_name (Name): Optional name of the attachment to get the transform. Not that this can represent a scene component's socket name or a control rig control for example.

Returns:
    TransformableHandle: returns the handle for this scene component

<a id="unreal.ConstraintsScriptingLibrary.create_transformable_component_handle"></a>

#### create_transformable_component_handle

```python
@classmethod
def create_transformable_component_handle(
        cls, world: World, scene_component: SceneComponent,
        socket_name: Name) -> TransformableComponentHandle
```

X.create_transformable_component_handle(world, scene_component, socket_name) -> TransformableComponentHandle
Create the transformable handle that deals with getting and setting transforms on this scene component

Args:
    world (World): 
    scene_component (SceneComponent): World to create the constraint
    socket_name (Name): Optional name of the socket to get the transform

Returns:
    TransformableComponentHandle: returns the handle for this scene component

<a id="unreal.ConstraintsScriptingLibrary.create_from_type"></a>

#### create_from_type

```python
@classmethod
def create_from_type(
        cls, world: World,
        type: TransformConstraintType) -> TickableTransformConstraint
```

X.create_from_type(world, type) -> TickableTransformConstraint
Create Constraint based on the specified type.

Args:
    world (World): World to create the constraint
    type (TransformConstraintType): The type of constraint

Returns:
    TickableTransformConstraint: return The constraint object

<a id="unreal.ConstraintsScriptingLibrary.add_constraint"></a>

#### add_constraint

```python
@classmethod
def add_constraint(cls, world: World, parent_handle: TransformableHandle,
                   child_handle: TransformableHandle,
                   constraint: TickableTransformConstraint,
                   maintain_offset: bool) -> bool
```

X.add_constraint(world, parent_handle, child_handle, constraint, maintain_offset) -> bool
Add Constraint

Args:
    world (World): 
    parent_handle (TransformableHandle): 
    child_handle (TransformableHandle): 
    constraint (TickableTransformConstraint): 
    maintain_offset (bool): 

Returns:
    bool:

<a id="unreal.TransformableHandle"></a>