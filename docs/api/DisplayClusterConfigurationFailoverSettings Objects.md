## DisplayClusterConfigurationFailoverSettings Objects

```python
class DisplayClusterConfigurationFailoverSettings(StructBase)
```

Display Cluster Configuration Failover Settings

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``failover_policy`` (DisplayClusterConfigurationFailoverPolicy):  [Read-Write] Failover policy

<a id="unreal.DisplayClusterConfigurationFailoverSettings.__init__"></a>

#### __init__

```python
def __init__(
    failover_policy:
    DisplayClusterConfigurationFailoverPolicy = DisplayClusterConfigurationFailoverPolicy
    .DISABLED
) -> None
```

<a id="unreal.DisplayClusterConfigurationFailoverSettings.failover_policy"></a>

#### failover_policy

```python
@property
def failover_policy() -> DisplayClusterConfigurationFailoverPolicy
```

(DisplayClusterConfigurationFailoverPolicy):  [Read-Write] Failover policy

<a id="unreal.DisplayClusterConfigurationFailoverSettings.failover_policy"></a>

#### failover_policy

```python
@failover_policy.setter
def failover_policy(value: DisplayClusterConfigurationFailoverPolicy) -> None
```

<a id="unreal.DisplayClusterConfigurationDiagnostics"></a>