## DisplayClusterConfigurationFailoverPolicy Objects

```python
class DisplayClusterConfigurationFailoverPolicy(EnumBase)
```

EDisplay Cluster Configuration Failover Policy

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayClusterConfiguration
- **File**: DisplayClusterConfigurationTypes_Enums.h

<a id="unreal.DisplayClusterConfigurationFailoverPolicy.DISABLED"></a>

#### DISABLED

0: No failover operations performed. The whole cluster gets terminated in case of any error

<a id="unreal.DisplayClusterConfigurationFailoverPolicy.DROP_SECONDARY_NODES_ONLY"></a>

#### DROP_SECONDARY_NODES_ONLY

1: This policy allows to drop any secondary node out of cluster in case it's failed,
and let the others continue working. However, the whole cluster will be terminated if primary node fails.

<a id="unreal.DisplayClusterConfigurationViewportLightcardOCIOMode"></a>