## GeneratedNavLinksProxy Objects

```python
class GeneratedNavLinksProxy(BaseGeneratedNavLinksProxy)
```

Experimental
Blueprintable class used to handle generated links as custom links.

**C++ Source:**

- **Module**: AIModule
- **File**: GeneratedNavLinksProxy.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``on_smart_link_reached`` (LinkReachedSignature):  [Read-Write]

<a id="unreal.GeneratedNavLinksProxy.on_smart_link_reached"></a>

#### on_smart_link_reached

```python
@property
def on_smart_link_reached() -> LinkReachedSignature
```

(LinkReachedSignature):  [Read-Write]

<a id="unreal.GeneratedNavLinksProxy.on_smart_link_reached"></a>

#### on_smart_link_reached

```python
@on_smart_link_reached.setter
def on_smart_link_reached(value: LinkReachedSignature) -> None
```

<a id="unreal.GeneratedNavLinksProxy.receive_smart_link_reached"></a>

#### receive_smart_link_reached

```python
def receive_smart_link_reached(agent: Actor, destination: Vector) -> None
```

x.receive_smart_link_reached(agent, destination) -> None
Called when agent reaches smart link during path following.

Args:
    agent (Actor): 
    destination (Vector):

<a id="unreal.ValueOrBBKeyBlueprintUtility"></a>