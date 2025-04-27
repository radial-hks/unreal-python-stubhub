## AIPerceptionSystem Objects

```python
class AIPerceptionSystem(AISubsystem)
```

AI Subsystem managing AI Perception through registered AI Senses between Listeners and Stimuli Sources

**C++ Source:**

- **Module**: AIModule
- **File**: AIPerceptionSystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``perception_aging_rate`` (float):  [Read-Write]

<a id="unreal.AIPerceptionSystem.report_perception_event"></a>

#### report_perception_event

```python
@classmethod
def report_perception_event(cls, world_context_object: Object,
                            perception_event: AISenseEvent) -> None
```

X.report_perception_event(world_context_object, perception_event) -> None
Report Perception Event

Args:
    world_context_object (Object): 
    perception_event (AISenseEvent):

<a id="unreal.AIPerceptionSystem.report_event"></a>

#### report_event

```python
def report_event(perception_event: AISenseEvent) -> None
```

x.report_event(perception_event) -> None
Report Event

Args:
    perception_event (AISenseEvent):

<a id="unreal.AIPerceptionSystem.register_perception_stimuli_source"></a>

#### register_perception_stimuli_source

```python
@classmethod
def register_perception_stimuli_source(cls, world_context_object: Object,
                                       sense: Class, target: Actor) -> bool
```

X.register_perception_stimuli_source(world_context_object, sense, target) -> bool
Register Perception Stimuli Source

Args:
    world_context_object (Object): 
    sense (type(Class)): 
    target (Actor): 

Returns:
    bool:

<a id="unreal.AIPerceptionSystem.get_sense_class_for_stimulus"></a>

#### get_sense_class_for_stimulus

```python
@classmethod
def get_sense_class_for_stimulus(cls, world_context_object: Object,
                                 stimulus: AIStimulus) -> Class
```

X.get_sense_class_for_stimulus(world_context_object, stimulus) -> type(Class)
Get Sense Class for Stimulus

Args:
    world_context_object (Object): 
    stimulus (AIStimulus): 

Returns:
    type(Class):

<a id="unreal.AISense"></a>