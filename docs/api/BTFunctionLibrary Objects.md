## BTFunctionLibrary Objects

```python
class BTFunctionLibrary(BlueprintFunctionLibrary)
```

BTFunction Library

**C++ Source:**

- **Module**: AIModule
- **File**: BTFunctionLibrary.h

<a id="unreal.BTFunctionLibrary.stop_using_external_event"></a>

#### stop_using_external_event

```python
@classmethod
def stop_using_external_event(cls, node_owner: BTNode) -> None
```

X.stop_using_external_event(node_owner) -> None
Save variables marked as "instance memory" and clear owning actor
deprecated: No longer needed

Args:
    node_owner (BTNode):

<a id="unreal.BTFunctionLibrary.start_using_external_event"></a>

#### start_using_external_event

```python
@classmethod
def start_using_external_event(cls, node_owner: BTNode,
                               owning_actor: Actor) -> None
```

X.start_using_external_event(node_owner, owning_actor) -> None
Initialize variables marked as "instance memory" and set owning actor for blackboard operations
deprecated: No longer needed

Args:
    node_owner (BTNode): 
    owning_actor (Actor):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_vector"></a>

#### set_blackboard_value_as_vector

```python
@classmethod
def set_blackboard_value_as_vector(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector,
                                   value: Vector) -> None
```

X.set_blackboard_value_as_vector(node_owner, key, value) -> None
Set Blackboard Value as Vector

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (Vector):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_string"></a>

#### set_blackboard_value_as_string

```python
@classmethod
def set_blackboard_value_as_string(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector,
                                   value: str) -> None
```

X.set_blackboard_value_as_string(node_owner, key, value) -> None
Set Blackboard Value as String

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (str):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_rotator"></a>

#### set_blackboard_value_as_rotator

```python
@classmethod
def set_blackboard_value_as_rotator(cls, node_owner: BTNode,
                                    key: BlackboardKeySelector,
                                    value: Rotator) -> None
```

X.set_blackboard_value_as_rotator(node_owner, key, value) -> None
Set Blackboard Value as Rotator

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (Rotator):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_object"></a>

#### set_blackboard_value_as_object

```python
@classmethod
def set_blackboard_value_as_object(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector,
                                   value: Object) -> None
```

X.set_blackboard_value_as_object(node_owner, key, value) -> None
Set Blackboard Value as Object

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (Object):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_name"></a>

#### set_blackboard_value_as_name

```python
@classmethod
def set_blackboard_value_as_name(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector,
                                 value: Name) -> None
```

X.set_blackboard_value_as_name(node_owner, key, value) -> None
Set Blackboard Value as Name

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (Name):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_int"></a>

#### set_blackboard_value_as_int

```python
@classmethod
def set_blackboard_value_as_int(cls, node_owner: BTNode,
                                key: BlackboardKeySelector,
                                value: int) -> None
```

X.set_blackboard_value_as_int(node_owner, key, value) -> None
Set Blackboard Value as Int

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (int32):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_float"></a>

#### set_blackboard_value_as_float

```python
@classmethod
def set_blackboard_value_as_float(cls, node_owner: BTNode,
                                  key: BlackboardKeySelector,
                                  value: float) -> None
```

X.set_blackboard_value_as_float(node_owner, key, value) -> None
Set Blackboard Value as Float

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (float):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_enum"></a>

#### set_blackboard_value_as_enum

```python
@classmethod
def set_blackboard_value_as_enum(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector,
                                 value: int) -> None
```

X.set_blackboard_value_as_enum(node_owner, key, value) -> None
Set Blackboard Value as Enum

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (uint8):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_class"></a>

#### set_blackboard_value_as_class

```python
@classmethod
def set_blackboard_value_as_class(cls, node_owner: BTNode,
                                  key: BlackboardKeySelector,
                                  value: Class) -> None
```

X.set_blackboard_value_as_class(node_owner, key, value) -> None
Set Blackboard Value as Class

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (type(Class)):

<a id="unreal.BTFunctionLibrary.set_blackboard_value_as_bool"></a>

#### set_blackboard_value_as_bool

```python
@classmethod
def set_blackboard_value_as_bool(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector,
                                 value: bool) -> None
```

X.set_blackboard_value_as_bool(node_owner, key, value) -> None
Set Blackboard Value as Bool

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 
    value (bool):

<a id="unreal.BTFunctionLibrary.get_owners_blackboard"></a>

#### get_owners_blackboard

```python
@classmethod
def get_owners_blackboard(cls, node_owner: BTNode) -> BlackboardComponent
```

X.get_owners_blackboard(node_owner) -> BlackboardComponent
Get Owners Blackboard

Args:
    node_owner (BTNode): 

Returns:
    BlackboardComponent:

<a id="unreal.BTFunctionLibrary.get_blackboard"></a>

#### get_blackboard

```python
@classmethod
def get_blackboard(cls, node_owner: BTNode) -> BlackboardComponent
```

deprecated: 'get_blackboard' was renamed to 'get_owners_blackboard'.

<a id="unreal.BTFunctionLibrary.get_owner_component"></a>

#### get_owner_component

```python
@classmethod
def get_owner_component(cls, node_owner: BTNode) -> BehaviorTreeComponent
```

X.get_owner_component(node_owner) -> BehaviorTreeComponent
Get Owner Component

Args:
    node_owner (BTNode): 

Returns:
    BehaviorTreeComponent:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_vector"></a>

#### get_blackboard_value_as_vector

```python
@classmethod
def get_blackboard_value_as_vector(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector) -> Vector
```

X.get_blackboard_value_as_vector(node_owner, key) -> Vector
Get Blackboard Value as Vector

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    Vector:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_string"></a>

#### get_blackboard_value_as_string

```python
@classmethod
def get_blackboard_value_as_string(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector) -> str
```

X.get_blackboard_value_as_string(node_owner, key) -> str
Get Blackboard Value as String

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    str:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_rotator"></a>

#### get_blackboard_value_as_rotator

```python
@classmethod
def get_blackboard_value_as_rotator(cls, node_owner: BTNode,
                                    key: BlackboardKeySelector) -> Rotator
```

X.get_blackboard_value_as_rotator(node_owner, key) -> Rotator
Get Blackboard Value as Rotator

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    Rotator:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_object"></a>

#### get_blackboard_value_as_object

```python
@classmethod
def get_blackboard_value_as_object(cls, node_owner: BTNode,
                                   key: BlackboardKeySelector) -> Object
```

X.get_blackboard_value_as_object(node_owner, key) -> Object
Get Blackboard Value as Object

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    Object:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_name"></a>

#### get_blackboard_value_as_name

```python
@classmethod
def get_blackboard_value_as_name(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector) -> Name
```

X.get_blackboard_value_as_name(node_owner, key) -> Name
Get Blackboard Value as Name

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    Name:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_int"></a>

#### get_blackboard_value_as_int

```python
@classmethod
def get_blackboard_value_as_int(cls, node_owner: BTNode,
                                key: BlackboardKeySelector) -> int
```

X.get_blackboard_value_as_int(node_owner, key) -> int32
Get Blackboard Value as Int

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    int32:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_float"></a>

#### get_blackboard_value_as_float

```python
@classmethod
def get_blackboard_value_as_float(cls, node_owner: BTNode,
                                  key: BlackboardKeySelector) -> float
```

X.get_blackboard_value_as_float(node_owner, key) -> float
Get Blackboard Value as Float

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    float:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_enum"></a>

#### get_blackboard_value_as_enum

```python
@classmethod
def get_blackboard_value_as_enum(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector) -> int
```

X.get_blackboard_value_as_enum(node_owner, key) -> uint8
Get Blackboard Value as Enum

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    uint8:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_class"></a>

#### get_blackboard_value_as_class

```python
@classmethod
def get_blackboard_value_as_class(cls, node_owner: BTNode,
                                  key: BlackboardKeySelector) -> Class
```

X.get_blackboard_value_as_class(node_owner, key) -> type(Class)
Get Blackboard Value as Class

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    type(Class):

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_bool"></a>

#### get_blackboard_value_as_bool

```python
@classmethod
def get_blackboard_value_as_bool(cls, node_owner: BTNode,
                                 key: BlackboardKeySelector) -> bool
```

X.get_blackboard_value_as_bool(node_owner, key) -> bool
Get Blackboard Value as Bool

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    bool:

<a id="unreal.BTFunctionLibrary.get_blackboard_value_as_actor"></a>

#### get_blackboard_value_as_actor

```python
@classmethod
def get_blackboard_value_as_actor(cls, node_owner: BTNode,
                                  key: BlackboardKeySelector) -> Actor
```

X.get_blackboard_value_as_actor(node_owner, key) -> Actor
Get Blackboard Value as Actor

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector): 

Returns:
    Actor:

<a id="unreal.BTFunctionLibrary.clear_blackboard_value_as_vector"></a>

#### clear_blackboard_value_as_vector

```python
@classmethod
def clear_blackboard_value_as_vector(cls, node_owner: BTNode,
                                     key: BlackboardKeySelector) -> None
```

X.clear_blackboard_value_as_vector(node_owner, key) -> None
(DEPRECATED) Use ClearBlackboardValue instead
deprecated: Use ClearBlackboardValue instead.

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector):

<a id="unreal.BTFunctionLibrary.clear_blackboard_value"></a>

#### clear_blackboard_value

```python
@classmethod
def clear_blackboard_value(cls, node_owner: BTNode,
                           key: BlackboardKeySelector) -> None
```

X.clear_blackboard_value(node_owner, key) -> None
Resets indicated value to "not set" value, based on values type

Args:
    node_owner (BTNode): 
    key (BlackboardKeySelector):

<a id="unreal.BTNode"></a>