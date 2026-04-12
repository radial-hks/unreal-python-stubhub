## GameFrameworkComponentManager Objects

```python
class GameFrameworkComponentManager(GameInstanceSubsystem)
```

GameFrameworkComponentManager

A manager to handle putting components on actors as they come and go.
Put in a request to instantiate components of a given class on actors of a given class and they will automatically be made for them as the actors are spawned.
Submit delegate handlers to listen for actors of a given class. Those handlers will automatically run when actors of a given class or registered as receivers or game events are sent.
Actors must opt-in to this behavior by calling AddReceiver/RemoveReceiver for themselves when they are ready to receive the components and when they want to remove them.
Any actors that are in memory when a request is made will automatically get the components, and any in memory when a request is removed will lose the components immediately.
Requests are reference counted, so if multiple requests are made for the same actor class and component class, only one component will be added and that component wont be removed until all requests are removed.

**C++ Source:**

- **Plugin**: ModularGameplay
- **Module**: ModularGameplay
- **File**: GameFrameworkComponentManager.h

<a id="unreal.GameFrameworkComponentManager.unregister_class_init_state_delegate"></a>

#### unregister\_class\_init\_state\_delegate

```python
def unregister_class_init_state_delegate(
        actor_class: Class,
        delegate_to_remove: ActorInitStateChangedBPDelegate) -> bool
```

x.unregister_class_init_state_delegate(actor_class, delegate_to_remove) -> bool
Removes a registered delegate bound to a class

Args:
    actor_class (Class): 
    delegate_to_remove (ActorInitStateChangedBPDelegate): 

Returns:
    bool:

<a id="unreal.GameFrameworkComponentManager.unregister_actor_init_state_delegate"></a>

#### unregister\_actor\_init\_state\_delegate

```python
def unregister_actor_init_state_delegate(
        actor: Actor,
        delegate_to_remove: ActorInitStateChangedBPDelegate) -> bool
```

x.unregister_actor_init_state_delegate(actor, delegate_to_remove) -> bool
Removes a registered delegate bound to a specific actor

Args:
    actor (Actor): 
    delegate_to_remove (ActorInitStateChangedBPDelegate): 

Returns:
    bool:

<a id="unreal.GameFrameworkComponentManager.send_extension_event"></a>

#### send\_extension\_event

```python
def send_extension_event(receiver: Actor,
                         event_name: Name,
                         only_in_game_worlds: bool = True) -> None
```

x.send_extension_event(receiver, event_name, only_in_game_worlds=True) -> None
Sends an arbitrary extension event that can be listened for by other systems

Args:
    receiver (Actor): 
    event_name (Name): 
    only_in_game_worlds (bool):

<a id="unreal.GameFrameworkComponentManager.remove_receiver"></a>

#### remove\_receiver

```python
def remove_receiver(receiver: Actor) -> None
```

x.remove_receiver(receiver) -> None
Removes an actor as a receiver for components.

Args:
    receiver (Actor):

<a id="unreal.GameFrameworkComponentManager.register_and_call_for_class_init_state"></a>

#### register\_and\_call\_for\_class\_init\_state

```python
def register_and_call_for_class_init_state(
        actor_class: Class,
        feature_name: Name,
        required_state: GameplayTag,
        delegate: ActorInitStateChangedBPDelegate,
        call_immediately: bool = True) -> bool
```

x.register_and_call_for_class_init_state(actor_class, feature_name, required_state, delegate, call_immediately=True) -> bool
Registers blueprint delegate for feature state change notifications on a class of actors and may call it immediately

Args:
    actor_class (Class): Name of an actor class to listen for changes to
    feature_name (Name): If not empty, only listen to state changes for the specified feature
    required_state (GameplayTag): If specified, only activate if the init state of the feature is equal to or later than this
    delegate (ActorInitStateChangedBPDelegate): Native delegate to call
    call_immediately (bool): If true and the actor feature is already in the specified state, call delegate immediately after registering

Returns:
    bool: true if delegate was registered

<a id="unreal.GameFrameworkComponentManager.register_and_call_for_actor_init_state"></a>

#### register\_and\_call\_for\_actor\_init\_state

```python
def register_and_call_for_actor_init_state(
        actor: Actor,
        feature_name: Name,
        required_state: GameplayTag,
        delegate: ActorInitStateChangedBPDelegate,
        call_immediately: bool = True) -> bool
```

x.register_and_call_for_actor_init_state(actor, feature_name, required_state, delegate, call_immediately=True) -> bool
Registers blueprint delegate for feature state change notifications on a specific actor and may call it immediately

Args:
    actor (Actor): The actor to listen for state changes to, if you don't have a specific actor call the Class version instead
    feature_name (Name): If not empty, only listen to state changes for the specified feature
    required_state (GameplayTag): If specified, only activate if the init state of the feature is equal to or later than this
    delegate (ActorInitStateChangedBPDelegate): Native delegate to call
    call_immediately (bool): If true and the actor feature is already in the specified state, call delegate immediately after registering

Returns:
    bool: true if delegate was registered

<a id="unreal.GameFrameworkComponentManager.add_receiver"></a>

#### add\_receiver

```python
def add_receiver(receiver: Actor,
                 add_only_in_game_worlds: bool = True) -> None
```

x.add_receiver(receiver, add_only_in_game_worlds=True) -> None
Adds an actor as a receiver for components. If it passes the actorclass filter on requests it will get the components.

Args:
    receiver (Actor): 
    add_only_in_game_worlds (bool):

<a id="unreal.GameFrameworkInitStateInterface"></a>