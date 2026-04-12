## RigVMGraphNotifType Objects

```python
class RigVMGraphNotifType(EnumBase)
```

The Graph Notification Type is used to differentiate
between all of the changes that can happen within a graph.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMNotifications.h

<a id="unreal.RigVMGraphNotifType.GRAPH_CHANGED"></a>

#### GRAPH\_CHANGED

0

<a id="unreal.RigVMGraphNotifType.NODE_ADDED"></a>

#### NODE\_ADDED

1: The graph has changed / a new graph has been picked (Subject == nullptr)

<a id="unreal.RigVMGraphNotifType.NODE_REMOVED"></a>

#### NODE\_REMOVED

2: A node has been added to the graph (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_SELECTED"></a>

#### NODE\_SELECTED

3: A node has been removed from the graph (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_DESELECTED"></a>

#### NODE\_DESELECTED

4: A node has been selected (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_SELECTION_CHANGED"></a>

#### NODE\_SELECTION\_CHANGED

5: A node has been deselected (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_POSITION_CHANGED"></a>

#### NODE\_POSITION\_CHANGED

6: The set of selected nodes has changed (Subject == nullptr)

<a id="unreal.RigVMGraphNotifType.NODE_SIZE_CHANGED"></a>

#### NODE\_SIZE\_CHANGED

7: A node's position has changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_COLOR_CHANGED"></a>

#### NODE\_COLOR\_CHANGED

8: A node's size has changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.PIN_ADDED"></a>

#### PIN\_ADDED

9: A node's color has changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.PIN_REMOVED"></a>

#### PIN\_REMOVED

10: A pin has been added to a given node (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_RENAMED"></a>

#### PIN\_RENAMED

11: A pin has been removed from a given node (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_EXPANSION_CHANGED"></a>

#### PIN\_EXPANSION\_CHANGED

12: A pin has been renamed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_WATCHED_CHANGED"></a>

#### PIN\_WATCHED\_CHANGED

13: A pin's expansion state has changed(Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_ARRAY_SIZE_CHANGED"></a>

#### PIN\_ARRAY\_SIZE\_CHANGED

14: A pin's watch state has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_DEFAULT_VALUE_CHANGED"></a>

#### PIN\_DEFAULT\_VALUE\_CHANGED

15: An array pin's size has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_DIRECTION_CHANGED"></a>

#### PIN\_DIRECTION\_CHANGED

16: A pin's default value has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_TYPE_CHANGED"></a>

#### PIN\_TYPE\_CHANGED

17: A pin's direction has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_INDEX_CHANGED"></a>

#### PIN\_INDEX\_CHANGED

18: A pin's data type has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.LINK_ADDED"></a>

#### LINK\_ADDED

19: A pin's index has changed (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.LINK_REMOVED"></a>

#### LINK\_REMOVED

20: A link has been added (Subject == URigVMLink)

<a id="unreal.RigVMGraphNotifType.COMMENT_TEXT_CHANGED"></a>

#### COMMENT\_TEXT\_CHANGED

21: A link has been removed (Subject == URigVMLink)

<a id="unreal.RigVMGraphNotifType.VARIABLE_ADDED"></a>

#### VARIABLE\_ADDED

22: A comment node's text has changed (Subject == URigVMCommentNode)

<a id="unreal.RigVMGraphNotifType.VARIABLE_REMOVED"></a>

#### VARIABLE\_REMOVED

23: A variable has been added (Subject == URigVMVariableNode)

<a id="unreal.RigVMGraphNotifType.VARIABLE_RENAMED"></a>

#### VARIABLE\_RENAMED

24: A variable has been removed (Subject == URigVMVariableNode)

<a id="unreal.RigVMGraphNotifType.INTERACTION_BRACKET_OPENED"></a>

#### INTERACTION\_BRACKET\_OPENED

25: A variable has been renamed (Subject == URigVMVariableNode)

<a id="unreal.RigVMGraphNotifType.INTERACTION_BRACKET_CLOSED"></a>

#### INTERACTION\_BRACKET\_CLOSED

26: A bracket has been opened (Subject == nullptr)

<a id="unreal.RigVMGraphNotifType.INTERACTION_BRACKET_CANCELED"></a>

#### INTERACTION\_BRACKET\_CANCELED

27: A bracket has been opened (Subject == nullptr)

<a id="unreal.RigVMGraphNotifType.PIN_BOUND_VARIABLE_CHANGED"></a>

#### PIN\_BOUND\_VARIABLE\_CHANGED

28: A bracket has been canceled (Subject == nullptr)

<a id="unreal.RigVMGraphNotifType.NODE_RENAMED"></a>

#### NODE\_RENAMED

29: A pin has been bound or unbound to / from a variable (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.FUNCTION_RENAMED"></a>

#### FUNCTION\_RENAMED

30: A node has been renamed in the graph (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_REFERENCE_CHANGED"></a>

#### NODE\_REFERENCE\_CHANGED

31: A function has been renamed in the graph (Subject == URigVMLibraryNode)

<a id="unreal.RigVMGraphNotifType.NODE_CATEGORY_CHANGED"></a>

#### NODE\_CATEGORY\_CHANGED

32: A node has changed it's referenced function

<a id="unreal.RigVMGraphNotifType.NODE_KEYWORDS_CHANGED"></a>

#### NODE\_KEYWORDS\_CHANGED

33: A node's category has changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.NODE_DESCRIPTION_CHANGED"></a>

#### NODE\_DESCRIPTION\_CHANGED

34: A node's keywords have changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.VARIABLE_REMAPPING_CHANGED"></a>

#### VARIABLE\_REMAPPING\_CHANGED

35: A node's description has changed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.LIBRARY_TEMPLATE_CHANGED"></a>

#### LIBRARY\_TEMPLATE\_CHANGED

36: A function reference node's remapping has changed (Subject == URigVMFunctionReferenceNode)

<a id="unreal.RigVMGraphNotifType.FUNCTION_ACCESS_CHANGED"></a>

#### FUNCTION\_ACCESS\_CHANGED

37: The definition of a library node's template has changed (Subject == URigVMLibraryNode)

<a id="unreal.RigVMGraphNotifType.VARIANT_TAGS_CHANGED"></a>

#### VARIANT\_TAGS\_CHANGED

38: The function has been made public/private (Subject == URigVMLibraryNode)

<a id="unreal.RigVMGraphNotifType.PIN_DISPLAY_NAME_CHANGED"></a>

#### PIN\_DISPLAY\_NAME\_CHANGED

39: The tags in the header of this function variant have changed (Subject == URigVMLibraryNode)

<a id="unreal.RigVMGraphNotifType.PIN_CATEGORY_CHANGED"></a>

#### PIN\_CATEGORY\_CHANGED

40: The display name of a pin has changed - requiring a rebuild of the node user interface (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_CATEGORIES_CHANGED"></a>

#### PIN\_CATEGORIES\_CHANGED

41: The category of a pin has changed - requiring a rebuild of the node user interface (Subject == URigVMPin)

<a id="unreal.RigVMGraphNotifType.PIN_CATEGORY_EXPANSION_CHANGED"></a>

#### PIN\_CATEGORY\_EXPANSION\_CHANGED

42: The category list of a node has changed - requiring a rebuild of the node user interface (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.FUNCTION_VARIANT_GUID_CHANGED"></a>

#### FUNCTION\_VARIANT\_GUID\_CHANGED

43: The category of a pin expanded / collapsed (Subject == URigVMNode)

<a id="unreal.RigVMGraphNotifType.INVALID"></a>

#### INVALID

44: The guid for a function has changed (Subject == URigVMLibraryNode)

<a id="unreal.RigVMTagDisplayMode"></a>