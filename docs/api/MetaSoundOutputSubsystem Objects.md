## MetaSoundOutputSubsystem Objects

```python
class MetaSoundOutputSubsystem(WorldSubsystem)
```

Provides access to a playing Metasound generator's outputs

**C++ Source:**

- **Plugin**: Metasound
- **Module**: MetasoundEngine
- **File**: MetasoundOutputSubsystem.h

<a id="unreal.MetaSoundOutputSubsystem.watch_output"></a>

#### watch_output

```python
def watch_output(audio_component: AudioComponent,
                 output_name: Name,
                 on_output_value_changed: OnMetasoundOutputValueChanged,
                 analyzer_name: Name = "None",
                 analyzer_output_name: Name = "None") -> bool
```

x.watch_output(audio_component, output_name, on_output_value_changed, analyzer_name="None", analyzer_output_name="None") -> bool
Watch an output on a Metasound playing on a given audio component.

Args:
    audio_component (AudioComponent): The audio component
    output_name (Name): The user-specified name of the output in the Metasound
    on_output_value_changed (OnMetasoundOutputValueChanged): The event to fire when the output's value changes
    analyzer_name (Name): (optional) The name of the analyzer to use on the output, defaults to a passthrough
    analyzer_output_name (Name): (optional) The name of the output on the analyzer to watch, defaults to the passthrough output

Returns:
    bool: true if the watch setup succeeded, false otherwise

<a id="unreal.MetaSoundPatch"></a>