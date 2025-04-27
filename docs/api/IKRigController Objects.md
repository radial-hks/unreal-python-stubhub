## IKRigController Objects

```python
class IKRigController(Object)
```

A singleton (per-asset) class used to make modifications to a UIKRigDefinition asset

All modifications to an IKRigDefinition must go through this controller.

Editors can subscribe to the callbacks on this controller to be notified of changes that require reinitialization
of a running IK Rig processor instance.
The API here is split into public/scripting sections which are accessible from Blueprint/Python and sections that
are only relevant to editors in C++.

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRigEditor
- **File**: IKRigController.h

<a id="unreal.IKRigController.set_solver_enabled"></a>

#### set_solver_enabled

```python
def set_solver_enabled(solver_index: int, is_enabled: bool) -> bool
```

x.set_solver_enabled(solver_index, is_enabled) -> bool
Set enabled/disabled status of the given solver.

Args:
    solver_index (int32): 
    is_enabled (bool): 

Returns:
    bool:

<a id="unreal.IKRigController.set_skeletal_mesh"></a>

#### set_skeletal_mesh

```python
def set_skeletal_mesh(skeletal_mesh: SkeletalMesh) -> bool
```

x.set_skeletal_mesh(skeletal_mesh) -> bool
Sets the preview mesh to use. Loads the hierarchy into the asset's IKRigSkeleton.
Returns true if the mesh was able to be set. False if it was incompatible for any reason.

Args:
    skeletal_mesh (SkeletalMesh): 

Returns:
    bool:

<a id="unreal.IKRigController.set_root_bone"></a>

#### set_root_bone

```python
def set_root_bone(root_bone_name: Name, solver_index: int) -> bool
```

x.set_root_bone(root_bone_name, solver_index) -> bool
Set the root bone on a given solver. (not all solvers support root bones, checks CanSetRootBone() first)

Args:
    root_bone_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.set_retarget_root"></a>

#### set_retarget_root

```python
def set_retarget_root(root_bone_name: Name) -> bool
```

x.set_retarget_root(root_bone_name) -> bool
Set the Root Bone of the retargeting (can only be one).

Args:
    root_bone_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.set_retarget_chain_start_bone"></a>

#### set_retarget_chain_start_bone

```python
def set_retarget_chain_start_bone(chain_name: Name,
                                  start_bone_name: Name) -> bool
```

x.set_retarget_chain_start_bone(chain_name, start_bone_name) -> bool
Set the Start Bone for the given Chain. Returns true if operation was successful.

Args:
    chain_name (Name): 
    start_bone_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.set_retarget_chain_goal"></a>

#### set_retarget_chain_goal

```python
def set_retarget_chain_goal(chain_name: Name, goal_name: Name) -> bool
```

x.set_retarget_chain_goal(chain_name, goal_name) -> bool
Set the Goal for the given Chain. Returns true if operation was successful.

Args:
    chain_name (Name): 
    goal_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.set_retarget_chain_end_bone"></a>

#### set_retarget_chain_end_bone

```python
def set_retarget_chain_end_bone(chain_name: Name, end_bone_name: Name) -> bool
```

x.set_retarget_chain_end_bone(chain_name, end_bone_name) -> bool
Set the End Bone for the given Chain. Returns true if operation was successful.

Args:
    chain_name (Name): 
    end_bone_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.set_goal_bone"></a>

#### set_goal_bone

```python
def set_goal_bone(goal_name: Name, new_bone_name: Name) -> bool
```

x.set_goal_bone(goal_name, new_bone_name) -> bool
The the Bone that the given Goal should be parented to / associated with.

Args:
    goal_name (Name): 
    new_bone_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.set_end_bone"></a>

#### set_end_bone

```python
def set_end_bone(end_bone_name: Name, solver_index: int) -> bool
```

x.set_end_bone(end_bone_name, solver_index) -> bool
Set the end bone on a given solver. (not all solvers require extra end bones, checks CanSetEndBone() first)

Args:
    end_bone_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.set_bone_excluded"></a>

#### set_bone_excluded

```python
def set_bone_excluded(bone_name: Name, exclude: bool) -> bool
```

x.set_bone_excluded(bone_name, exclude) -> bool
Include/exclude a bone from all the solvers. All bones are included by default.

Args:
    bone_name (Name): 
    exclude (bool): 

Returns:
    bool:

<a id="unreal.IKRigController.rename_retarget_chain"></a>

#### rename_retarget_chain

```python
def rename_retarget_chain(chain_name: Name, new_chain_name: Name) -> Name
```

x.rename_retarget_chain(chain_name, new_chain_name) -> Name
Renamed the given Chain. Returns the new name (same as old if unsuccessful).

Args:
    chain_name (Name): 
    new_chain_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.rename_goal"></a>

#### rename_goal

```python
def rename_goal(old_name: Name, potential_new_name: Name) -> Name
```

x.rename_goal(old_name, potential_new_name) -> Name
Rename a Goal. Returns new name, which may be different after being sanitized. Returns NAME_None if this fails.

Args:
    old_name (Name): 
    potential_new_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.remove_solver"></a>

#### remove_solver

```python
def remove_solver(solver_index: int) -> bool
```

x.remove_solver(solver_index) -> bool
Remove the solver at the given stack index.

Args:
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.remove_retarget_chain"></a>

#### remove_retarget_chain

```python
def remove_retarget_chain(chain_name: Name) -> bool
```

x.remove_retarget_chain(chain_name) -> bool
Remove a Chain with the given name. Returns true if a Chain was removed.

Args:
    chain_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.remove_goal"></a>

#### remove_goal

```python
def remove_goal(goal_name: Name) -> bool
```

x.remove_goal(goal_name) -> bool
Remove the Goal by name.

Args:
    goal_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.remove_bone_setting"></a>

#### remove_bone_setting

```python
def remove_bone_setting(bone_name: Name, solver_index: int) -> bool
```

x.remove_bone_setting(bone_name, solver_index) -> bool
Remove settings for the given Bone/Solver. Does nothing if Bone doesn't have setting in this Solver.

Args:
    bone_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.move_solver_in_stack"></a>

#### move_solver_in_stack

```python
def move_solver_in_stack(solver_to_move_index: int,
                         target_solver_index: int) -> bool
```

x.move_solver_in_stack(solver_to_move_index, target_solver_index) -> bool
Move the solver at the given index to the target index.

Args:
    solver_to_move_index (int32): 
    target_solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.is_skeletal_mesh_compatible"></a>

#### is_skeletal_mesh_compatible

```python
def is_skeletal_mesh_compatible(skeletal_mesh_to_check: SkeletalMesh) -> bool
```

x.is_skeletal_mesh_compatible(skeletal_mesh_to_check) -> bool
Returns true if the provided skeletal mesh could be used with this IK Rig.

Args:
    skeletal_mesh_to_check (SkeletalMesh): 

Returns:
    bool:

<a id="unreal.IKRigController.is_goal_connected_to_solver"></a>

#### is_goal_connected_to_solver

```python
def is_goal_connected_to_solver(goal_name: Name, solver_index: int) -> bool
```

x.is_goal_connected_to_solver(goal_name, solver_index) -> bool
Returns true if the given Goal is connected to the given Solver. False otherwise.

Args:
    goal_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.is_goal_connected_to_any_solver"></a>

#### is_goal_connected_to_any_solver

```python
def is_goal_connected_to_any_solver(goal_name: Name) -> bool
```

x.is_goal_connected_to_any_solver(goal_name) -> bool
Returns true if the given Goal is connected to ANY solver. False otherwise.

Args:
    goal_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.get_solver_enabled"></a>

#### get_solver_enabled

```python
def get_solver_enabled(solver_index: int) -> bool
```

x.get_solver_enabled(solver_index) -> bool
Get enabled status of the given solver.

Args:
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.get_solver_at_index"></a>

#### get_solver_at_index

```python
def get_solver_at_index(index: int) -> IKRigSolver
```

x.get_solver_at_index(index) -> IKRigSolver
Get access to the given solver.

Args:
    index (int32): 

Returns:
    IKRigSolver:

<a id="unreal.IKRigController.get_skeletal_mesh"></a>

#### get_skeletal_mesh

```python
def get_skeletal_mesh() -> SkeletalMesh
```

x.get_skeletal_mesh() -> SkeletalMesh
Get the skeletal mesh this asset is initialized with

Returns:
    SkeletalMesh:

<a id="unreal.IKRigController.get_root_bone"></a>

#### get_root_bone

```python
def get_root_bone(solver_index: int) -> Name
```

x.get_root_bone(solver_index) -> Name
Get the name of the root bone on a given solver. (not all solvers support root bones, checks CanSetRootBone() first)

Args:
    solver_index (int32): 

Returns:
    Name:

<a id="unreal.IKRigController.get_retarget_root"></a>

#### get_retarget_root

```python
def get_retarget_root() -> Name
```

x.get_retarget_root() -> Name
Get the name of the Root Bone of the retargeting (can only be one).

Returns:
    Name:

<a id="unreal.IKRigController.get_retarget_chain_start_bone"></a>

#### get_retarget_chain_start_bone

```python
def get_retarget_chain_start_bone(chain_name: Name) -> Name
```

x.get_retarget_chain_start_bone(chain_name) -> Name
Get the End Bone name for the given Chain.

Args:
    chain_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.get_retarget_chains"></a>

#### get_retarget_chains

```python
def get_retarget_chains() -> Array[BoneChain]
```

x.get_retarget_chains() -> Array[BoneChain]
Get read-only access to the list of Chains.

Returns:
    Array[BoneChain]:

<a id="unreal.IKRigController.get_retarget_chain_goal"></a>

#### get_retarget_chain_goal

```python
def get_retarget_chain_goal(chain_name: Name) -> Name
```

x.get_retarget_chain_goal(chain_name) -> Name
Get the Goal name for the given Chain.

Args:
    chain_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.get_retarget_chain_end_bone"></a>

#### get_retarget_chain_end_bone

```python
def get_retarget_chain_end_bone(chain_name: Name) -> Name
```

x.get_retarget_chain_end_bone(chain_name) -> Name
Get the Start Bone name for the given Chain.

Args:
    chain_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.get_ref_pose_transform_of_bone"></a>

#### get_ref_pose_transform_of_bone

```python
def get_ref_pose_transform_of_bone(bone_name: Name) -> Transform
```

x.get_ref_pose_transform_of_bone(bone_name) -> Transform
Get the global-space retarget pose transform of the given Bone.

Args:
    bone_name (Name): 

Returns:
    Transform:

<a id="unreal.IKRigController.get_num_solvers"></a>

#### get_num_solvers

```python
def get_num_solvers() -> int
```

x.get_num_solvers() -> int32
Get the number of solvers in the stack.

Returns:
    int32:

<a id="unreal.IKRigController.get_index_of_solver"></a>

#### get_index_of_solver

```python
def get_index_of_solver(solver: IKRigSolver) -> int
```

x.get_index_of_solver(solver) -> int32
Get access to the given solver.

Args:
    solver (IKRigSolver): 

Returns:
    int32:

<a id="unreal.IKRigController.get_goal_settings_for_solver"></a>

#### get_goal_settings_for_solver

```python
def get_goal_settings_for_solver(goal_name: Name, solver_index: int) -> Object
```

x.get_goal_settings_for_solver(goal_name, solver_index) -> Object
Get the UObject for the settings associated with the given Goal in the given Solver.
Solvers can define their own per-Goal settings depending on their needs. These are termed "Effectors".

Args:
    goal_name (Name): 
    solver_index (int32): 

Returns:
    Object:

<a id="unreal.IKRigController.get_goal_name_for_bone"></a>

#### get_goal_name_for_bone

```python
def get_goal_name_for_bone(bone_name: Name) -> Name
```

x.get_goal_name_for_bone(bone_name) -> Name
Get the Goal associated with the given Bone (may be NAME_None)

Args:
    bone_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.get_goal"></a>

#### get_goal

```python
def get_goal(goal_name: Name) -> IKRigEffectorGoal
```

x.get_goal(goal_name) -> IKRigEffectorGoal
Get read-write access to the Goal with the given name.

Args:
    goal_name (Name): 

Returns:
    IKRigEffectorGoal:

<a id="unreal.IKRigController.get_end_bone"></a>

#### get_end_bone

```python
def get_end_bone(solver_index: int) -> Name
```

x.get_end_bone(solver_index) -> Name
Get the name of the end bone on a given solver. (not all solvers require extra end bones, checks CanSetEndBone() first)

Args:
    solver_index (int32): 

Returns:
    Name:

<a id="unreal.IKRigController.get_controller"></a>

#### get_controller

```python
@classmethod
def get_controller(cls, ik_rig_definition: IKRigDefinition) -> IKRigController
```

X.get_controller(ik_rig_definition) -> IKRigController
Use this to get the controller for the given IKRig

Args:
    ik_rig_definition (IKRigDefinition): 

Returns:
    IKRigController:

<a id="unreal.IKRigController.get_bone_settings"></a>

#### get_bone_settings

```python
def get_bone_settings(bone_name: Name, solver_index: int) -> Object
```

x.get_bone_settings(bone_name, solver_index) -> Object
Get the generic (Solver-specific) Bone settings UObject for this Bone in the given Solver.

Args:
    bone_name (Name): 
    solver_index (int32): 

Returns:
    Object:

<a id="unreal.IKRigController.get_bone_for_goal"></a>

#### get_bone_for_goal

```python
def get_bone_for_goal(goal_name: Name) -> Name
```

x.get_bone_for_goal(goal_name) -> Name
The the Bone associated with the given Goal.

Args:
    goal_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.get_bone_excluded"></a>

#### get_bone_excluded

```python
def get_bone_excluded(bone_name: Name) -> bool
```

x.get_bone_excluded(bone_name) -> bool
Returns true if the given Bone is excluded, false otherwise.

Args:
    bone_name (Name): 

Returns:
    bool:

<a id="unreal.IKRigController.get_all_goals"></a>

#### get_all_goals

```python
def get_all_goals() -> Array[IKRigEffectorGoal]
```

x.get_all_goals() -> Array[IKRigEffectorGoal]
Get access to the list of Goals.

Returns:
    Array[IKRigEffectorGoal]:

<a id="unreal.IKRigController.disconnect_goal_from_solver"></a>

#### disconnect_goal_from_solver

```python
def disconnect_goal_from_solver(goal_to_remove: Name,
                                solver_index: int) -> bool
```

x.disconnect_goal_from_solver(goal_to_remove, solver_index) -> bool
Disconnect the given Goal from the given Solver. This removes the Effector that associates the Goal with the Solver.

Args:
    goal_to_remove (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.connect_goal_to_solver"></a>

#### connect_goal_to_solver

```python
def connect_goal_to_solver(goal_name: Name, solver_index: int) -> bool
```

x.connect_goal_to_solver(goal_name, solver_index) -> bool
Connect the given Goal to the given Solver. This creates an "Effector" with settings specific to this Solver.

Args:
    goal_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigController.apply_auto_generated_retarget_definition"></a>

#### apply_auto_generated_retarget_definition

```python
def apply_auto_generated_retarget_definition() -> bool
```

x.apply_auto_generated_retarget_definition() -> bool
Analyse the skeleton to see if it matches a known template and automatically generates all retarget chains and sets the retarget root
Returns true if a matching skeletal template was found and the retarget definition for it was applied.

Returns:
    bool:

<a id="unreal.IKRigController.apply_auto_fbik"></a>

#### apply_auto_fbik

```python
def apply_auto_fbik() -> bool
```

x.apply_auto_fbik() -> bool
Analyse the skeleton to see if it matches a known template and automatically generates a full body IK setup
Returns true if a matching skeletal template was found and the FBIK setup for it was applied.

Returns:
    bool:

<a id="unreal.IKRigController.add_solver"></a>

#### add_solver

```python
def add_solver(solver_class: Class) -> int
```

x.add_solver(solver_class) -> int32
Add a new solver of the given type to the bottom of the stack. Returns the stack index.

Args:
    solver_class (type(Class)): 

Returns:
    int32:

<a id="unreal.IKRigController.add_retarget_chain"></a>

#### add_retarget_chain

```python
def add_retarget_chain(chain_name: Name, start_bone_name: Name,
                       end_bone_name: Name, goal_name: Name) -> Name
```

x.add_retarget_chain(chain_name, start_bone_name, end_bone_name, goal_name) -> Name
Add a new chain with the given Chain and Bone names. Returns newly created chain name (uniquified).
Note: only the ChainName is required here, all else can be set later.

Args:
    chain_name (Name): 
    start_bone_name (Name): 
    end_bone_name (Name): 
    goal_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.add_new_goal"></a>

#### add_new_goal

```python
def add_new_goal(goal_name: Name, bone_name: Name) -> Name
```

x.add_new_goal(goal_name, bone_name) -> Name
Add a new Goal associated with the given Bone. GoalName must be unique. Bones can have multiple Goals (rare).

Args:
    goal_name (Name): 
    bone_name (Name): 

Returns:
    Name:

<a id="unreal.IKRigController.add_bone_setting"></a>

#### add_bone_setting

```python
def add_bone_setting(bone_name: Name, solver_index: int) -> bool
```

x.add_bone_setting(bone_name, solver_index) -> bool
Add settings to the given Bone/Solver. Does nothing if Bone already has settings in this Solver.

Args:
    bone_name (Name): 
    solver_index (int32): 

Returns:
    bool:

<a id="unreal.IKRigDefinitionFactory"></a>