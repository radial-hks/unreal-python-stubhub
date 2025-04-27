## RigVMEdGraphDisplaySettings Objects

```python
class RigVMEdGraphDisplaySettings(StructBase)
```

Rig VMEd Graph Display Settings

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMBlueprint.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_determine_range`` (bool):  [Read-Write]
- ``average_frames`` (int32):  [Read-Write] If you set this to more than 1 the results will be averaged across multiple frames
- ``max_duration_color`` (LinearColor):  [Read-Write] The color of the slowest instruction / node
- ``max_micro_seconds`` (double):  [Read-Write] The duration in microseconds of the slowest instruction / node
- ``min_duration_color`` (LinearColor):  [Read-Write] The color of the fastest instruction / node
- ``min_micro_seconds`` (double):  [Read-Write] The duration in microseconds of the fastest instruction / node
- ``node_run_limit`` (int32):  [Read-Write] A upper limit for counts for nodes used for debugging.
  If a node reaches this count a warning will be issued for the
  node and displayed both in the execution stack as well as in the
  graph. Setting this to <= 1 disables the warning.
  Note: The count limit doesn't apply to functions / collapse nodes.
- ``node_run_lower_bound`` (int32):  [Read-Write] A lower limit for counts for nodes used for debugging.
  Any node lower than this count won't show the run count.
- ``show_node_instruction_index`` (bool):  [Read-Write] When enabled shows the first node instruction index
  matching the execution stack window.
- ``show_node_run_counts`` (bool):  [Read-Write] When enabled shows the node counts both in the graph view as
  we as in the execution stack window.
  The number on each node represents how often the node has been run.
  Keep in mind when looking at nodes in a function the count
  represents the sum of all counts for each node based on all
  references of the function currently running.
- ``tag_display_mode`` (RigVMTagDisplayMode):  [Read-Write] The color of the slowest instruction / node
- ``total_micro_seconds`` (double):  [Read-Only] The total duration of the last execution of the rig

<a id="unreal.RigVMEdGraphDisplaySettings.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.RigGraphDisplaySettings"></a>