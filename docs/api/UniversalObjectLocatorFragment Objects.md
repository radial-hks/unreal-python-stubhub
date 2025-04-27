## UniversalObjectLocatorFragment Objects

```python
class UniversalObjectLocatorFragment(StructBase)
```

Universal Object Locator (UOL) Fragments provide an extensible mechanism for referencing permanent, transient
  or dynamically created objects relative to an external context. UOLs comprise zero or more nested fragments.

Creation and resolution of a fragment requires a context to be provided;
  normally this will be the object on which the UOL exists as a property.

The way in which the object is referenced is defined by globally registered 'FragmentTypes'
  (See IUniversalObjectLocatorModule::RegisterFragmentType). Each FragmentType can be thought of as somewhat
  equivalent to a www URI fragment type, though the 'path' is not necessarily just a string, but includes
  support for the full set of Engine Property types.

The type is implemented as a type-erased payload block, a fragment type handle and some internal flags.
Payloads will be allocated using the inline memory if alignment and size constraints allow, but
  will fall back to a heap allocation if necessary. Allocation should be avoided by keeping payload
  types small.

Aligned to 8 bytes, 32 (runtime) or 64 (editor) bytes big.

**C++ Source:**

- **Module**: UniversalObjectLocator
- **File**: UniversalObjectLocatorFragment.h

<a id="unreal.UniversalObjectLocatorFragment.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.SharedImageConstRefBlueprint"></a>