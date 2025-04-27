## PCGSettingsInterface Objects

```python
class PCGSettingsInterface(PCGData)
```

PCGSettings Interface

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``debug`` (bool):  [Read-Write]
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``enabled`` (bool):  [Read-Write]

<a id="unreal.PCGSettingsInterface.enabled"></a>

#### enabled

```python
@property
def enabled() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSettingsInterface.enabled"></a>

#### enabled

```python
@enabled.setter
def enabled(value: bool) -> None
```

<a id="unreal.PCGSettingsInterface.debug"></a>

#### debug

```python
@property
def debug() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSettingsInterface.debug"></a>

#### debug

```python
@debug.setter
def debug(value: bool) -> None
```

<a id="unreal.PCGSettingsInterface.debug_settings"></a>

#### debug_settings

```python
@property
def debug_settings() -> PCGDebugVisualizationSettings
```

(PCGDebugVisualizationSettings):  [Read-Write]

<a id="unreal.PCGSettingsInterface.debug_settings"></a>

#### debug_settings

```python
@debug_settings.setter
def debug_settings(value: PCGDebugVisualizationSettings) -> None
```

<a id="unreal.PCGSettingsInterface.break_debugger"></a>

#### break_debugger

```python
@property
def break_debugger() -> bool
```

(bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.

<a id="unreal.PCGSettingsInterface.break_debugger"></a>

#### break_debugger

```python
@break_debugger.setter
def break_debugger(value: bool) -> None
```

<a id="unreal.PCGSettings"></a>