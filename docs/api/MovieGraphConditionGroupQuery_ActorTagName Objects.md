## MovieGraphConditionGroupQuery_ActorTagName Objects

```python
class MovieGraphConditionGroupQuery_ActorTagName(
        MovieGraphConditionGroupQueryBase)
```

Query type which filters actors via tags on actors.

**C++ Source:**

- **Plugin**: MovieRenderPipeline
- **Module**: MovieRenderPipelineCore
- **File**: MovieGraphRenderLayerSubsystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``tags_to_match`` (str):  [Read-Write] Tags on the actor must match one or more of the specified tags to be a match. Not case sensitive. One tag per line. Wildcards ("?" and "*") are supported but not required.
  The "*" wildcard matches zero or more characters, and "?" matches exactly one character (and that character must be present).

  Wildcard examples:
  Foo* would match Foo, FooBar, and FooBaz, but not BarFoo.
  *Foo* would match the above in addition to BarFoo.
  Foo?Bar would match Foo.Bar and Foo_Bar, but not FooBar.
  Foo? would match Food, but not FooBar or BarFoo.
  Foo??? would match FooBar and FooBaz, but not Foo or Food.
  ?oo? would match Food, but not Foo.
  ?Foo* would match AFooBar, but not FooBar

<a id="unreal.MovieGraphConditionGroupQuery_ActorName"></a>