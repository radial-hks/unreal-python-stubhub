## VariantManagerLibrary Objects

```python
class VariantManagerLibrary(BlueprintFunctionLibrary)
```

Library of functions that can be used by the Python API to trigger VariantManager operations

**C++ Source:**

- **Plugin**: VariantManager
- **Module**: VariantManager
- **File**: VariantManagerBlueprintLibrary.h

<a id="unreal.VariantManagerLibrary.set_value_vector4"></a>

#### set_value_vector4

```python
@classmethod
def set_value_vector4(cls, property_: PropertyValue, value: Vector4) -> None
```

X.set_value_vector4(property_, value) -> None
Set Value Vector 4

Args:
    property_ (PropertyValue): 
    value (Vector4):

<a id="unreal.VariantManagerLibrary.set_value_vector2d"></a>

#### set_value_vector2d

```python
@classmethod
def set_value_vector2d(cls, property_: PropertyValue, value: Vector2D) -> None
```

X.set_value_vector2d(property_, value) -> None
Set Value Vector 2D

Args:
    property_ (PropertyValue): 
    value (Vector2D):

<a id="unreal.VariantManagerLibrary.set_value_vector"></a>

#### set_value_vector

```python
@classmethod
def set_value_vector(cls, property_: PropertyValue, value: Vector) -> None
```

X.set_value_vector(property_, value) -> None
Set Value Vector

Args:
    property_ (PropertyValue): 
    value (Vector):

<a id="unreal.VariantManagerLibrary.set_value_string"></a>

#### set_value_string

```python
@classmethod
def set_value_string(cls, property_: PropertyValue, value: str) -> None
```

X.set_value_string(property_, value) -> None
Set Value String

Args:
    property_ (PropertyValue): 
    value (str):

<a id="unreal.VariantManagerLibrary.set_value_rotator"></a>

#### set_value_rotator

```python
@classmethod
def set_value_rotator(cls, property_: PropertyValue, value: Rotator) -> None
```

X.set_value_rotator(property_, value) -> None
Set Value Rotator

Args:
    property_ (PropertyValue): 
    value (Rotator):

<a id="unreal.VariantManagerLibrary.set_value_quat"></a>

#### set_value_quat

```python
@classmethod
def set_value_quat(cls, property_: PropertyValue, value: Quat) -> None
```

X.set_value_quat(property_, value) -> None
Set Value Quat

Args:
    property_ (PropertyValue): 
    value (Quat):

<a id="unreal.VariantManagerLibrary.set_value_object"></a>

#### set_value_object

```python
@classmethod
def set_value_object(cls, property_: PropertyValue, value: Object) -> None
```

X.set_value_object(property_, value) -> None
Set Value Object

Args:
    property_ (PropertyValue): 
    value (Object):

<a id="unreal.VariantManagerLibrary.set_value_linear_color"></a>

#### set_value_linear_color

```python
@classmethod
def set_value_linear_color(cls, property_: PropertyValue,
                           value: LinearColor) -> None
```

X.set_value_linear_color(property_, value) -> None
Set Value Linear Color

Args:
    property_ (PropertyValue): 
    value (LinearColor):

<a id="unreal.VariantManagerLibrary.set_value_int_point"></a>

#### set_value_int_point

```python
@classmethod
def set_value_int_point(cls, property_: PropertyValue,
                        value: IntPoint) -> None
```

X.set_value_int_point(property_, value) -> None
Set Value Int Point

Args:
    property_ (PropertyValue): 
    value (IntPoint):

<a id="unreal.VariantManagerLibrary.set_value_int"></a>

#### set_value_int

```python
@classmethod
def set_value_int(cls, property_: PropertyValue, value: int) -> None
```

X.set_value_int(property_, value) -> None
Set Value Int

Args:
    property_ (PropertyValue): 
    value (int32):

<a id="unreal.VariantManagerLibrary.set_value_float"></a>

#### set_value_float

```python
@classmethod
def set_value_float(cls, property_: PropertyValue, value: float) -> None
```

X.set_value_float(property_, value) -> None
Set Value Float

Args:
    property_ (PropertyValue): 
    value (float):

<a id="unreal.VariantManagerLibrary.set_value_color"></a>

#### set_value_color

```python
@classmethod
def set_value_color(cls, property_: PropertyValue, value: Color) -> None
```

X.set_value_color(property_, value) -> None
Set Value Color

Args:
    property_ (PropertyValue): 
    value (Color):

<a id="unreal.VariantManagerLibrary.set_value_bool"></a>

#### set_value_bool

```python
@classmethod
def set_value_bool(cls, property_: PropertyValue, value: bool) -> None
```

X.set_value_bool(property_, value) -> None
Set Value Bool

Args:
    property_ (PropertyValue): 
    value (bool):

<a id="unreal.VariantManagerLibrary.set_dependency"></a>

#### set_dependency

```python
@classmethod
def set_dependency(cls, variant: Variant, index: int,
                   dependency: VariantDependency) -> VariantDependency
```

X.set_dependency(variant, index, dependency) -> VariantDependency
Set Dependency

Args:
    variant (Variant): 
    index (int32): 
    dependency (VariantDependency): 

Returns:
    VariantDependency: 

    dependency (VariantDependency):

<a id="unreal.VariantManagerLibrary.remove_variant_set_by_name"></a>

#### remove_variant_set_by_name

```python
@classmethod
def remove_variant_set_by_name(cls, level_variant_sets: LevelVariantSets,
                               variant_set_name: str) -> None
```

X.remove_variant_set_by_name(level_variant_sets, variant_set_name) -> None
Looks for a variant set with VariantSetName within LevelVariantSets and removes it, if it exists

Args:
    level_variant_sets (LevelVariantSets): 
    variant_set_name (str):

<a id="unreal.VariantManagerLibrary.remove_variant_set"></a>

#### remove_variant_set

```python
@classmethod
def remove_variant_set(cls, level_variant_sets: LevelVariantSets,
                       variant_set: VariantSet) -> None
```

X.remove_variant_set(level_variant_sets, variant_set) -> None
Removes VariantSet from LevelVariantSets, if that is its parent

Args:
    level_variant_sets (LevelVariantSets): 
    variant_set (VariantSet):

<a id="unreal.VariantManagerLibrary.remove_variant_by_name"></a>

#### remove_variant_by_name

```python
@classmethod
def remove_variant_by_name(cls, variant_set: VariantSet,
                           variant_name: str) -> None
```

X.remove_variant_by_name(variant_set, variant_name) -> None
Looks for a variant with VariantName within VariantSet and removes it, if it exists

Args:
    variant_set (VariantSet): 
    variant_name (str):

<a id="unreal.VariantManagerLibrary.remove_variant"></a>

#### remove_variant

```python
@classmethod
def remove_variant(cls, variant_set: VariantSet, variant: Variant) -> None
```

X.remove_variant(variant_set, variant) -> None
Removes Variant from VariantSet, if that is its parent

Args:
    variant_set (VariantSet): 
    variant (Variant):

<a id="unreal.VariantManagerLibrary.remove_captured_property_by_name"></a>

#### remove_captured_property_by_name

```python
@classmethod
def remove_captured_property_by_name(cls, variant: Variant, actor: Actor,
                                     property_path: str) -> None
```

X.remove_captured_property_by_name(variant, actor, property_path) -> None
Removes property capture with PropertyPath from Actor's binding within Variant, if it exists

Args:
    variant (Variant): 
    actor (Actor): 
    property_path (str):

<a id="unreal.VariantManagerLibrary.remove_captured_property"></a>

#### remove_captured_property

```python
@classmethod
def remove_captured_property(cls, variant: Variant, actor: Actor,
                             property_: PropertyValue) -> None
```

X.remove_captured_property(variant, actor, property_) -> None
Removes a property capture from an actor binding within Variant, if it exists

Args:
    variant (Variant): 
    actor (Actor): 
    property_ (PropertyValue):

<a id="unreal.VariantManagerLibrary.remove_actor_binding_by_name"></a>

#### remove_actor_binding_by_name

```python
@classmethod
def remove_actor_binding_by_name(cls, variant: Variant,
                                 actor_name: str) -> None
```

X.remove_actor_binding_by_name(variant, actor_name) -> None
Looks for an actor binding to an actor with ActorLabel within Variant and removes it, if it exists

Args:
    variant (Variant): 
    actor_name (str):

<a id="unreal.VariantManagerLibrary.remove_actor_binding"></a>

#### remove_actor_binding

```python
@classmethod
def remove_actor_binding(cls, variant: Variant, actor: Actor) -> None
```

X.remove_actor_binding(variant, actor) -> None
Removes an actor binding to Actor from Variant, if it exists

Args:
    variant (Variant): 
    actor (Actor):

<a id="unreal.VariantManagerLibrary.record"></a>

#### record

```python
@classmethod
def record(cls, prop_val: PropertyValue) -> None
```

X.record(prop_val) -> None
Records new data for PropVal from the actor from which it was captured

Args:
    prop_val (PropertyValue):

<a id="unreal.VariantManagerLibrary.get_value_vector4"></a>

#### get_value_vector4

```python
@classmethod
def get_value_vector4(cls, property_: PropertyValue) -> Vector4
```

X.get_value_vector4(property_) -> Vector4
Get Value Vector 4

Args:
    property_ (PropertyValue): 

Returns:
    Vector4:

<a id="unreal.VariantManagerLibrary.get_value_vector2d"></a>

#### get_value_vector2d

```python
@classmethod
def get_value_vector2d(cls, property_: PropertyValue) -> Vector2D
```

X.get_value_vector2d(property_) -> Vector2D
Get Value Vector 2D

Args:
    property_ (PropertyValue): 

Returns:
    Vector2D:

<a id="unreal.VariantManagerLibrary.get_value_vector"></a>

#### get_value_vector

```python
@classmethod
def get_value_vector(cls, property_: PropertyValue) -> Vector
```

X.get_value_vector(property_) -> Vector
Get Value Vector

Args:
    property_ (PropertyValue): 

Returns:
    Vector:

<a id="unreal.VariantManagerLibrary.get_value_string"></a>

#### get_value_string

```python
@classmethod
def get_value_string(cls, property_: PropertyValue) -> str
```

X.get_value_string(property_) -> str
Get Value String

Args:
    property_ (PropertyValue): 

Returns:
    str:

<a id="unreal.VariantManagerLibrary.get_value_rotator"></a>

#### get_value_rotator

```python
@classmethod
def get_value_rotator(cls, property_: PropertyValue) -> Rotator
```

X.get_value_rotator(property_) -> Rotator
Get Value Rotator

Args:
    property_ (PropertyValue): 

Returns:
    Rotator:

<a id="unreal.VariantManagerLibrary.get_value_quat"></a>

#### get_value_quat

```python
@classmethod
def get_value_quat(cls, property_: PropertyValue) -> Quat
```

X.get_value_quat(property_) -> Quat
Get Value Quat

Args:
    property_ (PropertyValue): 

Returns:
    Quat:

<a id="unreal.VariantManagerLibrary.get_value_object"></a>

#### get_value_object

```python
@classmethod
def get_value_object(cls, property_: PropertyValue) -> Object
```

X.get_value_object(property_) -> Object
Get Value Object

Args:
    property_ (PropertyValue): 

Returns:
    Object:

<a id="unreal.VariantManagerLibrary.get_value_linear_color"></a>

#### get_value_linear_color

```python
@classmethod
def get_value_linear_color(cls, property_: PropertyValue) -> LinearColor
```

X.get_value_linear_color(property_) -> LinearColor
Get Value Linear Color

Args:
    property_ (PropertyValue): 

Returns:
    LinearColor:

<a id="unreal.VariantManagerLibrary.get_value_int_point"></a>

#### get_value_int_point

```python
@classmethod
def get_value_int_point(cls, property_: PropertyValue) -> IntPoint
```

X.get_value_int_point(property_) -> IntPoint
Get Value Int Point

Args:
    property_ (PropertyValue): 

Returns:
    IntPoint:

<a id="unreal.VariantManagerLibrary.get_value_int"></a>

#### get_value_int

```python
@classmethod
def get_value_int(cls, property_: PropertyValue) -> int
```

X.get_value_int(property_) -> int32
Get Value Int

Args:
    property_ (PropertyValue): 

Returns:
    int32:

<a id="unreal.VariantManagerLibrary.get_value_float"></a>

#### get_value_float

```python
@classmethod
def get_value_float(cls, property_: PropertyValue) -> float
```

X.get_value_float(property_) -> float
Get Value Float

Args:
    property_ (PropertyValue): 

Returns:
    float:

<a id="unreal.VariantManagerLibrary.get_value_color"></a>

#### get_value_color

```python
@classmethod
def get_value_color(cls, property_: PropertyValue) -> Color
```

X.get_value_color(property_) -> Color
Get Value Color

Args:
    property_ (PropertyValue): 

Returns:
    Color:

<a id="unreal.VariantManagerLibrary.get_value_bool"></a>

#### get_value_bool

```python
@classmethod
def get_value_bool(cls, property_: PropertyValue) -> bool
```

X.get_value_bool(property_) -> bool
Get Value Bool

Args:
    property_ (PropertyValue): 

Returns:
    bool:

<a id="unreal.VariantManagerLibrary.get_property_type_string"></a>

#### get_property_type_string

```python
@classmethod
def get_property_type_string(cls, prop_val: PropertyValue) -> str
```

X.get_property_type_string(prop_val) -> str
This allows the scripting language to get the type of the C++ property its dealing with

Args:
    prop_val (PropertyValue): 

Returns:
    str:

<a id="unreal.VariantManagerLibrary.get_captured_properties"></a>

#### get_captured_properties

```python
@classmethod
def get_captured_properties(cls, variant: Variant,
                            actor: Actor) -> Array[PropertyValue]
```

X.get_captured_properties(variant, actor) -> Array[PropertyValue]
Returns which properties have been captured for this actor in Variant

Args:
    variant (Variant): 
    actor (Actor): 

Returns:
    Array[PropertyValue]:

<a id="unreal.VariantManagerLibrary.get_capturable_properties"></a>

#### get_capturable_properties

```python
@classmethod
def get_capturable_properties(cls, actor_or_class: Object) -> Array[str]
```

X.get_capturable_properties(actor_or_class) -> Array[str]
Returns a property path for all the properties we can capture for an actor. Will also
handle receiving the actor's class instead.

Args:
    actor_or_class (Object): 

Returns:
    Array[str]:

<a id="unreal.VariantManagerLibrary.delete_dependency"></a>

#### delete_dependency

```python
@classmethod
def delete_dependency(cls, variant: Variant, index: int) -> None
```

X.delete_dependency(variant, index) -> None
Delete Dependency

Args:
    variant (Variant): 
    index (int32):

<a id="unreal.VariantManagerLibrary.create_level_variant_sets_asset"></a>

#### create_level_variant_sets_asset

```python
@classmethod
def create_level_variant_sets_asset(cls, asset_name: str,
                                    asset_path: str) -> LevelVariantSets
```

X.create_level_variant_sets_asset(asset_name, asset_path) -> LevelVariantSets
Creates a new LevelVariantSetsAsset named AssetName (e.g. 'MyLevelVariantSets') in the content path AssetPath (e.g. '/Game')

Args:
    asset_name (str): 
    asset_path (str): 

Returns:
    LevelVariantSets:

<a id="unreal.VariantManagerLibrary.create_level_variant_sets_actor"></a>

#### create_level_variant_sets_actor

```python
@classmethod
def create_level_variant_sets_actor(
        cls,
        level_variant_sets_asset: LevelVariantSets) -> LevelVariantSetsActor
```

X.create_level_variant_sets_actor(level_variant_sets_asset) -> LevelVariantSetsActor
Creates a new ALevelVariantSetsActor in the current scene and assigns LevelVariantSetsAsset to it

Args:
    level_variant_sets_asset (LevelVariantSets): 

Returns:
    LevelVariantSetsActor:

<a id="unreal.VariantManagerLibrary.capture_property"></a>

#### capture_property

```python
@classmethod
def capture_property(cls, variant: Variant, actor: Actor,
                     property_path: str) -> PropertyValue
```

X.capture_property(variant, actor, property_path) -> PropertyValue
Finds the actor binding to Actor within Variant and tries capturing a property with PropertyPath
Returns the captured UPropertyValue if succeeded or nullptr if it failed.

Args:
    variant (Variant): 
    actor (Actor): 
    property_path (str): 

Returns:
    PropertyValue:

<a id="unreal.VariantManagerLibrary.apply"></a>

#### apply

```python
@classmethod
def apply(cls, prop_val: PropertyValue) -> None
```

X.apply(prop_val) -> None
Applies the recorded data from PropVal to the actor from which it was captured

Args:
    prop_val (PropertyValue):

<a id="unreal.VariantManagerLibrary.add_variant_set"></a>

#### add_variant_set

```python
@classmethod
def add_variant_set(cls, level_variant_sets: LevelVariantSets,
                    variant_set: VariantSet) -> None
```

X.add_variant_set(level_variant_sets, variant_set) -> None
Adds VariantSet to the LevelVariantSets' list of VariantSets

Args:
    level_variant_sets (LevelVariantSets): 
    variant_set (VariantSet):

<a id="unreal.VariantManagerLibrary.add_variant"></a>

#### add_variant

```python
@classmethod
def add_variant(cls, variant_set: VariantSet, variant: Variant) -> None
```

X.add_variant(variant_set, variant) -> None
Adds Variant to the VariantSet's list of Variants

Args:
    variant_set (VariantSet): 
    variant (Variant):

<a id="unreal.VariantManagerLibrary.add_dependency"></a>

#### add_dependency

```python
@classmethod
def add_dependency(
        cls, variant: Variant,
        dependency: VariantDependency) -> Tuple[int, VariantDependency]
```

X.add_dependency(variant, dependency) -> (int32, dependency=VariantDependency)
Add Dependency

Args:
    variant (Variant): 
    dependency (VariantDependency): 

Returns:
    VariantDependency: 

    dependency (VariantDependency):

<a id="unreal.VariantManagerLibrary.add_actor_binding"></a>

#### add_actor_binding

```python
@classmethod
def add_actor_binding(cls, variant: Variant, actor: Actor) -> None
```

X.add_actor_binding(variant, actor) -> None
Binds the Actor to the Variant, internally creating a VariantObjectBinding

Args:
    variant (Variant): 
    actor (Actor):

<a id="unreal.InterchangeUserData"></a>