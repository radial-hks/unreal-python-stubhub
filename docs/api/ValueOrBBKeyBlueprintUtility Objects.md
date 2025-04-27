## ValueOrBBKeyBlueprintUtility Objects

```python
class ValueOrBBKeyBlueprintUtility(BlueprintFunctionLibrary)
```

Value or BBKey Blueprint Utility

**C++ Source:**

- **Module**: AIModule
- **File**: ValueOrBBKeyBlueprintUtility.h

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_vector"></a>

#### get_vector

```python
@classmethod
def get_vector(cls, value: ValueOrBBKey_Vector,
               behavior_tree_comp: BehaviorTreeComponent) -> Vector
```

X.get_vector(value, behavior_tree_comp) -> Vector
Get Vector

Args:
    value (ValueOrBBKey_Vector): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    Vector:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_struct"></a>

#### get_struct

```python
@classmethod
def get_struct(cls, value: ValueOrBBKey_Struct,
               behavior_tree_comp: BehaviorTreeComponent) -> InstancedStruct
```

X.get_struct(value, behavior_tree_comp) -> InstancedStruct
Get Struct

Args:
    value (ValueOrBBKey_Struct): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    InstancedStruct:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_string"></a>

#### get_string

```python
@classmethod
def get_string(cls, value: ValueOrBBKey_String,
               behavior_tree_comp: BehaviorTreeComponent) -> str
```

X.get_string(value, behavior_tree_comp) -> str
Get String

Args:
    value (ValueOrBBKey_String): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    str:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_rotator"></a>

#### get_rotator

```python
@classmethod
def get_rotator(cls, value: ValueOrBBKey_Rotator,
                behavior_tree_comp: BehaviorTreeComponent) -> Rotator
```

X.get_rotator(value, behavior_tree_comp) -> Rotator
Get Rotator

Args:
    value (ValueOrBBKey_Rotator): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    Rotator:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_object"></a>

#### get_object

```python
@classmethod
def get_object(cls, value: ValueOrBBKey_Object,
               behavior_tree_comp: BehaviorTreeComponent) -> Object
```

X.get_object(value, behavior_tree_comp) -> Object
Get Object

Args:
    value (ValueOrBBKey_Object): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    Object:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_name"></a>

#### get_name

```python
@classmethod
def get_name(cls, value: ValueOrBBKey_Name,
             behavior_tree_comp: BehaviorTreeComponent) -> Name
```

X.get_name(value, behavior_tree_comp) -> Name
Get Name

Args:
    value (ValueOrBBKey_Name): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    Name:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_int32"></a>

#### get_int32

```python
@classmethod
def get_int32(cls, value: ValueOrBBKey_Int32,
              behavior_tree_comp: BehaviorTreeComponent) -> int
```

X.get_int32(value, behavior_tree_comp) -> int32
Get Int 32

Args:
    value (ValueOrBBKey_Int32): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    int32:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_float"></a>

#### get_float

```python
@classmethod
def get_float(cls, value: ValueOrBBKey_Float,
              behavior_tree_comp: BehaviorTreeComponent) -> float
```

X.get_float(value, behavior_tree_comp) -> float
Get Float

Args:
    value (ValueOrBBKey_Float): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    float:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_enum"></a>

#### get_enum

```python
@classmethod
def get_enum(cls, value: ValueOrBBKey_Enum,
             behavior_tree_comp: BehaviorTreeComponent) -> int
```

X.get_enum(value, behavior_tree_comp) -> uint8
Get Enum

Args:
    value (ValueOrBBKey_Enum): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    uint8:

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_class"></a>

#### get_class

```python
@classmethod
def get_class(cls, value: ValueOrBBKey_Class,
              behavior_tree_comp: BehaviorTreeComponent) -> Class
```

X.get_class(value, behavior_tree_comp) -> type(Class)
Get Class

Args:
    value (ValueOrBBKey_Class): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    type(Class):

<a id="unreal.ValueOrBBKeyBlueprintUtility.get_bool"></a>

#### get_bool

```python
@classmethod
def get_bool(cls, value: ValueOrBBKey_Bool,
             behavior_tree_comp: BehaviorTreeComponent) -> bool
```

X.get_bool(value, behavior_tree_comp) -> bool
Get Bool

Args:
    value (ValueOrBBKey_Bool): 
    behavior_tree_comp (BehaviorTreeComponent): 

Returns:
    bool:

<a id="unreal.PawnAction"></a>