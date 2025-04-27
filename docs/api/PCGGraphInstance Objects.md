## PCGGraphInstance Objects

```python
class PCGGraphInstance(PCGGraphInterface)
```

PCGGraph Instance

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGraph.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write] Can override the category of this instance.
- ``color`` (LinearColor):  [Read-Write] Override of the color for the subgraph node for this graph.
- ``description`` (Text):  [Read-Write] Can override the description of this instance.
- ``expose_to_library`` (bool):  [Read-Write]
- ``graph`` (PCGGraphInterface):  [Read-Write]
- ``override_category`` (bool):  [Read-Write]
- ``override_color`` (bool):  [Read-Write]
- ``override_description`` (bool):  [Read-Write]
- ``override_title`` (bool):  [Read-Write]
- ``parameters_overrides`` (PCGOverrideInstancedPropertyBag):  [Read-Write]
- ``title`` (Text):  [Read-Write] Override of the title for the subgraph node for this graph.

<a id="unreal.PCGGraphInstance.graph"></a>

#### graph

```python
@property
def graph() -> PCGGraphInterface
```

(PCGGraphInterface):  [Read-Only]

<a id="unreal.PCGGraphInstance.override_description"></a>

#### override_description

```python
@property
def override_description() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGraphInstance.override_description"></a>

#### override_description

```python
@override_description.setter
def override_description(value: bool) -> None
```

<a id="unreal.PCGGraphInstance.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write] Can override the description of this instance.

<a id="unreal.PCGGraphInstance.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.PCGGraphInstance.override_category"></a>

#### override_category

```python
@property
def override_category() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGGraphInstance.override_category"></a>

#### override_category

```python
@override_category.setter
def override_category(value: bool) -> None
```

<a id="unreal.PCGGraphInstance.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write] Can override the category of this instance.

<a id="unreal.PCGGraphInstance.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.PCGGraphInputOutputSettings"></a>