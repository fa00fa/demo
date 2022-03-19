import ast
import _ast
with open(r'C:\Users\Zz\Desktop\demo\dog.py') as f:
    tree=ast.parse(f.read())
    mname=[i for i in tree.body if isinstance(i,_ast.ClassDef)]
    print mname

