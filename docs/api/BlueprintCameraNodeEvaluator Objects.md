## BlueprintCameraNodeEvaluator Objects

```python
class BlueprintCameraNodeEvaluator(Object)
```

The base class for Blueprint camera node evaluators.

**C++ Source:**

- **Plugin**: GameplayCameras
- **Module**: GameplayCameras
- **File**: BlueprintCameraNode.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_pose`` (BlueprintCameraPose):  [Read-Write] The input/output camera pose for this frame.
- ``evaluation_context_owner`` (Object):  [Read-Write] The owner object of this camera node's evaluation context.
- ``is_first_frame`` (bool):  [Read-Write] Whether this is the first frame of this camera node's lifetime.
- ``variable_table`` (BlueprintCameraVariableTable):  [Read-Write] The input/output camera variable table for this frame.

<a id="unreal.BlueprintCameraNodeEvaluator.is_first_frame"></a>

#### is_first_frame

```python
@property
def is_first_frame() -> bool
```

(bool):  [Read-Only] Whether this is the first frame of this camera node's lifetime.

<a id="unreal.BlueprintCameraNodeEvaluator.evaluation_context_owner"></a>

#### evaluation_context_owner

```python
@property
def evaluation_context_owner() -> Object
```

(Object):  [Read-Only] The owner object of this camera node's evaluation context.

<a id="unreal.BlueprintCameraNodeEvaluator.camera_pose"></a>

#### camera_pose

```python
@property
def camera_pose() -> BlueprintCameraPose
```

(BlueprintCameraPose):  [Read-Write] The input/output camera pose for this frame.

<a id="unreal.BlueprintCameraNodeEvaluator.camera_pose"></a>

#### camera_pose

```python
@camera_pose.setter
def camera_pose(value: BlueprintCameraPose) -> None
```

<a id="unreal.BlueprintCameraNodeEvaluator.variable_table"></a>

#### variable_table

```python
@property
def variable_table() -> BlueprintCameraVariableTable
```

(BlueprintCameraVariableTable):  [Read-Write] The input/output camera variable table for this frame.

<a id="unreal.BlueprintCameraNodeEvaluator.variable_table"></a>

#### variable_table

```python
@variable_table.setter
def variable_table(value: BlueprintCameraVariableTable) -> None
```

<a id="unreal.BlueprintCameraNodeEvaluator.tick_camera_node"></a>

#### tick_camera_node

```python
def tick_camera_node(delta_time: float) -> None
```

x.tick_camera_node(delta_time) -> None
The main execution callback for the camera node. Call SetCameraPose to affect the result.

Args:
    delta_time (float):

<a id="unreal.BlueprintCameraNodeEvaluator.find_evaluation_context_owner_actor"></a>

#### find_evaluation_context_owner_actor

```python
def find_evaluation_context_owner_actor(actor_class: Class) -> Actor
```

x.find_evaluation_context_owner_actor(actor_class) -> Actor
A utility function that tries to find if an actor owns the evaluation context.
Handles the situation where the evaluation context is an actor component (like a
UGameplayCameraComponent) or an actor itself.

Args:
    actor_class (type(Class)): 

Returns:
    Actor:

<a id="unreal.OpenColorIOConfigurationFactoryNew"></a>