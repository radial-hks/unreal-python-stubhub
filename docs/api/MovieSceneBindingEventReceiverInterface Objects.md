## MovieSceneBindingEventReceiverInterface Objects

```python
class MovieSceneBindingEventReceiverInterface(Interface)
```

Movie Scene Binding Event Receiver Interface

**C++ Source:**

- **Module**: MovieScene
- **File**: MovieSceneBindingEventReceiverInterface.h

<a id="unreal.MovieSceneBindingEventReceiverInterface.on_object_unbound_by_sequencer"></a>

#### on_object_unbound_by_sequencer

```python
def on_object_unbound_by_sequencer(
        player: MovieSceneSequencePlayer,
        binding_id: MovieSceneObjectBindingID) -> None
```

x.on_object_unbound_by_sequencer(player, binding_id) -> None
On Object Unbound by Sequencer

Args:
    player (MovieSceneSequencePlayer): 
    binding_id (MovieSceneObjectBindingID):

<a id="unreal.MovieSceneBindingEventReceiverInterface.on_object_bound_by_sequencer"></a>

#### on_object_bound_by_sequencer

```python
def on_object_bound_by_sequencer(
        player: MovieSceneSequencePlayer,
        binding_id: MovieSceneObjectBindingID) -> None
```

x.on_object_bound_by_sequencer(player, binding_id) -> None
On Object Bound by Sequencer

Args:
    player (MovieSceneSequencePlayer): 
    binding_id (MovieSceneObjectBindingID):

<a id="unreal.MovieSceneEasingFunction"></a>