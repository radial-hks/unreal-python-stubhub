## AutomationScheduler Objects

```python
class AutomationScheduler(object)
```

Used to schedule python functions and generators to be run between editor ticks.
One iteration of a generator is done per tick. It means that each yield statement will call for an editor tick.
If a function or yield statement returns a function or a generator, that object is scheduled right after the next
tick. The previously scheduled tasks are run afterwards.

<a id="unreal.AutomationScheduler._singleton_instance"></a>

#### _singleton_instance

<a id="unreal.AutomationScheduler._lock"></a>

#### _lock

<a id="unreal.AutomationScheduler._delegate_handle"></a>

#### _delegate_handle

<a id="unreal.AutomationScheduler._current"></a>

#### _current

<a id="unreal.AutomationScheduler.schedule"></a>

#### schedule

Scheduled tasks as a priority list. It is None if the scheduler was not initiated.

<a id="unreal.AutomationScheduler.__new__"></a>

#### __new__

```python
def __new__(cls)
```

<a id="unreal.AutomationScheduler._callback"></a>

#### _callback

```python
def _callback(_)
```

Main loop

<a id="unreal.AutomationScheduler._shutdown"></a>

#### _shutdown

```python
@classmethod
def _shutdown(cls)
```

<a id="unreal.AutomationScheduler.add_latent_command"></a>

#### add_latent_command

```python
@classmethod
def add_latent_command(cls, task)
```

Add a function or a generator to the AutomationScheduler schedule.
Can be used as a decorator to add a function.
Note that order sequence is important here. Registered first is run first.

ie:
    @unreal.AutomationScheduler.add_latent_command
    def setup_level():
        pass

<a id="unreal.AutomationScheduler.set_latent_command_timeout"></a>

#### set_latent_command_timeout

```python
@classmethod
def set_latent_command_timeout(cls, seconds)
```

Set the Python Automation Test latent command timeout in second

<a id="unreal.AutomationScheduler.cleanup"></a>

#### cleanup

```python
@classmethod
def cleanup(cls)
```

Force a shutdown of the singleton instance if any is running