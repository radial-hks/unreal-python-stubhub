## AsyncPhysicsData Objects

```python
class AsyncPhysicsData(Object)
```

The base class for async physics data. Inherit from this to create custom data for async physics tick.
When no data is available (say due to massive latency or packet loss) we fall back on the default constructed data.
This means you should set the default values to something equivalent to no input (for example bPlayerWantsToJump should probably default to false)

**C++ Source:**

- **Module**: Engine
- **File**: AsyncPhysicsData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``replication_redundancy`` (int32):  [Read-Write] Determines how many times we redundantly send data to server. The higher this number the less packet loss, but more bandwidth is used

<a id="unreal.AudioPanelWidgetInterface"></a>