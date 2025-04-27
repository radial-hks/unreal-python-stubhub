## MovieGraphPinQueryRequirement Objects

```python
class MovieGraphPinQueryRequirement(EnumBase)
```

Specifies a restriction on pin properties when searching for a pin on a node.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphPin.h

<a id="unreal.MovieGraphPinQueryRequirement.BUILT_IN"></a>

#### BUILT_IN

0: The pin must be built-in, meaning that it is always present on the node.

<a id="unreal.MovieGraphPinQueryRequirement.DYNAMIC"></a>

#### DYNAMIC

1: The pin must be dynamic, meaning that it may not always exist on the node. These are typically user-created pins.

<a id="unreal.MovieGraphPinQueryRequirement.BUILT_IN_OR_DYNAMIC"></a>

#### BUILT_IN_OR_DYNAMIC

2: The pin can be either built-in or dynamic.

<a id="unreal.MovieGraphConditionGroupOpType"></a>