## GameFrameworkInitStateInterface Objects

```python
class GameFrameworkInitStateInterface(Interface)
```

Game Framework Init State Interface

**C++ Source:**

- **Plugin**: ModularGameplay
- **Module**: ModularGameplay
- **File**: GameFrameworkInitStateInterface.h

<a id="unreal.GameFrameworkInitStateInterface.unregister_init_state_delegate"></a>

#### unregister\_init\_state\_delegate

```python
def unregister_init_state_delegate(
        delegate: ActorInitStateChangedBPDelegate) -> bool
```

x.unregister_init_state_delegate(delegate) -> bool
Unbinds a BP delegate from changes to this feature

Args:
    delegate (ActorInitStateChangedBPDelegate): 

Returns:
    bool:

<a id="unreal.GameFrameworkInitStateInterface.register_and_call_for_init_state_change"></a>

#### register\_and\_call\_for\_init\_state\_change

```python
def register_and_call_for_init_state_change(
        required_state: GameplayTag,
        delegate: ActorInitStateChangedBPDelegate,
        call_immediately: bool = True) -> bool
```

x.register_and_call_for_init_state_change(required_state, delegate, call_immediately=True) -> bool
Binds a BP delegate to get called on a state change for this feature

Args:
    required_state (GameplayTag): 
    delegate (ActorInitStateChangedBPDelegate): 
    call_immediately (bool): 

Returns:
    bool:

<a id="unreal.GameFrameworkInitStateInterface.has_reached_init_state"></a>

#### has\_reached\_init\_state

```python
def has_reached_init_state(desired_state: GameplayTag) -> bool
```

x.has_reached_init_state(desired_state) -> bool
Checks the component manager to see if we have already reached the desired state or a later one

Args:
    desired_state (GameplayTag): 

Returns:
    bool:

<a id="unreal.GameFrameworkInitStateInterface.get_init_state"></a>

#### get\_init\_state

```python
def get_init_state() -> GameplayTag
```

x.get_init_state() -> GameplayTag
Returns the current feature state of this object, the default behavior is to query the manager

Returns:
    GameplayTag:

<a id="unreal.GameFrameworkInitStateInterface.get_feature_name"></a>

#### get\_feature\_name

```python
def get_feature_name() -> Name
```

x.get_feature_name() -> Name
Returns the feature this object implements, this interface is only meant for simple objects with a single feature like Actor

Returns:
    Name:

<a id="unreal.GameStateComponent"></a>