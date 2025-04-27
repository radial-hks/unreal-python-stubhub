## AIHelperLibrary Objects

```python
class AIHelperLibrary(BlueprintFunctionLibrary)
```

AIBlueprint Helper Library

**C++ Source:**

- **Module**: AIModule
- **File**: AIBlueprintHelperLibrary.h

<a id="unreal.AIHelperLibrary.unlock_ai_resources_with_animation"></a>

#### unlock_ai_resources_with_animation

```python
@classmethod
def unlock_ai_resources_with_animation(cls, anim_instance: AnimInstance,
                                       unlock_movement: bool,
                                       unlock_ai_logic: bool) -> None
```

X.unlock_ai_resources_with_animation(anim_instance, unlock_movement, unlock_ai_logic) -> None
unlocks indicated AI resources of animated pawn. Will unlock only animation-locked resources

Args:
    anim_instance (AnimInstance): 
    unlock_movement (bool): 
    unlock_ai_logic (bool):

<a id="unreal.AIHelperLibrary.spawn_ai_from_class"></a>

#### spawn_ai_from_class

```python
@classmethod
def spawn_ai_from_class(cls,
                        world_context_object: Object,
                        pawn_class: Class,
                        behavior_tree: BehaviorTree,
                        location: Vector,
                        rotation: Rotator = [0.000000, 0.000000, 0.000000],
                        no_collision_fail: bool = False,
                        owner: Actor = None) -> Pawn
```

X.spawn_ai_from_class(world_context_object, pawn_class, behavior_tree, location, rotation=[0.000000, 0.000000, 0.000000], no_collision_fail=False, owner=None) -> Pawn
Spawns AI agent of a given class. The PawnClass needs to have AIController
set for the function to spawn a controller as well.

Args:
    world_context_object (Object): 
    pawn_class (type(Class)): 
    behavior_tree (BehaviorTree): if set, and the function has successfully spawned and AI controller, this BehaviorTree asset will be assigned to the AI controller, and run.
    location (Vector): 
    rotation (Rotator): 
    no_collision_fail (bool): 
    owner (Actor): lets you spawn the AI in a sublevel rather than in the persistent level (which is the default behavior).

Returns:
    Pawn:

<a id="unreal.AIHelperLibrary.simple_move_to_location"></a>

#### simple_move_to_location

```python
@classmethod
def simple_move_to_location(cls, controller: Controller, goal: Vector) -> None
```

X.simple_move_to_location(controller, goal) -> None
Simple Move to Location

Args:
    controller (Controller): 
    goal (Vector):

<a id="unreal.AIHelperLibrary.simple_move_to_actor"></a>

#### simple_move_to_actor

```python
@classmethod
def simple_move_to_actor(cls, controller: Controller, goal: Actor) -> None
```

X.simple_move_to_actor(controller, goal) -> None
Simple Move to Actor

Args:
    controller (Controller): 
    goal (Actor):

<a id="unreal.AIHelperLibrary.send_ai_message"></a>

#### send_ai_message

```python
@classmethod
def send_ai_message(cls,
                    target: Pawn,
                    message: Name,
                    message_source: Object,
                    success: bool = True) -> None
```

X.send_ai_message(target, message, message_source, success=True) -> None
Send AIMessage

Args:
    target (Pawn): 
    message (Name): 
    message_source (Object): 
    success (bool):

<a id="unreal.AIHelperLibrary.lock_ai_resources_with_animation"></a>

#### lock_ai_resources_with_animation

```python
@classmethod
def lock_ai_resources_with_animation(cls, anim_instance: AnimInstance,
                                     lock_movement: bool,
                                     lock_ai_logic: bool) -> None
```

X.lock_ai_resources_with_animation(anim_instance, lock_movement, lock_ai_logic) -> None
locks indicated AI resources of animated pawn

Args:
    anim_instance (AnimInstance): 
    lock_movement (bool): 
    lock_ai_logic (bool):

<a id="unreal.AIHelperLibrary.is_valid_ai_rotation"></a>

#### is_valid_ai_rotation

```python
@classmethod
def is_valid_ai_rotation(cls, rotation: Rotator) -> bool
```

X.is_valid_ai_rotation(rotation) -> bool
Is Valid AIRotation

Args:
    rotation (Rotator): 

Returns:
    bool:

<a id="unreal.AIHelperLibrary.is_valid_ai_location"></a>

#### is_valid_ai_location

```python
@classmethod
def is_valid_ai_location(cls, location: Vector) -> bool
```

X.is_valid_ai_location(location) -> bool
Is Valid AILocation

Args:
    location (Vector): 

Returns:
    bool:

<a id="unreal.AIHelperLibrary.is_valid_ai_direction"></a>

#### is_valid_ai_direction

```python
@classmethod
def is_valid_ai_direction(cls, direction_vector: Vector) -> bool
```

X.is_valid_ai_direction(direction_vector) -> bool
Is Valid AIDirection

Args:
    direction_vector (Vector): 

Returns:
    bool:

<a id="unreal.AIHelperLibrary.get_next_nav_link_index"></a>

#### get_next_nav_link_index

```python
@classmethod
def get_next_nav_link_index(cls, controller: Controller) -> int
```

X.get_next_nav_link_index(controller) -> int32
Return the path index of the next nav link for the current path of the given controller. Returns INDEX_NONE if no path or no incoming nav link.

Args:
    controller (Controller): 

Returns:
    int32:

<a id="unreal.AIHelperLibrary.get_current_path_points"></a>

#### get_current_path_points

```python
@classmethod
def get_current_path_points(cls, controller: Controller) -> Array[Vector]
```

X.get_current_path_points(controller) -> Array[Vector]
Returns an array of navigation path points given controller is currently using.

Args:
    controller (Controller): 

Returns:
    Array[Vector]:

<a id="unreal.AIHelperLibrary.get_current_path_index"></a>

#### get_current_path_index

```python
@classmethod
def get_current_path_index(cls, controller: Controller) -> int
```

X.get_current_path_index(controller) -> int32
Return the path index the given controller is currently at. Returns INDEX_NONE if no path.

Args:
    controller (Controller): 

Returns:
    int32:

<a id="unreal.AIHelperLibrary.get_current_path"></a>

#### get_current_path

```python
@classmethod
def get_current_path(cls, controller: Controller) -> NavigationPath
```

X.get_current_path(controller) -> NavigationPath
Returns a NEW UOBJECT that is a COPY of navigation path given controller is currently using.
    The result being a copy means you won't be able to influence agent's pathfollowing
    by manipulating received path.
    Please use GetCurrentPathPoints if you only need the array of path points.

Args:
    controller (Controller): 

Returns:
    NavigationPath:

<a id="unreal.AIHelperLibrary.get_blackboard"></a>

#### get_blackboard

```python
@classmethod
def get_blackboard(cls, target: Actor) -> BlackboardComponent
```

X.get_blackboard(target) -> BlackboardComponent
Get Blackboard

Args:
    target (Actor): 

Returns:
    BlackboardComponent:

<a id="unreal.AIHelperLibrary.get_ai_controller"></a>

#### get_ai_controller

```python
@classmethod
def get_ai_controller(cls, controlled_actor: Actor) -> AIController
```

X.get_ai_controller(controlled_actor) -> AIController
The way it works exactly is if the actor passed in is a pawn, then the function retrieves
    pawn's controller cast to AIController. Otherwise the function returns actor cast to AIController.

Args:
    controlled_actor (Actor): 

Returns:
    AIController:

<a id="unreal.DetourCrowdAIController"></a>