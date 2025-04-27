## PCGSettingsInstance Objects

```python
class PCGSettingsInstance(PCGSettingsInterface)
```

PCGSettings Instance

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``debug`` (bool):  [Read-Write]
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]
- ``original_settings`` (PCGSettings):  [Read-Only]
- ``settings`` (PCGSettings):  [Read-Only]

<a id="unreal.PCGSettingsInstance.settings"></a>

#### settings

```python
@property
def settings() -> PCGSettings
```

(PCGSettings):  [Read-Only]

<a id="unreal.PCGTrivialSettings"></a>