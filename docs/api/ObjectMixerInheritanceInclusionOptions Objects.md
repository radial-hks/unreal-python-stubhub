## ObjectMixerInheritanceInclusionOptions Objects

```python
class ObjectMixerInheritanceInclusionOptions(EnumBase)
```

EObject Mixer Inheritance Inclusion Options

**C++ Source:**

- **Plugin**: ObjectMixer
- **Module**: ObjectMixerEditor
- **File**: ObjectMixerEditorObjectFilter.h

<a id="unreal.ObjectMixerInheritanceInclusionOptions.NONE"></a>

#### NONE

0: Get only the properties in the specified classes without considering parent or child classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ONLY_IMMEDIATE_PARENT"></a>

#### INCLUDE_ONLY_IMMEDIATE_PARENT

1: Get properties from the class that the specified classes immediately derive from, but not the parents' parents + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ONLY_IMMEDIATE_CHILDREN"></a>

#### INCLUDE_ONLY_IMMEDIATE_CHILDREN

2: Get properties from child classes but not child classes of child classes + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ONLY_IMMEDIATE_PARENT_AND_CHILDREN"></a>

#### INCLUDE_ONLY_IMMEDIATE_PARENT_AND_CHILDREN

3: IncludeOnlyImmediateParent + IncludeOnlyImmediateChildren + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ALL_PARENTS"></a>

#### INCLUDE_ALL_PARENTS

4: Go up the chain of parent classes to get all properties in the specified classes' ancestries + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ALL_CHILDREN"></a>

#### INCLUDE_ALL_CHILDREN

5: Get properties from all derived classes recursively + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ALL_PARENTS_AND_CHILDREN"></a>

#### INCLUDE_ALL_PARENTS_AND_CHILDREN

6: IncludeAllParents + IncludeAllChildren + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ALL_PARENTS_AND_ONLY_IMMEDIATE_CHILDREN"></a>

#### INCLUDE_ALL_PARENTS_AND_ONLY_IMMEDIATE_CHILDREN

7: IncludeAllParents + IncludeOnlyImmediateChildren + Specified Classes

<a id="unreal.ObjectMixerInheritanceInclusionOptions.INCLUDE_ONLY_IMMEDIATE_PARENT_AND_ALL_CHILDREN"></a>

#### INCLUDE_ONLY_IMMEDIATE_PARENT_AND_ALL_CHILDREN

8: IncludeOnlyImmediateParent + IncludeAllChildren + Specified Classes

<a id="unreal.ObjectMixerTreeViewMode"></a>