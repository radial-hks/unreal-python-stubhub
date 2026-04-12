## PythonPhysicsAssetLib Objects

```python
class PythonPhysicsAssetLib(BlueprintFunctionLibrary)
```

Python Physics Asset Lib

**C++ Source:**

- **Plugin**: TAPython
- **Module**: TAPython
- **File**: PythonPhysicsAssetLib.h

<a id="unreal.PythonPhysicsAssetLib.update_profile_instance"></a>

#### update\_profile\_instance

```python
@classmethod
def update_profile_instance(cls, physics_asset: PhysicsAsset,
                            constraint_index: int) -> None
```

X.update_profile_instance(physics_asset, constraint_index) -> None
Update the Profile according to the specified Constraint
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    constraint_index (int32): The index of constraint

<a id="unreal.PythonPhysicsAssetLib.set_body_size"></a>

#### set\_body\_size

```python
@classmethod
def set_body_size(cls, physics_asset: PhysicsAsset, body_index: int,
                  size: Vector) -> bool
```

X.set_body_size(physics_asset, body_index, size) -> bool
Set the Size value of the box body
prarm: BodyIndex                       The index of body
prarm: Size                            The new size value for the box body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    size (Vector): 

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.set_body_rotation"></a>

#### set\_body\_rotation

```python
@classmethod
def set_body_rotation(cls, physics_asset: PhysicsAsset, body_index: int,
                      rotation: Rotator) -> bool
```

X.set_body_rotation(physics_asset, body_index, rotation) -> bool
Set the rotation value of the specified body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    rotation (Rotator): The new Rotation value

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.set_body_radius"></a>

#### set\_body\_radius

```python
@classmethod
def set_body_radius(cls, physics_asset: PhysicsAsset, body_index: int,
                    radius: float) -> bool
```

X.set_body_radius(physics_asset, body_index, radius) -> bool
Set the Radius value of the body
prarm: BodyIndex                       The index of body
prarm: Radius                          The new radius
note: Support Sphere and Capsule body.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    radius (float): 

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.set_body_length"></a>

#### set\_body\_length

```python
@classmethod
def set_body_length(cls, physics_asset: PhysicsAsset, body_index: int,
                    length: float) -> bool
```

X.set_body_length(physics_asset, body_index, length) -> bool
Get the rotation value of the first body
prarm: BodyIndex                       The index of body
prarm: Length                          The new Length value for the capsule body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    length (float): 

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.set_body_center"></a>

#### set\_body\_center

```python
@classmethod
def set_body_center(cls, physics_asset: PhysicsAsset, body_index: int,
                    center: Vector) -> bool
```

X.set_body_center(physics_asset, body_index, center) -> bool
Set the center value of the specified body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    center (Vector): The new Center value

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.select_shape_by_names"></a>

#### select\_shape\_by\_names

```python
@classmethod
def select_shape_by_names(cls, physics_asset: PhysicsAsset,
                          names: Array[Name]) -> bool
```

X.select_shape_by_names(physics_asset, names) -> bool
Select the Shapes by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    names (Array[Name]): The shapes names.

Returns:
    bool: True if any succeed

<a id="unreal.PythonPhysicsAssetLib.select_shape_by_name"></a>

#### select\_shape\_by\_name

```python
@classmethod
def select_shape_by_name(cls, physics_asset: PhysicsAsset,
                         name_in: Name) -> bool
```

X.select_shape_by_name(physics_asset, name_in) -> bool
Select the Shape by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    name_in (Name): The name of shape.

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.select_constraint_by_names"></a>

#### select\_constraint\_by\_names

```python
@classmethod
def select_constraint_by_names(cls, physics_asset: PhysicsAsset,
                               names: Array[Name]) -> bool
```

X.select_constraint_by_names(physics_asset, names) -> bool
Select the constraints by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    names (Array[Name]): The constraints names.

Returns:
    bool: True if any succeed.

<a id="unreal.PythonPhysicsAssetLib.select_constraint_by_name"></a>

#### select\_constraint\_by\_name

```python
@classmethod
def select_constraint_by_name(cls, physics_asset: PhysicsAsset,
                              name_in: Name) -> bool
```

X.select_constraint_by_name(physics_asset, name_in) -> bool
Select the constraint by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    name_in (Name): The name of constraint.

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.select_body_by_names"></a>

#### select\_body\_by\_names

```python
@classmethod
def select_body_by_names(cls, physics_asset: PhysicsAsset,
                         names: Array[Name]) -> bool
```

X.select_body_by_names(physics_asset, names) -> bool
Select the Bodies by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    names (Array[Name]): The bodies names.

Returns:
    bool: True if any succeed

<a id="unreal.PythonPhysicsAssetLib.select_body_by_name"></a>

#### select\_body\_by\_name

```python
@classmethod
def select_body_by_name(cls, physics_asset: PhysicsAsset,
                        name_in: Name) -> bool
```

X.select_body_by_name(physics_asset, name_in) -> bool
Select the Body by name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    name_in (Name): 

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.scale_body"></a>

#### scale\_body

```python
@classmethod
def scale_body(cls, physics_asset: PhysicsAsset, body_index: int,
               scale: float) -> bool
```

X.scale_body(physics_asset, body_index, scale) -> bool
Scale the specified body
prarm: BodyIndex                       The index of body
prarm: Scale                           The scale value for body
Suppport: Sphere, Capsule and Box bodies
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 
    scale (float): 

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.rotate_selected_constraint"></a>

#### rotate\_selected\_constraint

```python
@classmethod
def rotate_selected_constraint(cls, physics_asset: PhysicsAsset,
                               rotation: Rotator) -> bool
```

X.rotate_selected_constraint(physics_asset, rotation) -> bool
Set the rotation of the selected constraint in Physics Asset Editor
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): 
    rotation (Rotator): The rotation value

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.rotate_selected_body"></a>

#### rotate\_selected\_body

```python
@classmethod
def rotate_selected_body(cls, physics_asset: PhysicsAsset,
                         rotation: Rotator) -> bool
```

X.rotate_selected_body(physics_asset, rotation) -> bool
Set the rotation of the selected body in Physics Asset Editor
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): 
    rotation (Rotator): The rotation value

Returns:
    bool: True if succeed

<a id="unreal.PythonPhysicsAssetLib.reset_constraint_properties"></a>

#### reset\_constraint\_properties

```python
@classmethod
def reset_constraint_properties(cls, physics_asset: PhysicsAsset,
                                constraint_index: int) -> None
```

X.reset_constraint_properties(physics_asset, constraint_index) -> None
Reset the specified Constraint's values
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    constraint_index (int32): The index of constraint

<a id="unreal.PythonPhysicsAssetLib.log_selected"></a>

#### log\_selected

```python
@classmethod
def log_selected(cls, physics_asset: PhysicsAsset) -> None
```

X.log_selected(physics_asset) -> None
Log Selected

Args:
    physics_asset (PhysicsAsset):

<a id="unreal.PythonPhysicsAssetLib.get_skeleton_hierarchy"></a>

#### get\_skeleton\_hierarchy

```python
@classmethod
def get_skeleton_hierarchy(
        cls, physics_asset: PhysicsAsset) -> Tuple[Array[Name], Array[int]]
```

X.get_skeleton_hierarchy(physics_asset) -> (bone_names=Array[Name], parents_indexes=Array[int32])
Get the bones hierarchy
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset

Returns:
    tuple: 

    bone_names (Array[Name]): 

    parents_indexes (Array[int32]):

<a id="unreal.PythonPhysicsAssetLib.get_selected_item_names"></a>

#### get\_selected\_item\_names

```python
@classmethod
def get_selected_item_names(cls, physics_asset: PhysicsAsset) -> Array[Name]
```

X.get_selected_item_names(physics_asset) -> Array[Name]
Get all the selected items name in PhysicsAsset editor window.
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The name of body.

Returns:
    Array[Name]: True if succeed

<a id="unreal.PythonPhysicsAssetLib.get_selected_bodies_indexes"></a>

#### get\_selected\_bodies\_indexes

```python
@classmethod
def get_selected_bodies_indexes(cls,
                                physics_asset: PhysicsAsset) -> Array[int]
```

X.get_selected_bodies_indexes(physics_asset) -> Array[int32]
Get the indexes of the selected bodies in Physics Asset Editor
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset

Returns:
    Array[int32]: Indexes values in list

<a id="unreal.PythonPhysicsAssetLib.get_selected"></a>

#### get\_selected

```python
@classmethod
def get_selected(cls, physics_asset: PhysicsAsset) -> bool
```

X.get_selected(physics_asset) -> bool
Get Selected

Args:
    physics_asset (PhysicsAsset): 

Returns:
    bool:

<a id="unreal.PythonPhysicsAssetLib.get_physics_asset_from_top_window"></a>

#### get\_physics\_asset\_from\_top\_window

```python
@classmethod
def get_physics_asset_from_top_window(cls) -> PhysicsAsset
```

X.get_physics_asset_from_top_window() -> PhysicsAsset
Get the PhysicsAsset from the top opened editor window.
note: Will return null if the PhysicsAsset Editor window is docked.
note: added in v1.0.10

Returns:
    PhysicsAsset: The opened PhysicsAsset.

<a id="unreal.PythonPhysicsAssetLib.get_edited_physics_assets"></a>

#### get\_edited\_physics\_assets

```python
@classmethod
def get_edited_physics_assets(cls) -> Array[PhysicsAsset]
```

X.get_edited_physics_assets() -> Array[PhysicsAsset]
Get all PhysicsAsset currently being tracked with open editors
note: added in v1.0.10

Returns:
    Array[PhysicsAsset]: The opened PhysicsAssets.

<a id="unreal.PythonPhysicsAssetLib.get_constraints_names"></a>

#### get\_constraints\_names

```python
@classmethod
def get_constraints_names(cls, physics_asset: PhysicsAsset) -> Array[Name]
```

X.get_constraints_names(physics_asset) -> Array[Name]
Get all the constraint's display names of PhysicsAsset
note: Display name format: "[ {parent_bone_name} -> {child_bone_name} ] Constraint"
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset

Returns:
    Array[Name]: 

    constraints_names (Array[Name]):

<a id="unreal.PythonPhysicsAssetLib.get_constraint_name"></a>

#### get\_constraint\_name

```python
@classmethod
def get_constraint_name(cls, physics_asset: PhysicsAsset,
                        constraint_index: int) -> Name
```

X.get_constraint_name(physics_asset, constraint_index) -> Name
Get the Constraint's name by Constraint Index
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    constraint_index (int32): The index of constraint

Returns:
    Name: Name of the Constraint

<a id="unreal.PythonPhysicsAssetLib.get_constraint_instance_accessor"></a>

#### get\_constraint\_instance\_accessor

```python
@classmethod
def get_constraint_instance_accessor(
        cls, physics_asset: PhysicsAsset,
        constraint_index: int) -> ConstraintInstanceAccessor
```

X.get_constraint_instance_accessor(physics_asset, constraint_index) -> ConstraintInstanceAccessor
Get the ConstraintInstanceAccessor from PhysicsAsset
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    constraint_index (int32): The index of constraint

Returns:
    ConstraintInstanceAccessor: The ConstraintInstanceAccessor

<a id="unreal.PythonPhysicsAssetLib.get_bone_index_from_body"></a>

#### get\_bone\_index\_from\_body

```python
@classmethod
def get_bone_index_from_body(cls, physics_asset: PhysicsAsset,
                             body_index: int) -> int
```

X.get_bone_index_from_body(physics_asset, body_index) -> int32
Get the first Body under the specified bone
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    int32: The bone's index

<a id="unreal.PythonPhysicsAssetLib.get_bone_indexes_of_constraint"></a>

#### get\_bone\_indexes\_of\_constraint

```python
@classmethod
def get_bone_indexes_of_constraint(cls, physics_asset: PhysicsAsset,
                                   constraint_index: int) -> Tuple[int, int]
```

X.get_bone_indexes_of_constraint(physics_asset, constraint_index) -> (parent_bone_index=int32, child_bone_index=int32)
Get the parent and child bone's indexes of the specified Constraint
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    constraint_index (int32): The index of Constraint

Returns:
    tuple: 

    parent_bone_index (int32): 

    child_bone_index (int32):

<a id="unreal.PythonPhysicsAssetLib.get_body_size"></a>

#### get\_body\_size

```python
@classmethod
def get_body_size(cls, physics_asset: PhysicsAsset,
                  body_index: int) -> Optional[Vector]
```

X.get_body_size(physics_asset, body_index) -> Vector or None
Get the Size value of the box body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    Vector or None: None or Size value of the Box Body

    size (Vector):

<a id="unreal.PythonPhysicsAssetLib.get_body_rotation"></a>

#### get\_body\_rotation

```python
@classmethod
def get_body_rotation(cls, physics_asset: PhysicsAsset,
                      body_index: int) -> Optional[Rotator]
```

X.get_body_rotation(physics_asset, body_index) -> Rotator or None
Get the rotation value of the first body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    Rotator or None: None or Rotation value

    result (Rotator):

<a id="unreal.PythonPhysicsAssetLib.get_body_radius"></a>

#### get\_body\_radius

```python
@classmethod
def get_body_radius(cls, physics_asset: PhysicsAsset,
                    body_index: int) -> Optional[float]
```

X.get_body_radius(physics_asset, body_index) -> float or None
Get the Radius value of the body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    float or None: None or Radius values

    radius (float):

<a id="unreal.PythonPhysicsAssetLib.get_body_length"></a>

#### get\_body\_length

```python
@classmethod
def get_body_length(cls, physics_asset: PhysicsAsset,
                    body_index: int) -> Optional[float]
```

X.get_body_length(physics_asset, body_index) -> float or None
Get the rotation value of the first body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    float or None: None or Length of the capsule body

    length (float):

<a id="unreal.PythonPhysicsAssetLib.get_body_center"></a>

#### get\_body\_center

```python
@classmethod
def get_body_center(cls, physics_asset: PhysicsAsset,
                    body_index: int) -> Optional[Vector]
```

X.get_body_center(physics_asset, body_index) -> Vector or None
Get the center value of the specified body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    Vector or None: None or Center value

    result (Vector):

<a id="unreal.PythonPhysicsAssetLib.get_bodies_rotations"></a>

#### get\_bodies\_rotations

```python
@classmethod
def get_bodies_rotations(cls, physics_asset: PhysicsAsset,
                         body_index: int) -> Optional[Array[Rotator]]
```

X.get_bodies_rotations(physics_asset, body_index) -> Array[Rotator] or None
Get the rotation value of the first body
prarm: BodyIndex                       The index of body
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    body_index (int32): 

Returns:
    Array[Rotator] or None: None or Rotation values

    result (Array[Rotator]):

<a id="unreal.PythonPhysicsAssetLib.get_bodies_hierarchy"></a>

#### get\_bodies\_hierarchy

```python
@classmethod
def get_bodies_hierarchy(
        cls, physics_asset: PhysicsAsset) -> Tuple[Array[Name], Array[int]]
```

X.get_bodies_hierarchy(physics_asset) -> (bodies_names=Array[Name], parent_bones_indexes=Array[int32])
Get all the bodies names and their parent bone's index
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset

Returns:
    tuple: 

    bodies_names (Array[Name]): 

    parent_bones_indexes (Array[int32]):

<a id="unreal.PythonPhysicsAssetLib.get_bodies_from_bone"></a>

#### get\_bodies\_from\_bone

```python
@classmethod
def get_bodies_from_bone(cls, physics_asset: PhysicsAsset,
                         bone_index: int) -> Array[int]
```

X.get_bodies_from_bone(physics_asset, bone_index) -> Array[int32]
Get the Bodies under the specified bone
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    bone_index (int32): The index of Bone

Returns:
    Array[int32]: The bodies's indexes in array

<a id="unreal.PythonPhysicsAssetLib.break_constraint_accessor"></a>

#### break\_constraint\_accessor

```python
@classmethod
def break_constraint_accessor(
        cls,
        accessor: ConstraintInstanceAccessor) -> Optional[Tuple[Object, int]]
```

X.break_constraint_accessor(accessor) -> (owner=Object, constraint_index=int32) or None
Get the Owner and Constraint Index from ConstraintInstanceAccessor
note: added in v1.0.10
note: need UE5

Args:
    accessor (ConstraintInstanceAccessor): The ConstraintInstanceAccessor instance

Returns:
    tuple or None: None or tuple(Owner, ConstraintIndex)

    owner (Object): 

    constraint_index (int32):

<a id="unreal.PythonPhysicsAssetLib.add_constraints"></a>

#### add\_constraints

```python
@classmethod
def add_constraints(cls, physics_asset: PhysicsAsset, parent_body_index: int,
                    child_bodies_indexes: Array[int]) -> Array[Name]
```

X.add_constraints(physics_asset, parent_body_index, child_bodies_indexes) -> Array[Name]
Add constraint to specified bodies
note: added in v1.0.10

Args:
    physics_asset (PhysicsAsset): The PhysicsAsset
    parent_body_index (int32): The parent body index of the new constraint
    child_bodies_indexes (Array[int32]): The child bodies indexes of the new constraint, one constraint for one body

Returns:
    Array[Name]: Added constraint names

<a id="unreal.PythonRBFTarget"></a>