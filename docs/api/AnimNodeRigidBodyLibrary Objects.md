## AnimNodeRigidBodyLibrary Objects

```python
class AnimNodeRigidBodyLibrary(BlueprintFunctionLibrary)
```

Exposes operations to be performed on a rigid body anim node

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_RigidBody_Library.h

<a id="unreal.AnimNodeRigidBodyLibrary.set_override_physics_asset"></a>

#### set_override_physics_asset

```python
@classmethod
def set_override_physics_asset(
        cls, node: RigidBodyAnimNodeReference,
        physics_asset: PhysicsAsset) -> RigidBodyAnimNodeReference
```

X.set_override_physics_asset(node, physics_asset) -> RigidBodyAnimNodeReference
Set the physics asset on the rigid body anim graph node (RBAN).

Args:
    node (RigidBodyAnimNodeReference): 
    physics_asset (PhysicsAsset): 

Returns:
    RigidBodyAnimNodeReference:

<a id="unreal.AnimNodeRigidBodyLibrary.convert_to_rigid_body_anim_node_pure"></a>

#### convert_to_rigid_body_anim_node_pure

```python
@classmethod
def convert_to_rigid_body_anim_node_pure(
        cls,
        node: AnimNodeReference) -> Tuple[RigidBodyAnimNodeReference, bool]
```

X.convert_to_rigid_body_anim_node_pure(node) -> (rigid_body_anim_node=RigidBodyAnimNodeReference, result=bool)
Get a rigid body anim node context from an anim node context (pure)

Args:
    node (AnimNodeReference): 

Returns:
    tuple: 

    rigid_body_anim_node (RigidBodyAnimNodeReference): 

    result (bool):

<a id="unreal.AnimNodeRigidBodyLibrary.convert_to_rigid_body_anim_node"></a>

#### convert_to_rigid_body_anim_node

```python
@classmethod
def convert_to_rigid_body_anim_node(
    cls, node: AnimNodeReference
) -> Tuple[RigidBodyAnimNodeReference, AnimNodeReferenceConversionResult]
```

X.convert_to_rigid_body_anim_node(node) -> (RigidBodyAnimNodeReference, result=AnimNodeReferenceConversionResult)
Get a rigid body anim node context from an anim node context

Args:
    node (AnimNodeReference): 

Returns:
    AnimNodeReferenceConversionResult: 

    result (AnimNodeReferenceConversionResult):

<a id="unreal.BlendSpaceLibrary"></a>