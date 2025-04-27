## MovieGraphConditionGroupQuery_ActorName Objects

```python
class MovieGraphConditionGroupQuery_ActorName(MovieGraphConditionGroupQueryBase
                                              )
```

Query type which filters actors via their name (label).

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``wildcard_search`` (str):  [Read-Write] The name that the actor needs to have in order to be a match. Not case sensitive. One name per line. Wildcards ("?" and "*") are supported but not required.
  The "*" wildcard matches zero or more characters, and "?" matches exactly one character (and that character must be present).

  Wildcard examples:
  Foo* would match Foo, FooBar, and FooBaz, but not BarFoo.
  *Foo* would match the above in addition to BarFoo.
  Foo?Bar would match Foo.Bar and Foo_Bar, but not FooBar.
  Foo? would match Food, but not FooBar or BarFoo.
  Foo??? would match FooBar and FooBaz, but not Foo or Food.
  ?oo? would match Food, but not Foo.
  ?Foo* would match AFooBar, but not FooBar

<a id="unreal.MovieGraphConditionGroupQuery_ActorType"></a>