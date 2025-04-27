## DisplayClusterClusterEventListener Objects

```python
class DisplayClusterClusterEventListener(Interface)
```

Display Cluster Cluster Event Listener

**C++ Source:**

- **Plugin**: nDisplay
- **Module**: DisplayCluster
- **File**: IDisplayClusterClusterEventListener.h

<a id="unreal.DisplayClusterClusterEventListener.on_cluster_event_json"></a>

#### on_cluster_event_json

```python
def on_cluster_event_json(event: DisplayClusterClusterEventJson) -> None
```

x.on_cluster_event_json(event) -> None
React on incoming JSON cluster events

Args:
    event (DisplayClusterClusterEventJson):

<a id="unreal.DisplayClusterClusterEventListener.on_cluster_event_binary"></a>

#### on_cluster_event_binary

```python
def on_cluster_event_binary(event: DisplayClusterClusterEventBinary) -> None
```

x.on_cluster_event_binary(event) -> None
React on incoming binary cluster events

Args:
    event (DisplayClusterClusterEventBinary):

<a id="unreal.LensDistortionModelHandlerBase"></a>