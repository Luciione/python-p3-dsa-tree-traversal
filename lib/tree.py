class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        # Define a depth-first traversal function
        def dfs(node):
            if node.data['id'] == target_id:
                return node

            for child in node.children:
                result = dfs(child)
                if result:
                    return result

        return dfs(self.root)  # Start the traversal from the root node

# Example usage
if __name__ == "__main__":
    root = Tree({
        'tag_name': 'html',
        'id': 'root',
        'text_content': '',
        'children': [
            Tree({
                'tag_name': 'body',
                'id': 'content',
                'text_content': '',
                'children': [
                    Tree({
                        'tag_name': 'div',
                        'id': 'header',
                        'text_content': '',
                        'children': []
                    }),
                    Tree({
                        'tag_name': 'div',
                        'id': 'main',
                        'text_content': '',
                        'children': [
                            Tree({
                                'tag_name': 'h1',
                                'id': 'heading',
                                'text_content': 'Title',
                                'children': []
                            }),
                            Tree({
                                'tag_name': 'p',
                                'id': 'paragraph',
                                'text_content': 'This is a paragraph.',
                                'children': []
                            })
                        ]
                    })
                ]
            })
        ]
    })

    element = root.get_element_by_id('heading')
    if element:
        print(f"Element with id 'heading' found: {element.data}")
    else:
        print("Element not found")
